_Bd='cdspTranscodeProfileGroup'
_Bc='cdspConferenceProfileGroup'
_Bb='cdspMtpProfileGroup'
_Ba='cdspTransCodingGroup'
_BZ='cdspVoiceInfoGroup'
_BY='cdspVideoOutOfResourceNotification'
_BX='cdspVideoUsageNotification'
_BW='cdspOperStateNotification'
_BV='cdspConferenceProfileRowStatus'
_BU='cdspConferenceProfileStorageType'
_BT='cdspConferenceProfileMaxAvailSess'
_BS='cdspConferenceProfileMaxConfSess'
_BR='cdspConferenceProfileMaxCodec'
_BQ='cdspConferenceApplicationStatus'
_BP='cdspConferenceApplication'
_BO='cdspConferenceAdminState'
_BN='cdspConferenceService'
_BM='cdspConferenceDescription'
_BL='cdspConferenceResourceId'
_BK='cdspMtpProfileMaxAvailSoftSess'
_BJ='cdspMtpProfileMaxCodec'
_BI='cdspMtpApplicationStatus'
_BH='cdspMtpApplication'
_BG='cdspMtpAdminState'
_BF='cdspMtpService'
_BE='cdspMtpDescription'
_BD='cdspMtpResourceId'
_BC='cdspTranscodeApplication'
_BB='cdspTranscodeAdminState'
_BA='cdspTranscodeService'
_B9='cdspTranscodeDescription'
_B8='cdspTranscodeResourceId'
_B7='cdspVideoOutOfResourceNotificationEnable'
_B6='cdspVideoUsageNotificationEnable'
_B5='cdspTotUnusedMtpSess'
_B4='cdspTotAvailMtpSess'
_B3='cdspTotUnusedTranscodeSess'
_B2='cdspTotAvailTranscodeSess'
_B1='cdspMtpProfileMaxAvailHardSess'
_B0='cdspMtpProfileMaxConfHardSess'
_A_='cdspMtpProfileMaxConfSoftSess'
_Az='cdspMtpProfileRowStatus'
_Ay='cdspTranscodeProfileMaxAvailSess'
_Ax='cdspTranscodeProfileMaxConfSess'
_Aw='cdspTranscodeProfileRowStatus'
_Av='cdspGlobMaxAvailTranscodeSess'
_Au='cdspGlobMaxConfTranscodeSess'
_At='cdspCurrentAvlbCap'
_As='cdspCurrentUtilCap'
_Ar='cdspVoiceModeIpIp'
_Aq='cdspTransparentIpIp'
_Ap='cdspPktLossConcealment'
_Ao='cdspVqmThreshSES'
_An='cdspRtcpXrExtRfactor'
_Am='cdspRtcpXrGminDefault'
_Al='cdspRtcpXrTransMultiplier'
_Ak='cdspRtcpXrControl'
_Aj='cdspVqmControl'
_Ai='cdspEnableOperStateNotification'
_Ah='cdspCodecTemplateSupported'
_Ag='cdspXAvailableSigBandwidth'
_Af='cdspXAvailableBearerBandwidth'
_Ae='cdspXNumberOfSigCalls'
_Ad='cdspXNumberOfBearerCalls'
_Ac='cdspNumCongestionOccurrence'
_Ab='cdspSigBearerChannelSplit'
_Aa='cdspActiveChannels'
_AZ='cdspInUseChannels'
_AY='cdspTotalChannels'
_AX='cdspCardMaxChanPerDSP'
_AW='cdspStatusXEntry'
_AV='cdspConferenceProfileId'
_AU='cdspMtpProfileId'
_AT='cdspTranscodeProfileId'
_AS='cdspCodecPoolIndex'
_AR='milliseconds'
_AQ='StorageType'
_AP='entPhysicalName'
_AO='cdspMgmtVideoNotificationsGroup'
_AN='cdspMgmtVideoInfoGroup'
_AM='cdspMgmtExtGeneralInfoGroup'
_AL='cdspMgmtNotificationsGroup'
_AK='cdspMIBCardStateNotification'
_AJ='cdspTranscodeProfileMaxCodec'
_AI='cdspRtcpTimerControl'
_AH='cdspDspNum'
_AG='cdspNx64Dsp'
_AF='cdspDspSwitchOverThreshold'
_AE='cdspNormalDsp'
_AD='cdspCongestedDsp'
_AC='cdspFailedDsp'
_AB='cdspTotalDsp'
_AA='cdspMIBEnableCardStatusNotification'
_A9='cdspLastAlarmTime'
_A8='cdspLastAlarmCauseText'
_A7='cdspLastAlarmCause'
_A6='cdspAlarms'
_A5='cdspCardLastResetTime'
_A4='cdspCardLastHiWaterUtilization'
_A3='cdspCardResourceUtilization'
_A2='cdspCardIndex'
_A1='invalid'
_A0='notDone'
_z='activeInDown'
_y='activeInProgress'
_x='done'
_w='cube'
_v='sbc'
_u='sccp'
_t='down'
_s='secure'
_r='nonSecure'
_q='codecs'
_p='normal'
_o='cdspDspfarmInfoGroup'
_n='cdspVoiceInfoGroupRev1'
_m='cdspCardVideoPoolUtilizationThreshold'
_l='cdspCardVideoPoolUtilization'
_k='cdspDtmfPowerTwist'
_j='cdspDtmfPowerLevel'
_i='cdspVadAdaptive'
_h='cdspRtcpRecvMultiplier'
_g='cdspRtcpTransInterval'
_f='cdspRtcpControl'
_e='cdspRtpSidPayloadType'
_d='cdspOperState'
_c='cdspCardState'
_b='not-accessible'
_a='other'
_Z='channels'
_Y='percent'
_X='Gauge32'
_W='cdspUtilInfoGroup'
_V='cdspMgmtGeneralInfoGroup'
_U='sessions'
_T='entPhysicalIndex'
_S='cdspTransCodingGroup1'
_R='ENTITY-MIB'
_Q='none'
_P='TruthValue'
_O='cdspVoiceInfoGroupRev2'
_N='cdspVQMGroup'
_M='cdspMgmtNotificationsGroupRev1'
_L='cdspMgmtGeneralInfoGroupRev1'
_K='cdspMgmtExtGeneralInfoGroupRev1'
_J='read-create'
_I='cdspChannelExtGroup'
_H='cdspChannelGroup'
_G='deprecated'
_F='Integer32'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-DSP-MGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percent,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','Percent')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_R,_T,_AP)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_X,_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_AQ,'TextualConvention','TimeStamp',_P)
ciscoDspMgmtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,86))
if mibBuilder.loadTexts:ciscoDspMgmtMIB.setRevisions(('2015-03-16 00:00','2011-02-17 00:00','2009-04-09 00:00','2007-09-03 00:05','2007-06-25 00:00','2007-06-20 00:00','2006-04-14 00:00','2005-11-02 00:00','2005-08-17 00:00','2005-08-04 00:00','2005-06-20 00:00','2005-05-18 00:00','2005-04-18 00:00','2004-10-21 00:00','2003-10-10 00:00','2003-08-20 00:00','2003-08-14 00:00','2000-08-14 00:00','1998-10-17 00:00'))
_CdspMgmtNotifications_ObjectIdentity=ObjectIdentity
cdspMgmtNotifications=_CdspMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,86,0))
_CdspMgmtObjects_ObjectIdentity=ObjectIdentity
cdspMgmtObjects=_CdspMgmtObjects_ObjectIdentity((1,3,6,1,4,1,9,9,86,1))
_CdspCardObjects_ObjectIdentity=ObjectIdentity
cdspCardObjects=_CdspCardObjects_ObjectIdentity((1,3,6,1,4,1,9,9,86,1,1))
_CdspCardStatusTable_Object=MibTable
cdspCardStatusTable=_CdspCardStatusTable_Object((1,3,6,1,4,1,9,9,86,1,1,1))
if mibBuilder.loadTexts:cdspCardStatusTable.setStatus(_B)
_CdspCardStatusEntry_Object=MibTableRow
cdspCardStatusEntry=_CdspCardStatusEntry_Object((1,3,6,1,4,1,9,9,86,1,1,1,1))
cdspCardStatusEntry.setIndexNames((0,_R,_T))
if mibBuilder.loadTexts:cdspCardStatusEntry.setStatus(_B)
_CdspCardIndex_Type=Integer32
_CdspCardIndex_Object=MibTableColumn
cdspCardIndex=_CdspCardIndex_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,1),_CdspCardIndex_Type())
cdspCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCardIndex.setStatus(_B)
class _CdspCardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_p,1),('warning',2),('critical',3),('fatal',4),('offLine',5)))
_CdspCardState_Type.__name__=_F
_CdspCardState_Object=MibTableColumn
cdspCardState=_CdspCardState_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,2),_CdspCardState_Type())
cdspCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCardState.setStatus(_B)
class _CdspCardResourceUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CdspCardResourceUtilization_Type.__name__=_D
_CdspCardResourceUtilization_Object=MibTableColumn
cdspCardResourceUtilization=_CdspCardResourceUtilization_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,3),_CdspCardResourceUtilization_Type())
cdspCardResourceUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCardResourceUtilization.setStatus(_B)
if mibBuilder.loadTexts:cdspCardResourceUtilization.setUnits(_Y)
class _CdspCardLastHiWaterUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CdspCardLastHiWaterUtilization_Type.__name__=_D
_CdspCardLastHiWaterUtilization_Object=MibTableColumn
cdspCardLastHiWaterUtilization=_CdspCardLastHiWaterUtilization_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,4),_CdspCardLastHiWaterUtilization_Type())
cdspCardLastHiWaterUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCardLastHiWaterUtilization.setStatus(_B)
if mibBuilder.loadTexts:cdspCardLastHiWaterUtilization.setUnits(_Y)
_CdspCardLastResetTime_Type=TimeStamp
_CdspCardLastResetTime_Object=MibTableColumn
cdspCardLastResetTime=_CdspCardLastResetTime_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,5),_CdspCardLastResetTime_Type())
cdspCardLastResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCardLastResetTime.setStatus(_B)
_CdspCardMaxChanPerDSP_Type=Unsigned32
_CdspCardMaxChanPerDSP_Object=MibTableColumn
cdspCardMaxChanPerDSP=_CdspCardMaxChanPerDSP_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,6),_CdspCardMaxChanPerDSP_Type())
cdspCardMaxChanPerDSP.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCardMaxChanPerDSP.setStatus(_B)
if mibBuilder.loadTexts:cdspCardMaxChanPerDSP.setUnits(_Z)
class _CdspTotalDsp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CdspTotalDsp_Type.__name__=_D
_CdspTotalDsp_Object=MibTableColumn
cdspTotalDsp=_CdspTotalDsp_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,7),_CdspTotalDsp_Type())
cdspTotalDsp.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTotalDsp.setStatus(_B)
class _CdspFailedDsp_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CdspFailedDsp_Type.__name__=_X
_CdspFailedDsp_Object=MibTableColumn
cdspFailedDsp=_CdspFailedDsp_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,8),_CdspFailedDsp_Type())
cdspFailedDsp.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspFailedDsp.setStatus(_B)
class _CdspDspSwitchOverThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CdspDspSwitchOverThreshold_Type.__name__=_D
_CdspDspSwitchOverThreshold_Object=MibTableColumn
cdspDspSwitchOverThreshold=_CdspDspSwitchOverThreshold_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,9),_CdspDspSwitchOverThreshold_Type())
cdspDspSwitchOverThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspDspSwitchOverThreshold.setStatus(_B)
class _CdspCongestedDsp_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CdspCongestedDsp_Type.__name__=_X
_CdspCongestedDsp_Object=MibTableColumn
cdspCongestedDsp=_CdspCongestedDsp_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,10),_CdspCongestedDsp_Type())
cdspCongestedDsp.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCongestedDsp.setStatus(_B)
class _CdspNormalDsp_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CdspNormalDsp_Type.__name__=_X
_CdspNormalDsp_Object=MibTableColumn
cdspNormalDsp=_CdspNormalDsp_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,11),_CdspNormalDsp_Type())
cdspNormalDsp.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspNormalDsp.setStatus(_B)
class _CdspNx64Dsp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CdspNx64Dsp_Type.__name__=_D
_CdspNx64Dsp_Object=MibTableColumn
cdspNx64Dsp=_CdspNx64Dsp_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,12),_CdspNx64Dsp_Type())
cdspNx64Dsp.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspNx64Dsp.setStatus(_B)
class _CdspCodecTemplateSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('tgw',1),('cable',2),('umts3G',3),('cdma3G',4),('tgw2',5),('fmc',6)))
_CdspCodecTemplateSupported_Type.__name__=_F
_CdspCodecTemplateSupported_Object=MibTableColumn
cdspCodecTemplateSupported=_CdspCodecTemplateSupported_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,13),_CdspCodecTemplateSupported_Type())
cdspCodecTemplateSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCodecTemplateSupported.setStatus(_B)
_CdspCardVideoPoolUtilization_Type=Percent
_CdspCardVideoPoolUtilization_Object=MibTableColumn
cdspCardVideoPoolUtilization=_CdspCardVideoPoolUtilization_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,14),_CdspCardVideoPoolUtilization_Type())
cdspCardVideoPoolUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCardVideoPoolUtilization.setStatus(_B)
class _CdspCardVideoPoolUtilizationThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CdspCardVideoPoolUtilizationThreshold_Type.__name__=_D
_CdspCardVideoPoolUtilizationThreshold_Object=MibTableColumn
cdspCardVideoPoolUtilizationThreshold=_CdspCardVideoPoolUtilizationThreshold_Object((1,3,6,1,4,1,9,9,86,1,1,1,1,15),_CdspCardVideoPoolUtilizationThreshold_Type())
cdspCardVideoPoolUtilizationThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspCardVideoPoolUtilizationThreshold.setStatus(_B)
_CdspObjects_ObjectIdentity=ObjectIdentity
cdspObjects=_CdspObjects_ObjectIdentity((1,3,6,1,4,1,9,9,86,1,2))
_CdspStatusTable_Object=MibTable
cdspStatusTable=_CdspStatusTable_Object((1,3,6,1,4,1,9,9,86,1,2,1))
if mibBuilder.loadTexts:cdspStatusTable.setStatus(_B)
_CdspStatusEntry_Object=MibTableRow
cdspStatusEntry=_CdspStatusEntry_Object((1,3,6,1,4,1,9,9,86,1,2,1,1))
cdspStatusEntry.setIndexNames((0,_R,_T))
if mibBuilder.loadTexts:cdspStatusEntry.setStatus(_B)
class _CdspOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_p,1),('shutdown',2),('congested',3),('failed',4)))
_CdspOperState_Type.__name__=_F
_CdspOperState_Object=MibTableColumn
cdspOperState=_CdspOperState_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,1),_CdspOperState_Type())
cdspOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspOperState.setStatus(_B)
_CdspAlarms_Type=Counter32
_CdspAlarms_Object=MibTableColumn
cdspAlarms=_CdspAlarms_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,2),_CdspAlarms_Type())
cdspAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspAlarms.setStatus(_B)
class _CdspLastAlarmCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_a,1),('noAlarm',2),('dspFatalError',3),('dspMemoryError',4),('dspBufferError',5),('dspDownloadError',6)))
_CdspLastAlarmCause_Type.__name__=_F
_CdspLastAlarmCause_Object=MibTableColumn
cdspLastAlarmCause=_CdspLastAlarmCause_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,3),_CdspLastAlarmCause_Type())
cdspLastAlarmCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspLastAlarmCause.setStatus(_B)
_CdspLastAlarmCauseText_Type=DisplayString
_CdspLastAlarmCauseText_Object=MibTableColumn
cdspLastAlarmCauseText=_CdspLastAlarmCauseText_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,4),_CdspLastAlarmCauseText_Type())
cdspLastAlarmCauseText.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspLastAlarmCauseText.setStatus(_B)
_CdspLastAlarmTime_Type=TimeStamp
_CdspLastAlarmTime_Object=MibTableColumn
cdspLastAlarmTime=_CdspLastAlarmTime_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,5),_CdspLastAlarmTime_Type())
cdspLastAlarmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspLastAlarmTime.setStatus(_B)
_CdspTotalChannels_Type=Unsigned32
_CdspTotalChannels_Object=MibTableColumn
cdspTotalChannels=_CdspTotalChannels_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,6),_CdspTotalChannels_Type())
cdspTotalChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTotalChannels.setStatus(_B)
if mibBuilder.loadTexts:cdspTotalChannels.setUnits(_Z)
_CdspInUseChannels_Type=Gauge32
_CdspInUseChannels_Object=MibTableColumn
cdspInUseChannels=_CdspInUseChannels_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,7),_CdspInUseChannels_Type())
cdspInUseChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspInUseChannels.setStatus(_B)
if mibBuilder.loadTexts:cdspInUseChannels.setUnits(_Z)
_CdspActiveChannels_Type=Gauge32
_CdspActiveChannels_Object=MibTableColumn
cdspActiveChannels=_CdspActiveChannels_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,8),_CdspActiveChannels_Type())
cdspActiveChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspActiveChannels.setStatus(_B)
if mibBuilder.loadTexts:cdspActiveChannels.setUnits(_Z)
_CdspSigBearerChannelSplit_Type=TruthValue
_CdspSigBearerChannelSplit_Object=MibTableColumn
cdspSigBearerChannelSplit=_CdspSigBearerChannelSplit_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,9),_CdspSigBearerChannelSplit_Type())
cdspSigBearerChannelSplit.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspSigBearerChannelSplit.setStatus(_B)
_CdspNumCongestionOccurrence_Type=Counter32
_CdspNumCongestionOccurrence_Object=MibTableColumn
cdspNumCongestionOccurrence=_CdspNumCongestionOccurrence_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,10),_CdspNumCongestionOccurrence_Type())
cdspNumCongestionOccurrence.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspNumCongestionOccurrence.setStatus(_B)
class _CdspDspNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,252))
_CdspDspNum_Type.__name__=_D
_CdspDspNum_Object=MibTableColumn
cdspDspNum=_CdspDspNum_Object((1,3,6,1,4,1,9,9,86,1,2,1,1,11),_CdspDspNum_Type())
cdspDspNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspDspNum.setStatus(_B)
_CdspStatusXTable_Object=MibTable
cdspStatusXTable=_CdspStatusXTable_Object((1,3,6,1,4,1,9,9,86,1,2,2))
if mibBuilder.loadTexts:cdspStatusXTable.setStatus(_B)
_CdspStatusXEntry_Object=MibTableRow
cdspStatusXEntry=_CdspStatusXEntry_Object((1,3,6,1,4,1,9,9,86,1,2,2,1))
if mibBuilder.loadTexts:cdspStatusXEntry.setStatus(_B)
_CdspXNumberOfBearerCalls_Type=Gauge32
_CdspXNumberOfBearerCalls_Object=MibTableColumn
cdspXNumberOfBearerCalls=_CdspXNumberOfBearerCalls_Object((1,3,6,1,4,1,9,9,86,1,2,2,1,1),_CdspXNumberOfBearerCalls_Type())
cdspXNumberOfBearerCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspXNumberOfBearerCalls.setStatus(_B)
if mibBuilder.loadTexts:cdspXNumberOfBearerCalls.setUnits('calls')
_CdspXNumberOfSigCalls_Type=Gauge32
_CdspXNumberOfSigCalls_Object=MibTableColumn
cdspXNumberOfSigCalls=_CdspXNumberOfSigCalls_Object((1,3,6,1,4,1,9,9,86,1,2,2,1,2),_CdspXNumberOfSigCalls_Type())
cdspXNumberOfSigCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspXNumberOfSigCalls.setStatus(_B)
if mibBuilder.loadTexts:cdspXNumberOfSigCalls.setUnits('calls')
_CdspXAvailableBearerBandwidth_Type=Gauge32
_CdspXAvailableBearerBandwidth_Object=MibTableColumn
cdspXAvailableBearerBandwidth=_CdspXAvailableBearerBandwidth_Object((1,3,6,1,4,1,9,9,86,1,2,2,1,3),_CdspXAvailableBearerBandwidth_Type())
cdspXAvailableBearerBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspXAvailableBearerBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cdspXAvailableBearerBandwidth.setUnits(_Y)
_CdspXAvailableSigBandwidth_Type=Gauge32
_CdspXAvailableSigBandwidth_Object=MibTableColumn
cdspXAvailableSigBandwidth=_CdspXAvailableSigBandwidth_Object((1,3,6,1,4,1,9,9,86,1,2,2,1,4),_CdspXAvailableSigBandwidth_Type())
cdspXAvailableSigBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspXAvailableSigBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cdspXAvailableSigBandwidth.setUnits(_Y)
_CdspMIBNotificationEnables_ObjectIdentity=ObjectIdentity
cdspMIBNotificationEnables=_CdspMIBNotificationEnables_ObjectIdentity((1,3,6,1,4,1,9,9,86,1,3))
class _CdspMIBEnableCardStatusNotification_Type(TruthValue):defaultValue=2
_CdspMIBEnableCardStatusNotification_Type.__name__=_P
_CdspMIBEnableCardStatusNotification_Object=MibScalar
cdspMIBEnableCardStatusNotification=_CdspMIBEnableCardStatusNotification_Object((1,3,6,1,4,1,9,9,86,1,3,1),_CdspMIBEnableCardStatusNotification_Type())
cdspMIBEnableCardStatusNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspMIBEnableCardStatusNotification.setStatus(_B)
class _CdspEnableOperStateNotification_Type(TruthValue):defaultValue=2
_CdspEnableOperStateNotification_Type.__name__=_P
_CdspEnableOperStateNotification_Object=MibScalar
cdspEnableOperStateNotification=_CdspEnableOperStateNotification_Object((1,3,6,1,4,1,9,9,86,1,3,2),_CdspEnableOperStateNotification_Type())
cdspEnableOperStateNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspEnableOperStateNotification.setStatus(_B)
_CdspVideoUsageNotificationEnable_Type=TruthValue
_CdspVideoUsageNotificationEnable_Object=MibScalar
cdspVideoUsageNotificationEnable=_CdspVideoUsageNotificationEnable_Object((1,3,6,1,4,1,9,9,86,1,3,3),_CdspVideoUsageNotificationEnable_Type())
cdspVideoUsageNotificationEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspVideoUsageNotificationEnable.setStatus(_B)
_CdspVideoOutOfResourceNotificationEnable_Type=TruthValue
_CdspVideoOutOfResourceNotificationEnable_Object=MibScalar
cdspVideoOutOfResourceNotificationEnable=_CdspVideoOutOfResourceNotificationEnable_Object((1,3,6,1,4,1,9,9,86,1,3,4),_CdspVideoOutOfResourceNotificationEnable_Type())
cdspVideoOutOfResourceNotificationEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspVideoOutOfResourceNotificationEnable.setStatus(_B)
_CdspVoiceObjects_ObjectIdentity=ObjectIdentity
cdspVoiceObjects=_CdspVoiceObjects_ObjectIdentity((1,3,6,1,4,1,9,9,86,1,4))
_CdspVoiceParamTable_Object=MibTable
cdspVoiceParamTable=_CdspVoiceParamTable_Object((1,3,6,1,4,1,9,9,86,1,4,1))
if mibBuilder.loadTexts:cdspVoiceParamTable.setStatus(_B)
_CdspVoiceParamEntry_Object=MibTableRow
cdspVoiceParamEntry=_CdspVoiceParamEntry_Object((1,3,6,1,4,1,9,9,86,1,4,1,1))
cdspVoiceParamEntry.setIndexNames((0,_R,_T))
if mibBuilder.loadTexts:cdspVoiceParamEntry.setStatus(_B)
class _CdspRtpSidPayloadType_Type(Integer32):defaultValue=13;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(13,19)));namedValues=NamedValues(*(('decimal',13),('hexadecimal',19)))
_CdspRtpSidPayloadType_Type.__name__=_F
_CdspRtpSidPayloadType_Object=MibTableColumn
cdspRtpSidPayloadType=_CdspRtpSidPayloadType_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,1),_CdspRtpSidPayloadType_Type())
cdspRtpSidPayloadType.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtpSidPayloadType.setStatus(_B)
class _CdspRtcpControl_Type(TruthValue):defaultValue=1
_CdspRtcpControl_Type.__name__=_P
_CdspRtcpControl_Object=MibTableColumn
cdspRtcpControl=_CdspRtcpControl_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,2),_CdspRtcpControl_Type())
cdspRtcpControl.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtcpControl.setStatus(_B)
class _CdspRtcpTransInterval_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,65535))
_CdspRtcpTransInterval_Type.__name__=_D
_CdspRtcpTransInterval_Object=MibTableColumn
cdspRtcpTransInterval=_CdspRtcpTransInterval_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,3),_CdspRtcpTransInterval_Type())
cdspRtcpTransInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtcpTransInterval.setStatus(_B)
if mibBuilder.loadTexts:cdspRtcpTransInterval.setUnits(_AR)
class _CdspRtcpRecvMultiplier_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CdspRtcpRecvMultiplier_Type.__name__=_D
_CdspRtcpRecvMultiplier_Object=MibTableColumn
cdspRtcpRecvMultiplier=_CdspRtcpRecvMultiplier_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,4),_CdspRtcpRecvMultiplier_Type())
cdspRtcpRecvMultiplier.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtcpRecvMultiplier.setStatus(_B)
class _CdspVadAdaptive_Type(TruthValue):defaultValue=2
_CdspVadAdaptive_Type.__name__=_P
_CdspVadAdaptive_Object=MibTableColumn
cdspVadAdaptive=_CdspVadAdaptive_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,5),_CdspVadAdaptive_Type())
cdspVadAdaptive.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspVadAdaptive.setStatus(_B)
class _CdspDtmfPowerLevel_Type(Integer32):defaultValue=-120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,30))
_CdspDtmfPowerLevel_Type.__name__=_F
_CdspDtmfPowerLevel_Object=MibTableColumn
cdspDtmfPowerLevel=_CdspDtmfPowerLevel_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,6),_CdspDtmfPowerLevel_Type())
cdspDtmfPowerLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspDtmfPowerLevel.setStatus(_B)
if mibBuilder.loadTexts:cdspDtmfPowerLevel.setUnits('0.1 dBm')
class _CdspDtmfPowerTwist_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_CdspDtmfPowerTwist_Type.__name__=_F
_CdspDtmfPowerTwist_Object=MibTableColumn
cdspDtmfPowerTwist=_CdspDtmfPowerTwist_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,7),_CdspDtmfPowerTwist_Type())
cdspDtmfPowerTwist.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspDtmfPowerTwist.setStatus(_B)
if mibBuilder.loadTexts:cdspDtmfPowerTwist.setUnits('0.1 dB')
class _CdspRtcpTimerControl_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('startImmediately',2),('startRtpOrRtcpPktRcvd',3),('startRtcpPktRcvd',4)))
_CdspRtcpTimerControl_Type.__name__=_F
_CdspRtcpTimerControl_Object=MibTableColumn
cdspRtcpTimerControl=_CdspRtcpTimerControl_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,8),_CdspRtcpTimerControl_Type())
cdspRtcpTimerControl.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtcpTimerControl.setStatus(_B)
class _CdspVqmControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('rfc3611Vqm',2),('xnq',3)))
_CdspVqmControl_Type.__name__=_F
_CdspVqmControl_Object=MibTableColumn
cdspVqmControl=_CdspVqmControl_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,9),_CdspVqmControl_Type())
cdspVqmControl.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspVqmControl.setStatus(_B)
class _CdspRtcpXrControl_Type(TruthValue):defaultValue=1
_CdspRtcpXrControl_Type.__name__=_P
_CdspRtcpXrControl_Object=MibTableColumn
cdspRtcpXrControl=_CdspRtcpXrControl_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,10),_CdspRtcpXrControl_Type())
cdspRtcpXrControl.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtcpXrControl.setStatus(_B)
class _CdspRtcpXrTransMultiplier_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_CdspRtcpXrTransMultiplier_Type.__name__=_D
_CdspRtcpXrTransMultiplier_Object=MibTableColumn
cdspRtcpXrTransMultiplier=_CdspRtcpXrTransMultiplier_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,11),_CdspRtcpXrTransMultiplier_Type())
cdspRtcpXrTransMultiplier.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtcpXrTransMultiplier.setStatus(_B)
class _CdspRtcpXrGminDefault_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CdspRtcpXrGminDefault_Type.__name__=_D
_CdspRtcpXrGminDefault_Object=MibTableColumn
cdspRtcpXrGminDefault=_CdspRtcpXrGminDefault_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,12),_CdspRtcpXrGminDefault_Type())
cdspRtcpXrGminDefault.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtcpXrGminDefault.setStatus(_B)
class _CdspRtcpXrExtRfactor_Type(Unsigned32):defaultValue=127;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CdspRtcpXrExtRfactor_Type.__name__=_D
_CdspRtcpXrExtRfactor_Object=MibTableColumn
cdspRtcpXrExtRfactor=_CdspRtcpXrExtRfactor_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,13),_CdspRtcpXrExtRfactor_Type())
cdspRtcpXrExtRfactor.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspRtcpXrExtRfactor.setStatus(_B)
class _CdspPktLossConcealment_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('simple',2),('g711A1',3)))
_CdspPktLossConcealment_Type.__name__=_F
_CdspPktLossConcealment_Object=MibTableColumn
cdspPktLossConcealment=_CdspPktLossConcealment_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,14),_CdspPktLossConcealment_Type())
cdspPktLossConcealment.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspPktLossConcealment.setStatus(_B)
class _CdspVqmThreshSES_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_CdspVqmThreshSES_Type.__name__=_D
_CdspVqmThreshSES_Object=MibTableColumn
cdspVqmThreshSES=_CdspVqmThreshSES_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,15),_CdspVqmThreshSES_Type())
cdspVqmThreshSES.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspVqmThreshSES.setStatus(_B)
if mibBuilder.loadTexts:cdspVqmThreshSES.setUnits(_AR)
class _CdspTransparentIpIp_Type(TruthValue):defaultValue=2
_CdspTransparentIpIp_Type.__name__=_P
_CdspTransparentIpIp_Object=MibTableColumn
cdspTransparentIpIp=_CdspTransparentIpIp_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,16),_CdspTransparentIpIp_Type())
cdspTransparentIpIp.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspTransparentIpIp.setStatus(_G)
class _CdspVoiceModeIpIp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_p,1),('fastRoute',2),('transparent',3)))
_CdspVoiceModeIpIp_Type.__name__=_F
_CdspVoiceModeIpIp_Object=MibTableColumn
cdspVoiceModeIpIp=_CdspVoiceModeIpIp_Object((1,3,6,1,4,1,9,9,86,1,4,1,1,17),_CdspVoiceModeIpIp_Type())
cdspVoiceModeIpIp.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspVoiceModeIpIp.setStatus(_B)
_CdspUtilObjects_ObjectIdentity=ObjectIdentity
cdspUtilObjects=_CdspUtilObjects_ObjectIdentity((1,3,6,1,4,1,9,9,86,1,5))
_CdspUtilTable_Object=MibTable
cdspUtilTable=_CdspUtilTable_Object((1,3,6,1,4,1,9,9,86,1,5,1))
if mibBuilder.loadTexts:cdspUtilTable.setStatus(_B)
_CdspUtilEntry_Object=MibTableRow
cdspUtilEntry=_CdspUtilEntry_Object((1,3,6,1,4,1,9,9,86,1,5,1,1))
cdspUtilEntry.setIndexNames((0,_R,_T),(0,_A,_AS))
if mibBuilder.loadTexts:cdspUtilEntry.setStatus(_B)
class _CdspCodecPoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CdspCodecPoolIndex_Type.__name__=_D
_CdspCodecPoolIndex_Object=MibTableColumn
cdspCodecPoolIndex=_CdspCodecPoolIndex_Object((1,3,6,1,4,1,9,9,86,1,5,1,1,1),_CdspCodecPoolIndex_Type())
cdspCodecPoolIndex.setMaxAccess(_b)
if mibBuilder.loadTexts:cdspCodecPoolIndex.setStatus(_B)
class _CdspCurrentUtilCap_Type(Unsigned32):defaultValue=0
_CdspCurrentUtilCap_Type.__name__=_D
_CdspCurrentUtilCap_Object=MibTableColumn
cdspCurrentUtilCap=_CdspCurrentUtilCap_Object((1,3,6,1,4,1,9,9,86,1,5,1,1,2),_CdspCurrentUtilCap_Type())
cdspCurrentUtilCap.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCurrentUtilCap.setStatus(_B)
class _CdspCurrentAvlbCap_Type(Unsigned32):defaultValue=0
_CdspCurrentAvlbCap_Type.__name__=_D
_CdspCurrentAvlbCap_Object=MibTableColumn
cdspCurrentAvlbCap=_CdspCurrentAvlbCap_Object((1,3,6,1,4,1,9,9,86,1,5,1,1,3),_CdspCurrentAvlbCap_Type())
cdspCurrentAvlbCap.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspCurrentAvlbCap.setStatus(_B)
_CdspDspfarmObjects_ObjectIdentity=ObjectIdentity
cdspDspfarmObjects=_CdspDspfarmObjects_ObjectIdentity((1,3,6,1,4,1,9,9,86,1,6))
class _CdspGlobMaxConfTranscodeSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspGlobMaxConfTranscodeSess_Type.__name__=_D
_CdspGlobMaxConfTranscodeSess_Object=MibScalar
cdspGlobMaxConfTranscodeSess=_CdspGlobMaxConfTranscodeSess_Object((1,3,6,1,4,1,9,9,86,1,6,1),_CdspGlobMaxConfTranscodeSess_Type())
cdspGlobMaxConfTranscodeSess.setMaxAccess(_E)
if mibBuilder.loadTexts:cdspGlobMaxConfTranscodeSess.setStatus(_B)
class _CdspGlobMaxAvailTranscodeSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspGlobMaxAvailTranscodeSess_Type.__name__=_D
_CdspGlobMaxAvailTranscodeSess_Object=MibScalar
cdspGlobMaxAvailTranscodeSess=_CdspGlobMaxAvailTranscodeSess_Object((1,3,6,1,4,1,9,9,86,1,6,2),_CdspGlobMaxAvailTranscodeSess_Type())
cdspGlobMaxAvailTranscodeSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspGlobMaxAvailTranscodeSess.setStatus(_B)
_CdspTranscodeProfileTable_Object=MibTable
cdspTranscodeProfileTable=_CdspTranscodeProfileTable_Object((1,3,6,1,4,1,9,9,86,1,6,3))
if mibBuilder.loadTexts:cdspTranscodeProfileTable.setStatus(_B)
_CdspTranscodeProfileEntry_Object=MibTableRow
cdspTranscodeProfileEntry=_CdspTranscodeProfileEntry_Object((1,3,6,1,4,1,9,9,86,1,6,3,1))
cdspTranscodeProfileEntry.setIndexNames((0,_A,_AT))
if mibBuilder.loadTexts:cdspTranscodeProfileEntry.setStatus(_B)
class _CdspTranscodeProfileMaxCodec_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdspTranscodeProfileMaxCodec_Type.__name__=_D
_CdspTranscodeProfileMaxCodec_Object=MibTableColumn
cdspTranscodeProfileMaxCodec=_CdspTranscodeProfileMaxCodec_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,1),_CdspTranscodeProfileMaxCodec_Type())
cdspTranscodeProfileMaxCodec.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspTranscodeProfileMaxCodec.setStatus(_B)
if mibBuilder.loadTexts:cdspTranscodeProfileMaxCodec.setUnits(_q)
class _CdspTranscodeProfileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdspTranscodeProfileId_Type.__name__=_D
_CdspTranscodeProfileId_Object=MibTableColumn
cdspTranscodeProfileId=_CdspTranscodeProfileId_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,2),_CdspTranscodeProfileId_Type())
cdspTranscodeProfileId.setMaxAccess(_b)
if mibBuilder.loadTexts:cdspTranscodeProfileId.setStatus(_B)
_CdspTranscodeProfileMaxConfSess_Type=Unsigned32
_CdspTranscodeProfileMaxConfSess_Object=MibTableColumn
cdspTranscodeProfileMaxConfSess=_CdspTranscodeProfileMaxConfSess_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,3),_CdspTranscodeProfileMaxConfSess_Type())
cdspTranscodeProfileMaxConfSess.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspTranscodeProfileMaxConfSess.setStatus(_B)
if mibBuilder.loadTexts:cdspTranscodeProfileMaxConfSess.setUnits(_U)
class _CdspTranscodeProfileMaxAvailSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspTranscodeProfileMaxAvailSess_Type.__name__=_D
_CdspTranscodeProfileMaxAvailSess_Object=MibTableColumn
cdspTranscodeProfileMaxAvailSess=_CdspTranscodeProfileMaxAvailSess_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,4),_CdspTranscodeProfileMaxAvailSess_Type())
cdspTranscodeProfileMaxAvailSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTranscodeProfileMaxAvailSess.setStatus(_B)
_CdspTranscodeProfileRowStatus_Type=RowStatus
_CdspTranscodeProfileRowStatus_Object=MibTableColumn
cdspTranscodeProfileRowStatus=_CdspTranscodeProfileRowStatus_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,5),_CdspTranscodeProfileRowStatus_Type())
cdspTranscodeProfileRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspTranscodeProfileRowStatus.setStatus(_B)
_CdspTranscodeResourceId_Type=Unsigned32
_CdspTranscodeResourceId_Object=MibTableColumn
cdspTranscodeResourceId=_CdspTranscodeResourceId_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,6),_CdspTranscodeResourceId_Type())
cdspTranscodeResourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTranscodeResourceId.setStatus(_B)
_CdspTranscodeDescription_Type=SnmpAdminString
_CdspTranscodeDescription_Object=MibTableColumn
cdspTranscodeDescription=_CdspTranscodeDescription_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,7),_CdspTranscodeDescription_Type())
cdspTranscodeDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTranscodeDescription.setStatus(_B)
class _CdspTranscodeService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_r,1),(_s,2)))
_CdspTranscodeService_Type.__name__=_F
_CdspTranscodeService_Object=MibTableColumn
cdspTranscodeService=_CdspTranscodeService_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,8),_CdspTranscodeService_Type())
cdspTranscodeService.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTranscodeService.setStatus(_B)
class _CdspTranscodeAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),('up',2)))
_CdspTranscodeAdminState_Type.__name__=_F
_CdspTranscodeAdminState_Object=MibTableColumn
cdspTranscodeAdminState=_CdspTranscodeAdminState_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,9),_CdspTranscodeAdminState_Type())
cdspTranscodeAdminState.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspTranscodeAdminState.setStatus(_B)
class _CdspTranscodeApplication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_u,2),(_v,3),(_w,4),(_a,5)))
_CdspTranscodeApplication_Type.__name__=_F
_CdspTranscodeApplication_Object=MibTableColumn
cdspTranscodeApplication=_CdspTranscodeApplication_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,10),_CdspTranscodeApplication_Type())
cdspTranscodeApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTranscodeApplication.setStatus(_B)
class _CdspTranscodeApplicationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),(_x,2),(_y,3),(_z,4),(_A0,5),(_A1,6)))
_CdspTranscodeApplicationStatus_Type.__name__=_F
_CdspTranscodeApplicationStatus_Object=MibTableColumn
cdspTranscodeApplicationStatus=_CdspTranscodeApplicationStatus_Object((1,3,6,1,4,1,9,9,86,1,6,3,1,11),_CdspTranscodeApplicationStatus_Type())
cdspTranscodeApplicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTranscodeApplicationStatus.setStatus(_B)
_CdspMtpProfileTable_Object=MibTable
cdspMtpProfileTable=_CdspMtpProfileTable_Object((1,3,6,1,4,1,9,9,86,1,6,4))
if mibBuilder.loadTexts:cdspMtpProfileTable.setStatus(_B)
_CdspMtpProfileEntry_Object=MibTableRow
cdspMtpProfileEntry=_CdspMtpProfileEntry_Object((1,3,6,1,4,1,9,9,86,1,6,4,1))
cdspMtpProfileEntry.setIndexNames((0,_A,_AU))
if mibBuilder.loadTexts:cdspMtpProfileEntry.setStatus(_B)
class _CdspMtpProfileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdspMtpProfileId_Type.__name__=_D
_CdspMtpProfileId_Object=MibTableColumn
cdspMtpProfileId=_CdspMtpProfileId_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,1),_CdspMtpProfileId_Type())
cdspMtpProfileId.setMaxAccess(_b)
if mibBuilder.loadTexts:cdspMtpProfileId.setStatus(_B)
class _CdspMtpProfileMaxConfSoftSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspMtpProfileMaxConfSoftSess_Type.__name__=_D
_CdspMtpProfileMaxConfSoftSess_Object=MibTableColumn
cdspMtpProfileMaxConfSoftSess=_CdspMtpProfileMaxConfSoftSess_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,2),_CdspMtpProfileMaxConfSoftSess_Type())
cdspMtpProfileMaxConfSoftSess.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspMtpProfileMaxConfSoftSess.setStatus(_B)
if mibBuilder.loadTexts:cdspMtpProfileMaxConfSoftSess.setUnits(_U)
class _CdspMtpProfileMaxConfHardSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspMtpProfileMaxConfHardSess_Type.__name__=_D
_CdspMtpProfileMaxConfHardSess_Object=MibTableColumn
cdspMtpProfileMaxConfHardSess=_CdspMtpProfileMaxConfHardSess_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,3),_CdspMtpProfileMaxConfHardSess_Type())
cdspMtpProfileMaxConfHardSess.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspMtpProfileMaxConfHardSess.setStatus(_B)
if mibBuilder.loadTexts:cdspMtpProfileMaxConfHardSess.setUnits(_U)
class _CdspMtpProfileMaxAvailHardSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspMtpProfileMaxAvailHardSess_Type.__name__=_D
_CdspMtpProfileMaxAvailHardSess_Object=MibTableColumn
cdspMtpProfileMaxAvailHardSess=_CdspMtpProfileMaxAvailHardSess_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,4),_CdspMtpProfileMaxAvailHardSess_Type())
cdspMtpProfileMaxAvailHardSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspMtpProfileMaxAvailHardSess.setStatus(_B)
if mibBuilder.loadTexts:cdspMtpProfileMaxAvailHardSess.setUnits(_U)
_CdspMtpProfileRowStatus_Type=RowStatus
_CdspMtpProfileRowStatus_Object=MibTableColumn
cdspMtpProfileRowStatus=_CdspMtpProfileRowStatus_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,5),_CdspMtpProfileRowStatus_Type())
cdspMtpProfileRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspMtpProfileRowStatus.setStatus(_B)
_CdspMtpResourceId_Type=Unsigned32
_CdspMtpResourceId_Object=MibTableColumn
cdspMtpResourceId=_CdspMtpResourceId_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,6),_CdspMtpResourceId_Type())
cdspMtpResourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspMtpResourceId.setStatus(_B)
_CdspMtpDescription_Type=SnmpAdminString
_CdspMtpDescription_Object=MibTableColumn
cdspMtpDescription=_CdspMtpDescription_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,7),_CdspMtpDescription_Type())
cdspMtpDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspMtpDescription.setStatus(_B)
class _CdspMtpService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_r,1),(_s,2)))
_CdspMtpService_Type.__name__=_F
_CdspMtpService_Object=MibTableColumn
cdspMtpService=_CdspMtpService_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,8),_CdspMtpService_Type())
cdspMtpService.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspMtpService.setStatus(_B)
class _CdspMtpAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),('up',2)))
_CdspMtpAdminState_Type.__name__=_F
_CdspMtpAdminState_Object=MibTableColumn
cdspMtpAdminState=_CdspMtpAdminState_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,9),_CdspMtpAdminState_Type())
cdspMtpAdminState.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspMtpAdminState.setStatus(_B)
class _CdspMtpApplication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_u,2),(_v,3),(_w,4),(_a,5)))
_CdspMtpApplication_Type.__name__=_F
_CdspMtpApplication_Object=MibTableColumn
cdspMtpApplication=_CdspMtpApplication_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,10),_CdspMtpApplication_Type())
cdspMtpApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspMtpApplication.setStatus(_B)
class _CdspMtpApplicationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),(_x,2),(_y,3),(_z,4),(_A0,5),(_A1,6)))
_CdspMtpApplicationStatus_Type.__name__=_F
_CdspMtpApplicationStatus_Object=MibTableColumn
cdspMtpApplicationStatus=_CdspMtpApplicationStatus_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,11),_CdspMtpApplicationStatus_Type())
cdspMtpApplicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspMtpApplicationStatus.setStatus(_B)
_CdspMtpProfileMaxCodec_Type=Unsigned32
_CdspMtpProfileMaxCodec_Object=MibTableColumn
cdspMtpProfileMaxCodec=_CdspMtpProfileMaxCodec_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,12),_CdspMtpProfileMaxCodec_Type())
cdspMtpProfileMaxCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspMtpProfileMaxCodec.setStatus(_B)
if mibBuilder.loadTexts:cdspMtpProfileMaxCodec.setUnits(_q)
_CdspMtpProfileMaxAvailSoftSess_Type=Unsigned32
_CdspMtpProfileMaxAvailSoftSess_Object=MibTableColumn
cdspMtpProfileMaxAvailSoftSess=_CdspMtpProfileMaxAvailSoftSess_Object((1,3,6,1,4,1,9,9,86,1,6,4,1,13),_CdspMtpProfileMaxAvailSoftSess_Type())
cdspMtpProfileMaxAvailSoftSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspMtpProfileMaxAvailSoftSess.setStatus(_B)
if mibBuilder.loadTexts:cdspMtpProfileMaxAvailSoftSess.setUnits(_U)
_CdspConferenceProfileTable_Object=MibTable
cdspConferenceProfileTable=_CdspConferenceProfileTable_Object((1,3,6,1,4,1,9,9,86,1,6,5))
if mibBuilder.loadTexts:cdspConferenceProfileTable.setStatus(_B)
_CdspConferenceProfileEntry_Object=MibTableRow
cdspConferenceProfileEntry=_CdspConferenceProfileEntry_Object((1,3,6,1,4,1,9,9,86,1,6,5,1))
cdspConferenceProfileEntry.setIndexNames((0,_A,_AV))
if mibBuilder.loadTexts:cdspConferenceProfileEntry.setStatus(_B)
class _CdspConferenceProfileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdspConferenceProfileId_Type.__name__=_D
_CdspConferenceProfileId_Object=MibTableColumn
cdspConferenceProfileId=_CdspConferenceProfileId_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,1),_CdspConferenceProfileId_Type())
cdspConferenceProfileId.setMaxAccess(_b)
if mibBuilder.loadTexts:cdspConferenceProfileId.setStatus(_B)
_CdspConferenceResourceId_Type=Unsigned32
_CdspConferenceResourceId_Object=MibTableColumn
cdspConferenceResourceId=_CdspConferenceResourceId_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,2),_CdspConferenceResourceId_Type())
cdspConferenceResourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspConferenceResourceId.setStatus(_B)
_CdspConferenceDescription_Type=SnmpAdminString
_CdspConferenceDescription_Object=MibTableColumn
cdspConferenceDescription=_CdspConferenceDescription_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,3),_CdspConferenceDescription_Type())
cdspConferenceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspConferenceDescription.setStatus(_B)
class _CdspConferenceService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_r,1),(_s,2)))
_CdspConferenceService_Type.__name__=_F
_CdspConferenceService_Object=MibTableColumn
cdspConferenceService=_CdspConferenceService_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,4),_CdspConferenceService_Type())
cdspConferenceService.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspConferenceService.setStatus(_B)
class _CdspConferenceAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),('up',2)))
_CdspConferenceAdminState_Type.__name__=_F
_CdspConferenceAdminState_Object=MibTableColumn
cdspConferenceAdminState=_CdspConferenceAdminState_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,5),_CdspConferenceAdminState_Type())
cdspConferenceAdminState.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspConferenceAdminState.setStatus(_B)
class _CdspConferenceApplication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_u,2),(_v,3),(_w,4),(_a,5)))
_CdspConferenceApplication_Type.__name__=_F
_CdspConferenceApplication_Object=MibTableColumn
cdspConferenceApplication=_CdspConferenceApplication_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,6),_CdspConferenceApplication_Type())
cdspConferenceApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspConferenceApplication.setStatus(_B)
class _CdspConferenceApplicationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),(_x,2),(_y,3),(_z,4),(_A0,5),(_A1,6)))
_CdspConferenceApplicationStatus_Type.__name__=_F
_CdspConferenceApplicationStatus_Object=MibTableColumn
cdspConferenceApplicationStatus=_CdspConferenceApplicationStatus_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,7),_CdspConferenceApplicationStatus_Type())
cdspConferenceApplicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspConferenceApplicationStatus.setStatus(_B)
class _CdspConferenceProfileMaxCodec_Type(Unsigned32):defaultValue=0
_CdspConferenceProfileMaxCodec_Type.__name__=_D
_CdspConferenceProfileMaxCodec_Object=MibTableColumn
cdspConferenceProfileMaxCodec=_CdspConferenceProfileMaxCodec_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,8),_CdspConferenceProfileMaxCodec_Type())
cdspConferenceProfileMaxCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspConferenceProfileMaxCodec.setStatus(_B)
if mibBuilder.loadTexts:cdspConferenceProfileMaxCodec.setUnits(_q)
class _CdspConferenceProfileMaxConfSess_Type(Unsigned32):defaultValue=0
_CdspConferenceProfileMaxConfSess_Type.__name__=_D
_CdspConferenceProfileMaxConfSess_Object=MibTableColumn
cdspConferenceProfileMaxConfSess=_CdspConferenceProfileMaxConfSess_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,9),_CdspConferenceProfileMaxConfSess_Type())
cdspConferenceProfileMaxConfSess.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspConferenceProfileMaxConfSess.setStatus(_B)
_CdspConferenceProfileMaxAvailSess_Type=Unsigned32
_CdspConferenceProfileMaxAvailSess_Object=MibTableColumn
cdspConferenceProfileMaxAvailSess=_CdspConferenceProfileMaxAvailSess_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,10),_CdspConferenceProfileMaxAvailSess_Type())
cdspConferenceProfileMaxAvailSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspConferenceProfileMaxAvailSess.setStatus(_B)
class _CdspConferenceProfileStorageType_Type(StorageType):defaultValue=3
_CdspConferenceProfileStorageType_Type.__name__=_AQ
_CdspConferenceProfileStorageType_Object=MibTableColumn
cdspConferenceProfileStorageType=_CdspConferenceProfileStorageType_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,11),_CdspConferenceProfileStorageType_Type())
cdspConferenceProfileStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspConferenceProfileStorageType.setStatus(_B)
_CdspConferenceProfileRowStatus_Type=RowStatus
_CdspConferenceProfileRowStatus_Object=MibTableColumn
cdspConferenceProfileRowStatus=_CdspConferenceProfileRowStatus_Object((1,3,6,1,4,1,9,9,86,1,6,5,1,12),_CdspConferenceProfileRowStatus_Type())
cdspConferenceProfileRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:cdspConferenceProfileRowStatus.setStatus(_B)
_CdspDspfarmUtilObjects_ObjectIdentity=ObjectIdentity
cdspDspfarmUtilObjects=_CdspDspfarmUtilObjects_ObjectIdentity((1,3,6,1,4,1,9,9,86,1,7))
class _CdspTotAvailTranscodeSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspTotAvailTranscodeSess_Type.__name__=_D
_CdspTotAvailTranscodeSess_Object=MibScalar
cdspTotAvailTranscodeSess=_CdspTotAvailTranscodeSess_Object((1,3,6,1,4,1,9,9,86,1,7,1),_CdspTotAvailTranscodeSess_Type())
cdspTotAvailTranscodeSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTotAvailTranscodeSess.setStatus(_B)
class _CdspTotUnusedTranscodeSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspTotUnusedTranscodeSess_Type.__name__=_D
_CdspTotUnusedTranscodeSess_Object=MibScalar
cdspTotUnusedTranscodeSess=_CdspTotUnusedTranscodeSess_Object((1,3,6,1,4,1,9,9,86,1,7,2),_CdspTotUnusedTranscodeSess_Type())
cdspTotUnusedTranscodeSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTotUnusedTranscodeSess.setStatus(_B)
class _CdspTotAvailMtpSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspTotAvailMtpSess_Type.__name__=_D
_CdspTotAvailMtpSess_Object=MibScalar
cdspTotAvailMtpSess=_CdspTotAvailMtpSess_Object((1,3,6,1,4,1,9,9,86,1,7,3),_CdspTotAvailMtpSess_Type())
cdspTotAvailMtpSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTotAvailMtpSess.setStatus(_B)
class _CdspTotUnusedMtpSess_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdspTotUnusedMtpSess_Type.__name__=_D
_CdspTotUnusedMtpSess_Object=MibScalar
cdspTotUnusedMtpSess=_CdspTotUnusedMtpSess_Object((1,3,6,1,4,1,9,9,86,1,7,4),_CdspTotUnusedMtpSess_Type())
cdspTotUnusedMtpSess.setMaxAccess(_C)
if mibBuilder.loadTexts:cdspTotUnusedMtpSess.setStatus(_B)
_CdspMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cdspMIBNotificationPrefix=_CdspMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,86,2))
_CdspMIBNotifications_ObjectIdentity=ObjectIdentity
cdspMIBNotifications=_CdspMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,86,2,0))
_CdspMgmtConformance_ObjectIdentity=ObjectIdentity
cdspMgmtConformance=_CdspMgmtConformance_ObjectIdentity((1,3,6,1,4,1,9,9,86,3))
_CdspMgmtCompliances_ObjectIdentity=ObjectIdentity
cdspMgmtCompliances=_CdspMgmtCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,86,3,1))
_CdspMgmtGroups_ObjectIdentity=ObjectIdentity
cdspMgmtGroups=_CdspMgmtGroups_ObjectIdentity((1,3,6,1,4,1,9,9,86,3,2))
cdspStatusEntry.registerAugmentions((_A,_AW))
cdspStatusXEntry.setIndexNames(*cdspStatusEntry.getIndexNames())
cdspMgmtGeneralInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,1))
cdspMgmtGeneralInfoGroup.setObjects(*((_A,_A2),(_A,_c),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_d),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:cdspMgmtGeneralInfoGroup.setStatus(_G)
cdspChannelGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,2))
cdspChannelGroup.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:cdspChannelGroup.setStatus(_B)
cdspMgmtExtGeneralInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,3))
cdspMgmtExtGeneralInfoGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:cdspMgmtExtGeneralInfoGroup.setStatus(_G)
cdspVoiceInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,4))
cdspVoiceInfoGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:cdspVoiceInfoGroup.setStatus(_G)
cdspChannelExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,6))
cdspChannelExtGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:cdspChannelExtGroup.setStatus(_B)
cdspVoiceInfoGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,7))
cdspVoiceInfoGroupRev1.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_AI)))
if mibBuilder.loadTexts:cdspVoiceInfoGroupRev1.setStatus(_G)
cdspMgmtExtGeneralInfoGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,8))
cdspMgmtExtGeneralInfoGroupRev1.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_Ah)))
if mibBuilder.loadTexts:cdspMgmtExtGeneralInfoGroupRev1.setStatus(_B)
cdspMgmtGeneralInfoGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,9))
cdspMgmtGeneralInfoGroupRev1.setObjects(*((_A,_A2),(_A,_c),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_d),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_Ai)))
if mibBuilder.loadTexts:cdspMgmtGeneralInfoGroupRev1.setStatus(_B)
cdspVQMGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,11))
cdspVQMGroup.setObjects(*((_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:cdspVQMGroup.setStatus(_B)
cdspVoiceInfoGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,12))
cdspVoiceInfoGroupRev2.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_AI),(_A,_Ap)))
if mibBuilder.loadTexts:cdspVoiceInfoGroupRev2.setStatus(_B)
cdspTransCodingGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,13))
cdspTransCodingGroup.setObjects((_A,_Aq))
if mibBuilder.loadTexts:cdspTransCodingGroup.setStatus(_G)
cdspTransCodingGroup1=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,14))
cdspTransCodingGroup1.setObjects((_A,_Ar))
if mibBuilder.loadTexts:cdspTransCodingGroup1.setStatus(_B)
cdspUtilInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,15))
cdspUtilInfoGroup.setObjects(*((_A,_As),(_A,_At)))
if mibBuilder.loadTexts:cdspUtilInfoGroup.setStatus(_B)
cdspDspfarmInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,16))
cdspDspfarmInfoGroup.setObjects(*((_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5)))
if mibBuilder.loadTexts:cdspDspfarmInfoGroup.setStatus(_B)
cdspMgmtVideoInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,18))
cdspMgmtVideoInfoGroup.setObjects(*((_A,_l),(_A,_m),(_A,_B6),(_A,_B7)))
if mibBuilder.loadTexts:cdspMgmtVideoInfoGroup.setStatus(_B)
cdspTranscodeProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,19))
cdspTranscodeProfileGroup.setObjects(*((_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_AJ),(_A,_AJ)))
if mibBuilder.loadTexts:cdspTranscodeProfileGroup.setStatus(_B)
cdspMtpProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,20))
cdspMtpProfileGroup.setObjects(*((_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG),(_A,_BH),(_A,_BI),(_A,_BJ),(_A,_BK)))
if mibBuilder.loadTexts:cdspMtpProfileGroup.setStatus(_B)
cdspConferenceProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,86,3,2,21))
cdspConferenceProfileGroup.setObjects(*((_A,_BL),(_A,_BM),(_A,_BN),(_A,_BO),(_A,_BP),(_A,_BQ),(_A,_BR),(_A,_BS),(_A,_BT),(_A,_BU),(_A,_BV)))
if mibBuilder.loadTexts:cdspConferenceProfileGroup.setStatus(_B)
cdspMIBCardStateNotification=NotificationType((1,3,6,1,4,1,9,9,86,2,0,1))
cdspMIBCardStateNotification.setObjects((_A,_c))
if mibBuilder.loadTexts:cdspMIBCardStateNotification.setStatus(_B)
cdspOperStateNotification=NotificationType((1,3,6,1,4,1,9,9,86,2,0,2))
cdspOperStateNotification.setObjects(*((_A,_d),(_R,_AP)))
if mibBuilder.loadTexts:cdspOperStateNotification.setStatus(_B)
cdspVideoUsageNotification=NotificationType((1,3,6,1,4,1,9,9,86,2,0,3))
cdspVideoUsageNotification.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:cdspVideoUsageNotification.setStatus(_B)
cdspVideoOutOfResourceNotification=NotificationType((1,3,6,1,4,1,9,9,86,2,0,4))
cdspVideoOutOfResourceNotification.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:cdspVideoOutOfResourceNotification.setStatus(_B)
cdspMgmtNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,86,3,2,5))
cdspMgmtNotificationsGroup.setObjects((_A,_AK))
if mibBuilder.loadTexts:cdspMgmtNotificationsGroup.setStatus(_G)
cdspMgmtNotificationsGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,86,3,2,10))
cdspMgmtNotificationsGroupRev1.setObjects(*((_A,_AK),(_A,_BW)))
if mibBuilder.loadTexts:cdspMgmtNotificationsGroupRev1.setStatus(_B)
cdspMgmtVideoNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,86,3,2,17))
cdspMgmtVideoNotificationsGroup.setObjects(*((_A,_BX),(_A,_BY)))
if mibBuilder.loadTexts:cdspMgmtVideoNotificationsGroup.setStatus(_B)
cdspMgmtCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,1))
cdspMgmtCompliance.setObjects((_A,_V))
if mibBuilder.loadTexts:cdspMgmtCompliance.setStatus(_G)
cdspMgmtComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,2))
cdspMgmtComplianceRev1.setObjects(*((_A,_V),(_A,_H)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev1.setStatus(_G)
cdspMgmtComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,3))
cdspMgmtComplianceRev2.setObjects(*((_A,_V),(_A,_AL),(_A,_AM),(_A,_H),(_A,_I),(_A,_BZ)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev2.setStatus(_G)
cdspMgmtComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,4))
cdspMgmtComplianceRev3.setObjects(*((_A,_V),(_A,_AL),(_A,_AM),(_A,_H),(_A,_I),(_A,_n)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev3.setStatus(_G)
cdspMgmtComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,5))
cdspMgmtComplianceRev4.setObjects(*((_A,_K),(_A,_H),(_A,_I),(_A,_n)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev4.setStatus(_G)
cdspMgmtComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,6))
cdspMgmtComplianceRev5.setObjects(*((_A,_L),(_A,_M),(_A,_K),(_A,_H),(_A,_I),(_A,_n),(_A,_N)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev5.setStatus(_G)
cdspMgmtComplianceRev6=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,7))
cdspMgmtComplianceRev6.setObjects(*((_A,_L),(_A,_M),(_A,_K),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev6.setStatus(_G)
cdspMgmtComplianceRev7=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,8))
cdspMgmtComplianceRev7.setObjects(*((_A,_L),(_A,_M),(_A,_K),(_A,_H),(_A,_I),(_A,_N),(_A,_O),(_A,_Ba)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev7.setStatus(_G)
cdspMgmtComplianceRev8=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,9))
cdspMgmtComplianceRev8.setObjects(*((_A,_L),(_A,_M),(_A,_K),(_A,_H),(_A,_I),(_A,_N),(_A,_O),(_A,_S)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev8.setStatus(_G)
cdspMgmtComplianceRev9=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,10))
cdspMgmtComplianceRev9.setObjects(*((_A,_L),(_A,_M),(_A,_K),(_A,_H),(_A,_I),(_A,_N),(_A,_O),(_A,_S),(_A,_W)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev9.setStatus(_G)
cdspMgmtComplianceRev10=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,11))
cdspMgmtComplianceRev10.setObjects(*((_A,_L),(_A,_M),(_A,_K),(_A,_H),(_A,_I),(_A,_N),(_A,_O),(_A,_S),(_A,_W),(_A,_o)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev10.setStatus(_G)
cdspMgmtComplianceRev11=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,12))
cdspMgmtComplianceRev11.setObjects(*((_A,_L),(_A,_M),(_A,_K),(_A,_H),(_A,_I),(_A,_N),(_A,_O),(_A,_S),(_A,_W),(_A,_o),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev11.setStatus(_G)
cdspMgmtComplianceRev12=ModuleCompliance((1,3,6,1,4,1,9,9,86,3,1,13))
cdspMgmtComplianceRev12.setObjects(*((_A,_L),(_A,_M),(_A,_K),(_A,_H),(_A,_I),(_A,_N),(_A,_O),(_A,_S),(_A,_W),(_A,_o),(_A,_AN),(_A,_AO),(_A,_Bb),(_A,_Bc),(_A,_Bd)))
if mibBuilder.loadTexts:cdspMgmtComplianceRev12.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDspMgmtMIB':ciscoDspMgmtMIB,'cdspMgmtNotifications':cdspMgmtNotifications,'cdspMgmtObjects':cdspMgmtObjects,'cdspCardObjects':cdspCardObjects,'cdspCardStatusTable':cdspCardStatusTable,'cdspCardStatusEntry':cdspCardStatusEntry,_A2:cdspCardIndex,_c:cdspCardState,_A3:cdspCardResourceUtilization,_A4:cdspCardLastHiWaterUtilization,_A5:cdspCardLastResetTime,_AX:cdspCardMaxChanPerDSP,_AB:cdspTotalDsp,_AC:cdspFailedDsp,_AF:cdspDspSwitchOverThreshold,_AD:cdspCongestedDsp,_AE:cdspNormalDsp,_AG:cdspNx64Dsp,_Ah:cdspCodecTemplateSupported,_l:cdspCardVideoPoolUtilization,_m:cdspCardVideoPoolUtilizationThreshold,'cdspObjects':cdspObjects,'cdspStatusTable':cdspStatusTable,'cdspStatusEntry':cdspStatusEntry,_d:cdspOperState,_A6:cdspAlarms,_A7:cdspLastAlarmCause,_A8:cdspLastAlarmCauseText,_A9:cdspLastAlarmTime,_AY:cdspTotalChannels,_AZ:cdspInUseChannels,_Aa:cdspActiveChannels,_Ab:cdspSigBearerChannelSplit,_Ac:cdspNumCongestionOccurrence,_AH:cdspDspNum,'cdspStatusXTable':cdspStatusXTable,_AW:cdspStatusXEntry,_Ad:cdspXNumberOfBearerCalls,_Ae:cdspXNumberOfSigCalls,_Af:cdspXAvailableBearerBandwidth,_Ag:cdspXAvailableSigBandwidth,'cdspMIBNotificationEnables':cdspMIBNotificationEnables,_AA:cdspMIBEnableCardStatusNotification,_Ai:cdspEnableOperStateNotification,_B6:cdspVideoUsageNotificationEnable,_B7:cdspVideoOutOfResourceNotificationEnable,'cdspVoiceObjects':cdspVoiceObjects,'cdspVoiceParamTable':cdspVoiceParamTable,'cdspVoiceParamEntry':cdspVoiceParamEntry,_e:cdspRtpSidPayloadType,_f:cdspRtcpControl,_g:cdspRtcpTransInterval,_h:cdspRtcpRecvMultiplier,_i:cdspVadAdaptive,_j:cdspDtmfPowerLevel,_k:cdspDtmfPowerTwist,_AI:cdspRtcpTimerControl,_Aj:cdspVqmControl,_Ak:cdspRtcpXrControl,_Al:cdspRtcpXrTransMultiplier,_Am:cdspRtcpXrGminDefault,_An:cdspRtcpXrExtRfactor,_Ap:cdspPktLossConcealment,_Ao:cdspVqmThreshSES,_Aq:cdspTransparentIpIp,_Ar:cdspVoiceModeIpIp,'cdspUtilObjects':cdspUtilObjects,'cdspUtilTable':cdspUtilTable,'cdspUtilEntry':cdspUtilEntry,_AS:cdspCodecPoolIndex,_As:cdspCurrentUtilCap,_At:cdspCurrentAvlbCap,'cdspDspfarmObjects':cdspDspfarmObjects,_Au:cdspGlobMaxConfTranscodeSess,_Av:cdspGlobMaxAvailTranscodeSess,'cdspTranscodeProfileTable':cdspTranscodeProfileTable,'cdspTranscodeProfileEntry':cdspTranscodeProfileEntry,_AJ:cdspTranscodeProfileMaxCodec,_AT:cdspTranscodeProfileId,_Ax:cdspTranscodeProfileMaxConfSess,_Ay:cdspTranscodeProfileMaxAvailSess,_Aw:cdspTranscodeProfileRowStatus,_B8:cdspTranscodeResourceId,_B9:cdspTranscodeDescription,_BA:cdspTranscodeService,_BB:cdspTranscodeAdminState,_BC:cdspTranscodeApplication,'cdspTranscodeApplicationStatus':cdspTranscodeApplicationStatus,'cdspMtpProfileTable':cdspMtpProfileTable,'cdspMtpProfileEntry':cdspMtpProfileEntry,_AU:cdspMtpProfileId,_A_:cdspMtpProfileMaxConfSoftSess,_B0:cdspMtpProfileMaxConfHardSess,_B1:cdspMtpProfileMaxAvailHardSess,_Az:cdspMtpProfileRowStatus,_BD:cdspMtpResourceId,_BE:cdspMtpDescription,_BF:cdspMtpService,_BG:cdspMtpAdminState,_BH:cdspMtpApplication,_BI:cdspMtpApplicationStatus,_BJ:cdspMtpProfileMaxCodec,_BK:cdspMtpProfileMaxAvailSoftSess,'cdspConferenceProfileTable':cdspConferenceProfileTable,'cdspConferenceProfileEntry':cdspConferenceProfileEntry,_AV:cdspConferenceProfileId,_BL:cdspConferenceResourceId,_BM:cdspConferenceDescription,_BN:cdspConferenceService,_BO:cdspConferenceAdminState,_BP:cdspConferenceApplication,_BQ:cdspConferenceApplicationStatus,_BR:cdspConferenceProfileMaxCodec,_BS:cdspConferenceProfileMaxConfSess,_BT:cdspConferenceProfileMaxAvailSess,_BU:cdspConferenceProfileStorageType,_BV:cdspConferenceProfileRowStatus,'cdspDspfarmUtilObjects':cdspDspfarmUtilObjects,_B2:cdspTotAvailTranscodeSess,_B3:cdspTotUnusedTranscodeSess,_B4:cdspTotAvailMtpSess,_B5:cdspTotUnusedMtpSess,'cdspMIBNotificationPrefix':cdspMIBNotificationPrefix,'cdspMIBNotifications':cdspMIBNotifications,_AK:cdspMIBCardStateNotification,_BW:cdspOperStateNotification,_BX:cdspVideoUsageNotification,_BY:cdspVideoOutOfResourceNotification,'cdspMgmtConformance':cdspMgmtConformance,'cdspMgmtCompliances':cdspMgmtCompliances,'cdspMgmtCompliance':cdspMgmtCompliance,'cdspMgmtComplianceRev1':cdspMgmtComplianceRev1,'cdspMgmtComplianceRev2':cdspMgmtComplianceRev2,'cdspMgmtComplianceRev3':cdspMgmtComplianceRev3,'cdspMgmtComplianceRev4':cdspMgmtComplianceRev4,'cdspMgmtComplianceRev5':cdspMgmtComplianceRev5,'cdspMgmtComplianceRev6':cdspMgmtComplianceRev6,'cdspMgmtComplianceRev7':cdspMgmtComplianceRev7,'cdspMgmtComplianceRev8':cdspMgmtComplianceRev8,'cdspMgmtComplianceRev9':cdspMgmtComplianceRev9,'cdspMgmtComplianceRev10':cdspMgmtComplianceRev10,'cdspMgmtComplianceRev11':cdspMgmtComplianceRev11,'cdspMgmtComplianceRev12':cdspMgmtComplianceRev12,'cdspMgmtGroups':cdspMgmtGroups,_V:cdspMgmtGeneralInfoGroup,_H:cdspChannelGroup,_AM:cdspMgmtExtGeneralInfoGroup,_BZ:cdspVoiceInfoGroup,_AL:cdspMgmtNotificationsGroup,_I:cdspChannelExtGroup,_n:cdspVoiceInfoGroupRev1,_K:cdspMgmtExtGeneralInfoGroupRev1,_L:cdspMgmtGeneralInfoGroupRev1,_M:cdspMgmtNotificationsGroupRev1,_N:cdspVQMGroup,_O:cdspVoiceInfoGroupRev2,_Ba:cdspTransCodingGroup,_S:cdspTransCodingGroup1,_W:cdspUtilInfoGroup,_o:cdspDspfarmInfoGroup,_AO:cdspMgmtVideoNotificationsGroup,_AN:cdspMgmtVideoInfoGroup,_Bd:cdspTranscodeProfileGroup,_Bb:cdspMtpProfileGroup,_Bc:cdspConferenceProfileGroup})