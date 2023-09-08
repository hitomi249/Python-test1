def create_html(fname: str, title: str):
    with open (fname, encoding="UTF-8", mode="w") as f:
        f.writelines("<!doctype html>\n")
        f.writelines("<html lang='ja'>\n")
        f.writelines("<head>\n")
        f.writelines("<meta charset='UTF-8'>\n")
        f.writelines(f"<title>{title}</title>\n")
        f.writelines("</head>\n")
        f.writelines("<body>\n")
        f.writelines("</body>\n")
        f.writelines("</html>\n")
    
for i in range(5):
    create_html(f"output/test{i}.html", "test")