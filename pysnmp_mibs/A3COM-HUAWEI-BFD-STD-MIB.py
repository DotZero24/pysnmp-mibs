_P='h3cBfdSessState'
_O='h3cBfdSessPerfEntry'
_N='h3cBfdSessStatEntry'
_M='BfdDiag'
_L='InetPortNumber'
_K='h3cBfdSessIndex'
_J='h3cBfdSessIfIndex'
_I='accessible-for-notify'
_H='h3cBfdIfIndex'
_G='Unsigned32'
_F='read-write'
_E='TruthValue'
_D='Integer32'
_C='A3COM-HUAWEI-BFD-STD-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_E)
h3cBfdMIB=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,72))
if mibBuilder.loadTexts:h3cBfdMIB.setRevisions(('2006-05-16 12:00',))
class BfdSessIndexTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdInterval(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdDiag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noDiagnostic',1),('controlDetectionTimeExpired',2),('echoFunctionFailed',3),('neighborSignaledSessionDown',4),('forwardingPlaneReset',5),('pathDown',6),('concatenatedPathDown',7),('administrativelyDown',8),('reverseConcatenatedPathDown',9)))
_H3cBfdNotifications_ObjectIdentity=ObjectIdentity
h3cBfdNotifications=_H3cBfdNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,72,0))
_H3cBfdObjects_ObjectIdentity=ObjectIdentity
h3cBfdObjects=_H3cBfdObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,72,1))
_H3cBfdGlobalObjects_ObjectIdentity=ObjectIdentity
h3cBfdGlobalObjects=_H3cBfdGlobalObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,72,1,1))
class _H3cBfdVersionNumber_Type(Unsigned32):defaultValue=1
_H3cBfdVersionNumber_Type.__name__=_G
_H3cBfdVersionNumber_Object=MibScalar
h3cBfdVersionNumber=_H3cBfdVersionNumber_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,1,1),_H3cBfdVersionNumber_Type())
h3cBfdVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdVersionNumber.setStatus(_A)
class _H3cBfdSysInitMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_H3cBfdSysInitMode_Type.__name__=_D
_H3cBfdSysInitMode_Object=MibScalar
h3cBfdSysInitMode=_H3cBfdSysInitMode_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,1,2),_H3cBfdSysInitMode_Type())
h3cBfdSysInitMode.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBfdSysInitMode.setStatus(_A)
class _H3cBfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_H3cBfdSessNotificationsEnable_Type.__name__=_E
_H3cBfdSessNotificationsEnable_Object=MibScalar
h3cBfdSessNotificationsEnable=_H3cBfdSessNotificationsEnable_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,1,3),_H3cBfdSessNotificationsEnable_Type())
h3cBfdSessNotificationsEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBfdSessNotificationsEnable.setStatus(_A)
_H3cBfdIfTable_Object=MibTable
h3cBfdIfTable=_H3cBfdIfTable_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,2))
if mibBuilder.loadTexts:h3cBfdIfTable.setStatus(_A)
_H3cBfdIfEntry_Object=MibTableRow
h3cBfdIfEntry=_H3cBfdIfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,2,1))
h3cBfdIfEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:h3cBfdIfEntry.setStatus(_A)
_H3cBfdIfIndex_Type=InterfaceIndex
_H3cBfdIfIndex_Object=MibTableColumn
h3cBfdIfIndex=_H3cBfdIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,2,1,1),_H3cBfdIfIndex_Type())
h3cBfdIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cBfdIfIndex.setStatus(_A)
_H3cBfdIfDesiredMinTxInterval_Type=BfdInterval
_H3cBfdIfDesiredMinTxInterval_Object=MibTableColumn
h3cBfdIfDesiredMinTxInterval=_H3cBfdIfDesiredMinTxInterval_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,2,1,2),_H3cBfdIfDesiredMinTxInterval_Type())
h3cBfdIfDesiredMinTxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBfdIfDesiredMinTxInterval.setStatus(_A)
_H3cBfdIfDesiredMinRxInterval_Type=BfdInterval
_H3cBfdIfDesiredMinRxInterval_Object=MibTableColumn
h3cBfdIfDesiredMinRxInterval=_H3cBfdIfDesiredMinRxInterval_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,2,1,3),_H3cBfdIfDesiredMinRxInterval_Type())
h3cBfdIfDesiredMinRxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBfdIfDesiredMinRxInterval.setStatus(_A)
_H3cBfdIfDetectMult_Type=Unsigned32
_H3cBfdIfDetectMult_Object=MibTableColumn
h3cBfdIfDetectMult=_H3cBfdIfDetectMult_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,2,1,4),_H3cBfdIfDetectMult_Type())
h3cBfdIfDetectMult.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBfdIfDetectMult.setStatus(_A)
class _H3cBfdIfAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('simple',2),('md5',3),('mmd5',4),('sha1',5),('msha1',6)))
_H3cBfdIfAuthType_Type.__name__=_D
_H3cBfdIfAuthType_Object=MibTableColumn
h3cBfdIfAuthType=_H3cBfdIfAuthType_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,2,1,5),_H3cBfdIfAuthType_Type())
h3cBfdIfAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdIfAuthType.setStatus(_A)
_H3cBfdSessTable_Object=MibTable
h3cBfdSessTable=_H3cBfdSessTable_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3))
if mibBuilder.loadTexts:h3cBfdSessTable.setStatus(_A)
_H3cBfdSessEntry_Object=MibTableRow
h3cBfdSessEntry=_H3cBfdSessEntry_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1))
h3cBfdSessEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:h3cBfdSessEntry.setStatus(_A)
_H3cBfdSessIfIndex_Type=InterfaceIndex
_H3cBfdSessIfIndex_Object=MibTableColumn
h3cBfdSessIfIndex=_H3cBfdSessIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,1),_H3cBfdSessIfIndex_Type())
h3cBfdSessIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cBfdSessIfIndex.setStatus(_A)
_H3cBfdSessIndex_Type=BfdSessIndexTC
_H3cBfdSessIndex_Object=MibTableColumn
h3cBfdSessIndex=_H3cBfdSessIndex_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,2),_H3cBfdSessIndex_Type())
h3cBfdSessIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cBfdSessIndex.setStatus(_A)
class _H3cBfdSessAppSupportId_Type(Bits):namedValues=NamedValues(*(('none',0),('ospf',1),('isis',2),('bgp',3),('mpls',4)))
_H3cBfdSessAppSupportId_Type.__name__='Bits'
_H3cBfdSessAppSupportId_Object=MibTableColumn
h3cBfdSessAppSupportId=_H3cBfdSessAppSupportId_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,3),_H3cBfdSessAppSupportId_Type())
h3cBfdSessAppSupportId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessAppSupportId.setStatus(_A)
class _H3cBfdSessLocalDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cBfdSessLocalDiscr_Type.__name__=_G
_H3cBfdSessLocalDiscr_Object=MibTableColumn
h3cBfdSessLocalDiscr=_H3cBfdSessLocalDiscr_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,4),_H3cBfdSessLocalDiscr_Type())
h3cBfdSessLocalDiscr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessLocalDiscr.setStatus(_A)
class _H3cBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cBfdSessRemoteDiscr_Type.__name__=_G
_H3cBfdSessRemoteDiscr_Object=MibTableColumn
h3cBfdSessRemoteDiscr=_H3cBfdSessRemoteDiscr_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,5),_H3cBfdSessRemoteDiscr_Type())
h3cBfdSessRemoteDiscr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessRemoteDiscr.setStatus(_A)
class _H3cBfdSessDstPort_Type(InetPortNumber):defaultValue=3784
_H3cBfdSessDstPort_Type.__name__=_L
_H3cBfdSessDstPort_Object=MibTableColumn
h3cBfdSessDstPort=_H3cBfdSessDstPort_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,6),_H3cBfdSessDstPort_Type())
h3cBfdSessDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessDstPort.setStatus(_A)
class _H3cBfdSessOperMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asynchModeWOEchoFun',1),('demandModeWOEchoFunction',2),('asyncModeWEchoFun',3),('demandModeWEchoFunction',4)))
_H3cBfdSessOperMode_Type.__name__=_D
_H3cBfdSessOperMode_Object=MibTableColumn
h3cBfdSessOperMode=_H3cBfdSessOperMode_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,7),_H3cBfdSessOperMode_Type())
h3cBfdSessOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessOperMode.setStatus(_A)
_H3cBfdSessAddrType_Type=InetAddressType
_H3cBfdSessAddrType_Object=MibTableColumn
h3cBfdSessAddrType=_H3cBfdSessAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,8),_H3cBfdSessAddrType_Type())
h3cBfdSessAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessAddrType.setStatus(_A)
_H3cBfdSessLocalAddr_Type=InetAddress
_H3cBfdSessLocalAddr_Object=MibTableColumn
h3cBfdSessLocalAddr=_H3cBfdSessLocalAddr_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,9),_H3cBfdSessLocalAddr_Type())
h3cBfdSessLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessLocalAddr.setStatus(_A)
_H3cBfdSessRemoteAddr_Type=InetAddress
_H3cBfdSessRemoteAddr_Object=MibTableColumn
h3cBfdSessRemoteAddr=_H3cBfdSessRemoteAddr_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,10),_H3cBfdSessRemoteAddr_Type())
h3cBfdSessRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessRemoteAddr.setStatus(_A)
class _H3cBfdSessLocalDiag_Type(BfdDiag):defaultValue=1
_H3cBfdSessLocalDiag_Type.__name__=_M
_H3cBfdSessLocalDiag_Object=MibTableColumn
h3cBfdSessLocalDiag=_H3cBfdSessLocalDiag_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,11),_H3cBfdSessLocalDiag_Type())
h3cBfdSessLocalDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessLocalDiag.setStatus(_A)
class _H3cBfdSessState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('adminDown',0),('down',1),('init',2),('up',3)))
_H3cBfdSessState_Type.__name__=_D
_H3cBfdSessState_Object=MibTableColumn
h3cBfdSessState=_H3cBfdSessState_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,12),_H3cBfdSessState_Type())
h3cBfdSessState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessState.setStatus(_A)
class _H3cBfdSessControlPlanIndepFlag_Type(TruthValue):defaultValue=1
_H3cBfdSessControlPlanIndepFlag_Type.__name__=_E
_H3cBfdSessControlPlanIndepFlag_Object=MibTableColumn
h3cBfdSessControlPlanIndepFlag=_H3cBfdSessControlPlanIndepFlag_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,13),_H3cBfdSessControlPlanIndepFlag_Type())
h3cBfdSessControlPlanIndepFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessControlPlanIndepFlag.setStatus(_A)
class _H3cBfdSessAuthFlag_Type(TruthValue):defaultValue=2
_H3cBfdSessAuthFlag_Type.__name__=_E
_H3cBfdSessAuthFlag_Object=MibTableColumn
h3cBfdSessAuthFlag=_H3cBfdSessAuthFlag_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,14),_H3cBfdSessAuthFlag_Type())
h3cBfdSessAuthFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessAuthFlag.setStatus(_A)
class _H3cBfdSessDemandModeFlag_Type(TruthValue):defaultValue=2
_H3cBfdSessDemandModeFlag_Type.__name__=_E
_H3cBfdSessDemandModeFlag_Object=MibTableColumn
h3cBfdSessDemandModeFlag=_H3cBfdSessDemandModeFlag_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,3,1,15),_H3cBfdSessDemandModeFlag_Type())
h3cBfdSessDemandModeFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessDemandModeFlag.setStatus(_A)
_H3cBfdSessStatTable_Object=MibTable
h3cBfdSessStatTable=_H3cBfdSessStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,4))
if mibBuilder.loadTexts:h3cBfdSessStatTable.setStatus(_A)
_H3cBfdSessStatEntry_Object=MibTableRow
h3cBfdSessStatEntry=_H3cBfdSessStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,4,1))
if mibBuilder.loadTexts:h3cBfdSessStatEntry.setStatus(_A)
_H3cBfdSessStatPktInHC_Type=Counter64
_H3cBfdSessStatPktInHC_Object=MibTableColumn
h3cBfdSessStatPktInHC=_H3cBfdSessStatPktInHC_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,4,1,1),_H3cBfdSessStatPktInHC_Type())
h3cBfdSessStatPktInHC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessStatPktInHC.setStatus(_A)
_H3cBfdSessStatPktOutHC_Type=Counter64
_H3cBfdSessStatPktOutHC_Object=MibTableColumn
h3cBfdSessStatPktOutHC=_H3cBfdSessStatPktOutHC_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,4,1,2),_H3cBfdSessStatPktOutHC_Type())
h3cBfdSessStatPktOutHC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessStatPktOutHC.setStatus(_A)
_H3cBfdSessStatDownCount_Type=Counter32
_H3cBfdSessStatDownCount_Object=MibTableColumn
h3cBfdSessStatDownCount=_H3cBfdSessStatDownCount_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,4,1,3),_H3cBfdSessStatDownCount_Type())
h3cBfdSessStatDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessStatDownCount.setStatus(_A)
_H3cBfdSessStatPktDiscard_Type=Counter64
_H3cBfdSessStatPktDiscard_Object=MibTableColumn
h3cBfdSessStatPktDiscard=_H3cBfdSessStatPktDiscard_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,4,1,4),_H3cBfdSessStatPktDiscard_Type())
h3cBfdSessStatPktDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessStatPktDiscard.setStatus(_A)
_H3cBfdSessStatPktLost_Type=Counter64
_H3cBfdSessStatPktLost_Object=MibTableColumn
h3cBfdSessStatPktLost=_H3cBfdSessStatPktLost_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,4,1,5),_H3cBfdSessStatPktLost_Type())
h3cBfdSessStatPktLost.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessStatPktLost.setStatus(_A)
_H3cBfdSessPerfTable_Object=MibTable
h3cBfdSessPerfTable=_H3cBfdSessPerfTable_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,5))
if mibBuilder.loadTexts:h3cBfdSessPerfTable.setStatus(_A)
_H3cBfdSessPerfEntry_Object=MibTableRow
h3cBfdSessPerfEntry=_H3cBfdSessPerfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,5,1))
if mibBuilder.loadTexts:h3cBfdSessPerfEntry.setStatus(_A)
_H3cBfdSessPerfCreatTime_Type=TimeStamp
_H3cBfdSessPerfCreatTime_Object=MibTableColumn
h3cBfdSessPerfCreatTime=_H3cBfdSessPerfCreatTime_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,5,1,1),_H3cBfdSessPerfCreatTime_Type())
h3cBfdSessPerfCreatTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessPerfCreatTime.setStatus(_A)
_H3cBfdSessPerfLastUpTime_Type=TimeStamp
_H3cBfdSessPerfLastUpTime_Object=MibTableColumn
h3cBfdSessPerfLastUpTime=_H3cBfdSessPerfLastUpTime_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,5,1,2),_H3cBfdSessPerfLastUpTime_Type())
h3cBfdSessPerfLastUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessPerfLastUpTime.setStatus(_A)
_H3cBfdSessPerfLastDownTime_Type=TimeStamp
_H3cBfdSessPerfLastDownTime_Object=MibTableColumn
h3cBfdSessPerfLastDownTime=_H3cBfdSessPerfLastDownTime_Object((1,3,6,1,4,1,43,45,1,10,2,72,1,5,1,3),_H3cBfdSessPerfLastDownTime_Type())
h3cBfdSessPerfLastDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBfdSessPerfLastDownTime.setStatus(_A)
_H3cBfdConformance_ObjectIdentity=ObjectIdentity
h3cBfdConformance=_H3cBfdConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,72,2))
h3cBfdSessEntry.registerAugmentions((_C,_N))
h3cBfdSessStatEntry.setIndexNames(*h3cBfdSessEntry.getIndexNames())
h3cBfdSessEntry.registerAugmentions((_C,_O))
h3cBfdSessPerfEntry.setIndexNames(*h3cBfdSessEntry.getIndexNames())
h3cBfdSessStateChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,72,0,1))
h3cBfdSessStateChange.setObjects(*((_C,_J),(_C,_K),(_C,_P)))
if mibBuilder.loadTexts:h3cBfdSessStateChange.setStatus(_A)
h3cBfdSessAuthFail=NotificationType((1,3,6,1,4,1,43,45,1,10,2,72,0,2))
h3cBfdSessAuthFail.setObjects((_C,_H))
if mibBuilder.loadTexts:h3cBfdSessAuthFail.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BfdSessIndexTC':BfdSessIndexTC,'BfdInterval':BfdInterval,_M:BfdDiag,'h3cBfdMIB':h3cBfdMIB,'h3cBfdNotifications':h3cBfdNotifications,'h3cBfdSessStateChange':h3cBfdSessStateChange,'h3cBfdSessAuthFail':h3cBfdSessAuthFail,'h3cBfdObjects':h3cBfdObjects,'h3cBfdGlobalObjects':h3cBfdGlobalObjects,'h3cBfdVersionNumber':h3cBfdVersionNumber,'h3cBfdSysInitMode':h3cBfdSysInitMode,'h3cBfdSessNotificationsEnable':h3cBfdSessNotificationsEnable,'h3cBfdIfTable':h3cBfdIfTable,'h3cBfdIfEntry':h3cBfdIfEntry,_H:h3cBfdIfIndex,'h3cBfdIfDesiredMinTxInterval':h3cBfdIfDesiredMinTxInterval,'h3cBfdIfDesiredMinRxInterval':h3cBfdIfDesiredMinRxInterval,'h3cBfdIfDetectMult':h3cBfdIfDetectMult,'h3cBfdIfAuthType':h3cBfdIfAuthType,'h3cBfdSessTable':h3cBfdSessTable,'h3cBfdSessEntry':h3cBfdSessEntry,_J:h3cBfdSessIfIndex,_K:h3cBfdSessIndex,'h3cBfdSessAppSupportId':h3cBfdSessAppSupportId,'h3cBfdSessLocalDiscr':h3cBfdSessLocalDiscr,'h3cBfdSessRemoteDiscr':h3cBfdSessRemoteDiscr,'h3cBfdSessDstPort':h3cBfdSessDstPort,'h3cBfdSessOperMode':h3cBfdSessOperMode,'h3cBfdSessAddrType':h3cBfdSessAddrType,'h3cBfdSessLocalAddr':h3cBfdSessLocalAddr,'h3cBfdSessRemoteAddr':h3cBfdSessRemoteAddr,'h3cBfdSessLocalDiag':h3cBfdSessLocalDiag,_P:h3cBfdSessState,'h3cBfdSessControlPlanIndepFlag':h3cBfdSessControlPlanIndepFlag,'h3cBfdSessAuthFlag':h3cBfdSessAuthFlag,'h3cBfdSessDemandModeFlag':h3cBfdSessDemandModeFlag,'h3cBfdSessStatTable':h3cBfdSessStatTable,_N:h3cBfdSessStatEntry,'h3cBfdSessStatPktInHC':h3cBfdSessStatPktInHC,'h3cBfdSessStatPktOutHC':h3cBfdSessStatPktOutHC,'h3cBfdSessStatDownCount':h3cBfdSessStatDownCount,'h3cBfdSessStatPktDiscard':h3cBfdSessStatPktDiscard,'h3cBfdSessStatPktLost':h3cBfdSessStatPktLost,'h3cBfdSessPerfTable':h3cBfdSessPerfTable,_O:h3cBfdSessPerfEntry,'h3cBfdSessPerfCreatTime':h3cBfdSessPerfCreatTime,'h3cBfdSessPerfLastUpTime':h3cBfdSessPerfLastUpTime,'h3cBfdSessPerfLastDownTime':h3cBfdSessPerfLastDownTime,'h3cBfdConformance':h3cBfdConformance})