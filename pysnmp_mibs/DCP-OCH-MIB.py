_a='dcpOchTableGroupV1'
_Z='dcpOchGeneralTableGroupV1'
_Y='dcpOchAlarm'
_X='dcpOchDescription'
_W='dcpOchStatus'
_V='dcpOchPortMode'
_U='dcpOchWantedOutputPower'
_T='dcpOchWssInsertionLoss'
_S='dcpOchWssAttenuation'
_R='dcpOchTxPower'
_Q='dcpOchRxPower'
_P='dcpOchChannelId'
_O='dcpOchGeneralConfiguredChannels'
_N='dcpOchGeneralUtilization'
_M='dcpOchGeneralActiveChannels'
_L='dcpOchGeneralMaxChannels'
_K='dcpOchGeneralSpacing'
_J='dcpOchGeneralPortName'
_I='dcpOchIndex'
_H='not-accessible'
_G='dcpOchGeneralIndex'
_F='DisplayString'
_E='Gauge32'
_D='Unsigned32'
_C='read-only'
_B='DCP-OCH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dcpGeneric,=mibBuilder.importSymbols('DCP-MIB','dcpGeneric')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_E,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
DcpHundreds,DcpTenths,InterfaceStatus,ItuPerceivedSeverity,OchPortMode,OpticalPower1Decimal=mibBuilder.importSymbols('SO-TC-MIB','DcpHundreds','DcpTenths','InterfaceStatus','ItuPerceivedSeverity','OchPortMode','OpticalPower1Decimal')
dcpOch=ModuleIdentity((1,3,6,1,4,1,30826,2,2,4))
if mibBuilder.loadTexts:dcpOch.setRevisions(('2021-03-18 14:49',))
_DcpOchGeneral_ObjectIdentity=ObjectIdentity
dcpOchGeneral=_DcpOchGeneral_ObjectIdentity((1,3,6,1,4,1,30826,2,2,4,1))
_DcpOchGeneralTable_Object=MibTable
dcpOchGeneralTable=_DcpOchGeneralTable_Object((1,3,6,1,4,1,30826,2,2,4,1,1))
if mibBuilder.loadTexts:dcpOchGeneralTable.setStatus(_A)
_DcpOchGeneralEntry_Object=MibTableRow
dcpOchGeneralEntry=_DcpOchGeneralEntry_Object((1,3,6,1,4,1,30826,2,2,4,1,1,1))
dcpOchGeneralEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:dcpOchGeneralEntry.setStatus(_A)
class _DcpOchGeneralIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_DcpOchGeneralIndex_Type.__name__=_D
_DcpOchGeneralIndex_Object=MibTableColumn
dcpOchGeneralIndex=_DcpOchGeneralIndex_Object((1,3,6,1,4,1,30826,2,2,4,1,1,1,1),_DcpOchGeneralIndex_Type())
dcpOchGeneralIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dcpOchGeneralIndex.setStatus(_A)
_DcpOchGeneralPortName_Type=DisplayString
_DcpOchGeneralPortName_Object=MibTableColumn
dcpOchGeneralPortName=_DcpOchGeneralPortName_Object((1,3,6,1,4,1,30826,2,2,4,1,1,1,2),_DcpOchGeneralPortName_Type())
dcpOchGeneralPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchGeneralPortName.setStatus(_A)
_DcpOchGeneralSpacing_Type=DcpHundreds
_DcpOchGeneralSpacing_Object=MibTableColumn
dcpOchGeneralSpacing=_DcpOchGeneralSpacing_Object((1,3,6,1,4,1,30826,2,2,4,1,1,1,3),_DcpOchGeneralSpacing_Type())
dcpOchGeneralSpacing.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchGeneralSpacing.setStatus(_A)
_DcpOchGeneralMaxChannels_Type=Unsigned32
_DcpOchGeneralMaxChannels_Object=MibTableColumn
dcpOchGeneralMaxChannels=_DcpOchGeneralMaxChannels_Object((1,3,6,1,4,1,30826,2,2,4,1,1,1,4),_DcpOchGeneralMaxChannels_Type())
dcpOchGeneralMaxChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchGeneralMaxChannels.setStatus(_A)
_DcpOchGeneralActiveChannels_Type=Unsigned32
_DcpOchGeneralActiveChannels_Object=MibTableColumn
dcpOchGeneralActiveChannels=_DcpOchGeneralActiveChannels_Object((1,3,6,1,4,1,30826,2,2,4,1,1,1,5),_DcpOchGeneralActiveChannels_Type())
dcpOchGeneralActiveChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchGeneralActiveChannels.setStatus(_A)
class _DcpOchGeneralUtilization_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DcpOchGeneralUtilization_Type.__name__=_E
_DcpOchGeneralUtilization_Object=MibTableColumn
dcpOchGeneralUtilization=_DcpOchGeneralUtilization_Object((1,3,6,1,4,1,30826,2,2,4,1,1,1,6),_DcpOchGeneralUtilization_Type())
dcpOchGeneralUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchGeneralUtilization.setStatus(_A)
_DcpOchGeneralConfiguredChannels_Type=Unsigned32
_DcpOchGeneralConfiguredChannels_Object=MibTableColumn
dcpOchGeneralConfiguredChannels=_DcpOchGeneralConfiguredChannels_Object((1,3,6,1,4,1,30826,2,2,4,1,1,1,7),_DcpOchGeneralConfiguredChannels_Type())
dcpOchGeneralConfiguredChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchGeneralConfiguredChannels.setStatus(_A)
_DcpOchObjects_ObjectIdentity=ObjectIdentity
dcpOchObjects=_DcpOchObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,4,2))
_DcpOchTable_Object=MibTable
dcpOchTable=_DcpOchTable_Object((1,3,6,1,4,1,30826,2,2,4,2,1))
if mibBuilder.loadTexts:dcpOchTable.setStatus(_A)
_DcpOchEntry_Object=MibTableRow
dcpOchEntry=_DcpOchEntry_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1))
dcpOchEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:dcpOchEntry.setStatus(_A)
class _DcpOchIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_DcpOchIndex_Type.__name__=_D
_DcpOchIndex_Object=MibTableColumn
dcpOchIndex=_DcpOchIndex_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,1),_DcpOchIndex_Type())
dcpOchIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dcpOchIndex.setStatus(_A)
_DcpOchChannelId_Type=DisplayString
_DcpOchChannelId_Object=MibTableColumn
dcpOchChannelId=_DcpOchChannelId_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,2),_DcpOchChannelId_Type())
dcpOchChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchChannelId.setStatus(_A)
_DcpOchRxPower_Type=DcpTenths
_DcpOchRxPower_Object=MibTableColumn
dcpOchRxPower=_DcpOchRxPower_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,3),_DcpOchRxPower_Type())
dcpOchRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchRxPower.setStatus(_A)
_DcpOchTxPower_Type=DcpTenths
_DcpOchTxPower_Object=MibTableColumn
dcpOchTxPower=_DcpOchTxPower_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,4),_DcpOchTxPower_Type())
dcpOchTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchTxPower.setStatus(_A)
_DcpOchWssAttenuation_Type=DcpTenths
_DcpOchWssAttenuation_Object=MibTableColumn
dcpOchWssAttenuation=_DcpOchWssAttenuation_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,5),_DcpOchWssAttenuation_Type())
dcpOchWssAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchWssAttenuation.setStatus(_A)
_DcpOchWssInsertionLoss_Type=DcpTenths
_DcpOchWssInsertionLoss_Object=MibTableColumn
dcpOchWssInsertionLoss=_DcpOchWssInsertionLoss_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,6),_DcpOchWssInsertionLoss_Type())
dcpOchWssInsertionLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchWssInsertionLoss.setStatus(_A)
_DcpOchWantedOutputPower_Type=DcpTenths
_DcpOchWantedOutputPower_Object=MibTableColumn
dcpOchWantedOutputPower=_DcpOchWantedOutputPower_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,7),_DcpOchWantedOutputPower_Type())
dcpOchWantedOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchWantedOutputPower.setStatus(_A)
_DcpOchPortMode_Type=OchPortMode
_DcpOchPortMode_Object=MibTableColumn
dcpOchPortMode=_DcpOchPortMode_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,8),_DcpOchPortMode_Type())
dcpOchPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchPortMode.setStatus(_A)
_DcpOchStatus_Type=InterfaceStatus
_DcpOchStatus_Object=MibTableColumn
dcpOchStatus=_DcpOchStatus_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,9),_DcpOchStatus_Type())
dcpOchStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchStatus.setStatus(_A)
class _DcpOchDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DcpOchDescription_Type.__name__=_F
_DcpOchDescription_Object=MibTableColumn
dcpOchDescription=_DcpOchDescription_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,10),_DcpOchDescription_Type())
dcpOchDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchDescription.setStatus(_A)
_DcpOchAlarm_Type=ItuPerceivedSeverity
_DcpOchAlarm_Object=MibTableColumn
dcpOchAlarm=_DcpOchAlarm_Object((1,3,6,1,4,1,30826,2,2,4,2,1,1,11),_DcpOchAlarm_Type())
dcpOchAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpOchAlarm.setStatus(_A)
_DcpOchMIBCompliance_ObjectIdentity=ObjectIdentity
dcpOchMIBCompliance=_DcpOchMIBCompliance_ObjectIdentity((1,3,6,1,4,1,30826,2,2,4,3))
_DcpOchMIBGroups_ObjectIdentity=ObjectIdentity
dcpOchMIBGroups=_DcpOchMIBGroups_ObjectIdentity((1,3,6,1,4,1,30826,2,2,4,3,1))
_DcpOchMIBCompliances_ObjectIdentity=ObjectIdentity
dcpOchMIBCompliances=_DcpOchMIBCompliances_ObjectIdentity((1,3,6,1,4,1,30826,2,2,4,3,2))
dcpOchGeneralTableGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,4,3,1,1))
dcpOchGeneralTableGroupV1.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:dcpOchGeneralTableGroupV1.setStatus(_A)
dcpOchTableGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,4,3,1,2))
dcpOchTableGroupV1.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:dcpOchTableGroupV1.setStatus(_A)
dcpOchBasicComplV1=ModuleCompliance((1,3,6,1,4,1,30826,2,2,4,3,2,1))
dcpOchBasicComplV1.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:dcpOchBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dcpOch':dcpOch,'dcpOchGeneral':dcpOchGeneral,'dcpOchGeneralTable':dcpOchGeneralTable,'dcpOchGeneralEntry':dcpOchGeneralEntry,_G:dcpOchGeneralIndex,_J:dcpOchGeneralPortName,_K:dcpOchGeneralSpacing,_L:dcpOchGeneralMaxChannels,_M:dcpOchGeneralActiveChannels,_N:dcpOchGeneralUtilization,_O:dcpOchGeneralConfiguredChannels,'dcpOchObjects':dcpOchObjects,'dcpOchTable':dcpOchTable,'dcpOchEntry':dcpOchEntry,_I:dcpOchIndex,_P:dcpOchChannelId,_Q:dcpOchRxPower,_R:dcpOchTxPower,_S:dcpOchWssAttenuation,_T:dcpOchWssInsertionLoss,_U:dcpOchWantedOutputPower,_V:dcpOchPortMode,_W:dcpOchStatus,_X:dcpOchDescription,_Y:dcpOchAlarm,'dcpOchMIBCompliance':dcpOchMIBCompliance,'dcpOchMIBGroups':dcpOchMIBGroups,_Z:dcpOchGeneralTableGroupV1,_a:dcpOchTableGroupV1,'dcpOchMIBCompliances':dcpOchMIBCompliances,'dcpOchBasicComplV1':dcpOchBasicComplV1})