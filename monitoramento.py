# ============================================================
# PROJETO 09 - CIDADE INTELIGENTE
# Sistema de Monitoramento de Sensores - Nova Aurora
# ============================================================

# -------------------- LIMITES -------------------------------

LIMITE_MINIMO = 0
LIMITE_ATENCAO = 30
LIMITE_CRITICO = 40
LIMITE_MAXIMO = 60


# -------------------- CADASTRO DOS SENSORES -----------------

sensores = [
    {
        "id": "N01",
        "regiao": "Norte",
        "localizacao": "Praça Central",
        "ip": "192.168.10.10",
        "temperatura": 25.5,
        "online": True
    },
    {
        "id": "N02",
        "regiao": "Norte",
        "localizacao": "Rua das Flores",
        "ip": "192.168.10.11",
        "temperatura": 35.0,
        "online": True
    },
    {
        "id": "S01",
        "regiao": "Sul",
        "localizacao": "Centro Comercial",
        "ip": "192.168.20.10",
        "temperatura": 42.5,
        "online": True
    },
    {
        "id": "S02",
        "regiao": "Sul",
        "localizacao": "Parque Municipal",
        "ip": "192.168.20.11",
        "temperatura": 28.0,
        "online": False
    },
    {
        "id": "S03",
        "regiao": "Sul",
        "localizacao": "Avenida Principal",
        "ip": "192.168.20.12",
        "temperatura": -5,
        "online": True
    }
]


# -------------------- RELATÓRIO -----------------------------

def criar_relatorio():
    """Cria os contadores de cada região."""

    categorias = [
        "Normal",
        "Atenção",
        "Crítica",
        "Inválida",
        "Offline"
    ]

    return {
        regiao: {categoria: 0 for categoria in categorias}
        for regiao in ["Norte", "Sul"]
    }


# -------------------- VALIDAÇÃO -----------------------------

def validar_temperatura(temperatura):
    """Verifica se a temperatura é numérica e está dentro dos limites."""

    if isinstance(temperatura, bool):
        return False

    if not isinstance(temperatura, (int, float)):
        return False

    if not LIMITE_MINIMO <= temperatura <= LIMITE_MAXIMO:
        return False

    return True


# -------------------- CLASSIFICAÇÃO -------------------------

def classificar_temperatura(temperatura):
    """Classifica a temperatura de acordo com os limites definidos."""

    if not validar_temperatura(temperatura):
        return "Inválida"

    if temperatura < LIMITE_ATENCAO:
        return "Normal"

    if temperatura < LIMITE_CRITICO:
        return "Atenção"

    return "Crítica"


# -------------------- PROCESSAMENTO -------------------------

def processar_sensor(sensor, relatorio):
    """Verifica o sensor e registra sua classificação."""

    print("\n" + "-" * 50)
    print("SENSOR:", sensor["id"])
    print("Região:", sensor["regiao"])
    print("Localização:", sensor["localizacao"])
    print("Endereço IP:", sensor["ip"])

    # Verifica a disponibilidade simulada do sensor
    if not sensor["online"]:
        classificacao = "Offline"
        print("ALERTA: SENSOR SEM COMUNICAÇÃO")

    else:
        temperatura = sensor["temperatura"]
        classificacao = classificar_temperatura(temperatura)

        print("Temperatura:", temperatura, "°C")
        print("Classificação:", classificacao)

        if classificacao == "Atenção":
            print("ALERTA: Temperatura acima do normal!")

        elif classificacao == "Crítica":
            print("ALERTA CRÍTICO: Temperatura muito elevada!")

        elif classificacao == "Inválida":
            print("ERRO: Medição inválida!")

    # Atualiza o relatório da região
    relatorio[sensor["regiao"]][classificacao] += 1


# -------------------- RELATÓRIO FINAL -----------------------

def gerar_relatorio(relatorio):
    """Exibe os resultados por região e o resumo geral."""

    print("\n")
    print("=" * 50)
    print("          RELATÓRIO FINAL")
    print("       CIDADE NOVA AURORA")
    print("=" * 50)

    # Exibe os resultados de cada região
    for regiao, dados in relatorio.items():

        print("\nREGIÃO:", regiao)
        print("-" * 35)

        for categoria, quantidade in dados.items():
            print(f"{categoria}: {quantidade}")

    # Calcula o resumo geral
    totais = {
        categoria: sum(
            dados[categoria] for dados in relatorio.values()
        )
        for categoria in relatorio["Norte"]
    }

    total_sensores = len(sensores)
    total_online = total_sensores - totais["Offline"]
    total_alertas = totais["Atenção"] + totais["Crítica"]

    print("\n" + "=" * 50)
    print("          RESUMO GERAL")
    print("=" * 50)

    print("Total de sensores:", total_sensores)
    print("Sensores online:", total_online)
    print("Sensores offline:", totais["Offline"])
    print("Temperaturas normais:", totais["Normal"])
    print("Temperaturas em atenção:", totais["Atenção"])
    print("Temperaturas críticas:", totais["Crítica"])
    print("Medições inválidas:", totais["Inválida"])
    print("Alertas de temperatura:", total_alertas)

    print("\nMonitoramento finalizado!")
    print("=" * 50)


# -------------------- EXECUÇÃO PRINCIPAL --------------------

def executar_monitoramento():
    """Executa o monitoramento de todos os sensores."""

    print("=" * 50)
    print("       CENTRAL DE MONITORAMENTO")
    print("          CIDADE NOVA AURORA")
    print("=" * 50)

    relatorio = criar_relatorio()

    for sensor in sensores:
        processar_sensor(sensor, relatorio)

    gerar_relatorio(relatorio)


# Inicia o programa
if __name__ == "__main__":
    executar_monitoramento()
