import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Imagem e Upscale para 4K")
        self.root.geometry("400x250")
        self.root.iconbitmap(r"D:/!Developer/py_ImagerConverter/imagem.ico")

        self.btn_import = tk.Button(root, text="Importar Imagem", command=self.importar_imagem)
        self.btn_import.pack(pady=5)

        self.format_var = tk.StringVar(value="PNG")
        self.format_label = tk.Label(root, text="Escolha o formato de conversão: (Converter em)")
        self.format_label.pack()
        
        self.format_options = ["PNG", "JPEG", "BMP", "TIFF", "WEBP", "ICO"]
        self.format_menu = tk.OptionMenu(root, self.format_var, *self.format_options)
        self.format_menu.pack(pady=5)
        
        self.btn_convert = tk.Button(root, text="Converter", command=self.converter_imagem)
        self.btn_convert.pack(pady=5)
        
        self.btn_upscale = tk.Button(root, text="Aumentar para 4K", command=self.upscale_4k)
        self.btn_upscale.pack(pady=5)

        self.arquivo = ""

    def importar_imagem(self):
        arquivo = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff;*.webp;*.gif")])
        if arquivo:
            self.arquivo = arquivo
            messagebox.showinfo("Sucesso", f"Imagem importada: {os.path.basename(arquivo)}")
    
    def converter_imagem(self):
        if not self.arquivo:
            messagebox.showwarning("Atenção", "Nenhuma imagem selecionada!")
            return
        
        img = Image.open(self.arquivo)
        formato = self.format_var.get().lower()
        novo_arquivo = os.path.splitext(self.arquivo)[0] + f".{formato}"
        img.save(novo_arquivo, formato.upper())
        messagebox.showinfo("Sucesso", f"Imagem convertida para {formato.upper()}: {novo_arquivo}")
    
    def upscale_4k(self):
        if not self.arquivo:
            messagebox.showwarning("Atenção", "Nenhuma imagem selecionada!")
            return
        
        img = Image.open(self.arquivo)
        img_4k = img.resize((3840, 2160), Image.LANCZOS)
        upscale_path = os.path.splitext(self.arquivo)[0] + "_4K.png"
        img_4k.save(upscale_path, "PNG")
        messagebox.showinfo("Sucesso", f"Imagem aumentada para 4K: {upscale_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
