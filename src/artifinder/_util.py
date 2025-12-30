import pathlib

import click

from qiime2.sdk.result import Result
from qiime2.core.archive.provenance_lib import ProvDAG

from ._version import __version__ as artifinder_version

@click.group()
def cli():
    """artifinder: a utility for rachis research data management"""
    pass

@cli.command()
@click.argument('search_dir',
                type=click.Path(exists=True, file_okay=False, dir_okay=True,
                                path_type=pathlib.Path))
@click.argument('target_result_fp',
                type=click.Path(exists=True, file_okay=True, dir_okay=False,
                                path_type=pathlib.Path))
@click.option('--verbose/--no-verbose', default=False, help='Verbose output')
@click.option('--include-targets', is_flag=True, default=False,
              help='Include target information.')
@click.option('--include-results-not-found', is_flag=True, default=False,
              help='Include results that were not found.')
def provenance(search_dir, target_result_fp, verbose, include_targets,
               include_results_not_found):
    """
    Find and identify rachis `Results` used in generating the target `Result`.

    SEARCH_DIR: Directory to search for `Results`

    TARGET_RESULT_FP: Path to target `Result`

    """
    target_uuids, found_uuids, unfound_uuids = _provenance_search(
        search_dir, target_result_fp, verbose)

    if include_targets:
        print('Target Result(s):')
        for target_uuid, (type, path) in target_uuids.items():
            print(f' * {target_uuid}')
            print(f'  * {type}')
            print(f'  * {path}')
            print('')

    print('Found `Results`:')
    for uuid, (type, path) in found_uuids.items():
        if uuid in target_uuids:
            continue
        print(f' * {uuid}')
        print(f'  * {type}')
        print(f'  * {path}')
        print('')

    if include_results_not_found:
        print('\n`Results` not found:')
        for uuid, type in unfound_uuids.items():
            print(f' * {uuid}')
            print(f'  * {type}')
            print('')

    print('')
    print('---')
    print(f'Run with `artifinder` version: {artifinder_version}')

def _provenance_search(search_dir, target_result_fp, verbose):
    target_uuids = {}
    target = Result.peek(target_result_fp)
    target_uuids[target.uuid] = (target.type, target_result_fp.absolute())

    if verbose:
        print("Parsing target's provenance...")
    prov_dag = ProvDAG(target_result_fp, verbose=verbose)

    if verbose:
        print("Scanning search path for .qza and .qzv files...")
    fps = list(search_dir.glob('**/*.qz[av]'))

    if verbose:
        print(f"Found {len(fps)} Results in search directory. "
              "Will now cross-reference those against the target's "
              "provenance.")

    observed_uuids = {
        Result.peek(fp).uuid: fp.absolute() for fp in fps}

    found_uuids = {}
    unfound_uuids = {}

    for n in prov_dag.collapsed_view:
        node_data = prov_dag.get_node_data(n)
        node_type = node_data.type
        if n in observed_uuids:
            found_uuids[n] = (node_type, observed_uuids[n])
        else:
            unfound_uuids[n] = node_type

    return target_uuids, found_uuids, unfound_uuids
