import urllib.request

url_list = ['https://example.com', 'https://example.org']
list_data_text = []

for url in url_list:
    site = urllib.request.urlopen(url=url)
    site = site.read()

    for i in site.split():
        if i == "https://":
            for url_i in url_list:
                if i == url_i:
                    break
                elif not site:
                    url_list.append(i)
                else:
                    print("Error Emilio if")

    with urllib.request.urlopen(str(url)) as f:
        list_data_text.append(f.read())

for web in list_data_text:
    # Do something with the HTML content
    print(web)
