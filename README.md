# 🧠 Reconhecimento Facial com OpenCV

Este projeto realiza **detecção de rostos e olhos em tempo real** utilizando a **biblioteca OpenCV** e os **classificadores Haar Cascade**, que são modelos pré-treinados de reconhecimento de padrões visuais.  
A captura é feita pela **webcam**, e o sistema desenha retângulos azuis ao redor dos rostos e verdes ao redor dos olhos detectados.

---

## 🧩 Funcionalidades

- 🧍‍♂️ Detecção automática de rostos em tempo real  
- 👁️ Identificação de olhos dentro de cada rosto  
- 📸 Captura direta pela webcam  
- 🔁 Espelhamento da imagem (efeito de espelho)  
- 🖼️ Exibição ao vivo com marcações visuais  
- ⎋ Encerramento fácil com a tecla **ESC**

---

## 💡 Vantagens do código

✅ **Simples e eficiente:** utiliza poucos recursos e funciona em praticamente qualquer computador.  
✅ **Detecção em tempo real:** a câmera processa as imagens instantaneamente.  
✅ **Alta compatibilidade:** o OpenCV é multiplataforma (Windows, Linux e macOS).  
✅ **Extensível:** o código pode ser adaptado para:
- sistemas de segurança com câmera;  
- controle de acesso automatizado;  
- monitoramento de atenção (ex: em motoristas ou alunos);  
- projetos de visão computacional educacionais;  
- sistemas que ajustam a interface conforme a presença de usuários.

---

## 🧰 Tecnologias utilizadas

- **Python 3**  
- **OpenCV (cv2)**  
- **Classificadores Haar Cascade**
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_eye.xml`

---

## 🖥️ Requisitos

Antes de rodar o projeto, verifique se você possui:

- Python instalado (versão 3.7 ou superior)  
- Webcam conectada e funcional  
- Conexão com a internet para baixar bibliotecas  

---

## ⚙️ Instalação da biblioteca OpenCV

Abra o **Prompt de Comando (cmd)** ou **Terminal** e execute:

```bash
pip install opencv-python
