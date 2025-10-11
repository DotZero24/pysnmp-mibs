# SNMP MIB module (SUPERMICRO-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-IGMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:21 2025
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

fsigmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36)
)
if mibBuilder.loadTexts:
    fsigmpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fsigmp_ObjectIdentity = ObjectIdentity
fsigmp = _Fsigmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1)
)


class _FsIgmpGlobalStatus_Type(Integer32):
    """Custom type fsIgmpGlobalStatus based on Integer32"""
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


_FsIgmpGlobalStatus_Type.__name__ = "Integer32"
_FsIgmpGlobalStatus_Object = MibScalar
fsIgmpGlobalStatus = _FsIgmpGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 1),
    _FsIgmpGlobalStatus_Type()
)
fsIgmpGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpGlobalStatus.setStatus("current")


class _FsIgmpTraceLevel_Type(Integer32):
    """Custom type fsIgmpTraceLevel based on Integer32"""
    defaultValue = 0


_FsIgmpTraceLevel_Type.__name__ = "Integer32"
_FsIgmpTraceLevel_Object = MibScalar
fsIgmpTraceLevel = _FsIgmpTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 2),
    _FsIgmpTraceLevel_Type()
)
fsIgmpTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpTraceLevel.setStatus("current")
_FsIgmpInterfaceTable_Object = MibTable
fsIgmpInterfaceTable = _FsIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3)
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceTable.setStatus("current")
_FsIgmpInterfaceEntry_Object = MibTableRow
fsIgmpInterfaceEntry = _FsIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1)
)
fsIgmpInterfaceEntry.setIndexNames(
    (0, "SUPERMICRO-IGMP-MIB", "fsIgmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceEntry.setStatus("current")
_FsIgmpInterfaceIfIndex_Type = InterfaceIndex
_FsIgmpInterfaceIfIndex_Object = MibTableColumn
fsIgmpInterfaceIfIndex = _FsIgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 1),
    _FsIgmpInterfaceIfIndex_Type()
)
fsIgmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIfIndex.setStatus("current")


class _FsIgmpInterfaceAdminStatus_Type(Integer32):
    """Custom type fsIgmpInterfaceAdminStatus based on Integer32"""
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


_FsIgmpInterfaceAdminStatus_Type.__name__ = "Integer32"
_FsIgmpInterfaceAdminStatus_Object = MibTableColumn
fsIgmpInterfaceAdminStatus = _FsIgmpInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 2),
    _FsIgmpInterfaceAdminStatus_Type()
)
fsIgmpInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceAdminStatus.setStatus("current")


class _FsIgmpInterfaceFastLeaveStatus_Type(Integer32):
    """Custom type fsIgmpInterfaceFastLeaveStatus based on Integer32"""
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


_FsIgmpInterfaceFastLeaveStatus_Type.__name__ = "Integer32"
_FsIgmpInterfaceFastLeaveStatus_Object = MibTableColumn
fsIgmpInterfaceFastLeaveStatus = _FsIgmpInterfaceFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 3),
    _FsIgmpInterfaceFastLeaveStatus_Type()
)
fsIgmpInterfaceFastLeaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceFastLeaveStatus.setStatus("current")


class _FsIgmpInterfaceOperStatus_Type(Integer32):
    """Custom type fsIgmpInterfaceOperStatus based on Integer32"""
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


