import os
from zipfile import ZipFile

import proj


def test_stegno_file_created():
    file1 = "Neymar.jpg"
    file2 = "text.zip"
    out_file = "super_image.jpg"
    proj.merge_files(file1, file2, out_file)
    assert os.path.isfile(out_file)


def test_stegno_file_content():
    with ZipFile('super_image.jpg') as zf:
        for file in zf.namelist():
            text = open(file).read()
            assert text == """NAME:ARCHIT SINGH
ACCOUNT TYPE:SAVINGS
ACCOUNT NUMBER:1667 8773 4773 9484
CVV:820
IFSC CODE:SBI91910109
"""


def test_stegno_file_integrity():
    hash1, hash2 = None, None
    zf = ZipFile("text.zip")
    text_file = zf.namelist()[0]
    hash1 = proj.calculate_hash(text_file)

    with ZipFile('super_image.jpg') as zf:
        text_file = zf.namelist()[0]
        hash2 = proj.calculate_hash(text_file)

    print(hash1, hash2)
    assert hash1 == hash2
