class DevDecorator():
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("We are in the decorator...")
        print("Entering wrapped func now", self.f.__name__)
        self.f()
        print("Exited wrapped func", self.f.__name__)


def do_not_decorate(a):
    return a

def core_function():
    print("core_function runs with conditional decoration")

def main():
    if use_decorator is True:
        core_function = do_not_decorate(core_function)
    else:
        core_function = do_not_decorate(DevDecorator(core_function))
    core_function()

if __name__ == "__main__":
    mail()
