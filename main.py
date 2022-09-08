import random
import time

#Vars

day = int(0)
jobday = int(0)
raiseday = int(-1)
money = 30.00
havejob = False
pending = False
job = "un"
pay = 1
vinv = [100, 100, 100, 100, 100]
yinv = [0, 0, 0, 0, 0]
price = [3.00, 2.50, 3.00, 1.50, 2.00]
left = False

#Funcs

def vinvf():
  global day
  print("The vending machine currently contains " + str(vinv[0]) + " bags of chips, " + str(vinv[1]) + " candy bars, " + str(vinv[2]) + " soda cans, " + str(vinv[3]) + " water bottles, and " + str(vinv[4]) + " juice boxes.")
  day -= 1
  
def buy():
  global money
  if money == 0.0:
    print("You can't buy anything. You're fresh out of money! Try getting some more.")
    return
  vinvf()
  
  try:
    choice = int(input("Which of these items would you like to buy? Enter a number from 1 to 5: "))
  except ValueError:
    print("\nPlease only enter a number from 1 to 5.")
    return
    
  if choice == 1:
    print("You have selected: bags of chips.")
  elif choice == 2:
    print("You have selected: candy bars.")
  elif choice == 3:
    print("You have selected: soda cans.")
  elif choice == 4:
    print("You have selected: water bottles.")
  elif choice == 5:
    print("You have selected: juice boxes.")
  else:
    print("\nThat\'s not a valid option. Please try again and select one of the listed options.")
    return
  allbuy(choice - 1)
  
def allbuy(vchoice):
  global money
  global day
  if vinv[vchoice] > 0:
    print("There are " + str(vinv[vchoice]) + " of them remaining in the vending machine. Each one costs " + str(price[vchoice]) + " dollars.")
    bquan = int(input("How many would you like to purchase? "))
    if bquan == 0:
      print("\nYou can't buy nothing. That would be silly.")
      return
    if bquan < 0:
      print("\nYou can't buy a negative amount of something. That would be literally impossible.")
      return
    bans = input("Are you sure you would like to purchase " + str(bquan) + "? Y/N: ")
    if bans == "Y" or "y":
      if money >= price[vchoice]:
        truebquan = 0
        vout = False
        while bquan > 0:
          money -= price[vchoice]
          vinv[vchoice] -= 1
          yinv[vchoice] += 1
          bquan -= 1
          truebquan += 1
          if money < price[vchoice]:
            cnb = True
            break
          else:
            cnb = False
          if vinv[vchoice] == 0:
            vout = True
            break
          else:
            vout = False
        mround()
        print("\nPurchase successful!\nYou have " + str(money) + " dollars remaining.")
        day += 1
        if cnb == True:
          print("You were only able to purchase " + str(truebquan) + " before running out of money.")
        if vout == True:
          print("You bought out the entire stock of that item!")
      else:
        print("\nYou don't have enough money. Try getting some more.")
    elif bans == "N" or "n":
      print("\nPurchase declined.")
  else:
    print("\nThere are no more of those left in the vending machine.")
    
def bal():
  global day
  print("You currently have " + str(money) + " dollars.")
  if job == "un":
    print("You are currently unemployed.")
  else:
    print("You have a job as a " + job + ", making " + str(pay) + " dollars per hour.")
  day -= 1
    
def yinvf():
  global day
  print("You currently have " + str(yinv[0]) + " bags of chips, " + str(yinv[1]) + " candy bars, " + str(yinv[2]) + " soda cans, " + str(yinv[3]) + " water bottles, and " + str(yinv[4]) + " juice boxes.")
  day -= 1
  
