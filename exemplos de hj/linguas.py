import random
import time

def gerar_codigo_estudo():
    return "LINGUA" + str(random.randint(1000, 9999))

def simular_status_estudo():
    status = [
        "Primeiros passos no idioma",
        "Vocabulário básico aprendido",
        "Compreensão oral em progresso",
        "Conversação intermediária",
        "Pronto para certificação internacional!"
    ]
    return random.choice(status)

def simulador_estudo_linguas():
    print("=" * 70)
    print("🌍 SIMULADOR DE PROGRESSO EM LÍNGUAS | ESTUDE E ACOMPANHE SUA JORNADA 🌍")
    print("=" * 70)

    # Entrada básica
    estudante = input("\n👤 Nome do estudante: ")
    linguas = input("🗣️ Quais idiomas você quer estudar? (ex: Inglês, Espanhol, Francês): ").split(",")
    linguas = [l.strip().capitalize() for l in linguas]
    horas_semanais = int(input("⏰ Quantas horas por semana você pode dedicar aos estudos? "))

    print(f"\n📚 Idiomas selecionados: {', '.join(linguas)}")
    print(f"⏳ Dedicação semanal: {horas_semanais} horas")

    # Pacotes de estudo
    print("\n🎁 PACOTES DE ESTUDO DISPONÍVEIS:")
    pacotes = {
        "1": {"bonus": "Acesso a podcasts", "monitoria": False, "certificado": False, "relatorio": False},
        "2": {"bonus": "Aulas ao vivo + podcasts", "monitoria": True, "certificado": True, "relatorio": True},
        "3": {"bonus": "Aulas VIP, podcasts, clube de conversação", "monitoria": True, "certificado": True, "relatorio": True}
    }

    for nome, dados in pacotes.items():
        print(f"🌟 Pacote {nome} | Bônus: {dados['bonus']} | Monitoria: {'Sim' if dados['monitoria'] else 'Não'} | Certificado: {'Sim' if dados['certificado'] else 'Não'} | Relatório de progresso: {'Sim' if dados['relatorio'] else 'Não'}")

    pacote_escolhido = input("\n📦 Escolha um pacote (1, 2, 3): ").strip()
    if pacote_escolhido not in pacotes:
        print("❌ Pacote inválido, usaremos o padrão 1.")
        pacote_escolhido = "1"

    pacote = pacotes[pacote_escolhido]

    # Simulação de progresso
    print("\n🚀 ACOMPANHAMENTO DO SEU PROGRESSO:")
    codigo = gerar_codigo_estudo()
    print(f"🔑 Seu código de acompanhamento: {codigo}")
    for lingua in linguas:
        print(f"\n🌐 Idioma: {lingua}")
        for i in range(3):
            status = simular_status_estudo()
            print(f"📈 Status: {status}")
            time.sleep(1)
        print(f"🎉 Continue praticando {lingua} para alcançar fluência!")

    # Relatório detalhado
    if pacote["relatorio"]:
        print("\n📊 Relatório de progresso será enviado por e-mail semanalmente.")
        print("Inclui gráficos de evolução, dicas personalizadas e feedback dos professores.")

    # Certificado
    if pacote["certificado"]:
        print("\n🎓 Ao concluir o curso, você receberá um certificado internacional reconhecido!")

    # Monitoria
    if pacote["monitoria"]:
        print("\n👩‍🏫 Monitoria individual disponível para tirar dúvidas e acelerar seu aprendizado.")

    # Estratégia motivacional
    print("\n🚩 DICAS PARA APRENDER MAIS RÁPIDO:")
    print("✔️ Pratique todos os dias, mesmo que por pouco tempo.")
    print("✔️ Participe de clubes de conversação e grupos de estudo.")
    print("✔️ Use aplicativos, músicas e filmes no idioma escolhido.")
    print("✔️ Não tenha medo de errar: cada erro é um passo para a fluência!")
    print("\n🎁 Feche agora e ganhe uma aula experimental grátis em qualquer idioma!")
    print("📞 Fale com a equipe: idiomas@estudomax.com | WhatsApp: (11) 97777-7777")
    print("💡 EstudoMax: Seu futuro bilíngue começa aqui!")

# Executa o programa
if __name__ == "__main__":
    simulador_estudo_linguas()