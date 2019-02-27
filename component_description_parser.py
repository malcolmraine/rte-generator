import xml.etree.ElementTree as ET
import component_gen
import component_main_gen
import shutil

xml_file = "component_description.xml"

rte_list = []

tree = ET.parse(xml_file)
root = tree.getroot()

component = root.find('component')
periodic_list = []
task_groups = {}
for periodic in root.find('periodics'):
    periodic_list.append([periodic.attrib['name'], periodic.attrib['period']])
    task_groups[periodic.attrib['period']] = []


for periodic in root.find('periodics'):
    temp_group = task_groups[periodic.attrib['period']]
    temp_group.append(periodic.attrib['name'])
    task_groups[periodic.attrib['period']] = temp_group


for rte in root.find('Rte_variables'):
    rte_list.append([rte.attrib['name'], rte.attrib['type']])

test2 = component_main_gen.MainComponentGen
test2.make_main_component(test2, "main", task_groups, rte_list)

comp_gen = component_gen.ComponentGen
print(comp_gen.create_periodic_definitions(comp_gen, periodic_list))
print(comp_gen.create_rte_access_abstractions(comp_gen, 'Imu', rte_list))

comp_gen.make_component(comp_gen, 'imu', periodic_list, rte_list)

# comp_gen.make_folder(comp_gen, "main")
# comp_gen.make_folder(comp_gen, "main/doc")
# comp_gen.make_folder(comp_gen, "main/include")
# comp_gen.make_folder(comp_gen, "main/source")