This is a short python script to update NearlyFreeSpeech.net DNS records.

This is useful for dynamic DNS applications, where you want to point
DNS records for a domain or subdomain at a computer whose IP address
may change.

USAGE
=====
The python script update_dns.py is configured with the following environment variables:

NFS_DNS_USER
------------
The username for authentication

NFS_DNS_APIKEY
------------
nearly free speech API key. See [NFS API Introduction](https://members.nearlyfreespeech.net/wiki/API/Introduction) for details


NFS_DNS_DOMAIN
--------------
The domain to adjust DNS records on

NFS_DNS_SUBDOMAIN
----------------
The subdomain to adjust DNS
records. If you want to update the A record of the domain, please set
an empty string for the environment variable

LICENSE
======
The work in this repository is licensed under MIT LICENSE


This repository takes advantage of the helper functions from
[python-nfs](https://github.com/ktdreyer/python-nfsn) for calculating
the authentication headers for API requests. This is licensed as CC0,
which allows this work to retain an MIT license
