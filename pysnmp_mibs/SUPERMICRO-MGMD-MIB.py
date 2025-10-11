# SNMP MIB module (SUPERMICRO-MGMD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MGMD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:09 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsmgmdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62)
)
if mibBuilder.loadTexts:
    fsmgmdMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fsmgmd_ObjectIdentity = ObjectIdentity
fsmgmd = _Fsmgmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1)
)


class _FsMgmdIgmpGlobalStatus_Type(Integer32):
    """Custom type fsMgmdIgmpGlobalStatus based on Integer32"""
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


_FsMgmdIgmpGlobalStatus_Type.__name__ = "Integer32"
_FsMgmdIgmpGlobalStatus_Object = MibScalar
fsMgmdIgmpGlobalStatus = _FsMgmdIgmpGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 1),
    _FsMgmdIgmpGlobalStatus_Type()
)
fsMgmdIgmpGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMgmdIgmpGlobalStatus.setStatus("current")


class _FsMgmdIgmpTraceLevel_Type(Integer32):
    """Custom type fsMgmdIgmpTraceLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMgmdIgmpTraceLevel_Type.__name__ = "Integer32"
_FsMgmdIgmpTraceLevel_Object = MibScalar
fsMgmdIgmpTraceLevel = _FsMgmdIgmpTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 2),
    _FsMgmdIgmpTraceLevel_Type()
)
fsMgmdIgmpTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMgmdIgmpTraceLevel.setStatus("current")


class _FsMgmdMldGlobalStatus_Type(Integer32):
    """Custom type fsMgmdMldGlobalStatus based on Integer32"""
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


_FsMgmdMldGlobalStatus_Type.__name__ = "Integer32"
_FsMgmdMldGlobalStatus_Object = MibScalar
fsMgmdMldGlobalStatus = _FsMgmdMldGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 3),
    _FsMgmdMldGlobalStatus_Type()
)
fsMgmdMldGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMgmdMldGlobalStatus.setStatus("current")


class _FsMgmdMldTraceLevel_Type(Integer32):
    """Custom type fsMgmdMldTraceLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMgmdMldTraceLevel_Type.__name__ = "Integer32"
_FsMgmdMldTraceLevel_Object = MibScalar
fsMgmdMldTraceLevel = _FsMgmdMldTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 4),
    _FsMgmdMldTraceLevel_Type()
)
fsMgmdMldTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMgmdMldTraceLevel.setStatus("current")
_FsMgmdInterfaceTable_Object = MibTable
fsMgmdInterfaceTable = _FsMgmdInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5)
)
if mibBuilder.loadTexts:
    fsMgmdInterfaceTable.setStatus("current")
_FsMgmdInterfaceEntry_Object = MibTableRow
fsMgmdInterfaceEntry = _FsMgmdInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1)
)
fsMgmdInterfaceEntry.setIndexNames(
    (0, "SUPERMICRO-MGMD-MIB", "fsMgmdInterfaceIfIndex"),
    (0, "SUPERMICRO-MGMD-MIB", "fsMgmdInterfaceAddrType"),
)
if mibBuilder.loadTexts:
    fsMgmdInterfaceEntry.setStatus("current")
_FsMgmdInterfaceIfIndex_Type = InterfaceIndex
_FsMgmdInterfaceIfIndex_Object = MibTableColumn
fsMgmdInterfaceIfIndex = _FsMgmdInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 1),
    _FsMgmdInterfaceIfIndex_Type()
)
fsMgmdInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMgmdInterfaceIfIndex.setStatus("current")
_FsMgmdInterfaceAddrType_Type = InetAddressType
_FsMgmdInterfaceAddrType_Object = MibTableColumn
fsMgmdInterfaceAddrType = _FsMgmdInterfaceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 2),
    _FsMgmdInterfaceAddrType_Type()
)
fsMgmdInterfaceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMgmdInterfaceAddrType.setStatus("current")


