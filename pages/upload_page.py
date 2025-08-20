from playwright.sync_api import Page, expect

class UploadPage:
    URL = "https://the-internet.herokuapp.com/upload"
    
    def __init__(self, page:Page):
        self.page = page
        self.file_input = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")
        self.uploaded_file_name = page.locator("#uploaded-files")
        
    def load(self):
        self.page.goto(self.URL)

    def upload_file(self, file_path: str):
        self.file_input.set_input_files(file_path)
        self.upload_button.click()

    def get_uploaded_filename(self) -> str:
        return self.uploaded_file_name.text_content().strip()
    