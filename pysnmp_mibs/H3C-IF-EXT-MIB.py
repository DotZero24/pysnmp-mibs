# SNMP MIB module (H3C-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-IF-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:58 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

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

h3cIfExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40)
)
if mibBuilder.loadTexts:
    h3cIfExt.setRevisions(
        ("2018-02-07 00:00",
         "2018-01-09 00:00",
         "2017-12-13 18:20",
         "2017-07-13 10:40",
         "2016-12-05 18:00",
         "2016-07-01 17:00",
         "2015-12-10 10:00",
         "2015-04-02 04:58",
         "2014-11-20 08:00",
         "2009-05-06 19:36",
         "2004-11-13 19:36")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cIfExtScalarGroup_ObjectIdentity = ObjectIdentity
h3cIfExtScalarGroup = _H3cIfExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1)
)
_H3cIfStatGlobalFlowInterval_Type = Integer32
_H3cIfStatGlobalFlowInterval_Object = MibScalar
h3cIfStatGlobalFlowInterval = _H3cIfStatGlobalFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1, 1),
    _H3cIfStatGlobalFlowInterval_Type()
)
h3cIfStatGlobalFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfStatGlobalFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cIfStatGlobalFlowInterval.setUnits("seconds")
_H3cIfShutDownInterval_Type = Integer32
_H3cIfShutDownInterval_Object = MibScalar
h3cIfShutDownInterval = _H3cIfShutDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1, 2),
    _H3cIfShutDownInterval_Type()
)
h3cIfShutDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfShutDownInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cIfShutDownInterval.setUnits("seconds")
_H3cIfThroughputInKbps_Type = CounterBasedGauge64
_H3cIfThroughputInKbps_Object = MibScalar
h3cIfThroughputInKbps = _H3cIfThroughputInKbps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1, 3),
    _H3cIfThroughputInKbps_Type()
)
h3cIfThroughputInKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfThroughputInKbps.setStatus("current")
_H3cIfThroughputOutKbps_Type = CounterBasedGauge64
_H3cIfThroughputOutKbps_Object = MibScalar
h3cIfThroughputOutKbps = _H3cIfThroughputOutKbps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1, 4),
    _H3cIfThroughputOutKbps_Type()
)
h3cIfThroughputOutKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfThroughputOutKbps.setStatus("current")
_H3cIfExtGroup_ObjectIdentity = ObjectIdentity
h3cIfExtGroup = _H3cIfExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2)
)
_H3cIfStat_ObjectIdentity = ObjectIdentity
h3cIfStat = _H3cIfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1)
)
_H3cIfStatScalarGroup_ObjectIdentity = ObjectIdentity
h3cIfStatScalarGroup = _H3cIfStatScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 1)
)
_H3cIfStatTable_ObjectIdentity = ObjectIdentity
h3cIfStatTable = _H3cIfStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2)
)
_H3cIfFlowStatTable_Object = MibTable
h3cIfFlowStatTable = _H3cIfFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfFlowStatTable.setStatus("current")
_H3cIfStatEntry_Object = MibTableRow
h3cIfStatEntry = _H3cIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1)
)
h3cIfStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfStatEntry.setStatus("current")
_H3cIfStatFlowInterval_Type = Integer32
_H3cIfStatFlowInterval_Object = MibTableColumn
h3cIfStatFlowInterval = _H3cIfStatFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 1),
    _H3cIfStatFlowInterval_Type()
)
h3cIfStatFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfStatFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cIfStatFlowInterval.setUnits("seconds")
_H3cIfStatFlowInBits_Type = Unsigned32
_H3cIfStatFlowInBits_Object = MibTableColumn
h3cIfStatFlowInBits = _H3cIfStatFlowInBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 2),
    _H3cIfStatFlowInBits_Type()
)
h3cIfStatFlowInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowInBits.setStatus("current")
_H3cIfStatFlowOutBits_Type = Unsigned32
_H3cIfStatFlowOutBits_Object = MibTableColumn
h3cIfStatFlowOutBits = _H3cIfStatFlowOutBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 3),
    _H3cIfStatFlowOutBits_Type()
)
h3cIfStatFlowOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowOutBits.setStatus("current")
_H3cIfStatFlowInPkts_Type = Unsigned32
_H3cIfStatFlowInPkts_Object = MibTableColumn
h3cIfStatFlowInPkts = _H3cIfStatFlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 4),
    _H3cIfStatFlowInPkts_Type()
)
h3cIfStatFlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowInPkts.setStatus("current")
_H3cIfStatFlowOutPkts_Type = Unsigned32
_H3cIfStatFlowOutPkts_Object = MibTableColumn
h3cIfStatFlowOutPkts = _H3cIfStatFlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 5),
    _H3cIfStatFlowOutPkts_Type()
)
h3cIfStatFlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowOutPkts.setStatus("current")
_H3cIfStatFlowInBytes_Type = Unsigned32
_H3cIfStatFlowInBytes_Object = MibTableColumn
h3cIfStatFlowInBytes = _H3cIfStatFlowInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 6),
    _H3cIfStatFlowInBytes_Type()
)
h3cIfStatFlowInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowInBytes.setStatus("current")
_H3cIfStatFlowOutBytes_Type = Unsigned32
_H3cIfStatFlowOutBytes_Object = MibTableColumn
h3cIfStatFlowOutBytes = _H3cIfStatFlowOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 7),
    _H3cIfStatFlowOutBytes_Type()
)
h3cIfStatFlowOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowOutBytes.setStatus("current")
_H3cIfSpeedStatTable_Object = MibTable
h3cIfSpeedStatTable = _H3cIfSpeedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cIfSpeedStatTable.setStatus("current")
_H3cIfSpeedStatEntry_Object = MibTableRow
h3cIfSpeedStatEntry = _H3cIfSpeedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1)
)
h3cIfSpeedStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfSpeedStatEntry.setStatus("current")
_H3cIfSpeedStatInterval_Type = Integer32
_H3cIfSpeedStatInterval_Object = MibTableColumn
h3cIfSpeedStatInterval = _H3cIfSpeedStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 1),
    _H3cIfSpeedStatInterval_Type()
)
h3cIfSpeedStatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfSpeedStatInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cIfSpeedStatInterval.setUnits("seconds")
_H3cIfSpeedStatInPkts_Type = Unsigned32
_H3cIfSpeedStatInPkts_Object = MibTableColumn
h3cIfSpeedStatInPkts = _H3cIfSpeedStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 2),
    _H3cIfSpeedStatInPkts_Type()
)
h3cIfSpeedStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatInPkts.setStatus("current")
_H3cIfSpeedStatOutPkts_Type = Unsigned32
_H3cIfSpeedStatOutPkts_Object = MibTableColumn
h3cIfSpeedStatOutPkts = _H3cIfSpeedStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 3),
    _H3cIfSpeedStatOutPkts_Type()
)
h3cIfSpeedStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatOutPkts.setStatus("current")
_H3cIfSpeedStatInBytes_Type = Unsigned32
_H3cIfSpeedStatInBytes_Object = MibTableColumn
h3cIfSpeedStatInBytes = _H3cIfSpeedStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 4),
    _H3cIfSpeedStatInBytes_Type()
)
h3cIfSpeedStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatInBytes.setStatus("current")
_H3cIfSpeedStatOutBytes_Type = Unsigned32
_H3cIfSpeedStatOutBytes_Object = MibTableColumn
h3cIfSpeedStatOutBytes = _H3cIfSpeedStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 5),
    _H3cIfSpeedStatOutBytes_Type()
)
h3cIfSpeedStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatOutBytes.setStatus("current")
_H3cIfHCFlowStatTable_Object = MibTable
h3cIfHCFlowStatTable = _H3cIfHCFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cIfHCFlowStatTable.setStatus("current")
_H3cIfHCFlowStatEntry_Object = MibTableRow
h3cIfHCFlowStatEntry = _H3cIfHCFlowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 3, 1)
)
h3cIfHCFlowStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfHCFlowStatEntry.setStatus("current")
_H3cIfStatFlowHCInBits_Type = CounterBasedGauge64
_H3cIfStatFlowHCInBits_Object = MibTableColumn
h3cIfStatFlowHCInBits = _H3cIfStatFlowHCInBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 3, 1, 1),
    _H3cIfStatFlowHCInBits_Type()
)
h3cIfStatFlowHCInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowHCInBits.setStatus("current")
_H3cIfStatFlowHCOutBits_Type = CounterBasedGauge64
_H3cIfStatFlowHCOutBits_Object = MibTableColumn
h3cIfStatFlowHCOutBits = _H3cIfStatFlowHCOutBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 3, 1, 2),
    _H3cIfStatFlowHCOutBits_Type()
)
h3cIfStatFlowHCOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowHCOutBits.setStatus("current")
_H3cIfStatFlowHCInPkts_Type = CounterBasedGauge64
_H3cIfStatFlowHCInPkts_Object = MibTableColumn
h3cIfStatFlowHCInPkts = _H3cIfStatFlowHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 3, 1, 3),
    _H3cIfStatFlowHCInPkts_Type()
)
h3cIfStatFlowHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowHCInPkts.setStatus("current")
_H3cIfStatFlowHCOutPkts_Type = CounterBasedGauge64
_H3cIfStatFlowHCOutPkts_Object = MibTableColumn
h3cIfStatFlowHCOutPkts = _H3cIfStatFlowHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 3, 1, 4),
    _H3cIfStatFlowHCOutPkts_Type()
)
h3cIfStatFlowHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowHCOutPkts.setStatus("current")
_H3cIfStatFlowHCInBytes_Type = CounterBasedGauge64
_H3cIfStatFlowHCInBytes_Object = MibTableColumn
h3cIfStatFlowHCInBytes = _H3cIfStatFlowHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 3, 1, 5),
    _H3cIfStatFlowHCInBytes_Type()
)
h3cIfStatFlowHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowHCInBytes.setStatus("current")
_H3cIfStatFlowHCOutBytes_Type = CounterBasedGauge64
_H3cIfStatFlowHCOutBytes_Object = MibTableColumn
h3cIfStatFlowHCOutBytes = _H3cIfStatFlowHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 3, 1, 6),
    _H3cIfStatFlowHCOutBytes_Type()
)
h3cIfStatFlowHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowHCOutBytes.setStatus("current")
_H3cIfHCSpeedStatTable_Object = MibTable
h3cIfHCSpeedStatTable = _H3cIfHCSpeedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cIfHCSpeedStatTable.setStatus("current")
_H3cIfHCSpeedStatEntry_Object = MibTableRow
h3cIfHCSpeedStatEntry = _H3cIfHCSpeedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 4, 1)
)
h3cIfHCSpeedStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfHCSpeedStatEntry.setStatus("current")
_H3cIfSpeedStatHCInPkts_Type = CounterBasedGauge64
_H3cIfSpeedStatHCInPkts_Object = MibTableColumn
h3cIfSpeedStatHCInPkts = _H3cIfSpeedStatHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 4, 1, 1),
    _H3cIfSpeedStatHCInPkts_Type()
)
h3cIfSpeedStatHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatHCInPkts.setStatus("current")
_H3cIfSpeedStatHCOutPkts_Type = CounterBasedGauge64
_H3cIfSpeedStatHCOutPkts_Object = MibTableColumn
h3cIfSpeedStatHCOutPkts = _H3cIfSpeedStatHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 4, 1, 2),
    _H3cIfSpeedStatHCOutPkts_Type()
)
h3cIfSpeedStatHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatHCOutPkts.setStatus("current")
_H3cIfSpeedStatHCInBytes_Type = CounterBasedGauge64
_H3cIfSpeedStatHCInBytes_Object = MibTableColumn
h3cIfSpeedStatHCInBytes = _H3cIfSpeedStatHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 4, 1, 3),
    _H3cIfSpeedStatHCInBytes_Type()
)
h3cIfSpeedStatHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatHCInBytes.setStatus("current")
_H3cIfSpeedStatHCOutBytes_Type = CounterBasedGauge64
_H3cIfSpeedStatHCOutBytes_Object = MibTableColumn
h3cIfSpeedStatHCOutBytes = _H3cIfSpeedStatHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 4, 1, 4),
    _H3cIfSpeedStatHCOutBytes_Type()
)
h3cIfSpeedStatHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatHCOutBytes.setStatus("current")
_H3cIfControl_ObjectIdentity = ObjectIdentity
h3cIfControl = _H3cIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2)
)
_H3cRTParentIfTable_Object = MibTable
h3cRTParentIfTable = _H3cRTParentIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cRTParentIfTable.setStatus("current")
_H3cRTParentIfEntry_Object = MibTableRow
h3cRTParentIfEntry = _H3cRTParentIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1)
)
h3cRTParentIfEntry.setIndexNames(
    (0, "H3C-IF-EXT-MIB", "h3cRTParentIfIndex"),
)
if mibBuilder.loadTexts:
    h3cRTParentIfEntry.setStatus("current")


