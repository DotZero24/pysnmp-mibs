# SNMP MIB module (FS-DHCPv6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-DHCPv6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:57 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

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
 RowStatus,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

fsDhcpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45)
)
if mibBuilder.loadTexts:
    fsDhcpv6MIB.setRevisions(
        ("2009-03-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDhcpv6MIBObjects_ObjectIdentity = ObjectIdentity
fsDhcpv6MIBObjects = _FsDhcpv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1)
)
if mibBuilder.loadTexts:
    fsDhcpv6MIBObjects.setStatus("current")
_FsDhcpv6ServerMIBObjects_ObjectIdentity = ObjectIdentity
fsDhcpv6ServerMIBObjects = _FsDhcpv6ServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1)
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerMIBObjects.setStatus("current")
_FsDhcpv6ServerCounters_ObjectIdentity = ObjectIdentity
fsDhcpv6ServerCounters = _FsDhcpv6ServerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerCounters.setStatus("current")
_FsDhcpv6ServerHCountSolicits_Type = Counter64
_FsDhcpv6ServerHCountSolicits_Object = MibScalar
fsDhcpv6ServerHCountSolicits = _FsDhcpv6ServerHCountSolicits_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 1),
    _FsDhcpv6ServerHCountSolicits_Type()
)
fsDhcpv6ServerHCountSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountSolicits.setStatus("current")
_FsDhcpv6ServerHCountRequests_Type = Counter64
_FsDhcpv6ServerHCountRequests_Object = MibScalar
fsDhcpv6ServerHCountRequests = _FsDhcpv6ServerHCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 2),
    _FsDhcpv6ServerHCountRequests_Type()
)
fsDhcpv6ServerHCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountRequests.setStatus("current")
_FsDhcpv6ServerHCountRenews_Type = Counter64
_FsDhcpv6ServerHCountRenews_Object = MibScalar
fsDhcpv6ServerHCountRenews = _FsDhcpv6ServerHCountRenews_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 3),
    _FsDhcpv6ServerHCountRenews_Type()
)
fsDhcpv6ServerHCountRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountRenews.setStatus("current")
_FsDhcpv6ServerHCountDeclines_Type = Counter64
_FsDhcpv6ServerHCountDeclines_Object = MibScalar
fsDhcpv6ServerHCountDeclines = _FsDhcpv6ServerHCountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 4),
    _FsDhcpv6ServerHCountDeclines_Type()
)
fsDhcpv6ServerHCountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountDeclines.setStatus("current")
_FsDhcpv6ServerHCountReleases_Type = Counter64
_FsDhcpv6ServerHCountReleases_Object = MibScalar
fsDhcpv6ServerHCountReleases = _FsDhcpv6ServerHCountReleases_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 5),
    _FsDhcpv6ServerHCountReleases_Type()
)
fsDhcpv6ServerHCountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountReleases.setStatus("current")
_FsDhcpv6ServerHCountInforms_Type = Counter64
_FsDhcpv6ServerHCountInforms_Object = MibScalar
fsDhcpv6ServerHCountInforms = _FsDhcpv6ServerHCountInforms_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 6),
    _FsDhcpv6ServerHCountInforms_Type()
)
fsDhcpv6ServerHCountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountInforms.setStatus("current")
_FsDhcpv6ServerHCountConfirms_Type = Counter64
_FsDhcpv6ServerHCountConfirms_Object = MibScalar
fsDhcpv6ServerHCountConfirms = _FsDhcpv6ServerHCountConfirms_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 7),
    _FsDhcpv6ServerHCountConfirms_Type()
)
fsDhcpv6ServerHCountConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountConfirms.setStatus("current")
_FsDhcpv6ServerHCountRebinds_Type = Counter64
_FsDhcpv6ServerHCountRebinds_Object = MibScalar
fsDhcpv6ServerHCountRebinds = _FsDhcpv6ServerHCountRebinds_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 8),
    _FsDhcpv6ServerHCountRebinds_Type()
)
fsDhcpv6ServerHCountRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountRebinds.setStatus("current")
_FsDhcpv6ServerHCountAdvertises_Type = Counter64
_FsDhcpv6ServerHCountAdvertises_Object = MibScalar
fsDhcpv6ServerHCountAdvertises = _FsDhcpv6ServerHCountAdvertises_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 9),
    _FsDhcpv6ServerHCountAdvertises_Type()
)
fsDhcpv6ServerHCountAdvertises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountAdvertises.setStatus("current")
_FsDhcpv6ServerHCountSuccReplies_Type = Counter64
_FsDhcpv6ServerHCountSuccReplies_Object = MibScalar
fsDhcpv6ServerHCountSuccReplies = _FsDhcpv6ServerHCountSuccReplies_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 10),
    _FsDhcpv6ServerHCountSuccReplies_Type()
)
fsDhcpv6ServerHCountSuccReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountSuccReplies.setStatus("current")
_FsDhcpv6ServerHCountFailReplies_Type = Counter64
_FsDhcpv6ServerHCountFailReplies_Object = MibScalar
fsDhcpv6ServerHCountFailReplies = _FsDhcpv6ServerHCountFailReplies_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 11),
    _FsDhcpv6ServerHCountFailReplies_Type()
)
fsDhcpv6ServerHCountFailReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountFailReplies.setStatus("current")
_FsDhcpv6ServerHCountInPkts_Type = Counter64
_FsDhcpv6ServerHCountInPkts_Object = MibScalar
fsDhcpv6ServerHCountInPkts = _FsDhcpv6ServerHCountInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 12),
    _FsDhcpv6ServerHCountInPkts_Type()
)
fsDhcpv6ServerHCountInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountInPkts.setStatus("current")
_FsDhcpv6ServerHCountOutPkts_Type = Counter64
_FsDhcpv6ServerHCountOutPkts_Object = MibScalar
fsDhcpv6ServerHCountOutPkts = _FsDhcpv6ServerHCountOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 13),
    _FsDhcpv6ServerHCountOutPkts_Type()
)
fsDhcpv6ServerHCountOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountOutPkts.setStatus("current")
_FsDhcpv6ServerHCountDroppedUnknown_Type = Counter64
_FsDhcpv6ServerHCountDroppedUnknown_Object = MibScalar
fsDhcpv6ServerHCountDroppedUnknown = _FsDhcpv6ServerHCountDroppedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 14),
    _FsDhcpv6ServerHCountDroppedUnknown_Type()
)
fsDhcpv6ServerHCountDroppedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountDroppedUnknown.setStatus("current")
_FsDhcpv6ServerHCountDroppedError_Type = Counter64
_FsDhcpv6ServerHCountDroppedError_Object = MibScalar
fsDhcpv6ServerHCountDroppedError = _FsDhcpv6ServerHCountDroppedError_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 15),
    _FsDhcpv6ServerHCountDroppedError_Type()
)
fsDhcpv6ServerHCountDroppedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountDroppedError.setStatus("current")
_FsDhcpv6ServerHCountRelayforward_Type = Counter64
_FsDhcpv6ServerHCountRelayforward_Object = MibScalar
fsDhcpv6ServerHCountRelayforward = _FsDhcpv6ServerHCountRelayforward_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 16),
    _FsDhcpv6ServerHCountRelayforward_Type()
)
fsDhcpv6ServerHCountRelayforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountRelayforward.setStatus("current")
_FsDhcpv6ServerHCountRelayreply_Type = Counter64
_FsDhcpv6ServerHCountRelayreply_Object = MibScalar
fsDhcpv6ServerHCountRelayreply = _FsDhcpv6ServerHCountRelayreply_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 17),
    _FsDhcpv6ServerHCountRelayreply_Type()
)
fsDhcpv6ServerHCountRelayreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountRelayreply.setStatus("current")
_FsDhcpv6ServerHCountReqtimes_Type = Counter64
_FsDhcpv6ServerHCountReqtimes_Object = MibScalar
fsDhcpv6ServerHCountReqtimes = _FsDhcpv6ServerHCountReqtimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 18),
    _FsDhcpv6ServerHCountReqtimes_Type()
)
fsDhcpv6ServerHCountReqtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountReqtimes.setStatus("current")
_FsDhcpv6ServerHCountReqSuctimes_Type = Counter64
_FsDhcpv6ServerHCountReqSuctimes_Object = MibScalar
fsDhcpv6ServerHCountReqSuctimes = _FsDhcpv6ServerHCountReqSuctimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 1, 19),
    _FsDhcpv6ServerHCountReqSuctimes_Type()
)
fsDhcpv6ServerHCountReqSuctimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerHCountReqSuctimes.setStatus("current")
_FsDhcpv6ServerConfiguration_ObjectIdentity = ObjectIdentity
fsDhcpv6ServerConfiguration = _FsDhcpv6ServerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerConfiguration.setStatus("current")
_FsDhcpv6ServerNumBindings_Type = Counter32
_FsDhcpv6ServerNumBindings_Object = MibScalar
fsDhcpv6ServerNumBindings = _FsDhcpv6ServerNumBindings_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 1),
    _FsDhcpv6ServerNumBindings_Type()
)
fsDhcpv6ServerNumBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerNumBindings.setStatus("current")
_FsDhcpv6ServerBindingsTable_Object = MibTable
fsDhcpv6ServerBindingsTable = _FsDhcpv6ServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsTable.setStatus("current")
_FsDhcpv6ServerBindingsEntry_Object = MibTableRow
fsDhcpv6ServerBindingsEntry = _FsDhcpv6ServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1)
)
fsDhcpv6ServerBindingsEntry.setIndexNames(
    (0, "FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsPoolName"),
    (0, "FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsClientDuid"),
    (0, "FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsIaType"),
    (0, "FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsIaId"),
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsEntry.setStatus("current")


class _FsDhcpv6ServerBindingsPoolName_Type(DisplayString):
    """Custom type fsDhcpv6ServerBindingsPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsDhcpv6ServerBindingsPoolName_Type.__name__ = "DisplayString"
_FsDhcpv6ServerBindingsPoolName_Object = MibTableColumn
fsDhcpv6ServerBindingsPoolName = _FsDhcpv6ServerBindingsPoolName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 1),
    _FsDhcpv6ServerBindingsPoolName_Type()
)
fsDhcpv6ServerBindingsPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsPoolName.setStatus("current")


class _FsDhcpv6ServerBindingsClientDuid_Type(OctetString):
    """Custom type fsDhcpv6ServerBindingsClientDuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_FsDhcpv6ServerBindingsClientDuid_Type.__name__ = "OctetString"
_FsDhcpv6ServerBindingsClientDuid_Object = MibTableColumn
fsDhcpv6ServerBindingsClientDuid = _FsDhcpv6ServerBindingsClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 2),
    _FsDhcpv6ServerBindingsClientDuid_Type()
)
fsDhcpv6ServerBindingsClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsClientDuid.setStatus("current")


