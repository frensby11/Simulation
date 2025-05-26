import flet as ft
import threading
import time
import world
import subjets

def main(page: ft.Page):
    page.title = "Simulation"

    ### Simulacion en segundo plano ###
    def Simulation(e):
        def simulation():
             
            # Crear funcion para enviar textos a la terminalde debug #
            # funciones que afectan la interfaz
            def SendText(text):
                clock = time.localtime()
                clock = f"{clock.tm_hour}:{clock.tm_min}:{clock.tm_sec}" # Crear str del timepo actual del mensag  
                mesage = f"\n{clock} {text}" # Construir mensaje
                Debug.value = Debug.value + mesage
            


            cell = subjets.Subject(id=1213, name=cell, death=False, x=1, y=1)
            world.World.add_subject(subject=cell, position=[12,12])

            SendText(f'El sujeto {cell} a sido agregado al mundo')
            page.update()

            while InitSimulation.value == True: 
                
                page.update()

        thread = threading.Thread(target=simulation, daemon=True)
        thread.start()


    ## Funciones  ##


    ### Complementos ###
    InitSimulation = ft.Switch(value=False, on_change=Simulation)


    # Entry que voy a autilizar para el debug de la app
    Debug = ft.TextField(
        multiline=True,
        read_only=True,
        filled=False,
        border_color=ft.Colors.TRANSPARENT,
        autofocus=True,
        color=ft.Colors.PURPLE,
    )

    # Parte isquierda de la ventana
    LeftColumn = ft.Column(
        expand=2,
        scroll=True,
        controls=[Debug]
    )

    # Parte derecha d ela ventana
    RightColumn = ft.Column(
        expand=1,
        scroll=True,
        width=200,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[InitSimulation]
        
    )

    # Dividir la ventana en dos usando Row con un divisor
    page.add(
        ft.Row(
            [
                LeftColumn,
                ft.VerticalDivider(width=1),
                RightColumn
            ],
            spacing=0,
            expand=True
        )
    )

    page.update()

ft.app(target=main)