#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_default

if __name__ == "__main__":

    builder = build_template_default.get_builder(build_types=["Release", "Debug"], archs=["x86_64"])
    builder.run()
