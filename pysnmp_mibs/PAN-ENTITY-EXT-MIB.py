_O='panEntityMIBPowerSupplyGroup'
_N='panEntityMIBFanTrayGroup'
_M='panEntityMIBFRUModuleGroup'
_L='panEntityMIBChassisGroup'
_K='panEntryPowerSupplyPowerCapacity'
_J='panEntryFanTrayPowerUsed'
_I='panEntryFRUModuleNumPorts'
_H='panEntryFRUModulePowerUsed'
_G='panEntityTotalPowerUsed'
_F='panEntityTotalPowerAvail'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='PAN-ENTITY-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
panModules,=mibBuilder.importSymbols('PAN-GLOBAL-REG','panModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
panEntityMIBModule=ModuleIdentity((1,3,6,1,4,1,25461,1,1,7))
if mibBuilder.loadTexts:panEntityMIBModule.setRevisions(('2012-11-05 11:06',))
_PanEntityMIBObjects_ObjectIdentity=ObjectIdentity
panEntityMIBObjects=_PanEntityMIBObjects_ObjectIdentity((1,3,6,1,4,1,25461,1,1,7,1))
_PanEntityChassisGroup_ObjectIdentity=ObjectIdentity
panEntityChassisGroup=_PanEntityChassisGroup_ObjectIdentity((1,3,6,1,4,1,25461,1,1,7,1,1))
if mibBuilder.loadTexts:panEntityChassisGroup.setStatus(_A)
_PanEntityTotalPowerAvail_Type=Integer32
_PanEntityTotalPowerAvail_Object=MibScalar
panEntityTotalPowerAvail=_PanEntityTotalPowerAvail_Object((1,3,6,1,4,1,25461,1,1,7,1,1,1),_PanEntityTotalPowerAvail_Type())
panEntityTotalPowerAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:panEntityTotalPowerAvail.setStatus(_A)
_PanEntityTotalPowerUsed_Type=Integer32
_PanEntityTotalPowerUsed_Object=MibScalar
panEntityTotalPowerUsed=_PanEntityTotalPowerUsed_Object((1,3,6,1,4,1,25461,1,1,7,1,1,2),_PanEntityTotalPowerUsed_Type())
panEntityTotalPowerUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:panEntityTotalPowerUsed.setStatus(_A)
_PanEntityFRUModuleGroup_ObjectIdentity=ObjectIdentity
panEntityFRUModuleGroup=_PanEntityFRUModuleGroup_ObjectIdentity((1,3,6,1,4,1,25461,1,1,7,1,2))
if mibBuilder.loadTexts:panEntityFRUModuleGroup.setStatus(_A)
_PanEntityFRUModuleTable_Object=MibTable
panEntityFRUModuleTable=_PanEntityFRUModuleTable_Object((1,3,6,1,4,1,25461,1,1,7,1,2,1))
if mibBuilder.loadTexts:panEntityFRUModuleTable.setStatus(_A)
_PanEntityFRUModuleEntry_Object=MibTableRow
panEntityFRUModuleEntry=_PanEntityFRUModuleEntry_Object((1,3,6,1,4,1,25461,1,1,7,1,2,1,1))
panEntityFRUModuleEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:panEntityFRUModuleEntry.setStatus(_A)
_PanEntryFRUModulePowerUsed_Type=Integer32
_PanEntryFRUModulePowerUsed_Object=MibTableColumn
panEntryFRUModulePowerUsed=_PanEntryFRUModulePowerUsed_Object((1,3,6,1,4,1,25461,1,1,7,1,2,1,1,1),_PanEntryFRUModulePowerUsed_Type())
panEntryFRUModulePowerUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:panEntryFRUModulePowerUsed.setStatus(_A)
_PanEntryFRUModuleNumPorts_Type=Integer32
_PanEntryFRUModuleNumPorts_Object=MibTableColumn
panEntryFRUModuleNumPorts=_PanEntryFRUModuleNumPorts_Object((1,3,6,1,4,1,25461,1,1,7,1,2,1,1,2),_PanEntryFRUModuleNumPorts_Type())
panEntryFRUModuleNumPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:panEntryFRUModuleNumPorts.setStatus(_A)
_PanEntityFanTrayGroup_ObjectIdentity=ObjectIdentity
panEntityFanTrayGroup=_PanEntityFanTrayGroup_ObjectIdentity((1,3,6,1,4,1,25461,1,1,7,1,3))
if mibBuilder.loadTexts:panEntityFanTrayGroup.setStatus(_A)
_PanEntityFanTrayTable_Object=MibTable
panEntityFanTrayTable=_PanEntityFanTrayTable_Object((1,3,6,1,4,1,25461,1,1,7,1,3,1))
if mibBuilder.loadTexts:panEntityFanTrayTable.setStatus(_A)
_PanEntityFanTrayEntry_Object=MibTableRow
panEntityFanTrayEntry=_PanEntityFanTrayEntry_Object((1,3,6,1,4,1,25461,1,1,7,1,3,1,1))
panEntityFanTrayEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:panEntityFanTrayEntry.setStatus(_A)
_PanEntryFanTrayPowerUsed_Type=Integer32
_PanEntryFanTrayPowerUsed_Object=MibTableColumn
panEntryFanTrayPowerUsed=_PanEntryFanTrayPowerUsed_Object((1,3,6,1,4,1,25461,1,1,7,1,3,1,1,1),_PanEntryFanTrayPowerUsed_Type())
panEntryFanTrayPowerUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:panEntryFanTrayPowerUsed.setStatus(_A)
_PanEntityPowerSupplyGroup_ObjectIdentity=ObjectIdentity
panEntityPowerSupplyGroup=_PanEntityPowerSupplyGroup_ObjectIdentity((1,3,6,1,4,1,25461,1,1,7,1,4))
if mibBuilder.loadTexts:panEntityPowerSupplyGroup.setStatus(_A)
_PanEntityPowerSupplyTable_Object=MibTable
panEntityPowerSupplyTable=_PanEntityPowerSupplyTable_Object((1,3,6,1,4,1,25461,1,1,7,1,4,1))
if mibBuilder.loadTexts:panEntityPowerSupplyTable.setStatus(_A)
_PanEntityPowerSupplyEntry_Object=MibTableRow
panEntityPowerSupplyEntry=_PanEntityPowerSupplyEntry_Object((1,3,6,1,4,1,25461,1,1,7,1,4,1,1))
panEntityPowerSupplyEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:panEntityPowerSupplyEntry.setStatus(_A)
_PanEntryPowerSupplyPowerCapacity_Type=Integer32
_PanEntryPowerSupplyPowerCapacity_Object=MibTableColumn
panEntryPowerSupplyPowerCapacity=_PanEntryPowerSupplyPowerCapacity_Object((1,3,6,1,4,1,25461,1,1,7,1,4,1,1,1),_PanEntryPowerSupplyPowerCapacity_Type())
panEntryPowerSupplyPowerCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:panEntryPowerSupplyPowerCapacity.setStatus(_A)
_PanEntityMIBConformance_ObjectIdentity=ObjectIdentity
panEntityMIBConformance=_PanEntityMIBConformance_ObjectIdentity((1,3,6,1,4,1,25461,1,1,7,2))
_PanEntityMIBCompliances_ObjectIdentity=ObjectIdentity
panEntityMIBCompliances=_PanEntityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,25461,1,1,7,2,1))
_PanEntityMIBGroups_ObjectIdentity=ObjectIdentity
panEntityMIBGroups=_PanEntityMIBGroups_ObjectIdentity((1,3,6,1,4,1,25461,1,1,7,2,2))
panEntityMIBChassisGroup=ObjectGroup((1,3,6,1,4,1,25461,1,1,7,2,2,1))
panEntityMIBChassisGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:panEntityMIBChassisGroup.setStatus(_A)
panEntityMIBFRUModuleGroup=ObjectGroup((1,3,6,1,4,1,25461,1,1,7,2,2,2))
panEntityMIBFRUModuleGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:panEntityMIBFRUModuleGroup.setStatus(_A)
panEntityMIBFanTrayGroup=ObjectGroup((1,3,6,1,4,1,25461,1,1,7,2,2,3))
panEntityMIBFanTrayGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:panEntityMIBFanTrayGroup.setStatus(_A)
panEntityMIBPowerSupplyGroup=ObjectGroup((1,3,6,1,4,1,25461,1,1,7,2,2,4))
panEntityMIBPowerSupplyGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:panEntityMIBPowerSupplyGroup.setStatus(_A)
panEntityMIBCompliance=ModuleCompliance((1,3,6,1,4,1,25461,1,1,7,2,1,1))
panEntityMIBCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:panEntityMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'panEntityMIBModule':panEntityMIBModule,'panEntityMIBObjects':panEntityMIBObjects,'panEntityChassisGroup':panEntityChassisGroup,_F:panEntityTotalPowerAvail,_G:panEntityTotalPowerUsed,'panEntityFRUModuleGroup':panEntityFRUModuleGroup,'panEntityFRUModuleTable':panEntityFRUModuleTable,'panEntityFRUModuleEntry':panEntityFRUModuleEntry,_H:panEntryFRUModulePowerUsed,_I:panEntryFRUModuleNumPorts,'panEntityFanTrayGroup':panEntityFanTrayGroup,'panEntityFanTrayTable':panEntityFanTrayTable,'panEntityFanTrayEntry':panEntityFanTrayEntry,_J:panEntryFanTrayPowerUsed,'panEntityPowerSupplyGroup':panEntityPowerSupplyGroup,'panEntityPowerSupplyTable':panEntityPowerSupplyTable,'panEntityPowerSupplyEntry':panEntityPowerSupplyEntry,_K:panEntryPowerSupplyPowerCapacity,'panEntityMIBConformance':panEntityMIBConformance,'panEntityMIBCompliances':panEntityMIBCompliances,'panEntityMIBCompliance':panEntityMIBCompliance,'panEntityMIBGroups':panEntityMIBGroups,_L:panEntityMIBChassisGroup,_M:panEntityMIBFRUModuleGroup,_N:panEntityMIBFanTrayGroup,_O:panEntityMIBPowerSupplyGroup})