import flet as ft
import flet.canvas as cv
import models as md


def main(page: ft.Page):
    # Padrões da pagina
    page.window.height = 720
    page.window.width = 420
    page.window.center()
    page.title = "NoteMoreMe"
    page.padding = 0
    page.bgcolor = ft.colors.WHITE70

    tamanho_letra = 16

    def add_banco(e):
        tb = md.Notas(texto = texto.value, titulo_texto = titulo_texto.value)
        md.session.add(tb)
        md.session.commit()
        texto.value = ""
        titulo_texto.value = ""
        page.update()

    bt = ft.Column([ft.FloatingActionButton(icon=ft.icons.POST_ADD,on_click=add_banco,tooltip="Adiciona o texto")],height=50)
    rail = ft.Column([ft.Container(expand=1,expand_loose=False,content=bt),ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        #width=60,
        expand=1,
        #group_alignment=-0.75,
        bgcolor=ft.colors.TRANSPARENT,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.TEXT_SNIPPET_OUTLINED, selected_icon=ft.icons.TEXT_SNIPPET, label="Novo"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Book",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Config"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    ),ft.Container(expand=1)],alignment=ft.alignment.center,width=60,)
    
    titulo_texto = ft.TextField(autocorrect = True,min_lines = 1,max_lines = 1,border = ft.InputBorder.NONE,bgcolor = ft.colors.TRANSPARENT,color = ft.colors.BLUE_GREY_800,
                         content_padding = ft.padding.only(top=40, right=62),text_size= (tamanho_letra*1.5))
    texto = ft.TextField(autocorrect = True,min_lines = 5,max_lines = 29,multiline = True,border = ft.InputBorder.NONE,bgcolor = ft.colors.TRANSPARENT,color = ft.colors.BLUE_GREY_800,
                         content_padding = ft.padding.only(top=18, right=62, bottom=48),text_size= tamanho_letra)
    
    def bg():
        cp = cv.Canvas(shapes=[cv.Path([cv.Path.MoveTo(60, 0),cv.Path.LineTo(60, page.window.height)],paint=ft.Paint(style=ft.PaintingStyle.STROKE,color=ft.colors.PINK_ACCENT_700))])
        for x in range(330):
            y = (x * 24) + 1
            linha = cv.Path([cv.Path.MoveTo(0, y),cv.Path.LineTo((page.window.width), y)],paint=ft.Paint(style=ft.PaintingStyle.STROKE,color=ft.colors.BLUE_400))
            if y > 48 and y < (page.window.height - 60):
                cp.shapes.append(linha)
        return cp

    
    input_texto = ft.Container(expand=True,content=texto)

    def carrega_pagina(e):
        page.controls.clear()
        page.add(bg())
        page.add(ft.Row([rail,ft.Column([titulo_texto,input_texto], alignment=ft.MainAxisAlignment.START, expand=True),],expand=True,))

    page.on_resized = carrega_pagina
    page.update()

ft.app(target=main,name="NoteMoreMe") 
