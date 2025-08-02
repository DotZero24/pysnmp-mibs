_W='adGenAOSPoEPortInfoGroup'
_V='adGenAOSPoESysInfoGroup'
_U='adGenAOSPoEPsePortAveragePower'
_T='adGenAOSPoEPsePortMaxPower'
_S='adGenAOSPoEPsePortCurrent'
_R='adGenAOSPoEPsePortVoltage'
_Q='adGenAOSPoEPsePortPowerClassifications'
_P='adGenAOSPoEPsePortPowerUsed'
_O='adGenAOSPoEPsePortPowerStatusMode'
_N='adGenAOSPoEPsePortPowerAdminMode'
_M='adGenAOSPoEPsePortIfName'
_L='adGenAOSPoEPseAverageTotalPowerUsed'
_K='adGenAOSPoEPseTotalPowerAvailable'
_J='adGenAOSPoEPseTotalPowerUsed'
_I='adGenAOSPoEPseTotalPower'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='Watts'
_D='DisplayString'
_C='read-only'
_B='ADTRAN-AOS-POE-STATUS-INFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSConformance,adGenAOSSwitch=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSConformance','adGenAOSSwitch')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
adGenAOSPoEStatusInfo=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,4,2))
if mibBuilder.loadTexts:adGenAOSPoEStatusInfo.setRevisions(('2018-07-15 00:00',))
_AdGenAOSPoEMon_ObjectIdentity=ObjectIdentity
adGenAOSPoEMon=_AdGenAOSPoEMon_ObjectIdentity((1,3,6,1,4,1,664,5,53,4,3))
_AdGenAOSPoESysInfo_ObjectIdentity=ObjectIdentity
adGenAOSPoESysInfo=_AdGenAOSPoESysInfo_ObjectIdentity((1,3,6,1,4,1,664,5,53,4,3,1))
class _AdGenAOSPoEPseTotalPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPseTotalPower_Type.__name__=_D
_AdGenAOSPoEPseTotalPower_Object=MibScalar
adGenAOSPoEPseTotalPower=_AdGenAOSPoEPseTotalPower_Object((1,3,6,1,4,1,664,5,53,4,3,1,1),_AdGenAOSPoEPseTotalPower_Type())
adGenAOSPoEPseTotalPower.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPseTotalPower.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPseTotalPower.setUnits(_E)
class _AdGenAOSPoEPseTotalPowerUsed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPseTotalPowerUsed_Type.__name__=_D
_AdGenAOSPoEPseTotalPowerUsed_Object=MibScalar
adGenAOSPoEPseTotalPowerUsed=_AdGenAOSPoEPseTotalPowerUsed_Object((1,3,6,1,4,1,664,5,53,4,3,1,2),_AdGenAOSPoEPseTotalPowerUsed_Type())
adGenAOSPoEPseTotalPowerUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPseTotalPowerUsed.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPseTotalPowerUsed.setUnits(_E)
class _AdGenAOSPoEPseTotalPowerAvailable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPseTotalPowerAvailable_Type.__name__=_D
_AdGenAOSPoEPseTotalPowerAvailable_Object=MibScalar
adGenAOSPoEPseTotalPowerAvailable=_AdGenAOSPoEPseTotalPowerAvailable_Object((1,3,6,1,4,1,664,5,53,4,3,1,3),_AdGenAOSPoEPseTotalPowerAvailable_Type())
adGenAOSPoEPseTotalPowerAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPseTotalPowerAvailable.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPseTotalPowerAvailable.setUnits(_E)
class _AdGenAOSPoEPseAverageTotalPowerUsed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPseAverageTotalPowerUsed_Type.__name__=_D
_AdGenAOSPoEPseAverageTotalPowerUsed_Object=MibScalar
adGenAOSPoEPseAverageTotalPowerUsed=_AdGenAOSPoEPseAverageTotalPowerUsed_Object((1,3,6,1,4,1,664,5,53,4,3,1,4),_AdGenAOSPoEPseAverageTotalPowerUsed_Type())
adGenAOSPoEPseAverageTotalPowerUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPseAverageTotalPowerUsed.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPseAverageTotalPowerUsed.setUnits(_E)
_AdGenAOSPoEPortInfo_ObjectIdentity=ObjectIdentity
adGenAOSPoEPortInfo=_AdGenAOSPoEPortInfo_ObjectIdentity((1,3,6,1,4,1,664,5,53,4,3,2))
_AdGenAOSPoEPortInfoTable_Object=MibTable
adGenAOSPoEPortInfoTable=_AdGenAOSPoEPortInfoTable_Object((1,3,6,1,4,1,664,5,53,4,3,2,1))
if mibBuilder.loadTexts:adGenAOSPoEPortInfoTable.setStatus(_A)
_AdGenAOSPoEPortInfoTableEntry_Object=MibTableRow
adGenAOSPoEPortInfoTableEntry=_AdGenAOSPoEPortInfoTableEntry_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1))
adGenAOSPoEPortInfoTableEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenAOSPoEPortInfoTableEntry.setStatus(_A)
class _AdGenAOSPoEPsePortIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AdGenAOSPoEPsePortIfName_Type.__name__=_D
_AdGenAOSPoEPsePortIfName_Object=MibTableColumn
adGenAOSPoEPsePortIfName=_AdGenAOSPoEPsePortIfName_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,1),_AdGenAOSPoEPsePortIfName_Type())
adGenAOSPoEPsePortIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortIfName.setStatus(_A)
_AdGenAOSPoEPsePortPowerAdminMode_Type=DisplayString
_AdGenAOSPoEPsePortPowerAdminMode_Object=MibTableColumn
adGenAOSPoEPsePortPowerAdminMode=_AdGenAOSPoEPsePortPowerAdminMode_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,2),_AdGenAOSPoEPsePortPowerAdminMode_Type())
adGenAOSPoEPsePortPowerAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortPowerAdminMode.setStatus(_A)
class _AdGenAOSPoEPsePortPowerStatusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('limited',1),('delivering',2),('searching',3),('fault',4),('denied',5),('disabledThermal',6),('disabled',7),('otherFault',8)))
_AdGenAOSPoEPsePortPowerStatusMode_Type.__name__=_F
_AdGenAOSPoEPsePortPowerStatusMode_Object=MibTableColumn
adGenAOSPoEPsePortPowerStatusMode=_AdGenAOSPoEPsePortPowerStatusMode_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,3),_AdGenAOSPoEPsePortPowerStatusMode_Type())
adGenAOSPoEPsePortPowerStatusMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortPowerStatusMode.setStatus(_A)
class _AdGenAOSPoEPsePortPowerUsed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPsePortPowerUsed_Type.__name__=_D
_AdGenAOSPoEPsePortPowerUsed_Object=MibTableColumn
adGenAOSPoEPsePortPowerUsed=_AdGenAOSPoEPsePortPowerUsed_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,4),_AdGenAOSPoEPsePortPowerUsed_Type())
adGenAOSPoEPsePortPowerUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortPowerUsed.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPsePortPowerUsed.setUnits(_E)
class _AdGenAOSPoEPsePortPowerClassifications_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('class0',1),('class1',2),('class2',3),('class3',4),('class4',5),('notApplicable',6)))
_AdGenAOSPoEPsePortPowerClassifications_Type.__name__=_F
_AdGenAOSPoEPsePortPowerClassifications_Object=MibTableColumn
adGenAOSPoEPsePortPowerClassifications=_AdGenAOSPoEPsePortPowerClassifications_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,5),_AdGenAOSPoEPsePortPowerClassifications_Type())
adGenAOSPoEPsePortPowerClassifications.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortPowerClassifications.setStatus(_A)
class _AdGenAOSPoEPsePortVoltage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPsePortVoltage_Type.__name__=_D
_AdGenAOSPoEPsePortVoltage_Object=MibTableColumn
adGenAOSPoEPsePortVoltage=_AdGenAOSPoEPsePortVoltage_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,6),_AdGenAOSPoEPsePortVoltage_Type())
adGenAOSPoEPsePortVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortVoltage.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPsePortVoltage.setUnits('Volts')
class _AdGenAOSPoEPsePortCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPsePortCurrent_Type.__name__=_D
_AdGenAOSPoEPsePortCurrent_Object=MibTableColumn
adGenAOSPoEPsePortCurrent=_AdGenAOSPoEPsePortCurrent_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,7),_AdGenAOSPoEPsePortCurrent_Type())
adGenAOSPoEPsePortCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortCurrent.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPsePortCurrent.setUnits('mA')
class _AdGenAOSPoEPsePortMaxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPsePortMaxPower_Type.__name__=_D
_AdGenAOSPoEPsePortMaxPower_Object=MibTableColumn
adGenAOSPoEPsePortMaxPower=_AdGenAOSPoEPsePortMaxPower_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,8),_AdGenAOSPoEPsePortMaxPower_Type())
adGenAOSPoEPsePortMaxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortMaxPower.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPsePortMaxPower.setUnits(_E)
class _AdGenAOSPoEPsePortAveragePower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AdGenAOSPoEPsePortAveragePower_Type.__name__=_D
_AdGenAOSPoEPsePortAveragePower_Object=MibTableColumn
adGenAOSPoEPsePortAveragePower=_AdGenAOSPoEPsePortAveragePower_Object((1,3,6,1,4,1,664,5,53,4,3,2,1,1,9),_AdGenAOSPoEPsePortAveragePower_Type())
adGenAOSPoEPsePortAveragePower.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSPoEPsePortAveragePower.setStatus(_A)
if mibBuilder.loadTexts:adGenAOSPoEPsePortAveragePower.setUnits(_E)
_AdGenAOSPowerOverEthernetConformance_ObjectIdentity=ObjectIdentity
adGenAOSPowerOverEthernetConformance=_AdGenAOSPowerOverEthernetConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,35))
_AdGenAOSPowerOverEthernetGroups_ObjectIdentity=ObjectIdentity
adGenAOSPowerOverEthernetGroups=_AdGenAOSPowerOverEthernetGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,35,1))
_AdGenAOSPowerOverEthernetCompliances_ObjectIdentity=ObjectIdentity
adGenAOSPowerOverEthernetCompliances=_AdGenAOSPowerOverEthernetCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,35,2))
adGenAOSPoESysInfoGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,35,1,1))
adGenAOSPoESysInfoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:adGenAOSPoESysInfoGroup.setStatus(_A)
adGenAOSPoEPortInfoGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,35,1,2))
adGenAOSPoEPortInfoGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:adGenAOSPoEPortInfoGroup.setStatus(_A)
adGenAOSPowerOverEthernetFullCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,35,2,1))
adGenAOSPowerOverEthernetFullCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:adGenAOSPowerOverEthernetFullCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAOSPoEMon':adGenAOSPoEMon,'adGenAOSPoESysInfo':adGenAOSPoESysInfo,_I:adGenAOSPoEPseTotalPower,_J:adGenAOSPoEPseTotalPowerUsed,_K:adGenAOSPoEPseTotalPowerAvailable,_L:adGenAOSPoEPseAverageTotalPowerUsed,'adGenAOSPoEPortInfo':adGenAOSPoEPortInfo,'adGenAOSPoEPortInfoTable':adGenAOSPoEPortInfoTable,'adGenAOSPoEPortInfoTableEntry':adGenAOSPoEPortInfoTableEntry,_M:adGenAOSPoEPsePortIfName,_N:adGenAOSPoEPsePortPowerAdminMode,_O:adGenAOSPoEPsePortPowerStatusMode,_P:adGenAOSPoEPsePortPowerUsed,_Q:adGenAOSPoEPsePortPowerClassifications,_R:adGenAOSPoEPsePortVoltage,_S:adGenAOSPoEPsePortCurrent,_T:adGenAOSPoEPsePortMaxPower,_U:adGenAOSPoEPsePortAveragePower,'adGenAOSPowerOverEthernetConformance':adGenAOSPowerOverEthernetConformance,'adGenAOSPowerOverEthernetGroups':adGenAOSPowerOverEthernetGroups,_V:adGenAOSPoESysInfoGroup,_W:adGenAOSPoEPortInfoGroup,'adGenAOSPowerOverEthernetCompliances':adGenAOSPowerOverEthernetCompliances,'adGenAOSPowerOverEthernetFullCompliance':adGenAOSPowerOverEthernetFullCompliance,'adGenAOSPoEStatusInfo':adGenAOSPoEStatusInfo})