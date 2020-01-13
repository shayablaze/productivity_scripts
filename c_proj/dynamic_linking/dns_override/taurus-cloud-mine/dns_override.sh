 export LD_PRELOAD=/usr/lib/libhostspriv.so
 echo "127.0.0.1 shaya_1" >> aaa
 echo "127.0.0.1 www.blazedemo.com" >> aaa
 echo "127.0.0.1 blazedemo.com" >> aaa
# echo "ynet.co.il nfl.com" >> aaa
 echo "*************************"
 curl www.blazedemo.com
 echo "*************************"
 curl shaya_2