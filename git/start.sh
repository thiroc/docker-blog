#!/bin/sh

cd /home/git

# If there is some public key in keys folder
# then it copies its contain in authorized_keys file
if [ "$(ls -A ./keys/)" ]; then
  cat ./keys/*.pub > .ssh/authorized_keys
  chown -R git:git .ssh
  chmod 700 .ssh
  chmod -R 600 .ssh/*
  chmod +r .ssh/authorized_keys
fi

# Checking permissions and fixing SGID bit in repo folder
chown -R git:git ./repo
chmod -R ug+rwX ./repo
find ./repo -type d -exec chmod g+s '{}' +
chmod ug+x ./repo/hooks/post-receive

# Change contents permission
chown -R git:git ./content
chmod -R ug+rw ./content

# -D flag avoids executing sshd as a daemon
/usr/sbin/sshd -D
