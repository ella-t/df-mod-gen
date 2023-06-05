class DFRaw:
    def __init__(self, path, filename, rawtype):
        self.file = open(path + filename + ".txt", "w")
        self.file.write(filename + "\n\n[OBJECT:" + rawtype + "]\n")

    def writetoken(self, token, arg = None):
        if arg is None:
            self.file.write("\n[" + token + "]")
        else:
            self.file.write("\n[" + token + ":" + arg + "]")

    def finishraw(self):
        self.file.close()

    def newline(self):
        self.file.write("\n")
