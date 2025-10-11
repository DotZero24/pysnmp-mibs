# SNMP MIB module (QTECH-BGP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-BGP4-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:00 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(bgpPeerEntry,
 bgpPeerRemoteAddr) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgpPeerEntry",
    "bgpPeerRemoteAddr")

(InetAutonomousSystemNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAutonomousSystemNumber")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechBgp4MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38)
)
if mibBuilder.loadTexts:
    qtechBgp4MIB.setRevisions(
        ("2003-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechBgpID(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



# MIB Managed Objects in the order of their OIDs

_QtechBgpBaseScalars_ObjectIdentity = ObjectIdentity
qtechBgpBaseScalars = _QtechBgpBaseScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1)
)
_QtechBgpSupportedCapabilities_ObjectIdentity = ObjectIdentity
qtechBgpSupportedCapabilities = _QtechBgpSupportedCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 1)
)
_QtechBgpCapabilitySupportAvailable_Type = TruthValue
_QtechBgpCapabilitySupportAvailable_Object = MibScalar
qtechBgpCapabilitySupportAvailable = _QtechBgpCapabilitySupportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 1, 1),
    _QtechBgpCapabilitySupportAvailable_Type()
)
qtechBgpCapabilitySupportAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpCapabilitySupportAvailable.setStatus("current")
_QtechBgpSupportedCapabilitiesTable_Object = MibTable
qtechBgpSupportedCapabilitiesTable = _QtechBgpSupportedCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qtechBgpSupportedCapabilitiesTable.setStatus("current")
_QtechBgpSupportedCapabilitiesEntry_Object = MibTableRow
qtechBgpSupportedCapabilitiesEntry = _QtechBgpSupportedCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 1, 2, 1)
)
qtechBgpSupportedCapabilitiesEntry.setIndexNames(
    (0, "QTECH-BGP4-MIB", "qtechBgpSupportedCapabilityCode"),
)
if mibBuilder.loadTexts:
    qtechBgpSupportedCapabilitiesEntry.setStatus("current")


class _QtechBgpSupportedCapabilityCode_Type(Unsigned32):
    """Custom type qtechBgpSupportedCapabilityCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechBgpSupportedCapabilityCode_Type.__name__ = "Unsigned32"
_QtechBgpSupportedCapabilityCode_Object = MibTableColumn
qtechBgpSupportedCapabilityCode = _QtechBgpSupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 1, 2, 1, 1),
    _QtechBgpSupportedCapabilityCode_Type()
)
qtechBgpSupportedCapabilityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpSupportedCapabilityCode.setStatus("current")
_QtechBgpSupportedCapability_Type = TruthValue
_QtechBgpSupportedCapability_Object = MibTableColumn
qtechBgpSupportedCapability = _QtechBgpSupportedCapability_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 1, 2, 1, 2),
    _QtechBgpSupportedCapability_Type()
)
qtechBgpSupportedCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpSupportedCapability.setStatus("current")
_QtechBgpBaseScalarExtensions_ObjectIdentity = ObjectIdentity
qtechBgpBaseScalarExtensions = _QtechBgpBaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 2)
)
_QtechBgpBaseScalarRouteReflectExts_ObjectIdentity = ObjectIdentity
qtechBgpBaseScalarRouteReflectExts = _QtechBgpBaseScalarRouteReflectExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 2, 1)
)
_QtechBgpRouteReflector_Type = TruthValue
_QtechBgpRouteReflector_Object = MibScalar
qtechBgpRouteReflector = _QtechBgpRouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 2, 1, 1),
    _QtechBgpRouteReflector_Type()
)
qtechBgpRouteReflector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpRouteReflector.setStatus("current")
_QtechBgpClusterId_Type = QtechBgpID
_QtechBgpClusterId_Object = MibScalar
qtechBgpClusterId = _QtechBgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 2, 1, 2),
    _QtechBgpClusterId_Type()
)
qtechBgpClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpClusterId.setStatus("current")
_QtechBgpBaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
qtechBgpBaseScalarASConfedExts = _QtechBgpBaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 2, 2)
)
_QtechBgpConfederationRouter_Type = TruthValue
_QtechBgpConfederationRouter_Object = MibScalar
qtechBgpConfederationRouter = _QtechBgpConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 2, 2, 1),
    _QtechBgpConfederationRouter_Type()
)
qtechBgpConfederationRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpConfederationRouter.setStatus("current")
_QtechBgpConfederationId_Type = InetAutonomousSystemNumber
_QtechBgpConfederationId_Object = MibScalar
qtechBgpConfederationId = _QtechBgpConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 1, 2, 2, 2),
    _QtechBgpConfederationId_Type()
)
qtechBgpConfederationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpConfederationId.setStatus("current")
_QtechBgpPeer_ObjectIdentity = ObjectIdentity
qtechBgpPeer = _QtechBgpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2)
)
_QtechBgpPeerPrefixInfoTable_Object = MibTable
qtechBgpPeerPrefixInfoTable = _QtechBgpPeerPrefixInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 1)
)
if mibBuilder.loadTexts:
    qtechBgpPeerPrefixInfoTable.setStatus("current")
_QtechBgpPeerPrefixInfoEntry_Object = MibTableRow
qtechBgpPeerPrefixInfoEntry = _QtechBgpPeerPrefixInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qtechBgpPeerPrefixInfoEntry.setStatus("current")


class _QtechBgpPeerPrefixLimit_Type(Unsigned32):
    """Custom type qtechBgpPeerPrefixLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechBgpPeerPrefixLimit_Type.__name__ = "Unsigned32"
