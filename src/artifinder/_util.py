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
@click.option('--verbose/--no-verbose', default=True, help='Verbose output')
@click.option('--report-target/--no-report-target', is_flag=True, default=True,
              help='Report target details.')
@click.option('--report-missing/--no-include-missing', is_flag=True,
              default=True,
              help='Report results that were not found in search dir.')
def prov(search_dir, target_result_fp, verbose, report_target,
         report_missing):
    """
    Find `Results` referenced in the target's provenance.

    SEARCH_DIR: Directory to search for `Results`

    TARGET_RESULT_FP: Path to target `Result`

    """
    target_uuids, found_uuids, unfound_uuids = _provenance_search(
        search_dir, target_result_fp, verbose)

    if report_target:
        print('Target `Result`:')
        for target_uuid, (type, path) in target_uuids.items():
            print(f'{target_uuid}\t{type}\t{path}')
        print('')

    print('Found `Results`:')
    for uuid, (type, path) in found_uuids.items():
        print(f'{uuid}\t{type}\t{path}')
    print('')

    if report_missing:
        print('`Results` not found:')
        for uuid, type in unfound_uuids.items():
            print(f'{uuid}\t{type}')
        print('')

def _provenance_search(search_dir, target_result_fp, verbose):
    target_uuids = {}
    target = Result.peek(target_result_fp)
    target_uuids[target.uuid] = (target.type, target_result_fp.absolute())

    if verbose:
        print(f'`artifinder` version: {artifinder_version}')
        print('')

    if verbose:
        print("Scanning search path for .qza and .qzv files...")
    fps = list(search_dir.glob('**/*.qz[av]'))

    if verbose:
        print(f"Found {len(fps)} `Results` in search directory. ")
        print("")

    if verbose:
        print("Parsing target's provenance...")
    prov_dag = ProvDAG(target_result_fp, verbose=verbose)

    observed_uuids = {
        Result.peek(fp).uuid: fp.absolute() for fp in fps}

    found_uuids = {}
    unfound_uuids = {}
    count_provenance_uuids = 0

    for n in prov_dag.collapsed_view:
        if n in target_uuids:
            continue
        node_data = prov_dag.get_node_data(n)
        node_type = node_data.type
        count_provenance_uuids += 1
        if n in observed_uuids:
            found_uuids[n] = (node_type, observed_uuids[n])
        else:
            unfound_uuids[n] = node_type

    if verbose:
        print(f"Found {count_provenance_uuids} `Results` in target's "
              "provenance (not including target).")
        print(f" * {len(found_uuids)} were found in the search directory.")
        print(f" * {len(unfound_uuids)} were not found in the search "
              "directory.")
        print("")

    return target_uuids, found_uuids, unfound_uuids
