class ToolString:

    def __init__(self):
        pass

    def is_palindromo(self, phrase):
        phrase = phrase.replace(" ", "")
        for i in range(len(phrase)):
            if phrase[i] != phrase[-i-1]:
                return False
        return True

    def is_upper(self, phrase):
        return phrase.isupper()
