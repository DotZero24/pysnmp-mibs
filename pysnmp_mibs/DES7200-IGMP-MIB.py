# SNMP MIB module (DES7200-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-IGMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:57 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myIgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26)
)
if mibBuilder.loadTexts:
    myIgmpMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyIgmpMIBObjects_ObjectIdentity = ObjectIdentity
myIgmpMIBObjects = _MyIgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1)
)
_MyIgmpInterfaceTable_Object = MibTable
myIgmpInterfaceTable = _MyIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1)
)
if mibBuilder.loadTexts:
    myIgmpInterfaceTable.setStatus("current")
_MyIgmpInterfaceEntry_Object = MibTableRow
myIgmpInterfaceEntry = _MyIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1)
)
myIgmpInterfaceEntry.setIndexNames(
    (0, "DES7200-IGMP-MIB", "myIgmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    myIgmpInterfaceEntry.setStatus("current")
_MyIgmpInterfaceIfIndex_Type = InterfaceIndex
_MyIgmpInterfaceIfIndex_Object = MibTableColumn
myIgmpInterfaceIfIndex = _MyIgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 1),
    _MyIgmpInterfaceIfIndex_Type()
)
myIgmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myIgmpInterfaceIfIndex.setStatus("current")


class _MyIgmpInterfaceQueryInterval_Type(Unsigned32):
    """Custom type myIgmpInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MyIgmpInterfaceQueryInterval_Type.__name__ = "Unsigned32"
_MyIgmpInterfaceQueryInterval_Object = MibTableColumn
myIgmpInterfaceQueryInterval = _MyIgmpInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 2),
    _MyIgmpInterfaceQueryInterval_Type()
)
myIgmpInterfaceQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    myIgmpInterfaceQueryInterval.setUnits("seconds")


class _MyIgmpInterfaceVersion_Type(Unsigned32):
    """Custom type myIgmpInterfaceVersion based on Unsigned32"""
    defaultValue = 2


_MyIgmpInterfaceVersion_Type.__name__ = "Unsigned32"
_MyIgmpInterfaceVersion_Object = MibTableColumn
myIgmpInterfaceVersion = _MyIgmpInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 3),
    _MyIgmpInterfaceVersion_Type()
)
myIgmpInterfaceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpInterfaceVersion.setStatus("current")
_MyIgmpInterfaceQuerier_Type = IpAddress
_MyIgmpInterfaceQuerier_Object = MibTableColumn
myIgmpInterfaceQuerier = _MyIgmpInterfaceQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 4),
    _MyIgmpInterfaceQuerier_Type()
)
myIgmpInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceQuerier.setStatus("current")


class _MyIgmpInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type myIgmpInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 250),
    )


_MyIgmpInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_MyIgmpInterfaceQueryMaxResponseTime_Object = MibTableColumn
myIgmpInterfaceQueryMaxResponseTime = _MyIgmpInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 5),
    _MyIgmpInterfaceQueryMaxResponseTime_Type()
)
myIgmpInterfaceQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    myIgmpInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_MyIgmpInterfaceQuerierUpTime_Type = TimeTicks
_MyIgmpInterfaceQuerierUpTime_Object = MibTableColumn
myIgmpInterfaceQuerierUpTime = _MyIgmpInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 6),
    _MyIgmpInterfaceQuerierUpTime_Type()
)
myIgmpInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceQuerierUpTime.setStatus("current")
_MyIgmpInterfaceQuerierExpiryTime_Type = TimeTicks
_MyIgmpInterfaceQuerierExpiryTime_Object = MibTableColumn
myIgmpInterfaceQuerierExpiryTime = _MyIgmpInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 7),
    _MyIgmpInterfaceQuerierExpiryTime_Type()
)
myIgmpInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceQuerierExpiryTime.setStatus("current")
_MyIgmpInterfaceVersion1QuerierTimer_Type = TimeTicks
_MyIgmpInterfaceVersion1QuerierTimer_Object = MibTableColumn
myIgmpInterfaceVersion1QuerierTimer = _MyIgmpInterfaceVersion1QuerierTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 8),
    _MyIgmpInterfaceVersion1QuerierTimer_Type()
)
myIgmpInterfaceVersion1QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceVersion1QuerierTimer.setStatus("current")
_MyIgmpInterfaceWrongVersionQueries_Type = Counter32
_MyIgmpInterfaceWrongVersionQueries_Object = MibTableColumn
myIgmpInterfaceWrongVersionQueries = _MyIgmpInterfaceWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 9),
    _MyIgmpInterfaceWrongVersionQueries_Type()
)
myIgmpInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceWrongVersionQueries.setStatus("current")
_MyIgmpInterfaceJoins_Type = Counter32
_MyIgmpInterfaceJoins_Object = MibTableColumn
myIgmpInterfaceJoins = _MyIgmpInterfaceJoins_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 10),
    _MyIgmpInterfaceJoins_Type()
)
myIgmpInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceJoins.setStatus("current")


class _MyIgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type myIgmpInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MyIgmpInterfaceProxyIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_MyIgmpInterfaceProxyIfIndex_Object = MibTableColumn
myIgmpInterfaceProxyIfIndex = _MyIgmpInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 11),
    _MyIgmpInterfaceProxyIfIndex_Type()
)
myIgmpInterfaceProxyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceProxyIfIndex.setStatus("obsolete")
_MyIgmpInterfaceGroups_Type = Gauge32
_MyIgmpInterfaceGroups_Object = MibTableColumn
myIgmpInterfaceGroups = _MyIgmpInterfaceGroups_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 12),
    _MyIgmpInterfaceGroups_Type()
)
myIgmpInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceGroups.setStatus("current")


class _MyIgmpInterfaceRobustness_Type(Unsigned32):
    """Custom type myIgmpInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MyIgmpInterfaceRobustness_Type.__name__ = "Unsigned32"
