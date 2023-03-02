from swish_qr import generate_swish_code

# save to svg
# svg_bytes = generate_swish_code(
#     "0123456789",
#     100.99,
#     "Test message!",
#     format="svg",
# )
# with open("sample.svg", "wb") as f:
#     f.write(svg_bytes)

# save to png
png_bytes = generate_swish_code(
    "0123456789",
    1,
    "",
    format="png",
)
with open("sample1.png", "wb") as f:
    f.write(png_bytes)

png_bytes = generate_swish_code(
    "0123456789",
    150000,
    "åäöåäöåäöåäöåäöåäöåäöåäöåäöåäöåäöåäöåäöåäöåäöåäööö",
    format="png",
)
with open("sample2.png", "wb") as f:
    f.write(png_bytes)
