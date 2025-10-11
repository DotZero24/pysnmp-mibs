# SNMP MIB module (ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-INFO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:02 2025
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

(adGenPseudowireCEMPerfInfo,
 adGenPseudowireCEMPerfInfoID) = mibBuilder.importSymbols(
    "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB",
    "adGenPseudowireCEMPerfInfo",
    "adGenPseudowireCEMPerfInfoID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenPseudowireCEMPerfInfoModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 30, 2, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPseudowireCEMCurrent15MinPerfTable_Object = MibTable
adGenPseudowireCEMCurrent15MinPerfTable = _AdGenPseudowireCEMCurrent15MinPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinPerfTable.setStatus("current")
_AdGenPseudowireCEMCurrent15MinPerfTableEntry_Object = MibTableRow
adGenPseudowireCEMCurrent15MinPerfTableEntry = _AdGenPseudowireCEMCurrent15MinPerfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1)
)
adGenPseudowireCEMCurrent15MinPerfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinPerfTableEntry.setStatus("current")
_AdGenPseudowireCEMCurrent15MinPacketsMissed_Type = Gauge32
_AdGenPseudowireCEMCurrent15MinPacketsMissed_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinPacketsMissed = _AdGenPseudowireCEMCurrent15MinPacketsMissed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 1),
    _AdGenPseudowireCEMCurrent15MinPacketsMissed_Type()
)
adGenPseudowireCEMCurrent15MinPacketsMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinPacketsMissed.setStatus("current")
_AdGenPseudowireCEMCurrent15MinPacketsDropped_Type = Gauge32
_AdGenPseudowireCEMCurrent15MinPacketsDropped_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinPacketsDropped = _AdGenPseudowireCEMCurrent15MinPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 2),
    _AdGenPseudowireCEMCurrent15MinPacketsDropped_Type()
)
adGenPseudowireCEMCurrent15MinPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinPacketsDropped.setStatus("current")
_AdGenPseudowireCEMCurrent15MinPacketsMalformed_Type = Gauge32
_AdGenPseudowireCEMCurrent15MinPacketsMalformed_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinPacketsMalformed = _AdGenPseudowireCEMCurrent15MinPacketsMalformed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 3),
    _AdGenPseudowireCEMCurrent15MinPacketsMalformed_Type()
)
adGenPseudowireCEMCurrent15MinPacketsMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinPacketsMalformed.setStatus("current")
_AdGenPseudowireCEMCurrent15MinFailureCount_Type = Gauge32
_AdGenPseudowireCEMCurrent15MinFailureCount_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinFailureCount = _AdGenPseudowireCEMCurrent15MinFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 4),
    _AdGenPseudowireCEMCurrent15MinFailureCount_Type()
)
adGenPseudowireCEMCurrent15MinFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinFailureCount.setStatus("current")
_AdGenPseudowireCEMCurrent15MinTxPacketCount_Type = Gauge32
_AdGenPseudowireCEMCurrent15MinTxPacketCount_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinTxPacketCount = _AdGenPseudowireCEMCurrent15MinTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 5),
    _AdGenPseudowireCEMCurrent15MinTxPacketCount_Type()
)
adGenPseudowireCEMCurrent15MinTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinTxPacketCount.setStatus("current")
_AdGenPseudowireCEMCurrent15MinRxPacketCount_Type = Gauge32
_AdGenPseudowireCEMCurrent15MinRxPacketCount_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinRxPacketCount = _AdGenPseudowireCEMCurrent15MinRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 6),
    _AdGenPseudowireCEMCurrent15MinRxPacketCount_Type()
)
adGenPseudowireCEMCurrent15MinRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinRxPacketCount.setStatus("current")
_AdGenPseudowireCEMCurrent15MinTxByteCount_Type = Counter64
_AdGenPseudowireCEMCurrent15MinTxByteCount_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinTxByteCount = _AdGenPseudowireCEMCurrent15MinTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 7),
    _AdGenPseudowireCEMCurrent15MinTxByteCount_Type()
)
adGenPseudowireCEMCurrent15MinTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinTxByteCount.setStatus("current")
_AdGenPseudowireCEMCurrent15MinRxByteCount_Type = Counter64
_AdGenPseudowireCEMCurrent15MinRxByteCount_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinRxByteCount = _AdGenPseudowireCEMCurrent15MinRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 8),
    _AdGenPseudowireCEMCurrent15MinRxByteCount_Type()
)
adGenPseudowireCEMCurrent15MinRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinRxByteCount.setStatus("current")
_AdGenPseudowireCEMCurrent15MinJitterBufferUnderrun_Type = Gauge32
_AdGenPseudowireCEMCurrent15MinJitterBufferUnderrun_Object = MibTableColumn
adGenPseudowireCEMCurrent15MinJitterBufferUnderrun = _AdGenPseudowireCEMCurrent15MinJitterBufferUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 1, 1, 9),
    _AdGenPseudowireCEMCurrent15MinJitterBufferUnderrun_Type()
)
adGenPseudowireCEMCurrent15MinJitterBufferUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent15MinJitterBufferUnderrun.setStatus("current")
_AdGenPseudowireCEMCurrent24HrPerfTable_Object = MibTable
adGenPseudowireCEMCurrent24HrPerfTable = _AdGenPseudowireCEMCurrent24HrPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrPerfTable.setStatus("current")
_AdGenPseudowireCEMCurrent24HrPerfTableEntry_Object = MibTableRow
adGenPseudowireCEMCurrent24HrPerfTableEntry = _AdGenPseudowireCEMCurrent24HrPerfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1)
)
adGenPseudowireCEMCurrent24HrPerfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrPerfTableEntry.setStatus("current")
_AdGenPseudowireCEMCurrent24HrPacketsMissed_Type = Gauge32
_AdGenPseudowireCEMCurrent24HrPacketsMissed_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrPacketsMissed = _AdGenPseudowireCEMCurrent24HrPacketsMissed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 1),
    _AdGenPseudowireCEMCurrent24HrPacketsMissed_Type()
)
adGenPseudowireCEMCurrent24HrPacketsMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrPacketsMissed.setStatus("current")
_AdGenPseudowireCEMCurrent24HrPacketsDropped_Type = Gauge32
_AdGenPseudowireCEMCurrent24HrPacketsDropped_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrPacketsDropped = _AdGenPseudowireCEMCurrent24HrPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 2),
    _AdGenPseudowireCEMCurrent24HrPacketsDropped_Type()
)
adGenPseudowireCEMCurrent24HrPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrPacketsDropped.setStatus("current")
_AdGenPseudowireCEMCurrent24HrPacketsMalformed_Type = Gauge32
_AdGenPseudowireCEMCurrent24HrPacketsMalformed_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrPacketsMalformed = _AdGenPseudowireCEMCurrent24HrPacketsMalformed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 3),
    _AdGenPseudowireCEMCurrent24HrPacketsMalformed_Type()
)
adGenPseudowireCEMCurrent24HrPacketsMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrPacketsMalformed.setStatus("current")
_AdGenPseudowireCEMCurrent24HrFailureCount_Type = Gauge32
_AdGenPseudowireCEMCurrent24HrFailureCount_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrFailureCount = _AdGenPseudowireCEMCurrent24HrFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 4),
    _AdGenPseudowireCEMCurrent24HrFailureCount_Type()
)
adGenPseudowireCEMCurrent24HrFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrFailureCount.setStatus("current")
_AdGenPseudowireCEMCurrent24HrTxPacketCount_Type = Gauge32
_AdGenPseudowireCEMCurrent24HrTxPacketCount_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrTxPacketCount = _AdGenPseudowireCEMCurrent24HrTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 5),
    _AdGenPseudowireCEMCurrent24HrTxPacketCount_Type()
)
adGenPseudowireCEMCurrent24HrTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrTxPacketCount.setStatus("current")
_AdGenPseudowireCEMCurrent24HrRxPacketCount_Type = Gauge32
_AdGenPseudowireCEMCurrent24HrRxPacketCount_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrRxPacketCount = _AdGenPseudowireCEMCurrent24HrRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 6),
    _AdGenPseudowireCEMCurrent24HrRxPacketCount_Type()
)
adGenPseudowireCEMCurrent24HrRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrRxPacketCount.setStatus("current")
_AdGenPseudowireCEMCurrent24HrTxByteCount_Type = Counter64
_AdGenPseudowireCEMCurrent24HrTxByteCount_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrTxByteCount = _AdGenPseudowireCEMCurrent24HrTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 7),
    _AdGenPseudowireCEMCurrent24HrTxByteCount_Type()
)
adGenPseudowireCEMCurrent24HrTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrTxByteCount.setStatus("current")
_AdGenPseudowireCEMCurrent24HrRxByteCount_Type = Counter64
_AdGenPseudowireCEMCurrent24HrRxByteCount_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrRxByteCount = _AdGenPseudowireCEMCurrent24HrRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 8),
    _AdGenPseudowireCEMCurrent24HrRxByteCount_Type()
)
adGenPseudowireCEMCurrent24HrRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrRxByteCount.setStatus("current")
_AdGenPseudowireCEMCurrent24HrJitterBufferUnderrun_Type = Gauge32
_AdGenPseudowireCEMCurrent24HrJitterBufferUnderrun_Object = MibTableColumn
adGenPseudowireCEMCurrent24HrJitterBufferUnderrun = _AdGenPseudowireCEMCurrent24HrJitterBufferUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 2, 1, 9),
    _AdGenPseudowireCEMCurrent24HrJitterBufferUnderrun_Type()
)
adGenPseudowireCEMCurrent24HrJitterBufferUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCurrent24HrJitterBufferUnderrun.setStatus("current")
_AdGenPseudowireCEMInterval15MinPerfTable_Object = MibTable
adGenPseudowireCEMInterval15MinPerfTable = _AdGenPseudowireCEMInterval15MinPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinPerfTable.setStatus("current")
_AdGenPseudowireCEMInterval15MinPerfTableEntry_Object = MibTableRow
adGenPseudowireCEMInterval15MinPerfTableEntry = _AdGenPseudowireCEMInterval15MinPerfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1)
)
adGenPseudowireCEMInterval15MinPerfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-INFO-MIB", "adGenPseudowireCEMIntervalNumber15Min"),
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinPerfTableEntry.setStatus("current")


