Feature: Login de Intu
    Scenario: Credenciales incorrectas Intu
        Given el usuario se encuentra en la pagina de login de intu
        When el usuario escribe credenciales erroneas
        Then aparece un mensaje de error