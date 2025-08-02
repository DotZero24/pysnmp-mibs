_AW='cwdxHeSuCpeGroup'
_AV='cwdxQosQueueGroup'
_AU='cwdxQosCtrlGroup'
_AT='cwdxHeSuMaxCpeNumber'
_AS='cwdxHeSuChOverRowStatus'
_AR='cwdxHeSuChOverTrapOnCompletion'
_AQ='cwdxHeSuChOverTimeExpiration'
_AP='cwdxHeTotalSusOffline'
_AO='cwdxHeTotalSusRegistered'
_AN='cwdxHeSuDefaultMaxCpes'
_AM='cwdxHeSuOnOffTrapInterval'
_AL='cwdxHeSuOnOffTrapEnable'
_AK='cwdxIfHeSuStatusDynSidCount'
_AJ='cwdxIfHeSuStatusMaxOfflineTime'
_AI='cwdxIfHeSuStatusAvgOfflineTime'
_AH='cwdxIfHeSuStatusMinOfflineTime'
_AG='cwdxIfHeSuStatusMaxOnlineTime'
_AF='cwdxIfHeSuStatusAvgOnlineTime'
_AE='cwdxIfHeSuStatusMinOnlineTime'
_AD='cwdxIfHeSuStatusPercentOnline'
_AC='cwdxIfHeSuStatusOnlineTimes'
_AB='cwdxSuMappingStatusIndex'
_AA='cwdxCpeAccessGroup'
_A9='cwdxCpeIpAddress'
_A8='cwdxBWQueueDiscards'
_A7='cwdxBWQueueDepth'
_A6='cwdxBWQueueMaxDepth'
_A5='cwdxBWQueueType'
_A4='cwdxBWQueueNumServedBeforeYield'
_A3='cwdxBWQueueOrder'
_A2='cwdxQosIpTosRatelimitMaxDownRate'
_A1='cwdxQosProfTosOverwriteValue'
_A0='cwdxQosProfTosOverwriteMask'
_z='cwdxQosProfName'
_y='cwdxQosProfGrantSize'
_x='cwdxQosProfGrantInterval'
_w='cwdxQosMaxDownBWExcessPackets'
_v='cwdxQosMaxUpBWExcessRequests'
_u='cwdxIfHeServiceOutPackets'
_t='cwdxIfHeServiceOutOctets'
_s='cwdxQosIfRateLimitShpGranularity'
_r='cwdxQosIfRateLimitShpMaxDelay'
_q='cwdxQosIfRateLimitExpWgt'
_p='cwdxQosIfRateLimitAlgo'
_o='cwdxQosCtrlUpMaxVirtualBW'
_n='cwdxQosCtrlUpReservedBW'
_m='cwdxQosCtrlUpAdmissionRejects'
_l='cwdxQosCtrlUpMaxRsvdBWPercent'
_k='cwdxQosCtrlUpAdmissionCtrl'
_j='cwdxQosProfileExtEntry'
_i='cwdxHeMacExtEntry'
_h='cwdxHeSuStatusExtEntry'
_g='cwdxHeServiceExtEntry'
_f='cwdxQosIpTosRatelimitIndex'
_e='cwdxHeSuChOverSerialNumber'
_d='cwdxSuMappingMacAddress'
_c='cwdxCpeMacAddress'
_b='cwdxCpeStatusIndex'
_a='cwdxBWQueueNameCode'
_Z='bits/second'
_Y='TruthValue'
_X='DisplayString'
_W='cwdIfQosProfIndex'
_V='cwdIfHeSuStatusUpChanIfIndex'
_U='cwdIfHeSuStatusServiceId'
_T='cwdIfHeSuStatusMacAddress'
_S='cwdIfHeSuStatusIpAddress'
_R='cwdIfHeSuStatusIndex'
_Q='cwdIfHeSuStatusDownChanIfIndex'
_P='cwdxHeSuChOverState'
_O='cwdxHeSuChOverOpInitiatedTime'
_N='cwdxHeSuChOverUpChannelId'
_M='cwdxHeSuChOverDownFrequency'
_L='cwdxHeSuChOverMacAddress'
_K='cwdxHeSuStatusValue'
_J='ifIndex'
_I='IF-MIB'
_H='not-accessible'
_G='CISCO-WIRELESS-DOCS-IF-MIB'
_F='read-create'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-WIRELESS-DOCS-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cwdIfHeMacEntry,cwdIfHeServiceEntry,cwdIfHeSuStatusDownChanIfIndex,cwdIfHeSuStatusEntry,cwdIfHeSuStatusIndex,cwdIfHeSuStatusIpAddress,cwdIfHeSuStatusMacAddress,cwdIfHeSuStatusServiceId,cwdIfHeSuStatusUpChanIfIndex,cwdIfQosProfIndex,cwdIfQosProfileEntry=mibBuilder.importSymbols(_G,'cwdIfHeMacEntry','cwdIfHeServiceEntry',_Q,'cwdIfHeSuStatusEntry',_R,_S,_T,_U,_V,_W,'cwdIfQosProfileEntry')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_X,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp',_Y)
ciscoWirelessDocsExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,169))
if mibBuilder.loadTexts:ciscoWirelessDocsExtMIB.setRevisions(('2000-07-17 10:03',))
_CiscoWirelessDocsExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWirelessDocsExtMIBObjects=_CiscoWirelessDocsExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,169,1))
_CwdxQosCtrlObjects_ObjectIdentity=ObjectIdentity
cwdxQosCtrlObjects=_CwdxQosCtrlObjects_ObjectIdentity((1,3,6,1,4,1,9,9,169,1,1))
_CwdxQosCtrlUpTable_Object=MibTable
cwdxQosCtrlUpTable=_CwdxQosCtrlUpTable_Object((1,3,6,1,4,1,9,9,169,1,1,1))
if mibBuilder.loadTexts:cwdxQosCtrlUpTable.setStatus(_A)
_CwdxQosCtrlUpEntry_Object=MibTableRow
cwdxQosCtrlUpEntry=_CwdxQosCtrlUpEntry_Object((1,3,6,1,4,1,9,9,169,1,1,1,1))
cwdxQosCtrlUpEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cwdxQosCtrlUpEntry.setStatus(_A)
_CwdxQosCtrlUpAdmissionCtrl_Type=TruthValue
_CwdxQosCtrlUpAdmissionCtrl_Object=MibTableColumn
cwdxQosCtrlUpAdmissionCtrl=_CwdxQosCtrlUpAdmissionCtrl_Object((1,3,6,1,4,1,9,9,169,1,1,1,1,1),_CwdxQosCtrlUpAdmissionCtrl_Type())
cwdxQosCtrlUpAdmissionCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxQosCtrlUpAdmissionCtrl.setStatus(_A)
class _CwdxQosCtrlUpMaxRsvdBWPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_CwdxQosCtrlUpMaxRsvdBWPercent_Type.__name__=_C
_CwdxQosCtrlUpMaxRsvdBWPercent_Object=MibTableColumn
cwdxQosCtrlUpMaxRsvdBWPercent=_CwdxQosCtrlUpMaxRsvdBWPercent_Object((1,3,6,1,4,1,9,9,169,1,1,1,1,2),_CwdxQosCtrlUpMaxRsvdBWPercent_Type())
cwdxQosCtrlUpMaxRsvdBWPercent.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxQosCtrlUpMaxRsvdBWPercent.setStatus(_A)
if mibBuilder.loadTexts:cwdxQosCtrlUpMaxRsvdBWPercent.setUnits('percent')
_CwdxQosCtrlUpAdmissionRejects_Type=Counter32
_CwdxQosCtrlUpAdmissionRejects_Object=MibTableColumn
cwdxQosCtrlUpAdmissionRejects=_CwdxQosCtrlUpAdmissionRejects_Object((1,3,6,1,4,1,9,9,169,1,1,1,1,3),_CwdxQosCtrlUpAdmissionRejects_Type())
cwdxQosCtrlUpAdmissionRejects.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxQosCtrlUpAdmissionRejects.setStatus(_A)
class _CwdxQosCtrlUpReservedBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,102400000))
_CwdxQosCtrlUpReservedBW_Type.__name__=_C
_CwdxQosCtrlUpReservedBW_Object=MibTableColumn
cwdxQosCtrlUpReservedBW=_CwdxQosCtrlUpReservedBW_Object((1,3,6,1,4,1,9,9,169,1,1,1,1,4),_CwdxQosCtrlUpReservedBW_Type())
cwdxQosCtrlUpReservedBW.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxQosCtrlUpReservedBW.setStatus(_A)
if mibBuilder.loadTexts:cwdxQosCtrlUpReservedBW.setUnits(_Z)
class _CwdxQosCtrlUpMaxVirtualBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,102400000))
_CwdxQosCtrlUpMaxVirtualBW_Type.__name__=_C
_CwdxQosCtrlUpMaxVirtualBW_Object=MibTableColumn
cwdxQosCtrlUpMaxVirtualBW=_CwdxQosCtrlUpMaxVirtualBW_Object((1,3,6,1,4,1,9,9,169,1,1,1,1,5),_CwdxQosCtrlUpMaxVirtualBW_Type())
cwdxQosCtrlUpMaxVirtualBW.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxQosCtrlUpMaxVirtualBW.setStatus(_A)
if mibBuilder.loadTexts:cwdxQosCtrlUpMaxVirtualBW.setUnits(_Z)
_CwdxQosIfRateLimitTable_Object=MibTable
cwdxQosIfRateLimitTable=_CwdxQosIfRateLimitTable_Object((1,3,6,1,4,1,9,9,169,1,1,2))
if mibBuilder.loadTexts:cwdxQosIfRateLimitTable.setStatus(_A)
_CwdxQosIfRateLimitEntry_Object=MibTableRow
cwdxQosIfRateLimitEntry=_CwdxQosIfRateLimitEntry_Object((1,3,6,1,4,1,9,9,169,1,1,2,1))
cwdxQosIfRateLimitEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cwdxQosIfRateLimitEntry.setStatus(_A)
class _CwdxQosIfRateLimitAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noRateLimit',1),('oneSecBurst',2),('carLike',3),('wgtExPacketDiscard',4),('shaping',5)))
_CwdxQosIfRateLimitAlgo_Type.__name__=_C
_CwdxQosIfRateLimitAlgo_Object=MibTableColumn
cwdxQosIfRateLimitAlgo=_CwdxQosIfRateLimitAlgo_Object((1,3,6,1,4,1,9,9,169,1,1,2,1,1),_CwdxQosIfRateLimitAlgo_Type())
cwdxQosIfRateLimitAlgo.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxQosIfRateLimitAlgo.setStatus(_A)
class _CwdxQosIfRateLimitExpWgt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CwdxQosIfRateLimitExpWgt_Type.__name__=_C
_CwdxQosIfRateLimitExpWgt_Object=MibTableColumn
cwdxQosIfRateLimitExpWgt=_CwdxQosIfRateLimitExpWgt_Object((1,3,6,1,4,1,9,9,169,1,1,2,1,2),_CwdxQosIfRateLimitExpWgt_Type())
cwdxQosIfRateLimitExpWgt.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxQosIfRateLimitExpWgt.setStatus(_A)
class _CwdxQosIfRateLimitShpMaxDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('na',1),('msec128',2),('msec256',3),('msec512',4),('msec1024',5)))
_CwdxQosIfRateLimitShpMaxDelay_Type.__name__=_C
_CwdxQosIfRateLimitShpMaxDelay_Object=MibTableColumn
cwdxQosIfRateLimitShpMaxDelay=_CwdxQosIfRateLimitShpMaxDelay_Object((1,3,6,1,4,1,9,9,169,1,1,2,1,3),_CwdxQosIfRateLimitShpMaxDelay_Type())
cwdxQosIfRateLimitShpMaxDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxQosIfRateLimitShpMaxDelay.setStatus(_A)
class _CwdxQosIfRateLimitShpGranularity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('na',1),('msec1',2),('msec2',3),('msec4',4),('msec8',5),('msec16',6)))
_CwdxQosIfRateLimitShpGranularity_Type.__name__=_C
_CwdxQosIfRateLimitShpGranularity_Object=MibTableColumn
cwdxQosIfRateLimitShpGranularity=_CwdxQosIfRateLimitShpGranularity_Object((1,3,6,1,4,1,9,9,169,1,1,2,1,4),_CwdxQosIfRateLimitShpGranularity_Type())
cwdxQosIfRateLimitShpGranularity.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxQosIfRateLimitShpGranularity.setStatus(_A)
_CwdxHeServiceExtTable_Object=MibTable
cwdxHeServiceExtTable=_CwdxHeServiceExtTable_Object((1,3,6,1,4,1,9,9,169,1,1,3))
if mibBuilder.loadTexts:cwdxHeServiceExtTable.setStatus(_A)
_CwdxHeServiceExtEntry_Object=MibTableRow
cwdxHeServiceExtEntry=_CwdxHeServiceExtEntry_Object((1,3,6,1,4,1,9,9,169,1,1,3,1))
if mibBuilder.loadTexts:cwdxHeServiceExtEntry.setStatus(_A)
_CwdxIfHeServiceOutOctets_Type=Counter32
_CwdxIfHeServiceOutOctets_Object=MibTableColumn
cwdxIfHeServiceOutOctets=_CwdxIfHeServiceOutOctets_Object((1,3,6,1,4,1,9,9,169,1,1,3,1,1),_CwdxIfHeServiceOutOctets_Type())
cwdxIfHeServiceOutOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeServiceOutOctets.setStatus(_A)
_CwdxIfHeServiceOutPackets_Type=Counter32
_CwdxIfHeServiceOutPackets_Object=MibTableColumn
cwdxIfHeServiceOutPackets=_CwdxIfHeServiceOutPackets_Object((1,3,6,1,4,1,9,9,169,1,1,3,1,2),_CwdxIfHeServiceOutPackets_Type())
cwdxIfHeServiceOutPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeServiceOutPackets.setStatus(_A)
_CwdxQosMaxUpBWExcessRequests_Type=Counter32
_CwdxQosMaxUpBWExcessRequests_Object=MibTableColumn
cwdxQosMaxUpBWExcessRequests=_CwdxQosMaxUpBWExcessRequests_Object((1,3,6,1,4,1,9,9,169,1,1,3,1,3),_CwdxQosMaxUpBWExcessRequests_Type())
cwdxQosMaxUpBWExcessRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxQosMaxUpBWExcessRequests.setStatus(_A)
_CwdxQosMaxDownBWExcessPackets_Type=Counter32
_CwdxQosMaxDownBWExcessPackets_Object=MibTableColumn
cwdxQosMaxDownBWExcessPackets=_CwdxQosMaxDownBWExcessPackets_Object((1,3,6,1,4,1,9,9,169,1,1,3,1,4),_CwdxQosMaxDownBWExcessPackets_Type())
cwdxQosMaxDownBWExcessPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxQosMaxDownBWExcessPackets.setStatus(_A)
_CwdxQosQueueObjects_ObjectIdentity=ObjectIdentity
cwdxQosQueueObjects=_CwdxQosQueueObjects_ObjectIdentity((1,3,6,1,4,1,9,9,169,1,2))
_CwdxBWQueueTable_Object=MibTable
cwdxBWQueueTable=_CwdxBWQueueTable_Object((1,3,6,1,4,1,9,9,169,1,2,1))
if mibBuilder.loadTexts:cwdxBWQueueTable.setStatus(_A)
_CwdxBWQueueEntry_Object=MibTableRow
cwdxBWQueueEntry=_CwdxBWQueueEntry_Object((1,3,6,1,4,1,9,9,169,1,2,1,1))
cwdxBWQueueEntry.setIndexNames((0,_I,_J),(0,_B,_a))
if mibBuilder.loadTexts:cwdxBWQueueEntry.setStatus(_A)
class _CwdxBWQueueNameCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cirQ',1),('tbeQ',2)))
_CwdxBWQueueNameCode_Type.__name__=_C
_CwdxBWQueueNameCode_Object=MibTableColumn
cwdxBWQueueNameCode=_CwdxBWQueueNameCode_Object((1,3,6,1,4,1,9,9,169,1,2,1,1,1),_CwdxBWQueueNameCode_Type())
cwdxBWQueueNameCode.setMaxAccess(_H)
if mibBuilder.loadTexts:cwdxBWQueueNameCode.setStatus(_A)
class _CwdxBWQueueOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CwdxBWQueueOrder_Type.__name__=_C
_CwdxBWQueueOrder_Object=MibTableColumn
cwdxBWQueueOrder=_CwdxBWQueueOrder_Object((1,3,6,1,4,1,9,9,169,1,2,1,1,2),_CwdxBWQueueOrder_Type())
cwdxBWQueueOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxBWQueueOrder.setStatus(_A)
class _CwdxBWQueueNumServedBeforeYield_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_CwdxBWQueueNumServedBeforeYield_Type.__name__=_C
_CwdxBWQueueNumServedBeforeYield_Object=MibTableColumn
cwdxBWQueueNumServedBeforeYield=_CwdxBWQueueNumServedBeforeYield_Object((1,3,6,1,4,1,9,9,169,1,2,1,1,3),_CwdxBWQueueNumServedBeforeYield_Type())
cwdxBWQueueNumServedBeforeYield.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxBWQueueNumServedBeforeYield.setStatus(_A)
class _CwdxBWQueueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('other',2),('fifo',3),('priority',4)))
_CwdxBWQueueType_Type.__name__=_C
_CwdxBWQueueType_Object=MibTableColumn
cwdxBWQueueType=_CwdxBWQueueType_Object((1,3,6,1,4,1,9,9,169,1,2,1,1,4),_CwdxBWQueueType_Type())
cwdxBWQueueType.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxBWQueueType.setStatus(_A)
_CwdxBWQueueMaxDepth_Type=Integer32
_CwdxBWQueueMaxDepth_Object=MibTableColumn
cwdxBWQueueMaxDepth=_CwdxBWQueueMaxDepth_Object((1,3,6,1,4,1,9,9,169,1,2,1,1,5),_CwdxBWQueueMaxDepth_Type())
cwdxBWQueueMaxDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxBWQueueMaxDepth.setStatus(_A)
_CwdxBWQueueDepth_Type=Integer32
_CwdxBWQueueDepth_Object=MibTableColumn
cwdxBWQueueDepth=_CwdxBWQueueDepth_Object((1,3,6,1,4,1,9,9,169,1,2,1,1,6),_CwdxBWQueueDepth_Type())
cwdxBWQueueDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxBWQueueDepth.setStatus(_A)
_CwdxBWQueueDiscards_Type=Counter32
_CwdxBWQueueDiscards_Object=MibTableColumn
cwdxBWQueueDiscards=_CwdxBWQueueDiscards_Object((1,3,6,1,4,1,9,9,169,1,2,1,1,7),_CwdxBWQueueDiscards_Type())
cwdxBWQueueDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxBWQueueDiscards.setStatus(_A)
_CwdxHeSuCpeObjects_ObjectIdentity=ObjectIdentity
cwdxHeSuCpeObjects=_CwdxHeSuCpeObjects_ObjectIdentity((1,3,6,1,4,1,9,9,169,1,3))
_CwdxCpeTable_Object=MibTable
cwdxCpeTable=_CwdxCpeTable_Object((1,3,6,1,4,1,9,9,169,1,3,1))
if mibBuilder.loadTexts:cwdxCpeTable.setStatus(_A)
_CwdxCpeEntry_Object=MibTableRow
cwdxCpeEntry=_CwdxCpeEntry_Object((1,3,6,1,4,1,9,9,169,1,3,1,1))
cwdxCpeEntry.setIndexNames((0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:cwdxCpeEntry.setStatus(_A)
class _CwdxCpeStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwdxCpeStatusIndex_Type.__name__=_C
_CwdxCpeStatusIndex_Object=MibTableColumn
cwdxCpeStatusIndex=_CwdxCpeStatusIndex_Object((1,3,6,1,4,1,9,9,169,1,3,1,1,1),_CwdxCpeStatusIndex_Type())
cwdxCpeStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cwdxCpeStatusIndex.setStatus(_A)
_CwdxCpeMacAddress_Type=MacAddress
_CwdxCpeMacAddress_Object=MibTableColumn
cwdxCpeMacAddress=_CwdxCpeMacAddress_Object((1,3,6,1,4,1,9,9,169,1,3,1,1,2),_CwdxCpeMacAddress_Type())
cwdxCpeMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cwdxCpeMacAddress.setStatus(_A)
_CwdxCpeIpAddress_Type=IpAddress
_CwdxCpeIpAddress_Object=MibTableColumn
cwdxCpeIpAddress=_CwdxCpeIpAddress_Object((1,3,6,1,4,1,9,9,169,1,3,1,1,3),_CwdxCpeIpAddress_Type())
cwdxCpeIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxCpeIpAddress.setStatus(_A)
_CwdxCpeAccessGroup_Type=DisplayString
_CwdxCpeAccessGroup_Object=MibTableColumn
cwdxCpeAccessGroup=_CwdxCpeAccessGroup_Object((1,3,6,1,4,1,9,9,169,1,3,1,1,4),_CwdxCpeAccessGroup_Type())
cwdxCpeAccessGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxCpeAccessGroup.setStatus(_A)
_CwdxSuMappingTable_Object=MibTable
cwdxSuMappingTable=_CwdxSuMappingTable_Object((1,3,6,1,4,1,9,9,169,1,3,2))
if mibBuilder.loadTexts:cwdxSuMappingTable.setStatus(_A)
_CwdxSuMappingEntry_Object=MibTableRow
cwdxSuMappingEntry=_CwdxSuMappingEntry_Object((1,3,6,1,4,1,9,9,169,1,3,2,1))
cwdxSuMappingEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:cwdxSuMappingEntry.setStatus(_A)
class _CwdxSuMappingStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwdxSuMappingStatusIndex_Type.__name__=_C
_CwdxSuMappingStatusIndex_Object=MibTableColumn
cwdxSuMappingStatusIndex=_CwdxSuMappingStatusIndex_Object((1,3,6,1,4,1,9,9,169,1,3,2,1,1),_CwdxSuMappingStatusIndex_Type())
cwdxSuMappingStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxSuMappingStatusIndex.setStatus(_A)
_CwdxSuMappingMacAddress_Type=MacAddress
_CwdxSuMappingMacAddress_Object=MibTableColumn
cwdxSuMappingMacAddress=_CwdxSuMappingMacAddress_Object((1,3,6,1,4,1,9,9,169,1,3,2,1,2),_CwdxSuMappingMacAddress_Type())
cwdxSuMappingMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cwdxSuMappingMacAddress.setStatus(_A)
_CwdxHeSuStatusExtTable_Object=MibTable
cwdxHeSuStatusExtTable=_CwdxHeSuStatusExtTable_Object((1,3,6,1,4,1,9,9,169,1,3,3))
if mibBuilder.loadTexts:cwdxHeSuStatusExtTable.setStatus(_A)
_CwdxHeSuStatusExtEntry_Object=MibTableRow
cwdxHeSuStatusExtEntry=_CwdxHeSuStatusExtEntry_Object((1,3,6,1,4,1,9,9,169,1,3,3,1))
if mibBuilder.loadTexts:cwdxHeSuStatusExtEntry.setStatus(_A)
class _CwdxHeSuStatusValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('offline',1),('others',2),('initRangingRcvd',3),('initDhcpReqRcvd',4),('onlineNetAccessDisabled',5),('onlineKekAssigned',6),('onlineTekAssigned',7),('rejectBadMic',8),('rejectBadCos',9),('kekRejected',10),('tekRejected',11),('online',12),('initTftpPacketRcvd',13),('initTodRequestRcvd',14)))
_CwdxHeSuStatusValue_Type.__name__=_C
_CwdxHeSuStatusValue_Object=MibTableColumn
cwdxHeSuStatusValue=_CwdxHeSuStatusValue_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,1),_CwdxHeSuStatusValue_Type())
cwdxHeSuStatusValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxHeSuStatusValue.setStatus(_A)
_CwdxIfHeSuStatusOnlineTimes_Type=Counter32
_CwdxIfHeSuStatusOnlineTimes_Object=MibTableColumn
cwdxIfHeSuStatusOnlineTimes=_CwdxIfHeSuStatusOnlineTimes_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,2),_CwdxIfHeSuStatusOnlineTimes_Type())
cwdxIfHeSuStatusOnlineTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusOnlineTimes.setStatus(_A)
class _CwdxIfHeSuStatusPercentOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CwdxIfHeSuStatusPercentOnline_Type.__name__=_C
_CwdxIfHeSuStatusPercentOnline_Object=MibTableColumn
cwdxIfHeSuStatusPercentOnline=_CwdxIfHeSuStatusPercentOnline_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,3),_CwdxIfHeSuStatusPercentOnline_Type())
cwdxIfHeSuStatusPercentOnline.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusPercentOnline.setStatus(_A)
_CwdxIfHeSuStatusMinOnlineTime_Type=TimeInterval
_CwdxIfHeSuStatusMinOnlineTime_Object=MibTableColumn
cwdxIfHeSuStatusMinOnlineTime=_CwdxIfHeSuStatusMinOnlineTime_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,4),_CwdxIfHeSuStatusMinOnlineTime_Type())
cwdxIfHeSuStatusMinOnlineTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusMinOnlineTime.setStatus(_A)
_CwdxIfHeSuStatusAvgOnlineTime_Type=TimeInterval
_CwdxIfHeSuStatusAvgOnlineTime_Object=MibTableColumn
cwdxIfHeSuStatusAvgOnlineTime=_CwdxIfHeSuStatusAvgOnlineTime_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,5),_CwdxIfHeSuStatusAvgOnlineTime_Type())
cwdxIfHeSuStatusAvgOnlineTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusAvgOnlineTime.setStatus(_A)
_CwdxIfHeSuStatusMaxOnlineTime_Type=TimeInterval
_CwdxIfHeSuStatusMaxOnlineTime_Object=MibTableColumn
cwdxIfHeSuStatusMaxOnlineTime=_CwdxIfHeSuStatusMaxOnlineTime_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,6),_CwdxIfHeSuStatusMaxOnlineTime_Type())
cwdxIfHeSuStatusMaxOnlineTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusMaxOnlineTime.setStatus(_A)
_CwdxIfHeSuStatusMinOfflineTime_Type=TimeInterval
_CwdxIfHeSuStatusMinOfflineTime_Object=MibTableColumn
cwdxIfHeSuStatusMinOfflineTime=_CwdxIfHeSuStatusMinOfflineTime_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,7),_CwdxIfHeSuStatusMinOfflineTime_Type())
cwdxIfHeSuStatusMinOfflineTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusMinOfflineTime.setStatus(_A)
_CwdxIfHeSuStatusAvgOfflineTime_Type=TimeInterval
_CwdxIfHeSuStatusAvgOfflineTime_Object=MibTableColumn
cwdxIfHeSuStatusAvgOfflineTime=_CwdxIfHeSuStatusAvgOfflineTime_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,8),_CwdxIfHeSuStatusAvgOfflineTime_Type())
cwdxIfHeSuStatusAvgOfflineTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusAvgOfflineTime.setStatus(_A)
_CwdxIfHeSuStatusMaxOfflineTime_Type=TimeInterval
_CwdxIfHeSuStatusMaxOfflineTime_Object=MibTableColumn
cwdxIfHeSuStatusMaxOfflineTime=_CwdxIfHeSuStatusMaxOfflineTime_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,9),_CwdxIfHeSuStatusMaxOfflineTime_Type())
cwdxIfHeSuStatusMaxOfflineTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusMaxOfflineTime.setStatus(_A)
class _CwdxIfHeSuStatusDynSidCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_CwdxIfHeSuStatusDynSidCount_Type.__name__=_C
_CwdxIfHeSuStatusDynSidCount_Object=MibTableColumn
cwdxIfHeSuStatusDynSidCount=_CwdxIfHeSuStatusDynSidCount_Object((1,3,6,1,4,1,9,9,169,1,3,3,1,10),_CwdxIfHeSuStatusDynSidCount_Type())
cwdxIfHeSuStatusDynSidCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxIfHeSuStatusDynSidCount.setStatus(_A)
_CwdxHeMacExtTable_Object=MibTable
cwdxHeMacExtTable=_CwdxHeMacExtTable_Object((1,3,6,1,4,1,9,9,169,1,3,4))
if mibBuilder.loadTexts:cwdxHeMacExtTable.setStatus(_A)
_CwdxHeMacExtEntry_Object=MibTableRow
cwdxHeMacExtEntry=_CwdxHeMacExtEntry_Object((1,3,6,1,4,1,9,9,169,1,3,4,1))
if mibBuilder.loadTexts:cwdxHeMacExtEntry.setStatus(_A)
_CwdxHeSuOnOffTrapEnable_Type=TruthValue
_CwdxHeSuOnOffTrapEnable_Object=MibTableColumn
cwdxHeSuOnOffTrapEnable=_CwdxHeSuOnOffTrapEnable_Object((1,3,6,1,4,1,9,9,169,1,3,4,1,1),_CwdxHeSuOnOffTrapEnable_Type())
cwdxHeSuOnOffTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxHeSuOnOffTrapEnable.setStatus(_A)
class _CwdxHeSuOnOffTrapInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_CwdxHeSuOnOffTrapInterval_Type.__name__=_C
_CwdxHeSuOnOffTrapInterval_Object=MibTableColumn
cwdxHeSuOnOffTrapInterval=_CwdxHeSuOnOffTrapInterval_Object((1,3,6,1,4,1,9,9,169,1,3,4,1,2),_CwdxHeSuOnOffTrapInterval_Type())
cwdxHeSuOnOffTrapInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxHeSuOnOffTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:cwdxHeSuOnOffTrapInterval.setUnits('seconds')
class _CwdxHeSuDefaultMaxCpes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CwdxHeSuDefaultMaxCpes_Type.__name__=_C
_CwdxHeSuDefaultMaxCpes_Object=MibTableColumn
cwdxHeSuDefaultMaxCpes=_CwdxHeSuDefaultMaxCpes_Object((1,3,6,1,4,1,9,9,169,1,3,4,1,3),_CwdxHeSuDefaultMaxCpes_Type())
cwdxHeSuDefaultMaxCpes.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxHeSuDefaultMaxCpes.setStatus(_A)
class _CwdxHeTotalSusRegistered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwdxHeTotalSusRegistered_Type.__name__=_C
_CwdxHeTotalSusRegistered_Object=MibTableColumn
cwdxHeTotalSusRegistered=_CwdxHeTotalSusRegistered_Object((1,3,6,1,4,1,9,9,169,1,3,4,1,4),_CwdxHeTotalSusRegistered_Type())
cwdxHeTotalSusRegistered.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxHeTotalSusRegistered.setStatus(_A)
class _CwdxHeTotalSusOffline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwdxHeTotalSusOffline_Type.__name__=_C
_CwdxHeTotalSusOffline_Object=MibTableColumn
cwdxHeTotalSusOffline=_CwdxHeTotalSusOffline_Object((1,3,6,1,4,1,9,9,169,1,3,4,1,5),_CwdxHeTotalSusOffline_Type())
cwdxHeTotalSusOffline.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxHeTotalSusOffline.setStatus(_A)
class _CwdxHeSuChOverTimeExpiration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_CwdxHeSuChOverTimeExpiration_Type.__name__=_C
_CwdxHeSuChOverTimeExpiration_Object=MibScalar
cwdxHeSuChOverTimeExpiration=_CwdxHeSuChOverTimeExpiration_Object((1,3,6,1,4,1,9,9,169,1,3,5),_CwdxHeSuChOverTimeExpiration_Type())
cwdxHeSuChOverTimeExpiration.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxHeSuChOverTimeExpiration.setStatus(_A)
if mibBuilder.loadTexts:cwdxHeSuChOverTimeExpiration.setUnits('minutes')
_CwdxHeSuChOverTable_Object=MibTable
cwdxHeSuChOverTable=_CwdxHeSuChOverTable_Object((1,3,6,1,4,1,9,9,169,1,3,6))
if mibBuilder.loadTexts:cwdxHeSuChOverTable.setStatus(_A)
_CwdxHeSuChOverEntry_Object=MibTableRow
cwdxHeSuChOverEntry=_CwdxHeSuChOverEntry_Object((1,3,6,1,4,1,9,9,169,1,3,6,1))
cwdxHeSuChOverEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:cwdxHeSuChOverEntry.setStatus(_A)
class _CwdxHeSuChOverSerialNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwdxHeSuChOverSerialNumber_Type.__name__=_C
_CwdxHeSuChOverSerialNumber_Object=MibTableColumn
cwdxHeSuChOverSerialNumber=_CwdxHeSuChOverSerialNumber_Object((1,3,6,1,4,1,9,9,169,1,3,6,1,1),_CwdxHeSuChOverSerialNumber_Type())
cwdxHeSuChOverSerialNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cwdxHeSuChOverSerialNumber.setStatus(_A)
_CwdxHeSuChOverMacAddress_Type=MacAddress
_CwdxHeSuChOverMacAddress_Object=MibTableColumn
cwdxHeSuChOverMacAddress=_CwdxHeSuChOverMacAddress_Object((1,3,6,1,4,1,9,9,169,1,3,6,1,2),_CwdxHeSuChOverMacAddress_Type())
cwdxHeSuChOverMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxHeSuChOverMacAddress.setStatus(_A)
class _CwdxHeSuChOverDownFrequency_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CwdxHeSuChOverDownFrequency_Type.__name__=_C
_CwdxHeSuChOverDownFrequency_Object=MibTableColumn
cwdxHeSuChOverDownFrequency=_CwdxHeSuChOverDownFrequency_Object((1,3,6,1,4,1,9,9,169,1,3,6,1,3),_CwdxHeSuChOverDownFrequency_Type())
cwdxHeSuChOverDownFrequency.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxHeSuChOverDownFrequency.setStatus(_A)
if mibBuilder.loadTexts:cwdxHeSuChOverDownFrequency.setUnits('hertz')
class _CwdxHeSuChOverUpChannelId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_CwdxHeSuChOverUpChannelId_Type.__name__=_C
_CwdxHeSuChOverUpChannelId_Object=MibTableColumn
cwdxHeSuChOverUpChannelId=_CwdxHeSuChOverUpChannelId_Object((1,3,6,1,4,1,9,9,169,1,3,6,1,4),_CwdxHeSuChOverUpChannelId_Type())
cwdxHeSuChOverUpChannelId.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxHeSuChOverUpChannelId.setStatus(_A)
class _CwdxHeSuChOverTrapOnCompletion_Type(TruthValue):defaultValue=2
_CwdxHeSuChOverTrapOnCompletion_Type.__name__=_Y
_CwdxHeSuChOverTrapOnCompletion_Object=MibTableColumn
cwdxHeSuChOverTrapOnCompletion=_CwdxHeSuChOverTrapOnCompletion_Object((1,3,6,1,4,1,9,9,169,1,3,6,1,5),_CwdxHeSuChOverTrapOnCompletion_Type())
cwdxHeSuChOverTrapOnCompletion.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxHeSuChOverTrapOnCompletion.setStatus(_A)
_CwdxHeSuChOverOpInitiatedTime_Type=TimeStamp
_CwdxHeSuChOverOpInitiatedTime_Object=MibTableColumn
cwdxHeSuChOverOpInitiatedTime=_CwdxHeSuChOverOpInitiatedTime_Object((1,3,6,1,4,1,9,9,169,1,3,6,1,6),_CwdxHeSuChOverOpInitiatedTime_Type())
cwdxHeSuChOverOpInitiatedTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxHeSuChOverOpInitiatedTime.setStatus(_A)
class _CwdxHeSuChOverState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('messageSent',1),('commandNotActive',2),('noOpNeeded',3),('suNotFound',4),('waitToSendMessage',5),('timeOut',6)))
_CwdxHeSuChOverState_Type.__name__=_C
_CwdxHeSuChOverState_Object=MibTableColumn
cwdxHeSuChOverState=_CwdxHeSuChOverState_Object((1,3,6,1,4,1,9,9,169,1,3,6,1,7),_CwdxHeSuChOverState_Type())
cwdxHeSuChOverState.setMaxAccess(_D)
if mibBuilder.loadTexts:cwdxHeSuChOverState.setStatus(_A)
_CwdxHeSuChOverRowStatus_Type=RowStatus
_CwdxHeSuChOverRowStatus_Object=MibTableColumn
cwdxHeSuChOverRowStatus=_CwdxHeSuChOverRowStatus_Object((1,3,6,1,4,1,9,9,169,1,3,6,1,8),_CwdxHeSuChOverRowStatus_Type())
cwdxHeSuChOverRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxHeSuChOverRowStatus.setStatus(_A)
_CwdxHeSuTable_Object=MibTable
cwdxHeSuTable=_CwdxHeSuTable_Object((1,3,6,1,4,1,9,9,169,1,3,7))
if mibBuilder.loadTexts:cwdxHeSuTable.setStatus(_A)
_CwdxHeSuEntry_Object=MibTableRow
cwdxHeSuEntry=_CwdxHeSuEntry_Object((1,3,6,1,4,1,9,9,169,1,3,7,1))
cwdxHeSuEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:cwdxHeSuEntry.setStatus(_A)
class _CwdxHeSuMaxCpeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_CwdxHeSuMaxCpeNumber_Type.__name__=_C
_CwdxHeSuMaxCpeNumber_Object=MibTableColumn
cwdxHeSuMaxCpeNumber=_CwdxHeSuMaxCpeNumber_Object((1,3,6,1,4,1,9,9,169,1,3,7,1,1),_CwdxHeSuMaxCpeNumber_Type())
cwdxHeSuMaxCpeNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxHeSuMaxCpeNumber.setStatus(_A)
_CwdxQosProfileExtObjects_ObjectIdentity=ObjectIdentity
cwdxQosProfileExtObjects=_CwdxQosProfileExtObjects_ObjectIdentity((1,3,6,1,4,1,9,9,169,1,4))
_CwdxQosProfileExtTable_Object=MibTable
cwdxQosProfileExtTable=_CwdxQosProfileExtTable_Object((1,3,6,1,4,1,9,9,169,1,4,1))
if mibBuilder.loadTexts:cwdxQosProfileExtTable.setStatus(_A)
_CwdxQosProfileExtEntry_Object=MibTableRow
cwdxQosProfileExtEntry=_CwdxQosProfileExtEntry_Object((1,3,6,1,4,1,9,9,169,1,4,1,1))
if mibBuilder.loadTexts:cwdxQosProfileExtEntry.setStatus(_A)
class _CwdxQosProfGrantInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwdxQosProfGrantInterval_Type.__name__=_C
_CwdxQosProfGrantInterval_Object=MibTableColumn
cwdxQosProfGrantInterval=_CwdxQosProfGrantInterval_Object((1,3,6,1,4,1,9,9,169,1,4,1,1,1),_CwdxQosProfGrantInterval_Type())
cwdxQosProfGrantInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxQosProfGrantInterval.setStatus(_A)
if mibBuilder.loadTexts:cwdxQosProfGrantInterval.setUnits('milliseconds')
class _CwdxQosProfGrantSize_Type(Integer32):defaultValue=229;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwdxQosProfGrantSize_Type.__name__=_C
_CwdxQosProfGrantSize_Object=MibTableColumn
cwdxQosProfGrantSize=_CwdxQosProfGrantSize_Object((1,3,6,1,4,1,9,9,169,1,4,1,1,2),_CwdxQosProfGrantSize_Type())
cwdxQosProfGrantSize.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxQosProfGrantSize.setStatus(_A)
if mibBuilder.loadTexts:cwdxQosProfGrantSize.setUnits('bytes')
class _CwdxQosProfName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CwdxQosProfName_Type.__name__=_X
_CwdxQosProfName_Object=MibTableColumn
cwdxQosProfName=_CwdxQosProfName_Object((1,3,6,1,4,1,9,9,169,1,4,1,1,3),_CwdxQosProfName_Type())
cwdxQosProfName.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxQosProfName.setStatus(_A)
class _CwdxQosProfTosOverwriteMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CwdxQosProfTosOverwriteMask_Type.__name__=_C
_CwdxQosProfTosOverwriteMask_Object=MibTableColumn
cwdxQosProfTosOverwriteMask=_CwdxQosProfTosOverwriteMask_Object((1,3,6,1,4,1,9,9,169,1,4,1,1,4),_CwdxQosProfTosOverwriteMask_Type())
cwdxQosProfTosOverwriteMask.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxQosProfTosOverwriteMask.setStatus(_A)
class _CwdxQosProfTosOverwriteValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CwdxQosProfTosOverwriteValue_Type.__name__=_C
_CwdxQosProfTosOverwriteValue_Object=MibTableColumn
cwdxQosProfTosOverwriteValue=_CwdxQosProfTosOverwriteValue_Object((1,3,6,1,4,1,9,9,169,1,4,1,1,5),_CwdxQosProfTosOverwriteValue_Type())
cwdxQosProfTosOverwriteValue.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdxQosProfTosOverwriteValue.setStatus(_A)
_CwdxQosIpTosRatelimitTable_Object=MibTable
cwdxQosIpTosRatelimitTable=_CwdxQosIpTosRatelimitTable_Object((1,3,6,1,4,1,9,9,169,1,4,2))
if mibBuilder.loadTexts:cwdxQosIpTosRatelimitTable.setStatus(_A)
_CwdxQosIpTosRatelimitEntry_Object=MibTableRow
cwdxQosIpTosRatelimitEntry=_CwdxQosIpTosRatelimitEntry_Object((1,3,6,1,4,1,9,9,169,1,4,2,1))
cwdxQosIpTosRatelimitEntry.setIndexNames((0,_G,_W),(0,_B,_f))
if mibBuilder.loadTexts:cwdxQosIpTosRatelimitEntry.setStatus(_A)
class _CwdxQosIpTosRatelimitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CwdxQosIpTosRatelimitIndex_Type.__name__=_C
_CwdxQosIpTosRatelimitIndex_Object=MibTableColumn
cwdxQosIpTosRatelimitIndex=_CwdxQosIpTosRatelimitIndex_Object((1,3,6,1,4,1,9,9,169,1,4,2,1,1),_CwdxQosIpTosRatelimitIndex_Type())
cwdxQosIpTosRatelimitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cwdxQosIpTosRatelimitIndex.setStatus(_A)
class _CwdxQosIpTosRatelimitMaxDownRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CwdxQosIpTosRatelimitMaxDownRate_Type.__name__=_C
_CwdxQosIpTosRatelimitMaxDownRate_Object=MibTableColumn
cwdxQosIpTosRatelimitMaxDownRate=_CwdxQosIpTosRatelimitMaxDownRate_Object((1,3,6,1,4,1,9,9,169,1,4,2,1,2),_CwdxQosIpTosRatelimitMaxDownRate_Type())
cwdxQosIpTosRatelimitMaxDownRate.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdxQosIpTosRatelimitMaxDownRate.setStatus(_A)
if mibBuilder.loadTexts:cwdxQosIpTosRatelimitMaxDownRate.setUnits('bps')
_CiscoWirelessDocsExtNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoWirelessDocsExtNotificationsPrefix=_CiscoWirelessDocsExtNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,169,2))
_CiscoWirelessDocsExtNotifications_ObjectIdentity=ObjectIdentity
ciscoWirelessDocsExtNotifications=_CiscoWirelessDocsExtNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,169,2,0))
_CiscoWirelessDocsExtConformance_ObjectIdentity=ObjectIdentity
ciscoWirelessDocsExtConformance=_CiscoWirelessDocsExtConformance_ObjectIdentity((1,3,6,1,4,1,9,9,169,3))
_CwdxDocsExtCompliances_ObjectIdentity=ObjectIdentity
cwdxDocsExtCompliances=_CwdxDocsExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,169,3,1))
_CwdxDocsExtGroups_ObjectIdentity=ObjectIdentity
cwdxDocsExtGroups=_CwdxDocsExtGroups_ObjectIdentity((1,3,6,1,4,1,9,9,169,3,2))
cwdIfHeServiceEntry.registerAugmentions((_B,_g))
cwdxHeServiceExtEntry.setIndexNames(*cwdIfHeServiceEntry.getIndexNames())
cwdIfHeSuStatusEntry.registerAugmentions((_B,_h))
cwdxHeSuStatusExtEntry.setIndexNames(*cwdIfHeSuStatusEntry.getIndexNames())
cwdIfHeMacEntry.registerAugmentions((_B,_i))
cwdxHeMacExtEntry.setIndexNames(*cwdIfHeMacEntry.getIndexNames())
cwdIfQosProfileEntry.registerAugmentions((_B,_j))
cwdxQosProfileExtEntry.setIndexNames(*cwdIfQosProfileEntry.getIndexNames())
cwdxQosCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,169,3,2,1))
cwdxQosCtrlGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:cwdxQosCtrlGroup.setStatus(_A)
cwdxQosQueueGroup=ObjectGroup((1,3,6,1,4,1,9,9,169,3,2,2))
cwdxQosQueueGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:cwdxQosQueueGroup.setStatus(_A)
cwdxHeSuCpeGroup=ObjectGroup((1,3,6,1,4,1,9,9,169,3,2,3))
cwdxHeSuCpeGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_K),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_L),(_B,_M),(_B,_N),(_B,_AR),(_B,_O),(_B,_P),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:cwdxHeSuCpeGroup.setStatus(_A)
cwdxHeSuOnOffNotification=NotificationType((1,3,6,1,4,1,9,9,169,2,0,1))
cwdxHeSuOnOffNotification.setObjects(*((_G,_T),(_G,_S),(_G,_Q),(_G,_V),(_G,_U),(_B,_K)))
if mibBuilder.loadTexts:cwdxHeSuOnOffNotification.setStatus(_A)
cwdxHeSuChOverNotification=NotificationType((1,3,6,1,4,1,9,9,169,2,0,2))
cwdxHeSuChOverNotification.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cwdxHeSuChOverNotification.setStatus(_A)
cwdxDocsExtCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,169,3,1,1))
cwdxDocsExtCompliance.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:cwdxDocsExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWirelessDocsExtMIB':ciscoWirelessDocsExtMIB,'ciscoWirelessDocsExtMIBObjects':ciscoWirelessDocsExtMIBObjects,'cwdxQosCtrlObjects':cwdxQosCtrlObjects,'cwdxQosCtrlUpTable':cwdxQosCtrlUpTable,'cwdxQosCtrlUpEntry':cwdxQosCtrlUpEntry,_k:cwdxQosCtrlUpAdmissionCtrl,_l:cwdxQosCtrlUpMaxRsvdBWPercent,_m:cwdxQosCtrlUpAdmissionRejects,_n:cwdxQosCtrlUpReservedBW,_o:cwdxQosCtrlUpMaxVirtualBW,'cwdxQosIfRateLimitTable':cwdxQosIfRateLimitTable,'cwdxQosIfRateLimitEntry':cwdxQosIfRateLimitEntry,_p:cwdxQosIfRateLimitAlgo,_q:cwdxQosIfRateLimitExpWgt,_r:cwdxQosIfRateLimitShpMaxDelay,_s:cwdxQosIfRateLimitShpGranularity,'cwdxHeServiceExtTable':cwdxHeServiceExtTable,_g:cwdxHeServiceExtEntry,_t:cwdxIfHeServiceOutOctets,_u:cwdxIfHeServiceOutPackets,_v:cwdxQosMaxUpBWExcessRequests,_w:cwdxQosMaxDownBWExcessPackets,'cwdxQosQueueObjects':cwdxQosQueueObjects,'cwdxBWQueueTable':cwdxBWQueueTable,'cwdxBWQueueEntry':cwdxBWQueueEntry,_a:cwdxBWQueueNameCode,_A3:cwdxBWQueueOrder,_A4:cwdxBWQueueNumServedBeforeYield,_A5:cwdxBWQueueType,_A6:cwdxBWQueueMaxDepth,_A7:cwdxBWQueueDepth,_A8:cwdxBWQueueDiscards,'cwdxHeSuCpeObjects':cwdxHeSuCpeObjects,'cwdxCpeTable':cwdxCpeTable,'cwdxCpeEntry':cwdxCpeEntry,_b:cwdxCpeStatusIndex,_c:cwdxCpeMacAddress,_A9:cwdxCpeIpAddress,_AA:cwdxCpeAccessGroup,'cwdxSuMappingTable':cwdxSuMappingTable,'cwdxSuMappingEntry':cwdxSuMappingEntry,_AB:cwdxSuMappingStatusIndex,_d:cwdxSuMappingMacAddress,'cwdxHeSuStatusExtTable':cwdxHeSuStatusExtTable,_h:cwdxHeSuStatusExtEntry,_K:cwdxHeSuStatusValue,_AC:cwdxIfHeSuStatusOnlineTimes,_AD:cwdxIfHeSuStatusPercentOnline,_AE:cwdxIfHeSuStatusMinOnlineTime,_AF:cwdxIfHeSuStatusAvgOnlineTime,_AG:cwdxIfHeSuStatusMaxOnlineTime,_AH:cwdxIfHeSuStatusMinOfflineTime,_AI:cwdxIfHeSuStatusAvgOfflineTime,_AJ:cwdxIfHeSuStatusMaxOfflineTime,_AK:cwdxIfHeSuStatusDynSidCount,'cwdxHeMacExtTable':cwdxHeMacExtTable,_i:cwdxHeMacExtEntry,_AL:cwdxHeSuOnOffTrapEnable,_AM:cwdxHeSuOnOffTrapInterval,_AN:cwdxHeSuDefaultMaxCpes,_AO:cwdxHeTotalSusRegistered,_AP:cwdxHeTotalSusOffline,_AQ:cwdxHeSuChOverTimeExpiration,'cwdxHeSuChOverTable':cwdxHeSuChOverTable,'cwdxHeSuChOverEntry':cwdxHeSuChOverEntry,_e:cwdxHeSuChOverSerialNumber,_L:cwdxHeSuChOverMacAddress,_M:cwdxHeSuChOverDownFrequency,_N:cwdxHeSuChOverUpChannelId,_AR:cwdxHeSuChOverTrapOnCompletion,_O:cwdxHeSuChOverOpInitiatedTime,_P:cwdxHeSuChOverState,_AS:cwdxHeSuChOverRowStatus,'cwdxHeSuTable':cwdxHeSuTable,'cwdxHeSuEntry':cwdxHeSuEntry,_AT:cwdxHeSuMaxCpeNumber,'cwdxQosProfileExtObjects':cwdxQosProfileExtObjects,'cwdxQosProfileExtTable':cwdxQosProfileExtTable,_j:cwdxQosProfileExtEntry,_x:cwdxQosProfGrantInterval,_y:cwdxQosProfGrantSize,_z:cwdxQosProfName,_A0:cwdxQosProfTosOverwriteMask,_A1:cwdxQosProfTosOverwriteValue,'cwdxQosIpTosRatelimitTable':cwdxQosIpTosRatelimitTable,'cwdxQosIpTosRatelimitEntry':cwdxQosIpTosRatelimitEntry,_f:cwdxQosIpTosRatelimitIndex,_A2:cwdxQosIpTosRatelimitMaxDownRate,'ciscoWirelessDocsExtNotificationsPrefix':ciscoWirelessDocsExtNotificationsPrefix,'ciscoWirelessDocsExtNotifications':ciscoWirelessDocsExtNotifications,'cwdxHeSuOnOffNotification':cwdxHeSuOnOffNotification,'cwdxHeSuChOverNotification':cwdxHeSuChOverNotification,'ciscoWirelessDocsExtConformance':ciscoWirelessDocsExtConformance,'cwdxDocsExtCompliances':cwdxDocsExtCompliances,'cwdxDocsExtCompliance':cwdxDocsExtCompliance,'cwdxDocsExtGroups':cwdxDocsExtGroups,_AU:cwdxQosCtrlGroup,_AV:cwdxQosQueueGroup,_AW:cwdxHeSuCpeGroup})