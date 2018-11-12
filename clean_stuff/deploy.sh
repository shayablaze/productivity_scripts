cd ~/Desktop/repos/bzdev && source bzdev-venv/bin/activate && python bzdev.py env deploy --id  126
kubectl scale deploy dpl-backend-worker-scheduler-126-ajzye01-shayablaze --replicas=5
kubectl scale deploy dpl-backend-worker-126-ajzye01-shayablaze --replicas=200
kubectl get deploy