from flask import Flask, render_template
import glob

# return filepaths for each image as a list
ffilm = glob.glob("static/images/ffilm/*")
doc = glob.glob("static/images/doc/*")
mvideo = glob.glob("static/images/mvideo/*")

# strip the filepath and just return the subfolder and file name per film/video/doc
ffilm = [s.replace("static/images/ffilm/", "") for s in ffilm]
mvideo = [s.replace("static/images/mvideo/", "") for s in mvideo]
doc = [s.replace("static/images/doc/", "") for s in doc]

# sort list by numerical order; numerical order is determined by marcin's preference
ffilm.sort()
doc.sort()
mvideo.sort()

# turn project info into a dict in order to populate the webpage w/ pertinent data
mvideo_dict = {
    "01 pixies - long rider": {
        "title": "Pixies - Long Rider",
        "url": "https://www.youtube.com/watch?v=thxrujYnY6c"
    },

    "02 starcrawler - chicken woman": {
        "title": "Starcrawler - Chicken Woman",
        "url": "https://www.youtube.com/watch?v=_8yTYlKPdS4&t=28s"
    },

    "03 theophilus london and tame impala - only you": {
        "title": "Theophilus London and Tame Impala - Only You",
        "url": "https://www.youtube.com/watch?v=DTR47fI0IKw"
    },

    "04 blackbear - hot girl bummer": {
        "title": "blackbear - hot girl bummer",
        "url": "https://www.youtube.com/watch?v=yMlKJGKyoCo"
    },

    "05 starcrawler - she gets around": {
        "title": "Starcrawler - She Gets Around",
        "url": "https://www.youtube.com/watch?v=dmhUvGkX_Pw"
    },

    "06 nick waterhouse - wreck the rod": {
        "title": "Nick Waterhouse - Wreck the Rod",
        "url": "https://www.youtube.com/watch?v=vP0ekLNKzTU"
    },

    "07 grent lavalley - summer angel": {
        "title": "Grant LaValley - Summer Angel",
        "url": "https://www.youtube.com/watch?v=VpYGBnUrLVc"
    },

    "08 stonefield - in the eve": {
        "title": "Stonefield - In the Eve",
        "url": "https://www.youtube.com/watch?v=63gsuRoP5ew"
    },

    "09 starcrawler - hollywood ending": {
        "title": "Starcrawler - Hollywood Ending",
        "url": "https://www.youtube.com/watch?v=8mrnIRpeizY"
    },

    "10 theophilus london - marchin": {
        "title": "Theophilus London - Marchin",
        "url": "https://www.youtube.com/watch?v=uAOQnZjQZj8"
    }

}

ffilm_dict = {
    "01 public toilet africa": {
        "title": "Public Toilet Africa",
        "url": "https://vimeo.com/manage/videos/686460483"
    },

    "02 last weekend": {
        "title": "Last Weekend",
        "url": "https://vimeo.com/manage/videos/692325221"
    },

    "03 watch me kill": {
        "title": "Watch me Kill",
        "url": "https://vimeo.com/manage/videos/271733565"
    },

    "04 modus operandai": {
        "title": "Modus Operandai",
        "url": "https://vimeo.com/manage/videos/686553301"
    },

    "05 from a son": {
        "title": "From a Son",
        "url": "javascript:void(0);"
    }

}

doc_dict = {
    "01 doc reel": {
        "title": "Documentary Reel",
        "url": "https://vimeo.com/manage/videos/690068955"
    },
}

application = Flask(__name__)


@application.route("/")
def home():
    # i am passing the file
    return render_template("index.html", ffilm = ffilm, doc = doc, mvideo = mvideo, 
    ffilm_dict = ffilm_dict, mvideo_dict = mvideo_dict, doc_dict = doc_dict)


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    application.run("localhost", debug=False)
