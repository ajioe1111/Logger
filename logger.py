from colorama import init, Fore, Style
import datetime

# Инициализация colorama для поддержки ANSI цветов в Windows
init(autoreset=True)

class ColoredLogger:
    def __init__(self):
        pass
    
    def _get_current_time(self):
        now = datetime.datetime.now()
        return now.strftime(f"{Fore.YELLOW}%Y-%m-%d %H:%M:%S{Style.RESET_ALL}")

    def _log_message(self, levelname, message):
        time_str = f"{Fore.YELLOW} ╭─<{self._get_current_time()}>\n{Style.RESET_ALL}"
        level_str = f"{Fore.CYAN} ╰─[{Style.BRIGHT}{levelname}{Style.RESET_ALL}{Fore.CYAN}] ➔ {Style.RESET_ALL}"
        print(f"{time_str}{level_str} {Fore.WHITE}{message}{Style.RESET_ALL}")

    def debug(self, message):
        self._log_message(f"{Fore.BLUE}DEBUG", message)

    def info(self, message):
        self._log_message(f"{Fore.GREEN}INFO", message)

    def warning(self, message):
        self._log_message(f"{Fore.YELLOW}WARNING", message)

    def error(self, message):
        self._log_message(f"{Fore.RED}ERROR", message)

    def critical(self, message):
        self._log_message(f"{Fore.MAGENTA}CRITICAL", message)

# Пример использования кастомного логгера
if __name__ == "__main__":
    logger = ColoredLogger()

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
