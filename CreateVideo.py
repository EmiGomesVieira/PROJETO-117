import os
import cv2

# Defina o caminho para a pasta de imagens
path = "Images"

# Crie uma lista para armazenar os nomes dos arquivos de imagem
images = []

# Verifique cada arquivo na pasta
for file in os.listdir(path):
    # Separe o nome do arquivo e a extensão
    name, ext = os.path.splitext(file)  # Corrigido aqui
    # Verifique se a extensão do arquivo corresponde à extensão da imagem (por exemplo, .jpg, .jpeg, .png)
    if ext.lower() in ['.jpg', '.jpeg', '.png']:
        # Crie o nome completo do arquivo
        file_name = os.path.join(path, file)
        print(file_name)  # Certifique-se de que os nomes dos arquivos sejam formados corretamente
        # Adicione o arquivo à lista de imagens
        images.append(file_name)

# Contador de imagens
count = len(images)

# Verifique se há imagens na lista
if count == 0:
    print("Nenhuma imagem encontrada na pasta.")
else:
    # Leia a primeira imagem para capturar suas dimensões
    frame = cv2.imread(images[0])
    height, width, channels = frame.shape
    size = (width, height)
    print(size)  # Verifique o resultado das dimensões

    # Crie o objeto VideoWriter
    out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

    # Adicione as imagens ao VideoWriter
    for i in range(0, count):
        frame = cv2.imread(images[i])
        out.write(frame)

    # Libere o objeto VideoWriter
    out.release()

    print("Concluído")

