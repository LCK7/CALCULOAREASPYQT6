# 📐 Calculadora de Áreas - PyQt6

¡Bienvenido a la **Calculadora de Áreas**!  
Una aplicación de escritorio desarrollada con **Python** y **PyQt6** que permite calcular fácilmente el área de figuras geométricas básicas: **círculo**, **cuadrado**, **rectángulo** y **triángulo**.

---

## 🧠 ¿Qué hace este programa?

Esta calculadora gráfica permite al usuario:

- Ingresar los valores necesarios para cada figura.
- Validar que los datos ingresados sean correctos (solo positivos).
- Calcular automáticamente el área.
- Mostrar el resultado en pantalla de forma clara.
- Limpiar los campos para realizar nuevos cálculos.

Todo esto con una interfaz moderna, amigable y profesional ✨.

---

## 🖼️ Interfaz de usuario

La interfaz está organizada en pestañas, una por cada figura:

- 🔵 **Círculo** – Ingresa el radio.
- 🟦 **Cuadrado** – Ingresa la longitud de un lado.
- 🟨 **Rectángulo** – Ingresa el largo y el ancho.
- 🔺 **Triángulo** – Ingresa la base y la altura.

Cada pestaña contiene:
- Campos de entrada validados.
- Botón para **calcular**.
- Botón para **limpiar**.
- Etiqueta que muestra el resultado o un mensaje de error.

---

## 🚀 Cómo ejecutar el proyecto

### 🔧 Requisitos

- Python 3.8 o superior
- PyQt6

### 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
````

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```


> Si no tienes `requirements.txt`, simplemente instala PyQt6:
>
> ```bash
> pip install PyQt6
> ```

3. Ejecuta la aplicación:

```bash
python app.py
```

---

## 📁 Estructura del proyecto

```
calculadora_areas/
├── app.py
├── README.md
├── integrantes.txt
├── src/
│   ├── logica/
│   │   └── validators.py
│   └── vista/
│       ├── main_window.py
│       ├── Tab_ui.py
│       ├── results.py
│       └── widgets/
│           ├── circulo_widget.py
│           ├── cuadrado_widget.py
│           ├── rectangulo_widget.py
│           └── triangulo_widget.py
```

---

## 🧪 Buenas prácticas implementadas

* ✅ Validación de entradas numéricas con `PositiveDoubleValidator`
* ✅ Separación de lógica y vista
* ✅ Uso de docstrings estilo Google para documentar clases y métodos
* ✅ Código modular y escalable
* ✅ Interfaz consistente y profesional
* ✅ Compatible con `python app.py` directamente

---

## 👥 Autores

Este proyecto fue realizado por el estudiante de Ingeniería de Sistemas e Informática para el curso de Construccion de Software.

- Gutierrez Taipe, Luis Alberto

---

## 💡 Licencia

Este proyecto es de uso académico. Puedes adaptarlo o ampliarlo según tus necesidades educativas. 🚀

> Si te gustó este proyecto, ⭐ ¡no olvides darle una estrella en GitHub!

