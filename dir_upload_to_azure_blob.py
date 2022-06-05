# below function can be used to upload folder and sub-folders from local to Container in Azure Blob Storage
from azure.storage.blob import BlobServiceClient
import os
# Install the following package before running this program
# pip install azure-storage-blob

def upload_data_to_adls():
    """
    Function to upload local directory to ADLS
    :return:
    """
    # Azure Storage connection string
    connect_str = ""
    # Name of the Azure container
    container_name = "data"
    # The path to be removed from the local directory path while uploading it to ADLS
    path_to_remove = "C:\\Users\\rk\\"
    # The local directory to upload to ADLS
    local_path = "C:\\Users\\rk\\test"
    
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # The below code block will iteratively traverse through the files and directories under the given folder and uploads to ADLS.
    for r, d, f in os.walk(local_path):
        print("r", r)
        print("d", d)
        print("f", f)
        if f:
            for file in f:
                file_path_on_azure = os.path.join(r, file).replace(path_to_remove, "")
                file_path_on_local = os.path.join(r, file)
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_path_on_azure)
                with open(file_path_on_local, "rb") as data:
                    blob_client.upload_blob(data)
                    print("uploading file —->", file_path_on_local)


if __name__ == '__main__':
    # invoking the upload_data_to_adls() function.
    upload_data_to_adls()
