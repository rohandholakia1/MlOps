

# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required

from azureml.core import Workspace, Dataset

# upload the local file to a datastore on the cloud

subscription_id = 'b3ec17a5-8d95-4801-9a7e-9ee6a85637c7'
resource_group = 'D_RG_Data_Sandbox'
workspace_name = 'dev_mls'

workspace = Workspace(subscription_id, resource_group, workspace_name)

# get the datastore to upload prepared data
datastore = workspace.get_default_datastore()

# upload the local file from src_dir to the target_path in datastore
datastore.upload(src_dir='data', target_path='data')

