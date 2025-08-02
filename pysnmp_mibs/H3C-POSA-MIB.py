_j='h3cPosaE1DialFallingThreshold'
_i='h3cPosaTradeSuccessFallingThreshold'
_h='h3cPosaTcpTradeLimit'
_g='h3cPosaFcmConnectionThreshold'
_f='h3cPosaTcpConnectionThreshold'
_e='h3cPosaAppStateChangeObject'
_d='h3cPosaServerEnable'
_c='h3cPosaE1StatIndex'
_b='h3cPosaTcpTermStatIndex'
_a='h3cPosaFcmStatIfIndex'
_Z='h3cPosaMapDestCode'
_Y='h3cPosaMapSrcCode'
_X='H3cTerminalAccessType'
_W='H3cTpduChangeStrategy'
_V='H3cAppMode'
_U='H3cAppServiceType'
_T='h3cPosaNiiStatIndex'
_S='seconds'
_R='-dBm'
_Q='h3cPosaTerminalID'
_P='h3cPosaAppID'
_O='not-accessible'
_N='accessible-for-notify'
_M='h3cPosaCallerStatCallerID'
_L='milliseconds'
_K='ifDescr'
_J='OctetString'
_I='ifIndex'
_H='IF-MIB'
_G='TruthValue'
_F='H3C-POSA-MIB'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_H,_K,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
h3cPosa=ModuleIdentity((1,3,6,1,4,1,2011,10,2,92))
if mibBuilder.loadTexts:h3cPosa.setRevisions(('2015-08-26 00:00','2014-11-14 00:00','2008-03-12 09:33'))
class H3cAppServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('flow',2)))
class H3cAppMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('temporary',2)))
class H3cPeerState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('notset',1),('down',2),('up',3),('kept',4),('linking',5),('linked',6),('multilink',7),('blocked',8),('error',9)))
class H3cTerminalAccessType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fcm',1),('flow',2),('tcp',3)))
class H3cTpduChangeStrategy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('changeTpduSrc',1),('changeTpduDest',2)))
_H3cPosaControl_ObjectIdentity=ObjectIdentity
h3cPosaControl=_H3cPosaControl_ObjectIdentity((1,3,6,1,4,1,2011,10,2,92,1))
class _H3cPosaServerEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_H3cPosaServerEnable_Type.__name__=_C
_H3cPosaServerEnable_Object=MibScalar
h3cPosaServerEnable=_H3cPosaServerEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,1),_H3cPosaServerEnable_Type())
h3cPosaServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaServerEnable.setStatus(_A)
class _H3cPosaFcmAnswerTimeout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2000))
_H3cPosaFcmAnswerTimeout_Type.__name__=_C
_H3cPosaFcmAnswerTimeout_Object=MibScalar
h3cPosaFcmAnswerTimeout=_H3cPosaFcmAnswerTimeout_Object((1,3,6,1,4,1,2011,10,2,92,1,2),_H3cPosaFcmAnswerTimeout_Type())
h3cPosaFcmAnswerTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmAnswerTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmAnswerTimeout.setUnits(_L)
class _H3cPosaFcmTradeTimeout_Type(Integer32):defaultValue=12000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30000,12000000))
_H3cPosaFcmTradeTimeout_Type.__name__=_C
_H3cPosaFcmTradeTimeout_Object=MibScalar
h3cPosaFcmTradeTimeout=_H3cPosaFcmTradeTimeout_Object((1,3,6,1,4,1,2011,10,2,92,1,3),_H3cPosaFcmTradeTimeout_Type())
h3cPosaFcmTradeTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmTradeTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmTradeTimeout.setUnits(_L)
class _H3cPosaFcmIdleTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12000))
_H3cPosaFcmIdleTimeout_Type.__name__=_C
_H3cPosaFcmIdleTimeout_Object=MibScalar
h3cPosaFcmIdleTimeout=_H3cPosaFcmIdleTimeout_Object((1,3,6,1,4,1,2011,10,2,92,1,4),_H3cPosaFcmIdleTimeout_Type())
h3cPosaFcmIdleTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmIdleTimeout.setUnits(_S)
class _H3cPosaSrvStateChangeTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaSrvStateChangeTrapEnable_Type.__name__=_G
_H3cPosaSrvStateChangeTrapEnable_Object=MibScalar
h3cPosaSrvStateChangeTrapEnable=_H3cPosaSrvStateChangeTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,5),_H3cPosaSrvStateChangeTrapEnable_Type())
h3cPosaSrvStateChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaSrvStateChangeTrapEnable.setStatus(_A)
class _H3cPosaAppStateChangeTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaAppStateChangeTrapEnable_Type.__name__=_G
_H3cPosaAppStateChangeTrapEnable_Object=MibScalar
h3cPosaAppStateChangeTrapEnable=_H3cPosaAppStateChangeTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,6),_H3cPosaAppStateChangeTrapEnable_Type())
h3cPosaAppStateChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaAppStateChangeTrapEnable.setStatus(_A)
class _H3cPosaTerminalHangUpTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaTerminalHangUpTrapEnable_Type.__name__=_G
_H3cPosaTerminalHangUpTrapEnable_Object=MibScalar
h3cPosaTerminalHangUpTrapEnable=_H3cPosaTerminalHangUpTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,7),_H3cPosaTerminalHangUpTrapEnable_Type())
h3cPosaTerminalHangUpTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTerminalHangUpTrapEnable.setStatus(_A)
class _H3cPosaFcmLnkNegoFailTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaFcmLnkNegoFailTrapEnable_Type.__name__=_G
_H3cPosaFcmLnkNegoFailTrapEnable_Object=MibScalar
h3cPosaFcmLnkNegoFailTrapEnable=_H3cPosaFcmLnkNegoFailTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,8),_H3cPosaFcmLnkNegoFailTrapEnable_Type())
h3cPosaFcmLnkNegoFailTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmLnkNegoFailTrapEnable.setStatus(_A)
class _H3cPosaFcmPhyNegoFailTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaFcmPhyNegoFailTrapEnable_Type.__name__=_G
_H3cPosaFcmPhyNegoFailTrapEnable_Object=MibScalar
h3cPosaFcmPhyNegoFailTrapEnable=_H3cPosaFcmPhyNegoFailTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,9),_H3cPosaFcmPhyNegoFailTrapEnable_Type())
h3cPosaFcmPhyNegoFailTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmPhyNegoFailTrapEnable.setStatus(_A)
_H3cPosaTcpConnectionNumber_Type=Integer32
_H3cPosaTcpConnectionNumber_Object=MibScalar
h3cPosaTcpConnectionNumber=_H3cPosaTcpConnectionNumber_Object((1,3,6,1,4,1,2011,10,2,92,1,10),_H3cPosaTcpConnectionNumber_Type())
h3cPosaTcpConnectionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpConnectionNumber.setStatus(_A)
_H3cPosaFcmConnectionNumber_Type=Integer32
_H3cPosaFcmConnectionNumber_Object=MibScalar
h3cPosaFcmConnectionNumber=_H3cPosaFcmConnectionNumber_Object((1,3,6,1,4,1,2011,10,2,92,1,11),_H3cPosaFcmConnectionNumber_Type())
h3cPosaFcmConnectionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaFcmConnectionNumber.setStatus(_A)
class _H3cPosaTcpConnectionThreshold_Type(Integer32):defaultValue=4096
_H3cPosaTcpConnectionThreshold_Type.__name__=_C
_H3cPosaTcpConnectionThreshold_Object=MibScalar
h3cPosaTcpConnectionThreshold=_H3cPosaTcpConnectionThreshold_Object((1,3,6,1,4,1,2011,10,2,92,1,12),_H3cPosaTcpConnectionThreshold_Type())
h3cPosaTcpConnectionThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTcpConnectionThreshold.setStatus(_A)
class _H3cPosaFcmConnectionThreshold_Type(Integer32):defaultValue=1024
_H3cPosaFcmConnectionThreshold_Type.__name__=_C
_H3cPosaFcmConnectionThreshold_Object=MibScalar
h3cPosaFcmConnectionThreshold=_H3cPosaFcmConnectionThreshold_Object((1,3,6,1,4,1,2011,10,2,92,1,13),_H3cPosaFcmConnectionThreshold_Type())
h3cPosaFcmConnectionThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmConnectionThreshold.setStatus(_A)
class _H3cPosaTcpConnectionTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaTcpConnectionTrapEnable_Type.__name__=_G
_H3cPosaTcpConnectionTrapEnable_Object=MibScalar
h3cPosaTcpConnectionTrapEnable=_H3cPosaTcpConnectionTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,14),_H3cPosaTcpConnectionTrapEnable_Type())
h3cPosaTcpConnectionTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTcpConnectionTrapEnable.setStatus(_A)
class _H3cPosaFcmConnectionTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaFcmConnectionTrapEnable_Type.__name__=_G
_H3cPosaFcmConnectionTrapEnable_Object=MibScalar
h3cPosaFcmConnectionTrapEnable=_H3cPosaFcmConnectionTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,15),_H3cPosaFcmConnectionTrapEnable_Type())
h3cPosaFcmConnectionTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmConnectionTrapEnable.setStatus(_A)
class _H3cPosaTcpTradeLimit_Type(Integer32):defaultValue=0
_H3cPosaTcpTradeLimit_Type.__name__=_C
_H3cPosaTcpTradeLimit_Object=MibScalar
h3cPosaTcpTradeLimit=_H3cPosaTcpTradeLimit_Object((1,3,6,1,4,1,2011,10,2,92,1,16),_H3cPosaTcpTradeLimit_Type())
h3cPosaTcpTradeLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTcpTradeLimit.setStatus(_A)
class _H3cPosaTcpTradeTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaTcpTradeTrapEnable_Type.__name__=_G
_H3cPosaTcpTradeTrapEnable_Object=MibScalar
h3cPosaTcpTradeTrapEnable=_H3cPosaTcpTradeTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,17),_H3cPosaTcpTradeTrapEnable_Type())
h3cPosaTcpTradeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTcpTradeTrapEnable.setStatus(_A)
class _H3cPosaTcpTradeTimeout_Type(Integer32):defaultValue=240
_H3cPosaTcpTradeTimeout_Type.__name__=_C
_H3cPosaTcpTradeTimeout_Object=MibScalar
h3cPosaTcpTradeTimeout=_H3cPosaTcpTradeTimeout_Object((1,3,6,1,4,1,2011,10,2,92,1,18),_H3cPosaTcpTradeTimeout_Type())
h3cPosaTcpTradeTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTcpTradeTimeout.setStatus(_A)
class _H3cPosaTradeSuccessFallingTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaTradeSuccessFallingTrapEnable_Type.__name__=_G
_H3cPosaTradeSuccessFallingTrapEnable_Object=MibScalar
h3cPosaTradeSuccessFallingTrapEnable=_H3cPosaTradeSuccessFallingTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,19),_H3cPosaTradeSuccessFallingTrapEnable_Type())
h3cPosaTradeSuccessFallingTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTradeSuccessFallingTrapEnable.setStatus(_A)
class _H3cPosaTradeSuccessFallingThreshold_Type(Integer32):defaultValue=90
_H3cPosaTradeSuccessFallingThreshold_Type.__name__=_C
_H3cPosaTradeSuccessFallingThreshold_Object=MibScalar
h3cPosaTradeSuccessFallingThreshold=_H3cPosaTradeSuccessFallingThreshold_Object((1,3,6,1,4,1,2011,10,2,92,1,20),_H3cPosaTradeSuccessFallingThreshold_Type())
h3cPosaTradeSuccessFallingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaTradeSuccessFallingThreshold.setStatus(_A)
class _H3cPosaE1DialFallingTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaE1DialFallingTrapEnable_Type.__name__=_G
_H3cPosaE1DialFallingTrapEnable_Object=MibScalar
h3cPosaE1DialFallingTrapEnable=_H3cPosaE1DialFallingTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,21),_H3cPosaE1DialFallingTrapEnable_Type())
h3cPosaE1DialFallingTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaE1DialFallingTrapEnable.setStatus(_A)
class _H3cPosaE1DialFallingThreshold_Type(Integer32):defaultValue=90
_H3cPosaE1DialFallingThreshold_Type.__name__=_C
_H3cPosaE1DialFallingThreshold_Object=MibScalar
h3cPosaE1DialFallingThreshold=_H3cPosaE1DialFallingThreshold_Object((1,3,6,1,4,1,2011,10,2,92,1,22),_H3cPosaE1DialFallingThreshold_Type())
h3cPosaE1DialFallingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaE1DialFallingThreshold.setStatus(_A)
class _H3cPosaFcmTradeAbnormalTrapEnable_Type(TruthValue):defaultValue=1
_H3cPosaFcmTradeAbnormalTrapEnable_Type.__name__=_G
_H3cPosaFcmTradeAbnormalTrapEnable_Object=MibScalar
h3cPosaFcmTradeAbnormalTrapEnable=_H3cPosaFcmTradeAbnormalTrapEnable_Object((1,3,6,1,4,1,2011,10,2,92,1,23),_H3cPosaFcmTradeAbnormalTrapEnable_Type())
h3cPosaFcmTradeAbnormalTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmTradeAbnormalTrapEnable.setStatus(_A)
_H3cPosaTables_ObjectIdentity=ObjectIdentity
h3cPosaTables=_H3cPosaTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,92,2))
_H3cPosaAppTable_Object=MibTable
h3cPosaAppTable=_H3cPosaAppTable_Object((1,3,6,1,4,1,2011,10,2,92,2,1))
if mibBuilder.loadTexts:h3cPosaAppTable.setStatus(_A)
_H3cPosaAppEntry_Object=MibTableRow
h3cPosaAppEntry=_H3cPosaAppEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1))
h3cPosaAppEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:h3cPosaAppEntry.setStatus(_A)
class _H3cPosaAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cPosaAppID_Type.__name__=_C
_H3cPosaAppID_Object=MibTableColumn
h3cPosaAppID=_H3cPosaAppID_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,1),_H3cPosaAppID_Type())
h3cPosaAppID.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cPosaAppID.setStatus(_A)
class _H3cPosaAppServiceType_Type(H3cAppServiceType):defaultValue=1
_H3cPosaAppServiceType_Type.__name__=_U
_H3cPosaAppServiceType_Object=MibTableColumn
h3cPosaAppServiceType=_H3cPosaAppServiceType_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,2),_H3cPosaAppServiceType_Type())
h3cPosaAppServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppServiceType.setStatus(_A)
_H3cPosaAppIfIndex_Type=Integer32
_H3cPosaAppIfIndex_Object=MibTableColumn
h3cPosaAppIfIndex=_H3cPosaAppIfIndex_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,3),_H3cPosaAppIfIndex_Type())
h3cPosaAppIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppIfIndex.setStatus(_A)
class _H3cPosaAppMode_Type(H3cAppMode):defaultValue=1
_H3cPosaAppMode_Type.__name__=_V
_H3cPosaAppMode_Object=MibTableColumn
h3cPosaAppMode=_H3cPosaAppMode_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,4),_H3cPosaAppMode_Type())
h3cPosaAppMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppMode.setStatus(_A)
_H3cPosaAppHostIPType_Type=InetAddressType
_H3cPosaAppHostIPType_Object=MibTableColumn
h3cPosaAppHostIPType=_H3cPosaAppHostIPType_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,5),_H3cPosaAppHostIPType_Type())
h3cPosaAppHostIPType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppHostIPType.setStatus(_A)
_H3cPosaAppHostIP_Type=InetAddress
_H3cPosaAppHostIP_Object=MibTableColumn
h3cPosaAppHostIP=_H3cPosaAppHostIP_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,6),_H3cPosaAppHostIP_Type())
h3cPosaAppHostIP.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppHostIP.setStatus(_A)
class _H3cPosaAppHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cPosaAppHostPort_Type.__name__=_C
_H3cPosaAppHostPort_Object=MibTableColumn
h3cPosaAppHostPort=_H3cPosaAppHostPort_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,7),_H3cPosaAppHostPort_Type())
h3cPosaAppHostPort.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppHostPort.setStatus(_A)
_H3cPosaAppRouterIPType_Type=InetAddressType
_H3cPosaAppRouterIPType_Object=MibTableColumn
h3cPosaAppRouterIPType=_H3cPosaAppRouterIPType_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,8),_H3cPosaAppRouterIPType_Type())
h3cPosaAppRouterIPType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppRouterIPType.setStatus(_A)
_H3cPosaAppRouterIP_Type=InetAddress
_H3cPosaAppRouterIP_Object=MibTableColumn
h3cPosaAppRouterIP=_H3cPosaAppRouterIP_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,9),_H3cPosaAppRouterIP_Type())
h3cPosaAppRouterIP.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppRouterIP.setStatus(_A)
class _H3cPosaAppKeepAliveInterval_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7200))
_H3cPosaAppKeepAliveInterval_Type.__name__=_C
_H3cPosaAppKeepAliveInterval_Object=MibTableColumn
h3cPosaAppKeepAliveInterval=_H3cPosaAppKeepAliveInterval_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,10),_H3cPosaAppKeepAliveInterval_Type())
h3cPosaAppKeepAliveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaAppKeepAliveInterval.setUnits(_S)
class _H3cPosaAppKeepAliveCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100))
_H3cPosaAppKeepAliveCount_Type.__name__=_C
_H3cPosaAppKeepAliveCount_Object=MibTableColumn
h3cPosaAppKeepAliveCount=_H3cPosaAppKeepAliveCount_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,11),_H3cPosaAppKeepAliveCount_Type())
h3cPosaAppKeepAliveCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppKeepAliveCount.setStatus(_A)
class _H3cPosaAppConnectTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_H3cPosaAppConnectTimeout_Type.__name__=_C
_H3cPosaAppConnectTimeout_Object=MibTableColumn
h3cPosaAppConnectTimeout=_H3cPosaAppConnectTimeout_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,12),_H3cPosaAppConnectTimeout_Type())
h3cPosaAppConnectTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppConnectTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaAppConnectTimeout.setUnits(_S)
_H3cPosaAppState_Type=H3cPeerState
_H3cPosaAppState_Object=MibTableColumn
h3cPosaAppState=_H3cPosaAppState_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,13),_H3cPosaAppState_Type())
h3cPosaAppState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppState.setStatus(_A)
_H3cPosaAppRowStatus_Type=RowStatus
_H3cPosaAppRowStatus_Object=MibTableColumn
h3cPosaAppRowStatus=_H3cPosaAppRowStatus_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,14),_H3cPosaAppRowStatus_Type())
h3cPosaAppRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppRowStatus.setStatus(_A)
class _H3cPosaAppName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cPosaAppName_Type.__name__=_J
_H3cPosaAppName_Object=MibTableColumn
h3cPosaAppName=_H3cPosaAppName_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,15),_H3cPosaAppName_Type())
h3cPosaAppName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppName.setStatus(_A)
class _H3cPosaCallerIDTransEnable_Type(TruthValue):defaultValue=2
_H3cPosaCallerIDTransEnable_Type.__name__=_G
_H3cPosaCallerIDTransEnable_Object=MibTableColumn
h3cPosaCallerIDTransEnable=_H3cPosaCallerIDTransEnable_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,16),_H3cPosaCallerIDTransEnable_Type())
h3cPosaCallerIDTransEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaCallerIDTransEnable.setStatus(_A)
class _H3cPosaTpduChangeStrategy_Type(H3cTpduChangeStrategy):defaultValue=1
_H3cPosaTpduChangeStrategy_Type.__name__=_W
_H3cPosaTpduChangeStrategy_Object=MibTableColumn
h3cPosaTpduChangeStrategy=_H3cPosaTpduChangeStrategy_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,17),_H3cPosaTpduChangeStrategy_Type())
h3cPosaTpduChangeStrategy.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTpduChangeStrategy.setStatus(_A)
class _H3cPosaBackupAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_H3cPosaBackupAppID_Type.__name__=_C
_H3cPosaBackupAppID_Object=MibTableColumn
h3cPosaBackupAppID=_H3cPosaBackupAppID_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,18),_H3cPosaBackupAppID_Type())
h3cPosaBackupAppID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaBackupAppID.setStatus(_A)
class _H3cPosaQuietTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_H3cPosaQuietTimeOut_Type.__name__=_C
_H3cPosaQuietTimeOut_Object=MibTableColumn
h3cPosaQuietTimeOut=_H3cPosaQuietTimeOut_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,19),_H3cPosaQuietTimeOut_Type())
h3cPosaQuietTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaQuietTimeOut.setStatus(_A)
class _H3cPosaAppHello_Type(TruthValue):defaultValue=2
_H3cPosaAppHello_Type.__name__=_G
_H3cPosaAppHello_Object=MibTableColumn
h3cPosaAppHello=_H3cPosaAppHello_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,20),_H3cPosaAppHello_Type())
h3cPosaAppHello.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppHello.setStatus(_A)
class _H3cPosaAppHelloInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_H3cPosaAppHelloInterval_Type.__name__=_C
_H3cPosaAppHelloInterval_Object=MibTableColumn
h3cPosaAppHelloInterval=_H3cPosaAppHelloInterval_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,21),_H3cPosaAppHelloInterval_Type())
h3cPosaAppHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppHelloInterval.setStatus(_A)
class _H3cPosaAppRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4999))
_H3cPosaAppRouterPort_Type.__name__=_C
_H3cPosaAppRouterPort_Object=MibTableColumn
h3cPosaAppRouterPort=_H3cPosaAppRouterPort_Object((1,3,6,1,4,1,2011,10,2,92,2,1,1,22),_H3cPosaAppRouterPort_Type())
h3cPosaAppRouterPort.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaAppRouterPort.setStatus(_A)
_H3cPosaTerminalTable_Object=MibTable
h3cPosaTerminalTable=_H3cPosaTerminalTable_Object((1,3,6,1,4,1,2011,10,2,92,2,2))
if mibBuilder.loadTexts:h3cPosaTerminalTable.setStatus(_A)
_H3cPosaTerminalEntry_Object=MibTableRow
h3cPosaTerminalEntry=_H3cPosaTerminalEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1))
h3cPosaTerminalEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:h3cPosaTerminalEntry.setStatus(_A)
class _H3cPosaTerminalID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cPosaTerminalID_Type.__name__=_C
_H3cPosaTerminalID_Object=MibTableColumn
h3cPosaTerminalID=_H3cPosaTerminalID_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,1),_H3cPosaTerminalID_Type())
h3cPosaTerminalID.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cPosaTerminalID.setStatus(_A)
class _H3cPosaTerminalAccessType_Type(H3cTerminalAccessType):defaultValue=1
_H3cPosaTerminalAccessType_Type.__name__=_X
_H3cPosaTerminalAccessType_Object=MibTableColumn
h3cPosaTerminalAccessType=_H3cPosaTerminalAccessType_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,2),_H3cPosaTerminalAccessType_Type())
h3cPosaTerminalAccessType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTerminalAccessType.setStatus(_A)
_H3cPosaTerminalIfIndex_Type=Integer32
_H3cPosaTerminalIfIndex_Object=MibTableColumn
h3cPosaTerminalIfIndex=_H3cPosaTerminalIfIndex_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,3),_H3cPosaTerminalIfIndex_Type())
h3cPosaTerminalIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTerminalIfIndex.setStatus(_A)
class _H3cPosaTerminalTransAppID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_H3cPosaTerminalTransAppID_Type.__name__=_C
_H3cPosaTerminalTransAppID_Object=MibTableColumn
h3cPosaTerminalTransAppID=_H3cPosaTerminalTransAppID_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,4),_H3cPosaTerminalTransAppID_Type())
h3cPosaTerminalTransAppID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTerminalTransAppID.setStatus(_A)
class _H3cPosaTerminalListenPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cPosaTerminalListenPort_Type.__name__=_C
_H3cPosaTerminalListenPort_Object=MibTableColumn
h3cPosaTerminalListenPort=_H3cPosaTerminalListenPort_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,5),_H3cPosaTerminalListenPort_Type())
h3cPosaTerminalListenPort.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTerminalListenPort.setStatus(_A)
_H3cPosaTerminalState_Type=H3cPeerState
_H3cPosaTerminalState_Object=MibTableColumn
h3cPosaTerminalState=_H3cPosaTerminalState_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,6),_H3cPosaTerminalState_Type())
h3cPosaTerminalState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalState.setStatus(_A)
_H3cPosaTerminalRowStatus_Type=RowStatus
_H3cPosaTerminalRowStatus_Object=MibTableColumn
h3cPosaTerminalRowStatus=_H3cPosaTerminalRowStatus_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,7),_H3cPosaTerminalRowStatus_Type())
h3cPosaTerminalRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTerminalRowStatus.setStatus(_A)
class _H3cPosaTerminalName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cPosaTerminalName_Type.__name__=_J
_H3cPosaTerminalName_Object=MibTableColumn
h3cPosaTerminalName=_H3cPosaTerminalName_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,8),_H3cPosaTerminalName_Type())
h3cPosaTerminalName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTerminalName.setStatus(_A)
_H3cPosaTerminalCfgIfIndex_Type=Integer32
_H3cPosaTerminalCfgIfIndex_Object=MibTableColumn
h3cPosaTerminalCfgIfIndex=_H3cPosaTerminalCfgIfIndex_Object((1,3,6,1,4,1,2011,10,2,92,2,2,1,9),_H3cPosaTerminalCfgIfIndex_Type())
h3cPosaTerminalCfgIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalCfgIfIndex.setStatus(_A)
_H3cPosaMapTable_Object=MibTable
h3cPosaMapTable=_H3cPosaMapTable_Object((1,3,6,1,4,1,2011,10,2,92,2,3))
if mibBuilder.loadTexts:h3cPosaMapTable.setStatus(_A)
_H3cPosaMapEntry_Object=MibTableRow
h3cPosaMapEntry=_H3cPosaMapEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,3,1))
h3cPosaMapEntry.setIndexNames((0,_F,_Y),(0,_F,_Z))
if mibBuilder.loadTexts:h3cPosaMapEntry.setStatus(_A)
class _H3cPosaMapDestCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,7))
_H3cPosaMapDestCode_Type.__name__=_J
_H3cPosaMapDestCode_Object=MibTableColumn
h3cPosaMapDestCode=_H3cPosaMapDestCode_Object((1,3,6,1,4,1,2011,10,2,92,2,3,1,1),_H3cPosaMapDestCode_Type())
h3cPosaMapDestCode.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cPosaMapDestCode.setStatus(_A)
class _H3cPosaMapAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cPosaMapAppID_Type.__name__=_C
_H3cPosaMapAppID_Object=MibTableColumn
h3cPosaMapAppID=_H3cPosaMapAppID_Object((1,3,6,1,4,1,2011,10,2,92,2,3,1,2),_H3cPosaMapAppID_Type())
h3cPosaMapAppID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaMapAppID.setStatus(_A)
_H3cPosaMapRowStatus_Type=RowStatus
_H3cPosaMapRowStatus_Object=MibTableColumn
h3cPosaMapRowStatus=_H3cPosaMapRowStatus_Object((1,3,6,1,4,1,2011,10,2,92,2,3,1,3),_H3cPosaMapRowStatus_Type())
h3cPosaMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaMapRowStatus.setStatus(_A)
class _H3cPosaMapSrcCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,7))
_H3cPosaMapSrcCode_Type.__name__=_J
_H3cPosaMapSrcCode_Object=MibTableColumn
h3cPosaMapSrcCode=_H3cPosaMapSrcCode_Object((1,3,6,1,4,1,2011,10,2,92,2,3,1,4),_H3cPosaMapSrcCode_Type())
h3cPosaMapSrcCode.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cPosaMapSrcCode.setStatus(_A)
_H3cPosaFcmStatTable_Object=MibTable
h3cPosaFcmStatTable=_H3cPosaFcmStatTable_Object((1,3,6,1,4,1,2011,10,2,92,2,4))
if mibBuilder.loadTexts:h3cPosaFcmStatTable.setStatus(_A)
_H3cPosaFcmStatEntry_Object=MibTableRow
h3cPosaFcmStatEntry=_H3cPosaFcmStatEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,4,1))
h3cPosaFcmStatEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:h3cPosaFcmStatEntry.setStatus(_A)
class _H3cPosaFcmStatIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPosaFcmStatIfIndex_Type.__name__=_C
_H3cPosaFcmStatIfIndex_Object=MibTableColumn
h3cPosaFcmStatIfIndex=_H3cPosaFcmStatIfIndex_Object((1,3,6,1,4,1,2011,10,2,92,2,4,1,1),_H3cPosaFcmStatIfIndex_Type())
h3cPosaFcmStatIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cPosaFcmStatIfIndex.setStatus(_A)
_H3cPosaFcmStatTimeoutCnts_Type=Counter32
_H3cPosaFcmStatTimeoutCnts_Object=MibTableColumn
h3cPosaFcmStatTimeoutCnts=_H3cPosaFcmStatTimeoutCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,4,1,2),_H3cPosaFcmStatTimeoutCnts_Type())
h3cPosaFcmStatTimeoutCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaFcmStatTimeoutCnts.setStatus(_A)
_H3cPosaFcmStatConnectFailCnts_Type=Counter32
_H3cPosaFcmStatConnectFailCnts_Object=MibTableColumn
h3cPosaFcmStatConnectFailCnts=_H3cPosaFcmStatConnectFailCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,4,1,3),_H3cPosaFcmStatConnectFailCnts_Type())
h3cPosaFcmStatConnectFailCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaFcmStatConnectFailCnts.setStatus(_A)
_H3cPosaFcmStatTransCnts_Type=Gauge32
_H3cPosaFcmStatTransCnts_Object=MibTableColumn
h3cPosaFcmStatTransCnts=_H3cPosaFcmStatTransCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,4,1,4),_H3cPosaFcmStatTransCnts_Type())
h3cPosaFcmStatTransCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaFcmStatTransCnts.setStatus(_A)
_H3cPosaFcmStatTransSuccessCnts_Type=Gauge32
_H3cPosaFcmStatTransSuccessCnts_Object=MibTableColumn
h3cPosaFcmStatTransSuccessCnts=_H3cPosaFcmStatTransSuccessCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,4,1,5),_H3cPosaFcmStatTransSuccessCnts_Type())
h3cPosaFcmStatTransSuccessCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaFcmStatTransSuccessCnts.setStatus(_A)
class _H3cPosaFcmStatTransCntsClear_Type(TruthValue):defaultValue=2
_H3cPosaFcmStatTransCntsClear_Type.__name__=_G
_H3cPosaFcmStatTransCntsClear_Object=MibTableColumn
h3cPosaFcmStatTransCntsClear=_H3cPosaFcmStatTransCntsClear_Object((1,3,6,1,4,1,2011,10,2,92,2,4,1,6),_H3cPosaFcmStatTransCntsClear_Type())
h3cPosaFcmStatTransCntsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmStatTransCntsClear.setStatus(_A)
_H3cPosaAppStatTable_Object=MibTable
h3cPosaAppStatTable=_H3cPosaAppStatTable_Object((1,3,6,1,4,1,2011,10,2,92,2,5))
if mibBuilder.loadTexts:h3cPosaAppStatTable.setStatus(_A)
_H3cPosaAppStatEntry_Object=MibTableRow
h3cPosaAppStatEntry=_H3cPosaAppStatEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,5,1))
h3cPosaAppStatEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:h3cPosaAppStatEntry.setStatus(_A)
_H3cPosaAppRecvPkts_Type=Counter32
_H3cPosaAppRecvPkts_Object=MibTableColumn
h3cPosaAppRecvPkts=_H3cPosaAppRecvPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,5,1,1),_H3cPosaAppRecvPkts_Type())
h3cPosaAppRecvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppRecvPkts.setStatus(_A)
_H3cPosaAppSendPkts_Type=Counter32
_H3cPosaAppSendPkts_Object=MibTableColumn
h3cPosaAppSendPkts=_H3cPosaAppSendPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,5,1,2),_H3cPosaAppSendPkts_Type())
h3cPosaAppSendPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppSendPkts.setStatus(_A)
_H3cPosaAppErrPkts_Type=Counter32
_H3cPosaAppErrPkts_Object=MibTableColumn
h3cPosaAppErrPkts=_H3cPosaAppErrPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,5,1,3),_H3cPosaAppErrPkts_Type())
h3cPosaAppErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppErrPkts.setStatus(_A)
_H3cPosaAppDistributeErrCnts_Type=Counter32
_H3cPosaAppDistributeErrCnts_Object=MibTableColumn
h3cPosaAppDistributeErrCnts=_H3cPosaAppDistributeErrCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,5,1,4),_H3cPosaAppDistributeErrCnts_Type())
h3cPosaAppDistributeErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppDistributeErrCnts.setStatus(_A)
_H3cPosaAppInDiscardedPkts_Type=Counter32
_H3cPosaAppInDiscardedPkts_Object=MibTableColumn
h3cPosaAppInDiscardedPkts=_H3cPosaAppInDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,5,1,5),_H3cPosaAppInDiscardedPkts_Type())
h3cPosaAppInDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppInDiscardedPkts.setStatus(_A)
_H3cPosaAppOutDiscardedPkts_Type=Counter32
_H3cPosaAppOutDiscardedPkts_Object=MibTableColumn
h3cPosaAppOutDiscardedPkts=_H3cPosaAppOutDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,5,1,6),_H3cPosaAppOutDiscardedPkts_Type())
h3cPosaAppOutDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaAppOutDiscardedPkts.setStatus(_A)
_H3cPosaTerminalStatTable_Object=MibTable
h3cPosaTerminalStatTable=_H3cPosaTerminalStatTable_Object((1,3,6,1,4,1,2011,10,2,92,2,6))
if mibBuilder.loadTexts:h3cPosaTerminalStatTable.setStatus(_A)
_H3cPosaTerminalStatEntry_Object=MibTableRow
h3cPosaTerminalStatEntry=_H3cPosaTerminalStatEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,6,1))
h3cPosaTerminalStatEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:h3cPosaTerminalStatEntry.setStatus(_A)
_H3cPosaTerminalRecvPkts_Type=Counter32
_H3cPosaTerminalRecvPkts_Object=MibTableColumn
h3cPosaTerminalRecvPkts=_H3cPosaTerminalRecvPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,6,1,1),_H3cPosaTerminalRecvPkts_Type())
h3cPosaTerminalRecvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalRecvPkts.setStatus(_A)
_H3cPosaTerminalSendPkts_Type=Counter32
_H3cPosaTerminalSendPkts_Object=MibTableColumn
h3cPosaTerminalSendPkts=_H3cPosaTerminalSendPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,6,1,2),_H3cPosaTerminalSendPkts_Type())
h3cPosaTerminalSendPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalSendPkts.setStatus(_A)
_H3cPosaTerminalErrPkts_Type=Counter32
_H3cPosaTerminalErrPkts_Object=MibTableColumn
h3cPosaTerminalErrPkts=_H3cPosaTerminalErrPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,6,1,3),_H3cPosaTerminalErrPkts_Type())
h3cPosaTerminalErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalErrPkts.setStatus(_A)
_H3cPosaTerminalMapErrCnts_Type=Counter32
_H3cPosaTerminalMapErrCnts_Object=MibTableColumn
h3cPosaTerminalMapErrCnts=_H3cPosaTerminalMapErrCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,6,1,4),_H3cPosaTerminalMapErrCnts_Type())
h3cPosaTerminalMapErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalMapErrCnts.setStatus(_A)
_H3cPosaTerminalInDiscardedPkts_Type=Counter32
_H3cPosaTerminalInDiscardedPkts_Object=MibTableColumn
h3cPosaTerminalInDiscardedPkts=_H3cPosaTerminalInDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,6,1,5),_H3cPosaTerminalInDiscardedPkts_Type())
h3cPosaTerminalInDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalInDiscardedPkts.setStatus(_A)
_H3cPosaTerminalOutDiscardedPkts_Type=Counter32
_H3cPosaTerminalOutDiscardedPkts_Object=MibTableColumn
h3cPosaTerminalOutDiscardedPkts=_H3cPosaTerminalOutDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,6,1,6),_H3cPosaTerminalOutDiscardedPkts_Type())
h3cPosaTerminalOutDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTerminalOutDiscardedPkts.setStatus(_A)
_H3cPosaTermianlTcpConnectionNumber_Type=Integer32
_H3cPosaTermianlTcpConnectionNumber_Object=MibTableColumn
h3cPosaTermianlTcpConnectionNumber=_H3cPosaTermianlTcpConnectionNumber_Object((1,3,6,1,4,1,2011,10,2,92,2,6,1,7),_H3cPosaTermianlTcpConnectionNumber_Type())
h3cPosaTermianlTcpConnectionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTermianlTcpConnectionNumber.setStatus(_A)
_H3cPosaBatchTerminalTable_Object=MibTable
h3cPosaBatchTerminalTable=_H3cPosaBatchTerminalTable_Object((1,3,6,1,4,1,2011,10,2,92,2,7))
if mibBuilder.loadTexts:h3cPosaBatchTerminalTable.setStatus(_A)
_H3cPosaBatchTerminalEntry_Object=MibTableRow
h3cPosaBatchTerminalEntry=_H3cPosaBatchTerminalEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,7,1))
h3cPosaBatchTerminalEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cPosaBatchTerminalEntry.setStatus(_A)
class _H3cPosaBatchTerminalFirstID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cPosaBatchTerminalFirstID_Type.__name__=_C
_H3cPosaBatchTerminalFirstID_Object=MibTableColumn
h3cPosaBatchTerminalFirstID=_H3cPosaBatchTerminalFirstID_Object((1,3,6,1,4,1,2011,10,2,92,2,7,1,1),_H3cPosaBatchTerminalFirstID_Type())
h3cPosaBatchTerminalFirstID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaBatchTerminalFirstID.setStatus(_A)
_H3cPosaBatchTerminalRowStatus_Type=RowStatus
_H3cPosaBatchTerminalRowStatus_Object=MibTableColumn
h3cPosaBatchTerminalRowStatus=_H3cPosaBatchTerminalRowStatus_Object((1,3,6,1,4,1,2011,10,2,92,2,7,1,2),_H3cPosaBatchTerminalRowStatus_Type())
h3cPosaBatchTerminalRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaBatchTerminalRowStatus.setStatus(_A)
_H3cPosaTcpTermStatTable_Object=MibTable
h3cPosaTcpTermStatTable=_H3cPosaTcpTermStatTable_Object((1,3,6,1,4,1,2011,10,2,92,2,8))
if mibBuilder.loadTexts:h3cPosaTcpTermStatTable.setStatus(_A)
_H3cPosaTcpTermStatEntry_Object=MibTableRow
h3cPosaTcpTermStatEntry=_H3cPosaTcpTermStatEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1))
h3cPosaTcpTermStatEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:h3cPosaTcpTermStatEntry.setStatus(_A)
class _H3cPosaTcpTermStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cPosaTcpTermStatIndex_Type.__name__=_C
_H3cPosaTcpTermStatIndex_Object=MibTableColumn
h3cPosaTcpTermStatIndex=_H3cPosaTcpTermStatIndex_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,1),_H3cPosaTcpTermStatIndex_Type())
h3cPosaTcpTermStatIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cPosaTcpTermStatIndex.setStatus(_A)
_H3cPosaTcpTermStatIPType_Type=InetAddressType
_H3cPosaTcpTermStatIPType_Object=MibTableColumn
h3cPosaTcpTermStatIPType=_H3cPosaTcpTermStatIPType_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,2),_H3cPosaTcpTermStatIPType_Type())
h3cPosaTcpTermStatIPType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTcpTermStatIPType.setStatus(_A)
_H3cPosaTcpTermStatIP_Type=InetAddress
_H3cPosaTcpTermStatIP_Object=MibTableColumn
h3cPosaTcpTermStatIP=_H3cPosaTcpTermStatIP_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,3),_H3cPosaTcpTermStatIP_Type())
h3cPosaTcpTermStatIP.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTcpTermStatIP.setStatus(_A)
_H3cPosaTcpTermStatIPMask_Type=InetAddress
_H3cPosaTcpTermStatIPMask_Object=MibTableColumn
h3cPosaTcpTermStatIPMask=_H3cPosaTcpTermStatIPMask_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,4),_H3cPosaTcpTermStatIPMask_Type())
h3cPosaTcpTermStatIPMask.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTcpTermStatIPMask.setStatus(_A)
_H3cPosaTcpTermRecvPkts_Type=Counter64
_H3cPosaTcpTermRecvPkts_Object=MibTableColumn
h3cPosaTcpTermRecvPkts=_H3cPosaTcpTermRecvPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,5),_H3cPosaTcpTermRecvPkts_Type())
h3cPosaTcpTermRecvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermRecvPkts.setStatus(_A)
_H3cPosaTcpTermSendPkts_Type=Counter64
_H3cPosaTcpTermSendPkts_Object=MibTableColumn
h3cPosaTcpTermSendPkts=_H3cPosaTcpTermSendPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,6),_H3cPosaTcpTermSendPkts_Type())
h3cPosaTcpTermSendPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermSendPkts.setStatus(_A)
_H3cPosaTcpTermErrPkts_Type=Counter64
_H3cPosaTcpTermErrPkts_Object=MibTableColumn
h3cPosaTcpTermErrPkts=_H3cPosaTcpTermErrPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,7),_H3cPosaTcpTermErrPkts_Type())
h3cPosaTcpTermErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermErrPkts.setStatus(_A)
_H3cPosaTcpTermMapErrCnts_Type=Counter64
_H3cPosaTcpTermMapErrCnts_Object=MibTableColumn
h3cPosaTcpTermMapErrCnts=_H3cPosaTcpTermMapErrCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,8),_H3cPosaTcpTermMapErrCnts_Type())
h3cPosaTcpTermMapErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermMapErrCnts.setStatus(_A)
_H3cPosaTcpTermInDiscardedPkts_Type=Counter64
_H3cPosaTcpTermInDiscardedPkts_Object=MibTableColumn
h3cPosaTcpTermInDiscardedPkts=_H3cPosaTcpTermInDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,9),_H3cPosaTcpTermInDiscardedPkts_Type())
h3cPosaTcpTermInDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermInDiscardedPkts.setStatus(_A)
_H3cPosaTcpTermOutDiscardedPkts_Type=Counter64
_H3cPosaTcpTermOutDiscardedPkts_Object=MibTableColumn
h3cPosaTcpTermOutDiscardedPkts=_H3cPosaTcpTermOutDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,10),_H3cPosaTcpTermOutDiscardedPkts_Type())
h3cPosaTcpTermOutDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaTcpTermOutDiscardedPkts.setStatus(_A)
_H3cPosaTcpTermStatRowStatus_Type=RowStatus
_H3cPosaTcpTermStatRowStatus_Object=MibTableColumn
h3cPosaTcpTermStatRowStatus=_H3cPosaTcpTermStatRowStatus_Object((1,3,6,1,4,1,2011,10,2,92,2,8,1,11),_H3cPosaTcpTermStatRowStatus_Type())
h3cPosaTcpTermStatRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaTcpTermStatRowStatus.setStatus(_A)
_H3cPosaFcmConfTable_Object=MibTable
h3cPosaFcmConfTable=_H3cPosaFcmConfTable_Object((1,3,6,1,4,1,2011,10,2,92,2,9))
if mibBuilder.loadTexts:h3cPosaFcmConfTable.setStatus(_A)
_H3cPosaFcmConfEntry_Object=MibTableRow
h3cPosaFcmConfEntry=_H3cPosaFcmConfEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1))
h3cPosaFcmConfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cPosaFcmConfEntry.setStatus(_A)
class _H3cPosaFcmNegoHookOff_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,6000))
_H3cPosaFcmNegoHookOff_Type.__name__=_C
_H3cPosaFcmNegoHookOff_Object=MibTableColumn
h3cPosaFcmNegoHookOff=_H3cPosaFcmNegoHookOff_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1,1),_H3cPosaFcmNegoHookOff_Type())
h3cPosaFcmNegoHookOff.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmNegoHookOff.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmNegoHookOff.setUnits(_L)
class _H3cPosaFcmNegoSilence_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3000))
_H3cPosaFcmNegoSilence_Type.__name__=_C
_H3cPosaFcmNegoSilence_Object=MibTableColumn
h3cPosaFcmNegoSilence=_H3cPosaFcmNegoSilence_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1,2),_H3cPosaFcmNegoSilence_Type())
h3cPosaFcmNegoSilence.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmNegoSilence.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmNegoSilence.setUnits(_L)
class _H3cPosaFcmNegoScrmbBinary1_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1500))
_H3cPosaFcmNegoScrmbBinary1_Type.__name__=_C
_H3cPosaFcmNegoScrmbBinary1_Object=MibTableColumn
h3cPosaFcmNegoScrmbBinary1=_H3cPosaFcmNegoScrmbBinary1_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1,3),_H3cPosaFcmNegoScrmbBinary1_Type())
h3cPosaFcmNegoScrmbBinary1.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmNegoScrmbBinary1.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmNegoScrmbBinary1.setUnits(_L)
class _H3cPosaFcmNegoUnscrmbBinary1_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1500))
_H3cPosaFcmNegoUnscrmbBinary1_Type.__name__=_C
_H3cPosaFcmNegoUnscrmbBinary1_Object=MibTableColumn
h3cPosaFcmNegoUnscrmbBinary1=_H3cPosaFcmNegoUnscrmbBinary1_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1,4),_H3cPosaFcmNegoUnscrmbBinary1_Type())
h3cPosaFcmNegoUnscrmbBinary1.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmNegoUnscrmbBinary1.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmNegoUnscrmbBinary1.setUnits(_L)
class _H3cPosaFcmThresholdRlsdOff_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,75))
_H3cPosaFcmThresholdRlsdOff_Type.__name__=_C
_H3cPosaFcmThresholdRlsdOff_Object=MibTableColumn
h3cPosaFcmThresholdRlsdOff=_H3cPosaFcmThresholdRlsdOff_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1,5),_H3cPosaFcmThresholdRlsdOff_Type())
h3cPosaFcmThresholdRlsdOff.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmThresholdRlsdOff.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmThresholdRlsdOff.setUnits(_R)
class _H3cPosaFcmThresholdRlsdOn_Type(Integer32):defaultValue=43;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,75))
_H3cPosaFcmThresholdRlsdOn_Type.__name__=_C
_H3cPosaFcmThresholdRlsdOn_Object=MibTableColumn
h3cPosaFcmThresholdRlsdOn=_H3cPosaFcmThresholdRlsdOn_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1,6),_H3cPosaFcmThresholdRlsdOn_Type())
h3cPosaFcmThresholdRlsdOn.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmThresholdRlsdOn.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmThresholdRlsdOn.setUnits(_R)
class _H3cPosaFcmThresholdTxPower_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,42))
_H3cPosaFcmThresholdTxPower_Type.__name__=_C
_H3cPosaFcmThresholdTxPower_Object=MibTableColumn
h3cPosaFcmThresholdTxPower=_H3cPosaFcmThresholdTxPower_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1,7),_H3cPosaFcmThresholdTxPower_Type())
h3cPosaFcmThresholdTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmThresholdTxPower.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmThresholdTxPower.setUnits(_R)
class _H3cPosaFcmThresholdAnswerTone_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,42))
_H3cPosaFcmThresholdAnswerTone_Type.__name__=_C
_H3cPosaFcmThresholdAnswerTone_Object=MibTableColumn
h3cPosaFcmThresholdAnswerTone=_H3cPosaFcmThresholdAnswerTone_Object((1,3,6,1,4,1,2011,10,2,92,2,9,1,8),_H3cPosaFcmThresholdAnswerTone_Type())
h3cPosaFcmThresholdAnswerTone.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPosaFcmThresholdAnswerTone.setStatus(_A)
if mibBuilder.loadTexts:h3cPosaFcmThresholdAnswerTone.setUnits(_R)
_H3cPosaCallerStatTable_Object=MibTable
h3cPosaCallerStatTable=_H3cPosaCallerStatTable_Object((1,3,6,1,4,1,2011,10,2,92,2,10))
if mibBuilder.loadTexts:h3cPosaCallerStatTable.setStatus(_A)
_H3cPosaCallerStatEntry_Object=MibTableRow
h3cPosaCallerStatEntry=_H3cPosaCallerStatEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1))
h3cPosaCallerStatEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:h3cPosaCallerStatEntry.setStatus(_A)
class _H3cPosaCallerStatCallerID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cPosaCallerStatCallerID_Type.__name__=_J
_H3cPosaCallerStatCallerID_Object=MibTableColumn
h3cPosaCallerStatCallerID=_H3cPosaCallerStatCallerID_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1,1),_H3cPosaCallerStatCallerID_Type())
h3cPosaCallerStatCallerID.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cPosaCallerStatCallerID.setStatus(_A)
_H3cPosaCallerRecvPkts_Type=Counter64
_H3cPosaCallerRecvPkts_Object=MibTableColumn
h3cPosaCallerRecvPkts=_H3cPosaCallerRecvPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1,2),_H3cPosaCallerRecvPkts_Type())
h3cPosaCallerRecvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaCallerRecvPkts.setStatus(_A)
_H3cPosaCallerSendPkts_Type=Counter64
_H3cPosaCallerSendPkts_Object=MibTableColumn
h3cPosaCallerSendPkts=_H3cPosaCallerSendPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1,3),_H3cPosaCallerSendPkts_Type())
h3cPosaCallerSendPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaCallerSendPkts.setStatus(_A)
_H3cPosaCallerErrPkts_Type=Counter64
_H3cPosaCallerErrPkts_Object=MibTableColumn
h3cPosaCallerErrPkts=_H3cPosaCallerErrPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1,4),_H3cPosaCallerErrPkts_Type())
h3cPosaCallerErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaCallerErrPkts.setStatus(_A)
_H3cPosaCallerMapErrCnts_Type=Counter64
_H3cPosaCallerMapErrCnts_Object=MibTableColumn
h3cPosaCallerMapErrCnts=_H3cPosaCallerMapErrCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1,5),_H3cPosaCallerMapErrCnts_Type())
h3cPosaCallerMapErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaCallerMapErrCnts.setStatus(_A)
_H3cPosaCallerInDiscardedPkts_Type=Counter64
_H3cPosaCallerInDiscardedPkts_Object=MibTableColumn
h3cPosaCallerInDiscardedPkts=_H3cPosaCallerInDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1,6),_H3cPosaCallerInDiscardedPkts_Type())
h3cPosaCallerInDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaCallerInDiscardedPkts.setStatus(_A)
_H3cPosaCallerOutDiscardedPkts_Type=Counter64
_H3cPosaCallerOutDiscardedPkts_Object=MibTableColumn
h3cPosaCallerOutDiscardedPkts=_H3cPosaCallerOutDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1,7),_H3cPosaCallerOutDiscardedPkts_Type())
h3cPosaCallerOutDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaCallerOutDiscardedPkts.setStatus(_A)
_H3cPosaCallerStatRowStatus_Type=RowStatus
_H3cPosaCallerStatRowStatus_Object=MibTableColumn
h3cPosaCallerStatRowStatus=_H3cPosaCallerStatRowStatus_Object((1,3,6,1,4,1,2011,10,2,92,2,10,1,8),_H3cPosaCallerStatRowStatus_Type())
h3cPosaCallerStatRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPosaCallerStatRowStatus.setStatus(_A)
_H3cPosaNiiStatTable_Object=MibTable
h3cPosaNiiStatTable=_H3cPosaNiiStatTable_Object((1,3,6,1,4,1,2011,10,2,92,2,11))
if mibBuilder.loadTexts:h3cPosaNiiStatTable.setStatus(_A)
_H3cPosaNiiStatEntry_Object=MibTableRow
h3cPosaNiiStatEntry=_H3cPosaNiiStatEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,11,1))
h3cPosaNiiStatEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:h3cPosaNiiStatEntry.setStatus(_A)
class _H3cPosaNiiStatIndex_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_H3cPosaNiiStatIndex_Type.__name__=_J
_H3cPosaNiiStatIndex_Object=MibTableColumn
h3cPosaNiiStatIndex=_H3cPosaNiiStatIndex_Object((1,3,6,1,4,1,2011,10,2,92,2,11,1,1),_H3cPosaNiiStatIndex_Type())
h3cPosaNiiStatIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cPosaNiiStatIndex.setStatus(_A)
_H3cPosaNiiRecvPkts_Type=Counter32
_H3cPosaNiiRecvPkts_Object=MibTableColumn
h3cPosaNiiRecvPkts=_H3cPosaNiiRecvPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,11,1,2),_H3cPosaNiiRecvPkts_Type())
h3cPosaNiiRecvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaNiiRecvPkts.setStatus(_A)
_H3cPosaNiiSendPkts_Type=Counter32
_H3cPosaNiiSendPkts_Object=MibTableColumn
h3cPosaNiiSendPkts=_H3cPosaNiiSendPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,11,1,3),_H3cPosaNiiSendPkts_Type())
h3cPosaNiiSendPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaNiiSendPkts.setStatus(_A)
_H3cPosaNiiSuccessTradeCnt_Type=Counter32
_H3cPosaNiiSuccessTradeCnt_Object=MibTableColumn
h3cPosaNiiSuccessTradeCnt=_H3cPosaNiiSuccessTradeCnt_Object((1,3,6,1,4,1,2011,10,2,92,2,11,1,4),_H3cPosaNiiSuccessTradeCnt_Type())
h3cPosaNiiSuccessTradeCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaNiiSuccessTradeCnt.setStatus(_A)
_H3cPosaNiiTradeCnt_Type=Counter32
_H3cPosaNiiTradeCnt_Object=MibTableColumn
h3cPosaNiiTradeCnt=_H3cPosaNiiTradeCnt_Object((1,3,6,1,4,1,2011,10,2,92,2,11,1,5),_H3cPosaNiiTradeCnt_Type())
h3cPosaNiiTradeCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaNiiTradeCnt.setStatus(_A)
_H3cPosaE1StatTable_Object=MibTable
h3cPosaE1StatTable=_H3cPosaE1StatTable_Object((1,3,6,1,4,1,2011,10,2,92,2,12))
if mibBuilder.loadTexts:h3cPosaE1StatTable.setStatus(_A)
_H3cPosaE1StatEntry_Object=MibTableRow
h3cPosaE1StatEntry=_H3cPosaE1StatEntry_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1))
h3cPosaE1StatEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:h3cPosaE1StatEntry.setStatus(_A)
class _H3cPosaE1StatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPosaE1StatIndex_Type.__name__=_C
_H3cPosaE1StatIndex_Object=MibTableColumn
h3cPosaE1StatIndex=_H3cPosaE1StatIndex_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,1),_H3cPosaE1StatIndex_Type())
h3cPosaE1StatIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cPosaE1StatIndex.setStatus(_A)
_H3cPosaE1DialCnt_Type=Counter32
_H3cPosaE1DialCnt_Object=MibTableColumn
h3cPosaE1DialCnt=_H3cPosaE1DialCnt_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,2),_H3cPosaE1DialCnt_Type())
h3cPosaE1DialCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaE1DialCnt.setStatus(_A)
_H3cPosaE1DialSuccess_Type=Counter32
_H3cPosaE1DialSuccess_Object=MibTableColumn
h3cPosaE1DialSuccess=_H3cPosaE1DialSuccess_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,3),_H3cPosaE1DialSuccess_Type())
h3cPosaE1DialSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaE1DialSuccess.setStatus(_A)
_H3cPosaE1RecvPkts_Type=Counter32
_H3cPosaE1RecvPkts_Object=MibTableColumn
h3cPosaE1RecvPkts=_H3cPosaE1RecvPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,4),_H3cPosaE1RecvPkts_Type())
h3cPosaE1RecvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaE1RecvPkts.setStatus(_A)
_H3cPosaE1SendPkts_Type=Counter32
_H3cPosaE1SendPkts_Object=MibTableColumn
h3cPosaE1SendPkts=_H3cPosaE1SendPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,5),_H3cPosaE1SendPkts_Type())
h3cPosaE1SendPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaE1SendPkts.setStatus(_A)
_H3cPosaE1ErrPkts_Type=Counter32
_H3cPosaE1ErrPkts_Object=MibTableColumn
h3cPosaE1ErrPkts=_H3cPosaE1ErrPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,6),_H3cPosaE1ErrPkts_Type())
h3cPosaE1ErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaE1ErrPkts.setStatus(_A)
_H3cPosaE1MapErrCnts_Type=Counter32
_H3cPosaE1MapErrCnts_Object=MibTableColumn
h3cPosaE1MapErrCnts=_H3cPosaE1MapErrCnts_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,7),_H3cPosaE1MapErrCnts_Type())
h3cPosaE1MapErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaE1MapErrCnts.setStatus(_A)
_H3cPosaE1InDiscardedPkts_Type=Counter32
_H3cPosaE1InDiscardedPkts_Object=MibTableColumn
h3cPosaE1InDiscardedPkts=_H3cPosaE1InDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,8),_H3cPosaE1InDiscardedPkts_Type())
h3cPosaE1InDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaE1InDiscardedPkts.setStatus(_A)
_H3cPosaE1OutDiscardedPkts_Type=Counter32
_H3cPosaE1OutDiscardedPkts_Object=MibTableColumn
h3cPosaE1OutDiscardedPkts=_H3cPosaE1OutDiscardedPkts_Object((1,3,6,1,4,1,2011,10,2,92,2,12,1,9),_H3cPosaE1OutDiscardedPkts_Type())
h3cPosaE1OutDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPosaE1OutDiscardedPkts.setStatus(_A)
_H3cPosaTrap_ObjectIdentity=ObjectIdentity
h3cPosaTrap=_H3cPosaTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,92,3))
_H3cPosaTrapPrex_ObjectIdentity=ObjectIdentity
h3cPosaTrapPrex=_H3cPosaTrapPrex_ObjectIdentity((1,3,6,1,4,1,2011,10,2,92,3,0))
_H3cPosaTrapObjects_ObjectIdentity=ObjectIdentity
h3cPosaTrapObjects=_H3cPosaTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,92,3,1))
class _H3cPosaAppStateChangeObject_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('available',1),('unavailable',2)))
_H3cPosaAppStateChangeObject_Type.__name__=_C
_H3cPosaAppStateChangeObject_Object=MibScalar
h3cPosaAppStateChangeObject=_H3cPosaAppStateChangeObject_Object((1,3,6,1,4,1,2011,10,2,92,3,1,1),_H3cPosaAppStateChangeObject_Type())
h3cPosaAppStateChangeObject.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cPosaAppStateChangeObject.setStatus(_A)
h3cPosaServerStatusChange=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,1))
h3cPosaServerStatusChange.setObjects((_F,_d))
if mibBuilder.loadTexts:h3cPosaServerStatusChange.setStatus(_A)
h3cPosaAppStateChange=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,2))
h3cPosaAppStateChange.setObjects(*((_F,_P),(_F,_e)))
if mibBuilder.loadTexts:h3cPosaAppStateChange.setStatus(_A)
h3cPosaTerminalHangUp=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,3))
h3cPosaTerminalHangUp.setObjects(*((_H,_I),(_H,_K),(_F,_M)))
if mibBuilder.loadTexts:h3cPosaTerminalHangUp.setStatus(_A)
h3cPosaFcmLinkNegoFailed=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,4))
h3cPosaFcmLinkNegoFailed.setObjects(*((_H,_I),(_H,_K),(_F,_M)))
if mibBuilder.loadTexts:h3cPosaFcmLinkNegoFailed.setStatus(_A)
h3cPosaFcmPhyNegoFailed=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,5))
h3cPosaFcmPhyNegoFailed.setObjects(*((_H,_I),(_H,_K),(_F,_M)))
if mibBuilder.loadTexts:h3cPosaFcmPhyNegoFailed.setStatus(_A)
h3cPosaTcpConnectionExceed=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,6))
h3cPosaTcpConnectionExceed.setObjects((_F,_f))
if mibBuilder.loadTexts:h3cPosaTcpConnectionExceed.setStatus(_A)
h3cPosaFcmConnectionExceed=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,7))
h3cPosaFcmConnectionExceed.setObjects((_F,_g))
if mibBuilder.loadTexts:h3cPosaFcmConnectionExceed.setStatus(_A)
h3cPosaTcpTradeExceed=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,8))
h3cPosaTcpTradeExceed.setObjects(*((_F,_h),(_F,_Q)))
if mibBuilder.loadTexts:h3cPosaTcpTradeExceed.setStatus(_A)
h3cPosaTradeSuccessFalling=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,9))
h3cPosaTradeSuccessFalling.setObjects(*((_F,_T),(_F,_i)))
if mibBuilder.loadTexts:h3cPosaTradeSuccessFalling.setStatus(_A)
h3cPosaE1DialFalling=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,10))
h3cPosaE1DialFalling.setObjects(*((_H,_I),(_H,_K),(_F,_j)))
if mibBuilder.loadTexts:h3cPosaE1DialFalling.setStatus(_A)
h3cPosaFcmTradeAbnormal=NotificationType((1,3,6,1,4,1,2011,10,2,92,3,0,11))
h3cPosaFcmTradeAbnormal.setObjects(*((_H,_I),(_H,_K),(_F,_M)))
if mibBuilder.loadTexts:h3cPosaFcmTradeAbnormal.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_U:H3cAppServiceType,_V:H3cAppMode,'H3cPeerState':H3cPeerState,_X:H3cTerminalAccessType,_W:H3cTpduChangeStrategy,'h3cPosa':h3cPosa,'h3cPosaControl':h3cPosaControl,_d:h3cPosaServerEnable,'h3cPosaFcmAnswerTimeout':h3cPosaFcmAnswerTimeout,'h3cPosaFcmTradeTimeout':h3cPosaFcmTradeTimeout,'h3cPosaFcmIdleTimeout':h3cPosaFcmIdleTimeout,'h3cPosaSrvStateChangeTrapEnable':h3cPosaSrvStateChangeTrapEnable,'h3cPosaAppStateChangeTrapEnable':h3cPosaAppStateChangeTrapEnable,'h3cPosaTerminalHangUpTrapEnable':h3cPosaTerminalHangUpTrapEnable,'h3cPosaFcmLnkNegoFailTrapEnable':h3cPosaFcmLnkNegoFailTrapEnable,'h3cPosaFcmPhyNegoFailTrapEnable':h3cPosaFcmPhyNegoFailTrapEnable,'h3cPosaTcpConnectionNumber':h3cPosaTcpConnectionNumber,'h3cPosaFcmConnectionNumber':h3cPosaFcmConnectionNumber,_f:h3cPosaTcpConnectionThreshold,_g:h3cPosaFcmConnectionThreshold,'h3cPosaTcpConnectionTrapEnable':h3cPosaTcpConnectionTrapEnable,'h3cPosaFcmConnectionTrapEnable':h3cPosaFcmConnectionTrapEnable,_h:h3cPosaTcpTradeLimit,'h3cPosaTcpTradeTrapEnable':h3cPosaTcpTradeTrapEnable,'h3cPosaTcpTradeTimeout':h3cPosaTcpTradeTimeout,'h3cPosaTradeSuccessFallingTrapEnable':h3cPosaTradeSuccessFallingTrapEnable,_i:h3cPosaTradeSuccessFallingThreshold,'h3cPosaE1DialFallingTrapEnable':h3cPosaE1DialFallingTrapEnable,_j:h3cPosaE1DialFallingThreshold,'h3cPosaFcmTradeAbnormalTrapEnable':h3cPosaFcmTradeAbnormalTrapEnable,'h3cPosaTables':h3cPosaTables,'h3cPosaAppTable':h3cPosaAppTable,'h3cPosaAppEntry':h3cPosaAppEntry,_P:h3cPosaAppID,'h3cPosaAppServiceType':h3cPosaAppServiceType,'h3cPosaAppIfIndex':h3cPosaAppIfIndex,'h3cPosaAppMode':h3cPosaAppMode,'h3cPosaAppHostIPType':h3cPosaAppHostIPType,'h3cPosaAppHostIP':h3cPosaAppHostIP,'h3cPosaAppHostPort':h3cPosaAppHostPort,'h3cPosaAppRouterIPType':h3cPosaAppRouterIPType,'h3cPosaAppRouterIP':h3cPosaAppRouterIP,'h3cPosaAppKeepAliveInterval':h3cPosaAppKeepAliveInterval,'h3cPosaAppKeepAliveCount':h3cPosaAppKeepAliveCount,'h3cPosaAppConnectTimeout':h3cPosaAppConnectTimeout,'h3cPosaAppState':h3cPosaAppState,'h3cPosaAppRowStatus':h3cPosaAppRowStatus,'h3cPosaAppName':h3cPosaAppName,'h3cPosaCallerIDTransEnable':h3cPosaCallerIDTransEnable,'h3cPosaTpduChangeStrategy':h3cPosaTpduChangeStrategy,'h3cPosaBackupAppID':h3cPosaBackupAppID,'h3cPosaQuietTimeOut':h3cPosaQuietTimeOut,'h3cPosaAppHello':h3cPosaAppHello,'h3cPosaAppHelloInterval':h3cPosaAppHelloInterval,'h3cPosaAppRouterPort':h3cPosaAppRouterPort,'h3cPosaTerminalTable':h3cPosaTerminalTable,'h3cPosaTerminalEntry':h3cPosaTerminalEntry,_Q:h3cPosaTerminalID,'h3cPosaTerminalAccessType':h3cPosaTerminalAccessType,'h3cPosaTerminalIfIndex':h3cPosaTerminalIfIndex,'h3cPosaTerminalTransAppID':h3cPosaTerminalTransAppID,'h3cPosaTerminalListenPort':h3cPosaTerminalListenPort,'h3cPosaTerminalState':h3cPosaTerminalState,'h3cPosaTerminalRowStatus':h3cPosaTerminalRowStatus,'h3cPosaTerminalName':h3cPosaTerminalName,'h3cPosaTerminalCfgIfIndex':h3cPosaTerminalCfgIfIndex,'h3cPosaMapTable':h3cPosaMapTable,'h3cPosaMapEntry':h3cPosaMapEntry,_Z:h3cPosaMapDestCode,'h3cPosaMapAppID':h3cPosaMapAppID,'h3cPosaMapRowStatus':h3cPosaMapRowStatus,_Y:h3cPosaMapSrcCode,'h3cPosaFcmStatTable':h3cPosaFcmStatTable,'h3cPosaFcmStatEntry':h3cPosaFcmStatEntry,_a:h3cPosaFcmStatIfIndex,'h3cPosaFcmStatTimeoutCnts':h3cPosaFcmStatTimeoutCnts,'h3cPosaFcmStatConnectFailCnts':h3cPosaFcmStatConnectFailCnts,'h3cPosaFcmStatTransCnts':h3cPosaFcmStatTransCnts,'h3cPosaFcmStatTransSuccessCnts':h3cPosaFcmStatTransSuccessCnts,'h3cPosaFcmStatTransCntsClear':h3cPosaFcmStatTransCntsClear,'h3cPosaAppStatTable':h3cPosaAppStatTable,'h3cPosaAppStatEntry':h3cPosaAppStatEntry,'h3cPosaAppRecvPkts':h3cPosaAppRecvPkts,'h3cPosaAppSendPkts':h3cPosaAppSendPkts,'h3cPosaAppErrPkts':h3cPosaAppErrPkts,'h3cPosaAppDistributeErrCnts':h3cPosaAppDistributeErrCnts,'h3cPosaAppInDiscardedPkts':h3cPosaAppInDiscardedPkts,'h3cPosaAppOutDiscardedPkts':h3cPosaAppOutDiscardedPkts,'h3cPosaTerminalStatTable':h3cPosaTerminalStatTable,'h3cPosaTerminalStatEntry':h3cPosaTerminalStatEntry,'h3cPosaTerminalRecvPkts':h3cPosaTerminalRecvPkts,'h3cPosaTerminalSendPkts':h3cPosaTerminalSendPkts,'h3cPosaTerminalErrPkts':h3cPosaTerminalErrPkts,'h3cPosaTerminalMapErrCnts':h3cPosaTerminalMapErrCnts,'h3cPosaTerminalInDiscardedPkts':h3cPosaTerminalInDiscardedPkts,'h3cPosaTerminalOutDiscardedPkts':h3cPosaTerminalOutDiscardedPkts,'h3cPosaTermianlTcpConnectionNumber':h3cPosaTermianlTcpConnectionNumber,'h3cPosaBatchTerminalTable':h3cPosaBatchTerminalTable,'h3cPosaBatchTerminalEntry':h3cPosaBatchTerminalEntry,'h3cPosaBatchTerminalFirstID':h3cPosaBatchTerminalFirstID,'h3cPosaBatchTerminalRowStatus':h3cPosaBatchTerminalRowStatus,'h3cPosaTcpTermStatTable':h3cPosaTcpTermStatTable,'h3cPosaTcpTermStatEntry':h3cPosaTcpTermStatEntry,_b:h3cPosaTcpTermStatIndex,'h3cPosaTcpTermStatIPType':h3cPosaTcpTermStatIPType,'h3cPosaTcpTermStatIP':h3cPosaTcpTermStatIP,'h3cPosaTcpTermStatIPMask':h3cPosaTcpTermStatIPMask,'h3cPosaTcpTermRecvPkts':h3cPosaTcpTermRecvPkts,'h3cPosaTcpTermSendPkts':h3cPosaTcpTermSendPkts,'h3cPosaTcpTermErrPkts':h3cPosaTcpTermErrPkts,'h3cPosaTcpTermMapErrCnts':h3cPosaTcpTermMapErrCnts,'h3cPosaTcpTermInDiscardedPkts':h3cPosaTcpTermInDiscardedPkts,'h3cPosaTcpTermOutDiscardedPkts':h3cPosaTcpTermOutDiscardedPkts,'h3cPosaTcpTermStatRowStatus':h3cPosaTcpTermStatRowStatus,'h3cPosaFcmConfTable':h3cPosaFcmConfTable,'h3cPosaFcmConfEntry':h3cPosaFcmConfEntry,'h3cPosaFcmNegoHookOff':h3cPosaFcmNegoHookOff,'h3cPosaFcmNegoSilence':h3cPosaFcmNegoSilence,'h3cPosaFcmNegoScrmbBinary1':h3cPosaFcmNegoScrmbBinary1,'h3cPosaFcmNegoUnscrmbBinary1':h3cPosaFcmNegoUnscrmbBinary1,'h3cPosaFcmThresholdRlsdOff':h3cPosaFcmThresholdRlsdOff,'h3cPosaFcmThresholdRlsdOn':h3cPosaFcmThresholdRlsdOn,'h3cPosaFcmThresholdTxPower':h3cPosaFcmThresholdTxPower,'h3cPosaFcmThresholdAnswerTone':h3cPosaFcmThresholdAnswerTone,'h3cPosaCallerStatTable':h3cPosaCallerStatTable,'h3cPosaCallerStatEntry':h3cPosaCallerStatEntry,_M:h3cPosaCallerStatCallerID,'h3cPosaCallerRecvPkts':h3cPosaCallerRecvPkts,'h3cPosaCallerSendPkts':h3cPosaCallerSendPkts,'h3cPosaCallerErrPkts':h3cPosaCallerErrPkts,'h3cPosaCallerMapErrCnts':h3cPosaCallerMapErrCnts,'h3cPosaCallerInDiscardedPkts':h3cPosaCallerInDiscardedPkts,'h3cPosaCallerOutDiscardedPkts':h3cPosaCallerOutDiscardedPkts,'h3cPosaCallerStatRowStatus':h3cPosaCallerStatRowStatus,'h3cPosaNiiStatTable':h3cPosaNiiStatTable,'h3cPosaNiiStatEntry':h3cPosaNiiStatEntry,_T:h3cPosaNiiStatIndex,'h3cPosaNiiRecvPkts':h3cPosaNiiRecvPkts,'h3cPosaNiiSendPkts':h3cPosaNiiSendPkts,'h3cPosaNiiSuccessTradeCnt':h3cPosaNiiSuccessTradeCnt,'h3cPosaNiiTradeCnt':h3cPosaNiiTradeCnt,'h3cPosaE1StatTable':h3cPosaE1StatTable,'h3cPosaE1StatEntry':h3cPosaE1StatEntry,_c:h3cPosaE1StatIndex,'h3cPosaE1DialCnt':h3cPosaE1DialCnt,'h3cPosaE1DialSuccess':h3cPosaE1DialSuccess,'h3cPosaE1RecvPkts':h3cPosaE1RecvPkts,'h3cPosaE1SendPkts':h3cPosaE1SendPkts,'h3cPosaE1ErrPkts':h3cPosaE1ErrPkts,'h3cPosaE1MapErrCnts':h3cPosaE1MapErrCnts,'h3cPosaE1InDiscardedPkts':h3cPosaE1InDiscardedPkts,'h3cPosaE1OutDiscardedPkts':h3cPosaE1OutDiscardedPkts,'h3cPosaTrap':h3cPosaTrap,'h3cPosaTrapPrex':h3cPosaTrapPrex,'h3cPosaServerStatusChange':h3cPosaServerStatusChange,'h3cPosaAppStateChange':h3cPosaAppStateChange,'h3cPosaTerminalHangUp':h3cPosaTerminalHangUp,'h3cPosaFcmLinkNegoFailed':h3cPosaFcmLinkNegoFailed,'h3cPosaFcmPhyNegoFailed':h3cPosaFcmPhyNegoFailed,'h3cPosaTcpConnectionExceed':h3cPosaTcpConnectionExceed,'h3cPosaFcmConnectionExceed':h3cPosaFcmConnectionExceed,'h3cPosaTcpTradeExceed':h3cPosaTcpTradeExceed,'h3cPosaTradeSuccessFalling':h3cPosaTradeSuccessFalling,'h3cPosaE1DialFalling':h3cPosaE1DialFalling,'h3cPosaFcmTradeAbnormal':h3cPosaFcmTradeAbnormal,'h3cPosaTrapObjects':h3cPosaTrapObjects,_e:h3cPosaAppStateChangeObject})