def more():
  global money
  global job
  global havejob
  global day
  global jobday
  global raiseday
  global pending
  global pay
  print("You can get more money in multiple ways. You may also manage your employment status here.")
  print("Your options are:\n")
  print("1. Work at your job")
  print("2. Quit your job")
  print("3. Sell items from your inventory")
  print("4. Ask a friend for money")
  
  try:
    mans = int(input("\nWhich would you like to do? "))
  except ValueError:
    print("\nPlease only enter a number from 1 to 4.")
    day -= 1
    return

  print("You have selected option: " + str(mans) + ".\n")

  if mans == 1:
    if havejob != False:
      jobhours = 0
      print("You are currently working as a " + job + ".\nPress Enter to work for 1 hour.")
      while jobhours < 8:
        input()
        jobhours += 1
        money += pay
        if jobhours == 1:
          print("You have worked for " + str(jobhours) + " hour.")
        else:
          print("You have worked for " + str(jobhours) + " hours.")
      print("The work day is now over.")
      print("\nYou gained " + str((pay * 8)) +" dollars.")
      raiseday += 1
      if raiseday == 0:
        raiseday += 1
    else:
      if pending != True:
        print("You do not yet have a job. Luckily, your favorite local restaurant is now hiring.")
        print("\nThe available positions are:")
        print("1. Waiter")
        print("2. Chef")
        print("3. Delivery Driver")
        try:
          jobinput = int(input("\nWhich position would you like to apply for? All jobs have a starting pay of 1 dollar per hour. "))
        except ValueError:
          print("\nPlease only enter a number from 1 to 3.")
          day -= 1
          return
        if jobinput == 1:
          job = "waiter"
        elif jobinput == 2:
          job = "chef"
        elif jobinput == 3:
          job = "delivery driver"
        else:
          print("\nThat\'s not a valid option. Please try again and select one of the listed options.")
          day -= 1
          return
        print("\nYou have submitted an application to be a " + job + ".\nWait until Day " + str(day + 3) + " to see if it gets accepted.")
        pending = True
        jobday = day + 3
      else:
        print("Your application is still being processed. Please wait until Day " + str(jobday) + " to see if it gets accepted.")
        day -= 1

  elif mans == 2:
    if havejob == False:
      print("You can\'t quit your job if you don\'t have one.")
      day -= 1
      return
    else:
      qj = input("Are you sure you want to quit your job? Your raises will be reset. Y/N:")
      if qj == "Y" or "y":
        havejob = False
        print("You no longer have a job.")
        pay = 1
      else:
        day -= 1
        return
    
  elif mans == 3:
    print("You can sell any item in your inventory for 80% of its original price.\n")
    yinvf()
    sellans = int(input("\nWhich item would you like to sell? Enter a number from 1 to 5: "))
    if sellans == 1:
      print("You have selected: bags of chips.")
    elif sellans == 2:
      print("You have selected: candy bars.")
    elif sellans == 3:
      print("You have selected: soda cans.")
    elif sellans == 4:
      print("You have selected: water bottles.")
    elif sellans == 5:
      print("You have selected: juice boxes.")
    else:
      print("\nThat\'s not a valid option. Please try again and select one of the listed options.")
      return
    sellans -= 1
    print("The original price for that item is " + str(price[sellans]) + ". It can be sold for " + str(round(((price[sellans]) * 0.8), 2)) + " dollars.")
    sellquan = int(input("How many would you like to sell? "))
    if sellquan == 0:
      print("\nYou can't sell nothing. That would be silly.")
      return
    else:
      truesellquan = 0
      while sellquan > 0:
        yinv[sellans] -= 1
        money += (price[sellans] * 0.8)
        sellquan -= 1
        truesellquan += 1
        if yinv[sellans] < 1:
          break
      print("\nSale successful!")
      day += 1

  elif mans == 4:
    print("Your friend has a 40% chance of agreeing to give you some money.")
    input("Press Enter to ask him.")
    print("...")
    time.sleep(1)
    mchance = random.random()
    if mchance <= 0.40:
      print("He agrees!")
      famount = round(((random.random() * 9) + 1), 2)
      money += famount
      print("He gave you " + str(famount) + " dollars. How generous!")
    else:
      print("He declines!")
      print("Looks like you're not getting any money from him today! Try asking again tomorrow.")
  else:
    print("That\'s not a valid option. Please try again and select one of the listed options.")
    day -= 1
    
def leave():
  global left
  bleft = input("Are you sure you would like to leave the vending machine? Y/N: ")
  if bleft == "Y" or "y":
    left = True
  else:
    left = False
def mround():
  global money
  mrounded = round(money, 2)
  money = mrounded
#Beginning of program
print("- Welcome to The Vending Machine. -\n")
print("Standing before you is a large vending machine full of tasty snacks and drinks.\n")
print("Your goal is to purchase everything in the vending machine through any means necessary.")

while left != True:
  mround()

  if vinv[0] == 0 and vinv[1] == 0 and vinv[2] == 0 and vinv[3] == 0 and vinv[4] == 0:
    print("\nYou did it! Over a total of " + str(day) + " days, you bought everything in the vending machine!")
    break

  day += 1
  print("\nDay " + str(day))

  if day == jobday:
    jobchance = random.random()
    if jobchance <= 0.8:
      print("Your job application was accepted! You may begin work as a " + job + " today.")
      havejob = True
      pending = False
    else:
      print("Your job application was denied! Try applying for a position other than a " + job + ".")
    jobday = 0
  if raiseday % 7 == 0:
    pay = round(pay * 1.25, 2)
    print("Good news! Your boss has given you a 25% raise! You will now be paid " + str(pay) + " dollars an hour.")
    raiseday = -1
    
  print("\nYour options are:")
  print("1. Check vending machine\'s inventory")
  print("2. Make a purchase")
  print("3. Check your balance and employment status")
  print("4. Check your inventory")
  print("5. Get more money")
  print("6. Leave")
  try:
    ans = int(input("\nWhat would you like to do? "))
  except ValueError:
    print("\nPlease only enter a number from 1 to 6.")
    day -= 1
    continue

  print("You have selected option: " + str(ans) + ".\n")

  if ans == 1:
    vinvf()
  elif ans == 2:
    buy()
  elif ans == 3:
    bal()
  elif ans == 4:
    yinvf()
  elif ans == 5:
    more()
  elif ans == 6:
    leave()
  else:
    print("That\'s not a valid option. Please select one of the listed options.")
    day -= 1
if left == True:
  print("\nYou walked away from the vending machine. Not to worry, as you can always return.")
else:
  print("\nYou are one dedicated player.")
print("Thanks for playing!")
