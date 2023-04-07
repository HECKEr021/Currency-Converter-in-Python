import tkinter as tk

import requests
response = requests.get('https://openexchangerates.org/api/currencies.json')


currencies = response.json()

window = tk.Tk()

window.title('CC-CURRENCY CONVERTER')


selected_currency = tk.StringVar()

currency_menu = tk.OptionMenu(window, selected_currency, *currencies.keys())

currency_menu.pack()

amount_entry = tk.Entry(window)

amount_entry.pack()

def convert_currency():

    amount = float(amount_entry.get())

    base_currency = selected_currency.get()

    target_currency = 'USD'

    api_url = 'https://openexchangerates.org/api/latest.json'

    params = {
        'APP_ID': 'b55f689438f74339aeddd182964aba51',

        'BASE': base_currency,

        'SYMBOLS': target_currency,
    }


    response = requests.get(api_url, params=params)


    if response.status_code == 200:
        data = response.json()
        if 'error' in data:
            result_label.config(text=f'Error: {data["DES"]}')
        else:
            exchange_rate = data['rates'][target_currency]

            converted_amount = amount * exchange_rate

            result_label.config(text=f'{converted_amount:.2f} {target_currency}')
    else:

        result_label.config(text='Error: API request failed')

convert_button = tk.Button(window, text='Convert', command=convert_currency)

convert_button.pack()


result_label = tk.Label(window, text='')

result_label.pack()

def reset_form():

    amount_entry.delete(0, tk.END)

    selected_currency.set('USD')

    result_label.config(text='')
reset_button = tk.Button(window, text='Reset', command=reset_form)

reset_button.pack()
window.mainloop()