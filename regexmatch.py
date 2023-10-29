import re

def coin(coin_name):
    x = re.split("/", coin_name)
    a=x[0][1:]+x[1]
    return a

def signal(coin_signal):
    if(coin_signal in ['buy','long']):
        return 'buy'
    elif(coin_signal in ['sell','short']):
        return 'sell'
    else:
        return 'Error: Signal is not clear'
    
def entry(coin_entry):
    x = re.search("[0-9]*\.[0-9]*", coin_entry)
    return x.group(0)

def stoploss(coin_stoploss):
    x = re.search("[0-9]*\.[0-9]*", coin_stoploss)
    return x.group(0)

def target(coin_target):
    coin_target=' '.join(coin_target)
    x = re.findall("[0-9]*\.[0-9]*", coin_target)
    return x

def leverage(coin_leverage):
    x = re.search("[0-9]+x$", coin_leverage)
    y = x.group(0)
    return y[0:-1]

def handle_call(call):
    divider=list(call.split('\n'))
    while '' in divider:
        divider.remove('')
    while ' ' in divider:
        divider.remove(' ')
    coin_name=coin(divider[0])
    signal_given=signal(divider[1])
    entry_given=entry(divider[2])
    stoploss_given=stoploss(divider[3])
    target_given=target(divider[4])
    leverage_given=leverage(divider[5])
    
    api_call=list([coin_name,signal_given,entry_given,stoploss_given,target_given,leverage_given])
    return api_call
