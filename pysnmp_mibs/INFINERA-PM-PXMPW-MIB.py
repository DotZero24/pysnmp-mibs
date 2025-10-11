# SNMP MIB module (INFINERA-PM-PXMPW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-PXMPW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:55 2025
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

pxmPwPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96)
)
if mibBuilder.loadTexts:
    pxmPwPmMIB.setRevisions(
        ("2015-02-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmPwRmonPm_ObjectIdentity = ObjectIdentity
pxmPwRmonPm = _PxmPwRmonPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1)
)
_PxmPwPmRealTable_Object = MibTable
pxmPwPmRealTable = _PxmPwPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 1)
)
if mibBuilder.loadTexts:
    pxmPwPmRealTable.setStatus("current")
_PxmPwPmRealEntry_Object = MibTableRow
pxmPwPmRealEntry = _PxmPwPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 1, 1)
)
pxmPwPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmPwPmRealEntry.setStatus("current")
_PxmPwPmRealRxPackets_Type = Counter64
_PxmPwPmRealRxPackets_Object = MibTableColumn
pxmPwPmRealRxPackets = _PxmPwPmRealRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 1, 1, 1),
    _PxmPwPmRealRxPackets_Type()
)
pxmPwPmRealRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmRealRxPackets.setStatus("current")
_PxmPwPmRealRxOctets_Type = Counter64
_PxmPwPmRealRxOctets_Object = MibTableColumn
pxmPwPmRealRxOctets = _PxmPwPmRealRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 1, 1, 2),
    _PxmPwPmRealRxOctets_Type()
)
pxmPwPmRealRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmRealRxOctets.setStatus("current")
_PxmPwPmRealTxPackets_Type = Counter64
_PxmPwPmRealTxPackets_Object = MibTableColumn
pxmPwPmRealTxPackets = _PxmPwPmRealTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 1, 1, 3),
    _PxmPwPmRealTxPackets_Type()
)
pxmPwPmRealTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmRealTxPackets.setStatus("current")
_PxmPwPmRealTxOctets_Type = Counter64
_PxmPwPmRealTxOctets_Object = MibTableColumn
pxmPwPmRealTxOctets = _PxmPwPmRealTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 1, 1, 4),
    _PxmPwPmRealTxOctets_Type()
)
pxmPwPmRealTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmRealTxOctets.setStatus("current")
_PxmPwPmTable_Object = MibTable
pxmPwPmTable = _PxmPwPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2)
)
if mibBuilder.loadTexts:
    pxmPwPmTable.setStatus("current")
_PxmPwPmEntry_Object = MibTableRow
pxmPwPmEntry = _PxmPwPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2, 1)
)
pxmPwPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmPwPmSampleDuration"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmPwPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmPwPmEntry.setStatus("current")


