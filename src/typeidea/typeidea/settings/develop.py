# coding:utf-8

'''
Created on 2017年9月6日

@author: zhan
'''

from .base import * 

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}