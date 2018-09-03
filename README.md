# CloudEdgeAI
This repo is for Geekon 2018 Edge AI in the cloud project

# concept
The way I envision this project is as follows:
* Use standard data sets as a base for style transfer (or other method) to generate look alike images to clouds and arial images. 
* Put the said model on an edge device (probably R-pi. Ill also bring my http://jevois.org/).
* Tie it to a kite - take it to the clouds.

## Items:
* Tamar and I plan to build a kite from leftover fabric / old dead kites. I'll also bring a couple of heavy lifting kites and a 300 m string.
* Tamar is working on getting cloud images + cloud that looks like things images.
* we need to explore ways to generate a training set. My idea below.
* We need to verify inference model can be placed on the R-pi


## HW:
* I have an R-pi and a Jevios, need to find an pi-cam - do you have one?
* For kites: need old kites / umbrellas / other things from ripstop fabric, spores and such.
* For training: I'll bring a PC with modest GPU running Ubuntu Python 3.6. I plan on using Keras over TF. If you think you'll also work on that part - can you bring a computer as well.

## AI process
As there are no available sources of clouds looking like things, we will need to generate those. One way to go about that is to use style transfer, another using GANs
style transfer: https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/15_Style_Transfer.ipynb
GANs: https://github.com/AntreasAntoniou/DAGAN (with decent review on such processes): https://arxiv.org/pdf/1711.04340.pdf  Refered from [here](https://ai-blog.co.il/2018/09/02/%D7%9C%D7%97%D7%95%D7%9C%D7%9C-data-%D7%97%D7%93%D7%A9-%D7%9B%D7%93%D7%99-%D7%9C%D7%A9%D7%A4%D7%A8-%D7%A1%D7%99%D7%95%D7%95%D7%92-%D7%94%D7%A8%D7%97%D7%91%D7%AA-data-%D7%91%D7%A2%D7%96%D7%A8%D7%AA-ga/)

# Example ideas
https://www.pyimagesearch.com/2017/12/18/keras-deep-learning-raspberry-pi/

# Dependencies
I think we should base on Keras over TF, but I guess Fast AI over Pytourch could be a way to go.
