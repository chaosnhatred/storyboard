#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Darcy Liu on 2012-04-11.
Copyright (c) 2012 Close To U. All rights reserved.
"""

from django.contrib import admin
from models import *

admin.site.register(Minisite)
admin.site.register(Page)
