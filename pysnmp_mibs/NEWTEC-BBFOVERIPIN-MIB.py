# SNMP MIB module (NEWTEC-BBFOVERIPIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-BBFOVERIPIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:49 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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

ntcBbfOverIpIn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200)
)
if mibBuilder.loadTexts:
    ntcBbfOverIpIn.setRevisions(
        ("2017-07-10 12:00",
         "2014-09-09 09:00",
         "2014-07-15 08:00",
         "2013-09-18 08:00",
         "2013-05-22 06:00",
         "2013-03-27 10:00",
         "2013-01-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcBbfOIpInObjects_ObjectIdentity = ObjectIdentity
ntcBbfOIpInObjects = _NtcBbfOIpInObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1)
)
if mibBuilder.loadTexts:
    ntcBbfOIpInObjects.setStatus("current")


class _NtcBbfOIpInEnable_Type(NtcEnable):
    """Custom type ntcBbfOIpInEnable based on NtcEnable"""
    defaultValue = 0


_NtcBbfOIpInEnable_Type.__name__ = "NtcEnable"
_NtcBbfOIpInEnable_Object = MibScalar
ntcBbfOIpInEnable = _NtcBbfOIpInEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 1),
    _NtcBbfOIpInEnable_Type()
)
ntcBbfOIpInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpInEnable.setStatus("current")


class _NtcBbfOIpInInputSelection_Type(Integer32):
    """Custom type ntcBbfOIpInInputSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("data1", 2),
          ("data2", 3),
          ("data", 4),
          ("any", 5))
    )


_NtcBbfOIpInInputSelection_Type.__name__ = "Integer32"
_NtcBbfOIpInInputSelection_Object = MibScalar
ntcBbfOIpInInputSelection = _NtcBbfOIpInInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 2),
    _NtcBbfOIpInInputSelection_Type()
)
ntcBbfOIpInInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpInInputSelection.setStatus("current")
_NtcConfigurationTableTable_Object = MibTable
ntcConfigurationTableTable = _NtcConfigurationTableTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3)
)
if mibBuilder.loadTexts:
    ntcConfigurationTableTable.setStatus("current")
_NtcConfigurationTableEntry_Object = MibTableRow
ntcConfigurationTableEntry = _NtcConfigurationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1)
)
ntcConfigurationTableEntry.setIndexNames(
    (0, "NEWTEC-BBFOVERIPIN-MIB", "ntcConfigurationTableName"),
)
if mibBuilder.loadTexts:
    ntcConfigurationTableEntry.setStatus("current")


class _NtcConfigurationTableName_Type(DisplayString):
    """Custom type ntcConfigurationTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtcConfigurationTableName_Type.__name__ = "DisplayString"
_NtcConfigurationTableName_Object = MibTableColumn
ntcConfigurationTableName = _NtcConfigurationTableName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1, 1),
    _NtcConfigurationTableName_Type()
)
ntcConfigurationTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcConfigurationTableName.setStatus("current")
_NtcConfigurationTableRowStatus_Type = RowStatus
_NtcConfigurationTableRowStatus_Object = MibTableColumn
ntcConfigurationTableRowStatus = _NtcConfigurationTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1, 2),
    _NtcConfigurationTableRowStatus_Type()
)
ntcConfigurationTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcConfigurationTableRowStatus.setStatus("current")
_NtcBbfOIpInEpEnable_Type = NtcEnable
_NtcBbfOIpInEpEnable_Object = MibTableColumn
ntcBbfOIpInEpEnable = _NtcBbfOIpInEpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1, 3),
    _NtcBbfOIpInEpEnable_Type()
)
ntcBbfOIpInEpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcBbfOIpInEpEnable.setStatus("current")


