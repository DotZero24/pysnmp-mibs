_AV='bfdSessDown'
_AU='bfdSessUp'
_AT='bfdSessPerfEchoPktDropHC'
_AS='bfdSessPerfEchoPktOutHC'
_AR='bfdSessPerfEchoPktInHC'
_AQ='bfdSessPerfCtrlPktDropHC'
_AP='bfdSessPerfCtrlPktOutHC'
_AO='bfdSessPerfCtrlPktInHC'
_AN='bfdSessPerfDiscTime'
_AM='bfdSessPerfSessUpCount'
_AL='bfdSessPerfLastCommLostDiag'
_AK='bfdSessPerfLastSessDownTime'
_AJ='bfdSessUpTime'
_AI='bfdSessPerfEchoPktDropLastTime'
_AH='bfdSessPerfEchoPktDrop'
_AG='bfdSessPerfEchoPktOut'
_AF='bfdSessPerfEchoPktIn'
_AE='bfdSessPerfCtrlPktDropLastTime'
_AD='bfdSessPerfCtrlPktDrop'
_AC='bfdSessPerfCtrlPktOut'
_AB='bfdSessPerfCtrlPktIn'
_AA='bfdSessIpMapIndex'
_A9='bfdSessDiscMapIndex'
_A8='bfdSessNegotiatedDetectMult'
_A7='bfdSessNegotiatedEchoInterval'
_A6='bfdSessNegotiatedInterval'
_A5='bfdSessRemoteHeardFlag'
_A4='bfdSessState'
_A3='bfdSessRemoteDiscr'
_A2='bfdSessIpMapRowStatus'
_A1='bfdSessIpMapStorageType'
_A0='bfdSessDiscMapRowStatus'
_z='bfdSessDiscMapStorageType'
_y='bfdSessRowStatus'
_x='bfdSessStorageType'
_w='bfdSessAuthenticationKey'
_v='bfdSessAuthenticationKeyID'
_u='bfdSessAuthenticationType'
_t='bfdSessAuthPresFlag'
_s='bfdSessDetectMult'
_r='bfdSessReqMinEchoRxInterval'
_q='bfdSessReqMinRxInterval'
_p='bfdSessDesiredMinTxInterval'
_o='bfdSessGTSMTTL'
_n='bfdSessGTSM'
_m='bfdSessMultipointFlag'
_l='bfdSessControlPlaneIndepFlag'
_k='bfdSessDemandModeDesiredFlag'
_j='bfdSessOperMode'
_i='bfdSessAdminStatus'
_h='bfdSessEchoSourceUdpPort'
_g='bfdSessSourceUdpPort'
_f='bfdSessDestinationUdpPort'
_e='bfdSessType'
_d='bfdSessVersionNumber'
_c='bfdSessNotificationsEnable'
_b='bfdAdminStatus'
_a='bfdSessPerfEntry'
_Z='bfdSessIndex'
_Y='read-write'
_X='InetPortNumber'
_W='BfdSessStateTC'
_V='BfdSessAuthenticationTypeTC'
_U='BfdCtrlSourcePortNumberTC'
_T='BfdCtrlDestPortNumberTC'
_S='bfdSessionPerfHCGroup'
_R='bfdNotificationGroup'
_Q='bfdSessionPerfGroup'
_P='bfdSessionReadOnlyGroup'
_O='bfdSessionGroup'
_N='bfdSessDstAddr'
_M='bfdSessDstAddrType'
_L='bfdSessSrcAddr'
_K='bfdSessSrcAddrType'
_J='bfdSessInterface'
_I='bfdSessDiscriminator'
_H='Integer32'
_G='Unsigned32'
_F='bfdSessDiag'
_E='TruthValue'
_D='read-only'
_C='read-create'
_B='current'
_A='BFD-STD-MIB-R'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BfdCtrlDestPortNumberTC,BfdCtrlSourcePortNumberTC,BfdDiagTC,BfdIntervalTC,BfdMultiplierTC,BfdSessAuthenticationTypeTC,BfdSessIndexTC,BfdSessOperModeTC,BfdSessStateTC,BfdSessTypeTC,BfdSessionAuthenticationKeyTC=mibBuilder.importSymbols('BFD-TC-STD-MIB-R',_T,_U,'BfdDiagTC','BfdIntervalTC','BfdMultiplierTC',_V,'BfdSessIndexTC','BfdSessOperModeTC',_W,'BfdSessTypeTC','BfdSessionAuthenticationKeyTC')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_X)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_E)
bfdMIB=ModuleIdentity((1,3,6,1,4,1,164,20,15))
if mibBuilder.loadTexts:bfdMIB.setRevisions(('2012-04-14 12:00',))
_RadExperimental_ObjectIdentity=ObjectIdentity
radExperimental=_RadExperimental_ObjectIdentity((1,3,6,1,4,1,164,20))
_BfdNotifications_ObjectIdentity=ObjectIdentity
bfdNotifications=_BfdNotifications_ObjectIdentity((1,3,6,1,4,1,164,20,15,0))
_BfdObjects_ObjectIdentity=ObjectIdentity
bfdObjects=_BfdObjects_ObjectIdentity((1,3,6,1,4,1,164,20,15,1))
_BfdScalarObjects_ObjectIdentity=ObjectIdentity
bfdScalarObjects=_BfdScalarObjects_ObjectIdentity((1,3,6,1,4,1,164,20,15,1,1))
class _BfdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_BfdAdminStatus_Type.__name__=_H
_BfdAdminStatus_Object=MibScalar
bfdAdminStatus=_BfdAdminStatus_Object((1,3,6,1,4,1,164,20,15,1,1,1),_BfdAdminStatus_Type())
bfdAdminStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:bfdAdminStatus.setStatus(_B)
class _BfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_BfdSessNotificationsEnable_Type.__name__=_E
_BfdSessNotificationsEnable_Object=MibScalar
bfdSessNotificationsEnable=_BfdSessNotificationsEnable_Object((1,3,6,1,4,1,164,20,15,1,1,2),_BfdSessNotificationsEnable_Type())
bfdSessNotificationsEnable.setMaxAccess(_Y)
if mibBuilder.loadTexts:bfdSessNotificationsEnable.setStatus(_B)
_BfdSessTable_Object=MibTable
bfdSessTable=_BfdSessTable_Object((1,3,6,1,4,1,164,20,15,1,2))
if mibBuilder.loadTexts:bfdSessTable.setStatus(_B)
_BfdSessEntry_Object=MibTableRow
bfdSessEntry=_BfdSessEntry_Object((1,3,6,1,4,1,164,20,15,1,2,1))
bfdSessEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:bfdSessEntry.setStatus(_B)
_BfdSessIndex_Type=BfdSessIndexTC
_BfdSessIndex_Object=MibTableColumn
bfdSessIndex=_BfdSessIndex_Object((1,3,6,1,4,1,164,20,15,1,2,1,1),_BfdSessIndex_Type())
bfdSessIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bfdSessIndex.setStatus(_B)
class _BfdSessVersionNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BfdSessVersionNumber_Type.__name__=_G
_BfdSessVersionNumber_Object=MibTableColumn
bfdSessVersionNumber=_BfdSessVersionNumber_Object((1,3,6,1,4,1,164,20,15,1,2,1,2),_BfdSessVersionNumber_Type())
bfdSessVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessVersionNumber.setStatus(_B)
_BfdSessType_Type=BfdSessTypeTC
_BfdSessType_Object=MibTableColumn
bfdSessType=_BfdSessType_Object((1,3,6,1,4,1,164,20,15,1,2,1,3),_BfdSessType_Type())
bfdSessType.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessType.setStatus(_B)
class _BfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_BfdSessDiscriminator_Type.__name__=_G
_BfdSessDiscriminator_Object=MibTableColumn
bfdSessDiscriminator=_BfdSessDiscriminator_Object((1,3,6,1,4,1,164,20,15,1,2,1,4),_BfdSessDiscriminator_Type())
bfdSessDiscriminator.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessDiscriminator.setStatus(_B)
class _BfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_BfdSessRemoteDiscr_Type.__name__=_G
_BfdSessRemoteDiscr_Object=MibTableColumn
bfdSessRemoteDiscr=_BfdSessRemoteDiscr_Object((1,3,6,1,4,1,164,20,15,1,2,1,5),_BfdSessRemoteDiscr_Type())
bfdSessRemoteDiscr.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessRemoteDiscr.setStatus(_B)
class _BfdSessDestinationUdpPort_Type(BfdCtrlDestPortNumberTC):defaultValue=0
_BfdSessDestinationUdpPort_Type.__name__=_T
_BfdSessDestinationUdpPort_Object=MibTableColumn
bfdSessDestinationUdpPort=_BfdSessDestinationUdpPort_Object((1,3,6,1,4,1,164,20,15,1,2,1,6),_BfdSessDestinationUdpPort_Type())
bfdSessDestinationUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDestinationUdpPort.setStatus(_B)
class _BfdSessSourceUdpPort_Type(BfdCtrlSourcePortNumberTC):defaultValue=0
_BfdSessSourceUdpPort_Type.__name__=_U
_BfdSessSourceUdpPort_Object=MibTableColumn
bfdSessSourceUdpPort=_BfdSessSourceUdpPort_Object((1,3,6,1,4,1,164,20,15,1,2,1,7),_BfdSessSourceUdpPort_Type())
bfdSessSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessSourceUdpPort.setStatus(_B)
class _BfdSessEchoSourceUdpPort_Type(InetPortNumber):defaultValue=0
_BfdSessEchoSourceUdpPort_Type.__name__=_X
_BfdSessEchoSourceUdpPort_Object=MibTableColumn
bfdSessEchoSourceUdpPort=_BfdSessEchoSourceUdpPort_Object((1,3,6,1,4,1,164,20,15,1,2,1,8),_BfdSessEchoSourceUdpPort_Type())
bfdSessEchoSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessEchoSourceUdpPort.setStatus(_B)
class _BfdSessAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_BfdSessAdminStatus_Type.__name__=_H
_BfdSessAdminStatus_Object=MibTableColumn
bfdSessAdminStatus=_BfdSessAdminStatus_Object((1,3,6,1,4,1,164,20,15,1,2,1,9),_BfdSessAdminStatus_Type())
bfdSessAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessAdminStatus.setStatus(_B)
class _BfdSessState_Type(BfdSessStateTC):defaultValue=2
_BfdSessState_Type.__name__=_W
_BfdSessState_Object=MibTableColumn
bfdSessState=_BfdSessState_Object((1,3,6,1,4,1,164,20,15,1,2,1,10),_BfdSessState_Type())
bfdSessState.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessState.setStatus(_B)
class _BfdSessRemoteHeardFlag_Type(TruthValue):defaultValue=2
_BfdSessRemoteHeardFlag_Type.__name__=_E
_BfdSessRemoteHeardFlag_Object=MibTableColumn
bfdSessRemoteHeardFlag=_BfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,164,20,15,1,2,1,11),_BfdSessRemoteHeardFlag_Type())
bfdSessRemoteHeardFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessRemoteHeardFlag.setStatus(_B)
_BfdSessDiag_Type=BfdDiagTC
_BfdSessDiag_Object=MibTableColumn
bfdSessDiag=_BfdSessDiag_Object((1,3,6,1,4,1,164,20,15,1,2,1,12),_BfdSessDiag_Type())
bfdSessDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessDiag.setStatus(_B)
_BfdSessOperMode_Type=BfdSessOperModeTC
_BfdSessOperMode_Object=MibTableColumn
bfdSessOperMode=_BfdSessOperMode_Object((1,3,6,1,4,1,164,20,15,1,2,1,13),_BfdSessOperMode_Type())
bfdSessOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessOperMode.setStatus(_B)
class _BfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_BfdSessDemandModeDesiredFlag_Type.__name__=_E
_BfdSessDemandModeDesiredFlag_Object=MibTableColumn
bfdSessDemandModeDesiredFlag=_BfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,164,20,15,1,2,1,14),_BfdSessDemandModeDesiredFlag_Type())
bfdSessDemandModeDesiredFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDemandModeDesiredFlag.setStatus(_B)
class _BfdSessControlPlaneIndepFlag_Type(TruthValue):defaultValue=2
_BfdSessControlPlaneIndepFlag_Type.__name__=_E
_BfdSessControlPlaneIndepFlag_Object=MibTableColumn
bfdSessControlPlaneIndepFlag=_BfdSessControlPlaneIndepFlag_Object((1,3,6,1,4,1,164,20,15,1,2,1,15),_BfdSessControlPlaneIndepFlag_Type())
bfdSessControlPlaneIndepFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessControlPlaneIndepFlag.setStatus(_B)
class _BfdSessMultipointFlag_Type(TruthValue):defaultValue=2
_BfdSessMultipointFlag_Type.__name__=_E
_BfdSessMultipointFlag_Object=MibTableColumn
bfdSessMultipointFlag=_BfdSessMultipointFlag_Object((1,3,6,1,4,1,164,20,15,1,2,1,16),_BfdSessMultipointFlag_Type())
bfdSessMultipointFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessMultipointFlag.setStatus(_B)
_BfdSessInterface_Type=InterfaceIndexOrZero
_BfdSessInterface_Object=MibTableColumn
bfdSessInterface=_BfdSessInterface_Object((1,3,6,1,4,1,164,20,15,1,2,1,17),_BfdSessInterface_Type())
bfdSessInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessInterface.setStatus(_B)
_BfdSessSrcAddrType_Type=InetAddressType
_BfdSessSrcAddrType_Object=MibTableColumn
bfdSessSrcAddrType=_BfdSessSrcAddrType_Object((1,3,6,1,4,1,164,20,15,1,2,1,18),_BfdSessSrcAddrType_Type())
bfdSessSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessSrcAddrType.setStatus(_B)
_BfdSessSrcAddr_Type=InetAddress
_BfdSessSrcAddr_Object=MibTableColumn
bfdSessSrcAddr=_BfdSessSrcAddr_Object((1,3,6,1,4,1,164,20,15,1,2,1,19),_BfdSessSrcAddr_Type())
bfdSessSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessSrcAddr.setStatus(_B)
_BfdSessDstAddrType_Type=InetAddressType
_BfdSessDstAddrType_Object=MibTableColumn
bfdSessDstAddrType=_BfdSessDstAddrType_Object((1,3,6,1,4,1,164,20,15,1,2,1,20),_BfdSessDstAddrType_Type())
bfdSessDstAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDstAddrType.setStatus(_B)
_BfdSessDstAddr_Type=InetAddress
_BfdSessDstAddr_Object=MibTableColumn
bfdSessDstAddr=_BfdSessDstAddr_Object((1,3,6,1,4,1,164,20,15,1,2,1,21),_BfdSessDstAddr_Type())
bfdSessDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDstAddr.setStatus(_B)
class _BfdSessGTSM_Type(TruthValue):defaultValue=2
_BfdSessGTSM_Type.__name__=_E
_BfdSessGTSM_Object=MibTableColumn
bfdSessGTSM=_BfdSessGTSM_Object((1,3,6,1,4,1,164,20,15,1,2,1,22),_BfdSessGTSM_Type())
bfdSessGTSM.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessGTSM.setStatus(_B)
class _BfdSessGTSMTTL_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BfdSessGTSMTTL_Type.__name__=_G
_BfdSessGTSMTTL_Object=MibTableColumn
bfdSessGTSMTTL=_BfdSessGTSMTTL_Object((1,3,6,1,4,1,164,20,15,1,2,1,23),_BfdSessGTSMTTL_Type())
bfdSessGTSMTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessGTSMTTL.setStatus(_B)
_BfdSessDesiredMinTxInterval_Type=BfdIntervalTC
_BfdSessDesiredMinTxInterval_Object=MibTableColumn
bfdSessDesiredMinTxInterval=_BfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,164,20,15,1,2,1,24),_BfdSessDesiredMinTxInterval_Type())
bfdSessDesiredMinTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDesiredMinTxInterval.setStatus(_B)
_BfdSessReqMinRxInterval_Type=BfdIntervalTC
_BfdSessReqMinRxInterval_Object=MibTableColumn
bfdSessReqMinRxInterval=_BfdSessReqMinRxInterval_Object((1,3,6,1,4,1,164,20,15,1,2,1,25),_BfdSessReqMinRxInterval_Type())
bfdSessReqMinRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessReqMinRxInterval.setStatus(_B)
_BfdSessReqMinEchoRxInterval_Type=BfdIntervalTC
_BfdSessReqMinEchoRxInterval_Object=MibTableColumn
bfdSessReqMinEchoRxInterval=_BfdSessReqMinEchoRxInterval_Object((1,3,6,1,4,1,164,20,15,1,2,1,26),_BfdSessReqMinEchoRxInterval_Type())
bfdSessReqMinEchoRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessReqMinEchoRxInterval.setStatus(_B)
_BfdSessDetectMult_Type=BfdMultiplierTC
_BfdSessDetectMult_Object=MibTableColumn
bfdSessDetectMult=_BfdSessDetectMult_Object((1,3,6,1,4,1,164,20,15,1,2,1,27),_BfdSessDetectMult_Type())
bfdSessDetectMult.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDetectMult.setStatus(_B)
_BfdSessNegotiatedInterval_Type=BfdIntervalTC
_BfdSessNegotiatedInterval_Object=MibTableColumn
bfdSessNegotiatedInterval=_BfdSessNegotiatedInterval_Object((1,3,6,1,4,1,164,20,15,1,2,1,28),_BfdSessNegotiatedInterval_Type())
bfdSessNegotiatedInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessNegotiatedInterval.setStatus(_B)
_BfdSessNegotiatedEchoInterval_Type=BfdIntervalTC
_BfdSessNegotiatedEchoInterval_Object=MibTableColumn
bfdSessNegotiatedEchoInterval=_BfdSessNegotiatedEchoInterval_Object((1,3,6,1,4,1,164,20,15,1,2,1,29),_BfdSessNegotiatedEchoInterval_Type())
bfdSessNegotiatedEchoInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessNegotiatedEchoInterval.setStatus(_B)
_BfdSessNegotiatedDetectMult_Type=BfdMultiplierTC
_BfdSessNegotiatedDetectMult_Object=MibTableColumn
bfdSessNegotiatedDetectMult=_BfdSessNegotiatedDetectMult_Object((1,3,6,1,4,1,164,20,15,1,2,1,30),_BfdSessNegotiatedDetectMult_Type())
bfdSessNegotiatedDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessNegotiatedDetectMult.setStatus(_B)
class _BfdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_BfdSessAuthPresFlag_Type.__name__=_E
_BfdSessAuthPresFlag_Object=MibTableColumn
bfdSessAuthPresFlag=_BfdSessAuthPresFlag_Object((1,3,6,1,4,1,164,20,15,1,2,1,31),_BfdSessAuthPresFlag_Type())
bfdSessAuthPresFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessAuthPresFlag.setStatus(_B)
class _BfdSessAuthenticationType_Type(BfdSessAuthenticationTypeTC):defaultValue=-1
_BfdSessAuthenticationType_Type.__name__=_V
_BfdSessAuthenticationType_Object=MibTableColumn
bfdSessAuthenticationType=_BfdSessAuthenticationType_Object((1,3,6,1,4,1,164,20,15,1,2,1,32),_BfdSessAuthenticationType_Type())
bfdSessAuthenticationType.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessAuthenticationType.setStatus(_B)
class _BfdSessAuthenticationKeyID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_BfdSessAuthenticationKeyID_Type.__name__=_H
_BfdSessAuthenticationKeyID_Object=MibTableColumn
bfdSessAuthenticationKeyID=_BfdSessAuthenticationKeyID_Object((1,3,6,1,4,1,164,20,15,1,2,1,33),_BfdSessAuthenticationKeyID_Type())
bfdSessAuthenticationKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessAuthenticationKeyID.setStatus(_B)
_BfdSessAuthenticationKey_Type=BfdSessionAuthenticationKeyTC
_BfdSessAuthenticationKey_Object=MibTableColumn
bfdSessAuthenticationKey=_BfdSessAuthenticationKey_Object((1,3,6,1,4,1,164,20,15,1,2,1,34),_BfdSessAuthenticationKey_Type())
bfdSessAuthenticationKey.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessAuthenticationKey.setStatus(_B)
_BfdSessStorageType_Type=StorageType
_BfdSessStorageType_Object=MibTableColumn
bfdSessStorageType=_BfdSessStorageType_Object((1,3,6,1,4,1,164,20,15,1,2,1,35),_BfdSessStorageType_Type())
bfdSessStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessStorageType.setStatus(_B)
_BfdSessRowStatus_Type=RowStatus
_BfdSessRowStatus_Object=MibTableColumn
bfdSessRowStatus=_BfdSessRowStatus_Object((1,3,6,1,4,1,164,20,15,1,2,1,36),_BfdSessRowStatus_Type())
bfdSessRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessRowStatus.setStatus(_B)
_BfdSessPerfTable_Object=MibTable
bfdSessPerfTable=_BfdSessPerfTable_Object((1,3,6,1,4,1,164,20,15,1,3))
if mibBuilder.loadTexts:bfdSessPerfTable.setStatus(_B)
_BfdSessPerfEntry_Object=MibTableRow
bfdSessPerfEntry=_BfdSessPerfEntry_Object((1,3,6,1,4,1,164,20,15,1,3,1))
if mibBuilder.loadTexts:bfdSessPerfEntry.setStatus(_B)
_BfdSessPerfCtrlPktIn_Type=Counter32
_BfdSessPerfCtrlPktIn_Object=MibTableColumn
bfdSessPerfCtrlPktIn=_BfdSessPerfCtrlPktIn_Object((1,3,6,1,4,1,164,20,15,1,3,1,1),_BfdSessPerfCtrlPktIn_Type())
bfdSessPerfCtrlPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfCtrlPktIn.setStatus(_B)
_BfdSessPerfCtrlPktOut_Type=Counter32
_BfdSessPerfCtrlPktOut_Object=MibTableColumn
bfdSessPerfCtrlPktOut=_BfdSessPerfCtrlPktOut_Object((1,3,6,1,4,1,164,20,15,1,3,1,2),_BfdSessPerfCtrlPktOut_Type())
bfdSessPerfCtrlPktOut.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfCtrlPktOut.setStatus(_B)
_BfdSessPerfCtrlPktDrop_Type=Counter32
_BfdSessPerfCtrlPktDrop_Object=MibTableColumn
bfdSessPerfCtrlPktDrop=_BfdSessPerfCtrlPktDrop_Object((1,3,6,1,4,1,164,20,15,1,3,1,3),_BfdSessPerfCtrlPktDrop_Type())
bfdSessPerfCtrlPktDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfCtrlPktDrop.setStatus(_B)
_BfdSessPerfCtrlPktDropLastTime_Type=TimeStamp
_BfdSessPerfCtrlPktDropLastTime_Object=MibTableColumn
bfdSessPerfCtrlPktDropLastTime=_BfdSessPerfCtrlPktDropLastTime_Object((1,3,6,1,4,1,164,20,15,1,3,1,4),_BfdSessPerfCtrlPktDropLastTime_Type())
bfdSessPerfCtrlPktDropLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfCtrlPktDropLastTime.setStatus(_B)
_BfdSessPerfEchoPktIn_Type=Counter32
_BfdSessPerfEchoPktIn_Object=MibTableColumn
bfdSessPerfEchoPktIn=_BfdSessPerfEchoPktIn_Object((1,3,6,1,4,1,164,20,15,1,3,1,5),_BfdSessPerfEchoPktIn_Type())
bfdSessPerfEchoPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfEchoPktIn.setStatus(_B)
_BfdSessPerfEchoPktOut_Type=Counter32
_BfdSessPerfEchoPktOut_Object=MibTableColumn
bfdSessPerfEchoPktOut=_BfdSessPerfEchoPktOut_Object((1,3,6,1,4,1,164,20,15,1,3,1,6),_BfdSessPerfEchoPktOut_Type())
bfdSessPerfEchoPktOut.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfEchoPktOut.setStatus(_B)
_BfdSessPerfEchoPktDrop_Type=Counter32
_BfdSessPerfEchoPktDrop_Object=MibTableColumn
bfdSessPerfEchoPktDrop=_BfdSessPerfEchoPktDrop_Object((1,3,6,1,4,1,164,20,15,1,3,1,7),_BfdSessPerfEchoPktDrop_Type())
bfdSessPerfEchoPktDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfEchoPktDrop.setStatus(_B)
_BfdSessPerfEchoPktDropLastTime_Type=TimeStamp
_BfdSessPerfEchoPktDropLastTime_Object=MibTableColumn
bfdSessPerfEchoPktDropLastTime=_BfdSessPerfEchoPktDropLastTime_Object((1,3,6,1,4,1,164,20,15,1,3,1,8),_BfdSessPerfEchoPktDropLastTime_Type())
bfdSessPerfEchoPktDropLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfEchoPktDropLastTime.setStatus(_B)
_BfdSessUpTime_Type=TimeStamp
_BfdSessUpTime_Object=MibTableColumn
bfdSessUpTime=_BfdSessUpTime_Object((1,3,6,1,4,1,164,20,15,1,3,1,9),_BfdSessUpTime_Type())
bfdSessUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessUpTime.setStatus(_B)
_BfdSessPerfLastSessDownTime_Type=TimeStamp
_BfdSessPerfLastSessDownTime_Object=MibTableColumn
bfdSessPerfLastSessDownTime=_BfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,164,20,15,1,3,1,10),_BfdSessPerfLastSessDownTime_Type())
bfdSessPerfLastSessDownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfLastSessDownTime.setStatus(_B)
_BfdSessPerfLastCommLostDiag_Type=BfdDiagTC
_BfdSessPerfLastCommLostDiag_Object=MibTableColumn
bfdSessPerfLastCommLostDiag=_BfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,164,20,15,1,3,1,11),_BfdSessPerfLastCommLostDiag_Type())
bfdSessPerfLastCommLostDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfLastCommLostDiag.setStatus(_B)
_BfdSessPerfSessUpCount_Type=Counter32
_BfdSessPerfSessUpCount_Object=MibTableColumn
bfdSessPerfSessUpCount=_BfdSessPerfSessUpCount_Object((1,3,6,1,4,1,164,20,15,1,3,1,12),_BfdSessPerfSessUpCount_Type())
bfdSessPerfSessUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfSessUpCount.setStatus(_B)
_BfdSessPerfDiscTime_Type=TimeStamp
_BfdSessPerfDiscTime_Object=MibTableColumn
bfdSessPerfDiscTime=_BfdSessPerfDiscTime_Object((1,3,6,1,4,1,164,20,15,1,3,1,13),_BfdSessPerfDiscTime_Type())
bfdSessPerfDiscTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfDiscTime.setStatus(_B)
_BfdSessPerfCtrlPktInHC_Type=Counter64
_BfdSessPerfCtrlPktInHC_Object=MibTableColumn
bfdSessPerfCtrlPktInHC=_BfdSessPerfCtrlPktInHC_Object((1,3,6,1,4,1,164,20,15,1,3,1,14),_BfdSessPerfCtrlPktInHC_Type())
bfdSessPerfCtrlPktInHC.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfCtrlPktInHC.setStatus(_B)
_BfdSessPerfCtrlPktOutHC_Type=Counter64
_BfdSessPerfCtrlPktOutHC_Object=MibTableColumn
bfdSessPerfCtrlPktOutHC=_BfdSessPerfCtrlPktOutHC_Object((1,3,6,1,4,1,164,20,15,1,3,1,15),_BfdSessPerfCtrlPktOutHC_Type())
bfdSessPerfCtrlPktOutHC.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfCtrlPktOutHC.setStatus(_B)
_BfdSessPerfCtrlPktDropHC_Type=Counter64
_BfdSessPerfCtrlPktDropHC_Object=MibTableColumn
bfdSessPerfCtrlPktDropHC=_BfdSessPerfCtrlPktDropHC_Object((1,3,6,1,4,1,164,20,15,1,3,1,16),_BfdSessPerfCtrlPktDropHC_Type())
bfdSessPerfCtrlPktDropHC.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfCtrlPktDropHC.setStatus(_B)
_BfdSessPerfEchoPktInHC_Type=Counter64
_BfdSessPerfEchoPktInHC_Object=MibTableColumn
bfdSessPerfEchoPktInHC=_BfdSessPerfEchoPktInHC_Object((1,3,6,1,4,1,164,20,15,1,3,1,17),_BfdSessPerfEchoPktInHC_Type())
bfdSessPerfEchoPktInHC.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfEchoPktInHC.setStatus(_B)
_BfdSessPerfEchoPktOutHC_Type=Counter64
_BfdSessPerfEchoPktOutHC_Object=MibTableColumn
bfdSessPerfEchoPktOutHC=_BfdSessPerfEchoPktOutHC_Object((1,3,6,1,4,1,164,20,15,1,3,1,18),_BfdSessPerfEchoPktOutHC_Type())
bfdSessPerfEchoPktOutHC.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfEchoPktOutHC.setStatus(_B)
_BfdSessPerfEchoPktDropHC_Type=Counter64
_BfdSessPerfEchoPktDropHC_Object=MibTableColumn
bfdSessPerfEchoPktDropHC=_BfdSessPerfEchoPktDropHC_Object((1,3,6,1,4,1,164,20,15,1,3,1,19),_BfdSessPerfEchoPktDropHC_Type())
bfdSessPerfEchoPktDropHC.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessPerfEchoPktDropHC.setStatus(_B)
_BfdSessDiscMapTable_Object=MibTable
bfdSessDiscMapTable=_BfdSessDiscMapTable_Object((1,3,6,1,4,1,164,20,15,1,4))
if mibBuilder.loadTexts:bfdSessDiscMapTable.setStatus(_B)
_BfdSessDiscMapEntry_Object=MibTableRow
bfdSessDiscMapEntry=_BfdSessDiscMapEntry_Object((1,3,6,1,4,1,164,20,15,1,4,1))
bfdSessDiscMapEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:bfdSessDiscMapEntry.setStatus(_B)
_BfdSessDiscMapIndex_Type=BfdSessIndexTC
_BfdSessDiscMapIndex_Object=MibTableColumn
bfdSessDiscMapIndex=_BfdSessDiscMapIndex_Object((1,3,6,1,4,1,164,20,15,1,4,1,1),_BfdSessDiscMapIndex_Type())
bfdSessDiscMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessDiscMapIndex.setStatus(_B)
_BfdSessDiscMapStorageType_Type=StorageType
_BfdSessDiscMapStorageType_Object=MibTableColumn
bfdSessDiscMapStorageType=_BfdSessDiscMapStorageType_Object((1,3,6,1,4,1,164,20,15,1,4,1,2),_BfdSessDiscMapStorageType_Type())
bfdSessDiscMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDiscMapStorageType.setStatus(_B)
_BfdSessDiscMapRowStatus_Type=RowStatus
_BfdSessDiscMapRowStatus_Object=MibTableColumn
bfdSessDiscMapRowStatus=_BfdSessDiscMapRowStatus_Object((1,3,6,1,4,1,164,20,15,1,4,1,3),_BfdSessDiscMapRowStatus_Type())
bfdSessDiscMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessDiscMapRowStatus.setStatus(_B)
_BfdSessIpMapTable_Object=MibTable
bfdSessIpMapTable=_BfdSessIpMapTable_Object((1,3,6,1,4,1,164,20,15,1,5))
if mibBuilder.loadTexts:bfdSessIpMapTable.setStatus(_B)
_BfdSessIpMapEntry_Object=MibTableRow
bfdSessIpMapEntry=_BfdSessIpMapEntry_Object((1,3,6,1,4,1,164,20,15,1,5,1))
bfdSessIpMapEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:bfdSessIpMapEntry.setStatus(_B)
_BfdSessIpMapIndex_Type=BfdSessIndexTC
_BfdSessIpMapIndex_Object=MibTableColumn
bfdSessIpMapIndex=_BfdSessIpMapIndex_Object((1,3,6,1,4,1,164,20,15,1,5,1,1),_BfdSessIpMapIndex_Type())
bfdSessIpMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessIpMapIndex.setStatus(_B)
_BfdSessIpMapStorageType_Type=StorageType
_BfdSessIpMapStorageType_Object=MibTableColumn
bfdSessIpMapStorageType=_BfdSessIpMapStorageType_Object((1,3,6,1,4,1,164,20,15,1,5,1,2),_BfdSessIpMapStorageType_Type())
bfdSessIpMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessIpMapStorageType.setStatus(_B)
_BfdSessIpMapRowStatus_Type=RowStatus
_BfdSessIpMapRowStatus_Object=MibTableColumn
bfdSessIpMapRowStatus=_BfdSessIpMapRowStatus_Object((1,3,6,1,4,1,164,20,15,1,5,1,3),_BfdSessIpMapRowStatus_Type())
bfdSessIpMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdSessIpMapRowStatus.setStatus(_B)
_BfdConformance_ObjectIdentity=ObjectIdentity
bfdConformance=_BfdConformance_ObjectIdentity((1,3,6,1,4,1,164,20,15,2))
_BfdGroups_ObjectIdentity=ObjectIdentity
bfdGroups=_BfdGroups_ObjectIdentity((1,3,6,1,4,1,164,20,15,2,1))
_BfdCompliances_ObjectIdentity=ObjectIdentity
bfdCompliances=_BfdCompliances_ObjectIdentity((1,3,6,1,4,1,164,20,15,2,2))
bfdSessEntry.registerAugmentions((_A,_a))
bfdSessPerfEntry.setIndexNames(*bfdSessEntry.getIndexNames())
bfdSessionGroup=ObjectGroup((1,3,6,1,4,1,164,20,15,2,1,1))
bfdSessionGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:bfdSessionGroup.setStatus(_B)
bfdSessionReadOnlyGroup=ObjectGroup((1,3,6,1,4,1,164,20,15,2,1,2))
bfdSessionReadOnlyGroup.setObjects(*((_A,_I),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_F),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:bfdSessionReadOnlyGroup.setStatus(_B)
bfdSessionPerfGroup=ObjectGroup((1,3,6,1,4,1,164,20,15,2,1,3))
bfdSessionPerfGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:bfdSessionPerfGroup.setStatus(_B)
bfdSessionPerfHCGroup=ObjectGroup((1,3,6,1,4,1,164,20,15,2,1,4))
bfdSessionPerfHCGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:bfdSessionPerfHCGroup.setStatus(_B)
bfdSessUp=NotificationType((1,3,6,1,4,1,164,20,15,0,1))
bfdSessUp.setObjects(*((_A,_F),(_A,_F)))
if mibBuilder.loadTexts:bfdSessUp.setStatus(_B)
bfdSessDown=NotificationType((1,3,6,1,4,1,164,20,15,0,2))
bfdSessDown.setObjects(*((_A,_F),(_A,_F)))
if mibBuilder.loadTexts:bfdSessDown.setStatus(_B)
bfdNotificationGroup=NotificationGroup((1,3,6,1,4,1,164,20,15,2,1,5))
bfdNotificationGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:bfdNotificationGroup.setStatus(_B)
bfdModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,164,20,15,2,2,1))
bfdModuleFullCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:bfdModuleFullCompliance.setStatus(_B)
bfdModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,164,20,15,2,2,2))
bfdModuleReadOnlyCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:bfdModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'radExperimental':radExperimental,'bfdMIB':bfdMIB,'bfdNotifications':bfdNotifications,_AU:bfdSessUp,_AV:bfdSessDown,'bfdObjects':bfdObjects,'bfdScalarObjects':bfdScalarObjects,_b:bfdAdminStatus,_c:bfdSessNotificationsEnable,'bfdSessTable':bfdSessTable,'bfdSessEntry':bfdSessEntry,_Z:bfdSessIndex,_d:bfdSessVersionNumber,_e:bfdSessType,_I:bfdSessDiscriminator,_A3:bfdSessRemoteDiscr,_f:bfdSessDestinationUdpPort,_g:bfdSessSourceUdpPort,_h:bfdSessEchoSourceUdpPort,_i:bfdSessAdminStatus,_A4:bfdSessState,_A5:bfdSessRemoteHeardFlag,_F:bfdSessDiag,_j:bfdSessOperMode,_k:bfdSessDemandModeDesiredFlag,_l:bfdSessControlPlaneIndepFlag,_m:bfdSessMultipointFlag,_J:bfdSessInterface,_K:bfdSessSrcAddrType,_L:bfdSessSrcAddr,_M:bfdSessDstAddrType,_N:bfdSessDstAddr,_n:bfdSessGTSM,_o:bfdSessGTSMTTL,_p:bfdSessDesiredMinTxInterval,_q:bfdSessReqMinRxInterval,_r:bfdSessReqMinEchoRxInterval,_s:bfdSessDetectMult,_A6:bfdSessNegotiatedInterval,_A7:bfdSessNegotiatedEchoInterval,_A8:bfdSessNegotiatedDetectMult,_t:bfdSessAuthPresFlag,_u:bfdSessAuthenticationType,_v:bfdSessAuthenticationKeyID,_w:bfdSessAuthenticationKey,_x:bfdSessStorageType,_y:bfdSessRowStatus,'bfdSessPerfTable':bfdSessPerfTable,_a:bfdSessPerfEntry,_AB:bfdSessPerfCtrlPktIn,_AC:bfdSessPerfCtrlPktOut,_AD:bfdSessPerfCtrlPktDrop,_AE:bfdSessPerfCtrlPktDropLastTime,_AF:bfdSessPerfEchoPktIn,_AG:bfdSessPerfEchoPktOut,_AH:bfdSessPerfEchoPktDrop,_AI:bfdSessPerfEchoPktDropLastTime,_AJ:bfdSessUpTime,_AK:bfdSessPerfLastSessDownTime,_AL:bfdSessPerfLastCommLostDiag,_AM:bfdSessPerfSessUpCount,_AN:bfdSessPerfDiscTime,_AO:bfdSessPerfCtrlPktInHC,_AP:bfdSessPerfCtrlPktOutHC,_AQ:bfdSessPerfCtrlPktDropHC,_AR:bfdSessPerfEchoPktInHC,_AS:bfdSessPerfEchoPktOutHC,_AT:bfdSessPerfEchoPktDropHC,'bfdSessDiscMapTable':bfdSessDiscMapTable,'bfdSessDiscMapEntry':bfdSessDiscMapEntry,_A9:bfdSessDiscMapIndex,_z:bfdSessDiscMapStorageType,_A0:bfdSessDiscMapRowStatus,'bfdSessIpMapTable':bfdSessIpMapTable,'bfdSessIpMapEntry':bfdSessIpMapEntry,_AA:bfdSessIpMapIndex,_A1:bfdSessIpMapStorageType,_A2:bfdSessIpMapRowStatus,'bfdConformance':bfdConformance,'bfdGroups':bfdGroups,_O:bfdSessionGroup,_P:bfdSessionReadOnlyGroup,_Q:bfdSessionPerfGroup,_S:bfdSessionPerfHCGroup,_R:bfdNotificationGroup,'bfdCompliances':bfdCompliances,'bfdModuleFullCompliance':bfdModuleFullCompliance,'bfdModuleReadOnlyCompliance':bfdModuleReadOnlyCompliance})