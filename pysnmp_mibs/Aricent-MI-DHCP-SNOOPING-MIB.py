# SNMP MIB module (Aricent-MI-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/Aricent-MI-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:12 2025
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
 enterprises,
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
    "enterprises",
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


# MODULE-IDENTITY

fsMIDhcpSnp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49)
)
if mibBuilder.loadTexts:
    fsMIDhcpSnp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIDhcpSnpGlobalConfig_ObjectIdentity = ObjectIdentity
fsMIDhcpSnpGlobalConfig = _FsMIDhcpSnpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1)
)
_FsMIDhcpSnpGlobalConfigTable_Object = MibTable
fsMIDhcpSnpGlobalConfigTable = _FsMIDhcpSnpGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIDhcpSnpGlobalConfigTable.setStatus("current")
_FsMIDhcpSnpGlobalConfigEntry_Object = MibTableRow
fsMIDhcpSnpGlobalConfigEntry = _FsMIDhcpSnpGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1, 1, 1)
)
fsMIDhcpSnpGlobalConfigEntry.setIndexNames(
    (0, "Aricent-MI-DHCP-SNOOPING-MIB", "fsMIDhcpSnpContextId"),
)
if mibBuilder.loadTexts:
    fsMIDhcpSnpGlobalConfigEntry.setStatus("current")


class _FsMIDhcpSnpContextId_Type(Integer32):
    """Custom type fsMIDhcpSnpContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDhcpSnpContextId_Type.__name__ = "Integer32"
_FsMIDhcpSnpContextId_Object = MibTableColumn
fsMIDhcpSnpContextId = _FsMIDhcpSnpContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1, 1, 1, 1),
    _FsMIDhcpSnpContextId_Type()
)
fsMIDhcpSnpContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDhcpSnpContextId.setStatus("current")


class _FsMIDhcpSnpSnoopingAdminStatus_Type(Integer32):
    """Custom type fsMIDhcpSnpSnoopingAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIDhcpSnpSnoopingAdminStatus_Type.__name__ = "Integer32"
_FsMIDhcpSnpSnoopingAdminStatus_Object = MibTableColumn
fsMIDhcpSnpSnoopingAdminStatus = _FsMIDhcpSnpSnoopingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1, 1, 1, 2),
    _FsMIDhcpSnpSnoopingAdminStatus_Type()
)
fsMIDhcpSnpSnoopingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpSnoopingAdminStatus.setStatus("current")


class _FsMIDhcpSnpMacVerifyStatus_Type(Integer32):
    """Custom type fsMIDhcpSnpMacVerifyStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIDhcpSnpMacVerifyStatus_Type.__name__ = "Integer32"
_FsMIDhcpSnpMacVerifyStatus_Object = MibTableColumn
fsMIDhcpSnpMacVerifyStatus = _FsMIDhcpSnpMacVerifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1, 1, 1, 3),
    _FsMIDhcpSnpMacVerifyStatus_Type()
)
fsMIDhcpSnpMacVerifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpMacVerifyStatus.setStatus("current")


class _FsMIDhcpSnpV6AdminStatus_Type(Integer32):
    """Custom type fsMIDhcpSnpV6AdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIDhcpSnpV6AdminStatus_Type.__name__ = "Integer32"
_FsMIDhcpSnpV6AdminStatus_Object = MibTableColumn
fsMIDhcpSnpV6AdminStatus = _FsMIDhcpSnpV6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1, 1, 1, 4),
    _FsMIDhcpSnpV6AdminStatus_Type()
)
fsMIDhcpSnpV6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6AdminStatus.setStatus("current")


class _FsMIDhcpSnpTraceValue_Type(Integer32):
    """Custom type fsMIDhcpSnpTraceValue based on Integer32"""
    defaultValue = 7


_FsMIDhcpSnpTraceValue_Type.__name__ = "Integer32"
_FsMIDhcpSnpTraceValue_Object = MibTableColumn
fsMIDhcpSnpTraceValue = _FsMIDhcpSnpTraceValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1, 1, 1, 5),
    _FsMIDhcpSnpTraceValue_Type()
)
fsMIDhcpSnpTraceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpTraceValue.setStatus("current")


class _FsMIDhcpSnpV6EnterpriseId_Type(Integer32):
    """Custom type fsMIDhcpSnpV6EnterpriseId based on Integer32"""
    defaultValue = 3561


