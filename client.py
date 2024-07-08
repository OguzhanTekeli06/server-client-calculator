import requests

def main():
    print("Hesap Makinesi")
    num1 = input("Birinci sayı: ")
    num2 = input("İkinci sayı: ")
    operation = input("İşlem (add, subtract, multiply, divide): ")

    url = 'http://localhost:5000/calculate'  #sunucu urlsi
    data = {                                 # Json formatında hazırlıyorum
        'num1': num1,
        'num2': num2,
        'operation': operation
    }

    response = requests.post(url, json=data)  # sunucuya Post isteği atıyorum

    if response.status_code == 200:
        result = response.json().get('result')  # Başarılı ise sunucudan dönen sonucu alııyoruz
        print(f"Sonuç: {result}")
    else:
        print(f"Hata: {response.json().get('error')}")

if __name__ == '__main__':
    main()

