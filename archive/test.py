import requests

response = requests.get("https://www.cpp.edu/sci/physics-astronomy/about/index.shtml")


with open('site.html', 'w') as file:
    file.write(response.text)