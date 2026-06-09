# AltBAR 🚀
O altímetro open-source da BAR.

## Histórico
Desenvolvido por Rodrigo de Marco, em seu trabalho de conclusão de curso de Engenharia Elétrica em 2016, o Microaltímetro Universal (MAU) foi o primeiro altímetro compacto produzido e comercializado no Brasil com aplicação em foguetemodelismo.  

Após o término do curso de graduação, Rodrigo mudou-se para a Holanda, mas com o apoio de Arthur Lang, seu colega de graduação, centenas de unidades do Microaltímetro Universal foram produzidas. As placas de circuito impresso eram produzidas pela empresa Circuitel em Curitiba, os componentes passivos eram comprados de uma distribuidora em São Paulo, e os ATtiny85, BMP280 e baterias importados da China. 

Com dimensões de 18 mm x 14 mm x 6 mm e massa 2 g, o MAU foi utilizado em várias edições do Festival Brasileiro de Minifoguetes e por vários grupos de foguetes no Brasil.

No entanto, devido à dificuldade de encontrar quem pudesse realizar a montagem dos componentes com qualidade e com preço baixo, a produção do altímetro foi descontinuada. Deste modo, restou apenas a possibilidade de importação de altímetros compactos, como o MicroPeak, cujo custo é praticamente proibitivo para a maioria entusiastas do foguetemodelismo.

Em 2018, Rodrigo de Marco disponibilizou publicamente o projeto do MAU em seu repositório no [GitHub](https://github.com/DeMarco/MAU-1.0). A partir deste projeto, em 2025, a Comissão de Eletrônicos de Custo Baixo da BAR (Associação Brasileira de Foguetemodelismo) iniciou o desenvolvimento do AltBAR com objetivo de viabilizar a produção de altímetros compactos por preços mais acessíveis. O AltBAR, portanto, é a continuidade do Microaltímetro Universal (MAU). 

## Altímetro e seus acessórios

<img width="886" height="664" alt="image" src="https://github.com/user-attachments/assets/a69341de-8c5a-4439-ab27-156651759ae3" />

A)	AltBAR
-	Dimensões: 30 mm x 16 mm x 6 mm
-	Massa com bateria CR1025 (3 V): 3,5 g
-	Gravação de até 46 segundos de voo
  
B)	Cabo 6 vias com fios invertidos nas extremidades. Os conectores são do tipo JST-GH 1.25 mm

C)	Placa adaptadora 

D)	Gravador AVR USB-ASP. IMPORTANTE: o jumper deve selecionar a tensão de 3,3 V

## Onde comprar?
Os arquivos de produção do AltBAR e da placa adaptadora (Gerber, BOM, Pick and place) estão [https://github.com/gbertoldo/AltBAR-UI/tree/master/Hardware](disponíveis publicamente), de modo que qualquer pessoa poderá solicitar o altímetro pronto em sites como PCBWay ou JLCPCB. O cabo JST-GH e o Gravador AVR USB-ASP podem ser encontrados em diversas lojas online.

Alternativamente, é possível adquirir o altímetro através dos fornecedores XX?

## Como utilizar o AltBAR
-	Insira a bateria CR1025 no altímetro.
-	Mude a chave para a posição “on”. O LED piscará três vezes indicando a inicialização. Em seguida, caso haja dados na memória, o LED piscará o apogeu. 
-	Insira o altímetro no minifoguete dentro de 60 s após ligá-lo. Esse é o tempo que o altímetro reserva para evitar que a inserção no minifoguete possa causar um falso evento de decolagem. Passados os 60 s, o LED pisca a cada um segundo, indicando que o altímetro está pronto para o lançamento.
-	Lance o minifoguete.
-	Recupere o altímetro, mova a chave para a posição “off” e aguarde 15 segundos antes de ligá-lo novamente. 
Observação:
-	Não é necessário apagar a memória do último voo. Caso exista, ela será sobrescrita. Por este motivo, é necessário cuidado ao manusear o altímetro após o voo. Não exponha o sensor à luz direta do Sol e nem à variações abruptas de pressão (como rajadas de vento).

## Interface gráfica – AltBAR-UI
### Visão geral
A interface gráfica AltBAR-UI é a forma mais simples para extrair os dados de voo, limpar a memória e gravar o firmware no altímetro. 

<img width="886" height="471" alt="image" src="https://github.com/user-attachments/assets/f92864a6-4805-4841-b8ee-46e9a978ca25" />

Para utilizá-la, siga os passos a seguir:
1)	Baixe e descompacte a interface AltBAR-UI;
2)	Acesse o diretório e rode o executável AltBAR-UI.exe;
3)	 Conecte as partes A, B, C e D. Garanta que o jumper do USB-ASP está na posição 3,3 V. Em seguida, conecte o gravador USB-ASP na porta USB do computador; 
4)	Mude a chave seletora do AltBAR para “off”. Nesta posição, o altímetro será desconectado da bateria, mas conectado à alimentação do computador.

### Gravação de firmware
Antes do primeiro uso do altímetro, é necessário carregar o firmware no microcontrolador, isto é, o software que fará a gestão do altímetro. Este procedimento precisa ser realizado somente uma vez. No menu “Operações” da interface gráfica, selecione a opção “Gravar firmware”.
 
Ao final da gravação, a seguinte mensagem será exibida no terminal inferior da interface:

<img width="480" height="314" alt="image" src="https://github.com/user-attachments/assets/4b28c2c9-34ad-4979-ab85-7fbc00b0bb0e" />

### Extração de dados de voo
Para extrair os dados do último voo, clique no botão “Extrair dados” na lateral direita da interface gráfica ou através do menu “Operações”, item “Extrair dados”. Caso haja dados de voo, será exibido um gráfico da altura como função do tempo na parte central da interface. Os mesmos dados do gráfico podem ser acessados através do botão “Relatório” ou no menu “Operações”, item “Relatório”.
Limpeza da memória de voo
Para limpar a memória de voo, basta clicar no botão “Limpar memória” na lateral direita da interface gráfica ou através do menu “Operações”, item “Limpar memória”. 
## Agradecimento
A Associação Brasileira de Minifoguetes (BAR) agradece a Rodrigo de Marco pela contribuição com o desenvolvimento do MAU e por compartilhar publicamente o seu projeto.
A BAR também agradece Ijanai dos Santos Sobrinho e Pedro Alves pela compra do primeiro lote de testes de AltBAR.




