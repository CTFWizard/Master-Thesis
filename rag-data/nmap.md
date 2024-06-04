# nmap
Nmap is a free and open source utility for network discovery and security auditing.

1. **Aggressive Scan (OS detection, version detection, script scanning, and traceroute)**:
   - This scan is comprehensive, combining various techniques including OS detection, version detection, script scanning, and traceroute to provide detailed information about the target.
   ```
   nmap -A <target-ip>
   ```

2. **OS Detection**:
   - This scan focuses solely on detecting the operating system running on the target machine, providing insights into the OS type and version.
   ```
   nmap -O <target-ip>
   ```

3. **Skip Host Discovery**:
   - This scan treats all hosts as online, skipping the initial host discovery phase and directly proceeding to port scanning.
   ```
   nmap -Pn <target-ip>
   ```

4. **TCP SYN Scan**:
   - Also known as a "stealth scan", this scan sends TCP SYN packets to the target's ports and analyzes the response to determine which ports are open, closed, or filtered.
   ```
   nmap -sS <target-ip>
   ```

5. **TCP Connect Scan**:
   - This scan performs a full TCP connection to each port, attempting to establish a connection and determine whether the port is open, closed, or filtered.
   ```
   nmap -sT <target-ip>
   ```

6. **UDP Scan**:
   - UDP scan is used to discover open UDP ports on the target machine, which are often overlooked but can be crucial for certain services.
   ```
   nmap -sU <target-ip>
   ```

7. **TCP NULL Scan**:
   - This scan sends TCP packets with no flags set (NULL packets) to target ports. The response (or lack thereof) helps identify open, closed, or filtered ports.
   ```
   nmap -sN <target-ip>
   ```

8. **TCP FIN Scan**:
   - Similar to the NULL scan, the FIN scan sends TCP packets with the FIN flag set to target ports, aiming to detect open ports based on the response or lack thereof.
   ```
   nmap -sF <target-ip>
   ```

9. **TCP ACK Scan**:
   - This scan sends TCP packets with only the ACK flag set to target ports, useful for determining firewall rules and filtering policies.
   ```
   nmap -sA <target-ip>
   ```

10. **Operating System Detection**:
    - This scan focuses on identifying the operating system running on the target machine, providing information such as OS type, version, and possible OS families.
    ```
    nmap -O <target-ip>
    ```

11. **Service Version Detection**:
    - This scan probes open ports to identify the services running on them and their versions, helping to assess potential vulnerabilities and security risks.
    ```
    nmap -sV <target-ip>
    ```

12. **RPC Scan**:
    - RPC scan is used specifically to enumerate RPC services on the target machine, revealing information about available RPC services and their versions.
    ```
    nmap -sR <target-ip>
    ```
  