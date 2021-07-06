def primary():
  print("Keep it logically awesome.")
  print("Practicing")
  print("second line")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  print(quotes)
  print(quotes[13])

if __name__== "__main__":
  primary()
