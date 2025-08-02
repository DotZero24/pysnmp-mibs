_An='tmnxBmpConfigV19v0Group'
_Am='tmnxBmpNotificationV16Group'
_Al='tmnxBmpNotificationObjs'
_Ak='tmnxBmpConfigV16Group'
_Aj='tmnxBmpConfigV15Group'
_Ai='tmnxBmpSessionStatusChange'
_Ah='tmnxBmpCollectorIpv6Port'
_Ag='tmnxBmpCollectorIpv6Addr'
_Af='tmnxBmpCollectorIpv6AddrType'
_Ae='tmnxBmpCollectorIpv4Port'
_Ad='tmnxBmpCollectorIpv4Addr'
_Ac='tmnxBmpCollectorIpv4AddrType'
_Ab='tmnxBmpCollectorAdminState'
_Aa='tmnxBmpStationFamily'
_AZ='tmnxBmpStationReportLocalRoutes'
_AY='tmnxBmpSessionRouteMirrorMsgs'
_AX='tmnxBmpSessionTerminationMsgs'
_AW='tmnxBmpSessionInitiationMsgs'
_AV='tmnxBmpSessionPeerDownMsgs'
_AU='tmnxBmpSessionPeerUpMsgs'
_AT='tmnxBmpSessionStatisticsMsgs'
_AS='tmnxBmpSessionRouteMonitorMsgs'
_AR='tmnxBmpSessionBytesSent'
_AQ='tmnxBmpSessionLastMsgSent'
_AP='tmnxBmpSessionConnStateChanged'
_AO='tmnxBmpSessionLocalAddrPort'
_AN='tmnxBmpSessionLocalAddr'
_AM='tmnxBmpSessionLocalAddrType'
_AL='tmnxBmpSessionConnectionState'
_AK='tmnxBmpStationTcpKaCount'
_AJ='tmnxBmpStationTcpKaInterval'
_AI='tmnxBmpStationTcpKaIdle'
_AH='tmnxBmpStationTcpKaAdminState'
_AG='tmnxBgpMonitorStationRowStatus'
_AF='tmnxBgpMonitorRouteMonitoring'
_AE='tmnxBgpMonitorAllStations'
_AD='tmnxBgpMonitorLastChanged'
_AC='tmnxBgpMonitorAdminState'
_AB='tmnxBgpMonitorRowStatus'
_AA='tmnxBgpMonitorTableLastCh'
_A9='tmnxBmpStationStatsReportIvl'
_A8='tmnxBmpStationInitiationMessage'
_A7='tmnxBmpStationRouter'
_A6='tmnxBmpStationRemotePort'
_A5='tmnxBmpStationRemoteIpAddress'
_A4='tmnxBmpStationRemoteIpAddrType'
_A3='tmnxBmpStationLocalIpAddress'
_A2='tmnxBmpStationLocalIpAddrType'
_A1='tmnxBmpStationConnectRetry'
_A0='tmnxBmpStationDescr'
_z='tmnxBmpStationAdminState'
_y='tmnxBmpStationLastChanged'
_x='tmnxBmpStationRowStatus'
_w='tmnxBmpStationTableLastCh'
_v='tmnxBmpAdminState'
_u='tmnxBmpSessionStationName'
_t='tmnxBmpSessionVRtrID'
_s='tmnxBgpMonitorStationName'
_r='tmnxBgpMonitorStationPeer'
_q='tmnxBgpMonitorStationPeerType'
_p='tmnxBgpMonitorStationPeerGroup'
_o='tmnxBgpMonitorStationVRtrID'
_n='tmnxBgpMonitorStationType'
_m='TmnxBgpMonitorRouteMonitoring'
_l='tmnxBgpMonitorPeer'
_k='tmnxBgpMonitorPeerType'
_j='tmnxBgpMonitorPeerGroup'
_i='tmnxBgpMonitorVRtrID'
_h='tmnxBgpMonitorType'
_g='TmnxBmpConnectionMode'
_f='tmnxBmpStationName'
_e='TmnxVRtrID'
_d='TItemDescription'
_c='TmnxIpFamily'
_b='TruthValue'
_a='tmnxBmpSessionChangeReason'
_Z='tmnxBmpSessionChangeNewState'
_Y='tmnxBmpSessionChangeOldState'
_X='tmnxBmpSessionChangeStationName'
_W='tmnxBmpSessionChangeVRtrID'
_V='tmnxBmpStationRoutesReportIvl'
_U='tmnxBmpStationMode'
_T='tmnxBmpStationErrorInterval'
_S='tmnxBmpStationMaxWaitTime'
_R='tmnxBmpStationSecondWaitTime'
_Q='tmnxBmpStationInitialWaitTime'
_P='DisplayString'
_O='minutes'
_N='InetPortNumber'
_M='accessible-for-notify'
_L='obsolete'
_K='seconds'
_J='TmnxAdminState'
_I='InetAddressType'
_H='read-write'
_G='InetAddress'
_F='Unsigned32'
_E='not-accessible'
_D='read-only'
_C='read-create'
_B='current'
_A='TIMETRA-BMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_I,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_b)
TmnxIpFamily,=mibBuilder.importSymbols('TIMETRA-BGP-MIB',_c)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TItemDescription,TLNamedItemOrEmpty,TNamedItem,TmnxAdminState,TmnxVRtrID=mibBuilder.importSymbols('TIMETRA-TC-MIB',_d,'TLNamedItemOrEmpty','TNamedItem',_J,_e)
timetraBmpMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,108))
if mibBuilder.loadTexts:timetraBmpMIBModule.setRevisions(('2016-01-01 00:00',))
class TmnxBmpConnectionMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
class TmnxBgpMonitorType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('bgpInstance',0),('bgpPeerGroup',1),('bgpNeighbor',2)))
class TmnxBgpMonitorRouteMonitoring(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('prePolicy',0),('postPolicy',1)))
class TmnxBmpSessionConnectionState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('inactive',0),('shutdown',1),('idle',2),('connecting',3),('welcoming',4),('established',5)))
_TmnxBmpConformance_ObjectIdentity=ObjectIdentity
tmnxBmpConformance=_TmnxBmpConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,108))
_TmnxBmpCompliances_ObjectIdentity=ObjectIdentity
tmnxBmpCompliances=_TmnxBmpCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,108,1))
_TmnxBmpGroups_ObjectIdentity=ObjectIdentity
tmnxBmpGroups=_TmnxBmpGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,108,2))
_TmnxBmpV15v0Groups_ObjectIdentity=ObjectIdentity
tmnxBmpV15v0Groups=_TmnxBmpV15v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,108,2,1))
_TmnxBmpV16v0Groups_ObjectIdentity=ObjectIdentity
tmnxBmpV16v0Groups=_TmnxBmpV16v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,108,2,2))
_TmnxBmpV19v0Groups_ObjectIdentity=ObjectIdentity
tmnxBmpV19v0Groups=_TmnxBmpV19v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,108,2,3))
_TmnxBmpObjs_ObjectIdentity=ObjectIdentity
tmnxBmpObjs=_TmnxBmpObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,108))
_TmnxBmpParameterObjs_ObjectIdentity=ObjectIdentity
tmnxBmpParameterObjs=_TmnxBmpParameterObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,108,1))
class _TmnxBmpAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxBmpAdminState_Type.__name__=_J
_TmnxBmpAdminState_Object=MibScalar
tmnxBmpAdminState=_TmnxBmpAdminState_Object((1,3,6,1,4,1,6527,3,1,2,108,1,1),_TmnxBmpAdminState_Type())
tmnxBmpAdminState.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxBmpAdminState.setStatus(_B)
_TmnxBmpStationTableLastCh_Type=TimeStamp
_TmnxBmpStationTableLastCh_Object=MibScalar
tmnxBmpStationTableLastCh=_TmnxBmpStationTableLastCh_Object((1,3,6,1,4,1,6527,3,1,2,108,1,2),_TmnxBmpStationTableLastCh_Type())
tmnxBmpStationTableLastCh.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpStationTableLastCh.setStatus(_B)
_TmnxBgpMonitorTableLastCh_Type=TimeStamp
_TmnxBgpMonitorTableLastCh_Object=MibScalar
tmnxBgpMonitorTableLastCh=_TmnxBgpMonitorTableLastCh_Object((1,3,6,1,4,1,6527,3,1,2,108,1,3),_TmnxBgpMonitorTableLastCh_Type())
tmnxBgpMonitorTableLastCh.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBgpMonitorTableLastCh.setStatus(_B)
_TmnxBmpStationObjs_ObjectIdentity=ObjectIdentity
tmnxBmpStationObjs=_TmnxBmpStationObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,108,2))
_TmnxBmpStationTable_Object=MibTable
tmnxBmpStationTable=_TmnxBmpStationTable_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1))
if mibBuilder.loadTexts:tmnxBmpStationTable.setStatus(_B)
_TmnxBmpStationEntry_Object=MibTableRow
tmnxBmpStationEntry=_TmnxBmpStationEntry_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1))
tmnxBmpStationEntry.setIndexNames((1,_A,_f))
if mibBuilder.loadTexts:tmnxBmpStationEntry.setStatus(_B)
_TmnxBmpStationName_Type=TNamedItem
_TmnxBmpStationName_Object=MibTableColumn
tmnxBmpStationName=_TmnxBmpStationName_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,1),_TmnxBmpStationName_Type())
tmnxBmpStationName.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBmpStationName.setStatus(_B)
_TmnxBmpStationRowStatus_Type=RowStatus
_TmnxBmpStationRowStatus_Object=MibTableColumn
tmnxBmpStationRowStatus=_TmnxBmpStationRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,2),_TmnxBmpStationRowStatus_Type())
tmnxBmpStationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationRowStatus.setStatus(_B)
_TmnxBmpStationLastChanged_Type=TimeStamp
_TmnxBmpStationLastChanged_Object=MibTableColumn
tmnxBmpStationLastChanged=_TmnxBmpStationLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,3),_TmnxBmpStationLastChanged_Type())
tmnxBmpStationLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpStationLastChanged.setStatus(_B)
class _TmnxBmpStationAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxBmpStationAdminState_Type.__name__=_J
_TmnxBmpStationAdminState_Object=MibTableColumn
tmnxBmpStationAdminState=_TmnxBmpStationAdminState_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,4),_TmnxBmpStationAdminState_Type())
tmnxBmpStationAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationAdminState.setStatus(_B)
class _TmnxBmpStationDescr_Type(TItemDescription):defaultHexValue=''
_TmnxBmpStationDescr_Type.__name__=_d
_TmnxBmpStationDescr_Object=MibTableColumn
tmnxBmpStationDescr=_TmnxBmpStationDescr_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,5),_TmnxBmpStationDescr_Type())
tmnxBmpStationDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationDescr.setStatus(_B)
class _TmnxBmpStationConnectRetry_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxBmpStationConnectRetry_Type.__name__=_F
_TmnxBmpStationConnectRetry_Object=MibTableColumn
tmnxBmpStationConnectRetry=_TmnxBmpStationConnectRetry_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,7),_TmnxBmpStationConnectRetry_Type())
tmnxBmpStationConnectRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationConnectRetry.setStatus(_B)
if mibBuilder.loadTexts:tmnxBmpStationConnectRetry.setUnits(_K)
class _TmnxBmpStationInitialWaitTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_TmnxBmpStationInitialWaitTime_Type.__name__=_F
_TmnxBmpStationInitialWaitTime_Object=MibTableColumn
tmnxBmpStationInitialWaitTime=_TmnxBmpStationInitialWaitTime_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,8),_TmnxBmpStationInitialWaitTime_Type())
tmnxBmpStationInitialWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationInitialWaitTime.setStatus(_L)
if mibBuilder.loadTexts:tmnxBmpStationInitialWaitTime.setUnits(_O)
class _TmnxBmpStationSecondWaitTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,720))
_TmnxBmpStationSecondWaitTime_Type.__name__=_F
_TmnxBmpStationSecondWaitTime_Object=MibTableColumn
tmnxBmpStationSecondWaitTime=_TmnxBmpStationSecondWaitTime_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,9),_TmnxBmpStationSecondWaitTime_Type())
tmnxBmpStationSecondWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationSecondWaitTime.setStatus(_L)
if mibBuilder.loadTexts:tmnxBmpStationSecondWaitTime.setUnits(_O)
class _TmnxBmpStationMaxWaitTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,720))
_TmnxBmpStationMaxWaitTime_Type.__name__=_F
_TmnxBmpStationMaxWaitTime_Object=MibTableColumn
tmnxBmpStationMaxWaitTime=_TmnxBmpStationMaxWaitTime_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,10),_TmnxBmpStationMaxWaitTime_Type())
tmnxBmpStationMaxWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationMaxWaitTime.setStatus(_L)
if mibBuilder.loadTexts:tmnxBmpStationMaxWaitTime.setUnits(_O)
class _TmnxBmpStationErrorInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_TmnxBmpStationErrorInterval_Type.__name__=_F
_TmnxBmpStationErrorInterval_Object=MibTableColumn
tmnxBmpStationErrorInterval=_TmnxBmpStationErrorInterval_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,11),_TmnxBmpStationErrorInterval_Type())
tmnxBmpStationErrorInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationErrorInterval.setStatus(_L)
if mibBuilder.loadTexts:tmnxBmpStationErrorInterval.setUnits(_O)
class _TmnxBmpStationLocalIpAddrType_Type(InetAddressType):defaultValue=0
_TmnxBmpStationLocalIpAddrType_Type.__name__=_I
_TmnxBmpStationLocalIpAddrType_Object=MibTableColumn
tmnxBmpStationLocalIpAddrType=_TmnxBmpStationLocalIpAddrType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,12),_TmnxBmpStationLocalIpAddrType_Type())
tmnxBmpStationLocalIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationLocalIpAddrType.setStatus(_B)
class _TmnxBmpStationLocalIpAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxBmpStationLocalIpAddress_Type.__name__=_G
_TmnxBmpStationLocalIpAddress_Object=MibTableColumn
tmnxBmpStationLocalIpAddress=_TmnxBmpStationLocalIpAddress_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,13),_TmnxBmpStationLocalIpAddress_Type())
tmnxBmpStationLocalIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationLocalIpAddress.setStatus(_B)
class _TmnxBmpStationRemoteIpAddrType_Type(InetAddressType):defaultValue=0
_TmnxBmpStationRemoteIpAddrType_Type.__name__=_I
_TmnxBmpStationRemoteIpAddrType_Object=MibTableColumn
tmnxBmpStationRemoteIpAddrType=_TmnxBmpStationRemoteIpAddrType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,14),_TmnxBmpStationRemoteIpAddrType_Type())
tmnxBmpStationRemoteIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationRemoteIpAddrType.setStatus(_B)
class _TmnxBmpStationRemoteIpAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxBmpStationRemoteIpAddress_Type.__name__=_G
_TmnxBmpStationRemoteIpAddress_Object=MibTableColumn
tmnxBmpStationRemoteIpAddress=_TmnxBmpStationRemoteIpAddress_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,15),_TmnxBmpStationRemoteIpAddress_Type())
tmnxBmpStationRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationRemoteIpAddress.setStatus(_B)
class _TmnxBmpStationRemotePort_Type(InetPortNumber):defaultValue=0
_TmnxBmpStationRemotePort_Type.__name__=_N
_TmnxBmpStationRemotePort_Object=MibTableColumn
tmnxBmpStationRemotePort=_TmnxBmpStationRemotePort_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,16),_TmnxBmpStationRemotePort_Type())
tmnxBmpStationRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationRemotePort.setStatus(_B)
class _TmnxBmpStationMode_Type(TmnxBmpConnectionMode):defaultValue=1
_TmnxBmpStationMode_Type.__name__=_g
_TmnxBmpStationMode_Object=MibTableColumn
tmnxBmpStationMode=_TmnxBmpStationMode_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,17),_TmnxBmpStationMode_Type())
tmnxBmpStationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationMode.setStatus(_L)
class _TmnxBmpStationRouter_Type(TmnxVRtrID):defaultValue=1
_TmnxBmpStationRouter_Type.__name__=_e
_TmnxBmpStationRouter_Object=MibTableColumn
tmnxBmpStationRouter=_TmnxBmpStationRouter_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,18),_TmnxBmpStationRouter_Type())
tmnxBmpStationRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationRouter.setStatus(_B)
class _TmnxBmpStationInitiationMessage_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxBmpStationInitiationMessage_Type.__name__=_P
_TmnxBmpStationInitiationMessage_Object=MibTableColumn
tmnxBmpStationInitiationMessage=_TmnxBmpStationInitiationMessage_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,19),_TmnxBmpStationInitiationMessage_Type())
tmnxBmpStationInitiationMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationInitiationMessage.setStatus(_B)
class _TmnxBmpStationStatsReportIvl_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(15,65535))
_TmnxBmpStationStatsReportIvl_Type.__name__=_F
_TmnxBmpStationStatsReportIvl_Object=MibTableColumn
tmnxBmpStationStatsReportIvl=_TmnxBmpStationStatsReportIvl_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,20),_TmnxBmpStationStatsReportIvl_Type())
tmnxBmpStationStatsReportIvl.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationStatsReportIvl.setStatus(_B)
if mibBuilder.loadTexts:tmnxBmpStationStatsReportIvl.setUnits(_K)
class _TmnxBmpStationTcpKaAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxBmpStationTcpKaAdminState_Type.__name__=_J
_TmnxBmpStationTcpKaAdminState_Object=MibTableColumn
tmnxBmpStationTcpKaAdminState=_TmnxBmpStationTcpKaAdminState_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,21),_TmnxBmpStationTcpKaAdminState_Type())
tmnxBmpStationTcpKaAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationTcpKaAdminState.setStatus(_B)
class _TmnxBmpStationTcpKaIdle_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_TmnxBmpStationTcpKaIdle_Type.__name__=_F
_TmnxBmpStationTcpKaIdle_Object=MibTableColumn
tmnxBmpStationTcpKaIdle=_TmnxBmpStationTcpKaIdle_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,22),_TmnxBmpStationTcpKaIdle_Type())
tmnxBmpStationTcpKaIdle.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationTcpKaIdle.setStatus(_B)
if mibBuilder.loadTexts:tmnxBmpStationTcpKaIdle.setUnits(_K)
class _TmnxBmpStationTcpKaInterval_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_TmnxBmpStationTcpKaInterval_Type.__name__=_F
_TmnxBmpStationTcpKaInterval_Object=MibTableColumn
tmnxBmpStationTcpKaInterval=_TmnxBmpStationTcpKaInterval_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,23),_TmnxBmpStationTcpKaInterval_Type())
tmnxBmpStationTcpKaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationTcpKaInterval.setStatus(_B)
if mibBuilder.loadTexts:tmnxBmpStationTcpKaInterval.setUnits(_K)
class _TmnxBmpStationTcpKaCount_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_TmnxBmpStationTcpKaCount_Type.__name__=_F
_TmnxBmpStationTcpKaCount_Object=MibTableColumn
tmnxBmpStationTcpKaCount=_TmnxBmpStationTcpKaCount_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,24),_TmnxBmpStationTcpKaCount_Type())
tmnxBmpStationTcpKaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationTcpKaCount.setStatus(_B)
if mibBuilder.loadTexts:tmnxBmpStationTcpKaCount.setUnits(_K)
class _TmnxBmpStationRoutesReportIvl_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_TmnxBmpStationRoutesReportIvl_Type.__name__=_F
_TmnxBmpStationRoutesReportIvl_Object=MibTableColumn
tmnxBmpStationRoutesReportIvl=_TmnxBmpStationRoutesReportIvl_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,25),_TmnxBmpStationRoutesReportIvl_Type())
tmnxBmpStationRoutesReportIvl.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationRoutesReportIvl.setStatus('deprecated')
if mibBuilder.loadTexts:tmnxBmpStationRoutesReportIvl.setUnits(_K)
class _TmnxBmpStationReportLocalRoutes_Type(TruthValue):defaultValue=2
_TmnxBmpStationReportLocalRoutes_Type.__name__=_b
_TmnxBmpStationReportLocalRoutes_Object=MibTableColumn
tmnxBmpStationReportLocalRoutes=_TmnxBmpStationReportLocalRoutes_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,26),_TmnxBmpStationReportLocalRoutes_Type())
tmnxBmpStationReportLocalRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationReportLocalRoutes.setStatus(_B)
class _TmnxBmpStationFamily_Type(TmnxIpFamily):defaultBinValue='01'
_TmnxBmpStationFamily_Type.__name__=_c
_TmnxBmpStationFamily_Object=MibTableColumn
tmnxBmpStationFamily=_TmnxBmpStationFamily_Object((1,3,6,1,4,1,6527,3,1,2,108,2,1,1,27),_TmnxBmpStationFamily_Type())
tmnxBmpStationFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBmpStationFamily.setStatus(_B)
_TmnxBgpMonitorTable_Object=MibTable
tmnxBgpMonitorTable=_TmnxBgpMonitorTable_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2))
if mibBuilder.loadTexts:tmnxBgpMonitorTable.setStatus(_B)
_TmnxBgpMonitorEntry_Object=MibTableRow
tmnxBgpMonitorEntry=_TmnxBgpMonitorEntry_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1))
tmnxBgpMonitorEntry.setIndexNames((0,_A,_h),(0,_A,_i),(0,_A,_j),(0,_A,_k),(0,_A,_l))
if mibBuilder.loadTexts:tmnxBgpMonitorEntry.setStatus(_B)
_TmnxBgpMonitorType_Type=TmnxBgpMonitorType
_TmnxBgpMonitorType_Object=MibTableColumn
tmnxBgpMonitorType=_TmnxBgpMonitorType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,1),_TmnxBgpMonitorType_Type())
tmnxBgpMonitorType.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorType.setStatus(_B)
_TmnxBgpMonitorVRtrID_Type=TmnxVRtrID
_TmnxBgpMonitorVRtrID_Object=MibTableColumn
tmnxBgpMonitorVRtrID=_TmnxBgpMonitorVRtrID_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,2),_TmnxBgpMonitorVRtrID_Type())
tmnxBgpMonitorVRtrID.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorVRtrID.setStatus(_B)
_TmnxBgpMonitorPeerGroup_Type=TLNamedItemOrEmpty
_TmnxBgpMonitorPeerGroup_Object=MibTableColumn
tmnxBgpMonitorPeerGroup=_TmnxBgpMonitorPeerGroup_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,3),_TmnxBgpMonitorPeerGroup_Type())
tmnxBgpMonitorPeerGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorPeerGroup.setStatus(_B)
class _TmnxBgpMonitorPeerType_Type(InetAddressType):defaultValue=0
_TmnxBgpMonitorPeerType_Type.__name__=_I
_TmnxBgpMonitorPeerType_Object=MibTableColumn
tmnxBgpMonitorPeerType=_TmnxBgpMonitorPeerType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,4),_TmnxBgpMonitorPeerType_Type())
tmnxBgpMonitorPeerType.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorPeerType.setStatus(_B)
class _TmnxBgpMonitorPeer_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_TmnxBgpMonitorPeer_Type.__name__=_G
_TmnxBgpMonitorPeer_Object=MibTableColumn
tmnxBgpMonitorPeer=_TmnxBgpMonitorPeer_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,5),_TmnxBgpMonitorPeer_Type())
tmnxBgpMonitorPeer.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorPeer.setStatus(_B)
_TmnxBgpMonitorRowStatus_Type=RowStatus
_TmnxBgpMonitorRowStatus_Object=MibTableColumn
tmnxBgpMonitorRowStatus=_TmnxBgpMonitorRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,6),_TmnxBgpMonitorRowStatus_Type())
tmnxBgpMonitorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBgpMonitorRowStatus.setStatus(_B)
class _TmnxBgpMonitorAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxBgpMonitorAdminState_Type.__name__=_J
_TmnxBgpMonitorAdminState_Object=MibTableColumn
tmnxBgpMonitorAdminState=_TmnxBgpMonitorAdminState_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,7),_TmnxBgpMonitorAdminState_Type())
tmnxBgpMonitorAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBgpMonitorAdminState.setStatus(_B)
_TmnxBgpMonitorLastChanged_Type=TimeStamp
_TmnxBgpMonitorLastChanged_Object=MibTableColumn
tmnxBgpMonitorLastChanged=_TmnxBgpMonitorLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,8),_TmnxBgpMonitorLastChanged_Type())
tmnxBgpMonitorLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBgpMonitorLastChanged.setStatus(_B)
_TmnxBgpMonitorAllStations_Type=TruthValue
_TmnxBgpMonitorAllStations_Object=MibTableColumn
tmnxBgpMonitorAllStations=_TmnxBgpMonitorAllStations_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,9),_TmnxBgpMonitorAllStations_Type())
tmnxBgpMonitorAllStations.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBgpMonitorAllStations.setStatus(_B)
class _TmnxBgpMonitorRouteMonitoring_Type(TmnxBgpMonitorRouteMonitoring):defaultBinValue='0'
_TmnxBgpMonitorRouteMonitoring_Type.__name__=_m
_TmnxBgpMonitorRouteMonitoring_Object=MibTableColumn
tmnxBgpMonitorRouteMonitoring=_TmnxBgpMonitorRouteMonitoring_Object((1,3,6,1,4,1,6527,3,1,2,108,2,2,1,10),_TmnxBgpMonitorRouteMonitoring_Type())
tmnxBgpMonitorRouteMonitoring.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBgpMonitorRouteMonitoring.setStatus(_B)
_TmnxBgpMonitorStationTable_Object=MibTable
tmnxBgpMonitorStationTable=_TmnxBgpMonitorStationTable_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3))
if mibBuilder.loadTexts:tmnxBgpMonitorStationTable.setStatus(_B)
_TmnxBgpMonitorStationEntry_Object=MibTableRow
tmnxBgpMonitorStationEntry=_TmnxBgpMonitorStationEntry_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3,1))
tmnxBgpMonitorStationEntry.setIndexNames((0,_A,_n),(0,_A,_o),(0,_A,_p),(0,_A,_q),(0,_A,_r),(1,_A,_s))
if mibBuilder.loadTexts:tmnxBgpMonitorStationEntry.setStatus(_B)
_TmnxBgpMonitorStationType_Type=TmnxBgpMonitorType
_TmnxBgpMonitorStationType_Object=MibTableColumn
tmnxBgpMonitorStationType=_TmnxBgpMonitorStationType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3,1,1),_TmnxBgpMonitorStationType_Type())
tmnxBgpMonitorStationType.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorStationType.setStatus(_B)
_TmnxBgpMonitorStationVRtrID_Type=TmnxVRtrID
_TmnxBgpMonitorStationVRtrID_Object=MibTableColumn
tmnxBgpMonitorStationVRtrID=_TmnxBgpMonitorStationVRtrID_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3,1,2),_TmnxBgpMonitorStationVRtrID_Type())
tmnxBgpMonitorStationVRtrID.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorStationVRtrID.setStatus(_B)
_TmnxBgpMonitorStationPeerGroup_Type=TLNamedItemOrEmpty
_TmnxBgpMonitorStationPeerGroup_Object=MibTableColumn
tmnxBgpMonitorStationPeerGroup=_TmnxBgpMonitorStationPeerGroup_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3,1,3),_TmnxBgpMonitorStationPeerGroup_Type())
tmnxBgpMonitorStationPeerGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorStationPeerGroup.setStatus(_B)
class _TmnxBgpMonitorStationPeerType_Type(InetAddressType):defaultValue=0
_TmnxBgpMonitorStationPeerType_Type.__name__=_I
_TmnxBgpMonitorStationPeerType_Object=MibTableColumn
tmnxBgpMonitorStationPeerType=_TmnxBgpMonitorStationPeerType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3,1,4),_TmnxBgpMonitorStationPeerType_Type())
tmnxBgpMonitorStationPeerType.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorStationPeerType.setStatus(_B)
class _TmnxBgpMonitorStationPeer_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_TmnxBgpMonitorStationPeer_Type.__name__=_G
_TmnxBgpMonitorStationPeer_Object=MibTableColumn
tmnxBgpMonitorStationPeer=_TmnxBgpMonitorStationPeer_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3,1,5),_TmnxBgpMonitorStationPeer_Type())
tmnxBgpMonitorStationPeer.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorStationPeer.setStatus(_B)
_TmnxBgpMonitorStationName_Type=TNamedItem
_TmnxBgpMonitorStationName_Object=MibTableColumn
tmnxBgpMonitorStationName=_TmnxBgpMonitorStationName_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3,1,6),_TmnxBgpMonitorStationName_Type())
tmnxBgpMonitorStationName.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBgpMonitorStationName.setStatus(_B)
_TmnxBgpMonitorStationRowStatus_Type=RowStatus
_TmnxBgpMonitorStationRowStatus_Object=MibTableColumn
tmnxBgpMonitorStationRowStatus=_TmnxBgpMonitorStationRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,108,2,3,1,7),_TmnxBgpMonitorStationRowStatus_Type())
tmnxBgpMonitorStationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxBgpMonitorStationRowStatus.setStatus(_B)
_TmnxBmpSessionTable_Object=MibTable
tmnxBmpSessionTable=_TmnxBmpSessionTable_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4))
if mibBuilder.loadTexts:tmnxBmpSessionTable.setStatus(_B)
_TmnxBmpSessionEntry_Object=MibTableRow
tmnxBmpSessionEntry=_TmnxBmpSessionEntry_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1))
tmnxBmpSessionEntry.setIndexNames((0,_A,_t),(1,_A,_u))
if mibBuilder.loadTexts:tmnxBmpSessionEntry.setStatus(_B)
_TmnxBmpSessionVRtrID_Type=TmnxVRtrID
_TmnxBmpSessionVRtrID_Object=MibTableColumn
tmnxBmpSessionVRtrID=_TmnxBmpSessionVRtrID_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,1),_TmnxBmpSessionVRtrID_Type())
tmnxBmpSessionVRtrID.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBmpSessionVRtrID.setStatus(_B)
_TmnxBmpSessionStationName_Type=TNamedItem
_TmnxBmpSessionStationName_Object=MibTableColumn
tmnxBmpSessionStationName=_TmnxBmpSessionStationName_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,2),_TmnxBmpSessionStationName_Type())
tmnxBmpSessionStationName.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxBmpSessionStationName.setStatus(_B)
_TmnxBmpSessionConnectionState_Type=TmnxBmpSessionConnectionState
_TmnxBmpSessionConnectionState_Object=MibTableColumn
tmnxBmpSessionConnectionState=_TmnxBmpSessionConnectionState_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,3),_TmnxBmpSessionConnectionState_Type())
tmnxBmpSessionConnectionState.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionConnectionState.setStatus(_B)
_TmnxBmpSessionLocalAddrType_Type=InetAddressType
_TmnxBmpSessionLocalAddrType_Object=MibTableColumn
tmnxBmpSessionLocalAddrType=_TmnxBmpSessionLocalAddrType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,4),_TmnxBmpSessionLocalAddrType_Type())
tmnxBmpSessionLocalAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionLocalAddrType.setStatus(_B)
class _TmnxBmpSessionLocalAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_TmnxBmpSessionLocalAddr_Type.__name__=_G
_TmnxBmpSessionLocalAddr_Object=MibTableColumn
tmnxBmpSessionLocalAddr=_TmnxBmpSessionLocalAddr_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,5),_TmnxBmpSessionLocalAddr_Type())
tmnxBmpSessionLocalAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionLocalAddr.setStatus(_B)
_TmnxBmpSessionLocalAddrPort_Type=InetPortNumber
_TmnxBmpSessionLocalAddrPort_Object=MibTableColumn
tmnxBmpSessionLocalAddrPort=_TmnxBmpSessionLocalAddrPort_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,6),_TmnxBmpSessionLocalAddrPort_Type())
tmnxBmpSessionLocalAddrPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionLocalAddrPort.setStatus(_B)
_TmnxBmpSessionConnStateChanged_Type=TimeStamp
_TmnxBmpSessionConnStateChanged_Object=MibTableColumn
tmnxBmpSessionConnStateChanged=_TmnxBmpSessionConnStateChanged_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,7),_TmnxBmpSessionConnStateChanged_Type())
tmnxBmpSessionConnStateChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionConnStateChanged.setStatus(_B)
_TmnxBmpSessionLastMsgSent_Type=TimeStamp
_TmnxBmpSessionLastMsgSent_Object=MibTableColumn
tmnxBmpSessionLastMsgSent=_TmnxBmpSessionLastMsgSent_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,8),_TmnxBmpSessionLastMsgSent_Type())
tmnxBmpSessionLastMsgSent.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionLastMsgSent.setStatus(_B)
_TmnxBmpSessionBytesSent_Type=Counter64
_TmnxBmpSessionBytesSent_Object=MibTableColumn
tmnxBmpSessionBytesSent=_TmnxBmpSessionBytesSent_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,9),_TmnxBmpSessionBytesSent_Type())
tmnxBmpSessionBytesSent.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionBytesSent.setStatus(_B)
_TmnxBmpSessionRouteMonitorMsgs_Type=Counter64
_TmnxBmpSessionRouteMonitorMsgs_Object=MibTableColumn
tmnxBmpSessionRouteMonitorMsgs=_TmnxBmpSessionRouteMonitorMsgs_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,10),_TmnxBmpSessionRouteMonitorMsgs_Type())
tmnxBmpSessionRouteMonitorMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionRouteMonitorMsgs.setStatus(_B)
_TmnxBmpSessionStatisticsMsgs_Type=Counter64
_TmnxBmpSessionStatisticsMsgs_Object=MibTableColumn
tmnxBmpSessionStatisticsMsgs=_TmnxBmpSessionStatisticsMsgs_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,11),_TmnxBmpSessionStatisticsMsgs_Type())
tmnxBmpSessionStatisticsMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionStatisticsMsgs.setStatus(_B)
_TmnxBmpSessionPeerUpMsgs_Type=Counter64
_TmnxBmpSessionPeerUpMsgs_Object=MibTableColumn
tmnxBmpSessionPeerUpMsgs=_TmnxBmpSessionPeerUpMsgs_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,12),_TmnxBmpSessionPeerUpMsgs_Type())
tmnxBmpSessionPeerUpMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionPeerUpMsgs.setStatus(_B)
_TmnxBmpSessionPeerDownMsgs_Type=Counter64
_TmnxBmpSessionPeerDownMsgs_Object=MibTableColumn
tmnxBmpSessionPeerDownMsgs=_TmnxBmpSessionPeerDownMsgs_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,13),_TmnxBmpSessionPeerDownMsgs_Type())
tmnxBmpSessionPeerDownMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionPeerDownMsgs.setStatus(_B)
_TmnxBmpSessionInitiationMsgs_Type=Counter64
_TmnxBmpSessionInitiationMsgs_Object=MibTableColumn
tmnxBmpSessionInitiationMsgs=_TmnxBmpSessionInitiationMsgs_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,14),_TmnxBmpSessionInitiationMsgs_Type())
tmnxBmpSessionInitiationMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionInitiationMsgs.setStatus(_B)
_TmnxBmpSessionTerminationMsgs_Type=Counter64
_TmnxBmpSessionTerminationMsgs_Object=MibTableColumn
tmnxBmpSessionTerminationMsgs=_TmnxBmpSessionTerminationMsgs_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,15),_TmnxBmpSessionTerminationMsgs_Type())
tmnxBmpSessionTerminationMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionTerminationMsgs.setStatus(_B)
_TmnxBmpSessionRouteMirrorMsgs_Type=Counter64
_TmnxBmpSessionRouteMirrorMsgs_Object=MibTableColumn
tmnxBmpSessionRouteMirrorMsgs=_TmnxBmpSessionRouteMirrorMsgs_Object((1,3,6,1,4,1,6527,3,1,2,108,2,4,1,16),_TmnxBmpSessionRouteMirrorMsgs_Type())
tmnxBmpSessionRouteMirrorMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxBmpSessionRouteMirrorMsgs.setStatus(_B)
_TmnxBmpCollectorObjs_ObjectIdentity=ObjectIdentity
tmnxBmpCollectorObjs=_TmnxBmpCollectorObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,108,2,5))
class _TmnxBmpCollectorAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxBmpCollectorAdminState_Type.__name__=_J
_TmnxBmpCollectorAdminState_Object=MibScalar
tmnxBmpCollectorAdminState=_TmnxBmpCollectorAdminState_Object((1,3,6,1,4,1,6527,3,1,2,108,2,5,1),_TmnxBmpCollectorAdminState_Type())
tmnxBmpCollectorAdminState.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxBmpCollectorAdminState.setStatus(_B)
class _TmnxBmpCollectorIpv4AddrType_Type(InetAddressType):defaultValue=0
_TmnxBmpCollectorIpv4AddrType_Type.__name__=_I
_TmnxBmpCollectorIpv4AddrType_Object=MibScalar
tmnxBmpCollectorIpv4AddrType=_TmnxBmpCollectorIpv4AddrType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,5,2),_TmnxBmpCollectorIpv4AddrType_Type())
tmnxBmpCollectorIpv4AddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxBmpCollectorIpv4AddrType.setStatus(_B)
class _TmnxBmpCollectorIpv4Addr_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_TmnxBmpCollectorIpv4Addr_Type.__name__=_G
_TmnxBmpCollectorIpv4Addr_Object=MibScalar
tmnxBmpCollectorIpv4Addr=_TmnxBmpCollectorIpv4Addr_Object((1,3,6,1,4,1,6527,3,1,2,108,2,5,3),_TmnxBmpCollectorIpv4Addr_Type())
tmnxBmpCollectorIpv4Addr.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxBmpCollectorIpv4Addr.setStatus(_B)
class _TmnxBmpCollectorIpv4Port_Type(InetPortNumber):defaultValue=4210
_TmnxBmpCollectorIpv4Port_Type.__name__=_N
_TmnxBmpCollectorIpv4Port_Object=MibScalar
tmnxBmpCollectorIpv4Port=_TmnxBmpCollectorIpv4Port_Object((1,3,6,1,4,1,6527,3,1,2,108,2,5,4),_TmnxBmpCollectorIpv4Port_Type())
tmnxBmpCollectorIpv4Port.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxBmpCollectorIpv4Port.setStatus(_B)
class _TmnxBmpCollectorIpv6AddrType_Type(InetAddressType):defaultValue=0
_TmnxBmpCollectorIpv6AddrType_Type.__name__=_I
_TmnxBmpCollectorIpv6AddrType_Object=MibScalar
tmnxBmpCollectorIpv6AddrType=_TmnxBmpCollectorIpv6AddrType_Object((1,3,6,1,4,1,6527,3,1,2,108,2,5,5),_TmnxBmpCollectorIpv6AddrType_Type())
tmnxBmpCollectorIpv6AddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxBmpCollectorIpv6AddrType.setStatus(_B)
class _TmnxBmpCollectorIpv6Addr_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_TmnxBmpCollectorIpv6Addr_Type.__name__=_G
_TmnxBmpCollectorIpv6Addr_Object=MibScalar
tmnxBmpCollectorIpv6Addr=_TmnxBmpCollectorIpv6Addr_Object((1,3,6,1,4,1,6527,3,1,2,108,2,5,6),_TmnxBmpCollectorIpv6Addr_Type())
tmnxBmpCollectorIpv6Addr.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxBmpCollectorIpv6Addr.setStatus(_B)
class _TmnxBmpCollectorIpv6Port_Type(InetPortNumber):defaultValue=4210
_TmnxBmpCollectorIpv6Port_Type.__name__=_N
_TmnxBmpCollectorIpv6Port_Object=MibScalar
tmnxBmpCollectorIpv6Port=_TmnxBmpCollectorIpv6Port_Object((1,3,6,1,4,1,6527,3,1,2,108,2,5,7),_TmnxBmpCollectorIpv6Port_Type())
tmnxBmpCollectorIpv6Port.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxBmpCollectorIpv6Port.setStatus(_B)
_TmnxBmpNotifObjects_ObjectIdentity=ObjectIdentity
tmnxBmpNotifObjects=_TmnxBmpNotifObjects_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,108,100))
_TmnxBmpSessionChangeVRtrID_Type=TmnxVRtrID
_TmnxBmpSessionChangeVRtrID_Object=MibScalar
tmnxBmpSessionChangeVRtrID=_TmnxBmpSessionChangeVRtrID_Object((1,3,6,1,4,1,6527,3,1,2,108,100,1),_TmnxBmpSessionChangeVRtrID_Type())
tmnxBmpSessionChangeVRtrID.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxBmpSessionChangeVRtrID.setStatus(_B)
_TmnxBmpSessionChangeStationName_Type=TNamedItem
_TmnxBmpSessionChangeStationName_Object=MibScalar
tmnxBmpSessionChangeStationName=_TmnxBmpSessionChangeStationName_Object((1,3,6,1,4,1,6527,3,1,2,108,100,2),_TmnxBmpSessionChangeStationName_Type())
tmnxBmpSessionChangeStationName.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxBmpSessionChangeStationName.setStatus(_B)
_TmnxBmpSessionChangeOldState_Type=TmnxBmpSessionConnectionState
_TmnxBmpSessionChangeOldState_Object=MibScalar
tmnxBmpSessionChangeOldState=_TmnxBmpSessionChangeOldState_Object((1,3,6,1,4,1,6527,3,1,2,108,100,3),_TmnxBmpSessionChangeOldState_Type())
tmnxBmpSessionChangeOldState.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxBmpSessionChangeOldState.setStatus(_B)
_TmnxBmpSessionChangeNewState_Type=TmnxBmpSessionConnectionState
_TmnxBmpSessionChangeNewState_Object=MibScalar
tmnxBmpSessionChangeNewState=_TmnxBmpSessionChangeNewState_Object((1,3,6,1,4,1,6527,3,1,2,108,100,4),_TmnxBmpSessionChangeNewState_Type())
tmnxBmpSessionChangeNewState.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxBmpSessionChangeNewState.setStatus(_B)
class _TmnxBmpSessionChangeReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxBmpSessionChangeReason_Type.__name__=_P
_TmnxBmpSessionChangeReason_Object=MibScalar
tmnxBmpSessionChangeReason=_TmnxBmpSessionChangeReason_Object((1,3,6,1,4,1,6527,3,1,2,108,100,5),_TmnxBmpSessionChangeReason_Type())
tmnxBmpSessionChangeReason.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxBmpSessionChangeReason.setStatus(_B)
_TmnxBmpNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxBmpNotifyPrefix=_TmnxBmpNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,108))
_TmnxBmpNotifications_ObjectIdentity=ObjectIdentity
tmnxBmpNotifications=_TmnxBmpNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,108,0))
tmnxBmpConfigV15Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,108,2,1,1))
tmnxBmpConfigV15Group.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_U),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:tmnxBmpConfigV15Group.setStatus(_B)
tmnxBmpConfigV16Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,108,2,2,1))
tmnxBmpConfigV16Group.setObjects(*((_A,_V),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:tmnxBmpConfigV16Group.setStatus(_B)
tmnxBmpObsoletedConfigV16Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,108,2,2,2))
tmnxBmpObsoletedConfigV16Group.setObjects(*((_A,_U),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_V)))
if mibBuilder.loadTexts:tmnxBmpObsoletedConfigV16Group.setStatus(_B)
tmnxBmpNotificationObjs=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,108,2,2,3))
tmnxBmpNotificationObjs.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:tmnxBmpNotificationObjs.setStatus(_B)
tmnxBmpConfigV19v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,108,2,3,1))
tmnxBmpConfigV19v0Group.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:tmnxBmpConfigV19v0Group.setStatus(_B)
tmnxBmpSessionStatusChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,108,0,1))
tmnxBmpSessionStatusChange.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:tmnxBmpSessionStatusChange.setStatus(_B)
tmnxBmpNotificationV16Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,108,2,2,4))
tmnxBmpNotificationV16Group.setObjects((_A,_Ai))
if mibBuilder.loadTexts:tmnxBmpNotificationV16Group.setStatus(_B)
tmnxBmpComplianceV15v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,108,1,1))
tmnxBmpComplianceV15v0.setObjects((_A,_Aj))
if mibBuilder.loadTexts:tmnxBmpComplianceV15v0.setStatus(_B)
tmnxBmpComplianceV16v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,108,1,2))
tmnxBmpComplianceV16v0.setObjects(*((_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:tmnxBmpComplianceV16v0.setStatus(_B)
tmnxBmpComplianceV19v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,108,1,3))
tmnxBmpComplianceV19v0.setObjects((_A,_An))
if mibBuilder.loadTexts:tmnxBmpComplianceV19v0.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_g:TmnxBmpConnectionMode,'TmnxBgpMonitorType':TmnxBgpMonitorType,_m:TmnxBgpMonitorRouteMonitoring,'TmnxBmpSessionConnectionState':TmnxBmpSessionConnectionState,'timetraBmpMIBModule':timetraBmpMIBModule,'tmnxBmpConformance':tmnxBmpConformance,'tmnxBmpCompliances':tmnxBmpCompliances,'tmnxBmpComplianceV15v0':tmnxBmpComplianceV15v0,'tmnxBmpComplianceV16v0':tmnxBmpComplianceV16v0,'tmnxBmpComplianceV19v0':tmnxBmpComplianceV19v0,'tmnxBmpGroups':tmnxBmpGroups,'tmnxBmpV15v0Groups':tmnxBmpV15v0Groups,_Aj:tmnxBmpConfigV15Group,'tmnxBmpV16v0Groups':tmnxBmpV16v0Groups,_Ak:tmnxBmpConfigV16Group,'tmnxBmpObsoletedConfigV16Group':tmnxBmpObsoletedConfigV16Group,_Al:tmnxBmpNotificationObjs,_Am:tmnxBmpNotificationV16Group,'tmnxBmpV19v0Groups':tmnxBmpV19v0Groups,_An:tmnxBmpConfigV19v0Group,'tmnxBmpObjs':tmnxBmpObjs,'tmnxBmpParameterObjs':tmnxBmpParameterObjs,_v:tmnxBmpAdminState,_w:tmnxBmpStationTableLastCh,_AA:tmnxBgpMonitorTableLastCh,'tmnxBmpStationObjs':tmnxBmpStationObjs,'tmnxBmpStationTable':tmnxBmpStationTable,'tmnxBmpStationEntry':tmnxBmpStationEntry,_f:tmnxBmpStationName,_x:tmnxBmpStationRowStatus,_y:tmnxBmpStationLastChanged,_z:tmnxBmpStationAdminState,_A0:tmnxBmpStationDescr,_A1:tmnxBmpStationConnectRetry,_Q:tmnxBmpStationInitialWaitTime,_R:tmnxBmpStationSecondWaitTime,_S:tmnxBmpStationMaxWaitTime,_T:tmnxBmpStationErrorInterval,_A2:tmnxBmpStationLocalIpAddrType,_A3:tmnxBmpStationLocalIpAddress,_A4:tmnxBmpStationRemoteIpAddrType,_A5:tmnxBmpStationRemoteIpAddress,_A6:tmnxBmpStationRemotePort,_U:tmnxBmpStationMode,_A7:tmnxBmpStationRouter,_A8:tmnxBmpStationInitiationMessage,_A9:tmnxBmpStationStatsReportIvl,_AH:tmnxBmpStationTcpKaAdminState,_AI:tmnxBmpStationTcpKaIdle,_AJ:tmnxBmpStationTcpKaInterval,_AK:tmnxBmpStationTcpKaCount,_V:tmnxBmpStationRoutesReportIvl,_AZ:tmnxBmpStationReportLocalRoutes,_Aa:tmnxBmpStationFamily,'tmnxBgpMonitorTable':tmnxBgpMonitorTable,'tmnxBgpMonitorEntry':tmnxBgpMonitorEntry,_h:tmnxBgpMonitorType,_i:tmnxBgpMonitorVRtrID,_j:tmnxBgpMonitorPeerGroup,_k:tmnxBgpMonitorPeerType,_l:tmnxBgpMonitorPeer,_AB:tmnxBgpMonitorRowStatus,_AC:tmnxBgpMonitorAdminState,_AD:tmnxBgpMonitorLastChanged,_AE:tmnxBgpMonitorAllStations,_AF:tmnxBgpMonitorRouteMonitoring,'tmnxBgpMonitorStationTable':tmnxBgpMonitorStationTable,'tmnxBgpMonitorStationEntry':tmnxBgpMonitorStationEntry,_n:tmnxBgpMonitorStationType,_o:tmnxBgpMonitorStationVRtrID,_p:tmnxBgpMonitorStationPeerGroup,_q:tmnxBgpMonitorStationPeerType,_r:tmnxBgpMonitorStationPeer,_s:tmnxBgpMonitorStationName,_AG:tmnxBgpMonitorStationRowStatus,'tmnxBmpSessionTable':tmnxBmpSessionTable,'tmnxBmpSessionEntry':tmnxBmpSessionEntry,_t:tmnxBmpSessionVRtrID,_u:tmnxBmpSessionStationName,_AL:tmnxBmpSessionConnectionState,_AM:tmnxBmpSessionLocalAddrType,_AN:tmnxBmpSessionLocalAddr,_AO:tmnxBmpSessionLocalAddrPort,_AP:tmnxBmpSessionConnStateChanged,_AQ:tmnxBmpSessionLastMsgSent,_AR:tmnxBmpSessionBytesSent,_AS:tmnxBmpSessionRouteMonitorMsgs,_AT:tmnxBmpSessionStatisticsMsgs,_AU:tmnxBmpSessionPeerUpMsgs,_AV:tmnxBmpSessionPeerDownMsgs,_AW:tmnxBmpSessionInitiationMsgs,_AX:tmnxBmpSessionTerminationMsgs,_AY:tmnxBmpSessionRouteMirrorMsgs,'tmnxBmpCollectorObjs':tmnxBmpCollectorObjs,_Ab:tmnxBmpCollectorAdminState,_Ac:tmnxBmpCollectorIpv4AddrType,_Ad:tmnxBmpCollectorIpv4Addr,_Ae:tmnxBmpCollectorIpv4Port,_Af:tmnxBmpCollectorIpv6AddrType,_Ag:tmnxBmpCollectorIpv6Addr,_Ah:tmnxBmpCollectorIpv6Port,'tmnxBmpNotifObjects':tmnxBmpNotifObjects,_W:tmnxBmpSessionChangeVRtrID,_X:tmnxBmpSessionChangeStationName,_Y:tmnxBmpSessionChangeOldState,_Z:tmnxBmpSessionChangeNewState,_a:tmnxBmpSessionChangeReason,'tmnxBmpNotifyPrefix':tmnxBmpNotifyPrefix,'tmnxBmpNotifications':tmnxBmpNotifications,_Ai:tmnxBmpSessionStatusChange})