from colorama import Fore, Style, init
import pprint



class SimpleLogger:
    COLORS = {
        'r': Fore.RED,
        'g': Fore.GREEN,
        'b': Fore.BLUE,
        'y': Fore.YELLOW,
        'm': Fore.MAGENTA,
        'c': Fore.CYAN,
        'w': Fore.WHITE,
        'k': Fore.BLACK,
        'o': Fore.LIGHTRED_EX
    }
    
    @staticmethod
    def print(*args, color='w', end="\n"):
        color_code = SimpleLogger.COLORS.get(color.lower(), Fore.WHITE)
        
        if isinstance(args[-1], str) and args[-1] in SimpleLogger.COLORS:
            color_code = SimpleLogger.COLORS[args[-1]]
            args = args[:len(args)-1]
            
        args = map(lambda arg: str(arg), args)
        formatted_args = color_code + " ".join(args) + Style.RESET_ALL
        
        print(formatted_args, end=end)
            
