# Secret passphrase
# FIXME: Temporarily SECRET must have the same value as SECRET_KEYS
#        due to the current spring boot implementation
SECRET = '/etc/keyczar/keys'
# Secret keyczar keys
SECRET_KEYS = '/etc/keyczar/keys'
# Fill as needed
DEBUG = True
IGNORE_AUTH = False
# SECRET_KEY = 'admin'
CONSUL_ENDPOINT = 'http://consul:8500/v1/kv'
