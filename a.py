from __future__ import annotations
from b import B

class A:
    def run(self):
        print("hello from A")


    def run_b(self, b: B):
        b.run()

