# SNMP MIB module (QTECH-DHCPv6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-DHCPv6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:13 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

qtechDhcpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45)
)
if mibBuilder.loadTexts:
    qtechDhcpv6MIB.setRevisions(
        ("2009-03-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechDhcpv6MIBObjects_ObjectIdentity = ObjectIdentity
qtechDhcpv6MIBObjects = _QtechDhcpv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1)
)
if mibBuilder.loadTexts:
    qtechDhcpv6MIBObjects.setStatus("current")
_QtechDhcpv6ServerMIBObjects_ObjectIdentity = ObjectIdentity
qtechDhcpv6ServerMIBObjects = _QtechDhcpv6ServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1)
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerMIBObjects.setStatus("current")
_QtechDhcpv6ServerCounters_ObjectIdentity = ObjectIdentity
qtechDhcpv6ServerCounters = _QtechDhcpv6ServerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerCounters.setStatus("current")
_QtechDhcpv6ServerHCountSolicits_Type = Counter64
_QtechDhcpv6ServerHCountSolicits_Object = MibScalar
qtechDhcpv6ServerHCountSolicits = _QtechDhcpv6ServerHCountSolicits_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 1),
    _QtechDhcpv6ServerHCountSolicits_Type()
)
qtechDhcpv6ServerHCountSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountSolicits.setStatus("current")
_QtechDhcpv6ServerHCountRequests_Type = Counter64
_QtechDhcpv6ServerHCountRequests_Object = MibScalar
qtechDhcpv6ServerHCountRequests = _QtechDhcpv6ServerHCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 2),
    _QtechDhcpv6ServerHCountRequests_Type()
)
qtechDhcpv6ServerHCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountRequests.setStatus("current")
_QtechDhcpv6ServerHCountRenews_Type = Counter64
_QtechDhcpv6ServerHCountRenews_Object = MibScalar
qtechDhcpv6ServerHCountRenews = _QtechDhcpv6ServerHCountRenews_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 3),
    _QtechDhcpv6ServerHCountRenews_Type()
)
qtechDhcpv6ServerHCountRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountRenews.setStatus("current")
_QtechDhcpv6ServerHCountDeclines_Type = Counter64
_QtechDhcpv6ServerHCountDeclines_Object = MibScalar
qtechDhcpv6ServerHCountDeclines = _QtechDhcpv6ServerHCountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 4),
    _QtechDhcpv6ServerHCountDeclines_Type()
)
qtechDhcpv6ServerHCountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountDeclines.setStatus("current")
_QtechDhcpv6ServerHCountReleases_Type = Counter64
_QtechDhcpv6ServerHCountReleases_Object = MibScalar
qtechDhcpv6ServerHCountReleases = _QtechDhcpv6ServerHCountReleases_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 5),
    _QtechDhcpv6ServerHCountReleases_Type()
)
qtechDhcpv6ServerHCountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountReleases.setStatus("current")
_QtechDhcpv6ServerHCountInforms_Type = Counter64
_QtechDhcpv6ServerHCountInforms_Object = MibScalar
qtechDhcpv6ServerHCountInforms = _QtechDhcpv6ServerHCountInforms_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 6),
    _QtechDhcpv6ServerHCountInforms_Type()
)
qtechDhcpv6ServerHCountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountInforms.setStatus("current")
_QtechDhcpv6ServerHCountConfirms_Type = Counter64
_QtechDhcpv6ServerHCountConfirms_Object = MibScalar
qtechDhcpv6ServerHCountConfirms = _QtechDhcpv6ServerHCountConfirms_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 7),
    _QtechDhcpv6ServerHCountConfirms_Type()
)
qtechDhcpv6ServerHCountConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountConfirms.setStatus("current")
_QtechDhcpv6ServerHCountRebinds_Type = Counter64
_QtechDhcpv6ServerHCountRebinds_Object = MibScalar
qtechDhcpv6ServerHCountRebinds = _QtechDhcpv6ServerHCountRebinds_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 8),
    _QtechDhcpv6ServerHCountRebinds_Type()
)
qtechDhcpv6ServerHCountRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountRebinds.setStatus("current")
_QtechDhcpv6ServerHCountAdvertises_Type = Counter64
_QtechDhcpv6ServerHCountAdvertises_Object = MibScalar
qtechDhcpv6ServerHCountAdvertises = _QtechDhcpv6ServerHCountAdvertises_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 9),
    _QtechDhcpv6ServerHCountAdvertises_Type()
)
qtechDhcpv6ServerHCountAdvertises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountAdvertises.setStatus("current")
_QtechDhcpv6ServerHCountSuccReplies_Type = Counter64
_QtechDhcpv6ServerHCountSuccReplies_Object = MibScalar
qtechDhcpv6ServerHCountSuccReplies = _QtechDhcpv6ServerHCountSuccReplies_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 10),
    _QtechDhcpv6ServerHCountSuccReplies_Type()
)
qtechDhcpv6ServerHCountSuccReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountSuccReplies.setStatus("current")
_QtechDhcpv6ServerHCountFailReplies_Type = Counter64
_QtechDhcpv6ServerHCountFailReplies_Object = MibScalar
qtechDhcpv6ServerHCountFailReplies = _QtechDhcpv6ServerHCountFailReplies_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 11),
    _QtechDhcpv6ServerHCountFailReplies_Type()
)
qtechDhcpv6ServerHCountFailReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountFailReplies.setStatus("current")
_QtechDhcpv6ServerHCountInPkts_Type = Counter64
_QtechDhcpv6ServerHCountInPkts_Object = MibScalar
qtechDhcpv6ServerHCountInPkts = _QtechDhcpv6ServerHCountInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 12),
    _QtechDhcpv6ServerHCountInPkts_Type()
)
qtechDhcpv6ServerHCountInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountInPkts.setStatus("current")
_QtechDhcpv6ServerHCountOutPkts_Type = Counter64
_QtechDhcpv6ServerHCountOutPkts_Object = MibScalar
qtechDhcpv6ServerHCountOutPkts = _QtechDhcpv6ServerHCountOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 13),
    _QtechDhcpv6ServerHCountOutPkts_Type()
)
qtechDhcpv6ServerHCountOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountOutPkts.setStatus("current")
_QtechDhcpv6ServerHCountDroppedUnknown_Type = Counter64
_QtechDhcpv6ServerHCountDroppedUnknown_Object = MibScalar
qtechDhcpv6ServerHCountDroppedUnknown = _QtechDhcpv6ServerHCountDroppedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 14),
    _QtechDhcpv6ServerHCountDroppedUnknown_Type()
)
qtechDhcpv6ServerHCountDroppedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountDroppedUnknown.setStatus("current")
_QtechDhcpv6ServerHCountDroppedError_Type = Counter64
_QtechDhcpv6ServerHCountDroppedError_Object = MibScalar
qtechDhcpv6ServerHCountDroppedError = _QtechDhcpv6ServerHCountDroppedError_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 15),
    _QtechDhcpv6ServerHCountDroppedError_Type()
)
qtechDhcpv6ServerHCountDroppedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountDroppedError.setStatus("current")
_QtechDhcpv6ServerHCountRelayforward_Type = Counter64
_QtechDhcpv6ServerHCountRelayforward_Object = MibScalar
qtechDhcpv6ServerHCountRelayforward = _QtechDhcpv6ServerHCountRelayforward_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 16),
    _QtechDhcpv6ServerHCountRelayforward_Type()
)
qtechDhcpv6ServerHCountRelayforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountRelayforward.setStatus("current")
_QtechDhcpv6ServerHCountRelayreply_Type = Counter64
_QtechDhcpv6ServerHCountRelayreply_Object = MibScalar
qtechDhcpv6ServerHCountRelayreply = _QtechDhcpv6ServerHCountRelayreply_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 17),
    _QtechDhcpv6ServerHCountRelayreply_Type()
)
qtechDhcpv6ServerHCountRelayreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountRelayreply.setStatus("current")
_QtechDhcpv6ServerHCountReqtimes_Type = Counter64
_QtechDhcpv6ServerHCountReqtimes_Object = MibScalar
qtechDhcpv6ServerHCountReqtimes = _QtechDhcpv6ServerHCountReqtimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 18),
    _QtechDhcpv6ServerHCountReqtimes_Type()
)
qtechDhcpv6ServerHCountReqtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountReqtimes.setStatus("current")
_QtechDhcpv6ServerHCountReqSuctimes_Type = Counter64
_QtechDhcpv6ServerHCountReqSuctimes_Object = MibScalar
qtechDhcpv6ServerHCountReqSuctimes = _QtechDhcpv6ServerHCountReqSuctimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 1, 19),
    _QtechDhcpv6ServerHCountReqSuctimes_Type()
)
qtechDhcpv6ServerHCountReqSuctimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerHCountReqSuctimes.setStatus("current")
_QtechDhcpv6ServerConfiguration_ObjectIdentity = ObjectIdentity
qtechDhcpv6ServerConfiguration = _QtechDhcpv6ServerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerConfiguration.setStatus("current")
_QtechDhcpv6ServerNumBindings_Type = Counter32
_QtechDhcpv6ServerNumBindings_Object = MibScalar
qtechDhcpv6ServerNumBindings = _QtechDhcpv6ServerNumBindings_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 1),
    _QtechDhcpv6ServerNumBindings_Type()
)
qtechDhcpv6ServerNumBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerNumBindings.setStatus("current")
_QtechDhcpv6ServerBindingsTable_Object = MibTable
qtechDhcpv6ServerBindingsTable = _QtechDhcpv6ServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsTable.setStatus("current")
_QtechDhcpv6ServerBindingsEntry_Object = MibTableRow
qtechDhcpv6ServerBindingsEntry = _QtechDhcpv6ServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1)
)
qtechDhcpv6ServerBindingsEntry.setIndexNames(
    (0, "QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsPoolName"),
    (0, "QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsClientDuid"),
    (0, "QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsIaType"),
    (0, "QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsIaId"),
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsEntry.setStatus("current")


class _QtechDhcpv6ServerBindingsPoolName_Type(DisplayString):
    """Custom type qtechDhcpv6ServerBindingsPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechDhcpv6ServerBindingsPoolName_Type.__name__ = "DisplayString"
_QtechDhcpv6ServerBindingsPoolName_Object = MibTableColumn
qtechDhcpv6ServerBindingsPoolName = _QtechDhcpv6ServerBindingsPoolName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 1),
    _QtechDhcpv6ServerBindingsPoolName_Type()
)
qtechDhcpv6ServerBindingsPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsPoolName.setStatus("current")


class _QtechDhcpv6ServerBindingsClientDuid_Type(OctetString):
    """Custom type qtechDhcpv6ServerBindingsClientDuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_QtechDhcpv6ServerBindingsClientDuid_Type.__name__ = "OctetString"
_QtechDhcpv6ServerBindingsClientDuid_Object = MibTableColumn
qtechDhcpv6ServerBindingsClientDuid = _QtechDhcpv6ServerBindingsClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 2),
    _QtechDhcpv6ServerBindingsClientDuid_Type()
)
qtechDhcpv6ServerBindingsClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsClientDuid.setStatus("current")


