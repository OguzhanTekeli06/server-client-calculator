import tkinter as tk
import requests

def calculate():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    operation = entry_operation.get()

    url = 'http://localhost:5000/calculate'
    data = {
        'num1': num1,
        'num2': num2,
        'operation': operation
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            result = response.json().get('result')
            label_result.config(text=f"Sonuç: {result}")
        else:
            label_result.config(text=f"Hata: {response.json().get('error')}")
    except requests.exceptions.ConnectionError:
        label_result.config(text="Bağlantı hatası: Sunucu çalışmıyor olabilir.")

# Tkinter uygulamasını oluşturma
root = tk.Tk()
root.title("Hesap Makinesi")

# Giriş alanları ve etiketler
label_num1 = tk.Label(root, text="Birinci Sayı:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="İkinci Sayı:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operation = tk.Label(root, text="İşlem (add, subtract, multiply, divide):")
label_operation.pack()
entry_operation = tk.Entry(root)
entry_operation.pack()

button_calculate = tk.Button(root, text="Hesapla", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# Uygulamayı başlatma
root.mainloop()