class _PxmPwPmTimestamp_Type(Integer32):
    """Custom type pxmPwPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmPwPmTimestamp_Type.__name__ = "Integer32"
_PxmPwPmTimestamp_Object = MibTableColumn
pxmPwPmTimestamp = _PxmPwPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2, 1, 1),
    _PxmPwPmTimestamp_Type()
)
pxmPwPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmPwPmTimestamp.setStatus("current")


class _PxmPwPmSampleDuration_Type(Integer32):
    """Custom type pxmPwPmSampleDuration based on Integer32"""
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


_PxmPwPmSampleDuration_Type.__name__ = "Integer32"
_PxmPwPmSampleDuration_Object = MibTableColumn
pxmPwPmSampleDuration = _PxmPwPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2, 1, 2),
    _PxmPwPmSampleDuration_Type()
)
pxmPwPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmPwPmSampleDuration.setStatus("current")
_PxmPwPmValidity_Type = TruthValue
_PxmPwPmValidity_Object = MibTableColumn
pxmPwPmValidity = _PxmPwPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2, 1, 3),
    _PxmPwPmValidity_Type()
)
pxmPwPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmValidity.setStatus("current")
_PxmPwPmRxPackets_Type = HCPerfIntervalCount
_PxmPwPmRxPackets_Object = MibTableColumn
pxmPwPmRxPackets = _PxmPwPmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2, 1, 4),
    _PxmPwPmRxPackets_Type()
)
pxmPwPmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmRxPackets.setStatus("current")
_PxmPwPmRxOctets_Type = HCPerfIntervalCount
_PxmPwPmRxOctets_Object = MibTableColumn
pxmPwPmRxOctets = _PxmPwPmRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2, 1, 5),
    _PxmPwPmRxOctets_Type()
)
pxmPwPmRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmRxOctets.setStatus("current")
_PxmPwPmTxPackets_Type = HCPerfIntervalCount
_PxmPwPmTxPackets_Object = MibTableColumn
pxmPwPmTxPackets = _PxmPwPmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2, 1, 6),
    _PxmPwPmTxPackets_Type()
)
pxmPwPmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmTxPackets.setStatus("current")
_PxmPwPmTxOctets_Type = HCPerfIntervalCount
_PxmPwPmTxOctets_Object = MibTableColumn
pxmPwPmTxOctets = _PxmPwPmTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 1, 2, 1, 7),
    _PxmPwPmTxOctets_Type()
)
pxmPwPmTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwPmTxOctets.setStatus("current")
_PxmCmPwPmObjects_ObjectIdentity = ObjectIdentity
pxmCmPwPmObjects = _PxmCmPwPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2)
)
_PxmCmPwRealPm_ObjectIdentity = ObjectIdentity
pxmCmPwRealPm = _PxmCmPwRealPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1)
)
_PxmTC0PwPmRealTable_Object = MibTable
pxmTC0PwPmRealTable = _PxmTC0PwPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pxmTC0PwPmRealTable.setStatus("current")
_PxmTC0PwPmRealEntry_Object = MibTableRow
pxmTC0PwPmRealEntry = _PxmTC0PwPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1)
)
pxmTC0PwPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC0PwPmRealEntry.setStatus("current")
_PxmTC0PwPmRealTCNum_Type = Integer32
_PxmTC0PwPmRealTCNum_Object = MibTableColumn
pxmTC0PwPmRealTCNum = _PxmTC0PwPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 1),
    _PxmTC0PwPmRealTCNum_Type()
)
pxmTC0PwPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealTCNum.setStatus("current")
_PxmTC0PwPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC0PwPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC0PwPmRealTDQueuingCurrentQDepth = _PxmTC0PwPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 2),
    _PxmTC0PwPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC0PwPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC0PwPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC0PwPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC0PwPmRealQueueingDiscardOctets = _PxmTC0PwPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 3),
    _PxmTC0PwPmRealQueueingDiscardOctets_Type()
)
pxmTC0PwPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC0PwPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC0PwPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC0PwPmRealQueueingDiscardPkts = _PxmTC0PwPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 4),
    _PxmTC0PwPmRealQueueingDiscardPkts_Type()
)
pxmTC0PwPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC0PwPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC0PwPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC0PwPmRealRandomGreenDropPkts = _PxmTC0PwPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 5),
    _PxmTC0PwPmRealRandomGreenDropPkts_Type()
)
pxmTC0PwPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC0PwPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC0PwPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC0PwPmRealRandomGreenDropOctets = _PxmTC0PwPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 6),
    _PxmTC0PwPmRealRandomGreenDropOctets_Type()
)
pxmTC0PwPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC0PwPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC0PwPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC0PwPmRealRandomYellowDropPkts = _PxmTC0PwPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 7),
    _PxmTC0PwPmRealRandomYellowDropPkts_Type()
)
pxmTC0PwPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC0PwPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC0PwPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC0PwPmRealRandomYellowDropOctets = _PxmTC0PwPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 8),
    _PxmTC0PwPmRealRandomYellowDropOctets_Type()
)
pxmTC0PwPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC0PwPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC0PwPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC0PwPmRealQueueingTransmitPkts = _PxmTC0PwPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 9),
    _PxmTC0PwPmRealQueueingTransmitPkts_Type()
)
pxmTC0PwPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC0PwPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC0PwPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC0PwPmRealQueueingTransmitOctets = _PxmTC0PwPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 10),
    _PxmTC0PwPmRealQueueingTransmitOctets_Type()
)
pxmTC0PwPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC0PwPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC0PwPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC0PwPmRealQueueingMeanQSizeUnit = _PxmTC0PwPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 11),
    _PxmTC0PwPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC0PwPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC0PwPmRealMeanQSize_Type = Integer32
_PxmTC0PwPmRealMeanQSize_Object = MibTableColumn
pxmTC0PwPmRealMeanQSize = _PxmTC0PwPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 1, 1, 12),
    _PxmTC0PwPmRealMeanQSize_Type()
)
pxmTC0PwPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRealMeanQSize.setStatus("current")
_PxmTC2PwPmRealTable_Object = MibTable
pxmTC2PwPmRealTable = _PxmTC2PwPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pxmTC2PwPmRealTable.setStatus("current")
_PxmTC2PwPmRealEntry_Object = MibTableRow
pxmTC2PwPmRealEntry = _PxmTC2PwPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1)
)
pxmTC2PwPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC2PwPmRealEntry.setStatus("current")
_PxmTC2PwPmRealTCNum_Type = Integer32
_PxmTC2PwPmRealTCNum_Object = MibTableColumn
pxmTC2PwPmRealTCNum = _PxmTC2PwPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 1),
    _PxmTC2PwPmRealTCNum_Type()
)
pxmTC2PwPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealTCNum.setStatus("current")
_PxmTC2PwPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC2PwPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC2PwPmRealTDQueuingCurrentQDepth = _PxmTC2PwPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 2),
    _PxmTC2PwPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC2PwPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC2PwPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC2PwPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC2PwPmRealQueueingDiscardOctets = _PxmTC2PwPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 3),
    _PxmTC2PwPmRealQueueingDiscardOctets_Type()
)
pxmTC2PwPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC2PwPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC2PwPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC2PwPmRealQueueingDiscardPkts = _PxmTC2PwPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 4),
    _PxmTC2PwPmRealQueueingDiscardPkts_Type()
)
pxmTC2PwPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC2PwPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC2PwPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC2PwPmRealRandomGreenDropPkts = _PxmTC2PwPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 5),
    _PxmTC2PwPmRealRandomGreenDropPkts_Type()
)
pxmTC2PwPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC2PwPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC2PwPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC2PwPmRealRandomGreenDropOctets = _PxmTC2PwPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 6),
    _PxmTC2PwPmRealRandomGreenDropOctets_Type()
)
pxmTC2PwPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC2PwPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC2PwPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC2PwPmRealRandomYellowDropPkts = _PxmTC2PwPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 7),
    _PxmTC2PwPmRealRandomYellowDropPkts_Type()
)
pxmTC2PwPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC2PwPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC2PwPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC2PwPmRealRandomYellowDropOctets = _PxmTC2PwPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 8),
    _PxmTC2PwPmRealRandomYellowDropOctets_Type()
)
pxmTC2PwPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC2PwPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC2PwPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC2PwPmRealQueueingTransmitPkts = _PxmTC2PwPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 9),
    _PxmTC2PwPmRealQueueingTransmitPkts_Type()
)
pxmTC2PwPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC2PwPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC2PwPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC2PwPmRealQueueingTransmitOctets = _PxmTC2PwPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 10),
    _PxmTC2PwPmRealQueueingTransmitOctets_Type()
)
pxmTC2PwPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC2PwPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC2PwPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC2PwPmRealQueueingMeanQSizeUnit = _PxmTC2PwPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 11),
    _PxmTC2PwPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC2PwPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC2PwPmRealMeanQSize_Type = Integer32
_PxmTC2PwPmRealMeanQSize_Object = MibTableColumn
pxmTC2PwPmRealMeanQSize = _PxmTC2PwPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 2, 1, 12),
    _PxmTC2PwPmRealMeanQSize_Type()
)
pxmTC2PwPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRealMeanQSize.setStatus("current")
_PxmTC4PwPmRealTable_Object = MibTable
pxmTC4PwPmRealTable = _PxmTC4PwPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pxmTC4PwPmRealTable.setStatus("current")
_PxmTC4PwPmRealEntry_Object = MibTableRow
pxmTC4PwPmRealEntry = _PxmTC4PwPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1)
)
pxmTC4PwPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC4PwPmRealEntry.setStatus("current")
_PxmTC4PwPmRealTCNum_Type = Integer32
_PxmTC4PwPmRealTCNum_Object = MibTableColumn
pxmTC4PwPmRealTCNum = _PxmTC4PwPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 1),
    _PxmTC4PwPmRealTCNum_Type()
)
pxmTC4PwPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealTCNum.setStatus("current")
_PxmTC4PwPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC4PwPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC4PwPmRealTDQueuingCurrentQDepth = _PxmTC4PwPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 2),
    _PxmTC4PwPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC4PwPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC4PwPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC4PwPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC4PwPmRealQueueingDiscardOctets = _PxmTC4PwPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 3),
    _PxmTC4PwPmRealQueueingDiscardOctets_Type()
)
pxmTC4PwPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC4PwPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC4PwPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC4PwPmRealQueueingDiscardPkts = _PxmTC4PwPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 4),
    _PxmTC4PwPmRealQueueingDiscardPkts_Type()
)
pxmTC4PwPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC4PwPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC4PwPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC4PwPmRealRandomGreenDropPkts = _PxmTC4PwPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 5),
    _PxmTC4PwPmRealRandomGreenDropPkts_Type()
)
pxmTC4PwPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC4PwPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC4PwPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC4PwPmRealRandomGreenDropOctets = _PxmTC4PwPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 6),
    _PxmTC4PwPmRealRandomGreenDropOctets_Type()
)
pxmTC4PwPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC4PwPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC4PwPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC4PwPmRealRandomYellowDropPkts = _PxmTC4PwPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 7),
    _PxmTC4PwPmRealRandomYellowDropPkts_Type()
)
pxmTC4PwPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC4PwPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC4PwPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC4PwPmRealRandomYellowDropOctets = _PxmTC4PwPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 8),
    _PxmTC4PwPmRealRandomYellowDropOctets_Type()
)
pxmTC4PwPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC4PwPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC4PwPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC4PwPmRealQueueingTransmitPkts = _PxmTC4PwPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 9),
    _PxmTC4PwPmRealQueueingTransmitPkts_Type()
)
pxmTC4PwPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC4PwPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC4PwPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC4PwPmRealQueueingTransmitOctets = _PxmTC4PwPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 10),
    _PxmTC4PwPmRealQueueingTransmitOctets_Type()
)
pxmTC4PwPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC4PwPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC4PwPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC4PwPmRealQueueingMeanQSizeUnit = _PxmTC4PwPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 11),
    _PxmTC4PwPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC4PwPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC4PwPmRealMeanQSize_Type = Integer32
_PxmTC4PwPmRealMeanQSize_Object = MibTableColumn
pxmTC4PwPmRealMeanQSize = _PxmTC4PwPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 3, 1, 12),
    _PxmTC4PwPmRealMeanQSize_Type()
)
pxmTC4PwPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRealMeanQSize.setStatus("current")
_PxmTC6PwPmRealTable_Object = MibTable
pxmTC6PwPmRealTable = _PxmTC6PwPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4)
)
if mibBuilder.loadTexts:
    pxmTC6PwPmRealTable.setStatus("current")
_PxmTC6PwPmRealEntry_Object = MibTableRow
pxmTC6PwPmRealEntry = _PxmTC6PwPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1)
)
pxmTC6PwPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC6PwPmRealEntry.setStatus("current")
_PxmTC6PwPmRealTCNum_Type = Integer32
_PxmTC6PwPmRealTCNum_Object = MibTableColumn
pxmTC6PwPmRealTCNum = _PxmTC6PwPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 1),
    _PxmTC6PwPmRealTCNum_Type()
)
pxmTC6PwPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealTCNum.setStatus("current")
_PxmTC6PwPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC6PwPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC6PwPmRealTDQueuingCurrentQDepth = _PxmTC6PwPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 2),
    _PxmTC6PwPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC6PwPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC6PwPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC6PwPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC6PwPmRealQueueingDiscardOctets = _PxmTC6PwPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 3),
    _PxmTC6PwPmRealQueueingDiscardOctets_Type()
)
pxmTC6PwPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC6PwPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC6PwPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC6PwPmRealQueueingDiscardPkts = _PxmTC6PwPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 4),
    _PxmTC6PwPmRealQueueingDiscardPkts_Type()
)
pxmTC6PwPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC6PwPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC6PwPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC6PwPmRealRandomGreenDropPkts = _PxmTC6PwPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 5),
    _PxmTC6PwPmRealRandomGreenDropPkts_Type()
)
pxmTC6PwPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC6PwPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC6PwPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC6PwPmRealRandomGreenDropOctets = _PxmTC6PwPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 6),
    _PxmTC6PwPmRealRandomGreenDropOctets_Type()
)
pxmTC6PwPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC6PwPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC6PwPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC6PwPmRealRandomYellowDropPkts = _PxmTC6PwPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 7),
    _PxmTC6PwPmRealRandomYellowDropPkts_Type()
)
pxmTC6PwPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC6PwPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC6PwPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC6PwPmRealRandomYellowDropOctets = _PxmTC6PwPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 8),
    _PxmTC6PwPmRealRandomYellowDropOctets_Type()
)
pxmTC6PwPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC6PwPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC6PwPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC6PwPmRealQueueingTransmitPkts = _PxmTC6PwPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 9),
    _PxmTC6PwPmRealQueueingTransmitPkts_Type()
)
pxmTC6PwPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC6PwPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC6PwPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC6PwPmRealQueueingTransmitOctets = _PxmTC6PwPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 10),
    _PxmTC6PwPmRealQueueingTransmitOctets_Type()
)
pxmTC6PwPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC6PwPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC6PwPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC6PwPmRealQueueingMeanQSizeUnit = _PxmTC6PwPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 11),
    _PxmTC6PwPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC6PwPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC6PwPmRealMeanQSize_Type = Integer32
_PxmTC6PwPmRealMeanQSize_Object = MibTableColumn
pxmTC6PwPmRealMeanQSize = _PxmTC6PwPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 4, 1, 12),
    _PxmTC6PwPmRealMeanQSize_Type()
)
pxmTC6PwPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRealMeanQSize.setStatus("current")
_PxmTC7PwPmRealTable_Object = MibTable
pxmTC7PwPmRealTable = _PxmTC7PwPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5)
)
if mibBuilder.loadTexts:
    pxmTC7PwPmRealTable.setStatus("current")
_PxmTC7PwPmRealEntry_Object = MibTableRow
pxmTC7PwPmRealEntry = _PxmTC7PwPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1)
)
pxmTC7PwPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC7PwPmRealEntry.setStatus("current")
_PxmTC7PwPmRealTCNum_Type = Integer32
_PxmTC7PwPmRealTCNum_Object = MibTableColumn
pxmTC7PwPmRealTCNum = _PxmTC7PwPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 1),
    _PxmTC7PwPmRealTCNum_Type()
)
pxmTC7PwPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealTCNum.setStatus("current")
_PxmTC7PwPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC7PwPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC7PwPmRealTDQueuingCurrentQDepth = _PxmTC7PwPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 2),
    _PxmTC7PwPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC7PwPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC7PwPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC7PwPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC7PwPmRealQueueingDiscardOctets = _PxmTC7PwPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 3),
    _PxmTC7PwPmRealQueueingDiscardOctets_Type()
)
pxmTC7PwPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC7PwPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC7PwPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC7PwPmRealQueueingDiscardPkts = _PxmTC7PwPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 4),
    _PxmTC7PwPmRealQueueingDiscardPkts_Type()
)
pxmTC7PwPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC7PwPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC7PwPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC7PwPmRealRandomGreenDropPkts = _PxmTC7PwPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 5),
    _PxmTC7PwPmRealRandomGreenDropPkts_Type()
)
pxmTC7PwPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC7PwPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC7PwPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC7PwPmRealRandomGreenDropOctets = _PxmTC7PwPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 6),
    _PxmTC7PwPmRealRandomGreenDropOctets_Type()
)
pxmTC7PwPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC7PwPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC7PwPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC7PwPmRealRandomYellowDropPkts = _PxmTC7PwPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 7),
    _PxmTC7PwPmRealRandomYellowDropPkts_Type()
)
pxmTC7PwPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC7PwPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC7PwPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC7PwPmRealRandomYellowDropOctets = _PxmTC7PwPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 8),
    _PxmTC7PwPmRealRandomYellowDropOctets_Type()
)
pxmTC7PwPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC7PwPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC7PwPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC7PwPmRealQueueingTransmitPkts = _PxmTC7PwPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 9),
    _PxmTC7PwPmRealQueueingTransmitPkts_Type()
)
pxmTC7PwPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC7PwPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC7PwPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC7PwPmRealQueueingTransmitOctets = _PxmTC7PwPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 10),
    _PxmTC7PwPmRealQueueingTransmitOctets_Type()
)
pxmTC7PwPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC7PwPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC7PwPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC7PwPmRealQueueingMeanQSizeUnit = _PxmTC7PwPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 11),
    _PxmTC7PwPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC7PwPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC7PwPmRealMeanQSize_Type = Integer32
_PxmTC7PwPmRealMeanQSize_Object = MibTableColumn
pxmTC7PwPmRealMeanQSize = _PxmTC7PwPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 5, 1, 12),
    _PxmTC7PwPmRealMeanQSize_Type()
)
pxmTC7PwPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRealMeanQSize.setStatus("current")
_PxmTCANYPwPmRealTable_Object = MibTable
pxmTCANYPwPmRealTable = _PxmTCANYPwPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6)
)
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealTable.setStatus("current")
_PxmTCANYPwPmRealEntry_Object = MibTableRow
pxmTCANYPwPmRealEntry = _PxmTCANYPwPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1)
)
pxmTCANYPwPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealEntry.setStatus("current")
_PxmTCANYPwPmRealTCNum_Type = Integer32
_PxmTCANYPwPmRealTCNum_Object = MibTableColumn
pxmTCANYPwPmRealTCNum = _PxmTCANYPwPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 1),
    _PxmTCANYPwPmRealTCNum_Type()
)
pxmTCANYPwPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealTCNum.setStatus("current")
_PxmTCANYPwPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTCANYPwPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTCANYPwPmRealTDQueuingCurrentQDepth = _PxmTCANYPwPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 2),
    _PxmTCANYPwPmRealTDQueuingCurrentQDepth_Type()
)
pxmTCANYPwPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTCANYPwPmRealQueueingDiscardOctets_Type = Counter64
_PxmTCANYPwPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTCANYPwPmRealQueueingDiscardOctets = _PxmTCANYPwPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 3),
    _PxmTCANYPwPmRealQueueingDiscardOctets_Type()
)
pxmTCANYPwPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealQueueingDiscardOctets.setStatus("current")
_PxmTCANYPwPmRealQueueingDiscardPkts_Type = Integer32
_PxmTCANYPwPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTCANYPwPmRealQueueingDiscardPkts = _PxmTCANYPwPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 4),
    _PxmTCANYPwPmRealQueueingDiscardPkts_Type()
)
pxmTCANYPwPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealQueueingDiscardPkts.setStatus("current")
_PxmTCANYPwPmRealRandomGreenDropPkts_Type = Counter64
_PxmTCANYPwPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTCANYPwPmRealRandomGreenDropPkts = _PxmTCANYPwPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 5),
    _PxmTCANYPwPmRealRandomGreenDropPkts_Type()
)
pxmTCANYPwPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealRandomGreenDropPkts.setStatus("current")
_PxmTCANYPwPmRealRandomGreenDropOctets_Type = Counter64
_PxmTCANYPwPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTCANYPwPmRealRandomGreenDropOctets = _PxmTCANYPwPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 6),
    _PxmTCANYPwPmRealRandomGreenDropOctets_Type()
)
pxmTCANYPwPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealRandomGreenDropOctets.setStatus("current")
_PxmTCANYPwPmRealRandomYellowDropPkts_Type = Counter64
_PxmTCANYPwPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTCANYPwPmRealRandomYellowDropPkts = _PxmTCANYPwPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 7),
    _PxmTCANYPwPmRealRandomYellowDropPkts_Type()
)
pxmTCANYPwPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealRandomYellowDropPkts.setStatus("current")
_PxmTCANYPwPmRealRandomYellowDropOctets_Type = Counter64
_PxmTCANYPwPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTCANYPwPmRealRandomYellowDropOctets = _PxmTCANYPwPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 8),
    _PxmTCANYPwPmRealRandomYellowDropOctets_Type()
)
pxmTCANYPwPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealRandomYellowDropOctets.setStatus("current")
_PxmTCANYPwPmRealQueueingTransmitPkts_Type = Counter64
_PxmTCANYPwPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTCANYPwPmRealQueueingTransmitPkts = _PxmTCANYPwPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 9),
    _PxmTCANYPwPmRealQueueingTransmitPkts_Type()
)
pxmTCANYPwPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealQueueingTransmitPkts.setStatus("current")
_PxmTCANYPwPmRealQueueingTransmitOctets_Type = Counter64
_PxmTCANYPwPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTCANYPwPmRealQueueingTransmitOctets = _PxmTCANYPwPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 10),
    _PxmTCANYPwPmRealQueueingTransmitOctets_Type()
)
pxmTCANYPwPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealQueueingTransmitOctets.setStatus("current")
_PxmTCANYPwPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTCANYPwPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTCANYPwPmRealQueueingMeanQSizeUnit = _PxmTCANYPwPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 11),
    _PxmTCANYPwPmRealQueueingMeanQSizeUnit_Type()
)
pxmTCANYPwPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTCANYPwPmRealMeanQSize_Type = Integer32
_PxmTCANYPwPmRealMeanQSize_Object = MibTableColumn
pxmTCANYPwPmRealMeanQSize = _PxmTCANYPwPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 1, 6, 1, 12),
    _PxmTCANYPwPmRealMeanQSize_Type()
)
pxmTCANYPwPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealMeanQSize.setStatus("current")
_PxmCmPwPm_ObjectIdentity = ObjectIdentity
pxmCmPwPm = _PxmCmPwPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2)
)
_PxmTC0PwPmTable_Object = MibTable
pxmTC0PwPmTable = _PxmTC0PwPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pxmTC0PwPmTable.setStatus("current")
_PxmTC0PwPmEntry_Object = MibTableRow
pxmTC0PwPmEntry = _PxmTC0PwPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1)
)
pxmTC0PwPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmSampleDuration"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC0PwPmEntry.setStatus("current")


class _PxmTC0PwPmTimestamp_Type(Integer32):
    """Custom type pxmTC0PwPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC0PwPmTimestamp_Type.__name__ = "Integer32"
