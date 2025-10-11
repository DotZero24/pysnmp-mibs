# SNMP MIB module (ZTE-AN-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-MAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:08 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnMacMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnMacObjects_ObjectIdentity = ObjectIdentity
zxAnMacObjects = _ZxAnMacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1)
)
_ZxAnMacGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnMacGlobalObjects = _ZxAnMacGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1)
)
_ZxAnMacTableCapacity_Type = Integer32
_ZxAnMacTableCapacity_Object = MibScalar
zxAnMacTableCapacity = _ZxAnMacTableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 1),
    _ZxAnMacTableCapacity_Type()
)
zxAnMacTableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacTableCapacity.setStatus("current")
_ZxAnMacTableCurrUtilization_Type = Integer32
_ZxAnMacTableCurrUtilization_Object = MibScalar
zxAnMacTableCurrUtilization = _ZxAnMacTableCurrUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 2),
    _ZxAnMacTableCurrUtilization_Type()
)
zxAnMacTableCurrUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacTableCurrUtilization.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMacTableCurrUtilization.setUnits("percent")


class _ZxAnMacTableUtilizationThreshold_Type(Integer32):
    """Custom type zxAnMacTableUtilizationThreshold based on Integer32"""
    defaultValue = 70


_ZxAnMacTableUtilizationThreshold_Type.__name__ = "Integer32"
_ZxAnMacTableUtilizationThreshold_Object = MibScalar
zxAnMacTableUtilizationThreshold = _ZxAnMacTableUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 3),
    _ZxAnMacTableUtilizationThreshold_Type()
)
zxAnMacTableUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMacTableUtilizationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMacTableUtilizationThreshold.setUnits("percent")
_ZxAnMacTableCurrMaxUtilization_Type = Integer32
_ZxAnMacTableCurrMaxUtilization_Object = MibScalar
zxAnMacTableCurrMaxUtilization = _ZxAnMacTableCurrMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 4),
    _ZxAnMacTableCurrMaxUtilization_Type()
)
zxAnMacTableCurrMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacTableCurrMaxUtilization.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMacTableCurrMaxUtilization.setUnits("percent")
_ZxAnMacTableHisMaxUtilization_Type = Integer32
_ZxAnMacTableHisMaxUtilization_Object = MibScalar
zxAnMacTableHisMaxUtilization = _ZxAnMacTableHisMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 5),
    _ZxAnMacTableHisMaxUtilization_Type()
)
zxAnMacTableHisMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacTableHisMaxUtilization.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMacTableHisMaxUtilization.setUnits("percent")


class _ZxAnMacTableMonitorInterval_Type(Integer32):
    """Custom type zxAnMacTableMonitorInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1440),
    )


_ZxAnMacTableMonitorInterval_Type.__name__ = "Integer32"
_ZxAnMacTableMonitorInterval_Object = MibScalar
zxAnMacTableMonitorInterval = _ZxAnMacTableMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 6),
    _ZxAnMacTableMonitorInterval_Type()
)
zxAnMacTableMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMacTableMonitorInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMacTableMonitorInterval.setUnits("minute")
_ZxAnMacTableMonitorElapsedTime_Type = Integer32
_ZxAnMacTableMonitorElapsedTime_Object = MibScalar
zxAnMacTableMonitorElapsedTime = _ZxAnMacTableMonitorElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 7),
    _ZxAnMacTableMonitorElapsedTime_Type()
)
zxAnMacTableMonitorElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacTableMonitorElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMacTableMonitorElapsedTime.setUnits("second")


class _ZxAnMacAgingTime_Type(Integer32):
    """Custom type zxAnMacAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_ZxAnMacAgingTime_Type.__name__ = "Integer32"
