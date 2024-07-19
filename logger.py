from colorama import init, Fore, Style
import datetime
import re

# Инициализация colorama для поддержки ANSI цветов в Windows
init(autoreset=True)

class ColoredLogger:
    def __init__(self, log_file="app.log"):
        self.log_file = log_file
        # Открываем файл для логирования в режиме добавления (append)
        self.file_handle = open(self.log_file, "a", encoding="utf-8")

    def __del__(self):
        if self.file_handle:
            self.file_handle.close()

    def _get_current_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def _remove_ansi_escape(self, text):
        ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', text)

    def _log_message(self, levelname, message):
        current_time = self._get_current_time()
        time_str = f"╭─<{current_time}>"
        level_str = f"╰─[{levelname}] ➔ "
        
        # Формируем лог для консоли с цветами
        console_time_str = f"{Fore.YELLOW}{time_str}{Style.RESET_ALL}\n"
        console_level_str = f"{Fore.CYAN}{level_str}{Style.RESET_ALL} {Fore.WHITE}{message}{Style.RESET_ALL}"
        console_log_entry = f"{console_time_str}{console_level_str}"
        
        # Формируем лог для файла без цветов
        file_time_str = f"{time_str}\n"
        file_level_str = f"{level_str} {message}\n"
        file_log_entry = f"{file_time_str}{file_level_str}"
        file_log_entry = self._remove_ansi_escape(file_log_entry)
        
        # Записываем лог в файл
        self.file_handle.write(file_log_entry)
        self.file_handle.flush()  # Принудительно сбрасываем буфер, чтобы запись была немедленной
        
        # Выводим лог в консоль
        print(console_log_entry)

    def debug(self, message):
        self._log_message(f"{Style.BRIGHT}{Fore.BLUE}DEBUG", message)

    def info(self, message):
        self._log_message(f"{Style.BRIGHT}{Fore.GREEN}INFO", message)

    def warning(self, message):
        self._log_message(f"{Style.BRIGHT}{Fore.YELLOW}WARNING", message)

    def error(self, message):
        self._log_message(f"{Style.BRIGHT}{Fore.RED}ERROR", message)

    def critical(self, message):
        self._log_message(f"{Style.BRIGHT}{Fore.MAGENTA}CRITICAL", message)

# Пример использования кастомного логгера
if __name__ == "__main__":
    logger = ColoredLogger()

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
