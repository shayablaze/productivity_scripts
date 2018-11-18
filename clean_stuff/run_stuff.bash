#python destroy_masters.py
mongo --port 27019 < mongo_clean.sh
redis-cli -p 6378 < redis_clean.sh
cd /Users/ajzye01/Desktop/repos/productivity_scripts/clean_stuff
redis-cli -p 6378 < redis_clean.sh
