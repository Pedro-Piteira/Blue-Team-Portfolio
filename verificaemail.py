import customtkinter as ctk
ctk.set_appearance_mode("Dark")
def confirm(e):
    if("@"in e and "." in e):
        return True
    else:
        return False
def atualizar_label(a,v):
    em = a.get()
    v.configure(text="Válido" if confirm(em)  else "Inválido")
app=ctk.CTk()
app.geometry("800x600")
email=ctk.CTkEntry(app,placeholder_text="Insira o seu email")
email.pack(pady=10)
ver=ctk.CTkLabel(app,text="")
confirmar=ctk.CTkButton(app,text="Confirmar email",width=10,height=10,command=lambda :atualizar_label(email,ver))
confirmar.pack(pady=10)
ver.pack(pady=10)



app.mainloop()