class _FsDhcpv6ServerBindingsIaType_Type(Integer32):
    """Custom type fsDhcpv6ServerBindingsIaType based on Integer32"""
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


_FsDhcpv6ServerBindingsIaType_Type.__name__ = "Integer32"
_FsDhcpv6ServerBindingsIaType_Object = MibTableColumn
fsDhcpv6ServerBindingsIaType = _FsDhcpv6ServerBindingsIaType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 3),
    _FsDhcpv6ServerBindingsIaType_Type()
)
fsDhcpv6ServerBindingsIaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsIaType.setStatus("current")
_FsDhcpv6ServerBindingsIaId_Type = Unsigned32
_FsDhcpv6ServerBindingsIaId_Object = MibTableColumn
fsDhcpv6ServerBindingsIaId = _FsDhcpv6ServerBindingsIaId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 4),
    _FsDhcpv6ServerBindingsIaId_Type()
)
fsDhcpv6ServerBindingsIaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsIaId.setStatus("current")
_FsDhcpv6ServerBindingsAddress_Type = Ipv6Address
_FsDhcpv6ServerBindingsAddress_Object = MibTableColumn
fsDhcpv6ServerBindingsAddress = _FsDhcpv6ServerBindingsAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 5),
    _FsDhcpv6ServerBindingsAddress_Type()
)
fsDhcpv6ServerBindingsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsAddress.setStatus("current")
_FsDhcpv6ServerBindingsPrefix_Type = Ipv6AddressPrefix
_FsDhcpv6ServerBindingsPrefix_Object = MibTableColumn
fsDhcpv6ServerBindingsPrefix = _FsDhcpv6ServerBindingsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 6),
    _FsDhcpv6ServerBindingsPrefix_Type()
)
fsDhcpv6ServerBindingsPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsPrefix.setStatus("current")


