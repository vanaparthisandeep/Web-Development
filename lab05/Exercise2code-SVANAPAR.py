import requests
import json
url = "https://michaelgathara.com/api/python-challenge"
response = requests.get(url)
summons = response.json()
print("Name: SANDEEP VANAPARTHI")
print("Blazer ID: SVANAPAR\n")
print(summons)

for snag in summons:
    snag_id = snag['id']
    assertion = snag['problem']
    assertion = assertion.rstrip('?')
    print("\nQUERY:", snag_id)
    print("Solve_Expression:", assertion)
    try:
        solution = eval(assertion)
        print("Solu:", solution)
    except SyntaxError:
        print("Expression cannot be solved")