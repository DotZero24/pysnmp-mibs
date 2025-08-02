_p='ifSdhRsGroupV2'
_o='ifSdhMsGroupV1'
_n='ifSdhRsTxLossOfFrame'
_m='ifSdhMsTxAlarmIndicationSignal'
_l='ifSdhGeneralIfSdhMsStateLastChangeTime'
_k='ifSdhGeneralIfSdhMsConfigLastChangeTime'
_j='ifSdhGeneralIfSdhMsTableSize'
_i='ifSdhGeneralIfSdhRsStateLastChangeTime'
_h='ifSdhGeneralIfSdhRsConfigLastChangeTime'
_g='ifSdhGeneralIfSdhRsTableSize'
_f='ifSdhGeneralStateLastChangeTime'
_e='ifSdhGeneralConfigLastChangeTime'
_d='EnabledDisabledWithNA'
_c='ifSdhMsGroupV2'
_b='ifSdhRsGroupV1'
_a='ifSdhMsRemoteDefectIndication'
_Z='ifSdhMsRxAlarmIndicationSignal'
_Y='ifSdhMsRxSignalStatus'
_X='ifSdhMsTxSignalStatus'
_W='ifSdhMsOhTransparencyBitmask'
_V='ifSdhMsConnIfBasicIfIndex'
_U='ifSdhMsName'
_T='ifSdhRsLossOfFrame'
_S='ifSdhRsTraceMismatch'
_R='ifSdhRsRxSignalStatus'
_Q='ifSdhRsTxSignalStatus'
_P='ifSdhRsTraceAlarmMode'
_O='ifSdhRsTraceExpected'
_N='ifSdhRsTraceReceived'
_M='ifSdhRsTraceTransmitted'
_L='ifSdhRsOhTransparencyBitmask'
_K='ifSdhRsConnIfBasicIfIndex'
_J='ifSdhRsName'
_I='Unsigned32WithNA'
_H='ifSdhGeneralGroupV1'
_G='deprecated'
_F='ifSdhMsIndex'
_E='ifSdhRsIndex'
_D='DisplayStringWithNA'
_C='read-only'
_B='current'
_A='LUM-IFSDH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfSdhMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfSdhMIB','lumModules')
DisplayStringWithNA,EnabledDisabledWithNA,FaultStatusWithNA,MgmtNameString,SignalStatusWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC',_D,_d,'FaultStatusWithNA','MgmtNameString','SignalStatusWithNA',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfSdhMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,52))
if mibBuilder.loadTexts:lumIfSdhMIBModule.setRevisions(('2017-06-15 00:00','2015-01-23 00:00','2014-05-16 00:00','2013-11-15 00:00','2013-05-01 00:00'))
_LumIfSdhConfs_ObjectIdentity=ObjectIdentity
lumIfSdhConfs=_LumIfSdhConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,52,1))
_LumIfSdhGroups_ObjectIdentity=ObjectIdentity
lumIfSdhGroups=_LumIfSdhGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,52,1,1))
_LumIfSdhCompl_ObjectIdentity=ObjectIdentity
lumIfSdhCompl=_LumIfSdhCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,52,1,2))
_LumIfSdhMIBObjects_ObjectIdentity=ObjectIdentity
lumIfSdhMIBObjects=_LumIfSdhMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,52,2))
_IfSdhGeneral_ObjectIdentity=ObjectIdentity
ifSdhGeneral=_IfSdhGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,52,2,1))
_IfSdhGeneralConfigLastChangeTime_Type=DateAndTime
_IfSdhGeneralConfigLastChangeTime_Object=MibScalar
ifSdhGeneralConfigLastChangeTime=_IfSdhGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,52,2,1,1),_IfSdhGeneralConfigLastChangeTime_Type())
ifSdhGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhGeneralConfigLastChangeTime.setStatus(_B)
_IfSdhGeneralStateLastChangeTime_Type=DateAndTime
_IfSdhGeneralStateLastChangeTime_Object=MibScalar
ifSdhGeneralStateLastChangeTime=_IfSdhGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,52,2,1,2),_IfSdhGeneralStateLastChangeTime_Type())
ifSdhGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhGeneralStateLastChangeTime.setStatus(_B)
_IfSdhGeneralIfSdhRsTableSize_Type=Unsigned32
_IfSdhGeneralIfSdhRsTableSize_Object=MibScalar
ifSdhGeneralIfSdhRsTableSize=_IfSdhGeneralIfSdhRsTableSize_Object((1,3,6,1,4,1,8708,2,52,2,1,3),_IfSdhGeneralIfSdhRsTableSize_Type())
ifSdhGeneralIfSdhRsTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhGeneralIfSdhRsTableSize.setStatus(_B)
_IfSdhGeneralIfSdhRsConfigLastChangeTime_Type=DateAndTime
_IfSdhGeneralIfSdhRsConfigLastChangeTime_Object=MibScalar
ifSdhGeneralIfSdhRsConfigLastChangeTime=_IfSdhGeneralIfSdhRsConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,52,2,1,4),_IfSdhGeneralIfSdhRsConfigLastChangeTime_Type())
ifSdhGeneralIfSdhRsConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhGeneralIfSdhRsConfigLastChangeTime.setStatus(_B)
_IfSdhGeneralIfSdhRsStateLastChangeTime_Type=DateAndTime
_IfSdhGeneralIfSdhRsStateLastChangeTime_Object=MibScalar
ifSdhGeneralIfSdhRsStateLastChangeTime=_IfSdhGeneralIfSdhRsStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,52,2,1,5),_IfSdhGeneralIfSdhRsStateLastChangeTime_Type())
ifSdhGeneralIfSdhRsStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhGeneralIfSdhRsStateLastChangeTime.setStatus(_B)
_IfSdhGeneralIfSdhMsTableSize_Type=Unsigned32
_IfSdhGeneralIfSdhMsTableSize_Object=MibScalar
ifSdhGeneralIfSdhMsTableSize=_IfSdhGeneralIfSdhMsTableSize_Object((1,3,6,1,4,1,8708,2,52,2,1,6),_IfSdhGeneralIfSdhMsTableSize_Type())
ifSdhGeneralIfSdhMsTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhGeneralIfSdhMsTableSize.setStatus(_B)
_IfSdhGeneralIfSdhMsConfigLastChangeTime_Type=DateAndTime
_IfSdhGeneralIfSdhMsConfigLastChangeTime_Object=MibScalar
ifSdhGeneralIfSdhMsConfigLastChangeTime=_IfSdhGeneralIfSdhMsConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,52,2,1,7),_IfSdhGeneralIfSdhMsConfigLastChangeTime_Type())
ifSdhGeneralIfSdhMsConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhGeneralIfSdhMsConfigLastChangeTime.setStatus(_B)
_IfSdhGeneralIfSdhMsStateLastChangeTime_Type=DateAndTime
_IfSdhGeneralIfSdhMsStateLastChangeTime_Object=MibScalar
ifSdhGeneralIfSdhMsStateLastChangeTime=_IfSdhGeneralIfSdhMsStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,52,2,1,8),_IfSdhGeneralIfSdhMsStateLastChangeTime_Type())
ifSdhGeneralIfSdhMsStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhGeneralIfSdhMsStateLastChangeTime.setStatus(_B)
_IfSdhRsList_ObjectIdentity=ObjectIdentity
ifSdhRsList=_IfSdhRsList_ObjectIdentity((1,3,6,1,4,1,8708,2,52,2,2))
_IfSdhRsTable_Object=MibTable
ifSdhRsTable=_IfSdhRsTable_Object((1,3,6,1,4,1,8708,2,52,2,2,1))
if mibBuilder.loadTexts:ifSdhRsTable.setStatus(_B)
_IfSdhRsEntry_Object=MibTableRow
ifSdhRsEntry=_IfSdhRsEntry_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1))
ifSdhRsEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:ifSdhRsEntry.setStatus(_B)
_IfSdhRsIndex_Type=Unsigned32
_IfSdhRsIndex_Object=MibTableColumn
ifSdhRsIndex=_IfSdhRsIndex_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,1),_IfSdhRsIndex_Type())
ifSdhRsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsIndex.setStatus(_B)
_IfSdhRsName_Type=MgmtNameString
_IfSdhRsName_Object=MibTableColumn
ifSdhRsName=_IfSdhRsName_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,2),_IfSdhRsName_Type())
ifSdhRsName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsName.setStatus(_B)
_IfSdhRsConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfSdhRsConnIfBasicIfIndex_Object=MibTableColumn
ifSdhRsConnIfBasicIfIndex=_IfSdhRsConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,3),_IfSdhRsConnIfBasicIfIndex_Type())
ifSdhRsConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsConnIfBasicIfIndex.setStatus(_B)
class _IfSdhRsOhTransparencyBitmask_Type(Unsigned32WithNA):defaultValue=0
_IfSdhRsOhTransparencyBitmask_Type.__name__=_I
_IfSdhRsOhTransparencyBitmask_Object=MibTableColumn
ifSdhRsOhTransparencyBitmask=_IfSdhRsOhTransparencyBitmask_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,4),_IfSdhRsOhTransparencyBitmask_Type())
ifSdhRsOhTransparencyBitmask.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsOhTransparencyBitmask.setStatus(_B)
class _IfSdhRsTraceTransmitted_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfSdhRsTraceTransmitted_Type.__name__=_D
_IfSdhRsTraceTransmitted_Object=MibTableColumn
ifSdhRsTraceTransmitted=_IfSdhRsTraceTransmitted_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,5),_IfSdhRsTraceTransmitted_Type())
ifSdhRsTraceTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsTraceTransmitted.setStatus(_B)
class _IfSdhRsTraceReceived_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfSdhRsTraceReceived_Type.__name__=_D
_IfSdhRsTraceReceived_Object=MibTableColumn
ifSdhRsTraceReceived=_IfSdhRsTraceReceived_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,6),_IfSdhRsTraceReceived_Type())
ifSdhRsTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsTraceReceived.setStatus(_B)
class _IfSdhRsTraceExpected_Type(DisplayStringWithNA):defaultValue=OctetString('');subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfSdhRsTraceExpected_Type.__name__=_D
_IfSdhRsTraceExpected_Object=MibTableColumn
ifSdhRsTraceExpected=_IfSdhRsTraceExpected_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,7),_IfSdhRsTraceExpected_Type())
ifSdhRsTraceExpected.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsTraceExpected.setStatus(_B)
class _IfSdhRsTraceAlarmMode_Type(EnabledDisabledWithNA):defaultValue=1
_IfSdhRsTraceAlarmMode_Type.__name__=_d
_IfSdhRsTraceAlarmMode_Object=MibTableColumn
ifSdhRsTraceAlarmMode=_IfSdhRsTraceAlarmMode_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,8),_IfSdhRsTraceAlarmMode_Type())
ifSdhRsTraceAlarmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsTraceAlarmMode.setStatus(_B)
_IfSdhRsTxSignalStatus_Type=SignalStatusWithNA
_IfSdhRsTxSignalStatus_Object=MibTableColumn
ifSdhRsTxSignalStatus=_IfSdhRsTxSignalStatus_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,9),_IfSdhRsTxSignalStatus_Type())
ifSdhRsTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsTxSignalStatus.setStatus(_B)
_IfSdhRsRxSignalStatus_Type=SignalStatusWithNA
_IfSdhRsRxSignalStatus_Object=MibTableColumn
ifSdhRsRxSignalStatus=_IfSdhRsRxSignalStatus_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,10),_IfSdhRsRxSignalStatus_Type())
ifSdhRsRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsRxSignalStatus.setStatus(_B)
_IfSdhRsTraceMismatch_Type=FaultStatusWithNA
_IfSdhRsTraceMismatch_Object=MibTableColumn
ifSdhRsTraceMismatch=_IfSdhRsTraceMismatch_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,11),_IfSdhRsTraceMismatch_Type())
ifSdhRsTraceMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsTraceMismatch.setStatus(_B)
_IfSdhRsLossOfFrame_Type=FaultStatusWithNA
_IfSdhRsLossOfFrame_Object=MibTableColumn
ifSdhRsLossOfFrame=_IfSdhRsLossOfFrame_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,12),_IfSdhRsLossOfFrame_Type())
ifSdhRsLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsLossOfFrame.setStatus(_B)
_IfSdhRsTxLossOfFrame_Type=FaultStatusWithNA
_IfSdhRsTxLossOfFrame_Object=MibTableColumn
ifSdhRsTxLossOfFrame=_IfSdhRsTxLossOfFrame_Object((1,3,6,1,4,1,8708,2,52,2,2,1,1,13),_IfSdhRsTxLossOfFrame_Type())
ifSdhRsTxLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhRsTxLossOfFrame.setStatus(_B)
_IfSdhMsList_ObjectIdentity=ObjectIdentity
ifSdhMsList=_IfSdhMsList_ObjectIdentity((1,3,6,1,4,1,8708,2,52,2,3))
_IfSdhMsTable_Object=MibTable
ifSdhMsTable=_IfSdhMsTable_Object((1,3,6,1,4,1,8708,2,52,2,3,1))
if mibBuilder.loadTexts:ifSdhMsTable.setStatus(_B)
_IfSdhMsEntry_Object=MibTableRow
ifSdhMsEntry=_IfSdhMsEntry_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1))
ifSdhMsEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:ifSdhMsEntry.setStatus(_B)
_IfSdhMsIndex_Type=Unsigned32
_IfSdhMsIndex_Object=MibTableColumn
ifSdhMsIndex=_IfSdhMsIndex_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,1),_IfSdhMsIndex_Type())
ifSdhMsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsIndex.setStatus(_B)
_IfSdhMsName_Type=MgmtNameString
_IfSdhMsName_Object=MibTableColumn
ifSdhMsName=_IfSdhMsName_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,2),_IfSdhMsName_Type())
ifSdhMsName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsName.setStatus(_B)
_IfSdhMsConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfSdhMsConnIfBasicIfIndex_Object=MibTableColumn
ifSdhMsConnIfBasicIfIndex=_IfSdhMsConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,3),_IfSdhMsConnIfBasicIfIndex_Type())
ifSdhMsConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsConnIfBasicIfIndex.setStatus(_B)
class _IfSdhMsOhTransparencyBitmask_Type(Unsigned32WithNA):defaultValue=0
_IfSdhMsOhTransparencyBitmask_Type.__name__=_I
_IfSdhMsOhTransparencyBitmask_Object=MibTableColumn
ifSdhMsOhTransparencyBitmask=_IfSdhMsOhTransparencyBitmask_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,4),_IfSdhMsOhTransparencyBitmask_Type())
ifSdhMsOhTransparencyBitmask.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsOhTransparencyBitmask.setStatus(_B)
_IfSdhMsTxSignalStatus_Type=SignalStatusWithNA
_IfSdhMsTxSignalStatus_Object=MibTableColumn
ifSdhMsTxSignalStatus=_IfSdhMsTxSignalStatus_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,5),_IfSdhMsTxSignalStatus_Type())
ifSdhMsTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsTxSignalStatus.setStatus(_B)
_IfSdhMsRxSignalStatus_Type=SignalStatusWithNA
_IfSdhMsRxSignalStatus_Object=MibTableColumn
ifSdhMsRxSignalStatus=_IfSdhMsRxSignalStatus_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,6),_IfSdhMsRxSignalStatus_Type())
ifSdhMsRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsRxSignalStatus.setStatus(_B)
_IfSdhMsRxAlarmIndicationSignal_Type=FaultStatusWithNA
_IfSdhMsRxAlarmIndicationSignal_Object=MibTableColumn
ifSdhMsRxAlarmIndicationSignal=_IfSdhMsRxAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,7),_IfSdhMsRxAlarmIndicationSignal_Type())
ifSdhMsRxAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsRxAlarmIndicationSignal.setStatus(_B)
_IfSdhMsRemoteDefectIndication_Type=FaultStatusWithNA
_IfSdhMsRemoteDefectIndication_Object=MibTableColumn
ifSdhMsRemoteDefectIndication=_IfSdhMsRemoteDefectIndication_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,8),_IfSdhMsRemoteDefectIndication_Type())
ifSdhMsRemoteDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsRemoteDefectIndication.setStatus(_B)
_IfSdhMsTxAlarmIndicationSignal_Type=FaultStatusWithNA
_IfSdhMsTxAlarmIndicationSignal_Object=MibTableColumn
ifSdhMsTxAlarmIndicationSignal=_IfSdhMsTxAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,52,2,3,1,1,9),_IfSdhMsTxAlarmIndicationSignal_Type())
ifSdhMsTxAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifSdhMsTxAlarmIndicationSignal.setStatus(_B)
_IfSdhAuList_ObjectIdentity=ObjectIdentity
ifSdhAuList=_IfSdhAuList_ObjectIdentity((1,3,6,1,4,1,8708,2,52,2,4))
_IfSdhVcList_ObjectIdentity=ObjectIdentity
ifSdhVcList=_IfSdhVcList_ObjectIdentity((1,3,6,1,4,1,8708,2,52,2,5))
ifSdhGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,52,1,1,1))
ifSdhGeneralGroupV1.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ifSdhGeneralGroupV1.setStatus(_B)
ifSdhRsGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,52,1,1,2))
ifSdhRsGroupV1.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ifSdhRsGroupV1.setStatus(_G)
ifSdhMsGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,52,1,1,3))
ifSdhMsGroupV1.setObjects(*((_A,_F),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ifSdhMsGroupV1.setStatus(_G)
ifSdhMsGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,52,1,1,4))
ifSdhMsGroupV2.setObjects(*((_A,_F),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_m)))
if mibBuilder.loadTexts:ifSdhMsGroupV2.setStatus(_B)
ifSdhRsGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,52,1,1,5))
ifSdhRsGroupV2.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_n)))
if mibBuilder.loadTexts:ifSdhRsGroupV2.setStatus(_B)
lumIfSdhComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,52,1,2,1))
lumIfSdhComplV1.setObjects(*((_A,_H),(_A,_b),(_A,_o)))
if mibBuilder.loadTexts:lumIfSdhComplV1.setStatus(_G)
lumIfSdhComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,52,1,2,2))
lumIfSdhComplV2.setObjects(*((_A,_H),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:lumIfSdhComplV2.setStatus(_G)
lumIfSdhComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,52,1,2,3))
lumIfSdhComplV3.setObjects(*((_A,_H),(_A,_p),(_A,_c)))
if mibBuilder.loadTexts:lumIfSdhComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfSdhMIBModule':lumIfSdhMIBModule,'lumIfSdhConfs':lumIfSdhConfs,'lumIfSdhGroups':lumIfSdhGroups,_H:ifSdhGeneralGroupV1,_b:ifSdhRsGroupV1,_o:ifSdhMsGroupV1,_c:ifSdhMsGroupV2,_p:ifSdhRsGroupV2,'lumIfSdhCompl':lumIfSdhCompl,'lumIfSdhComplV1':lumIfSdhComplV1,'lumIfSdhComplV2':lumIfSdhComplV2,'lumIfSdhComplV3':lumIfSdhComplV3,'lumIfSdhMIBObjects':lumIfSdhMIBObjects,'ifSdhGeneral':ifSdhGeneral,_e:ifSdhGeneralConfigLastChangeTime,_f:ifSdhGeneralStateLastChangeTime,_g:ifSdhGeneralIfSdhRsTableSize,_h:ifSdhGeneralIfSdhRsConfigLastChangeTime,_i:ifSdhGeneralIfSdhRsStateLastChangeTime,_j:ifSdhGeneralIfSdhMsTableSize,_k:ifSdhGeneralIfSdhMsConfigLastChangeTime,_l:ifSdhGeneralIfSdhMsStateLastChangeTime,'ifSdhRsList':ifSdhRsList,'ifSdhRsTable':ifSdhRsTable,'ifSdhRsEntry':ifSdhRsEntry,_E:ifSdhRsIndex,_J:ifSdhRsName,_K:ifSdhRsConnIfBasicIfIndex,_L:ifSdhRsOhTransparencyBitmask,_M:ifSdhRsTraceTransmitted,_N:ifSdhRsTraceReceived,_O:ifSdhRsTraceExpected,_P:ifSdhRsTraceAlarmMode,_Q:ifSdhRsTxSignalStatus,_R:ifSdhRsRxSignalStatus,_S:ifSdhRsTraceMismatch,_T:ifSdhRsLossOfFrame,_n:ifSdhRsTxLossOfFrame,'ifSdhMsList':ifSdhMsList,'ifSdhMsTable':ifSdhMsTable,'ifSdhMsEntry':ifSdhMsEntry,_F:ifSdhMsIndex,_U:ifSdhMsName,_V:ifSdhMsConnIfBasicIfIndex,_W:ifSdhMsOhTransparencyBitmask,_X:ifSdhMsTxSignalStatus,_Y:ifSdhMsRxSignalStatus,_Z:ifSdhMsRxAlarmIndicationSignal,_a:ifSdhMsRemoteDefectIndication,_m:ifSdhMsTxAlarmIndicationSignal,'ifSdhAuList':ifSdhAuList,'ifSdhVcList':ifSdhVcList})