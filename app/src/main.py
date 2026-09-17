import flet as ft


def main(page: ft.Page):
    page.title = "YouTube Playlist Player"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 700
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Componentes de Entrada
    txt_busca = ft.TextField(
        hint_text="Cole a URL ou digite o nome do vídeo...", expand=True
    )
    btn_buscar = ft.Button("Adicionar", icon=ft.Icons.ADD)

    # Lista da Playlist
    lista_playlist = ft.ListView(expand=True, spacing=10, padding=10)

    # Controles
    lbl_tocando = ft.Text("Nenhuma música tocando", size=14, italic=True)
    btn_play_pause = ft.IconButton(icon=ft.Icons.PLAY_ARROW, icon_size=32)

    # Adicionando elementos à página
    page.add(
        ft.Text("🎵 Playlist Player", size=24, weight=ft.FontWeight.BOLD),
        ft.Row([txt_busca, btn_buscar]),
        ft.Divider(),
        ft.Text("Sua Playlist:", size=16, weight=ft.FontWeight.BOLD),
        ft.Container(
            content=lista_playlist,
            border=ft.Border.all(1, ft.Colors.GREY_800),
            border_radius=8,
            height=350,
        ),
        ft.Divider(),
        lbl_tocando,
        ft.Row([btn_play_pause], alignment=ft.MainAxisAlignment.CENTER),
    )


# Execução moderna (sem necessidade de parâmetro target)
ft.run(main)