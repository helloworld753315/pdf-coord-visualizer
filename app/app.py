from modules.pdf import Pdf

def main():
    pdf = Pdf(
        import_path="files/com_humanculture2023.pdf",
    )
    pdf.convert_image()

if __name__ == "__main__":
    main()