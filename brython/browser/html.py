#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################

tags = {}


class _Tag:
    _autocomp = None

    def __init__(self, name):
        self.tagName = name


def maketag(name):
    return _Tag(name)
