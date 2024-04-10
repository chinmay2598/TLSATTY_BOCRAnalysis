from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create Opportunities sub model
Opportunities_DLC=str.Model("DLC Inspection Plan Optimization")
#import structure and connections from Excel
input.readStructFromExcel(Opportunities_DLC,"BOCR_DLC.xlsx","Opportunities",False)
input.readConnectionsFromExcel(Opportunities_DLC,"BOCR_DLC.xlsx","OpportunitiesConnections",False)
# Opportunities_DLC.printStruct()
# Opportunities_DLC.drawGraphModel()

# input.export4ExcelQuestFull(Opportunities_DLC,"BOCR_DLC_Opportunities_empty.xlsx",True)
calc.calcAHPMatricesSave2File(Opportunities_DLC,"BOCR_DLC_Opportunities_filledin.xlsx","BOCR_DLC_Opportunities_results.xlsx")