class _H3cRTParentIfIndex_Type(Integer32):
    """Custom type h3cRTParentIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cRTParentIfIndex_Type.__name__ = "Integer32"
_H3cRTParentIfIndex_Object = MibTableColumn
h3cRTParentIfIndex = _H3cRTParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 1),
    _H3cRTParentIfIndex_Type()
)
h3cRTParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRTParentIfIndex.setStatus("current")
_H3cRTMinSubIfOrdinal_Type = Integer32
_H3cRTMinSubIfOrdinal_Object = MibTableColumn
h3cRTMinSubIfOrdinal = _H3cRTMinSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 2),
    _H3cRTMinSubIfOrdinal_Type()
)
h3cRTMinSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRTMinSubIfOrdinal.setStatus("current")
_H3cRTMaxSubIfOrdinal_Type = Integer32
_H3cRTMaxSubIfOrdinal_Object = MibTableColumn
h3cRTMaxSubIfOrdinal = _H3cRTMaxSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 3),
    _H3cRTMaxSubIfOrdinal_Type()
)
h3cRTMaxSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRTMaxSubIfOrdinal.setStatus("current")
_H3cRTSubIfTable_Object = MibTable
h3cRTSubIfTable = _H3cRTSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2)
)
if mibBuilder.loadTexts:
    h3cRTSubIfTable.setStatus("current")
_H3cRTSubIfEntry_Object = MibTableRow
h3cRTSubIfEntry = _H3cRTSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1)
)
h3cRTSubIfEntry.setIndexNames(
    (0, "H3C-IF-EXT-MIB", "h3cRTSubIfParentIfIndex"),
    (0, "H3C-IF-EXT-MIB", "h3cRTSubIfOrdinal"),
)
if mibBuilder.loadTexts:
    h3cRTSubIfEntry.setStatus("current")


class _H3cRTSubIfParentIfIndex_Type(Integer32):
    """Custom type h3cRTSubIfParentIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cRTSubIfParentIfIndex_Type.__name__ = "Integer32"
_H3cRTSubIfParentIfIndex_Object = MibTableColumn
h3cRTSubIfParentIfIndex = _H3cRTSubIfParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 1),
    _H3cRTSubIfParentIfIndex_Type()
)
h3cRTSubIfParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRTSubIfParentIfIndex.setStatus("current")


class _H3cRTSubIfOrdinal_Type(Integer32):
    """Custom type h3cRTSubIfOrdinal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cRTSubIfOrdinal_Type.__name__ = "Integer32"
_H3cRTSubIfOrdinal_Object = MibTableColumn
h3cRTSubIfOrdinal = _H3cRTSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 2),
    _H3cRTSubIfOrdinal_Type()
)
h3cRTSubIfOrdinal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRTSubIfOrdinal.setStatus("current")
_H3cRTSubIfSubIfIndex_Type = Integer32
_H3cRTSubIfSubIfIndex_Object = MibTableColumn
h3cRTSubIfSubIfIndex = _H3cRTSubIfSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 3),
    _H3cRTSubIfSubIfIndex_Type()
)
h3cRTSubIfSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRTSubIfSubIfIndex.setStatus("current")


class _H3cRTSubIfSubIfDesc_Type(DisplayString):
    """Custom type h3cRTSubIfSubIfDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cRTSubIfSubIfDesc_Type.__name__ = "DisplayString"
_H3cRTSubIfSubIfDesc_Object = MibTableColumn
h3cRTSubIfSubIfDesc = _H3cRTSubIfSubIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 4),
    _H3cRTSubIfSubIfDesc_Type()
)
h3cRTSubIfSubIfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRTSubIfSubIfDesc.setStatus("current")
_H3cRTSubIfRowStatus_Type = RowStatus
_H3cRTSubIfRowStatus_Object = MibTableColumn
h3cRTSubIfRowStatus = _H3cRTSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 5),
    _H3cRTSubIfRowStatus_Type()
)
h3cRTSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRTSubIfRowStatus.setStatus("current")
_H3cIfLinkModeTable_Object = MibTable
h3cIfLinkModeTable = _H3cIfLinkModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3)
)
if mibBuilder.loadTexts:
    h3cIfLinkModeTable.setStatus("current")
_H3cIfLinkModeEntry_Object = MibTableRow
h3cIfLinkModeEntry = _H3cIfLinkModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1)
)
h3cIfLinkModeEntry.setIndexNames(
    (0, "H3C-IF-EXT-MIB", "h3cIfLinkModeIndex"),
)
if mibBuilder.loadTexts:
    h3cIfLinkModeEntry.setStatus("current")


class _H3cIfLinkModeIndex_Type(Integer32):
    """Custom type h3cIfLinkModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIfLinkModeIndex_Type.__name__ = "Integer32"
_H3cIfLinkModeIndex_Object = MibTableColumn
h3cIfLinkModeIndex = _H3cIfLinkModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 1),
    _H3cIfLinkModeIndex_Type()
)
h3cIfLinkModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfLinkModeIndex.setStatus("current")


class _H3cIfLinkMode_Type(Integer32):
    """Custom type h3cIfLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridgeMode", 1),
          ("routeMode", 2))
    )


_H3cIfLinkMode_Type.__name__ = "Integer32"
_H3cIfLinkMode_Object = MibTableColumn
h3cIfLinkMode = _H3cIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 2),
    _H3cIfLinkMode_Type()
)
h3cIfLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfLinkMode.setStatus("current")
_H3cIfLinkModeSwitchSupport_Type = TruthValue
_H3cIfLinkModeSwitchSupport_Object = MibTableColumn
h3cIfLinkModeSwitchSupport = _H3cIfLinkModeSwitchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 3),
    _H3cIfLinkModeSwitchSupport_Type()
)
h3cIfLinkModeSwitchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfLinkModeSwitchSupport.setStatus("current")
_H3cIfPortTypeTable_Object = MibTable
h3cIfPortTypeTable = _H3cIfPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 4)
)
if mibBuilder.loadTexts:
    h3cIfPortTypeTable.setStatus("current")
_H3cIfPortTypeEntry_Object = MibTableRow
h3cIfPortTypeEntry = _H3cIfPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 4, 1)
)
h3cIfPortTypeEntry.setIndexNames(
    (0, "H3C-IF-EXT-MIB", "h3cIfPortTypeIndex"),
)
if mibBuilder.loadTexts:
    h3cIfPortTypeEntry.setStatus("current")
_H3cIfPortTypeIndex_Type = InterfaceIndex
_H3cIfPortTypeIndex_Object = MibTableColumn
h3cIfPortTypeIndex = _H3cIfPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 4, 1, 1),
    _H3cIfPortTypeIndex_Type()
)
h3cIfPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfPortTypeIndex.setStatus("current")


class _H3cIfPortType_Type(Integer32):
    """Custom type h3cIfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ethernet", 2),
          ("fc", 3))
    )


_H3cIfPortType_Type.__name__ = "Integer32"
_H3cIfPortType_Object = MibTableColumn
h3cIfPortType = _H3cIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 4, 1, 2),
    _H3cIfPortType_Type()
)
h3cIfPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfPortType.setStatus("current")
_H3cIfPfcDot1pTable_Object = MibTable
h3cIfPfcDot1pTable = _H3cIfPfcDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 5)
)
if mibBuilder.loadTexts:
    h3cIfPfcDot1pTable.setStatus("current")
_H3cIfPfcDot1pEntry_Object = MibTableRow
h3cIfPfcDot1pEntry = _H3cIfPfcDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 5, 1)
)
h3cIfPfcDot1pEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-IF-EXT-MIB", "h3cIfPfcDot1pValue"),
)
if mibBuilder.loadTexts:
    h3cIfPfcDot1pEntry.setStatus("current")


class _H3cIfPfcDot1pValue_Type(Integer32):
    """Custom type h3cIfPfcDot1pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("pri0", 1),
          ("pri1", 2),
          ("pri2", 3),
          ("pri3", 4),
          ("pri4", 5),
          ("pri5", 6),
          ("pri6", 7),
          ("pri7", 8))
    )


