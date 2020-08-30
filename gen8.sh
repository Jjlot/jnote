yum install samba git nfs

vim /etc/samba/smb.conf

smbpasswd -a root

systemctl enable smb

git config --global user.name "Jjlot"
git config --global user.email "jingran84@163.com"


showmount --all

showmount -e 127.0.0.1

vim /etc/exports


firewall-cmd --zone=public --add-port=139/tcp --permanent
firewall-cmd --zone=public --add-port=445/tcp --permanent
firewall-cmd --zone=public --add-port=137/udp --permanent
firewall-cmd --zone=public --add-port=138/udp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=111/tcp --permanent
firewall-cmd --zone=public --add-port=111/udp --permanent

systemctl enable firewalld
firewall-cmd --reload
systemctl restart firewalld.service

vim /etc/fstab


