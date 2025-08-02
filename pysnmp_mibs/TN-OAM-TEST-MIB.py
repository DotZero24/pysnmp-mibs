_AM='tnOamEthCfmPingCtlEntry'
_AL='TmnxOamTestMode'
_AK='tnOamSaaCtlTestIndex'
_AJ='tnOamLspTrMapIndex'
_AI='TmnxOamMplsEchoDownMapTlvOrNone'
_AH='controlChannel'
_AG='0000000000000000'
_AF='tnOamPingHistoryIndex'
_AE='testCompletion'
_AD='testFailure'
_AC='undetermined'
_AB='unspecified'
_AA='TmnxVcIdOrNone'
_A9='TmnxAdminState'
_A8='TItemDescription'
_A7='MacAddress'
_A6='Dot1agCfmMepIdOrZero'
_A5='TmnxOamVccvAssocChannel'
_A4='TmnxOamVccvTestSubMode'
_A3='TmnxOamLspAssocChannel'
_A2='TmnxOamMplsTpPathType'
_A1='TmnxOamLspTestSubMode'
_A0='time-to-live value'
_z='tnOamPingResultsTestRunIndex'
_y='seconds'
_x='milliseconds'
_w='unknown'
_v='static'
_u='notApplicable'
_t='TmnxSpokeSdpIdOrZero'
_s='TmnxServId'
_r='TmnxMplsTpNodeID'
_q='TmnxMplsTpGlobalID'
_p='TProfile'
_o='TFCName'
_n='SdpBindId'
_m='IpAddressPrefixLength'
_l='SdpId'
_k='Bits'
_j='InetAddressPrefixLength'
_i='tnOamTrProbeHistoryProbeIndex'
_h='tnOamTrProbeHistoryHopIndex'
_g='tnOamTrProbeHistoryIndex'
_f='probes'
_e='00000000'
_d='Octets'
_c='disabled'
_b='enabled'
_a='StorageType'
_Z='tnOamTrResultsTestRunIndex'
_Y='octets'
_X='none'
_W='TmnxVRtrID'
_V='TmnxPwGlobalIdOrZero'
_U='IpAddress'
_T='microseconds squared'
_S='tnOamPingCtlTestIndex'
_R='SnmpAdminString'
_Q='OctetString'
_P='tnOamTrCtlTestIndex'
_O='TNamedItemOrEmpty'
_N='not-accessible'
_M='TruthValue'
_L='InetAddressType'
_K='tnSysSwitchId'
_J='TROPIC-SYSTEM-MIB'
_I='Integer32'
_H='microseconds'
_G='InetAddress'
_F='obsolete'
_E='TN-OAM-TEST-MIB'
_D='Unsigned32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmMepIdOrZero,=mibBuilder.importSymbols('IEEE8021-CFM-MIB',_A6)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_j,_L)
RouterID,=mibBuilder.importSymbols('OSPF-MIB','RouterID')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_k,'Counter32','Counter64','Gauge32',_I,_U,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString',_A7,'PhysAddress','RowStatus',_a,'TextualConvention','TimeStamp',_M)
SdpBindVcType,SdpId=mibBuilder.importSymbols('TN-SERV-MIB','SdpBindVcType',_l)
IpAddressPrefixLength,SdpBindId,TFCName,TItemDescription,TLNamedItemOrEmpty,TNamedItemOrEmpty,TProfile,TmnxAdminState,TmnxMplsTpGlobalID,TmnxMplsTpNodeID,TmnxPwGlobalIdOrZero,TmnxServId,TmnxSpokeSdpIdOrZero,TmnxStrSapId,TmnxVRtrID,TmnxVcIdOrNone=mibBuilder.importSymbols('TN-TC-MIB',_m,_n,_o,_A8,'TLNamedItemOrEmpty',_O,_p,_A9,_q,_r,_V,_s,_t,'TmnxStrSapId',_W,_AA)
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_J,_K)
tnOamTestMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,11))
if mibBuilder.loadTexts:tnOamTestMIBModule.setRevisions(('2021-06-04 00:00','2020-06-19 00:00','2019-11-15 00:00','2019-03-29 00:00','2015-08-24 00:00','2015-08-05 00:00','2015-05-05 00:00','2013-08-22 00:00','2013-03-26 00:00','2011-02-01 00:00','2009-02-28 00:00','2008-01-01 00:00','2007-01-01 00:00','2006-03-09 00:00','2005-08-31 00:00','2005-01-24 00:00','2004-01-15 00:00','2003-08-15 00:00','2003-01-20 00:00','2001-11-15 00:00'))
class TmnxOamLspAssocChannel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_u,1),('nonIp',2),(_X,3),('ipv4',4)))
class TmnxOamLspTestSubMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AB,1),(_v,2),('bgpLabeledPrefix',3)))
class TmnxOamMplsEchoDownMapTlv(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dsmap',1),('ddmap',2)))
class TmnxOamMplsEchoDownMapTlvOrNone(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dsmap',1),('ddmap',2),(_X,3)))
class TmnxOamMplsTpPathType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('working',1),('protect',2),('active',3)))
class TmnxOamTestMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notConfigured',0),('ping',1),('traceroute',2)))
class TmnxOamPingRtnCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_u,0),('fecEgress',1),('fecNoMap',2),('notDownstream',3),('downstream',4),('downstreamNotLabel',5),('downstreamNotMac',6),('downstreamNotMacFlood',7),('malformedEchoRequest',8),('tlvNotUnderstood',9),('downstreamNotInMfib',10),('downstreamMismatched',11),('upstreamIfIdUnkn',12),('noMplsFwd',13),('noLabelAtStackDepth',14),('protoIntfMismatched',15),('terminatedByOneLabel',16),('seeDDMapForRetCodeSubCode',17),('fecStackChange',18)))
class TmnxOamAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_w,0),('ipv4Address',1),('ipv6Address',2),('macAddress',3),('sapId',4),('sdpId',5),('localCpu',6),('ipv4Unnumbered',7),('ipv6Unnumbered',8),('sdpBindId',9)))
class TmnxOamResponseStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155)));namedValues=NamedValues(*(('responseReceived',1),(_w,2),('internalError',3),('maxConcurrentLimitReached',4),('requestTimedOut',5),('unknownOrigSdpId',6),('downOrigSdpId',7),('requestTerminated',8),('invalidOriginatorId',9),('invalidResponderId',10),('unknownRespSdpId',11),('downRespSdpId',12),('invalidServiceId',13),('invalidSdp',14),('downServiceSdp',15),('noServiceEgressLabel',16),('invalidHostAddress',17),('invalidMacAddress',18),('invalidLspName',19),('macIsLocal',20),('farEndUnreachable',21),('downOriginatorId',22),('downResponderId',23),('changedResponderId',24),('downOrigSvcId',25),('downRespSvcId',26),('noServiceIngressLabel',27),('mismatchCustId',28),('mismatchSvcType',29),('mismatchSvcMtu',30),('mismatchSvcLabel',31),('noSdpBoundToSvc',32),('downOrigSdpBinding',33),('invalidLspPathName',34),('noLspEndpointAddr',35),('invalidLspId',36),('downLspPath',37),('invalidLspProtocol',38),('invalidLspLabel',39),('routeIsLocal',40),('noRouteToDest',41),('localExtranetRoute',42),('srcIpInBgpVpnRoute',43),('srcIpInvalid',44),('bgpDaemonBusy',45),('mcastNotEnabled',46),('mTraceNoSGFlow',47),('mTraceSysIpNotCfg',48),('noFwdEntryInMfib',49),('dnsNameNotFound',50),('noSocket',51),('socketOptVprnIdFail',52),('socketOptIfInexFail',53),('socketOptNextHopFail',54),('socketOptMtuDiscFail',55),('socketOptSndbufFail',56),('socketOptHdrincFail',57),('socketOptTosFail',58),('socketOptTtlFail',59),('bindSocketFail',60),('noRouteByIntf',61),('noIntf',62),('noLocalIp',63),('sendtoFail',64),('rcvdWrongType',65),('noDirectInterface',66),('nexthopUnreachable',67),('socketOptHwTimeStampFail',68),('noSpokeSdpInVll',69),('farEndVccvNotSupported',70),('noVcEgressLabel',71),('socketOptIpSessionFail',72),('rcvdWrongSize',73),('dnsLookupFail',74),('noIpv6SrcAddrOnIntf',75),('multipathNotSupported',76),('nhIntfNameNotFound',77),('msPwInvalidReplyMode',78),('ancpNoAncpString',79),('ancpNoSubscriber',80),('ancpNoAncpStringForSubscriber',81),('ancpNoAccessNodeforAncpString',82),('ancpNoAncpCapabilityNegotiated',83),('ancpOtherTestInProgress',84),('ancpMaxNbrAncpTestsInProgress',85),('spokeSdpOperDown',86),('noMsPwVccvInReplyDir',87),('p2mpLspNameOrInstInvalid',88),('p2mpLspS2LPathDown',89),('p2mpLspS2LAddressInvalid',90),('p2mpLspNotOperational',91),('p2mpLspTrMultipleReplies',92),('invalidMepId',93),('multipleReplies',94),('packetSizeTooBig',95),('gtpPingError',96),('gtpPingRsrcUnavailable',97),('gtpPingDupRequest',98),('gtpPingCleanUpInProg',99),('invalidInterface',100),('p2mpLspNotFound',101),('ethCfmSlmInLoss',102),('ethCfmSlmOutLoss',103),('ethCfmSlmUnacknowledged',104),('spokeSdpFecNoBndFound',105),('mtraceNotSupportedP2mp',106),('useFec129Parameters',107),('dnsServerUnexpectedResponse',108),('dnsServerResponseFormErr',109),('dnsServerResponseServFail',110),('dnsServerResponseNotImp',111),('dnsServerResponseRefused',112),('sendFailUndefinedServiceId',113),('sendFailWrongServiceType',114),('sendFailSubnettedService',115),('invalidRespServiceId',116),('adminDownOrigSdpBind',117),('operDownRespSdpBind',118),('adminDownRespSdpBind',119),('sdpBindVcidMismatch',120),('sdpBindTypeMismatch',121),('sdpBindVcTypeMismatch',122),('sdpBindVlanVcTagMismatch',123),('adminDownOrigSvc',124),('adminDownRespSvc',125),('adminDownOrigSdpId',126),('adminDownRespSdpId',127),('mTraceSourceIsNotRemote',128),('invalidVirtualRouterId',129),('ldpPrefixIsLocal',130),('sourceIpIsNotLocal',131),('nextHopIpIsLocal',132),('targetIpIsLocal',133),('invalidControlPlaneOption',134),('iomRevisionNotSupported',135),('invalidSourceMacOption',136),('sendFailSpbMgdService',137),('useStaticPwParameters',138),('type1Fec129PwNotSupported',139),('mplsTpLspPathNotOperational',140),('invalidStaticMplsTpLsp',141),('controlWordNotValid',142),('pwPathIdNotConfigured',143),('notSupportedOnVcSwitchService',144),('sdpFarEndNotSupported',145),('mplsTpLspPathShutdown',146),('forceOptionIsBlocked',147),('intfForLspPathIsNotOperational',148),('ttlExpired',149),('networkUnreachable',150),('hostUnreachable',151),('bgpLabelPrefixIsLocal',152),('bgpLabelPrefixUnknown',153),('ldpPrefixUnknown',154),('l2tpv3DeliveryTypeUnsupported',155)))
class TmnxOamSignalProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_w,0),(_v,1),('bgp',2),('ldp',3),('rsvpTe',4),('crLdp',5)))
class TmnxOamTestResponsePlane(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('controlPlane',1),('dataPlane',2),(_X,3)))
class TmnxOamSaaThreshold(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noThreshold',0),('inJitter',1),('outJitter',2),('rtJitter',3),('inLoss',4),('outLoss',5),('rtLoss',6),('inLatency',7),('outLatency',8),('rtLatency',9)))
class TmnxOamVccvAssocChannel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),('nonIp',2),('ipv4',3)))
class TmnxOamVccvTestSubMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AB,1),(_v,2)))
class TmnxOamVcType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,11)));namedValues=NamedValues(*(('meshSdp',5),('spokeSdp',11)))
class TmnxOamTestResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_AC,0),('success',1),('failed',2),('aborted',3),('txResourcesUnavail',4)))
_TnOamTestObjs_ObjectIdentity=ObjectIdentity
tnOamTestObjs=_TnOamTestObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,11))
_TnOamPingObjs_ObjectIdentity=ObjectIdentity
tnOamPingObjs=_TnOamPingObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,11,1))
_TnOamPingCtlAttributeTotal_Type=Integer32
_TnOamPingCtlAttributeTotal_Object=MibScalar
tnOamPingCtlAttributeTotal=_TnOamPingCtlAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,11,1,3),_TnOamPingCtlAttributeTotal_Type())
tnOamPingCtlAttributeTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingCtlAttributeTotal.setStatus(_A)
_TnOamPingCtlTable_Object=MibTable
tnOamPingCtlTable=_TnOamPingCtlTable_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4))
if mibBuilder.loadTexts:tnOamPingCtlTable.setStatus(_A)
_TnOamPingCtlEntry_Object=MibTableRow
tnOamPingCtlEntry=_TnOamPingCtlEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1))
tnOamPingCtlEntry.setIndexNames((0,_J,_K),(0,_E,_S))
if mibBuilder.loadTexts:tnOamPingCtlEntry.setStatus(_A)
class _TnOamPingCtlTestIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TnOamPingCtlTestIndex_Type.__name__=_R
_TnOamPingCtlTestIndex_Object=MibTableColumn
tnOamPingCtlTestIndex=_TnOamPingCtlTestIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,1),_TnOamPingCtlTestIndex_Type())
tnOamPingCtlTestIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamPingCtlTestIndex.setStatus(_A)
_TnOamPingCtlRowStatus_Type=RowStatus
_TnOamPingCtlRowStatus_Object=MibTableColumn
tnOamPingCtlRowStatus=_TnOamPingCtlRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,2),_TnOamPingCtlRowStatus_Type())
tnOamPingCtlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlRowStatus.setStatus(_A)
class _TnOamPingCtlStorageType_Type(StorageType):defaultValue=2
_TnOamPingCtlStorageType_Type.__name__=_a
_TnOamPingCtlStorageType_Object=MibTableColumn
tnOamPingCtlStorageType=_TnOamPingCtlStorageType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,3),_TnOamPingCtlStorageType_Type())
tnOamPingCtlStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlStorageType.setStatus(_A)
class _TnOamPingCtlDescr_Type(SnmpAdminString):defaultHexValue=''
_TnOamPingCtlDescr_Type.__name__=_R
_TnOamPingCtlDescr_Object=MibTableColumn
tnOamPingCtlDescr=_TnOamPingCtlDescr_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,4),_TnOamPingCtlDescr_Type())
tnOamPingCtlDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlDescr.setStatus(_A)
class _TnOamPingCtlTestMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*((_X,0),('sdpPing',1),('mtuPing',2),('svcPing',3),('macPing',5),('macPopulate',6),('macPurge',7),('lspPing',8),('vprnPing',9),('atmPing',10),('mfibPing',11),('cpePing',12),('mrInfo',13),('vccvPing',14),('icmpPing',15),('dnsPing',16),('ancpLoopback',17),('p2mpLspPing',18),('ethCfmLoopback',19),('ethCfmTwoWayDelay',20),('mobGtpPing',21),('ethCfmTwoWaySlm',22),('ethCfmTwoWayLm',23),('ethCfmOneWayDelay',24)))
_TnOamPingCtlTestMode_Type.__name__=_I
_TnOamPingCtlTestMode_Object=MibTableColumn
tnOamPingCtlTestMode=_TnOamPingCtlTestMode_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,5),_TnOamPingCtlTestMode_Type())
tnOamPingCtlTestMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlTestMode.setStatus(_A)
class _TnOamPingCtlAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_TnOamPingCtlAdminStatus_Type.__name__=_I
_TnOamPingCtlAdminStatus_Object=MibTableColumn
tnOamPingCtlAdminStatus=_TnOamPingCtlAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,6),_TnOamPingCtlAdminStatus_Type())
tnOamPingCtlAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlAdminStatus.setStatus(_A)
class _TnOamPingCtlOrigSdpId_Type(SdpId):defaultValue=0
_TnOamPingCtlOrigSdpId_Type.__name__=_l
_TnOamPingCtlOrigSdpId_Object=MibTableColumn
tnOamPingCtlOrigSdpId=_TnOamPingCtlOrigSdpId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,7),_TnOamPingCtlOrigSdpId_Type())
tnOamPingCtlOrigSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlOrigSdpId.setStatus(_A)
class _TnOamPingCtlRespSdpId_Type(SdpId):defaultValue=0
_TnOamPingCtlRespSdpId_Type.__name__=_l
_TnOamPingCtlRespSdpId_Object=MibTableColumn
tnOamPingCtlRespSdpId=_TnOamPingCtlRespSdpId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,8),_TnOamPingCtlRespSdpId_Type())
tnOamPingCtlRespSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlRespSdpId.setStatus(_A)
class _TnOamPingCtlFcName_Type(TFCName):defaultValue=OctetString('be')
_TnOamPingCtlFcName_Type.__name__=_o
_TnOamPingCtlFcName_Object=MibTableColumn
tnOamPingCtlFcName=_TnOamPingCtlFcName_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,9),_TnOamPingCtlFcName_Type())
tnOamPingCtlFcName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlFcName.setStatus(_A)
class _TnOamPingCtlProfile_Type(TProfile):defaultValue=2
_TnOamPingCtlProfile_Type.__name__=_p
_TnOamPingCtlProfile_Object=MibTableColumn
tnOamPingCtlProfile=_TnOamPingCtlProfile_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,10),_TnOamPingCtlProfile_Type())
tnOamPingCtlProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlProfile.setStatus(_A)
class _TnOamPingCtlMtuStartSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(40,9198))
_TnOamPingCtlMtuStartSize_Type.__name__=_D
_TnOamPingCtlMtuStartSize_Object=MibTableColumn
tnOamPingCtlMtuStartSize=_TnOamPingCtlMtuStartSize_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,11),_TnOamPingCtlMtuStartSize_Type())
tnOamPingCtlMtuStartSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlMtuStartSize.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingCtlMtuStartSize.setUnits(_d)
class _TnOamPingCtlMtuEndSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(40,9198))
_TnOamPingCtlMtuEndSize_Type.__name__=_D
_TnOamPingCtlMtuEndSize_Object=MibTableColumn
tnOamPingCtlMtuEndSize=_TnOamPingCtlMtuEndSize_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,12),_TnOamPingCtlMtuEndSize_Type())
tnOamPingCtlMtuEndSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlMtuEndSize.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingCtlMtuEndSize.setUnits(_d)
class _TnOamPingCtlMtuStepSize_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_TnOamPingCtlMtuStepSize_Type.__name__=_D
_TnOamPingCtlMtuStepSize_Object=MibTableColumn
tnOamPingCtlMtuStepSize=_TnOamPingCtlMtuStepSize_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,13),_TnOamPingCtlMtuStepSize_Type())
tnOamPingCtlMtuStepSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlMtuStepSize.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingCtlMtuStepSize.setUnits(_d)
class _TnOamPingCtlTargetIpAddress_Type(IpAddress):defaultHexValue=_e
_TnOamPingCtlTargetIpAddress_Type.__name__=_U
_TnOamPingCtlTargetIpAddress_Object=MibTableColumn
tnOamPingCtlTargetIpAddress=_TnOamPingCtlTargetIpAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,14),_TnOamPingCtlTargetIpAddress_Type())
tnOamPingCtlTargetIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlTargetIpAddress.setStatus(_F)
class _TnOamPingCtlServiceId_Type(TmnxServId):defaultValue=0;subtypeSpec=TmnxServId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TnOamPingCtlServiceId_Type.__name__=_s
_TnOamPingCtlServiceId_Object=MibTableColumn
tnOamPingCtlServiceId=_TnOamPingCtlServiceId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,15),_TnOamPingCtlServiceId_Type())
tnOamPingCtlServiceId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlServiceId.setStatus(_A)
class _TnOamPingCtlLocalSdp_Type(TruthValue):defaultValue=2
_TnOamPingCtlLocalSdp_Type.__name__=_M
_TnOamPingCtlLocalSdp_Object=MibTableColumn
tnOamPingCtlLocalSdp=_TnOamPingCtlLocalSdp_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,16),_TnOamPingCtlLocalSdp_Type())
tnOamPingCtlLocalSdp.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlLocalSdp.setStatus(_A)
class _TnOamPingCtlRemoteSdp_Type(TruthValue):defaultValue=2
_TnOamPingCtlRemoteSdp_Type.__name__=_M
_TnOamPingCtlRemoteSdp_Object=MibTableColumn
tnOamPingCtlRemoteSdp=_TnOamPingCtlRemoteSdp_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,17),_TnOamPingCtlRemoteSdp_Type())
tnOamPingCtlRemoteSdp.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlRemoteSdp.setStatus(_A)
class _TnOamPingCtlSize_Type(Unsigned32):defaultValue=72;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16384))
_TnOamPingCtlSize_Type.__name__=_D
_TnOamPingCtlSize_Object=MibTableColumn
tnOamPingCtlSize=_TnOamPingCtlSize_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,18),_TnOamPingCtlSize_Type())
tnOamPingCtlSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlSize.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingCtlSize.setUnits(_Y)
class _TnOamPingCtlTimeOut_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120000))
_TnOamPingCtlTimeOut_Type.__name__=_D
_TnOamPingCtlTimeOut_Object=MibTableColumn
tnOamPingCtlTimeOut=_TnOamPingCtlTimeOut_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,19),_TnOamPingCtlTimeOut_Type())
tnOamPingCtlTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlTimeOut.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingCtlTimeOut.setUnits(_x)
class _TnOamPingCtlProbeCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_TnOamPingCtlProbeCount_Type.__name__=_D
_TnOamPingCtlProbeCount_Object=MibTableColumn
tnOamPingCtlProbeCount=_TnOamPingCtlProbeCount_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,20),_TnOamPingCtlProbeCount_Type())
tnOamPingCtlProbeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlProbeCount.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingCtlProbeCount.setUnits(_f)
class _TnOamPingCtlInterval_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,90000))
_TnOamPingCtlInterval_Type.__name__=_D
_TnOamPingCtlInterval_Object=MibTableColumn
tnOamPingCtlInterval=_TnOamPingCtlInterval_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,21),_TnOamPingCtlInterval_Type())
tnOamPingCtlInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlInterval.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingCtlInterval.setUnits(_x)
class _TnOamPingCtlMaxRows_Type(Unsigned32):defaultValue=300
_TnOamPingCtlMaxRows_Type.__name__=_D
_TnOamPingCtlMaxRows_Object=MibTableColumn
tnOamPingCtlMaxRows=_TnOamPingCtlMaxRows_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,22),_TnOamPingCtlMaxRows_Type())
tnOamPingCtlMaxRows.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlMaxRows.setStatus(_F)
if mibBuilder.loadTexts:tnOamPingCtlMaxRows.setUnits('rows')
class _TnOamPingCtlTrapGeneration_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('probeFailure',0),(_AD,1),(_AE,2)))
_TnOamPingCtlTrapGeneration_Type.__name__=_k
_TnOamPingCtlTrapGeneration_Object=MibTableColumn
tnOamPingCtlTrapGeneration=_TnOamPingCtlTrapGeneration_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,23),_TnOamPingCtlTrapGeneration_Type())
tnOamPingCtlTrapGeneration.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlTrapGeneration.setStatus(_A)
class _TnOamPingCtlTrapProbeFailureFilter_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_TnOamPingCtlTrapProbeFailureFilter_Type.__name__=_D
_TnOamPingCtlTrapProbeFailureFilter_Object=MibTableColumn
tnOamPingCtlTrapProbeFailureFilter=_TnOamPingCtlTrapProbeFailureFilter_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,24),_TnOamPingCtlTrapProbeFailureFilter_Type())
tnOamPingCtlTrapProbeFailureFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlTrapProbeFailureFilter.setStatus(_A)
class _TnOamPingCtlTrapTestFailureFilter_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_TnOamPingCtlTrapTestFailureFilter_Type.__name__=_D
_TnOamPingCtlTrapTestFailureFilter_Object=MibTableColumn
tnOamPingCtlTrapTestFailureFilter=_TnOamPingCtlTrapTestFailureFilter_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,25),_TnOamPingCtlTrapTestFailureFilter_Type())
tnOamPingCtlTrapTestFailureFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlTrapTestFailureFilter.setStatus(_A)
class _TnOamPingCtlSAA_Type(TruthValue):defaultValue=2
_TnOamPingCtlSAA_Type.__name__=_M
_TnOamPingCtlSAA_Object=MibTableColumn
tnOamPingCtlSAA=_TnOamPingCtlSAA_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,26),_TnOamPingCtlSAA_Type())
tnOamPingCtlSAA.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlSAA.setStatus(_A)
_TnOamPingCtlRuns_Type=Counter32
_TnOamPingCtlRuns_Object=MibTableColumn
tnOamPingCtlRuns=_TnOamPingCtlRuns_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,27),_TnOamPingCtlRuns_Type())
tnOamPingCtlRuns.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingCtlRuns.setStatus(_A)
_TnOamPingCtlFailures_Type=Counter32
_TnOamPingCtlFailures_Object=MibTableColumn
tnOamPingCtlFailures=_TnOamPingCtlFailures_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,28),_TnOamPingCtlFailures_Type())
tnOamPingCtlFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingCtlFailures.setStatus(_A)
_TnOamPingCtlLastRunResult_Type=TmnxOamTestResult
_TnOamPingCtlLastRunResult_Object=MibTableColumn
tnOamPingCtlLastRunResult=_TnOamPingCtlLastRunResult_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,29),_TnOamPingCtlLastRunResult_Type())
tnOamPingCtlLastRunResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingCtlLastRunResult.setStatus(_A)
_TnOamPingCtlLastChanged_Type=TimeStamp
_TnOamPingCtlLastChanged_Object=MibTableColumn
tnOamPingCtlLastChanged=_TnOamPingCtlLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,30),_TnOamPingCtlLastChanged_Type())
tnOamPingCtlLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingCtlLastChanged.setStatus(_A)
class _TnOamPingCtlVRtrID_Type(TmnxVRtrID):defaultValue=1
_TnOamPingCtlVRtrID_Type.__name__=_W
_TnOamPingCtlVRtrID_Object=MibTableColumn
tnOamPingCtlVRtrID=_TnOamPingCtlVRtrID_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,31),_TnOamPingCtlVRtrID_Type())
tnOamPingCtlVRtrID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlVRtrID.setStatus(_A)
class _TnOamPingCtlTgtAddrType_Type(InetAddressType):defaultValue=0
_TnOamPingCtlTgtAddrType_Type.__name__=_L
_TnOamPingCtlTgtAddrType_Object=MibTableColumn
tnOamPingCtlTgtAddrType=_TnOamPingCtlTgtAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,32),_TnOamPingCtlTgtAddrType_Type())
tnOamPingCtlTgtAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlTgtAddrType.setStatus(_A)
class _TnOamPingCtlTgtAddress_Type(InetAddress):defaultHexValue=''
_TnOamPingCtlTgtAddress_Type.__name__=_G
_TnOamPingCtlTgtAddress_Object=MibTableColumn
tnOamPingCtlTgtAddress=_TnOamPingCtlTgtAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,33),_TnOamPingCtlTgtAddress_Type())
tnOamPingCtlTgtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlTgtAddress.setStatus(_A)
class _TnOamPingCtlSrcAddrType_Type(InetAddressType):defaultValue=0
_TnOamPingCtlSrcAddrType_Type.__name__=_L
_TnOamPingCtlSrcAddrType_Object=MibTableColumn
tnOamPingCtlSrcAddrType=_TnOamPingCtlSrcAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,34),_TnOamPingCtlSrcAddrType_Type())
tnOamPingCtlSrcAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlSrcAddrType.setStatus(_A)
class _TnOamPingCtlSrcAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamPingCtlSrcAddress_Type.__name__=_G
_TnOamPingCtlSrcAddress_Object=MibTableColumn
tnOamPingCtlSrcAddress=_TnOamPingCtlSrcAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,35),_TnOamPingCtlSrcAddress_Type())
tnOamPingCtlSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlSrcAddress.setStatus(_A)
class _TnOamPingCtlDnsName_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnOamPingCtlDnsName_Type.__name__=_Q
_TnOamPingCtlDnsName_Object=MibTableColumn
tnOamPingCtlDnsName=_TnOamPingCtlDnsName_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,36),_TnOamPingCtlDnsName_Type())
tnOamPingCtlDnsName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlDnsName.setStatus(_A)
class _TnOamPingCtlDNSRecord_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4Arecord',1),('ipv6AAAArecord',2)))
_TnOamPingCtlDNSRecord_Type.__name__=_I
_TnOamPingCtlDNSRecord_Object=MibTableColumn
tnOamPingCtlDNSRecord=_TnOamPingCtlDNSRecord_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,37),_TnOamPingCtlDNSRecord_Type())
tnOamPingCtlDNSRecord.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlDNSRecord.setStatus(_A)
class _TnOamPingCtlIntervalUnits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_y,1),('centiseconds',2),('decimilliseconds',3)))
_TnOamPingCtlIntervalUnits_Type.__name__=_I
_TnOamPingCtlIntervalUnits_Object=MibTableColumn
tnOamPingCtlIntervalUnits=_TnOamPingCtlIntervalUnits_Object((1,3,6,1,4,1,7483,6,1,2,11,1,4,1,38),_TnOamPingCtlIntervalUnits_Type())
tnOamPingCtlIntervalUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamPingCtlIntervalUnits.setStatus(_A)
_TnOamPingResultsTable_Object=MibTable
tnOamPingResultsTable=_TnOamPingResultsTable_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6))
if mibBuilder.loadTexts:tnOamPingResultsTable.setStatus(_A)
_TnOamPingResultsEntry_Object=MibTableRow
tnOamPingResultsEntry=_TnOamPingResultsEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1))
tnOamPingResultsEntry.setIndexNames((0,_J,_K),(0,_E,_S),(0,_E,_z))
if mibBuilder.loadTexts:tnOamPingResultsEntry.setStatus(_A)
class _TnOamPingResultsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_TnOamPingResultsOperStatus_Type.__name__=_I
_TnOamPingResultsOperStatus_Object=MibTableColumn
tnOamPingResultsOperStatus=_TnOamPingResultsOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,1),_TnOamPingResultsOperStatus_Type())
tnOamPingResultsOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsOperStatus.setStatus(_A)
_TnOamPingResultsMinRtt_Type=Unsigned32
_TnOamPingResultsMinRtt_Object=MibTableColumn
tnOamPingResultsMinRtt=_TnOamPingResultsMinRtt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,4),_TnOamPingResultsMinRtt_Type())
tnOamPingResultsMinRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsMinRtt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsMinRtt.setUnits(_H)
_TnOamPingResultsMaxRtt_Type=Unsigned32
_TnOamPingResultsMaxRtt_Object=MibTableColumn
tnOamPingResultsMaxRtt=_TnOamPingResultsMaxRtt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,5),_TnOamPingResultsMaxRtt_Type())
tnOamPingResultsMaxRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsMaxRtt.setUnits(_H)
_TnOamPingResultsAverageRtt_Type=Unsigned32
_TnOamPingResultsAverageRtt_Object=MibTableColumn
tnOamPingResultsAverageRtt=_TnOamPingResultsAverageRtt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,6),_TnOamPingResultsAverageRtt_Type())
tnOamPingResultsAverageRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsAverageRtt.setUnits(_H)
_TnOamPingResultsRttSumOfSquares_Type=Unsigned32
_TnOamPingResultsRttSumOfSquares_Object=MibTableColumn
tnOamPingResultsRttSumOfSquares=_TnOamPingResultsRttSumOfSquares_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,7),_TnOamPingResultsRttSumOfSquares_Type())
tnOamPingResultsRttSumOfSquares.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsRttSumOfSquares.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsRttSumOfSquares.setUnits(_T)
_TnOamPingResultsMtuResponseSize_Type=Unsigned32
_TnOamPingResultsMtuResponseSize_Object=MibTableColumn
tnOamPingResultsMtuResponseSize=_TnOamPingResultsMtuResponseSize_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,8),_TnOamPingResultsMtuResponseSize_Type())
tnOamPingResultsMtuResponseSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsMtuResponseSize.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsMtuResponseSize.setUnits(_d)
class _TnOamPingResultsSvcPing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_AC,0),('failed',1),('success',2)))
_TnOamPingResultsSvcPing_Type.__name__=_I
_TnOamPingResultsSvcPing_Object=MibTableColumn
tnOamPingResultsSvcPing=_TnOamPingResultsSvcPing_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,9),_TnOamPingResultsSvcPing_Type())
tnOamPingResultsSvcPing.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsSvcPing.setStatus(_A)
_TnOamPingResultsProbeResponses_Type=Unsigned32
_TnOamPingResultsProbeResponses_Object=MibTableColumn
tnOamPingResultsProbeResponses=_TnOamPingResultsProbeResponses_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,10),_TnOamPingResultsProbeResponses_Type())
tnOamPingResultsProbeResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsProbeResponses.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsProbeResponses.setUnits('responses')
_TnOamPingResultsSentProbes_Type=Unsigned32
_TnOamPingResultsSentProbes_Object=MibTableColumn
tnOamPingResultsSentProbes=_TnOamPingResultsSentProbes_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,11),_TnOamPingResultsSentProbes_Type())
tnOamPingResultsSentProbes.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsSentProbes.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsSentProbes.setUnits(_f)
_TnOamPingResultsLastGoodProbe_Type=DateAndTime
_TnOamPingResultsLastGoodProbe_Object=MibTableColumn
tnOamPingResultsLastGoodProbe=_TnOamPingResultsLastGoodProbe_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,12),_TnOamPingResultsLastGoodProbe_Type())
tnOamPingResultsLastGoodProbe.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsLastGoodProbe.setStatus(_A)
class _TnOamPingResultsLastRespHeader_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(100,100));fixedLength=100
_TnOamPingResultsLastRespHeader_Type.__name__=_Q
_TnOamPingResultsLastRespHeader_Object=MibTableColumn
tnOamPingResultsLastRespHeader=_TnOamPingResultsLastRespHeader_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,13),_TnOamPingResultsLastRespHeader_Type())
tnOamPingResultsLastRespHeader.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsLastRespHeader.setStatus(_F)
_TnOamPingResultsMinTt_Type=Integer32
_TnOamPingResultsMinTt_Object=MibTableColumn
tnOamPingResultsMinTt=_TnOamPingResultsMinTt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,14),_TnOamPingResultsMinTt_Type())
tnOamPingResultsMinTt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsMinTt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsMinTt.setUnits(_H)
_TnOamPingResultsMaxTt_Type=Integer32
_TnOamPingResultsMaxTt_Object=MibTableColumn
tnOamPingResultsMaxTt=_TnOamPingResultsMaxTt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,15),_TnOamPingResultsMaxTt_Type())
tnOamPingResultsMaxTt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsMaxTt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsMaxTt.setUnits(_H)
_TnOamPingResultsAverageTt_Type=Integer32
_TnOamPingResultsAverageTt_Object=MibTableColumn
tnOamPingResultsAverageTt=_TnOamPingResultsAverageTt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,16),_TnOamPingResultsAverageTt_Type())
tnOamPingResultsAverageTt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsAverageTt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsAverageTt.setUnits(_H)
_TnOamPingResultsTtSumOfSquares_Type=Unsigned32
_TnOamPingResultsTtSumOfSquares_Object=MibTableColumn
tnOamPingResultsTtSumOfSquares=_TnOamPingResultsTtSumOfSquares_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,17),_TnOamPingResultsTtSumOfSquares_Type())
tnOamPingResultsTtSumOfSquares.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsTtSumOfSquares.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsTtSumOfSquares.setUnits(_T)
_TnOamPingResultsMinInTt_Type=Integer32
_TnOamPingResultsMinInTt_Object=MibTableColumn
tnOamPingResultsMinInTt=_TnOamPingResultsMinInTt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,18),_TnOamPingResultsMinInTt_Type())
tnOamPingResultsMinInTt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsMinInTt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsMinInTt.setUnits(_H)
_TnOamPingResultsMaxInTt_Type=Integer32
_TnOamPingResultsMaxInTt_Object=MibTableColumn
tnOamPingResultsMaxInTt=_TnOamPingResultsMaxInTt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,19),_TnOamPingResultsMaxInTt_Type())
tnOamPingResultsMaxInTt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsMaxInTt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsMaxInTt.setUnits(_H)
_TnOamPingResultsAverageInTt_Type=Integer32
_TnOamPingResultsAverageInTt_Object=MibTableColumn
tnOamPingResultsAverageInTt=_TnOamPingResultsAverageInTt_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,20),_TnOamPingResultsAverageInTt_Type())
tnOamPingResultsAverageInTt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsAverageInTt.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsAverageInTt.setUnits(_H)
_TnOamPingResultsInTtSumOfSqrs_Type=Unsigned32
_TnOamPingResultsInTtSumOfSqrs_Object=MibTableColumn
tnOamPingResultsInTtSumOfSqrs=_TnOamPingResultsInTtSumOfSqrs_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,21),_TnOamPingResultsInTtSumOfSqrs_Type())
tnOamPingResultsInTtSumOfSqrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsInTtSumOfSqrs.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsInTtSumOfSqrs.setUnits(_T)
_TnOamPingResultsOutJitter_Type=Integer32
_TnOamPingResultsOutJitter_Object=MibTableColumn
tnOamPingResultsOutJitter=_TnOamPingResultsOutJitter_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,22),_TnOamPingResultsOutJitter_Type())
tnOamPingResultsOutJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsOutJitter.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsOutJitter.setUnits(_H)
_TnOamPingResultsInJitter_Type=Integer32
_TnOamPingResultsInJitter_Object=MibTableColumn
tnOamPingResultsInJitter=_TnOamPingResultsInJitter_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,23),_TnOamPingResultsInJitter_Type())
tnOamPingResultsInJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsInJitter.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsInJitter.setUnits(_H)
_TnOamPingResultsRtJitter_Type=Integer32
_TnOamPingResultsRtJitter_Object=MibTableColumn
tnOamPingResultsRtJitter=_TnOamPingResultsRtJitter_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,24),_TnOamPingResultsRtJitter_Type())
tnOamPingResultsRtJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsRtJitter.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsRtJitter.setUnits(_H)
_TnOamPingResultsProbeTimeouts_Type=Unsigned32
_TnOamPingResultsProbeTimeouts_Object=MibTableColumn
tnOamPingResultsProbeTimeouts=_TnOamPingResultsProbeTimeouts_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,25),_TnOamPingResultsProbeTimeouts_Type())
tnOamPingResultsProbeTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsProbeTimeouts.setStatus(_A)
_TnOamPingResultsProbeFailures_Type=Unsigned32
_TnOamPingResultsProbeFailures_Object=MibTableColumn
tnOamPingResultsProbeFailures=_TnOamPingResultsProbeFailures_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,26),_TnOamPingResultsProbeFailures_Type())
tnOamPingResultsProbeFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsProbeFailures.setStatus(_A)
class _TnOamPingResultsTestRunIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TnOamPingResultsTestRunIndex_Type.__name__=_D
_TnOamPingResultsTestRunIndex_Object=MibTableColumn
tnOamPingResultsTestRunIndex=_TnOamPingResultsTestRunIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,27),_TnOamPingResultsTestRunIndex_Type())
tnOamPingResultsTestRunIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamPingResultsTestRunIndex.setStatus(_A)
_TnOamPingResultsRttOFSumSquares_Type=Counter32
_TnOamPingResultsRttOFSumSquares_Object=MibTableColumn
tnOamPingResultsRttOFSumSquares=_TnOamPingResultsRttOFSumSquares_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,28),_TnOamPingResultsRttOFSumSquares_Type())
tnOamPingResultsRttOFSumSquares.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsRttOFSumSquares.setStatus(_A)
_TnOamPingResultsRttHCSumSquares_Type=Counter64
_TnOamPingResultsRttHCSumSquares_Object=MibTableColumn
tnOamPingResultsRttHCSumSquares=_TnOamPingResultsRttHCSumSquares_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,29),_TnOamPingResultsRttHCSumSquares_Type())
tnOamPingResultsRttHCSumSquares.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsRttHCSumSquares.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsRttHCSumSquares.setUnits(_T)
_TnOamPingResultsTtOFSumSquares_Type=Counter32
_TnOamPingResultsTtOFSumSquares_Object=MibTableColumn
tnOamPingResultsTtOFSumSquares=_TnOamPingResultsTtOFSumSquares_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,30),_TnOamPingResultsTtOFSumSquares_Type())
tnOamPingResultsTtOFSumSquares.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsTtOFSumSquares.setStatus(_A)
_TnOamPingResultsTtHCSumSquares_Type=Counter64
_TnOamPingResultsTtHCSumSquares_Object=MibTableColumn
tnOamPingResultsTtHCSumSquares=_TnOamPingResultsTtHCSumSquares_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,31),_TnOamPingResultsTtHCSumSquares_Type())
tnOamPingResultsTtHCSumSquares.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsTtHCSumSquares.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsTtHCSumSquares.setUnits(_T)
_TnOamPingResultsInTtOFSumSqrs_Type=Counter32
_TnOamPingResultsInTtOFSumSqrs_Object=MibTableColumn
tnOamPingResultsInTtOFSumSqrs=_TnOamPingResultsInTtOFSumSqrs_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,32),_TnOamPingResultsInTtOFSumSqrs_Type())
tnOamPingResultsInTtOFSumSqrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsInTtOFSumSqrs.setStatus(_A)
_TnOamPingResultsInTtHCSumSqrs_Type=Counter64
_TnOamPingResultsInTtHCSumSqrs_Object=MibTableColumn
tnOamPingResultsInTtHCSumSqrs=_TnOamPingResultsInTtHCSumSqrs_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,33),_TnOamPingResultsInTtHCSumSqrs_Type())
tnOamPingResultsInTtHCSumSqrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsInTtHCSumSqrs.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingResultsInTtHCSumSqrs.setUnits(_T)
_TnOamPingResultsTestRunResult_Type=TmnxOamTestResult
_TnOamPingResultsTestRunResult_Object=MibTableColumn
tnOamPingResultsTestRunResult=_TnOamPingResultsTestRunResult_Object((1,3,6,1,4,1,7483,6,1,2,11,1,6,1,34),_TnOamPingResultsTestRunResult_Type())
tnOamPingResultsTestRunResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingResultsTestRunResult.setStatus(_A)
_TnOamPingHistoryTable_Object=MibTable
tnOamPingHistoryTable=_TnOamPingHistoryTable_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8))
if mibBuilder.loadTexts:tnOamPingHistoryTable.setStatus(_A)
_TnOamPingHistoryEntry_Object=MibTableRow
tnOamPingHistoryEntry=_TnOamPingHistoryEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1))
tnOamPingHistoryEntry.setIndexNames((0,_J,_K),(0,_E,_S),(0,_E,_z),(0,_E,_AF))
if mibBuilder.loadTexts:tnOamPingHistoryEntry.setStatus(_A)
class _TnOamPingHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TnOamPingHistoryIndex_Type.__name__=_D
_TnOamPingHistoryIndex_Object=MibTableColumn
tnOamPingHistoryIndex=_TnOamPingHistoryIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,1),_TnOamPingHistoryIndex_Type())
tnOamPingHistoryIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamPingHistoryIndex.setStatus(_A)
_TnOamPingHistoryResponse_Type=Unsigned32
_TnOamPingHistoryResponse_Object=MibTableColumn
tnOamPingHistoryResponse=_TnOamPingHistoryResponse_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,2),_TnOamPingHistoryResponse_Type())
tnOamPingHistoryResponse.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryResponse.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingHistoryResponse.setUnits(_H)
_TnOamPingHistoryOneWayTime_Type=Integer32
_TnOamPingHistoryOneWayTime_Object=MibTableColumn
tnOamPingHistoryOneWayTime=_TnOamPingHistoryOneWayTime_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,3),_TnOamPingHistoryOneWayTime_Type())
tnOamPingHistoryOneWayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryOneWayTime.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingHistoryOneWayTime.setUnits(_H)
_TnOamPingHistorySize_Type=Unsigned32
_TnOamPingHistorySize_Object=MibTableColumn
tnOamPingHistorySize=_TnOamPingHistorySize_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,4),_TnOamPingHistorySize_Type())
tnOamPingHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistorySize.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingHistorySize.setUnits(_Y)
_TnOamPingHistoryStatus_Type=TmnxOamResponseStatus
_TnOamPingHistoryStatus_Object=MibTableColumn
tnOamPingHistoryStatus=_TnOamPingHistoryStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,5),_TnOamPingHistoryStatus_Type())
tnOamPingHistoryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryStatus.setStatus(_A)
_TnOamPingHistoryTime_Type=DateAndTime
_TnOamPingHistoryTime_Object=MibTableColumn
tnOamPingHistoryTime=_TnOamPingHistoryTime_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,6),_TnOamPingHistoryTime_Type())
tnOamPingHistoryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryTime.setStatus(_A)
_TnOamPingHistoryReturnCode_Type=Integer32
_TnOamPingHistoryReturnCode_Object=MibTableColumn
tnOamPingHistoryReturnCode=_TnOamPingHistoryReturnCode_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,7),_TnOamPingHistoryReturnCode_Type())
tnOamPingHistoryReturnCode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryReturnCode.setStatus(_A)
_TnOamPingHistorySrcIpAddress_Type=IpAddress
_TnOamPingHistorySrcIpAddress_Object=MibTableColumn
tnOamPingHistorySrcIpAddress=_TnOamPingHistorySrcIpAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,8),_TnOamPingHistorySrcIpAddress_Type())
tnOamPingHistorySrcIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistorySrcIpAddress.setStatus(_F)
_TnOamPingHistAddressType_Type=TmnxOamAddressType
_TnOamPingHistAddressType_Object=MibTableColumn
tnOamPingHistAddressType=_TnOamPingHistAddressType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,9),_TnOamPingHistAddressType_Type())
tnOamPingHistAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistAddressType.setStatus(_A)
_TnOamPingHistSapId_Type=TmnxStrSapId
_TnOamPingHistSapId_Object=MibTableColumn
tnOamPingHistSapId=_TnOamPingHistSapId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,10),_TnOamPingHistSapId_Type())
tnOamPingHistSapId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistSapId.setStatus(_A)
_TnOamPingHistoryVersion_Type=Unsigned32
_TnOamPingHistoryVersion_Object=MibTableColumn
tnOamPingHistoryVersion=_TnOamPingHistoryVersion_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,12),_TnOamPingHistoryVersion_Type())
tnOamPingHistoryVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryVersion.setStatus(_A)
_TnOamPingHistoryCpeMacAddr_Type=MacAddress
_TnOamPingHistoryCpeMacAddr_Object=MibTableColumn
tnOamPingHistoryCpeMacAddr=_TnOamPingHistoryCpeMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,13),_TnOamPingHistoryCpeMacAddr_Type())
tnOamPingHistoryCpeMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryCpeMacAddr.setStatus(_A)
_TnOamPingHistoryRespSvcId_Type=TmnxServId
_TnOamPingHistoryRespSvcId_Object=MibTableColumn
tnOamPingHistoryRespSvcId=_TnOamPingHistoryRespSvcId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,14),_TnOamPingHistoryRespSvcId_Type())
tnOamPingHistoryRespSvcId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryRespSvcId.setStatus(_A)
_TnOamPingHistorySequence_Type=Unsigned32
_TnOamPingHistorySequence_Object=MibTableColumn
tnOamPingHistorySequence=_TnOamPingHistorySequence_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,15),_TnOamPingHistorySequence_Type())
tnOamPingHistorySequence.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistorySequence.setStatus(_A)
_TnOamPingHistoryIfIndex_Type=InterfaceIndexOrZero
_TnOamPingHistoryIfIndex_Object=MibTableColumn
tnOamPingHistoryIfIndex=_TnOamPingHistoryIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,16),_TnOamPingHistoryIfIndex_Type())
tnOamPingHistoryIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryIfIndex.setStatus(_A)
_TnOamPingHistoryDataLen_Type=Unsigned32
_TnOamPingHistoryDataLen_Object=MibTableColumn
tnOamPingHistoryDataLen=_TnOamPingHistoryDataLen_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,17),_TnOamPingHistoryDataLen_Type())
tnOamPingHistoryDataLen.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryDataLen.setStatus(_A)
_TnOamPingHistoryRespPlane_Type=TmnxOamTestResponsePlane
_TnOamPingHistoryRespPlane_Object=MibTableColumn
tnOamPingHistoryRespPlane=_TnOamPingHistoryRespPlane_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,18),_TnOamPingHistoryRespPlane_Type())
tnOamPingHistoryRespPlane.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryRespPlane.setStatus(_A)
class _TnOamPingHistoryReqHdr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,150))
_TnOamPingHistoryReqHdr_Type.__name__=_Q
_TnOamPingHistoryReqHdr_Object=MibTableColumn
tnOamPingHistoryReqHdr=_TnOamPingHistoryReqHdr_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,19),_TnOamPingHistoryReqHdr_Type())
tnOamPingHistoryReqHdr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryReqHdr.setStatus(_F)
class _TnOamPingHistoryRespHdr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,150))
_TnOamPingHistoryRespHdr_Type.__name__=_Q
_TnOamPingHistoryRespHdr_Object=MibTableColumn
tnOamPingHistoryRespHdr=_TnOamPingHistoryRespHdr_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,20),_TnOamPingHistoryRespHdr_Type())
tnOamPingHistoryRespHdr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryRespHdr.setStatus(_A)
_TnOamPingHistoryDnsAddrType_Type=InetAddressType
_TnOamPingHistoryDnsAddrType_Object=MibTableColumn
tnOamPingHistoryDnsAddrType=_TnOamPingHistoryDnsAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,21),_TnOamPingHistoryDnsAddrType_Type())
tnOamPingHistoryDnsAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryDnsAddrType.setStatus(_A)
class _TnOamPingHistoryDnsAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamPingHistoryDnsAddress_Type.__name__=_G
_TnOamPingHistoryDnsAddress_Object=MibTableColumn
tnOamPingHistoryDnsAddress=_TnOamPingHistoryDnsAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,22),_TnOamPingHistoryDnsAddress_Type())
tnOamPingHistoryDnsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryDnsAddress.setStatus(_A)
_TnOamPingHistorySrcAddrType_Type=InetAddressType
_TnOamPingHistorySrcAddrType_Object=MibTableColumn
tnOamPingHistorySrcAddrType=_TnOamPingHistorySrcAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,23),_TnOamPingHistorySrcAddrType_Type())
tnOamPingHistorySrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistorySrcAddrType.setStatus(_A)
class _TnOamPingHistorySrcAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_TnOamPingHistorySrcAddress_Type.__name__=_G
_TnOamPingHistorySrcAddress_Object=MibTableColumn
tnOamPingHistorySrcAddress=_TnOamPingHistorySrcAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,24),_TnOamPingHistorySrcAddress_Type())
tnOamPingHistorySrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistorySrcAddress.setStatus(_A)
_TnOamPingHistoryInOneWayTime_Type=Integer32
_TnOamPingHistoryInOneWayTime_Object=MibTableColumn
tnOamPingHistoryInOneWayTime=_TnOamPingHistoryInOneWayTime_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,25),_TnOamPingHistoryInOneWayTime_Type())
tnOamPingHistoryInOneWayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryInOneWayTime.setStatus(_A)
if mibBuilder.loadTexts:tnOamPingHistoryInOneWayTime.setUnits(_H)
_TnOamPingHistoryLspName_Type=TLNamedItemOrEmpty
_TnOamPingHistoryLspName_Object=MibTableColumn
tnOamPingHistoryLspName=_TnOamPingHistoryLspName_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,26),_TnOamPingHistoryLspName_Type())
tnOamPingHistoryLspName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryLspName.setStatus(_A)
_TnOamPingHistNextHopAddrType_Type=InetAddressType
_TnOamPingHistNextHopAddrType_Object=MibTableColumn
tnOamPingHistNextHopAddrType=_TnOamPingHistNextHopAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,27),_TnOamPingHistNextHopAddrType_Type())
tnOamPingHistNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistNextHopAddrType.setStatus(_A)
class _TnOamPingHistNextHopAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_TnOamPingHistNextHopAddress_Type.__name__=_G
_TnOamPingHistNextHopAddress_Object=MibTableColumn
tnOamPingHistNextHopAddress=_TnOamPingHistNextHopAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,28),_TnOamPingHistNextHopAddress_Type())
tnOamPingHistNextHopAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistNextHopAddress.setStatus(_A)
_TnOamPingHistorySrcGlobalId_Type=TmnxMplsTpGlobalID
_TnOamPingHistorySrcGlobalId_Object=MibTableColumn
tnOamPingHistorySrcGlobalId=_TnOamPingHistorySrcGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,29),_TnOamPingHistorySrcGlobalId_Type())
tnOamPingHistorySrcGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistorySrcGlobalId.setStatus(_A)
_TnOamPingHistorySrcNodeId_Type=TmnxMplsTpNodeID
_TnOamPingHistorySrcNodeId_Object=MibTableColumn
tnOamPingHistorySrcNodeId=_TnOamPingHistorySrcNodeId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,30),_TnOamPingHistorySrcNodeId_Type())
tnOamPingHistorySrcNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistorySrcNodeId.setStatus(_A)
_TnOamPingHistorySdpBindId_Type=TNamedItemOrEmpty
_TnOamPingHistorySdpBindId_Object=MibTableColumn
tnOamPingHistorySdpBindId=_TnOamPingHistorySdpBindId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,31),_TnOamPingHistorySdpBindId_Type())
tnOamPingHistorySdpBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistorySdpBindId.setStatus(_A)
_TnOamPingHistoryRtrnSubcode_Type=Unsigned32
_TnOamPingHistoryRtrnSubcode_Object=MibTableColumn
tnOamPingHistoryRtrnSubcode=_TnOamPingHistoryRtrnSubcode_Object((1,3,6,1,4,1,7483,6,1,2,11,1,8,1,32),_TnOamPingHistoryRtrnSubcode_Type())
tnOamPingHistoryRtrnSubcode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamPingHistoryRtrnSubcode.setStatus(_A)
_TnOamLspPingCtlTable_Object=MibTable
tnOamLspPingCtlTable=_TnOamLspPingCtlTable_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16))
if mibBuilder.loadTexts:tnOamLspPingCtlTable.setStatus(_A)
_TnOamLspPingCtlEntry_Object=MibTableRow
tnOamLspPingCtlEntry=_TnOamLspPingCtlEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1))
tnOamLspPingCtlEntry.setIndexNames((0,_J,_K),(0,_E,_S))
if mibBuilder.loadTexts:tnOamLspPingCtlEntry.setStatus(_A)
class _TnOamLspPingCtlVRtrID_Type(TmnxVRtrID):defaultValue=1
_TnOamLspPingCtlVRtrID_Type.__name__=_W
_TnOamLspPingCtlVRtrID_Object=MibTableColumn
tnOamLspPingCtlVRtrID=_TnOamLspPingCtlVRtrID_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,1),_TnOamLspPingCtlVRtrID_Type())
tnOamLspPingCtlVRtrID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlVRtrID.setStatus(_F)
class _TnOamLspPingCtlLspName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnOamLspPingCtlLspName_Type.__name__=_O
_TnOamLspPingCtlLspName_Object=MibTableColumn
tnOamLspPingCtlLspName=_TnOamLspPingCtlLspName_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,2),_TnOamLspPingCtlLspName_Type())
tnOamLspPingCtlLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlLspName.setStatus(_A)
class _TnOamLspPingCtlReturnLsp_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnOamLspPingCtlReturnLsp_Type.__name__=_O
_TnOamLspPingCtlReturnLsp_Object=MibTableColumn
tnOamLspPingCtlReturnLsp=_TnOamLspPingCtlReturnLsp_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,3),_TnOamLspPingCtlReturnLsp_Type())
tnOamLspPingCtlReturnLsp.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlReturnLsp.setStatus(_F)
class _TnOamLspPingCtlTtl_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TnOamLspPingCtlTtl_Type.__name__=_D
_TnOamLspPingCtlTtl_Object=MibTableColumn
tnOamLspPingCtlTtl=_TnOamLspPingCtlTtl_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,4),_TnOamLspPingCtlTtl_Type())
tnOamLspPingCtlTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlTtl.setStatus(_A)
if mibBuilder.loadTexts:tnOamLspPingCtlTtl.setUnits(_A0)
class _TnOamLspPingCtlPathName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnOamLspPingCtlPathName_Type.__name__=_O
_TnOamLspPingCtlPathName_Object=MibTableColumn
tnOamLspPingCtlPathName=_TnOamLspPingCtlPathName_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,5),_TnOamLspPingCtlPathName_Type())
tnOamLspPingCtlPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlPathName.setStatus(_A)
class _TnOamLspPingCtlLdpIpPrefix_Type(IpAddress):defaultHexValue=_e
_TnOamLspPingCtlLdpIpPrefix_Type.__name__=_U
_TnOamLspPingCtlLdpIpPrefix_Object=MibTableColumn
tnOamLspPingCtlLdpIpPrefix=_TnOamLspPingCtlLdpIpPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,6),_TnOamLspPingCtlLdpIpPrefix_Type())
tnOamLspPingCtlLdpIpPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlLdpIpPrefix.setStatus(_F)
class _TnOamLspPingCtlLdpIpPrefixLen_Type(IpAddressPrefixLength):defaultValue=32
_TnOamLspPingCtlLdpIpPrefixLen_Type.__name__=_m
_TnOamLspPingCtlLdpIpPrefixLen_Object=MibTableColumn
tnOamLspPingCtlLdpIpPrefixLen=_TnOamLspPingCtlLdpIpPrefixLen_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,7),_TnOamLspPingCtlLdpIpPrefixLen_Type())
tnOamLspPingCtlLdpIpPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlLdpIpPrefixLen.setStatus(_F)
class _TnOamLspPingCtlLdpPrefixType_Type(InetAddressType):defaultValue=0
_TnOamLspPingCtlLdpPrefixType_Type.__name__=_L
_TnOamLspPingCtlLdpPrefixType_Object=MibTableColumn
tnOamLspPingCtlLdpPrefixType=_TnOamLspPingCtlLdpPrefixType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,8),_TnOamLspPingCtlLdpPrefixType_Type())
tnOamLspPingCtlLdpPrefixType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlLdpPrefixType.setStatus(_A)
class _TnOamLspPingCtlLdpPrefix_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamLspPingCtlLdpPrefix_Type.__name__=_G
_TnOamLspPingCtlLdpPrefix_Object=MibTableColumn
tnOamLspPingCtlLdpPrefix=_TnOamLspPingCtlLdpPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,9),_TnOamLspPingCtlLdpPrefix_Type())
tnOamLspPingCtlLdpPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlLdpPrefix.setStatus(_A)
class _TnOamLspPingCtlLdpPrefixLen_Type(InetAddressPrefixLength):defaultValue=32
_TnOamLspPingCtlLdpPrefixLen_Type.__name__=_j
_TnOamLspPingCtlLdpPrefixLen_Object=MibTableColumn
tnOamLspPingCtlLdpPrefixLen=_TnOamLspPingCtlLdpPrefixLen_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,10),_TnOamLspPingCtlLdpPrefixLen_Type())
tnOamLspPingCtlLdpPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlLdpPrefixLen.setStatus(_A)
class _TnOamLspPingCtlPathDestType_Type(InetAddressType):defaultValue=0
_TnOamLspPingCtlPathDestType_Type.__name__=_L
_TnOamLspPingCtlPathDestType_Object=MibTableColumn
tnOamLspPingCtlPathDestType=_TnOamLspPingCtlPathDestType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,11),_TnOamLspPingCtlPathDestType_Type())
tnOamLspPingCtlPathDestType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlPathDestType.setStatus(_A)
class _TnOamLspPingCtlPathDest_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamLspPingCtlPathDest_Type.__name__=_G
_TnOamLspPingCtlPathDest_Object=MibTableColumn
tnOamLspPingCtlPathDest=_TnOamLspPingCtlPathDest_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,12),_TnOamLspPingCtlPathDest_Type())
tnOamLspPingCtlPathDest.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlPathDest.setStatus(_A)
class _TnOamLspPingCtlNhIntfName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnOamLspPingCtlNhIntfName_Type.__name__=_O
_TnOamLspPingCtlNhIntfName_Object=MibTableColumn
tnOamLspPingCtlNhIntfName=_TnOamLspPingCtlNhIntfName_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,13),_TnOamLspPingCtlNhIntfName_Type())
tnOamLspPingCtlNhIntfName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlNhIntfName.setStatus(_A)
class _TnOamLspPingCtlNhAddressType_Type(InetAddressType):defaultValue=0
_TnOamLspPingCtlNhAddressType_Type.__name__=_L
_TnOamLspPingCtlNhAddressType_Object=MibTableColumn
tnOamLspPingCtlNhAddressType=_TnOamLspPingCtlNhAddressType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,14),_TnOamLspPingCtlNhAddressType_Type())
tnOamLspPingCtlNhAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlNhAddressType.setStatus(_A)
class _TnOamLspPingCtlNhAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamLspPingCtlNhAddress_Type.__name__=_G
_TnOamLspPingCtlNhAddress_Object=MibTableColumn
tnOamLspPingCtlNhAddress=_TnOamLspPingCtlNhAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,15),_TnOamLspPingCtlNhAddress_Type())
tnOamLspPingCtlNhAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlNhAddress.setStatus(_A)
class _TnOamLspPingCtlTestSubMode_Type(TmnxOamLspTestSubMode):defaultValue=1
_TnOamLspPingCtlTestSubMode_Type.__name__=_A1
_TnOamLspPingCtlTestSubMode_Object=MibTableColumn
tnOamLspPingCtlTestSubMode=_TnOamLspPingCtlTestSubMode_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,16),_TnOamLspPingCtlTestSubMode_Type())
tnOamLspPingCtlTestSubMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlTestSubMode.setStatus(_A)
class _TnOamLspPingCtlMplsTpPathType_Type(TmnxOamMplsTpPathType):defaultValue=3
_TnOamLspPingCtlMplsTpPathType_Type.__name__=_A2
_TnOamLspPingCtlMplsTpPathType_Object=MibTableColumn
tnOamLspPingCtlMplsTpPathType=_TnOamLspPingCtlMplsTpPathType_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,17),_TnOamLspPingCtlMplsTpPathType_Type())
tnOamLspPingCtlMplsTpPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlMplsTpPathType.setStatus(_A)
class _TnOamLspPingCtlMplsTpGlobalId_Type(TmnxMplsTpGlobalID):defaultValue=0
_TnOamLspPingCtlMplsTpGlobalId_Type.__name__=_q
_TnOamLspPingCtlMplsTpGlobalId_Object=MibTableColumn
tnOamLspPingCtlMplsTpGlobalId=_TnOamLspPingCtlMplsTpGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,18),_TnOamLspPingCtlMplsTpGlobalId_Type())
tnOamLspPingCtlMplsTpGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlMplsTpGlobalId.setStatus(_A)
class _TnOamLspPingCtlMplsTpNodeId_Type(TmnxMplsTpNodeID):defaultValue=0
_TnOamLspPingCtlMplsTpNodeId_Type.__name__=_r
_TnOamLspPingCtlMplsTpNodeId_Object=MibTableColumn
tnOamLspPingCtlMplsTpNodeId=_TnOamLspPingCtlMplsTpNodeId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,19),_TnOamLspPingCtlMplsTpNodeId_Type())
tnOamLspPingCtlMplsTpNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlMplsTpNodeId.setStatus(_A)
class _TnOamLspPingCtlAssocChannel_Type(TmnxOamLspAssocChannel):defaultValue=1
_TnOamLspPingCtlAssocChannel_Type.__name__=_A3
_TnOamLspPingCtlAssocChannel_Object=MibTableColumn
tnOamLspPingCtlAssocChannel=_TnOamLspPingCtlAssocChannel_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,20),_TnOamLspPingCtlAssocChannel_Type())
tnOamLspPingCtlAssocChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlAssocChannel.setStatus(_A)
class _TnOamLspPingCtlForce_Type(TruthValue):defaultValue=2
_TnOamLspPingCtlForce_Type.__name__=_M
_TnOamLspPingCtlForce_Object=MibTableColumn
tnOamLspPingCtlForce=_TnOamLspPingCtlForce_Object((1,3,6,1,4,1,7483,6,1,2,11,1,16,1,21),_TnOamLspPingCtlForce_Type())
tnOamLspPingCtlForce.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspPingCtlForce.setStatus(_A)
_TnOamVccvPingCtlTable_Object=MibTable
tnOamVccvPingCtlTable=_TnOamVccvPingCtlTable_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32))
if mibBuilder.loadTexts:tnOamVccvPingCtlTable.setStatus(_A)
_TnOamVccvPingCtlEntry_Object=MibTableRow
tnOamVccvPingCtlEntry=_TnOamVccvPingCtlEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1))
tnOamVccvPingCtlEntry.setIndexNames((0,_J,_K),(0,_E,_S))
if mibBuilder.loadTexts:tnOamVccvPingCtlEntry.setStatus(_A)
class _TnOamVccvPingCtlSdpIdVcId_Type(SdpBindId):defaultHexValue=_AG
_TnOamVccvPingCtlSdpIdVcId_Type.__name__=_n
_TnOamVccvPingCtlSdpIdVcId_Object=MibTableColumn
tnOamVccvPingCtlSdpIdVcId=_TnOamVccvPingCtlSdpIdVcId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,1),_TnOamVccvPingCtlSdpIdVcId_Type())
tnOamVccvPingCtlSdpIdVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlSdpIdVcId.setStatus(_A)
class _TnOamVccvPingCtlReplyMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('ip',2),(_AH,4)))
_TnOamVccvPingCtlReplyMode_Type.__name__=_I
_TnOamVccvPingCtlReplyMode_Object=MibTableColumn
tnOamVccvPingCtlReplyMode=_TnOamVccvPingCtlReplyMode_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,2),_TnOamVccvPingCtlReplyMode_Type())
tnOamVccvPingCtlReplyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlReplyMode.setStatus(_A)
class _TnOamVccvPingCtlPwId_Type(TmnxVcIdOrNone):defaultValue=0
_TnOamVccvPingCtlPwId_Type.__name__=_AA
_TnOamVccvPingCtlPwId_Object=MibTableColumn
tnOamVccvPingCtlPwId=_TnOamVccvPingCtlPwId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,3),_TnOamVccvPingCtlPwId_Type())
tnOamVccvPingCtlPwId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlPwId.setStatus(_A)
class _TnOamVccvPingCtlTtl_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TnOamVccvPingCtlTtl_Type.__name__=_D
_TnOamVccvPingCtlTtl_Object=MibTableColumn
tnOamVccvPingCtlTtl=_TnOamVccvPingCtlTtl_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,4),_TnOamVccvPingCtlTtl_Type())
tnOamVccvPingCtlTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlTtl.setStatus(_A)
if mibBuilder.loadTexts:tnOamVccvPingCtlTtl.setUnits(_A0)
class _TnOamVccvPingCtlSpokeSdpId_Type(TmnxSpokeSdpIdOrZero):defaultValue=0
_TnOamVccvPingCtlSpokeSdpId_Type.__name__=_t
_TnOamVccvPingCtlSpokeSdpId_Object=MibTableColumn
tnOamVccvPingCtlSpokeSdpId=_TnOamVccvPingCtlSpokeSdpId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,5),_TnOamVccvPingCtlSpokeSdpId_Type())
tnOamVccvPingCtlSpokeSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlSpokeSdpId.setStatus(_A)
class _TnOamVccvPingCtlSaiiGlobalId_Type(TmnxPwGlobalIdOrZero):defaultValue=0
_TnOamVccvPingCtlSaiiGlobalId_Type.__name__=_V
_TnOamVccvPingCtlSaiiGlobalId_Object=MibTableColumn
tnOamVccvPingCtlSaiiGlobalId=_TnOamVccvPingCtlSaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,6),_TnOamVccvPingCtlSaiiGlobalId_Type())
tnOamVccvPingCtlSaiiGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlSaiiGlobalId.setStatus(_A)
class _TnOamVccvPingCtlSaiiPrefix_Type(Unsigned32):defaultValue=0
_TnOamVccvPingCtlSaiiPrefix_Type.__name__=_D
_TnOamVccvPingCtlSaiiPrefix_Object=MibTableColumn
tnOamVccvPingCtlSaiiPrefix=_TnOamVccvPingCtlSaiiPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,7),_TnOamVccvPingCtlSaiiPrefix_Type())
tnOamVccvPingCtlSaiiPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlSaiiPrefix.setStatus(_A)
class _TnOamVccvPingCtlSaiiAcId_Type(Unsigned32):defaultValue=0
_TnOamVccvPingCtlSaiiAcId_Type.__name__=_D
_TnOamVccvPingCtlSaiiAcId_Object=MibTableColumn
tnOamVccvPingCtlSaiiAcId=_TnOamVccvPingCtlSaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,8),_TnOamVccvPingCtlSaiiAcId_Type())
tnOamVccvPingCtlSaiiAcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlSaiiAcId.setStatus(_A)
class _TnOamVccvPingCtlTaiiGlobalId_Type(TmnxPwGlobalIdOrZero):defaultValue=0
_TnOamVccvPingCtlTaiiGlobalId_Type.__name__=_V
_TnOamVccvPingCtlTaiiGlobalId_Object=MibTableColumn
tnOamVccvPingCtlTaiiGlobalId=_TnOamVccvPingCtlTaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,9),_TnOamVccvPingCtlTaiiGlobalId_Type())
tnOamVccvPingCtlTaiiGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlTaiiGlobalId.setStatus(_A)
class _TnOamVccvPingCtlTaiiPrefix_Type(Unsigned32):defaultValue=0
_TnOamVccvPingCtlTaiiPrefix_Type.__name__=_D
_TnOamVccvPingCtlTaiiPrefix_Object=MibTableColumn
tnOamVccvPingCtlTaiiPrefix=_TnOamVccvPingCtlTaiiPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,10),_TnOamVccvPingCtlTaiiPrefix_Type())
tnOamVccvPingCtlTaiiPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlTaiiPrefix.setStatus(_A)
class _TnOamVccvPingCtlTaiiAcId_Type(Unsigned32):defaultValue=0
_TnOamVccvPingCtlTaiiAcId_Type.__name__=_D
_TnOamVccvPingCtlTaiiAcId_Object=MibTableColumn
tnOamVccvPingCtlTaiiAcId=_TnOamVccvPingCtlTaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,11),_TnOamVccvPingCtlTaiiAcId_Type())
tnOamVccvPingCtlTaiiAcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlTaiiAcId.setStatus(_A)
class _TnOamVccvPingCtlMplsTpGlobalId_Type(TmnxMplsTpGlobalID):defaultValue=0
_TnOamVccvPingCtlMplsTpGlobalId_Type.__name__=_q
_TnOamVccvPingCtlMplsTpGlobalId_Object=MibTableColumn
tnOamVccvPingCtlMplsTpGlobalId=_TnOamVccvPingCtlMplsTpGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,12),_TnOamVccvPingCtlMplsTpGlobalId_Type())
tnOamVccvPingCtlMplsTpGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlMplsTpGlobalId.setStatus(_A)
class _TnOamVccvPingCtlMplsTpNodeId_Type(TmnxMplsTpNodeID):defaultValue=0
_TnOamVccvPingCtlMplsTpNodeId_Type.__name__=_r
_TnOamVccvPingCtlMplsTpNodeId_Object=MibTableColumn
tnOamVccvPingCtlMplsTpNodeId=_TnOamVccvPingCtlMplsTpNodeId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,13),_TnOamVccvPingCtlMplsTpNodeId_Type())
tnOamVccvPingCtlMplsTpNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlMplsTpNodeId.setStatus(_A)
class _TnOamVccvPingCtlTestSubMode_Type(TmnxOamVccvTestSubMode):defaultValue=1
_TnOamVccvPingCtlTestSubMode_Type.__name__=_A4
_TnOamVccvPingCtlTestSubMode_Object=MibTableColumn
tnOamVccvPingCtlTestSubMode=_TnOamVccvPingCtlTestSubMode_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,14),_TnOamVccvPingCtlTestSubMode_Type())
tnOamVccvPingCtlTestSubMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlTestSubMode.setStatus(_A)
class _TnOamVccvPingCtlAssocChannel_Type(TmnxOamVccvAssocChannel):defaultValue=1
_TnOamVccvPingCtlAssocChannel_Type.__name__=_A5
_TnOamVccvPingCtlAssocChannel_Object=MibTableColumn
tnOamVccvPingCtlAssocChannel=_TnOamVccvPingCtlAssocChannel_Object((1,3,6,1,4,1,7483,6,1,2,11,1,32,1,15),_TnOamVccvPingCtlAssocChannel_Type())
tnOamVccvPingCtlAssocChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvPingCtlAssocChannel.setStatus(_A)
_TnOamEthCfmPingCtlTable_Object=MibTable
tnOamEthCfmPingCtlTable=_TnOamEthCfmPingCtlTable_Object((1,3,6,1,4,1,7483,6,1,2,11,1,44))
if mibBuilder.loadTexts:tnOamEthCfmPingCtlTable.setStatus(_A)
_TnOamEthCfmPingCtlEntry_Object=MibTableRow
tnOamEthCfmPingCtlEntry=_TnOamEthCfmPingCtlEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,1,44,1))
if mibBuilder.loadTexts:tnOamEthCfmPingCtlEntry.setStatus(_A)
class _TnOamEthCfmPingCtlTgtMacAddr_Type(MacAddress):defaultHexValue='000000000000'
_TnOamEthCfmPingCtlTgtMacAddr_Type.__name__=_A7
_TnOamEthCfmPingCtlTgtMacAddr_Object=MibTableColumn
tnOamEthCfmPingCtlTgtMacAddr=_TnOamEthCfmPingCtlTgtMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,11,1,44,1,1),_TnOamEthCfmPingCtlTgtMacAddr_Type())
tnOamEthCfmPingCtlTgtMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamEthCfmPingCtlTgtMacAddr.setStatus(_A)
class _TnOamEthCfmPingCtlSrcMdIndex_Type(Unsigned32):defaultValue=0
_TnOamEthCfmPingCtlSrcMdIndex_Type.__name__=_D
_TnOamEthCfmPingCtlSrcMdIndex_Object=MibTableColumn
tnOamEthCfmPingCtlSrcMdIndex=_TnOamEthCfmPingCtlSrcMdIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,1,44,1,2),_TnOamEthCfmPingCtlSrcMdIndex_Type())
tnOamEthCfmPingCtlSrcMdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamEthCfmPingCtlSrcMdIndex.setStatus(_A)
class _TnOamEthCfmPingCtlSrcMaIndex_Type(Unsigned32):defaultValue=0
_TnOamEthCfmPingCtlSrcMaIndex_Type.__name__=_D
_TnOamEthCfmPingCtlSrcMaIndex_Object=MibTableColumn
tnOamEthCfmPingCtlSrcMaIndex=_TnOamEthCfmPingCtlSrcMaIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,1,44,1,3),_TnOamEthCfmPingCtlSrcMaIndex_Type())
tnOamEthCfmPingCtlSrcMaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamEthCfmPingCtlSrcMaIndex.setStatus(_A)
class _TnOamEthCfmPingCtlSrcMepId_Type(Dot1agCfmMepIdOrZero):defaultValue=0
_TnOamEthCfmPingCtlSrcMepId_Type.__name__=_A6
_TnOamEthCfmPingCtlSrcMepId_Object=MibTableColumn
tnOamEthCfmPingCtlSrcMepId=_TnOamEthCfmPingCtlSrcMepId_Object((1,3,6,1,4,1,7483,6,1,2,11,1,44,1,4),_TnOamEthCfmPingCtlSrcMepId_Type())
tnOamEthCfmPingCtlSrcMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamEthCfmPingCtlSrcMepId.setStatus(_A)
_TnOamTraceRouteObjs_ObjectIdentity=ObjectIdentity
tnOamTraceRouteObjs=_TnOamTraceRouteObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,11,2))
_TnOamTrCtlTable_Object=MibTable
tnOamTrCtlTable=_TnOamTrCtlTable_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3))
if mibBuilder.loadTexts:tnOamTrCtlTable.setStatus(_A)
_TnOamTrCtlEntry_Object=MibTableRow
tnOamTrCtlEntry=_TnOamTrCtlEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1))
tnOamTrCtlEntry.setIndexNames((0,_J,_K),(0,_E,_P))
if mibBuilder.loadTexts:tnOamTrCtlEntry.setStatus(_A)
class _TnOamTrCtlTestIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TnOamTrCtlTestIndex_Type.__name__=_R
_TnOamTrCtlTestIndex_Object=MibTableColumn
tnOamTrCtlTestIndex=_TnOamTrCtlTestIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,2),_TnOamTrCtlTestIndex_Type())
tnOamTrCtlTestIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamTrCtlTestIndex.setStatus(_A)
_TnOamTrCtlRowStatus_Type=RowStatus
_TnOamTrCtlRowStatus_Object=MibTableColumn
tnOamTrCtlRowStatus=_TnOamTrCtlRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,3),_TnOamTrCtlRowStatus_Type())
tnOamTrCtlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlRowStatus.setStatus(_A)
class _TnOamTrCtlStorageType_Type(StorageType):defaultValue=2
_TnOamTrCtlStorageType_Type.__name__=_a
_TnOamTrCtlStorageType_Object=MibTableColumn
tnOamTrCtlStorageType=_TnOamTrCtlStorageType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,4),_TnOamTrCtlStorageType_Type())
tnOamTrCtlStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlStorageType.setStatus(_A)
class _TnOamTrCtlDescr_Type(SnmpAdminString):defaultHexValue='00'
_TnOamTrCtlDescr_Type.__name__=_R
_TnOamTrCtlDescr_Object=MibTableColumn
tnOamTrCtlDescr=_TnOamTrCtlDescr_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,5),_TnOamTrCtlDescr_Type())
tnOamTrCtlDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlDescr.setStatus(_A)
class _TnOamTrCtlTestMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_X,0),('macTraceRoute',1),('lspTraceRoute',2),('vprnTraceRoute',3),('mcastTraceRoute',4),('icmpTraceRoute',5),('ldpTreeTrace',6),('vccvTraceRoute',7),('p2mpLspTrace',8),('ethCfmLinkTrace',9)))
_TnOamTrCtlTestMode_Type.__name__=_I
_TnOamTrCtlTestMode_Object=MibTableColumn
tnOamTrCtlTestMode=_TnOamTrCtlTestMode_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,6),_TnOamTrCtlTestMode_Type())
tnOamTrCtlTestMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlTestMode.setStatus(_A)
class _TnOamTrCtlAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_TnOamTrCtlAdminStatus_Type.__name__=_I
_TnOamTrCtlAdminStatus_Object=MibTableColumn
tnOamTrCtlAdminStatus=_TnOamTrCtlAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,7),_TnOamTrCtlAdminStatus_Type())
tnOamTrCtlAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlAdminStatus.setStatus(_A)
class _TnOamTrCtlFcName_Type(TFCName):defaultValue=OctetString('be')
_TnOamTrCtlFcName_Type.__name__=_o
_TnOamTrCtlFcName_Object=MibTableColumn
tnOamTrCtlFcName=_TnOamTrCtlFcName_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,8),_TnOamTrCtlFcName_Type())
tnOamTrCtlFcName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlFcName.setStatus(_A)
class _TnOamTrCtlProfile_Type(TProfile):defaultValue=2
_TnOamTrCtlProfile_Type.__name__=_p
_TnOamTrCtlProfile_Object=MibTableColumn
tnOamTrCtlProfile=_TnOamTrCtlProfile_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,9),_TnOamTrCtlProfile_Type())
tnOamTrCtlProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlProfile.setStatus(_A)
class _TnOamTrCtlTargetIpAddress_Type(IpAddress):defaultHexValue=_e
_TnOamTrCtlTargetIpAddress_Type.__name__=_U
_TnOamTrCtlTargetIpAddress_Object=MibTableColumn
tnOamTrCtlTargetIpAddress=_TnOamTrCtlTargetIpAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,10),_TnOamTrCtlTargetIpAddress_Type())
tnOamTrCtlTargetIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlTargetIpAddress.setStatus(_F)
class _TnOamTrCtlServiceId_Type(TmnxServId):defaultValue=0;subtypeSpec=TmnxServId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TnOamTrCtlServiceId_Type.__name__=_s
_TnOamTrCtlServiceId_Object=MibTableColumn
tnOamTrCtlServiceId=_TnOamTrCtlServiceId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,11),_TnOamTrCtlServiceId_Type())
tnOamTrCtlServiceId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlServiceId.setStatus(_A)
class _TnOamTrCtlDataSize_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9198))
_TnOamTrCtlDataSize_Type.__name__=_D
_TnOamTrCtlDataSize_Object=MibTableColumn
tnOamTrCtlDataSize=_TnOamTrCtlDataSize_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,12),_TnOamTrCtlDataSize_Type())
tnOamTrCtlDataSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlDataSize.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrCtlDataSize.setUnits(_Y)
class _TnOamTrCtlTimeOut_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_TnOamTrCtlTimeOut_Type.__name__=_D
_TnOamTrCtlTimeOut_Object=MibTableColumn
tnOamTrCtlTimeOut=_TnOamTrCtlTimeOut_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,13),_TnOamTrCtlTimeOut_Type())
tnOamTrCtlTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlTimeOut.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrCtlTimeOut.setUnits(_y)
class _TnOamTrCtlProbesPerHop_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnOamTrCtlProbesPerHop_Type.__name__=_D
_TnOamTrCtlProbesPerHop_Object=MibTableColumn
tnOamTrCtlProbesPerHop=_TnOamTrCtlProbesPerHop_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,14),_TnOamTrCtlProbesPerHop_Type())
tnOamTrCtlProbesPerHop.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlProbesPerHop.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrCtlProbesPerHop.setUnits(_f)
class _TnOamTrCtlMaxTtl_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TnOamTrCtlMaxTtl_Type.__name__=_D
_TnOamTrCtlMaxTtl_Object=MibTableColumn
tnOamTrCtlMaxTtl=_TnOamTrCtlMaxTtl_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,15),_TnOamTrCtlMaxTtl_Type())
tnOamTrCtlMaxTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlMaxTtl.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrCtlMaxTtl.setUnits(_A0)
class _TnOamTrCtlInitialTtl_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TnOamTrCtlInitialTtl_Type.__name__=_D
_TnOamTrCtlInitialTtl_Object=MibTableColumn
tnOamTrCtlInitialTtl=_TnOamTrCtlInitialTtl_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,16),_TnOamTrCtlInitialTtl_Type())
tnOamTrCtlInitialTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlInitialTtl.setStatus(_A)
class _TnOamTrCtlDSField_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnOamTrCtlDSField_Type.__name__=_D
_TnOamTrCtlDSField_Object=MibTableColumn
tnOamTrCtlDSField=_TnOamTrCtlDSField_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,17),_TnOamTrCtlDSField_Type())
tnOamTrCtlDSField.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlDSField.setStatus(_A)
class _TnOamTrCtlMaxFailures_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TnOamTrCtlMaxFailures_Type.__name__=_D
_TnOamTrCtlMaxFailures_Object=MibTableColumn
tnOamTrCtlMaxFailures=_TnOamTrCtlMaxFailures_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,18),_TnOamTrCtlMaxFailures_Type())
tnOamTrCtlMaxFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlMaxFailures.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrCtlMaxFailures.setUnits('timeouts')
class _TnOamTrCtlInterval_Type(Unsigned32):defaultValue=1
_TnOamTrCtlInterval_Type.__name__=_D
_TnOamTrCtlInterval_Object=MibTableColumn
tnOamTrCtlInterval=_TnOamTrCtlInterval_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,19),_TnOamTrCtlInterval_Type())
tnOamTrCtlInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlInterval.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrCtlInterval.setUnits(_y)
class _TnOamTrCtlMaxRows_Type(Unsigned32):defaultValue=300
_TnOamTrCtlMaxRows_Type.__name__=_D
_TnOamTrCtlMaxRows_Object=MibTableColumn
tnOamTrCtlMaxRows=_TnOamTrCtlMaxRows_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,20),_TnOamTrCtlMaxRows_Type())
tnOamTrCtlMaxRows.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlMaxRows.setStatus(_F)
if mibBuilder.loadTexts:tnOamTrCtlMaxRows.setUnits('rows')
class _TnOamTrCtlTrapGeneration_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('pathChange',0),(_AD,1),(_AE,2)))
_TnOamTrCtlTrapGeneration_Type.__name__=_k
_TnOamTrCtlTrapGeneration_Object=MibTableColumn
tnOamTrCtlTrapGeneration=_TnOamTrCtlTrapGeneration_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,21),_TnOamTrCtlTrapGeneration_Type())
tnOamTrCtlTrapGeneration.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlTrapGeneration.setStatus(_A)
class _TnOamTrCtlCreateHopsEntries_Type(TruthValue):defaultValue=2
_TnOamTrCtlCreateHopsEntries_Type.__name__=_M
_TnOamTrCtlCreateHopsEntries_Object=MibTableColumn
tnOamTrCtlCreateHopsEntries=_TnOamTrCtlCreateHopsEntries_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,22),_TnOamTrCtlCreateHopsEntries_Type())
tnOamTrCtlCreateHopsEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlCreateHopsEntries.setStatus(_F)
class _TnOamTrCtlSAA_Type(TruthValue):defaultValue=2
_TnOamTrCtlSAA_Type.__name__=_M
_TnOamTrCtlSAA_Object=MibTableColumn
tnOamTrCtlSAA=_TnOamTrCtlSAA_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,23),_TnOamTrCtlSAA_Type())
tnOamTrCtlSAA.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlSAA.setStatus(_A)
_TnOamTrCtlRuns_Type=Counter32
_TnOamTrCtlRuns_Object=MibTableColumn
tnOamTrCtlRuns=_TnOamTrCtlRuns_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,24),_TnOamTrCtlRuns_Type())
tnOamTrCtlRuns.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrCtlRuns.setStatus(_A)
_TnOamTrCtlFailures_Type=Counter32
_TnOamTrCtlFailures_Object=MibTableColumn
tnOamTrCtlFailures=_TnOamTrCtlFailures_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,25),_TnOamTrCtlFailures_Type())
tnOamTrCtlFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrCtlFailures.setStatus(_A)
_TnOamTrCtlLastRunResult_Type=TmnxOamTestResult
_TnOamTrCtlLastRunResult_Object=MibTableColumn
tnOamTrCtlLastRunResult=_TnOamTrCtlLastRunResult_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,26),_TnOamTrCtlLastRunResult_Type())
tnOamTrCtlLastRunResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrCtlLastRunResult.setStatus(_A)
_TnOamTrCtlLastChanged_Type=TimeStamp
_TnOamTrCtlLastChanged_Object=MibTableColumn
tnOamTrCtlLastChanged=_TnOamTrCtlLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,27),_TnOamTrCtlLastChanged_Type())
tnOamTrCtlLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrCtlLastChanged.setStatus(_A)
class _TnOamTrCtlVRtrID_Type(TmnxVRtrID):defaultValue=1
_TnOamTrCtlVRtrID_Type.__name__=_W
_TnOamTrCtlVRtrID_Object=MibTableColumn
tnOamTrCtlVRtrID=_TnOamTrCtlVRtrID_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,28),_TnOamTrCtlVRtrID_Type())
tnOamTrCtlVRtrID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlVRtrID.setStatus(_A)
class _TnOamTrCtlTgtAddrType_Type(InetAddressType):defaultValue=0
_TnOamTrCtlTgtAddrType_Type.__name__=_L
_TnOamTrCtlTgtAddrType_Object=MibTableColumn
tnOamTrCtlTgtAddrType=_TnOamTrCtlTgtAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,29),_TnOamTrCtlTgtAddrType_Type())
tnOamTrCtlTgtAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlTgtAddrType.setStatus(_A)
class _TnOamTrCtlTgtAddress_Type(InetAddress):defaultHexValue=''
_TnOamTrCtlTgtAddress_Type.__name__=_G
_TnOamTrCtlTgtAddress_Object=MibTableColumn
tnOamTrCtlTgtAddress=_TnOamTrCtlTgtAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,30),_TnOamTrCtlTgtAddress_Type())
tnOamTrCtlTgtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlTgtAddress.setStatus(_A)
class _TnOamTrCtlSrcAddrType_Type(InetAddressType):defaultValue=0
_TnOamTrCtlSrcAddrType_Type.__name__=_L
_TnOamTrCtlSrcAddrType_Object=MibTableColumn
tnOamTrCtlSrcAddrType=_TnOamTrCtlSrcAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,31),_TnOamTrCtlSrcAddrType_Type())
tnOamTrCtlSrcAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlSrcAddrType.setStatus(_A)
class _TnOamTrCtlSrcAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamTrCtlSrcAddress_Type.__name__=_G
_TnOamTrCtlSrcAddress_Object=MibTableColumn
tnOamTrCtlSrcAddress=_TnOamTrCtlSrcAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,32),_TnOamTrCtlSrcAddress_Type())
tnOamTrCtlSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlSrcAddress.setStatus(_A)
class _TnOamTrCtlWaitMilliSec_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60000))
_TnOamTrCtlWaitMilliSec_Type.__name__=_D
_TnOamTrCtlWaitMilliSec_Object=MibTableColumn
tnOamTrCtlWaitMilliSec=_TnOamTrCtlWaitMilliSec_Object((1,3,6,1,4,1,7483,6,1,2,11,2,3,1,33),_TnOamTrCtlWaitMilliSec_Type())
tnOamTrCtlWaitMilliSec.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamTrCtlWaitMilliSec.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrCtlWaitMilliSec.setUnits(_x)
_TnOamTrResultsTable_Object=MibTable
tnOamTrResultsTable=_TnOamTrResultsTable_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4))
if mibBuilder.loadTexts:tnOamTrResultsTable.setStatus(_A)
_TnOamTrResultsEntry_Object=MibTableRow
tnOamTrResultsEntry=_TnOamTrResultsEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1))
tnOamTrResultsEntry.setIndexNames((0,_J,_K),(0,_E,_P),(0,_E,_Z))
if mibBuilder.loadTexts:tnOamTrResultsEntry.setStatus(_A)
class _TnOamTrResultsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_TnOamTrResultsOperStatus_Type.__name__=_I
_TnOamTrResultsOperStatus_Object=MibTableColumn
tnOamTrResultsOperStatus=_TnOamTrResultsOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,1),_TnOamTrResultsOperStatus_Type())
tnOamTrResultsOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsOperStatus.setStatus(_A)
_TnOamTrResultsCurHopCount_Type=Gauge32
_TnOamTrResultsCurHopCount_Object=MibTableColumn
tnOamTrResultsCurHopCount=_TnOamTrResultsCurHopCount_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,2),_TnOamTrResultsCurHopCount_Type())
tnOamTrResultsCurHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsCurHopCount.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrResultsCurHopCount.setUnits('hops')
_TnOamTrResultsCurProbeCount_Type=Gauge32
_TnOamTrResultsCurProbeCount_Object=MibTableColumn
tnOamTrResultsCurProbeCount=_TnOamTrResultsCurProbeCount_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,3),_TnOamTrResultsCurProbeCount_Type())
tnOamTrResultsCurProbeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsCurProbeCount.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrResultsCurProbeCount.setUnits(_f)
_TnOamTrResultsIpTgtAddr_Type=IpAddress
_TnOamTrResultsIpTgtAddr_Object=MibTableColumn
tnOamTrResultsIpTgtAddr=_TnOamTrResultsIpTgtAddr_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,4),_TnOamTrResultsIpTgtAddr_Type())
tnOamTrResultsIpTgtAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsIpTgtAddr.setStatus(_F)
_TnOamTrResultsTestAttempts_Type=Unsigned32
_TnOamTrResultsTestAttempts_Object=MibTableColumn
tnOamTrResultsTestAttempts=_TnOamTrResultsTestAttempts_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,5),_TnOamTrResultsTestAttempts_Type())
tnOamTrResultsTestAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsTestAttempts.setStatus(_F)
if mibBuilder.loadTexts:tnOamTrResultsTestAttempts.setUnits('tests')
_TnOamTrResultsTestSuccesses_Type=Unsigned32
_TnOamTrResultsTestSuccesses_Object=MibTableColumn
tnOamTrResultsTestSuccesses=_TnOamTrResultsTestSuccesses_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,6),_TnOamTrResultsTestSuccesses_Type())
tnOamTrResultsTestSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsTestSuccesses.setStatus(_F)
if mibBuilder.loadTexts:tnOamTrResultsTestSuccesses.setUnits('tests')
_TnOamTrResultsLastGoodPath_Type=DateAndTime
_TnOamTrResultsLastGoodPath_Object=MibTableColumn
tnOamTrResultsLastGoodPath=_TnOamTrResultsLastGoodPath_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,7),_TnOamTrResultsLastGoodPath_Type())
tnOamTrResultsLastGoodPath.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsLastGoodPath.setStatus(_A)
class _TnOamTrResultsTestRunIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TnOamTrResultsTestRunIndex_Type.__name__=_D
_TnOamTrResultsTestRunIndex_Object=MibTableColumn
tnOamTrResultsTestRunIndex=_TnOamTrResultsTestRunIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,8),_TnOamTrResultsTestRunIndex_Type())
tnOamTrResultsTestRunIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamTrResultsTestRunIndex.setStatus(_A)
_TnOamTrResultsTgtAddrType_Type=InetAddressType
_TnOamTrResultsTgtAddrType_Object=MibTableColumn
tnOamTrResultsTgtAddrType=_TnOamTrResultsTgtAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,9),_TnOamTrResultsTgtAddrType_Type())
tnOamTrResultsTgtAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsTgtAddrType.setStatus(_A)
class _TnOamTrResultsTgtAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamTrResultsTgtAddress_Type.__name__=_G
_TnOamTrResultsTgtAddress_Object=MibTableColumn
tnOamTrResultsTgtAddress=_TnOamTrResultsTgtAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,10),_TnOamTrResultsTgtAddress_Type())
tnOamTrResultsTgtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsTgtAddress.setStatus(_A)
_TnOamTrResultsTestRunResult_Type=TmnxOamTestResult
_TnOamTrResultsTestRunResult_Object=MibTableColumn
tnOamTrResultsTestRunResult=_TnOamTrResultsTestRunResult_Object((1,3,6,1,4,1,7483,6,1,2,11,2,4,1,11),_TnOamTrResultsTestRunResult_Type())
tnOamTrResultsTestRunResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrResultsTestRunResult.setStatus(_A)
_TnOamTrProbeHistoryTable_Object=MibTable
tnOamTrProbeHistoryTable=_TnOamTrProbeHistoryTable_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5))
if mibBuilder.loadTexts:tnOamTrProbeHistoryTable.setStatus(_A)
_TnOamTrProbeHistoryEntry_Object=MibTableRow
tnOamTrProbeHistoryEntry=_TnOamTrProbeHistoryEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1))
tnOamTrProbeHistoryEntry.setIndexNames((0,_J,_K),(0,_E,_P),(0,_E,_Z),(0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:tnOamTrProbeHistoryEntry.setStatus(_A)
class _TnOamTrProbeHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TnOamTrProbeHistoryIndex_Type.__name__=_D
_TnOamTrProbeHistoryIndex_Object=MibTableColumn
tnOamTrProbeHistoryIndex=_TnOamTrProbeHistoryIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,1),_TnOamTrProbeHistoryIndex_Type())
tnOamTrProbeHistoryIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamTrProbeHistoryIndex.setStatus(_A)
class _TnOamTrProbeHistoryHopIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TnOamTrProbeHistoryHopIndex_Type.__name__=_D
_TnOamTrProbeHistoryHopIndex_Object=MibTableColumn
tnOamTrProbeHistoryHopIndex=_TnOamTrProbeHistoryHopIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,2),_TnOamTrProbeHistoryHopIndex_Type())
tnOamTrProbeHistoryHopIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamTrProbeHistoryHopIndex.setStatus(_A)
class _TnOamTrProbeHistoryProbeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnOamTrProbeHistoryProbeIndex_Type.__name__=_D
_TnOamTrProbeHistoryProbeIndex_Object=MibTableColumn
tnOamTrProbeHistoryProbeIndex=_TnOamTrProbeHistoryProbeIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,3),_TnOamTrProbeHistoryProbeIndex_Type())
tnOamTrProbeHistoryProbeIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamTrProbeHistoryProbeIndex.setStatus(_A)
_TnOamTrProbeHistoryIpAddr_Type=IpAddress
_TnOamTrProbeHistoryIpAddr_Object=MibTableColumn
tnOamTrProbeHistoryIpAddr=_TnOamTrProbeHistoryIpAddr_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,4),_TnOamTrProbeHistoryIpAddr_Type())
tnOamTrProbeHistoryIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryIpAddr.setStatus(_F)
_TnOamTrProbeHistoryResponse_Type=Unsigned32
_TnOamTrProbeHistoryResponse_Object=MibTableColumn
tnOamTrProbeHistoryResponse=_TnOamTrProbeHistoryResponse_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,5),_TnOamTrProbeHistoryResponse_Type())
tnOamTrProbeHistoryResponse.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryResponse.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrProbeHistoryResponse.setUnits(_H)
_TnOamTrProbeHistoryOneWayTime_Type=Integer32
_TnOamTrProbeHistoryOneWayTime_Object=MibTableColumn
tnOamTrProbeHistoryOneWayTime=_TnOamTrProbeHistoryOneWayTime_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,6),_TnOamTrProbeHistoryOneWayTime_Type())
tnOamTrProbeHistoryOneWayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryOneWayTime.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrProbeHistoryOneWayTime.setUnits(_H)
_TnOamTrProbeHistoryStatus_Type=TmnxOamResponseStatus
_TnOamTrProbeHistoryStatus_Object=MibTableColumn
tnOamTrProbeHistoryStatus=_TnOamTrProbeHistoryStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,7),_TnOamTrProbeHistoryStatus_Type())
tnOamTrProbeHistoryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryStatus.setStatus(_A)
_TnOamTrProbeHistoryLastRC_Type=Integer32
_TnOamTrProbeHistoryLastRC_Object=MibTableColumn
tnOamTrProbeHistoryLastRC=_TnOamTrProbeHistoryLastRC_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,8),_TnOamTrProbeHistoryLastRC_Type())
tnOamTrProbeHistoryLastRC.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryLastRC.setStatus(_A)
_TnOamTrProbeHistoryTime_Type=DateAndTime
_TnOamTrProbeHistoryTime_Object=MibTableColumn
tnOamTrProbeHistoryTime=_TnOamTrProbeHistoryTime_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,9),_TnOamTrProbeHistoryTime_Type())
tnOamTrProbeHistoryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryTime.setStatus(_A)
_TnOamTrProbeHistoryResponsePlane_Type=TmnxOamTestResponsePlane
_TnOamTrProbeHistoryResponsePlane_Object=MibTableColumn
tnOamTrProbeHistoryResponsePlane=_TnOamTrProbeHistoryResponsePlane_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,10),_TnOamTrProbeHistoryResponsePlane_Type())
tnOamTrProbeHistoryResponsePlane.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryResponsePlane.setStatus(_A)
_TnOamTrProbeHistoryAddressType_Type=TmnxOamAddressType
_TnOamTrProbeHistoryAddressType_Object=MibTableColumn
tnOamTrProbeHistoryAddressType=_TnOamTrProbeHistoryAddressType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,11),_TnOamTrProbeHistoryAddressType_Type())
tnOamTrProbeHistoryAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryAddressType.setStatus(_A)
_TnOamTrProbeHistorySapId_Type=TmnxStrSapId
_TnOamTrProbeHistorySapId_Object=MibTableColumn
tnOamTrProbeHistorySapId=_TnOamTrProbeHistorySapId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,12),_TnOamTrProbeHistorySapId_Type())
tnOamTrProbeHistorySapId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistorySapId.setStatus(_A)
_TnOamTrProbeHistoryVersion_Type=Unsigned32
_TnOamTrProbeHistoryVersion_Object=MibTableColumn
tnOamTrProbeHistoryVersion=_TnOamTrProbeHistoryVersion_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,14),_TnOamTrProbeHistoryVersion_Type())
tnOamTrProbeHistoryVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryVersion.setStatus(_A)
_TnOamTrProbeHistoryRouterID_Type=RouterID
_TnOamTrProbeHistoryRouterID_Object=MibTableColumn
tnOamTrProbeHistoryRouterID=_TnOamTrProbeHistoryRouterID_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,15),_TnOamTrProbeHistoryRouterID_Type())
tnOamTrProbeHistoryRouterID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryRouterID.setStatus(_A)
_TnOamTrProbeHistoryIfIndex_Type=InterfaceIndexOrZero
_TnOamTrProbeHistoryIfIndex_Object=MibTableColumn
tnOamTrProbeHistoryIfIndex=_TnOamTrProbeHistoryIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,16),_TnOamTrProbeHistoryIfIndex_Type())
tnOamTrProbeHistoryIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryIfIndex.setStatus(_A)
_TnOamTrProbeHistoryDataLen_Type=Unsigned32
_TnOamTrProbeHistoryDataLen_Object=MibTableColumn
tnOamTrProbeHistoryDataLen=_TnOamTrProbeHistoryDataLen_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,17),_TnOamTrProbeHistoryDataLen_Type())
tnOamTrProbeHistoryDataLen.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryDataLen.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrProbeHistoryDataLen.setUnits(_Y)
_TnOamTrProbeHistorySize_Type=Unsigned32
_TnOamTrProbeHistorySize_Object=MibTableColumn
tnOamTrProbeHistorySize=_TnOamTrProbeHistorySize_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,18),_TnOamTrProbeHistorySize_Type())
tnOamTrProbeHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistorySize.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrProbeHistorySize.setUnits(_Y)
_TnOamTrProbeHistoryInOneWayTime_Type=Integer32
_TnOamTrProbeHistoryInOneWayTime_Object=MibTableColumn
tnOamTrProbeHistoryInOneWayTime=_TnOamTrProbeHistoryInOneWayTime_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,19),_TnOamTrProbeHistoryInOneWayTime_Type())
tnOamTrProbeHistoryInOneWayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryInOneWayTime.setStatus(_A)
if mibBuilder.loadTexts:tnOamTrProbeHistoryInOneWayTime.setUnits(_H)
_TnOamTrProbeHistoryAddrType_Type=InetAddressType
_TnOamTrProbeHistoryAddrType_Object=MibTableColumn
tnOamTrProbeHistoryAddrType=_TnOamTrProbeHistoryAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,20),_TnOamTrProbeHistoryAddrType_Type())
tnOamTrProbeHistoryAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryAddrType.setStatus(_A)
class _TnOamTrProbeHistoryAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamTrProbeHistoryAddress_Type.__name__=_G
_TnOamTrProbeHistoryAddress_Object=MibTableColumn
tnOamTrProbeHistoryAddress=_TnOamTrProbeHistoryAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,21),_TnOamTrProbeHistoryAddress_Type())
tnOamTrProbeHistoryAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistoryAddress.setStatus(_A)
_TnOamTrProbeHistorySrcGlobalId_Type=TmnxMplsTpGlobalID
_TnOamTrProbeHistorySrcGlobalId_Object=MibTableColumn
tnOamTrProbeHistorySrcGlobalId=_TnOamTrProbeHistorySrcGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,22),_TnOamTrProbeHistorySrcGlobalId_Type())
tnOamTrProbeHistorySrcGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistorySrcGlobalId.setStatus(_A)
_TnOamTrProbeHistorySrcNodeId_Type=TmnxMplsTpNodeID
_TnOamTrProbeHistorySrcNodeId_Object=MibTableColumn
tnOamTrProbeHistorySrcNodeId=_TnOamTrProbeHistorySrcNodeId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,5,1,23),_TnOamTrProbeHistorySrcNodeId_Type())
tnOamTrProbeHistorySrcNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTrProbeHistorySrcNodeId.setStatus(_A)
_TnOamLspTrCtlTable_Object=MibTable
tnOamLspTrCtlTable=_TnOamLspTrCtlTable_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9))
if mibBuilder.loadTexts:tnOamLspTrCtlTable.setStatus(_A)
_TnOamLspTrCtlEntry_Object=MibTableRow
tnOamLspTrCtlEntry=_TnOamLspTrCtlEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1))
tnOamLspTrCtlEntry.setIndexNames((0,_J,_K),(0,_E,_P))
if mibBuilder.loadTexts:tnOamLspTrCtlEntry.setStatus(_A)
class _TnOamLspTrCtlVRtrID_Type(TmnxVRtrID):defaultValue=1
_TnOamLspTrCtlVRtrID_Type.__name__=_W
_TnOamLspTrCtlVRtrID_Object=MibTableColumn
tnOamLspTrCtlVRtrID=_TnOamLspTrCtlVRtrID_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,1),_TnOamLspTrCtlVRtrID_Type())
tnOamLspTrCtlVRtrID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlVRtrID.setStatus(_F)
class _TnOamLspTrCtlLspName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnOamLspTrCtlLspName_Type.__name__=_O
_TnOamLspTrCtlLspName_Object=MibTableColumn
tnOamLspTrCtlLspName=_TnOamLspTrCtlLspName_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,2),_TnOamLspTrCtlLspName_Type())
tnOamLspTrCtlLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlLspName.setStatus(_A)
class _TnOamLspTrCtlPathName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnOamLspTrCtlPathName_Type.__name__=_O
_TnOamLspTrCtlPathName_Object=MibTableColumn
tnOamLspTrCtlPathName=_TnOamLspTrCtlPathName_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,3),_TnOamLspTrCtlPathName_Type())
tnOamLspTrCtlPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlPathName.setStatus(_A)
class _TnOamLspTrCtlLdpIpPrefix_Type(IpAddress):defaultHexValue=_e
_TnOamLspTrCtlLdpIpPrefix_Type.__name__=_U
_TnOamLspTrCtlLdpIpPrefix_Object=MibTableColumn
tnOamLspTrCtlLdpIpPrefix=_TnOamLspTrCtlLdpIpPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,4),_TnOamLspTrCtlLdpIpPrefix_Type())
tnOamLspTrCtlLdpIpPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlLdpIpPrefix.setStatus(_F)
class _TnOamLspTrCtlLdpIpPrefixLen_Type(IpAddressPrefixLength):defaultValue=32
_TnOamLspTrCtlLdpIpPrefixLen_Type.__name__=_m
_TnOamLspTrCtlLdpIpPrefixLen_Object=MibTableColumn
tnOamLspTrCtlLdpIpPrefixLen=_TnOamLspTrCtlLdpIpPrefixLen_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,5),_TnOamLspTrCtlLdpIpPrefixLen_Type())
tnOamLspTrCtlLdpIpPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlLdpIpPrefixLen.setStatus(_F)
class _TnOamLspTrCtlLdpPrefixType_Type(InetAddressType):defaultValue=0
_TnOamLspTrCtlLdpPrefixType_Type.__name__=_L
_TnOamLspTrCtlLdpPrefixType_Object=MibTableColumn
tnOamLspTrCtlLdpPrefixType=_TnOamLspTrCtlLdpPrefixType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,6),_TnOamLspTrCtlLdpPrefixType_Type())
tnOamLspTrCtlLdpPrefixType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlLdpPrefixType.setStatus(_A)
class _TnOamLspTrCtlLdpPrefix_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamLspTrCtlLdpPrefix_Type.__name__=_G
_TnOamLspTrCtlLdpPrefix_Object=MibTableColumn
tnOamLspTrCtlLdpPrefix=_TnOamLspTrCtlLdpPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,7),_TnOamLspTrCtlLdpPrefix_Type())
tnOamLspTrCtlLdpPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlLdpPrefix.setStatus(_A)
class _TnOamLspTrCtlLdpPrefixLen_Type(InetAddressPrefixLength):defaultValue=32
_TnOamLspTrCtlLdpPrefixLen_Type.__name__=_j
_TnOamLspTrCtlLdpPrefixLen_Object=MibTableColumn
tnOamLspTrCtlLdpPrefixLen=_TnOamLspTrCtlLdpPrefixLen_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,8),_TnOamLspTrCtlLdpPrefixLen_Type())
tnOamLspTrCtlLdpPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlLdpPrefixLen.setStatus(_A)
class _TnOamLspTrCtlPathDestType_Type(InetAddressType):defaultValue=0
_TnOamLspTrCtlPathDestType_Type.__name__=_L
_TnOamLspTrCtlPathDestType_Object=MibTableColumn
tnOamLspTrCtlPathDestType=_TnOamLspTrCtlPathDestType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,9),_TnOamLspTrCtlPathDestType_Type())
tnOamLspTrCtlPathDestType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlPathDestType.setStatus(_A)
class _TnOamLspTrCtlPathDest_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamLspTrCtlPathDest_Type.__name__=_G
_TnOamLspTrCtlPathDest_Object=MibTableColumn
tnOamLspTrCtlPathDest=_TnOamLspTrCtlPathDest_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,10),_TnOamLspTrCtlPathDest_Type())
tnOamLspTrCtlPathDest.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlPathDest.setStatus(_A)
class _TnOamLspTrCtlNhIntfName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnOamLspTrCtlNhIntfName_Type.__name__=_O
_TnOamLspTrCtlNhIntfName_Object=MibTableColumn
tnOamLspTrCtlNhIntfName=_TnOamLspTrCtlNhIntfName_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,11),_TnOamLspTrCtlNhIntfName_Type())
tnOamLspTrCtlNhIntfName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlNhIntfName.setStatus(_A)
class _TnOamLspTrCtlNhAddressType_Type(InetAddressType):defaultValue=0
_TnOamLspTrCtlNhAddressType_Type.__name__=_L
_TnOamLspTrCtlNhAddressType_Object=MibTableColumn
tnOamLspTrCtlNhAddressType=_TnOamLspTrCtlNhAddressType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,12),_TnOamLspTrCtlNhAddressType_Type())
tnOamLspTrCtlNhAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlNhAddressType.setStatus(_A)
class _TnOamLspTrCtlNhAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamLspTrCtlNhAddress_Type.__name__=_G
_TnOamLspTrCtlNhAddress_Object=MibTableColumn
tnOamLspTrCtlNhAddress=_TnOamLspTrCtlNhAddress_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,13),_TnOamLspTrCtlNhAddress_Type())
tnOamLspTrCtlNhAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlNhAddress.setStatus(_A)
class _TnOamLspTrCtlDownstreamMapTlv_Type(TmnxOamMplsEchoDownMapTlvOrNone):defaultValue=1
_TnOamLspTrCtlDownstreamMapTlv_Type.__name__=_AI
_TnOamLspTrCtlDownstreamMapTlv_Object=MibTableColumn
tnOamLspTrCtlDownstreamMapTlv=_TnOamLspTrCtlDownstreamMapTlv_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,14),_TnOamLspTrCtlDownstreamMapTlv_Type())
tnOamLspTrCtlDownstreamMapTlv.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlDownstreamMapTlv.setStatus(_A)
class _TnOamLspTrCtlTestSubMode_Type(TmnxOamLspTestSubMode):defaultValue=1
_TnOamLspTrCtlTestSubMode_Type.__name__=_A1
_TnOamLspTrCtlTestSubMode_Object=MibTableColumn
tnOamLspTrCtlTestSubMode=_TnOamLspTrCtlTestSubMode_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,15),_TnOamLspTrCtlTestSubMode_Type())
tnOamLspTrCtlTestSubMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlTestSubMode.setStatus(_A)
class _TnOamLspTrCtlMplsTpPathType_Type(TmnxOamMplsTpPathType):defaultValue=3
_TnOamLspTrCtlMplsTpPathType_Type.__name__=_A2
_TnOamLspTrCtlMplsTpPathType_Object=MibTableColumn
tnOamLspTrCtlMplsTpPathType=_TnOamLspTrCtlMplsTpPathType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,16),_TnOamLspTrCtlMplsTpPathType_Type())
tnOamLspTrCtlMplsTpPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlMplsTpPathType.setStatus(_A)
class _TnOamLspTrCtlAssocChannel_Type(TmnxOamLspAssocChannel):defaultValue=1
_TnOamLspTrCtlAssocChannel_Type.__name__=_A3
_TnOamLspTrCtlAssocChannel_Object=MibTableColumn
tnOamLspTrCtlAssocChannel=_TnOamLspTrCtlAssocChannel_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,17),_TnOamLspTrCtlAssocChannel_Type())
tnOamLspTrCtlAssocChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlAssocChannel.setStatus(_A)
class _TnOamLspTrCtlForce_Type(TruthValue):defaultValue=2
_TnOamLspTrCtlForce_Type.__name__=_M
_TnOamLspTrCtlForce_Object=MibTableColumn
tnOamLspTrCtlForce=_TnOamLspTrCtlForce_Object((1,3,6,1,4,1,7483,6,1,2,11,2,9,1,18),_TnOamLspTrCtlForce_Type())
tnOamLspTrCtlForce.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamLspTrCtlForce.setStatus(_A)
_TnOamLspTrMapTable_Object=MibTable
tnOamLspTrMapTable=_TnOamLspTrMapTable_Object((1,3,6,1,4,1,7483,6,1,2,11,2,10))
if mibBuilder.loadTexts:tnOamLspTrMapTable.setStatus(_A)
_TnOamLspTrMapEntry_Object=MibTableRow
tnOamLspTrMapEntry=_TnOamLspTrMapEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,2,10,1))
tnOamLspTrMapEntry.setIndexNames((0,_J,_K),(0,_E,_P),(0,_E,_Z),(0,_E,_g),(0,_E,_h),(0,_E,_i),(0,_E,_AJ))
if mibBuilder.loadTexts:tnOamLspTrMapEntry.setStatus(_A)
class _TnOamLspTrMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TnOamLspTrMapIndex_Type.__name__=_D
_TnOamLspTrMapIndex_Object=MibTableColumn
tnOamLspTrMapIndex=_TnOamLspTrMapIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,2,10,1,1),_TnOamLspTrMapIndex_Type())
tnOamLspTrMapIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamLspTrMapIndex.setStatus(_A)
_TnOamLspTrMapDSIPv4Addr_Type=IpAddress
_TnOamLspTrMapDSIPv4Addr_Object=MibTableColumn
tnOamLspTrMapDSIPv4Addr=_TnOamLspTrMapDSIPv4Addr_Object((1,3,6,1,4,1,7483,6,1,2,11,2,10,1,2),_TnOamLspTrMapDSIPv4Addr_Type())
tnOamLspTrMapDSIPv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamLspTrMapDSIPv4Addr.setStatus(_A)
_TnOamLspTrMapAddrType_Type=TmnxOamAddressType
_TnOamLspTrMapAddrType_Object=MibTableColumn
tnOamLspTrMapAddrType=_TnOamLspTrMapAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,10,1,3),_TnOamLspTrMapAddrType_Type())
tnOamLspTrMapAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamLspTrMapAddrType.setStatus(_A)
_TnOamLspTrMapDSIfAddr_Type=Unsigned32
_TnOamLspTrMapDSIfAddr_Object=MibTableColumn
tnOamLspTrMapDSIfAddr=_TnOamLspTrMapDSIfAddr_Object((1,3,6,1,4,1,7483,6,1,2,11,2,10,1,4),_TnOamLspTrMapDSIfAddr_Type())
tnOamLspTrMapDSIfAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamLspTrMapDSIfAddr.setStatus(_A)
class _TnOamLspTrMapMTU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnOamLspTrMapMTU_Type.__name__=_D
_TnOamLspTrMapMTU_Object=MibTableColumn
tnOamLspTrMapMTU=_TnOamLspTrMapMTU_Object((1,3,6,1,4,1,7483,6,1,2,11,2,10,1,5),_TnOamLspTrMapMTU_Type())
tnOamLspTrMapMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamLspTrMapMTU.setStatus(_A)
class _TnOamLspTrMapDSIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnOamLspTrMapDSIndex_Type.__name__=_D
_TnOamLspTrMapDSIndex_Object=MibTableColumn
tnOamLspTrMapDSIndex=_TnOamLspTrMapDSIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,2,10,1,6),_TnOamLspTrMapDSIndex_Type())
tnOamLspTrMapDSIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamLspTrMapDSIndex.setStatus(_F)
_TnOamVccvTrCtlTable_Object=MibTable
tnOamVccvTrCtlTable=_TnOamVccvTrCtlTable_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26))
if mibBuilder.loadTexts:tnOamVccvTrCtlTable.setStatus(_A)
_TnOamVccvTrCtlEntry_Object=MibTableRow
tnOamVccvTrCtlEntry=_TnOamVccvTrCtlEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1))
tnOamVccvTrCtlEntry.setIndexNames((0,_J,_K),(0,_E,_P))
if mibBuilder.loadTexts:tnOamVccvTrCtlEntry.setStatus(_A)
class _TnOamVccvTrCtlSdpIdVcId_Type(SdpBindId):defaultHexValue=_AG
_TnOamVccvTrCtlSdpIdVcId_Type.__name__=_n
_TnOamVccvTrCtlSdpIdVcId_Object=MibTableColumn
tnOamVccvTrCtlSdpIdVcId=_TnOamVccvTrCtlSdpIdVcId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,1),_TnOamVccvTrCtlSdpIdVcId_Type())
tnOamVccvTrCtlSdpIdVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlSdpIdVcId.setStatus(_A)
class _TnOamVccvTrCtlReplyMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('ip',2),(_AH,4)))
_TnOamVccvTrCtlReplyMode_Type.__name__=_I
_TnOamVccvTrCtlReplyMode_Object=MibTableColumn
tnOamVccvTrCtlReplyMode=_TnOamVccvTrCtlReplyMode_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,2),_TnOamVccvTrCtlReplyMode_Type())
tnOamVccvTrCtlReplyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlReplyMode.setStatus(_A)
class _TnOamVccvTrCtlSpokeSdpId_Type(TmnxSpokeSdpIdOrZero):defaultValue=0
_TnOamVccvTrCtlSpokeSdpId_Type.__name__=_t
_TnOamVccvTrCtlSpokeSdpId_Object=MibTableColumn
tnOamVccvTrCtlSpokeSdpId=_TnOamVccvTrCtlSpokeSdpId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,3),_TnOamVccvTrCtlSpokeSdpId_Type())
tnOamVccvTrCtlSpokeSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlSpokeSdpId.setStatus(_A)
class _TnOamVccvTrCtlSaiiGlobalId_Type(TmnxPwGlobalIdOrZero):defaultValue=0
_TnOamVccvTrCtlSaiiGlobalId_Type.__name__=_V
_TnOamVccvTrCtlSaiiGlobalId_Object=MibTableColumn
tnOamVccvTrCtlSaiiGlobalId=_TnOamVccvTrCtlSaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,4),_TnOamVccvTrCtlSaiiGlobalId_Type())
tnOamVccvTrCtlSaiiGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlSaiiGlobalId.setStatus(_A)
class _TnOamVccvTrCtlSaiiPrefix_Type(Unsigned32):defaultValue=0
_TnOamVccvTrCtlSaiiPrefix_Type.__name__=_D
_TnOamVccvTrCtlSaiiPrefix_Object=MibTableColumn
tnOamVccvTrCtlSaiiPrefix=_TnOamVccvTrCtlSaiiPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,5),_TnOamVccvTrCtlSaiiPrefix_Type())
tnOamVccvTrCtlSaiiPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlSaiiPrefix.setStatus(_A)
class _TnOamVccvTrCtlSaiiAcId_Type(Unsigned32):defaultValue=0
_TnOamVccvTrCtlSaiiAcId_Type.__name__=_D
_TnOamVccvTrCtlSaiiAcId_Object=MibTableColumn
tnOamVccvTrCtlSaiiAcId=_TnOamVccvTrCtlSaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,6),_TnOamVccvTrCtlSaiiAcId_Type())
tnOamVccvTrCtlSaiiAcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlSaiiAcId.setStatus(_A)
class _TnOamVccvTrCtlTaiiGlobalId_Type(TmnxPwGlobalIdOrZero):defaultValue=0
_TnOamVccvTrCtlTaiiGlobalId_Type.__name__=_V
_TnOamVccvTrCtlTaiiGlobalId_Object=MibTableColumn
tnOamVccvTrCtlTaiiGlobalId=_TnOamVccvTrCtlTaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,7),_TnOamVccvTrCtlTaiiGlobalId_Type())
tnOamVccvTrCtlTaiiGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlTaiiGlobalId.setStatus(_A)
class _TnOamVccvTrCtlTaiiPrefix_Type(Unsigned32):defaultValue=0
_TnOamVccvTrCtlTaiiPrefix_Type.__name__=_D
_TnOamVccvTrCtlTaiiPrefix_Object=MibTableColumn
tnOamVccvTrCtlTaiiPrefix=_TnOamVccvTrCtlTaiiPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,8),_TnOamVccvTrCtlTaiiPrefix_Type())
tnOamVccvTrCtlTaiiPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlTaiiPrefix.setStatus(_A)
class _TnOamVccvTrCtlTaiiAcId_Type(Unsigned32):defaultValue=0
_TnOamVccvTrCtlTaiiAcId_Type.__name__=_D
_TnOamVccvTrCtlTaiiAcId_Object=MibTableColumn
tnOamVccvTrCtlTaiiAcId=_TnOamVccvTrCtlTaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,9),_TnOamVccvTrCtlTaiiAcId_Type())
tnOamVccvTrCtlTaiiAcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlTaiiAcId.setStatus(_A)
class _TnOamVccvTrCtlTestSubMode_Type(TmnxOamVccvTestSubMode):defaultValue=1
_TnOamVccvTrCtlTestSubMode_Type.__name__=_A4
_TnOamVccvTrCtlTestSubMode_Object=MibTableColumn
tnOamVccvTrCtlTestSubMode=_TnOamVccvTrCtlTestSubMode_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,10),_TnOamVccvTrCtlTestSubMode_Type())
tnOamVccvTrCtlTestSubMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlTestSubMode.setStatus(_A)
class _TnOamVccvTrCtlAssocChannel_Type(TmnxOamVccvAssocChannel):defaultValue=1
_TnOamVccvTrCtlAssocChannel_Type.__name__=_A5
_TnOamVccvTrCtlAssocChannel_Object=MibTableColumn
tnOamVccvTrCtlAssocChannel=_TnOamVccvTrCtlAssocChannel_Object((1,3,6,1,4,1,7483,6,1,2,11,2,26,1,11),_TnOamVccvTrCtlAssocChannel_Type())
tnOamVccvTrCtlAssocChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamVccvTrCtlAssocChannel.setStatus(_A)
_TnOamVccvTrNextPwSegmentTable_Object=MibTable
tnOamVccvTrNextPwSegmentTable=_TnOamVccvTrNextPwSegmentTable_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27))
if mibBuilder.loadTexts:tnOamVccvTrNextPwSegmentTable.setStatus(_A)
_TnOamVccvTrNextPwSegmentEntry_Object=MibTableRow
tnOamVccvTrNextPwSegmentEntry=_TnOamVccvTrNextPwSegmentEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1))
tnOamVccvTrNextPwSegmentEntry.setIndexNames((0,_J,_K),(0,_E,_P),(0,_E,_Z),(0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:tnOamVccvTrNextPwSegmentEntry.setStatus(_A)
_TnOamVccvTrNextPwID_Type=TmnxVcIdOrNone
_TnOamVccvTrNextPwID_Object=MibTableColumn
tnOamVccvTrNextPwID=_TnOamVccvTrNextPwID_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,1),_TnOamVccvTrNextPwID_Type())
tnOamVccvTrNextPwID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextPwID.setStatus(_A)
_TnOamVccvTrNextPwType_Type=SdpBindVcType
_TnOamVccvTrNextPwType_Object=MibTableColumn
tnOamVccvTrNextPwType=_TnOamVccvTrNextPwType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,2),_TnOamVccvTrNextPwType_Type())
tnOamVccvTrNextPwType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextPwType.setStatus(_A)
_TnOamVccvTrNextSenderAddrType_Type=InetAddressType
_TnOamVccvTrNextSenderAddrType_Object=MibTableColumn
tnOamVccvTrNextSenderAddrType=_TnOamVccvTrNextSenderAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,3),_TnOamVccvTrNextSenderAddrType_Type())
tnOamVccvTrNextSenderAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextSenderAddrType.setStatus(_A)
class _TnOamVccvTrNextSenderAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamVccvTrNextSenderAddr_Type.__name__=_G
_TnOamVccvTrNextSenderAddr_Object=MibTableColumn
tnOamVccvTrNextSenderAddr=_TnOamVccvTrNextSenderAddr_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,4),_TnOamVccvTrNextSenderAddr_Type())
tnOamVccvTrNextSenderAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextSenderAddr.setStatus(_A)
_TnOamVccvTrNextRemoteAddrType_Type=InetAddressType
_TnOamVccvTrNextRemoteAddrType_Object=MibTableColumn
tnOamVccvTrNextRemoteAddrType=_TnOamVccvTrNextRemoteAddrType_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,5),_TnOamVccvTrNextRemoteAddrType_Type())
tnOamVccvTrNextRemoteAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextRemoteAddrType.setStatus(_A)
class _TnOamVccvTrNextRemoteAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnOamVccvTrNextRemoteAddr_Type.__name__=_G
_TnOamVccvTrNextRemoteAddr_Object=MibTableColumn
tnOamVccvTrNextRemoteAddr=_TnOamVccvTrNextRemoteAddr_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,6),_TnOamVccvTrNextRemoteAddr_Type())
tnOamVccvTrNextRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextRemoteAddr.setStatus(_A)
_TnOamVccvTrNextSaiiGlobalId_Type=TmnxPwGlobalIdOrZero
_TnOamVccvTrNextSaiiGlobalId_Object=MibTableColumn
tnOamVccvTrNextSaiiGlobalId=_TnOamVccvTrNextSaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,7),_TnOamVccvTrNextSaiiGlobalId_Type())
tnOamVccvTrNextSaiiGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextSaiiGlobalId.setStatus(_A)
_TnOamVccvTrNextSaiiPrefix_Type=Unsigned32
_TnOamVccvTrNextSaiiPrefix_Object=MibTableColumn
tnOamVccvTrNextSaiiPrefix=_TnOamVccvTrNextSaiiPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,8),_TnOamVccvTrNextSaiiPrefix_Type())
tnOamVccvTrNextSaiiPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextSaiiPrefix.setStatus(_A)
_TnOamVccvTrNextSaiiAcId_Type=Unsigned32
_TnOamVccvTrNextSaiiAcId_Object=MibTableColumn
tnOamVccvTrNextSaiiAcId=_TnOamVccvTrNextSaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,9),_TnOamVccvTrNextSaiiAcId_Type())
tnOamVccvTrNextSaiiAcId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextSaiiAcId.setStatus(_A)
_TnOamVccvTrNextTaiiGlobalId_Type=TmnxPwGlobalIdOrZero
_TnOamVccvTrNextTaiiGlobalId_Object=MibTableColumn
tnOamVccvTrNextTaiiGlobalId=_TnOamVccvTrNextTaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,10),_TnOamVccvTrNextTaiiGlobalId_Type())
tnOamVccvTrNextTaiiGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTaiiGlobalId.setStatus(_A)
_TnOamVccvTrNextTaiiPrefix_Type=Unsigned32
_TnOamVccvTrNextTaiiPrefix_Object=MibTableColumn
tnOamVccvTrNextTaiiPrefix=_TnOamVccvTrNextTaiiPrefix_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,11),_TnOamVccvTrNextTaiiPrefix_Type())
tnOamVccvTrNextTaiiPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTaiiPrefix.setStatus(_A)
_TnOamVccvTrNextTaiiAcId_Type=Unsigned32
_TnOamVccvTrNextTaiiAcId_Object=MibTableColumn
tnOamVccvTrNextTaiiAcId=_TnOamVccvTrNextTaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,12),_TnOamVccvTrNextTaiiAcId_Type())
tnOamVccvTrNextTaiiAcId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTaiiAcId.setStatus(_A)
class _TnOamVccvTrNextTpAgi_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_TnOamVccvTrNextTpAgi_Type.__name__=_Q
_TnOamVccvTrNextTpAgi_Object=MibTableColumn
tnOamVccvTrNextTpAgi=_TnOamVccvTrNextTpAgi_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,13),_TnOamVccvTrNextTpAgi_Type())
tnOamVccvTrNextTpAgi.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTpAgi.setStatus(_A)
_TnOamVccvTrNextTpSaiiGlobalId_Type=TmnxMplsTpGlobalID
_TnOamVccvTrNextTpSaiiGlobalId_Object=MibTableColumn
tnOamVccvTrNextTpSaiiGlobalId=_TnOamVccvTrNextTpSaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,14),_TnOamVccvTrNextTpSaiiGlobalId_Type())
tnOamVccvTrNextTpSaiiGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTpSaiiGlobalId.setStatus(_A)
_TnOamVccvTrNextTpSaiiNodeId_Type=TmnxMplsTpNodeID
_TnOamVccvTrNextTpSaiiNodeId_Object=MibTableColumn
tnOamVccvTrNextTpSaiiNodeId=_TnOamVccvTrNextTpSaiiNodeId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,15),_TnOamVccvTrNextTpSaiiNodeId_Type())
tnOamVccvTrNextTpSaiiNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTpSaiiNodeId.setStatus(_A)
_TnOamVccvTrNextTpSaiiAcId_Type=Unsigned32
_TnOamVccvTrNextTpSaiiAcId_Object=MibTableColumn
tnOamVccvTrNextTpSaiiAcId=_TnOamVccvTrNextTpSaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,16),_TnOamVccvTrNextTpSaiiAcId_Type())
tnOamVccvTrNextTpSaiiAcId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTpSaiiAcId.setStatus(_A)
_TnOamVccvTrNextTpTaiiGlobalId_Type=TmnxMplsTpGlobalID
_TnOamVccvTrNextTpTaiiGlobalId_Object=MibTableColumn
tnOamVccvTrNextTpTaiiGlobalId=_TnOamVccvTrNextTpTaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,17),_TnOamVccvTrNextTpTaiiGlobalId_Type())
tnOamVccvTrNextTpTaiiGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTpTaiiGlobalId.setStatus(_A)
_TnOamVccvTrNextTpTaiiNodeId_Type=TmnxMplsTpNodeID
_TnOamVccvTrNextTpTaiiNodeId_Object=MibTableColumn
tnOamVccvTrNextTpTaiiNodeId=_TnOamVccvTrNextTpTaiiNodeId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,18),_TnOamVccvTrNextTpTaiiNodeId_Type())
tnOamVccvTrNextTpTaiiNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTpTaiiNodeId.setStatus(_A)
_TnOamVccvTrNextTpTaiiAcId_Type=Unsigned32
_TnOamVccvTrNextTpTaiiAcId_Object=MibTableColumn
tnOamVccvTrNextTpTaiiAcId=_TnOamVccvTrNextTpTaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,11,2,27,1,19),_TnOamVccvTrNextTpTaiiAcId_Type())
tnOamVccvTrNextTpTaiiAcId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamVccvTrNextTpTaiiAcId.setStatus(_A)
_TnOamSaaObjs_ObjectIdentity=ObjectIdentity
tnOamSaaObjs=_TnOamSaaObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,11,3))
_TnOamSaaCtlAttributeTotal_Type=Integer32
_TnOamSaaCtlAttributeTotal_Object=MibScalar
tnOamSaaCtlAttributeTotal=_TnOamSaaCtlAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,11,3,3),_TnOamSaaCtlAttributeTotal_Type())
tnOamSaaCtlAttributeTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamSaaCtlAttributeTotal.setStatus(_A)
_TnOamSaaCtlTable_Object=MibTable
tnOamSaaCtlTable=_TnOamSaaCtlTable_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4))
if mibBuilder.loadTexts:tnOamSaaCtlTable.setStatus(_A)
_TnOamSaaCtlEntry_Object=MibTableRow
tnOamSaaCtlEntry=_TnOamSaaCtlEntry_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1))
tnOamSaaCtlEntry.setIndexNames((0,_J,_K),(0,_E,_AK))
if mibBuilder.loadTexts:tnOamSaaCtlEntry.setStatus(_A)
class _TnOamSaaCtlTestIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TnOamSaaCtlTestIndex_Type.__name__=_R
_TnOamSaaCtlTestIndex_Object=MibTableColumn
tnOamSaaCtlTestIndex=_TnOamSaaCtlTestIndex_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,1),_TnOamSaaCtlTestIndex_Type())
tnOamSaaCtlTestIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tnOamSaaCtlTestIndex.setStatus(_A)
_TnOamSaaCtlRowStatus_Type=RowStatus
_TnOamSaaCtlRowStatus_Object=MibTableColumn
tnOamSaaCtlRowStatus=_TnOamSaaCtlRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,2),_TnOamSaaCtlRowStatus_Type())
tnOamSaaCtlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlRowStatus.setStatus(_A)
class _TnOamSaaCtlStorageType_Type(StorageType):defaultValue=3
_TnOamSaaCtlStorageType_Type.__name__=_a
_TnOamSaaCtlStorageType_Object=MibTableColumn
tnOamSaaCtlStorageType=_TnOamSaaCtlStorageType_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,3),_TnOamSaaCtlStorageType_Type())
tnOamSaaCtlStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlStorageType.setStatus(_A)
_TnOamSaaCtlLastChanged_Type=TimeStamp
_TnOamSaaCtlLastChanged_Object=MibTableColumn
tnOamSaaCtlLastChanged=_TnOamSaaCtlLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,4),_TnOamSaaCtlLastChanged_Type())
tnOamSaaCtlLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamSaaCtlLastChanged.setStatus(_A)
class _TnOamSaaCtlAdminStatus_Type(TmnxAdminState):defaultValue=3
_TnOamSaaCtlAdminStatus_Type.__name__=_A9
_TnOamSaaCtlAdminStatus_Object=MibTableColumn
tnOamSaaCtlAdminStatus=_TnOamSaaCtlAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,5),_TnOamSaaCtlAdminStatus_Type())
tnOamSaaCtlAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlAdminStatus.setStatus(_A)
class _TnOamSaaCtlDescr_Type(TItemDescription):defaultHexValue=''
_TnOamSaaCtlDescr_Type.__name__=_A8
_TnOamSaaCtlDescr_Object=MibTableColumn
tnOamSaaCtlDescr=_TnOamSaaCtlDescr_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,6),_TnOamSaaCtlDescr_Type())
tnOamSaaCtlDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlDescr.setStatus(_A)
class _TnOamSaaCtlTestMode_Type(TmnxOamTestMode):defaultValue=0
_TnOamSaaCtlTestMode_Type.__name__=_AL
_TnOamSaaCtlTestMode_Object=MibTableColumn
tnOamSaaCtlTestMode=_TnOamSaaCtlTestMode_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,7),_TnOamSaaCtlTestMode_Type())
tnOamSaaCtlTestMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamSaaCtlTestMode.setStatus(_A)
_TnOamSaaCtlRuns_Type=Counter32
_TnOamSaaCtlRuns_Object=MibTableColumn
tnOamSaaCtlRuns=_TnOamSaaCtlRuns_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,8),_TnOamSaaCtlRuns_Type())
tnOamSaaCtlRuns.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamSaaCtlRuns.setStatus(_A)
_TnOamSaaCtlFailures_Type=Counter32
_TnOamSaaCtlFailures_Object=MibTableColumn
tnOamSaaCtlFailures=_TnOamSaaCtlFailures_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,9),_TnOamSaaCtlFailures_Type())
tnOamSaaCtlFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamSaaCtlFailures.setStatus(_A)
_TnOamSaaCtlLastRunResult_Type=TmnxOamTestResult
_TnOamSaaCtlLastRunResult_Object=MibTableColumn
tnOamSaaCtlLastRunResult=_TnOamSaaCtlLastRunResult_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,10),_TnOamSaaCtlLastRunResult_Type())
tnOamSaaCtlLastRunResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamSaaCtlLastRunResult.setStatus(_A)
class _TnOamSaaCtlAcctPolicyId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TnOamSaaCtlAcctPolicyId_Type.__name__=_I
_TnOamSaaCtlAcctPolicyId_Object=MibTableColumn
tnOamSaaCtlAcctPolicyId=_TnOamSaaCtlAcctPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,11),_TnOamSaaCtlAcctPolicyId_Type())
tnOamSaaCtlAcctPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlAcctPolicyId.setStatus(_A)
class _TnOamSaaCtlSuppressAccounting_Type(TruthValue):defaultValue=2
_TnOamSaaCtlSuppressAccounting_Type.__name__=_M
_TnOamSaaCtlSuppressAccounting_Object=MibTableColumn
tnOamSaaCtlSuppressAccounting=_TnOamSaaCtlSuppressAccounting_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,12),_TnOamSaaCtlSuppressAccounting_Type())
tnOamSaaCtlSuppressAccounting.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlSuppressAccounting.setStatus(_A)
class _TnOamSaaCtlContinuous_Type(TruthValue):defaultValue=2
_TnOamSaaCtlContinuous_Type.__name__=_M
_TnOamSaaCtlContinuous_Object=MibTableColumn
tnOamSaaCtlContinuous=_TnOamSaaCtlContinuous_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,13),_TnOamSaaCtlContinuous_Type())
tnOamSaaCtlContinuous.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlContinuous.setStatus(_A)
class _TnOamSaaCtlKeepProbeHistoryAdm_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('keep',1),('drop',2),('auto',3)))
_TnOamSaaCtlKeepProbeHistoryAdm_Type.__name__=_I
_TnOamSaaCtlKeepProbeHistoryAdm_Object=MibTableColumn
tnOamSaaCtlKeepProbeHistoryAdm=_TnOamSaaCtlKeepProbeHistoryAdm_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,15),_TnOamSaaCtlKeepProbeHistoryAdm_Type())
tnOamSaaCtlKeepProbeHistoryAdm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlKeepProbeHistoryAdm.setStatus(_A)
class _TnOamSaaCtlKeepProbeHistoryOpr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keep',1),('drop',2)))
_TnOamSaaCtlKeepProbeHistoryOpr_Type.__name__=_I
_TnOamSaaCtlKeepProbeHistoryOpr_Object=MibTableColumn
tnOamSaaCtlKeepProbeHistoryOpr=_TnOamSaaCtlKeepProbeHistoryOpr_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,16),_TnOamSaaCtlKeepProbeHistoryOpr_Type())
tnOamSaaCtlKeepProbeHistoryOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamSaaCtlKeepProbeHistoryOpr.setStatus(_A)
class _TnOamSaaCtlAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnOamSaaCtlAlmProfName_Type.__name__=_Q
_TnOamSaaCtlAlmProfName_Object=MibTableColumn
tnOamSaaCtlAlmProfName=_TnOamSaaCtlAlmProfName_Object((1,3,6,1,4,1,7483,6,1,2,11,3,4,1,17),_TnOamSaaCtlAlmProfName_Type())
tnOamSaaCtlAlmProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnOamSaaCtlAlmProfName.setStatus(_A)
_TnOamTestScalar1_Type=Unsigned32
_TnOamTestScalar1_Object=MibScalar
tnOamTestScalar1=_TnOamTestScalar1_Object((1,3,6,1,4,1,7483,6,1,2,11,101),_TnOamTestScalar1_Type())
tnOamTestScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTestScalar1.setStatus(_A)
_TnOamTestScalar2_Type=Unsigned32
_TnOamTestScalar2_Object=MibScalar
tnOamTestScalar2=_TnOamTestScalar2_Object((1,3,6,1,4,1,7483,6,1,2,11,102),_TnOamTestScalar2_Type())
tnOamTestScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOamTestScalar2.setStatus(_A)
_TnOamTestNotifications_ObjectIdentity=ObjectIdentity
tnOamTestNotifications=_TnOamTestNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,11))
_TnOamPingNotifyPrefix_ObjectIdentity=ObjectIdentity
tnOamPingNotifyPrefix=_TnOamPingNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,11,1))
_TnOamPingNotifications_ObjectIdentity=ObjectIdentity
tnOamPingNotifications=_TnOamPingNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,11,1,0))
_TnOamTraceRouteNotifyPrefix_ObjectIdentity=ObjectIdentity
tnOamTraceRouteNotifyPrefix=_TnOamTraceRouteNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,11,2))
_TnOamTraceRouteNotifications_ObjectIdentity=ObjectIdentity
tnOamTraceRouteNotifications=_TnOamTraceRouteNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,11,2,0))
_TnOamSaaNotifyPrefix_ObjectIdentity=ObjectIdentity
tnOamSaaNotifyPrefix=_TnOamSaaNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,11,3))
_TnOamSaaNotifications_ObjectIdentity=ObjectIdentity
tnOamSaaNotifications=_TnOamSaaNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,11,3,0))
tnOamPingCtlEntry.registerAugmentions((_E,_AM))
tnOamEthCfmPingCtlEntry.setIndexNames(*tnOamPingCtlEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_A3:TmnxOamLspAssocChannel,_A1:TmnxOamLspTestSubMode,'TmnxOamMplsEchoDownMapTlv':TmnxOamMplsEchoDownMapTlv,_AI:TmnxOamMplsEchoDownMapTlvOrNone,_A2:TmnxOamMplsTpPathType,_AL:TmnxOamTestMode,'TmnxOamPingRtnCode':TmnxOamPingRtnCode,'TmnxOamAddressType':TmnxOamAddressType,'TmnxOamResponseStatus':TmnxOamResponseStatus,'TmnxOamSignalProtocol':TmnxOamSignalProtocol,'TmnxOamTestResponsePlane':TmnxOamTestResponsePlane,'TmnxOamSaaThreshold':TmnxOamSaaThreshold,_A5:TmnxOamVccvAssocChannel,_A4:TmnxOamVccvTestSubMode,'TmnxOamVcType':TmnxOamVcType,'TmnxOamTestResult':TmnxOamTestResult,'tnOamTestMIBModule':tnOamTestMIBModule,'tnOamTestObjs':tnOamTestObjs,'tnOamPingObjs':tnOamPingObjs,'tnOamPingCtlAttributeTotal':tnOamPingCtlAttributeTotal,'tnOamPingCtlTable':tnOamPingCtlTable,'tnOamPingCtlEntry':tnOamPingCtlEntry,_S:tnOamPingCtlTestIndex,'tnOamPingCtlRowStatus':tnOamPingCtlRowStatus,'tnOamPingCtlStorageType':tnOamPingCtlStorageType,'tnOamPingCtlDescr':tnOamPingCtlDescr,'tnOamPingCtlTestMode':tnOamPingCtlTestMode,'tnOamPingCtlAdminStatus':tnOamPingCtlAdminStatus,'tnOamPingCtlOrigSdpId':tnOamPingCtlOrigSdpId,'tnOamPingCtlRespSdpId':tnOamPingCtlRespSdpId,'tnOamPingCtlFcName':tnOamPingCtlFcName,'tnOamPingCtlProfile':tnOamPingCtlProfile,'tnOamPingCtlMtuStartSize':tnOamPingCtlMtuStartSize,'tnOamPingCtlMtuEndSize':tnOamPingCtlMtuEndSize,'tnOamPingCtlMtuStepSize':tnOamPingCtlMtuStepSize,'tnOamPingCtlTargetIpAddress':tnOamPingCtlTargetIpAddress,'tnOamPingCtlServiceId':tnOamPingCtlServiceId,'tnOamPingCtlLocalSdp':tnOamPingCtlLocalSdp,'tnOamPingCtlRemoteSdp':tnOamPingCtlRemoteSdp,'tnOamPingCtlSize':tnOamPingCtlSize,'tnOamPingCtlTimeOut':tnOamPingCtlTimeOut,'tnOamPingCtlProbeCount':tnOamPingCtlProbeCount,'tnOamPingCtlInterval':tnOamPingCtlInterval,'tnOamPingCtlMaxRows':tnOamPingCtlMaxRows,'tnOamPingCtlTrapGeneration':tnOamPingCtlTrapGeneration,'tnOamPingCtlTrapProbeFailureFilter':tnOamPingCtlTrapProbeFailureFilter,'tnOamPingCtlTrapTestFailureFilter':tnOamPingCtlTrapTestFailureFilter,'tnOamPingCtlSAA':tnOamPingCtlSAA,'tnOamPingCtlRuns':tnOamPingCtlRuns,'tnOamPingCtlFailures':tnOamPingCtlFailures,'tnOamPingCtlLastRunResult':tnOamPingCtlLastRunResult,'tnOamPingCtlLastChanged':tnOamPingCtlLastChanged,'tnOamPingCtlVRtrID':tnOamPingCtlVRtrID,'tnOamPingCtlTgtAddrType':tnOamPingCtlTgtAddrType,'tnOamPingCtlTgtAddress':tnOamPingCtlTgtAddress,'tnOamPingCtlSrcAddrType':tnOamPingCtlSrcAddrType,'tnOamPingCtlSrcAddress':tnOamPingCtlSrcAddress,'tnOamPingCtlDnsName':tnOamPingCtlDnsName,'tnOamPingCtlDNSRecord':tnOamPingCtlDNSRecord,'tnOamPingCtlIntervalUnits':tnOamPingCtlIntervalUnits,'tnOamPingResultsTable':tnOamPingResultsTable,'tnOamPingResultsEntry':tnOamPingResultsEntry,'tnOamPingResultsOperStatus':tnOamPingResultsOperStatus,'tnOamPingResultsMinRtt':tnOamPingResultsMinRtt,'tnOamPingResultsMaxRtt':tnOamPingResultsMaxRtt,'tnOamPingResultsAverageRtt':tnOamPingResultsAverageRtt,'tnOamPingResultsRttSumOfSquares':tnOamPingResultsRttSumOfSquares,'tnOamPingResultsMtuResponseSize':tnOamPingResultsMtuResponseSize,'tnOamPingResultsSvcPing':tnOamPingResultsSvcPing,'tnOamPingResultsProbeResponses':tnOamPingResultsProbeResponses,'tnOamPingResultsSentProbes':tnOamPingResultsSentProbes,'tnOamPingResultsLastGoodProbe':tnOamPingResultsLastGoodProbe,'tnOamPingResultsLastRespHeader':tnOamPingResultsLastRespHeader,'tnOamPingResultsMinTt':tnOamPingResultsMinTt,'tnOamPingResultsMaxTt':tnOamPingResultsMaxTt,'tnOamPingResultsAverageTt':tnOamPingResultsAverageTt,'tnOamPingResultsTtSumOfSquares':tnOamPingResultsTtSumOfSquares,'tnOamPingResultsMinInTt':tnOamPingResultsMinInTt,'tnOamPingResultsMaxInTt':tnOamPingResultsMaxInTt,'tnOamPingResultsAverageInTt':tnOamPingResultsAverageInTt,'tnOamPingResultsInTtSumOfSqrs':tnOamPingResultsInTtSumOfSqrs,'tnOamPingResultsOutJitter':tnOamPingResultsOutJitter,'tnOamPingResultsInJitter':tnOamPingResultsInJitter,'tnOamPingResultsRtJitter':tnOamPingResultsRtJitter,'tnOamPingResultsProbeTimeouts':tnOamPingResultsProbeTimeouts,'tnOamPingResultsProbeFailures':tnOamPingResultsProbeFailures,_z:tnOamPingResultsTestRunIndex,'tnOamPingResultsRttOFSumSquares':tnOamPingResultsRttOFSumSquares,'tnOamPingResultsRttHCSumSquares':tnOamPingResultsRttHCSumSquares,'tnOamPingResultsTtOFSumSquares':tnOamPingResultsTtOFSumSquares,'tnOamPingResultsTtHCSumSquares':tnOamPingResultsTtHCSumSquares,'tnOamPingResultsInTtOFSumSqrs':tnOamPingResultsInTtOFSumSqrs,'tnOamPingResultsInTtHCSumSqrs':tnOamPingResultsInTtHCSumSqrs,'tnOamPingResultsTestRunResult':tnOamPingResultsTestRunResult,'tnOamPingHistoryTable':tnOamPingHistoryTable,'tnOamPingHistoryEntry':tnOamPingHistoryEntry,_AF:tnOamPingHistoryIndex,'tnOamPingHistoryResponse':tnOamPingHistoryResponse,'tnOamPingHistoryOneWayTime':tnOamPingHistoryOneWayTime,'tnOamPingHistorySize':tnOamPingHistorySize,'tnOamPingHistoryStatus':tnOamPingHistoryStatus,'tnOamPingHistoryTime':tnOamPingHistoryTime,'tnOamPingHistoryReturnCode':tnOamPingHistoryReturnCode,'tnOamPingHistorySrcIpAddress':tnOamPingHistorySrcIpAddress,'tnOamPingHistAddressType':tnOamPingHistAddressType,'tnOamPingHistSapId':tnOamPingHistSapId,'tnOamPingHistoryVersion':tnOamPingHistoryVersion,'tnOamPingHistoryCpeMacAddr':tnOamPingHistoryCpeMacAddr,'tnOamPingHistoryRespSvcId':tnOamPingHistoryRespSvcId,'tnOamPingHistorySequence':tnOamPingHistorySequence,'tnOamPingHistoryIfIndex':tnOamPingHistoryIfIndex,'tnOamPingHistoryDataLen':tnOamPingHistoryDataLen,'tnOamPingHistoryRespPlane':tnOamPingHistoryRespPlane,'tnOamPingHistoryReqHdr':tnOamPingHistoryReqHdr,'tnOamPingHistoryRespHdr':tnOamPingHistoryRespHdr,'tnOamPingHistoryDnsAddrType':tnOamPingHistoryDnsAddrType,'tnOamPingHistoryDnsAddress':tnOamPingHistoryDnsAddress,'tnOamPingHistorySrcAddrType':tnOamPingHistorySrcAddrType,'tnOamPingHistorySrcAddress':tnOamPingHistorySrcAddress,'tnOamPingHistoryInOneWayTime':tnOamPingHistoryInOneWayTime,'tnOamPingHistoryLspName':tnOamPingHistoryLspName,'tnOamPingHistNextHopAddrType':tnOamPingHistNextHopAddrType,'tnOamPingHistNextHopAddress':tnOamPingHistNextHopAddress,'tnOamPingHistorySrcGlobalId':tnOamPingHistorySrcGlobalId,'tnOamPingHistorySrcNodeId':tnOamPingHistorySrcNodeId,'tnOamPingHistorySdpBindId':tnOamPingHistorySdpBindId,'tnOamPingHistoryRtrnSubcode':tnOamPingHistoryRtrnSubcode,'tnOamLspPingCtlTable':tnOamLspPingCtlTable,'tnOamLspPingCtlEntry':tnOamLspPingCtlEntry,'tnOamLspPingCtlVRtrID':tnOamLspPingCtlVRtrID,'tnOamLspPingCtlLspName':tnOamLspPingCtlLspName,'tnOamLspPingCtlReturnLsp':tnOamLspPingCtlReturnLsp,'tnOamLspPingCtlTtl':tnOamLspPingCtlTtl,'tnOamLspPingCtlPathName':tnOamLspPingCtlPathName,'tnOamLspPingCtlLdpIpPrefix':tnOamLspPingCtlLdpIpPrefix,'tnOamLspPingCtlLdpIpPrefixLen':tnOamLspPingCtlLdpIpPrefixLen,'tnOamLspPingCtlLdpPrefixType':tnOamLspPingCtlLdpPrefixType,'tnOamLspPingCtlLdpPrefix':tnOamLspPingCtlLdpPrefix,'tnOamLspPingCtlLdpPrefixLen':tnOamLspPingCtlLdpPrefixLen,'tnOamLspPingCtlPathDestType':tnOamLspPingCtlPathDestType,'tnOamLspPingCtlPathDest':tnOamLspPingCtlPathDest,'tnOamLspPingCtlNhIntfName':tnOamLspPingCtlNhIntfName,'tnOamLspPingCtlNhAddressType':tnOamLspPingCtlNhAddressType,'tnOamLspPingCtlNhAddress':tnOamLspPingCtlNhAddress,'tnOamLspPingCtlTestSubMode':tnOamLspPingCtlTestSubMode,'tnOamLspPingCtlMplsTpPathType':tnOamLspPingCtlMplsTpPathType,'tnOamLspPingCtlMplsTpGlobalId':tnOamLspPingCtlMplsTpGlobalId,'tnOamLspPingCtlMplsTpNodeId':tnOamLspPingCtlMplsTpNodeId,'tnOamLspPingCtlAssocChannel':tnOamLspPingCtlAssocChannel,'tnOamLspPingCtlForce':tnOamLspPingCtlForce,'tnOamVccvPingCtlTable':tnOamVccvPingCtlTable,'tnOamVccvPingCtlEntry':tnOamVccvPingCtlEntry,'tnOamVccvPingCtlSdpIdVcId':tnOamVccvPingCtlSdpIdVcId,'tnOamVccvPingCtlReplyMode':tnOamVccvPingCtlReplyMode,'tnOamVccvPingCtlPwId':tnOamVccvPingCtlPwId,'tnOamVccvPingCtlTtl':tnOamVccvPingCtlTtl,'tnOamVccvPingCtlSpokeSdpId':tnOamVccvPingCtlSpokeSdpId,'tnOamVccvPingCtlSaiiGlobalId':tnOamVccvPingCtlSaiiGlobalId,'tnOamVccvPingCtlSaiiPrefix':tnOamVccvPingCtlSaiiPrefix,'tnOamVccvPingCtlSaiiAcId':tnOamVccvPingCtlSaiiAcId,'tnOamVccvPingCtlTaiiGlobalId':tnOamVccvPingCtlTaiiGlobalId,'tnOamVccvPingCtlTaiiPrefix':tnOamVccvPingCtlTaiiPrefix,'tnOamVccvPingCtlTaiiAcId':tnOamVccvPingCtlTaiiAcId,'tnOamVccvPingCtlMplsTpGlobalId':tnOamVccvPingCtlMplsTpGlobalId,'tnOamVccvPingCtlMplsTpNodeId':tnOamVccvPingCtlMplsTpNodeId,'tnOamVccvPingCtlTestSubMode':tnOamVccvPingCtlTestSubMode,'tnOamVccvPingCtlAssocChannel':tnOamVccvPingCtlAssocChannel,'tnOamEthCfmPingCtlTable':tnOamEthCfmPingCtlTable,_AM:tnOamEthCfmPingCtlEntry,'tnOamEthCfmPingCtlTgtMacAddr':tnOamEthCfmPingCtlTgtMacAddr,'tnOamEthCfmPingCtlSrcMdIndex':tnOamEthCfmPingCtlSrcMdIndex,'tnOamEthCfmPingCtlSrcMaIndex':tnOamEthCfmPingCtlSrcMaIndex,'tnOamEthCfmPingCtlSrcMepId':tnOamEthCfmPingCtlSrcMepId,'tnOamTraceRouteObjs':tnOamTraceRouteObjs,'tnOamTrCtlTable':tnOamTrCtlTable,'tnOamTrCtlEntry':tnOamTrCtlEntry,_P:tnOamTrCtlTestIndex,'tnOamTrCtlRowStatus':tnOamTrCtlRowStatus,'tnOamTrCtlStorageType':tnOamTrCtlStorageType,'tnOamTrCtlDescr':tnOamTrCtlDescr,'tnOamTrCtlTestMode':tnOamTrCtlTestMode,'tnOamTrCtlAdminStatus':tnOamTrCtlAdminStatus,'tnOamTrCtlFcName':tnOamTrCtlFcName,'tnOamTrCtlProfile':tnOamTrCtlProfile,'tnOamTrCtlTargetIpAddress':tnOamTrCtlTargetIpAddress,'tnOamTrCtlServiceId':tnOamTrCtlServiceId,'tnOamTrCtlDataSize':tnOamTrCtlDataSize,'tnOamTrCtlTimeOut':tnOamTrCtlTimeOut,'tnOamTrCtlProbesPerHop':tnOamTrCtlProbesPerHop,'tnOamTrCtlMaxTtl':tnOamTrCtlMaxTtl,'tnOamTrCtlInitialTtl':tnOamTrCtlInitialTtl,'tnOamTrCtlDSField':tnOamTrCtlDSField,'tnOamTrCtlMaxFailures':tnOamTrCtlMaxFailures,'tnOamTrCtlInterval':tnOamTrCtlInterval,'tnOamTrCtlMaxRows':tnOamTrCtlMaxRows,'tnOamTrCtlTrapGeneration':tnOamTrCtlTrapGeneration,'tnOamTrCtlCreateHopsEntries':tnOamTrCtlCreateHopsEntries,'tnOamTrCtlSAA':tnOamTrCtlSAA,'tnOamTrCtlRuns':tnOamTrCtlRuns,'tnOamTrCtlFailures':tnOamTrCtlFailures,'tnOamTrCtlLastRunResult':tnOamTrCtlLastRunResult,'tnOamTrCtlLastChanged':tnOamTrCtlLastChanged,'tnOamTrCtlVRtrID':tnOamTrCtlVRtrID,'tnOamTrCtlTgtAddrType':tnOamTrCtlTgtAddrType,'tnOamTrCtlTgtAddress':tnOamTrCtlTgtAddress,'tnOamTrCtlSrcAddrType':tnOamTrCtlSrcAddrType,'tnOamTrCtlSrcAddress':tnOamTrCtlSrcAddress,'tnOamTrCtlWaitMilliSec':tnOamTrCtlWaitMilliSec,'tnOamTrResultsTable':tnOamTrResultsTable,'tnOamTrResultsEntry':tnOamTrResultsEntry,'tnOamTrResultsOperStatus':tnOamTrResultsOperStatus,'tnOamTrResultsCurHopCount':tnOamTrResultsCurHopCount,'tnOamTrResultsCurProbeCount':tnOamTrResultsCurProbeCount,'tnOamTrResultsIpTgtAddr':tnOamTrResultsIpTgtAddr,'tnOamTrResultsTestAttempts':tnOamTrResultsTestAttempts,'tnOamTrResultsTestSuccesses':tnOamTrResultsTestSuccesses,'tnOamTrResultsLastGoodPath':tnOamTrResultsLastGoodPath,_Z:tnOamTrResultsTestRunIndex,'tnOamTrResultsTgtAddrType':tnOamTrResultsTgtAddrType,'tnOamTrResultsTgtAddress':tnOamTrResultsTgtAddress,'tnOamTrResultsTestRunResult':tnOamTrResultsTestRunResult,'tnOamTrProbeHistoryTable':tnOamTrProbeHistoryTable,'tnOamTrProbeHistoryEntry':tnOamTrProbeHistoryEntry,_g:tnOamTrProbeHistoryIndex,_h:tnOamTrProbeHistoryHopIndex,_i:tnOamTrProbeHistoryProbeIndex,'tnOamTrProbeHistoryIpAddr':tnOamTrProbeHistoryIpAddr,'tnOamTrProbeHistoryResponse':tnOamTrProbeHistoryResponse,'tnOamTrProbeHistoryOneWayTime':tnOamTrProbeHistoryOneWayTime,'tnOamTrProbeHistoryStatus':tnOamTrProbeHistoryStatus,'tnOamTrProbeHistoryLastRC':tnOamTrProbeHistoryLastRC,'tnOamTrProbeHistoryTime':tnOamTrProbeHistoryTime,'tnOamTrProbeHistoryResponsePlane':tnOamTrProbeHistoryResponsePlane,'tnOamTrProbeHistoryAddressType':tnOamTrProbeHistoryAddressType,'tnOamTrProbeHistorySapId':tnOamTrProbeHistorySapId,'tnOamTrProbeHistoryVersion':tnOamTrProbeHistoryVersion,'tnOamTrProbeHistoryRouterID':tnOamTrProbeHistoryRouterID,'tnOamTrProbeHistoryIfIndex':tnOamTrProbeHistoryIfIndex,'tnOamTrProbeHistoryDataLen':tnOamTrProbeHistoryDataLen,'tnOamTrProbeHistorySize':tnOamTrProbeHistorySize,'tnOamTrProbeHistoryInOneWayTime':tnOamTrProbeHistoryInOneWayTime,'tnOamTrProbeHistoryAddrType':tnOamTrProbeHistoryAddrType,'tnOamTrProbeHistoryAddress':tnOamTrProbeHistoryAddress,'tnOamTrProbeHistorySrcGlobalId':tnOamTrProbeHistorySrcGlobalId,'tnOamTrProbeHistorySrcNodeId':tnOamTrProbeHistorySrcNodeId,'tnOamLspTrCtlTable':tnOamLspTrCtlTable,'tnOamLspTrCtlEntry':tnOamLspTrCtlEntry,'tnOamLspTrCtlVRtrID':tnOamLspTrCtlVRtrID,'tnOamLspTrCtlLspName':tnOamLspTrCtlLspName,'tnOamLspTrCtlPathName':tnOamLspTrCtlPathName,'tnOamLspTrCtlLdpIpPrefix':tnOamLspTrCtlLdpIpPrefix,'tnOamLspTrCtlLdpIpPrefixLen':tnOamLspTrCtlLdpIpPrefixLen,'tnOamLspTrCtlLdpPrefixType':tnOamLspTrCtlLdpPrefixType,'tnOamLspTrCtlLdpPrefix':tnOamLspTrCtlLdpPrefix,'tnOamLspTrCtlLdpPrefixLen':tnOamLspTrCtlLdpPrefixLen,'tnOamLspTrCtlPathDestType':tnOamLspTrCtlPathDestType,'tnOamLspTrCtlPathDest':tnOamLspTrCtlPathDest,'tnOamLspTrCtlNhIntfName':tnOamLspTrCtlNhIntfName,'tnOamLspTrCtlNhAddressType':tnOamLspTrCtlNhAddressType,'tnOamLspTrCtlNhAddress':tnOamLspTrCtlNhAddress,'tnOamLspTrCtlDownstreamMapTlv':tnOamLspTrCtlDownstreamMapTlv,'tnOamLspTrCtlTestSubMode':tnOamLspTrCtlTestSubMode,'tnOamLspTrCtlMplsTpPathType':tnOamLspTrCtlMplsTpPathType,'tnOamLspTrCtlAssocChannel':tnOamLspTrCtlAssocChannel,'tnOamLspTrCtlForce':tnOamLspTrCtlForce,'tnOamLspTrMapTable':tnOamLspTrMapTable,'tnOamLspTrMapEntry':tnOamLspTrMapEntry,_AJ:tnOamLspTrMapIndex,'tnOamLspTrMapDSIPv4Addr':tnOamLspTrMapDSIPv4Addr,'tnOamLspTrMapAddrType':tnOamLspTrMapAddrType,'tnOamLspTrMapDSIfAddr':tnOamLspTrMapDSIfAddr,'tnOamLspTrMapMTU':tnOamLspTrMapMTU,'tnOamLspTrMapDSIndex':tnOamLspTrMapDSIndex,'tnOamVccvTrCtlTable':tnOamVccvTrCtlTable,'tnOamVccvTrCtlEntry':tnOamVccvTrCtlEntry,'tnOamVccvTrCtlSdpIdVcId':tnOamVccvTrCtlSdpIdVcId,'tnOamVccvTrCtlReplyMode':tnOamVccvTrCtlReplyMode,'tnOamVccvTrCtlSpokeSdpId':tnOamVccvTrCtlSpokeSdpId,'tnOamVccvTrCtlSaiiGlobalId':tnOamVccvTrCtlSaiiGlobalId,'tnOamVccvTrCtlSaiiPrefix':tnOamVccvTrCtlSaiiPrefix,'tnOamVccvTrCtlSaiiAcId':tnOamVccvTrCtlSaiiAcId,'tnOamVccvTrCtlTaiiGlobalId':tnOamVccvTrCtlTaiiGlobalId,'tnOamVccvTrCtlTaiiPrefix':tnOamVccvTrCtlTaiiPrefix,'tnOamVccvTrCtlTaiiAcId':tnOamVccvTrCtlTaiiAcId,'tnOamVccvTrCtlTestSubMode':tnOamVccvTrCtlTestSubMode,'tnOamVccvTrCtlAssocChannel':tnOamVccvTrCtlAssocChannel,'tnOamVccvTrNextPwSegmentTable':tnOamVccvTrNextPwSegmentTable,'tnOamVccvTrNextPwSegmentEntry':tnOamVccvTrNextPwSegmentEntry,'tnOamVccvTrNextPwID':tnOamVccvTrNextPwID,'tnOamVccvTrNextPwType':tnOamVccvTrNextPwType,'tnOamVccvTrNextSenderAddrType':tnOamVccvTrNextSenderAddrType,'tnOamVccvTrNextSenderAddr':tnOamVccvTrNextSenderAddr,'tnOamVccvTrNextRemoteAddrType':tnOamVccvTrNextRemoteAddrType,'tnOamVccvTrNextRemoteAddr':tnOamVccvTrNextRemoteAddr,'tnOamVccvTrNextSaiiGlobalId':tnOamVccvTrNextSaiiGlobalId,'tnOamVccvTrNextSaiiPrefix':tnOamVccvTrNextSaiiPrefix,'tnOamVccvTrNextSaiiAcId':tnOamVccvTrNextSaiiAcId,'tnOamVccvTrNextTaiiGlobalId':tnOamVccvTrNextTaiiGlobalId,'tnOamVccvTrNextTaiiPrefix':tnOamVccvTrNextTaiiPrefix,'tnOamVccvTrNextTaiiAcId':tnOamVccvTrNextTaiiAcId,'tnOamVccvTrNextTpAgi':tnOamVccvTrNextTpAgi,'tnOamVccvTrNextTpSaiiGlobalId':tnOamVccvTrNextTpSaiiGlobalId,'tnOamVccvTrNextTpSaiiNodeId':tnOamVccvTrNextTpSaiiNodeId,'tnOamVccvTrNextTpSaiiAcId':tnOamVccvTrNextTpSaiiAcId,'tnOamVccvTrNextTpTaiiGlobalId':tnOamVccvTrNextTpTaiiGlobalId,'tnOamVccvTrNextTpTaiiNodeId':tnOamVccvTrNextTpTaiiNodeId,'tnOamVccvTrNextTpTaiiAcId':tnOamVccvTrNextTpTaiiAcId,'tnOamSaaObjs':tnOamSaaObjs,'tnOamSaaCtlAttributeTotal':tnOamSaaCtlAttributeTotal,'tnOamSaaCtlTable':tnOamSaaCtlTable,'tnOamSaaCtlEntry':tnOamSaaCtlEntry,_AK:tnOamSaaCtlTestIndex,'tnOamSaaCtlRowStatus':tnOamSaaCtlRowStatus,'tnOamSaaCtlStorageType':tnOamSaaCtlStorageType,'tnOamSaaCtlLastChanged':tnOamSaaCtlLastChanged,'tnOamSaaCtlAdminStatus':tnOamSaaCtlAdminStatus,'tnOamSaaCtlDescr':tnOamSaaCtlDescr,'tnOamSaaCtlTestMode':tnOamSaaCtlTestMode,'tnOamSaaCtlRuns':tnOamSaaCtlRuns,'tnOamSaaCtlFailures':tnOamSaaCtlFailures,'tnOamSaaCtlLastRunResult':tnOamSaaCtlLastRunResult,'tnOamSaaCtlAcctPolicyId':tnOamSaaCtlAcctPolicyId,'tnOamSaaCtlSuppressAccounting':tnOamSaaCtlSuppressAccounting,'tnOamSaaCtlContinuous':tnOamSaaCtlContinuous,'tnOamSaaCtlKeepProbeHistoryAdm':tnOamSaaCtlKeepProbeHistoryAdm,'tnOamSaaCtlKeepProbeHistoryOpr':tnOamSaaCtlKeepProbeHistoryOpr,'tnOamSaaCtlAlmProfName':tnOamSaaCtlAlmProfName,'tnOamTestScalar1':tnOamTestScalar1,'tnOamTestScalar2':tnOamTestScalar2,'tnOamTestNotifications':tnOamTestNotifications,'tnOamPingNotifyPrefix':tnOamPingNotifyPrefix,'tnOamPingNotifications':tnOamPingNotifications,'tnOamTraceRouteNotifyPrefix':tnOamTraceRouteNotifyPrefix,'tnOamTraceRouteNotifications':tnOamTraceRouteNotifications,'tnOamSaaNotifyPrefix':tnOamSaaNotifyPrefix,'tnOamSaaNotifications':tnOamSaaNotifications})