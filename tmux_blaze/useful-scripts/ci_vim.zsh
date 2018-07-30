#!/bin/zsh

kubectl -n ns-jenkins exec -it  $(kubectl get pods -n ns-jenkins -l role=backend-worker -o yaml | grep "name: dpl-backend-worker-67-jenkins-ci*" | head -n 1 | cut -d':' -f2 | awk '{print $1}') -- sh -c "apt-get install vim; bash"
