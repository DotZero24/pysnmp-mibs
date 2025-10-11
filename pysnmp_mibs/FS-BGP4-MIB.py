# SNMP MIB module (FS-BGP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-BGP4-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:21 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InetAutonomousSystemNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAutonomousSystemNumber")

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

fsBgp4MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38)
)
if mibBuilder.loadTexts:
    fsBgp4MIB.setRevisions(
        ("2003-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSBgpID(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



# MIB Managed Objects in the order of their OIDs

_FsBgpBaseScalars_ObjectIdentity = ObjectIdentity
fsBgpBaseScalars = _FsBgpBaseScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1)
)
_FsBgpSupportedCapabilities_ObjectIdentity = ObjectIdentity
fsBgpSupportedCapabilities = _FsBgpSupportedCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 1)
)
_FsBgpCapabilitySupportAvailable_Type = TruthValue
_FsBgpCapabilitySupportAvailable_Object = MibScalar
fsBgpCapabilitySupportAvailable = _FsBgpCapabilitySupportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 1, 1),
    _FsBgpCapabilitySupportAvailable_Type()
)
fsBgpCapabilitySupportAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpCapabilitySupportAvailable.setStatus("current")
_FsBgpSupportedCapabilitiesTable_Object = MibTable
fsBgpSupportedCapabilitiesTable = _FsBgpSupportedCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsBgpSupportedCapabilitiesTable.setStatus("current")
_FsBgpSupportedCapabilitiesEntry_Object = MibTableRow
fsBgpSupportedCapabilitiesEntry = _FsBgpSupportedCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 1, 2, 1)
)
fsBgpSupportedCapabilitiesEntry.setIndexNames(
    (0, "FS-BGP4-MIB", "fsBgpSupportedCapabilityCode"),
)
if mibBuilder.loadTexts:
    fsBgpSupportedCapabilitiesEntry.setStatus("current")


class _FsBgpSupportedCapabilityCode_Type(Unsigned32):
    """Custom type fsBgpSupportedCapabilityCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsBgpSupportedCapabilityCode_Type.__name__ = "Unsigned32"
_FsBgpSupportedCapabilityCode_Object = MibTableColumn
fsBgpSupportedCapabilityCode = _FsBgpSupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 1, 2, 1, 1),
    _FsBgpSupportedCapabilityCode_Type()
)
fsBgpSupportedCapabilityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpSupportedCapabilityCode.setStatus("current")
_FsBgpSupportedCapability_Type = TruthValue
_FsBgpSupportedCapability_Object = MibTableColumn
fsBgpSupportedCapability = _FsBgpSupportedCapability_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 1, 2, 1, 2),
    _FsBgpSupportedCapability_Type()
)
fsBgpSupportedCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpSupportedCapability.setStatus("current")
_FsBgpBaseScalarExtensions_ObjectIdentity = ObjectIdentity
fsBgpBaseScalarExtensions = _FsBgpBaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 2)
)
_FsBgpBaseScalarRouteReflectExts_ObjectIdentity = ObjectIdentity
fsBgpBaseScalarRouteReflectExts = _FsBgpBaseScalarRouteReflectExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 2, 1)
)
_FsBgpRouteReflector_Type = TruthValue
_FsBgpRouteReflector_Object = MibScalar
fsBgpRouteReflector = _FsBgpRouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 2, 1, 1),
    _FsBgpRouteReflector_Type()
)
fsBgpRouteReflector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpRouteReflector.setStatus("current")
_FsBgpClusterId_Type = FSBgpID
_FsBgpClusterId_Object = MibScalar
fsBgpClusterId = _FsBgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 2, 1, 2),
    _FsBgpClusterId_Type()
)
fsBgpClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpClusterId.setStatus("current")
_FsBgpBaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
fsBgpBaseScalarASConfedExts = _FsBgpBaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 2, 2)
)
_FsBgpConfederationRouter_Type = TruthValue
_FsBgpConfederationRouter_Object = MibScalar
fsBgpConfederationRouter = _FsBgpConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 2, 2, 1),
    _FsBgpConfederationRouter_Type()
)
fsBgpConfederationRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpConfederationRouter.setStatus("current")
_FsBgpConfederationId_Type = InetAutonomousSystemNumber
_FsBgpConfederationId_Object = MibScalar
fsBgpConfederationId = _FsBgpConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 1, 2, 2, 2),
    _FsBgpConfederationId_Type()
)
fsBgpConfederationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpConfederationId.setStatus("current")
_FsBgpPeer_ObjectIdentity = ObjectIdentity
fsBgpPeer = _FsBgpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2)
)
_FsBgpPeerPrefixInfoTable_Object = MibTable
fsBgpPeerPrefixInfoTable = _FsBgpPeerPrefixInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 1)
)
if mibBuilder.loadTexts:
    fsBgpPeerPrefixInfoTable.setStatus("current")
_FsBgpPeerPrefixInfoEntry_Object = MibTableRow
fsBgpPeerPrefixInfoEntry = _FsBgpPeerPrefixInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsBgpPeerPrefixInfoEntry.setStatus("current")


class _FsBgpPeerPrefixLimit_Type(Unsigned32):
    """Custom type fsBgpPeerPrefixLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsBgpPeerPrefixLimit_Type.__name__ = "Unsigned32"
