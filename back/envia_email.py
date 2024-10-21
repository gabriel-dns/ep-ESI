import smtplib
import os
from email.mime.text import MIMEText


class Email():
    

    def trata_json():
        #Função que recebe json e devolve os valores para envio do email
        pass


    def envia_email(subject, sender, recipients, deadline, link):

        # subject, sender, recipients, deadline, link = trata_json(json)

        message = f"Olá aluno você está recebendo esta mensagem pois foi liberado o formulário a ser preenchido até a data de {deadline}.\nVocê consegue preencher o formulário de avaliação do semestre de pós-graduação clicando nesse link: {link}"
        print(message)


        # Criando a mensagem MIME com codificação UTF-8
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender
        # Retirado o To para os destinatários não saberem a lista de emails
        #msg['To'] = ', '.join(recipients)

        # Iniciando o servidor SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        #TODO: MUDAR ISSO AQUI PARA ALGUMA VARIÁVEL DE AMBIENTE OU SERVIÇO DE AUTENTICAÇÃO
        # Fazendo login no servidor   |
        #                             v
        server.login(sender, 'oxji jsrr ryry mlyu')

        # Enviando o e-mail
        server.sendmail(sender, recipients, msg.as_string())

        print("Email has been sent!")

    


if __name__ == "__main__":


    sender = 'esi.code.proj@gmail.com'
    recipients = ["kennedy_menezes@usp.br"]
    subject = "Link para Formulário Semestral"
    deadline = "2024-12-12"
    link = "link..."
    
    Email.envia_email(subject, sender, recipients, deadline, link)

    # Função final recebendo JSON
    # Email.envia_email(json)





