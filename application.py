from flask import Flask, render_template
import glob

# return filepaths for each image as a list
ffilm = glob.glob("static/images/ffilm/*")
doc = glob.glob("static/images/doc/*")
mvideo = glob.glob("static/images/mvideo/*")
festivals_dir = glob.glob("static/images/festivals/*")
festivals = glob.glob("static/images/festivals/*/*.jpg")

# strip the filepath and just return the subfolder and file name per film/video/doc
# this allows me to use the subfolder as a dictionary key to access info in the 3 dicts
ffilm = [s.replace("static/images/ffilm/", "") for s in ffilm]
mvideo = [s.replace("static/images/mvideo/", "") for s in mvideo]
doc = [s.replace("static/images/doc/", "") for s in doc]
festivals_dir = [s.replace("static/images/festivals/", "") for s in festivals_dir]
festivals = [s.replace("static/images/festivals/*/", "") for s in festivals]

# sort list by numerical order; numerical order is determined by marcin's preference
ffilm.sort()
doc.sort()
mvideo.sort()

# turn project info into a dict in order to populate the webpage w/ pertinent data
mvideo_dict = {
    "01 pixies - long rider": {
        "title": "Pixies - Long Rider",
        "url": "https://www.youtube.com/embed/thxrujYnY6c"
    },

    "02 starcrawler - chicken woman": {
        "title": "Starcrawler - Chicken Woman",
        "url": "https://www.youtube.com/embed/_8yTYlKPdS4"
    },

    "03 theophilus london and tame impala - only you": {
        "title": "Theophilus London and Tame Impala - Only You",
        "url": "https://www.youtube.com/embed/DTR47fI0IKw"
    },

    "04 blackbear - hot girl bummer": {
        "title": "blackbear - hot girl bummer",
        "url": "https://www.youtube.com/embed/yMlKJGKyoCo"
    },

    "05 starcrawler - she gets around": {
        "title": "Starcrawler - She Gets Around",
        "url": "https://www.youtube.com/embed/dmhUvGkX_Pw"
    },

    "06 nick waterhouse - wreck the rod": {
        "title": "Nick Waterhouse - Wreck the Rod",
        "url": "https://www.youtube.com/embed/vP0ekLNKzTU"
    },

    "07 grent lavalley - summer angel": {
        "title": "Grant LaValley - Summer Angel",
        "url": "https://www.youtube.com/embed/VpYGBnUrLVc"
    },

    "08 stonefield - in the eve": {
        "title": "Stonefield - In the Eve",
        "url": "https://www.youtube.com/embed/63gsuRoP5ew"
    },

    "09 starcrawler - hollywood ending": {
        "title": "Starcrawler - Hollywood Ending",
        "url": "https://www.youtube.com/embed/8mrnIRpeizY"
    },

    "10 theophilus london - marchin": {
        "title": "Theophilus London - Marchin",
        "url": "https://www.youtube.com/embed/uAOQnZjQZj8"
    }

}

ffilm_dict = {
    "01 public toilet africa": {
        "title": "Public Toilet Africa",
        "director": "Kofi Ofosu - Yeboah",
        "runtime": "95 min",
        "url": "https://player.vimeo.com/video/686460483?h=688592efc4"
    },

    "02 last weekend": {
        "title": "Last Weekend",
        "director": "Curtis Williams",
        "runtime": "90 min",
        "url": "https://player.vimeo.com/video/692325221?h=c93639a266"
    },

    "03 watch me kill": {
        "title": "Watch Me Kill",
        "director": "T. A. Acierto",
        "runtime": "114 min",
        "url": "https://player.vimeo.com/video/271733565?h=eba5988977"
    },

    "04 modus operandi 2": {
        "title": "Modus Operandi 2",
        "director": "Frankie Latina",
        "runtime": "123 min",
        "url": "https://player.vimeo.com/video/686553301?h=33116328e7"
    },

    "05 from a son": {
        "title": "From a Son",
        "director": "Gilbert Trejo",
        "runtime": "85 min",
        "url": "javascript:void(0);"
    },

    "06 grave bandits": {
        "title": "Grave Bandits",
        "director": "T. A. Acierto",
        "runtime": "100 min",
        "url": "https://player.vimeo.com/video/271732653?h=e91647f7ad"
    }

}

doc_dict = {
    "01 doc reel": {
        "title": "Documentary Reel",
        "url": "https://player.vimeo.com/video/690068955?h=caa183e699"
    },
}

festivals_dict = {}

# for any directories that exist in the "festivals" folder...
for film in festivals_dir:
    # ... enter a new key into the festivals_dict; the value is any image file that includes the film name we are currently iterating
    festivals_dict[film] = [img for img in festivals if film in img]

application = Flask(__name__)


@application.route("/")
def home():
    # i am passing the file
    return render_template("index.html", ffilm = ffilm, doc = doc, mvideo = mvideo, 
    ffilm_dict = ffilm_dict, mvideo_dict = mvideo_dict, doc_dict = doc_dict, festivals_dict = festivals_dict)

@application.route("/player/<video>&<videotype>")
def player(video, videotype):
    return render_template("player.html", ffilm = ffilm, doc = doc, mvideo = mvideo, 
    ffilm_dict = ffilm_dict, mvideo_dict = mvideo_dict, doc_dict = doc_dict, festivals_dict = festivals_dict, video=video, videotype=videotype)

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    application.run("localhost", debug=False) # CHANGE TO FALSE PRIOR TO PUSHING
