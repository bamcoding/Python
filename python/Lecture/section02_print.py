# format 사용 [], {}, ()
print("{} and {}".format("you","me"))
print("{0} and {1} and {0}".format("you","me"))
print("{a} and {b} and {b}".format(a="you",b="me"))

print("%s and %s" % ("you","me"))
print("price is %2d, discount percent is %2.1f" % (3,3.2222))
print("i {0:s} you {1:d}".format("love",100))

print("where are", end=' ')
print('you')
