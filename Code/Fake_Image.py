from randimage import get_random_image, show_array
import time

start_time = time.time()
image_size = (317, 202)
img = get_random_image(image_size)
show_array(img)
print('Total time taken', time.time() - start_time)
