Source: https://happycamper84.medium.com/hash-cracking-cheatsheet-7c10f2b31143

Examples:

#hashcat on bcrypt (used in OpenBSD, used in various Linux distros in the past)
hashcat -m3200 ‘$2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG’ /home/kali/Downloads/Wordlists/rockyou.txt -force


#SHA256 (used in many *nix for password hashes)
hashcat -m1400 ‘9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1’ /home/kali/Downloads/Wordlists/rockyou.txt –force


#hash resulting from ASREPRoast (copy/paste the hash from GetNPUsers.py & enclose in single quotes)
hashcat -m 18200 ‘$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:479e4f94a068ef144a788436c7df94e7$7a05e6b2e85dff303406c56f1c85feefe6ea6b5fbbe6a9d9cc59cf190add2502d2b8906eabe9d1f6a49cf90a707f94118477754fc7c04c2644824d35d25b11ee5dcc1bb519b78367d172374fdab521fb236fbd0f4dccb6d3f3a9a7c5ea0b1223a7a29adc38665abb144feff9f0b539b26f2f32d49d0a6820fd05c6b64ffe611df26d0adb0d05b7eab01639cdfc2d7ffaab92e94c7c077eaeeef14e9ce69d4088aabba32f6bb8c10235e0b03c496c409257c64d839e397e9c979346557f0d675cdb9f97224ba0954be9540f91cd7ea7be20ea745a9bf393807201ff9ff2685ac1f801dd77d2c049249f34a3e6509be3eb821b’ -a 3 rockyou.txt


#run hashcat on a hash that was copy/pasted into a file after Kerberoasting
hashcat -m 19700 hashes.kerberoast2 rockyou.txt –force


John
john --wordlist=/home/kali/Downloads/Wordlists/rockyou.txt /home/kali/Downloads/hashes/THM/combined.txt


zip2john backup.zip > /home/kali/Downloads/hashes/ziphash.txt
john --wordlist=/home/kali/Downloads/Wordlists/rockyou.txt /home/kali/Downloads/hashes/ziphash.txt


rar2john secure.rar > rarhash.txt
john --wordlist=/home/kali/Downloads/Wordlists/rockyou.txt rarhash.txt


John is great for cracking password protected ssh keys. If you don’t already have ssh2john loaded then you can grab it here.
python /usr/share/john/ssh2john.py idrsa.id_rsa > ssh
john --wordlist=/home/kali/Downloads/Wordlists/rockyou.txt ssh


It’s not quite as handy as hashcat’s table, however there is a list of john formats matched to hash types here.
#For example run John on a SHA256 hash
john --format=raw-sha256 --wordlist=/home/kali/Downloads/Wordlists/rockyou.txt /home/kali/Downloads/hashes/THM/hash3.txt


#Another example; John vs a hash grabbed via Kerberoasting
john hash.txt --format=krb5tgs --wordlist=rockyou.txt

