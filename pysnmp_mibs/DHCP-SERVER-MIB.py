# SNMP MIB module (DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/DHCP-Server-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:51 2025
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

rcDhcpServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12)
)
if mibBuilder.loadTexts:
    rcDhcpServer.setRevisions(
        ("2004-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDhcpServerMibObjects_ObjectIdentity = ObjectIdentity
rcDhcpServerMibObjects = _RcDhcpServerMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1)
)
_RcDhcpDot1dDhcp_ObjectIdentity = ObjectIdentity
rcDhcpDot1dDhcp = _RcDhcpDot1dDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1)
)


class _RcDhcpPropEnable_Type(EnableVar):
    """Custom type rcDhcpPropEnable based on EnableVar"""
    defaultValue = 2


_RcDhcpPropEnable_Type.__name__ = "EnableVar"
_RcDhcpPropEnable_Object = MibScalar
rcDhcpPropEnable = _RcDhcpPropEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 1),
    _RcDhcpPropEnable_Type()
)
rcDhcpPropEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpPropEnable.setStatus("current")
_RcDhcpVlanActive_Type = Vlanset
_RcDhcpVlanActive_Object = MibScalar
rcDhcpVlanActive = _RcDhcpVlanActive_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 2),
    _RcDhcpVlanActive_Type()
)
rcDhcpVlanActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpVlanActive.setStatus("current")


class _RcDhcpIpNextIndex_Type(Integer32):
    """Custom type rcDhcpIpNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RcDhcpIpNextIndex_Type.__name__ = "Integer32"
_RcDhcpIpNextIndex_Object = MibScalar
rcDhcpIpNextIndex = _RcDhcpIpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 3),
    _RcDhcpIpNextIndex_Type()
)
rcDhcpIpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpIpNextIndex.setStatus("current")


class _RcDhcpMaxLease_Type(Integer32):
    """Custom type rcDhcpMaxLease based on Integer32"""
    defaultValue = 10080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcDhcpMaxLease_Type.__name__ = "Integer32"
_RcDhcpMaxLease_Object = MibScalar
rcDhcpMaxLease = _RcDhcpMaxLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 4),
    _RcDhcpMaxLease_Type()
)
rcDhcpMaxLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpMaxLease.setStatus("current")


class _RcDhcpMinLease_Type(Integer32):
    """Custom type rcDhcpMinLease based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcDhcpMinLease_Type.__name__ = "Integer32"
_RcDhcpMinLease_Object = MibScalar
rcDhcpMinLease = _RcDhcpMinLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 5),
    _RcDhcpMinLease_Type()
)
rcDhcpMinLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpMinLease.setStatus("current")


class _RcDhcpDefLease_Type(Integer32):
    """Custom type rcDhcpDefLease based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcDhcpDefLease_Type.__name__ = "Integer32"
_RcDhcpDefLease_Object = MibScalar
rcDhcpDefLease = _RcDhcpDefLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 6),
    _RcDhcpDefLease_Type()
)
rcDhcpDefLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpDefLease.setStatus("current")
_RcDhcpVlanAuth_Type = Vlanset
_RcDhcpVlanAuth_Object = MibScalar
rcDhcpVlanAuth = _RcDhcpVlanAuth_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 7),
    _RcDhcpVlanAuth_Type()
)
rcDhcpVlanAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpVlanAuth.setStatus("current")
_RcDhcpServerStartTime_Type = TimeTicks
_RcDhcpServerStartTime_Object = MibScalar
rcDhcpServerStartTime = _RcDhcpServerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 8),
    _RcDhcpServerStartTime_Type()
)
rcDhcpServerStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpServerStartTime.setStatus("current")
_RcDhcpIpTable_Object = MibTable
rcDhcpIpTable = _RcDhcpIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9)
)
if mibBuilder.loadTexts:
    rcDhcpIpTable.setStatus("current")
_RcDhcpIpEntry_Object = MibTableRow
rcDhcpIpEntry = _RcDhcpIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1)
)
rcDhcpIpEntry.setIndexNames(
    (0, "DHCP-SERVER-MIB", "rcDhcpIpIndex"),
)
if mibBuilder.loadTexts:
    rcDhcpIpEntry.setStatus("current")


class _RcDhcpIpIndex_Type(Integer32):
    """Custom type rcDhcpIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RcDhcpIpIndex_Type.__name__ = "Integer32"
