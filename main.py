import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.title = 'SignUp'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 300
    page.window_resizable = False

    #Setup Fields
    username: TextField = TextField(hint_text="Username", width=300, text_align=ft.TextAlign.LEFT)
    password: TextField = TextField(hint_text="Password", width=300, text_align=ft.TextAlign.LEFT,password=True)
    checkbox_signup : Checkbox = Checkbox(label="I agree", value=False)
    submitt: ElevatedButton = ElevatedButton(text='Sign Up', width = 300, disabled=True)

    def validate(e: ControlEvent) -> None:
        if all([username.value, password.value, checkbox_signup.value]):
            submitt.disabled = False
        else:
            submitt.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        print('Username', username.value)
        print("Password",password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f"Welcome: {username.value}",size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    checkbox_signup.on_change = validate
    username.on_change = validate
    password.on_change = validate
    submitt.on_click = submit

    #Render the page sign up
    page.add(
        Row(
            controls=[
                Column(
                    [username,password,checkbox_signup, submitt]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.app(target=main)