class _FsDhcpv6ServerBindingsPrefixLength_Type(Integer32):
    """Custom type fsDhcpv6ServerBindingsPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsDhcpv6ServerBindingsPrefixLength_Type.__name__ = "Integer32"
_FsDhcpv6ServerBindingsPrefixLength_Object = MibTableColumn
fsDhcpv6ServerBindingsPrefixLength = _FsDhcpv6ServerBindingsPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 7),
    _FsDhcpv6ServerBindingsPrefixLength_Type()
)
fsDhcpv6ServerBindingsPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsPrefixLength.setStatus("current")
_FsDhcpv6ServerBindingsDuration_Type = Unsigned32
_FsDhcpv6ServerBindingsDuration_Object = MibTableColumn
fsDhcpv6ServerBindingsDuration = _FsDhcpv6ServerBindingsDuration_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 8),
    _FsDhcpv6ServerBindingsDuration_Type()
)
fsDhcpv6ServerBindingsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsDuration.setStatus("current")
_FsDhcpv6ServerBindingsIfIndex_Type = InterfaceIndex
_FsDhcpv6ServerBindingsIfIndex_Object = MibTableColumn
fsDhcpv6ServerBindingsIfIndex = _FsDhcpv6ServerBindingsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 9),
    _FsDhcpv6ServerBindingsIfIndex_Type()
)
fsDhcpv6ServerBindingsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpv6ServerBindingsIfIndex.setStatus("current")
_FsDhcpv6ServerPoolUsageTable_Object = MibTable
fsDhcpv6ServerPoolUsageTable = _FsDhcpv6ServerPoolUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerPoolUsageTable.setStatus("current")
_FsDhcpv6ServerPoolEntry_Object = MibTableRow
fsDhcpv6ServerPoolEntry = _FsDhcpv6ServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1)
)
fsDhcpv6ServerPoolEntry.setIndexNames(
    (0, "FS-DHCPv6-MIB", "fsIPv6PoolUsageIndex"),
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerPoolEntry.setStatus("current")
_FsIPv6PoolUsageIndex_Type = Unsigned32
_FsIPv6PoolUsageIndex_Object = MibTableColumn
fsIPv6PoolUsageIndex = _FsIPv6PoolUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 1),
    _FsIPv6PoolUsageIndex_Type()
)
fsIPv6PoolUsageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPv6PoolUsageIndex.setStatus("current")


class _FsIPv6PoolUsageName_Type(DisplayString):
    """Custom type fsIPv6PoolUsageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsIPv6PoolUsageName_Type.__name__ = "DisplayString"