_PxmTC0PwPmTimestamp_Object = MibTableColumn
pxmTC0PwPmTimestamp = _PxmTC0PwPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 1),
    _PxmTC0PwPmTimestamp_Type()
)
pxmTC0PwPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC0PwPmTimestamp.setStatus("current")


class _PxmTC0PwPmSampleDuration_Type(Integer32):
    """Custom type pxmTC0PwPmSampleDuration based on Integer32"""
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


_PxmTC0PwPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC0PwPmSampleDuration_Object = MibTableColumn
pxmTC0PwPmSampleDuration = _PxmTC0PwPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 2),
    _PxmTC0PwPmSampleDuration_Type()
)
pxmTC0PwPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC0PwPmSampleDuration.setStatus("current")
_PxmTC0PwPmValidity_Type = TruthValue
_PxmTC0PwPmValidity_Object = MibTableColumn
pxmTC0PwPmValidity = _PxmTC0PwPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 3),
    _PxmTC0PwPmValidity_Type()
)
pxmTC0PwPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmValidity.setStatus("current")
_PxmTC0PwPmTCNum_Type = Integer32
_PxmTC0PwPmTCNum_Object = MibTableColumn
pxmTC0PwPmTCNum = _PxmTC0PwPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 4),
    _PxmTC0PwPmTCNum_Type()
)
pxmTC0PwPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmTCNum.setStatus("current")
_PxmTC0PwPmQueueingDiscardOctets_Type = Counter64
_PxmTC0PwPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC0PwPmQueueingDiscardOctets = _PxmTC0PwPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 5),
    _PxmTC0PwPmQueueingDiscardOctets_Type()
)
pxmTC0PwPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmQueueingDiscardOctets.setStatus("current")
_PxmTC0PwPmQueueingDiscardPkts_Type = Integer32
_PxmTC0PwPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC0PwPmQueueingDiscardPkts = _PxmTC0PwPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 6),
    _PxmTC0PwPmQueueingDiscardPkts_Type()
)
pxmTC0PwPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmQueueingDiscardPkts.setStatus("current")
_PxmTC0PwPmRandomGreenDropPkts_Type = Counter64
_PxmTC0PwPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC0PwPmRandomGreenDropPkts = _PxmTC0PwPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 7),
    _PxmTC0PwPmRandomGreenDropPkts_Type()
)
pxmTC0PwPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRandomGreenDropPkts.setStatus("current")
_PxmTC0PwPmRandomGreenDropOctets_Type = Counter64
_PxmTC0PwPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC0PwPmRandomGreenDropOctets = _PxmTC0PwPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 8),
    _PxmTC0PwPmRandomGreenDropOctets_Type()
)
pxmTC0PwPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRandomGreenDropOctets.setStatus("current")
_PxmTC0PwPmRandomYellowDropPkts_Type = Counter64
_PxmTC0PwPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC0PwPmRandomYellowDropPkts = _PxmTC0PwPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 9),
    _PxmTC0PwPmRandomYellowDropPkts_Type()
)
pxmTC0PwPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRandomYellowDropPkts.setStatus("current")
_PxmTC0PwPmRandomYellowDropOctets_Type = Counter64
_PxmTC0PwPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC0PwPmRandomYellowDropOctets = _PxmTC0PwPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 10),
    _PxmTC0PwPmRandomYellowDropOctets_Type()
)
pxmTC0PwPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmRandomYellowDropOctets.setStatus("current")
_PxmTC0PwPmQueueingTransmitPkts_Type = Counter64
_PxmTC0PwPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC0PwPmQueueingTransmitPkts = _PxmTC0PwPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 11),
    _PxmTC0PwPmQueueingTransmitPkts_Type()
)
pxmTC0PwPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmQueueingTransmitPkts.setStatus("current")
_PxmTC0PwPmQueueingTransmitOctets_Type = Counter64
_PxmTC0PwPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC0PwPmQueueingTransmitOctets = _PxmTC0PwPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 1, 1, 12),
    _PxmTC0PwPmQueueingTransmitOctets_Type()
)
pxmTC0PwPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0PwPmQueueingTransmitOctets.setStatus("current")
_PxmTC2PwPmTable_Object = MibTable
pxmTC2PwPmTable = _PxmTC2PwPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pxmTC2PwPmTable.setStatus("current")
_PxmTC2PwPmEntry_Object = MibTableRow
pxmTC2PwPmEntry = _PxmTC2PwPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1)
)
pxmTC2PwPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmSampleDuration"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC2PwPmEntry.setStatus("current")


