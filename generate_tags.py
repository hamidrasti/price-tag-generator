import os
import textwrap

import pandas as pd
from PIL import Image, ImageDraw, ImageFont, features

import settings

raqm_is_available = features.check("raqm")

print(f"raqm is {'available.' if raqm_is_available else 'not available!'}")

w, h, m = (
    settings.WIDTH,
    settings.HEIGHT,
    settings.MARGIN,
)
font_path = f"{settings.ASSETS_DIR}/fonts/title.ttf"
price_font_path = f"{settings.ASSETS_DIR}/fonts/price.ttf"

logo_img = Image.open("logo.png")

df = pd.read_excel(f"{settings.ASSETS_DIR}/input.xlsx", sheet_name="Sheet1")

for index, row in df.iterrows():
    title = row["Title"]
    price = f"{row['Price']:,}"
    price_coupon = f"{row['CouponPrice']:,}"

    price_label = "قیمت:"
    price_coupon_label = "قیمت با بن:"

    price_font = ImageFont.truetype(price_font_path, size=36, encoding="unic")
    price_label_font = ImageFont.truetype(price_font_path, size=24, encoding="unic")
    title_font = ImageFont.truetype(font_path, size=44, encoding="unic")

    back_img = Image.new("RGB", (w, h), color="white")
    back_img.paste(logo_img, (w - w // 4 + m, 4 * m))

    img_draw = ImageDraw.Draw(back_img)
    img_draw.rectangle(
        [(w // 4 + m, 2 * m), (w - w // 4 - m, h - 2 * m)],
        fill="#d0cece",
        outline="#d0cece",
    )
    img_draw.rectangle(
        [(2 * m, 2 * m), (w // 6 - m, h // 2 - m)], fill="black", outline="black"
    )
    img_draw.rectangle(
        [(2 * m, h // 2 + m), (w // 6 - m, h - 2 * m)], fill="black", outline="black"
    )

    # print(font.getbbox(title))
    # title_x, title_y, text_width, text_height = img_draw.textbbox((w // 4 + m, 2 * m), title, font=font)
    # title_x = (w - text_width) // 2
    # title_y = (h - text_height) // 2

    title_lines = textwrap.wrap(title, width=30)
    if len(title_lines) > 1:
        img_draw.text(
            img_draw.textbbox((w // 2, h // 2.5), title_lines[0], font=title_font),
            title_lines[0],
            font=title_font,
            fill="black",
            direction="rtl",
            anchor="mm",
            align="center",
        )
        img_draw.text(
            img_draw.textbbox((w // 2, h // 1.5), title_lines[1], font=title_font),
            title_lines[1],
            font=title_font,
            fill="black",
            direction="rtl",
            anchor="mm",
            align="center",
        )
    else:
        img_draw.text(
            img_draw.textbbox((w // 2, h // 2), title, font=title_font),
            title,
            font=title_font,
            fill="black",
            direction="rtl",
            anchor="mm",
            align="center",
        )
    img_draw.text(
        img_draw.textbbox((w // 12 - m, h // 4), price, font=price_font),
        price,
        font=price_font,
        fill="white",
        direction="rtl",
        anchor="mm",
        align="center",
    )
    img_draw.text(
        img_draw.textbbox((w // 12 - m, h - h // 4), price_coupon, font=price_font),
        price_coupon,
        font=price_font,
        fill="white",
        direction="rtl",
        anchor="mm",
        align="center",
    )

    img_draw.text(
        img_draw.textbbox((w // 5 - m, h // 4), price_label, font=price_label_font),
        price_label,
        font=price_label_font,
        fill="black",
        direction="rtl",
        anchor="mm",
        align="center",
    )
    img_draw.text(
        img_draw.textbbox(
            (w // 5 - m, h - h // 4), price_coupon_label, font=price_label_font
        ),
        price_coupon_label,
        font=price_label_font,
        fill="black",
        direction="rtl",
        anchor="mm",
        align="center",
    )

    os.makedirs(f"{settings.BASE_DIR}/output", exist_ok=True)
    back_img.save(f"{settings.BASE_DIR}/output/product_{index + 1}.png")

    if index == 0:
        break

print("check output directory.")
