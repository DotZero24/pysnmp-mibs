# SNMP MIB module (FS-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IGMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:19 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsIgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26)
)
if mibBuilder.loadTexts:
    fsIgmpMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIgmpMIBObjects_ObjectIdentity = ObjectIdentity
fsIgmpMIBObjects = _FsIgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1)
)
_FsIgmpInterfaceTable_Object = MibTable
fsIgmpInterfaceTable = _FsIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1)
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceTable.setStatus("current")
_FsIgmpInterfaceEntry_Object = MibTableRow
fsIgmpInterfaceEntry = _FsIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1)
)
fsIgmpInterfaceEntry.setIndexNames(
    (0, "FS-IGMP-MIB", "fsIgmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceEntry.setStatus("current")
_FsIgmpInterfaceIfIndex_Type = InterfaceIndex
_FsIgmpInterfaceIfIndex_Object = MibTableColumn
fsIgmpInterfaceIfIndex = _FsIgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 1),
    _FsIgmpInterfaceIfIndex_Type()
)
fsIgmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIfIndex.setStatus("current")


class _FsIgmpInterfaceQueryInterval_Type(Unsigned32):
    """Custom type fsIgmpInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsIgmpInterfaceQueryInterval_Type.__name__ = "Unsigned32"
_FsIgmpInterfaceQueryInterval_Object = MibTableColumn
fsIgmpInterfaceQueryInterval = _FsIgmpInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 2),
    _FsIgmpInterfaceQueryInterval_Type()
)
fsIgmpInterfaceQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQueryInterval.setUnits("seconds")


class _FsIgmpInterfaceVersion_Type(Unsigned32):
    """Custom type fsIgmpInterfaceVersion based on Unsigned32"""
    defaultValue = 2


_FsIgmpInterfaceVersion_Type.__name__ = "Unsigned32"
_FsIgmpInterfaceVersion_Object = MibTableColumn
fsIgmpInterfaceVersion = _FsIgmpInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 3),
    _FsIgmpInterfaceVersion_Type()
)
fsIgmpInterfaceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceVersion.setStatus("current")
_FsIgmpInterfaceQuerier_Type = IpAddress
_FsIgmpInterfaceQuerier_Object = MibTableColumn
fsIgmpInterfaceQuerier = _FsIgmpInterfaceQuerier_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 4),
    _FsIgmpInterfaceQuerier_Type()
)
fsIgmpInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQuerier.setStatus("current")


class _FsIgmpInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type fsIgmpInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 250),
    )


_FsIgmpInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_FsIgmpInterfaceQueryMaxResponseTime_Object = MibTableColumn
fsIgmpInterfaceQueryMaxResponseTime = _FsIgmpInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 5),
    _FsIgmpInterfaceQueryMaxResponseTime_Type()
)
fsIgmpInterfaceQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_FsIgmpInterfaceQuerierUpTime_Type = TimeTicks
_FsIgmpInterfaceQuerierUpTime_Object = MibTableColumn
fsIgmpInterfaceQuerierUpTime = _FsIgmpInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 6),
    _FsIgmpInterfaceQuerierUpTime_Type()
)
fsIgmpInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQuerierUpTime.setStatus("current")
_FsIgmpInterfaceQuerierExpiryTime_Type = TimeTicks
_FsIgmpInterfaceQuerierExpiryTime_Object = MibTableColumn
fsIgmpInterfaceQuerierExpiryTime = _FsIgmpInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 7),
    _FsIgmpInterfaceQuerierExpiryTime_Type()
)
fsIgmpInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQuerierExpiryTime.setStatus("current")
_FsIgmpInterfaceVersion1QuerierTimer_Type = TimeTicks
_FsIgmpInterfaceVersion1QuerierTimer_Object = MibTableColumn
fsIgmpInterfaceVersion1QuerierTimer = _FsIgmpInterfaceVersion1QuerierTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 8),
    _FsIgmpInterfaceVersion1QuerierTimer_Type()
)
fsIgmpInterfaceVersion1QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceVersion1QuerierTimer.setStatus("current")
_FsIgmpInterfaceWrongVersionQueries_Type = Counter32
_FsIgmpInterfaceWrongVersionQueries_Object = MibTableColumn
fsIgmpInterfaceWrongVersionQueries = _FsIgmpInterfaceWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 9),
    _FsIgmpInterfaceWrongVersionQueries_Type()
)
fsIgmpInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceWrongVersionQueries.setStatus("current")
_FsIgmpInterfaceJoins_Type = Counter32
_FsIgmpInterfaceJoins_Object = MibTableColumn
fsIgmpInterfaceJoins = _FsIgmpInterfaceJoins_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 10),
    _FsIgmpInterfaceJoins_Type()
)
fsIgmpInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceJoins.setStatus("current")


class _FsIgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type fsIgmpInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsIgmpInterfaceProxyIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_FsIgmpInterfaceProxyIfIndex_Object = MibTableColumn
fsIgmpInterfaceProxyIfIndex = _FsIgmpInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 11),
    _FsIgmpInterfaceProxyIfIndex_Type()
)
fsIgmpInterfaceProxyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceProxyIfIndex.setStatus("obsolete")
_FsIgmpInterfaceGroups_Type = Gauge32
_FsIgmpInterfaceGroups_Object = MibTableColumn
fsIgmpInterfaceGroups = _FsIgmpInterfaceGroups_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 12),
    _FsIgmpInterfaceGroups_Type()
)
fsIgmpInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceGroups.setStatus("current")


class _FsIgmpInterfaceRobustness_Type(Unsigned32):
    """Custom type fsIgmpInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsIgmpInterfaceRobustness_Type.__name__ = "Unsigned32"
