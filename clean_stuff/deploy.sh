kubectl exec -i $(kubectl get pods -l role=bza -o jsonpath="{.items[0].metadata.name}") -- rm /tmp/routes.php
cd ~/Desktop/repos/bzdev && pipenv shell && python bzdev.py env deploy --id  126
kubectl scale deploy dpl-backend-worker-scheduler-126-ajzye01-shayablaze --replicas=5
k scale deploy dpl-bza-126-ajzye01-shayablaze --replicas=5
kubectl scale deploy dpl-backend-worker-126-ajzye01-shayablaze --replicas=200
kubectl get deploy