_H3cIfPfcDot1pValue_Type.__name__ = "Integer32"
_H3cIfPfcDot1pValue_Object = MibTableColumn
h3cIfPfcDot1pValue = _H3cIfPfcDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 5, 1, 1),
    _H3cIfPfcDot1pValue_Type()
)
h3cIfPfcDot1pValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfPfcDot1pValue.setStatus("current")
_H3cIfPfcDot1pInPps_Type = Unsigned32
_H3cIfPfcDot1pInPps_Object = MibTableColumn
h3cIfPfcDot1pInPps = _H3cIfPfcDot1pInPps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 5, 1, 2),
    _H3cIfPfcDot1pInPps_Type()
)
h3cIfPfcDot1pInPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfPfcDot1pInPps.setStatus("current")
_H3cIfPfcDot1pOutPps_Type = Unsigned32
_H3cIfPfcDot1pOutPps_Object = MibTableColumn
h3cIfPfcDot1pOutPps = _H3cIfPfcDot1pOutPps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 5, 1, 3),
    _H3cIfPfcDot1pOutPps_Type()
)
h3cIfPfcDot1pOutPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfPfcDot1pOutPps.setStatus("current")
_H3cIfPfcDot1pInPpsThreshold_Type = Unsigned32
_H3cIfPfcDot1pInPpsThreshold_Object = MibTableColumn
h3cIfPfcDot1pInPpsThreshold = _H3cIfPfcDot1pInPpsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 5, 1, 4),
    _H3cIfPfcDot1pInPpsThreshold_Type()
)
h3cIfPfcDot1pInPpsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfPfcDot1pInPpsThreshold.setStatus("current")
_H3cIfPfcDot1pOutPpsThreshold_Type = Unsigned32
_H3cIfPfcDot1pOutPpsThreshold_Object = MibTableColumn
h3cIfPfcDot1pOutPpsThreshold = _H3cIfPfcDot1pOutPpsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 5, 1, 5),
    _H3cIfPfcDot1pOutPpsThreshold_Type()
)
h3cIfPfcDot1pOutPpsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfPfcDot1pOutPpsThreshold.setStatus("current")
_H3cIfInterfaces_ObjectIdentity = ObjectIdentity
h3cIfInterfaces = _H3cIfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3)
)
_H3cIfPhysicalNumber_Type = Integer32
_H3cIfPhysicalNumber_Object = MibScalar
h3cIfPhysicalNumber = _H3cIfPhysicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 1),
    _H3cIfPhysicalNumber_Type()
)
h3cIfPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfPhysicalNumber.setStatus("current")
_H3cIfTable_Object = MibTable
h3cIfTable = _H3cIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2)
)
if mibBuilder.loadTexts:
    h3cIfTable.setStatus("current")
_H3cIfEntry_Object = MibTableRow
h3cIfEntry = _H3cIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1)
)
h3cIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfEntry.setStatus("current")
_H3cIfUpDownTimes_Type = Integer32
_H3cIfUpDownTimes_Object = MibTableColumn
h3cIfUpDownTimes = _H3cIfUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 1),
    _H3cIfUpDownTimes_Type()
)
h3cIfUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfUpDownTimes.setStatus("current")
_H3cIfMtu_Type = Integer32
_H3cIfMtu_Object = MibTableColumn
h3cIfMtu = _H3cIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 2),
    _H3cIfMtu_Type()
)
h3cIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMtu.setStatus("current")


class _H3cIfBandwidthRate_Type(Integer32):
    """Custom type h3cIfBandwidthRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cIfBandwidthRate_Type.__name__ = "Integer32"
_H3cIfBandwidthRate_Object = MibTableColumn
h3cIfBandwidthRate = _H3cIfBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 3),
    _H3cIfBandwidthRate_Type()
)
h3cIfBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfBandwidthRate.setStatus("current")


class _H3cIfDiscardPktRate_Type(Integer32):
    """Custom type h3cIfDiscardPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cIfDiscardPktRate_Type.__name__ = "Integer32"
_H3cIfDiscardPktRate_Object = MibTableColumn
h3cIfDiscardPktRate = _H3cIfDiscardPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 4),
    _H3cIfDiscardPktRate_Type()
)
h3cIfDiscardPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfDiscardPktRate.setStatus("current")
_H3cIfStatusKeepTime_Type = TimeTicks
_H3cIfStatusKeepTime_Object = MibTableColumn
h3cIfStatusKeepTime = _H3cIfStatusKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 5),
    _H3cIfStatusKeepTime_Type()
)
h3cIfStatusKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatusKeepTime.setStatus("current")
_H3cIfInNUcastPkts_Type = Counter64
_H3cIfInNUcastPkts_Object = MibTableColumn
h3cIfInNUcastPkts = _H3cIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 6),
    _H3cIfInNUcastPkts_Type()
)
h3cIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfInNUcastPkts.setStatus("current")
_H3cIfOutNUcastPkts_Type = Counter64
_H3cIfOutNUcastPkts_Object = MibTableColumn
h3cIfOutNUcastPkts = _H3cIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 7),
    _H3cIfOutNUcastPkts_Type()
)
h3cIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfOutNUcastPkts.setStatus("current")
_H3cIfIsPoe_Type = TruthValue
_H3cIfIsPoe_Object = MibTableColumn
h3cIfIsPoe = _H3cIfIsPoe_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 8),
    _H3cIfIsPoe_Type()
)
h3cIfIsPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfIsPoe.setStatus("current")


class _H3cIfOperStatus_Type(Integer32):
    """Custom type h3cIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("admindown", 4))
    )


_H3cIfOperStatus_Type.__name__ = "Integer32"
_H3cIfOperStatus_Object = MibTableColumn
h3cIfOperStatus = _H3cIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 9),
    _H3cIfOperStatus_Type()
)
h3cIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfOperStatus.setStatus("current")
_H3cIfDownTimes_Type = Integer32
_H3cIfDownTimes_Object = MibTableColumn
h3cIfDownTimes = _H3cIfDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 10),
    _H3cIfDownTimes_Type()
)
h3cIfDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfDownTimes.setStatus("current")


class _H3cIfPfcStatus_Type(Integer32):
    """Custom type h3cIfPfcStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("auto", 3))
    )


_H3cIfPfcStatus_Type.__name__ = "Integer32"
_H3cIfPfcStatus_Object = MibTableColumn
h3cIfPfcStatus = _H3cIfPfcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 11),
    _H3cIfPfcStatus_Type()
)
h3cIfPfcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfPfcStatus.setStatus("current")


class _H3cIfPfcDot1pNoDrop_Type(Bits):
    """Custom type h3cIfPfcDot1pNoDrop based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("pri0", 0),
          ("pri1", 1),
          ("pri2", 2),
          ("pri3", 3),
          ("pri4", 4),
          ("pri5", 5),
          ("pri6", 6),
          ("pri7", 7))
    )

_H3cIfPfcDot1pNoDrop_Type.__name__ = "Bits"
_H3cIfPfcDot1pNoDrop_Object = MibTableColumn
h3cIfPfcDot1pNoDrop = _H3cIfPfcDot1pNoDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 12),
    _H3cIfPfcDot1pNoDrop_Type()
)
h3cIfPfcDot1pNoDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfPfcDot1pNoDrop.setStatus("current")


class _H3cIfDescription_Type(DisplayString):
    """Custom type h3cIfDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cIfDescription_Type.__name__ = "DisplayString"
_H3cIfDescription_Object = MibTableColumn
h3cIfDescription = _H3cIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 13),
    _H3cIfDescription_Type()
)
h3cIfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfDescription.setStatus("current")
_H3cIfFwdErrDiscards_Type = Unsigned32
_H3cIfFwdErrDiscards_Object = MibTableColumn
h3cIfFwdErrDiscards = _H3cIfFwdErrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 14),
    _H3cIfFwdErrDiscards_Type()
)
h3cIfFwdErrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfFwdErrDiscards.setStatus("current")
_H3cIfUsingTable_Object = MibTable
h3cIfUsingTable = _H3cIfUsingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 3)
)
if mibBuilder.loadTexts:
    h3cIfUsingTable.setStatus("current")
_H3cIfUsingEntry_Object = MibTableRow
h3cIfUsingEntry = _H3cIfUsingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 3, 1)
)
h3cIfUsingEntry.setIndexNames(
    (0, "H3C-IF-EXT-MIB", "h3cIfUsingIndex"),
)
if mibBuilder.loadTexts:
    h3cIfUsingEntry.setStatus("current")


class _H3cIfUsingIndex_Type(Integer32):
    """Custom type h3cIfUsingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIfUsingIndex_Type.__name__ = "Integer32"
_H3cIfUsingIndex_Object = MibTableColumn
h3cIfUsingIndex = _H3cIfUsingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 3, 1, 1),
    _H3cIfUsingIndex_Type()
)
h3cIfUsingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfUsingIndex.setStatus("current")
_H3cIfUsingSupportType_Type = Integer32
_H3cIfUsingSupportType_Object = MibTableColumn
h3cIfUsingSupportType = _H3cIfUsingSupportType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 3, 1, 2),
    _H3cIfUsingSupportType_Type()
)
h3cIfUsingSupportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfUsingSupportType.setStatus("current")


class _H3cIfUsingType_Type(Integer32):
    """Custom type h3cIfUsingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noUsing", 0),
          ("using10GE", 1),
          ("using20GE", 2),
          ("using40GE", 3),
          ("using100GE", 4),
          ("using25GE", 5),
          ("using50GE", 6))
    )


_H3cIfUsingType_Type.__name__ = "Integer32"
_H3cIfUsingType_Object = MibTableColumn
h3cIfUsingType = _H3cIfUsingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 3, 1, 3),
    _H3cIfUsingType_Type()
)
h3cIfUsingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfUsingType.setStatus("current")


class _H3cIfUsingStatus_Type(Integer32):
    """Custom type h3cIfUsingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noUsing", 0),
          ("needReboot", 1))
    )


_H3cIfUsingStatus_Type.__name__ = "Integer32"
_H3cIfUsingStatus_Object = MibTableColumn
h3cIfUsingStatus = _H3cIfUsingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 3, 1, 4),
    _H3cIfUsingStatus_Type()
)
h3cIfUsingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfUsingStatus.setStatus("current")
_H3cIfExtTrap_ObjectIdentity = ObjectIdentity
h3cIfExtTrap = _H3cIfExtTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3)
)
_H3cIfExtTrapPrex_ObjectIdentity = ObjectIdentity
h3cIfExtTrapPrex = _H3cIfExtTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0)
)
_H3cIfExtTrapObject_ObjectIdentity = ObjectIdentity
h3cIfExtTrapObject = _H3cIfExtTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1)
)
_H3cIfExtTrapCfgTable_Object = MibTable
h3cIfExtTrapCfgTable = _H3cIfExtTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfExtTrapCfgTable.setStatus("current")
_H3cIfExtTrapCfgEntry_Object = MibTableRow
h3cIfExtTrapCfgEntry = _H3cIfExtTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1)
)
h3cIfExtTrapCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfExtTrapCfgEntry.setStatus("current")


class _H3cIfBandwidthUpperLimit_Type(Integer32):
    """Custom type h3cIfBandwidthUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cIfBandwidthUpperLimit_Type.__name__ = "Integer32"
