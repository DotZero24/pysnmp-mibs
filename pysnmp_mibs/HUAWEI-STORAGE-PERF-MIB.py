# SNMP MIB module (HUAWEI-STORAGE-PERF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-STORAGE-PERF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:29:48 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251)
)
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21)
)
_HwPerfDiskTable_Object = MibTable
hwPerfDiskTable = _HwPerfDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10)
)
if mibBuilder.loadTexts:
    hwPerfDiskTable.setStatus("current")
_HwPerfDiskEntry_Object = MibTableRow
hwPerfDiskEntry = _HwPerfDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1)
)
hwPerfDiskEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-PERF-MIB", "hwPerfDiskIndex"),
)
if mibBuilder.loadTexts:
    hwPerfDiskEntry.setStatus("current")
_HwPerfDiskIndex_Type = OctetString
_HwPerfDiskIndex_Object = MibTableColumn
hwPerfDiskIndex = _HwPerfDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 1),
    _HwPerfDiskIndex_Type()
)
hwPerfDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskIndex.setStatus("current")
_HwPerfDiskTotalIOPS_Type = Unsigned32
_HwPerfDiskTotalIOPS_Object = MibTableColumn
hwPerfDiskTotalIOPS = _HwPerfDiskTotalIOPS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 2),
    _HwPerfDiskTotalIOPS_Type()
)
hwPerfDiskTotalIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskTotalIOPS.setStatus("current")
_HwPerfDiskReadIOPS_Type = Unsigned32
_HwPerfDiskReadIOPS_Object = MibTableColumn
hwPerfDiskReadIOPS = _HwPerfDiskReadIOPS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 3),
    _HwPerfDiskReadIOPS_Type()
)
hwPerfDiskReadIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskReadIOPS.setStatus("current")
_HwPerfDiskWriteIOPS_Type = Unsigned32
_HwPerfDiskWriteIOPS_Object = MibTableColumn
hwPerfDiskWriteIOPS = _HwPerfDiskWriteIOPS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 4),
    _HwPerfDiskWriteIOPS_Type()
)
hwPerfDiskWriteIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskWriteIOPS.setStatus("current")
_HwPerfDiskTotalTraffic_Type = Counter64
_HwPerfDiskTotalTraffic_Object = MibTableColumn
hwPerfDiskTotalTraffic = _HwPerfDiskTotalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 5),
    _HwPerfDiskTotalTraffic_Type()
)
hwPerfDiskTotalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskTotalTraffic.setStatus("current")
_HwPerfDiskReadTraffic_Type = Counter64
_HwPerfDiskReadTraffic_Object = MibTableColumn
hwPerfDiskReadTraffic = _HwPerfDiskReadTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 6),
    _HwPerfDiskReadTraffic_Type()
)
hwPerfDiskReadTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskReadTraffic.setStatus("current")
_HwPerfDiskWriteTraffic_Type = Counter64
_HwPerfDiskWriteTraffic_Object = MibTableColumn
hwPerfDiskWriteTraffic = _HwPerfDiskWriteTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 7),
    _HwPerfDiskWriteTraffic_Type()
)
hwPerfDiskWriteTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskWriteTraffic.setStatus("current")
_HwPerfDiskDelay_Type = Counter64
_HwPerfDiskDelay_Object = MibTableColumn
hwPerfDiskDelay = _HwPerfDiskDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 8),
    _HwPerfDiskDelay_Type()
)
hwPerfDiskDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskDelay.setStatus("current")
_HwPerfDiskLengthOfQueue_Type = Unsigned32
_HwPerfDiskLengthOfQueue_Object = MibTableColumn
hwPerfDiskLengthOfQueue = _HwPerfDiskLengthOfQueue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 9),
    _HwPerfDiskLengthOfQueue_Type()
)
hwPerfDiskLengthOfQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskLengthOfQueue.setStatus("current")
_HwPerfDiskAverageIO_Type = Unsigned32
_HwPerfDiskAverageIO_Object = MibTableColumn
hwPerfDiskAverageIO = _HwPerfDiskAverageIO_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 11),
    _HwPerfDiskAverageIO_Type()
)
hwPerfDiskAverageIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPerfDiskAverageIO.setStatus("current")
_HwPerfDiskAverageReadIO_Type = Unsigned32
_HwPerfDiskAverageReadIO_Object = MibTableColumn
hwPerfDiskAverageReadIO = _HwPerfDiskAverageReadIO_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 12),
    _HwPerfDiskAverageReadIO_Type()
)
hwPerfDiskAverageReadIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskAverageReadIO.setStatus("current")
_HwPerfDiskAverageWriteIO_Type = Unsigned32
_HwPerfDiskAverageWriteIO_Object = MibTableColumn
hwPerfDiskAverageWriteIO = _HwPerfDiskAverageWriteIO_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 13),
    _HwPerfDiskAverageWriteIO_Type()
)
hwPerfDiskAverageWriteIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskAverageWriteIO.setStatus("current")
_HwPerfDiskMaxIOPS_Type = Unsigned32
_HwPerfDiskMaxIOPS_Object = MibTableColumn
hwPerfDiskMaxIOPS = _HwPerfDiskMaxIOPS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 21, 10, 1, 14),
    _HwPerfDiskMaxIOPS_Type()
)
hwPerfDiskMaxIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfDiskMaxIOPS.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-STORAGE-PERF-MIB",
    **{"huawei": huawei,
       "products": products,
       "storage": storage,
       "performance": performance,
       "hwPerfDiskTable": hwPerfDiskTable,
       "hwPerfDiskEntry": hwPerfDiskEntry,
       "hwPerfDiskIndex": hwPerfDiskIndex,
       "hwPerfDiskTotalIOPS": hwPerfDiskTotalIOPS,
       "hwPerfDiskReadIOPS": hwPerfDiskReadIOPS,
       "hwPerfDiskWriteIOPS": hwPerfDiskWriteIOPS,
       "hwPerfDiskTotalTraffic": hwPerfDiskTotalTraffic,
       "hwPerfDiskReadTraffic": hwPerfDiskReadTraffic,
       "hwPerfDiskWriteTraffic": hwPerfDiskWriteTraffic,
       "hwPerfDiskDelay": hwPerfDiskDelay,
       "hwPerfDiskLengthOfQueue": hwPerfDiskLengthOfQueue,
       "hwPerfDiskAverageIO": hwPerfDiskAverageIO,
       "hwPerfDiskAverageReadIO": hwPerfDiskAverageReadIO,
       "hwPerfDiskAverageWriteIO": hwPerfDiskAverageWriteIO,
       "hwPerfDiskMaxIOPS": hwPerfDiskMaxIOPS}
)
