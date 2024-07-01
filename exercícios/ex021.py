import pygame

# Inicializa todos os módulos do Pygame
pygame.init()

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Carrega o arquivo de música
try:
    pygame.mixer.music.load('ex021.mp3')
    print("Arquivo de música carregado com sucesso.")
except pygame.error as e:
    print(f"Erro ao carregar o arquivo de música: {e}")

# Toca a música
try:
    pygame.mixer.music.play()
    print("Reprodução de música iniciada.")
except pygame.error as e:
    print(f"Erro ao tentar reproduzir a música: {e}")

# Mantém o programa em execução até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
