import random

def main():
  #print("Keep it logically awesome!")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 16
  rnd = random.randint(0, last)
  rnd1 = random.randint(0, last-rnd)
  print(quotes[rnd], end=quotes[rnd1])

if __name__== "__main__":
  main()
