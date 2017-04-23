from __future__ import print_function
from zipline.api import order, order_target, record, symbol

import numpy as np
import pandas as pd
from pandas_datareader import DataReader

class Strategy(object):
  def __init__(self, capital):
    self.capital = capital
    self.used = 0
    self.margin = 0
    self.leverage = 0

  def trade(self, context, data):
    '''Execute some trades according to this strategy'''
    pass

  def exit(self):
    '''Exit this strategy'''
    pass

  def adjust_capital(self, capital):
    '''Adjust how much capital is allocated to this strategy'''
    self.capital = capital

  def get_margin(self):
    '''Return the acceptable trading margin'''
    return self.margin * self.capital

  def can_trade(self, cost):
    margin = self.get_margin()
    return (self.capital - margin - self.used) < cost

  def s_order(self, ticker, qty, data):
    # First check that we have enough capital to do so
    cost = data.current(ticker)['price'] * qty
    if self.can_trade(cost):
      order(ticker, qty)
      return True
    return False

  def s_order_target(self, ticker, qty, data):
    # First check that we have enough capital to do so
    cost = data.current(ticker)['price'] * qty
    if self.can_trade(cost):
      order_target(ticker, qty)
      return True
    return False

  def s_order_target_percent(self, ticker, percent):
    # First check that we have enough capital to do so
    cost = self.capital * percent
    if self.can_trade(cost):
      order_target_percent(ticker, percent)
      return True
    return False


class LongShortStrategy(Strategy):
  def __init__(self, capital):
    Strategy.__init__(self, capital)
    self.long_positions = {}
    self.short_positions = {}

  def trade(self, context, data):
    # Just order target of each of the positions
    for ticker in self.long_positions:
      qty = self.long_positions[ticker]
      self.s_order_target(ticker, qty, data)
    for ticker in self.short_positions:
      qty = self.short_positions[ticker]
      self.s_order_target(ticker, -qty, data)

  def exit(self):
    # Attempt to liquidate every position
    for ticker in self.long_positions:
      order_target(ticker, 0)
    for ticker in self.short_positions:
      order_target(ticker, 0)


