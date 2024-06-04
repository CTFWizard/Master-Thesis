John the Ripper (JtR) is a popular password-cracking tool. 


In single-crack mode, John takes a string and generates variations of that string in order to generate a set of passwords.
For example, if our username is “stealth” and the password is “StEaLtH”, we can use the single mode of John to generate password variations (STEALTH, Stealth, STealth, and so on).

We use the “format” flag to specify the hash type and the “single” flag to let John know we want to use the single crack mode. We will also create a crack.txt file which will contain the username and the hash value of the password.
stealth:d776dd32d662b8efbdf853837269bd725203c579

Now we can use the following command to use John’s single crack mode:
john --single --format=raw-sha1 crack.txt



In dictionary mode, we will provide John with a list of passwords. John will generate hashes for these on the fly and compare them with our password hash.

For this example, we will use the RockYou wordlist. If you are using Kali, you can find it at /usr/share/wordlists/rockyou.txt. We will also have a crack.txt file with just the password hash.
edba955d0ea15fdef4f61726ef97e5af507430c0

john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha1 crack.txt

