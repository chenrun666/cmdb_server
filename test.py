old = {1, 2, 3, 4}
new = {2, 3, 4, 5}

delete = old - new
print(delete)

update = old & new
print(update)


add = new - old
print(add)