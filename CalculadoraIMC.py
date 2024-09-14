import dearpygui.dearpygui as dpg


def calcular_imc():
    try:
        
        peso = float(dpg.get_value("input_peso"))
        altura = float(dpg.get_value("input_altura"))
        
       
        imc = peso / (altura * altura)
        
        
        if imc < 16.9:
            resultado = "Muita abaixo do peso"
        elif imc >= 16.9 and imc <= 18.4:
            resultado = "Abaixo do peso"
        elif imc >= 18.5 and imc <= 24.9:
            resultado = "Peso normal"
        elif imc >= 25 and imc <= 29.9:
            resultado = "Acima do peso"
        elif imc >= 30 and imc <= 35:
            resultado = "Obesidade grau 1"
        elif imc >= 35 and imc <= 40:
            resultado = "Obesidade grau 2"
        else:
            resultado = "Obesidade grau 3"
        
        
        dpg.set_value("resultado_texto", f"Seu IMC é {imc:.2f}: {resultado}")
    except ValueError:
        dpg.set_value("resultado_texto", "Por favor, insira valores válidos.")


dpg.create_context()


with dpg.window(label="Calculadora de IMC", width=400, height=300):
    dpg.add_text("Digite seu peso em quilogramas:")
    dpg.add_input_text(tag="input_peso", width=200)
    
    dpg.add_text("Digite sua altura em centímetros:")
    dpg.add_input_text(tag="input_altura", width=200)
    
    dpg.add_button(label="Calcular IMC", callback=calcular_imc)
    
    dpg.add_text("", tag="resultado_texto")

dpg.create_viewport(title='Calculadora de IMC', width=400, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
