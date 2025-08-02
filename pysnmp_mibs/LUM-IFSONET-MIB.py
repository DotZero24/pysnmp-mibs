_p='ifSonetSectionGroupV2'
_o='ifSonetLineGroupV1'
_n='ifSonetSectionTxLossOfFrame'
_m='ifSonetLineTxAlarmIndicationSignal'
_l='ifSonetGeneralIfSonetLineStateLastChangeTime'
_k='ifSonetGeneralIfSonetLineConfigLastChangeTime'
_j='ifSonetGeneralIfSonetLineTableSize'
_i='ifSonetGeneralIfSonetSectionStateLastChangeTime'
_h='ifSonetGeneralIfSonetSectionConfigLastChangeTime'
_g='ifSonetGeneralIfSonetSectionTableSize'
_f='ifSonetGeneralStateLastChangeTime'
_e='ifSonetGeneralConfigLastChangeTime'
_d='EnabledDisabledWithNA'
_c='ifSonetLineGroupV2'
_b='ifSonetSectionGroupV1'
_a='ifSonetLineRemoteDefectIndication'
_Z='ifSonetLineRxAlarmIndicationSignal'
_Y='ifSonetLineRxSignalStatus'
_X='ifSonetLineTxSignalStatus'
_W='ifSonetLineOhTransparencyBitmask'
_V='ifSonetLineConnIfBasicIfIndex'
_U='ifSonetLineName'
_T='ifSonetSectionLossOfFrame'
_S='ifSonetSectionTraceMismatch'
_R='ifSonetSectionRxSignalStatus'
_Q='ifSonetSectionTxSignalStatus'
_P='ifSonetSectionTraceAlarmMode'
_O='ifSonetSectionTraceExpected'
_N='ifSonetSectionTraceReceived'
_M='ifSonetSectionTraceTransmitted'
_L='ifSonetSectionOhTransparencyBitmask'
_K='ifSonetSectionConnIfBasicIfIndex'
_J='ifSonetSectionName'
_I='Unsigned32WithNA'
_H='ifSonetGeneralGroupV1'
_G='deprecated'
_F='ifSonetLineIndex'
_E='ifSonetSectionIndex'
_D='DisplayStringWithNA'
_C='read-only'
_B='current'
_A='LUM-IFSONET-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfSonetMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfSonetMIB','lumModules')
DisplayStringWithNA,EnabledDisabledWithNA,FaultStatusWithNA,MgmtNameString,SignalStatusWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC',_D,_d,'FaultStatusWithNA','MgmtNameString','SignalStatusWithNA',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfSonetMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,53))
if mibBuilder.loadTexts:lumIfSonetMIBModule.setRevisions(('2017-06-15 00:00','2015-01-23 00:00','2014-05-16 00:00','2013-11-15 00:00','2013-05-01 00:00'))
_LumIfSonetConfs_ObjectIdentity=ObjectIdentity
lumIfSonetConfs=_LumIfSonetConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,53,1))
_LumIfSonetGroups_ObjectIdentity=ObjectIdentity
lumIfSonetGroups=_LumIfSonetGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,53,1,1))
_LumIfSonetCompl_ObjectIdentity=ObjectIdentity
lumIfSonetCompl=_LumIfSonetCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,53,1,2))
_LumIfSonetMIBObjects_ObjectIdentity=ObjectIdentity
lumIfSonetMIBObjects=_LumIfSonetMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,53,2))
_IfSonetGeneral_ObjectIdentity=ObjectIdentity
ifSonetGeneral=_IfSonetGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,53,2,1))
_IfSonetGeneralConfigLastChangeTime_Type=DateAndTime
_IfSonetGeneralConfigLastChangeTime_Object=MibScalar
ifSonetGeneralConfigLastChangeTime=_IfSonetGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,53,2,1,1),_IfSonetGeneralConfigLastChangeTime_Type())
ifSonetGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetGeneralConfigLastChangeTime.setStatus(_B)
_IfSonetGeneralStateLastChangeTime_Type=DateAndTime
_IfSonetGeneralStateLastChangeTime_Object=MibScalar
ifSonetGeneralStateLastChangeTime=_IfSonetGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,53,2,1,2),_IfSonetGeneralStateLastChangeTime_Type())
ifSonetGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetGeneralStateLastChangeTime.setStatus(_B)
_IfSonetGeneralIfSonetSectionTableSize_Type=Unsigned32
_IfSonetGeneralIfSonetSectionTableSize_Object=MibScalar
ifSonetGeneralIfSonetSectionTableSize=_IfSonetGeneralIfSonetSectionTableSize_Object((1,3,6,1,4,1,8708,2,53,2,1,3),_IfSonetGeneralIfSonetSectionTableSize_Type())
ifSonetGeneralIfSonetSectionTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetGeneralIfSonetSectionTableSize.setStatus(_B)
_IfSonetGeneralIfSonetSectionConfigLastChangeTime_Type=DateAndTime
_IfSonetGeneralIfSonetSectionConfigLastChangeTime_Object=MibScalar
ifSonetGeneralIfSonetSectionConfigLastChangeTime=_IfSonetGeneralIfSonetSectionConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,53,2,1,4),_IfSonetGeneralIfSonetSectionConfigLastChangeTime_Type())
ifSonetGeneralIfSonetSectionConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetGeneralIfSonetSectionConfigLastChangeTime.setStatus(_B)
_IfSonetGeneralIfSonetSectionStateLastChangeTime_Type=DateAndTime
_IfSonetGeneralIfSonetSectionStateLastChangeTime_Object=MibScalar
ifSonetGeneralIfSonetSectionStateLastChangeTime=_IfSonetGeneralIfSonetSectionStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,53,2,1,5),_IfSonetGeneralIfSonetSectionStateLastChangeTime_Type())
ifSonetGeneralIfSonetSectionStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetGeneralIfSonetSectionStateLastChangeTime.setStatus(_B)
_IfSonetGeneralIfSonetLineTableSize_Type=Unsigned32
_IfSonetGeneralIfSonetLineTableSize_Object=MibScalar
ifSonetGeneralIfSonetLineTableSize=_IfSonetGeneralIfSonetLineTableSize_Object((1,3,6,1,4,1,8708,2,53,2,1,6),_IfSonetGeneralIfSonetLineTableSize_Type())
ifSonetGeneralIfSonetLineTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetGeneralIfSonetLineTableSize.setStatus(_B)
_IfSonetGeneralIfSonetLineConfigLastChangeTime_Type=DateAndTime
_IfSonetGeneralIfSonetLineConfigLastChangeTime_Object=MibScalar
ifSonetGeneralIfSonetLineConfigLastChangeTime=_IfSonetGeneralIfSonetLineConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,53,2,1,7),_IfSonetGeneralIfSonetLineConfigLastChangeTime_Type())
ifSonetGeneralIfSonetLineConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetGeneralIfSonetLineConfigLastChangeTime.setStatus(_B)
_IfSonetGeneralIfSonetLineStateLastChangeTime_Type=DateAndTime
_IfSonetGeneralIfSonetLineStateLastChangeTime_Object=MibScalar
ifSonetGeneralIfSonetLineStateLastChangeTime=_IfSonetGeneralIfSonetLineStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,53,2,1,8),_IfSonetGeneralIfSonetLineStateLastChangeTime_Type())
ifSonetGeneralIfSonetLineStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetGeneralIfSonetLineStateLastChangeTime.setStatus(_B)
_IfSonetSectionList_ObjectIdentity=ObjectIdentity
ifSonetSectionList=_IfSonetSectionList_ObjectIdentity((1,3,6,1,4,1,8708,2,53,2,2))
_IfSonetSectionTable_Object=MibTable
ifSonetSectionTable=_IfSonetSectionTable_Object((1,3,6,1,4,1,8708,2,53,2,2,1))
if mibBuilder.loadTexts:ifSonetSectionTable.setStatus(_B)
_IfSonetSectionEntry_Object=MibTableRow
ifSonetSectionEntry=_IfSonetSectionEntry_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1))
ifSonetSectionEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:ifSonetSectionEntry.setStatus(_B)
_IfSonetSectionIndex_Type=Unsigned32
_IfSonetSectionIndex_Object=MibTableColumn
ifSonetSectionIndex=_IfSonetSectionIndex_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,1),_IfSonetSectionIndex_Type())
ifSonetSectionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionIndex.setStatus(_B)
_IfSonetSectionName_Type=MgmtNameString
_IfSonetSectionName_Object=MibTableColumn
ifSonetSectionName=_IfSonetSectionName_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,2),_IfSonetSectionName_Type())
ifSonetSectionName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionName.setStatus(_B)
_IfSonetSectionConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfSonetSectionConnIfBasicIfIndex_Object=MibTableColumn
ifSonetSectionConnIfBasicIfIndex=_IfSonetSectionConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,3),_IfSonetSectionConnIfBasicIfIndex_Type())
ifSonetSectionConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionConnIfBasicIfIndex.setStatus(_B)
class _IfSonetSectionOhTransparencyBitmask_Type(Unsigned32WithNA):defaultValue=0
_IfSonetSectionOhTransparencyBitmask_Type.__name__=_I
_IfSonetSectionOhTransparencyBitmask_Object=MibTableColumn
ifSonetSectionOhTransparencyBitmask=_IfSonetSectionOhTransparencyBitmask_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,4),_IfSonetSectionOhTransparencyBitmask_Type())
ifSonetSectionOhTransparencyBitmask.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionOhTransparencyBitmask.setStatus(_B)
class _IfSonetSectionTraceTransmitted_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IfSonetSectionTraceTransmitted_Type.__name__=_D
_IfSonetSectionTraceTransmitted_Object=MibTableColumn
ifSonetSectionTraceTransmitted=_IfSonetSectionTraceTransmitted_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,5),_IfSonetSectionTraceTransmitted_Type())
ifSonetSectionTraceTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionTraceTransmitted.setStatus(_B)
class _IfSonetSectionTraceReceived_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IfSonetSectionTraceReceived_Type.__name__=_D
_IfSonetSectionTraceReceived_Object=MibTableColumn
ifSonetSectionTraceReceived=_IfSonetSectionTraceReceived_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,6),_IfSonetSectionTraceReceived_Type())
ifSonetSectionTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionTraceReceived.setStatus(_B)
class _IfSonetSectionTraceExpected_Type(DisplayStringWithNA):defaultValue=OctetString('');subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IfSonetSectionTraceExpected_Type.__name__=_D
_IfSonetSectionTraceExpected_Object=MibTableColumn
ifSonetSectionTraceExpected=_IfSonetSectionTraceExpected_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,7),_IfSonetSectionTraceExpected_Type())
ifSonetSectionTraceExpected.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionTraceExpected.setStatus(_B)
class _IfSonetSectionTraceAlarmMode_Type(EnabledDisabledWithNA):defaultValue=1
_IfSonetSectionTraceAlarmMode_Type.__name__=_d
_IfSonetSectionTraceAlarmMode_Object=MibTableColumn
ifSonetSectionTraceAlarmMode=_IfSonetSectionTraceAlarmMode_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,8),_IfSonetSectionTraceAlarmMode_Type())
ifSonetSectionTraceAlarmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionTraceAlarmMode.setStatus(_B)
_IfSonetSectionTxSignalStatus_Type=SignalStatusWithNA
_IfSonetSectionTxSignalStatus_Object=MibTableColumn
ifSonetSectionTxSignalStatus=_IfSonetSectionTxSignalStatus_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,9),_IfSonetSectionTxSignalStatus_Type())
ifSonetSectionTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionTxSignalStatus.setStatus(_B)
_IfSonetSectionRxSignalStatus_Type=SignalStatusWithNA
_IfSonetSectionRxSignalStatus_Object=MibTableColumn
ifSonetSectionRxSignalStatus=_IfSonetSectionRxSignalStatus_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,10),_IfSonetSectionRxSignalStatus_Type())
ifSonetSectionRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionRxSignalStatus.setStatus(_B)
_IfSonetSectionTraceMismatch_Type=FaultStatusWithNA
_IfSonetSectionTraceMismatch_Object=MibTableColumn
ifSonetSectionTraceMismatch=_IfSonetSectionTraceMismatch_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,11),_IfSonetSectionTraceMismatch_Type())
ifSonetSectionTraceMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionTraceMismatch.setStatus(_B)
_IfSonetSectionLossOfFrame_Type=FaultStatusWithNA
_IfSonetSectionLossOfFrame_Object=MibTableColumn
ifSonetSectionLossOfFrame=_IfSonetSectionLossOfFrame_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,12),_IfSonetSectionLossOfFrame_Type())
ifSonetSectionLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionLossOfFrame.setStatus(_B)
_IfSonetSectionTxLossOfFrame_Type=FaultStatusWithNA
_IfSonetSectionTxLossOfFrame_Object=MibTableColumn
ifSonetSectionTxLossOfFrame=_IfSonetSectionTxLossOfFrame_Object((1,3,6,1,4,1,8708,2,53,2,2,1,1,13),_IfSonetSectionTxLossOfFrame_Type())
ifSonetSectionTxLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetSectionTxLossOfFrame.setStatus(_B)
_IfSonetLineList_ObjectIdentity=ObjectIdentity
ifSonetLineList=_IfSonetLineList_ObjectIdentity((1,3,6,1,4,1,8708,2,53,2,3))
_IfSonetLineTable_Object=MibTable
ifSonetLineTable=_IfSonetLineTable_Object((1,3,6,1,4,1,8708,2,53,2,3,1))
if mibBuilder.loadTexts:ifSonetLineTable.setStatus(_B)
_IfSonetLineEntry_Object=MibTableRow
ifSonetLineEntry=_IfSonetLineEntry_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1))
ifSonetLineEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:ifSonetLineEntry.setStatus(_B)
_IfSonetLineIndex_Type=Unsigned32
_IfSonetLineIndex_Object=MibTableColumn
ifSonetLineIndex=_IfSonetLineIndex_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,1),_IfSonetLineIndex_Type())
ifSonetLineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineIndex.setStatus(_B)
_IfSonetLineName_Type=MgmtNameString
_IfSonetLineName_Object=MibTableColumn
ifSonetLineName=_IfSonetLineName_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,2),_IfSonetLineName_Type())
ifSonetLineName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineName.setStatus(_B)
_IfSonetLineConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfSonetLineConnIfBasicIfIndex_Object=MibTableColumn
ifSonetLineConnIfBasicIfIndex=_IfSonetLineConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,3),_IfSonetLineConnIfBasicIfIndex_Type())
ifSonetLineConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineConnIfBasicIfIndex.setStatus(_B)
class _IfSonetLineOhTransparencyBitmask_Type(Unsigned32WithNA):defaultValue=0
_IfSonetLineOhTransparencyBitmask_Type.__name__=_I
_IfSonetLineOhTransparencyBitmask_Object=MibTableColumn
ifSonetLineOhTransparencyBitmask=_IfSonetLineOhTransparencyBitmask_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,4),_IfSonetLineOhTransparencyBitmask_Type())
ifSonetLineOhTransparencyBitmask.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineOhTransparencyBitmask.setStatus(_B)
_IfSonetLineTxSignalStatus_Type=SignalStatusWithNA
_IfSonetLineTxSignalStatus_Object=MibTableColumn
ifSonetLineTxSignalStatus=_IfSonetLineTxSignalStatus_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,5),_IfSonetLineTxSignalStatus_Type())
ifSonetLineTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineTxSignalStatus.setStatus(_B)
_IfSonetLineRxSignalStatus_Type=SignalStatusWithNA
_IfSonetLineRxSignalStatus_Object=MibTableColumn
ifSonetLineRxSignalStatus=_IfSonetLineRxSignalStatus_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,6),_IfSonetLineRxSignalStatus_Type())
ifSonetLineRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineRxSignalStatus.setStatus(_B)
_IfSonetLineRxAlarmIndicationSignal_Type=FaultStatusWithNA
_IfSonetLineRxAlarmIndicationSignal_Object=MibTableColumn
ifSonetLineRxAlarmIndicationSignal=_IfSonetLineRxAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,7),_IfSonetLineRxAlarmIndicationSignal_Type())
ifSonetLineRxAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineRxAlarmIndicationSignal.setStatus(_B)
_IfSonetLineRemoteDefectIndication_Type=FaultStatusWithNA
_IfSonetLineRemoteDefectIndication_Object=MibTableColumn
ifSonetLineRemoteDefectIndication=_IfSonetLineRemoteDefectIndication_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,8),_IfSonetLineRemoteDefectIndication_Type())
ifSonetLineRemoteDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineRemoteDefectIndication.setStatus(_B)
_IfSonetLineTxAlarmIndicationSignal_Type=FaultStatusWithNA
_IfSonetLineTxAlarmIndicationSignal_Object=MibTableColumn
ifSonetLineTxAlarmIndicationSignal=_IfSonetLineTxAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,53,2,3,1,1,9),_IfSonetLineTxAlarmIndicationSignal_Type())
ifSonetLineTxAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSonetLineTxAlarmIndicationSignal.setStatus(_B)
_IfSonetStsList_ObjectIdentity=ObjectIdentity
ifSonetStsList=_IfSonetStsList_ObjectIdentity((1,3,6,1,4,1,8708,2,53,2,4))
_IfSonetStsSpeList_ObjectIdentity=ObjectIdentity
ifSonetStsSpeList=_IfSonetStsSpeList_ObjectIdentity((1,3,6,1,4,1,8708,2,53,2,5))
ifSonetGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,53,1,1,1))
ifSonetGeneralGroupV1.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ifSonetGeneralGroupV1.setStatus(_B)
ifSonetSectionGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,53,1,1,2))
ifSonetSectionGroupV1.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ifSonetSectionGroupV1.setStatus(_G)
ifSonetLineGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,53,1,1,3))
ifSonetLineGroupV1.setObjects(*((_A,_F),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ifSonetLineGroupV1.setStatus(_G)
ifSonetLineGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,53,1,1,4))
ifSonetLineGroupV2.setObjects(*((_A,_F),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_m)))
if mibBuilder.loadTexts:ifSonetLineGroupV2.setStatus(_B)
ifSonetSectionGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,53,1,1,5))
ifSonetSectionGroupV2.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_n)))
if mibBuilder.loadTexts:ifSonetSectionGroupV2.setStatus(_B)
lumIfSonetComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,53,1,2,1))
lumIfSonetComplV1.setObjects(*((_A,_H),(_A,_b),(_A,_o)))
if mibBuilder.loadTexts:lumIfSonetComplV1.setStatus(_G)
lumIfSonetComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,53,1,2,2))
lumIfSonetComplV2.setObjects(*((_A,_H),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:lumIfSonetComplV2.setStatus(_G)
lumIfSonetComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,53,1,2,3))
lumIfSonetComplV3.setObjects(*((_A,_H),(_A,_p),(_A,_c)))
if mibBuilder.loadTexts:lumIfSonetComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfSonetMIBModule':lumIfSonetMIBModule,'lumIfSonetConfs':lumIfSonetConfs,'lumIfSonetGroups':lumIfSonetGroups,_H:ifSonetGeneralGroupV1,_b:ifSonetSectionGroupV1,_o:ifSonetLineGroupV1,_c:ifSonetLineGroupV2,_p:ifSonetSectionGroupV2,'lumIfSonetCompl':lumIfSonetCompl,'lumIfSonetComplV1':lumIfSonetComplV1,'lumIfSonetComplV2':lumIfSonetComplV2,'lumIfSonetComplV3':lumIfSonetComplV3,'lumIfSonetMIBObjects':lumIfSonetMIBObjects,'ifSonetGeneral':ifSonetGeneral,_e:ifSonetGeneralConfigLastChangeTime,_f:ifSonetGeneralStateLastChangeTime,_g:ifSonetGeneralIfSonetSectionTableSize,_h:ifSonetGeneralIfSonetSectionConfigLastChangeTime,_i:ifSonetGeneralIfSonetSectionStateLastChangeTime,_j:ifSonetGeneralIfSonetLineTableSize,_k:ifSonetGeneralIfSonetLineConfigLastChangeTime,_l:ifSonetGeneralIfSonetLineStateLastChangeTime,'ifSonetSectionList':ifSonetSectionList,'ifSonetSectionTable':ifSonetSectionTable,'ifSonetSectionEntry':ifSonetSectionEntry,_E:ifSonetSectionIndex,_J:ifSonetSectionName,_K:ifSonetSectionConnIfBasicIfIndex,_L:ifSonetSectionOhTransparencyBitmask,_M:ifSonetSectionTraceTransmitted,_N:ifSonetSectionTraceReceived,_O:ifSonetSectionTraceExpected,_P:ifSonetSectionTraceAlarmMode,_Q:ifSonetSectionTxSignalStatus,_R:ifSonetSectionRxSignalStatus,_S:ifSonetSectionTraceMismatch,_T:ifSonetSectionLossOfFrame,_n:ifSonetSectionTxLossOfFrame,'ifSonetLineList':ifSonetLineList,'ifSonetLineTable':ifSonetLineTable,'ifSonetLineEntry':ifSonetLineEntry,_F:ifSonetLineIndex,_U:ifSonetLineName,_V:ifSonetLineConnIfBasicIfIndex,_W:ifSonetLineOhTransparencyBitmask,_X:ifSonetLineTxSignalStatus,_Y:ifSonetLineRxSignalStatus,_Z:ifSonetLineRxAlarmIndicationSignal,_a:ifSonetLineRemoteDefectIndication,_m:ifSonetLineTxAlarmIndicationSignal,'ifSonetStsList':ifSonetStsList,'ifSonetStsSpeList':ifSonetStsSpeList})