import base64


def generate_corners(size):
    return (
        '<path fill="none" stroke="url(#gradient)" stroke-linejoin="round" stroke-width="1.0" '
        'd="M 4.5 10.5 v -0.875 a 5.125 5.125 0 0 1 5.125 -5.125 h 0.875 v 6 Z"/>'
        '<path fill="url(#gradient)" d="M 6 9.125 a 3 3 0 0 1 3 -3 v 3 Z"/>'
        '<path fill="none" stroke="url(#gradient)" stroke-linejoin="round" stroke-width="1.0" '
        f'd="M 4.5 {size - 3}.5 v 0.875 a 5.125 5.125 0 0 0 5.125 5.125 h 0.875 v -6 Z"/>'
        f'<path fill="url(#gradient)" d="M 6 {size - 2}.875 a 3 3 0 0 0 3 3 v -3 Z"/>'
        '<path fill="none" stroke="url(#gradient)" stroke-linejoin="round" stroke-width="1.0" '
        f'd="M {size + 3}.5 10.5 v -0.875 a 5.125 5.125 0 0 0 -5.125 -5.125 h -0.875 v 6 Z"/>'
        f'<path fill="url(#gradient)" d="M {size + 2} 9.125 a 3 3 0 0 0 -3 -3 v 3 Z"/>'
    )


def generate_logo(size, margin):
    return (
        '<use x="490" y="490" '
        f'transform="scale({(0.00083643122676579925 * (size + 8))})" xlink:href="#w"/>'
    )


def logo_image():
    with open("swish-logo.png", "rb") as f:
        data = f.read()
    b64data = base64.encodebytes(data).decode("utf8")
    return (
        '<image id="w" width="210" height="210" preserveAspectRatio="none" '
        # f'xlink:href="data:image/png;base64,{b64data}" x="{size/2+.5}" y="{size/2+.5}" />'
        f'xlink:href="data:image/png;base64,{b64data}" />'
    )


def generate_svg_template(viewbox, dimensions, background, circles, corners, logo):
    return f"""
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
    viewBox="{viewbox}"{dimensions}><defs>
    {logo_image()}
    <linearGradient id="gradient" x1="0%" x2="100%" y1="100%" y2="0%"
    gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#B43092"/>
        <stop offset="100%" stop-color="#EF4123"/>
    </linearGradient>
    </defs>{background}<g fill="url(#gradient)">{circles}</g>{corners}{logo}</svg>"""
