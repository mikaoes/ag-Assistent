verbose = True

verbose and print("Core importted")

if __name__ == "__main__":
    print("Core is main")
    import cli
else:
    print("Core is not main")
    import core.cli as cli

def start(env):
    print("core.start called")
    if env == "cli":
        print("Starting CLI...")
        cli.start()
    elif env == "gui":
        print("Starting GUI...")
        # added later