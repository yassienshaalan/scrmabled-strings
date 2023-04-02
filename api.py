from flask import Flask, request
import logging
import importlib
module_name = 'scrmabled-strings'
module = importlib.import_module(module_name)

app = Flask(__name__)

@app.route('/wordcounter', methods=['POST'])
def mypostendpoint():
    counts = []
    try:
        dictionary_file = request.files['dictionary_file']
        try:
            input_file = request.files['input_file']
            try:
                solver = module.ScrmabledStringsSolver(dictionary_file, input_file)
                counts = solver.solve_api(dictionary_file,input_file)
                print("Results for this run")
                logging.info(f"Results for this run")
                for i in range(len(counts)):
                    print(f"Case #{i}: {counts[i]}")
                    logging.info(f"Processed Case #{i}. Match count: {counts[i]}")
                print("--------------------")
                logging.info(f"--------------------")
                return counts
            except Exception as e:
                # code to handle the exception
                print("An error occurred in solving the problem:", e)
                return 'Error'
        except FileNotFoundError:
            print(f"Error: Could not find file '{input_file}'.")
            logging.error(f"Could not find file '{input_file}'.")
            return 'Error'
    except FileNotFoundError:
        print(f"Error: Could not find file '{dictionary_file}'.")
        logging.error(f"Could not find file '{dictionary_file}'.")
        return 'Error'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)