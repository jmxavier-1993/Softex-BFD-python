import qrcode

# 1. Cole o URL completo do seu perfil do LinkedIn aqui
url_do_linkedin = "https://www.linkedin.com/in/julianamarinhoxavier/"

# 2. Configurar os parâmetros do QR code
qr = qrcode.QRCode(
    version=1,  # Controla o tamanho (1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Nível de correção de erro (L, M, Q, H)
    box_size=10, # Tamanho de cada "quadrado" do QR code
    border=4,    # Tamanho da borda branca ao redor
)

# 3. Adicionar os dados (o seu link)
qr.add_data(url_do_linkedin)
qr.make(fit=True)

# 4. Criar a imagem (você pode até definir as cores)
img = qr.make_image(fill_color="black", back_color="white")

# 5. Salvar a imagem
nome_do_arquivo = "meu_linkedin_qr_avancado.png"
img.save(nome_do_arquivo)

print(f"QR code avançado salvo com sucesso como '{nome_do_arquivo}'!")