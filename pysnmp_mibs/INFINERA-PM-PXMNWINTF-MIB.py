# SNMP MIB module (INFINERA-PM-PXMNWINTF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-PXMNWINTF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:02 2025
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

(HCPerfIntervalCount,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfIntervalCount")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(perfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "perfMon")

(FloatHundredths,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnServiceType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pxmNwIntfPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98)
)
if mibBuilder.loadTexts:
    pxmNwIntfPmMIB.setRevisions(
        ("2014-02-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmNwIntfRmonPm_ObjectIdentity = ObjectIdentity
pxmNwIntfRmonPm = _PxmNwIntfRmonPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1)
)
_PxmNwIntfPmRealTable_Object = MibTable
pxmNwIntfPmRealTable = _PxmNwIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 1)
)
if mibBuilder.loadTexts:
    pxmNwIntfPmRealTable.setStatus("current")
_PxmNwIntfPmRealEntry_Object = MibTableRow
pxmNwIntfPmRealEntry = _PxmNwIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 1, 1)
)
pxmNwIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmNwIntfPmRealEntry.setStatus("current")
_PxmNwIntfPmRealRxPackets_Type = Counter64
_PxmNwIntfPmRealRxPackets_Object = MibTableColumn
pxmNwIntfPmRealRxPackets = _PxmNwIntfPmRealRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 1, 1, 1),
    _PxmNwIntfPmRealRxPackets_Type()
)
pxmNwIntfPmRealRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmRealRxPackets.setStatus("current")
_PxmNwIntfPmRealTxPackets_Type = Counter64
_PxmNwIntfPmRealTxPackets_Object = MibTableColumn
pxmNwIntfPmRealTxPackets = _PxmNwIntfPmRealTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 1, 1, 2),
    _PxmNwIntfPmRealTxPackets_Type()
)
pxmNwIntfPmRealTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmRealTxPackets.setStatus("current")
_PxmNwIntfPmRealRxOctets_Type = Counter64
_PxmNwIntfPmRealRxOctets_Object = MibTableColumn
pxmNwIntfPmRealRxOctets = _PxmNwIntfPmRealRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 1, 1, 3),
    _PxmNwIntfPmRealRxOctets_Type()
)
pxmNwIntfPmRealRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmRealRxOctets.setStatus("current")
_PxmNwIntfPmRealTxOctets_Type = Counter64
_PxmNwIntfPmRealTxOctets_Object = MibTableColumn
pxmNwIntfPmRealTxOctets = _PxmNwIntfPmRealTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 1, 1, 4),
    _PxmNwIntfPmRealTxOctets_Type()
)
pxmNwIntfPmRealTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmRealTxOctets.setStatus("current")
_PxmNwIntfPmRealRxLU_Type = FloatHundredths
_PxmNwIntfPmRealRxLU_Object = MibTableColumn
pxmNwIntfPmRealRxLU = _PxmNwIntfPmRealRxLU_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 1, 1, 5),
    _PxmNwIntfPmRealRxLU_Type()
)
pxmNwIntfPmRealRxLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmRealRxLU.setStatus("current")
_PxmNwIntfPmRealTxLU_Type = FloatHundredths
_PxmNwIntfPmRealTxLU_Object = MibTableColumn
pxmNwIntfPmRealTxLU = _PxmNwIntfPmRealTxLU_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 1, 1, 6),
    _PxmNwIntfPmRealTxLU_Type()
)
pxmNwIntfPmRealTxLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmRealTxLU.setStatus("current")
_PxmNwIntfPmTable_Object = MibTable
pxmNwIntfPmTable = _PxmNwIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2)
)
if mibBuilder.loadTexts:
    pxmNwIntfPmTable.setStatus("current")
_PxmNwIntfPmEntry_Object = MibTableRow
pxmNwIntfPmEntry = _PxmNwIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2, 1)
)
pxmNwIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmNwIntfPmEntry.setStatus("current")


