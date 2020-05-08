import PySimpleGUI as sg 
import sys

Price = 0

Cashout = 0

Fruits_list = [
    ("Royal Gala Apples 1kg pack"  , 5.90),
    ("Bananas 1kg pack", 4.90),
    ("Oranges 1 kg pack", 5.90),
    ("Watermelon 1kg slice", 2.00),
    ("Strawberries punnet", 3.00),
]

Vegetable_list = [
    ("Sweet Corn", 1.20),
    ("White Potatoes 2kg", 7.00),
    ("Mushrooms: Pre-packed", 6.90),
    ("Cucumbers: Pre-packed", 11.00),
    ("Carrots: Pre-packed", 2.00),
]

Bread_list = [
    ("White Bread Loaf", 3.40),
    ("Wholemeal Bread Loaf", 3.00),
]

Barcodelist = [
    (0, "Nestle: Milo", 7.50),
    (1, "Weet-bix", 5.00),
    (2, "Full Cream Milk: 2L", 3.20),
    (3, "Reduced Fat Milk: 2L", 4.00),
    (4, "White Sugar", 1.75),
    (5, "Table Salt", 0.90),
    (6, "Butter", 5.70),
    (7, "Sliced Tasty Cheese", 8.60),
    (8, "Tomato Sauce", 2.95),
    (9, "BBQ Sauce", 2.95),
    (10, "24 Pk 600mL Bottled water", 15.00),
    (11, "Coca-Cola: 2L", 2.15),
    (12, "Apple Juice: 2L", 2.00),
    (13, "Lollies Party Mix", 3.00),
    (14, "Block of Milk Chocolate", 5.00),
]

Fruits =[[sg.Text('Fruits', size=(6,0)),],      
    [sg.Listbox(Fruits_list, size=(50,30), key="Fruits")]]

Vegetable =[[sg.Text('vegetable', size=(6,0))],      
    [sg.Listbox(Vegetable_list, size=(50,30), key="Vegetable")]]

Bread =[[sg.Text('Bread', size=(6,0))],      
    [sg.Listbox(Bread_list, size=(50,30), key="Bread")]]

trolley=['']

items = ['']

Left_frame = [
        [sg.Button("Fruits")],
        [sg.Button("Vegetables")],
        [sg.Button("Bread")],
]

Right_frame = [
        [sg.Listbox(trolley, size=(50,30), key='items')],[sg.Button("Update", size=(5,1))],
]

layout_Main = [
    [sg.Text("Welcome to the Ibrahim Corner store")],
    [sg.Frame("Sections", Left_frame), sg.Frame("Trolley", Right_frame,)],
    [sg.Text('Scan Items', font='Helvetica 15')], [sg.Input(key="code")],
    [sg.Text("Total price: $"), sg.Text(Price, size=(15, 1), key="total")],
    [sg.Button("Pay"), sg.Button("Cancel")]
]

window = sg.Window("Ibrahim Corner store").Layout(layout_Main).Finalize()
event, values = window.read()

while True:
    event, values = window.read()
    if event in (None, "cancel"):
        break
    if event == 'Pay':
        layout_pay = [
           [sg.Text("Total price: $"), sg.Text(Price, size=(15, 1), key="total")],
           [sg.Button("Cash")], [sg.Button('Card')]
        ]
        window_Pay = sg.Window("CASH or CARD").Layout(layout_pay).Finalize()
        event_Pay, values_Pay = window_Pay.read()
        while True:
            event_Pay, values_Pay = window_Pay.read()
            if event_Pay == 'Cash':
                sg.popup(trolley)
                break
                window_Pay.close()
                window.close()
            if event_Pay == 'Card':
                sg.popup("Tap Card")
                layout_progress = [[sg.Text('A custom progress meter')],
                        [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
                        [sg.Cancel()]]
                window_progress = sg.Window('Custom Progress Meter', layout_progress)
                for i in range(1000):
                    event_progress, values_progress = window_progress.read(timeout=0)
                    if event_progress == 'Cancel' or event_progress is None:
                        break
                    window_progress['progbar'].update_bar(i + 1)
                window_progress.close()
                sg.popup('Done!')
    if event == 'Fruits':
        window.Disappear()
        layout_Fruits = [
            [sg.Text("Fruits")],
            [sg.Column(Fruits)],
            [sg.Button("Add to Cart"), sg.Button("Checkout")]]
        window_Fruits = sg.Window('Fruits').layout(layout_Fruits).Finalize()
        window_Fruits.Maximize()
        event_Fruits, values_Fruits = window_Fruits.read()
        while True:
            event_Fruits, values_Fruits = window_Fruits.read()
            if event_Fruits == "Add to Cart":
                trolley.append(values_Fruits["Fruits"])
            if event_Fruits == "Checkout":
                window_Fruits.close()
                sg.Popup("Your trolley contains:",trolley)
                break 
        window.reappear()
    if event == 'Vegetables':
        window.Disappear()
        layout_Vegetables = [
            [sg.Text("Vegetables")],
            [sg.Column(Vegetable)],
            [sg.Button("Add to Cart"), sg.Button("Checkout")]
        ]
        window_Vegetable = sg.Window('Vegetable').layout(layout_Vegetables).Finalize()
        window_Vegetable.Maximize()
        event_Vegetable, values_Vegetable = window_Vegetable.read()
        while True:
            event_Vegetable, values_Vegetable = window_Vegetable.read()
            if event_Vegetable == "Add to Cart":
                trolley.append(values_Vegetable["Vegetable"])
            if event_Vegetable == "Checkout":
                window_Vegetable.close()
                sg.Popup("Your trolley contains:",trolley)
                break 
        window.reappear()
    if event == 'Bread':
        window.Disappear()
        layout_Bread = [
            [sg.Text("Bread")],
            [sg.Column(Bread)],
            [sg.Button("Add to Cart"), sg.Button("Checkout")]]
        window_Bread = sg.Window('Bread').layout(layout_Bread).Finalize()
        window_Bread.Maximize()
        event_Bread, values_Bread = window_Bread.read()
        while True:
            event_Bread, values_Bread = window_Bread.read()
            if event_Bread == "Add to Cart":
                trolley.append(values_Bread["Bread"])
            if event_Bread == "Checkout":
                window_Bread.close()
                sg.Popup("Your trolley contains:",trolley)
                break 
        window.reappear()
    try:
        scanCodeInt = int(values["code"])
    except ValueError:
        continue
    if event == 'Update':
        if -1 < scanCodeInt < 15:
            trolley.append(Barcodelist[scanCodeInt][1])
            Price = Price + float(Barcodelist[scanCodeInt][2])
            Price = round(Price, 1)
            window["items"].Update(trolley)
            window["total"].Update(Price)
        else:
            sg.popup("Invalid ID number")