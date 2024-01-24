
# Conversor de imagem para preto e branco

# Fazer instalação do pacote Pillow: pip install pillow

# Importando a biblioteca Pillow
from PIL import Image

# Informe o nome ou o caminho da imagem
imagem_original = Image.open("foto.png")

# Processo de conversão
imagem_preto_branco = imagem_original.convert("L")
imagem_preto_branco.save("foto_preto_e_branco.png")

# Apresentando imagem ja convertida para preto e branco
imagem_preto_branco.show()
