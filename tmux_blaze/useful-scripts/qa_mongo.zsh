kubectl -n ns-jenkins port-forward $(kubectl get pods -n ns-jenkins -l role=mongo -o yaml | grep "name: dpl-mongo-79-jenkins-qa*" | head -n 1 | cut -d':' -f2 | awk '{print $1}') 27016:27017
