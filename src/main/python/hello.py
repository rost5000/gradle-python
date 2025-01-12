from termcolor import colored

colored_text = colored("hello java", "red", attrs=["reverse", "blink"])
print(colored_text)