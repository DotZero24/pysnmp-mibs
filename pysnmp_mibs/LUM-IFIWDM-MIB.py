_A7='ifIwdmPathGroupV1'
_A6='ifIwdmMsGroupV3'
_A5='ifIwdmRsGroupV3'
_A4='ifIwdmGeneralGroupV2'
_A3='ifIwdmMsGroupV2'
_A2='ifIwdmRsGroupV2'
_A1='ifIwdmMsGroupV1'
_A0='ifIwdmRsGroupV1'
_z='ifIwdmPathRate'
_y='ifIwdmPathRxSignalStatus'
_x='ifIwdmPathTxSignalStatus'
_w='ifIwdmPathConnIfBasicIfIndex'
_v='ifIwdmPathClientSignalFailure'
_u='ifIwdmPathBackwardDefectIndication'
_t='ifIwdmPathUId'
_s='ifIwdmPathName'
_r='ifIwdmMsRate'
_q='ifIwdmRsRate'
_p='ifIwdmGeneralIfIwdmPathStateLastChangeTime'
_o='ifIwdmGeneralIfIwdmPathConfigLastChangeTime'
_n='ifIwdmGeneralIfIwdmPathTableSize'
_m='read-write'
_l='EnabledDisabledWithNA'
_k='ifIwdmGeneralGroupV1'
_j='ifIwdmMsRxSignalStatus'
_i='ifIwdmMsTxSignalStatus'
_h='ifIwdmRsRxSignalStatus'
_g='ifIwdmRsTxSignalStatus'
_f='ifIwdmGeneralIfIwdmMsStateLastChangeTime'
_e='ifIwdmGeneralIfIwdmMsConfigLastChangeTime'
_d='ifIwdmGeneralIfIwdmMsTableSize'
_c='ifIwdmGeneralIfIwdmRsStateLastChangeTime'
_b='ifIwdmGeneralIfIwdmRsConfigLastChangeTime'
_a='ifIwdmGeneralIfIwdmRsTableSize'
_Z='ifIwdmGeneralStateLastChangeTime'
_Y='ifIwdmGeneralConfigLastChangeTime'
_X='ifIwdmPathIndex'
_W='ifIwdmMsConnIfBasicIfIndex'
_V='ifIwdmMsUpId'
_U='ifIwdmMsBackwardDefectIndication'
_T='ifIwdmMsAlarmIndicationSignal'
_S='ifIwdmMsName'
_R='ifIwdmRsConnIfBasicIfIndex'
_Q='ifIwdmRsLossOfFrame'
_P='ifIwdmRsUpId'
_O='ifIwdmRsTraceTraceMismatch'
_N='ifIwdmRsTraceAlarmMode'
_M='ifIwdmRsTraceExpected'
_L='ifIwdmRsTraceReceived'
_K='ifIwdmRsTraceTransmitted'
_J='ifIwdmRsName'
_I='Unsigned32'
_H='SignalFormat'
_G='DisplayStringWithNA'
_F='ifIwdmMsIndex'
_E='ifIwdmRsIndex'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-IFIWDM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfIwdmMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfIwdmMIB','lumModules')
DisplayStringWithNA,EnabledDisabledWithNA,FaultStatusWithNA,MgmtNameString,SignalFormat,SignalStatusWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC',_G,_l,'FaultStatusWithNA','MgmtNameString',_H,'SignalStatusWithNA','Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfIwdmMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,63))
if mibBuilder.loadTexts:lumIfIwdmMIBModule.setRevisions(('2017-06-15 00:00','2016-09-30 00:00','2016-06-14 00:00','2015-12-22 00:00','2015-01-23 00:00'))
_LumIfIwdmConfs_ObjectIdentity=ObjectIdentity
lumIfIwdmConfs=_LumIfIwdmConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,63,1))
_LumIfIwdmGroups_ObjectIdentity=ObjectIdentity
lumIfIwdmGroups=_LumIfIwdmGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,63,1,1))
_LumIfIwdmCompl_ObjectIdentity=ObjectIdentity
lumIfIwdmCompl=_LumIfIwdmCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,63,1,2))
_LumIfIwdmMIBObjects_ObjectIdentity=ObjectIdentity
lumIfIwdmMIBObjects=_LumIfIwdmMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,63,2))
_IfIwdmGeneral_ObjectIdentity=ObjectIdentity
ifIwdmGeneral=_IfIwdmGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,63,2,1))
_IfIwdmGeneralConfigLastChangeTime_Type=DateAndTime
_IfIwdmGeneralConfigLastChangeTime_Object=MibScalar
ifIwdmGeneralConfigLastChangeTime=_IfIwdmGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,63,2,1,1),_IfIwdmGeneralConfigLastChangeTime_Type())
ifIwdmGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralConfigLastChangeTime.setStatus(_B)
_IfIwdmGeneralStateLastChangeTime_Type=DateAndTime
_IfIwdmGeneralStateLastChangeTime_Object=MibScalar
ifIwdmGeneralStateLastChangeTime=_IfIwdmGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,63,2,1,2),_IfIwdmGeneralStateLastChangeTime_Type())
ifIwdmGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralStateLastChangeTime.setStatus(_B)
_IfIwdmGeneralIfIwdmRsTableSize_Type=Unsigned32
_IfIwdmGeneralIfIwdmRsTableSize_Object=MibScalar
ifIwdmGeneralIfIwdmRsTableSize=_IfIwdmGeneralIfIwdmRsTableSize_Object((1,3,6,1,4,1,8708,2,63,2,1,3),_IfIwdmGeneralIfIwdmRsTableSize_Type())
ifIwdmGeneralIfIwdmRsTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmRsTableSize.setStatus(_B)
_IfIwdmGeneralIfIwdmRsConfigLastChangeTime_Type=DateAndTime
_IfIwdmGeneralIfIwdmRsConfigLastChangeTime_Object=MibScalar
ifIwdmGeneralIfIwdmRsConfigLastChangeTime=_IfIwdmGeneralIfIwdmRsConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,63,2,1,4),_IfIwdmGeneralIfIwdmRsConfigLastChangeTime_Type())
ifIwdmGeneralIfIwdmRsConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmRsConfigLastChangeTime.setStatus(_B)
_IfIwdmGeneralIfIwdmRsStateLastChangeTime_Type=DateAndTime
_IfIwdmGeneralIfIwdmRsStateLastChangeTime_Object=MibScalar
ifIwdmGeneralIfIwdmRsStateLastChangeTime=_IfIwdmGeneralIfIwdmRsStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,63,2,1,5),_IfIwdmGeneralIfIwdmRsStateLastChangeTime_Type())
ifIwdmGeneralIfIwdmRsStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmRsStateLastChangeTime.setStatus(_B)
_IfIwdmGeneralIfIwdmMsTableSize_Type=Unsigned32
_IfIwdmGeneralIfIwdmMsTableSize_Object=MibScalar
ifIwdmGeneralIfIwdmMsTableSize=_IfIwdmGeneralIfIwdmMsTableSize_Object((1,3,6,1,4,1,8708,2,63,2,1,6),_IfIwdmGeneralIfIwdmMsTableSize_Type())
ifIwdmGeneralIfIwdmMsTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmMsTableSize.setStatus(_B)
_IfIwdmGeneralIfIwdmMsConfigLastChangeTime_Type=DateAndTime
_IfIwdmGeneralIfIwdmMsConfigLastChangeTime_Object=MibScalar
ifIwdmGeneralIfIwdmMsConfigLastChangeTime=_IfIwdmGeneralIfIwdmMsConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,63,2,1,7),_IfIwdmGeneralIfIwdmMsConfigLastChangeTime_Type())
ifIwdmGeneralIfIwdmMsConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmMsConfigLastChangeTime.setStatus(_B)
_IfIwdmGeneralIfIwdmMsStateLastChangeTime_Type=DateAndTime
_IfIwdmGeneralIfIwdmMsStateLastChangeTime_Object=MibScalar
ifIwdmGeneralIfIwdmMsStateLastChangeTime=_IfIwdmGeneralIfIwdmMsStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,63,2,1,8),_IfIwdmGeneralIfIwdmMsStateLastChangeTime_Type())
ifIwdmGeneralIfIwdmMsStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmMsStateLastChangeTime.setStatus(_B)
_IfIwdmGeneralIfIwdmPathTableSize_Type=Unsigned32
_IfIwdmGeneralIfIwdmPathTableSize_Object=MibScalar
ifIwdmGeneralIfIwdmPathTableSize=_IfIwdmGeneralIfIwdmPathTableSize_Object((1,3,6,1,4,1,8708,2,63,2,1,9),_IfIwdmGeneralIfIwdmPathTableSize_Type())
ifIwdmGeneralIfIwdmPathTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmPathTableSize.setStatus(_B)
_IfIwdmGeneralIfIwdmPathConfigLastChangeTime_Type=DateAndTime
_IfIwdmGeneralIfIwdmPathConfigLastChangeTime_Object=MibScalar
ifIwdmGeneralIfIwdmPathConfigLastChangeTime=_IfIwdmGeneralIfIwdmPathConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,63,2,1,10),_IfIwdmGeneralIfIwdmPathConfigLastChangeTime_Type())
ifIwdmGeneralIfIwdmPathConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmPathConfigLastChangeTime.setStatus(_B)
_IfIwdmGeneralIfIwdmPathStateLastChangeTime_Type=DateAndTime
_IfIwdmGeneralIfIwdmPathStateLastChangeTime_Object=MibScalar
ifIwdmGeneralIfIwdmPathStateLastChangeTime=_IfIwdmGeneralIfIwdmPathStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,63,2,1,11),_IfIwdmGeneralIfIwdmPathStateLastChangeTime_Type())
ifIwdmGeneralIfIwdmPathStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmGeneralIfIwdmPathStateLastChangeTime.setStatus(_B)
_IfIwdmRsList_ObjectIdentity=ObjectIdentity
ifIwdmRsList=_IfIwdmRsList_ObjectIdentity((1,3,6,1,4,1,8708,2,63,2,2))
_IfIwdmRsTable_Object=MibTable
ifIwdmRsTable=_IfIwdmRsTable_Object((1,3,6,1,4,1,8708,2,63,2,2,1))
if mibBuilder.loadTexts:ifIwdmRsTable.setStatus(_B)
_IfIwdmRsEntry_Object=MibTableRow
ifIwdmRsEntry=_IfIwdmRsEntry_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1))
ifIwdmRsEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:ifIwdmRsEntry.setStatus(_B)
_IfIwdmRsIndex_Type=Unsigned32
_IfIwdmRsIndex_Object=MibTableColumn
ifIwdmRsIndex=_IfIwdmRsIndex_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,1),_IfIwdmRsIndex_Type())
ifIwdmRsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsIndex.setStatus(_B)
_IfIwdmRsName_Type=MgmtNameString
_IfIwdmRsName_Object=MibTableColumn
ifIwdmRsName=_IfIwdmRsName_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,2),_IfIwdmRsName_Type())
ifIwdmRsName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsName.setStatus(_B)
class _IfIwdmRsTraceTransmitted_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IfIwdmRsTraceTransmitted_Type.__name__=_G
_IfIwdmRsTraceTransmitted_Object=MibTableColumn
ifIwdmRsTraceTransmitted=_IfIwdmRsTraceTransmitted_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,3),_IfIwdmRsTraceTransmitted_Type())
ifIwdmRsTraceTransmitted.setMaxAccess(_m)
if mibBuilder.loadTexts:ifIwdmRsTraceTransmitted.setStatus(_B)
class _IfIwdmRsTraceReceived_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IfIwdmRsTraceReceived_Type.__name__=_G
_IfIwdmRsTraceReceived_Object=MibTableColumn
ifIwdmRsTraceReceived=_IfIwdmRsTraceReceived_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,4),_IfIwdmRsTraceReceived_Type())
ifIwdmRsTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsTraceReceived.setStatus(_B)
class _IfIwdmRsTraceExpected_Type(DisplayStringWithNA):defaultValue=OctetString('');subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IfIwdmRsTraceExpected_Type.__name__=_G
_IfIwdmRsTraceExpected_Object=MibTableColumn
ifIwdmRsTraceExpected=_IfIwdmRsTraceExpected_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,5),_IfIwdmRsTraceExpected_Type())
ifIwdmRsTraceExpected.setMaxAccess(_m)
if mibBuilder.loadTexts:ifIwdmRsTraceExpected.setStatus(_B)
class _IfIwdmRsTraceAlarmMode_Type(EnabledDisabledWithNA):defaultValue=1
_IfIwdmRsTraceAlarmMode_Type.__name__=_l
_IfIwdmRsTraceAlarmMode_Object=MibTableColumn
ifIwdmRsTraceAlarmMode=_IfIwdmRsTraceAlarmMode_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,6),_IfIwdmRsTraceAlarmMode_Type())
ifIwdmRsTraceAlarmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsTraceAlarmMode.setStatus(_B)
_IfIwdmRsTraceTraceMismatch_Type=FaultStatusWithNA
_IfIwdmRsTraceTraceMismatch_Object=MibTableColumn
ifIwdmRsTraceTraceMismatch=_IfIwdmRsTraceTraceMismatch_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,7),_IfIwdmRsTraceTraceMismatch_Type())
ifIwdmRsTraceTraceMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsTraceTraceMismatch.setStatus(_B)
class _IfIwdmRsUpId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IfIwdmRsUpId_Type.__name__=_I
_IfIwdmRsUpId_Object=MibTableColumn
ifIwdmRsUpId=_IfIwdmRsUpId_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,8),_IfIwdmRsUpId_Type())
ifIwdmRsUpId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsUpId.setStatus(_B)
_IfIwdmRsLossOfFrame_Type=FaultStatusWithNA
_IfIwdmRsLossOfFrame_Object=MibTableColumn
ifIwdmRsLossOfFrame=_IfIwdmRsLossOfFrame_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,9),_IfIwdmRsLossOfFrame_Type())
ifIwdmRsLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsLossOfFrame.setStatus(_B)
_IfIwdmRsConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfIwdmRsConnIfBasicIfIndex_Object=MibTableColumn
ifIwdmRsConnIfBasicIfIndex=_IfIwdmRsConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,10),_IfIwdmRsConnIfBasicIfIndex_Type())
ifIwdmRsConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsConnIfBasicIfIndex.setStatus(_B)
_IfIwdmRsTxSignalStatus_Type=SignalStatusWithNA
_IfIwdmRsTxSignalStatus_Object=MibTableColumn
ifIwdmRsTxSignalStatus=_IfIwdmRsTxSignalStatus_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,11),_IfIwdmRsTxSignalStatus_Type())
ifIwdmRsTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsTxSignalStatus.setStatus(_B)
_IfIwdmRsRxSignalStatus_Type=SignalStatusWithNA
_IfIwdmRsRxSignalStatus_Object=MibTableColumn
ifIwdmRsRxSignalStatus=_IfIwdmRsRxSignalStatus_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,12),_IfIwdmRsRxSignalStatus_Type())
ifIwdmRsRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsRxSignalStatus.setStatus(_B)
class _IfIwdmRsRate_Type(SignalFormat):defaultValue=75
_IfIwdmRsRate_Type.__name__=_H
_IfIwdmRsRate_Object=MibTableColumn
ifIwdmRsRate=_IfIwdmRsRate_Object((1,3,6,1,4,1,8708,2,63,2,2,1,1,13),_IfIwdmRsRate_Type())
ifIwdmRsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmRsRate.setStatus(_B)
_IfIwdmMsList_ObjectIdentity=ObjectIdentity
ifIwdmMsList=_IfIwdmMsList_ObjectIdentity((1,3,6,1,4,1,8708,2,63,2,3))
_IfIwdmMsTable_Object=MibTable
ifIwdmMsTable=_IfIwdmMsTable_Object((1,3,6,1,4,1,8708,2,63,2,3,1))
if mibBuilder.loadTexts:ifIwdmMsTable.setStatus(_B)
_IfIwdmMsEntry_Object=MibTableRow
ifIwdmMsEntry=_IfIwdmMsEntry_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1))
ifIwdmMsEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:ifIwdmMsEntry.setStatus(_B)
_IfIwdmMsIndex_Type=Unsigned32
_IfIwdmMsIndex_Object=MibTableColumn
ifIwdmMsIndex=_IfIwdmMsIndex_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,1),_IfIwdmMsIndex_Type())
ifIwdmMsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsIndex.setStatus(_B)
_IfIwdmMsName_Type=MgmtNameString
_IfIwdmMsName_Object=MibTableColumn
ifIwdmMsName=_IfIwdmMsName_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,2),_IfIwdmMsName_Type())
ifIwdmMsName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsName.setStatus(_B)
_IfIwdmMsAlarmIndicationSignal_Type=FaultStatusWithNA
_IfIwdmMsAlarmIndicationSignal_Object=MibTableColumn
ifIwdmMsAlarmIndicationSignal=_IfIwdmMsAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,3),_IfIwdmMsAlarmIndicationSignal_Type())
ifIwdmMsAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsAlarmIndicationSignal.setStatus(_B)
_IfIwdmMsBackwardDefectIndication_Type=FaultStatusWithNA
_IfIwdmMsBackwardDefectIndication_Object=MibTableColumn
ifIwdmMsBackwardDefectIndication=_IfIwdmMsBackwardDefectIndication_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,4),_IfIwdmMsBackwardDefectIndication_Type())
ifIwdmMsBackwardDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsBackwardDefectIndication.setStatus(_B)
class _IfIwdmMsUpId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IfIwdmMsUpId_Type.__name__=_I
_IfIwdmMsUpId_Object=MibTableColumn
ifIwdmMsUpId=_IfIwdmMsUpId_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,5),_IfIwdmMsUpId_Type())
ifIwdmMsUpId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsUpId.setStatus(_B)
_IfIwdmMsConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfIwdmMsConnIfBasicIfIndex_Object=MibTableColumn
ifIwdmMsConnIfBasicIfIndex=_IfIwdmMsConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,6),_IfIwdmMsConnIfBasicIfIndex_Type())
ifIwdmMsConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsConnIfBasicIfIndex.setStatus(_B)
_IfIwdmMsTxSignalStatus_Type=SignalStatusWithNA
_IfIwdmMsTxSignalStatus_Object=MibTableColumn
ifIwdmMsTxSignalStatus=_IfIwdmMsTxSignalStatus_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,7),_IfIwdmMsTxSignalStatus_Type())
ifIwdmMsTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsTxSignalStatus.setStatus(_B)
_IfIwdmMsRxSignalStatus_Type=SignalStatusWithNA
_IfIwdmMsRxSignalStatus_Object=MibTableColumn
ifIwdmMsRxSignalStatus=_IfIwdmMsRxSignalStatus_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,8),_IfIwdmMsRxSignalStatus_Type())
ifIwdmMsRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsRxSignalStatus.setStatus(_B)
class _IfIwdmMsRate_Type(SignalFormat):defaultValue=75
_IfIwdmMsRate_Type.__name__=_H
_IfIwdmMsRate_Object=MibTableColumn
ifIwdmMsRate=_IfIwdmMsRate_Object((1,3,6,1,4,1,8708,2,63,2,3,1,1,9),_IfIwdmMsRate_Type())
ifIwdmMsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmMsRate.setStatus(_B)
_IfIwdmPathList_ObjectIdentity=ObjectIdentity
ifIwdmPathList=_IfIwdmPathList_ObjectIdentity((1,3,6,1,4,1,8708,2,63,2,4))
_IfIwdmPathTable_Object=MibTable
ifIwdmPathTable=_IfIwdmPathTable_Object((1,3,6,1,4,1,8708,2,63,2,4,1))
if mibBuilder.loadTexts:ifIwdmPathTable.setStatus(_B)
_IfIwdmPathEntry_Object=MibTableRow
ifIwdmPathEntry=_IfIwdmPathEntry_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1))
ifIwdmPathEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:ifIwdmPathEntry.setStatus(_B)
_IfIwdmPathIndex_Type=Unsigned32
_IfIwdmPathIndex_Object=MibTableColumn
ifIwdmPathIndex=_IfIwdmPathIndex_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,1),_IfIwdmPathIndex_Type())
ifIwdmPathIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathIndex.setStatus(_B)
_IfIwdmPathName_Type=MgmtNameString
_IfIwdmPathName_Object=MibTableColumn
ifIwdmPathName=_IfIwdmPathName_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,2),_IfIwdmPathName_Type())
ifIwdmPathName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathName.setStatus(_B)
_IfIwdmPathBackwardDefectIndication_Type=FaultStatusWithNA
_IfIwdmPathBackwardDefectIndication_Object=MibTableColumn
ifIwdmPathBackwardDefectIndication=_IfIwdmPathBackwardDefectIndication_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,3),_IfIwdmPathBackwardDefectIndication_Type())
ifIwdmPathBackwardDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathBackwardDefectIndication.setStatus(_B)
_IfIwdmPathClientSignalFailure_Type=FaultStatusWithNA
_IfIwdmPathClientSignalFailure_Object=MibTableColumn
ifIwdmPathClientSignalFailure=_IfIwdmPathClientSignalFailure_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,4),_IfIwdmPathClientSignalFailure_Type())
ifIwdmPathClientSignalFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathClientSignalFailure.setStatus(_B)
class _IfIwdmPathUId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IfIwdmPathUId_Type.__name__=_I
_IfIwdmPathUId_Object=MibTableColumn
ifIwdmPathUId=_IfIwdmPathUId_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,5),_IfIwdmPathUId_Type())
ifIwdmPathUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathUId.setStatus(_B)
_IfIwdmPathConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfIwdmPathConnIfBasicIfIndex_Object=MibTableColumn
ifIwdmPathConnIfBasicIfIndex=_IfIwdmPathConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,6),_IfIwdmPathConnIfBasicIfIndex_Type())
ifIwdmPathConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathConnIfBasicIfIndex.setStatus(_B)
_IfIwdmPathTxSignalStatus_Type=SignalStatusWithNA
_IfIwdmPathTxSignalStatus_Object=MibTableColumn
ifIwdmPathTxSignalStatus=_IfIwdmPathTxSignalStatus_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,7),_IfIwdmPathTxSignalStatus_Type())
ifIwdmPathTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathTxSignalStatus.setStatus(_B)
_IfIwdmPathRxSignalStatus_Type=SignalStatusWithNA
_IfIwdmPathRxSignalStatus_Object=MibTableColumn
ifIwdmPathRxSignalStatus=_IfIwdmPathRxSignalStatus_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,8),_IfIwdmPathRxSignalStatus_Type())
ifIwdmPathRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathRxSignalStatus.setStatus(_B)
class _IfIwdmPathRate_Type(SignalFormat):defaultValue=2147483647
_IfIwdmPathRate_Type.__name__=_H
_IfIwdmPathRate_Object=MibTableColumn
ifIwdmPathRate=_IfIwdmPathRate_Object((1,3,6,1,4,1,8708,2,63,2,4,1,1,9),_IfIwdmPathRate_Type())
ifIwdmPathRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifIwdmPathRate.setStatus(_B)
ifIwdmGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,1))
ifIwdmGeneralGroupV1.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ifIwdmGeneralGroupV1.setStatus(_D)
ifIwdmGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,2))
ifIwdmGeneralGroupV2.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ifIwdmGeneralGroupV2.setStatus(_B)
ifIwdmRsGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,3))
ifIwdmRsGroupV1.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ifIwdmRsGroupV1.setStatus(_D)
ifIwdmMsGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,4))
ifIwdmMsGroupV1.setObjects(*((_A,_F),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ifIwdmMsGroupV1.setStatus(_D)
ifIwdmRsGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,5))
ifIwdmRsGroupV2.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ifIwdmRsGroupV2.setStatus(_D)
ifIwdmMsGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,6))
ifIwdmMsGroupV2.setObjects(*((_A,_F),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ifIwdmMsGroupV2.setStatus(_D)
ifIwdmRsGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,7))
ifIwdmRsGroupV3.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_g),(_A,_h),(_A,_q)))
if mibBuilder.loadTexts:ifIwdmRsGroupV3.setStatus(_B)
ifIwdmMsGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,8))
ifIwdmMsGroupV3.setObjects(*((_A,_F),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_i),(_A,_j),(_A,_r)))
if mibBuilder.loadTexts:ifIwdmMsGroupV3.setStatus(_B)
ifIwdmPathGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,63,1,1,9))
ifIwdmPathGroupV1.setObjects(*((_A,_X),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ifIwdmPathGroupV1.setStatus(_B)
lumIfIwdmComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,63,1,2,1))
lumIfIwdmComplV1.setObjects(*((_A,_k),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:lumIfIwdmComplV1.setStatus(_D)
lumIfIwdmComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,63,1,2,2))
lumIfIwdmComplV2.setObjects(*((_A,_k),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:lumIfIwdmComplV2.setStatus(_D)
lumIfIwdmComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,63,1,2,3))
lumIfIwdmComplV3.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:lumIfIwdmComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfIwdmMIBModule':lumIfIwdmMIBModule,'lumIfIwdmConfs':lumIfIwdmConfs,'lumIfIwdmGroups':lumIfIwdmGroups,_k:ifIwdmGeneralGroupV1,_A4:ifIwdmGeneralGroupV2,_A0:ifIwdmRsGroupV1,_A1:ifIwdmMsGroupV1,_A2:ifIwdmRsGroupV2,_A3:ifIwdmMsGroupV2,_A5:ifIwdmRsGroupV3,_A6:ifIwdmMsGroupV3,_A7:ifIwdmPathGroupV1,'lumIfIwdmCompl':lumIfIwdmCompl,'lumIfIwdmComplV1':lumIfIwdmComplV1,'lumIfIwdmComplV2':lumIfIwdmComplV2,'lumIfIwdmComplV3':lumIfIwdmComplV3,'lumIfIwdmMIBObjects':lumIfIwdmMIBObjects,'ifIwdmGeneral':ifIwdmGeneral,_Y:ifIwdmGeneralConfigLastChangeTime,_Z:ifIwdmGeneralStateLastChangeTime,_a:ifIwdmGeneralIfIwdmRsTableSize,_b:ifIwdmGeneralIfIwdmRsConfigLastChangeTime,_c:ifIwdmGeneralIfIwdmRsStateLastChangeTime,_d:ifIwdmGeneralIfIwdmMsTableSize,_e:ifIwdmGeneralIfIwdmMsConfigLastChangeTime,_f:ifIwdmGeneralIfIwdmMsStateLastChangeTime,_n:ifIwdmGeneralIfIwdmPathTableSize,_o:ifIwdmGeneralIfIwdmPathConfigLastChangeTime,_p:ifIwdmGeneralIfIwdmPathStateLastChangeTime,'ifIwdmRsList':ifIwdmRsList,'ifIwdmRsTable':ifIwdmRsTable,'ifIwdmRsEntry':ifIwdmRsEntry,_E:ifIwdmRsIndex,_J:ifIwdmRsName,_K:ifIwdmRsTraceTransmitted,_L:ifIwdmRsTraceReceived,_M:ifIwdmRsTraceExpected,_N:ifIwdmRsTraceAlarmMode,_O:ifIwdmRsTraceTraceMismatch,_P:ifIwdmRsUpId,_Q:ifIwdmRsLossOfFrame,_R:ifIwdmRsConnIfBasicIfIndex,_g:ifIwdmRsTxSignalStatus,_h:ifIwdmRsRxSignalStatus,_q:ifIwdmRsRate,'ifIwdmMsList':ifIwdmMsList,'ifIwdmMsTable':ifIwdmMsTable,'ifIwdmMsEntry':ifIwdmMsEntry,_F:ifIwdmMsIndex,_S:ifIwdmMsName,_T:ifIwdmMsAlarmIndicationSignal,_U:ifIwdmMsBackwardDefectIndication,_V:ifIwdmMsUpId,_W:ifIwdmMsConnIfBasicIfIndex,_i:ifIwdmMsTxSignalStatus,_j:ifIwdmMsRxSignalStatus,_r:ifIwdmMsRate,'ifIwdmPathList':ifIwdmPathList,'ifIwdmPathTable':ifIwdmPathTable,'ifIwdmPathEntry':ifIwdmPathEntry,_X:ifIwdmPathIndex,_s:ifIwdmPathName,_u:ifIwdmPathBackwardDefectIndication,_v:ifIwdmPathClientSignalFailure,_t:ifIwdmPathUId,_w:ifIwdmPathConnIfBasicIfIndex,_x:ifIwdmPathTxSignalStatus,_y:ifIwdmPathRxSignalStatus,_z:ifIwdmPathRate})