import datetime
import colorama


def color(text, bg=colorama.Back.BLACK, fg=colorama.Fore.WHITE):
    return f'{bg}{fg}{text}{colorama.Style.RESET_ALL}'


def log(text, case="log"):
    colorama.init(autoreset=True)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if case.lower() == "log":
        print(f'{time} {color(case.upper(), bg=colorama.Back.BLUE)} {text}')

    elif case.lower() == "warn":
        print(f'{time} {color(case.upper(), colorama.Back.YELLOW, colorama.Fore.BLACK)} {text}')

    elif case.lower() == "error":
        print(f'{time} {color(case.upper(), colorama.Back.RED)} {text}')

    elif case.lower() == "debug":
        print(f'{time} {color(case.upper(), fg=colorama.Fore.GREEN)} {text}')

    elif case.lower() == "ready":
        print(f'{time} {color(case.upper(), colorama.Back.GREEN, colorama.Fore.BLACK)} {text}')