_FsIgmpInterfaceRobustness_Object = MibTableColumn
fsIgmpInterfaceRobustness = _FsIgmpInterfaceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 13),
    _FsIgmpInterfaceRobustness_Type()
)
fsIgmpInterfaceRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRobustness.setStatus("current")


class _FsIgmpInterfaceLastMembQueryIntvl_Type(Unsigned32):
    """Custom type fsIgmpInterfaceLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655),
    )


_FsIgmpInterfaceLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_FsIgmpInterfaceLastMembQueryIntvl_Object = MibTableColumn
fsIgmpInterfaceLastMembQueryIntvl = _FsIgmpInterfaceLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 14),
    _FsIgmpInterfaceLastMembQueryIntvl_Type()
)
fsIgmpInterfaceLastMembQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    fsIgmpInterfaceLastMembQueryIntvl.setUnits("tenths of seconds")


class _FsIgmpInterfaceQuerierPresentTimeout_Type(Integer32):
    """Custom type fsIgmpInterfaceQuerierPresentTimeout based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_FsIgmpInterfaceQuerierPresentTimeout_Type.__name__ = "Integer32"
_FsIgmpInterfaceQuerierPresentTimeout_Object = MibTableColumn
fsIgmpInterfaceQuerierPresentTimeout = _FsIgmpInterfaceQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 15),
    _FsIgmpInterfaceQuerierPresentTimeout_Type()
)
fsIgmpInterfaceQuerierPresentTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQuerierPresentTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQuerierPresentTimeout.setUnits("seconds")
_FsIgmpInterfaceLeaves_Type = Counter32
_FsIgmpInterfaceLeaves_Object = MibTableColumn
fsIgmpInterfaceLeaves = _FsIgmpInterfaceLeaves_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 16),
    _FsIgmpInterfaceLeaves_Type()
)
fsIgmpInterfaceLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceLeaves.setStatus("current")


class _FsIgmpInterfaceAccessGroupAclName_Type(DisplayString):
    """Custom type fsIgmpInterfaceAccessGroupAclName based on DisplayString"""
    defaultValue = OctetString("")


