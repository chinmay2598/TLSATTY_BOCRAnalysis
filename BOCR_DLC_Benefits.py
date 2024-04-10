from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create Opportunities sub model
Benefits_DLC=str.Model("DLC Inspection Plan Optimization")
#import structure and connections from Excel
input.readStructFromExcel(Benefits_DLC,"BOCR_DLC.xlsx","Benefits",False)
input.readConnectionsFromExcel(Benefits_DLC,"BOCR_DLC.xlsx","BenefitsConnections",False)
# Benefits_DLC.printStruct()
# Benefits_DLC.drawGraphModel()

#input.export4ExcelQuestFull(Benefits_DLC,"BOCR_DLC_Benefits_empty.xlsx",True)
calc.calcAHPMatricesSave2File(Benefits_DLC,"BOCR_DLC_Benefits_filledin.xlsx","BOCR_DLC_Benefits_results.xlsx")

