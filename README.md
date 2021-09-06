# custom_authentication_hub
JupyterHub provides a Multi-user notebook environment. It basically helps in hosting a unified Jupyter Notebook server with an ability to host number of child notebook servers one for each user.

If you need a simple case for a small amount of users (0-100) and single server take a look at The Littlest JupyterHub distribution.

If you need to allow for even more users, a dynamic amount of servers can be used on a cloud, take a look at the Zero to JupyterHub with Kubernetes .

Based on the documentation available on the official site, there are 4 key sub-components that form a part of JupyterHub ecosystem-
* Hub - This is a tornado process and often referred as heart of the ecosysystem.
* Configurable Node Proxy - Node http proxy that recieves client request
* Multiple Single User Jupyter Notebook Servers - One Notebook Server per user and are all monitored by Spawners.
* Authentication Class- Manages the authentication of the users

Different authenticators control access to JupyterHub. The default one (PAM) uses the user accounts on the server where JupyterHub is running. If you use this, you will need to create a user account on the system for each user on your team. Using other authenticators, you can allow users to sign in with e.g. a GitHub account, or with any single-sign-on system your organization has.

In this repository, there is a sample implementation for LDAP and SSO based Authentication and it corresponding integration with JupyterHub in a Kubernest Environment.

# Installation of LDAP Authenticator for JupyterHub

You can install it from pip with:
'''
pip install jupyterhub-ldapauthenticator
'''

...or using conda with:
'''
conda install -c conda-forge jupyterhub-ldapauthenticator
'''
