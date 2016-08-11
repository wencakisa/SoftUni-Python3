import os

import json
import yaml


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
            for line in json.load(f):
                yield line


class YAMLoader(Loader):
    def load_data(self):
        with open(self.filename) as f:
            for line in yaml.load(f):
                yield line