_FsIgmpInterfaceOperStatus_Type.__name__ = "Integer32"
_FsIgmpInterfaceOperStatus_Object = MibTableColumn
fsIgmpInterfaceOperStatus = _FsIgmpInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 4),
    _FsIgmpInterfaceOperStatus_Type()
)
fsIgmpInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceOperStatus.setStatus("current")
_FsIgmpInterfaceIncomingPkts_Type = Counter32
_FsIgmpInterfaceIncomingPkts_Object = MibTableColumn
fsIgmpInterfaceIncomingPkts = _FsIgmpInterfaceIncomingPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 5),
    _FsIgmpInterfaceIncomingPkts_Type()
)
fsIgmpInterfaceIncomingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingPkts.setStatus("current")
_FsIgmpInterfaceIncomingJoins_Type = Counter32
_FsIgmpInterfaceIncomingJoins_Object = MibTableColumn
fsIgmpInterfaceIncomingJoins = _FsIgmpInterfaceIncomingJoins_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 6),
    _FsIgmpInterfaceIncomingJoins_Type()
)
fsIgmpInterfaceIncomingJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingJoins.setStatus("current")
_FsIgmpInterfaceIncomingLeaves_Type = Counter32
_FsIgmpInterfaceIncomingLeaves_Object = MibTableColumn
fsIgmpInterfaceIncomingLeaves = _FsIgmpInterfaceIncomingLeaves_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 7),
    _FsIgmpInterfaceIncomingLeaves_Type()
)
fsIgmpInterfaceIncomingLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingLeaves.setStatus("current")
_FsIgmpInterfaceIncomingQueries_Type = Counter32
_FsIgmpInterfaceIncomingQueries_Object = MibTableColumn
fsIgmpInterfaceIncomingQueries = _FsIgmpInterfaceIncomingQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 8),
    _FsIgmpInterfaceIncomingQueries_Type()
)
fsIgmpInterfaceIncomingQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingQueries.setStatus("current")
_FsIgmpInterfaceOutgoingQueries_Type = Counter32
_FsIgmpInterfaceOutgoingQueries_Object = MibTableColumn
fsIgmpInterfaceOutgoingQueries = _FsIgmpInterfaceOutgoingQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 9),
    _FsIgmpInterfaceOutgoingQueries_Type()
)
fsIgmpInterfaceOutgoingQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceOutgoingQueries.setStatus("current")
_FsIgmpInterfaceRxGenQueries_Type = Counter32
_FsIgmpInterfaceRxGenQueries_Object = MibTableColumn
fsIgmpInterfaceRxGenQueries = _FsIgmpInterfaceRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 10),
    _FsIgmpInterfaceRxGenQueries_Type()
)
fsIgmpInterfaceRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxGenQueries.setStatus("current")
_FsIgmpInterfaceRxGrpQueries_Type = Counter32
_FsIgmpInterfaceRxGrpQueries_Object = MibTableColumn
fsIgmpInterfaceRxGrpQueries = _FsIgmpInterfaceRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 11),
    _FsIgmpInterfaceRxGrpQueries_Type()
)
fsIgmpInterfaceRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxGrpQueries.setStatus("current")
_FsIgmpInterfaceRxGrpAndSrcQueries_Type = Counter32
_FsIgmpInterfaceRxGrpAndSrcQueries_Object = MibTableColumn
fsIgmpInterfaceRxGrpAndSrcQueries = _FsIgmpInterfaceRxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 12),
    _FsIgmpInterfaceRxGrpAndSrcQueries_Type()
)
fsIgmpInterfaceRxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxGrpAndSrcQueries.setStatus("current")
_FsIgmpInterfaceRxv1v2Reports_Type = Counter32
_FsIgmpInterfaceRxv1v2Reports_Object = MibTableColumn
fsIgmpInterfaceRxv1v2Reports = _FsIgmpInterfaceRxv1v2Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 13),
    _FsIgmpInterfaceRxv1v2Reports_Type()
)
fsIgmpInterfaceRxv1v2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxv1v2Reports.setStatus("current")
_FsIgmpInterfaceRxv3Reports_Type = Counter32
_FsIgmpInterfaceRxv3Reports_Object = MibTableColumn
fsIgmpInterfaceRxv3Reports = _FsIgmpInterfaceRxv3Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 14),
    _FsIgmpInterfaceRxv3Reports_Type()
)
fsIgmpInterfaceRxv3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxv3Reports.setStatus("current")
_FsIgmpInterfaceTxGenQueries_Type = Counter32
_FsIgmpInterfaceTxGenQueries_Object = MibTableColumn
fsIgmpInterfaceTxGenQueries = _FsIgmpInterfaceTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 15),
    _FsIgmpInterfaceTxGenQueries_Type()
)
fsIgmpInterfaceTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxGenQueries.setStatus("current")
_FsIgmpInterfaceTxGrpQueries_Type = Counter32
_FsIgmpInterfaceTxGrpQueries_Object = MibTableColumn
fsIgmpInterfaceTxGrpQueries = _FsIgmpInterfaceTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 16),
    _FsIgmpInterfaceTxGrpQueries_Type()
)
fsIgmpInterfaceTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxGrpQueries.setStatus("current")
_FsIgmpInterfaceTxGrpAndSrcQueries_Type = Counter32
_FsIgmpInterfaceTxGrpAndSrcQueries_Object = MibTableColumn
fsIgmpInterfaceTxGrpAndSrcQueries = _FsIgmpInterfaceTxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 17),
    _FsIgmpInterfaceTxGrpAndSrcQueries_Type()
)
fsIgmpInterfaceTxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxGrpAndSrcQueries.setStatus("current")
_FsIgmpInterfaceTxv1v2Reports_Type = Counter32
_FsIgmpInterfaceTxv1v2Reports_Object = MibTableColumn
fsIgmpInterfaceTxv1v2Reports = _FsIgmpInterfaceTxv1v2Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 18),
    _FsIgmpInterfaceTxv1v2Reports_Type()
)
fsIgmpInterfaceTxv1v2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxv1v2Reports.setStatus("current")
_FsIgmpInterfaceTxv3Reports_Type = Counter32
_FsIgmpInterfaceTxv3Reports_Object = MibTableColumn
fsIgmpInterfaceTxv3Reports = _FsIgmpInterfaceTxv3Reports_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 19),
    _FsIgmpInterfaceTxv3Reports_Type()
)
fsIgmpInterfaceTxv3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxv3Reports.setStatus("current")
_FsIgmpInterfaceTxv2Leaves_Type = Counter32
_FsIgmpInterfaceTxv2Leaves_Object = MibTableColumn
fsIgmpInterfaceTxv2Leaves = _FsIgmpInterfaceTxv2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 3, 1, 20),
    _FsIgmpInterfaceTxv2Leaves_Type()
)
fsIgmpInterfaceTxv2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxv2Leaves.setStatus("current")
_FsIgmpCacheTable_Object = MibTable
fsIgmpCacheTable = _FsIgmpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 4)
)
if mibBuilder.loadTexts:
    fsIgmpCacheTable.setStatus("current")
