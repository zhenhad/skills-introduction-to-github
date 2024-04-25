# Vision Transformers (ViT):
Traditionally, Convolutional Neural Networks (CNNs) have been the go-to models for visual tasks, but ViTs offer a novel alternative. By leveraging the self-attention mechanisms and Transformer architectures, ViTs break the limitations imposed by local receptive fields in CNNs.
## Why ViT?
They capture global dependencies and long-range interactions within an image. This leads to remarkable performance improvements in various computer vision tasks, including image classification, object detection, and image generation.

The network’s ability to focus on different input areas at different times allows it to capture local and global relationships, so collect spatial relationships in images more effectively than other types of neural networks. They have the ability to effectively model high-dimensional visual data.
transformers are a type of neural network architecture that:

processes incoming data through self-attention techniques. 
The self-attention mechanism
allows the network to focus on different sections of the input data at other times. It allows to capture both local and global associations
![Transformer](transformer_architecture.jpg)

## conventional feedforward: 
each neuron in a given layer is connected to all neurons in the next layer.
## self-attention mechanism:
each neuron in a specific layer is connected to all other neurons in that layer, including itself.

the input image is divided into a grid of patches, and each patch is treated as an element in the input sequence.

# Attention Mechanism in Computer Vision (CV):
The model needed to focus on different image portions at different times.

Attention mechanisms are utilized in vision transformers to record the image’s local and global spatial relationships. Instead of using convolutions to extract image features, the input image is partitioned into a grid of patches, with each patch regarded as a sequence element. The self-attention mechanism is then applied to the sequence of patch embeddings to generate a new set of embeddings that represent the spatial relationships between the patches.

Vision transformers can capture long-range dependencies and relationships between patches in the image more effectively by using self-attention rather than convolutions

# Patch-based Processing:

breaking the input image into smaller, fixed-size patches and treating each patch as a single token. This method has both advantages and cons.

## Advantages:
* vision transformers may accept inputs of various sizes without extra resizing or cropping. This is especially beneficial for applications like object detection and segmentation, where the size and shape of the objects in the image might change significantly.

* interactions between patches throughout the image, allowing for more excellent capture of the global image context. This is especially significant for tasks like scene comprehension or image captioning, where the context and interactions between items in the image are critical for creating accurate descriptions.





###References:
_*
