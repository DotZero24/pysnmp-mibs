# SNMP MIB module (DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/DHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:05 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(EnableVar,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "Vlanset")


# MODULE-IDENTITY

rcDhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13)
)
if mibBuilder.loadTexts:
    rcDhcpRelay.setRevisions(
        ("2004-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDhcpRelayMibObjects_ObjectIdentity = ObjectIdentity
rcDhcpRelayMibObjects = _RcDhcpRelayMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1)
)
_RcDhcpRelayGroup_ObjectIdentity = ObjectIdentity
rcDhcpRelayGroup = _RcDhcpRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1)
)
_RcDhcpRelayEnable_Type = EnableVar
_RcDhcpRelayEnable_Object = MibScalar
rcDhcpRelayEnable = _RcDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 1),
    _RcDhcpRelayEnable_Type()
)
rcDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpRelayEnable.setStatus("current")
_RcDhcpRelayStartTime_Type = TimeTicks
_RcDhcpRelayStartTime_Object = MibScalar
rcDhcpRelayStartTime = _RcDhcpRelayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 2),
    _RcDhcpRelayStartTime_Type()
)
rcDhcpRelayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStartTime.setStatus("mandatory")
_RcDhcpRelayServerTable_Object = MibTable
rcDhcpRelayServerTable = _RcDhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rcDhcpRelayServerTable.setStatus("current")
_RcDhcpRelayServerEntry_Object = MibTableRow
rcDhcpRelayServerEntry = _RcDhcpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 3, 1)
)
rcDhcpRelayServerEntry.setIndexNames(
    (0, "DHCP-RELAY-MIB", "rcDhcpRelayServerIndex"),
)
if mibBuilder.loadTexts:
    rcDhcpRelayServerEntry.setStatus("current")
_RcDhcpRelayServerIndex_Type = Integer32
_RcDhcpRelayServerIndex_Object = MibTableColumn
rcDhcpRelayServerIndex = _RcDhcpRelayServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 3, 1, 1),
    _RcDhcpRelayServerIndex_Type()
)
rcDhcpRelayServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpRelayServerIndex.setStatus("current")
_RcDhcpRelayServerAddress_Type = IpAddress
_RcDhcpRelayServerAddress_Object = MibTableColumn
rcDhcpRelayServerAddress = _RcDhcpRelayServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 3, 1, 2),
    _RcDhcpRelayServerAddress_Type()
)
rcDhcpRelayServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpRelayServerAddress.setStatus("current")
_RcDhcpRelayServerRowStatus_Type = RowStatus
_RcDhcpRelayServerRowStatus_Object = MibTableColumn
rcDhcpRelayServerRowStatus = _RcDhcpRelayServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 3, 1, 3),
    _RcDhcpRelayServerRowStatus_Type()
)
rcDhcpRelayServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpRelayServerRowStatus.setStatus("current")


