import flet as ft

def main(page: ft.Page):
    
    page.title = "Pizza Builder"
    page.window.width = 600
    page.window.height = 700

    
    def toggle_pepperoni(e):
        pepperoni.visible = pepperoni_switch.value
        page.update()

    def toggle_mushrooms(e):
        mushrooms.visible = mushrooms_switch.value
        page.update()

    def toggle_olives(e):
        olives.visible = olives_switch.value
        page.update()

   
    base_pizza = ft.Image(
        src="assets/images/pizza_base.png",
        width=400,
        height=400
    )

   
    pepperoni = ft.Image(
        src="assets/images/pepperoni.png",
        width=320,
        height=320,
        left=40,
        top=40,
        visible=False
    )

    mushrooms = ft.Image(
        src="assets/images/mushrooms.png",
        width=320,
        height=320,
        left=40,
        top=40,
        visible=False
    )

    olives = ft.Image(
        src="assets/images/olives.png",
        width=320,
        height=320,
        left=40,
        top=40,
        visible=False
    )

    
    pizza_stack = ft.Stack(
        width=400,
        height=400,
        controls=[
            base_pizza,
            pepperoni,
            mushrooms,
            olives
        ]
    )

    
    pepperoni_switch = ft.Switch(label="Pepperoni", on_change=toggle_pepperoni)
    mushrooms_switch = ft.Switch(label="Mushrooms", on_change=toggle_mushrooms)
    olives_switch = ft.Switch(label="Olives", on_change=toggle_olives)

   
    page.add(
        ft.Column(
            [
                pizza_stack,
                pepperoni_switch,
                mushrooms_switch,
                olives_switch
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)