_H3cIfBandwidthUpperLimit_Object = MibTableColumn
h3cIfBandwidthUpperLimit = _H3cIfBandwidthUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1, 1),
    _H3cIfBandwidthUpperLimit_Type()
)
h3cIfBandwidthUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfBandwidthUpperLimit.setStatus("current")


class _H3cIfDiscardPktRateUpperLimit_Type(Integer32):
    """Custom type h3cIfDiscardPktRateUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cIfDiscardPktRateUpperLimit_Type.__name__ = "Integer32"
_H3cIfDiscardPktRateUpperLimit_Object = MibTableColumn
h3cIfDiscardPktRateUpperLimit = _H3cIfDiscardPktRateUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1, 2),
    _H3cIfDiscardPktRateUpperLimit_Type()
)
h3cIfDiscardPktRateUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfDiscardPktRateUpperLimit.setStatus("current")
_H3cIfMonScalarGroup_ObjectIdentity = ObjectIdentity
h3cIfMonScalarGroup = _H3cIfMonScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 4)
)
_H3cIfMonGroup_ObjectIdentity = ObjectIdentity
h3cIfMonGroup = _H3cIfMonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5)
)
_H3cIfMonStat_ObjectIdentity = ObjectIdentity
h3cIfMonStat = _H3cIfMonStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1)
)
_H3cIfMonStatTable_Object = MibTable
h3cIfMonStatTable = _H3cIfMonStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfMonStatTable.setStatus("current")
_H3cIfMonStatEntry_Object = MibTableRow
h3cIfMonStatEntry = _H3cIfMonStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1)
)
h3cIfMonStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfMonStatEntry.setStatus("current")
_H3cIfMonInputRateStatistics_Type = Counter64
_H3cIfMonInputRateStatistics_Object = MibTableColumn
h3cIfMonInputRateStatistics = _H3cIfMonInputRateStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 1),
    _H3cIfMonInputRateStatistics_Type()
)
h3cIfMonInputRateStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonInputRateStatistics.setStatus("current")
_H3cIfMonOutputRateStatistics_Type = Counter64
_H3cIfMonOutputRateStatistics_Object = MibTableColumn
h3cIfMonOutputRateStatistics = _H3cIfMonOutputRateStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 2),
    _H3cIfMonOutputRateStatistics_Type()
)
h3cIfMonOutputRateStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonOutputRateStatistics.setStatus("current")
_H3cIfMonInputErrorAlarmStatistics_Type = Counter64
_H3cIfMonInputErrorAlarmStatistics_Object = MibTableColumn
h3cIfMonInputErrorAlarmStatistics = _H3cIfMonInputErrorAlarmStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 3),
    _H3cIfMonInputErrorAlarmStatistics_Type()
)
h3cIfMonInputErrorAlarmStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonInputErrorAlarmStatistics.setStatus("current")
_H3cIfMonOutputErrorAlarmStatistics_Type = Counter64
_H3cIfMonOutputErrorAlarmStatistics_Object = MibTableColumn
h3cIfMonOutputErrorAlarmStatistics = _H3cIfMonOutputErrorAlarmStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 4),
    _H3cIfMonOutputErrorAlarmStatistics_Type()
)
h3cIfMonOutputErrorAlarmStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonOutputErrorAlarmStatistics.setStatus("current")
_H3cIfMonSdhErrorStatistics_Type = Counter64
_H3cIfMonSdhErrorStatistics_Object = MibTableColumn
h3cIfMonSdhErrorStatistics = _H3cIfMonSdhErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 5),
    _H3cIfMonSdhErrorStatistics_Type()
)
h3cIfMonSdhErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonSdhErrorStatistics.setStatus("current")
_H3cIfMonSdhB1ErrorStatistics_Type = Counter64
_H3cIfMonSdhB1ErrorStatistics_Object = MibTableColumn
h3cIfMonSdhB1ErrorStatistics = _H3cIfMonSdhB1ErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 6),
    _H3cIfMonSdhB1ErrorStatistics_Type()
)
h3cIfMonSdhB1ErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonSdhB1ErrorStatistics.setStatus("current")
_H3cIfMonSdhB2ErrorStatistics_Type = Counter64
_H3cIfMonSdhB2ErrorStatistics_Object = MibTableColumn
h3cIfMonSdhB2ErrorStatistics = _H3cIfMonSdhB2ErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 7),
    _H3cIfMonSdhB2ErrorStatistics_Type()
)
h3cIfMonSdhB2ErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonSdhB2ErrorStatistics.setStatus("current")
_H3cIfMonCRCErrorStatistics_Type = Counter64
_H3cIfMonCRCErrorStatistics_Object = MibTableColumn
h3cIfMonCRCErrorStatistics = _H3cIfMonCRCErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 8),
    _H3cIfMonCRCErrorStatistics_Type()
)
h3cIfMonCRCErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonCRCErrorStatistics.setStatus("current")
_H3cIfMonPauseFrameStatistics_Type = Counter64
_H3cIfMonPauseFrameStatistics_Object = MibTableColumn
h3cIfMonPauseFrameStatistics = _H3cIfMonPauseFrameStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 9),
    _H3cIfMonPauseFrameStatistics_Type()
)
h3cIfMonPauseFrameStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonPauseFrameStatistics.setStatus("current")
_H3cIfMonTxPauseFrameStatistics_Type = Counter64
_H3cIfMonTxPauseFrameStatistics_Object = MibTableColumn
h3cIfMonTxPauseFrameStatistics = _H3cIfMonTxPauseFrameStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 1, 1, 1, 10),
    _H3cIfMonTxPauseFrameStatistics_Type()
)
h3cIfMonTxPauseFrameStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfMonTxPauseFrameStatistics.setStatus("current")
_H3cIfMonControl_ObjectIdentity = ObjectIdentity
h3cIfMonControl = _H3cIfMonControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2)
)
_H3cIfMonThresholdTable_Object = MibTable
h3cIfMonThresholdTable = _H3cIfMonThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfMonThresholdTable.setStatus("current")
_H3cIfMonThresholdEntry_Object = MibTableRow
h3cIfMonThresholdEntry = _H3cIfMonThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1)
)
h3cIfMonThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfMonThresholdEntry.setStatus("current")


class _H3cIfMonInputRateLowThres_Type(Unsigned32):
    """Custom type h3cIfMonInputRateLowThres based on Unsigned32"""
    defaultValue = 80


_H3cIfMonInputRateLowThres_Type.__name__ = "Unsigned32"
_H3cIfMonInputRateLowThres_Object = MibTableColumn
h3cIfMonInputRateLowThres = _H3cIfMonInputRateLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 1),
    _H3cIfMonInputRateLowThres_Type()
)
h3cIfMonInputRateLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonInputRateLowThres.setStatus("current")


class _H3cIfMonInputRateHighThres_Type(Unsigned32):
    """Custom type h3cIfMonInputRateHighThres based on Unsigned32"""
    defaultValue = 90


_H3cIfMonInputRateHighThres_Type.__name__ = "Unsigned32"
_H3cIfMonInputRateHighThres_Object = MibTableColumn
h3cIfMonInputRateHighThres = _H3cIfMonInputRateHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 2),
    _H3cIfMonInputRateHighThres_Type()
)
h3cIfMonInputRateHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonInputRateHighThres.setStatus("current")


class _H3cIfMonOutputRateLowThres_Type(Unsigned32):
    """Custom type h3cIfMonOutputRateLowThres based on Unsigned32"""
    defaultValue = 80


_H3cIfMonOutputRateLowThres_Type.__name__ = "Unsigned32"
_H3cIfMonOutputRateLowThres_Object = MibTableColumn
h3cIfMonOutputRateLowThres = _H3cIfMonOutputRateLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 3),
    _H3cIfMonOutputRateLowThres_Type()
)
h3cIfMonOutputRateLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonOutputRateLowThres.setStatus("current")


class _H3cIfMonOutputRateHighThres_Type(Unsigned32):
    """Custom type h3cIfMonOutputRateHighThres based on Unsigned32"""
    defaultValue = 90


_H3cIfMonOutputRateHighThres_Type.__name__ = "Unsigned32"
_H3cIfMonOutputRateHighThres_Object = MibTableColumn
h3cIfMonOutputRateHighThres = _H3cIfMonOutputRateHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 4),
    _H3cIfMonOutputRateHighThres_Type()
)
h3cIfMonOutputRateHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonOutputRateHighThres.setStatus("current")


class _H3cIfMonInputErrorAlarmLowThres_Type(Unsigned32):
    """Custom type h3cIfMonInputErrorAlarmLowThres based on Unsigned32"""
    defaultValue = 100


_H3cIfMonInputErrorAlarmLowThres_Type.__name__ = "Unsigned32"
_H3cIfMonInputErrorAlarmLowThres_Object = MibTableColumn
h3cIfMonInputErrorAlarmLowThres = _H3cIfMonInputErrorAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 5),
    _H3cIfMonInputErrorAlarmLowThres_Type()
)
h3cIfMonInputErrorAlarmLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonInputErrorAlarmLowThres.setStatus("current")


class _H3cIfMonInputErrorAlarmHighThres_Type(Unsigned32):
    """Custom type h3cIfMonInputErrorAlarmHighThres based on Unsigned32"""
    defaultValue = 1000


_H3cIfMonInputErrorAlarmHighThres_Type.__name__ = "Unsigned32"
_H3cIfMonInputErrorAlarmHighThres_Object = MibTableColumn
h3cIfMonInputErrorAlarmHighThres = _H3cIfMonInputErrorAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 6),
    _H3cIfMonInputErrorAlarmHighThres_Type()
)
h3cIfMonInputErrorAlarmHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonInputErrorAlarmHighThres.setStatus("current")


class _H3cIfMonInputErrorAlarmInterval_Type(Unsigned32):
    """Custom type h3cIfMonInputErrorAlarmInterval based on Unsigned32"""
    defaultValue = 10


_H3cIfMonInputErrorAlarmInterval_Type.__name__ = "Unsigned32"
_H3cIfMonInputErrorAlarmInterval_Object = MibTableColumn
h3cIfMonInputErrorAlarmInterval = _H3cIfMonInputErrorAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 7),
    _H3cIfMonInputErrorAlarmInterval_Type()
)
h3cIfMonInputErrorAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonInputErrorAlarmInterval.setStatus("current")


class _H3cIfMonOutputErrorAlarmLowThres_Type(Unsigned32):
    """Custom type h3cIfMonOutputErrorAlarmLowThres based on Unsigned32"""
    defaultValue = 100


_H3cIfMonOutputErrorAlarmLowThres_Type.__name__ = "Unsigned32"
_H3cIfMonOutputErrorAlarmLowThres_Object = MibTableColumn
h3cIfMonOutputErrorAlarmLowThres = _H3cIfMonOutputErrorAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 8),
    _H3cIfMonOutputErrorAlarmLowThres_Type()
)
h3cIfMonOutputErrorAlarmLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonOutputErrorAlarmLowThres.setStatus("current")


class _H3cIfMonOutputErrorAlarmHighThres_Type(Unsigned32):
    """Custom type h3cIfMonOutputErrorAlarmHighThres based on Unsigned32"""
    defaultValue = 1000


_H3cIfMonOutputErrorAlarmHighThres_Type.__name__ = "Unsigned32"
_H3cIfMonOutputErrorAlarmHighThres_Object = MibTableColumn
h3cIfMonOutputErrorAlarmHighThres = _H3cIfMonOutputErrorAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 9),
    _H3cIfMonOutputErrorAlarmHighThres_Type()
)
h3cIfMonOutputErrorAlarmHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonOutputErrorAlarmHighThres.setStatus("current")


class _H3cIfMonOutputErrorAlarmInterval_Type(Unsigned32):
    """Custom type h3cIfMonOutputErrorAlarmInterval based on Unsigned32"""
    defaultValue = 10


_H3cIfMonOutputErrorAlarmInterval_Type.__name__ = "Unsigned32"
_H3cIfMonOutputErrorAlarmInterval_Object = MibTableColumn
h3cIfMonOutputErrorAlarmInterval = _H3cIfMonOutputErrorAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 10),
    _H3cIfMonOutputErrorAlarmInterval_Type()
)
h3cIfMonOutputErrorAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonOutputErrorAlarmInterval.setStatus("current")


class _H3cIfMonSdhErrorLowThres_Type(Unsigned32):
    """Custom type h3cIfMonSdhErrorLowThres based on Unsigned32"""
    defaultValue = 100


_H3cIfMonSdhErrorLowThres_Type.__name__ = "Unsigned32"
_H3cIfMonSdhErrorLowThres_Object = MibTableColumn
h3cIfMonSdhErrorLowThres = _H3cIfMonSdhErrorLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 11),
    _H3cIfMonSdhErrorLowThres_Type()
)
h3cIfMonSdhErrorLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhErrorLowThres.setStatus("current")


class _H3cIfMonSdhErrorHighThres_Type(Unsigned32):
    """Custom type h3cIfMonSdhErrorHighThres based on Unsigned32"""
    defaultValue = 1000


_H3cIfMonSdhErrorHighThres_Type.__name__ = "Unsigned32"
_H3cIfMonSdhErrorHighThres_Object = MibTableColumn
h3cIfMonSdhErrorHighThres = _H3cIfMonSdhErrorHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 12),
    _H3cIfMonSdhErrorHighThres_Type()
)
h3cIfMonSdhErrorHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhErrorHighThres.setStatus("current")


class _H3cIfMonSdhErrorInterval_Type(Unsigned32):
    """Custom type h3cIfMonSdhErrorInterval based on Unsigned32"""
    defaultValue = 10


_H3cIfMonSdhErrorInterval_Type.__name__ = "Unsigned32"
_H3cIfMonSdhErrorInterval_Object = MibTableColumn
h3cIfMonSdhErrorInterval = _H3cIfMonSdhErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 13),
    _H3cIfMonSdhErrorInterval_Type()
)
h3cIfMonSdhErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhErrorInterval.setStatus("current")
_H3cIfMonSdhB1ErrorLowThres_Type = Unsigned32
_H3cIfMonSdhB1ErrorLowThres_Object = MibTableColumn
h3cIfMonSdhB1ErrorLowThres = _H3cIfMonSdhB1ErrorLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 14),
    _H3cIfMonSdhB1ErrorLowThres_Type()
)
h3cIfMonSdhB1ErrorLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhB1ErrorLowThres.setStatus("current")


class _H3cIfMonSdhB1ErrorHighThres_Type(Unsigned32):
    """Custom type h3cIfMonSdhB1ErrorHighThres based on Unsigned32"""
    defaultValue = 1000


_H3cIfMonSdhB1ErrorHighThres_Type.__name__ = "Unsigned32"
_H3cIfMonSdhB1ErrorHighThres_Object = MibTableColumn
h3cIfMonSdhB1ErrorHighThres = _H3cIfMonSdhB1ErrorHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 15),
    _H3cIfMonSdhB1ErrorHighThres_Type()
)
h3cIfMonSdhB1ErrorHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhB1ErrorHighThres.setStatus("current")


class _H3cIfMonSdhB1ErrorInterval_Type(Unsigned32):
    """Custom type h3cIfMonSdhB1ErrorInterval based on Unsigned32"""
    defaultValue = 10


_H3cIfMonSdhB1ErrorInterval_Type.__name__ = "Unsigned32"
_H3cIfMonSdhB1ErrorInterval_Object = MibTableColumn
h3cIfMonSdhB1ErrorInterval = _H3cIfMonSdhB1ErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 16),
    _H3cIfMonSdhB1ErrorInterval_Type()
)
h3cIfMonSdhB1ErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhB1ErrorInterval.setStatus("current")
_H3cIfMonSdhB2ErrorLowThres_Type = Unsigned32
_H3cIfMonSdhB2ErrorLowThres_Object = MibTableColumn
h3cIfMonSdhB2ErrorLowThres = _H3cIfMonSdhB2ErrorLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 17),
    _H3cIfMonSdhB2ErrorLowThres_Type()
)
h3cIfMonSdhB2ErrorLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhB2ErrorLowThres.setStatus("current")


class _H3cIfMonSdhB2ErrorHighThres_Type(Unsigned32):
    """Custom type h3cIfMonSdhB2ErrorHighThres based on Unsigned32"""
    defaultValue = 1000


_H3cIfMonSdhB2ErrorHighThres_Type.__name__ = "Unsigned32"
_H3cIfMonSdhB2ErrorHighThres_Object = MibTableColumn
h3cIfMonSdhB2ErrorHighThres = _H3cIfMonSdhB2ErrorHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 18),
    _H3cIfMonSdhB2ErrorHighThres_Type()
)
h3cIfMonSdhB2ErrorHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhB2ErrorHighThres.setStatus("current")


class _H3cIfMonSdhB2ErrorInterval_Type(Unsigned32):
    """Custom type h3cIfMonSdhB2ErrorInterval based on Unsigned32"""
    defaultValue = 10


_H3cIfMonSdhB2ErrorInterval_Type.__name__ = "Unsigned32"
_H3cIfMonSdhB2ErrorInterval_Object = MibTableColumn
h3cIfMonSdhB2ErrorInterval = _H3cIfMonSdhB2ErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 19),
    _H3cIfMonSdhB2ErrorInterval_Type()
)
h3cIfMonSdhB2ErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhB2ErrorInterval.setStatus("current")
_H3cIfMonCRCErrorLowThres_Type = Unsigned32
_H3cIfMonCRCErrorLowThres_Object = MibTableColumn
h3cIfMonCRCErrorLowThres = _H3cIfMonCRCErrorLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 20),
    _H3cIfMonCRCErrorLowThres_Type()
)
h3cIfMonCRCErrorLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonCRCErrorLowThres.setStatus("current")
_H3cIfMonCRCErrorHighThres_Type = Unsigned32
_H3cIfMonCRCErrorHighThres_Object = MibTableColumn
h3cIfMonCRCErrorHighThres = _H3cIfMonCRCErrorHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 21),
    _H3cIfMonCRCErrorHighThres_Type()
)
h3cIfMonCRCErrorHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonCRCErrorHighThres.setStatus("current")


class _H3cIfMonCRCErrorInterval_Type(Unsigned32):
    """Custom type h3cIfMonCRCErrorInterval based on Unsigned32"""
    defaultValue = 10


_H3cIfMonCRCErrorInterval_Type.__name__ = "Unsigned32"
_H3cIfMonCRCErrorInterval_Object = MibTableColumn
h3cIfMonCRCErrorInterval = _H3cIfMonCRCErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 22),
    _H3cIfMonCRCErrorInterval_Type()
)
h3cIfMonCRCErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonCRCErrorInterval.setStatus("current")


class _H3cIfMonCRCErrType_Type(Integer32):
    """Custom type h3cIfMonCRCErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("ratio", 2))
    )


