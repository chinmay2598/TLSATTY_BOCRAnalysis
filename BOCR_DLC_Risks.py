from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create Risks sub model
Risks_DLC=str.Model("DLC Inspection Plan Optimization")
#import structure and connections from Excel
input.readStructFromExcel(Risks_DLC,"BOCR_DLC.xlsx","Risks",False)
input.readConnectionsFromExcel(Risks_DLC,"BOCR_DLC.xlsx","RisksConnections",False)
# Risks_DLC.printStruct()
# Risks_DLC.drawGraphModel()

# input.export4ExcelQuestFull(Risks_DLC,"BOCR_DLC_Risks_empty.xlsx",True)
calc.calcAHPMatricesSave2File(Risks_DLC,"BOCR_DLC_Risks_filledin.xlsx","BOCR_DLC_Risks_results.xlsx")