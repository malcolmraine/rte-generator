import xml.etree.ElementTree as ET
import component_gen
import component_main_gen
import os
import shutil


comp_gen = component_gen.ComponentGen
xml_file = "component_description.xml"


tree = ET.parse(xml_file)
root = tree.getroot()
component = root.find('component')
master_periodic_list = []
master_rte_list = []
task_groups = {}
project_path = ""

if not os.path.exists(root.attrib['name']):
    project_path = root.attrib['name']
    os.mkdir(project_path)

for component in root.findall('component'):
    periodic_list = []
    rte_list = []
    print(component.tag, "\t", component.attrib['name'])
    for periodic in component.iter('periodic'):
        periodic_list.append([periodic.attrib['name'], periodic.attrib['period']])
        master_periodic_list.append([periodic.attrib['name'], periodic.attrib['period']])

        task_groups[periodic.attrib['period']] = []

        temp_group = task_groups[periodic.attrib['period']]
        temp_group.append(periodic.attrib['name'])
        task_groups[periodic.attrib['period']] = temp_group
        print(periodic.attrib['name'])

    for var in component.iter('var'):
        rte_list.append([var.attrib['name'], var.attrib['type']])
        master_rte_list.append([var.attrib['name'], var.attrib['type']])

    print(rte_list)
    print("\n")
    comp_gen.make_component(comp_gen, component.attrib['name'], periodic_list, rte_list)

test2 = component_main_gen.MainComponentGen
test2.make_main_component(test2, "main", task_groups, master_rte_list)


print(comp_gen.create_periodic_definitions(comp_gen, periodic_list))
print(comp_gen.create_rte_access_abstractions(comp_gen, 'Imu', rte_list))
