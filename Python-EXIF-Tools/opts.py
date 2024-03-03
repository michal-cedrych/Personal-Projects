from Opts import Opts

def main():
    opts = Opts("a:bc", ["todo=", "foo"])
    print("shortopts: ", opts.short_opts)
    print("longopts: ", opts.long_opts)
    print("args:", opts.args)
    print("script name: ", opts.script_name)
if __name__ == '__main__':
    main()
