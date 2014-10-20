# -*- coding: utf-8 -*-
import xlsxwriter


class ExportXls:

    def __init__(self, iface, fileName, settings, profiles, hekto, attribs, decimalDelimiter):
        self.iface = iface
        self.fileName = fileName
        self.settings = settings
        self.profiles = profiles
        self.hekto = hekto
        self.attribs = attribs
        self.decimalDelimiter = decimalDelimiter

    def create(self):
        # XLSX-Datei zusaetzlich zur CSV-Datei speichern
        fileNameXlsx = '{0}.xlsx'.format(self.fileName)
        workbook = xlsxwriter.Workbook(fileNameXlsx)

        worksheet_1 = workbook.add_worksheet('Data')
        worksheet_1.set_paper(9)                        # A4
        worksheet_1.set_column('A:AL', 15)              # Spalten breiter machen

        worksheet_2 = workbook.add_worksheet('Diagram')
        worksheet_2.set_paper(9)                        # A4

        format_center = workbook.add_format()
        format_center.set_align('center')
        format_float = workbook.add_format()
        format_float.set_align('right')
        format_float.set_num_format('0.00')
        format_nofloat = workbook.add_format()
        format_nofloat.set_align('right')
        format_nofloat.set_num_format('0')

        row = 0
        col = 0
        profilspalte = 0

        header = self.profiles[0].writeArrayHeader(self.settings.mapData.rasters.selectedRasters(),
                                                   self.hekto,
                                                   self.attribs)
        for kopfspalte in header:
            worksheet_1.write(row, col, kopfspalte, format_center)

            if kopfspalte == "Profilenumber":
                profilspalte = col

            col += 1

        row = 1
        col = 0
        previous_profile = 1

        profiles = []
        lines = []

        #TODO: aus profilspalte diagram_spalte erzeugen!
        diagram_spalte = "E"
        line_beginn = 1

        for profil in self.profiles:
            profilArray = profil.toArray(self.hekto, self.attribs, self.decimalDelimiter)
            profiles.append(profilArray)

            spalte = 0

            for segmente in profilArray:
                for vertex in segmente:
                    for eigenschaft in vertex:
                        if self.XlsFormat_NoFloat(header, spalte):
                            worksheet_1.write(row, col + spalte, eigenschaft, format_nofloat)
                        else:
                            worksheet_1.write(row, col + spalte, eigenschaft, format_float)

                        if spalte == profilspalte:
                            profile_ID = eigenschaft

                            if profile_ID == previous_profile:
                                previous_profile = eigenschaft
                            else:
                                lines.append('Data!${0}${1}:${0}${2}'.format(diagram_spalte,
                                                                             line_beginn,
                                                                             row))
                                line_beginn = row + 1
                                previous_profile = eigenschaft

                        spalte += 1

                        if spalte >= len(vertex):
                            spalte = 0
                            row += 1

        self.CreateXlsDiagram(workbook, worksheet_2, lines, "DTM")

        workbook.close()

    def CreateXlsDiagram(self, workbook, worksheet, lines, raster):
        if 1 == 2:
            return

        chart = workbook.add_chart({'type': 'line'})

        for line in lines:
            chart.add_series({
                'values':   line
            })

        worksheet.insert_chart('B23', chart)

    def XlsFormat_NoFloat(self, header, spalte):
        nofloat = False
        if header[spalte] == "Profilenumber":
            nofloat = True
        elif header[spalte] == "Segmentnumber":
            nofloat = True
        elif header[spalte] == "Pointnumber":
            nofloat = True
        return nofloat