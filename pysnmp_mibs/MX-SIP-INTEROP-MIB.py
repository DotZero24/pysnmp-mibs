_A4='sipInteropGroupVer1'
_A3='sipInteropInternationalCodeMappingString'
_A2='sipInteropInternationalCodeMappingEnable'
_A1='sipInteropDtmfTransportDuration'
_A0='sipInteropDtmfTransportMethod'
_z='sipInteropFromUriDomainSelection'
_y='sipInteropAllowAsymmetricDtmfPayloadType'
_x='sipInteropUseDtmfPayloadTypeFoundInAnswer'
_w='sipInteropProxyAuthenticationUriParametersEnable'
_v='sipInteropAuthenticationQop'
_u='sipInteropDefaultPublicationExpiration'
_t='sipInteropDefaultRegistrationExpiration'
_s='sipInteropIgnoreViaBranchIdInCancelEnable'
_r='sipInteropBranchMatchingMethod'
_q='sipInteropAckUnsupportedInfoRequests'
_p='sipInteropRejectCodeForNoRessource'
_o='sipInteropRingingResponseCode'
_n='sipInteropUsePAssertedHeader'
_m='sipInteropReuseCredentialEnable'
_l='sipInteropRemoveOutboundProxyRouteHeader'
_k='sipInteropLockDnsSrvRecordPerCallEnable'
_j='sipInteropBehaviorOnT38InviteRejectedWith606'
_i='sipInteropT38NoSignalBehavior'
_h='sipInteropUseItuT38Format'
_g='sipInteropConferenceServerMechanism'
_f='sipInteropReferredByConfig'
_e='sipInteropRetryFailedRegistration'
_d='sipInteropRegisterHomeDomainHostOverride'
_c='sipInteropIgnoreUsernameParam'
_b='sipInteropSdpOriginLineSessionIDAndVersionMaxLength'
_a='sipInteropCallWaitingToneControlViaSipInfo'
_Z='sipInteropLocalRingOnProvisionalResponse'
_Y='sipInteropSipOptionsMethodSupport'
_X='sipInteropMwiMessageSummaryValidation'
_W='sipInteropIgnoreMediaRenegotiationAfterCngDetection'
_V='sipInteropOnHoldAnswerSdpStreamDirection'
_U='sipInteropOnHoldSdpStreamDirection'
_T='sipInteropAllowMultipleActiveMediaInAnswer'
_S='sipInteropSdpDirectionAttributeEnable'
_R='sipInteropUAHeaderConfig'
_Q='sipInteropSendUAHeaderEnable'
_P='sipInteropAutomaticRejectionCode'
_O='sipInteropMaxForwardsValue'
_N='sipInteropSymmetricUdpSourcePortEnable'
_M='sipInteropReplacesVersion'
_L='sipInteropTransmissionTimeout'
_K='sipInteropSessionTimerVersion'
_J='sipInteropTransferVersion'
_I='sipInteropReplacesConfig'
_H='inactive'
_G='OctetString'
_F='Unsigned32'
_E='Integer32'
_D='MxEnableState'
_C='MX-SIP-INTEROP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sipInteropMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,20))
if mibBuilder.loadTexts:sipInteropMIB.setRevisions(('2010-12-10 00:00','2010-10-05 00:00','2009-10-28 00:00','2009-09-30 00:00','2009-08-10 00:00','2009-04-23 00:00','2009-03-27 00:00','2008-11-26 00:00','2008-11-18 00:00','2008-10-31 00:00','2008-10-17 00:00','2008-06-12 00:00','2008-03-03 00:00','2008-01-11 00:00','2007-08-08 00:00','2007-08-06 00:00','2007-08-01 00:00','2007-07-18 00:00','2007-07-03 00:00','2007-06-20 00:00','2007-06-14 00:00','2007-05-28 00:00','2007-05-03 00:00','2007-04-18 00:00','2007-02-02 00:00','2007-02-23 00:00','2006-05-24 00:00','2005-10-07 00:00','2005-06-28 00:00','2005-05-20 00:00','2005-01-25 00:00','2005-01-10 00:00','2004-12-22 00:00','2004-11-02 00:00','2004-10-25 00:00','2004-10-04 00:00','2004-09-29 00:00','2004-09-21 00:00','2004-07-28 00:00','2004-06-14 00:00','2004-06-02 00:00','2004-04-27 00:00','2004-04-21 00:00','2004-03-25 00:00','2004-02-13 00:00','2003-11-17 00:00','2003-11-06 00:00','2003-11-05 00:00','2003-11-03 00:00','2003-03-11 00:00','2002-10-28 00:00','2002-10-16 00:00','2002-10-01 00:00'))
_SipInteropMIBObjects_ObjectIdentity=ObjectIdentity
sipInteropMIBObjects=_SipInteropMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,20,1))
class _SipInteropReplacesConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('doNotUseReplaces',0),('useReplacesWithRequire',1),('useReplacesNoRequire',2)))
_SipInteropReplacesConfig_Type.__name__=_E
_SipInteropReplacesConfig_Object=MibScalar
sipInteropReplacesConfig=_SipInteropReplacesConfig_Object((1,3,6,1,4,1,4935,99,20,1,5),_SipInteropReplacesConfig_Type())
sipInteropReplacesConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropReplacesConfig.setStatus(_A)
class _SipInteropTransferVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('transfer02',0),('transfer05UsingRefer02',1),('sippingTransfer01UsingReferRfc3515',2)))
_SipInteropTransferVersion_Type.__name__=_E
_SipInteropTransferVersion_Object=MibScalar
sipInteropTransferVersion=_SipInteropTransferVersion_Object((1,3,6,1,4,1,4935,99,20,1,10),_SipInteropTransferVersion_Type())
sipInteropTransferVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropTransferVersion.setStatus(_A)
class _SipInteropSessionTimerVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('sessionTimer04',0),('sessionTimer08',1)))
_SipInteropSessionTimerVersion_Type.__name__=_E
_SipInteropSessionTimerVersion_Object=MibScalar
sipInteropSessionTimerVersion=_SipInteropSessionTimerVersion_Object((1,3,6,1,4,1,4935,99,20,1,15),_SipInteropSessionTimerVersion_Type())
sipInteropSessionTimerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropSessionTimerVersion.setStatus(_A)
class _SipInteropTransmissionTimeout_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SipInteropTransmissionTimeout_Type.__name__=_F
_SipInteropTransmissionTimeout_Object=MibScalar
sipInteropTransmissionTimeout=_SipInteropTransmissionTimeout_Object((1,3,6,1,4,1,4935,99,20,1,20),_SipInteropTransmissionTimeout_Type())
sipInteropTransmissionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropTransmissionTimeout.setStatus(_A)
class _SipInteropReplacesVersion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('replaces01',0),('replaces03',1)))
_SipInteropReplacesVersion_Type.__name__=_E
_SipInteropReplacesVersion_Object=MibScalar
sipInteropReplacesVersion=_SipInteropReplacesVersion_Object((1,3,6,1,4,1,4935,99,20,1,25),_SipInteropReplacesVersion_Type())
sipInteropReplacesVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropReplacesVersion.setStatus(_A)
class _SipInteropSymmetricUdpSourcePortEnable_Type(MxEnableState):defaultValue=1
_SipInteropSymmetricUdpSourcePortEnable_Type.__name__=_D
_SipInteropSymmetricUdpSourcePortEnable_Object=MibScalar
sipInteropSymmetricUdpSourcePortEnable=_SipInteropSymmetricUdpSourcePortEnable_Object((1,3,6,1,4,1,4935,99,20,1,30),_SipInteropSymmetricUdpSourcePortEnable_Type())
sipInteropSymmetricUdpSourcePortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropSymmetricUdpSourcePortEnable.setStatus(_A)
class _SipInteropMaxForwardsValue_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,200))
_SipInteropMaxForwardsValue_Type.__name__=_E
_SipInteropMaxForwardsValue_Object=MibScalar
sipInteropMaxForwardsValue=_SipInteropMaxForwardsValue_Object((1,3,6,1,4,1,4935,99,20,1,35),_SipInteropMaxForwardsValue_Type())
sipInteropMaxForwardsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropMaxForwardsValue.setStatus(_A)
class _SipInteropAutomaticRejectionCode_Type(Unsigned32):defaultValue=480;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,699))
_SipInteropAutomaticRejectionCode_Type.__name__=_F
_SipInteropAutomaticRejectionCode_Object=MibScalar
sipInteropAutomaticRejectionCode=_SipInteropAutomaticRejectionCode_Object((1,3,6,1,4,1,4935,99,20,1,40),_SipInteropAutomaticRejectionCode_Type())
sipInteropAutomaticRejectionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropAutomaticRejectionCode.setStatus(_A)
class _SipInteropSendUAHeaderEnable_Type(MxEnableState):defaultValue=1
_SipInteropSendUAHeaderEnable_Type.__name__=_D
_SipInteropSendUAHeaderEnable_Object=MibScalar
sipInteropSendUAHeaderEnable=_SipInteropSendUAHeaderEnable_Object((1,3,6,1,4,1,4935,99,20,1,50),_SipInteropSendUAHeaderEnable_Type())
sipInteropSendUAHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropSendUAHeaderEnable.setStatus(_A)
class _SipInteropUAHeaderConfig_Type(OctetString):defaultValue=OctetString('MxSipApp/%version%');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SipInteropUAHeaderConfig_Type.__name__=_G
_SipInteropUAHeaderConfig_Object=MibScalar
sipInteropUAHeaderConfig=_SipInteropUAHeaderConfig_Object((1,3,6,1,4,1,4935,99,20,1,55),_SipInteropUAHeaderConfig_Type())
sipInteropUAHeaderConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropUAHeaderConfig.setStatus(_A)
class _SipInteropSdpDirectionAttributeEnable_Type(MxEnableState):defaultValue=1
_SipInteropSdpDirectionAttributeEnable_Type.__name__=_D
_SipInteropSdpDirectionAttributeEnable_Object=MibScalar
sipInteropSdpDirectionAttributeEnable=_SipInteropSdpDirectionAttributeEnable_Object((1,3,6,1,4,1,4935,99,20,1,75),_SipInteropSdpDirectionAttributeEnable_Type())
sipInteropSdpDirectionAttributeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropSdpDirectionAttributeEnable.setStatus(_A)
class _SipInteropAllowMultipleActiveMediaInAnswer_Type(MxEnableState):defaultValue=1
_SipInteropAllowMultipleActiveMediaInAnswer_Type.__name__=_D
_SipInteropAllowMultipleActiveMediaInAnswer_Object=MibScalar
sipInteropAllowMultipleActiveMediaInAnswer=_SipInteropAllowMultipleActiveMediaInAnswer_Object((1,3,6,1,4,1,4935,99,20,1,95),_SipInteropAllowMultipleActiveMediaInAnswer_Type())
sipInteropAllowMultipleActiveMediaInAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropAllowMultipleActiveMediaInAnswer.setStatus(_A)
class _SipInteropOnHoldSdpStreamDirection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('sendonly',1)))
_SipInteropOnHoldSdpStreamDirection_Type.__name__=_E
_SipInteropOnHoldSdpStreamDirection_Object=MibScalar
sipInteropOnHoldSdpStreamDirection=_SipInteropOnHoldSdpStreamDirection_Object((1,3,6,1,4,1,4935,99,20,1,100),_SipInteropOnHoldSdpStreamDirection_Type())
sipInteropOnHoldSdpStreamDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropOnHoldSdpStreamDirection.setStatus(_A)
class _SipInteropOnHoldAnswerSdpStreamDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('recvonly',1)))
_SipInteropOnHoldAnswerSdpStreamDirection_Type.__name__=_E
_SipInteropOnHoldAnswerSdpStreamDirection_Object=MibScalar
sipInteropOnHoldAnswerSdpStreamDirection=_SipInteropOnHoldAnswerSdpStreamDirection_Object((1,3,6,1,4,1,4935,99,20,1,105),_SipInteropOnHoldAnswerSdpStreamDirection_Type())
sipInteropOnHoldAnswerSdpStreamDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropOnHoldAnswerSdpStreamDirection.setStatus(_A)
class _SipInteropIgnoreMediaRenegotiationAfterCngDetection_Type(MxEnableState):defaultValue=0
_SipInteropIgnoreMediaRenegotiationAfterCngDetection_Type.__name__=_D
_SipInteropIgnoreMediaRenegotiationAfterCngDetection_Object=MibScalar
sipInteropIgnoreMediaRenegotiationAfterCngDetection=_SipInteropIgnoreMediaRenegotiationAfterCngDetection_Object((1,3,6,1,4,1,4935,99,20,1,110),_SipInteropIgnoreMediaRenegotiationAfterCngDetection_Type())
sipInteropIgnoreMediaRenegotiationAfterCngDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropIgnoreMediaRenegotiationAfterCngDetection.setStatus(_A)
class _SipInteropMwiMessageSummaryValidation_Type(MxEnableState):defaultValue=1
_SipInteropMwiMessageSummaryValidation_Type.__name__=_D
_SipInteropMwiMessageSummaryValidation_Object=MibScalar
sipInteropMwiMessageSummaryValidation=_SipInteropMwiMessageSummaryValidation_Object((1,3,6,1,4,1,4935,99,20,1,125),_SipInteropMwiMessageSummaryValidation_Type())
sipInteropMwiMessageSummaryValidation.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropMwiMessageSummaryValidation.setStatus(_A)
class _SipInteropSipOptionsMethodSupport_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('alwaysOk',1)))
_SipInteropSipOptionsMethodSupport_Type.__name__=_E
_SipInteropSipOptionsMethodSupport_Object=MibScalar
sipInteropSipOptionsMethodSupport=_SipInteropSipOptionsMethodSupport_Object((1,3,6,1,4,1,4935,99,20,1,130),_SipInteropSipOptionsMethodSupport_Type())
sipInteropSipOptionsMethodSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropSipOptionsMethodSupport.setStatus(_A)
class _SipInteropLocalRingOnProvisionalResponse_Type(MxEnableState):defaultValue=0
_SipInteropLocalRingOnProvisionalResponse_Type.__name__=_D
_SipInteropLocalRingOnProvisionalResponse_Object=MibScalar
sipInteropLocalRingOnProvisionalResponse=_SipInteropLocalRingOnProvisionalResponse_Object((1,3,6,1,4,1,4935,99,20,1,150),_SipInteropLocalRingOnProvisionalResponse_Type())
sipInteropLocalRingOnProvisionalResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropLocalRingOnProvisionalResponse.setStatus(_A)
class _SipInteropCallWaitingToneControlViaSipInfo_Type(MxEnableState):defaultValue=0
_SipInteropCallWaitingToneControlViaSipInfo_Type.__name__=_D
_SipInteropCallWaitingToneControlViaSipInfo_Object=MibScalar
sipInteropCallWaitingToneControlViaSipInfo=_SipInteropCallWaitingToneControlViaSipInfo_Object((1,3,6,1,4,1,4935,99,20,1,175),_SipInteropCallWaitingToneControlViaSipInfo_Type())
sipInteropCallWaitingToneControlViaSipInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropCallWaitingToneControlViaSipInfo.setStatus(_A)
class _SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20)));namedValues=NamedValues(*(('max-32bits',10),('max-64bits',20)))
_SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Type.__name__=_E
_SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Object=MibScalar
sipInteropSdpOriginLineSessionIDAndVersionMaxLength=_SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Object((1,3,6,1,4,1,4935,99,20,1,200),_SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Type())
sipInteropSdpOriginLineSessionIDAndVersionMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropSdpOriginLineSessionIDAndVersionMaxLength.setStatus(_A)
class _SipInteropIgnoreUsernameParam_Type(MxEnableState):defaultValue=0
_SipInteropIgnoreUsernameParam_Type.__name__=_D
_SipInteropIgnoreUsernameParam_Object=MibScalar
sipInteropIgnoreUsernameParam=_SipInteropIgnoreUsernameParam_Object((1,3,6,1,4,1,4935,99,20,1,210),_SipInteropIgnoreUsernameParam_Type())
sipInteropIgnoreUsernameParam.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropIgnoreUsernameParam.setStatus(_A)
class _SipInteropEscapePoundInSipUriUsername_Type(MxEnableState):defaultValue=1
_SipInteropEscapePoundInSipUriUsername_Type.__name__=_D
_SipInteropEscapePoundInSipUriUsername_Object=MibScalar
sipInteropEscapePoundInSipUriUsername=_SipInteropEscapePoundInSipUriUsername_Object((1,3,6,1,4,1,4935,99,20,1,215),_SipInteropEscapePoundInSipUriUsername_Type())
sipInteropEscapePoundInSipUriUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropEscapePoundInSipUriUsername.setStatus(_A)
class _SipInteropRegisterHomeDomainHostOverride_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SipInteropRegisterHomeDomainHostOverride_Type.__name__=_G
_SipInteropRegisterHomeDomainHostOverride_Object=MibScalar
sipInteropRegisterHomeDomainHostOverride=_SipInteropRegisterHomeDomainHostOverride_Object((1,3,6,1,4,1,4935,99,20,1,225),_SipInteropRegisterHomeDomainHostOverride_Type())
sipInteropRegisterHomeDomainHostOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropRegisterHomeDomainHostOverride.setStatus(_A)
class _SipInteropRetryFailedRegistration_Type(MxEnableState):defaultValue=1
_SipInteropRetryFailedRegistration_Type.__name__=_D
_SipInteropRetryFailedRegistration_Object=MibScalar
sipInteropRetryFailedRegistration=_SipInteropRetryFailedRegistration_Object((1,3,6,1,4,1,4935,99,20,1,235),_SipInteropRetryFailedRegistration_Type())
sipInteropRetryFailedRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropRetryFailedRegistration.setStatus(_A)
class _SipInteropUseSipDomainInRequestURI_Type(MxEnableState):defaultValue=0
_SipInteropUseSipDomainInRequestURI_Type.__name__=_D
_SipInteropUseSipDomainInRequestURI_Object=MibScalar
sipInteropUseSipDomainInRequestURI=_SipInteropUseSipDomainInRequestURI_Object((1,3,6,1,4,1,4935,99,20,1,240),_SipInteropUseSipDomainInRequestURI_Type())
sipInteropUseSipDomainInRequestURI.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropUseSipDomainInRequestURI.setStatus(_A)
class _SipInteropReferredByConfig_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('useSipStackDefault',0),('useLocalUrl',1)))
_SipInteropReferredByConfig_Type.__name__=_E
_SipInteropReferredByConfig_Object=MibScalar
sipInteropReferredByConfig=_SipInteropReferredByConfig_Object((1,3,6,1,4,1,4935,99,20,1,250),_SipInteropReferredByConfig_Type())
sipInteropReferredByConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropReferredByConfig.setStatus(_A)
class _SipInteropConferenceServerMechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rfc4579WithoutErrorRecovery',0),('rfc4579WithErrorRecovery',1)))
_SipInteropConferenceServerMechanism_Type.__name__=_E
_SipInteropConferenceServerMechanism_Object=MibScalar
sipInteropConferenceServerMechanism=_SipInteropConferenceServerMechanism_Object((1,3,6,1,4,1,4935,99,20,1,255),_SipInteropConferenceServerMechanism_Type())
sipInteropConferenceServerMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropConferenceServerMechanism.setStatus(_A)
class _SipInteropUseItuT38Format_Type(MxEnableState):defaultValue=0
_SipInteropUseItuT38Format_Type.__name__=_D
_SipInteropUseItuT38Format_Object=MibScalar
sipInteropUseItuT38Format=_SipInteropUseItuT38Format_Object((1,3,6,1,4,1,4935,99,20,1,275),_SipInteropUseItuT38Format_Type())
sipInteropUseItuT38Format.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropUseItuT38Format.setStatus(_A)
class _SipInteropT38NoSignalBehavior_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('receivingReInvite',0),('receivingAck',1)))
_SipInteropT38NoSignalBehavior_Type.__name__=_E
_SipInteropT38NoSignalBehavior_Object=MibScalar
sipInteropT38NoSignalBehavior=_SipInteropT38NoSignalBehavior_Object((1,3,6,1,4,1,4935,99,20,1,285),_SipInteropT38NoSignalBehavior_Type())
sipInteropT38NoSignalBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropT38NoSignalBehavior.setStatus(_A)
class _SipInteropBehaviorOnT38InviteRejectedWith606_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*(('dropCall',1),('usePreviousMediaNegotiation',4)))
_SipInteropBehaviorOnT38InviteRejectedWith606_Type.__name__=_E
_SipInteropBehaviorOnT38InviteRejectedWith606_Object=MibScalar
sipInteropBehaviorOnT38InviteRejectedWith606=_SipInteropBehaviorOnT38InviteRejectedWith606_Object((1,3,6,1,4,1,4935,99,20,1,290),_SipInteropBehaviorOnT38InviteRejectedWith606_Type())
sipInteropBehaviorOnT38InviteRejectedWith606.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropBehaviorOnT38InviteRejectedWith606.setStatus(_A)
class _SipInteropLockDnsSrvRecordPerCallEnable_Type(MxEnableState):defaultValue=0
_SipInteropLockDnsSrvRecordPerCallEnable_Type.__name__=_D
_SipInteropLockDnsSrvRecordPerCallEnable_Object=MibScalar
sipInteropLockDnsSrvRecordPerCallEnable=_SipInteropLockDnsSrvRecordPerCallEnable_Object((1,3,6,1,4,1,4935,99,20,1,300),_SipInteropLockDnsSrvRecordPerCallEnable_Type())
sipInteropLockDnsSrvRecordPerCallEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropLockDnsSrvRecordPerCallEnable.setStatus(_A)
class _SipInteropRemoveOutboundProxyRouteHeader_Type(MxEnableState):defaultValue=0
_SipInteropRemoveOutboundProxyRouteHeader_Type.__name__=_D
_SipInteropRemoveOutboundProxyRouteHeader_Object=MibScalar
sipInteropRemoveOutboundProxyRouteHeader=_SipInteropRemoveOutboundProxyRouteHeader_Object((1,3,6,1,4,1,4935,99,20,1,325),_SipInteropRemoveOutboundProxyRouteHeader_Type())
sipInteropRemoveOutboundProxyRouteHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropRemoveOutboundProxyRouteHeader.setStatus(_A)
class _SipInteropReuseCredentialEnable_Type(MxEnableState):defaultValue=1
_SipInteropReuseCredentialEnable_Type.__name__=_D
_SipInteropReuseCredentialEnable_Object=MibScalar
sipInteropReuseCredentialEnable=_SipInteropReuseCredentialEnable_Object((1,3,6,1,4,1,4935,99,20,1,350),_SipInteropReuseCredentialEnable_Type())
sipInteropReuseCredentialEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropReuseCredentialEnable.setStatus(_A)
class _SipInteropUsePAssertedHeader_Type(MxEnableState):defaultValue=0
_SipInteropUsePAssertedHeader_Type.__name__=_D
_SipInteropUsePAssertedHeader_Object=MibScalar
sipInteropUsePAssertedHeader=_SipInteropUsePAssertedHeader_Object((1,3,6,1,4,1,4935,99,20,1,360),_SipInteropUsePAssertedHeader_Type())
sipInteropUsePAssertedHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropUsePAssertedHeader.setStatus(_A)
class _SipInteropRingingResponseCode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('send180Ringing',0),('send183WithSdp',1)))
_SipInteropRingingResponseCode_Type.__name__=_E
_SipInteropRingingResponseCode_Object=MibScalar
sipInteropRingingResponseCode=_SipInteropRingingResponseCode_Object((1,3,6,1,4,1,4935,99,20,1,375),_SipInteropRingingResponseCode_Type())
sipInteropRingingResponseCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropRingingResponseCode.setStatus(_A)
class _SipInteropRejectCodeForNoRessource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('temporarilyUnavailable',0),('busyHere',1)))
_SipInteropRejectCodeForNoRessource_Type.__name__=_E
_SipInteropRejectCodeForNoRessource_Object=MibScalar
sipInteropRejectCodeForNoRessource=_SipInteropRejectCodeForNoRessource_Object((1,3,6,1,4,1,4935,99,20,1,400),_SipInteropRejectCodeForNoRessource_Type())
sipInteropRejectCodeForNoRessource.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropRejectCodeForNoRessource.setStatus(_A)
class _SipInteropAckUnsupportedInfoRequests_Type(MxEnableState):defaultValue=0
_SipInteropAckUnsupportedInfoRequests_Type.__name__=_D
_SipInteropAckUnsupportedInfoRequests_Object=MibScalar
sipInteropAckUnsupportedInfoRequests=_SipInteropAckUnsupportedInfoRequests_Object((1,3,6,1,4,1,4935,99,20,1,415),_SipInteropAckUnsupportedInfoRequests_Type())
sipInteropAckUnsupportedInfoRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropAckUnsupportedInfoRequests.setStatus(_A)
class _SipInteropBranchMatchingMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rfc2543',0),('rfc3261',1)))
_SipInteropBranchMatchingMethod_Type.__name__=_E
_SipInteropBranchMatchingMethod_Object=MibScalar
sipInteropBranchMatchingMethod=_SipInteropBranchMatchingMethod_Object((1,3,6,1,4,1,4935,99,20,1,425),_SipInteropBranchMatchingMethod_Type())
sipInteropBranchMatchingMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropBranchMatchingMethod.setStatus(_A)
class _SipInteropIgnoreViaBranchIdInCancelEnable_Type(MxEnableState):defaultValue=0
_SipInteropIgnoreViaBranchIdInCancelEnable_Type.__name__=_D
_SipInteropIgnoreViaBranchIdInCancelEnable_Object=MibScalar
sipInteropIgnoreViaBranchIdInCancelEnable=_SipInteropIgnoreViaBranchIdInCancelEnable_Object((1,3,6,1,4,1,4935,99,20,1,432),_SipInteropIgnoreViaBranchIdInCancelEnable_Type())
sipInteropIgnoreViaBranchIdInCancelEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropIgnoreViaBranchIdInCancelEnable.setStatus(_A)
class _SipInteropDefaultRegistrationExpiration_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_SipInteropDefaultRegistrationExpiration_Type.__name__=_F
_SipInteropDefaultRegistrationExpiration_Object=MibScalar
sipInteropDefaultRegistrationExpiration=_SipInteropDefaultRegistrationExpiration_Object((1,3,6,1,4,1,4935,99,20,1,438),_SipInteropDefaultRegistrationExpiration_Type())
sipInteropDefaultRegistrationExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropDefaultRegistrationExpiration.setStatus(_A)
class _SipInteropDefaultPublicationExpiration_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_SipInteropDefaultPublicationExpiration_Type.__name__=_F
_SipInteropDefaultPublicationExpiration_Object=MibScalar
sipInteropDefaultPublicationExpiration=_SipInteropDefaultPublicationExpiration_Object((1,3,6,1,4,1,4935,99,20,1,439),_SipInteropDefaultPublicationExpiration_Type())
sipInteropDefaultPublicationExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropDefaultPublicationExpiration.setStatus(_A)
class _SipInteropAuthenticationQop_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('auth',0),('auth-int',1)))
_SipInteropAuthenticationQop_Type.__name__=_E
_SipInteropAuthenticationQop_Object=MibScalar
sipInteropAuthenticationQop=_SipInteropAuthenticationQop_Object((1,3,6,1,4,1,4935,99,20,1,444),_SipInteropAuthenticationQop_Type())
sipInteropAuthenticationQop.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropAuthenticationQop.setStatus(_A)
class _SipInteropProxyAuthenticationUriParametersEnable_Type(MxEnableState):defaultValue=1
_SipInteropProxyAuthenticationUriParametersEnable_Type.__name__=_D
_SipInteropProxyAuthenticationUriParametersEnable_Object=MibScalar
sipInteropProxyAuthenticationUriParametersEnable=_SipInteropProxyAuthenticationUriParametersEnable_Object((1,3,6,1,4,1,4935,99,20,1,445),_SipInteropProxyAuthenticationUriParametersEnable_Type())
sipInteropProxyAuthenticationUriParametersEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropProxyAuthenticationUriParametersEnable.setStatus(_A)
class _SipInteropUseDtmfPayloadTypeFoundInAnswer_Type(MxEnableState):defaultValue=0
_SipInteropUseDtmfPayloadTypeFoundInAnswer_Type.__name__=_D
_SipInteropUseDtmfPayloadTypeFoundInAnswer_Object=MibScalar
sipInteropUseDtmfPayloadTypeFoundInAnswer=_SipInteropUseDtmfPayloadTypeFoundInAnswer_Object((1,3,6,1,4,1,4935,99,20,1,447),_SipInteropUseDtmfPayloadTypeFoundInAnswer_Type())
sipInteropUseDtmfPayloadTypeFoundInAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropUseDtmfPayloadTypeFoundInAnswer.setStatus(_A)
class _SipInteropAllowAsymmetricDtmfPayloadType_Type(MxEnableState):defaultValue=0
_SipInteropAllowAsymmetricDtmfPayloadType_Type.__name__=_D
_SipInteropAllowAsymmetricDtmfPayloadType_Object=MibScalar
sipInteropAllowAsymmetricDtmfPayloadType=_SipInteropAllowAsymmetricDtmfPayloadType_Object((1,3,6,1,4,1,4935,99,20,1,448),_SipInteropAllowAsymmetricDtmfPayloadType_Type())
sipInteropAllowAsymmetricDtmfPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropAllowAsymmetricDtmfPayloadType.setStatus(_A)
class _SipInteropFromUriDomainSelection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('sipDomain',0),('localHostWanAddress',1),('localHostFqdn',2)))
_SipInteropFromUriDomainSelection_Type.__name__=_E
_SipInteropFromUriDomainSelection_Object=MibScalar
sipInteropFromUriDomainSelection=_SipInteropFromUriDomainSelection_Object((1,3,6,1,4,1,4935,99,20,1,449),_SipInteropFromUriDomainSelection_Type())
sipInteropFromUriDomainSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropFromUriDomainSelection.setStatus(_A)
_SipInteropDtmfTransportBySipProtocol_ObjectIdentity=ObjectIdentity
sipInteropDtmfTransportBySipProtocol=_SipInteropDtmfTransportBySipProtocol_ObjectIdentity((1,3,6,1,4,1,4935,99,20,1,450))
class _SipInteropDtmfTransportMethod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('draftChoudhuriSipInfoDigit00',0),('infoDtmfRelay',1)))
_SipInteropDtmfTransportMethod_Type.__name__=_E
_SipInteropDtmfTransportMethod_Object=MibScalar
sipInteropDtmfTransportMethod=_SipInteropDtmfTransportMethod_Object((1,3,6,1,4,1,4935,99,20,1,450,50),_SipInteropDtmfTransportMethod_Type())
sipInteropDtmfTransportMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropDtmfTransportMethod.setStatus(_A)
class _SipInteropDtmfTransportDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,2000))
_SipInteropDtmfTransportDuration_Type.__name__=_E
_SipInteropDtmfTransportDuration_Object=MibScalar
sipInteropDtmfTransportDuration=_SipInteropDtmfTransportDuration_Object((1,3,6,1,4,1,4935,99,20,1,450,100),_SipInteropDtmfTransportDuration_Type())
sipInteropDtmfTransportDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropDtmfTransportDuration.setStatus(_A)
_SipInteropInternationalCodeMapping_ObjectIdentity=ObjectIdentity
sipInteropInternationalCodeMapping=_SipInteropInternationalCodeMapping_ObjectIdentity((1,3,6,1,4,1,4935,99,20,1,500))
class _SipInteropInternationalCodeMappingEnable_Type(MxEnableState):defaultValue=0
_SipInteropInternationalCodeMappingEnable_Type.__name__=_D
_SipInteropInternationalCodeMappingEnable_Object=MibScalar
sipInteropInternationalCodeMappingEnable=_SipInteropInternationalCodeMappingEnable_Object((1,3,6,1,4,1,4935,99,20,1,500,50),_SipInteropInternationalCodeMappingEnable_Type())
sipInteropInternationalCodeMappingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropInternationalCodeMappingEnable.setStatus(_A)
class _SipInteropInternationalCodeMappingString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_SipInteropInternationalCodeMappingString_Type.__name__=_G
_SipInteropInternationalCodeMappingString_Object=MibScalar
sipInteropInternationalCodeMappingString=_SipInteropInternationalCodeMappingString_Object((1,3,6,1,4,1,4935,99,20,1,500,100),_SipInteropInternationalCodeMappingString_Type())
sipInteropInternationalCodeMappingString.setMaxAccess(_B)
if mibBuilder.loadTexts:sipInteropInternationalCodeMappingString.setStatus(_A)
_SipInteropConformance_ObjectIdentity=ObjectIdentity
sipInteropConformance=_SipInteropConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,20,2))
_SipInteropCompliances_ObjectIdentity=ObjectIdentity
sipInteropCompliances=_SipInteropCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,20,2,1))
_SipInteropGroups_ObjectIdentity=ObjectIdentity
sipInteropGroups=_SipInteropGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,20,2,2))
sipInteropGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,20,2,2,5))
sipInteropGroupVer1.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_C,_g),(_C,_h),(_C,_i),(_C,_j),(_C,_k),(_C,_l),(_C,_m),(_C,_n),(_C,_o),(_C,_p),(_C,_q),(_C,_r),(_C,_s),(_C,_t),(_C,_u),(_C,_v),(_C,_w),(_C,_x),(_C,_y),(_C,_z),(_C,_A0),(_C,_A1),(_C,_A2),(_C,_A3)))
if mibBuilder.loadTexts:sipInteropGroupVer1.setStatus(_A)
sipInteropBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,20,2,1,1))
sipInteropBasicComplVer1.setObjects((_C,_A4))
if mibBuilder.loadTexts:sipInteropBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'sipInteropMIB':sipInteropMIB,'sipInteropMIBObjects':sipInteropMIBObjects,_I:sipInteropReplacesConfig,_J:sipInteropTransferVersion,_K:sipInteropSessionTimerVersion,_L:sipInteropTransmissionTimeout,_M:sipInteropReplacesVersion,_N:sipInteropSymmetricUdpSourcePortEnable,_O:sipInteropMaxForwardsValue,_P:sipInteropAutomaticRejectionCode,_Q:sipInteropSendUAHeaderEnable,_R:sipInteropUAHeaderConfig,_S:sipInteropSdpDirectionAttributeEnable,_T:sipInteropAllowMultipleActiveMediaInAnswer,_U:sipInteropOnHoldSdpStreamDirection,_V:sipInteropOnHoldAnswerSdpStreamDirection,_W:sipInteropIgnoreMediaRenegotiationAfterCngDetection,_X:sipInteropMwiMessageSummaryValidation,_Y:sipInteropSipOptionsMethodSupport,_Z:sipInteropLocalRingOnProvisionalResponse,_a:sipInteropCallWaitingToneControlViaSipInfo,_b:sipInteropSdpOriginLineSessionIDAndVersionMaxLength,_c:sipInteropIgnoreUsernameParam,'sipInteropEscapePoundInSipUriUsername':sipInteropEscapePoundInSipUriUsername,_d:sipInteropRegisterHomeDomainHostOverride,_e:sipInteropRetryFailedRegistration,'sipInteropUseSipDomainInRequestURI':sipInteropUseSipDomainInRequestURI,_f:sipInteropReferredByConfig,_g:sipInteropConferenceServerMechanism,_h:sipInteropUseItuT38Format,_i:sipInteropT38NoSignalBehavior,_j:sipInteropBehaviorOnT38InviteRejectedWith606,_k:sipInteropLockDnsSrvRecordPerCallEnable,_l:sipInteropRemoveOutboundProxyRouteHeader,_m:sipInteropReuseCredentialEnable,_n:sipInteropUsePAssertedHeader,_o:sipInteropRingingResponseCode,_p:sipInteropRejectCodeForNoRessource,_q:sipInteropAckUnsupportedInfoRequests,_r:sipInteropBranchMatchingMethod,_s:sipInteropIgnoreViaBranchIdInCancelEnable,_t:sipInteropDefaultRegistrationExpiration,_u:sipInteropDefaultPublicationExpiration,_v:sipInteropAuthenticationQop,_w:sipInteropProxyAuthenticationUriParametersEnable,_x:sipInteropUseDtmfPayloadTypeFoundInAnswer,_y:sipInteropAllowAsymmetricDtmfPayloadType,_z:sipInteropFromUriDomainSelection,'sipInteropDtmfTransportBySipProtocol':sipInteropDtmfTransportBySipProtocol,_A0:sipInteropDtmfTransportMethod,_A1:sipInteropDtmfTransportDuration,'sipInteropInternationalCodeMapping':sipInteropInternationalCodeMapping,_A2:sipInteropInternationalCodeMappingEnable,_A3:sipInteropInternationalCodeMappingString,'sipInteropConformance':sipInteropConformance,'sipInteropCompliances':sipInteropCompliances,'sipInteropBasicComplVer1':sipInteropBasicComplVer1,'sipInteropGroups':sipInteropGroups,_A4:sipInteropGroupVer1})