_QtechBgpPeerPrefixLimit_Object = MibTableColumn
qtechBgpPeerPrefixLimit = _QtechBgpPeerPrefixLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 1, 1, 1),
    _QtechBgpPeerPrefixLimit_Type()
)
qtechBgpPeerPrefixLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerPrefixLimit.setStatus("deprecated")
_QtechBgpPeerPrefixAccepted_Type = Counter32
_QtechBgpPeerPrefixAccepted_Object = MibTableColumn
qtechBgpPeerPrefixAccepted = _QtechBgpPeerPrefixAccepted_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 1, 1, 2),
    _QtechBgpPeerPrefixAccepted_Type()
)
qtechBgpPeerPrefixAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerPrefixAccepted.setStatus("deprecated")
_QtechBgpPeerPrefixAdvertised_Type = Counter32
_QtechBgpPeerPrefixAdvertised_Object = MibTableColumn
qtechBgpPeerPrefixAdvertised = _QtechBgpPeerPrefixAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 1, 1, 3),
    _QtechBgpPeerPrefixAdvertised_Type()
)
qtechBgpPeerPrefixAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerPrefixAdvertised.setStatus("deprecated")
_QtechBgpPeerCapabilities_ObjectIdentity = ObjectIdentity
qtechBgpPeerCapabilities = _QtechBgpPeerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2)
)
_QtechBgpPeerCapsAnnouncedTable_Object = MibTable
qtechBgpPeerCapsAnnouncedTable = _QtechBgpPeerCapsAnnouncedTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2, 1)
)
if mibBuilder.loadTexts:
    qtechBgpPeerCapsAnnouncedTable.setStatus("current")
_QtechBgpPeerCapsAnnouncedEntry_Object = MibTableRow
qtechBgpPeerCapsAnnouncedEntry = _QtechBgpPeerCapsAnnouncedEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2, 1, 1)
)
qtechBgpPeerCapsAnnouncedEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "QTECH-BGP4-MIB", "qtechBgpPeerCapAnnouncedCode"),
)
if mibBuilder.loadTexts:
    qtechBgpPeerCapsAnnouncedEntry.setStatus("current")


class _QtechBgpPeerCapAnnouncedCode_Type(Unsigned32):
    """Custom type qtechBgpPeerCapAnnouncedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechBgpPeerCapAnnouncedCode_Type.__name__ = "Unsigned32"
_QtechBgpPeerCapAnnouncedCode_Object = MibTableColumn
qtechBgpPeerCapAnnouncedCode = _QtechBgpPeerCapAnnouncedCode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2, 1, 1, 1),
    _QtechBgpPeerCapAnnouncedCode_Type()
)
qtechBgpPeerCapAnnouncedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerCapAnnouncedCode.setStatus("current")


class _QtechBgpPeerCapAnnouncedValue_Type(OctetString):
    """Custom type qtechBgpPeerCapAnnouncedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechBgpPeerCapAnnouncedValue_Type.__name__ = "OctetString"
_QtechBgpPeerCapAnnouncedValue_Object = MibTableColumn
qtechBgpPeerCapAnnouncedValue = _QtechBgpPeerCapAnnouncedValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2, 1, 1, 2),
    _QtechBgpPeerCapAnnouncedValue_Type()
)
qtechBgpPeerCapAnnouncedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerCapAnnouncedValue.setStatus("current")
_QtechBgpPeerCapsReceivedTable_Object = MibTable
qtechBgpPeerCapsReceivedTable = _QtechBgpPeerCapsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2, 2)
)
if mibBuilder.loadTexts:
    qtechBgpPeerCapsReceivedTable.setStatus("current")
