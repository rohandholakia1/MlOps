
# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required

from azureml.core import Workspace, Dataset

# upload the local file to a datastore on the cloud

subscription_id = 'b3ec17a5-8d95-4801-9a7e-9ee6a85637c7'
resource_group = 'D_RG_Data_Sandbox'
workspace_name = 'dev_mls'

workspace = Workspace(subscription_id, resource_group, workspace_name)

print(workspace)

# get the datastore to upload prepared data
datastore = workspace.get_default_datastore()



local_path = "C:\\Users\\rdholakia\\Documents\\Project\\MLOpsVector\\MlOps\\data"
# upload the local file from src_dir to the target_path in datastore
datastore.upload(src_dir=local_path, target_path='vector_data')



dataset = Dataset.Tabular.from_delimited_files(path =[(datastore, ('vector_data/IndexationValuesSQL.csv'))])
dataset = dataset.register(workspace = workspace,
                           name = 'vector_indexation_values_sql')









# List all datastores registered in the current workspace
datastores = workspace.datastores
for name, datastore in datastores.items():
    print(name, datastore.datastore_type)
    
    
vector_ds = vector_ds.register(workspace=workspace,
                                 name='vector_ds',
                                 description='vector training data')




from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = <connectionstring>
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_name="dummy"
container_client=blob_service_client.get_container_client(container_name)

blob_list = container_client.list_blobs(name_starts_with="dir1/")
for blob in blob_list:
print("\t" + blob.name)