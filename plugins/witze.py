import httpimport

with httpimport.github_repo('mikaoes', 'witzapide-wrapper'):
  import src as witze

def quarkspeise() :
    return witze.request()

commands = {
    "erzähl mir einen witz" : quarkspeise
}