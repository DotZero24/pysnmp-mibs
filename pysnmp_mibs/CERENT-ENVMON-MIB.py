_S='cerentEnvMonMibObjectsGroup'
_R='cerentEnvMonTemperatureStatsThresholdHigh'
_Q='cerentEnvMonTemperatureStatsCurrentValue'
_P='cerentEnvMonTemperatureStatsDescr'
_O='cerentEnvMonVoltageStatsThresholdVeryLow'
_N='cerentEnvMonVoltageStatsThresholdLow'
_M='cerentEnvMonVoltageStatsThresholdHigh'
_L='cerentEnvMonVoltageStatsThresholdVeryHigh'
_K='cerentEnvMonVoltageStatsCurrentValue'
_J='cerentEnvMonVoltageStatsDescr'
_I='Degree Celsius'
_H='cerentEnvMonTemperatureStatsIndex'
_G='not-accessible'
_F='cerentEnvMonVoltageStatsIndex'
_E='Integer32'
_D='millivolts'
_C='read-only'
_B='CERENT-ENVMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cerentGeneric,cerentModules,cerentRequirements=mibBuilder.importSymbols('CERENT-GLOBAL-REGISTRY','cerentGeneric','cerentModules','cerentRequirements')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cerentEnvMonMIB=ModuleIdentity((1,3,6,1,4,1,3607,1,10,120))
if mibBuilder.loadTexts:cerentEnvMonMIB.setRevisions(('2004-01-27 14:51',))
_CerentEnvMonObjects_ObjectIdentity=ObjectIdentity
cerentEnvMonObjects=_CerentEnvMonObjects_ObjectIdentity((1,3,6,1,4,1,3607,2,80))
if mibBuilder.loadTexts:cerentEnvMonObjects.setStatus(_A)
_CerentEnvMonVoltageStatsTable_Object=MibTable
cerentEnvMonVoltageStatsTable=_CerentEnvMonVoltageStatsTable_Object((1,3,6,1,4,1,3607,2,80,10))
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsTable.setStatus(_A)
_CerentEnvMonVoltageStatsEntry_Object=MibTableRow
cerentEnvMonVoltageStatsEntry=_CerentEnvMonVoltageStatsEntry_Object((1,3,6,1,4,1,3607,2,80,10,1))
cerentEnvMonVoltageStatsEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsEntry.setStatus(_A)
class _CerentEnvMonVoltageStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CerentEnvMonVoltageStatsIndex_Type.__name__=_E
_CerentEnvMonVoltageStatsIndex_Object=MibTableColumn
cerentEnvMonVoltageStatsIndex=_CerentEnvMonVoltageStatsIndex_Object((1,3,6,1,4,1,3607,2,80,10,1,10),_CerentEnvMonVoltageStatsIndex_Type())
cerentEnvMonVoltageStatsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsIndex.setStatus(_A)
_CerentEnvMonVoltageStatsDescr_Type=DisplayString
_CerentEnvMonVoltageStatsDescr_Object=MibTableColumn
cerentEnvMonVoltageStatsDescr=_CerentEnvMonVoltageStatsDescr_Object((1,3,6,1,4,1,3607,2,80,10,1,20),_CerentEnvMonVoltageStatsDescr_Type())
cerentEnvMonVoltageStatsDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsDescr.setStatus(_A)
_CerentEnvMonVoltageStatsCurrentValue_Type=Integer32
_CerentEnvMonVoltageStatsCurrentValue_Object=MibTableColumn
cerentEnvMonVoltageStatsCurrentValue=_CerentEnvMonVoltageStatsCurrentValue_Object((1,3,6,1,4,1,3607,2,80,10,1,30),_CerentEnvMonVoltageStatsCurrentValue_Type())
cerentEnvMonVoltageStatsCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsCurrentValue.setStatus(_A)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsCurrentValue.setUnits(_D)
_CerentEnvMonVoltageStatsThresholdVeryHigh_Type=Integer32
_CerentEnvMonVoltageStatsThresholdVeryHigh_Object=MibTableColumn
cerentEnvMonVoltageStatsThresholdVeryHigh=_CerentEnvMonVoltageStatsThresholdVeryHigh_Object((1,3,6,1,4,1,3607,2,80,10,1,40),_CerentEnvMonVoltageStatsThresholdVeryHigh_Type())
cerentEnvMonVoltageStatsThresholdVeryHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsThresholdVeryHigh.setStatus(_A)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsThresholdVeryHigh.setUnits(_D)
_CerentEnvMonVoltageStatsThresholdHigh_Type=Integer32
_CerentEnvMonVoltageStatsThresholdHigh_Object=MibTableColumn
cerentEnvMonVoltageStatsThresholdHigh=_CerentEnvMonVoltageStatsThresholdHigh_Object((1,3,6,1,4,1,3607,2,80,10,1,50),_CerentEnvMonVoltageStatsThresholdHigh_Type())
cerentEnvMonVoltageStatsThresholdHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsThresholdHigh.setStatus(_A)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsThresholdHigh.setUnits(_D)
_CerentEnvMonVoltageStatsThresholdLow_Type=Integer32
_CerentEnvMonVoltageStatsThresholdLow_Object=MibTableColumn
cerentEnvMonVoltageStatsThresholdLow=_CerentEnvMonVoltageStatsThresholdLow_Object((1,3,6,1,4,1,3607,2,80,10,1,60),_CerentEnvMonVoltageStatsThresholdLow_Type())
cerentEnvMonVoltageStatsThresholdLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsThresholdLow.setStatus(_A)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsThresholdLow.setUnits(_D)
_CerentEnvMonVoltageStatsThresholdVeryLow_Type=Integer32
_CerentEnvMonVoltageStatsThresholdVeryLow_Object=MibTableColumn
cerentEnvMonVoltageStatsThresholdVeryLow=_CerentEnvMonVoltageStatsThresholdVeryLow_Object((1,3,6,1,4,1,3607,2,80,10,1,70),_CerentEnvMonVoltageStatsThresholdVeryLow_Type())
cerentEnvMonVoltageStatsThresholdVeryLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsThresholdVeryLow.setStatus(_A)
if mibBuilder.loadTexts:cerentEnvMonVoltageStatsThresholdVeryLow.setUnits(_D)
_CerentEnvMonTemperatureStatsTable_Object=MibTable
cerentEnvMonTemperatureStatsTable=_CerentEnvMonTemperatureStatsTable_Object((1,3,6,1,4,1,3607,2,80,20))
if mibBuilder.loadTexts:cerentEnvMonTemperatureStatsTable.setStatus(_A)
_CerentEnvMonTemperatureStatsEntry_Object=MibTableRow
cerentEnvMonTemperatureStatsEntry=_CerentEnvMonTemperatureStatsEntry_Object((1,3,6,1,4,1,3607,2,80,20,1))
cerentEnvMonTemperatureStatsEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cerentEnvMonTemperatureStatsEntry.setStatus(_A)
class _CerentEnvMonTemperatureStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CerentEnvMonTemperatureStatsIndex_Type.__name__=_E
_CerentEnvMonTemperatureStatsIndex_Object=MibTableColumn
cerentEnvMonTemperatureStatsIndex=_CerentEnvMonTemperatureStatsIndex_Object((1,3,6,1,4,1,3607,2,80,20,1,10),_CerentEnvMonTemperatureStatsIndex_Type())
cerentEnvMonTemperatureStatsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cerentEnvMonTemperatureStatsIndex.setStatus(_A)
_CerentEnvMonTemperatureStatsDescr_Type=DisplayString
_CerentEnvMonTemperatureStatsDescr_Object=MibTableColumn
cerentEnvMonTemperatureStatsDescr=_CerentEnvMonTemperatureStatsDescr_Object((1,3,6,1,4,1,3607,2,80,20,1,20),_CerentEnvMonTemperatureStatsDescr_Type())
cerentEnvMonTemperatureStatsDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonTemperatureStatsDescr.setStatus(_A)
_CerentEnvMonTemperatureStatsCurrentValue_Type=Gauge32
_CerentEnvMonTemperatureStatsCurrentValue_Object=MibTableColumn
cerentEnvMonTemperatureStatsCurrentValue=_CerentEnvMonTemperatureStatsCurrentValue_Object((1,3,6,1,4,1,3607,2,80,20,1,30),_CerentEnvMonTemperatureStatsCurrentValue_Type())
cerentEnvMonTemperatureStatsCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonTemperatureStatsCurrentValue.setStatus(_A)
if mibBuilder.loadTexts:cerentEnvMonTemperatureStatsCurrentValue.setUnits(_I)
_CerentEnvMonTemperatureStatsThresholdHigh_Type=Gauge32
_CerentEnvMonTemperatureStatsThresholdHigh_Object=MibTableColumn
cerentEnvMonTemperatureStatsThresholdHigh=_CerentEnvMonTemperatureStatsThresholdHigh_Object((1,3,6,1,4,1,3607,2,80,20,1,40),_CerentEnvMonTemperatureStatsThresholdHigh_Type())
cerentEnvMonTemperatureStatsThresholdHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentEnvMonTemperatureStatsThresholdHigh.setStatus(_A)
if mibBuilder.loadTexts:cerentEnvMonTemperatureStatsThresholdHigh.setUnits(_I)
_CerentEnvMonMibConformance_ObjectIdentity=ObjectIdentity
cerentEnvMonMibConformance=_CerentEnvMonMibConformance_ObjectIdentity((1,3,6,1,4,1,3607,5,70))
if mibBuilder.loadTexts:cerentEnvMonMibConformance.setStatus(_A)
_CerentEnvMonMibCompliance_ObjectIdentity=ObjectIdentity
cerentEnvMonMibCompliance=_CerentEnvMonMibCompliance_ObjectIdentity((1,3,6,1,4,1,3607,5,70,10))
if mibBuilder.loadTexts:cerentEnvMonMibCompliance.setStatus(_A)
_CerentEnvMonMibGroups_ObjectIdentity=ObjectIdentity
cerentEnvMonMibGroups=_CerentEnvMonMibGroups_ObjectIdentity((1,3,6,1,4,1,3607,5,70,20))
if mibBuilder.loadTexts:cerentEnvMonMibGroups.setStatus(_A)
cerentEnvMonMibObjectsGroup=ObjectGroup((1,3,6,1,4,1,3607,5,70,20,10))
cerentEnvMonMibObjectsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cerentEnvMonMibObjectsGroup.setStatus(_A)
cerentEnvMonMibBasicCompliance=ModuleCompliance((1,3,6,1,4,1,3607,5,70,10,10))
cerentEnvMonMibBasicCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:cerentEnvMonMibBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cerentEnvMonMIB':cerentEnvMonMIB,'cerentEnvMonObjects':cerentEnvMonObjects,'cerentEnvMonVoltageStatsTable':cerentEnvMonVoltageStatsTable,'cerentEnvMonVoltageStatsEntry':cerentEnvMonVoltageStatsEntry,_F:cerentEnvMonVoltageStatsIndex,_J:cerentEnvMonVoltageStatsDescr,_K:cerentEnvMonVoltageStatsCurrentValue,_L:cerentEnvMonVoltageStatsThresholdVeryHigh,_M:cerentEnvMonVoltageStatsThresholdHigh,_N:cerentEnvMonVoltageStatsThresholdLow,_O:cerentEnvMonVoltageStatsThresholdVeryLow,'cerentEnvMonTemperatureStatsTable':cerentEnvMonTemperatureStatsTable,'cerentEnvMonTemperatureStatsEntry':cerentEnvMonTemperatureStatsEntry,_H:cerentEnvMonTemperatureStatsIndex,_P:cerentEnvMonTemperatureStatsDescr,_Q:cerentEnvMonTemperatureStatsCurrentValue,_R:cerentEnvMonTemperatureStatsThresholdHigh,'cerentEnvMonMibConformance':cerentEnvMonMibConformance,'cerentEnvMonMibCompliance':cerentEnvMonMibCompliance,'cerentEnvMonMibBasicCompliance':cerentEnvMonMibBasicCompliance,'cerentEnvMonMibGroups':cerentEnvMonMibGroups,_S:cerentEnvMonMibObjectsGroup})