_H3cIfMonCRCErrType_Type.__name__ = "Integer32"
_H3cIfMonCRCErrType_Object = MibTableColumn
h3cIfMonCRCErrType = _H3cIfMonCRCErrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 23),
    _H3cIfMonCRCErrType_Type()
)
h3cIfMonCRCErrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonCRCErrType.setStatus("current")
_H3cIfMonPauseFrameLowThres_Type = Unsigned32
_H3cIfMonPauseFrameLowThres_Object = MibTableColumn
h3cIfMonPauseFrameLowThres = _H3cIfMonPauseFrameLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 24),
    _H3cIfMonPauseFrameLowThres_Type()
)
h3cIfMonPauseFrameLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonPauseFrameLowThres.setStatus("current")
_H3cIfMonPauseFrameHighThres_Type = Unsigned32
_H3cIfMonPauseFrameHighThres_Object = MibTableColumn
h3cIfMonPauseFrameHighThres = _H3cIfMonPauseFrameHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 25),
    _H3cIfMonPauseFrameHighThres_Type()
)
h3cIfMonPauseFrameHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonPauseFrameHighThres.setStatus("current")
_H3cIfMonPauseFrameInterval_Type = Unsigned32
_H3cIfMonPauseFrameInterval_Object = MibTableColumn
h3cIfMonPauseFrameInterval = _H3cIfMonPauseFrameInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 26),
    _H3cIfMonPauseFrameInterval_Type()
)
h3cIfMonPauseFrameInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonPauseFrameInterval.setStatus("current")


