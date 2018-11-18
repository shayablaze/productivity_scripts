current_dir=$(dirname $0)
. ${current_dir}/creds
curl 'https://bza-126-ajzye01-shayablaze.env.blazemeter.net/api/v4/admin/tag-terminate?env=bza-126-ajzye01-shayablaze.env.blazemeter.net&locationId=ap-northeast-2' -X POST 'Content-Type: text/plain;charset=UTF-8' -H 'Accept: application/json' --user $user_info
