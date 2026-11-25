#!/usr/bin/env python3
"""Entry program for news-image-20261125.

Validates the bundled entry.png (PNG signature, at most 1 MiB,
at most 1024x1024 px) and writes it byte-identically to
/output/entry.png (or MAKEFUN_OUTPUT_DIR when set).

Python 3.13, standard library only, no network. Deterministic:
the same bytes are written on every run.
"""
import os
import struct
import sys
from pathlib import Path

MAX_BYTES = 1_048_576
MAX_DIM = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.is_file():
        fail(f"entry.png not found next to main.py ({src})")

    data = src.read_bytes()
    if len(data) > MAX_BYTES:
        fail(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    if len(data) < 33 or data[:8] != PNG_SIGNATURE:
        fail("entry.png is not a valid PNG (bad signature)")

    # IHDR: 4-byte length, "IHDR", then width and height as big-endian u32.
    if data[12:16] != b"IHDR":
        fail("entry.png has no IHDR chunk where expected")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        fail(f"entry.png is {width}x{height}, over the 1024x1024 limit")
    if width == 0 or height == 0:
        fail("entry.png has a zero dimension")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.png"
    out_path.write_bytes(data)
    print(f"wrote {out_path} ({len(data)} bytes, {width}x{height})")


if __name__ == "__main__":
    main()
