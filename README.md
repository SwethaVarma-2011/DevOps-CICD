# DevOps-CICD

# Docker commands
docker build -t <pathOfTheDockerfile>  # To build docker image from docker file
docker run --name <containerName> -p 8080:8080 -it <image_name>   # To create a container of that image

# Kubernetes Commands
kubectl get all # To get all pods(deployment,service)
kubectl get deployment/service/pod <PodName>  # To get any particular pod
kubectl describe pod <PodName>  # to get all details of the pod
kubectl describe pod <PodName> -o yaml > <FileName> # To describe the pod and copy the output of the pod to the new file in local
kubectl delete -f <FileName>  # To delete the file along with the pod in kubuernetes
kubectl apply -f <FileName> # to create the pod


# helm commands
helm create <chartName>  -# To create helm chart
helm install <ChartReleaseName> <PathofTheChart> # (helm install web-app ./python-web-app) It will automatically creates the all pods in the template folder.
helm list (To list the chartReleases)
helm upgrade <ChartReleaseName> <PathofTheChart> # It creates new revision of the chart release
helm uninstall <ChartReleaseName>   # To delete the Chart Release.To delete all pods