class _NtcBbfOIpInIpEpAddressType_Type(Integer32):
    """Custom type ntcBbfOIpInIpEpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 0),
          ("multicast", 1))
    )


_NtcBbfOIpInIpEpAddressType_Type.__name__ = "Integer32"
_NtcBbfOIpInIpEpAddressType_Object = MibTableColumn
ntcBbfOIpInIpEpAddressType = _NtcBbfOIpInIpEpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1, 4),
    _NtcBbfOIpInIpEpAddressType_Type()
)
ntcBbfOIpInIpEpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcBbfOIpInIpEpAddressType.setStatus("current")
_NtcBbfOIpInEpMulticastAddress_Type = IpAddress
_NtcBbfOIpInEpMulticastAddress_Object = MibTableColumn
ntcBbfOIpInEpMulticastAddress = _NtcBbfOIpInEpMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1, 5),
    _NtcBbfOIpInEpMulticastAddress_Type()
)
ntcBbfOIpInEpMulticastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcBbfOIpInEpMulticastAddress.setStatus("current")


class _NtcBbfOIpInEpIpUdpPort_Type(Unsigned32):
    """Custom type ntcBbfOIpInEpIpUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcBbfOIpInEpIpUdpPort_Type.__name__ = "Unsigned32"
_NtcBbfOIpInEpIpUdpPort_Object = MibTableColumn
ntcBbfOIpInEpIpUdpPort = _NtcBbfOIpInEpIpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1, 6),
    _NtcBbfOIpInEpIpUdpPort_Type()
)
ntcBbfOIpInEpIpUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcBbfOIpInEpIpUdpPort.setStatus("current")


class _NtcBbfOIpInEpBbfType_Type(Integer32):
    """Custom type ntcBbfOIpInEpBbfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dvbbbf", 0),
          ("ntcbbf", 1))
    )


_NtcBbfOIpInEpBbfType_Type.__name__ = "Integer32"
_NtcBbfOIpInEpBbfType_Object = MibTableColumn
ntcBbfOIpInEpBbfType = _NtcBbfOIpInEpBbfType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1, 7),
    _NtcBbfOIpInEpBbfType_Type()
)
ntcBbfOIpInEpBbfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcBbfOIpInEpBbfType.setStatus("current")
_NtcBbfOIpInEpSourceRedundancy_Type = NtcEnable
_NtcBbfOIpInEpSourceRedundancy_Object = MibTableColumn
ntcBbfOIpInEpSourceRedundancy = _NtcBbfOIpInEpSourceRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 3, 1, 8),
    _NtcBbfOIpInEpSourceRedundancy_Type()
)
ntcBbfOIpInEpSourceRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcBbfOIpInEpSourceRedundancy.setStatus("current")
_NtcBbfOIpInMonitor_ObjectIdentity = ObjectIdentity
ntcBbfOIpInMonitor = _NtcBbfOIpInMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4)
)
if mibBuilder.loadTexts:
    ntcBbfOIpInMonitor.setStatus("current")


class _NtcBbfOIpInMonCounterReset_Type(Integer32):
    """Custom type ntcBbfOIpInMonCounterReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcBbfOIpInMonCounterReset_Type.__name__ = "Integer32"