_FsBgpPeerPrefixLimit_Object = MibTableColumn
fsBgpPeerPrefixLimit = _FsBgpPeerPrefixLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 1, 1, 1),
    _FsBgpPeerPrefixLimit_Type()
)
fsBgpPeerPrefixLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerPrefixLimit.setStatus("deprecated")
_FsBgpPeerPrefixAccepted_Type = Counter32
_FsBgpPeerPrefixAccepted_Object = MibTableColumn
fsBgpPeerPrefixAccepted = _FsBgpPeerPrefixAccepted_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 1, 1, 2),
    _FsBgpPeerPrefixAccepted_Type()
)
fsBgpPeerPrefixAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerPrefixAccepted.setStatus("deprecated")
_FsBgpPeerPrefixAdvertised_Type = Counter32
_FsBgpPeerPrefixAdvertised_Object = MibTableColumn
fsBgpPeerPrefixAdvertised = _FsBgpPeerPrefixAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 1, 1, 3),
    _FsBgpPeerPrefixAdvertised_Type()
)
fsBgpPeerPrefixAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerPrefixAdvertised.setStatus("deprecated")
_FsBgpPeerCapabilities_ObjectIdentity = ObjectIdentity
fsBgpPeerCapabilities = _FsBgpPeerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2)
)
_FsBgpPeerCapsAnnouncedTable_Object = MibTable
fsBgpPeerCapsAnnouncedTable = _FsBgpPeerCapsAnnouncedTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fsBgpPeerCapsAnnouncedTable.setStatus("current")
_FsBgpPeerCapsAnnouncedEntry_Object = MibTableRow
fsBgpPeerCapsAnnouncedEntry = _FsBgpPeerCapsAnnouncedEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2, 1, 1)
)
fsBgpPeerCapsAnnouncedEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "FS-BGP4-MIB", "fsBgpPeerCapAnnouncedCode"),
)
if mibBuilder.loadTexts:
    fsBgpPeerCapsAnnouncedEntry.setStatus("current")


class _FsBgpPeerCapAnnouncedCode_Type(Unsigned32):
    """Custom type fsBgpPeerCapAnnouncedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsBgpPeerCapAnnouncedCode_Type.__name__ = "Unsigned32"
_FsBgpPeerCapAnnouncedCode_Object = MibTableColumn
fsBgpPeerCapAnnouncedCode = _FsBgpPeerCapAnnouncedCode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2, 1, 1, 1),
    _FsBgpPeerCapAnnouncedCode_Type()
)
fsBgpPeerCapAnnouncedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerCapAnnouncedCode.setStatus("current")


class _FsBgpPeerCapAnnouncedValue_Type(OctetString):
    """Custom type fsBgpPeerCapAnnouncedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsBgpPeerCapAnnouncedValue_Type.__name__ = "OctetString"