class _H3cIfMonTxPauseFrameLowThres_Type(Unsigned32):
    """Custom type h3cIfMonTxPauseFrameLowThres based on Unsigned32"""
    defaultValue = 100


_H3cIfMonTxPauseFrameLowThres_Type.__name__ = "Unsigned32"
_H3cIfMonTxPauseFrameLowThres_Object = MibTableColumn
h3cIfMonTxPauseFrameLowThres = _H3cIfMonTxPauseFrameLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 27),
    _H3cIfMonTxPauseFrameLowThres_Type()
)
h3cIfMonTxPauseFrameLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonTxPauseFrameLowThres.setStatus("current")


class _H3cIfMonTxPauseFrameHighThres_Type(Unsigned32):
    """Custom type h3cIfMonTxPauseFrameHighThres based on Unsigned32"""
    defaultValue = 500


_H3cIfMonTxPauseFrameHighThres_Type.__name__ = "Unsigned32"
_H3cIfMonTxPauseFrameHighThres_Object = MibTableColumn
h3cIfMonTxPauseFrameHighThres = _H3cIfMonTxPauseFrameHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 28),
    _H3cIfMonTxPauseFrameHighThres_Type()
)
h3cIfMonTxPauseFrameHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonTxPauseFrameHighThres.setStatus("current")


class _H3cIfMonTxPauseFrameInterval_Type(Unsigned32):
    """Custom type h3cIfMonTxPauseFrameInterval based on Unsigned32"""
    defaultValue = 10


_H3cIfMonTxPauseFrameInterval_Type.__name__ = "Unsigned32"
_H3cIfMonTxPauseFrameInterval_Object = MibTableColumn
h3cIfMonTxPauseFrameInterval = _H3cIfMonTxPauseFrameInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 1, 1, 29),
    _H3cIfMonTxPauseFrameInterval_Type()
)
h3cIfMonTxPauseFrameInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonTxPauseFrameInterval.setStatus("current")
_H3cIfMonAlarmDownEnableTable_Object = MibTable
h3cIfMonAlarmDownEnableTable = _H3cIfMonAlarmDownEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2)
)
if mibBuilder.loadTexts:
    h3cIfMonAlarmDownEnableTable.setStatus("current")
_H3cIfMonAlarmDownEnableEntry_Object = MibTableRow
h3cIfMonAlarmDownEnableEntry = _H3cIfMonAlarmDownEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1)
)
h3cIfMonAlarmDownEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfMonAlarmDownEnableEntry.setStatus("current")


class _H3cIfMonInputRateEnableDown_Type(TruthValue):
    """Custom type h3cIfMonInputRateEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonInputRateEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonInputRateEnableDown_Object = MibTableColumn
h3cIfMonInputRateEnableDown = _H3cIfMonInputRateEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 1),
    _H3cIfMonInputRateEnableDown_Type()
)
h3cIfMonInputRateEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonInputRateEnableDown.setStatus("current")


class _H3cIfMonOutputRateEnableDown_Type(TruthValue):
    """Custom type h3cIfMonOutputRateEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonOutputRateEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonOutputRateEnableDown_Object = MibTableColumn
h3cIfMonOutputRateEnableDown = _H3cIfMonOutputRateEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 2),
    _H3cIfMonOutputRateEnableDown_Type()
)
h3cIfMonOutputRateEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonOutputRateEnableDown.setStatus("current")


class _H3cIfMonInputErrorAlarmEnableDown_Type(TruthValue):
    """Custom type h3cIfMonInputErrorAlarmEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonInputErrorAlarmEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonInputErrorAlarmEnableDown_Object = MibTableColumn
h3cIfMonInputErrorAlarmEnableDown = _H3cIfMonInputErrorAlarmEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 3),
    _H3cIfMonInputErrorAlarmEnableDown_Type()
)
h3cIfMonInputErrorAlarmEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonInputErrorAlarmEnableDown.setStatus("current")


class _H3cIfMonOutputErrorAlarmEnableDown_Type(TruthValue):
    """Custom type h3cIfMonOutputErrorAlarmEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonOutputErrorAlarmEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonOutputErrorAlarmEnableDown_Object = MibTableColumn
h3cIfMonOutputErrorAlarmEnableDown = _H3cIfMonOutputErrorAlarmEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 4),
    _H3cIfMonOutputErrorAlarmEnableDown_Type()
)
h3cIfMonOutputErrorAlarmEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonOutputErrorAlarmEnableDown.setStatus("current")


class _H3cIfMonSdhErrorEnableDown_Type(TruthValue):
    """Custom type h3cIfMonSdhErrorEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonSdhErrorEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonSdhErrorEnableDown_Object = MibTableColumn
h3cIfMonSdhErrorEnableDown = _H3cIfMonSdhErrorEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 5),
    _H3cIfMonSdhErrorEnableDown_Type()
)
h3cIfMonSdhErrorEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhErrorEnableDown.setStatus("current")


class _H3cIfMonSdhB1ErrorEnableDown_Type(TruthValue):
    """Custom type h3cIfMonSdhB1ErrorEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonSdhB1ErrorEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonSdhB1ErrorEnableDown_Object = MibTableColumn
h3cIfMonSdhB1ErrorEnableDown = _H3cIfMonSdhB1ErrorEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 6),
    _H3cIfMonSdhB1ErrorEnableDown_Type()
)
h3cIfMonSdhB1ErrorEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhB1ErrorEnableDown.setStatus("current")


class _H3cIfMonSdhB2ErrorEnableDown_Type(TruthValue):
    """Custom type h3cIfMonSdhB2ErrorEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonSdhB2ErrorEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonSdhB2ErrorEnableDown_Object = MibTableColumn
h3cIfMonSdhB2ErrorEnableDown = _H3cIfMonSdhB2ErrorEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 7),
    _H3cIfMonSdhB2ErrorEnableDown_Type()
)
h3cIfMonSdhB2ErrorEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonSdhB2ErrorEnableDown.setStatus("current")


class _H3cIfMonCRCErrorEnableDown_Type(TruthValue):
    """Custom type h3cIfMonCRCErrorEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonCRCErrorEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonCRCErrorEnableDown_Object = MibTableColumn
h3cIfMonCRCErrorEnableDown = _H3cIfMonCRCErrorEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 8),
    _H3cIfMonCRCErrorEnableDown_Type()
)
h3cIfMonCRCErrorEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonCRCErrorEnableDown.setStatus("current")