_FsIgmpCacheEntry_Object = MibTableRow
fsIgmpCacheEntry = _FsIgmpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 4, 1)
)
fsIgmpCacheEntry.setIndexNames(
    (0, "SUPERMICRO-IGMP-MIB", "fsIgmpCacheAddress"),
    (0, "SUPERMICRO-IGMP-MIB", "fsIgmpCacheIfIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpCacheEntry.setStatus("current")
_FsIgmpCacheAddress_Type = IpAddress
_FsIgmpCacheAddress_Object = MibTableColumn
fsIgmpCacheAddress = _FsIgmpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 4, 1, 1),
    _FsIgmpCacheAddress_Type()
)
fsIgmpCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpCacheAddress.setStatus("current")
_FsIgmpCacheIfIndex_Type = InterfaceIndex
_FsIgmpCacheIfIndex_Object = MibTableColumn
fsIgmpCacheIfIndex = _FsIgmpCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 4, 1, 2),
    _FsIgmpCacheIfIndex_Type()
)
fsIgmpCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpCacheIfIndex.setStatus("current")
_FsIgmpCacheGroupCompMode_Type = Integer32
_FsIgmpCacheGroupCompMode_Object = MibTableColumn
fsIgmpCacheGroupCompMode = _FsIgmpCacheGroupCompMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 36, 1, 4, 1, 3),
    _FsIgmpCacheGroupCompMode_Type()
)
fsIgmpCacheGroupCompMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpCacheGroupCompMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-IGMP-MIB",
    **{"fsigmpMIB": fsigmpMIB,
       "fsigmp": fsigmp,
       "fsIgmpGlobalStatus": fsIgmpGlobalStatus,
       "fsIgmpTraceLevel": fsIgmpTraceLevel,
       "fsIgmpInterfaceTable": fsIgmpInterfaceTable,
       "fsIgmpInterfaceEntry": fsIgmpInterfaceEntry,
       "fsIgmpInterfaceIfIndex": fsIgmpInterfaceIfIndex,
       "fsIgmpInterfaceAdminStatus": fsIgmpInterfaceAdminStatus,
       "fsIgmpInterfaceFastLeaveStatus": fsIgmpInterfaceFastLeaveStatus,
       "fsIgmpInterfaceOperStatus": fsIgmpInterfaceOperStatus,
       "fsIgmpInterfaceIncomingPkts": fsIgmpInterfaceIncomingPkts,
       "fsIgmpInterfaceIncomingJoins": fsIgmpInterfaceIncomingJoins,
       "fsIgmpInterfaceIncomingLeaves": fsIgmpInterfaceIncomingLeaves,
       "fsIgmpInterfaceIncomingQueries": fsIgmpInterfaceIncomingQueries,
       "fsIgmpInterfaceOutgoingQueries": fsIgmpInterfaceOutgoingQueries,
       "fsIgmpInterfaceRxGenQueries": fsIgmpInterfaceRxGenQueries,
       "fsIgmpInterfaceRxGrpQueries": fsIgmpInterfaceRxGrpQueries,
       "fsIgmpInterfaceRxGrpAndSrcQueries": fsIgmpInterfaceRxGrpAndSrcQueries,
       "fsIgmpInterfaceRxv1v2Reports": fsIgmpInterfaceRxv1v2Reports,
       "fsIgmpInterfaceRxv3Reports": fsIgmpInterfaceRxv3Reports,
       "fsIgmpInterfaceTxGenQueries": fsIgmpInterfaceTxGenQueries,
       "fsIgmpInterfaceTxGrpQueries": fsIgmpInterfaceTxGrpQueries,
       "fsIgmpInterfaceTxGrpAndSrcQueries": fsIgmpInterfaceTxGrpAndSrcQueries,
       "fsIgmpInterfaceTxv1v2Reports": fsIgmpInterfaceTxv1v2Reports,
       "fsIgmpInterfaceTxv3Reports": fsIgmpInterfaceTxv3Reports,
       "fsIgmpInterfaceTxv2Leaves": fsIgmpInterfaceTxv2Leaves,
       "fsIgmpCacheTable": fsIgmpCacheTable,
       "fsIgmpCacheEntry": fsIgmpCacheEntry,
       "fsIgmpCacheAddress": fsIgmpCacheAddress,
       "fsIgmpCacheIfIndex": fsIgmpCacheIfIndex,
       "fsIgmpCacheGroupCompMode": fsIgmpCacheGroupCompMode}
)
