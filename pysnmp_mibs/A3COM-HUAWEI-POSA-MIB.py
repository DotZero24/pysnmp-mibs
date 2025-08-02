_c='h3cPosaAppStateChangeObject'
_b='h3cPosaServerEnable'
_a='h3cPosaCallerStatCallerID'
_Z='h3cPosaTcpTermStatIndex'
_Y='h3cPosaFcmStatIfIndex'
_X='h3cPosaMapDestCode'
_W='h3cPosaMapSrcCode'
_V='H3cTerminalAccessType'
_U='H3cTpduChangeStrategy'
_T='H3cAppMode'
_S='H3cAppServiceType'
_R='accessible-for-notify'
_Q='h3cPosaTerminalID'
_P='seconds'
_O='-dBm'
_N='h3cPosaAppID'
_M='ifDescr'
_L='not-accessible'
_K='milliseconds'
_J='ifIndex'
_I='OctetString'
_H='TruthValue'
_G='IF-MIB'
_F='A3COM-HUAWEI-POSA-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_G,_M,_J)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
h3cPosa=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,92))
if mibBuilder.loadTexts:h3cPosa.setRevisions(('2008-03-12 09:33',))
class H3cAppServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('flow',2)))
class H3cAppMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('temporary',2)))
class H3cPeerState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('notset',1),('down',2),('up',3),('kept',4),('linking',5),('linked',6),('multilink',7),('blocked',8)))
class H3cTerminalAccessType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fcm',1),('flow',2),('tcp',3)))
class H3cTpduChangeStrategy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('changeTpduSrc',1),('changeTpduDest',2)))
_H3cPosaControl_ObjectIdentity=ObjectIdentity
h3cPosaControl=_H3cPosaControl_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,92,1))
class _H3cPosaServerEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_H3cPosaServerEnable_Type.__name__=_D
_H3cPosaServerEnable_Object=MibScalar
h3cPosaServerEnable=_H3cPosaServerEnable_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,1),_H3cPosaServerEnable_Type())
h3cPosaServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaServerEnable.setStatus(_A)
class _H3cPosaFcmAnswerTimeout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2000))
_H3cPosaFcmAnswerTimeout_Type.__name__=_D
_H3cPosaFcmAnswerTimeout_Object=MibScalar
h3cPosaFcmAnswerTimeout=_H3cPosaFcmAnswerTimeout_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,2),_H3cPosaFcmAnswerTimeout_Type())
h3cPosaFcmAnswerTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmAnswerTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmAnswerTimeout.setUnits(_K)
class _H3cPosaFcmTradeTimeout_Type(Integer32):defaultValue=12000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30000,12000000))
_H3cPosaFcmTradeTimeout_Type.__name__=_D
_H3cPosaFcmTradeTimeout_Object=MibScalar
h3cPosaFcmTradeTimeout=_H3cPosaFcmTradeTimeout_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,3),_H3cPosaFcmTradeTimeout_Type())
h3cPosaFcmTradeTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmTradeTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmTradeTimeout.setUnits(_K)
class _H3cPosaFcmIdleTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12000))
_H3cPosaFcmIdleTimeout_Type.__name__=_D
_H3cPosaFcmIdleTimeout_Object=MibScalar
h3cPosaFcmIdleTimeout=_H3cPosaFcmIdleTimeout_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,4),_H3cPosaFcmIdleTimeout_Type())
h3cPosaFcmIdleTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmIdleTimeout.setUnits(_P)
class _H3cPosaSrvStateChangeTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaSrvStateChangeTrapEnable_Type.__name__=_H
_H3cPosaSrvStateChangeTrapEnable_Object=MibScalar
h3cPosaSrvStateChangeTrapEnable=_H3cPosaSrvStateChangeTrapEnable_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,5),_H3cPosaSrvStateChangeTrapEnable_Type())
h3cPosaSrvStateChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaSrvStateChangeTrapEnable.setStatus(_A)
class _H3cPosaAppStateChangeTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaAppStateChangeTrapEnable_Type.__name__=_H
_H3cPosaAppStateChangeTrapEnable_Object=MibScalar
h3cPosaAppStateChangeTrapEnable=_H3cPosaAppStateChangeTrapEnable_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,6),_H3cPosaAppStateChangeTrapEnable_Type())
h3cPosaAppStateChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaAppStateChangeTrapEnable.setStatus(_A)
class _H3cPosaTerminalHangUpTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaTerminalHangUpTrapEnable_Type.__name__=_H
_H3cPosaTerminalHangUpTrapEnable_Object=MibScalar
h3cPosaTerminalHangUpTrapEnable=_H3cPosaTerminalHangUpTrapEnable_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,7),_H3cPosaTerminalHangUpTrapEnable_Type())
h3cPosaTerminalHangUpTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTerminalHangUpTrapEnable.setStatus(_A)
class _H3cPosaFcmLnkNegoFailTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaFcmLnkNegoFailTrapEnable_Type.__name__=_H
_H3cPosaFcmLnkNegoFailTrapEnable_Object=MibScalar
h3cPosaFcmLnkNegoFailTrapEnable=_H3cPosaFcmLnkNegoFailTrapEnable_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,8),_H3cPosaFcmLnkNegoFailTrapEnable_Type())
h3cPosaFcmLnkNegoFailTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmLnkNegoFailTrapEnable.setStatus(_A)
class _H3cPosaFcmPhyNegoFailTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaFcmPhyNegoFailTrapEnable_Type.__name__=_H
_H3cPosaFcmPhyNegoFailTrapEnable_Object=MibScalar
h3cPosaFcmPhyNegoFailTrapEnable=_H3cPosaFcmPhyNegoFailTrapEnable_Object((1,3,6,1,4,1,43,45,1,10,2,92,1,9),_H3cPosaFcmPhyNegoFailTrapEnable_Type())
h3cPosaFcmPhyNegoFailTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmPhyNegoFailTrapEnable.setStatus(_A)
_H3cPosaTables_ObjectIdentity=ObjectIdentity
h3cPosaTables=_H3cPosaTables_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,92,2))
_H3cPosaAppTable_Object=MibTable
h3cPosaAppTable=_H3cPosaAppTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1))
if mibBuilder.loadTexts:h3cPosaAppTable.setStatus(_A)
_H3cPosaAppEntry_Object=MibTableRow
h3cPosaAppEntry=_H3cPosaAppEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1))
h3cPosaAppEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:h3cPosaAppEntry.setStatus(_A)
class _H3cPosaAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_H3cPosaAppID_Type.__name__=_D
_H3cPosaAppID_Object=MibTableColumn
h3cPosaAppID=_H3cPosaAppID_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,1),_H3cPosaAppID_Type())
h3cPosaAppID.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cPosaAppID.setStatus(_A)
class _H3cPosaAppServiceType_Type(H3cAppServiceType):defaultValue=1
_H3cPosaAppServiceType_Type.__name__=_S
_H3cPosaAppServiceType_Object=MibTableColumn
h3cPosaAppServiceType=_H3cPosaAppServiceType_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,2),_H3cPosaAppServiceType_Type())
h3cPosaAppServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppServiceType.setStatus(_A)
_H3cPosaAppIfIndex_Type=Integer32
_H3cPosaAppIfIndex_Object=MibTableColumn
h3cPosaAppIfIndex=_H3cPosaAppIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,3),_H3cPosaAppIfIndex_Type())
h3cPosaAppIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppIfIndex.setStatus(_A)
class _H3cPosaAppMode_Type(H3cAppMode):defaultValue=1
_H3cPosaAppMode_Type.__name__=_T
_H3cPosaAppMode_Object=MibTableColumn
h3cPosaAppMode=_H3cPosaAppMode_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,4),_H3cPosaAppMode_Type())
h3cPosaAppMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppMode.setStatus(_A)
_H3cPosaAppHostIPType_Type=InetAddressType
_H3cPosaAppHostIPType_Object=MibTableColumn
h3cPosaAppHostIPType=_H3cPosaAppHostIPType_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,5),_H3cPosaAppHostIPType_Type())
h3cPosaAppHostIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppHostIPType.setStatus(_A)
_H3cPosaAppHostIP_Type=InetAddress
_H3cPosaAppHostIP_Object=MibTableColumn
h3cPosaAppHostIP=_H3cPosaAppHostIP_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,6),_H3cPosaAppHostIP_Type())
h3cPosaAppHostIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppHostIP.setStatus(_A)
class _H3cPosaAppHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cPosaAppHostPort_Type.__name__=_D
_H3cPosaAppHostPort_Object=MibTableColumn
h3cPosaAppHostPort=_H3cPosaAppHostPort_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,7),_H3cPosaAppHostPort_Type())
h3cPosaAppHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppHostPort.setStatus(_A)
_H3cPosaAppRouterIPType_Type=InetAddressType
_H3cPosaAppRouterIPType_Object=MibTableColumn
h3cPosaAppRouterIPType=_H3cPosaAppRouterIPType_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,8),_H3cPosaAppRouterIPType_Type())
h3cPosaAppRouterIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppRouterIPType.setStatus(_A)
_H3cPosaAppRouterIP_Type=InetAddress
_H3cPosaAppRouterIP_Object=MibTableColumn
h3cPosaAppRouterIP=_H3cPosaAppRouterIP_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,9),_H3cPosaAppRouterIP_Type())
h3cPosaAppRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppRouterIP.setStatus(_A)
class _H3cPosaAppKeepAliveInterval_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7200))
_H3cPosaAppKeepAliveInterval_Type.__name__=_D
_H3cPosaAppKeepAliveInterval_Object=MibTableColumn
h3cPosaAppKeepAliveInterval=_H3cPosaAppKeepAliveInterval_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,10),_H3cPosaAppKeepAliveInterval_Type())
h3cPosaAppKeepAliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaAppKeepAliveInterval.setUnits(_P)
class _H3cPosaAppKeepAliveCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100))
_H3cPosaAppKeepAliveCount_Type.__name__=_D
_H3cPosaAppKeepAliveCount_Object=MibTableColumn
h3cPosaAppKeepAliveCount=_H3cPosaAppKeepAliveCount_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,11),_H3cPosaAppKeepAliveCount_Type())
h3cPosaAppKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppKeepAliveCount.setStatus(_A)
class _H3cPosaAppConnectTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_H3cPosaAppConnectTimeout_Type.__name__=_D
_H3cPosaAppConnectTimeout_Object=MibTableColumn
h3cPosaAppConnectTimeout=_H3cPosaAppConnectTimeout_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,12),_H3cPosaAppConnectTimeout_Type())
h3cPosaAppConnectTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppConnectTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaAppConnectTimeout.setUnits(_P)
_H3cPosaAppState_Type=H3cPeerState
_H3cPosaAppState_Object=MibTableColumn
h3cPosaAppState=_H3cPosaAppState_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,13),_H3cPosaAppState_Type())
h3cPosaAppState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaAppState.setStatus(_A)
_H3cPosaAppRowStatus_Type=RowStatus
_H3cPosaAppRowStatus_Object=MibTableColumn
h3cPosaAppRowStatus=_H3cPosaAppRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,14),_H3cPosaAppRowStatus_Type())
h3cPosaAppRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppRowStatus.setStatus(_A)
class _H3cPosaAppName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cPosaAppName_Type.__name__=_I
_H3cPosaAppName_Object=MibTableColumn
h3cPosaAppName=_H3cPosaAppName_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,15),_H3cPosaAppName_Type())
h3cPosaAppName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppName.setStatus(_A)
class _H3cPosaCallerIDTransEnable_Type(TruthValue):defaultValue=2
_H3cPosaCallerIDTransEnable_Type.__name__=_H
_H3cPosaCallerIDTransEnable_Object=MibTableColumn
h3cPosaCallerIDTransEnable=_H3cPosaCallerIDTransEnable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,16),_H3cPosaCallerIDTransEnable_Type())
h3cPosaCallerIDTransEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaCallerIDTransEnable.setStatus(_A)
class _H3cPosaTpduChangeStrategy_Type(H3cTpduChangeStrategy):defaultValue=1
_H3cPosaTpduChangeStrategy_Type.__name__=_U
_H3cPosaTpduChangeStrategy_Object=MibTableColumn
h3cPosaTpduChangeStrategy=_H3cPosaTpduChangeStrategy_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,17),_H3cPosaTpduChangeStrategy_Type())
h3cPosaTpduChangeStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTpduChangeStrategy.setStatus(_A)
class _H3cPosaBackupAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_H3cPosaBackupAppID_Type.__name__=_D
_H3cPosaBackupAppID_Object=MibTableColumn
h3cPosaBackupAppID=_H3cPosaBackupAppID_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,18),_H3cPosaBackupAppID_Type())
h3cPosaBackupAppID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaBackupAppID.setStatus(_A)
class _H3cPosaQuietTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_H3cPosaQuietTimeOut_Type.__name__=_D
_H3cPosaQuietTimeOut_Object=MibTableColumn
h3cPosaQuietTimeOut=_H3cPosaQuietTimeOut_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,19),_H3cPosaQuietTimeOut_Type())
h3cPosaQuietTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaQuietTimeOut.setStatus(_A)
class _H3cPosaAppHello_Type(TruthValue):defaultValue=2
_H3cPosaAppHello_Type.__name__=_H
_H3cPosaAppHello_Object=MibTableColumn
h3cPosaAppHello=_H3cPosaAppHello_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,20),_H3cPosaAppHello_Type())
h3cPosaAppHello.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppHello.setStatus(_A)
class _H3cPosaAppHelloInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_H3cPosaAppHelloInterval_Type.__name__=_D
_H3cPosaAppHelloInterval_Object=MibTableColumn
h3cPosaAppHelloInterval=_H3cPosaAppHelloInterval_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,21),_H3cPosaAppHelloInterval_Type())
h3cPosaAppHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppHelloInterval.setStatus(_A)
class _H3cPosaAppRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4999))
_H3cPosaAppRouterPort_Type.__name__=_D
_H3cPosaAppRouterPort_Object=MibTableColumn
h3cPosaAppRouterPort=_H3cPosaAppRouterPort_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,1,1,22),_H3cPosaAppRouterPort_Type())
h3cPosaAppRouterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppRouterPort.setStatus(_A)
_H3cPosaTerminalTable_Object=MibTable
h3cPosaTerminalTable=_H3cPosaTerminalTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2))
if mibBuilder.loadTexts:h3cPosaTerminalTable.setStatus(_A)
_H3cPosaTerminalEntry_Object=MibTableRow
h3cPosaTerminalEntry=_H3cPosaTerminalEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1))
h3cPosaTerminalEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:h3cPosaTerminalEntry.setStatus(_A)
class _H3cPosaTerminalID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cPosaTerminalID_Type.__name__=_D
_H3cPosaTerminalID_Object=MibTableColumn
h3cPosaTerminalID=_H3cPosaTerminalID_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,1),_H3cPosaTerminalID_Type())
h3cPosaTerminalID.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPosaTerminalID.setStatus(_A)
class _H3cPosaTerminalAccessType_Type(H3cTerminalAccessType):defaultValue=1
_H3cPosaTerminalAccessType_Type.__name__=_V
_H3cPosaTerminalAccessType_Object=MibTableColumn
h3cPosaTerminalAccessType=_H3cPosaTerminalAccessType_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,2),_H3cPosaTerminalAccessType_Type())
h3cPosaTerminalAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalAccessType.setStatus(_A)
_H3cPosaTerminalIfIndex_Type=Integer32
_H3cPosaTerminalIfIndex_Object=MibTableColumn
h3cPosaTerminalIfIndex=_H3cPosaTerminalIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,3),_H3cPosaTerminalIfIndex_Type())
h3cPosaTerminalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalIfIndex.setStatus(_A)
class _H3cPosaTerminalTransAppID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_H3cPosaTerminalTransAppID_Type.__name__=_D
_H3cPosaTerminalTransAppID_Object=MibTableColumn
h3cPosaTerminalTransAppID=_H3cPosaTerminalTransAppID_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,4),_H3cPosaTerminalTransAppID_Type())
h3cPosaTerminalTransAppID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalTransAppID.setStatus(_A)
class _H3cPosaTerminalListenPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cPosaTerminalListenPort_Type.__name__=_D
_H3cPosaTerminalListenPort_Object=MibTableColumn
h3cPosaTerminalListenPort=_H3cPosaTerminalListenPort_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,5),_H3cPosaTerminalListenPort_Type())
h3cPosaTerminalListenPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalListenPort.setStatus(_A)
_H3cPosaTerminalState_Type=H3cPeerState
_H3cPosaTerminalState_Object=MibTableColumn
h3cPosaTerminalState=_H3cPosaTerminalState_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,6),_H3cPosaTerminalState_Type())
h3cPosaTerminalState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTerminalState.setStatus(_A)
_H3cPosaTerminalRowStatus_Type=RowStatus
_H3cPosaTerminalRowStatus_Object=MibTableColumn
h3cPosaTerminalRowStatus=_H3cPosaTerminalRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,7),_H3cPosaTerminalRowStatus_Type())
h3cPosaTerminalRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalRowStatus.setStatus(_A)
class _H3cPosaTerminalName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cPosaTerminalName_Type.__name__=_I
_H3cPosaTerminalName_Object=MibTableColumn
h3cPosaTerminalName=_H3cPosaTerminalName_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,8),_H3cPosaTerminalName_Type())
h3cPosaTerminalName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalName.setStatus(_A)
_H3cPosaTerminalCfgIfIndex_Type=Integer32
_H3cPosaTerminalCfgIfIndex_Object=MibTableColumn
h3cPosaTerminalCfgIfIndex=_H3cPosaTerminalCfgIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,2,1,9),_H3cPosaTerminalCfgIfIndex_Type())
h3cPosaTerminalCfgIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTerminalCfgIfIndex.setStatus(_A)
_H3cPosaMapTable_Object=MibTable
h3cPosaMapTable=_H3cPosaMapTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,3))
if mibBuilder.loadTexts:h3cPosaMapTable.setStatus(_A)
_H3cPosaMapEntry_Object=MibTableRow
h3cPosaMapEntry=_H3cPosaMapEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,3,1))
h3cPosaMapEntry.setIndexNames((0,_F,_W),(0,_F,_X))
if mibBuilder.loadTexts:h3cPosaMapEntry.setStatus(_A)
class _H3cPosaMapDestCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,7))
_H3cPosaMapDestCode_Type.__name__=_I
_H3cPosaMapDestCode_Object=MibTableColumn
h3cPosaMapDestCode=_H3cPosaMapDestCode_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,3,1,1),_H3cPosaMapDestCode_Type())
h3cPosaMapDestCode.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPosaMapDestCode.setStatus(_A)
class _H3cPosaMapAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_H3cPosaMapAppID_Type.__name__=_D
_H3cPosaMapAppID_Object=MibTableColumn
h3cPosaMapAppID=_H3cPosaMapAppID_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,3,1,2),_H3cPosaMapAppID_Type())
h3cPosaMapAppID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaMapAppID.setStatus(_A)
_H3cPosaMapRowStatus_Type=RowStatus
_H3cPosaMapRowStatus_Object=MibTableColumn
h3cPosaMapRowStatus=_H3cPosaMapRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,3,1,3),_H3cPosaMapRowStatus_Type())
h3cPosaMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaMapRowStatus.setStatus(_A)
class _H3cPosaMapSrcCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,7))
_H3cPosaMapSrcCode_Type.__name__=_I
_H3cPosaMapSrcCode_Object=MibTableColumn
h3cPosaMapSrcCode=_H3cPosaMapSrcCode_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,3,1,4),_H3cPosaMapSrcCode_Type())
h3cPosaMapSrcCode.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPosaMapSrcCode.setStatus(_A)
_H3cPosaFcmStatTable_Object=MibTable
h3cPosaFcmStatTable=_H3cPosaFcmStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,4))
if mibBuilder.loadTexts:h3cPosaFcmStatTable.setStatus(_A)
_H3cPosaFcmStatEntry_Object=MibTableRow
h3cPosaFcmStatEntry=_H3cPosaFcmStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,4,1))
h3cPosaFcmStatEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:h3cPosaFcmStatEntry.setStatus(_A)
class _H3cPosaFcmStatIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPosaFcmStatIfIndex_Type.__name__=_D
_H3cPosaFcmStatIfIndex_Object=MibTableColumn
h3cPosaFcmStatIfIndex=_H3cPosaFcmStatIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,4,1,1),_H3cPosaFcmStatIfIndex_Type())
h3cPosaFcmStatIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPosaFcmStatIfIndex.setStatus(_A)
_H3cPosaFcmStatTimeoutCnts_Type=Counter32
_H3cPosaFcmStatTimeoutCnts_Object=MibTableColumn
h3cPosaFcmStatTimeoutCnts=_H3cPosaFcmStatTimeoutCnts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,4,1,2),_H3cPosaFcmStatTimeoutCnts_Type())
h3cPosaFcmStatTimeoutCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaFcmStatTimeoutCnts.setStatus(_A)
_H3cPosaFcmStatConnectFailCnts_Type=Counter32
_H3cPosaFcmStatConnectFailCnts_Object=MibTableColumn
h3cPosaFcmStatConnectFailCnts=_H3cPosaFcmStatConnectFailCnts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,4,1,3),_H3cPosaFcmStatConnectFailCnts_Type())
h3cPosaFcmStatConnectFailCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaFcmStatConnectFailCnts.setStatus(_A)
_H3cPosaFcmStatTransCnts_Type=Gauge32
_H3cPosaFcmStatTransCnts_Object=MibTableColumn
h3cPosaFcmStatTransCnts=_H3cPosaFcmStatTransCnts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,4,1,4),_H3cPosaFcmStatTransCnts_Type())
h3cPosaFcmStatTransCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaFcmStatTransCnts.setStatus(_A)
_H3cPosaFcmStatTransSuccessCnts_Type=Gauge32
_H3cPosaFcmStatTransSuccessCnts_Object=MibTableColumn
h3cPosaFcmStatTransSuccessCnts=_H3cPosaFcmStatTransSuccessCnts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,4,1,5),_H3cPosaFcmStatTransSuccessCnts_Type())
h3cPosaFcmStatTransSuccessCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaFcmStatTransSuccessCnts.setStatus(_A)
class _H3cPosaFcmStatTransCntsClear_Type(TruthValue):defaultValue=2
_H3cPosaFcmStatTransCntsClear_Type.__name__=_H
_H3cPosaFcmStatTransCntsClear_Object=MibTableColumn
h3cPosaFcmStatTransCntsClear=_H3cPosaFcmStatTransCntsClear_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,4,1,6),_H3cPosaFcmStatTransCntsClear_Type())
h3cPosaFcmStatTransCntsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmStatTransCntsClear.setStatus(_A)
_H3cPosaAppStatTable_Object=MibTable
h3cPosaAppStatTable=_H3cPosaAppStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,5))
if mibBuilder.loadTexts:h3cPosaAppStatTable.setStatus(_A)
_H3cPosaAppStatEntry_Object=MibTableRow
h3cPosaAppStatEntry=_H3cPosaAppStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,5,1))
h3cPosaAppStatEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:h3cPosaAppStatEntry.setStatus(_A)
_H3cPosaAppRecvPkts_Type=Counter32
_H3cPosaAppRecvPkts_Object=MibTableColumn
h3cPosaAppRecvPkts=_H3cPosaAppRecvPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,5,1,1),_H3cPosaAppRecvPkts_Type())
h3cPosaAppRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaAppRecvPkts.setStatus(_A)
_H3cPosaAppSendPkts_Type=Counter32
_H3cPosaAppSendPkts_Object=MibTableColumn
h3cPosaAppSendPkts=_H3cPosaAppSendPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,5,1,2),_H3cPosaAppSendPkts_Type())
h3cPosaAppSendPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaAppSendPkts.setStatus(_A)
_H3cPosaAppErrPkts_Type=Counter32
_H3cPosaAppErrPkts_Object=MibTableColumn
h3cPosaAppErrPkts=_H3cPosaAppErrPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,5,1,3),_H3cPosaAppErrPkts_Type())
h3cPosaAppErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaAppErrPkts.setStatus(_A)
_H3cPosaAppDistributeErrCnts_Type=Counter32
_H3cPosaAppDistributeErrCnts_Object=MibTableColumn
h3cPosaAppDistributeErrCnts=_H3cPosaAppDistributeErrCnts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,5,1,4),_H3cPosaAppDistributeErrCnts_Type())
h3cPosaAppDistributeErrCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaAppDistributeErrCnts.setStatus(_A)
_H3cPosaAppInDiscardedPkts_Type=Counter32
_H3cPosaAppInDiscardedPkts_Object=MibTableColumn
h3cPosaAppInDiscardedPkts=_H3cPosaAppInDiscardedPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,5,1,5),_H3cPosaAppInDiscardedPkts_Type())
h3cPosaAppInDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaAppInDiscardedPkts.setStatus(_A)
_H3cPosaAppOutDiscardedPkts_Type=Counter32
_H3cPosaAppOutDiscardedPkts_Object=MibTableColumn
h3cPosaAppOutDiscardedPkts=_H3cPosaAppOutDiscardedPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,5,1,6),_H3cPosaAppOutDiscardedPkts_Type())
h3cPosaAppOutDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaAppOutDiscardedPkts.setStatus(_A)
_H3cPosaTerminalStatTable_Object=MibTable
h3cPosaTerminalStatTable=_H3cPosaTerminalStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,6))
if mibBuilder.loadTexts:h3cPosaTerminalStatTable.setStatus(_A)
_H3cPosaTerminalStatEntry_Object=MibTableRow
h3cPosaTerminalStatEntry=_H3cPosaTerminalStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,6,1))
h3cPosaTerminalStatEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:h3cPosaTerminalStatEntry.setStatus(_A)
_H3cPosaTerminalRecvPkts_Type=Counter32
_H3cPosaTerminalRecvPkts_Object=MibTableColumn
h3cPosaTerminalRecvPkts=_H3cPosaTerminalRecvPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,6,1,1),_H3cPosaTerminalRecvPkts_Type())
h3cPosaTerminalRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTerminalRecvPkts.setStatus(_A)
_H3cPosaTerminalSendPkts_Type=Counter32
_H3cPosaTerminalSendPkts_Object=MibTableColumn
h3cPosaTerminalSendPkts=_H3cPosaTerminalSendPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,6,1,2),_H3cPosaTerminalSendPkts_Type())
h3cPosaTerminalSendPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTerminalSendPkts.setStatus(_A)
_H3cPosaTerminalErrPkts_Type=Counter32
_H3cPosaTerminalErrPkts_Object=MibTableColumn
h3cPosaTerminalErrPkts=_H3cPosaTerminalErrPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,6,1,3),_H3cPosaTerminalErrPkts_Type())
h3cPosaTerminalErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTerminalErrPkts.setStatus(_A)
_H3cPosaTerminalMapErrCnts_Type=Counter32
_H3cPosaTerminalMapErrCnts_Object=MibTableColumn
h3cPosaTerminalMapErrCnts=_H3cPosaTerminalMapErrCnts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,6,1,4),_H3cPosaTerminalMapErrCnts_Type())
h3cPosaTerminalMapErrCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTerminalMapErrCnts.setStatus(_A)
_H3cPosaTerminalInDiscardedPkts_Type=Counter32
_H3cPosaTerminalInDiscardedPkts_Object=MibTableColumn
h3cPosaTerminalInDiscardedPkts=_H3cPosaTerminalInDiscardedPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,6,1,5),_H3cPosaTerminalInDiscardedPkts_Type())
h3cPosaTerminalInDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTerminalInDiscardedPkts.setStatus(_A)
_H3cPosaTerminalOutDiscardedPkts_Type=Counter32
_H3cPosaTerminalOutDiscardedPkts_Object=MibTableColumn
h3cPosaTerminalOutDiscardedPkts=_H3cPosaTerminalOutDiscardedPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,6,1,6),_H3cPosaTerminalOutDiscardedPkts_Type())
h3cPosaTerminalOutDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTerminalOutDiscardedPkts.setStatus(_A)
_H3cPosaBatchTerminalTable_Object=MibTable
h3cPosaBatchTerminalTable=_H3cPosaBatchTerminalTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,7))
if mibBuilder.loadTexts:h3cPosaBatchTerminalTable.setStatus(_A)
_H3cPosaBatchTerminalEntry_Object=MibTableRow
h3cPosaBatchTerminalEntry=_H3cPosaBatchTerminalEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,7,1))
h3cPosaBatchTerminalEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:h3cPosaBatchTerminalEntry.setStatus(_A)
class _H3cPosaBatchTerminalFirstID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cPosaBatchTerminalFirstID_Type.__name__=_D
_H3cPosaBatchTerminalFirstID_Object=MibTableColumn
h3cPosaBatchTerminalFirstID=_H3cPosaBatchTerminalFirstID_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,7,1,1),_H3cPosaBatchTerminalFirstID_Type())
h3cPosaBatchTerminalFirstID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaBatchTerminalFirstID.setStatus(_A)
_H3cPosaBatchTerminalRowStatus_Type=RowStatus
_H3cPosaBatchTerminalRowStatus_Object=MibTableColumn
h3cPosaBatchTerminalRowStatus=_H3cPosaBatchTerminalRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,7,1,2),_H3cPosaBatchTerminalRowStatus_Type())
h3cPosaBatchTerminalRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaBatchTerminalRowStatus.setStatus(_A)
_H3cPosaTcpTermStatTable_Object=MibTable
h3cPosaTcpTermStatTable=_H3cPosaTcpTermStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8))
if mibBuilder.loadTexts:h3cPosaTcpTermStatTable.setStatus(_A)
_H3cPosaTcpTermStatEntry_Object=MibTableRow
h3cPosaTcpTermStatEntry=_H3cPosaTcpTermStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1))
h3cPosaTcpTermStatEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:h3cPosaTcpTermStatEntry.setStatus(_A)
class _H3cPosaTcpTermStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cPosaTcpTermStatIndex_Type.__name__=_D
_H3cPosaTcpTermStatIndex_Object=MibTableColumn
h3cPosaTcpTermStatIndex=_H3cPosaTcpTermStatIndex_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,1),_H3cPosaTcpTermStatIndex_Type())
h3cPosaTcpTermStatIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPosaTcpTermStatIndex.setStatus(_A)
_H3cPosaTcpTermStatIPType_Type=InetAddressType
_H3cPosaTcpTermStatIPType_Object=MibTableColumn
h3cPosaTcpTermStatIPType=_H3cPosaTcpTermStatIPType_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,2),_H3cPosaTcpTermStatIPType_Type())
h3cPosaTcpTermStatIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermStatIPType.setStatus(_A)
_H3cPosaTcpTermStatIP_Type=InetAddress
_H3cPosaTcpTermStatIP_Object=MibTableColumn
h3cPosaTcpTermStatIP=_H3cPosaTcpTermStatIP_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,3),_H3cPosaTcpTermStatIP_Type())
h3cPosaTcpTermStatIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermStatIP.setStatus(_A)
_H3cPosaTcpTermStatIPMask_Type=InetAddress
_H3cPosaTcpTermStatIPMask_Object=MibTableColumn
h3cPosaTcpTermStatIPMask=_H3cPosaTcpTermStatIPMask_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,4),_H3cPosaTcpTermStatIPMask_Type())
h3cPosaTcpTermStatIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermStatIPMask.setStatus(_A)
_H3cPosaTcpTermRecvPkts_Type=Counter64
_H3cPosaTcpTermRecvPkts_Object=MibTableColumn
h3cPosaTcpTermRecvPkts=_H3cPosaTcpTermRecvPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,5),_H3cPosaTcpTermRecvPkts_Type())
h3cPosaTcpTermRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTcpTermRecvPkts.setStatus(_A)
_H3cPosaTcpTermSendPkts_Type=Counter64
_H3cPosaTcpTermSendPkts_Object=MibTableColumn
h3cPosaTcpTermSendPkts=_H3cPosaTcpTermSendPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,6),_H3cPosaTcpTermSendPkts_Type())
h3cPosaTcpTermSendPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTcpTermSendPkts.setStatus(_A)
_H3cPosaTcpTermErrPkts_Type=Counter64
_H3cPosaTcpTermErrPkts_Object=MibTableColumn
h3cPosaTcpTermErrPkts=_H3cPosaTcpTermErrPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,7),_H3cPosaTcpTermErrPkts_Type())
h3cPosaTcpTermErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTcpTermErrPkts.setStatus(_A)
_H3cPosaTcpTermMapErrCnts_Type=Counter64
_H3cPosaTcpTermMapErrCnts_Object=MibTableColumn
h3cPosaTcpTermMapErrCnts=_H3cPosaTcpTermMapErrCnts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,8),_H3cPosaTcpTermMapErrCnts_Type())
h3cPosaTcpTermMapErrCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTcpTermMapErrCnts.setStatus(_A)
_H3cPosaTcpTermInDiscardedPkts_Type=Counter64
_H3cPosaTcpTermInDiscardedPkts_Object=MibTableColumn
h3cPosaTcpTermInDiscardedPkts=_H3cPosaTcpTermInDiscardedPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,9),_H3cPosaTcpTermInDiscardedPkts_Type())
h3cPosaTcpTermInDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTcpTermInDiscardedPkts.setStatus(_A)
_H3cPosaTcpTermOutDiscardedPkts_Type=Counter64
_H3cPosaTcpTermOutDiscardedPkts_Object=MibTableColumn
h3cPosaTcpTermOutDiscardedPkts=_H3cPosaTcpTermOutDiscardedPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,10),_H3cPosaTcpTermOutDiscardedPkts_Type())
h3cPosaTcpTermOutDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaTcpTermOutDiscardedPkts.setStatus(_A)
_H3cPosaTcpTermStatRowStatus_Type=RowStatus
_H3cPosaTcpTermStatRowStatus_Object=MibTableColumn
h3cPosaTcpTermStatRowStatus=_H3cPosaTcpTermStatRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,8,1,11),_H3cPosaTcpTermStatRowStatus_Type())
h3cPosaTcpTermStatRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermStatRowStatus.setStatus(_A)
_H3cPosaFcmConfTable_Object=MibTable
h3cPosaFcmConfTable=_H3cPosaFcmConfTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9))
if mibBuilder.loadTexts:h3cPosaFcmConfTable.setStatus(_A)
_H3cPosaFcmConfEntry_Object=MibTableRow
h3cPosaFcmConfEntry=_H3cPosaFcmConfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1))
h3cPosaFcmConfEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:h3cPosaFcmConfEntry.setStatus(_A)
class _H3cPosaFcmNegoHookOff_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,6000))
_H3cPosaFcmNegoHookOff_Type.__name__=_D
_H3cPosaFcmNegoHookOff_Object=MibTableColumn
h3cPosaFcmNegoHookOff=_H3cPosaFcmNegoHookOff_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1,1),_H3cPosaFcmNegoHookOff_Type())
h3cPosaFcmNegoHookOff.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmNegoHookOff.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmNegoHookOff.setUnits(_K)
class _H3cPosaFcmNegoSilence_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3000))
_H3cPosaFcmNegoSilence_Type.__name__=_D
_H3cPosaFcmNegoSilence_Object=MibTableColumn
h3cPosaFcmNegoSilence=_H3cPosaFcmNegoSilence_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1,2),_H3cPosaFcmNegoSilence_Type())
h3cPosaFcmNegoSilence.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmNegoSilence.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmNegoSilence.setUnits(_K)
class _H3cPosaFcmNegoScrmbBinary1_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1500))
_H3cPosaFcmNegoScrmbBinary1_Type.__name__=_D
_H3cPosaFcmNegoScrmbBinary1_Object=MibTableColumn
h3cPosaFcmNegoScrmbBinary1=_H3cPosaFcmNegoScrmbBinary1_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1,3),_H3cPosaFcmNegoScrmbBinary1_Type())
h3cPosaFcmNegoScrmbBinary1.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmNegoScrmbBinary1.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmNegoScrmbBinary1.setUnits(_K)
class _H3cPosaFcmNegoUnscrmbBinary1_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1500))
_H3cPosaFcmNegoUnscrmbBinary1_Type.__name__=_D
_H3cPosaFcmNegoUnscrmbBinary1_Object=MibTableColumn
h3cPosaFcmNegoUnscrmbBinary1=_H3cPosaFcmNegoUnscrmbBinary1_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1,4),_H3cPosaFcmNegoUnscrmbBinary1_Type())
h3cPosaFcmNegoUnscrmbBinary1.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmNegoUnscrmbBinary1.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmNegoUnscrmbBinary1.setUnits(_K)
class _H3cPosaFcmThresholdRlsdOff_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,75))
_H3cPosaFcmThresholdRlsdOff_Type.__name__=_D
_H3cPosaFcmThresholdRlsdOff_Object=MibTableColumn
h3cPosaFcmThresholdRlsdOff=_H3cPosaFcmThresholdRlsdOff_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1,5),_H3cPosaFcmThresholdRlsdOff_Type())
h3cPosaFcmThresholdRlsdOff.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmThresholdRlsdOff.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmThresholdRlsdOff.setUnits(_O)
class _H3cPosaFcmThresholdRlsdOn_Type(Integer32):defaultValue=43;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,75))
_H3cPosaFcmThresholdRlsdOn_Type.__name__=_D
_H3cPosaFcmThresholdRlsdOn_Object=MibTableColumn
h3cPosaFcmThresholdRlsdOn=_H3cPosaFcmThresholdRlsdOn_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1,6),_H3cPosaFcmThresholdRlsdOn_Type())
h3cPosaFcmThresholdRlsdOn.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmThresholdRlsdOn.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmThresholdRlsdOn.setUnits(_O)
class _H3cPosaFcmThresholdTxPower_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,42))
_H3cPosaFcmThresholdTxPower_Type.__name__=_D
_H3cPosaFcmThresholdTxPower_Object=MibTableColumn
h3cPosaFcmThresholdTxPower=_H3cPosaFcmThresholdTxPower_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1,7),_H3cPosaFcmThresholdTxPower_Type())
h3cPosaFcmThresholdTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmThresholdTxPower.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmThresholdTxPower.setUnits(_O)
class _H3cPosaFcmThresholdAnswerTone_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,42))
_H3cPosaFcmThresholdAnswerTone_Type.__name__=_D
_H3cPosaFcmThresholdAnswerTone_Object=MibTableColumn
h3cPosaFcmThresholdAnswerTone=_H3cPosaFcmThresholdAnswerTone_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,9,1,8),_H3cPosaFcmThresholdAnswerTone_Type())
h3cPosaFcmThresholdAnswerTone.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmThresholdAnswerTone.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmThresholdAnswerTone.setUnits(_O)
_H3cPosaCallerStatTable_Object=MibTable
h3cPosaCallerStatTable=_H3cPosaCallerStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10))
if mibBuilder.loadTexts:h3cPosaCallerStatTable.setStatus(_A)
_H3cPosaCallerStatEntry_Object=MibTableRow
h3cPosaCallerStatEntry=_H3cPosaCallerStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1))
h3cPosaCallerStatEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:h3cPosaCallerStatEntry.setStatus(_A)
class _H3cPosaCallerStatCallerID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cPosaCallerStatCallerID_Type.__name__=_I
_H3cPosaCallerStatCallerID_Object=MibTableColumn
h3cPosaCallerStatCallerID=_H3cPosaCallerStatCallerID_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1,1),_H3cPosaCallerStatCallerID_Type())
h3cPosaCallerStatCallerID.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPosaCallerStatCallerID.setStatus(_A)
_H3cPosaCallerRecvPkts_Type=Counter64
_H3cPosaCallerRecvPkts_Object=MibTableColumn
h3cPosaCallerRecvPkts=_H3cPosaCallerRecvPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1,2),_H3cPosaCallerRecvPkts_Type())
h3cPosaCallerRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaCallerRecvPkts.setStatus(_A)
_H3cPosaCallerSendPkts_Type=Counter64
_H3cPosaCallerSendPkts_Object=MibTableColumn
h3cPosaCallerSendPkts=_H3cPosaCallerSendPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1,3),_H3cPosaCallerSendPkts_Type())
h3cPosaCallerSendPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaCallerSendPkts.setStatus(_A)
_H3cPosaCallerErrPkts_Type=Counter64
_H3cPosaCallerErrPkts_Object=MibTableColumn
h3cPosaCallerErrPkts=_H3cPosaCallerErrPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1,4),_H3cPosaCallerErrPkts_Type())
h3cPosaCallerErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaCallerErrPkts.setStatus(_A)
_H3cPosaCallerMapErrCnts_Type=Counter64
_H3cPosaCallerMapErrCnts_Object=MibTableColumn
h3cPosaCallerMapErrCnts=_H3cPosaCallerMapErrCnts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1,5),_H3cPosaCallerMapErrCnts_Type())
h3cPosaCallerMapErrCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaCallerMapErrCnts.setStatus(_A)
_H3cPosaCallerInDiscardedPkts_Type=Counter64
_H3cPosaCallerInDiscardedPkts_Object=MibTableColumn
h3cPosaCallerInDiscardedPkts=_H3cPosaCallerInDiscardedPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1,6),_H3cPosaCallerInDiscardedPkts_Type())
h3cPosaCallerInDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaCallerInDiscardedPkts.setStatus(_A)
_H3cPosaCallerOutDiscardedPkts_Type=Counter64
_H3cPosaCallerOutDiscardedPkts_Object=MibTableColumn
h3cPosaCallerOutDiscardedPkts=_H3cPosaCallerOutDiscardedPkts_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1,7),_H3cPosaCallerOutDiscardedPkts_Type())
h3cPosaCallerOutDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPosaCallerOutDiscardedPkts.setStatus(_A)
_H3cPosaCallerStatRowStatus_Type=RowStatus
_H3cPosaCallerStatRowStatus_Object=MibTableColumn
h3cPosaCallerStatRowStatus=_H3cPosaCallerStatRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,92,2,10,1,8),_H3cPosaCallerStatRowStatus_Type())
h3cPosaCallerStatRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaCallerStatRowStatus.setStatus(_A)
_H3cPosaTrap_ObjectIdentity=ObjectIdentity
h3cPosaTrap=_H3cPosaTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,92,3))
_H3cPosaTrapPrex_ObjectIdentity=ObjectIdentity
h3cPosaTrapPrex=_H3cPosaTrapPrex_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,92,3,0))
_H3cPosaTrapObjects_ObjectIdentity=ObjectIdentity
h3cPosaTrapObjects=_H3cPosaTrapObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,92,3,1))
class _H3cPosaAppStateChangeObject_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('available',1),('unavailable',2)))
_H3cPosaAppStateChangeObject_Type.__name__=_D
_H3cPosaAppStateChangeObject_Object=MibScalar
h3cPosaAppStateChangeObject=_H3cPosaAppStateChangeObject_Object((1,3,6,1,4,1,43,45,1,10,2,92,3,1,1),_H3cPosaAppStateChangeObject_Type())
h3cPosaAppStateChangeObject.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cPosaAppStateChangeObject.setStatus(_A)
h3cPosaServerStatusChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,92,3,0,1))
h3cPosaServerStatusChange.setObjects((_F,_b))
if mibBuilder.loadTexts:h3cPosaServerStatusChange.setStatus(_A)
h3cPosaAppStateChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,92,3,0,2))
h3cPosaAppStateChange.setObjects(*((_F,_N),(_F,_c)))
if mibBuilder.loadTexts:h3cPosaAppStateChange.setStatus(_A)
h3cPosaTerminalHangUp=NotificationType((1,3,6,1,4,1,43,45,1,10,2,92,3,0,3))
h3cPosaTerminalHangUp.setObjects(*((_G,_J),(_G,_M)))
if mibBuilder.loadTexts:h3cPosaTerminalHangUp.setStatus(_A)
h3cPosaFcmLinkNegoFailed=NotificationType((1,3,6,1,4,1,43,45,1,10,2,92,3,0,4))
h3cPosaFcmLinkNegoFailed.setObjects(*((_G,_J),(_G,_M)))
if mibBuilder.loadTexts:h3cPosaFcmLinkNegoFailed.setStatus(_A)
h3cPosaFcmPhyNegoFailed=NotificationType((1,3,6,1,4,1,43,45,1,10,2,92,3,0,5))
h3cPosaFcmPhyNegoFailed.setObjects(*((_G,_J),(_G,_M)))
if mibBuilder.loadTexts:h3cPosaFcmPhyNegoFailed.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_S:H3cAppServiceType,_T:H3cAppMode,'H3cPeerState':H3cPeerState,_V:H3cTerminalAccessType,_U:H3cTpduChangeStrategy,'h3cPosa':h3cPosa,'h3cPosaControl':h3cPosaControl,_b:h3cPosaServerEnable,'h3cPosaFcmAnswerTimeout':h3cPosaFcmAnswerTimeout,'h3cPosaFcmTradeTimeout':h3cPosaFcmTradeTimeout,'h3cPosaFcmIdleTimeout':h3cPosaFcmIdleTimeout,'h3cPosaSrvStateChangeTrapEnable':h3cPosaSrvStateChangeTrapEnable,'h3cPosaAppStateChangeTrapEnable':h3cPosaAppStateChangeTrapEnable,'h3cPosaTerminalHangUpTrapEnable':h3cPosaTerminalHangUpTrapEnable,'h3cPosaFcmLnkNegoFailTrapEnable':h3cPosaFcmLnkNegoFailTrapEnable,'h3cPosaFcmPhyNegoFailTrapEnable':h3cPosaFcmPhyNegoFailTrapEnable,'h3cPosaTables':h3cPosaTables,'h3cPosaAppTable':h3cPosaAppTable,'h3cPosaAppEntry':h3cPosaAppEntry,_N:h3cPosaAppID,'h3cPosaAppServiceType':h3cPosaAppServiceType,'h3cPosaAppIfIndex':h3cPosaAppIfIndex,'h3cPosaAppMode':h3cPosaAppMode,'h3cPosaAppHostIPType':h3cPosaAppHostIPType,'h3cPosaAppHostIP':h3cPosaAppHostIP,'h3cPosaAppHostPort':h3cPosaAppHostPort,'h3cPosaAppRouterIPType':h3cPosaAppRouterIPType,'h3cPosaAppRouterIP':h3cPosaAppRouterIP,'h3cPosaAppKeepAliveInterval':h3cPosaAppKeepAliveInterval,'h3cPosaAppKeepAliveCount':h3cPosaAppKeepAliveCount,'h3cPosaAppConnectTimeout':h3cPosaAppConnectTimeout,'h3cPosaAppState':h3cPosaAppState,'h3cPosaAppRowStatus':h3cPosaAppRowStatus,'h3cPosaAppName':h3cPosaAppName,'h3cPosaCallerIDTransEnable':h3cPosaCallerIDTransEnable,'h3cPosaTpduChangeStrategy':h3cPosaTpduChangeStrategy,'h3cPosaBackupAppID':h3cPosaBackupAppID,'h3cPosaQuietTimeOut':h3cPosaQuietTimeOut,'h3cPosaAppHello':h3cPosaAppHello,'h3cPosaAppHelloInterval':h3cPosaAppHelloInterval,'h3cPosaAppRouterPort':h3cPosaAppRouterPort,'h3cPosaTerminalTable':h3cPosaTerminalTable,'h3cPosaTerminalEntry':h3cPosaTerminalEntry,_Q:h3cPosaTerminalID,'h3cPosaTerminalAccessType':h3cPosaTerminalAccessType,'h3cPosaTerminalIfIndex':h3cPosaTerminalIfIndex,'h3cPosaTerminalTransAppID':h3cPosaTerminalTransAppID,'h3cPosaTerminalListenPort':h3cPosaTerminalListenPort,'h3cPosaTerminalState':h3cPosaTerminalState,'h3cPosaTerminalRowStatus':h3cPosaTerminalRowStatus,'h3cPosaTerminalName':h3cPosaTerminalName,'h3cPosaTerminalCfgIfIndex':h3cPosaTerminalCfgIfIndex,'h3cPosaMapTable':h3cPosaMapTable,'h3cPosaMapEntry':h3cPosaMapEntry,_X:h3cPosaMapDestCode,'h3cPosaMapAppID':h3cPosaMapAppID,'h3cPosaMapRowStatus':h3cPosaMapRowStatus,_W:h3cPosaMapSrcCode,'h3cPosaFcmStatTable':h3cPosaFcmStatTable,'h3cPosaFcmStatEntry':h3cPosaFcmStatEntry,_Y:h3cPosaFcmStatIfIndex,'h3cPosaFcmStatTimeoutCnts':h3cPosaFcmStatTimeoutCnts,'h3cPosaFcmStatConnectFailCnts':h3cPosaFcmStatConnectFailCnts,'h3cPosaFcmStatTransCnts':h3cPosaFcmStatTransCnts,'h3cPosaFcmStatTransSuccessCnts':h3cPosaFcmStatTransSuccessCnts,'h3cPosaFcmStatTransCntsClear':h3cPosaFcmStatTransCntsClear,'h3cPosaAppStatTable':h3cPosaAppStatTable,'h3cPosaAppStatEntry':h3cPosaAppStatEntry,'h3cPosaAppRecvPkts':h3cPosaAppRecvPkts,'h3cPosaAppSendPkts':h3cPosaAppSendPkts,'h3cPosaAppErrPkts':h3cPosaAppErrPkts,'h3cPosaAppDistributeErrCnts':h3cPosaAppDistributeErrCnts,'h3cPosaAppInDiscardedPkts':h3cPosaAppInDiscardedPkts,'h3cPosaAppOutDiscardedPkts':h3cPosaAppOutDiscardedPkts,'h3cPosaTerminalStatTable':h3cPosaTerminalStatTable,'h3cPosaTerminalStatEntry':h3cPosaTerminalStatEntry,'h3cPosaTerminalRecvPkts':h3cPosaTerminalRecvPkts,'h3cPosaTerminalSendPkts':h3cPosaTerminalSendPkts,'h3cPosaTerminalErrPkts':h3cPosaTerminalErrPkts,'h3cPosaTerminalMapErrCnts':h3cPosaTerminalMapErrCnts,'h3cPosaTerminalInDiscardedPkts':h3cPosaTerminalInDiscardedPkts,'h3cPosaTerminalOutDiscardedPkts':h3cPosaTerminalOutDiscardedPkts,'h3cPosaBatchTerminalTable':h3cPosaBatchTerminalTable,'h3cPosaBatchTerminalEntry':h3cPosaBatchTerminalEntry,'h3cPosaBatchTerminalFirstID':h3cPosaBatchTerminalFirstID,'h3cPosaBatchTerminalRowStatus':h3cPosaBatchTerminalRowStatus,'h3cPosaTcpTermStatTable':h3cPosaTcpTermStatTable,'h3cPosaTcpTermStatEntry':h3cPosaTcpTermStatEntry,_Z:h3cPosaTcpTermStatIndex,'h3cPosaTcpTermStatIPType':h3cPosaTcpTermStatIPType,'h3cPosaTcpTermStatIP':h3cPosaTcpTermStatIP,'h3cPosaTcpTermStatIPMask':h3cPosaTcpTermStatIPMask,'h3cPosaTcpTermRecvPkts':h3cPosaTcpTermRecvPkts,'h3cPosaTcpTermSendPkts':h3cPosaTcpTermSendPkts,'h3cPosaTcpTermErrPkts':h3cPosaTcpTermErrPkts,'h3cPosaTcpTermMapErrCnts':h3cPosaTcpTermMapErrCnts,'h3cPosaTcpTermInDiscardedPkts':h3cPosaTcpTermInDiscardedPkts,'h3cPosaTcpTermOutDiscardedPkts':h3cPosaTcpTermOutDiscardedPkts,'h3cPosaTcpTermStatRowStatus':h3cPosaTcpTermStatRowStatus,'h3cPosaFcmConfTable':h3cPosaFcmConfTable,'h3cPosaFcmConfEntry':h3cPosaFcmConfEntry,'h3cPosaFcmNegoHookOff':h3cPosaFcmNegoHookOff,'h3cPosaFcmNegoSilence':h3cPosaFcmNegoSilence,'h3cPosaFcmNegoScrmbBinary1':h3cPosaFcmNegoScrmbBinary1,'h3cPosaFcmNegoUnscrmbBinary1':h3cPosaFcmNegoUnscrmbBinary1,'h3cPosaFcmThresholdRlsdOff':h3cPosaFcmThresholdRlsdOff,'h3cPosaFcmThresholdRlsdOn':h3cPosaFcmThresholdRlsdOn,'h3cPosaFcmThresholdTxPower':h3cPosaFcmThresholdTxPower,'h3cPosaFcmThresholdAnswerTone':h3cPosaFcmThresholdAnswerTone,'h3cPosaCallerStatTable':h3cPosaCallerStatTable,'h3cPosaCallerStatEntry':h3cPosaCallerStatEntry,_a:h3cPosaCallerStatCallerID,'h3cPosaCallerRecvPkts':h3cPosaCallerRecvPkts,'h3cPosaCallerSendPkts':h3cPosaCallerSendPkts,'h3cPosaCallerErrPkts':h3cPosaCallerErrPkts,'h3cPosaCallerMapErrCnts':h3cPosaCallerMapErrCnts,'h3cPosaCallerInDiscardedPkts':h3cPosaCallerInDiscardedPkts,'h3cPosaCallerOutDiscardedPkts':h3cPosaCallerOutDiscardedPkts,'h3cPosaCallerStatRowStatus':h3cPosaCallerStatRowStatus,'h3cPosaTrap':h3cPosaTrap,'h3cPosaTrapPrex':h3cPosaTrapPrex,'h3cPosaServerStatusChange':h3cPosaServerStatusChange,'h3cPosaAppStateChange':h3cPosaAppStateChange,'h3cPosaTerminalHangUp':h3cPosaTerminalHangUp,'h3cPosaFcmLinkNegoFailed':h3cPosaFcmLinkNegoFailed,'h3cPosaFcmPhyNegoFailed':h3cPosaFcmPhyNegoFailed,'h3cPosaTrapObjects':h3cPosaTrapObjects,_c:h3cPosaAppStateChangeObject})