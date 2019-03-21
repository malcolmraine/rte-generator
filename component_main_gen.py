import os
import datetime


class MainComponentGen:
    """These are simple syntax generators"""
    @staticmethod
    def ast(n):
        output = ""
        for r in range(0, n):
            output = output + "*"
        return output

    @staticmethod
    def nl(n):
        output = ""
        for r in range(0, n):
            output = output + "\n"
        return output

    @staticmethod
    def define(macro, equals_string):
        return "#define " + macro + "\t" + equals_string + "\n"

    """ These function do the heavy lifting for component generation"""
    def make_folder(self, folder_name):
        try:
            os.mkdir(folder_name)
        except OSError:
            pass

    def make_main_component(self, component_name, task_groups, rte_list):
        doc_path = component_name + "/doc"
        include_path = component_name + "/include"
        source_path = component_name + "/source"
        read_me_path = doc_path + "/" + component_name + "_Description.txt"

        self.make_folder(self, component_name)
        self.make_folder(self, doc_path)
        self.make_folder(self, include_path)
        self.make_folder(self, source_path)

        read_me = open(read_me_path, 'w+')
        read_me.close()

        self.create_main_c_file(self, source_path + "/main", 'TrackedRobotVehicle', task_groups)
        self.create_main_h_file(self, include_path + "/main", 'TrackedRobotVehicle', task_groups)
        self.create_task_group_c_file(self, source_path + "/task_groups", 'TrackedRobotVehicle', task_groups)
        self.create_task_group_h_file(self, include_path + "/task_groups", 'TrackedRobotVehicle', task_groups)
        self.create_rte_file(self, include_path + "/main", 'TrackedRobotVehicle', rte_list)

    @staticmethod
    def section_header(self, title):
        output = "/" + self.ast(88) + self.nl(1) + self.ast(1) + " " + title + self.nl(1) + self.ast(88) + "/" + self.nl(1)
        return output

    def create_main_c_file(self, file_path, component_name, task_groups):
        header = "/*\n * Generated: " + str(datetime.datetime.now())[:-7] + "\n * User: " + str(os.getlogin()) + "\n*/\n"
        file_contents = header + self.section_header(self, "HEADER FILES") + \
                        "#include " + '"' + file_path + ".h" + '"' + self.nl(1) + \
                        "#include " + '"' + "Rte_" + component_name + ".h" + '"' + self.nl(2) + \
                        self.section_header(self, "DEFINES") + self.nl(2) + \
                        self.section_header(self, "GLOBAL VARIABLES") + self.nl(2) + \
                        self.section_header(self, "FUNCTION IMPLEMENTATIONS") + \
                        self.create_task_prototypes(self, task_groups) + self.nl(2) + \
                        self.section_header(self, "END OF FILE")

        c_file = open(file_path + ".c", "w+")
        c_file.write(file_contents)
        c_file.close()

    def create_main_h_file(self, file_path, project_name, task_groups):
        header = "/*\n * Generated: " + str(datetime.datetime.now())[:-7] + "\n * User: " + str(os.getlogin()) + "\n*/"
        file_contents = header + \
                        "#ifndef " + project_name.upper() + "_MAIN_H" + self.nl(1) + \
                        "#define  " + project_name.upper() + "_MAIN_H" + self.nl(1) + \
                        self.section_header(self, "HEADER FILES") + \
                        "#include " + '"' + file_path + ".h" + '"' + self.nl(1) + \
                        "#include " + '"main/includes/task_groups.h"' + self.nl(1) + \
                        "#include " + '"main/includes/Rte.h"' + self.nl(2) + \
                        self.section_header(self, "DEFINES") + self.nl(2) + \
                        self.section_header(self, "GLOBAL VARIABLES") + self.nl(2) + \
                        self.section_header(self, "FUNCTION PROTOTYPES") + \
                        "#endif //" + project_name.upper() + "_MAIN_H" + self.nl(1) + \
                        self.section_header(self, "END OF FILE")

        h_file = open(file_path + ".h", "w+")
        h_file.write(file_contents)
        h_file.close()

    def create_task_group_c_file(self, file_path, component_name, task_groups):
        header = "/*\n * Generated: " + str(datetime.datetime.now())[:-7] + "\n * User: " + str(os.getlogin()) + "\n*/\n"
        file_contents = header + self.section_header(self, "HEADER FILES") + \
                        "#include " + '"task_groups.h"' + '"' + self.nl(1) + \
                        "#include " + '"' + "Rte_" + component_name + '.h"' + self.nl(2) + \
                        self.section_header(self, "DEFINES") + self.nl(2) + \
                        self.section_header(self, "GLOBAL VARIABLES") + self.nl(2) + \
                        self.section_header(self, "FUNCTION IMPLEMENTATIONS") + \
                        self.create_task_definitions(self, task_groups) + self.nl(2) + \
                        self.section_header(self, "END OF FILE")

        c_file = open(file_path + ".c", "w+")
        c_file.write(file_contents)
        c_file.close()

    def create_task_group_h_file(self, file_path, project_name, task_groups):
        header = "/*\n * Generated: " + str(datetime.datetime.now())[:-7] + "\n * User: " + str(os.getlogin()) + "\n*/"
        file_contents = header + \
                        "#ifndef " + project_name.upper() + "_MAIN_H" + self.nl(1) + \
                        "#define  " + project_name.upper() + "_MAIN_H" + self.nl(1) + \
                        self.section_header(self, "HEADER FILES") + \
                        self.section_header(self, "DEFINES") + self.nl(0) + \
                        "typedef void TASK;" + self.nl(1) + \
                        self.section_header(self, "GLOBAL VARIABLES") + self.nl(2) + \
                        self.section_header(self, "FUNCTION PROTOTYPES") + \
                        self.create_task_prototypes(self, task_groups) + self.nl(2) + \
                        "#endif //" + project_name.upper() + "_MAIN_H" + self.nl(1) + \
                        self.section_header(self, "END OF FILE")

        h_file = open(file_path + ".h", "w+")
        h_file.write(file_contents)
        h_file.close()

    def create_rte_file(self, file_path, project_name, rte_list):
        rte_var_string = ""
        rte_func_string = ""
        for n in range(len(rte_list)):
            rte_type = (rte_list[n])[1]
            rte_var = " Rte_" + (rte_list[n])[0]
            rte_read = rte_type + " Rte_Read_" + (rte_list[n])[0]
            rte_write = "void Rte_Write_" + (rte_list[n])[0]

            if rte_var not in rte_var_string:
                rte_var_string = rte_var_string + rte_type + rte_var + ";" + self.nl(1)
                rte_func_string = rte_func_string + "inline " + rte_read + "() { return " + rte_var + "; }\n" + \
                                  "inline " + rte_write + "(" + rte_type+ " x) {" + rte_var + " = " + "x }\n\n"

        header = "/*\n * Generated: " + str(datetime.datetime.now())[:-7] + "\n * User: " + str(os.getlogin()) + "\n*/"
        file_contents = header + \
                        "\n#ifndef " + project_name.upper() + "_RTE_H" + self.nl(1) + \
                        "#define  " + project_name.upper() + "_RTE_H" + self.nl(1) + \
                        self.section_header(self, "HEADER FILES") + self.nl(2) + \
                        self.section_header(self, "DEFINES") + self.nl(2) + \
                        self.section_header(self, "RTE VARIABLES") + self.nl(0) + \
                        rte_var_string + self.nl(1) + \
                        self.section_header(self, "RTE INTERFACE FUNCTIONS") + \
                        rte_func_string + self.nl(1) + \
                        "#endif //" + project_name.upper() + "_RTE_H" + self.nl(1) + \
                        self.section_header(self, "END OF FILE")

        h_file = open("main/include/Rte.h", "w+")
        h_file.write(file_contents)
        h_file.close()

    def create_task_definitions(self, task_groups):
        main_string = ""
        for key in task_groups:
            group = task_groups[key]
            proto_string = "/*\tTask for " + str(key) + "ms periodics\t*/\nTASK group_" + str(key) + "ms(void)\n{" + \
                           "\tfor ( ; ; )\n\t{" + self.nl(1)

            for n in range(len(group)):
                proto_string = proto_string + "\t\tvoid " + group[n] + "(void);" + self.nl(1)
            main_string = main_string + proto_string + "\t}\n}" + self.nl(3)

        return main_string

    def create_task_prototypes(self, task_groups):
        main_string = ""
        for key in task_groups:
            main_string = main_string + "TASK group_" + str(key) + "ms(void);\n"

        return main_string