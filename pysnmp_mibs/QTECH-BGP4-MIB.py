_O='qtechBgpPeerConfedMemberEntry'
_N='qtechBgpPeerReflectorClientEntry'
_M='qtechBgpPeerPrefixInfoEntry'
_L='qtechBgpPeerCapReceivedCode'
_K='qtechBgpPeerCapAnnouncedCode'
_J='qtechBgpSupportedCapabilityCode'
_I='Integer32'
_H='deprecated'
_G='bgpPeerRemoteAddr'
_F='BGP4-MIB'
_E='OctetString'
_D='Unsigned32'
_C='QTECH-BGP4-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bgpPeerEntry,bgpPeerRemoteAddr=mibBuilder.importSymbols(_F,'bgpPeerEntry',_G)
InetAutonomousSystemNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAutonomousSystemNumber')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
qtechBgp4MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,38))
if mibBuilder.loadTexts:qtechBgp4MIB.setRevisions(('2003-04-01 00:00',))
class QtechBgpID(TextualConvention,OctetString):status=_A;displayHint='1d.';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_QtechBgpBaseScalars_ObjectIdentity=ObjectIdentity
qtechBgpBaseScalars=_QtechBgpBaseScalars_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,1))
_QtechBgpSupportedCapabilities_ObjectIdentity=ObjectIdentity
qtechBgpSupportedCapabilities=_QtechBgpSupportedCapabilities_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,1,1))
_QtechBgpCapabilitySupportAvailable_Type=TruthValue
_QtechBgpCapabilitySupportAvailable_Object=MibScalar
qtechBgpCapabilitySupportAvailable=_QtechBgpCapabilitySupportAvailable_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,1,1),_QtechBgpCapabilitySupportAvailable_Type())
qtechBgpCapabilitySupportAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpCapabilitySupportAvailable.setStatus(_A)
_QtechBgpSupportedCapabilitiesTable_Object=MibTable
qtechBgpSupportedCapabilitiesTable=_QtechBgpSupportedCapabilitiesTable_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,1,2))
if mibBuilder.loadTexts:qtechBgpSupportedCapabilitiesTable.setStatus(_A)
_QtechBgpSupportedCapabilitiesEntry_Object=MibTableRow
qtechBgpSupportedCapabilitiesEntry=_QtechBgpSupportedCapabilitiesEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,1,2,1))
qtechBgpSupportedCapabilitiesEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:qtechBgpSupportedCapabilitiesEntry.setStatus(_A)
class _QtechBgpSupportedCapabilityCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechBgpSupportedCapabilityCode_Type.__name__=_D
_QtechBgpSupportedCapabilityCode_Object=MibTableColumn
qtechBgpSupportedCapabilityCode=_QtechBgpSupportedCapabilityCode_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,1,2,1,1),_QtechBgpSupportedCapabilityCode_Type())
qtechBgpSupportedCapabilityCode.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpSupportedCapabilityCode.setStatus(_A)
_QtechBgpSupportedCapability_Type=TruthValue
_QtechBgpSupportedCapability_Object=MibTableColumn
qtechBgpSupportedCapability=_QtechBgpSupportedCapability_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,1,2,1,2),_QtechBgpSupportedCapability_Type())
qtechBgpSupportedCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpSupportedCapability.setStatus(_A)
_QtechBgpBaseScalarExtensions_ObjectIdentity=ObjectIdentity
qtechBgpBaseScalarExtensions=_QtechBgpBaseScalarExtensions_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,1,2))
_QtechBgpBaseScalarRouteReflectExts_ObjectIdentity=ObjectIdentity
qtechBgpBaseScalarRouteReflectExts=_QtechBgpBaseScalarRouteReflectExts_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,1,2,1))
_QtechBgpRouteReflector_Type=TruthValue
_QtechBgpRouteReflector_Object=MibScalar
qtechBgpRouteReflector=_QtechBgpRouteReflector_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,2,1,1),_QtechBgpRouteReflector_Type())
qtechBgpRouteReflector.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpRouteReflector.setStatus(_A)
_QtechBgpClusterId_Type=QtechBgpID
_QtechBgpClusterId_Object=MibScalar
qtechBgpClusterId=_QtechBgpClusterId_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,2,1,2),_QtechBgpClusterId_Type())
qtechBgpClusterId.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpClusterId.setStatus(_A)
_QtechBgpBaseScalarASConfedExts_ObjectIdentity=ObjectIdentity
qtechBgpBaseScalarASConfedExts=_QtechBgpBaseScalarASConfedExts_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,1,2,2))
_QtechBgpConfederationRouter_Type=TruthValue
_QtechBgpConfederationRouter_Object=MibScalar
qtechBgpConfederationRouter=_QtechBgpConfederationRouter_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,2,2,1),_QtechBgpConfederationRouter_Type())
qtechBgpConfederationRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpConfederationRouter.setStatus(_A)
_QtechBgpConfederationId_Type=InetAutonomousSystemNumber
_QtechBgpConfederationId_Object=MibScalar
qtechBgpConfederationId=_QtechBgpConfederationId_Object((1,3,6,1,4,1,27514,1,1,10,2,38,1,2,2,2),_QtechBgpConfederationId_Type())
qtechBgpConfederationId.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpConfederationId.setStatus(_A)
_QtechBgpPeer_ObjectIdentity=ObjectIdentity
qtechBgpPeer=_QtechBgpPeer_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,2))
_QtechBgpPeerPrefixInfoTable_Object=MibTable
qtechBgpPeerPrefixInfoTable=_QtechBgpPeerPrefixInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,1))
if mibBuilder.loadTexts:qtechBgpPeerPrefixInfoTable.setStatus(_A)
_QtechBgpPeerPrefixInfoEntry_Object=MibTableRow
qtechBgpPeerPrefixInfoEntry=_QtechBgpPeerPrefixInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,1,1))
if mibBuilder.loadTexts:qtechBgpPeerPrefixInfoEntry.setStatus(_A)
class _QtechBgpPeerPrefixLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_QtechBgpPeerPrefixLimit_Type.__name__=_D
_QtechBgpPeerPrefixLimit_Object=MibTableColumn
qtechBgpPeerPrefixLimit=_QtechBgpPeerPrefixLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,1,1,1),_QtechBgpPeerPrefixLimit_Type())
qtechBgpPeerPrefixLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerPrefixLimit.setStatus(_H)
_QtechBgpPeerPrefixAccepted_Type=Counter32
_QtechBgpPeerPrefixAccepted_Object=MibTableColumn
qtechBgpPeerPrefixAccepted=_QtechBgpPeerPrefixAccepted_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,1,1,2),_QtechBgpPeerPrefixAccepted_Type())
qtechBgpPeerPrefixAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerPrefixAccepted.setStatus(_H)
_QtechBgpPeerPrefixAdvertised_Type=Counter32
_QtechBgpPeerPrefixAdvertised_Object=MibTableColumn
qtechBgpPeerPrefixAdvertised=_QtechBgpPeerPrefixAdvertised_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,1,1,3),_QtechBgpPeerPrefixAdvertised_Type())
qtechBgpPeerPrefixAdvertised.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerPrefixAdvertised.setStatus(_H)
_QtechBgpPeerCapabilities_ObjectIdentity=ObjectIdentity
qtechBgpPeerCapabilities=_QtechBgpPeerCapabilities_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,2,2))
_QtechBgpPeerCapsAnnouncedTable_Object=MibTable
qtechBgpPeerCapsAnnouncedTable=_QtechBgpPeerCapsAnnouncedTable_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,2,1))
if mibBuilder.loadTexts:qtechBgpPeerCapsAnnouncedTable.setStatus(_A)
_QtechBgpPeerCapsAnnouncedEntry_Object=MibTableRow
qtechBgpPeerCapsAnnouncedEntry=_QtechBgpPeerCapsAnnouncedEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,2,1,1))
qtechBgpPeerCapsAnnouncedEntry.setIndexNames((0,_F,_G),(0,_C,_K))
if mibBuilder.loadTexts:qtechBgpPeerCapsAnnouncedEntry.setStatus(_A)
class _QtechBgpPeerCapAnnouncedCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechBgpPeerCapAnnouncedCode_Type.__name__=_D
_QtechBgpPeerCapAnnouncedCode_Object=MibTableColumn
qtechBgpPeerCapAnnouncedCode=_QtechBgpPeerCapAnnouncedCode_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,2,1,1,1),_QtechBgpPeerCapAnnouncedCode_Type())
qtechBgpPeerCapAnnouncedCode.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerCapAnnouncedCode.setStatus(_A)
class _QtechBgpPeerCapAnnouncedValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechBgpPeerCapAnnouncedValue_Type.__name__=_E
_QtechBgpPeerCapAnnouncedValue_Object=MibTableColumn
qtechBgpPeerCapAnnouncedValue=_QtechBgpPeerCapAnnouncedValue_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,2,1,1,2),_QtechBgpPeerCapAnnouncedValue_Type())
qtechBgpPeerCapAnnouncedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerCapAnnouncedValue.setStatus(_A)
_QtechBgpPeerCapsReceivedTable_Object=MibTable
qtechBgpPeerCapsReceivedTable=_QtechBgpPeerCapsReceivedTable_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,2,2))
if mibBuilder.loadTexts:qtechBgpPeerCapsReceivedTable.setStatus(_A)
_QtechBgpPeerCapsReceivedEntry_Object=MibTableRow
qtechBgpPeerCapsReceivedEntry=_QtechBgpPeerCapsReceivedEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,2,2,1))
qtechBgpPeerCapsReceivedEntry.setIndexNames((0,_F,_G),(0,_C,_L))
if mibBuilder.loadTexts:qtechBgpPeerCapsReceivedEntry.setStatus(_A)
class _QtechBgpPeerCapReceivedCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechBgpPeerCapReceivedCode_Type.__name__=_D
_QtechBgpPeerCapReceivedCode_Object=MibTableColumn
qtechBgpPeerCapReceivedCode=_QtechBgpPeerCapReceivedCode_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,2,2,1,1),_QtechBgpPeerCapReceivedCode_Type())
qtechBgpPeerCapReceivedCode.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerCapReceivedCode.setStatus(_A)
class _QtechBgpPeerCapReceivedValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechBgpPeerCapReceivedValue_Type.__name__=_E
_QtechBgpPeerCapReceivedValue_Object=MibTableColumn
qtechBgpPeerCapReceivedValue=_QtechBgpPeerCapReceivedValue_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,2,2,1,3),_QtechBgpPeerCapReceivedValue_Type())
qtechBgpPeerCapReceivedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerCapReceivedValue.setStatus(_A)
_QtechBgpPeerExtensions_ObjectIdentity=ObjectIdentity
qtechBgpPeerExtensions=_QtechBgpPeerExtensions_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,2,3))
_QtechBgpPeerRouteReflectionExts_ObjectIdentity=ObjectIdentity
qtechBgpPeerRouteReflectionExts=_QtechBgpPeerRouteReflectionExts_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,2,3,1))
_QtechBgpPeerReflectorClientTable_Object=MibTable
qtechBgpPeerReflectorClientTable=_QtechBgpPeerReflectorClientTable_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,3,1,1))
if mibBuilder.loadTexts:qtechBgpPeerReflectorClientTable.setStatus(_A)
_QtechBgpPeerReflectorClientEntry_Object=MibTableRow
qtechBgpPeerReflectorClientEntry=_QtechBgpPeerReflectorClientEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,3,1,1,1))
if mibBuilder.loadTexts:qtechBgpPeerReflectorClientEntry.setStatus(_A)
class _QtechBgpPeerReflectorClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nonClient',0),('client',1),('meshedClient',2)))
_QtechBgpPeerReflectorClient_Type.__name__=_I
_QtechBgpPeerReflectorClient_Object=MibTableColumn
qtechBgpPeerReflectorClient=_QtechBgpPeerReflectorClient_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,3,1,1,1,1),_QtechBgpPeerReflectorClient_Type())
qtechBgpPeerReflectorClient.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerReflectorClient.setStatus(_A)
_QtechBgpPeerASConfederationExts_ObjectIdentity=ObjectIdentity
qtechBgpPeerASConfederationExts=_QtechBgpPeerASConfederationExts_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,2,3,2))
_QtechBgpPeerConfedMemberTable_Object=MibTable
qtechBgpPeerConfedMemberTable=_QtechBgpPeerConfedMemberTable_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,3,2,1))
if mibBuilder.loadTexts:qtechBgpPeerConfedMemberTable.setStatus(_A)
_QtechBgpPeerConfedMemberEntry_Object=MibTableRow
qtechBgpPeerConfedMemberEntry=_QtechBgpPeerConfedMemberEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,3,2,1,1))
if mibBuilder.loadTexts:qtechBgpPeerConfedMemberEntry.setStatus(_A)
_QtechBgpPeerConfedMember_Type=TruthValue
_QtechBgpPeerConfedMember_Object=MibTableColumn
qtechBgpPeerConfedMember=_QtechBgpPeerConfedMember_Object((1,3,6,1,4,1,27514,1,1,10,2,38,2,3,2,1,1,1),_QtechBgpPeerConfedMember_Type())
qtechBgpPeerConfedMember.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechBgpPeerConfedMember.setStatus(_A)
_QtechBgpConformance_ObjectIdentity=ObjectIdentity
qtechBgpConformance=_QtechBgpConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,3))
_QtechBgpMIBCompliances_ObjectIdentity=ObjectIdentity
qtechBgpMIBCompliances=_QtechBgpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,3,1))
_QtechBgpMIBGroups_ObjectIdentity=ObjectIdentity
qtechBgpMIBGroups=_QtechBgpMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,38,3,2))
bgpPeerEntry.registerAugmentions((_C,_M))
qtechBgpPeerPrefixInfoEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions((_C,_N))
qtechBgpPeerReflectorClientEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions((_C,_O))
qtechBgpPeerConfedMemberEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'QtechBgpID':QtechBgpID,'qtechBgp4MIB':qtechBgp4MIB,'qtechBgpBaseScalars':qtechBgpBaseScalars,'qtechBgpSupportedCapabilities':qtechBgpSupportedCapabilities,'qtechBgpCapabilitySupportAvailable':qtechBgpCapabilitySupportAvailable,'qtechBgpSupportedCapabilitiesTable':qtechBgpSupportedCapabilitiesTable,'qtechBgpSupportedCapabilitiesEntry':qtechBgpSupportedCapabilitiesEntry,_J:qtechBgpSupportedCapabilityCode,'qtechBgpSupportedCapability':qtechBgpSupportedCapability,'qtechBgpBaseScalarExtensions':qtechBgpBaseScalarExtensions,'qtechBgpBaseScalarRouteReflectExts':qtechBgpBaseScalarRouteReflectExts,'qtechBgpRouteReflector':qtechBgpRouteReflector,'qtechBgpClusterId':qtechBgpClusterId,'qtechBgpBaseScalarASConfedExts':qtechBgpBaseScalarASConfedExts,'qtechBgpConfederationRouter':qtechBgpConfederationRouter,'qtechBgpConfederationId':qtechBgpConfederationId,'qtechBgpPeer':qtechBgpPeer,'qtechBgpPeerPrefixInfoTable':qtechBgpPeerPrefixInfoTable,_M:qtechBgpPeerPrefixInfoEntry,'qtechBgpPeerPrefixLimit':qtechBgpPeerPrefixLimit,'qtechBgpPeerPrefixAccepted':qtechBgpPeerPrefixAccepted,'qtechBgpPeerPrefixAdvertised':qtechBgpPeerPrefixAdvertised,'qtechBgpPeerCapabilities':qtechBgpPeerCapabilities,'qtechBgpPeerCapsAnnouncedTable':qtechBgpPeerCapsAnnouncedTable,'qtechBgpPeerCapsAnnouncedEntry':qtechBgpPeerCapsAnnouncedEntry,_K:qtechBgpPeerCapAnnouncedCode,'qtechBgpPeerCapAnnouncedValue':qtechBgpPeerCapAnnouncedValue,'qtechBgpPeerCapsReceivedTable':qtechBgpPeerCapsReceivedTable,'qtechBgpPeerCapsReceivedEntry':qtechBgpPeerCapsReceivedEntry,_L:qtechBgpPeerCapReceivedCode,'qtechBgpPeerCapReceivedValue':qtechBgpPeerCapReceivedValue,'qtechBgpPeerExtensions':qtechBgpPeerExtensions,'qtechBgpPeerRouteReflectionExts':qtechBgpPeerRouteReflectionExts,'qtechBgpPeerReflectorClientTable':qtechBgpPeerReflectorClientTable,_N:qtechBgpPeerReflectorClientEntry,'qtechBgpPeerReflectorClient':qtechBgpPeerReflectorClient,'qtechBgpPeerASConfederationExts':qtechBgpPeerASConfederationExts,'qtechBgpPeerConfedMemberTable':qtechBgpPeerConfedMemberTable,_O:qtechBgpPeerConfedMemberEntry,'qtechBgpPeerConfedMember':qtechBgpPeerConfedMember,'qtechBgpConformance':qtechBgpConformance,'qtechBgpMIBCompliances':qtechBgpMIBCompliances,'qtechBgpMIBGroups':qtechBgpMIBGroups})