_AY='fsBfdSessDown'
_AX='fsBfdSessUp'
_AW='fsBfdSessPerfEchoPktDropHC'
_AV='fsBfdSessPerfEchoPktOutHC'
_AU='fsBfdSessPerfEchoPktInHC'
_AT='fsBfdSessPerfCtrlPktDropHC'
_AS='fsBfdSessPerfCtrlPktOutHC'
_AR='fsBfdSessPerfCtrlPktInHC'
_AQ='fsBfdSessPerfDiscTime'
_AP='fsBfdSessPerfSessUpCount'
_AO='fsBfdSessPerfLastCommLostDiag'
_AN='fsBfdSessPerfLastSessDownTime'
_AM='fsBfdSessUpTime'
_AL='fsBfdSessPerfEchoPktDropLastTime'
_AK='fsBfdSessPerfEchoPktDrop'
_AJ='fsBfdSessPerfEchoPktOut'
_AI='fsBfdSessPerfEchoPktIn'
_AH='fsBfdSessPerfCtrlPktDropLastTime'
_AG='fsBfdSessPerfCtrlPktDrop'
_AF='fsBfdSessPerfCtrlPktOut'
_AE='fsBfdSessPerfCtrlPktIn'
_AD='fsBfdSessIpMapIndex'
_AC='fsBfdSessDiscMapIndex'
_AB='fsBfdSessNegotiatedDetectMult'
_AA='fsBfdSessNegotiatedEchoInterval'
_A9='fsBfdSessNegotiatedInterval'
_A8='fsBfdSessRemoteHeardFlag'
_A7='fsBfdSessState'
_A6='fsBfdSessRemoteDiscr'
_A5='fsBfdSessIpMapRowStatus'
_A4='fsBfdSessIpMapStorageType'
_A3='fsBfdSessDiscMapRowStatus'
_A2='fsBfdSessDiscMapStorageType'
_A1='fsBfdSessRowStatus'
_A0='fsBfdSessStorageType'
_z='fsBfdSessAuthenticationKey'
_y='fsBfdSessAuthenticationKeyID'
_x='fsBfdSessAuthenticationType'
_w='fsBfdSessAuthPresFlag'
_v='fsBfdSessDetectMult'
_u='fsBfdSessReqMinEchoRxInterval'
_t='fsBfdSessReqMinRxInterval'
_s='fsBfdSessDesiredMinTxInterval'
_r='fsBfdSessGTSMTTL'
_q='fsBfdSessGTSM'
_p='fsBfdSessMultipointFlag'
_o='fsBfdSessControlPlaneIndepFlag'
_n='fsBfdSessDemandModeDesiredFlag'
_m='fsBfdSessOperMode'
_l='fsBfdSessAdminStatus'
_k='fsBfdSessEchoSourceUdpPort'
_j='fsBfdSessSourceUdpPort'
_i='fsBfdSessDestinationUdpPort'
_h='fsBfdSessType'
_g='fsBfdSessVersionNumber'
_f='fsBfdSessNotificationsEnable'
_e='fsBfdAdminStatus'
_d='fsBfdSessPerfEntry'
_c='FSBfdSessAuthenticationTypeTC'
_b='FSBfdSessStateTC'
_a='FSBfdCtrlSourcePortNumberTC'
_Z='FSBfdCtrlDestPortNumberTC'
_Y='fsBfdSessIndex'
_X='read-write'
_W='InetPortNumber'
_V='fsBfdSessionPerfHCGroup'
_U='fsBfdNotificationGroup'
_T='fsBfdSessionPerfGroup'
_S='fsBfdSessionReadOnlyGroup'
_R='fsBfdSessionGroup'
_Q='fsBfdSessIfDes'
_P='fsBfdSessIfName'
_O='fsBfdSessDstAddr'
_N='fsBfdSessDstAddrType'
_M='fsBfdSessSrcAddr'
_L='fsBfdSessSrcAddrType'
_K='fsBfdSessDiscriminator'
_J='DisplayString'
_I='Integer32'
_H='fsBfdSessInterface'
_G='Unsigned32'
_F='fsBfdSessDiag'
_E='TruthValue'
_D='read-only'
_C='read-create'
_B='FS-BFD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_W)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_E)
fsBfdMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,48))
if mibBuilder.loadTexts:fsBfdMIB.setRevisions(('2012-04-14 12:00',))
class FSBfdSessIndexTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class FSBfdIntervalTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class FSBfdMultiplierTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class FSBfdDiagTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noDiagnostic',0),('controlDetectionTimeExpired',1),('echoFunctionFailed',2),('neighborSignaledSessionDown',3),('forwardingPlaneReset',4),('pathDown',5),('concatenatedPathDown',6),('administrativelyDown',7),('reverseConcatenatedPathDown',8)))
class FSBfdSessTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('singleHop',1),('multiHopTotallyArbitraryPaths',2),('multiHopOutOfBandSignaling',3),('multiHopUnidirectionalLinks',4),('multiPointHead',5),('multiPointTail',6)))
class FSBfdSessOperModeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asyncModeWEchoFunction',1),('asynchModeWOEchoFunction',2),('demandModeWEchoFunction',3),('demandModeWOEchoFunction',4)))
class FSBfdCtrlDestPortNumberTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class FSBfdCtrlSourcePortNumberTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class FSBfdSessStateTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4),('failing',5)))
class FSBfdSessAuthenticationTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5)));namedValues=NamedValues(*(('noAuthentication',-1),('reserved',0),('simplePassword',1),('keyedMD5',2),('meticulousKeyedMD5',3),('keyedSHA1',4),('meticulousKeyedSHA1',5)))
class FSBfdSessionAuthenticationKeyTC(TextualConvention,OctetString):status=_A;displayHint='1x ';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,252))
_FsBfdNotifications_ObjectIdentity=ObjectIdentity
fsBfdNotifications=_FsBfdNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,48,0))
_FsBfdObjects_ObjectIdentity=ObjectIdentity
fsBfdObjects=_FsBfdObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,48,1))
_FsBfdScalarObjects_ObjectIdentity=ObjectIdentity
fsBfdScalarObjects=_FsBfdScalarObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,48,1,1))
class _FsBfdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsBfdAdminStatus_Type.__name__=_I
_FsBfdAdminStatus_Object=MibScalar
fsBfdAdminStatus=_FsBfdAdminStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,1,1),_FsBfdAdminStatus_Type())
fsBfdAdminStatus.setMaxAccess(_X)
if mibBuilder.loadTexts:fsBfdAdminStatus.setStatus(_A)
class _FsBfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_FsBfdSessNotificationsEnable_Type.__name__=_E
_FsBfdSessNotificationsEnable_Object=MibScalar
fsBfdSessNotificationsEnable=_FsBfdSessNotificationsEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,1,2),_FsBfdSessNotificationsEnable_Type())
fsBfdSessNotificationsEnable.setMaxAccess(_X)
if mibBuilder.loadTexts:fsBfdSessNotificationsEnable.setStatus(_A)
_FsBfdSessTable_Object=MibTable
fsBfdSessTable=_FsBfdSessTable_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2))
if mibBuilder.loadTexts:fsBfdSessTable.setStatus(_A)
_FsBfdSessEntry_Object=MibTableRow
fsBfdSessEntry=_FsBfdSessEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1))
fsBfdSessEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:fsBfdSessEntry.setStatus(_A)
_FsBfdSessIndex_Type=FSBfdSessIndexTC
_FsBfdSessIndex_Object=MibTableColumn
fsBfdSessIndex=_FsBfdSessIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,1),_FsBfdSessIndex_Type())
fsBfdSessIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsBfdSessIndex.setStatus(_A)
class _FsBfdSessVersionNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsBfdSessVersionNumber_Type.__name__=_G
_FsBfdSessVersionNumber_Object=MibTableColumn
fsBfdSessVersionNumber=_FsBfdSessVersionNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,2),_FsBfdSessVersionNumber_Type())
fsBfdSessVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessVersionNumber.setStatus(_A)
_FsBfdSessType_Type=FSBfdSessTypeTC
_FsBfdSessType_Object=MibTableColumn
fsBfdSessType=_FsBfdSessType_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,3),_FsBfdSessType_Type())
fsBfdSessType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessType.setStatus(_A)
class _FsBfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsBfdSessDiscriminator_Type.__name__=_G
_FsBfdSessDiscriminator_Object=MibTableColumn
fsBfdSessDiscriminator=_FsBfdSessDiscriminator_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,4),_FsBfdSessDiscriminator_Type())
fsBfdSessDiscriminator.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessDiscriminator.setStatus(_A)
class _FsBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_FsBfdSessRemoteDiscr_Type.__name__=_G
_FsBfdSessRemoteDiscr_Object=MibTableColumn
fsBfdSessRemoteDiscr=_FsBfdSessRemoteDiscr_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,5),_FsBfdSessRemoteDiscr_Type())
fsBfdSessRemoteDiscr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessRemoteDiscr.setStatus(_A)
class _FsBfdSessDestinationUdpPort_Type(FSBfdCtrlDestPortNumberTC):defaultValue=0
_FsBfdSessDestinationUdpPort_Type.__name__=_Z
_FsBfdSessDestinationUdpPort_Object=MibTableColumn
fsBfdSessDestinationUdpPort=_FsBfdSessDestinationUdpPort_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,6),_FsBfdSessDestinationUdpPort_Type())
fsBfdSessDestinationUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessDestinationUdpPort.setStatus(_A)
class _FsBfdSessSourceUdpPort_Type(FSBfdCtrlSourcePortNumberTC):defaultValue=0
_FsBfdSessSourceUdpPort_Type.__name__=_a
_FsBfdSessSourceUdpPort_Object=MibTableColumn
fsBfdSessSourceUdpPort=_FsBfdSessSourceUdpPort_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,7),_FsBfdSessSourceUdpPort_Type())
fsBfdSessSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessSourceUdpPort.setStatus(_A)
class _FsBfdSessEchoSourceUdpPort_Type(InetPortNumber):defaultValue=0
_FsBfdSessEchoSourceUdpPort_Type.__name__=_W
_FsBfdSessEchoSourceUdpPort_Object=MibTableColumn
fsBfdSessEchoSourceUdpPort=_FsBfdSessEchoSourceUdpPort_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,8),_FsBfdSessEchoSourceUdpPort_Type())
fsBfdSessEchoSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessEchoSourceUdpPort.setStatus(_A)
class _FsBfdSessAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_FsBfdSessAdminStatus_Type.__name__=_I
_FsBfdSessAdminStatus_Object=MibTableColumn
fsBfdSessAdminStatus=_FsBfdSessAdminStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,9),_FsBfdSessAdminStatus_Type())
fsBfdSessAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessAdminStatus.setStatus(_A)
class _FsBfdSessState_Type(FSBfdSessStateTC):defaultValue=2
_FsBfdSessState_Type.__name__=_b
_FsBfdSessState_Object=MibTableColumn
fsBfdSessState=_FsBfdSessState_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,10),_FsBfdSessState_Type())
fsBfdSessState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessState.setStatus(_A)
class _FsBfdSessRemoteHeardFlag_Type(TruthValue):defaultValue=2
_FsBfdSessRemoteHeardFlag_Type.__name__=_E
_FsBfdSessRemoteHeardFlag_Object=MibTableColumn
fsBfdSessRemoteHeardFlag=_FsBfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,11),_FsBfdSessRemoteHeardFlag_Type())
fsBfdSessRemoteHeardFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessRemoteHeardFlag.setStatus(_A)
_FsBfdSessDiag_Type=FSBfdDiagTC
_FsBfdSessDiag_Object=MibTableColumn
fsBfdSessDiag=_FsBfdSessDiag_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,12),_FsBfdSessDiag_Type())
fsBfdSessDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessDiag.setStatus(_A)
_FsBfdSessOperMode_Type=FSBfdSessOperModeTC
_FsBfdSessOperMode_Object=MibTableColumn
fsBfdSessOperMode=_FsBfdSessOperMode_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,13),_FsBfdSessOperMode_Type())
fsBfdSessOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessOperMode.setStatus(_A)
class _FsBfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_FsBfdSessDemandModeDesiredFlag_Type.__name__=_E
_FsBfdSessDemandModeDesiredFlag_Object=MibTableColumn
fsBfdSessDemandModeDesiredFlag=_FsBfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,14),_FsBfdSessDemandModeDesiredFlag_Type())
fsBfdSessDemandModeDesiredFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessDemandModeDesiredFlag.setStatus(_A)
class _FsBfdSessControlPlaneIndepFlag_Type(TruthValue):defaultValue=2
_FsBfdSessControlPlaneIndepFlag_Type.__name__=_E
_FsBfdSessControlPlaneIndepFlag_Object=MibTableColumn
fsBfdSessControlPlaneIndepFlag=_FsBfdSessControlPlaneIndepFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,15),_FsBfdSessControlPlaneIndepFlag_Type())
fsBfdSessControlPlaneIndepFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessControlPlaneIndepFlag.setStatus(_A)
class _FsBfdSessMultipointFlag_Type(TruthValue):defaultValue=2
_FsBfdSessMultipointFlag_Type.__name__=_E
_FsBfdSessMultipointFlag_Object=MibTableColumn
fsBfdSessMultipointFlag=_FsBfdSessMultipointFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,16),_FsBfdSessMultipointFlag_Type())
fsBfdSessMultipointFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessMultipointFlag.setStatus(_A)
_FsBfdSessInterface_Type=InterfaceIndexOrZero
_FsBfdSessInterface_Object=MibTableColumn
fsBfdSessInterface=_FsBfdSessInterface_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,17),_FsBfdSessInterface_Type())
fsBfdSessInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessInterface.setStatus(_A)
_FsBfdSessSrcAddrType_Type=InetAddressType
_FsBfdSessSrcAddrType_Object=MibTableColumn
fsBfdSessSrcAddrType=_FsBfdSessSrcAddrType_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,18),_FsBfdSessSrcAddrType_Type())
fsBfdSessSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessSrcAddrType.setStatus(_A)
_FsBfdSessSrcAddr_Type=InetAddress
_FsBfdSessSrcAddr_Object=MibTableColumn
fsBfdSessSrcAddr=_FsBfdSessSrcAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,19),_FsBfdSessSrcAddr_Type())
fsBfdSessSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessSrcAddr.setStatus(_A)
_FsBfdSessDstAddrType_Type=InetAddressType
_FsBfdSessDstAddrType_Object=MibTableColumn
fsBfdSessDstAddrType=_FsBfdSessDstAddrType_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,20),_FsBfdSessDstAddrType_Type())
fsBfdSessDstAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessDstAddrType.setStatus(_A)
_FsBfdSessDstAddr_Type=InetAddress
_FsBfdSessDstAddr_Object=MibTableColumn
fsBfdSessDstAddr=_FsBfdSessDstAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,21),_FsBfdSessDstAddr_Type())
fsBfdSessDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessDstAddr.setStatus(_A)
class _FsBfdSessGTSM_Type(TruthValue):defaultValue=2
_FsBfdSessGTSM_Type.__name__=_E
_FsBfdSessGTSM_Object=MibTableColumn
fsBfdSessGTSM=_FsBfdSessGTSM_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,22),_FsBfdSessGTSM_Type())
fsBfdSessGTSM.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessGTSM.setStatus(_A)
class _FsBfdSessGTSMTTL_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsBfdSessGTSMTTL_Type.__name__=_G
_FsBfdSessGTSMTTL_Object=MibTableColumn
fsBfdSessGTSMTTL=_FsBfdSessGTSMTTL_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,23),_FsBfdSessGTSMTTL_Type())
fsBfdSessGTSMTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessGTSMTTL.setStatus(_A)
_FsBfdSessDesiredMinTxInterval_Type=FSBfdIntervalTC
_FsBfdSessDesiredMinTxInterval_Object=MibTableColumn
fsBfdSessDesiredMinTxInterval=_FsBfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,24),_FsBfdSessDesiredMinTxInterval_Type())
fsBfdSessDesiredMinTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessDesiredMinTxInterval.setStatus(_A)
_FsBfdSessReqMinRxInterval_Type=FSBfdIntervalTC
_FsBfdSessReqMinRxInterval_Object=MibTableColumn
fsBfdSessReqMinRxInterval=_FsBfdSessReqMinRxInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,25),_FsBfdSessReqMinRxInterval_Type())
fsBfdSessReqMinRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessReqMinRxInterval.setStatus(_A)
_FsBfdSessReqMinEchoRxInterval_Type=FSBfdIntervalTC
_FsBfdSessReqMinEchoRxInterval_Object=MibTableColumn
fsBfdSessReqMinEchoRxInterval=_FsBfdSessReqMinEchoRxInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,26),_FsBfdSessReqMinEchoRxInterval_Type())
fsBfdSessReqMinEchoRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessReqMinEchoRxInterval.setStatus(_A)
_FsBfdSessDetectMult_Type=FSBfdMultiplierTC
_FsBfdSessDetectMult_Object=MibTableColumn
fsBfdSessDetectMult=_FsBfdSessDetectMult_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,27),_FsBfdSessDetectMult_Type())
fsBfdSessDetectMult.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessDetectMult.setStatus(_A)
_FsBfdSessNegotiatedInterval_Type=FSBfdIntervalTC
_FsBfdSessNegotiatedInterval_Object=MibTableColumn
fsBfdSessNegotiatedInterval=_FsBfdSessNegotiatedInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,28),_FsBfdSessNegotiatedInterval_Type())
fsBfdSessNegotiatedInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessNegotiatedInterval.setStatus(_A)
_FsBfdSessNegotiatedEchoInterval_Type=FSBfdIntervalTC
_FsBfdSessNegotiatedEchoInterval_Object=MibTableColumn
fsBfdSessNegotiatedEchoInterval=_FsBfdSessNegotiatedEchoInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,29),_FsBfdSessNegotiatedEchoInterval_Type())
fsBfdSessNegotiatedEchoInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessNegotiatedEchoInterval.setStatus(_A)
_FsBfdSessNegotiatedDetectMult_Type=FSBfdMultiplierTC
_FsBfdSessNegotiatedDetectMult_Object=MibTableColumn
fsBfdSessNegotiatedDetectMult=_FsBfdSessNegotiatedDetectMult_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,30),_FsBfdSessNegotiatedDetectMult_Type())
fsBfdSessNegotiatedDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessNegotiatedDetectMult.setStatus(_A)
class _FsBfdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_FsBfdSessAuthPresFlag_Type.__name__=_E
_FsBfdSessAuthPresFlag_Object=MibTableColumn
fsBfdSessAuthPresFlag=_FsBfdSessAuthPresFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,31),_FsBfdSessAuthPresFlag_Type())
fsBfdSessAuthPresFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessAuthPresFlag.setStatus(_A)
class _FsBfdSessAuthenticationType_Type(FSBfdSessAuthenticationTypeTC):defaultValue=-1
_FsBfdSessAuthenticationType_Type.__name__=_c
_FsBfdSessAuthenticationType_Object=MibTableColumn
fsBfdSessAuthenticationType=_FsBfdSessAuthenticationType_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,32),_FsBfdSessAuthenticationType_Type())
fsBfdSessAuthenticationType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessAuthenticationType.setStatus(_A)
class _FsBfdSessAuthenticationKeyID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_FsBfdSessAuthenticationKeyID_Type.__name__=_I
_FsBfdSessAuthenticationKeyID_Object=MibTableColumn
fsBfdSessAuthenticationKeyID=_FsBfdSessAuthenticationKeyID_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,33),_FsBfdSessAuthenticationKeyID_Type())
fsBfdSessAuthenticationKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessAuthenticationKeyID.setStatus(_A)
_FsBfdSessAuthenticationKey_Type=FSBfdSessionAuthenticationKeyTC
_FsBfdSessAuthenticationKey_Object=MibTableColumn
fsBfdSessAuthenticationKey=_FsBfdSessAuthenticationKey_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,34),_FsBfdSessAuthenticationKey_Type())
fsBfdSessAuthenticationKey.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessAuthenticationKey.setStatus(_A)
_FsBfdSessStorageType_Type=StorageType
_FsBfdSessStorageType_Object=MibTableColumn
fsBfdSessStorageType=_FsBfdSessStorageType_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,35),_FsBfdSessStorageType_Type())
fsBfdSessStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessStorageType.setStatus(_A)
_FsBfdSessRowStatus_Type=RowStatus
_FsBfdSessRowStatus_Object=MibTableColumn
fsBfdSessRowStatus=_FsBfdSessRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,36),_FsBfdSessRowStatus_Type())
fsBfdSessRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessRowStatus.setStatus(_A)
class _FsBfdSessIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsBfdSessIfName_Type.__name__=_J
_FsBfdSessIfName_Object=MibTableColumn
fsBfdSessIfName=_FsBfdSessIfName_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,37),_FsBfdSessIfName_Type())
fsBfdSessIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessIfName.setStatus(_A)
class _FsBfdSessIfDes_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsBfdSessIfDes_Type.__name__=_J
_FsBfdSessIfDes_Object=MibTableColumn
fsBfdSessIfDes=_FsBfdSessIfDes_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,2,1,38),_FsBfdSessIfDes_Type())
fsBfdSessIfDes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessIfDes.setStatus(_A)
_FsBfdSessPerfTable_Object=MibTable
fsBfdSessPerfTable=_FsBfdSessPerfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3))
if mibBuilder.loadTexts:fsBfdSessPerfTable.setStatus(_A)
_FsBfdSessPerfEntry_Object=MibTableRow
fsBfdSessPerfEntry=_FsBfdSessPerfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1))
if mibBuilder.loadTexts:fsBfdSessPerfEntry.setStatus(_A)
_FsBfdSessPerfCtrlPktIn_Type=Counter32
_FsBfdSessPerfCtrlPktIn_Object=MibTableColumn
fsBfdSessPerfCtrlPktIn=_FsBfdSessPerfCtrlPktIn_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,1),_FsBfdSessPerfCtrlPktIn_Type())
fsBfdSessPerfCtrlPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfCtrlPktIn.setStatus(_A)
_FsBfdSessPerfCtrlPktOut_Type=Counter32
_FsBfdSessPerfCtrlPktOut_Object=MibTableColumn
fsBfdSessPerfCtrlPktOut=_FsBfdSessPerfCtrlPktOut_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,2),_FsBfdSessPerfCtrlPktOut_Type())
fsBfdSessPerfCtrlPktOut.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfCtrlPktOut.setStatus(_A)
_FsBfdSessPerfCtrlPktDrop_Type=Counter32
_FsBfdSessPerfCtrlPktDrop_Object=MibTableColumn
fsBfdSessPerfCtrlPktDrop=_FsBfdSessPerfCtrlPktDrop_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,3),_FsBfdSessPerfCtrlPktDrop_Type())
fsBfdSessPerfCtrlPktDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfCtrlPktDrop.setStatus(_A)
_FsBfdSessPerfCtrlPktDropLastTime_Type=TimeStamp
_FsBfdSessPerfCtrlPktDropLastTime_Object=MibTableColumn
fsBfdSessPerfCtrlPktDropLastTime=_FsBfdSessPerfCtrlPktDropLastTime_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,4),_FsBfdSessPerfCtrlPktDropLastTime_Type())
fsBfdSessPerfCtrlPktDropLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfCtrlPktDropLastTime.setStatus(_A)
_FsBfdSessPerfEchoPktIn_Type=Counter32
_FsBfdSessPerfEchoPktIn_Object=MibTableColumn
fsBfdSessPerfEchoPktIn=_FsBfdSessPerfEchoPktIn_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,5),_FsBfdSessPerfEchoPktIn_Type())
fsBfdSessPerfEchoPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfEchoPktIn.setStatus(_A)
_FsBfdSessPerfEchoPktOut_Type=Counter32
_FsBfdSessPerfEchoPktOut_Object=MibTableColumn
fsBfdSessPerfEchoPktOut=_FsBfdSessPerfEchoPktOut_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,6),_FsBfdSessPerfEchoPktOut_Type())
fsBfdSessPerfEchoPktOut.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfEchoPktOut.setStatus(_A)
_FsBfdSessPerfEchoPktDrop_Type=Counter32
_FsBfdSessPerfEchoPktDrop_Object=MibTableColumn
fsBfdSessPerfEchoPktDrop=_FsBfdSessPerfEchoPktDrop_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,7),_FsBfdSessPerfEchoPktDrop_Type())
fsBfdSessPerfEchoPktDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfEchoPktDrop.setStatus(_A)
_FsBfdSessPerfEchoPktDropLastTime_Type=TimeStamp
_FsBfdSessPerfEchoPktDropLastTime_Object=MibTableColumn
fsBfdSessPerfEchoPktDropLastTime=_FsBfdSessPerfEchoPktDropLastTime_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,8),_FsBfdSessPerfEchoPktDropLastTime_Type())
fsBfdSessPerfEchoPktDropLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfEchoPktDropLastTime.setStatus(_A)
_FsBfdSessUpTime_Type=TimeStamp
_FsBfdSessUpTime_Object=MibTableColumn
fsBfdSessUpTime=_FsBfdSessUpTime_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,9),_FsBfdSessUpTime_Type())
fsBfdSessUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessUpTime.setStatus(_A)
_FsBfdSessPerfLastSessDownTime_Type=TimeStamp
_FsBfdSessPerfLastSessDownTime_Object=MibTableColumn
fsBfdSessPerfLastSessDownTime=_FsBfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,10),_FsBfdSessPerfLastSessDownTime_Type())
fsBfdSessPerfLastSessDownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfLastSessDownTime.setStatus(_A)
_FsBfdSessPerfLastCommLostDiag_Type=FSBfdDiagTC
_FsBfdSessPerfLastCommLostDiag_Object=MibTableColumn
fsBfdSessPerfLastCommLostDiag=_FsBfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,11),_FsBfdSessPerfLastCommLostDiag_Type())
fsBfdSessPerfLastCommLostDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfLastCommLostDiag.setStatus(_A)
_FsBfdSessPerfSessUpCount_Type=Counter32
_FsBfdSessPerfSessUpCount_Object=MibTableColumn
fsBfdSessPerfSessUpCount=_FsBfdSessPerfSessUpCount_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,12),_FsBfdSessPerfSessUpCount_Type())
fsBfdSessPerfSessUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfSessUpCount.setStatus(_A)
_FsBfdSessPerfDiscTime_Type=TimeStamp
_FsBfdSessPerfDiscTime_Object=MibTableColumn
fsBfdSessPerfDiscTime=_FsBfdSessPerfDiscTime_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,13),_FsBfdSessPerfDiscTime_Type())
fsBfdSessPerfDiscTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfDiscTime.setStatus(_A)
_FsBfdSessPerfCtrlPktInHC_Type=Counter64
_FsBfdSessPerfCtrlPktInHC_Object=MibTableColumn
fsBfdSessPerfCtrlPktInHC=_FsBfdSessPerfCtrlPktInHC_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,14),_FsBfdSessPerfCtrlPktInHC_Type())
fsBfdSessPerfCtrlPktInHC.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfCtrlPktInHC.setStatus(_A)
_FsBfdSessPerfCtrlPktOutHC_Type=Counter64
_FsBfdSessPerfCtrlPktOutHC_Object=MibTableColumn
fsBfdSessPerfCtrlPktOutHC=_FsBfdSessPerfCtrlPktOutHC_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,15),_FsBfdSessPerfCtrlPktOutHC_Type())
fsBfdSessPerfCtrlPktOutHC.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfCtrlPktOutHC.setStatus(_A)
_FsBfdSessPerfCtrlPktDropHC_Type=Counter64
_FsBfdSessPerfCtrlPktDropHC_Object=MibTableColumn
fsBfdSessPerfCtrlPktDropHC=_FsBfdSessPerfCtrlPktDropHC_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,16),_FsBfdSessPerfCtrlPktDropHC_Type())
fsBfdSessPerfCtrlPktDropHC.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfCtrlPktDropHC.setStatus(_A)
_FsBfdSessPerfEchoPktInHC_Type=Counter64
_FsBfdSessPerfEchoPktInHC_Object=MibTableColumn
fsBfdSessPerfEchoPktInHC=_FsBfdSessPerfEchoPktInHC_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,17),_FsBfdSessPerfEchoPktInHC_Type())
fsBfdSessPerfEchoPktInHC.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfEchoPktInHC.setStatus(_A)
_FsBfdSessPerfEchoPktOutHC_Type=Counter64
_FsBfdSessPerfEchoPktOutHC_Object=MibTableColumn
fsBfdSessPerfEchoPktOutHC=_FsBfdSessPerfEchoPktOutHC_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,18),_FsBfdSessPerfEchoPktOutHC_Type())
fsBfdSessPerfEchoPktOutHC.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfEchoPktOutHC.setStatus(_A)
_FsBfdSessPerfEchoPktDropHC_Type=Counter64
_FsBfdSessPerfEchoPktDropHC_Object=MibTableColumn
fsBfdSessPerfEchoPktDropHC=_FsBfdSessPerfEchoPktDropHC_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,3,1,19),_FsBfdSessPerfEchoPktDropHC_Type())
fsBfdSessPerfEchoPktDropHC.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessPerfEchoPktDropHC.setStatus(_A)
_FsBfdSessDiscMapTable_Object=MibTable
fsBfdSessDiscMapTable=_FsBfdSessDiscMapTable_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,4))
if mibBuilder.loadTexts:fsBfdSessDiscMapTable.setStatus(_A)
_FsBfdSessDiscMapEntry_Object=MibTableRow
fsBfdSessDiscMapEntry=_FsBfdSessDiscMapEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,4,1))
fsBfdSessDiscMapEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsBfdSessDiscMapEntry.setStatus(_A)
_FsBfdSessDiscMapIndex_Type=FSBfdSessIndexTC
_FsBfdSessDiscMapIndex_Object=MibTableColumn
fsBfdSessDiscMapIndex=_FsBfdSessDiscMapIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,4,1,1),_FsBfdSessDiscMapIndex_Type())
fsBfdSessDiscMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessDiscMapIndex.setStatus(_A)
_FsBfdSessDiscMapStorageType_Type=StorageType
_FsBfdSessDiscMapStorageType_Object=MibTableColumn
fsBfdSessDiscMapStorageType=_FsBfdSessDiscMapStorageType_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,4,1,2),_FsBfdSessDiscMapStorageType_Type())
fsBfdSessDiscMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessDiscMapStorageType.setStatus(_A)
_FsBfdSessDiscMapRowStatus_Type=RowStatus
_FsBfdSessDiscMapRowStatus_Object=MibTableColumn
fsBfdSessDiscMapRowStatus=_FsBfdSessDiscMapRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,4,1,3),_FsBfdSessDiscMapRowStatus_Type())
fsBfdSessDiscMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessDiscMapRowStatus.setStatus(_A)
_FsBfdSessIpMapTable_Object=MibTable
fsBfdSessIpMapTable=_FsBfdSessIpMapTable_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,5))
if mibBuilder.loadTexts:fsBfdSessIpMapTable.setStatus(_A)
_FsBfdSessIpMapEntry_Object=MibTableRow
fsBfdSessIpMapEntry=_FsBfdSessIpMapEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,5,1))
fsBfdSessIpMapEntry.setIndexNames((0,_B,_H),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:fsBfdSessIpMapEntry.setStatus(_A)
_FsBfdSessIpMapIndex_Type=FSBfdSessIndexTC
_FsBfdSessIpMapIndex_Object=MibTableColumn
fsBfdSessIpMapIndex=_FsBfdSessIpMapIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,5,1,1),_FsBfdSessIpMapIndex_Type())
fsBfdSessIpMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsBfdSessIpMapIndex.setStatus(_A)
_FsBfdSessIpMapStorageType_Type=StorageType
_FsBfdSessIpMapStorageType_Object=MibTableColumn
fsBfdSessIpMapStorageType=_FsBfdSessIpMapStorageType_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,5,1,2),_FsBfdSessIpMapStorageType_Type())
fsBfdSessIpMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessIpMapStorageType.setStatus(_A)
_FsBfdSessIpMapRowStatus_Type=RowStatus
_FsBfdSessIpMapRowStatus_Object=MibTableColumn
fsBfdSessIpMapRowStatus=_FsBfdSessIpMapRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,48,1,5,1,3),_FsBfdSessIpMapRowStatus_Type())
fsBfdSessIpMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBfdSessIpMapRowStatus.setStatus(_A)
_FsBfdConformance_ObjectIdentity=ObjectIdentity
fsBfdConformance=_FsBfdConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,48,2))
_FsBfdGroups_ObjectIdentity=ObjectIdentity
fsBfdGroups=_FsBfdGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,48,2,1))
_FsBfdCompliances_ObjectIdentity=ObjectIdentity
fsBfdCompliances=_FsBfdCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,48,2,2))
fsBfdSessEntry.registerAugmentions((_B,_d))
fsBfdSessPerfEntry.setIndexNames(*fsBfdSessEntry.getIndexNames())
fsBfdSessionGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,48,2,1,1))
fsBfdSessionGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_H),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:fsBfdSessionGroup.setStatus(_A)
fsBfdSessionReadOnlyGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,48,2,1,2))
fsBfdSessionReadOnlyGroup.setObjects(*((_B,_K),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_F),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:fsBfdSessionReadOnlyGroup.setStatus(_A)
fsBfdSessionPerfGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,48,2,1,3))
fsBfdSessionPerfGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:fsBfdSessionPerfGroup.setStatus(_A)
fsBfdSessionPerfHCGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,48,2,1,4))
fsBfdSessionPerfHCGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:fsBfdSessionPerfHCGroup.setStatus(_A)
fsBfdSessUp=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,48,0,1))
fsBfdSessUp.setObjects(*((_B,_F),(_B,_F),(_B,_H),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:fsBfdSessUp.setStatus(_A)
fsBfdSessDown=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,48,0,2))
fsBfdSessDown.setObjects(*((_B,_F),(_B,_F),(_B,_H),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:fsBfdSessDown.setStatus(_A)
fsBfdNotificationGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,48,2,1,5))
fsBfdNotificationGroup.setObjects(*((_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:fsBfdNotificationGroup.setStatus(_A)
fsBfdModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,48,2,2,1))
fsBfdModuleFullCompliance.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsBfdModuleFullCompliance.setStatus(_A)
fsBfdModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,48,2,2,2))
fsBfdModuleReadOnlyCompliance.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsBfdModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FSBfdSessIndexTC':FSBfdSessIndexTC,'FSBfdIntervalTC':FSBfdIntervalTC,'FSBfdMultiplierTC':FSBfdMultiplierTC,'FSBfdDiagTC':FSBfdDiagTC,'FSBfdSessTypeTC':FSBfdSessTypeTC,'FSBfdSessOperModeTC':FSBfdSessOperModeTC,_Z:FSBfdCtrlDestPortNumberTC,_a:FSBfdCtrlSourcePortNumberTC,_b:FSBfdSessStateTC,_c:FSBfdSessAuthenticationTypeTC,'FSBfdSessionAuthenticationKeyTC':FSBfdSessionAuthenticationKeyTC,'fsBfdMIB':fsBfdMIB,'fsBfdNotifications':fsBfdNotifications,_AX:fsBfdSessUp,_AY:fsBfdSessDown,'fsBfdObjects':fsBfdObjects,'fsBfdScalarObjects':fsBfdScalarObjects,_e:fsBfdAdminStatus,_f:fsBfdSessNotificationsEnable,'fsBfdSessTable':fsBfdSessTable,'fsBfdSessEntry':fsBfdSessEntry,_Y:fsBfdSessIndex,_g:fsBfdSessVersionNumber,_h:fsBfdSessType,_K:fsBfdSessDiscriminator,_A6:fsBfdSessRemoteDiscr,_i:fsBfdSessDestinationUdpPort,_j:fsBfdSessSourceUdpPort,_k:fsBfdSessEchoSourceUdpPort,_l:fsBfdSessAdminStatus,_A7:fsBfdSessState,_A8:fsBfdSessRemoteHeardFlag,_F:fsBfdSessDiag,_m:fsBfdSessOperMode,_n:fsBfdSessDemandModeDesiredFlag,_o:fsBfdSessControlPlaneIndepFlag,_p:fsBfdSessMultipointFlag,_H:fsBfdSessInterface,_L:fsBfdSessSrcAddrType,_M:fsBfdSessSrcAddr,_N:fsBfdSessDstAddrType,_O:fsBfdSessDstAddr,_q:fsBfdSessGTSM,_r:fsBfdSessGTSMTTL,_s:fsBfdSessDesiredMinTxInterval,_t:fsBfdSessReqMinRxInterval,_u:fsBfdSessReqMinEchoRxInterval,_v:fsBfdSessDetectMult,_A9:fsBfdSessNegotiatedInterval,_AA:fsBfdSessNegotiatedEchoInterval,_AB:fsBfdSessNegotiatedDetectMult,_w:fsBfdSessAuthPresFlag,_x:fsBfdSessAuthenticationType,_y:fsBfdSessAuthenticationKeyID,_z:fsBfdSessAuthenticationKey,_A0:fsBfdSessStorageType,_A1:fsBfdSessRowStatus,_P:fsBfdSessIfName,_Q:fsBfdSessIfDes,'fsBfdSessPerfTable':fsBfdSessPerfTable,_d:fsBfdSessPerfEntry,_AE:fsBfdSessPerfCtrlPktIn,_AF:fsBfdSessPerfCtrlPktOut,_AG:fsBfdSessPerfCtrlPktDrop,_AH:fsBfdSessPerfCtrlPktDropLastTime,_AI:fsBfdSessPerfEchoPktIn,_AJ:fsBfdSessPerfEchoPktOut,_AK:fsBfdSessPerfEchoPktDrop,_AL:fsBfdSessPerfEchoPktDropLastTime,_AM:fsBfdSessUpTime,_AN:fsBfdSessPerfLastSessDownTime,_AO:fsBfdSessPerfLastCommLostDiag,_AP:fsBfdSessPerfSessUpCount,_AQ:fsBfdSessPerfDiscTime,_AR:fsBfdSessPerfCtrlPktInHC,_AS:fsBfdSessPerfCtrlPktOutHC,_AT:fsBfdSessPerfCtrlPktDropHC,_AU:fsBfdSessPerfEchoPktInHC,_AV:fsBfdSessPerfEchoPktOutHC,_AW:fsBfdSessPerfEchoPktDropHC,'fsBfdSessDiscMapTable':fsBfdSessDiscMapTable,'fsBfdSessDiscMapEntry':fsBfdSessDiscMapEntry,_AC:fsBfdSessDiscMapIndex,_A2:fsBfdSessDiscMapStorageType,_A3:fsBfdSessDiscMapRowStatus,'fsBfdSessIpMapTable':fsBfdSessIpMapTable,'fsBfdSessIpMapEntry':fsBfdSessIpMapEntry,_AD:fsBfdSessIpMapIndex,_A4:fsBfdSessIpMapStorageType,_A5:fsBfdSessIpMapRowStatus,'fsBfdConformance':fsBfdConformance,'fsBfdGroups':fsBfdGroups,_R:fsBfdSessionGroup,_S:fsBfdSessionReadOnlyGroup,_T:fsBfdSessionPerfGroup,_V:fsBfdSessionPerfHCGroup,_U:fsBfdNotificationGroup,'fsBfdCompliances':fsBfdCompliances,'fsBfdModuleFullCompliance':fsBfdModuleFullCompliance,'fsBfdModuleReadOnlyCompliance':fsBfdModuleReadOnlyCompliance})