class _AdGenPseudowireCEMIntervalNumber15Min_Type(Integer32):
    """Custom type adGenPseudowireCEMIntervalNumber15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenPseudowireCEMIntervalNumber15Min_Type.__name__ = "Integer32"
_AdGenPseudowireCEMIntervalNumber15Min_Object = MibTableColumn
adGenPseudowireCEMIntervalNumber15Min = _AdGenPseudowireCEMIntervalNumber15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 1),
    _AdGenPseudowireCEMIntervalNumber15Min_Type()
)
adGenPseudowireCEMIntervalNumber15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMIntervalNumber15Min.setStatus("current")
_AdGenPseudowireCEMInterval15MinPacketsMissed_Type = Gauge32
_AdGenPseudowireCEMInterval15MinPacketsMissed_Object = MibTableColumn
adGenPseudowireCEMInterval15MinPacketsMissed = _AdGenPseudowireCEMInterval15MinPacketsMissed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 2),
    _AdGenPseudowireCEMInterval15MinPacketsMissed_Type()
)
adGenPseudowireCEMInterval15MinPacketsMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinPacketsMissed.setStatus("current")
_AdGenPseudowireCEMInterval15MinPacketsDropped_Type = Gauge32
_AdGenPseudowireCEMInterval15MinPacketsDropped_Object = MibTableColumn
adGenPseudowireCEMInterval15MinPacketsDropped = _AdGenPseudowireCEMInterval15MinPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 3),
    _AdGenPseudowireCEMInterval15MinPacketsDropped_Type()
)
adGenPseudowireCEMInterval15MinPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinPacketsDropped.setStatus("current")
_AdGenPseudowireCEMInterval15MinPacketsMalformed_Type = Gauge32
_AdGenPseudowireCEMInterval15MinPacketsMalformed_Object = MibTableColumn
adGenPseudowireCEMInterval15MinPacketsMalformed = _AdGenPseudowireCEMInterval15MinPacketsMalformed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 4),
    _AdGenPseudowireCEMInterval15MinPacketsMalformed_Type()
)
adGenPseudowireCEMInterval15MinPacketsMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinPacketsMalformed.setStatus("current")
_AdGenPseudowireCEMInterval15MinFailureCount_Type = Gauge32
_AdGenPseudowireCEMInterval15MinFailureCount_Object = MibTableColumn
adGenPseudowireCEMInterval15MinFailureCount = _AdGenPseudowireCEMInterval15MinFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 5),
    _AdGenPseudowireCEMInterval15MinFailureCount_Type()
)
adGenPseudowireCEMInterval15MinFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinFailureCount.setStatus("current")
_AdGenPseudowireCEMInterval15MinTxPacketCount_Type = Gauge32
_AdGenPseudowireCEMInterval15MinTxPacketCount_Object = MibTableColumn
adGenPseudowireCEMInterval15MinTxPacketCount = _AdGenPseudowireCEMInterval15MinTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 6),
    _AdGenPseudowireCEMInterval15MinTxPacketCount_Type()
)
adGenPseudowireCEMInterval15MinTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinTxPacketCount.setStatus("current")
_AdGenPseudowireCEMInterval15MinRxPacketCount_Type = Gauge32
_AdGenPseudowireCEMInterval15MinRxPacketCount_Object = MibTableColumn
adGenPseudowireCEMInterval15MinRxPacketCount = _AdGenPseudowireCEMInterval15MinRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 7),
    _AdGenPseudowireCEMInterval15MinRxPacketCount_Type()
)
adGenPseudowireCEMInterval15MinRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinRxPacketCount.setStatus("current")
_AdGenPseudowireCEMInterval15MinTxByteCount_Type = Counter64
_AdGenPseudowireCEMInterval15MinTxByteCount_Object = MibTableColumn
adGenPseudowireCEMInterval15MinTxByteCount = _AdGenPseudowireCEMInterval15MinTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 8),
    _AdGenPseudowireCEMInterval15MinTxByteCount_Type()
)
adGenPseudowireCEMInterval15MinTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinTxByteCount.setStatus("current")
_AdGenPseudowireCEMInterval15MinRxByteCount_Type = Counter64
_AdGenPseudowireCEMInterval15MinRxByteCount_Object = MibTableColumn
adGenPseudowireCEMInterval15MinRxByteCount = _AdGenPseudowireCEMInterval15MinRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 9),
    _AdGenPseudowireCEMInterval15MinRxByteCount_Type()
)
adGenPseudowireCEMInterval15MinRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinRxByteCount.setStatus("current")
_AdGenPseudowireCEMInterval15MinJitterBufferUnderrun_Type = Gauge32
_AdGenPseudowireCEMInterval15MinJitterBufferUnderrun_Object = MibTableColumn
adGenPseudowireCEMInterval15MinJitterBufferUnderrun = _AdGenPseudowireCEMInterval15MinJitterBufferUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 3, 1, 10),
    _AdGenPseudowireCEMInterval15MinJitterBufferUnderrun_Type()
)
adGenPseudowireCEMInterval15MinJitterBufferUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval15MinJitterBufferUnderrun.setStatus("current")
_AdGenPseudowireCEMInterval24HrPerfTable_Object = MibTable
adGenPseudowireCEMInterval24HrPerfTable = _AdGenPseudowireCEMInterval24HrPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrPerfTable.setStatus("current")
_AdGenPseudowireCEMInterval24HrPerfTableEntry_Object = MibTableRow
adGenPseudowireCEMInterval24HrPerfTableEntry = _AdGenPseudowireCEMInterval24HrPerfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1)
)
adGenPseudowireCEMInterval24HrPerfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-INFO-MIB", "adGenPseudowireCEMIntervalNumber24Hr"),
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrPerfTableEntry.setStatus("current")


class _AdGenPseudowireCEMIntervalNumber24Hr_Type(Integer32):
    """Custom type adGenPseudowireCEMIntervalNumber24Hr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenPseudowireCEMIntervalNumber24Hr_Type.__name__ = "Integer32"
