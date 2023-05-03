from kubernetes import client, config

config.load_config()


def read_configmap(configmap_name: str) -> dict:
    """
    Read a configmap from the cluster and return it as a V1ConfigMap object
    :return: V1ConfigMap
    """
    if not configmap_name:
        raise ValueError("configmap_name must be specified")
    v1 = client.CoreV1Api()
    configmap = v1.read_namespaced_config_map(name=configmap_name, namespace="default")
    # convert to dict
    return configmap.data


def read_secret(secret_name: str):
    """
    Read a secret from the cluster and return it as a V1Secret object
    :param secret_name:
    :return:
    """
    if not secret_name:
        raise ValueError("secret_name must be specified")
    v1 = client.CoreV1Api()
    secret = v1.read_namespaced_secret(name=secret_name, namespace="default")
    # convert to dict
    return secret.data
