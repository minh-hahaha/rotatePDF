import tkinter as tk
from tkinter import filedialog, ttk



def on_select(event):
    selected_item = drop_var.get()

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
    if file_path:
        pdf_file_path_entry.delete(0, tk.END)
        pdf_file_path_entry.insert(tk.END, file_path)

def execute_custom_script():
    pdf_file_path = pdf_file_path_entry.get()
    rotation = drop_var_rotation.get()
    rotatePage = text_entry5.get()
    rotatePageListStr = text_entry3.get().split(',')
    
    
    try:
        import PyPDF2
        def PDFRotateAll(fileAddress,rotation):
            # creating a pdf File object of original pdf
            pdfFileObj = open(fileAddress, 'rb')
            # creating a pdf Reader object
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            # creating a pdf writer object for new pdf
            pdfWriter = PyPDF2.PdfWriter()
    
            for page in range(len(pdfReader.pages)):
                pageObject = pdfReader.pages[page]
                pageObject.rotate(int(rotation))
                pdfWriter.add_page(pageObject)
    
            # new file to save
            newFile = open(fileAddress, 'wb')
            pdfWriter.write(newFile)
            pdfFileObj.close()
            newFile.close()
    

        def PDFRotate(fileAddress, rotatePage, rotation):
            # creating a pdf File object of original pdf
            pdfFileObj = open(fileAddress, 'rb')
            # creating a pdf Reader object
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            # creating a pdf writer object for new pdf
            pdfWriter = PyPDF2.PdfWriter()
    
    
            for page in range(len(pdfReader.pages)):
                pageNumber = int(int(rotatePage) - 1) # page number in binary
                if (page == pageNumber): 
                    # creating a page object
                    pageObject = pdfReader.pages[pageNumber]
                    # rotate page object
                    pageObject.rotate(int(rotation))
                    pdfWriter.add_page(pageObject)
                else:
                    pageObject = pdfReader.pages[page]
                    pdfWriter.add_page(pageObject)

            # new file to save
            newFile = open(fileAddress, 'wb')
            pdfWriter.write(newFile)
            pdfFileObj.close()
            newFile.close()

        def PDFRotateMultiple(fileAddress, rotation, pageList):
            # creating a pdf File object of original pdf
            pdfFileObj = open(fileAddress, 'rb')
            # creating a pdf Reader object
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            # creating a pdf writer object for new pdf
            pdfWriter = PyPDF2.PdfWriter()
    
            # go through every page and add to pdfWriter while changing pages that need rotation
            for page in range(len(pdfReader.pages)):
                if page in pageList: 
                    pageObject = pdfReader.pages[page]
                    pageObject.rotate(int(rotation))
                    pdfWriter.add_page(pageObject)
                else:
                    pageObject = pdfReader.pages[page]
                    pdfWriter.add_page(pageObject)
            
            # new file to save
            newFile = open(fileAddress, 'wb')
            pdfWriter.write(newFile)
            pdfFileObj.close()
            newFile.close()
        
    
        ## User Inputs
        fileAddress = pdf_file_path        
        if drop_var.get() == options[0]:
            PDFRotateAll(fileAddress,rotation)
        elif drop_var.get() == options[1]:
            rotatePageList = []
            for string in rotatePageListStr:
                rotatePageList.append(int(string)-1)
            PDFRotateMultiple(fileAddress, rotation, rotatePageList)
        elif drop_var.get() == options[2]:
            PDFRotate(fileAddress, rotatePage, rotation)
  
  
    except Exception as e:
        print(f"Error: {e}")

# Create the main application window
root = tk.Tk()
root.title("PDF Rotater")

window_width = 300
window_height = 440
root.geometry(f"{window_width}x{window_height}")


# Caption for PDF file path
pdf_caption = tk.Label(root, text="Select PDF File:")
pdf_caption.pack()

# PDF file path entry widget
pdf_file_path_entry = tk.Entry(root, width=30)
pdf_file_path_entry.pack()

# Button to select PDF file
select_pdf_button = tk.Button(root, text="Browse", command=select_pdf_file)
select_pdf_button.pack(pady=5)

captionLine = tk.Label(root, text="___________________________________")
captionLine.pack()


# Type Drop Down
options = ["All Pages", "Multiple Pages", "One Page"]
# Combobox variable to store the selected item
drop_var = tk.StringVar()
# Create the Combobox with the variable and options
dropdown_menu = ttk.Combobox(root, textvariable=drop_var, values=options)
dropdown_menu.pack(pady=10)
# Bind the event to handle selection change
dropdown_menu.bind("<<ComboboxSelected>>", on_select)


caption5 = tk.Label(root, text=" One Page - Page Number")
caption5.pack()
text_entry5 = tk.Entry(root, width=20)
text_entry5.pack(pady=5)

caption3 = tk.Label(root, text="Multiple Pages number(i.e. 1,5,99)")
caption3.pack()
text_entry3 = tk.Entry(root, width=20)
text_entry3.pack(pady=5)


caption4 = tk.Label(root, text="Rotation (90-180-270)")
caption4.pack()


# Rotation dropdown
rotationOptions = ["90", "180", "270"]
# Combobox variable to store the selected item
drop_var_rotation = tk.StringVar()
# Create the Combobox with the variable and options
dropdown_rotation = ttk.Combobox(root, textvariable=drop_var_rotation, values=rotationOptions)
dropdown_rotation.pack(pady=10)
# Bind the event to handle selection change
dropdown_rotation.bind("<<ComboboxSelected>>", on_select)

# Button to execute the custom Python script
execute_button = tk.Button(root, text="Execute Custom Script", command=execute_custom_script)
execute_button.pack(pady=10)




root.mainloop()
