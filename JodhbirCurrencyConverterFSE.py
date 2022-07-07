#-------------------------------------------------------------------------------
# Name: Jodhbir
# Student No. 31500853
# Date: March 31, 2021
# Filename: JodhbirCurrencyConverterFSE.py
# Teacher: Mr. Sarros
# Purpose: To convert currencies inputed by the user
#-------------------------------------------------------------------------------

def CAD_USD():#Canada to United States
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in CAD is ", round(sendAmount*0.79,2), " in USD")#calculates and prints amount
def CAD_JPY():#Canada to Yen
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in CAD is ", round(sendAmount*87.64,2), " in JPY")
def CAD_GBP():#Canada to British pounds
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in CAD is ", round(sendAmount*0.58,2), " in GBP")
def CAD_EUR():#Canada to Euros
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in CAD is ", round(sendAmount*0.68,2), " in EUR")

def USD_CAD():#United States to Canada
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in USD is ", round(sendAmount*1.26,2), " in CAD")
def USD_JPY():#United States to Yen
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in USD is ", round(sendAmount*110.62,2), " in JPY")
def USD_GBP():#United States to British pounds
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in USD is ", round(sendAmount*0.73,2), " in GBP")
def USD_EUR():#Unites States to Euros
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in USD is ", round(sendAmount*0.85,2), " in EUR")

def JPY_CAD():#Yen to Canada
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in JPY is ", round(sendAmount*0.011,2), " in CAD")
def JPY_USD():#Yen to United States
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in JPY is ", round(sendAmount*0.0090,2), " in USD")
def JPY_GBP():#Yen to British pounds
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in JPY is ", round(sendAmount*0.0066,2), " in GBP")
def JPY_EUR():#Yen to Euros
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in JPY is ", round(sendAmount*0.0077,2), " in EUR")

def GBP_CAD():#British pounds to Canada
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in GBP is ", round(sendAmount*1.73,2), " in CAD")
def GBP_USD():#British pounds to United States
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in GBP is ", round(sendAmount*1.37,2), " in USD")
def GBP_JPY():#British pounds to yen
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in GBP is ", round(sendAmount*151.91,2), " in JPY")
def GBP_EUR():#British pounds to Euros
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in GBP is ", round(sendAmount*1.17,2), " in EUR")

def EUR_CAD():#Euros to Canada
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in EUR is ", round(sendAmount*1.48,2), " in CAD")
def EUR_USD():#Euros to United States
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in EUR is ", round(sendAmount*1.17,2), " in USD")
def EUR_JPY():#Euros to yen
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in EUR is ", round(sendAmount*129.56,2), " in JPY")
def EUR_GBP():#Euros to British pounds
    sendAmount = float(input("How much money do you want to send? "))
    print(sendAmount, " in EUR is ", round(sendAmount*0.85,2), " in GBP")

print ("Welcome to this currency converter!")
print ("I can convert your money to these currencies:")
print ("CAD (Canada), USD (United States), JPY (Japan), GBP (British pound), EUR (Euro)")#lists supported currencies
print ("When ready to stop, type in STOP when it asks for the input currency")
inputCurrency = ""#initializes inputCurrency so it can be used as a condition for the loop

while inputCurrency != "STOP":#while STOP isn't inputed, it keeps running this code that's indented

    inputCurrency = input("Which currency do you have?, please make sure to type in the three capital letters! ")#starts with this currency
    if inputCurrency == "STOP":
        break #Breaks the loop when STOP is inputed into the input currency place
    outputCurrency = input("Which currency would you like to convert to? ")#outputs to this currency
    print ("Money is going from ", inputCurrency, " to ", outputCurrency)#lists the currencies used in exchange
    

    if inputCurrency == "CAD":#if input currency is CAD, checks for output currency
        if outputCurrency == "USD":
            CAD_USD()#calls the function that was defined earlier
        elif outputCurrency == "JPY":
            CAD_JPY()
        elif outputCurrency == "GBP":
            CAD_GBP()
        elif outputCurrency == "EUR":
            CAD_EUR()

    elif inputCurrency == "USD":#if input is USD, checks for output currency
        if outputCurrency == "CAD":
            USD_CAD()
        elif outputCurrency == "JPY":
            USD_JPY()
        elif outputCurrency == "GBP":
            USD_GBP()
        elif outputCurrency == "EUR":
            USD_EUR()

    elif inputCurrency == "JPY":#if input is JPY, checks for output currency
        if outputCurrency == "CAD":
            JPY_CAD()
        elif outputCurrency == "USD":
            JPY_USD()
        elif outputCurrency == "GBP":
            JPY_GBP()
        elif outputCurrency == "EUR":
            JPY_EUR()

    elif inputCurrency == "GBP":#if input is GBP, checks for output currency
        if outputCurrency == "CAD":
            GBP_CAD()
        elif outputCurrency == "USD":
            GBP_USD()
        elif outputCurrency == "JPY":
            GBP_JPY()
        elif outputCurrency == "EUR":
            GBP_EUR()

    elif inputCurrency == "EUR":#if input is EUR, checks for output currency
        if outputCurrency == "CAD":
            EUR_CAD()
        elif outputCurrency == "USD":
            EUR_USD()
        elif outputCurrency == "JPY":
            EUR_JPY()
        elif outputCurrency == "GBP":
            EUR_GBP()

print ("Thanks for using this currency exchanger!")#when the loop breaks, this message is printed
