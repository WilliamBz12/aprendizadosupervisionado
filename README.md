# aprendizadosupervisionado
Arquivo utiliza tecnicas algebricas para encontrar o resultado
Pega varios vetores Ex: (1, 2, 3) = 1 ; (2,3,4) = 2; ...
E calcula a distância do vetor desejado para eles pelo metodo euclidiano
Ex: ( 3, 4, 5) = ?
Efetua-se o calculo da distancia desse vetor para os que foram utilizados para o aprendizado, 
amarzena-se em uma chave e organiza-se por ondem crescente.

Define-se um K (sempre bom ser impar) e pega-se os K arquivos mais proximos do vetor, efetuando
uma votação majoritaria.

E por fim retorna o resultado que obteu maior numero de 'votos'.
