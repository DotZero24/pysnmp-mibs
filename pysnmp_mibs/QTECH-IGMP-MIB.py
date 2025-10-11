# SNMP MIB module (QTECH-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-IGMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:09 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechIgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26)
)
if mibBuilder.loadTexts:
    qtechIgmpMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechIgmpMIBObjects_ObjectIdentity = ObjectIdentity
qtechIgmpMIBObjects = _QtechIgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1)
)
_QtechIgmpInterfaceTable_Object = MibTable
qtechIgmpInterfaceTable = _QtechIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1)
)
if mibBuilder.loadTexts:
    qtechIgmpInterfaceTable.setStatus("current")
_QtechIgmpInterfaceEntry_Object = MibTableRow
qtechIgmpInterfaceEntry = _QtechIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1)
)
qtechIgmpInterfaceEntry.setIndexNames(
    (0, "QTECH-IGMP-MIB", "qtechIgmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIgmpInterfaceEntry.setStatus("current")
_QtechIgmpInterfaceIfIndex_Type = InterfaceIndex
_QtechIgmpInterfaceIfIndex_Object = MibTableColumn
qtechIgmpInterfaceIfIndex = _QtechIgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 1),
    _QtechIgmpInterfaceIfIndex_Type()
)
qtechIgmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceIfIndex.setStatus("current")


class _QtechIgmpInterfaceQueryInterval_Type(Unsigned32):
    """Custom type qtechIgmpInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechIgmpInterfaceQueryInterval_Type.__name__ = "Unsigned32"
_QtechIgmpInterfaceQueryInterval_Object = MibTableColumn
qtechIgmpInterfaceQueryInterval = _QtechIgmpInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 2),
    _QtechIgmpInterfaceQueryInterval_Type()
)
qtechIgmpInterfaceQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQueryInterval.setUnits("seconds")


class _QtechIgmpInterfaceVersion_Type(Unsigned32):
    """Custom type qtechIgmpInterfaceVersion based on Unsigned32"""
    defaultValue = 2


_QtechIgmpInterfaceVersion_Type.__name__ = "Unsigned32"
_QtechIgmpInterfaceVersion_Object = MibTableColumn
qtechIgmpInterfaceVersion = _QtechIgmpInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 3),
    _QtechIgmpInterfaceVersion_Type()
)
qtechIgmpInterfaceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceVersion.setStatus("current")
_QtechIgmpInterfaceQuerier_Type = IpAddress
_QtechIgmpInterfaceQuerier_Object = MibTableColumn
qtechIgmpInterfaceQuerier = _QtechIgmpInterfaceQuerier_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 4),
    _QtechIgmpInterfaceQuerier_Type()
)
qtechIgmpInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQuerier.setStatus("current")


class _QtechIgmpInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type qtechIgmpInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 250),
    )


_QtechIgmpInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_QtechIgmpInterfaceQueryMaxResponseTime_Object = MibTableColumn
qtechIgmpInterfaceQueryMaxResponseTime = _QtechIgmpInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 5),
    _QtechIgmpInterfaceQueryMaxResponseTime_Type()
)
qtechIgmpInterfaceQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_QtechIgmpInterfaceQuerierUpTime_Type = TimeTicks
_QtechIgmpInterfaceQuerierUpTime_Object = MibTableColumn
qtechIgmpInterfaceQuerierUpTime = _QtechIgmpInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 6),
    _QtechIgmpInterfaceQuerierUpTime_Type()
)
qtechIgmpInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQuerierUpTime.setStatus("current")
_QtechIgmpInterfaceQuerierExpiryTime_Type = TimeTicks
_QtechIgmpInterfaceQuerierExpiryTime_Object = MibTableColumn
qtechIgmpInterfaceQuerierExpiryTime = _QtechIgmpInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 7),
    _QtechIgmpInterfaceQuerierExpiryTime_Type()
)
qtechIgmpInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQuerierExpiryTime.setStatus("current")
_QtechIgmpInterfaceVersion1QuerierTimer_Type = TimeTicks
_QtechIgmpInterfaceVersion1QuerierTimer_Object = MibTableColumn
qtechIgmpInterfaceVersion1QuerierTimer = _QtechIgmpInterfaceVersion1QuerierTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 8),
    _QtechIgmpInterfaceVersion1QuerierTimer_Type()
)
qtechIgmpInterfaceVersion1QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceVersion1QuerierTimer.setStatus("current")
_QtechIgmpInterfaceWrongVersionQueries_Type = Counter32
_QtechIgmpInterfaceWrongVersionQueries_Object = MibTableColumn
qtechIgmpInterfaceWrongVersionQueries = _QtechIgmpInterfaceWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 9),
    _QtechIgmpInterfaceWrongVersionQueries_Type()
)
qtechIgmpInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceWrongVersionQueries.setStatus("current")
_QtechIgmpInterfaceJoins_Type = Counter32
_QtechIgmpInterfaceJoins_Object = MibTableColumn
qtechIgmpInterfaceJoins = _QtechIgmpInterfaceJoins_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 10),
    _QtechIgmpInterfaceJoins_Type()
)
qtechIgmpInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceJoins.setStatus("current")


class _QtechIgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type qtechIgmpInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_QtechIgmpInterfaceProxyIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_QtechIgmpInterfaceProxyIfIndex_Object = MibTableColumn
qtechIgmpInterfaceProxyIfIndex = _QtechIgmpInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 11),
    _QtechIgmpInterfaceProxyIfIndex_Type()
)
qtechIgmpInterfaceProxyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceProxyIfIndex.setStatus("obsolete")
_QtechIgmpInterfaceGroups_Type = Gauge32
_QtechIgmpInterfaceGroups_Object = MibTableColumn
qtechIgmpInterfaceGroups = _QtechIgmpInterfaceGroups_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 12),
    _QtechIgmpInterfaceGroups_Type()
)
qtechIgmpInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceGroups.setStatus("current")


class _QtechIgmpInterfaceRobustness_Type(Unsigned32):
    """Custom type qtechIgmpInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechIgmpInterfaceRobustness_Type.__name__ = "Unsigned32"
