_Aq='ciscoWdsInfoNotifGroup'
_Ap='ciscoWdsInfoRoamStatisticsGroup'
_Ao='ciscoWdsInfoMobilityGroup'
_An='ciscoWdsInfoStatisticsGroup'
_Am='ciscoWdsInfoNetworkManagerGroup'
_Al='ciscoWdsInfoMobileNodeGroup'
_Ak='ciscoWdsInfoAccessPointGroup'
_Aj='ciscoWdsInfoMacAuthCacheGroup'
_Ai='cwdsiHsrpStateChange'
_Ah='cwdsiLcpStatusChange'
_Ag='cwdsiRoamMblGrpStatsFiveMinutes'
_Af='cwdsiRoamMblGrpStatsOneMinute'
_Ae='cwdsiRoamMblGrpStatsFiveSeconds'
_Ad='cwdsiRoamMblGrpStatsFastSecured'
_Ac='cwdsiRoamMblGrpStatsAuthAaa'
_Ab='cwdsiRoamMblGrpStatsNoAuthAaa'
_Aa='cwdsiRoamMblGrpStatsTotal'
_AZ='cwdsiRoamStatsAvgFiveMinutes'
_AY='cwdsiRoamStatsAvgOneMinute'
_AX='cwdsiRoamStatsAvgFiveSeconds'
_AW='cwdsiRoamStatsStartTime'
_AV='cwdsiMobilityGrpMnNum'
_AU='cwdsiMobilityGrpFlags'
_AT='cwdsiMobilityGrpTunnelMtu'
_AS='cwdsiMobilityGrpTunnelAddr'
_AR='cwdsiMobilityGrpTunnelAddrType'
_AQ='cwdsiWdsHsrpVirtualAddr'
_AP='cwdsiWdsHsrpVirtualAddrType'
_AO='cwdsiWdsAddr'
_AN='cwdsiWdsAddrType'
_AM='cwdsiCsMgmtAddr'
_AL='cwdsiCsMgmtAddrType'
_AK='cwdsiRnMismatchCount'
_AJ='cwdsiMicFailureCount'
_AI='cwdsiKscFailureCount'
_AH='cwdsiMscMismatchCount'
_AG='cwdsiRoamsFastSecuredCount'
_AF='cwdsiRoamsWithFullAaaAuthCount'
_AE='cwdsiRoamsWithoutAaaAuthCount'
_AD='cwdsiMacSpoofingBlockCount'
_AC='cwdsiAaaAuthFailureCount'
_AB='cwdsiAaaAuthSuccessCount'
_AA='cwdsiAaaAuthAttemptCount'
_A9='cwdsiMnNum'
_A8='cwdsiApNum'
_A7='cwdsiWnmDiscontinuityTime'
_A6='cwdsiWnmDropRxMsgCount'
_A5='cwdsiWnmRxMsgCount'
_A4='cwdsiWnmIndicatedMsgCount'
_A3='cwdsiWnmDropUmdTxMsgCount'
_A2='cwdsiWnmDropMicTxMsgCount'
_A1='cwdsiWnmWaitingAckMsgCount'
_A0='cwdsiWnmRetryTxMsgCount'
_z='cwdsiWnmSentMsgCount'
_y='cwdsiWnmReqMsgCount'
_x='cwdsiWnmClientTracking'
_w='cwdsiWnmLinkStatus'
_v='cwdsiWnmState'
_u='cwdsiMnLifetime'
_t='cwdsiMnUptime'
_s='cwdsiMnAuthType'
_r='cwdsiMnKeyMgmt'
_q='cwdsiMnSsid'
_p='cwdsiMnVlan'
_o='cwdsiMnBssid'
_n='cwdsiMnState'
_m='cwdsiMnMobilityNetworkId'
_l='cwdsiMnApAddrType'
_k='cwdsiMnApAddr'
_j='cwdsiMnApMacAddr'
_i='cwdsiMnAddrType'
_h='cwdsiMnAddr'
_g='cwdsiApNeighborPortName'
_f='cwdsiApNeighborName'
_e='cwdsiApNeighborAddr'
_d='cwdsiApNeighborAddrType'
_c='cwdsiApLifeTime'
_b='cwdsiApState'
_a='cwdsiApName'
_Z='cwdsiApAddrType'
_Y='cwdsiApAddr'
_X='cwdsiMacAuthCacheAge'
_W='cwdsiRoamMblGrpStatsNetworkId'
_V='cwdsiMobilityGrpNetworkId'
_U='mobile-nodes'
_T='cwdsiWnmAddr'
_S='cwdsiWnmAddrType'
_R='cwdsiMnMacAddr'
_Q='seconds'
_P='cwdsiApMacAddr'
_O='cwdsiMacAuthCacheMacAddr'
_N='initial'
_M='unknown'
_L='disabled'
_K='active'
_J='cwdsiHsrpState'
_I='cwdsiLcpStatus'
_H='Unsigned32'
_G='Integer32'
_F='InetAddress'
_E='roams-per-second'
_D='not-accessible'
_C='read-only'
_B='CISCO-WDS-INFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CDot11IfVlanIdOrZero,=mibBuilder.importSymbols('CISCO-DOT11-IF-MIB','CDot11IfVlanIdOrZero')
CDot11SecAuthKeyMgmtType,CDot11SsidString=mibBuilder.importSymbols('CISCO-DOT11-SSID-SECURITY-MIB','CDot11SecAuthKeyMgmtType','CDot11SsidString')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp')
ciscoWdsInfoMIB=ModuleIdentity((1,3,6,1,4,1,9,9,509))
if mibBuilder.loadTexts:ciscoWdsInfoMIB.setRevisions(('2005-09-15 00:00',))
class CWdsClientTrackingStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('inactive',2),(_L,3)))
class CWdsDeviceAuthType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('open',0),('shared',1),('leap',2),('eap',3),('mac',4),('macOrEap',5),('macOrLeap',6),('eapOptional',7)))
class CWdsDeviceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),(_N,2),('authInProgress',3),('authFailed',4),('authenticated',5),('securityKeysSetup',6),('registered',7),('detached',8)))
_CiscoWdsInfoMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWdsInfoMIBNotifs=_CiscoWdsInfoMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,509,0))
_CiscoWdsInfoMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWdsInfoMIBObjects=_CiscoWdsInfoMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,509,1))
_CiscoWdsInfoMacAuthCache_ObjectIdentity=ObjectIdentity
ciscoWdsInfoMacAuthCache=_CiscoWdsInfoMacAuthCache_ObjectIdentity((1,3,6,1,4,1,9,9,509,1,1))
_CwdsiMacAuthCacheTable_Object=MibTable
cwdsiMacAuthCacheTable=_CwdsiMacAuthCacheTable_Object((1,3,6,1,4,1,9,9,509,1,1,1))
if mibBuilder.loadTexts:cwdsiMacAuthCacheTable.setStatus(_A)
_CwdsiMacAuthCacheEntry_Object=MibTableRow
cwdsiMacAuthCacheEntry=_CwdsiMacAuthCacheEntry_Object((1,3,6,1,4,1,9,9,509,1,1,1,1))
cwdsiMacAuthCacheEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cwdsiMacAuthCacheEntry.setStatus(_A)
_CwdsiMacAuthCacheMacAddr_Type=MacAddress
_CwdsiMacAuthCacheMacAddr_Object=MibTableColumn
cwdsiMacAuthCacheMacAddr=_CwdsiMacAuthCacheMacAddr_Object((1,3,6,1,4,1,9,9,509,1,1,1,1,1),_CwdsiMacAuthCacheMacAddr_Type())
cwdsiMacAuthCacheMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdsiMacAuthCacheMacAddr.setStatus(_A)
_CwdsiMacAuthCacheAge_Type=Unsigned32
_CwdsiMacAuthCacheAge_Object=MibTableColumn
cwdsiMacAuthCacheAge=_CwdsiMacAuthCacheAge_Object((1,3,6,1,4,1,9,9,509,1,1,1,1,2),_CwdsiMacAuthCacheAge_Type())
cwdsiMacAuthCacheAge.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMacAuthCacheAge.setStatus(_A)
if mibBuilder.loadTexts:cwdsiMacAuthCacheAge.setUnits('minutes')
_CiscoWdsInfoAccessPoint_ObjectIdentity=ObjectIdentity
ciscoWdsInfoAccessPoint=_CiscoWdsInfoAccessPoint_ObjectIdentity((1,3,6,1,4,1,9,9,509,1,2))
_CwdsiApTable_Object=MibTable
cwdsiApTable=_CwdsiApTable_Object((1,3,6,1,4,1,9,9,509,1,2,1))
if mibBuilder.loadTexts:cwdsiApTable.setStatus(_A)
_CwdsiApEntry_Object=MibTableRow
cwdsiApEntry=_CwdsiApEntry_Object((1,3,6,1,4,1,9,9,509,1,2,1,1))
cwdsiApEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:cwdsiApEntry.setStatus(_A)
_CwdsiApMacAddr_Type=MacAddress
_CwdsiApMacAddr_Object=MibTableColumn
cwdsiApMacAddr=_CwdsiApMacAddr_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,1),_CwdsiApMacAddr_Type())
cwdsiApMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdsiApMacAddr.setStatus(_A)
_CwdsiApAddrType_Type=InetAddressType
_CwdsiApAddrType_Object=MibTableColumn
cwdsiApAddrType=_CwdsiApAddrType_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,2),_CwdsiApAddrType_Type())
cwdsiApAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApAddrType.setStatus(_A)
_CwdsiApAddr_Type=InetAddress
_CwdsiApAddr_Object=MibTableColumn
cwdsiApAddr=_CwdsiApAddr_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,3),_CwdsiApAddr_Type())
cwdsiApAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApAddr.setStatus(_A)
_CwdsiApName_Type=SnmpAdminString
_CwdsiApName_Object=MibTableColumn
cwdsiApName=_CwdsiApName_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,4),_CwdsiApName_Type())
cwdsiApName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApName.setStatus(_A)
_CwdsiApState_Type=CWdsDeviceState
_CwdsiApState_Object=MibTableColumn
cwdsiApState=_CwdsiApState_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,5),_CwdsiApState_Type())
cwdsiApState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApState.setStatus(_A)
_CwdsiApLifeTime_Type=Unsigned32
_CwdsiApLifeTime_Object=MibTableColumn
cwdsiApLifeTime=_CwdsiApLifeTime_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,6),_CwdsiApLifeTime_Type())
cwdsiApLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApLifeTime.setStatus(_A)
if mibBuilder.loadTexts:cwdsiApLifeTime.setUnits(_Q)
_CwdsiApNeighborAddrType_Type=InetAddressType
_CwdsiApNeighborAddrType_Object=MibTableColumn
cwdsiApNeighborAddrType=_CwdsiApNeighborAddrType_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,7),_CwdsiApNeighborAddrType_Type())
cwdsiApNeighborAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApNeighborAddrType.setStatus(_A)
_CwdsiApNeighborAddr_Type=InetAddress
_CwdsiApNeighborAddr_Object=MibTableColumn
cwdsiApNeighborAddr=_CwdsiApNeighborAddr_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,8),_CwdsiApNeighborAddr_Type())
cwdsiApNeighborAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApNeighborAddr.setStatus(_A)
_CwdsiApNeighborName_Type=SnmpAdminString
_CwdsiApNeighborName_Object=MibTableColumn
cwdsiApNeighborName=_CwdsiApNeighborName_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,9),_CwdsiApNeighborName_Type())
cwdsiApNeighborName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApNeighborName.setStatus(_A)
_CwdsiApNeighborPortName_Type=SnmpAdminString
_CwdsiApNeighborPortName_Object=MibTableColumn
cwdsiApNeighborPortName=_CwdsiApNeighborPortName_Object((1,3,6,1,4,1,9,9,509,1,2,1,1,10),_CwdsiApNeighborPortName_Type())
cwdsiApNeighborPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApNeighborPortName.setStatus(_A)
_CiscoWdsInfoMobileNode_ObjectIdentity=ObjectIdentity
ciscoWdsInfoMobileNode=_CiscoWdsInfoMobileNode_ObjectIdentity((1,3,6,1,4,1,9,9,509,1,3))
_CwdsiMnTable_Object=MibTable
cwdsiMnTable=_CwdsiMnTable_Object((1,3,6,1,4,1,9,9,509,1,3,1))
if mibBuilder.loadTexts:cwdsiMnTable.setStatus(_A)
_CwdsiMnEntry_Object=MibTableRow
cwdsiMnEntry=_CwdsiMnEntry_Object((1,3,6,1,4,1,9,9,509,1,3,1,1))
cwdsiMnEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:cwdsiMnEntry.setStatus(_A)
_CwdsiMnMacAddr_Type=MacAddress
_CwdsiMnMacAddr_Object=MibTableColumn
cwdsiMnMacAddr=_CwdsiMnMacAddr_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,1),_CwdsiMnMacAddr_Type())
cwdsiMnMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdsiMnMacAddr.setStatus(_A)
_CwdsiMnAddrType_Type=InetAddressType
_CwdsiMnAddrType_Object=MibTableColumn
cwdsiMnAddrType=_CwdsiMnAddrType_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,2),_CwdsiMnAddrType_Type())
cwdsiMnAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnAddrType.setStatus(_A)
_CwdsiMnAddr_Type=InetAddress
_CwdsiMnAddr_Object=MibTableColumn
cwdsiMnAddr=_CwdsiMnAddr_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,3),_CwdsiMnAddr_Type())
cwdsiMnAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnAddr.setStatus(_A)
_CwdsiMnApMacAddr_Type=MacAddress
_CwdsiMnApMacAddr_Object=MibTableColumn
cwdsiMnApMacAddr=_CwdsiMnApMacAddr_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,4),_CwdsiMnApMacAddr_Type())
cwdsiMnApMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnApMacAddr.setStatus(_A)
_CwdsiMnApAddrType_Type=InetAddressType
_CwdsiMnApAddrType_Object=MibTableColumn
cwdsiMnApAddrType=_CwdsiMnApAddrType_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,5),_CwdsiMnApAddrType_Type())
cwdsiMnApAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnApAddrType.setStatus(_A)
_CwdsiMnApAddr_Type=InetAddress
_CwdsiMnApAddr_Object=MibTableColumn
cwdsiMnApAddr=_CwdsiMnApAddr_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,6),_CwdsiMnApAddr_Type())
cwdsiMnApAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnApAddr.setStatus(_A)
class _CwdsiMnMobilityNetworkId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_CwdsiMnMobilityNetworkId_Type.__name__=_H
_CwdsiMnMobilityNetworkId_Object=MibTableColumn
cwdsiMnMobilityNetworkId=_CwdsiMnMobilityNetworkId_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,7),_CwdsiMnMobilityNetworkId_Type())
cwdsiMnMobilityNetworkId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnMobilityNetworkId.setStatus(_A)
_CwdsiMnState_Type=CWdsDeviceState
_CwdsiMnState_Object=MibTableColumn
cwdsiMnState=_CwdsiMnState_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,8),_CwdsiMnState_Type())
cwdsiMnState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnState.setStatus(_A)
_CwdsiMnSsid_Type=CDot11SsidString
_CwdsiMnSsid_Object=MibTableColumn
cwdsiMnSsid=_CwdsiMnSsid_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,9),_CwdsiMnSsid_Type())
cwdsiMnSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnSsid.setStatus(_A)
_CwdsiMnBssid_Type=MacAddress
_CwdsiMnBssid_Object=MibTableColumn
cwdsiMnBssid=_CwdsiMnBssid_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,10),_CwdsiMnBssid_Type())
cwdsiMnBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnBssid.setStatus(_A)
_CwdsiMnVlan_Type=CDot11IfVlanIdOrZero
_CwdsiMnVlan_Object=MibTableColumn
cwdsiMnVlan=_CwdsiMnVlan_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,11),_CwdsiMnVlan_Type())
cwdsiMnVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnVlan.setStatus(_A)
_CwdsiMnKeyMgmt_Type=CDot11SecAuthKeyMgmtType
_CwdsiMnKeyMgmt_Object=MibTableColumn
cwdsiMnKeyMgmt=_CwdsiMnKeyMgmt_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,12),_CwdsiMnKeyMgmt_Type())
cwdsiMnKeyMgmt.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnKeyMgmt.setStatus(_A)
_CwdsiMnAuthType_Type=CWdsDeviceAuthType
_CwdsiMnAuthType_Object=MibTableColumn
cwdsiMnAuthType=_CwdsiMnAuthType_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,13),_CwdsiMnAuthType_Type())
cwdsiMnAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnAuthType.setStatus(_A)
_CwdsiMnUptime_Type=TimeStamp
_CwdsiMnUptime_Object=MibTableColumn
cwdsiMnUptime=_CwdsiMnUptime_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,14),_CwdsiMnUptime_Type())
cwdsiMnUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnUptime.setStatus(_A)
_CwdsiMnLifetime_Type=Unsigned32
_CwdsiMnLifetime_Object=MibTableColumn
cwdsiMnLifetime=_CwdsiMnLifetime_Object((1,3,6,1,4,1,9,9,509,1,3,1,1,15),_CwdsiMnLifetime_Type())
cwdsiMnLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnLifetime.setStatus(_A)
if mibBuilder.loadTexts:cwdsiMnLifetime.setUnits(_Q)
_CiscoWdsInfoNetworkManager_ObjectIdentity=ObjectIdentity
ciscoWdsInfoNetworkManager=_CiscoWdsInfoNetworkManager_ObjectIdentity((1,3,6,1,4,1,9,9,509,1,4))
_CwdsiWnmTable_Object=MibTable
cwdsiWnmTable=_CwdsiWnmTable_Object((1,3,6,1,4,1,9,9,509,1,4,1))
if mibBuilder.loadTexts:cwdsiWnmTable.setStatus(_A)
_CwdsiWnmEntry_Object=MibTableRow
cwdsiWnmEntry=_CwdsiWnmEntry_Object((1,3,6,1,4,1,9,9,509,1,4,1,1))
cwdsiWnmEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cwdsiWnmEntry.setStatus(_A)
_CwdsiWnmAddrType_Type=InetAddressType
_CwdsiWnmAddrType_Object=MibTableColumn
cwdsiWnmAddrType=_CwdsiWnmAddrType_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,1),_CwdsiWnmAddrType_Type())
cwdsiWnmAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdsiWnmAddrType.setStatus(_A)
class _CwdsiWnmAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CwdsiWnmAddr_Type.__name__=_F
_CwdsiWnmAddr_Object=MibTableColumn
cwdsiWnmAddr=_CwdsiWnmAddr_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,2),_CwdsiWnmAddr_Type())
cwdsiWnmAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdsiWnmAddr.setStatus(_A)
_CwdsiWnmState_Type=CWdsDeviceState
_CwdsiWnmState_Object=MibTableColumn
cwdsiWnmState=_CwdsiWnmState_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,3),_CwdsiWnmState_Type())
cwdsiWnmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmState.setStatus(_A)
class _CwdsiWnmLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CwdsiWnmLinkStatus_Type.__name__=_G
_CwdsiWnmLinkStatus_Object=MibTableColumn
cwdsiWnmLinkStatus=_CwdsiWnmLinkStatus_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,4),_CwdsiWnmLinkStatus_Type())
cwdsiWnmLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmLinkStatus.setStatus(_A)
_CwdsiWnmClientTracking_Type=CWdsClientTrackingStatus
_CwdsiWnmClientTracking_Object=MibTableColumn
cwdsiWnmClientTracking=_CwdsiWnmClientTracking_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,5),_CwdsiWnmClientTracking_Type())
cwdsiWnmClientTracking.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmClientTracking.setStatus(_A)
_CwdsiWnmReqMsgCount_Type=Counter32
_CwdsiWnmReqMsgCount_Object=MibTableColumn
cwdsiWnmReqMsgCount=_CwdsiWnmReqMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,6),_CwdsiWnmReqMsgCount_Type())
cwdsiWnmReqMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmReqMsgCount.setStatus(_A)
_CwdsiWnmSentMsgCount_Type=Counter32
_CwdsiWnmSentMsgCount_Object=MibTableColumn
cwdsiWnmSentMsgCount=_CwdsiWnmSentMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,7),_CwdsiWnmSentMsgCount_Type())
cwdsiWnmSentMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmSentMsgCount.setStatus(_A)
_CwdsiWnmRetryTxMsgCount_Type=Counter32
_CwdsiWnmRetryTxMsgCount_Object=MibTableColumn
cwdsiWnmRetryTxMsgCount=_CwdsiWnmRetryTxMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,8),_CwdsiWnmRetryTxMsgCount_Type())
cwdsiWnmRetryTxMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmRetryTxMsgCount.setStatus(_A)
_CwdsiWnmWaitingAckMsgCount_Type=Counter32
_CwdsiWnmWaitingAckMsgCount_Object=MibTableColumn
cwdsiWnmWaitingAckMsgCount=_CwdsiWnmWaitingAckMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,9),_CwdsiWnmWaitingAckMsgCount_Type())
cwdsiWnmWaitingAckMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmWaitingAckMsgCount.setStatus(_A)
_CwdsiWnmDropMicTxMsgCount_Type=Counter32
_CwdsiWnmDropMicTxMsgCount_Object=MibTableColumn
cwdsiWnmDropMicTxMsgCount=_CwdsiWnmDropMicTxMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,10),_CwdsiWnmDropMicTxMsgCount_Type())
cwdsiWnmDropMicTxMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmDropMicTxMsgCount.setStatus(_A)
_CwdsiWnmDropUmdTxMsgCount_Type=Counter32
_CwdsiWnmDropUmdTxMsgCount_Object=MibTableColumn
cwdsiWnmDropUmdTxMsgCount=_CwdsiWnmDropUmdTxMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,11),_CwdsiWnmDropUmdTxMsgCount_Type())
cwdsiWnmDropUmdTxMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmDropUmdTxMsgCount.setStatus(_A)
_CwdsiWnmIndicatedMsgCount_Type=Counter32
_CwdsiWnmIndicatedMsgCount_Object=MibTableColumn
cwdsiWnmIndicatedMsgCount=_CwdsiWnmIndicatedMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,12),_CwdsiWnmIndicatedMsgCount_Type())
cwdsiWnmIndicatedMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmIndicatedMsgCount.setStatus(_A)
_CwdsiWnmRxMsgCount_Type=Counter32
_CwdsiWnmRxMsgCount_Object=MibTableColumn
cwdsiWnmRxMsgCount=_CwdsiWnmRxMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,13),_CwdsiWnmRxMsgCount_Type())
cwdsiWnmRxMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmRxMsgCount.setStatus(_A)
_CwdsiWnmDropRxMsgCount_Type=Counter32
_CwdsiWnmDropRxMsgCount_Object=MibTableColumn
cwdsiWnmDropRxMsgCount=_CwdsiWnmDropRxMsgCount_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,14),_CwdsiWnmDropRxMsgCount_Type())
cwdsiWnmDropRxMsgCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmDropRxMsgCount.setStatus(_A)
_CwdsiWnmDiscontinuityTime_Type=TimeStamp
_CwdsiWnmDiscontinuityTime_Object=MibTableColumn
cwdsiWnmDiscontinuityTime=_CwdsiWnmDiscontinuityTime_Object((1,3,6,1,4,1,9,9,509,1,4,1,1,15),_CwdsiWnmDiscontinuityTime_Type())
cwdsiWnmDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWnmDiscontinuityTime.setStatus(_A)
_CiscoWdsInfoStatistics_ObjectIdentity=ObjectIdentity
ciscoWdsInfoStatistics=_CiscoWdsInfoStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,509,1,5))
_CwdsiApNum_Type=Gauge32
_CwdsiApNum_Object=MibScalar
cwdsiApNum=_CwdsiApNum_Object((1,3,6,1,4,1,9,9,509,1,5,1),_CwdsiApNum_Type())
cwdsiApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiApNum.setStatus(_A)
if mibBuilder.loadTexts:cwdsiApNum.setUnits('access-points')
_CwdsiMnNum_Type=Gauge32
_CwdsiMnNum_Object=MibScalar
cwdsiMnNum=_CwdsiMnNum_Object((1,3,6,1,4,1,9,9,509,1,5,2),_CwdsiMnNum_Type())
cwdsiMnNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMnNum.setStatus(_A)
if mibBuilder.loadTexts:cwdsiMnNum.setUnits(_U)
_CwdsiAaaAuthAttemptCount_Type=Counter32
_CwdsiAaaAuthAttemptCount_Object=MibScalar
cwdsiAaaAuthAttemptCount=_CwdsiAaaAuthAttemptCount_Object((1,3,6,1,4,1,9,9,509,1,5,3),_CwdsiAaaAuthAttemptCount_Type())
cwdsiAaaAuthAttemptCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiAaaAuthAttemptCount.setStatus(_A)
_CwdsiAaaAuthSuccessCount_Type=Counter32
_CwdsiAaaAuthSuccessCount_Object=MibScalar
cwdsiAaaAuthSuccessCount=_CwdsiAaaAuthSuccessCount_Object((1,3,6,1,4,1,9,9,509,1,5,4),_CwdsiAaaAuthSuccessCount_Type())
cwdsiAaaAuthSuccessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiAaaAuthSuccessCount.setStatus(_A)
_CwdsiAaaAuthFailureCount_Type=Counter32
_CwdsiAaaAuthFailureCount_Object=MibScalar
cwdsiAaaAuthFailureCount=_CwdsiAaaAuthFailureCount_Object((1,3,6,1,4,1,9,9,509,1,5,5),_CwdsiAaaAuthFailureCount_Type())
cwdsiAaaAuthFailureCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiAaaAuthFailureCount.setStatus(_A)
_CwdsiMacSpoofingBlockCount_Type=Counter32
_CwdsiMacSpoofingBlockCount_Object=MibScalar
cwdsiMacSpoofingBlockCount=_CwdsiMacSpoofingBlockCount_Object((1,3,6,1,4,1,9,9,509,1,5,6),_CwdsiMacSpoofingBlockCount_Type())
cwdsiMacSpoofingBlockCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMacSpoofingBlockCount.setStatus(_A)
_CwdsiRoamsWithoutAaaAuthCount_Type=Counter32
_CwdsiRoamsWithoutAaaAuthCount_Object=MibScalar
cwdsiRoamsWithoutAaaAuthCount=_CwdsiRoamsWithoutAaaAuthCount_Object((1,3,6,1,4,1,9,9,509,1,5,7),_CwdsiRoamsWithoutAaaAuthCount_Type())
cwdsiRoamsWithoutAaaAuthCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamsWithoutAaaAuthCount.setStatus(_A)
_CwdsiRoamsWithFullAaaAuthCount_Type=Counter32
_CwdsiRoamsWithFullAaaAuthCount_Object=MibScalar
cwdsiRoamsWithFullAaaAuthCount=_CwdsiRoamsWithFullAaaAuthCount_Object((1,3,6,1,4,1,9,9,509,1,5,8),_CwdsiRoamsWithFullAaaAuthCount_Type())
cwdsiRoamsWithFullAaaAuthCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamsWithFullAaaAuthCount.setStatus(_A)
_CwdsiRoamsFastSecuredCount_Type=Counter32
_CwdsiRoamsFastSecuredCount_Object=MibScalar
cwdsiRoamsFastSecuredCount=_CwdsiRoamsFastSecuredCount_Object((1,3,6,1,4,1,9,9,509,1,5,9),_CwdsiRoamsFastSecuredCount_Type())
cwdsiRoamsFastSecuredCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamsFastSecuredCount.setStatus(_A)
_CwdsiMscMismatchCount_Type=Counter32
_CwdsiMscMismatchCount_Object=MibScalar
cwdsiMscMismatchCount=_CwdsiMscMismatchCount_Object((1,3,6,1,4,1,9,9,509,1,5,10),_CwdsiMscMismatchCount_Type())
cwdsiMscMismatchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMscMismatchCount.setStatus(_A)
_CwdsiKscFailureCount_Type=Counter32
_CwdsiKscFailureCount_Object=MibScalar
cwdsiKscFailureCount=_CwdsiKscFailureCount_Object((1,3,6,1,4,1,9,9,509,1,5,11),_CwdsiKscFailureCount_Type())
cwdsiKscFailureCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiKscFailureCount.setStatus(_A)
_CwdsiMicFailureCount_Type=Counter32
_CwdsiMicFailureCount_Object=MibScalar
cwdsiMicFailureCount=_CwdsiMicFailureCount_Object((1,3,6,1,4,1,9,9,509,1,5,12),_CwdsiMicFailureCount_Type())
cwdsiMicFailureCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMicFailureCount.setStatus(_A)
_CwdsiRnMismatchCount_Type=Counter32
_CwdsiRnMismatchCount_Object=MibScalar
cwdsiRnMismatchCount=_CwdsiRnMismatchCount_Object((1,3,6,1,4,1,9,9,509,1,5,13),_CwdsiRnMismatchCount_Type())
cwdsiRnMismatchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRnMismatchCount.setStatus(_A)
_CiscoWdsInfoMobility_ObjectIdentity=ObjectIdentity
ciscoWdsInfoMobility=_CiscoWdsInfoMobility_ObjectIdentity((1,3,6,1,4,1,9,9,509,1,6))
class _CwdsiLcpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('up',2),('inTransition',3)))
_CwdsiLcpStatus_Type.__name__=_G
_CwdsiLcpStatus_Object=MibScalar
cwdsiLcpStatus=_CwdsiLcpStatus_Object((1,3,6,1,4,1,9,9,509,1,6,1),_CwdsiLcpStatus_Type())
cwdsiLcpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiLcpStatus.setStatus(_A)
_CwdsiCsMgmtAddrType_Type=InetAddressType
_CwdsiCsMgmtAddrType_Object=MibScalar
cwdsiCsMgmtAddrType=_CwdsiCsMgmtAddrType_Object((1,3,6,1,4,1,9,9,509,1,6,2),_CwdsiCsMgmtAddrType_Type())
cwdsiCsMgmtAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiCsMgmtAddrType.setStatus(_A)
class _CwdsiCsMgmtAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CwdsiCsMgmtAddr_Type.__name__=_F
_CwdsiCsMgmtAddr_Object=MibScalar
cwdsiCsMgmtAddr=_CwdsiCsMgmtAddr_Object((1,3,6,1,4,1,9,9,509,1,6,3),_CwdsiCsMgmtAddr_Type())
cwdsiCsMgmtAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiCsMgmtAddr.setStatus(_A)
_CwdsiWdsAddrType_Type=InetAddressType
_CwdsiWdsAddrType_Object=MibScalar
cwdsiWdsAddrType=_CwdsiWdsAddrType_Object((1,3,6,1,4,1,9,9,509,1,6,4),_CwdsiWdsAddrType_Type())
cwdsiWdsAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWdsAddrType.setStatus(_A)
class _CwdsiWdsAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CwdsiWdsAddr_Type.__name__=_F
_CwdsiWdsAddr_Object=MibScalar
cwdsiWdsAddr=_CwdsiWdsAddr_Object((1,3,6,1,4,1,9,9,509,1,6,5),_CwdsiWdsAddr_Type())
cwdsiWdsAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWdsAddr.setStatus(_A)
_CwdsiWdsHsrpVirtualAddrType_Type=InetAddressType
_CwdsiWdsHsrpVirtualAddrType_Object=MibScalar
cwdsiWdsHsrpVirtualAddrType=_CwdsiWdsHsrpVirtualAddrType_Object((1,3,6,1,4,1,9,9,509,1,6,6),_CwdsiWdsHsrpVirtualAddrType_Type())
cwdsiWdsHsrpVirtualAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWdsHsrpVirtualAddrType.setStatus(_A)
class _CwdsiWdsHsrpVirtualAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CwdsiWdsHsrpVirtualAddr_Type.__name__=_F
_CwdsiWdsHsrpVirtualAddr_Object=MibScalar
cwdsiWdsHsrpVirtualAddr=_CwdsiWdsHsrpVirtualAddr_Object((1,3,6,1,4,1,9,9,509,1,6,7),_CwdsiWdsHsrpVirtualAddr_Type())
cwdsiWdsHsrpVirtualAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiWdsHsrpVirtualAddr.setStatus(_A)
class _CwdsiHsrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),(_L,2),(_N,3),('learn',4),('backup',5),('speak',6),('standby',7),(_K,8)))
_CwdsiHsrpState_Type.__name__=_G
_CwdsiHsrpState_Object=MibScalar
cwdsiHsrpState=_CwdsiHsrpState_Object((1,3,6,1,4,1,9,9,509,1,6,8),_CwdsiHsrpState_Type())
cwdsiHsrpState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiHsrpState.setStatus(_A)
_CwdsiMobilityGroupTable_Object=MibTable
cwdsiMobilityGroupTable=_CwdsiMobilityGroupTable_Object((1,3,6,1,4,1,9,9,509,1,6,9))
if mibBuilder.loadTexts:cwdsiMobilityGroupTable.setStatus(_A)
_CwdsiMobilityGroupEntry_Object=MibTableRow
cwdsiMobilityGroupEntry=_CwdsiMobilityGroupEntry_Object((1,3,6,1,4,1,9,9,509,1,6,9,1))
cwdsiMobilityGroupEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:cwdsiMobilityGroupEntry.setStatus(_A)
_CwdsiMobilityGrpNetworkId_Type=Unsigned32
_CwdsiMobilityGrpNetworkId_Object=MibTableColumn
cwdsiMobilityGrpNetworkId=_CwdsiMobilityGrpNetworkId_Object((1,3,6,1,4,1,9,9,509,1,6,9,1,1),_CwdsiMobilityGrpNetworkId_Type())
cwdsiMobilityGrpNetworkId.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdsiMobilityGrpNetworkId.setStatus(_A)
_CwdsiMobilityGrpTunnelAddrType_Type=InetAddressType
_CwdsiMobilityGrpTunnelAddrType_Object=MibTableColumn
cwdsiMobilityGrpTunnelAddrType=_CwdsiMobilityGrpTunnelAddrType_Object((1,3,6,1,4,1,9,9,509,1,6,9,1,2),_CwdsiMobilityGrpTunnelAddrType_Type())
cwdsiMobilityGrpTunnelAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMobilityGrpTunnelAddrType.setStatus(_A)
_CwdsiMobilityGrpTunnelAddr_Type=InetAddress
_CwdsiMobilityGrpTunnelAddr_Object=MibTableColumn
cwdsiMobilityGrpTunnelAddr=_CwdsiMobilityGrpTunnelAddr_Object((1,3,6,1,4,1,9,9,509,1,6,9,1,3),_CwdsiMobilityGrpTunnelAddr_Type())
cwdsiMobilityGrpTunnelAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMobilityGrpTunnelAddr.setStatus(_A)
_CwdsiMobilityGrpTunnelMtu_Type=Unsigned32
_CwdsiMobilityGrpTunnelMtu_Object=MibTableColumn
cwdsiMobilityGrpTunnelMtu=_CwdsiMobilityGrpTunnelMtu_Object((1,3,6,1,4,1,9,9,509,1,6,9,1,4),_CwdsiMobilityGrpTunnelMtu_Type())
cwdsiMobilityGrpTunnelMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMobilityGrpTunnelMtu.setStatus(_A)
class _CwdsiMobilityGrpFlags_Type(Bits):namedValues=NamedValues(*(('none',0),('trusted',1),('broadcast',2),('tcpMssAdjust',3),('dynamic',4),('multicast',5),('ipDiscovery',6)))
_CwdsiMobilityGrpFlags_Type.__name__='Bits'
_CwdsiMobilityGrpFlags_Object=MibTableColumn
cwdsiMobilityGrpFlags=_CwdsiMobilityGrpFlags_Object((1,3,6,1,4,1,9,9,509,1,6,9,1,5),_CwdsiMobilityGrpFlags_Type())
cwdsiMobilityGrpFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMobilityGrpFlags.setStatus(_A)
_CwdsiMobilityGrpMnNum_Type=Gauge32
_CwdsiMobilityGrpMnNum_Object=MibTableColumn
cwdsiMobilityGrpMnNum=_CwdsiMobilityGrpMnNum_Object((1,3,6,1,4,1,9,9,509,1,6,9,1,6),_CwdsiMobilityGrpMnNum_Type())
cwdsiMobilityGrpMnNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiMobilityGrpMnNum.setStatus(_A)
if mibBuilder.loadTexts:cwdsiMobilityGrpMnNum.setUnits(_U)
_CiscoWdsInfoRoamStatistics_ObjectIdentity=ObjectIdentity
ciscoWdsInfoRoamStatistics=_CiscoWdsInfoRoamStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,509,1,7))
_CwdsiRoamStatsStartTime_Type=DateAndTime
_CwdsiRoamStatsStartTime_Object=MibScalar
cwdsiRoamStatsStartTime=_CwdsiRoamStatsStartTime_Object((1,3,6,1,4,1,9,9,509,1,7,1),_CwdsiRoamStatsStartTime_Type())
cwdsiRoamStatsStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamStatsStartTime.setStatus(_A)
_CwdsiRoamStatsAvgFiveSeconds_Type=Gauge32
_CwdsiRoamStatsAvgFiveSeconds_Object=MibScalar
cwdsiRoamStatsAvgFiveSeconds=_CwdsiRoamStatsAvgFiveSeconds_Object((1,3,6,1,4,1,9,9,509,1,7,2),_CwdsiRoamStatsAvgFiveSeconds_Type())
cwdsiRoamStatsAvgFiveSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamStatsAvgFiveSeconds.setStatus(_A)
if mibBuilder.loadTexts:cwdsiRoamStatsAvgFiveSeconds.setUnits(_E)
_CwdsiRoamStatsAvgOneMinute_Type=Gauge32
_CwdsiRoamStatsAvgOneMinute_Object=MibScalar
cwdsiRoamStatsAvgOneMinute=_CwdsiRoamStatsAvgOneMinute_Object((1,3,6,1,4,1,9,9,509,1,7,3),_CwdsiRoamStatsAvgOneMinute_Type())
cwdsiRoamStatsAvgOneMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamStatsAvgOneMinute.setStatus(_A)
if mibBuilder.loadTexts:cwdsiRoamStatsAvgOneMinute.setUnits(_E)
_CwdsiRoamStatsAvgFiveMinutes_Type=Gauge32
_CwdsiRoamStatsAvgFiveMinutes_Object=MibScalar
cwdsiRoamStatsAvgFiveMinutes=_CwdsiRoamStatsAvgFiveMinutes_Object((1,3,6,1,4,1,9,9,509,1,7,4),_CwdsiRoamStatsAvgFiveMinutes_Type())
cwdsiRoamStatsAvgFiveMinutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamStatsAvgFiveMinutes.setStatus(_A)
if mibBuilder.loadTexts:cwdsiRoamStatsAvgFiveMinutes.setUnits(_E)
_CwdsiRoamMblGrpStatsTable_Object=MibTable
cwdsiRoamMblGrpStatsTable=_CwdsiRoamMblGrpStatsTable_Object((1,3,6,1,4,1,9,9,509,1,7,5))
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsTable.setStatus(_A)
_CwdsiRoamMblGrpStatsEntry_Object=MibTableRow
cwdsiRoamMblGrpStatsEntry=_CwdsiRoamMblGrpStatsEntry_Object((1,3,6,1,4,1,9,9,509,1,7,5,1))
cwdsiRoamMblGrpStatsEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsEntry.setStatus(_A)
class _CwdsiRoamMblGrpStatsNetworkId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_CwdsiRoamMblGrpStatsNetworkId_Type.__name__=_H
_CwdsiRoamMblGrpStatsNetworkId_Object=MibTableColumn
cwdsiRoamMblGrpStatsNetworkId=_CwdsiRoamMblGrpStatsNetworkId_Object((1,3,6,1,4,1,9,9,509,1,7,5,1,1),_CwdsiRoamMblGrpStatsNetworkId_Type())
cwdsiRoamMblGrpStatsNetworkId.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsNetworkId.setStatus(_A)
_CwdsiRoamMblGrpStatsTotal_Type=Counter32
_CwdsiRoamMblGrpStatsTotal_Object=MibTableColumn
cwdsiRoamMblGrpStatsTotal=_CwdsiRoamMblGrpStatsTotal_Object((1,3,6,1,4,1,9,9,509,1,7,5,1,2),_CwdsiRoamMblGrpStatsTotal_Type())
cwdsiRoamMblGrpStatsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsTotal.setStatus(_A)
_CwdsiRoamMblGrpStatsNoAuthAaa_Type=Counter32
_CwdsiRoamMblGrpStatsNoAuthAaa_Object=MibTableColumn
cwdsiRoamMblGrpStatsNoAuthAaa=_CwdsiRoamMblGrpStatsNoAuthAaa_Object((1,3,6,1,4,1,9,9,509,1,7,5,1,3),_CwdsiRoamMblGrpStatsNoAuthAaa_Type())
cwdsiRoamMblGrpStatsNoAuthAaa.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsNoAuthAaa.setStatus(_A)
_CwdsiRoamMblGrpStatsAuthAaa_Type=Counter32
_CwdsiRoamMblGrpStatsAuthAaa_Object=MibTableColumn
cwdsiRoamMblGrpStatsAuthAaa=_CwdsiRoamMblGrpStatsAuthAaa_Object((1,3,6,1,4,1,9,9,509,1,7,5,1,4),_CwdsiRoamMblGrpStatsAuthAaa_Type())
cwdsiRoamMblGrpStatsAuthAaa.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsAuthAaa.setStatus(_A)
_CwdsiRoamMblGrpStatsFastSecured_Type=Counter32
_CwdsiRoamMblGrpStatsFastSecured_Object=MibTableColumn
cwdsiRoamMblGrpStatsFastSecured=_CwdsiRoamMblGrpStatsFastSecured_Object((1,3,6,1,4,1,9,9,509,1,7,5,1,5),_CwdsiRoamMblGrpStatsFastSecured_Type())
cwdsiRoamMblGrpStatsFastSecured.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsFastSecured.setStatus(_A)
_CwdsiRoamMblGrpStatsFiveSeconds_Type=Gauge32
_CwdsiRoamMblGrpStatsFiveSeconds_Object=MibTableColumn
cwdsiRoamMblGrpStatsFiveSeconds=_CwdsiRoamMblGrpStatsFiveSeconds_Object((1,3,6,1,4,1,9,9,509,1,7,5,1,6),_CwdsiRoamMblGrpStatsFiveSeconds_Type())
cwdsiRoamMblGrpStatsFiveSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsFiveSeconds.setStatus(_A)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsFiveSeconds.setUnits(_E)
_CwdsiRoamMblGrpStatsOneMinute_Type=Gauge32
_CwdsiRoamMblGrpStatsOneMinute_Object=MibTableColumn
cwdsiRoamMblGrpStatsOneMinute=_CwdsiRoamMblGrpStatsOneMinute_Object((1,3,6,1,4,1,9,9,509,1,7,5,1,7),_CwdsiRoamMblGrpStatsOneMinute_Type())
cwdsiRoamMblGrpStatsOneMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsOneMinute.setStatus(_A)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsOneMinute.setUnits(_E)
_CwdsiRoamMblGrpStatsFiveMinutes_Type=Gauge32
_CwdsiRoamMblGrpStatsFiveMinutes_Object=MibTableColumn
cwdsiRoamMblGrpStatsFiveMinutes=_CwdsiRoamMblGrpStatsFiveMinutes_Object((1,3,6,1,4,1,9,9,509,1,7,5,1,8),_CwdsiRoamMblGrpStatsFiveMinutes_Type())
cwdsiRoamMblGrpStatsFiveMinutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsFiveMinutes.setStatus(_A)
if mibBuilder.loadTexts:cwdsiRoamMblGrpStatsFiveMinutes.setUnits(_E)
_CiscoWdsInfoMIBConform_ObjectIdentity=ObjectIdentity
ciscoWdsInfoMIBConform=_CiscoWdsInfoMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,509,2))
_CiscoWdsInfoMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWdsInfoMIBCompliances=_CiscoWdsInfoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,509,2,1))
_CiscoWdsInfoMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWdsInfoMIBGroups=_CiscoWdsInfoMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,509,2,2))
ciscoWdsInfoMacAuthCacheGroup=ObjectGroup((1,3,6,1,4,1,9,9,509,2,2,1))
ciscoWdsInfoMacAuthCacheGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:ciscoWdsInfoMacAuthCacheGroup.setStatus(_A)
ciscoWdsInfoAccessPointGroup=ObjectGroup((1,3,6,1,4,1,9,9,509,2,2,2))
ciscoWdsInfoAccessPointGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ciscoWdsInfoAccessPointGroup.setStatus(_A)
ciscoWdsInfoMobileNodeGroup=ObjectGroup((1,3,6,1,4,1,9,9,509,2,2,3))
ciscoWdsInfoMobileNodeGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoWdsInfoMobileNodeGroup.setStatus(_A)
ciscoWdsInfoNetworkManagerGroup=ObjectGroup((1,3,6,1,4,1,9,9,509,2,2,4))
ciscoWdsInfoNetworkManagerGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:ciscoWdsInfoNetworkManagerGroup.setStatus(_A)
ciscoWdsInfoStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,509,2,2,5))
ciscoWdsInfoStatisticsGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:ciscoWdsInfoStatisticsGroup.setStatus(_A)
ciscoWdsInfoMobilityGroup=ObjectGroup((1,3,6,1,4,1,9,9,509,2,2,6))
ciscoWdsInfoMobilityGroup.setObjects(*((_B,_I),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_J),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:ciscoWdsInfoMobilityGroup.setStatus(_A)
ciscoWdsInfoRoamStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,509,2,2,7))
ciscoWdsInfoRoamStatisticsGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:ciscoWdsInfoRoamStatisticsGroup.setStatus(_A)
cwdsiLcpStatusChange=NotificationType((1,3,6,1,4,1,9,9,509,0,1))
cwdsiLcpStatusChange.setObjects((_B,_I))
if mibBuilder.loadTexts:cwdsiLcpStatusChange.setStatus(_A)
cwdsiHsrpStateChange=NotificationType((1,3,6,1,4,1,9,9,509,0,2))
cwdsiHsrpStateChange.setObjects((_B,_J))
if mibBuilder.loadTexts:cwdsiHsrpStateChange.setStatus(_A)
ciscoWdsInfoNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,509,2,2,8))
ciscoWdsInfoNotifGroup.setObjects(*((_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:ciscoWdsInfoNotifGroup.setStatus(_A)
ciscoWdsInfoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,509,2,1,1))
ciscoWdsInfoMIBCompliance.setObjects(*((_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:ciscoWdsInfoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CWdsClientTrackingStatus':CWdsClientTrackingStatus,'CWdsDeviceAuthType':CWdsDeviceAuthType,'CWdsDeviceState':CWdsDeviceState,'ciscoWdsInfoMIB':ciscoWdsInfoMIB,'ciscoWdsInfoMIBNotifs':ciscoWdsInfoMIBNotifs,_Ah:cwdsiLcpStatusChange,_Ai:cwdsiHsrpStateChange,'ciscoWdsInfoMIBObjects':ciscoWdsInfoMIBObjects,'ciscoWdsInfoMacAuthCache':ciscoWdsInfoMacAuthCache,'cwdsiMacAuthCacheTable':cwdsiMacAuthCacheTable,'cwdsiMacAuthCacheEntry':cwdsiMacAuthCacheEntry,_O:cwdsiMacAuthCacheMacAddr,_X:cwdsiMacAuthCacheAge,'ciscoWdsInfoAccessPoint':ciscoWdsInfoAccessPoint,'cwdsiApTable':cwdsiApTable,'cwdsiApEntry':cwdsiApEntry,_P:cwdsiApMacAddr,_Z:cwdsiApAddrType,_Y:cwdsiApAddr,_a:cwdsiApName,_b:cwdsiApState,_c:cwdsiApLifeTime,_d:cwdsiApNeighborAddrType,_e:cwdsiApNeighborAddr,_f:cwdsiApNeighborName,_g:cwdsiApNeighborPortName,'ciscoWdsInfoMobileNode':ciscoWdsInfoMobileNode,'cwdsiMnTable':cwdsiMnTable,'cwdsiMnEntry':cwdsiMnEntry,_R:cwdsiMnMacAddr,_i:cwdsiMnAddrType,_h:cwdsiMnAddr,_j:cwdsiMnApMacAddr,_l:cwdsiMnApAddrType,_k:cwdsiMnApAddr,_m:cwdsiMnMobilityNetworkId,_n:cwdsiMnState,_q:cwdsiMnSsid,_o:cwdsiMnBssid,_p:cwdsiMnVlan,_r:cwdsiMnKeyMgmt,_s:cwdsiMnAuthType,_t:cwdsiMnUptime,_u:cwdsiMnLifetime,'ciscoWdsInfoNetworkManager':ciscoWdsInfoNetworkManager,'cwdsiWnmTable':cwdsiWnmTable,'cwdsiWnmEntry':cwdsiWnmEntry,_S:cwdsiWnmAddrType,_T:cwdsiWnmAddr,_v:cwdsiWnmState,_w:cwdsiWnmLinkStatus,_x:cwdsiWnmClientTracking,_y:cwdsiWnmReqMsgCount,_z:cwdsiWnmSentMsgCount,_A0:cwdsiWnmRetryTxMsgCount,_A1:cwdsiWnmWaitingAckMsgCount,_A2:cwdsiWnmDropMicTxMsgCount,_A3:cwdsiWnmDropUmdTxMsgCount,_A4:cwdsiWnmIndicatedMsgCount,_A5:cwdsiWnmRxMsgCount,_A6:cwdsiWnmDropRxMsgCount,_A7:cwdsiWnmDiscontinuityTime,'ciscoWdsInfoStatistics':ciscoWdsInfoStatistics,_A8:cwdsiApNum,_A9:cwdsiMnNum,_AA:cwdsiAaaAuthAttemptCount,_AB:cwdsiAaaAuthSuccessCount,_AC:cwdsiAaaAuthFailureCount,_AD:cwdsiMacSpoofingBlockCount,_AE:cwdsiRoamsWithoutAaaAuthCount,_AF:cwdsiRoamsWithFullAaaAuthCount,_AG:cwdsiRoamsFastSecuredCount,_AH:cwdsiMscMismatchCount,_AI:cwdsiKscFailureCount,_AJ:cwdsiMicFailureCount,_AK:cwdsiRnMismatchCount,'ciscoWdsInfoMobility':ciscoWdsInfoMobility,_I:cwdsiLcpStatus,_AL:cwdsiCsMgmtAddrType,_AM:cwdsiCsMgmtAddr,_AN:cwdsiWdsAddrType,_AO:cwdsiWdsAddr,_AP:cwdsiWdsHsrpVirtualAddrType,_AQ:cwdsiWdsHsrpVirtualAddr,_J:cwdsiHsrpState,'cwdsiMobilityGroupTable':cwdsiMobilityGroupTable,'cwdsiMobilityGroupEntry':cwdsiMobilityGroupEntry,_V:cwdsiMobilityGrpNetworkId,_AR:cwdsiMobilityGrpTunnelAddrType,_AS:cwdsiMobilityGrpTunnelAddr,_AT:cwdsiMobilityGrpTunnelMtu,_AU:cwdsiMobilityGrpFlags,_AV:cwdsiMobilityGrpMnNum,'ciscoWdsInfoRoamStatistics':ciscoWdsInfoRoamStatistics,_AW:cwdsiRoamStatsStartTime,_AX:cwdsiRoamStatsAvgFiveSeconds,_AY:cwdsiRoamStatsAvgOneMinute,_AZ:cwdsiRoamStatsAvgFiveMinutes,'cwdsiRoamMblGrpStatsTable':cwdsiRoamMblGrpStatsTable,'cwdsiRoamMblGrpStatsEntry':cwdsiRoamMblGrpStatsEntry,_W:cwdsiRoamMblGrpStatsNetworkId,_Aa:cwdsiRoamMblGrpStatsTotal,_Ab:cwdsiRoamMblGrpStatsNoAuthAaa,_Ac:cwdsiRoamMblGrpStatsAuthAaa,_Ad:cwdsiRoamMblGrpStatsFastSecured,_Ae:cwdsiRoamMblGrpStatsFiveSeconds,_Af:cwdsiRoamMblGrpStatsOneMinute,_Ag:cwdsiRoamMblGrpStatsFiveMinutes,'ciscoWdsInfoMIBConform':ciscoWdsInfoMIBConform,'ciscoWdsInfoMIBCompliances':ciscoWdsInfoMIBCompliances,'ciscoWdsInfoMIBCompliance':ciscoWdsInfoMIBCompliance,'ciscoWdsInfoMIBGroups':ciscoWdsInfoMIBGroups,_Aj:ciscoWdsInfoMacAuthCacheGroup,_Ak:ciscoWdsInfoAccessPointGroup,_Al:ciscoWdsInfoMobileNodeGroup,_Am:ciscoWdsInfoNetworkManagerGroup,_An:ciscoWdsInfoStatisticsGroup,_Ao:ciscoWdsInfoMobilityGroup,_Ap:ciscoWdsInfoRoamStatisticsGroup,_Aq:ciscoWdsInfoNotifGroup})