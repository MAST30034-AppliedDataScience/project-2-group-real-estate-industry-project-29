import pandas as pd
import os
from tqdm import tqdm
from opencage.geocoder import OpenCageGeocode
import traceback
import multiprocessing

multiprocessing.set_start_method("spawn", force=True)

def geocode_chunk(file_path, output_folder, start_record, chunk_size=400):
    # Load the original data
    properties_df = pd.read_csv(file_path)

    # Limit the data to the specified range of records
    end_record = start_record + chunk_size
    properties_df = properties_df.iloc[start_record:end_record]

    # Drop rows with missing address fields
    properties_df.dropna(subset=['Address Line 1', 'Address Line 2'], inplace=True)

    # Create empty lists to store latitude and longitude
    latitudes = []
    longitudes = []

    # Initialize OpenCage Geocode API
    api_key = 'bfd72baf24d54842bced29afa4ec2311'  # Replace with your actual OpenCage API key
    geocoder = OpenCageGeocode(api_key)

    # Total number of addresses
    total_addresses = len(properties_df)

    # Initialize progress bar with total addresses
    try:
        with tqdm(total=total_addresses, desc=f"Geocoding addresses {start_record} to {end_record}") as pbar:
            for _, row in properties_df.iterrows():
                # Concatenate address using the actual column names 'Address Line 1' and 'Address Line 2'
                full_address = f"{row['Address Line 1']}, {row['Address Line 2']}"

                try:
                    # Geocode the address using OpenCage
                    results = geocoder.geocode(full_address)

                    if results and len(results):
                        latitudes.append(results[0]['geometry']['lat'])
                        longitudes.append(results[0]['geometry']['lng'])
                    else:
                        latitudes.append(None)
                        longitudes.append(None)
                except Exception as e:
                    latitudes.append(None)
                    longitudes.append(None)
                    print(f"Error geocoding address '{full_address}': {e}")

                # Update progress bar
                pbar.update(1)
    except Exception as e:
        # Save the partially processed data in case of an error
        properties_df['latitude'] = latitudes
        properties_df['longitude'] = longitudes
        partial_file_path = os.path.join(output_folder, f"geocoded_partial_{start_record}_{end_record}.csv")
        properties_df.to_csv(partial_file_path, index=False)
        print(f"An error occurred: {e}")
        print(f"The partially processed data has been saved as '{partial_file_path}'.")
        traceback.print_exc()
        return

    # Add latitude and longitude to the dataframe
    properties_df['latitude'] = latitudes
    properties_df['longitude'] = longitudes

    # Save the updated data to a new CSV file
    output_file_path = os.path.join(output_folder, f"geocoded_{start_record}_{end_record}.csv")
    properties_df.to_csv(output_file_path, index=False)
    print(f"Geocoding completed. The data has been saved as '{output_file_path}'.")

def run_geocoding_in_parallel(file_path, output_folder, start_record=0, chunk_size=400, num_processes=3):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    processes = []
    for i in range(num_processes):
        process_start_record = start_record + i * chunk_size
        p = multiprocessing.Process(target=geocode_chunk, args=(file_path, output_folder, process_start_record, chunk_size))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == '__main__':
    # Call the function to run geocoding in parallel
    file_path = "victoria_combined_rent_listings.csv"
    output_folder = "geocoded_output"
    run_geocoding_in_parallel(file_path, output_folder, start_record=6400, chunk_size=400, num_processes=7)