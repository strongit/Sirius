#encoding=utf8
"""
Django settings for Aries project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
#LDAP
AUTHENTICATION_BACKENDS = (
'django_auth_ldap.backend.LDAPBackend',
'django.contrib.auth.backends.ModelBackend',
)

CORS_ORIGIN_WHITELIST = (
    'google.com',
    '192.168.164.120:4001'
)
#LOG_BASE_DIR="/opt/pan.lu/gitsource/Sirius-dev/Sirius/log"
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,sys
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_BASE_DIR=os.path.join(BASE_DIR.rstrip("Aries"), "log")
FTP_LOCAL_DIR=os.path.join(BASE_DIR.rstrip("Aries"), "download/")

FILE_PATH=os.path.join(BASE_DIR.rstrip("Aries"), "sbin")
file_name='{0}/Aries.yaml'.format(FILE_PATH).replace('\\','/')
yaml_file = open(file_name)
SETTINGS = yaml.load(yaml_file)
print SETTINGS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4q+z5arz(+!__dtzxpn*n7g@3w0s7x)xtr+v!ts9m!-vzp=^)4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
APPEND_SLASH=False
# Application definition
INSTALLED_APPS = (
#    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user_auth',
    'hdfs',
    'kd_agent',
	'openstack',
    'codis',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Aries.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Aries.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'complete': {
            'format': '[%(levelname)s %(asctime)s @ %(process)d] (%(pathname)s/%(funcName)s:%(lineno)d) - %(message)s'
        },
        'online': {
            'format': '[%(levelname)s %(asctime)s @ %(process)d] - %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter': 'online',
            'filename' : '{0}/error.log'.format(LOG_BASE_DIR).replace('\\','/')
        },
        'ac_file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter': 'complete',
            'filename' :'{0}/service.log'.format(LOG_BASE_DIR).replace('\\','/')
        },
        'cmd_file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter': 'complete',
            'filename' :'{0}/cmd.log'.format(LOG_BASE_DIR).replace('\\','/')
        },
        'hdfs_file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter': 'complete',
            'filename' :'{0}/hdfs.log'.format(LOG_BASE_DIR).replace('\\','/')
        },
        'kd_agent_file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter': 'complete',
            'filename' :'{0}/service.log'.format(LOG_BASE_DIR).replace('\\','/')
        },
        'openstack_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'complete',
            'filename': '{0}/openstack.log'.format(LOG_BASE_DIR).replace('\\', '/')
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'complete'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        '': {
            'handlers':['file'],
            'propagate': False,
            'level':'DEBUG',
        },
        'cmd_log': {
            'handlers':['cmd_file', 'console'],
            'propagate': False,
            'level':'DEBUG',
        },
        'access_log': {
            'handlers':['ac_file', 'console'],
            'propagate': False,
            'level':'DEBUG',
        },
        'hdfs_log': {
            'handlers':['hdfs_file', 'console'],
            'propagate': False,
            'level':'DEBUG',
        },
        'kd_agent_log': {
            'handlers':['kd_agent_file','console'],
            'propagate': False,
            'level':'DEBUG',
        },
        'openstack_log': {
            'handlers': ['openstack_log'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['ac_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# 提供k8s服务的地址
K8S_SETTINGS = SETTINGS["K8S"]
K8S_IP = K8S_SETTINGS["K8S_IP"]
K8S_PORT = K8S_SETTINGS["K8S_PORT"]
INFLUXDB_IP = K8S_SETTINGS["INFLUXDB_IP"]
INFLUXDB_PORT = K8S_SETTINGS["INFLUXDB_PORT"]
INFLUXDB_DATABASE = K8S_SETTINGS["INFLUXDB_DATABASE"]


BDMS_SETTINGS = SETTINGS["BDMS"]
BDMS_IP = BDMS_SETTINGS["IP"]
BDMS_PORT =  BDMS_SETTINGS["PORT"]
BDMS_USERNAME =  BDMS_SETTINGS["USERNAME"]
BDMS_PASSWORD =  BDMS_SETTINGS["PASSWORD"]

DATABASES = SETTINGS["DATABASES"]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

AUTH_LDAP_SETTINGS = SETTINGS["AUTH_LDAP"]
AUTH_LDAP_SERVER_URI = AUTH_LDAP_SETTINGS["SERVER_URI"]
AUTH_LDAP_USER_DN_TEMPLATE = AUTH_LDAP_SETTINGS["USER_DN_TEMPLATE"]
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = AUTH_LDAP_SETTINGS["BIND_AS_AUTHENTICATING_USER"]
AUTH_LDAP_CACHE_GROUPS = AUTH_LDAP_SETTINGS["CACHE_GROUPS"]
AUTH_LDAP_GROUP_CACHE_TIMEOUT = AUTH_LDAP_SETTINGS["GROUP_CACHE_TIMEOUT"]
AUTH_LDAP_USER_ATTR_MAP = AUTH_LDAP_SETTINGS["USER_ATTR_MAP"]

REST_BASE_URI = SETTINGS["REST_BASE_URI"]
SHARE_PROXY_BASE_URI = SETTINGS["SHARE_PROXY_BASE_URI"]

AMBARI_SETTINGS = SETTINGS["AMBARI"]
AMBARI_URL = AMBARI_SETTINGS["AMBARI_URL"]
HDFS_URL = AMBARI_SETTINGS["HDFS_URL"]
HADOOP_CLIENT = AMBARI_SETTINGS["HADOOP_CLIENT"]
AMBARI_USER = AMBARI_SETTINGS["AMBARI_USER"]
AMBARI_PASSWORD = AMBARI_SETTINGS["AMBARI_PASSWORD"]

########################
#   webhdfs settigns   #
########################


# the webhdfs node maybe more than one node, so webhdfs hosts is a list
# the item of webhdfs hosts list is "ip:port", default port is 50070
WEBHDFS_SETTINGS = SETTINGS["WEBHDFS"]
WEBHDFS_HOSTS = WEBHDFS_SETTINGS["HOSTS"]
# webhdfs port, it`s default value is 50070
WEBHDFS_PORT = WEBHDFS_SETTINGS["PORT"]
WEBHDFS_PATH = WEBHDFS_SETTINGS["PATH"]
WEBHDFS_USER = WEBHDFS_SETTINGS["USER"]
WEBHDFS_TIMEOUT = WEBHDFS_SETTINGS["TIMEOUT"]
WEBHDFS_MAX_TRIES = WEBHDFS_SETTINGS["MAX_TRIES"]
WEBHDFS_RETRY_DELAY = WEBHDFS_SETTINGS["RETRY_DELAY"]
# HADOOP_RUN_SCRIPT = os.path.join(BASE_DIR, os.path.pardir, 'sbin/hadoop-run.sh')
HADOOP_RUN_SCRIPT = "hadoop-run.sh"
SESSION_COOKIE_AGE=60*30
#kubectl_file
KUBECTL_OSX = os.path.join(BASE_DIR, '../package', 'kubectl_osx_1_2_4')
KUBECTL_LINUX = os.path.join(BASE_DIR, '../package', 'kubectl_linux_1_2_4')

#codis设置
CODIS_LOCAL_DIR = os.path.join(BASE_DIR, "codis/redisconf/")
CODIS_COMMOND_DIR = os.path.join(BASE_DIR, "codis/commandlog/")
CODIS_DATADIR = os.path.join(BASE_DIR, "codis/serverconf/data/")
CODIS_LOGFILE_DIR = os.path.join(BASE_DIR, "codis/serverconf/log/")
CODIS_PIDFILE_DIR = os.path.join(BASE_DIR, "codis/serverconf/pid/")
CODIS_SHOME = os.path.join(BASE_DIR, "codis/")

CODIS_SETTINGS = SETTINGS["CODIS"]
CODIS_INDEX_LINE = CODIS_SETTINGS["INDEX_LINE"]
CODIS_ZK_ADDR = CODIS_SETTINGS["ZK_ADDR"]
#CODIS_HOST_INFO = [0,'172.24.3.64','root','',0,'a',0]
CODIS_HOST_INFO = CODIS_SETTINGS["HOST_INFO"]
CODIS_MEMORY_MAX = CODIS_SETTINGS["MEMORY_MAX"]
OPENTSDB_URL = CODIS_SETTINGS["PENTSDB_URL"]
SSH_PKEY = CODIS_SETTINGS["SSH_PKEY"] 
SSH_KNOWN_HOSTS =  CODIS_SETTINGS['SSH_KNOWN_HOSTS']

#openstack设置：
OPENSTACK_SETTINGS = SETTINGS["OPENSTACK"]
IP_KEYSTONE = OPENSTACK_SETTINGS["IP_KEYSTONE"]
PORT_KEYSTONE = OPENSTACK_SETTINGS["PORT_KEYSTONE"]
IP_NOVA = OPENSTACK_SETTINGS["IP_NOVA"]
PORT_NOVA = OPENSTACK_SETTINGS["PORT_NOVA"]
IP_CINDER = OPENSTACK_SETTINGS["IP_CINDER"]
PORT_CINDER = OPENSTACK_SETTINGS["PORT_CINDER"]

#启动一个线程开始定时统计配额. default: 10m
POLL_TIME = 600
import sumSpace
sumSpace.run(POLL_TIME)
