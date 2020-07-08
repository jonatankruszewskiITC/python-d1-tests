import os
import shutil


def delete_folder():
    location = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk(location):
        for name in files:
            if name == 'requirements.txt':
                os.remove((os.path.join(root, name)))
        for name in dirs:
            if name == 'venv':
                shutil.rmtree((os.path.join(root, name)))


delete_folder()
