_R='zxAnBfdStdSessPerfEntry'
_Q='zxAnBfdStdSessPeerIpAddress'
_P='zxAnBfdStdSessPeerIpAddressType'
_O='zxAnBfdStdSessIfIndex'
_N='zxAnBfdStdSessDiscIndex'
_M='zxAnBfdStdSessIndex'
_L='read-write'
_K='OctetString'
_J='InetPortNumber'
_I='zxAnBfdStdSessDiag'
_H='not-accessible'
_G='Unsigned32'
_F='TruthValue'
_E='Integer32'
_D='ZTE-AN-BFD-STD-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_F)
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnBfdStdMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,16))
if mibBuilder.loadTexts:zxAnBfdStdMib.setRevisions(('2010-03-03 12:00',))
class ZxAnBfdStdSessIndexTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class ZxAnBfdStdInterval(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class ZxAnBfdStdMultiplier(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class ZxAnBfdStdDiag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,99)));namedValues=NamedValues(*(('controlDetectionTimeExpired',1),('echoFunctionFailed',2),('neighborSignaledSessionDown',3),('forwardingPlaneReset',4),('pathDown',5),('concatenatedPathDown',6),('administrativelyDown',7),('reverseConcatenatedPathDown',8),('noDiagnostic',99)))
_ZxAnBfdStdNotifications_ObjectIdentity=ObjectIdentity
zxAnBfdStdNotifications=_ZxAnBfdStdNotifications_ObjectIdentity((1,3,6,1,4,1,3902,1015,16,0))
_ZxAnBfdStdObjects_ObjectIdentity=ObjectIdentity
zxAnBfdStdObjects=_ZxAnBfdStdObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,16,1))
_ZxAnBfdStdGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnBfdStdGlobalObjects=_ZxAnBfdStdGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,16,1,1))
class _ZxAnBfdStdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ZxAnBfdStdAdminStatus_Type.__name__=_E
_ZxAnBfdStdAdminStatus_Object=MibScalar
zxAnBfdStdAdminStatus=_ZxAnBfdStdAdminStatus_Object((1,3,6,1,4,1,3902,1015,16,1,1,1),_ZxAnBfdStdAdminStatus_Type())
zxAnBfdStdAdminStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnBfdStdAdminStatus.setStatus(_A)
class _ZxAnBfdStdSessTrapsEnable_Type(TruthValue):defaultValue=2
_ZxAnBfdStdSessTrapsEnable_Type.__name__=_F
_ZxAnBfdStdSessTrapsEnable_Object=MibScalar
zxAnBfdStdSessTrapsEnable=_ZxAnBfdStdSessTrapsEnable_Object((1,3,6,1,4,1,3902,1015,16,1,1,2),_ZxAnBfdStdSessTrapsEnable_Type())
zxAnBfdStdSessTrapsEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnBfdStdSessTrapsEnable.setStatus(_A)
_ZxAnBfdStdSessTable_Object=MibTable
zxAnBfdStdSessTable=_ZxAnBfdStdSessTable_Object((1,3,6,1,4,1,3902,1015,16,1,2))
if mibBuilder.loadTexts:zxAnBfdStdSessTable.setStatus(_A)
_ZxAnBfdStdSessEntry_Object=MibTableRow
zxAnBfdStdSessEntry=_ZxAnBfdStdSessEntry_Object((1,3,6,1,4,1,3902,1015,16,1,2,1))
zxAnBfdStdSessEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:zxAnBfdStdSessEntry.setStatus(_A)
_ZxAnBfdStdSessIndex_Type=ZxAnBfdStdSessIndexTC
_ZxAnBfdStdSessIndex_Object=MibTableColumn
zxAnBfdStdSessIndex=_ZxAnBfdStdSessIndex_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,1),_ZxAnBfdStdSessIndex_Type())
zxAnBfdStdSessIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnBfdStdSessIndex.setStatus(_A)
class _ZxAnBfdStdSessVersionNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnBfdStdSessVersionNumber_Type.__name__=_G
_ZxAnBfdStdSessVersionNumber_Object=MibTableColumn
zxAnBfdStdSessVersionNumber=_ZxAnBfdStdSessVersionNumber_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,2),_ZxAnBfdStdSessVersionNumber_Type())
zxAnBfdStdSessVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessVersionNumber.setStatus(_A)
class _ZxAnBfdStdSessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('singleHop',1),('multiHopTotallyArbitraryPaths',2),('multiHopOutOfBandSignaling',3),('multiHopUnidirectionalLinks',4)))
_ZxAnBfdStdSessType_Type.__name__=_E
_ZxAnBfdStdSessType_Object=MibTableColumn
zxAnBfdStdSessType=_ZxAnBfdStdSessType_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,3),_ZxAnBfdStdSessType_Type())
zxAnBfdStdSessType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessType.setStatus(_A)
class _ZxAnBfdStdSessMHopUniLinkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('active',2),('passive',3)))
_ZxAnBfdStdSessMHopUniLinkMode_Type.__name__=_E
_ZxAnBfdStdSessMHopUniLinkMode_Object=MibTableColumn
zxAnBfdStdSessMHopUniLinkMode=_ZxAnBfdStdSessMHopUniLinkMode_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,4),_ZxAnBfdStdSessMHopUniLinkMode_Type())
zxAnBfdStdSessMHopUniLinkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessMHopUniLinkMode.setStatus(_A)
class _ZxAnBfdStdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ZxAnBfdStdSessDiscriminator_Type.__name__=_G
_ZxAnBfdStdSessDiscriminator_Object=MibTableColumn
zxAnBfdStdSessDiscriminator=_ZxAnBfdStdSessDiscriminator_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,5),_ZxAnBfdStdSessDiscriminator_Type())
zxAnBfdStdSessDiscriminator.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessDiscriminator.setStatus(_A)
class _ZxAnBfdStdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_ZxAnBfdStdSessRemoteDiscr_Type.__name__=_G
_ZxAnBfdStdSessRemoteDiscr_Object=MibTableColumn
zxAnBfdStdSessRemoteDiscr=_ZxAnBfdStdSessRemoteDiscr_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,6),_ZxAnBfdStdSessRemoteDiscr_Type())
zxAnBfdStdSessRemoteDiscr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessRemoteDiscr.setStatus(_A)
class _ZxAnBfdStdSessDestinationUdpPort_Type(InetPortNumber):defaultValue=0
_ZxAnBfdStdSessDestinationUdpPort_Type.__name__=_J
_ZxAnBfdStdSessDestinationUdpPort_Object=MibTableColumn
zxAnBfdStdSessDestinationUdpPort=_ZxAnBfdStdSessDestinationUdpPort_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,7),_ZxAnBfdStdSessDestinationUdpPort_Type())
zxAnBfdStdSessDestinationUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessDestinationUdpPort.setStatus(_A)
class _ZxAnBfdStdSessSourceUdpPort_Type(InetPortNumber):defaultValue=0
_ZxAnBfdStdSessSourceUdpPort_Type.__name__=_J
_ZxAnBfdStdSessSourceUdpPort_Object=MibTableColumn
zxAnBfdStdSessSourceUdpPort=_ZxAnBfdStdSessSourceUdpPort_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,8),_ZxAnBfdStdSessSourceUdpPort_Type())
zxAnBfdStdSessSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessSourceUdpPort.setStatus(_A)
class _ZxAnBfdStdSessEchoSourceUdpPort_Type(InetPortNumber):defaultValue=0
_ZxAnBfdStdSessEchoSourceUdpPort_Type.__name__=_J
_ZxAnBfdStdSessEchoSourceUdpPort_Object=MibTableColumn
zxAnBfdStdSessEchoSourceUdpPort=_ZxAnBfdStdSessEchoSourceUdpPort_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,9),_ZxAnBfdStdSessEchoSourceUdpPort_Type())
zxAnBfdStdSessEchoSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessEchoSourceUdpPort.setStatus(_A)
class _ZxAnBfdStdSessAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_ZxAnBfdStdSessAdminStatus_Type.__name__=_E
_ZxAnBfdStdSessAdminStatus_Object=MibTableColumn
zxAnBfdStdSessAdminStatus=_ZxAnBfdStdSessAdminStatus_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,10),_ZxAnBfdStdSessAdminStatus_Type())
zxAnBfdStdSessAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessAdminStatus.setStatus(_A)
class _ZxAnBfdStdSessState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4),('failing',5)))
_ZxAnBfdStdSessState_Type.__name__=_E
_ZxAnBfdStdSessState_Object=MibTableColumn
zxAnBfdStdSessState=_ZxAnBfdStdSessState_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,11),_ZxAnBfdStdSessState_Type())
zxAnBfdStdSessState.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessState.setStatus(_A)
class _ZxAnBfdStdSessRemoteHeardFlag_Type(TruthValue):defaultValue=2
_ZxAnBfdStdSessRemoteHeardFlag_Type.__name__=_F
_ZxAnBfdStdSessRemoteHeardFlag_Object=MibTableColumn
zxAnBfdStdSessRemoteHeardFlag=_ZxAnBfdStdSessRemoteHeardFlag_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,12),_ZxAnBfdStdSessRemoteHeardFlag_Type())
zxAnBfdStdSessRemoteHeardFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessRemoteHeardFlag.setStatus(_A)
_ZxAnBfdStdSessDiag_Type=ZxAnBfdStdDiag
_ZxAnBfdStdSessDiag_Object=MibTableColumn
zxAnBfdStdSessDiag=_ZxAnBfdStdSessDiag_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,13),_ZxAnBfdStdSessDiag_Type())
zxAnBfdStdSessDiag.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:zxAnBfdStdSessDiag.setStatus(_A)
class _ZxAnBfdStdSessOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asyncModeWEchoFunction',1),('asynchModeWOEchoFunction',2),('demandModeWEchoFunction',3),('demandModeWOEchoFunction',4)))
_ZxAnBfdStdSessOperMode_Type.__name__=_E
_ZxAnBfdStdSessOperMode_Object=MibTableColumn
zxAnBfdStdSessOperMode=_ZxAnBfdStdSessOperMode_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,14),_ZxAnBfdStdSessOperMode_Type())
zxAnBfdStdSessOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessOperMode.setStatus(_A)
class _ZxAnBfdStdSessDesiredDmdMode_Type(TruthValue):defaultValue=2
_ZxAnBfdStdSessDesiredDmdMode_Type.__name__=_F
_ZxAnBfdStdSessDesiredDmdMode_Object=MibTableColumn
zxAnBfdStdSessDesiredDmdMode=_ZxAnBfdStdSessDesiredDmdMode_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,15),_ZxAnBfdStdSessDesiredDmdMode_Type())
zxAnBfdStdSessDesiredDmdMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessDesiredDmdMode.setStatus(_A)
class _ZxAnBfdStdSessCtrlPlaneIndep_Type(TruthValue):defaultValue=2
_ZxAnBfdStdSessCtrlPlaneIndep_Type.__name__=_F
_ZxAnBfdStdSessCtrlPlaneIndep_Object=MibTableColumn
zxAnBfdStdSessCtrlPlaneIndep=_ZxAnBfdStdSessCtrlPlaneIndep_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,16),_ZxAnBfdStdSessCtrlPlaneIndep_Type())
zxAnBfdStdSessCtrlPlaneIndep.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessCtrlPlaneIndep.setStatus(_A)
class _ZxAnBfdStdSessMultipointFlag_Type(TruthValue):defaultValue=2
_ZxAnBfdStdSessMultipointFlag_Type.__name__=_F
_ZxAnBfdStdSessMultipointFlag_Object=MibTableColumn
zxAnBfdStdSessMultipointFlag=_ZxAnBfdStdSessMultipointFlag_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,17),_ZxAnBfdStdSessMultipointFlag_Type())
zxAnBfdStdSessMultipointFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessMultipointFlag.setStatus(_A)
_ZxAnBfdStdSessInterface_Type=InterfaceIndexOrZero
_ZxAnBfdStdSessInterface_Object=MibTableColumn
zxAnBfdStdSessInterface=_ZxAnBfdStdSessInterface_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,18),_ZxAnBfdStdSessInterface_Type())
zxAnBfdStdSessInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessInterface.setStatus(_A)
_ZxAnBfdStdSessPeerIpAddrType_Type=InetAddressType
_ZxAnBfdStdSessPeerIpAddrType_Object=MibTableColumn
zxAnBfdStdSessPeerIpAddrType=_ZxAnBfdStdSessPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,19),_ZxAnBfdStdSessPeerIpAddrType_Type())
zxAnBfdStdSessPeerIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessPeerIpAddrType.setStatus(_A)
_ZxAnBfdStdSessPeerIpAddr_Type=InetAddress
_ZxAnBfdStdSessPeerIpAddr_Object=MibTableColumn
zxAnBfdStdSessPeerIpAddr=_ZxAnBfdStdSessPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,20),_ZxAnBfdStdSessPeerIpAddr_Type())
zxAnBfdStdSessPeerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessPeerIpAddr.setStatus(_A)
class _ZxAnBfdStdSessGTSM_Type(TruthValue):defaultValue=2
_ZxAnBfdStdSessGTSM_Type.__name__=_F
_ZxAnBfdStdSessGTSM_Object=MibTableColumn
zxAnBfdStdSessGTSM=_ZxAnBfdStdSessGTSM_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,21),_ZxAnBfdStdSessGTSM_Type())
zxAnBfdStdSessGTSM.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessGTSM.setStatus(_A)
class _ZxAnBfdStdSessGTSMTTL_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnBfdStdSessGTSMTTL_Type.__name__=_G
_ZxAnBfdStdSessGTSMTTL_Object=MibTableColumn
zxAnBfdStdSessGTSMTTL=_ZxAnBfdStdSessGTSMTTL_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,22),_ZxAnBfdStdSessGTSMTTL_Type())
zxAnBfdStdSessGTSMTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessGTSMTTL.setStatus(_A)
_ZxAnBfdStdSessDesiredMinTxIntv_Type=ZxAnBfdStdInterval
_ZxAnBfdStdSessDesiredMinTxIntv_Object=MibTableColumn
zxAnBfdStdSessDesiredMinTxIntv=_ZxAnBfdStdSessDesiredMinTxIntv_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,23),_ZxAnBfdStdSessDesiredMinTxIntv_Type())
zxAnBfdStdSessDesiredMinTxIntv.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessDesiredMinTxIntv.setStatus(_A)
_ZxAnBfdStdSessReqMinRxIntv_Type=ZxAnBfdStdInterval
_ZxAnBfdStdSessReqMinRxIntv_Object=MibTableColumn
zxAnBfdStdSessReqMinRxIntv=_ZxAnBfdStdSessReqMinRxIntv_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,24),_ZxAnBfdStdSessReqMinRxIntv_Type())
zxAnBfdStdSessReqMinRxIntv.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessReqMinRxIntv.setStatus(_A)
_ZxAnBfdStdSessReqMinEchoRxIntv_Type=ZxAnBfdStdInterval
_ZxAnBfdStdSessReqMinEchoRxIntv_Object=MibTableColumn
zxAnBfdStdSessReqMinEchoRxIntv=_ZxAnBfdStdSessReqMinEchoRxIntv_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,25),_ZxAnBfdStdSessReqMinEchoRxIntv_Type())
zxAnBfdStdSessReqMinEchoRxIntv.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessReqMinEchoRxIntv.setStatus(_A)
_ZxAnBfdStdSessDetectMult_Type=ZxAnBfdStdMultiplier
_ZxAnBfdStdSessDetectMult_Object=MibTableColumn
zxAnBfdStdSessDetectMult=_ZxAnBfdStdSessDetectMult_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,26),_ZxAnBfdStdSessDetectMult_Type())
zxAnBfdStdSessDetectMult.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessDetectMult.setStatus(_A)
_ZxAnBfdStdSessNegInterval_Type=ZxAnBfdStdInterval
_ZxAnBfdStdSessNegInterval_Object=MibTableColumn
zxAnBfdStdSessNegInterval=_ZxAnBfdStdSessNegInterval_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,27),_ZxAnBfdStdSessNegInterval_Type())
zxAnBfdStdSessNegInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessNegInterval.setStatus(_A)
_ZxAnBfdStdSessNegEchoInterval_Type=ZxAnBfdStdInterval
_ZxAnBfdStdSessNegEchoInterval_Object=MibTableColumn
zxAnBfdStdSessNegEchoInterval=_ZxAnBfdStdSessNegEchoInterval_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,28),_ZxAnBfdStdSessNegEchoInterval_Type())
zxAnBfdStdSessNegEchoInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessNegEchoInterval.setStatus(_A)
_ZxAnBfdStdSessNegDetectMult_Type=ZxAnBfdStdMultiplier
_ZxAnBfdStdSessNegDetectMult_Object=MibTableColumn
zxAnBfdStdSessNegDetectMult=_ZxAnBfdStdSessNegDetectMult_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,29),_ZxAnBfdStdSessNegDetectMult_Type())
zxAnBfdStdSessNegDetectMult.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessNegDetectMult.setStatus(_A)
class _ZxAnBfdStdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_ZxAnBfdStdSessAuthPresFlag_Type.__name__=_F
_ZxAnBfdStdSessAuthPresFlag_Object=MibTableColumn
zxAnBfdStdSessAuthPresFlag=_ZxAnBfdStdSessAuthPresFlag_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,30),_ZxAnBfdStdSessAuthPresFlag_Type())
zxAnBfdStdSessAuthPresFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessAuthPresFlag.setStatus(_A)
class _ZxAnBfdStdSessAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*(('simplePassword',1),('keyedMD5',2),('meticulousKeyedMD5',3),('keyedSHA1',4),('meticulousKeyedSHA1',5),('reserved',99)))
_ZxAnBfdStdSessAuthType_Type.__name__=_E
_ZxAnBfdStdSessAuthType_Object=MibTableColumn
zxAnBfdStdSessAuthType=_ZxAnBfdStdSessAuthType_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,31),_ZxAnBfdStdSessAuthType_Type())
zxAnBfdStdSessAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessAuthType.setStatus(_A)
class _ZxAnBfdStdSessAuthKeyID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_ZxAnBfdStdSessAuthKeyID_Type.__name__=_E
_ZxAnBfdStdSessAuthKeyID_Object=MibTableColumn
zxAnBfdStdSessAuthKeyID=_ZxAnBfdStdSessAuthKeyID_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,32),_ZxAnBfdStdSessAuthKeyID_Type())
zxAnBfdStdSessAuthKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessAuthKeyID.setStatus(_A)
class _ZxAnBfdStdSessAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,252))
_ZxAnBfdStdSessAuthKey_Type.__name__=_K
_ZxAnBfdStdSessAuthKey_Object=MibTableColumn
zxAnBfdStdSessAuthKey=_ZxAnBfdStdSessAuthKey_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,33),_ZxAnBfdStdSessAuthKey_Type())
zxAnBfdStdSessAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessAuthKey.setStatus(_A)
_ZxAnBfdStdSessIpAddrType_Type=InetAddressType
_ZxAnBfdStdSessIpAddrType_Object=MibTableColumn
zxAnBfdStdSessIpAddrType=_ZxAnBfdStdSessIpAddrType_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,34),_ZxAnBfdStdSessIpAddrType_Type())
zxAnBfdStdSessIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessIpAddrType.setStatus(_A)
_ZxAnBfdStdSessIpAddr_Type=InetAddress
_ZxAnBfdStdSessIpAddr_Object=MibTableColumn
zxAnBfdStdSessIpAddr=_ZxAnBfdStdSessIpAddr_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,35),_ZxAnBfdStdSessIpAddr_Type())
zxAnBfdStdSessIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessIpAddr.setStatus(_A)
class _ZxAnBfdStdSessAppType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64,128,256,512,1024,2048)));namedValues=NamedValues(*(('bgp',1),('ospf',2),('isis',4),('rsvp',8),('ldp',16),('static',32),('rsvpLsp',64),('ldpLsp',128),('vrrp',256),('pbr',512),('pw',1024),('pim',2048)))
_ZxAnBfdStdSessAppType_Type.__name__=_E
_ZxAnBfdStdSessAppType_Object=MibTableColumn
zxAnBfdStdSessAppType=_ZxAnBfdStdSessAppType_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,36),_ZxAnBfdStdSessAppType_Type())
zxAnBfdStdSessAppType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessAppType.setStatus(_A)
_ZxAnBfdStdSessStorType_Type=StorageType
_ZxAnBfdStdSessStorType_Object=MibTableColumn
zxAnBfdStdSessStorType=_ZxAnBfdStdSessStorType_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,60),_ZxAnBfdStdSessStorType_Type())
zxAnBfdStdSessStorType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessStorType.setStatus(_A)
_ZxAnBfdStdSessRowStatus_Type=RowStatus
_ZxAnBfdStdSessRowStatus_Object=MibTableColumn
zxAnBfdStdSessRowStatus=_ZxAnBfdStdSessRowStatus_Object((1,3,6,1,4,1,3902,1015,16,1,2,1,61),_ZxAnBfdStdSessRowStatus_Type())
zxAnBfdStdSessRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnBfdStdSessRowStatus.setStatus(_A)
_ZxAnBfdStdSessPerfTable_Object=MibTable
zxAnBfdStdSessPerfTable=_ZxAnBfdStdSessPerfTable_Object((1,3,6,1,4,1,3902,1015,16,1,3))
if mibBuilder.loadTexts:zxAnBfdStdSessPerfTable.setStatus(_A)
_ZxAnBfdStdSessPerfEntry_Object=MibTableRow
zxAnBfdStdSessPerfEntry=_ZxAnBfdStdSessPerfEntry_Object((1,3,6,1,4,1,3902,1015,16,1,3,1))
if mibBuilder.loadTexts:zxAnBfdStdSessPerfEntry.setStatus(_A)
_ZxAnBfdStdSessPerfCtrlPktIn_Type=Counter32
_ZxAnBfdStdSessPerfCtrlPktIn_Object=MibTableColumn
zxAnBfdStdSessPerfCtrlPktIn=_ZxAnBfdStdSessPerfCtrlPktIn_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,1),_ZxAnBfdStdSessPerfCtrlPktIn_Type())
zxAnBfdStdSessPerfCtrlPktIn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfCtrlPktIn.setStatus(_A)
_ZxAnBfdStdSessPerfCtrlPktOut_Type=Counter32
_ZxAnBfdStdSessPerfCtrlPktOut_Object=MibTableColumn
zxAnBfdStdSessPerfCtrlPktOut=_ZxAnBfdStdSessPerfCtrlPktOut_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,2),_ZxAnBfdStdSessPerfCtrlPktOut_Type())
zxAnBfdStdSessPerfCtrlPktOut.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfCtrlPktOut.setStatus(_A)
_ZxAnBfdStdSessPerfCtrlPktDrop_Type=Counter32
_ZxAnBfdStdSessPerfCtrlPktDrop_Object=MibTableColumn
zxAnBfdStdSessPerfCtrlPktDrop=_ZxAnBfdStdSessPerfCtrlPktDrop_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,3),_ZxAnBfdStdSessPerfCtrlPktDrop_Type())
zxAnBfdStdSessPerfCtrlPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfCtrlPktDrop.setStatus(_A)
_ZxAnBfdStdSessPerfCtrlPktDLT_Type=TimeStamp
_ZxAnBfdStdSessPerfCtrlPktDLT_Object=MibTableColumn
zxAnBfdStdSessPerfCtrlPktDLT=_ZxAnBfdStdSessPerfCtrlPktDLT_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,4),_ZxAnBfdStdSessPerfCtrlPktDLT_Type())
zxAnBfdStdSessPerfCtrlPktDLT.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfCtrlPktDLT.setStatus(_A)
_ZxAnBfdStdSessPerfEchoPktIn_Type=Counter32
_ZxAnBfdStdSessPerfEchoPktIn_Object=MibTableColumn
zxAnBfdStdSessPerfEchoPktIn=_ZxAnBfdStdSessPerfEchoPktIn_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,5),_ZxAnBfdStdSessPerfEchoPktIn_Type())
zxAnBfdStdSessPerfEchoPktIn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfEchoPktIn.setStatus(_A)
_ZxAnBfdStdSessPerfEchoPktOut_Type=Counter32
_ZxAnBfdStdSessPerfEchoPktOut_Object=MibTableColumn
zxAnBfdStdSessPerfEchoPktOut=_ZxAnBfdStdSessPerfEchoPktOut_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,6),_ZxAnBfdStdSessPerfEchoPktOut_Type())
zxAnBfdStdSessPerfEchoPktOut.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfEchoPktOut.setStatus(_A)
_ZxAnBfdStdSessPerfEchoPktDrop_Type=Counter32
_ZxAnBfdStdSessPerfEchoPktDrop_Object=MibTableColumn
zxAnBfdStdSessPerfEchoPktDrop=_ZxAnBfdStdSessPerfEchoPktDrop_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,7),_ZxAnBfdStdSessPerfEchoPktDrop_Type())
zxAnBfdStdSessPerfEchoPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfEchoPktDrop.setStatus(_A)
_ZxAnBfdStdSessPerfEchoPktDLT_Type=TimeStamp
_ZxAnBfdStdSessPerfEchoPktDLT_Object=MibTableColumn
zxAnBfdStdSessPerfEchoPktDLT=_ZxAnBfdStdSessPerfEchoPktDLT_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,8),_ZxAnBfdStdSessPerfEchoPktDLT_Type())
zxAnBfdStdSessPerfEchoPktDLT.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfEchoPktDLT.setStatus(_A)
_ZxAnBfdStdSessUpTime_Type=TimeStamp
_ZxAnBfdStdSessUpTime_Object=MibTableColumn
zxAnBfdStdSessUpTime=_ZxAnBfdStdSessUpTime_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,9),_ZxAnBfdStdSessUpTime_Type())
zxAnBfdStdSessUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessUpTime.setStatus(_A)
_ZxAnBfdStdSessPerfLastSessDT_Type=TimeStamp
_ZxAnBfdStdSessPerfLastSessDT_Object=MibTableColumn
zxAnBfdStdSessPerfLastSessDT=_ZxAnBfdStdSessPerfLastSessDT_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,10),_ZxAnBfdStdSessPerfLastSessDT_Type())
zxAnBfdStdSessPerfLastSessDT.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfLastSessDT.setStatus(_A)
_ZxAnBfdStdSessPerfLastCommLDC_Type=ZxAnBfdStdDiag
_ZxAnBfdStdSessPerfLastCommLDC_Object=MibTableColumn
zxAnBfdStdSessPerfLastCommLDC=_ZxAnBfdStdSessPerfLastCommLDC_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,11),_ZxAnBfdStdSessPerfLastCommLDC_Type())
zxAnBfdStdSessPerfLastCommLDC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfLastCommLDC.setStatus(_A)
_ZxAnBfdStdSessPerfSessUpCount_Type=Counter32
_ZxAnBfdStdSessPerfSessUpCount_Object=MibTableColumn
zxAnBfdStdSessPerfSessUpCount=_ZxAnBfdStdSessPerfSessUpCount_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,12),_ZxAnBfdStdSessPerfSessUpCount_Type())
zxAnBfdStdSessPerfSessUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfSessUpCount.setStatus(_A)
_ZxAnBfdStdSessPerfDiscTime_Type=TimeStamp
_ZxAnBfdStdSessPerfDiscTime_Object=MibTableColumn
zxAnBfdStdSessPerfDiscTime=_ZxAnBfdStdSessPerfDiscTime_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,13),_ZxAnBfdStdSessPerfDiscTime_Type())
zxAnBfdStdSessPerfDiscTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfDiscTime.setStatus(_A)
_ZxAnBfdStdSessPerfCtrlPktInHC_Type=Counter64
_ZxAnBfdStdSessPerfCtrlPktInHC_Object=MibTableColumn
zxAnBfdStdSessPerfCtrlPktInHC=_ZxAnBfdStdSessPerfCtrlPktInHC_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,14),_ZxAnBfdStdSessPerfCtrlPktInHC_Type())
zxAnBfdStdSessPerfCtrlPktInHC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfCtrlPktInHC.setStatus(_A)
_ZxAnBfdStdSessPerfCtrlPktOutHC_Type=Counter64
_ZxAnBfdStdSessPerfCtrlPktOutHC_Object=MibTableColumn
zxAnBfdStdSessPerfCtrlPktOutHC=_ZxAnBfdStdSessPerfCtrlPktOutHC_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,15),_ZxAnBfdStdSessPerfCtrlPktOutHC_Type())
zxAnBfdStdSessPerfCtrlPktOutHC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfCtrlPktOutHC.setStatus(_A)
_ZxAnBfdStdSessPerfCtrlPktDropHC_Type=Counter64
_ZxAnBfdStdSessPerfCtrlPktDropHC_Object=MibTableColumn
zxAnBfdStdSessPerfCtrlPktDropHC=_ZxAnBfdStdSessPerfCtrlPktDropHC_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,16),_ZxAnBfdStdSessPerfCtrlPktDropHC_Type())
zxAnBfdStdSessPerfCtrlPktDropHC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfCtrlPktDropHC.setStatus(_A)
_ZxAnBfdStdSessPerfEchoPktInHC_Type=Counter64
_ZxAnBfdStdSessPerfEchoPktInHC_Object=MibTableColumn
zxAnBfdStdSessPerfEchoPktInHC=_ZxAnBfdStdSessPerfEchoPktInHC_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,17),_ZxAnBfdStdSessPerfEchoPktInHC_Type())
zxAnBfdStdSessPerfEchoPktInHC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfEchoPktInHC.setStatus(_A)
_ZxAnBfdStdSessPerfEchoPktOutHC_Type=Counter64
_ZxAnBfdStdSessPerfEchoPktOutHC_Object=MibTableColumn
zxAnBfdStdSessPerfEchoPktOutHC=_ZxAnBfdStdSessPerfEchoPktOutHC_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,18),_ZxAnBfdStdSessPerfEchoPktOutHC_Type())
zxAnBfdStdSessPerfEchoPktOutHC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfEchoPktOutHC.setStatus(_A)
_ZxAnBfdStdSessPerfEchoPktDropHC_Type=Counter64
_ZxAnBfdStdSessPerfEchoPktDropHC_Object=MibTableColumn
zxAnBfdStdSessPerfEchoPktDropHC=_ZxAnBfdStdSessPerfEchoPktDropHC_Object((1,3,6,1,4,1,3902,1015,16,1,3,1,19),_ZxAnBfdStdSessPerfEchoPktDropHC_Type())
zxAnBfdStdSessPerfEchoPktDropHC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessPerfEchoPktDropHC.setStatus(_A)
_ZxAnBfdStdSessDiscMapTable_Object=MibTable
zxAnBfdStdSessDiscMapTable=_ZxAnBfdStdSessDiscMapTable_Object((1,3,6,1,4,1,3902,1015,16,1,4))
if mibBuilder.loadTexts:zxAnBfdStdSessDiscMapTable.setStatus(_A)
_ZxAnBfdStdSessDiscMapEntry_Object=MibTableRow
zxAnBfdStdSessDiscMapEntry=_ZxAnBfdStdSessDiscMapEntry_Object((1,3,6,1,4,1,3902,1015,16,1,4,1))
zxAnBfdStdSessDiscMapEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:zxAnBfdStdSessDiscMapEntry.setStatus(_A)
class _ZxAnBfdStdSessDiscIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ZxAnBfdStdSessDiscIndex_Type.__name__=_G
_ZxAnBfdStdSessDiscIndex_Object=MibTableColumn
zxAnBfdStdSessDiscIndex=_ZxAnBfdStdSessDiscIndex_Object((1,3,6,1,4,1,3902,1015,16,1,4,1,1),_ZxAnBfdStdSessDiscIndex_Type())
zxAnBfdStdSessDiscIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnBfdStdSessDiscIndex.setStatus(_A)
_ZxAnBfdStdSessDiscMapIndex_Type=ZxAnBfdStdSessIndexTC
_ZxAnBfdStdSessDiscMapIndex_Object=MibTableColumn
zxAnBfdStdSessDiscMapIndex=_ZxAnBfdStdSessDiscMapIndex_Object((1,3,6,1,4,1,3902,1015,16,1,4,1,2),_ZxAnBfdStdSessDiscMapIndex_Type())
zxAnBfdStdSessDiscMapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessDiscMapIndex.setStatus(_A)
_ZxAnBfdStdSessIpMapTable_Object=MibTable
zxAnBfdStdSessIpMapTable=_ZxAnBfdStdSessIpMapTable_Object((1,3,6,1,4,1,3902,1015,16,1,5))
if mibBuilder.loadTexts:zxAnBfdStdSessIpMapTable.setStatus(_A)
_ZxAnBfdStdSessIpMapEntry_Object=MibTableRow
zxAnBfdStdSessIpMapEntry=_ZxAnBfdStdSessIpMapEntry_Object((1,3,6,1,4,1,3902,1015,16,1,5,1))
zxAnBfdStdSessIpMapEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:zxAnBfdStdSessIpMapEntry.setStatus(_A)
_ZxAnBfdStdSessIfIndex_Type=InterfaceIndexOrZero
_ZxAnBfdStdSessIfIndex_Object=MibTableColumn
zxAnBfdStdSessIfIndex=_ZxAnBfdStdSessIfIndex_Object((1,3,6,1,4,1,3902,1015,16,1,5,1,1),_ZxAnBfdStdSessIfIndex_Type())
zxAnBfdStdSessIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnBfdStdSessIfIndex.setStatus(_A)
_ZxAnBfdStdSessPeerIpAddressType_Type=InetAddressType
_ZxAnBfdStdSessPeerIpAddressType_Object=MibTableColumn
zxAnBfdStdSessPeerIpAddressType=_ZxAnBfdStdSessPeerIpAddressType_Object((1,3,6,1,4,1,3902,1015,16,1,5,1,2),_ZxAnBfdStdSessPeerIpAddressType_Type())
zxAnBfdStdSessPeerIpAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnBfdStdSessPeerIpAddressType.setStatus(_A)
_ZxAnBfdStdSessPeerIpAddress_Type=InetAddress
_ZxAnBfdStdSessPeerIpAddress_Object=MibTableColumn
zxAnBfdStdSessPeerIpAddress=_ZxAnBfdStdSessPeerIpAddress_Object((1,3,6,1,4,1,3902,1015,16,1,5,1,3),_ZxAnBfdStdSessPeerIpAddress_Type())
zxAnBfdStdSessPeerIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnBfdStdSessPeerIpAddress.setStatus(_A)
_ZxAnBfdStdSessIpMapIndex_Type=ZxAnBfdStdSessIndexTC
_ZxAnBfdStdSessIpMapIndex_Object=MibTableColumn
zxAnBfdStdSessIpMapIndex=_ZxAnBfdStdSessIpMapIndex_Object((1,3,6,1,4,1,3902,1015,16,1,5,1,4),_ZxAnBfdStdSessIpMapIndex_Type())
zxAnBfdStdSessIpMapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdStdSessIpMapIndex.setStatus(_A)
_ZxAnBfdStdConformance_ObjectIdentity=ObjectIdentity
zxAnBfdStdConformance=_ZxAnBfdStdConformance_ObjectIdentity((1,3,6,1,4,1,3902,1015,16,2))
zxAnBfdStdSessEntry.registerAugmentions((_D,_R))
zxAnBfdStdSessPerfEntry.setIndexNames(*zxAnBfdStdSessEntry.getIndexNames())
zxAnBfdStdSessUp=NotificationType((1,3,6,1,4,1,3902,1015,16,0,1))
zxAnBfdStdSessUp.setObjects(*((_D,_I),(_D,_I)))
if mibBuilder.loadTexts:zxAnBfdStdSessUp.setStatus(_A)
zxAnBfdStdSessDown=NotificationType((1,3,6,1,4,1,3902,1015,16,0,2))
zxAnBfdStdSessDown.setObjects(*((_D,_I),(_D,_I)))
if mibBuilder.loadTexts:zxAnBfdStdSessDown.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ZxAnBfdStdSessIndexTC':ZxAnBfdStdSessIndexTC,'ZxAnBfdStdInterval':ZxAnBfdStdInterval,'ZxAnBfdStdMultiplier':ZxAnBfdStdMultiplier,'ZxAnBfdStdDiag':ZxAnBfdStdDiag,'zxAnBfdStdMib':zxAnBfdStdMib,'zxAnBfdStdNotifications':zxAnBfdStdNotifications,'zxAnBfdStdSessUp':zxAnBfdStdSessUp,'zxAnBfdStdSessDown':zxAnBfdStdSessDown,'zxAnBfdStdObjects':zxAnBfdStdObjects,'zxAnBfdStdGlobalObjects':zxAnBfdStdGlobalObjects,'zxAnBfdStdAdminStatus':zxAnBfdStdAdminStatus,'zxAnBfdStdSessTrapsEnable':zxAnBfdStdSessTrapsEnable,'zxAnBfdStdSessTable':zxAnBfdStdSessTable,'zxAnBfdStdSessEntry':zxAnBfdStdSessEntry,_M:zxAnBfdStdSessIndex,'zxAnBfdStdSessVersionNumber':zxAnBfdStdSessVersionNumber,'zxAnBfdStdSessType':zxAnBfdStdSessType,'zxAnBfdStdSessMHopUniLinkMode':zxAnBfdStdSessMHopUniLinkMode,'zxAnBfdStdSessDiscriminator':zxAnBfdStdSessDiscriminator,'zxAnBfdStdSessRemoteDiscr':zxAnBfdStdSessRemoteDiscr,'zxAnBfdStdSessDestinationUdpPort':zxAnBfdStdSessDestinationUdpPort,'zxAnBfdStdSessSourceUdpPort':zxAnBfdStdSessSourceUdpPort,'zxAnBfdStdSessEchoSourceUdpPort':zxAnBfdStdSessEchoSourceUdpPort,'zxAnBfdStdSessAdminStatus':zxAnBfdStdSessAdminStatus,'zxAnBfdStdSessState':zxAnBfdStdSessState,'zxAnBfdStdSessRemoteHeardFlag':zxAnBfdStdSessRemoteHeardFlag,_I:zxAnBfdStdSessDiag,'zxAnBfdStdSessOperMode':zxAnBfdStdSessOperMode,'zxAnBfdStdSessDesiredDmdMode':zxAnBfdStdSessDesiredDmdMode,'zxAnBfdStdSessCtrlPlaneIndep':zxAnBfdStdSessCtrlPlaneIndep,'zxAnBfdStdSessMultipointFlag':zxAnBfdStdSessMultipointFlag,'zxAnBfdStdSessInterface':zxAnBfdStdSessInterface,'zxAnBfdStdSessPeerIpAddrType':zxAnBfdStdSessPeerIpAddrType,'zxAnBfdStdSessPeerIpAddr':zxAnBfdStdSessPeerIpAddr,'zxAnBfdStdSessGTSM':zxAnBfdStdSessGTSM,'zxAnBfdStdSessGTSMTTL':zxAnBfdStdSessGTSMTTL,'zxAnBfdStdSessDesiredMinTxIntv':zxAnBfdStdSessDesiredMinTxIntv,'zxAnBfdStdSessReqMinRxIntv':zxAnBfdStdSessReqMinRxIntv,'zxAnBfdStdSessReqMinEchoRxIntv':zxAnBfdStdSessReqMinEchoRxIntv,'zxAnBfdStdSessDetectMult':zxAnBfdStdSessDetectMult,'zxAnBfdStdSessNegInterval':zxAnBfdStdSessNegInterval,'zxAnBfdStdSessNegEchoInterval':zxAnBfdStdSessNegEchoInterval,'zxAnBfdStdSessNegDetectMult':zxAnBfdStdSessNegDetectMult,'zxAnBfdStdSessAuthPresFlag':zxAnBfdStdSessAuthPresFlag,'zxAnBfdStdSessAuthType':zxAnBfdStdSessAuthType,'zxAnBfdStdSessAuthKeyID':zxAnBfdStdSessAuthKeyID,'zxAnBfdStdSessAuthKey':zxAnBfdStdSessAuthKey,'zxAnBfdStdSessIpAddrType':zxAnBfdStdSessIpAddrType,'zxAnBfdStdSessIpAddr':zxAnBfdStdSessIpAddr,'zxAnBfdStdSessAppType':zxAnBfdStdSessAppType,'zxAnBfdStdSessStorType':zxAnBfdStdSessStorType,'zxAnBfdStdSessRowStatus':zxAnBfdStdSessRowStatus,'zxAnBfdStdSessPerfTable':zxAnBfdStdSessPerfTable,_R:zxAnBfdStdSessPerfEntry,'zxAnBfdStdSessPerfCtrlPktIn':zxAnBfdStdSessPerfCtrlPktIn,'zxAnBfdStdSessPerfCtrlPktOut':zxAnBfdStdSessPerfCtrlPktOut,'zxAnBfdStdSessPerfCtrlPktDrop':zxAnBfdStdSessPerfCtrlPktDrop,'zxAnBfdStdSessPerfCtrlPktDLT':zxAnBfdStdSessPerfCtrlPktDLT,'zxAnBfdStdSessPerfEchoPktIn':zxAnBfdStdSessPerfEchoPktIn,'zxAnBfdStdSessPerfEchoPktOut':zxAnBfdStdSessPerfEchoPktOut,'zxAnBfdStdSessPerfEchoPktDrop':zxAnBfdStdSessPerfEchoPktDrop,'zxAnBfdStdSessPerfEchoPktDLT':zxAnBfdStdSessPerfEchoPktDLT,'zxAnBfdStdSessUpTime':zxAnBfdStdSessUpTime,'zxAnBfdStdSessPerfLastSessDT':zxAnBfdStdSessPerfLastSessDT,'zxAnBfdStdSessPerfLastCommLDC':zxAnBfdStdSessPerfLastCommLDC,'zxAnBfdStdSessPerfSessUpCount':zxAnBfdStdSessPerfSessUpCount,'zxAnBfdStdSessPerfDiscTime':zxAnBfdStdSessPerfDiscTime,'zxAnBfdStdSessPerfCtrlPktInHC':zxAnBfdStdSessPerfCtrlPktInHC,'zxAnBfdStdSessPerfCtrlPktOutHC':zxAnBfdStdSessPerfCtrlPktOutHC,'zxAnBfdStdSessPerfCtrlPktDropHC':zxAnBfdStdSessPerfCtrlPktDropHC,'zxAnBfdStdSessPerfEchoPktInHC':zxAnBfdStdSessPerfEchoPktInHC,'zxAnBfdStdSessPerfEchoPktOutHC':zxAnBfdStdSessPerfEchoPktOutHC,'zxAnBfdStdSessPerfEchoPktDropHC':zxAnBfdStdSessPerfEchoPktDropHC,'zxAnBfdStdSessDiscMapTable':zxAnBfdStdSessDiscMapTable,'zxAnBfdStdSessDiscMapEntry':zxAnBfdStdSessDiscMapEntry,_N:zxAnBfdStdSessDiscIndex,'zxAnBfdStdSessDiscMapIndex':zxAnBfdStdSessDiscMapIndex,'zxAnBfdStdSessIpMapTable':zxAnBfdStdSessIpMapTable,'zxAnBfdStdSessIpMapEntry':zxAnBfdStdSessIpMapEntry,_O:zxAnBfdStdSessIfIndex,_P:zxAnBfdStdSessPeerIpAddressType,_Q:zxAnBfdStdSessPeerIpAddress,'zxAnBfdStdSessIpMapIndex':zxAnBfdStdSessIpMapIndex,'zxAnBfdStdConformance':zxAnBfdStdConformance})