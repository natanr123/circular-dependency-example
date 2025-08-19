from __future__ import annotations
import b

class A:
    def run(self):
        print("hello from A")

    def run_b(self, b: b.B):
        b.run()

