## Modelagem TROPOS do PP
Aluno : Tarcísio Batista de Freitas Junior 20/0052128

> Explicação : Olá professora, depois da revisão do PEAS do meu projeto, a senhora verificou que o sistema modelado não tinha 
necessidade de um agente para resolvê-lo. Portanto , fiz algumas modificações na idéia original. A minha idéia original era uma analisador 
de comentário de uma viagem de ônibus. A idéia agora se baseia em 2 agentes embutidos em um transporte público. Nesse caso, o sistema do carro
é autônomo e o ônibus percorre um grid bidimensional. Terei então 2 agentes, um para defição do caminho a ser seguido. E outro que, de acordo com a  interação do passageiro com o veículo, toma atitudes para melhorar a qualidade da viagem.

Como não é a idéia dessa atividade, fiz apenas um mini-PEAS para explica-los.

**Agente 1 -** _Software do veículo para movimentar-se_

1. A célula pode possuir buraco, onde reflete a luz, e é captada pelo sensor do ônibus. o caminho possui 4 buracos, que tem chance de 40%
de furar o pneu, fazendo a viagem falhar.<br></br>
2. A célula pode ter uma barricada de moradores, impedindo sua passagem. Neste caso, o veículo deve mudar sua direção - ele só pode andar 
em células adjacentes. São 5 barricadas no caminho, que podem acabar criando caminhos sem saída. Nese caso, o veículo deve voltar e percorrer outro.<br></br>
3. O caminho é um grid de proporções 7x7 onde o veículo deve andar o menor número possível de células para chegar ao destino. Saindo da
posição [0,0] e chegando na posição [7,7];<br></br>
4. O objetivo é chegar ao final, pelo menor caminho e mais seguro possível.

**Agente 2 -** _Software de atendimento ao passageiro_

1. O software registra a temperatura local, e de acordo com o registro, deve ligar o ar condicionado ou o aquecedor do veículo.
2. O software registra a claridade local, e de acordo com a mesma, fecha ou abre a cortina, ou acende a luz individual de cada passageiro.
3. O software capta os dados inseridos no computador de bordo de cada passageiro para saber se alguma atitude é necessária, sem que 
os valores sejam alcançados.
4. O objetivo do software é proporcionar a melhor experiência de viagem para cada passageiro. Dá-se por completo, se ao final da viagem,
a avaliação do atendimento eletrônico for maior ou igual a 8. 

A imagem a seguir mostra o ambiente percorrido pelo veículo:

<br><br>
<br><br>
<br><br>
<br><br>


 <table style="border: 1px solid black;">
  <tr style="border: 1px solid black;">
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🌋</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🏁</th>
  </tr>
  <tr style="border: 1px solid black;">
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
  </tr>
  <tr style="border: 1px solid black;">
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🕳️</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🌋</th>
  </tr>
   <tr style="border: 1px solid black;">
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🌋</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🕳️</th>
  </tr>
   <tr style="border: 1px solid black;">
    <th style="border: 1px solid black;">🕳️</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🌋</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
  </tr>
   <tr style="border: 1px solid black;">
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🕳️</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
  </tr>
   <tr style="border: 1px solid black;">
       <th style="border: 1px solid black;" >🚐</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">🌋</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
    <th style="border: 1px solid black;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>

  </tr>
</table>

### Legendas
🚐 -> veículo <br></br>
🌋 -> barricada <br></br>
🕳️ -> buraco <br></br>
🏁 -> chegada <br></br>