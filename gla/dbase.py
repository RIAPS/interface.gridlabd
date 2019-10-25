'''
Created on Feb 20, 2017

@author: riaps
'''
import logging

import pprint
from time import time

from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError

import datetime
import random
import math
import cmath
import time
from gla.config import Config


class Database(object):     

    def __init__(self,conf,logSpec):
        super(Database, self).__init__()
        self.logger = logging.getLogger(__name__)
        self.conf = conf
        self.logSpec = logSpec
        try:
            self.client = InfluxDBClient(self.conf.dbhost,self.conf.dbport,
                                         self.conf.dbuser,self.conf.dbpassword,
                                         self.conf.dbname)
            self.client.create_database(self.conf.dbname)
            # self.retention_policy = 'awesome_policy'
            # self.client.create_retention_policy(self.retention_policy, '3d', 3, default=True)
            self.client.switch_database(self.conf.dbname)
        except:
            self.logger.error("database connection failed")
            self.client = None
        self.records = []
                        
    def log(self, when, spec,value):
        timeSpec = when.isoformat() + 'Z'
        obj, attr = spec.obj, spec.attr 
        if value != None:
            fields = None
            try:
                floatValue = float(value)
                fields = { "value" : floatValue }
            except:
                try:
                    c_value = value[0:-1]+'j' if value[-1] == 'i' else value
                    complexValue = complex(c_value)
                    (mag,phi) = cmath.polar(complexValue)
                    phase = math.degrees(phi)
                    fields = { "mag" : mag, 
                              "phi" : phase 
                              }
                except:
                    sValue = str(value)
                    try: 
                        fields = { "state" : { "OPEN" : 0, "CLOSED" : 1}[sValue]}
                    except:
                        fields = { "state" : sValue }
            if fields != None:
                record = {  "time": timeSpec,
                            "measurement": attr,
                            "tags" : { "object" : obj },
                            "fields" : fields
                            }
                self.records.append(record)
    
    def flush(self):
        self.logger.info("writing: %s" % str(self.records))
        if self.client:
            _res = self.client.write_points(self.records)     # , retention_policy=self.retention_policy)
        self.records = []
        
    def stop(self):
        if self.client and self.conf.dbrop:
            self.client.drop_database(self.conf.dbname)
            
    def __destroy__(self):
        if self.client and self.conf.dbrop:
            self.client.drop_database(self.conf.dbname)
            
            
        
