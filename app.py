import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import PyPDF2
import os
import pandas as pd
import ttkbootstrap as ttkb
from tkinter import messagebox
import threading
import tkinter.messagebox as msgbox

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def process_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    saved_files = []
    if file_paths:
        progress_bar["maximum"] = len(file_paths)
        for file_path in file_paths:
            text = extract_text_from_pdf(file_path)
            data = text.split('\n')
            df = pd.DataFrame(columns=['Periodo', 'Salario Nível', 'Referencia Adicional Noturno', 'Valor Adicional Noturno', 'HE 50%', 'HE 50% Ref', 'HE 100%', 'HE 100% Ref'])
            periodo, salario_nivel, ref_adicional_noturno, valor_adicional_noturno, he_50, he_50_ref, he_100, he_100_ref = None, None, None, None, None, None, None, None
            for line in data:
                if 'Período Folha:' in line:
                    if periodo:
                        df.loc[len(df.index)] = [
                            periodo, salario_nivel if salario_nivel else 0,
                            ref_adicional_noturno if ref_adicional_noturno else 0, valor_adicional_noturno if valor_adicional_noturno else 0,
                            he_50 if he_50 else 0, he_50_ref if he_50_ref else 0, he_100 if he_100 else 0, he_100_ref if he_100_ref else 0
                        ]
                        salario_nivel, ref_adicional_noturno, valor_adicional_noturno, he_50, he_50_ref, he_100, he_100_ref = None, None, None, None, None, None, None
                    periodo = line.split(':')[-1].strip()
                elif 'Salário Nível:' in line:
                    salario_nivel = float(line.split("Salário Nível:")[1].split()[0].replace('.', '').replace(',', '.'))
                elif '60- ADICIONAL NOTURNO' in line:
                    line_parts = line.split()
                    valor_adicional_noturno = float(line_parts[-1].replace('.', '').replace(',', '.'))
                    ref_adicional_noturno = float(line_parts[-2].replace('.', '').replace(',', '.'))
                elif '34- HORAS EXTRAS C/ 50%' in line:
                    line_parts = line.split()
                    he_50 = float(line_parts[-1].replace('.', '').replace(',', '.'))
                    he_50_ref = float(line_parts[-2].replace('.', '').replace(',', '.'))
                elif '36- HORAS EXTRAS C/ 100%' in line:
                    line_parts = line.split()
                    he_100 = float(line_parts[-1].replace('.', '').replace(',', '.'))
                    he_100_ref = float(line_parts[-2].replace('.', '').replace(',', '.'))
            if periodo:
                df.loc[len(df.index)] = [
                    periodo, salario_nivel if salario_nivel else 0,
                    ref_adicional_noturno if ref_adicional_noturno else 0, valor_adicional_noturno if valor_adicional_noturno else 0,
                    he_50 if he_50 else 0, he_50_ref if he_50_ref else 0, he_100 if he_100 else 0, he_100_ref if he_100_ref else 0
                ]
            df = df[~df['Periodo'].str.contains('TodosPág')]
            csv_filename = file_path.rsplit('.', 1)[0] + '.csv'
            df.to_csv(csv_filename, index=False)
            saved_files.append(csv_filename)
            progress_bar["value"] += 1
        progress_bar["value"] = 0  # Reset progress bar after completion
        messagebox.showinfo("Pronto!", "Processamento concluído. Arquivos salvos em: \n" + '\n'.join(saved_files))

root = tk.Tk()
style = ttkb.Style(theme='cosmo')

root.title("Fast data")
root.iconbitmap('C:/Users/Edson/Downloads/flesh.ico')

root.geometry('300x100')

open_button = ttk.Button(root, text="Importar todos PDFs", command=process_files)
open_button.pack(pady=10)

progress_bar = ttk.Progressbar(root, length=200)
progress_bar.pack(pady=10)

root.mainloop()
