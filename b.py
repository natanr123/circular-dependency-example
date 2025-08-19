from __future__ import annotations
from a import A

class B:
    def run(self):
        print("hello from B")

    def run_a(self, a: A):
        a.run()