_QtechBgpPeerCapsReceivedEntry_Object = MibTableRow
qtechBgpPeerCapsReceivedEntry = _QtechBgpPeerCapsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2, 2, 1)
)
qtechBgpPeerCapsReceivedEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "QTECH-BGP4-MIB", "qtechBgpPeerCapReceivedCode"),
)
if mibBuilder.loadTexts:
    qtechBgpPeerCapsReceivedEntry.setStatus("current")


class _QtechBgpPeerCapReceivedCode_Type(Unsigned32):
    """Custom type qtechBgpPeerCapReceivedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechBgpPeerCapReceivedCode_Type.__name__ = "Unsigned32"
_QtechBgpPeerCapReceivedCode_Object = MibTableColumn
qtechBgpPeerCapReceivedCode = _QtechBgpPeerCapReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2, 2, 1, 1),
    _QtechBgpPeerCapReceivedCode_Type()
)
qtechBgpPeerCapReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerCapReceivedCode.setStatus("current")


class _QtechBgpPeerCapReceivedValue_Type(OctetString):
    """Custom type qtechBgpPeerCapReceivedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechBgpPeerCapReceivedValue_Type.__name__ = "OctetString"
_QtechBgpPeerCapReceivedValue_Object = MibTableColumn
qtechBgpPeerCapReceivedValue = _QtechBgpPeerCapReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 2, 2, 1, 3),
    _QtechBgpPeerCapReceivedValue_Type()
)
qtechBgpPeerCapReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerCapReceivedValue.setStatus("current")
_QtechBgpPeerExtensions_ObjectIdentity = ObjectIdentity
qtechBgpPeerExtensions = _QtechBgpPeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3)
)
_QtechBgpPeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
qtechBgpPeerRouteReflectionExts = _QtechBgpPeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3, 1)
)
_QtechBgpPeerReflectorClientTable_Object = MibTable
qtechBgpPeerReflectorClientTable = _QtechBgpPeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qtechBgpPeerReflectorClientTable.setStatus("current")
_QtechBgpPeerReflectorClientEntry_Object = MibTableRow
qtechBgpPeerReflectorClientEntry = _QtechBgpPeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechBgpPeerReflectorClientEntry.setStatus("current")


