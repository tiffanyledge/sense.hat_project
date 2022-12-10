from flask import Flask, render_template, request
import time
from sense_hat import SenseHat

sense = SenseHat()
app = Flask(__name__)




r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)
	

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/message', methods=['POST'])
def action():
    user_input = request.form['animation']
    if user_input == "regular kirby":
        image1 = [c, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c,
         d, c, c, c, c, c, c, c,
         d, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c,
         g, g, g, g, g, g, g, g
        ]		
        sense.set_pixels(image1)
        time.sleep(0.5)	
		
	 		

        image2 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                n, c, c, c, c, c, c, c,
                n, c, c, c, c, c, c, c,
                n, d, c, c, c, c, c, c,
                d, d, c, c, c, c, c, c,
                r, c, c, c, c, c, c, c,
                r, g, g, g, g, g, g, g
        ]		
        sense.set_pixels(image2)
        time.sleep(0.5)	
                

        image3 = [c, c, c, c, c, c, c, c,
                n, c, c, c, c, c, c, c,
                n, n, c, c, c, c, c, c,
                k, n, c, c, c, c, c, c,
                b, n, d, c, c, c, c, c,
                n, d, d, c, c, c, c, c,
                n, r, c, c, c, c, c, c,
                r, r, g, g, g, g, g, g
        ]	
        sense.set_pixels(image3)
        time.sleep(0.5)	

        image4 = [c, c, c, c, c, c, c, c,
                n, n, c, c, c, c, c, c,
                n, n, n, c, c, c, c, c,
                n, k, n, c, c, c, c, c,
                n, b, n, d, c, c, c, c,
                n, n, d, d, c, c, c, c,
                n, n, r, c, c, c, c, c,
                g, r, r, g, g, g, g, g
        ]		
        sense.set_pixels(image4)
        time.sleep(0.5)

        image5 = [c, c, c, c, c, c, c, c,
                n, n, n, c, c, c, c, c,
                n, n, n, n, c, c, c, c,
                k, n, k, n, c, c, c, c,
                b, n, b, n, d, c, c, c,
                n, n, n, d, d, c, c, c,
                d, n, n, r, c, c, c, c,
                r, g, r, r, g, g, g, g
        ]	
        sense.set_pixels(image5)
        time.sleep(0.5)
        image6 = [c, c, c, c, c, c, c, c,
                n, n, n, n, c, c, c, c,
                n, n, n, n, n, c, c, c,
                n, k, n, k, n, c, c, c,
                n, b, n, b, n, d, c, c,
                n, n, n, n, d, d, c, c,
                d, d, n, n, r, c, c, c,
                r, r, g, r, r, g, g, g
        ]		
        sense.set_pixels(image6)
        time.sleep(0.5)

        image7 = [c, c, c, c, c, c, c, c,
                n, n, n, n, n, c, c, c,
                n, n, n, n, n, n, c, c,
                d, n, k, n, k, n, c, c,
                n, n, b, n, b, n, d, c,
                d, n, n, n, n, d, d, c,
                r, d, d, n, n, r, c, c,
                r, r, r, g, r, r, g, g
        ]	
        sense.set_pixels(image7)
        time.sleep(0.5)

        image8 = [c, c, c, c, c, c, c, c,
                c, c, n, n, n, n, c, c,
                c, n, n, n, n, n, n, c,
                c, d, n, k, n, k, n, c,
                d, n, n, b, n, b, n, d,
                d, d, n, n, n, n, d, d,
                c, r, d, d, n, n, r, c,
                g, r, r, r, g, r, r, g
        ]		
                
                
        sense.set_pixels(image8)
        time.sleep(0.5)

        image9 = [c, c, n, n, n, n, c, c,
                c, n, n, n, n, n, n, c,
                c, d, n, k, n, k, n, c,
                d, n, n, b, n, b, n, d,
                d, d, n, n, n, n, d, d,
                c, r, d, d, n, n, r, c,
                c, r, r, r, c, r, r, c,
                g, g, g, g, g, g, g, g
        ]	
        sense.set_pixels(image9)	
        time.sleep(0.5)

        sense.set_pixels(image8)
        time.sleep(0.5)


        image10 = [c, c, c, c, c, c, c, c,
                c, c, c, n, n, n, n, c,
                c, c, n, n, n, n, n, n,
                c, c, d, n, k, n, k, n,
                c, d, n, n, b, n, b, n,
                c, d, d, n, n, n, n, d,
                c, c, r, d, d, c, n, r,
                g, g, r, r, r, g, r, r
        ]		
                
                        
        sense.set_pixels(image10)		
        time.sleep(0.5)

        image11 = [c, c, c, c, c, c, c, c,
                c, c, c, c, n, n, n, n,
                c, c, c, n, n, n, n, n,
                c, c, c, d, n, k, n, k,
                c, c, d, n, n, b, n, b,
                c, c, d, d, n, n, n, n,
                c, c, c, r, d, d, c, n,
                g, g, g, r, r, r, g, r
        ]		
                
        sense.set_pixels(image11)		
        time.sleep(0.5)

        image12 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, n, n, n,
                c, c, c, c, n, n, n, n,
                c, c, c, c, d, n, k, n,
                c, c, c, d, n, n, b, n,
                c, c, c, d, n, n, n, n,
                c, c, c, c, r, d, d, c,
                g, g, g, g, r, r, r, g
        ]		

        sense.set_pixels(image12)
        time.sleep(0.5)

        image13 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, n,
                c, c, c, c, c, c, n, n,
                c, c, c, c, c, c, d, n,
                c, c, c, c, c, d, n, n,
                c, c, c, c, c, d, d, n,
                c, c, c, c, c, c, r, d,
                g, g, g, g, g, g, r, r
        ]	

        sense.set_pixels(image13)
        time.sleep(0.5)

        image14 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, n,
                c, c, c, c, c, c, n, n,
                c, c, c, c, c, c, d, n,
                c, c, c, c, c, d, n, n,
                c, c, c, c, c, d, d, n,
                c, c, c, c, c, c, r, d,
                g, g, g, g, g, g, r, r
        ]	

        sense.set_pixels(image14)		
        time.sleep(0.5)		

        image15 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, n,
                c, c, c, c, c, c, c, d,
                c, c, c, c, c, c, d, n,
                c, c, c, c, c, c, d, d,
                c, c, c, c, c, c, c, r,
                g, g, g, g, g, g, g, r
        ]		

        sense.set_pixels(image15)
        time.sleep(0.5)
                
            

        image16 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, d,
                c, c, c, c, c, c, c, d,
                c, c, c, c, c, c, c, c,
                g, g, g, g, g, g, g, g
        ] 	

        sense.set_pixels(image16)
        time.sleep(0.5)

        image17 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                g, g, g, g, g, g, g, g
        ]	
		
        sense.set_pixels(image17)
        time.sleep(0.5)		
        print ('animation')
    elif user_input == "farmer kirby":
        
        img1 = [c, c, c, c, c, c, c, c,
        c, c, c, c, p, c, c, c,
        c, c, c, p, p, p, c, c,
        c, c, p, p, y, p, p, c,
        c, c, c, p, g, p, c, c,
        c, c, c, c, g, c, c, c,
        o, c, c, c, g, c, c, c,
        w, w, w, w, w, w, w, w
        ]
        sense.set_pixels(img1)
        time.sleep(0.5)	
        
        img2 = [c, c, c, c, c, c, c, c,
        c, c, c, c, p, c, c, c,
        c, c, c, p, p, p, c, c,
        c, c, p, p, y, p, p, c,
        c, c, c, p, g, p, c, c,
        o, c, c, c, g, c, c, c,
        c, o, c, c, g, c, c, c,
        w, w, w, w, w, w, w, w
        ]
        sense.set_pixels(img2)
        time.sleep(0.5)	

        img3 = [c, c, c, c, c, c, c, c,
        c, c, c, c, p, c, c, c,
        c, c, c, p, p, p, c, c,
        c, c, p, p, y, p, p, c,
        o, c, c, p, g, p, c, c,
        c, o, c, c, g, c, c, c,
        c, c, o, c, g, c, c, c,
        w, w, w, w, w, w, w, w
        ]
        sense.set_pixels(img3)
        time.sleep(0.5)	

        img4 = [c, c, c, c, c, c, c, c,
        y, c, c, c, p, c, c, c,
        c, c, c, p, p, p, c, c,
        c, c, p, p, y, p, p, c,
        d, o, c, p, g, p, c, c,
        d, c, o, c, g, c, c, c,
        c, c, c, o, g, c, c, c,
        w, w, w, w, w, w, w, w
        ]
        sense.set_pixels(img4)
        time.sleep(0.5)	

        img5 = [c, c, c, c, c, c, c, c,
        y, y, c, c, c, c, c, c,
        n, c, c, c, c, c, c, c,
        n, c, c, c, c, c, c, c,
        n, d, c, c, c, c, c, p,
        d, d, o, c, c, c, p, p,
        r, c, c, o, g, g, g, y,
        r, w, w, w, w, w, p, p
        ]
        sense.set_pixels(img5)
        time.sleep(0.5)	


        img6 = [y, c, c, c, c, c, c, c,
        y, y, y, c, c, c, c, c,
        n, n, c, c, c, c, c, c,
        k, n, c, c, c, c, c, c,
        b, n, d, c, c, c, c, p,
        n, d, d, o, c, c, p, p,
        n, r, c, c, o, g, g, y,
        r, r, w, w, w, o, p, p
        ]
        sense.set_pixels(img6)
        time.sleep(0.5)	 

        img7 = [y, y, c, c, c, c, c, c,
                y, y, y, y, c, c, c, c,
                n, n, n, c, c, c, c, c,
                n, k, n, c, c, c, c, c,
                n, b, n, d, c, c, c, p,
                n, n, d, d, o, c, p, p,
                n, n, r, c, c, o, g, y,
                w, r, r, w, w, w, o, p
        ]	
        sense.set_pixels(img7)
        time.sleep(0.5)	

        img8 = [y, y, y, c, c, c, c, c,
        y, y, y, y, y, c, c, c,
        n, n, n, n, c, c, c, c,
        k, n, k, n, c, c, c, c,
        b, n, b, n, d, c, c, p,
        n, n, n, d, d, o, p, p,
        d, n, n, r, c, c, o, y,
        r, w, r, r, w, w, w, o
        ]
        sense.set_pixels(img8)
        time.sleep(0.5)	
        
        img9 = [y, y, y, y, c, c, c, c,
        y, y, y, y, y, y, c, c,
        n, n, n, n, n, c, c, c,
        n, k, n, k, n, c, c, c,
        n, b, n, b, n, d, c, p,
        n, n, n, n, d, d, o, p,
        d, d, n, n, r, c, c, o,
        r, r, w, r, r, w, w, w
        ]	
        sense.set_pixels(img9)
        time.sleep(0.5)	
        
        img10 = [c, y, y, y, y, c, c, c,
        y, y, y, y, y, y, y, c,
        n, n, n, n, n, n, c, c,
        d, n, k, n, k, n, c, c,
        n, n, b, n, b, n, d, c,
        d, n, n, n, n, d, d, o,
        r, d, d, n, n, r, c, c,
        r, r, r, w, r, r, w, w
        ]
        sense.set_pixels(img10)
        time.sleep(0.5)	
        img11 = [c, c, y, y, y, y, c, c,
        y, y, y, y, y, y, y, y,
        c, n, n, n, n, n, n, c,
        c, d, n, k, n, k, n, c,
        d, n, n, b, n, b, n, d,
        d, d, n, n, n, n, d, d,
        c, r, d, d, n, n, r, c,
        w, r, r, r, w, r, r, w
        ]
        sense.set_pixels(img11)
        time.sleep(0.5)	 

        img12 = [c, c, c, y, y, y, y, c,
        c, y, y, y, y, y, y, y,
        c, c, n, n, n, n, n, n,
        c, c, d, n, k, n, k, n,
        c, d, n, n, b, n, b, n,
        c, d, d, n, n, n, n, d,
        c, c, r, d, d, n, n, r,
        w, w, r, r, r, w, r, r
        ]
        sense.set_pixels(img12)
        time.sleep(0.5)	

        img13 = [c, c, c, c, y, y, y, y,
        c, c, y, y, y, y, y, y,
        c, c, c, n, n, n, n, n,
        c, c, c, d, n, k, n, k,
        c, c, d, n, n, b, n, b,
        c, c, d, d, n, n, n, n,
        c, c, c, r, d, d, n, n,
        w, w, w, r, r, r, w, r
        ]
        sense.set_pixels(img13)
        time.sleep(0.5)
        img14 = [c, c, c, c, c, y, y, y,
                c, c, c, y, y, y, y, y,
                c, c, c, c, n, n, n, n,
                c, c, c, c, d, n, k, n,
                c, c, c, d, n, n, b, n,
                c, c, c, d, d, n, n, n,
                c, c, c, c, r, d, d, n,
                w, w, w, w, r, r, r, w
        ]
        sense.set_pixels(img14)
        time.sleep(0.5)	

        img15 = [c, c, c, c, c, c, y, y,
                c, c, c, c, y, y, y, y,
                c, c, c, c, c, n, n, n,
                c, c, c, c, c, d, n, k,
                c, c, c, c, d, n, n, b,
                c, c, c, c, d, d, n, n,
                c, c, c, c, c, r, d, d,
                w, w, w, w, w, r, r, r
        ]
        sense.set_pixels(img15)
        time.sleep(0.5)	

        img16 = [c, c, c, c, c, c, c, y,
                c, c, c, c, c, y, y, y,
                c, c, c, c, c, c, n, n,
                c, c, c, c, c, c, d, n,
                c, c, c, c, c, d, n, n,
                c, c, c, c, c, d, d, n,
                c, c, c, c, c, c, r, d,
                w, w, w, w, w, w, r, r
        ]
        sense.set_pixels(img16)
        time.sleep(0.5)	


        img17 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, y, y,
                c, c, c, c, c, c, c, n,
                c, c, c, c, c, c, c, d,
                c, c, c, c, c, c, d, n,
                c, c, c, c, c, c, d, d,
                c, c, c, c, c, c, c, r,
                w, w, w, w, w, w, w, r
        ]
        sense.set_pixels(img17)
        time.sleep(0.5)


        img18 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, y,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, d,
                c, c, c, c, c, c, c, d,
                c, c, c, c, c, c, c, c,
                w, w, w, w, w, w, w, w
        ]
        sense.set_pixels(img18)
        time.sleep(0.5)

        img19 = [c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                w, w, w, w, w, w, w, w
        ]
        sense.set_pixels(img19)
        time.sleep(0.5)
        print ('animation')
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