class _PxmTC2PwPmTimestamp_Type(Integer32):
    """Custom type pxmTC2PwPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC2PwPmTimestamp_Type.__name__ = "Integer32"
_PxmTC2PwPmTimestamp_Object = MibTableColumn
pxmTC2PwPmTimestamp = _PxmTC2PwPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 1),
    _PxmTC2PwPmTimestamp_Type()
)
pxmTC2PwPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC2PwPmTimestamp.setStatus("current")


class _PxmTC2PwPmSampleDuration_Type(Integer32):
    """Custom type pxmTC2PwPmSampleDuration based on Integer32"""
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


_PxmTC2PwPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC2PwPmSampleDuration_Object = MibTableColumn
pxmTC2PwPmSampleDuration = _PxmTC2PwPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 2),
    _PxmTC2PwPmSampleDuration_Type()
)
pxmTC2PwPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC2PwPmSampleDuration.setStatus("current")
_PxmTC2PwPmValidity_Type = TruthValue
_PxmTC2PwPmValidity_Object = MibTableColumn
pxmTC2PwPmValidity = _PxmTC2PwPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 3),
    _PxmTC2PwPmValidity_Type()
)
pxmTC2PwPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmValidity.setStatus("current")
_PxmTC2PwPmTCNum_Type = Integer32
_PxmTC2PwPmTCNum_Object = MibTableColumn
pxmTC2PwPmTCNum = _PxmTC2PwPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 4),
    _PxmTC2PwPmTCNum_Type()
)
pxmTC2PwPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmTCNum.setStatus("current")
_PxmTC2PwPmQueueingDiscardOctets_Type = Counter64
_PxmTC2PwPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC2PwPmQueueingDiscardOctets = _PxmTC2PwPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 5),
    _PxmTC2PwPmQueueingDiscardOctets_Type()
)
pxmTC2PwPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmQueueingDiscardOctets.setStatus("current")
_PxmTC2PwPmQueueingDiscardPkts_Type = Integer32
_PxmTC2PwPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC2PwPmQueueingDiscardPkts = _PxmTC2PwPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 6),
    _PxmTC2PwPmQueueingDiscardPkts_Type()
)
pxmTC2PwPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmQueueingDiscardPkts.setStatus("current")
_PxmTC2PwPmRandomGreenDropPkts_Type = Counter64
_PxmTC2PwPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC2PwPmRandomGreenDropPkts = _PxmTC2PwPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 7),
    _PxmTC2PwPmRandomGreenDropPkts_Type()
)
pxmTC2PwPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRandomGreenDropPkts.setStatus("current")
_PxmTC2PwPmRandomGreenDropOctets_Type = Counter64
_PxmTC2PwPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC2PwPmRandomGreenDropOctets = _PxmTC2PwPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 8),
    _PxmTC2PwPmRandomGreenDropOctets_Type()
)
pxmTC2PwPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRandomGreenDropOctets.setStatus("current")
_PxmTC2PwPmRandomYellowDropPkts_Type = Counter64
_PxmTC2PwPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC2PwPmRandomYellowDropPkts = _PxmTC2PwPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 9),
    _PxmTC2PwPmRandomYellowDropPkts_Type()
)
pxmTC2PwPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRandomYellowDropPkts.setStatus("current")
_PxmTC2PwPmRandomYellowDropOctets_Type = Counter64
_PxmTC2PwPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC2PwPmRandomYellowDropOctets = _PxmTC2PwPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 10),
    _PxmTC2PwPmRandomYellowDropOctets_Type()
)
pxmTC2PwPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmRandomYellowDropOctets.setStatus("current")
_PxmTC2PwPmQueueingTransmitPkts_Type = Counter64
_PxmTC2PwPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC2PwPmQueueingTransmitPkts = _PxmTC2PwPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 11),
    _PxmTC2PwPmQueueingTransmitPkts_Type()
)
pxmTC2PwPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmQueueingTransmitPkts.setStatus("current")
_PxmTC2PwPmQueueingTransmitOctets_Type = Counter64
_PxmTC2PwPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC2PwPmQueueingTransmitOctets = _PxmTC2PwPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 2, 1, 12),
    _PxmTC2PwPmQueueingTransmitOctets_Type()
)
pxmTC2PwPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2PwPmQueueingTransmitOctets.setStatus("current")
_PxmTC4PwPmTable_Object = MibTable
pxmTC4PwPmTable = _PxmTC4PwPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pxmTC4PwPmTable.setStatus("current")
_PxmTC4PwPmEntry_Object = MibTableRow
pxmTC4PwPmEntry = _PxmTC4PwPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1)
)
pxmTC4PwPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmSampleDuration"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC4PwPmEntry.setStatus("current")


class _PxmTC4PwPmTimestamp_Type(Integer32):
    """Custom type pxmTC4PwPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC4PwPmTimestamp_Type.__name__ = "Integer32"
_PxmTC4PwPmTimestamp_Object = MibTableColumn
pxmTC4PwPmTimestamp = _PxmTC4PwPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 1),
    _PxmTC4PwPmTimestamp_Type()
)
pxmTC4PwPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC4PwPmTimestamp.setStatus("current")


class _PxmTC4PwPmSampleDuration_Type(Integer32):
    """Custom type pxmTC4PwPmSampleDuration based on Integer32"""
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


_PxmTC4PwPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC4PwPmSampleDuration_Object = MibTableColumn
pxmTC4PwPmSampleDuration = _PxmTC4PwPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 2),
    _PxmTC4PwPmSampleDuration_Type()
)
pxmTC4PwPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC4PwPmSampleDuration.setStatus("current")
_PxmTC4PwPmValidity_Type = TruthValue
_PxmTC4PwPmValidity_Object = MibTableColumn
pxmTC4PwPmValidity = _PxmTC4PwPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 3),
    _PxmTC4PwPmValidity_Type()
)
pxmTC4PwPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmValidity.setStatus("current")
_PxmTC4PwPmTCNum_Type = Integer32
_PxmTC4PwPmTCNum_Object = MibTableColumn
pxmTC4PwPmTCNum = _PxmTC4PwPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 4),
    _PxmTC4PwPmTCNum_Type()
)
pxmTC4PwPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmTCNum.setStatus("current")
_PxmTC4PwPmQueueingDiscardOctets_Type = Counter64
_PxmTC4PwPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC4PwPmQueueingDiscardOctets = _PxmTC4PwPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 5),
    _PxmTC4PwPmQueueingDiscardOctets_Type()
)
pxmTC4PwPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmQueueingDiscardOctets.setStatus("current")
_PxmTC4PwPmQueueingDiscardPkts_Type = Integer32
_PxmTC4PwPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC4PwPmQueueingDiscardPkts = _PxmTC4PwPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 6),
    _PxmTC4PwPmQueueingDiscardPkts_Type()
)
pxmTC4PwPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmQueueingDiscardPkts.setStatus("current")
_PxmTC4PwPmRandomGreenDropPkts_Type = Counter64
_PxmTC4PwPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC4PwPmRandomGreenDropPkts = _PxmTC4PwPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 7),
    _PxmTC4PwPmRandomGreenDropPkts_Type()
)
pxmTC4PwPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRandomGreenDropPkts.setStatus("current")
_PxmTC4PwPmRandomGreenDropOctets_Type = Counter64
_PxmTC4PwPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC4PwPmRandomGreenDropOctets = _PxmTC4PwPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 8),
    _PxmTC4PwPmRandomGreenDropOctets_Type()
)
pxmTC4PwPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRandomGreenDropOctets.setStatus("current")
_PxmTC4PwPmRandomYellowDropPkts_Type = Counter64
_PxmTC4PwPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC4PwPmRandomYellowDropPkts = _PxmTC4PwPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 9),
    _PxmTC4PwPmRandomYellowDropPkts_Type()
)
pxmTC4PwPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRandomYellowDropPkts.setStatus("current")
_PxmTC4PwPmRandomYellowDropOctets_Type = Counter64
_PxmTC4PwPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC4PwPmRandomYellowDropOctets = _PxmTC4PwPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 10),
    _PxmTC4PwPmRandomYellowDropOctets_Type()
)
pxmTC4PwPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmRandomYellowDropOctets.setStatus("current")
_PxmTC4PwPmQueueingTransmitPkts_Type = Counter64
_PxmTC4PwPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC4PwPmQueueingTransmitPkts = _PxmTC4PwPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 11),
    _PxmTC4PwPmQueueingTransmitPkts_Type()
)
pxmTC4PwPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmQueueingTransmitPkts.setStatus("current")
_PxmTC4PwPmQueueingTransmitOctets_Type = Counter64
_PxmTC4PwPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC4PwPmQueueingTransmitOctets = _PxmTC4PwPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 3, 1, 12),
    _PxmTC4PwPmQueueingTransmitOctets_Type()
)
pxmTC4PwPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4PwPmQueueingTransmitOctets.setStatus("current")
_PxmTC6PwPmTable_Object = MibTable
pxmTC6PwPmTable = _PxmTC6PwPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pxmTC6PwPmTable.setStatus("current")
_PxmTC6PwPmEntry_Object = MibTableRow
pxmTC6PwPmEntry = _PxmTC6PwPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1)
)
pxmTC6PwPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmSampleDuration"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC6PwPmEntry.setStatus("current")


