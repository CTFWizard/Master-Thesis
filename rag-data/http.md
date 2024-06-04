# HTTP


## Service validation
Tell user to use browser manually to check ports responding with HTTP, nginx, apache, lighttp, IIS, django

## Redirect
If attempting to access the host through a web browser causes a redirect, it might be required to add the host to /etc/hosts
sudo echo "<IP address> <hostname>" >> /etc/hosts

## Port 80
Port 80 is reserved for web services with HTTP
Port 8080 is commonly used as an alternative to port 80

## Port 443
Port 443 is reserved for HTTPS
Port 8443 is commonly used as an alternative port

## Fuzzing
URL fuzzing:
UI Tool: OWASP DirBuster - give target url (eg http://<hostname>:<port>/), provide a wordlist (eg megabeast.txt, subdomains-top1million-110000.txt)

Fuzzing for sub-directories
gobuster dir -u <url> -w <wordlist>
gobuster dir -u <http://exampple.com> -w /usr/share/wordlists/dirb/common.txt

Fuzzing for sub-domains
gobuster dns -d <domain> -w <wordlist>
gobuster dns -d exampledomain.com -w /usr/share/wordlists/subdomains-top1million-110000.txt

## Intercept network traffic
Burpsuite CE can be used for manual vulnerability scanning for HTTP connections by intercepting the network traffic between the host and a client browser.