# 🎨 Color Detection using OpenCV

This project uses OpenCV and NumPy to detect specific colors (Blue, Red, Green, Yellow) in an image using the HSV color space.

## 🧰 Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

1. Place your input image in the project folder.
2. Update the image path in `color_detection.py`:

```python
img = cv2.imread('your_image.webp')  # Replace with your actual image file name
```

3. Run the script:

```bash
python color_detection.py
```

This will open separate windows showing the original image and masks for each detected color. Press any key to close them.

## 🎯 HSV Color Ranges Used

- **Blue**: `[100, 150, 0]` to `[140, 255, 255]`
- **Red**: Two ranges `[0, 120, 70]` to `[10, 255, 255]` and `[170, 120, 70]` to `[180, 255, 255]`
- **Green**: `[40, 70, 70]` to `[80, 255, 255]`
- **Yellow**: `[20, 100, 100]` to `[30, 255, 255]`

These can be adjusted based on your lighting or image.

## 📜 License

This project is licensed under the MIT License.