class _PxmTC6PwPmTimestamp_Type(Integer32):
    """Custom type pxmTC6PwPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC6PwPmTimestamp_Type.__name__ = "Integer32"
_PxmTC6PwPmTimestamp_Object = MibTableColumn
pxmTC6PwPmTimestamp = _PxmTC6PwPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 1),
    _PxmTC6PwPmTimestamp_Type()
)
pxmTC6PwPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC6PwPmTimestamp.setStatus("current")


class _PxmTC6PwPmSampleDuration_Type(Integer32):
    """Custom type pxmTC6PwPmSampleDuration based on Integer32"""
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


_PxmTC6PwPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC6PwPmSampleDuration_Object = MibTableColumn
pxmTC6PwPmSampleDuration = _PxmTC6PwPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 2),
    _PxmTC6PwPmSampleDuration_Type()
)
pxmTC6PwPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC6PwPmSampleDuration.setStatus("current")
_PxmTC6PwPmValidity_Type = TruthValue
_PxmTC6PwPmValidity_Object = MibTableColumn
pxmTC6PwPmValidity = _PxmTC6PwPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 3),
    _PxmTC6PwPmValidity_Type()
)
pxmTC6PwPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmValidity.setStatus("current")
_PxmTC6PwPmTCNum_Type = Integer32
_PxmTC6PwPmTCNum_Object = MibTableColumn
pxmTC6PwPmTCNum = _PxmTC6PwPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 4),
    _PxmTC6PwPmTCNum_Type()
)
pxmTC6PwPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmTCNum.setStatus("current")
_PxmTC6PwPmQueueingDiscardOctets_Type = Counter64
_PxmTC6PwPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC6PwPmQueueingDiscardOctets = _PxmTC6PwPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 5),
    _PxmTC6PwPmQueueingDiscardOctets_Type()
)
pxmTC6PwPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmQueueingDiscardOctets.setStatus("current")
_PxmTC6PwPmQueueingDiscardPkts_Type = Integer32
_PxmTC6PwPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC6PwPmQueueingDiscardPkts = _PxmTC6PwPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 6),
    _PxmTC6PwPmQueueingDiscardPkts_Type()
)
pxmTC6PwPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmQueueingDiscardPkts.setStatus("current")
_PxmTC6PwPmRandomGreenDropPkts_Type = Counter64
_PxmTC6PwPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC6PwPmRandomGreenDropPkts = _PxmTC6PwPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 7),
    _PxmTC6PwPmRandomGreenDropPkts_Type()
)
pxmTC6PwPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRandomGreenDropPkts.setStatus("current")
_PxmTC6PwPmRandomGreenDropOctets_Type = Counter64
_PxmTC6PwPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC6PwPmRandomGreenDropOctets = _PxmTC6PwPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 8),
    _PxmTC6PwPmRandomGreenDropOctets_Type()
)
pxmTC6PwPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRandomGreenDropOctets.setStatus("current")
_PxmTC6PwPmRandomYellowDropPkts_Type = Counter64
_PxmTC6PwPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC6PwPmRandomYellowDropPkts = _PxmTC6PwPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 9),
    _PxmTC6PwPmRandomYellowDropPkts_Type()
)
pxmTC6PwPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRandomYellowDropPkts.setStatus("current")
_PxmTC6PwPmRandomYellowDropOctets_Type = Counter64
_PxmTC6PwPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC6PwPmRandomYellowDropOctets = _PxmTC6PwPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 10),
    _PxmTC6PwPmRandomYellowDropOctets_Type()
)
pxmTC6PwPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmRandomYellowDropOctets.setStatus("current")
_PxmTC6PwPmQueueingTransmitPkts_Type = Counter64
_PxmTC6PwPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC6PwPmQueueingTransmitPkts = _PxmTC6PwPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 11),
    _PxmTC6PwPmQueueingTransmitPkts_Type()
)
pxmTC6PwPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmQueueingTransmitPkts.setStatus("current")
_PxmTC6PwPmQueueingTransmitOctets_Type = Counter64
_PxmTC6PwPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC6PwPmQueueingTransmitOctets = _PxmTC6PwPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 4, 1, 12),
    _PxmTC6PwPmQueueingTransmitOctets_Type()
)
pxmTC6PwPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6PwPmQueueingTransmitOctets.setStatus("current")
_PxmTC7PwPmTable_Object = MibTable
pxmTC7PwPmTable = _PxmTC7PwPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5)
)
if mibBuilder.loadTexts:
    pxmTC7PwPmTable.setStatus("current")
_PxmTC7PwPmEntry_Object = MibTableRow
pxmTC7PwPmEntry = _PxmTC7PwPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1)
)
pxmTC7PwPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmSampleDuration"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC7PwPmEntry.setStatus("current")


class _PxmTC7PwPmTimestamp_Type(Integer32):
    """Custom type pxmTC7PwPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC7PwPmTimestamp_Type.__name__ = "Integer32"
_PxmTC7PwPmTimestamp_Object = MibTableColumn
pxmTC7PwPmTimestamp = _PxmTC7PwPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 1),
    _PxmTC7PwPmTimestamp_Type()
)
pxmTC7PwPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC7PwPmTimestamp.setStatus("current")


class _PxmTC7PwPmSampleDuration_Type(Integer32):
    """Custom type pxmTC7PwPmSampleDuration based on Integer32"""
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


_PxmTC7PwPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC7PwPmSampleDuration_Object = MibTableColumn
pxmTC7PwPmSampleDuration = _PxmTC7PwPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 2),
    _PxmTC7PwPmSampleDuration_Type()
)
pxmTC7PwPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC7PwPmSampleDuration.setStatus("current")
_PxmTC7PwPmValidity_Type = TruthValue
_PxmTC7PwPmValidity_Object = MibTableColumn
pxmTC7PwPmValidity = _PxmTC7PwPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 3),
    _PxmTC7PwPmValidity_Type()
)
pxmTC7PwPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmValidity.setStatus("current")
_PxmTC7PwPmTCNum_Type = Integer32
_PxmTC7PwPmTCNum_Object = MibTableColumn
pxmTC7PwPmTCNum = _PxmTC7PwPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 4),
    _PxmTC7PwPmTCNum_Type()
)
pxmTC7PwPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmTCNum.setStatus("current")
_PxmTC7PwPmQueueingDiscardOctets_Type = Counter64
_PxmTC7PwPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC7PwPmQueueingDiscardOctets = _PxmTC7PwPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 5),
    _PxmTC7PwPmQueueingDiscardOctets_Type()
)
pxmTC7PwPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmQueueingDiscardOctets.setStatus("current")
_PxmTC7PwPmQueueingDiscardPkts_Type = Integer32
_PxmTC7PwPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC7PwPmQueueingDiscardPkts = _PxmTC7PwPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 6),
    _PxmTC7PwPmQueueingDiscardPkts_Type()
)
pxmTC7PwPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmQueueingDiscardPkts.setStatus("current")
_PxmTC7PwPmRandomGreenDropPkts_Type = Counter64
_PxmTC7PwPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC7PwPmRandomGreenDropPkts = _PxmTC7PwPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 7),
    _PxmTC7PwPmRandomGreenDropPkts_Type()
)
pxmTC7PwPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRandomGreenDropPkts.setStatus("current")
_PxmTC7PwPmRandomGreenDropOctets_Type = Counter64
_PxmTC7PwPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC7PwPmRandomGreenDropOctets = _PxmTC7PwPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 8),
    _PxmTC7PwPmRandomGreenDropOctets_Type()
)
pxmTC7PwPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRandomGreenDropOctets.setStatus("current")
_PxmTC7PwPmRandomYellowDropPkts_Type = Counter64
_PxmTC7PwPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC7PwPmRandomYellowDropPkts = _PxmTC7PwPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 9),
    _PxmTC7PwPmRandomYellowDropPkts_Type()
)
pxmTC7PwPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRandomYellowDropPkts.setStatus("current")
_PxmTC7PwPmRandomYellowDropOctets_Type = Counter64
_PxmTC7PwPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC7PwPmRandomYellowDropOctets = _PxmTC7PwPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 10),
    _PxmTC7PwPmRandomYellowDropOctets_Type()
)
pxmTC7PwPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmRandomYellowDropOctets.setStatus("current")
_PxmTC7PwPmQueueingTransmitPkts_Type = Counter64
_PxmTC7PwPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC7PwPmQueueingTransmitPkts = _PxmTC7PwPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 11),
    _PxmTC7PwPmQueueingTransmitPkts_Type()
)
pxmTC7PwPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmQueueingTransmitPkts.setStatus("current")
_PxmTC7PwPmQueueingTransmitOctets_Type = Counter64
_PxmTC7PwPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC7PwPmQueueingTransmitOctets = _PxmTC7PwPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 5, 1, 12),
    _PxmTC7PwPmQueueingTransmitOctets_Type()
)
pxmTC7PwPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7PwPmQueueingTransmitOctets.setStatus("current")
_PxmTCANYPwPmTable_Object = MibTable
pxmTCANYPwPmTable = _PxmTCANYPwPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6)
)
if mibBuilder.loadTexts:
    pxmTCANYPwPmTable.setStatus("current")