_FsMIDhcpSnpV6EnterpriseId_Type.__name__ = "Integer32"
_FsMIDhcpSnpV6EnterpriseId_Object = MibTableColumn
fsMIDhcpSnpV6EnterpriseId = _FsMIDhcpSnpV6EnterpriseId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 1, 1, 1, 6),
    _FsMIDhcpSnpV6EnterpriseId_Type()
)
fsMIDhcpSnpV6EnterpriseId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6EnterpriseId.setStatus("current")
_FsMIDhcpSnpInterface_ObjectIdentity = ObjectIdentity
fsMIDhcpSnpInterface = _FsMIDhcpSnpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2)
)
_FsMIDhcpSnpInterfaceTable_Object = MibTable
fsMIDhcpSnpInterfaceTable = _FsMIDhcpSnpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIDhcpSnpInterfaceTable.setStatus("current")
_FsMIDhcpSnpInterfaceEntry_Object = MibTableRow
fsMIDhcpSnpInterfaceEntry = _FsMIDhcpSnpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1)
)
fsMIDhcpSnpInterfaceEntry.setIndexNames(
    (0, "Aricent-MI-DHCP-SNOOPING-MIB", "fsMIDhcpSnpContextId"),
    (0, "Aricent-MI-DHCP-SNOOPING-MIB", "fsMIDhcpSnpVlanId"),
)
if mibBuilder.loadTexts:
    fsMIDhcpSnpInterfaceEntry.setStatus("current")


class _FsMIDhcpSnpVlanId_Type(Integer32):
    """Custom type fsMIDhcpSnpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIDhcpSnpVlanId_Type.__name__ = "Integer32"
_FsMIDhcpSnpVlanId_Object = MibTableColumn
fsMIDhcpSnpVlanId = _FsMIDhcpSnpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 2),
    _FsMIDhcpSnpVlanId_Type()
)
fsMIDhcpSnpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDhcpSnpVlanId.setStatus("current")


class _FsMIDhcpSnpVlanSnpStatus_Type(Integer32):
    """Custom type fsMIDhcpSnpVlanSnpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIDhcpSnpVlanSnpStatus_Type.__name__ = "Integer32"
_FsMIDhcpSnpVlanSnpStatus_Object = MibTableColumn
fsMIDhcpSnpVlanSnpStatus = _FsMIDhcpSnpVlanSnpStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 3),
    _FsMIDhcpSnpVlanSnpStatus_Type()
)
fsMIDhcpSnpVlanSnpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpVlanSnpStatus.setStatus("current")
_FsMIDhcpSnpRxDiscovers_Type = Counter32
_FsMIDhcpSnpRxDiscovers_Object = MibTableColumn
fsMIDhcpSnpRxDiscovers = _FsMIDhcpSnpRxDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 4),
    _FsMIDhcpSnpRxDiscovers_Type()
)
fsMIDhcpSnpRxDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpRxDiscovers.setStatus("current")
_FsMIDhcpSnpRxRequests_Type = Counter32
_FsMIDhcpSnpRxRequests_Object = MibTableColumn
fsMIDhcpSnpRxRequests = _FsMIDhcpSnpRxRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 5),
    _FsMIDhcpSnpRxRequests_Type()
)
fsMIDhcpSnpRxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpRxRequests.setStatus("current")
_FsMIDhcpSnpRxReleases_Type = Counter32
_FsMIDhcpSnpRxReleases_Object = MibTableColumn
fsMIDhcpSnpRxReleases = _FsMIDhcpSnpRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 6),
    _FsMIDhcpSnpRxReleases_Type()
)
fsMIDhcpSnpRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpRxReleases.setStatus("current")
_FsMIDhcpSnpRxDeclines_Type = Counter32
_FsMIDhcpSnpRxDeclines_Object = MibTableColumn
fsMIDhcpSnpRxDeclines = _FsMIDhcpSnpRxDeclines_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 7),
    _FsMIDhcpSnpRxDeclines_Type()
)
fsMIDhcpSnpRxDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpRxDeclines.setStatus("current")
_FsMIDhcpSnpRxInforms_Type = Counter32
_FsMIDhcpSnpRxInforms_Object = MibTableColumn
fsMIDhcpSnpRxInforms = _FsMIDhcpSnpRxInforms_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 8),
    _FsMIDhcpSnpRxInforms_Type()
)
fsMIDhcpSnpRxInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpRxInforms.setStatus("current")
_FsMIDhcpSnpTxOffers_Type = Counter32
_FsMIDhcpSnpTxOffers_Object = MibTableColumn
fsMIDhcpSnpTxOffers = _FsMIDhcpSnpTxOffers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 9),
    _FsMIDhcpSnpTxOffers_Type()
)
fsMIDhcpSnpTxOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpTxOffers.setStatus("current")
_FsMIDhcpSnpTxAcks_Type = Counter32
_FsMIDhcpSnpTxAcks_Object = MibTableColumn
fsMIDhcpSnpTxAcks = _FsMIDhcpSnpTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 10),
    _FsMIDhcpSnpTxAcks_Type()
)
fsMIDhcpSnpTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpTxAcks.setStatus("current")
_FsMIDhcpSnpTxNaks_Type = Counter32
_FsMIDhcpSnpTxNaks_Object = MibTableColumn
fsMIDhcpSnpTxNaks = _FsMIDhcpSnpTxNaks_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 11),
    _FsMIDhcpSnpTxNaks_Type()
)
fsMIDhcpSnpTxNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpTxNaks.setStatus("current")
_FsMIDhcpSnpNoOfDiscards_Type = Counter32
_FsMIDhcpSnpNoOfDiscards_Object = MibTableColumn
fsMIDhcpSnpNoOfDiscards = _FsMIDhcpSnpNoOfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 12),
    _FsMIDhcpSnpNoOfDiscards_Type()
)
fsMIDhcpSnpNoOfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpNoOfDiscards.setStatus("current")
_FsMIDhcpSnpMacDiscards_Type = Counter32
_FsMIDhcpSnpMacDiscards_Object = MibTableColumn
fsMIDhcpSnpMacDiscards = _FsMIDhcpSnpMacDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 13),
    _FsMIDhcpSnpMacDiscards_Type()
)
fsMIDhcpSnpMacDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpMacDiscards.setStatus("current")
_FsMIDhcpSnpServerDiscards_Type = Counter32
_FsMIDhcpSnpServerDiscards_Object = MibTableColumn
fsMIDhcpSnpServerDiscards = _FsMIDhcpSnpServerDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 14),
    _FsMIDhcpSnpServerDiscards_Type()
)
fsMIDhcpSnpServerDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpServerDiscards.setStatus("current")
_FsMIDhcpSnpOptionDiscards_Type = Counter32
_FsMIDhcpSnpOptionDiscards_Object = MibTableColumn
fsMIDhcpSnpOptionDiscards = _FsMIDhcpSnpOptionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 15),
    _FsMIDhcpSnpOptionDiscards_Type()
)
fsMIDhcpSnpOptionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpOptionDiscards.setStatus("current")
_FsMIDhcpSnpInterfaceStatus_Type = RowStatus
_FsMIDhcpSnpInterfaceStatus_Object = MibTableColumn
fsMIDhcpSnpInterfaceStatus = _FsMIDhcpSnpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 16),
    _FsMIDhcpSnpInterfaceStatus_Type()
)
fsMIDhcpSnpInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpInterfaceStatus.setStatus("current")