_ZxAnMacAgingTime_Object = MibScalar
zxAnMacAgingTime = _ZxAnMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 8),
    _ZxAnMacAgingTime_Type()
)
zxAnMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMacAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMacAgingTime.setUnits("seconds")
_ZxAnMacTableCurrTotalMacAddress_Type = Integer32
_ZxAnMacTableCurrTotalMacAddress_Object = MibScalar
zxAnMacTableCurrTotalMacAddress = _ZxAnMacTableCurrTotalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 9),
    _ZxAnMacTableCurrTotalMacAddress_Type()
)
zxAnMacTableCurrTotalMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacTableCurrTotalMacAddress.setStatus("current")


class _ZxAnMacCapabilities_Type(Bits):
    """Custom type zxAnMacCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("macForwardingTableIndexChanged", 0),
          ("supportPermanentMac", 1))
    )

_ZxAnMacCapabilities_Type.__name__ = "Bits"
_ZxAnMacCapabilities_Object = MibScalar
zxAnMacCapabilities = _ZxAnMacCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 1, 50),
    _ZxAnMacCapabilities_Type()
)
zxAnMacCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacCapabilities.setStatus("current")
_ZxAnMacForwardingTable_Object = MibTable
zxAnMacForwardingTable = _ZxAnMacForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnMacForwardingTable.setStatus("current")
_ZxAnMacForwardingEntry_Object = MibTableRow
zxAnMacForwardingEntry = _ZxAnMacForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 3, 1)
)
zxAnMacForwardingEntry.setIndexNames(
    (0, "ZTE-AN-MAC-MIB", "zxAnMacForwardingAddrType"),
    (0, "ZTE-AN-MAC-MIB", "zxAnMacForwardingIfIndex"),
    (0, "ZTE-AN-MAC-MIB", "zxAnMacForwardingVlanId"),
    (0, "ZTE-AN-MAC-MIB", "zxAnMacForwardingAddr"),
)
if mibBuilder.loadTexts:
    zxAnMacForwardingEntry.setStatus("current")


class _ZxAnMacForwardingAddrType_Type(Integer32):
    """Custom type zxAnMacForwardingAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2),
          ("static", 3))
    )


_ZxAnMacForwardingAddrType_Type.__name__ = "Integer32"
_ZxAnMacForwardingAddrType_Object = MibTableColumn
zxAnMacForwardingAddrType = _ZxAnMacForwardingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 3, 1, 1),
    _ZxAnMacForwardingAddrType_Type()
)
zxAnMacForwardingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMacForwardingAddrType.setStatus("current")
_ZxAnMacForwardingIfIndex_Type = ZxAnIfindex
_ZxAnMacForwardingIfIndex_Object = MibTableColumn
zxAnMacForwardingIfIndex = _ZxAnMacForwardingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 3, 1, 2),
    _ZxAnMacForwardingIfIndex_Type()
)
zxAnMacForwardingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMacForwardingIfIndex.setStatus("current")
_ZxAnMacForwardingVlanId_Type = Integer32
_ZxAnMacForwardingVlanId_Object = MibTableColumn
zxAnMacForwardingVlanId = _ZxAnMacForwardingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 3, 1, 3),
    _ZxAnMacForwardingVlanId_Type()
)
zxAnMacForwardingVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMacForwardingVlanId.setStatus("current")
_ZxAnMacForwardingAddr_Type = MacAddress
_ZxAnMacForwardingAddr_Object = MibTableColumn
zxAnMacForwardingAddr = _ZxAnMacForwardingAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 3, 1, 4),
    _ZxAnMacForwardingAddr_Type()
)
zxAnMacForwardingAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMacForwardingAddr.setStatus("current")
_ZxAnMacFwdConfRowStatus_Type = RowStatus
_ZxAnMacFwdConfRowStatus_Object = MibTableColumn
zxAnMacFwdConfRowStatus = _ZxAnMacFwdConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 3, 1, 5),
    _ZxAnMacFwdConfRowStatus_Type()
)
zxAnMacFwdConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMacFwdConfRowStatus.setStatus("current")
_ZxAnMacPoolTable_Object = MibTable
zxAnMacPoolTable = _ZxAnMacPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnMacPoolTable.setStatus("current")
_ZxAnMacPoolEntry_Object = MibTableRow
zxAnMacPoolEntry = _ZxAnMacPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 4, 1)
)
zxAnMacPoolEntry.setIndexNames(
    (0, "ZTE-AN-MAC-MIB", "zxAnMacPoolIndex"),
)
if mibBuilder.loadTexts:
    zxAnMacPoolEntry.setStatus("current")


