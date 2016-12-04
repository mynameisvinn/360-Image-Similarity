import cv2
import unittest
import SSIM.ssim


class FactorialTest(unittest.TestCase):
    
    def test_identity(self):
    	img = cv2.imread('images/download.png', 0) # 0 flag indicates read as grayscale
        self.assertEqual(SSIM.ssim.compute_ssim(img, img, img.shape[1]), 1.0)

if __name__ == "__main__":
    unittest.main()