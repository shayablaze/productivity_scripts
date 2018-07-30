#!/bin/zsh
kubectl -n ns-jenkins exec -i  $(kubectl get pods -n ns-jenkins -l role=backend-worker -o yaml | grep "name: dpl-backend-worker-79-jenkins-qa*" | head -n 1 | cut -d':' -f2 | awk '{print $1}') -- sh -c "tail -f /var/log/blazemeter/blazemeter.log.json" | jq -r
