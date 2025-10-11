# SNMP MIB module (IGMPV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/IGMPV3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:56 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

swIgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwIgmpMIBObjects_ObjectIdentity = ObjectIdentity
swIgmpMIBObjects = _SwIgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1)
)
_MgmdRouterInterfaceTable_Object = MibTable
mgmdRouterInterfaceTable = _MgmdRouterInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4)
)
if mibBuilder.loadTexts:
    mgmdRouterInterfaceTable.setStatus("current")
_MgmdRouterInterfaceEntry_Object = MibTableRow
mgmdRouterInterfaceEntry = _MgmdRouterInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1)
)
mgmdRouterInterfaceEntry.setIndexNames(
    (0, "IGMPV3-MIB", "mgmdRouterInterfaceIfIndex"),
    (0, "IGMPV3-MIB", "mgmdRouterInterfaceQuerierType"),
)
if mibBuilder.loadTexts:
    mgmdRouterInterfaceEntry.setStatus("current")
_MgmdRouterInterfaceIfIndex_Type = InterfaceIndex
_MgmdRouterInterfaceIfIndex_Object = MibTableColumn
mgmdRouterInterfaceIfIndex = _MgmdRouterInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 1),
    _MgmdRouterInterfaceIfIndex_Type()
)
mgmdRouterInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceIfIndex.setStatus("current")
_MgmdRouterInterfaceQuerierType_Type = InetAddressType
_MgmdRouterInterfaceQuerierType_Object = MibTableColumn
mgmdRouterInterfaceQuerierType = _MgmdRouterInterfaceQuerierType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 2),
    _MgmdRouterInterfaceQuerierType_Type()
)
mgmdRouterInterfaceQuerierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQuerierType.setStatus("current")
_MgmdRouterInterfaceQuerier_Type = InetAddress
_MgmdRouterInterfaceQuerier_Object = MibTableColumn
mgmdRouterInterfaceQuerier = _MgmdRouterInterfaceQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 3),
    _MgmdRouterInterfaceQuerier_Type()
)
mgmdRouterInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQuerier.setStatus("current")


class _MgmdRouterInterfaceQueryInterval_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125


_MgmdRouterInterfaceQueryInterval_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceQueryInterval_Object = MibTableColumn
mgmdRouterInterfaceQueryInterval = _MgmdRouterInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 4),
    _MgmdRouterInterfaceQueryInterval_Type()
)
mgmdRouterInterfaceQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQueryInterval.setUnits("seconds")
_MgmdRouterInterfaceStatus_Type = RowStatus
_MgmdRouterInterfaceStatus_Object = MibTableColumn
mgmdRouterInterfaceStatus = _MgmdRouterInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 5),
    _MgmdRouterInterfaceStatus_Type()
)
mgmdRouterInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceStatus.setStatus("current")