class _PxmNwIntfPmTimestamp_Type(Integer32):
    """Custom type pxmNwIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmNwIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmNwIntfPmTimestamp_Object = MibTableColumn
pxmNwIntfPmTimestamp = _PxmNwIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2, 1, 1),
    _PxmNwIntfPmTimestamp_Type()
)
pxmNwIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmNwIntfPmTimestamp.setStatus("current")


class _PxmNwIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmNwIntfPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_PxmNwIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmNwIntfPmSampleDuration_Object = MibTableColumn
pxmNwIntfPmSampleDuration = _PxmNwIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2, 1, 2),
    _PxmNwIntfPmSampleDuration_Type()
)
pxmNwIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmNwIntfPmSampleDuration.setStatus("current")
_PxmNwIntfPmValidity_Type = TruthValue
_PxmNwIntfPmValidity_Object = MibTableColumn
pxmNwIntfPmValidity = _PxmNwIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2, 1, 3),
    _PxmNwIntfPmValidity_Type()
)
pxmNwIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmValidity.setStatus("current")
_PxmNwIntfPmRxPackets_Type = HCPerfIntervalCount
_PxmNwIntfPmRxPackets_Object = MibTableColumn
pxmNwIntfPmRxPackets = _PxmNwIntfPmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2, 1, 4),
    _PxmNwIntfPmRxPackets_Type()
)
pxmNwIntfPmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmRxPackets.setStatus("current")
_PxmNwIntfPmTxPackets_Type = HCPerfIntervalCount
_PxmNwIntfPmTxPackets_Object = MibTableColumn
pxmNwIntfPmTxPackets = _PxmNwIntfPmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2, 1, 5),
    _PxmNwIntfPmTxPackets_Type()
)
pxmNwIntfPmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmTxPackets.setStatus("current")
_PxmNwIntfPmRxOctets_Type = HCPerfIntervalCount
_PxmNwIntfPmRxOctets_Object = MibTableColumn
pxmNwIntfPmRxOctets = _PxmNwIntfPmRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2, 1, 6),
    _PxmNwIntfPmRxOctets_Type()
)
pxmNwIntfPmRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmRxOctets.setStatus("current")
_PxmNwIntfPmTxOctets_Type = HCPerfIntervalCount
_PxmNwIntfPmTxOctets_Object = MibTableColumn
pxmNwIntfPmTxOctets = _PxmNwIntfPmTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 1, 2, 1, 7),
    _PxmNwIntfPmTxOctets_Type()
)
pxmNwIntfPmTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfPmTxOctets.setStatus("current")
_PxmCmNwIntfPmObjects_ObjectIdentity = ObjectIdentity
pxmCmNwIntfPmObjects = _PxmCmNwIntfPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2)
)
_PxmCmNwIntfRealPm_ObjectIdentity = ObjectIdentity
pxmCmNwIntfRealPm = _PxmCmNwIntfRealPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1)
)
_PxmTC0NwIntfPmRealTable_Object = MibTable
pxmTC0NwIntfPmRealTable = _PxmTC0NwIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealTable.setStatus("current")
_PxmTC0NwIntfPmRealEntry_Object = MibTableRow
pxmTC0NwIntfPmRealEntry = _PxmTC0NwIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1)
)
pxmTC0NwIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealEntry.setStatus("current")
_PxmTC0NwIntfPmRealTCNum_Type = Integer32
_PxmTC0NwIntfPmRealTCNum_Object = MibTableColumn
pxmTC0NwIntfPmRealTCNum = _PxmTC0NwIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 1),
    _PxmTC0NwIntfPmRealTCNum_Type()
)
pxmTC0NwIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealTCNum.setStatus("current")
_PxmTC0NwIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC0NwIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC0NwIntfPmRealTDQueuingCurrentQDepth = _PxmTC0NwIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 2),
    _PxmTC0NwIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC0NwIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC0NwIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC0NwIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC0NwIntfPmRealQueueingDiscardOctets = _PxmTC0NwIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 3),
    _PxmTC0NwIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC0NwIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC0NwIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC0NwIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC0NwIntfPmRealQueueingDiscardPkts = _PxmTC0NwIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 4),
    _PxmTC0NwIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC0NwIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC0NwIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC0NwIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC0NwIntfPmRealRandomGreenDropPkts = _PxmTC0NwIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 5),
    _PxmTC0NwIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC0NwIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC0NwIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC0NwIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC0NwIntfPmRealRandomGreenDropOctets = _PxmTC0NwIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 6),
    _PxmTC0NwIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC0NwIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC0NwIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC0NwIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC0NwIntfPmRealRandomYellowDropPkts = _PxmTC0NwIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 7),
    _PxmTC0NwIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC0NwIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC0NwIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC0NwIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC0NwIntfPmRealRandomYellowDropOctets = _PxmTC0NwIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 8),
    _PxmTC0NwIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC0NwIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC0NwIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC0NwIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC0NwIntfPmRealQueueingTransmitPkts = _PxmTC0NwIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 9),
    _PxmTC0NwIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC0NwIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC0NwIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC0NwIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC0NwIntfPmRealQueueingTransmitOctets = _PxmTC0NwIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 10),
    _PxmTC0NwIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC0NwIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC0NwIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC0NwIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC0NwIntfPmRealQueueingMeanQSizeUnit = _PxmTC0NwIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 11),
    _PxmTC0NwIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC0NwIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC0NwIntfPmRealMeanQSize_Type = Integer32
_PxmTC0NwIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC0NwIntfPmRealMeanQSize = _PxmTC0NwIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 1, 1, 12),
    _PxmTC0NwIntfPmRealMeanQSize_Type()
)
pxmTC0NwIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealMeanQSize.setStatus("current")
_PxmTC2NwIntfPmRealTable_Object = MibTable
pxmTC2NwIntfPmRealTable = _PxmTC2NwIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealTable.setStatus("current")
_PxmTC2NwIntfPmRealEntry_Object = MibTableRow
pxmTC2NwIntfPmRealEntry = _PxmTC2NwIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1)
)
pxmTC2NwIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealEntry.setStatus("current")
_PxmTC2NwIntfPmRealTCNum_Type = Integer32
_PxmTC2NwIntfPmRealTCNum_Object = MibTableColumn
pxmTC2NwIntfPmRealTCNum = _PxmTC2NwIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 1),
    _PxmTC2NwIntfPmRealTCNum_Type()
)
pxmTC2NwIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealTCNum.setStatus("current")
_PxmTC2NwIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC2NwIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC2NwIntfPmRealTDQueuingCurrentQDepth = _PxmTC2NwIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 2),
    _PxmTC2NwIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC2NwIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC2NwIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC2NwIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC2NwIntfPmRealQueueingDiscardOctets = _PxmTC2NwIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 3),
    _PxmTC2NwIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC2NwIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC2NwIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC2NwIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC2NwIntfPmRealQueueingDiscardPkts = _PxmTC2NwIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 4),
    _PxmTC2NwIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC2NwIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC2NwIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC2NwIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC2NwIntfPmRealRandomGreenDropPkts = _PxmTC2NwIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 5),
    _PxmTC2NwIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC2NwIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC2NwIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC2NwIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC2NwIntfPmRealRandomGreenDropOctets = _PxmTC2NwIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 6),
    _PxmTC2NwIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC2NwIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC2NwIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC2NwIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC2NwIntfPmRealRandomYellowDropPkts = _PxmTC2NwIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 7),
    _PxmTC2NwIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC2NwIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC2NwIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC2NwIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC2NwIntfPmRealRandomYellowDropOctets = _PxmTC2NwIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 8),
    _PxmTC2NwIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC2NwIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC2NwIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC2NwIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC2NwIntfPmRealQueueingTransmitPkts = _PxmTC2NwIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 9),
    _PxmTC2NwIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC2NwIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC2NwIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC2NwIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC2NwIntfPmRealQueueingTransmitOctets = _PxmTC2NwIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 10),
    _PxmTC2NwIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC2NwIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC2NwIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC2NwIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC2NwIntfPmRealQueueingMeanQSizeUnit = _PxmTC2NwIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 11),
    _PxmTC2NwIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC2NwIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC2NwIntfPmRealMeanQSize_Type = Integer32
_PxmTC2NwIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC2NwIntfPmRealMeanQSize = _PxmTC2NwIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 2, 1, 12),
    _PxmTC2NwIntfPmRealMeanQSize_Type()
)
pxmTC2NwIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealMeanQSize.setStatus("current")
_PxmTC4NwIntfPmRealTable_Object = MibTable
pxmTC4NwIntfPmRealTable = _PxmTC4NwIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealTable.setStatus("current")
_PxmTC4NwIntfPmRealEntry_Object = MibTableRow
pxmTC4NwIntfPmRealEntry = _PxmTC4NwIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1)
)
pxmTC4NwIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealEntry.setStatus("current")
_PxmTC4NwIntfPmRealTCNum_Type = Integer32
_PxmTC4NwIntfPmRealTCNum_Object = MibTableColumn
pxmTC4NwIntfPmRealTCNum = _PxmTC4NwIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 1),
    _PxmTC4NwIntfPmRealTCNum_Type()
)
pxmTC4NwIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealTCNum.setStatus("current")
_PxmTC4NwIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC4NwIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC4NwIntfPmRealTDQueuingCurrentQDepth = _PxmTC4NwIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 2),
    _PxmTC4NwIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC4NwIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC4NwIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC4NwIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC4NwIntfPmRealQueueingDiscardOctets = _PxmTC4NwIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 3),
    _PxmTC4NwIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC4NwIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC4NwIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC4NwIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC4NwIntfPmRealQueueingDiscardPkts = _PxmTC4NwIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 4),
    _PxmTC4NwIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC4NwIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC4NwIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC4NwIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC4NwIntfPmRealRandomGreenDropPkts = _PxmTC4NwIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 5),
    _PxmTC4NwIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC4NwIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC4NwIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC4NwIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC4NwIntfPmRealRandomGreenDropOctets = _PxmTC4NwIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 6),
    _PxmTC4NwIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC4NwIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC4NwIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC4NwIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC4NwIntfPmRealRandomYellowDropPkts = _PxmTC4NwIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 7),
    _PxmTC4NwIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC4NwIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC4NwIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC4NwIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC4NwIntfPmRealRandomYellowDropOctets = _PxmTC4NwIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 8),
    _PxmTC4NwIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC4NwIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC4NwIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC4NwIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC4NwIntfPmRealQueueingTransmitPkts = _PxmTC4NwIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 9),
    _PxmTC4NwIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC4NwIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC4NwIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC4NwIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC4NwIntfPmRealQueueingTransmitOctets = _PxmTC4NwIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 10),
    _PxmTC4NwIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC4NwIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC4NwIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC4NwIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC4NwIntfPmRealQueueingMeanQSizeUnit = _PxmTC4NwIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 11),
    _PxmTC4NwIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC4NwIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC4NwIntfPmRealMeanQSize_Type = Integer32
_PxmTC4NwIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC4NwIntfPmRealMeanQSize = _PxmTC4NwIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 3, 1, 12),
    _PxmTC4NwIntfPmRealMeanQSize_Type()
)
pxmTC4NwIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealMeanQSize.setStatus("current")
_PxmTC6NwIntfPmRealTable_Object = MibTable
pxmTC6NwIntfPmRealTable = _PxmTC6NwIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4)
)
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealTable.setStatus("current")
_PxmTC6NwIntfPmRealEntry_Object = MibTableRow
pxmTC6NwIntfPmRealEntry = _PxmTC6NwIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1)
)
pxmTC6NwIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealEntry.setStatus("current")
_PxmTC6NwIntfPmRealTCNum_Type = Integer32
_PxmTC6NwIntfPmRealTCNum_Object = MibTableColumn
pxmTC6NwIntfPmRealTCNum = _PxmTC6NwIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 1),
    _PxmTC6NwIntfPmRealTCNum_Type()
)
pxmTC6NwIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealTCNum.setStatus("current")
_PxmTC6NwIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC6NwIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC6NwIntfPmRealTDQueuingCurrentQDepth = _PxmTC6NwIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 2),
    _PxmTC6NwIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC6NwIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC6NwIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC6NwIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC6NwIntfPmRealQueueingDiscardOctets = _PxmTC6NwIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 3),
    _PxmTC6NwIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC6NwIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC6NwIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC6NwIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC6NwIntfPmRealQueueingDiscardPkts = _PxmTC6NwIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 4),
    _PxmTC6NwIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC6NwIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC6NwIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC6NwIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC6NwIntfPmRealRandomGreenDropPkts = _PxmTC6NwIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 5),
    _PxmTC6NwIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC6NwIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC6NwIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC6NwIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC6NwIntfPmRealRandomGreenDropOctets = _PxmTC6NwIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 6),
    _PxmTC6NwIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC6NwIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC6NwIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC6NwIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC6NwIntfPmRealRandomYellowDropPkts = _PxmTC6NwIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 7),
    _PxmTC6NwIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC6NwIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC6NwIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC6NwIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC6NwIntfPmRealRandomYellowDropOctets = _PxmTC6NwIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 8),
    _PxmTC6NwIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC6NwIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC6NwIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC6NwIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC6NwIntfPmRealQueueingTransmitPkts = _PxmTC6NwIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 9),
    _PxmTC6NwIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC6NwIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC6NwIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC6NwIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC6NwIntfPmRealQueueingTransmitOctets = _PxmTC6NwIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 10),
    _PxmTC6NwIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC6NwIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC6NwIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC6NwIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC6NwIntfPmRealQueueingMeanQSizeUnit = _PxmTC6NwIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 11),
    _PxmTC6NwIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC6NwIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC6NwIntfPmRealMeanQSize_Type = Integer32
_PxmTC6NwIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC6NwIntfPmRealMeanQSize = _PxmTC6NwIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 4, 1, 12),
    _PxmTC6NwIntfPmRealMeanQSize_Type()
)
pxmTC6NwIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealMeanQSize.setStatus("current")
_PxmTC7NwIntfPmRealTable_Object = MibTable
pxmTC7NwIntfPmRealTable = _PxmTC7NwIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5)
)
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealTable.setStatus("current")
_PxmTC7NwIntfPmRealEntry_Object = MibTableRow
pxmTC7NwIntfPmRealEntry = _PxmTC7NwIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1)
)
pxmTC7NwIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealEntry.setStatus("current")
_PxmTC7NwIntfPmRealTCNum_Type = Integer32
_PxmTC7NwIntfPmRealTCNum_Object = MibTableColumn
pxmTC7NwIntfPmRealTCNum = _PxmTC7NwIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 1),
    _PxmTC7NwIntfPmRealTCNum_Type()
)
pxmTC7NwIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealTCNum.setStatus("current")
_PxmTC7NwIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC7NwIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC7NwIntfPmRealTDQueuingCurrentQDepth = _PxmTC7NwIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 2),
    _PxmTC7NwIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC7NwIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC7NwIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC7NwIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC7NwIntfPmRealQueueingDiscardOctets = _PxmTC7NwIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 3),
    _PxmTC7NwIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC7NwIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC7NwIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC7NwIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC7NwIntfPmRealQueueingDiscardPkts = _PxmTC7NwIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 4),
    _PxmTC7NwIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC7NwIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC7NwIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC7NwIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC7NwIntfPmRealRandomGreenDropPkts = _PxmTC7NwIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 5),
    _PxmTC7NwIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC7NwIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC7NwIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC7NwIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC7NwIntfPmRealRandomGreenDropOctets = _PxmTC7NwIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 6),
    _PxmTC7NwIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC7NwIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC7NwIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC7NwIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC7NwIntfPmRealRandomYellowDropPkts = _PxmTC7NwIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 7),
    _PxmTC7NwIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC7NwIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC7NwIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC7NwIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC7NwIntfPmRealRandomYellowDropOctets = _PxmTC7NwIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 8),
    _PxmTC7NwIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC7NwIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC7NwIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC7NwIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC7NwIntfPmRealQueueingTransmitPkts = _PxmTC7NwIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 9),
    _PxmTC7NwIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC7NwIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC7NwIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC7NwIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC7NwIntfPmRealQueueingTransmitOctets = _PxmTC7NwIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 10),
    _PxmTC7NwIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC7NwIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC7NwIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC7NwIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC7NwIntfPmRealQueueingMeanQSizeUnit = _PxmTC7NwIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 11),
    _PxmTC7NwIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC7NwIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC7NwIntfPmRealMeanQSize_Type = Integer32
_PxmTC7NwIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC7NwIntfPmRealMeanQSize = _PxmTC7NwIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 5, 1, 12),
    _PxmTC7NwIntfPmRealMeanQSize_Type()
)
pxmTC7NwIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealMeanQSize.setStatus("current")
_PxmTCANYNwIntfPmRealTable_Object = MibTable
pxmTCANYNwIntfPmRealTable = _PxmTCANYNwIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6)
)
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealTable.setStatus("current")
_PxmTCANYNwIntfPmRealEntry_Object = MibTableRow
pxmTCANYNwIntfPmRealEntry = _PxmTCANYNwIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1)
)
pxmTCANYNwIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealEntry.setStatus("current")
_PxmTCANYNwIntfPmRealTCNum_Type = Integer32
_PxmTCANYNwIntfPmRealTCNum_Object = MibTableColumn
pxmTCANYNwIntfPmRealTCNum = _PxmTCANYNwIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 1),
    _PxmTCANYNwIntfPmRealTCNum_Type()
)
pxmTCANYNwIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealTCNum.setStatus("current")
_PxmTCANYNwIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTCANYNwIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTCANYNwIntfPmRealTDQueuingCurrentQDepth = _PxmTCANYNwIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 2),
    _PxmTCANYNwIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTCANYNwIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTCANYNwIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTCANYNwIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTCANYNwIntfPmRealQueueingDiscardOctets = _PxmTCANYNwIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 3),
    _PxmTCANYNwIntfPmRealQueueingDiscardOctets_Type()
)
pxmTCANYNwIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTCANYNwIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTCANYNwIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTCANYNwIntfPmRealQueueingDiscardPkts = _PxmTCANYNwIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 4),
    _PxmTCANYNwIntfPmRealQueueingDiscardPkts_Type()
)
pxmTCANYNwIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTCANYNwIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTCANYNwIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTCANYNwIntfPmRealRandomGreenDropPkts = _PxmTCANYNwIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 5),
    _PxmTCANYNwIntfPmRealRandomGreenDropPkts_Type()
)
pxmTCANYNwIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTCANYNwIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTCANYNwIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTCANYNwIntfPmRealRandomGreenDropOctets = _PxmTCANYNwIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 6),
    _PxmTCANYNwIntfPmRealRandomGreenDropOctets_Type()
)
pxmTCANYNwIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTCANYNwIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTCANYNwIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTCANYNwIntfPmRealRandomYellowDropPkts = _PxmTCANYNwIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 7),
    _PxmTCANYNwIntfPmRealRandomYellowDropPkts_Type()
)
pxmTCANYNwIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTCANYNwIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTCANYNwIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTCANYNwIntfPmRealRandomYellowDropOctets = _PxmTCANYNwIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 8),
    _PxmTCANYNwIntfPmRealRandomYellowDropOctets_Type()
)
pxmTCANYNwIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTCANYNwIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTCANYNwIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTCANYNwIntfPmRealQueueingTransmitPkts = _PxmTCANYNwIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 9),
    _PxmTCANYNwIntfPmRealQueueingTransmitPkts_Type()
)
pxmTCANYNwIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTCANYNwIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTCANYNwIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTCANYNwIntfPmRealQueueingTransmitOctets = _PxmTCANYNwIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 10),
    _PxmTCANYNwIntfPmRealQueueingTransmitOctets_Type()
)
pxmTCANYNwIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTCANYNwIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTCANYNwIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTCANYNwIntfPmRealQueueingMeanQSizeUnit = _PxmTCANYNwIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 11),
    _PxmTCANYNwIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTCANYNwIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTCANYNwIntfPmRealMeanQSize_Type = Integer32
_PxmTCANYNwIntfPmRealMeanQSize_Object = MibTableColumn
pxmTCANYNwIntfPmRealMeanQSize = _PxmTCANYNwIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 1, 6, 1, 12),
    _PxmTCANYNwIntfPmRealMeanQSize_Type()
)
pxmTCANYNwIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealMeanQSize.setStatus("current")
_PxmCmNwIntfPm_ObjectIdentity = ObjectIdentity
pxmCmNwIntfPm = _PxmCmNwIntfPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2)
)
_PxmTC0NwIntfPmTable_Object = MibTable
pxmTC0NwIntfPmTable = _PxmTC0NwIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmTable.setStatus("current")
_PxmTC0NwIntfPmEntry_Object = MibTableRow
pxmTC0NwIntfPmEntry = _PxmTC0NwIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1)
)
pxmTC0NwIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmEntry.setStatus("current")


class _PxmTC0NwIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC0NwIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC0NwIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC0NwIntfPmTimestamp_Object = MibTableColumn
pxmTC0NwIntfPmTimestamp = _PxmTC0NwIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 1),
    _PxmTC0NwIntfPmTimestamp_Type()
)
pxmTC0NwIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmTimestamp.setStatus("current")


class _PxmTC0NwIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC0NwIntfPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_PxmTC0NwIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC0NwIntfPmSampleDuration_Object = MibTableColumn
pxmTC0NwIntfPmSampleDuration = _PxmTC0NwIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 2),
    _PxmTC0NwIntfPmSampleDuration_Type()
)
pxmTC0NwIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmSampleDuration.setStatus("current")
_PxmTC0NwIntfPmValidity_Type = TruthValue
_PxmTC0NwIntfPmValidity_Object = MibTableColumn
pxmTC0NwIntfPmValidity = _PxmTC0NwIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 3),
    _PxmTC0NwIntfPmValidity_Type()
)
pxmTC0NwIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmValidity.setStatus("current")
_PxmTC0NwIntfPmTCNum_Type = Integer32
_PxmTC0NwIntfPmTCNum_Object = MibTableColumn
pxmTC0NwIntfPmTCNum = _PxmTC0NwIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 4),
    _PxmTC0NwIntfPmTCNum_Type()
)
pxmTC0NwIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmTCNum.setStatus("current")
_PxmTC0NwIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC0NwIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC0NwIntfPmQueueingDiscardOctets = _PxmTC0NwIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 5),
    _PxmTC0NwIntfPmQueueingDiscardOctets_Type()
)
pxmTC0NwIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC0NwIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC0NwIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC0NwIntfPmQueueingDiscardPkts = _PxmTC0NwIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 6),
    _PxmTC0NwIntfPmQueueingDiscardPkts_Type()
)
pxmTC0NwIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC0NwIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC0NwIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC0NwIntfPmRandomGreenDropPkts = _PxmTC0NwIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 7),
    _PxmTC0NwIntfPmRandomGreenDropPkts_Type()
)
pxmTC0NwIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC0NwIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC0NwIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC0NwIntfPmRandomGreenDropOctets = _PxmTC0NwIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 8),
    _PxmTC0NwIntfPmRandomGreenDropOctets_Type()
)
pxmTC0NwIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC0NwIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC0NwIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC0NwIntfPmRandomYellowDropPkts = _PxmTC0NwIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 9),
    _PxmTC0NwIntfPmRandomYellowDropPkts_Type()
)
pxmTC0NwIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC0NwIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC0NwIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC0NwIntfPmRandomYellowDropOctets = _PxmTC0NwIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 10),
    _PxmTC0NwIntfPmRandomYellowDropOctets_Type()
)
pxmTC0NwIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC0NwIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC0NwIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC0NwIntfPmQueueingTransmitPkts = _PxmTC0NwIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 11),
    _PxmTC0NwIntfPmQueueingTransmitPkts_Type()
)
pxmTC0NwIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC0NwIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC0NwIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC0NwIntfPmQueueingTransmitOctets = _PxmTC0NwIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 1, 1, 12),
    _PxmTC0NwIntfPmQueueingTransmitOctets_Type()
)
pxmTC0NwIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTC2NwIntfPmTable_Object = MibTable
pxmTC2NwIntfPmTable = _PxmTC2NwIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmTable.setStatus("current")
_PxmTC2NwIntfPmEntry_Object = MibTableRow
pxmTC2NwIntfPmEntry = _PxmTC2NwIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1)
)
pxmTC2NwIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmEntry.setStatus("current")


class _PxmTC2NwIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC2NwIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC2NwIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC2NwIntfPmTimestamp_Object = MibTableColumn
pxmTC2NwIntfPmTimestamp = _PxmTC2NwIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 1),
    _PxmTC2NwIntfPmTimestamp_Type()
)
pxmTC2NwIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmTimestamp.setStatus("current")


class _PxmTC2NwIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC2NwIntfPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_PxmTC2NwIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC2NwIntfPmSampleDuration_Object = MibTableColumn
pxmTC2NwIntfPmSampleDuration = _PxmTC2NwIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 2),
    _PxmTC2NwIntfPmSampleDuration_Type()
)
pxmTC2NwIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmSampleDuration.setStatus("current")
_PxmTC2NwIntfPmValidity_Type = TruthValue
_PxmTC2NwIntfPmValidity_Object = MibTableColumn
pxmTC2NwIntfPmValidity = _PxmTC2NwIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 3),
    _PxmTC2NwIntfPmValidity_Type()
)
pxmTC2NwIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmValidity.setStatus("current")
_PxmTC2NwIntfPmTCNum_Type = Integer32
_PxmTC2NwIntfPmTCNum_Object = MibTableColumn
pxmTC2NwIntfPmTCNum = _PxmTC2NwIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 4),
    _PxmTC2NwIntfPmTCNum_Type()
)
pxmTC2NwIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmTCNum.setStatus("current")
_PxmTC2NwIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC2NwIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC2NwIntfPmQueueingDiscardOctets = _PxmTC2NwIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 5),
    _PxmTC2NwIntfPmQueueingDiscardOctets_Type()
)
pxmTC2NwIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC2NwIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC2NwIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC2NwIntfPmQueueingDiscardPkts = _PxmTC2NwIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 6),
    _PxmTC2NwIntfPmQueueingDiscardPkts_Type()
)
pxmTC2NwIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC2NwIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC2NwIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC2NwIntfPmRandomGreenDropPkts = _PxmTC2NwIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 7),
    _PxmTC2NwIntfPmRandomGreenDropPkts_Type()
)
pxmTC2NwIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC2NwIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC2NwIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC2NwIntfPmRandomGreenDropOctets = _PxmTC2NwIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 8),
    _PxmTC2NwIntfPmRandomGreenDropOctets_Type()
)
pxmTC2NwIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC2NwIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC2NwIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC2NwIntfPmRandomYellowDropPkts = _PxmTC2NwIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 9),
    _PxmTC2NwIntfPmRandomYellowDropPkts_Type()
)
pxmTC2NwIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC2NwIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC2NwIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC2NwIntfPmRandomYellowDropOctets = _PxmTC2NwIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 10),
    _PxmTC2NwIntfPmRandomYellowDropOctets_Type()
)
pxmTC2NwIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC2NwIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC2NwIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC2NwIntfPmQueueingTransmitPkts = _PxmTC2NwIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 11),
    _PxmTC2NwIntfPmQueueingTransmitPkts_Type()
)
pxmTC2NwIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC2NwIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC2NwIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC2NwIntfPmQueueingTransmitOctets = _PxmTC2NwIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 2, 1, 12),
    _PxmTC2NwIntfPmQueueingTransmitOctets_Type()
)
pxmTC2NwIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTC4NwIntfPmTable_Object = MibTable
pxmTC4NwIntfPmTable = _PxmTC4NwIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmTable.setStatus("current")
_PxmTC4NwIntfPmEntry_Object = MibTableRow
pxmTC4NwIntfPmEntry = _PxmTC4NwIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1)
)
pxmTC4NwIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmEntry.setStatus("current")


class _PxmTC4NwIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC4NwIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC4NwIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC4NwIntfPmTimestamp_Object = MibTableColumn
pxmTC4NwIntfPmTimestamp = _PxmTC4NwIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 1),
    _PxmTC4NwIntfPmTimestamp_Type()
)
pxmTC4NwIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmTimestamp.setStatus("current")


class _PxmTC4NwIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC4NwIntfPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_PxmTC4NwIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC4NwIntfPmSampleDuration_Object = MibTableColumn
pxmTC4NwIntfPmSampleDuration = _PxmTC4NwIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 2),
    _PxmTC4NwIntfPmSampleDuration_Type()
)
pxmTC4NwIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmSampleDuration.setStatus("current")
_PxmTC4NwIntfPmValidity_Type = TruthValue
_PxmTC4NwIntfPmValidity_Object = MibTableColumn
pxmTC4NwIntfPmValidity = _PxmTC4NwIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 3),
    _PxmTC4NwIntfPmValidity_Type()
)
pxmTC4NwIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmValidity.setStatus("current")
_PxmTC4NwIntfPmTCNum_Type = Integer32
_PxmTC4NwIntfPmTCNum_Object = MibTableColumn
pxmTC4NwIntfPmTCNum = _PxmTC4NwIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 4),
    _PxmTC4NwIntfPmTCNum_Type()
)
pxmTC4NwIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmTCNum.setStatus("current")
_PxmTC4NwIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC4NwIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC4NwIntfPmQueueingDiscardOctets = _PxmTC4NwIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 5),
    _PxmTC4NwIntfPmQueueingDiscardOctets_Type()
)
pxmTC4NwIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC4NwIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC4NwIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC4NwIntfPmQueueingDiscardPkts = _PxmTC4NwIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 6),
    _PxmTC4NwIntfPmQueueingDiscardPkts_Type()
)
pxmTC4NwIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC4NwIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC4NwIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC4NwIntfPmRandomGreenDropPkts = _PxmTC4NwIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 7),
    _PxmTC4NwIntfPmRandomGreenDropPkts_Type()
)
pxmTC4NwIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC4NwIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC4NwIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC4NwIntfPmRandomGreenDropOctets = _PxmTC4NwIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 8),
    _PxmTC4NwIntfPmRandomGreenDropOctets_Type()
)
pxmTC4NwIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC4NwIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC4NwIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC4NwIntfPmRandomYellowDropPkts = _PxmTC4NwIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 9),
    _PxmTC4NwIntfPmRandomYellowDropPkts_Type()
)
pxmTC4NwIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC4NwIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC4NwIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC4NwIntfPmRandomYellowDropOctets = _PxmTC4NwIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 10),
    _PxmTC4NwIntfPmRandomYellowDropOctets_Type()
)
pxmTC4NwIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC4NwIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC4NwIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC4NwIntfPmQueueingTransmitPkts = _PxmTC4NwIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 11),
    _PxmTC4NwIntfPmQueueingTransmitPkts_Type()
)
pxmTC4NwIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC4NwIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC4NwIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC4NwIntfPmQueueingTransmitOctets = _PxmTC4NwIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 3, 1, 12),
    _PxmTC4NwIntfPmQueueingTransmitOctets_Type()
)
pxmTC4NwIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTC6NwIntfPmTable_Object = MibTable
pxmTC6NwIntfPmTable = _PxmTC6NwIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmTable.setStatus("current")
_PxmTC6NwIntfPmEntry_Object = MibTableRow
pxmTC6NwIntfPmEntry = _PxmTC6NwIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1)
)
pxmTC6NwIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmEntry.setStatus("current")


class _PxmTC6NwIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC6NwIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC6NwIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC6NwIntfPmTimestamp_Object = MibTableColumn
pxmTC6NwIntfPmTimestamp = _PxmTC6NwIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 1),
    _PxmTC6NwIntfPmTimestamp_Type()
)
pxmTC6NwIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmTimestamp.setStatus("current")


class _PxmTC6NwIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC6NwIntfPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_PxmTC6NwIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC6NwIntfPmSampleDuration_Object = MibTableColumn
pxmTC6NwIntfPmSampleDuration = _PxmTC6NwIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 2),
    _PxmTC6NwIntfPmSampleDuration_Type()
)
pxmTC6NwIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmSampleDuration.setStatus("current")
_PxmTC6NwIntfPmValidity_Type = TruthValue
_PxmTC6NwIntfPmValidity_Object = MibTableColumn
pxmTC6NwIntfPmValidity = _PxmTC6NwIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 3),
    _PxmTC6NwIntfPmValidity_Type()
)
pxmTC6NwIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmValidity.setStatus("current")
_PxmTC6NwIntfPmTCNum_Type = Integer32
_PxmTC6NwIntfPmTCNum_Object = MibTableColumn
pxmTC6NwIntfPmTCNum = _PxmTC6NwIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 4),
    _PxmTC6NwIntfPmTCNum_Type()
)
pxmTC6NwIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmTCNum.setStatus("current")
_PxmTC6NwIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC6NwIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC6NwIntfPmQueueingDiscardOctets = _PxmTC6NwIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 5),
    _PxmTC6NwIntfPmQueueingDiscardOctets_Type()
)
pxmTC6NwIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC6NwIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC6NwIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC6NwIntfPmQueueingDiscardPkts = _PxmTC6NwIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 6),
    _PxmTC6NwIntfPmQueueingDiscardPkts_Type()
)
pxmTC6NwIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC6NwIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC6NwIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC6NwIntfPmRandomGreenDropPkts = _PxmTC6NwIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 7),
    _PxmTC6NwIntfPmRandomGreenDropPkts_Type()
)
pxmTC6NwIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC6NwIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC6NwIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC6NwIntfPmRandomGreenDropOctets = _PxmTC6NwIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 8),
    _PxmTC6NwIntfPmRandomGreenDropOctets_Type()
)
pxmTC6NwIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC6NwIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC6NwIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC6NwIntfPmRandomYellowDropPkts = _PxmTC6NwIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 9),
    _PxmTC6NwIntfPmRandomYellowDropPkts_Type()
)
pxmTC6NwIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC6NwIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC6NwIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC6NwIntfPmRandomYellowDropOctets = _PxmTC6NwIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 10),
    _PxmTC6NwIntfPmRandomYellowDropOctets_Type()
)
pxmTC6NwIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC6NwIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC6NwIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC6NwIntfPmQueueingTransmitPkts = _PxmTC6NwIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 11),
    _PxmTC6NwIntfPmQueueingTransmitPkts_Type()
)
pxmTC6NwIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC6NwIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC6NwIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC6NwIntfPmQueueingTransmitOctets = _PxmTC6NwIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 4, 1, 12),
    _PxmTC6NwIntfPmQueueingTransmitOctets_Type()
)
pxmTC6NwIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTC7NwIntfPmTable_Object = MibTable
pxmTC7NwIntfPmTable = _PxmTC7NwIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5)
)
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmTable.setStatus("current")
_PxmTC7NwIntfPmEntry_Object = MibTableRow
pxmTC7NwIntfPmEntry = _PxmTC7NwIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1)
)
pxmTC7NwIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmEntry.setStatus("current")


class _PxmTC7NwIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC7NwIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC7NwIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC7NwIntfPmTimestamp_Object = MibTableColumn
pxmTC7NwIntfPmTimestamp = _PxmTC7NwIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 1),
    _PxmTC7NwIntfPmTimestamp_Type()
)
pxmTC7NwIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmTimestamp.setStatus("current")


class _PxmTC7NwIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC7NwIntfPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_PxmTC7NwIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC7NwIntfPmSampleDuration_Object = MibTableColumn
pxmTC7NwIntfPmSampleDuration = _PxmTC7NwIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 2),
    _PxmTC7NwIntfPmSampleDuration_Type()
)
pxmTC7NwIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmSampleDuration.setStatus("current")
_PxmTC7NwIntfPmValidity_Type = TruthValue
_PxmTC7NwIntfPmValidity_Object = MibTableColumn
pxmTC7NwIntfPmValidity = _PxmTC7NwIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 3),
    _PxmTC7NwIntfPmValidity_Type()
)
pxmTC7NwIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmValidity.setStatus("current")
_PxmTC7NwIntfPmTCNum_Type = Integer32
_PxmTC7NwIntfPmTCNum_Object = MibTableColumn
pxmTC7NwIntfPmTCNum = _PxmTC7NwIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 4),
    _PxmTC7NwIntfPmTCNum_Type()
)
pxmTC7NwIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmTCNum.setStatus("current")
_PxmTC7NwIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC7NwIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC7NwIntfPmQueueingDiscardOctets = _PxmTC7NwIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 5),
    _PxmTC7NwIntfPmQueueingDiscardOctets_Type()
)
pxmTC7NwIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC7NwIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC7NwIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC7NwIntfPmQueueingDiscardPkts = _PxmTC7NwIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 6),
    _PxmTC7NwIntfPmQueueingDiscardPkts_Type()
)
pxmTC7NwIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC7NwIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC7NwIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC7NwIntfPmRandomGreenDropPkts = _PxmTC7NwIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 7),
    _PxmTC7NwIntfPmRandomGreenDropPkts_Type()
)
pxmTC7NwIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC7NwIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC7NwIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC7NwIntfPmRandomGreenDropOctets = _PxmTC7NwIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 8),
    _PxmTC7NwIntfPmRandomGreenDropOctets_Type()
)
pxmTC7NwIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC7NwIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC7NwIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC7NwIntfPmRandomYellowDropPkts = _PxmTC7NwIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 9),
    _PxmTC7NwIntfPmRandomYellowDropPkts_Type()
)
pxmTC7NwIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC7NwIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC7NwIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC7NwIntfPmRandomYellowDropOctets = _PxmTC7NwIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 10),
    _PxmTC7NwIntfPmRandomYellowDropOctets_Type()
)
pxmTC7NwIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC7NwIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC7NwIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC7NwIntfPmQueueingTransmitPkts = _PxmTC7NwIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 11),
    _PxmTC7NwIntfPmQueueingTransmitPkts_Type()
)
pxmTC7NwIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC7NwIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC7NwIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC7NwIntfPmQueueingTransmitOctets = _PxmTC7NwIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 5, 1, 12),
    _PxmTC7NwIntfPmQueueingTransmitOctets_Type()
)
pxmTC7NwIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTCANYNwIntfPmTable_Object = MibTable
pxmTCANYNwIntfPmTable = _PxmTCANYNwIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6)
)
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmTable.setStatus("current")
_PxmTCANYNwIntfPmEntry_Object = MibTableRow
pxmTCANYNwIntfPmEntry = _PxmTCANYNwIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1)
)
pxmTCANYNwIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmEntry.setStatus("current")


class _PxmTCANYNwIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTCANYNwIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTCANYNwIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTCANYNwIntfPmTimestamp_Object = MibTableColumn
pxmTCANYNwIntfPmTimestamp = _PxmTCANYNwIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 1),
    _PxmTCANYNwIntfPmTimestamp_Type()
)
pxmTCANYNwIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmTimestamp.setStatus("current")


class _PxmTCANYNwIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTCANYNwIntfPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_PxmTCANYNwIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTCANYNwIntfPmSampleDuration_Object = MibTableColumn
pxmTCANYNwIntfPmSampleDuration = _PxmTCANYNwIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 2),
    _PxmTCANYNwIntfPmSampleDuration_Type()
)
pxmTCANYNwIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmSampleDuration.setStatus("current")
_PxmTCANYNwIntfPmValidity_Type = TruthValue
_PxmTCANYNwIntfPmValidity_Object = MibTableColumn
pxmTCANYNwIntfPmValidity = _PxmTCANYNwIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 3),
    _PxmTCANYNwIntfPmValidity_Type()
)
pxmTCANYNwIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmValidity.setStatus("current")
_PxmTCANYNwIntfPmTCNum_Type = Integer32
_PxmTCANYNwIntfPmTCNum_Object = MibTableColumn
pxmTCANYNwIntfPmTCNum = _PxmTCANYNwIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 4),
    _PxmTCANYNwIntfPmTCNum_Type()
)
pxmTCANYNwIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmTCNum.setStatus("current")
_PxmTCANYNwIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTCANYNwIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTCANYNwIntfPmQueueingDiscardOctets = _PxmTCANYNwIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 5),
    _PxmTCANYNwIntfPmQueueingDiscardOctets_Type()
)
pxmTCANYNwIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTCANYNwIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTCANYNwIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTCANYNwIntfPmQueueingDiscardPkts = _PxmTCANYNwIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 6),
    _PxmTCANYNwIntfPmQueueingDiscardPkts_Type()
)
pxmTCANYNwIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTCANYNwIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTCANYNwIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTCANYNwIntfPmRandomGreenDropPkts = _PxmTCANYNwIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 7),
    _PxmTCANYNwIntfPmRandomGreenDropPkts_Type()
)
pxmTCANYNwIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTCANYNwIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTCANYNwIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTCANYNwIntfPmRandomGreenDropOctets = _PxmTCANYNwIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 8),
    _PxmTCANYNwIntfPmRandomGreenDropOctets_Type()
)
pxmTCANYNwIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTCANYNwIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTCANYNwIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTCANYNwIntfPmRandomYellowDropPkts = _PxmTCANYNwIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 9),
    _PxmTCANYNwIntfPmRandomYellowDropPkts_Type()
)
pxmTCANYNwIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTCANYNwIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTCANYNwIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTCANYNwIntfPmRandomYellowDropOctets = _PxmTCANYNwIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 10),
    _PxmTCANYNwIntfPmRandomYellowDropOctets_Type()
)
pxmTCANYNwIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTCANYNwIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTCANYNwIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTCANYNwIntfPmQueueingTransmitPkts = _PxmTCANYNwIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 11),
    _PxmTCANYNwIntfPmQueueingTransmitPkts_Type()
)
pxmTCANYNwIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTCANYNwIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTCANYNwIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTCANYNwIntfPmQueueingTransmitOctets = _PxmTCANYNwIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 2, 2, 6, 1, 12),
    _PxmTCANYNwIntfPmQueueingTransmitOctets_Type()
)
pxmTCANYNwIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmQueueingTransmitOctets.setStatus("current")
_PxmNwIntfPmConformance_ObjectIdentity = ObjectIdentity
pxmNwIntfPmConformance = _PxmNwIntfPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3)
)
_PxmNwIntfPmCompliances_ObjectIdentity = ObjectIdentity
pxmNwIntfPmCompliances = _PxmNwIntfPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 1)
)
_PxmNwIntfPmGroups_ObjectIdentity = ObjectIdentity
pxmNwIntfPmGroups = _PxmNwIntfPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2)
)

# Managed Objects groups

pxmNwIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 1)
)
pxmNwIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmValidity"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRxPackets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmTxPackets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRxOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmTxOctets"))
)
if mibBuilder.loadTexts:
    pxmNwIntfPmGroup.setStatus("current")

pxmNwIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 2)
)
pxmNwIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRealRxPackets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRealTxPackets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRealRxOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRealTxOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRealRxLU"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRealTxLU"))
)
if mibBuilder.loadTexts:
    pxmNwIntfPmRealGroup.setStatus("current")

pxmTC0NwIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 3)
)
pxmTC0NwIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmValidity"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmGroup.setStatus("current")

pxmTC0NwIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 4)
)
pxmTC0NwIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC0NwIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC0NwIntfPmRealGroup.setStatus("current")

pxmTC2NwIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 5)
)
pxmTC2NwIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmValidity"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmGroup.setStatus("current")

pxmTC2NwIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 6)
)
pxmTC2NwIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC2NwIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC2NwIntfPmRealGroup.setStatus("current")

pxmTC4NwIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 7)
)
pxmTC4NwIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmValidity"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmGroup.setStatus("current")

pxmTC4NwIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 8)
)
pxmTC4NwIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC4NwIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC4NwIntfPmRealGroup.setStatus("current")

pxmTC6NwIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 9)
)
pxmTC6NwIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmValidity"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmGroup.setStatus("current")

pxmTC6NwIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 10)
)
pxmTC6NwIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC6NwIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC6NwIntfPmRealGroup.setStatus("current")

pxmTC7NwIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 11)
)
pxmTC7NwIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmValidity"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmGroup.setStatus("current")

pxmTC7NwIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 12)
)
pxmTC7NwIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTC7NwIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC7NwIntfPmRealGroup.setStatus("current")

pxmTCANYNwIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 13)
)
pxmTCANYNwIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmValidity"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmGroup.setStatus("current")

pxmTCANYNwIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 2, 14)
)
pxmTCANYNwIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealTCNum"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMNWINTF-MIB", "pxmTCANYNwIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTCANYNwIntfPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmNwIntfPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 1, 1)
)
pxmNwIntfPmCompliance.setObjects(
    ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmGroup")
)
if mibBuilder.loadTexts:
    pxmNwIntfPmCompliance.setStatus(
        "current"
    )

pxmNwIntfPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 98, 3, 1, 2)
)
pxmNwIntfPmRealCompliance.setObjects(
    ("INFINERA-PM-PXMNWINTF-MIB", "pxmNwIntfPmRealGroup")
)
if mibBuilder.loadTexts:
    pxmNwIntfPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-PXMNWINTF-MIB",
    **{"pxmNwIntfPmMIB": pxmNwIntfPmMIB,
       "pxmNwIntfRmonPm": pxmNwIntfRmonPm,
       "pxmNwIntfPmRealTable": pxmNwIntfPmRealTable,
       "pxmNwIntfPmRealEntry": pxmNwIntfPmRealEntry,
       "pxmNwIntfPmRealRxPackets": pxmNwIntfPmRealRxPackets,
       "pxmNwIntfPmRealTxPackets": pxmNwIntfPmRealTxPackets,
       "pxmNwIntfPmRealRxOctets": pxmNwIntfPmRealRxOctets,
       "pxmNwIntfPmRealTxOctets": pxmNwIntfPmRealTxOctets,
       "pxmNwIntfPmRealRxLU": pxmNwIntfPmRealRxLU,
       "pxmNwIntfPmRealTxLU": pxmNwIntfPmRealTxLU,
       "pxmNwIntfPmTable": pxmNwIntfPmTable,
       "pxmNwIntfPmEntry": pxmNwIntfPmEntry,
       "pxmNwIntfPmTimestamp": pxmNwIntfPmTimestamp,
       "pxmNwIntfPmSampleDuration": pxmNwIntfPmSampleDuration,
       "pxmNwIntfPmValidity": pxmNwIntfPmValidity,
       "pxmNwIntfPmRxPackets": pxmNwIntfPmRxPackets,
       "pxmNwIntfPmTxPackets": pxmNwIntfPmTxPackets,
       "pxmNwIntfPmRxOctets": pxmNwIntfPmRxOctets,
       "pxmNwIntfPmTxOctets": pxmNwIntfPmTxOctets,
       "pxmCmNwIntfPmObjects": pxmCmNwIntfPmObjects,
       "pxmCmNwIntfRealPm": pxmCmNwIntfRealPm,
       "pxmTC0NwIntfPmRealTable": pxmTC0NwIntfPmRealTable,
       "pxmTC0NwIntfPmRealEntry": pxmTC0NwIntfPmRealEntry,
       "pxmTC0NwIntfPmRealTCNum": pxmTC0NwIntfPmRealTCNum,
       "pxmTC0NwIntfPmRealTDQueuingCurrentQDepth": pxmTC0NwIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC0NwIntfPmRealQueueingDiscardOctets": pxmTC0NwIntfPmRealQueueingDiscardOctets,
       "pxmTC0NwIntfPmRealQueueingDiscardPkts": pxmTC0NwIntfPmRealQueueingDiscardPkts,
       "pxmTC0NwIntfPmRealRandomGreenDropPkts": pxmTC0NwIntfPmRealRandomGreenDropPkts,
       "pxmTC0NwIntfPmRealRandomGreenDropOctets": pxmTC0NwIntfPmRealRandomGreenDropOctets,
       "pxmTC0NwIntfPmRealRandomYellowDropPkts": pxmTC0NwIntfPmRealRandomYellowDropPkts,
       "pxmTC0NwIntfPmRealRandomYellowDropOctets": pxmTC0NwIntfPmRealRandomYellowDropOctets,
       "pxmTC0NwIntfPmRealQueueingTransmitPkts": pxmTC0NwIntfPmRealQueueingTransmitPkts,
       "pxmTC0NwIntfPmRealQueueingTransmitOctets": pxmTC0NwIntfPmRealQueueingTransmitOctets,
       "pxmTC0NwIntfPmRealQueueingMeanQSizeUnit": pxmTC0NwIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC0NwIntfPmRealMeanQSize": pxmTC0NwIntfPmRealMeanQSize,
       "pxmTC2NwIntfPmRealTable": pxmTC2NwIntfPmRealTable,
       "pxmTC2NwIntfPmRealEntry": pxmTC2NwIntfPmRealEntry,
       "pxmTC2NwIntfPmRealTCNum": pxmTC2NwIntfPmRealTCNum,
       "pxmTC2NwIntfPmRealTDQueuingCurrentQDepth": pxmTC2NwIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC2NwIntfPmRealQueueingDiscardOctets": pxmTC2NwIntfPmRealQueueingDiscardOctets,
       "pxmTC2NwIntfPmRealQueueingDiscardPkts": pxmTC2NwIntfPmRealQueueingDiscardPkts,
       "pxmTC2NwIntfPmRealRandomGreenDropPkts": pxmTC2NwIntfPmRealRandomGreenDropPkts,
       "pxmTC2NwIntfPmRealRandomGreenDropOctets": pxmTC2NwIntfPmRealRandomGreenDropOctets,
       "pxmTC2NwIntfPmRealRandomYellowDropPkts": pxmTC2NwIntfPmRealRandomYellowDropPkts,
       "pxmTC2NwIntfPmRealRandomYellowDropOctets": pxmTC2NwIntfPmRealRandomYellowDropOctets,
       "pxmTC2NwIntfPmRealQueueingTransmitPkts": pxmTC2NwIntfPmRealQueueingTransmitPkts,
       "pxmTC2NwIntfPmRealQueueingTransmitOctets": pxmTC2NwIntfPmRealQueueingTransmitOctets,
       "pxmTC2NwIntfPmRealQueueingMeanQSizeUnit": pxmTC2NwIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC2NwIntfPmRealMeanQSize": pxmTC2NwIntfPmRealMeanQSize,
       "pxmTC4NwIntfPmRealTable": pxmTC4NwIntfPmRealTable,
       "pxmTC4NwIntfPmRealEntry": pxmTC4NwIntfPmRealEntry,
       "pxmTC4NwIntfPmRealTCNum": pxmTC4NwIntfPmRealTCNum,
       "pxmTC4NwIntfPmRealTDQueuingCurrentQDepth": pxmTC4NwIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC4NwIntfPmRealQueueingDiscardOctets": pxmTC4NwIntfPmRealQueueingDiscardOctets,
       "pxmTC4NwIntfPmRealQueueingDiscardPkts": pxmTC4NwIntfPmRealQueueingDiscardPkts,
       "pxmTC4NwIntfPmRealRandomGreenDropPkts": pxmTC4NwIntfPmRealRandomGreenDropPkts,
       "pxmTC4NwIntfPmRealRandomGreenDropOctets": pxmTC4NwIntfPmRealRandomGreenDropOctets,
       "pxmTC4NwIntfPmRealRandomYellowDropPkts": pxmTC4NwIntfPmRealRandomYellowDropPkts,
       "pxmTC4NwIntfPmRealRandomYellowDropOctets": pxmTC4NwIntfPmRealRandomYellowDropOctets,
       "pxmTC4NwIntfPmRealQueueingTransmitPkts": pxmTC4NwIntfPmRealQueueingTransmitPkts,
       "pxmTC4NwIntfPmRealQueueingTransmitOctets": pxmTC4NwIntfPmRealQueueingTransmitOctets,
       "pxmTC4NwIntfPmRealQueueingMeanQSizeUnit": pxmTC4NwIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC4NwIntfPmRealMeanQSize": pxmTC4NwIntfPmRealMeanQSize,
       "pxmTC6NwIntfPmRealTable": pxmTC6NwIntfPmRealTable,
       "pxmTC6NwIntfPmRealEntry": pxmTC6NwIntfPmRealEntry,
       "pxmTC6NwIntfPmRealTCNum": pxmTC6NwIntfPmRealTCNum,
       "pxmTC6NwIntfPmRealTDQueuingCurrentQDepth": pxmTC6NwIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC6NwIntfPmRealQueueingDiscardOctets": pxmTC6NwIntfPmRealQueueingDiscardOctets,
       "pxmTC6NwIntfPmRealQueueingDiscardPkts": pxmTC6NwIntfPmRealQueueingDiscardPkts,
       "pxmTC6NwIntfPmRealRandomGreenDropPkts": pxmTC6NwIntfPmRealRandomGreenDropPkts,
       "pxmTC6NwIntfPmRealRandomGreenDropOctets": pxmTC6NwIntfPmRealRandomGreenDropOctets,
       "pxmTC6NwIntfPmRealRandomYellowDropPkts": pxmTC6NwIntfPmRealRandomYellowDropPkts,
       "pxmTC6NwIntfPmRealRandomYellowDropOctets": pxmTC6NwIntfPmRealRandomYellowDropOctets,
       "pxmTC6NwIntfPmRealQueueingTransmitPkts": pxmTC6NwIntfPmRealQueueingTransmitPkts,
       "pxmTC6NwIntfPmRealQueueingTransmitOctets": pxmTC6NwIntfPmRealQueueingTransmitOctets,
       "pxmTC6NwIntfPmRealQueueingMeanQSizeUnit": pxmTC6NwIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC6NwIntfPmRealMeanQSize": pxmTC6NwIntfPmRealMeanQSize,
       "pxmTC7NwIntfPmRealTable": pxmTC7NwIntfPmRealTable,
       "pxmTC7NwIntfPmRealEntry": pxmTC7NwIntfPmRealEntry,
       "pxmTC7NwIntfPmRealTCNum": pxmTC7NwIntfPmRealTCNum,
       "pxmTC7NwIntfPmRealTDQueuingCurrentQDepth": pxmTC7NwIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC7NwIntfPmRealQueueingDiscardOctets": pxmTC7NwIntfPmRealQueueingDiscardOctets,
       "pxmTC7NwIntfPmRealQueueingDiscardPkts": pxmTC7NwIntfPmRealQueueingDiscardPkts,
       "pxmTC7NwIntfPmRealRandomGreenDropPkts": pxmTC7NwIntfPmRealRandomGreenDropPkts,
       "pxmTC7NwIntfPmRealRandomGreenDropOctets": pxmTC7NwIntfPmRealRandomGreenDropOctets,
       "pxmTC7NwIntfPmRealRandomYellowDropPkts": pxmTC7NwIntfPmRealRandomYellowDropPkts,
       "pxmTC7NwIntfPmRealRandomYellowDropOctets": pxmTC7NwIntfPmRealRandomYellowDropOctets,
       "pxmTC7NwIntfPmRealQueueingTransmitPkts": pxmTC7NwIntfPmRealQueueingTransmitPkts,
       "pxmTC7NwIntfPmRealQueueingTransmitOctets": pxmTC7NwIntfPmRealQueueingTransmitOctets,
       "pxmTC7NwIntfPmRealQueueingMeanQSizeUnit": pxmTC7NwIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC7NwIntfPmRealMeanQSize": pxmTC7NwIntfPmRealMeanQSize,
       "pxmTCANYNwIntfPmRealTable": pxmTCANYNwIntfPmRealTable,
       "pxmTCANYNwIntfPmRealEntry": pxmTCANYNwIntfPmRealEntry,
       "pxmTCANYNwIntfPmRealTCNum": pxmTCANYNwIntfPmRealTCNum,
       "pxmTCANYNwIntfPmRealTDQueuingCurrentQDepth": pxmTCANYNwIntfPmRealTDQueuingCurrentQDepth,
       "pxmTCANYNwIntfPmRealQueueingDiscardOctets": pxmTCANYNwIntfPmRealQueueingDiscardOctets,
       "pxmTCANYNwIntfPmRealQueueingDiscardPkts": pxmTCANYNwIntfPmRealQueueingDiscardPkts,
       "pxmTCANYNwIntfPmRealRandomGreenDropPkts": pxmTCANYNwIntfPmRealRandomGreenDropPkts,
       "pxmTCANYNwIntfPmRealRandomGreenDropOctets": pxmTCANYNwIntfPmRealRandomGreenDropOctets,
       "pxmTCANYNwIntfPmRealRandomYellowDropPkts": pxmTCANYNwIntfPmRealRandomYellowDropPkts,
       "pxmTCANYNwIntfPmRealRandomYellowDropOctets": pxmTCANYNwIntfPmRealRandomYellowDropOctets,
       "pxmTCANYNwIntfPmRealQueueingTransmitPkts": pxmTCANYNwIntfPmRealQueueingTransmitPkts,
       "pxmTCANYNwIntfPmRealQueueingTransmitOctets": pxmTCANYNwIntfPmRealQueueingTransmitOctets,
       "pxmTCANYNwIntfPmRealQueueingMeanQSizeUnit": pxmTCANYNwIntfPmRealQueueingMeanQSizeUnit,
       "pxmTCANYNwIntfPmRealMeanQSize": pxmTCANYNwIntfPmRealMeanQSize,
       "pxmCmNwIntfPm": pxmCmNwIntfPm,
       "pxmTC0NwIntfPmTable": pxmTC0NwIntfPmTable,
       "pxmTC0NwIntfPmEntry": pxmTC0NwIntfPmEntry,
       "pxmTC0NwIntfPmTimestamp": pxmTC0NwIntfPmTimestamp,
       "pxmTC0NwIntfPmSampleDuration": pxmTC0NwIntfPmSampleDuration,
       "pxmTC0NwIntfPmValidity": pxmTC0NwIntfPmValidity,
       "pxmTC0NwIntfPmTCNum": pxmTC0NwIntfPmTCNum,
       "pxmTC0NwIntfPmQueueingDiscardOctets": pxmTC0NwIntfPmQueueingDiscardOctets,
       "pxmTC0NwIntfPmQueueingDiscardPkts": pxmTC0NwIntfPmQueueingDiscardPkts,
       "pxmTC0NwIntfPmRandomGreenDropPkts": pxmTC0NwIntfPmRandomGreenDropPkts,
       "pxmTC0NwIntfPmRandomGreenDropOctets": pxmTC0NwIntfPmRandomGreenDropOctets,
       "pxmTC0NwIntfPmRandomYellowDropPkts": pxmTC0NwIntfPmRandomYellowDropPkts,
       "pxmTC0NwIntfPmRandomYellowDropOctets": pxmTC0NwIntfPmRandomYellowDropOctets,
       "pxmTC0NwIntfPmQueueingTransmitPkts": pxmTC0NwIntfPmQueueingTransmitPkts,
       "pxmTC0NwIntfPmQueueingTransmitOctets": pxmTC0NwIntfPmQueueingTransmitOctets,
       "pxmTC2NwIntfPmTable": pxmTC2NwIntfPmTable,
       "pxmTC2NwIntfPmEntry": pxmTC2NwIntfPmEntry,
       "pxmTC2NwIntfPmTimestamp": pxmTC2NwIntfPmTimestamp,
       "pxmTC2NwIntfPmSampleDuration": pxmTC2NwIntfPmSampleDuration,
       "pxmTC2NwIntfPmValidity": pxmTC2NwIntfPmValidity,
       "pxmTC2NwIntfPmTCNum": pxmTC2NwIntfPmTCNum,
       "pxmTC2NwIntfPmQueueingDiscardOctets": pxmTC2NwIntfPmQueueingDiscardOctets,
       "pxmTC2NwIntfPmQueueingDiscardPkts": pxmTC2NwIntfPmQueueingDiscardPkts,
       "pxmTC2NwIntfPmRandomGreenDropPkts": pxmTC2NwIntfPmRandomGreenDropPkts,
       "pxmTC2NwIntfPmRandomGreenDropOctets": pxmTC2NwIntfPmRandomGreenDropOctets,
       "pxmTC2NwIntfPmRandomYellowDropPkts": pxmTC2NwIntfPmRandomYellowDropPkts,
       "pxmTC2NwIntfPmRandomYellowDropOctets": pxmTC2NwIntfPmRandomYellowDropOctets,
       "pxmTC2NwIntfPmQueueingTransmitPkts": pxmTC2NwIntfPmQueueingTransmitPkts,
       "pxmTC2NwIntfPmQueueingTransmitOctets": pxmTC2NwIntfPmQueueingTransmitOctets,
       "pxmTC4NwIntfPmTable": pxmTC4NwIntfPmTable,
       "pxmTC4NwIntfPmEntry": pxmTC4NwIntfPmEntry,
       "pxmTC4NwIntfPmTimestamp": pxmTC4NwIntfPmTimestamp,
       "pxmTC4NwIntfPmSampleDuration": pxmTC4NwIntfPmSampleDuration,
       "pxmTC4NwIntfPmValidity": pxmTC4NwIntfPmValidity,
       "pxmTC4NwIntfPmTCNum": pxmTC4NwIntfPmTCNum,
       "pxmTC4NwIntfPmQueueingDiscardOctets": pxmTC4NwIntfPmQueueingDiscardOctets,
       "pxmTC4NwIntfPmQueueingDiscardPkts": pxmTC4NwIntfPmQueueingDiscardPkts,
       "pxmTC4NwIntfPmRandomGreenDropPkts": pxmTC4NwIntfPmRandomGreenDropPkts,
       "pxmTC4NwIntfPmRandomGreenDropOctets": pxmTC4NwIntfPmRandomGreenDropOctets,
       "pxmTC4NwIntfPmRandomYellowDropPkts": pxmTC4NwIntfPmRandomYellowDropPkts,
       "pxmTC4NwIntfPmRandomYellowDropOctets": pxmTC4NwIntfPmRandomYellowDropOctets,
       "pxmTC4NwIntfPmQueueingTransmitPkts": pxmTC4NwIntfPmQueueingTransmitPkts,
       "pxmTC4NwIntfPmQueueingTransmitOctets": pxmTC4NwIntfPmQueueingTransmitOctets,
       "pxmTC6NwIntfPmTable": pxmTC6NwIntfPmTable,
       "pxmTC6NwIntfPmEntry": pxmTC6NwIntfPmEntry,
       "pxmTC6NwIntfPmTimestamp": pxmTC6NwIntfPmTimestamp,
       "pxmTC6NwIntfPmSampleDuration": pxmTC6NwIntfPmSampleDuration,
       "pxmTC6NwIntfPmValidity": pxmTC6NwIntfPmValidity,
       "pxmTC6NwIntfPmTCNum": pxmTC6NwIntfPmTCNum,
       "pxmTC6NwIntfPmQueueingDiscardOctets": pxmTC6NwIntfPmQueueingDiscardOctets,
       "pxmTC6NwIntfPmQueueingDiscardPkts": pxmTC6NwIntfPmQueueingDiscardPkts,
       "pxmTC6NwIntfPmRandomGreenDropPkts": pxmTC6NwIntfPmRandomGreenDropPkts,
       "pxmTC6NwIntfPmRandomGreenDropOctets": pxmTC6NwIntfPmRandomGreenDropOctets,
       "pxmTC6NwIntfPmRandomYellowDropPkts": pxmTC6NwIntfPmRandomYellowDropPkts,
       "pxmTC6NwIntfPmRandomYellowDropOctets": pxmTC6NwIntfPmRandomYellowDropOctets,
       "pxmTC6NwIntfPmQueueingTransmitPkts": pxmTC6NwIntfPmQueueingTransmitPkts,
       "pxmTC6NwIntfPmQueueingTransmitOctets": pxmTC6NwIntfPmQueueingTransmitOctets,
       "pxmTC7NwIntfPmTable": pxmTC7NwIntfPmTable,
       "pxmTC7NwIntfPmEntry": pxmTC7NwIntfPmEntry,
       "pxmTC7NwIntfPmTimestamp": pxmTC7NwIntfPmTimestamp,
       "pxmTC7NwIntfPmSampleDuration": pxmTC7NwIntfPmSampleDuration,
       "pxmTC7NwIntfPmValidity": pxmTC7NwIntfPmValidity,
       "pxmTC7NwIntfPmTCNum": pxmTC7NwIntfPmTCNum,
       "pxmTC7NwIntfPmQueueingDiscardOctets": pxmTC7NwIntfPmQueueingDiscardOctets,
       "pxmTC7NwIntfPmQueueingDiscardPkts": pxmTC7NwIntfPmQueueingDiscardPkts,
       "pxmTC7NwIntfPmRandomGreenDropPkts": pxmTC7NwIntfPmRandomGreenDropPkts,
       "pxmTC7NwIntfPmRandomGreenDropOctets": pxmTC7NwIntfPmRandomGreenDropOctets,
       "pxmTC7NwIntfPmRandomYellowDropPkts": pxmTC7NwIntfPmRandomYellowDropPkts,
       "pxmTC7NwIntfPmRandomYellowDropOctets": pxmTC7NwIntfPmRandomYellowDropOctets,
       "pxmTC7NwIntfPmQueueingTransmitPkts": pxmTC7NwIntfPmQueueingTransmitPkts,
       "pxmTC7NwIntfPmQueueingTransmitOctets": pxmTC7NwIntfPmQueueingTransmitOctets,
       "pxmTCANYNwIntfPmTable": pxmTCANYNwIntfPmTable,
       "pxmTCANYNwIntfPmEntry": pxmTCANYNwIntfPmEntry,
       "pxmTCANYNwIntfPmTimestamp": pxmTCANYNwIntfPmTimestamp,
       "pxmTCANYNwIntfPmSampleDuration": pxmTCANYNwIntfPmSampleDuration,
       "pxmTCANYNwIntfPmValidity": pxmTCANYNwIntfPmValidity,
       "pxmTCANYNwIntfPmTCNum": pxmTCANYNwIntfPmTCNum,
       "pxmTCANYNwIntfPmQueueingDiscardOctets": pxmTCANYNwIntfPmQueueingDiscardOctets,
       "pxmTCANYNwIntfPmQueueingDiscardPkts": pxmTCANYNwIntfPmQueueingDiscardPkts,
       "pxmTCANYNwIntfPmRandomGreenDropPkts": pxmTCANYNwIntfPmRandomGreenDropPkts,
       "pxmTCANYNwIntfPmRandomGreenDropOctets": pxmTCANYNwIntfPmRandomGreenDropOctets,
       "pxmTCANYNwIntfPmRandomYellowDropPkts": pxmTCANYNwIntfPmRandomYellowDropPkts,
       "pxmTCANYNwIntfPmRandomYellowDropOctets": pxmTCANYNwIntfPmRandomYellowDropOctets,
       "pxmTCANYNwIntfPmQueueingTransmitPkts": pxmTCANYNwIntfPmQueueingTransmitPkts,
       "pxmTCANYNwIntfPmQueueingTransmitOctets": pxmTCANYNwIntfPmQueueingTransmitOctets,
       "pxmNwIntfPmConformance": pxmNwIntfPmConformance,
       "pxmNwIntfPmCompliances": pxmNwIntfPmCompliances,
       "pxmNwIntfPmCompliance": pxmNwIntfPmCompliance,
       "pxmNwIntfPmRealCompliance": pxmNwIntfPmRealCompliance,
       "pxmNwIntfPmGroups": pxmNwIntfPmGroups,
       "pxmNwIntfPmGroup": pxmNwIntfPmGroup,
       "pxmNwIntfPmRealGroup": pxmNwIntfPmRealGroup,
       "pxmTC0NwIntfPmGroup": pxmTC0NwIntfPmGroup,
       "pxmTC0NwIntfPmRealGroup": pxmTC0NwIntfPmRealGroup,
       "pxmTC2NwIntfPmGroup": pxmTC2NwIntfPmGroup,
       "pxmTC2NwIntfPmRealGroup": pxmTC2NwIntfPmRealGroup,
       "pxmTC4NwIntfPmGroup": pxmTC4NwIntfPmGroup,
       "pxmTC4NwIntfPmRealGroup": pxmTC4NwIntfPmRealGroup,
       "pxmTC6NwIntfPmGroup": pxmTC6NwIntfPmGroup,
       "pxmTC6NwIntfPmRealGroup": pxmTC6NwIntfPmRealGroup,
       "pxmTC7NwIntfPmGroup": pxmTC7NwIntfPmGroup,
       "pxmTC7NwIntfPmRealGroup": pxmTC7NwIntfPmRealGroup,
       "pxmTCANYNwIntfPmGroup": pxmTCANYNwIntfPmGroup,
       "pxmTCANYNwIntfPmRealGroup": pxmTCANYNwIntfPmRealGroup}
)