class _FsMIDhcpSnpV6VlanSnpStatus_Type(Integer32):
    """Custom type fsMIDhcpSnpV6VlanSnpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIDhcpSnpV6VlanSnpStatus_Type.__name__ = "Integer32"
_FsMIDhcpSnpV6VlanSnpStatus_Object = MibTableColumn
fsMIDhcpSnpV6VlanSnpStatus = _FsMIDhcpSnpV6VlanSnpStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 17),
    _FsMIDhcpSnpV6VlanSnpStatus_Type()
)
fsMIDhcpSnpV6VlanSnpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6VlanSnpStatus.setStatus("current")
_FsMIDhcpSnpV6RxClientPkts_Type = Counter32
_FsMIDhcpSnpV6RxClientPkts_Object = MibTableColumn
fsMIDhcpSnpV6RxClientPkts = _FsMIDhcpSnpV6RxClientPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 18),
    _FsMIDhcpSnpV6RxClientPkts_Type()
)
fsMIDhcpSnpV6RxClientPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6RxClientPkts.setStatus("current")
_FsMIDhcpSnpV6TxClientPkts_Type = Counter32
_FsMIDhcpSnpV6TxClientPkts_Object = MibTableColumn
fsMIDhcpSnpV6TxClientPkts = _FsMIDhcpSnpV6TxClientPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 19),
    _FsMIDhcpSnpV6TxClientPkts_Type()
)
fsMIDhcpSnpV6TxClientPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6TxClientPkts.setStatus("current")
_FsMIDhcpSnpV6TxRelayForwards_Type = Counter32
_FsMIDhcpSnpV6TxRelayForwards_Object = MibTableColumn
fsMIDhcpSnpV6TxRelayForwards = _FsMIDhcpSnpV6TxRelayForwards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 20),
    _FsMIDhcpSnpV6TxRelayForwards_Type()
)
fsMIDhcpSnpV6TxRelayForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6TxRelayForwards.setStatus("current")
_FsMIDhcpSnpV6RxRelayReplys_Type = Counter32
_FsMIDhcpSnpV6RxRelayReplys_Object = MibTableColumn
fsMIDhcpSnpV6RxRelayReplys = _FsMIDhcpSnpV6RxRelayReplys_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 21),
    _FsMIDhcpSnpV6RxRelayReplys_Type()
)
fsMIDhcpSnpV6RxRelayReplys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6RxRelayReplys.setStatus("current")
_FsMIDhcpSnpV6PktDrops_Type = Counter32
_FsMIDhcpSnpV6PktDrops_Object = MibTableColumn
fsMIDhcpSnpV6PktDrops = _FsMIDhcpSnpV6PktDrops_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 22),
    _FsMIDhcpSnpV6PktDrops_Type()
)
fsMIDhcpSnpV6PktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6PktDrops.setStatus("current")


class _FsMIDhcpSnpV6ClearStatistics_Type(Integer32):
    """Custom type fsMIDhcpSnpV6ClearStatistics based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIDhcpSnpV6ClearStatistics_Type.__name__ = "Integer32"
