_AZ='h225DisconnectCauseCodeGroup'
_AY='h225FromH323PeerDisconnects'
_AX='h225FromOtherPeerDisconnects'
_AW='h225CauseCodeDescription'
_AV='h225RasStatsRequestInProgOuts'
_AU='h225RasStatsRequestInProgIns'
_AT='h225RasStatsResourceAvailConOuts'
_AS='h225RasStatsResourceAvailConfIns'
_AR='h225RasStatsResourceAvailIndOuts'
_AQ='h225RasStatsResourceAvailIndIns'
_AP='h225RasStatsUnregisterRejectOuts'
_AO='h225RasStatsUnregisterRejectIns'
_AN='h225RasStatsUnregisterConfOuts'
_AM='h225RasStatsUnregisterConfirmIns'
_AL='h225RasStatsUnregisterReqOuts'
_AK='h225RasStatsUnregisterReqIns'
_AJ='h225RasStatsDisengageRejectOuts'
_AI='h225RasStatsDisengageRejectIns'
_AH='h225RasStatsDisengageConfirmOuts'
_AG='h225RasStatsDisengageConfirmIns'
_AF='h225RasStatsDisengageReqOuts'
_AE='h225RasStatsDisengageReqIns'
_AD='h225RasStatsBandwidthRejectOuts'
_AC='h225RasStatsBandwidthRejectIns'
_AB='h225RasStatsBandwidthConfirmOuts'
_AA='h225RasStatsBandwidthConfirmIns'
_A9='h225RasStatsBandwidthReqOuts'
_A8='h225RasStatsBandwidthReqIns'
_A7='h225RasStatsAdmissionRejectOuts'
_A6='h225RasStatsAdmissionRejectIns'
_A5='h225RasStatsAdmissionConfirmOuts'
_A4='h225RasStatsAdmissionConfirmIns'
_A3='h225RasStatsAdmissionReqOuts'
_A2='h225RasStatsAdmissionReqIns'
_A1='h225RasStatsRegistrationRejOuts'
_A0='h225RasStatsRegistrationRejIns'
_z='h225RasStatsRegistrationConfOuts'
_y='h225RasStatsRegistrationConfIns'
_x='h225RasStatsRegistrationReqOuts'
_w='h225RasStatsRegistrationReqIns'
_v='h225RasStatsGkDiscoveryRejOuts'
_u='h225RasStatsGkDiscoveryRejectIns'
_t='h225RasStatsGkDiscoveryConfOuts'
_s='h225RasStatsGkDiscoveryConfIns'
_r='h225RasStatsGkDiscoveryReqOuts'
_q='h225RasStatsGkDiscoveryReqIns'
_p='h225CallSignalStatsPassthroFails'
_o='h225CallSignalStatsPassthroOuts'
_n='h225CallSignalStatsPassthroIns'
_m='h225CallSignalStatsRejectFails'
_l='h225CallSignalStatsRejectOuts'
_k='h225CallSignalStatsRejectIns'
_j='h225CallSignalStatsReleaseFails'
_i='h225CallSignalStatsReleaseOuts'
_h='h225CallSignalStatsReleaseIns'
_g='h225CallSignalStatsFacilityFails'
_f='h225CallSignalStatsFacilityOuts'
_e='h225CallSignalStatsFacilityIns'
_d='h225CallSignalStatsUserInfoFails'
_c='h225CallSignalStatsUserInfoOuts'
_b='h225CallSignalStatsUserInfoIns'
_a='h225CallSignalStatsInfoFails'
_Z='h225CallSignalStatsInfoOuts'
_Y='h225CallSignalStatsInfoIns'
_X='h225CallSignalStatsNotifyFails'
_W='h225CallSignalStatsNotifyOuts'
_V='h225CallSignalStatsNotifyIns'
_U='h225CallSignalStatsCallProcFails'
_T='h225CallSignalStatsCallProcsOuts'
_S='h225CallSignalStatsCallProcsIns'
_R='h225CallSignalStatsProgFails'
_Q='h225CallSignalStatsProgOuts'
_P='h225CallSignalStatsProgIns'
_O='h225CallSignalStatsAlertingFails'
_N='h225CallSignalStatsAlertingOuts'
_M='h225CallSignalStatsAlertingIns'
_L='h225CallSignalStatsSetupConFails'
_K='h225CallSignalStatsSetupConfOuts'
_J='h225CallSignalStatsSetupConfIns'
_I='h225CallSignalStatsSetupFails'
_H='h225CallSignalStatsSetupOuts'
_G='h225CallSignalStatsSetupIns'
_F='h225CauseCode'
_E='h225RasStatsGroup'
_D='h225CallSignalStatsGroup'
_C='read-only'
_B='CISCO-H225-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoH225MIB=ModuleIdentity((1,3,6,1,4,1,9,9,397))
if mibBuilder.loadTexts:ciscoH225MIB.setRevisions(('2004-11-24 00:00','2004-03-15 00:00'))
class CauseCodeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,53,55,57,58,62,63,65,66,69,70,79,81,82,83,84,85,86,87,88,90,91,93,95,96,97,98,99,100,101,102,103,110,111,126,127,128,129,160,170,171,172,180,250,251,256)));namedValues=NamedValues(*(('unallocatedNumber',1),('noRouteToSpecifiedTransitNetwork',2),('noRouteToDestination',3),('sendSpecialInformationTone',4),('misdialledTrunkPrefix',5),('channelUnacceptable',6),('callAwardedAndDelivered',7),('preemption',8),('preemptionCircuitReserved',9),('glare',15),('normalCallClearing',16),('userBusy',17),('noUserResponding',18),('noAnswerFromUser',19),('subscriberAbsent',20),('callRejected',21),('numberChanged',22),('redirectionToNewDestination',23),('exchangeRoutingError',25),('nonSelectedUserClearing',26),('destinationOutOfOrder',27),('invalidNumberORAddressIncomplete',28),('facilityRejected',29),('responseToSTATUSENQUIRY',30),('normalUnspecified',31),('nocircuitORchannelAvailable',34),('requestedVPCIorVCINotAvailable',35),('vpciORvciAssignmentFailure',36),('cellRateNotAvailable',37),('networkOutOfOrder',38),('permanentFrameModeOutOfService',39),('permanentFrameModeOperational',40),('temporaryFailure',41),('switchingEquipmentCongestion',42),('accessInformationDiscarded',43),('noRequestedCircuitORchannel',44),('noVPCIorVCIAvailable',45),('precedenceCallBlocked',46),('resourceUnavailableUnspecified',47),('qualityOfServiceNotAvailable',49),('requestedFacilityNotSubscribed',50),('outgoingCallsBarredWithinCUG',53),('incomingCallsBarredWithinCUG',55),('bearerCapabilityNotAuthorized',57),('bearerCapabilityNotAvailable',58),('inconsistencyInOutgoingInfo',62),('noServiceOROption',63),('bearerCapabilityNotImplemented',65),('channelTypeNotImplemented',66),('requestedFacilityNotImplemented',69),('onlyRestrictedDigitalInfoBC',70),('serviceOROptionNotImplemented',79),('invalidCallReferenceValue',81),('identifiedChannelDoesNotExist',82),('callExistsButCallIdentityDoesNot',83),('callIdentityInUse',84),('noCallSuspended',85),('requestedCallIdentityCleared',86),('userNotMemberOfCUG',87),('incompatibleDestination',88),('nonExistentCUG',90),('invalidTransitNetworkSelection',91),('allParametersNotSupported',93),('invalidMessageUnspecified',95),('mandatoryInfoElementMissing',96),('messageTypeNotImplemented',97),('messageInCompatible',98),('infoElementORNotImplemented',99),('invalidInfoElementContents',100),('messageInCompatibleCallState',101),('recoveryOnTimerExpiry',102),('nonImplementedParamPassedon',103),('unrecognizedParamMSGDiscarded',110),('protocolErrorUnspecified',111),('noVoiceResource',126),('interworkingUnspecified',127),('nextNodeUnreachable',128),('htspmOutOfService',129),('dtlTransitNotNodeId',160),('noDSPChannel',170),('codecIncompatible',171),('dspError',172),('glaringSwitchPRI',180),('sipUndefinedMapped',250),('sipUndefinedUnmapped',251),('unknownCauseCodeType',256)))
_H225MIBObjects_ObjectIdentity=ObjectIdentity
h225MIBObjects=_H225MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,397,1))
_H225CallSignal_ObjectIdentity=ObjectIdentity
h225CallSignal=_H225CallSignal_ObjectIdentity((1,3,6,1,4,1,9,9,397,1,1))
_H225CallSignalStats_ObjectIdentity=ObjectIdentity
h225CallSignalStats=_H225CallSignalStats_ObjectIdentity((1,3,6,1,4,1,9,9,397,1,1,1))
_H225CallSignalStatsSetupIns_Type=Counter32
_H225CallSignalStatsSetupIns_Object=MibScalar
h225CallSignalStatsSetupIns=_H225CallSignalStatsSetupIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,1),_H225CallSignalStatsSetupIns_Type())
h225CallSignalStatsSetupIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsSetupIns.setStatus(_A)
_H225CallSignalStatsSetupOuts_Type=Counter32
_H225CallSignalStatsSetupOuts_Object=MibScalar
h225CallSignalStatsSetupOuts=_H225CallSignalStatsSetupOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,2),_H225CallSignalStatsSetupOuts_Type())
h225CallSignalStatsSetupOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsSetupOuts.setStatus(_A)
_H225CallSignalStatsSetupFails_Type=Counter32
_H225CallSignalStatsSetupFails_Object=MibScalar
h225CallSignalStatsSetupFails=_H225CallSignalStatsSetupFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,3),_H225CallSignalStatsSetupFails_Type())
h225CallSignalStatsSetupFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsSetupFails.setStatus(_A)
_H225CallSignalStatsSetupConfIns_Type=Counter32
_H225CallSignalStatsSetupConfIns_Object=MibScalar
h225CallSignalStatsSetupConfIns=_H225CallSignalStatsSetupConfIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,4),_H225CallSignalStatsSetupConfIns_Type())
h225CallSignalStatsSetupConfIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsSetupConfIns.setStatus(_A)
_H225CallSignalStatsSetupConfOuts_Type=Counter32
_H225CallSignalStatsSetupConfOuts_Object=MibScalar
h225CallSignalStatsSetupConfOuts=_H225CallSignalStatsSetupConfOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,5),_H225CallSignalStatsSetupConfOuts_Type())
h225CallSignalStatsSetupConfOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsSetupConfOuts.setStatus(_A)
_H225CallSignalStatsSetupConFails_Type=Counter32
_H225CallSignalStatsSetupConFails_Object=MibScalar
h225CallSignalStatsSetupConFails=_H225CallSignalStatsSetupConFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,6),_H225CallSignalStatsSetupConFails_Type())
h225CallSignalStatsSetupConFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsSetupConFails.setStatus(_A)
_H225CallSignalStatsAlertingIns_Type=Counter32
_H225CallSignalStatsAlertingIns_Object=MibScalar
h225CallSignalStatsAlertingIns=_H225CallSignalStatsAlertingIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,7),_H225CallSignalStatsAlertingIns_Type())
h225CallSignalStatsAlertingIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsAlertingIns.setStatus(_A)
_H225CallSignalStatsAlertingOuts_Type=Counter32
_H225CallSignalStatsAlertingOuts_Object=MibScalar
h225CallSignalStatsAlertingOuts=_H225CallSignalStatsAlertingOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,8),_H225CallSignalStatsAlertingOuts_Type())
h225CallSignalStatsAlertingOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsAlertingOuts.setStatus(_A)
_H225CallSignalStatsAlertingFails_Type=Counter32
_H225CallSignalStatsAlertingFails_Object=MibScalar
h225CallSignalStatsAlertingFails=_H225CallSignalStatsAlertingFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,9),_H225CallSignalStatsAlertingFails_Type())
h225CallSignalStatsAlertingFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsAlertingFails.setStatus(_A)
_H225CallSignalStatsProgIns_Type=Counter32
_H225CallSignalStatsProgIns_Object=MibScalar
h225CallSignalStatsProgIns=_H225CallSignalStatsProgIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,10),_H225CallSignalStatsProgIns_Type())
h225CallSignalStatsProgIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsProgIns.setStatus(_A)
_H225CallSignalStatsProgOuts_Type=Counter32
_H225CallSignalStatsProgOuts_Object=MibScalar
h225CallSignalStatsProgOuts=_H225CallSignalStatsProgOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,11),_H225CallSignalStatsProgOuts_Type())
h225CallSignalStatsProgOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsProgOuts.setStatus(_A)
_H225CallSignalStatsProgFails_Type=Counter32
_H225CallSignalStatsProgFails_Object=MibScalar
h225CallSignalStatsProgFails=_H225CallSignalStatsProgFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,12),_H225CallSignalStatsProgFails_Type())
h225CallSignalStatsProgFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsProgFails.setStatus(_A)
_H225CallSignalStatsCallProcsIns_Type=Counter32
_H225CallSignalStatsCallProcsIns_Object=MibScalar
h225CallSignalStatsCallProcsIns=_H225CallSignalStatsCallProcsIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,13),_H225CallSignalStatsCallProcsIns_Type())
h225CallSignalStatsCallProcsIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsCallProcsIns.setStatus(_A)
_H225CallSignalStatsCallProcsOuts_Type=Counter32
_H225CallSignalStatsCallProcsOuts_Object=MibScalar
h225CallSignalStatsCallProcsOuts=_H225CallSignalStatsCallProcsOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,14),_H225CallSignalStatsCallProcsOuts_Type())
h225CallSignalStatsCallProcsOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsCallProcsOuts.setStatus(_A)
_H225CallSignalStatsCallProcFails_Type=Counter32
_H225CallSignalStatsCallProcFails_Object=MibScalar
h225CallSignalStatsCallProcFails=_H225CallSignalStatsCallProcFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,15),_H225CallSignalStatsCallProcFails_Type())
h225CallSignalStatsCallProcFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsCallProcFails.setStatus(_A)
_H225CallSignalStatsNotifyIns_Type=Counter32
_H225CallSignalStatsNotifyIns_Object=MibScalar
h225CallSignalStatsNotifyIns=_H225CallSignalStatsNotifyIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,16),_H225CallSignalStatsNotifyIns_Type())
h225CallSignalStatsNotifyIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsNotifyIns.setStatus(_A)
_H225CallSignalStatsNotifyOuts_Type=Counter32
_H225CallSignalStatsNotifyOuts_Object=MibScalar
h225CallSignalStatsNotifyOuts=_H225CallSignalStatsNotifyOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,17),_H225CallSignalStatsNotifyOuts_Type())
h225CallSignalStatsNotifyOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsNotifyOuts.setStatus(_A)
_H225CallSignalStatsNotifyFails_Type=Counter32
_H225CallSignalStatsNotifyFails_Object=MibScalar
h225CallSignalStatsNotifyFails=_H225CallSignalStatsNotifyFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,18),_H225CallSignalStatsNotifyFails_Type())
h225CallSignalStatsNotifyFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsNotifyFails.setStatus(_A)
_H225CallSignalStatsInfoIns_Type=Counter32
_H225CallSignalStatsInfoIns_Object=MibScalar
h225CallSignalStatsInfoIns=_H225CallSignalStatsInfoIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,19),_H225CallSignalStatsInfoIns_Type())
h225CallSignalStatsInfoIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsInfoIns.setStatus(_A)
_H225CallSignalStatsInfoOuts_Type=Counter32
_H225CallSignalStatsInfoOuts_Object=MibScalar
h225CallSignalStatsInfoOuts=_H225CallSignalStatsInfoOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,20),_H225CallSignalStatsInfoOuts_Type())
h225CallSignalStatsInfoOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsInfoOuts.setStatus(_A)
_H225CallSignalStatsInfoFails_Type=Counter32
_H225CallSignalStatsInfoFails_Object=MibScalar
h225CallSignalStatsInfoFails=_H225CallSignalStatsInfoFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,21),_H225CallSignalStatsInfoFails_Type())
h225CallSignalStatsInfoFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsInfoFails.setStatus(_A)
_H225CallSignalStatsUserInfoIns_Type=Counter32
_H225CallSignalStatsUserInfoIns_Object=MibScalar
h225CallSignalStatsUserInfoIns=_H225CallSignalStatsUserInfoIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,22),_H225CallSignalStatsUserInfoIns_Type())
h225CallSignalStatsUserInfoIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsUserInfoIns.setStatus(_A)
_H225CallSignalStatsUserInfoOuts_Type=Counter32
_H225CallSignalStatsUserInfoOuts_Object=MibScalar
h225CallSignalStatsUserInfoOuts=_H225CallSignalStatsUserInfoOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,23),_H225CallSignalStatsUserInfoOuts_Type())
h225CallSignalStatsUserInfoOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsUserInfoOuts.setStatus(_A)
_H225CallSignalStatsUserInfoFails_Type=Counter32
_H225CallSignalStatsUserInfoFails_Object=MibScalar
h225CallSignalStatsUserInfoFails=_H225CallSignalStatsUserInfoFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,24),_H225CallSignalStatsUserInfoFails_Type())
h225CallSignalStatsUserInfoFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsUserInfoFails.setStatus(_A)
_H225CallSignalStatsFacilityIns_Type=Counter32
_H225CallSignalStatsFacilityIns_Object=MibScalar
h225CallSignalStatsFacilityIns=_H225CallSignalStatsFacilityIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,25),_H225CallSignalStatsFacilityIns_Type())
h225CallSignalStatsFacilityIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsFacilityIns.setStatus(_A)
_H225CallSignalStatsFacilityOuts_Type=Counter32
_H225CallSignalStatsFacilityOuts_Object=MibScalar
h225CallSignalStatsFacilityOuts=_H225CallSignalStatsFacilityOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,26),_H225CallSignalStatsFacilityOuts_Type())
h225CallSignalStatsFacilityOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsFacilityOuts.setStatus(_A)
_H225CallSignalStatsFacilityFails_Type=Counter32
_H225CallSignalStatsFacilityFails_Object=MibScalar
h225CallSignalStatsFacilityFails=_H225CallSignalStatsFacilityFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,27),_H225CallSignalStatsFacilityFails_Type())
h225CallSignalStatsFacilityFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsFacilityFails.setStatus(_A)
_H225CallSignalStatsReleaseIns_Type=Counter32
_H225CallSignalStatsReleaseIns_Object=MibScalar
h225CallSignalStatsReleaseIns=_H225CallSignalStatsReleaseIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,28),_H225CallSignalStatsReleaseIns_Type())
h225CallSignalStatsReleaseIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsReleaseIns.setStatus(_A)
_H225CallSignalStatsReleaseOuts_Type=Counter32
_H225CallSignalStatsReleaseOuts_Object=MibScalar
h225CallSignalStatsReleaseOuts=_H225CallSignalStatsReleaseOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,29),_H225CallSignalStatsReleaseOuts_Type())
h225CallSignalStatsReleaseOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsReleaseOuts.setStatus(_A)
_H225CallSignalStatsReleaseFails_Type=Counter32
_H225CallSignalStatsReleaseFails_Object=MibScalar
h225CallSignalStatsReleaseFails=_H225CallSignalStatsReleaseFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,30),_H225CallSignalStatsReleaseFails_Type())
h225CallSignalStatsReleaseFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsReleaseFails.setStatus(_A)
_H225CallSignalStatsRejectIns_Type=Counter32
_H225CallSignalStatsRejectIns_Object=MibScalar
h225CallSignalStatsRejectIns=_H225CallSignalStatsRejectIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,31),_H225CallSignalStatsRejectIns_Type())
h225CallSignalStatsRejectIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsRejectIns.setStatus(_A)
_H225CallSignalStatsRejectOuts_Type=Counter32
_H225CallSignalStatsRejectOuts_Object=MibScalar
h225CallSignalStatsRejectOuts=_H225CallSignalStatsRejectOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,32),_H225CallSignalStatsRejectOuts_Type())
h225CallSignalStatsRejectOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsRejectOuts.setStatus(_A)
_H225CallSignalStatsRejectFails_Type=Counter32
_H225CallSignalStatsRejectFails_Object=MibScalar
h225CallSignalStatsRejectFails=_H225CallSignalStatsRejectFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,33),_H225CallSignalStatsRejectFails_Type())
h225CallSignalStatsRejectFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsRejectFails.setStatus(_A)
_H225CallSignalStatsPassthroIns_Type=Counter32
_H225CallSignalStatsPassthroIns_Object=MibScalar
h225CallSignalStatsPassthroIns=_H225CallSignalStatsPassthroIns_Object((1,3,6,1,4,1,9,9,397,1,1,1,34),_H225CallSignalStatsPassthroIns_Type())
h225CallSignalStatsPassthroIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsPassthroIns.setStatus(_A)
_H225CallSignalStatsPassthroOuts_Type=Counter32
_H225CallSignalStatsPassthroOuts_Object=MibScalar
h225CallSignalStatsPassthroOuts=_H225CallSignalStatsPassthroOuts_Object((1,3,6,1,4,1,9,9,397,1,1,1,35),_H225CallSignalStatsPassthroOuts_Type())
h225CallSignalStatsPassthroOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsPassthroOuts.setStatus(_A)
_H225CallSignalStatsPassthroFails_Type=Counter32
_H225CallSignalStatsPassthroFails_Object=MibScalar
h225CallSignalStatsPassthroFails=_H225CallSignalStatsPassthroFails_Object((1,3,6,1,4,1,9,9,397,1,1,1,36),_H225CallSignalStatsPassthroFails_Type())
h225CallSignalStatsPassthroFails.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CallSignalStatsPassthroFails.setStatus(_A)
_H225Ras_ObjectIdentity=ObjectIdentity
h225Ras=_H225Ras_ObjectIdentity((1,3,6,1,4,1,9,9,397,1,2))
_H225RasStats_ObjectIdentity=ObjectIdentity
h225RasStats=_H225RasStats_ObjectIdentity((1,3,6,1,4,1,9,9,397,1,2,1))
_H225RasStatsGkDiscoveryReqIns_Type=Counter32
_H225RasStatsGkDiscoveryReqIns_Object=MibScalar
h225RasStatsGkDiscoveryReqIns=_H225RasStatsGkDiscoveryReqIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,1),_H225RasStatsGkDiscoveryReqIns_Type())
h225RasStatsGkDiscoveryReqIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsGkDiscoveryReqIns.setStatus(_A)
_H225RasStatsGkDiscoveryReqOuts_Type=Counter32
_H225RasStatsGkDiscoveryReqOuts_Object=MibScalar
h225RasStatsGkDiscoveryReqOuts=_H225RasStatsGkDiscoveryReqOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,2),_H225RasStatsGkDiscoveryReqOuts_Type())
h225RasStatsGkDiscoveryReqOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsGkDiscoveryReqOuts.setStatus(_A)
_H225RasStatsGkDiscoveryConfIns_Type=Counter32
_H225RasStatsGkDiscoveryConfIns_Object=MibScalar
h225RasStatsGkDiscoveryConfIns=_H225RasStatsGkDiscoveryConfIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,3),_H225RasStatsGkDiscoveryConfIns_Type())
h225RasStatsGkDiscoveryConfIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsGkDiscoveryConfIns.setStatus(_A)
_H225RasStatsGkDiscoveryConfOuts_Type=Counter32
_H225RasStatsGkDiscoveryConfOuts_Object=MibScalar
h225RasStatsGkDiscoveryConfOuts=_H225RasStatsGkDiscoveryConfOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,4),_H225RasStatsGkDiscoveryConfOuts_Type())
h225RasStatsGkDiscoveryConfOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsGkDiscoveryConfOuts.setStatus(_A)
_H225RasStatsGkDiscoveryRejectIns_Type=Counter32
_H225RasStatsGkDiscoveryRejectIns_Object=MibScalar
h225RasStatsGkDiscoveryRejectIns=_H225RasStatsGkDiscoveryRejectIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,5),_H225RasStatsGkDiscoveryRejectIns_Type())
h225RasStatsGkDiscoveryRejectIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsGkDiscoveryRejectIns.setStatus(_A)
_H225RasStatsGkDiscoveryRejOuts_Type=Counter32
_H225RasStatsGkDiscoveryRejOuts_Object=MibScalar
h225RasStatsGkDiscoveryRejOuts=_H225RasStatsGkDiscoveryRejOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,6),_H225RasStatsGkDiscoveryRejOuts_Type())
h225RasStatsGkDiscoveryRejOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsGkDiscoveryRejOuts.setStatus(_A)
_H225RasStatsRegistrationReqIns_Type=Counter32
_H225RasStatsRegistrationReqIns_Object=MibScalar
h225RasStatsRegistrationReqIns=_H225RasStatsRegistrationReqIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,7),_H225RasStatsRegistrationReqIns_Type())
h225RasStatsRegistrationReqIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsRegistrationReqIns.setStatus(_A)
_H225RasStatsRegistrationReqOuts_Type=Counter32
_H225RasStatsRegistrationReqOuts_Object=MibScalar
h225RasStatsRegistrationReqOuts=_H225RasStatsRegistrationReqOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,8),_H225RasStatsRegistrationReqOuts_Type())
h225RasStatsRegistrationReqOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsRegistrationReqOuts.setStatus(_A)
_H225RasStatsRegistrationConfIns_Type=Counter32
_H225RasStatsRegistrationConfIns_Object=MibScalar
h225RasStatsRegistrationConfIns=_H225RasStatsRegistrationConfIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,9),_H225RasStatsRegistrationConfIns_Type())
h225RasStatsRegistrationConfIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsRegistrationConfIns.setStatus(_A)
_H225RasStatsRegistrationConfOuts_Type=Counter32
_H225RasStatsRegistrationConfOuts_Object=MibScalar
h225RasStatsRegistrationConfOuts=_H225RasStatsRegistrationConfOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,10),_H225RasStatsRegistrationConfOuts_Type())
h225RasStatsRegistrationConfOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsRegistrationConfOuts.setStatus(_A)
_H225RasStatsRegistrationRejIns_Type=Counter32
_H225RasStatsRegistrationRejIns_Object=MibScalar
h225RasStatsRegistrationRejIns=_H225RasStatsRegistrationRejIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,11),_H225RasStatsRegistrationRejIns_Type())
h225RasStatsRegistrationRejIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsRegistrationRejIns.setStatus(_A)
_H225RasStatsRegistrationRejOuts_Type=Counter32
_H225RasStatsRegistrationRejOuts_Object=MibScalar
h225RasStatsRegistrationRejOuts=_H225RasStatsRegistrationRejOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,12),_H225RasStatsRegistrationRejOuts_Type())
h225RasStatsRegistrationRejOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsRegistrationRejOuts.setStatus(_A)
_H225RasStatsAdmissionReqIns_Type=Counter32
_H225RasStatsAdmissionReqIns_Object=MibScalar
h225RasStatsAdmissionReqIns=_H225RasStatsAdmissionReqIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,13),_H225RasStatsAdmissionReqIns_Type())
h225RasStatsAdmissionReqIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsAdmissionReqIns.setStatus(_A)
_H225RasStatsAdmissionReqOuts_Type=Counter32
_H225RasStatsAdmissionReqOuts_Object=MibScalar
h225RasStatsAdmissionReqOuts=_H225RasStatsAdmissionReqOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,14),_H225RasStatsAdmissionReqOuts_Type())
h225RasStatsAdmissionReqOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsAdmissionReqOuts.setStatus(_A)
_H225RasStatsAdmissionConfirmIns_Type=Counter32
_H225RasStatsAdmissionConfirmIns_Object=MibScalar
h225RasStatsAdmissionConfirmIns=_H225RasStatsAdmissionConfirmIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,15),_H225RasStatsAdmissionConfirmIns_Type())
h225RasStatsAdmissionConfirmIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsAdmissionConfirmIns.setStatus(_A)
_H225RasStatsAdmissionConfirmOuts_Type=Counter32
_H225RasStatsAdmissionConfirmOuts_Object=MibScalar
h225RasStatsAdmissionConfirmOuts=_H225RasStatsAdmissionConfirmOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,16),_H225RasStatsAdmissionConfirmOuts_Type())
h225RasStatsAdmissionConfirmOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsAdmissionConfirmOuts.setStatus(_A)
_H225RasStatsAdmissionRejectIns_Type=Counter32
_H225RasStatsAdmissionRejectIns_Object=MibScalar
h225RasStatsAdmissionRejectIns=_H225RasStatsAdmissionRejectIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,17),_H225RasStatsAdmissionRejectIns_Type())
h225RasStatsAdmissionRejectIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsAdmissionRejectIns.setStatus(_A)
_H225RasStatsAdmissionRejectOuts_Type=Counter32
_H225RasStatsAdmissionRejectOuts_Object=MibScalar
h225RasStatsAdmissionRejectOuts=_H225RasStatsAdmissionRejectOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,18),_H225RasStatsAdmissionRejectOuts_Type())
h225RasStatsAdmissionRejectOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsAdmissionRejectOuts.setStatus(_A)
_H225RasStatsBandwidthReqIns_Type=Counter32
_H225RasStatsBandwidthReqIns_Object=MibScalar
h225RasStatsBandwidthReqIns=_H225RasStatsBandwidthReqIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,19),_H225RasStatsBandwidthReqIns_Type())
h225RasStatsBandwidthReqIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsBandwidthReqIns.setStatus(_A)
_H225RasStatsBandwidthReqOuts_Type=Counter32
_H225RasStatsBandwidthReqOuts_Object=MibScalar
h225RasStatsBandwidthReqOuts=_H225RasStatsBandwidthReqOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,20),_H225RasStatsBandwidthReqOuts_Type())
h225RasStatsBandwidthReqOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsBandwidthReqOuts.setStatus(_A)
_H225RasStatsBandwidthConfirmIns_Type=Counter32
_H225RasStatsBandwidthConfirmIns_Object=MibScalar
h225RasStatsBandwidthConfirmIns=_H225RasStatsBandwidthConfirmIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,21),_H225RasStatsBandwidthConfirmIns_Type())
h225RasStatsBandwidthConfirmIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsBandwidthConfirmIns.setStatus(_A)
_H225RasStatsBandwidthConfirmOuts_Type=Counter32
_H225RasStatsBandwidthConfirmOuts_Object=MibScalar
h225RasStatsBandwidthConfirmOuts=_H225RasStatsBandwidthConfirmOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,22),_H225RasStatsBandwidthConfirmOuts_Type())
h225RasStatsBandwidthConfirmOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsBandwidthConfirmOuts.setStatus(_A)
_H225RasStatsBandwidthRejectIns_Type=Counter32
_H225RasStatsBandwidthRejectIns_Object=MibScalar
h225RasStatsBandwidthRejectIns=_H225RasStatsBandwidthRejectIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,23),_H225RasStatsBandwidthRejectIns_Type())
h225RasStatsBandwidthRejectIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsBandwidthRejectIns.setStatus(_A)
_H225RasStatsBandwidthRejectOuts_Type=Counter32
_H225RasStatsBandwidthRejectOuts_Object=MibScalar
h225RasStatsBandwidthRejectOuts=_H225RasStatsBandwidthRejectOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,24),_H225RasStatsBandwidthRejectOuts_Type())
h225RasStatsBandwidthRejectOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsBandwidthRejectOuts.setStatus(_A)
_H225RasStatsDisengageReqIns_Type=Counter32
_H225RasStatsDisengageReqIns_Object=MibScalar
h225RasStatsDisengageReqIns=_H225RasStatsDisengageReqIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,25),_H225RasStatsDisengageReqIns_Type())
h225RasStatsDisengageReqIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsDisengageReqIns.setStatus(_A)
_H225RasStatsDisengageReqOuts_Type=Counter32
_H225RasStatsDisengageReqOuts_Object=MibScalar
h225RasStatsDisengageReqOuts=_H225RasStatsDisengageReqOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,26),_H225RasStatsDisengageReqOuts_Type())
h225RasStatsDisengageReqOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsDisengageReqOuts.setStatus(_A)
_H225RasStatsDisengageConfirmIns_Type=Counter32
_H225RasStatsDisengageConfirmIns_Object=MibScalar
h225RasStatsDisengageConfirmIns=_H225RasStatsDisengageConfirmIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,27),_H225RasStatsDisengageConfirmIns_Type())
h225RasStatsDisengageConfirmIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsDisengageConfirmIns.setStatus(_A)
_H225RasStatsDisengageConfirmOuts_Type=Counter32
_H225RasStatsDisengageConfirmOuts_Object=MibScalar
h225RasStatsDisengageConfirmOuts=_H225RasStatsDisengageConfirmOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,28),_H225RasStatsDisengageConfirmOuts_Type())
h225RasStatsDisengageConfirmOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsDisengageConfirmOuts.setStatus(_A)
_H225RasStatsDisengageRejectIns_Type=Counter32
_H225RasStatsDisengageRejectIns_Object=MibScalar
h225RasStatsDisengageRejectIns=_H225RasStatsDisengageRejectIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,29),_H225RasStatsDisengageRejectIns_Type())
h225RasStatsDisengageRejectIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsDisengageRejectIns.setStatus(_A)
_H225RasStatsDisengageRejectOuts_Type=Counter32
_H225RasStatsDisengageRejectOuts_Object=MibScalar
h225RasStatsDisengageRejectOuts=_H225RasStatsDisengageRejectOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,30),_H225RasStatsDisengageRejectOuts_Type())
h225RasStatsDisengageRejectOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsDisengageRejectOuts.setStatus(_A)
_H225RasStatsUnregisterReqIns_Type=Counter32
_H225RasStatsUnregisterReqIns_Object=MibScalar
h225RasStatsUnregisterReqIns=_H225RasStatsUnregisterReqIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,31),_H225RasStatsUnregisterReqIns_Type())
h225RasStatsUnregisterReqIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsUnregisterReqIns.setStatus(_A)
_H225RasStatsUnregisterReqOuts_Type=Counter32
_H225RasStatsUnregisterReqOuts_Object=MibScalar
h225RasStatsUnregisterReqOuts=_H225RasStatsUnregisterReqOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,32),_H225RasStatsUnregisterReqOuts_Type())
h225RasStatsUnregisterReqOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsUnregisterReqOuts.setStatus(_A)
_H225RasStatsUnregisterConfirmIns_Type=Counter32
_H225RasStatsUnregisterConfirmIns_Object=MibScalar
h225RasStatsUnregisterConfirmIns=_H225RasStatsUnregisterConfirmIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,33),_H225RasStatsUnregisterConfirmIns_Type())
h225RasStatsUnregisterConfirmIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsUnregisterConfirmIns.setStatus(_A)
_H225RasStatsUnregisterConfOuts_Type=Counter32
_H225RasStatsUnregisterConfOuts_Object=MibScalar
h225RasStatsUnregisterConfOuts=_H225RasStatsUnregisterConfOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,34),_H225RasStatsUnregisterConfOuts_Type())
h225RasStatsUnregisterConfOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsUnregisterConfOuts.setStatus(_A)
_H225RasStatsUnregisterRejectIns_Type=Counter32
_H225RasStatsUnregisterRejectIns_Object=MibScalar
h225RasStatsUnregisterRejectIns=_H225RasStatsUnregisterRejectIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,35),_H225RasStatsUnregisterRejectIns_Type())
h225RasStatsUnregisterRejectIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsUnregisterRejectIns.setStatus(_A)
_H225RasStatsUnregisterRejectOuts_Type=Counter32
_H225RasStatsUnregisterRejectOuts_Object=MibScalar
h225RasStatsUnregisterRejectOuts=_H225RasStatsUnregisterRejectOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,36),_H225RasStatsUnregisterRejectOuts_Type())
h225RasStatsUnregisterRejectOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsUnregisterRejectOuts.setStatus(_A)
_H225RasStatsResourceAvailIndIns_Type=Counter32
_H225RasStatsResourceAvailIndIns_Object=MibScalar
h225RasStatsResourceAvailIndIns=_H225RasStatsResourceAvailIndIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,37),_H225RasStatsResourceAvailIndIns_Type())
h225RasStatsResourceAvailIndIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsResourceAvailIndIns.setStatus(_A)
_H225RasStatsResourceAvailIndOuts_Type=Counter32
_H225RasStatsResourceAvailIndOuts_Object=MibScalar
h225RasStatsResourceAvailIndOuts=_H225RasStatsResourceAvailIndOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,38),_H225RasStatsResourceAvailIndOuts_Type())
h225RasStatsResourceAvailIndOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsResourceAvailIndOuts.setStatus(_A)
_H225RasStatsResourceAvailConfIns_Type=Counter32
_H225RasStatsResourceAvailConfIns_Object=MibScalar
h225RasStatsResourceAvailConfIns=_H225RasStatsResourceAvailConfIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,39),_H225RasStatsResourceAvailConfIns_Type())
h225RasStatsResourceAvailConfIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsResourceAvailConfIns.setStatus(_A)
_H225RasStatsResourceAvailConOuts_Type=Counter32
_H225RasStatsResourceAvailConOuts_Object=MibScalar
h225RasStatsResourceAvailConOuts=_H225RasStatsResourceAvailConOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,40),_H225RasStatsResourceAvailConOuts_Type())
h225RasStatsResourceAvailConOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsResourceAvailConOuts.setStatus(_A)
_H225RasStatsRequestInProgIns_Type=Counter32
_H225RasStatsRequestInProgIns_Object=MibScalar
h225RasStatsRequestInProgIns=_H225RasStatsRequestInProgIns_Object((1,3,6,1,4,1,9,9,397,1,2,1,41),_H225RasStatsRequestInProgIns_Type())
h225RasStatsRequestInProgIns.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsRequestInProgIns.setStatus(_A)
_H225RasStatsRequestInProgOuts_Type=Counter32
_H225RasStatsRequestInProgOuts_Object=MibScalar
h225RasStatsRequestInProgOuts=_H225RasStatsRequestInProgOuts_Object((1,3,6,1,4,1,9,9,397,1,2,1,42),_H225RasStatsRequestInProgOuts_Type())
h225RasStatsRequestInProgOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:h225RasStatsRequestInProgOuts.setStatus(_A)
_H225MIBConformance_ObjectIdentity=ObjectIdentity
h225MIBConformance=_H225MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,397,1,3))
_H225MIBCompliances_ObjectIdentity=ObjectIdentity
h225MIBCompliances=_H225MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,397,1,3,1))
_H225MIBGroups_ObjectIdentity=ObjectIdentity
h225MIBGroups=_H225MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,397,1,3,2))
_H225DisconnectCauseCode_ObjectIdentity=ObjectIdentity
h225DisconnectCauseCode=_H225DisconnectCauseCode_ObjectIdentity((1,3,6,1,4,1,9,9,397,1,4))
_H225DisconnectCauseCodeTable_Object=MibTable
h225DisconnectCauseCodeTable=_H225DisconnectCauseCodeTable_Object((1,3,6,1,4,1,9,9,397,1,4,1))
if mibBuilder.loadTexts:h225DisconnectCauseCodeTable.setStatus(_A)
_H225DisconnectCauseCodeEntry_Object=MibTableRow
h225DisconnectCauseCodeEntry=_H225DisconnectCauseCodeEntry_Object((1,3,6,1,4,1,9,9,397,1,4,1,1))
h225DisconnectCauseCodeEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:h225DisconnectCauseCodeEntry.setStatus(_A)
_H225CauseCode_Type=CauseCodeType
_H225CauseCode_Object=MibTableColumn
h225CauseCode=_H225CauseCode_Object((1,3,6,1,4,1,9,9,397,1,4,1,1,1),_H225CauseCode_Type())
h225CauseCode.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h225CauseCode.setStatus(_A)
_H225CauseCodeDescription_Type=DisplayString
_H225CauseCodeDescription_Object=MibTableColumn
h225CauseCodeDescription=_H225CauseCodeDescription_Object((1,3,6,1,4,1,9,9,397,1,4,1,1,2),_H225CauseCodeDescription_Type())
h225CauseCodeDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:h225CauseCodeDescription.setStatus(_A)
_H225FromOtherPeerDisconnects_Type=Counter32
_H225FromOtherPeerDisconnects_Object=MibTableColumn
h225FromOtherPeerDisconnects=_H225FromOtherPeerDisconnects_Object((1,3,6,1,4,1,9,9,397,1,4,1,1,3),_H225FromOtherPeerDisconnects_Type())
h225FromOtherPeerDisconnects.setMaxAccess(_C)
if mibBuilder.loadTexts:h225FromOtherPeerDisconnects.setStatus(_A)
_H225FromH323PeerDisconnects_Type=Counter32
_H225FromH323PeerDisconnects_Object=MibTableColumn
h225FromH323PeerDisconnects=_H225FromH323PeerDisconnects_Object((1,3,6,1,4,1,9,9,397,1,4,1,1,4),_H225FromH323PeerDisconnects_Type())
h225FromH323PeerDisconnects.setMaxAccess(_C)
if mibBuilder.loadTexts:h225FromH323PeerDisconnects.setStatus(_A)
h225CallSignalStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,397,1,3,2,1))
h225CallSignalStatsGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:h225CallSignalStatsGroup.setStatus(_A)
h225RasStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,397,1,3,2,2))
h225RasStatsGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:h225RasStatsGroup.setStatus(_A)
h225DisconnectCauseCodeGroup=ObjectGroup((1,3,6,1,4,1,9,9,397,1,3,2,3))
h225DisconnectCauseCodeGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:h225DisconnectCauseCodeGroup.setStatus(_A)
h225MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,397,1,3,1,1))
h225MIBCompliance.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:h225MIBCompliance.setStatus('deprecated')
h225MIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,397,1,3,1,2))
h225MIBComplianceRev1.setObjects(*((_B,_D),(_B,_E),(_B,_AZ)))
if mibBuilder.loadTexts:h225MIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CauseCodeType':CauseCodeType,'ciscoH225MIB':ciscoH225MIB,'h225MIBObjects':h225MIBObjects,'h225CallSignal':h225CallSignal,'h225CallSignalStats':h225CallSignalStats,_G:h225CallSignalStatsSetupIns,_H:h225CallSignalStatsSetupOuts,_I:h225CallSignalStatsSetupFails,_J:h225CallSignalStatsSetupConfIns,_K:h225CallSignalStatsSetupConfOuts,_L:h225CallSignalStatsSetupConFails,_M:h225CallSignalStatsAlertingIns,_N:h225CallSignalStatsAlertingOuts,_O:h225CallSignalStatsAlertingFails,_P:h225CallSignalStatsProgIns,_Q:h225CallSignalStatsProgOuts,_R:h225CallSignalStatsProgFails,_S:h225CallSignalStatsCallProcsIns,_T:h225CallSignalStatsCallProcsOuts,_U:h225CallSignalStatsCallProcFails,_V:h225CallSignalStatsNotifyIns,_W:h225CallSignalStatsNotifyOuts,_X:h225CallSignalStatsNotifyFails,_Y:h225CallSignalStatsInfoIns,_Z:h225CallSignalStatsInfoOuts,_a:h225CallSignalStatsInfoFails,_b:h225CallSignalStatsUserInfoIns,_c:h225CallSignalStatsUserInfoOuts,_d:h225CallSignalStatsUserInfoFails,_e:h225CallSignalStatsFacilityIns,_f:h225CallSignalStatsFacilityOuts,_g:h225CallSignalStatsFacilityFails,_h:h225CallSignalStatsReleaseIns,_i:h225CallSignalStatsReleaseOuts,_j:h225CallSignalStatsReleaseFails,_k:h225CallSignalStatsRejectIns,_l:h225CallSignalStatsRejectOuts,_m:h225CallSignalStatsRejectFails,_n:h225CallSignalStatsPassthroIns,_o:h225CallSignalStatsPassthroOuts,_p:h225CallSignalStatsPassthroFails,'h225Ras':h225Ras,'h225RasStats':h225RasStats,_q:h225RasStatsGkDiscoveryReqIns,_r:h225RasStatsGkDiscoveryReqOuts,_s:h225RasStatsGkDiscoveryConfIns,_t:h225RasStatsGkDiscoveryConfOuts,_u:h225RasStatsGkDiscoveryRejectIns,_v:h225RasStatsGkDiscoveryRejOuts,_w:h225RasStatsRegistrationReqIns,_x:h225RasStatsRegistrationReqOuts,_y:h225RasStatsRegistrationConfIns,_z:h225RasStatsRegistrationConfOuts,_A0:h225RasStatsRegistrationRejIns,_A1:h225RasStatsRegistrationRejOuts,_A2:h225RasStatsAdmissionReqIns,_A3:h225RasStatsAdmissionReqOuts,_A4:h225RasStatsAdmissionConfirmIns,_A5:h225RasStatsAdmissionConfirmOuts,_A6:h225RasStatsAdmissionRejectIns,_A7:h225RasStatsAdmissionRejectOuts,_A8:h225RasStatsBandwidthReqIns,_A9:h225RasStatsBandwidthReqOuts,_AA:h225RasStatsBandwidthConfirmIns,_AB:h225RasStatsBandwidthConfirmOuts,_AC:h225RasStatsBandwidthRejectIns,_AD:h225RasStatsBandwidthRejectOuts,_AE:h225RasStatsDisengageReqIns,_AF:h225RasStatsDisengageReqOuts,_AG:h225RasStatsDisengageConfirmIns,_AH:h225RasStatsDisengageConfirmOuts,_AI:h225RasStatsDisengageRejectIns,_AJ:h225RasStatsDisengageRejectOuts,_AK:h225RasStatsUnregisterReqIns,_AL:h225RasStatsUnregisterReqOuts,_AM:h225RasStatsUnregisterConfirmIns,_AN:h225RasStatsUnregisterConfOuts,_AO:h225RasStatsUnregisterRejectIns,_AP:h225RasStatsUnregisterRejectOuts,_AQ:h225RasStatsResourceAvailIndIns,_AR:h225RasStatsResourceAvailIndOuts,_AS:h225RasStatsResourceAvailConfIns,_AT:h225RasStatsResourceAvailConOuts,_AU:h225RasStatsRequestInProgIns,_AV:h225RasStatsRequestInProgOuts,'h225MIBConformance':h225MIBConformance,'h225MIBCompliances':h225MIBCompliances,'h225MIBCompliance':h225MIBCompliance,'h225MIBComplianceRev1':h225MIBComplianceRev1,'h225MIBGroups':h225MIBGroups,_D:h225CallSignalStatsGroup,_E:h225RasStatsGroup,_AZ:h225DisconnectCauseCodeGroup,'h225DisconnectCauseCode':h225DisconnectCauseCode,'h225DisconnectCauseCodeTable':h225DisconnectCauseCodeTable,'h225DisconnectCauseCodeEntry':h225DisconnectCauseCodeEntry,_F:h225CauseCode,_AW:h225CauseCodeDescription,_AX:h225FromOtherPeerDisconnects,_AY:h225FromH323PeerDisconnects})