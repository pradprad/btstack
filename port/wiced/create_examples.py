#!/usr/bin/env python
#
# Create project files for all BTstack embedded examples in WICED/apps/btstack

import os
import shutil
import sys
import time
import subprocess

mk_template = '''#
# BTstack example 'EXAMPLE' for WICED port
#
# Generated by TOOL
# On DATE

NAME := EXAMPLE

GLOBAL_INCLUDES += .

$(NAME)_SOURCES := ../../../libraries/btstack/example/embedded/EXAMPLE.c
$(NAME)_COMPONENTS += btstack/port/wiced
'''

gatt_update_template = '''#!/bin/sh
DIR=`dirname $0`
BTSTACK_ROOT=$DIR/../../../libraries/btstack
echo "Creating EXAMPLE.h from EXAMPLE.gatt"
$BTSTACK_ROOT/tool/compile-gatt.py $BTSTACK_ROOT/example/embedded/EXAMPLE.gatt $DIR/EXAMPLE.h
'''

# get script path
script_path = os.path.abspath(os.path.dirname(sys.argv[0]))

# validate WICED root by reading version.txt
wiced_root = script_path + "/../../../../"
wiced_version = ""
try:
    with open(wiced_root + 'version.txt', 'r') as fin:
        wiced_version = fin.read()  # Read the contents of the file into memory.
except:
    pass
if not "WICED Version" in wiced_version:
    print("Cannot find WICED root. Make sure BTstack is checked out in WICED-SDK-X/libraries")
    sys.exit(1)

# show WICED version
print("Found %s" % wiced_version)

# path to examples
examples_embedded = script_path + "/../../example/embedded/"

# path to WICED/apps/btstack
apps_btstack = wiced_root + "/apps/btstack/"

print("Creating examples in apps/btstack:")

# iterate over btstack examples
for file in os.listdir(examples_embedded):
    if not file.endswith(".c"):
        continue
    example = file[:-2]

    # create folder
    apps_folder = apps_btstack + example + "/"
    if not os.path.exists(apps_folder):
        os.makedirs(apps_folder)

    # create .mk file
    with open(apps_folder + example + ".mk", "wt") as fout:
        fout.write(mk_template.replace("EXAMPLE", example).replace("TOOL", script_path).replace("DATE",time.strftime("%c")))

    # create update_gatt.sh if .gatt file is present
    gatt_path = examples_embedded + example + ".gatt"
    if os.path.exists(gatt_path):
        update_gatt_script = apps_folder + "update_gatt_db.sh"
        with open(update_gatt_script, "wt") as fout:
            fout.write(gatt_update_template.replace("EXAMPLE", example))        
        os.chmod(update_gatt_script, 0o755)
        subprocess.call(update_gatt_script + "> /dev/null", shell=True)
        print("- %s including compiled GATT DB" % example)
    else:
        print("- %s" % example)
