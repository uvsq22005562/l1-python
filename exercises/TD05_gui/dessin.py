import tkinter as tk

racine = tk.Tk()

bouton1 = tk.Button(racine, text="choisir une couleur",
                    font=("helvetica", "10"))
bouton2 = tk.Button(racine, text="cercle", font=("helvetica", "10"))
bouton3 = tk.Button(racine, text="carré", font=("helvetica", "10"))
bouton4 = tk.Button(racine, text="croix", font=("helvetica", "10"))

canvas = tk.Canvas(racine, width="400", height="400", bg="black")


canvas.grid(column=1, row=1, rowspan=3)
bouton1.grid(column=1, row=0)
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)
bouton4.grid(column=0, row=3)


racine.mainloop()
