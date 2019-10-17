#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Read_JSON(object):

    def read(self, name_of_file):
        file = name_of_file + ".json"

        try:
            with open(file) as f:
                d = json.load(f)

            return d
        except Exception as e:
            print("Erro ao ler o arquivo")
            print(str(e))

        return None