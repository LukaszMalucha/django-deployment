### CAP ROVER

ssh root@64......

ufw allow 80,443,3000,996,7946,4789,2377/tcp; ufw allow 7946,4789,2377/udp; 

docker run -p 80:80 -p 443:443 -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock -v /captain:/captain caprover/caprover 

sudo netstat -pna | grep 3000

npm install -g caprover

caprover serversetup

Paste IP only




