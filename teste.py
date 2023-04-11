import tkinter as tk
from tkinter import filedialog
import pandas as pd
import re
import os
import pandas as pd
from google.cloud import storage

filepath1 = ''
nome_bucket = ''

def select_file():
    global filepath1
    
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    print("Arquivo selecionado: ", file_path)
    filepath1 = file_path
    
    root.destroy()

def select_bucket():
    global nome_bucket
    
    root = tk.Tk()
    root.withdraw()
    nome_bucket = tk.simpledialog.askstring("Informe o nome do bucket", "Digite o nome do bucket")

    
    print("Nome do bucket: ", nome_bucket)

    
    root.destroy()



root = tk.Tk()


root.title("TELA DE USO")
root.geometry("400x150")


select_file_button = tk.Button(root, text="Selecionar arquivo", command=select_file)
select_file_button.pack(pady=10)


select_bucket_button = tk.Button(root, text="Informar nome do bucket", command=select_bucket)
select_bucket_button.pack(pady=10)


enviar_button = tk.Button(root, text="Enviar", command=root.destroy)
enviar_button.pack(pady=10)

root.mainloop()


print("Arquivo selecionado: ", filepath1)
print("Nome do bucket: ", nome_bucket)


dados = pd.read_csv(filepath1)


print(dados)





os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  'SEU CAMINHO PARA O JSON GERADO DENTRO DO GOOGLE APPLICATION'

storage_client = storage.Client()

# %%

bucket = storage_client.get_bucket('gcp-storage-assai-raw')

# %%
def upload_to_bucket(blob_name, file_path, bucket_name):
    
    bucket = storage_client.get_bucket(bucket_name)
    
    blob = bucket.blob(blob_name)
   
    blob.upload_from_filename(file_path)
    
    return blob


caminho_arquivo = filepath1
nome_arquivo = re.search(r'[^\\/:*?"<>|\r\n]+$', caminho_arquivo).group()
# %%
upload_to_bucket(nome_arquivo,filepath1,nome_bucket)
