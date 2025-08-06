__author__ = "Vivek"
__author_email__ = "vivekltp120@gmail.com"


import qrcode

# Text or URL to encode
data = """
# 🍽️ Lauki Halwa Nutrition Facts

Lauki Halwa, also known as Bottle Gourd Halwa, is a delicious and nutritious dessert made from grated bottle gourd (lauki), milk, sugar, and ghee. It is a popular sweet dish in Indian cuisine, especially enjoyed during festivals and special occasions. Below is a breakdown of the nutritional content of a typical serving (100g) of Lauki Halwa.

## 🌾 Nutritional Information (Per 100g Serving)

Calories:  
- 🔸 Energy: ~150-250 kcal

Macronutrients:  
- 🔹 Carbohydrates: ~20-30g  
  - Sugars: ~15-25g  
  - Dietary Fiber: ~1-2g  
- 🔹 Protein: ~3-5g  
- 🔹 Fats: ~7-12g  
  - Saturated Fat: ~4-6g  
  - Unsaturated Fat: ~1-3g  
- 🔹 Cholesterol: ~15-25mg

Micronutrients:  
- 🔸 Calcium: ~80-120mg  
- 🔸 Iron: ~0.5-1mg  
- 🔸 Magnesium: ~10-20mg  
- 🔸 Potassium: ~100-150mg  
- 🔸 Sodium: ~50-100mg  
- 🔸 Phosphorus: ~70-90mg

Vitamins:  
- 🔹 Vitamin A: ~100-200 IU  
- 🔹 Vitamin B1 (Thiamine): ~0.05mg  
- 🔹 Vitamin B2 (Riboflavin): ~0.1mg  
- 🔹 Vitamin B3 (Niacin): ~0.3mg  
- 🔹 Vitamin C: ~2-4mg

Additional Nutrients:  
- 🔸 Water Content: ~60-70g  
- 🔸 Ash (Minerals): ~1-2g

## 🍽️ Health Benefits

1. High in Dietary Fiber  
2. Rich in Vitamins and Minerals  
3. Source of Healthy Fats  
4. Hydrating and Cooling  
5. Good for Digestion
"""

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='blue', back_color='white')

# Save the image
img.save('lauki_halwa_qrcode.png')
