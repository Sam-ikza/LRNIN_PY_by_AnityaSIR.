# two guard problm

from abc import ABC, abstractmethod


# =========================
# LOGIC GATE
# =========================

class LogicGate:

    def NOT(self, a):
        return 1 - a


# =========================
# ABSTRACT GUARD CLASS
# =========================

class Guard(ABC):

    @abstractmethod
    def answer(self):
        pass


# =========================
# TRUTHFUL GUARD
# =========================

class TruthfulGuard(Guard):

    def answer(self):

        # Other guard is a liar.
        # Liar points to Forest.

        return 0


# =========================
# LYING GUARD
# =========================

class LyingGuard(Guard):

    def answer(self):

        # Other guard tells truth.
        # Truthful guard points to City.
        # Lying guard says Forest.

        return 0


# =========================
# PRISONER CLASS
# =========================

class Prisoner:

    def __init__(self, name):

        self.name = name
        self.gate = LogicGate()

    def escape(self, guard):

        print("Prisoner:", self.name)

        print("Question: ")
        print("If I ask the other guard which way goes to City?")

        # Polymorphism
        answer = guard.answer()

        print("Guard says:", answer)

        # NOT gate
        direction = self.gate.NOT(answer)

        if direction == 1:

            print("NOT gate output:", direction)
            print("Prisoner goes to City")
            print("Prisoner escaped!")

        else:

            print("NOT gate output:", direction)
            print("Prisoner goes to Forest")


# =========================
# MAIN PROGRAM
# =========================

truthful_guard = TruthfulGuard()
lying_guard = LyingGuard()

prisoner = Prisoner("John")


print("---- Asking Truthful Guard ----")
prisoner.escape(truthful_guard)


print("\n---- Asking Lying Guard ----")
prisoner.escape(lying_guard)