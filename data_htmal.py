import urllib.request
import os

def download_websites(url_list, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for url in url_list:
        site = urllib.request.urlopen(url=url)
        html = site.read().decode('utf-8')
        filename = os.path.join(output_dir, url.split('/')[-1] + '.txt')
        with open(filename, 'w') as f:
            f.write(html)

import urllib.request
import os

url_list = ["https://www.google.com", "https://www.yahoo.com", "https://www.bing.com"]
folder_path = "./website_data"  # Speicherpfad für den heruntergeladenen HTML-Code

if not os.path.exists(folder_path):  # Überprüfen Sie, ob der Ordner bereits vorhanden ist
    os.mkdir(folder_path)  # Wenn nicht, erstellen Sie den Ordner

for url in url_list:
    site = urllib.request.urlopen(url=url)
    site = site.read().decode('utf-8')  # Konvertieren Sie die Bytes in einen String

    # Verwenden Sie die URL als Dateinamen, ersetzen Sie den Schrägstrich durch einen Unterstrich
    filename = url.replace("/", "_") + ".txt"  

    # Schreiben Sie den HTML-Code in eine Textdatei und speichern Sie sie im Ordner
    with open(os.path.join(folder_path, filename), "w", encoding='utf-8') as f:
        f.write(site)
