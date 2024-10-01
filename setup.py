# ----------------------------------------------------------------------------
# Copyright (c) 2024, Greg Caporaso.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

description = ("A template QIIME 2 plugin.")

setup(
    name="artifinder",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="Greg Caporaso",
    author_email="greg.caporaso@nau.edu",
    description=description,
    url="https://cap-lab.bio",
    entry_points={
        "qiime2.plugins": [
            "artifinder="
            "artifinder"
            ".plugin_setup:plugin"]
    },
    package_data={
        "artifinder": ["citations.bib"],
        "artifinder.tests": ["data/*"],
    },
    zip_safe=False,
)
