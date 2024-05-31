# Catalyst Center Webhook Receiver and Network Troubleshooting

The repo includes the files for a webook receiver for Catalyst Center event notifications.

Also, it includes the Network Troubleshooting App that will be triggered from the Webhook Receiver to Jenkins.
The network Troubleshooting App is developed using the Catalyst Center Pythong SDK.
The Jenkinsfile is provided as a reference.

Sample Output from Pipeline Run:

```python
Started by user Gabriel Zapodeanu
[Pipeline] Start of Pipeline
[Pipeline] getContext
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/Network Troubleshooting
[Pipeline] {
[Pipeline] isUnix
[Pipeline] withEnv
[Pipeline] {
[Pipeline] sh
+ docker inspect -f . python:latest
.
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] withDockerContainer
Jenkins does not seem to be running inside a container
$ docker run -t -d -u 130:137 -w "/var/lib/jenkins/workspace/Network Troubleshooting" -v "/var/lib/jenkins/workspace/Network Troubleshooting:/var/lib/jenkins/workspace/Network Troubleshooting:rw,z" -v "/var/lib/jenkins/workspace/Network Troubleshooting@tmp:/var/lib/jenkins/workspace/Network Troubleshooting@tmp:rw,z" -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** python:latest cat
$ docker top 89cd2b338ba375f2a5f817f1f10c67c626bb21e44b79c1c83164283c964b520e -eo pid,comm
[Pipeline] {
[Pipeline] withCredentials
Masking supported pattern matches of $GITHUB_TOKEN
[Pipeline] {
[Pipeline] withEnv
[Pipeline] {
[Pipeline] timeout
Timeout set to expire in 15 min
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Environment variables)
[Pipeline] echo


Pipeline name: Network Troubleshooting ..............................
[Pipeline] echo
App name: network_troubleshooting.py ..............................
[Pipeline] echo
GitHub repo name: catalyst_center_network_troubleshooting ..............................
[Pipeline] echo
Workspace: /var/lib/jenkins/workspace/Network Troubleshooting ..............................
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build Python Environment)
[Pipeline] echo


Jenkins Network Troubleshooting build start..............................
[Pipeline] echo


Building the Docker container:..............................
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Check Input Params)
[Pipeline] echo
Assurance Issue Id: 3e4e8424-9b67-4c9d-abb3-223cb2b758be
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Pull or Clone the source code)
[Pipeline] withEnv
[Pipeline] {
[Pipeline] script
[Pipeline] {
[Pipeline] fileExists
[Pipeline] echo


Pull code from GitHub:..............................
[Pipeline] dir
Running in /var/lib/jenkins/workspace/Network Troubleshooting/catalyst_center_network_troubleshooting
[Pipeline] {
[Pipeline] sh
+ git pull --ff-only https://zapodeanu:****@github.com/zapodeanu/catalyst_center_network_troubleshooting.git
From https://github.com/zapodeanu/catalyst_center_network_troubleshooting
 * branch            HEAD       -> FETCH_HEAD
Already up to date.
[Pipeline] }
[Pipeline] // dir
[Pipeline] fileExists
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Install Python libraries)
[Pipeline] withEnv
[Pipeline] {
[Pipeline] sh
+ pip install -r catalyst_center_network_troubleshooting/requirements.txt --no-warn-script-location
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: requests in ./.local/lib/python3.11/site-packages (from -r catalyst_center_network_troubleshooting/requirements.txt (line 1)) (2.31.0)
Requirement already satisfied: urllib3 in ./.local/lib/python3.11/site-packages (from -r catalyst_center_network_troubleshooting/requirements.txt (line 2)) (2.2.1)
Requirement already satisfied: dnacentersdk in ./.local/lib/python3.11/site-packages (from -r catalyst_center_network_troubleshooting/requirements.txt (line 3)) (2.6.11)
Requirement already satisfied: python-dotenv in ./.local/lib/python3.11/site-packages (from -r catalyst_center_network_troubleshooting/requirements.txt (line 4)) (1.0.1)
Requirement already satisfied: PyYAML in ./.local/lib/python3.11/site-packages (from -r catalyst_center_network_troubleshooting/requirements.txt (line 5)) (6.0.1)
Requirement already satisfied: charset-normalizer<4,>=2 in ./.local/lib/python3.11/site-packages (from requests->-r catalyst_center_network_troubleshooting/requirements.txt (line 1)) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in ./.local/lib/python3.11/site-packages (from requests->-r catalyst_center_network_troubleshooting/requirements.txt (line 1)) (3.7)
Requirement already satisfied: certifi>=2017.4.17 in ./.local/lib/python3.11/site-packages (from requests->-r catalyst_center_network_troubleshooting/requirements.txt (line 1)) (2024.2.2)
Requirement already satisfied: fastjsonschema<3.0.0,>=2.16.2 in ./.local/lib/python3.11/site-packages (from dnacentersdk->-r catalyst_center_network_troubleshooting/requirements.txt (line 3)) (2.19.1)
Requirement already satisfied: future<0.19.0,>=0.18.3 in ./.local/lib/python3.11/site-packages (from dnacentersdk->-r catalyst_center_network_troubleshooting/requirements.txt (line 3)) (0.18.3)
Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in ./.local/lib/python3.11/site-packages (from dnacentersdk->-r catalyst_center_network_troubleshooting/requirements.txt (line 3)) (1.0.0)

[notice] A new release of pip available: 22.3.1 -> 24.0
[notice] To update, run: pip install --upgrade pip
[Pipeline] echo


Verify Python version and Libraries:..............................
[Pipeline] sh
+ python --version
Python 3.11.2
[Pipeline] sh
+ pip3 list
Package            Version
------------------ --------
certifi            2024.2.2
charset-normalizer 3.3.2
dnacentersdk       2.6.11
fastjsonschema     2.19.1
future             0.18.3
idna               3.7
pip                22.3.1
python-dotenv      1.0.1
PyYAML             6.0.1
requests           2.31.0
requests-toolbelt  1.0.0
setuptools         65.5.1
urllib3            2.2.1
wheel              0.38.4

[notice] A new release of pip available: 22.3.1 -> 24.0
[notice] To update, run: pip install --upgrade pip
[Pipeline] echo


Verify Application Files:..............................
[Pipeline] sh
+ ls catalyst_center_network_troubleshooting/
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
NOTICE
README.md
environment.env
network_troubleshooting.py
requirements.txt
troubleshooting_knowledgebase.yml
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Execute Python application)
[Pipeline] echo


App Network Troubleshooting run:..............................
[Pipeline] withEnv
[Pipeline] {
[Pipeline] echo


Verify Working Path:..............................
[Pipeline] sh
+ pwd
/var/lib/jenkins/workspace/Network Troubleshooting
[Pipeline] dir
Running in /var/lib/jenkins/workspace/Network Troubleshooting/catalyst_center_network_troubleshooting
[Pipeline] {
[Pipeline] sh
+ python3 network_troubleshooting.py 3e4e8424-9b67-4c9d-abb3-223cb2b758be
INFO:root: App "Network Troubleshooting.py" run start, 2024-05-31 04:02:57
INFO:root: The Assurance issue Id received is: 3e4e8424-9b67-4c9d-abb3-223cb2b758be
INFO:root:
--------------------------------------------------------------------

INFO:root: The issue details
INFO:root:   Severity: HIGH
INFO:root:   Priority: P1
INFO:root:   Issue name: BGP_Down
INFO:root:   Summary: BGP is down on 'PDX-RO' with neighbor '10.93.131.2'
INFO:root:   Description: Device name 'PDX-RO' at site 'Global/OR/PDX/Floor-2': BGP is down with neighbor '10.93.131.2'
INFO:root:   Timestamp: Fri May 31 04:00:52 2024
INFO:root:   Issue Details: https://10.93.141.45/dna/assurance/issueDetails?issueId=3e4e8424-9b67-4c9d-abb3-223cb2b758be
INFO:root:
--------------------------------------------------------------------

INFO:root: The device details
INFO:root:   Hostname: PDX-RO
INFO:root:   Location: Global/OR/PDX/Floor-2
INFO:root:   Device Role: BORDER ROUTER
INFO:root:   Device Id: 01f7cdf2-2298-42c7-bb74-dc68e3c3a051
INFO:root:   Reachability: REACHABLE
INFO:root:   Health: 10.0
INFO:root:   Management IP Address: 10.93.141.23
INFO:root:   Serial Number: 92ML86IWCBN
INFO:root:   Family: CSR1000V
INFO:root:   Software: 17.3.7
INFO:root:
--------------------------------------------------------------------

INFO:root: Device Compliance Status
INFO:root:    EOX status: COMPLIANT_WARNING
INFO:root:    RUNNING_CONFIG status: COMPLIANT
INFO:root:    IMAGE status: NON_COMPLIANT
INFO:root:    NETWORK_SETTINGS status: COMPLIANT
INFO:root:    PSIRT status: NON_COMPLIANT
INFO:root:
--------------------------------------------------------------------

INFO:root: Suggested actions execution started
INFO:root: Suggested actions execution completed
INFO:root:
...............................

INFO:root:   Cisco DNA Center Suggested Action 1: Check for BGP OutQ. A nonzero value for OutQ indicates an MTU mismatch.
INFO:root:   Device: PDX-RO
INFO:root:   Command: show ip bgp summary | in OutQ|10.93.131.2
INFO:root:   Command output: 
show ip bgp summary | in OutQ|10.93.131.2
Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.93.131.2     4        65004       0       0        1    0    0 00:01:34 Idle
PDX-RO#
INFO:root:
...............................

INFO:root:   Cisco DNA Center Suggested Action 2: Check the TCP agreed max segment. Add 40 bytes for the TCP and IP header. The total should match MTU value configured on the interface.
INFO:root:   Device: PDX-RO
INFO:root:   Command: show ip bgp neighbors | in tcp
INFO:root:   Command output: 
show ip bgp neighbors | in tcp
  Transport(tcp) path-mtu-discovery is enabled
  Transport(tcp) path-mtu-discovery is enabled
  Transport(tcp) path-mtu-discovery is enabled
PDX-RO#
INFO:root:
...............................

INFO:root:   Cisco DNA Center Suggested Action 3: Ping the BGP peer with max interface MTU and 'do not fragment' bit set.
INFO:root:   Device: PDX-RO
INFO:root:   Command: ping 10.93.131.2 size 1500 df
INFO:root:   Command output: 
ping 10.93.131.2 size 1500 df
Type escape sequence to abort.
Sending 5, 1500-byte ICMP Echos to 10.93.131.2, timeout is 2 seconds:
Packet sent with the DF bit set
.....
Success rate is 0 percent (0/5)
PDX-RO#
INFO:root:
...............................

INFO:root:   Cisco DNA Center Suggested Action 4: Check BGP summary.
INFO:root:   Device: PDX-RO
INFO:root:   Command: show ip bgp all summary
INFO:root:   Command output: 
show ip bgp all summary
For address family: IPv4 Unicast
BGP router identifier 10.93.141.23, local AS number 65002
BGP table version is 175, main routing table version 175
2 network entries using 496 bytes of memory
2 path entries using 272 bytes of memory
2/2 BGP path/bestpath attribute entries using 576 bytes of memory
1 BGP AS-PATH entries using 24 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 1368 total bytes of memory
BGP activity 88/86 prefixes, 88/86 paths, scan interval 60 secs
4 networks peaked at 12:42:53 Apr 22 2024 PDT (5w3d ago)

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.93.131.2     4        65004       0       0        1    0    0 00:02:16 Idle
10.93.141.17    4        65003  140404  140487      175    0    0 3w1d            1
10.93.141.42    4        65001       0       0        1    0    0 3w1d     Idle
PDX-RO#
INFO:root:
--------------------------------------------------------------------

INFO:root: Knowledgebase CLI commands:
INFO:root:    show running | sec bgp
INFO:root:    show logging
INFO:root:    show ip interface bri
INFO:root:    show cdp neighbors detail
INFO:root:    show ip route bgp
INFO:root:  
INFO:root: Knowledgebase commands execution started
INFO:root: Task Id: 018fce51-b4fd-7585-895f-a7b29fdcd87b
INFO:root: Knowledgebase commands execution completed
INFO:root: Commands output file Id: 45f2c18d-6c3c-481b-9d42-bcf2eec1c3af

INFO:root: Knowledgebase CLI commands output:
INFO:root:
...............................
    show ip interface bri
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.93.141.41    YES NVRAM  up                    up      
GigabitEthernet2       10.93.131.1     YES NVRAM  administratively down down    
GigabitEthernet3       unassigned      YES NVRAM  down                  down    
Loopback1              10.93.141.23    YES NVRAM  up                    up      
PDX-RO#
INFO:root:
...............................
    show running | sec bgp
router bgp 65002
 bgp log-neighbor-changes
 timers bgp 15 45 30
 neighbor 10.93.131.2 remote-as 65004
 neighbor 10.93.141.17 remote-as 65003
 neighbor 10.93.141.17 ebgp-multihop 5
 neighbor 10.93.141.42 remote-as 65001
 neighbor 10.93.141.42 ebgp-multihop 5
 !
 address-family ipv4
  network 10.93.141.23 mask 255.255.255.255
  neighbor 10.93.131.2 activate
  neighbor 10.93.141.17 activate
  neighbor 10.93.141.42 activate
 exit-address-family
snmp-server enable traps bgp
snmp-server enable traps bgp cbgp2
PDX-RO#
INFO:root:
...............................
    show logging
Syslog logging: enabled (0 messages dropped, 3 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)

No Active Message Discriminator.



No Inactive Message Discriminator.


    Console logging: level emergencies, 0 messages logged, xml disabled,
                     filtering disabled
    Monitor logging: level debugging, 43 messages logged, xml disabled,
                     filtering disabled
    Buffer logging:  level debugging, 40333 messages logged, xml disabled,
                    filtering disabled
    Exception Logging: size (4096 bytes)
    Count and timestamp logging messages: disabled
    Persistent logging: disabled

No active filter modules.

    Trap logging: level informational, 42592 message lines logged
        Logging to 10.93.141.37  (udp port 8514, audit disabled,
              link up),
              42591 message lines logged, 
              0 message lines rate-limited, 
              0 message lines dropped-by-MD, 
              xml disabled, sequence number disabled
              filtering disabled
        Logging to 10.93.141.45  (udp port 514, audit disabled,
              link up),
              42592 message lines logged, 
              0 message lines rate-limited, 
              0 message lines dropped-by-MD, 
              xml disabled, sequence number disabled
              filtering disabled
        Logging to 10.93.141.37  (udp port 514, audit disabled,
              link up),
              42592 message lines logged, 
              0 message lines rate-limited, 
              0 message lines dropped-by-MD, 
              xml disabled, sequence number disabled
              filtering disabled
        Logging Source-Interface:       VRF Name:
        Loopback1                       
    TLS Profiles: 

Log Buffer (8192 bytes):
acenter] [Source: 10.93.141.45] [localport: 22] at 03:16:12 PDT Fri May 31 2024
May 31 03:16:12: %SYS-6-LOGOUT: User dnacenter has exited tty session 1(10.93.141.45)
May 31 03:16:12: %DMI-5-AUTH_PASSED: R0/0: dmiauthd: User 'dnacenter' authenticated successfully from 10.93.141.45:5279 and was authorized for netconf over ssh. External groups: PRIV15
May 31 03:16:12: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:12 PDT Fri May 31 2024
May 31 03:16:17: %DMI-5-AUTH_PASSED: R0/0: dmiauthd: User 'dnacenter' authenticated successfully from 10.93.141.45:58268 and was authorized for netconf over ssh. External groups: PRIV15
May 31 03:16:18: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:18 PDT Fri May 31 2024
May 31 03:16:18: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:18 PDT Fri May 31 2024
May 31 03:16:19: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:19 PDT Fri May 31 2024
May 31 03:16:19: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:19 PDT Fri May 31 2024
May 31 03:16:19: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:19 PDT Fri May 31 2024
May 31 03:16:19: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:19 PDT Fri May 31 2024
May 31 03:16:20: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:20 PDT Fri May 31 2024
May 31 03:16:23: %SYS-6-LOGOUT: User dnacenter has exited tty session 1(10.93.141.45)
May 31 03:16:23: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:23 PDT Fri May 31 2024
May 31 03:16:25: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:16:25 PDT Fri May 31 2024
May 31 03:16:29: %DMI-5-AUTH_PASSED: R0/0: dmiauthd: User 'dnacenter' authenticated successfully from 10.93.141.45:31790 and was authorized for netconf over ssh. External groups: PRIV15
May 31 03:18:34: %SYS-6-LOGOUT: User dnacenter has exited tty session 1(10.93.141.45)
May 31 03:29:35: %PKI-3-CRL_FETCH_FAIL: CRL fetch for trustpoint DNAC-CA failed
                      Reason : Enrollment URL not configured.
May 31 03:46:12: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:12 PDT Fri May 31 2024
May 31 03:46:12: %SYS-6-LOGOUT: User dnacenter has exited tty session 1(10.93.141.45)
May 31 03:46:12: %DMI-5-AUTH_PASSED: R0/0: dmiauthd: User 'dnacenter' authenticated successfully from 10.93.141.45:14091 and was authorized for netconf over ssh. External groups: PRIV15
May 31 03:46:12: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:12 PDT Fri May 31 2024
May 31 03:46:18: %DMI-5-AUTH_PASSED: R0/0: dmiauthd: User 'dnacenter' authenticated successfully from 10.93.141.45:21177 and was authorized for netconf over ssh. External groups: PRIV15
May 31 03:46:18: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:18 PDT Fri May 31 2024
May 31 03:46:19: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:19 PDT Fri May 31 2024
May 31 03:46:19: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:19 PDT Fri May 31 2024
May 31 03:46:19: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:19 PDT Fri May 31 2024
May 31 03:46:19: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:19 PDT Fri May 31 2024
May 31 03:46:20: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:20 PDT Fri May 31 2024
May 31 03:46:20: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:20 PDT Fri May 31 2024
May 31 03:46:23: %SYS-6-LOGOUT: User dnacenter has exited tty session 1(10.93.141.45)
May 31 03:46:23: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:23 PDT Fri May 31 2024
May 31 03:46:25: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 03:46:25 PDT Fri May 31 2024
May 31 03:46:29: %DMI-5-AUTH_PASSED: R0/0: dmiauthd: User 'dnacenter' authenticated successfully from 10.93.141.45:28205 and was authorized for netconf over ssh. External groups: PRIV15
May 31 03:48:33: %SYS-6-LOGOUT: User dnacenter has exited tty session 1(10.93.141.45)
May 31 03:54:16: %PKI-3-CRL_FETCH_FAIL: CRL fetch for trustpoint DNAC-CA failed
                      Reason : Enrollment URL not configured.
May 31 04:00:51: %DMI-5-AUTH_PASSED: R0/0: dmiauthd: User 'demotme' authenticated successfully from 10.93.141.47:51318 and was authorized for netconf over ssh. External groups: PRIV15
May 31 04:00:52: %BGP-5-NBR_RESET: Neighbor 10.93.131.2 reset (Interface flap)
May 31 04:00:52: %DUAL-5-NBRCHANGE: EIGRP-IPv4 123: Neighbor 10.93.131.2 (GigabitEthernet2) is down: interface down
May 31 04:00:52: %BGP-5-ADJCHANGE: neighbor 10.93.131.2 Down Interface flap
May 31 04:00:52: %BGP_SESSION-5-ADJCHANGE: neighbor 10.93.131.2 IPv4 Unicast topology base removed from session  Interface flap
May 31 04:00:52: %SYS-5-CONFIG_P: Configured programmatically by process iosp_vty_100001_dmiauthd_fd_174 from console as NETCONF on vty63
May 31 04:00:52: %DMI-5-CONFIG_I: R0/0: dmiauthd: Configured from NETCONF/RESTCONF by demotme, transaction-id 9351
May 31 04:00:54: %LINK-5-CHANGED: Interface GigabitEthernet2, changed state to administratively down
May 31 04:00:55: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet2, changed state to down
May 31 04:01:18: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:01:18 PDT Fri May 31 2024
May 31 04:02:36: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:36 PDT Fri May 31 2024
May 31 04:02:36: %SYS-6-LOGOUT: User dnacenter has exited tty session 2(10.93.141.45)
May 31 04:02:36: %DMI-5-AUTH_PASSED: R0/0: dmiauthd: User 'dnacenter' authenticated successfully from 10.93.141.45:21252 and was authorized for netconf over ssh. External groups: PRIV15
May 31 04:02:36: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:36 PDT Fri May 31 2024
May 31 04:02:39: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:39 PDT Fri May 31 2024
May 31 04:02:39: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:39 PDT Fri May 31 2024
May 31 04:02:39: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:39 PDT Fri May 31 2024
May 31 04:02:40: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:40 PDT Fri May 31 2024
May 31 04:02:40: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:40 PDT Fri May 31 2024
May 31 04:02:40: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:40 PDT Fri May 31 2024
May 31 04:02:40: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:40 PDT Fri May 31 2024
May 31 04:02:41: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:41 PDT Fri May 31 2024
May 31 04:02:43: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: dnacenter] [Source: 10.93.141.45] [localport: 22] at 04:02:43 PDT Fri May 31 2024
PDX-RO#
INFO:root:
...............................
    show cdp neighbors detail
-------------------------
Device ID: ISE26
Entry address(es): 
  IP address: 10.93.141.40
Platform: ISE-VM-K9,  Capabilities: Host 
Interface: GigabitEthernet1,  Port ID (outgoing port): eth0
Holdtime : 123 sec

Version :
Cisco Identity Services Engine version: 2.6.0.156 Copyright (c) 2024 Cisco Systems.

advertisement version: 2

-------------------------
Device ID: C9800-CL
Entry address(es): 
  IP address: 10.93.141.38
Platform: cisco C9800-CL,  Capabilities: Router IGMP 
Interface: GigabitEthernet1,  Port ID (outgoing port): GigabitEthernet2
Holdtime : 168 sec

Version :
Cisco IOS Software [Amsterdam], C9800-CL Software (C9800-CL-K9_IOSXE), Version 17.3.7, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2023 by Cisco Systems, Inc.
Compiled Fri 24-Mar-23 02:56 by mcpre

advertisement version: 2
VTP Management Domain: ''
Duplex: full
Management address(es): 
  IP address: 10.93.141.38

-------------------------
Device ID: C9800-CL
Entry address(es): 
  IP address: 10.93.141.38
Platform: cisco C9800-CL,  Capabilities: Router IGMP 
Interface: GigabitEthernet1,  Port ID (outgoing port): GigabitEthernet1
Holdtime : 159 sec

Version :
Cisco IOS Software [Amsterdam], C9800-CL Software (C9800-CL-K9_IOSXE), Version 17.3.7, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2023 by Cisco Systems, Inc.
Compiled Fri 24-Mar-23 02:56 by mcpre

advertisement version: 2
VTP Management Domain: ''
Duplex: full
Management address(es): 
  IP address: 10.93.141.38

-------------------------
Device ID: PDX-RN
Entry address(es): 
  IP address: 10.93.141.42
Platform: cisco CSR1000V,  Capabilities: Router IGMP 
Interface: GigabitEthernet1,  Port ID (outgoing port): GigabitEthernet1
Holdtime : 145 sec

Version :
Cisco IOS Software [Amsterdam], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.3.8a, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2023 by Cisco Systems, Inc.
Compiled Fri 20-Oct-23 15:48 by mcpre

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 10.93.141.42


Total cdp entries displayed : 4
PDX-RO#
INFO:root:
...............................
    show ip route bgp
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is 10.93.141.33 to network 0.0.0.0

      10.0.0.0/8 is variably subnetted, 13 subnets, 5 masks
B        10.93.130.0/24 [20/0] via 10.93.141.17, 3w1d
PDX-RO#
INFO:root: App "Network Troubleshooting.py" run end, 2024-05-31 04:04:14
[Pipeline] }
[Pipeline] // dir
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] echo


Jenkins Network Troubleshooting build end
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // timeout
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // withCredentials
[Pipeline] }
$ docker stop --time=1 89cd2b338ba375f2a5f817f1f10c67c626bb21e44b79c1c83164283c964b520e
$ docker rm -f --volumes 89cd2b338ba375f2a5f817f1f10c67c626bb21e44b79c1c83164283c964b520e
[Pipeline] // withDockerContainer
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```