import os
import sys

from json import load as load_json
from json.decoder import JSONDecodeError

from yaml import load as load_yaml, YAMLError


class Loader:
    def __init__(self, filename):
        if not os.access(filename, os.R_OK) or not os.path.isfile(filename):
            raise ValueError('Inaccessible file: {}'.format(filename))

        self.filename = filename

    def load_data(self):
        raise NotImplementedError()


class JSONLoader(Loader):
    def load_data(self):
        with open(self.filename) as f:
            try:
                return load_json(f)
            except JSONDecodeError as jde:
                print('Failed to parse JSON: {}'.format(str(jde)))
                sys.exit(2)


class YAMLoader(Loader):
    def load_data(self):
        with open(self.filename) as f:
            try:
                return load_yaml(f)
            except YAMLError as ye:
                print('Failed to parse YAML: {}'.format(str(ye)))
                sys.exit(2)