class _RcDhcpRelayServerNextIndex_Type(Integer32):
    """Custom type rcDhcpRelayServerNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcDhcpRelayServerNextIndex_Type.__name__ = "Integer32"
_RcDhcpRelayServerNextIndex_Object = MibScalar
rcDhcpRelayServerNextIndex = _RcDhcpRelayServerNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 4),
    _RcDhcpRelayServerNextIndex_Type()
)
rcDhcpRelayServerNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayServerNextIndex.setStatus("current")
_RcDhcpRelayVlans_Type = Vlanset
_RcDhcpRelayVlans_Object = MibScalar
rcDhcpRelayVlans = _RcDhcpRelayVlans_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 1, 5),
    _RcDhcpRelayVlans_Type()
)
rcDhcpRelayVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpRelayVlans.setStatus("current")
_RcDhcpRelayStatistics_ObjectIdentity = ObjectIdentity
rcDhcpRelayStatistics = _RcDhcpRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2)
)
_RcDhcpRelayStatsBootps_Type = Counter32
_RcDhcpRelayStatsBootps_Object = MibScalar
rcDhcpRelayStatsBootps = _RcDhcpRelayStatsBootps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 1),
    _RcDhcpRelayStatsBootps_Type()
)
rcDhcpRelayStatsBootps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsBootps.setStatus("mandatory")
_RcDhcpRelayStatsDiscovers_Type = Counter32
_RcDhcpRelayStatsDiscovers_Object = MibScalar
rcDhcpRelayStatsDiscovers = _RcDhcpRelayStatsDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 2),
    _RcDhcpRelayStatsDiscovers_Type()
)
rcDhcpRelayStatsDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsDiscovers.setStatus("mandatory")
_RcDhcpRelayStatsRequests_Type = Counter32
_RcDhcpRelayStatsRequests_Object = MibScalar
rcDhcpRelayStatsRequests = _RcDhcpRelayStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 3),
    _RcDhcpRelayStatsRequests_Type()
)
rcDhcpRelayStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsRequests.setStatus("mandatory")
_RcDhcpRelayStatsReleases_Type = Counter32
_RcDhcpRelayStatsReleases_Object = MibScalar
rcDhcpRelayStatsReleases = _RcDhcpRelayStatsReleases_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 4),
    _RcDhcpRelayStatsReleases_Type()
)
rcDhcpRelayStatsReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsReleases.setStatus("mandatory")
_RcDhcpRelayStatsOffers_Type = Counter32
_RcDhcpRelayStatsOffers_Object = MibScalar
rcDhcpRelayStatsOffers = _RcDhcpRelayStatsOffers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 5),
    _RcDhcpRelayStatsOffers_Type()
)
rcDhcpRelayStatsOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsOffers.setStatus("mandatory")
_RcDhcpRelayStatsAcks_Type = Counter32
_RcDhcpRelayStatsAcks_Object = MibScalar
rcDhcpRelayStatsAcks = _RcDhcpRelayStatsAcks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 6),
    _RcDhcpRelayStatsAcks_Type()
)
rcDhcpRelayStatsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsAcks.setStatus("mandatory")
_RcDhcpRelayStatsNacks_Type = Counter32
_RcDhcpRelayStatsNacks_Object = MibScalar
rcDhcpRelayStatsNacks = _RcDhcpRelayStatsNacks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 7),
    _RcDhcpRelayStatsNacks_Type()
)
rcDhcpRelayStatsNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsNacks.setStatus("mandatory")
_RcDhcpRelayStatsDeclines_Type = Counter32
_RcDhcpRelayStatsDeclines_Object = MibScalar
rcDhcpRelayStatsDeclines = _RcDhcpRelayStatsDeclines_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 8),
    _RcDhcpRelayStatsDeclines_Type()
)
rcDhcpRelayStatsDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsDeclines.setStatus("mandatory")
_RcDhcpRelayStatsInformations_Type = Counter32
_RcDhcpRelayStatsInformations_Object = MibScalar
rcDhcpRelayStatsInformations = _RcDhcpRelayStatsInformations_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 9),
    _RcDhcpRelayStatsInformations_Type()
)
rcDhcpRelayStatsInformations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsInformations.setStatus("mandatory")
_RcDhcpRelayStatsUnknows_Type = Counter32
_RcDhcpRelayStatsUnknows_Object = MibScalar
rcDhcpRelayStatsUnknows = _RcDhcpRelayStatsUnknows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 10),
    _RcDhcpRelayStatsUnknows_Type()
)
rcDhcpRelayStatsUnknows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsUnknows.setStatus("mandatory")
_RcDhcpRelayStatsPackets_Type = Counter32
_RcDhcpRelayStatsPackets_Object = MibScalar
rcDhcpRelayStatsPackets = _RcDhcpRelayStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 13, 1, 2, 11),
    _RcDhcpRelayStatsPackets_Type()
)
rcDhcpRelayStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayStatsPackets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCP-RELAY-MIB",
    **{"rcDhcpRelay": rcDhcpRelay,
       "rcDhcpRelayMibObjects": rcDhcpRelayMibObjects,
       "rcDhcpRelayGroup": rcDhcpRelayGroup,
       "rcDhcpRelayEnable": rcDhcpRelayEnable,
       "rcDhcpRelayStartTime": rcDhcpRelayStartTime,
       "rcDhcpRelayServerTable": rcDhcpRelayServerTable,
       "rcDhcpRelayServerEntry": rcDhcpRelayServerEntry,
       "rcDhcpRelayServerIndex": rcDhcpRelayServerIndex,
       "rcDhcpRelayServerAddress": rcDhcpRelayServerAddress,
       "rcDhcpRelayServerRowStatus": rcDhcpRelayServerRowStatus,
       "rcDhcpRelayServerNextIndex": rcDhcpRelayServerNextIndex,
       "rcDhcpRelayVlans": rcDhcpRelayVlans,
       "rcDhcpRelayStatistics": rcDhcpRelayStatistics,
       "rcDhcpRelayStatsBootps": rcDhcpRelayStatsBootps,
       "rcDhcpRelayStatsDiscovers": rcDhcpRelayStatsDiscovers,
       "rcDhcpRelayStatsRequests": rcDhcpRelayStatsRequests,
       "rcDhcpRelayStatsReleases": rcDhcpRelayStatsReleases,
       "rcDhcpRelayStatsOffers": rcDhcpRelayStatsOffers,
       "rcDhcpRelayStatsAcks": rcDhcpRelayStatsAcks,
       "rcDhcpRelayStatsNacks": rcDhcpRelayStatsNacks,
       "rcDhcpRelayStatsDeclines": rcDhcpRelayStatsDeclines,
       "rcDhcpRelayStatsInformations": rcDhcpRelayStatsInformations,
       "rcDhcpRelayStatsUnknows": rcDhcpRelayStatsUnknows,
       "rcDhcpRelayStatsPackets": rcDhcpRelayStatsPackets}
)
