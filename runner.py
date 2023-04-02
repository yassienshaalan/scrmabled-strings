import requests

url = 'http://localhost:80/wordcounter'  # Replace localhost with your server ip if you have

dictionary_file = open('testing_data/test_dict_2.txt', 'rb')  
input_file = open('testing_data/test_input_2.txt', 'rb') 

files = {'dictionary_file': dictionary_file, 'input_file': input_file}
response = requests.post(url, files=files)
if response.status_code!=200:
    print("An error occurred: status code", response.status_code)
else:
    counts = response.content.decode("utf-8").strip('[').strip(']\n').split(',')
    for i in range(len(counts)):
         print(f"Case #{i}: {counts[i]}")

dictionary_file.close()
input_file.close()