_MyIgmpInterfaceRobustness_Object = MibTableColumn
myIgmpInterfaceRobustness = _MyIgmpInterfaceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 13),
    _MyIgmpInterfaceRobustness_Type()
)
myIgmpInterfaceRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpInterfaceRobustness.setStatus("current")


class _MyIgmpInterfaceLastMembQueryIntvl_Type(Unsigned32):
    """Custom type myIgmpInterfaceLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655),
    )


_MyIgmpInterfaceLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_MyIgmpInterfaceLastMembQueryIntvl_Object = MibTableColumn
myIgmpInterfaceLastMembQueryIntvl = _MyIgmpInterfaceLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 14),
    _MyIgmpInterfaceLastMembQueryIntvl_Type()
)
myIgmpInterfaceLastMembQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpInterfaceLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    myIgmpInterfaceLastMembQueryIntvl.setUnits("tenths of seconds")


class _MyIgmpInterfaceQuerierPresentTimeout_Type(Integer32):
    """Custom type myIgmpInterfaceQuerierPresentTimeout based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_MyIgmpInterfaceQuerierPresentTimeout_Type.__name__ = "Integer32"
_MyIgmpInterfaceQuerierPresentTimeout_Object = MibTableColumn
myIgmpInterfaceQuerierPresentTimeout = _MyIgmpInterfaceQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 15),
    _MyIgmpInterfaceQuerierPresentTimeout_Type()
)
myIgmpInterfaceQuerierPresentTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpInterfaceQuerierPresentTimeout.setStatus("current")
if mibBuilder.loadTexts:
    myIgmpInterfaceQuerierPresentTimeout.setUnits("seconds")
_MyIgmpInterfaceLeaves_Type = Counter32
_MyIgmpInterfaceLeaves_Object = MibTableColumn
myIgmpInterfaceLeaves = _MyIgmpInterfaceLeaves_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 16),
    _MyIgmpInterfaceLeaves_Type()
)
myIgmpInterfaceLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceLeaves.setStatus("current")


class _MyIgmpInterfaceAccessGroupAclName_Type(DisplayString):
    """Custom type myIgmpInterfaceAccessGroupAclName based on DisplayString"""
    defaultValue = OctetString("")


