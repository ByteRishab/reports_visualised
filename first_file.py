from xml.etree.ElementTree import Element as E, tostring
from xml.dom import minidom
# from second_level import ReportSections
class Report:
    def __init__(self):
        self.reportsections = None  # Will be set by ReportSections
        self.rprtprmtrsl = ReportParametersLayout()
        self.rprtu = ReportUnitType()
        self.pgu = PageUnit()
        self.dfltfam = DefaultFontFamily()
        #  here we make the static 

    def to_xml(self):
        report = E("Report")
        report.attrib = {
            "xmlns:rd": "http://schemas.microsoft.com/SQLServer/reporting/reportdesigner",
            "xmlns:df": "http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition/defaultfontfamily",
            "xmlns": "http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition"
        }
        if self.reportsections:
            report.append(self.reportsections.to_xml())
        report.append(self.rprtprmtrsl.to_xml())
        report.append(self.rprtu.to_xml())
        report.append(self.pgu.to_xml())
        report.append(self.dfltfam.to_xml())
        return report

class ReportSections:
    def __init__(self, report=None):
        if report is None:
            self.report = Report()
            self.report.reportsections = self
        else:
            self.report = report
        self.reportsection = None  # Will be set by ReportSection

    def to_xml(self):
        reportsections = E("ReportSections")
        if self.reportsection:
            reportsections.append(self.reportsection.to_xml())
        return reportsections
    
    def get_report(self):
        return self.report



class ReportParametersLayout:
    def __init__(self): pass
    def to_xml(self):
        return E("ReportParametersLayout")

class ReportUnitType:
    def __init__(self): pass
    def to_xml(self):
        rprtu = E("rd:ReportUnitType")
        rprtu.text = "Inch"
        return rprtu

class PageUnit:
    def __init__(self): pass
    def to_xml(self):
        pgu = E("rd:PageUnit")
        pgu.text = "Px"
        return pgu

class DefaultFontFamily:
    def __init__(self): pass
    def to_xml(self):
        dfltfam = E("df:DefaultFontFamily")
        dfltfam.text = "Segoe UI"
        return dfltfam

def pretty_xml(elem):
    rough_string = tostring(elem, encoding='utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ", encoding='utf-8').decode('utf-8')



class ReportSection:
    def __init__(self, reportsections=None):
        if reportsections is None:
            self.reportsections = ReportSections()
            self.reportsections.reportsection = self
        else:
            self.reportsections = reportsections
        self.body = None
        self.page = E("Page")
        self.width = E("Width")
        self.width.text = "6.5in"

    def to_xml(self):
        reportsection = E("ReportSection")
        reportsection.append(self.body.to_xml())
        reportsection.append(self.page)
        reportsection.append(self.width)
        return reportsection
    
    def get_report(self):
        return self.reportsections.get_report()


class Body:
    def __init__(self, body_hieght=3.25, reportsection=None):
        if reportsection is None:
            self.reportsection = ReportSection()
            self.reportsection.body = self
        else:
            self.reportsection = reportsection
        self.hieght = E("Height")
        self.hieght.text = f"{body_hieght}in"
        self.reportitems = None
        self.style = E("Style")
    def to_xml(self):
        body = E("Body")
        body.append(self.hieght)


        if self.reportitems:
            body.append(self.reportitems.to_xml())
        body.append(self.style)
        return body
    def get_report(self):
        return self.reportsection.get_report()


xmlreport = Body()
report = xmlreport.get_report()
print(pretty_xml(report.to_xml()))
