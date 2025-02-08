# Import delle librerie necessarie
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class crea_report_da_csv:
    
    def __init__(self, master):
        # Inizializzazione dell'interfaccia grafica e delle componenti principali
        self.master = master
        self.master.title("Creazione Report da CSV")  # Imposta il titolo della finestra
        self.master.geometry("800x800")  # Imposta le dimensioni della finestra

        # Pulsante per aprire il file CSV
        open_button = ttk.Button(master, text="Apri i files CSV", command=self.scegli_file_csv)
        open_button.pack(pady=20)  # Aggiunge il pulsante alla finestra con un margine di spaziatura

        # Treeview per visualizzare i dati del CSV
        self.treeview = ttk.Treeview(master)
        self.treeview["columns"] = ("DATA", "POTENZA", "MER", "TEMPERATURA", "CAMPO_RICEVUTO")
        self.treeview["show"] = "headings"  # Rimuove la colonna degli indici
        self.treeview.heading("#0", text="")  # Rimuove l'intestazione della colonna degli indici

        # Imposta le intestazioni delle colonne e la larghezza
        for col in self.treeview["columns"]:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, anchor="center", width=100)
        
        self.treeview.pack(padx=20, pady=20)  # Aggiunge il Treeview alla finestra con spaziatura

        # Pulsante per visualizzare il grafico
        plot_button = ttk.Button(master, text="Seleziona i dati che vuoi visualizzare", command=self.visualizza_grafico)
        plot_button.pack(pady=10)  # Aggiunge il pulsante alla finestra con spaziatura

    def scegli_file_csv(self):
        # Apre una finestra di dialogo per selezionare uno o più file CSV
        url_files = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])

        if url_files:
            try:
                # Inizializza un nuovo DataFrame vuoto
                self.df = pd.DataFrame()

                for url_file in url_files:
                    # Legge i dati dal file CSV usando Pandas
                    df = pd.read_csv(url_file, delimiter=";", parse_dates=["DATA"], dayfirst=True, infer_datetime_format=True)

                    # Aggiunge i dati al DataFrame principale
                    self.df = pd.concat([self.df, df], ignore_index=True)

                # Ordina il DataFrame in base alla colonna DATA
                self.df.sort_values(by="DATA", inplace=True)

                # Pulisce il Treeview
                for item in self.treeview.get_children():
                    self.treeview.delete(item)

                # Aggiunge i dati al Treeview
                for i, row in self.df.iterrows():
                    self.treeview.insert("", i, values=tuple(row))

            except Exception as e:
                # Gestisce eventuali errori mostrando una finestra di dialogo
                messagebox.showerror("Errore", f"Errore durante la lettura dei file CSV: {str(e)}")
                print(e)


    def visualizza_grafico(self):
        # Apre una finestra di dialogo per selezionare le colonne da visualizzare nel grafico
        selected_columns = self.seleziona_quali_dati_confrontare()

        if selected_columns:
            # Crea il grafico utilizzando solo le colonne selezionate
            fig, ax = plt.subplots(figsize=(8, 6))
            for col in selected_columns:
                ax.plot(self.df["DATA"], self.df[col], marker='o', label=col)

            ax.set_title("REPORT")  # Imposta il titolo del grafico
            ax.set_xlabel("DATA")  # Imposta l'etichetta dell'asse x

            # Imposta i valori della legenda sull'asse x inclinati di 45 gradi
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

            ax.set_ylabel("Valore")  # Imposta l'etichetta dell'asse y
            ax.legend()  # Aggiunge la legenda al grafico

            # Mostra il grafico in una finestra di dialogo
            plot_dialog = tk.Toplevel(self.master)
            plot_dialog.title("Grafico")
            canvas = FigureCanvasTkAgg(fig, master=plot_dialog)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            

    def seleziona_quali_dati_confrontare(self):
    # Crea una finestra di dialogo per selezionare le colonne
        dialog = tk.Toplevel(self.master)
        dialog.title("Seleziona i dati che vuoi visualizzare nel grafico")

            # Lista di controllo per selezionare le colonne
        selected_columns = []
        listbox = tk.Listbox(dialog, selectmode=tk.MULTIPLE)
            
        for col in self.df.columns:
                # Escludi la colonna "DATA" dalla lista selezionabile
                if col != "DATA":
                    listbox.insert(tk.END, col)

        listbox.pack(padx=20, pady=20)

            # Pulsante per confermare la selezione
        confirm_button = ttk.Button(dialog, text="Conferma", command=lambda: self.conferma_selezione(dialog, listbox, selected_columns))
        confirm_button.pack(pady=10)

        dialog.wait_window(dialog)
        return selected_columns

    def conferma_selezione(self, dialog, listbox, selected_columns):
        # Ottiene gli elementi selezionati nella lista
        selected_indices = listbox.curselection()
        for index in selected_indices:
            selected_columns.append(listbox.get(index))

        # Chiude la finestra di dialogo
        dialog.destroy()

# Punto di ingresso dell'applicazione
if __name__ == '__main__':
    root = tk.Tk()
    app = crea_report_da_csv(root)
    root.mainloop()
