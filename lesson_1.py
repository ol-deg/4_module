def palindrom(slovo):
  slovo1 = slovo[::-1]
  if slovo == slovo1:
    return True
  else:
    return False
print(palindrom('cvbvc'))