_RcDhcpIpIndex_Object = MibTableColumn
rcDhcpIpIndex = _RcDhcpIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 1),
    _RcDhcpIpIndex_Type()
)
rcDhcpIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpIpIndex.setStatus("current")


class _RcDhcpIpEntryName_Type(OctetString):
    """Custom type rcDhcpIpEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcDhcpIpEntryName_Type.__name__ = "OctetString"
_RcDhcpIpEntryName_Object = MibTableColumn
rcDhcpIpEntryName = _RcDhcpIpEntryName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 2),
    _RcDhcpIpEntryName_Type()
)
rcDhcpIpEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpEntryName.setStatus("current")
_RcDhcpIpVlanset_Type = Vlanset
_RcDhcpIpVlanset_Object = MibTableColumn
rcDhcpIpVlanset = _RcDhcpIpVlanset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 3),
    _RcDhcpIpVlanset_Type()
)
rcDhcpIpVlanset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpVlanset.setStatus("current")
_RcDhcpIpStartIp_Type = IpAddress
_RcDhcpIpStartIp_Object = MibTableColumn
rcDhcpIpStartIp = _RcDhcpIpStartIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 4),
    _RcDhcpIpStartIp_Type()
)
rcDhcpIpStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpStartIp.setStatus("current")
_RcDhcpIpEndIp_Type = IpAddress
_RcDhcpIpEndIp_Object = MibTableColumn
rcDhcpIpEndIp = _RcDhcpIpEndIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 5),
    _RcDhcpIpEndIp_Type()
)
rcDhcpIpEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpEndIp.setStatus("current")
_RcDhcpIpNetmask_Type = IpAddress
_RcDhcpIpNetmask_Object = MibTableColumn
rcDhcpIpNetmask = _RcDhcpIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 6),
    _RcDhcpIpNetmask_Type()
)
rcDhcpIpNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpNetmask.setStatus("current")
_RcDhcpIpGateway_Type = IpAddress
_RcDhcpIpGateway_Object = MibTableColumn
rcDhcpIpGateway = _RcDhcpIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 7),
    _RcDhcpIpGateway_Type()
)
rcDhcpIpGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpGateway.setStatus("current")
_RcDhcpIpDnsServer_Type = IpAddress
_RcDhcpIpDnsServer_Object = MibTableColumn
rcDhcpIpDnsServer = _RcDhcpIpDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 8),
    _RcDhcpIpDnsServer_Type()
)
rcDhcpIpDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpDnsServer.setStatus("current")
_RcDhcpIpSecondaryDnsServer_Type = IpAddress
_RcDhcpIpSecondaryDnsServer_Object = MibTableColumn
rcDhcpIpSecondaryDnsServer = _RcDhcpIpSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 9),
    _RcDhcpIpSecondaryDnsServer_Type()
)
rcDhcpIpSecondaryDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpSecondaryDnsServer.setStatus("current")
_RcDhcpIpRowStatus_Type = RowStatus
_RcDhcpIpRowStatus_Object = MibTableColumn
rcDhcpIpRowStatus = _RcDhcpIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 9, 1, 10),
    _RcDhcpIpRowStatus_Type()
)
rcDhcpIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpIpRowStatus.setStatus("current")


class _RcDhcpRelayNextIndex_Type(Integer32):
    """Custom type rcDhcpRelayNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcDhcpRelayNextIndex_Type.__name__ = "Integer32"
_RcDhcpRelayNextIndex_Object = MibScalar
rcDhcpRelayNextIndex = _RcDhcpRelayNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 10),
    _RcDhcpRelayNextIndex_Type()
)
rcDhcpRelayNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpRelayNextIndex.setStatus("current")
_RcDhcpRelayTable_Object = MibTable
rcDhcpRelayTable = _RcDhcpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 11)
)
if mibBuilder.loadTexts:
    rcDhcpRelayTable.setStatus("current")
_RcDhcpRelayEntry_Object = MibTableRow
rcDhcpRelayEntry = _RcDhcpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 11, 1)
)
rcDhcpRelayEntry.setIndexNames(
    (0, "DHCP-SERVER-MIB", "rcDhcpRelayIndex"),
)
if mibBuilder.loadTexts:
    rcDhcpRelayEntry.setStatus("current")
