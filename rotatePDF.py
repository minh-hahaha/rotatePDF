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
            print(page) # debug
        else:
            pageObject = pdfReader.pages[page]
            pdfWriter.add_page(pageObject)
            print(page) # debug
            
    # new file to save
    newFile = open(fileAddress, 'wb')
    pdfWriter.write(newFile)
    pdfFileObj.close()
    newFile.close()
        
    
## User Inputs
fileAddress = input("Enter File Address:  ")
rotateAll = input("Rotate all? (y/n) : ")
if rotateAll.lower() == "y":
    rotation = input("Rotation Angle (90-180-270) : ")
    PDFRotateAll(fileAddress,rotation)

else:
    multiple = input("Multiple Pages to Rotate? (y/n) : ")

    ## Are there  multiple pages?
    if (multiple.lower() == "y"):
        rotatePageList = []
        numPages = input("How many pages? : ")
        pages = int(numPages)
    
        for page in range(pages):
            pageInput = input("Page #" + str(page+1) + " : ")
            rotatePageList.append((int(pageInput)-1))
        
        rotation = input("Rotation Angle (90-180-270) : ")
    
        PDFRotateMultiple(fileAddress, rotation, rotatePageList)
    
    elif(multiple.lower() == "n"): 
        rotatePage = input ("Rotate Page : ")
        rotation = input("Rotation Angle (90-180-270) : ")
        PDFRotate(fileAddress, rotatePage, rotation)
  


