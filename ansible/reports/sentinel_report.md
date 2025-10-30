# 🛰️ Rapport Nova Sentinel

**Horodatage :** 2025-10-30 20:22:15

## Informations Système
- **Hostname** : BASTION
- **Os** : Linux
- **Os_version** : #34~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Sep 23 15:35:20 UTC 2
- **Architecture** : x86_64
- **Kernel** : 6.14.0-34-generic

## CPU
- **Cpu percent** : 1.5
- **Cpu count** : 2

## Mémoire
- **Total mb** : 7893
- **Used mb** : 1070
- **Free mb** : 6519
- **Percent used** : 17.4

## Disque
- **Total gb** : 19.52
- **Used gb** : 10.5
- **Free gb** : 8.0
- **Percent used** : 56.8

## Réseau
- **lo** : 127.0.0.1
- **ens33** : 192.168.198.146
- **ens37** : 192.168.16.128

### Ports ouverts
```
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                 
udp   UNCONN 0      0            0.0.0.0:5353       0.0.0.0:*    users:(("avahi-daemon",pid=1221,fd=12))                
udp   UNCONN 0      0            0.0.0.0:47293      0.0.0.0:*    users:(("avahi-daemon",pid=1221,fd=14))                
udp   UNCONN 0      0         127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=624,fd=16))              
udp   UNCONN 0      0      127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=624,fd=14))              
udp   UNCONN 0      0               [::]:5353          [::]:*    users:(("avahi-daemon",pid=1221,fd=13))                
udp   UNCONN 0      0               [::]:34544         [::]:*    users:(("avahi-daemon",pid=1221,fd=15))                
tcp   LISTEN 0      4096       127.0.0.1:8200       0.0.0.0:*    users:(("vault",pid=3867,fd=7))                        
tcp   LISTEN 0      4096       127.0.0.1:8201       0.0.0.0:*    users:(("vault",pid=3867,fd=8))                        
tcp   LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=624,fd=17))              
tcp   LISTEN 0      4096       127.0.0.1:631        0.0.0.0:*    users:(("cupsd",pid=1654,fd=7))                        
tcp   LISTEN 0      4096         0.0.0.0:2222       0.0.0.0:*    users:(("sshd",pid=1665,fd=3),("systemd",pid=1,fd=244))
tcp   LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=624,fd=15))              
tcp   LISTEN 0      4096            [::]:2222          [::]:*    users:(("sshd",pid=1665,fd=4),("systemd",pid=1,fd=245))
tcp   LISTEN 0      4096           [::1]:631           [::]:*    users:(("cupsd",pid=1654,fd=6))                        

```

## Processus
- **Nombre total** : 310

## Sécurité (Optionnel)
### Fichiers SUID
/snap/core22/2045/usr/bin/chfn
/snap/core22/2045/usr/bin/chsh
/snap/core22/2045/usr/bin/gpasswd
/snap/core22/2045/usr/bin/mount
/snap/core22/2045/usr/bin/newgrp
/snap/core22/2045/usr/bin/passwd
/snap/core22/2045/usr/bin/su
/snap/core22/2045/usr/bin/sudo
/snap/core22/2045/usr/bin/umount
/snap/core22/2045/usr/lib/dbus-1.0/dbus-daemon-launch-helper

### Utilisateurs UID < 1000
root 0 /root
daemon 1 /usr/sbin
bin 2 /bin
sys 3 /dev
sync 4 /bin
games 5 /usr/games
man 6 /var/cache/man
lp 7 /var/spool/lpd
mail 8 /var/mail
news 9 /var/spool/news
uucp 10 /var/spool/uucp
proxy 13 /bin
www-data 33 /var/www
backup 34 /var/backups
list 38 /var/list
irc 39 /run/ircd
_apt 42 /nonexistent
systemd-network 998 /
systemd-timesync 996 /
dhcpcd 100 /usr/lib/dhcpcd
messagebus 101 /nonexistent
syslog 102 /nonexistent
systemd-resolve 991 /
uuidd 103 /run/uuidd
usbmux 104 /var/lib/usbmux
tss 105 /var/lib/tpm
systemd-oom 990 /
kernoops 106 /
whoopsie 107 /nonexistent
dnsmasq 999 /var/lib/misc
avahi 108 /run/avahi-daemon
tcpdump 109 /nonexistent
sssd 110 /var/lib/sss
speech-dispatcher 111 /run/speech-dispatcher
cups-pk-helper 112 /nonexistent
fwupd-refresh 989 /var/lib/fwupd
saned 113 /var/lib/saned
geoclue 114 /var/lib/geoclue
cups-browsed 115 /nonexistent
hplip 116 /run/hplip
gnome-remote-desktop 988 /var/lib/gnome-remote-desktop
polkitd 987 /
rtkit 117 /proc
colord 118 /var/lib/colord
gnome-initial-setup 119 /run/gnome-initial-setup/
gdm 120 /var/lib/gdm3
nm-openvpn 121 /var/lib/openvpn/chroot
sshd 122 /run/sshd
vault 997 /home/vault
