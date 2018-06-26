import sys
from integrator import synthesis

def main():
    # get two images from the command line
    img_1_path = sys.argv[1]
    img_2_path = sys.argv[2]

    # Synthesis class
    synthe_class = synthesis(img_1_path, img_2_path)

    out_1 = synthe_class.high_pass_function()
    out_2 = synthe_class.low_pass_function()
    synthe_class.synthesize(out_1, out_2)

if __name__ == "__main__":
    main()
