from zipline.api import order, order_target, record, symbol

class Execution(object):
  def __init__(self):
    # Map from strategy id to position
    self.strat_counter = 0
    self.strats = {}
    self.allocated = 0

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
  
  def execute all

  def execute(self, strategy_id):
    for strat in strats:
      trades = strat.trade()
      for trade in trades:
        order_target(trade[0], trade[1])

  def exit(self, strategy_id):
    for 
