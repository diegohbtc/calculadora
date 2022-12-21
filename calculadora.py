from tkinter import Tk, Text, Button

class Interfaz:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora") 
        self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="orchid", foreground="white", font=("Helvetica",15))
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.operacion=""
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton4=self.crearBoton(u"\u232B",escribir=False)
        boton5=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton(u"\u00F7")
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        boton13=self.crearBoton(".")
        boton14=self.crearBoton(0)
        boton15=self.crearBoton("+")
        boton16=self.crearBoton("-")
        boton17=self.crearBoton("=",escribir=False,ancho=20,alto=2)

    def crearBoton(self,valor,escribir=True,ancho=9,alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda: self.click(valor,escribir))



ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()
