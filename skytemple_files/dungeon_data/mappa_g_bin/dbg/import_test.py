#  Copyright 2020-2021 Parakoopa and the SkyTemple Contributors
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
import os

from ndspy.rom import NintendoDSRom

from skytemple_files.dungeon_data.mappa_g_bin.handler import MappaGBinHandler

output_dir = os.path.join(os.path.dirname(__file__), 'dbg_output')
base_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..')
os.makedirs(output_dir, exist_ok=True)

rom = NintendoDSRom.fromFile(os.path.join(base_dir, 'skyworkcopy_us.nds'))

mappa_bin = rom.getFileByName('BALANCE/mappa_gs.bin')
mappa = MappaGBinHandler.deserialize(mappa_bin)

mappa_after_bin = MappaGBinHandler.serialize(mappa)

with open('/tmp/before.bin', 'wb') as f:
    f.write(mappa_bin)

with open('/tmp/after.bin', 'wb') as f:
    f.write(mappa_after_bin)

mappa_after = MappaGBinHandler.deserialize(mappa_after_bin)
for i_fl in range(0, len(mappa.floor_lists)):
    assert len(mappa.floor_lists[i_fl]) == len(mappa_after.floor_lists[i_fl])
    for i in range(0, len(mappa.floor_lists[i_fl])):
        assert mappa.floor_lists[i_fl][i].layout == mappa_after.floor_lists[i_fl][i].layout
assert mappa == mappa_after
