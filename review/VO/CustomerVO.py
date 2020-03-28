from ItemVO import ItemVO

class CustomerVO(ItemVO):
  def toString2():
    return 'CustomerVO is %s'% super.toString
  pass


cu = CustomerVO
print(cu.toString2())


if __name__ == "__main__":
    pass