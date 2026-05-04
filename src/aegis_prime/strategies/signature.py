import re
from abc import ABC, abstractmethod

from aegis_prime.parsing.signature.normalizer import Normalizer
from aegis_prime.parsing.signature.pattern import PatternExtractor
from aegis_prime.parsing.signature.extractor import AssertionExtractor
from aegis_prime.parsing.signature.tokenizer import Tokenizer

class SignatureStrategy(ABC):
    @abstractmethod
    def generate(self, message: str) -> str:
        pass


class DefaultSignatureStrategy(SignatureStrategy):

    def __init__(self):
        self.extractor = AssertionExtractor()
        self.tokenizer = Tokenizer()
        self.normalizer = Normalizer()
        self.pattern_extractor = PatternExtractor()

    def generate(self, message: str) -> str:
        assertion = self.extractor.extract(message)

        if not assertion:
            return "other:"

        ast = self.tokenizer.tokenize(assertion.raw)

        pattern = self.pattern_extractor.extract(ast)
        normalized = self.normalizer.normalize(ast)

        return f"{pattern.value}:{normalized}"