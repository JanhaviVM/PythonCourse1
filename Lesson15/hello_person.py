def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Ola",
        "German": "Hallo"
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    # only one arguement can be created at a time with the add_arguement function.
    # inside parser.add_arguement, we define the command line arguement that python will look for and accept when executed
    # --n or --name are the arguement flags, both refer to the same arguement being created.
    # metavar is what the display name is, incase you get a message that refers back to this arguement.
    # dest is the name for us to use across the code when referring to the arguement coming from args
    # required says when using the file, this argument needs to be provided.
    # help is shown incase you get a message that refers back to this arguement.
    parser.add_argument(
        "-n", "--name", metavar="name", dest="firstname",
        required=True, help="The name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting"
    )

    # 'args' stores the values passed from the command line when running a script
    # then it processes them based on your definitons
    # then stores them inside variable names
    args = parser.parse_args()

    # msg = f"Hello {args.firstname}!"
    # print(msg)

    hello(args.firstname, args.lang)

# Purpose of parser
# the parser converts the raw string -n "Janhavi"
# into computer readable structure args.name = "Janhavi"
