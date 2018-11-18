current_dir=$(dirname $0)
. ${current_dir}/creds

MASTER_ID='';
ENV='bza-126-ajzye01-shayablaze.env.blazemeter.net'
curl "https://bza-126-ajzye01-shayablaze.env.blazemeter.net/api/v4/admin/tag-terminate?env=$ENV&locationId=ap-northeast-2&masterId=$MASTER_ID" -X POST 'Content-Type: text/plain;charset=UTF-8' -H 'Accept: application/json' --user $user_info
