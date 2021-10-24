class Solution_2047:
    def countValidWords(self, sentence: str) -> int:
        tokens = sentence.split(" ")
        count = 0
        for token in tokens:
            if len(token.strip()) > 0:
                token = token.strip()
                hyphen = False
                valid = True
                for i, c in enumerate(list(token)):
                    if c.isdigit():
                        valid = False
                        break
                    if c == '-' and (
                            (i == 0 or i == len(token) - 1) or not (token[i - 1].isalpha() and token[i + 1].isalpha())):
                        valid = False
                        break
                    if c == '-':
                        if hyphen:
                            valid = False
                        else:
                            hyphen = True
                    if c in ('!', '.', ',') and i < len(token) - 1:
                        valid = False
                        break
                count += valid
        return count

