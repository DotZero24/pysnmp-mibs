_b='cie1000PoeStatusInterfaceTableInfoGroup'
_a='cie1000PoeConfigInterfaceParamTableInfoGroup'
_Z='cie1000PoeConfigSwitchParamTableInfoGroup'
_Y='cie1000PoeConfigGlobalsInfoGroup'
_X='cie1000PoeCapabilitiesInterfaceInfoGroup'
_W='cie1000PoeStatusInterfaceCurrentConsumption'
_V='cie1000PoeStatusInterfacePowerReserved'
_U='cie1000PoeStatusInterfacePowerConsumption'
_T='cie1000PoeStatusInterfaceCurrentState'
_S='cie1000PoeStatusInterfacePDClass'
_R='cie1000PoeConfigInterfaceParamMaxPower'
_Q='cie1000PoeConfigInterfaceParamPriority'
_P='cie1000PoeConfigInterfaceParamMode'
_O='cie1000PoeConfigSwitchParamCapacitorDetection'
_N='cie1000PoeConfigSwitchParamMaxPower'
_M='cie1000PoeConfigGlobalsManagementMode'
_L='cie1000PoeCapabilitiesInterfacePoE'
_K='Unsigned32'
_J='cie1000PoeStatusInterfaceIfIndex'
_I='cie1000PoeConfigInterfaceParamIfIndex'
_H='cie1000PoeConfigSwitchParamSwitchId'
_G='cie1000PoeCapabilitiesInterfaceIfIndex'
_F='Integer32'
_E='accessible-for-notify'
_D='read-write'
_C='read-only'
_B='CIE1000-POE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CIE1000InterfaceIndex,=mibBuilder.importSymbols('CIE1000-TC','CIE1000InterfaceIndex')
cie1000SwitchMgmt,=mibBuilder.importSymbols('CISCO-IE1000-MIB','cie1000SwitchMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cie1000PoeMib=ModuleIdentity((1,3,6,1,4,1,9,9,832,1,43))
if mibBuilder.loadTexts:cie1000PoeMib.setRevisions(('2014-08-20 00:00',))
class CIE1000poeMgmtModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('classReservedPower',0),('classConsumption',1),('allocatedReservedPower',2),('allocatedConsumption',3),('lldpReservedPower',4),('lldpConsumption',5)))
class CIE1000poeModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disable',0),('poeDot3af',1),('poePlusDot3at',2)))
class CIE1000poePowerPriorityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('low',0),('high',1),('critical',2)))
class CIE1000poeStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notSupported',0),('budgetExceeded',1),('noPoweredDeviceDetected',2),('poweredDeviceOn',3),('poweredDeviceOff',4),('poweredDeviceOverloaded',5),('unknownState',6),('disabled',7)))
_Cie1000PoeMibObjects_ObjectIdentity=ObjectIdentity
cie1000PoeMibObjects=_Cie1000PoeMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,1))
_Cie1000PoeCapabilities_ObjectIdentity=ObjectIdentity
cie1000PoeCapabilities=_Cie1000PoeCapabilities_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,1,1))
_Cie1000PoeCapabilitiesInterfaceTable_Object=MibTable
cie1000PoeCapabilitiesInterfaceTable=_Cie1000PoeCapabilitiesInterfaceTable_Object((1,3,6,1,4,1,9,9,832,1,43,1,1,1))
if mibBuilder.loadTexts:cie1000PoeCapabilitiesInterfaceTable.setStatus(_A)
_Cie1000PoeCapabilitiesInterfaceEntry_Object=MibTableRow
cie1000PoeCapabilitiesInterfaceEntry=_Cie1000PoeCapabilitiesInterfaceEntry_Object((1,3,6,1,4,1,9,9,832,1,43,1,1,1,1))
cie1000PoeCapabilitiesInterfaceEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cie1000PoeCapabilitiesInterfaceEntry.setStatus(_A)
_Cie1000PoeCapabilitiesInterfaceIfIndex_Type=CIE1000InterfaceIndex
_Cie1000PoeCapabilitiesInterfaceIfIndex_Object=MibTableColumn
cie1000PoeCapabilitiesInterfaceIfIndex=_Cie1000PoeCapabilitiesInterfaceIfIndex_Object((1,3,6,1,4,1,9,9,832,1,43,1,1,1,1,1),_Cie1000PoeCapabilitiesInterfaceIfIndex_Type())
cie1000PoeCapabilitiesInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000PoeCapabilitiesInterfaceIfIndex.setStatus(_A)
_Cie1000PoeCapabilitiesInterfacePoE_Type=TruthValue
_Cie1000PoeCapabilitiesInterfacePoE_Object=MibTableColumn
cie1000PoeCapabilitiesInterfacePoE=_Cie1000PoeCapabilitiesInterfacePoE_Object((1,3,6,1,4,1,9,9,832,1,43,1,1,1,1,2),_Cie1000PoeCapabilitiesInterfacePoE_Type())
cie1000PoeCapabilitiesInterfacePoE.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000PoeCapabilitiesInterfacePoE.setStatus(_A)
_Cie1000PoeConfig_ObjectIdentity=ObjectIdentity
cie1000PoeConfig=_Cie1000PoeConfig_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,1,2))
_Cie1000PoeConfigGlobals_ObjectIdentity=ObjectIdentity
cie1000PoeConfigGlobals=_Cie1000PoeConfigGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,1,2,1))
_Cie1000PoeConfigGlobalsManagementMode_Type=CIE1000poeMgmtModeType
_Cie1000PoeConfigGlobalsManagementMode_Object=MibScalar
cie1000PoeConfigGlobalsManagementMode=_Cie1000PoeConfigGlobalsManagementMode_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,1,1),_Cie1000PoeConfigGlobalsManagementMode_Type())
cie1000PoeConfigGlobalsManagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000PoeConfigGlobalsManagementMode.setStatus(_A)
_Cie1000PoeConfigSwitch_ObjectIdentity=ObjectIdentity
cie1000PoeConfigSwitch=_Cie1000PoeConfigSwitch_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,1,2,2))
_Cie1000PoeConfigSwitchParamTable_Object=MibTable
cie1000PoeConfigSwitchParamTable=_Cie1000PoeConfigSwitchParamTable_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,2,1))
if mibBuilder.loadTexts:cie1000PoeConfigSwitchParamTable.setStatus(_A)
_Cie1000PoeConfigSwitchParamEntry_Object=MibTableRow
cie1000PoeConfigSwitchParamEntry=_Cie1000PoeConfigSwitchParamEntry_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,2,1,1))
cie1000PoeConfigSwitchParamEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cie1000PoeConfigSwitchParamEntry.setStatus(_A)
class _Cie1000PoeConfigSwitchParamSwitchId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Cie1000PoeConfigSwitchParamSwitchId_Type.__name__=_K
_Cie1000PoeConfigSwitchParamSwitchId_Object=MibTableColumn
cie1000PoeConfigSwitchParamSwitchId=_Cie1000PoeConfigSwitchParamSwitchId_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,2,1,1,1),_Cie1000PoeConfigSwitchParamSwitchId_Type())
cie1000PoeConfigSwitchParamSwitchId.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000PoeConfigSwitchParamSwitchId.setStatus(_A)
class _Cie1000PoeConfigSwitchParamMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_Cie1000PoeConfigSwitchParamMaxPower_Type.__name__=_F
_Cie1000PoeConfigSwitchParamMaxPower_Object=MibTableColumn
cie1000PoeConfigSwitchParamMaxPower=_Cie1000PoeConfigSwitchParamMaxPower_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,2,1,1,2),_Cie1000PoeConfigSwitchParamMaxPower_Type())
cie1000PoeConfigSwitchParamMaxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000PoeConfigSwitchParamMaxPower.setStatus(_A)
_Cie1000PoeConfigSwitchParamCapacitorDetection_Type=TruthValue
_Cie1000PoeConfigSwitchParamCapacitorDetection_Object=MibTableColumn
cie1000PoeConfigSwitchParamCapacitorDetection=_Cie1000PoeConfigSwitchParamCapacitorDetection_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,2,1,1,3),_Cie1000PoeConfigSwitchParamCapacitorDetection_Type())
cie1000PoeConfigSwitchParamCapacitorDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000PoeConfigSwitchParamCapacitorDetection.setStatus(_A)
_Cie1000PoeConfigInterface_ObjectIdentity=ObjectIdentity
cie1000PoeConfigInterface=_Cie1000PoeConfigInterface_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,1,2,3))
_Cie1000PoeConfigInterfaceParamTable_Object=MibTable
cie1000PoeConfigInterfaceParamTable=_Cie1000PoeConfigInterfaceParamTable_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,3,1))
if mibBuilder.loadTexts:cie1000PoeConfigInterfaceParamTable.setStatus(_A)
_Cie1000PoeConfigInterfaceParamEntry_Object=MibTableRow
cie1000PoeConfigInterfaceParamEntry=_Cie1000PoeConfigInterfaceParamEntry_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,3,1,1))
cie1000PoeConfigInterfaceParamEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cie1000PoeConfigInterfaceParamEntry.setStatus(_A)
_Cie1000PoeConfigInterfaceParamIfIndex_Type=CIE1000InterfaceIndex
_Cie1000PoeConfigInterfaceParamIfIndex_Object=MibTableColumn
cie1000PoeConfigInterfaceParamIfIndex=_Cie1000PoeConfigInterfaceParamIfIndex_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,3,1,1,1),_Cie1000PoeConfigInterfaceParamIfIndex_Type())
cie1000PoeConfigInterfaceParamIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000PoeConfigInterfaceParamIfIndex.setStatus(_A)
_Cie1000PoeConfigInterfaceParamMode_Type=CIE1000poeModeType
_Cie1000PoeConfigInterfaceParamMode_Object=MibTableColumn
cie1000PoeConfigInterfaceParamMode=_Cie1000PoeConfigInterfaceParamMode_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,3,1,1,2),_Cie1000PoeConfigInterfaceParamMode_Type())
cie1000PoeConfigInterfaceParamMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000PoeConfigInterfaceParamMode.setStatus(_A)
_Cie1000PoeConfigInterfaceParamPriority_Type=CIE1000poePowerPriorityType
_Cie1000PoeConfigInterfaceParamPriority_Object=MibTableColumn
cie1000PoeConfigInterfaceParamPriority=_Cie1000PoeConfigInterfaceParamPriority_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,3,1,1,3),_Cie1000PoeConfigInterfaceParamPriority_Type())
cie1000PoeConfigInterfaceParamPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000PoeConfigInterfaceParamPriority.setStatus(_A)
class _Cie1000PoeConfigInterfaceParamMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_Cie1000PoeConfigInterfaceParamMaxPower_Type.__name__=_F
_Cie1000PoeConfigInterfaceParamMaxPower_Object=MibTableColumn
cie1000PoeConfigInterfaceParamMaxPower=_Cie1000PoeConfigInterfaceParamMaxPower_Object((1,3,6,1,4,1,9,9,832,1,43,1,2,3,1,1,4),_Cie1000PoeConfigInterfaceParamMaxPower_Type())
cie1000PoeConfigInterfaceParamMaxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000PoeConfigInterfaceParamMaxPower.setStatus(_A)
_Cie1000PoeStatus_ObjectIdentity=ObjectIdentity
cie1000PoeStatus=_Cie1000PoeStatus_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,1,3))
_Cie1000PoeStatusInterfaceTable_Object=MibTable
cie1000PoeStatusInterfaceTable=_Cie1000PoeStatusInterfaceTable_Object((1,3,6,1,4,1,9,9,832,1,43,1,3,1))
if mibBuilder.loadTexts:cie1000PoeStatusInterfaceTable.setStatus(_A)
_Cie1000PoeStatusInterfaceEntry_Object=MibTableRow
cie1000PoeStatusInterfaceEntry=_Cie1000PoeStatusInterfaceEntry_Object((1,3,6,1,4,1,9,9,832,1,43,1,3,1,1))
cie1000PoeStatusInterfaceEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cie1000PoeStatusInterfaceEntry.setStatus(_A)
_Cie1000PoeStatusInterfaceIfIndex_Type=CIE1000InterfaceIndex
_Cie1000PoeStatusInterfaceIfIndex_Object=MibTableColumn
cie1000PoeStatusInterfaceIfIndex=_Cie1000PoeStatusInterfaceIfIndex_Object((1,3,6,1,4,1,9,9,832,1,43,1,3,1,1,1),_Cie1000PoeStatusInterfaceIfIndex_Type())
cie1000PoeStatusInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000PoeStatusInterfaceIfIndex.setStatus(_A)
_Cie1000PoeStatusInterfacePDClass_Type=Integer32
_Cie1000PoeStatusInterfacePDClass_Object=MibTableColumn
cie1000PoeStatusInterfacePDClass=_Cie1000PoeStatusInterfacePDClass_Object((1,3,6,1,4,1,9,9,832,1,43,1,3,1,1,2),_Cie1000PoeStatusInterfacePDClass_Type())
cie1000PoeStatusInterfacePDClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000PoeStatusInterfacePDClass.setStatus(_A)
_Cie1000PoeStatusInterfaceCurrentState_Type=CIE1000poeStatusType
_Cie1000PoeStatusInterfaceCurrentState_Object=MibTableColumn
cie1000PoeStatusInterfaceCurrentState=_Cie1000PoeStatusInterfaceCurrentState_Object((1,3,6,1,4,1,9,9,832,1,43,1,3,1,1,3),_Cie1000PoeStatusInterfaceCurrentState_Type())
cie1000PoeStatusInterfaceCurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000PoeStatusInterfaceCurrentState.setStatus(_A)
_Cie1000PoeStatusInterfacePowerConsumption_Type=Integer32
_Cie1000PoeStatusInterfacePowerConsumption_Object=MibTableColumn
cie1000PoeStatusInterfacePowerConsumption=_Cie1000PoeStatusInterfacePowerConsumption_Object((1,3,6,1,4,1,9,9,832,1,43,1,3,1,1,4),_Cie1000PoeStatusInterfacePowerConsumption_Type())
cie1000PoeStatusInterfacePowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000PoeStatusInterfacePowerConsumption.setStatus(_A)
_Cie1000PoeStatusInterfacePowerReserved_Type=Integer32
_Cie1000PoeStatusInterfacePowerReserved_Object=MibTableColumn
cie1000PoeStatusInterfacePowerReserved=_Cie1000PoeStatusInterfacePowerReserved_Object((1,3,6,1,4,1,9,9,832,1,43,1,3,1,1,5),_Cie1000PoeStatusInterfacePowerReserved_Type())
cie1000PoeStatusInterfacePowerReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000PoeStatusInterfacePowerReserved.setStatus(_A)
_Cie1000PoeStatusInterfaceCurrentConsumption_Type=Integer32
_Cie1000PoeStatusInterfaceCurrentConsumption_Object=MibTableColumn
cie1000PoeStatusInterfaceCurrentConsumption=_Cie1000PoeStatusInterfaceCurrentConsumption_Object((1,3,6,1,4,1,9,9,832,1,43,1,3,1,1,6),_Cie1000PoeStatusInterfaceCurrentConsumption_Type())
cie1000PoeStatusInterfaceCurrentConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000PoeStatusInterfaceCurrentConsumption.setStatus(_A)
_Cie1000PoeMibConformance_ObjectIdentity=ObjectIdentity
cie1000PoeMibConformance=_Cie1000PoeMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,2))
_Cie1000PoeMibCompliances_ObjectIdentity=ObjectIdentity
cie1000PoeMibCompliances=_Cie1000PoeMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,2,1))
_Cie1000PoeMibGroups_ObjectIdentity=ObjectIdentity
cie1000PoeMibGroups=_Cie1000PoeMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,43,2,2))
cie1000PoeCapabilitiesInterfaceInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,43,2,2,1))
cie1000PoeCapabilitiesInterfaceInfoGroup.setObjects(*((_B,_G),(_B,_L)))
if mibBuilder.loadTexts:cie1000PoeCapabilitiesInterfaceInfoGroup.setStatus(_A)
cie1000PoeConfigGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,43,2,2,2))
cie1000PoeConfigGlobalsInfoGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:cie1000PoeConfigGlobalsInfoGroup.setStatus(_A)
cie1000PoeConfigSwitchParamTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,43,2,2,3))
cie1000PoeConfigSwitchParamTableInfoGroup.setObjects(*((_B,_H),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cie1000PoeConfigSwitchParamTableInfoGroup.setStatus(_A)
cie1000PoeConfigInterfaceParamTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,43,2,2,4))
cie1000PoeConfigInterfaceParamTableInfoGroup.setObjects(*((_B,_I),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cie1000PoeConfigInterfaceParamTableInfoGroup.setStatus(_A)
cie1000PoeStatusInterfaceTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,43,2,2,5))
cie1000PoeStatusInterfaceTableInfoGroup.setObjects(*((_B,_J),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cie1000PoeStatusInterfaceTableInfoGroup.setStatus(_A)
cie1000PoeMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,832,1,43,2,1,1))
cie1000PoeMibCompliance.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:cie1000PoeMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CIE1000poeMgmtModeType':CIE1000poeMgmtModeType,'CIE1000poeModeType':CIE1000poeModeType,'CIE1000poePowerPriorityType':CIE1000poePowerPriorityType,'CIE1000poeStatusType':CIE1000poeStatusType,'cie1000PoeMib':cie1000PoeMib,'cie1000PoeMibObjects':cie1000PoeMibObjects,'cie1000PoeCapabilities':cie1000PoeCapabilities,'cie1000PoeCapabilitiesInterfaceTable':cie1000PoeCapabilitiesInterfaceTable,'cie1000PoeCapabilitiesInterfaceEntry':cie1000PoeCapabilitiesInterfaceEntry,_G:cie1000PoeCapabilitiesInterfaceIfIndex,_L:cie1000PoeCapabilitiesInterfacePoE,'cie1000PoeConfig':cie1000PoeConfig,'cie1000PoeConfigGlobals':cie1000PoeConfigGlobals,_M:cie1000PoeConfigGlobalsManagementMode,'cie1000PoeConfigSwitch':cie1000PoeConfigSwitch,'cie1000PoeConfigSwitchParamTable':cie1000PoeConfigSwitchParamTable,'cie1000PoeConfigSwitchParamEntry':cie1000PoeConfigSwitchParamEntry,_H:cie1000PoeConfigSwitchParamSwitchId,_N:cie1000PoeConfigSwitchParamMaxPower,_O:cie1000PoeConfigSwitchParamCapacitorDetection,'cie1000PoeConfigInterface':cie1000PoeConfigInterface,'cie1000PoeConfigInterfaceParamTable':cie1000PoeConfigInterfaceParamTable,'cie1000PoeConfigInterfaceParamEntry':cie1000PoeConfigInterfaceParamEntry,_I:cie1000PoeConfigInterfaceParamIfIndex,_P:cie1000PoeConfigInterfaceParamMode,_Q:cie1000PoeConfigInterfaceParamPriority,_R:cie1000PoeConfigInterfaceParamMaxPower,'cie1000PoeStatus':cie1000PoeStatus,'cie1000PoeStatusInterfaceTable':cie1000PoeStatusInterfaceTable,'cie1000PoeStatusInterfaceEntry':cie1000PoeStatusInterfaceEntry,_J:cie1000PoeStatusInterfaceIfIndex,_S:cie1000PoeStatusInterfacePDClass,_T:cie1000PoeStatusInterfaceCurrentState,_U:cie1000PoeStatusInterfacePowerConsumption,_V:cie1000PoeStatusInterfacePowerReserved,_W:cie1000PoeStatusInterfaceCurrentConsumption,'cie1000PoeMibConformance':cie1000PoeMibConformance,'cie1000PoeMibCompliances':cie1000PoeMibCompliances,'cie1000PoeMibCompliance':cie1000PoeMibCompliance,'cie1000PoeMibGroups':cie1000PoeMibGroups,_X:cie1000PoeCapabilitiesInterfaceInfoGroup,_Y:cie1000PoeConfigGlobalsInfoGroup,_Z:cie1000PoeConfigSwitchParamTableInfoGroup,_a:cie1000PoeConfigInterfaceParamTableInfoGroup,_b:cie1000PoeStatusInterfaceTableInfoGroup})