_FsIgmpInterfaceAccessGroupAclName_Type.__name__ = "DisplayString"
_FsIgmpInterfaceAccessGroupAclName_Object = MibTableColumn
fsIgmpInterfaceAccessGroupAclName = _FsIgmpInterfaceAccessGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 17),
    _FsIgmpInterfaceAccessGroupAclName_Type()
)
fsIgmpInterfaceAccessGroupAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceAccessGroupAclName.setStatus("current")
_FsIgmpInterfaceEnabled_Type = EnabledStatus
_FsIgmpInterfaceEnabled_Object = MibTableColumn
fsIgmpInterfaceEnabled = _FsIgmpInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 18),
    _FsIgmpInterfaceEnabled_Type()
)
fsIgmpInterfaceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceEnabled.setStatus("current")
_FsIgmpInterfaceHostVersion_Type = Unsigned32
_FsIgmpInterfaceHostVersion_Object = MibTableColumn
fsIgmpInterfaceHostVersion = _FsIgmpInterfaceHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 1, 1, 19),
    _FsIgmpInterfaceHostVersion_Type()
)
fsIgmpInterfaceHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceHostVersion.setStatus("current")
_FsIgmpInterfaceStaticTable_Object = MibTable
fsIgmpInterfaceStaticTable = _FsIgmpInterfaceStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 2)
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceStaticTable.setStatus("current")
_FsIgmpInterfaceStaticEntry_Object = MibTableRow
fsIgmpInterfaceStaticEntry = _FsIgmpInterfaceStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 2, 1)
)
fsIgmpInterfaceStaticEntry.setIndexNames(
    (0, "FS-IGMP-MIB", "fsIgmpInterfaceStaticInterface"),
    (0, "FS-IGMP-MIB", "fsIgmpInterfaceStaticGroupAddress"),
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceStaticEntry.setStatus("current")
_FsIgmpInterfaceStaticInterface_Type = InterfaceIndex
_FsIgmpInterfaceStaticInterface_Object = MibTableColumn
fsIgmpInterfaceStaticInterface = _FsIgmpInterfaceStaticInterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 2, 1, 1),
    _FsIgmpInterfaceStaticInterface_Type()
)
fsIgmpInterfaceStaticInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpInterfaceStaticInterface.setStatus("current")
_FsIgmpInterfaceStaticGroupAddress_Type = IpAddress
_FsIgmpInterfaceStaticGroupAddress_Object = MibTableColumn
fsIgmpInterfaceStaticGroupAddress = _FsIgmpInterfaceStaticGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 2, 1, 2),
    _FsIgmpInterfaceStaticGroupAddress_Type()
)
fsIgmpInterfaceStaticGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpInterfaceStaticGroupAddress.setStatus("current")
_FsIgmpInterfaceStaticStatus_Type = RowStatus
_FsIgmpInterfaceStaticStatus_Object = MibTableColumn
fsIgmpInterfaceStaticStatus = _FsIgmpInterfaceStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 2, 1, 3),
    _FsIgmpInterfaceStaticStatus_Type()
)
fsIgmpInterfaceStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIgmpInterfaceStaticStatus.setStatus("current")
_FsIgmpTraps_ObjectIdentity = ObjectIdentity
fsIgmpTraps = _FsIgmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 3)
)
_FsIgmpMIBConformance_ObjectIdentity = ObjectIdentity
fsIgmpMIBConformance = _FsIgmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 2)
)
_FsIgmpMIBCompliances_ObjectIdentity = ObjectIdentity
fsIgmpMIBCompliances = _FsIgmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 2, 1)
)
_FsIgmpMIBGroups_ObjectIdentity = ObjectIdentity
fsIgmpMIBGroups = _FsIgmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 2, 2)
)

# Managed Objects groups

fsIgmpInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 2, 2, 1)
)
fsIgmpInterfaceMIBGroup.setObjects(
      *(("FS-IGMP-MIB", "fsIgmpInterfaceQueryInterval"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceVersion"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceQuerier"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceQueryMaxResponseTime"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceQuerierUpTime"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceQuerierExpiryTime"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceVersion1QuerierTimer"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceWrongVersionQueries"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceJoins"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceProxyIfIndex"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceGroups"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceRobustness"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceLastMembQueryIntvl"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceQuerierPresentTimeout"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceLeaves"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceAccessGroupAclName"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceEnabled"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceMIBGroup.setStatus("current")

fsIgmpInterfaceStaticMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 2, 2, 2)
)
fsIgmpInterfaceStaticMIBGroup.setObjects(
    ("FS-IGMP-MIB", "fsIgmpInterfaceStaticStatus")
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceStaticMIBGroup.setStatus("current")


# Notification objects

fsIgmpVersionConflicted = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 1, 3, 1)
)
fsIgmpVersionConflicted.setObjects(
      *(("FS-IGMP-MIB", "fsIgmpInterfaceIfIndex"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceVersion"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    fsIgmpVersionConflicted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsIgmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 2, 1, 1)
)
fsIgmpMIBCompliance.setObjects(
      *(("FS-IGMP-MIB", "fsIgmpInterfaceMIBGroup"),
        ("FS-IGMP-MIB", "fsIgmpInterfaceStaticMIBGroup"))
)
if mibBuilder.loadTexts:
    fsIgmpMIBCompliance.setStatus(
        "current"
    )

igmpExternCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 26, 2, 1, 2)
)
if mibBuilder.loadTexts:
    igmpExternCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IGMP-MIB",
    **{"fsIgmpMIB": fsIgmpMIB,
       "fsIgmpMIBObjects": fsIgmpMIBObjects,
       "fsIgmpInterfaceTable": fsIgmpInterfaceTable,
       "fsIgmpInterfaceEntry": fsIgmpInterfaceEntry,
       "fsIgmpInterfaceIfIndex": fsIgmpInterfaceIfIndex,
       "fsIgmpInterfaceQueryInterval": fsIgmpInterfaceQueryInterval,
       "fsIgmpInterfaceVersion": fsIgmpInterfaceVersion,
       "fsIgmpInterfaceQuerier": fsIgmpInterfaceQuerier,
       "fsIgmpInterfaceQueryMaxResponseTime": fsIgmpInterfaceQueryMaxResponseTime,
       "fsIgmpInterfaceQuerierUpTime": fsIgmpInterfaceQuerierUpTime,
       "fsIgmpInterfaceQuerierExpiryTime": fsIgmpInterfaceQuerierExpiryTime,
       "fsIgmpInterfaceVersion1QuerierTimer": fsIgmpInterfaceVersion1QuerierTimer,
       "fsIgmpInterfaceWrongVersionQueries": fsIgmpInterfaceWrongVersionQueries,
       "fsIgmpInterfaceJoins": fsIgmpInterfaceJoins,
       "fsIgmpInterfaceProxyIfIndex": fsIgmpInterfaceProxyIfIndex,
       "fsIgmpInterfaceGroups": fsIgmpInterfaceGroups,
       "fsIgmpInterfaceRobustness": fsIgmpInterfaceRobustness,
       "fsIgmpInterfaceLastMembQueryIntvl": fsIgmpInterfaceLastMembQueryIntvl,
       "fsIgmpInterfaceQuerierPresentTimeout": fsIgmpInterfaceQuerierPresentTimeout,
       "fsIgmpInterfaceLeaves": fsIgmpInterfaceLeaves,
       "fsIgmpInterfaceAccessGroupAclName": fsIgmpInterfaceAccessGroupAclName,
       "fsIgmpInterfaceEnabled": fsIgmpInterfaceEnabled,
       "fsIgmpInterfaceHostVersion": fsIgmpInterfaceHostVersion,
       "fsIgmpInterfaceStaticTable": fsIgmpInterfaceStaticTable,
       "fsIgmpInterfaceStaticEntry": fsIgmpInterfaceStaticEntry,
       "fsIgmpInterfaceStaticInterface": fsIgmpInterfaceStaticInterface,
       "fsIgmpInterfaceStaticGroupAddress": fsIgmpInterfaceStaticGroupAddress,
       "fsIgmpInterfaceStaticStatus": fsIgmpInterfaceStaticStatus,
       "fsIgmpTraps": fsIgmpTraps,
       "fsIgmpVersionConflicted": fsIgmpVersionConflicted,
       "fsIgmpMIBConformance": fsIgmpMIBConformance,
       "fsIgmpMIBCompliances": fsIgmpMIBCompliances,
       "fsIgmpMIBCompliance": fsIgmpMIBCompliance,
       "igmpExternCompliance": igmpExternCompliance,
       "fsIgmpMIBGroups": fsIgmpMIBGroups,
       "fsIgmpInterfaceMIBGroup": fsIgmpInterfaceMIBGroup,
       "fsIgmpInterfaceStaticMIBGroup": fsIgmpInterfaceStaticMIBGroup}
)
