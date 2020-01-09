import os

from PIL import Image
from bitstring import BitStream
from ndspy.rom import NintendoDSRom

from skytemple_files.graphics.kao.handler import KaoHandler

dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..')

rom = NintendoDSRom.fromFile(os.path.join(dir, 'skyworkcopy.nds'))

kao_data = rom.getFileByName('FONT/kaomado.kao')
kao = KaoHandler.deserialize(BitStream(kao_data))
#kao.get(427, 0).get().show()
with open(os.path.join(dir, 'kaomado.kao'), 'wb') as f:
    f.write(kao_data)

with open('/tmp/new.png', 'rb') as f:
    i = Image.open(f)
    kao.get(427, 0).set(i)
    kao.get(427, 2).set(i)

kao_data_new = KaoHandler.serialize(kao)
#kao.get(427, 0).get().show()
rom.setFileByName('FONT/kaomado.kao', kao_data_new.bytes)
with open(os.path.join(dir, 'kaomado_edit.kao'), 'wb') as f:
    f.write(kao_data_new.bytes)
rom.saveToFile(os.path.join(dir, 'skyworkcopy_edit.nds'))

# Test
kao_data = rom.getFileByName('FONT/kaomado.kao')
kao = KaoHandler.deserialize(BitStream(kao_data))
kao.get(427, 0).get().show()
kao.get(427, 2).get().show()

os.system(f'xxd {os.path.join(dir, "kaomado.kao")} > {os.path.join(dir, "kaomado.kao.hex")}')
os.system(f'xxd {os.path.join(dir, "kaomado_edit.kao")} > {os.path.join(dir, "kaomado_edit.kao.hex")}')

# Sanity check: Open ROM again and also dump the file again
rom = NintendoDSRom.fromFile(os.path.join(dir, 'skyworkcopy_edit.nds'))
kao_data_new2 = rom.getFileByName('FONT/kaomado.kao')
with open(os.path.join(dir, 'kaomado_edit_second.kao'), 'wb') as f:
    f.write(kao_data_new2)
os.system(f'xxd {os.path.join(dir, "kaomado_edit_second.kao")} > {os.path.join(dir, "kaomado_edit_second.kao.hex")}')
