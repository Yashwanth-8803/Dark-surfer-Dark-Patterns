from PIL import Image, ImageDraw

def create_icon(size, filename):
    # Create a square image with dark blue background
    img = Image.new("RGB", (size, size), "#0A0A23")
    draw = ImageDraw.Draw(img)

    # Draw a simple magnifying glass shape (circle + handle)
    # Circle (lens)
    lens_radius = size // 4
    lens_center = (size // 2 - lens_radius // 2, size // 2 - lens_radius // 2)
    draw.ellipse([
        lens_center[0], lens_center[1],
        lens_center[0] + lens_radius, lens_center[1] + lens_radius
    ], outline="white", width=max(1, size // 16))

    # Handle (line from lens to bottom-right)
    handle_start = (
        lens_center[0] + lens_radius * 3 // 4,
        lens_center[1] + lens_radius * 3 // 4
    )
    handle_end = (size - size // 8, size - size // 8)
    draw.line([handle_start, handle_end], fill="white", width=max(1, size // 16))

    # Save the image
    img.save(filename)
    print(f"{filename} created.")

# Generate icons
create_icon(16, "icon16.png")
create_icon(48, "icon48.png")
create_icon(128, "icon128.png")