_FsIPv6PoolUsageName_Object = MibTableColumn
fsIPv6PoolUsageName = _FsIPv6PoolUsageName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 2),
    _FsIPv6PoolUsageName_Type()
)
fsIPv6PoolUsageName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPv6PoolUsageName.setStatus("current")
_FsIPv6DHCPIPPoolUsage_Type = Unsigned32
_FsIPv6DHCPIPPoolUsage_Object = MibTableColumn
fsIPv6DHCPIPPoolUsage = _FsIPv6DHCPIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 3),
    _FsIPv6DHCPIPPoolUsage_Type()
)
fsIPv6DHCPIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPv6DHCPIPPoolUsage.setStatus("current")
_FsIPv6PoolUsageRawStatus_Type = RowStatus
_FsIPv6PoolUsageRawStatus_Object = MibTableColumn
fsIPv6PoolUsageRawStatus = _FsIPv6PoolUsageRawStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 4),
    _FsIPv6PoolUsageRawStatus_Type()
)
fsIPv6PoolUsageRawStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPv6PoolUsageRawStatus.setStatus("current")
_FsDhcpv6ServerPoolConfigTable_Object = MibTable
fsDhcpv6ServerPoolConfigTable = _FsDhcpv6ServerPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerPoolConfigTable.setStatus("current")
_FsDhcpv6ServerPoolCfgEntry_Object = MibTableRow
fsDhcpv6ServerPoolCfgEntry = _FsDhcpv6ServerPoolCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1)
)
fsDhcpv6ServerPoolCfgEntry.setIndexNames(
    (0, "FS-DHCPv6-MIB", "fsIPv6PoolCfgIndex"),
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerPoolCfgEntry.setStatus("current")
_FsIPv6PoolCfgIndex_Type = Unsigned32
_FsIPv6PoolCfgIndex_Object = MibTableColumn
fsIPv6PoolCfgIndex = _FsIPv6PoolCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 1),
    _FsIPv6PoolCfgIndex_Type()
)
fsIPv6PoolCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPv6PoolCfgIndex.setStatus("current")


