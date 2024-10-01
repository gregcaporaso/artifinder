# ----------------------------------------------------------------------------
# Copyright (c) 2024, Greg Caporaso.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Citations, Plugin
from artifinder import __version__

citations = Citations.load("citations.bib", package="artifinder")

plugin = Plugin(
    name="artifinder",
    version=__version__,
    website="https://cap-lab.bio",
    package="artifinder",
    description="Tooling for Q2-based Research Data Management.",
)