_FsBgpPeerCapAnnouncedValue_Object = MibTableColumn
fsBgpPeerCapAnnouncedValue = _FsBgpPeerCapAnnouncedValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2, 1, 1, 2),
    _FsBgpPeerCapAnnouncedValue_Type()
)
fsBgpPeerCapAnnouncedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerCapAnnouncedValue.setStatus("current")
_FsBgpPeerCapsReceivedTable_Object = MibTable
fsBgpPeerCapsReceivedTable = _FsBgpPeerCapsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fsBgpPeerCapsReceivedTable.setStatus("current")
_FsBgpPeerCapsReceivedEntry_Object = MibTableRow
fsBgpPeerCapsReceivedEntry = _FsBgpPeerCapsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2, 2, 1)
)
fsBgpPeerCapsReceivedEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "FS-BGP4-MIB", "fsBgpPeerCapReceivedCode"),
)
if mibBuilder.loadTexts:
    fsBgpPeerCapsReceivedEntry.setStatus("current")


class _FsBgpPeerCapReceivedCode_Type(Unsigned32):
    """Custom type fsBgpPeerCapReceivedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsBgpPeerCapReceivedCode_Type.__name__ = "Unsigned32"
_FsBgpPeerCapReceivedCode_Object = MibTableColumn
fsBgpPeerCapReceivedCode = _FsBgpPeerCapReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2, 2, 1, 1),
    _FsBgpPeerCapReceivedCode_Type()
)
fsBgpPeerCapReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerCapReceivedCode.setStatus("current")


class _FsBgpPeerCapReceivedValue_Type(OctetString):
    """Custom type fsBgpPeerCapReceivedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsBgpPeerCapReceivedValue_Type.__name__ = "OctetString"
_FsBgpPeerCapReceivedValue_Object = MibTableColumn
fsBgpPeerCapReceivedValue = _FsBgpPeerCapReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 2, 2, 1, 3),
    _FsBgpPeerCapReceivedValue_Type()
)
fsBgpPeerCapReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerCapReceivedValue.setStatus("current")
_FsBgpPeerExtensions_ObjectIdentity = ObjectIdentity
fsBgpPeerExtensions = _FsBgpPeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3)
)
_FsBgpPeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
fsBgpPeerRouteReflectionExts = _FsBgpPeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3, 1)
)
_FsBgpPeerReflectorClientTable_Object = MibTable
fsBgpPeerReflectorClientTable = _FsBgpPeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fsBgpPeerReflectorClientTable.setStatus("current")
_FsBgpPeerReflectorClientEntry_Object = MibTableRow
fsBgpPeerReflectorClientEntry = _FsBgpPeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsBgpPeerReflectorClientEntry.setStatus("current")


class _FsBgpPeerReflectorClient_Type(Integer32):
    """Custom type fsBgpPeerReflectorClient based on Integer32"""
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


