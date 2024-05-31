import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def show(image, title="Image"):
    plt.figure(figsize=(8, 8))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

def read_txt(filename):
    with open(filename) as f:
        lines = f.readlines()
    coords = []
    for line in lines:
        values = line.split(' ')
        class_id = int(values[0])
        x, y, w, h = map(float, values[1:5])
        coords.append((class_id, [x, y, w, h]))
    return coords

def rotate_image(image, angle):
    center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

def find_rotated_bbox(coord, rotated_mask):
    x, y, w, h = coord
    y_indices, x_indices = np.where(rotated_mask == 1)
    min_x = np.min(x_indices)
    max_x = np.max(x_indices)
    min_y = np.min(y_indices)
    max_y = np.max(y_indices)
    
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    width = max_x - min_x
    height = max_y - min_y

    return center_x, center_y, width, height

input_folder = "./ornek_resimler"
output_folder = "./output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        img = cv2.imread(os.path.join(input_folder, filename))
        img_height, img_width = img.shape[:2]
        
        rotated_image = rotate_image(img, 15)
        cv2.imwrite(os.path.join(output_folder, "rotated_" + filename), rotated_image)

        txt_filename = filename.replace(".jpg", ".txt")
        coords = read_txt(os.path.join(input_folder, txt_filename))

        rotated_coords = []
        for class_id, coord in coords:
            mask = np.zeros((img_height, img_width), dtype=np.uint8)
            x, y, w, h = coord
            start_x = int((x - w/2) * img_width)
            start_y = int((y - h/2) * img_height)
            end_x = int((x + w/2) * img_width)
            end_y = int((y + h/2) * img_height)
            mask[start_y:end_y, start_x:end_x] = 1
            
            rotated_mask = rotate_image(mask, 15)
            
            rotated_coord = find_rotated_bbox(coord, rotated_mask)
            rotated_coords.append((class_id, rotated_coord))

        output_txt_filename = "rotated_" + txt_filename
        output_txt_path = os.path.join(output_folder, output_txt_filename)
        with open(output_txt_path, 'w') as txt_file:
            for class_id, rotated_coord in rotated_coords:
                x = rotated_coord[0] / rotated_image.shape[1]
                y = rotated_coord[1] / rotated_image.shape[0]
                w = rotated_coord[2] / rotated_image.shape[1]
                h = rotated_coord[3] / rotated_image.shape[0]
                line = "{} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(class_id, x, y, w, h)
                txt_file.write(line)

        ##print("Written YOLO coordinates to:", output_txt_path)
