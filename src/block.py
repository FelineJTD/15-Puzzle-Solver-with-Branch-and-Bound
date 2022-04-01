class Block:
  def __init__(self, value):
    self.value = value

  def print(self):
    if (self.value < 10):
      print(f"0{self.value}", end=" ")
    elif (self.value == 16):
      print("--", end=" ")
    else:
      print(self.value, end=" ")