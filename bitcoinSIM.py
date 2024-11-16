#Coded by Janelle Sampson


from datetime import datetime


################################ Functions #################################
def balance(Trader):
    live = GetLive()
    formatTM = "{:.2f}".format(Trader.money)
    formatLP = "{:.2f}".format(live.scrape())
    print("Balance: ")
    print("USD Balance: $" + str(formatTM))
    print("Your " + trader1.wallet.ticker+ ": " + str(Trader.bitcoins))
    print("Current " + trader1.wallet.ticker + " Market Price: $", formatLP)

################################ Classes #################################

class Wallet:
    def __init__(self):
        self.ticker = "BTC"
        self.coinCount = 0.00
        self.money = 275000.00

    def printWalletStats(self):
        print(self.ticker, ": ", self.coinCount)

    def walletSet(self, newcoin):
        self.coinCount = newcoin


class Trader:
    def __init__(self):
        self.wallet = Wallet()
        self.money = self.wallet.money
        self.bitcoins = self.wallet.coinCount


    def traderSell(self, soldAmount):
        self.money += soldAmount

    def traderBuy(self, boughtAmount):
        self.money -= boughtAmount


class Ledger:

    def __init__(self):
        self.buy = 0
        self.sell = 0
        self.money = trader1.money
        self.ledger = []

        print("A ledger has been created...")
        print()

    #Add a buy to the ledger
    def addBuyToLedger(self, newCoins, buyPrice):
        if trader1.money < newCoins * buyPrice:
            print("You don't have enough money to buy that much Bitcoin.")
            print()
        else:
            trader1.money -= newCoins * buyPrice
            trader1.bitcoins += newCoins
            self.ledger.append("Bought " + str(newCoins) + " " + trader1.wallet.ticker + " on " + str(Date.datePrint(self)))
            print("Your purchase was successful.")
            print()

    #Add a sell to the ledger
    def addSellToLedger(self, soldCoins, sellPrice):
        if trader1.bitcoins < soldCoins:
            print("You don't have enough " + trader1.wallet.ticker + " to sell.")
            print()
        else:
            trader1.money += soldCoins * sellPrice
            trader1.bitcoins -= soldCoins
            self.ledger.append("Sold " + str(soldCoins) + " " +  trader1.wallet.ticker + " on " + str(Date.datePrint(self)))
            print("Your sale was successful.")
            print()


    #Print
    def printHistory(self):
        for item in self.ledger:
            print(item)

class Date:
    currentDateTime = datetime.now()
    longDate = currentDateTime.strftime("%A, %B %d, %Y")
    @staticmethod
    def datePrint(self):
        formatted_timestamp = datetime.now().strftime("%A, %B %d, %Y  %H:%M:%S.%f")
        return formatted_timestamp

class GetLive:

    def scrape(self):
        try:
            import requests
        except ImportError:
            import subprocess

            subprocess.check_call(["python", "-m", "pip", "install", "requests"])

        # Scrape from Coinbase (API)
        url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

        response = requests.get(url)
        data = response.json()

        # Print
        bitcoinPrice = data['data']['amount']
        floatBP = float(bitcoinPrice)
        return floatBP

################################# Variables #################################

trader1 = Trader()
ledger = Ledger()
livePrice = GetLive()
currentDate = Date()

################################# Main #################################

#Menu
loop = True
while loop:
    print("Menu:")
    menu = ["Price", "Buy", "Sell", "Balance", "History", "Exit"]
    for thing in menu:
        print(thing)

    print()
    print()
    selection = input("Enter your choice: ").lower()
    if selection != "price" and selection != "buy" and selection != "sell" and selection != "balance" and selection != "history" and selection != "exit":
        print("Invalid. ")
    print()

    if selection == "exit":
        print("Goodbye")
        loop = False

    if selection == "balance":
        balance(trader1)
        print()

    if selection == "buy":
        bitcoinToBuy = float(input("Enter the amount of BTC to buy: "))
        ledger.addBuyToLedger(bitcoinToBuy, livePrice.scrape())


    if selection == "sell":
        bitcoinToBuy = float(input("Enter the amount of BTC to sell: "))
        ledger.addSellToLedger(bitcoinToBuy, livePrice.scrape())


    if selection == "history":
        ledger.printHistory()
        print()

    if selection == "price":
        price = livePrice.scrape()
        print("Current Market Price for " + trader1.wallet.ticker + " is: $", "{:.2f}".format(price))
        print()

############# Please be advised that the Bitcoin price is scraped from Coinbase and is live ######################