from flask import Flask, render_template

app = Flask(__name__)

def calcular_factorial(n):
    if not isinstance(n, int) or n < 0:
        return "El número debe ser entero positivo"
    if n == 0:
        return 1;
    else: 
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
@app.route('/factorial/<int:numero>')
def mostrar_factorial(numero):
    factorial = calcular_factorial(numero)
    return render_template('factorial.html', numero=numero, factorial=factorial)

@app.route('/')
def inicio():
    return "Ingresa un número en la URL después de /factorial/ para ver su factorial. Ejemplo: /factorial/5"

if __name__ == '__main__':
    app.run(debug=True)