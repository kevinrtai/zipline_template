from zipline.api import order, order_target, record, symbol

class Execution(object):
  def __init__(self):
    # Map from strategy id to position
    self.strat_counter = 0
    self.strats = {}
    self.allocated = 0

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

  def add_strategy(self, strat, allocation):
    if allocation + self.allocated > 1:
      raise Exception('Allocation exceeds 1')
 
    self.allocated += allocation 
    self.strats[self.strat_counter] = {
                                        'allocation': allocation, 
                                        'positions': {},
                                        'strategy': strat
                                      }
    self.strat_counter += 1

  def modify_allocation(self, strat, allocation):
    self.allocated = 
  
  def execute_all(self):

  def execute(self, strategy_id):
    for strat in strats:
      trades = strat.trade()
      for trade in trades:
        order_target(trade[0], trade[1])

  def exit(self, strategy_id):
    for 
