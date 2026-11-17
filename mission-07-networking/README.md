# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 was to investigate how computers talk to one another across local and global networks:
- Explain core networking terms (LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, Client-Server) with practical examples.
- Use command-line tools (`ping` and `nslookup`) to test network connectivity and perform domain name resolution.
- Understand the role of DNS in web browsing.
- Detail the step-by-step journey of what happens when a user types a website address into a browser until the page appears.

---

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A network covering a small, localized physical area like a single home, classroom, or office building, enabling high-speed local data sharing. | College computer lab where 40 desktops are connected via Ethernet cables to share a local lab printer and file server. |
| **MAN (Metropolitan Area Network)** | A network spanning a city or large university campus, larger than a LAN but smaller than a WAN. | A municipal cable TV network or a connected multi-campus network across Bengaluru city. |
| **WAN (Wide Area Network)** | A network covering large geographical areas across cities, states, or countries, often connected through fiber-optic cables and satellites. | The global Internet, connecting computers and data centers worldwide across continents. |
| **DNS (Domain Name System)** | The "phonebook" of the Internet; it translates human-friendly domain names into machine-readable IP addresses. | Translating `example.com` into the IP address `172.66.147.243`. |
| **Router** | A specialized network device that forwards data packets between different networks by inspecting destination IP addresses. | Your home Wi-Fi router, which connects personal devices in your home LAN to your ISP's wide-area network. |
| **Protocol** | A standardized set of rules and message formats that communicating computers must follow to exchange data correctly. | HTTP / HTTPS for loading web pages, TCP for reliable packet delivery, and IP for network addressing. |
| **Packet switching** | The method of slicing digital data into small chunks (packets), sending them independently across network paths, and reassembling them at the destination. | Streaming music or downloading a file where chunks take different network routes and get reordered by your device. |
| **Client-server** | An architecture where client devices request services or data, and dedicated central server computers respond and fulfill those requests. | Your web browser (the client) requesting a web page from GitHub's web servers (the server). |

---

### Task 7.2 — Observe network information

#### Terminal Connectivity & DNS Lookup Output:
```bash
# Testing connectivity to a public example domain
ping -c 3 example.com
```
*Output observed:*
```text
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=54 time=50.0 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=54 time=84.3 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=54 time=52.5 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 50.0/62.3/84.3/15.5 ms
```

```bash
# Querying DNS records for example.com
nslookup example.com
```
*Output observed:*
```text
Server:		[redacted-dns-server]
Address:	[redacted-dns-server]#53

Non-authoritative answer:
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 172.66.147.243
```

#### Questions answered:
- **What a connectivity test helps you check:**
  A tool like `ping` sends ICMP Echo Request packets to a target IP or domain to verify whether the remote server is alive and reachable. It measures packet loss (0.0% here means connection is rock solid) and round-trip latency (average 62.3 ms here), showing how fast signals travel between your machine and the server.
- **What information a DNS lookup displays:**
  `nslookup` displays which local DNS resolver handled the query (`[redacted]#53`) and returns the target server's public IPv4/IPv6 addresses (e.g. `104.20.23.154` and `172.66.147.243`).
- **Role of DNS when entering a website name:**
  Routers and network hardware do not understand English names like `example.com` — they only route packets by numerical IP addresses. When a user types a name, the browser immediately contacts DNS to look up the associated IP address so it knows where to direct the connection.

---

### Task 7.3 — What happens when you open a website?

1. **User Request & URL Input (Client):**
   The user types `https://example.com` into the web browser (the client) and presses Enter. The browser parses the URL into the protocol (`https://`), domain name (`example.com`), and resource path.
2. **DNS Resolution (Client to DNS):**
   The client checks its internal browser cache and operating system DNS cache. If the IP address is not cached, the client sends a DNS query packet to a recursive DNS resolver. The DNS resolver looks up `example.com` and returns its IP address (e.g. `172.66.147.243`).
3. **Establishing Connection via TCP & TLS (Router & Protocols):**
   Armed with the server's IP address, the client initiates a TCP 3-way handshake (`SYN`, `SYN-ACK`, `ACK`) using the TCP/IP protocol. Data travels through the local Wi-Fi router, through the ISP network, and across internet routers via packet switching. Because HTTPS is used, an additional TLS handshake takes place to exchange cryptographic keys and encrypt the session.
4. **Sending HTTP Request (Client to Server):**
   Over the encrypted channel, the browser client sends an HTTP `GET` request packet asking the web server for the website files.
5. **Server Processing & Response (Server):**
   The remote server at `172.66.147.243` accepts the request packet, checks for the requested webpage, and replies with an HTTP response packet containing a status code (`200 OK`) and the file payload (HTML, CSS, JavaScript, and images).
6. **Rendering the Page (Client):**
   The client browser receives the data packets, reassembles them in correct order, parses the HTML markup, applies CSS styling, executes JavaScript, and renders the visual webpage on the user's screen.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Sent 3 ICMP echo packets to test reachability, latency, and packet loss.
- `nslookup example.com`: Queried DNS servers to resolve domain name into public IP addresses.

## 4. My understanding
- Networks are structured layers: applications use high-level protocols like HTTP, while underlying network devices route binary packets using IP and TCP.
- Without DNS, we would have to memorize long sequences of numbers for every single website we visit.
- Packet switching is resilient: large files are split into tiny packets that can take different routes across the internet and be reassembled without dropping the entire download if one packet drops.

## 5. Difficulties faced
- In macOS, `ping` continues running forever until you press `Ctrl+C`.

## 6. How I resolved them
- I learned to use the `-c 3` flag (`ping -c 3 example.com`), which automatically stops after sending 3 packets.

## 7. Evidence / files
- `mission-07-networking/README.md` (this file)

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Branch:** `main`
- **Pushed to GitHub:** Yes
