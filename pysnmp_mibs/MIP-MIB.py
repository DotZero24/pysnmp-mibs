_Bq='mipSecNotificationsGroup'
_Bp='haRegNodeCountersGroup'
_Bo='haRegistrationGroup'
_Bn='faRegistrationGroup'
_Bm='faAdvertisementGroup'
_Bl='faSystemGroup'
_Bk='maAdvertisementGroup'
_Bj='mnRegistrationGroup'
_Bi='mnDiscoveryGroup'
_Bh='mnSystemGroup'
_Bg='mipSecViolationGroup'
_Bf='mipSecAssociationGroup'
_Be='mipSystemGroup'
_Bd='mipAuthFailure'
_Bc='haRecentServiceDeniedCode'
_Bb='haRecentServiceDeniedTime'
_Ba='haRecentServiceAcceptedTime'
_BZ='haOverallServiceTime'
_BY='haServiceRequestsDenied'
_BX='haServiceRequestsAccepted'
_BW='haDeRegRepliesSent'
_BV='haRegRepliesSent'
_BU='haDeRegRequestsReceived'
_BT='haRegRequestsReceived'
_BS='haProxyARPsSent'
_BR='haGratuitiousARPsSent'
_BQ='haUnknownHA'
_BP='haTooManyBindings'
_BO='haPoorlyFormedRequest'
_BN='haIDMismatch'
_BM='haFAAuthenticationFailure'
_BL='haMNAuthenticationFailure'
_BK='haInsufficientResource'
_BJ='haAdmProhibited'
_BI='haReasonUnspecified'
_BH='haMultiBindingUnsupported'
_BG='haRegistrationAccepted'
_BF='haMobilityBindingTimeRemaining'
_BE='haMobilityBindingTimeGranted'
_BD='haMobilityBindingRegIDHigh'
_BC='haMobilityBindingRegIDLow'
_BB='haMobilityBindingRegFlags'
_BA='haMobilityBindingSourceAddress'
_B9='faPoorlyFormedReplies'
_B8='faHAAuthenticationFailure'
_B7='faRegRepliesRelayed'
_B6='faRegRepliesRecieved'
_B5='faHAUnreachable'
_B4='faVJCompressionUnavailable'
_B3='faEncapsulationUnavailable'
_B2='faPoorlyFormedRequests'
_B1='faRegLifetimeTooLong'
_B0='faMNAuthenticationFailure'
_A_='faInsufficientResource'
_Az='faAdmProhibited'
_Ay='faReasonUnspecified'
_Ax='faRegRequestsRelayed'
_Aw='faRegRequestsReceived'
_Av='faVisitorRegIsAccepted'
_Au='faVisitorRegIDHigh'
_At='faVisitorRegIDLow'
_As='faVisitorRegFlags'
_Ar='faVisitorTimeRemaining'
_Aq='faVisitorTimeGranted'
_Ap='faVisitorHomeAgentAddress'
_Ao='faVisitorHomeAddress'
_An='faRegistrationRequired'
_Am='faCOAStatus'
_Al='maSolicitationsReceived'
_Ak='maAdvsSentForSolicitation'
_Aj='maAdvertisementsSent'
_Ai='maAdvStatus'
_Ah='maAdvResponseSolicitationOnly'
_Ag='maAdvMaxAdvLifetime'
_Af='maAdvMinInterval'
_Ae='maAdvMaxInterval'
_Ad='maAdvAddress'
_Ac='maAdvPrefixLengthInclusion'
_Ab='maAdvMaxRegLifetime'
_Aa='mnRegRequestsWithDirectedBroadcast'
_AZ='mnRegRequestsDeniedByHADueToID'
_AY='mnRegRequestsDeniedByFA'
_AX='mnRegRequestsDeniedByHA'
_AW='mnRegRequestsAccepted'
_AV='mnRepliesFAAuthenticationFailure'
_AU='mnRepliesHAAuthenticationFailure'
_AT='mnRepliesIgnoredUnknownExtension'
_AS='mnRepliesDroppedInvalidExtension'
_AR='mnRepliesInvalidID'
_AQ='mnRepliesUnknownFA'
_AP='mnRepliesUnknownHA'
_AO='mnRepliesInvalidHomeAddress'
_AN='mnDeRegRepliesRecieved'
_AM='mnDeRegRequestsSent'
_AL='mnRegRepliesRecieved'
_AK='mnRegRequestsSent'
_AJ='mnCOAIsLocal'
_AI='mnRegIsAccepted'
_AH='mnRegTimeSent'
_AG='mnRegTimeRemaining'
_AF='mnRegTimeRequested'
_AE='mnRegIDHigh'
_AD='mnRegIDLow'
_AC='mnRegFlags'
_AB='mnAgentRebootsDectected'
_AA='mnGratuitousARPsSend'
_A9='mnMoveFromFAToHA'
_A8='mnMoveFromFAToFA'
_A7='mnMoveFromHAToFA'
_A6='mnAdvsIgnoredUnknownExtension'
_A5='mnAdvsDroppedInvalidExtension'
_A4='mnAdvertisementsReceived'
_A3='mnSolicitationsSent'
_A2='mnAdvTimeReceived'
_A1='mnAdvMaxAdvLifetime'
_A0='mnAdvMaxRegLifetime'
_z='mnAdvFlags'
_y='mnAdvSequence'
_x='mnAdvSourceAddress'
_w='mnHAStatus'
_v='mnHomeAddress'
_u='mnCurrentHA'
_t='mnState'
_s='mipSecRecentViolationTime'
_r='mipSecViolationCounter'
_q='mipSecTotalViolations'
_p='mipSecReplayMethod'
_o='mipSecKey'
_n='mipSecAlgorithmMode'
_m='mipSecAlgorithmType'
_l='mipEncapsulationSupported'
_k='mipEnable'
_j='mipEntities'
_i='faSupportedCOA'
_h='maInterfaceAddress'
_g='mnHAAddress'
_f='mipSecSPI'
_e='mipSecPeerAddress'
_d='read-write'
_c='homeAgent'
_b='foreignAgent'
_a='vjCompression'
_Z='TruthValue'
_Y='Unsigned32'
_X='OctetString'
_W='mipSecRecentViolationReason'
_V='mipSecRecentViolationIDHigh'
_U='mipSecRecentViolationIDLow'
_T='mipSecRecentViolationSPI'
_S='haMobilityBindingCOA'
_R='faVisitorIPAddress'
_Q='mnRegCOA'
_P='mnRegAgentAddress'
_O='mnCOA'
_N='mnFAAddress'
_M='mipSecViolatorAddress'
_L='minEnc'
_K='gre'
_J='haMobilityBindingMN'
_I='Bits'
_H='not-accessible'
_G='other'
_F='seconds'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='MIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_X,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Y,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_Z)
mipMIB=ModuleIdentity((1,3,6,1,2,1,44))
class RegistrationFlags(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_a,0),(_K,1),(_L,2),('decapsulationbyMN',3),('broadcastDatagram',4),('simultaneousBindings',5)))
_MipMIBObjects_ObjectIdentity=ObjectIdentity
mipMIBObjects=_MipMIBObjects_ObjectIdentity((1,3,6,1,2,1,44,1))
_MipSystem_ObjectIdentity=ObjectIdentity
mipSystem=_MipSystem_ObjectIdentity((1,3,6,1,2,1,44,1,1))
class _MipEntities_Type(Bits):namedValues=NamedValues(*(('mobileNode',0),(_b,1),(_c,2)))
_MipEntities_Type.__name__=_I
_MipEntities_Object=MibScalar
mipEntities=_MipEntities_Object((1,3,6,1,2,1,44,1,1,1),_MipEntities_Type())
mipEntities.setMaxAccess(_C)
if mibBuilder.loadTexts:mipEntities.setStatus(_A)
class _MipEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MipEnable_Type.__name__=_D
_MipEnable_Object=MibScalar
mipEnable=_MipEnable_Object((1,3,6,1,2,1,44,1,1,2),_MipEnable_Type())
mipEnable.setMaxAccess(_d)
if mibBuilder.loadTexts:mipEnable.setStatus(_A)
class _MipEncapsulationSupported_Type(Bits):namedValues=NamedValues(*(('ipInIp',0),(_K,1),(_L,2),(_G,3)))
_MipEncapsulationSupported_Type.__name__=_I
_MipEncapsulationSupported_Object=MibScalar
mipEncapsulationSupported=_MipEncapsulationSupported_Object((1,3,6,1,2,1,44,1,1,3),_MipEncapsulationSupported_Type())
mipEncapsulationSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:mipEncapsulationSupported.setStatus(_A)
_MipSecurity_ObjectIdentity=ObjectIdentity
mipSecurity=_MipSecurity_ObjectIdentity((1,3,6,1,2,1,44,1,2))
_MipSecAssocTable_Object=MibTable
mipSecAssocTable=_MipSecAssocTable_Object((1,3,6,1,2,1,44,1,2,1))
if mibBuilder.loadTexts:mipSecAssocTable.setStatus(_A)
_MipSecAssocEntry_Object=MibTableRow
mipSecAssocEntry=_MipSecAssocEntry_Object((1,3,6,1,2,1,44,1,2,1,1))
mipSecAssocEntry.setIndexNames((0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:mipSecAssocEntry.setStatus(_A)
_MipSecPeerAddress_Type=IpAddress
_MipSecPeerAddress_Object=MibTableColumn
mipSecPeerAddress=_MipSecPeerAddress_Object((1,3,6,1,2,1,44,1,2,1,1,1),_MipSecPeerAddress_Type())
mipSecPeerAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:mipSecPeerAddress.setStatus(_A)
class _MipSecSPI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MipSecSPI_Type.__name__=_Y
_MipSecSPI_Object=MibTableColumn
mipSecSPI=_MipSecSPI_Object((1,3,6,1,2,1,44,1,2,1,1,2),_MipSecSPI_Type())
mipSecSPI.setMaxAccess(_H)
if mibBuilder.loadTexts:mipSecSPI.setStatus(_A)
class _MipSecAlgorithmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('md5',2)))
_MipSecAlgorithmType_Type.__name__=_D
_MipSecAlgorithmType_Object=MibTableColumn
mipSecAlgorithmType=_MipSecAlgorithmType_Object((1,3,6,1,2,1,44,1,2,1,1,3),_MipSecAlgorithmType_Type())
mipSecAlgorithmType.setMaxAccess(_E)
if mibBuilder.loadTexts:mipSecAlgorithmType.setStatus(_A)
class _MipSecAlgorithmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('prefixSuffix',2)))
_MipSecAlgorithmMode_Type.__name__=_D
_MipSecAlgorithmMode_Object=MibTableColumn
mipSecAlgorithmMode=_MipSecAlgorithmMode_Object((1,3,6,1,2,1,44,1,2,1,1,4),_MipSecAlgorithmMode_Type())
mipSecAlgorithmMode.setMaxAccess(_E)
if mibBuilder.loadTexts:mipSecAlgorithmMode.setStatus(_A)
class _MipSecKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_MipSecKey_Type.__name__=_X
_MipSecKey_Object=MibTableColumn
mipSecKey=_MipSecKey_Object((1,3,6,1,2,1,44,1,2,1,1,5),_MipSecKey_Type())
mipSecKey.setMaxAccess(_E)
if mibBuilder.loadTexts:mipSecKey.setStatus(_A)
class _MipSecReplayMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('timestamps',2),('nonces',3)))
_MipSecReplayMethod_Type.__name__=_D
_MipSecReplayMethod_Object=MibTableColumn
mipSecReplayMethod=_MipSecReplayMethod_Object((1,3,6,1,2,1,44,1,2,1,1,6),_MipSecReplayMethod_Type())
mipSecReplayMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:mipSecReplayMethod.setStatus(_A)
_MipSecTotalViolations_Type=Counter32
_MipSecTotalViolations_Object=MibScalar
mipSecTotalViolations=_MipSecTotalViolations_Object((1,3,6,1,2,1,44,1,2,2),_MipSecTotalViolations_Type())
mipSecTotalViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:mipSecTotalViolations.setStatus(_A)
_MipSecViolationTable_Object=MibTable
mipSecViolationTable=_MipSecViolationTable_Object((1,3,6,1,2,1,44,1,2,3))
if mibBuilder.loadTexts:mipSecViolationTable.setStatus(_A)
_MipSecViolationEntry_Object=MibTableRow
mipSecViolationEntry=_MipSecViolationEntry_Object((1,3,6,1,2,1,44,1,2,3,1))
mipSecViolationEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:mipSecViolationEntry.setStatus(_A)
_MipSecViolatorAddress_Type=IpAddress
_MipSecViolatorAddress_Object=MibTableColumn
mipSecViolatorAddress=_MipSecViolatorAddress_Object((1,3,6,1,2,1,44,1,2,3,1,1),_MipSecViolatorAddress_Type())
mipSecViolatorAddress.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:mipSecViolatorAddress.setStatus(_A)
_MipSecViolationCounter_Type=Counter32
_MipSecViolationCounter_Object=MibTableColumn
mipSecViolationCounter=_MipSecViolationCounter_Object((1,3,6,1,2,1,44,1,2,3,1,2),_MipSecViolationCounter_Type())
mipSecViolationCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:mipSecViolationCounter.setStatus(_A)
_MipSecRecentViolationSPI_Type=Integer32
_MipSecRecentViolationSPI_Object=MibTableColumn
mipSecRecentViolationSPI=_MipSecRecentViolationSPI_Object((1,3,6,1,2,1,44,1,2,3,1,3),_MipSecRecentViolationSPI_Type())
mipSecRecentViolationSPI.setMaxAccess(_C)
if mibBuilder.loadTexts:mipSecRecentViolationSPI.setStatus(_A)
_MipSecRecentViolationTime_Type=TimeStamp
_MipSecRecentViolationTime_Object=MibTableColumn
mipSecRecentViolationTime=_MipSecRecentViolationTime_Object((1,3,6,1,2,1,44,1,2,3,1,4),_MipSecRecentViolationTime_Type())
mipSecRecentViolationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mipSecRecentViolationTime.setStatus(_A)
_MipSecRecentViolationIDLow_Type=Integer32
_MipSecRecentViolationIDLow_Object=MibTableColumn
mipSecRecentViolationIDLow=_MipSecRecentViolationIDLow_Object((1,3,6,1,2,1,44,1,2,3,1,5),_MipSecRecentViolationIDLow_Type())
mipSecRecentViolationIDLow.setMaxAccess(_C)
if mibBuilder.loadTexts:mipSecRecentViolationIDLow.setStatus(_A)
_MipSecRecentViolationIDHigh_Type=Integer32
_MipSecRecentViolationIDHigh_Object=MibTableColumn
mipSecRecentViolationIDHigh=_MipSecRecentViolationIDHigh_Object((1,3,6,1,2,1,44,1,2,3,1,6),_MipSecRecentViolationIDHigh_Type())
mipSecRecentViolationIDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:mipSecRecentViolationIDHigh.setStatus(_A)
class _MipSecRecentViolationReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noMobilitySecurityAssociation',1),('badAuthenticator',2),('badIdentifier',3),('badSPI',4),('missingSecurityExtension',5),(_G,6)))
_MipSecRecentViolationReason_Type.__name__=_D
_MipSecRecentViolationReason_Object=MibTableColumn
mipSecRecentViolationReason=_MipSecRecentViolationReason_Object((1,3,6,1,2,1,44,1,2,3,1,7),_MipSecRecentViolationReason_Type())
mipSecRecentViolationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:mipSecRecentViolationReason.setStatus(_A)
_MipMN_ObjectIdentity=ObjectIdentity
mipMN=_MipMN_ObjectIdentity((1,3,6,1,2,1,44,1,3))
_MnSystem_ObjectIdentity=ObjectIdentity
mnSystem=_MnSystem_ObjectIdentity((1,3,6,1,2,1,44,1,3,1))
class _MnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('home',1),('registered',2),('pending',3),('isolated',4),('unknown',5)))
_MnState_Type.__name__=_D
_MnState_Object=MibScalar
mnState=_MnState_Object((1,3,6,1,2,1,44,1,3,1,1),_MnState_Type())
mnState.setMaxAccess(_C)
if mibBuilder.loadTexts:mnState.setStatus(_A)
_MnHomeAddress_Type=IpAddress
_MnHomeAddress_Object=MibScalar
mnHomeAddress=_MnHomeAddress_Object((1,3,6,1,2,1,44,1,3,1,2),_MnHomeAddress_Type())
mnHomeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mnHomeAddress.setStatus(_A)
_MnHATable_Object=MibTable
mnHATable=_MnHATable_Object((1,3,6,1,2,1,44,1,3,1,3))
if mibBuilder.loadTexts:mnHATable.setStatus(_A)
_MnHAEntry_Object=MibTableRow
mnHAEntry=_MnHAEntry_Object((1,3,6,1,2,1,44,1,3,1,3,1))
mnHAEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:mnHAEntry.setStatus(_A)
_MnHAAddress_Type=IpAddress
_MnHAAddress_Object=MibTableColumn
mnHAAddress=_MnHAAddress_Object((1,3,6,1,2,1,44,1,3,1,3,1,1),_MnHAAddress_Type())
mnHAAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:mnHAAddress.setStatus(_A)
_MnCurrentHA_Type=TruthValue
_MnCurrentHA_Object=MibTableColumn
mnCurrentHA=_MnCurrentHA_Object((1,3,6,1,2,1,44,1,3,1,3,1,2),_MnCurrentHA_Type())
mnCurrentHA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnCurrentHA.setStatus(_A)
_MnHAStatus_Type=RowStatus
_MnHAStatus_Object=MibTableColumn
mnHAStatus=_MnHAStatus_Object((1,3,6,1,2,1,44,1,3,1,3,1,3),_MnHAStatus_Type())
mnHAStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mnHAStatus.setStatus(_A)
_MnDiscovery_ObjectIdentity=ObjectIdentity
mnDiscovery=_MnDiscovery_ObjectIdentity((1,3,6,1,2,1,44,1,3,2))
_MnFATable_Object=MibTable
mnFATable=_MnFATable_Object((1,3,6,1,2,1,44,1,3,2,1))
if mibBuilder.loadTexts:mnFATable.setStatus(_A)
_MnFAEntry_Object=MibTableRow
mnFAEntry=_MnFAEntry_Object((1,3,6,1,2,1,44,1,3,2,1,1))
mnFAEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:mnFAEntry.setStatus(_A)
_MnFAAddress_Type=IpAddress
_MnFAAddress_Object=MibTableColumn
mnFAAddress=_MnFAAddress_Object((1,3,6,1,2,1,44,1,3,2,1,1,1),_MnFAAddress_Type())
mnFAAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mnFAAddress.setStatus(_A)
_MnCOA_Type=IpAddress
_MnCOA_Object=MibTableColumn
mnCOA=_MnCOA_Object((1,3,6,1,2,1,44,1,3,2,1,1,2),_MnCOA_Type())
mnCOA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnCOA.setStatus(_A)
_MnRecentAdvReceived_ObjectIdentity=ObjectIdentity
mnRecentAdvReceived=_MnRecentAdvReceived_ObjectIdentity((1,3,6,1,2,1,44,1,3,2,2))
_MnAdvSourceAddress_Type=IpAddress
_MnAdvSourceAddress_Object=MibScalar
mnAdvSourceAddress=_MnAdvSourceAddress_Object((1,3,6,1,2,1,44,1,3,2,2,1),_MnAdvSourceAddress_Type())
mnAdvSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvSourceAddress.setStatus(_A)
class _MnAdvSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MnAdvSequence_Type.__name__=_D
_MnAdvSequence_Object=MibScalar
mnAdvSequence=_MnAdvSequence_Object((1,3,6,1,2,1,44,1,3,2,2,2),_MnAdvSequence_Type())
mnAdvSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvSequence.setStatus(_A)
class _MnAdvFlags_Type(Bits):namedValues=NamedValues(*((_a,0),(_K,1),(_L,2),(_b,3),(_c,4),('busy',5),('regRequired',6)))
_MnAdvFlags_Type.__name__=_I
_MnAdvFlags_Object=MibScalar
mnAdvFlags=_MnAdvFlags_Object((1,3,6,1,2,1,44,1,3,2,2,3),_MnAdvFlags_Type())
mnAdvFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvFlags.setStatus(_A)
class _MnAdvMaxRegLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MnAdvMaxRegLifetime_Type.__name__=_D
_MnAdvMaxRegLifetime_Object=MibScalar
mnAdvMaxRegLifetime=_MnAdvMaxRegLifetime_Object((1,3,6,1,2,1,44,1,3,2,2,4),_MnAdvMaxRegLifetime_Type())
mnAdvMaxRegLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvMaxRegLifetime.setStatus(_A)
if mibBuilder.loadTexts:mnAdvMaxRegLifetime.setUnits(_F)
class _MnAdvMaxAdvLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MnAdvMaxAdvLifetime_Type.__name__=_D
_MnAdvMaxAdvLifetime_Object=MibScalar
mnAdvMaxAdvLifetime=_MnAdvMaxAdvLifetime_Object((1,3,6,1,2,1,44,1,3,2,2,5),_MnAdvMaxAdvLifetime_Type())
mnAdvMaxAdvLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvMaxAdvLifetime.setStatus(_A)
if mibBuilder.loadTexts:mnAdvMaxAdvLifetime.setUnits(_F)
_MnAdvTimeReceived_Type=TimeStamp
_MnAdvTimeReceived_Object=MibScalar
mnAdvTimeReceived=_MnAdvTimeReceived_Object((1,3,6,1,2,1,44,1,3,2,2,6),_MnAdvTimeReceived_Type())
mnAdvTimeReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvTimeReceived.setStatus(_A)
_MnSolicitationsSent_Type=Counter32
_MnSolicitationsSent_Object=MibScalar
mnSolicitationsSent=_MnSolicitationsSent_Object((1,3,6,1,2,1,44,1,3,2,3),_MnSolicitationsSent_Type())
mnSolicitationsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mnSolicitationsSent.setStatus(_A)
_MnAdvertisementsReceived_Type=Counter32
_MnAdvertisementsReceived_Object=MibScalar
mnAdvertisementsReceived=_MnAdvertisementsReceived_Object((1,3,6,1,2,1,44,1,3,2,4),_MnAdvertisementsReceived_Type())
mnAdvertisementsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvertisementsReceived.setStatus(_A)
_MnAdvsDroppedInvalidExtension_Type=Counter32
_MnAdvsDroppedInvalidExtension_Object=MibScalar
mnAdvsDroppedInvalidExtension=_MnAdvsDroppedInvalidExtension_Object((1,3,6,1,2,1,44,1,3,2,5),_MnAdvsDroppedInvalidExtension_Type())
mnAdvsDroppedInvalidExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvsDroppedInvalidExtension.setStatus(_A)
_MnAdvsIgnoredUnknownExtension_Type=Counter32
_MnAdvsIgnoredUnknownExtension_Object=MibScalar
mnAdvsIgnoredUnknownExtension=_MnAdvsIgnoredUnknownExtension_Object((1,3,6,1,2,1,44,1,3,2,6),_MnAdvsIgnoredUnknownExtension_Type())
mnAdvsIgnoredUnknownExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAdvsIgnoredUnknownExtension.setStatus(_A)
_MnMoveFromHAToFA_Type=Counter32
_MnMoveFromHAToFA_Object=MibScalar
mnMoveFromHAToFA=_MnMoveFromHAToFA_Object((1,3,6,1,2,1,44,1,3,2,7),_MnMoveFromHAToFA_Type())
mnMoveFromHAToFA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnMoveFromHAToFA.setStatus(_A)
_MnMoveFromFAToFA_Type=Counter32
_MnMoveFromFAToFA_Object=MibScalar
mnMoveFromFAToFA=_MnMoveFromFAToFA_Object((1,3,6,1,2,1,44,1,3,2,8),_MnMoveFromFAToFA_Type())
mnMoveFromFAToFA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnMoveFromFAToFA.setStatus(_A)
_MnMoveFromFAToHA_Type=Counter32
_MnMoveFromFAToHA_Object=MibScalar
mnMoveFromFAToHA=_MnMoveFromFAToHA_Object((1,3,6,1,2,1,44,1,3,2,9),_MnMoveFromFAToHA_Type())
mnMoveFromFAToHA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnMoveFromFAToHA.setStatus(_A)
_MnGratuitousARPsSend_Type=Counter32
_MnGratuitousARPsSend_Object=MibScalar
mnGratuitousARPsSend=_MnGratuitousARPsSend_Object((1,3,6,1,2,1,44,1,3,2,10),_MnGratuitousARPsSend_Type())
mnGratuitousARPsSend.setMaxAccess(_C)
if mibBuilder.loadTexts:mnGratuitousARPsSend.setStatus(_A)
_MnAgentRebootsDectected_Type=Counter32
_MnAgentRebootsDectected_Object=MibScalar
mnAgentRebootsDectected=_MnAgentRebootsDectected_Object((1,3,6,1,2,1,44,1,3,2,11),_MnAgentRebootsDectected_Type())
mnAgentRebootsDectected.setMaxAccess(_C)
if mibBuilder.loadTexts:mnAgentRebootsDectected.setStatus(_A)
_MnRegistration_ObjectIdentity=ObjectIdentity
mnRegistration=_MnRegistration_ObjectIdentity((1,3,6,1,2,1,44,1,3,3))
_MnRegistrationTable_Object=MibTable
mnRegistrationTable=_MnRegistrationTable_Object((1,3,6,1,2,1,44,1,3,3,1))
if mibBuilder.loadTexts:mnRegistrationTable.setStatus(_A)
_MnRegistrationEntry_Object=MibTableRow
mnRegistrationEntry=_MnRegistrationEntry_Object((1,3,6,1,2,1,44,1,3,3,1,1))
mnRegistrationEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:mnRegistrationEntry.setStatus(_A)
_MnRegAgentAddress_Type=IpAddress
_MnRegAgentAddress_Object=MibTableColumn
mnRegAgentAddress=_MnRegAgentAddress_Object((1,3,6,1,2,1,44,1,3,3,1,1,1),_MnRegAgentAddress_Type())
mnRegAgentAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegAgentAddress.setStatus(_A)
_MnRegCOA_Type=IpAddress
_MnRegCOA_Object=MibTableColumn
mnRegCOA=_MnRegCOA_Object((1,3,6,1,2,1,44,1,3,3,1,1,2),_MnRegCOA_Type())
mnRegCOA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegCOA.setStatus(_A)
_MnRegFlags_Type=RegistrationFlags
_MnRegFlags_Object=MibTableColumn
mnRegFlags=_MnRegFlags_Object((1,3,6,1,2,1,44,1,3,3,1,1,3),_MnRegFlags_Type())
mnRegFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegFlags.setStatus(_A)
_MnRegIDLow_Type=Integer32
_MnRegIDLow_Object=MibTableColumn
mnRegIDLow=_MnRegIDLow_Object((1,3,6,1,2,1,44,1,3,3,1,1,4),_MnRegIDLow_Type())
mnRegIDLow.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegIDLow.setStatus(_A)
_MnRegIDHigh_Type=Integer32
_MnRegIDHigh_Object=MibTableColumn
mnRegIDHigh=_MnRegIDHigh_Object((1,3,6,1,2,1,44,1,3,3,1,1,5),_MnRegIDHigh_Type())
mnRegIDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegIDHigh.setStatus(_A)
_MnRegTimeRequested_Type=Integer32
_MnRegTimeRequested_Object=MibTableColumn
mnRegTimeRequested=_MnRegTimeRequested_Object((1,3,6,1,2,1,44,1,3,3,1,1,6),_MnRegTimeRequested_Type())
mnRegTimeRequested.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegTimeRequested.setStatus(_A)
if mibBuilder.loadTexts:mnRegTimeRequested.setUnits(_F)
_MnRegTimeRemaining_Type=Gauge32
_MnRegTimeRemaining_Object=MibTableColumn
mnRegTimeRemaining=_MnRegTimeRemaining_Object((1,3,6,1,2,1,44,1,3,3,1,1,7),_MnRegTimeRemaining_Type())
mnRegTimeRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegTimeRemaining.setStatus(_A)
if mibBuilder.loadTexts:mnRegTimeRemaining.setUnits(_F)
_MnRegTimeSent_Type=TimeStamp
_MnRegTimeSent_Object=MibTableColumn
mnRegTimeSent=_MnRegTimeSent_Object((1,3,6,1,2,1,44,1,3,3,1,1,8),_MnRegTimeSent_Type())
mnRegTimeSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegTimeSent.setStatus(_A)
_MnRegIsAccepted_Type=TruthValue
_MnRegIsAccepted_Object=MibTableColumn
mnRegIsAccepted=_MnRegIsAccepted_Object((1,3,6,1,2,1,44,1,3,3,1,1,9),_MnRegIsAccepted_Type())
mnRegIsAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegIsAccepted.setStatus(_A)
_MnCOAIsLocal_Type=TruthValue
_MnCOAIsLocal_Object=MibTableColumn
mnCOAIsLocal=_MnCOAIsLocal_Object((1,3,6,1,2,1,44,1,3,3,1,1,10),_MnCOAIsLocal_Type())
mnCOAIsLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:mnCOAIsLocal.setStatus(_A)
_MnRegRequestsSent_Type=Counter32
_MnRegRequestsSent_Object=MibScalar
mnRegRequestsSent=_MnRegRequestsSent_Object((1,3,6,1,2,1,44,1,3,3,2),_MnRegRequestsSent_Type())
mnRegRequestsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegRequestsSent.setStatus(_A)
_MnDeRegRequestsSent_Type=Counter32
_MnDeRegRequestsSent_Object=MibScalar
mnDeRegRequestsSent=_MnDeRegRequestsSent_Object((1,3,6,1,2,1,44,1,3,3,3),_MnDeRegRequestsSent_Type())
mnDeRegRequestsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mnDeRegRequestsSent.setStatus(_A)
_MnRegRepliesRecieved_Type=Counter32
_MnRegRepliesRecieved_Object=MibScalar
mnRegRepliesRecieved=_MnRegRepliesRecieved_Object((1,3,6,1,2,1,44,1,3,3,4),_MnRegRepliesRecieved_Type())
mnRegRepliesRecieved.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegRepliesRecieved.setStatus(_A)
_MnDeRegRepliesRecieved_Type=Counter32
_MnDeRegRepliesRecieved_Object=MibScalar
mnDeRegRepliesRecieved=_MnDeRegRepliesRecieved_Object((1,3,6,1,2,1,44,1,3,3,5),_MnDeRegRepliesRecieved_Type())
mnDeRegRepliesRecieved.setMaxAccess(_C)
if mibBuilder.loadTexts:mnDeRegRepliesRecieved.setStatus(_A)
_MnRepliesInvalidHomeAddress_Type=Counter32
_MnRepliesInvalidHomeAddress_Object=MibScalar
mnRepliesInvalidHomeAddress=_MnRepliesInvalidHomeAddress_Object((1,3,6,1,2,1,44,1,3,3,6),_MnRepliesInvalidHomeAddress_Type())
mnRepliesInvalidHomeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRepliesInvalidHomeAddress.setStatus(_A)
_MnRepliesUnknownHA_Type=Counter32
_MnRepliesUnknownHA_Object=MibScalar
mnRepliesUnknownHA=_MnRepliesUnknownHA_Object((1,3,6,1,2,1,44,1,3,3,7),_MnRepliesUnknownHA_Type())
mnRepliesUnknownHA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRepliesUnknownHA.setStatus(_A)
_MnRepliesUnknownFA_Type=Counter32
_MnRepliesUnknownFA_Object=MibScalar
mnRepliesUnknownFA=_MnRepliesUnknownFA_Object((1,3,6,1,2,1,44,1,3,3,8),_MnRepliesUnknownFA_Type())
mnRepliesUnknownFA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRepliesUnknownFA.setStatus(_A)
_MnRepliesInvalidID_Type=Counter32
_MnRepliesInvalidID_Object=MibScalar
mnRepliesInvalidID=_MnRepliesInvalidID_Object((1,3,6,1,2,1,44,1,3,3,9),_MnRepliesInvalidID_Type())
mnRepliesInvalidID.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRepliesInvalidID.setStatus(_A)
_MnRepliesDroppedInvalidExtension_Type=Counter32
_MnRepliesDroppedInvalidExtension_Object=MibScalar
mnRepliesDroppedInvalidExtension=_MnRepliesDroppedInvalidExtension_Object((1,3,6,1,2,1,44,1,3,3,10),_MnRepliesDroppedInvalidExtension_Type())
mnRepliesDroppedInvalidExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRepliesDroppedInvalidExtension.setStatus(_A)
_MnRepliesIgnoredUnknownExtension_Type=Counter32
_MnRepliesIgnoredUnknownExtension_Object=MibScalar
mnRepliesIgnoredUnknownExtension=_MnRepliesIgnoredUnknownExtension_Object((1,3,6,1,2,1,44,1,3,3,11),_MnRepliesIgnoredUnknownExtension_Type())
mnRepliesIgnoredUnknownExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRepliesIgnoredUnknownExtension.setStatus(_A)
_MnRepliesHAAuthenticationFailure_Type=Counter32
_MnRepliesHAAuthenticationFailure_Object=MibScalar
mnRepliesHAAuthenticationFailure=_MnRepliesHAAuthenticationFailure_Object((1,3,6,1,2,1,44,1,3,3,12),_MnRepliesHAAuthenticationFailure_Type())
mnRepliesHAAuthenticationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRepliesHAAuthenticationFailure.setStatus(_A)
_MnRepliesFAAuthenticationFailure_Type=Counter32
_MnRepliesFAAuthenticationFailure_Object=MibScalar
mnRepliesFAAuthenticationFailure=_MnRepliesFAAuthenticationFailure_Object((1,3,6,1,2,1,44,1,3,3,13),_MnRepliesFAAuthenticationFailure_Type())
mnRepliesFAAuthenticationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRepliesFAAuthenticationFailure.setStatus(_A)
_MnRegRequestsAccepted_Type=Counter32
_MnRegRequestsAccepted_Object=MibScalar
mnRegRequestsAccepted=_MnRegRequestsAccepted_Object((1,3,6,1,2,1,44,1,3,3,14),_MnRegRequestsAccepted_Type())
mnRegRequestsAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegRequestsAccepted.setStatus(_A)
_MnRegRequestsDeniedByHA_Type=Counter32
_MnRegRequestsDeniedByHA_Object=MibScalar
mnRegRequestsDeniedByHA=_MnRegRequestsDeniedByHA_Object((1,3,6,1,2,1,44,1,3,3,15),_MnRegRequestsDeniedByHA_Type())
mnRegRequestsDeniedByHA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegRequestsDeniedByHA.setStatus(_A)
_MnRegRequestsDeniedByFA_Type=Counter32
_MnRegRequestsDeniedByFA_Object=MibScalar
mnRegRequestsDeniedByFA=_MnRegRequestsDeniedByFA_Object((1,3,6,1,2,1,44,1,3,3,16),_MnRegRequestsDeniedByFA_Type())
mnRegRequestsDeniedByFA.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegRequestsDeniedByFA.setStatus(_A)
_MnRegRequestsDeniedByHADueToID_Type=Counter32
_MnRegRequestsDeniedByHADueToID_Object=MibScalar
mnRegRequestsDeniedByHADueToID=_MnRegRequestsDeniedByHADueToID_Object((1,3,6,1,2,1,44,1,3,3,17),_MnRegRequestsDeniedByHADueToID_Type())
mnRegRequestsDeniedByHADueToID.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegRequestsDeniedByHADueToID.setStatus(_A)
_MnRegRequestsWithDirectedBroadcast_Type=Counter32
_MnRegRequestsWithDirectedBroadcast_Object=MibScalar
mnRegRequestsWithDirectedBroadcast=_MnRegRequestsWithDirectedBroadcast_Object((1,3,6,1,2,1,44,1,3,3,18),_MnRegRequestsWithDirectedBroadcast_Type())
mnRegRequestsWithDirectedBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:mnRegRequestsWithDirectedBroadcast.setStatus(_A)
_MipMA_ObjectIdentity=ObjectIdentity
mipMA=_MipMA_ObjectIdentity((1,3,6,1,2,1,44,1,4))
_MaAdvertisement_ObjectIdentity=ObjectIdentity
maAdvertisement=_MaAdvertisement_ObjectIdentity((1,3,6,1,2,1,44,1,4,2))
_MaAdvConfigTable_Object=MibTable
maAdvConfigTable=_MaAdvConfigTable_Object((1,3,6,1,2,1,44,1,4,2,1))
if mibBuilder.loadTexts:maAdvConfigTable.setStatus(_A)
_MaAdvConfigEntry_Object=MibTableRow
maAdvConfigEntry=_MaAdvConfigEntry_Object((1,3,6,1,2,1,44,1,4,2,1,1))
maAdvConfigEntry.setIndexNames((0,_B,_h))
if mibBuilder.loadTexts:maAdvConfigEntry.setStatus(_A)
_MaInterfaceAddress_Type=IpAddress
_MaInterfaceAddress_Object=MibTableColumn
maInterfaceAddress=_MaInterfaceAddress_Object((1,3,6,1,2,1,44,1,4,2,1,1,1),_MaInterfaceAddress_Type())
maInterfaceAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:maInterfaceAddress.setStatus(_A)
class _MaAdvMaxRegLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MaAdvMaxRegLifetime_Type.__name__=_D
_MaAdvMaxRegLifetime_Object=MibTableColumn
maAdvMaxRegLifetime=_MaAdvMaxRegLifetime_Object((1,3,6,1,2,1,44,1,4,2,1,1,2),_MaAdvMaxRegLifetime_Type())
maAdvMaxRegLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:maAdvMaxRegLifetime.setStatus(_A)
if mibBuilder.loadTexts:maAdvMaxRegLifetime.setUnits(_F)
_MaAdvPrefixLengthInclusion_Type=TruthValue
_MaAdvPrefixLengthInclusion_Object=MibTableColumn
maAdvPrefixLengthInclusion=_MaAdvPrefixLengthInclusion_Object((1,3,6,1,2,1,44,1,4,2,1,1,3),_MaAdvPrefixLengthInclusion_Type())
maAdvPrefixLengthInclusion.setMaxAccess(_E)
if mibBuilder.loadTexts:maAdvPrefixLengthInclusion.setStatus(_A)
_MaAdvAddress_Type=IpAddress
_MaAdvAddress_Object=MibTableColumn
maAdvAddress=_MaAdvAddress_Object((1,3,6,1,2,1,44,1,4,2,1,1,4),_MaAdvAddress_Type())
maAdvAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:maAdvAddress.setStatus(_A)
class _MaAdvMaxInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_MaAdvMaxInterval_Type.__name__=_D
_MaAdvMaxInterval_Object=MibTableColumn
maAdvMaxInterval=_MaAdvMaxInterval_Object((1,3,6,1,2,1,44,1,4,2,1,1,5),_MaAdvMaxInterval_Type())
maAdvMaxInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:maAdvMaxInterval.setStatus(_A)
if mibBuilder.loadTexts:maAdvMaxInterval.setUnits(_F)
class _MaAdvMinInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_MaAdvMinInterval_Type.__name__=_D
_MaAdvMinInterval_Object=MibTableColumn
maAdvMinInterval=_MaAdvMinInterval_Object((1,3,6,1,2,1,44,1,4,2,1,1,6),_MaAdvMinInterval_Type())
maAdvMinInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:maAdvMinInterval.setStatus(_A)
if mibBuilder.loadTexts:maAdvMinInterval.setUnits(_F)
class _MaAdvMaxAdvLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,9000))
_MaAdvMaxAdvLifetime_Type.__name__=_D
_MaAdvMaxAdvLifetime_Object=MibTableColumn
maAdvMaxAdvLifetime=_MaAdvMaxAdvLifetime_Object((1,3,6,1,2,1,44,1,4,2,1,1,7),_MaAdvMaxAdvLifetime_Type())
maAdvMaxAdvLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:maAdvMaxAdvLifetime.setStatus(_A)
if mibBuilder.loadTexts:maAdvMaxAdvLifetime.setUnits(_F)
class _MaAdvResponseSolicitationOnly_Type(TruthValue):defaultValue=2
_MaAdvResponseSolicitationOnly_Type.__name__=_Z
_MaAdvResponseSolicitationOnly_Object=MibTableColumn
maAdvResponseSolicitationOnly=_MaAdvResponseSolicitationOnly_Object((1,3,6,1,2,1,44,1,4,2,1,1,8),_MaAdvResponseSolicitationOnly_Type())
maAdvResponseSolicitationOnly.setMaxAccess(_E)
if mibBuilder.loadTexts:maAdvResponseSolicitationOnly.setStatus(_A)
_MaAdvStatus_Type=RowStatus
_MaAdvStatus_Object=MibTableColumn
maAdvStatus=_MaAdvStatus_Object((1,3,6,1,2,1,44,1,4,2,1,1,9),_MaAdvStatus_Type())
maAdvStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:maAdvStatus.setStatus(_A)
_MaAdvertisementsSent_Type=Counter32
_MaAdvertisementsSent_Object=MibScalar
maAdvertisementsSent=_MaAdvertisementsSent_Object((1,3,6,1,2,1,44,1,4,2,2),_MaAdvertisementsSent_Type())
maAdvertisementsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:maAdvertisementsSent.setStatus(_A)
_MaAdvsSentForSolicitation_Type=Counter32
_MaAdvsSentForSolicitation_Object=MibScalar
maAdvsSentForSolicitation=_MaAdvsSentForSolicitation_Object((1,3,6,1,2,1,44,1,4,2,3),_MaAdvsSentForSolicitation_Type())
maAdvsSentForSolicitation.setMaxAccess(_C)
if mibBuilder.loadTexts:maAdvsSentForSolicitation.setStatus(_A)
_MaSolicitationsReceived_Type=Counter32
_MaSolicitationsReceived_Object=MibScalar
maSolicitationsReceived=_MaSolicitationsReceived_Object((1,3,6,1,2,1,44,1,4,2,4),_MaSolicitationsReceived_Type())
maSolicitationsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:maSolicitationsReceived.setStatus(_A)
_MipFA_ObjectIdentity=ObjectIdentity
mipFA=_MipFA_ObjectIdentity((1,3,6,1,2,1,44,1,5))
_FaSystem_ObjectIdentity=ObjectIdentity
faSystem=_FaSystem_ObjectIdentity((1,3,6,1,2,1,44,1,5,1))
_FaCOATable_Object=MibTable
faCOATable=_FaCOATable_Object((1,3,6,1,2,1,44,1,5,1,1))
if mibBuilder.loadTexts:faCOATable.setStatus(_A)
_FaCOAEntry_Object=MibTableRow
faCOAEntry=_FaCOAEntry_Object((1,3,6,1,2,1,44,1,5,1,1,1))
faCOAEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:faCOAEntry.setStatus(_A)
_FaSupportedCOA_Type=IpAddress
_FaSupportedCOA_Object=MibTableColumn
faSupportedCOA=_FaSupportedCOA_Object((1,3,6,1,2,1,44,1,5,1,1,1,1),_FaSupportedCOA_Type())
faSupportedCOA.setMaxAccess(_H)
if mibBuilder.loadTexts:faSupportedCOA.setStatus(_A)
_FaCOAStatus_Type=RowStatus
_FaCOAStatus_Object=MibTableColumn
faCOAStatus=_FaCOAStatus_Object((1,3,6,1,2,1,44,1,5,1,1,1,2),_FaCOAStatus_Type())
faCOAStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:faCOAStatus.setStatus(_A)
_FaAdvertisement_ObjectIdentity=ObjectIdentity
faAdvertisement=_FaAdvertisement_ObjectIdentity((1,3,6,1,2,1,44,1,5,2))
_FaIsBusy_Type=TruthValue
_FaIsBusy_Object=MibScalar
faIsBusy=_FaIsBusy_Object((1,3,6,1,2,1,44,1,5,2,1),_FaIsBusy_Type())
faIsBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:faIsBusy.setStatus(_A)
_FaRegistrationRequired_Type=TruthValue
_FaRegistrationRequired_Object=MibScalar
faRegistrationRequired=_FaRegistrationRequired_Object((1,3,6,1,2,1,44,1,5,2,2),_FaRegistrationRequired_Type())
faRegistrationRequired.setMaxAccess(_d)
if mibBuilder.loadTexts:faRegistrationRequired.setStatus(_A)
_FaRegistration_ObjectIdentity=ObjectIdentity
faRegistration=_FaRegistration_ObjectIdentity((1,3,6,1,2,1,44,1,5,3))
_FaVisitorTable_Object=MibTable
faVisitorTable=_FaVisitorTable_Object((1,3,6,1,2,1,44,1,5,3,1))
if mibBuilder.loadTexts:faVisitorTable.setStatus(_A)
_FaVisitorEntry_Object=MibTableRow
faVisitorEntry=_FaVisitorEntry_Object((1,3,6,1,2,1,44,1,5,3,1,1))
faVisitorEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:faVisitorEntry.setStatus(_A)
_FaVisitorIPAddress_Type=IpAddress
_FaVisitorIPAddress_Object=MibTableColumn
faVisitorIPAddress=_FaVisitorIPAddress_Object((1,3,6,1,2,1,44,1,5,3,1,1,1),_FaVisitorIPAddress_Type())
faVisitorIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorIPAddress.setStatus(_A)
_FaVisitorHomeAddress_Type=IpAddress
_FaVisitorHomeAddress_Object=MibTableColumn
faVisitorHomeAddress=_FaVisitorHomeAddress_Object((1,3,6,1,2,1,44,1,5,3,1,1,2),_FaVisitorHomeAddress_Type())
faVisitorHomeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorHomeAddress.setStatus(_A)
_FaVisitorHomeAgentAddress_Type=IpAddress
_FaVisitorHomeAgentAddress_Object=MibTableColumn
faVisitorHomeAgentAddress=_FaVisitorHomeAgentAddress_Object((1,3,6,1,2,1,44,1,5,3,1,1,3),_FaVisitorHomeAgentAddress_Type())
faVisitorHomeAgentAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorHomeAgentAddress.setStatus(_A)
_FaVisitorTimeGranted_Type=Integer32
_FaVisitorTimeGranted_Object=MibTableColumn
faVisitorTimeGranted=_FaVisitorTimeGranted_Object((1,3,6,1,2,1,44,1,5,3,1,1,4),_FaVisitorTimeGranted_Type())
faVisitorTimeGranted.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorTimeGranted.setStatus(_A)
if mibBuilder.loadTexts:faVisitorTimeGranted.setUnits(_F)
_FaVisitorTimeRemaining_Type=Gauge32
_FaVisitorTimeRemaining_Object=MibTableColumn
faVisitorTimeRemaining=_FaVisitorTimeRemaining_Object((1,3,6,1,2,1,44,1,5,3,1,1,5),_FaVisitorTimeRemaining_Type())
faVisitorTimeRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorTimeRemaining.setStatus(_A)
if mibBuilder.loadTexts:faVisitorTimeRemaining.setUnits(_F)
_FaVisitorRegFlags_Type=RegistrationFlags
_FaVisitorRegFlags_Object=MibTableColumn
faVisitorRegFlags=_FaVisitorRegFlags_Object((1,3,6,1,2,1,44,1,5,3,1,1,6),_FaVisitorRegFlags_Type())
faVisitorRegFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorRegFlags.setStatus(_A)
_FaVisitorRegIDLow_Type=Integer32
_FaVisitorRegIDLow_Object=MibTableColumn
faVisitorRegIDLow=_FaVisitorRegIDLow_Object((1,3,6,1,2,1,44,1,5,3,1,1,7),_FaVisitorRegIDLow_Type())
faVisitorRegIDLow.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorRegIDLow.setStatus(_A)
_FaVisitorRegIDHigh_Type=Integer32
_FaVisitorRegIDHigh_Object=MibTableColumn
faVisitorRegIDHigh=_FaVisitorRegIDHigh_Object((1,3,6,1,2,1,44,1,5,3,1,1,8),_FaVisitorRegIDHigh_Type())
faVisitorRegIDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorRegIDHigh.setStatus(_A)
_FaVisitorRegIsAccepted_Type=TruthValue
_FaVisitorRegIsAccepted_Object=MibTableColumn
faVisitorRegIsAccepted=_FaVisitorRegIsAccepted_Object((1,3,6,1,2,1,44,1,5,3,1,1,9),_FaVisitorRegIsAccepted_Type())
faVisitorRegIsAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:faVisitorRegIsAccepted.setStatus(_A)
_FaRegRequestsReceived_Type=Counter32
_FaRegRequestsReceived_Object=MibScalar
faRegRequestsReceived=_FaRegRequestsReceived_Object((1,3,6,1,2,1,44,1,5,3,2),_FaRegRequestsReceived_Type())
faRegRequestsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:faRegRequestsReceived.setStatus(_A)
_FaRegRequestsRelayed_Type=Counter32
_FaRegRequestsRelayed_Object=MibScalar
faRegRequestsRelayed=_FaRegRequestsRelayed_Object((1,3,6,1,2,1,44,1,5,3,3),_FaRegRequestsRelayed_Type())
faRegRequestsRelayed.setMaxAccess(_C)
if mibBuilder.loadTexts:faRegRequestsRelayed.setStatus(_A)
_FaReasonUnspecified_Type=Counter32
_FaReasonUnspecified_Object=MibScalar
faReasonUnspecified=_FaReasonUnspecified_Object((1,3,6,1,2,1,44,1,5,3,4),_FaReasonUnspecified_Type())
faReasonUnspecified.setMaxAccess(_C)
if mibBuilder.loadTexts:faReasonUnspecified.setStatus(_A)
_FaAdmProhibited_Type=Counter32
_FaAdmProhibited_Object=MibScalar
faAdmProhibited=_FaAdmProhibited_Object((1,3,6,1,2,1,44,1,5,3,5),_FaAdmProhibited_Type())
faAdmProhibited.setMaxAccess(_C)
if mibBuilder.loadTexts:faAdmProhibited.setStatus(_A)
_FaInsufficientResource_Type=Counter32
_FaInsufficientResource_Object=MibScalar
faInsufficientResource=_FaInsufficientResource_Object((1,3,6,1,2,1,44,1,5,3,6),_FaInsufficientResource_Type())
faInsufficientResource.setMaxAccess(_C)
if mibBuilder.loadTexts:faInsufficientResource.setStatus(_A)
_FaMNAuthenticationFailure_Type=Counter32
_FaMNAuthenticationFailure_Object=MibScalar
faMNAuthenticationFailure=_FaMNAuthenticationFailure_Object((1,3,6,1,2,1,44,1,5,3,7),_FaMNAuthenticationFailure_Type())
faMNAuthenticationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:faMNAuthenticationFailure.setStatus(_A)
_FaRegLifetimeTooLong_Type=Counter32
_FaRegLifetimeTooLong_Object=MibScalar
faRegLifetimeTooLong=_FaRegLifetimeTooLong_Object((1,3,6,1,2,1,44,1,5,3,8),_FaRegLifetimeTooLong_Type())
faRegLifetimeTooLong.setMaxAccess(_C)
if mibBuilder.loadTexts:faRegLifetimeTooLong.setStatus(_A)
_FaPoorlyFormedRequests_Type=Counter32
_FaPoorlyFormedRequests_Object=MibScalar
faPoorlyFormedRequests=_FaPoorlyFormedRequests_Object((1,3,6,1,2,1,44,1,5,3,9),_FaPoorlyFormedRequests_Type())
faPoorlyFormedRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:faPoorlyFormedRequests.setStatus(_A)
_FaEncapsulationUnavailable_Type=Counter32
_FaEncapsulationUnavailable_Object=MibScalar
faEncapsulationUnavailable=_FaEncapsulationUnavailable_Object((1,3,6,1,2,1,44,1,5,3,10),_FaEncapsulationUnavailable_Type())
faEncapsulationUnavailable.setMaxAccess(_C)
if mibBuilder.loadTexts:faEncapsulationUnavailable.setStatus(_A)
_FaVJCompressionUnavailable_Type=Counter32
_FaVJCompressionUnavailable_Object=MibScalar
faVJCompressionUnavailable=_FaVJCompressionUnavailable_Object((1,3,6,1,2,1,44,1,5,3,11),_FaVJCompressionUnavailable_Type())
faVJCompressionUnavailable.setMaxAccess(_C)
if mibBuilder.loadTexts:faVJCompressionUnavailable.setStatus(_A)
_FaHAUnreachable_Type=Counter32
_FaHAUnreachable_Object=MibScalar
faHAUnreachable=_FaHAUnreachable_Object((1,3,6,1,2,1,44,1,5,3,12),_FaHAUnreachable_Type())
faHAUnreachable.setMaxAccess(_C)
if mibBuilder.loadTexts:faHAUnreachable.setStatus(_A)
_FaRegRepliesRecieved_Type=Counter32
_FaRegRepliesRecieved_Object=MibScalar
faRegRepliesRecieved=_FaRegRepliesRecieved_Object((1,3,6,1,2,1,44,1,5,3,13),_FaRegRepliesRecieved_Type())
faRegRepliesRecieved.setMaxAccess(_C)
if mibBuilder.loadTexts:faRegRepliesRecieved.setStatus(_A)
_FaRegRepliesRelayed_Type=Counter32
_FaRegRepliesRelayed_Object=MibScalar
faRegRepliesRelayed=_FaRegRepliesRelayed_Object((1,3,6,1,2,1,44,1,5,3,14),_FaRegRepliesRelayed_Type())
faRegRepliesRelayed.setMaxAccess(_C)
if mibBuilder.loadTexts:faRegRepliesRelayed.setStatus(_A)
_FaHAAuthenticationFailure_Type=Counter32
_FaHAAuthenticationFailure_Object=MibScalar
faHAAuthenticationFailure=_FaHAAuthenticationFailure_Object((1,3,6,1,2,1,44,1,5,3,15),_FaHAAuthenticationFailure_Type())
faHAAuthenticationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:faHAAuthenticationFailure.setStatus(_A)
_FaPoorlyFormedReplies_Type=Counter32
_FaPoorlyFormedReplies_Object=MibScalar
faPoorlyFormedReplies=_FaPoorlyFormedReplies_Object((1,3,6,1,2,1,44,1,5,3,16),_FaPoorlyFormedReplies_Type())
faPoorlyFormedReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:faPoorlyFormedReplies.setStatus(_A)
_MipHA_ObjectIdentity=ObjectIdentity
mipHA=_MipHA_ObjectIdentity((1,3,6,1,2,1,44,1,6))
_HaRegistration_ObjectIdentity=ObjectIdentity
haRegistration=_HaRegistration_ObjectIdentity((1,3,6,1,2,1,44,1,6,3))
_HaMobilityBindingTable_Object=MibTable
haMobilityBindingTable=_HaMobilityBindingTable_Object((1,3,6,1,2,1,44,1,6,3,1))
if mibBuilder.loadTexts:haMobilityBindingTable.setStatus(_A)
_HaMobilityBindingEntry_Object=MibTableRow
haMobilityBindingEntry=_HaMobilityBindingEntry_Object((1,3,6,1,2,1,44,1,6,3,1,1))
haMobilityBindingEntry.setIndexNames((0,_B,_J),(0,_B,_S))
if mibBuilder.loadTexts:haMobilityBindingEntry.setStatus(_A)
_HaMobilityBindingMN_Type=IpAddress
_HaMobilityBindingMN_Object=MibTableColumn
haMobilityBindingMN=_HaMobilityBindingMN_Object((1,3,6,1,2,1,44,1,6,3,1,1,1),_HaMobilityBindingMN_Type())
haMobilityBindingMN.setMaxAccess(_C)
if mibBuilder.loadTexts:haMobilityBindingMN.setStatus(_A)
_HaMobilityBindingCOA_Type=IpAddress
_HaMobilityBindingCOA_Object=MibTableColumn
haMobilityBindingCOA=_HaMobilityBindingCOA_Object((1,3,6,1,2,1,44,1,6,3,1,1,2),_HaMobilityBindingCOA_Type())
haMobilityBindingCOA.setMaxAccess(_C)
if mibBuilder.loadTexts:haMobilityBindingCOA.setStatus(_A)
_HaMobilityBindingSourceAddress_Type=IpAddress
_HaMobilityBindingSourceAddress_Object=MibTableColumn
haMobilityBindingSourceAddress=_HaMobilityBindingSourceAddress_Object((1,3,6,1,2,1,44,1,6,3,1,1,3),_HaMobilityBindingSourceAddress_Type())
haMobilityBindingSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:haMobilityBindingSourceAddress.setStatus(_A)
_HaMobilityBindingRegFlags_Type=RegistrationFlags
_HaMobilityBindingRegFlags_Object=MibTableColumn
haMobilityBindingRegFlags=_HaMobilityBindingRegFlags_Object((1,3,6,1,2,1,44,1,6,3,1,1,4),_HaMobilityBindingRegFlags_Type())
haMobilityBindingRegFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:haMobilityBindingRegFlags.setStatus(_A)
_HaMobilityBindingRegIDLow_Type=Integer32
_HaMobilityBindingRegIDLow_Object=MibTableColumn
haMobilityBindingRegIDLow=_HaMobilityBindingRegIDLow_Object((1,3,6,1,2,1,44,1,6,3,1,1,5),_HaMobilityBindingRegIDLow_Type())
haMobilityBindingRegIDLow.setMaxAccess(_C)
if mibBuilder.loadTexts:haMobilityBindingRegIDLow.setStatus(_A)
_HaMobilityBindingRegIDHigh_Type=Integer32
_HaMobilityBindingRegIDHigh_Object=MibTableColumn
haMobilityBindingRegIDHigh=_HaMobilityBindingRegIDHigh_Object((1,3,6,1,2,1,44,1,6,3,1,1,6),_HaMobilityBindingRegIDHigh_Type())
haMobilityBindingRegIDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:haMobilityBindingRegIDHigh.setStatus(_A)
_HaMobilityBindingTimeGranted_Type=Integer32
_HaMobilityBindingTimeGranted_Object=MibTableColumn
haMobilityBindingTimeGranted=_HaMobilityBindingTimeGranted_Object((1,3,6,1,2,1,44,1,6,3,1,1,7),_HaMobilityBindingTimeGranted_Type())
haMobilityBindingTimeGranted.setMaxAccess(_C)
if mibBuilder.loadTexts:haMobilityBindingTimeGranted.setStatus(_A)
if mibBuilder.loadTexts:haMobilityBindingTimeGranted.setUnits(_F)
_HaMobilityBindingTimeRemaining_Type=Gauge32
_HaMobilityBindingTimeRemaining_Object=MibTableColumn
haMobilityBindingTimeRemaining=_HaMobilityBindingTimeRemaining_Object((1,3,6,1,2,1,44,1,6,3,1,1,8),_HaMobilityBindingTimeRemaining_Type())
haMobilityBindingTimeRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:haMobilityBindingTimeRemaining.setStatus(_A)
if mibBuilder.loadTexts:haMobilityBindingTimeRemaining.setUnits(_F)
_HaCounterTable_Object=MibTable
haCounterTable=_HaCounterTable_Object((1,3,6,1,2,1,44,1,6,3,2))
if mibBuilder.loadTexts:haCounterTable.setStatus(_A)
_HaCounterEntry_Object=MibTableRow
haCounterEntry=_HaCounterEntry_Object((1,3,6,1,2,1,44,1,6,3,2,1))
haCounterEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:haCounterEntry.setStatus(_A)
_HaServiceRequestsAccepted_Type=Counter32
_HaServiceRequestsAccepted_Object=MibTableColumn
haServiceRequestsAccepted=_HaServiceRequestsAccepted_Object((1,3,6,1,2,1,44,1,6,3,2,1,2),_HaServiceRequestsAccepted_Type())
haServiceRequestsAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:haServiceRequestsAccepted.setStatus(_A)
_HaServiceRequestsDenied_Type=Counter32
_HaServiceRequestsDenied_Object=MibTableColumn
haServiceRequestsDenied=_HaServiceRequestsDenied_Object((1,3,6,1,2,1,44,1,6,3,2,1,3),_HaServiceRequestsDenied_Type())
haServiceRequestsDenied.setMaxAccess(_C)
if mibBuilder.loadTexts:haServiceRequestsDenied.setStatus(_A)
_HaOverallServiceTime_Type=Gauge32
_HaOverallServiceTime_Object=MibTableColumn
haOverallServiceTime=_HaOverallServiceTime_Object((1,3,6,1,2,1,44,1,6,3,2,1,4),_HaOverallServiceTime_Type())
haOverallServiceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:haOverallServiceTime.setStatus(_A)
if mibBuilder.loadTexts:haOverallServiceTime.setUnits(_F)
_HaRecentServiceAcceptedTime_Type=TimeStamp
_HaRecentServiceAcceptedTime_Object=MibTableColumn
haRecentServiceAcceptedTime=_HaRecentServiceAcceptedTime_Object((1,3,6,1,2,1,44,1,6,3,2,1,5),_HaRecentServiceAcceptedTime_Type())
haRecentServiceAcceptedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:haRecentServiceAcceptedTime.setStatus(_A)
_HaRecentServiceDeniedTime_Type=TimeStamp
_HaRecentServiceDeniedTime_Object=MibTableColumn
haRecentServiceDeniedTime=_HaRecentServiceDeniedTime_Object((1,3,6,1,2,1,44,1,6,3,2,1,6),_HaRecentServiceDeniedTime_Type())
haRecentServiceDeniedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:haRecentServiceDeniedTime.setStatus(_A)
class _HaRecentServiceDeniedCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(128,129,130,131,132,133,134,135,136)));namedValues=NamedValues(*(('reasonUnspecified',128),('admProhibited',129),('insufficientResource',130),('mnAuthenticationFailure',131),('faAuthenticationFailure',132),('idMismatch',133),('poorlyFormedRequest',134),('tooManyBindings',135),('unknownHA',136)))
_HaRecentServiceDeniedCode_Type.__name__=_D
_HaRecentServiceDeniedCode_Object=MibTableColumn
haRecentServiceDeniedCode=_HaRecentServiceDeniedCode_Object((1,3,6,1,2,1,44,1,6,3,2,1,7),_HaRecentServiceDeniedCode_Type())
haRecentServiceDeniedCode.setMaxAccess(_C)
if mibBuilder.loadTexts:haRecentServiceDeniedCode.setStatus(_A)
_HaRegistrationAccepted_Type=Counter32
_HaRegistrationAccepted_Object=MibScalar
haRegistrationAccepted=_HaRegistrationAccepted_Object((1,3,6,1,2,1,44,1,6,3,3),_HaRegistrationAccepted_Type())
haRegistrationAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:haRegistrationAccepted.setStatus(_A)
_HaMultiBindingUnsupported_Type=Counter32
_HaMultiBindingUnsupported_Object=MibScalar
haMultiBindingUnsupported=_HaMultiBindingUnsupported_Object((1,3,6,1,2,1,44,1,6,3,4),_HaMultiBindingUnsupported_Type())
haMultiBindingUnsupported.setMaxAccess(_C)
if mibBuilder.loadTexts:haMultiBindingUnsupported.setStatus(_A)
_HaReasonUnspecified_Type=Counter32
_HaReasonUnspecified_Object=MibScalar
haReasonUnspecified=_HaReasonUnspecified_Object((1,3,6,1,2,1,44,1,6,3,5),_HaReasonUnspecified_Type())
haReasonUnspecified.setMaxAccess(_C)
if mibBuilder.loadTexts:haReasonUnspecified.setStatus(_A)
_HaAdmProhibited_Type=Counter32
_HaAdmProhibited_Object=MibScalar
haAdmProhibited=_HaAdmProhibited_Object((1,3,6,1,2,1,44,1,6,3,6),_HaAdmProhibited_Type())
haAdmProhibited.setMaxAccess(_C)
if mibBuilder.loadTexts:haAdmProhibited.setStatus(_A)
_HaInsufficientResource_Type=Counter32
_HaInsufficientResource_Object=MibScalar
haInsufficientResource=_HaInsufficientResource_Object((1,3,6,1,2,1,44,1,6,3,7),_HaInsufficientResource_Type())
haInsufficientResource.setMaxAccess(_C)
if mibBuilder.loadTexts:haInsufficientResource.setStatus(_A)
_HaMNAuthenticationFailure_Type=Counter32
_HaMNAuthenticationFailure_Object=MibScalar
haMNAuthenticationFailure=_HaMNAuthenticationFailure_Object((1,3,6,1,2,1,44,1,6,3,8),_HaMNAuthenticationFailure_Type())
haMNAuthenticationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:haMNAuthenticationFailure.setStatus(_A)
_HaFAAuthenticationFailure_Type=Counter32
_HaFAAuthenticationFailure_Object=MibScalar
haFAAuthenticationFailure=_HaFAAuthenticationFailure_Object((1,3,6,1,2,1,44,1,6,3,9),_HaFAAuthenticationFailure_Type())
haFAAuthenticationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:haFAAuthenticationFailure.setStatus(_A)
_HaIDMismatch_Type=Counter32
_HaIDMismatch_Object=MibScalar
haIDMismatch=_HaIDMismatch_Object((1,3,6,1,2,1,44,1,6,3,10),_HaIDMismatch_Type())
haIDMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:haIDMismatch.setStatus(_A)
_HaPoorlyFormedRequest_Type=Counter32
_HaPoorlyFormedRequest_Object=MibScalar
haPoorlyFormedRequest=_HaPoorlyFormedRequest_Object((1,3,6,1,2,1,44,1,6,3,11),_HaPoorlyFormedRequest_Type())
haPoorlyFormedRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:haPoorlyFormedRequest.setStatus(_A)
_HaTooManyBindings_Type=Counter32
_HaTooManyBindings_Object=MibScalar
haTooManyBindings=_HaTooManyBindings_Object((1,3,6,1,2,1,44,1,6,3,12),_HaTooManyBindings_Type())
haTooManyBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:haTooManyBindings.setStatus(_A)
_HaUnknownHA_Type=Counter32
_HaUnknownHA_Object=MibScalar
haUnknownHA=_HaUnknownHA_Object((1,3,6,1,2,1,44,1,6,3,13),_HaUnknownHA_Type())
haUnknownHA.setMaxAccess(_C)
if mibBuilder.loadTexts:haUnknownHA.setStatus(_A)
_HaGratuitiousARPsSent_Type=Counter32
_HaGratuitiousARPsSent_Object=MibScalar
haGratuitiousARPsSent=_HaGratuitiousARPsSent_Object((1,3,6,1,2,1,44,1,6,3,14),_HaGratuitiousARPsSent_Type())
haGratuitiousARPsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:haGratuitiousARPsSent.setStatus(_A)
_HaProxyARPsSent_Type=Counter32
_HaProxyARPsSent_Object=MibScalar
haProxyARPsSent=_HaProxyARPsSent_Object((1,3,6,1,2,1,44,1,6,3,15),_HaProxyARPsSent_Type())
haProxyARPsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:haProxyARPsSent.setStatus(_A)
_HaRegRequestsReceived_Type=Counter32
_HaRegRequestsReceived_Object=MibScalar
haRegRequestsReceived=_HaRegRequestsReceived_Object((1,3,6,1,2,1,44,1,6,3,16),_HaRegRequestsReceived_Type())
haRegRequestsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:haRegRequestsReceived.setStatus(_A)
_HaDeRegRequestsReceived_Type=Counter32
_HaDeRegRequestsReceived_Object=MibScalar
haDeRegRequestsReceived=_HaDeRegRequestsReceived_Object((1,3,6,1,2,1,44,1,6,3,17),_HaDeRegRequestsReceived_Type())
haDeRegRequestsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:haDeRegRequestsReceived.setStatus(_A)
_HaRegRepliesSent_Type=Counter32
_HaRegRepliesSent_Object=MibScalar
haRegRepliesSent=_HaRegRepliesSent_Object((1,3,6,1,2,1,44,1,6,3,18),_HaRegRepliesSent_Type())
haRegRepliesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:haRegRepliesSent.setStatus(_A)
_HaDeRegRepliesSent_Type=Counter32
_HaDeRegRepliesSent_Object=MibScalar
haDeRegRepliesSent=_HaDeRegRepliesSent_Object((1,3,6,1,2,1,44,1,6,3,19),_HaDeRegRepliesSent_Type())
haDeRegRepliesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:haDeRegRepliesSent.setStatus(_A)
_MipMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
mipMIBNotificationPrefix=_MipMIBNotificationPrefix_ObjectIdentity((1,3,6,1,2,1,44,2))
_MipMIBNotifications_ObjectIdentity=ObjectIdentity
mipMIBNotifications=_MipMIBNotifications_ObjectIdentity((1,3,6,1,2,1,44,2,0))
_MipMIBConformance_ObjectIdentity=ObjectIdentity
mipMIBConformance=_MipMIBConformance_ObjectIdentity((1,3,6,1,2,1,44,3))
_MipGroups_ObjectIdentity=ObjectIdentity
mipGroups=_MipGroups_ObjectIdentity((1,3,6,1,2,1,44,3,1))
_MipCompliances_ObjectIdentity=ObjectIdentity
mipCompliances=_MipCompliances_ObjectIdentity((1,3,6,1,2,1,44,3,2))
mipSystemGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,1))
mipSystemGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:mipSystemGroup.setStatus(_A)
mipSecAssociationGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,2))
mipSecAssociationGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:mipSecAssociationGroup.setStatus(_A)
mipSecViolationGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,3))
mipSecViolationGroup.setObjects(*((_B,_q),(_B,_r),(_B,_T),(_B,_s),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:mipSecViolationGroup.setStatus(_A)
mnSystemGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,4))
mnSystemGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:mnSystemGroup.setStatus(_A)
mnDiscoveryGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,5))
mnDiscoveryGroup.setObjects(*((_B,_N),(_B,_O),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:mnDiscoveryGroup.setStatus(_A)
mnRegistrationGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,6))
mnRegistrationGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:mnRegistrationGroup.setStatus(_A)
maAdvertisementGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,7))
maAdvertisementGroup.setObjects(*((_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:maAdvertisementGroup.setStatus(_A)
faSystemGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,8))
faSystemGroup.setObjects((_B,_Am))
if mibBuilder.loadTexts:faSystemGroup.setStatus(_A)
faAdvertisementGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,9))
faAdvertisementGroup.setObjects(*((_B,'faIsBusy'),(_B,_An)))
if mibBuilder.loadTexts:faAdvertisementGroup.setStatus(_A)
faRegistrationGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,10))
faRegistrationGroup.setObjects(*((_B,_R),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9)))
if mibBuilder.loadTexts:faRegistrationGroup.setStatus(_A)
haRegistrationGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,11))
haRegistrationGroup.setObjects(*((_B,_J),(_B,_S),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR),(_B,_BS),(_B,_BT),(_B,_BU),(_B,_BV),(_B,_BW)))
if mibBuilder.loadTexts:haRegistrationGroup.setStatus(_A)
haRegNodeCountersGroup=ObjectGroup((1,3,6,1,2,1,44,3,1,12))
haRegNodeCountersGroup.setObjects(*((_B,_BX),(_B,_BY),(_B,_BZ),(_B,_Ba),(_B,_Bb),(_B,_Bc)))
if mibBuilder.loadTexts:haRegNodeCountersGroup.setStatus(_A)
mipAuthFailure=NotificationType((1,3,6,1,2,1,44,2,0,1))
mipAuthFailure.setObjects(*((_B,_M),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:mipAuthFailure.setStatus(_A)
mipSecNotificationsGroup=NotificationGroup((1,3,6,1,2,1,44,3,1,13))
mipSecNotificationsGroup.setObjects((_B,_Bd))
if mibBuilder.loadTexts:mipSecNotificationsGroup.setStatus(_A)
mipCompliance=ModuleCompliance((1,3,6,1,2,1,44,3,2,1))
mipCompliance.setObjects(*((_B,_Be),(_B,_Bf),(_B,_Bg),(_B,_Bh),(_B,_Bi),(_B,_Bj),(_B,_Bk),(_B,_Bl),(_B,_Bm),(_B,_Bn),(_B,_Bo),(_B,_Bp),(_B,_Bq)))
if mibBuilder.loadTexts:mipCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RegistrationFlags':RegistrationFlags,'mipMIB':mipMIB,'mipMIBObjects':mipMIBObjects,'mipSystem':mipSystem,_j:mipEntities,_k:mipEnable,_l:mipEncapsulationSupported,'mipSecurity':mipSecurity,'mipSecAssocTable':mipSecAssocTable,'mipSecAssocEntry':mipSecAssocEntry,_e:mipSecPeerAddress,_f:mipSecSPI,_m:mipSecAlgorithmType,_n:mipSecAlgorithmMode,_o:mipSecKey,_p:mipSecReplayMethod,_q:mipSecTotalViolations,'mipSecViolationTable':mipSecViolationTable,'mipSecViolationEntry':mipSecViolationEntry,_M:mipSecViolatorAddress,_r:mipSecViolationCounter,_T:mipSecRecentViolationSPI,_s:mipSecRecentViolationTime,_U:mipSecRecentViolationIDLow,_V:mipSecRecentViolationIDHigh,_W:mipSecRecentViolationReason,'mipMN':mipMN,'mnSystem':mnSystem,_t:mnState,_v:mnHomeAddress,'mnHATable':mnHATable,'mnHAEntry':mnHAEntry,_g:mnHAAddress,_u:mnCurrentHA,_w:mnHAStatus,'mnDiscovery':mnDiscovery,'mnFATable':mnFATable,'mnFAEntry':mnFAEntry,_N:mnFAAddress,_O:mnCOA,'mnRecentAdvReceived':mnRecentAdvReceived,_x:mnAdvSourceAddress,_y:mnAdvSequence,_z:mnAdvFlags,_A0:mnAdvMaxRegLifetime,_A1:mnAdvMaxAdvLifetime,_A2:mnAdvTimeReceived,_A3:mnSolicitationsSent,_A4:mnAdvertisementsReceived,_A5:mnAdvsDroppedInvalidExtension,_A6:mnAdvsIgnoredUnknownExtension,_A7:mnMoveFromHAToFA,_A8:mnMoveFromFAToFA,_A9:mnMoveFromFAToHA,_AA:mnGratuitousARPsSend,_AB:mnAgentRebootsDectected,'mnRegistration':mnRegistration,'mnRegistrationTable':mnRegistrationTable,'mnRegistrationEntry':mnRegistrationEntry,_P:mnRegAgentAddress,_Q:mnRegCOA,_AC:mnRegFlags,_AD:mnRegIDLow,_AE:mnRegIDHigh,_AF:mnRegTimeRequested,_AG:mnRegTimeRemaining,_AH:mnRegTimeSent,_AI:mnRegIsAccepted,_AJ:mnCOAIsLocal,_AK:mnRegRequestsSent,_AM:mnDeRegRequestsSent,_AL:mnRegRepliesRecieved,_AN:mnDeRegRepliesRecieved,_AO:mnRepliesInvalidHomeAddress,_AP:mnRepliesUnknownHA,_AQ:mnRepliesUnknownFA,_AR:mnRepliesInvalidID,_AS:mnRepliesDroppedInvalidExtension,_AT:mnRepliesIgnoredUnknownExtension,_AU:mnRepliesHAAuthenticationFailure,_AV:mnRepliesFAAuthenticationFailure,_AW:mnRegRequestsAccepted,_AX:mnRegRequestsDeniedByHA,_AY:mnRegRequestsDeniedByFA,_AZ:mnRegRequestsDeniedByHADueToID,_Aa:mnRegRequestsWithDirectedBroadcast,'mipMA':mipMA,'maAdvertisement':maAdvertisement,'maAdvConfigTable':maAdvConfigTable,'maAdvConfigEntry':maAdvConfigEntry,_h:maInterfaceAddress,_Ab:maAdvMaxRegLifetime,_Ac:maAdvPrefixLengthInclusion,_Ad:maAdvAddress,_Ae:maAdvMaxInterval,_Af:maAdvMinInterval,_Ag:maAdvMaxAdvLifetime,_Ah:maAdvResponseSolicitationOnly,_Ai:maAdvStatus,_Aj:maAdvertisementsSent,_Ak:maAdvsSentForSolicitation,_Al:maSolicitationsReceived,'mipFA':mipFA,'faSystem':faSystem,'faCOATable':faCOATable,'faCOAEntry':faCOAEntry,_i:faSupportedCOA,_Am:faCOAStatus,'faAdvertisement':faAdvertisement,'faIsBusy':faIsBusy,_An:faRegistrationRequired,'faRegistration':faRegistration,'faVisitorTable':faVisitorTable,'faVisitorEntry':faVisitorEntry,_R:faVisitorIPAddress,_Ao:faVisitorHomeAddress,_Ap:faVisitorHomeAgentAddress,_Aq:faVisitorTimeGranted,_Ar:faVisitorTimeRemaining,_As:faVisitorRegFlags,_At:faVisitorRegIDLow,_Au:faVisitorRegIDHigh,_Av:faVisitorRegIsAccepted,_Aw:faRegRequestsReceived,_Ax:faRegRequestsRelayed,_Ay:faReasonUnspecified,_Az:faAdmProhibited,_A_:faInsufficientResource,_B0:faMNAuthenticationFailure,_B1:faRegLifetimeTooLong,_B2:faPoorlyFormedRequests,_B3:faEncapsulationUnavailable,_B4:faVJCompressionUnavailable,_B5:faHAUnreachable,_B6:faRegRepliesRecieved,_B7:faRegRepliesRelayed,_B8:faHAAuthenticationFailure,_B9:faPoorlyFormedReplies,'mipHA':mipHA,'haRegistration':haRegistration,'haMobilityBindingTable':haMobilityBindingTable,'haMobilityBindingEntry':haMobilityBindingEntry,_J:haMobilityBindingMN,_S:haMobilityBindingCOA,_BA:haMobilityBindingSourceAddress,_BB:haMobilityBindingRegFlags,_BC:haMobilityBindingRegIDLow,_BD:haMobilityBindingRegIDHigh,_BE:haMobilityBindingTimeGranted,_BF:haMobilityBindingTimeRemaining,'haCounterTable':haCounterTable,'haCounterEntry':haCounterEntry,_BX:haServiceRequestsAccepted,_BY:haServiceRequestsDenied,_BZ:haOverallServiceTime,_Ba:haRecentServiceAcceptedTime,_Bb:haRecentServiceDeniedTime,_Bc:haRecentServiceDeniedCode,_BG:haRegistrationAccepted,_BH:haMultiBindingUnsupported,_BI:haReasonUnspecified,_BJ:haAdmProhibited,_BK:haInsufficientResource,_BL:haMNAuthenticationFailure,_BM:haFAAuthenticationFailure,_BN:haIDMismatch,_BO:haPoorlyFormedRequest,_BP:haTooManyBindings,_BQ:haUnknownHA,_BR:haGratuitiousARPsSent,_BS:haProxyARPsSent,_BT:haRegRequestsReceived,_BU:haDeRegRequestsReceived,_BV:haRegRepliesSent,_BW:haDeRegRepliesSent,'mipMIBNotificationPrefix':mipMIBNotificationPrefix,'mipMIBNotifications':mipMIBNotifications,_Bd:mipAuthFailure,'mipMIBConformance':mipMIBConformance,'mipGroups':mipGroups,_Be:mipSystemGroup,_Bf:mipSecAssociationGroup,_Bg:mipSecViolationGroup,_Bh:mnSystemGroup,_Bi:mnDiscoveryGroup,_Bj:mnRegistrationGroup,_Bk:maAdvertisementGroup,_Bl:faSystemGroup,_Bm:faAdvertisementGroup,_Bn:faRegistrationGroup,_Bo:haRegistrationGroup,_Bp:haRegNodeCountersGroup,_Bq:mipSecNotificationsGroup,'mipCompliances':mipCompliances,'mipCompliance':mipCompliance})