class _FsIPv6PoolName_Type(DisplayString):
    """Custom type fsIPv6PoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsIPv6PoolName_Type.__name__ = "DisplayString"
_FsIPv6PoolName_Object = MibTableColumn
fsIPv6PoolName = _FsIPv6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 2),
    _FsIPv6PoolName_Type()
)
fsIPv6PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPv6PoolName.setStatus("current")
_FsIPv6PoolStartAddr_Type = InetAddressIPv6
_FsIPv6PoolStartAddr_Object = MibTableColumn
fsIPv6PoolStartAddr = _FsIPv6PoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 3),
    _FsIPv6PoolStartAddr_Type()
)
fsIPv6PoolStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPv6PoolStartAddr.setStatus("current")
_FsIPv6PoolStopAddr_Type = InetAddressIPv6
_FsIPv6PoolStopAddr_Object = MibTableColumn
fsIPv6PoolStopAddr = _FsIPv6PoolStopAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 4),
    _FsIPv6PoolStopAddr_Type()
)
fsIPv6PoolStopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPv6PoolStopAddr.setStatus("current")
_FsIPv6NetPrefixLen_Type = Unsigned32
_FsIPv6NetPrefixLen_Object = MibTableColumn
fsIPv6NetPrefixLen = _FsIPv6NetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 5),
    _FsIPv6NetPrefixLen_Type()
)
fsIPv6NetPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPv6NetPrefixLen.setStatus("current")
_FsPrimDNSServerIPv6Address_Type = InetAddressIPv6
_FsPrimDNSServerIPv6Address_Object = MibTableColumn
fsPrimDNSServerIPv6Address = _FsPrimDNSServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 6),
    _FsPrimDNSServerIPv6Address_Type()
)
fsPrimDNSServerIPv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPrimDNSServerIPv6Address.setStatus("current")
_FsSeconDNSServerIPv6Address_Type = InetAddressIPv6
_FsSeconDNSServerIPv6Address_Object = MibTableColumn
fsSeconDNSServerIPv6Address = _FsSeconDNSServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 7),
    _FsSeconDNSServerIPv6Address_Type()
)
fsSeconDNSServerIPv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSeconDNSServerIPv6Address.setStatus("current")
_FsIPv6AddrLease_Type = TimeTicks
_FsIPv6AddrLease_Object = MibTableColumn
fsIPv6AddrLease = _FsIPv6AddrLease_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 8),
    _FsIPv6AddrLease_Type()
)
fsIPv6AddrLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPv6AddrLease.setStatus("current")
_FsIPv6RawStatus_Type = RowStatus
_FsIPv6RawStatus_Object = MibTableColumn
fsIPv6RawStatus = _FsIPv6RawStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 9),
    _FsIPv6RawStatus_Type()
)
fsIPv6RawStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIPv6RawStatus.setStatus("current")
_FsDhcpv6MIBConformance_ObjectIdentity = ObjectIdentity
fsDhcpv6MIBConformance = _FsDhcpv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 2)
)
if mibBuilder.loadTexts:
    fsDhcpv6MIBConformance.setStatus("current")
_FsDhcpv6MIBCompliances_ObjectIdentity = ObjectIdentity
fsDhcpv6MIBCompliances = _FsDhcpv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 2, 1)
)
_FsDhcpv6MIBGroups_ObjectIdentity = ObjectIdentity
fsDhcpv6MIBGroups = _FsDhcpv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 2, 2)
)

# Managed Objects groups

fsDhcpv6ServerCountersObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 2, 2, 1)
)
fsDhcpv6ServerCountersObjects.setObjects(
      *(("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountSolicits"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountRenews"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountDeclines"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountReleases"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountInforms"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountConfirms"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountRebinds"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountAdvertises"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountSuccReplies"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountFailReplies"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountInPkts"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountOutPkts"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountDroppedUnknown"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountDroppedError"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountRelayforward"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountRelayreply"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountReqtimes"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerHCountReqSuctimes"))
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerCountersObjects.setStatus("current")

fsDhcpv6ServerConfigurationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 2, 2, 2)
)
fsDhcpv6ServerConfigurationObjects.setObjects(
      *(("FS-DHCPv6-MIB", "fsDhcpv6ServerNumBindings"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsPoolName"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsClientDuid"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsIaType"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsIaId"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsAddress"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsPrefix"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsPrefixLength"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsDuration"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerBindingsIfIndex"))
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerConfigurationObjects.setStatus("current")

fsDhcpv6ServerPoolUsageTableObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 2, 2, 3)
)
fsDhcpv6ServerPoolUsageTableObjects.setObjects(
      *(("FS-DHCPv6-MIB", "fsIPv6PoolUsageIndex"),
        ("FS-DHCPv6-MIB", "fsIPv6PoolName"),
        ("FS-DHCPv6-MIB", "fsIPv6DHCPIPPoolUsage"),
        ("FS-DHCPv6-MIB", "fsIPv6PoolUsageRawStatus"))
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerPoolUsageTableObjects.setStatus("current")

fsDhcpv6ServerPoolConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 2, 2, 4)
)
fsDhcpv6ServerPoolConfigGroup.setObjects(
      *(("FS-DHCPv6-MIB", "fsIPv6PoolCfgIndex"),
        ("FS-DHCPv6-MIB", "fsIPv6PoolName"),
        ("FS-DHCPv6-MIB", "fsIPv6PoolStartAddr"),
        ("FS-DHCPv6-MIB", "fsIPv6PoolStopAddr"),
        ("FS-DHCPv6-MIB", "fsIPv6NetPrefixLen"),
        ("FS-DHCPv6-MIB", "fsPrimDNSServerIPv6Address"),
        ("FS-DHCPv6-MIB", "fsSeconDNSServerIPv6Address"),
        ("FS-DHCPv6-MIB", "fsIPv6AddrLease"),
        ("FS-DHCPv6-MIB", "fsIPv6RawStatus"))
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerPoolConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsDhcpv6ServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 45, 2, 1, 1)
)
fsDhcpv6ServerCompliance.setObjects(
      *(("FS-DHCPv6-MIB", "fsDhcpv6ServerCountersObjects"),
        ("FS-DHCPv6-MIB", "fsDhcpv6ServerConfigurationObjects"))
)
if mibBuilder.loadTexts:
    fsDhcpv6ServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-DHCPv6-MIB",
    **{"fsDhcpv6MIB": fsDhcpv6MIB,
       "fsDhcpv6MIBObjects": fsDhcpv6MIBObjects,
       "fsDhcpv6ServerMIBObjects": fsDhcpv6ServerMIBObjects,
       "fsDhcpv6ServerCounters": fsDhcpv6ServerCounters,
       "fsDhcpv6ServerHCountSolicits": fsDhcpv6ServerHCountSolicits,
       "fsDhcpv6ServerHCountRequests": fsDhcpv6ServerHCountRequests,
       "fsDhcpv6ServerHCountRenews": fsDhcpv6ServerHCountRenews,
       "fsDhcpv6ServerHCountDeclines": fsDhcpv6ServerHCountDeclines,
       "fsDhcpv6ServerHCountReleases": fsDhcpv6ServerHCountReleases,
       "fsDhcpv6ServerHCountInforms": fsDhcpv6ServerHCountInforms,
       "fsDhcpv6ServerHCountConfirms": fsDhcpv6ServerHCountConfirms,
       "fsDhcpv6ServerHCountRebinds": fsDhcpv6ServerHCountRebinds,
       "fsDhcpv6ServerHCountAdvertises": fsDhcpv6ServerHCountAdvertises,
       "fsDhcpv6ServerHCountSuccReplies": fsDhcpv6ServerHCountSuccReplies,
       "fsDhcpv6ServerHCountFailReplies": fsDhcpv6ServerHCountFailReplies,
       "fsDhcpv6ServerHCountInPkts": fsDhcpv6ServerHCountInPkts,
       "fsDhcpv6ServerHCountOutPkts": fsDhcpv6ServerHCountOutPkts,
       "fsDhcpv6ServerHCountDroppedUnknown": fsDhcpv6ServerHCountDroppedUnknown,
       "fsDhcpv6ServerHCountDroppedError": fsDhcpv6ServerHCountDroppedError,
       "fsDhcpv6ServerHCountRelayforward": fsDhcpv6ServerHCountRelayforward,
       "fsDhcpv6ServerHCountRelayreply": fsDhcpv6ServerHCountRelayreply,
       "fsDhcpv6ServerHCountReqtimes": fsDhcpv6ServerHCountReqtimes,
       "fsDhcpv6ServerHCountReqSuctimes": fsDhcpv6ServerHCountReqSuctimes,
       "fsDhcpv6ServerConfiguration": fsDhcpv6ServerConfiguration,
       "fsDhcpv6ServerNumBindings": fsDhcpv6ServerNumBindings,
       "fsDhcpv6ServerBindingsTable": fsDhcpv6ServerBindingsTable,
       "fsDhcpv6ServerBindingsEntry": fsDhcpv6ServerBindingsEntry,
       "fsDhcpv6ServerBindingsPoolName": fsDhcpv6ServerBindingsPoolName,
       "fsDhcpv6ServerBindingsClientDuid": fsDhcpv6ServerBindingsClientDuid,
       "fsDhcpv6ServerBindingsIaType": fsDhcpv6ServerBindingsIaType,
       "fsDhcpv6ServerBindingsIaId": fsDhcpv6ServerBindingsIaId,
       "fsDhcpv6ServerBindingsAddress": fsDhcpv6ServerBindingsAddress,
       "fsDhcpv6ServerBindingsPrefix": fsDhcpv6ServerBindingsPrefix,
       "fsDhcpv6ServerBindingsPrefixLength": fsDhcpv6ServerBindingsPrefixLength,
       "fsDhcpv6ServerBindingsDuration": fsDhcpv6ServerBindingsDuration,
       "fsDhcpv6ServerBindingsIfIndex": fsDhcpv6ServerBindingsIfIndex,
       "fsDhcpv6ServerPoolUsageTable": fsDhcpv6ServerPoolUsageTable,
       "fsDhcpv6ServerPoolEntry": fsDhcpv6ServerPoolEntry,
       "fsIPv6PoolUsageIndex": fsIPv6PoolUsageIndex,
       "fsIPv6PoolUsageName": fsIPv6PoolUsageName,
       "fsIPv6DHCPIPPoolUsage": fsIPv6DHCPIPPoolUsage,
       "fsIPv6PoolUsageRawStatus": fsIPv6PoolUsageRawStatus,
       "fsDhcpv6ServerPoolConfigTable": fsDhcpv6ServerPoolConfigTable,
       "fsDhcpv6ServerPoolCfgEntry": fsDhcpv6ServerPoolCfgEntry,
       "fsIPv6PoolCfgIndex": fsIPv6PoolCfgIndex,
       "fsIPv6PoolName": fsIPv6PoolName,
       "fsIPv6PoolStartAddr": fsIPv6PoolStartAddr,
       "fsIPv6PoolStopAddr": fsIPv6PoolStopAddr,
       "fsIPv6NetPrefixLen": fsIPv6NetPrefixLen,
       "fsPrimDNSServerIPv6Address": fsPrimDNSServerIPv6Address,
       "fsSeconDNSServerIPv6Address": fsSeconDNSServerIPv6Address,
       "fsIPv6AddrLease": fsIPv6AddrLease,
       "fsIPv6RawStatus": fsIPv6RawStatus,
       "fsDhcpv6MIBConformance": fsDhcpv6MIBConformance,
       "fsDhcpv6MIBCompliances": fsDhcpv6MIBCompliances,
       "fsDhcpv6ServerCompliance": fsDhcpv6ServerCompliance,
       "fsDhcpv6MIBGroups": fsDhcpv6MIBGroups,
       "fsDhcpv6ServerCountersObjects": fsDhcpv6ServerCountersObjects,
       "fsDhcpv6ServerConfigurationObjects": fsDhcpv6ServerConfigurationObjects,
       "fsDhcpv6ServerPoolUsageTableObjects": fsDhcpv6ServerPoolUsageTableObjects,
       "fsDhcpv6ServerPoolConfigGroup": fsDhcpv6ServerPoolConfigGroup}
)
