# Glossary
# T: DTag size
# N: Fragment Compressed Number (FCN) size
# M: Window identifier (present only if windows are used) size
# U: Reassembly Check Sequence (RCS) size


class Header:
    profile = None

    RULE_ID = ""
    DTAG = ""
    W = ""
    FCN = ""
    RCS = ""
    C = ""
    COMPRESSED_BITMAP = ""

    string = ""

    def __init__(self, profile, rule_id, dtag, w, fcn, c=""):  # rule_id is arbitrary, as it's not applicable for F/R

        self.profile = profile

        direction = profile.direction

        if direction == "DOWNLINK":
            self.FCN = ""
            self.C = c

        if len(rule_id) != profile.RULE_ID_SIZE:
            print('RULE must be of length RULE_ID_SIZE')
        else:
            self.RULE_ID = rule_id

        if profile.T == "0":
            self.DTAG = ""
        elif len(dtag) != profile.T:
            print('DTAG must be of length T')
        else:
            self.DTAG = dtag

        if len(w) != profile.WINDOW_SIZE:
            print('W must be of length WINDOW_SIZE')
        else:
            self.W = w

        if fcn != "":
            if len(fcn) != profile.N:
                print('FCN must be of length N')
            else:
                self.FCN = fcn

        self.string = "".join([self.RULE_ID, self.DTAG, self.W, self.FCN, self.C])  # self.C ?

    def test(self):

        print("HEADER:")
        print(self.string)

        if len(self.string) != self.profile.HEADER_LENGTH:
            print('The header has not been initialized correctly.')
