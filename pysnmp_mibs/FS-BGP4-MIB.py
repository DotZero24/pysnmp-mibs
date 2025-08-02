_O='fsBgpPeerConfedMemberEntry'
_N='fsBgpPeerReflectorClientEntry'
_M='fsBgpPeerPrefixInfoEntry'
_L='fsBgpPeerCapReceivedCode'
_K='fsBgpPeerCapAnnouncedCode'
_J='fsBgpSupportedCapabilityCode'
_I='Integer32'
_H='deprecated'
_G='bgpPeerRemoteAddr'
_F='BGP4-MIB'
_E='OctetString'
_D='Unsigned32'
_C='FS-BGP4-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bgpPeerEntry,bgpPeerRemoteAddr=mibBuilder.importSymbols(_F,'bgpPeerEntry',_G)
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAutonomousSystemNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAutonomousSystemNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fsBgp4MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,38))
if mibBuilder.loadTexts:fsBgp4MIB.setRevisions(('2003-04-01 00:00',))
class FSBgpID(TextualConvention,OctetString):status=_A;displayHint='1d.';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_FsBgpBaseScalars_ObjectIdentity=ObjectIdentity
fsBgpBaseScalars=_FsBgpBaseScalars_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,1))
_FsBgpSupportedCapabilities_ObjectIdentity=ObjectIdentity
fsBgpSupportedCapabilities=_FsBgpSupportedCapabilities_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,1,1))
_FsBgpCapabilitySupportAvailable_Type=TruthValue
_FsBgpCapabilitySupportAvailable_Object=MibScalar
fsBgpCapabilitySupportAvailable=_FsBgpCapabilitySupportAvailable_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,1,1),_FsBgpCapabilitySupportAvailable_Type())
fsBgpCapabilitySupportAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpCapabilitySupportAvailable.setStatus(_A)
_FsBgpSupportedCapabilitiesTable_Object=MibTable
fsBgpSupportedCapabilitiesTable=_FsBgpSupportedCapabilitiesTable_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,1,2))
if mibBuilder.loadTexts:fsBgpSupportedCapabilitiesTable.setStatus(_A)
_FsBgpSupportedCapabilitiesEntry_Object=MibTableRow
fsBgpSupportedCapabilitiesEntry=_FsBgpSupportedCapabilitiesEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,1,2,1))
fsBgpSupportedCapabilitiesEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:fsBgpSupportedCapabilitiesEntry.setStatus(_A)
class _FsBgpSupportedCapabilityCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsBgpSupportedCapabilityCode_Type.__name__=_D
_FsBgpSupportedCapabilityCode_Object=MibTableColumn
fsBgpSupportedCapabilityCode=_FsBgpSupportedCapabilityCode_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,1,2,1,1),_FsBgpSupportedCapabilityCode_Type())
fsBgpSupportedCapabilityCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpSupportedCapabilityCode.setStatus(_A)
_FsBgpSupportedCapability_Type=TruthValue
_FsBgpSupportedCapability_Object=MibTableColumn
fsBgpSupportedCapability=_FsBgpSupportedCapability_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,1,2,1,2),_FsBgpSupportedCapability_Type())
fsBgpSupportedCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpSupportedCapability.setStatus(_A)
_FsBgpBaseScalarExtensions_ObjectIdentity=ObjectIdentity
fsBgpBaseScalarExtensions=_FsBgpBaseScalarExtensions_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,1,2))
_FsBgpBaseScalarRouteReflectExts_ObjectIdentity=ObjectIdentity
fsBgpBaseScalarRouteReflectExts=_FsBgpBaseScalarRouteReflectExts_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,1,2,1))
_FsBgpRouteReflector_Type=TruthValue
_FsBgpRouteReflector_Object=MibScalar
fsBgpRouteReflector=_FsBgpRouteReflector_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,2,1,1),_FsBgpRouteReflector_Type())
fsBgpRouteReflector.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpRouteReflector.setStatus(_A)
_FsBgpClusterId_Type=FSBgpID
_FsBgpClusterId_Object=MibScalar
fsBgpClusterId=_FsBgpClusterId_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,2,1,2),_FsBgpClusterId_Type())
fsBgpClusterId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpClusterId.setStatus(_A)
_FsBgpBaseScalarASConfedExts_ObjectIdentity=ObjectIdentity
fsBgpBaseScalarASConfedExts=_FsBgpBaseScalarASConfedExts_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,1,2,2))
_FsBgpConfederationRouter_Type=TruthValue
_FsBgpConfederationRouter_Object=MibScalar
fsBgpConfederationRouter=_FsBgpConfederationRouter_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,2,2,1),_FsBgpConfederationRouter_Type())
fsBgpConfederationRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpConfederationRouter.setStatus(_A)
_FsBgpConfederationId_Type=InetAutonomousSystemNumber
_FsBgpConfederationId_Object=MibScalar
fsBgpConfederationId=_FsBgpConfederationId_Object((1,3,6,1,4,1,52642,1,1,10,2,38,1,2,2,2),_FsBgpConfederationId_Type())
fsBgpConfederationId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpConfederationId.setStatus(_A)
_FsBgpPeer_ObjectIdentity=ObjectIdentity
fsBgpPeer=_FsBgpPeer_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,2))
_FsBgpPeerPrefixInfoTable_Object=MibTable
fsBgpPeerPrefixInfoTable=_FsBgpPeerPrefixInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,1))
if mibBuilder.loadTexts:fsBgpPeerPrefixInfoTable.setStatus(_A)
_FsBgpPeerPrefixInfoEntry_Object=MibTableRow
fsBgpPeerPrefixInfoEntry=_FsBgpPeerPrefixInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,1,1))
if mibBuilder.loadTexts:fsBgpPeerPrefixInfoEntry.setStatus(_A)
class _FsBgpPeerPrefixLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsBgpPeerPrefixLimit_Type.__name__=_D
_FsBgpPeerPrefixLimit_Object=MibTableColumn
fsBgpPeerPrefixLimit=_FsBgpPeerPrefixLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,1,1,1),_FsBgpPeerPrefixLimit_Type())
fsBgpPeerPrefixLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerPrefixLimit.setStatus(_H)
_FsBgpPeerPrefixAccepted_Type=Counter32
_FsBgpPeerPrefixAccepted_Object=MibTableColumn
fsBgpPeerPrefixAccepted=_FsBgpPeerPrefixAccepted_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,1,1,2),_FsBgpPeerPrefixAccepted_Type())
fsBgpPeerPrefixAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerPrefixAccepted.setStatus(_H)
_FsBgpPeerPrefixAdvertised_Type=Counter32
_FsBgpPeerPrefixAdvertised_Object=MibTableColumn
fsBgpPeerPrefixAdvertised=_FsBgpPeerPrefixAdvertised_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,1,1,3),_FsBgpPeerPrefixAdvertised_Type())
fsBgpPeerPrefixAdvertised.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerPrefixAdvertised.setStatus(_H)
_FsBgpPeerCapabilities_ObjectIdentity=ObjectIdentity
fsBgpPeerCapabilities=_FsBgpPeerCapabilities_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,2,2))
_FsBgpPeerCapsAnnouncedTable_Object=MibTable
fsBgpPeerCapsAnnouncedTable=_FsBgpPeerCapsAnnouncedTable_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,2,1))
if mibBuilder.loadTexts:fsBgpPeerCapsAnnouncedTable.setStatus(_A)
_FsBgpPeerCapsAnnouncedEntry_Object=MibTableRow
fsBgpPeerCapsAnnouncedEntry=_FsBgpPeerCapsAnnouncedEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,2,1,1))
fsBgpPeerCapsAnnouncedEntry.setIndexNames((0,_F,_G),(0,_C,_K))
if mibBuilder.loadTexts:fsBgpPeerCapsAnnouncedEntry.setStatus(_A)
class _FsBgpPeerCapAnnouncedCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsBgpPeerCapAnnouncedCode_Type.__name__=_D
_FsBgpPeerCapAnnouncedCode_Object=MibTableColumn
fsBgpPeerCapAnnouncedCode=_FsBgpPeerCapAnnouncedCode_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,2,1,1,1),_FsBgpPeerCapAnnouncedCode_Type())
fsBgpPeerCapAnnouncedCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerCapAnnouncedCode.setStatus(_A)
class _FsBgpPeerCapAnnouncedValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsBgpPeerCapAnnouncedValue_Type.__name__=_E
_FsBgpPeerCapAnnouncedValue_Object=MibTableColumn
fsBgpPeerCapAnnouncedValue=_FsBgpPeerCapAnnouncedValue_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,2,1,1,2),_FsBgpPeerCapAnnouncedValue_Type())
fsBgpPeerCapAnnouncedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerCapAnnouncedValue.setStatus(_A)
_FsBgpPeerCapsReceivedTable_Object=MibTable
fsBgpPeerCapsReceivedTable=_FsBgpPeerCapsReceivedTable_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,2,2))
if mibBuilder.loadTexts:fsBgpPeerCapsReceivedTable.setStatus(_A)
_FsBgpPeerCapsReceivedEntry_Object=MibTableRow
fsBgpPeerCapsReceivedEntry=_FsBgpPeerCapsReceivedEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,2,2,1))
fsBgpPeerCapsReceivedEntry.setIndexNames((0,_F,_G),(0,_C,_L))
if mibBuilder.loadTexts:fsBgpPeerCapsReceivedEntry.setStatus(_A)
class _FsBgpPeerCapReceivedCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsBgpPeerCapReceivedCode_Type.__name__=_D
_FsBgpPeerCapReceivedCode_Object=MibTableColumn
fsBgpPeerCapReceivedCode=_FsBgpPeerCapReceivedCode_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,2,2,1,1),_FsBgpPeerCapReceivedCode_Type())
fsBgpPeerCapReceivedCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerCapReceivedCode.setStatus(_A)
class _FsBgpPeerCapReceivedValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsBgpPeerCapReceivedValue_Type.__name__=_E
_FsBgpPeerCapReceivedValue_Object=MibTableColumn
fsBgpPeerCapReceivedValue=_FsBgpPeerCapReceivedValue_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,2,2,1,3),_FsBgpPeerCapReceivedValue_Type())
fsBgpPeerCapReceivedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerCapReceivedValue.setStatus(_A)
_FsBgpPeerExtensions_ObjectIdentity=ObjectIdentity
fsBgpPeerExtensions=_FsBgpPeerExtensions_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,2,3))
_FsBgpPeerRouteReflectionExts_ObjectIdentity=ObjectIdentity
fsBgpPeerRouteReflectionExts=_FsBgpPeerRouteReflectionExts_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,2,3,1))
_FsBgpPeerReflectorClientTable_Object=MibTable
fsBgpPeerReflectorClientTable=_FsBgpPeerReflectorClientTable_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,3,1,1))
if mibBuilder.loadTexts:fsBgpPeerReflectorClientTable.setStatus(_A)
_FsBgpPeerReflectorClientEntry_Object=MibTableRow
fsBgpPeerReflectorClientEntry=_FsBgpPeerReflectorClientEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,3,1,1,1))
if mibBuilder.loadTexts:fsBgpPeerReflectorClientEntry.setStatus(_A)
class _FsBgpPeerReflectorClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nonClient',0),('client',1),('meshedClient',2)))
_FsBgpPeerReflectorClient_Type.__name__=_I
_FsBgpPeerReflectorClient_Object=MibTableColumn
fsBgpPeerReflectorClient=_FsBgpPeerReflectorClient_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,3,1,1,1,1),_FsBgpPeerReflectorClient_Type())
fsBgpPeerReflectorClient.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerReflectorClient.setStatus(_A)
_FsBgpPeerASConfederationExts_ObjectIdentity=ObjectIdentity
fsBgpPeerASConfederationExts=_FsBgpPeerASConfederationExts_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,2,3,2))
_FsBgpPeerConfedMemberTable_Object=MibTable
fsBgpPeerConfedMemberTable=_FsBgpPeerConfedMemberTable_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,3,2,1))
if mibBuilder.loadTexts:fsBgpPeerConfedMemberTable.setStatus(_A)
_FsBgpPeerConfedMemberEntry_Object=MibTableRow
fsBgpPeerConfedMemberEntry=_FsBgpPeerConfedMemberEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,3,2,1,1))
if mibBuilder.loadTexts:fsBgpPeerConfedMemberEntry.setStatus(_A)
_FsBgpPeerConfedMember_Type=TruthValue
_FsBgpPeerConfedMember_Object=MibTableColumn
fsBgpPeerConfedMember=_FsBgpPeerConfedMember_Object((1,3,6,1,4,1,52642,1,1,10,2,38,2,3,2,1,1,1),_FsBgpPeerConfedMember_Type())
fsBgpPeerConfedMember.setMaxAccess(_B)
if mibBuilder.loadTexts:fsBgpPeerConfedMember.setStatus(_A)
_FsBgpConformance_ObjectIdentity=ObjectIdentity
fsBgpConformance=_FsBgpConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,3))
_FsBgpMIBCompliances_ObjectIdentity=ObjectIdentity
fsBgpMIBCompliances=_FsBgpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,3,1))
_FsBgpMIBGroups_ObjectIdentity=ObjectIdentity
fsBgpMIBGroups=_FsBgpMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,38,3,2))
bgpPeerEntry.registerAugmentions((_C,_M))
fsBgpPeerPrefixInfoEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions((_C,_N))
fsBgpPeerReflectorClientEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions((_C,_O))
fsBgpPeerConfedMemberEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'FSBgpID':FSBgpID,'fsBgp4MIB':fsBgp4MIB,'fsBgpBaseScalars':fsBgpBaseScalars,'fsBgpSupportedCapabilities':fsBgpSupportedCapabilities,'fsBgpCapabilitySupportAvailable':fsBgpCapabilitySupportAvailable,'fsBgpSupportedCapabilitiesTable':fsBgpSupportedCapabilitiesTable,'fsBgpSupportedCapabilitiesEntry':fsBgpSupportedCapabilitiesEntry,_J:fsBgpSupportedCapabilityCode,'fsBgpSupportedCapability':fsBgpSupportedCapability,'fsBgpBaseScalarExtensions':fsBgpBaseScalarExtensions,'fsBgpBaseScalarRouteReflectExts':fsBgpBaseScalarRouteReflectExts,'fsBgpRouteReflector':fsBgpRouteReflector,'fsBgpClusterId':fsBgpClusterId,'fsBgpBaseScalarASConfedExts':fsBgpBaseScalarASConfedExts,'fsBgpConfederationRouter':fsBgpConfederationRouter,'fsBgpConfederationId':fsBgpConfederationId,'fsBgpPeer':fsBgpPeer,'fsBgpPeerPrefixInfoTable':fsBgpPeerPrefixInfoTable,_M:fsBgpPeerPrefixInfoEntry,'fsBgpPeerPrefixLimit':fsBgpPeerPrefixLimit,'fsBgpPeerPrefixAccepted':fsBgpPeerPrefixAccepted,'fsBgpPeerPrefixAdvertised':fsBgpPeerPrefixAdvertised,'fsBgpPeerCapabilities':fsBgpPeerCapabilities,'fsBgpPeerCapsAnnouncedTable':fsBgpPeerCapsAnnouncedTable,'fsBgpPeerCapsAnnouncedEntry':fsBgpPeerCapsAnnouncedEntry,_K:fsBgpPeerCapAnnouncedCode,'fsBgpPeerCapAnnouncedValue':fsBgpPeerCapAnnouncedValue,'fsBgpPeerCapsReceivedTable':fsBgpPeerCapsReceivedTable,'fsBgpPeerCapsReceivedEntry':fsBgpPeerCapsReceivedEntry,_L:fsBgpPeerCapReceivedCode,'fsBgpPeerCapReceivedValue':fsBgpPeerCapReceivedValue,'fsBgpPeerExtensions':fsBgpPeerExtensions,'fsBgpPeerRouteReflectionExts':fsBgpPeerRouteReflectionExts,'fsBgpPeerReflectorClientTable':fsBgpPeerReflectorClientTable,_N:fsBgpPeerReflectorClientEntry,'fsBgpPeerReflectorClient':fsBgpPeerReflectorClient,'fsBgpPeerASConfederationExts':fsBgpPeerASConfederationExts,'fsBgpPeerConfedMemberTable':fsBgpPeerConfedMemberTable,_O:fsBgpPeerConfedMemberEntry,'fsBgpPeerConfedMember':fsBgpPeerConfedMember,'fsBgpConformance':fsBgpConformance,'fsBgpMIBCompliances':fsBgpMIBCompliances,'fsBgpMIBGroups':fsBgpMIBGroups})