#!/usr/bin/env python3
"""Print each sentence's midpoint second from timing.json, comma-separated, for `hyperframes check --at`.

Usage: midpoints.py <timing.json>
"""
import json, sys

print(",".join(f"{(s['start'] + s['end']) / 2:.2f}" for s in json.load(open(sys.argv[1]))["sentences"]))
