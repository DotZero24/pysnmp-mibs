_Ai='pmip6LmaNotificationGroup'
_Ah='pmip6MagNotificationGroup'
_Ag='pmip6LmaHomeTunnelReleased'
_Af='pmip6LmaHomeTunnelEstablished'
_Ae='pmip6MagHomeTunnelReleased'
_Ad='pmip6MagHomeTunnelEstablished'
_Ac='pmip6LmaHomeNetworkPrefixLifeTime'
_Ab='pmip6LmaHomeNetworkPrefixLength'
_Aa='pmip6LmaTimestampValidityWindow'
_AZ='pmip6LmaMaxDelayBeforeNewBCEAssign'
_AY='pmip6LmaMinDelayBeforeBCEDelete'
_AX='pmip6LmaStatus'
_AW='pmip6MagProfMnLocalMobilityAnchorAddress'
_AV='pmip6MagProfMnLocalMobilityAnchorAddressType'
_AU='pmip6MagProfMnIdentifier'
_AT='pmip6MagMnLLIdentifier'
_AS='pmip6MagMnIdentifier'
_AR='pmip6MagBLTimeRecentlyAccepted'
_AQ='pmip6MagBLMnInterfaceATT'
_AP='pmip6MagBLMagIfIdentifierToMn'
_AO='pmip6MagBLMagLinkLocalAddress'
_AN='pmip6MagBLMagLinkLocalAddressType'
_AM='pmip6MagBLFlag'
_AL='pmip6MagEnableMagLocalRouting'
_AK='pmip6MagHomeNetworkPrefixLifeTime'
_AJ='pmip6MagHomeNetworkPrefixLength'
_AI='pmip6MagStatus'
_AH='pmip6CounterDiscontinuityTime'
_AG='pmip6BindingBindingAcks'
_AF='pmip6BindingDeRegistrations'
_AE='pmip6BindingLifeTimeExtensionAfterHandOff'
_AD='pmip6BindingLifeTimeExtensionNoHandOff'
_AC='pmip6InitialBindingRegistrations'
_AB='pmip6BcePbuPrefixSetDoNotMatch'
_AA='pmip6TimestampLowerThanPrevAccepted'
_A9='pmip6TimestampMismatch'
_A8='pmip6NotAuthorizedForHomeNetworkPrefix'
_A7='pmip6MissingAccessTechTypeOption'
_A6='pmip6MissingHandOffIndicatorOption'
_A5='pmip6MissingHomeNetworkPrefixOption'
_A4='pmip6ProxyRegNotEnabled'
_A3='pmip6NotLMAForThisMobileNode'
_A2='pmip6MagNotAuthorizedForProxyReg'
_A1='pmip6MissingMnIdentifierOption'
_A0='pmip6LmaMnLLIdentifier'
_z='pmip6LmaMnIdentifier'
_y='pmip6BindingTimeRecentlyAccepted'
_x='pmip6BindingMnInterfaceATT'
_w='pmip6BindingMagLinkLocalAddress'
_v='pmip6BindingMagLinkLocalAddressType'
_u='pmip6BindingPBUFlag'
_t='pmip6FixedMagLinkLayerAddressOnAllAccessLinks'
_s='pmip6FixedMagLinkLocalAddressOnAllAccessLinks'
_r='pmip6FixedMagLinkLocalAddressOnAllAccessLinksType'
_q='pmip6MobileNodeGeneratedTimestampInUse'
_p='pmip6Capabilities'
_o='pmip6MagBLEntry'
_n='pmip6BindingCacheEntry'
_m='pmip6LmaHomeNetworkPrefix'
_l='pmip6LmaHomeNetworkPrefixType'
_k='pmip6LmaLMAA'
_j='pmip6LmaLMAAType'
_i='pmip6MagProfMnIndex'
_h='seconds'
_g='pmip6MagHomeNetworkPrefix'
_f='pmip6MagHomeNetworkPrefixType'
_e='tunneled'
_d='activated'
_c='unknown'
_b='pmip6MagProxyCOA'
_a='pmip6MagProxyCOAType'
_Z='disabled'
_Y='enabled'
_X='pmip6LmaConfigurationGroup'
_W='pmip6MagRegistrationGroup'
_V='pmip6MagConfigurationGroup'
_U='pmip6StatsGroup'
_T='pmip6BindingCacheGroup'
_S='milliseconds'
_R='TruthValue'
_Q='pmip6LmaLMAAState'
_P='pmip6MagBLTunnelIfIdentifier'
_O='pmip6MagProxyCOAState'
_N='pmip6BindingTunnelIfIdentifier'
_M='pmip6BindingMnLLIndex'
_L='pmip6MagBLMnLLIndex'
_K='pmip6LmaSystemGroup'
_J='pmip6MagSystemGroup'
_I='pmip6SystemGroup'
_H='pmip6BindingMnIndex'
_G='pmip6MagBLMnIndex'
_F='Integer32'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='PMIPV6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
Ipv6AddressIfIdentifierTC,=mibBuilder.importSymbols('IP-MIB','Ipv6AddressIfIdentifierTC')
mip6BindingCacheEntry,mip6MnBLEntry=mibBuilder.importSymbols('MOBILEIPV6-MIB','mip6BindingCacheEntry','mip6MnBLEntry')
Pmip6MnIdentifier,Pmip6MnIndex,Pmip6MnInterfaceATT,Pmip6MnLLIdentifier,Pmip6MnLLIndex,Pmip6TimeStamp64=mibBuilder.importSymbols('PMIPV6-TC-MIB','Pmip6MnIdentifier','Pmip6MnIndex','Pmip6MnInterfaceATT','Pmip6MnLLIdentifier','Pmip6MnLLIndex','Pmip6TimeStamp64')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_R)
pmip6MIB=ModuleIdentity((1,3,6,1,2,1,206))
if mibBuilder.loadTexts:pmip6MIB.setRevisions(('2012-05-07 00:00',))
_Pmip6Notifications_ObjectIdentity=ObjectIdentity
pmip6Notifications=_Pmip6Notifications_ObjectIdentity((1,3,6,1,2,1,206,0))
_Pmip6Objects_ObjectIdentity=ObjectIdentity
pmip6Objects=_Pmip6Objects_ObjectIdentity((1,3,6,1,2,1,206,1))
_Pmip6Core_ObjectIdentity=ObjectIdentity
pmip6Core=_Pmip6Core_ObjectIdentity((1,3,6,1,2,1,206,1,1))
_Pmip6System_ObjectIdentity=ObjectIdentity
pmip6System=_Pmip6System_ObjectIdentity((1,3,6,1,2,1,206,1,1,1))
class _Pmip6Capabilities_Type(Bits):namedValues=NamedValues(*(('mobilityAccessGateway',0),('localMobilityAnchor',1)))
_Pmip6Capabilities_Type.__name__='Bits'
_Pmip6Capabilities_Object=MibScalar
pmip6Capabilities=_Pmip6Capabilities_Object((1,3,6,1,2,1,206,1,1,1,1),_Pmip6Capabilities_Type())
pmip6Capabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6Capabilities.setStatus(_A)
_Pmip6Bindings_ObjectIdentity=ObjectIdentity
pmip6Bindings=_Pmip6Bindings_ObjectIdentity((1,3,6,1,2,1,206,1,1,2))
_Pmip6BindingCacheTable_Object=MibTable
pmip6BindingCacheTable=_Pmip6BindingCacheTable_Object((1,3,6,1,2,1,206,1,1,2,1))
if mibBuilder.loadTexts:pmip6BindingCacheTable.setStatus(_A)
_Pmip6BindingCacheEntry_Object=MibTableRow
pmip6BindingCacheEntry=_Pmip6BindingCacheEntry_Object((1,3,6,1,2,1,206,1,1,2,1,1))
if mibBuilder.loadTexts:pmip6BindingCacheEntry.setStatus(_A)
_Pmip6BindingPBUFlag_Type=TruthValue
_Pmip6BindingPBUFlag_Object=MibTableColumn
pmip6BindingPBUFlag=_Pmip6BindingPBUFlag_Object((1,3,6,1,2,1,206,1,1,2,1,1,1),_Pmip6BindingPBUFlag_Type())
pmip6BindingPBUFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingPBUFlag.setStatus(_A)
_Pmip6BindingMnIndex_Type=Pmip6MnIndex
_Pmip6BindingMnIndex_Object=MibTableColumn
pmip6BindingMnIndex=_Pmip6BindingMnIndex_Object((1,3,6,1,2,1,206,1,1,2,1,1,2),_Pmip6BindingMnIndex_Type())
pmip6BindingMnIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingMnIndex.setStatus(_A)
_Pmip6BindingMnLLIndex_Type=Pmip6MnLLIndex
_Pmip6BindingMnLLIndex_Object=MibTableColumn
pmip6BindingMnLLIndex=_Pmip6BindingMnLLIndex_Object((1,3,6,1,2,1,206,1,1,2,1,1,3),_Pmip6BindingMnLLIndex_Type())
pmip6BindingMnLLIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingMnLLIndex.setStatus(_A)
_Pmip6BindingMagLinkLocalAddressType_Type=InetAddressType
_Pmip6BindingMagLinkLocalAddressType_Object=MibTableColumn
pmip6BindingMagLinkLocalAddressType=_Pmip6BindingMagLinkLocalAddressType_Object((1,3,6,1,2,1,206,1,1,2,1,1,4),_Pmip6BindingMagLinkLocalAddressType_Type())
pmip6BindingMagLinkLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingMagLinkLocalAddressType.setStatus(_A)
_Pmip6BindingMagLinkLocalAddress_Type=InetAddress
_Pmip6BindingMagLinkLocalAddress_Object=MibTableColumn
pmip6BindingMagLinkLocalAddress=_Pmip6BindingMagLinkLocalAddress_Object((1,3,6,1,2,1,206,1,1,2,1,1,5),_Pmip6BindingMagLinkLocalAddress_Type())
pmip6BindingMagLinkLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingMagLinkLocalAddress.setStatus(_A)
_Pmip6BindingTunnelIfIdentifier_Type=Ipv6AddressIfIdentifierTC
_Pmip6BindingTunnelIfIdentifier_Object=MibTableColumn
pmip6BindingTunnelIfIdentifier=_Pmip6BindingTunnelIfIdentifier_Object((1,3,6,1,2,1,206,1,1,2,1,1,6),_Pmip6BindingTunnelIfIdentifier_Type())
pmip6BindingTunnelIfIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingTunnelIfIdentifier.setStatus(_A)
_Pmip6BindingMnInterfaceATT_Type=Pmip6MnInterfaceATT
_Pmip6BindingMnInterfaceATT_Object=MibTableColumn
pmip6BindingMnInterfaceATT=_Pmip6BindingMnInterfaceATT_Object((1,3,6,1,2,1,206,1,1,2,1,1,7),_Pmip6BindingMnInterfaceATT_Type())
pmip6BindingMnInterfaceATT.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingMnInterfaceATT.setStatus(_A)
_Pmip6BindingTimeRecentlyAccepted_Type=Pmip6TimeStamp64
_Pmip6BindingTimeRecentlyAccepted_Object=MibTableColumn
pmip6BindingTimeRecentlyAccepted=_Pmip6BindingTimeRecentlyAccepted_Object((1,3,6,1,2,1,206,1,1,2,1,1,8),_Pmip6BindingTimeRecentlyAccepted_Type())
pmip6BindingTimeRecentlyAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingTimeRecentlyAccepted.setStatus(_A)
_Pmip6Conf_ObjectIdentity=ObjectIdentity
pmip6Conf=_Pmip6Conf_ObjectIdentity((1,3,6,1,2,1,206,1,1,3))
class _Pmip6MobileNodeGeneratedTimestampInUse_Type(TruthValue):defaultValue=2
_Pmip6MobileNodeGeneratedTimestampInUse_Type.__name__=_R
_Pmip6MobileNodeGeneratedTimestampInUse_Object=MibScalar
pmip6MobileNodeGeneratedTimestampInUse=_Pmip6MobileNodeGeneratedTimestampInUse_Object((1,3,6,1,2,1,206,1,1,3,1),_Pmip6MobileNodeGeneratedTimestampInUse_Type())
pmip6MobileNodeGeneratedTimestampInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6MobileNodeGeneratedTimestampInUse.setStatus(_A)
_Pmip6FixedMagLinkLocalAddressOnAllAccessLinksType_Type=InetAddressType
_Pmip6FixedMagLinkLocalAddressOnAllAccessLinksType_Object=MibScalar
pmip6FixedMagLinkLocalAddressOnAllAccessLinksType=_Pmip6FixedMagLinkLocalAddressOnAllAccessLinksType_Object((1,3,6,1,2,1,206,1,1,3,2),_Pmip6FixedMagLinkLocalAddressOnAllAccessLinksType_Type())
pmip6FixedMagLinkLocalAddressOnAllAccessLinksType.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6FixedMagLinkLocalAddressOnAllAccessLinksType.setStatus(_A)
_Pmip6FixedMagLinkLocalAddressOnAllAccessLinks_Type=InetAddress
_Pmip6FixedMagLinkLocalAddressOnAllAccessLinks_Object=MibScalar
pmip6FixedMagLinkLocalAddressOnAllAccessLinks=_Pmip6FixedMagLinkLocalAddressOnAllAccessLinks_Object((1,3,6,1,2,1,206,1,1,3,3),_Pmip6FixedMagLinkLocalAddressOnAllAccessLinks_Type())
pmip6FixedMagLinkLocalAddressOnAllAccessLinks.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6FixedMagLinkLocalAddressOnAllAccessLinks.setStatus(_A)
_Pmip6FixedMagLinkLayerAddressOnAllAccessLinks_Type=PhysAddress
_Pmip6FixedMagLinkLayerAddressOnAllAccessLinks_Object=MibScalar
pmip6FixedMagLinkLayerAddressOnAllAccessLinks=_Pmip6FixedMagLinkLayerAddressOnAllAccessLinks_Object((1,3,6,1,2,1,206,1,1,3,4),_Pmip6FixedMagLinkLayerAddressOnAllAccessLinks_Type())
pmip6FixedMagLinkLayerAddressOnAllAccessLinks.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6FixedMagLinkLayerAddressOnAllAccessLinks.setStatus(_A)
_Pmip6Stats_ObjectIdentity=ObjectIdentity
pmip6Stats=_Pmip6Stats_ObjectIdentity((1,3,6,1,2,1,206,1,1,4))
_Pmip6BindingRegCounters_ObjectIdentity=ObjectIdentity
pmip6BindingRegCounters=_Pmip6BindingRegCounters_ObjectIdentity((1,3,6,1,2,1,206,1,1,4,1))
_Pmip6MissingMnIdentifierOption_Type=Counter32
_Pmip6MissingMnIdentifierOption_Object=MibScalar
pmip6MissingMnIdentifierOption=_Pmip6MissingMnIdentifierOption_Object((1,3,6,1,2,1,206,1,1,4,1,1),_Pmip6MissingMnIdentifierOption_Type())
pmip6MissingMnIdentifierOption.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MissingMnIdentifierOption.setStatus(_A)
_Pmip6MagNotAuthorizedForProxyReg_Type=Counter32
_Pmip6MagNotAuthorizedForProxyReg_Object=MibScalar
pmip6MagNotAuthorizedForProxyReg=_Pmip6MagNotAuthorizedForProxyReg_Object((1,3,6,1,2,1,206,1,1,4,1,2),_Pmip6MagNotAuthorizedForProxyReg_Type())
pmip6MagNotAuthorizedForProxyReg.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagNotAuthorizedForProxyReg.setStatus(_A)
_Pmip6NotLMAForThisMobileNode_Type=Counter32
_Pmip6NotLMAForThisMobileNode_Object=MibScalar
pmip6NotLMAForThisMobileNode=_Pmip6NotLMAForThisMobileNode_Object((1,3,6,1,2,1,206,1,1,4,1,3),_Pmip6NotLMAForThisMobileNode_Type())
pmip6NotLMAForThisMobileNode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6NotLMAForThisMobileNode.setStatus(_A)
_Pmip6ProxyRegNotEnabled_Type=Counter32
_Pmip6ProxyRegNotEnabled_Object=MibScalar
pmip6ProxyRegNotEnabled=_Pmip6ProxyRegNotEnabled_Object((1,3,6,1,2,1,206,1,1,4,1,4),_Pmip6ProxyRegNotEnabled_Type())
pmip6ProxyRegNotEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6ProxyRegNotEnabled.setStatus(_A)
_Pmip6MissingHomeNetworkPrefixOption_Type=Counter32
_Pmip6MissingHomeNetworkPrefixOption_Object=MibScalar
pmip6MissingHomeNetworkPrefixOption=_Pmip6MissingHomeNetworkPrefixOption_Object((1,3,6,1,2,1,206,1,1,4,1,5),_Pmip6MissingHomeNetworkPrefixOption_Type())
pmip6MissingHomeNetworkPrefixOption.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MissingHomeNetworkPrefixOption.setStatus(_A)
_Pmip6MissingHandOffIndicatorOption_Type=Counter32
_Pmip6MissingHandOffIndicatorOption_Object=MibScalar
pmip6MissingHandOffIndicatorOption=_Pmip6MissingHandOffIndicatorOption_Object((1,3,6,1,2,1,206,1,1,4,1,6),_Pmip6MissingHandOffIndicatorOption_Type())
pmip6MissingHandOffIndicatorOption.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MissingHandOffIndicatorOption.setStatus(_A)
_Pmip6MissingAccessTechTypeOption_Type=Counter32
_Pmip6MissingAccessTechTypeOption_Object=MibScalar
pmip6MissingAccessTechTypeOption=_Pmip6MissingAccessTechTypeOption_Object((1,3,6,1,2,1,206,1,1,4,1,7),_Pmip6MissingAccessTechTypeOption_Type())
pmip6MissingAccessTechTypeOption.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MissingAccessTechTypeOption.setStatus(_A)
_Pmip6NotAuthorizedForHomeNetworkPrefix_Type=Counter32
_Pmip6NotAuthorizedForHomeNetworkPrefix_Object=MibScalar
pmip6NotAuthorizedForHomeNetworkPrefix=_Pmip6NotAuthorizedForHomeNetworkPrefix_Object((1,3,6,1,2,1,206,1,1,4,1,8),_Pmip6NotAuthorizedForHomeNetworkPrefix_Type())
pmip6NotAuthorizedForHomeNetworkPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6NotAuthorizedForHomeNetworkPrefix.setStatus(_A)
_Pmip6TimestampMismatch_Type=Counter32
_Pmip6TimestampMismatch_Object=MibScalar
pmip6TimestampMismatch=_Pmip6TimestampMismatch_Object((1,3,6,1,2,1,206,1,1,4,1,9),_Pmip6TimestampMismatch_Type())
pmip6TimestampMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6TimestampMismatch.setStatus(_A)
_Pmip6TimestampLowerThanPrevAccepted_Type=Counter32
_Pmip6TimestampLowerThanPrevAccepted_Object=MibScalar
pmip6TimestampLowerThanPrevAccepted=_Pmip6TimestampLowerThanPrevAccepted_Object((1,3,6,1,2,1,206,1,1,4,1,10),_Pmip6TimestampLowerThanPrevAccepted_Type())
pmip6TimestampLowerThanPrevAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6TimestampLowerThanPrevAccepted.setStatus(_A)
_Pmip6BcePbuPrefixSetDoNotMatch_Type=Counter32
_Pmip6BcePbuPrefixSetDoNotMatch_Object=MibScalar
pmip6BcePbuPrefixSetDoNotMatch=_Pmip6BcePbuPrefixSetDoNotMatch_Object((1,3,6,1,2,1,206,1,1,4,1,11),_Pmip6BcePbuPrefixSetDoNotMatch_Type())
pmip6BcePbuPrefixSetDoNotMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BcePbuPrefixSetDoNotMatch.setStatus(_A)
_Pmip6InitialBindingRegistrations_Type=Counter32
_Pmip6InitialBindingRegistrations_Object=MibScalar
pmip6InitialBindingRegistrations=_Pmip6InitialBindingRegistrations_Object((1,3,6,1,2,1,206,1,1,4,1,12),_Pmip6InitialBindingRegistrations_Type())
pmip6InitialBindingRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6InitialBindingRegistrations.setStatus(_A)
_Pmip6BindingLifeTimeExtensionNoHandOff_Type=Counter32
_Pmip6BindingLifeTimeExtensionNoHandOff_Object=MibScalar
pmip6BindingLifeTimeExtensionNoHandOff=_Pmip6BindingLifeTimeExtensionNoHandOff_Object((1,3,6,1,2,1,206,1,1,4,1,13),_Pmip6BindingLifeTimeExtensionNoHandOff_Type())
pmip6BindingLifeTimeExtensionNoHandOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingLifeTimeExtensionNoHandOff.setStatus(_A)
_Pmip6BindingLifeTimeExtensionAfterHandOff_Type=Counter32
_Pmip6BindingLifeTimeExtensionAfterHandOff_Object=MibScalar
pmip6BindingLifeTimeExtensionAfterHandOff=_Pmip6BindingLifeTimeExtensionAfterHandOff_Object((1,3,6,1,2,1,206,1,1,4,1,14),_Pmip6BindingLifeTimeExtensionAfterHandOff_Type())
pmip6BindingLifeTimeExtensionAfterHandOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingLifeTimeExtensionAfterHandOff.setStatus(_A)
_Pmip6BindingDeRegistrations_Type=Counter32
_Pmip6BindingDeRegistrations_Object=MibScalar
pmip6BindingDeRegistrations=_Pmip6BindingDeRegistrations_Object((1,3,6,1,2,1,206,1,1,4,1,15),_Pmip6BindingDeRegistrations_Type())
pmip6BindingDeRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingDeRegistrations.setStatus(_A)
_Pmip6BindingBindingAcks_Type=Counter32
_Pmip6BindingBindingAcks_Object=MibScalar
pmip6BindingBindingAcks=_Pmip6BindingBindingAcks_Object((1,3,6,1,2,1,206,1,1,4,1,16),_Pmip6BindingBindingAcks_Type())
pmip6BindingBindingAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6BindingBindingAcks.setStatus(_A)
_Pmip6CounterDiscontinuityTime_Type=TimeStamp
_Pmip6CounterDiscontinuityTime_Object=MibScalar
pmip6CounterDiscontinuityTime=_Pmip6CounterDiscontinuityTime_Object((1,3,6,1,2,1,206,1,1,4,1,17),_Pmip6CounterDiscontinuityTime_Type())
pmip6CounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6CounterDiscontinuityTime.setStatus(_A)
_Pmip6Mag_ObjectIdentity=ObjectIdentity
pmip6Mag=_Pmip6Mag_ObjectIdentity((1,3,6,1,2,1,206,1,2))
_Pmip6MagSystem_ObjectIdentity=ObjectIdentity
pmip6MagSystem=_Pmip6MagSystem_ObjectIdentity((1,3,6,1,2,1,206,1,2,1))
class _Pmip6MagStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_Pmip6MagStatus_Type.__name__=_F
_Pmip6MagStatus_Object=MibScalar
pmip6MagStatus=_Pmip6MagStatus_Object((1,3,6,1,2,1,206,1,2,1,1),_Pmip6MagStatus_Type())
pmip6MagStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6MagStatus.setStatus(_A)
_Pmip6MagProxyCOATable_Object=MibTable
pmip6MagProxyCOATable=_Pmip6MagProxyCOATable_Object((1,3,6,1,2,1,206,1,2,1,2))
if mibBuilder.loadTexts:pmip6MagProxyCOATable.setStatus(_A)
_Pmip6MagProxyCOAEntry_Object=MibTableRow
pmip6MagProxyCOAEntry=_Pmip6MagProxyCOAEntry_Object((1,3,6,1,2,1,206,1,2,1,2,1))
pmip6MagProxyCOAEntry.setIndexNames((0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:pmip6MagProxyCOAEntry.setStatus(_A)
_Pmip6MagProxyCOAType_Type=InetAddressType
_Pmip6MagProxyCOAType_Object=MibTableColumn
pmip6MagProxyCOAType=_Pmip6MagProxyCOAType_Object((1,3,6,1,2,1,206,1,2,1,2,1,1),_Pmip6MagProxyCOAType_Type())
pmip6MagProxyCOAType.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6MagProxyCOAType.setStatus(_A)
_Pmip6MagProxyCOA_Type=InetAddress
_Pmip6MagProxyCOA_Object=MibTableColumn
pmip6MagProxyCOA=_Pmip6MagProxyCOA_Object((1,3,6,1,2,1,206,1,2,1,2,1,2),_Pmip6MagProxyCOA_Type())
pmip6MagProxyCOA.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6MagProxyCOA.setStatus(_A)
class _Pmip6MagProxyCOAState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3)))
_Pmip6MagProxyCOAState_Type.__name__=_F
_Pmip6MagProxyCOAState_Object=MibTableColumn
pmip6MagProxyCOAState=_Pmip6MagProxyCOAState_Object((1,3,6,1,2,1,206,1,2,1,2,1,3),_Pmip6MagProxyCOAState_Type())
pmip6MagProxyCOAState.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagProxyCOAState.setStatus(_A)
_Pmip6MagConf_ObjectIdentity=ObjectIdentity
pmip6MagConf=_Pmip6MagConf_ObjectIdentity((1,3,6,1,2,1,206,1,2,2))
class _Pmip6MagEnableMagLocalRouting_Type(TruthValue):defaultValue=2
_Pmip6MagEnableMagLocalRouting_Type.__name__=_R
_Pmip6MagEnableMagLocalRouting_Object=MibScalar
pmip6MagEnableMagLocalRouting=_Pmip6MagEnableMagLocalRouting_Object((1,3,6,1,2,1,206,1,2,2,1),_Pmip6MagEnableMagLocalRouting_Type())
pmip6MagEnableMagLocalRouting.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6MagEnableMagLocalRouting.setStatus(_A)
_Pmip6MagMnIdentifierTable_Object=MibTable
pmip6MagMnIdentifierTable=_Pmip6MagMnIdentifierTable_Object((1,3,6,1,2,1,206,1,2,2,2))
if mibBuilder.loadTexts:pmip6MagMnIdentifierTable.setStatus(_A)
_Pmip6MagMnIdentifierEntry_Object=MibTableRow
pmip6MagMnIdentifierEntry=_Pmip6MagMnIdentifierEntry_Object((1,3,6,1,2,1,206,1,2,2,2,1))
pmip6MagMnIdentifierEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:pmip6MagMnIdentifierEntry.setStatus(_A)
_Pmip6MagMnIdentifier_Type=Pmip6MnIdentifier
_Pmip6MagMnIdentifier_Object=MibTableColumn
pmip6MagMnIdentifier=_Pmip6MagMnIdentifier_Object((1,3,6,1,2,1,206,1,2,2,2,1,1),_Pmip6MagMnIdentifier_Type())
pmip6MagMnIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagMnIdentifier.setStatus(_A)
_Pmip6MagMnLLIdentifierTable_Object=MibTable
pmip6MagMnLLIdentifierTable=_Pmip6MagMnLLIdentifierTable_Object((1,3,6,1,2,1,206,1,2,2,3))
if mibBuilder.loadTexts:pmip6MagMnLLIdentifierTable.setStatus(_A)
_Pmip6MagMnLLIdentifierEntry_Object=MibTableRow
pmip6MagMnLLIdentifierEntry=_Pmip6MagMnLLIdentifierEntry_Object((1,3,6,1,2,1,206,1,2,2,3,1))
pmip6MagMnLLIdentifierEntry.setIndexNames((0,_B,_G),(0,_B,_L))
if mibBuilder.loadTexts:pmip6MagMnLLIdentifierEntry.setStatus(_A)
_Pmip6MagMnLLIdentifier_Type=Pmip6MnLLIdentifier
_Pmip6MagMnLLIdentifier_Object=MibTableColumn
pmip6MagMnLLIdentifier=_Pmip6MagMnLLIdentifier_Object((1,3,6,1,2,1,206,1,2,2,3,1,1),_Pmip6MagMnLLIdentifier_Type())
pmip6MagMnLLIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagMnLLIdentifier.setStatus(_A)
_Pmip6MagHomeNetworkPrefixTable_Object=MibTable
pmip6MagHomeNetworkPrefixTable=_Pmip6MagHomeNetworkPrefixTable_Object((1,3,6,1,2,1,206,1,2,2,4))
if mibBuilder.loadTexts:pmip6MagHomeNetworkPrefixTable.setStatus(_A)
_Pmip6MagHomeNetworkPrefixEntry_Object=MibTableRow
pmip6MagHomeNetworkPrefixEntry=_Pmip6MagHomeNetworkPrefixEntry_Object((1,3,6,1,2,1,206,1,2,2,4,1))
pmip6MagHomeNetworkPrefixEntry.setIndexNames((0,_B,_G),(0,_B,_L),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:pmip6MagHomeNetworkPrefixEntry.setStatus(_A)
_Pmip6MagHomeNetworkPrefixType_Type=InetAddressType
_Pmip6MagHomeNetworkPrefixType_Object=MibTableColumn
pmip6MagHomeNetworkPrefixType=_Pmip6MagHomeNetworkPrefixType_Object((1,3,6,1,2,1,206,1,2,2,4,1,1),_Pmip6MagHomeNetworkPrefixType_Type())
pmip6MagHomeNetworkPrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6MagHomeNetworkPrefixType.setStatus(_A)
_Pmip6MagHomeNetworkPrefix_Type=InetAddress
_Pmip6MagHomeNetworkPrefix_Object=MibTableColumn
pmip6MagHomeNetworkPrefix=_Pmip6MagHomeNetworkPrefix_Object((1,3,6,1,2,1,206,1,2,2,4,1,2),_Pmip6MagHomeNetworkPrefix_Type())
pmip6MagHomeNetworkPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6MagHomeNetworkPrefix.setStatus(_A)
_Pmip6MagHomeNetworkPrefixLength_Type=InetAddressPrefixLength
_Pmip6MagHomeNetworkPrefixLength_Object=MibTableColumn
pmip6MagHomeNetworkPrefixLength=_Pmip6MagHomeNetworkPrefixLength_Object((1,3,6,1,2,1,206,1,2,2,4,1,3),_Pmip6MagHomeNetworkPrefixLength_Type())
pmip6MagHomeNetworkPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagHomeNetworkPrefixLength.setStatus(_A)
_Pmip6MagHomeNetworkPrefixLifeTime_Type=Unsigned32
_Pmip6MagHomeNetworkPrefixLifeTime_Object=MibTableColumn
pmip6MagHomeNetworkPrefixLifeTime=_Pmip6MagHomeNetworkPrefixLifeTime_Object((1,3,6,1,2,1,206,1,2,2,4,1,4),_Pmip6MagHomeNetworkPrefixLifeTime_Type())
pmip6MagHomeNetworkPrefixLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagHomeNetworkPrefixLifeTime.setStatus(_A)
if mibBuilder.loadTexts:pmip6MagHomeNetworkPrefixLifeTime.setUnits(_h)
_Pmip6MagRegistration_ObjectIdentity=ObjectIdentity
pmip6MagRegistration=_Pmip6MagRegistration_ObjectIdentity((1,3,6,1,2,1,206,1,2,3))
_Pmip6MagBLTable_Object=MibTable
pmip6MagBLTable=_Pmip6MagBLTable_Object((1,3,6,1,2,1,206,1,2,3,1))
if mibBuilder.loadTexts:pmip6MagBLTable.setStatus(_A)
_Pmip6MagBLEntry_Object=MibTableRow
pmip6MagBLEntry=_Pmip6MagBLEntry_Object((1,3,6,1,2,1,206,1,2,3,1,1))
if mibBuilder.loadTexts:pmip6MagBLEntry.setStatus(_A)
_Pmip6MagBLFlag_Type=TruthValue
_Pmip6MagBLFlag_Object=MibTableColumn
pmip6MagBLFlag=_Pmip6MagBLFlag_Object((1,3,6,1,2,1,206,1,2,3,1,1,1),_Pmip6MagBLFlag_Type())
pmip6MagBLFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLFlag.setStatus(_A)
_Pmip6MagBLMnIndex_Type=Pmip6MnIndex
_Pmip6MagBLMnIndex_Object=MibTableColumn
pmip6MagBLMnIndex=_Pmip6MagBLMnIndex_Object((1,3,6,1,2,1,206,1,2,3,1,1,2),_Pmip6MagBLMnIndex_Type())
pmip6MagBLMnIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLMnIndex.setStatus(_A)
_Pmip6MagBLMnLLIndex_Type=Pmip6MnLLIndex
_Pmip6MagBLMnLLIndex_Object=MibTableColumn
pmip6MagBLMnLLIndex=_Pmip6MagBLMnLLIndex_Object((1,3,6,1,2,1,206,1,2,3,1,1,3),_Pmip6MagBLMnLLIndex_Type())
pmip6MagBLMnLLIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLMnLLIndex.setStatus(_A)
_Pmip6MagBLMagLinkLocalAddressType_Type=InetAddressType
_Pmip6MagBLMagLinkLocalAddressType_Object=MibTableColumn
pmip6MagBLMagLinkLocalAddressType=_Pmip6MagBLMagLinkLocalAddressType_Object((1,3,6,1,2,1,206,1,2,3,1,1,4),_Pmip6MagBLMagLinkLocalAddressType_Type())
pmip6MagBLMagLinkLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLMagLinkLocalAddressType.setStatus(_A)
_Pmip6MagBLMagLinkLocalAddress_Type=InetAddress
_Pmip6MagBLMagLinkLocalAddress_Object=MibTableColumn
pmip6MagBLMagLinkLocalAddress=_Pmip6MagBLMagLinkLocalAddress_Object((1,3,6,1,2,1,206,1,2,3,1,1,5),_Pmip6MagBLMagLinkLocalAddress_Type())
pmip6MagBLMagLinkLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLMagLinkLocalAddress.setStatus(_A)
_Pmip6MagBLMagIfIdentifierToMn_Type=Ipv6AddressIfIdentifierTC
_Pmip6MagBLMagIfIdentifierToMn_Object=MibTableColumn
pmip6MagBLMagIfIdentifierToMn=_Pmip6MagBLMagIfIdentifierToMn_Object((1,3,6,1,2,1,206,1,2,3,1,1,6),_Pmip6MagBLMagIfIdentifierToMn_Type())
pmip6MagBLMagIfIdentifierToMn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLMagIfIdentifierToMn.setStatus(_A)
_Pmip6MagBLTunnelIfIdentifier_Type=Ipv6AddressIfIdentifierTC
_Pmip6MagBLTunnelIfIdentifier_Object=MibTableColumn
pmip6MagBLTunnelIfIdentifier=_Pmip6MagBLTunnelIfIdentifier_Object((1,3,6,1,2,1,206,1,2,3,1,1,7),_Pmip6MagBLTunnelIfIdentifier_Type())
pmip6MagBLTunnelIfIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLTunnelIfIdentifier.setStatus(_A)
_Pmip6MagBLMnInterfaceATT_Type=Pmip6MnInterfaceATT
_Pmip6MagBLMnInterfaceATT_Object=MibTableColumn
pmip6MagBLMnInterfaceATT=_Pmip6MagBLMnInterfaceATT_Object((1,3,6,1,2,1,206,1,2,3,1,1,8),_Pmip6MagBLMnInterfaceATT_Type())
pmip6MagBLMnInterfaceATT.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLMnInterfaceATT.setStatus(_A)
_Pmip6MagBLTimeRecentlyAccepted_Type=Pmip6TimeStamp64
_Pmip6MagBLTimeRecentlyAccepted_Object=MibTableColumn
pmip6MagBLTimeRecentlyAccepted=_Pmip6MagBLTimeRecentlyAccepted_Object((1,3,6,1,2,1,206,1,2,3,1,1,9),_Pmip6MagBLTimeRecentlyAccepted_Type())
pmip6MagBLTimeRecentlyAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagBLTimeRecentlyAccepted.setStatus(_A)
_Pmip6MagMnProfileTable_Object=MibTable
pmip6MagMnProfileTable=_Pmip6MagMnProfileTable_Object((1,3,6,1,2,1,206,1,2,3,2))
if mibBuilder.loadTexts:pmip6MagMnProfileTable.setStatus(_A)
_Pmip6MagMnProfileEntry_Object=MibTableRow
pmip6MagMnProfileEntry=_Pmip6MagMnProfileEntry_Object((1,3,6,1,2,1,206,1,2,3,2,1))
pmip6MagMnProfileEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:pmip6MagMnProfileEntry.setStatus(_A)
_Pmip6MagProfMnIndex_Type=Pmip6MnIndex
_Pmip6MagProfMnIndex_Object=MibTableColumn
pmip6MagProfMnIndex=_Pmip6MagProfMnIndex_Object((1,3,6,1,2,1,206,1,2,3,2,1,1),_Pmip6MagProfMnIndex_Type())
pmip6MagProfMnIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6MagProfMnIndex.setStatus(_A)
_Pmip6MagProfMnIdentifier_Type=Pmip6MnIdentifier
_Pmip6MagProfMnIdentifier_Object=MibTableColumn
pmip6MagProfMnIdentifier=_Pmip6MagProfMnIdentifier_Object((1,3,6,1,2,1,206,1,2,3,2,1,2),_Pmip6MagProfMnIdentifier_Type())
pmip6MagProfMnIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagProfMnIdentifier.setStatus(_A)
_Pmip6MagProfMnLocalMobilityAnchorAddressType_Type=InetAddressType
_Pmip6MagProfMnLocalMobilityAnchorAddressType_Object=MibTableColumn
pmip6MagProfMnLocalMobilityAnchorAddressType=_Pmip6MagProfMnLocalMobilityAnchorAddressType_Object((1,3,6,1,2,1,206,1,2,3,2,1,3),_Pmip6MagProfMnLocalMobilityAnchorAddressType_Type())
pmip6MagProfMnLocalMobilityAnchorAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagProfMnLocalMobilityAnchorAddressType.setStatus(_A)
_Pmip6MagProfMnLocalMobilityAnchorAddress_Type=InetAddress
_Pmip6MagProfMnLocalMobilityAnchorAddress_Object=MibTableColumn
pmip6MagProfMnLocalMobilityAnchorAddress=_Pmip6MagProfMnLocalMobilityAnchorAddress_Object((1,3,6,1,2,1,206,1,2,3,2,1,4),_Pmip6MagProfMnLocalMobilityAnchorAddress_Type())
pmip6MagProfMnLocalMobilityAnchorAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6MagProfMnLocalMobilityAnchorAddress.setStatus(_A)
_Pmip6Lma_ObjectIdentity=ObjectIdentity
pmip6Lma=_Pmip6Lma_ObjectIdentity((1,3,6,1,2,1,206,1,3))
_Pmip6LmaSystem_ObjectIdentity=ObjectIdentity
pmip6LmaSystem=_Pmip6LmaSystem_ObjectIdentity((1,3,6,1,2,1,206,1,3,1))
class _Pmip6LmaStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_Pmip6LmaStatus_Type.__name__=_F
_Pmip6LmaStatus_Object=MibScalar
pmip6LmaStatus=_Pmip6LmaStatus_Object((1,3,6,1,2,1,206,1,3,1,1),_Pmip6LmaStatus_Type())
pmip6LmaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6LmaStatus.setStatus(_A)
_Pmip6LmaLMAATable_Object=MibTable
pmip6LmaLMAATable=_Pmip6LmaLMAATable_Object((1,3,6,1,2,1,206,1,3,1,2))
if mibBuilder.loadTexts:pmip6LmaLMAATable.setStatus(_A)
_Pmip6LmaLMAAEntry_Object=MibTableRow
pmip6LmaLMAAEntry=_Pmip6LmaLMAAEntry_Object((1,3,6,1,2,1,206,1,3,1,2,1))
pmip6LmaLMAAEntry.setIndexNames((0,_B,_j),(0,_B,_k))
if mibBuilder.loadTexts:pmip6LmaLMAAEntry.setStatus(_A)
_Pmip6LmaLMAAType_Type=InetAddressType
_Pmip6LmaLMAAType_Object=MibTableColumn
pmip6LmaLMAAType=_Pmip6LmaLMAAType_Object((1,3,6,1,2,1,206,1,3,1,2,1,1),_Pmip6LmaLMAAType_Type())
pmip6LmaLMAAType.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6LmaLMAAType.setStatus(_A)
_Pmip6LmaLMAA_Type=InetAddress
_Pmip6LmaLMAA_Object=MibTableColumn
pmip6LmaLMAA=_Pmip6LmaLMAA_Object((1,3,6,1,2,1,206,1,3,1,2,1,2),_Pmip6LmaLMAA_Type())
pmip6LmaLMAA.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6LmaLMAA.setStatus(_A)
class _Pmip6LmaLMAAState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3)))
_Pmip6LmaLMAAState_Type.__name__=_F
_Pmip6LmaLMAAState_Object=MibTableColumn
pmip6LmaLMAAState=_Pmip6LmaLMAAState_Object((1,3,6,1,2,1,206,1,3,1,2,1,3),_Pmip6LmaLMAAState_Type())
pmip6LmaLMAAState.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6LmaLMAAState.setStatus(_A)
_Pmip6LmaConf_ObjectIdentity=ObjectIdentity
pmip6LmaConf=_Pmip6LmaConf_ObjectIdentity((1,3,6,1,2,1,206,1,3,2))
class _Pmip6LmaMinDelayBeforeBCEDelete_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Pmip6LmaMinDelayBeforeBCEDelete_Type.__name__=_F
_Pmip6LmaMinDelayBeforeBCEDelete_Object=MibScalar
pmip6LmaMinDelayBeforeBCEDelete=_Pmip6LmaMinDelayBeforeBCEDelete_Object((1,3,6,1,2,1,206,1,3,2,1),_Pmip6LmaMinDelayBeforeBCEDelete_Type())
pmip6LmaMinDelayBeforeBCEDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6LmaMinDelayBeforeBCEDelete.setStatus(_A)
if mibBuilder.loadTexts:pmip6LmaMinDelayBeforeBCEDelete.setUnits(_S)
class _Pmip6LmaMaxDelayBeforeNewBCEAssign_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Pmip6LmaMaxDelayBeforeNewBCEAssign_Type.__name__=_F
_Pmip6LmaMaxDelayBeforeNewBCEAssign_Object=MibScalar
pmip6LmaMaxDelayBeforeNewBCEAssign=_Pmip6LmaMaxDelayBeforeNewBCEAssign_Object((1,3,6,1,2,1,206,1,3,2,2),_Pmip6LmaMaxDelayBeforeNewBCEAssign_Type())
pmip6LmaMaxDelayBeforeNewBCEAssign.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6LmaMaxDelayBeforeNewBCEAssign.setStatus(_A)
if mibBuilder.loadTexts:pmip6LmaMaxDelayBeforeNewBCEAssign.setUnits(_S)
class _Pmip6LmaTimestampValidityWindow_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Pmip6LmaTimestampValidityWindow_Type.__name__=_F
_Pmip6LmaTimestampValidityWindow_Object=MibScalar
pmip6LmaTimestampValidityWindow=_Pmip6LmaTimestampValidityWindow_Object((1,3,6,1,2,1,206,1,3,2,3),_Pmip6LmaTimestampValidityWindow_Type())
pmip6LmaTimestampValidityWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6LmaTimestampValidityWindow.setStatus(_A)
if mibBuilder.loadTexts:pmip6LmaTimestampValidityWindow.setUnits(_S)
_Pmip6LmaMnIdentifierTable_Object=MibTable
pmip6LmaMnIdentifierTable=_Pmip6LmaMnIdentifierTable_Object((1,3,6,1,2,1,206,1,3,2,4))
if mibBuilder.loadTexts:pmip6LmaMnIdentifierTable.setStatus(_A)
_Pmip6LmaMnIdentifierEntry_Object=MibTableRow
pmip6LmaMnIdentifierEntry=_Pmip6LmaMnIdentifierEntry_Object((1,3,6,1,2,1,206,1,3,2,4,1))
pmip6LmaMnIdentifierEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:pmip6LmaMnIdentifierEntry.setStatus(_A)
_Pmip6LmaMnIdentifier_Type=Pmip6MnIdentifier
_Pmip6LmaMnIdentifier_Object=MibTableColumn
pmip6LmaMnIdentifier=_Pmip6LmaMnIdentifier_Object((1,3,6,1,2,1,206,1,3,2,4,1,1),_Pmip6LmaMnIdentifier_Type())
pmip6LmaMnIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6LmaMnIdentifier.setStatus(_A)
_Pmip6LmaMnLLIdentifierTable_Object=MibTable
pmip6LmaMnLLIdentifierTable=_Pmip6LmaMnLLIdentifierTable_Object((1,3,6,1,2,1,206,1,3,2,5))
if mibBuilder.loadTexts:pmip6LmaMnLLIdentifierTable.setStatus(_A)
_Pmip6LmaMnLLIdentifierEntry_Object=MibTableRow
pmip6LmaMnLLIdentifierEntry=_Pmip6LmaMnLLIdentifierEntry_Object((1,3,6,1,2,1,206,1,3,2,5,1))
pmip6LmaMnLLIdentifierEntry.setIndexNames((0,_B,_H),(0,_B,_M))
if mibBuilder.loadTexts:pmip6LmaMnLLIdentifierEntry.setStatus(_A)
_Pmip6LmaMnLLIdentifier_Type=Pmip6MnLLIdentifier
_Pmip6LmaMnLLIdentifier_Object=MibTableColumn
pmip6LmaMnLLIdentifier=_Pmip6LmaMnLLIdentifier_Object((1,3,6,1,2,1,206,1,3,2,5,1,1),_Pmip6LmaMnLLIdentifier_Type())
pmip6LmaMnLLIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6LmaMnLLIdentifier.setStatus(_A)
_Pmip6LmaHomeNetworkPrefixTable_Object=MibTable
pmip6LmaHomeNetworkPrefixTable=_Pmip6LmaHomeNetworkPrefixTable_Object((1,3,6,1,2,1,206,1,3,2,6))
if mibBuilder.loadTexts:pmip6LmaHomeNetworkPrefixTable.setStatus(_A)
_Pmip6LmaHomeNetworkPrefixEntry_Object=MibTableRow
pmip6LmaHomeNetworkPrefixEntry=_Pmip6LmaHomeNetworkPrefixEntry_Object((1,3,6,1,2,1,206,1,3,2,6,1))
pmip6LmaHomeNetworkPrefixEntry.setIndexNames((0,_B,_H),(0,_B,_M),(0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:pmip6LmaHomeNetworkPrefixEntry.setStatus(_A)
_Pmip6LmaHomeNetworkPrefixType_Type=InetAddressType
_Pmip6LmaHomeNetworkPrefixType_Object=MibTableColumn
pmip6LmaHomeNetworkPrefixType=_Pmip6LmaHomeNetworkPrefixType_Object((1,3,6,1,2,1,206,1,3,2,6,1,1),_Pmip6LmaHomeNetworkPrefixType_Type())
pmip6LmaHomeNetworkPrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6LmaHomeNetworkPrefixType.setStatus(_A)
_Pmip6LmaHomeNetworkPrefix_Type=InetAddress
_Pmip6LmaHomeNetworkPrefix_Object=MibTableColumn
pmip6LmaHomeNetworkPrefix=_Pmip6LmaHomeNetworkPrefix_Object((1,3,6,1,2,1,206,1,3,2,6,1,2),_Pmip6LmaHomeNetworkPrefix_Type())
pmip6LmaHomeNetworkPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:pmip6LmaHomeNetworkPrefix.setStatus(_A)
_Pmip6LmaHomeNetworkPrefixLength_Type=InetAddressPrefixLength
_Pmip6LmaHomeNetworkPrefixLength_Object=MibTableColumn
pmip6LmaHomeNetworkPrefixLength=_Pmip6LmaHomeNetworkPrefixLength_Object((1,3,6,1,2,1,206,1,3,2,6,1,3),_Pmip6LmaHomeNetworkPrefixLength_Type())
pmip6LmaHomeNetworkPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:pmip6LmaHomeNetworkPrefixLength.setStatus(_A)
_Pmip6LmaHomeNetworkPrefixLifeTime_Type=Gauge32
_Pmip6LmaHomeNetworkPrefixLifeTime_Object=MibTableColumn
pmip6LmaHomeNetworkPrefixLifeTime=_Pmip6LmaHomeNetworkPrefixLifeTime_Object((1,3,6,1,2,1,206,1,3,2,6,1,4),_Pmip6LmaHomeNetworkPrefixLifeTime_Type())
pmip6LmaHomeNetworkPrefixLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pmip6LmaHomeNetworkPrefixLifeTime.setStatus(_A)
if mibBuilder.loadTexts:pmip6LmaHomeNetworkPrefixLifeTime.setUnits(_h)
_Pmip6Conformance_ObjectIdentity=ObjectIdentity
pmip6Conformance=_Pmip6Conformance_ObjectIdentity((1,3,6,1,2,1,206,2))
_Pmip6Groups_ObjectIdentity=ObjectIdentity
pmip6Groups=_Pmip6Groups_ObjectIdentity((1,3,6,1,2,1,206,2,1))
_Pmip6Compliances_ObjectIdentity=ObjectIdentity
pmip6Compliances=_Pmip6Compliances_ObjectIdentity((1,3,6,1,2,1,206,2,2))
mip6BindingCacheEntry.registerAugmentions((_B,_n))
pmip6BindingCacheEntry.setIndexNames(*mip6BindingCacheEntry.getIndexNames())
mip6MnBLEntry.registerAugmentions((_B,_o))
pmip6MagBLEntry.setIndexNames(*mip6MnBLEntry.getIndexNames())
pmip6SystemGroup=ObjectGroup((1,3,6,1,2,1,206,2,1,1))
pmip6SystemGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:pmip6SystemGroup.setStatus(_A)
pmip6BindingCacheGroup=ObjectGroup((1,3,6,1,2,1,206,2,1,2))
pmip6BindingCacheGroup.setObjects(*((_B,_u),(_B,_H),(_B,_M),(_B,_v),(_B,_w),(_B,_N),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:pmip6BindingCacheGroup.setStatus(_A)
pmip6StatsGroup=ObjectGroup((1,3,6,1,2,1,206,2,1,3))
pmip6StatsGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:pmip6StatsGroup.setStatus(_A)
pmip6MagSystemGroup=ObjectGroup((1,3,6,1,2,1,206,2,1,4))
pmip6MagSystemGroup.setObjects(*((_B,_AI),(_B,_O)))
if mibBuilder.loadTexts:pmip6MagSystemGroup.setStatus(_A)
pmip6MagConfigurationGroup=ObjectGroup((1,3,6,1,2,1,206,2,1,5))
pmip6MagConfigurationGroup.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:pmip6MagConfigurationGroup.setStatus(_A)
pmip6MagRegistrationGroup=ObjectGroup((1,3,6,1,2,1,206,2,1,6))
pmip6MagRegistrationGroup.setObjects(*((_B,_AM),(_B,_G),(_B,_L),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_P),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:pmip6MagRegistrationGroup.setStatus(_A)
pmip6LmaSystemGroup=ObjectGroup((1,3,6,1,2,1,206,2,1,7))
pmip6LmaSystemGroup.setObjects(*((_B,_AX),(_B,_Q)))
if mibBuilder.loadTexts:pmip6LmaSystemGroup.setStatus(_A)
pmip6LmaConfigurationGroup=ObjectGroup((1,3,6,1,2,1,206,2,1,8))
pmip6LmaConfigurationGroup.setObjects(*((_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:pmip6LmaConfigurationGroup.setStatus(_A)
pmip6MagHomeTunnelEstablished=NotificationType((1,3,6,1,2,1,206,0,1))
pmip6MagHomeTunnelEstablished.setObjects(*((_B,_P),(_B,_O)))
if mibBuilder.loadTexts:pmip6MagHomeTunnelEstablished.setStatus(_A)
pmip6MagHomeTunnelReleased=NotificationType((1,3,6,1,2,1,206,0,2))
pmip6MagHomeTunnelReleased.setObjects(*((_B,_P),(_B,_O)))
if mibBuilder.loadTexts:pmip6MagHomeTunnelReleased.setStatus(_A)
pmip6LmaHomeTunnelEstablished=NotificationType((1,3,6,1,2,1,206,0,3))
pmip6LmaHomeTunnelEstablished.setObjects(*((_B,_N),(_B,_Q)))
if mibBuilder.loadTexts:pmip6LmaHomeTunnelEstablished.setStatus(_A)
pmip6LmaHomeTunnelReleased=NotificationType((1,3,6,1,2,1,206,0,4))
pmip6LmaHomeTunnelReleased.setObjects(*((_B,_N),(_B,_Q)))
if mibBuilder.loadTexts:pmip6LmaHomeTunnelReleased.setStatus(_A)
pmip6MagNotificationGroup=NotificationGroup((1,3,6,1,2,1,206,2,1,9))
pmip6MagNotificationGroup.setObjects(*((_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:pmip6MagNotificationGroup.setStatus(_A)
pmip6LmaNotificationGroup=NotificationGroup((1,3,6,1,2,1,206,2,1,10))
pmip6LmaNotificationGroup.setObjects(*((_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:pmip6LmaNotificationGroup.setStatus(_A)
pmip6CoreCompliance=ModuleCompliance((1,3,6,1,2,1,206,2,2,1))
pmip6CoreCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:pmip6CoreCompliance.setStatus(_A)
pmip6Compliance2=ModuleCompliance((1,3,6,1,2,1,206,2,2,2))
pmip6Compliance2.setObjects(*((_B,_I),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:pmip6Compliance2.setStatus(_A)
pmip6CoreReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,206,2,2,3))
pmip6CoreReadOnlyCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:pmip6CoreReadOnlyCompliance.setStatus(_A)
pmip6ReadOnlyCompliance2=ModuleCompliance((1,3,6,1,2,1,206,2,2,4))
pmip6ReadOnlyCompliance2.setObjects(*((_B,_I),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:pmip6ReadOnlyCompliance2.setStatus(_A)
pmip6MagCoreCompliance=ModuleCompliance((1,3,6,1,2,1,206,2,2,5))
pmip6MagCoreCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:pmip6MagCoreCompliance.setStatus(_A)
pmip6MagCompliance2=ModuleCompliance((1,3,6,1,2,1,206,2,2,6))
pmip6MagCompliance2.setObjects(*((_B,_J),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:pmip6MagCompliance2.setStatus(_A)
pmip6MagCoreReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,206,2,2,7))
pmip6MagCoreReadOnlyCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:pmip6MagCoreReadOnlyCompliance.setStatus(_A)
pmip6MagReadOnlyCompliance2=ModuleCompliance((1,3,6,1,2,1,206,2,2,8))
pmip6MagReadOnlyCompliance2.setObjects(*((_B,_J),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:pmip6MagReadOnlyCompliance2.setStatus(_A)
pmip6LmaCoreCompliance=ModuleCompliance((1,3,6,1,2,1,206,2,2,9))
pmip6LmaCoreCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:pmip6LmaCoreCompliance.setStatus(_A)
pmip6LmaCompliance2=ModuleCompliance((1,3,6,1,2,1,206,2,2,10))
pmip6LmaCompliance2.setObjects(*((_B,_K),(_B,_X)))
if mibBuilder.loadTexts:pmip6LmaCompliance2.setStatus(_A)
pmip6LmaReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,206,2,2,11))
pmip6LmaReadOnlyCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:pmip6LmaReadOnlyCompliance.setStatus(_A)
pmip6LmaReadOnlyCompliance2=ModuleCompliance((1,3,6,1,2,1,206,2,2,12))
pmip6LmaReadOnlyCompliance2.setObjects(*((_B,_K),(_B,_X)))
if mibBuilder.loadTexts:pmip6LmaReadOnlyCompliance2.setStatus(_A)
pmip6MagNotificationCompliance=ModuleCompliance((1,3,6,1,2,1,206,2,2,13))
pmip6MagNotificationCompliance.setObjects((_B,_Ah))
if mibBuilder.loadTexts:pmip6MagNotificationCompliance.setStatus(_A)
pmip6LmaNotificationCompliance=ModuleCompliance((1,3,6,1,2,1,206,2,2,14))
pmip6LmaNotificationCompliance.setObjects((_B,_Ai))
if mibBuilder.loadTexts:pmip6LmaNotificationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pmip6MIB':pmip6MIB,'pmip6Notifications':pmip6Notifications,_Ad:pmip6MagHomeTunnelEstablished,_Ae:pmip6MagHomeTunnelReleased,_Af:pmip6LmaHomeTunnelEstablished,_Ag:pmip6LmaHomeTunnelReleased,'pmip6Objects':pmip6Objects,'pmip6Core':pmip6Core,'pmip6System':pmip6System,_p:pmip6Capabilities,'pmip6Bindings':pmip6Bindings,'pmip6BindingCacheTable':pmip6BindingCacheTable,_n:pmip6BindingCacheEntry,_u:pmip6BindingPBUFlag,_H:pmip6BindingMnIndex,_M:pmip6BindingMnLLIndex,_v:pmip6BindingMagLinkLocalAddressType,_w:pmip6BindingMagLinkLocalAddress,_N:pmip6BindingTunnelIfIdentifier,_x:pmip6BindingMnInterfaceATT,_y:pmip6BindingTimeRecentlyAccepted,'pmip6Conf':pmip6Conf,_q:pmip6MobileNodeGeneratedTimestampInUse,_r:pmip6FixedMagLinkLocalAddressOnAllAccessLinksType,_s:pmip6FixedMagLinkLocalAddressOnAllAccessLinks,_t:pmip6FixedMagLinkLayerAddressOnAllAccessLinks,'pmip6Stats':pmip6Stats,'pmip6BindingRegCounters':pmip6BindingRegCounters,_A1:pmip6MissingMnIdentifierOption,_A2:pmip6MagNotAuthorizedForProxyReg,_A3:pmip6NotLMAForThisMobileNode,_A4:pmip6ProxyRegNotEnabled,_A5:pmip6MissingHomeNetworkPrefixOption,_A6:pmip6MissingHandOffIndicatorOption,_A7:pmip6MissingAccessTechTypeOption,_A8:pmip6NotAuthorizedForHomeNetworkPrefix,_A9:pmip6TimestampMismatch,_AA:pmip6TimestampLowerThanPrevAccepted,_AB:pmip6BcePbuPrefixSetDoNotMatch,_AC:pmip6InitialBindingRegistrations,_AD:pmip6BindingLifeTimeExtensionNoHandOff,_AE:pmip6BindingLifeTimeExtensionAfterHandOff,_AF:pmip6BindingDeRegistrations,_AG:pmip6BindingBindingAcks,_AH:pmip6CounterDiscontinuityTime,'pmip6Mag':pmip6Mag,'pmip6MagSystem':pmip6MagSystem,_AI:pmip6MagStatus,'pmip6MagProxyCOATable':pmip6MagProxyCOATable,'pmip6MagProxyCOAEntry':pmip6MagProxyCOAEntry,_a:pmip6MagProxyCOAType,_b:pmip6MagProxyCOA,_O:pmip6MagProxyCOAState,'pmip6MagConf':pmip6MagConf,_AL:pmip6MagEnableMagLocalRouting,'pmip6MagMnIdentifierTable':pmip6MagMnIdentifierTable,'pmip6MagMnIdentifierEntry':pmip6MagMnIdentifierEntry,_AS:pmip6MagMnIdentifier,'pmip6MagMnLLIdentifierTable':pmip6MagMnLLIdentifierTable,'pmip6MagMnLLIdentifierEntry':pmip6MagMnLLIdentifierEntry,_AT:pmip6MagMnLLIdentifier,'pmip6MagHomeNetworkPrefixTable':pmip6MagHomeNetworkPrefixTable,'pmip6MagHomeNetworkPrefixEntry':pmip6MagHomeNetworkPrefixEntry,_f:pmip6MagHomeNetworkPrefixType,_g:pmip6MagHomeNetworkPrefix,_AJ:pmip6MagHomeNetworkPrefixLength,_AK:pmip6MagHomeNetworkPrefixLifeTime,'pmip6MagRegistration':pmip6MagRegistration,'pmip6MagBLTable':pmip6MagBLTable,_o:pmip6MagBLEntry,_AM:pmip6MagBLFlag,_G:pmip6MagBLMnIndex,_L:pmip6MagBLMnLLIndex,_AN:pmip6MagBLMagLinkLocalAddressType,_AO:pmip6MagBLMagLinkLocalAddress,_AP:pmip6MagBLMagIfIdentifierToMn,_P:pmip6MagBLTunnelIfIdentifier,_AQ:pmip6MagBLMnInterfaceATT,_AR:pmip6MagBLTimeRecentlyAccepted,'pmip6MagMnProfileTable':pmip6MagMnProfileTable,'pmip6MagMnProfileEntry':pmip6MagMnProfileEntry,_i:pmip6MagProfMnIndex,_AU:pmip6MagProfMnIdentifier,_AV:pmip6MagProfMnLocalMobilityAnchorAddressType,_AW:pmip6MagProfMnLocalMobilityAnchorAddress,'pmip6Lma':pmip6Lma,'pmip6LmaSystem':pmip6LmaSystem,_AX:pmip6LmaStatus,'pmip6LmaLMAATable':pmip6LmaLMAATable,'pmip6LmaLMAAEntry':pmip6LmaLMAAEntry,_j:pmip6LmaLMAAType,_k:pmip6LmaLMAA,_Q:pmip6LmaLMAAState,'pmip6LmaConf':pmip6LmaConf,_AY:pmip6LmaMinDelayBeforeBCEDelete,_AZ:pmip6LmaMaxDelayBeforeNewBCEAssign,_Aa:pmip6LmaTimestampValidityWindow,'pmip6LmaMnIdentifierTable':pmip6LmaMnIdentifierTable,'pmip6LmaMnIdentifierEntry':pmip6LmaMnIdentifierEntry,_z:pmip6LmaMnIdentifier,'pmip6LmaMnLLIdentifierTable':pmip6LmaMnLLIdentifierTable,'pmip6LmaMnLLIdentifierEntry':pmip6LmaMnLLIdentifierEntry,_A0:pmip6LmaMnLLIdentifier,'pmip6LmaHomeNetworkPrefixTable':pmip6LmaHomeNetworkPrefixTable,'pmip6LmaHomeNetworkPrefixEntry':pmip6LmaHomeNetworkPrefixEntry,_l:pmip6LmaHomeNetworkPrefixType,_m:pmip6LmaHomeNetworkPrefix,_Ab:pmip6LmaHomeNetworkPrefixLength,_Ac:pmip6LmaHomeNetworkPrefixLifeTime,'pmip6Conformance':pmip6Conformance,'pmip6Groups':pmip6Groups,_I:pmip6SystemGroup,_T:pmip6BindingCacheGroup,_U:pmip6StatsGroup,_J:pmip6MagSystemGroup,_V:pmip6MagConfigurationGroup,_W:pmip6MagRegistrationGroup,_K:pmip6LmaSystemGroup,_X:pmip6LmaConfigurationGroup,_Ah:pmip6MagNotificationGroup,_Ai:pmip6LmaNotificationGroup,'pmip6Compliances':pmip6Compliances,'pmip6CoreCompliance':pmip6CoreCompliance,'pmip6Compliance2':pmip6Compliance2,'pmip6CoreReadOnlyCompliance':pmip6CoreReadOnlyCompliance,'pmip6ReadOnlyCompliance2':pmip6ReadOnlyCompliance2,'pmip6MagCoreCompliance':pmip6MagCoreCompliance,'pmip6MagCompliance2':pmip6MagCompliance2,'pmip6MagCoreReadOnlyCompliance':pmip6MagCoreReadOnlyCompliance,'pmip6MagReadOnlyCompliance2':pmip6MagReadOnlyCompliance2,'pmip6LmaCoreCompliance':pmip6LmaCoreCompliance,'pmip6LmaCompliance2':pmip6LmaCompliance2,'pmip6LmaReadOnlyCompliance':pmip6LmaReadOnlyCompliance,'pmip6LmaReadOnlyCompliance2':pmip6LmaReadOnlyCompliance2,'pmip6MagNotificationCompliance':pmip6MagNotificationCompliance,'pmip6LmaNotificationCompliance':pmip6LmaNotificationCompliance})