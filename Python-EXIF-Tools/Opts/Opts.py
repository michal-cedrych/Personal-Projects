import os
import sys
import getopt

class Opts:
    
    __SHORTOPT_LEADER = '-'
    __LONGOPT_LEADER = "--"
    __SHORTOPT_FOLLOWER = ':'
    __LONGOPT_FOLLOWER = '='
    __SHORTOPTS_HELP = "h?"
    __LONGOPTS_HELP = ["help"]
    __PATHCHARS = ".\\"
    short_opts = {}
    long_opts = {}
    args = []
    script_name = ""
    
    def __init__(self, shortopts_options, longopts_options, longhelp_text="longhelp"):
        shortopts_options = self.__SHORTOPTS_HELP + shortopts_options
        longopts_options = self.__LONGOPTS_HELP + longopts_options
        self.__shortopts_options_parsed, self.__longopts_options_parsed = self.parse_options(shortopts_options, longopts_options)
        self.__longhelp_text = longhelp_text
        self.script_name = self.get_script_name()
        print("shortopts_options", shortopts_options)
        print("longopts_options", longopts_options)
        print("self.__shortopts_options_parsed", self.__shortopts_options_parsed)
        print("self.__longopts_options_parsed", self.__longopts_options_parsed)
        self.short_opts, self.long_opts, self.args = self.get_opts(shortopts_options, longopts_options)
        
    def parse_options(self, shortopts_options, longopts_options):
        shortopts_options_parsed = []
        longopts_options_parsed = []
        for shortopt in shortopts_options:
            if shortopt == self.__SHORTOPT_FOLLOWER: continue
            else: shortopts_options_parsed.append(shortopt)
        for longopt in longopts_options:
            longopts_options_parsed.append(longopt.strip(self.__LONGOPT_FOLLOWER))
        return shortopts_options_parsed, longopts_options_parsed
        
    def get_script_name(self):
        return os.path.basename(sys.argv[0])
        
    def get_opts(self, shortopts_options, longopts_options):
        shortopts = {}
        longopts = {}
        
        # DEV print out sys.argv
        for i in range(len(sys.argv)):
            print(i, ": ", sys.argv[i])
        
        try:
            opts, args = getopt.getopt(sys.argv[1:], shortopts_options, longopts_options)
        except getopt.GetoptError as e:
            print(str(e).capitalize())
            self.short_help()
            sys.exit()
        print("getopt-opts", opts)
        print("getopt-args", args)
        # populate shortopts/longopts with all False
        for shortopt in shortopts_options: shortopts.update({shortopt: False})
        for longopt in longopts_options: longopts.update({longopt: False})
        
        # set flags from opts passed on command line
        for opt, arg in opts:
            in_short_help = opt.strip(Opts.__SHORTOPT_LEADER) in self.__SHORTOPTS_HELP
            in_long_help = opt.strip(Opts.__LONGOPT_LEADER) in self.__LONGOPTS_HELP
            in_short = opt.strip(Opts.__SHORTOPT_LEADER) in shortopts_options
            in_long = (opt.strip(Opts.__LONGOPT_LEADER) in longopts_options) or (opt.strip(Opts.__LONGOPT_LEADER) + Opts.__LONGOPT_FOLLOWER in longopts_options)
            print("opt:", opt)
            print("arg:", arg)
            print("in short:", in_short)
            print("in long:", in_long)
            
            if in_short_help:
                self.short_help()
                sys.exit()
            elif in_long_help:
                self.long_help()
                sys.exit()
            elif (in_short): # set True in the self.__shortopts dict any short options found on the command line input
                if not arg: shortopts[opt.strip(Opts.__SHORTOPT_LEADER)] = True
                elif arg: shortopts[opt.strip(Opts.__SHORTOPT_LEADER)] = arg
            elif (in_long):  # set True in the self.__longopts dict any long options found on the command line input
                if not arg: longopts[opt.strip(Opts.__LONGOPT_LEADER)] = True
                elif arg: longopts[opt.strip(Opts.__LONGOPT_LEADER)] = arg
            else:
                print("not short_help, long_help, or in shortopts_options or longopts_options")
                self.short_help()
                sys.exit()
        if not (opts and args):
            print("No opts or args provided")
            self.short_help()
            sys.exit()
        return shortopts, longopts, args
    
    def short_help(self):
        short_help_usage_string = "usage: "
        short_help_usage_string += self.script_name + " "
        for shortopt in self.__shortopts_options_parsed:
            short_help_usage_string += self.__SHORTOPT_LEADER + shortopt + " "
        for longopt in self.__longopts_options_parsed:
            short_help_usage_string += self.__LONGOPT_LEADER + longopt + " "
        short_help_usage_string.rstrip() # remove hanging space
        print(short_help_usage_string)
        
    def long_help(self):
        self.short_help()
        # with open(r".\longhelp.txt") as longhelp:
        #     print(longhelp.read())
        print("\n" + self.__longhelp_text)
        