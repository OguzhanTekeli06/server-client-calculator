from flask import Flask, request, jsonify

app = Flask(__name__) # Flask uygulaması oluşturuyorum

@app.route('/calculate', methods=['POST'])  # Calculate endpointi için POST isteklerini dinleyen fonksiyon
def calculate():
    data = request.get_json()   # istekten Json verisi alınıyor
    operation = data.get('operation')  # Bu Jsondan gerekli bilgileri çekiyorum
    num1 = data.get('num1')
    num2 = data.get('num2')

    if not all([operation, num1, num2]):
        return jsonify({'error': 'Missing data'}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid numbers'}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})     # Sonucu JSON formatında döndürüyoruz

if __name__ == '__main__':               # # Uygulamayı ana modül olarak çalıştırdığımızda Flask sunucusunu başlatıyoruz
    app.run(host='0.0.0.0', port=5000)

