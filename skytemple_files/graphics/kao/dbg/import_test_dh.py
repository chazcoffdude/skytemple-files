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

with open(os.path.join(dir, 'dh', 'new427.png'), 'rb') as f:
    i = Image.open(f)
    kao.get(427, 0).set(i)
    kao.get(427, 2).set(i)

with open(os.path.join(dir, 'dh', 'new051.png'), 'rb') as f:
    i = Image.open(f)
    kao.get(51, 0).set(i)
    kao.get(51, 2).set(i)

with open(os.path.join(dir, 'dh', 'new000.png'), 'rb') as f:
    i = Image.open(f)
    kao.get(0, 0).set(i)
    kao.get(0, 2).set(i)

with open(os.path.join(dir, 'dh', 'new003.png'), 'rb') as f:
    i = Image.open(f)
    kao.get(3, 0).set(i)
    kao.get(3, 2).set(i)

with open(os.path.join(dir, 'dh', 'new151.png'), 'rb') as f:
    i = Image.open(f)
    kao.get(151, 0).set(i)
    kao.get(151, 2).set(i)

with open(os.path.join(dir, 'dh', 'new024.png'), 'rb') as f:
    i = Image.open(f)
    kao.get(24, 0).set(i)
    kao.get(24, 2).set(i)

kao_data_new = KaoHandler.serialize(kao)
#kao.get(427, 0).get().show()
rom.setFileByName('FONT/kaomado.kao', kao_data_new.bytes)
with open(os.path.join(dir, 'kaomado_edit.kao'), 'wb') as f:
    f.write(kao_data_new.bytes)

with open(os.path.join(dir, 'dh', 'text_e.str'), 'rb') as f:
    rom.setFileByName('MESSAGE/text_e.str', f.read())

rom.saveToFile(os.path.join(dir, 'skyworkcopy_edit.nds'))

# Test
kao_data = rom.getFileByName('FONT/kaomado.kao')
kao = KaoHandler.deserialize(BitStream(kao_data))
kao.get(427, 0).get().show()
kao.get(51, 0).get().show()
kao.get(0, 0).get().show()
kao.get(3, 0).get().show()
kao.get(151, 0).get().show()
kao.get(24, 0).get().show()
