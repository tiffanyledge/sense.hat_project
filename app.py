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

	


# image1 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          d, c, c, c, c, c, c, c,
#          d, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          g, g, g, g, g, g, g, g
# ]		
	
		
	 		

# image2 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          n, c, c, c, c, c, c, c,
#          n, c, c, c, c, c, c, c,
#          n, d, c, c, c, c, c, c,
#          d, d, c, c, c, c, c, c,
#          r, c, c, c, c, c, c, c,
#          r, g, g, g, g, g, g, g
# ]		

		

# image3 = [c, c, c, c, c, c, c, c,
#          n, c, c, c, c, c, c, c,
#          n, n, c, c, c, c, c, c,
#          k, n, c, c, c, c, c, c,
#          b, n, d, c, c, c, c, c,
#          n, d, d, c, c, c, c, c,
#          n, r, c, c, c, c, c, c,
#          r, r, g, g, g, g, g, g
# ]	


# image4 = [c, c, c, c, c, c, c, c,
#          n, n, c, c, c, c, c, c,
#          n, n, n, c, c, c, c, c,
#          n, k, n, c, c, c, c, c,
#          n, b, n, d, c, c, c, c,
#          n, n, d, d, c, c, c, c,
#          n, n, r, c, c, c, c, c,
#          g, r, r, g, g, g, g, g
# ]		


# image5 = [c, c, c, c, c, c, c, c,
#          n, n, n, c, c, c, c, c,
#          n, n, n, n, c, c, c, c,
#          k, n, k, n, c, c, c, c,
#          b, n, b, n, d, c, c, c,
#          n, n, n, d, d, c, c, c,
#          d, n, n, r, c, c, c, c,
#          r, g, r, r, g, g, g, g
# ]	

# image6 = [c, c, c, c, c, c, c, c,
#          n, n, n, n, c, c, c, c,
#          n, n, n, n, n, c, c, c,
#          n, k, n, k, n, c, c, c,
#          n, b, n, b, n, d, c, c,
#          n, n, n, n, d, d, c, c,
#          d, d, n, n, r, c, c, c,
#          r, r, g, r, r, g, g, g
# ]		

# image7 = [c, c, c, c, c, c, c, c,
#          n, n, n, n, n, c, c, c,
#          n, n, n, n, n, n, c, c,
#          d, n, k, n, k, n, c, c,
#          n, n, b, n, b, n, d, c,
#          d, n, n, n, n, d, d, c,
#          r, d, d, n, n, r, c, c,
#          r, r, r, g, r, r, g, g
# ]	


# image8 = [c, c, c, c, c, c, c, c,
#          c, c, n, n, n, n, c, c,
#          c, n, n, n, n, n, n, c,
#          c, d, n, k, n, k, n, c,
#          d, n, n, b, n, b, n, d,
#          d, d, n, n, n, n, d, d,
#          c, r, d, d, n, n, r, c,
#          g, r, r, r, g, r, r, g
# ]		
		
		


# image9 = [c, c, n, n, n, n, c, c,
#          c, n, n, n, n, n, n, c,
#          c, d, n, k, n, k, n, c,
#          d, n, n, b, n, b, n, d,
#          d, d, n, n, n, n, d, d,
#          c, r, d, d, n, n, r, c,
#          c, r, r, r, c, r, r, c,
#          g, g, g, g, g, g, g, g
# ]	


# image10 = [c, c, c, c, c, c, c, c,
#          c, c, c, n, n, n, n, c,
#          c, c, n, n, n, n, n, n,
#          c, c, d, n, k, n, k, n,
#          c, d, n, n, b, n, b, n,
#          c, d, d, n, n, n, n, d,
#          c, c, r, d, d, c, n, r,
#          g, g, r, r, r, g, r, r
# ]		
		
				


# image11 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, n, n, n, n,
#          c, c, c, n, n, n, n, n,
#          c, c, c, d, n, k, n, k,
#          c, c, d, n, n, b, n, b,
#          c, c, d, d, n, n, n, n,
#          c, c, c, r, d, d, c, n,
#          g, g, g, r, r, r, g, r
# ]		
		


# image12 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, c, n, n, n,
#          c, c, c, c, n, n, n, n,
#          c, c, c, c, d, n, k, n,
#          c, c, c, d, n, n, b, n,
#          c, c, c, d, n, n, n, n,
#          c, c, c, c, r, d, d, c,
#          g, g, g, g, r, r, r, g
# ]		



# image13 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, n,
#          c, c, c, c, c, c, n, n,
#          c, c, c, c, c, c, d, n,
#          c, c, c, c, c, d, n, n,
#          c, c, c, c, c, d, d, n,
#          c, c, c, c, c, c, r, d,
#          g, g, g, g, g, g, r, r
# ]

# image14 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, n,
#          c, c, c, c, c, c, n, n,
#          c, c, c, c, c, c, d, n,
#          c, c, c, c, c, d, n, n,
#          c, c, c, c, c, d, d, n,
#          c, c, c, c, c, c, r, d,
#          g, g, g, g, g, g, r, r
# ]	

	

# image15 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, n,
#          c, c, c, c, c, c, c, d,
#          c, c, c, c, c, c, d, n,
#          c, c, c, c, c, c, d, d,
#          c, c, c, c, c, c, c, r,
#          g, g, g, g, g, g, g, r
# ]		
	

# image16 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, d,
#          c, c, c, c, c, c, c, d,
#          c, c, c, c, c, c, c, c,
#          g, g, g, g, g, g, g, g
# ] 	


# image17 = [c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          c, c, c, c, c, c, c, c,
#          g, g, g, g, g, g, g, g
# ]	
			

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/message', methods=['POST'])
def action():
    user_input = request.form['animation']
    if user_input == "run":
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
    elif user_input == "cry":
        sense.set_pixels(image13)
        print ('animation')
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