_AdGenPseudowireCEMIntervalNumber24Hr_Object = MibTableColumn
adGenPseudowireCEMIntervalNumber24Hr = _AdGenPseudowireCEMIntervalNumber24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 1),
    _AdGenPseudowireCEMIntervalNumber24Hr_Type()
)
adGenPseudowireCEMIntervalNumber24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMIntervalNumber24Hr.setStatus("current")
_AdGenPseudowireCEMInterval24HrPacketsMissed_Type = Gauge32
_AdGenPseudowireCEMInterval24HrPacketsMissed_Object = MibTableColumn
adGenPseudowireCEMInterval24HrPacketsMissed = _AdGenPseudowireCEMInterval24HrPacketsMissed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 2),
    _AdGenPseudowireCEMInterval24HrPacketsMissed_Type()
)
adGenPseudowireCEMInterval24HrPacketsMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrPacketsMissed.setStatus("current")
_AdGenPseudowireCEMInterval24HrPacketsDropped_Type = Gauge32
_AdGenPseudowireCEMInterval24HrPacketsDropped_Object = MibTableColumn
adGenPseudowireCEMInterval24HrPacketsDropped = _AdGenPseudowireCEMInterval24HrPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 3),
    _AdGenPseudowireCEMInterval24HrPacketsDropped_Type()
)
adGenPseudowireCEMInterval24HrPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrPacketsDropped.setStatus("current")
_AdGenPseudowireCEMInterval24HrPacketsMalformed_Type = Gauge32
_AdGenPseudowireCEMInterval24HrPacketsMalformed_Object = MibTableColumn
adGenPseudowireCEMInterval24HrPacketsMalformed = _AdGenPseudowireCEMInterval24HrPacketsMalformed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 4),
    _AdGenPseudowireCEMInterval24HrPacketsMalformed_Type()
)
adGenPseudowireCEMInterval24HrPacketsMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrPacketsMalformed.setStatus("current")
_AdGenPseudowireCEMInterval24HrFailureCount_Type = Gauge32
_AdGenPseudowireCEMInterval24HrFailureCount_Object = MibTableColumn
adGenPseudowireCEMInterval24HrFailureCount = _AdGenPseudowireCEMInterval24HrFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 5),
    _AdGenPseudowireCEMInterval24HrFailureCount_Type()
)
adGenPseudowireCEMInterval24HrFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrFailureCount.setStatus("current")
_AdGenPseudowireCEMInterval24HrTxPacketCount_Type = Gauge32
_AdGenPseudowireCEMInterval24HrTxPacketCount_Object = MibTableColumn
adGenPseudowireCEMInterval24HrTxPacketCount = _AdGenPseudowireCEMInterval24HrTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 6),
    _AdGenPseudowireCEMInterval24HrTxPacketCount_Type()
)
adGenPseudowireCEMInterval24HrTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrTxPacketCount.setStatus("current")
_AdGenPseudowireCEMInterval24HrRxPacketCount_Type = Gauge32
_AdGenPseudowireCEMInterval24HrRxPacketCount_Object = MibTableColumn
adGenPseudowireCEMInterval24HrRxPacketCount = _AdGenPseudowireCEMInterval24HrRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 7),
    _AdGenPseudowireCEMInterval24HrRxPacketCount_Type()
)
adGenPseudowireCEMInterval24HrRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrRxPacketCount.setStatus("current")
_AdGenPseudowireCEMInterval24HrTxByteCount_Type = Counter64
_AdGenPseudowireCEMInterval24HrTxByteCount_Object = MibTableColumn
adGenPseudowireCEMInterval24HrTxByteCount = _AdGenPseudowireCEMInterval24HrTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 8),
    _AdGenPseudowireCEMInterval24HrTxByteCount_Type()
)
adGenPseudowireCEMInterval24HrTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrTxByteCount.setStatus("current")
_AdGenPseudowireCEMInterval24HrRxByteCount_Type = Counter64
_AdGenPseudowireCEMInterval24HrRxByteCount_Object = MibTableColumn
adGenPseudowireCEMInterval24HrRxByteCount = _AdGenPseudowireCEMInterval24HrRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 9),
    _AdGenPseudowireCEMInterval24HrRxByteCount_Type()
)
adGenPseudowireCEMInterval24HrRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrRxByteCount.setStatus("current")
_AdGenPseudowireCEMInterval24HrJitterBufferUnderrun_Type = Gauge32
_AdGenPseudowireCEMInterval24HrJitterBufferUnderrun_Object = MibTableColumn
adGenPseudowireCEMInterval24HrJitterBufferUnderrun = _AdGenPseudowireCEMInterval24HrJitterBufferUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2, 4, 1, 10),
    _AdGenPseudowireCEMInterval24HrJitterBufferUnderrun_Type()
)
adGenPseudowireCEMInterval24HrJitterBufferUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMInterval24HrJitterBufferUnderrun.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-INFO-MIB",
    **{"adGenPseudowireCEMCurrent15MinPerfTable": adGenPseudowireCEMCurrent15MinPerfTable,
       "adGenPseudowireCEMCurrent15MinPerfTableEntry": adGenPseudowireCEMCurrent15MinPerfTableEntry,
       "adGenPseudowireCEMCurrent15MinPacketsMissed": adGenPseudowireCEMCurrent15MinPacketsMissed,
       "adGenPseudowireCEMCurrent15MinPacketsDropped": adGenPseudowireCEMCurrent15MinPacketsDropped,
       "adGenPseudowireCEMCurrent15MinPacketsMalformed": adGenPseudowireCEMCurrent15MinPacketsMalformed,
       "adGenPseudowireCEMCurrent15MinFailureCount": adGenPseudowireCEMCurrent15MinFailureCount,
       "adGenPseudowireCEMCurrent15MinTxPacketCount": adGenPseudowireCEMCurrent15MinTxPacketCount,
       "adGenPseudowireCEMCurrent15MinRxPacketCount": adGenPseudowireCEMCurrent15MinRxPacketCount,
       "adGenPseudowireCEMCurrent15MinTxByteCount": adGenPseudowireCEMCurrent15MinTxByteCount,
       "adGenPseudowireCEMCurrent15MinRxByteCount": adGenPseudowireCEMCurrent15MinRxByteCount,
       "adGenPseudowireCEMCurrent15MinJitterBufferUnderrun": adGenPseudowireCEMCurrent15MinJitterBufferUnderrun,
       "adGenPseudowireCEMCurrent24HrPerfTable": adGenPseudowireCEMCurrent24HrPerfTable,
       "adGenPseudowireCEMCurrent24HrPerfTableEntry": adGenPseudowireCEMCurrent24HrPerfTableEntry,
       "adGenPseudowireCEMCurrent24HrPacketsMissed": adGenPseudowireCEMCurrent24HrPacketsMissed,
       "adGenPseudowireCEMCurrent24HrPacketsDropped": adGenPseudowireCEMCurrent24HrPacketsDropped,
       "adGenPseudowireCEMCurrent24HrPacketsMalformed": adGenPseudowireCEMCurrent24HrPacketsMalformed,
       "adGenPseudowireCEMCurrent24HrFailureCount": adGenPseudowireCEMCurrent24HrFailureCount,
       "adGenPseudowireCEMCurrent24HrTxPacketCount": adGenPseudowireCEMCurrent24HrTxPacketCount,
       "adGenPseudowireCEMCurrent24HrRxPacketCount": adGenPseudowireCEMCurrent24HrRxPacketCount,
       "adGenPseudowireCEMCurrent24HrTxByteCount": adGenPseudowireCEMCurrent24HrTxByteCount,
       "adGenPseudowireCEMCurrent24HrRxByteCount": adGenPseudowireCEMCurrent24HrRxByteCount,
       "adGenPseudowireCEMCurrent24HrJitterBufferUnderrun": adGenPseudowireCEMCurrent24HrJitterBufferUnderrun,
       "adGenPseudowireCEMInterval15MinPerfTable": adGenPseudowireCEMInterval15MinPerfTable,
       "adGenPseudowireCEMInterval15MinPerfTableEntry": adGenPseudowireCEMInterval15MinPerfTableEntry,
       "adGenPseudowireCEMIntervalNumber15Min": adGenPseudowireCEMIntervalNumber15Min,
       "adGenPseudowireCEMInterval15MinPacketsMissed": adGenPseudowireCEMInterval15MinPacketsMissed,
       "adGenPseudowireCEMInterval15MinPacketsDropped": adGenPseudowireCEMInterval15MinPacketsDropped,
       "adGenPseudowireCEMInterval15MinPacketsMalformed": adGenPseudowireCEMInterval15MinPacketsMalformed,
       "adGenPseudowireCEMInterval15MinFailureCount": adGenPseudowireCEMInterval15MinFailureCount,
       "adGenPseudowireCEMInterval15MinTxPacketCount": adGenPseudowireCEMInterval15MinTxPacketCount,
       "adGenPseudowireCEMInterval15MinRxPacketCount": adGenPseudowireCEMInterval15MinRxPacketCount,
       "adGenPseudowireCEMInterval15MinTxByteCount": adGenPseudowireCEMInterval15MinTxByteCount,
       "adGenPseudowireCEMInterval15MinRxByteCount": adGenPseudowireCEMInterval15MinRxByteCount,
       "adGenPseudowireCEMInterval15MinJitterBufferUnderrun": adGenPseudowireCEMInterval15MinJitterBufferUnderrun,
       "adGenPseudowireCEMInterval24HrPerfTable": adGenPseudowireCEMInterval24HrPerfTable,
       "adGenPseudowireCEMInterval24HrPerfTableEntry": adGenPseudowireCEMInterval24HrPerfTableEntry,
       "adGenPseudowireCEMIntervalNumber24Hr": adGenPseudowireCEMIntervalNumber24Hr,
       "adGenPseudowireCEMInterval24HrPacketsMissed": adGenPseudowireCEMInterval24HrPacketsMissed,
       "adGenPseudowireCEMInterval24HrPacketsDropped": adGenPseudowireCEMInterval24HrPacketsDropped,
       "adGenPseudowireCEMInterval24HrPacketsMalformed": adGenPseudowireCEMInterval24HrPacketsMalformed,
       "adGenPseudowireCEMInterval24HrFailureCount": adGenPseudowireCEMInterval24HrFailureCount,
       "adGenPseudowireCEMInterval24HrTxPacketCount": adGenPseudowireCEMInterval24HrTxPacketCount,
       "adGenPseudowireCEMInterval24HrRxPacketCount": adGenPseudowireCEMInterval24HrRxPacketCount,
       "adGenPseudowireCEMInterval24HrTxByteCount": adGenPseudowireCEMInterval24HrTxByteCount,
       "adGenPseudowireCEMInterval24HrRxByteCount": adGenPseudowireCEMInterval24HrRxByteCount,
       "adGenPseudowireCEMInterval24HrJitterBufferUnderrun": adGenPseudowireCEMInterval24HrJitterBufferUnderrun,
       "adGenPseudowireCEMPerfInfoModuleIdentity": adGenPseudowireCEMPerfInfoModuleIdentity}
)