_NtcBbfOIpInMonCounterReset_Object = MibScalar
ntcBbfOIpInMonCounterReset = _NtcBbfOIpInMonCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 1),
    _NtcBbfOIpInMonCounterReset_Type()
)
ntcBbfOIpInMonCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonCounterReset.setStatus("current")
_NtcBbfOIpInMonBbfInputBitRateT_Type = Unsigned32
_NtcBbfOIpInMonBbfInputBitRateT_Object = MibScalar
ntcBbfOIpInMonBbfInputBitRateT = _NtcBbfOIpInMonBbfInputBitRateT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 2),
    _NtcBbfOIpInMonBbfInputBitRateT_Type()
)
ntcBbfOIpInMonBbfInputBitRateT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInputBitRateT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInputBitRateT.setUnits("bps")
_NtcBbfOIpInMonBbfInCountT_Type = Counter32
_NtcBbfOIpInMonBbfInCountT_Object = MibScalar
ntcBbfOIpInMonBbfInCountT = _NtcBbfOIpInMonBbfInCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 3),
    _NtcBbfOIpInMonBbfInCountT_Type()
)
ntcBbfOIpInMonBbfInCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInCountT.setUnits("frames")
_NtcBbfOIpInMonBbfOutCountT_Type = Counter32
_NtcBbfOIpInMonBbfOutCountT_Object = MibScalar
ntcBbfOIpInMonBbfOutCountT = _NtcBbfOIpInMonBbfOutCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 4),
    _NtcBbfOIpInMonBbfOutCountT_Type()
)
ntcBbfOIpInMonBbfOutCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfOutCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfOutCountT.setUnits("frames")
_NtcBbfOIpInMonBbfDropCountT_Type = Counter32
_NtcBbfOIpInMonBbfDropCountT_Object = MibScalar
ntcBbfOIpInMonBbfDropCountT = _NtcBbfOIpInMonBbfDropCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 5),
    _NtcBbfOIpInMonBbfDropCountT_Type()
)
ntcBbfOIpInMonBbfDropCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfDropCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfDropCountT.setUnits("frames")
_NtcBbfOIpInMonBbfOverflowCountT_Type = Counter32
_NtcBbfOIpInMonBbfOverflowCountT_Object = MibScalar
ntcBbfOIpInMonBbfOverflowCountT = _NtcBbfOIpInMonBbfOverflowCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 6),
    _NtcBbfOIpInMonBbfOverflowCountT_Type()
)
ntcBbfOIpInMonBbfOverflowCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfOverflowCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfOverflowCountT.setUnits("frames")
_NtcBbfOIpInMonBbfByteOutCountT_Type = Counter32
_NtcBbfOIpInMonBbfByteOutCountT_Object = MibScalar
ntcBbfOIpInMonBbfByteOutCountT = _NtcBbfOIpInMonBbfByteOutCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 7),
    _NtcBbfOIpInMonBbfByteOutCountT_Type()
)
ntcBbfOIpInMonBbfByteOutCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfByteOutCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfByteOutCountT.setUnits("bytes")
_NtcBbfOIpInMonBbfInvFrameCountT_Type = Counter32
_NtcBbfOIpInMonBbfInvFrameCountT_Object = MibScalar
ntcBbfOIpInMonBbfInvFrameCountT = _NtcBbfOIpInMonBbfInvFrameCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 8),
    _NtcBbfOIpInMonBbfInvFrameCountT_Type()
)
ntcBbfOIpInMonBbfInvFrameCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInvFrameCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInvFrameCountT.setUnits("frames")
_NtcBbfOIpInMonBbfDiscontCountT_Type = Counter32
_NtcBbfOIpInMonBbfDiscontCountT_Object = MibScalar
ntcBbfOIpInMonBbfDiscontCountT = _NtcBbfOIpInMonBbfDiscontCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 9),
    _NtcBbfOIpInMonBbfDiscontCountT_Type()
)
ntcBbfOIpInMonBbfDiscontCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfDiscontCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfDiscontCountT.setUnits("frames")
_NtcBbfOIpInMonBbfModcodNSCountT_Type = Counter32
_NtcBbfOIpInMonBbfModcodNSCountT_Object = MibScalar
ntcBbfOIpInMonBbfModcodNSCountT = _NtcBbfOIpInMonBbfModcodNSCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 10),
    _NtcBbfOIpInMonBbfModcodNSCountT_Type()
)
ntcBbfOIpInMonBbfModcodNSCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfModcodNSCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfModcodNSCountT.setUnits("frames")
_NtcMonitoringTableTable_Object = MibTable
ntcMonitoringTableTable = _NtcMonitoringTableTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11)
)
if mibBuilder.loadTexts:
    ntcMonitoringTableTable.setStatus("current")
_NtcMonitoringTableEntry_Object = MibTableRow
ntcMonitoringTableEntry = _NtcMonitoringTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1)
)
ntcMonitoringTableEntry.setIndexNames(
    (0, "NEWTEC-BBFOVERIPIN-MIB", "ntcMonitoringTableName"),
)
if mibBuilder.loadTexts:
    ntcMonitoringTableEntry.setStatus("current")


