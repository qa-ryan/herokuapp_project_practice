class BasePage:
    def __init__(self, page):
        self.page = page

    def log_status(self, message):
        print(f"\n{message}")