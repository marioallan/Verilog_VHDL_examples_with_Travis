# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2020, Lars Asplund lars.anders.asplund@gmail.com

"""
VHDL UART
---------
A more realistic test bench of an UART to show VUnit VHDL usage on a
typical module.
"""

from pathlib import Path
from vunit import VUnit

VU = VUnit.from_argv()
VU.add_osvvm()
VU.add_verification_components()

SRC_PATH = Path(__file__).parent 

VU.add_library("neander_lib").add_source_files(SRC_PATH / "src" / "*.vhd")
VU.add_library("tb_neander_lib").add_source_files(SRC_PATH / "test" / "*.vhd")

VU.main()