class _QtechDhcpv6ServerBindingsIaType_Type(Integer32):
    """Custom type qtechDhcpv6ServerBindingsIaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iana", 1),
          ("iata", 2),
          ("iapd", 3))
    )


_QtechDhcpv6ServerBindingsIaType_Type.__name__ = "Integer32"
_QtechDhcpv6ServerBindingsIaType_Object = MibTableColumn
qtechDhcpv6ServerBindingsIaType = _QtechDhcpv6ServerBindingsIaType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 3),
    _QtechDhcpv6ServerBindingsIaType_Type()
)
qtechDhcpv6ServerBindingsIaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsIaType.setStatus("current")
_QtechDhcpv6ServerBindingsIaId_Type = Unsigned32
_QtechDhcpv6ServerBindingsIaId_Object = MibTableColumn
qtechDhcpv6ServerBindingsIaId = _QtechDhcpv6ServerBindingsIaId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 4),
    _QtechDhcpv6ServerBindingsIaId_Type()
)
qtechDhcpv6ServerBindingsIaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsIaId.setStatus("current")
_QtechDhcpv6ServerBindingsAddress_Type = Ipv6Address
_QtechDhcpv6ServerBindingsAddress_Object = MibTableColumn
qtechDhcpv6ServerBindingsAddress = _QtechDhcpv6ServerBindingsAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 5),
    _QtechDhcpv6ServerBindingsAddress_Type()
)
qtechDhcpv6ServerBindingsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsAddress.setStatus("current")
_QtechDhcpv6ServerBindingsPrefix_Type = Ipv6AddressPrefix
_QtechDhcpv6ServerBindingsPrefix_Object = MibTableColumn
qtechDhcpv6ServerBindingsPrefix = _QtechDhcpv6ServerBindingsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 6),
    _QtechDhcpv6ServerBindingsPrefix_Type()
)
qtechDhcpv6ServerBindingsPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsPrefix.setStatus("current")


class _QtechDhcpv6ServerBindingsPrefixLength_Type(Integer32):
    """Custom type qtechDhcpv6ServerBindingsPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_QtechDhcpv6ServerBindingsPrefixLength_Type.__name__ = "Integer32"
