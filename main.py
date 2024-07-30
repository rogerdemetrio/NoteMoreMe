import flet as ft
import flet.canvas as cv

def main(page: ft.Page):
    # Padrões da pagina
    page.window.height = 900
    page.window.width = 600
    page.window.center()
    page.title = "NoteMoreMe"
    page.padding = 0
    page.bgcolor = ft.colors.WHITE70

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)

    input_texto = ft.Container(
            expand=True,
            content=ft.TextField(
                autocorrect = True,
                min_lines = 5,
                max_lines = 25,
                multiline = True,
                border = ft.InputBorder.NONE,
                bgcolor = ft.colors.TRANSPARENT,
                filled = True,
                color = ft.colors.BLUE_GREY_800,
                content_padding = 60
            ))
    
    cp = cv.Canvas(shapes=[cv.Path([cv.Path.MoveTo(60, 0),cv.Path.LineTo(60, 3000)],paint=ft.Paint(style=ft.PaintingStyle.STROKE,color=ft.colors.PINK_ACCENT_700),),],width=float("inf"))
    for x in range(50):
        y = x * 24
        linha = cv.Path([cv.Path.MoveTo(0, y),cv.Path.LineTo(3000, y)],paint=ft.Paint(style=ft.PaintingStyle.STROKE,color=ft.colors.BLUE_500),)
        cp.shapes.append(linha)
    page.add(cp)
    page.add(input_texto)
    
ft.app(target=main,name="NoteMoreMe") 