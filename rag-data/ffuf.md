# Source: https://medium.com/@cuncis/ffuf-the-fast-and-flexible-web-fuzzer-for-penetration-testing-cheat-sheet-10fc5688974f

FFUF (Fuzz Faster U Fool) is a fast web fuzzer written in Go, designed to help in quickly discovering potential vulnerabilities in web applications by performing brute force attacks on various parts of a web application.

Examples:

1. Basic usage:
ffuf -w wordlist.txt -u http://example.com/FUZZ

2. Add custom header:
ffuf -w wordlist.txt -u http://example.com/FUZZ -H "Authorization: Bearer <token>"

3. Use POST method:
ffuf -w wordlist.txt -u http://example.com/api -X POST -d "param1=value1&param2=value2"

4. Finding subdomain:
ffuf -u https://FUZZ.example.com -w wordlist.txt -mc 200,301,302,403

5. Follow redirects:
ffuf -w wordlist.txt -u http://example.com/FUZZ -r

6. Use a proxy:
ffuf -w wordlist.txt -u http://example.com/FUZZ -p http://127.0.0.1:8080

7. Exclude directories:
ffuf -w wordlist.txt -u http://example.com/FUZZ -exclude-dirs "admin,backup,test"

8. Use custom match string:
ffuf -w wordlist.txt -u http://example.com/FUZZ -c "Password incorrect"

9. Number of threads:
ffuf -w wordlist.txt -u http://example.com/FUZZ -t 50