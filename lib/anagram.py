class Anagram:
	"""Detects anagrams for a given word.

	Usage:
		a = Anagram("listen")
		a.match(["enlist", "google"])  # -> ["enlist"]
	"""

	def __init__(self, word: str):
		self.word = word
		# Precompute a sorted representation for fast comparison
		self._signature = self._signature_of(word)

	@staticmethod
	def _signature_of(word: str) -> str:
		return "".join(sorted(word))

	def match(self, candidates):
		"""Return a list of candidates that are anagrams of the initialized word.

		The order of returned matches follows the order in `candidates`.
		"""
		matches = []
		for cand in candidates:
			if self._signature == self._signature_of(cand):
				matches.append(cand)
		return matches