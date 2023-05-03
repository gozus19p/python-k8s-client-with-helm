# Python K8s Client

Made with study purposes, this project is a simple Python client for Kubernetes API.

## Helm commands

```bash
#!/bin/bash

echo "Installing Helm Chart..."
export KUBECONFIG=~/.kube/config

helm install my-chart ./helm-chart

echo "Upgrading Helm Chart..."
helm upgrade my-chart ./helm-chart
```

Under `helm-chart/values.yaml` you can find the default values for the chart.
For each element of `serviceNames` array, a configmap will be created with the name `<service-name>-config`.