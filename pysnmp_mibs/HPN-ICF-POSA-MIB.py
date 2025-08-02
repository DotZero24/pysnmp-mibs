_f='hpnicfPosaTcpTradeLimit'
_e='hpnicfPosaFcmConnectionThreshold'
_d='hpnicfPosaTcpConnectionThreshold'
_c='hpnicfPosaAppStateChangeObject'
_b='hpnicfPosaServerEnable'
_a='hpnicfPosaCallerStatCallerID'
_Z='hpnicfPosaTcpTermStatIndex'
_Y='hpnicfPosaFcmStatIfIndex'
_X='hpnicfPosaMapDestCode'
_W='hpnicfPosaMapSrcCode'
_V='HpnicfTerminalAccessType'
_U='HpnicfTpduChangeStrategy'
_T='HpnicfAppMode'
_S='HpnicfAppServiceType'
_R='accessible-for-notify'
_Q='seconds'
_P='-dBm'
_O='hpnicfPosaTerminalID'
_N='hpnicfPosaAppID'
_M='ifDescr'
_L='not-accessible'
_K='milliseconds'
_J='ifIndex'
_I='OctetString'
_H='IF-MIB'
_G='TruthValue'
_F='HPN-ICF-POSA-MIB'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_H,_M,_J)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
hpnicfPosa=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,92))
if mibBuilder.loadTexts:hpnicfPosa.setRevisions(('2014-05-29 00:00','2008-03-12 09:33'))
class HpnicfAppServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('flow',2)))
class HpnicfAppMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('temporary',2)))
class HpnicfPeerState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('notset',1),('down',2),('up',3),('kept',4),('linking',5),('linked',6),('multilink',7),('blocked',8),('error',9)))
class HpnicfTerminalAccessType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fcm',1),('flow',2),('tcp',3)))
class HpnicfTpduChangeStrategy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('changeTpduSrc',1),('changeTpduDest',2)))
_HpnicfPosaControl_ObjectIdentity=ObjectIdentity
hpnicfPosaControl=_HpnicfPosaControl_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,92,1))
class _HpnicfPosaServerEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_HpnicfPosaServerEnable_Type.__name__=_C
_HpnicfPosaServerEnable_Object=MibScalar
hpnicfPosaServerEnable=_HpnicfPosaServerEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,1),_HpnicfPosaServerEnable_Type())
hpnicfPosaServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaServerEnable.setStatus(_A)
class _HpnicfPosaFcmAnswerTimeout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2000))
_HpnicfPosaFcmAnswerTimeout_Type.__name__=_C
_HpnicfPosaFcmAnswerTimeout_Object=MibScalar
hpnicfPosaFcmAnswerTimeout=_HpnicfPosaFcmAnswerTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,2),_HpnicfPosaFcmAnswerTimeout_Type())
hpnicfPosaFcmAnswerTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmAnswerTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmAnswerTimeout.setUnits(_K)
class _HpnicfPosaFcmTradeTimeout_Type(Integer32):defaultValue=12000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30000,12000000))
_HpnicfPosaFcmTradeTimeout_Type.__name__=_C
_HpnicfPosaFcmTradeTimeout_Object=MibScalar
hpnicfPosaFcmTradeTimeout=_HpnicfPosaFcmTradeTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,3),_HpnicfPosaFcmTradeTimeout_Type())
hpnicfPosaFcmTradeTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmTradeTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmTradeTimeout.setUnits(_K)
class _HpnicfPosaFcmIdleTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12000))
_HpnicfPosaFcmIdleTimeout_Type.__name__=_C
_HpnicfPosaFcmIdleTimeout_Object=MibScalar
hpnicfPosaFcmIdleTimeout=_HpnicfPosaFcmIdleTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,4),_HpnicfPosaFcmIdleTimeout_Type())
hpnicfPosaFcmIdleTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmIdleTimeout.setUnits(_Q)
class _HpnicfPosaSrvStateChangeTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfPosaSrvStateChangeTrapEnable_Type.__name__=_G
_HpnicfPosaSrvStateChangeTrapEnable_Object=MibScalar
hpnicfPosaSrvStateChangeTrapEnable=_HpnicfPosaSrvStateChangeTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,5),_HpnicfPosaSrvStateChangeTrapEnable_Type())
hpnicfPosaSrvStateChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaSrvStateChangeTrapEnable.setStatus(_A)
class _HpnicfPosaAppStateChangeTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfPosaAppStateChangeTrapEnable_Type.__name__=_G
_HpnicfPosaAppStateChangeTrapEnable_Object=MibScalar
hpnicfPosaAppStateChangeTrapEnable=_HpnicfPosaAppStateChangeTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,6),_HpnicfPosaAppStateChangeTrapEnable_Type())
hpnicfPosaAppStateChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaAppStateChangeTrapEnable.setStatus(_A)
class _HpnicfPosaTerminalHangUpTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfPosaTerminalHangUpTrapEnable_Type.__name__=_G
_HpnicfPosaTerminalHangUpTrapEnable_Object=MibScalar
hpnicfPosaTerminalHangUpTrapEnable=_HpnicfPosaTerminalHangUpTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,7),_HpnicfPosaTerminalHangUpTrapEnable_Type())
hpnicfPosaTerminalHangUpTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaTerminalHangUpTrapEnable.setStatus(_A)
class _HpnicfPosaFcmLnkNegoFailTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfPosaFcmLnkNegoFailTrapEnable_Type.__name__=_G
_HpnicfPosaFcmLnkNegoFailTrapEnable_Object=MibScalar
hpnicfPosaFcmLnkNegoFailTrapEnable=_HpnicfPosaFcmLnkNegoFailTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,8),_HpnicfPosaFcmLnkNegoFailTrapEnable_Type())
hpnicfPosaFcmLnkNegoFailTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmLnkNegoFailTrapEnable.setStatus(_A)
class _HpnicfPosaFcmPhyNegoFailTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfPosaFcmPhyNegoFailTrapEnable_Type.__name__=_G
_HpnicfPosaFcmPhyNegoFailTrapEnable_Object=MibScalar
hpnicfPosaFcmPhyNegoFailTrapEnable=_HpnicfPosaFcmPhyNegoFailTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,9),_HpnicfPosaFcmPhyNegoFailTrapEnable_Type())
hpnicfPosaFcmPhyNegoFailTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmPhyNegoFailTrapEnable.setStatus(_A)
_HpnicfPosaTcpConnectionNumber_Type=Integer32
_HpnicfPosaTcpConnectionNumber_Object=MibScalar
hpnicfPosaTcpConnectionNumber=_HpnicfPosaTcpConnectionNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,10),_HpnicfPosaTcpConnectionNumber_Type())
hpnicfPosaTcpConnectionNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTcpConnectionNumber.setStatus(_A)
_HpnicfPosaFcmConnectionNumber_Type=Integer32
_HpnicfPosaFcmConnectionNumber_Object=MibScalar
hpnicfPosaFcmConnectionNumber=_HpnicfPosaFcmConnectionNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,11),_HpnicfPosaFcmConnectionNumber_Type())
hpnicfPosaFcmConnectionNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaFcmConnectionNumber.setStatus(_A)
class _HpnicfPosaTcpConnectionThreshold_Type(Integer32):defaultValue=4096
_HpnicfPosaTcpConnectionThreshold_Type.__name__=_C
_HpnicfPosaTcpConnectionThreshold_Object=MibScalar
hpnicfPosaTcpConnectionThreshold=_HpnicfPosaTcpConnectionThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,12),_HpnicfPosaTcpConnectionThreshold_Type())
hpnicfPosaTcpConnectionThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaTcpConnectionThreshold.setStatus(_A)
class _HpnicfPosaFcmConnectionThreshold_Type(Integer32):defaultValue=255
_HpnicfPosaFcmConnectionThreshold_Type.__name__=_C
_HpnicfPosaFcmConnectionThreshold_Object=MibScalar
hpnicfPosaFcmConnectionThreshold=_HpnicfPosaFcmConnectionThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,13),_HpnicfPosaFcmConnectionThreshold_Type())
hpnicfPosaFcmConnectionThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmConnectionThreshold.setStatus(_A)
class _HpnicfPosaTcpConnectionTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfPosaTcpConnectionTrapEnable_Type.__name__=_G
_HpnicfPosaTcpConnectionTrapEnable_Object=MibScalar
hpnicfPosaTcpConnectionTrapEnable=_HpnicfPosaTcpConnectionTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,14),_HpnicfPosaTcpConnectionTrapEnable_Type())
hpnicfPosaTcpConnectionTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaTcpConnectionTrapEnable.setStatus(_A)
class _HpnicfPosaFcmConnectionTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfPosaFcmConnectionTrapEnable_Type.__name__=_G
_HpnicfPosaFcmConnectionTrapEnable_Object=MibScalar
hpnicfPosaFcmConnectionTrapEnable=_HpnicfPosaFcmConnectionTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,15),_HpnicfPosaFcmConnectionTrapEnable_Type())
hpnicfPosaFcmConnectionTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmConnectionTrapEnable.setStatus(_A)
class _HpnicfPosaTcpTradeLimit_Type(Integer32):defaultValue=0
_HpnicfPosaTcpTradeLimit_Type.__name__=_C
_HpnicfPosaTcpTradeLimit_Object=MibScalar
hpnicfPosaTcpTradeLimit=_HpnicfPosaTcpTradeLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,16),_HpnicfPosaTcpTradeLimit_Type())
hpnicfPosaTcpTradeLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaTcpTradeLimit.setStatus(_A)
class _HpnicfPosaTcpTradeTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfPosaTcpTradeTrapEnable_Type.__name__=_G
_HpnicfPosaTcpTradeTrapEnable_Object=MibScalar
hpnicfPosaTcpTradeTrapEnable=_HpnicfPosaTcpTradeTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,17),_HpnicfPosaTcpTradeTrapEnable_Type())
hpnicfPosaTcpTradeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaTcpTradeTrapEnable.setStatus(_A)
class _HpnicfPosaTcpTradeTimeout_Type(Integer32):defaultValue=240
_HpnicfPosaTcpTradeTimeout_Type.__name__=_C
_HpnicfPosaTcpTradeTimeout_Object=MibScalar
hpnicfPosaTcpTradeTimeout=_HpnicfPosaTcpTradeTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,1,18),_HpnicfPosaTcpTradeTimeout_Type())
hpnicfPosaTcpTradeTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaTcpTradeTimeout.setStatus(_A)
_HpnicfPosaTables_ObjectIdentity=ObjectIdentity
hpnicfPosaTables=_HpnicfPosaTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,92,2))
_HpnicfPosaAppTable_Object=MibTable
hpnicfPosaAppTable=_HpnicfPosaAppTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1))
if mibBuilder.loadTexts:hpnicfPosaAppTable.setStatus(_A)
_HpnicfPosaAppEntry_Object=MibTableRow
hpnicfPosaAppEntry=_HpnicfPosaAppEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1))
hpnicfPosaAppEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:hpnicfPosaAppEntry.setStatus(_A)
class _HpnicfPosaAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfPosaAppID_Type.__name__=_C
_HpnicfPosaAppID_Object=MibTableColumn
hpnicfPosaAppID=_HpnicfPosaAppID_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,1),_HpnicfPosaAppID_Type())
hpnicfPosaAppID.setMaxAccess(_R)
if mibBuilder.loadTexts:hpnicfPosaAppID.setStatus(_A)
class _HpnicfPosaAppServiceType_Type(HpnicfAppServiceType):defaultValue=1
_HpnicfPosaAppServiceType_Type.__name__=_S
_HpnicfPosaAppServiceType_Object=MibTableColumn
hpnicfPosaAppServiceType=_HpnicfPosaAppServiceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,2),_HpnicfPosaAppServiceType_Type())
hpnicfPosaAppServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppServiceType.setStatus(_A)
_HpnicfPosaAppIfIndex_Type=Integer32
_HpnicfPosaAppIfIndex_Object=MibTableColumn
hpnicfPosaAppIfIndex=_HpnicfPosaAppIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,3),_HpnicfPosaAppIfIndex_Type())
hpnicfPosaAppIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppIfIndex.setStatus(_A)
class _HpnicfPosaAppMode_Type(HpnicfAppMode):defaultValue=1
_HpnicfPosaAppMode_Type.__name__=_T
_HpnicfPosaAppMode_Object=MibTableColumn
hpnicfPosaAppMode=_HpnicfPosaAppMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,4),_HpnicfPosaAppMode_Type())
hpnicfPosaAppMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppMode.setStatus(_A)
_HpnicfPosaAppHostIPType_Type=InetAddressType
_HpnicfPosaAppHostIPType_Object=MibTableColumn
hpnicfPosaAppHostIPType=_HpnicfPosaAppHostIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,5),_HpnicfPosaAppHostIPType_Type())
hpnicfPosaAppHostIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppHostIPType.setStatus(_A)
_HpnicfPosaAppHostIP_Type=InetAddress
_HpnicfPosaAppHostIP_Object=MibTableColumn
hpnicfPosaAppHostIP=_HpnicfPosaAppHostIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,6),_HpnicfPosaAppHostIP_Type())
hpnicfPosaAppHostIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppHostIP.setStatus(_A)
class _HpnicfPosaAppHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfPosaAppHostPort_Type.__name__=_C
_HpnicfPosaAppHostPort_Object=MibTableColumn
hpnicfPosaAppHostPort=_HpnicfPosaAppHostPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,7),_HpnicfPosaAppHostPort_Type())
hpnicfPosaAppHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppHostPort.setStatus(_A)
_HpnicfPosaAppRouterIPType_Type=InetAddressType
_HpnicfPosaAppRouterIPType_Object=MibTableColumn
hpnicfPosaAppRouterIPType=_HpnicfPosaAppRouterIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,8),_HpnicfPosaAppRouterIPType_Type())
hpnicfPosaAppRouterIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppRouterIPType.setStatus(_A)
_HpnicfPosaAppRouterIP_Type=InetAddress
_HpnicfPosaAppRouterIP_Object=MibTableColumn
hpnicfPosaAppRouterIP=_HpnicfPosaAppRouterIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,9),_HpnicfPosaAppRouterIP_Type())
hpnicfPosaAppRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppRouterIP.setStatus(_A)
class _HpnicfPosaAppKeepAliveInterval_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7200))
_HpnicfPosaAppKeepAliveInterval_Type.__name__=_C
_HpnicfPosaAppKeepAliveInterval_Object=MibTableColumn
hpnicfPosaAppKeepAliveInterval=_HpnicfPosaAppKeepAliveInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,10),_HpnicfPosaAppKeepAliveInterval_Type())
hpnicfPosaAppKeepAliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaAppKeepAliveInterval.setUnits(_Q)
class _HpnicfPosaAppKeepAliveCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100))
_HpnicfPosaAppKeepAliveCount_Type.__name__=_C
_HpnicfPosaAppKeepAliveCount_Object=MibTableColumn
hpnicfPosaAppKeepAliveCount=_HpnicfPosaAppKeepAliveCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,11),_HpnicfPosaAppKeepAliveCount_Type())
hpnicfPosaAppKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppKeepAliveCount.setStatus(_A)
class _HpnicfPosaAppConnectTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HpnicfPosaAppConnectTimeout_Type.__name__=_C
_HpnicfPosaAppConnectTimeout_Object=MibTableColumn
hpnicfPosaAppConnectTimeout=_HpnicfPosaAppConnectTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,12),_HpnicfPosaAppConnectTimeout_Type())
hpnicfPosaAppConnectTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppConnectTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaAppConnectTimeout.setUnits(_Q)
_HpnicfPosaAppState_Type=HpnicfPeerState
_HpnicfPosaAppState_Object=MibTableColumn
hpnicfPosaAppState=_HpnicfPosaAppState_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,13),_HpnicfPosaAppState_Type())
hpnicfPosaAppState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaAppState.setStatus(_A)
_HpnicfPosaAppRowStatus_Type=RowStatus
_HpnicfPosaAppRowStatus_Object=MibTableColumn
hpnicfPosaAppRowStatus=_HpnicfPosaAppRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,14),_HpnicfPosaAppRowStatus_Type())
hpnicfPosaAppRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppRowStatus.setStatus(_A)
class _HpnicfPosaAppName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfPosaAppName_Type.__name__=_I
_HpnicfPosaAppName_Object=MibTableColumn
hpnicfPosaAppName=_HpnicfPosaAppName_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,15),_HpnicfPosaAppName_Type())
hpnicfPosaAppName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppName.setStatus(_A)
class _HpnicfPosaCallerIDTransEnable_Type(TruthValue):defaultValue=2
_HpnicfPosaCallerIDTransEnable_Type.__name__=_G
_HpnicfPosaCallerIDTransEnable_Object=MibTableColumn
hpnicfPosaCallerIDTransEnable=_HpnicfPosaCallerIDTransEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,16),_HpnicfPosaCallerIDTransEnable_Type())
hpnicfPosaCallerIDTransEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaCallerIDTransEnable.setStatus(_A)
class _HpnicfPosaTpduChangeStrategy_Type(HpnicfTpduChangeStrategy):defaultValue=1
_HpnicfPosaTpduChangeStrategy_Type.__name__=_U
_HpnicfPosaTpduChangeStrategy_Object=MibTableColumn
hpnicfPosaTpduChangeStrategy=_HpnicfPosaTpduChangeStrategy_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,17),_HpnicfPosaTpduChangeStrategy_Type())
hpnicfPosaTpduChangeStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTpduChangeStrategy.setStatus(_A)
class _HpnicfPosaBackupAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_HpnicfPosaBackupAppID_Type.__name__=_C
_HpnicfPosaBackupAppID_Object=MibTableColumn
hpnicfPosaBackupAppID=_HpnicfPosaBackupAppID_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,18),_HpnicfPosaBackupAppID_Type())
hpnicfPosaBackupAppID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaBackupAppID.setStatus(_A)
class _HpnicfPosaQuietTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_HpnicfPosaQuietTimeOut_Type.__name__=_C
_HpnicfPosaQuietTimeOut_Object=MibTableColumn
hpnicfPosaQuietTimeOut=_HpnicfPosaQuietTimeOut_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,19),_HpnicfPosaQuietTimeOut_Type())
hpnicfPosaQuietTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaQuietTimeOut.setStatus(_A)
class _HpnicfPosaAppHello_Type(TruthValue):defaultValue=2
_HpnicfPosaAppHello_Type.__name__=_G
_HpnicfPosaAppHello_Object=MibTableColumn
hpnicfPosaAppHello=_HpnicfPosaAppHello_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,20),_HpnicfPosaAppHello_Type())
hpnicfPosaAppHello.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppHello.setStatus(_A)
class _HpnicfPosaAppHelloInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_HpnicfPosaAppHelloInterval_Type.__name__=_C
_HpnicfPosaAppHelloInterval_Object=MibTableColumn
hpnicfPosaAppHelloInterval=_HpnicfPosaAppHelloInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,21),_HpnicfPosaAppHelloInterval_Type())
hpnicfPosaAppHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppHelloInterval.setStatus(_A)
class _HpnicfPosaAppRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4999))
_HpnicfPosaAppRouterPort_Type.__name__=_C
_HpnicfPosaAppRouterPort_Object=MibTableColumn
hpnicfPosaAppRouterPort=_HpnicfPosaAppRouterPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,1,1,22),_HpnicfPosaAppRouterPort_Type())
hpnicfPosaAppRouterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaAppRouterPort.setStatus(_A)
_HpnicfPosaTerminalTable_Object=MibTable
hpnicfPosaTerminalTable=_HpnicfPosaTerminalTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2))
if mibBuilder.loadTexts:hpnicfPosaTerminalTable.setStatus(_A)
_HpnicfPosaTerminalEntry_Object=MibTableRow
hpnicfPosaTerminalEntry=_HpnicfPosaTerminalEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1))
hpnicfPosaTerminalEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:hpnicfPosaTerminalEntry.setStatus(_A)
class _HpnicfPosaTerminalID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfPosaTerminalID_Type.__name__=_C
_HpnicfPosaTerminalID_Object=MibTableColumn
hpnicfPosaTerminalID=_HpnicfPosaTerminalID_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,1),_HpnicfPosaTerminalID_Type())
hpnicfPosaTerminalID.setMaxAccess(_R)
if mibBuilder.loadTexts:hpnicfPosaTerminalID.setStatus(_A)
class _HpnicfPosaTerminalAccessType_Type(HpnicfTerminalAccessType):defaultValue=1
_HpnicfPosaTerminalAccessType_Type.__name__=_V
_HpnicfPosaTerminalAccessType_Object=MibTableColumn
hpnicfPosaTerminalAccessType=_HpnicfPosaTerminalAccessType_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,2),_HpnicfPosaTerminalAccessType_Type())
hpnicfPosaTerminalAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTerminalAccessType.setStatus(_A)
_HpnicfPosaTerminalIfIndex_Type=Integer32
_HpnicfPosaTerminalIfIndex_Object=MibTableColumn
hpnicfPosaTerminalIfIndex=_HpnicfPosaTerminalIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,3),_HpnicfPosaTerminalIfIndex_Type())
hpnicfPosaTerminalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTerminalIfIndex.setStatus(_A)
class _HpnicfPosaTerminalTransAppID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_HpnicfPosaTerminalTransAppID_Type.__name__=_C
_HpnicfPosaTerminalTransAppID_Object=MibTableColumn
hpnicfPosaTerminalTransAppID=_HpnicfPosaTerminalTransAppID_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,4),_HpnicfPosaTerminalTransAppID_Type())
hpnicfPosaTerminalTransAppID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTerminalTransAppID.setStatus(_A)
class _HpnicfPosaTerminalListenPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfPosaTerminalListenPort_Type.__name__=_C
_HpnicfPosaTerminalListenPort_Object=MibTableColumn
hpnicfPosaTerminalListenPort=_HpnicfPosaTerminalListenPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,5),_HpnicfPosaTerminalListenPort_Type())
hpnicfPosaTerminalListenPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTerminalListenPort.setStatus(_A)
_HpnicfPosaTerminalState_Type=HpnicfPeerState
_HpnicfPosaTerminalState_Object=MibTableColumn
hpnicfPosaTerminalState=_HpnicfPosaTerminalState_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,6),_HpnicfPosaTerminalState_Type())
hpnicfPosaTerminalState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTerminalState.setStatus(_A)
_HpnicfPosaTerminalRowStatus_Type=RowStatus
_HpnicfPosaTerminalRowStatus_Object=MibTableColumn
hpnicfPosaTerminalRowStatus=_HpnicfPosaTerminalRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,7),_HpnicfPosaTerminalRowStatus_Type())
hpnicfPosaTerminalRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTerminalRowStatus.setStatus(_A)
class _HpnicfPosaTerminalName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfPosaTerminalName_Type.__name__=_I
_HpnicfPosaTerminalName_Object=MibTableColumn
hpnicfPosaTerminalName=_HpnicfPosaTerminalName_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,8),_HpnicfPosaTerminalName_Type())
hpnicfPosaTerminalName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTerminalName.setStatus(_A)
_HpnicfPosaTerminalCfgIfIndex_Type=Integer32
_HpnicfPosaTerminalCfgIfIndex_Object=MibTableColumn
hpnicfPosaTerminalCfgIfIndex=_HpnicfPosaTerminalCfgIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,2,1,9),_HpnicfPosaTerminalCfgIfIndex_Type())
hpnicfPosaTerminalCfgIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTerminalCfgIfIndex.setStatus(_A)
_HpnicfPosaMapTable_Object=MibTable
hpnicfPosaMapTable=_HpnicfPosaMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,3))
if mibBuilder.loadTexts:hpnicfPosaMapTable.setStatus(_A)
_HpnicfPosaMapEntry_Object=MibTableRow
hpnicfPosaMapEntry=_HpnicfPosaMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,3,1))
hpnicfPosaMapEntry.setIndexNames((0,_F,_W),(0,_F,_X))
if mibBuilder.loadTexts:hpnicfPosaMapEntry.setStatus(_A)
class _HpnicfPosaMapDestCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,7))
_HpnicfPosaMapDestCode_Type.__name__=_I
_HpnicfPosaMapDestCode_Object=MibTableColumn
hpnicfPosaMapDestCode=_HpnicfPosaMapDestCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,3,1,1),_HpnicfPosaMapDestCode_Type())
hpnicfPosaMapDestCode.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfPosaMapDestCode.setStatus(_A)
class _HpnicfPosaMapAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfPosaMapAppID_Type.__name__=_C
_HpnicfPosaMapAppID_Object=MibTableColumn
hpnicfPosaMapAppID=_HpnicfPosaMapAppID_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,3,1,2),_HpnicfPosaMapAppID_Type())
hpnicfPosaMapAppID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaMapAppID.setStatus(_A)
_HpnicfPosaMapRowStatus_Type=RowStatus
_HpnicfPosaMapRowStatus_Object=MibTableColumn
hpnicfPosaMapRowStatus=_HpnicfPosaMapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,3,1,3),_HpnicfPosaMapRowStatus_Type())
hpnicfPosaMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaMapRowStatus.setStatus(_A)
class _HpnicfPosaMapSrcCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,7))
_HpnicfPosaMapSrcCode_Type.__name__=_I
_HpnicfPosaMapSrcCode_Object=MibTableColumn
hpnicfPosaMapSrcCode=_HpnicfPosaMapSrcCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,3,1,4),_HpnicfPosaMapSrcCode_Type())
hpnicfPosaMapSrcCode.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfPosaMapSrcCode.setStatus(_A)
_HpnicfPosaFcmStatTable_Object=MibTable
hpnicfPosaFcmStatTable=_HpnicfPosaFcmStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,4))
if mibBuilder.loadTexts:hpnicfPosaFcmStatTable.setStatus(_A)
_HpnicfPosaFcmStatEntry_Object=MibTableRow
hpnicfPosaFcmStatEntry=_HpnicfPosaFcmStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,4,1))
hpnicfPosaFcmStatEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:hpnicfPosaFcmStatEntry.setStatus(_A)
class _HpnicfPosaFcmStatIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfPosaFcmStatIfIndex_Type.__name__=_C
_HpnicfPosaFcmStatIfIndex_Object=MibTableColumn
hpnicfPosaFcmStatIfIndex=_HpnicfPosaFcmStatIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,4,1,1),_HpnicfPosaFcmStatIfIndex_Type())
hpnicfPosaFcmStatIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfPosaFcmStatIfIndex.setStatus(_A)
_HpnicfPosaFcmStatTimeoutCnts_Type=Counter32
_HpnicfPosaFcmStatTimeoutCnts_Object=MibTableColumn
hpnicfPosaFcmStatTimeoutCnts=_HpnicfPosaFcmStatTimeoutCnts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,4,1,2),_HpnicfPosaFcmStatTimeoutCnts_Type())
hpnicfPosaFcmStatTimeoutCnts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaFcmStatTimeoutCnts.setStatus(_A)
_HpnicfPosaFcmStatConnectFailCnts_Type=Counter32
_HpnicfPosaFcmStatConnectFailCnts_Object=MibTableColumn
hpnicfPosaFcmStatConnectFailCnts=_HpnicfPosaFcmStatConnectFailCnts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,4,1,3),_HpnicfPosaFcmStatConnectFailCnts_Type())
hpnicfPosaFcmStatConnectFailCnts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaFcmStatConnectFailCnts.setStatus(_A)
_HpnicfPosaFcmStatTransCnts_Type=Gauge32
_HpnicfPosaFcmStatTransCnts_Object=MibTableColumn
hpnicfPosaFcmStatTransCnts=_HpnicfPosaFcmStatTransCnts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,4,1,4),_HpnicfPosaFcmStatTransCnts_Type())
hpnicfPosaFcmStatTransCnts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaFcmStatTransCnts.setStatus(_A)
_HpnicfPosaFcmStatTransSuccessCnts_Type=Gauge32
_HpnicfPosaFcmStatTransSuccessCnts_Object=MibTableColumn
hpnicfPosaFcmStatTransSuccessCnts=_HpnicfPosaFcmStatTransSuccessCnts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,4,1,5),_HpnicfPosaFcmStatTransSuccessCnts_Type())
hpnicfPosaFcmStatTransSuccessCnts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaFcmStatTransSuccessCnts.setStatus(_A)
class _HpnicfPosaFcmStatTransCntsClear_Type(TruthValue):defaultValue=2
_HpnicfPosaFcmStatTransCntsClear_Type.__name__=_G
_HpnicfPosaFcmStatTransCntsClear_Object=MibTableColumn
hpnicfPosaFcmStatTransCntsClear=_HpnicfPosaFcmStatTransCntsClear_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,4,1,6),_HpnicfPosaFcmStatTransCntsClear_Type())
hpnicfPosaFcmStatTransCntsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmStatTransCntsClear.setStatus(_A)
_HpnicfPosaAppStatTable_Object=MibTable
hpnicfPosaAppStatTable=_HpnicfPosaAppStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,5))
if mibBuilder.loadTexts:hpnicfPosaAppStatTable.setStatus(_A)
_HpnicfPosaAppStatEntry_Object=MibTableRow
hpnicfPosaAppStatEntry=_HpnicfPosaAppStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,5,1))
hpnicfPosaAppStatEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:hpnicfPosaAppStatEntry.setStatus(_A)
_HpnicfPosaAppRecvPkts_Type=Counter32
_HpnicfPosaAppRecvPkts_Object=MibTableColumn
hpnicfPosaAppRecvPkts=_HpnicfPosaAppRecvPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,5,1,1),_HpnicfPosaAppRecvPkts_Type())
hpnicfPosaAppRecvPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaAppRecvPkts.setStatus(_A)
_HpnicfPosaAppSendPkts_Type=Counter32
_HpnicfPosaAppSendPkts_Object=MibTableColumn
hpnicfPosaAppSendPkts=_HpnicfPosaAppSendPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,5,1,2),_HpnicfPosaAppSendPkts_Type())
hpnicfPosaAppSendPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaAppSendPkts.setStatus(_A)
_HpnicfPosaAppErrPkts_Type=Counter32
_HpnicfPosaAppErrPkts_Object=MibTableColumn
hpnicfPosaAppErrPkts=_HpnicfPosaAppErrPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,5,1,3),_HpnicfPosaAppErrPkts_Type())
hpnicfPosaAppErrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaAppErrPkts.setStatus(_A)
_HpnicfPosaAppDistributeErrCnts_Type=Counter32
_HpnicfPosaAppDistributeErrCnts_Object=MibTableColumn
hpnicfPosaAppDistributeErrCnts=_HpnicfPosaAppDistributeErrCnts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,5,1,4),_HpnicfPosaAppDistributeErrCnts_Type())
hpnicfPosaAppDistributeErrCnts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaAppDistributeErrCnts.setStatus(_A)
_HpnicfPosaAppInDiscardedPkts_Type=Counter32
_HpnicfPosaAppInDiscardedPkts_Object=MibTableColumn
hpnicfPosaAppInDiscardedPkts=_HpnicfPosaAppInDiscardedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,5,1,5),_HpnicfPosaAppInDiscardedPkts_Type())
hpnicfPosaAppInDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaAppInDiscardedPkts.setStatus(_A)
_HpnicfPosaAppOutDiscardedPkts_Type=Counter32
_HpnicfPosaAppOutDiscardedPkts_Object=MibTableColumn
hpnicfPosaAppOutDiscardedPkts=_HpnicfPosaAppOutDiscardedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,5,1,6),_HpnicfPosaAppOutDiscardedPkts_Type())
hpnicfPosaAppOutDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaAppOutDiscardedPkts.setStatus(_A)
_HpnicfPosaTerminalStatTable_Object=MibTable
hpnicfPosaTerminalStatTable=_HpnicfPosaTerminalStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,6))
if mibBuilder.loadTexts:hpnicfPosaTerminalStatTable.setStatus(_A)
_HpnicfPosaTerminalStatEntry_Object=MibTableRow
hpnicfPosaTerminalStatEntry=_HpnicfPosaTerminalStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,6,1))
hpnicfPosaTerminalStatEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:hpnicfPosaTerminalStatEntry.setStatus(_A)
_HpnicfPosaTerminalRecvPkts_Type=Counter32
_HpnicfPosaTerminalRecvPkts_Object=MibTableColumn
hpnicfPosaTerminalRecvPkts=_HpnicfPosaTerminalRecvPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,6,1,1),_HpnicfPosaTerminalRecvPkts_Type())
hpnicfPosaTerminalRecvPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTerminalRecvPkts.setStatus(_A)
_HpnicfPosaTerminalSendPkts_Type=Counter32
_HpnicfPosaTerminalSendPkts_Object=MibTableColumn
hpnicfPosaTerminalSendPkts=_HpnicfPosaTerminalSendPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,6,1,2),_HpnicfPosaTerminalSendPkts_Type())
hpnicfPosaTerminalSendPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTerminalSendPkts.setStatus(_A)
_HpnicfPosaTerminalErrPkts_Type=Counter32
_HpnicfPosaTerminalErrPkts_Object=MibTableColumn
hpnicfPosaTerminalErrPkts=_HpnicfPosaTerminalErrPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,6,1,3),_HpnicfPosaTerminalErrPkts_Type())
hpnicfPosaTerminalErrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTerminalErrPkts.setStatus(_A)
_HpnicfPosaTerminalMapErrCnts_Type=Counter32
_HpnicfPosaTerminalMapErrCnts_Object=MibTableColumn
hpnicfPosaTerminalMapErrCnts=_HpnicfPosaTerminalMapErrCnts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,6,1,4),_HpnicfPosaTerminalMapErrCnts_Type())
hpnicfPosaTerminalMapErrCnts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTerminalMapErrCnts.setStatus(_A)
_HpnicfPosaTerminalInDiscardedPkts_Type=Counter32
_HpnicfPosaTerminalInDiscardedPkts_Object=MibTableColumn
hpnicfPosaTerminalInDiscardedPkts=_HpnicfPosaTerminalInDiscardedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,6,1,5),_HpnicfPosaTerminalInDiscardedPkts_Type())
hpnicfPosaTerminalInDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTerminalInDiscardedPkts.setStatus(_A)
_HpnicfPosaTerminalOutDiscardedPkts_Type=Counter32
_HpnicfPosaTerminalOutDiscardedPkts_Object=MibTableColumn
hpnicfPosaTerminalOutDiscardedPkts=_HpnicfPosaTerminalOutDiscardedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,6,1,6),_HpnicfPosaTerminalOutDiscardedPkts_Type())
hpnicfPosaTerminalOutDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTerminalOutDiscardedPkts.setStatus(_A)
_HpnicfPosaBatchTerminalTable_Object=MibTable
hpnicfPosaBatchTerminalTable=_HpnicfPosaBatchTerminalTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,7))
if mibBuilder.loadTexts:hpnicfPosaBatchTerminalTable.setStatus(_A)
_HpnicfPosaBatchTerminalEntry_Object=MibTableRow
hpnicfPosaBatchTerminalEntry=_HpnicfPosaBatchTerminalEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,7,1))
hpnicfPosaBatchTerminalEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:hpnicfPosaBatchTerminalEntry.setStatus(_A)
class _HpnicfPosaBatchTerminalFirstID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfPosaBatchTerminalFirstID_Type.__name__=_C
_HpnicfPosaBatchTerminalFirstID_Object=MibTableColumn
hpnicfPosaBatchTerminalFirstID=_HpnicfPosaBatchTerminalFirstID_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,7,1,1),_HpnicfPosaBatchTerminalFirstID_Type())
hpnicfPosaBatchTerminalFirstID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaBatchTerminalFirstID.setStatus(_A)
_HpnicfPosaBatchTerminalRowStatus_Type=RowStatus
_HpnicfPosaBatchTerminalRowStatus_Object=MibTableColumn
hpnicfPosaBatchTerminalRowStatus=_HpnicfPosaBatchTerminalRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,7,1,2),_HpnicfPosaBatchTerminalRowStatus_Type())
hpnicfPosaBatchTerminalRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaBatchTerminalRowStatus.setStatus(_A)
_HpnicfPosaTcpTermStatTable_Object=MibTable
hpnicfPosaTcpTermStatTable=_HpnicfPosaTcpTermStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8))
if mibBuilder.loadTexts:hpnicfPosaTcpTermStatTable.setStatus(_A)
_HpnicfPosaTcpTermStatEntry_Object=MibTableRow
hpnicfPosaTcpTermStatEntry=_HpnicfPosaTcpTermStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1))
hpnicfPosaTcpTermStatEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:hpnicfPosaTcpTermStatEntry.setStatus(_A)
class _HpnicfPosaTcpTermStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfPosaTcpTermStatIndex_Type.__name__=_C
_HpnicfPosaTcpTermStatIndex_Object=MibTableColumn
hpnicfPosaTcpTermStatIndex=_HpnicfPosaTcpTermStatIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,1),_HpnicfPosaTcpTermStatIndex_Type())
hpnicfPosaTcpTermStatIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfPosaTcpTermStatIndex.setStatus(_A)
_HpnicfPosaTcpTermStatIPType_Type=InetAddressType
_HpnicfPosaTcpTermStatIPType_Object=MibTableColumn
hpnicfPosaTcpTermStatIPType=_HpnicfPosaTcpTermStatIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,2),_HpnicfPosaTcpTermStatIPType_Type())
hpnicfPosaTcpTermStatIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTcpTermStatIPType.setStatus(_A)
_HpnicfPosaTcpTermStatIP_Type=InetAddress
_HpnicfPosaTcpTermStatIP_Object=MibTableColumn
hpnicfPosaTcpTermStatIP=_HpnicfPosaTcpTermStatIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,3),_HpnicfPosaTcpTermStatIP_Type())
hpnicfPosaTcpTermStatIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTcpTermStatIP.setStatus(_A)
_HpnicfPosaTcpTermStatIPMask_Type=InetAddress
_HpnicfPosaTcpTermStatIPMask_Object=MibTableColumn
hpnicfPosaTcpTermStatIPMask=_HpnicfPosaTcpTermStatIPMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,4),_HpnicfPosaTcpTermStatIPMask_Type())
hpnicfPosaTcpTermStatIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTcpTermStatIPMask.setStatus(_A)
_HpnicfPosaTcpTermRecvPkts_Type=Counter64
_HpnicfPosaTcpTermRecvPkts_Object=MibTableColumn
hpnicfPosaTcpTermRecvPkts=_HpnicfPosaTcpTermRecvPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,5),_HpnicfPosaTcpTermRecvPkts_Type())
hpnicfPosaTcpTermRecvPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTcpTermRecvPkts.setStatus(_A)
_HpnicfPosaTcpTermSendPkts_Type=Counter64
_HpnicfPosaTcpTermSendPkts_Object=MibTableColumn
hpnicfPosaTcpTermSendPkts=_HpnicfPosaTcpTermSendPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,6),_HpnicfPosaTcpTermSendPkts_Type())
hpnicfPosaTcpTermSendPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTcpTermSendPkts.setStatus(_A)
_HpnicfPosaTcpTermErrPkts_Type=Counter64
_HpnicfPosaTcpTermErrPkts_Object=MibTableColumn
hpnicfPosaTcpTermErrPkts=_HpnicfPosaTcpTermErrPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,7),_HpnicfPosaTcpTermErrPkts_Type())
hpnicfPosaTcpTermErrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTcpTermErrPkts.setStatus(_A)
_HpnicfPosaTcpTermMapErrCnts_Type=Counter64
_HpnicfPosaTcpTermMapErrCnts_Object=MibTableColumn
hpnicfPosaTcpTermMapErrCnts=_HpnicfPosaTcpTermMapErrCnts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,8),_HpnicfPosaTcpTermMapErrCnts_Type())
hpnicfPosaTcpTermMapErrCnts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTcpTermMapErrCnts.setStatus(_A)
_HpnicfPosaTcpTermInDiscardedPkts_Type=Counter64
_HpnicfPosaTcpTermInDiscardedPkts_Object=MibTableColumn
hpnicfPosaTcpTermInDiscardedPkts=_HpnicfPosaTcpTermInDiscardedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,9),_HpnicfPosaTcpTermInDiscardedPkts_Type())
hpnicfPosaTcpTermInDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTcpTermInDiscardedPkts.setStatus(_A)
_HpnicfPosaTcpTermOutDiscardedPkts_Type=Counter64
_HpnicfPosaTcpTermOutDiscardedPkts_Object=MibTableColumn
hpnicfPosaTcpTermOutDiscardedPkts=_HpnicfPosaTcpTermOutDiscardedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,10),_HpnicfPosaTcpTermOutDiscardedPkts_Type())
hpnicfPosaTcpTermOutDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaTcpTermOutDiscardedPkts.setStatus(_A)
_HpnicfPosaTcpTermStatRowStatus_Type=RowStatus
_HpnicfPosaTcpTermStatRowStatus_Object=MibTableColumn
hpnicfPosaTcpTermStatRowStatus=_HpnicfPosaTcpTermStatRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,8,1,11),_HpnicfPosaTcpTermStatRowStatus_Type())
hpnicfPosaTcpTermStatRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaTcpTermStatRowStatus.setStatus(_A)
_HpnicfPosaFcmConfTable_Object=MibTable
hpnicfPosaFcmConfTable=_HpnicfPosaFcmConfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9))
if mibBuilder.loadTexts:hpnicfPosaFcmConfTable.setStatus(_A)
_HpnicfPosaFcmConfEntry_Object=MibTableRow
hpnicfPosaFcmConfEntry=_HpnicfPosaFcmConfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1))
hpnicfPosaFcmConfEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:hpnicfPosaFcmConfEntry.setStatus(_A)
class _HpnicfPosaFcmNegoHookOff_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,6000))
_HpnicfPosaFcmNegoHookOff_Type.__name__=_C
_HpnicfPosaFcmNegoHookOff_Object=MibTableColumn
hpnicfPosaFcmNegoHookOff=_HpnicfPosaFcmNegoHookOff_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1,1),_HpnicfPosaFcmNegoHookOff_Type())
hpnicfPosaFcmNegoHookOff.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmNegoHookOff.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmNegoHookOff.setUnits(_K)
class _HpnicfPosaFcmNegoSilence_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3000))
_HpnicfPosaFcmNegoSilence_Type.__name__=_C
_HpnicfPosaFcmNegoSilence_Object=MibTableColumn
hpnicfPosaFcmNegoSilence=_HpnicfPosaFcmNegoSilence_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1,2),_HpnicfPosaFcmNegoSilence_Type())
hpnicfPosaFcmNegoSilence.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmNegoSilence.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmNegoSilence.setUnits(_K)
class _HpnicfPosaFcmNegoScrmbBinary1_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1500))
_HpnicfPosaFcmNegoScrmbBinary1_Type.__name__=_C
_HpnicfPosaFcmNegoScrmbBinary1_Object=MibTableColumn
hpnicfPosaFcmNegoScrmbBinary1=_HpnicfPosaFcmNegoScrmbBinary1_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1,3),_HpnicfPosaFcmNegoScrmbBinary1_Type())
hpnicfPosaFcmNegoScrmbBinary1.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmNegoScrmbBinary1.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmNegoScrmbBinary1.setUnits(_K)
class _HpnicfPosaFcmNegoUnscrmbBinary1_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1500))
_HpnicfPosaFcmNegoUnscrmbBinary1_Type.__name__=_C
_HpnicfPosaFcmNegoUnscrmbBinary1_Object=MibTableColumn
hpnicfPosaFcmNegoUnscrmbBinary1=_HpnicfPosaFcmNegoUnscrmbBinary1_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1,4),_HpnicfPosaFcmNegoUnscrmbBinary1_Type())
hpnicfPosaFcmNegoUnscrmbBinary1.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmNegoUnscrmbBinary1.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmNegoUnscrmbBinary1.setUnits(_K)
class _HpnicfPosaFcmThresholdRlsdOff_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,75))
_HpnicfPosaFcmThresholdRlsdOff_Type.__name__=_C
_HpnicfPosaFcmThresholdRlsdOff_Object=MibTableColumn
hpnicfPosaFcmThresholdRlsdOff=_HpnicfPosaFcmThresholdRlsdOff_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1,5),_HpnicfPosaFcmThresholdRlsdOff_Type())
hpnicfPosaFcmThresholdRlsdOff.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmThresholdRlsdOff.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmThresholdRlsdOff.setUnits(_P)
class _HpnicfPosaFcmThresholdRlsdOn_Type(Integer32):defaultValue=43;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,75))
_HpnicfPosaFcmThresholdRlsdOn_Type.__name__=_C
_HpnicfPosaFcmThresholdRlsdOn_Object=MibTableColumn
hpnicfPosaFcmThresholdRlsdOn=_HpnicfPosaFcmThresholdRlsdOn_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1,6),_HpnicfPosaFcmThresholdRlsdOn_Type())
hpnicfPosaFcmThresholdRlsdOn.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmThresholdRlsdOn.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmThresholdRlsdOn.setUnits(_P)
class _HpnicfPosaFcmThresholdTxPower_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,42))
_HpnicfPosaFcmThresholdTxPower_Type.__name__=_C
_HpnicfPosaFcmThresholdTxPower_Object=MibTableColumn
hpnicfPosaFcmThresholdTxPower=_HpnicfPosaFcmThresholdTxPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1,7),_HpnicfPosaFcmThresholdTxPower_Type())
hpnicfPosaFcmThresholdTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmThresholdTxPower.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmThresholdTxPower.setUnits(_P)
class _HpnicfPosaFcmThresholdAnswerTone_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,42))
_HpnicfPosaFcmThresholdAnswerTone_Type.__name__=_C
_HpnicfPosaFcmThresholdAnswerTone_Object=MibTableColumn
hpnicfPosaFcmThresholdAnswerTone=_HpnicfPosaFcmThresholdAnswerTone_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,9,1,8),_HpnicfPosaFcmThresholdAnswerTone_Type())
hpnicfPosaFcmThresholdAnswerTone.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPosaFcmThresholdAnswerTone.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPosaFcmThresholdAnswerTone.setUnits(_P)
_HpnicfPosaCallerStatTable_Object=MibTable
hpnicfPosaCallerStatTable=_HpnicfPosaCallerStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10))
if mibBuilder.loadTexts:hpnicfPosaCallerStatTable.setStatus(_A)
_HpnicfPosaCallerStatEntry_Object=MibTableRow
hpnicfPosaCallerStatEntry=_HpnicfPosaCallerStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1))
hpnicfPosaCallerStatEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:hpnicfPosaCallerStatEntry.setStatus(_A)
class _HpnicfPosaCallerStatCallerID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfPosaCallerStatCallerID_Type.__name__=_I
_HpnicfPosaCallerStatCallerID_Object=MibTableColumn
hpnicfPosaCallerStatCallerID=_HpnicfPosaCallerStatCallerID_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1,1),_HpnicfPosaCallerStatCallerID_Type())
hpnicfPosaCallerStatCallerID.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfPosaCallerStatCallerID.setStatus(_A)
_HpnicfPosaCallerRecvPkts_Type=Counter64
_HpnicfPosaCallerRecvPkts_Object=MibTableColumn
hpnicfPosaCallerRecvPkts=_HpnicfPosaCallerRecvPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1,2),_HpnicfPosaCallerRecvPkts_Type())
hpnicfPosaCallerRecvPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaCallerRecvPkts.setStatus(_A)
_HpnicfPosaCallerSendPkts_Type=Counter64
_HpnicfPosaCallerSendPkts_Object=MibTableColumn
hpnicfPosaCallerSendPkts=_HpnicfPosaCallerSendPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1,3),_HpnicfPosaCallerSendPkts_Type())
hpnicfPosaCallerSendPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaCallerSendPkts.setStatus(_A)
_HpnicfPosaCallerErrPkts_Type=Counter64
_HpnicfPosaCallerErrPkts_Object=MibTableColumn
hpnicfPosaCallerErrPkts=_HpnicfPosaCallerErrPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1,4),_HpnicfPosaCallerErrPkts_Type())
hpnicfPosaCallerErrPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaCallerErrPkts.setStatus(_A)
_HpnicfPosaCallerMapErrCnts_Type=Counter64
_HpnicfPosaCallerMapErrCnts_Object=MibTableColumn
hpnicfPosaCallerMapErrCnts=_HpnicfPosaCallerMapErrCnts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1,5),_HpnicfPosaCallerMapErrCnts_Type())
hpnicfPosaCallerMapErrCnts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaCallerMapErrCnts.setStatus(_A)
_HpnicfPosaCallerInDiscardedPkts_Type=Counter64
_HpnicfPosaCallerInDiscardedPkts_Object=MibTableColumn
hpnicfPosaCallerInDiscardedPkts=_HpnicfPosaCallerInDiscardedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1,6),_HpnicfPosaCallerInDiscardedPkts_Type())
hpnicfPosaCallerInDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaCallerInDiscardedPkts.setStatus(_A)
_HpnicfPosaCallerOutDiscardedPkts_Type=Counter64
_HpnicfPosaCallerOutDiscardedPkts_Object=MibTableColumn
hpnicfPosaCallerOutDiscardedPkts=_HpnicfPosaCallerOutDiscardedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1,7),_HpnicfPosaCallerOutDiscardedPkts_Type())
hpnicfPosaCallerOutDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfPosaCallerOutDiscardedPkts.setStatus(_A)
_HpnicfPosaCallerStatRowStatus_Type=RowStatus
_HpnicfPosaCallerStatRowStatus_Object=MibTableColumn
hpnicfPosaCallerStatRowStatus=_HpnicfPosaCallerStatRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,2,10,1,8),_HpnicfPosaCallerStatRowStatus_Type())
hpnicfPosaCallerStatRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosaCallerStatRowStatus.setStatus(_A)
_HpnicfPosaTrap_ObjectIdentity=ObjectIdentity
hpnicfPosaTrap=_HpnicfPosaTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,92,3))
_HpnicfPosaTrapPrex_ObjectIdentity=ObjectIdentity
hpnicfPosaTrapPrex=_HpnicfPosaTrapPrex_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0))
_HpnicfPosaTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfPosaTrapObjects=_HpnicfPosaTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,92,3,1))
class _HpnicfPosaAppStateChangeObject_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('available',1),('unavailable',2)))
_HpnicfPosaAppStateChangeObject_Type.__name__=_C
_HpnicfPosaAppStateChangeObject_Object=MibScalar
hpnicfPosaAppStateChangeObject=_HpnicfPosaAppStateChangeObject_Object((1,3,6,1,4,1,11,2,14,11,15,2,92,3,1,1),_HpnicfPosaAppStateChangeObject_Type())
hpnicfPosaAppStateChangeObject.setMaxAccess(_R)
if mibBuilder.loadTexts:hpnicfPosaAppStateChangeObject.setStatus(_A)
hpnicfPosaServerStatusChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0,1))
hpnicfPosaServerStatusChange.setObjects((_F,_b))
if mibBuilder.loadTexts:hpnicfPosaServerStatusChange.setStatus(_A)
hpnicfPosaAppStateChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0,2))
hpnicfPosaAppStateChange.setObjects(*((_F,_N),(_F,_c)))
if mibBuilder.loadTexts:hpnicfPosaAppStateChange.setStatus(_A)
hpnicfPosaTerminalHangUp=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0,3))
hpnicfPosaTerminalHangUp.setObjects(*((_H,_J),(_H,_M)))
if mibBuilder.loadTexts:hpnicfPosaTerminalHangUp.setStatus(_A)
hpnicfPosaFcmLinkNegoFailed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0,4))
hpnicfPosaFcmLinkNegoFailed.setObjects(*((_H,_J),(_H,_M)))
if mibBuilder.loadTexts:hpnicfPosaFcmLinkNegoFailed.setStatus(_A)
hpnicfPosaFcmPhyNegoFailed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0,5))
hpnicfPosaFcmPhyNegoFailed.setObjects(*((_H,_J),(_H,_M)))
if mibBuilder.loadTexts:hpnicfPosaFcmPhyNegoFailed.setStatus(_A)
hpnicfPosaTcpConnectionExceed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0,6))
hpnicfPosaTcpConnectionExceed.setObjects((_F,_d))
if mibBuilder.loadTexts:hpnicfPosaTcpConnectionExceed.setStatus(_A)
hpnicfPosaFcmConnectionExceed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0,7))
hpnicfPosaFcmConnectionExceed.setObjects((_F,_e))
if mibBuilder.loadTexts:hpnicfPosaFcmConnectionExceed.setStatus(_A)
hpnicfPosaTcpTradeExceed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,92,3,0,8))
hpnicfPosaTcpTradeExceed.setObjects(*((_F,_f),(_F,_O)))
if mibBuilder.loadTexts:hpnicfPosaTcpTradeExceed.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_S:HpnicfAppServiceType,_T:HpnicfAppMode,'HpnicfPeerState':HpnicfPeerState,_V:HpnicfTerminalAccessType,_U:HpnicfTpduChangeStrategy,'hpnicfPosa':hpnicfPosa,'hpnicfPosaControl':hpnicfPosaControl,_b:hpnicfPosaServerEnable,'hpnicfPosaFcmAnswerTimeout':hpnicfPosaFcmAnswerTimeout,'hpnicfPosaFcmTradeTimeout':hpnicfPosaFcmTradeTimeout,'hpnicfPosaFcmIdleTimeout':hpnicfPosaFcmIdleTimeout,'hpnicfPosaSrvStateChangeTrapEnable':hpnicfPosaSrvStateChangeTrapEnable,'hpnicfPosaAppStateChangeTrapEnable':hpnicfPosaAppStateChangeTrapEnable,'hpnicfPosaTerminalHangUpTrapEnable':hpnicfPosaTerminalHangUpTrapEnable,'hpnicfPosaFcmLnkNegoFailTrapEnable':hpnicfPosaFcmLnkNegoFailTrapEnable,'hpnicfPosaFcmPhyNegoFailTrapEnable':hpnicfPosaFcmPhyNegoFailTrapEnable,'hpnicfPosaTcpConnectionNumber':hpnicfPosaTcpConnectionNumber,'hpnicfPosaFcmConnectionNumber':hpnicfPosaFcmConnectionNumber,_d:hpnicfPosaTcpConnectionThreshold,_e:hpnicfPosaFcmConnectionThreshold,'hpnicfPosaTcpConnectionTrapEnable':hpnicfPosaTcpConnectionTrapEnable,'hpnicfPosaFcmConnectionTrapEnable':hpnicfPosaFcmConnectionTrapEnable,_f:hpnicfPosaTcpTradeLimit,'hpnicfPosaTcpTradeTrapEnable':hpnicfPosaTcpTradeTrapEnable,'hpnicfPosaTcpTradeTimeout':hpnicfPosaTcpTradeTimeout,'hpnicfPosaTables':hpnicfPosaTables,'hpnicfPosaAppTable':hpnicfPosaAppTable,'hpnicfPosaAppEntry':hpnicfPosaAppEntry,_N:hpnicfPosaAppID,'hpnicfPosaAppServiceType':hpnicfPosaAppServiceType,'hpnicfPosaAppIfIndex':hpnicfPosaAppIfIndex,'hpnicfPosaAppMode':hpnicfPosaAppMode,'hpnicfPosaAppHostIPType':hpnicfPosaAppHostIPType,'hpnicfPosaAppHostIP':hpnicfPosaAppHostIP,'hpnicfPosaAppHostPort':hpnicfPosaAppHostPort,'hpnicfPosaAppRouterIPType':hpnicfPosaAppRouterIPType,'hpnicfPosaAppRouterIP':hpnicfPosaAppRouterIP,'hpnicfPosaAppKeepAliveInterval':hpnicfPosaAppKeepAliveInterval,'hpnicfPosaAppKeepAliveCount':hpnicfPosaAppKeepAliveCount,'hpnicfPosaAppConnectTimeout':hpnicfPosaAppConnectTimeout,'hpnicfPosaAppState':hpnicfPosaAppState,'hpnicfPosaAppRowStatus':hpnicfPosaAppRowStatus,'hpnicfPosaAppName':hpnicfPosaAppName,'hpnicfPosaCallerIDTransEnable':hpnicfPosaCallerIDTransEnable,'hpnicfPosaTpduChangeStrategy':hpnicfPosaTpduChangeStrategy,'hpnicfPosaBackupAppID':hpnicfPosaBackupAppID,'hpnicfPosaQuietTimeOut':hpnicfPosaQuietTimeOut,'hpnicfPosaAppHello':hpnicfPosaAppHello,'hpnicfPosaAppHelloInterval':hpnicfPosaAppHelloInterval,'hpnicfPosaAppRouterPort':hpnicfPosaAppRouterPort,'hpnicfPosaTerminalTable':hpnicfPosaTerminalTable,'hpnicfPosaTerminalEntry':hpnicfPosaTerminalEntry,_O:hpnicfPosaTerminalID,'hpnicfPosaTerminalAccessType':hpnicfPosaTerminalAccessType,'hpnicfPosaTerminalIfIndex':hpnicfPosaTerminalIfIndex,'hpnicfPosaTerminalTransAppID':hpnicfPosaTerminalTransAppID,'hpnicfPosaTerminalListenPort':hpnicfPosaTerminalListenPort,'hpnicfPosaTerminalState':hpnicfPosaTerminalState,'hpnicfPosaTerminalRowStatus':hpnicfPosaTerminalRowStatus,'hpnicfPosaTerminalName':hpnicfPosaTerminalName,'hpnicfPosaTerminalCfgIfIndex':hpnicfPosaTerminalCfgIfIndex,'hpnicfPosaMapTable':hpnicfPosaMapTable,'hpnicfPosaMapEntry':hpnicfPosaMapEntry,_X:hpnicfPosaMapDestCode,'hpnicfPosaMapAppID':hpnicfPosaMapAppID,'hpnicfPosaMapRowStatus':hpnicfPosaMapRowStatus,_W:hpnicfPosaMapSrcCode,'hpnicfPosaFcmStatTable':hpnicfPosaFcmStatTable,'hpnicfPosaFcmStatEntry':hpnicfPosaFcmStatEntry,_Y:hpnicfPosaFcmStatIfIndex,'hpnicfPosaFcmStatTimeoutCnts':hpnicfPosaFcmStatTimeoutCnts,'hpnicfPosaFcmStatConnectFailCnts':hpnicfPosaFcmStatConnectFailCnts,'hpnicfPosaFcmStatTransCnts':hpnicfPosaFcmStatTransCnts,'hpnicfPosaFcmStatTransSuccessCnts':hpnicfPosaFcmStatTransSuccessCnts,'hpnicfPosaFcmStatTransCntsClear':hpnicfPosaFcmStatTransCntsClear,'hpnicfPosaAppStatTable':hpnicfPosaAppStatTable,'hpnicfPosaAppStatEntry':hpnicfPosaAppStatEntry,'hpnicfPosaAppRecvPkts':hpnicfPosaAppRecvPkts,'hpnicfPosaAppSendPkts':hpnicfPosaAppSendPkts,'hpnicfPosaAppErrPkts':hpnicfPosaAppErrPkts,'hpnicfPosaAppDistributeErrCnts':hpnicfPosaAppDistributeErrCnts,'hpnicfPosaAppInDiscardedPkts':hpnicfPosaAppInDiscardedPkts,'hpnicfPosaAppOutDiscardedPkts':hpnicfPosaAppOutDiscardedPkts,'hpnicfPosaTerminalStatTable':hpnicfPosaTerminalStatTable,'hpnicfPosaTerminalStatEntry':hpnicfPosaTerminalStatEntry,'hpnicfPosaTerminalRecvPkts':hpnicfPosaTerminalRecvPkts,'hpnicfPosaTerminalSendPkts':hpnicfPosaTerminalSendPkts,'hpnicfPosaTerminalErrPkts':hpnicfPosaTerminalErrPkts,'hpnicfPosaTerminalMapErrCnts':hpnicfPosaTerminalMapErrCnts,'hpnicfPosaTerminalInDiscardedPkts':hpnicfPosaTerminalInDiscardedPkts,'hpnicfPosaTerminalOutDiscardedPkts':hpnicfPosaTerminalOutDiscardedPkts,'hpnicfPosaBatchTerminalTable':hpnicfPosaBatchTerminalTable,'hpnicfPosaBatchTerminalEntry':hpnicfPosaBatchTerminalEntry,'hpnicfPosaBatchTerminalFirstID':hpnicfPosaBatchTerminalFirstID,'hpnicfPosaBatchTerminalRowStatus':hpnicfPosaBatchTerminalRowStatus,'hpnicfPosaTcpTermStatTable':hpnicfPosaTcpTermStatTable,'hpnicfPosaTcpTermStatEntry':hpnicfPosaTcpTermStatEntry,_Z:hpnicfPosaTcpTermStatIndex,'hpnicfPosaTcpTermStatIPType':hpnicfPosaTcpTermStatIPType,'hpnicfPosaTcpTermStatIP':hpnicfPosaTcpTermStatIP,'hpnicfPosaTcpTermStatIPMask':hpnicfPosaTcpTermStatIPMask,'hpnicfPosaTcpTermRecvPkts':hpnicfPosaTcpTermRecvPkts,'hpnicfPosaTcpTermSendPkts':hpnicfPosaTcpTermSendPkts,'hpnicfPosaTcpTermErrPkts':hpnicfPosaTcpTermErrPkts,'hpnicfPosaTcpTermMapErrCnts':hpnicfPosaTcpTermMapErrCnts,'hpnicfPosaTcpTermInDiscardedPkts':hpnicfPosaTcpTermInDiscardedPkts,'hpnicfPosaTcpTermOutDiscardedPkts':hpnicfPosaTcpTermOutDiscardedPkts,'hpnicfPosaTcpTermStatRowStatus':hpnicfPosaTcpTermStatRowStatus,'hpnicfPosaFcmConfTable':hpnicfPosaFcmConfTable,'hpnicfPosaFcmConfEntry':hpnicfPosaFcmConfEntry,'hpnicfPosaFcmNegoHookOff':hpnicfPosaFcmNegoHookOff,'hpnicfPosaFcmNegoSilence':hpnicfPosaFcmNegoSilence,'hpnicfPosaFcmNegoScrmbBinary1':hpnicfPosaFcmNegoScrmbBinary1,'hpnicfPosaFcmNegoUnscrmbBinary1':hpnicfPosaFcmNegoUnscrmbBinary1,'hpnicfPosaFcmThresholdRlsdOff':hpnicfPosaFcmThresholdRlsdOff,'hpnicfPosaFcmThresholdRlsdOn':hpnicfPosaFcmThresholdRlsdOn,'hpnicfPosaFcmThresholdTxPower':hpnicfPosaFcmThresholdTxPower,'hpnicfPosaFcmThresholdAnswerTone':hpnicfPosaFcmThresholdAnswerTone,'hpnicfPosaCallerStatTable':hpnicfPosaCallerStatTable,'hpnicfPosaCallerStatEntry':hpnicfPosaCallerStatEntry,_a:hpnicfPosaCallerStatCallerID,'hpnicfPosaCallerRecvPkts':hpnicfPosaCallerRecvPkts,'hpnicfPosaCallerSendPkts':hpnicfPosaCallerSendPkts,'hpnicfPosaCallerErrPkts':hpnicfPosaCallerErrPkts,'hpnicfPosaCallerMapErrCnts':hpnicfPosaCallerMapErrCnts,'hpnicfPosaCallerInDiscardedPkts':hpnicfPosaCallerInDiscardedPkts,'hpnicfPosaCallerOutDiscardedPkts':hpnicfPosaCallerOutDiscardedPkts,'hpnicfPosaCallerStatRowStatus':hpnicfPosaCallerStatRowStatus,'hpnicfPosaTrap':hpnicfPosaTrap,'hpnicfPosaTrapPrex':hpnicfPosaTrapPrex,'hpnicfPosaServerStatusChange':hpnicfPosaServerStatusChange,'hpnicfPosaAppStateChange':hpnicfPosaAppStateChange,'hpnicfPosaTerminalHangUp':hpnicfPosaTerminalHangUp,'hpnicfPosaFcmLinkNegoFailed':hpnicfPosaFcmLinkNegoFailed,'hpnicfPosaFcmPhyNegoFailed':hpnicfPosaFcmPhyNegoFailed,'hpnicfPosaTcpConnectionExceed':hpnicfPosaTcpConnectionExceed,'hpnicfPosaFcmConnectionExceed':hpnicfPosaFcmConnectionExceed,'hpnicfPosaTcpTradeExceed':hpnicfPosaTcpTradeExceed,'hpnicfPosaTrapObjects':hpnicfPosaTrapObjects,_c:hpnicfPosaAppStateChangeObject})