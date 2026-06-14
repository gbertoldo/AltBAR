# Instalação do driver para AVR-USB-ASP

O Windows geralmente não consegue carregar automaticamente o driver USB genérico correto exigido pelo AVRDUDE para este programador. Para corrigir o problema:
- Baixe o Zadig (uma ferramenta segura e de código aberto para instalar drivers USB genéricos) em [zadig.akeo.ie](zadig.akeo.ie).
- Conecte seu USBasp a uma porta USB.
- Abra o Zadig. No menu superior, selecione Opções -> marque a opção Listar todos os dispositivos.
- No menu suspenso principal, procure e selecione USBasp.
- Verifique se o ID USB corresponde ao erro: 16C0 e 05DC.
- Use a seta ao lado da caixa de driver de destino para escolher libusb-win32 (ou libusbK).
- Clique no botão grande que diz Substituir driver ou Instalar driver.
- Reinicie o AVRDUDE e tente executar o comando novamente.