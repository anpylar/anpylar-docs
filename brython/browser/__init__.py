#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
import builtins
import sys

# Mock-up some of the brython structures which are imported / partially used
# in AnPyLar so that importing for the documentation works


class Document:
    window = None
    body = None
    head = None


class Window:
    def eval(self, *args, **kwargs):
        pass


class DOMNodeDict:
    tags = {}
    select_one = None
    select = None


class Imported:
    def __getattr__(self, name):
        return sys.modules[name]


class Brython:
    DOMNodeDict = DOMNodeDict()
    imported = Imported()
    win = Window()


document = Document()
window = Window()


builtins.__BRYTHON__ = B = Brython()
window.__BRYTHON__ = B
