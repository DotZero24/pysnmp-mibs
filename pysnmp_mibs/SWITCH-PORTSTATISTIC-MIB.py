# SNMP MIB module (SWITCH-PORTSTATISTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-PORTSTATISTIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:02 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rcPortStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcPortStatsTrap_ObjectIdentity = ObjectIdentity
rcPortStatsTrap = _RcPortStatsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 1)
)
_RcPortStatsObject_ObjectIdentity = ObjectIdentity
rcPortStatsObject = _RcPortStatsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2)
)
_RcPortStatsScalar_ObjectIdentity = ObjectIdentity
rcPortStatsScalar = _RcPortStatsScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 1)
)


class _RcPortStatsPeriod_Type(Integer32):
    """Custom type rcPortStatsPeriod based on Integer32"""
    defaultValue = 2000


_RcPortStatsPeriod_Type.__name__ = "Integer32"
_RcPortStatsPeriod_Object = MibScalar
rcPortStatsPeriod = _RcPortStatsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 1, 1),
    _RcPortStatsPeriod_Type()
)
rcPortStatsPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStatsPeriod.setStatus("current")
_RcPortStatsTable_Object = MibTable
rcPortStatsTable = _RcPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    rcPortStatsTable.setStatus("current")
_RcPortStatsEntry_Object = MibTableRow
rcPortStatsEntry = _RcPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 2, 1)
)
rcPortStatsEntry.setIndexNames(
    (0, "SWITCH-PORTSTATISTIC-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rcPortStatsEntry.setStatus("current")
_RcPortStatsEnable_Type = TruthValue
_RcPortStatsEnable_Object = MibTableColumn
rcPortStatsEnable = _RcPortStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 2, 1, 1),
    _RcPortStatsEnable_Type()
)
rcPortStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStatsEnable.setStatus("current")
_RcPortStatsHistoryPortStatsNextIndex_Type = Integer32
_RcPortStatsHistoryPortStatsNextIndex_Object = MibTableColumn
rcPortStatsHistoryPortStatsNextIndex = _RcPortStatsHistoryPortStatsNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 2, 1, 2),
    _RcPortStatsHistoryPortStatsNextIndex_Type()
)
rcPortStatsHistoryPortStatsNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortStatsHistoryPortStatsNextIndex.setStatus("current")
_RcPortStatsClear_Type = TruthValue
_RcPortStatsClear_Object = MibTableColumn
rcPortStatsClear = _RcPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 2, 1, 3),
    _RcPortStatsClear_Type()
)
rcPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStatsClear.setStatus("current")
_RcCurrentPortStatsTable_Object = MibTable
rcCurrentPortStatsTable = _RcCurrentPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    rcCurrentPortStatsTable.setStatus("current")
_RcCurrentPortStatsEntry_Object = MibTableRow
rcCurrentPortStatsEntry = _RcCurrentPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 3, 1)
)
rcCurrentPortStatsEntry.setIndexNames(
    (0, "SWITCH-PORTSTATISTIC-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rcCurrentPortStatsEntry.setStatus("current")
_RcCurrentPortStatsInPacket_Type = Counter64
_RcCurrentPortStatsInPacket_Object = MibTableColumn
rcCurrentPortStatsInPacket = _RcCurrentPortStatsInPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 3, 1, 1),
    _RcCurrentPortStatsInPacket_Type()
)
rcCurrentPortStatsInPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurrentPortStatsInPacket.setStatus("current")
_RcCurrentPortStatsOutPacket_Type = Counter64
_RcCurrentPortStatsOutPacket_Object = MibTableColumn
rcCurrentPortStatsOutPacket = _RcCurrentPortStatsOutPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 3, 1, 2),
    _RcCurrentPortStatsOutPacket_Type()
)
rcCurrentPortStatsOutPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurrentPortStatsOutPacket.setStatus("current")
_RcCurrentPortStatsInAllBits_Type = Counter64
_RcCurrentPortStatsInAllBits_Object = MibTableColumn
rcCurrentPortStatsInAllBits = _RcCurrentPortStatsInAllBits_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 3, 1, 3),
    _RcCurrentPortStatsInAllBits_Type()
)
rcCurrentPortStatsInAllBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurrentPortStatsInAllBits.setStatus("current")
_RcCurrentPortStatsOutAllBits_Type = Counter64
_RcCurrentPortStatsOutAllBits_Object = MibTableColumn
rcCurrentPortStatsOutAllBits = _RcCurrentPortStatsOutAllBits_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 3, 1, 4),
    _RcCurrentPortStatsOutAllBits_Type()
)
rcCurrentPortStatsOutAllBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurrentPortStatsOutAllBits.setStatus("current")
_RcCurrentPortStatsInBandwidthUtilization_Type = Integer32
_RcCurrentPortStatsInBandwidthUtilization_Object = MibTableColumn
rcCurrentPortStatsInBandwidthUtilization = _RcCurrentPortStatsInBandwidthUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 3, 1, 5),
    _RcCurrentPortStatsInBandwidthUtilization_Type()
)
rcCurrentPortStatsInBandwidthUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurrentPortStatsInBandwidthUtilization.setStatus("current")
_RcCurrentPortStatsEBandwidthUtilization_Type = Integer32
_RcCurrentPortStatsEBandwidthUtilization_Object = MibTableColumn
rcCurrentPortStatsEBandwidthUtilization = _RcCurrentPortStatsEBandwidthUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 3, 1, 6),
    _RcCurrentPortStatsEBandwidthUtilization_Type()
)
rcCurrentPortStatsEBandwidthUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurrentPortStatsEBandwidthUtilization.setStatus("current")
_RcHistoryPortStatsTable_Object = MibTable
rcHistoryPortStatsTable = _RcHistoryPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4)
)
if mibBuilder.loadTexts:
    rcHistoryPortStatsTable.setStatus("current")
