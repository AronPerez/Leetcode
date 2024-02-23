class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_freq = Counter(words)
        word_size = len(words[0])
        total_words = len(words)
        total_size = word_size * total_words

        result = []

        for i in range(len(s) - total_size + 1):
            window = s[i:i + total_size]
            window_freq = Counter()

            for j in range(0, total_size, word_size):
                word = window[j:j + word_size]
                window_freq[word] += 1

            if window_freq == word_freq:
                result.append(i)

        return result


        