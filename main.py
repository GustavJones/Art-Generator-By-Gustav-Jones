from PIL import Image, ImageDraw
import random, os, math, naming_bot, delete_images, config

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variables
delete_image_files = config.config["Delete Files"]
if delete_image_files:
  images_amount = 0
else:
  images_amount = config.config["Images Amount"]
image_size = config.config["Image Size"]
large_image_size = image_size * 2
half_image = image_size // 2
line_size = image_size // 250
max_sides = config.config["Max Sides"]
shapes_amount = config.config["Shapes Amount"]

# Classes
class Shapes():
  def draw(self):
    shape_colour = random_colour()
    draw.polygon(coords, shape_colour, shape_colour)

  def get_coords(self):
    global coords
    coords = []
    for _ in range(random.randint(3, max_sides)):
      coords.append(random_pos())

  def smoothen(self):
    image.resize((image_size, image_size), Image.ANTIALIAS)

# Functions
def calculate_dist(coord1, coord2):
  dist = math.sqrt(
    (coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2
  )
  return int(dist)
  
def random_pos():
  return (
    random.randint(
      large_image_size // 15,
      large_image_size - large_image_size // 15
    ),
    random.randint(
      large_image_size // 15,
      large_image_size - large_image_size // 15
    )
  )

def random_colour():
  return (

    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
  )

def create_image():
  global image, draw
  image = Image.new(
    "RGB",
    (
      large_image_size,
      large_image_size
    ),
    random_colour()
  )
  draw = ImageDraw.Draw(image)
 
def save_image(image_num):
  image.save(
    os.path.join(
      "results",
      str(image_num) + ") " + naming_bot.name_image()
    )
  )

# Loops, If Statements And Other
for number in range(images_amount):
  create_image()
  shape = Shapes()
  for _ in range(shapes_amount):
    shape.get_coords()
    shape.draw()
  shape.smoothen()
  save_image(number)

if delete_image_files:
  delete_images.delete_all()

print("Done!")