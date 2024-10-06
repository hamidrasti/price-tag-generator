# Price Tag Generator

This Python project generates price tags based on product details from an Excel file. The tags include product titles, prices, and coupon prices, and are saved as images. The project leverages `Pillow`, `Pandas`, and `openpyxl` libraries to handle image creation and data extraction.

## Features
- Automatically reads product data from an Excel file (`input.xlsx`).
- Creates price tags with product titles, original prices, and discounted coupon prices.
- Supports custom fonts for titles and prices.
- Saves generated tags in the `output` directory.

## Requirements

Before running the project, ensure the following packages are installed:

```bash
pip install -r requirements.txt
```

`requirements.txt` includes the following:
- `openpyxl` (for reading Excel files)
- `pandas` (for data processing)
- `pillow` (for image generation)

### Additional System Dependencies
For proper rendering of text using RTL (right-to-left) languages or complex fonts (like Arabic or Persian), `Pillow` requires the installation of `libraqm` on your system. You can install it using the following:

For **Debian/Ubuntu-based systems**:
```bash
sudo apt install libraqm-dev
```

This will enable the `PIL.ImageFont.truetype()` function to support advanced text layouts.

## Project Structure

```
|-- assets
|   |-- fonts
|       |-- title.ttf
|       |-- price.ttf
|   |-- input.xlsx
|   |-- logo.png
|-- output/
|-- generate_tags.py
|-- settings.py
|-- requirements.txt
```

- **`assets/fonts/`**: Contains custom fonts for the title and price.
- **`assets/input.xlsx`**: Your Excel file with product data.
- **`assets/logo.png`**: Your Logo file.
- **`output/`**: Generated price tags will be saved here.
- **`generate_tags.py`**: Main script for generating price tags.
- **`settings.py`**: Configuration for image size, paths, etc.
- **`requirements.txt`**: List of dependencies.

## Input Excel File Format

The input file (`input.xlsx`) must contain a sheet named **Sheet1**, and the following columns:
- **Title**: Product title.
- **Price**: Original product price.
- **CouponPrice**: Discounted price using a coupon.

Example:

| Title           | Price   | CouponPrice |
|-----------------|---------|-------------|
| Product 1       | 100,000 | 90,000      |
| Product 2       | 150,000 | 130,000     |

## How to Use

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure that `libraqm` is installed for RTL support.

3. Place your product data in `assets/input.xlsx`.

4. Run the tag generator:
   ```bash
   python generate_tags.py
   ```

5. Check the generated images in the `output/` folder.

## Output

Each price tag will be saved in the `output` directory as a PNG file, with filenames like `product_1.png`, `product_2.png`, etc.