# test_script.py

from BioGatewayQuery import type_data, getGene_info

# Llama a las funciones para asegurarte de que funcionan correctamente
# Asegúrate de tener algunos datos de prueba para pasar a las funciones
test_instance = "TOX3"
gene = "TOX3"
taxon = "9606"

print(type_data(test_instance))
print(getGene_info(gene, taxon))