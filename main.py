import flet as ft


def main(page: ft.Page):
    # configuração da pagina
    page.title = "minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    # definição de funções
    def mostrar_nome(e):
        txt_resultado.value = input_nome.value + " " + input_sobrenome.value
        page.update()
    # criação de componentes
    input_nome = ft.TextField(label="Nome", hint_text="digite seu Nome")
    input_sobrenome = ft.TextField(label="Sobrenome", hint_text="digite seu Sobrenome")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_nome,
    )
    txt_resultado = ft.Text(value="")




    # botao(input)




    # contruir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,

                btn_enviar,
                txt_resultado,
            ]

        )

    )


ft.app(main)
