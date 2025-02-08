import csv
import random  # Placeholder for generating responses

index = 0
def generate_response(prompt):
    global index 
    index += 1
    # Placeholder for actual response generation (replace with API call if needed)
    return f"Response {index}"

def process_csv(input_file, output_file):
    global index
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read header ("prompt", "number of runs")
        data = []
        for row in reader:
            prompt, num_runs = row[0], row[1]
            try:
                num_runs = int(num_runs)
            except ValueError:
                print(f"Invalid number of runs: {num_runs}")
                continue
            
            responses = [generate_response(prompt) for _ in range(num_runs)]
            data.append([prompt] + responses)
            index = 0
            
    
    max_responses = max(len(row) - 1 for row in data)
    headers = ["input prompt"] + [f"response {i+1}" for i in range(max_responses)]
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == "__main__":
    input_csv = "input.csv"   # Change this to your actual input file
    output_csv = "output.csv"  # Change this to your desired output file
    process_csv(input_csv, output_csv)
    print(f"Responses written to {output_csv}")
