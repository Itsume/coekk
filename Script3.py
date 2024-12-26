import discord
import asyncio
import os

# Função para obter o token
def get_token():
    token_file = "discord_token.txt"
    
    # Verifica se o token já foi salvo em um arquivo
    if os.path.exists(token_file):
        with open(token_file, "r") as file:
            token = file.read().strip()
            print("Token carregado a partir do arquivo.")
            return token
    else:
        # Se o arquivo não existir, solicita o token ao usuário e salva no arquivo
        token = input("Digite o seu token do Discord: ")
        with open(token_file, "w") as file:
            file.write(token)
            print("Token salvo para futuras execuções.")
        return token

# Função principal para o script
async def main():
    # Obter o token sem pedir novamente após a primeira vez
    token = get_token()

    # Solicitar os dados do servidor e canal
    guild_id = int(input("Digite o ID do servidor: "))
    channel_id = int(input("Digite o ID do canal: "))
    
    # Comandos a serem enviados
    comandos = [
        "k!crime", 
        "k!gf", 
        "k!fofocar", 
        "k!rep <@1254707566127091775>", 
        "k!dep all", 
        "k!work"
    ]
    
    # Cria uma instância do cliente
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'Logado como {client.user}')
        guild = client.get_guild(guild_id)
        if guild is None:
            print("Servidor não encontrado.")
            return

        channel = guild.get_channel(channel_id)
        if channel is None:
            print("Canal não encontrado.")
            return

        # Loop para enviar os comandos de 10 em 10 minutos
        while True:
            for comando in comandos:
                await channel.send(comando)
                print(f'Comando enviado: {comando}')
                await asyncio.sleep(5)  # Intervalo de 5 segundos entre comandos

            print("Ciclo completo. Aguardando 10 minutos para reiniciar.")
            await asyncio.sleep(600)  # Espera 10 minutos (600 segundos)

    # Inicia o cliente com o token
    await client.start(token)

# Executar o script
asyncio.run(main())
