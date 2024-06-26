class BlockCrawlerResponse:
  def __init__(self, block, total_ether_value):
    self.block = block
    self.total_ether_value = total_ether_value

  def __str__(self):
        return f'Block with block number {self.block} transacted the most ether in the given block range with a total of {self.total_ether_value} ether transacted'