class _NtcMonitoringTableName_Type(DisplayString):
    """Custom type ntcMonitoringTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcMonitoringTableName_Type.__name__ = "DisplayString"
_NtcMonitoringTableName_Object = MibTableColumn
ntcMonitoringTableName = _NtcMonitoringTableName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 1),
    _NtcMonitoringTableName_Type()
)
ntcMonitoringTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMonitoringTableName.setStatus("current")
_NtcBbfOIpInMonBbfInputBitRate_Type = Unsigned32
_NtcBbfOIpInMonBbfInputBitRate_Object = MibTableColumn
ntcBbfOIpInMonBbfInputBitRate = _NtcBbfOIpInMonBbfInputBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 2),
    _NtcBbfOIpInMonBbfInputBitRate_Type()
)
ntcBbfOIpInMonBbfInputBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInputBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInputBitRate.setUnits("bps")


class _NtcBbfOIpInMonSourceAddress_Type(DisplayString):
    """Custom type ntcBbfOIpInMonSourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcBbfOIpInMonSourceAddress_Type.__name__ = "DisplayString"
_NtcBbfOIpInMonSourceAddress_Object = MibTableColumn
ntcBbfOIpInMonSourceAddress = _NtcBbfOIpInMonSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 3),
    _NtcBbfOIpInMonSourceAddress_Type()
)
ntcBbfOIpInMonSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonSourceAddress.setStatus("current")
_NtcBbfOIpInMonBbfInCount_Type = Counter32
_NtcBbfOIpInMonBbfInCount_Object = MibTableColumn
ntcBbfOIpInMonBbfInCount = _NtcBbfOIpInMonBbfInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 4),
    _NtcBbfOIpInMonBbfInCount_Type()
)
ntcBbfOIpInMonBbfInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInCount.setUnits("frames")
_NtcBbfOIpInMonBbfOutCount_Type = Counter32
_NtcBbfOIpInMonBbfOutCount_Object = MibTableColumn
ntcBbfOIpInMonBbfOutCount = _NtcBbfOIpInMonBbfOutCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 5),
    _NtcBbfOIpInMonBbfOutCount_Type()
)
ntcBbfOIpInMonBbfOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfOutCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfOutCount.setUnits("frames")
_NtcBbfOIpInMonBbfByteOutCount_Type = Counter32
_NtcBbfOIpInMonBbfByteOutCount_Object = MibTableColumn
ntcBbfOIpInMonBbfByteOutCount = _NtcBbfOIpInMonBbfByteOutCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 6),
    _NtcBbfOIpInMonBbfByteOutCount_Type()
)
ntcBbfOIpInMonBbfByteOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfByteOutCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfByteOutCount.setUnits("bytes")
_NtcBbfOIpInMonBbfDropCount_Type = Counter32
_NtcBbfOIpInMonBbfDropCount_Object = MibTableColumn
ntcBbfOIpInMonBbfDropCount = _NtcBbfOIpInMonBbfDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 7),
    _NtcBbfOIpInMonBbfDropCount_Type()
)
ntcBbfOIpInMonBbfDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfDropCount.setUnits("frames")
_NtcBbfOIpInMonBbfOverflowCount_Type = Counter32
_NtcBbfOIpInMonBbfOverflowCount_Object = MibTableColumn
ntcBbfOIpInMonBbfOverflowCount = _NtcBbfOIpInMonBbfOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 8),
    _NtcBbfOIpInMonBbfOverflowCount_Type()
)
ntcBbfOIpInMonBbfOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfOverflowCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfOverflowCount.setUnits("frames")
_NtcBbfOIpInMonBbfInvFrameCount_Type = Counter32
_NtcBbfOIpInMonBbfInvFrameCount_Object = MibTableColumn
ntcBbfOIpInMonBbfInvFrameCount = _NtcBbfOIpInMonBbfInvFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 9),
    _NtcBbfOIpInMonBbfInvFrameCount_Type()
)
ntcBbfOIpInMonBbfInvFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInvFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInvFrameCount.setUnits("frames")
_NtcBbfOIpInMonBbfDiscontCount_Type = Counter32
_NtcBbfOIpInMonBbfDiscontCount_Object = MibTableColumn
ntcBbfOIpInMonBbfDiscontCount = _NtcBbfOIpInMonBbfDiscontCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 10),
    _NtcBbfOIpInMonBbfDiscontCount_Type()
)
ntcBbfOIpInMonBbfDiscontCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfDiscontCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfDiscontCount.setUnits("frames")
_NtcBbfOIpInMonBbfModNS_Type = Counter32
_NtcBbfOIpInMonBbfModNS_Object = MibTableColumn
ntcBbfOIpInMonBbfModNS = _NtcBbfOIpInMonBbfModNS_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 11),
    _NtcBbfOIpInMonBbfModNS_Type()
)
ntcBbfOIpInMonBbfModNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfModNS.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfModNS.setUnits("frames")
_NtcBbfOIpInMonBbfByteCorCount_Type = Counter32
_NtcBbfOIpInMonBbfByteCorCount_Object = MibTableColumn
ntcBbfOIpInMonBbfByteCorCount = _NtcBbfOIpInMonBbfByteCorCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 12),
    _NtcBbfOIpInMonBbfByteCorCount_Type()
)
ntcBbfOIpInMonBbfByteCorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfByteCorCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfByteCorCount.setUnits("bytes")
_NtcBbfOIpInMonBbfInvSignCount_Type = Counter32
_NtcBbfOIpInMonBbfInvSignCount_Object = MibTableColumn
ntcBbfOIpInMonBbfInvSignCount = _NtcBbfOIpInMonBbfInvSignCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 11, 1, 13),
    _NtcBbfOIpInMonBbfInvSignCount_Type()
)
ntcBbfOIpInMonBbfInvSignCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInvSignCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInvSignCount.setUnits("frames")
_NtcAlarmStatusTableTable_Object = MibTable
ntcAlarmStatusTableTable = _NtcAlarmStatusTableTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 12)
)
if mibBuilder.loadTexts:
    ntcAlarmStatusTableTable.setStatus("current")
