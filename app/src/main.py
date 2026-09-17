import flet as ft
import yt_dlp


def buscar_video_youtube(query: str):
    """Busca informações do vídeo no YouTube via yt-dlp."""
    ydl_opts = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "quiet": True,
        "default_search": "ytsearch1",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        url = query if query.startswith("http") else f"ytsearch1:{query}"
        info = ydl.extract_info(url, download=False)
        if "entries" in info:
            info = info["entries"][0]
        return {
            "id": info["id"],
            "title": info["title"],
            "duration": info.get("duration_string", "00:00"),
            "webpage_url": info["webpage_url"],
        }


def main(page: ft.Page):
    page.title = "YouTube Playlist Player"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 700

    txt_busca = ft.TextField(hint_text="URL ou nome da música...", expand=True)
    lista_playlist = ft.ListView(expand=True, spacing=10, padding=10)

    def acao_buscar(e):
        if not txt_busca.value:
            return

        btn_buscar.disabled = True
        page.update()

        try:
            dados = buscar_video_youtube(txt_busca.value)

            lista_playlist.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.MUSIC_NOTE),
                    title=ft.Text(
                        dados["title"],
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                    subtitle=ft.Text(f"Duração: {dados['duration']}"),
                    trailing=ft.IconButton(
                        icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_400
                    ),
                )
            )
            txt_busca.value = ""
        except Exception as err:
            page.open(ft.SnackBar(content=ft.Text(f"Erro ao buscar: {err}")))

        btn_buscar.disabled = False
        page.update()

    btn_buscar = ft.Button(
        "Adicionar", icon=ft.Icons.ADD, on_click=acao_buscar
    )

    page.add(
        ft.Text("🎵 Playlist Player", size=24, weight=ft.FontWeight.BOLD),
        ft.Row([txt_busca, btn_buscar]),
        ft.Divider(),
        ft.Container(
            content=lista_playlist,
            border=ft.Border.all(1, ft.Colors.GREY_800),  # CORRIGIDO
            border_radius=8,
            height=450,
        ),
    )


ft.run(main)  # CORRIGIDO