_QtechIgmpInterfaceRobustness_Object = MibTableColumn
qtechIgmpInterfaceRobustness = _QtechIgmpInterfaceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 13),
    _QtechIgmpInterfaceRobustness_Type()
)
qtechIgmpInterfaceRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceRobustness.setStatus("current")


class _QtechIgmpInterfaceLastMembQueryIntvl_Type(Unsigned32):
    """Custom type qtechIgmpInterfaceLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655),
    )


_QtechIgmpInterfaceLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_QtechIgmpInterfaceLastMembQueryIntvl_Object = MibTableColumn
qtechIgmpInterfaceLastMembQueryIntvl = _QtechIgmpInterfaceLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 14),
    _QtechIgmpInterfaceLastMembQueryIntvl_Type()
)
qtechIgmpInterfaceLastMembQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceLastMembQueryIntvl.setUnits("tenths of seconds")


class _QtechIgmpInterfaceQuerierPresentTimeout_Type(Integer32):
    """Custom type qtechIgmpInterfaceQuerierPresentTimeout based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_QtechIgmpInterfaceQuerierPresentTimeout_Type.__name__ = "Integer32"
_QtechIgmpInterfaceQuerierPresentTimeout_Object = MibTableColumn
qtechIgmpInterfaceQuerierPresentTimeout = _QtechIgmpInterfaceQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 15),
    _QtechIgmpInterfaceQuerierPresentTimeout_Type()
)
qtechIgmpInterfaceQuerierPresentTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQuerierPresentTimeout.setStatus("current")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceQuerierPresentTimeout.setUnits("seconds")
_QtechIgmpInterfaceLeaves_Type = Counter32
_QtechIgmpInterfaceLeaves_Object = MibTableColumn
qtechIgmpInterfaceLeaves = _QtechIgmpInterfaceLeaves_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 16),
    _QtechIgmpInterfaceLeaves_Type()
)
qtechIgmpInterfaceLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceLeaves.setStatus("current")


class _QtechIgmpInterfaceAccessGroupAclName_Type(DisplayString):
    """Custom type qtechIgmpInterfaceAccessGroupAclName based on DisplayString"""
    defaultValue = OctetString("")