class _MgmdRouterInterfaceVersion_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceVersion based on Unsigned32"""
    defaultValue = 3


_MgmdRouterInterfaceVersion_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceVersion_Object = MibTableColumn
mgmdRouterInterfaceVersion = _MgmdRouterInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 6),
    _MgmdRouterInterfaceVersion_Type()
)
mgmdRouterInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceVersion.setStatus("current")


class _MgmdRouterInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MgmdRouterInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceQueryMaxResponseTime_Object = MibTableColumn
mgmdRouterInterfaceQueryMaxResponseTime = _MgmdRouterInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 7),
    _MgmdRouterInterfaceQueryMaxResponseTime_Type()
)
mgmdRouterInterfaceQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_MgmdRouterInterfaceQuerierUpTime_Type = TimeTicks
_MgmdRouterInterfaceQuerierUpTime_Object = MibTableColumn
mgmdRouterInterfaceQuerierUpTime = _MgmdRouterInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 8),
    _MgmdRouterInterfaceQuerierUpTime_Type()
)
mgmdRouterInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQuerierUpTime.setStatus("current")
_MgmdRouterInterfaceQuerierExpiryTime_Type = TimeTicks
_MgmdRouterInterfaceQuerierExpiryTime_Object = MibTableColumn
mgmdRouterInterfaceQuerierExpiryTime = _MgmdRouterInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 9),
    _MgmdRouterInterfaceQuerierExpiryTime_Type()
)
mgmdRouterInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQuerierExpiryTime.setStatus("current")


class _MgmdRouterInterfaceRobustness_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MgmdRouterInterfaceRobustness_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceRobustness_Object = MibTableColumn
mgmdRouterInterfaceRobustness = _MgmdRouterInterfaceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 14),
    _MgmdRouterInterfaceRobustness_Type()
)
mgmdRouterInterfaceRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceRobustness.setStatus("current")


class _MgmdRouterInterfaceLastMembQueryIntvl_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MgmdRouterInterfaceLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceLastMembQueryIntvl_Object = MibTableColumn
mgmdRouterInterfaceLastMembQueryIntvl = _MgmdRouterInterfaceLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 4, 1, 15),
    _MgmdRouterInterfaceLastMembQueryIntvl_Type()
)
mgmdRouterInterfaceLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceLastMembQueryIntvl.setUnits("tenths of seconds")
_MgmdRouterCacheTable_Object = MibTable
mgmdRouterCacheTable = _MgmdRouterCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6)
)
if mibBuilder.loadTexts:
    mgmdRouterCacheTable.setStatus("current")
_MgmdRouterCacheEntry_Object = MibTableRow
mgmdRouterCacheEntry = _MgmdRouterCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1)
)
mgmdRouterCacheEntry.setIndexNames(
    (0, "IGMPV3-MIB", "mgmdRouterCacheAddressType"),
    (0, "IGMPV3-MIB", "mgmdRouterCacheIfIndex"),
    (0, "IGMPV3-MIB", "mgmdRouterCacheAddress"),
)
if mibBuilder.loadTexts:
    mgmdRouterCacheEntry.setStatus("current")
_MgmdRouterCacheAddressType_Type = InetAddressType
_MgmdRouterCacheAddressType_Object = MibTableColumn
mgmdRouterCacheAddressType = _MgmdRouterCacheAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 1),
    _MgmdRouterCacheAddressType_Type()
)
mgmdRouterCacheAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheAddressType.setStatus("current")
_MgmdRouterCacheIfIndex_Type = InterfaceIndex
_MgmdRouterCacheIfIndex_Object = MibTableColumn
mgmdRouterCacheIfIndex = _MgmdRouterCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 2),
    _MgmdRouterCacheIfIndex_Type()
)
mgmdRouterCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterCacheIfIndex.setStatus("current")
_MgmdRouterCacheAddress_Type = InetAddress
_MgmdRouterCacheAddress_Object = MibTableColumn
mgmdRouterCacheAddress = _MgmdRouterCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 3),
    _MgmdRouterCacheAddress_Type()
)
mgmdRouterCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterCacheAddress.setStatus("current")
_MgmdRouterCacheLastReporter_Type = InetAddress
_MgmdRouterCacheLastReporter_Object = MibTableColumn
mgmdRouterCacheLastReporter = _MgmdRouterCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 4),
    _MgmdRouterCacheLastReporter_Type()
)
mgmdRouterCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheLastReporter.setStatus("current")
_MgmdRouterCacheExpiryTime_Type = TimeTicks
_MgmdRouterCacheExpiryTime_Object = MibTableColumn
mgmdRouterCacheExpiryTime = _MgmdRouterCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 6),
    _MgmdRouterCacheExpiryTime_Type()
)
mgmdRouterCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheExpiryTime.setStatus("current")
_MgmdRouterCacheStatus_Type = RowStatus
_MgmdRouterCacheStatus_Object = MibTableColumn
mgmdRouterCacheStatus = _MgmdRouterCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 7),
    _MgmdRouterCacheStatus_Type()
)
mgmdRouterCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterCacheStatus.setStatus("current")
_MgmdRouterCacheVersion1HostTimer_Type = TimeTicks
_MgmdRouterCacheVersion1HostTimer_Object = MibTableColumn
mgmdRouterCacheVersion1HostTimer = _MgmdRouterCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 8),
    _MgmdRouterCacheVersion1HostTimer_Type()
)
mgmdRouterCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheVersion1HostTimer.setStatus("current")
_MgmdRouterCacheVersion2HostTimer_Type = TimeTicks
_MgmdRouterCacheVersion2HostTimer_Object = MibTableColumn
mgmdRouterCacheVersion2HostTimer = _MgmdRouterCacheVersion2HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 9),
    _MgmdRouterCacheVersion2HostTimer_Type()
)
mgmdRouterCacheVersion2HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheVersion2HostTimer.setStatus("current")


class _MgmdRouterCacheSourceFilterMode_Type(Integer32):
    """Custom type mgmdRouterCacheSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_MgmdRouterCacheSourceFilterMode_Type.__name__ = "Integer32"
