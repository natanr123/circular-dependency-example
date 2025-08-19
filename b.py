from __future__ import annotations
# from a import A # this will cause a circular dependency exception
import a

class B:
    def run(self):
        print("hello from B")

    def run_a(self, a: a.A):
        a.run()
