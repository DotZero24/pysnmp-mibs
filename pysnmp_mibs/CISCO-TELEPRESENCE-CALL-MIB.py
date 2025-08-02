_BW='ctpcMgmtSysConnEventNotification'
_BV='ctpcMgmtSysConnFailNotification'
_BU='ctpcExtNumberMask'
_BT='ctpcRxCoSPrevious'
_BS='ctpcRxCoSCurrent'
_BR='ctpcRxDscpPrevious'
_BQ='ctpcRxDscpCurrent'
_BP='ctpcTxDscpAudioConfigured'
_BO='ctpcTxDscpTelepresenceConfigured'
_BN='ctpcRxMaxCallLostPacketsRecTime'
_BM='ctpcRxMaxCallLostPackets'
_BL='ctpcRxMaxPeriodLostPackets'
_BK='ctpcRxPeriodBitRate'
_BJ='ctpcRxCallBitRate'
_BI='ctpcTxPeriodBitRate'
_BH='ctpcTxCallBitRate'
_BG='ctpcTxVideoVertPixels'
_BF='ctpcTxVideoHorzPixels'
_BE='ctpcRxVideoVertPixels'
_BD='ctpcRxVideoHorzPixels'
_BC='ctpcMediaDestPort'
_BB='ctpcMediaSrcPort'
_BA='ctpcCallTermReason'
_B9='ctpcRxFrameRate'
_B8='ctpcRxCodec'
_B7='ctpcTxFrameRate'
_B6='ctpcTxCodec'
_B5='ctpcRemoteDevice'
_B4='ctpcAttributes'
_B3='ctpcMgmtSysConnEventTimeStamp'
_B2='ctpcMgmtSysConnEventSIPRespCode'
_B1='ctpcMgmtSysConnEventStatus'
_B0='ctpcMgmtSysConnEventHistLastIndex'
_A_='ctpcMgmtSysConnEventHistTableSize'
_Az='ctpcStatEventTimeStamp'
_Ay='ctpcStatEventHistLastIndex'
_Ax='ctpcStatEventHistTableSize'
_Aw='ctpcMaxCallJitterRecTime'
_Av='ctpcMaxCallJitter'
_Au='ctpcMaxPeriodJitter'
_At='ctpcAvgCallJitter'
_As='ctpcAvgPeriodJitter'
_Ar='ctpcRxCallAuthFailure'
_Aq='ctpcRxShapingWindow'
_Ap='ctpcRxIDRPackets'
_Ao='ctpcRxLatePackets'
_An='ctpcRxDuplicatePackets'
_Am='ctpcRxOutOfOrderPackets'
_Al='ctpcRxCallLostPackets'
_Ak='ctpcRxPeriodLostPackets'
_Aj='ctpcRxLostPackets'
_Ai='ctpcRxTotalPackets'
_Ah='ctpcRxTotalBytes'
_Ag='ctpcRxActive'
_Af='ctpcTxShapingWindow'
_Ae='ctpcTxIDRPackets'
_Ad='ctpcTxCallLostPackets'
_Ac='ctpcTxPeriodLostPackets'
_Ab='ctpcTxLostPackets'
_Aa='ctpcTxTotalPackets'
_AZ='ctpcTxTotalBytes'
_AY='ctpcTxActive'
_AX='ctpcMaxCallLatencyRecTime'
_AW='ctpcMaxCallLatency'
_AV='ctpcMaxPeriodLatency'
_AU='ctpcAvgCallLatency'
_AT='ctpcAvgPeriodLatency'
_AS='ctpcRowStatus'
_AR='ctpcLatestBitRate'
_AQ='ctpcInitialBitRate'
_AP='ctpcState'
_AO='ctpcDirection'
_AN='ctpcSecurity'
_AM='ctpcDuration'
_AL='ctpcStartDateAndTime'
_AK='ctpcTxDestAddr'
_AJ='ctpcTxDestAddrType'
_AI='ctpcLocalSIPCallId'
_AH='ctpcRemoteDirNum'
_AG='ctpcTableLastIndex'
_AF='ctpcTableSize'
_AE='ctpcSamplePeriod'
_AD='ctpcStatTotalCallTime'
_AC='ctpcStatTotalCalls'
_AB='ctpcStatOverallCallTime'
_AA='ctpcStatOverallCalls'
_A9='ctpcActiveMgmtSysIndex'
_A8='ctpcLocalAddr'
_A7='ctpcLocalAddrType'
_A6='ctpcLocalDirNum'
_A5='ctpcStatMonitoredStatus'
_A4='ctpcStatStartupAlarm'
_A3='ctpcStatFallingThreshold'
_A2='ctpcStatRisingThreshold'
_A1='ctpcStatMonitoredUnit'
_A0='ctpcMgmtSysConnNotifyEnable'
_z='ctpcStatNotifyEnable'
_y='ctpcMgmtSysConnEventHistoryIndex'
_x='ctpcStatEventHistoryIndex'
_w='millifps'
_v='ctpcStreamSource'
_u='CtpcStatAlarmMode'
_t='ctpcStatMonitoredStreamType'
_s='ctpcStatMonitoredType'
_r='ctpcMgmtSysIndex'
_q='ctpcLocalDirNumIndex'
_p='internalError'
_o='SnmpAdminString'
_n='ciscoTpCallInformationGroupSup2'
_m='ciscoTpCallNotificationGroupRev1'
_l='ctpcStatNotificaion'
_k='ctpcMgmtSysSIPRespCode'
_j='ctpcMgmtSysConnStatus'
_i='ctpcStatEventCrossedType'
_h='ctpcStatEventCrossedValue'
_g='ctpcStatEventMonObjectInst'
_f='ctpcStreamType'
_e='TruthValue'
_d='ciscoTpCallStatisticsGroupSup3'
_c='ctpcMgmtSysAddr'
_b='ctpcMgmtSysAddrType'
_a='Kbps'
_Z='pixels'
_Y='ctpcIndex'
_X='ciscoTpCallStatisticsGroupSup2'
_W='deprecated'
_V='ciscoTpCallMgmtSysConnEventHistGroup'
_U='ciscoTpCallStatisticsGroupSup1'
_T='ciscoTpCallInformationGroupSup1'
_S='read-write'
_R='other'
_Q='ciscoTpCallEventHistoryGroup'
_P='ciscoTpCallConfigurationGroup'
_O='ciscoTpCallStatisticsGroup'
_N='ciscoTpCallInformationGroup'
_M='seconds'
_L='micropercent'
_K='Integer32'
_J='unknown'
_I='not-accessible'
_H='read-create'
_G='packets'
_F='milliseconds'
_E='Unsigned32'
_D='Gauge32'
_C='read-only'
_B='current'
_A='CISCO-TELEPRESENCE-CALL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
QosLayer2Cos,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','QosLayer2Cos')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Unsigned64,=mibBuilder.importSymbols('CISCO-TC','Unsigned64')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_o)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_D,_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_e,'VariablePointer')
ciscoTelepresenceCallMIB=ModuleIdentity((1,3,6,1,4,1,9,9,644))
if mibBuilder.loadTexts:ciscoTelepresenceCallMIB.setRevisions(('2014-07-24 00:00','2012-11-08 00:00','2012-04-20 00:00','2012-01-11 00:00','2011-05-16 00:00','2011-02-04 00:00','2011-01-31 00:00','2009-10-21 00:00','2008-09-17 00:00','2008-01-23 00:00','2007-12-28 00:00'))
class CtpcE164Address(TextualConvention,OctetString):status=_B;displayHint='32t';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class CtpcStreamMediaType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('video',1),('audio',2),('content',3)))
class CtpcStreamSourceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('secCodec1',1),('priCodec',2),('secCodec2',3),('auxiliary1',4),('secLegacy1',5),('priLegacy',6),('secLegacy2',7),('auxiliary2',8),('center',9),('left',10),('right',11),('legacyCtr',12),('legacyLeft',13),('legacyRight',14),('auxiliary3',15),('auxiliary4',16),(_R,17)))
class CtpcStateCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_J,1),(_R,2),('noMgmtSysConn',3),('noDialTone',4),('invalidNumber',5),('ringing',6),('noAnswer',7),('inProgress',8),('remoteHold',9),('shareLineActive',10),('inLocalConference',11),('terminatedbyError',12),('localHold',13),('terminatedNormally',14),('answer',15),('resume',16),('busy',17),('pause',18),('playback',19),('recording',20)))
class CtpcStatMonitoredAttribute(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('latency',1),('jitter',2),('packetLoss',3),('authFailurePacket',4)))
class CtpcStatMonitoredAttributeUnit(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_L,2),(_G,3)))
class CtpcStatAlarmMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
class CtpcStatThreshCrossedType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('risingThreshold',1),('fallingThreshold',2)))
class CtpcAttributes(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('interop',0),('highDefinitionInterop',1),('webEx',2),('schedule',3),('satellite',4),('t1',5),('liveDesk',6)))
class CtpcRemoteDeviceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_J,1),(_R,2),('audioDevice',3),('videoLegacyDevice',4),('highDefinitionLegacyDevice',5),('singleTelepresence',6),('tripleTelepresence',7),('telepresenceMultipointSwitch',8),('telepresenceRecordingServer',9),('telepresenceTranscodingDevice',10)))
class CtpcCodecType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_J,1),(_R,2),('aaclc',3),('aacld',4),('g711A',5),('g711U',6),('g722',7),('g7221',8),('g728',9),('g729',10),('h263',11),('h264',12),('aacldLatm',13),('h265',14)))
class CtpcMgmtSysConnStatusCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_R,2),(_p,3),('notRegister',4),('registered',5),('registraionFailure',6)))
class CtpcCallTerminationCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_J,1),(_R,2),(_p,3),('localDisconnected',4),('remoteDisconnected',5),('networkCongestion',6),('mediaNegotiationFailure',7),('securityConfigMismatched',8),('incompatibleRemoteEndPt',9),('serviceUnavailable',10),('remoteTerminatedWithError',11),('incall',12)))
_CiscoTelepresenceCallMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoTelepresenceCallMIBNotifs=_CiscoTelepresenceCallMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,644,0))
_CiscoTelepresenceCallMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTelepresenceCallMIBObjects=_CiscoTelepresenceCallMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,644,1))
_CtpcObjects_ObjectIdentity=ObjectIdentity
ctpcObjects=_CtpcObjects_ObjectIdentity((1,3,6,1,4,1,9,9,644,1,1))
class _CtpcStatNotifyEnable_Type(TruthValue):defaultValue=2
_CtpcStatNotifyEnable_Type.__name__=_e
_CtpcStatNotifyEnable_Object=MibScalar
ctpcStatNotifyEnable=_CtpcStatNotifyEnable_Object((1,3,6,1,4,1,9,9,644,1,1,1),_CtpcStatNotifyEnable_Type())
ctpcStatNotifyEnable.setMaxAccess(_S)
if mibBuilder.loadTexts:ctpcStatNotifyEnable.setStatus(_B)
class _CtpcMgmtSysConnNotifyEnable_Type(TruthValue):defaultValue=2
_CtpcMgmtSysConnNotifyEnable_Type.__name__=_e
_CtpcMgmtSysConnNotifyEnable_Object=MibScalar
ctpcMgmtSysConnNotifyEnable=_CtpcMgmtSysConnNotifyEnable_Object((1,3,6,1,4,1,9,9,644,1,1,2),_CtpcMgmtSysConnNotifyEnable_Type())
ctpcMgmtSysConnNotifyEnable.setMaxAccess(_S)
if mibBuilder.loadTexts:ctpcMgmtSysConnNotifyEnable.setStatus(_B)
_CtpcInfoObjects_ObjectIdentity=ObjectIdentity
ctpcInfoObjects=_CtpcInfoObjects_ObjectIdentity((1,3,6,1,4,1,9,9,644,1,2))
_CtpcLocalAddrType_Type=InetAddressType
_CtpcLocalAddrType_Object=MibScalar
ctpcLocalAddrType=_CtpcLocalAddrType_Object((1,3,6,1,4,1,9,9,644,1,2,1),_CtpcLocalAddrType_Type())
ctpcLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcLocalAddrType.setStatus(_B)
_CtpcLocalAddr_Type=InetAddress
_CtpcLocalAddr_Object=MibScalar
ctpcLocalAddr=_CtpcLocalAddr_Object((1,3,6,1,4,1,9,9,644,1,2,2),_CtpcLocalAddr_Type())
ctpcLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcLocalAddr.setStatus(_B)
_CtpcLocalDirNumTable_Object=MibTable
ctpcLocalDirNumTable=_CtpcLocalDirNumTable_Object((1,3,6,1,4,1,9,9,644,1,2,3))
if mibBuilder.loadTexts:ctpcLocalDirNumTable.setStatus(_B)
_CtpcLocalDirNumEntry_Object=MibTableRow
ctpcLocalDirNumEntry=_CtpcLocalDirNumEntry_Object((1,3,6,1,4,1,9,9,644,1,2,3,1))
ctpcLocalDirNumEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:ctpcLocalDirNumEntry.setStatus(_B)
_CtpcLocalDirNumIndex_Type=Unsigned32
_CtpcLocalDirNumIndex_Object=MibTableColumn
ctpcLocalDirNumIndex=_CtpcLocalDirNumIndex_Object((1,3,6,1,4,1,9,9,644,1,2,3,1,1),_CtpcLocalDirNumIndex_Type())
ctpcLocalDirNumIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcLocalDirNumIndex.setStatus(_B)
_CtpcLocalDirNum_Type=CtpcE164Address
_CtpcLocalDirNum_Object=MibTableColumn
ctpcLocalDirNum=_CtpcLocalDirNum_Object((1,3,6,1,4,1,9,9,644,1,2,3,1,2),_CtpcLocalDirNum_Type())
ctpcLocalDirNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcLocalDirNum.setStatus(_B)
_CtpcExtNumberMask_Type=SnmpAdminString
_CtpcExtNumberMask_Object=MibTableColumn
ctpcExtNumberMask=_CtpcExtNumberMask_Object((1,3,6,1,4,1,9,9,644,1,2,3,1,3),_CtpcExtNumberMask_Type())
ctpcExtNumberMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcExtNumberMask.setStatus(_B)
class _CtpcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noMgmtSys',1),('mgmtSys',2)))
_CtpcMode_Type.__name__=_K
_CtpcMode_Object=MibScalar
ctpcMode=_CtpcMode_Object((1,3,6,1,4,1,9,9,644,1,2,4),_CtpcMode_Type())
ctpcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMode.setStatus(_B)
_CtpcActiveMgmtSysIndex_Type=Unsigned32
_CtpcActiveMgmtSysIndex_Object=MibScalar
ctpcActiveMgmtSysIndex=_CtpcActiveMgmtSysIndex_Object((1,3,6,1,4,1,9,9,644,1,2,5),_CtpcActiveMgmtSysIndex_Type())
ctpcActiveMgmtSysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcActiveMgmtSysIndex.setStatus(_B)
_CtpcMgmtSysTable_Object=MibTable
ctpcMgmtSysTable=_CtpcMgmtSysTable_Object((1,3,6,1,4,1,9,9,644,1,2,6))
if mibBuilder.loadTexts:ctpcMgmtSysTable.setStatus(_B)
_CtpcMgmtSysEntry_Object=MibTableRow
ctpcMgmtSysEntry=_CtpcMgmtSysEntry_Object((1,3,6,1,4,1,9,9,644,1,2,6,1))
ctpcMgmtSysEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:ctpcMgmtSysEntry.setStatus(_B)
class _CtpcMgmtSysIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CtpcMgmtSysIndex_Type.__name__=_E
_CtpcMgmtSysIndex_Object=MibTableColumn
ctpcMgmtSysIndex=_CtpcMgmtSysIndex_Object((1,3,6,1,4,1,9,9,644,1,2,6,1,1),_CtpcMgmtSysIndex_Type())
ctpcMgmtSysIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcMgmtSysIndex.setStatus(_B)
_CtpcMgmtSysAddrType_Type=InetAddressType
_CtpcMgmtSysAddrType_Object=MibTableColumn
ctpcMgmtSysAddrType=_CtpcMgmtSysAddrType_Object((1,3,6,1,4,1,9,9,644,1,2,6,1,2),_CtpcMgmtSysAddrType_Type())
ctpcMgmtSysAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMgmtSysAddrType.setStatus(_B)
_CtpcMgmtSysAddr_Type=InetAddress
_CtpcMgmtSysAddr_Object=MibTableColumn
ctpcMgmtSysAddr=_CtpcMgmtSysAddr_Object((1,3,6,1,4,1,9,9,644,1,2,6,1,3),_CtpcMgmtSysAddr_Type())
ctpcMgmtSysAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMgmtSysAddr.setStatus(_B)
_CtpcMgmtSysConnStatus_Type=CtpcMgmtSysConnStatusCode
_CtpcMgmtSysConnStatus_Object=MibTableColumn
ctpcMgmtSysConnStatus=_CtpcMgmtSysConnStatus_Object((1,3,6,1,4,1,9,9,644,1,2,6,1,4),_CtpcMgmtSysConnStatus_Type())
ctpcMgmtSysConnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMgmtSysConnStatus.setStatus(_B)
_CtpcMgmtSysSIPRespCode_Type=Unsigned32
_CtpcMgmtSysSIPRespCode_Object=MibTableColumn
ctpcMgmtSysSIPRespCode=_CtpcMgmtSysSIPRespCode_Object((1,3,6,1,4,1,9,9,644,1,2,6,1,5),_CtpcMgmtSysSIPRespCode_Type())
ctpcMgmtSysSIPRespCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMgmtSysSIPRespCode.setStatus(_B)
_CtpcTxDscpTelepresenceConfigured_Type=Dscp
_CtpcTxDscpTelepresenceConfigured_Object=MibScalar
ctpcTxDscpTelepresenceConfigured=_CtpcTxDscpTelepresenceConfigured_Object((1,3,6,1,4,1,9,9,644,1,2,7),_CtpcTxDscpTelepresenceConfigured_Type())
ctpcTxDscpTelepresenceConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxDscpTelepresenceConfigured.setStatus(_B)
_CtpcTxDscpAudioConfigured_Type=Dscp
_CtpcTxDscpAudioConfigured_Object=MibScalar
ctpcTxDscpAudioConfigured=_CtpcTxDscpAudioConfigured_Object((1,3,6,1,4,1,9,9,644,1,2,8),_CtpcTxDscpAudioConfigured_Type())
ctpcTxDscpAudioConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxDscpAudioConfigured.setStatus(_B)
_CtpcStatMonitorObjects_ObjectIdentity=ObjectIdentity
ctpcStatMonitorObjects=_CtpcStatMonitorObjects_ObjectIdentity((1,3,6,1,4,1,9,9,644,1,3))
_CtpcStatMonitoredTable_Object=MibTable
ctpcStatMonitoredTable=_CtpcStatMonitoredTable_Object((1,3,6,1,4,1,9,9,644,1,3,1))
if mibBuilder.loadTexts:ctpcStatMonitoredTable.setStatus(_B)
_CtpcStatMonitoredEntry_Object=MibTableRow
ctpcStatMonitoredEntry=_CtpcStatMonitoredEntry_Object((1,3,6,1,4,1,9,9,644,1,3,1,1))
ctpcStatMonitoredEntry.setIndexNames((0,_A,_s),(0,_A,_t))
if mibBuilder.loadTexts:ctpcStatMonitoredEntry.setStatus(_B)
_CtpcStatMonitoredType_Type=CtpcStatMonitoredAttribute
_CtpcStatMonitoredType_Object=MibTableColumn
ctpcStatMonitoredType=_CtpcStatMonitoredType_Object((1,3,6,1,4,1,9,9,644,1,3,1,1,1),_CtpcStatMonitoredType_Type())
ctpcStatMonitoredType.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcStatMonitoredType.setStatus(_B)
class _CtpcStatMonitoredStreamType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('all',0),('video',1),('audio',2)))
_CtpcStatMonitoredStreamType_Type.__name__=_K
_CtpcStatMonitoredStreamType_Object=MibTableColumn
ctpcStatMonitoredStreamType=_CtpcStatMonitoredStreamType_Object((1,3,6,1,4,1,9,9,644,1,3,1,1,2),_CtpcStatMonitoredStreamType_Type())
ctpcStatMonitoredStreamType.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcStatMonitoredStreamType.setStatus(_B)
_CtpcStatMonitoredUnit_Type=CtpcStatMonitoredAttributeUnit
_CtpcStatMonitoredUnit_Object=MibTableColumn
ctpcStatMonitoredUnit=_CtpcStatMonitoredUnit_Object((1,3,6,1,4,1,9,9,644,1,3,1,1,3),_CtpcStatMonitoredUnit_Type())
ctpcStatMonitoredUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatMonitoredUnit.setStatus(_B)
_CtpcStatRisingThreshold_Type=Unsigned32
_CtpcStatRisingThreshold_Object=MibTableColumn
ctpcStatRisingThreshold=_CtpcStatRisingThreshold_Object((1,3,6,1,4,1,9,9,644,1,3,1,1,4),_CtpcStatRisingThreshold_Type())
ctpcStatRisingThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcStatRisingThreshold.setStatus(_B)
_CtpcStatFallingThreshold_Type=Unsigned32
_CtpcStatFallingThreshold_Object=MibTableColumn
ctpcStatFallingThreshold=_CtpcStatFallingThreshold_Object((1,3,6,1,4,1,9,9,644,1,3,1,1,5),_CtpcStatFallingThreshold_Type())
ctpcStatFallingThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcStatFallingThreshold.setStatus(_B)
class _CtpcStatStartupAlarm_Type(CtpcStatAlarmMode):defaultValue=3
_CtpcStatStartupAlarm_Type.__name__=_u
_CtpcStatStartupAlarm_Object=MibTableColumn
ctpcStatStartupAlarm=_CtpcStatStartupAlarm_Object((1,3,6,1,4,1,9,9,644,1,3,1,1,6),_CtpcStatStartupAlarm_Type())
ctpcStatStartupAlarm.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcStatStartupAlarm.setStatus(_B)
_CtpcStatMonitoredStatus_Type=RowStatus
_CtpcStatMonitoredStatus_Object=MibTableColumn
ctpcStatMonitoredStatus=_CtpcStatMonitoredStatus_Object((1,3,6,1,4,1,9,9,644,1,3,1,1,7),_CtpcStatMonitoredStatus_Type())
ctpcStatMonitoredStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcStatMonitoredStatus.setStatus(_B)
_CtpcStatObjects_ObjectIdentity=ObjectIdentity
ctpcStatObjects=_CtpcStatObjects_ObjectIdentity((1,3,6,1,4,1,9,9,644,1,4))
_CtpcStatOverallCalls_Type=Unsigned32
_CtpcStatOverallCalls_Object=MibScalar
ctpcStatOverallCalls=_CtpcStatOverallCalls_Object((1,3,6,1,4,1,9,9,644,1,4,1),_CtpcStatOverallCalls_Type())
ctpcStatOverallCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatOverallCalls.setStatus(_B)
_CtpcStatOverallCallTime_Type=Unsigned32
_CtpcStatOverallCallTime_Object=MibScalar
ctpcStatOverallCallTime=_CtpcStatOverallCallTime_Object((1,3,6,1,4,1,9,9,644,1,4,2),_CtpcStatOverallCallTime_Type())
ctpcStatOverallCallTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatOverallCallTime.setStatus(_B)
if mibBuilder.loadTexts:ctpcStatOverallCallTime.setUnits(_M)
_CtpcStatTotalCalls_Type=Unsigned32
_CtpcStatTotalCalls_Object=MibScalar
ctpcStatTotalCalls=_CtpcStatTotalCalls_Object((1,3,6,1,4,1,9,9,644,1,4,3),_CtpcStatTotalCalls_Type())
ctpcStatTotalCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatTotalCalls.setStatus(_B)
_CtpcStatTotalCallTime_Type=Unsigned32
_CtpcStatTotalCallTime_Object=MibScalar
ctpcStatTotalCallTime=_CtpcStatTotalCallTime_Object((1,3,6,1,4,1,9,9,644,1,4,4),_CtpcStatTotalCallTime_Type())
ctpcStatTotalCallTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatTotalCallTime.setStatus(_B)
if mibBuilder.loadTexts:ctpcStatTotalCallTime.setUnits(_M)
class _CtpcSamplePeriod_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_CtpcSamplePeriod_Type.__name__=_E
_CtpcSamplePeriod_Object=MibScalar
ctpcSamplePeriod=_CtpcSamplePeriod_Object((1,3,6,1,4,1,9,9,644,1,4,5),_CtpcSamplePeriod_Type())
ctpcSamplePeriod.setMaxAccess(_S)
if mibBuilder.loadTexts:ctpcSamplePeriod.setStatus(_B)
if mibBuilder.loadTexts:ctpcSamplePeriod.setUnits(_M)
class _CtpcTableSize_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,500))
_CtpcTableSize_Type.__name__=_K
_CtpcTableSize_Object=MibScalar
ctpcTableSize=_CtpcTableSize_Object((1,3,6,1,4,1,9,9,644,1,4,6),_CtpcTableSize_Type())
ctpcTableSize.setMaxAccess(_S)
if mibBuilder.loadTexts:ctpcTableSize.setStatus(_B)
class _CtpcTableLastIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CtpcTableLastIndex_Type.__name__=_E
_CtpcTableLastIndex_Object=MibScalar
ctpcTableLastIndex=_CtpcTableLastIndex_Object((1,3,6,1,4,1,9,9,644,1,4,7),_CtpcTableLastIndex_Type())
ctpcTableLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTableLastIndex.setStatus(_B)
_CtpcTable_Object=MibTable
ctpcTable=_CtpcTable_Object((1,3,6,1,4,1,9,9,644,1,4,8))
if mibBuilder.loadTexts:ctpcTable.setStatus(_B)
_CtpcEntry_Object=MibTableRow
ctpcEntry=_CtpcEntry_Object((1,3,6,1,4,1,9,9,644,1,4,8,1))
ctpcEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:ctpcEntry.setStatus(_B)
class _CtpcIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CtpcIndex_Type.__name__=_E
_CtpcIndex_Object=MibTableColumn
ctpcIndex=_CtpcIndex_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,1),_CtpcIndex_Type())
ctpcIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcIndex.setStatus(_B)
_CtpcRemoteDirNum_Type=CtpcE164Address
_CtpcRemoteDirNum_Object=MibTableColumn
ctpcRemoteDirNum=_CtpcRemoteDirNum_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,2),_CtpcRemoteDirNum_Type())
ctpcRemoteDirNum.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcRemoteDirNum.setStatus(_B)
class _CtpcLocalSIPCallId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtpcLocalSIPCallId_Type.__name__=_o
_CtpcLocalSIPCallId_Object=MibTableColumn
ctpcLocalSIPCallId=_CtpcLocalSIPCallId_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,3),_CtpcLocalSIPCallId_Type())
ctpcLocalSIPCallId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcLocalSIPCallId.setStatus(_B)
_CtpcTxDestAddrType_Type=InetAddressType
_CtpcTxDestAddrType_Object=MibTableColumn
ctpcTxDestAddrType=_CtpcTxDestAddrType_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,4),_CtpcTxDestAddrType_Type())
ctpcTxDestAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxDestAddrType.setStatus(_B)
_CtpcTxDestAddr_Type=InetAddress
_CtpcTxDestAddr_Object=MibTableColumn
ctpcTxDestAddr=_CtpcTxDestAddr_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,5),_CtpcTxDestAddr_Type())
ctpcTxDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxDestAddr.setStatus(_B)
_CtpcStartDateAndTime_Type=DateAndTime
_CtpcStartDateAndTime_Object=MibTableColumn
ctpcStartDateAndTime=_CtpcStartDateAndTime_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,6),_CtpcStartDateAndTime_Type())
ctpcStartDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStartDateAndTime.setStatus(_B)
_CtpcDuration_Type=Unsigned32
_CtpcDuration_Object=MibTableColumn
ctpcDuration=_CtpcDuration_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,7),_CtpcDuration_Type())
ctpcDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcDuration.setStatus(_B)
if mibBuilder.loadTexts:ctpcDuration.setUnits(_M)
class _CtpcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('audioVideo',1),('audioOnly',2),(_J,3)))
_CtpcType_Type.__name__=_K
_CtpcType_Object=MibTableColumn
ctpcType=_CtpcType_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,8),_CtpcType_Type())
ctpcType.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcType.setStatus(_B)
class _CtpcSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nonSecured',1),('authenticated',2),('secured',3),(_J,4)))
_CtpcSecurity_Type.__name__=_K
_CtpcSecurity_Object=MibTableColumn
ctpcSecurity=_CtpcSecurity_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,9),_CtpcSecurity_Type())
ctpcSecurity.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcSecurity.setStatus(_B)
class _CtpcDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('incoming',1),('outgoing',2),(_J,3)))
_CtpcDirection_Type.__name__=_K
_CtpcDirection_Object=MibTableColumn
ctpcDirection=_CtpcDirection_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,10),_CtpcDirection_Type())
ctpcDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcDirection.setStatus(_B)
_CtpcState_Type=CtpcStateCode
_CtpcState_Object=MibTableColumn
ctpcState=_CtpcState_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,11),_CtpcState_Type())
ctpcState.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcState.setStatus(_B)
_CtpcInitialBitRate_Type=Unsigned32
_CtpcInitialBitRate_Object=MibTableColumn
ctpcInitialBitRate=_CtpcInitialBitRate_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,12),_CtpcInitialBitRate_Type())
ctpcInitialBitRate.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcInitialBitRate.setStatus(_B)
if mibBuilder.loadTexts:ctpcInitialBitRate.setUnits('kbps')
_CtpcLatestBitRate_Type=Unsigned32
_CtpcLatestBitRate_Object=MibTableColumn
ctpcLatestBitRate=_CtpcLatestBitRate_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,13),_CtpcLatestBitRate_Type())
ctpcLatestBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcLatestBitRate.setStatus(_B)
if mibBuilder.loadTexts:ctpcLatestBitRate.setUnits('kbps')
_CtpcRowStatus_Type=RowStatus
_CtpcRowStatus_Object=MibTableColumn
ctpcRowStatus=_CtpcRowStatus_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,14),_CtpcRowStatus_Type())
ctpcRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ctpcRowStatus.setStatus(_B)
_CtpcAttributes_Type=CtpcAttributes
_CtpcAttributes_Object=MibTableColumn
ctpcAttributes=_CtpcAttributes_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,15),_CtpcAttributes_Type())
ctpcAttributes.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcAttributes.setStatus(_B)
_CtpcRemoteDevice_Type=CtpcRemoteDeviceType
_CtpcRemoteDevice_Object=MibTableColumn
ctpcRemoteDevice=_CtpcRemoteDevice_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,16),_CtpcRemoteDevice_Type())
ctpcRemoteDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRemoteDevice.setStatus(_B)
_CtpcCallTermReason_Type=CtpcCallTerminationCode
_CtpcCallTermReason_Object=MibTableColumn
ctpcCallTermReason=_CtpcCallTermReason_Object((1,3,6,1,4,1,9,9,644,1,4,8,1,17),_CtpcCallTermReason_Type())
ctpcCallTermReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcCallTermReason.setStatus(_B)
_CtpcStatStreamTypeTable_Object=MibTable
ctpcStatStreamTypeTable=_CtpcStatStreamTypeTable_Object((1,3,6,1,4,1,9,9,644,1,4,9))
if mibBuilder.loadTexts:ctpcStatStreamTypeTable.setStatus(_B)
_CtpcStatStreamTypeEntry_Object=MibTableRow
ctpcStatStreamTypeEntry=_CtpcStatStreamTypeEntry_Object((1,3,6,1,4,1,9,9,644,1,4,9,1))
ctpcStatStreamTypeEntry.setIndexNames((0,_A,_Y),(0,_A,_f))
if mibBuilder.loadTexts:ctpcStatStreamTypeEntry.setStatus(_B)
_CtpcStreamType_Type=CtpcStreamMediaType
_CtpcStreamType_Object=MibTableColumn
ctpcStreamType=_CtpcStreamType_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,1),_CtpcStreamType_Type())
ctpcStreamType.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcStreamType.setStatus(_B)
_CtpcAvgPeriodLatency_Type=Gauge32
_CtpcAvgPeriodLatency_Object=MibTableColumn
ctpcAvgPeriodLatency=_CtpcAvgPeriodLatency_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,2),_CtpcAvgPeriodLatency_Type())
ctpcAvgPeriodLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcAvgPeriodLatency.setStatus(_B)
if mibBuilder.loadTexts:ctpcAvgPeriodLatency.setUnits(_F)
_CtpcAvgCallLatency_Type=Gauge32
_CtpcAvgCallLatency_Object=MibTableColumn
ctpcAvgCallLatency=_CtpcAvgCallLatency_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,3),_CtpcAvgCallLatency_Type())
ctpcAvgCallLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcAvgCallLatency.setStatus(_B)
if mibBuilder.loadTexts:ctpcAvgCallLatency.setUnits(_F)
_CtpcMaxPeriodLatency_Type=Gauge32
_CtpcMaxPeriodLatency_Object=MibTableColumn
ctpcMaxPeriodLatency=_CtpcMaxPeriodLatency_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,4),_CtpcMaxPeriodLatency_Type())
ctpcMaxPeriodLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMaxPeriodLatency.setStatus(_B)
if mibBuilder.loadTexts:ctpcMaxPeriodLatency.setUnits(_F)
_CtpcMaxCallLatency_Type=Gauge32
_CtpcMaxCallLatency_Object=MibTableColumn
ctpcMaxCallLatency=_CtpcMaxCallLatency_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,5),_CtpcMaxCallLatency_Type())
ctpcMaxCallLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMaxCallLatency.setStatus(_B)
if mibBuilder.loadTexts:ctpcMaxCallLatency.setUnits(_F)
_CtpcMaxCallLatencyRecTime_Type=Unsigned32
_CtpcMaxCallLatencyRecTime_Object=MibTableColumn
ctpcMaxCallLatencyRecTime=_CtpcMaxCallLatencyRecTime_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,6),_CtpcMaxCallLatencyRecTime_Type())
ctpcMaxCallLatencyRecTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMaxCallLatencyRecTime.setStatus(_B)
if mibBuilder.loadTexts:ctpcMaxCallLatencyRecTime.setUnits(_M)
_CtpcMediaSrcPort_Type=Unsigned32
_CtpcMediaSrcPort_Object=MibTableColumn
ctpcMediaSrcPort=_CtpcMediaSrcPort_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,7),_CtpcMediaSrcPort_Type())
ctpcMediaSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMediaSrcPort.setStatus(_B)
_CtpcMediaDestPort_Type=Unsigned32
_CtpcMediaDestPort_Object=MibTableColumn
ctpcMediaDestPort=_CtpcMediaDestPort_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,8),_CtpcMediaDestPort_Type())
ctpcMediaDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMediaDestPort.setStatus(_B)
_CtpcRxDscpCurrent_Type=Dscp
_CtpcRxDscpCurrent_Object=MibTableColumn
ctpcRxDscpCurrent=_CtpcRxDscpCurrent_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,9),_CtpcRxDscpCurrent_Type())
ctpcRxDscpCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxDscpCurrent.setStatus(_B)
_CtpcRxDscpPrevious_Type=Dscp
_CtpcRxDscpPrevious_Object=MibTableColumn
ctpcRxDscpPrevious=_CtpcRxDscpPrevious_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,10),_CtpcRxDscpPrevious_Type())
ctpcRxDscpPrevious.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxDscpPrevious.setStatus(_B)
_CtpcRxCoSCurrent_Type=QosLayer2Cos
_CtpcRxCoSCurrent_Object=MibTableColumn
ctpcRxCoSCurrent=_CtpcRxCoSCurrent_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,11),_CtpcRxCoSCurrent_Type())
ctpcRxCoSCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxCoSCurrent.setStatus(_B)
_CtpcRxCoSPrevious_Type=QosLayer2Cos
_CtpcRxCoSPrevious_Object=MibTableColumn
ctpcRxCoSPrevious=_CtpcRxCoSPrevious_Object((1,3,6,1,4,1,9,9,644,1,4,9,1,12),_CtpcRxCoSPrevious_Type())
ctpcRxCoSPrevious.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxCoSPrevious.setStatus(_B)
_CtpcStatStreamSourceTable_Object=MibTable
ctpcStatStreamSourceTable=_CtpcStatStreamSourceTable_Object((1,3,6,1,4,1,9,9,644,1,4,10))
if mibBuilder.loadTexts:ctpcStatStreamSourceTable.setStatus(_B)
_CtpcStatStreamSourceEntry_Object=MibTableRow
ctpcStatStreamSourceEntry=_CtpcStatStreamSourceEntry_Object((1,3,6,1,4,1,9,9,644,1,4,10,1))
ctpcStatStreamSourceEntry.setIndexNames((0,_A,_Y),(0,_A,_f),(0,_A,_v))
if mibBuilder.loadTexts:ctpcStatStreamSourceEntry.setStatus(_B)
_CtpcStreamSource_Type=CtpcStreamSourceType
_CtpcStreamSource_Object=MibTableColumn
ctpcStreamSource=_CtpcStreamSource_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,1),_CtpcStreamSource_Type())
ctpcStreamSource.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcStreamSource.setStatus(_B)
_CtpcTxActive_Type=TruthValue
_CtpcTxActive_Object=MibTableColumn
ctpcTxActive=_CtpcTxActive_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,2),_CtpcTxActive_Type())
ctpcTxActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxActive.setStatus(_B)
_CtpcTxTotalBytes_Type=Counter64
_CtpcTxTotalBytes_Object=MibTableColumn
ctpcTxTotalBytes=_CtpcTxTotalBytes_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,3),_CtpcTxTotalBytes_Type())
ctpcTxTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxTotalBytes.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxTotalBytes.setUnits('bytes')
_CtpcTxTotalPackets_Type=Counter64
_CtpcTxTotalPackets_Object=MibTableColumn
ctpcTxTotalPackets=_CtpcTxTotalPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,4),_CtpcTxTotalPackets_Type())
ctpcTxTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxTotalPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxTotalPackets.setUnits(_G)
_CtpcTxLostPackets_Type=Counter64
_CtpcTxLostPackets_Object=MibTableColumn
ctpcTxLostPackets=_CtpcTxLostPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,5),_CtpcTxLostPackets_Type())
ctpcTxLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxLostPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxLostPackets.setUnits(_G)
class _CtpcTxPeriodLostPackets_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CtpcTxPeriodLostPackets_Type.__name__=_D
_CtpcTxPeriodLostPackets_Object=MibTableColumn
ctpcTxPeriodLostPackets=_CtpcTxPeriodLostPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,6),_CtpcTxPeriodLostPackets_Type())
ctpcTxPeriodLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxPeriodLostPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxPeriodLostPackets.setUnits(_L)
class _CtpcTxCallLostPackets_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CtpcTxCallLostPackets_Type.__name__=_D
_CtpcTxCallLostPackets_Object=MibTableColumn
ctpcTxCallLostPackets=_CtpcTxCallLostPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,7),_CtpcTxCallLostPackets_Type())
ctpcTxCallLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxCallLostPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxCallLostPackets.setUnits(_L)
_CtpcTxIDRPackets_Type=Counter64
_CtpcTxIDRPackets_Object=MibTableColumn
ctpcTxIDRPackets=_CtpcTxIDRPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,8),_CtpcTxIDRPackets_Type())
ctpcTxIDRPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxIDRPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxIDRPackets.setUnits(_G)
_CtpcTxShapingWindow_Type=Gauge32
_CtpcTxShapingWindow_Object=MibTableColumn
ctpcTxShapingWindow=_CtpcTxShapingWindow_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,9),_CtpcTxShapingWindow_Type())
ctpcTxShapingWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxShapingWindow.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxShapingWindow.setUnits(_F)
_CtpcRxActive_Type=TruthValue
_CtpcRxActive_Object=MibTableColumn
ctpcRxActive=_CtpcRxActive_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,10),_CtpcRxActive_Type())
ctpcRxActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxActive.setStatus(_B)
_CtpcRxTotalBytes_Type=Counter64
_CtpcRxTotalBytes_Object=MibTableColumn
ctpcRxTotalBytes=_CtpcRxTotalBytes_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,11),_CtpcRxTotalBytes_Type())
ctpcRxTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxTotalBytes.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxTotalBytes.setUnits('bytes')
_CtpcRxTotalPackets_Type=Counter64
_CtpcRxTotalPackets_Object=MibTableColumn
ctpcRxTotalPackets=_CtpcRxTotalPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,12),_CtpcRxTotalPackets_Type())
ctpcRxTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxTotalPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxTotalPackets.setUnits(_G)
_CtpcRxLostPackets_Type=Counter64
_CtpcRxLostPackets_Object=MibTableColumn
ctpcRxLostPackets=_CtpcRxLostPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,13),_CtpcRxLostPackets_Type())
ctpcRxLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxLostPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxLostPackets.setUnits(_G)
class _CtpcRxPeriodLostPackets_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CtpcRxPeriodLostPackets_Type.__name__=_D
_CtpcRxPeriodLostPackets_Object=MibTableColumn
ctpcRxPeriodLostPackets=_CtpcRxPeriodLostPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,14),_CtpcRxPeriodLostPackets_Type())
ctpcRxPeriodLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxPeriodLostPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxPeriodLostPackets.setUnits(_L)
class _CtpcRxCallLostPackets_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CtpcRxCallLostPackets_Type.__name__=_D
_CtpcRxCallLostPackets_Object=MibTableColumn
ctpcRxCallLostPackets=_CtpcRxCallLostPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,15),_CtpcRxCallLostPackets_Type())
ctpcRxCallLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxCallLostPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxCallLostPackets.setUnits(_L)
_CtpcRxOutOfOrderPackets_Type=Counter64
_CtpcRxOutOfOrderPackets_Object=MibTableColumn
ctpcRxOutOfOrderPackets=_CtpcRxOutOfOrderPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,16),_CtpcRxOutOfOrderPackets_Type())
ctpcRxOutOfOrderPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxOutOfOrderPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxOutOfOrderPackets.setUnits(_G)
_CtpcRxDuplicatePackets_Type=Counter64
_CtpcRxDuplicatePackets_Object=MibTableColumn
ctpcRxDuplicatePackets=_CtpcRxDuplicatePackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,17),_CtpcRxDuplicatePackets_Type())
ctpcRxDuplicatePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxDuplicatePackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxDuplicatePackets.setUnits(_G)
_CtpcRxLatePackets_Type=Counter64
_CtpcRxLatePackets_Object=MibTableColumn
ctpcRxLatePackets=_CtpcRxLatePackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,18),_CtpcRxLatePackets_Type())
ctpcRxLatePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxLatePackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxLatePackets.setUnits(_G)
_CtpcRxIDRPackets_Type=Counter64
_CtpcRxIDRPackets_Object=MibTableColumn
ctpcRxIDRPackets=_CtpcRxIDRPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,19),_CtpcRxIDRPackets_Type())
ctpcRxIDRPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxIDRPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxIDRPackets.setUnits(_G)
_CtpcRxShapingWindow_Type=Gauge32
_CtpcRxShapingWindow_Object=MibTableColumn
ctpcRxShapingWindow=_CtpcRxShapingWindow_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,20),_CtpcRxShapingWindow_Type())
ctpcRxShapingWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxShapingWindow.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxShapingWindow.setUnits(_F)
_CtpcRxCallAuthFailure_Type=Counter64
_CtpcRxCallAuthFailure_Object=MibTableColumn
ctpcRxCallAuthFailure=_CtpcRxCallAuthFailure_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,21),_CtpcRxCallAuthFailure_Type())
ctpcRxCallAuthFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxCallAuthFailure.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxCallAuthFailure.setUnits(_G)
_CtpcAvgPeriodJitter_Type=Unsigned64
_CtpcAvgPeriodJitter_Object=MibTableColumn
ctpcAvgPeriodJitter=_CtpcAvgPeriodJitter_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,22),_CtpcAvgPeriodJitter_Type())
ctpcAvgPeriodJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcAvgPeriodJitter.setStatus(_B)
if mibBuilder.loadTexts:ctpcAvgPeriodJitter.setUnits(_F)
_CtpcAvgCallJitter_Type=Unsigned64
_CtpcAvgCallJitter_Object=MibTableColumn
ctpcAvgCallJitter=_CtpcAvgCallJitter_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,23),_CtpcAvgCallJitter_Type())
ctpcAvgCallJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcAvgCallJitter.setStatus(_B)
if mibBuilder.loadTexts:ctpcAvgCallJitter.setUnits(_F)
_CtpcMaxPeriodJitter_Type=Unsigned64
_CtpcMaxPeriodJitter_Object=MibTableColumn
ctpcMaxPeriodJitter=_CtpcMaxPeriodJitter_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,24),_CtpcMaxPeriodJitter_Type())
ctpcMaxPeriodJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMaxPeriodJitter.setStatus(_B)
if mibBuilder.loadTexts:ctpcMaxPeriodJitter.setUnits(_F)
_CtpcMaxCallJitter_Type=Unsigned64
_CtpcMaxCallJitter_Object=MibTableColumn
ctpcMaxCallJitter=_CtpcMaxCallJitter_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,25),_CtpcMaxCallJitter_Type())
ctpcMaxCallJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMaxCallJitter.setStatus(_B)
if mibBuilder.loadTexts:ctpcMaxCallJitter.setUnits(_F)
_CtpcMaxCallJitterRecTime_Type=Unsigned32
_CtpcMaxCallJitterRecTime_Object=MibTableColumn
ctpcMaxCallJitterRecTime=_CtpcMaxCallJitterRecTime_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,26),_CtpcMaxCallJitterRecTime_Type())
ctpcMaxCallJitterRecTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMaxCallJitterRecTime.setStatus(_B)
if mibBuilder.loadTexts:ctpcMaxCallJitterRecTime.setUnits(_M)
_CtpcTxCodec_Type=CtpcCodecType
_CtpcTxCodec_Object=MibTableColumn
ctpcTxCodec=_CtpcTxCodec_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,27),_CtpcTxCodec_Type())
ctpcTxCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxCodec.setStatus(_B)
_CtpcTxFrameRate_Type=Unsigned32
_CtpcTxFrameRate_Object=MibTableColumn
ctpcTxFrameRate=_CtpcTxFrameRate_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,28),_CtpcTxFrameRate_Type())
ctpcTxFrameRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxFrameRate.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxFrameRate.setUnits(_w)
_CtpcRxCodec_Type=CtpcCodecType
_CtpcRxCodec_Object=MibTableColumn
ctpcRxCodec=_CtpcRxCodec_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,29),_CtpcRxCodec_Type())
ctpcRxCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxCodec.setStatus(_B)
_CtpcRxFrameRate_Type=Unsigned32
_CtpcRxFrameRate_Object=MibTableColumn
ctpcRxFrameRate=_CtpcRxFrameRate_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,30),_CtpcRxFrameRate_Type())
ctpcRxFrameRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxFrameRate.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxFrameRate.setUnits(_w)
class _CtpcTxVideoHorzPixels_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtpcTxVideoHorzPixels_Type.__name__=_D
_CtpcTxVideoHorzPixels_Object=MibTableColumn
ctpcTxVideoHorzPixels=_CtpcTxVideoHorzPixels_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,31),_CtpcTxVideoHorzPixels_Type())
ctpcTxVideoHorzPixels.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxVideoHorzPixels.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxVideoHorzPixels.setUnits(_Z)
class _CtpcTxVideoVertPixels_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtpcTxVideoVertPixels_Type.__name__=_D
_CtpcTxVideoVertPixels_Object=MibTableColumn
ctpcTxVideoVertPixels=_CtpcTxVideoVertPixels_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,32),_CtpcTxVideoVertPixels_Type())
ctpcTxVideoVertPixels.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxVideoVertPixels.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxVideoVertPixels.setUnits(_Z)
class _CtpcRxVideoHorzPixels_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtpcRxVideoHorzPixels_Type.__name__=_D
_CtpcRxVideoHorzPixels_Object=MibTableColumn
ctpcRxVideoHorzPixels=_CtpcRxVideoHorzPixels_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,33),_CtpcRxVideoHorzPixels_Type())
ctpcRxVideoHorzPixels.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxVideoHorzPixels.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxVideoHorzPixels.setUnits(_Z)
class _CtpcRxVideoVertPixels_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtpcRxVideoVertPixels_Type.__name__=_D
_CtpcRxVideoVertPixels_Object=MibTableColumn
ctpcRxVideoVertPixels=_CtpcRxVideoVertPixels_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,34),_CtpcRxVideoVertPixels_Type())
ctpcRxVideoVertPixels.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxVideoVertPixels.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxVideoVertPixels.setUnits(_Z)
_CtpcTxCallBitRate_Type=Gauge32
_CtpcTxCallBitRate_Object=MibTableColumn
ctpcTxCallBitRate=_CtpcTxCallBitRate_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,35),_CtpcTxCallBitRate_Type())
ctpcTxCallBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxCallBitRate.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxCallBitRate.setUnits(_a)
_CtpcTxPeriodBitRate_Type=Gauge32
_CtpcTxPeriodBitRate_Object=MibTableColumn
ctpcTxPeriodBitRate=_CtpcTxPeriodBitRate_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,36),_CtpcTxPeriodBitRate_Type())
ctpcTxPeriodBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTxPeriodBitRate.setStatus(_B)
if mibBuilder.loadTexts:ctpcTxPeriodBitRate.setUnits(_a)
_CtpcRxCallBitRate_Type=Gauge32
_CtpcRxCallBitRate_Object=MibTableColumn
ctpcRxCallBitRate=_CtpcRxCallBitRate_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,37),_CtpcRxCallBitRate_Type())
ctpcRxCallBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxCallBitRate.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxCallBitRate.setUnits(_a)
_CtpcRxPeriodBitRate_Type=Gauge32
_CtpcRxPeriodBitRate_Object=MibTableColumn
ctpcRxPeriodBitRate=_CtpcRxPeriodBitRate_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,38),_CtpcRxPeriodBitRate_Type())
ctpcRxPeriodBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxPeriodBitRate.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxPeriodBitRate.setUnits(_a)
class _CtpcRxMaxPeriodLostPackets_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CtpcRxMaxPeriodLostPackets_Type.__name__=_D
_CtpcRxMaxPeriodLostPackets_Object=MibTableColumn
ctpcRxMaxPeriodLostPackets=_CtpcRxMaxPeriodLostPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,39),_CtpcRxMaxPeriodLostPackets_Type())
ctpcRxMaxPeriodLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxMaxPeriodLostPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxMaxPeriodLostPackets.setUnits(_L)
class _CtpcRxMaxCallLostPackets_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CtpcRxMaxCallLostPackets_Type.__name__=_D
_CtpcRxMaxCallLostPackets_Object=MibTableColumn
ctpcRxMaxCallLostPackets=_CtpcRxMaxCallLostPackets_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,40),_CtpcRxMaxCallLostPackets_Type())
ctpcRxMaxCallLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxMaxCallLostPackets.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxMaxCallLostPackets.setUnits(_L)
_CtpcRxMaxCallLostPacketsRecTime_Type=Gauge32
_CtpcRxMaxCallLostPacketsRecTime_Object=MibTableColumn
ctpcRxMaxCallLostPacketsRecTime=_CtpcRxMaxCallLostPacketsRecTime_Object((1,3,6,1,4,1,9,9,644,1,4,10,1,41),_CtpcRxMaxCallLostPacketsRecTime_Type())
ctpcRxMaxCallLostPacketsRecTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcRxMaxCallLostPacketsRecTime.setStatus(_B)
if mibBuilder.loadTexts:ctpcRxMaxCallLostPacketsRecTime.setUnits(_M)
_CtpcStatEventHistory_ObjectIdentity=ObjectIdentity
ctpcStatEventHistory=_CtpcStatEventHistory_ObjectIdentity((1,3,6,1,4,1,9,9,644,1,5))
class _CtpcStatEventHistTableSize_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CtpcStatEventHistTableSize_Type.__name__=_E
_CtpcStatEventHistTableSize_Object=MibScalar
ctpcStatEventHistTableSize=_CtpcStatEventHistTableSize_Object((1,3,6,1,4,1,9,9,644,1,5,1),_CtpcStatEventHistTableSize_Type())
ctpcStatEventHistTableSize.setMaxAccess(_S)
if mibBuilder.loadTexts:ctpcStatEventHistTableSize.setStatus(_B)
class _CtpcStatEventHistLastIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CtpcStatEventHistLastIndex_Type.__name__=_E
_CtpcStatEventHistLastIndex_Object=MibScalar
ctpcStatEventHistLastIndex=_CtpcStatEventHistLastIndex_Object((1,3,6,1,4,1,9,9,644,1,5,2),_CtpcStatEventHistLastIndex_Type())
ctpcStatEventHistLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatEventHistLastIndex.setStatus(_B)
_CtpcStatEventHistoryTable_Object=MibTable
ctpcStatEventHistoryTable=_CtpcStatEventHistoryTable_Object((1,3,6,1,4,1,9,9,644,1,5,3))
if mibBuilder.loadTexts:ctpcStatEventHistoryTable.setStatus(_B)
_CtpcStatEventHistoryEntry_Object=MibTableRow
ctpcStatEventHistoryEntry=_CtpcStatEventHistoryEntry_Object((1,3,6,1,4,1,9,9,644,1,5,3,1))
ctpcStatEventHistoryEntry.setIndexNames((0,_A,_x))
if mibBuilder.loadTexts:ctpcStatEventHistoryEntry.setStatus(_B)
class _CtpcStatEventHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CtpcStatEventHistoryIndex_Type.__name__=_E
_CtpcStatEventHistoryIndex_Object=MibTableColumn
ctpcStatEventHistoryIndex=_CtpcStatEventHistoryIndex_Object((1,3,6,1,4,1,9,9,644,1,5,3,1,1),_CtpcStatEventHistoryIndex_Type())
ctpcStatEventHistoryIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcStatEventHistoryIndex.setStatus(_B)
_CtpcStatEventMonObjectInst_Type=VariablePointer
_CtpcStatEventMonObjectInst_Object=MibTableColumn
ctpcStatEventMonObjectInst=_CtpcStatEventMonObjectInst_Object((1,3,6,1,4,1,9,9,644,1,5,3,1,2),_CtpcStatEventMonObjectInst_Type())
ctpcStatEventMonObjectInst.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatEventMonObjectInst.setStatus(_B)
_CtpcStatEventCrossedValue_Type=Unsigned64
_CtpcStatEventCrossedValue_Object=MibTableColumn
ctpcStatEventCrossedValue=_CtpcStatEventCrossedValue_Object((1,3,6,1,4,1,9,9,644,1,5,3,1,3),_CtpcStatEventCrossedValue_Type())
ctpcStatEventCrossedValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatEventCrossedValue.setStatus(_B)
_CtpcStatEventCrossedType_Type=CtpcStatThreshCrossedType
_CtpcStatEventCrossedType_Object=MibTableColumn
ctpcStatEventCrossedType=_CtpcStatEventCrossedType_Object((1,3,6,1,4,1,9,9,644,1,5,3,1,4),_CtpcStatEventCrossedType_Type())
ctpcStatEventCrossedType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatEventCrossedType.setStatus(_B)
_CtpcStatEventTimeStamp_Type=TimeTicks
_CtpcStatEventTimeStamp_Object=MibTableColumn
ctpcStatEventTimeStamp=_CtpcStatEventTimeStamp_Object((1,3,6,1,4,1,9,9,644,1,5,3,1,5),_CtpcStatEventTimeStamp_Type())
ctpcStatEventTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcStatEventTimeStamp.setStatus(_B)
_CtpcMgmtSysConnEventHistory_ObjectIdentity=ObjectIdentity
ctpcMgmtSysConnEventHistory=_CtpcMgmtSysConnEventHistory_ObjectIdentity((1,3,6,1,4,1,9,9,644,1,6))
class _CtpcMgmtSysConnEventHistTableSize_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CtpcMgmtSysConnEventHistTableSize_Type.__name__=_E
_CtpcMgmtSysConnEventHistTableSize_Object=MibScalar
ctpcMgmtSysConnEventHistTableSize=_CtpcMgmtSysConnEventHistTableSize_Object((1,3,6,1,4,1,9,9,644,1,6,1),_CtpcMgmtSysConnEventHistTableSize_Type())
ctpcMgmtSysConnEventHistTableSize.setMaxAccess(_S)
if mibBuilder.loadTexts:ctpcMgmtSysConnEventHistTableSize.setStatus(_B)
class _CtpcMgmtSysConnEventHistLastIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CtpcMgmtSysConnEventHistLastIndex_Type.__name__=_E
_CtpcMgmtSysConnEventHistLastIndex_Object=MibScalar
ctpcMgmtSysConnEventHistLastIndex=_CtpcMgmtSysConnEventHistLastIndex_Object((1,3,6,1,4,1,9,9,644,1,6,2),_CtpcMgmtSysConnEventHistLastIndex_Type())
ctpcMgmtSysConnEventHistLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMgmtSysConnEventHistLastIndex.setStatus(_B)
_CtpcMgmtSysConnEventHistoryTable_Object=MibTable
ctpcMgmtSysConnEventHistoryTable=_CtpcMgmtSysConnEventHistoryTable_Object((1,3,6,1,4,1,9,9,644,1,6,3))
if mibBuilder.loadTexts:ctpcMgmtSysConnEventHistoryTable.setStatus(_B)
_CtpcMgmtSysConnEventHistoryEntry_Object=MibTableRow
ctpcMgmtSysConnEventHistoryEntry=_CtpcMgmtSysConnEventHistoryEntry_Object((1,3,6,1,4,1,9,9,644,1,6,3,1))
ctpcMgmtSysConnEventHistoryEntry.setIndexNames((0,_A,_y))
if mibBuilder.loadTexts:ctpcMgmtSysConnEventHistoryEntry.setStatus(_B)
class _CtpcMgmtSysConnEventHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CtpcMgmtSysConnEventHistoryIndex_Type.__name__=_E
_CtpcMgmtSysConnEventHistoryIndex_Object=MibTableColumn
ctpcMgmtSysConnEventHistoryIndex=_CtpcMgmtSysConnEventHistoryIndex_Object((1,3,6,1,4,1,9,9,644,1,6,3,1,1),_CtpcMgmtSysConnEventHistoryIndex_Type())
ctpcMgmtSysConnEventHistoryIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ctpcMgmtSysConnEventHistoryIndex.setStatus(_B)
_CtpcMgmtSysConnEventStatus_Type=CtpcMgmtSysConnStatusCode
_CtpcMgmtSysConnEventStatus_Object=MibTableColumn
ctpcMgmtSysConnEventStatus=_CtpcMgmtSysConnEventStatus_Object((1,3,6,1,4,1,9,9,644,1,6,3,1,2),_CtpcMgmtSysConnEventStatus_Type())
ctpcMgmtSysConnEventStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMgmtSysConnEventStatus.setStatus(_B)
_CtpcMgmtSysConnEventSIPRespCode_Type=Unsigned32
_CtpcMgmtSysConnEventSIPRespCode_Object=MibTableColumn
ctpcMgmtSysConnEventSIPRespCode=_CtpcMgmtSysConnEventSIPRespCode_Object((1,3,6,1,4,1,9,9,644,1,6,3,1,3),_CtpcMgmtSysConnEventSIPRespCode_Type())
ctpcMgmtSysConnEventSIPRespCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMgmtSysConnEventSIPRespCode.setStatus(_B)
_CtpcMgmtSysConnEventTimeStamp_Type=TimeTicks
_CtpcMgmtSysConnEventTimeStamp_Object=MibTableColumn
ctpcMgmtSysConnEventTimeStamp=_CtpcMgmtSysConnEventTimeStamp_Object((1,3,6,1,4,1,9,9,644,1,6,3,1,4),_CtpcMgmtSysConnEventTimeStamp_Type())
ctpcMgmtSysConnEventTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcMgmtSysConnEventTimeStamp.setStatus(_B)
_CiscoTelepresenceCallMIBConform_ObjectIdentity=ObjectIdentity
ciscoTelepresenceCallMIBConform=_CiscoTelepresenceCallMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,644,2))
_CiscoTpCallMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTpCallMIBCompliances=_CiscoTpCallMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,644,2,1))
_CiscoTpCallMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTpCallMIBGroups=_CiscoTpCallMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,644,2,2))
ciscoTpCallConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,1))
ciscoTpCallConfigurationGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:ciscoTpCallConfigurationGroup.setStatus(_B)
ciscoTpCallInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,2))
ciscoTpCallInformationGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,'ctpcMode'),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ciscoTpCallInformationGroup.setStatus(_B)
ciscoTpCallStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,3))
ciscoTpCallStatisticsGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,'ctpcType'),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw)))
if mibBuilder.loadTexts:ciscoTpCallStatisticsGroup.setStatus(_B)
ciscoTpCallEventHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,4))
ciscoTpCallEventHistoryGroup.setObjects(*((_A,_Ax),(_A,_Ay),(_A,_g),(_A,_h),(_A,_i),(_A,_Az)))
if mibBuilder.loadTexts:ciscoTpCallEventHistoryGroup.setStatus(_B)
ciscoTpCallMgmtSysConnEventHistGroup=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,6))
ciscoTpCallMgmtSysConnEventHistGroup.setObjects(*((_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3)))
if mibBuilder.loadTexts:ciscoTpCallMgmtSysConnEventHistGroup.setStatus(_B)
ciscoTpCallInformationGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,7))
ciscoTpCallInformationGroupSup1.setObjects(*((_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ciscoTpCallInformationGroupSup1.setStatus(_B)
ciscoTpCallStatisticsGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,8))
ciscoTpCallStatisticsGroupSup1.setObjects(*((_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9)))
if mibBuilder.loadTexts:ciscoTpCallStatisticsGroupSup1.setStatus(_B)
ciscoTpCallStatisticsGroupSup2=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,10))
ciscoTpCallStatisticsGroupSup2.setObjects(*((_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG)))
if mibBuilder.loadTexts:ciscoTpCallStatisticsGroupSup2.setStatus(_B)
ciscoTpCallStatisticsGroupSup3=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,11))
ciscoTpCallStatisticsGroupSup3.setObjects(*((_A,_BH),(_A,_BI),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM),(_A,_BN),(_A,_BO),(_A,_BP),(_A,_BQ),(_A,_BR),(_A,_BS),(_A,_BT)))
if mibBuilder.loadTexts:ciscoTpCallStatisticsGroupSup3.setStatus(_B)
ciscoTpCallInformationGroupSup2=ObjectGroup((1,3,6,1,4,1,9,9,644,2,2,12))
ciscoTpCallInformationGroupSup2.setObjects((_A,_BU))
if mibBuilder.loadTexts:ciscoTpCallInformationGroupSup2.setStatus(_B)
ctpcMgmtSysConnFailNotification=NotificationType((1,3,6,1,4,1,9,9,644,0,1))
ctpcMgmtSysConnFailNotification.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ctpcMgmtSysConnFailNotification.setStatus(_W)
ctpcStatNotificaion=NotificationType((1,3,6,1,4,1,9,9,644,0,2))
ctpcStatNotificaion.setObjects(*((_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ctpcStatNotificaion.setStatus(_B)
ctpcMgmtSysConnEventNotification=NotificationType((1,3,6,1,4,1,9,9,644,0,3))
ctpcMgmtSysConnEventNotification.setObjects(*((_A,_b),(_A,_c),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ctpcMgmtSysConnEventNotification.setStatus(_B)
ciscoTpCallNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,644,2,2,5))
ciscoTpCallNotificationGroup.setObjects(*((_A,_BV),(_A,_l)))
if mibBuilder.loadTexts:ciscoTpCallNotificationGroup.setStatus('obsolete')
ciscoTpCallNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,644,2,2,9))
ciscoTpCallNotificationGroupRev1.setObjects(*((_A,_BW),(_A,_l)))
if mibBuilder.loadTexts:ciscoTpCallNotificationGroupRev1.setStatus(_B)
ciscoTpCallMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,644,2,1,1))
ciscoTpCallMIBCompliance.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoTpCallMIBCompliance.setStatus(_W)
ciscoTpCallMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,644,2,1,2))
ciscoTpCallMIBComplianceRev1.setObjects(*((_A,_N),(_A,_T),(_A,_O),(_A,_U),(_A,_P),(_A,_Q),(_A,_V)))
if mibBuilder.loadTexts:ciscoTpCallMIBComplianceRev1.setStatus(_W)
ciscoTpCallMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,644,2,1,3))
ciscoTpCallMIBComplianceRev2.setObjects(*((_A,_N),(_A,_T),(_A,_O),(_A,_U),(_A,_X),(_A,_P),(_A,_Q),(_A,_V),(_A,_m)))
if mibBuilder.loadTexts:ciscoTpCallMIBComplianceRev2.setStatus(_W)
ciscoTpCallMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,644,2,1,4))
ciscoTpCallMIBComplianceRev3.setObjects(*((_A,_N),(_A,_T),(_A,_O),(_A,_U),(_A,_X),(_A,_d),(_A,_P),(_A,_Q),(_A,_V)))
if mibBuilder.loadTexts:ciscoTpCallMIBComplianceRev3.setStatus(_W)
ciscoTpCallMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,644,2,1,5))
ciscoTpCallMIBComplianceRev4.setObjects(*((_A,_N),(_A,_T),(_A,_n),(_A,_O),(_A,_U),(_A,_X),(_A,_d),(_A,_P),(_A,_Q),(_A,_V)))
if mibBuilder.loadTexts:ciscoTpCallMIBComplianceRev4.setStatus(_B)
ciscoTpCallMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,9,644,2,1,6))
ciscoTpCallMIBComplianceRev5.setObjects(*((_A,_N),(_A,_T),(_A,_n),(_A,_O),(_A,_U),(_A,_X),(_A,_d),(_A,_m),(_A,_P),(_A,_Q),(_A,_V)))
if mibBuilder.loadTexts:ciscoTpCallMIBComplianceRev5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CtpcE164Address':CtpcE164Address,'CtpcStreamMediaType':CtpcStreamMediaType,'CtpcStreamSourceType':CtpcStreamSourceType,'CtpcStateCode':CtpcStateCode,'CtpcStatMonitoredAttribute':CtpcStatMonitoredAttribute,'CtpcStatMonitoredAttributeUnit':CtpcStatMonitoredAttributeUnit,_u:CtpcStatAlarmMode,'CtpcStatThreshCrossedType':CtpcStatThreshCrossedType,'CtpcAttributes':CtpcAttributes,'CtpcRemoteDeviceType':CtpcRemoteDeviceType,'CtpcCodecType':CtpcCodecType,'CtpcMgmtSysConnStatusCode':CtpcMgmtSysConnStatusCode,'CtpcCallTerminationCode':CtpcCallTerminationCode,'ciscoTelepresenceCallMIB':ciscoTelepresenceCallMIB,'ciscoTelepresenceCallMIBNotifs':ciscoTelepresenceCallMIBNotifs,_BV:ctpcMgmtSysConnFailNotification,_l:ctpcStatNotificaion,_BW:ctpcMgmtSysConnEventNotification,'ciscoTelepresenceCallMIBObjects':ciscoTelepresenceCallMIBObjects,'ctpcObjects':ctpcObjects,_z:ctpcStatNotifyEnable,_A0:ctpcMgmtSysConnNotifyEnable,'ctpcInfoObjects':ctpcInfoObjects,_A7:ctpcLocalAddrType,_A8:ctpcLocalAddr,'ctpcLocalDirNumTable':ctpcLocalDirNumTable,'ctpcLocalDirNumEntry':ctpcLocalDirNumEntry,_q:ctpcLocalDirNumIndex,_A6:ctpcLocalDirNum,_BU:ctpcExtNumberMask,'ctpcMode':ctpcMode,_A9:ctpcActiveMgmtSysIndex,'ctpcMgmtSysTable':ctpcMgmtSysTable,'ctpcMgmtSysEntry':ctpcMgmtSysEntry,_r:ctpcMgmtSysIndex,_b:ctpcMgmtSysAddrType,_c:ctpcMgmtSysAddr,_j:ctpcMgmtSysConnStatus,_k:ctpcMgmtSysSIPRespCode,_BO:ctpcTxDscpTelepresenceConfigured,_BP:ctpcTxDscpAudioConfigured,'ctpcStatMonitorObjects':ctpcStatMonitorObjects,'ctpcStatMonitoredTable':ctpcStatMonitoredTable,'ctpcStatMonitoredEntry':ctpcStatMonitoredEntry,_s:ctpcStatMonitoredType,_t:ctpcStatMonitoredStreamType,_A1:ctpcStatMonitoredUnit,_A2:ctpcStatRisingThreshold,_A3:ctpcStatFallingThreshold,_A4:ctpcStatStartupAlarm,_A5:ctpcStatMonitoredStatus,'ctpcStatObjects':ctpcStatObjects,_AA:ctpcStatOverallCalls,_AB:ctpcStatOverallCallTime,_AC:ctpcStatTotalCalls,_AD:ctpcStatTotalCallTime,_AE:ctpcSamplePeriod,_AF:ctpcTableSize,_AG:ctpcTableLastIndex,'ctpcTable':ctpcTable,'ctpcEntry':ctpcEntry,_Y:ctpcIndex,_AH:ctpcRemoteDirNum,_AI:ctpcLocalSIPCallId,_AJ:ctpcTxDestAddrType,_AK:ctpcTxDestAddr,_AL:ctpcStartDateAndTime,_AM:ctpcDuration,'ctpcType':ctpcType,_AN:ctpcSecurity,_AO:ctpcDirection,_AP:ctpcState,_AQ:ctpcInitialBitRate,_AR:ctpcLatestBitRate,_AS:ctpcRowStatus,_B4:ctpcAttributes,_B5:ctpcRemoteDevice,_BA:ctpcCallTermReason,'ctpcStatStreamTypeTable':ctpcStatStreamTypeTable,'ctpcStatStreamTypeEntry':ctpcStatStreamTypeEntry,_f:ctpcStreamType,_AT:ctpcAvgPeriodLatency,_AU:ctpcAvgCallLatency,_AV:ctpcMaxPeriodLatency,_AW:ctpcMaxCallLatency,_AX:ctpcMaxCallLatencyRecTime,_BB:ctpcMediaSrcPort,_BC:ctpcMediaDestPort,_BQ:ctpcRxDscpCurrent,_BR:ctpcRxDscpPrevious,_BS:ctpcRxCoSCurrent,_BT:ctpcRxCoSPrevious,'ctpcStatStreamSourceTable':ctpcStatStreamSourceTable,'ctpcStatStreamSourceEntry':ctpcStatStreamSourceEntry,_v:ctpcStreamSource,_AY:ctpcTxActive,_AZ:ctpcTxTotalBytes,_Aa:ctpcTxTotalPackets,_Ab:ctpcTxLostPackets,_Ac:ctpcTxPeriodLostPackets,_Ad:ctpcTxCallLostPackets,_Ae:ctpcTxIDRPackets,_Af:ctpcTxShapingWindow,_Ag:ctpcRxActive,_Ah:ctpcRxTotalBytes,_Ai:ctpcRxTotalPackets,_Aj:ctpcRxLostPackets,_Ak:ctpcRxPeriodLostPackets,_Al:ctpcRxCallLostPackets,_Am:ctpcRxOutOfOrderPackets,_An:ctpcRxDuplicatePackets,_Ao:ctpcRxLatePackets,_Ap:ctpcRxIDRPackets,_Aq:ctpcRxShapingWindow,_Ar:ctpcRxCallAuthFailure,_As:ctpcAvgPeriodJitter,_At:ctpcAvgCallJitter,_Au:ctpcMaxPeriodJitter,_Av:ctpcMaxCallJitter,_Aw:ctpcMaxCallJitterRecTime,_B6:ctpcTxCodec,_B7:ctpcTxFrameRate,_B8:ctpcRxCodec,_B9:ctpcRxFrameRate,_BF:ctpcTxVideoHorzPixels,_BG:ctpcTxVideoVertPixels,_BD:ctpcRxVideoHorzPixels,_BE:ctpcRxVideoVertPixels,_BH:ctpcTxCallBitRate,_BI:ctpcTxPeriodBitRate,_BJ:ctpcRxCallBitRate,_BK:ctpcRxPeriodBitRate,_BL:ctpcRxMaxPeriodLostPackets,_BM:ctpcRxMaxCallLostPackets,_BN:ctpcRxMaxCallLostPacketsRecTime,'ctpcStatEventHistory':ctpcStatEventHistory,_Ax:ctpcStatEventHistTableSize,_Ay:ctpcStatEventHistLastIndex,'ctpcStatEventHistoryTable':ctpcStatEventHistoryTable,'ctpcStatEventHistoryEntry':ctpcStatEventHistoryEntry,_x:ctpcStatEventHistoryIndex,_g:ctpcStatEventMonObjectInst,_h:ctpcStatEventCrossedValue,_i:ctpcStatEventCrossedType,_Az:ctpcStatEventTimeStamp,'ctpcMgmtSysConnEventHistory':ctpcMgmtSysConnEventHistory,_A_:ctpcMgmtSysConnEventHistTableSize,_B0:ctpcMgmtSysConnEventHistLastIndex,'ctpcMgmtSysConnEventHistoryTable':ctpcMgmtSysConnEventHistoryTable,'ctpcMgmtSysConnEventHistoryEntry':ctpcMgmtSysConnEventHistoryEntry,_y:ctpcMgmtSysConnEventHistoryIndex,_B1:ctpcMgmtSysConnEventStatus,_B2:ctpcMgmtSysConnEventSIPRespCode,_B3:ctpcMgmtSysConnEventTimeStamp,'ciscoTelepresenceCallMIBConform':ciscoTelepresenceCallMIBConform,'ciscoTpCallMIBCompliances':ciscoTpCallMIBCompliances,'ciscoTpCallMIBCompliance':ciscoTpCallMIBCompliance,'ciscoTpCallMIBComplianceRev1':ciscoTpCallMIBComplianceRev1,'ciscoTpCallMIBComplianceRev2':ciscoTpCallMIBComplianceRev2,'ciscoTpCallMIBComplianceRev3':ciscoTpCallMIBComplianceRev3,'ciscoTpCallMIBComplianceRev4':ciscoTpCallMIBComplianceRev4,'ciscoTpCallMIBComplianceRev5':ciscoTpCallMIBComplianceRev5,'ciscoTpCallMIBGroups':ciscoTpCallMIBGroups,_P:ciscoTpCallConfigurationGroup,_N:ciscoTpCallInformationGroup,_O:ciscoTpCallStatisticsGroup,_Q:ciscoTpCallEventHistoryGroup,'ciscoTpCallNotificationGroup':ciscoTpCallNotificationGroup,_V:ciscoTpCallMgmtSysConnEventHistGroup,_T:ciscoTpCallInformationGroupSup1,_U:ciscoTpCallStatisticsGroupSup1,_m:ciscoTpCallNotificationGroupRev1,_X:ciscoTpCallStatisticsGroupSup2,_d:ciscoTpCallStatisticsGroupSup3,_n:ciscoTpCallInformationGroupSup2})