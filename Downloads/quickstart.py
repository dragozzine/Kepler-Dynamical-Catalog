import pandas as pd

# Due to restrictions on the file size in Github, we separated the KDC into 8 sections
# Indicate below via 'True' or 'False' whether you would like all or parts of the KDC
import_file1 = True
import_file2 = True
import_file3 = True
import_file4 = True
import_file5 = True
import_file6 = True
import_file7 = True
import_file8 = True
import_file9 = True
import_file10 = True
import_file11 = True
import_file12 = True

files = [import_file1, import_file2, import_file3, import_file4, import_file5, import_file6, import_file7, import_file8, import_file9, import_file10,
         import_file11, import_file12]
from kdc_column_files import column_groups
input_files = list(column_groups.keys())
# print(input_files)
output_file = []

# Indicate below whether you want just the 'ksdc', 'kmdc', or 'all'
# Note that if you want 'ksdc' or 'kmdc', you must include the file that has the 'multiplicity' column, as that is the indicator of
# which objects are multis and which are singles
kdc_part = "all"

for file in range(len(files)):
    if files[file]:
        print(f"Reading {input_files[file]}.parquet ...")
        df = pd.read_parquet(f"{input_files[file]}.parquet")
        df = df.drop(columns=['kdc_index','multiplicity']) if file > 0 else df
        output_file.append(df)
    else:
        continue
print("Finished reading files.")

print("Combining files...")
combined = pd.concat(output_file, axis=1, ignore_index=False)
# all_columns = combined.columns.tolist()
# print(all_columns)
if kdc_part.lower() == "all":
    pass
    
elif kdc_part.lower() == "kmdc":
    combined = combined[combined["multiplicity"]>1]
    
elif kdc_part.lower() == "ksdc":
    combined = combined[combined["multiplicity"]==1]
    
else:
    print("Please carefully type 'ksdc', 'kmdc', or 'all'.")
    raise SystemExit
print("Combined.")

# Indicate the file type you want to save the combined file as. Choose between 'csv', 'h5', or 'parquet'. NO DOTS (.)
file_type = "h5"

# Also indicate the desired filename
filename = "testing"

print("Saving file...")
if file_type.lower() == "csv":
    import pyarrow as pa
    import pyarrow.csv as ar_csv
    table = pa.Table.from_pandas(combined)
    ar_csv.write_csv(table, f"{filename}.csv")
elif file_type.lower() == "h5":
    # Convert pandas nullable extension dtypes (Int64, Float64, boolean, etc.) 
    # to plain NumPy dtypes that PyTables can handle
    for col in combined.columns:
        if pd.api.types.is_extension_array_dtype(combined[col]):
            if pd.api.types.is_string_dtype(combined[col]):
                # pandas 'string' dtype -> plain object dtype (Python str), 
                # which PyTables handles fine
                combined[col] = combined[col].astype(object)
            else:
                # Nullable numeric/boolean extension dtypes (Int64, Float64, boolean)
                combined[col] = combined[col].astype("float64")
    combined.to_hdf(f"{filename}.h5", key="kdc")
elif file_type.lower() == "parquet":
    combined.to_parquet(f"{filename}.parquet")
else:
    print("Please carefully type 'csv', 'h5', or 'parquet' with NO PERIOD (.).")
    raise SystemExit
print("Done.")