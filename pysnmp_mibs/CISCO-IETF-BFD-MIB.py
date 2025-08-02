_A7='ciscoBfdSession04Group'
_A6='ciscoBfdSession03Group'
_A5='ciscoBfdSession0304Group'
_A4='ciscoBfdSessionGroup'
_A3='ciscoBfdSessDown'
_A2='ciscoBfdSessUp'
_A1='ciscoBfdSessIpMapIndex'
_A0='ciscoBfdSessDiscMapIndex'
_z='ciscoBfdSessType'
_y='ciscoBfdSessVersionNumber'
_x='ciscoBfdSessPerfPktOutHC'
_w='ciscoBfdSessPerfPktInHC'
_v='ciscoBfdSessPerfDiscTime'
_u='ciscoBfdSessPerfSessUpCount'
_t='ciscoBfdSessPerfLastCommLostDiag'
_s='ciscoBfdSessPerfLastSessDownTime'
_r='ciscoBfdSessUpTime'
_q='ciscoBfdSessPerfPktOut'
_p='ciscoBfdSessPerfPktIn'
_o='deprecated'
_n='ciscoBfdSessPerfEntry'
_m='ciscoBfdSessIndex'
_l='read-write'
_k='InetPortNumber'
_j='ciscoBfdNotificationGroup'
_i='ciscoBfdSessionPerfHCGroup'
_h='ciscoBfdSessionPerfGroup'
_g='ciscoBfdSessAuthenticationType'
_f='ciscoBfdSessAuthPresFlag'
_e='ciscoBfdSessMapBfdIndex'
_d='ciscoBfdSessRowStatus'
_c='ciscoBfdSessStorType'
_b='ciscoBfdSessDetectMult'
_a='ciscoBfdSessReqMinEchoRxInterval'
_Z='ciscoBfdSessReqMinRxInterval'
_Y='ciscoBfdSessDesiredMinTxInterval'
_X='ciscoBfdSessControlPlanIndepFlag'
_W='ciscoBfdSessEchoFuncModeDesiredFlag'
_V='ciscoBfdSessDemandModeDesiredFlag'
_U='ciscoBfdSessOperMode'
_T='ciscoBfdSessRemoteHeardFlag'
_S='ciscoBfdSessState'
_R='ciscoBfdSessUdpPort'
_Q='ciscoBfdSessRemoteDiscr'
_P='ciscoBfdVersionNumber'
_O='ciscoBfdAdminStatus'
_N='ciscoBfdSessNotificationsEnable'
_M='ciscoBfdSessInterface'
_L='ciscoBfdSessApplicationId'
_K='ciscoBfdSessAddr'
_J='ciscoBfdSessAddrType'
_I='ciscoBfdSessDiscriminator'
_H='Unsigned32'
_G='TruthValue'
_F='Integer32'
_E='ciscoBfdSessDiag'
_D='read-create'
_C='read-only'
_B='current'
_A='CISCO-IETF-BFD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_k)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_G)
ciscoIetfBfdMIB=ModuleIdentity((1,3,6,1,4,1,9,10,137))
if mibBuilder.loadTexts:ciscoIetfBfdMIB.setRevisions(('2011-03-14 00:00','2010-02-18 00:00','2008-04-24 00:00','2007-06-04 00:00'))
class CiscoBfdSessIndexTC(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CiscoBfdInterval(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class CiscoBfdDiag(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noDiagnostic',0),('controlDetectionTimeExpired',1),('echoFunctionFailed',2),('neighborSignaledSessionDown',3),('forwardingPlaneReset',4),('pathDown',5),('concatenatedPathDown',6),('administrativelyDown',7),('reverseConcatenatedPathDown',8)))
_CiscoBfdNotifications_ObjectIdentity=ObjectIdentity
ciscoBfdNotifications=_CiscoBfdNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,137,0))
_CiscoBfdObjects_ObjectIdentity=ObjectIdentity
ciscoBfdObjects=_CiscoBfdObjects_ObjectIdentity((1,3,6,1,4,1,9,10,137,1))
_CiscoBfdScalarObjects_ObjectIdentity=ObjectIdentity
ciscoBfdScalarObjects=_CiscoBfdScalarObjects_ObjectIdentity((1,3,6,1,4,1,9,10,137,1,1))
class _CiscoBfdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CiscoBfdAdminStatus_Type.__name__=_F
_CiscoBfdAdminStatus_Object=MibScalar
ciscoBfdAdminStatus=_CiscoBfdAdminStatus_Object((1,3,6,1,4,1,9,10,137,1,1,1),_CiscoBfdAdminStatus_Type())
ciscoBfdAdminStatus.setMaxAccess(_l)
if mibBuilder.loadTexts:ciscoBfdAdminStatus.setStatus(_B)
class _CiscoBfdVersionNumber_Type(Unsigned32):defaultValue=0
_CiscoBfdVersionNumber_Type.__name__=_H
_CiscoBfdVersionNumber_Object=MibScalar
ciscoBfdVersionNumber=_CiscoBfdVersionNumber_Object((1,3,6,1,4,1,9,10,137,1,1,3),_CiscoBfdVersionNumber_Type())
ciscoBfdVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdVersionNumber.setStatus(_B)
class _CiscoBfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_CiscoBfdSessNotificationsEnable_Type.__name__=_G
_CiscoBfdSessNotificationsEnable_Object=MibScalar
ciscoBfdSessNotificationsEnable=_CiscoBfdSessNotificationsEnable_Object((1,3,6,1,4,1,9,10,137,1,1,4),_CiscoBfdSessNotificationsEnable_Type())
ciscoBfdSessNotificationsEnable.setMaxAccess(_l)
if mibBuilder.loadTexts:ciscoBfdSessNotificationsEnable.setStatus(_B)
_CiscoBfdSessTable_Object=MibTable
ciscoBfdSessTable=_CiscoBfdSessTable_Object((1,3,6,1,4,1,9,10,137,1,2))
if mibBuilder.loadTexts:ciscoBfdSessTable.setStatus(_B)
_CiscoBfdSessEntry_Object=MibTableRow
ciscoBfdSessEntry=_CiscoBfdSessEntry_Object((1,3,6,1,4,1,9,10,137,1,2,1))
ciscoBfdSessEntry.setIndexNames((0,_A,_m))
if mibBuilder.loadTexts:ciscoBfdSessEntry.setStatus(_B)
_CiscoBfdSessIndex_Type=CiscoBfdSessIndexTC
_CiscoBfdSessIndex_Object=MibTableColumn
ciscoBfdSessIndex=_CiscoBfdSessIndex_Object((1,3,6,1,4,1,9,10,137,1,2,1,1),_CiscoBfdSessIndex_Type())
ciscoBfdSessIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoBfdSessIndex.setStatus(_B)
_CiscoBfdSessApplicationId_Type=Unsigned32
_CiscoBfdSessApplicationId_Object=MibTableColumn
ciscoBfdSessApplicationId=_CiscoBfdSessApplicationId_Object((1,3,6,1,4,1,9,10,137,1,2,1,2),_CiscoBfdSessApplicationId_Type())
ciscoBfdSessApplicationId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessApplicationId.setStatus(_B)
class _CiscoBfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CiscoBfdSessDiscriminator_Type.__name__=_H
_CiscoBfdSessDiscriminator_Object=MibTableColumn
ciscoBfdSessDiscriminator=_CiscoBfdSessDiscriminator_Object((1,3,6,1,4,1,9,10,137,1,2,1,3),_CiscoBfdSessDiscriminator_Type())
ciscoBfdSessDiscriminator.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessDiscriminator.setStatus(_B)
class _CiscoBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiscoBfdSessRemoteDiscr_Type.__name__=_H
_CiscoBfdSessRemoteDiscr_Object=MibTableColumn
ciscoBfdSessRemoteDiscr=_CiscoBfdSessRemoteDiscr_Object((1,3,6,1,4,1,9,10,137,1,2,1,4),_CiscoBfdSessRemoteDiscr_Type())
ciscoBfdSessRemoteDiscr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessRemoteDiscr.setStatus(_B)
class _CiscoBfdSessUdpPort_Type(InetPortNumber):defaultValue=0
_CiscoBfdSessUdpPort_Type.__name__=_k
_CiscoBfdSessUdpPort_Object=MibTableColumn
ciscoBfdSessUdpPort=_CiscoBfdSessUdpPort_Object((1,3,6,1,4,1,9,10,137,1,2,1,5),_CiscoBfdSessUdpPort_Type())
ciscoBfdSessUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessUdpPort.setStatus(_B)
class _CiscoBfdSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4),('failing',5)))
_CiscoBfdSessState_Type.__name__=_F
_CiscoBfdSessState_Object=MibTableColumn
ciscoBfdSessState=_CiscoBfdSessState_Object((1,3,6,1,4,1,9,10,137,1,2,1,6),_CiscoBfdSessState_Type())
ciscoBfdSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessState.setStatus(_B)
_CiscoBfdSessRemoteHeardFlag_Type=TruthValue
_CiscoBfdSessRemoteHeardFlag_Object=MibTableColumn
ciscoBfdSessRemoteHeardFlag=_CiscoBfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,9,10,137,1,2,1,7),_CiscoBfdSessRemoteHeardFlag_Type())
ciscoBfdSessRemoteHeardFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessRemoteHeardFlag.setStatus(_B)
_CiscoBfdSessDiag_Type=CiscoBfdDiag
_CiscoBfdSessDiag_Object=MibTableColumn
ciscoBfdSessDiag=_CiscoBfdSessDiag_Object((1,3,6,1,4,1,9,10,137,1,2,1,8),_CiscoBfdSessDiag_Type())
ciscoBfdSessDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessDiag.setStatus(_B)
class _CiscoBfdSessOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asyncModeWEchoFun',1),('asynchModeWOEchoFun',2),('demandModeWEchoFunction',3),('demandModeWOEchoFunction',4)))
_CiscoBfdSessOperMode_Type.__name__=_F
_CiscoBfdSessOperMode_Object=MibTableColumn
ciscoBfdSessOperMode=_CiscoBfdSessOperMode_Object((1,3,6,1,4,1,9,10,137,1,2,1,9),_CiscoBfdSessOperMode_Type())
ciscoBfdSessOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessOperMode.setStatus(_B)
class _CiscoBfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_CiscoBfdSessDemandModeDesiredFlag_Type.__name__=_G
_CiscoBfdSessDemandModeDesiredFlag_Object=MibTableColumn
ciscoBfdSessDemandModeDesiredFlag=_CiscoBfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,9,10,137,1,2,1,10),_CiscoBfdSessDemandModeDesiredFlag_Type())
ciscoBfdSessDemandModeDesiredFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessDemandModeDesiredFlag.setStatus(_B)
class _CiscoBfdSessEchoFuncModeDesiredFlag_Type(TruthValue):defaultValue=2
_CiscoBfdSessEchoFuncModeDesiredFlag_Type.__name__=_G
_CiscoBfdSessEchoFuncModeDesiredFlag_Object=MibTableColumn
ciscoBfdSessEchoFuncModeDesiredFlag=_CiscoBfdSessEchoFuncModeDesiredFlag_Object((1,3,6,1,4,1,9,10,137,1,2,1,11),_CiscoBfdSessEchoFuncModeDesiredFlag_Type())
ciscoBfdSessEchoFuncModeDesiredFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessEchoFuncModeDesiredFlag.setStatus(_B)
class _CiscoBfdSessControlPlanIndepFlag_Type(TruthValue):defaultValue=2
_CiscoBfdSessControlPlanIndepFlag_Type.__name__=_G
_CiscoBfdSessControlPlanIndepFlag_Object=MibTableColumn
ciscoBfdSessControlPlanIndepFlag=_CiscoBfdSessControlPlanIndepFlag_Object((1,3,6,1,4,1,9,10,137,1,2,1,12),_CiscoBfdSessControlPlanIndepFlag_Type())
ciscoBfdSessControlPlanIndepFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessControlPlanIndepFlag.setStatus(_B)
_CiscoBfdSessAddrType_Type=InetAddressType
_CiscoBfdSessAddrType_Object=MibTableColumn
ciscoBfdSessAddrType=_CiscoBfdSessAddrType_Object((1,3,6,1,4,1,9,10,137,1,2,1,13),_CiscoBfdSessAddrType_Type())
ciscoBfdSessAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessAddrType.setStatus(_B)
_CiscoBfdSessAddr_Type=InetAddress
_CiscoBfdSessAddr_Object=MibTableColumn
ciscoBfdSessAddr=_CiscoBfdSessAddr_Object((1,3,6,1,4,1,9,10,137,1,2,1,14),_CiscoBfdSessAddr_Type())
ciscoBfdSessAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessAddr.setStatus(_B)
_CiscoBfdSessDesiredMinTxInterval_Type=CiscoBfdInterval
_CiscoBfdSessDesiredMinTxInterval_Object=MibTableColumn
ciscoBfdSessDesiredMinTxInterval=_CiscoBfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,9,10,137,1,2,1,15),_CiscoBfdSessDesiredMinTxInterval_Type())
ciscoBfdSessDesiredMinTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessDesiredMinTxInterval.setStatus(_B)
_CiscoBfdSessReqMinRxInterval_Type=CiscoBfdInterval
_CiscoBfdSessReqMinRxInterval_Object=MibTableColumn
ciscoBfdSessReqMinRxInterval=_CiscoBfdSessReqMinRxInterval_Object((1,3,6,1,4,1,9,10,137,1,2,1,16),_CiscoBfdSessReqMinRxInterval_Type())
ciscoBfdSessReqMinRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessReqMinRxInterval.setStatus(_B)
_CiscoBfdSessReqMinEchoRxInterval_Type=CiscoBfdInterval
_CiscoBfdSessReqMinEchoRxInterval_Object=MibTableColumn
ciscoBfdSessReqMinEchoRxInterval=_CiscoBfdSessReqMinEchoRxInterval_Object((1,3,6,1,4,1,9,10,137,1,2,1,17),_CiscoBfdSessReqMinEchoRxInterval_Type())
ciscoBfdSessReqMinEchoRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessReqMinEchoRxInterval.setStatus(_B)
_CiscoBfdSessDetectMult_Type=Unsigned32
_CiscoBfdSessDetectMult_Object=MibTableColumn
ciscoBfdSessDetectMult=_CiscoBfdSessDetectMult_Object((1,3,6,1,4,1,9,10,137,1,2,1,18),_CiscoBfdSessDetectMult_Type())
ciscoBfdSessDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessDetectMult.setStatus(_B)
_CiscoBfdSessStorType_Type=StorageType
_CiscoBfdSessStorType_Object=MibTableColumn
ciscoBfdSessStorType=_CiscoBfdSessStorType_Object((1,3,6,1,4,1,9,10,137,1,2,1,19),_CiscoBfdSessStorType_Type())
ciscoBfdSessStorType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessStorType.setStatus(_B)
_CiscoBfdSessRowStatus_Type=RowStatus
_CiscoBfdSessRowStatus_Object=MibTableColumn
ciscoBfdSessRowStatus=_CiscoBfdSessRowStatus_Object((1,3,6,1,4,1,9,10,137,1,2,1,20),_CiscoBfdSessRowStatus_Type())
ciscoBfdSessRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessRowStatus.setStatus(_B)
class _CiscoBfdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_CiscoBfdSessAuthPresFlag_Type.__name__=_G
_CiscoBfdSessAuthPresFlag_Object=MibTableColumn
ciscoBfdSessAuthPresFlag=_CiscoBfdSessAuthPresFlag_Object((1,3,6,1,4,1,9,10,137,1,2,1,21),_CiscoBfdSessAuthPresFlag_Type())
ciscoBfdSessAuthPresFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessAuthPresFlag.setStatus(_B)
class _CiscoBfdSessAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('simplePassword',1),('keyedMD5',2),('meticulousKeyedMD5',3),('keyedSHA1',4),('meticulousKeyedSHA1',5)))
_CiscoBfdSessAuthenticationType_Type.__name__=_F
_CiscoBfdSessAuthenticationType_Object=MibTableColumn
ciscoBfdSessAuthenticationType=_CiscoBfdSessAuthenticationType_Object((1,3,6,1,4,1,9,10,137,1,2,1,22),_CiscoBfdSessAuthenticationType_Type())
ciscoBfdSessAuthenticationType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoBfdSessAuthenticationType.setStatus(_B)
class _CiscoBfdSessVersionNumber_Type(Unsigned32):defaultValue=0
_CiscoBfdSessVersionNumber_Type.__name__=_H
_CiscoBfdSessVersionNumber_Object=MibTableColumn
ciscoBfdSessVersionNumber=_CiscoBfdSessVersionNumber_Object((1,3,6,1,4,1,9,10,137,1,2,1,23),_CiscoBfdSessVersionNumber_Type())
ciscoBfdSessVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessVersionNumber.setStatus(_B)
class _CiscoBfdSessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('singleHop',1),('multiHop',2)))
_CiscoBfdSessType_Type.__name__=_F
_CiscoBfdSessType_Object=MibTableColumn
ciscoBfdSessType=_CiscoBfdSessType_Object((1,3,6,1,4,1,9,10,137,1,2,1,24),_CiscoBfdSessType_Type())
ciscoBfdSessType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessType.setStatus(_B)
_CiscoBfdSessInterface_Type=InterfaceIndex
_CiscoBfdSessInterface_Object=MibTableColumn
ciscoBfdSessInterface=_CiscoBfdSessInterface_Object((1,3,6,1,4,1,9,10,137,1,2,1,25),_CiscoBfdSessInterface_Type())
ciscoBfdSessInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessInterface.setStatus(_B)
_CiscoBfdSessPerfTable_Object=MibTable
ciscoBfdSessPerfTable=_CiscoBfdSessPerfTable_Object((1,3,6,1,4,1,9,10,137,1,3))
if mibBuilder.loadTexts:ciscoBfdSessPerfTable.setStatus(_B)
_CiscoBfdSessPerfEntry_Object=MibTableRow
ciscoBfdSessPerfEntry=_CiscoBfdSessPerfEntry_Object((1,3,6,1,4,1,9,10,137,1,3,1))
if mibBuilder.loadTexts:ciscoBfdSessPerfEntry.setStatus(_B)
_CiscoBfdSessPerfPktIn_Type=Counter32
_CiscoBfdSessPerfPktIn_Object=MibTableColumn
ciscoBfdSessPerfPktIn=_CiscoBfdSessPerfPktIn_Object((1,3,6,1,4,1,9,10,137,1,3,1,1),_CiscoBfdSessPerfPktIn_Type())
ciscoBfdSessPerfPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessPerfPktIn.setStatus(_B)
_CiscoBfdSessPerfPktOut_Type=Counter32
_CiscoBfdSessPerfPktOut_Object=MibTableColumn
ciscoBfdSessPerfPktOut=_CiscoBfdSessPerfPktOut_Object((1,3,6,1,4,1,9,10,137,1,3,1,2),_CiscoBfdSessPerfPktOut_Type())
ciscoBfdSessPerfPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessPerfPktOut.setStatus(_B)
_CiscoBfdSessUpTime_Type=TimeStamp
_CiscoBfdSessUpTime_Object=MibTableColumn
ciscoBfdSessUpTime=_CiscoBfdSessUpTime_Object((1,3,6,1,4,1,9,10,137,1,3,1,3),_CiscoBfdSessUpTime_Type())
ciscoBfdSessUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessUpTime.setStatus(_B)
_CiscoBfdSessPerfLastSessDownTime_Type=TimeStamp
_CiscoBfdSessPerfLastSessDownTime_Object=MibTableColumn
ciscoBfdSessPerfLastSessDownTime=_CiscoBfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,9,10,137,1,3,1,4),_CiscoBfdSessPerfLastSessDownTime_Type())
ciscoBfdSessPerfLastSessDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessPerfLastSessDownTime.setStatus(_B)
_CiscoBfdSessPerfLastCommLostDiag_Type=CiscoBfdDiag
_CiscoBfdSessPerfLastCommLostDiag_Object=MibTableColumn
ciscoBfdSessPerfLastCommLostDiag=_CiscoBfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,9,10,137,1,3,1,5),_CiscoBfdSessPerfLastCommLostDiag_Type())
ciscoBfdSessPerfLastCommLostDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessPerfLastCommLostDiag.setStatus(_B)
_CiscoBfdSessPerfSessUpCount_Type=Counter32
_CiscoBfdSessPerfSessUpCount_Object=MibTableColumn
ciscoBfdSessPerfSessUpCount=_CiscoBfdSessPerfSessUpCount_Object((1,3,6,1,4,1,9,10,137,1,3,1,6),_CiscoBfdSessPerfSessUpCount_Type())
ciscoBfdSessPerfSessUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessPerfSessUpCount.setStatus(_B)
_CiscoBfdSessPerfDiscTime_Type=TimeStamp
_CiscoBfdSessPerfDiscTime_Object=MibTableColumn
ciscoBfdSessPerfDiscTime=_CiscoBfdSessPerfDiscTime_Object((1,3,6,1,4,1,9,10,137,1,3,1,7),_CiscoBfdSessPerfDiscTime_Type())
ciscoBfdSessPerfDiscTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessPerfDiscTime.setStatus(_B)
_CiscoBfdSessPerfPktInHC_Type=Counter64
_CiscoBfdSessPerfPktInHC_Object=MibTableColumn
ciscoBfdSessPerfPktInHC=_CiscoBfdSessPerfPktInHC_Object((1,3,6,1,4,1,9,10,137,1,3,1,8),_CiscoBfdSessPerfPktInHC_Type())
ciscoBfdSessPerfPktInHC.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessPerfPktInHC.setStatus(_B)
_CiscoBfdSessPerfPktOutHC_Type=Counter64
_CiscoBfdSessPerfPktOutHC_Object=MibTableColumn
ciscoBfdSessPerfPktOutHC=_CiscoBfdSessPerfPktOutHC_Object((1,3,6,1,4,1,9,10,137,1,3,1,9),_CiscoBfdSessPerfPktOutHC_Type())
ciscoBfdSessPerfPktOutHC.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessPerfPktOutHC.setStatus(_B)
_CiscoBfdSessMapTable_Object=MibTable
ciscoBfdSessMapTable=_CiscoBfdSessMapTable_Object((1,3,6,1,4,1,9,10,137,1,4))
if mibBuilder.loadTexts:ciscoBfdSessMapTable.setStatus(_B)
_CiscoBfdSessMapEntry_Object=MibTableRow
ciscoBfdSessMapEntry=_CiscoBfdSessMapEntry_Object((1,3,6,1,4,1,9,10,137,1,4,1))
ciscoBfdSessMapEntry.setIndexNames((0,_A,_L),(0,_A,_I),(0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:ciscoBfdSessMapEntry.setStatus(_B)
_CiscoBfdSessMapBfdIndex_Type=CiscoBfdSessIndexTC
_CiscoBfdSessMapBfdIndex_Object=MibTableColumn
ciscoBfdSessMapBfdIndex=_CiscoBfdSessMapBfdIndex_Object((1,3,6,1,4,1,9,10,137,1,4,1,1),_CiscoBfdSessMapBfdIndex_Type())
ciscoBfdSessMapBfdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessMapBfdIndex.setStatus(_B)
_CiscoBfdSessDiscMapTable_Object=MibTable
ciscoBfdSessDiscMapTable=_CiscoBfdSessDiscMapTable_Object((1,3,6,1,4,1,9,10,137,1,5))
if mibBuilder.loadTexts:ciscoBfdSessDiscMapTable.setStatus(_B)
_CiscoBfdSessDiscMapEntry_Object=MibTableRow
ciscoBfdSessDiscMapEntry=_CiscoBfdSessDiscMapEntry_Object((1,3,6,1,4,1,9,10,137,1,5,1))
ciscoBfdSessDiscMapEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ciscoBfdSessDiscMapEntry.setStatus(_B)
_CiscoBfdSessDiscMapIndex_Type=CiscoBfdSessIndexTC
_CiscoBfdSessDiscMapIndex_Object=MibTableColumn
ciscoBfdSessDiscMapIndex=_CiscoBfdSessDiscMapIndex_Object((1,3,6,1,4,1,9,10,137,1,5,1,1),_CiscoBfdSessDiscMapIndex_Type())
ciscoBfdSessDiscMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessDiscMapIndex.setStatus(_B)
_CiscoBfdSessIpMapTable_Object=MibTable
ciscoBfdSessIpMapTable=_CiscoBfdSessIpMapTable_Object((1,3,6,1,4,1,9,10,137,1,6))
if mibBuilder.loadTexts:ciscoBfdSessIpMapTable.setStatus(_B)
_CiscoBfdSessIpMapEntry_Object=MibTableRow
ciscoBfdSessIpMapEntry=_CiscoBfdSessIpMapEntry_Object((1,3,6,1,4,1,9,10,137,1,6,1))
ciscoBfdSessIpMapEntry.setIndexNames((0,_A,_M),(0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:ciscoBfdSessIpMapEntry.setStatus(_B)
_CiscoBfdSessIpMapIndex_Type=CiscoBfdSessIndexTC
_CiscoBfdSessIpMapIndex_Object=MibTableColumn
ciscoBfdSessIpMapIndex=_CiscoBfdSessIpMapIndex_Object((1,3,6,1,4,1,9,10,137,1,6,1,1),_CiscoBfdSessIpMapIndex_Type())
ciscoBfdSessIpMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBfdSessIpMapIndex.setStatus(_B)
_CiscoBfdConformance_ObjectIdentity=ObjectIdentity
ciscoBfdConformance=_CiscoBfdConformance_ObjectIdentity((1,3,6,1,4,1,9,10,137,3))
_CiscoBfdGroups_ObjectIdentity=ObjectIdentity
ciscoBfdGroups=_CiscoBfdGroups_ObjectIdentity((1,3,6,1,4,1,9,10,137,3,1))
_CiscoBfdCompliances_ObjectIdentity=ObjectIdentity
ciscoBfdCompliances=_CiscoBfdCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,137,3,2))
ciscoBfdSessEntry.registerAugmentions((_A,_n))
ciscoBfdSessPerfEntry.setIndexNames(*ciscoBfdSessEntry.getIndexNames())
ciscoBfdSessionGroup=ObjectGroup((1,3,6,1,4,1,9,10,137,3,1,1))
ciscoBfdSessionGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_L),(_A,_I),(_A,_J),(_A,_K),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_E),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoBfdSessionGroup.setStatus(_o)
ciscoBfdSessionPerfGroup=ObjectGroup((1,3,6,1,4,1,9,10,137,3,1,2))
ciscoBfdSessionPerfGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:ciscoBfdSessionPerfGroup.setStatus(_B)
ciscoBfdSessionPerfHCGroup=ObjectGroup((1,3,6,1,4,1,9,10,137,3,1,3))
ciscoBfdSessionPerfHCGroup.setObjects(*((_A,_w),(_A,_x)))
if mibBuilder.loadTexts:ciscoBfdSessionPerfHCGroup.setStatus(_B)
ciscoBfdSession0304Group=ObjectGroup((1,3,6,1,4,1,9,10,137,3,1,5))
ciscoBfdSession0304Group.setObjects(*((_A,_N),(_A,_O),(_A,_I),(_A,_J),(_A,_K),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_E),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoBfdSession0304Group.setStatus(_B)
ciscoBfdSession03Group=ObjectGroup((1,3,6,1,4,1,9,10,137,3,1,6))
ciscoBfdSession03Group.setObjects(*((_A,_P),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:ciscoBfdSession03Group.setStatus(_B)
ciscoBfdSession04Group=ObjectGroup((1,3,6,1,4,1,9,10,137,3,1,7))
ciscoBfdSession04Group.setObjects(*((_A,_y),(_A,_z),(_A,_M),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ciscoBfdSession04Group.setStatus(_B)
ciscoBfdSessUp=NotificationType((1,3,6,1,4,1,9,10,137,0,1))
ciscoBfdSessUp.setObjects(*((_A,_E),(_A,_E)))
if mibBuilder.loadTexts:ciscoBfdSessUp.setStatus(_B)
ciscoBfdSessDown=NotificationType((1,3,6,1,4,1,9,10,137,0,2))
ciscoBfdSessDown.setObjects(*((_A,_E),(_A,_E)))
if mibBuilder.loadTexts:ciscoBfdSessDown.setStatus(_B)
ciscoBfdNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,137,3,1,4))
ciscoBfdNotificationGroup.setObjects(*((_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoBfdNotificationGroup.setStatus(_B)
ciscoBfdModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,137,3,2,1))
ciscoBfdModuleFullCompliance.setObjects(*((_A,_A4),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoBfdModuleFullCompliance.setStatus(_o)
ciscoBfdModuleFullComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,10,137,3,2,2))
ciscoBfdModuleFullComplianceRev2.setObjects(*((_A,_A5),(_A,_h),(_A,_i),(_A,_j),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:ciscoBfdModuleFullComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoBfdSessIndexTC':CiscoBfdSessIndexTC,'CiscoBfdInterval':CiscoBfdInterval,'CiscoBfdDiag':CiscoBfdDiag,'ciscoIetfBfdMIB':ciscoIetfBfdMIB,'ciscoBfdNotifications':ciscoBfdNotifications,_A2:ciscoBfdSessUp,_A3:ciscoBfdSessDown,'ciscoBfdObjects':ciscoBfdObjects,'ciscoBfdScalarObjects':ciscoBfdScalarObjects,_O:ciscoBfdAdminStatus,_P:ciscoBfdVersionNumber,_N:ciscoBfdSessNotificationsEnable,'ciscoBfdSessTable':ciscoBfdSessTable,'ciscoBfdSessEntry':ciscoBfdSessEntry,_m:ciscoBfdSessIndex,_L:ciscoBfdSessApplicationId,_I:ciscoBfdSessDiscriminator,_Q:ciscoBfdSessRemoteDiscr,_R:ciscoBfdSessUdpPort,_S:ciscoBfdSessState,_T:ciscoBfdSessRemoteHeardFlag,_E:ciscoBfdSessDiag,_U:ciscoBfdSessOperMode,_V:ciscoBfdSessDemandModeDesiredFlag,_W:ciscoBfdSessEchoFuncModeDesiredFlag,_X:ciscoBfdSessControlPlanIndepFlag,_J:ciscoBfdSessAddrType,_K:ciscoBfdSessAddr,_Y:ciscoBfdSessDesiredMinTxInterval,_Z:ciscoBfdSessReqMinRxInterval,_a:ciscoBfdSessReqMinEchoRxInterval,_b:ciscoBfdSessDetectMult,_c:ciscoBfdSessStorType,_d:ciscoBfdSessRowStatus,_f:ciscoBfdSessAuthPresFlag,_g:ciscoBfdSessAuthenticationType,_y:ciscoBfdSessVersionNumber,_z:ciscoBfdSessType,_M:ciscoBfdSessInterface,'ciscoBfdSessPerfTable':ciscoBfdSessPerfTable,_n:ciscoBfdSessPerfEntry,_p:ciscoBfdSessPerfPktIn,_q:ciscoBfdSessPerfPktOut,_r:ciscoBfdSessUpTime,_s:ciscoBfdSessPerfLastSessDownTime,_t:ciscoBfdSessPerfLastCommLostDiag,_u:ciscoBfdSessPerfSessUpCount,_v:ciscoBfdSessPerfDiscTime,_w:ciscoBfdSessPerfPktInHC,_x:ciscoBfdSessPerfPktOutHC,'ciscoBfdSessMapTable':ciscoBfdSessMapTable,'ciscoBfdSessMapEntry':ciscoBfdSessMapEntry,_e:ciscoBfdSessMapBfdIndex,'ciscoBfdSessDiscMapTable':ciscoBfdSessDiscMapTable,'ciscoBfdSessDiscMapEntry':ciscoBfdSessDiscMapEntry,_A0:ciscoBfdSessDiscMapIndex,'ciscoBfdSessIpMapTable':ciscoBfdSessIpMapTable,'ciscoBfdSessIpMapEntry':ciscoBfdSessIpMapEntry,_A1:ciscoBfdSessIpMapIndex,'ciscoBfdConformance':ciscoBfdConformance,'ciscoBfdGroups':ciscoBfdGroups,_A4:ciscoBfdSessionGroup,_h:ciscoBfdSessionPerfGroup,_i:ciscoBfdSessionPerfHCGroup,_j:ciscoBfdNotificationGroup,_A5:ciscoBfdSession0304Group,_A6:ciscoBfdSession03Group,_A7:ciscoBfdSession04Group,'ciscoBfdCompliances':ciscoBfdCompliances,'ciscoBfdModuleFullCompliance':ciscoBfdModuleFullCompliance,'ciscoBfdModuleFullComplianceRev2':ciscoBfdModuleFullComplianceRev2})