_Q='hpnicfBfdSessNumberLimit'
_P='hpnicfBfdSessPerfEntry'
_O='hpnicfBfdSessStatEntry'
_N='BfdDiag'
_M='InetPortNumber'
_L='accessible-for-notify'
_K='hpnicfBfdIfIndex'
_J='hpnicfBfdSessState'
_I='hpnicfBfdSessIndex'
_H='hpnicfBfdSessIfIndex'
_G='read-write'
_F='TruthValue'
_E='Unsigned32'
_D='Integer32'
_C='HPN-ICF-BFD-STD-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_F)
hpnicfBfdMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,72))
if mibBuilder.loadTexts:hpnicfBfdMIB.setRevisions(('2014-01-17 12:00','2006-05-16 12:00'))
class BfdSessIndexTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdInterval(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdDiag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noDiagnostic',1),('controlDetectionTimeExpired',2),('echoFunctionFailed',3),('neighborSignaledSessionDown',4),('forwardingPlaneReset',5),('pathDown',6),('concatenatedPathDown',7),('administrativelyDown',8),('reverseConcatenatedPathDown',9)))
_HpnicfBfdNotifications_ObjectIdentity=ObjectIdentity
hpnicfBfdNotifications=_HpnicfBfdNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,72,0))
_HpnicfBfdObjects_ObjectIdentity=ObjectIdentity
hpnicfBfdObjects=_HpnicfBfdObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,72,1))
_HpnicfBfdGlobalObjects_ObjectIdentity=ObjectIdentity
hpnicfBfdGlobalObjects=_HpnicfBfdGlobalObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,72,1,1))
class _HpnicfBfdVersionNumber_Type(Unsigned32):defaultValue=1
_HpnicfBfdVersionNumber_Type.__name__=_E
_HpnicfBfdVersionNumber_Object=MibScalar
hpnicfBfdVersionNumber=_HpnicfBfdVersionNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,1,1),_HpnicfBfdVersionNumber_Type())
hpnicfBfdVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdVersionNumber.setStatus(_A)
class _HpnicfBfdSysInitMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_HpnicfBfdSysInitMode_Type.__name__=_D
_HpnicfBfdSysInitMode_Object=MibScalar
hpnicfBfdSysInitMode=_HpnicfBfdSysInitMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,1,2),_HpnicfBfdSysInitMode_Type())
hpnicfBfdSysInitMode.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfBfdSysInitMode.setStatus(_A)
class _HpnicfBfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_HpnicfBfdSessNotificationsEnable_Type.__name__=_F
_HpnicfBfdSessNotificationsEnable_Object=MibScalar
hpnicfBfdSessNotificationsEnable=_HpnicfBfdSessNotificationsEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,1,3),_HpnicfBfdSessNotificationsEnable_Type())
hpnicfBfdSessNotificationsEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfBfdSessNotificationsEnable.setStatus(_A)
class _HpnicfBfdSessNumberLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfBfdSessNumberLimit_Type.__name__=_E
_HpnicfBfdSessNumberLimit_Object=MibScalar
hpnicfBfdSessNumberLimit=_HpnicfBfdSessNumberLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,1,4),_HpnicfBfdSessNumberLimit_Type())
hpnicfBfdSessNumberLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessNumberLimit.setStatus(_A)
_HpnicfBfdIfTable_Object=MibTable
hpnicfBfdIfTable=_HpnicfBfdIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,2))
if mibBuilder.loadTexts:hpnicfBfdIfTable.setStatus(_A)
_HpnicfBfdIfEntry_Object=MibTableRow
hpnicfBfdIfEntry=_HpnicfBfdIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,2,1))
hpnicfBfdIfEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:hpnicfBfdIfEntry.setStatus(_A)
_HpnicfBfdIfIndex_Type=InterfaceIndex
_HpnicfBfdIfIndex_Object=MibTableColumn
hpnicfBfdIfIndex=_HpnicfBfdIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,2,1,1),_HpnicfBfdIfIndex_Type())
hpnicfBfdIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfBfdIfIndex.setStatus(_A)
_HpnicfBfdIfDesiredMinTxInterval_Type=BfdInterval
_HpnicfBfdIfDesiredMinTxInterval_Object=MibTableColumn
hpnicfBfdIfDesiredMinTxInterval=_HpnicfBfdIfDesiredMinTxInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,2,1,2),_HpnicfBfdIfDesiredMinTxInterval_Type())
hpnicfBfdIfDesiredMinTxInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfBfdIfDesiredMinTxInterval.setStatus(_A)
_HpnicfBfdIfDesiredMinRxInterval_Type=BfdInterval
_HpnicfBfdIfDesiredMinRxInterval_Object=MibTableColumn
hpnicfBfdIfDesiredMinRxInterval=_HpnicfBfdIfDesiredMinRxInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,2,1,3),_HpnicfBfdIfDesiredMinRxInterval_Type())
hpnicfBfdIfDesiredMinRxInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfBfdIfDesiredMinRxInterval.setStatus(_A)
_HpnicfBfdIfDetectMult_Type=Unsigned32
_HpnicfBfdIfDetectMult_Object=MibTableColumn
hpnicfBfdIfDetectMult=_HpnicfBfdIfDetectMult_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,2,1,4),_HpnicfBfdIfDetectMult_Type())
hpnicfBfdIfDetectMult.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfBfdIfDetectMult.setStatus(_A)
class _HpnicfBfdIfAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('simple',2),('md5',3),('mmd5',4),('sha1',5),('msha1',6)))
_HpnicfBfdIfAuthType_Type.__name__=_D
_HpnicfBfdIfAuthType_Object=MibTableColumn
hpnicfBfdIfAuthType=_HpnicfBfdIfAuthType_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,2,1,5),_HpnicfBfdIfAuthType_Type())
hpnicfBfdIfAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdIfAuthType.setStatus(_A)
_HpnicfBfdSessTable_Object=MibTable
hpnicfBfdSessTable=_HpnicfBfdSessTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3))
if mibBuilder.loadTexts:hpnicfBfdSessTable.setStatus(_A)
_HpnicfBfdSessEntry_Object=MibTableRow
hpnicfBfdSessEntry=_HpnicfBfdSessEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1))
hpnicfBfdSessEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:hpnicfBfdSessEntry.setStatus(_A)
_HpnicfBfdSessIfIndex_Type=InterfaceIndex
_HpnicfBfdSessIfIndex_Object=MibTableColumn
hpnicfBfdSessIfIndex=_HpnicfBfdSessIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,1),_HpnicfBfdSessIfIndex_Type())
hpnicfBfdSessIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfBfdSessIfIndex.setStatus(_A)
_HpnicfBfdSessIndex_Type=BfdSessIndexTC
_HpnicfBfdSessIndex_Object=MibTableColumn
hpnicfBfdSessIndex=_HpnicfBfdSessIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,2),_HpnicfBfdSessIndex_Type())
hpnicfBfdSessIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfBfdSessIndex.setStatus(_A)
class _HpnicfBfdSessAppSupportId_Type(Bits):namedValues=NamedValues(*(('none',0),('ospf',1),('isis',2),('bgp',3),('mpls',4)))
_HpnicfBfdSessAppSupportId_Type.__name__='Bits'
_HpnicfBfdSessAppSupportId_Object=MibTableColumn
hpnicfBfdSessAppSupportId=_HpnicfBfdSessAppSupportId_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,3),_HpnicfBfdSessAppSupportId_Type())
hpnicfBfdSessAppSupportId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessAppSupportId.setStatus(_A)
class _HpnicfBfdSessLocalDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfBfdSessLocalDiscr_Type.__name__=_E
_HpnicfBfdSessLocalDiscr_Object=MibTableColumn
hpnicfBfdSessLocalDiscr=_HpnicfBfdSessLocalDiscr_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,4),_HpnicfBfdSessLocalDiscr_Type())
hpnicfBfdSessLocalDiscr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessLocalDiscr.setStatus(_A)
class _HpnicfBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfBfdSessRemoteDiscr_Type.__name__=_E
_HpnicfBfdSessRemoteDiscr_Object=MibTableColumn
hpnicfBfdSessRemoteDiscr=_HpnicfBfdSessRemoteDiscr_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,5),_HpnicfBfdSessRemoteDiscr_Type())
hpnicfBfdSessRemoteDiscr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessRemoteDiscr.setStatus(_A)
class _HpnicfBfdSessDstPort_Type(InetPortNumber):defaultValue=3784
_HpnicfBfdSessDstPort_Type.__name__=_M
_HpnicfBfdSessDstPort_Object=MibTableColumn
hpnicfBfdSessDstPort=_HpnicfBfdSessDstPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,6),_HpnicfBfdSessDstPort_Type())
hpnicfBfdSessDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessDstPort.setStatus(_A)
class _HpnicfBfdSessOperMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asynchModeWOEchoFun',1),('demandModeWOEchoFunction',2),('asyncModeWEchoFun',3),('demandModeWEchoFunction',4)))
_HpnicfBfdSessOperMode_Type.__name__=_D
_HpnicfBfdSessOperMode_Object=MibTableColumn
hpnicfBfdSessOperMode=_HpnicfBfdSessOperMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,7),_HpnicfBfdSessOperMode_Type())
hpnicfBfdSessOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessOperMode.setStatus(_A)
_HpnicfBfdSessAddrType_Type=InetAddressType
_HpnicfBfdSessAddrType_Object=MibTableColumn
hpnicfBfdSessAddrType=_HpnicfBfdSessAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,8),_HpnicfBfdSessAddrType_Type())
hpnicfBfdSessAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessAddrType.setStatus(_A)
_HpnicfBfdSessLocalAddr_Type=InetAddress
_HpnicfBfdSessLocalAddr_Object=MibTableColumn
hpnicfBfdSessLocalAddr=_HpnicfBfdSessLocalAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,9),_HpnicfBfdSessLocalAddr_Type())
hpnicfBfdSessLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessLocalAddr.setStatus(_A)
_HpnicfBfdSessRemoteAddr_Type=InetAddress
_HpnicfBfdSessRemoteAddr_Object=MibTableColumn
hpnicfBfdSessRemoteAddr=_HpnicfBfdSessRemoteAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,10),_HpnicfBfdSessRemoteAddr_Type())
hpnicfBfdSessRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessRemoteAddr.setStatus(_A)
class _HpnicfBfdSessLocalDiag_Type(BfdDiag):defaultValue=1
_HpnicfBfdSessLocalDiag_Type.__name__=_N
_HpnicfBfdSessLocalDiag_Object=MibTableColumn
hpnicfBfdSessLocalDiag=_HpnicfBfdSessLocalDiag_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,11),_HpnicfBfdSessLocalDiag_Type())
hpnicfBfdSessLocalDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessLocalDiag.setStatus(_A)
class _HpnicfBfdSessState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('adminDown',0),('down',1),('init',2),('up',3)))
_HpnicfBfdSessState_Type.__name__=_D
_HpnicfBfdSessState_Object=MibTableColumn
hpnicfBfdSessState=_HpnicfBfdSessState_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,12),_HpnicfBfdSessState_Type())
hpnicfBfdSessState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessState.setStatus(_A)
class _HpnicfBfdSessControlPlanIndepFlag_Type(TruthValue):defaultValue=1
_HpnicfBfdSessControlPlanIndepFlag_Type.__name__=_F
_HpnicfBfdSessControlPlanIndepFlag_Object=MibTableColumn
hpnicfBfdSessControlPlanIndepFlag=_HpnicfBfdSessControlPlanIndepFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,13),_HpnicfBfdSessControlPlanIndepFlag_Type())
hpnicfBfdSessControlPlanIndepFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessControlPlanIndepFlag.setStatus(_A)
class _HpnicfBfdSessAuthFlag_Type(TruthValue):defaultValue=2
_HpnicfBfdSessAuthFlag_Type.__name__=_F
_HpnicfBfdSessAuthFlag_Object=MibTableColumn
hpnicfBfdSessAuthFlag=_HpnicfBfdSessAuthFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,14),_HpnicfBfdSessAuthFlag_Type())
hpnicfBfdSessAuthFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessAuthFlag.setStatus(_A)
class _HpnicfBfdSessDemandModeFlag_Type(TruthValue):defaultValue=2
_HpnicfBfdSessDemandModeFlag_Type.__name__=_F
_HpnicfBfdSessDemandModeFlag_Object=MibTableColumn
hpnicfBfdSessDemandModeFlag=_HpnicfBfdSessDemandModeFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,3,1,15),_HpnicfBfdSessDemandModeFlag_Type())
hpnicfBfdSessDemandModeFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessDemandModeFlag.setStatus(_A)
_HpnicfBfdSessStatTable_Object=MibTable
hpnicfBfdSessStatTable=_HpnicfBfdSessStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,4))
if mibBuilder.loadTexts:hpnicfBfdSessStatTable.setStatus(_A)
_HpnicfBfdSessStatEntry_Object=MibTableRow
hpnicfBfdSessStatEntry=_HpnicfBfdSessStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,4,1))
if mibBuilder.loadTexts:hpnicfBfdSessStatEntry.setStatus(_A)
_HpnicfBfdSessStatPktInHC_Type=Counter64
_HpnicfBfdSessStatPktInHC_Object=MibTableColumn
hpnicfBfdSessStatPktInHC=_HpnicfBfdSessStatPktInHC_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,4,1,1),_HpnicfBfdSessStatPktInHC_Type())
hpnicfBfdSessStatPktInHC.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessStatPktInHC.setStatus(_A)
_HpnicfBfdSessStatPktOutHC_Type=Counter64
_HpnicfBfdSessStatPktOutHC_Object=MibTableColumn
hpnicfBfdSessStatPktOutHC=_HpnicfBfdSessStatPktOutHC_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,4,1,2),_HpnicfBfdSessStatPktOutHC_Type())
hpnicfBfdSessStatPktOutHC.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessStatPktOutHC.setStatus(_A)
_HpnicfBfdSessStatDownCount_Type=Counter32
_HpnicfBfdSessStatDownCount_Object=MibTableColumn
hpnicfBfdSessStatDownCount=_HpnicfBfdSessStatDownCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,4,1,3),_HpnicfBfdSessStatDownCount_Type())
hpnicfBfdSessStatDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessStatDownCount.setStatus(_A)
_HpnicfBfdSessStatPktDiscard_Type=Counter64
_HpnicfBfdSessStatPktDiscard_Object=MibTableColumn
hpnicfBfdSessStatPktDiscard=_HpnicfBfdSessStatPktDiscard_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,4,1,4),_HpnicfBfdSessStatPktDiscard_Type())
hpnicfBfdSessStatPktDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessStatPktDiscard.setStatus(_A)
_HpnicfBfdSessStatPktLost_Type=Counter64
_HpnicfBfdSessStatPktLost_Object=MibTableColumn
hpnicfBfdSessStatPktLost=_HpnicfBfdSessStatPktLost_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,4,1,5),_HpnicfBfdSessStatPktLost_Type())
hpnicfBfdSessStatPktLost.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessStatPktLost.setStatus(_A)
_HpnicfBfdSessPerfTable_Object=MibTable
hpnicfBfdSessPerfTable=_HpnicfBfdSessPerfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,5))
if mibBuilder.loadTexts:hpnicfBfdSessPerfTable.setStatus(_A)
_HpnicfBfdSessPerfEntry_Object=MibTableRow
hpnicfBfdSessPerfEntry=_HpnicfBfdSessPerfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,5,1))
if mibBuilder.loadTexts:hpnicfBfdSessPerfEntry.setStatus(_A)
_HpnicfBfdSessPerfCreatTime_Type=TimeStamp
_HpnicfBfdSessPerfCreatTime_Object=MibTableColumn
hpnicfBfdSessPerfCreatTime=_HpnicfBfdSessPerfCreatTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,5,1,1),_HpnicfBfdSessPerfCreatTime_Type())
hpnicfBfdSessPerfCreatTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessPerfCreatTime.setStatus(_A)
_HpnicfBfdSessPerfLastUpTime_Type=TimeStamp
_HpnicfBfdSessPerfLastUpTime_Object=MibTableColumn
hpnicfBfdSessPerfLastUpTime=_HpnicfBfdSessPerfLastUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,5,1,2),_HpnicfBfdSessPerfLastUpTime_Type())
hpnicfBfdSessPerfLastUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessPerfLastUpTime.setStatus(_A)
_HpnicfBfdSessPerfLastDownTime_Type=TimeStamp
_HpnicfBfdSessPerfLastDownTime_Object=MibTableColumn
hpnicfBfdSessPerfLastDownTime=_HpnicfBfdSessPerfLastDownTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,72,1,5,1,3),_HpnicfBfdSessPerfLastDownTime_Type())
hpnicfBfdSessPerfLastDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBfdSessPerfLastDownTime.setStatus(_A)
_HpnicfBfdConformance_ObjectIdentity=ObjectIdentity
hpnicfBfdConformance=_HpnicfBfdConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,72,2))
hpnicfBfdSessEntry.registerAugmentions((_C,_O))
hpnicfBfdSessStatEntry.setIndexNames(*hpnicfBfdSessEntry.getIndexNames())
hpnicfBfdSessEntry.registerAugmentions((_C,_P))
hpnicfBfdSessPerfEntry.setIndexNames(*hpnicfBfdSessEntry.getIndexNames())
hpnicfBfdSessStateChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,72,0,1))
hpnicfBfdSessStateChange.setObjects(*((_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:hpnicfBfdSessStateChange.setStatus(_A)
hpnicfBfdSessAuthFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,72,0,2))
hpnicfBfdSessAuthFail.setObjects((_C,_K))
if mibBuilder.loadTexts:hpnicfBfdSessAuthFail.setStatus(_A)
hpnicfBfdSessStateUp=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,72,0,3))
hpnicfBfdSessStateUp.setObjects(*((_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:hpnicfBfdSessStateUp.setStatus(_A)
hpnicfBfdSessStateDown=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,72,0,4))
hpnicfBfdSessStateDown.setObjects(*((_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:hpnicfBfdSessStateDown.setStatus(_A)
hpnicfBfdSessReachLimit=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,72,0,5))
hpnicfBfdSessReachLimit.setObjects((_C,_Q))
if mibBuilder.loadTexts:hpnicfBfdSessReachLimit.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BfdSessIndexTC':BfdSessIndexTC,'BfdInterval':BfdInterval,_N:BfdDiag,'hpnicfBfdMIB':hpnicfBfdMIB,'hpnicfBfdNotifications':hpnicfBfdNotifications,'hpnicfBfdSessStateChange':hpnicfBfdSessStateChange,'hpnicfBfdSessAuthFail':hpnicfBfdSessAuthFail,'hpnicfBfdSessStateUp':hpnicfBfdSessStateUp,'hpnicfBfdSessStateDown':hpnicfBfdSessStateDown,'hpnicfBfdSessReachLimit':hpnicfBfdSessReachLimit,'hpnicfBfdObjects':hpnicfBfdObjects,'hpnicfBfdGlobalObjects':hpnicfBfdGlobalObjects,'hpnicfBfdVersionNumber':hpnicfBfdVersionNumber,'hpnicfBfdSysInitMode':hpnicfBfdSysInitMode,'hpnicfBfdSessNotificationsEnable':hpnicfBfdSessNotificationsEnable,_Q:hpnicfBfdSessNumberLimit,'hpnicfBfdIfTable':hpnicfBfdIfTable,'hpnicfBfdIfEntry':hpnicfBfdIfEntry,_K:hpnicfBfdIfIndex,'hpnicfBfdIfDesiredMinTxInterval':hpnicfBfdIfDesiredMinTxInterval,'hpnicfBfdIfDesiredMinRxInterval':hpnicfBfdIfDesiredMinRxInterval,'hpnicfBfdIfDetectMult':hpnicfBfdIfDetectMult,'hpnicfBfdIfAuthType':hpnicfBfdIfAuthType,'hpnicfBfdSessTable':hpnicfBfdSessTable,'hpnicfBfdSessEntry':hpnicfBfdSessEntry,_H:hpnicfBfdSessIfIndex,_I:hpnicfBfdSessIndex,'hpnicfBfdSessAppSupportId':hpnicfBfdSessAppSupportId,'hpnicfBfdSessLocalDiscr':hpnicfBfdSessLocalDiscr,'hpnicfBfdSessRemoteDiscr':hpnicfBfdSessRemoteDiscr,'hpnicfBfdSessDstPort':hpnicfBfdSessDstPort,'hpnicfBfdSessOperMode':hpnicfBfdSessOperMode,'hpnicfBfdSessAddrType':hpnicfBfdSessAddrType,'hpnicfBfdSessLocalAddr':hpnicfBfdSessLocalAddr,'hpnicfBfdSessRemoteAddr':hpnicfBfdSessRemoteAddr,'hpnicfBfdSessLocalDiag':hpnicfBfdSessLocalDiag,_J:hpnicfBfdSessState,'hpnicfBfdSessControlPlanIndepFlag':hpnicfBfdSessControlPlanIndepFlag,'hpnicfBfdSessAuthFlag':hpnicfBfdSessAuthFlag,'hpnicfBfdSessDemandModeFlag':hpnicfBfdSessDemandModeFlag,'hpnicfBfdSessStatTable':hpnicfBfdSessStatTable,_O:hpnicfBfdSessStatEntry,'hpnicfBfdSessStatPktInHC':hpnicfBfdSessStatPktInHC,'hpnicfBfdSessStatPktOutHC':hpnicfBfdSessStatPktOutHC,'hpnicfBfdSessStatDownCount':hpnicfBfdSessStatDownCount,'hpnicfBfdSessStatPktDiscard':hpnicfBfdSessStatPktDiscard,'hpnicfBfdSessStatPktLost':hpnicfBfdSessStatPktLost,'hpnicfBfdSessPerfTable':hpnicfBfdSessPerfTable,_P:hpnicfBfdSessPerfEntry,'hpnicfBfdSessPerfCreatTime':hpnicfBfdSessPerfCreatTime,'hpnicfBfdSessPerfLastUpTime':hpnicfBfdSessPerfLastUpTime,'hpnicfBfdSessPerfLastDownTime':hpnicfBfdSessPerfLastDownTime,'hpnicfBfdConformance':hpnicfBfdConformance})