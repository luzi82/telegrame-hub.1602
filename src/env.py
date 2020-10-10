import futsu.storage
import os

STAGE = os.environ['STAGE']
CONF_PATH = os.environ['CONF_PATH']
PUBLIC_STATIC_PATH       = os.environ['PUBLIC_STATIC_PATH']
PUBLIC_MUTABLE_PATH      = os.environ['PUBLIC_MUTABLE_PATH']
PUBLIC_STATIC_HTTP_PATH  = os.environ['PUBLIC_STATIC_HTTP_PATH']
PUBLIC_MUTABLE_HTTP_PATH = os.environ['PUBLIC_MUTABLE_HTTP_PATH']
PRIVATE_STATIC_PATH      = os.environ['PRIVATE_STATIC_PATH']
PRIVATE_MUTABLE_PATH     = os.environ['PRIVATE_MUTABLE_PATH']
DB_TABLE_NAME            = os.environ['DB_TABLE_NAME']
DYNAMODB_ENDPOINT_URL    = os.environ.get('DYNAMODB_ENDPOINT_URL',None)
DYNAMODB_REGION          = os.environ.get('DYNAMODB_REGION',None)

VERSION = 'v1602327422'

PRIVATE_MUTABLE_VERSION_PATH = futsu.storage.join(PRIVATE_MUTABLE_PATH,VERSION)

SETUP_TG_AUTH_BOT_DATA_PATH = futsu.storage.join(PRIVATE_MUTABLE_VERSION_PATH,'SETUP','TG_AUTH_BOT_DATA.json')
SETUP_SET_DOMAIN_DONE_PATH = futsu.storage.join(PRIVATE_MUTABLE_VERSION_PATH,'SETUP','SET_DOMAIN_DONE')
SETUP_DONE_PATH = futsu.storage.join(PRIVATE_MUTABLE_VERSION_PATH,'SETUP','DONE')