_PxmTCANYPwPmEntry_Object = MibTableRow
pxmTCANYPwPmEntry = _PxmTCANYPwPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1)
)
pxmTCANYPwPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmSampleDuration"),
    (0, "INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTCANYPwPmEntry.setStatus("current")


class _PxmTCANYPwPmTimestamp_Type(Integer32):
    """Custom type pxmTCANYPwPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTCANYPwPmTimestamp_Type.__name__ = "Integer32"
_PxmTCANYPwPmTimestamp_Object = MibTableColumn
pxmTCANYPwPmTimestamp = _PxmTCANYPwPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 1),
    _PxmTCANYPwPmTimestamp_Type()
)
pxmTCANYPwPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTCANYPwPmTimestamp.setStatus("current")


class _PxmTCANYPwPmSampleDuration_Type(Integer32):
    """Custom type pxmTCANYPwPmSampleDuration based on Integer32"""
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


_PxmTCANYPwPmSampleDuration_Type.__name__ = "Integer32"
_PxmTCANYPwPmSampleDuration_Object = MibTableColumn
pxmTCANYPwPmSampleDuration = _PxmTCANYPwPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 2),
    _PxmTCANYPwPmSampleDuration_Type()
)
pxmTCANYPwPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTCANYPwPmSampleDuration.setStatus("current")
_PxmTCANYPwPmValidity_Type = TruthValue
_PxmTCANYPwPmValidity_Object = MibTableColumn
pxmTCANYPwPmValidity = _PxmTCANYPwPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 3),
    _PxmTCANYPwPmValidity_Type()
)
pxmTCANYPwPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmValidity.setStatus("current")
_PxmTCANYPwPmTCNum_Type = Integer32
_PxmTCANYPwPmTCNum_Object = MibTableColumn
pxmTCANYPwPmTCNum = _PxmTCANYPwPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 4),
    _PxmTCANYPwPmTCNum_Type()
)
pxmTCANYPwPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmTCNum.setStatus("current")
_PxmTCANYPwPmQueueingDiscardOctets_Type = Counter64
_PxmTCANYPwPmQueueingDiscardOctets_Object = MibTableColumn
pxmTCANYPwPmQueueingDiscardOctets = _PxmTCANYPwPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 5),
    _PxmTCANYPwPmQueueingDiscardOctets_Type()
)
pxmTCANYPwPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmQueueingDiscardOctets.setStatus("current")
_PxmTCANYPwPmQueueingDiscardPkts_Type = Integer32
_PxmTCANYPwPmQueueingDiscardPkts_Object = MibTableColumn
pxmTCANYPwPmQueueingDiscardPkts = _PxmTCANYPwPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 6),
    _PxmTCANYPwPmQueueingDiscardPkts_Type()
)
pxmTCANYPwPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmQueueingDiscardPkts.setStatus("current")
_PxmTCANYPwPmRandomGreenDropPkts_Type = Counter64
_PxmTCANYPwPmRandomGreenDropPkts_Object = MibTableColumn
pxmTCANYPwPmRandomGreenDropPkts = _PxmTCANYPwPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 7),
    _PxmTCANYPwPmRandomGreenDropPkts_Type()
)
pxmTCANYPwPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRandomGreenDropPkts.setStatus("current")
_PxmTCANYPwPmRandomGreenDropOctets_Type = Counter64
_PxmTCANYPwPmRandomGreenDropOctets_Object = MibTableColumn
pxmTCANYPwPmRandomGreenDropOctets = _PxmTCANYPwPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 8),
    _PxmTCANYPwPmRandomGreenDropOctets_Type()
)
pxmTCANYPwPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRandomGreenDropOctets.setStatus("current")
_PxmTCANYPwPmRandomYellowDropPkts_Type = Counter64
_PxmTCANYPwPmRandomYellowDropPkts_Object = MibTableColumn
pxmTCANYPwPmRandomYellowDropPkts = _PxmTCANYPwPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 9),
    _PxmTCANYPwPmRandomYellowDropPkts_Type()
)
pxmTCANYPwPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRandomYellowDropPkts.setStatus("current")
_PxmTCANYPwPmRandomYellowDropOctets_Type = Counter64
_PxmTCANYPwPmRandomYellowDropOctets_Object = MibTableColumn
pxmTCANYPwPmRandomYellowDropOctets = _PxmTCANYPwPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 10),
    _PxmTCANYPwPmRandomYellowDropOctets_Type()
)
pxmTCANYPwPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmRandomYellowDropOctets.setStatus("current")
_PxmTCANYPwPmQueueingTransmitPkts_Type = Counter64
_PxmTCANYPwPmQueueingTransmitPkts_Object = MibTableColumn
pxmTCANYPwPmQueueingTransmitPkts = _PxmTCANYPwPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 11),
    _PxmTCANYPwPmQueueingTransmitPkts_Type()
)
pxmTCANYPwPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmQueueingTransmitPkts.setStatus("current")
_PxmTCANYPwPmQueueingTransmitOctets_Type = Counter64
_PxmTCANYPwPmQueueingTransmitOctets_Object = MibTableColumn
pxmTCANYPwPmQueueingTransmitOctets = _PxmTCANYPwPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 2, 2, 6, 1, 12),
    _PxmTCANYPwPmQueueingTransmitOctets_Type()
)
pxmTCANYPwPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYPwPmQueueingTransmitOctets.setStatus("current")
_PxmPwPmConformance_ObjectIdentity = ObjectIdentity
pxmPwPmConformance = _PxmPwPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3)
)
_PxmPwPmCompliances_ObjectIdentity = ObjectIdentity
pxmPwPmCompliances = _PxmPwPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 1)
)
_PxmPwPmGroups_ObjectIdentity = ObjectIdentity
pxmPwPmGroups = _PxmPwPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2)
)

# Managed Objects groups

pxmPwPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 1)
)
pxmPwPmGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmPwPmValidity"),
        ("INFINERA-PM-PXMPW-MIB", "pxmPwPmRxPackets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmPwPmRxOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmPwPmTxPackets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmPwPmTxOctets"))
)
if mibBuilder.loadTexts:
    pxmPwPmGroup.setStatus("current")

pxmPwPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 2)
)
pxmPwPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmPwPmRealRxPackets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmPwPmRealRxOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmPwPmRealTxPackets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmPwPmRealTxOctets"))
)
if mibBuilder.loadTexts:
    pxmPwPmRealGroup.setStatus("current")

pxmTC0PwPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 3)
)
pxmTC0PwPmGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmValidity"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC0PwPmGroup.setStatus("current")

pxmTC0PwPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 4)
)
pxmTC0PwPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC0PwPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC0PwPmRealGroup.setStatus("current")

pxmTC2PwPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 5)
)
pxmTC2PwPmGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmValidity"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC2PwPmGroup.setStatus("current")

pxmTC2PwPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 6)
)
pxmTC2PwPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC2PwPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC2PwPmRealGroup.setStatus("current")

pxmTC4PwPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 7)
)
pxmTC4PwPmGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmValidity"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC4PwPmGroup.setStatus("current")

pxmTC4PwPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 8)
)
pxmTC4PwPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC4PwPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC4PwPmRealGroup.setStatus("current")

pxmTC6PwPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 9)
)
pxmTC6PwPmGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmValidity"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC6PwPmGroup.setStatus("current")

pxmTC6PwPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 10)
)
pxmTC6PwPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC6PwPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC6PwPmRealGroup.setStatus("current")

pxmTC7PwPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 11)
)
pxmTC7PwPmGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmValidity"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC7PwPmGroup.setStatus("current")

pxmTC7PwPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 12)
)
pxmTC7PwPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTC7PwPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC7PwPmRealGroup.setStatus("current")

pxmTCANYPwPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 13)
)
pxmTCANYPwPmGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmValidity"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTCANYPwPmGroup.setStatus("current")

pxmTCANYPwPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 2, 14)
)
pxmTCANYPwPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealTCNum"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMPW-MIB", "pxmTCANYPwPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTCANYPwPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmPwPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 1, 1)
)
pxmPwPmCompliance.setObjects(
    ("INFINERA-PM-PXMPW-MIB", "pxmPwPmGroup")
)
if mibBuilder.loadTexts:
    pxmPwPmCompliance.setStatus(
        "current"
    )

pxmPwPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 96, 3, 1, 2)
)
pxmPwPmRealCompliance.setObjects(
    ("INFINERA-PM-PXMPW-MIB", "pxmPwPmRealGroup")
)
if mibBuilder.loadTexts:
    pxmPwPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-PXMPW-MIB",
    **{"pxmPwPmMIB": pxmPwPmMIB,
       "pxmPwRmonPm": pxmPwRmonPm,
       "pxmPwPmRealTable": pxmPwPmRealTable,
       "pxmPwPmRealEntry": pxmPwPmRealEntry,
       "pxmPwPmRealRxPackets": pxmPwPmRealRxPackets,
       "pxmPwPmRealRxOctets": pxmPwPmRealRxOctets,
       "pxmPwPmRealTxPackets": pxmPwPmRealTxPackets,
       "pxmPwPmRealTxOctets": pxmPwPmRealTxOctets,
       "pxmPwPmTable": pxmPwPmTable,
       "pxmPwPmEntry": pxmPwPmEntry,
       "pxmPwPmTimestamp": pxmPwPmTimestamp,
       "pxmPwPmSampleDuration": pxmPwPmSampleDuration,
       "pxmPwPmValidity": pxmPwPmValidity,
       "pxmPwPmRxPackets": pxmPwPmRxPackets,
       "pxmPwPmRxOctets": pxmPwPmRxOctets,
       "pxmPwPmTxPackets": pxmPwPmTxPackets,
       "pxmPwPmTxOctets": pxmPwPmTxOctets,
       "pxmCmPwPmObjects": pxmCmPwPmObjects,
       "pxmCmPwRealPm": pxmCmPwRealPm,
       "pxmTC0PwPmRealTable": pxmTC0PwPmRealTable,
       "pxmTC0PwPmRealEntry": pxmTC0PwPmRealEntry,
       "pxmTC0PwPmRealTCNum": pxmTC0PwPmRealTCNum,
       "pxmTC0PwPmRealTDQueuingCurrentQDepth": pxmTC0PwPmRealTDQueuingCurrentQDepth,
       "pxmTC0PwPmRealQueueingDiscardOctets": pxmTC0PwPmRealQueueingDiscardOctets,
       "pxmTC0PwPmRealQueueingDiscardPkts": pxmTC0PwPmRealQueueingDiscardPkts,
       "pxmTC0PwPmRealRandomGreenDropPkts": pxmTC0PwPmRealRandomGreenDropPkts,
       "pxmTC0PwPmRealRandomGreenDropOctets": pxmTC0PwPmRealRandomGreenDropOctets,
       "pxmTC0PwPmRealRandomYellowDropPkts": pxmTC0PwPmRealRandomYellowDropPkts,
       "pxmTC0PwPmRealRandomYellowDropOctets": pxmTC0PwPmRealRandomYellowDropOctets,
       "pxmTC0PwPmRealQueueingTransmitPkts": pxmTC0PwPmRealQueueingTransmitPkts,
       "pxmTC0PwPmRealQueueingTransmitOctets": pxmTC0PwPmRealQueueingTransmitOctets,
       "pxmTC0PwPmRealQueueingMeanQSizeUnit": pxmTC0PwPmRealQueueingMeanQSizeUnit,
       "pxmTC0PwPmRealMeanQSize": pxmTC0PwPmRealMeanQSize,
       "pxmTC2PwPmRealTable": pxmTC2PwPmRealTable,
       "pxmTC2PwPmRealEntry": pxmTC2PwPmRealEntry,
       "pxmTC2PwPmRealTCNum": pxmTC2PwPmRealTCNum,
       "pxmTC2PwPmRealTDQueuingCurrentQDepth": pxmTC2PwPmRealTDQueuingCurrentQDepth,
       "pxmTC2PwPmRealQueueingDiscardOctets": pxmTC2PwPmRealQueueingDiscardOctets,
       "pxmTC2PwPmRealQueueingDiscardPkts": pxmTC2PwPmRealQueueingDiscardPkts,
       "pxmTC2PwPmRealRandomGreenDropPkts": pxmTC2PwPmRealRandomGreenDropPkts,
       "pxmTC2PwPmRealRandomGreenDropOctets": pxmTC2PwPmRealRandomGreenDropOctets,
       "pxmTC2PwPmRealRandomYellowDropPkts": pxmTC2PwPmRealRandomYellowDropPkts,
       "pxmTC2PwPmRealRandomYellowDropOctets": pxmTC2PwPmRealRandomYellowDropOctets,
       "pxmTC2PwPmRealQueueingTransmitPkts": pxmTC2PwPmRealQueueingTransmitPkts,
       "pxmTC2PwPmRealQueueingTransmitOctets": pxmTC2PwPmRealQueueingTransmitOctets,
       "pxmTC2PwPmRealQueueingMeanQSizeUnit": pxmTC2PwPmRealQueueingMeanQSizeUnit,
       "pxmTC2PwPmRealMeanQSize": pxmTC2PwPmRealMeanQSize,
       "pxmTC4PwPmRealTable": pxmTC4PwPmRealTable,
       "pxmTC4PwPmRealEntry": pxmTC4PwPmRealEntry,
       "pxmTC4PwPmRealTCNum": pxmTC4PwPmRealTCNum,
       "pxmTC4PwPmRealTDQueuingCurrentQDepth": pxmTC4PwPmRealTDQueuingCurrentQDepth,
       "pxmTC4PwPmRealQueueingDiscardOctets": pxmTC4PwPmRealQueueingDiscardOctets,
       "pxmTC4PwPmRealQueueingDiscardPkts": pxmTC4PwPmRealQueueingDiscardPkts,
       "pxmTC4PwPmRealRandomGreenDropPkts": pxmTC4PwPmRealRandomGreenDropPkts,
       "pxmTC4PwPmRealRandomGreenDropOctets": pxmTC4PwPmRealRandomGreenDropOctets,
       "pxmTC4PwPmRealRandomYellowDropPkts": pxmTC4PwPmRealRandomYellowDropPkts,
       "pxmTC4PwPmRealRandomYellowDropOctets": pxmTC4PwPmRealRandomYellowDropOctets,
       "pxmTC4PwPmRealQueueingTransmitPkts": pxmTC4PwPmRealQueueingTransmitPkts,
       "pxmTC4PwPmRealQueueingTransmitOctets": pxmTC4PwPmRealQueueingTransmitOctets,
       "pxmTC4PwPmRealQueueingMeanQSizeUnit": pxmTC4PwPmRealQueueingMeanQSizeUnit,
       "pxmTC4PwPmRealMeanQSize": pxmTC4PwPmRealMeanQSize,
       "pxmTC6PwPmRealTable": pxmTC6PwPmRealTable,
       "pxmTC6PwPmRealEntry": pxmTC6PwPmRealEntry,
       "pxmTC6PwPmRealTCNum": pxmTC6PwPmRealTCNum,
       "pxmTC6PwPmRealTDQueuingCurrentQDepth": pxmTC6PwPmRealTDQueuingCurrentQDepth,
       "pxmTC6PwPmRealQueueingDiscardOctets": pxmTC6PwPmRealQueueingDiscardOctets,
       "pxmTC6PwPmRealQueueingDiscardPkts": pxmTC6PwPmRealQueueingDiscardPkts,
       "pxmTC6PwPmRealRandomGreenDropPkts": pxmTC6PwPmRealRandomGreenDropPkts,
       "pxmTC6PwPmRealRandomGreenDropOctets": pxmTC6PwPmRealRandomGreenDropOctets,
       "pxmTC6PwPmRealRandomYellowDropPkts": pxmTC6PwPmRealRandomYellowDropPkts,
       "pxmTC6PwPmRealRandomYellowDropOctets": pxmTC6PwPmRealRandomYellowDropOctets,
       "pxmTC6PwPmRealQueueingTransmitPkts": pxmTC6PwPmRealQueueingTransmitPkts,
       "pxmTC6PwPmRealQueueingTransmitOctets": pxmTC6PwPmRealQueueingTransmitOctets,
       "pxmTC6PwPmRealQueueingMeanQSizeUnit": pxmTC6PwPmRealQueueingMeanQSizeUnit,
       "pxmTC6PwPmRealMeanQSize": pxmTC6PwPmRealMeanQSize,
       "pxmTC7PwPmRealTable": pxmTC7PwPmRealTable,
       "pxmTC7PwPmRealEntry": pxmTC7PwPmRealEntry,
       "pxmTC7PwPmRealTCNum": pxmTC7PwPmRealTCNum,
       "pxmTC7PwPmRealTDQueuingCurrentQDepth": pxmTC7PwPmRealTDQueuingCurrentQDepth,
       "pxmTC7PwPmRealQueueingDiscardOctets": pxmTC7PwPmRealQueueingDiscardOctets,
       "pxmTC7PwPmRealQueueingDiscardPkts": pxmTC7PwPmRealQueueingDiscardPkts,
       "pxmTC7PwPmRealRandomGreenDropPkts": pxmTC7PwPmRealRandomGreenDropPkts,
       "pxmTC7PwPmRealRandomGreenDropOctets": pxmTC7PwPmRealRandomGreenDropOctets,
       "pxmTC7PwPmRealRandomYellowDropPkts": pxmTC7PwPmRealRandomYellowDropPkts,
       "pxmTC7PwPmRealRandomYellowDropOctets": pxmTC7PwPmRealRandomYellowDropOctets,
       "pxmTC7PwPmRealQueueingTransmitPkts": pxmTC7PwPmRealQueueingTransmitPkts,
       "pxmTC7PwPmRealQueueingTransmitOctets": pxmTC7PwPmRealQueueingTransmitOctets,
       "pxmTC7PwPmRealQueueingMeanQSizeUnit": pxmTC7PwPmRealQueueingMeanQSizeUnit,
       "pxmTC7PwPmRealMeanQSize": pxmTC7PwPmRealMeanQSize,
       "pxmTCANYPwPmRealTable": pxmTCANYPwPmRealTable,
       "pxmTCANYPwPmRealEntry": pxmTCANYPwPmRealEntry,
       "pxmTCANYPwPmRealTCNum": pxmTCANYPwPmRealTCNum,
       "pxmTCANYPwPmRealTDQueuingCurrentQDepth": pxmTCANYPwPmRealTDQueuingCurrentQDepth,
       "pxmTCANYPwPmRealQueueingDiscardOctets": pxmTCANYPwPmRealQueueingDiscardOctets,
       "pxmTCANYPwPmRealQueueingDiscardPkts": pxmTCANYPwPmRealQueueingDiscardPkts,
       "pxmTCANYPwPmRealRandomGreenDropPkts": pxmTCANYPwPmRealRandomGreenDropPkts,
       "pxmTCANYPwPmRealRandomGreenDropOctets": pxmTCANYPwPmRealRandomGreenDropOctets,
       "pxmTCANYPwPmRealRandomYellowDropPkts": pxmTCANYPwPmRealRandomYellowDropPkts,
       "pxmTCANYPwPmRealRandomYellowDropOctets": pxmTCANYPwPmRealRandomYellowDropOctets,
       "pxmTCANYPwPmRealQueueingTransmitPkts": pxmTCANYPwPmRealQueueingTransmitPkts,
       "pxmTCANYPwPmRealQueueingTransmitOctets": pxmTCANYPwPmRealQueueingTransmitOctets,
       "pxmTCANYPwPmRealQueueingMeanQSizeUnit": pxmTCANYPwPmRealQueueingMeanQSizeUnit,
       "pxmTCANYPwPmRealMeanQSize": pxmTCANYPwPmRealMeanQSize,
       "pxmCmPwPm": pxmCmPwPm,
       "pxmTC0PwPmTable": pxmTC0PwPmTable,
       "pxmTC0PwPmEntry": pxmTC0PwPmEntry,
       "pxmTC0PwPmTimestamp": pxmTC0PwPmTimestamp,
       "pxmTC0PwPmSampleDuration": pxmTC0PwPmSampleDuration,
       "pxmTC0PwPmValidity": pxmTC0PwPmValidity,
       "pxmTC0PwPmTCNum": pxmTC0PwPmTCNum,
       "pxmTC0PwPmQueueingDiscardOctets": pxmTC0PwPmQueueingDiscardOctets,
       "pxmTC0PwPmQueueingDiscardPkts": pxmTC0PwPmQueueingDiscardPkts,
       "pxmTC0PwPmRandomGreenDropPkts": pxmTC0PwPmRandomGreenDropPkts,
       "pxmTC0PwPmRandomGreenDropOctets": pxmTC0PwPmRandomGreenDropOctets,
       "pxmTC0PwPmRandomYellowDropPkts": pxmTC0PwPmRandomYellowDropPkts,
       "pxmTC0PwPmRandomYellowDropOctets": pxmTC0PwPmRandomYellowDropOctets,
       "pxmTC0PwPmQueueingTransmitPkts": pxmTC0PwPmQueueingTransmitPkts,
       "pxmTC0PwPmQueueingTransmitOctets": pxmTC0PwPmQueueingTransmitOctets,
       "pxmTC2PwPmTable": pxmTC2PwPmTable,
       "pxmTC2PwPmEntry": pxmTC2PwPmEntry,
       "pxmTC2PwPmTimestamp": pxmTC2PwPmTimestamp,
       "pxmTC2PwPmSampleDuration": pxmTC2PwPmSampleDuration,
       "pxmTC2PwPmValidity": pxmTC2PwPmValidity,
       "pxmTC2PwPmTCNum": pxmTC2PwPmTCNum,
       "pxmTC2PwPmQueueingDiscardOctets": pxmTC2PwPmQueueingDiscardOctets,
       "pxmTC2PwPmQueueingDiscardPkts": pxmTC2PwPmQueueingDiscardPkts,
       "pxmTC2PwPmRandomGreenDropPkts": pxmTC2PwPmRandomGreenDropPkts,
       "pxmTC2PwPmRandomGreenDropOctets": pxmTC2PwPmRandomGreenDropOctets,
       "pxmTC2PwPmRandomYellowDropPkts": pxmTC2PwPmRandomYellowDropPkts,
       "pxmTC2PwPmRandomYellowDropOctets": pxmTC2PwPmRandomYellowDropOctets,
       "pxmTC2PwPmQueueingTransmitPkts": pxmTC2PwPmQueueingTransmitPkts,
       "pxmTC2PwPmQueueingTransmitOctets": pxmTC2PwPmQueueingTransmitOctets,
       "pxmTC4PwPmTable": pxmTC4PwPmTable,
       "pxmTC4PwPmEntry": pxmTC4PwPmEntry,
       "pxmTC4PwPmTimestamp": pxmTC4PwPmTimestamp,
       "pxmTC4PwPmSampleDuration": pxmTC4PwPmSampleDuration,
       "pxmTC4PwPmValidity": pxmTC4PwPmValidity,
       "pxmTC4PwPmTCNum": pxmTC4PwPmTCNum,
       "pxmTC4PwPmQueueingDiscardOctets": pxmTC4PwPmQueueingDiscardOctets,
       "pxmTC4PwPmQueueingDiscardPkts": pxmTC4PwPmQueueingDiscardPkts,
       "pxmTC4PwPmRandomGreenDropPkts": pxmTC4PwPmRandomGreenDropPkts,
       "pxmTC4PwPmRandomGreenDropOctets": pxmTC4PwPmRandomGreenDropOctets,
       "pxmTC4PwPmRandomYellowDropPkts": pxmTC4PwPmRandomYellowDropPkts,
       "pxmTC4PwPmRandomYellowDropOctets": pxmTC4PwPmRandomYellowDropOctets,
       "pxmTC4PwPmQueueingTransmitPkts": pxmTC4PwPmQueueingTransmitPkts,
       "pxmTC4PwPmQueueingTransmitOctets": pxmTC4PwPmQueueingTransmitOctets,
       "pxmTC6PwPmTable": pxmTC6PwPmTable,
       "pxmTC6PwPmEntry": pxmTC6PwPmEntry,
       "pxmTC6PwPmTimestamp": pxmTC6PwPmTimestamp,
       "pxmTC6PwPmSampleDuration": pxmTC6PwPmSampleDuration,
       "pxmTC6PwPmValidity": pxmTC6PwPmValidity,
       "pxmTC6PwPmTCNum": pxmTC6PwPmTCNum,
       "pxmTC6PwPmQueueingDiscardOctets": pxmTC6PwPmQueueingDiscardOctets,
       "pxmTC6PwPmQueueingDiscardPkts": pxmTC6PwPmQueueingDiscardPkts,
       "pxmTC6PwPmRandomGreenDropPkts": pxmTC6PwPmRandomGreenDropPkts,
       "pxmTC6PwPmRandomGreenDropOctets": pxmTC6PwPmRandomGreenDropOctets,
       "pxmTC6PwPmRandomYellowDropPkts": pxmTC6PwPmRandomYellowDropPkts,
       "pxmTC6PwPmRandomYellowDropOctets": pxmTC6PwPmRandomYellowDropOctets,
       "pxmTC6PwPmQueueingTransmitPkts": pxmTC6PwPmQueueingTransmitPkts,
       "pxmTC6PwPmQueueingTransmitOctets": pxmTC6PwPmQueueingTransmitOctets,
       "pxmTC7PwPmTable": pxmTC7PwPmTable,
       "pxmTC7PwPmEntry": pxmTC7PwPmEntry,
       "pxmTC7PwPmTimestamp": pxmTC7PwPmTimestamp,
       "pxmTC7PwPmSampleDuration": pxmTC7PwPmSampleDuration,
       "pxmTC7PwPmValidity": pxmTC7PwPmValidity,
       "pxmTC7PwPmTCNum": pxmTC7PwPmTCNum,
       "pxmTC7PwPmQueueingDiscardOctets": pxmTC7PwPmQueueingDiscardOctets,
       "pxmTC7PwPmQueueingDiscardPkts": pxmTC7PwPmQueueingDiscardPkts,
       "pxmTC7PwPmRandomGreenDropPkts": pxmTC7PwPmRandomGreenDropPkts,
       "pxmTC7PwPmRandomGreenDropOctets": pxmTC7PwPmRandomGreenDropOctets,
       "pxmTC7PwPmRandomYellowDropPkts": pxmTC7PwPmRandomYellowDropPkts,
       "pxmTC7PwPmRandomYellowDropOctets": pxmTC7PwPmRandomYellowDropOctets,
       "pxmTC7PwPmQueueingTransmitPkts": pxmTC7PwPmQueueingTransmitPkts,
       "pxmTC7PwPmQueueingTransmitOctets": pxmTC7PwPmQueueingTransmitOctets,
       "pxmTCANYPwPmTable": pxmTCANYPwPmTable,
       "pxmTCANYPwPmEntry": pxmTCANYPwPmEntry,
       "pxmTCANYPwPmTimestamp": pxmTCANYPwPmTimestamp,
       "pxmTCANYPwPmSampleDuration": pxmTCANYPwPmSampleDuration,
       "pxmTCANYPwPmValidity": pxmTCANYPwPmValidity,
       "pxmTCANYPwPmTCNum": pxmTCANYPwPmTCNum,
       "pxmTCANYPwPmQueueingDiscardOctets": pxmTCANYPwPmQueueingDiscardOctets,
       "pxmTCANYPwPmQueueingDiscardPkts": pxmTCANYPwPmQueueingDiscardPkts,
       "pxmTCANYPwPmRandomGreenDropPkts": pxmTCANYPwPmRandomGreenDropPkts,
       "pxmTCANYPwPmRandomGreenDropOctets": pxmTCANYPwPmRandomGreenDropOctets,
       "pxmTCANYPwPmRandomYellowDropPkts": pxmTCANYPwPmRandomYellowDropPkts,
       "pxmTCANYPwPmRandomYellowDropOctets": pxmTCANYPwPmRandomYellowDropOctets,
       "pxmTCANYPwPmQueueingTransmitPkts": pxmTCANYPwPmQueueingTransmitPkts,
       "pxmTCANYPwPmQueueingTransmitOctets": pxmTCANYPwPmQueueingTransmitOctets,
       "pxmPwPmConformance": pxmPwPmConformance,
       "pxmPwPmCompliances": pxmPwPmCompliances,
       "pxmPwPmCompliance": pxmPwPmCompliance,
       "pxmPwPmRealCompliance": pxmPwPmRealCompliance,
       "pxmPwPmGroups": pxmPwPmGroups,
       "pxmPwPmGroup": pxmPwPmGroup,
       "pxmPwPmRealGroup": pxmPwPmRealGroup,
       "pxmTC0PwPmGroup": pxmTC0PwPmGroup,
       "pxmTC0PwPmRealGroup": pxmTC0PwPmRealGroup,
       "pxmTC2PwPmGroup": pxmTC2PwPmGroup,
       "pxmTC2PwPmRealGroup": pxmTC2PwPmRealGroup,
       "pxmTC4PwPmGroup": pxmTC4PwPmGroup,
       "pxmTC4PwPmRealGroup": pxmTC4PwPmRealGroup,
       "pxmTC6PwPmGroup": pxmTC6PwPmGroup,
       "pxmTC6PwPmRealGroup": pxmTC6PwPmRealGroup,
       "pxmTC7PwPmGroup": pxmTC7PwPmGroup,
       "pxmTC7PwPmRealGroup": pxmTC7PwPmRealGroup,
       "pxmTCANYPwPmGroup": pxmTCANYPwPmGroup,
       "pxmTCANYPwPmRealGroup": pxmTCANYPwPmRealGroup}
)
