class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        check = False
        Temporary = ""

        for strings in source:
            i = 0
            if not check:
                Temporary = ""

            while i < len(strings):
                if not check and i+1 < len(strings) and strings[i:i+2] == "/*":
                    check = True
                    i += 2
                elif check and i+1 < len(strings) and strings[i:i+2] == "*/":
                    check = False
                    i += 2
                elif not check and i+1 < len(strings) and strings[i:i+2] == "//":
                    break
                elif not check:
                    Temporary += strings[i]
                    i += 1
                else:
                    i += 1

            if not check and Temporary:
                result.append(Temporary)

        return result
