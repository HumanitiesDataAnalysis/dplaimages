# DPLAimages

Tools for image analysis with the DPLA and TensorFlow, created to support work in Northeastern University graduate courses.
Initially forked from [@lwrubel's `dplaplay.`](https://github.com/lwrubel/dplaplay)


# The Idea

There are 5 million images in the DPLA, and image analysis has gotten crazy good lately.
What are some of the low-hanging fruit historians should be looking towards?

# Structure

`exploration/`: Some demo notebooks showing what can be done.

`DPLAimages/`: A folder with a class for DPLA images and for TensorFlow models.
	           These are classes designed to be capacious in doing whatever might be useful. 

`config.py`: A file *not* included in this repo, that must contain your DPLA API key. My file looks like, in its entirety (except that the below isn't a valid API key):

```
dpla_api_key = "f82e91041287b52f268b739b1bfa49bb"
```

# Philosophy

Basically, the primary object is an `Image`, initialized with some search results.
Then you can do stuff to it; print it in a notebook, check it for faces, extract the bottleneck hash.

# Downloads

It's nice to be able to cache things like thumbnails and Inception hashes. This should have some way to do that.