_MgmdRouterCacheSourceFilterMode_Object = MibTableColumn
mgmdRouterCacheSourceFilterMode = _MgmdRouterCacheSourceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 6, 1, 10),
    _MgmdRouterCacheSourceFilterMode_Type()
)
mgmdRouterCacheSourceFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheSourceFilterMode.setStatus("current")
_MgmdRouterSrcListTable_Object = MibTable
mgmdRouterSrcListTable = _MgmdRouterSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 10)
)
if mibBuilder.loadTexts:
    mgmdRouterSrcListTable.setStatus("current")
_MgmdRouterSrcListEntry_Object = MibTableRow
mgmdRouterSrcListEntry = _MgmdRouterSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 10, 1)
)
mgmdRouterSrcListEntry.setIndexNames(
    (0, "IGMPV3-MIB", "mgmdRouterSrcListAddressType"),
    (0, "IGMPV3-MIB", "mgmdRouterSrcListIfIndex"),
    (0, "IGMPV3-MIB", "mgmdRouterSrcListAddress"),
    (0, "IGMPV3-MIB", "mgmdRouterSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    mgmdRouterSrcListEntry.setStatus("current")
_MgmdRouterSrcListAddressType_Type = InetAddressType
_MgmdRouterSrcListAddressType_Object = MibTableColumn
mgmdRouterSrcListAddressType = _MgmdRouterSrcListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 10, 1, 1),
    _MgmdRouterSrcListAddressType_Type()
)
mgmdRouterSrcListAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterSrcListAddressType.setStatus("current")
_MgmdRouterSrcListIfIndex_Type = InterfaceIndex
_MgmdRouterSrcListIfIndex_Object = MibTableColumn
mgmdRouterSrcListIfIndex = _MgmdRouterSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 10, 1, 2),
    _MgmdRouterSrcListIfIndex_Type()
)
mgmdRouterSrcListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterSrcListIfIndex.setStatus("current")
_MgmdRouterSrcListAddress_Type = InetAddress
_MgmdRouterSrcListAddress_Object = MibTableColumn
mgmdRouterSrcListAddress = _MgmdRouterSrcListAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 10, 1, 3),
    _MgmdRouterSrcListAddress_Type()
)
mgmdRouterSrcListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterSrcListAddress.setStatus("current")
_MgmdRouterSrcListHostAddress_Type = InetAddress
_MgmdRouterSrcListHostAddress_Object = MibTableColumn
mgmdRouterSrcListHostAddress = _MgmdRouterSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 10, 1, 4),
    _MgmdRouterSrcListHostAddress_Type()
)
mgmdRouterSrcListHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterSrcListHostAddress.setStatus("current")
_MgmdRouterSrcListExpire_Type = TimeTicks
_MgmdRouterSrcListExpire_Object = MibTableColumn
mgmdRouterSrcListExpire = _MgmdRouterSrcListExpire_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 10, 1, 5),
    _MgmdRouterSrcListExpire_Type()
)
mgmdRouterSrcListExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterSrcListExpire.setStatus("current")
_MgmdRouterChkSubSrcNetTable_Object = MibTable
mgmdRouterChkSubSrcNetTable = _MgmdRouterChkSubSrcNetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 11)
)
if mibBuilder.loadTexts:
    mgmdRouterChkSubSrcNetTable.setStatus("current")
_MgmdRouterChkSubSrcNetEntry_Object = MibTableRow
mgmdRouterChkSubSrcNetEntry = _MgmdRouterChkSubSrcNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 11, 1)
)
mgmdRouterChkSubSrcNetEntry.setIndexNames(
    (0, "IGMPV3-MIB", "mgmdRouterChkSubSrcNetIfIndex"),
)
if mibBuilder.loadTexts:
    mgmdRouterChkSubSrcNetEntry.setStatus("current")
