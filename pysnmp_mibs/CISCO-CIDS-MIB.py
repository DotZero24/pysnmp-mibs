_B9='ciscoCidsOptionalObjectGroupRev3'
_B8='ciscoCidsNotificationsGroupRev1'
_B7='ciscoCidsHealthObjectGroupRev1'
_B6='ciscoCidsAlertObjectGroupRev2'
_B5='ciscoCidsOptionalObjectGroup'
_B4='ciscoCidsAlertObjectGroup'
_B3='ciscoCidsGeneralObjectGroup'
_B2='ciscoCidsHealthMetricChange'
_B1='ciscoCidsHealthHeartBeat'
_B0='ciscoCidsError'
_A_='ciscoCidsAlert'
_Az='cidsAlertVirtualSensor'
_Ay='cidsHealthSecMonUtilizedPartitionSpace'
_Ax='cidsHealthSecMonTotalPartitionSpace'
_Aw='cidsHealthSecMonCollaborationAppStatus'
_Av='cidsHealthSecMonVirtSensorStatus'
_Au='cidsHealthSecMonSensorLoad'
_At='cidsHealthSecMonAnalysisEngMemPercent'
_As='cidsHealthSecMonMissedPktPctAndThresh'
_Ar='cidsHealthSecMonByPassMode'
_Aq='cidsHealthSecMonAnalysisEngineStatus'
_Ap='cidsHealthSecMonMainAppStatus'
_Ao='cidsHealthSecMonLicenseStatus'
_An='cidsHealthSecMonSignatureVersion'
_Am='cidsHealthSecMonSoftwareVersion'
_Al='cidsHealthSecMonAvailability'
_Ak='cidsAlertTcpOneWayResetSent'
_Aj='cidsAlertBlockHost'
_Ai='cidsAlertDenyPacket'
_Ah='cidsAlertRiskRatingWatchList'
_Ag='cidsAlertRiskRatingRelevance'
_Af='cidsAlertRiskRatingTargetValue'
_Ae='cidsAlertThreatValueRating'
_Ad='cidsHealthSensorStatsResetTime'
_Ac='cidsHealthCommandAndControlPort'
_Ab='cidsHealthIsSensorActive'
_Aa='cidsHealthIsSensorMemoryCritical'
_AZ='cidsHealthIpDualIp'
_AY='cidsHealthUdpDualIpAndPorts'
_AX='cidsHealthTcpDualIpAndPorts'
_AW='cidsHealthActiveNodes'
_AV='cidsHealthTcpStreams'
_AU='cidsHealthTcpClosingStreams'
_AT='cidsHealthTCPEstablishedStreams'
_AS='cidsHealthTcpEmbryonicStreams'
_AR='cidsHealthDatagramsInFRU'
_AQ='cidsHealthFragmentsInFRU'
_AP='cidsHealthAlarmsGenerated'
_AO='cidsHealthPacketDenialRate'
_AN='cidsHealthPacketLoss'
_AM='cidsHealthSecMonPartitionName'
_AL='not-accessible'
_AK='cidsHealthSecMonVirtSensorName'
_AJ='TruthValue'
_AI='ciscoCidsOptionalObjectGroupRev2'
_AH='cidsAlertDenyAttackSerReqNotPerf'
_AG='cidsAlertDenyAttackVicReqNotPerf'
_AF='cidsAlertDeniedAttackSericePair'
_AE='cidsAlertDeniedAttackVictimPair'
_AD='cidsAlertRateLimitRequested'
_AC='cidsAlertLogPairPacketsActivated'
_AB='cidsAlertLogVictimPacketsAct'
_AA='cidsAlertLogAttackerPacketsAct'
_A9='cidsAlertBlockConnectionReq'
_A8='cidsAlertDenyAttackerReqNotPerf'
_A7='cidsAlertDenyFlowReqNotPerf'
_A6='cidsAlertDenyPacketReqNotPerf'
_A5='cidsAlertDeniedFlow'
_A4='cidsAlertDeniedAttacker'
_A3='cidsAlertProtocol'
_A2='cidsAlertIfIndex'
_A1='cidsErrorMessage'
_A0='cidsErrorName'
_z='cidsErrorSeverity'
_y='cidsNotificationsEnabled'
_x='percent'
_w='Unsigned32'
_v='ciscoCidsOptionalObjectGroupRev1'
_u='cidsHealthSecMonSensorLoadColor'
_t='cidsHealthSecMonOverallAppColor'
_s='cidsHealthSecMonOverallHealth'
_r='cidsAlertAttackerAddress'
_q='cidsAlertVictimAddress'
_p='cidsAlertInterfaceGroup'
_o='cidsAlertSignatureSubSigId'
_n='cidsAlertSignatureSigId'
_m='cidsAlertSignatureSigName'
_l='cidsAlertAlarmTraits'
_k='cidsAlertSeverity'
_j='cidsGeneralOriginatorAppId'
_i='cidsGeneralOriginatorAppName'
_h='ciscoCidsNotificationsGroup'
_g='ciscoCidsAlertObjectGroupRev1'
_f='ciscoCidsGeneralObjectGroupRev1'
_e='cidsAlertEventRiskRating'
_d='cidsThreatResponseSeverity'
_c='cidsThreatResponseStatus'
_b='cidsAlertIpLogId'
_a='cidsAlertDetails'
_Z='cidsAlertShunRequested'
_Y='cidsAlertTcpResetSent'
_X='cidsAlertIpLoggingActivated'
_W='cidsAlertAttackerContext'
_V='cidsAlertVictimContext'
_U='cidsAlertVlan'
_T='cidsAlertSummaryInitialAlert'
_S='cidsAlertSummaryFinal'
_R='cidsAlertSummaryType'
_Q='cidsAlertSummary'
_P='cidsAlertSignatureVersion'
_O='cidsAlertSignature'
_N='ciscoCidsHealthObjectGroup'
_M='ciscoCidsErrorObjectGroup'
_L='SnmpAdminString'
_K='cidsGeneralOriginatorHostId'
_J='cidsGeneralUTCTime'
_I='cidsGeneralLocalTime'
_H='cidsGeneralEventId'
_G='DisplayString'
_F='Integer32'
_E='deprecated'
_D='read-only'
_C='accessible-for-notify'
_B='current'
_A='CISCO-CIDS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoIpProtocol,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoIpProtocol','Unsigned64')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_w,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention',_AJ)
ciscoCidsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,383))
if mibBuilder.loadTexts:ciscoCidsMIB.setRevisions(('2013-08-08 00:00','2008-06-26 00:00','2006-03-02 00:00','2005-10-10 00:00','2003-12-18 00:00'))
class CidsHealthStatusColor(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green',1),('yellow',2),('red',3)))
class CidsApplicationStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('notResponding',1),('notRunning',2),('processingTransaction',3),('reconfiguring',4),('running',5),('starting',6),('stopping',7),('unknown',8),('upgradeInprogress',9)))
class CidsErrorCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('errAuthenticationTokenExpired',1),('errConfigCollision',2),('errInUse',3),('errInvalidDocument',4),('errLimitExceeded',5),('errNotAvailable',6),('errNotFound',7),('errNotSupported',8),('errPermissionDenied',9),('errSyslog',10),('errSystemError',11),('errTransport',12),('errUnacceptableValue',13),('errUnclassified',14),('errWarning',15),('errEngineBuildFailed',16)))
class CidsTargetValue(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('zeroValue',1),('low',2),('medium',3),('high',4),('missionCritical',5)))
class CidsAttackRelevance(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('relevant',1),('notRelevant',2),('unknown',3)))
_CiscoCidsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCidsMIBNotifs=_CiscoCidsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,383,0))
_CiscoCidsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCidsMIBObjects=_CiscoCidsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,383,1))
_CidsGeneral_ObjectIdentity=ObjectIdentity
cidsGeneral=_CidsGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,383,1,1))
_CidsGeneralEventId_Type=Unsigned64
_CidsGeneralEventId_Object=MibScalar
cidsGeneralEventId=_CidsGeneralEventId_Object((1,3,6,1,4,1,9,9,383,1,1,1),_CidsGeneralEventId_Type())
cidsGeneralEventId.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsGeneralEventId.setStatus(_B)
_CidsGeneralLocalTime_Type=DateAndTime
_CidsGeneralLocalTime_Object=MibScalar
cidsGeneralLocalTime=_CidsGeneralLocalTime_Object((1,3,6,1,4,1,9,9,383,1,1,2),_CidsGeneralLocalTime_Type())
cidsGeneralLocalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsGeneralLocalTime.setStatus(_B)
_CidsGeneralUTCTime_Type=DateAndTime
_CidsGeneralUTCTime_Object=MibScalar
cidsGeneralUTCTime=_CidsGeneralUTCTime_Object((1,3,6,1,4,1,9,9,383,1,1,3),_CidsGeneralUTCTime_Type())
cidsGeneralUTCTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsGeneralUTCTime.setStatus(_B)
_CidsGeneralOriginatorHostId_Type=SnmpAdminString
_CidsGeneralOriginatorHostId_Object=MibScalar
cidsGeneralOriginatorHostId=_CidsGeneralOriginatorHostId_Object((1,3,6,1,4,1,9,9,383,1,1,4),_CidsGeneralOriginatorHostId_Type())
cidsGeneralOriginatorHostId.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsGeneralOriginatorHostId.setStatus(_B)
_CidsGeneralOriginatorAppName_Type=SnmpAdminString
_CidsGeneralOriginatorAppName_Object=MibScalar
cidsGeneralOriginatorAppName=_CidsGeneralOriginatorAppName_Object((1,3,6,1,4,1,9,9,383,1,1,5),_CidsGeneralOriginatorAppName_Type())
cidsGeneralOriginatorAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsGeneralOriginatorAppName.setStatus(_B)
_CidsGeneralOriginatorAppId_Type=SnmpAdminString
_CidsGeneralOriginatorAppId_Object=MibScalar
cidsGeneralOriginatorAppId=_CidsGeneralOriginatorAppId_Object((1,3,6,1,4,1,9,9,383,1,1,6),_CidsGeneralOriginatorAppId_Type())
cidsGeneralOriginatorAppId.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsGeneralOriginatorAppId.setStatus(_B)
class _CidsNotificationsEnabled_Type(TruthValue):defaultValue=2
_CidsNotificationsEnabled_Type.__name__=_AJ
_CidsNotificationsEnabled_Object=MibScalar
cidsNotificationsEnabled=_CidsNotificationsEnabled_Object((1,3,6,1,4,1,9,9,383,1,1,7),_CidsNotificationsEnabled_Type())
cidsNotificationsEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:cidsNotificationsEnabled.setStatus(_B)
_CidsAlert_ObjectIdentity=ObjectIdentity
cidsAlert=_CidsAlert_ObjectIdentity((1,3,6,1,4,1,9,9,383,1,2))
_CidsAlertSeverity_Type=SnmpAdminString
_CidsAlertSeverity_Object=MibScalar
cidsAlertSeverity=_CidsAlertSeverity_Object((1,3,6,1,4,1,9,9,383,1,2,1),_CidsAlertSeverity_Type())
cidsAlertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSeverity.setStatus(_B)
_CidsAlertAlarmTraits_Type=Unsigned32
_CidsAlertAlarmTraits_Object=MibScalar
cidsAlertAlarmTraits=_CidsAlertAlarmTraits_Object((1,3,6,1,4,1,9,9,383,1,2,2),_CidsAlertAlarmTraits_Type())
cidsAlertAlarmTraits.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertAlarmTraits.setStatus(_B)
class _CidsAlertSignature_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CidsAlertSignature_Type.__name__=_L
_CidsAlertSignature_Object=MibScalar
cidsAlertSignature=_CidsAlertSignature_Object((1,3,6,1,4,1,9,9,383,1,2,3),_CidsAlertSignature_Type())
cidsAlertSignature.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSignature.setStatus(_B)
class _CidsAlertSignatureSigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CidsAlertSignatureSigName_Type.__name__=_L
_CidsAlertSignatureSigName_Object=MibScalar
cidsAlertSignatureSigName=_CidsAlertSignatureSigName_Object((1,3,6,1,4,1,9,9,383,1,2,4),_CidsAlertSignatureSigName_Type())
cidsAlertSignatureSigName.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSignatureSigName.setStatus(_B)
_CidsAlertSignatureSigId_Type=Unsigned32
_CidsAlertSignatureSigId_Object=MibScalar
cidsAlertSignatureSigId=_CidsAlertSignatureSigId_Object((1,3,6,1,4,1,9,9,383,1,2,5),_CidsAlertSignatureSigId_Type())
cidsAlertSignatureSigId.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSignatureSigId.setStatus(_B)
_CidsAlertSignatureSubSigId_Type=Unsigned32
_CidsAlertSignatureSubSigId_Object=MibScalar
cidsAlertSignatureSubSigId=_CidsAlertSignatureSubSigId_Object((1,3,6,1,4,1,9,9,383,1,2,6),_CidsAlertSignatureSubSigId_Type())
cidsAlertSignatureSubSigId.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSignatureSubSigId.setStatus(_B)
class _CidsAlertSignatureVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CidsAlertSignatureVersion_Type.__name__=_L
_CidsAlertSignatureVersion_Object=MibScalar
cidsAlertSignatureVersion=_CidsAlertSignatureVersion_Object((1,3,6,1,4,1,9,9,383,1,2,7),_CidsAlertSignatureVersion_Type())
cidsAlertSignatureVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSignatureVersion.setStatus(_B)
_CidsAlertSummary_Type=Unsigned32
_CidsAlertSummary_Object=MibScalar
cidsAlertSummary=_CidsAlertSummary_Object((1,3,6,1,4,1,9,9,383,1,2,8),_CidsAlertSummary_Type())
cidsAlertSummary.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSummary.setStatus(_B)
class _CidsAlertSummaryType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CidsAlertSummaryType_Type.__name__=_L
_CidsAlertSummaryType_Object=MibScalar
cidsAlertSummaryType=_CidsAlertSummaryType_Object((1,3,6,1,4,1,9,9,383,1,2,9),_CidsAlertSummaryType_Type())
cidsAlertSummaryType.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSummaryType.setStatus(_B)
_CidsAlertSummaryFinal_Type=TruthValue
_CidsAlertSummaryFinal_Object=MibScalar
cidsAlertSummaryFinal=_CidsAlertSummaryFinal_Object((1,3,6,1,4,1,9,9,383,1,2,10),_CidsAlertSummaryFinal_Type())
cidsAlertSummaryFinal.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSummaryFinal.setStatus(_B)
_CidsAlertSummaryInitialAlert_Type=Unsigned64
_CidsAlertSummaryInitialAlert_Object=MibScalar
cidsAlertSummaryInitialAlert=_CidsAlertSummaryInitialAlert_Object((1,3,6,1,4,1,9,9,383,1,2,11),_CidsAlertSummaryInitialAlert_Type())
cidsAlertSummaryInitialAlert.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertSummaryInitialAlert.setStatus(_B)
class _CidsAlertInterfaceGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CidsAlertInterfaceGroup_Type.__name__=_F
_CidsAlertInterfaceGroup_Object=MibScalar
cidsAlertInterfaceGroup=_CidsAlertInterfaceGroup_Object((1,3,6,1,4,1,9,9,383,1,2,12),_CidsAlertInterfaceGroup_Type())
cidsAlertInterfaceGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertInterfaceGroup.setStatus(_E)
class _CidsAlertVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CidsAlertVlan_Type.__name__=_w
_CidsAlertVlan_Object=MibScalar
cidsAlertVlan=_CidsAlertVlan_Object((1,3,6,1,4,1,9,9,383,1,2,13),_CidsAlertVlan_Type())
cidsAlertVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertVlan.setStatus(_B)
_CidsAlertVictimContext_Type=SnmpAdminString
_CidsAlertVictimContext_Object=MibScalar
cidsAlertVictimContext=_CidsAlertVictimContext_Object((1,3,6,1,4,1,9,9,383,1,2,14),_CidsAlertVictimContext_Type())
cidsAlertVictimContext.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertVictimContext.setStatus(_B)
_CidsAlertAttackerContext_Type=SnmpAdminString
_CidsAlertAttackerContext_Object=MibScalar
cidsAlertAttackerContext=_CidsAlertAttackerContext_Object((1,3,6,1,4,1,9,9,383,1,2,15),_CidsAlertAttackerContext_Type())
cidsAlertAttackerContext.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertAttackerContext.setStatus(_B)
_CidsAlertAttackerAddress_Type=SnmpAdminString
_CidsAlertAttackerAddress_Object=MibScalar
cidsAlertAttackerAddress=_CidsAlertAttackerAddress_Object((1,3,6,1,4,1,9,9,383,1,2,16),_CidsAlertAttackerAddress_Type())
cidsAlertAttackerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertAttackerAddress.setStatus(_B)
_CidsAlertVictimAddress_Type=SnmpAdminString
_CidsAlertVictimAddress_Object=MibScalar
cidsAlertVictimAddress=_CidsAlertVictimAddress_Object((1,3,6,1,4,1,9,9,383,1,2,17),_CidsAlertVictimAddress_Type())
cidsAlertVictimAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertVictimAddress.setStatus(_B)
_CidsAlertIpLoggingActivated_Type=TruthValue
_CidsAlertIpLoggingActivated_Object=MibScalar
cidsAlertIpLoggingActivated=_CidsAlertIpLoggingActivated_Object((1,3,6,1,4,1,9,9,383,1,2,18),_CidsAlertIpLoggingActivated_Type())
cidsAlertIpLoggingActivated.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertIpLoggingActivated.setStatus(_B)
_CidsAlertTcpResetSent_Type=TruthValue
_CidsAlertTcpResetSent_Object=MibScalar
cidsAlertTcpResetSent=_CidsAlertTcpResetSent_Object((1,3,6,1,4,1,9,9,383,1,2,19),_CidsAlertTcpResetSent_Type())
cidsAlertTcpResetSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertTcpResetSent.setStatus(_B)
_CidsAlertShunRequested_Type=TruthValue
_CidsAlertShunRequested_Object=MibScalar
cidsAlertShunRequested=_CidsAlertShunRequested_Object((1,3,6,1,4,1,9,9,383,1,2,20),_CidsAlertShunRequested_Type())
cidsAlertShunRequested.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertShunRequested.setStatus(_B)
_CidsAlertDetails_Type=SnmpAdminString
_CidsAlertDetails_Object=MibScalar
cidsAlertDetails=_CidsAlertDetails_Object((1,3,6,1,4,1,9,9,383,1,2,21),_CidsAlertDetails_Type())
cidsAlertDetails.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDetails.setStatus(_B)
_CidsAlertIpLogId_Type=SnmpAdminString
_CidsAlertIpLogId_Object=MibScalar
cidsAlertIpLogId=_CidsAlertIpLogId_Object((1,3,6,1,4,1,9,9,383,1,2,22),_CidsAlertIpLogId_Type())
cidsAlertIpLogId.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertIpLogId.setStatus(_B)
_CidsThreatResponseStatus_Type=SnmpAdminString
_CidsThreatResponseStatus_Object=MibScalar
cidsThreatResponseStatus=_CidsThreatResponseStatus_Object((1,3,6,1,4,1,9,9,383,1,2,23),_CidsThreatResponseStatus_Type())
cidsThreatResponseStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsThreatResponseStatus.setStatus(_B)
class _CidsThreatResponseSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CidsThreatResponseSeverity_Type.__name__=_F
_CidsThreatResponseSeverity_Object=MibScalar
cidsThreatResponseSeverity=_CidsThreatResponseSeverity_Object((1,3,6,1,4,1,9,9,383,1,2,24),_CidsThreatResponseSeverity_Type())
cidsThreatResponseSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsThreatResponseSeverity.setStatus(_B)
_CidsAlertEventRiskRating_Type=Unsigned32
_CidsAlertEventRiskRating_Object=MibScalar
cidsAlertEventRiskRating=_CidsAlertEventRiskRating_Object((1,3,6,1,4,1,9,9,383,1,2,25),_CidsAlertEventRiskRating_Type())
cidsAlertEventRiskRating.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertEventRiskRating.setStatus(_B)
_CidsAlertIfIndex_Type=InterfaceIndex
_CidsAlertIfIndex_Object=MibScalar
cidsAlertIfIndex=_CidsAlertIfIndex_Object((1,3,6,1,4,1,9,9,383,1,2,26),_CidsAlertIfIndex_Type())
cidsAlertIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertIfIndex.setStatus(_B)
_CidsAlertProtocol_Type=CiscoIpProtocol
_CidsAlertProtocol_Object=MibScalar
cidsAlertProtocol=_CidsAlertProtocol_Object((1,3,6,1,4,1,9,9,383,1,2,27),_CidsAlertProtocol_Type())
cidsAlertProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertProtocol.setStatus(_B)
_CidsAlertDeniedAttacker_Type=TruthValue
_CidsAlertDeniedAttacker_Object=MibScalar
cidsAlertDeniedAttacker=_CidsAlertDeniedAttacker_Object((1,3,6,1,4,1,9,9,383,1,2,28),_CidsAlertDeniedAttacker_Type())
cidsAlertDeniedAttacker.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDeniedAttacker.setStatus(_B)
_CidsAlertDeniedFlow_Type=TruthValue
_CidsAlertDeniedFlow_Object=MibScalar
cidsAlertDeniedFlow=_CidsAlertDeniedFlow_Object((1,3,6,1,4,1,9,9,383,1,2,29),_CidsAlertDeniedFlow_Type())
cidsAlertDeniedFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDeniedFlow.setStatus(_B)
_CidsAlertDenyPacketReqNotPerf_Type=TruthValue
_CidsAlertDenyPacketReqNotPerf_Object=MibScalar
cidsAlertDenyPacketReqNotPerf=_CidsAlertDenyPacketReqNotPerf_Object((1,3,6,1,4,1,9,9,383,1,2,30),_CidsAlertDenyPacketReqNotPerf_Type())
cidsAlertDenyPacketReqNotPerf.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDenyPacketReqNotPerf.setStatus(_B)
_CidsAlertDenyFlowReqNotPerf_Type=TruthValue
_CidsAlertDenyFlowReqNotPerf_Object=MibScalar
cidsAlertDenyFlowReqNotPerf=_CidsAlertDenyFlowReqNotPerf_Object((1,3,6,1,4,1,9,9,383,1,2,31),_CidsAlertDenyFlowReqNotPerf_Type())
cidsAlertDenyFlowReqNotPerf.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDenyFlowReqNotPerf.setStatus(_B)
_CidsAlertDenyAttackerReqNotPerf_Type=TruthValue
_CidsAlertDenyAttackerReqNotPerf_Object=MibScalar
cidsAlertDenyAttackerReqNotPerf=_CidsAlertDenyAttackerReqNotPerf_Object((1,3,6,1,4,1,9,9,383,1,2,32),_CidsAlertDenyAttackerReqNotPerf_Type())
cidsAlertDenyAttackerReqNotPerf.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDenyAttackerReqNotPerf.setStatus(_B)
_CidsAlertBlockConnectionReq_Type=TruthValue
_CidsAlertBlockConnectionReq_Object=MibScalar
cidsAlertBlockConnectionReq=_CidsAlertBlockConnectionReq_Object((1,3,6,1,4,1,9,9,383,1,2,33),_CidsAlertBlockConnectionReq_Type())
cidsAlertBlockConnectionReq.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertBlockConnectionReq.setStatus(_B)
_CidsAlertLogAttackerPacketsAct_Type=TruthValue
_CidsAlertLogAttackerPacketsAct_Object=MibScalar
cidsAlertLogAttackerPacketsAct=_CidsAlertLogAttackerPacketsAct_Object((1,3,6,1,4,1,9,9,383,1,2,34),_CidsAlertLogAttackerPacketsAct_Type())
cidsAlertLogAttackerPacketsAct.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertLogAttackerPacketsAct.setStatus(_B)
_CidsAlertLogVictimPacketsAct_Type=TruthValue
_CidsAlertLogVictimPacketsAct_Object=MibScalar
cidsAlertLogVictimPacketsAct=_CidsAlertLogVictimPacketsAct_Object((1,3,6,1,4,1,9,9,383,1,2,35),_CidsAlertLogVictimPacketsAct_Type())
cidsAlertLogVictimPacketsAct.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertLogVictimPacketsAct.setStatus(_B)
_CidsAlertLogPairPacketsActivated_Type=TruthValue
_CidsAlertLogPairPacketsActivated_Object=MibScalar
cidsAlertLogPairPacketsActivated=_CidsAlertLogPairPacketsActivated_Object((1,3,6,1,4,1,9,9,383,1,2,36),_CidsAlertLogPairPacketsActivated_Type())
cidsAlertLogPairPacketsActivated.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertLogPairPacketsActivated.setStatus(_B)
_CidsAlertRateLimitRequested_Type=TruthValue
_CidsAlertRateLimitRequested_Object=MibScalar
cidsAlertRateLimitRequested=_CidsAlertRateLimitRequested_Object((1,3,6,1,4,1,9,9,383,1,2,37),_CidsAlertRateLimitRequested_Type())
cidsAlertRateLimitRequested.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertRateLimitRequested.setStatus(_B)
_CidsAlertDeniedAttackVictimPair_Type=TruthValue
_CidsAlertDeniedAttackVictimPair_Object=MibScalar
cidsAlertDeniedAttackVictimPair=_CidsAlertDeniedAttackVictimPair_Object((1,3,6,1,4,1,9,9,383,1,2,38),_CidsAlertDeniedAttackVictimPair_Type())
cidsAlertDeniedAttackVictimPair.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDeniedAttackVictimPair.setStatus(_B)
_CidsAlertDeniedAttackSericePair_Type=TruthValue
_CidsAlertDeniedAttackSericePair_Object=MibScalar
cidsAlertDeniedAttackSericePair=_CidsAlertDeniedAttackSericePair_Object((1,3,6,1,4,1,9,9,383,1,2,39),_CidsAlertDeniedAttackSericePair_Type())
cidsAlertDeniedAttackSericePair.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDeniedAttackSericePair.setStatus(_B)
_CidsAlertDenyAttackVicReqNotPerf_Type=TruthValue
_CidsAlertDenyAttackVicReqNotPerf_Object=MibScalar
cidsAlertDenyAttackVicReqNotPerf=_CidsAlertDenyAttackVicReqNotPerf_Object((1,3,6,1,4,1,9,9,383,1,2,40),_CidsAlertDenyAttackVicReqNotPerf_Type())
cidsAlertDenyAttackVicReqNotPerf.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDenyAttackVicReqNotPerf.setStatus(_B)
_CidsAlertDenyAttackSerReqNotPerf_Type=TruthValue
_CidsAlertDenyAttackSerReqNotPerf_Object=MibScalar
cidsAlertDenyAttackSerReqNotPerf=_CidsAlertDenyAttackSerReqNotPerf_Object((1,3,6,1,4,1,9,9,383,1,2,41),_CidsAlertDenyAttackSerReqNotPerf_Type())
cidsAlertDenyAttackSerReqNotPerf.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDenyAttackSerReqNotPerf.setStatus(_B)
_CidsAlertThreatValueRating_Type=Unsigned32
_CidsAlertThreatValueRating_Object=MibScalar
cidsAlertThreatValueRating=_CidsAlertThreatValueRating_Object((1,3,6,1,4,1,9,9,383,1,2,42),_CidsAlertThreatValueRating_Type())
cidsAlertThreatValueRating.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertThreatValueRating.setStatus(_B)
_CidsAlertRiskRatingTargetValue_Type=CidsTargetValue
_CidsAlertRiskRatingTargetValue_Object=MibScalar
cidsAlertRiskRatingTargetValue=_CidsAlertRiskRatingTargetValue_Object((1,3,6,1,4,1,9,9,383,1,2,43),_CidsAlertRiskRatingTargetValue_Type())
cidsAlertRiskRatingTargetValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertRiskRatingTargetValue.setStatus(_B)
_CidsAlertRiskRatingRelevance_Type=CidsAttackRelevance
_CidsAlertRiskRatingRelevance_Object=MibScalar
cidsAlertRiskRatingRelevance=_CidsAlertRiskRatingRelevance_Object((1,3,6,1,4,1,9,9,383,1,2,44),_CidsAlertRiskRatingRelevance_Type())
cidsAlertRiskRatingRelevance.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertRiskRatingRelevance.setStatus(_B)
_CidsAlertRiskRatingWatchList_Type=Unsigned32
_CidsAlertRiskRatingWatchList_Object=MibScalar
cidsAlertRiskRatingWatchList=_CidsAlertRiskRatingWatchList_Object((1,3,6,1,4,1,9,9,383,1,2,45),_CidsAlertRiskRatingWatchList_Type())
cidsAlertRiskRatingWatchList.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertRiskRatingWatchList.setStatus(_B)
_CidsAlertDenyPacket_Type=TruthValue
_CidsAlertDenyPacket_Object=MibScalar
cidsAlertDenyPacket=_CidsAlertDenyPacket_Object((1,3,6,1,4,1,9,9,383,1,2,46),_CidsAlertDenyPacket_Type())
cidsAlertDenyPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertDenyPacket.setStatus(_B)
_CidsAlertBlockHost_Type=TruthValue
_CidsAlertBlockHost_Object=MibScalar
cidsAlertBlockHost=_CidsAlertBlockHost_Object((1,3,6,1,4,1,9,9,383,1,2,47),_CidsAlertBlockHost_Type())
cidsAlertBlockHost.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertBlockHost.setStatus(_B)
_CidsAlertTcpOneWayResetSent_Type=TruthValue
_CidsAlertTcpOneWayResetSent_Object=MibScalar
cidsAlertTcpOneWayResetSent=_CidsAlertTcpOneWayResetSent_Object((1,3,6,1,4,1,9,9,383,1,2,48),_CidsAlertTcpOneWayResetSent_Type())
cidsAlertTcpOneWayResetSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertTcpOneWayResetSent.setStatus(_B)
class _CidsAlertVirtualSensor_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CidsAlertVirtualSensor_Type.__name__=_L
_CidsAlertVirtualSensor_Object=MibScalar
cidsAlertVirtualSensor=_CidsAlertVirtualSensor_Object((1,3,6,1,4,1,9,9,383,1,2,49),_CidsAlertVirtualSensor_Type())
cidsAlertVirtualSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsAlertVirtualSensor.setStatus(_B)
_CidsError_ObjectIdentity=ObjectIdentity
cidsError=_CidsError_ObjectIdentity((1,3,6,1,4,1,9,9,383,1,3))
_CidsErrorSeverity_Type=SnmpAdminString
_CidsErrorSeverity_Object=MibScalar
cidsErrorSeverity=_CidsErrorSeverity_Object((1,3,6,1,4,1,9,9,383,1,3,1),_CidsErrorSeverity_Type())
cidsErrorSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsErrorSeverity.setStatus(_B)
_CidsErrorName_Type=CidsErrorCode
_CidsErrorName_Object=MibScalar
cidsErrorName=_CidsErrorName_Object((1,3,6,1,4,1,9,9,383,1,3,2),_CidsErrorName_Type())
cidsErrorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsErrorName.setStatus(_B)
_CidsErrorMessage_Type=SnmpAdminString
_CidsErrorMessage_Object=MibScalar
cidsErrorMessage=_CidsErrorMessage_Object((1,3,6,1,4,1,9,9,383,1,3,3),_CidsErrorMessage_Type())
cidsErrorMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsErrorMessage.setStatus(_B)
_CidsHealth_ObjectIdentity=ObjectIdentity
cidsHealth=_CidsHealth_ObjectIdentity((1,3,6,1,4,1,9,9,383,1,4))
class _CidsHealthPacketLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CidsHealthPacketLoss_Type.__name__=_F
_CidsHealthPacketLoss_Object=MibScalar
cidsHealthPacketLoss=_CidsHealthPacketLoss_Object((1,3,6,1,4,1,9,9,383,1,4,1),_CidsHealthPacketLoss_Type())
cidsHealthPacketLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthPacketLoss.setStatus(_B)
if mibBuilder.loadTexts:cidsHealthPacketLoss.setUnits(_x)
class _CidsHealthPacketDenialRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CidsHealthPacketDenialRate_Type.__name__=_F
_CidsHealthPacketDenialRate_Object=MibScalar
cidsHealthPacketDenialRate=_CidsHealthPacketDenialRate_Object((1,3,6,1,4,1,9,9,383,1,4,2),_CidsHealthPacketDenialRate_Type())
cidsHealthPacketDenialRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthPacketDenialRate.setStatus(_B)
if mibBuilder.loadTexts:cidsHealthPacketDenialRate.setUnits(_x)
_CidsHealthAlarmsGenerated_Type=Counter32
_CidsHealthAlarmsGenerated_Object=MibScalar
cidsHealthAlarmsGenerated=_CidsHealthAlarmsGenerated_Object((1,3,6,1,4,1,9,9,383,1,4,3),_CidsHealthAlarmsGenerated_Type())
cidsHealthAlarmsGenerated.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthAlarmsGenerated.setStatus(_B)
_CidsHealthFragmentsInFRU_Type=Gauge32
_CidsHealthFragmentsInFRU_Object=MibScalar
cidsHealthFragmentsInFRU=_CidsHealthFragmentsInFRU_Object((1,3,6,1,4,1,9,9,383,1,4,4),_CidsHealthFragmentsInFRU_Type())
cidsHealthFragmentsInFRU.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthFragmentsInFRU.setStatus(_B)
_CidsHealthDatagramsInFRU_Type=Gauge32
_CidsHealthDatagramsInFRU_Object=MibScalar
cidsHealthDatagramsInFRU=_CidsHealthDatagramsInFRU_Object((1,3,6,1,4,1,9,9,383,1,4,5),_CidsHealthDatagramsInFRU_Type())
cidsHealthDatagramsInFRU.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthDatagramsInFRU.setStatus(_B)
_CidsHealthTcpEmbryonicStreams_Type=Gauge32
_CidsHealthTcpEmbryonicStreams_Object=MibScalar
cidsHealthTcpEmbryonicStreams=_CidsHealthTcpEmbryonicStreams_Object((1,3,6,1,4,1,9,9,383,1,4,6),_CidsHealthTcpEmbryonicStreams_Type())
cidsHealthTcpEmbryonicStreams.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthTcpEmbryonicStreams.setStatus(_B)
_CidsHealthTCPEstablishedStreams_Type=Gauge32
_CidsHealthTCPEstablishedStreams_Object=MibScalar
cidsHealthTCPEstablishedStreams=_CidsHealthTCPEstablishedStreams_Object((1,3,6,1,4,1,9,9,383,1,4,7),_CidsHealthTCPEstablishedStreams_Type())
cidsHealthTCPEstablishedStreams.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthTCPEstablishedStreams.setStatus(_B)
_CidsHealthTcpClosingStreams_Type=Gauge32
_CidsHealthTcpClosingStreams_Object=MibScalar
cidsHealthTcpClosingStreams=_CidsHealthTcpClosingStreams_Object((1,3,6,1,4,1,9,9,383,1,4,8),_CidsHealthTcpClosingStreams_Type())
cidsHealthTcpClosingStreams.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthTcpClosingStreams.setStatus(_B)
_CidsHealthTcpStreams_Type=Gauge32
_CidsHealthTcpStreams_Object=MibScalar
cidsHealthTcpStreams=_CidsHealthTcpStreams_Object((1,3,6,1,4,1,9,9,383,1,4,9),_CidsHealthTcpStreams_Type())
cidsHealthTcpStreams.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthTcpStreams.setStatus(_B)
_CidsHealthActiveNodes_Type=Gauge32
_CidsHealthActiveNodes_Object=MibScalar
cidsHealthActiveNodes=_CidsHealthActiveNodes_Object((1,3,6,1,4,1,9,9,383,1,4,10),_CidsHealthActiveNodes_Type())
cidsHealthActiveNodes.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthActiveNodes.setStatus(_B)
_CidsHealthTcpDualIpAndPorts_Type=Gauge32
_CidsHealthTcpDualIpAndPorts_Object=MibScalar
cidsHealthTcpDualIpAndPorts=_CidsHealthTcpDualIpAndPorts_Object((1,3,6,1,4,1,9,9,383,1,4,11),_CidsHealthTcpDualIpAndPorts_Type())
cidsHealthTcpDualIpAndPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthTcpDualIpAndPorts.setStatus(_B)
_CidsHealthUdpDualIpAndPorts_Type=Gauge32
_CidsHealthUdpDualIpAndPorts_Object=MibScalar
cidsHealthUdpDualIpAndPorts=_CidsHealthUdpDualIpAndPorts_Object((1,3,6,1,4,1,9,9,383,1,4,12),_CidsHealthUdpDualIpAndPorts_Type())
cidsHealthUdpDualIpAndPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthUdpDualIpAndPorts.setStatus(_B)
_CidsHealthIpDualIp_Type=Gauge32
_CidsHealthIpDualIp_Object=MibScalar
cidsHealthIpDualIp=_CidsHealthIpDualIp_Object((1,3,6,1,4,1,9,9,383,1,4,13),_CidsHealthIpDualIp_Type())
cidsHealthIpDualIp.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthIpDualIp.setStatus(_B)
class _CidsHealthIsSensorMemoryCritical_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CidsHealthIsSensorMemoryCritical_Type.__name__=_w
_CidsHealthIsSensorMemoryCritical_Object=MibScalar
cidsHealthIsSensorMemoryCritical=_CidsHealthIsSensorMemoryCritical_Object((1,3,6,1,4,1,9,9,383,1,4,14),_CidsHealthIsSensorMemoryCritical_Type())
cidsHealthIsSensorMemoryCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthIsSensorMemoryCritical.setStatus(_B)
_CidsHealthIsSensorActive_Type=TruthValue
_CidsHealthIsSensorActive_Object=MibScalar
cidsHealthIsSensorActive=_CidsHealthIsSensorActive_Object((1,3,6,1,4,1,9,9,383,1,4,15),_CidsHealthIsSensorActive_Type())
cidsHealthIsSensorActive.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthIsSensorActive.setStatus(_B)
_CidsHealthCommandAndControlPort_Type=SnmpAdminString
_CidsHealthCommandAndControlPort_Object=MibScalar
cidsHealthCommandAndControlPort=_CidsHealthCommandAndControlPort_Object((1,3,6,1,4,1,9,9,383,1,4,16),_CidsHealthCommandAndControlPort_Type())
cidsHealthCommandAndControlPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthCommandAndControlPort.setStatus(_B)
_CidsHealthSensorStatsResetTime_Type=TimeTicks
_CidsHealthSensorStatsResetTime_Object=MibScalar
cidsHealthSensorStatsResetTime=_CidsHealthSensorStatsResetTime_Object((1,3,6,1,4,1,9,9,383,1,4,17),_CidsHealthSensorStatsResetTime_Type())
cidsHealthSensorStatsResetTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSensorStatsResetTime.setStatus(_B)
_CidsHealthSecMonAvailability_Type=TruthValue
_CidsHealthSecMonAvailability_Object=MibScalar
cidsHealthSecMonAvailability=_CidsHealthSecMonAvailability_Object((1,3,6,1,4,1,9,9,383,1,4,18),_CidsHealthSecMonAvailability_Type())
cidsHealthSecMonAvailability.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonAvailability.setStatus(_B)
_CidsHealthSecMonOverallHealth_Type=CidsHealthStatusColor
_CidsHealthSecMonOverallHealth_Object=MibScalar
cidsHealthSecMonOverallHealth=_CidsHealthSecMonOverallHealth_Object((1,3,6,1,4,1,9,9,383,1,4,19),_CidsHealthSecMonOverallHealth_Type())
cidsHealthSecMonOverallHealth.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonOverallHealth.setStatus(_B)
class _CidsHealthSecMonSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CidsHealthSecMonSoftwareVersion_Type.__name__=_G
_CidsHealthSecMonSoftwareVersion_Object=MibScalar
cidsHealthSecMonSoftwareVersion=_CidsHealthSecMonSoftwareVersion_Object((1,3,6,1,4,1,9,9,383,1,4,20),_CidsHealthSecMonSoftwareVersion_Type())
cidsHealthSecMonSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonSoftwareVersion.setStatus(_B)
class _CidsHealthSecMonSignatureVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CidsHealthSecMonSignatureVersion_Type.__name__=_G
_CidsHealthSecMonSignatureVersion_Object=MibScalar
cidsHealthSecMonSignatureVersion=_CidsHealthSecMonSignatureVersion_Object((1,3,6,1,4,1,9,9,383,1,4,21),_CidsHealthSecMonSignatureVersion_Type())
cidsHealthSecMonSignatureVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonSignatureVersion.setStatus(_B)
class _CidsHealthSecMonLicenseStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CidsHealthSecMonLicenseStatus_Type.__name__=_G
_CidsHealthSecMonLicenseStatus_Object=MibScalar
cidsHealthSecMonLicenseStatus=_CidsHealthSecMonLicenseStatus_Object((1,3,6,1,4,1,9,9,383,1,4,22),_CidsHealthSecMonLicenseStatus_Type())
cidsHealthSecMonLicenseStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonLicenseStatus.setStatus(_B)
_CidsHealthSecMonOverallAppColor_Type=CidsHealthStatusColor
_CidsHealthSecMonOverallAppColor_Object=MibScalar
cidsHealthSecMonOverallAppColor=_CidsHealthSecMonOverallAppColor_Object((1,3,6,1,4,1,9,9,383,1,4,23),_CidsHealthSecMonOverallAppColor_Type())
cidsHealthSecMonOverallAppColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsHealthSecMonOverallAppColor.setStatus(_B)
_CidsHealthSecMonMainAppStatus_Type=CidsApplicationStatus
_CidsHealthSecMonMainAppStatus_Object=MibScalar
cidsHealthSecMonMainAppStatus=_CidsHealthSecMonMainAppStatus_Object((1,3,6,1,4,1,9,9,383,1,4,24),_CidsHealthSecMonMainAppStatus_Type())
cidsHealthSecMonMainAppStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonMainAppStatus.setStatus(_B)
_CidsHealthSecMonAnalysisEngineStatus_Type=CidsApplicationStatus
_CidsHealthSecMonAnalysisEngineStatus_Object=MibScalar
cidsHealthSecMonAnalysisEngineStatus=_CidsHealthSecMonAnalysisEngineStatus_Object((1,3,6,1,4,1,9,9,383,1,4,25),_CidsHealthSecMonAnalysisEngineStatus_Type())
cidsHealthSecMonAnalysisEngineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonAnalysisEngineStatus.setStatus(_B)
_CidsHealthSecMonCollaborationAppStatus_Type=CidsApplicationStatus
_CidsHealthSecMonCollaborationAppStatus_Object=MibScalar
cidsHealthSecMonCollaborationAppStatus=_CidsHealthSecMonCollaborationAppStatus_Object((1,3,6,1,4,1,9,9,383,1,4,26),_CidsHealthSecMonCollaborationAppStatus_Type())
cidsHealthSecMonCollaborationAppStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonCollaborationAppStatus.setStatus(_B)
_CidsHealthSecMonByPassMode_Type=TruthValue
_CidsHealthSecMonByPassMode_Object=MibScalar
cidsHealthSecMonByPassMode=_CidsHealthSecMonByPassMode_Object((1,3,6,1,4,1,9,9,383,1,4,27),_CidsHealthSecMonByPassMode_Type())
cidsHealthSecMonByPassMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsHealthSecMonByPassMode.setStatus(_B)
class _CidsHealthSecMonMissedPktPctAndThresh_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CidsHealthSecMonMissedPktPctAndThresh_Type.__name__=_G
_CidsHealthSecMonMissedPktPctAndThresh_Object=MibScalar
cidsHealthSecMonMissedPktPctAndThresh=_CidsHealthSecMonMissedPktPctAndThresh_Object((1,3,6,1,4,1,9,9,383,1,4,28),_CidsHealthSecMonMissedPktPctAndThresh_Type())
cidsHealthSecMonMissedPktPctAndThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonMissedPktPctAndThresh.setStatus(_B)
class _CidsHealthSecMonAnalysisEngMemPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CidsHealthSecMonAnalysisEngMemPercent_Type.__name__=_F
_CidsHealthSecMonAnalysisEngMemPercent_Object=MibScalar
cidsHealthSecMonAnalysisEngMemPercent=_CidsHealthSecMonAnalysisEngMemPercent_Object((1,3,6,1,4,1,9,9,383,1,4,29),_CidsHealthSecMonAnalysisEngMemPercent_Type())
cidsHealthSecMonAnalysisEngMemPercent.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonAnalysisEngMemPercent.setStatus(_B)
if mibBuilder.loadTexts:cidsHealthSecMonAnalysisEngMemPercent.setUnits(_x)
class _CidsHealthSecMonSensorLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CidsHealthSecMonSensorLoad_Type.__name__=_F
_CidsHealthSecMonSensorLoad_Object=MibScalar
cidsHealthSecMonSensorLoad=_CidsHealthSecMonSensorLoad_Object((1,3,6,1,4,1,9,9,383,1,4,30),_CidsHealthSecMonSensorLoad_Type())
cidsHealthSecMonSensorLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonSensorLoad.setStatus(_B)
_CidsHealthSecMonSensorLoadColor_Type=CidsHealthStatusColor
_CidsHealthSecMonSensorLoadColor_Object=MibScalar
cidsHealthSecMonSensorLoadColor=_CidsHealthSecMonSensorLoadColor_Object((1,3,6,1,4,1,9,9,383,1,4,31),_CidsHealthSecMonSensorLoadColor_Type())
cidsHealthSecMonSensorLoadColor.setMaxAccess(_C)
if mibBuilder.loadTexts:cidsHealthSecMonSensorLoadColor.setStatus(_B)
_CidsHealthSecMonVirtSensorStatusTable_Object=MibTable
cidsHealthSecMonVirtSensorStatusTable=_CidsHealthSecMonVirtSensorStatusTable_Object((1,3,6,1,4,1,9,9,383,1,4,32))
if mibBuilder.loadTexts:cidsHealthSecMonVirtSensorStatusTable.setStatus(_B)
_CidsHealthSecMonVirtSensorStatusEntry_Object=MibTableRow
cidsHealthSecMonVirtSensorStatusEntry=_CidsHealthSecMonVirtSensorStatusEntry_Object((1,3,6,1,4,1,9,9,383,1,4,32,1))
cidsHealthSecMonVirtSensorStatusEntry.setIndexNames((0,_A,_AK))
if mibBuilder.loadTexts:cidsHealthSecMonVirtSensorStatusEntry.setStatus(_B)
class _CidsHealthSecMonVirtSensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CidsHealthSecMonVirtSensorName_Type.__name__=_G
_CidsHealthSecMonVirtSensorName_Object=MibTableColumn
cidsHealthSecMonVirtSensorName=_CidsHealthSecMonVirtSensorName_Object((1,3,6,1,4,1,9,9,383,1,4,32,1,1),_CidsHealthSecMonVirtSensorName_Type())
cidsHealthSecMonVirtSensorName.setMaxAccess(_AL)
if mibBuilder.loadTexts:cidsHealthSecMonVirtSensorName.setStatus(_B)
_CidsHealthSecMonVirtSensorStatus_Type=CidsHealthStatusColor
_CidsHealthSecMonVirtSensorStatus_Object=MibTableColumn
cidsHealthSecMonVirtSensorStatus=_CidsHealthSecMonVirtSensorStatus_Object((1,3,6,1,4,1,9,9,383,1,4,32,1,2),_CidsHealthSecMonVirtSensorStatus_Type())
cidsHealthSecMonVirtSensorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonVirtSensorStatus.setStatus(_B)
_CidsHealthSecMonDataStorageTable_Object=MibTable
cidsHealthSecMonDataStorageTable=_CidsHealthSecMonDataStorageTable_Object((1,3,6,1,4,1,9,9,383,1,4,33))
if mibBuilder.loadTexts:cidsHealthSecMonDataStorageTable.setStatus(_B)
_CidsHealthSecMonDataStorageEntry_Object=MibTableRow
cidsHealthSecMonDataStorageEntry=_CidsHealthSecMonDataStorageEntry_Object((1,3,6,1,4,1,9,9,383,1,4,33,1))
cidsHealthSecMonDataStorageEntry.setIndexNames((0,_A,_AM))
if mibBuilder.loadTexts:cidsHealthSecMonDataStorageEntry.setStatus(_B)
class _CidsHealthSecMonPartitionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CidsHealthSecMonPartitionName_Type.__name__=_G
_CidsHealthSecMonPartitionName_Object=MibTableColumn
cidsHealthSecMonPartitionName=_CidsHealthSecMonPartitionName_Object((1,3,6,1,4,1,9,9,383,1,4,33,1,1),_CidsHealthSecMonPartitionName_Type())
cidsHealthSecMonPartitionName.setMaxAccess(_AL)
if mibBuilder.loadTexts:cidsHealthSecMonPartitionName.setStatus(_B)
_CidsHealthSecMonTotalPartitionSpace_Type=Unsigned32
_CidsHealthSecMonTotalPartitionSpace_Object=MibTableColumn
cidsHealthSecMonTotalPartitionSpace=_CidsHealthSecMonTotalPartitionSpace_Object((1,3,6,1,4,1,9,9,383,1,4,33,1,2),_CidsHealthSecMonTotalPartitionSpace_Type())
cidsHealthSecMonTotalPartitionSpace.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonTotalPartitionSpace.setStatus(_B)
if mibBuilder.loadTexts:cidsHealthSecMonTotalPartitionSpace.setUnits('MB')
_CidsHealthSecMonUtilizedPartitionSpace_Type=Unsigned32
_CidsHealthSecMonUtilizedPartitionSpace_Object=MibTableColumn
cidsHealthSecMonUtilizedPartitionSpace=_CidsHealthSecMonUtilizedPartitionSpace_Object((1,3,6,1,4,1,9,9,383,1,4,33,1,3),_CidsHealthSecMonUtilizedPartitionSpace_Type())
cidsHealthSecMonUtilizedPartitionSpace.setMaxAccess(_D)
if mibBuilder.loadTexts:cidsHealthSecMonUtilizedPartitionSpace.setStatus(_B)
if mibBuilder.loadTexts:cidsHealthSecMonUtilizedPartitionSpace.setUnits('MB')
_CiscoCidsMIBConform_ObjectIdentity=ObjectIdentity
ciscoCidsMIBConform=_CiscoCidsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,383,2))
_CiscoCidsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCidsMIBCompliances=_CiscoCidsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,383,2,1))
_CiscoCidsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCidsMIBGroups=_CiscoCidsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,383,2,2))
ciscoCidsGeneralObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,1))
ciscoCidsGeneralObjectGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_i),(_A,_j),(_A,_y)))
if mibBuilder.loadTexts:ciscoCidsGeneralObjectGroup.setStatus(_E)
ciscoCidsAlertObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,2))
ciscoCidsAlertObjectGroup.setObjects(*((_A,_k),(_A,_l),(_A,_O),(_A,_m),(_A,_n),(_A,_o),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_p),(_A,_U),(_A,_V),(_A,_W),(_A,_q),(_A,_r),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoCidsAlertObjectGroup.setStatus(_E)
ciscoCidsErrorObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,3))
ciscoCidsErrorObjectGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ciscoCidsErrorObjectGroup.setStatus(_B)
ciscoCidsHealthObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,5))
ciscoCidsHealthObjectGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:ciscoCidsHealthObjectGroup.setStatus(_B)
ciscoCidsGeneralObjectGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,6))
ciscoCidsGeneralObjectGroupRev1.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_y)))
if mibBuilder.loadTexts:ciscoCidsGeneralObjectGroupRev1.setStatus(_B)
ciscoCidsAlertObjectGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,7))
ciscoCidsAlertObjectGroupRev1.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:ciscoCidsAlertObjectGroupRev1.setStatus(_B)
ciscoCidsOptionalObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,8))
ciscoCidsOptionalObjectGroup.setObjects(*((_A,_i),(_A,_j),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_p),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:ciscoCidsOptionalObjectGroup.setStatus(_E)
ciscoCidsOptionalObjectGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,9))
ciscoCidsOptionalObjectGroupRev1.setObjects(*((_A,_i),(_A,_j),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_p),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:ciscoCidsOptionalObjectGroupRev1.setStatus(_B)
ciscoCidsOptionalObjectGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,10))
ciscoCidsOptionalObjectGroupRev2.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:ciscoCidsOptionalObjectGroupRev2.setStatus(_B)
ciscoCidsAlertObjectGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,11))
ciscoCidsAlertObjectGroupRev2.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoCidsAlertObjectGroupRev2.setStatus(_B)
ciscoCidsHealthObjectGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,12))
ciscoCidsHealthObjectGroupRev1.setObjects(*((_A,_Al),(_A,_s),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:ciscoCidsHealthObjectGroupRev1.setStatus(_B)
ciscoCidsOptionalObjectGroupRev3=ObjectGroup((1,3,6,1,4,1,9,9,383,2,2,13))
ciscoCidsOptionalObjectGroupRev3.setObjects((_A,_Az))
if mibBuilder.loadTexts:ciscoCidsOptionalObjectGroupRev3.setStatus(_B)
ciscoCidsAlert=NotificationType((1,3,6,1,4,1,9,9,383,0,1))
ciscoCidsAlert.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_k),(_A,_m),(_A,_n),(_A,_o),(_A,_l),(_A,_r),(_A,_q)))
if mibBuilder.loadTexts:ciscoCidsAlert.setStatus(_B)
ciscoCidsError=NotificationType((1,3,6,1,4,1,9,9,383,0,2))
ciscoCidsError.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ciscoCidsError.setStatus(_B)
ciscoCidsHealthHeartBeat=NotificationType((1,3,6,1,4,1,9,9,383,0,3))
ciscoCidsHealthHeartBeat.setObjects(*((_A,_H),(_A,_K),(_A,_I),(_A,_J),(_A,_t),(_A,_u),(_A,_s)))
if mibBuilder.loadTexts:ciscoCidsHealthHeartBeat.setStatus(_B)
ciscoCidsHealthMetricChange=NotificationType((1,3,6,1,4,1,9,9,383,0,4))
ciscoCidsHealthMetricChange.setObjects(*((_A,_H),(_A,_K),(_A,_I),(_A,_J),(_A,_t),(_A,_u),(_A,_s)))
if mibBuilder.loadTexts:ciscoCidsHealthMetricChange.setStatus(_B)
ciscoCidsNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,383,2,2,4))
ciscoCidsNotificationsGroup.setObjects(*((_A,_A_),(_A,_B0)))
if mibBuilder.loadTexts:ciscoCidsNotificationsGroup.setStatus(_B)
ciscoCidsNotificationsGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,383,2,2,14))
ciscoCidsNotificationsGroupRev1.setObjects(*((_A,_B1),(_A,_B2)))
if mibBuilder.loadTexts:ciscoCidsNotificationsGroupRev1.setStatus(_B)
ciscoCidsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,383,2,1,1))
ciscoCidsMIBCompliance.setObjects(*((_A,_B3),(_A,_B4),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoCidsMIBCompliance.setStatus(_E)
ciscoCidsMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,383,2,1,2))
ciscoCidsMIBComplianceRev1.setObjects(*((_A,_f),(_A,_g),(_A,_M),(_A,_N),(_A,_h),(_A,_B5)))
if mibBuilder.loadTexts:ciscoCidsMIBComplianceRev1.setStatus(_E)
ciscoCidsMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,383,2,1,3))
ciscoCidsMIBComplianceRev2.setObjects(*((_A,_f),(_A,_g),(_A,_M),(_A,_N),(_A,_h),(_A,_v)))
if mibBuilder.loadTexts:ciscoCidsMIBComplianceRev2.setStatus(_E)
ciscoCidsMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,383,2,1,4))
ciscoCidsMIBComplianceRev3.setObjects(*((_A,_f),(_A,_g),(_A,_M),(_A,_N),(_A,_h),(_A,_AI),(_A,_v)))
if mibBuilder.loadTexts:ciscoCidsMIBComplianceRev3.setStatus(_E)
ciscoCidsMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,383,2,1,5))
ciscoCidsMIBComplianceRev4.setObjects(*((_A,_M),(_A,_f),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_N),(_A,_h),(_A,_g),(_A,_B9),(_A,_AI),(_A,_v)))
if mibBuilder.loadTexts:ciscoCidsMIBComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CidsHealthStatusColor':CidsHealthStatusColor,'CidsApplicationStatus':CidsApplicationStatus,'CidsErrorCode':CidsErrorCode,'CidsTargetValue':CidsTargetValue,'CidsAttackRelevance':CidsAttackRelevance,'ciscoCidsMIB':ciscoCidsMIB,'ciscoCidsMIBNotifs':ciscoCidsMIBNotifs,_A_:ciscoCidsAlert,_B0:ciscoCidsError,_B1:ciscoCidsHealthHeartBeat,_B2:ciscoCidsHealthMetricChange,'ciscoCidsMIBObjects':ciscoCidsMIBObjects,'cidsGeneral':cidsGeneral,_H:cidsGeneralEventId,_I:cidsGeneralLocalTime,_J:cidsGeneralUTCTime,_K:cidsGeneralOriginatorHostId,_i:cidsGeneralOriginatorAppName,_j:cidsGeneralOriginatorAppId,_y:cidsNotificationsEnabled,'cidsAlert':cidsAlert,_k:cidsAlertSeverity,_l:cidsAlertAlarmTraits,_O:cidsAlertSignature,_m:cidsAlertSignatureSigName,_n:cidsAlertSignatureSigId,_o:cidsAlertSignatureSubSigId,_P:cidsAlertSignatureVersion,_Q:cidsAlertSummary,_R:cidsAlertSummaryType,_S:cidsAlertSummaryFinal,_T:cidsAlertSummaryInitialAlert,_p:cidsAlertInterfaceGroup,_U:cidsAlertVlan,_V:cidsAlertVictimContext,_W:cidsAlertAttackerContext,_r:cidsAlertAttackerAddress,_q:cidsAlertVictimAddress,_X:cidsAlertIpLoggingActivated,_Y:cidsAlertTcpResetSent,_Z:cidsAlertShunRequested,_a:cidsAlertDetails,_b:cidsAlertIpLogId,_c:cidsThreatResponseStatus,_d:cidsThreatResponseSeverity,_e:cidsAlertEventRiskRating,_A2:cidsAlertIfIndex,_A3:cidsAlertProtocol,_A4:cidsAlertDeniedAttacker,_A5:cidsAlertDeniedFlow,_A6:cidsAlertDenyPacketReqNotPerf,_A7:cidsAlertDenyFlowReqNotPerf,_A8:cidsAlertDenyAttackerReqNotPerf,_A9:cidsAlertBlockConnectionReq,_AA:cidsAlertLogAttackerPacketsAct,_AB:cidsAlertLogVictimPacketsAct,_AC:cidsAlertLogPairPacketsActivated,_AD:cidsAlertRateLimitRequested,_AE:cidsAlertDeniedAttackVictimPair,_AF:cidsAlertDeniedAttackSericePair,_AG:cidsAlertDenyAttackVicReqNotPerf,_AH:cidsAlertDenyAttackSerReqNotPerf,_Ae:cidsAlertThreatValueRating,_Af:cidsAlertRiskRatingTargetValue,_Ag:cidsAlertRiskRatingRelevance,_Ah:cidsAlertRiskRatingWatchList,_Ai:cidsAlertDenyPacket,_Aj:cidsAlertBlockHost,_Ak:cidsAlertTcpOneWayResetSent,_Az:cidsAlertVirtualSensor,'cidsError':cidsError,_z:cidsErrorSeverity,_A0:cidsErrorName,_A1:cidsErrorMessage,'cidsHealth':cidsHealth,_AN:cidsHealthPacketLoss,_AO:cidsHealthPacketDenialRate,_AP:cidsHealthAlarmsGenerated,_AQ:cidsHealthFragmentsInFRU,_AR:cidsHealthDatagramsInFRU,_AS:cidsHealthTcpEmbryonicStreams,_AT:cidsHealthTCPEstablishedStreams,_AU:cidsHealthTcpClosingStreams,_AV:cidsHealthTcpStreams,_AW:cidsHealthActiveNodes,_AX:cidsHealthTcpDualIpAndPorts,_AY:cidsHealthUdpDualIpAndPorts,_AZ:cidsHealthIpDualIp,_Aa:cidsHealthIsSensorMemoryCritical,_Ab:cidsHealthIsSensorActive,_Ac:cidsHealthCommandAndControlPort,_Ad:cidsHealthSensorStatsResetTime,_Al:cidsHealthSecMonAvailability,_s:cidsHealthSecMonOverallHealth,_Am:cidsHealthSecMonSoftwareVersion,_An:cidsHealthSecMonSignatureVersion,_Ao:cidsHealthSecMonLicenseStatus,_t:cidsHealthSecMonOverallAppColor,_Ap:cidsHealthSecMonMainAppStatus,_Aq:cidsHealthSecMonAnalysisEngineStatus,_Aw:cidsHealthSecMonCollaborationAppStatus,_Ar:cidsHealthSecMonByPassMode,_As:cidsHealthSecMonMissedPktPctAndThresh,_At:cidsHealthSecMonAnalysisEngMemPercent,_Au:cidsHealthSecMonSensorLoad,_u:cidsHealthSecMonSensorLoadColor,'cidsHealthSecMonVirtSensorStatusTable':cidsHealthSecMonVirtSensorStatusTable,'cidsHealthSecMonVirtSensorStatusEntry':cidsHealthSecMonVirtSensorStatusEntry,_AK:cidsHealthSecMonVirtSensorName,_Av:cidsHealthSecMonVirtSensorStatus,'cidsHealthSecMonDataStorageTable':cidsHealthSecMonDataStorageTable,'cidsHealthSecMonDataStorageEntry':cidsHealthSecMonDataStorageEntry,_AM:cidsHealthSecMonPartitionName,_Ax:cidsHealthSecMonTotalPartitionSpace,_Ay:cidsHealthSecMonUtilizedPartitionSpace,'ciscoCidsMIBConform':ciscoCidsMIBConform,'ciscoCidsMIBCompliances':ciscoCidsMIBCompliances,'ciscoCidsMIBCompliance':ciscoCidsMIBCompliance,'ciscoCidsMIBComplianceRev1':ciscoCidsMIBComplianceRev1,'ciscoCidsMIBComplianceRev2':ciscoCidsMIBComplianceRev2,'ciscoCidsMIBComplianceRev3':ciscoCidsMIBComplianceRev3,'ciscoCidsMIBComplianceRev4':ciscoCidsMIBComplianceRev4,'ciscoCidsMIBGroups':ciscoCidsMIBGroups,_B3:ciscoCidsGeneralObjectGroup,_B4:ciscoCidsAlertObjectGroup,_M:ciscoCidsErrorObjectGroup,_h:ciscoCidsNotificationsGroup,_N:ciscoCidsHealthObjectGroup,_f:ciscoCidsGeneralObjectGroupRev1,_g:ciscoCidsAlertObjectGroupRev1,_B5:ciscoCidsOptionalObjectGroup,_v:ciscoCidsOptionalObjectGroupRev1,_AI:ciscoCidsOptionalObjectGroupRev2,_B6:ciscoCidsAlertObjectGroupRev2,_B7:ciscoCidsHealthObjectGroupRev1,_B9:ciscoCidsOptionalObjectGroupRev3,_B8:ciscoCidsNotificationsGroupRev1})