_FsMIDhcpSnpV6ClearStatistics_Object = MibTableColumn
fsMIDhcpSnpV6ClearStatistics = _FsMIDhcpSnpV6ClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 49, 2, 1, 1, 23),
    _FsMIDhcpSnpV6ClearStatistics_Type()
)
fsMIDhcpSnpV6ClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpSnpV6ClearStatistics.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Aricent-MI-DHCP-SNOOPING-MIB",
    **{"fsMIDhcpSnp": fsMIDhcpSnp,
       "fsMIDhcpSnpGlobalConfig": fsMIDhcpSnpGlobalConfig,
       "fsMIDhcpSnpGlobalConfigTable": fsMIDhcpSnpGlobalConfigTable,
       "fsMIDhcpSnpGlobalConfigEntry": fsMIDhcpSnpGlobalConfigEntry,
       "fsMIDhcpSnpContextId": fsMIDhcpSnpContextId,
       "fsMIDhcpSnpSnoopingAdminStatus": fsMIDhcpSnpSnoopingAdminStatus,
       "fsMIDhcpSnpMacVerifyStatus": fsMIDhcpSnpMacVerifyStatus,
       "fsMIDhcpSnpV6AdminStatus": fsMIDhcpSnpV6AdminStatus,
       "fsMIDhcpSnpTraceValue": fsMIDhcpSnpTraceValue,
       "fsMIDhcpSnpV6EnterpriseId": fsMIDhcpSnpV6EnterpriseId,
       "fsMIDhcpSnpInterface": fsMIDhcpSnpInterface,
       "fsMIDhcpSnpInterfaceTable": fsMIDhcpSnpInterfaceTable,
       "fsMIDhcpSnpInterfaceEntry": fsMIDhcpSnpInterfaceEntry,
       "fsMIDhcpSnpVlanId": fsMIDhcpSnpVlanId,
       "fsMIDhcpSnpVlanSnpStatus": fsMIDhcpSnpVlanSnpStatus,
       "fsMIDhcpSnpRxDiscovers": fsMIDhcpSnpRxDiscovers,
       "fsMIDhcpSnpRxRequests": fsMIDhcpSnpRxRequests,
       "fsMIDhcpSnpRxReleases": fsMIDhcpSnpRxReleases,
       "fsMIDhcpSnpRxDeclines": fsMIDhcpSnpRxDeclines,
       "fsMIDhcpSnpRxInforms": fsMIDhcpSnpRxInforms,
       "fsMIDhcpSnpTxOffers": fsMIDhcpSnpTxOffers,
       "fsMIDhcpSnpTxAcks": fsMIDhcpSnpTxAcks,
       "fsMIDhcpSnpTxNaks": fsMIDhcpSnpTxNaks,
       "fsMIDhcpSnpNoOfDiscards": fsMIDhcpSnpNoOfDiscards,
       "fsMIDhcpSnpMacDiscards": fsMIDhcpSnpMacDiscards,
       "fsMIDhcpSnpServerDiscards": fsMIDhcpSnpServerDiscards,
       "fsMIDhcpSnpOptionDiscards": fsMIDhcpSnpOptionDiscards,
       "fsMIDhcpSnpInterfaceStatus": fsMIDhcpSnpInterfaceStatus,
       "fsMIDhcpSnpV6VlanSnpStatus": fsMIDhcpSnpV6VlanSnpStatus,
       "fsMIDhcpSnpV6RxClientPkts": fsMIDhcpSnpV6RxClientPkts,
       "fsMIDhcpSnpV6TxClientPkts": fsMIDhcpSnpV6TxClientPkts,
       "fsMIDhcpSnpV6TxRelayForwards": fsMIDhcpSnpV6TxRelayForwards,
       "fsMIDhcpSnpV6RxRelayReplys": fsMIDhcpSnpV6RxRelayReplys,
       "fsMIDhcpSnpV6PktDrops": fsMIDhcpSnpV6PktDrops,
       "fsMIDhcpSnpV6ClearStatistics": fsMIDhcpSnpV6ClearStatistics}
)
