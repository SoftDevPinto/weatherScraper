from tkinter import Tk, Label, Entry, Button
from requests_html import HTMLSession


# Define the styles
BACKGROUND_COLOR = 'white'
FONT_STYLE = ('Arial', 12, 'bold')
LABEL_STYLE = {'font': FONT_STYLE, 'bg': BACKGROUND_COLOR, 'fg': '#333333', 'padx': 5, 'pady': 5}
ENTRY_STYLE = {'font': FONT_STYLE, 'bg': 'white', 'fg': '#333333', 'highlightthickness': 1, 'highlightcolor': '#cccccc','highlightbackground': '#cccccc', 'bd': 0, 'relief': 'solid'}
BUTTON_STYLE = {
    'font': FONT_STYLE,
    'bg': '#1a73e8',
    'fg': 'white',
    'activebackground': '#0d47a1',
    'activeforeground': 'white',
    'bd': 0,
    'relief': 'flat',
    'padx': 10,
    'pady': 5,
    'cursor': 'hand2',
    'bg': '#4285f4',
    'activebackground': '#1a73e8',
}

RESULT_STYLE = {'font': FONT_STYLE, 'bg': BACKGROUND_COLOR, 'fg': '#333333', 'padx': 5, 'pady': 5}

# Define the function to get the weather
def get_weather():
    query = location_entry.get()

    url = f'https://www.google.com/search?q=weather+{query}'
    s = HTMLSession()

    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})

    temp = r.html.find('span#wob_tm', first=True).text

    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text

    desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text


    result_label.config(text=f'{query}: {temp}{unit}, {desc}')

# Create the main window
root = Tk()
root.title('Weather App')
root.config(bg=BACKGROUND_COLOR)

# Create the input field and button
location_label = Label(root, text='Enter location:', **LABEL_STYLE)
location_label.pack()
location_entry = Entry(root, **ENTRY_STYLE)
location_entry.pack()
location_entry.focus()
get_weather_button = Button(root, text='Get Weather', command=get_weather, **BUTTON_STYLE)
get_weather_button.pack(pady=10)

# Create the label to display the result
result_label = Label(root, text='', **RESULT_STYLE)
result_label.pack()

# Start the main loop
root.mainloop()
