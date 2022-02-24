def say_hello(name: str):
    print(f'hello, {name}!!!')


if __name__ == '__main__':
    name = input("Enter your name: ")
    say_hello(name)
