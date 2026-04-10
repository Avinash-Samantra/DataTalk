import pymupdf

doc = pymupdf.open("C:/Users/avina/Downloads/Subject_Syllabus_030705506.pdf")
page = doc.load_page(0)
pix = page.get_pixmap()
# pix.save(f"page-{page.number}.png")
help(pymupdf.open)