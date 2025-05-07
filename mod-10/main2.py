def format_name(f_name, l_name):
    """Vai pegar o primeiro nome e o sobrenome e transforma usando caixa alto ou simples """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    print("depois do return")


formated_string = format_name(f_name="AlISon", l_name="SUASSUNA")

length = len(formated_string)

# aaaaaaa