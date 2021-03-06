import boto3 # type: ignore
import datetime
import endpoint_auth
import endpoint_hub
import endpoint_setup
import env
import flask
import flask_login # type: ignore
import fk
import futsu.json # type: ignore
import futsu.storage # type: ignore
import logging
import middleware
import os
import random
import telegram
import th
import werkzeug.middleware.proxy_fix

app = flask.Flask(__name__)
app.wsgi_app = middleware.WebTemplateMiddleWare(app.wsgi_app, app) # type: ignore
app.wsgi_app = werkzeug.middleware.proxy_fix.ProxyFix(app.wsgi_app) # type: ignore

STAGE = os.environ['STAGE']
CONF_PATH = os.environ['CONF_PATH']
PUBLIC_COMPUTE_URL_PREFIX   = os.environ['PUBLIC_COMPUTE_URL_PREFIX']
PUBLIC_STATIC_URL_PREFIX    = os.environ['PUBLIC_STATIC_URL_PREFIX']
PUBLIC_DEPLOYGEN_URL_PREFIX = os.environ['PUBLIC_DEPLOYGEN_URL_PREFIX']
PUBLIC_MUTABLE_URL_PREFIX   = os.environ['PUBLIC_MUTABLE_URL_PREFIX']
PUBLIC_TMP_URL_PREFIX       = os.environ['PUBLIC_TMP_URL_PREFIX']
PUBLIC_STATIC_PATH          = os.environ['PUBLIC_STATIC_PATH']
PUBLIC_MUTABLE_PATH         = os.environ['PUBLIC_MUTABLE_PATH']
PRIVATE_STATIC_PATH         = os.environ['PRIVATE_STATIC_PATH']
PRIVATE_MUTABLE_PATH        = os.environ['PRIVATE_MUTABLE_PATH']
DB_TABLE_NAME = os.environ['DB_TABLE_NAME']
DYNAMODB_ENDPOINT_URL = os.environ.get('DYNAMODB_ENDPOINT_URL',None)
DYNAMODB_REGION       = os.environ.get('DYNAMODB_REGION',None)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

configure_telegram = th.configure_telegram

app.secret_key = env.get_conf_data()['FLASK_SECRET'].encode('utf-8')

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

endpoint_auth.init_login_manager(login_manager)
endpoint_auth.add_url_rule(app)

endpoint_hub.add_url_rule(app)

endpoint_setup.add_url_rule(app)

#TODO: if setup not done, redirect to /setup
@app.route('/')
@flask_login.login_required
def index():
    now_ts = int(datetime.datetime.now().timestamp())

    private_dummy_path = futsu.storage.join(PRIVATE_STATIC_PATH,'private.txt')
    private_txt = futsu.storage.path_to_bytes(private_dummy_path).decode('utf-8')

    timestamp_path = futsu.storage.join(PRIVATE_MUTABLE_PATH,'timestamp')
    last_ts = futsu.storage.path_to_bytes(timestamp_path).decode('utf-8') if futsu.storage.is_blob_exist(timestamp_path) else -1
    futsu.storage.bytes_to_path(timestamp_path,f'{now_ts}'.encode('utf-8'))

    job0_timestamp_path = futsu.storage.join(PRIVATE_MUTABLE_PATH,'job0_timestamp')
    job0_ts = futsu.storage.path_to_bytes(job0_timestamp_path).decode('utf-8') if futsu.storage.is_blob_exist(job0_timestamp_path) else -1

    return flask.render_template('home.tmpl',
        PUBLIC_STATIC_URL_PREFIX = env.PUBLIC_STATIC_URL_PREFIX,
    )

@app.route('/compute_domain')
def get_compute_domain():
    conf_data = futsu.json.path_to_data(futsu.storage.join(CONF_PATH,'conf.json'))
    return conf_data['COMPUTE_DOMAIN']


@app.route('/telegram/webhook', methods=['POST'])
def post_webhook():
    now = int(datetime.datetime.now().timestamp())

    # event = flask.request.get_json()
    # logger.info(f'Event: {event}')

    bot = configure_telegram()

    # logger.info('JGSQVFPC')
    # if event.get('body') is None:
    #     return fk.e400('NXDQNYUR require body')

    logger.info('RMYYLVSD')
    body_data = flask.request.get_json()
    logger.info(f'body_data: {body_data}')
    if 'message' not in body_data:
        return fk.e400('FEHPCSGD require body.message')
    if 'date' not in body_data['message']:
        return fk.e400('WGQWMYUR require body.date')

    logger.info('LFLCITSK')
    ts_int = int(body_data['message']['date'])
    ts_diff = abs(ts_int-now)
    logger.info('MOSUOFFJ now={now}, ts_int={ts_int}, ts_diff={ts_diff}'.format(
        now=now,
        ts_int=ts_int,
        ts_diff=ts_diff,
    ))
    if abs(ts_int-now) > 30:
        logger.info('AUKKICOG ignore timeout')
        return fk.r200('TIMEOUT') # avoid telegram webhook loop

    update = telegram.Update.de_json(body_data, bot)
    chat_id = update.message.chat.id
    text = update.message.text

    word_list = text.split(' ')
    word_list = filter(lambda i:len(i)>0, word_list)
    word_list = list(word_list)

    ret_text = None
    if word_list[0] == '/start':
        ret_text = "Hello from telegram-hub.1602"

    if ret_text is not None:
        bot.sendMessage(chat_id=chat_id, text=ret_text)
        logger.info('Message sent')

    return fk.r200()


# TODO: remove me
@app.route('/set_webhook')
def get_setwebhook():
    host = flask.request.host
    bot = configure_telegram()
    url = f'https://{host}/telegram/webhook'
    logger.info(f'FZKSPASM URL: {url}')
    set_webhook_result = bot.set_webhook(url, timeout=30)

    if set_webhook_result:
        return fk.r200({'set_webhook_result':set_webhook_result})

    return fk.e500({'set_webhook_result':set_webhook_result})


@app.context_processor
def context_processor():
    return {
      'current_user': flask_login.current_user,
      'env': env,
    }
