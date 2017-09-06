import IPython
import os
import requests

ftypes = {
    'image/jpeg':"jpg",
    'image/png':"png",
    'image/gif':"gif"
}


class Image(object):
    def __init__(self,doc):
        self.dpla_desc = doc
        self.dpla_id = doc['id']
        self.embedding = None
        
    def set_tensorflow_session(self):
        pass
    
    def display_in_ipython(self):
        IPython.core.display.display(IPython.core.display.Image(filename=self.cache_thumbnail()))
    
    def get_bottleneck_layer(self,sess):
        if self.embedding is not None:
            return self.embedding
        self.embedding = sess.run(bottleneck,{'DecodeJpeg:0': self.image_data()})
        return self.embedding
    
    def cache_thumbnail(self,prefix="thumbnails"):
        """
        Given a DPLA document record, return the file location if it's already been
        downloaded: otherwise, 
        """
        doc = self.dpla_desc
        image = doc['object']
        identifier = doc['id']
        url = doc["object"]
        for suffix in ["png","jpg","gif"]:
            p = "{}/{}.{}".format(prefix,identifier,suffix)
            if os.path.exists(p):
                return p

        r = requests.get(url, stream = True)
        ftype = r.headers["Content-Type"]

        with open("{}/{}.{}".format(prefix,identifier,ftypes[ftype]), 'wb') as fd:
            for chunk in r.iter_content(400):
                fd.write(chunk)
        return "{}/{}.{}".format(prefix,identifier,ftypes[ftype])


    def image_data(self):
        image = PIL.Image.open(self.cache_thumbnail())
        
        if len(np.array(image).shape) == 2:
            image = np.tile(np.expand_dims(np.array(image),2),3)

        image_array = np.array(image)[:, :, 0:3]  # Select RGB channels only.
        return image_array
    
    def infer_imagenet_labels(self,sess=None, n=7,verbose = True):
        if sess is None:
            sess = set_tensorflow_session
        # This is altered from the original code to take a numpy array of rgb channels, 
        # and to return an array.
        predictions = sess.run(softmax_tensor,{'DecodeJpeg:0': self.image_data()})
        predictions = np.squeeze(predictions)

        # Creates node ID --> English string lookup.

        top_k = predictions.argsort()[-n:][::-1]
        prediction_list = []
        for node_id in top_k:
            human_string = node_lookup.id_to_string(node_id)
            score = predictions[node_id]
            prediction_list.append((score,human_string))
            if verbose:
                print('%s (score = %.4f)' % (human_string, score))
        return prediction_list
    
    def download_full_size(self,path=None):
        pass
        # What percentage of DPLA is IIIF compatible?
        # https://github.com/lovasoa/dezoomify/wiki/How-to-download-full-resolution-images-from-an-IIIF-compatible-server