_QtechDhcpv6ServerBindingsPrefixLength_Object = MibTableColumn
qtechDhcpv6ServerBindingsPrefixLength = _QtechDhcpv6ServerBindingsPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 7),
    _QtechDhcpv6ServerBindingsPrefixLength_Type()
)
qtechDhcpv6ServerBindingsPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsPrefixLength.setStatus("current")
_QtechDhcpv6ServerBindingsDuration_Type = Unsigned32
_QtechDhcpv6ServerBindingsDuration_Object = MibTableColumn
qtechDhcpv6ServerBindingsDuration = _QtechDhcpv6ServerBindingsDuration_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 8),
    _QtechDhcpv6ServerBindingsDuration_Type()
)
qtechDhcpv6ServerBindingsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsDuration.setStatus("current")
_QtechDhcpv6ServerBindingsIfIndex_Type = InterfaceIndex
_QtechDhcpv6ServerBindingsIfIndex_Object = MibTableColumn
qtechDhcpv6ServerBindingsIfIndex = _QtechDhcpv6ServerBindingsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 9),
    _QtechDhcpv6ServerBindingsIfIndex_Type()
)
qtechDhcpv6ServerBindingsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerBindingsIfIndex.setStatus("current")
_QtechDhcpv6ServerPoolTable_Object = MibTable
qtechDhcpv6ServerPoolTable = _QtechDhcpv6ServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerPoolTable.setStatus("current")
_QtechDhcpv6ServerPoolEntry_Object = MibTableRow
qtechDhcpv6ServerPoolEntry = _QtechDhcpv6ServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1)
)
qtechDhcpv6ServerPoolEntry.setIndexNames(
    (0, "QTECH-DHCPv6-MIB", "qtechDhcpv6ServerIPPoolName"),
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerPoolEntry.setStatus("current")


class _QtechDhcpv6ServerIPPoolName_Type(DisplayString):
    """Custom type qtechDhcpv6ServerIPPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechDhcpv6ServerIPPoolName_Type.__name__ = "DisplayString"
_QtechDhcpv6ServerIPPoolName_Object = MibTableColumn
qtechDhcpv6ServerIPPoolName = _QtechDhcpv6ServerIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 1),
    _QtechDhcpv6ServerIPPoolName_Type()
)
qtechDhcpv6ServerIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerIPPoolName.setStatus("current")
_QtechDhcpv6ServerDHCPIPPoolUsage_Type = Unsigned32
_QtechDhcpv6ServerDHCPIPPoolUsage_Object = MibTableColumn
qtechDhcpv6ServerDHCPIPPoolUsage = _QtechDhcpv6ServerDHCPIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 2),
    _QtechDhcpv6ServerDHCPIPPoolUsage_Type()
)
qtechDhcpv6ServerDHCPIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpv6ServerDHCPIPPoolUsage.setStatus("current")
_QtechDhcpv6MIBConformance_ObjectIdentity = ObjectIdentity
qtechDhcpv6MIBConformance = _QtechDhcpv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 2)
)
if mibBuilder.loadTexts:
    qtechDhcpv6MIBConformance.setStatus("current")
_QtechDhcpv6MIBCompliances_ObjectIdentity = ObjectIdentity
qtechDhcpv6MIBCompliances = _QtechDhcpv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 2, 1)
)
_QtechDhcpv6MIBGroups_ObjectIdentity = ObjectIdentity
qtechDhcpv6MIBGroups = _QtechDhcpv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 2, 2)
)

# Managed Objects groups

qtechDhcpv6ServerCountersObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 2, 2, 1)
)
qtechDhcpv6ServerCountersObjects.setObjects(
      *(("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountSolicits"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountRenews"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountDeclines"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountReleases"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountInforms"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountConfirms"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountRebinds"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountAdvertises"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountSuccReplies"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountFailReplies"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountInPkts"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountOutPkts"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountDroppedUnknown"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountDroppedError"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountRelayforward"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountRelayreply"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountReqtimes"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerHCountReqSuctimes"))
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerCountersObjects.setStatus("current")

qtechDhcpv6ServerConfigurationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 2, 2, 2)
)
qtechDhcpv6ServerConfigurationObjects.setObjects(
      *(("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerNumBindings"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsPoolName"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsClientDuid"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsIaType"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsIaId"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsAddress"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsPrefix"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsPrefixLength"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsDuration"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerBindingsIfIndex"))
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerConfigurationObjects.setStatus("current")

qtechDhcpv6ServerPoolTableObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 2, 2, 3)
)
qtechDhcpv6ServerPoolTableObjects.setObjects(
      *(("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerIPPoolName"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerDHCPIPPoolUsage"))
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerPoolTableObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechDhcpv6ServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 45, 2, 1, 1)
)
qtechDhcpv6ServerCompliance.setObjects(
      *(("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerCountersObjects"),
        ("QTECH-DHCPv6-MIB", "qtechDhcpv6ServerConfigurationObjects"))
)
if mibBuilder.loadTexts:
    qtechDhcpv6ServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-DHCPv6-MIB",
    **{"qtechDhcpv6MIB": qtechDhcpv6MIB,
       "qtechDhcpv6MIBObjects": qtechDhcpv6MIBObjects,
       "qtechDhcpv6ServerMIBObjects": qtechDhcpv6ServerMIBObjects,
       "qtechDhcpv6ServerCounters": qtechDhcpv6ServerCounters,
       "qtechDhcpv6ServerHCountSolicits": qtechDhcpv6ServerHCountSolicits,
       "qtechDhcpv6ServerHCountRequests": qtechDhcpv6ServerHCountRequests,
       "qtechDhcpv6ServerHCountRenews": qtechDhcpv6ServerHCountRenews,
       "qtechDhcpv6ServerHCountDeclines": qtechDhcpv6ServerHCountDeclines,
       "qtechDhcpv6ServerHCountReleases": qtechDhcpv6ServerHCountReleases,
       "qtechDhcpv6ServerHCountInforms": qtechDhcpv6ServerHCountInforms,
       "qtechDhcpv6ServerHCountConfirms": qtechDhcpv6ServerHCountConfirms,
       "qtechDhcpv6ServerHCountRebinds": qtechDhcpv6ServerHCountRebinds,
       "qtechDhcpv6ServerHCountAdvertises": qtechDhcpv6ServerHCountAdvertises,
       "qtechDhcpv6ServerHCountSuccReplies": qtechDhcpv6ServerHCountSuccReplies,
       "qtechDhcpv6ServerHCountFailReplies": qtechDhcpv6ServerHCountFailReplies,
       "qtechDhcpv6ServerHCountInPkts": qtechDhcpv6ServerHCountInPkts,
       "qtechDhcpv6ServerHCountOutPkts": qtechDhcpv6ServerHCountOutPkts,
       "qtechDhcpv6ServerHCountDroppedUnknown": qtechDhcpv6ServerHCountDroppedUnknown,
       "qtechDhcpv6ServerHCountDroppedError": qtechDhcpv6ServerHCountDroppedError,
       "qtechDhcpv6ServerHCountRelayforward": qtechDhcpv6ServerHCountRelayforward,
       "qtechDhcpv6ServerHCountRelayreply": qtechDhcpv6ServerHCountRelayreply,
       "qtechDhcpv6ServerHCountReqtimes": qtechDhcpv6ServerHCountReqtimes,
       "qtechDhcpv6ServerHCountReqSuctimes": qtechDhcpv6ServerHCountReqSuctimes,
       "qtechDhcpv6ServerConfiguration": qtechDhcpv6ServerConfiguration,
       "qtechDhcpv6ServerNumBindings": qtechDhcpv6ServerNumBindings,
       "qtechDhcpv6ServerBindingsTable": qtechDhcpv6ServerBindingsTable,
       "qtechDhcpv6ServerBindingsEntry": qtechDhcpv6ServerBindingsEntry,
       "qtechDhcpv6ServerBindingsPoolName": qtechDhcpv6ServerBindingsPoolName,
       "qtechDhcpv6ServerBindingsClientDuid": qtechDhcpv6ServerBindingsClientDuid,
       "qtechDhcpv6ServerBindingsIaType": qtechDhcpv6ServerBindingsIaType,
       "qtechDhcpv6ServerBindingsIaId": qtechDhcpv6ServerBindingsIaId,
       "qtechDhcpv6ServerBindingsAddress": qtechDhcpv6ServerBindingsAddress,
       "qtechDhcpv6ServerBindingsPrefix": qtechDhcpv6ServerBindingsPrefix,
       "qtechDhcpv6ServerBindingsPrefixLength": qtechDhcpv6ServerBindingsPrefixLength,
       "qtechDhcpv6ServerBindingsDuration": qtechDhcpv6ServerBindingsDuration,
       "qtechDhcpv6ServerBindingsIfIndex": qtechDhcpv6ServerBindingsIfIndex,
       "qtechDhcpv6ServerPoolTable": qtechDhcpv6ServerPoolTable,
       "qtechDhcpv6ServerPoolEntry": qtechDhcpv6ServerPoolEntry,
       "qtechDhcpv6ServerIPPoolName": qtechDhcpv6ServerIPPoolName,
       "qtechDhcpv6ServerDHCPIPPoolUsage": qtechDhcpv6ServerDHCPIPPoolUsage,
       "qtechDhcpv6MIBConformance": qtechDhcpv6MIBConformance,
       "qtechDhcpv6MIBCompliances": qtechDhcpv6MIBCompliances,
       "qtechDhcpv6ServerCompliance": qtechDhcpv6ServerCompliance,
       "qtechDhcpv6MIBGroups": qtechDhcpv6MIBGroups,
       "qtechDhcpv6ServerCountersObjects": qtechDhcpv6ServerCountersObjects,
       "qtechDhcpv6ServerConfigurationObjects": qtechDhcpv6ServerConfigurationObjects,
       "qtechDhcpv6ServerPoolTableObjects": qtechDhcpv6ServerPoolTableObjects}
)
