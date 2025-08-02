_AQ='nemoNotificationGroup'
_AP='nemoHaGlobalStatsGroup'
_AO='nemoHaStatsGroup'
_AN='nemoHomeTunnelReleased'
_AM='nemoHomeTunnelEstablished'
_AL='nemoHaBUAcksOtherError'
_AK='nemoHaBUAcksForwardingSetupFailed'
_AJ='nemoHaBUAcksNotAuthorizedForPrefix'
_AI='nemoHaBUAcksInvalidPrefix'
_AH='nemoHaBUAcksOperationNotPermitted'
_AG='nemoHaBUAcksRegTypeChangeDisallowed'
_AF='nemoHaBUAcksWONemoSupport'
_AE='nemoHaCtrDiscontinuityTime'
_AD='nemoHaRecentBURejectionCode'
_AC='nemoHaBURejectionTime'
_AB='nemoHaBUAcceptedTime'
_AA='nemoHaBCEntryCreationTime'
_A9='nemoHaBURequestsDenied'
_A8='nemoHaBURequestsAccepted'
_A7='nemoHaMobileNetworkPrefixSource'
_A6='nemoHaMobileNetworkPrefixLength'
_A5='nemoHaMobileNetworkPrefix'
_A4='nemoHaMobileNetworkPrefixType'
_A3='nemoMrBindingAcksOtherError'
_A2='nemoMrBindingAcksForwardingSetupFailed'
_A1='nemoMrBindingAcksNotAuthorizedForPrefix'
_A0='nemoMrBindingAcksInvalidPrefix'
_z='nemoMrBindingAcksOperationNotPermitted'
_y='nemoMrBindingAcksRegTypeChangeDisallowed'
_x='nemoMrBindingAcksWONemoSupport'
_w='nemoMrPrefixRegMode'
_v='nemoMrMobilityMessagesRecd'
_u='nemoMrMobilityMessagesSent'
_t='nemoMrBLMrFlag'
_s='nemoMrBLMode'
_r='nemoMrBetterIfDetected'
_q='nemoMrMovedFNtoFN'
_p='nemoMrMovedOutofHome'
_o='nemoMrMovedHome'
_n='nemoMrDiscoveryRepliesRouterFlagZero'
_m='nemoMrDiscoveryReplies'
_l='nemoMrDiscoveryRequests'
_k='nemoMrEgressIfRoamHoldDownTime'
_j='nemoMrEgressIfDescription'
_i='nemoMrEgressIfPriority'
_h='nemoCounterDiscontinuityTime'
_g='nemoBindingMrMode'
_f='nemoBindingMrFlag'
_e='nemoStatus'
_d='nemoCapabilities'
_c='nemoMrBLEntry'
_b='nemoBindingCacheEntry'
_a='nemoHaMobileNetworkPrefixSeqNo'
_Z='not-accessible'
_Y='nemoMrEgressIfIndex'
_X='read-write'
_W='nemoHaSystemGroup'
_V='nemoMrRegistrationGroup'
_U='nemoMrConfGroup'
_T='nemoStatsGroup'
_S='nemoBindingCacheGroup'
_R='explicitMode'
_Q='implicitMode'
_P='mip6MnBLCOAType'
_O='mip6MnBLCOA'
_N='mip6BindingHomeAddressType'
_M='mip6BindingHomeAddress'
_L='nemoMrBLEstablishedHomeTunnelIfIndex'
_K='nemoMrBLActiveEgressIfIndex'
_J='nemoMrBLCareofAddressPrefixLength'
_I='nemoMrBLHomeAddressPrefixLength'
_H='DateAndTime'
_G='Unsigned32'
_F='nemoSystemGroup'
_E='Integer32'
_D='MOBILEIPV6-MIB'
_C='read-only'
_B='NEMO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
mip6BindingCacheEntry,mip6BindingHomeAddress,mip6BindingHomeAddressType,mip6MnBLCOA,mip6MnBLCOAType,mip6MnBLEntry=mibBuilder.importSymbols(_D,'mip6BindingCacheEntry',_M,_N,_O,_P,'mip6MnBLEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
nemoMIB=ModuleIdentity((1,3,6,1,2,1,184))
if mibBuilder.loadTexts:nemoMIB.setRevisions(('2009-03-10 00:00',))
class NemoBURequestRejectionCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(140,141,142,143)));namedValues=NamedValues(*(('mobileRouterOperationNotPermitted',140),('invalidPrefix',141),('notAuthorizedForPrefix',142),('forwardingSetupFailed',143)))
_NemoNotifications_ObjectIdentity=ObjectIdentity
nemoNotifications=_NemoNotifications_ObjectIdentity((1,3,6,1,2,1,184,0))
_NemoObjects_ObjectIdentity=ObjectIdentity
nemoObjects=_NemoObjects_ObjectIdentity((1,3,6,1,2,1,184,1))
_NemoCore_ObjectIdentity=ObjectIdentity
nemoCore=_NemoCore_ObjectIdentity((1,3,6,1,2,1,184,1,1))
_NemoSystem_ObjectIdentity=ObjectIdentity
nemoSystem=_NemoSystem_ObjectIdentity((1,3,6,1,2,1,184,1,1,1))
class _NemoCapabilities_Type(Bits):namedValues=NamedValues(*(('mobileRouter',0),('homeAgentSupport',1)))
_NemoCapabilities_Type.__name__='Bits'
_NemoCapabilities_Object=MibScalar
nemoCapabilities=_NemoCapabilities_Object((1,3,6,1,2,1,184,1,1,1,1),_NemoCapabilities_Type())
nemoCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoCapabilities.setStatus(_A)
class _NemoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_NemoStatus_Type.__name__=_E
_NemoStatus_Object=MibScalar
nemoStatus=_NemoStatus_Object((1,3,6,1,2,1,184,1,1,1,2),_NemoStatus_Type())
nemoStatus.setMaxAccess(_X)
if mibBuilder.loadTexts:nemoStatus.setStatus(_A)
_NemoBindings_ObjectIdentity=ObjectIdentity
nemoBindings=_NemoBindings_ObjectIdentity((1,3,6,1,2,1,184,1,1,2))
_NemoBindingCacheTable_Object=MibTable
nemoBindingCacheTable=_NemoBindingCacheTable_Object((1,3,6,1,2,1,184,1,1,2,1))
if mibBuilder.loadTexts:nemoBindingCacheTable.setStatus(_A)
_NemoBindingCacheEntry_Object=MibTableRow
nemoBindingCacheEntry=_NemoBindingCacheEntry_Object((1,3,6,1,2,1,184,1,1,2,1,1))
if mibBuilder.loadTexts:nemoBindingCacheEntry.setStatus(_A)
_NemoBindingMrFlag_Type=TruthValue
_NemoBindingMrFlag_Object=MibTableColumn
nemoBindingMrFlag=_NemoBindingMrFlag_Object((1,3,6,1,2,1,184,1,1,2,1,1,1),_NemoBindingMrFlag_Type())
nemoBindingMrFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoBindingMrFlag.setStatus(_A)
class _NemoBindingMrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_NemoBindingMrMode_Type.__name__=_E
_NemoBindingMrMode_Object=MibTableColumn
nemoBindingMrMode=_NemoBindingMrMode_Object((1,3,6,1,2,1,184,1,1,2,1,1,2),_NemoBindingMrMode_Type())
nemoBindingMrMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoBindingMrMode.setStatus(_A)
_NemoConfiguration_ObjectIdentity=ObjectIdentity
nemoConfiguration=_NemoConfiguration_ObjectIdentity((1,3,6,1,2,1,184,1,1,3))
_NemoStats_ObjectIdentity=ObjectIdentity
nemoStats=_NemoStats_ObjectIdentity((1,3,6,1,2,1,184,1,1,4))
_NemoCounterDiscontinuityTime_Type=TimeStamp
_NemoCounterDiscontinuityTime_Object=MibScalar
nemoCounterDiscontinuityTime=_NemoCounterDiscontinuityTime_Object((1,3,6,1,2,1,184,1,1,4,1),_NemoCounterDiscontinuityTime_Type())
nemoCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoCounterDiscontinuityTime.setStatus(_A)
_NemoMr_ObjectIdentity=ObjectIdentity
nemoMr=_NemoMr_ObjectIdentity((1,3,6,1,2,1,184,1,2))
_NemoMrSystem_ObjectIdentity=ObjectIdentity
nemoMrSystem=_NemoMrSystem_ObjectIdentity((1,3,6,1,2,1,184,1,2,1))
_NemoMrEgressIfTable_Object=MibTable
nemoMrEgressIfTable=_NemoMrEgressIfTable_Object((1,3,6,1,2,1,184,1,2,1,1))
if mibBuilder.loadTexts:nemoMrEgressIfTable.setStatus(_A)
_NemoMrEgressIfEntry_Object=MibTableRow
nemoMrEgressIfEntry=_NemoMrEgressIfEntry_Object((1,3,6,1,2,1,184,1,2,1,1,1))
nemoMrEgressIfEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:nemoMrEgressIfEntry.setStatus(_A)
_NemoMrEgressIfIndex_Type=InterfaceIndex
_NemoMrEgressIfIndex_Object=MibTableColumn
nemoMrEgressIfIndex=_NemoMrEgressIfIndex_Object((1,3,6,1,2,1,184,1,2,1,1,1,1),_NemoMrEgressIfIndex_Type())
nemoMrEgressIfIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:nemoMrEgressIfIndex.setStatus(_A)
class _NemoMrEgressIfPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NemoMrEgressIfPriority_Type.__name__=_G
_NemoMrEgressIfPriority_Object=MibTableColumn
nemoMrEgressIfPriority=_NemoMrEgressIfPriority_Object((1,3,6,1,2,1,184,1,2,1,1,1,2),_NemoMrEgressIfPriority_Type())
nemoMrEgressIfPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrEgressIfPriority.setStatus(_A)
_NemoMrEgressIfDescription_Type=SnmpAdminString
_NemoMrEgressIfDescription_Object=MibTableColumn
nemoMrEgressIfDescription=_NemoMrEgressIfDescription_Object((1,3,6,1,2,1,184,1,2,1,1,1,3),_NemoMrEgressIfDescription_Type())
nemoMrEgressIfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrEgressIfDescription.setStatus(_A)
_NemoMrEgressIfRoamHoldDownTime_Type=Gauge32
_NemoMrEgressIfRoamHoldDownTime_Object=MibTableColumn
nemoMrEgressIfRoamHoldDownTime=_NemoMrEgressIfRoamHoldDownTime_Object((1,3,6,1,2,1,184,1,2,1,1,1,4),_NemoMrEgressIfRoamHoldDownTime_Type())
nemoMrEgressIfRoamHoldDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrEgressIfRoamHoldDownTime.setStatus(_A)
if mibBuilder.loadTexts:nemoMrEgressIfRoamHoldDownTime.setUnits('seconds')
_NemoMrConf_ObjectIdentity=ObjectIdentity
nemoMrConf=_NemoMrConf_ObjectIdentity((1,3,6,1,2,1,184,1,2,2))
_NemoMrDiscoveryRequests_Type=Counter32
_NemoMrDiscoveryRequests_Object=MibScalar
nemoMrDiscoveryRequests=_NemoMrDiscoveryRequests_Object((1,3,6,1,2,1,184,1,2,2,1),_NemoMrDiscoveryRequests_Type())
nemoMrDiscoveryRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrDiscoveryRequests.setStatus(_A)
_NemoMrDiscoveryReplies_Type=Counter32
_NemoMrDiscoveryReplies_Object=MibScalar
nemoMrDiscoveryReplies=_NemoMrDiscoveryReplies_Object((1,3,6,1,2,1,184,1,2,2,2),_NemoMrDiscoveryReplies_Type())
nemoMrDiscoveryReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrDiscoveryReplies.setStatus(_A)
_NemoMrDiscoveryRepliesRouterFlagZero_Type=Counter32
_NemoMrDiscoveryRepliesRouterFlagZero_Object=MibScalar
nemoMrDiscoveryRepliesRouterFlagZero=_NemoMrDiscoveryRepliesRouterFlagZero_Object((1,3,6,1,2,1,184,1,2,2,3),_NemoMrDiscoveryRepliesRouterFlagZero_Type())
nemoMrDiscoveryRepliesRouterFlagZero.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrDiscoveryRepliesRouterFlagZero.setStatus(_A)
_NemoMrMovedHome_Type=Counter32
_NemoMrMovedHome_Object=MibScalar
nemoMrMovedHome=_NemoMrMovedHome_Object((1,3,6,1,2,1,184,1,2,2,4),_NemoMrMovedHome_Type())
nemoMrMovedHome.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrMovedHome.setStatus(_A)
_NemoMrMovedOutofHome_Type=Counter32
_NemoMrMovedOutofHome_Object=MibScalar
nemoMrMovedOutofHome=_NemoMrMovedOutofHome_Object((1,3,6,1,2,1,184,1,2,2,5),_NemoMrMovedOutofHome_Type())
nemoMrMovedOutofHome.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrMovedOutofHome.setStatus(_A)
_NemoMrMovedFNtoFN_Type=Counter32
_NemoMrMovedFNtoFN_Object=MibScalar
nemoMrMovedFNtoFN=_NemoMrMovedFNtoFN_Object((1,3,6,1,2,1,184,1,2,2,6),_NemoMrMovedFNtoFN_Type())
nemoMrMovedFNtoFN.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrMovedFNtoFN.setStatus(_A)
_NemoMrBetterIfDetected_Type=Counter32
_NemoMrBetterIfDetected_Object=MibScalar
nemoMrBetterIfDetected=_NemoMrBetterIfDetected_Object((1,3,6,1,2,1,184,1,2,2,7),_NemoMrBetterIfDetected_Type())
nemoMrBetterIfDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBetterIfDetected.setStatus(_A)
_NemoMrRegistration_ObjectIdentity=ObjectIdentity
nemoMrRegistration=_NemoMrRegistration_ObjectIdentity((1,3,6,1,2,1,184,1,2,3))
_NemoMrBLTable_Object=MibTable
nemoMrBLTable=_NemoMrBLTable_Object((1,3,6,1,2,1,184,1,2,3,1))
if mibBuilder.loadTexts:nemoMrBLTable.setStatus(_A)
_NemoMrBLEntry_Object=MibTableRow
nemoMrBLEntry=_NemoMrBLEntry_Object((1,3,6,1,2,1,184,1,2,3,1,1))
if mibBuilder.loadTexts:nemoMrBLEntry.setStatus(_A)
class _NemoMrBLMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_NemoMrBLMode_Type.__name__=_E
_NemoMrBLMode_Object=MibTableColumn
nemoMrBLMode=_NemoMrBLMode_Object((1,3,6,1,2,1,184,1,2,3,1,1,1),_NemoMrBLMode_Type())
nemoMrBLMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBLMode.setStatus(_A)
_NemoMrBLMrFlag_Type=TruthValue
_NemoMrBLMrFlag_Object=MibTableColumn
nemoMrBLMrFlag=_NemoMrBLMrFlag_Object((1,3,6,1,2,1,184,1,2,3,1,1,2),_NemoMrBLMrFlag_Type())
nemoMrBLMrFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBLMrFlag.setStatus(_A)
_NemoMrBLHomeAddressPrefixLength_Type=InetAddressPrefixLength
_NemoMrBLHomeAddressPrefixLength_Object=MibTableColumn
nemoMrBLHomeAddressPrefixLength=_NemoMrBLHomeAddressPrefixLength_Object((1,3,6,1,2,1,184,1,2,3,1,1,3),_NemoMrBLHomeAddressPrefixLength_Type())
nemoMrBLHomeAddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBLHomeAddressPrefixLength.setStatus(_A)
_NemoMrBLCareofAddressPrefixLength_Type=InetAddressPrefixLength
_NemoMrBLCareofAddressPrefixLength_Object=MibTableColumn
nemoMrBLCareofAddressPrefixLength=_NemoMrBLCareofAddressPrefixLength_Object((1,3,6,1,2,1,184,1,2,3,1,1,4),_NemoMrBLCareofAddressPrefixLength_Type())
nemoMrBLCareofAddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBLCareofAddressPrefixLength.setStatus(_A)
_NemoMrBLActiveEgressIfIndex_Type=InterfaceIndex
_NemoMrBLActiveEgressIfIndex_Object=MibTableColumn
nemoMrBLActiveEgressIfIndex=_NemoMrBLActiveEgressIfIndex_Object((1,3,6,1,2,1,184,1,2,3,1,1,5),_NemoMrBLActiveEgressIfIndex_Type())
nemoMrBLActiveEgressIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBLActiveEgressIfIndex.setStatus(_A)
_NemoMrBLEstablishedHomeTunnelIfIndex_Type=InterfaceIndex
_NemoMrBLEstablishedHomeTunnelIfIndex_Object=MibTableColumn
nemoMrBLEstablishedHomeTunnelIfIndex=_NemoMrBLEstablishedHomeTunnelIfIndex_Object((1,3,6,1,2,1,184,1,2,3,1,1,6),_NemoMrBLEstablishedHomeTunnelIfIndex_Type())
nemoMrBLEstablishedHomeTunnelIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBLEstablishedHomeTunnelIfIndex.setStatus(_A)
_NemoMrRegnCounters_ObjectIdentity=ObjectIdentity
nemoMrRegnCounters=_NemoMrRegnCounters_ObjectIdentity((1,3,6,1,2,1,184,1,2,3,2))
_NemoMrMobilityMessagesSent_Type=Counter32
_NemoMrMobilityMessagesSent_Object=MibScalar
nemoMrMobilityMessagesSent=_NemoMrMobilityMessagesSent_Object((1,3,6,1,2,1,184,1,2,3,2,1),_NemoMrMobilityMessagesSent_Type())
nemoMrMobilityMessagesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrMobilityMessagesSent.setStatus(_A)
_NemoMrMobilityMessagesRecd_Type=Counter32
_NemoMrMobilityMessagesRecd_Object=MibScalar
nemoMrMobilityMessagesRecd=_NemoMrMobilityMessagesRecd_Object((1,3,6,1,2,1,184,1,2,3,2,2),_NemoMrMobilityMessagesRecd_Type())
nemoMrMobilityMessagesRecd.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrMobilityMessagesRecd.setStatus(_A)
class _NemoMrPrefixRegMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_NemoMrPrefixRegMode_Type.__name__=_E
_NemoMrPrefixRegMode_Object=MibScalar
nemoMrPrefixRegMode=_NemoMrPrefixRegMode_Object((1,3,6,1,2,1,184,1,2,3,3),_NemoMrPrefixRegMode_Type())
nemoMrPrefixRegMode.setMaxAccess(_X)
if mibBuilder.loadTexts:nemoMrPrefixRegMode.setStatus(_A)
_NemoMrGlobalStats_ObjectIdentity=ObjectIdentity
nemoMrGlobalStats=_NemoMrGlobalStats_ObjectIdentity((1,3,6,1,2,1,184,1,2,4))
_NemoMrBindingAcksWONemoSupport_Type=Counter32
_NemoMrBindingAcksWONemoSupport_Object=MibScalar
nemoMrBindingAcksWONemoSupport=_NemoMrBindingAcksWONemoSupport_Object((1,3,6,1,2,1,184,1,2,4,1),_NemoMrBindingAcksWONemoSupport_Type())
nemoMrBindingAcksWONemoSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBindingAcksWONemoSupport.setStatus(_A)
_NemoMrBindingAcksRegTypeChangeDisallowed_Type=Counter32
_NemoMrBindingAcksRegTypeChangeDisallowed_Object=MibScalar
nemoMrBindingAcksRegTypeChangeDisallowed=_NemoMrBindingAcksRegTypeChangeDisallowed_Object((1,3,6,1,2,1,184,1,2,4,2),_NemoMrBindingAcksRegTypeChangeDisallowed_Type())
nemoMrBindingAcksRegTypeChangeDisallowed.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBindingAcksRegTypeChangeDisallowed.setStatus(_A)
_NemoMrBindingAcksOperationNotPermitted_Type=Counter32
_NemoMrBindingAcksOperationNotPermitted_Object=MibScalar
nemoMrBindingAcksOperationNotPermitted=_NemoMrBindingAcksOperationNotPermitted_Object((1,3,6,1,2,1,184,1,2,4,3),_NemoMrBindingAcksOperationNotPermitted_Type())
nemoMrBindingAcksOperationNotPermitted.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBindingAcksOperationNotPermitted.setStatus(_A)
_NemoMrBindingAcksInvalidPrefix_Type=Counter32
_NemoMrBindingAcksInvalidPrefix_Object=MibScalar
nemoMrBindingAcksInvalidPrefix=_NemoMrBindingAcksInvalidPrefix_Object((1,3,6,1,2,1,184,1,2,4,4),_NemoMrBindingAcksInvalidPrefix_Type())
nemoMrBindingAcksInvalidPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBindingAcksInvalidPrefix.setStatus(_A)
_NemoMrBindingAcksNotAuthorizedForPrefix_Type=Counter32
_NemoMrBindingAcksNotAuthorizedForPrefix_Object=MibScalar
nemoMrBindingAcksNotAuthorizedForPrefix=_NemoMrBindingAcksNotAuthorizedForPrefix_Object((1,3,6,1,2,1,184,1,2,4,5),_NemoMrBindingAcksNotAuthorizedForPrefix_Type())
nemoMrBindingAcksNotAuthorizedForPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBindingAcksNotAuthorizedForPrefix.setStatus(_A)
_NemoMrBindingAcksForwardingSetupFailed_Type=Counter32
_NemoMrBindingAcksForwardingSetupFailed_Object=MibScalar
nemoMrBindingAcksForwardingSetupFailed=_NemoMrBindingAcksForwardingSetupFailed_Object((1,3,6,1,2,1,184,1,2,4,6),_NemoMrBindingAcksForwardingSetupFailed_Type())
nemoMrBindingAcksForwardingSetupFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBindingAcksForwardingSetupFailed.setStatus(_A)
_NemoMrBindingAcksOtherError_Type=Counter32
_NemoMrBindingAcksOtherError_Object=MibScalar
nemoMrBindingAcksOtherError=_NemoMrBindingAcksOtherError_Object((1,3,6,1,2,1,184,1,2,4,7),_NemoMrBindingAcksOtherError_Type())
nemoMrBindingAcksOtherError.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoMrBindingAcksOtherError.setStatus(_A)
_NemoCn_ObjectIdentity=ObjectIdentity
nemoCn=_NemoCn_ObjectIdentity((1,3,6,1,2,1,184,1,3))
_NemoHa_ObjectIdentity=ObjectIdentity
nemoHa=_NemoHa_ObjectIdentity((1,3,6,1,2,1,184,1,4))
_NemoHaAdvertisement_ObjectIdentity=ObjectIdentity
nemoHaAdvertisement=_NemoHaAdvertisement_ObjectIdentity((1,3,6,1,2,1,184,1,4,1))
_NemoHaStats_ObjectIdentity=ObjectIdentity
nemoHaStats=_NemoHaStats_ObjectIdentity((1,3,6,1,2,1,184,1,4,2))
_NemoHaGlobalStats_ObjectIdentity=ObjectIdentity
nemoHaGlobalStats=_NemoHaGlobalStats_ObjectIdentity((1,3,6,1,2,1,184,1,4,2,1))
_NemoHaBUAcksWONemoSupport_Type=Counter32
_NemoHaBUAcksWONemoSupport_Object=MibScalar
nemoHaBUAcksWONemoSupport=_NemoHaBUAcksWONemoSupport_Object((1,3,6,1,2,1,184,1,4,2,1,1),_NemoHaBUAcksWONemoSupport_Type())
nemoHaBUAcksWONemoSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBUAcksWONemoSupport.setStatus(_A)
_NemoHaBUAcksRegTypeChangeDisallowed_Type=Counter32
_NemoHaBUAcksRegTypeChangeDisallowed_Object=MibScalar
nemoHaBUAcksRegTypeChangeDisallowed=_NemoHaBUAcksRegTypeChangeDisallowed_Object((1,3,6,1,2,1,184,1,4,2,1,2),_NemoHaBUAcksRegTypeChangeDisallowed_Type())
nemoHaBUAcksRegTypeChangeDisallowed.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBUAcksRegTypeChangeDisallowed.setStatus(_A)
_NemoHaBUAcksOperationNotPermitted_Type=Counter32
_NemoHaBUAcksOperationNotPermitted_Object=MibScalar
nemoHaBUAcksOperationNotPermitted=_NemoHaBUAcksOperationNotPermitted_Object((1,3,6,1,2,1,184,1,4,2,1,3),_NemoHaBUAcksOperationNotPermitted_Type())
nemoHaBUAcksOperationNotPermitted.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBUAcksOperationNotPermitted.setStatus(_A)
_NemoHaBUAcksInvalidPrefix_Type=Counter32
_NemoHaBUAcksInvalidPrefix_Object=MibScalar
nemoHaBUAcksInvalidPrefix=_NemoHaBUAcksInvalidPrefix_Object((1,3,6,1,2,1,184,1,4,2,1,4),_NemoHaBUAcksInvalidPrefix_Type())
nemoHaBUAcksInvalidPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBUAcksInvalidPrefix.setStatus(_A)
_NemoHaBUAcksNotAuthorizedForPrefix_Type=Counter32
_NemoHaBUAcksNotAuthorizedForPrefix_Object=MibScalar
nemoHaBUAcksNotAuthorizedForPrefix=_NemoHaBUAcksNotAuthorizedForPrefix_Object((1,3,6,1,2,1,184,1,4,2,1,5),_NemoHaBUAcksNotAuthorizedForPrefix_Type())
nemoHaBUAcksNotAuthorizedForPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBUAcksNotAuthorizedForPrefix.setStatus(_A)
_NemoHaBUAcksForwardingSetupFailed_Type=Counter32
_NemoHaBUAcksForwardingSetupFailed_Object=MibScalar
nemoHaBUAcksForwardingSetupFailed=_NemoHaBUAcksForwardingSetupFailed_Object((1,3,6,1,2,1,184,1,4,2,1,6),_NemoHaBUAcksForwardingSetupFailed_Type())
nemoHaBUAcksForwardingSetupFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBUAcksForwardingSetupFailed.setStatus(_A)
_NemoHaBUAcksOtherError_Type=Counter32
_NemoHaBUAcksOtherError_Object=MibScalar
nemoHaBUAcksOtherError=_NemoHaBUAcksOtherError_Object((1,3,6,1,2,1,184,1,4,2,1,7),_NemoHaBUAcksOtherError_Type())
nemoHaBUAcksOtherError.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBUAcksOtherError.setStatus(_A)
_NemoHaCounterTable_Object=MibTable
nemoHaCounterTable=_NemoHaCounterTable_Object((1,3,6,1,2,1,184,1,4,2,2))
if mibBuilder.loadTexts:nemoHaCounterTable.setStatus(_A)
_NemoHaCounterEntry_Object=MibTableRow
nemoHaCounterEntry=_NemoHaCounterEntry_Object((1,3,6,1,2,1,184,1,4,2,2,1))
nemoHaCounterEntry.setIndexNames((0,_D,_N),(0,_D,_M))
if mibBuilder.loadTexts:nemoHaCounterEntry.setStatus(_A)
_NemoHaBURequestsAccepted_Type=Counter32
_NemoHaBURequestsAccepted_Object=MibTableColumn
nemoHaBURequestsAccepted=_NemoHaBURequestsAccepted_Object((1,3,6,1,2,1,184,1,4,2,2,1,1),_NemoHaBURequestsAccepted_Type())
nemoHaBURequestsAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBURequestsAccepted.setStatus(_A)
_NemoHaBURequestsDenied_Type=Counter32
_NemoHaBURequestsDenied_Object=MibTableColumn
nemoHaBURequestsDenied=_NemoHaBURequestsDenied_Object((1,3,6,1,2,1,184,1,4,2,2,1,2),_NemoHaBURequestsDenied_Type())
nemoHaBURequestsDenied.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBURequestsDenied.setStatus(_A)
class _NemoHaBCEntryCreationTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_NemoHaBCEntryCreationTime_Type.__name__=_H
_NemoHaBCEntryCreationTime_Object=MibTableColumn
nemoHaBCEntryCreationTime=_NemoHaBCEntryCreationTime_Object((1,3,6,1,2,1,184,1,4,2,2,1,3),_NemoHaBCEntryCreationTime_Type())
nemoHaBCEntryCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBCEntryCreationTime.setStatus(_A)
class _NemoHaBUAcceptedTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_NemoHaBUAcceptedTime_Type.__name__=_H
_NemoHaBUAcceptedTime_Object=MibTableColumn
nemoHaBUAcceptedTime=_NemoHaBUAcceptedTime_Object((1,3,6,1,2,1,184,1,4,2,2,1,4),_NemoHaBUAcceptedTime_Type())
nemoHaBUAcceptedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBUAcceptedTime.setStatus(_A)
class _NemoHaBURejectionTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_NemoHaBURejectionTime_Type.__name__=_H
_NemoHaBURejectionTime_Object=MibTableColumn
nemoHaBURejectionTime=_NemoHaBURejectionTime_Object((1,3,6,1,2,1,184,1,4,2,2,1,5),_NemoHaBURejectionTime_Type())
nemoHaBURejectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaBURejectionTime.setStatus(_A)
_NemoHaRecentBURejectionCode_Type=NemoBURequestRejectionCode
_NemoHaRecentBURejectionCode_Object=MibTableColumn
nemoHaRecentBURejectionCode=_NemoHaRecentBURejectionCode_Object((1,3,6,1,2,1,184,1,4,2,2,1,6),_NemoHaRecentBURejectionCode_Type())
nemoHaRecentBURejectionCode.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaRecentBURejectionCode.setStatus(_A)
_NemoHaCtrDiscontinuityTime_Type=TimeStamp
_NemoHaCtrDiscontinuityTime_Object=MibTableColumn
nemoHaCtrDiscontinuityTime=_NemoHaCtrDiscontinuityTime_Object((1,3,6,1,2,1,184,1,4,2,2,1,7),_NemoHaCtrDiscontinuityTime_Type())
nemoHaCtrDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaCtrDiscontinuityTime.setStatus(_A)
_NemoHaRegistration_ObjectIdentity=ObjectIdentity
nemoHaRegistration=_NemoHaRegistration_ObjectIdentity((1,3,6,1,2,1,184,1,4,3))
_NemoHaMobileNetworkPrefixTable_Object=MibTable
nemoHaMobileNetworkPrefixTable=_NemoHaMobileNetworkPrefixTable_Object((1,3,6,1,2,1,184,1,4,3,1))
if mibBuilder.loadTexts:nemoHaMobileNetworkPrefixTable.setStatus(_A)
_NemoHaMobileNetworkPrefixEntry_Object=MibTableRow
nemoHaMobileNetworkPrefixEntry=_NemoHaMobileNetworkPrefixEntry_Object((1,3,6,1,2,1,184,1,4,3,1,1))
nemoHaMobileNetworkPrefixEntry.setIndexNames((0,_D,_N),(0,_D,_M),(0,_B,_a))
if mibBuilder.loadTexts:nemoHaMobileNetworkPrefixEntry.setStatus(_A)
class _NemoHaMobileNetworkPrefixSeqNo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_NemoHaMobileNetworkPrefixSeqNo_Type.__name__=_G
_NemoHaMobileNetworkPrefixSeqNo_Object=MibTableColumn
nemoHaMobileNetworkPrefixSeqNo=_NemoHaMobileNetworkPrefixSeqNo_Object((1,3,6,1,2,1,184,1,4,3,1,1,1),_NemoHaMobileNetworkPrefixSeqNo_Type())
nemoHaMobileNetworkPrefixSeqNo.setMaxAccess(_Z)
if mibBuilder.loadTexts:nemoHaMobileNetworkPrefixSeqNo.setStatus(_A)
_NemoHaMobileNetworkPrefixType_Type=InetAddressType
_NemoHaMobileNetworkPrefixType_Object=MibTableColumn
nemoHaMobileNetworkPrefixType=_NemoHaMobileNetworkPrefixType_Object((1,3,6,1,2,1,184,1,4,3,1,1,2),_NemoHaMobileNetworkPrefixType_Type())
nemoHaMobileNetworkPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaMobileNetworkPrefixType.setStatus(_A)
_NemoHaMobileNetworkPrefix_Type=InetAddress
_NemoHaMobileNetworkPrefix_Object=MibTableColumn
nemoHaMobileNetworkPrefix=_NemoHaMobileNetworkPrefix_Object((1,3,6,1,2,1,184,1,4,3,1,1,3),_NemoHaMobileNetworkPrefix_Type())
nemoHaMobileNetworkPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaMobileNetworkPrefix.setStatus(_A)
class _NemoHaMobileNetworkPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_NemoHaMobileNetworkPrefixLength_Type.__name__=_G
_NemoHaMobileNetworkPrefixLength_Object=MibTableColumn
nemoHaMobileNetworkPrefixLength=_NemoHaMobileNetworkPrefixLength_Object((1,3,6,1,2,1,184,1,4,3,1,1,4),_NemoHaMobileNetworkPrefixLength_Type())
nemoHaMobileNetworkPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaMobileNetworkPrefixLength.setStatus(_A)
class _NemoHaMobileNetworkPrefixSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configured',1),('bindingUpdate',2)))
_NemoHaMobileNetworkPrefixSource_Type.__name__=_E
_NemoHaMobileNetworkPrefixSource_Object=MibTableColumn
nemoHaMobileNetworkPrefixSource=_NemoHaMobileNetworkPrefixSource_Object((1,3,6,1,2,1,184,1,4,3,1,1,5),_NemoHaMobileNetworkPrefixSource_Type())
nemoHaMobileNetworkPrefixSource.setMaxAccess(_C)
if mibBuilder.loadTexts:nemoHaMobileNetworkPrefixSource.setStatus(_A)
_NemoConformance_ObjectIdentity=ObjectIdentity
nemoConformance=_NemoConformance_ObjectIdentity((1,3,6,1,2,1,184,2))
_NemoGroups_ObjectIdentity=ObjectIdentity
nemoGroups=_NemoGroups_ObjectIdentity((1,3,6,1,2,1,184,2,1))
_NemoCompliances_ObjectIdentity=ObjectIdentity
nemoCompliances=_NemoCompliances_ObjectIdentity((1,3,6,1,2,1,184,2,2))
mip6BindingCacheEntry.registerAugmentions((_B,_b))
nemoBindingCacheEntry.setIndexNames(*mip6BindingCacheEntry.getIndexNames())
mip6MnBLEntry.registerAugmentions((_B,_c))
nemoMrBLEntry.setIndexNames(*mip6MnBLEntry.getIndexNames())
nemoSystemGroup=ObjectGroup((1,3,6,1,2,1,184,2,1,1))
nemoSystemGroup.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:nemoSystemGroup.setStatus(_A)
nemoBindingCacheGroup=ObjectGroup((1,3,6,1,2,1,184,2,1,2))
nemoBindingCacheGroup.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:nemoBindingCacheGroup.setStatus(_A)
nemoStatsGroup=ObjectGroup((1,3,6,1,2,1,184,2,1,3))
nemoStatsGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:nemoStatsGroup.setStatus(_A)
nemoMrConfGroup=ObjectGroup((1,3,6,1,2,1,184,2,1,4))
nemoMrConfGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:nemoMrConfGroup.setStatus(_A)
nemoMrRegistrationGroup=ObjectGroup((1,3,6,1,2,1,184,2,1,5))
nemoMrRegistrationGroup.setObjects(*((_B,_s),(_B,_t),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:nemoMrRegistrationGroup.setStatus(_A)
nemoHaSystemGroup=ObjectGroup((1,3,6,1,2,1,184,2,1,6))
nemoHaSystemGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:nemoHaSystemGroup.setStatus(_A)
nemoHaStatsGroup=ObjectGroup((1,3,6,1,2,1,184,2,1,7))
nemoHaStatsGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:nemoHaStatsGroup.setStatus(_A)
nemoHaGlobalStatsGroup=ObjectGroup((1,3,6,1,2,1,184,2,1,8))
nemoHaGlobalStatsGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:nemoHaGlobalStatsGroup.setStatus(_A)
nemoHomeTunnelEstablished=NotificationType((1,3,6,1,2,1,184,0,1))
nemoHomeTunnelEstablished.setObjects(*((_B,_K),(_B,_L),(_D,_P),(_D,_O),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:nemoHomeTunnelEstablished.setStatus(_A)
nemoHomeTunnelReleased=NotificationType((1,3,6,1,2,1,184,0,2))
nemoHomeTunnelReleased.setObjects(*((_B,_K),(_B,_L),(_D,_P),(_D,_O),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:nemoHomeTunnelReleased.setStatus(_A)
nemoNotificationGroup=NotificationGroup((1,3,6,1,2,1,184,2,1,9))
nemoNotificationGroup.setObjects(*((_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:nemoNotificationGroup.setStatus(_A)
nemoCoreCompliance=ModuleCompliance((1,3,6,1,2,1,184,2,2,1))
nemoCoreCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:nemoCoreCompliance.setStatus(_A)
nemoCompliance2=ModuleCompliance((1,3,6,1,2,1,184,2,2,2))
nemoCompliance2.setObjects(*((_B,_F),(_B,_S)))
if mibBuilder.loadTexts:nemoCompliance2.setStatus(_A)
nemoCoreReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,184,2,2,3))
nemoCoreReadOnlyCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:nemoCoreReadOnlyCompliance.setStatus(_A)
nemoReadOnlyCompliance2=ModuleCompliance((1,3,6,1,2,1,184,2,2,4))
nemoReadOnlyCompliance2.setObjects(*((_B,_F),(_B,_S)))
if mibBuilder.loadTexts:nemoReadOnlyCompliance2.setStatus(_A)
nemoMrCompliance=ModuleCompliance((1,3,6,1,2,1,184,2,2,5))
nemoMrCompliance.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:nemoMrCompliance.setStatus(_A)
nemoMrReadOnlyCompliance2=ModuleCompliance((1,3,6,1,2,1,184,2,2,6))
nemoMrReadOnlyCompliance2.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:nemoMrReadOnlyCompliance2.setStatus(_A)
nemoHaCoreCompliance=ModuleCompliance((1,3,6,1,2,1,184,2,2,7))
nemoHaCoreCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:nemoHaCoreCompliance.setStatus(_A)
nemoHaCompliance2=ModuleCompliance((1,3,6,1,2,1,184,2,2,8))
nemoHaCompliance2.setObjects(*((_B,_W),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:nemoHaCompliance2.setStatus(_A)
nemoNotificationCompliance=ModuleCompliance((1,3,6,1,2,1,184,2,2,9))
nemoNotificationCompliance.setObjects((_B,_AQ))
if mibBuilder.loadTexts:nemoNotificationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NemoBURequestRejectionCode':NemoBURequestRejectionCode,'nemoMIB':nemoMIB,'nemoNotifications':nemoNotifications,_AM:nemoHomeTunnelEstablished,_AN:nemoHomeTunnelReleased,'nemoObjects':nemoObjects,'nemoCore':nemoCore,'nemoSystem':nemoSystem,_d:nemoCapabilities,_e:nemoStatus,'nemoBindings':nemoBindings,'nemoBindingCacheTable':nemoBindingCacheTable,_b:nemoBindingCacheEntry,_f:nemoBindingMrFlag,_g:nemoBindingMrMode,'nemoConfiguration':nemoConfiguration,'nemoStats':nemoStats,_h:nemoCounterDiscontinuityTime,'nemoMr':nemoMr,'nemoMrSystem':nemoMrSystem,'nemoMrEgressIfTable':nemoMrEgressIfTable,'nemoMrEgressIfEntry':nemoMrEgressIfEntry,_Y:nemoMrEgressIfIndex,_i:nemoMrEgressIfPriority,_j:nemoMrEgressIfDescription,_k:nemoMrEgressIfRoamHoldDownTime,'nemoMrConf':nemoMrConf,_l:nemoMrDiscoveryRequests,_m:nemoMrDiscoveryReplies,_n:nemoMrDiscoveryRepliesRouterFlagZero,_o:nemoMrMovedHome,_p:nemoMrMovedOutofHome,_q:nemoMrMovedFNtoFN,_r:nemoMrBetterIfDetected,'nemoMrRegistration':nemoMrRegistration,'nemoMrBLTable':nemoMrBLTable,_c:nemoMrBLEntry,_s:nemoMrBLMode,_t:nemoMrBLMrFlag,_I:nemoMrBLHomeAddressPrefixLength,_J:nemoMrBLCareofAddressPrefixLength,_K:nemoMrBLActiveEgressIfIndex,_L:nemoMrBLEstablishedHomeTunnelIfIndex,'nemoMrRegnCounters':nemoMrRegnCounters,_u:nemoMrMobilityMessagesSent,_v:nemoMrMobilityMessagesRecd,_w:nemoMrPrefixRegMode,'nemoMrGlobalStats':nemoMrGlobalStats,_x:nemoMrBindingAcksWONemoSupport,_y:nemoMrBindingAcksRegTypeChangeDisallowed,_z:nemoMrBindingAcksOperationNotPermitted,_A0:nemoMrBindingAcksInvalidPrefix,_A1:nemoMrBindingAcksNotAuthorizedForPrefix,_A2:nemoMrBindingAcksForwardingSetupFailed,_A3:nemoMrBindingAcksOtherError,'nemoCn':nemoCn,'nemoHa':nemoHa,'nemoHaAdvertisement':nemoHaAdvertisement,'nemoHaStats':nemoHaStats,'nemoHaGlobalStats':nemoHaGlobalStats,_AF:nemoHaBUAcksWONemoSupport,_AG:nemoHaBUAcksRegTypeChangeDisallowed,_AH:nemoHaBUAcksOperationNotPermitted,_AI:nemoHaBUAcksInvalidPrefix,_AJ:nemoHaBUAcksNotAuthorizedForPrefix,_AK:nemoHaBUAcksForwardingSetupFailed,_AL:nemoHaBUAcksOtherError,'nemoHaCounterTable':nemoHaCounterTable,'nemoHaCounterEntry':nemoHaCounterEntry,_A8:nemoHaBURequestsAccepted,_A9:nemoHaBURequestsDenied,_AA:nemoHaBCEntryCreationTime,_AB:nemoHaBUAcceptedTime,_AC:nemoHaBURejectionTime,_AD:nemoHaRecentBURejectionCode,_AE:nemoHaCtrDiscontinuityTime,'nemoHaRegistration':nemoHaRegistration,'nemoHaMobileNetworkPrefixTable':nemoHaMobileNetworkPrefixTable,'nemoHaMobileNetworkPrefixEntry':nemoHaMobileNetworkPrefixEntry,_a:nemoHaMobileNetworkPrefixSeqNo,_A4:nemoHaMobileNetworkPrefixType,_A5:nemoHaMobileNetworkPrefix,_A6:nemoHaMobileNetworkPrefixLength,_A7:nemoHaMobileNetworkPrefixSource,'nemoConformance':nemoConformance,'nemoGroups':nemoGroups,_F:nemoSystemGroup,_S:nemoBindingCacheGroup,_T:nemoStatsGroup,_U:nemoMrConfGroup,_V:nemoMrRegistrationGroup,_W:nemoHaSystemGroup,_AO:nemoHaStatsGroup,_AP:nemoHaGlobalStatsGroup,_AQ:nemoNotificationGroup,'nemoCompliances':nemoCompliances,'nemoCoreCompliance':nemoCoreCompliance,'nemoCompliance2':nemoCompliance2,'nemoCoreReadOnlyCompliance':nemoCoreReadOnlyCompliance,'nemoReadOnlyCompliance2':nemoReadOnlyCompliance2,'nemoMrCompliance':nemoMrCompliance,'nemoMrReadOnlyCompliance2':nemoMrReadOnlyCompliance2,'nemoHaCoreCompliance':nemoHaCoreCompliance,'nemoHaCompliance2':nemoHaCompliance2,'nemoNotificationCompliance':nemoNotificationCompliance})