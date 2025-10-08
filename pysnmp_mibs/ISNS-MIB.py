#
# PySNMP MIB module ISNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/ISNS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
FcAddressIdOrZero, FcNameIdOrZero = mibBuilder.importSymbols("FC-MGMT-MIB", "FcAddressIdOrZero", "FcNameIdOrZero")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
TimeStamp, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention")
isnsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 163))
isnsMIB.setRevisions(('2007-07-11 00:00',))
if mibBuilder.loadTexts: isnsMIB.setLastUpdated('200707110000Z')
if mibBuilder.loadTexts: isnsMIB.setOrganization('IETF IPS Working Group')
class IsnsDiscoveryDomainSetId(TextualConvention, Unsigned32):
    reference = 'RFC 4171, Section 6.11.1.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IsnsDdsStatusType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 6.11.1.3'
    status = 'current'
    namedValues = NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("reserved29", 29), ("reserved30", 30), ("ddsEnabled", 31))

class IsnsDiscoveryDomainId(TextualConvention, Unsigned32):
    reference = 'RFC 4171, Section 6'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IsnsDdFeatureType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 6.11.2.9'
    status = 'current'
    namedValues = NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("reserved29", 29), ("reserved30", 30), ("bootlist", 31))

class IsnsDdDdsModificationType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 2.4'
    status = 'current'
    namedValues = NamedValues(("controlNode", 0), ("targetIscsiNode", 1), ("initiatorIscsiNode", 2), ("targetIfcpNode", 3), ("initiatorIfcpNode", 4))

class IsnsEntityIndexIdOrZero(TextualConvention, Unsigned32):
    reference = 'RFC 4171, Section 6'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IsnsPortalGroupIndexId(TextualConvention, Unsigned32):
    reference = 'RFC 4171, Section 6'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IsnsPortalIndexId(TextualConvention, Unsigned32):
    reference = 'RFC 4171, Section 6'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IsnsPortalPortTypeId(TextualConvention, Integer32):
    reference = 'RFC 4171, Section 6.3.2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("udp", 1), ("tcp", 2))

class IsnsPortalGroupTagIdOrNull(TextualConvention, Integer32):
    reference = 'RFC 4171, Section 6.5.4, and RFC 3720'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 65535)

class IsnsPortalSecurityType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 6.3.9'
    status = 'current'
    namedValues = NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("tunnelModePreferred", 25), ("transportModePreferred", 26), ("pfsEnabled", 27), ("agressiveModeEnabled", 28), ("mainModeEnabled", 29), ("ikeIPsecEnabled", 30), ("bitmapVALID", 31))

class IsnsNodeIndexId(TextualConvention, Unsigned32):
    reference = 'RFC 4171, Section 6.4.5'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IsnsIscsiNodeType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 6.4.2'
    status = 'current'
    namedValues = NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("control", 29), ("initiator", 30), ("target", 31))

class IsnsFcClassOfServiceType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 6.6.8'
    status = 'current'
    namedValues = NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("class3", 28), ("class2", 29))

class IsnsIscsiScnType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 6.4.4'
    status = 'current'
    namedValues = NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("initiatorAndSelfOnly", 24), ("targetAndSelfOnly", 25), ("managementRegistrationScn", 26), ("objectRemoved", 27), ("objectAdded", 28), ("objectUpdated", 29), ("ddOrDdsMemberRemoved", 30), ("ddOrDdsMemberAdded", 31))

class IsnsIfcpScnType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 6.6.12'
    status = 'current'
    namedValues = NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("initiatorAndSelfOnly", 24), ("targetAndSelfOnly", 25), ("managementRegistrationScn", 26), ("objectRemoved", 27), ("objectAdded", 28), ("objectUpdated", 29), ("ddOrDdsMemberRemoved", 30), ("ddOrDdsMemberAdded", 31))

class IsnsFcPortRoleType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 6.6.13'
    status = 'current'
    namedValues = NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("control", 29), ("initiator", 30), ("target", 31))

class IsnsSrvrDiscoveryMethodsType(TextualConvention, Bits):
    reference = 'RFC 4171, Section 2.5'
    status = 'current'
    namedValues = NamedValues(("dhcp", 0), ("slp", 1), ("multicastGroupHb", 2), ("broadcastHb", 3), ("cfgdServerList", 4), ("other", 5))

isnsNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 0))
isnsObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1))
isnsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 2))
isnsServerInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1))
isnsServerTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 1), )
if mibBuilder.loadTexts: isnsServerTable.setStatus('current')
isnsServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"))
if mibBuilder.loadTexts: isnsServerEntry.setStatus('current')
isnsServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: isnsServerIndex.setStatus('current')
isnsServerName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerName.setStatus('current')
isnsServerIsnsVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerIsnsVersion.setStatus('current')
isnsServerVendorInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerVendorInfo.setStatus('current')
isnsServerPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 5), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerPhysicalIndex.setStatus('current')
isnsServerTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerTcpPort.setStatus('current')
isnsServerUdpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 7), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerUdpPort.setStatus('current')
isnsServerDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerDiscontinuityTime.setStatus('current')
isnsServerRole = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("server", 2), ("backupServer", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerRole.setStatus('current')
isnsServerDiscoveryMethodsEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 10), IsnsSrvrDiscoveryMethodsType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerDiscoveryMethodsEnabled.setStatus('current')
isnsServerDiscoveryMcGroupType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 11), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerDiscoveryMcGroupType.setStatus('current')
isnsServerDiscoveryMcGroupAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 12), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerDiscoveryMcGroupAddress.setStatus('current')
isnsServerEsiNonResponseThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerEsiNonResponseThreshold.setStatus('current')
isnsServerEnableControlNodeMgtScn = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 14), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerEnableControlNodeMgtScn.setStatus('current')
isnsServerDefaultDdDdsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inNoDomain", 1), ("inDefaultDdAndDds", 2))).clone('inNoDomain')).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerDefaultDdDdsStatus.setStatus('current')
isnsServerUpdateDdDdsSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 16), IsnsDdDdsModificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerUpdateDdDdsSupported.setStatus('current')
isnsServerUpdateDdDdsEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 17), IsnsDdDdsModificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsServerUpdateDdDdsEnabled.setStatus('current')
isnsNumObjectsTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 2), )
if mibBuilder.loadTexts: isnsNumObjectsTable.setStatus('current')
isnsNumObjectsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1), )
isnsServerEntry.registerAugmentions(("ISNS-MIB", "isnsNumObjectsEntry"))
isnsNumObjectsEntry.setIndexNames(*isnsServerEntry.getIndexNames())
if mibBuilder.loadTexts: isnsNumObjectsEntry.setStatus('current')
isnsNumDds = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsNumDds.setStatus('current')
isnsNumDd = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsNumDd.setStatus('current')
isnsNumEntities = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsNumEntities.setStatus('current')
isnsNumPortals = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsNumPortals.setStatus('current')
isnsNumPortalGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsNumPortalGroups.setStatus('current')
isnsNumIscsiNodes = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsNumIscsiNodes.setStatus('current')
isnsNumFcPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsNumFcPorts.setStatus('current')
isnsNumFcNodes = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsNumFcNodes.setStatus('current')
isnsControlNodeInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 3))
isnsControlNodeIscsiTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1), )
if mibBuilder.loadTexts: isnsControlNodeIscsiTable.setStatus('current')
isnsControlNodeIscsiEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsControlNodeIscsiNodeIndex"))
if mibBuilder.loadTexts: isnsControlNodeIscsiEntry.setStatus('current')
isnsControlNodeIscsiNodeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1, 1), IsnsNodeIndexId())
if mibBuilder.loadTexts: isnsControlNodeIscsiNodeIndex.setStatus('current')
isnsControlNodeIscsiNodeName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsControlNodeIscsiNodeName.setStatus('current')
isnsControlNodeIscsiIsRegistered = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsControlNodeIscsiIsRegistered.setStatus('current')
isnsControlNodeIscsiRcvMgtSCN = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsControlNodeIscsiRcvMgtSCN.setStatus('current')
isnsControlNodeFcPortTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2), )
if mibBuilder.loadTexts: isnsControlNodeFcPortTable.setStatus('current')
isnsControlNodeFcPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsControlNodeFcPortWwpn"))
if mibBuilder.loadTexts: isnsControlNodeFcPortEntry.setStatus('current')
isnsControlNodeFcPortWwpn = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8))
if mibBuilder.loadTexts: isnsControlNodeFcPortWwpn.setStatus('current')
isnsControlNodeFcPortIsRegistered = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsControlNodeFcPortIsRegistered.setStatus('current')
isnsControlNodeFcPortRcvMgtSCN = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsControlNodeFcPortRcvMgtSCN.setStatus('current')
isnsDdsInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 4))
isnsDdsTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1), )
if mibBuilder.loadTexts: isnsDdsTable.setStatus('current')
isnsDdsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsDdsId"))
if mibBuilder.loadTexts: isnsDdsEntry.setStatus('current')
isnsDdsId = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1, 1, 1), IsnsDiscoveryDomainSetId())
if mibBuilder.loadTexts: isnsDdsId.setStatus('current')
isnsDdsSymbolicName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdsSymbolicName.setStatus('current')
isnsDdsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1, 1, 3), IsnsDdsStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdsStatus.setStatus('current')
isnsDdsMemberTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 2), )
if mibBuilder.loadTexts: isnsDdsMemberTable.setStatus('current')
isnsDdsMemberEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 2, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsDdsId"), (0, "ISNS-MIB", "isnsDdsMemberDdId"))
if mibBuilder.loadTexts: isnsDdsMemberEntry.setStatus('current')
isnsDdsMemberDdId = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 2, 1, 1), IsnsDiscoveryDomainId())
if mibBuilder.loadTexts: isnsDdsMemberDdId.setStatus('current')
isnsDdsMemberSymbolicName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdsMemberSymbolicName.setStatus('current')
isnsDdInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 5))
isnsDdTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1), )
if mibBuilder.loadTexts: isnsDdTable.setStatus('current')
isnsDdEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsDdId"))
if mibBuilder.loadTexts: isnsDdEntry.setStatus('current')
isnsDdId = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1, 1, 1), IsnsDiscoveryDomainId())
if mibBuilder.loadTexts: isnsDdId.setStatus('current')
isnsDdSymbolicName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdSymbolicName.setStatus('current')
isnsDdFeatures = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1, 1, 3), IsnsDdFeatureType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdFeatures.setStatus('current')
isnsDdIscsiMemberTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2), )
if mibBuilder.loadTexts: isnsDdIscsiMemberTable.setStatus('current')
isnsDdIscsiMemberEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsDdId"), (0, "ISNS-MIB", "isnsDdIscsiMemberIndex"))
if mibBuilder.loadTexts: isnsDdIscsiMemberEntry.setStatus('current')
isnsDdIscsiMemberIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2, 1, 1), IsnsNodeIndexId())
if mibBuilder.loadTexts: isnsDdIscsiMemberIndex.setStatus('current')
isnsDdIscsiMemberName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 223))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdIscsiMemberName.setStatus('current')
isnsDdIscsiMemberIsRegistered = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdIscsiMemberIsRegistered.setStatus('current')
isnsDdPortalMemberTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3), )
if mibBuilder.loadTexts: isnsDdPortalMemberTable.setStatus('current')
isnsDdPortalMemberEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsDdId"), (0, "ISNS-MIB", "isnsDdPortalMemberIndex"))
if mibBuilder.loadTexts: isnsDdPortalMemberEntry.setStatus('current')
isnsDdPortalMemberIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 1), IsnsPortalIndexId())
if mibBuilder.loadTexts: isnsDdPortalMemberIndex.setStatus('current')
isnsDdPortalMemberAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdPortalMemberAddressType.setStatus('current')
isnsDdPortalMemberAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdPortalMemberAddress.setStatus('current')
isnsDdPortalMemberPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 4), IsnsPortalPortTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdPortalMemberPortType.setStatus('current')
isnsDdPortalMemberPort = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 5), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdPortalMemberPort.setStatus('current')
isnsDdPortalMemberIsRegistered = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdPortalMemberIsRegistered.setStatus('current')
isnsDdFcPortMemberTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 4), )
if mibBuilder.loadTexts: isnsDdFcPortMemberTable.setStatus('current')
isnsDdFcPortMemberEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 4, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsDdId"), (0, "ISNS-MIB", "isnsDdFcPortMemberPortName"))
if mibBuilder.loadTexts: isnsDdFcPortMemberEntry.setStatus('current')
isnsDdFcPortMemberPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 4, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8))
if mibBuilder.loadTexts: isnsDdFcPortMemberPortName.setStatus('current')
isnsDdFcPortMemberIsRegistered = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 4, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsDdFcPortMemberIsRegistered.setStatus('current')
isnsReg = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 6))
isnsRegEntityInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1))
isnsRegEntityTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1), )
if mibBuilder.loadTexts: isnsRegEntityTable.setStatus('current')
isnsRegEntityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsRegEntityIndex"))
if mibBuilder.loadTexts: isnsRegEntityEntry.setStatus('current')
isnsRegEntityIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 1), IsnsEntityIndexIdOrZero().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: isnsRegEntityIndex.setStatus('current')
isnsRegEntityEID = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityEID.setStatus('current')
isnsRegEntityProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityProtocol.setStatus('current')
isnsRegEntityManagementAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityManagementAddressType.setStatus('current')
isnsRegEntityManagementAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityManagementAddress.setStatus('current')
isnsRegEntityTimestamp = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityTimestamp.setStatus('current')
isnsRegEntityVersionMin = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 254), ValueRangeConstraint(255, 255), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityVersionMin.setStatus('current')
isnsRegEntityVersionMax = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 254), ValueRangeConstraint(255, 255), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityVersionMax.setStatus('current')
isnsRegEntityRegistrationPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityRegistrationPeriod.setStatus('current')
isnsRegEntityNumObjectsTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2), )
if mibBuilder.loadTexts: isnsRegEntityNumObjectsTable.setStatus('current')
isnsRegEntityNumObjectsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsRegEntityIndex"))
if mibBuilder.loadTexts: isnsRegEntityNumObjectsEntry.setStatus('current')
isnsRegEntityInfoNumPortals = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityInfoNumPortals.setStatus('current')
isnsRegEntityInfoNumPortalGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityInfoNumPortalGroups.setStatus('current')
isnsRegEntityInfoNumIscsiNodes = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityInfoNumIscsiNodes.setStatus('current')
isnsRegEntityInfoNumFcPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityInfoNumFcPorts.setStatus('current')
isnsRegEntityInfoNumFcNodes = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegEntityInfoNumFcNodes.setStatus('current')
isnsRegPortalInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2))
isnsRegPortalTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1), )
if mibBuilder.loadTexts: isnsRegPortalTable.setStatus('current')
isnsRegPortalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsRegEntityIndex"), (0, "ISNS-MIB", "isnsRegPortalPortalIndex"))
if mibBuilder.loadTexts: isnsRegPortalEntry.setStatus('current')
isnsRegPortalPortalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 1), IsnsPortalIndexId())
if mibBuilder.loadTexts: isnsRegPortalPortalIndex.setStatus('current')
isnsRegPortalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalAddressType.setStatus('current')
isnsRegPortalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalAddress.setStatus('current')
isnsRegPortalPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 4), IsnsPortalPortTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalPortType.setStatus('current')
isnsRegPortalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 5), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalPort.setStatus('current')
isnsRegPortalSymbolicName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalSymbolicName.setStatus('current')
isnsRegPortalEsiInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalEsiInterval.setStatus('current')
isnsRegPortalEsiPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 8), IsnsPortalPortTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalEsiPortType.setStatus('current')
isnsRegPortalEsiPort = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 9), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalEsiPort.setStatus('current')
isnsRegPortalScnPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 10), IsnsPortalPortTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalScnPortType.setStatus('current')
isnsRegPortalScnPort = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 11), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalScnPort.setStatus('current')
isnsRegPortalSecurityInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 12), IsnsPortalSecurityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPortalSecurityInfo.setStatus('current')
isnsRegPortalGroupInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3))
isnsRegPgTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1), )
if mibBuilder.loadTexts: isnsRegPgTable.setStatus('current')
isnsRegPgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsRegEntityIndex"), (0, "ISNS-MIB", "isnsRegPgIndex"))
if mibBuilder.loadTexts: isnsRegPgEntry.setStatus('current')
isnsRegPgIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 1), IsnsPortalGroupIndexId())
if mibBuilder.loadTexts: isnsRegPgIndex.setStatus('current')
isnsRegPgIscsiNodeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 2), IsnsNodeIndexId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPgIscsiNodeIndex.setStatus('current')
isnsRegPgIscsiName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 223))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPgIscsiName.setStatus('current')
isnsRegPgPortalPortalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 4), IsnsPortalIndexId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPgPortalPortalIndex.setStatus('current')
isnsRegPgPortalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPgPortalAddressType.setStatus('current')
isnsRegPgPortalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPgPortalAddress.setStatus('current')
isnsRegPgPortalPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 7), IsnsPortalPortTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPgPortalPortType.setStatus('current')
isnsRegPgPortalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 8), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPgPortalPort.setStatus('current')
isnsRegPgPGT = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 9), IsnsPortalGroupTagIdOrNull()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegPgPGT.setStatus('current')
isnsRegIscsiNodeInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4))
isnsRegIscsiNodeTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1), )
if mibBuilder.loadTexts: isnsRegIscsiNodeTable.setStatus('current')
isnsRegIscsiNodeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsRegEntityIndex"), (0, "ISNS-MIB", "isnsRegIscsiNodeIndex"))
if mibBuilder.loadTexts: isnsRegIscsiNodeEntry.setStatus('current')
isnsRegIscsiNodeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 1), IsnsNodeIndexId())
if mibBuilder.loadTexts: isnsRegIscsiNodeIndex.setStatus('current')
isnsRegIscsiNodeName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 223))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegIscsiNodeName.setStatus('current')
isnsRegIscsiNodeType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 3), IsnsIscsiNodeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegIscsiNodeType.setStatus('current')
isnsRegIscsiNodeAlias = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegIscsiNodeAlias.setStatus('current')
isnsRegIscsiNodeScnTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 5), IsnsIscsiScnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegIscsiNodeScnTypes.setStatus('current')
isnsRegIscsiNodeWwnToken = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 6), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegIscsiNodeWwnToken.setStatus('current')
isnsRegIscsiNodeAuthMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegIscsiNodeAuthMethod.setStatus('current')
isnsRegFcNodeInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5))
isnsRegFcNodeTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1), )
if mibBuilder.loadTexts: isnsRegFcNodeTable.setStatus('current')
isnsRegFcNodeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsRegFcNodeWwnn"))
if mibBuilder.loadTexts: isnsRegFcNodeEntry.setStatus('current')
isnsRegFcNodeWwnn = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8))
if mibBuilder.loadTexts: isnsRegFcNodeWwnn.setStatus('current')
isnsRegFcNodeSymbolicName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcNodeSymbolicName.setStatus('current')
isnsRegFcNodeAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcNodeAddressType.setStatus('current')
isnsRegFcNodeAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcNodeAddress.setStatus('current')
isnsRegFcNodeIPA = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcNodeIPA.setStatus('current')
isnsRegFcNodeProxyIscsiName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 223))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcNodeProxyIscsiName.setStatus('current')
isnsRegFcNodeNumFcPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcNodeNumFcPorts.setStatus('current')
isnsRegFcPortTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2), )
if mibBuilder.loadTexts: isnsRegFcPortTable.setStatus('current')
isnsRegFcPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsRegEntityIndex"), (0, "ISNS-MIB", "isnsRegFcPortWwpn"))
if mibBuilder.loadTexts: isnsRegFcPortEntry.setStatus('current')
isnsRegFcPortWwpn = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8))
if mibBuilder.loadTexts: isnsRegFcPortWwpn.setStatus('current')
isnsRegFcPortID = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 2), FcAddressIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortID.setStatus('current')
isnsRegFcPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortType.setStatus('current')
isnsRegFcPortSymbolicName = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortSymbolicName.setStatus('current')
isnsRegFcPortFabricPortWwn = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 5), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortFabricPortWwn.setStatus('current')
isnsRegFcPortHA = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 6), FcAddressIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortHA.setStatus('current')
isnsRegFcPortAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortAddressType.setStatus('current')
isnsRegFcPortAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortAddress.setStatus('current')
isnsRegFcPortFcCos = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 9), IsnsFcClassOfServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortFcCos.setStatus('current')
isnsRegFcPortFc4Types = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortFc4Types.setStatus('current')
isnsRegFcPortFc4Descr = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(4, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortFc4Descr.setStatus('current')
isnsRegFcPortFc4Features = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortFc4Features.setStatus('current')
isnsRegFcPortScnTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 13), IsnsIfcpScnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortScnTypes.setStatus('current')
isnsRegFcPortRole = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 14), IsnsFcPortRoleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortRole.setStatus('current')
isnsRegFcPortFcNodeWwnn = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 15), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortFcNodeWwnn.setStatus('current')
isnsRegFcPortPpnWwn = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 16), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcPortPpnWwn.setStatus('current')
isnsRegFcNodePortTable = MibTable((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 3), )
if mibBuilder.loadTexts: isnsRegFcNodePortTable.setStatus('current')
isnsRegFcNodePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 3, 1), ).setIndexNames((0, "ISNS-MIB", "isnsServerIndex"), (0, "ISNS-MIB", "isnsRegFcNodeWwnn"), (0, "ISNS-MIB", "isnsRegFcPortWwpn"))
if mibBuilder.loadTexts: isnsRegFcNodePortEntry.setStatus('current')
isnsRegFcNodePortEntityIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 3, 1, 1), IsnsEntityIndexIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isnsRegFcNodePortEntityIndex.setStatus('current')
isnsNotificationsInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 1, 2))
isnsInstanceInfo = MibScalar((1, 3, 6, 1, 2, 1, 163, 1, 2, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isnsInstanceInfo.setStatus('current')
isnsAddressNotificationType = MibScalar((1, 3, 6, 1, 2, 1, 163, 1, 2, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isnsAddressNotificationType.setStatus('current')
isnsAddressNotification = MibScalar((1, 3, 6, 1, 2, 1, 163, 1, 2, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isnsAddressNotification.setStatus('current')
isnsTcpPortNotification = MibScalar((1, 3, 6, 1, 2, 1, 163, 1, 2, 4), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isnsTcpPortNotification.setStatus('current')
isnsUdpPortNotification = MibScalar((1, 3, 6, 1, 2, 1, 163, 1, 2, 5), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isnsUdpPortNotification.setStatus('current')
isnsServerStart = NotificationType((1, 3, 6, 1, 2, 1, 163, 0, 1)).setObjects(("ISNS-MIB", "isnsInstanceInfo"), ("ISNS-MIB", "isnsAddressNotificationType"), ("ISNS-MIB", "isnsAddressNotification"), ("ISNS-MIB", "isnsTcpPortNotification"), ("ISNS-MIB", "isnsUdpPortNotification"))
if mibBuilder.loadTexts: isnsServerStart.setStatus('current')
isnsServerShutdown = NotificationType((1, 3, 6, 1, 2, 1, 163, 0, 2)).setObjects(("ISNS-MIB", "isnsInstanceInfo"), ("ISNS-MIB", "isnsAddressNotificationType"), ("ISNS-MIB", "isnsAddressNotification"), ("ISNS-MIB", "isnsTcpPortNotification"), ("ISNS-MIB", "isnsUdpPortNotification"))
if mibBuilder.loadTexts: isnsServerShutdown.setStatus('current')
isnsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 2, 1))
isnsIscsiServerCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 163, 2, 1, 1)).setObjects(("ISNS-MIB", "isnsServerAttributesGroup"), ("ISNS-MIB", "isnsServerIscsiControlNodeGroup"), ("ISNS-MIB", "isnsServerIscsiDdsDdObjGroup"), ("ISNS-MIB", "isnsServerRegIscsiObjGroup"), ("ISNS-MIB", "isnsServerNumObjectsGroup"), ("ISNS-MIB", "isnsNotificationsObjGroup"), ("ISNS-MIB", "isnsServerNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsIscsiServerCompliance = isnsIscsiServerCompliance.setStatus('current')
isnsIfcpServerCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 163, 2, 1, 2)).setObjects(("ISNS-MIB", "isnsServerAttributesGroup"), ("ISNS-MIB", "isnsServerIfcpPortControlNodeGroup"), ("ISNS-MIB", "isnsServerIfcpDdsDdObjGroup"), ("ISNS-MIB", "isnsServerRegIfcpObjGroup"), ("ISNS-MIB", "isnsServerNumObjectsGroup"), ("ISNS-MIB", "isnsNotificationsObjGroup"), ("ISNS-MIB", "isnsServerNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsIfcpServerCompliance = isnsIfcpServerCompliance.setStatus('current')
isnsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 163, 2, 2))
isnsServerAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 1)).setObjects(("ISNS-MIB", "isnsServerName"), ("ISNS-MIB", "isnsServerIsnsVersion"), ("ISNS-MIB", "isnsServerVendorInfo"), ("ISNS-MIB", "isnsServerPhysicalIndex"), ("ISNS-MIB", "isnsServerTcpPort"), ("ISNS-MIB", "isnsServerUdpPort"), ("ISNS-MIB", "isnsServerDiscontinuityTime"), ("ISNS-MIB", "isnsServerRole"), ("ISNS-MIB", "isnsServerDiscoveryMethodsEnabled"), ("ISNS-MIB", "isnsServerDiscoveryMcGroupType"), ("ISNS-MIB", "isnsServerDiscoveryMcGroupAddress"), ("ISNS-MIB", "isnsServerEsiNonResponseThreshold"), ("ISNS-MIB", "isnsServerEnableControlNodeMgtScn"), ("ISNS-MIB", "isnsServerDefaultDdDdsStatus"), ("ISNS-MIB", "isnsServerUpdateDdDdsSupported"), ("ISNS-MIB", "isnsServerUpdateDdDdsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerAttributesGroup = isnsServerAttributesGroup.setStatus('current')
isnsServerNumObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 2)).setObjects(("ISNS-MIB", "isnsNumDds"), ("ISNS-MIB", "isnsNumDd"), ("ISNS-MIB", "isnsNumEntities"), ("ISNS-MIB", "isnsNumPortals"), ("ISNS-MIB", "isnsNumPortalGroups"), ("ISNS-MIB", "isnsNumIscsiNodes"), ("ISNS-MIB", "isnsNumFcPorts"), ("ISNS-MIB", "isnsNumFcNodes"), ("ISNS-MIB", "isnsRegEntityInfoNumPortals"), ("ISNS-MIB", "isnsRegEntityInfoNumPortalGroups"), ("ISNS-MIB", "isnsRegEntityInfoNumIscsiNodes"), ("ISNS-MIB", "isnsRegEntityInfoNumFcPorts"), ("ISNS-MIB", "isnsRegEntityInfoNumFcNodes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerNumObjectsGroup = isnsServerNumObjectsGroup.setStatus('current')
isnsServerIscsiControlNodeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 3)).setObjects(("ISNS-MIB", "isnsControlNodeIscsiNodeName"), ("ISNS-MIB", "isnsControlNodeIscsiIsRegistered"), ("ISNS-MIB", "isnsControlNodeIscsiRcvMgtSCN"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerIscsiControlNodeGroup = isnsServerIscsiControlNodeGroup.setStatus('current')
isnsServerIfcpPortControlNodeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 4)).setObjects(("ISNS-MIB", "isnsControlNodeFcPortIsRegistered"), ("ISNS-MIB", "isnsControlNodeFcPortRcvMgtSCN"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerIfcpPortControlNodeGroup = isnsServerIfcpPortControlNodeGroup.setStatus('current')
isnsServerIscsiDdsDdObjGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 5)).setObjects(("ISNS-MIB", "isnsDdsSymbolicName"), ("ISNS-MIB", "isnsDdsStatus"), ("ISNS-MIB", "isnsDdsMemberSymbolicName"), ("ISNS-MIB", "isnsDdSymbolicName"), ("ISNS-MIB", "isnsDdFeatures"), ("ISNS-MIB", "isnsDdIscsiMemberName"), ("ISNS-MIB", "isnsDdIscsiMemberIsRegistered"), ("ISNS-MIB", "isnsDdPortalMemberAddressType"), ("ISNS-MIB", "isnsDdPortalMemberAddress"), ("ISNS-MIB", "isnsDdPortalMemberPortType"), ("ISNS-MIB", "isnsDdPortalMemberPort"), ("ISNS-MIB", "isnsDdPortalMemberIsRegistered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerIscsiDdsDdObjGroup = isnsServerIscsiDdsDdObjGroup.setStatus('current')
isnsServerIfcpDdsDdObjGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 6)).setObjects(("ISNS-MIB", "isnsDdsSymbolicName"), ("ISNS-MIB", "isnsDdsStatus"), ("ISNS-MIB", "isnsDdSymbolicName"), ("ISNS-MIB", "isnsDdFeatures"), ("ISNS-MIB", "isnsDdPortalMemberAddressType"), ("ISNS-MIB", "isnsDdPortalMemberAddress"), ("ISNS-MIB", "isnsDdPortalMemberPortType"), ("ISNS-MIB", "isnsDdPortalMemberPort"), ("ISNS-MIB", "isnsDdPortalMemberIsRegistered"), ("ISNS-MIB", "isnsDdFcPortMemberIsRegistered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerIfcpDdsDdObjGroup = isnsServerIfcpDdsDdObjGroup.setStatus('current')
isnsServerRegIscsiObjGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 7)).setObjects(("ISNS-MIB", "isnsRegEntityEID"), ("ISNS-MIB", "isnsRegEntityProtocol"), ("ISNS-MIB", "isnsRegEntityManagementAddressType"), ("ISNS-MIB", "isnsRegEntityManagementAddress"), ("ISNS-MIB", "isnsRegEntityTimestamp"), ("ISNS-MIB", "isnsRegEntityVersionMin"), ("ISNS-MIB", "isnsRegEntityVersionMax"), ("ISNS-MIB", "isnsRegEntityRegistrationPeriod"), ("ISNS-MIB", "isnsRegEntityInfoNumPortals"), ("ISNS-MIB", "isnsRegEntityInfoNumPortalGroups"), ("ISNS-MIB", "isnsRegEntityInfoNumIscsiNodes"), ("ISNS-MIB", "isnsRegEntityInfoNumFcPorts"), ("ISNS-MIB", "isnsRegEntityInfoNumFcNodes"), ("ISNS-MIB", "isnsRegPortalAddressType"), ("ISNS-MIB", "isnsRegPortalAddress"), ("ISNS-MIB", "isnsRegPortalPortType"), ("ISNS-MIB", "isnsRegPortalPort"), ("ISNS-MIB", "isnsRegPortalSymbolicName"), ("ISNS-MIB", "isnsRegPortalEsiInterval"), ("ISNS-MIB", "isnsRegPortalEsiPortType"), ("ISNS-MIB", "isnsRegPortalEsiPort"), ("ISNS-MIB", "isnsRegPortalScnPortType"), ("ISNS-MIB", "isnsRegPortalScnPort"), ("ISNS-MIB", "isnsRegPortalSecurityInfo"), ("ISNS-MIB", "isnsRegPgIscsiNodeIndex"), ("ISNS-MIB", "isnsRegPgIscsiName"), ("ISNS-MIB", "isnsRegPgPortalPortalIndex"), ("ISNS-MIB", "isnsRegPgPortalAddressType"), ("ISNS-MIB", "isnsRegPgPortalAddress"), ("ISNS-MIB", "isnsRegPgPortalPortType"), ("ISNS-MIB", "isnsRegPgPortalPort"), ("ISNS-MIB", "isnsRegPgPGT"), ("ISNS-MIB", "isnsRegIscsiNodeName"), ("ISNS-MIB", "isnsRegIscsiNodeType"), ("ISNS-MIB", "isnsRegIscsiNodeAlias"), ("ISNS-MIB", "isnsRegIscsiNodeScnTypes"), ("ISNS-MIB", "isnsRegIscsiNodeWwnToken"), ("ISNS-MIB", "isnsRegIscsiNodeAuthMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerRegIscsiObjGroup = isnsServerRegIscsiObjGroup.setStatus('current')
isnsServerRegIfcpObjGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 8)).setObjects(("ISNS-MIB", "isnsRegEntityEID"), ("ISNS-MIB", "isnsRegEntityProtocol"), ("ISNS-MIB", "isnsRegEntityManagementAddressType"), ("ISNS-MIB", "isnsRegEntityManagementAddress"), ("ISNS-MIB", "isnsRegEntityTimestamp"), ("ISNS-MIB", "isnsRegEntityVersionMin"), ("ISNS-MIB", "isnsRegEntityVersionMax"), ("ISNS-MIB", "isnsRegEntityRegistrationPeriod"), ("ISNS-MIB", "isnsRegEntityInfoNumPortals"), ("ISNS-MIB", "isnsRegEntityInfoNumPortalGroups"), ("ISNS-MIB", "isnsRegEntityInfoNumIscsiNodes"), ("ISNS-MIB", "isnsRegEntityInfoNumFcPorts"), ("ISNS-MIB", "isnsRegEntityInfoNumFcNodes"), ("ISNS-MIB", "isnsRegPortalAddressType"), ("ISNS-MIB", "isnsRegPortalAddress"), ("ISNS-MIB", "isnsRegPortalPortType"), ("ISNS-MIB", "isnsRegPortalPort"), ("ISNS-MIB", "isnsRegPortalSymbolicName"), ("ISNS-MIB", "isnsRegPortalEsiInterval"), ("ISNS-MIB", "isnsRegPortalEsiPortType"), ("ISNS-MIB", "isnsRegPortalEsiPort"), ("ISNS-MIB", "isnsRegPortalScnPortType"), ("ISNS-MIB", "isnsRegPortalScnPort"), ("ISNS-MIB", "isnsRegPortalSecurityInfo"), ("ISNS-MIB", "isnsRegFcPortID"), ("ISNS-MIB", "isnsRegFcPortType"), ("ISNS-MIB", "isnsRegFcPortSymbolicName"), ("ISNS-MIB", "isnsRegFcPortFabricPortWwn"), ("ISNS-MIB", "isnsRegFcPortHA"), ("ISNS-MIB", "isnsRegFcPortAddressType"), ("ISNS-MIB", "isnsRegFcPortAddress"), ("ISNS-MIB", "isnsRegFcPortFcCos"), ("ISNS-MIB", "isnsRegFcPortFc4Types"), ("ISNS-MIB", "isnsRegFcPortFc4Descr"), ("ISNS-MIB", "isnsRegFcPortFc4Features"), ("ISNS-MIB", "isnsRegFcPortScnTypes"), ("ISNS-MIB", "isnsRegFcPortRole"), ("ISNS-MIB", "isnsRegFcPortFcNodeWwnn"), ("ISNS-MIB", "isnsRegFcPortPpnWwn"), ("ISNS-MIB", "isnsRegFcNodeSymbolicName"), ("ISNS-MIB", "isnsRegFcNodeAddressType"), ("ISNS-MIB", "isnsRegFcNodeAddress"), ("ISNS-MIB", "isnsRegFcNodeIPA"), ("ISNS-MIB", "isnsRegFcNodeProxyIscsiName"), ("ISNS-MIB", "isnsRegFcNodeNumFcPorts"), ("ISNS-MIB", "isnsRegFcNodePortEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerRegIfcpObjGroup = isnsServerRegIfcpObjGroup.setStatus('current')
isnsNotificationsObjGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 9)).setObjects(("ISNS-MIB", "isnsInstanceInfo"), ("ISNS-MIB", "isnsAddressNotificationType"), ("ISNS-MIB", "isnsAddressNotification"), ("ISNS-MIB", "isnsTcpPortNotification"), ("ISNS-MIB", "isnsUdpPortNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsNotificationsObjGroup = isnsNotificationsObjGroup.setStatus('current')
isnsServerNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 163, 2, 2, 10)).setObjects(("ISNS-MIB", "isnsServerStart"), ("ISNS-MIB", "isnsServerShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isnsServerNotificationGroup = isnsServerNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ISNS-MIB", isnsServerDiscoveryMcGroupType=isnsServerDiscoveryMcGroupType, isnsRegPgPGT=isnsRegPgPGT, isnsDdIscsiMemberTable=isnsDdIscsiMemberTable, isnsRegIscsiNodeAlias=isnsRegIscsiNodeAlias, IsnsIscsiScnType=IsnsIscsiScnType, isnsRegIscsiNodeEntry=isnsRegIscsiNodeEntry, isnsDdsSymbolicName=isnsDdsSymbolicName, IsnsDdsStatusType=IsnsDdsStatusType, isnsDdPortalMemberTable=isnsDdPortalMemberTable, isnsControlNodeFcPortWwpn=isnsControlNodeFcPortWwpn, isnsServerDiscontinuityTime=isnsServerDiscontinuityTime, isnsRegPortalEsiPort=isnsRegPortalEsiPort, isnsServerVendorInfo=isnsServerVendorInfo, isnsRegEntityInfoNumPortalGroups=isnsRegEntityInfoNumPortalGroups, isnsRegFcNodeAddress=isnsRegFcNodeAddress, isnsRegEntityVersionMax=isnsRegEntityVersionMax, isnsNumObjectsEntry=isnsNumObjectsEntry, isnsDdPortalMemberAddressType=isnsDdPortalMemberAddressType, isnsNumPortalGroups=isnsNumPortalGroups, isnsNumFcPorts=isnsNumFcPorts, isnsRegPgPortalPortalIndex=isnsRegPgPortalPortalIndex, isnsDdPortalMemberEntry=isnsDdPortalMemberEntry, IsnsFcPortRoleType=IsnsFcPortRoleType, isnsRegPortalPortType=isnsRegPortalPortType, isnsRegPortalEsiInterval=isnsRegPortalEsiInterval, isnsRegFcNodePortTable=isnsRegFcNodePortTable, isnsRegPortalScnPortType=isnsRegPortalScnPortType, isnsServerNumObjectsGroup=isnsServerNumObjectsGroup, isnsRegPortalEsiPortType=isnsRegPortalEsiPortType, isnsControlNodeIscsiTable=isnsControlNodeIscsiTable, isnsRegIscsiNodeWwnToken=isnsRegIscsiNodeWwnToken, isnsNumDd=isnsNumDd, isnsRegPgPortalPort=isnsRegPgPortalPort, isnsDdsStatus=isnsDdsStatus, isnsDdsMemberSymbolicName=isnsDdsMemberSymbolicName, isnsRegEntityEntry=isnsRegEntityEntry, isnsDdPortalMemberAddress=isnsDdPortalMemberAddress, IsnsPortalIndexId=IsnsPortalIndexId, isnsControlNodeIscsiNodeName=isnsControlNodeIscsiNodeName, IsnsIscsiNodeType=IsnsIscsiNodeType, isnsDdIscsiMemberIsRegistered=isnsDdIscsiMemberIsRegistered, isnsRegPgPortalPortType=isnsRegPgPortalPortType, isnsServerIndex=isnsServerIndex, isnsRegFcNodePortEntry=isnsRegFcNodePortEntry, isnsRegPortalEntry=isnsRegPortalEntry, IsnsDiscoveryDomainSetId=IsnsDiscoveryDomainSetId, isnsRegFcPortAddress=isnsRegFcPortAddress, isnsDdsId=isnsDdsId, isnsRegFcPortAddressType=isnsRegFcPortAddressType, isnsRegPgIscsiName=isnsRegPgIscsiName, isnsNumIscsiNodes=isnsNumIscsiNodes, isnsRegFcPortScnTypes=isnsRegFcPortScnTypes, isnsDdSymbolicName=isnsDdSymbolicName, isnsIscsiServerCompliance=isnsIscsiServerCompliance, isnsRegEntityNumObjectsTable=isnsRegEntityNumObjectsTable, isnsServerEnableControlNodeMgtScn=isnsServerEnableControlNodeMgtScn, IsnsPortalSecurityType=IsnsPortalSecurityType, isnsCompliances=isnsCompliances, isnsServerRegIscsiObjGroup=isnsServerRegIscsiObjGroup, isnsDdFcPortMemberIsRegistered=isnsDdFcPortMemberIsRegistered, isnsRegPgPortalAddressType=isnsRegPgPortalAddressType, isnsNumPortals=isnsNumPortals, IsnsPortalGroupTagIdOrNull=IsnsPortalGroupTagIdOrNull, isnsAddressNotificationType=isnsAddressNotificationType, IsnsPortalPortTypeId=IsnsPortalPortTypeId, isnsDdFcPortMemberTable=isnsDdFcPortMemberTable, isnsServerRegIfcpObjGroup=isnsServerRegIfcpObjGroup, isnsRegFcNodeIPA=isnsRegFcNodeIPA, isnsRegFcPortEntry=isnsRegFcPortEntry, isnsConformance=isnsConformance, isnsRegIscsiNodeScnTypes=isnsRegIscsiNodeScnTypes, isnsDdsMemberDdId=isnsDdsMemberDdId, isnsRegEntityManagementAddressType=isnsRegEntityManagementAddressType, isnsControlNodeIscsiIsRegistered=isnsControlNodeIscsiIsRegistered, isnsRegEntityRegistrationPeriod=isnsRegEntityRegistrationPeriod, isnsServerEsiNonResponseThreshold=isnsServerEsiNonResponseThreshold, isnsRegPgIscsiNodeIndex=isnsRegPgIscsiNodeIndex, IsnsDdDdsModificationType=IsnsDdDdsModificationType, isnsRegIscsiNodeName=isnsRegIscsiNodeName, isnsRegIscsiNodeIndex=isnsRegIscsiNodeIndex, isnsServerName=isnsServerName, isnsNotifications=isnsNotifications, isnsDdIscsiMemberEntry=isnsDdIscsiMemberEntry, isnsRegFcPortID=isnsRegFcPortID, isnsRegPortalScnPort=isnsRegPortalScnPort, isnsRegFcNodeEntry=isnsRegFcNodeEntry, isnsRegFcPortTable=isnsRegFcPortTable, isnsDdPortalMemberIndex=isnsDdPortalMemberIndex, isnsServerDiscoveryMethodsEnabled=isnsServerDiscoveryMethodsEnabled, isnsReg=isnsReg, isnsNumDds=isnsNumDds, isnsRegPortalSymbolicName=isnsRegPortalSymbolicName, isnsControlNodeIscsiRcvMgtSCN=isnsControlNodeIscsiRcvMgtSCN, isnsRegPortalPortalIndex=isnsRegPortalPortalIndex, isnsServerEntry=isnsServerEntry, isnsIfcpServerCompliance=isnsIfcpServerCompliance, isnsDdFeatures=isnsDdFeatures, isnsRegPgIndex=isnsRegPgIndex, isnsRegFcNodeTable=isnsRegFcNodeTable, isnsServerIfcpPortControlNodeGroup=isnsServerIfcpPortControlNodeGroup, IsnsIfcpScnType=IsnsIfcpScnType, isnsServerIsnsVersion=isnsServerIsnsVersion, isnsRegPortalPort=isnsRegPortalPort, isnsRegPgTable=isnsRegPgTable, isnsRegFcNodeInfo=isnsRegFcNodeInfo, isnsControlNodeFcPortTable=isnsControlNodeFcPortTable, isnsRegFcPortFc4Descr=isnsRegFcPortFc4Descr, isnsRegEntityInfoNumIscsiNodes=isnsRegEntityInfoNumIscsiNodes, isnsServerDiscoveryMcGroupAddress=isnsServerDiscoveryMcGroupAddress, isnsRegFcNodeNumFcPorts=isnsRegFcNodeNumFcPorts, isnsDdId=isnsDdId, isnsNotificationsObjGroup=isnsNotificationsObjGroup, isnsNumFcNodes=isnsNumFcNodes, isnsControlNodeFcPortIsRegistered=isnsControlNodeFcPortIsRegistered, isnsNotificationsInfo=isnsNotificationsInfo, isnsInstanceInfo=isnsInstanceInfo, isnsDdsMemberTable=isnsDdsMemberTable, isnsRegPortalTable=isnsRegPortalTable, IsnsDiscoveryDomainId=IsnsDiscoveryDomainId, isnsDdIscsiMemberIndex=isnsDdIscsiMemberIndex, isnsRegIscsiNodeTable=isnsRegIscsiNodeTable, isnsDdTable=isnsDdTable, isnsRegEntityTable=isnsRegEntityTable, isnsServerIscsiControlNodeGroup=isnsServerIscsiControlNodeGroup, isnsRegFcPortFc4Features=isnsRegFcPortFc4Features, isnsServerTable=isnsServerTable, isnsRegEntityVersionMin=isnsRegEntityVersionMin, isnsServerIscsiDdsDdObjGroup=isnsServerIscsiDdsDdObjGroup, IsnsPortalGroupIndexId=IsnsPortalGroupIndexId, isnsControlNodeIscsiEntry=isnsControlNodeIscsiEntry, isnsDdInfo=isnsDdInfo, isnsDdFcPortMemberPortName=isnsDdFcPortMemberPortName, isnsUdpPortNotification=isnsUdpPortNotification, isnsDdIscsiMemberName=isnsDdIscsiMemberName, isnsServerRole=isnsServerRole, isnsRegEntityProtocol=isnsRegEntityProtocol, isnsDdsInfo=isnsDdsInfo, isnsRegFcNodeProxyIscsiName=isnsRegFcNodeProxyIscsiName, isnsRegFcPortFcNodeWwnn=isnsRegFcPortFcNodeWwnn, isnsRegFcNodePortEntityIndex=isnsRegFcNodePortEntityIndex, isnsServerAttributesGroup=isnsServerAttributesGroup, isnsServerIfcpDdsDdObjGroup=isnsServerIfcpDdsDdObjGroup, IsnsFcClassOfServiceType=IsnsFcClassOfServiceType, isnsRegEntityNumObjectsEntry=isnsRegEntityNumObjectsEntry, isnsRegFcNodeSymbolicName=isnsRegFcNodeSymbolicName, isnsServerTcpPort=isnsServerTcpPort, isnsRegIscsiNodeAuthMethod=isnsRegIscsiNodeAuthMethod, isnsDdPortalMemberPort=isnsDdPortalMemberPort, isnsRegEntityInfo=isnsRegEntityInfo, isnsNumEntities=isnsNumEntities, isnsAddressNotification=isnsAddressNotification, isnsControlNodeFcPortRcvMgtSCN=isnsControlNodeFcPortRcvMgtSCN, isnsRegIscsiNodeType=isnsRegIscsiNodeType, isnsRegPortalAddressType=isnsRegPortalAddressType, isnsServerShutdown=isnsServerShutdown, isnsRegFcPortType=isnsRegFcPortType, IsnsNodeIndexId=IsnsNodeIndexId, isnsRegEntityIndex=isnsRegEntityIndex, isnsMIB=isnsMIB, isnsRegEntityInfoNumFcPorts=isnsRegEntityInfoNumFcPorts, isnsServerStart=isnsServerStart, isnsRegEntityTimestamp=isnsRegEntityTimestamp, isnsControlNodeFcPortEntry=isnsControlNodeFcPortEntry, isnsDdsEntry=isnsDdsEntry, isnsServerNotificationGroup=isnsServerNotificationGroup, isnsServerDefaultDdDdsStatus=isnsServerDefaultDdDdsStatus, isnsRegFcPortHA=isnsRegFcPortHA, isnsRegFcNodeAddressType=isnsRegFcNodeAddressType, isnsRegFcPortWwpn=isnsRegFcPortWwpn, isnsDdsTable=isnsDdsTable, isnsRegPgEntry=isnsRegPgEntry, isnsRegFcPortFc4Types=isnsRegFcPortFc4Types, isnsServerPhysicalIndex=isnsServerPhysicalIndex, isnsRegEntityManagementAddress=isnsRegEntityManagementAddress, isnsRegFcPortFabricPortWwn=isnsRegFcPortFabricPortWwn, isnsTcpPortNotification=isnsTcpPortNotification, isnsServerInfo=isnsServerInfo, isnsRegEntityInfoNumPortals=isnsRegEntityInfoNumPortals, isnsRegFcNodeWwnn=isnsRegFcNodeWwnn, isnsRegPortalSecurityInfo=isnsRegPortalSecurityInfo, isnsDdsMemberEntry=isnsDdsMemberEntry, isnsRegPortalGroupInfo=isnsRegPortalGroupInfo, IsnsEntityIndexIdOrZero=IsnsEntityIndexIdOrZero, isnsDdFcPortMemberEntry=isnsDdFcPortMemberEntry, isnsRegPortalAddress=isnsRegPortalAddress, isnsServerUpdateDdDdsEnabled=isnsServerUpdateDdDdsEnabled, isnsServerUpdateDdDdsSupported=isnsServerUpdateDdDdsSupported, isnsRegIscsiNodeInfo=isnsRegIscsiNodeInfo, isnsRegFcPortRole=isnsRegFcPortRole, PYSNMP_MODULE_ID=isnsMIB, isnsDdEntry=isnsDdEntry, isnsNumObjectsTable=isnsNumObjectsTable, isnsDdPortalMemberPortType=isnsDdPortalMemberPortType, isnsRegEntityEID=isnsRegEntityEID, isnsRegFcPortFcCos=isnsRegFcPortFcCos, isnsDdPortalMemberIsRegistered=isnsDdPortalMemberIsRegistered, isnsServerUdpPort=isnsServerUdpPort, isnsGroups=isnsGroups, isnsRegFcPortPpnWwn=isnsRegFcPortPpnWwn, isnsControlNodeInfo=isnsControlNodeInfo, isnsRegEntityInfoNumFcNodes=isnsRegEntityInfoNumFcNodes, isnsRegPgPortalAddress=isnsRegPgPortalAddress, isnsObjects=isnsObjects, IsnsSrvrDiscoveryMethodsType=IsnsSrvrDiscoveryMethodsType, isnsControlNodeIscsiNodeIndex=isnsControlNodeIscsiNodeIndex, isnsRegPortalInfo=isnsRegPortalInfo, IsnsDdFeatureType=IsnsDdFeatureType, isnsRegFcPortSymbolicName=isnsRegFcPortSymbolicName)
