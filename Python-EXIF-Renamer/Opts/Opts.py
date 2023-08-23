import sys
import os
import getopt

class Opts:
    
    def __init__(self, shortopts, longopts):
        self.__options = {}
        sopts, lopts = self.parseOpts(shortopts, longopts)
        self.getOpts(sopts, lopts)
        
    def parseOpts(self):
        shortopts = "h?"
        longopts = ["help", "revert"]

    def getOpts(self, shortopts, longopts):
        for longopt in longopts:
            self.__options__.update({longopt: False})

        def shortHelp():
            usage_string = "Usage:  <project_folder> "
            for shortopt in shortopts:
                usage_string += "-" + shortopt + " "
            for longopt in longopts:
                usage_string += "--" + longopt + " "
            usage_string.rstrip() # remove hanging space
            print(usage_string)

        # def longHelp():
        #     shortHelp()
        #     with open(r".\longhelp.txt") as longhelp:
        #         print(longhelp.read())

        # DEV print out sys.argv
        # for i in range(len(sys.argv)):
        #     print(i, ": ", sys.argv[i])
        # print(len(sys.argv))
        argv_start = 1
        project_folder = os.getcwd()
        if len(sys.argv) < 2: # if no args passed (sys.argv[0] is the script path and provided automatically)
            project_folder = os.getcwd()
            argv_start = 1
        if len(sys.argv) > 1: # if args passed
            if os.path.isdir(sys.argv[1]): # check if first one is a folder
                project_folder = sys.argv[1]
                argv_start = 2
            elif not os.path.isdir(sys.argv[1]): # if first one is not a folder
                project_folder = os.getcwd()
                if sys.argv[1].startswith('-'): # check if first one is an option
                    argv_start = 1
        try:
            opts, args = getopt.getopt(sys.argv[argv_start:], shortopts, longopts)
        except getopt.GetoptError as e:
            print(str(e).capitalize())
            shortHelp()
            sys.exit()

        # set flags/call funcs from opts passed on command line
        for opt, arg in opts:
            if opt in "--help":
                # longHelp()
                sys.exit()
            elif opt in ["-h", "-?"]:
                shortHelp()
                sys.exit()
            elif opt.strip("--") in longopts:  # set True in the options dict any long options found on the command line input
                    options[opt.strip("--")] = True
            else:
                shortHelp()
        if not opts and args:
            shortHelp()
            sys.exit()

        return project_folder