_MgmdRouterChkSubSrcNetIfIndex_Type = InterfaceIndex
_MgmdRouterChkSubSrcNetIfIndex_Object = MibTableColumn
mgmdRouterChkSubSrcNetIfIndex = _MgmdRouterChkSubSrcNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 11, 1, 1),
    _MgmdRouterChkSubSrcNetIfIndex_Type()
)
mgmdRouterChkSubSrcNetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterChkSubSrcNetIfIndex.setStatus("current")
_MgmdRouterChkSubSrcNetIpAddr_Type = IpAddress
_MgmdRouterChkSubSrcNetIpAddr_Object = MibTableColumn
mgmdRouterChkSubSrcNetIpAddr = _MgmdRouterChkSubSrcNetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 11, 1, 2),
    _MgmdRouterChkSubSrcNetIpAddr_Type()
)
mgmdRouterChkSubSrcNetIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterChkSubSrcNetIpAddr.setStatus("current")
_MgmdRouterChkSubSrcNetIpNetMask_Type = IpAddress
_MgmdRouterChkSubSrcNetIpNetMask_Object = MibTableColumn
mgmdRouterChkSubSrcNetIpNetMask = _MgmdRouterChkSubSrcNetIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 11, 1, 3),
    _MgmdRouterChkSubSrcNetIpNetMask_Type()
)
mgmdRouterChkSubSrcNetIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterChkSubSrcNetIpNetMask.setStatus("current")


class _MgmdRouterChkSubSrcNetState_Type(Integer32):
    """Custom type mgmdRouterChkSubSrcNetState based on Integer32"""
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


_MgmdRouterChkSubSrcNetState_Type.__name__ = "Integer32"
_MgmdRouterChkSubSrcNetState_Object = MibTableColumn
mgmdRouterChkSubSrcNetState = _MgmdRouterChkSubSrcNetState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 11, 1, 4),
    _MgmdRouterChkSubSrcNetState_Type()
)
mgmdRouterChkSubSrcNetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdRouterChkSubSrcNetState.setStatus("current")
_MgmdRouterIGMPStaticGroupTable_Object = MibTable
mgmdRouterIGMPStaticGroupTable = _MgmdRouterIGMPStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 12)
)
if mibBuilder.loadTexts:
    mgmdRouterIGMPStaticGroupTable.setStatus("current")
_MgmdRouterIGMPStaticGroupEntry_Object = MibTableRow
mgmdRouterIGMPStaticGroupEntry = _MgmdRouterIGMPStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 12, 1)
)
mgmdRouterIGMPStaticGroupEntry.setIndexNames(
    (0, "IGMPV3-MIB", "mgmdRouterIGMPStaticGroupIfIndex"),
    (0, "IGMPV3-MIB", "mgmdRouterIGMPStaticGroupIpAddr"),
)
if mibBuilder.loadTexts:
    mgmdRouterIGMPStaticGroupEntry.setStatus("current")
