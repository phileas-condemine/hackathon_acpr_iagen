from azure.storage.blob import BlobServiceClient
import os

# Remplacez par votre chaîne de connexion au compte de stockage Azure
connect_str = "AzureConnexion"

# Nom de votre conteneur
container_name = 'equipe-6'


# Chemin local où vous souhaitez sauvegarder le fichier téléchargé

# Initialiser le BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Accéder au conteneur
container_client = blob_service_client.get_container_client(container_name)

blobs_list = container_client.list_blobs()
for blob in blobs_list:
    # Accéder au blob et télécharger    
    download_file_path = os.path.join('RAG_AZURE/dataset', blob.name)

    blob_client = container_client.get_blob_client(blob.name)
    print(f"Téléchargement du blob vers {download_file_path}")
    #acces au contenu du du fichier que vous pouvez traiter en local classiquement
    blob_content = blob_client.download_blob().readall()
    # Télécharger le fichier warning il faut au préalable avoir écrit le fichier même vide 
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())


print("Téléchargement terminé")
