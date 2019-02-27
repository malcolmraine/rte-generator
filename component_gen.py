import os
import datetime

class ComponentGen:

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


    def make_component(self, component_name, periodics_list, rte_list):
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

        self.create_c_file(self, source_path + "/" + component_name, component_name, periodics_list)
        self.create_h_file(self, include_path + "/" + component_name, component_name, 'TrackedRobotVehicle', periodics_list)
        self.create_rte_file(self, include_path + "/" + component_name, component_name, 'TrackedRobotVehicle', rte_list)



    @staticmethod
    def section_header(self, title):
        output = "/" + self.ast(88) + self.nl(1) + self.ast(1) + " " + title + self.nl(1) + self.ast(88) + "/" + self.nl(1)
        return output

    def create_c_file(self, file_path, component_name, periodics_list):
        header = "/*\n * Generated: " + str(datetime.datetime.now())[:-7] + "\n * User: " + str(os.getlogin()) + "\n*/\n"
        file_contents = header + self.section_header(self, "HEADER FILES") + \
                        "#include " + '"' + file_path + ".h" + '"' + self.nl(1) + \
                        "#include " + '"' + "Rte_" + component_name + ".h" + '"' + self.nl(2) + \
                        self.section_header(self, "DEFINES") + self.nl(2) + \
                        self.section_header(self, "GLOBAL VARIABLES") + self.nl(2) + \
                        self.section_header(self, "FUNCTION IMPLEMENTATIONS") + \
                        self.create_periodic_definitions(self, periodics_list) + self.nl(2) + \
                        self.section_header(self, "END OF FILE")

        c_file = open(file_path + ".c", "w+")
        c_file.write(file_contents)
        c_file.close()


    def create_h_file(self, file_path, component_name, project_name, periodics_list):
        header = "/*\n * Generated: " + str(datetime.datetime.now())[:-7] + "\n * User: " + str(os.getlogin()) + "\n*/"
        file_contents = header + \
                        "#ifndef " + project_name.upper() + "_" + component_name.upper() + "_H" + self.nl(1) + \
                        "#define  " + project_name.upper() + "_" + component_name.upper() + "_H" + self.nl(1) + \
                        self.section_header(self, "HEADER FILES") + \
                        "#include " + '"' + file_path + ".h" + '"' + self.nl(2) + \
                        self.section_header(self, "DEFINES") + self.nl(2) + \
                        self.section_header(self, "GLOBAL VARIABLES") + self.nl(2) + \
                        self.section_header(self, "FUNCTION PROTOTYPES") + \
                        self.create_periodic_prototypes(self, periodics_list) + self.nl(2) + \
                        "#endif //" + project_name.upper() + "_" + component_name.upper() + "_H" + self.nl(1) + \
                        self.section_header(self, "END OF FILE")

        h_file = open(file_path + ".h", "w+")
        h_file.write(file_contents)
        h_file.close()

    def create_rte_file(self, file_path, component_name, project_name, rte_list):
        header = "/*\n * Generated: " + str(datetime.datetime.now())[:-7] + "\n * User: " + str(os.getlogin()) + "\n*/"
        file_contents = header + \
                        "\n#ifndef " + project_name.upper() + "_RTE_" + component_name.upper() + "_H" + self.nl(1) + \
                        "#define  " + project_name.upper() + "_RTE_" + component_name.upper() + "_H" + self.nl(1) + \
                        self.section_header(self, "HEADER FILES") + self.nl(0) + \
                        "#include " + '"main/include/Rte.h"' + self.nl(2) + \
                        self.section_header(self, "DEFINES") + self.nl(0) + \
                        self.create_rte_access_abstractions(self, component_name, rte_list) + self.nl(2) + \
                        "#endif //" + project_name.upper() + "_" + component_name.upper() + "_H" + self.nl(1) + \
                        self.section_header(self, "END OF FILE")

        h_file = open(component_name + "/include/Rte_" + component_name + ".h", "w+")
        h_file.write(file_contents)
        h_file.close()


    def create_rte_access_abstractions(self, component_name, rte_list):
        main_string = ""

        for n in range(len(rte_list)):
            #self.define("Rte_Read_" + component_name + "_" + rte_list[n] + "()", "Rte_Read_" + rte_list[n] + "()")

            # main_string = main_string + "#define Rte_Read_" + component_name + "_" + rte_list[n] + "()\t\t\tRte_Read_" + rte_list[n] + \
            #     "()\n" + "#define Rte_Write_" + component_name + "_" + rte_list[n] + "(x)\t\t\tRte_Write_" + rte_list[n] + "(x)\n"

            macro_read = "Rte_Read_" + component_name + "_" + (rte_list[n])[0] + "()"
            equals_string_read = "Rte_Read_" + (rte_list[n])[0] + "()"
            macro_write = "Rte_Write_" + component_name + "_" + (rte_list[n])[0] + "(x)"
            equals_string_write = "Rte_Write_" + (rte_list[n])[0] + "(x)"

            main_string = main_string + self.define(macro_read, equals_string_read) + \
                                        self.define(macro_write, equals_string_write)

        return main_string

    def create_periodic_definitions(self, periodics_list):
        main_string = ""
        for n in range(len(periodics_list)):
            proto_string = "void " + (periodics_list[n])[0] + "(void)\n{" + self.nl(1) + \
                        "\t/*\tBegin local variables\t*/\n\n\t/*\tEnd local variables\t*/" + self.nl(3) + "}" + self.nl(3)
            main_string = main_string + proto_string

        return main_string

    def create_periodic_prototypes(self, periodics_list):
        main_string = ""
        for n in range(len(periodics_list)):
            proto_string = "void " + (periodics_list[n])[0] + "( void );" + self.nl(1)
            main_string = main_string + proto_string

        return main_string
