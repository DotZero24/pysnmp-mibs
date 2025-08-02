_AV='extremeBfdSessDown'
_AU='extremeBfdSessUp'
_AT='extremeBfdSessPerfEchoPktDropHC'
_AS='extremeBfdSessPerfEchoPktOutHC'
_AR='extremeBfdSessPerfEchoPktInHC'
_AQ='extremeBfdSessPerfCtrlPktDropHC'
_AP='extremeBfdSessPerfCtrlPktOutHC'
_AO='extremeBfdSessPerfCtrlPktInHC'
_AN='extremeBfdSessPerfDiscTime'
_AM='extremeBfdSessPerfSessUpCount'
_AL='extremeBfdSessPerfLastCommLostDiag'
_AK='extremeBfdSessPerfLastSessDownTime'
_AJ='extremeBfdSessUpTime'
_AI='extremeBfdSessPerfEchoPktDropLastTime'
_AH='extremeBfdSessPerfEchoPktDrop'
_AG='extremeBfdSessPerfEchoPktOut'
_AF='extremeBfdSessPerfEchoPktIn'
_AE='extremeBfdSessPerfCtrlPktDropLastTime'
_AD='extremeBfdSessPerfCtrlPktDrop'
_AC='extremeBfdSessPerfCtrlPktOut'
_AB='extremeBfdSessPerfCtrlPktIn'
_AA='extremeBfdSessIpMapIndex'
_A9='extremeBfdSessDiscMapIndex'
_A8='extremeBfdSessNegotiatedDetectMult'
_A7='extremeBfdSessNegotiatedEchoInterval'
_A6='extremeBfdSessNegotiatedInterval'
_A5='extremeBfdSessRemoteHeardFlag'
_A4='extremeBfdSessState'
_A3='extremeBfdSessRemoteDiscr'
_A2='extremeBfdSessIpMapRowStatus'
_A1='extremeBfdSessIpMapStorageType'
_A0='extremeBfdSessDiscMapRowStatus'
_z='extremeBfdSessDiscMapStorageType'
_y='extremeBfdSessRowStatus'
_x='extremeBfdSessStorageType'
_w='extremeBfdSessAuthenticationKey'
_v='extremeBfdSessAuthenticationKeyID'
_u='extremeBfdSessAuthenticationType'
_t='extremeBfdSessAuthPresFlag'
_s='extremeBfdSessDetectMult'
_r='extremeBfdSessReqMinEchoRxInterval'
_q='extremeBfdSessReqMinRxInterval'
_p='extremeBfdSessDesiredMinTxInterval'
_o='extremeBfdSessGTSMTTL'
_n='extremeBfdSessGTSM'
_m='extremeBfdSessMultipointFlag'
_l='extremeBfdSessControlPlaneIndepFlag'
_k='extremeBfdSessDemandModeDesiredFlag'
_j='extremeBfdSessAdminStatus'
_i='extremeBfdSessEchoSourceUdpPort'
_h='extremeBfdSessSourceUdpPort'
_g='extremeBfdSessDestinationUdpPort'
_f='extremeBfdSessType'
_e='extremeBfdSessVersionNumber'
_d='extremeBfdSessNotificationsEnable'
_c='extremeBfdAdminStatus'
_b='extremeBfdSessPerfEntry'
_a='extremeBfdSessIndex'
_Z='read-write'
_Y='InetPortNumber'
_X='ExtremeBfdSessStateTC'
_W='ExtremeBfdSessAuthenticationTypeTC'
_V='ExtremeBfdCtrlSourcePortNumberTC'
_U='ExtremeBfdCtrlDestPortNumberTC'
_T='extremeBfdSessionPerfHCGroup'
_S='extremeBfdNotificationGroup'
_R='extremeBfdSessionPerfGroup'
_Q='extremeBfdSessionReadOnlyGroup'
_P='extremeBfdSessionGroup'
_O='extremeBfdSessDstAddr'
_N='extremeBfdSessDstAddrType'
_M='extremeBfdSessSrcAddr'
_L='extremeBfdSessSrcAddrType'
_K='extremeBfdSessInterface'
_J='extremeBfdSessDiscriminator'
_I='extremeBfdSessDiag'
_H='extremeBfdSessOperMode'
_G='Integer32'
_F='Unsigned32'
_E='TruthValue'
_D='read-only'
_C='read-create'
_B='current'
_A='EXTREME-IETF-BFD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeBfd,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeBfd')
ExtremeBfdCtrlDestPortNumberTC,ExtremeBfdCtrlSourcePortNumberTC,ExtremeBfdDiagTC,ExtremeBfdIntervalTC,ExtremeBfdMultiplierTC,ExtremeBfdSessAuthenticationTypeTC,ExtremeBfdSessIndexTC,ExtremeBfdSessOperModeTC,ExtremeBfdSessStateTC,ExtremeBfdSessTypeTC,ExtremeBfdSessionAuthenticationKeyTC=mibBuilder.importSymbols('EXTREME-IETF-BFD-TC-MIB',_U,_V,'ExtremeBfdDiagTC','ExtremeBfdIntervalTC','ExtremeBfdMultiplierTC',_W,'ExtremeBfdSessIndexTC','ExtremeBfdSessOperModeTC',_X,'ExtremeBfdSessTypeTC','ExtremeBfdSessionAuthenticationKeyTC')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_Y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_E)
extremeIetfBfdMib=ModuleIdentity((1,3,6,1,4,1,1916,1,43,2))
if mibBuilder.loadTexts:extremeIetfBfdMib.setRevisions(('2012-12-17 12:00',))
_ExtremeBfdNotifications_ObjectIdentity=ObjectIdentity
extremeBfdNotifications=_ExtremeBfdNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,43,2,0))
_ExtremeBfdObjects_ObjectIdentity=ObjectIdentity
extremeBfdObjects=_ExtremeBfdObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,43,2,1))
_ExtremeBfdScalarObjects_ObjectIdentity=ObjectIdentity
extremeBfdScalarObjects=_ExtremeBfdScalarObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,43,2,1,1))
class _ExtremeBfdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ExtremeBfdAdminStatus_Type.__name__=_G
_ExtremeBfdAdminStatus_Object=MibScalar
extremeBfdAdminStatus=_ExtremeBfdAdminStatus_Object((1,3,6,1,4,1,1916,1,43,2,1,1,1),_ExtremeBfdAdminStatus_Type())
extremeBfdAdminStatus.setMaxAccess(_Z)
if mibBuilder.loadTexts:extremeBfdAdminStatus.setStatus(_B)
class _ExtremeBfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_ExtremeBfdSessNotificationsEnable_Type.__name__=_E
_ExtremeBfdSessNotificationsEnable_Object=MibScalar
extremeBfdSessNotificationsEnable=_ExtremeBfdSessNotificationsEnable_Object((1,3,6,1,4,1,1916,1,43,2,1,1,2),_ExtremeBfdSessNotificationsEnable_Type())
extremeBfdSessNotificationsEnable.setMaxAccess(_Z)
if mibBuilder.loadTexts:extremeBfdSessNotificationsEnable.setStatus(_B)
_ExtremeBfdSessTable_Object=MibTable
extremeBfdSessTable=_ExtremeBfdSessTable_Object((1,3,6,1,4,1,1916,1,43,2,1,2))
if mibBuilder.loadTexts:extremeBfdSessTable.setStatus(_B)
_ExtremeBfdSessEntry_Object=MibTableRow
extremeBfdSessEntry=_ExtremeBfdSessEntry_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1))
extremeBfdSessEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:extremeBfdSessEntry.setStatus(_B)
_ExtremeBfdSessIndex_Type=ExtremeBfdSessIndexTC
_ExtremeBfdSessIndex_Object=MibTableColumn
extremeBfdSessIndex=_ExtremeBfdSessIndex_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,1),_ExtremeBfdSessIndex_Type())
extremeBfdSessIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:extremeBfdSessIndex.setStatus(_B)
class _ExtremeBfdSessVersionNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ExtremeBfdSessVersionNumber_Type.__name__=_F
_ExtremeBfdSessVersionNumber_Object=MibTableColumn
extremeBfdSessVersionNumber=_ExtremeBfdSessVersionNumber_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,2),_ExtremeBfdSessVersionNumber_Type())
extremeBfdSessVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessVersionNumber.setStatus(_B)
_ExtremeBfdSessType_Type=ExtremeBfdSessTypeTC
_ExtremeBfdSessType_Object=MibTableColumn
extremeBfdSessType=_ExtremeBfdSessType_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,3),_ExtremeBfdSessType_Type())
extremeBfdSessType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessType.setStatus(_B)
class _ExtremeBfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ExtremeBfdSessDiscriminator_Type.__name__=_F
_ExtremeBfdSessDiscriminator_Object=MibTableColumn
extremeBfdSessDiscriminator=_ExtremeBfdSessDiscriminator_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,4),_ExtremeBfdSessDiscriminator_Type())
extremeBfdSessDiscriminator.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessDiscriminator.setStatus(_B)
class _ExtremeBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_ExtremeBfdSessRemoteDiscr_Type.__name__=_F
_ExtremeBfdSessRemoteDiscr_Object=MibTableColumn
extremeBfdSessRemoteDiscr=_ExtremeBfdSessRemoteDiscr_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,5),_ExtremeBfdSessRemoteDiscr_Type())
extremeBfdSessRemoteDiscr.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessRemoteDiscr.setStatus(_B)
class _ExtremeBfdSessDestinationUdpPort_Type(ExtremeBfdCtrlDestPortNumberTC):defaultValue=0
_ExtremeBfdSessDestinationUdpPort_Type.__name__=_U
_ExtremeBfdSessDestinationUdpPort_Object=MibTableColumn
extremeBfdSessDestinationUdpPort=_ExtremeBfdSessDestinationUdpPort_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,6),_ExtremeBfdSessDestinationUdpPort_Type())
extremeBfdSessDestinationUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessDestinationUdpPort.setStatus(_B)
class _ExtremeBfdSessSourceUdpPort_Type(ExtremeBfdCtrlSourcePortNumberTC):defaultValue=0
_ExtremeBfdSessSourceUdpPort_Type.__name__=_V
_ExtremeBfdSessSourceUdpPort_Object=MibTableColumn
extremeBfdSessSourceUdpPort=_ExtremeBfdSessSourceUdpPort_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,7),_ExtremeBfdSessSourceUdpPort_Type())
extremeBfdSessSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessSourceUdpPort.setStatus(_B)
class _ExtremeBfdSessEchoSourceUdpPort_Type(InetPortNumber):defaultValue=0
_ExtremeBfdSessEchoSourceUdpPort_Type.__name__=_Y
_ExtremeBfdSessEchoSourceUdpPort_Object=MibTableColumn
extremeBfdSessEchoSourceUdpPort=_ExtremeBfdSessEchoSourceUdpPort_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,8),_ExtremeBfdSessEchoSourceUdpPort_Type())
extremeBfdSessEchoSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessEchoSourceUdpPort.setStatus(_B)
class _ExtremeBfdSessAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_ExtremeBfdSessAdminStatus_Type.__name__=_G
_ExtremeBfdSessAdminStatus_Object=MibTableColumn
extremeBfdSessAdminStatus=_ExtremeBfdSessAdminStatus_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,9),_ExtremeBfdSessAdminStatus_Type())
extremeBfdSessAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessAdminStatus.setStatus(_B)
class _ExtremeBfdSessState_Type(ExtremeBfdSessStateTC):defaultValue=2
_ExtremeBfdSessState_Type.__name__=_X
_ExtremeBfdSessState_Object=MibTableColumn
extremeBfdSessState=_ExtremeBfdSessState_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,10),_ExtremeBfdSessState_Type())
extremeBfdSessState.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessState.setStatus(_B)
class _ExtremeBfdSessRemoteHeardFlag_Type(TruthValue):defaultValue=2
_ExtremeBfdSessRemoteHeardFlag_Type.__name__=_E
_ExtremeBfdSessRemoteHeardFlag_Object=MibTableColumn
extremeBfdSessRemoteHeardFlag=_ExtremeBfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,11),_ExtremeBfdSessRemoteHeardFlag_Type())
extremeBfdSessRemoteHeardFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessRemoteHeardFlag.setStatus(_B)
_ExtremeBfdSessDiag_Type=ExtremeBfdDiagTC
_ExtremeBfdSessDiag_Object=MibTableColumn
extremeBfdSessDiag=_ExtremeBfdSessDiag_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,12),_ExtremeBfdSessDiag_Type())
extremeBfdSessDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessDiag.setStatus(_B)
_ExtremeBfdSessOperMode_Type=ExtremeBfdSessOperModeTC
_ExtremeBfdSessOperMode_Object=MibTableColumn
extremeBfdSessOperMode=_ExtremeBfdSessOperMode_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,13),_ExtremeBfdSessOperMode_Type())
extremeBfdSessOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessOperMode.setStatus(_B)
class _ExtremeBfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_ExtremeBfdSessDemandModeDesiredFlag_Type.__name__=_E
_ExtremeBfdSessDemandModeDesiredFlag_Object=MibTableColumn
extremeBfdSessDemandModeDesiredFlag=_ExtremeBfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,14),_ExtremeBfdSessDemandModeDesiredFlag_Type())
extremeBfdSessDemandModeDesiredFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessDemandModeDesiredFlag.setStatus(_B)
class _ExtremeBfdSessControlPlaneIndepFlag_Type(TruthValue):defaultValue=2
_ExtremeBfdSessControlPlaneIndepFlag_Type.__name__=_E
_ExtremeBfdSessControlPlaneIndepFlag_Object=MibTableColumn
extremeBfdSessControlPlaneIndepFlag=_ExtremeBfdSessControlPlaneIndepFlag_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,15),_ExtremeBfdSessControlPlaneIndepFlag_Type())
extremeBfdSessControlPlaneIndepFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessControlPlaneIndepFlag.setStatus(_B)
class _ExtremeBfdSessMultipointFlag_Type(TruthValue):defaultValue=2
_ExtremeBfdSessMultipointFlag_Type.__name__=_E
_ExtremeBfdSessMultipointFlag_Object=MibTableColumn
extremeBfdSessMultipointFlag=_ExtremeBfdSessMultipointFlag_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,16),_ExtremeBfdSessMultipointFlag_Type())
extremeBfdSessMultipointFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessMultipointFlag.setStatus(_B)
_ExtremeBfdSessInterface_Type=InterfaceIndexOrZero
_ExtremeBfdSessInterface_Object=MibTableColumn
extremeBfdSessInterface=_ExtremeBfdSessInterface_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,17),_ExtremeBfdSessInterface_Type())
extremeBfdSessInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessInterface.setStatus(_B)
_ExtremeBfdSessSrcAddrType_Type=InetAddressType
_ExtremeBfdSessSrcAddrType_Object=MibTableColumn
extremeBfdSessSrcAddrType=_ExtremeBfdSessSrcAddrType_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,18),_ExtremeBfdSessSrcAddrType_Type())
extremeBfdSessSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessSrcAddrType.setStatus(_B)
_ExtremeBfdSessSrcAddr_Type=InetAddress
_ExtremeBfdSessSrcAddr_Object=MibTableColumn
extremeBfdSessSrcAddr=_ExtremeBfdSessSrcAddr_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,19),_ExtremeBfdSessSrcAddr_Type())
extremeBfdSessSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessSrcAddr.setStatus(_B)
_ExtremeBfdSessDstAddrType_Type=InetAddressType
_ExtremeBfdSessDstAddrType_Object=MibTableColumn
extremeBfdSessDstAddrType=_ExtremeBfdSessDstAddrType_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,20),_ExtremeBfdSessDstAddrType_Type())
extremeBfdSessDstAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessDstAddrType.setStatus(_B)
_ExtremeBfdSessDstAddr_Type=InetAddress
_ExtremeBfdSessDstAddr_Object=MibTableColumn
extremeBfdSessDstAddr=_ExtremeBfdSessDstAddr_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,21),_ExtremeBfdSessDstAddr_Type())
extremeBfdSessDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessDstAddr.setStatus(_B)
class _ExtremeBfdSessGTSM_Type(TruthValue):defaultValue=2
_ExtremeBfdSessGTSM_Type.__name__=_E
_ExtremeBfdSessGTSM_Object=MibTableColumn
extremeBfdSessGTSM=_ExtremeBfdSessGTSM_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,22),_ExtremeBfdSessGTSM_Type())
extremeBfdSessGTSM.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessGTSM.setStatus(_B)
class _ExtremeBfdSessGTSMTTL_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeBfdSessGTSMTTL_Type.__name__=_F
_ExtremeBfdSessGTSMTTL_Object=MibTableColumn
extremeBfdSessGTSMTTL=_ExtremeBfdSessGTSMTTL_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,23),_ExtremeBfdSessGTSMTTL_Type())
extremeBfdSessGTSMTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessGTSMTTL.setStatus(_B)
_ExtremeBfdSessDesiredMinTxInterval_Type=ExtremeBfdIntervalTC
_ExtremeBfdSessDesiredMinTxInterval_Object=MibTableColumn
extremeBfdSessDesiredMinTxInterval=_ExtremeBfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,24),_ExtremeBfdSessDesiredMinTxInterval_Type())
extremeBfdSessDesiredMinTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessDesiredMinTxInterval.setStatus(_B)
_ExtremeBfdSessReqMinRxInterval_Type=ExtremeBfdIntervalTC
_ExtremeBfdSessReqMinRxInterval_Object=MibTableColumn
extremeBfdSessReqMinRxInterval=_ExtremeBfdSessReqMinRxInterval_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,25),_ExtremeBfdSessReqMinRxInterval_Type())
extremeBfdSessReqMinRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessReqMinRxInterval.setStatus(_B)
_ExtremeBfdSessReqMinEchoRxInterval_Type=ExtremeBfdIntervalTC
_ExtremeBfdSessReqMinEchoRxInterval_Object=MibTableColumn
extremeBfdSessReqMinEchoRxInterval=_ExtremeBfdSessReqMinEchoRxInterval_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,26),_ExtremeBfdSessReqMinEchoRxInterval_Type())
extremeBfdSessReqMinEchoRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessReqMinEchoRxInterval.setStatus(_B)
_ExtremeBfdSessDetectMult_Type=ExtremeBfdMultiplierTC
_ExtremeBfdSessDetectMult_Object=MibTableColumn
extremeBfdSessDetectMult=_ExtremeBfdSessDetectMult_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,27),_ExtremeBfdSessDetectMult_Type())
extremeBfdSessDetectMult.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessDetectMult.setStatus(_B)
_ExtremeBfdSessNegotiatedInterval_Type=ExtremeBfdIntervalTC
_ExtremeBfdSessNegotiatedInterval_Object=MibTableColumn
extremeBfdSessNegotiatedInterval=_ExtremeBfdSessNegotiatedInterval_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,28),_ExtremeBfdSessNegotiatedInterval_Type())
extremeBfdSessNegotiatedInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessNegotiatedInterval.setStatus(_B)
_ExtremeBfdSessNegotiatedEchoInterval_Type=ExtremeBfdIntervalTC
_ExtremeBfdSessNegotiatedEchoInterval_Object=MibTableColumn
extremeBfdSessNegotiatedEchoInterval=_ExtremeBfdSessNegotiatedEchoInterval_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,29),_ExtremeBfdSessNegotiatedEchoInterval_Type())
extremeBfdSessNegotiatedEchoInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessNegotiatedEchoInterval.setStatus(_B)
_ExtremeBfdSessNegotiatedDetectMult_Type=ExtremeBfdMultiplierTC
_ExtremeBfdSessNegotiatedDetectMult_Object=MibTableColumn
extremeBfdSessNegotiatedDetectMult=_ExtremeBfdSessNegotiatedDetectMult_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,30),_ExtremeBfdSessNegotiatedDetectMult_Type())
extremeBfdSessNegotiatedDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessNegotiatedDetectMult.setStatus(_B)
class _ExtremeBfdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_ExtremeBfdSessAuthPresFlag_Type.__name__=_E
_ExtremeBfdSessAuthPresFlag_Object=MibTableColumn
extremeBfdSessAuthPresFlag=_ExtremeBfdSessAuthPresFlag_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,31),_ExtremeBfdSessAuthPresFlag_Type())
extremeBfdSessAuthPresFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessAuthPresFlag.setStatus(_B)
class _ExtremeBfdSessAuthenticationType_Type(ExtremeBfdSessAuthenticationTypeTC):defaultValue=-1
_ExtremeBfdSessAuthenticationType_Type.__name__=_W
_ExtremeBfdSessAuthenticationType_Object=MibTableColumn
extremeBfdSessAuthenticationType=_ExtremeBfdSessAuthenticationType_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,32),_ExtremeBfdSessAuthenticationType_Type())
extremeBfdSessAuthenticationType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessAuthenticationType.setStatus(_B)
class _ExtremeBfdSessAuthenticationKeyID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_ExtremeBfdSessAuthenticationKeyID_Type.__name__=_G
_ExtremeBfdSessAuthenticationKeyID_Object=MibTableColumn
extremeBfdSessAuthenticationKeyID=_ExtremeBfdSessAuthenticationKeyID_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,33),_ExtremeBfdSessAuthenticationKeyID_Type())
extremeBfdSessAuthenticationKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessAuthenticationKeyID.setStatus(_B)
_ExtremeBfdSessAuthenticationKey_Type=ExtremeBfdSessionAuthenticationKeyTC
_ExtremeBfdSessAuthenticationKey_Object=MibTableColumn
extremeBfdSessAuthenticationKey=_ExtremeBfdSessAuthenticationKey_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,34),_ExtremeBfdSessAuthenticationKey_Type())
extremeBfdSessAuthenticationKey.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessAuthenticationKey.setStatus(_B)
_ExtremeBfdSessStorageType_Type=StorageType
_ExtremeBfdSessStorageType_Object=MibTableColumn
extremeBfdSessStorageType=_ExtremeBfdSessStorageType_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,35),_ExtremeBfdSessStorageType_Type())
extremeBfdSessStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessStorageType.setStatus(_B)
_ExtremeBfdSessRowStatus_Type=RowStatus
_ExtremeBfdSessRowStatus_Object=MibTableColumn
extremeBfdSessRowStatus=_ExtremeBfdSessRowStatus_Object((1,3,6,1,4,1,1916,1,43,2,1,2,1,36),_ExtremeBfdSessRowStatus_Type())
extremeBfdSessRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessRowStatus.setStatus(_B)
_ExtremeBfdSessPerfTable_Object=MibTable
extremeBfdSessPerfTable=_ExtremeBfdSessPerfTable_Object((1,3,6,1,4,1,1916,1,43,2,1,3))
if mibBuilder.loadTexts:extremeBfdSessPerfTable.setStatus(_B)
_ExtremeBfdSessPerfEntry_Object=MibTableRow
extremeBfdSessPerfEntry=_ExtremeBfdSessPerfEntry_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1))
if mibBuilder.loadTexts:extremeBfdSessPerfEntry.setStatus(_B)
_ExtremeBfdSessPerfCtrlPktIn_Type=Counter32
_ExtremeBfdSessPerfCtrlPktIn_Object=MibTableColumn
extremeBfdSessPerfCtrlPktIn=_ExtremeBfdSessPerfCtrlPktIn_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,1),_ExtremeBfdSessPerfCtrlPktIn_Type())
extremeBfdSessPerfCtrlPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfCtrlPktIn.setStatus(_B)
_ExtremeBfdSessPerfCtrlPktOut_Type=Counter32
_ExtremeBfdSessPerfCtrlPktOut_Object=MibTableColumn
extremeBfdSessPerfCtrlPktOut=_ExtremeBfdSessPerfCtrlPktOut_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,2),_ExtremeBfdSessPerfCtrlPktOut_Type())
extremeBfdSessPerfCtrlPktOut.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfCtrlPktOut.setStatus(_B)
_ExtremeBfdSessPerfCtrlPktDrop_Type=Counter32
_ExtremeBfdSessPerfCtrlPktDrop_Object=MibTableColumn
extremeBfdSessPerfCtrlPktDrop=_ExtremeBfdSessPerfCtrlPktDrop_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,3),_ExtremeBfdSessPerfCtrlPktDrop_Type())
extremeBfdSessPerfCtrlPktDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfCtrlPktDrop.setStatus(_B)
_ExtremeBfdSessPerfCtrlPktDropLastTime_Type=TimeStamp
_ExtremeBfdSessPerfCtrlPktDropLastTime_Object=MibTableColumn
extremeBfdSessPerfCtrlPktDropLastTime=_ExtremeBfdSessPerfCtrlPktDropLastTime_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,4),_ExtremeBfdSessPerfCtrlPktDropLastTime_Type())
extremeBfdSessPerfCtrlPktDropLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfCtrlPktDropLastTime.setStatus(_B)
_ExtremeBfdSessPerfEchoPktIn_Type=Counter32
_ExtremeBfdSessPerfEchoPktIn_Object=MibTableColumn
extremeBfdSessPerfEchoPktIn=_ExtremeBfdSessPerfEchoPktIn_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,5),_ExtremeBfdSessPerfEchoPktIn_Type())
extremeBfdSessPerfEchoPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfEchoPktIn.setStatus(_B)
_ExtremeBfdSessPerfEchoPktOut_Type=Counter32
_ExtremeBfdSessPerfEchoPktOut_Object=MibTableColumn
extremeBfdSessPerfEchoPktOut=_ExtremeBfdSessPerfEchoPktOut_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,6),_ExtremeBfdSessPerfEchoPktOut_Type())
extremeBfdSessPerfEchoPktOut.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfEchoPktOut.setStatus(_B)
_ExtremeBfdSessPerfEchoPktDrop_Type=Counter32
_ExtremeBfdSessPerfEchoPktDrop_Object=MibTableColumn
extremeBfdSessPerfEchoPktDrop=_ExtremeBfdSessPerfEchoPktDrop_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,7),_ExtremeBfdSessPerfEchoPktDrop_Type())
extremeBfdSessPerfEchoPktDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfEchoPktDrop.setStatus(_B)
_ExtremeBfdSessPerfEchoPktDropLastTime_Type=TimeStamp
_ExtremeBfdSessPerfEchoPktDropLastTime_Object=MibTableColumn
extremeBfdSessPerfEchoPktDropLastTime=_ExtremeBfdSessPerfEchoPktDropLastTime_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,8),_ExtremeBfdSessPerfEchoPktDropLastTime_Type())
extremeBfdSessPerfEchoPktDropLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfEchoPktDropLastTime.setStatus(_B)
_ExtremeBfdSessUpTime_Type=TimeStamp
_ExtremeBfdSessUpTime_Object=MibTableColumn
extremeBfdSessUpTime=_ExtremeBfdSessUpTime_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,9),_ExtremeBfdSessUpTime_Type())
extremeBfdSessUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessUpTime.setStatus(_B)
_ExtremeBfdSessPerfLastSessDownTime_Type=TimeStamp
_ExtremeBfdSessPerfLastSessDownTime_Object=MibTableColumn
extremeBfdSessPerfLastSessDownTime=_ExtremeBfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,10),_ExtremeBfdSessPerfLastSessDownTime_Type())
extremeBfdSessPerfLastSessDownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfLastSessDownTime.setStatus(_B)
_ExtremeBfdSessPerfLastCommLostDiag_Type=ExtremeBfdDiagTC
_ExtremeBfdSessPerfLastCommLostDiag_Object=MibTableColumn
extremeBfdSessPerfLastCommLostDiag=_ExtremeBfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,11),_ExtremeBfdSessPerfLastCommLostDiag_Type())
extremeBfdSessPerfLastCommLostDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfLastCommLostDiag.setStatus(_B)
_ExtremeBfdSessPerfSessUpCount_Type=Counter32
_ExtremeBfdSessPerfSessUpCount_Object=MibTableColumn
extremeBfdSessPerfSessUpCount=_ExtremeBfdSessPerfSessUpCount_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,12),_ExtremeBfdSessPerfSessUpCount_Type())
extremeBfdSessPerfSessUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfSessUpCount.setStatus(_B)
_ExtremeBfdSessPerfDiscTime_Type=TimeStamp
_ExtremeBfdSessPerfDiscTime_Object=MibTableColumn
extremeBfdSessPerfDiscTime=_ExtremeBfdSessPerfDiscTime_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,13),_ExtremeBfdSessPerfDiscTime_Type())
extremeBfdSessPerfDiscTime.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfDiscTime.setStatus(_B)
_ExtremeBfdSessPerfCtrlPktInHC_Type=Counter64
_ExtremeBfdSessPerfCtrlPktInHC_Object=MibTableColumn
extremeBfdSessPerfCtrlPktInHC=_ExtremeBfdSessPerfCtrlPktInHC_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,14),_ExtremeBfdSessPerfCtrlPktInHC_Type())
extremeBfdSessPerfCtrlPktInHC.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfCtrlPktInHC.setStatus(_B)
_ExtremeBfdSessPerfCtrlPktOutHC_Type=Counter64
_ExtremeBfdSessPerfCtrlPktOutHC_Object=MibTableColumn
extremeBfdSessPerfCtrlPktOutHC=_ExtremeBfdSessPerfCtrlPktOutHC_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,15),_ExtremeBfdSessPerfCtrlPktOutHC_Type())
extremeBfdSessPerfCtrlPktOutHC.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfCtrlPktOutHC.setStatus(_B)
_ExtremeBfdSessPerfCtrlPktDropHC_Type=Counter64
_ExtremeBfdSessPerfCtrlPktDropHC_Object=MibTableColumn
extremeBfdSessPerfCtrlPktDropHC=_ExtremeBfdSessPerfCtrlPktDropHC_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,16),_ExtremeBfdSessPerfCtrlPktDropHC_Type())
extremeBfdSessPerfCtrlPktDropHC.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfCtrlPktDropHC.setStatus(_B)
_ExtremeBfdSessPerfEchoPktInHC_Type=Counter64
_ExtremeBfdSessPerfEchoPktInHC_Object=MibTableColumn
extremeBfdSessPerfEchoPktInHC=_ExtremeBfdSessPerfEchoPktInHC_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,17),_ExtremeBfdSessPerfEchoPktInHC_Type())
extremeBfdSessPerfEchoPktInHC.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfEchoPktInHC.setStatus(_B)
_ExtremeBfdSessPerfEchoPktOutHC_Type=Counter64
_ExtremeBfdSessPerfEchoPktOutHC_Object=MibTableColumn
extremeBfdSessPerfEchoPktOutHC=_ExtremeBfdSessPerfEchoPktOutHC_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,18),_ExtremeBfdSessPerfEchoPktOutHC_Type())
extremeBfdSessPerfEchoPktOutHC.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfEchoPktOutHC.setStatus(_B)
_ExtremeBfdSessPerfEchoPktDropHC_Type=Counter64
_ExtremeBfdSessPerfEchoPktDropHC_Object=MibTableColumn
extremeBfdSessPerfEchoPktDropHC=_ExtremeBfdSessPerfEchoPktDropHC_Object((1,3,6,1,4,1,1916,1,43,2,1,3,1,19),_ExtremeBfdSessPerfEchoPktDropHC_Type())
extremeBfdSessPerfEchoPktDropHC.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessPerfEchoPktDropHC.setStatus(_B)
_ExtremeBfdSessDiscMapTable_Object=MibTable
extremeBfdSessDiscMapTable=_ExtremeBfdSessDiscMapTable_Object((1,3,6,1,4,1,1916,1,43,2,1,4))
if mibBuilder.loadTexts:extremeBfdSessDiscMapTable.setStatus(_B)
_ExtremeBfdSessDiscMapEntry_Object=MibTableRow
extremeBfdSessDiscMapEntry=_ExtremeBfdSessDiscMapEntry_Object((1,3,6,1,4,1,1916,1,43,2,1,4,1))
extremeBfdSessDiscMapEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:extremeBfdSessDiscMapEntry.setStatus(_B)
_ExtremeBfdSessDiscMapIndex_Type=ExtremeBfdSessIndexTC
_ExtremeBfdSessDiscMapIndex_Object=MibTableColumn
extremeBfdSessDiscMapIndex=_ExtremeBfdSessDiscMapIndex_Object((1,3,6,1,4,1,1916,1,43,2,1,4,1,1),_ExtremeBfdSessDiscMapIndex_Type())
extremeBfdSessDiscMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessDiscMapIndex.setStatus(_B)
_ExtremeBfdSessDiscMapStorageType_Type=StorageType
_ExtremeBfdSessDiscMapStorageType_Object=MibTableColumn
extremeBfdSessDiscMapStorageType=_ExtremeBfdSessDiscMapStorageType_Object((1,3,6,1,4,1,1916,1,43,2,1,4,1,2),_ExtremeBfdSessDiscMapStorageType_Type())
extremeBfdSessDiscMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessDiscMapStorageType.setStatus(_B)
_ExtremeBfdSessDiscMapRowStatus_Type=RowStatus
_ExtremeBfdSessDiscMapRowStatus_Object=MibTableColumn
extremeBfdSessDiscMapRowStatus=_ExtremeBfdSessDiscMapRowStatus_Object((1,3,6,1,4,1,1916,1,43,2,1,4,1,3),_ExtremeBfdSessDiscMapRowStatus_Type())
extremeBfdSessDiscMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessDiscMapRowStatus.setStatus(_B)
_ExtremeBfdSessIpMapTable_Object=MibTable
extremeBfdSessIpMapTable=_ExtremeBfdSessIpMapTable_Object((1,3,6,1,4,1,1916,1,43,2,1,5))
if mibBuilder.loadTexts:extremeBfdSessIpMapTable.setStatus(_B)
_ExtremeBfdSessIpMapEntry_Object=MibTableRow
extremeBfdSessIpMapEntry=_ExtremeBfdSessIpMapEntry_Object((1,3,6,1,4,1,1916,1,43,2,1,5,1))
extremeBfdSessIpMapEntry.setIndexNames((0,_A,_K),(0,_A,_L),(0,_A,_M),(0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:extremeBfdSessIpMapEntry.setStatus(_B)
_ExtremeBfdSessIpMapIndex_Type=ExtremeBfdSessIndexTC
_ExtremeBfdSessIpMapIndex_Object=MibTableColumn
extremeBfdSessIpMapIndex=_ExtremeBfdSessIpMapIndex_Object((1,3,6,1,4,1,1916,1,43,2,1,5,1,1),_ExtremeBfdSessIpMapIndex_Type())
extremeBfdSessIpMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeBfdSessIpMapIndex.setStatus(_B)
_ExtremeBfdSessIpMapStorageType_Type=StorageType
_ExtremeBfdSessIpMapStorageType_Object=MibTableColumn
extremeBfdSessIpMapStorageType=_ExtremeBfdSessIpMapStorageType_Object((1,3,6,1,4,1,1916,1,43,2,1,5,1,2),_ExtremeBfdSessIpMapStorageType_Type())
extremeBfdSessIpMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessIpMapStorageType.setStatus(_B)
_ExtremeBfdSessIpMapRowStatus_Type=RowStatus
_ExtremeBfdSessIpMapRowStatus_Object=MibTableColumn
extremeBfdSessIpMapRowStatus=_ExtremeBfdSessIpMapRowStatus_Object((1,3,6,1,4,1,1916,1,43,2,1,5,1,3),_ExtremeBfdSessIpMapRowStatus_Type())
extremeBfdSessIpMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBfdSessIpMapRowStatus.setStatus(_B)
_ExtremeBfdConformance_ObjectIdentity=ObjectIdentity
extremeBfdConformance=_ExtremeBfdConformance_ObjectIdentity((1,3,6,1,4,1,1916,1,43,2,2))
_ExtremeBfdGroups_ObjectIdentity=ObjectIdentity
extremeBfdGroups=_ExtremeBfdGroups_ObjectIdentity((1,3,6,1,4,1,1916,1,43,2,2,1))
_ExtremeBfdCompliances_ObjectIdentity=ObjectIdentity
extremeBfdCompliances=_ExtremeBfdCompliances_ObjectIdentity((1,3,6,1,4,1,1916,1,43,2,2,2))
extremeBfdSessEntry.registerAugmentions((_A,_b))
extremeBfdSessPerfEntry.setIndexNames(*extremeBfdSessEntry.getIndexNames())
extremeBfdSessionGroup=ObjectGroup((1,3,6,1,4,1,1916,1,43,2,2,1,1))
extremeBfdSessionGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_H),(_A,_k),(_A,_l),(_A,_m),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:extremeBfdSessionGroup.setStatus(_B)
extremeBfdSessionReadOnlyGroup=ObjectGroup((1,3,6,1,4,1,1916,1,43,2,2,1,2))
extremeBfdSessionReadOnlyGroup.setObjects(*((_A,_J),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_I),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:extremeBfdSessionReadOnlyGroup.setStatus(_B)
extremeBfdSessionPerfGroup=ObjectGroup((1,3,6,1,4,1,1916,1,43,2,2,1,3))
extremeBfdSessionPerfGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:extremeBfdSessionPerfGroup.setStatus(_B)
extremeBfdSessionPerfHCGroup=ObjectGroup((1,3,6,1,4,1,1916,1,43,2,2,1,4))
extremeBfdSessionPerfHCGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:extremeBfdSessionPerfHCGroup.setStatus(_B)
extremeBfdSessUp=NotificationType((1,3,6,1,4,1,1916,1,43,2,0,1))
extremeBfdSessUp.setObjects(*((_A,_I),(_A,_H)))
if mibBuilder.loadTexts:extremeBfdSessUp.setStatus(_B)
extremeBfdSessDown=NotificationType((1,3,6,1,4,1,1916,1,43,2,0,2))
extremeBfdSessDown.setObjects(*((_A,_I),(_A,_H)))
if mibBuilder.loadTexts:extremeBfdSessDown.setStatus(_B)
extremeBfdNotificationGroup=NotificationGroup((1,3,6,1,4,1,1916,1,43,2,2,1,5))
extremeBfdNotificationGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:extremeBfdNotificationGroup.setStatus(_B)
extremeBfdModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,1916,1,43,2,2,2,1))
extremeBfdModuleFullCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:extremeBfdModuleFullCompliance.setStatus(_B)
extremeBfdModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,1916,1,43,2,2,2,2))
extremeBfdModuleReadOnlyCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:extremeBfdModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'extremeIetfBfdMib':extremeIetfBfdMib,'extremeBfdNotifications':extremeBfdNotifications,_AU:extremeBfdSessUp,_AV:extremeBfdSessDown,'extremeBfdObjects':extremeBfdObjects,'extremeBfdScalarObjects':extremeBfdScalarObjects,_c:extremeBfdAdminStatus,_d:extremeBfdSessNotificationsEnable,'extremeBfdSessTable':extremeBfdSessTable,'extremeBfdSessEntry':extremeBfdSessEntry,_a:extremeBfdSessIndex,_e:extremeBfdSessVersionNumber,_f:extremeBfdSessType,_J:extremeBfdSessDiscriminator,_A3:extremeBfdSessRemoteDiscr,_g:extremeBfdSessDestinationUdpPort,_h:extremeBfdSessSourceUdpPort,_i:extremeBfdSessEchoSourceUdpPort,_j:extremeBfdSessAdminStatus,_A4:extremeBfdSessState,_A5:extremeBfdSessRemoteHeardFlag,_I:extremeBfdSessDiag,_H:extremeBfdSessOperMode,_k:extremeBfdSessDemandModeDesiredFlag,_l:extremeBfdSessControlPlaneIndepFlag,_m:extremeBfdSessMultipointFlag,_K:extremeBfdSessInterface,_L:extremeBfdSessSrcAddrType,_M:extremeBfdSessSrcAddr,_N:extremeBfdSessDstAddrType,_O:extremeBfdSessDstAddr,_n:extremeBfdSessGTSM,_o:extremeBfdSessGTSMTTL,_p:extremeBfdSessDesiredMinTxInterval,_q:extremeBfdSessReqMinRxInterval,_r:extremeBfdSessReqMinEchoRxInterval,_s:extremeBfdSessDetectMult,_A6:extremeBfdSessNegotiatedInterval,_A7:extremeBfdSessNegotiatedEchoInterval,_A8:extremeBfdSessNegotiatedDetectMult,_t:extremeBfdSessAuthPresFlag,_u:extremeBfdSessAuthenticationType,_v:extremeBfdSessAuthenticationKeyID,_w:extremeBfdSessAuthenticationKey,_x:extremeBfdSessStorageType,_y:extremeBfdSessRowStatus,'extremeBfdSessPerfTable':extremeBfdSessPerfTable,_b:extremeBfdSessPerfEntry,_AB:extremeBfdSessPerfCtrlPktIn,_AC:extremeBfdSessPerfCtrlPktOut,_AD:extremeBfdSessPerfCtrlPktDrop,_AE:extremeBfdSessPerfCtrlPktDropLastTime,_AF:extremeBfdSessPerfEchoPktIn,_AG:extremeBfdSessPerfEchoPktOut,_AH:extremeBfdSessPerfEchoPktDrop,_AI:extremeBfdSessPerfEchoPktDropLastTime,_AJ:extremeBfdSessUpTime,_AK:extremeBfdSessPerfLastSessDownTime,_AL:extremeBfdSessPerfLastCommLostDiag,_AM:extremeBfdSessPerfSessUpCount,_AN:extremeBfdSessPerfDiscTime,_AO:extremeBfdSessPerfCtrlPktInHC,_AP:extremeBfdSessPerfCtrlPktOutHC,_AQ:extremeBfdSessPerfCtrlPktDropHC,_AR:extremeBfdSessPerfEchoPktInHC,_AS:extremeBfdSessPerfEchoPktOutHC,_AT:extremeBfdSessPerfEchoPktDropHC,'extremeBfdSessDiscMapTable':extremeBfdSessDiscMapTable,'extremeBfdSessDiscMapEntry':extremeBfdSessDiscMapEntry,_A9:extremeBfdSessDiscMapIndex,_z:extremeBfdSessDiscMapStorageType,_A0:extremeBfdSessDiscMapRowStatus,'extremeBfdSessIpMapTable':extremeBfdSessIpMapTable,'extremeBfdSessIpMapEntry':extremeBfdSessIpMapEntry,_AA:extremeBfdSessIpMapIndex,_A1:extremeBfdSessIpMapStorageType,_A2:extremeBfdSessIpMapRowStatus,'extremeBfdConformance':extremeBfdConformance,'extremeBfdGroups':extremeBfdGroups,_P:extremeBfdSessionGroup,_Q:extremeBfdSessionReadOnlyGroup,_R:extremeBfdSessionPerfGroup,_T:extremeBfdSessionPerfHCGroup,_S:extremeBfdNotificationGroup,'extremeBfdCompliances':extremeBfdCompliances,'extremeBfdModuleFullCompliance':extremeBfdModuleFullCompliance,'extremeBfdModuleReadOnlyCompliance':extremeBfdModuleReadOnlyCompliance})