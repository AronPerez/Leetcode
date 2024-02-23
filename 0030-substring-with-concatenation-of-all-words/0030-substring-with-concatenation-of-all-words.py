class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_freq = {}
        for word in words:
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1

        total_words = len(words)
        word_length = len(words[0])
        total_length = total_words * word_length

        result = []
        for i in range(len(s) - total_length + 1):
            window = s[i:i + total_length]
            window_freq = {}
            for j in range(0, total_length, word_length):
                word = window[j:j + word_length]
                if word not in window_freq:
                    window_freq[word] = 0
                window_freq[word] += 1

            if window_freq == word_freq:
                result.append(i)

        return result

        