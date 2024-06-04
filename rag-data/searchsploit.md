# SearchSploit
  Usage: searchsploit [options] term1 [term2] ... [termN]

==========
 Examples 
==========
  searchsploit afd windows local
  searchsploit -t oracle windows
  searchsploit -p 39446
  searchsploit linux kernel 3.2 --exclude="(PoC)|/dos/"
  searchsploit -s Apache Struts 2.0.0
  searchsploit linux reverse password
  searchsploit -j 55555 | jq
  searchsploit --cve 2021-44228

  For more examples, see the manual: https://www.exploit-db.com/searchsploit

searchsploit output looks like this, where the left column contains the title of the exploit, and the right column contains a filepath or url to the exploit file.
------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                          |  Path
------------------------------------------------------------------------ ---------------------------------
Oracle 10g (Windows x86) - 'PROCESS_DUP_HANDLE' Local Privilege Escalat | windows_x86/local/3451.c
Oracle 9i XDB (Windows x86) - FTP PASS Overflow (Metasploit)            | windows_x86/remote/16731.rb
Oracle 9i XDB (Windows x86) - FTP UNLOCK Overflow (Metasploit)          | windows_x86/remote/16714.rb
Oracle 9i XDB (Windows x86) - HTTP PASS Overflow (Metasploit)           | windows_x86/remote/16809.rb
Oracle MySQL (Windows) - FILE Privilege Abuse (Metasploit)              | windows/remote/35777.rb
Oracle MySQL (Windows) - MOF Execution (Metasploit)                     | windows/remote/23179.rb
Oracle MySQL for Microsoft Windows - Payload Execution (Metasploit)     | windows/remote/16957.rb
Oracle VirtualBox Guest Additions 5.1.18 - Unprivileged Windows User-Mo | multiple/dos/41932.cpp
Oracle VM VirtualBox 5.0.32 r112930 (x64) - Windows Process COM Injecti | windows_x86-64/local/41908.txt
------------------------------------------------------------------------ ---------------------------------
