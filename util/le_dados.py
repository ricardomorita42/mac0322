#!/usr/bin/env python
# -*- coding: utf-8 -*-



with open("dados.txt","r") as f:
    content = f.readlines()

content = [x.strip("\n") for x in content]
content = [float(x) for x in content]

print content
