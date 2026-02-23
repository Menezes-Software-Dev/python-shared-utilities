# --- Numeric Validator Suite v4 (High-Precision Manual Parsing) ---
# This version prioritizes data integrity by processing strings character by character.
# By avoiding direct string-to-float conversion, we eliminate binary representation 
# noise (e.g., 52.300000000000004). 
# Returns: [Status, Converted Value, Is_Negative, Is_Float]

def numeric_validator(num):
    """
    Sanitizes numerical strings using manual fixed-point logic for maximum precision.
    Ideal for ERPs and industrial systems where precision is mandatory.
    """
    # Verifica se a entrada é uma string para evitar erros de processamento
    if not isinstance(num, str):
        return [False, num, False, False]

    # Buffer para armazenar apenas os dígitos numéricos extraídos
    buffer_digits = ""
    # Flag booleana para indicar se um separador decimal foi encontrado
    is_float = False
    # Contador para rastrear o número de dígitos após o separador
    decimal_count = -1
    # Verifica se a string começa com sinal de menos (ignorando espaços iniciais)
    is_negative = num.strip().startswith("-")

    # Passo 1: Loop de leitura caractere a caractere
    for char in num:
        # Se encontrar vírgula ou ponto, marcamos o número como float
        if char in (",", "."):
            is_float = True
            continue # Pula para o próximo caractere sem adicionar o separador ao buffer
        
        # Só adiciona ao buffer se for dígito ou um sinal de menos no início
        if char.isdigit() or (char == "-" and not buffer_digits):
            buffer_digits += char # Concatena o dígito à string limpa
            # Se já passamos por um separador, incrementamos o contador de casas decimais
            if is_float:
                decimal_count += 1

    try:
        # Passo 2: Validação Básica
        # Se o buffer estiver vazio ou contiver apenas o sinal de menos, a entrada é inválida
        if not buffer_digits or buffer_digits == "-":
            return [False, num, False, False]

        # Passo 3: Lógica de Reconstrução Numérica
        if is_float:
            # Converte a string limpa de dígitos para float
            valor_bruto = float(buffer_digits)
            # Reposiciona a vírgula dividindo por 10 elevado à quantidade de casas decimais
            converted_val = valor_bruto / (10 ** (decimal_count + 1))
        else:
            # Se não houver separador, converte diretamente para inteiro
            converted_val = int(buffer_digits)

        # Passo 4: Retorno Final
        # Retorna [Sucesso, Valor, Flag_Negativo, eh_float]
        return [True, converted_val, is_negative, is_float]

    except (ValueError, ZeroDivisionError):
        # Captura qualquer erro inesperado de conversão ou cálculo
        return [False, num, False, False]