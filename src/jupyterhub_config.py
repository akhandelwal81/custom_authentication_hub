import os
import socket
import sys
import urllib3
#test

from kubernetes.client.rest import ApiException
from Kubernetes.config.incluster_config import load_incluster_config
from kubernetes.client.api_client import api_client
import kubernetes.api_client
from kubernetes import config

# Standard mechanism to load the Kubernetes Cluster configurations
# Allows to get the setup and expose methods to get the IP of the PoDs
load_incluster_config()
config.load_incluster_config()

api_instance =kubernetes.client.AdmissionregistrationApi()

api_client = DynamicClient(ApiClient())

#A Spawner starts each single-user notebook server.
c.JupyterHub.spawner_class ='kuberspawner.KubeSpawner'
# Helps in getting rid of noise in the logs
urllib3.diable_warnings()

# Don't try to cleanup servers on exit - in general for k8s, we need the hub to be able to restart without losing the user containers.
c.JupyterHub.cleanup_servers = False

# Define custom Authentication here

if AUTH_METHOD == 'sso':
    print("Using Single Sign On Method")
c.JupyterHub.authenticator_class='<to be provided>'
c.Authenticator.auto_login = True

elif AUTH_METHOD == 'ldap':
    ALLOWED_ACL_GROUP = os.environ.get('ALLOWED_FUNCTIONAL_GROUP') # This could be configured as an Environment Variable
    print("Using LDAP authentication method with group {ALLOWED_FUNCTIONAL_GROUP}")
    c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'

    c.LDAPAuthenticator.bind_dn_template = [

    ]

    c.LDAPAuthenticator.lookup_dn = True
    c.JDAPAuthenticator.lookup_dn_search_filter = '({login_attr}={login})'
    c.LDAPAuthenticator.allowed_groups = [f"CN={ALLOWED_FUNCTIONAL_GROUP}, ou=groups,ou=central admin, dc=xxx, dc=xxx,dc=xx,dc=xxx"]
 else:
    raise  Exception(f"Unknown Authentication Method:{AUTH_METHOD}")