_RcHistoryPortStatsEntry_Object = MibTableRow
rcHistoryPortStatsEntry = _RcHistoryPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4, 1)
)
rcHistoryPortStatsEntry.setIndexNames(
    (0, "SWITCH-PORTSTATISTIC-MIB", "ifIndex"),
    (0, "SWITCH-PORTSTATISTIC-MIB", "rcHistoryStatsIndex"),
)
if mibBuilder.loadTexts:
    rcHistoryPortStatsEntry.setStatus("current")
_RcHistoryPortStatsIndex_Type = Integer32
_RcHistoryPortStatsIndex_Object = MibTableColumn
rcHistoryPortStatsIndex = _RcHistoryPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4, 1, 1),
    _RcHistoryPortStatsIndex_Type()
)
rcHistoryPortStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcHistoryPortStatsIndex.setStatus("current")
_RcHistoryPortStatsInPacket_Type = Counter64
_RcHistoryPortStatsInPacket_Object = MibTableColumn
rcHistoryPortStatsInPacket = _RcHistoryPortStatsInPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4, 1, 2),
    _RcHistoryPortStatsInPacket_Type()
)
rcHistoryPortStatsInPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHistoryPortStatsInPacket.setStatus("current")
_RcHistoryPortStatsOutPacket_Type = Counter64
_RcHistoryPortStatsOutPacket_Object = MibTableColumn
rcHistoryPortStatsOutPacket = _RcHistoryPortStatsOutPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4, 1, 3),
    _RcHistoryPortStatsOutPacket_Type()
)
rcHistoryPortStatsOutPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHistoryPortStatsOutPacket.setStatus("current")
_RcHistoryPortStatsInAllBits_Type = Counter64
_RcHistoryPortStatsInAllBits_Object = MibTableColumn
rcHistoryPortStatsInAllBits = _RcHistoryPortStatsInAllBits_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4, 1, 4),
    _RcHistoryPortStatsInAllBits_Type()
)
rcHistoryPortStatsInAllBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHistoryPortStatsInAllBits.setStatus("current")
_RcHistoryPortStatsOutAllBits_Type = Counter64
_RcHistoryPortStatsOutAllBits_Object = MibTableColumn
rcHistoryPortStatsOutAllBits = _RcHistoryPortStatsOutAllBits_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4, 1, 5),
    _RcHistoryPortStatsOutAllBits_Type()
)
rcHistoryPortStatsOutAllBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHistoryPortStatsOutAllBits.setStatus("current")
_RcHistoryPortStatsInBandwidthUtilization_Type = Integer32
_RcHistoryPortStatsInBandwidthUtilization_Object = MibTableColumn
rcHistoryPortStatsInBandwidthUtilization = _RcHistoryPortStatsInBandwidthUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4, 1, 6),
    _RcHistoryPortStatsInBandwidthUtilization_Type()
)
rcHistoryPortStatsInBandwidthUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHistoryPortStatsInBandwidthUtilization.setStatus("current")
_RcHistoryPortStatsEBandwidthUtilization_Type = Integer32
_RcHistoryPortStatsEBandwidthUtilization_Object = MibTableColumn
rcHistoryPortStatsEBandwidthUtilization = _RcHistoryPortStatsEBandwidthUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 2, 4, 1, 7),
    _RcHistoryPortStatsEBandwidthUtilization_Type()
)
rcHistoryPortStatsEBandwidthUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHistoryPortStatsEBandwidthUtilization.setStatus("current")
_RcPortStatsConformance_ObjectIdentity = ObjectIdentity
rcPortStatsConformance = _RcPortStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 7, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-PORTSTATISTIC-MIB",
    **{"rcPortStatistics": rcPortStatistics,
       "rcPortStatsTrap": rcPortStatsTrap,
       "rcPortStatsObject": rcPortStatsObject,
       "rcPortStatsScalar": rcPortStatsScalar,
       "rcPortStatsPeriod": rcPortStatsPeriod,
       "rcPortStatsTable": rcPortStatsTable,
       "rcPortStatsEntry": rcPortStatsEntry,
       "rcPortStatsEnable": rcPortStatsEnable,
       "rcPortStatsHistoryPortStatsNextIndex": rcPortStatsHistoryPortStatsNextIndex,
       "rcPortStatsClear": rcPortStatsClear,
       "rcCurrentPortStatsTable": rcCurrentPortStatsTable,
       "rcCurrentPortStatsEntry": rcCurrentPortStatsEntry,
       "rcCurrentPortStatsInPacket": rcCurrentPortStatsInPacket,
       "rcCurrentPortStatsOutPacket": rcCurrentPortStatsOutPacket,
       "rcCurrentPortStatsInAllBits": rcCurrentPortStatsInAllBits,
       "rcCurrentPortStatsOutAllBits": rcCurrentPortStatsOutAllBits,
       "rcCurrentPortStatsInBandwidthUtilization": rcCurrentPortStatsInBandwidthUtilization,
       "rcCurrentPortStatsEBandwidthUtilization": rcCurrentPortStatsEBandwidthUtilization,
       "rcHistoryPortStatsTable": rcHistoryPortStatsTable,
       "rcHistoryPortStatsEntry": rcHistoryPortStatsEntry,
       "rcHistoryPortStatsIndex": rcHistoryPortStatsIndex,
       "rcHistoryPortStatsInPacket": rcHistoryPortStatsInPacket,
       "rcHistoryPortStatsOutPacket": rcHistoryPortStatsOutPacket,
       "rcHistoryPortStatsInAllBits": rcHistoryPortStatsInAllBits,
       "rcHistoryPortStatsOutAllBits": rcHistoryPortStatsOutAllBits,
       "rcHistoryPortStatsInBandwidthUtilization": rcHistoryPortStatsInBandwidthUtilization,
       "rcHistoryPortStatsEBandwidthUtilization": rcHistoryPortStatsEBandwidthUtilization,
       "rcPortStatsConformance": rcPortStatsConformance}
)