class _FsMgmdInterfaceAdminStatus_Type(Integer32):
    """Custom type fsMgmdInterfaceAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsMgmdInterfaceAdminStatus_Type.__name__ = "Integer32"
_FsMgmdInterfaceAdminStatus_Object = MibTableColumn
fsMgmdInterfaceAdminStatus = _FsMgmdInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 3),
    _FsMgmdInterfaceAdminStatus_Type()
)
fsMgmdInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMgmdInterfaceAdminStatus.setStatus("current")


class _FsMgmdInterfaceFastLeaveStatus_Type(Integer32):
    """Custom type fsMgmdInterfaceFastLeaveStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsMgmdInterfaceFastLeaveStatus_Type.__name__ = "Integer32"
_FsMgmdInterfaceFastLeaveStatus_Object = MibTableColumn
fsMgmdInterfaceFastLeaveStatus = _FsMgmdInterfaceFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 4),
    _FsMgmdInterfaceFastLeaveStatus_Type()
)
fsMgmdInterfaceFastLeaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMgmdInterfaceFastLeaveStatus.setStatus("current")


class _FsMgmdInterfaceOperStatus_Type(Integer32):
    """Custom type fsMgmdInterfaceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsMgmdInterfaceOperStatus_Type.__name__ = "Integer32"
_FsMgmdInterfaceOperStatus_Object = MibTableColumn
fsMgmdInterfaceOperStatus = _FsMgmdInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 5),
    _FsMgmdInterfaceOperStatus_Type()
)
fsMgmdInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceOperStatus.setStatus("current")
_FsMgmdInterfaceIncomingPkts_Type = Counter32
_FsMgmdInterfaceIncomingPkts_Object = MibTableColumn
fsMgmdInterfaceIncomingPkts = _FsMgmdInterfaceIncomingPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 6),
    _FsMgmdInterfaceIncomingPkts_Type()
)
fsMgmdInterfaceIncomingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceIncomingPkts.setStatus("current")
_FsMgmdInterfaceIncomingJoins_Type = Counter32
_FsMgmdInterfaceIncomingJoins_Object = MibTableColumn
fsMgmdInterfaceIncomingJoins = _FsMgmdInterfaceIncomingJoins_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 7),
    _FsMgmdInterfaceIncomingJoins_Type()
)
fsMgmdInterfaceIncomingJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceIncomingJoins.setStatus("current")
_FsMgmdInterfaceIncomingLeaves_Type = Counter32
_FsMgmdInterfaceIncomingLeaves_Object = MibTableColumn
fsMgmdInterfaceIncomingLeaves = _FsMgmdInterfaceIncomingLeaves_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 8),
    _FsMgmdInterfaceIncomingLeaves_Type()
)
fsMgmdInterfaceIncomingLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceIncomingLeaves.setStatus("current")
_FsMgmdInterfaceIncomingQueries_Type = Counter32
_FsMgmdInterfaceIncomingQueries_Object = MibTableColumn
fsMgmdInterfaceIncomingQueries = _FsMgmdInterfaceIncomingQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 9),
    _FsMgmdInterfaceIncomingQueries_Type()
)
fsMgmdInterfaceIncomingQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceIncomingQueries.setStatus("current")
_FsMgmdInterfaceOutgoingQueries_Type = Counter32
_FsMgmdInterfaceOutgoingQueries_Object = MibTableColumn
fsMgmdInterfaceOutgoingQueries = _FsMgmdInterfaceOutgoingQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 10),
    _FsMgmdInterfaceOutgoingQueries_Type()
)
fsMgmdInterfaceOutgoingQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceOutgoingQueries.setStatus("current")
_FsMgmdInterfaceRxGenQueries_Type = Counter32
_FsMgmdInterfaceRxGenQueries_Object = MibTableColumn
fsMgmdInterfaceRxGenQueries = _FsMgmdInterfaceRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 11),
    _FsMgmdInterfaceRxGenQueries_Type()
)
fsMgmdInterfaceRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceRxGenQueries.setStatus("current")
_FsMgmdInterfaceRxGrpQueries_Type = Counter32
_FsMgmdInterfaceRxGrpQueries_Object = MibTableColumn
fsMgmdInterfaceRxGrpQueries = _FsMgmdInterfaceRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 12),
    _FsMgmdInterfaceRxGrpQueries_Type()
)
fsMgmdInterfaceRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceRxGrpQueries.setStatus("current")
_FsMgmdInterfaceRxGrpAndSrcQueries_Type = Counter32
_FsMgmdInterfaceRxGrpAndSrcQueries_Object = MibTableColumn
fsMgmdInterfaceRxGrpAndSrcQueries = _FsMgmdInterfaceRxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 13),
    _FsMgmdInterfaceRxGrpAndSrcQueries_Type()
)
fsMgmdInterfaceRxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceRxGrpAndSrcQueries.setStatus("current")
_FsMgmdInterfaceRxIgmpv1v2Reports_Type = Counter32
_FsMgmdInterfaceRxIgmpv1v2Reports_Object = MibTableColumn
fsMgmdInterfaceRxIgmpv1v2Reports = _FsMgmdInterfaceRxIgmpv1v2Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 14),
    _FsMgmdInterfaceRxIgmpv1v2Reports_Type()
)
fsMgmdInterfaceRxIgmpv1v2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceRxIgmpv1v2Reports.setStatus("current")
_FsMgmdInterfaceRxIgmpv3Reports_Type = Counter32
_FsMgmdInterfaceRxIgmpv3Reports_Object = MibTableColumn
fsMgmdInterfaceRxIgmpv3Reports = _FsMgmdInterfaceRxIgmpv3Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 15),
    _FsMgmdInterfaceRxIgmpv3Reports_Type()
)
fsMgmdInterfaceRxIgmpv3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceRxIgmpv3Reports.setStatus("current")
_FsMgmdInterfaceRxMldv1Reports_Type = Counter32
_FsMgmdInterfaceRxMldv1Reports_Object = MibTableColumn
fsMgmdInterfaceRxMldv1Reports = _FsMgmdInterfaceRxMldv1Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 16),
    _FsMgmdInterfaceRxMldv1Reports_Type()
)
fsMgmdInterfaceRxMldv1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceRxMldv1Reports.setStatus("current")
_FsMgmdInterfaceRxMldv2Reports_Type = Counter32
_FsMgmdInterfaceRxMldv2Reports_Object = MibTableColumn
fsMgmdInterfaceRxMldv2Reports = _FsMgmdInterfaceRxMldv2Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 17),
    _FsMgmdInterfaceRxMldv2Reports_Type()
)
fsMgmdInterfaceRxMldv2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceRxMldv2Reports.setStatus("current")
_FsMgmdInterfaceTxGenQueries_Type = Counter32
_FsMgmdInterfaceTxGenQueries_Object = MibTableColumn
fsMgmdInterfaceTxGenQueries = _FsMgmdInterfaceTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 18),
    _FsMgmdInterfaceTxGenQueries_Type()
)
fsMgmdInterfaceTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceTxGenQueries.setStatus("current")
_FsMgmdInterfaceTxGrpQueries_Type = Counter32
_FsMgmdInterfaceTxGrpQueries_Object = MibTableColumn
fsMgmdInterfaceTxGrpQueries = _FsMgmdInterfaceTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 19),
    _FsMgmdInterfaceTxGrpQueries_Type()
)
fsMgmdInterfaceTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceTxGrpQueries.setStatus("current")
_FsMgmdInterfaceTxGrpAndSrcQueries_Type = Counter32
_FsMgmdInterfaceTxGrpAndSrcQueries_Object = MibTableColumn
fsMgmdInterfaceTxGrpAndSrcQueries = _FsMgmdInterfaceTxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 20),
    _FsMgmdInterfaceTxGrpAndSrcQueries_Type()
)
fsMgmdInterfaceTxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceTxGrpAndSrcQueries.setStatus("current")
_FsMgmdInterfaceTxIgmpv1v2Reports_Type = Counter32
_FsMgmdInterfaceTxIgmpv1v2Reports_Object = MibTableColumn
fsMgmdInterfaceTxIgmpv1v2Reports = _FsMgmdInterfaceTxIgmpv1v2Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 21),
    _FsMgmdInterfaceTxIgmpv1v2Reports_Type()
)
fsMgmdInterfaceTxIgmpv1v2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceTxIgmpv1v2Reports.setStatus("current")
_FsMgmdInterfaceTxIgmpv3Reports_Type = Counter32
_FsMgmdInterfaceTxIgmpv3Reports_Object = MibTableColumn
fsMgmdInterfaceTxIgmpv3Reports = _FsMgmdInterfaceTxIgmpv3Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 22),
    _FsMgmdInterfaceTxIgmpv3Reports_Type()
)
fsMgmdInterfaceTxIgmpv3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceTxIgmpv3Reports.setStatus("current")
_FsMgmdInterfaceTxMldv1Reports_Type = Counter32
_FsMgmdInterfaceTxMldv1Reports_Object = MibTableColumn
fsMgmdInterfaceTxMldv1Reports = _FsMgmdInterfaceTxMldv1Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 23),
    _FsMgmdInterfaceTxMldv1Reports_Type()
)
fsMgmdInterfaceTxMldv1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceTxMldv1Reports.setStatus("current")
_FsMgmdInterfaceTxMldv2Reports_Type = Counter32
_FsMgmdInterfaceTxMldv2Reports_Object = MibTableColumn
fsMgmdInterfaceTxMldv2Reports = _FsMgmdInterfaceTxMldv2Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 24),
    _FsMgmdInterfaceTxMldv2Reports_Type()
)
fsMgmdInterfaceTxMldv2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceTxMldv2Reports.setStatus("current")
_FsMgmdInterfaceTxLeaves_Type = Counter32
_FsMgmdInterfaceTxLeaves_Object = MibTableColumn
fsMgmdInterfaceTxLeaves = _FsMgmdInterfaceTxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 5, 1, 25),
    _FsMgmdInterfaceTxLeaves_Type()
)
fsMgmdInterfaceTxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdInterfaceTxLeaves.setStatus("current")
_FsMgmdCacheTable_Object = MibTable
fsMgmdCacheTable = _FsMgmdCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 26)
)
if mibBuilder.loadTexts:
    fsMgmdCacheTable.setStatus("current")
_FsMgmdCacheEntry_Object = MibTableRow
fsMgmdCacheEntry = _FsMgmdCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 26, 1)
)
fsMgmdCacheEntry.setIndexNames(
    (0, "SUPERMICRO-MGMD-MIB", "fsMgmdCacheAddrType"),
    (0, "SUPERMICRO-MGMD-MIB", "fsMgmdCacheAddress"),
    (0, "SUPERMICRO-MGMD-MIB", "fsMgmdCacheIfIndex"),
)
if mibBuilder.loadTexts:
    fsMgmdCacheEntry.setStatus("current")
_FsMgmdCacheAddrType_Type = InetAddressType
_FsMgmdCacheAddrType_Object = MibTableColumn
fsMgmdCacheAddrType = _FsMgmdCacheAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 26, 1, 1),
    _FsMgmdCacheAddrType_Type()
)
fsMgmdCacheAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMgmdCacheAddrType.setStatus("current")


class _FsMgmdCacheAddress_Type(InetAddress):
    """Custom type fsMgmdCacheAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_FsMgmdCacheAddress_Type.__name__ = "InetAddress"