_MgmdRouterIGMPStaticGroupIfIndex_Type = InterfaceIndex
_MgmdRouterIGMPStaticGroupIfIndex_Object = MibTableColumn
mgmdRouterIGMPStaticGroupIfIndex = _MgmdRouterIGMPStaticGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 12, 1, 1),
    _MgmdRouterIGMPStaticGroupIfIndex_Type()
)
mgmdRouterIGMPStaticGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterIGMPStaticGroupIfIndex.setStatus("current")
_MgmdRouterIGMPStaticGroupIpAddr_Type = IpAddress
_MgmdRouterIGMPStaticGroupIpAddr_Object = MibTableColumn
mgmdRouterIGMPStaticGroupIpAddr = _MgmdRouterIGMPStaticGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 12, 1, 2),
    _MgmdRouterIGMPStaticGroupIpAddr_Type()
)
mgmdRouterIGMPStaticGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterIGMPStaticGroupIpAddr.setStatus("current")
_MgmdRouterIGMPStaticGroupRowStatus_Type = RowStatus
_MgmdRouterIGMPStaticGroupRowStatus_Object = MibTableColumn
mgmdRouterIGMPStaticGroupRowStatus = _MgmdRouterIGMPStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 18, 1, 12, 1, 3),
    _MgmdRouterIGMPStaticGroupRowStatus_Type()
)
mgmdRouterIGMPStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterIGMPStaticGroupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IGMPV3-MIB",
    **{"swIgmpMIB": swIgmpMIB,
       "swIgmpMIBObjects": swIgmpMIBObjects,
       "mgmdRouterInterfaceTable": mgmdRouterInterfaceTable,
       "mgmdRouterInterfaceEntry": mgmdRouterInterfaceEntry,
       "mgmdRouterInterfaceIfIndex": mgmdRouterInterfaceIfIndex,
       "mgmdRouterInterfaceQuerierType": mgmdRouterInterfaceQuerierType,
       "mgmdRouterInterfaceQuerier": mgmdRouterInterfaceQuerier,
       "mgmdRouterInterfaceQueryInterval": mgmdRouterInterfaceQueryInterval,
       "mgmdRouterInterfaceStatus": mgmdRouterInterfaceStatus,
       "mgmdRouterInterfaceVersion": mgmdRouterInterfaceVersion,
       "mgmdRouterInterfaceQueryMaxResponseTime": mgmdRouterInterfaceQueryMaxResponseTime,
       "mgmdRouterInterfaceQuerierUpTime": mgmdRouterInterfaceQuerierUpTime,
       "mgmdRouterInterfaceQuerierExpiryTime": mgmdRouterInterfaceQuerierExpiryTime,
       "mgmdRouterInterfaceRobustness": mgmdRouterInterfaceRobustness,
       "mgmdRouterInterfaceLastMembQueryIntvl": mgmdRouterInterfaceLastMembQueryIntvl,
       "mgmdRouterCacheTable": mgmdRouterCacheTable,
       "mgmdRouterCacheEntry": mgmdRouterCacheEntry,
       "mgmdRouterCacheAddressType": mgmdRouterCacheAddressType,
       "mgmdRouterCacheIfIndex": mgmdRouterCacheIfIndex,
       "mgmdRouterCacheAddress": mgmdRouterCacheAddress,
       "mgmdRouterCacheLastReporter": mgmdRouterCacheLastReporter,
       "mgmdRouterCacheExpiryTime": mgmdRouterCacheExpiryTime,
       "mgmdRouterCacheStatus": mgmdRouterCacheStatus,
       "mgmdRouterCacheVersion1HostTimer": mgmdRouterCacheVersion1HostTimer,
       "mgmdRouterCacheVersion2HostTimer": mgmdRouterCacheVersion2HostTimer,
       "mgmdRouterCacheSourceFilterMode": mgmdRouterCacheSourceFilterMode,
       "mgmdRouterSrcListTable": mgmdRouterSrcListTable,
       "mgmdRouterSrcListEntry": mgmdRouterSrcListEntry,
       "mgmdRouterSrcListAddressType": mgmdRouterSrcListAddressType,
       "mgmdRouterSrcListIfIndex": mgmdRouterSrcListIfIndex,
       "mgmdRouterSrcListAddress": mgmdRouterSrcListAddress,
       "mgmdRouterSrcListHostAddress": mgmdRouterSrcListHostAddress,
       "mgmdRouterSrcListExpire": mgmdRouterSrcListExpire,
       "mgmdRouterChkSubSrcNetTable": mgmdRouterChkSubSrcNetTable,
       "mgmdRouterChkSubSrcNetEntry": mgmdRouterChkSubSrcNetEntry,
       "mgmdRouterChkSubSrcNetIfIndex": mgmdRouterChkSubSrcNetIfIndex,
       "mgmdRouterChkSubSrcNetIpAddr": mgmdRouterChkSubSrcNetIpAddr,
       "mgmdRouterChkSubSrcNetIpNetMask": mgmdRouterChkSubSrcNetIpNetMask,
       "mgmdRouterChkSubSrcNetState": mgmdRouterChkSubSrcNetState,
       "mgmdRouterIGMPStaticGroupTable": mgmdRouterIGMPStaticGroupTable,
       "mgmdRouterIGMPStaticGroupEntry": mgmdRouterIGMPStaticGroupEntry,
       "mgmdRouterIGMPStaticGroupIfIndex": mgmdRouterIGMPStaticGroupIfIndex,
       "mgmdRouterIGMPStaticGroupIpAddr": mgmdRouterIGMPStaticGroupIpAddr,
       "mgmdRouterIGMPStaticGroupRowStatus": mgmdRouterIGMPStaticGroupRowStatus}
)
