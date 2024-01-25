#!/usr/bin/python3
import importlib.util
import os


def main():
    # Télécharger le fichier .pyc
    curl_command = "curl -Lso 'hidden_4.pyc' 'https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc'"
    os.system(curl_command)

    # Charger le module compilé
    module_name = "hidden_4"
    module_spec = importlib.util.spec_from_file_location(module_name, "./hidden_4.pyc")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    # Afficher les noms qui ne commencent pas par '__'
    for name in dir(module):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
