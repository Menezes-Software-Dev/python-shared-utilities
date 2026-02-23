Data Cleaning Tools / Ferramentas de Limpeza de Dados

[EN] About / [PT] Sobre

[EN] This directory contains specialized scripts for data sanitization and normalization, focused on ensuring integrity before database insertion or mathematical processing. These tools were developed to bridge the gap between human-entered data and strict system requirements.

[PT] Este diretório contém scripts especializados para sanitização e normalização de dados, focados em garantir a integridade antes da inserção em base de dados ou processamento matemático. Estas ferramentas foram desenvolvidas para unir a flexibilidade da entrada de dados humana aos requisitos rigorosos do sistema.

🛠️ Tool: numeric_validator.py

[EN] A high-precision numerical validator that handles regional separators (commas and dots) and prevents binary noise.
[PT] Um validador numérico de alta precisão que trata separadores regionais (vírgulas e pontos) e evita ruído binário.

Why use this? / Porquê usar esta ferramenta?

[EN] No Binary Noise: By using manual character-by-character parsing, we avoid the common IEEE 754 float errors (like 52.300000000000004), ensuring the number remains exactly as typed.

[PT] Sem Ruído Binário: Ao utilizar análise manual caractere a caractere, evitamos os erros comuns de float IEEE 754 (como 52.300000000000004), garantindo que o número permaneça exatamente como foi digitado.

[EN] Full Metadata: Returns a structured list [Status, Value, Is_Negative, Is_Float], allowing the main system to make informed decisions based on the data's original state.

[PT] Metadados Completos: Retorna uma lista estruturada [Status, Valor, Negativo, eh_float], permitindo que o sistema principal tome decisões informadas com base no estado original do dado.

[EN] Dynamic Typing: Automatically detects and returns int or float based on the input string properties.

[PT] Tipagem Dinâmica: Deteta e retorna automaticamente int ou float baseado nas propriedades da string de entrada.

📈 Evolution History / Histórico de Evolução

[EN] This tool evolved through 4 distinct versions to reach professional maturity:

v1: Basic loop logic.

v2: Expansion to a function suite with negative support.

v3: Implementation of dynamic typing and metadata return.

v4: Refactored for high precision, manual parsing, and production-ready performance.

[PT] Esta ferramenta evoluiu através de 4 versões distintas até atingir a maturidade profissional:

v1: Lógica de loop básica.

v2: Expansão para uma suíte de funções com suporte a negativos.

v3: Implementação de tipagem dinâmica e retorno de metadados.

v4: Refatorada para alta precisão, análise manual e performance pronta para produção.

Status: Version 4 (Consolidated / Consolidada)