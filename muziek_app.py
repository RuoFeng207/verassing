import pygame
import sys
import time
pygame.init()
pygame.mixer.init()




def teken_knop(scherm, tekst, x, y, breedte, hoogte, kleur, kleur_tekst, uitlijn):
    # Knop tekenen
    pygame.draw.rect(scherm, kleur, (x, y, breedte, hoogte), width=0)
    # Uitleg
    pygame.draw.rect(scherm, uitlijn, (x, y, breedte, hoogte), width=2)
    
    # Lettertype
    font = pygame.font.SysFont(None, 40)
    
    # Maak de tekst
    tekst_opmaak = font.render(tekst, True, kleur_tekst)
    
    # Bereken de positie van de tekst
    tekst_rect = tekst_opmaak.get_rect(center=(x + breedte // 2, y + hoogte // 2))
    
    # Teken de tekst op de knop
    scherm.blit(tekst_opmaak, tekst_rect)
    
    # Retourneer de rechthoek van de knop voor botsingsdetectie
    return pygame.Rect(x, y, breedte, hoogte)


def tekst(scherm, tekst, x, y, kleur_tekst):
    # lettertype
    font = pygame.font.SysFont(None, 60)
    
    # Maak de tekst
    tekst_opmaak = font.render(tekst, True, kleur_tekst)
    
    # Bereken de positie van de tekst
    tekst_rect = tekst_opmaak.get_rect(center=(x, y))
    
    # Teken de tekst op het scherm
    scherm.blit(tekst_opmaak, tekst_rect)


# kleur
rood = 255, 0, 0
lichtrood = 255, 102, 102
wit = 255, 255, 255
zwart = 0, 0, 0
# Display
scherm_hoogte = 600
scherm_breete = 600
scherm = pygame.display.set_mode((scherm_breete, scherm_hoogte))
pygame.display.set_caption("Verjaardag")

# achtergrond laden
achtergrond = pygame.image.load("party_background.jpg")
achtergrond = pygame.transform.scale(achtergrond, (600, 600))
# muziek
sound1 = pygame.mixer.Sound("er_is_er_een_jarig.mp3")
sound2 = pygame.mixer.Sound("gefeliciteerd.mp3")
sound3 = pygame.mixer.Sound("lang_zal_hij_leven.mp3")
# main loop en eventhandler
while True:
    #cur_pos
    cur = pygame.mouse.get_pos()
    for event in pygame.event.get():     
        # Controleer of de muis op de knop is geklikt         
        if event.type==pygame.MOUSEBUTTONDOWN: 
            if knop1.collidepoint(cur):   #muziek
                sound1.play()
                time.sleep(26)
                sound2.play()
                time.sleep(32)
                sound3.play()
                time.sleep(1)
            if knop2.collidepoint(cur): #afsluiten
                print("Bedankt voor het luisteren!")
                quit()

        if event.type ==pygame.MOUSEBUTTONUP:
            if knop1.collidepoint(cur):  
                print("Knop play is losgelaten!")
            if knop2.collidepoint(cur): 
                print("Knop afsluiten is losgelaten!")
                    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teken achtergrond
    scherm.blit(achtergrond, (0, 0))
    tekst(scherm, "gefeliciteerd", scherm_breete // 2, 330, zwart) 
    # Teken de knoppen

         
        #knop1
    if (scherm_breete - 150) // 2 < cur[0] < (scherm_breete - 150) // 2 + 150 and 400 < cur[1] < 400 + 50:

        knop1=teken_knop(scherm, "Play", (scherm_breete - 150) // 2, 400, 150, 50, lichtrood, wit,zwart)
    else:
        knop1=teken_knop(scherm, "Play", (scherm_breete - 150) // 2, 400, 150, 50, rood, wit,zwart)

        #knop 2
    if (scherm_breete - 150) // 2 < cur[0] < (scherm_breete - 150) // 2 + 150 and 470 < cur[1] < 470 + 50:
        knop2=teken_knop(scherm, "Afsluiten", (scherm_breete - 150) // 2, 470, 150, 50, lichtrood, wit,zwart)
    
    else:
        knop2=teken_knop(scherm, "Afsluiten", (scherm_breete - 150) // 2, 470, 150, 50, rood, wit,zwart)




    pygame.display.update()
