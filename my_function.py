def say_hello(name: str):
    print(f'hello, {name}!!!')


def print_message():
    print("this is 'hello app'")


if __name__ == '__main__':
    print_message()
    name = input("Enter your name: ")
    say_hello(name)
