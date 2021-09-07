import re
from jupyterhub.auth import Authenticator
import ldap3
from ldap3.utils.conv import escape_filter_chars
from tornado import gen
from traitlets import Unicode, INT, Bool, List, Union

class LDAPAuthenticator(Authenticator):
  server_address = Unicode(
    config=True,
    help="""
    Address of the LDAP Server to contact
    Could be an IP or Host Name
    """
  )
  server_port = Int(
    config=True,
    help="""
    Port on which to contact the LDAP Server
    
    Defaults to '636' if 'use_ssl' is set , '389' otherwise.
    """
  )