_QtechIgmpInterfaceAccessGroupAclName_Type.__name__ = "DisplayString"
_QtechIgmpInterfaceAccessGroupAclName_Object = MibTableColumn
qtechIgmpInterfaceAccessGroupAclName = _QtechIgmpInterfaceAccessGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 17),
    _QtechIgmpInterfaceAccessGroupAclName_Type()
)
qtechIgmpInterfaceAccessGroupAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceAccessGroupAclName.setStatus("current")
_QtechIgmpInterfaceEnabled_Type = EnabledStatus
_QtechIgmpInterfaceEnabled_Object = MibTableColumn
qtechIgmpInterfaceEnabled = _QtechIgmpInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 18),
    _QtechIgmpInterfaceEnabled_Type()
)
qtechIgmpInterfaceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceEnabled.setStatus("current")
_QtechIgmpInterfaceHostVersion_Type = Unsigned32
_QtechIgmpInterfaceHostVersion_Object = MibTableColumn
qtechIgmpInterfaceHostVersion = _QtechIgmpInterfaceHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 1, 1, 19),
    _QtechIgmpInterfaceHostVersion_Type()
)
qtechIgmpInterfaceHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceHostVersion.setStatus("current")
_QtechIgmpInterfaceStaticTable_Object = MibTable
qtechIgmpInterfaceStaticTable = _QtechIgmpInterfaceStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 2)
)
if mibBuilder.loadTexts:
    qtechIgmpInterfaceStaticTable.setStatus("current")
_QtechIgmpInterfaceStaticEntry_Object = MibTableRow
qtechIgmpInterfaceStaticEntry = _QtechIgmpInterfaceStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 2, 1)
)
qtechIgmpInterfaceStaticEntry.setIndexNames(
    (0, "QTECH-IGMP-MIB", "qtechIgmpInterfaceStaticInterface"),
    (0, "QTECH-IGMP-MIB", "qtechIgmpInterfaceStaticGroupAddress"),
)
if mibBuilder.loadTexts:
    qtechIgmpInterfaceStaticEntry.setStatus("current")
_QtechIgmpInterfaceStaticInterface_Type = InterfaceIndex
_QtechIgmpInterfaceStaticInterface_Object = MibTableColumn
qtechIgmpInterfaceStaticInterface = _QtechIgmpInterfaceStaticInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 2, 1, 1),
    _QtechIgmpInterfaceStaticInterface_Type()
)
qtechIgmpInterfaceStaticInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceStaticInterface.setStatus("current")
_QtechIgmpInterfaceStaticGroupAddress_Type = IpAddress
_QtechIgmpInterfaceStaticGroupAddress_Object = MibTableColumn
qtechIgmpInterfaceStaticGroupAddress = _QtechIgmpInterfaceStaticGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 2, 1, 2),
    _QtechIgmpInterfaceStaticGroupAddress_Type()
)
qtechIgmpInterfaceStaticGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceStaticGroupAddress.setStatus("current")
_QtechIgmpInterfaceStaticStatus_Type = RowStatus
_QtechIgmpInterfaceStaticStatus_Object = MibTableColumn
qtechIgmpInterfaceStaticStatus = _QtechIgmpInterfaceStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 2, 1, 3),
    _QtechIgmpInterfaceStaticStatus_Type()
)
qtechIgmpInterfaceStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIgmpInterfaceStaticStatus.setStatus("current")
_QtechIgmpTraps_ObjectIdentity = ObjectIdentity
qtechIgmpTraps = _QtechIgmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 3)
)
_QtechIgmpMIBConformance_ObjectIdentity = ObjectIdentity
qtechIgmpMIBConformance = _QtechIgmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 2)
)
_QtechIgmpMIBCompliances_ObjectIdentity = ObjectIdentity
qtechIgmpMIBCompliances = _QtechIgmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 2, 1)
)
_QtechIgmpMIBGroups_ObjectIdentity = ObjectIdentity
qtechIgmpMIBGroups = _QtechIgmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 2, 2)
)

# Managed Objects groups

qtechIgmpInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 2, 2, 1)
)
qtechIgmpInterfaceMIBGroup.setObjects(
      *(("QTECH-IGMP-MIB", "qtechIgmpInterfaceQueryInterval"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceVersion"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceQuerier"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceQueryMaxResponseTime"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceQuerierUpTime"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceQuerierExpiryTime"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceVersion1QuerierTimer"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceWrongVersionQueries"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceJoins"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceProxyIfIndex"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceGroups"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceRobustness"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceLastMembQueryIntvl"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceQuerierPresentTimeout"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceLeaves"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceAccessGroupAclName"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceEnabled"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    qtechIgmpInterfaceMIBGroup.setStatus("current")

qtechIgmpInterfaceStaticMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 2, 2, 2)
)
qtechIgmpInterfaceStaticMIBGroup.setObjects(
    ("QTECH-IGMP-MIB", "qtechIgmpInterfaceStaticStatus")
)
if mibBuilder.loadTexts:
    qtechIgmpInterfaceStaticMIBGroup.setStatus("current")


# Notification objects

qtechIgmpVersionConflicted = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 1, 3, 1)
)
qtechIgmpVersionConflicted.setObjects(
      *(("QTECH-IGMP-MIB", "qtechIgmpInterfaceIfIndex"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceVersion"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    qtechIgmpVersionConflicted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechIgmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 2, 1, 1)
)
qtechIgmpMIBCompliance.setObjects(
      *(("QTECH-IGMP-MIB", "qtechIgmpInterfaceMIBGroup"),
        ("QTECH-IGMP-MIB", "qtechIgmpInterfaceStaticMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechIgmpMIBCompliance.setStatus(
        "current"
    )

igmpExternCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 26, 2, 1, 2)
)
if mibBuilder.loadTexts:
    igmpExternCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-IGMP-MIB",
    **{"qtechIgmpMIB": qtechIgmpMIB,
       "qtechIgmpMIBObjects": qtechIgmpMIBObjects,
       "qtechIgmpInterfaceTable": qtechIgmpInterfaceTable,
       "qtechIgmpInterfaceEntry": qtechIgmpInterfaceEntry,
       "qtechIgmpInterfaceIfIndex": qtechIgmpInterfaceIfIndex,
       "qtechIgmpInterfaceQueryInterval": qtechIgmpInterfaceQueryInterval,
       "qtechIgmpInterfaceVersion": qtechIgmpInterfaceVersion,
       "qtechIgmpInterfaceQuerier": qtechIgmpInterfaceQuerier,
       "qtechIgmpInterfaceQueryMaxResponseTime": qtechIgmpInterfaceQueryMaxResponseTime,
       "qtechIgmpInterfaceQuerierUpTime": qtechIgmpInterfaceQuerierUpTime,
       "qtechIgmpInterfaceQuerierExpiryTime": qtechIgmpInterfaceQuerierExpiryTime,
       "qtechIgmpInterfaceVersion1QuerierTimer": qtechIgmpInterfaceVersion1QuerierTimer,
       "qtechIgmpInterfaceWrongVersionQueries": qtechIgmpInterfaceWrongVersionQueries,
       "qtechIgmpInterfaceJoins": qtechIgmpInterfaceJoins,
       "qtechIgmpInterfaceProxyIfIndex": qtechIgmpInterfaceProxyIfIndex,
       "qtechIgmpInterfaceGroups": qtechIgmpInterfaceGroups,
       "qtechIgmpInterfaceRobustness": qtechIgmpInterfaceRobustness,
       "qtechIgmpInterfaceLastMembQueryIntvl": qtechIgmpInterfaceLastMembQueryIntvl,
       "qtechIgmpInterfaceQuerierPresentTimeout": qtechIgmpInterfaceQuerierPresentTimeout,
       "qtechIgmpInterfaceLeaves": qtechIgmpInterfaceLeaves,
       "qtechIgmpInterfaceAccessGroupAclName": qtechIgmpInterfaceAccessGroupAclName,
       "qtechIgmpInterfaceEnabled": qtechIgmpInterfaceEnabled,
       "qtechIgmpInterfaceHostVersion": qtechIgmpInterfaceHostVersion,
       "qtechIgmpInterfaceStaticTable": qtechIgmpInterfaceStaticTable,
       "qtechIgmpInterfaceStaticEntry": qtechIgmpInterfaceStaticEntry,
       "qtechIgmpInterfaceStaticInterface": qtechIgmpInterfaceStaticInterface,
       "qtechIgmpInterfaceStaticGroupAddress": qtechIgmpInterfaceStaticGroupAddress,
       "qtechIgmpInterfaceStaticStatus": qtechIgmpInterfaceStaticStatus,
       "qtechIgmpTraps": qtechIgmpTraps,
       "qtechIgmpVersionConflicted": qtechIgmpVersionConflicted,
       "qtechIgmpMIBConformance": qtechIgmpMIBConformance,
       "qtechIgmpMIBCompliances": qtechIgmpMIBCompliances,
       "qtechIgmpMIBCompliance": qtechIgmpMIBCompliance,
       "igmpExternCompliance": igmpExternCompliance,
       "qtechIgmpMIBGroups": qtechIgmpMIBGroups,
       "qtechIgmpInterfaceMIBGroup": qtechIgmpInterfaceMIBGroup,
       "qtechIgmpInterfaceStaticMIBGroup": qtechIgmpInterfaceStaticMIBGroup}
)
