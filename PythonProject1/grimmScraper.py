# 2021-03-03 ebb: I'm adapting a script for downloading videos
# from GeeksforGeeks.org: https://www.geeksforgeeks.org/downloading-files-web-using-python/
# ebb: Before beginning, go out to your shell (Git Bash or Terminal) and enter:
# pip install BeautifulSoup4
import bs4
import requests
import os

# ebb: This variable stores the website address that you want to scrape.
archive_url = "https://www.cs.cmu.edu/~spok/grimmtmp/"

def get_tales():
    # create response object
    r = requests.get(archive_url)

    # create beautiful-soup object
    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    # find all links on web-page
    for item in soup.findAll('li'):
        link = item.find('a')
        href = archive_url + link['href']
        download_links(href)
    print("All tales downloaded!")
    # ebb: The print line indicating
    # all files downloaded needs to go after THIS loop finished.
    # Do you see why it makes sense and works here?
    # Hint: it has to do with when we call the function download_links(href)
def download_links(href):
    # obtain filename by splitting url and getting last string
    file_name = href.split('/')[-1]
    print("Downloading file: " + file_name)
    # Convert to an f "picture string" just for fun. :-)

    # create response object
    r = requests.get(href, stream = True)

    workingDir = os.getcwd()
    # PREVIOUS LINE IS SUPER IMPORTANT! It defines a variable for MY CURRENT WORKING DIRECTORY!
    print("current working directory: " + workingDir)
    fileDeposit = os.path.join(workingDir, 'grimmTales', file_name)
    print(fileDeposit)


    # download started
    with open(fileDeposit, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                f.write(chunk)
                print("Downloaded " + file_name)

    return

# ebb: Basically the line below initiates the whole program, sets it in motion.
# On the line if __name__ == "__main__": ,
# see: https://medium.com/@j.yanming/debugging-from-main-to-main-in-python-fe2a9784b36
if __name__ == "__main__":

    # getting all links to files
    get_tales = get_tales()






