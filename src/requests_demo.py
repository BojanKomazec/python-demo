import encodings
import requests

def requests_demo():

    mode = 'r'

    # ValueError: Must have exactly one of create/read/write/append mode and at most one plus
    # mode = 'b'
    # mode = 'rb'

    # Use default enconding (utf-8)
    encoding = None

    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x96 in position 310915: invalid start byte
    # encoding = 'utf-8'

    # encoding = 'latin-1'

    # UnicodeDecodeError: 'ascii' codec can't decode byte 0x96 in position 310915: ordinal not in range(128)
    # encoding = 'ascii'

    encoding = 'iso-8859-1'

    with open("./test_scripts/report.out", mode=mode, encoding=encoding) as a_file:
        file_dict = {"report.out": a_file}
        url = "http://3665-195-74-76-233.ngrok.io/push-file"
        resp = requests.post(url, files=file_dict)
        print(f"Response status code: {resp.status_code}")