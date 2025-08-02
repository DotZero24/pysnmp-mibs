_B9='cwdIfModGroup'
_B8='cwdIfQosHeGroup'
_B7='cwdIfQosGroup'
_B6='cwdIfHeGroup'
_B5='cwdIfSuGroup'
_B4='cwdIfBasicGroup'
_B3='cwdIfHeServiceInPackets'
_B2='cwdIfHeServiceInOctets'
_B1='cwdIfHeServiceCreateTime'
_B0='cwdIfHeServiceQosProfile'
_A_='cwdIfHeServiceAdminStatus'
_Az='cwdIfHeServiceSuStatusIndex'
_Ay='cwdIfHeSuStatusServiceId'
_Ax='cwdIfHeSuStatusIfIndex'
_Aw='cwdIfHeSuStatusValue'
_Av='cwdIfHeSuStatusTimingOffset'
_Au='cwdIfHeSuStatusRxPower'
_At='cwdIfHeSuStatusUpChanIfIndex'
_As='cwdIfHeSuStatusDownChanIfIndex'
_Ar='cwdIfHeSuStatusIpAddress'
_Aq='cwdIfHeSuStatusMacAddress'
_Ap='cwdIfHeStatusT5Timeouts'
_Ao='cwdIfHeStatusInvalidDataReqs'
_An='cwdIfHeStatusFailedRegReqs'
_Am='cwdIfHeStatusInvalidRegReqs'
_Al='cwdIfHeStatusRangingAborteds'
_Ak='cwdIfHeStatusInvalidRangeReqs'
_Aj='cwdIfHeInvitedRangingAttempts'
_Ai='cwdIfHeInsertionInterval'
_Ah='cwdIfHeMaxServiceIds'
_Ag='cwdIfHeUcdInterval'
_Af='cwdIfHeSyncInterval'
_Ae='cwdIfHeCapabilities'
_Ad='cwdIfModMultipathRobustness'
_Ac='cwdIfModBurstLength'
_Ab='cwdIfModThroughput'
_Aa='cwdIfModBandwidth'
_AZ='cwdIfModRowStatus'
_AY='cwdIfHeQosProfilePermissions'
_AX='cwdIfQosProfStatus'
_AW='cwdIfQosProfBaselinePrivacy'
_AV='cwdIfQosProfMaxTxBurst'
_AU='cwdIfQosProfMaxDownBandwidth'
_AT='cwdIfQosProfGuarUpBandwidth'
_AS='cwdIfQosProfMaxUpBandwidth'
_AR='cwdIfQosProfPriority'
_AQ='cwdIfSuServiceRqExceeded'
_AP='cwdIfSuServiceRqRetries'
_AO='cwdIfSuServiceTxExceeded'
_AN='cwdIfSuServiceTxRetries'
_AM='cwdIfSuServiceTxSlotsDed'
_AL='cwdIfSuServiceTxSlotsImmed'
_AK='cwdIfSuServiceQosProfile'
_AJ='cwdIfSuStatusRangingAborteds'
_AI='cwdIfSuStatusT4Timeouts'
_AH='cwdIfSuStatusT3Timeouts'
_AG='cwdIfSuStatusT2Timeouts'
_AF='cwdIfSuStatusT1Timeouts'
_AE='cwdIfSuStatusInvalidRegResp'
_AD='cwdIfSuStatusInvalidRangingResp'
_AC='cwdIfSuStatusInvalidUcds'
_AB='cwdIfSuStatusInvalidMaps'
_AA='cwdIfSuStatusLostSyncs'
_A9='cwdIfSuStatusResets'
_A8='cwdIfSuStatusTxPower'
_A7='cwdIfSuStatusCode'
_A6='cwdIfSuStatusValue'
_A5='cwdIfSuRangingRespTimeout'
_A4='cwdIfSuCapabilities'
_A3='cwdIfSuHeAddress'
_A2='cwdIfSigQSignalNoise'
_A1='cwdIfSigQUncorrectables'
_A0='cwdIfSigQCorrecteds'
_z='cwdIfSigQUnerroreds'
_y='cwdIfSigQIncludesContention'
_x='cwdIfUpChannelTxBackoffEnd'
_w='cwdIfUpChannelTxBackoffStart'
_v='cwdIfUpChannelRangBackoffEnd'
_u='cwdIfUpChannelRangBackoffStart'
_t='cwdIfUpChannelTxTimingOffset'
_s='cwdIfUpChannelSlotSize'
_r='cwdIfUpChannelModProfileIndex'
_q='cwdIfUpChannelTargetPower'
_p='cwdIfUpChannelWidth'
_o='cwdIfUpChannelFrequency'
_n='cwdIfUpChannelId'
_m='cwdIfUpChannelSubChannelNumber'
_l='cwdIfDownChannelModProfileIndex'
_k='cwdIfDownChannelPower'
_j='cwdIfDownChannelWidth'
_i='cwdIfDownChannelFrequency'
_h='cwdIfDownChannelId'
_g='cwdIfDownChannelSubChannelNumber'
_f='cwdIfChannelSubChannelPlanVer'
_e='cwdIfChannelMiniSlotTimeBaseTick'
_d='cwdIfChannelDownWidth'
_c='cwdIfChannelDownFrequency'
_b='cwdIfChannelUpWidth'
_a='cwdIfChannelUpFrequency'
_Z='cwdIfHeServiceId'
_Y='cwdIfHeSuStatusIndex'
_X='Milliseconds'
_W='cwdIfSuServiceId'
_V='accessDenied'
_U='registrationComplete'
_T='ipComplete'
_S='rangingComplete'
_R='concatenation'
_Q='atmCells'
_P='cwdIfModIndex'
_O='cwdIfQosProfIndex'
_N='TruthValue'
_M='TimeInterval'
_L='dBm - decibel milliwatts'
_K='Bits'
_J='not-accessible'
_I='kHz'
_H='ifIndex'
_G='IF-MIB'
_F='read-create'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-WIRELESS-DOCS-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CwrdBm,=mibBuilder.importSymbols('CISCO-WIRELESS-TC-MIB','CwrdBm')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndex','InterfaceIndexOrZero',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_M,'TimeStamp',_N)
ciscoWirelessDocsIfMib=ModuleIdentity((1,3,6,1,4,1,9,9,167))
if mibBuilder.loadTexts:ciscoWirelessDocsIfMib.setRevisions(('2005-12-27 10:03','2000-06-07 10:03'))
_CwdIfMibObjects_ObjectIdentity=ObjectIdentity
cwdIfMibObjects=_CwdIfMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,167,1))
_CwdIfBaseObjects_ObjectIdentity=ObjectIdentity
cwdIfBaseObjects=_CwdIfBaseObjects_ObjectIdentity((1,3,6,1,4,1,9,9,167,1,1))
_CwdIfChannelTable_Object=MibTable
cwdIfChannelTable=_CwdIfChannelTable_Object((1,3,6,1,4,1,9,9,167,1,1,1))
if mibBuilder.loadTexts:cwdIfChannelTable.setStatus(_A)
_CwdIfChannelEntry_Object=MibTableRow
cwdIfChannelEntry=_CwdIfChannelEntry_Object((1,3,6,1,4,1,9,9,167,1,1,1,1))
cwdIfChannelEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwdIfChannelEntry.setStatus(_A)
class _CwdIfChannelUpFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000000))
_CwdIfChannelUpFrequency_Type.__name__=_D
_CwdIfChannelUpFrequency_Object=MibTableColumn
cwdIfChannelUpFrequency=_CwdIfChannelUpFrequency_Object((1,3,6,1,4,1,9,9,167,1,1,1,1,1),_CwdIfChannelUpFrequency_Type())
cwdIfChannelUpFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfChannelUpFrequency.setStatus(_A)
if mibBuilder.loadTexts:cwdIfChannelUpFrequency.setUnits(_I)
class _CwdIfChannelUpWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500000))
_CwdIfChannelUpWidth_Type.__name__=_D
_CwdIfChannelUpWidth_Object=MibTableColumn
cwdIfChannelUpWidth=_CwdIfChannelUpWidth_Object((1,3,6,1,4,1,9,9,167,1,1,1,1,2),_CwdIfChannelUpWidth_Type())
cwdIfChannelUpWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfChannelUpWidth.setStatus(_A)
if mibBuilder.loadTexts:cwdIfChannelUpWidth.setUnits(_I)
class _CwdIfChannelDownFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000000))
_CwdIfChannelDownFrequency_Type.__name__=_D
_CwdIfChannelDownFrequency_Object=MibTableColumn
cwdIfChannelDownFrequency=_CwdIfChannelDownFrequency_Object((1,3,6,1,4,1,9,9,167,1,1,1,1,3),_CwdIfChannelDownFrequency_Type())
cwdIfChannelDownFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfChannelDownFrequency.setStatus(_A)
if mibBuilder.loadTexts:cwdIfChannelDownFrequency.setUnits(_I)
class _CwdIfChannelDownWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500000))
_CwdIfChannelDownWidth_Type.__name__=_D
_CwdIfChannelDownWidth_Object=MibTableColumn
cwdIfChannelDownWidth=_CwdIfChannelDownWidth_Object((1,3,6,1,4,1,9,9,167,1,1,1,1,4),_CwdIfChannelDownWidth_Type())
cwdIfChannelDownWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfChannelDownWidth.setStatus(_A)
if mibBuilder.loadTexts:cwdIfChannelDownWidth.setUnits(_I)
class _CwdIfChannelMiniSlotTimeBaseTick_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,102400000))
_CwdIfChannelMiniSlotTimeBaseTick_Type.__name__=_D
_CwdIfChannelMiniSlotTimeBaseTick_Object=MibTableColumn
cwdIfChannelMiniSlotTimeBaseTick=_CwdIfChannelMiniSlotTimeBaseTick_Object((1,3,6,1,4,1,9,9,167,1,1,1,1,5),_CwdIfChannelMiniSlotTimeBaseTick_Type())
cwdIfChannelMiniSlotTimeBaseTick.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfChannelMiniSlotTimeBaseTick.setStatus(_A)
if mibBuilder.loadTexts:cwdIfChannelMiniSlotTimeBaseTick.setUnits('Microseconds')
_CwdIfChannelSubChannelPlanVer_Type=Unsigned32
_CwdIfChannelSubChannelPlanVer_Object=MibTableColumn
cwdIfChannelSubChannelPlanVer=_CwdIfChannelSubChannelPlanVer_Object((1,3,6,1,4,1,9,9,167,1,1,1,1,6),_CwdIfChannelSubChannelPlanVer_Type())
cwdIfChannelSubChannelPlanVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfChannelSubChannelPlanVer.setStatus(_A)
_CwdIfDownstreamChannelTable_Object=MibTable
cwdIfDownstreamChannelTable=_CwdIfDownstreamChannelTable_Object((1,3,6,1,4,1,9,9,167,1,1,2))
if mibBuilder.loadTexts:cwdIfDownstreamChannelTable.setStatus(_A)
_CwdIfDownstreamChannelEntry_Object=MibTableRow
cwdIfDownstreamChannelEntry=_CwdIfDownstreamChannelEntry_Object((1,3,6,1,4,1,9,9,167,1,1,2,1))
cwdIfDownstreamChannelEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwdIfDownstreamChannelEntry.setStatus(_A)
class _CwdIfDownChannelSubChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CwdIfDownChannelSubChannelNumber_Type.__name__=_D
_CwdIfDownChannelSubChannelNumber_Object=MibTableColumn
cwdIfDownChannelSubChannelNumber=_CwdIfDownChannelSubChannelNumber_Object((1,3,6,1,4,1,9,9,167,1,1,2,1,1),_CwdIfDownChannelSubChannelNumber_Type())
cwdIfDownChannelSubChannelNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfDownChannelSubChannelNumber.setStatus(_A)
class _CwdIfDownChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CwdIfDownChannelId_Type.__name__=_D
_CwdIfDownChannelId_Object=MibTableColumn
cwdIfDownChannelId=_CwdIfDownChannelId_Object((1,3,6,1,4,1,9,9,167,1,1,2,1,2),_CwdIfDownChannelId_Type())
cwdIfDownChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfDownChannelId.setStatus(_A)
class _CwdIfDownChannelFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000000))
_CwdIfDownChannelFrequency_Type.__name__=_D
_CwdIfDownChannelFrequency_Object=MibTableColumn
cwdIfDownChannelFrequency=_CwdIfDownChannelFrequency_Object((1,3,6,1,4,1,9,9,167,1,1,2,1,3),_CwdIfDownChannelFrequency_Type())
cwdIfDownChannelFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfDownChannelFrequency.setStatus(_A)
if mibBuilder.loadTexts:cwdIfDownChannelFrequency.setUnits(_I)
class _CwdIfDownChannelWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500000))
_CwdIfDownChannelWidth_Type.__name__=_D
_CwdIfDownChannelWidth_Object=MibTableColumn
cwdIfDownChannelWidth=_CwdIfDownChannelWidth_Object((1,3,6,1,4,1,9,9,167,1,1,2,1,4),_CwdIfDownChannelWidth_Type())
cwdIfDownChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfDownChannelWidth.setStatus(_A)
if mibBuilder.loadTexts:cwdIfDownChannelWidth.setUnits(_I)
class _CwdIfDownChannelPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-80,50))
_CwdIfDownChannelPower_Type.__name__=_D
_CwdIfDownChannelPower_Object=MibTableColumn
cwdIfDownChannelPower=_CwdIfDownChannelPower_Object((1,3,6,1,4,1,9,9,167,1,1,2,1,5),_CwdIfDownChannelPower_Type())
cwdIfDownChannelPower.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfDownChannelPower.setStatus(_A)
if mibBuilder.loadTexts:cwdIfDownChannelPower.setUnits(_L)
_CwdIfDownChannelModProfileIndex_Type=Unsigned32
_CwdIfDownChannelModProfileIndex_Object=MibTableColumn
cwdIfDownChannelModProfileIndex=_CwdIfDownChannelModProfileIndex_Object((1,3,6,1,4,1,9,9,167,1,1,2,1,6),_CwdIfDownChannelModProfileIndex_Type())
cwdIfDownChannelModProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfDownChannelModProfileIndex.setStatus(_A)
_CwdIfUpstreamChannelTable_Object=MibTable
cwdIfUpstreamChannelTable=_CwdIfUpstreamChannelTable_Object((1,3,6,1,4,1,9,9,167,1,1,4))
if mibBuilder.loadTexts:cwdIfUpstreamChannelTable.setStatus(_A)
_CwdIfUpstreamChannelEntry_Object=MibTableRow
cwdIfUpstreamChannelEntry=_CwdIfUpstreamChannelEntry_Object((1,3,6,1,4,1,9,9,167,1,1,4,1))
cwdIfUpstreamChannelEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwdIfUpstreamChannelEntry.setStatus(_A)
class _CwdIfUpChannelSubChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CwdIfUpChannelSubChannelNumber_Type.__name__=_D
_CwdIfUpChannelSubChannelNumber_Object=MibTableColumn
cwdIfUpChannelSubChannelNumber=_CwdIfUpChannelSubChannelNumber_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,1),_CwdIfUpChannelSubChannelNumber_Type())
cwdIfUpChannelSubChannelNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfUpChannelSubChannelNumber.setStatus(_A)
class _CwdIfUpChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CwdIfUpChannelId_Type.__name__=_D
_CwdIfUpChannelId_Object=MibTableColumn
cwdIfUpChannelId=_CwdIfUpChannelId_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,2),_CwdIfUpChannelId_Type())
cwdIfUpChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfUpChannelId.setStatus(_A)
class _CwdIfUpChannelFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000000))
_CwdIfUpChannelFrequency_Type.__name__=_D
_CwdIfUpChannelFrequency_Object=MibTableColumn
cwdIfUpChannelFrequency=_CwdIfUpChannelFrequency_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,3),_CwdIfUpChannelFrequency_Type())
cwdIfUpChannelFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfUpChannelFrequency.setStatus(_A)
if mibBuilder.loadTexts:cwdIfUpChannelFrequency.setUnits(_I)
class _CwdIfUpChannelWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500000))
_CwdIfUpChannelWidth_Type.__name__=_D
_CwdIfUpChannelWidth_Object=MibTableColumn
cwdIfUpChannelWidth=_CwdIfUpChannelWidth_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,4),_CwdIfUpChannelWidth_Type())
cwdIfUpChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfUpChannelWidth.setStatus(_A)
if mibBuilder.loadTexts:cwdIfUpChannelWidth.setUnits(_I)
class _CwdIfUpChannelTargetPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-80,50))
_CwdIfUpChannelTargetPower_Type.__name__=_D
_CwdIfUpChannelTargetPower_Object=MibTableColumn
cwdIfUpChannelTargetPower=_CwdIfUpChannelTargetPower_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,5),_CwdIfUpChannelTargetPower_Type())
cwdIfUpChannelTargetPower.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfUpChannelTargetPower.setStatus(_A)
if mibBuilder.loadTexts:cwdIfUpChannelTargetPower.setUnits(_L)
_CwdIfUpChannelModProfileIndex_Type=Unsigned32
_CwdIfUpChannelModProfileIndex_Object=MibTableColumn
cwdIfUpChannelModProfileIndex=_CwdIfUpChannelModProfileIndex_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,6),_CwdIfUpChannelModProfileIndex_Type())
cwdIfUpChannelModProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfUpChannelModProfileIndex.setStatus(_A)
_CwdIfUpChannelSlotSize_Type=Unsigned32
_CwdIfUpChannelSlotSize_Object=MibTableColumn
cwdIfUpChannelSlotSize=_CwdIfUpChannelSlotSize_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,7),_CwdIfUpChannelSlotSize_Type())
cwdIfUpChannelSlotSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfUpChannelSlotSize.setStatus(_A)
_CwdIfUpChannelTxTimingOffset_Type=Unsigned32
_CwdIfUpChannelTxTimingOffset_Object=MibTableColumn
cwdIfUpChannelTxTimingOffset=_CwdIfUpChannelTxTimingOffset_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,8),_CwdIfUpChannelTxTimingOffset_Type())
cwdIfUpChannelTxTimingOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfUpChannelTxTimingOffset.setStatus(_A)
class _CwdIfUpChannelRangBackoffStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CwdIfUpChannelRangBackoffStart_Type.__name__=_D
_CwdIfUpChannelRangBackoffStart_Object=MibTableColumn
cwdIfUpChannelRangBackoffStart=_CwdIfUpChannelRangBackoffStart_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,9),_CwdIfUpChannelRangBackoffStart_Type())
cwdIfUpChannelRangBackoffStart.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfUpChannelRangBackoffStart.setStatus(_A)
class _CwdIfUpChannelRangBackoffEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CwdIfUpChannelRangBackoffEnd_Type.__name__=_D
_CwdIfUpChannelRangBackoffEnd_Object=MibTableColumn
cwdIfUpChannelRangBackoffEnd=_CwdIfUpChannelRangBackoffEnd_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,10),_CwdIfUpChannelRangBackoffEnd_Type())
cwdIfUpChannelRangBackoffEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfUpChannelRangBackoffEnd.setStatus(_A)
class _CwdIfUpChannelTxBackoffStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CwdIfUpChannelTxBackoffStart_Type.__name__=_D
_CwdIfUpChannelTxBackoffStart_Object=MibTableColumn
cwdIfUpChannelTxBackoffStart=_CwdIfUpChannelTxBackoffStart_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,11),_CwdIfUpChannelTxBackoffStart_Type())
cwdIfUpChannelTxBackoffStart.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfUpChannelTxBackoffStart.setStatus(_A)
class _CwdIfUpChannelTxBackoffEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CwdIfUpChannelTxBackoffEnd_Type.__name__=_D
_CwdIfUpChannelTxBackoffEnd_Object=MibTableColumn
cwdIfUpChannelTxBackoffEnd=_CwdIfUpChannelTxBackoffEnd_Object((1,3,6,1,4,1,9,9,167,1,1,4,1,12),_CwdIfUpChannelTxBackoffEnd_Type())
cwdIfUpChannelTxBackoffEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfUpChannelTxBackoffEnd.setStatus(_A)
_CwdIfQosProfileTable_Object=MibTable
cwdIfQosProfileTable=_CwdIfQosProfileTable_Object((1,3,6,1,4,1,9,9,167,1,1,5))
if mibBuilder.loadTexts:cwdIfQosProfileTable.setStatus(_A)
_CwdIfQosProfileEntry_Object=MibTableRow
cwdIfQosProfileEntry=_CwdIfQosProfileEntry_Object((1,3,6,1,4,1,9,9,167,1,1,5,1))
cwdIfQosProfileEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cwdIfQosProfileEntry.setStatus(_A)
class _CwdIfQosProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_CwdIfQosProfIndex_Type.__name__=_D
_CwdIfQosProfIndex_Object=MibTableColumn
cwdIfQosProfIndex=_CwdIfQosProfIndex_Object((1,3,6,1,4,1,9,9,167,1,1,5,1,1),_CwdIfQosProfIndex_Type())
cwdIfQosProfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cwdIfQosProfIndex.setStatus(_A)
class _CwdIfQosProfPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CwdIfQosProfPriority_Type.__name__=_D
_CwdIfQosProfPriority_Object=MibTableColumn
cwdIfQosProfPriority=_CwdIfQosProfPriority_Object((1,3,6,1,4,1,9,9,167,1,1,5,1,2),_CwdIfQosProfPriority_Type())
cwdIfQosProfPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfQosProfPriority.setStatus(_A)
class _CwdIfQosProfMaxUpBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CwdIfQosProfMaxUpBandwidth_Type.__name__=_D
_CwdIfQosProfMaxUpBandwidth_Object=MibTableColumn
cwdIfQosProfMaxUpBandwidth=_CwdIfQosProfMaxUpBandwidth_Object((1,3,6,1,4,1,9,9,167,1,1,5,1,3),_CwdIfQosProfMaxUpBandwidth_Type())
cwdIfQosProfMaxUpBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfQosProfMaxUpBandwidth.setStatus(_A)
class _CwdIfQosProfGuarUpBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CwdIfQosProfGuarUpBandwidth_Type.__name__=_D
_CwdIfQosProfGuarUpBandwidth_Object=MibTableColumn
cwdIfQosProfGuarUpBandwidth=_CwdIfQosProfGuarUpBandwidth_Object((1,3,6,1,4,1,9,9,167,1,1,5,1,4),_CwdIfQosProfGuarUpBandwidth_Type())
cwdIfQosProfGuarUpBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfQosProfGuarUpBandwidth.setStatus(_A)
class _CwdIfQosProfMaxDownBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CwdIfQosProfMaxDownBandwidth_Type.__name__=_D
_CwdIfQosProfMaxDownBandwidth_Object=MibTableColumn
cwdIfQosProfMaxDownBandwidth=_CwdIfQosProfMaxDownBandwidth_Object((1,3,6,1,4,1,9,9,167,1,1,5,1,5),_CwdIfQosProfMaxDownBandwidth_Type())
cwdIfQosProfMaxDownBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfQosProfMaxDownBandwidth.setStatus(_A)
class _CwdIfQosProfMaxTxBurst_Type(Integer32):defaultValue=0
_CwdIfQosProfMaxTxBurst_Type.__name__=_D
_CwdIfQosProfMaxTxBurst_Object=MibTableColumn
cwdIfQosProfMaxTxBurst=_CwdIfQosProfMaxTxBurst_Object((1,3,6,1,4,1,9,9,167,1,1,5,1,6),_CwdIfQosProfMaxTxBurst_Type())
cwdIfQosProfMaxTxBurst.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfQosProfMaxTxBurst.setStatus(_A)
class _CwdIfQosProfBaselinePrivacy_Type(TruthValue):defaultValue=2
_CwdIfQosProfBaselinePrivacy_Type.__name__=_N
_CwdIfQosProfBaselinePrivacy_Object=MibTableColumn
cwdIfQosProfBaselinePrivacy=_CwdIfQosProfBaselinePrivacy_Object((1,3,6,1,4,1,9,9,167,1,1,5,1,7),_CwdIfQosProfBaselinePrivacy_Type())
cwdIfQosProfBaselinePrivacy.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfQosProfBaselinePrivacy.setStatus(_A)
_CwdIfQosProfStatus_Type=RowStatus
_CwdIfQosProfStatus_Object=MibTableColumn
cwdIfQosProfStatus=_CwdIfQosProfStatus_Object((1,3,6,1,4,1,9,9,167,1,1,5,1,8),_CwdIfQosProfStatus_Type())
cwdIfQosProfStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfQosProfStatus.setStatus(_A)
_CwdIfSignalQualityTable_Object=MibTable
cwdIfSignalQualityTable=_CwdIfSignalQualityTable_Object((1,3,6,1,4,1,9,9,167,1,1,6))
if mibBuilder.loadTexts:cwdIfSignalQualityTable.setStatus(_A)
_CwdIfSignalQualityEntry_Object=MibTableRow
cwdIfSignalQualityEntry=_CwdIfSignalQualityEntry_Object((1,3,6,1,4,1,9,9,167,1,1,6,1))
cwdIfSignalQualityEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwdIfSignalQualityEntry.setStatus(_A)
_CwdIfSigQIncludesContention_Type=TruthValue
_CwdIfSigQIncludesContention_Object=MibTableColumn
cwdIfSigQIncludesContention=_CwdIfSigQIncludesContention_Object((1,3,6,1,4,1,9,9,167,1,1,6,1,1),_CwdIfSigQIncludesContention_Type())
cwdIfSigQIncludesContention.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSigQIncludesContention.setStatus(_A)
_CwdIfSigQUnerroreds_Type=Counter32
_CwdIfSigQUnerroreds_Object=MibTableColumn
cwdIfSigQUnerroreds=_CwdIfSigQUnerroreds_Object((1,3,6,1,4,1,9,9,167,1,1,6,1,2),_CwdIfSigQUnerroreds_Type())
cwdIfSigQUnerroreds.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSigQUnerroreds.setStatus(_A)
_CwdIfSigQCorrecteds_Type=Counter32
_CwdIfSigQCorrecteds_Object=MibTableColumn
cwdIfSigQCorrecteds=_CwdIfSigQCorrecteds_Object((1,3,6,1,4,1,9,9,167,1,1,6,1,3),_CwdIfSigQCorrecteds_Type())
cwdIfSigQCorrecteds.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSigQCorrecteds.setStatus(_A)
_CwdIfSigQUncorrectables_Type=Counter32
_CwdIfSigQUncorrectables_Object=MibTableColumn
cwdIfSigQUncorrectables=_CwdIfSigQUncorrectables_Object((1,3,6,1,4,1,9,9,167,1,1,6,1,4),_CwdIfSigQUncorrectables_Type())
cwdIfSigQUncorrectables.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSigQUncorrectables.setStatus(_A)
_CwdIfSigQSignalNoise_Type=CwrdBm
_CwdIfSigQSignalNoise_Object=MibTableColumn
cwdIfSigQSignalNoise=_CwdIfSigQSignalNoise_Object((1,3,6,1,4,1,9,9,167,1,1,6,1,5),_CwdIfSigQSignalNoise_Type())
cwdIfSigQSignalNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSigQSignalNoise.setStatus(_A)
_CwdIfModulationTable_Object=MibTable
cwdIfModulationTable=_CwdIfModulationTable_Object((1,3,6,1,4,1,9,9,167,1,1,7))
if mibBuilder.loadTexts:cwdIfModulationTable.setStatus(_A)
_CwdIfModulationEntry_Object=MibTableRow
cwdIfModulationEntry=_CwdIfModulationEntry_Object((1,3,6,1,4,1,9,9,167,1,1,7,1))
cwdIfModulationEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:cwdIfModulationEntry.setStatus(_A)
class _CwdIfModIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwdIfModIndex_Type.__name__=_D
_CwdIfModIndex_Object=MibTableColumn
cwdIfModIndex=_CwdIfModIndex_Object((1,3,6,1,4,1,9,9,167,1,1,7,1,1),_CwdIfModIndex_Type())
cwdIfModIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cwdIfModIndex.setStatus(_A)
_CwdIfModRowStatus_Type=RowStatus
_CwdIfModRowStatus_Object=MibTableColumn
cwdIfModRowStatus=_CwdIfModRowStatus_Object((1,3,6,1,4,1,9,9,167,1,1,7,1,2),_CwdIfModRowStatus_Type())
cwdIfModRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfModRowStatus.setStatus(_A)
class _CwdIfModBandwidth_Type(Integer32):defaultValue=6000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500000))
_CwdIfModBandwidth_Type.__name__=_D
_CwdIfModBandwidth_Object=MibTableColumn
cwdIfModBandwidth=_CwdIfModBandwidth_Object((1,3,6,1,4,1,9,9,167,1,1,7,1,3),_CwdIfModBandwidth_Type())
cwdIfModBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfModBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cwdIfModBandwidth.setUnits(_I)
class _CwdIfModThroughput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50000000))
_CwdIfModThroughput_Type.__name__=_D
_CwdIfModThroughput_Object=MibTableColumn
cwdIfModThroughput=_CwdIfModThroughput_Object((1,3,6,1,4,1,9,9,167,1,1,7,1,4),_CwdIfModThroughput_Type())
cwdIfModThroughput.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfModThroughput.setStatus(_A)
if mibBuilder.loadTexts:cwdIfModThroughput.setUnits('bps')
class _CwdIfModBurstLength_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('veryShort',1),('short',2),('medium',3),('long',4)))
_CwdIfModBurstLength_Type.__name__=_D
_CwdIfModBurstLength_Object=MibTableColumn
cwdIfModBurstLength=_CwdIfModBurstLength_Object((1,3,6,1,4,1,9,9,167,1,1,7,1,5),_CwdIfModBurstLength_Type())
cwdIfModBurstLength.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfModBurstLength.setStatus(_A)
class _CwdIfModMultipathRobustness_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('high',2)))
_CwdIfModMultipathRobustness_Type.__name__=_D
_CwdIfModMultipathRobustness_Object=MibTableColumn
cwdIfModMultipathRobustness=_CwdIfModMultipathRobustness_Object((1,3,6,1,4,1,9,9,167,1,1,7,1,6),_CwdIfModMultipathRobustness_Type())
cwdIfModMultipathRobustness.setMaxAccess(_F)
if mibBuilder.loadTexts:cwdIfModMultipathRobustness.setStatus(_A)
_CwdIfSuObjects_ObjectIdentity=ObjectIdentity
cwdIfSuObjects=_CwdIfSuObjects_ObjectIdentity((1,3,6,1,4,1,9,9,167,1,2))
_CwdIfSuMacTable_Object=MibTable
cwdIfSuMacTable=_CwdIfSuMacTable_Object((1,3,6,1,4,1,9,9,167,1,2,1))
if mibBuilder.loadTexts:cwdIfSuMacTable.setStatus(_A)
_CwdIfSuMacEntry_Object=MibTableRow
cwdIfSuMacEntry=_CwdIfSuMacEntry_Object((1,3,6,1,4,1,9,9,167,1,2,1,1))
cwdIfSuMacEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwdIfSuMacEntry.setStatus(_A)
_CwdIfSuHeAddress_Type=MacAddress
_CwdIfSuHeAddress_Object=MibTableColumn
cwdIfSuHeAddress=_CwdIfSuHeAddress_Object((1,3,6,1,4,1,9,9,167,1,2,1,1,1),_CwdIfSuHeAddress_Type())
cwdIfSuHeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuHeAddress.setStatus(_A)
class _CwdIfSuCapabilities_Type(Bits):namedValues=NamedValues(*((_Q,0),(_R,1)))
_CwdIfSuCapabilities_Type.__name__=_K
_CwdIfSuCapabilities_Object=MibTableColumn
cwdIfSuCapabilities=_CwdIfSuCapabilities_Object((1,3,6,1,4,1,9,9,167,1,2,1,1,2),_CwdIfSuCapabilities_Type())
cwdIfSuCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuCapabilities.setStatus(_A)
class _CwdIfSuRangingRespTimeout_Type(TimeInterval):defaultValue=20
_CwdIfSuRangingRespTimeout_Type.__name__=_M
_CwdIfSuRangingRespTimeout_Object=MibTableColumn
cwdIfSuRangingRespTimeout=_CwdIfSuRangingRespTimeout_Object((1,3,6,1,4,1,9,9,167,1,2,1,1,3),_CwdIfSuRangingRespTimeout_Type())
cwdIfSuRangingRespTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfSuRangingRespTimeout.setStatus(_A)
_CwdIfSuStatusTable_Object=MibTable
cwdIfSuStatusTable=_CwdIfSuStatusTable_Object((1,3,6,1,4,1,9,9,167,1,2,2))
if mibBuilder.loadTexts:cwdIfSuStatusTable.setStatus(_A)
_CwdIfSuStatusEntry_Object=MibTableRow
cwdIfSuStatusEntry=_CwdIfSuStatusEntry_Object((1,3,6,1,4,1,9,9,167,1,2,2,1))
cwdIfSuStatusEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwdIfSuStatusEntry.setStatus(_A)
class _CwdIfSuStatusValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('other',1),('notReady',2),('notSynchronized',3),('phySynchronized',4),('usParametersAcquired',5),(_S,6),(_T,7),('todEstablished',8),('securityEstablished',9),('paramTransferComplete',10),(_U,11),('operational',12),(_V,13)))
_CwdIfSuStatusValue_Type.__name__=_D
_CwdIfSuStatusValue_Object=MibTableColumn
cwdIfSuStatusValue=_CwdIfSuStatusValue_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,1),_CwdIfSuStatusValue_Type())
cwdIfSuStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusValue.setStatus(_A)
_CwdIfSuStatusCode_Type=OctetString
_CwdIfSuStatusCode_Object=MibTableColumn
cwdIfSuStatusCode=_CwdIfSuStatusCode_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,2),_CwdIfSuStatusCode_Type())
cwdIfSuStatusCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusCode.setStatus(_A)
class _CwdIfSuStatusTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-80,50))
_CwdIfSuStatusTxPower_Type.__name__=_D
_CwdIfSuStatusTxPower_Object=MibTableColumn
cwdIfSuStatusTxPower=_CwdIfSuStatusTxPower_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,3),_CwdIfSuStatusTxPower_Type())
cwdIfSuStatusTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusTxPower.setStatus(_A)
if mibBuilder.loadTexts:cwdIfSuStatusTxPower.setUnits(_L)
_CwdIfSuStatusResets_Type=Counter32
_CwdIfSuStatusResets_Object=MibTableColumn
cwdIfSuStatusResets=_CwdIfSuStatusResets_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,4),_CwdIfSuStatusResets_Type())
cwdIfSuStatusResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusResets.setStatus(_A)
_CwdIfSuStatusLostSyncs_Type=Counter32
_CwdIfSuStatusLostSyncs_Object=MibTableColumn
cwdIfSuStatusLostSyncs=_CwdIfSuStatusLostSyncs_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,5),_CwdIfSuStatusLostSyncs_Type())
cwdIfSuStatusLostSyncs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusLostSyncs.setStatus(_A)
_CwdIfSuStatusInvalidMaps_Type=Counter32
_CwdIfSuStatusInvalidMaps_Object=MibTableColumn
cwdIfSuStatusInvalidMaps=_CwdIfSuStatusInvalidMaps_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,6),_CwdIfSuStatusInvalidMaps_Type())
cwdIfSuStatusInvalidMaps.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusInvalidMaps.setStatus(_A)
_CwdIfSuStatusInvalidUcds_Type=Counter32
_CwdIfSuStatusInvalidUcds_Object=MibTableColumn
cwdIfSuStatusInvalidUcds=_CwdIfSuStatusInvalidUcds_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,7),_CwdIfSuStatusInvalidUcds_Type())
cwdIfSuStatusInvalidUcds.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusInvalidUcds.setStatus(_A)
_CwdIfSuStatusInvalidRangingResp_Type=Counter32
_CwdIfSuStatusInvalidRangingResp_Object=MibTableColumn
cwdIfSuStatusInvalidRangingResp=_CwdIfSuStatusInvalidRangingResp_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,8),_CwdIfSuStatusInvalidRangingResp_Type())
cwdIfSuStatusInvalidRangingResp.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusInvalidRangingResp.setStatus(_A)
_CwdIfSuStatusInvalidRegResp_Type=Counter32
_CwdIfSuStatusInvalidRegResp_Object=MibTableColumn
cwdIfSuStatusInvalidRegResp=_CwdIfSuStatusInvalidRegResp_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,9),_CwdIfSuStatusInvalidRegResp_Type())
cwdIfSuStatusInvalidRegResp.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusInvalidRegResp.setStatus(_A)
_CwdIfSuStatusT1Timeouts_Type=Counter32
_CwdIfSuStatusT1Timeouts_Object=MibTableColumn
cwdIfSuStatusT1Timeouts=_CwdIfSuStatusT1Timeouts_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,10),_CwdIfSuStatusT1Timeouts_Type())
cwdIfSuStatusT1Timeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusT1Timeouts.setStatus(_A)
_CwdIfSuStatusT2Timeouts_Type=Counter32
_CwdIfSuStatusT2Timeouts_Object=MibTableColumn
cwdIfSuStatusT2Timeouts=_CwdIfSuStatusT2Timeouts_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,11),_CwdIfSuStatusT2Timeouts_Type())
cwdIfSuStatusT2Timeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusT2Timeouts.setStatus(_A)
_CwdIfSuStatusT3Timeouts_Type=Counter32
_CwdIfSuStatusT3Timeouts_Object=MibTableColumn
cwdIfSuStatusT3Timeouts=_CwdIfSuStatusT3Timeouts_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,12),_CwdIfSuStatusT3Timeouts_Type())
cwdIfSuStatusT3Timeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusT3Timeouts.setStatus(_A)
_CwdIfSuStatusT4Timeouts_Type=Counter32
_CwdIfSuStatusT4Timeouts_Object=MibTableColumn
cwdIfSuStatusT4Timeouts=_CwdIfSuStatusT4Timeouts_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,13),_CwdIfSuStatusT4Timeouts_Type())
cwdIfSuStatusT4Timeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusT4Timeouts.setStatus(_A)
_CwdIfSuStatusRangingAborteds_Type=Counter32
_CwdIfSuStatusRangingAborteds_Object=MibTableColumn
cwdIfSuStatusRangingAborteds=_CwdIfSuStatusRangingAborteds_Object((1,3,6,1,4,1,9,9,167,1,2,2,1,14),_CwdIfSuStatusRangingAborteds_Type())
cwdIfSuStatusRangingAborteds.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuStatusRangingAborteds.setStatus(_A)
_CwdIfSuServiceTable_Object=MibTable
cwdIfSuServiceTable=_CwdIfSuServiceTable_Object((1,3,6,1,4,1,9,9,167,1,2,3))
if mibBuilder.loadTexts:cwdIfSuServiceTable.setStatus(_A)
_CwdIfSuServiceEntry_Object=MibTableRow
cwdIfSuServiceEntry=_CwdIfSuServiceEntry_Object((1,3,6,1,4,1,9,9,167,1,2,3,1))
cwdIfSuServiceEntry.setIndexNames((0,_G,_H),(0,_B,_W))
if mibBuilder.loadTexts:cwdIfSuServiceEntry.setStatus(_A)
class _CwdIfSuServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_CwdIfSuServiceId_Type.__name__=_D
_CwdIfSuServiceId_Object=MibTableColumn
cwdIfSuServiceId=_CwdIfSuServiceId_Object((1,3,6,1,4,1,9,9,167,1,2,3,1,1),_CwdIfSuServiceId_Type())
cwdIfSuServiceId.setMaxAccess(_J)
if mibBuilder.loadTexts:cwdIfSuServiceId.setStatus(_A)
class _CwdIfSuServiceQosProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_CwdIfSuServiceQosProfile_Type.__name__=_D
_CwdIfSuServiceQosProfile_Object=MibTableColumn
cwdIfSuServiceQosProfile=_CwdIfSuServiceQosProfile_Object((1,3,6,1,4,1,9,9,167,1,2,3,1,2),_CwdIfSuServiceQosProfile_Type())
cwdIfSuServiceQosProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuServiceQosProfile.setStatus(_A)
_CwdIfSuServiceTxSlotsImmed_Type=Counter32
_CwdIfSuServiceTxSlotsImmed_Object=MibTableColumn
cwdIfSuServiceTxSlotsImmed=_CwdIfSuServiceTxSlotsImmed_Object((1,3,6,1,4,1,9,9,167,1,2,3,1,3),_CwdIfSuServiceTxSlotsImmed_Type())
cwdIfSuServiceTxSlotsImmed.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuServiceTxSlotsImmed.setStatus(_A)
_CwdIfSuServiceTxSlotsDed_Type=Counter32
_CwdIfSuServiceTxSlotsDed_Object=MibTableColumn
cwdIfSuServiceTxSlotsDed=_CwdIfSuServiceTxSlotsDed_Object((1,3,6,1,4,1,9,9,167,1,2,3,1,4),_CwdIfSuServiceTxSlotsDed_Type())
cwdIfSuServiceTxSlotsDed.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuServiceTxSlotsDed.setStatus(_A)
_CwdIfSuServiceTxRetries_Type=Counter32
_CwdIfSuServiceTxRetries_Object=MibTableColumn
cwdIfSuServiceTxRetries=_CwdIfSuServiceTxRetries_Object((1,3,6,1,4,1,9,9,167,1,2,3,1,5),_CwdIfSuServiceTxRetries_Type())
cwdIfSuServiceTxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuServiceTxRetries.setStatus(_A)
_CwdIfSuServiceTxExceeded_Type=Counter32
_CwdIfSuServiceTxExceeded_Object=MibTableColumn
cwdIfSuServiceTxExceeded=_CwdIfSuServiceTxExceeded_Object((1,3,6,1,4,1,9,9,167,1,2,3,1,6),_CwdIfSuServiceTxExceeded_Type())
cwdIfSuServiceTxExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuServiceTxExceeded.setStatus(_A)
_CwdIfSuServiceRqRetries_Type=Counter32
_CwdIfSuServiceRqRetries_Object=MibTableColumn
cwdIfSuServiceRqRetries=_CwdIfSuServiceRqRetries_Object((1,3,6,1,4,1,9,9,167,1,2,3,1,7),_CwdIfSuServiceRqRetries_Type())
cwdIfSuServiceRqRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuServiceRqRetries.setStatus(_A)
_CwdIfSuServiceRqExceeded_Type=Counter32
_CwdIfSuServiceRqExceeded_Object=MibTableColumn
cwdIfSuServiceRqExceeded=_CwdIfSuServiceRqExceeded_Object((1,3,6,1,4,1,9,9,167,1,2,3,1,8),_CwdIfSuServiceRqExceeded_Type())
cwdIfSuServiceRqExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfSuServiceRqExceeded.setStatus(_A)
_CwdIfHeObjects_ObjectIdentity=ObjectIdentity
cwdIfHeObjects=_CwdIfHeObjects_ObjectIdentity((1,3,6,1,4,1,9,9,167,1,3))
_CwdIfHeMacTable_Object=MibTable
cwdIfHeMacTable=_CwdIfHeMacTable_Object((1,3,6,1,4,1,9,9,167,1,3,1))
if mibBuilder.loadTexts:cwdIfHeMacTable.setStatus(_A)
_CwdIfHeMacEntry_Object=MibTableRow
cwdIfHeMacEntry=_CwdIfHeMacEntry_Object((1,3,6,1,4,1,9,9,167,1,3,1,1))
cwdIfHeMacEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwdIfHeMacEntry.setStatus(_A)
class _CwdIfHeCapabilities_Type(Bits):namedValues=NamedValues(*((_Q,0),(_R,1)))
_CwdIfHeCapabilities_Type.__name__=_K
_CwdIfHeCapabilities_Object=MibTableColumn
cwdIfHeCapabilities=_CwdIfHeCapabilities_Object((1,3,6,1,4,1,9,9,167,1,3,1,1,1),_CwdIfHeCapabilities_Type())
cwdIfHeCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeCapabilities.setStatus(_A)
class _CwdIfHeSyncInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_CwdIfHeSyncInterval_Type.__name__=_D
_CwdIfHeSyncInterval_Object=MibTableColumn
cwdIfHeSyncInterval=_CwdIfHeSyncInterval_Object((1,3,6,1,4,1,9,9,167,1,3,1,1,2),_CwdIfHeSyncInterval_Type())
cwdIfHeSyncInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfHeSyncInterval.setStatus(_A)
if mibBuilder.loadTexts:cwdIfHeSyncInterval.setUnits(_X)
class _CwdIfHeUcdInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_CwdIfHeUcdInterval_Type.__name__=_D
_CwdIfHeUcdInterval_Object=MibTableColumn
cwdIfHeUcdInterval=_CwdIfHeUcdInterval_Object((1,3,6,1,4,1,9,9,167,1,3,1,1,3),_CwdIfHeUcdInterval_Type())
cwdIfHeUcdInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfHeUcdInterval.setStatus(_A)
if mibBuilder.loadTexts:cwdIfHeUcdInterval.setUnits(_X)
class _CwdIfHeMaxServiceIds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_CwdIfHeMaxServiceIds_Type.__name__=_D
_CwdIfHeMaxServiceIds_Object=MibTableColumn
cwdIfHeMaxServiceIds=_CwdIfHeMaxServiceIds_Object((1,3,6,1,4,1,9,9,167,1,3,1,1,4),_CwdIfHeMaxServiceIds_Type())
cwdIfHeMaxServiceIds.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeMaxServiceIds.setStatus(_A)
_CwdIfHeInsertionInterval_Type=TimeInterval
_CwdIfHeInsertionInterval_Object=MibTableColumn
cwdIfHeInsertionInterval=_CwdIfHeInsertionInterval_Object((1,3,6,1,4,1,9,9,167,1,3,1,1,5),_CwdIfHeInsertionInterval_Type())
cwdIfHeInsertionInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfHeInsertionInterval.setStatus(_A)
class _CwdIfHeInvitedRangingAttempts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CwdIfHeInvitedRangingAttempts_Type.__name__=_D
_CwdIfHeInvitedRangingAttempts_Object=MibTableColumn
cwdIfHeInvitedRangingAttempts=_CwdIfHeInvitedRangingAttempts_Object((1,3,6,1,4,1,9,9,167,1,3,1,1,6),_CwdIfHeInvitedRangingAttempts_Type())
cwdIfHeInvitedRangingAttempts.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfHeInvitedRangingAttempts.setStatus(_A)
_CwdIfHeStatusTable_Object=MibTable
cwdIfHeStatusTable=_CwdIfHeStatusTable_Object((1,3,6,1,4,1,9,9,167,1,3,2))
if mibBuilder.loadTexts:cwdIfHeStatusTable.setStatus(_A)
_CwdIfHeStatusEntry_Object=MibTableRow
cwdIfHeStatusEntry=_CwdIfHeStatusEntry_Object((1,3,6,1,4,1,9,9,167,1,3,2,1))
cwdIfHeStatusEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwdIfHeStatusEntry.setStatus(_A)
_CwdIfHeStatusInvalidRangeReqs_Type=Counter32
_CwdIfHeStatusInvalidRangeReqs_Object=MibTableColumn
cwdIfHeStatusInvalidRangeReqs=_CwdIfHeStatusInvalidRangeReqs_Object((1,3,6,1,4,1,9,9,167,1,3,2,1,1),_CwdIfHeStatusInvalidRangeReqs_Type())
cwdIfHeStatusInvalidRangeReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeStatusInvalidRangeReqs.setStatus(_A)
_CwdIfHeStatusRangingAborteds_Type=Counter32
_CwdIfHeStatusRangingAborteds_Object=MibTableColumn
cwdIfHeStatusRangingAborteds=_CwdIfHeStatusRangingAborteds_Object((1,3,6,1,4,1,9,9,167,1,3,2,1,2),_CwdIfHeStatusRangingAborteds_Type())
cwdIfHeStatusRangingAborteds.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeStatusRangingAborteds.setStatus(_A)
_CwdIfHeStatusInvalidRegReqs_Type=Counter32
_CwdIfHeStatusInvalidRegReqs_Object=MibTableColumn
cwdIfHeStatusInvalidRegReqs=_CwdIfHeStatusInvalidRegReqs_Object((1,3,6,1,4,1,9,9,167,1,3,2,1,3),_CwdIfHeStatusInvalidRegReqs_Type())
cwdIfHeStatusInvalidRegReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeStatusInvalidRegReqs.setStatus(_A)
_CwdIfHeStatusFailedRegReqs_Type=Counter32
_CwdIfHeStatusFailedRegReqs_Object=MibTableColumn
cwdIfHeStatusFailedRegReqs=_CwdIfHeStatusFailedRegReqs_Object((1,3,6,1,4,1,9,9,167,1,3,2,1,4),_CwdIfHeStatusFailedRegReqs_Type())
cwdIfHeStatusFailedRegReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeStatusFailedRegReqs.setStatus(_A)
_CwdIfHeStatusInvalidDataReqs_Type=Counter32
_CwdIfHeStatusInvalidDataReqs_Object=MibTableColumn
cwdIfHeStatusInvalidDataReqs=_CwdIfHeStatusInvalidDataReqs_Object((1,3,6,1,4,1,9,9,167,1,3,2,1,5),_CwdIfHeStatusInvalidDataReqs_Type())
cwdIfHeStatusInvalidDataReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeStatusInvalidDataReqs.setStatus(_A)
_CwdIfHeStatusT5Timeouts_Type=Counter32
_CwdIfHeStatusT5Timeouts_Object=MibTableColumn
cwdIfHeStatusT5Timeouts=_CwdIfHeStatusT5Timeouts_Object((1,3,6,1,4,1,9,9,167,1,3,2,1,6),_CwdIfHeStatusT5Timeouts_Type())
cwdIfHeStatusT5Timeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeStatusT5Timeouts.setStatus(_A)
_CwdIfHeSuStatusTable_Object=MibTable
cwdIfHeSuStatusTable=_CwdIfHeSuStatusTable_Object((1,3,6,1,4,1,9,9,167,1,3,3))
if mibBuilder.loadTexts:cwdIfHeSuStatusTable.setStatus(_A)
_CwdIfHeSuStatusEntry_Object=MibTableRow
cwdIfHeSuStatusEntry=_CwdIfHeSuStatusEntry_Object((1,3,6,1,4,1,9,9,167,1,3,3,1))
cwdIfHeSuStatusEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:cwdIfHeSuStatusEntry.setStatus(_A)
class _CwdIfHeSuStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwdIfHeSuStatusIndex_Type.__name__=_D
_CwdIfHeSuStatusIndex_Object=MibTableColumn
cwdIfHeSuStatusIndex=_CwdIfHeSuStatusIndex_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,1),_CwdIfHeSuStatusIndex_Type())
cwdIfHeSuStatusIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cwdIfHeSuStatusIndex.setStatus(_A)
_CwdIfHeSuStatusMacAddress_Type=MacAddress
_CwdIfHeSuStatusMacAddress_Object=MibTableColumn
cwdIfHeSuStatusMacAddress=_CwdIfHeSuStatusMacAddress_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,2),_CwdIfHeSuStatusMacAddress_Type())
cwdIfHeSuStatusMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusMacAddress.setStatus(_A)
_CwdIfHeSuStatusIpAddress_Type=IpAddress
_CwdIfHeSuStatusIpAddress_Object=MibTableColumn
cwdIfHeSuStatusIpAddress=_CwdIfHeSuStatusIpAddress_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,3),_CwdIfHeSuStatusIpAddress_Type())
cwdIfHeSuStatusIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusIpAddress.setStatus(_A)
_CwdIfHeSuStatusDownChanIfIndex_Type=InterfaceIndexOrZero
_CwdIfHeSuStatusDownChanIfIndex_Object=MibTableColumn
cwdIfHeSuStatusDownChanIfIndex=_CwdIfHeSuStatusDownChanIfIndex_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,4),_CwdIfHeSuStatusDownChanIfIndex_Type())
cwdIfHeSuStatusDownChanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusDownChanIfIndex.setStatus(_A)
_CwdIfHeSuStatusUpChanIfIndex_Type=InterfaceIndexOrZero
_CwdIfHeSuStatusUpChanIfIndex_Object=MibTableColumn
cwdIfHeSuStatusUpChanIfIndex=_CwdIfHeSuStatusUpChanIfIndex_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,5),_CwdIfHeSuStatusUpChanIfIndex_Type())
cwdIfHeSuStatusUpChanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusUpChanIfIndex.setStatus(_A)
class _CwdIfHeSuStatusRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-80,33))
_CwdIfHeSuStatusRxPower_Type.__name__=_D
_CwdIfHeSuStatusRxPower_Object=MibTableColumn
cwdIfHeSuStatusRxPower=_CwdIfHeSuStatusRxPower_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,6),_CwdIfHeSuStatusRxPower_Type())
cwdIfHeSuStatusRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusRxPower.setStatus(_A)
if mibBuilder.loadTexts:cwdIfHeSuStatusRxPower.setUnits('dBm Decibel milliwatts')
_CwdIfHeSuStatusTimingOffset_Type=Unsigned32
_CwdIfHeSuStatusTimingOffset_Object=MibTableColumn
cwdIfHeSuStatusTimingOffset=_CwdIfHeSuStatusTimingOffset_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,7),_CwdIfHeSuStatusTimingOffset_Type())
cwdIfHeSuStatusTimingOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusTimingOffset.setStatus(_A)
class _CwdIfHeSuStatusValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('ranging',2),('rangingAborted',3),(_S,4),(_T,5),(_U,6),(_V,7)))
_CwdIfHeSuStatusValue_Type.__name__=_D
_CwdIfHeSuStatusValue_Object=MibTableColumn
cwdIfHeSuStatusValue=_CwdIfHeSuStatusValue_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,8),_CwdIfHeSuStatusValue_Type())
cwdIfHeSuStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusValue.setStatus(_A)
_CwdIfHeSuStatusIfIndex_Type=InterfaceIndex
_CwdIfHeSuStatusIfIndex_Object=MibTableColumn
cwdIfHeSuStatusIfIndex=_CwdIfHeSuStatusIfIndex_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,9),_CwdIfHeSuStatusIfIndex_Type())
cwdIfHeSuStatusIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusIfIndex.setStatus(_A)
class _CwdIfHeSuStatusServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_CwdIfHeSuStatusServiceId_Type.__name__=_D
_CwdIfHeSuStatusServiceId_Object=MibTableColumn
cwdIfHeSuStatusServiceId=_CwdIfHeSuStatusServiceId_Object((1,3,6,1,4,1,9,9,167,1,3,3,1,10),_CwdIfHeSuStatusServiceId_Type())
cwdIfHeSuStatusServiceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeSuStatusServiceId.setStatus(_A)
_CwdIfHeServiceTable_Object=MibTable
cwdIfHeServiceTable=_CwdIfHeServiceTable_Object((1,3,6,1,4,1,9,9,167,1,3,4))
if mibBuilder.loadTexts:cwdIfHeServiceTable.setStatus(_A)
_CwdIfHeServiceEntry_Object=MibTableRow
cwdIfHeServiceEntry=_CwdIfHeServiceEntry_Object((1,3,6,1,4,1,9,9,167,1,3,4,1))
cwdIfHeServiceEntry.setIndexNames((0,_G,_H),(0,_B,_Z))
if mibBuilder.loadTexts:cwdIfHeServiceEntry.setStatus(_A)
class _CwdIfHeServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_CwdIfHeServiceId_Type.__name__=_D
_CwdIfHeServiceId_Object=MibTableColumn
cwdIfHeServiceId=_CwdIfHeServiceId_Object((1,3,6,1,4,1,9,9,167,1,3,4,1,1),_CwdIfHeServiceId_Type())
cwdIfHeServiceId.setMaxAccess(_J)
if mibBuilder.loadTexts:cwdIfHeServiceId.setStatus(_A)
class _CwdIfHeServiceSuStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwdIfHeServiceSuStatusIndex_Type.__name__=_D
_CwdIfHeServiceSuStatusIndex_Object=MibTableColumn
cwdIfHeServiceSuStatusIndex=_CwdIfHeServiceSuStatusIndex_Object((1,3,6,1,4,1,9,9,167,1,3,4,1,2),_CwdIfHeServiceSuStatusIndex_Type())
cwdIfHeServiceSuStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeServiceSuStatusIndex.setStatus(_A)
class _CwdIfHeServiceAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('destroyed',3)))
_CwdIfHeServiceAdminStatus_Type.__name__=_D
_CwdIfHeServiceAdminStatus_Object=MibTableColumn
cwdIfHeServiceAdminStatus=_CwdIfHeServiceAdminStatus_Object((1,3,6,1,4,1,9,9,167,1,3,4,1,3),_CwdIfHeServiceAdminStatus_Type())
cwdIfHeServiceAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfHeServiceAdminStatus.setStatus(_A)
class _CwdIfHeServiceQosProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_CwdIfHeServiceQosProfile_Type.__name__=_D
_CwdIfHeServiceQosProfile_Object=MibTableColumn
cwdIfHeServiceQosProfile=_CwdIfHeServiceQosProfile_Object((1,3,6,1,4,1,9,9,167,1,3,4,1,4),_CwdIfHeServiceQosProfile_Type())
cwdIfHeServiceQosProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeServiceQosProfile.setStatus(_A)
_CwdIfHeServiceCreateTime_Type=TimeStamp
_CwdIfHeServiceCreateTime_Object=MibTableColumn
cwdIfHeServiceCreateTime=_CwdIfHeServiceCreateTime_Object((1,3,6,1,4,1,9,9,167,1,3,4,1,5),_CwdIfHeServiceCreateTime_Type())
cwdIfHeServiceCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeServiceCreateTime.setStatus(_A)
_CwdIfHeServiceInOctets_Type=Counter32
_CwdIfHeServiceInOctets_Object=MibTableColumn
cwdIfHeServiceInOctets=_CwdIfHeServiceInOctets_Object((1,3,6,1,4,1,9,9,167,1,3,4,1,6),_CwdIfHeServiceInOctets_Type())
cwdIfHeServiceInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeServiceInOctets.setStatus(_A)
_CwdIfHeServiceInPackets_Type=Counter32
_CwdIfHeServiceInPackets_Object=MibTableColumn
cwdIfHeServiceInPackets=_CwdIfHeServiceInPackets_Object((1,3,6,1,4,1,9,9,167,1,3,4,1,7),_CwdIfHeServiceInPackets_Type())
cwdIfHeServiceInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cwdIfHeServiceInPackets.setStatus(_A)
class _CwdIfHeQosProfilePermissions_Type(Bits):namedValues=NamedValues(*(('createByManagement',0),('updateByManagement',1),('createBySubscriberUnits',2)))
_CwdIfHeQosProfilePermissions_Type.__name__=_K
_CwdIfHeQosProfilePermissions_Object=MibScalar
cwdIfHeQosProfilePermissions=_CwdIfHeQosProfilePermissions_Object((1,3,6,1,4,1,9,9,167,1,3,6),_CwdIfHeQosProfilePermissions_Type())
cwdIfHeQosProfilePermissions.setMaxAccess(_E)
if mibBuilder.loadTexts:cwdIfHeQosProfilePermissions.setStatus(_A)
_CwdIfNotification_ObjectIdentity=ObjectIdentity
cwdIfNotification=_CwdIfNotification_ObjectIdentity((1,3,6,1,4,1,9,9,167,2))
_CwdIfConformance_ObjectIdentity=ObjectIdentity
cwdIfConformance=_CwdIfConformance_ObjectIdentity((1,3,6,1,4,1,9,9,167,3))
_CwdIfCompliances_ObjectIdentity=ObjectIdentity
cwdIfCompliances=_CwdIfCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,167,3,1))
_CwdIfGroups_ObjectIdentity=ObjectIdentity
cwdIfGroups=_CwdIfGroups_ObjectIdentity((1,3,6,1,4,1,9,9,167,3,2))
cwdIfBasicGroup=ObjectGroup((1,3,6,1,4,1,9,9,167,3,2,1))
cwdIfBasicGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:cwdIfBasicGroup.setStatus(_A)
cwdIfSuGroup=ObjectGroup((1,3,6,1,4,1,9,9,167,3,2,2))
cwdIfSuGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:cwdIfSuGroup.setStatus(_A)
cwdIfQosGroup=ObjectGroup((1,3,6,1,4,1,9,9,167,3,2,3))
cwdIfQosGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:cwdIfQosGroup.setStatus(_A)
cwdIfQosHeGroup=ObjectGroup((1,3,6,1,4,1,9,9,167,3,2,4))
cwdIfQosHeGroup.setObjects((_B,_AY))
if mibBuilder.loadTexts:cwdIfQosHeGroup.setStatus(_A)
cwdIfModGroup=ObjectGroup((1,3,6,1,4,1,9,9,167,3,2,5))
cwdIfModGroup.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:cwdIfModGroup.setStatus(_A)
cwdIfHeGroup=ObjectGroup((1,3,6,1,4,1,9,9,167,3,2,7))
cwdIfHeGroup.setObjects(*((_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:cwdIfHeGroup.setStatus(_A)
cwdIfBasicCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,167,3,1,2))
cwdIfBasicCompliance.setObjects(*((_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9)))
if mibBuilder.loadTexts:cwdIfBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWirelessDocsIfMib':ciscoWirelessDocsIfMib,'cwdIfMibObjects':cwdIfMibObjects,'cwdIfBaseObjects':cwdIfBaseObjects,'cwdIfChannelTable':cwdIfChannelTable,'cwdIfChannelEntry':cwdIfChannelEntry,_a:cwdIfChannelUpFrequency,_b:cwdIfChannelUpWidth,_c:cwdIfChannelDownFrequency,_d:cwdIfChannelDownWidth,_e:cwdIfChannelMiniSlotTimeBaseTick,_f:cwdIfChannelSubChannelPlanVer,'cwdIfDownstreamChannelTable':cwdIfDownstreamChannelTable,'cwdIfDownstreamChannelEntry':cwdIfDownstreamChannelEntry,_g:cwdIfDownChannelSubChannelNumber,_h:cwdIfDownChannelId,_i:cwdIfDownChannelFrequency,_j:cwdIfDownChannelWidth,_k:cwdIfDownChannelPower,_l:cwdIfDownChannelModProfileIndex,'cwdIfUpstreamChannelTable':cwdIfUpstreamChannelTable,'cwdIfUpstreamChannelEntry':cwdIfUpstreamChannelEntry,_m:cwdIfUpChannelSubChannelNumber,_n:cwdIfUpChannelId,_o:cwdIfUpChannelFrequency,_p:cwdIfUpChannelWidth,_q:cwdIfUpChannelTargetPower,_r:cwdIfUpChannelModProfileIndex,_s:cwdIfUpChannelSlotSize,_t:cwdIfUpChannelTxTimingOffset,_u:cwdIfUpChannelRangBackoffStart,_v:cwdIfUpChannelRangBackoffEnd,_w:cwdIfUpChannelTxBackoffStart,_x:cwdIfUpChannelTxBackoffEnd,'cwdIfQosProfileTable':cwdIfQosProfileTable,'cwdIfQosProfileEntry':cwdIfQosProfileEntry,_O:cwdIfQosProfIndex,_AR:cwdIfQosProfPriority,_AS:cwdIfQosProfMaxUpBandwidth,_AT:cwdIfQosProfGuarUpBandwidth,_AU:cwdIfQosProfMaxDownBandwidth,_AV:cwdIfQosProfMaxTxBurst,_AW:cwdIfQosProfBaselinePrivacy,_AX:cwdIfQosProfStatus,'cwdIfSignalQualityTable':cwdIfSignalQualityTable,'cwdIfSignalQualityEntry':cwdIfSignalQualityEntry,_y:cwdIfSigQIncludesContention,_z:cwdIfSigQUnerroreds,_A0:cwdIfSigQCorrecteds,_A1:cwdIfSigQUncorrectables,_A2:cwdIfSigQSignalNoise,'cwdIfModulationTable':cwdIfModulationTable,'cwdIfModulationEntry':cwdIfModulationEntry,_P:cwdIfModIndex,_AZ:cwdIfModRowStatus,_Aa:cwdIfModBandwidth,_Ab:cwdIfModThroughput,_Ac:cwdIfModBurstLength,_Ad:cwdIfModMultipathRobustness,'cwdIfSuObjects':cwdIfSuObjects,'cwdIfSuMacTable':cwdIfSuMacTable,'cwdIfSuMacEntry':cwdIfSuMacEntry,_A3:cwdIfSuHeAddress,_A4:cwdIfSuCapabilities,_A5:cwdIfSuRangingRespTimeout,'cwdIfSuStatusTable':cwdIfSuStatusTable,'cwdIfSuStatusEntry':cwdIfSuStatusEntry,_A6:cwdIfSuStatusValue,_A7:cwdIfSuStatusCode,_A8:cwdIfSuStatusTxPower,_A9:cwdIfSuStatusResets,_AA:cwdIfSuStatusLostSyncs,_AB:cwdIfSuStatusInvalidMaps,_AC:cwdIfSuStatusInvalidUcds,_AD:cwdIfSuStatusInvalidRangingResp,_AE:cwdIfSuStatusInvalidRegResp,_AF:cwdIfSuStatusT1Timeouts,_AG:cwdIfSuStatusT2Timeouts,_AH:cwdIfSuStatusT3Timeouts,_AI:cwdIfSuStatusT4Timeouts,_AJ:cwdIfSuStatusRangingAborteds,'cwdIfSuServiceTable':cwdIfSuServiceTable,'cwdIfSuServiceEntry':cwdIfSuServiceEntry,_W:cwdIfSuServiceId,_AK:cwdIfSuServiceQosProfile,_AL:cwdIfSuServiceTxSlotsImmed,_AM:cwdIfSuServiceTxSlotsDed,_AN:cwdIfSuServiceTxRetries,_AO:cwdIfSuServiceTxExceeded,_AP:cwdIfSuServiceRqRetries,_AQ:cwdIfSuServiceRqExceeded,'cwdIfHeObjects':cwdIfHeObjects,'cwdIfHeMacTable':cwdIfHeMacTable,'cwdIfHeMacEntry':cwdIfHeMacEntry,_Ae:cwdIfHeCapabilities,_Af:cwdIfHeSyncInterval,_Ag:cwdIfHeUcdInterval,_Ah:cwdIfHeMaxServiceIds,_Ai:cwdIfHeInsertionInterval,_Aj:cwdIfHeInvitedRangingAttempts,'cwdIfHeStatusTable':cwdIfHeStatusTable,'cwdIfHeStatusEntry':cwdIfHeStatusEntry,_Ak:cwdIfHeStatusInvalidRangeReqs,_Al:cwdIfHeStatusRangingAborteds,_Am:cwdIfHeStatusInvalidRegReqs,_An:cwdIfHeStatusFailedRegReqs,_Ao:cwdIfHeStatusInvalidDataReqs,_Ap:cwdIfHeStatusT5Timeouts,'cwdIfHeSuStatusTable':cwdIfHeSuStatusTable,'cwdIfHeSuStatusEntry':cwdIfHeSuStatusEntry,_Y:cwdIfHeSuStatusIndex,_Aq:cwdIfHeSuStatusMacAddress,_Ar:cwdIfHeSuStatusIpAddress,_As:cwdIfHeSuStatusDownChanIfIndex,_At:cwdIfHeSuStatusUpChanIfIndex,_Au:cwdIfHeSuStatusRxPower,_Av:cwdIfHeSuStatusTimingOffset,_Aw:cwdIfHeSuStatusValue,_Ax:cwdIfHeSuStatusIfIndex,_Ay:cwdIfHeSuStatusServiceId,'cwdIfHeServiceTable':cwdIfHeServiceTable,'cwdIfHeServiceEntry':cwdIfHeServiceEntry,_Z:cwdIfHeServiceId,_Az:cwdIfHeServiceSuStatusIndex,_A_:cwdIfHeServiceAdminStatus,_B0:cwdIfHeServiceQosProfile,_B1:cwdIfHeServiceCreateTime,_B2:cwdIfHeServiceInOctets,_B3:cwdIfHeServiceInPackets,_AY:cwdIfHeQosProfilePermissions,'cwdIfNotification':cwdIfNotification,'cwdIfConformance':cwdIfConformance,'cwdIfCompliances':cwdIfCompliances,'cwdIfBasicCompliance':cwdIfBasicCompliance,'cwdIfGroups':cwdIfGroups,_B4:cwdIfBasicGroup,_B5:cwdIfSuGroup,_B7:cwdIfQosGroup,_B8:cwdIfQosHeGroup,_B9:cwdIfModGroup,_B6:cwdIfHeGroup})