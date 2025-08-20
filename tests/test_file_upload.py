import os
import pytest
from pages.upload_page import UploadPage

@pytest.fixture(scope="function")
def sample_file(tmp_path, request):
    # If sample_upload.txt exists in test_files/, copy it; otherwise create sample file.
    base_dir = os.path.dirname(request.fspath)
    source = os.path.join(base_dir, "..", "test_files", "sample_upload.txt")
    if os.path.exists(source):
        return source
    else:
        # create temporary file
        sample = tmp_path / "sample_upload.txt"
        sample.write_text("Hello, Playwright!")
        return str(sample)

def test_file_upload(page, sample_file):
    upload = UploadPage(page)
    upload.load()
    upload.upload_file(sample_file)
    
    uploaded_name = upload.get_uploaded_filename()
    assert os.path.basename(sample_file) == uploaded_name, (
        f"Expected uploaded filename to be '{os.path.basename(sample_file)}', "
        f"but got '{uploaded_name}'"
    )