_FsBgpPeerReflectorClient_Type.__name__ = "Integer32"
_FsBgpPeerReflectorClient_Object = MibTableColumn
fsBgpPeerReflectorClient = _FsBgpPeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3, 1, 1, 1, 1),
    _FsBgpPeerReflectorClient_Type()
)
fsBgpPeerReflectorClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerReflectorClient.setStatus("current")
_FsBgpPeerASConfederationExts_ObjectIdentity = ObjectIdentity
fsBgpPeerASConfederationExts = _FsBgpPeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3, 2)
)
_FsBgpPeerConfedMemberTable_Object = MibTable
fsBgpPeerConfedMemberTable = _FsBgpPeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fsBgpPeerConfedMemberTable.setStatus("current")
_FsBgpPeerConfedMemberEntry_Object = MibTableRow
fsBgpPeerConfedMemberEntry = _FsBgpPeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsBgpPeerConfedMemberEntry.setStatus("current")
_FsBgpPeerConfedMember_Type = TruthValue
_FsBgpPeerConfedMember_Object = MibTableColumn
fsBgpPeerConfedMember = _FsBgpPeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 2, 3, 2, 1, 1, 1),
    _FsBgpPeerConfedMember_Type()
)
fsBgpPeerConfedMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgpPeerConfedMember.setStatus("current")
_FsBgpConformance_ObjectIdentity = ObjectIdentity
fsBgpConformance = _FsBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 3)
)
_FsBgpMIBCompliances_ObjectIdentity = ObjectIdentity
fsBgpMIBCompliances = _FsBgpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 3, 1)
)
_FsBgpMIBGroups_ObjectIdentity = ObjectIdentity
fsBgpMIBGroups = _FsBgpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 38, 3, 2)
)
bgpPeerEntry.registerAugmentions(
    ("FS-BGP4-MIB",
     "fsBgpPeerPrefixInfoEntry")
)
fsBgpPeerPrefixInfoEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions(
    ("FS-BGP4-MIB",
     "fsBgpPeerReflectorClientEntry")
)
fsBgpPeerReflectorClientEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions(
    ("FS-BGP4-MIB",
     "fsBgpPeerConfedMemberEntry")
)
fsBgpPeerConfedMemberEntry.setIndexNames(*bgpPeerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-BGP4-MIB",
    **{"FSBgpID": FSBgpID,
       "fsBgp4MIB": fsBgp4MIB,
       "fsBgpBaseScalars": fsBgpBaseScalars,
       "fsBgpSupportedCapabilities": fsBgpSupportedCapabilities,
       "fsBgpCapabilitySupportAvailable": fsBgpCapabilitySupportAvailable,
       "fsBgpSupportedCapabilitiesTable": fsBgpSupportedCapabilitiesTable,
       "fsBgpSupportedCapabilitiesEntry": fsBgpSupportedCapabilitiesEntry,
       "fsBgpSupportedCapabilityCode": fsBgpSupportedCapabilityCode,
       "fsBgpSupportedCapability": fsBgpSupportedCapability,
       "fsBgpBaseScalarExtensions": fsBgpBaseScalarExtensions,
       "fsBgpBaseScalarRouteReflectExts": fsBgpBaseScalarRouteReflectExts,
       "fsBgpRouteReflector": fsBgpRouteReflector,
       "fsBgpClusterId": fsBgpClusterId,
       "fsBgpBaseScalarASConfedExts": fsBgpBaseScalarASConfedExts,
       "fsBgpConfederationRouter": fsBgpConfederationRouter,
       "fsBgpConfederationId": fsBgpConfederationId,
       "fsBgpPeer": fsBgpPeer,
       "fsBgpPeerPrefixInfoTable": fsBgpPeerPrefixInfoTable,
       "fsBgpPeerPrefixInfoEntry": fsBgpPeerPrefixInfoEntry,
       "fsBgpPeerPrefixLimit": fsBgpPeerPrefixLimit,
       "fsBgpPeerPrefixAccepted": fsBgpPeerPrefixAccepted,
       "fsBgpPeerPrefixAdvertised": fsBgpPeerPrefixAdvertised,
       "fsBgpPeerCapabilities": fsBgpPeerCapabilities,
       "fsBgpPeerCapsAnnouncedTable": fsBgpPeerCapsAnnouncedTable,
       "fsBgpPeerCapsAnnouncedEntry": fsBgpPeerCapsAnnouncedEntry,
       "fsBgpPeerCapAnnouncedCode": fsBgpPeerCapAnnouncedCode,
       "fsBgpPeerCapAnnouncedValue": fsBgpPeerCapAnnouncedValue,
       "fsBgpPeerCapsReceivedTable": fsBgpPeerCapsReceivedTable,
       "fsBgpPeerCapsReceivedEntry": fsBgpPeerCapsReceivedEntry,
       "fsBgpPeerCapReceivedCode": fsBgpPeerCapReceivedCode,
       "fsBgpPeerCapReceivedValue": fsBgpPeerCapReceivedValue,
       "fsBgpPeerExtensions": fsBgpPeerExtensions,
       "fsBgpPeerRouteReflectionExts": fsBgpPeerRouteReflectionExts,
       "fsBgpPeerReflectorClientTable": fsBgpPeerReflectorClientTable,
       "fsBgpPeerReflectorClientEntry": fsBgpPeerReflectorClientEntry,
       "fsBgpPeerReflectorClient": fsBgpPeerReflectorClient,
       "fsBgpPeerASConfederationExts": fsBgpPeerASConfederationExts,
       "fsBgpPeerConfedMemberTable": fsBgpPeerConfedMemberTable,
       "fsBgpPeerConfedMemberEntry": fsBgpPeerConfedMemberEntry,
       "fsBgpPeerConfedMember": fsBgpPeerConfedMember,
       "fsBgpConformance": fsBgpConformance,
       "fsBgpMIBCompliances": fsBgpMIBCompliances,
       "fsBgpMIBGroups": fsBgpMIBGroups}
)
