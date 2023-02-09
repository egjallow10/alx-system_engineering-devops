Issue Summary:
 Duration: The outage occurred on January 15th, 2023 from 9:30 AM to 11:30 AM (UTC -5). Impact: During the outage, the website's login feature was unavailable to all users, resulting in 100% of users being affected. Users were unable to access their accounts and complete their transactions. Root Cause: The root cause of the outage was a network connectivity issue between the web server and the database server.
Timeline:
9:30 AM: The issue was detected when customers began complaining about the inability to log in to their accounts.
9:45 AM: An engineer was notified of the issue through a monitoring alert and started investigating the issue.
10:00 AM: The engineer discovered that the web server was unable to communicate with the database server, causing the login feature to be unavailable.
10:15 AM: The engineer assumed that the issue was caused by a firewall issue and started investigating the firewall configurations.
10:30 AM: The investigation revealed that the firewall configurations were correct and that the issue was not related to the firewall.
10:45 AM: The incident was escalated to the network team for further investigation.
11:00 AM: The network team discovered that there was a network connectivity issue between the web server and the database server, which was causing the login feature to be unavailable.
11:15 AM: The network team resolved the connectivity issue by reconfiguring the network settings.
11:30 AM: The login feature was restored and all systems were functioning normally.
Root Cause and Resolution: 
The root cause of the outage was a network connectivity issue between the web server and the database server. This issue was caused by a misconfiguration of the network settings, which resulted in a loss of connectivity between the two servers. To resolve the issue, the network team reconfigured the network settings, which restored the connectivity between the web server and the database server and made the login feature available again.
Corrective and Preventative Measures: The following corrective and preventative measures have been taken to avoid similar outages in the future:
Implement regular checks of network configurations to prevent misconfigurations from occurring.
Implement monitoring for network connectivity between critical servers to quickly detect connectivity issues.
Implement a network failover plan to ensure that critical services remain available even in the event of network connectivity issues.
Regularly review and update the incident response plan to ensure that incidents are handled efficiently and effectively in the future.


