import base64
import encodings
from tarfile import ENCODING
import requests

def upload_file_demo_1():
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

    with open("./data/report.out", mode=mode, encoding=encoding) as a_file:
        file_dict = {"report.out": a_file}
        url = "http://3665-195-74-76-233.ngrok.io/push-file"
        resp = requests.post(url, files=file_dict)
        print(f"Response status code: {resp.status_code}")

def upload_file_demo_2():
    MODE = 'rb'

    # Use default enconding (utf-8)
    ENCODING = None

    # file = "./data/AvastSecureBrowser-103.0.2437.114.dmg"
    FILE = "./data/dummy_1MB.bin"
    SSL_CERT_VERIFY = True
    proxies = {}
    # proxies["http"] = "http://build-proxy.re.ida.avast.com:8080"
    # proxies["https"] = "https://build-proxy.re.ida.avast.com:8080"

    with open(file = FILE, mode=MODE, encoding=ENCODING) as file_descriptor:
        file_dict = {"file": file_descriptor}
        # token = ""
        token = str(base64.b64encode(("bojan.komazec@avast.com" + ":" + "E$q3@h6j0^XQvaRA").encode("utf-8")), "utf-8")
        headers={
            "Authorization": "Basic " + token
        }
        url = "https://dev-admin.avastbrowser.com/wp-json/wp/v2/media/"
        resp = requests.post(url, headers=headers, files=file_dict, proxies = proxies, verify=SSL_CERT_VERIFY)
        print(f"Response status code: {resp.status_code}")

def requests_demo():
    # upload_file_demo_1()
    upload_file_demo_2()

requests_demo()
