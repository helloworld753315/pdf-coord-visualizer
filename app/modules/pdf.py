import fitz

class Pdf:
    def __init__(self, import_path):
        self.import_path = import_path

    def convert_image(self, page_number=0, dpi=300):
        doc = fitz.open(self.import_path)
        page = doc.load_page(page_number)
        
        # 解像度の設定
        zoom = dpi / 72  # PDFのデフォルトDPIは72
        matrix = fitz.Matrix(zoom, zoom)

        pix = page.get_pixmap(matrix=matrix)

        image_path = f'files/export/page_{page_number}.png'
        pix.save(image_path)
        
        doc.close()

        return image_path