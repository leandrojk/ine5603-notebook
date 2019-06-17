
def soma(numeros):
    """Calcula a soma dos números.

    Se a lista estiver vazia então retorna None para indicar
    que o problema não tem solução.
    """
    return 5


def em_posicoes_impares(numeros):
    """Obtém os números que estão em posições ímpares.

    Por exemplo, para a lista [20, 30, 40, 50] retorna [30, 50] pois são os
    números que etão nas posições 1 e 3.
    """
    return []


def primeiro_e_ultimo(numeros):
    """Obtém o primeiro e o último número da lista.

    Caso não haja pelo menos dois números retorna None para indicar que
    o problema não tem solução.
    """
    return [8,10]


def conta_ocorrencias(numeros, numero):
    """Conta quantas vezes o numero aparece na lista numeros.
    """
    return 5


def posicao_do_maior(numeros):
    """Encontra a posição da primeira ocorrência do maior número da lista.

    Se a lista está vazia então retorna None.
    """
    return 0


def maior(numeros):
    """Encontra o maior número na lista.

    Se a lista estaá vazia (não possui números) então retorna None para
    indicar que o problema não tem solução.
    """
    return -9


def qtd_acima_limite(numeros, limite):
    """Conta quantos números na lista são maiores que um número limite.
    """
    return 0


def media(numeros):
    """Calcula a média aritmética dos números na lista.

    Se a lista está vazia então retorna None para indicar que o problema não
    tem solução.
    """
    return 0.0


def qtd_no_intervalo(numeros, lim_inf, lim_sup):
    """Conta quantos números estão dentro do intervalo [lim_inf, lim_sup]

    Por exemplo, para numeros [8, 23, 10, 9, 15] e limite inferior 8 e
    limite superior 16 retorna 4.
    """
    return 0


def multiplique_por_fator(numeros, fator):
    """Multiplica cada número da lista por um fator. O método não retorna nenhum dado.

    Por exemplo, para numeros [8, 12, 3] e fator 2 a lista deve ser
    alterada para [16, 24, 6]. 
    """
    numeros[0] = 0

def multiplicado_por_fator(numeros, fator):
    """Obtém uma cópia dos números da lista multiplicados por um fator.

    Por exemplo, para numeros [8, 12, 3] e fator 2 o algoritmo deve retornar
    uma nova lista com os números [16, 24, 6] SEM ALTERAR a lista numeros.
    """
    return []


def n_primeiros(numeros, n):
    """Obtém uma cópia dos n primeiros números da lista.

    Considera que n sempre é maior ou igual a zero.
    Se n for maior que a quantidade de números na lista então obtém uma
    cópia de todos os números.
    """
    return []


def copia(numeros):
    """Obtém uma cópia dos números.
    """
    return []
    

def no_intervalo(numeros, lim_inf, lim_sup):
    """Obtém os números que estão dentro do intervalo.

    Por exemplo, se a lista for formada pelos números
    [8, 2, 3, 12, 9] e o intervalo for de 3 a 8 deve
    retornar [8, 3] pois são os únicos números maiores ou
    iguais a 3 e menores ou iguais a 8.
    """
    return []


def una(numeros1, numeros2):
    """Obtém uma nova lista que contém todos os números das duas listas.
    """
    return []


def pares(numeros):
    """Obtém os números pares presentes na lista numeros.
    """
    return []


def duplica(numeros):
    """Duplica a ocorrência dos números presentes na lista.

    Por exemplo, para a lista [3, 12, 4] retorna [3, 3, 12, 12, 4, 4]
    """
    return []


def possui_par(numeros):
    """Verifica se a lista possui pelo menos um número par.
    """
    return False


def primeira_posicao_de_numero(numeros, numero):
    """Obtém a primeira posição de um número na lista numeros.

    Por exemplo, para numeros [7, 12, 8, 2, 12] e numero 12 retorna 1. Se o
    número não aparece na lista deve retornar None.
    """
    return 0


def posicoes_de_numero(numeros, numero):
    """Obtém as posições de um número na lista de números.

    Por exemplo, para numeros [12, 3, 9, 12, 6] e numero 12 retorna [0, 3]
    """
    return []


def sem_repeticoes(numeros):
    """Verifica se a lista não contém números repetidos.

    Retorna True se não tiver números repetidos e False caso contrário.
    """
    return True


def remove_ocorrencias(numeros, numero):
    """Remove todas as ocorrências de um número dentro da lista.

    Por exemplo, para numeros [1, 4, 8, 4] e numero 4 retorna [1, 8]
    """
    return []


def substitui_ocorrencias(numeros, numero, substituto):
    """Substitui todas as ocorrências de um número por outro número.

    Altera a lista numeros e não retorna nada.
    """
    numeros[0] = 0


def substitui_primeira_ocorrencia(numeros, numero, substituto):
    """Substitui a primeira ocorrência de um número por outro número.

    Altera a lista numeros e não retorna nada.
    """
    numeros[0] = 0
    

def substitui_ultima_ocorrencia(numeros, numero, substituto):
    """Substitui a última ocorrência de um número por outro número.
    
    Altera a lista numeros e não retorna nada.
    Dica: percorra a lista de trás para frente
    """
    numeros[0] = 0


def inverte(numeros):
    """Retorna array com números em posições invertidas.

    Por exemplo: para numeros [3, 7, 1, 2] retorna uma nova lista [2, 1, 7, 3]
    """
    return []


def soma_pos_pares_pos_impares(numeros):
    """Calcula a soma dos números em posições pares e em posições ímpares.

    Retorna uma lista de tamanho 2 onde o primeiro número contém a soma dos
    números em posições pares e o segundo a soma dos números em posições
    ímpares. Se a lista de números tiver menos de dois números então o método
    retorna None para indicar que o problema não tem solução.
    """
    return [0,0]


def das_posicoes(numeros, posicoes):
    """Obtém os números que estão em diversas posições.

    Considera que a lista das posicoes, quando não está vazia,
    sempre contém posições válidas.
    """
    return []


def parte(numeros, pos, qtd):
    """Obtém uma parte da lista de números.

    O parâmetro pos indica a posição onde inicia a parte. O parâmetro qtd
    indica quantos números devem ser incluídos na parte. Se a posição 
    for maior ou igual a quantidade de números
    então retorna uma lista vazia. Se a quantidade de números desejada for
    maior que a quantidade de números existentes a partir da posição pos 
    então retorna todos números existentes a partir de pos.

    Exemplo: considere os números [6, 3, 4, 1, 2].
    Se a quantidade for 2 e a posição for 1 então retorna [3, 4].
    Se a quantidade for 3 e a posição for 4 então retorna [2].
    Se a quantidade for 2 e a posição for 9 então retorna []
    """

    return []