_FsMgmdCacheAddress_Object = MibTableColumn
fsMgmdCacheAddress = _FsMgmdCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 26, 1, 2),
    _FsMgmdCacheAddress_Type()
)
fsMgmdCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMgmdCacheAddress.setStatus("current")
_FsMgmdCacheIfIndex_Type = InterfaceIndex
_FsMgmdCacheIfIndex_Object = MibTableColumn
fsMgmdCacheIfIndex = _FsMgmdCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 26, 1, 3),
    _FsMgmdCacheIfIndex_Type()
)
fsMgmdCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMgmdCacheIfIndex.setStatus("current")
_FsMgmdCacheGroupCompMode_Type = Integer32
_FsMgmdCacheGroupCompMode_Object = MibTableColumn
fsMgmdCacheGroupCompMode = _FsMgmdCacheGroupCompMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 62, 1, 26, 1, 4),
    _FsMgmdCacheGroupCompMode_Type()
)
fsMgmdCacheGroupCompMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMgmdCacheGroupCompMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MGMD-MIB",
    **{"fsmgmdMIB": fsmgmdMIB,
       "fsmgmd": fsmgmd,
       "fsMgmdIgmpGlobalStatus": fsMgmdIgmpGlobalStatus,
       "fsMgmdIgmpTraceLevel": fsMgmdIgmpTraceLevel,
       "fsMgmdMldGlobalStatus": fsMgmdMldGlobalStatus,
       "fsMgmdMldTraceLevel": fsMgmdMldTraceLevel,
       "fsMgmdInterfaceTable": fsMgmdInterfaceTable,
       "fsMgmdInterfaceEntry": fsMgmdInterfaceEntry,
       "fsMgmdInterfaceIfIndex": fsMgmdInterfaceIfIndex,
       "fsMgmdInterfaceAddrType": fsMgmdInterfaceAddrType,
       "fsMgmdInterfaceAdminStatus": fsMgmdInterfaceAdminStatus,
       "fsMgmdInterfaceFastLeaveStatus": fsMgmdInterfaceFastLeaveStatus,
       "fsMgmdInterfaceOperStatus": fsMgmdInterfaceOperStatus,
       "fsMgmdInterfaceIncomingPkts": fsMgmdInterfaceIncomingPkts,
       "fsMgmdInterfaceIncomingJoins": fsMgmdInterfaceIncomingJoins,
       "fsMgmdInterfaceIncomingLeaves": fsMgmdInterfaceIncomingLeaves,
       "fsMgmdInterfaceIncomingQueries": fsMgmdInterfaceIncomingQueries,
       "fsMgmdInterfaceOutgoingQueries": fsMgmdInterfaceOutgoingQueries,
       "fsMgmdInterfaceRxGenQueries": fsMgmdInterfaceRxGenQueries,
       "fsMgmdInterfaceRxGrpQueries": fsMgmdInterfaceRxGrpQueries,
       "fsMgmdInterfaceRxGrpAndSrcQueries": fsMgmdInterfaceRxGrpAndSrcQueries,
       "fsMgmdInterfaceRxIgmpv1v2Reports": fsMgmdInterfaceRxIgmpv1v2Reports,
       "fsMgmdInterfaceRxIgmpv3Reports": fsMgmdInterfaceRxIgmpv3Reports,
       "fsMgmdInterfaceRxMldv1Reports": fsMgmdInterfaceRxMldv1Reports,
       "fsMgmdInterfaceRxMldv2Reports": fsMgmdInterfaceRxMldv2Reports,
       "fsMgmdInterfaceTxGenQueries": fsMgmdInterfaceTxGenQueries,
       "fsMgmdInterfaceTxGrpQueries": fsMgmdInterfaceTxGrpQueries,
       "fsMgmdInterfaceTxGrpAndSrcQueries": fsMgmdInterfaceTxGrpAndSrcQueries,
       "fsMgmdInterfaceTxIgmpv1v2Reports": fsMgmdInterfaceTxIgmpv1v2Reports,
       "fsMgmdInterfaceTxIgmpv3Reports": fsMgmdInterfaceTxIgmpv3Reports,
       "fsMgmdInterfaceTxMldv1Reports": fsMgmdInterfaceTxMldv1Reports,
       "fsMgmdInterfaceTxMldv2Reports": fsMgmdInterfaceTxMldv2Reports,
       "fsMgmdInterfaceTxLeaves": fsMgmdInterfaceTxLeaves,
       "fsMgmdCacheTable": fsMgmdCacheTable,
       "fsMgmdCacheEntry": fsMgmdCacheEntry,
       "fsMgmdCacheAddrType": fsMgmdCacheAddrType,
       "fsMgmdCacheAddress": fsMgmdCacheAddress,
       "fsMgmdCacheIfIndex": fsMgmdCacheIfIndex,
       "fsMgmdCacheGroupCompMode": fsMgmdCacheGroupCompMode}
)
