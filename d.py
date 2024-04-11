# Analyze_Image_Fubction: 


import numpy as np
from skimage import measure, morphology
from skimage.filters import threshold_otsu
from scipy import ndimage
from skimage.color import rgb2gray
import pandas as pd
from PIL import Image

def analyze_image(nuclei_bw, img_n, nucleizone):
    img_gray = np.array(img_n)[:,:,0]  # Assuming imgN is a PIL image or a NumPy array

    properties = ['area', 'perimeter', 'centroid', 'solidity', 'weighted_centroid']
    nucleidata = pd.DataFrame(measure.regionprops_table(nuclei_bw, img_gray, properties=properties))
    if len(nucleidata) >= 5000:
        mean_area = nucleidata['area'].mean()
        max_area = nucleidata['area'].max()
        nuclei_bw = morphology.remove_small_objects(nuclei_bw, min_size=mean_area*0.7)
        nuclei_bw = morphology.remove_small_objects(nuclei_bw, min_size=max_area, connectivity=None, in_place=False)
        nucleidata = pd.DataFrame(measure.regionprops_table(nuclei_bw, img_gray, properties=properties))
    
    nuclei_label = measure.label(nuclei_bw)

    # Compactness
    nucleidata['compactness'] = nucleidata['perimeter'] ** 2 / nucleidata['area'] - 1
    
    # Other parameters
    boundaries = measure.find_contours(nuclei_bw, level=0.8)
    radius = []
    variance = []
    smoothness = []
    
    for region in measure.regionprops(nuclei_label):
        centroid = region.weighted_centroid
        region_boundary = boundaries[region.label - 1]  # Adjusting label to match boundary index
        distances = np.sqrt((region_boundary[:, 0] - centroid[0]) ** 2 + (region_boundary[:, 1] - centroid[1]) ** 2)
        
        radius.append(distances.mean())
        region_image = img_gray[nuclei_label == region.label]
        variance.append(np.std(region_image))
        smoothness.append(np.std(distances))
    
    nucleidata['radius'] = radius
    nucleidata['smoothness'] = smoothness
    nucleidata['texture'] = variance

    # ImageData calculation
    imagedata = {
        'radius_me': np.mean(nucleidata['radius']),
        # Add other mean calculations in the same manner
        # Standard error deviation calculations
        'radius_stde': np.std(nucleidata['radius']) / np.sqrt(len(nucleidata)),
        # Add other standard error deviations in the same manner
        # "worst" or "highest" values
        'radius_worst': np.max(nucleidata['radius']),
        # Add other "worst" calculations in the same manner
        # Density calculations
        'density': len(nucleidata) / (img_n.size[0] * img_n.size[1] * 0.25 ** 2) / 10e-6,
        'numbofcells': len(nucleidata),
        'densityinzone': len(nucleidata) / (np.sum(nucleizone == 1) * 0.25 ** 2) / 10e-6,
        'zonearea': np.sum(nucleizone == 1) / (img_n.size[0] * img_n.size[1])
    }

    imagedata = pd.DataFrame([imagedata])

    return imagedata, nuclei_label, nucleizone, nucleidata