class _QtechBgpPeerReflectorClient_Type(Integer32):
    """Custom type qtechBgpPeerReflectorClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonClient", 0),
          ("client", 1),
          ("meshedClient", 2))
    )


_QtechBgpPeerReflectorClient_Type.__name__ = "Integer32"
_QtechBgpPeerReflectorClient_Object = MibTableColumn
qtechBgpPeerReflectorClient = _QtechBgpPeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3, 1, 1, 1, 1),
    _QtechBgpPeerReflectorClient_Type()
)
qtechBgpPeerReflectorClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerReflectorClient.setStatus("current")
_QtechBgpPeerASConfederationExts_ObjectIdentity = ObjectIdentity
qtechBgpPeerASConfederationExts = _QtechBgpPeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3, 2)
)
_QtechBgpPeerConfedMemberTable_Object = MibTable
qtechBgpPeerConfedMemberTable = _QtechBgpPeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    qtechBgpPeerConfedMemberTable.setStatus("current")
_QtechBgpPeerConfedMemberEntry_Object = MibTableRow
qtechBgpPeerConfedMemberEntry = _QtechBgpPeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qtechBgpPeerConfedMemberEntry.setStatus("current")
_QtechBgpPeerConfedMember_Type = TruthValue
_QtechBgpPeerConfedMember_Object = MibTableColumn
qtechBgpPeerConfedMember = _QtechBgpPeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 2, 3, 2, 1, 1, 1),
    _QtechBgpPeerConfedMember_Type()
)
qtechBgpPeerConfedMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBgpPeerConfedMember.setStatus("current")
_QtechBgpConformance_ObjectIdentity = ObjectIdentity
qtechBgpConformance = _QtechBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 3)
)
_QtechBgpMIBCompliances_ObjectIdentity = ObjectIdentity
qtechBgpMIBCompliances = _QtechBgpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 3, 1)
)
_QtechBgpMIBGroups_ObjectIdentity = ObjectIdentity
qtechBgpMIBGroups = _QtechBgpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 38, 3, 2)
)
bgpPeerEntry.registerAugmentions(
    ("QTECH-BGP4-MIB",
     "qtechBgpPeerPrefixInfoEntry")
)
qtechBgpPeerPrefixInfoEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions(
    ("QTECH-BGP4-MIB",
     "qtechBgpPeerReflectorClientEntry")
)
qtechBgpPeerReflectorClientEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions(
    ("QTECH-BGP4-MIB",
     "qtechBgpPeerConfedMemberEntry")
)
qtechBgpPeerConfedMemberEntry.setIndexNames(*bgpPeerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-BGP4-MIB",
    **{"QtechBgpID": QtechBgpID,
       "qtechBgp4MIB": qtechBgp4MIB,
       "qtechBgpBaseScalars": qtechBgpBaseScalars,
       "qtechBgpSupportedCapabilities": qtechBgpSupportedCapabilities,
       "qtechBgpCapabilitySupportAvailable": qtechBgpCapabilitySupportAvailable,
       "qtechBgpSupportedCapabilitiesTable": qtechBgpSupportedCapabilitiesTable,
       "qtechBgpSupportedCapabilitiesEntry": qtechBgpSupportedCapabilitiesEntry,
       "qtechBgpSupportedCapabilityCode": qtechBgpSupportedCapabilityCode,
       "qtechBgpSupportedCapability": qtechBgpSupportedCapability,
       "qtechBgpBaseScalarExtensions": qtechBgpBaseScalarExtensions,
       "qtechBgpBaseScalarRouteReflectExts": qtechBgpBaseScalarRouteReflectExts,
       "qtechBgpRouteReflector": qtechBgpRouteReflector,
       "qtechBgpClusterId": qtechBgpClusterId,
       "qtechBgpBaseScalarASConfedExts": qtechBgpBaseScalarASConfedExts,
       "qtechBgpConfederationRouter": qtechBgpConfederationRouter,
       "qtechBgpConfederationId": qtechBgpConfederationId,
       "qtechBgpPeer": qtechBgpPeer,
       "qtechBgpPeerPrefixInfoTable": qtechBgpPeerPrefixInfoTable,
       "qtechBgpPeerPrefixInfoEntry": qtechBgpPeerPrefixInfoEntry,
       "qtechBgpPeerPrefixLimit": qtechBgpPeerPrefixLimit,
       "qtechBgpPeerPrefixAccepted": qtechBgpPeerPrefixAccepted,
       "qtechBgpPeerPrefixAdvertised": qtechBgpPeerPrefixAdvertised,
       "qtechBgpPeerCapabilities": qtechBgpPeerCapabilities,
       "qtechBgpPeerCapsAnnouncedTable": qtechBgpPeerCapsAnnouncedTable,
       "qtechBgpPeerCapsAnnouncedEntry": qtechBgpPeerCapsAnnouncedEntry,
       "qtechBgpPeerCapAnnouncedCode": qtechBgpPeerCapAnnouncedCode,
       "qtechBgpPeerCapAnnouncedValue": qtechBgpPeerCapAnnouncedValue,
       "qtechBgpPeerCapsReceivedTable": qtechBgpPeerCapsReceivedTable,
       "qtechBgpPeerCapsReceivedEntry": qtechBgpPeerCapsReceivedEntry,
       "qtechBgpPeerCapReceivedCode": qtechBgpPeerCapReceivedCode,
       "qtechBgpPeerCapReceivedValue": qtechBgpPeerCapReceivedValue,
       "qtechBgpPeerExtensions": qtechBgpPeerExtensions,
       "qtechBgpPeerRouteReflectionExts": qtechBgpPeerRouteReflectionExts,
       "qtechBgpPeerReflectorClientTable": qtechBgpPeerReflectorClientTable,
       "qtechBgpPeerReflectorClientEntry": qtechBgpPeerReflectorClientEntry,
       "qtechBgpPeerReflectorClient": qtechBgpPeerReflectorClient,
       "qtechBgpPeerASConfederationExts": qtechBgpPeerASConfederationExts,
       "qtechBgpPeerConfedMemberTable": qtechBgpPeerConfedMemberTable,
       "qtechBgpPeerConfedMemberEntry": qtechBgpPeerConfedMemberEntry,
       "qtechBgpPeerConfedMember": qtechBgpPeerConfedMember,
       "qtechBgpConformance": qtechBgpConformance,
       "qtechBgpMIBCompliances": qtechBgpMIBCompliances,
       "qtechBgpMIBGroups": qtechBgpMIBGroups}
)
