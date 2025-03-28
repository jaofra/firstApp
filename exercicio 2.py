import flet as ft


def main(page: ft.Page, mostrar_nome=None):
    # configuração da pagina
    page.title = "minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    # definição de funções
    def impar_par(e):
        num = input_numero.value
        try:
            num = int(num)
            if num % 2 == 0:
                txt_resultado.value = 'é par'
            else:
                txt_resultado.value = 'impar'
        except ValueError:
            txt_resultado.value = 'insira um valor correto'
        page.update()
    # criação de componentes
    input_numero = ft.TextField(label="numero", hint_text="digite um numero")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=impar_par
    )
    txt_resultado = ft.Text(value="")




    # botao(input)

    ft.TextField(label="Digite um numero:")



    # contruir o layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_enviar,
                txt_resultado,
            ]

        )

    )


ft.app(main)