_MyIgmpInterfaceAccessGroupAclName_Type.__name__ = "DisplayString"
_MyIgmpInterfaceAccessGroupAclName_Object = MibTableColumn
myIgmpInterfaceAccessGroupAclName = _MyIgmpInterfaceAccessGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 17),
    _MyIgmpInterfaceAccessGroupAclName_Type()
)
myIgmpInterfaceAccessGroupAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpInterfaceAccessGroupAclName.setStatus("current")
_MyIgmpInterfaceEnabled_Type = EnabledStatus
_MyIgmpInterfaceEnabled_Object = MibTableColumn
myIgmpInterfaceEnabled = _MyIgmpInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 18),
    _MyIgmpInterfaceEnabled_Type()
)
myIgmpInterfaceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceEnabled.setStatus("current")
_MyIgmpInterfaceHostVersion_Type = Unsigned32
_MyIgmpInterfaceHostVersion_Object = MibTableColumn
myIgmpInterfaceHostVersion = _MyIgmpInterfaceHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 1, 1, 19),
    _MyIgmpInterfaceHostVersion_Type()
)
myIgmpInterfaceHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpInterfaceHostVersion.setStatus("current")
_MyIgmpInterfaceStaticTable_Object = MibTable
myIgmpInterfaceStaticTable = _MyIgmpInterfaceStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 2)
)
if mibBuilder.loadTexts:
    myIgmpInterfaceStaticTable.setStatus("current")
_MyIgmpInterfaceStaticEntry_Object = MibTableRow
myIgmpInterfaceStaticEntry = _MyIgmpInterfaceStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 2, 1)
)
myIgmpInterfaceStaticEntry.setIndexNames(
    (0, "DES7200-IGMP-MIB", "myIgmpInterfaceStaticInterface"),
    (0, "DES7200-IGMP-MIB", "myIgmpInterfaceStaticGroupAddress"),
)
if mibBuilder.loadTexts:
    myIgmpInterfaceStaticEntry.setStatus("current")
_MyIgmpInterfaceStaticInterface_Type = InterfaceIndex
_MyIgmpInterfaceStaticInterface_Object = MibTableColumn
myIgmpInterfaceStaticInterface = _MyIgmpInterfaceStaticInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 2, 1, 1),
    _MyIgmpInterfaceStaticInterface_Type()
)
myIgmpInterfaceStaticInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myIgmpInterfaceStaticInterface.setStatus("current")
_MyIgmpInterfaceStaticGroupAddress_Type = IpAddress
_MyIgmpInterfaceStaticGroupAddress_Object = MibTableColumn
myIgmpInterfaceStaticGroupAddress = _MyIgmpInterfaceStaticGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 2, 1, 2),
    _MyIgmpInterfaceStaticGroupAddress_Type()
)
myIgmpInterfaceStaticGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myIgmpInterfaceStaticGroupAddress.setStatus("current")
_MyIgmpInterfaceStaticStatus_Type = RowStatus
_MyIgmpInterfaceStaticStatus_Object = MibTableColumn
myIgmpInterfaceStaticStatus = _MyIgmpInterfaceStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 2, 1, 3),
    _MyIgmpInterfaceStaticStatus_Type()
)
myIgmpInterfaceStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myIgmpInterfaceStaticStatus.setStatus("current")
_MyIgmpTraps_ObjectIdentity = ObjectIdentity
myIgmpTraps = _MyIgmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 3)
)
_MyIgmpMIBConformance_ObjectIdentity = ObjectIdentity
myIgmpMIBConformance = _MyIgmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 2)
)
_MyIgmpMIBCompliances_ObjectIdentity = ObjectIdentity
myIgmpMIBCompliances = _MyIgmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 2, 1)
)
_MyIgmpMIBGroups_ObjectIdentity = ObjectIdentity
myIgmpMIBGroups = _MyIgmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 2, 2)
)

# Managed Objects groups

myIgmpInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 2, 2, 1)
)
myIgmpInterfaceMIBGroup.setObjects(
      *(("DES7200-IGMP-MIB", "myIgmpInterfaceIfIndex"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceQueryInterval"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceVersion"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceQuerier"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceQueryMaxResponseTime"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceQuerierUpTime"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceQuerierExpiryTime"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceVersion1QuerierTimer"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceWrongVersionQueries"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceJoins"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceProxyIfIndex"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceGroups"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceRobustness"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceLastMembQueryIntvl"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceQuerierPresentTimeout"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceLeaves"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceAccessGroupAclName"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceEnabled"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    myIgmpInterfaceMIBGroup.setStatus("current")

myIgmpInterfaceStaticMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 2, 2, 2)
)
myIgmpInterfaceStaticMIBGroup.setObjects(
      *(("DES7200-IGMP-MIB", "myIgmpInterfaceStaticInterface"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceStaticGroupAddress"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceStaticStatus"))
)
if mibBuilder.loadTexts:
    myIgmpInterfaceStaticMIBGroup.setStatus("current")


# Notification objects

myIgmpVersionConflicted = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 1, 3, 1)
)
myIgmpVersionConflicted.setObjects(
      *(("DES7200-IGMP-MIB", "myIgmpInterfaceIfIndex"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceVersion"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    myIgmpVersionConflicted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

myIgmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 2, 1, 1)
)
myIgmpMIBCompliance.setObjects(
      *(("DES7200-IGMP-MIB", "myIgmpInterfaceMIBGroup"),
        ("DES7200-IGMP-MIB", "myIgmpInterfaceStaticMIBGroup"))
)
if mibBuilder.loadTexts:
    myIgmpMIBCompliance.setStatus(
        "current"
    )

igmpExternCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 26, 2, 1, 2)
)
if mibBuilder.loadTexts:
    igmpExternCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-IGMP-MIB",
    **{"myIgmpMIB": myIgmpMIB,
       "myIgmpMIBObjects": myIgmpMIBObjects,
       "myIgmpInterfaceTable": myIgmpInterfaceTable,
       "myIgmpInterfaceEntry": myIgmpInterfaceEntry,
       "myIgmpInterfaceIfIndex": myIgmpInterfaceIfIndex,
       "myIgmpInterfaceQueryInterval": myIgmpInterfaceQueryInterval,
       "myIgmpInterfaceVersion": myIgmpInterfaceVersion,
       "myIgmpInterfaceQuerier": myIgmpInterfaceQuerier,
       "myIgmpInterfaceQueryMaxResponseTime": myIgmpInterfaceQueryMaxResponseTime,
       "myIgmpInterfaceQuerierUpTime": myIgmpInterfaceQuerierUpTime,
       "myIgmpInterfaceQuerierExpiryTime": myIgmpInterfaceQuerierExpiryTime,
       "myIgmpInterfaceVersion1QuerierTimer": myIgmpInterfaceVersion1QuerierTimer,
       "myIgmpInterfaceWrongVersionQueries": myIgmpInterfaceWrongVersionQueries,
       "myIgmpInterfaceJoins": myIgmpInterfaceJoins,
       "myIgmpInterfaceProxyIfIndex": myIgmpInterfaceProxyIfIndex,
       "myIgmpInterfaceGroups": myIgmpInterfaceGroups,
       "myIgmpInterfaceRobustness": myIgmpInterfaceRobustness,
       "myIgmpInterfaceLastMembQueryIntvl": myIgmpInterfaceLastMembQueryIntvl,
       "myIgmpInterfaceQuerierPresentTimeout": myIgmpInterfaceQuerierPresentTimeout,
       "myIgmpInterfaceLeaves": myIgmpInterfaceLeaves,
       "myIgmpInterfaceAccessGroupAclName": myIgmpInterfaceAccessGroupAclName,
       "myIgmpInterfaceEnabled": myIgmpInterfaceEnabled,
       "myIgmpInterfaceHostVersion": myIgmpInterfaceHostVersion,
       "myIgmpInterfaceStaticTable": myIgmpInterfaceStaticTable,
       "myIgmpInterfaceStaticEntry": myIgmpInterfaceStaticEntry,
       "myIgmpInterfaceStaticInterface": myIgmpInterfaceStaticInterface,
       "myIgmpInterfaceStaticGroupAddress": myIgmpInterfaceStaticGroupAddress,
       "myIgmpInterfaceStaticStatus": myIgmpInterfaceStaticStatus,
       "myIgmpTraps": myIgmpTraps,
       "myIgmpVersionConflicted": myIgmpVersionConflicted,
       "myIgmpMIBConformance": myIgmpMIBConformance,
       "myIgmpMIBCompliances": myIgmpMIBCompliances,
       "myIgmpMIBCompliance": myIgmpMIBCompliance,
       "igmpExternCompliance": igmpExternCompliance,
       "myIgmpMIBGroups": myIgmpMIBGroups,
       "myIgmpInterfaceMIBGroup": myIgmpInterfaceMIBGroup,
       "myIgmpInterfaceStaticMIBGroup": myIgmpInterfaceStaticMIBGroup}
)
