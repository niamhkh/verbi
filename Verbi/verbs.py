"""
This script contains all the Italian verb data.
"""


class TranslationError(Exception):
    pass


class V_are:
    """
    This class is for verbs that end in -are.
    """
    def __init__(self, body):
        if str(body)[-3:] == "are":
            self.body = str(body)[:-3]
        else:
            self.body = str(body).lower()

    def __str__(self):
        return self.body + "-"

    def __repr__(self):
        return "V_are(" + self.body + "-" + ")"

    def present(self, subject):
        if subject.lower() == "io":
            return self.body + "o"
        elif subject.lower() == "tu":
            return self.body + "i"
        elif subject.lower() in ("lui", "lei"):
            return self.body + "a"
        elif subject.lower() == "noi":
            return self.body + "iamo"
        elif subject.lower() == "voi":
            return self.body + "ete"
        elif subject.lower() == "loro":
            return self.body + "ono"
        else:
            try:
                with open("error_logs/errors.txt", "a") as f:
                    from datetime import date
                    t = str(date.today())
                    s = f"{t} - present - {self.body + 'are'} - {subject.lower()}\n"
                    f.write(s)
            except FileNotFoundError:
                print("It couldn't find errors.txt")
            finally:
                raise TranslationError(f"There is no conjugation for the subject {subject.lower()}")


class V_ire:
    """
    This class is for verbs that end in -ire.
    """
    def __init__(self, body):
        if str(body)[-3:] == "ire":
            self.body = str(body)[:-3]
        else:
            self.body = str(body).lower()

    def __str__(self):
        return self.body + "-"

    def __repr__(self):
        return "V_ire(" + self.body + "-" + ")"

    def present(self, subject):
        if subject.lower() == "io":
            return self.body + "o"
        elif subject.lower() == "tu":
            return self.body + "i"
        elif subject.lower() in ("lui", "lei"):
            return self.body + "e"
        elif subject.lower() == "noi":
            return self.body + "iamo"
        elif subject.lower() == "voi":
            return self.body + "ete"
        elif subject.lower() == "loro":
            return self.body + "ono"
        else:
            try:
                with open("error_logs/errors.txt", "a") as f:
                    from datetime import date
                    t = str(date.today())
                    s = f"{t} - present - {self.body + 'ire'} - {subject.lower()}\n"
                    f.write(s)
            except FileNotFoundError:
                print("It couldn't find errors.txt")
            finally:
                raise TranslationError(f"There is no conjugation for the subject {subject.lower()}")


class V_ere:
    """
    This class is for verbs that end in -ere.
    """
    def __init__(self, body):
        if str(body)[-3:] == "ere":
            self.body = str(body)[:-3]
        else:
            self.body = str(body).lower()

    def __str__(self):
        return self.body + "-"

    def __repr__(self):
        return "V_ere(" + self.body + "-" + ")"

    def present(self, subject):
        if subject.lower() == "io":
            return self.body + "o"
        elif subject.lower() == "tu":
            return self.body + "i"
        elif subject.lower() in ("lui", "lei"):
            return self.body + "e"
        elif subject.lower() == "noi":
            return self.body + "iamo"
        elif subject.lower() == "voi":
            return self.body + "ete"
        elif subject.lower() == "loro":
            return self.body + "ono"
        else:
            try:
                with open("error_logs/errors.txt", "a") as f:
                    from datetime import date
                    t = str(date.today())
                    s = f"{t} - present - {self.body + 'ere'} - {subject.lower()}\n"
                    f.write(s)
            except FileNotFoundError:
                print("It couldn't find errors.txt")
            finally:
                raise TranslationError(f"There is no conjugation for the subject {subject.lower()}")


def create_verb(verb):
    if verb.lower()[-3:] == "are":
        return V_are(verb)
    elif verb.lower()[-3:] == "ire":
        return V_ire(verb)
    elif verb.lower()[-3:] == "ere":
        return V_ere(verb)
    else:
        return TranslationError(f"{verb} does not end in -are, -ire, or -ere.")


if __name__ == "__main__":
    v1 = create_verb("ascoltare")
    print(v1)

    v2 = create_verb("dormire")
    print(v2.present('lui'))
