# não tem necessidade de importar o TestCase do Django, esse é um teste separado
from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 1,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)
    
    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        # Current Page = 1 - Middle page = 2
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 1,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)
        
        # Current Page = 2 - Middle page = 2
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 2,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

        # Current Page = 3 - Middle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 3,
        )['pagination']
        self.assertEqual([2,3,4,5], pagination)

        # Current Page = 4 - Middle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 4,
        )['pagination']
        self.assertEqual([3,4,5,6], pagination)


    def test_make_sure_middle_ranges_are_correct(self):
        # Current Page = 10 - Middle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        # Current Page = 12 - Middle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 12,
        )['pagination']
        self.assertEqual([11,12,13,14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        # Current Page = 18 - Middle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 18,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

        # Current Page = 19 - Middle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 19,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)
        
        # Current Page = 20 - Middle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 20,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

        # Current Page = 21 - Middle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qtd_de_paginas = 4, # quantidade de paginas mostradas no pé da pagina: ex 1 [2] 3 4   |   2 [3] 4 5
            current_page = 21,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

