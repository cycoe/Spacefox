import os
import re


print("install tiles for original df...")
os.system("sudo cp -r ./data/art/* /home/cycoe/.dwarffortress/data/art")
os.system("sudo cp -r ./data/init/* /home/cycoe/.dwarffortress/data/init")
os.system("sudo cp -r ./raw/objects/* /home/cycoe/.dwarffortress/raw/objects")
os.system("sudo cp -r ./raw/graphics/* /home/cycoe/.dwarffortress/raw/graphics")


print("install tiles for twbt...")
os.system("sudo cp -r ./data/twbt_art/* /home/cycoe/.dwarffortress/data/art")
os.system("sudo cp -r ./data/twbt_init/* /home/cycoe/.dwarffortress/data/init")
os.system("sudo cp -r ./raw/twbt_objects/* /home/cycoe/.dwarffortress/raw/objects")
os.system("sudo cp -r ./raw/twbt_graphics/* /home/cycoe/.dwarffortress/raw/graphics")

onLoad = None
files = os.listdir('.')
for file in files:
    if re.match('onLoad.+', file):
        onLoad = file
        break

os.system("sudo cp -r ./{} /home/cycoe/.dwarffortress/raw/".format(onLoad))


print("install tiles for saves...")
for save in os.listdir('/home/cycoe/.dwarffortress/data/save'):
    if os.path.exists('/home/cycoe/.dwarffortress/data/save/{}/raw'.format(save)):
        os.system("sudo cp -r ./raw/objects/* /home/cycoe/.dwarffortress/data/save/{}/raw/objects".format(save))
        os.system("sudo cp -r ./raw/graphics/* /home/cycoe/.dwarffortress/data/save/{}/raw/graphics".format(save))
        os.system("sudo cp -r ./raw/twbt_objects/* /home/cycoe/.dwarffortress/data/save/{}/raw/objects".format(save))
        os.system("sudo cp -r ./raw/twbt_graphics/* /home/cycoe/.dwarffortress/data/save/{}/raw/graphics".format(save))
