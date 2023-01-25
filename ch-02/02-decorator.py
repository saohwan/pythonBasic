# decorator


def copyright(func):
    def new_func():
        print("@ anananadwdwldkladsjflkdjsflkd")
        func()
    return new_func


@copyright
def smile():
    print("😀")


@copyright
def angry():
    print("😡")


@copyright
def love():
    print("😍")


smile()
angry()
love()

