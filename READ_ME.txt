Purpose:
    this script generates random IPv4 addresses. After an address is generated,
    the SYN packet is sent to the address on port 21 (standard FTP port). If a
    SYN/ACK packet is received, then 21 is confirmed open.

    If an open FTP service is running on the endpoint, the script will then
    attempt to establish a session via 'anonymous login' or a non-credentialed
    login. If the server (and believe it or not, there are more than a few) allows
    anonymous logins, the script will finally upload the user-specified payload
    to the server.

Technique:
    When dropping backdoors, shells, bots, etc, it is beneficial to give the payload
    a convincing naming convention, ex: 'payload_money_generator.exe' or 'porn.elf.'
    Of course, choosing payloads that are closed-source (compiled) are going to be
    your best bet since obviously no one can edit and figure out the intent behind
    the file.

Responsibility:
    This script is a proof-of-concept and should be modified only to probe IP/s
    and/or IP range/s that the end-user has explicit permission to scan.

    By modifying, copying, re-distributing, and executing this script, you are
    hereby baring full legal and ethical responsibility for actions intened and
    unintended that arises from use of this script.

Known bugs:
    In order to send SYN probes, the Scapy library is used. The downside is that
    when sending the <CTRL+C> SIGINT signal that is used to abort operating, it
    sometimes becomes ignored and spamming <CTRL+C> a few consecutive times will
    do the trick to end the script.

    Although this is unprofessional, I've spent quite some time trying to
    mitigate this issue, but to no avail I'm still working out this ongoing bug.

    If anyone beat me to a solutionn, please reach out.

Enjoy!
