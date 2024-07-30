import flet as ft

def main(page: ft.Page):
    # Padrões da pagina
    page.window.height = 960
    page.window.width = 640
    page.window.center()
    page.title = "NoteMoreMe"
    

    page.add(
        ft.Container(
            ft.TextField(
                autocorrect=True,
                min_lines=5,
                max_lines=25,
                multiline=True,
                border=ft.InputBorder.NONE,
                filled=True,
                hint_text="Comece seu texto por aqui ♥",
            )
        )
    )

    
ft.app(target=main,name="NoteMoreMe")