import unittest
import processa_numeros as pn


class TestaModulo(unittest.TestCase):
            
    def test_soma(self):
        self.assertIsNone(pn.soma([]),
                          'soma de [] deveria dar None')
        self.assertEqual(pn.soma([5]), 5,
                         'soma de [5] deveria dar 5')
        self.assertEqual(pn.soma([1,2,3]), 6,
                         'soma de [1, 2, 3] deveria dar 6')

    def test_em_posicoes_impares(self):
        self.assertEqual(pn.em_posicoes_impares([]), [],
             'para lista [] deveria retornar []')

        self.assertEqual(pn.em_posicoes_impares([34]), [],
            'para lista [34] deveria retornar []')

        self.assertEqual(pn.em_posicoes_impares([23,87]), [87],
            'para lista [23, 87] deveria retornar [87]')

        self.assertEqual(pn.em_posicoes_impares([34,87,19]), [87],
            'para lista [34, 87, 19] deveria retornar [87]')

        self.assertEqual(pn.em_posicoes_impares([34,87,19,90]), [87,90],
            'para LISTA [34, 87, 19, 90] deveria retornar [87, 90]')

    def test_primeiro_e_ultimo(self):
        self.assertIsNone(pn.primeiro_e_ultimo([]),
                          'para lista [] deveria retornar None')

        self.assertIsNone(pn.primeiro_e_ultimo([8]),
                          'para lista [8] deveria retornar None')

        self.assertEqual(pn.primeiro_e_ultimo([8, 20]), [8, 20],
            'para lista [8, 20] deveria retornar [8, 20]')

        self.assertEqual(pn.primeiro_e_ultimo([8, 20,2,4,1, 30]), [8, 30],
            'para lista [8, 20, 2, 4, 1, 30] deveria retornar [8, 30]')

    def test_conta_ocorrencias(self):
        sae = self.assertEqual
        sae(pn.conta_ocorrencias([], 6), 0,
            'para lista [] e n 6 deveria retornar 0')

        sae(pn.conta_ocorrencias([10], 6), 0,
            'para lista [10] e n 6 deveria retornar 0')

        sae(pn.conta_ocorrencias([10, 20], 6), 0,
            'para lista [10, 20] e n 6 deveria retornar 0')

        sae(pn.conta_ocorrencias([6, 10, 20], 6), 1,
            'para lista [6, 10, 20] e n 6 deveria retornar 1')

        sae(pn.conta_ocorrencias([1, 10, 6], 6), 1,
            'para lista [1, 10, 6] e n 6 deveria retornar 1')

        sae(pn.conta_ocorrencias([1, 6, 6], 6), 2,
            'para lista [1, 6, 6] e n 6 deveria retornar 2')

        sae(pn.conta_ocorrencias([6, 6, 6], 6), 3,
            'para lista [6 6 6] e n 6 deveria retornar 3')

    def test_posicao_do_maior(self):
        sae = self.assertEqual
        self.assertIsNone(pn.posicao_do_maior([]),
            'para lista [] deveria retornar None')

        sae(pn.posicao_do_maior([8]), 0,
            'para lista [8] deveria retornar 0')

        sae(pn.posicao_do_maior([8, 1]), 0,
            'para lista [8, 1] deveria retornar 0')

        sae(pn.posicao_do_maior([3, 8]), 1,
            'para lista [3, 8] deveria retornar 1')

        sae(pn.posicao_do_maior([3, 8, 6]), 1,
            'para lista [3, 8, 6] deveria retornar 1')

        sae(pn.posicao_do_maior([1, 3, 8]), 2,
            'para lista [1, 3, 8] deveria retornar 2')

        sae(pn.posicao_do_maior([3, 3, 3]), 0,
            'para lista [3, 3, 3] deveria retornar 0')

        sae(pn.posicao_do_maior([-21, -3, -88]), 1,
            'para lista [-21, -3, -88] deveria retornar 1')

        sae(pn.posicao_do_maior([-21, -3, -88, 30, 6, 55, 4]), 5,
            'para lista [-21, -3, -88, 30, 6, 55, 4] deveria retornar 5')

    def test_maior(self):
        sae = self.assertEqual
        self.assertIsNone(pn.maior([]),
                          'para lista [] deveria retornar None')

        sae(pn.maior([6]), 6,
            'para lista [6] deveria retornar 6')

        sae(pn.maior([6, 3, 5]), 6,
            'para lista [6, 3, 5] deveria retornar 6')

        sae(pn.maior([6, 23, 35]), 35,
            'para lista [6, 23, 35] deveria retornar 55')

        sae(pn.maior([-6, -23, -35]), -6,
            'para lista [-6, -23, -35] deveria retornar -6')

        sae(pn.maior([8, 15, 35, 20, 66, 14, 29, 9]), 66,
            'para lista [8, 15, 35, 20, 66, 14, 29, 9] deveria retornar 66')

    def test_qtd_acima_limite(self):
        sae = self.assertEqual
        sae(pn.qtd_acima_limite([], 8), 0,
            'para lista [] deveria retornar 0')

        sae(pn.qtd_acima_limite([7], 8), 0,
            'para lista [7] e limite 8 deveria retornar 0')

        sae(pn.qtd_acima_limite([8], 8), 0,
            'para lista [8] e limite 8 deveria retornar 0')

        sae(pn.qtd_acima_limite([9, 8], 8), 1,
            'para lista [9, 8] e limite 8 deveria retornar 1')

        sae(pn.qtd_acima_limite([9, 8, 12], 8), 2,
            'para lista [9, 8, 12] e limite 8 deveria retornar 1')

        sae(pn.qtd_acima_limite([5, 76, 9], 8), 2,
            'para lista [6, 76, 9] e limite 8 deveria retornar 2')

    def test_media(self):
        self.assertIsNone(pn.media([]),
                          'para lista [] deveria retornar None')

        self.assertEqual(pn.media([9]), 9,
                         'para lista [9] deveria retornar 9.0')

        self.assertEqual(pn.media([9, 11]), 10,
                         'para lista [9, 11] deveria retornar 10.0')

        self.assertEqual(pn.media([8, 3, 6, 1]), 4.5,
                         'para lista [8, 3, 6, 1] deveria retornar 4.5')

    def test_qtd_no_intervalo(self):
        sae = self.assertEqual
        sae(pn.qtd_no_intervalo([], 2, 8), 0,
            'para lista [] deveria retornar 0')

        sae(pn.qtd_no_intervalo([1], 2, 8), 0,
            'para lista [1] e intervalo 2 8 deveria retornar 0')

        sae(pn.qtd_no_intervalo([2], 2, 8), 1,
            'para lista [2] e intervalo 2 8 deveria retornar 1')

        sae(pn.qtd_no_intervalo([2, 4], 2, 8), 2,
            'para lista [2, 4] e intervalo 2 8 deveria retornar 2')

        sae(pn.qtd_no_intervalo([2, 4, 8], 2, 8), 3,
            'para lista [2, 4, 8] e intervalo 2 8 deveria retornar 3')

    def test_multiplique_por_fator(self):
        sae = self.assertEqual
        mpf = pn.multiplique_por_fator
        a = []
        mpf(a, 8)
        sae(a, [], 'para lista [] deveria permanecer []')

        a = [2]
        mpf(a, 2)
        sae(a, [4], 'para lista [2] e fator 2 deveria alterar para [4]')

        a = [2, 3, 4]
        mpf(a, 2)
        sae(a, [4,6,8], 'para lista [2, 2, 4] e fator 2 deveria alterar para [4, 6, 8]')

        self.assertIsNone(mpf([], 7), 'sempre deveria retornar None')
        self.assertIsNone(mpf([8,4], 7), 'sempre deveria retornar None')
        self.assertIsNone(mpf([2,3,4,5,6], 7), 'sempre deveria retornar None')

    def test_multiplicado_por_fator(self):
        sae = self.assertEqual
        mpf = pn.multiplicado_por_fator
        a = []
        m = mpf(a, 8)
        sae(m, [], 'para lista [] deveria retornar []')
        self.assertIsNot(m, a, 'deveria retornar nova lista')

        a = [2]
        m = mpf(a, 2)
        sae(m, [4], 'para lista [2] e fator 2 deveria retornar [4]')
        self.assertIsNot(m, a, 'deveria retornar nova lista')

        a = [2, 3, 4]
        m = mpf(a, 2)
        sae(m, [4,6,8], 'para lista [2 2 4] e fator 2 deveria retornar [4 6 8]')
        self.assertIsNot(m, a, 'deveria retornar nova lista')


    def test_n_primeiros(self):
        sae = self.assertEqual
        npr = pn.n_primeiros
        a = []
        np = npr(a, 3)
        sae(np, [], 'para lista [] deveria retornar []')
        self.assertIsNot(np, a, 'deveria retornar nova lista')

        a = [4]
        np = npr(a, 3)
        sae(np, [4], 'para lista [4] e n 3 deveria retornar [4]')
        self.assertIsNot(np, a, 'deveria retornar nova lista')

        a = [4, 40, 50]
        np = npr(a, 0)
        sae(np, [], 'para lista [4 40 50] e n 0 deveria retornar []')
        self.assertIsNot(np, a, 'deveria retornar nova lista')

        a = [4, 40, 50]
        np = npr(a, 1)
        sae(np, [4], 'para lista [4 40 50] e n 1 deveria retornar [4]')
        self.assertIsNot(np, a, 'deveria retornar nova lista')

        a = [4, 40, 50]
        np = npr(a, 2)
        sae(np, [4,40], 'para lista [4 40 50] e n 2 deveria retornar [4, 40]')
        self.assertIsNot(np, a, 'deveria retornar nova lista')

        a = [4, 40, 50]
        np = npr(a, 3)
        sae(np, [4, 40, 50], 'para lista [4 40 50] e n 3 deveria retornar [4, 40, 50]')
        self.assertIsNot(np, a, 'deveria retornar nova lista')

        a = [4, 40, 50]
        np = npr(a, 4)
        sae(np, [4,40,50], 'para lista [4 40 50] e n 4 deveria retornar [4 40 50]')
        self.assertIsNot(np, a, 'deveria retornar nova lista')

    def test_copia(self):
        sae = self.assertEqual
        c = pn.copia
        a = []
        nc = c(a)
        sae(nc, [], 'para lista [] deveria retornar []')
        self.assertIsNot(nc, a, 'deveria retornar nova lista')

        a = [8]
        nc = c(a)
        sae(nc, [8], 'para lista [8] deveria retornar [8]')
        self.assertIsNot(nc, a, 'deveria retornar nova lista')

        a = [8, 9]
        nc = c(a)
        sae(nc, [8,9], 'para lista [8 9] deveria retornar [8 9]')
        self.assertIsNot(nc, a, 'deveria retornar nova lista')

        a = [7, 8, 9]
        nc = c(a)
        sae(nc, [7,8,9], 'para lista [7 8 9] deveria retornar [7 8 9]')
        self.assertIsNot(nc, a, 'deveria retornar nova lista')


    def test_no_intervalo(self):
        sae = self.assertEqual
        sain = self.assertIsNot
        msg_erro = 'com lista {} e intervalo {} deveria retornar nova lista {}'

        a = []
        no_int = pn.no_intervalo(a, 1, 20)
        sae(no_int, [], 'para lista [] deveria retornar []')
        sain(a, no_int, msg_erro.format(a, '1 20', []))
        sain(a, no_int, 'para lista [] deveria retornar nova lista []')

        a = [-2]
        no_int = pn.no_intervalo(a, 1, 20)
        sae(no_int, [], msg_erro.format(a, '1 20', []))

        a = [56, 87, 0]
        no_int = pn.no_intervalo(a, 1, 20)
        sae(no_int, [], msg_erro.format(a, '1 20', []))

        a = [3, 4, 5]
        no_int = pn.no_intervalo(a, 1, 20)
        sae(no_int, [3,4,5], msg_erro.format(a, '1 20', [3, 4, 5]))
        sain(a, no_int, msg_erro.format(a, '1 20', [3, 4, 5]))

        a = [1, 42, 53]
        no_int = pn.no_intervalo(a, 1, 20)
        sae(no_int, [1], msg_erro.format(a, '1 20', [1]))

        a = [88, 20, 53]
        no_int = pn.no_intervalo(a, 1, 20)
        sae(no_int, [20], msg_erro.format(a, '1 20', [20]))

        a = [88, 3, 25, 6, 53, 10]
        no_int = pn.no_intervalo(a, 1, 20)
        sae(no_int, [3,6,10], msg_erro.format(a, '1 20', [3, 6, 10]))

    def test_una(self):
        sae = self.assertEqual
        sain = self.assertIsNot

        a = []
        b = []
        u = pn.una(a, b)
        sae(u, [], 'unir [] com [] deveria retornar []')
        sain(u, a, 'unir [] com [] deveria retornar nova lista []')
        sain(u, b, 'unir [] com [] deveria retornar nova lista []')

        a = [1, 2, 3]
        b = []
        u = pn.una(a, b)
        sae(u, [1,2,3], 'unir [1, 2, 3] com [] deveria retornar [1, 2, 3]')
        sain(u, a, 'unir [1, 2, 3] com [] deveria retornar nova lista [1, 2, 3]')

        a = []
        b = [1, 2, 3]
        u = pn.una(a, b)
        sae(u, [1,2,3], 'unir [] com [1, 2, 3] deveria retornar [1, 2, 3]')
        sain(u, a, 'unir [] com [1, 2, 3] deveria retornar nova lista [1, 2, 3]')

        a = [1, 2]
        b = [3, 4]
        u = pn.una(a, b)
        sae(u, [1,2,3,4], 'unir [1, 2] com [3, 4] deveria retornar [1, 2, 3, 4]')
        sae(a, [1, 2], 'unir [1, 2] com [3, 4] deveria manter lista [1, 2]')
        sae(b, [3, 4], 'unir [1, 2] com [3, 4] deveria manter lista [3, 4]')

    def test_pares(self):
        sae = self.assertEqual
        sain = self.assertIsNot

        a = []
        p = pn.pares(a)
        sae(p, [], 'para lista [] deveria retornar []')
        sain(p, a, 'para lista [] deveria retornar nova lista []')

        a = [8]
        p = pn.pares(a)
        sae(p, [8], 'para lista [8] deveria retornar [8]')
        sain(p, a, 'para lista [8] deveria retornar nova lista [8]')

        a = [3]
        p = pn.pares(a)
        sae(p, [],'para lista [3] deveria retornar []')

        a = [2, 4, 6]
        p = pn.pares(a)
        sae(p, [2,4,6], 'para lista [2, 4, 6] deveria retornar [2, 4, 6]')
        sain(p, a, 'com array [2, 4, 6] deveria retornar nova lista [2, 4, 6]')

        a = [5, 1, 7]
        p = pn.pares(a)
        sae(p, [], 'para lista [5, 1, 7] deveria retornar []')

        a = [5, 8, 7]
        p = pn.pares(a)
        sae(p, [8], 'para lista [5, 8, 7] deveria retornar [8]')

        a = [5, 8, 7, 10]
        p = pn.pares(a)
        sae(p, [8,10], 'para lista [5 8 7 10] deveria retornar [8 10]')

        a = [8, 7, 13]
        p = pn.pares(a)
        sae(p, [8], 'para lista [8 7 13] deveria retornar [8]')

    def test_duplica(self):
        sae = self.assertEqual
        sain = self.assertIsNot

        a = []
        d = pn.duplica(a)
        sae(d, [], 'com lista [] deveria retornar []')
        sain(d, a, 'com lista [] deveria retornar nova lista []')

        a = [4]
        d = pn.duplica(a)
        sae(d, [4,4], 'com lista [4] deveria retornar [4, 4]')

        a = [4, 5]
        d = pn.duplica(a)
        sae(d, [4,4,5,5], 'com lista [4] deveria retornar [4, 4, 5, 5]')

    def test_possui_par(self):
        sat = self.assertTrue
        saf = self.assertFalse

        saf(pn.possui_par([]), 'lista [] não possui par')

        sat(pn.possui_par([4]), 'lista [4] possui par')

        sat(pn.possui_par([4,5,7]), 'lista [4, 5, 7] possui par')

        sat(pn.possui_par([5,7,10]), 'lista [5, 7, 10] possui par')

        sat(pn.possui_par([5,7,10,13,21]), 'lista [5, 7, 10, 13, 21] possui par')

    def test_primeira_posicao_de_numero(self):
        sae = self._baseAssertEqual
        ppn = pn.primeira_posicao_de_numero

        self.assertIsNone(ppn([], 6),
            'para lista [] deveria retornar None')

        self.assertIsNone(ppn([8], 6),
            'para lista [8] e número 6 deveria retornar None')

        sae(ppn([8], 8), 0,
            'para lista [8] e número 8 deveria retornar 0')

        sae(ppn([1, 4, 8], 8), 2,
            'para lista [1, 4, 8] e número 8 deveria retornar 2')

        sae(ppn([1, 4, 8, 2, 8], 8), 2,
            'para lista [1, 4, 8, 2, 8] e número 8 deveria retornar 2')

    def test_posicoes_de_numero(self):
        pdn = pn.posicoes_de_numero
        sae = self.assertEqual

        nums = []
        ps = pdn(nums, 5)
        sae(ps, [], 'para lista [] deveria retornar []')
        self.assertIsNot(ps, nums, 'para lista [] deveria retornar novo []')

        nums = [1, 2, 3, 4]
        ps = pdn(nums, 5)
        sae(ps, [], 'para lista [1, 2, 3, 4] e número 5 deveria retornar []')

        nums = [1, 2, 5]
        ps = pdn(nums, 5)
        sae(ps, [2], 'para lista [1 2 5] e número 5 deveria retornar [2]')

        nums = [1, 5, 2, 5]
        ps = pdn(nums, 5)
        sae(ps, [1,3], 'para lista [1 5 2 5] e número 5 deveria retornar [1 3]')

    def test_sem_repeticoes(self):
        sat = self.assertTrue
        saf = self.assertFalse
        sr = pn.sem_repeticoes

        sat(sr([]), 'para lista [] deveria retornar True')
        sat(sr([3]), 'para lista [3] deveria retornar True')
        sat(sr([2, 3, 9]), 'para lista [2, 3, 9] deveria retornar True')
        saf(sr([2, 2]), 'para lista [2, 2] deveria retornar False')
        saf(sr([1, 2, 2]), 'para lista [1, 2, 2] deveria retornar False')
        saf(sr([1, 4, 1, 7]),
            'para lista [1, 4, 1, 7] deveria retornar False')

    def test_remove_ocorrencias(self):
        sae = self.assertEqual
        sain = self.assertIsNot
        ro = pn.remove_ocorrencias

        a = []
        b = ro(a, 7)
        sae(b, [], 'para lista [] deveria retornar []')
        sain(a, b, 'para lista [] deveria retornar novo []')

        a = [7]
        b = ro(a, 7)
        sae(b, [], 'para lista [7] e número 7 deveria retornar []')

        a = [7, 3, 7, 9]
        b = ro(a, 7)
        sae(b, [3,9], 'para lista [7, 3, 7, 9] e número 7 deveria retornar [3, 9]')


    def test_substitui_ocorrencias(self):
        sae = self.assertEqual
        so = pn.substitui_ocorrencias

        a = []
        so(a, 7, 12)
        sae(a, [], 'para lista [] deveria retornar []')

        a = [7]
        so(a, 7, 4)
        sae(a, [4], 'para lista [7] subst. 7 por 4 deveria retornar [4]')

        a = [7, 3, 7, 9]
        so(a, 7, 4)
        sae(a, [4,3,4,9],
            'para lista [7, 3, 7, 9] subst. 7 por 4 deveria retornar [4, 3, 4, 9]')

        a = [7, 3, 7, 9]
        so(a, 1, 4)
        sae(a, [7,3,7,9],
            'para lista [7, 3, 7, 9] subst. 1 por 4 deveria retornar [7, 3, 7, 9]')

    def test_substitui_primeira_ocorrencia(self):
        sae = self.assertEqual
        spo = pn.substitui_primeira_ocorrencia

        a = []
        spo(a, 7, 12)
        sae(a, [], 'para lista [] deveria retornar []')

        a = [7]
        spo(a, 7, 4)
        sae(a, [4], 'para lista [7] subst. 7 por 4 deveria retornar [4]')

        a = [7, 3, 7, 9]
        spo(a, 7, 4)
        sae(a, [4,3,7,9],
            'para lista [7, 3, 7, 9] subst. 7 por 4 deveria retornar [4, 3, 7, 9]')

        a = [7, 3, 7, 9]
        spo(a, 1, 4)
        sae(a, [7,3,7,9],
            'para lista [7, 3, 7, 9] subst. 1 por 4 deveria retornar [7, 3, 7, 9]')

    def test_substitui_ultima_ocorrencia(self):
        sae = self.assertEqual
        suo = pn.substitui_ultima_ocorrencia

        a = []
        suo(a, 7, 12)
        sae(a, [], 'para lista [] deveria retornar []')

        a = [7]
        suo(a, 7, 4)
        sae(a, [4], 'para lista [7] subst. 7 por 4 deveria retornar [4]')

        a = [7, 3, 7, 9]
        suo(a, 7, 4)
        sae(a, [7,3,4,9],
            'para lista [7, 3, 7, 9] subst. 7 por 4 deveria retornar [7, 3, 4, 9]')

        a = [7, 3, 7, 9]
        suo(a, 1, 4)
        sae(a, [7,3,7,9],
            'para lista [7, 3, 7, 9] subst. 1 por 4 deveria retornar [7, 3, 7, 9]')

        a = [3, 7, 9, 7]
        suo(a, 7, 4)
        sae(a, [3,7,9,4],
            'para lista [3 7 9 7] subst. 7 por 4 deveria retornar [3 7 9 4]')

    def test_inverte(self):
        sae = self.assertEqual
        sain = self.assertIsNot

        a = []
        b = pn.inverte(a)
        sae(b, [], 'para lista [] deveria retornar []')
        sain(b, a, 'para lista [] deveria retornar nova lista []')

        a = [6]
        b = pn.inverte(a)
        sae(b, [6], 'para lista [6] deveria retornar [6]')
        sain(b, a, 'para lista [6] deveria retornar nova lista [6]')

        a = [6, 2]
        b = pn.inverte(a)
        sae(b, [2,6], 'para lista [6, 2] deveria retornar [2, 6]')
        sain(b, a, 'para lista [6, 2] deveria retornar nova lista [2, 6]')

        a = [6, 2, 3]
        b = pn.inverte(a)
        sae(b, [3,2,6], 'para lista [6, 2, 3] deveria retornar [2, 6, 3]')
        sain(b, a, 'para lista [6, 2, 3] deveria retornar nova lista [3, 2, 6]')

    def test_soma_pos_pares_pos_impares(self):
        sain = self.assertIsNot
        sae = self.assertEqual
        spi = pn.soma_pos_pares_pos_impares

        self.assertIsNone(spi([]),
                          'para lista [] deveria retornar None')

        self.assertIsNone(spi([7]),
                          'para lista [7] deveria retornar None')
        a = [8, 4]
        b = spi(a)
        sae(b, [8,4], 'para lista [8, 4] deveria retornar [8, 4]')
        sain(b, a, 'para lista [8, 4] deveria retornar nova lista [8, 4]')

        a = [3, 4, 2]
        b = spi(a)
        sae(b, [5,4], 'para lista [3 4 2] deveria retornar [5 4]')

        a = [3, 4, 2, 3]
        b = spi(a)
        sae(b, [5,7], 'para lista [3 4 2 3] deveria retornar [5 7]')

    def test_das_posicoes(self):
        sain = self.assertIsNot
        sae = self.assertEqual
        dp = pn.das_posicoes

        a = []
        ps = []
        b = dp(a, ps)
        sae(b, [], 'para lista [] deveria retornar []')
        sain(b, a, 'para lista [] deveria retornar novo []')
        sain(b, ps, 'para lista [] deveria retornar novo []')

        a = [8]
        ps = [0]
        b = dp(a, ps)
        sae(b, [8], 'para lista [8] e posicoes [0] deveria retornar [8]')
        sain(b, a, 'para lista [8] e pos [0] deveria retornar nova lista [8]')

        a = [8]
        ps = [0, 0]
        b = dp(a, ps)
        sae(b, [8,8], 'para lista [8] e pos [0, 0] deveria retornar [8, 8]')

        a = [8, 3, 1, 2]
        ps = [2, 0, 1]
        b = dp(a, ps)
        sae(b, [1,8,3], 
            'para lista [8, 3, 1, 2] e pos [2, 0, 1] deveria retornar [1, 8, 3]')

    def test_parte(self):
        sae = self.assertEqual

        a = [1, 2]
        b = pn.parte(a, qtd=4, pos=2)
        sae(b, [], 'parte([1, 2], qtd=4, pos=2]) deveria retornar []')

        a = [8, 3]
        b = pn.parte(a, qtd=1, pos=0)
        sae(b, [8], 'parte([8 ,3], qtd=1, pos=0]) deveria retornar [8]')

        a = [8, 3]
        b = pn.parte(a, qtd=3, pos=0)
        sae(b, [8,3], 'parte([8, 3], qtd=3, pos=0]) deveria retornar [8, 3]')

        a = [8, 3, 1, 7]
        b = pn.parte(a, qtd=2, pos=2)
        sae(b, [1,7], 'parte([8, 3, 1, 7], qtd=2, pos=2]) deveria retornar [1, 7]')

if __name__ == '__main__':
    unittest.main()
