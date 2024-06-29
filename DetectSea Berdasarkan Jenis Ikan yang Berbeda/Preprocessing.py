import numpy as np
import cv2
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
class Enchantment:
    def __init__(self, num_workers=1):
        self.num_workers = num_workers
    
    def equalize_histogram_single(self, image):
        flat_image = image.flatten()
        histogram, _ = np.histogram(flat_image, bins=256, range=(0, 256))
        cumulative_histogram = np.cumsum(histogram)
        normalization_factor = 255 / cumulative_histogram[-1]
        mapping = np.round(normalization_factor * cumulative_histogram).astype(np.uint8)
        return mapping[image]
    
    def equalize_histogram(self, images):
        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            results = list(executor.map(self.equalize_histogram_single, images))
        return results
    
    def blur_single(self, image, kernel_size, blur_type):
            if blur_type == 'mean':
                return cv2.blur(image, (kernel_size, kernel_size))
            elif blur_type == 'median':
                return cv2.medianBlur(image, kernel_size)
            elif blur_type == 'gaussian':
                return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
            else:
                raise ValueError("Unsupported blur type")

    def blur_images(self, images, kernel_size=3, blur_type='mean'):
            with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
                results = list(executor.map(self.blur_single, images, repeat(kernel_size), repeat(blur_type)))
            return np.array(results)