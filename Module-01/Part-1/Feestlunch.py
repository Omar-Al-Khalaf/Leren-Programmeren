# ==== Start ==== #
antaalcroissants = 17
croissantprijs = 0.39
stokbrodenprijs = 2.78
kortingsbonnen = 0.50
antaalkortingsbonnen = 3
antaalstokbroden = 2
Total = antaalcroissants * croissantprijs + antaalstokbroden * stokbrodenprijs - kortingsbonnen * antaalkortingsbonnen

# ==== Coding ==== #

print(f'You buy {antaalcroissants} croissants and {antaalstokbroden} stokbroden and you have {antaalkortingsbonnen} worth of kortingsbonnen you Total is :', Total)
