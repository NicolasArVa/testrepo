def main():
    name = input("What's your name? ").strip().title()
    hello(name)
    
def hello(subject="World"):
    print("Hello,", subject)

main()