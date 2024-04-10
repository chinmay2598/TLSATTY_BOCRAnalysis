from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create Costs sub model
Costs_DLC=str.Model("DLC Inspection Plan Optimization")
#import structure and connections from Excel
input.readStructFromExcel(Costs_DLC,"BOCR_DLC.xlsx","Costs",False)
input.readConnectionsFromExcel(Costs_DLC,"BOCR_DLC.xlsx","CostsConnections",False)
# Costs_DLC.printStruct()
# Costs_DLC.drawGraphModel()

# input.export4ExcelQuestFull(Costs_DLC,"BOCR_DLC_Costs_empty.xlsx",True)
calc.calcAHPMatricesSave2File(Costs_DLC,"BOCR_DLC_Costs_filledin.xlsx","BOCR_DLC_Costs_results.xlsx")
