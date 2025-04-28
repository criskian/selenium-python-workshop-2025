Feature: Search de mercadolibre
    Scenario: Producto válido iphone 13
        Given el usuario se encuentra en la pagina de inicio de mercadolibre
        When el usuario escribe el producto Iphone 13
        Then aparecen resultados del producto