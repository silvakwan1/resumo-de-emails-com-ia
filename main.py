import os
from dotenv import load_dotenv
from Gemini import Gemini
from Inteirar_sobre_o_array import Inteirar_sobre_o_array

load_dotenv()

API_KEY = os.getenv("GEMINI_KAY")

if not API_KEY:
    print("ERRO: A variável GEMINI_KAY não foi encontrada no arquivo .env")
    exit(1)

# Lista de emails
emails_corpos = [
    "Boa tarde!\n\nVenho por meio deste e-mail solicitar informações mais detalhadas sobre os serviços oferecidos por sua empresa. Tenho interesse em entender melhor como funciona o processo de contratação, quais soluções estão disponíveis e de que forma elas podem atender às minhas necessidades atuais.\n\nCaso possível, peço também o envio de materiais complementares ou uma apresentação institucional.\n\nFico no aguardo do seu retorno.\n\nAtenciosamente.",
    "Olá, tudo bem?\n\nGostaria de solicitar um orçamento referente aos serviços que vocês oferecem. Atualmente estou avaliando algumas opções no mercado e acredito que sua empresa pode ser uma excelente parceira.\n\nSe possível, peço que incluam no orçamento informações sobre prazos, formas de pagamento e suporte.\n\nAgradeço desde já pela atenção e fico no aguardo do retorno.",
    "Prezados,\n\nEstou entrando em contato para obter mais detalhes sobre as soluções disponibilizadas por sua empresa. Tenho interesse em compreender melhor os diferenciais, bem como os benefícios que podem agregar ao meu projeto.\n\nSe houver algum material explicativo ou portfólio, ficarei grato em receber.\n\nAguardo retorno.\n\nCordialmente.",
    "Boa noite!\n\nGostaria de verificar a disponibilidade de atendimento, bem como os valores relacionados aos serviços prestados. Estou em fase de planejamento e preciso reunir o máximo de informações possíveis para tomada de decisão.\n\nDesde já agradeço pela atenção e colaboração.\n\nObrigado.",
    "Olá,\n\nTenho interesse em contratar seus serviços e gostaria de receber mais informações sobre como funciona todo o processo, desde o primeiro contato até a execução.\n\nTambém gostaria de saber sobre prazos médios e formas de acompanhamento do serviço.\n\nFico no aguardo do retorno.\n\nAtenciosamente.",
    "Prezados senhores,\n\nVenho por meio deste solicitar um orçamento detalhado dos serviços oferecidos. Caso possível, peço que incluam informações sobre condições comerciais, prazos e diferenciais competitivos.\n\nAgradeço pela atenção dispensada.\n\nAtenciosamente.",
    "Bom dia!\n\nPoderiam me informar com mais detalhes como funciona o serviço oferecido por vocês? Tenho interesse em entender as etapas do processo, bem como os resultados esperados.\n\nSe possível, gostaria também de saber se há algum tipo de suporte após a contratação.\n\nObrigado pela atenção.",
    "Olá equipe,\n\nGostaria de entender melhor os planos e valores disponíveis. Estou analisando algumas opções e preciso de informações mais completas para comparação.\n\nCaso haja diferentes pacotes ou modalidades, peço a gentileza de detalhá-los.\n\nAguardo retorno.",
    "Boa tarde,\n\nEstou interessado em uma possível parceria entre nossas partes e gostaria de iniciar uma conversa para explorar oportunidades de colaboração.\n\nAcredito que podemos desenvolver algo vantajoso para ambos.\n\nFico à disposição para alinharmos uma reunião.\n\nAtenciosamente.",
    "Prezados,\n\nGostaria de solicitar suporte referente a um serviço contratado anteriormente. Estou enfrentando algumas dúvidas e preciso de orientação para dar continuidade corretamente.\n\nPeço, por gentileza, que me informem os próximos passos.\n\nFico no aguardo.",
    "Olá,\n\nPoderiam me enviar mais informações sobre os prazos de execução dos serviços? Essa informação é essencial para o meu planejamento interno.\n\nAlém disso, gostaria de saber se há possibilidade de personalização conforme a necessidade.\n\nObrigado.",
    "Bom dia,\n\nTenho interesse em conhecer melhor o portfólio da empresa, bem como os principais projetos já realizados.\n\nAcredito que isso ajudará bastante na minha avaliação.\n\nFico no aguardo do retorno.\n\nAtenciosamente.",
    "Boa tarde!\n\nGostaria de agendar uma conversa para entender melhor os serviços oferecidos. Acredito que uma reunião rápida pode facilitar bastante o alinhamento de expectativas.\n\nPor favor, me informem a disponibilidade.\n\nAtenciosamente.",
    "Olá,\n\nEstou atualmente avaliando fornecedores e gostaria de incluir sua empresa nesse processo.\n\nPara isso, preciso de algumas informações adicionais sobre serviços, valores e diferenciais.\n\nAguardo retorno.\n\nObrigado.",
    "Prezados,\n\nGostaria de confirmar algumas informações antes de prosseguir com a contratação do serviço.\n\nPeço a gentileza de esclarecer pontos relacionados a prazos, suporte e condições comerciais.\n\nObrigado pela atenção.",
    "Boa noite,\n\nPoderiam me informar se há suporte disponível após a contratação do serviço? Esse é um ponto muito importante para minha decisão.\n\nFico no aguardo da resposta.\n\nAtenciosamente.",
    "Boa tarde,\n\nGostaria de receber uma proposta comercial completa, incluindo valores, prazos e condições.\n\nEssa proposta será utilizada para análise interna.\n\nFico no aguardo.",
    "Olá,\n\nTenho interesse imediato na contratação dos serviços e gostaria de um retorno com certa urgência.\n\nSe possível, peço que priorizem este atendimento.\n\nObrigado pela atenção.",
    "Olá,\n\nGostaria de saber se vocês atendem na minha região e quais são as condições para isso.\n\nCaso haja alguma taxa adicional ou requisito específico, peço que informem.\n\nObrigado.",
    "Bom dia!\n\nEstou entrando em contato para tirar algumas dúvidas sobre os serviços oferecidos.\n\nTenho interesse em compreender melhor os benefícios e como eles podem se aplicar ao meu caso.\n\nAtenciosamente."
]

# Inicializa o cliente Gemini
gemini = Gemini(API_KEY)

# Itera sobre os emails e mostra os resumos
total_emails = len(emails_corpos)

for i, email in enumerate(Inteirar_sobre_o_array.get_items(emails_corpos)):
    print(f"\n{i+1}° email")
    print("-" * 66)
    
    resumo = gemini.resumir_email(email)
    print(f"\nResumo: {resumo}\n")
    
    print("-" * 66)
    restantes = total_emails - (i + 1)
    print(f"Ainda restam {restantes} emails para serem resumidos de {total_emails} total.")
    
    if restantes > 0:
        saida = input("\nVer mais um resumo? (sim para continuar, sair para encerrar): ").strip().lower()
        if saida == "sair":
            break
