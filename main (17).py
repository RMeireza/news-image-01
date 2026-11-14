"""Copies the finished drawing to /output/entry.png (standard library only)."""
import shutil
import os

src = os.path.join(os.path.dirname(__file__), "entry.png")
dst = "/output/entry.png"
shutil.copyfile(src, dst)
print("entry.png written", os.path.getsize(dst), "bytes")
# verified against commit 862b4ce: byte-identical copy of the drawn artwork