class _H3cIfMonPauseFrameEnableDown_Type(TruthValue):
    """Custom type h3cIfMonPauseFrameEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonPauseFrameEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonPauseFrameEnableDown_Object = MibTableColumn
h3cIfMonPauseFrameEnableDown = _H3cIfMonPauseFrameEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 9),
    _H3cIfMonPauseFrameEnableDown_Type()
)
h3cIfMonPauseFrameEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonPauseFrameEnableDown.setStatus("current")


class _H3cIfMonTxPauseFrameEnableDown_Type(TruthValue):
    """Custom type h3cIfMonTxPauseFrameEnableDown based on TruthValue"""
    defaultValue = 2


_H3cIfMonTxPauseFrameEnableDown_Type.__name__ = "TruthValue"
_H3cIfMonTxPauseFrameEnableDown_Object = MibTableColumn
h3cIfMonTxPauseFrameEnableDown = _H3cIfMonTxPauseFrameEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 5, 2, 2, 1, 10),
    _H3cIfMonTxPauseFrameEnableDown_Type()
)
h3cIfMonTxPauseFrameEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMonTxPauseFrameEnableDown.setStatus("current")
_H3cIfMonTrap_ObjectIdentity = ObjectIdentity
h3cIfMonTrap = _H3cIfMonTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6)
)
_H3cIfMonTrapPrex_ObjectIdentity = ObjectIdentity
h3cIfMonTrapPrex = _H3cIfMonTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0)
)
_H3cIfMonTrapObject_ObjectIdentity = ObjectIdentity
h3cIfMonTrapObject = _H3cIfMonTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 1)
)

# Managed Objects groups


# Notification objects

h3cIfBandwidthUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 1)
)
h3cIfBandwidthUsageHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfBandwidthRate"),
        ("H3C-IF-EXT-MIB", "h3cIfBandwidthUpperLimit"))
)
if mibBuilder.loadTexts:
    h3cIfBandwidthUsageHigh.setStatus(
        "current"
    )

h3cIfDiscardPktRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 2)
)
h3cIfDiscardPktRateHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfDiscardPktRate"),
        ("H3C-IF-EXT-MIB", "h3cIfDiscardPktRateUpperLimit"))
)
if mibBuilder.loadTexts:
    h3cIfDiscardPktRateHigh.setStatus(
        "current"
    )

h3cIfDampeningSuppressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 3)
)
h3cIfDampeningSuppressed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cIfDampeningSuppressed.setStatus(
        "current"
    )

h3cIfDampeningNotSuppressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 4)
)
h3cIfDampeningNotSuppressed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cIfDampeningNotSuppressed.setStatus(
        "current"
    )

h3cIfPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 5)
)
h3cIfPortUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cIfPortUp.setStatus(
        "current"
    )

h3cIfPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 6)
)
h3cIfPortDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cIfPortDown.setStatus(
        "current"
    )

h3cIfPfcOutRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 7)
)
h3cIfPfcOutRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfPfcDot1pValue"),
        ("H3C-IF-EXT-MIB", "h3cIfPfcDot1pOutPps"),
        ("H3C-IF-EXT-MIB", "h3cIfPfcDot1pOutPpsThreshold"))
)
if mibBuilder.loadTexts:
    h3cIfPfcOutRising.setStatus(
        "current"
    )

h3cIfPfcInRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 8)
)
h3cIfPfcInRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfPfcDot1pValue"),
        ("H3C-IF-EXT-MIB", "h3cIfPfcDot1pInPps"),
        ("H3C-IF-EXT-MIB", "h3cIfPfcDot1pInPpsThreshold"))
)
if mibBuilder.loadTexts:
    h3cIfPfcInRising.setStatus(
        "current"
    )

h3cIfMonInputRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 1)
)
h3cIfMonInputRateRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputRateLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputRateHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputRateStatistics"))
)
if mibBuilder.loadTexts:
    h3cIfMonInputRateRising.setStatus(
        "current"
    )

h3cIfMonInputRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 2)
)
h3cIfMonInputRateResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputRateLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputRateHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputRateStatistics"))
)
if mibBuilder.loadTexts:
    h3cIfMonInputRateResume.setStatus(
        "current"
    )

h3cIfMonOutputRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 3)
)
h3cIfMonOutputRateRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputRateLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputRateHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputRateStatistics"))
)
if mibBuilder.loadTexts:
    h3cIfMonOutputRateRising.setStatus(
        "current"
    )

h3cIfMonOutputRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 4)
)
h3cIfMonOutputRateResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputRateLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputRateHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputRateStatistics"))
)
if mibBuilder.loadTexts:
    h3cIfMonOutputRateResume.setStatus(
        "current"
    )

h3cIfMonInputErrorAlarmRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 5)
)
h3cIfMonInputErrorAlarmRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputErrorAlarmHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputErrorAlarmLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputErrorAlarmStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputErrorAlarmInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonInputErrorAlarmRising.setStatus(
        "current"
    )

h3cIfMonInputErrorAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 6)
)
h3cIfMonInputErrorAlarmResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputErrorAlarmHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputErrorAlarmLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputErrorAlarmStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonInputErrorAlarmInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonInputErrorAlarmResume.setStatus(
        "current"
    )

h3cIfMonOutputErrorAlarmRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 7)
)
h3cIfMonOutputErrorAlarmRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputErrorAlarmHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputErrorAlarmLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputErrorAlarmStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputErrorAlarmInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonOutputErrorAlarmRising.setStatus(
        "current"
    )

h3cIfMonOutputErrorAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 8)
)
h3cIfMonOutputErrorAlarmResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputErrorAlarmHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputErrorAlarmLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputErrorAlarmStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonOutputErrorAlarmInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonOutputErrorAlarmResume.setStatus(
        "current"
    )

h3cIfMonSdhErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 9)
)
h3cIfMonSdhErrorRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhErrorLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhErrorHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhErrorStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhErrorInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonSdhErrorRising.setStatus(
        "current"
    )

h3cIfMonSdhErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 10)
)
h3cIfMonSdhErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhErrorLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhErrorHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhErrorStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhErrorInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonSdhErrorResume.setStatus(
        "current"
    )

h3cIfMonSdhB1ErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 11)
)
h3cIfMonSdhB1ErrorRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB1ErrorLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB1ErrorHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB1ErrorStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB1ErrorInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonSdhB1ErrorRising.setStatus(
        "current"
    )

h3cIfMonSdhB1ErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 12)
)
h3cIfMonSdhB1ErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB1ErrorLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB1ErrorHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB1ErrorStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB1ErrorInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonSdhB1ErrorResume.setStatus(
        "current"
    )

h3cIfMonSdhB2ErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 13)
)
h3cIfMonSdhB2ErrorRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB2ErrorLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB2ErrorHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB2ErrorStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB2ErrorInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonSdhB2ErrorRising.setStatus(
        "current"
    )

h3cIfMonSdhB2ErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 14)
)
h3cIfMonSdhB2ErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB2ErrorLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB2ErrorHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB2ErrorStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonSdhB2ErrorInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonSdhB2ErrorResume.setStatus(
        "current"
    )

h3cIfMonCRCErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 15)
)
h3cIfMonCRCErrorRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrorHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrorLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrorStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrorInterval"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrType"))
)
if mibBuilder.loadTexts:
    h3cIfMonCRCErrorRising.setStatus(
        "current"
    )

h3cIfMonCRCErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 16)
)
h3cIfMonCRCErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrorHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrorLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrorStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrorInterval"),
        ("H3C-IF-EXT-MIB", "h3cIfMonCRCErrType"))
)
if mibBuilder.loadTexts:
    h3cIfMonCRCErrorResume.setStatus(
        "current"
    )

h3cIfMonPauseFrameRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 17)
)
h3cIfMonPauseFrameRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonPauseFrameHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonPauseFrameLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonPauseFrameStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonPauseFrameRising.setStatus(
        "current"
    )

h3cIfMonPauseFrameResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 18)
)
h3cIfMonPauseFrameResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonPauseFrameHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonPauseFrameLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonPauseFrameStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonPauseFrameResume.setStatus(
        "current"
    )

h3cIfMonTxPauseFrameRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 19)
)
h3cIfMonTxPauseFrameRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonTxPauseFrameHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonTxPauseFrameLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonTxPauseFrameStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonTxPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonTxPauseFrameRising.setStatus(
        "current"
    )

h3cIfMonTxPauseFrameResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 6, 0, 20)
)
h3cIfMonTxPauseFrameResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfMonTxPauseFrameHighThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonTxPauseFrameLowThres"),
        ("H3C-IF-EXT-MIB", "h3cIfMonTxPauseFrameStatistics"),
        ("H3C-IF-EXT-MIB", "h3cIfMonTxPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    h3cIfMonTxPauseFrameResume.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-IF-EXT-MIB",
    **{"h3cIfExt": h3cIfExt,
       "h3cIfExtScalarGroup": h3cIfExtScalarGroup,
       "h3cIfStatGlobalFlowInterval": h3cIfStatGlobalFlowInterval,
       "h3cIfShutDownInterval": h3cIfShutDownInterval,
       "h3cIfThroughputInKbps": h3cIfThroughputInKbps,
       "h3cIfThroughputOutKbps": h3cIfThroughputOutKbps,
       "h3cIfExtGroup": h3cIfExtGroup,
       "h3cIfStat": h3cIfStat,
       "h3cIfStatScalarGroup": h3cIfStatScalarGroup,
       "h3cIfStatTable": h3cIfStatTable,
       "h3cIfFlowStatTable": h3cIfFlowStatTable,
       "h3cIfStatEntry": h3cIfStatEntry,
       "h3cIfStatFlowInterval": h3cIfStatFlowInterval,
       "h3cIfStatFlowInBits": h3cIfStatFlowInBits,
       "h3cIfStatFlowOutBits": h3cIfStatFlowOutBits,
       "h3cIfStatFlowInPkts": h3cIfStatFlowInPkts,
       "h3cIfStatFlowOutPkts": h3cIfStatFlowOutPkts,
       "h3cIfStatFlowInBytes": h3cIfStatFlowInBytes,
       "h3cIfStatFlowOutBytes": h3cIfStatFlowOutBytes,
       "h3cIfSpeedStatTable": h3cIfSpeedStatTable,
       "h3cIfSpeedStatEntry": h3cIfSpeedStatEntry,
       "h3cIfSpeedStatInterval": h3cIfSpeedStatInterval,
       "h3cIfSpeedStatInPkts": h3cIfSpeedStatInPkts,
       "h3cIfSpeedStatOutPkts": h3cIfSpeedStatOutPkts,
       "h3cIfSpeedStatInBytes": h3cIfSpeedStatInBytes,
       "h3cIfSpeedStatOutBytes": h3cIfSpeedStatOutBytes,
       "h3cIfHCFlowStatTable": h3cIfHCFlowStatTable,
       "h3cIfHCFlowStatEntry": h3cIfHCFlowStatEntry,
       "h3cIfStatFlowHCInBits": h3cIfStatFlowHCInBits,
       "h3cIfStatFlowHCOutBits": h3cIfStatFlowHCOutBits,
       "h3cIfStatFlowHCInPkts": h3cIfStatFlowHCInPkts,
       "h3cIfStatFlowHCOutPkts": h3cIfStatFlowHCOutPkts,
       "h3cIfStatFlowHCInBytes": h3cIfStatFlowHCInBytes,
       "h3cIfStatFlowHCOutBytes": h3cIfStatFlowHCOutBytes,
       "h3cIfHCSpeedStatTable": h3cIfHCSpeedStatTable,
       "h3cIfHCSpeedStatEntry": h3cIfHCSpeedStatEntry,
       "h3cIfSpeedStatHCInPkts": h3cIfSpeedStatHCInPkts,
       "h3cIfSpeedStatHCOutPkts": h3cIfSpeedStatHCOutPkts,
       "h3cIfSpeedStatHCInBytes": h3cIfSpeedStatHCInBytes,
       "h3cIfSpeedStatHCOutBytes": h3cIfSpeedStatHCOutBytes,
       "h3cIfControl": h3cIfControl,
       "h3cRTParentIfTable": h3cRTParentIfTable,
       "h3cRTParentIfEntry": h3cRTParentIfEntry,
       "h3cRTParentIfIndex": h3cRTParentIfIndex,
       "h3cRTMinSubIfOrdinal": h3cRTMinSubIfOrdinal,
       "h3cRTMaxSubIfOrdinal": h3cRTMaxSubIfOrdinal,
       "h3cRTSubIfTable": h3cRTSubIfTable,
       "h3cRTSubIfEntry": h3cRTSubIfEntry,
       "h3cRTSubIfParentIfIndex": h3cRTSubIfParentIfIndex,
       "h3cRTSubIfOrdinal": h3cRTSubIfOrdinal,
       "h3cRTSubIfSubIfIndex": h3cRTSubIfSubIfIndex,
       "h3cRTSubIfSubIfDesc": h3cRTSubIfSubIfDesc,
       "h3cRTSubIfRowStatus": h3cRTSubIfRowStatus,
       "h3cIfLinkModeTable": h3cIfLinkModeTable,
       "h3cIfLinkModeEntry": h3cIfLinkModeEntry,
       "h3cIfLinkModeIndex": h3cIfLinkModeIndex,
       "h3cIfLinkMode": h3cIfLinkMode,
       "h3cIfLinkModeSwitchSupport": h3cIfLinkModeSwitchSupport,
       "h3cIfPortTypeTable": h3cIfPortTypeTable,
       "h3cIfPortTypeEntry": h3cIfPortTypeEntry,
       "h3cIfPortTypeIndex": h3cIfPortTypeIndex,
       "h3cIfPortType": h3cIfPortType,
       "h3cIfPfcDot1pTable": h3cIfPfcDot1pTable,
       "h3cIfPfcDot1pEntry": h3cIfPfcDot1pEntry,
       "h3cIfPfcDot1pValue": h3cIfPfcDot1pValue,
       "h3cIfPfcDot1pInPps": h3cIfPfcDot1pInPps,
       "h3cIfPfcDot1pOutPps": h3cIfPfcDot1pOutPps,
       "h3cIfPfcDot1pInPpsThreshold": h3cIfPfcDot1pInPpsThreshold,
       "h3cIfPfcDot1pOutPpsThreshold": h3cIfPfcDot1pOutPpsThreshold,
       "h3cIfInterfaces": h3cIfInterfaces,
       "h3cIfPhysicalNumber": h3cIfPhysicalNumber,
       "h3cIfTable": h3cIfTable,
       "h3cIfEntry": h3cIfEntry,
       "h3cIfUpDownTimes": h3cIfUpDownTimes,
       "h3cIfMtu": h3cIfMtu,
       "h3cIfBandwidthRate": h3cIfBandwidthRate,
       "h3cIfDiscardPktRate": h3cIfDiscardPktRate,
       "h3cIfStatusKeepTime": h3cIfStatusKeepTime,
       "h3cIfInNUcastPkts": h3cIfInNUcastPkts,
       "h3cIfOutNUcastPkts": h3cIfOutNUcastPkts,
       "h3cIfIsPoe": h3cIfIsPoe,
       "h3cIfOperStatus": h3cIfOperStatus,
       "h3cIfDownTimes": h3cIfDownTimes,
       "h3cIfPfcStatus": h3cIfPfcStatus,
       "h3cIfPfcDot1pNoDrop": h3cIfPfcDot1pNoDrop,
       "h3cIfDescription": h3cIfDescription,
       "h3cIfFwdErrDiscards": h3cIfFwdErrDiscards,
       "h3cIfUsingTable": h3cIfUsingTable,
       "h3cIfUsingEntry": h3cIfUsingEntry,
       "h3cIfUsingIndex": h3cIfUsingIndex,
       "h3cIfUsingSupportType": h3cIfUsingSupportType,
       "h3cIfUsingType": h3cIfUsingType,
       "h3cIfUsingStatus": h3cIfUsingStatus,
       "h3cIfExtTrap": h3cIfExtTrap,
       "h3cIfExtTrapPrex": h3cIfExtTrapPrex,
       "h3cIfBandwidthUsageHigh": h3cIfBandwidthUsageHigh,
       "h3cIfDiscardPktRateHigh": h3cIfDiscardPktRateHigh,
       "h3cIfDampeningSuppressed": h3cIfDampeningSuppressed,
       "h3cIfDampeningNotSuppressed": h3cIfDampeningNotSuppressed,
       "h3cIfPortUp": h3cIfPortUp,
       "h3cIfPortDown": h3cIfPortDown,
       "h3cIfPfcOutRising": h3cIfPfcOutRising,
       "h3cIfPfcInRising": h3cIfPfcInRising,
       "h3cIfExtTrapObject": h3cIfExtTrapObject,
       "h3cIfExtTrapCfgTable": h3cIfExtTrapCfgTable,
       "h3cIfExtTrapCfgEntry": h3cIfExtTrapCfgEntry,
       "h3cIfBandwidthUpperLimit": h3cIfBandwidthUpperLimit,
       "h3cIfDiscardPktRateUpperLimit": h3cIfDiscardPktRateUpperLimit,
       "h3cIfMonScalarGroup": h3cIfMonScalarGroup,
       "h3cIfMonGroup": h3cIfMonGroup,
       "h3cIfMonStat": h3cIfMonStat,
       "h3cIfMonStatTable": h3cIfMonStatTable,
       "h3cIfMonStatEntry": h3cIfMonStatEntry,
       "h3cIfMonInputRateStatistics": h3cIfMonInputRateStatistics,
       "h3cIfMonOutputRateStatistics": h3cIfMonOutputRateStatistics,
       "h3cIfMonInputErrorAlarmStatistics": h3cIfMonInputErrorAlarmStatistics,
       "h3cIfMonOutputErrorAlarmStatistics": h3cIfMonOutputErrorAlarmStatistics,
       "h3cIfMonSdhErrorStatistics": h3cIfMonSdhErrorStatistics,
       "h3cIfMonSdhB1ErrorStatistics": h3cIfMonSdhB1ErrorStatistics,
       "h3cIfMonSdhB2ErrorStatistics": h3cIfMonSdhB2ErrorStatistics,
       "h3cIfMonCRCErrorStatistics": h3cIfMonCRCErrorStatistics,
       "h3cIfMonPauseFrameStatistics": h3cIfMonPauseFrameStatistics,
       "h3cIfMonTxPauseFrameStatistics": h3cIfMonTxPauseFrameStatistics,
       "h3cIfMonControl": h3cIfMonControl,
       "h3cIfMonThresholdTable": h3cIfMonThresholdTable,
       "h3cIfMonThresholdEntry": h3cIfMonThresholdEntry,
       "h3cIfMonInputRateLowThres": h3cIfMonInputRateLowThres,
       "h3cIfMonInputRateHighThres": h3cIfMonInputRateHighThres,
       "h3cIfMonOutputRateLowThres": h3cIfMonOutputRateLowThres,
       "h3cIfMonOutputRateHighThres": h3cIfMonOutputRateHighThres,
       "h3cIfMonInputErrorAlarmLowThres": h3cIfMonInputErrorAlarmLowThres,
       "h3cIfMonInputErrorAlarmHighThres": h3cIfMonInputErrorAlarmHighThres,
       "h3cIfMonInputErrorAlarmInterval": h3cIfMonInputErrorAlarmInterval,
       "h3cIfMonOutputErrorAlarmLowThres": h3cIfMonOutputErrorAlarmLowThres,
       "h3cIfMonOutputErrorAlarmHighThres": h3cIfMonOutputErrorAlarmHighThres,
       "h3cIfMonOutputErrorAlarmInterval": h3cIfMonOutputErrorAlarmInterval,
       "h3cIfMonSdhErrorLowThres": h3cIfMonSdhErrorLowThres,
       "h3cIfMonSdhErrorHighThres": h3cIfMonSdhErrorHighThres,
       "h3cIfMonSdhErrorInterval": h3cIfMonSdhErrorInterval,
       "h3cIfMonSdhB1ErrorLowThres": h3cIfMonSdhB1ErrorLowThres,
       "h3cIfMonSdhB1ErrorHighThres": h3cIfMonSdhB1ErrorHighThres,
       "h3cIfMonSdhB1ErrorInterval": h3cIfMonSdhB1ErrorInterval,
       "h3cIfMonSdhB2ErrorLowThres": h3cIfMonSdhB2ErrorLowThres,
       "h3cIfMonSdhB2ErrorHighThres": h3cIfMonSdhB2ErrorHighThres,
       "h3cIfMonSdhB2ErrorInterval": h3cIfMonSdhB2ErrorInterval,
       "h3cIfMonCRCErrorLowThres": h3cIfMonCRCErrorLowThres,
       "h3cIfMonCRCErrorHighThres": h3cIfMonCRCErrorHighThres,
       "h3cIfMonCRCErrorInterval": h3cIfMonCRCErrorInterval,
       "h3cIfMonCRCErrType": h3cIfMonCRCErrType,
       "h3cIfMonPauseFrameLowThres": h3cIfMonPauseFrameLowThres,
       "h3cIfMonPauseFrameHighThres": h3cIfMonPauseFrameHighThres,
       "h3cIfMonPauseFrameInterval": h3cIfMonPauseFrameInterval,
       "h3cIfMonTxPauseFrameLowThres": h3cIfMonTxPauseFrameLowThres,
       "h3cIfMonTxPauseFrameHighThres": h3cIfMonTxPauseFrameHighThres,
       "h3cIfMonTxPauseFrameInterval": h3cIfMonTxPauseFrameInterval,
       "h3cIfMonAlarmDownEnableTable": h3cIfMonAlarmDownEnableTable,
       "h3cIfMonAlarmDownEnableEntry": h3cIfMonAlarmDownEnableEntry,
       "h3cIfMonInputRateEnableDown": h3cIfMonInputRateEnableDown,
       "h3cIfMonOutputRateEnableDown": h3cIfMonOutputRateEnableDown,
       "h3cIfMonInputErrorAlarmEnableDown": h3cIfMonInputErrorAlarmEnableDown,
       "h3cIfMonOutputErrorAlarmEnableDown": h3cIfMonOutputErrorAlarmEnableDown,
       "h3cIfMonSdhErrorEnableDown": h3cIfMonSdhErrorEnableDown,
       "h3cIfMonSdhB1ErrorEnableDown": h3cIfMonSdhB1ErrorEnableDown,
       "h3cIfMonSdhB2ErrorEnableDown": h3cIfMonSdhB2ErrorEnableDown,
       "h3cIfMonCRCErrorEnableDown": h3cIfMonCRCErrorEnableDown,
       "h3cIfMonPauseFrameEnableDown": h3cIfMonPauseFrameEnableDown,
       "h3cIfMonTxPauseFrameEnableDown": h3cIfMonTxPauseFrameEnableDown,
       "h3cIfMonTrap": h3cIfMonTrap,
       "h3cIfMonTrapPrex": h3cIfMonTrapPrex,
       "h3cIfMonInputRateRising": h3cIfMonInputRateRising,
       "h3cIfMonInputRateResume": h3cIfMonInputRateResume,
       "h3cIfMonOutputRateRising": h3cIfMonOutputRateRising,
       "h3cIfMonOutputRateResume": h3cIfMonOutputRateResume,
       "h3cIfMonInputErrorAlarmRising": h3cIfMonInputErrorAlarmRising,
       "h3cIfMonInputErrorAlarmResume": h3cIfMonInputErrorAlarmResume,
       "h3cIfMonOutputErrorAlarmRising": h3cIfMonOutputErrorAlarmRising,
       "h3cIfMonOutputErrorAlarmResume": h3cIfMonOutputErrorAlarmResume,
       "h3cIfMonSdhErrorRising": h3cIfMonSdhErrorRising,
       "h3cIfMonSdhErrorResume": h3cIfMonSdhErrorResume,
       "h3cIfMonSdhB1ErrorRising": h3cIfMonSdhB1ErrorRising,
       "h3cIfMonSdhB1ErrorResume": h3cIfMonSdhB1ErrorResume,
       "h3cIfMonSdhB2ErrorRising": h3cIfMonSdhB2ErrorRising,
       "h3cIfMonSdhB2ErrorResume": h3cIfMonSdhB2ErrorResume,
       "h3cIfMonCRCErrorRising": h3cIfMonCRCErrorRising,
       "h3cIfMonCRCErrorResume": h3cIfMonCRCErrorResume,
       "h3cIfMonPauseFrameRising": h3cIfMonPauseFrameRising,
       "h3cIfMonPauseFrameResume": h3cIfMonPauseFrameResume,
       "h3cIfMonTxPauseFrameRising": h3cIfMonTxPauseFrameRising,
       "h3cIfMonTxPauseFrameResume": h3cIfMonTxPauseFrameResume,
       "h3cIfMonTrapObject": h3cIfMonTrapObject}
)
