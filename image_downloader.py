import requests 


def download_files(url):

    local_filename = url.split("/")[-1]
    with requests.get(url,stream=True) as r:
        print("Downloading...")
        with open("C:\\Users\\korisnik\\Desktop\\python projects\\"+local_filename,"wb") as f:
            print("Writing data to file...")
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print("Download complete.")
    print("File saved as "+local_filename)


while True: 
    print("-"*70)
    print("Welcome to the image downloader")
    print("-"*70)
    image_url = input(str("Image url: "))
    download_files(image_url)
    print("")