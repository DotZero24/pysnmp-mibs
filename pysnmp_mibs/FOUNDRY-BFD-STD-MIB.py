_y='bfdSessionPerfGroup'
_x='bfdSessionGroup'
_w='bfdSessDown'
_v='bfdSessUp'
_u='bfdSessPerfPktOutHC'
_t='bfdSessPerfPktInHC'
_s='bfdSessPerfDiscTime'
_r='bfdSessPerfSessUpCount'
_q='bfdSessPerfLastCommLostDiag'
_p='bfdSessPerfLastSessDownTime'
_o='bfdSessPerfUpTime'
_n='bfdSessPerfPktOut'
_m='bfdSessPerfPktIn'
_l='bfdSessAuthenticationType'
_k='bfdSessAuthPresFlag'
_j='bfdSessMapBfdIndex'
_i='bfdSessRowStatus'
_h='bfdSessStorType'
_g='bfdSessDetectMult'
_f='bfdSessReqMinEchoRxInterval'
_e='bfdSessReqMinRxInterval'
_d='bfdSessDesiredMinTxInterval'
_c='bfdSessControlPlanIndepFlag'
_b='bfdSessEchoFuncModeDesiredFlag'
_a='bfdSessDemandModeDesiredFlag'
_Z='bfdSessOperMode'
_Y='bfdSessRemoteHeardFlag'
_X='bfdSessState'
_W='bfdSessUdpPort'
_V='bfdSessRemoteDiscr'
_U='bfdVersionNumber'
_T='bfdAdminStatus'
_S='bfdSessNotificationsEnable'
_R='bfdSessPerfEntry'
_Q='bfdSessIndex'
_P='read-write'
_O='InetPortNumber'
_N='bfdNotificationGroup'
_M='bfdSessionPerfHCGroup'
_L='bfdSessAddr'
_K='bfdSessAddrType'
_J='bfdSessDiscriminator'
_I='bfdSessApplicationId'
_H='Unsigned32'
_G='Integer32'
_F='bfdSessDiag'
_E='TruthValue'
_D='read-create'
_C='read-only'
_B='current'
_A='FOUNDRY-BFD-STD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bfd,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','bfd')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_E)
bfdMIB=ModuleIdentity((1,3,6,1,4,1,1991,3,3,1))
if mibBuilder.loadTexts:bfdMIB.setRevisions(('2005-08-22 12:00',))
class BfdSessIndexTC(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdInterval(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdDiag(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noDiagnostic',1),('controlDetectionTimeExpired',2),('echoFunctionFailed',3),('neighborSignaledSessionDown',4),('forwardingPlaneReset',5),('pathDown',6),('concatenatedPathDown',7),('administrativelyDown',8),('reverseConcatenatedPathDown',9)))
_BfdNotifications_ObjectIdentity=ObjectIdentity
bfdNotifications=_BfdNotifications_ObjectIdentity((1,3,6,1,4,1,1991,3,3,1,0))
_BfdObjects_ObjectIdentity=ObjectIdentity
bfdObjects=_BfdObjects_ObjectIdentity((1,3,6,1,4,1,1991,3,3,1,1))
_BfdScalarObjects_ObjectIdentity=ObjectIdentity
bfdScalarObjects=_BfdScalarObjects_ObjectIdentity((1,3,6,1,4,1,1991,3,3,1,1,1))
class _BfdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_BfdAdminStatus_Type.__name__=_G
_BfdAdminStatus_Object=MibScalar
bfdAdminStatus=_BfdAdminStatus_Object((1,3,6,1,4,1,1991,3,3,1,1,1,1),_BfdAdminStatus_Type())
bfdAdminStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:bfdAdminStatus.setStatus(_B)
class _BfdVersionNumber_Type(Unsigned32):defaultValue=0
_BfdVersionNumber_Type.__name__=_H
_BfdVersionNumber_Object=MibScalar
bfdVersionNumber=_BfdVersionNumber_Object((1,3,6,1,4,1,1991,3,3,1,1,1,3),_BfdVersionNumber_Type())
bfdVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdVersionNumber.setStatus(_B)
class _BfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_BfdSessNotificationsEnable_Type.__name__=_E
_BfdSessNotificationsEnable_Object=MibScalar
bfdSessNotificationsEnable=_BfdSessNotificationsEnable_Object((1,3,6,1,4,1,1991,3,3,1,1,1,4),_BfdSessNotificationsEnable_Type())
bfdSessNotificationsEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:bfdSessNotificationsEnable.setStatus(_B)
_BfdSessTable_Object=MibTable
bfdSessTable=_BfdSessTable_Object((1,3,6,1,4,1,1991,3,3,1,1,2))
if mibBuilder.loadTexts:bfdSessTable.setStatus(_B)
_BfdSessEntry_Object=MibTableRow
bfdSessEntry=_BfdSessEntry_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1))
bfdSessEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:bfdSessEntry.setStatus(_B)
_BfdSessIndex_Type=BfdSessIndexTC
_BfdSessIndex_Object=MibTableColumn
bfdSessIndex=_BfdSessIndex_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,1),_BfdSessIndex_Type())
bfdSessIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bfdSessIndex.setStatus(_B)
_BfdSessApplicationId_Type=Unsigned32
_BfdSessApplicationId_Object=MibTableColumn
bfdSessApplicationId=_BfdSessApplicationId_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,2),_BfdSessApplicationId_Type())
bfdSessApplicationId.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessApplicationId.setStatus(_B)
class _BfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_BfdSessDiscriminator_Type.__name__=_H
_BfdSessDiscriminator_Object=MibTableColumn
bfdSessDiscriminator=_BfdSessDiscriminator_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,3),_BfdSessDiscriminator_Type())
bfdSessDiscriminator.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDiscriminator.setStatus(_B)
class _BfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_BfdSessRemoteDiscr_Type.__name__=_H
_BfdSessRemoteDiscr_Object=MibTableColumn
bfdSessRemoteDiscr=_BfdSessRemoteDiscr_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,4),_BfdSessRemoteDiscr_Type())
bfdSessRemoteDiscr.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessRemoteDiscr.setStatus(_B)
class _BfdSessUdpPort_Type(InetPortNumber):defaultValue=0
_BfdSessUdpPort_Type.__name__=_O
_BfdSessUdpPort_Object=MibTableColumn
bfdSessUdpPort=_BfdSessUdpPort_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,5),_BfdSessUdpPort_Type())
bfdSessUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessUdpPort.setStatus(_B)
class _BfdSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4)))
_BfdSessState_Type.__name__=_G
_BfdSessState_Object=MibTableColumn
bfdSessState=_BfdSessState_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,6),_BfdSessState_Type())
bfdSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessState.setStatus(_B)
_BfdSessRemoteHeardFlag_Type=TruthValue
_BfdSessRemoteHeardFlag_Object=MibTableColumn
bfdSessRemoteHeardFlag=_BfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,7),_BfdSessRemoteHeardFlag_Type())
bfdSessRemoteHeardFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessRemoteHeardFlag.setStatus(_B)
_BfdSessDiag_Type=Unsigned32
_BfdSessDiag_Object=MibTableColumn
bfdSessDiag=_BfdSessDiag_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,8),_BfdSessDiag_Type())
bfdSessDiag.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:bfdSessDiag.setStatus(_B)
class _BfdSessOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asyncModeWEchoFun',1),('asynchModeWOEchoFun',2),('demandModeWEchoFunction',3),('demandModeWOEchoFunction',4)))
_BfdSessOperMode_Type.__name__=_G
_BfdSessOperMode_Object=MibTableColumn
bfdSessOperMode=_BfdSessOperMode_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,9),_BfdSessOperMode_Type())
bfdSessOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessOperMode.setStatus(_B)
class _BfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_BfdSessDemandModeDesiredFlag_Type.__name__=_E
_BfdSessDemandModeDesiredFlag_Object=MibTableColumn
bfdSessDemandModeDesiredFlag=_BfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,10),_BfdSessDemandModeDesiredFlag_Type())
bfdSessDemandModeDesiredFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessDemandModeDesiredFlag.setStatus(_B)
class _BfdSessEchoFuncModeDesiredFlag_Type(TruthValue):defaultValue=2
_BfdSessEchoFuncModeDesiredFlag_Type.__name__=_E
_BfdSessEchoFuncModeDesiredFlag_Object=MibTableColumn
bfdSessEchoFuncModeDesiredFlag=_BfdSessEchoFuncModeDesiredFlag_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,11),_BfdSessEchoFuncModeDesiredFlag_Type())
bfdSessEchoFuncModeDesiredFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessEchoFuncModeDesiredFlag.setStatus(_B)
class _BfdSessControlPlanIndepFlag_Type(TruthValue):defaultValue=2
_BfdSessControlPlanIndepFlag_Type.__name__=_E
_BfdSessControlPlanIndepFlag_Object=MibTableColumn
bfdSessControlPlanIndepFlag=_BfdSessControlPlanIndepFlag_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,12),_BfdSessControlPlanIndepFlag_Type())
bfdSessControlPlanIndepFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessControlPlanIndepFlag.setStatus(_B)
_BfdSessAddrType_Type=InetAddressType
_BfdSessAddrType_Object=MibTableColumn
bfdSessAddrType=_BfdSessAddrType_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,13),_BfdSessAddrType_Type())
bfdSessAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessAddrType.setStatus(_B)
_BfdSessAddr_Type=InetAddress
_BfdSessAddr_Object=MibTableColumn
bfdSessAddr=_BfdSessAddr_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,14),_BfdSessAddr_Type())
bfdSessAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessAddr.setStatus(_B)
_BfdSessDesiredMinTxInterval_Type=BfdInterval
_BfdSessDesiredMinTxInterval_Object=MibTableColumn
bfdSessDesiredMinTxInterval=_BfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,15),_BfdSessDesiredMinTxInterval_Type())
bfdSessDesiredMinTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessDesiredMinTxInterval.setStatus(_B)
_BfdSessReqMinRxInterval_Type=BfdInterval
_BfdSessReqMinRxInterval_Object=MibTableColumn
bfdSessReqMinRxInterval=_BfdSessReqMinRxInterval_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,16),_BfdSessReqMinRxInterval_Type())
bfdSessReqMinRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessReqMinRxInterval.setStatus(_B)
_BfdSessReqMinEchoRxInterval_Type=BfdInterval
_BfdSessReqMinEchoRxInterval_Object=MibTableColumn
bfdSessReqMinEchoRxInterval=_BfdSessReqMinEchoRxInterval_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,17),_BfdSessReqMinEchoRxInterval_Type())
bfdSessReqMinEchoRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessReqMinEchoRxInterval.setStatus(_B)
_BfdSessDetectMult_Type=Unsigned32
_BfdSessDetectMult_Object=MibTableColumn
bfdSessDetectMult=_BfdSessDetectMult_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,18),_BfdSessDetectMult_Type())
bfdSessDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessDetectMult.setStatus(_B)
_BfdSessStorType_Type=StorageType
_BfdSessStorType_Object=MibTableColumn
bfdSessStorType=_BfdSessStorType_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,19),_BfdSessStorType_Type())
bfdSessStorType.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessStorType.setStatus(_B)
_BfdSessRowStatus_Type=RowStatus
_BfdSessRowStatus_Object=MibTableColumn
bfdSessRowStatus=_BfdSessRowStatus_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,20),_BfdSessRowStatus_Type())
bfdSessRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessRowStatus.setStatus(_B)
class _BfdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_BfdSessAuthPresFlag_Type.__name__=_E
_BfdSessAuthPresFlag_Object=MibTableColumn
bfdSessAuthPresFlag=_BfdSessAuthPresFlag_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,21),_BfdSessAuthPresFlag_Type())
bfdSessAuthPresFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessAuthPresFlag.setStatus(_B)
class _BfdSessAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('simplePassword',1),('keyedMD5',2),('meticulousKeyedMD5',3),('keyedSHA1',4),('meticulousKeyedSHA1',5)))
_BfdSessAuthenticationType_Type.__name__=_G
_BfdSessAuthenticationType_Object=MibTableColumn
bfdSessAuthenticationType=_BfdSessAuthenticationType_Object((1,3,6,1,4,1,1991,3,3,1,1,2,1,22),_BfdSessAuthenticationType_Type())
bfdSessAuthenticationType.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessAuthenticationType.setStatus(_B)
_BfdSessPerfTable_Object=MibTable
bfdSessPerfTable=_BfdSessPerfTable_Object((1,3,6,1,4,1,1991,3,3,1,1,3))
if mibBuilder.loadTexts:bfdSessPerfTable.setStatus(_B)
_BfdSessPerfEntry_Object=MibTableRow
bfdSessPerfEntry=_BfdSessPerfEntry_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1))
if mibBuilder.loadTexts:bfdSessPerfEntry.setStatus(_B)
_BfdSessPerfPktIn_Type=Counter32
_BfdSessPerfPktIn_Object=MibTableColumn
bfdSessPerfPktIn=_BfdSessPerfPktIn_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,1),_BfdSessPerfPktIn_Type())
bfdSessPerfPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfPktIn.setStatus(_B)
_BfdSessPerfPktOut_Type=Counter32
_BfdSessPerfPktOut_Object=MibTableColumn
bfdSessPerfPktOut=_BfdSessPerfPktOut_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,2),_BfdSessPerfPktOut_Type())
bfdSessPerfPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfPktOut.setStatus(_B)
_BfdSessPerfUpTime_Type=TimeStamp
_BfdSessPerfUpTime_Object=MibTableColumn
bfdSessPerfUpTime=_BfdSessPerfUpTime_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,3),_BfdSessPerfUpTime_Type())
bfdSessPerfUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfUpTime.setStatus(_B)
_BfdSessPerfLastSessDownTime_Type=TimeStamp
_BfdSessPerfLastSessDownTime_Object=MibTableColumn
bfdSessPerfLastSessDownTime=_BfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,4),_BfdSessPerfLastSessDownTime_Type())
bfdSessPerfLastSessDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfLastSessDownTime.setStatus(_B)
_BfdSessPerfLastCommLostDiag_Type=BfdDiag
_BfdSessPerfLastCommLostDiag_Object=MibTableColumn
bfdSessPerfLastCommLostDiag=_BfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,5),_BfdSessPerfLastCommLostDiag_Type())
bfdSessPerfLastCommLostDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfLastCommLostDiag.setStatus(_B)
_BfdSessPerfSessUpCount_Type=Counter32
_BfdSessPerfSessUpCount_Object=MibTableColumn
bfdSessPerfSessUpCount=_BfdSessPerfSessUpCount_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,6),_BfdSessPerfSessUpCount_Type())
bfdSessPerfSessUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfSessUpCount.setStatus(_B)
_BfdSessPerfDiscTime_Type=TimeStamp
_BfdSessPerfDiscTime_Object=MibTableColumn
bfdSessPerfDiscTime=_BfdSessPerfDiscTime_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,7),_BfdSessPerfDiscTime_Type())
bfdSessPerfDiscTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfDiscTime.setStatus(_B)
_BfdSessPerfPktInHC_Type=Counter64
_BfdSessPerfPktInHC_Object=MibTableColumn
bfdSessPerfPktInHC=_BfdSessPerfPktInHC_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,8),_BfdSessPerfPktInHC_Type())
bfdSessPerfPktInHC.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfPktInHC.setStatus(_B)
_BfdSessPerfPktOutHC_Type=Counter64
_BfdSessPerfPktOutHC_Object=MibTableColumn
bfdSessPerfPktOutHC=_BfdSessPerfPktOutHC_Object((1,3,6,1,4,1,1991,3,3,1,1,3,1,9),_BfdSessPerfPktOutHC_Type())
bfdSessPerfPktOutHC.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessPerfPktOutHC.setStatus(_B)
_BfdSessMapTable_Object=MibTable
bfdSessMapTable=_BfdSessMapTable_Object((1,3,6,1,4,1,1991,3,3,1,1,4))
if mibBuilder.loadTexts:bfdSessMapTable.setStatus(_B)
_BfdSessMapEntry_Object=MibTableRow
bfdSessMapEntry=_BfdSessMapEntry_Object((1,3,6,1,4,1,1991,3,3,1,1,4,1))
bfdSessMapEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:bfdSessMapEntry.setStatus(_B)
_BfdSessMapBfdIndex_Type=BfdSessIndexTC
_BfdSessMapBfdIndex_Object=MibTableColumn
bfdSessMapBfdIndex=_BfdSessMapBfdIndex_Object((1,3,6,1,4,1,1991,3,3,1,1,4,1,1),_BfdSessMapBfdIndex_Type())
bfdSessMapBfdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessMapBfdIndex.setStatus(_B)
_BfdConformance_ObjectIdentity=ObjectIdentity
bfdConformance=_BfdConformance_ObjectIdentity((1,3,6,1,4,1,1991,3,3,1,3))
_BfdGroups_ObjectIdentity=ObjectIdentity
bfdGroups=_BfdGroups_ObjectIdentity((1,3,6,1,4,1,1991,3,3,1,3,1))
_BfdCompliances_ObjectIdentity=ObjectIdentity
bfdCompliances=_BfdCompliances_ObjectIdentity((1,3,6,1,4,1,1991,3,3,1,3,2))
bfdSessEntry.registerAugmentions((_A,_R))
bfdSessPerfEntry.setIndexNames(*bfdSessEntry.getIndexNames())
bfdSessionGroup=ObjectGroup((1,3,6,1,4,1,1991,3,3,1,3,1,1))
bfdSessionGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_F),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:bfdSessionGroup.setStatus(_B)
bfdSessionPerfGroup=ObjectGroup((1,3,6,1,4,1,1991,3,3,1,3,1,2))
bfdSessionPerfGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:bfdSessionPerfGroup.setStatus(_B)
bfdSessionPerfHCGroup=ObjectGroup((1,3,6,1,4,1,1991,3,3,1,3,1,3))
bfdSessionPerfHCGroup.setObjects(*((_A,_t),(_A,_u)))
if mibBuilder.loadTexts:bfdSessionPerfHCGroup.setStatus(_B)
bfdSessUp=NotificationType((1,3,6,1,4,1,1991,3,3,1,0,1))
bfdSessUp.setObjects(*((_A,_F),(_A,_F)))
if mibBuilder.loadTexts:bfdSessUp.setStatus(_B)
bfdSessDown=NotificationType((1,3,6,1,4,1,1991,3,3,1,0,2))
bfdSessDown.setObjects(*((_A,_F),(_A,_F)))
if mibBuilder.loadTexts:bfdSessDown.setStatus(_B)
bfdNotificationGroup=NotificationGroup((1,3,6,1,4,1,1991,3,3,1,3,1,4))
bfdNotificationGroup.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:bfdNotificationGroup.setStatus(_B)
bfdModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,1991,3,3,1,3,2,1))
bfdModuleFullCompliance.setObjects(*((_A,_x),(_A,_y),(_A,_M),(_A,_N),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:bfdModuleFullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'BfdSessIndexTC':BfdSessIndexTC,'BfdInterval':BfdInterval,'BfdDiag':BfdDiag,'bfdMIB':bfdMIB,'bfdNotifications':bfdNotifications,_v:bfdSessUp,_w:bfdSessDown,'bfdObjects':bfdObjects,'bfdScalarObjects':bfdScalarObjects,_T:bfdAdminStatus,_U:bfdVersionNumber,_S:bfdSessNotificationsEnable,'bfdSessTable':bfdSessTable,'bfdSessEntry':bfdSessEntry,_Q:bfdSessIndex,_I:bfdSessApplicationId,_J:bfdSessDiscriminator,_V:bfdSessRemoteDiscr,_W:bfdSessUdpPort,_X:bfdSessState,_Y:bfdSessRemoteHeardFlag,_F:bfdSessDiag,_Z:bfdSessOperMode,_a:bfdSessDemandModeDesiredFlag,_b:bfdSessEchoFuncModeDesiredFlag,_c:bfdSessControlPlanIndepFlag,_K:bfdSessAddrType,_L:bfdSessAddr,_d:bfdSessDesiredMinTxInterval,_e:bfdSessReqMinRxInterval,_f:bfdSessReqMinEchoRxInterval,_g:bfdSessDetectMult,_h:bfdSessStorType,_i:bfdSessRowStatus,_k:bfdSessAuthPresFlag,_l:bfdSessAuthenticationType,'bfdSessPerfTable':bfdSessPerfTable,_R:bfdSessPerfEntry,_m:bfdSessPerfPktIn,_n:bfdSessPerfPktOut,_o:bfdSessPerfUpTime,_p:bfdSessPerfLastSessDownTime,_q:bfdSessPerfLastCommLostDiag,_r:bfdSessPerfSessUpCount,_s:bfdSessPerfDiscTime,_t:bfdSessPerfPktInHC,_u:bfdSessPerfPktOutHC,'bfdSessMapTable':bfdSessMapTable,'bfdSessMapEntry':bfdSessMapEntry,_j:bfdSessMapBfdIndex,'bfdConformance':bfdConformance,'bfdGroups':bfdGroups,_x:bfdSessionGroup,_y:bfdSessionPerfGroup,_M:bfdSessionPerfHCGroup,_N:bfdNotificationGroup,'bfdCompliances':bfdCompliances,'bfdModuleFullCompliance':bfdModuleFullCompliance})