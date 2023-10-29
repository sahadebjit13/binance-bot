from binance.um_futures import UMFutures
import API_token as keys
import fire
def execute(api_call):

    um_futures_client = UMFutures(key=keys.BINANCE_KEY, secret=keys.BINANCE_SECRET)
    amount_and_target=fire.target()


    symbol=api_call[0].upper()
    side=api_call[1].upper()
    price=round(float(api_call[2]),4)

    
    amount=amount_and_target['amount']
    quantity=round(11.0/(float(price)),8)
    stoploss=api_call[3]
    target=api_call[4]
    
    

    if side=='BUY':
        params_entry = {
            'symbol': symbol,
            'side': 'BUY',
            'type': 'LIMIT',
            'timeInForce': 'GTC',
            'quantity': quantity,
            'price': price
        }
        params_stoploss = {
            'symbol': symbol,
            'side': 'SELL',
            'type': 'STOP_MARKET',
            'closePosition': True,
            'stopPrice': round(float(stoploss),8)
        }
        params_target = {
            'symbol': symbol,
            'side': 'SELL',
            'type': 'TAKE_PROFIT',
            'quantity': quantity,
            'price': round(float(target[0]),8)
        }
        
        
        um_futures_client.new_order(**params_entry)
        um_futures_client.new_order(**params_stoploss)
        um_futures_client.new_order(**params_target)
    
    elif side=='SELL':
        params_entry = {
            'symbol': symbol,
            'side': 'SELL',
            'type': 'LIMIT',
            'timeInForce': 'GTC',
            'quantity': quantity,
            'price': price
        }
        params_stoploss = {
            'symbol': symbol,
            'side': 'BUY',
            'type': 'STOP_MARKET',
            'closePosition': True,
            'price': round(float(stoploss),8)
        }
        params_target = {
            'symbol': symbol,
            'side': 'BUY',
            'type': 'TAKE_PROFIT',
            'quantity': quantity,
            'price': round(float(target[0]),8)
        }
        
        
        um_futures_client.new_order(**params_entry)
        um_futures_client.new_order(**params_stoploss)
        um_futures_client.new_order(**params_target)

    else:
        print('Trade not executed')
    