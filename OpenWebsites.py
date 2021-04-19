import subprocess

# created for a mac (may work for a windows system as well)
# requires a file called open_tabs.txt to be in the same folder as this script
# each website needs to be on it's own line

f = open("open_tabs.txt", "r")
websites_list = f.read
for site in f:
    #print(site)
    #Call_URL = "https://www.google.com"
    mycmd = r'open -a "Google Chrome" {}'.format(site)
    subprocess.Popen(mycmd,shell = True)
