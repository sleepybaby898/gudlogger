from colorama import Fore
from datetime import datetime

class Logger():
    def __init__(
            self,
            debug: bool = False,
            defaultPrefix: str = None,
            shouldColorText: bool = False,
            newlineBetweenLogs: bool = False,
    ) -> None:
        self.debugMode = debug
        self.defaultPrefix = defaultPrefix
        self.shouldColorText = shouldColorText
        self.newLine = newlineBetweenLogs
        pass
    """
    Default functions (write, prefix)
    """
    def write(self, log: str) -> None:
        if not self.newLine:
            print(f"{log}")
        else:
            print(f"{log}\n")
    
    def prefix(self, data: str, color: Fore, title: str = None) -> str:
        s = Logger._prefix(
            data=data,
            color=color,
            title=title,
            defaultPrefix=self.defaultPrefix,
            shouldColor=self.shouldColorText
        )
        return s
    
    def _prefix(data: str, color: Fore, title: str = None, defaultPrefix: str = None, shouldColor: bool = False):
        pr1 = ""
        if defaultPrefix is not None:
            if "<TIME>" in defaultPrefix:
                defaultPrefix = defaultPrefix.replace("<TIME>", f"{color}{datetime.now().strftime(f'{color}%H{Fore.WHITE}:{color}%M{Fore.WHITE}:{color}%S')}{Fore.WHITE} |{color}")
            
            pr1 = pr1 = pr1 + f"{color}{defaultPrefix}{Fore.RESET} | "
        
        pr2 = f"{color}{data} >"

        finalPrefix = f"{pr1}{pr2}"

        if title is not None:
            finalPrefix = finalPrefix + f" {Fore.WHITE}[{color}{title}{Fore.WHITE}]{color}"
        
        if not shouldColor:
            finalPrefix = finalPrefix + f"{Fore.RESET}"
        
        return finalPrefix
    """
    Logging functions ( e.g error, info, warn)
    """
    def info(self, data: str, title: str = None) -> None:
        prefix = self.prefix(f"i", Fore.LIGHTBLUE_EX, title)
        self.write(f"{prefix} {data} {Fore.RESET}")
    
    def warn(self, data: str, title: str = None) -> None:
        prefix = self.prefix(f"!", Fore.YELLOW, title)
        self.write(f"{prefix} {data} {Fore.RESET}")
    
    def error(self, data: str, title: str = None) -> None:
        prefix = self.prefix(f"!", Fore.RED, title)
        self.write(f"{prefix} {data} {Fore.RESET}")

    def debug(self, data: str, title: str = None) -> None:
        prefix = self.prefix(f"~", Fore.LIGHTMAGENTA_EX, title)
        self.write(f"{prefix} {data} {Fore.RESET}")
    
    def valid(self, data: str, title: str = None) -> None:
        prefix = self.prefix(f"✓", Fore.LIGHTGREEN_EX, title)
        self.write(f"{prefix} {data} {Fore.RESET}")
    
    def invalid(self, data: str, title: str = None) -> None:
        prefix = self.prefix(f"-", Fore.LIGHTGREEN_EX, title)
        self.write(f"{prefix} {data} {Fore.RESET}")