class _ZxAnMacPoolIndex_Type(Integer32):
    """Custom type zxAnMacPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnMacPoolIndex_Type.__name__ = "Integer32"
_ZxAnMacPoolIndex_Object = MibTableColumn
zxAnMacPoolIndex = _ZxAnMacPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 4, 1, 1),
    _ZxAnMacPoolIndex_Type()
)
zxAnMacPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMacPoolIndex.setStatus("current")
_ZxAnMacPoolStartMac_Type = MacAddress
_ZxAnMacPoolStartMac_Object = MibTableColumn
zxAnMacPoolStartMac = _ZxAnMacPoolStartMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 4, 1, 2),
    _ZxAnMacPoolStartMac_Type()
)
zxAnMacPoolStartMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMacPoolStartMac.setStatus("current")


class _ZxAnMacPoolSize_Type(Integer32):
    """Custom type zxAnMacPoolSize based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ZxAnMacPoolSize_Type.__name__ = "Integer32"
_ZxAnMacPoolSize_Object = MibTableColumn
zxAnMacPoolSize = _ZxAnMacPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 4, 1, 3),
    _ZxAnMacPoolSize_Type()
)
zxAnMacPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMacPoolSize.setStatus("current")


class _ZxAnMacPoolAvailableSize_Type(Integer32):
    """Custom type zxAnMacPoolAvailableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ZxAnMacPoolAvailableSize_Type.__name__ = "Integer32"
_ZxAnMacPoolAvailableSize_Object = MibTableColumn
zxAnMacPoolAvailableSize = _ZxAnMacPoolAvailableSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 4, 1, 4),
    _ZxAnMacPoolAvailableSize_Type()
)
zxAnMacPoolAvailableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacPoolAvailableSize.setStatus("current")
_ZxAnMacPoolRowStatus_Type = RowStatus
_ZxAnMacPoolRowStatus_Object = MibTableColumn
zxAnMacPoolRowStatus = _ZxAnMacPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 1, 4, 1, 5),
    _ZxAnMacPoolRowStatus_Type()
)
zxAnMacPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMacPoolRowStatus.setStatus("current")
_ZxAnMacTrapObjects_ObjectIdentity = ObjectIdentity
zxAnMacTrapObjects = _ZxAnMacTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 2)
)
_ZxAnMacPerfObjects_ObjectIdentity = ObjectIdentity
zxAnMacPerfObjects = _ZxAnMacPerfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 3)
)
_ZxAnMacUsageRateGroupPerf_Type = Counter64
_ZxAnMacUsageRateGroupPerf_Object = MibScalar
zxAnMacUsageRateGroupPerf = _ZxAnMacUsageRateGroupPerf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 3, 1),
    _ZxAnMacUsageRateGroupPerf_Type()
)
zxAnMacUsageRateGroupPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacUsageRateGroupPerf.setStatus("current")
_ZxAnMacMaxUsageRatePerf_Type = Counter64
_ZxAnMacMaxUsageRatePerf_Object = MibScalar
zxAnMacMaxUsageRatePerf = _ZxAnMacMaxUsageRatePerf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 3, 2),
    _ZxAnMacMaxUsageRatePerf_Type()
)
zxAnMacMaxUsageRatePerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacMaxUsageRatePerf.setStatus("current")
_ZxAnMacMinUsageRatePerf_Type = Counter64
_ZxAnMacMinUsageRatePerf_Object = MibScalar
zxAnMacMinUsageRatePerf = _ZxAnMacMinUsageRatePerf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 3, 3),
    _ZxAnMacMinUsageRatePerf_Type()
)
zxAnMacMinUsageRatePerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacMinUsageRatePerf.setStatus("current")
_ZxAnMacAverageUsageRatePerf_Type = Counter64
_ZxAnMacAverageUsageRatePerf_Object = MibScalar
zxAnMacAverageUsageRatePerf = _ZxAnMacAverageUsageRatePerf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 3, 4),
    _ZxAnMacAverageUsageRatePerf_Type()
)
zxAnMacAverageUsageRatePerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMacAverageUsageRatePerf.setStatus("current")

# Managed Objects groups


# Notification objects

zxAnMacTableUsageOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 6, 2, 1)
)
zxAnMacTableUsageOverThreshTrap.setObjects(
      *(("ZTE-AN-MAC-MIB", "zxAnMacTableCurrentUsage"),
        ("ZTE-AN-MAC-MIB", "zxAnMacTableUsageThreshold"))
)
if mibBuilder.loadTexts:
    zxAnMacTableUsageOverThreshTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-MAC-MIB",
    **{"zxAnMacMib": zxAnMacMib,
       "zxAnMacObjects": zxAnMacObjects,
       "zxAnMacGlobalObjects": zxAnMacGlobalObjects,
       "zxAnMacTableCapacity": zxAnMacTableCapacity,
       "zxAnMacTableCurrUtilization": zxAnMacTableCurrUtilization,
       "zxAnMacTableUtilizationThreshold": zxAnMacTableUtilizationThreshold,
       "zxAnMacTableCurrMaxUtilization": zxAnMacTableCurrMaxUtilization,
       "zxAnMacTableHisMaxUtilization": zxAnMacTableHisMaxUtilization,
       "zxAnMacTableMonitorInterval": zxAnMacTableMonitorInterval,
       "zxAnMacTableMonitorElapsedTime": zxAnMacTableMonitorElapsedTime,
       "zxAnMacAgingTime": zxAnMacAgingTime,
       "zxAnMacTableCurrTotalMacAddress": zxAnMacTableCurrTotalMacAddress,
       "zxAnMacCapabilities": zxAnMacCapabilities,
       "zxAnMacForwardingTable": zxAnMacForwardingTable,
       "zxAnMacForwardingEntry": zxAnMacForwardingEntry,
       "zxAnMacForwardingAddrType": zxAnMacForwardingAddrType,
       "zxAnMacForwardingIfIndex": zxAnMacForwardingIfIndex,
       "zxAnMacForwardingVlanId": zxAnMacForwardingVlanId,
       "zxAnMacForwardingAddr": zxAnMacForwardingAddr,
       "zxAnMacFwdConfRowStatus": zxAnMacFwdConfRowStatus,
       "zxAnMacPoolTable": zxAnMacPoolTable,
       "zxAnMacPoolEntry": zxAnMacPoolEntry,
       "zxAnMacPoolIndex": zxAnMacPoolIndex,
       "zxAnMacPoolStartMac": zxAnMacPoolStartMac,
       "zxAnMacPoolSize": zxAnMacPoolSize,
       "zxAnMacPoolAvailableSize": zxAnMacPoolAvailableSize,
       "zxAnMacPoolRowStatus": zxAnMacPoolRowStatus,
       "zxAnMacTrapObjects": zxAnMacTrapObjects,
       "zxAnMacTableUsageOverThreshTrap": zxAnMacTableUsageOverThreshTrap,
       "zxAnMacPerfObjects": zxAnMacPerfObjects,
       "zxAnMacUsageRateGroupPerf": zxAnMacUsageRateGroupPerf,
       "zxAnMacMaxUsageRatePerf": zxAnMacMaxUsageRatePerf,
       "zxAnMacMinUsageRatePerf": zxAnMacMinUsageRatePerf,
       "zxAnMacAverageUsageRatePerf": zxAnMacAverageUsageRatePerf}
)
