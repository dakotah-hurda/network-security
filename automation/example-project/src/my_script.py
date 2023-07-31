def helper_function01(name: str) -> bool:
  if len(name) > 0: 
    return True
  else:
    return False

def main():
  name = input("What's your name?")
  if helper_function01(name):
    print(f"Hello, {name}.")
  else:
    print("You didn't provide a name.")

if __name__ == '__main__':
  main()
