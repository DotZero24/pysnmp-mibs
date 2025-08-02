_AV='qtechBfdSessDown'
_AU='qtechBfdSessUp'
_AT='qtechBfdSessPerfEchoPktDropHC'
_AS='qtechBfdSessPerfEchoPktOutHC'
_AR='qtechBfdSessPerfEchoPktInHC'
_AQ='qtechBfdSessPerfCtrlPktDropHC'
_AP='qtechBfdSessPerfCtrlPktOutHC'
_AO='qtechBfdSessPerfCtrlPktInHC'
_AN='qtechBfdSessPerfDiscTime'
_AM='qtechBfdSessPerfSessUpCount'
_AL='qtechBfdSessPerfLastCommLostDiag'
_AK='qtechBfdSessPerfLastSessDownTime'
_AJ='qtechBfdSessUpTime'
_AI='qtechBfdSessPerfEchoPktDropLastTime'
_AH='qtechBfdSessPerfEchoPktDrop'
_AG='qtechBfdSessPerfEchoPktOut'
_AF='qtechBfdSessPerfEchoPktIn'
_AE='qtechBfdSessPerfCtrlPktDropLastTime'
_AD='qtechBfdSessPerfCtrlPktDrop'
_AC='qtechBfdSessPerfCtrlPktOut'
_AB='qtechBfdSessPerfCtrlPktIn'
_AA='qtechBfdSessIpMapIndex'
_A9='qtechBfdSessDiscMapIndex'
_A8='qtechBfdSessNegotiatedDetectMult'
_A7='qtechBfdSessNegotiatedEchoInterval'
_A6='qtechBfdSessNegotiatedInterval'
_A5='qtechBfdSessRemoteHeardFlag'
_A4='qtechBfdSessState'
_A3='qtechBfdSessRemoteDiscr'
_A2='qtechBfdSessIpMapRowStatus'
_A1='qtechBfdSessIpMapStorageType'
_A0='qtechBfdSessDiscMapRowStatus'
_z='qtechBfdSessDiscMapStorageType'
_y='qtechBfdSessRowStatus'
_x='qtechBfdSessStorageType'
_w='qtechBfdSessAuthenticationKey'
_v='qtechBfdSessAuthenticationKeyID'
_u='qtechBfdSessAuthenticationType'
_t='qtechBfdSessAuthPresFlag'
_s='qtechBfdSessDetectMult'
_r='qtechBfdSessReqMinEchoRxInterval'
_q='qtechBfdSessReqMinRxInterval'
_p='qtechBfdSessDesiredMinTxInterval'
_o='qtechBfdSessGTSMTTL'
_n='qtechBfdSessGTSM'
_m='qtechBfdSessMultipointFlag'
_l='qtechBfdSessControlPlaneIndepFlag'
_k='qtechBfdSessDemandModeDesiredFlag'
_j='qtechBfdSessOperMode'
_i='qtechBfdSessAdminStatus'
_h='qtechBfdSessEchoSourceUdpPort'
_g='qtechBfdSessSourceUdpPort'
_f='qtechBfdSessDestinationUdpPort'
_e='qtechBfdSessType'
_d='qtechBfdSessVersionNumber'
_c='qtechBfdSessNotificationsEnable'
_b='qtechBfdAdminStatus'
_a='qtechBfdSessPerfEntry'
_Z='QtechBfdSessAuthenticationTypeTC'
_Y='QtechBfdSessStateTC'
_X='QtechBfdCtrlSourcePortNumberTC'
_W='QtechBfdCtrlDestPortNumberTC'
_V='qtechBfdSessIndex'
_U='read-write'
_T='InetPortNumber'
_S='qtechBfdSessionPerfHCGroup'
_R='qtechBfdNotificationGroup'
_Q='qtechBfdSessionPerfGroup'
_P='qtechBfdSessionReadOnlyGroup'
_O='qtechBfdSessionGroup'
_N='qtechBfdSessDstAddr'
_M='qtechBfdSessDstAddrType'
_L='qtechBfdSessSrcAddr'
_K='qtechBfdSessSrcAddrType'
_J='qtechBfdSessInterface'
_I='qtechBfdSessDiscriminator'
_H='Integer32'
_G='Unsigned32'
_F='qtechBfdSessDiag'
_E='TruthValue'
_D='read-only'
_C='read-create'
_B='QTECH-BFD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_T)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_E)
qtechBfdMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,48))
if mibBuilder.loadTexts:qtechBfdMIB.setRevisions(('2012-04-14 12:00',))
class QtechBfdSessIndexTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class QtechBfdIntervalTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class QtechBfdMultiplierTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class QtechBfdDiagTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noDiagnostic',0),('controlDetectionTimeExpired',1),('echoFunctionFailed',2),('neighborSignaledSessionDown',3),('forwardingPlaneReset',4),('pathDown',5),('concatenatedPathDown',6),('administrativelyDown',7),('reverseConcatenatedPathDown',8)))
class QtechBfdSessTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('singleHop',1),('multiHopTotallyArbitraryPaths',2),('multiHopOutOfBandSignaling',3),('multiHopUnidirectionalLinks',4),('multiPointHead',5),('multiPointTail',6)))
class QtechBfdSessOperModeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asyncModeWEchoFunction',1),('asynchModeWOEchoFunction',2),('demandModeWEchoFunction',3),('demandModeWOEchoFunction',4)))
class QtechBfdCtrlDestPortNumberTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class QtechBfdCtrlSourcePortNumberTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class QtechBfdSessStateTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4),('failing',5)))
class QtechBfdSessAuthenticationTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5)));namedValues=NamedValues(*(('noAuthentication',-1),('reserved',0),('simplePassword',1),('keyedMD5',2),('meticulousKeyedMD5',3),('keyedSHA1',4),('meticulousKeyedSHA1',5)))
class QtechBfdSessionAuthenticationKeyTC(TextualConvention,OctetString):status=_A;displayHint='1x ';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,252))
_QtechBfdNotifications_ObjectIdentity=ObjectIdentity
qtechBfdNotifications=_QtechBfdNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,48,0))
_QtechBfdObjects_ObjectIdentity=ObjectIdentity
qtechBfdObjects=_QtechBfdObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,48,1))
_QtechBfdScalarObjects_ObjectIdentity=ObjectIdentity
qtechBfdScalarObjects=_QtechBfdScalarObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,48,1,1))
class _QtechBfdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_QtechBfdAdminStatus_Type.__name__=_H
_QtechBfdAdminStatus_Object=MibScalar
qtechBfdAdminStatus=_QtechBfdAdminStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,1,1),_QtechBfdAdminStatus_Type())
qtechBfdAdminStatus.setMaxAccess(_U)
if mibBuilder.loadTexts:qtechBfdAdminStatus.setStatus(_A)
class _QtechBfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_QtechBfdSessNotificationsEnable_Type.__name__=_E
_QtechBfdSessNotificationsEnable_Object=MibScalar
qtechBfdSessNotificationsEnable=_QtechBfdSessNotificationsEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,1,2),_QtechBfdSessNotificationsEnable_Type())
qtechBfdSessNotificationsEnable.setMaxAccess(_U)
if mibBuilder.loadTexts:qtechBfdSessNotificationsEnable.setStatus(_A)
_QtechBfdSessTable_Object=MibTable
qtechBfdSessTable=_QtechBfdSessTable_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2))
if mibBuilder.loadTexts:qtechBfdSessTable.setStatus(_A)
_QtechBfdSessEntry_Object=MibTableRow
qtechBfdSessEntry=_QtechBfdSessEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1))
qtechBfdSessEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:qtechBfdSessEntry.setStatus(_A)
_QtechBfdSessIndex_Type=QtechBfdSessIndexTC
_QtechBfdSessIndex_Object=MibTableColumn
qtechBfdSessIndex=_QtechBfdSessIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,1),_QtechBfdSessIndex_Type())
qtechBfdSessIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechBfdSessIndex.setStatus(_A)
class _QtechBfdSessVersionNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechBfdSessVersionNumber_Type.__name__=_G
_QtechBfdSessVersionNumber_Object=MibTableColumn
qtechBfdSessVersionNumber=_QtechBfdSessVersionNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,2),_QtechBfdSessVersionNumber_Type())
qtechBfdSessVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessVersionNumber.setStatus(_A)
_QtechBfdSessType_Type=QtechBfdSessTypeTC
_QtechBfdSessType_Object=MibTableColumn
qtechBfdSessType=_QtechBfdSessType_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,3),_QtechBfdSessType_Type())
qtechBfdSessType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessType.setStatus(_A)
class _QtechBfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_QtechBfdSessDiscriminator_Type.__name__=_G
_QtechBfdSessDiscriminator_Object=MibTableColumn
qtechBfdSessDiscriminator=_QtechBfdSessDiscriminator_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,4),_QtechBfdSessDiscriminator_Type())
qtechBfdSessDiscriminator.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessDiscriminator.setStatus(_A)
class _QtechBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_QtechBfdSessRemoteDiscr_Type.__name__=_G
_QtechBfdSessRemoteDiscr_Object=MibTableColumn
qtechBfdSessRemoteDiscr=_QtechBfdSessRemoteDiscr_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,5),_QtechBfdSessRemoteDiscr_Type())
qtechBfdSessRemoteDiscr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessRemoteDiscr.setStatus(_A)
class _QtechBfdSessDestinationUdpPort_Type(QtechBfdCtrlDestPortNumberTC):defaultValue=0
_QtechBfdSessDestinationUdpPort_Type.__name__=_W
_QtechBfdSessDestinationUdpPort_Object=MibTableColumn
qtechBfdSessDestinationUdpPort=_QtechBfdSessDestinationUdpPort_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,6),_QtechBfdSessDestinationUdpPort_Type())
qtechBfdSessDestinationUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessDestinationUdpPort.setStatus(_A)
class _QtechBfdSessSourceUdpPort_Type(QtechBfdCtrlSourcePortNumberTC):defaultValue=0
_QtechBfdSessSourceUdpPort_Type.__name__=_X
_QtechBfdSessSourceUdpPort_Object=MibTableColumn
qtechBfdSessSourceUdpPort=_QtechBfdSessSourceUdpPort_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,7),_QtechBfdSessSourceUdpPort_Type())
qtechBfdSessSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessSourceUdpPort.setStatus(_A)
class _QtechBfdSessEchoSourceUdpPort_Type(InetPortNumber):defaultValue=0
_QtechBfdSessEchoSourceUdpPort_Type.__name__=_T
_QtechBfdSessEchoSourceUdpPort_Object=MibTableColumn
qtechBfdSessEchoSourceUdpPort=_QtechBfdSessEchoSourceUdpPort_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,8),_QtechBfdSessEchoSourceUdpPort_Type())
qtechBfdSessEchoSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessEchoSourceUdpPort.setStatus(_A)
class _QtechBfdSessAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_QtechBfdSessAdminStatus_Type.__name__=_H
_QtechBfdSessAdminStatus_Object=MibTableColumn
qtechBfdSessAdminStatus=_QtechBfdSessAdminStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,9),_QtechBfdSessAdminStatus_Type())
qtechBfdSessAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessAdminStatus.setStatus(_A)
class _QtechBfdSessState_Type(QtechBfdSessStateTC):defaultValue=2
_QtechBfdSessState_Type.__name__=_Y
_QtechBfdSessState_Object=MibTableColumn
qtechBfdSessState=_QtechBfdSessState_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,10),_QtechBfdSessState_Type())
qtechBfdSessState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessState.setStatus(_A)
class _QtechBfdSessRemoteHeardFlag_Type(TruthValue):defaultValue=2
_QtechBfdSessRemoteHeardFlag_Type.__name__=_E
_QtechBfdSessRemoteHeardFlag_Object=MibTableColumn
qtechBfdSessRemoteHeardFlag=_QtechBfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,11),_QtechBfdSessRemoteHeardFlag_Type())
qtechBfdSessRemoteHeardFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessRemoteHeardFlag.setStatus(_A)
_QtechBfdSessDiag_Type=QtechBfdDiagTC
_QtechBfdSessDiag_Object=MibTableColumn
qtechBfdSessDiag=_QtechBfdSessDiag_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,12),_QtechBfdSessDiag_Type())
qtechBfdSessDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessDiag.setStatus(_A)
_QtechBfdSessOperMode_Type=QtechBfdSessOperModeTC
_QtechBfdSessOperMode_Object=MibTableColumn
qtechBfdSessOperMode=_QtechBfdSessOperMode_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,13),_QtechBfdSessOperMode_Type())
qtechBfdSessOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessOperMode.setStatus(_A)
class _QtechBfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_QtechBfdSessDemandModeDesiredFlag_Type.__name__=_E
_QtechBfdSessDemandModeDesiredFlag_Object=MibTableColumn
qtechBfdSessDemandModeDesiredFlag=_QtechBfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,14),_QtechBfdSessDemandModeDesiredFlag_Type())
qtechBfdSessDemandModeDesiredFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessDemandModeDesiredFlag.setStatus(_A)
class _QtechBfdSessControlPlaneIndepFlag_Type(TruthValue):defaultValue=2
_QtechBfdSessControlPlaneIndepFlag_Type.__name__=_E
_QtechBfdSessControlPlaneIndepFlag_Object=MibTableColumn
qtechBfdSessControlPlaneIndepFlag=_QtechBfdSessControlPlaneIndepFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,15),_QtechBfdSessControlPlaneIndepFlag_Type())
qtechBfdSessControlPlaneIndepFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessControlPlaneIndepFlag.setStatus(_A)
class _QtechBfdSessMultipointFlag_Type(TruthValue):defaultValue=2
_QtechBfdSessMultipointFlag_Type.__name__=_E
_QtechBfdSessMultipointFlag_Object=MibTableColumn
qtechBfdSessMultipointFlag=_QtechBfdSessMultipointFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,16),_QtechBfdSessMultipointFlag_Type())
qtechBfdSessMultipointFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessMultipointFlag.setStatus(_A)
_QtechBfdSessInterface_Type=InterfaceIndexOrZero
_QtechBfdSessInterface_Object=MibTableColumn
qtechBfdSessInterface=_QtechBfdSessInterface_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,17),_QtechBfdSessInterface_Type())
qtechBfdSessInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessInterface.setStatus(_A)
_QtechBfdSessSrcAddrType_Type=InetAddressType
_QtechBfdSessSrcAddrType_Object=MibTableColumn
qtechBfdSessSrcAddrType=_QtechBfdSessSrcAddrType_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,18),_QtechBfdSessSrcAddrType_Type())
qtechBfdSessSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessSrcAddrType.setStatus(_A)
_QtechBfdSessSrcAddr_Type=InetAddress
_QtechBfdSessSrcAddr_Object=MibTableColumn
qtechBfdSessSrcAddr=_QtechBfdSessSrcAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,19),_QtechBfdSessSrcAddr_Type())
qtechBfdSessSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessSrcAddr.setStatus(_A)
_QtechBfdSessDstAddrType_Type=InetAddressType
_QtechBfdSessDstAddrType_Object=MibTableColumn
qtechBfdSessDstAddrType=_QtechBfdSessDstAddrType_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,20),_QtechBfdSessDstAddrType_Type())
qtechBfdSessDstAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessDstAddrType.setStatus(_A)
_QtechBfdSessDstAddr_Type=InetAddress
_QtechBfdSessDstAddr_Object=MibTableColumn
qtechBfdSessDstAddr=_QtechBfdSessDstAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,21),_QtechBfdSessDstAddr_Type())
qtechBfdSessDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessDstAddr.setStatus(_A)
class _QtechBfdSessGTSM_Type(TruthValue):defaultValue=2
_QtechBfdSessGTSM_Type.__name__=_E
_QtechBfdSessGTSM_Object=MibTableColumn
qtechBfdSessGTSM=_QtechBfdSessGTSM_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,22),_QtechBfdSessGTSM_Type())
qtechBfdSessGTSM.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessGTSM.setStatus(_A)
class _QtechBfdSessGTSMTTL_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechBfdSessGTSMTTL_Type.__name__=_G
_QtechBfdSessGTSMTTL_Object=MibTableColumn
qtechBfdSessGTSMTTL=_QtechBfdSessGTSMTTL_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,23),_QtechBfdSessGTSMTTL_Type())
qtechBfdSessGTSMTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessGTSMTTL.setStatus(_A)
_QtechBfdSessDesiredMinTxInterval_Type=QtechBfdIntervalTC
_QtechBfdSessDesiredMinTxInterval_Object=MibTableColumn
qtechBfdSessDesiredMinTxInterval=_QtechBfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,24),_QtechBfdSessDesiredMinTxInterval_Type())
qtechBfdSessDesiredMinTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessDesiredMinTxInterval.setStatus(_A)
_QtechBfdSessReqMinRxInterval_Type=QtechBfdIntervalTC
_QtechBfdSessReqMinRxInterval_Object=MibTableColumn
qtechBfdSessReqMinRxInterval=_QtechBfdSessReqMinRxInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,25),_QtechBfdSessReqMinRxInterval_Type())
qtechBfdSessReqMinRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessReqMinRxInterval.setStatus(_A)
_QtechBfdSessReqMinEchoRxInterval_Type=QtechBfdIntervalTC
_QtechBfdSessReqMinEchoRxInterval_Object=MibTableColumn
qtechBfdSessReqMinEchoRxInterval=_QtechBfdSessReqMinEchoRxInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,26),_QtechBfdSessReqMinEchoRxInterval_Type())
qtechBfdSessReqMinEchoRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessReqMinEchoRxInterval.setStatus(_A)
_QtechBfdSessDetectMult_Type=QtechBfdMultiplierTC
_QtechBfdSessDetectMult_Object=MibTableColumn
qtechBfdSessDetectMult=_QtechBfdSessDetectMult_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,27),_QtechBfdSessDetectMult_Type())
qtechBfdSessDetectMult.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessDetectMult.setStatus(_A)
_QtechBfdSessNegotiatedInterval_Type=QtechBfdIntervalTC
_QtechBfdSessNegotiatedInterval_Object=MibTableColumn
qtechBfdSessNegotiatedInterval=_QtechBfdSessNegotiatedInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,28),_QtechBfdSessNegotiatedInterval_Type())
qtechBfdSessNegotiatedInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessNegotiatedInterval.setStatus(_A)
_QtechBfdSessNegotiatedEchoInterval_Type=QtechBfdIntervalTC
_QtechBfdSessNegotiatedEchoInterval_Object=MibTableColumn
qtechBfdSessNegotiatedEchoInterval=_QtechBfdSessNegotiatedEchoInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,29),_QtechBfdSessNegotiatedEchoInterval_Type())
qtechBfdSessNegotiatedEchoInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessNegotiatedEchoInterval.setStatus(_A)
_QtechBfdSessNegotiatedDetectMult_Type=QtechBfdMultiplierTC
_QtechBfdSessNegotiatedDetectMult_Object=MibTableColumn
qtechBfdSessNegotiatedDetectMult=_QtechBfdSessNegotiatedDetectMult_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,30),_QtechBfdSessNegotiatedDetectMult_Type())
qtechBfdSessNegotiatedDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessNegotiatedDetectMult.setStatus(_A)
class _QtechBfdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_QtechBfdSessAuthPresFlag_Type.__name__=_E
_QtechBfdSessAuthPresFlag_Object=MibTableColumn
qtechBfdSessAuthPresFlag=_QtechBfdSessAuthPresFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,31),_QtechBfdSessAuthPresFlag_Type())
qtechBfdSessAuthPresFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessAuthPresFlag.setStatus(_A)
class _QtechBfdSessAuthenticationType_Type(QtechBfdSessAuthenticationTypeTC):defaultValue=-1
_QtechBfdSessAuthenticationType_Type.__name__=_Z
_QtechBfdSessAuthenticationType_Object=MibTableColumn
qtechBfdSessAuthenticationType=_QtechBfdSessAuthenticationType_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,32),_QtechBfdSessAuthenticationType_Type())
qtechBfdSessAuthenticationType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessAuthenticationType.setStatus(_A)
class _QtechBfdSessAuthenticationKeyID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_QtechBfdSessAuthenticationKeyID_Type.__name__=_H
_QtechBfdSessAuthenticationKeyID_Object=MibTableColumn
qtechBfdSessAuthenticationKeyID=_QtechBfdSessAuthenticationKeyID_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,33),_QtechBfdSessAuthenticationKeyID_Type())
qtechBfdSessAuthenticationKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessAuthenticationKeyID.setStatus(_A)
_QtechBfdSessAuthenticationKey_Type=QtechBfdSessionAuthenticationKeyTC
_QtechBfdSessAuthenticationKey_Object=MibTableColumn
qtechBfdSessAuthenticationKey=_QtechBfdSessAuthenticationKey_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,34),_QtechBfdSessAuthenticationKey_Type())
qtechBfdSessAuthenticationKey.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessAuthenticationKey.setStatus(_A)
_QtechBfdSessStorageType_Type=StorageType
_QtechBfdSessStorageType_Object=MibTableColumn
qtechBfdSessStorageType=_QtechBfdSessStorageType_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,35),_QtechBfdSessStorageType_Type())
qtechBfdSessStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessStorageType.setStatus(_A)
_QtechBfdSessRowStatus_Type=RowStatus
_QtechBfdSessRowStatus_Object=MibTableColumn
qtechBfdSessRowStatus=_QtechBfdSessRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,2,1,36),_QtechBfdSessRowStatus_Type())
qtechBfdSessRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessRowStatus.setStatus(_A)
_QtechBfdSessPerfTable_Object=MibTable
qtechBfdSessPerfTable=_QtechBfdSessPerfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3))
if mibBuilder.loadTexts:qtechBfdSessPerfTable.setStatus(_A)
_QtechBfdSessPerfEntry_Object=MibTableRow
qtechBfdSessPerfEntry=_QtechBfdSessPerfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1))
if mibBuilder.loadTexts:qtechBfdSessPerfEntry.setStatus(_A)
_QtechBfdSessPerfCtrlPktIn_Type=Counter32
_QtechBfdSessPerfCtrlPktIn_Object=MibTableColumn
qtechBfdSessPerfCtrlPktIn=_QtechBfdSessPerfCtrlPktIn_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,1),_QtechBfdSessPerfCtrlPktIn_Type())
qtechBfdSessPerfCtrlPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfCtrlPktIn.setStatus(_A)
_QtechBfdSessPerfCtrlPktOut_Type=Counter32
_QtechBfdSessPerfCtrlPktOut_Object=MibTableColumn
qtechBfdSessPerfCtrlPktOut=_QtechBfdSessPerfCtrlPktOut_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,2),_QtechBfdSessPerfCtrlPktOut_Type())
qtechBfdSessPerfCtrlPktOut.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfCtrlPktOut.setStatus(_A)
_QtechBfdSessPerfCtrlPktDrop_Type=Counter32
_QtechBfdSessPerfCtrlPktDrop_Object=MibTableColumn
qtechBfdSessPerfCtrlPktDrop=_QtechBfdSessPerfCtrlPktDrop_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,3),_QtechBfdSessPerfCtrlPktDrop_Type())
qtechBfdSessPerfCtrlPktDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfCtrlPktDrop.setStatus(_A)
_QtechBfdSessPerfCtrlPktDropLastTime_Type=TimeStamp
_QtechBfdSessPerfCtrlPktDropLastTime_Object=MibTableColumn
qtechBfdSessPerfCtrlPktDropLastTime=_QtechBfdSessPerfCtrlPktDropLastTime_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,4),_QtechBfdSessPerfCtrlPktDropLastTime_Type())
qtechBfdSessPerfCtrlPktDropLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfCtrlPktDropLastTime.setStatus(_A)
_QtechBfdSessPerfEchoPktIn_Type=Counter32
_QtechBfdSessPerfEchoPktIn_Object=MibTableColumn
qtechBfdSessPerfEchoPktIn=_QtechBfdSessPerfEchoPktIn_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,5),_QtechBfdSessPerfEchoPktIn_Type())
qtechBfdSessPerfEchoPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfEchoPktIn.setStatus(_A)
_QtechBfdSessPerfEchoPktOut_Type=Counter32
_QtechBfdSessPerfEchoPktOut_Object=MibTableColumn
qtechBfdSessPerfEchoPktOut=_QtechBfdSessPerfEchoPktOut_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,6),_QtechBfdSessPerfEchoPktOut_Type())
qtechBfdSessPerfEchoPktOut.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfEchoPktOut.setStatus(_A)
_QtechBfdSessPerfEchoPktDrop_Type=Counter32
_QtechBfdSessPerfEchoPktDrop_Object=MibTableColumn
qtechBfdSessPerfEchoPktDrop=_QtechBfdSessPerfEchoPktDrop_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,7),_QtechBfdSessPerfEchoPktDrop_Type())
qtechBfdSessPerfEchoPktDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfEchoPktDrop.setStatus(_A)
_QtechBfdSessPerfEchoPktDropLastTime_Type=TimeStamp
_QtechBfdSessPerfEchoPktDropLastTime_Object=MibTableColumn
qtechBfdSessPerfEchoPktDropLastTime=_QtechBfdSessPerfEchoPktDropLastTime_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,8),_QtechBfdSessPerfEchoPktDropLastTime_Type())
qtechBfdSessPerfEchoPktDropLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfEchoPktDropLastTime.setStatus(_A)
_QtechBfdSessUpTime_Type=TimeStamp
_QtechBfdSessUpTime_Object=MibTableColumn
qtechBfdSessUpTime=_QtechBfdSessUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,9),_QtechBfdSessUpTime_Type())
qtechBfdSessUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessUpTime.setStatus(_A)
_QtechBfdSessPerfLastSessDownTime_Type=TimeStamp
_QtechBfdSessPerfLastSessDownTime_Object=MibTableColumn
qtechBfdSessPerfLastSessDownTime=_QtechBfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,10),_QtechBfdSessPerfLastSessDownTime_Type())
qtechBfdSessPerfLastSessDownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfLastSessDownTime.setStatus(_A)
_QtechBfdSessPerfLastCommLostDiag_Type=QtechBfdDiagTC
_QtechBfdSessPerfLastCommLostDiag_Object=MibTableColumn
qtechBfdSessPerfLastCommLostDiag=_QtechBfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,11),_QtechBfdSessPerfLastCommLostDiag_Type())
qtechBfdSessPerfLastCommLostDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfLastCommLostDiag.setStatus(_A)
_QtechBfdSessPerfSessUpCount_Type=Counter32
_QtechBfdSessPerfSessUpCount_Object=MibTableColumn
qtechBfdSessPerfSessUpCount=_QtechBfdSessPerfSessUpCount_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,12),_QtechBfdSessPerfSessUpCount_Type())
qtechBfdSessPerfSessUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfSessUpCount.setStatus(_A)
_QtechBfdSessPerfDiscTime_Type=TimeStamp
_QtechBfdSessPerfDiscTime_Object=MibTableColumn
qtechBfdSessPerfDiscTime=_QtechBfdSessPerfDiscTime_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,13),_QtechBfdSessPerfDiscTime_Type())
qtechBfdSessPerfDiscTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfDiscTime.setStatus(_A)
_QtechBfdSessPerfCtrlPktInHC_Type=Counter64
_QtechBfdSessPerfCtrlPktInHC_Object=MibTableColumn
qtechBfdSessPerfCtrlPktInHC=_QtechBfdSessPerfCtrlPktInHC_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,14),_QtechBfdSessPerfCtrlPktInHC_Type())
qtechBfdSessPerfCtrlPktInHC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfCtrlPktInHC.setStatus(_A)
_QtechBfdSessPerfCtrlPktOutHC_Type=Counter64
_QtechBfdSessPerfCtrlPktOutHC_Object=MibTableColumn
qtechBfdSessPerfCtrlPktOutHC=_QtechBfdSessPerfCtrlPktOutHC_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,15),_QtechBfdSessPerfCtrlPktOutHC_Type())
qtechBfdSessPerfCtrlPktOutHC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfCtrlPktOutHC.setStatus(_A)
_QtechBfdSessPerfCtrlPktDropHC_Type=Counter64
_QtechBfdSessPerfCtrlPktDropHC_Object=MibTableColumn
qtechBfdSessPerfCtrlPktDropHC=_QtechBfdSessPerfCtrlPktDropHC_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,16),_QtechBfdSessPerfCtrlPktDropHC_Type())
qtechBfdSessPerfCtrlPktDropHC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfCtrlPktDropHC.setStatus(_A)
_QtechBfdSessPerfEchoPktInHC_Type=Counter64
_QtechBfdSessPerfEchoPktInHC_Object=MibTableColumn
qtechBfdSessPerfEchoPktInHC=_QtechBfdSessPerfEchoPktInHC_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,17),_QtechBfdSessPerfEchoPktInHC_Type())
qtechBfdSessPerfEchoPktInHC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfEchoPktInHC.setStatus(_A)
_QtechBfdSessPerfEchoPktOutHC_Type=Counter64
_QtechBfdSessPerfEchoPktOutHC_Object=MibTableColumn
qtechBfdSessPerfEchoPktOutHC=_QtechBfdSessPerfEchoPktOutHC_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,18),_QtechBfdSessPerfEchoPktOutHC_Type())
qtechBfdSessPerfEchoPktOutHC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfEchoPktOutHC.setStatus(_A)
_QtechBfdSessPerfEchoPktDropHC_Type=Counter64
_QtechBfdSessPerfEchoPktDropHC_Object=MibTableColumn
qtechBfdSessPerfEchoPktDropHC=_QtechBfdSessPerfEchoPktDropHC_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,3,1,19),_QtechBfdSessPerfEchoPktDropHC_Type())
qtechBfdSessPerfEchoPktDropHC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessPerfEchoPktDropHC.setStatus(_A)
_QtechBfdSessDiscMapTable_Object=MibTable
qtechBfdSessDiscMapTable=_QtechBfdSessDiscMapTable_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,4))
if mibBuilder.loadTexts:qtechBfdSessDiscMapTable.setStatus(_A)
_QtechBfdSessDiscMapEntry_Object=MibTableRow
qtechBfdSessDiscMapEntry=_QtechBfdSessDiscMapEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,4,1))
qtechBfdSessDiscMapEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechBfdSessDiscMapEntry.setStatus(_A)
_QtechBfdSessDiscMapIndex_Type=QtechBfdSessIndexTC
_QtechBfdSessDiscMapIndex_Object=MibTableColumn
qtechBfdSessDiscMapIndex=_QtechBfdSessDiscMapIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,4,1,1),_QtechBfdSessDiscMapIndex_Type())
qtechBfdSessDiscMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessDiscMapIndex.setStatus(_A)
_QtechBfdSessDiscMapStorageType_Type=StorageType
_QtechBfdSessDiscMapStorageType_Object=MibTableColumn
qtechBfdSessDiscMapStorageType=_QtechBfdSessDiscMapStorageType_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,4,1,2),_QtechBfdSessDiscMapStorageType_Type())
qtechBfdSessDiscMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessDiscMapStorageType.setStatus(_A)
_QtechBfdSessDiscMapRowStatus_Type=RowStatus
_QtechBfdSessDiscMapRowStatus_Object=MibTableColumn
qtechBfdSessDiscMapRowStatus=_QtechBfdSessDiscMapRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,4,1,3),_QtechBfdSessDiscMapRowStatus_Type())
qtechBfdSessDiscMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessDiscMapRowStatus.setStatus(_A)
_QtechBfdSessIpMapTable_Object=MibTable
qtechBfdSessIpMapTable=_QtechBfdSessIpMapTable_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,5))
if mibBuilder.loadTexts:qtechBfdSessIpMapTable.setStatus(_A)
_QtechBfdSessIpMapEntry_Object=MibTableRow
qtechBfdSessIpMapEntry=_QtechBfdSessIpMapEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,5,1))
qtechBfdSessIpMapEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:qtechBfdSessIpMapEntry.setStatus(_A)
_QtechBfdSessIpMapIndex_Type=QtechBfdSessIndexTC
_QtechBfdSessIpMapIndex_Object=MibTableColumn
qtechBfdSessIpMapIndex=_QtechBfdSessIpMapIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,5,1,1),_QtechBfdSessIpMapIndex_Type())
qtechBfdSessIpMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBfdSessIpMapIndex.setStatus(_A)
_QtechBfdSessIpMapStorageType_Type=StorageType
_QtechBfdSessIpMapStorageType_Object=MibTableColumn
qtechBfdSessIpMapStorageType=_QtechBfdSessIpMapStorageType_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,5,1,2),_QtechBfdSessIpMapStorageType_Type())
qtechBfdSessIpMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessIpMapStorageType.setStatus(_A)
_QtechBfdSessIpMapRowStatus_Type=RowStatus
_QtechBfdSessIpMapRowStatus_Object=MibTableColumn
qtechBfdSessIpMapRowStatus=_QtechBfdSessIpMapRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,48,1,5,1,3),_QtechBfdSessIpMapRowStatus_Type())
qtechBfdSessIpMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBfdSessIpMapRowStatus.setStatus(_A)
_QtechBfdConformance_ObjectIdentity=ObjectIdentity
qtechBfdConformance=_QtechBfdConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,48,2))
_QtechBfdGroups_ObjectIdentity=ObjectIdentity
qtechBfdGroups=_QtechBfdGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,48,2,1))
_QtechBfdCompliances_ObjectIdentity=ObjectIdentity
qtechBfdCompliances=_QtechBfdCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,48,2,2))
qtechBfdSessEntry.registerAugmentions((_B,_a))
qtechBfdSessPerfEntry.setIndexNames(*qtechBfdSessEntry.getIndexNames())
qtechBfdSessionGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,48,2,1,1))
qtechBfdSessionGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:qtechBfdSessionGroup.setStatus(_A)
qtechBfdSessionReadOnlyGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,48,2,1,2))
qtechBfdSessionReadOnlyGroup.setObjects(*((_B,_I),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_F),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:qtechBfdSessionReadOnlyGroup.setStatus(_A)
qtechBfdSessionPerfGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,48,2,1,3))
qtechBfdSessionPerfGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:qtechBfdSessionPerfGroup.setStatus(_A)
qtechBfdSessionPerfHCGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,48,2,1,4))
qtechBfdSessionPerfHCGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:qtechBfdSessionPerfHCGroup.setStatus(_A)
qtechBfdSessUp=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,48,0,1))
qtechBfdSessUp.setObjects(*((_B,_F),(_B,_F)))
if mibBuilder.loadTexts:qtechBfdSessUp.setStatus(_A)
qtechBfdSessDown=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,48,0,2))
qtechBfdSessDown.setObjects(*((_B,_F),(_B,_F)))
if mibBuilder.loadTexts:qtechBfdSessDown.setStatus(_A)
qtechBfdNotificationGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,48,2,1,5))
qtechBfdNotificationGroup.setObjects(*((_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:qtechBfdNotificationGroup.setStatus(_A)
qtechBfdModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,48,2,2,1))
qtechBfdModuleFullCompliance.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:qtechBfdModuleFullCompliance.setStatus(_A)
qtechBfdModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,48,2,2,2))
qtechBfdModuleReadOnlyCompliance.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:qtechBfdModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'QtechBfdSessIndexTC':QtechBfdSessIndexTC,'QtechBfdIntervalTC':QtechBfdIntervalTC,'QtechBfdMultiplierTC':QtechBfdMultiplierTC,'QtechBfdDiagTC':QtechBfdDiagTC,'QtechBfdSessTypeTC':QtechBfdSessTypeTC,'QtechBfdSessOperModeTC':QtechBfdSessOperModeTC,_W:QtechBfdCtrlDestPortNumberTC,_X:QtechBfdCtrlSourcePortNumberTC,_Y:QtechBfdSessStateTC,_Z:QtechBfdSessAuthenticationTypeTC,'QtechBfdSessionAuthenticationKeyTC':QtechBfdSessionAuthenticationKeyTC,'qtechBfdMIB':qtechBfdMIB,'qtechBfdNotifications':qtechBfdNotifications,_AU:qtechBfdSessUp,_AV:qtechBfdSessDown,'qtechBfdObjects':qtechBfdObjects,'qtechBfdScalarObjects':qtechBfdScalarObjects,_b:qtechBfdAdminStatus,_c:qtechBfdSessNotificationsEnable,'qtechBfdSessTable':qtechBfdSessTable,'qtechBfdSessEntry':qtechBfdSessEntry,_V:qtechBfdSessIndex,_d:qtechBfdSessVersionNumber,_e:qtechBfdSessType,_I:qtechBfdSessDiscriminator,_A3:qtechBfdSessRemoteDiscr,_f:qtechBfdSessDestinationUdpPort,_g:qtechBfdSessSourceUdpPort,_h:qtechBfdSessEchoSourceUdpPort,_i:qtechBfdSessAdminStatus,_A4:qtechBfdSessState,_A5:qtechBfdSessRemoteHeardFlag,_F:qtechBfdSessDiag,_j:qtechBfdSessOperMode,_k:qtechBfdSessDemandModeDesiredFlag,_l:qtechBfdSessControlPlaneIndepFlag,_m:qtechBfdSessMultipointFlag,_J:qtechBfdSessInterface,_K:qtechBfdSessSrcAddrType,_L:qtechBfdSessSrcAddr,_M:qtechBfdSessDstAddrType,_N:qtechBfdSessDstAddr,_n:qtechBfdSessGTSM,_o:qtechBfdSessGTSMTTL,_p:qtechBfdSessDesiredMinTxInterval,_q:qtechBfdSessReqMinRxInterval,_r:qtechBfdSessReqMinEchoRxInterval,_s:qtechBfdSessDetectMult,_A6:qtechBfdSessNegotiatedInterval,_A7:qtechBfdSessNegotiatedEchoInterval,_A8:qtechBfdSessNegotiatedDetectMult,_t:qtechBfdSessAuthPresFlag,_u:qtechBfdSessAuthenticationType,_v:qtechBfdSessAuthenticationKeyID,_w:qtechBfdSessAuthenticationKey,_x:qtechBfdSessStorageType,_y:qtechBfdSessRowStatus,'qtechBfdSessPerfTable':qtechBfdSessPerfTable,_a:qtechBfdSessPerfEntry,_AB:qtechBfdSessPerfCtrlPktIn,_AC:qtechBfdSessPerfCtrlPktOut,_AD:qtechBfdSessPerfCtrlPktDrop,_AE:qtechBfdSessPerfCtrlPktDropLastTime,_AF:qtechBfdSessPerfEchoPktIn,_AG:qtechBfdSessPerfEchoPktOut,_AH:qtechBfdSessPerfEchoPktDrop,_AI:qtechBfdSessPerfEchoPktDropLastTime,_AJ:qtechBfdSessUpTime,_AK:qtechBfdSessPerfLastSessDownTime,_AL:qtechBfdSessPerfLastCommLostDiag,_AM:qtechBfdSessPerfSessUpCount,_AN:qtechBfdSessPerfDiscTime,_AO:qtechBfdSessPerfCtrlPktInHC,_AP:qtechBfdSessPerfCtrlPktOutHC,_AQ:qtechBfdSessPerfCtrlPktDropHC,_AR:qtechBfdSessPerfEchoPktInHC,_AS:qtechBfdSessPerfEchoPktOutHC,_AT:qtechBfdSessPerfEchoPktDropHC,'qtechBfdSessDiscMapTable':qtechBfdSessDiscMapTable,'qtechBfdSessDiscMapEntry':qtechBfdSessDiscMapEntry,_A9:qtechBfdSessDiscMapIndex,_z:qtechBfdSessDiscMapStorageType,_A0:qtechBfdSessDiscMapRowStatus,'qtechBfdSessIpMapTable':qtechBfdSessIpMapTable,'qtechBfdSessIpMapEntry':qtechBfdSessIpMapEntry,_AA:qtechBfdSessIpMapIndex,_A1:qtechBfdSessIpMapStorageType,_A2:qtechBfdSessIpMapRowStatus,'qtechBfdConformance':qtechBfdConformance,'qtechBfdGroups':qtechBfdGroups,_O:qtechBfdSessionGroup,_P:qtechBfdSessionReadOnlyGroup,_Q:qtechBfdSessionPerfGroup,_S:qtechBfdSessionPerfHCGroup,_R:qtechBfdNotificationGroup,'qtechBfdCompliances':qtechBfdCompliances,'qtechBfdModuleFullCompliance':qtechBfdModuleFullCompliance,'qtechBfdModuleReadOnlyCompliance':qtechBfdModuleReadOnlyCompliance})