from __future__ import print_function
from zipline.api import order, order_target, record, symbol

import numpy as np
import pandas as pd
from pandas_datareader import DataReader

def initialize(context):
  context.trading_day_counter = 0
  context.pair = [symbol('TLT'), symbol('IEI')]
  context.size = 200000


def handle_data(context, data):
  # Keep track of how many days the algorithm has been running
  context.trading_day_counter += 1

  # Construct Kalman filter since the start of trading 


def record_vars(context): 
  '''Record information here'''
  pass
