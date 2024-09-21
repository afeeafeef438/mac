import pyfiglet
import requests


assci_banner=pyfiglet.figlet_format("sub domain enumarater")
print(assci_banner)

domain=input("enter the domain:")
sub_list=input("enter the sub-list(with path):")
list=open(sub_list).read()
content=list.splitlines()

for sub in content:
    req=f"https://{sub}.{domain}"
try:
    requests.get(req)
except requests.ConnectionError:
    print("invalid domain")
else:
    print("subdomain found:",req)