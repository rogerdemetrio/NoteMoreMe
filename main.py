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

    tamanho_letra = 16

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)

    input_texto = ft.Container(expand=True,content=ft.TextField(autocorrect = True,min_lines = 5,max_lines = 29,multiline = True,border = ft.InputBorder.NONE,bgcolor = ft.colors.TRANSPARENT,
            color = ft.colors.BLUE_GREY_800,content_padding = ft.padding.symmetric(horizontal=62,vertical=48),text_size= tamanho_letra
        ))

    def carrega_pagina(e):
        page.controls.clear()
        cp = cv.Canvas(shapes=[cv.Path([cv.Path.MoveTo(60, 0),cv.Path.LineTo(60, page.window.height)],paint=ft.Paint(style=ft.PaintingStyle.STROKE,color=ft.colors.PINK_ACCENT_700))])
        for x in range(330):
            y = (x * 24) + 1
            linha = cv.Path([cv.Path.MoveTo(0, y),cv.Path.LineTo((page.window.width), y)],paint=ft.Paint(style=ft.PaintingStyle.STROKE,color=ft.colors.BLUE_400))
            if y > 48 and y < (page.window.height - 60):
                cp.shapes.append(linha)
        page.add(cp)
        page.add(input_texto)
    
    page.on_resized = carrega_pagina
    page.update()

ft.app(target=main,name="NoteMoreMe") 