_RcDhcpRelayIndex_Type = Integer32
_RcDhcpRelayIndex_Object = MibTableColumn
rcDhcpRelayIndex = _RcDhcpRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 11, 1, 1),
    _RcDhcpRelayIndex_Type()
)
rcDhcpRelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpRelayIndex.setStatus("current")
_RcDhcpRelayAddress_Type = IpAddress
_RcDhcpRelayAddress_Object = MibTableColumn
rcDhcpRelayAddress = _RcDhcpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 11, 1, 2),
    _RcDhcpRelayAddress_Type()
)
rcDhcpRelayAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpRelayAddress.setStatus("current")
_RcDhcpRelayMask_Type = IpAddress
_RcDhcpRelayMask_Object = MibTableColumn
rcDhcpRelayMask = _RcDhcpRelayMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 11, 1, 3),
    _RcDhcpRelayMask_Type()
)
rcDhcpRelayMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpRelayMask.setStatus("current")
_RcDhcpRelayRowStatus_Type = RowStatus
_RcDhcpRelayRowStatus_Object = MibTableColumn
rcDhcpRelayRowStatus = _RcDhcpRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 1, 11, 1, 4),
    _RcDhcpRelayRowStatus_Type()
)
rcDhcpRelayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpRelayRowStatus.setStatus("current")
_RcDhcpServerStatistics_ObjectIdentity = ObjectIdentity
rcDhcpServerStatistics = _RcDhcpServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2)
)
_RcDhcpServerStatsBootps_Type = Counter32
_RcDhcpServerStatsBootps_Object = MibScalar
rcDhcpServerStatsBootps = _RcDhcpServerStatsBootps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 1),
    _RcDhcpServerStatsBootps_Type()
)
rcDhcpServerStatsBootps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsBootps.setStatus("mandatory")
_RcDhcpServerStatsDiscovers_Type = Counter32
_RcDhcpServerStatsDiscovers_Object = MibScalar
rcDhcpServerStatsDiscovers = _RcDhcpServerStatsDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 2),
    _RcDhcpServerStatsDiscovers_Type()
)
rcDhcpServerStatsDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsDiscovers.setStatus("mandatory")
_RcDhcpServerStatsRequests_Type = Counter32
_RcDhcpServerStatsRequests_Object = MibScalar
rcDhcpServerStatsRequests = _RcDhcpServerStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 3),
    _RcDhcpServerStatsRequests_Type()
)
rcDhcpServerStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsRequests.setStatus("mandatory")
_RcDhcpServerStatsReleases_Type = Counter32
_RcDhcpServerStatsReleases_Object = MibScalar
rcDhcpServerStatsReleases = _RcDhcpServerStatsReleases_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 4),
    _RcDhcpServerStatsReleases_Type()
)
rcDhcpServerStatsReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsReleases.setStatus("mandatory")
_RcDhcpServerStatsOffers_Type = Counter32
_RcDhcpServerStatsOffers_Object = MibScalar
rcDhcpServerStatsOffers = _RcDhcpServerStatsOffers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 5),
    _RcDhcpServerStatsOffers_Type()
)
rcDhcpServerStatsOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsOffers.setStatus("mandatory")
_RcDhcpServerStatsAcks_Type = Counter32
_RcDhcpServerStatsAcks_Object = MibScalar
rcDhcpServerStatsAcks = _RcDhcpServerStatsAcks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 6),
    _RcDhcpServerStatsAcks_Type()
)
rcDhcpServerStatsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsAcks.setStatus("mandatory")
_RcDhcpServerStatsNacks_Type = Counter32
_RcDhcpServerStatsNacks_Object = MibScalar
rcDhcpServerStatsNacks = _RcDhcpServerStatsNacks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 7),
    _RcDhcpServerStatsNacks_Type()
)
rcDhcpServerStatsNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsNacks.setStatus("mandatory")
_RcDhcpServerStatsDeclines_Type = Counter32
_RcDhcpServerStatsDeclines_Object = MibScalar
rcDhcpServerStatsDeclines = _RcDhcpServerStatsDeclines_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 8),
    _RcDhcpServerStatsDeclines_Type()
)
rcDhcpServerStatsDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsDeclines.setStatus("mandatory")
_RcDhcpServerStatsInformations_Type = Counter32
_RcDhcpServerStatsInformations_Object = MibScalar
rcDhcpServerStatsInformations = _RcDhcpServerStatsInformations_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 9),
    _RcDhcpServerStatsInformations_Type()
)
rcDhcpServerStatsInformations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsInformations.setStatus("mandatory")
_RcDhcpServerStatsUnknows_Type = Counter32
_RcDhcpServerStatsUnknows_Object = MibScalar
rcDhcpServerStatsUnknows = _RcDhcpServerStatsUnknows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 10),
    _RcDhcpServerStatsUnknows_Type()
)
rcDhcpServerStatsUnknows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsUnknows.setStatus("mandatory")
_RcDhcpServerStatsPackets_Type = Counter32
_RcDhcpServerStatsPackets_Object = MibScalar
rcDhcpServerStatsPackets = _RcDhcpServerStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 12, 1, 2, 11),
    _RcDhcpServerStatsPackets_Type()
)
rcDhcpServerStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpServerStatsPackets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCP-SERVER-MIB",
    **{"rcDhcpServer": rcDhcpServer,
       "rcDhcpServerMibObjects": rcDhcpServerMibObjects,
       "rcDhcpDot1dDhcp": rcDhcpDot1dDhcp,
       "rcDhcpPropEnable": rcDhcpPropEnable,
       "rcDhcpVlanActive": rcDhcpVlanActive,
       "rcDhcpIpNextIndex": rcDhcpIpNextIndex,
       "rcDhcpMaxLease": rcDhcpMaxLease,
       "rcDhcpMinLease": rcDhcpMinLease,
       "rcDhcpDefLease": rcDhcpDefLease,
       "rcDhcpVlanAuth": rcDhcpVlanAuth,
       "rcDhcpServerStartTime": rcDhcpServerStartTime,
       "rcDhcpIpTable": rcDhcpIpTable,
       "rcDhcpIpEntry": rcDhcpIpEntry,
       "rcDhcpIpIndex": rcDhcpIpIndex,
       "rcDhcpIpEntryName": rcDhcpIpEntryName,
       "rcDhcpIpVlanset": rcDhcpIpVlanset,
       "rcDhcpIpStartIp": rcDhcpIpStartIp,
       "rcDhcpIpEndIp": rcDhcpIpEndIp,
       "rcDhcpIpNetmask": rcDhcpIpNetmask,
       "rcDhcpIpGateway": rcDhcpIpGateway,
       "rcDhcpIpDnsServer": rcDhcpIpDnsServer,
       "rcDhcpIpSecondaryDnsServer": rcDhcpIpSecondaryDnsServer,
       "rcDhcpIpRowStatus": rcDhcpIpRowStatus,
       "rcDhcpRelayNextIndex": rcDhcpRelayNextIndex,
       "rcDhcpRelayTable": rcDhcpRelayTable,
       "rcDhcpRelayEntry": rcDhcpRelayEntry,
       "rcDhcpRelayIndex": rcDhcpRelayIndex,
       "rcDhcpRelayAddress": rcDhcpRelayAddress,
       "rcDhcpRelayMask": rcDhcpRelayMask,
       "rcDhcpRelayRowStatus": rcDhcpRelayRowStatus,
       "rcDhcpServerStatistics": rcDhcpServerStatistics,
       "rcDhcpServerStatsBootps": rcDhcpServerStatsBootps,
       "rcDhcpServerStatsDiscovers": rcDhcpServerStatsDiscovers,
       "rcDhcpServerStatsRequests": rcDhcpServerStatsRequests,
       "rcDhcpServerStatsReleases": rcDhcpServerStatsReleases,
       "rcDhcpServerStatsOffers": rcDhcpServerStatsOffers,
       "rcDhcpServerStatsAcks": rcDhcpServerStatsAcks,
       "rcDhcpServerStatsNacks": rcDhcpServerStatsNacks,
       "rcDhcpServerStatsDeclines": rcDhcpServerStatsDeclines,
       "rcDhcpServerStatsInformations": rcDhcpServerStatsInformations,
       "rcDhcpServerStatsUnknows": rcDhcpServerStatsUnknows,
       "rcDhcpServerStatsPackets": rcDhcpServerStatsPackets}
)
