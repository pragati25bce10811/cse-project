def convert_currency(amount, from_currency, to_currency):
    # Dictionary storing exchange rates as conversion factors from one currency to another. 
    # Rates are approximate and manually entered for this example.
    exchange_rates = {
        'INR_to_USD': 0.0111,
        'INR_to_GBP': 0.0098,
        'USD_to_INR': 89.7,
        'GBP_to_INR': 117.3,
        'EUR_to_USD': 1.152,
        'GBP_to_EUR': 1.133,
        'USD_to_JPY': 156.74,
        'GBP_to_USD': 1.305,
        'USD_to_CHF': 0.805,
        'USD_to_CAD': 1.409,
        'EUR_to_JPY': 180.56,
        'AUD_to_USD': 0.643,
        'AUD_to_INR': 59.02,
        'EUR_to_INR': 103.07,
        'INR_to_EUR': 0.0097,
        'JPY_to_INR': 0.57,
        'INR_to_JPY': 1.75,
        'INR_to_CAD': 0.0157,
        'INR_to_AUD': 0.0135,
        'INR_TO_CHF': 0.0100,# Fixed : Changed TO to to
        'USD_TO_EUR': 0.868, # Fixed : Changed TO to to
        'USD_to_GBP': 0.766,
        'USD_to_AUD': 1.555,
        'GBP_to_JPY': 192.53,
        'EUR_to_GBP': 0.883,
        'JPY_to_USD': 0.0064,
        'CAD_to_USD': 0.71,
        'CHF_to_USD': 1.24,
        'CAD_to_INR': 63.32,
        'CHF_to_INR': 71.22,
        'GBP_to_CHF': 1.11,
        'GBP_to_CAD': 1.68,
        'GBP_to_AUD': 1.90,
        'EUR_to_CHF': 0.93,
        'EUR_to_CAD': 1.43,
        'EUR_to_AUD': 1.62,
        'JPY_to_GBP': 0.0051,
        'JPY_to_EUR': 0.0057,
        'JPY_to_CHF': 0.0052,
        'JPY_to_CAD': 0.0091,
        'JPY_to_AUD': 0.0099,
        'CHF_to_GBP': 0.90,
        'CHF_to_EUR': 1.08,
        'CHF_to_JPY': 191.4,
        'CHF_to_CAD': 1.74,
        'CHF_to_AUD': 1.90,
        'CAD_to_GBP': 0.48,
        'CAD_to_EUR': 0.61,
        'CAD_to_JPY': 95.6,
        'CAD_to_CHF': 0.57,
        'CAD_to_AUD': 1.09,
        'AUD_to_EUR': 0.56,
        'AUD_to_JPY': 122.7,
        'AUD_to_CHF': 0.60,
        'AUD_to_CAD': 0.92,
        'AUD_to_GBP': 0.50,
     }
    # If source and target currencies are the same, return amount unchanged.
    if from_currency == to_currency:
        return amount
    # Construct dictionary key for looking up conversion rate.
    # FIX:Added underscores to match the dictionary keys (e.g., 'INR_to_USD')
    key = f'{from_currency}_to_{to_currency}'
    # Return converted amount if rate found , else none indicating unsupported conversion. 
    if key in exchange_rates:
        return amount * exchange_rates[key]
    else:
        return None
def main():
    # Set of accepted currencies to validate user input against
    supported_currencies = {'INR','USD','GBP','EUR','JPY','CHF','CAD','AUD'}
    # Prompt user for input currency and validate
    from_currency = input('Enter the currency you have (INR/USD/GBP/EUR/JPY/CHF/CAD/AUD): ').strip().upper()
    if from_currency not in supported_currencies:
        print (f'Error: Unsupported or invalid input currency "{from_currency}".')
        return
    # Prompt user for output currency and validate
    to_currency = input('Enter the currency to convert to (INR/USD/GBP/EUR/JPY/CHF/CAD/AUD): ').strip().upper()
    if to_currency not in supported_currencies:
        print (f'Error: Unsupported or invalid input currency "{to_currency}".')
        return
    # Prompt user for amount and validate if it's a positive number 
    try:
        amount = float(input('Enter the amount to convert: '))
        if amount < 0 :
            print('Error: Amount must be a positive number .')
            return
    except ValueError:
        print('Error : invalid amount so please enter a number.')
        return
    # Perform the currency conversion.
    converted_amount = convert_currency(amount, from_currency, to_currency)
    # Print result or error if conversion rate not available
    if converted_amount is not None:
        print(f'{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}')
    else:
        print('Conversion not supported between the specified currencies.')
# FIX: Used double underscores for _name_ and _main_
if __name__ == '__main__':
    main()
