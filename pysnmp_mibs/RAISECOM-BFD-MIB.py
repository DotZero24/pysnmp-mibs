_a='raisecomBfdSessPerfEntry'
_Z='raisecomBfdTemplateName'
_Y='raisecomBfdIfIndex'
_X='raisecomBfdSessDstAddr'
_W='raisecomBfdSessDstAddrType'
_V='raisecomBfdSessSrcAddr'
_U='raisecomBfdSessSrcAddrType'
_T='raisecomBfdSessInterface'
_S='raisecomBfdSessDiscriminator'
_R='BfdSessStateTC'
_Q='BfdCtrlSourcePortNumberTC'
_P='BfdCtrlDestPortNumberTC'
_O='raisecomBfdSessIndex'
_N='EnableVar'
_M='InetPortNumber'
_L='not-accessible'
_K='OctetString'
_J='BfdSessAuthenticationTypeTC'
_I='raisecomBfdSessDiag'
_H='Integer32'
_G='TruthValue'
_F='Unsigned32'
_E='RAISECOM-BFD-MIB'
_D='read-write'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_M)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks',_F,'iso','mib-2','zeroDotZero')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_G)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_N)
raisecomBfd=ModuleIdentity((1,3,6,1,4,1,8886,1,35))
if mibBuilder.loadTexts:raisecomBfd.setRevisions(('2011-04-20 00:00',))
class BfdSessIndexTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdIntervalTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class BfdMultiplierTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class BfdDiagTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noDiagnostic',0),('controlDetectionTimeExpired',1),('echoFunctionFailed',2),('neighborSignaledSessionDown',3),('forwardingPlaneReset',4),('pathDown',5),('concatenatedPathDown',6),('administrativelyDown',7),('reverseConcatenatedPathDown',8)))
class BfdSessTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('singleHop',1),('multiHopTotallyArbitraryPaths',2),('multiHopOutOfBandSignaling',3),('multiHopUnidirectionalLinks',4),('multiPointHead',5),('multiPointTail',6)))
class BfdSessOperModeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asyncModeWEchoFunction',1),('asynchModeWOEchoFunction',2),('demandModeWEchoFunction',3),('demandModeWOEchoFunction',4)))
class BfdCtrlDestPortNumberTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class BfdCtrlSourcePortNumberTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class BfdSessStateTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4),('failing',5)))
class BfdSessAuthenticationTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5)));namedValues=NamedValues(*(('noAuthentication',-1),('reserved',0),('simplePassword',1),('keyedMD5',2),('meticulousKeyedMD5',3),('keyedSHA1',4),('meticulousKeyedSHA1',5)))
class BfdSessionAuthenticationKeyTC(TextualConvention,OctetString):status=_A;displayHint='1x ';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,252))
_RaisecomBfdNotifications_ObjectIdentity=ObjectIdentity
raisecomBfdNotifications=_RaisecomBfdNotifications_ObjectIdentity((1,3,6,1,4,1,8886,1,35,0))
_RaisecomBfdObjects_ObjectIdentity=ObjectIdentity
raisecomBfdObjects=_RaisecomBfdObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,35,1))
_RaisecomBfdScalarObjects_ObjectIdentity=ObjectIdentity
raisecomBfdScalarObjects=_RaisecomBfdScalarObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,35,1,1))
class _RaisecomBfdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RaisecomBfdAdminStatus_Type.__name__=_H
_RaisecomBfdAdminStatus_Object=MibScalar
raisecomBfdAdminStatus=_RaisecomBfdAdminStatus_Object((1,3,6,1,4,1,8886,1,35,1,1,1),_RaisecomBfdAdminStatus_Type())
raisecomBfdAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdAdminStatus.setStatus(_A)
class _RaisecomBfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_RaisecomBfdSessNotificationsEnable_Type.__name__=_G
_RaisecomBfdSessNotificationsEnable_Object=MibScalar
raisecomBfdSessNotificationsEnable=_RaisecomBfdSessNotificationsEnable_Object((1,3,6,1,4,1,8886,1,35,1,1,2),_RaisecomBfdSessNotificationsEnable_Type())
raisecomBfdSessNotificationsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdSessNotificationsEnable.setStatus(_A)
class _RaisecomBfdRoleMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activeRole',1),('passiveRole',2)))
_RaisecomBfdRoleMode_Type.__name__=_H
_RaisecomBfdRoleMode_Object=MibScalar
raisecomBfdRoleMode=_RaisecomBfdRoleMode_Object((1,3,6,1,4,1,8886,1,35,1,1,3),_RaisecomBfdRoleMode_Type())
raisecomBfdRoleMode.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdRoleMode.setStatus(_A)
_RaisecomBfdEchoSourceIpType_Type=InetAddressType
_RaisecomBfdEchoSourceIpType_Object=MibScalar
raisecomBfdEchoSourceIpType=_RaisecomBfdEchoSourceIpType_Object((1,3,6,1,4,1,8886,1,35,1,1,4),_RaisecomBfdEchoSourceIpType_Type())
raisecomBfdEchoSourceIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdEchoSourceIpType.setStatus(_A)
_RaisecomBfdEchoSourceIpAddr_Type=InetAddress
_RaisecomBfdEchoSourceIpAddr_Object=MibScalar
raisecomBfdEchoSourceIpAddr=_RaisecomBfdEchoSourceIpAddr_Object((1,3,6,1,4,1,8886,1,35,1,1,5),_RaisecomBfdEchoSourceIpAddr_Type())
raisecomBfdEchoSourceIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdEchoSourceIpAddr.setStatus(_A)
class _RaisecomBfdAllSessionsStatisticsClear_Type(EnableVar):defaultValue=2
_RaisecomBfdAllSessionsStatisticsClear_Type.__name__=_N
_RaisecomBfdAllSessionsStatisticsClear_Object=MibScalar
raisecomBfdAllSessionsStatisticsClear=_RaisecomBfdAllSessionsStatisticsClear_Object((1,3,6,1,4,1,8886,1,35,1,1,6),_RaisecomBfdAllSessionsStatisticsClear_Type())
raisecomBfdAllSessionsStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdAllSessionsStatisticsClear.setStatus(_A)
_RaisecomBfdSessTable_Object=MibTable
raisecomBfdSessTable=_RaisecomBfdSessTable_Object((1,3,6,1,4,1,8886,1,35,1,2))
if mibBuilder.loadTexts:raisecomBfdSessTable.setStatus(_A)
_RaisecomBfdSessEntry_Object=MibTableRow
raisecomBfdSessEntry=_RaisecomBfdSessEntry_Object((1,3,6,1,4,1,8886,1,35,1,2,1))
raisecomBfdSessEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:raisecomBfdSessEntry.setStatus(_A)
_RaisecomBfdSessIndex_Type=BfdSessIndexTC
_RaisecomBfdSessIndex_Object=MibTableColumn
raisecomBfdSessIndex=_RaisecomBfdSessIndex_Object((1,3,6,1,4,1,8886,1,35,1,2,1,1),_RaisecomBfdSessIndex_Type())
raisecomBfdSessIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomBfdSessIndex.setStatus(_A)
class _RaisecomBfdSessVersionNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomBfdSessVersionNumber_Type.__name__=_F
_RaisecomBfdSessVersionNumber_Object=MibTableColumn
raisecomBfdSessVersionNumber=_RaisecomBfdSessVersionNumber_Object((1,3,6,1,4,1,8886,1,35,1,2,1,2),_RaisecomBfdSessVersionNumber_Type())
raisecomBfdSessVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessVersionNumber.setStatus(_A)
_RaisecomBfdSessType_Type=BfdSessTypeTC
_RaisecomBfdSessType_Object=MibTableColumn
raisecomBfdSessType=_RaisecomBfdSessType_Object((1,3,6,1,4,1,8886,1,35,1,2,1,3),_RaisecomBfdSessType_Type())
raisecomBfdSessType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessType.setStatus(_A)
class _RaisecomBfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RaisecomBfdSessDiscriminator_Type.__name__=_F
_RaisecomBfdSessDiscriminator_Object=MibTableColumn
raisecomBfdSessDiscriminator=_RaisecomBfdSessDiscriminator_Object((1,3,6,1,4,1,8886,1,35,1,2,1,4),_RaisecomBfdSessDiscriminator_Type())
raisecomBfdSessDiscriminator.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessDiscriminator.setStatus(_A)
class _RaisecomBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_RaisecomBfdSessRemoteDiscr_Type.__name__=_F
_RaisecomBfdSessRemoteDiscr_Object=MibTableColumn
raisecomBfdSessRemoteDiscr=_RaisecomBfdSessRemoteDiscr_Object((1,3,6,1,4,1,8886,1,35,1,2,1,5),_RaisecomBfdSessRemoteDiscr_Type())
raisecomBfdSessRemoteDiscr.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessRemoteDiscr.setStatus(_A)
class _RaisecomBfdSessDestinationUdpPort_Type(BfdCtrlDestPortNumberTC):defaultValue=0
_RaisecomBfdSessDestinationUdpPort_Type.__name__=_P
_RaisecomBfdSessDestinationUdpPort_Object=MibTableColumn
raisecomBfdSessDestinationUdpPort=_RaisecomBfdSessDestinationUdpPort_Object((1,3,6,1,4,1,8886,1,35,1,2,1,6),_RaisecomBfdSessDestinationUdpPort_Type())
raisecomBfdSessDestinationUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessDestinationUdpPort.setStatus(_A)
class _RaisecomBfdSessSourceUdpPort_Type(BfdCtrlSourcePortNumberTC):defaultValue=0
_RaisecomBfdSessSourceUdpPort_Type.__name__=_Q
_RaisecomBfdSessSourceUdpPort_Object=MibTableColumn
raisecomBfdSessSourceUdpPort=_RaisecomBfdSessSourceUdpPort_Object((1,3,6,1,4,1,8886,1,35,1,2,1,7),_RaisecomBfdSessSourceUdpPort_Type())
raisecomBfdSessSourceUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessSourceUdpPort.setStatus(_A)
class _RaisecomBfdSessEchoSourceUdpPort_Type(InetPortNumber):defaultValue=0
_RaisecomBfdSessEchoSourceUdpPort_Type.__name__=_M
_RaisecomBfdSessEchoSourceUdpPort_Object=MibTableColumn
raisecomBfdSessEchoSourceUdpPort=_RaisecomBfdSessEchoSourceUdpPort_Object((1,3,6,1,4,1,8886,1,35,1,2,1,8),_RaisecomBfdSessEchoSourceUdpPort_Type())
raisecomBfdSessEchoSourceUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessEchoSourceUdpPort.setStatus(_A)
class _RaisecomBfdSessAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_RaisecomBfdSessAdminStatus_Type.__name__=_H
_RaisecomBfdSessAdminStatus_Object=MibTableColumn
raisecomBfdSessAdminStatus=_RaisecomBfdSessAdminStatus_Object((1,3,6,1,4,1,8886,1,35,1,2,1,9),_RaisecomBfdSessAdminStatus_Type())
raisecomBfdSessAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessAdminStatus.setStatus(_A)
class _RaisecomBfdSessState_Type(BfdSessStateTC):defaultValue=2
_RaisecomBfdSessState_Type.__name__=_R
_RaisecomBfdSessState_Object=MibTableColumn
raisecomBfdSessState=_RaisecomBfdSessState_Object((1,3,6,1,4,1,8886,1,35,1,2,1,10),_RaisecomBfdSessState_Type())
raisecomBfdSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessState.setStatus(_A)
class _RaisecomBfdSessRemoteHeardFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdSessRemoteHeardFlag_Type.__name__=_G
_RaisecomBfdSessRemoteHeardFlag_Object=MibTableColumn
raisecomBfdSessRemoteHeardFlag=_RaisecomBfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,8886,1,35,1,2,1,11),_RaisecomBfdSessRemoteHeardFlag_Type())
raisecomBfdSessRemoteHeardFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessRemoteHeardFlag.setStatus(_A)
_RaisecomBfdSessDiag_Type=BfdDiagTC
_RaisecomBfdSessDiag_Object=MibTableColumn
raisecomBfdSessDiag=_RaisecomBfdSessDiag_Object((1,3,6,1,4,1,8886,1,35,1,2,1,12),_RaisecomBfdSessDiag_Type())
raisecomBfdSessDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessDiag.setStatus(_A)
_RaisecomBfdSessOperMode_Type=BfdSessOperModeTC
_RaisecomBfdSessOperMode_Object=MibTableColumn
raisecomBfdSessOperMode=_RaisecomBfdSessOperMode_Object((1,3,6,1,4,1,8886,1,35,1,2,1,13),_RaisecomBfdSessOperMode_Type())
raisecomBfdSessOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessOperMode.setStatus(_A)
class _RaisecomBfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdSessDemandModeDesiredFlag_Type.__name__=_G
_RaisecomBfdSessDemandModeDesiredFlag_Object=MibTableColumn
raisecomBfdSessDemandModeDesiredFlag=_RaisecomBfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,8886,1,35,1,2,1,14),_RaisecomBfdSessDemandModeDesiredFlag_Type())
raisecomBfdSessDemandModeDesiredFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessDemandModeDesiredFlag.setStatus(_A)
class _RaisecomBfdSessControlPlaneIndepFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdSessControlPlaneIndepFlag_Type.__name__=_G
_RaisecomBfdSessControlPlaneIndepFlag_Object=MibTableColumn
raisecomBfdSessControlPlaneIndepFlag=_RaisecomBfdSessControlPlaneIndepFlag_Object((1,3,6,1,4,1,8886,1,35,1,2,1,15),_RaisecomBfdSessControlPlaneIndepFlag_Type())
raisecomBfdSessControlPlaneIndepFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessControlPlaneIndepFlag.setStatus(_A)
class _RaisecomBfdSessMultipointFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdSessMultipointFlag_Type.__name__=_G
_RaisecomBfdSessMultipointFlag_Object=MibTableColumn
raisecomBfdSessMultipointFlag=_RaisecomBfdSessMultipointFlag_Object((1,3,6,1,4,1,8886,1,35,1,2,1,16),_RaisecomBfdSessMultipointFlag_Type())
raisecomBfdSessMultipointFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessMultipointFlag.setStatus(_A)
_RaisecomBfdSessInterface_Type=InterfaceIndexOrZero
_RaisecomBfdSessInterface_Object=MibTableColumn
raisecomBfdSessInterface=_RaisecomBfdSessInterface_Object((1,3,6,1,4,1,8886,1,35,1,2,1,17),_RaisecomBfdSessInterface_Type())
raisecomBfdSessInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessInterface.setStatus(_A)
_RaisecomBfdSessSrcAddrType_Type=InetAddressType
_RaisecomBfdSessSrcAddrType_Object=MibTableColumn
raisecomBfdSessSrcAddrType=_RaisecomBfdSessSrcAddrType_Object((1,3,6,1,4,1,8886,1,35,1,2,1,18),_RaisecomBfdSessSrcAddrType_Type())
raisecomBfdSessSrcAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessSrcAddrType.setStatus(_A)
_RaisecomBfdSessSrcAddr_Type=InetAddress
_RaisecomBfdSessSrcAddr_Object=MibTableColumn
raisecomBfdSessSrcAddr=_RaisecomBfdSessSrcAddr_Object((1,3,6,1,4,1,8886,1,35,1,2,1,19),_RaisecomBfdSessSrcAddr_Type())
raisecomBfdSessSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessSrcAddr.setStatus(_A)
_RaisecomBfdSessDstAddrType_Type=InetAddressType
_RaisecomBfdSessDstAddrType_Object=MibTableColumn
raisecomBfdSessDstAddrType=_RaisecomBfdSessDstAddrType_Object((1,3,6,1,4,1,8886,1,35,1,2,1,20),_RaisecomBfdSessDstAddrType_Type())
raisecomBfdSessDstAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessDstAddrType.setStatus(_A)
_RaisecomBfdSessDstAddr_Type=InetAddress
_RaisecomBfdSessDstAddr_Object=MibTableColumn
raisecomBfdSessDstAddr=_RaisecomBfdSessDstAddr_Object((1,3,6,1,4,1,8886,1,35,1,2,1,21),_RaisecomBfdSessDstAddr_Type())
raisecomBfdSessDstAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessDstAddr.setStatus(_A)
class _RaisecomBfdSessGTSM_Type(TruthValue):defaultValue=2
_RaisecomBfdSessGTSM_Type.__name__=_G
_RaisecomBfdSessGTSM_Object=MibTableColumn
raisecomBfdSessGTSM=_RaisecomBfdSessGTSM_Object((1,3,6,1,4,1,8886,1,35,1,2,1,22),_RaisecomBfdSessGTSM_Type())
raisecomBfdSessGTSM.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessGTSM.setStatus(_A)
class _RaisecomBfdSessGTSMTTL_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomBfdSessGTSMTTL_Type.__name__=_F
_RaisecomBfdSessGTSMTTL_Object=MibTableColumn
raisecomBfdSessGTSMTTL=_RaisecomBfdSessGTSMTTL_Object((1,3,6,1,4,1,8886,1,35,1,2,1,23),_RaisecomBfdSessGTSMTTL_Type())
raisecomBfdSessGTSMTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessGTSMTTL.setStatus(_A)
_RaisecomBfdSessDesiredMinTxInterval_Type=BfdIntervalTC
_RaisecomBfdSessDesiredMinTxInterval_Object=MibTableColumn
raisecomBfdSessDesiredMinTxInterval=_RaisecomBfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,8886,1,35,1,2,1,24),_RaisecomBfdSessDesiredMinTxInterval_Type())
raisecomBfdSessDesiredMinTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessDesiredMinTxInterval.setStatus(_A)
_RaisecomBfdSessReqMinRxInterval_Type=BfdIntervalTC
_RaisecomBfdSessReqMinRxInterval_Object=MibTableColumn
raisecomBfdSessReqMinRxInterval=_RaisecomBfdSessReqMinRxInterval_Object((1,3,6,1,4,1,8886,1,35,1,2,1,25),_RaisecomBfdSessReqMinRxInterval_Type())
raisecomBfdSessReqMinRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessReqMinRxInterval.setStatus(_A)
_RaisecomBfdSessReqMinEchoRxInterval_Type=BfdIntervalTC
_RaisecomBfdSessReqMinEchoRxInterval_Object=MibTableColumn
raisecomBfdSessReqMinEchoRxInterval=_RaisecomBfdSessReqMinEchoRxInterval_Object((1,3,6,1,4,1,8886,1,35,1,2,1,26),_RaisecomBfdSessReqMinEchoRxInterval_Type())
raisecomBfdSessReqMinEchoRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessReqMinEchoRxInterval.setStatus(_A)
_RaisecomBfdSessDetectMult_Type=BfdMultiplierTC
_RaisecomBfdSessDetectMult_Object=MibTableColumn
raisecomBfdSessDetectMult=_RaisecomBfdSessDetectMult_Object((1,3,6,1,4,1,8886,1,35,1,2,1,27),_RaisecomBfdSessDetectMult_Type())
raisecomBfdSessDetectMult.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessDetectMult.setStatus(_A)
_RaisecomBfdSessNegotiatedInterval_Type=BfdIntervalTC
_RaisecomBfdSessNegotiatedInterval_Object=MibTableColumn
raisecomBfdSessNegotiatedInterval=_RaisecomBfdSessNegotiatedInterval_Object((1,3,6,1,4,1,8886,1,35,1,2,1,28),_RaisecomBfdSessNegotiatedInterval_Type())
raisecomBfdSessNegotiatedInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessNegotiatedInterval.setStatus(_A)
_RaisecomBfdSessNegotiatedEchoInterval_Type=BfdIntervalTC
_RaisecomBfdSessNegotiatedEchoInterval_Object=MibTableColumn
raisecomBfdSessNegotiatedEchoInterval=_RaisecomBfdSessNegotiatedEchoInterval_Object((1,3,6,1,4,1,8886,1,35,1,2,1,29),_RaisecomBfdSessNegotiatedEchoInterval_Type())
raisecomBfdSessNegotiatedEchoInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessNegotiatedEchoInterval.setStatus(_A)
_RaisecomBfdSessNegotiatedDetectMult_Type=BfdMultiplierTC
_RaisecomBfdSessNegotiatedDetectMult_Object=MibTableColumn
raisecomBfdSessNegotiatedDetectMult=_RaisecomBfdSessNegotiatedDetectMult_Object((1,3,6,1,4,1,8886,1,35,1,2,1,30),_RaisecomBfdSessNegotiatedDetectMult_Type())
raisecomBfdSessNegotiatedDetectMult.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessNegotiatedDetectMult.setStatus(_A)
class _RaisecomBfdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdSessAuthPresFlag_Type.__name__=_G
_RaisecomBfdSessAuthPresFlag_Object=MibTableColumn
raisecomBfdSessAuthPresFlag=_RaisecomBfdSessAuthPresFlag_Object((1,3,6,1,4,1,8886,1,35,1,2,1,31),_RaisecomBfdSessAuthPresFlag_Type())
raisecomBfdSessAuthPresFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessAuthPresFlag.setStatus(_A)
class _RaisecomBfdSessAuthenticationType_Type(BfdSessAuthenticationTypeTC):defaultValue=-1
_RaisecomBfdSessAuthenticationType_Type.__name__=_J
_RaisecomBfdSessAuthenticationType_Object=MibTableColumn
raisecomBfdSessAuthenticationType=_RaisecomBfdSessAuthenticationType_Object((1,3,6,1,4,1,8886,1,35,1,2,1,32),_RaisecomBfdSessAuthenticationType_Type())
raisecomBfdSessAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessAuthenticationType.setStatus(_A)
class _RaisecomBfdSessAuthenticationKeyID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_RaisecomBfdSessAuthenticationKeyID_Type.__name__=_H
_RaisecomBfdSessAuthenticationKeyID_Object=MibTableColumn
raisecomBfdSessAuthenticationKeyID=_RaisecomBfdSessAuthenticationKeyID_Object((1,3,6,1,4,1,8886,1,35,1,2,1,33),_RaisecomBfdSessAuthenticationKeyID_Type())
raisecomBfdSessAuthenticationKeyID.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessAuthenticationKeyID.setStatus(_A)
_RaisecomBfdSessAuthenticationKey_Type=BfdSessionAuthenticationKeyTC
_RaisecomBfdSessAuthenticationKey_Object=MibTableColumn
raisecomBfdSessAuthenticationKey=_RaisecomBfdSessAuthenticationKey_Object((1,3,6,1,4,1,8886,1,35,1,2,1,34),_RaisecomBfdSessAuthenticationKey_Type())
raisecomBfdSessAuthenticationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessAuthenticationKey.setStatus(_A)
_RaisecomBfdSessStorType_Type=StorageType
_RaisecomBfdSessStorType_Object=MibTableColumn
raisecomBfdSessStorType=_RaisecomBfdSessStorType_Object((1,3,6,1,4,1,8886,1,35,1,2,1,35),_RaisecomBfdSessStorType_Type())
raisecomBfdSessStorType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessStorType.setStatus(_A)
_RaisecomBfdSessRowStatus_Type=RowStatus
_RaisecomBfdSessRowStatus_Object=MibTableColumn
raisecomBfdSessRowStatus=_RaisecomBfdSessRowStatus_Object((1,3,6,1,4,1,8886,1,35,1,2,1,36),_RaisecomBfdSessRowStatus_Type())
raisecomBfdSessRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessRowStatus.setStatus(_A)
class _RaisecomBfdSessTemplateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomBfdSessTemplateName_Type.__name__=_K
_RaisecomBfdSessTemplateName_Object=MibTableColumn
raisecomBfdSessTemplateName=_RaisecomBfdSessTemplateName_Object((1,3,6,1,4,1,8886,1,35,1,2,1,37),_RaisecomBfdSessTemplateName_Type())
raisecomBfdSessTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdSessTemplateName.setStatus(_A)
_RaisecomBfdSessPerfTable_Object=MibTable
raisecomBfdSessPerfTable=_RaisecomBfdSessPerfTable_Object((1,3,6,1,4,1,8886,1,35,1,3))
if mibBuilder.loadTexts:raisecomBfdSessPerfTable.setStatus(_A)
_RaisecomBfdSessPerfEntry_Object=MibTableRow
raisecomBfdSessPerfEntry=_RaisecomBfdSessPerfEntry_Object((1,3,6,1,4,1,8886,1,35,1,3,1))
if mibBuilder.loadTexts:raisecomBfdSessPerfEntry.setStatus(_A)
_RaisecomBfdSessPerfCtrlPktIn_Type=Counter32
_RaisecomBfdSessPerfCtrlPktIn_Object=MibTableColumn
raisecomBfdSessPerfCtrlPktIn=_RaisecomBfdSessPerfCtrlPktIn_Object((1,3,6,1,4,1,8886,1,35,1,3,1,1),_RaisecomBfdSessPerfCtrlPktIn_Type())
raisecomBfdSessPerfCtrlPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfCtrlPktIn.setStatus(_A)
_RaisecomBfdSessPerfCtrlPktOut_Type=Counter32
_RaisecomBfdSessPerfCtrlPktOut_Object=MibTableColumn
raisecomBfdSessPerfCtrlPktOut=_RaisecomBfdSessPerfCtrlPktOut_Object((1,3,6,1,4,1,8886,1,35,1,3,1,2),_RaisecomBfdSessPerfCtrlPktOut_Type())
raisecomBfdSessPerfCtrlPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfCtrlPktOut.setStatus(_A)
_RaisecomBfdSessPerfCtrlPktDrop_Type=Counter32
_RaisecomBfdSessPerfCtrlPktDrop_Object=MibTableColumn
raisecomBfdSessPerfCtrlPktDrop=_RaisecomBfdSessPerfCtrlPktDrop_Object((1,3,6,1,4,1,8886,1,35,1,3,1,3),_RaisecomBfdSessPerfCtrlPktDrop_Type())
raisecomBfdSessPerfCtrlPktDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfCtrlPktDrop.setStatus(_A)
_RaisecomBfdSessPerfCtrlPktDropLastTime_Type=TimeStamp
_RaisecomBfdSessPerfCtrlPktDropLastTime_Object=MibTableColumn
raisecomBfdSessPerfCtrlPktDropLastTime=_RaisecomBfdSessPerfCtrlPktDropLastTime_Object((1,3,6,1,4,1,8886,1,35,1,3,1,4),_RaisecomBfdSessPerfCtrlPktDropLastTime_Type())
raisecomBfdSessPerfCtrlPktDropLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfCtrlPktDropLastTime.setStatus(_A)
_RaisecomBfdSessPerfEchoPktIn_Type=Counter32
_RaisecomBfdSessPerfEchoPktIn_Object=MibTableColumn
raisecomBfdSessPerfEchoPktIn=_RaisecomBfdSessPerfEchoPktIn_Object((1,3,6,1,4,1,8886,1,35,1,3,1,5),_RaisecomBfdSessPerfEchoPktIn_Type())
raisecomBfdSessPerfEchoPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfEchoPktIn.setStatus(_A)
_RaisecomBfdSessPerfEchoPktOut_Type=Counter32
_RaisecomBfdSessPerfEchoPktOut_Object=MibTableColumn
raisecomBfdSessPerfEchoPktOut=_RaisecomBfdSessPerfEchoPktOut_Object((1,3,6,1,4,1,8886,1,35,1,3,1,6),_RaisecomBfdSessPerfEchoPktOut_Type())
raisecomBfdSessPerfEchoPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfEchoPktOut.setStatus(_A)
_RaisecomBfdSessPerfEchoPktDrop_Type=Counter32
_RaisecomBfdSessPerfEchoPktDrop_Object=MibTableColumn
raisecomBfdSessPerfEchoPktDrop=_RaisecomBfdSessPerfEchoPktDrop_Object((1,3,6,1,4,1,8886,1,35,1,3,1,7),_RaisecomBfdSessPerfEchoPktDrop_Type())
raisecomBfdSessPerfEchoPktDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfEchoPktDrop.setStatus(_A)
_RaisecomBfdSessPerfEchoPktDropLastTime_Type=TimeStamp
_RaisecomBfdSessPerfEchoPktDropLastTime_Object=MibTableColumn
raisecomBfdSessPerfEchoPktDropLastTime=_RaisecomBfdSessPerfEchoPktDropLastTime_Object((1,3,6,1,4,1,8886,1,35,1,3,1,8),_RaisecomBfdSessPerfEchoPktDropLastTime_Type())
raisecomBfdSessPerfEchoPktDropLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfEchoPktDropLastTime.setStatus(_A)
_RaisecomBfdSessUpTime_Type=TimeStamp
_RaisecomBfdSessUpTime_Object=MibTableColumn
raisecomBfdSessUpTime=_RaisecomBfdSessUpTime_Object((1,3,6,1,4,1,8886,1,35,1,3,1,9),_RaisecomBfdSessUpTime_Type())
raisecomBfdSessUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessUpTime.setStatus(_A)
_RaisecomBfdSessPerfLastSessDownTime_Type=TimeStamp
_RaisecomBfdSessPerfLastSessDownTime_Object=MibTableColumn
raisecomBfdSessPerfLastSessDownTime=_RaisecomBfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,8886,1,35,1,3,1,10),_RaisecomBfdSessPerfLastSessDownTime_Type())
raisecomBfdSessPerfLastSessDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfLastSessDownTime.setStatus(_A)
_RaisecomBfdSessPerfLastCommLostDiag_Type=BfdDiagTC
_RaisecomBfdSessPerfLastCommLostDiag_Object=MibTableColumn
raisecomBfdSessPerfLastCommLostDiag=_RaisecomBfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,8886,1,35,1,3,1,11),_RaisecomBfdSessPerfLastCommLostDiag_Type())
raisecomBfdSessPerfLastCommLostDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfLastCommLostDiag.setStatus(_A)
_RaisecomBfdSessPerfSessUpCount_Type=Counter32
_RaisecomBfdSessPerfSessUpCount_Object=MibTableColumn
raisecomBfdSessPerfSessUpCount=_RaisecomBfdSessPerfSessUpCount_Object((1,3,6,1,4,1,8886,1,35,1,3,1,12),_RaisecomBfdSessPerfSessUpCount_Type())
raisecomBfdSessPerfSessUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfSessUpCount.setStatus(_A)
_RaisecomBfdSessPerfDiscTime_Type=TimeStamp
_RaisecomBfdSessPerfDiscTime_Object=MibTableColumn
raisecomBfdSessPerfDiscTime=_RaisecomBfdSessPerfDiscTime_Object((1,3,6,1,4,1,8886,1,35,1,3,1,13),_RaisecomBfdSessPerfDiscTime_Type())
raisecomBfdSessPerfDiscTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfDiscTime.setStatus(_A)
_RaisecomBfdSessPerfCtrlPktInHC_Type=Counter64
_RaisecomBfdSessPerfCtrlPktInHC_Object=MibTableColumn
raisecomBfdSessPerfCtrlPktInHC=_RaisecomBfdSessPerfCtrlPktInHC_Object((1,3,6,1,4,1,8886,1,35,1,3,1,14),_RaisecomBfdSessPerfCtrlPktInHC_Type())
raisecomBfdSessPerfCtrlPktInHC.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfCtrlPktInHC.setStatus(_A)
_RaisecomBfdSessPerfCtrlPktOutHC_Type=Counter64
_RaisecomBfdSessPerfCtrlPktOutHC_Object=MibTableColumn
raisecomBfdSessPerfCtrlPktOutHC=_RaisecomBfdSessPerfCtrlPktOutHC_Object((1,3,6,1,4,1,8886,1,35,1,3,1,15),_RaisecomBfdSessPerfCtrlPktOutHC_Type())
raisecomBfdSessPerfCtrlPktOutHC.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfCtrlPktOutHC.setStatus(_A)
_RaisecomBfdSessPerfCtrlPktDropHC_Type=Counter64
_RaisecomBfdSessPerfCtrlPktDropHC_Object=MibTableColumn
raisecomBfdSessPerfCtrlPktDropHC=_RaisecomBfdSessPerfCtrlPktDropHC_Object((1,3,6,1,4,1,8886,1,35,1,3,1,16),_RaisecomBfdSessPerfCtrlPktDropHC_Type())
raisecomBfdSessPerfCtrlPktDropHC.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfCtrlPktDropHC.setStatus(_A)
_RaisecomBfdSessPerfEchoPktInHC_Type=Counter64
_RaisecomBfdSessPerfEchoPktInHC_Object=MibTableColumn
raisecomBfdSessPerfEchoPktInHC=_RaisecomBfdSessPerfEchoPktInHC_Object((1,3,6,1,4,1,8886,1,35,1,3,1,17),_RaisecomBfdSessPerfEchoPktInHC_Type())
raisecomBfdSessPerfEchoPktInHC.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfEchoPktInHC.setStatus(_A)
_RaisecomBfdSessPerfEchoPktOutHC_Type=Counter64
_RaisecomBfdSessPerfEchoPktOutHC_Object=MibTableColumn
raisecomBfdSessPerfEchoPktOutHC=_RaisecomBfdSessPerfEchoPktOutHC_Object((1,3,6,1,4,1,8886,1,35,1,3,1,18),_RaisecomBfdSessPerfEchoPktOutHC_Type())
raisecomBfdSessPerfEchoPktOutHC.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfEchoPktOutHC.setStatus(_A)
_RaisecomBfdSessPerfEchoPktDropHC_Type=Counter64
_RaisecomBfdSessPerfEchoPktDropHC_Object=MibTableColumn
raisecomBfdSessPerfEchoPktDropHC=_RaisecomBfdSessPerfEchoPktDropHC_Object((1,3,6,1,4,1,8886,1,35,1,3,1,19),_RaisecomBfdSessPerfEchoPktDropHC_Type())
raisecomBfdSessPerfEchoPktDropHC.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessPerfEchoPktDropHC.setStatus(_A)
_RaisecomBfdSessDiscMapTable_Object=MibTable
raisecomBfdSessDiscMapTable=_RaisecomBfdSessDiscMapTable_Object((1,3,6,1,4,1,8886,1,35,1,4))
if mibBuilder.loadTexts:raisecomBfdSessDiscMapTable.setStatus(_A)
_RaisecomBfdSessDiscMapEntry_Object=MibTableRow
raisecomBfdSessDiscMapEntry=_RaisecomBfdSessDiscMapEntry_Object((1,3,6,1,4,1,8886,1,35,1,4,1))
raisecomBfdSessDiscMapEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:raisecomBfdSessDiscMapEntry.setStatus(_A)
_RaisecomBfdSessDiscMapIndex_Type=BfdSessIndexTC
_RaisecomBfdSessDiscMapIndex_Object=MibTableColumn
raisecomBfdSessDiscMapIndex=_RaisecomBfdSessDiscMapIndex_Object((1,3,6,1,4,1,8886,1,35,1,4,1,1),_RaisecomBfdSessDiscMapIndex_Type())
raisecomBfdSessDiscMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessDiscMapIndex.setStatus(_A)
_RaisecomBfdSessIpMapTable_Object=MibTable
raisecomBfdSessIpMapTable=_RaisecomBfdSessIpMapTable_Object((1,3,6,1,4,1,8886,1,35,1,5))
if mibBuilder.loadTexts:raisecomBfdSessIpMapTable.setStatus(_A)
_RaisecomBfdSessIpMapEntry_Object=MibTableRow
raisecomBfdSessIpMapEntry=_RaisecomBfdSessIpMapEntry_Object((1,3,6,1,4,1,8886,1,35,1,5,1))
raisecomBfdSessIpMapEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_E,_V),(0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:raisecomBfdSessIpMapEntry.setStatus(_A)
_RaisecomBfdSessIpMapIndex_Type=BfdSessIndexTC
_RaisecomBfdSessIpMapIndex_Object=MibTableColumn
raisecomBfdSessIpMapIndex=_RaisecomBfdSessIpMapIndex_Object((1,3,6,1,4,1,8886,1,35,1,5,1,1),_RaisecomBfdSessIpMapIndex_Type())
raisecomBfdSessIpMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomBfdSessIpMapIndex.setStatus(_A)
_RaisecomBfdIfTable_Object=MibTable
raisecomBfdIfTable=_RaisecomBfdIfTable_Object((1,3,6,1,4,1,8886,1,35,1,6))
if mibBuilder.loadTexts:raisecomBfdIfTable.setStatus(_A)
_RaisecomBfdIfEntry_Object=MibTableRow
raisecomBfdIfEntry=_RaisecomBfdIfEntry_Object((1,3,6,1,4,1,8886,1,35,1,6,1))
raisecomBfdIfEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:raisecomBfdIfEntry.setStatus(_A)
_RaisecomBfdIfIndex_Type=Unsigned32
_RaisecomBfdIfIndex_Object=MibTableColumn
raisecomBfdIfIndex=_RaisecomBfdIfIndex_Object((1,3,6,1,4,1,8886,1,35,1,6,1,1),_RaisecomBfdIfIndex_Type())
raisecomBfdIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomBfdIfIndex.setStatus(_A)
class _RaisecomBfdIfDesiredMinTxInterval_Type(Unsigned32):defaultValue=500
_RaisecomBfdIfDesiredMinTxInterval_Type.__name__=_F
_RaisecomBfdIfDesiredMinTxInterval_Object=MibTableColumn
raisecomBfdIfDesiredMinTxInterval=_RaisecomBfdIfDesiredMinTxInterval_Object((1,3,6,1,4,1,8886,1,35,1,6,1,2),_RaisecomBfdIfDesiredMinTxInterval_Type())
raisecomBfdIfDesiredMinTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfDesiredMinTxInterval.setStatus(_A)
class _RaisecomBfdIfReqMinRxInterval_Type(Unsigned32):defaultValue=500
_RaisecomBfdIfReqMinRxInterval_Type.__name__=_F
_RaisecomBfdIfReqMinRxInterval_Object=MibTableColumn
raisecomBfdIfReqMinRxInterval=_RaisecomBfdIfReqMinRxInterval_Object((1,3,6,1,4,1,8886,1,35,1,6,1,3),_RaisecomBfdIfReqMinRxInterval_Type())
raisecomBfdIfReqMinRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfReqMinRxInterval.setStatus(_A)
class _RaisecomBfdIfDetectMult_Type(Unsigned32):defaultValue=3
_RaisecomBfdIfDetectMult_Type.__name__=_F
_RaisecomBfdIfDetectMult_Object=MibTableColumn
raisecomBfdIfDetectMult=_RaisecomBfdIfDetectMult_Object((1,3,6,1,4,1,8886,1,35,1,6,1,4),_RaisecomBfdIfDetectMult_Type())
raisecomBfdIfDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfDetectMult.setStatus(_A)
class _RaisecomBfdIfReqMinEchoRxInterval_Type(Unsigned32):defaultValue=500
_RaisecomBfdIfReqMinEchoRxInterval_Type.__name__=_F
_RaisecomBfdIfReqMinEchoRxInterval_Object=MibTableColumn
raisecomBfdIfReqMinEchoRxInterval=_RaisecomBfdIfReqMinEchoRxInterval_Object((1,3,6,1,4,1,8886,1,35,1,6,1,5),_RaisecomBfdIfReqMinEchoRxInterval_Type())
raisecomBfdIfReqMinEchoRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfReqMinEchoRxInterval.setStatus(_A)
class _RaisecomBfdIfAuthPresFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdIfAuthPresFlag_Type.__name__=_G
_RaisecomBfdIfAuthPresFlag_Object=MibTableColumn
raisecomBfdIfAuthPresFlag=_RaisecomBfdIfAuthPresFlag_Object((1,3,6,1,4,1,8886,1,35,1,6,1,6),_RaisecomBfdIfAuthPresFlag_Type())
raisecomBfdIfAuthPresFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfAuthPresFlag.setStatus(_A)
class _RaisecomBfdIfAuthenticationType_Type(BfdSessAuthenticationTypeTC):defaultValue=-1
_RaisecomBfdIfAuthenticationType_Type.__name__=_J
_RaisecomBfdIfAuthenticationType_Object=MibTableColumn
raisecomBfdIfAuthenticationType=_RaisecomBfdIfAuthenticationType_Object((1,3,6,1,4,1,8886,1,35,1,6,1,7),_RaisecomBfdIfAuthenticationType_Type())
raisecomBfdIfAuthenticationType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfAuthenticationType.setStatus(_A)
class _RaisecomBfdIfAuthenticationKeyID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_RaisecomBfdIfAuthenticationKeyID_Type.__name__=_H
_RaisecomBfdIfAuthenticationKeyID_Object=MibTableColumn
raisecomBfdIfAuthenticationKeyID=_RaisecomBfdIfAuthenticationKeyID_Object((1,3,6,1,4,1,8886,1,35,1,6,1,8),_RaisecomBfdIfAuthenticationKeyID_Type())
raisecomBfdIfAuthenticationKeyID.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfAuthenticationKeyID.setStatus(_A)
_RaisecomBfdIfAuthenticationKey_Type=BfdSessionAuthenticationKeyTC
_RaisecomBfdIfAuthenticationKey_Object=MibTableColumn
raisecomBfdIfAuthenticationKey=_RaisecomBfdIfAuthenticationKey_Object((1,3,6,1,4,1,8886,1,35,1,6,1,9),_RaisecomBfdIfAuthenticationKey_Type())
raisecomBfdIfAuthenticationKey.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfAuthenticationKey.setStatus(_A)
class _RaisecomBfdIfDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdIfDemandModeDesiredFlag_Type.__name__=_G
_RaisecomBfdIfDemandModeDesiredFlag_Object=MibTableColumn
raisecomBfdIfDemandModeDesiredFlag=_RaisecomBfdIfDemandModeDesiredFlag_Object((1,3,6,1,4,1,8886,1,35,1,6,1,10),_RaisecomBfdIfDemandModeDesiredFlag_Type())
raisecomBfdIfDemandModeDesiredFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdIfDemandModeDesiredFlag.setStatus(_A)
_RaisecomBfdTemplateTable_Object=MibTable
raisecomBfdTemplateTable=_RaisecomBfdTemplateTable_Object((1,3,6,1,4,1,8886,1,35,1,7))
if mibBuilder.loadTexts:raisecomBfdTemplateTable.setStatus(_A)
_RaisecomBfdTemplateEntry_Object=MibTableRow
raisecomBfdTemplateEntry=_RaisecomBfdTemplateEntry_Object((1,3,6,1,4,1,8886,1,35,1,7,1))
raisecomBfdTemplateEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:raisecomBfdTemplateEntry.setStatus(_A)
class _RaisecomBfdTemplateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomBfdTemplateName_Type.__name__=_K
_RaisecomBfdTemplateName_Object=MibTableColumn
raisecomBfdTemplateName=_RaisecomBfdTemplateName_Object((1,3,6,1,4,1,8886,1,35,1,7,1,1),_RaisecomBfdTemplateName_Type())
raisecomBfdTemplateName.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomBfdTemplateName.setStatus(_A)
_RaisecomBfdTemplateType_Type=BfdSessTypeTC
_RaisecomBfdTemplateType_Object=MibTableColumn
raisecomBfdTemplateType=_RaisecomBfdTemplateType_Object((1,3,6,1,4,1,8886,1,35,1,7,1,2),_RaisecomBfdTemplateType_Type())
raisecomBfdTemplateType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdTemplateType.setStatus(_A)
class _RaisecomBfdTemplateDesiredMinTxInterval_Type(Unsigned32):defaultValue=500
_RaisecomBfdTemplateDesiredMinTxInterval_Type.__name__=_F
_RaisecomBfdTemplateDesiredMinTxInterval_Object=MibTableColumn
raisecomBfdTemplateDesiredMinTxInterval=_RaisecomBfdTemplateDesiredMinTxInterval_Object((1,3,6,1,4,1,8886,1,35,1,7,1,3),_RaisecomBfdTemplateDesiredMinTxInterval_Type())
raisecomBfdTemplateDesiredMinTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdTemplateDesiredMinTxInterval.setStatus(_A)
class _RaisecomBfdTemplateReqMinRxInterval_Type(Unsigned32):defaultValue=500
_RaisecomBfdTemplateReqMinRxInterval_Type.__name__=_F
_RaisecomBfdTemplateReqMinRxInterval_Object=MibTableColumn
raisecomBfdTemplateReqMinRxInterval=_RaisecomBfdTemplateReqMinRxInterval_Object((1,3,6,1,4,1,8886,1,35,1,7,1,4),_RaisecomBfdTemplateReqMinRxInterval_Type())
raisecomBfdTemplateReqMinRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdTemplateReqMinRxInterval.setStatus(_A)
class _RaisecomBfdTemplateDetectMult_Type(Unsigned32):defaultValue=3
_RaisecomBfdTemplateDetectMult_Type.__name__=_F
_RaisecomBfdTemplateDetectMult_Object=MibTableColumn
raisecomBfdTemplateDetectMult=_RaisecomBfdTemplateDetectMult_Object((1,3,6,1,4,1,8886,1,35,1,7,1,5),_RaisecomBfdTemplateDetectMult_Type())
raisecomBfdTemplateDetectMult.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdTemplateDetectMult.setStatus(_A)
class _RaisecomBfdTemplateAuthPresFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdTemplateAuthPresFlag_Type.__name__=_G
_RaisecomBfdTemplateAuthPresFlag_Object=MibTableColumn
raisecomBfdTemplateAuthPresFlag=_RaisecomBfdTemplateAuthPresFlag_Object((1,3,6,1,4,1,8886,1,35,1,7,1,6),_RaisecomBfdTemplateAuthPresFlag_Type())
raisecomBfdTemplateAuthPresFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdTemplateAuthPresFlag.setStatus(_A)
class _RaisecomBfdTemplateAuthenticationType_Type(BfdSessAuthenticationTypeTC):defaultValue=-1
_RaisecomBfdTemplateAuthenticationType_Type.__name__=_J
_RaisecomBfdTemplateAuthenticationType_Object=MibTableColumn
raisecomBfdTemplateAuthenticationType=_RaisecomBfdTemplateAuthenticationType_Object((1,3,6,1,4,1,8886,1,35,1,7,1,7),_RaisecomBfdTemplateAuthenticationType_Type())
raisecomBfdTemplateAuthenticationType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdTemplateAuthenticationType.setStatus(_A)
class _RaisecomBfdTemplateAuthenticationKeyID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_RaisecomBfdTemplateAuthenticationKeyID_Type.__name__=_H
_RaisecomBfdTemplateAuthenticationKeyID_Object=MibTableColumn
raisecomBfdTemplateAuthenticationKeyID=_RaisecomBfdTemplateAuthenticationKeyID_Object((1,3,6,1,4,1,8886,1,35,1,7,1,8),_RaisecomBfdTemplateAuthenticationKeyID_Type())
raisecomBfdTemplateAuthenticationKeyID.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdTemplateAuthenticationKeyID.setStatus(_A)
_RaisecomBfdTemplateAuthenticationKey_Type=BfdSessionAuthenticationKeyTC
_RaisecomBfdTemplateAuthenticationKey_Object=MibTableColumn
raisecomBfdTemplateAuthenticationKey=_RaisecomBfdTemplateAuthenticationKey_Object((1,3,6,1,4,1,8886,1,35,1,7,1,9),_RaisecomBfdTemplateAuthenticationKey_Type())
raisecomBfdTemplateAuthenticationKey.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdTemplateAuthenticationKey.setStatus(_A)
class _RaisecomBfdTemplateDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_RaisecomBfdTemplateDemandModeDesiredFlag_Type.__name__=_G
_RaisecomBfdTemplateDemandModeDesiredFlag_Object=MibTableColumn
raisecomBfdTemplateDemandModeDesiredFlag=_RaisecomBfdTemplateDemandModeDesiredFlag_Object((1,3,6,1,4,1,8886,1,35,1,7,1,10),_RaisecomBfdTemplateDemandModeDesiredFlag_Type())
raisecomBfdTemplateDemandModeDesiredFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomBfdTemplateDemandModeDesiredFlag.setStatus(_A)
_RaisecomBfdTemplateRowStatus_Type=RowStatus
_RaisecomBfdTemplateRowStatus_Object=MibTableColumn
raisecomBfdTemplateRowStatus=_RaisecomBfdTemplateRowStatus_Object((1,3,6,1,4,1,8886,1,35,1,7,1,11),_RaisecomBfdTemplateRowStatus_Type())
raisecomBfdTemplateRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomBfdTemplateRowStatus.setStatus(_A)
_RaisecomBfdConformance_ObjectIdentity=ObjectIdentity
raisecomBfdConformance=_RaisecomBfdConformance_ObjectIdentity((1,3,6,1,4,1,8886,1,35,2))
_RaisecomBfdGroups_ObjectIdentity=ObjectIdentity
raisecomBfdGroups=_RaisecomBfdGroups_ObjectIdentity((1,3,6,1,4,1,8886,1,35,2,1))
_RaisecomBfdCompliances_ObjectIdentity=ObjectIdentity
raisecomBfdCompliances=_RaisecomBfdCompliances_ObjectIdentity((1,3,6,1,4,1,8886,1,35,2,2))
raisecomBfdSessEntry.registerAugmentions((_E,_a))
raisecomBfdSessPerfEntry.setIndexNames(*raisecomBfdSessEntry.getIndexNames())
raisecomBfdSessUp=NotificationType((1,3,6,1,4,1,8886,1,35,0,1))
raisecomBfdSessUp.setObjects(*((_E,_I),(_E,_I)))
if mibBuilder.loadTexts:raisecomBfdSessUp.setStatus(_A)
raisecomBfdSessDown=NotificationType((1,3,6,1,4,1,8886,1,35,0,2))
raisecomBfdSessDown.setObjects(*((_E,_I),(_E,_I)))
if mibBuilder.loadTexts:raisecomBfdSessDown.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'BfdSessIndexTC':BfdSessIndexTC,'BfdIntervalTC':BfdIntervalTC,'BfdMultiplierTC':BfdMultiplierTC,'BfdDiagTC':BfdDiagTC,'BfdSessTypeTC':BfdSessTypeTC,'BfdSessOperModeTC':BfdSessOperModeTC,_P:BfdCtrlDestPortNumberTC,_Q:BfdCtrlSourcePortNumberTC,_R:BfdSessStateTC,_J:BfdSessAuthenticationTypeTC,'BfdSessionAuthenticationKeyTC':BfdSessionAuthenticationKeyTC,'raisecomBfd':raisecomBfd,'raisecomBfdNotifications':raisecomBfdNotifications,'raisecomBfdSessUp':raisecomBfdSessUp,'raisecomBfdSessDown':raisecomBfdSessDown,'raisecomBfdObjects':raisecomBfdObjects,'raisecomBfdScalarObjects':raisecomBfdScalarObjects,'raisecomBfdAdminStatus':raisecomBfdAdminStatus,'raisecomBfdSessNotificationsEnable':raisecomBfdSessNotificationsEnable,'raisecomBfdRoleMode':raisecomBfdRoleMode,'raisecomBfdEchoSourceIpType':raisecomBfdEchoSourceIpType,'raisecomBfdEchoSourceIpAddr':raisecomBfdEchoSourceIpAddr,'raisecomBfdAllSessionsStatisticsClear':raisecomBfdAllSessionsStatisticsClear,'raisecomBfdSessTable':raisecomBfdSessTable,'raisecomBfdSessEntry':raisecomBfdSessEntry,_O:raisecomBfdSessIndex,'raisecomBfdSessVersionNumber':raisecomBfdSessVersionNumber,'raisecomBfdSessType':raisecomBfdSessType,_S:raisecomBfdSessDiscriminator,'raisecomBfdSessRemoteDiscr':raisecomBfdSessRemoteDiscr,'raisecomBfdSessDestinationUdpPort':raisecomBfdSessDestinationUdpPort,'raisecomBfdSessSourceUdpPort':raisecomBfdSessSourceUdpPort,'raisecomBfdSessEchoSourceUdpPort':raisecomBfdSessEchoSourceUdpPort,'raisecomBfdSessAdminStatus':raisecomBfdSessAdminStatus,'raisecomBfdSessState':raisecomBfdSessState,'raisecomBfdSessRemoteHeardFlag':raisecomBfdSessRemoteHeardFlag,_I:raisecomBfdSessDiag,'raisecomBfdSessOperMode':raisecomBfdSessOperMode,'raisecomBfdSessDemandModeDesiredFlag':raisecomBfdSessDemandModeDesiredFlag,'raisecomBfdSessControlPlaneIndepFlag':raisecomBfdSessControlPlaneIndepFlag,'raisecomBfdSessMultipointFlag':raisecomBfdSessMultipointFlag,_T:raisecomBfdSessInterface,_U:raisecomBfdSessSrcAddrType,_V:raisecomBfdSessSrcAddr,_W:raisecomBfdSessDstAddrType,_X:raisecomBfdSessDstAddr,'raisecomBfdSessGTSM':raisecomBfdSessGTSM,'raisecomBfdSessGTSMTTL':raisecomBfdSessGTSMTTL,'raisecomBfdSessDesiredMinTxInterval':raisecomBfdSessDesiredMinTxInterval,'raisecomBfdSessReqMinRxInterval':raisecomBfdSessReqMinRxInterval,'raisecomBfdSessReqMinEchoRxInterval':raisecomBfdSessReqMinEchoRxInterval,'raisecomBfdSessDetectMult':raisecomBfdSessDetectMult,'raisecomBfdSessNegotiatedInterval':raisecomBfdSessNegotiatedInterval,'raisecomBfdSessNegotiatedEchoInterval':raisecomBfdSessNegotiatedEchoInterval,'raisecomBfdSessNegotiatedDetectMult':raisecomBfdSessNegotiatedDetectMult,'raisecomBfdSessAuthPresFlag':raisecomBfdSessAuthPresFlag,'raisecomBfdSessAuthenticationType':raisecomBfdSessAuthenticationType,'raisecomBfdSessAuthenticationKeyID':raisecomBfdSessAuthenticationKeyID,'raisecomBfdSessAuthenticationKey':raisecomBfdSessAuthenticationKey,'raisecomBfdSessStorType':raisecomBfdSessStorType,'raisecomBfdSessRowStatus':raisecomBfdSessRowStatus,'raisecomBfdSessTemplateName':raisecomBfdSessTemplateName,'raisecomBfdSessPerfTable':raisecomBfdSessPerfTable,_a:raisecomBfdSessPerfEntry,'raisecomBfdSessPerfCtrlPktIn':raisecomBfdSessPerfCtrlPktIn,'raisecomBfdSessPerfCtrlPktOut':raisecomBfdSessPerfCtrlPktOut,'raisecomBfdSessPerfCtrlPktDrop':raisecomBfdSessPerfCtrlPktDrop,'raisecomBfdSessPerfCtrlPktDropLastTime':raisecomBfdSessPerfCtrlPktDropLastTime,'raisecomBfdSessPerfEchoPktIn':raisecomBfdSessPerfEchoPktIn,'raisecomBfdSessPerfEchoPktOut':raisecomBfdSessPerfEchoPktOut,'raisecomBfdSessPerfEchoPktDrop':raisecomBfdSessPerfEchoPktDrop,'raisecomBfdSessPerfEchoPktDropLastTime':raisecomBfdSessPerfEchoPktDropLastTime,'raisecomBfdSessUpTime':raisecomBfdSessUpTime,'raisecomBfdSessPerfLastSessDownTime':raisecomBfdSessPerfLastSessDownTime,'raisecomBfdSessPerfLastCommLostDiag':raisecomBfdSessPerfLastCommLostDiag,'raisecomBfdSessPerfSessUpCount':raisecomBfdSessPerfSessUpCount,'raisecomBfdSessPerfDiscTime':raisecomBfdSessPerfDiscTime,'raisecomBfdSessPerfCtrlPktInHC':raisecomBfdSessPerfCtrlPktInHC,'raisecomBfdSessPerfCtrlPktOutHC':raisecomBfdSessPerfCtrlPktOutHC,'raisecomBfdSessPerfCtrlPktDropHC':raisecomBfdSessPerfCtrlPktDropHC,'raisecomBfdSessPerfEchoPktInHC':raisecomBfdSessPerfEchoPktInHC,'raisecomBfdSessPerfEchoPktOutHC':raisecomBfdSessPerfEchoPktOutHC,'raisecomBfdSessPerfEchoPktDropHC':raisecomBfdSessPerfEchoPktDropHC,'raisecomBfdSessDiscMapTable':raisecomBfdSessDiscMapTable,'raisecomBfdSessDiscMapEntry':raisecomBfdSessDiscMapEntry,'raisecomBfdSessDiscMapIndex':raisecomBfdSessDiscMapIndex,'raisecomBfdSessIpMapTable':raisecomBfdSessIpMapTable,'raisecomBfdSessIpMapEntry':raisecomBfdSessIpMapEntry,'raisecomBfdSessIpMapIndex':raisecomBfdSessIpMapIndex,'raisecomBfdIfTable':raisecomBfdIfTable,'raisecomBfdIfEntry':raisecomBfdIfEntry,_Y:raisecomBfdIfIndex,'raisecomBfdIfDesiredMinTxInterval':raisecomBfdIfDesiredMinTxInterval,'raisecomBfdIfReqMinRxInterval':raisecomBfdIfReqMinRxInterval,'raisecomBfdIfDetectMult':raisecomBfdIfDetectMult,'raisecomBfdIfReqMinEchoRxInterval':raisecomBfdIfReqMinEchoRxInterval,'raisecomBfdIfAuthPresFlag':raisecomBfdIfAuthPresFlag,'raisecomBfdIfAuthenticationType':raisecomBfdIfAuthenticationType,'raisecomBfdIfAuthenticationKeyID':raisecomBfdIfAuthenticationKeyID,'raisecomBfdIfAuthenticationKey':raisecomBfdIfAuthenticationKey,'raisecomBfdIfDemandModeDesiredFlag':raisecomBfdIfDemandModeDesiredFlag,'raisecomBfdTemplateTable':raisecomBfdTemplateTable,'raisecomBfdTemplateEntry':raisecomBfdTemplateEntry,_Z:raisecomBfdTemplateName,'raisecomBfdTemplateType':raisecomBfdTemplateType,'raisecomBfdTemplateDesiredMinTxInterval':raisecomBfdTemplateDesiredMinTxInterval,'raisecomBfdTemplateReqMinRxInterval':raisecomBfdTemplateReqMinRxInterval,'raisecomBfdTemplateDetectMult':raisecomBfdTemplateDetectMult,'raisecomBfdTemplateAuthPresFlag':raisecomBfdTemplateAuthPresFlag,'raisecomBfdTemplateAuthenticationType':raisecomBfdTemplateAuthenticationType,'raisecomBfdTemplateAuthenticationKeyID':raisecomBfdTemplateAuthenticationKeyID,'raisecomBfdTemplateAuthenticationKey':raisecomBfdTemplateAuthenticationKey,'raisecomBfdTemplateDemandModeDesiredFlag':raisecomBfdTemplateDemandModeDesiredFlag,'raisecomBfdTemplateRowStatus':raisecomBfdTemplateRowStatus,'raisecomBfdConformance':raisecomBfdConformance,'raisecomBfdGroups':raisecomBfdGroups,'raisecomBfdCompliances':raisecomBfdCompliances})