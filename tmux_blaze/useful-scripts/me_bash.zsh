#!/bin/zsh

kubectl exec -it $(kubectl get pods -l role=bza -o jsonpath="{.items[0].metadata.name}") -- sh -c "cd /home/blazemeter/vol/www/a.blazemeter.com/; touch bla.txt; bash"
