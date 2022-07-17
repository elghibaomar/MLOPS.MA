export KUBECONFIG=/Users/omarelghiba/Desktop/django-k8s/.kube/kubeconfig.yaml

kubectl create secret generic django-web-env-prod  --from-env-file=web/.env.prod

docker buildx build --platform=linux/amd64 -t registry.digitalocean.com/om-k8s/django-k8s-web:latest -f Dockerfile .

docker push registry.digitalocean.com/om-k8s/django-k8s-web --all-tags