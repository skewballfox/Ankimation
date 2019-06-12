def save_html(html, path):
    """save html to file
    uses 'rb' (write bytes) in order to avoid encoding issues"""
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    """
    open locally saved html as file
    uses 'rb' (read bytes) in order to avoid encoding issues"""
    with open(path, 'rb') as f:
        return f.read()