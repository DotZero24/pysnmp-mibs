_Aj='ifOtnMonTraceGroupV4'
_Ai='ifOtnMonPmGroupV3'
_Ah='ifOtnMonTraceGroupV3'
_Ag='ifOtnMonTraceGroupV2'
_Af='ifOtnMonPmGroupV1'
_Ae='ifOtnMonTraceUpPortId'
_Ad='ifOtnMonPmUpPortId'
_Ac='ifOtnMonTcmSwitchCriteria'
_Ab='ifOtnMonPmRxLockedDefectIndication'
_Aa='ifOtnMonSmBackwardIncomingAlignmentError'
_AZ='ifOtnMonSmIncomingAlignmentError'
_AY='ifOtnMonSmBackwardDefectIndication'
_AX='ifOtnMonSmRxSignalStatus'
_AW='ifOtnMonSmTxSignalStatus'
_AV='ifOtnMonSmConnIfBasicIfIndex'
_AU='ifOtnMonSmName'
_AT='ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime'
_AS='ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime'
_AR='ifOtnMonGeneralIfOtnMonTraceTableSize'
_AQ='ifOtnMonGeneralIfOtnMonPmStateLastChangeTime'
_AP='ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime'
_AO='ifOtnMonGeneralIfOtnMonPmTableSize'
_AN='ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime'
_AM='ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime'
_AL='ifOtnMonGeneralIfOtnMonTcmTableSize'
_AK='ifOtnMonGeneralIfOtnMonSmStateLastChangeTime'
_AJ='ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime'
_AI='ifOtnMonGeneralIfOtnMonSmTableSize'
_AH='ifOtnMonGeneralStateLastChangeTime'
_AG='ifOtnMonGeneralConfigLastChangeTime'
_AF='TruthValueWithNA'
_AE='TcmNumber'
_AD='OtnTIMDetModeWithNA'
_AC='ifOtnMonTraceGroupV1'
_AB='ifOtnMonTcmGroupV1'
_AA='ifOtnMonTraceConnOtnDirection'
_A9='ifOtnMonPmTxLockedDefectIndication'
_A8='ifOtnMonPmTxOpenConnectionIndication'
_A7='ifOtnMonPmTxAlarmIndicationSignal'
_A6='ifOtnMonPmTxBackwardDefectIndication'
_A5='ifOtnMonTcmIncomingAlignmentError'
_A4='ifOtnMonTcmLossOfTandemConnection'
_A3='ifOtnMonTcmRxLockedDefectIndication'
_A2='ifOtnMonTcmRxOpenConnectionIndication'
_A1='ifOtnMonTcmRxAlarmIndicationSignal'
_A0='ifOtnMonTcmBackwardIncomingAlignmentError'
_z='ifOtnMonTcmBackwardDefectIndication'
_y='ifOtnMonTcmRxSignalStatus'
_x='ifOtnMonTcmTxSignalStatus'
_w='ifOtnMonTcmTcmNumber'
_v='ifOtnMonTcmMode'
_u='ifOtnMonTcmAlarmMode'
_t='ifOtnMonTcmConnOduIndex'
_s='ifOtnMonTcmName'
_r='ifOtnMonSmIndex'
_q='Integer32'
_p='OtnAlarmMode'
_o='EnabledDisabledWithNA'
_n='ifOtnMonTcmGroupV2'
_m='ifOtnMonPmGroupV2'
_l='ifOtnMonPmRxOpenConnectionIndication'
_k='ifOtnMonPmRxAlarmIndicationSignal'
_j='ifOtnMonPmRxBackwardDefectIndication'
_i='ifOtnMonPmRxSignalStatus'
_h='ifOtnMonPmTxSignalStatus'
_g='ifOtnMonPmAlarmMode'
_f='ifOtnMonPmConnOduIndex'
_e='ifOtnMonPmName'
_d='ifOtnMonTcmIndex'
_c='ifOtnMonTraceTraceMismatch'
_b='ifOtnMonTraceRxSignalStatus'
_a='ifOtnMonTraceTxSignalStatus'
_Z='ifOtnMonTraceTIMConsequenceActionsDisabled'
_Y='ifOtnMonTraceTraceAlarmMode'
_X='ifOtnMonTraceTraceIdMMDetectionMode'
_W='ifOtnMonTraceOpSpecificTraceReceived'
_V='ifOtnMonTraceOpSpecificTraceTransmitted'
_U='ifOtnMonTraceDapiTraceExpected'
_T='ifOtnMonTraceDapiTraceReceived'
_S='ifOtnMonTraceDapiTraceReceivedByte0'
_R='ifOtnMonTraceDapiTraceTransmitted'
_Q='ifOtnMonTraceSapiTraceExpected'
_P='ifOtnMonTraceSapiTraceReceived'
_O='ifOtnMonTraceSapiTraceReceivedByte0'
_N='ifOtnMonTraceSapiTraceTransmitted'
_M='ifOtnMonTraceConnOtnType'
_L='ifOtnMonTraceConnOtnIndex'
_K='ifOtnMonTraceName'
_J='ifOtnMonPmIndex'
_I='ifOtnMonSmGroupV1'
_H='ifOtnMonGeneralGroupV1'
_G='read-write'
_F='ifOtnMonTraceIndex'
_E='DisplayStringWithNA'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-IFOTNMON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfOtnMonMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfOtnMonMIB','lumModules')
DisplayStringWithNA,EnabledDisabledWithNA,FaultStatusWithNA,MgmtNameString,OtnAlarmMode,OtnDirectionWithNA,OtnTIMDetModeWithNA,OtnTypeWithNA,SignalStatusWithNA,TcmMode,TcmNumber,TruthValueWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC',_E,_o,'FaultStatusWithNA','MgmtNameString',_p,'OtnDirectionWithNA',_AD,'OtnTypeWithNA','SignalStatusWithNA','TcmMode',_AE,_AF,'Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_q,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfOtnMonMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,55))
if mibBuilder.loadTexts:lumIfOtnMonMIBModule.setRevisions(('2017-06-22 00:00','2016-11-30 00:00','2016-11-04 00:00','2015-05-29 00:00','2014-09-30 00:00','2014-05-16 00:00','2013-11-15 00:00','2013-05-01 00:00'))
_LumIfOtnMonConfs_ObjectIdentity=ObjectIdentity
lumIfOtnMonConfs=_LumIfOtnMonConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,55,1))
_LumIfOtnMonGroups_ObjectIdentity=ObjectIdentity
lumIfOtnMonGroups=_LumIfOtnMonGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,55,1,1))
_LumIfOtnMonCompl_ObjectIdentity=ObjectIdentity
lumIfOtnMonCompl=_LumIfOtnMonCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,55,1,2))
_LumIfOtnMonMIBObjects_ObjectIdentity=ObjectIdentity
lumIfOtnMonMIBObjects=_LumIfOtnMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,55,2))
_IfOtnMonGeneral_ObjectIdentity=ObjectIdentity
ifOtnMonGeneral=_IfOtnMonGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,55,2,1))
_IfOtnMonGeneralConfigLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralConfigLastChangeTime_Object=MibScalar
ifOtnMonGeneralConfigLastChangeTime=_IfOtnMonGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,1),_IfOtnMonGeneralConfigLastChangeTime_Type())
ifOtnMonGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralConfigLastChangeTime.setStatus(_B)
_IfOtnMonGeneralStateLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralStateLastChangeTime_Object=MibScalar
ifOtnMonGeneralStateLastChangeTime=_IfOtnMonGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,2),_IfOtnMonGeneralStateLastChangeTime_Type())
ifOtnMonGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralStateLastChangeTime.setStatus(_B)
_IfOtnMonGeneralIfOtnMonSmTableSize_Type=Unsigned32
_IfOtnMonGeneralIfOtnMonSmTableSize_Object=MibScalar
ifOtnMonGeneralIfOtnMonSmTableSize=_IfOtnMonGeneralIfOtnMonSmTableSize_Object((1,3,6,1,4,1,8708,2,55,2,1,3),_IfOtnMonGeneralIfOtnMonSmTableSize_Type())
ifOtnMonGeneralIfOtnMonSmTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonSmTableSize.setStatus(_B)
_IfOtnMonGeneralIfOtnMonSmConfigLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralIfOtnMonSmConfigLastChangeTime_Object=MibScalar
ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime=_IfOtnMonGeneralIfOtnMonSmConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,4),_IfOtnMonGeneralIfOtnMonSmConfigLastChangeTime_Type())
ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime.setStatus(_B)
_IfOtnMonGeneralIfOtnMonSmStateLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralIfOtnMonSmStateLastChangeTime_Object=MibScalar
ifOtnMonGeneralIfOtnMonSmStateLastChangeTime=_IfOtnMonGeneralIfOtnMonSmStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,5),_IfOtnMonGeneralIfOtnMonSmStateLastChangeTime_Type())
ifOtnMonGeneralIfOtnMonSmStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonSmStateLastChangeTime.setStatus(_B)
_IfOtnMonGeneralIfOtnMonTcmTableSize_Type=Unsigned32
_IfOtnMonGeneralIfOtnMonTcmTableSize_Object=MibScalar
ifOtnMonGeneralIfOtnMonTcmTableSize=_IfOtnMonGeneralIfOtnMonTcmTableSize_Object((1,3,6,1,4,1,8708,2,55,2,1,6),_IfOtnMonGeneralIfOtnMonTcmTableSize_Type())
ifOtnMonGeneralIfOtnMonTcmTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonTcmTableSize.setStatus(_B)
_IfOtnMonGeneralIfOtnMonTcmConfigLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralIfOtnMonTcmConfigLastChangeTime_Object=MibScalar
ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime=_IfOtnMonGeneralIfOtnMonTcmConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,7),_IfOtnMonGeneralIfOtnMonTcmConfigLastChangeTime_Type())
ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime.setStatus(_B)
_IfOtnMonGeneralIfOtnMonTcmStateLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralIfOtnMonTcmStateLastChangeTime_Object=MibScalar
ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime=_IfOtnMonGeneralIfOtnMonTcmStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,8),_IfOtnMonGeneralIfOtnMonTcmStateLastChangeTime_Type())
ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime.setStatus(_B)
_IfOtnMonGeneralIfOtnMonPmTableSize_Type=Unsigned32
_IfOtnMonGeneralIfOtnMonPmTableSize_Object=MibScalar
ifOtnMonGeneralIfOtnMonPmTableSize=_IfOtnMonGeneralIfOtnMonPmTableSize_Object((1,3,6,1,4,1,8708,2,55,2,1,9),_IfOtnMonGeneralIfOtnMonPmTableSize_Type())
ifOtnMonGeneralIfOtnMonPmTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonPmTableSize.setStatus(_B)
_IfOtnMonGeneralIfOtnMonPmConfigLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralIfOtnMonPmConfigLastChangeTime_Object=MibScalar
ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime=_IfOtnMonGeneralIfOtnMonPmConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,10),_IfOtnMonGeneralIfOtnMonPmConfigLastChangeTime_Type())
ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime.setStatus(_B)
_IfOtnMonGeneralIfOtnMonPmStateLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralIfOtnMonPmStateLastChangeTime_Object=MibScalar
ifOtnMonGeneralIfOtnMonPmStateLastChangeTime=_IfOtnMonGeneralIfOtnMonPmStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,11),_IfOtnMonGeneralIfOtnMonPmStateLastChangeTime_Type())
ifOtnMonGeneralIfOtnMonPmStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonPmStateLastChangeTime.setStatus(_B)
_IfOtnMonGeneralIfOtnMonTraceTableSize_Type=Unsigned32
_IfOtnMonGeneralIfOtnMonTraceTableSize_Object=MibScalar
ifOtnMonGeneralIfOtnMonTraceTableSize=_IfOtnMonGeneralIfOtnMonTraceTableSize_Object((1,3,6,1,4,1,8708,2,55,2,1,12),_IfOtnMonGeneralIfOtnMonTraceTableSize_Type())
ifOtnMonGeneralIfOtnMonTraceTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonTraceTableSize.setStatus(_B)
_IfOtnMonGeneralIfOtnMonTraceConfigLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralIfOtnMonTraceConfigLastChangeTime_Object=MibScalar
ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime=_IfOtnMonGeneralIfOtnMonTraceConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,13),_IfOtnMonGeneralIfOtnMonTraceConfigLastChangeTime_Type())
ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime.setStatus(_B)
_IfOtnMonGeneralIfOtnMonTraceStateLastChangeTime_Type=DateAndTime
_IfOtnMonGeneralIfOtnMonTraceStateLastChangeTime_Object=MibScalar
ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime=_IfOtnMonGeneralIfOtnMonTraceStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,55,2,1,14),_IfOtnMonGeneralIfOtnMonTraceStateLastChangeTime_Type())
ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime.setStatus(_B)
_IfOtnMonSmList_ObjectIdentity=ObjectIdentity
ifOtnMonSmList=_IfOtnMonSmList_ObjectIdentity((1,3,6,1,4,1,8708,2,55,2,2))
_IfOtnMonSmTable_Object=MibTable
ifOtnMonSmTable=_IfOtnMonSmTable_Object((1,3,6,1,4,1,8708,2,55,2,2,1))
if mibBuilder.loadTexts:ifOtnMonSmTable.setStatus(_B)
_IfOtnMonSmEntry_Object=MibTableRow
ifOtnMonSmEntry=_IfOtnMonSmEntry_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1))
ifOtnMonSmEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:ifOtnMonSmEntry.setStatus(_B)
_IfOtnMonSmIndex_Type=Unsigned32
_IfOtnMonSmIndex_Object=MibTableColumn
ifOtnMonSmIndex=_IfOtnMonSmIndex_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1,1),_IfOtnMonSmIndex_Type())
ifOtnMonSmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonSmIndex.setStatus(_B)
_IfOtnMonSmName_Type=MgmtNameString
_IfOtnMonSmName_Object=MibTableColumn
ifOtnMonSmName=_IfOtnMonSmName_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1,2),_IfOtnMonSmName_Type())
ifOtnMonSmName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonSmName.setStatus(_B)
_IfOtnMonSmConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfOtnMonSmConnIfBasicIfIndex_Object=MibTableColumn
ifOtnMonSmConnIfBasicIfIndex=_IfOtnMonSmConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1,3),_IfOtnMonSmConnIfBasicIfIndex_Type())
ifOtnMonSmConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonSmConnIfBasicIfIndex.setStatus(_B)
_IfOtnMonSmTxSignalStatus_Type=SignalStatusWithNA
_IfOtnMonSmTxSignalStatus_Object=MibTableColumn
ifOtnMonSmTxSignalStatus=_IfOtnMonSmTxSignalStatus_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1,4),_IfOtnMonSmTxSignalStatus_Type())
ifOtnMonSmTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonSmTxSignalStatus.setStatus(_B)
_IfOtnMonSmRxSignalStatus_Type=SignalStatusWithNA
_IfOtnMonSmRxSignalStatus_Object=MibTableColumn
ifOtnMonSmRxSignalStatus=_IfOtnMonSmRxSignalStatus_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1,5),_IfOtnMonSmRxSignalStatus_Type())
ifOtnMonSmRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonSmRxSignalStatus.setStatus(_B)
_IfOtnMonSmBackwardDefectIndication_Type=FaultStatusWithNA
_IfOtnMonSmBackwardDefectIndication_Object=MibTableColumn
ifOtnMonSmBackwardDefectIndication=_IfOtnMonSmBackwardDefectIndication_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1,6),_IfOtnMonSmBackwardDefectIndication_Type())
ifOtnMonSmBackwardDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonSmBackwardDefectIndication.setStatus(_B)
_IfOtnMonSmIncomingAlignmentError_Type=FaultStatusWithNA
_IfOtnMonSmIncomingAlignmentError_Object=MibTableColumn
ifOtnMonSmIncomingAlignmentError=_IfOtnMonSmIncomingAlignmentError_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1,7),_IfOtnMonSmIncomingAlignmentError_Type())
ifOtnMonSmIncomingAlignmentError.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonSmIncomingAlignmentError.setStatus(_B)
_IfOtnMonSmBackwardIncomingAlignmentError_Type=FaultStatusWithNA
_IfOtnMonSmBackwardIncomingAlignmentError_Object=MibTableColumn
ifOtnMonSmBackwardIncomingAlignmentError=_IfOtnMonSmBackwardIncomingAlignmentError_Object((1,3,6,1,4,1,8708,2,55,2,2,1,1,8),_IfOtnMonSmBackwardIncomingAlignmentError_Type())
ifOtnMonSmBackwardIncomingAlignmentError.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonSmBackwardIncomingAlignmentError.setStatus(_B)
_IfOtnMonTcmList_ObjectIdentity=ObjectIdentity
ifOtnMonTcmList=_IfOtnMonTcmList_ObjectIdentity((1,3,6,1,4,1,8708,2,55,2,3))
_IfOtnMonTcmTable_Object=MibTable
ifOtnMonTcmTable=_IfOtnMonTcmTable_Object((1,3,6,1,4,1,8708,2,55,2,3,1))
if mibBuilder.loadTexts:ifOtnMonTcmTable.setStatus(_B)
_IfOtnMonTcmEntry_Object=MibTableRow
ifOtnMonTcmEntry=_IfOtnMonTcmEntry_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1))
ifOtnMonTcmEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:ifOtnMonTcmEntry.setStatus(_B)
_IfOtnMonTcmIndex_Type=Unsigned32
_IfOtnMonTcmIndex_Object=MibTableColumn
ifOtnMonTcmIndex=_IfOtnMonTcmIndex_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,1),_IfOtnMonTcmIndex_Type())
ifOtnMonTcmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmIndex.setStatus(_B)
_IfOtnMonTcmName_Type=MgmtNameString
_IfOtnMonTcmName_Object=MibTableColumn
ifOtnMonTcmName=_IfOtnMonTcmName_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,2),_IfOtnMonTcmName_Type())
ifOtnMonTcmName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmName.setStatus(_B)
_IfOtnMonTcmConnOduIndex_Type=Unsigned32WithNA
_IfOtnMonTcmConnOduIndex_Object=MibTableColumn
ifOtnMonTcmConnOduIndex=_IfOtnMonTcmConnOduIndex_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,3),_IfOtnMonTcmConnOduIndex_Type())
ifOtnMonTcmConnOduIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmConnOduIndex.setStatus(_B)
class _IfOtnMonTcmAlarmMode_Type(OtnAlarmMode):defaultValue=0
_IfOtnMonTcmAlarmMode_Type.__name__=_p
_IfOtnMonTcmAlarmMode_Object=MibTableColumn
ifOtnMonTcmAlarmMode=_IfOtnMonTcmAlarmMode_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,4),_IfOtnMonTcmAlarmMode_Type())
ifOtnMonTcmAlarmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmAlarmMode.setStatus(_B)
class _IfOtnMonTcmMode_Type(TcmMode):defaultValue=1
_IfOtnMonTcmMode_Type.__name__='TcmMode'
_IfOtnMonTcmMode_Object=MibTableColumn
ifOtnMonTcmMode=_IfOtnMonTcmMode_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,5),_IfOtnMonTcmMode_Type())
ifOtnMonTcmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmMode.setStatus(_B)
class _IfOtnMonTcmTcmNumber_Type(TcmNumber):defaultValue=0
_IfOtnMonTcmTcmNumber_Type.__name__=_AE
_IfOtnMonTcmTcmNumber_Object=MibTableColumn
ifOtnMonTcmTcmNumber=_IfOtnMonTcmTcmNumber_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,6),_IfOtnMonTcmTcmNumber_Type())
ifOtnMonTcmTcmNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmTcmNumber.setStatus(_B)
_IfOtnMonTcmTxSignalStatus_Type=SignalStatusWithNA
_IfOtnMonTcmTxSignalStatus_Object=MibTableColumn
ifOtnMonTcmTxSignalStatus=_IfOtnMonTcmTxSignalStatus_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,7),_IfOtnMonTcmTxSignalStatus_Type())
ifOtnMonTcmTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmTxSignalStatus.setStatus(_B)
_IfOtnMonTcmRxSignalStatus_Type=SignalStatusWithNA
_IfOtnMonTcmRxSignalStatus_Object=MibTableColumn
ifOtnMonTcmRxSignalStatus=_IfOtnMonTcmRxSignalStatus_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,8),_IfOtnMonTcmRxSignalStatus_Type())
ifOtnMonTcmRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmRxSignalStatus.setStatus(_B)
_IfOtnMonTcmBackwardDefectIndication_Type=FaultStatusWithNA
_IfOtnMonTcmBackwardDefectIndication_Object=MibTableColumn
ifOtnMonTcmBackwardDefectIndication=_IfOtnMonTcmBackwardDefectIndication_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,9),_IfOtnMonTcmBackwardDefectIndication_Type())
ifOtnMonTcmBackwardDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmBackwardDefectIndication.setStatus(_B)
_IfOtnMonTcmBackwardIncomingAlignmentError_Type=FaultStatusWithNA
_IfOtnMonTcmBackwardIncomingAlignmentError_Object=MibTableColumn
ifOtnMonTcmBackwardIncomingAlignmentError=_IfOtnMonTcmBackwardIncomingAlignmentError_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,10),_IfOtnMonTcmBackwardIncomingAlignmentError_Type())
ifOtnMonTcmBackwardIncomingAlignmentError.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmBackwardIncomingAlignmentError.setStatus(_B)
_IfOtnMonTcmRxAlarmIndicationSignal_Type=FaultStatusWithNA
_IfOtnMonTcmRxAlarmIndicationSignal_Object=MibTableColumn
ifOtnMonTcmRxAlarmIndicationSignal=_IfOtnMonTcmRxAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,11),_IfOtnMonTcmRxAlarmIndicationSignal_Type())
ifOtnMonTcmRxAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmRxAlarmIndicationSignal.setStatus(_B)
_IfOtnMonTcmRxOpenConnectionIndication_Type=FaultStatusWithNA
_IfOtnMonTcmRxOpenConnectionIndication_Object=MibTableColumn
ifOtnMonTcmRxOpenConnectionIndication=_IfOtnMonTcmRxOpenConnectionIndication_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,12),_IfOtnMonTcmRxOpenConnectionIndication_Type())
ifOtnMonTcmRxOpenConnectionIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmRxOpenConnectionIndication.setStatus(_B)
_IfOtnMonTcmRxLockedDefectIndication_Type=FaultStatusWithNA
_IfOtnMonTcmRxLockedDefectIndication_Object=MibTableColumn
ifOtnMonTcmRxLockedDefectIndication=_IfOtnMonTcmRxLockedDefectIndication_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,13),_IfOtnMonTcmRxLockedDefectIndication_Type())
ifOtnMonTcmRxLockedDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmRxLockedDefectIndication.setStatus(_B)
_IfOtnMonTcmLossOfTandemConnection_Type=FaultStatusWithNA
_IfOtnMonTcmLossOfTandemConnection_Object=MibTableColumn
ifOtnMonTcmLossOfTandemConnection=_IfOtnMonTcmLossOfTandemConnection_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,14),_IfOtnMonTcmLossOfTandemConnection_Type())
ifOtnMonTcmLossOfTandemConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmLossOfTandemConnection.setStatus(_B)
_IfOtnMonTcmIncomingAlignmentError_Type=FaultStatusWithNA
_IfOtnMonTcmIncomingAlignmentError_Object=MibTableColumn
ifOtnMonTcmIncomingAlignmentError=_IfOtnMonTcmIncomingAlignmentError_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,15),_IfOtnMonTcmIncomingAlignmentError_Type())
ifOtnMonTcmIncomingAlignmentError.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmIncomingAlignmentError.setStatus(_B)
class _IfOtnMonTcmSwitchCriteria_Type(EnabledDisabledWithNA):defaultValue=1
_IfOtnMonTcmSwitchCriteria_Type.__name__=_o
_IfOtnMonTcmSwitchCriteria_Object=MibTableColumn
ifOtnMonTcmSwitchCriteria=_IfOtnMonTcmSwitchCriteria_Object((1,3,6,1,4,1,8708,2,55,2,3,1,1,16),_IfOtnMonTcmSwitchCriteria_Type())
ifOtnMonTcmSwitchCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTcmSwitchCriteria.setStatus(_B)
_IfOtnMonPmList_ObjectIdentity=ObjectIdentity
ifOtnMonPmList=_IfOtnMonPmList_ObjectIdentity((1,3,6,1,4,1,8708,2,55,2,4))
_IfOtnMonPmTable_Object=MibTable
ifOtnMonPmTable=_IfOtnMonPmTable_Object((1,3,6,1,4,1,8708,2,55,2,4,1))
if mibBuilder.loadTexts:ifOtnMonPmTable.setStatus(_B)
_IfOtnMonPmEntry_Object=MibTableRow
ifOtnMonPmEntry=_IfOtnMonPmEntry_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1))
ifOtnMonPmEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:ifOtnMonPmEntry.setStatus(_B)
_IfOtnMonPmIndex_Type=Unsigned32
_IfOtnMonPmIndex_Object=MibTableColumn
ifOtnMonPmIndex=_IfOtnMonPmIndex_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,1),_IfOtnMonPmIndex_Type())
ifOtnMonPmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmIndex.setStatus(_B)
_IfOtnMonPmName_Type=MgmtNameString
_IfOtnMonPmName_Object=MibTableColumn
ifOtnMonPmName=_IfOtnMonPmName_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,2),_IfOtnMonPmName_Type())
ifOtnMonPmName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmName.setStatus(_B)
_IfOtnMonPmConnOduIndex_Type=Unsigned32WithNA
_IfOtnMonPmConnOduIndex_Object=MibTableColumn
ifOtnMonPmConnOduIndex=_IfOtnMonPmConnOduIndex_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,4),_IfOtnMonPmConnOduIndex_Type())
ifOtnMonPmConnOduIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmConnOduIndex.setStatus(_B)
class _IfOtnMonPmAlarmMode_Type(OtnAlarmMode):defaultValue=1
_IfOtnMonPmAlarmMode_Type.__name__=_p
_IfOtnMonPmAlarmMode_Object=MibTableColumn
ifOtnMonPmAlarmMode=_IfOtnMonPmAlarmMode_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,5),_IfOtnMonPmAlarmMode_Type())
ifOtnMonPmAlarmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmAlarmMode.setStatus(_B)
_IfOtnMonPmTxSignalStatus_Type=SignalStatusWithNA
_IfOtnMonPmTxSignalStatus_Object=MibTableColumn
ifOtnMonPmTxSignalStatus=_IfOtnMonPmTxSignalStatus_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,6),_IfOtnMonPmTxSignalStatus_Type())
ifOtnMonPmTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmTxSignalStatus.setStatus(_B)
_IfOtnMonPmRxSignalStatus_Type=SignalStatusWithNA
_IfOtnMonPmRxSignalStatus_Object=MibTableColumn
ifOtnMonPmRxSignalStatus=_IfOtnMonPmRxSignalStatus_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,7),_IfOtnMonPmRxSignalStatus_Type())
ifOtnMonPmRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmRxSignalStatus.setStatus(_B)
_IfOtnMonPmRxBackwardDefectIndication_Type=FaultStatusWithNA
_IfOtnMonPmRxBackwardDefectIndication_Object=MibTableColumn
ifOtnMonPmRxBackwardDefectIndication=_IfOtnMonPmRxBackwardDefectIndication_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,8),_IfOtnMonPmRxBackwardDefectIndication_Type())
ifOtnMonPmRxBackwardDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmRxBackwardDefectIndication.setStatus(_B)
_IfOtnMonPmRxAlarmIndicationSignal_Type=FaultStatusWithNA
_IfOtnMonPmRxAlarmIndicationSignal_Object=MibTableColumn
ifOtnMonPmRxAlarmIndicationSignal=_IfOtnMonPmRxAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,9),_IfOtnMonPmRxAlarmIndicationSignal_Type())
ifOtnMonPmRxAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmRxAlarmIndicationSignal.setStatus(_B)
_IfOtnMonPmRxOpenConnectionIndication_Type=FaultStatusWithNA
_IfOtnMonPmRxOpenConnectionIndication_Object=MibTableColumn
ifOtnMonPmRxOpenConnectionIndication=_IfOtnMonPmRxOpenConnectionIndication_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,10),_IfOtnMonPmRxOpenConnectionIndication_Type())
ifOtnMonPmRxOpenConnectionIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmRxOpenConnectionIndication.setStatus(_B)
_IfOtnMonPmRxLockedDefectIndication_Type=FaultStatusWithNA
_IfOtnMonPmRxLockedDefectIndication_Object=MibTableColumn
ifOtnMonPmRxLockedDefectIndication=_IfOtnMonPmRxLockedDefectIndication_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,11),_IfOtnMonPmRxLockedDefectIndication_Type())
ifOtnMonPmRxLockedDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmRxLockedDefectIndication.setStatus(_B)
_IfOtnMonPmTxBackwardDefectIndication_Type=FaultStatusWithNA
_IfOtnMonPmTxBackwardDefectIndication_Object=MibTableColumn
ifOtnMonPmTxBackwardDefectIndication=_IfOtnMonPmTxBackwardDefectIndication_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,12),_IfOtnMonPmTxBackwardDefectIndication_Type())
ifOtnMonPmTxBackwardDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmTxBackwardDefectIndication.setStatus(_B)
_IfOtnMonPmTxAlarmIndicationSignal_Type=FaultStatusWithNA
_IfOtnMonPmTxAlarmIndicationSignal_Object=MibTableColumn
ifOtnMonPmTxAlarmIndicationSignal=_IfOtnMonPmTxAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,13),_IfOtnMonPmTxAlarmIndicationSignal_Type())
ifOtnMonPmTxAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmTxAlarmIndicationSignal.setStatus(_B)
_IfOtnMonPmTxOpenConnectionIndication_Type=FaultStatusWithNA
_IfOtnMonPmTxOpenConnectionIndication_Object=MibTableColumn
ifOtnMonPmTxOpenConnectionIndication=_IfOtnMonPmTxOpenConnectionIndication_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,14),_IfOtnMonPmTxOpenConnectionIndication_Type())
ifOtnMonPmTxOpenConnectionIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmTxOpenConnectionIndication.setStatus(_B)
_IfOtnMonPmTxLockedDefectIndication_Type=FaultStatusWithNA
_IfOtnMonPmTxLockedDefectIndication_Object=MibTableColumn
ifOtnMonPmTxLockedDefectIndication=_IfOtnMonPmTxLockedDefectIndication_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,15),_IfOtnMonPmTxLockedDefectIndication_Type())
ifOtnMonPmTxLockedDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmTxLockedDefectIndication.setStatus(_B)
class _IfOtnMonPmUpPortId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_IfOtnMonPmUpPortId_Type.__name__=_q
_IfOtnMonPmUpPortId_Object=MibTableColumn
ifOtnMonPmUpPortId=_IfOtnMonPmUpPortId_Object((1,3,6,1,4,1,8708,2,55,2,4,1,1,16),_IfOtnMonPmUpPortId_Type())
ifOtnMonPmUpPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonPmUpPortId.setStatus(_B)
_IfOtnMonTraceList_ObjectIdentity=ObjectIdentity
ifOtnMonTraceList=_IfOtnMonTraceList_ObjectIdentity((1,3,6,1,4,1,8708,2,55,2,5))
_IfOtnMonTraceTable_Object=MibTable
ifOtnMonTraceTable=_IfOtnMonTraceTable_Object((1,3,6,1,4,1,8708,2,55,2,5,1))
if mibBuilder.loadTexts:ifOtnMonTraceTable.setStatus(_B)
_IfOtnMonTraceEntry_Object=MibTableRow
ifOtnMonTraceEntry=_IfOtnMonTraceEntry_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1))
ifOtnMonTraceEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:ifOtnMonTraceEntry.setStatus(_B)
_IfOtnMonTraceIndex_Type=Unsigned32
_IfOtnMonTraceIndex_Object=MibTableColumn
ifOtnMonTraceIndex=_IfOtnMonTraceIndex_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,1),_IfOtnMonTraceIndex_Type())
ifOtnMonTraceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceIndex.setStatus(_B)
_IfOtnMonTraceName_Type=MgmtNameString
_IfOtnMonTraceName_Object=MibTableColumn
ifOtnMonTraceName=_IfOtnMonTraceName_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,2),_IfOtnMonTraceName_Type())
ifOtnMonTraceName.setMaxAccess('read-create')
if mibBuilder.loadTexts:ifOtnMonTraceName.setStatus(_B)
_IfOtnMonTraceConnOtnType_Type=OtnTypeWithNA
_IfOtnMonTraceConnOtnType_Object=MibTableColumn
ifOtnMonTraceConnOtnType=_IfOtnMonTraceConnOtnType_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,3),_IfOtnMonTraceConnOtnType_Type())
ifOtnMonTraceConnOtnType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceConnOtnType.setStatus(_B)
_IfOtnMonTraceConnOtnIndex_Type=Unsigned32WithNA
_IfOtnMonTraceConnOtnIndex_Object=MibTableColumn
ifOtnMonTraceConnOtnIndex=_IfOtnMonTraceConnOtnIndex_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,4),_IfOtnMonTraceConnOtnIndex_Type())
ifOtnMonTraceConnOtnIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceConnOtnIndex.setStatus(_B)
class _IfOtnMonTraceSapiTraceTransmitted_Type(DisplayStringWithNA):defaultValue=OctetString('');subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfOtnMonTraceSapiTraceTransmitted_Type.__name__=_E
_IfOtnMonTraceSapiTraceTransmitted_Object=MibTableColumn
ifOtnMonTraceSapiTraceTransmitted=_IfOtnMonTraceSapiTraceTransmitted_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,5),_IfOtnMonTraceSapiTraceTransmitted_Type())
ifOtnMonTraceSapiTraceTransmitted.setMaxAccess(_G)
if mibBuilder.loadTexts:ifOtnMonTraceSapiTraceTransmitted.setStatus(_B)
_IfOtnMonTraceSapiTraceReceivedByte0_Type=Unsigned32WithNA
_IfOtnMonTraceSapiTraceReceivedByte0_Object=MibTableColumn
ifOtnMonTraceSapiTraceReceivedByte0=_IfOtnMonTraceSapiTraceReceivedByte0_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,6),_IfOtnMonTraceSapiTraceReceivedByte0_Type())
ifOtnMonTraceSapiTraceReceivedByte0.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceSapiTraceReceivedByte0.setStatus(_D)
class _IfOtnMonTraceSapiTraceReceived_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfOtnMonTraceSapiTraceReceived_Type.__name__=_E
_IfOtnMonTraceSapiTraceReceived_Object=MibTableColumn
ifOtnMonTraceSapiTraceReceived=_IfOtnMonTraceSapiTraceReceived_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,7),_IfOtnMonTraceSapiTraceReceived_Type())
ifOtnMonTraceSapiTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceSapiTraceReceived.setStatus(_B)
class _IfOtnMonTraceSapiTraceExpected_Type(DisplayStringWithNA):defaultValue=OctetString('');subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfOtnMonTraceSapiTraceExpected_Type.__name__=_E
_IfOtnMonTraceSapiTraceExpected_Object=MibTableColumn
ifOtnMonTraceSapiTraceExpected=_IfOtnMonTraceSapiTraceExpected_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,8),_IfOtnMonTraceSapiTraceExpected_Type())
ifOtnMonTraceSapiTraceExpected.setMaxAccess(_G)
if mibBuilder.loadTexts:ifOtnMonTraceSapiTraceExpected.setStatus(_B)
class _IfOtnMonTraceDapiTraceTransmitted_Type(DisplayStringWithNA):defaultValue=OctetString('');subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfOtnMonTraceDapiTraceTransmitted_Type.__name__=_E
_IfOtnMonTraceDapiTraceTransmitted_Object=MibTableColumn
ifOtnMonTraceDapiTraceTransmitted=_IfOtnMonTraceDapiTraceTransmitted_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,9),_IfOtnMonTraceDapiTraceTransmitted_Type())
ifOtnMonTraceDapiTraceTransmitted.setMaxAccess(_G)
if mibBuilder.loadTexts:ifOtnMonTraceDapiTraceTransmitted.setStatus(_B)
_IfOtnMonTraceDapiTraceReceivedByte0_Type=Unsigned32WithNA
_IfOtnMonTraceDapiTraceReceivedByte0_Object=MibTableColumn
ifOtnMonTraceDapiTraceReceivedByte0=_IfOtnMonTraceDapiTraceReceivedByte0_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,10),_IfOtnMonTraceDapiTraceReceivedByte0_Type())
ifOtnMonTraceDapiTraceReceivedByte0.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceDapiTraceReceivedByte0.setStatus(_D)
class _IfOtnMonTraceDapiTraceReceived_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfOtnMonTraceDapiTraceReceived_Type.__name__=_E
_IfOtnMonTraceDapiTraceReceived_Object=MibTableColumn
ifOtnMonTraceDapiTraceReceived=_IfOtnMonTraceDapiTraceReceived_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,11),_IfOtnMonTraceDapiTraceReceived_Type())
ifOtnMonTraceDapiTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceDapiTraceReceived.setStatus(_B)
class _IfOtnMonTraceDapiTraceExpected_Type(DisplayStringWithNA):defaultValue=OctetString('');subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfOtnMonTraceDapiTraceExpected_Type.__name__=_E
_IfOtnMonTraceDapiTraceExpected_Object=MibTableColumn
ifOtnMonTraceDapiTraceExpected=_IfOtnMonTraceDapiTraceExpected_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,12),_IfOtnMonTraceDapiTraceExpected_Type())
ifOtnMonTraceDapiTraceExpected.setMaxAccess(_G)
if mibBuilder.loadTexts:ifOtnMonTraceDapiTraceExpected.setStatus(_B)
class _IfOtnMonTraceOpSpecificTraceTransmitted_Type(DisplayStringWithNA):defaultValue=OctetString('');subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IfOtnMonTraceOpSpecificTraceTransmitted_Type.__name__=_E
_IfOtnMonTraceOpSpecificTraceTransmitted_Object=MibTableColumn
ifOtnMonTraceOpSpecificTraceTransmitted=_IfOtnMonTraceOpSpecificTraceTransmitted_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,13),_IfOtnMonTraceOpSpecificTraceTransmitted_Type())
ifOtnMonTraceOpSpecificTraceTransmitted.setMaxAccess(_G)
if mibBuilder.loadTexts:ifOtnMonTraceOpSpecificTraceTransmitted.setStatus(_B)
class _IfOtnMonTraceOpSpecificTraceReceived_Type(DisplayStringWithNA):subtypeSpec=DisplayStringWithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IfOtnMonTraceOpSpecificTraceReceived_Type.__name__=_E
_IfOtnMonTraceOpSpecificTraceReceived_Object=MibTableColumn
ifOtnMonTraceOpSpecificTraceReceived=_IfOtnMonTraceOpSpecificTraceReceived_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,14),_IfOtnMonTraceOpSpecificTraceReceived_Type())
ifOtnMonTraceOpSpecificTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceOpSpecificTraceReceived.setStatus(_B)
class _IfOtnMonTraceTraceIdMMDetectionMode_Type(OtnTIMDetModeWithNA):defaultValue=0
_IfOtnMonTraceTraceIdMMDetectionMode_Type.__name__=_AD
_IfOtnMonTraceTraceIdMMDetectionMode_Object=MibTableColumn
ifOtnMonTraceTraceIdMMDetectionMode=_IfOtnMonTraceTraceIdMMDetectionMode_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,15),_IfOtnMonTraceTraceIdMMDetectionMode_Type())
ifOtnMonTraceTraceIdMMDetectionMode.setMaxAccess(_G)
if mibBuilder.loadTexts:ifOtnMonTraceTraceIdMMDetectionMode.setStatus(_B)
class _IfOtnMonTraceTraceAlarmMode_Type(EnabledDisabledWithNA):defaultValue=1
_IfOtnMonTraceTraceAlarmMode_Type.__name__=_o
_IfOtnMonTraceTraceAlarmMode_Object=MibTableColumn
ifOtnMonTraceTraceAlarmMode=_IfOtnMonTraceTraceAlarmMode_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,16),_IfOtnMonTraceTraceAlarmMode_Type())
ifOtnMonTraceTraceAlarmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceTraceAlarmMode.setStatus(_D)
class _IfOtnMonTraceTIMConsequenceActionsDisabled_Type(TruthValueWithNA):defaultValue=0
_IfOtnMonTraceTIMConsequenceActionsDisabled_Type.__name__=_AF
_IfOtnMonTraceTIMConsequenceActionsDisabled_Object=MibTableColumn
ifOtnMonTraceTIMConsequenceActionsDisabled=_IfOtnMonTraceTIMConsequenceActionsDisabled_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,17),_IfOtnMonTraceTIMConsequenceActionsDisabled_Type())
ifOtnMonTraceTIMConsequenceActionsDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceTIMConsequenceActionsDisabled.setStatus(_B)
_IfOtnMonTraceTxSignalStatus_Type=SignalStatusWithNA
_IfOtnMonTraceTxSignalStatus_Object=MibTableColumn
ifOtnMonTraceTxSignalStatus=_IfOtnMonTraceTxSignalStatus_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,18),_IfOtnMonTraceTxSignalStatus_Type())
ifOtnMonTraceTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceTxSignalStatus.setStatus(_B)
_IfOtnMonTraceRxSignalStatus_Type=SignalStatusWithNA
_IfOtnMonTraceRxSignalStatus_Object=MibTableColumn
ifOtnMonTraceRxSignalStatus=_IfOtnMonTraceRxSignalStatus_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,19),_IfOtnMonTraceRxSignalStatus_Type())
ifOtnMonTraceRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceRxSignalStatus.setStatus(_B)
_IfOtnMonTraceTraceMismatch_Type=FaultStatusWithNA
_IfOtnMonTraceTraceMismatch_Object=MibTableColumn
ifOtnMonTraceTraceMismatch=_IfOtnMonTraceTraceMismatch_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,20),_IfOtnMonTraceTraceMismatch_Type())
ifOtnMonTraceTraceMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceTraceMismatch.setStatus(_B)
_IfOtnMonTraceConnOtnDirection_Type=OtnDirectionWithNA
_IfOtnMonTraceConnOtnDirection_Object=MibTableColumn
ifOtnMonTraceConnOtnDirection=_IfOtnMonTraceConnOtnDirection_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,21),_IfOtnMonTraceConnOtnDirection_Type())
ifOtnMonTraceConnOtnDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceConnOtnDirection.setStatus(_B)
class _IfOtnMonTraceUpPortId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_IfOtnMonTraceUpPortId_Type.__name__=_q
_IfOtnMonTraceUpPortId_Object=MibTableColumn
ifOtnMonTraceUpPortId=_IfOtnMonTraceUpPortId_Object((1,3,6,1,4,1,8708,2,55,2,5,1,1,22),_IfOtnMonTraceUpPortId_Type())
ifOtnMonTraceUpPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnMonTraceUpPortId.setStatus(_B)
ifOtnMonGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,1))
ifOtnMonGeneralGroupV1.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:ifOtnMonGeneralGroupV1.setStatus(_B)
ifOtnMonSmGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,2))
ifOtnMonSmGroupV1.setObjects(*((_A,_r),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:ifOtnMonSmGroupV1.setStatus(_B)
ifOtnMonTcmGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,3))
ifOtnMonTcmGroupV1.setObjects(*((_A,_d),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:ifOtnMonTcmGroupV1.setStatus(_D)
ifOtnMonPmGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,4))
ifOtnMonPmGroupV1.setObjects(*((_A,_J),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_Ab)))
if mibBuilder.loadTexts:ifOtnMonPmGroupV1.setStatus(_D)
ifOtnMonTraceGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,5))
ifOtnMonTraceGroupV1.setObjects(*((_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ifOtnMonTraceGroupV1.setStatus(_D)
ifOtnMonPmGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,6))
ifOtnMonPmGroupV2.setObjects(*((_A,_J),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:ifOtnMonPmGroupV2.setStatus(_D)
ifOtnMonTcmGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,7))
ifOtnMonTcmGroupV2.setObjects(*((_A,_d),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_Ac)))
if mibBuilder.loadTexts:ifOtnMonTcmGroupV2.setStatus(_B)
ifOtnMonTraceGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,8))
ifOtnMonTraceGroupV2.setObjects(*((_A,_F),(_A,_K),(_A,_M),(_A,_L),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ifOtnMonTraceGroupV2.setStatus(_D)
ifOtnMonTraceGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,9))
ifOtnMonTraceGroupV3.setObjects(*((_A,_F),(_A,_K),(_A,_M),(_A,_L),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_AA)))
if mibBuilder.loadTexts:ifOtnMonTraceGroupV3.setStatus(_D)
ifOtnMonPmGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,10))
ifOtnMonPmGroupV3.setObjects(*((_A,_J),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_Ad)))
if mibBuilder.loadTexts:ifOtnMonPmGroupV3.setStatus(_B)
ifOtnMonTraceGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,55,1,1,11))
ifOtnMonTraceGroupV4.setObjects(*((_A,_F),(_A,_K),(_A,_M),(_A,_L),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_AA),(_A,_Ae)))
if mibBuilder.loadTexts:ifOtnMonTraceGroupV4.setStatus(_B)
lumIfOtnMonComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,55,1,2,1))
lumIfOtnMonComplV1.setObjects(*((_A,_H),(_A,_I),(_A,_AB),(_A,_Af),(_A,_AC)))
if mibBuilder.loadTexts:lumIfOtnMonComplV1.setStatus(_D)
lumIfOtnMonComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,55,1,2,2))
lumIfOtnMonComplV2.setObjects(*((_A,_H),(_A,_I),(_A,_AB),(_A,_m),(_A,_AC)))
if mibBuilder.loadTexts:lumIfOtnMonComplV2.setStatus(_D)
lumIfOtnMonComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,55,1,2,3))
lumIfOtnMonComplV3.setObjects(*((_A,_H),(_A,_I),(_A,_n),(_A,_m),(_A,_Ag)))
if mibBuilder.loadTexts:lumIfOtnMonComplV3.setStatus(_D)
lumIfOtnMonComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,55,1,2,4))
lumIfOtnMonComplV4.setObjects(*((_A,_H),(_A,_I),(_A,_n),(_A,_m),(_A,_Ah)))
if mibBuilder.loadTexts:lumIfOtnMonComplV4.setStatus(_D)
lumIfOtnMonComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,55,1,2,5))
lumIfOtnMonComplV5.setObjects(*((_A,_H),(_A,_I),(_A,_n),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:lumIfOtnMonComplV5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfOtnMonMIBModule':lumIfOtnMonMIBModule,'lumIfOtnMonConfs':lumIfOtnMonConfs,'lumIfOtnMonGroups':lumIfOtnMonGroups,_H:ifOtnMonGeneralGroupV1,_I:ifOtnMonSmGroupV1,_AB:ifOtnMonTcmGroupV1,_Af:ifOtnMonPmGroupV1,_AC:ifOtnMonTraceGroupV1,_m:ifOtnMonPmGroupV2,_n:ifOtnMonTcmGroupV2,_Ag:ifOtnMonTraceGroupV2,_Ah:ifOtnMonTraceGroupV3,_Ai:ifOtnMonPmGroupV3,_Aj:ifOtnMonTraceGroupV4,'lumIfOtnMonCompl':lumIfOtnMonCompl,'lumIfOtnMonComplV1':lumIfOtnMonComplV1,'lumIfOtnMonComplV2':lumIfOtnMonComplV2,'lumIfOtnMonComplV3':lumIfOtnMonComplV3,'lumIfOtnMonComplV4':lumIfOtnMonComplV4,'lumIfOtnMonComplV5':lumIfOtnMonComplV5,'lumIfOtnMonMIBObjects':lumIfOtnMonMIBObjects,'ifOtnMonGeneral':ifOtnMonGeneral,_AG:ifOtnMonGeneralConfigLastChangeTime,_AH:ifOtnMonGeneralStateLastChangeTime,_AI:ifOtnMonGeneralIfOtnMonSmTableSize,_AJ:ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime,_AK:ifOtnMonGeneralIfOtnMonSmStateLastChangeTime,_AL:ifOtnMonGeneralIfOtnMonTcmTableSize,_AM:ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime,_AN:ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime,_AO:ifOtnMonGeneralIfOtnMonPmTableSize,_AP:ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime,_AQ:ifOtnMonGeneralIfOtnMonPmStateLastChangeTime,_AR:ifOtnMonGeneralIfOtnMonTraceTableSize,_AS:ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime,_AT:ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime,'ifOtnMonSmList':ifOtnMonSmList,'ifOtnMonSmTable':ifOtnMonSmTable,'ifOtnMonSmEntry':ifOtnMonSmEntry,_r:ifOtnMonSmIndex,_AU:ifOtnMonSmName,_AV:ifOtnMonSmConnIfBasicIfIndex,_AW:ifOtnMonSmTxSignalStatus,_AX:ifOtnMonSmRxSignalStatus,_AY:ifOtnMonSmBackwardDefectIndication,_AZ:ifOtnMonSmIncomingAlignmentError,_Aa:ifOtnMonSmBackwardIncomingAlignmentError,'ifOtnMonTcmList':ifOtnMonTcmList,'ifOtnMonTcmTable':ifOtnMonTcmTable,'ifOtnMonTcmEntry':ifOtnMonTcmEntry,_d:ifOtnMonTcmIndex,_s:ifOtnMonTcmName,_t:ifOtnMonTcmConnOduIndex,_u:ifOtnMonTcmAlarmMode,_v:ifOtnMonTcmMode,_w:ifOtnMonTcmTcmNumber,_x:ifOtnMonTcmTxSignalStatus,_y:ifOtnMonTcmRxSignalStatus,_z:ifOtnMonTcmBackwardDefectIndication,_A0:ifOtnMonTcmBackwardIncomingAlignmentError,_A1:ifOtnMonTcmRxAlarmIndicationSignal,_A2:ifOtnMonTcmRxOpenConnectionIndication,_A3:ifOtnMonTcmRxLockedDefectIndication,_A4:ifOtnMonTcmLossOfTandemConnection,_A5:ifOtnMonTcmIncomingAlignmentError,_Ac:ifOtnMonTcmSwitchCriteria,'ifOtnMonPmList':ifOtnMonPmList,'ifOtnMonPmTable':ifOtnMonPmTable,'ifOtnMonPmEntry':ifOtnMonPmEntry,_J:ifOtnMonPmIndex,_e:ifOtnMonPmName,_f:ifOtnMonPmConnOduIndex,_g:ifOtnMonPmAlarmMode,_h:ifOtnMonPmTxSignalStatus,_i:ifOtnMonPmRxSignalStatus,_j:ifOtnMonPmRxBackwardDefectIndication,_k:ifOtnMonPmRxAlarmIndicationSignal,_l:ifOtnMonPmRxOpenConnectionIndication,_Ab:ifOtnMonPmRxLockedDefectIndication,_A6:ifOtnMonPmTxBackwardDefectIndication,_A7:ifOtnMonPmTxAlarmIndicationSignal,_A8:ifOtnMonPmTxOpenConnectionIndication,_A9:ifOtnMonPmTxLockedDefectIndication,_Ad:ifOtnMonPmUpPortId,'ifOtnMonTraceList':ifOtnMonTraceList,'ifOtnMonTraceTable':ifOtnMonTraceTable,'ifOtnMonTraceEntry':ifOtnMonTraceEntry,_F:ifOtnMonTraceIndex,_K:ifOtnMonTraceName,_M:ifOtnMonTraceConnOtnType,_L:ifOtnMonTraceConnOtnIndex,_N:ifOtnMonTraceSapiTraceTransmitted,_O:ifOtnMonTraceSapiTraceReceivedByte0,_P:ifOtnMonTraceSapiTraceReceived,_Q:ifOtnMonTraceSapiTraceExpected,_R:ifOtnMonTraceDapiTraceTransmitted,_S:ifOtnMonTraceDapiTraceReceivedByte0,_T:ifOtnMonTraceDapiTraceReceived,_U:ifOtnMonTraceDapiTraceExpected,_V:ifOtnMonTraceOpSpecificTraceTransmitted,_W:ifOtnMonTraceOpSpecificTraceReceived,_X:ifOtnMonTraceTraceIdMMDetectionMode,_Y:ifOtnMonTraceTraceAlarmMode,_Z:ifOtnMonTraceTIMConsequenceActionsDisabled,_a:ifOtnMonTraceTxSignalStatus,_b:ifOtnMonTraceRxSignalStatus,_c:ifOtnMonTraceTraceMismatch,_AA:ifOtnMonTraceConnOtnDirection,_Ae:ifOtnMonTraceUpPortId})