_NtcAlarmStatusTableEntry_Object = MibTableRow
ntcAlarmStatusTableEntry = _NtcAlarmStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 12, 1)
)
ntcAlarmStatusTableEntry.setIndexNames(
    (0, "NEWTEC-BBFOVERIPIN-MIB", "ntcStreamInx"),
)
if mibBuilder.loadTexts:
    ntcAlarmStatusTableEntry.setStatus("current")


class _NtcStreamInx_Type(DisplayString):
    """Custom type ntcStreamInx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcStreamInx_Type.__name__ = "DisplayString"
_NtcStreamInx_Object = MibTableColumn
ntcStreamInx = _NtcStreamInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 12, 1, 1),
    _NtcStreamInx_Type()
)
ntcStreamInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcStreamInx.setStatus("current")
_NtcBbfOIpInMonBbfNoInpDataError_Type = NtcAlarmState
_NtcBbfOIpInMonBbfNoInpDataError_Object = MibTableColumn
ntcBbfOIpInMonBbfNoInpDataError = _NtcBbfOIpInMonBbfNoInpDataError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 12, 1, 2),
    _NtcBbfOIpInMonBbfNoInpDataError_Type()
)
ntcBbfOIpInMonBbfNoInpDataError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfNoInpDataError.setStatus("current")
_NtcBbfOverflowError_Type = NtcAlarmState
_NtcBbfOverflowError_Object = MibTableColumn
ntcBbfOverflowError = _NtcBbfOverflowError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 12, 1, 3),
    _NtcBbfOverflowError_Type()
)
ntcBbfOverflowError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOverflowError.setStatus("current")
_NtcBbfDiscontinuityError_Type = NtcAlarmState
_NtcBbfDiscontinuityError_Object = MibTableColumn
ntcBbfDiscontinuityError = _NtcBbfDiscontinuityError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 12, 1, 4),
    _NtcBbfDiscontinuityError_Type()
)
ntcBbfDiscontinuityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfDiscontinuityError.setStatus("current")
_NtcBbfModcodNotSupportedError_Type = NtcAlarmState
_NtcBbfModcodNotSupportedError_Object = MibTableColumn
ntcBbfModcodNotSupportedError = _NtcBbfModcodNotSupportedError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 12, 1, 5),
    _NtcBbfModcodNotSupportedError_Type()
)
ntcBbfModcodNotSupportedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfModcodNotSupportedError.setStatus("current")
_NtcBbfOIpInMonBbfByteCorCountT_Type = Counter32
_NtcBbfOIpInMonBbfByteCorCountT_Object = MibScalar
ntcBbfOIpInMonBbfByteCorCountT = _NtcBbfOIpInMonBbfByteCorCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 13),
    _NtcBbfOIpInMonBbfByteCorCountT_Type()
)
ntcBbfOIpInMonBbfByteCorCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfByteCorCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfByteCorCountT.setUnits("bytes")
_NtcBbfOIpInMonBbfInvSignCountT_Type = Counter32
_NtcBbfOIpInMonBbfInvSignCountT_Object = MibScalar
ntcBbfOIpInMonBbfInvSignCountT = _NtcBbfOIpInMonBbfInvSignCountT_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 4, 14),
    _NtcBbfOIpInMonBbfInvSignCountT_Type()
)
ntcBbfOIpInMonBbfInvSignCountT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInvSignCountT.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpInMonBbfInvSignCountT.setUnits("frames")
_NtcBbfOIpInAlarm_ObjectIdentity = ObjectIdentity
ntcBbfOIpInAlarm = _NtcBbfOIpInAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 5)
)
if mibBuilder.loadTexts:
    ntcBbfOIpInAlarm.setStatus("current")
_NtcBbfOIpInAlmGeneralBbfOverIpIn_Type = NtcAlarmState
_NtcBbfOIpInAlmGeneralBbfOverIpIn_Object = MibScalar
ntcBbfOIpInAlmGeneralBbfOverIpIn = _NtcBbfOIpInAlmGeneralBbfOverIpIn_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 5, 1),
    _NtcBbfOIpInAlmGeneralBbfOverIpIn_Type()
)
ntcBbfOIpInAlmGeneralBbfOverIpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInAlmGeneralBbfOverIpIn.setStatus("current")
_NtcBbfOIpInAlmNoInputData_Type = NtcAlarmState
_NtcBbfOIpInAlmNoInputData_Object = MibScalar
ntcBbfOIpInAlmNoInputData = _NtcBbfOIpInAlmNoInputData_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 5, 2),
    _NtcBbfOIpInAlmNoInputData_Type()
)
ntcBbfOIpInAlmNoInputData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInAlmNoInputData.setStatus("current")
_NtcBbfOIpInAlmBufferOverflow_Type = NtcAlarmState
_NtcBbfOIpInAlmBufferOverflow_Object = MibScalar
ntcBbfOIpInAlmBufferOverflow = _NtcBbfOIpInAlmBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 5, 3),
    _NtcBbfOIpInAlmBufferOverflow_Type()
)
ntcBbfOIpInAlmBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInAlmBufferOverflow.setStatus("current")
_NtcBbfOIpInAlBbfOverIPDiscont_Type = NtcAlarmState
_NtcBbfOIpInAlBbfOverIPDiscont_Object = MibScalar
ntcBbfOIpInAlBbfOverIPDiscont = _NtcBbfOIpInAlBbfOverIPDiscont_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 5, 4),
    _NtcBbfOIpInAlBbfOverIPDiscont_Type()
)
ntcBbfOIpInAlBbfOverIPDiscont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInAlBbfOverIPDiscont.setStatus("current")
_NtcBbfOIpInAlBbfOverIPModNS_Type = NtcAlarmState
_NtcBbfOIpInAlBbfOverIPModNS_Object = MibScalar
ntcBbfOIpInAlBbfOverIPModNS = _NtcBbfOIpInAlBbfOverIPModNS_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 1, 5, 5),
    _NtcBbfOIpInAlBbfOverIPModNS_Type()
)
ntcBbfOIpInAlBbfOverIPModNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpInAlBbfOverIPModNS.setStatus("current")
_NtcBbfOIpInConformance_ObjectIdentity = ObjectIdentity
ntcBbfOIpInConformance = _NtcBbfOIpInConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 2)
)
if mibBuilder.loadTexts:
    ntcBbfOIpInConformance.setStatus("current")
_NtcBbfOIpInConfCompliance_ObjectIdentity = ObjectIdentity
ntcBbfOIpInConfCompliance = _NtcBbfOIpInConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 2, 1)
)
if mibBuilder.loadTexts:
    ntcBbfOIpInConfCompliance.setStatus("current")
_NtcBbfOIpInConfGroup_ObjectIdentity = ObjectIdentity
ntcBbfOIpInConfGroup = _NtcBbfOIpInConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 2, 2)
)
if mibBuilder.loadTexts:
    ntcBbfOIpInConfGroup.setStatus("current")

# Managed Objects groups

ntcBbfOIpInConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 2, 2, 1)
)
ntcBbfOIpInConfGrpV1Standard.setObjects(
      *(("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInEnable"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInInputSelection"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcConfigurationTableRowStatus"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInEpEnable"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInIpEpAddressType"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInEpMulticastAddress"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInEpIpUdpPort"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInEpBbfType"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInEpSourceRedundancy"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonCounterReset"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfInputBitRateT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfInCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfOutCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfDropCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfOverflowCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfByteOutCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfInvFrameCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfDiscontCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfModcodNSCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfInputBitRate"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonSourceAddress"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfInCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfOutCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfByteOutCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfDropCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfOverflowCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfInvFrameCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfDiscontCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfModNS"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfByteCorCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfInvSignCount"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfNoInpDataError"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOverflowError"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfDiscontinuityError"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfModcodNotSupportedError"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfByteCorCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInMonBbfInvSignCountT"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInAlmGeneralBbfOverIpIn"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInAlmNoInputData"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInAlmBufferOverflow"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInAlBbfOverIPDiscont"),
        ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInAlBbfOverIPModNS"))
)
if mibBuilder.loadTexts:
    ntcBbfOIpInConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcBbfOIpInConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1200, 2, 1, 1)
)
ntcBbfOIpInConfCompV1Standard.setObjects(
    ("NEWTEC-BBFOVERIPIN-MIB", "ntcBbfOIpInConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcBbfOIpInConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-BBFOVERIPIN-MIB",
    **{"ntcBbfOverIpIn": ntcBbfOverIpIn,
       "ntcBbfOIpInObjects": ntcBbfOIpInObjects,
       "ntcBbfOIpInEnable": ntcBbfOIpInEnable,
       "ntcBbfOIpInInputSelection": ntcBbfOIpInInputSelection,
       "ntcConfigurationTableTable": ntcConfigurationTableTable,
       "ntcConfigurationTableEntry": ntcConfigurationTableEntry,
       "ntcConfigurationTableName": ntcConfigurationTableName,
       "ntcConfigurationTableRowStatus": ntcConfigurationTableRowStatus,
       "ntcBbfOIpInEpEnable": ntcBbfOIpInEpEnable,
       "ntcBbfOIpInIpEpAddressType": ntcBbfOIpInIpEpAddressType,
       "ntcBbfOIpInEpMulticastAddress": ntcBbfOIpInEpMulticastAddress,
       "ntcBbfOIpInEpIpUdpPort": ntcBbfOIpInEpIpUdpPort,
       "ntcBbfOIpInEpBbfType": ntcBbfOIpInEpBbfType,
       "ntcBbfOIpInEpSourceRedundancy": ntcBbfOIpInEpSourceRedundancy,
       "ntcBbfOIpInMonitor": ntcBbfOIpInMonitor,
       "ntcBbfOIpInMonCounterReset": ntcBbfOIpInMonCounterReset,
       "ntcBbfOIpInMonBbfInputBitRateT": ntcBbfOIpInMonBbfInputBitRateT,
       "ntcBbfOIpInMonBbfInCountT": ntcBbfOIpInMonBbfInCountT,
       "ntcBbfOIpInMonBbfOutCountT": ntcBbfOIpInMonBbfOutCountT,
       "ntcBbfOIpInMonBbfDropCountT": ntcBbfOIpInMonBbfDropCountT,
       "ntcBbfOIpInMonBbfOverflowCountT": ntcBbfOIpInMonBbfOverflowCountT,
       "ntcBbfOIpInMonBbfByteOutCountT": ntcBbfOIpInMonBbfByteOutCountT,
       "ntcBbfOIpInMonBbfInvFrameCountT": ntcBbfOIpInMonBbfInvFrameCountT,
       "ntcBbfOIpInMonBbfDiscontCountT": ntcBbfOIpInMonBbfDiscontCountT,
       "ntcBbfOIpInMonBbfModcodNSCountT": ntcBbfOIpInMonBbfModcodNSCountT,
       "ntcMonitoringTableTable": ntcMonitoringTableTable,
       "ntcMonitoringTableEntry": ntcMonitoringTableEntry,
       "ntcMonitoringTableName": ntcMonitoringTableName,
       "ntcBbfOIpInMonBbfInputBitRate": ntcBbfOIpInMonBbfInputBitRate,
       "ntcBbfOIpInMonSourceAddress": ntcBbfOIpInMonSourceAddress,
       "ntcBbfOIpInMonBbfInCount": ntcBbfOIpInMonBbfInCount,
       "ntcBbfOIpInMonBbfOutCount": ntcBbfOIpInMonBbfOutCount,
       "ntcBbfOIpInMonBbfByteOutCount": ntcBbfOIpInMonBbfByteOutCount,
       "ntcBbfOIpInMonBbfDropCount": ntcBbfOIpInMonBbfDropCount,
       "ntcBbfOIpInMonBbfOverflowCount": ntcBbfOIpInMonBbfOverflowCount,
       "ntcBbfOIpInMonBbfInvFrameCount": ntcBbfOIpInMonBbfInvFrameCount,
       "ntcBbfOIpInMonBbfDiscontCount": ntcBbfOIpInMonBbfDiscontCount,
       "ntcBbfOIpInMonBbfModNS": ntcBbfOIpInMonBbfModNS,
       "ntcBbfOIpInMonBbfByteCorCount": ntcBbfOIpInMonBbfByteCorCount,
       "ntcBbfOIpInMonBbfInvSignCount": ntcBbfOIpInMonBbfInvSignCount,
       "ntcAlarmStatusTableTable": ntcAlarmStatusTableTable,
       "ntcAlarmStatusTableEntry": ntcAlarmStatusTableEntry,
       "ntcStreamInx": ntcStreamInx,
       "ntcBbfOIpInMonBbfNoInpDataError": ntcBbfOIpInMonBbfNoInpDataError,
       "ntcBbfOverflowError": ntcBbfOverflowError,
       "ntcBbfDiscontinuityError": ntcBbfDiscontinuityError,
       "ntcBbfModcodNotSupportedError": ntcBbfModcodNotSupportedError,
       "ntcBbfOIpInMonBbfByteCorCountT": ntcBbfOIpInMonBbfByteCorCountT,
       "ntcBbfOIpInMonBbfInvSignCountT": ntcBbfOIpInMonBbfInvSignCountT,
       "ntcBbfOIpInAlarm": ntcBbfOIpInAlarm,
       "ntcBbfOIpInAlmGeneralBbfOverIpIn": ntcBbfOIpInAlmGeneralBbfOverIpIn,
       "ntcBbfOIpInAlmNoInputData": ntcBbfOIpInAlmNoInputData,
       "ntcBbfOIpInAlmBufferOverflow": ntcBbfOIpInAlmBufferOverflow,
       "ntcBbfOIpInAlBbfOverIPDiscont": ntcBbfOIpInAlBbfOverIPDiscont,
       "ntcBbfOIpInAlBbfOverIPModNS": ntcBbfOIpInAlBbfOverIPModNS,
       "ntcBbfOIpInConformance": ntcBbfOIpInConformance,
       "ntcBbfOIpInConfCompliance": ntcBbfOIpInConfCompliance,
       "ntcBbfOIpInConfCompV1Standard": ntcBbfOIpInConfCompV1Standard,
       "ntcBbfOIpInConfGroup": ntcBbfOIpInConfGroup,
       "ntcBbfOIpInConfGrpV1Standard": ntcBbfOIpInConfGrpV1Standard}
)
