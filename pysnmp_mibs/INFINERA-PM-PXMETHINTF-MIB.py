# SNMP MIB module (INFINERA-PM-PXMETHINTF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-PXMETHINTF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:44 2025
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

pxmEthIntfPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97)
)
if mibBuilder.loadTexts:
    pxmEthIntfPmMIB.setRevisions(
        ("2014-02-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmEthIntfRmonPm_ObjectIdentity = ObjectIdentity
pxmEthIntfRmonPm = _PxmEthIntfRmonPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1)
)
_PxmEthIntfPmRealTable_Object = MibTable
pxmEthIntfPmRealTable = _PxmEthIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1)
)
if mibBuilder.loadTexts:
    pxmEthIntfPmRealTable.setStatus("current")
_PxmEthIntfPmRealEntry_Object = MibTableRow
pxmEthIntfPmRealEntry = _PxmEthIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1)
)
pxmEthIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmEthIntfPmRealEntry.setStatus("current")
_PxmEthIntfPmRealRxPackets_Type = Counter64
_PxmEthIntfPmRealRxPackets_Object = MibTableColumn
pxmEthIntfPmRealRxPackets = _PxmEthIntfPmRealRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 1),
    _PxmEthIntfPmRealRxPackets_Type()
)
pxmEthIntfPmRealRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxPackets.setStatus("current")
_PxmEthIntfPmRealRxOctets_Type = Counter64
_PxmEthIntfPmRealRxOctets_Object = MibTableColumn
pxmEthIntfPmRealRxOctets = _PxmEthIntfPmRealRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 2),
    _PxmEthIntfPmRealRxOctets_Type()
)
pxmEthIntfPmRealRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxOctets.setStatus("current")
_PxmEthIntfPmRealRxCrcAlignedErr_Type = Integer32
_PxmEthIntfPmRealRxCrcAlignedErr_Object = MibTableColumn
pxmEthIntfPmRealRxCrcAlignedErr = _PxmEthIntfPmRealRxCrcAlignedErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 3),
    _PxmEthIntfPmRealRxCrcAlignedErr_Type()
)
pxmEthIntfPmRealRxCrcAlignedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxCrcAlignedErr.setStatus("current")
_PxmEthIntfPmRealRxUndersized_Type = Counter64
_PxmEthIntfPmRealRxUndersized_Object = MibTableColumn
pxmEthIntfPmRealRxUndersized = _PxmEthIntfPmRealRxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 4),
    _PxmEthIntfPmRealRxUndersized_Type()
)
pxmEthIntfPmRealRxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxUndersized.setStatus("current")
_PxmEthIntfPmRealRxOversized_Type = Counter64
_PxmEthIntfPmRealRxOversized_Object = MibTableColumn
pxmEthIntfPmRealRxOversized = _PxmEthIntfPmRealRxOversized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 5),
    _PxmEthIntfPmRealRxOversized_Type()
)
pxmEthIntfPmRealRxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxOversized.setStatus("current")
_PxmEthIntfPmRealRxUnicastPkts_Type = Counter64
_PxmEthIntfPmRealRxUnicastPkts_Object = MibTableColumn
pxmEthIntfPmRealRxUnicastPkts = _PxmEthIntfPmRealRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 6),
    _PxmEthIntfPmRealRxUnicastPkts_Type()
)
pxmEthIntfPmRealRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxUnicastPkts.setStatus("current")
_PxmEthIntfPmRealRxBroadcastPkts_Type = Counter64
_PxmEthIntfPmRealRxBroadcastPkts_Object = MibTableColumn
pxmEthIntfPmRealRxBroadcastPkts = _PxmEthIntfPmRealRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 7),
    _PxmEthIntfPmRealRxBroadcastPkts_Type()
)
pxmEthIntfPmRealRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxBroadcastPkts.setStatus("current")
_PxmEthIntfPmRealRxMulticastPkts_Type = Counter64
_PxmEthIntfPmRealRxMulticastPkts_Object = MibTableColumn
pxmEthIntfPmRealRxMulticastPkts = _PxmEthIntfPmRealRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 8),
    _PxmEthIntfPmRealRxMulticastPkts_Type()
)
pxmEthIntfPmRealRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxMulticastPkts.setStatus("current")
_PxmEthIntfPmRealRxPktErrors_Type = Counter64
_PxmEthIntfPmRealRxPktErrors_Object = MibTableColumn
pxmEthIntfPmRealRxPktErrors = _PxmEthIntfPmRealRxPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 9),
    _PxmEthIntfPmRealRxPktErrors_Type()
)
pxmEthIntfPmRealRxPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxPktErrors.setStatus("current")
_PxmEthIntfPmRealRxSize64_Type = Counter64
_PxmEthIntfPmRealRxSize64_Object = MibTableColumn
pxmEthIntfPmRealRxSize64 = _PxmEthIntfPmRealRxSize64_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 10),
    _PxmEthIntfPmRealRxSize64_Type()
)
pxmEthIntfPmRealRxSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxSize64.setStatus("current")
_PxmEthIntfPmRealRxSize65to127_Type = Counter64
_PxmEthIntfPmRealRxSize65to127_Object = MibTableColumn
pxmEthIntfPmRealRxSize65to127 = _PxmEthIntfPmRealRxSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 11),
    _PxmEthIntfPmRealRxSize65to127_Type()
)
pxmEthIntfPmRealRxSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxSize65to127.setStatus("current")
_PxmEthIntfPmRealRxSize128to255_Type = Counter64
_PxmEthIntfPmRealRxSize128to255_Object = MibTableColumn
pxmEthIntfPmRealRxSize128to255 = _PxmEthIntfPmRealRxSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 12),
    _PxmEthIntfPmRealRxSize128to255_Type()
)
pxmEthIntfPmRealRxSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxSize128to255.setStatus("current")
_PxmEthIntfPmRealRxSize256to511_Type = Counter64
_PxmEthIntfPmRealRxSize256to511_Object = MibTableColumn
pxmEthIntfPmRealRxSize256to511 = _PxmEthIntfPmRealRxSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 13),
    _PxmEthIntfPmRealRxSize256to511_Type()
)
pxmEthIntfPmRealRxSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxSize256to511.setStatus("current")
_PxmEthIntfPmRealRxSize512to1023_Type = Counter64
_PxmEthIntfPmRealRxSize512to1023_Object = MibTableColumn
pxmEthIntfPmRealRxSize512to1023 = _PxmEthIntfPmRealRxSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 14),
    _PxmEthIntfPmRealRxSize512to1023_Type()
)
pxmEthIntfPmRealRxSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxSize512to1023.setStatus("current")
_PxmEthIntfPmRealRxSize1024to1518_Type = Counter64
_PxmEthIntfPmRealRxSize1024to1518_Object = MibTableColumn
pxmEthIntfPmRealRxSize1024to1518 = _PxmEthIntfPmRealRxSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 15),
    _PxmEthIntfPmRealRxSize1024to1518_Type()
)
pxmEthIntfPmRealRxSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxSize1024to1518.setStatus("current")
_PxmEthIntfPmRealRxLU_Type = FloatHundredths
_PxmEthIntfPmRealRxLU_Object = MibTableColumn
pxmEthIntfPmRealRxLU = _PxmEthIntfPmRealRxLU_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 16),
    _PxmEthIntfPmRealRxLU_Type()
)
pxmEthIntfPmRealRxLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealRxLU.setStatus("current")
_PxmEthIntfPmRealTxPackets_Type = Counter64
_PxmEthIntfPmRealTxPackets_Object = MibTableColumn
pxmEthIntfPmRealTxPackets = _PxmEthIntfPmRealTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 17),
    _PxmEthIntfPmRealTxPackets_Type()
)
pxmEthIntfPmRealTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealTxPackets.setStatus("current")
_PxmEthIntfPmRealTxOctets_Type = Counter64
_PxmEthIntfPmRealTxOctets_Object = MibTableColumn
pxmEthIntfPmRealTxOctets = _PxmEthIntfPmRealTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 18),
    _PxmEthIntfPmRealTxOctets_Type()
)
pxmEthIntfPmRealTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealTxOctets.setStatus("current")
_PxmEthIntfPmRealTxUnicastPkts_Type = Counter64
_PxmEthIntfPmRealTxUnicastPkts_Object = MibTableColumn
pxmEthIntfPmRealTxUnicastPkts = _PxmEthIntfPmRealTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 19),
    _PxmEthIntfPmRealTxUnicastPkts_Type()
)
pxmEthIntfPmRealTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealTxUnicastPkts.setStatus("current")
_PxmEthIntfPmRealTxBroadcastPkts_Type = Counter64
_PxmEthIntfPmRealTxBroadcastPkts_Object = MibTableColumn
pxmEthIntfPmRealTxBroadcastPkts = _PxmEthIntfPmRealTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 20),
    _PxmEthIntfPmRealTxBroadcastPkts_Type()
)
pxmEthIntfPmRealTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealTxBroadcastPkts.setStatus("current")
_PxmEthIntfPmRealTxMulticastPkts_Type = Counter64
_PxmEthIntfPmRealTxMulticastPkts_Object = MibTableColumn
pxmEthIntfPmRealTxMulticastPkts = _PxmEthIntfPmRealTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 21),
    _PxmEthIntfPmRealTxMulticastPkts_Type()
)
pxmEthIntfPmRealTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealTxMulticastPkts.setStatus("current")
_PxmEthIntfPmRealTxPktErrors_Type = Counter64
_PxmEthIntfPmRealTxPktErrors_Object = MibTableColumn
pxmEthIntfPmRealTxPktErrors = _PxmEthIntfPmRealTxPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 22),
    _PxmEthIntfPmRealTxPktErrors_Type()
)
pxmEthIntfPmRealTxPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealTxPktErrors.setStatus("current")
_PxmEthIntfPmRealTxLU_Type = FloatHundredths
_PxmEthIntfPmRealTxLU_Object = MibTableColumn
pxmEthIntfPmRealTxLU = _PxmEthIntfPmRealTxLU_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 1, 1, 23),
    _PxmEthIntfPmRealTxLU_Type()
)
pxmEthIntfPmRealTxLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRealTxLU.setStatus("current")
_PxmEthIntfPmTable_Object = MibTable
pxmEthIntfPmTable = _PxmEthIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2)
)
if mibBuilder.loadTexts:
    pxmEthIntfPmTable.setStatus("current")
_PxmEthIntfPmEntry_Object = MibTableRow
pxmEthIntfPmEntry = _PxmEthIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1)
)
pxmEthIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmEthIntfPmEntry.setStatus("current")


class _PxmEthIntfPmTimestamp_Type(Integer32):
    """Custom type pxmEthIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmEthIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmEthIntfPmTimestamp_Object = MibTableColumn
pxmEthIntfPmTimestamp = _PxmEthIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 1),
    _PxmEthIntfPmTimestamp_Type()
)
pxmEthIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmEthIntfPmTimestamp.setStatus("current")


class _PxmEthIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmEthIntfPmSampleDuration based on Integer32"""
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


_PxmEthIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmEthIntfPmSampleDuration_Object = MibTableColumn
pxmEthIntfPmSampleDuration = _PxmEthIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 2),
    _PxmEthIntfPmSampleDuration_Type()
)
pxmEthIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmEthIntfPmSampleDuration.setStatus("current")
_PxmEthIntfPmValidity_Type = TruthValue
_PxmEthIntfPmValidity_Object = MibTableColumn
pxmEthIntfPmValidity = _PxmEthIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 3),
    _PxmEthIntfPmValidity_Type()
)
pxmEthIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmValidity.setStatus("current")
_PxmEthIntfPmRxPackets_Type = HCPerfIntervalCount
_PxmEthIntfPmRxPackets_Object = MibTableColumn
pxmEthIntfPmRxPackets = _PxmEthIntfPmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 4),
    _PxmEthIntfPmRxPackets_Type()
)
pxmEthIntfPmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxPackets.setStatus("current")
_PxmEthIntfPmRxOctets_Type = HCPerfIntervalCount
_PxmEthIntfPmRxOctets_Object = MibTableColumn
pxmEthIntfPmRxOctets = _PxmEthIntfPmRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 5),
    _PxmEthIntfPmRxOctets_Type()
)
pxmEthIntfPmRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxOctets.setStatus("current")
_PxmEthIntfPmRxCrcAlignedErr_Type = Integer32
_PxmEthIntfPmRxCrcAlignedErr_Object = MibTableColumn
pxmEthIntfPmRxCrcAlignedErr = _PxmEthIntfPmRxCrcAlignedErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 6),
    _PxmEthIntfPmRxCrcAlignedErr_Type()
)
pxmEthIntfPmRxCrcAlignedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxCrcAlignedErr.setStatus("current")
_PxmEthIntfPmRxUndersized_Type = HCPerfIntervalCount
_PxmEthIntfPmRxUndersized_Object = MibTableColumn
pxmEthIntfPmRxUndersized = _PxmEthIntfPmRxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 7),
    _PxmEthIntfPmRxUndersized_Type()
)
pxmEthIntfPmRxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxUndersized.setStatus("current")
_PxmEthIntfPmRxOversized_Type = HCPerfIntervalCount
_PxmEthIntfPmRxOversized_Object = MibTableColumn
pxmEthIntfPmRxOversized = _PxmEthIntfPmRxOversized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 8),
    _PxmEthIntfPmRxOversized_Type()
)
pxmEthIntfPmRxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxOversized.setStatus("current")
_PxmEthIntfPmRxUnicastPkts_Type = HCPerfIntervalCount
_PxmEthIntfPmRxUnicastPkts_Object = MibTableColumn
pxmEthIntfPmRxUnicastPkts = _PxmEthIntfPmRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 9),
    _PxmEthIntfPmRxUnicastPkts_Type()
)
pxmEthIntfPmRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxUnicastPkts.setStatus("current")
_PxmEthIntfPmRxBroadcastPkts_Type = HCPerfIntervalCount
_PxmEthIntfPmRxBroadcastPkts_Object = MibTableColumn
pxmEthIntfPmRxBroadcastPkts = _PxmEthIntfPmRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 10),
    _PxmEthIntfPmRxBroadcastPkts_Type()
)
pxmEthIntfPmRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxBroadcastPkts.setStatus("current")
_PxmEthIntfPmRxMulticastPkts_Type = HCPerfIntervalCount
_PxmEthIntfPmRxMulticastPkts_Object = MibTableColumn
pxmEthIntfPmRxMulticastPkts = _PxmEthIntfPmRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 11),
    _PxmEthIntfPmRxMulticastPkts_Type()
)
pxmEthIntfPmRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxMulticastPkts.setStatus("current")
_PxmEthIntfPmRxPktErrors_Type = HCPerfIntervalCount
_PxmEthIntfPmRxPktErrors_Object = MibTableColumn
pxmEthIntfPmRxPktErrors = _PxmEthIntfPmRxPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 12),
    _PxmEthIntfPmRxPktErrors_Type()
)
pxmEthIntfPmRxPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxPktErrors.setStatus("current")
_PxmEthIntfPmRxSize64_Type = HCPerfIntervalCount
_PxmEthIntfPmRxSize64_Object = MibTableColumn
pxmEthIntfPmRxSize64 = _PxmEthIntfPmRxSize64_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 13),
    _PxmEthIntfPmRxSize64_Type()
)
pxmEthIntfPmRxSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxSize64.setStatus("current")
_PxmEthIntfPmRxSize65to127_Type = HCPerfIntervalCount
_PxmEthIntfPmRxSize65to127_Object = MibTableColumn
pxmEthIntfPmRxSize65to127 = _PxmEthIntfPmRxSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 14),
    _PxmEthIntfPmRxSize65to127_Type()
)
pxmEthIntfPmRxSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxSize65to127.setStatus("current")
_PxmEthIntfPmRxSize128to255_Type = HCPerfIntervalCount
_PxmEthIntfPmRxSize128to255_Object = MibTableColumn
pxmEthIntfPmRxSize128to255 = _PxmEthIntfPmRxSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 15),
    _PxmEthIntfPmRxSize128to255_Type()
)
pxmEthIntfPmRxSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxSize128to255.setStatus("current")
_PxmEthIntfPmRxSize256to511_Type = HCPerfIntervalCount
_PxmEthIntfPmRxSize256to511_Object = MibTableColumn
pxmEthIntfPmRxSize256to511 = _PxmEthIntfPmRxSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 16),
    _PxmEthIntfPmRxSize256to511_Type()
)
pxmEthIntfPmRxSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxSize256to511.setStatus("current")
_PxmEthIntfPmRxSize512to1023_Type = HCPerfIntervalCount
_PxmEthIntfPmRxSize512to1023_Object = MibTableColumn
pxmEthIntfPmRxSize512to1023 = _PxmEthIntfPmRxSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 17),
    _PxmEthIntfPmRxSize512to1023_Type()
)
pxmEthIntfPmRxSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxSize512to1023.setStatus("current")
_PxmEthIntfPmRxSize1024to1518_Type = HCPerfIntervalCount
_PxmEthIntfPmRxSize1024to1518_Object = MibTableColumn
pxmEthIntfPmRxSize1024to1518 = _PxmEthIntfPmRxSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 18),
    _PxmEthIntfPmRxSize1024to1518_Type()
)
pxmEthIntfPmRxSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmRxSize1024to1518.setStatus("current")
_PxmEthIntfPmTxPackets_Type = HCPerfIntervalCount
_PxmEthIntfPmTxPackets_Object = MibTableColumn
pxmEthIntfPmTxPackets = _PxmEthIntfPmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 19),
    _PxmEthIntfPmTxPackets_Type()
)
pxmEthIntfPmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmTxPackets.setStatus("current")
_PxmEthIntfPmTxOctets_Type = HCPerfIntervalCount
_PxmEthIntfPmTxOctets_Object = MibTableColumn
pxmEthIntfPmTxOctets = _PxmEthIntfPmTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 20),
    _PxmEthIntfPmTxOctets_Type()
)
pxmEthIntfPmTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmTxOctets.setStatus("current")
_PxmEthIntfPmTxUnicastPkts_Type = HCPerfIntervalCount
_PxmEthIntfPmTxUnicastPkts_Object = MibTableColumn
pxmEthIntfPmTxUnicastPkts = _PxmEthIntfPmTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 21),
    _PxmEthIntfPmTxUnicastPkts_Type()
)
pxmEthIntfPmTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmTxUnicastPkts.setStatus("current")
_PxmEthIntfPmTxBroadcastPkts_Type = HCPerfIntervalCount
_PxmEthIntfPmTxBroadcastPkts_Object = MibTableColumn
pxmEthIntfPmTxBroadcastPkts = _PxmEthIntfPmTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 22),
    _PxmEthIntfPmTxBroadcastPkts_Type()
)
pxmEthIntfPmTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmTxBroadcastPkts.setStatus("current")
_PxmEthIntfPmTxMulticastPkts_Type = HCPerfIntervalCount
_PxmEthIntfPmTxMulticastPkts_Object = MibTableColumn
pxmEthIntfPmTxMulticastPkts = _PxmEthIntfPmTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 23),
    _PxmEthIntfPmTxMulticastPkts_Type()
)
pxmEthIntfPmTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmTxMulticastPkts.setStatus("current")
_PxmEthIntfPmTxPktErrors_Type = HCPerfIntervalCount
_PxmEthIntfPmTxPktErrors_Object = MibTableColumn
pxmEthIntfPmTxPktErrors = _PxmEthIntfPmTxPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 1, 2, 1, 24),
    _PxmEthIntfPmTxPktErrors_Type()
)
pxmEthIntfPmTxPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfPmTxPktErrors.setStatus("current")
_PxmEthIntfBwpPm_ObjectIdentity = ObjectIdentity
pxmEthIntfBwpPm = _PxmEthIntfBwpPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2)
)
_PxmBwpEthIntfPmRealTable_Object = MibTable
pxmBwpEthIntfPmRealTable = _PxmBwpEthIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 1)
)
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealTable.setStatus("current")
_PxmBwpEthIntfPmRealEntry_Object = MibTableRow
pxmBwpEthIntfPmRealEntry = _PxmBwpEthIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 1, 1)
)
pxmBwpEthIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealEntry.setStatus("current")
_PxmBwpEthIntfPmRealPolicerConformedPkts_Type = Counter64
_PxmBwpEthIntfPmRealPolicerConformedPkts_Object = MibTableColumn
pxmBwpEthIntfPmRealPolicerConformedPkts = _PxmBwpEthIntfPmRealPolicerConformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 1, 1, 1),
    _PxmBwpEthIntfPmRealPolicerConformedPkts_Type()
)
pxmBwpEthIntfPmRealPolicerConformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealPolicerConformedPkts.setStatus("current")
_PxmBwpEthIntfPmRealPolicerConformedOctets_Type = Counter64
_PxmBwpEthIntfPmRealPolicerConformedOctets_Object = MibTableColumn
pxmBwpEthIntfPmRealPolicerConformedOctets = _PxmBwpEthIntfPmRealPolicerConformedOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 1, 1, 2),
    _PxmBwpEthIntfPmRealPolicerConformedOctets_Type()
)
pxmBwpEthIntfPmRealPolicerConformedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealPolicerConformedOctets.setStatus("current")
_PxmBwpEthIntfPmRealPolicerExceededPkts_Type = Counter64
_PxmBwpEthIntfPmRealPolicerExceededPkts_Object = MibTableColumn
pxmBwpEthIntfPmRealPolicerExceededPkts = _PxmBwpEthIntfPmRealPolicerExceededPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 1, 1, 3),
    _PxmBwpEthIntfPmRealPolicerExceededPkts_Type()
)
pxmBwpEthIntfPmRealPolicerExceededPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealPolicerExceededPkts.setStatus("current")
_PxmBwpEthIntfPmRealPolicerExceededOctets_Type = Counter64
_PxmBwpEthIntfPmRealPolicerExceededOctets_Object = MibTableColumn
pxmBwpEthIntfPmRealPolicerExceededOctets = _PxmBwpEthIntfPmRealPolicerExceededOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 1, 1, 4),
    _PxmBwpEthIntfPmRealPolicerExceededOctets_Type()
)
pxmBwpEthIntfPmRealPolicerExceededOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealPolicerExceededOctets.setStatus("current")
_PxmBwpEthIntfPmRealPolicerViolatedPkts_Type = Counter64
_PxmBwpEthIntfPmRealPolicerViolatedPkts_Object = MibTableColumn
pxmBwpEthIntfPmRealPolicerViolatedPkts = _PxmBwpEthIntfPmRealPolicerViolatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 1, 1, 5),
    _PxmBwpEthIntfPmRealPolicerViolatedPkts_Type()
)
pxmBwpEthIntfPmRealPolicerViolatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealPolicerViolatedPkts.setStatus("current")
_PxmBwpEthIntfPmRealPolicerViolatedOctets_Type = Counter64
_PxmBwpEthIntfPmRealPolicerViolatedOctets_Object = MibTableColumn
pxmBwpEthIntfPmRealPolicerViolatedOctets = _PxmBwpEthIntfPmRealPolicerViolatedOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 1, 1, 6),
    _PxmBwpEthIntfPmRealPolicerViolatedOctets_Type()
)
pxmBwpEthIntfPmRealPolicerViolatedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealPolicerViolatedOctets.setStatus("current")
_PxmBwpEthIntfPmTable_Object = MibTable
pxmBwpEthIntfPmTable = _PxmBwpEthIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2)
)
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmTable.setStatus("current")
_PxmBwpEthIntfPmEntry_Object = MibTableRow
pxmBwpEthIntfPmEntry = _PxmBwpEthIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1)
)
pxmBwpEthIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmEntry.setStatus("current")


class _PxmBwpEthIntfPmTimestamp_Type(Integer32):
    """Custom type pxmBwpEthIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmBwpEthIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmBwpEthIntfPmTimestamp_Object = MibTableColumn
pxmBwpEthIntfPmTimestamp = _PxmBwpEthIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 1),
    _PxmBwpEthIntfPmTimestamp_Type()
)
pxmBwpEthIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmTimestamp.setStatus("current")


class _PxmBwpEthIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmBwpEthIntfPmSampleDuration based on Integer32"""
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


_PxmBwpEthIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmBwpEthIntfPmSampleDuration_Object = MibTableColumn
pxmBwpEthIntfPmSampleDuration = _PxmBwpEthIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 2),
    _PxmBwpEthIntfPmSampleDuration_Type()
)
pxmBwpEthIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmSampleDuration.setStatus("current")
_PxmBwpEthIntfPmValidity_Type = TruthValue
_PxmBwpEthIntfPmValidity_Object = MibTableColumn
pxmBwpEthIntfPmValidity = _PxmBwpEthIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 3),
    _PxmBwpEthIntfPmValidity_Type()
)
pxmBwpEthIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmValidity.setStatus("current")
_PxmBwpEthIntfPmPolicerConformedPkts_Type = HCPerfIntervalCount
_PxmBwpEthIntfPmPolicerConformedPkts_Object = MibTableColumn
pxmBwpEthIntfPmPolicerConformedPkts = _PxmBwpEthIntfPmPolicerConformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 4),
    _PxmBwpEthIntfPmPolicerConformedPkts_Type()
)
pxmBwpEthIntfPmPolicerConformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmPolicerConformedPkts.setStatus("current")
_PxmBwpEthIntfPmPolicerConformedOctets_Type = HCPerfIntervalCount
_PxmBwpEthIntfPmPolicerConformedOctets_Object = MibTableColumn
pxmBwpEthIntfPmPolicerConformedOctets = _PxmBwpEthIntfPmPolicerConformedOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 5),
    _PxmBwpEthIntfPmPolicerConformedOctets_Type()
)
pxmBwpEthIntfPmPolicerConformedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmPolicerConformedOctets.setStatus("current")
_PxmBwpEthIntfPmPolicerExceededPkts_Type = HCPerfIntervalCount
_PxmBwpEthIntfPmPolicerExceededPkts_Object = MibTableColumn
pxmBwpEthIntfPmPolicerExceededPkts = _PxmBwpEthIntfPmPolicerExceededPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 6),
    _PxmBwpEthIntfPmPolicerExceededPkts_Type()
)
pxmBwpEthIntfPmPolicerExceededPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmPolicerExceededPkts.setStatus("current")
_PxmBwpEthIntfPmPolicerExceededOctets_Type = HCPerfIntervalCount
_PxmBwpEthIntfPmPolicerExceededOctets_Object = MibTableColumn
pxmBwpEthIntfPmPolicerExceededOctets = _PxmBwpEthIntfPmPolicerExceededOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 7),
    _PxmBwpEthIntfPmPolicerExceededOctets_Type()
)
pxmBwpEthIntfPmPolicerExceededOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmPolicerExceededOctets.setStatus("current")
_PxmBwpEthIntfPmPolicerViolatedPkts_Type = HCPerfIntervalCount
_PxmBwpEthIntfPmPolicerViolatedPkts_Object = MibTableColumn
pxmBwpEthIntfPmPolicerViolatedPkts = _PxmBwpEthIntfPmPolicerViolatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 8),
    _PxmBwpEthIntfPmPolicerViolatedPkts_Type()
)
pxmBwpEthIntfPmPolicerViolatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmPolicerViolatedPkts.setStatus("current")
_PxmBwpEthIntfPmPolicerViolatedOctets_Type = HCPerfIntervalCount
_PxmBwpEthIntfPmPolicerViolatedOctets_Object = MibTableColumn
pxmBwpEthIntfPmPolicerViolatedOctets = _PxmBwpEthIntfPmPolicerViolatedOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 2, 2, 1, 9),
    _PxmBwpEthIntfPmPolicerViolatedOctets_Type()
)
pxmBwpEthIntfPmPolicerViolatedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmPolicerViolatedOctets.setStatus("current")
_PxmCmEthIntfPmObjects_ObjectIdentity = ObjectIdentity
pxmCmEthIntfPmObjects = _PxmCmEthIntfPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3)
)
_PxmCmEthIntfRealPm_ObjectIdentity = ObjectIdentity
pxmCmEthIntfRealPm = _PxmCmEthIntfRealPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1)
)
_PxmTC0EthIntfPmRealTable_Object = MibTable
pxmTC0EthIntfPmRealTable = _PxmTC0EthIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealTable.setStatus("current")
_PxmTC0EthIntfPmRealEntry_Object = MibTableRow
pxmTC0EthIntfPmRealEntry = _PxmTC0EthIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1)
)
pxmTC0EthIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealEntry.setStatus("current")
_PxmTC0EthIntfPmRealTCNum_Type = Integer32
_PxmTC0EthIntfPmRealTCNum_Object = MibTableColumn
pxmTC0EthIntfPmRealTCNum = _PxmTC0EthIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 1),
    _PxmTC0EthIntfPmRealTCNum_Type()
)
pxmTC0EthIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealTCNum.setStatus("current")
_PxmTC0EthIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC0EthIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC0EthIntfPmRealTDQueuingCurrentQDepth = _PxmTC0EthIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 2),
    _PxmTC0EthIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC0EthIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC0EthIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC0EthIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC0EthIntfPmRealQueueingDiscardOctets = _PxmTC0EthIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 3),
    _PxmTC0EthIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC0EthIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC0EthIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC0EthIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC0EthIntfPmRealQueueingDiscardPkts = _PxmTC0EthIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 4),
    _PxmTC0EthIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC0EthIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC0EthIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC0EthIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC0EthIntfPmRealRandomGreenDropPkts = _PxmTC0EthIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 5),
    _PxmTC0EthIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC0EthIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC0EthIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC0EthIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC0EthIntfPmRealRandomGreenDropOctets = _PxmTC0EthIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 6),
    _PxmTC0EthIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC0EthIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC0EthIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC0EthIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC0EthIntfPmRealRandomYellowDropPkts = _PxmTC0EthIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 7),
    _PxmTC0EthIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC0EthIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC0EthIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC0EthIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC0EthIntfPmRealRandomYellowDropOctets = _PxmTC0EthIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 8),
    _PxmTC0EthIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC0EthIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC0EthIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC0EthIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC0EthIntfPmRealQueueingTransmitPkts = _PxmTC0EthIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 9),
    _PxmTC0EthIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC0EthIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC0EthIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC0EthIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC0EthIntfPmRealQueueingTransmitOctets = _PxmTC0EthIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 10),
    _PxmTC0EthIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC0EthIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC0EthIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC0EthIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC0EthIntfPmRealQueueingMeanQSizeUnit = _PxmTC0EthIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 11),
    _PxmTC0EthIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC0EthIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC0EthIntfPmRealMeanQSize_Type = Integer32
_PxmTC0EthIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC0EthIntfPmRealMeanQSize = _PxmTC0EthIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 1, 1, 12),
    _PxmTC0EthIntfPmRealMeanQSize_Type()
)
pxmTC0EthIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealMeanQSize.setStatus("current")
_PxmTC2EthIntfPmRealTable_Object = MibTable
pxmTC2EthIntfPmRealTable = _PxmTC2EthIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2)
)
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealTable.setStatus("current")
_PxmTC2EthIntfPmRealEntry_Object = MibTableRow
pxmTC2EthIntfPmRealEntry = _PxmTC2EthIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1)
)
pxmTC2EthIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealEntry.setStatus("current")
_PxmTC2EthIntfPmRealTCNum_Type = Integer32
_PxmTC2EthIntfPmRealTCNum_Object = MibTableColumn
pxmTC2EthIntfPmRealTCNum = _PxmTC2EthIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 1),
    _PxmTC2EthIntfPmRealTCNum_Type()
)
pxmTC2EthIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealTCNum.setStatus("current")
_PxmTC2EthIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC2EthIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC2EthIntfPmRealTDQueuingCurrentQDepth = _PxmTC2EthIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 2),
    _PxmTC2EthIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC2EthIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC2EthIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC2EthIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC2EthIntfPmRealQueueingDiscardOctets = _PxmTC2EthIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 3),
    _PxmTC2EthIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC2EthIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC2EthIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC2EthIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC2EthIntfPmRealQueueingDiscardPkts = _PxmTC2EthIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 4),
    _PxmTC2EthIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC2EthIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC2EthIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC2EthIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC2EthIntfPmRealRandomGreenDropPkts = _PxmTC2EthIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 5),
    _PxmTC2EthIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC2EthIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC2EthIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC2EthIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC2EthIntfPmRealRandomGreenDropOctets = _PxmTC2EthIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 6),
    _PxmTC2EthIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC2EthIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC2EthIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC2EthIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC2EthIntfPmRealRandomYellowDropPkts = _PxmTC2EthIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 7),
    _PxmTC2EthIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC2EthIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC2EthIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC2EthIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC2EthIntfPmRealRandomYellowDropOctets = _PxmTC2EthIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 8),
    _PxmTC2EthIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC2EthIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC2EthIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC2EthIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC2EthIntfPmRealQueueingTransmitPkts = _PxmTC2EthIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 9),
    _PxmTC2EthIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC2EthIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC2EthIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC2EthIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC2EthIntfPmRealQueueingTransmitOctets = _PxmTC2EthIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 10),
    _PxmTC2EthIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC2EthIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC2EthIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC2EthIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC2EthIntfPmRealQueueingMeanQSizeUnit = _PxmTC2EthIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 11),
    _PxmTC2EthIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC2EthIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC2EthIntfPmRealMeanQSize_Type = Integer32
_PxmTC2EthIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC2EthIntfPmRealMeanQSize = _PxmTC2EthIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 2, 1, 12),
    _PxmTC2EthIntfPmRealMeanQSize_Type()
)
pxmTC2EthIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealMeanQSize.setStatus("current")
_PxmTC4EthIntfPmRealTable_Object = MibTable
pxmTC4EthIntfPmRealTable = _PxmTC4EthIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3)
)
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealTable.setStatus("current")
_PxmTC4EthIntfPmRealEntry_Object = MibTableRow
pxmTC4EthIntfPmRealEntry = _PxmTC4EthIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1)
)
pxmTC4EthIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealEntry.setStatus("current")
_PxmTC4EthIntfPmRealTCNum_Type = Integer32
_PxmTC4EthIntfPmRealTCNum_Object = MibTableColumn
pxmTC4EthIntfPmRealTCNum = _PxmTC4EthIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 1),
    _PxmTC4EthIntfPmRealTCNum_Type()
)
pxmTC4EthIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealTCNum.setStatus("current")
_PxmTC4EthIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC4EthIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC4EthIntfPmRealTDQueuingCurrentQDepth = _PxmTC4EthIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 2),
    _PxmTC4EthIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC4EthIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC4EthIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC4EthIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC4EthIntfPmRealQueueingDiscardOctets = _PxmTC4EthIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 3),
    _PxmTC4EthIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC4EthIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC4EthIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC4EthIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC4EthIntfPmRealQueueingDiscardPkts = _PxmTC4EthIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 4),
    _PxmTC4EthIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC4EthIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC4EthIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC4EthIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC4EthIntfPmRealRandomGreenDropPkts = _PxmTC4EthIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 5),
    _PxmTC4EthIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC4EthIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC4EthIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC4EthIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC4EthIntfPmRealRandomGreenDropOctets = _PxmTC4EthIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 6),
    _PxmTC4EthIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC4EthIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC4EthIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC4EthIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC4EthIntfPmRealRandomYellowDropPkts = _PxmTC4EthIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 7),
    _PxmTC4EthIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC4EthIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC4EthIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC4EthIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC4EthIntfPmRealRandomYellowDropOctets = _PxmTC4EthIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 8),
    _PxmTC4EthIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC4EthIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC4EthIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC4EthIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC4EthIntfPmRealQueueingTransmitPkts = _PxmTC4EthIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 9),
    _PxmTC4EthIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC4EthIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC4EthIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC4EthIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC4EthIntfPmRealQueueingTransmitOctets = _PxmTC4EthIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 10),
    _PxmTC4EthIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC4EthIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC4EthIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC4EthIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC4EthIntfPmRealQueueingMeanQSizeUnit = _PxmTC4EthIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 11),
    _PxmTC4EthIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC4EthIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC4EthIntfPmRealMeanQSize_Type = Integer32
_PxmTC4EthIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC4EthIntfPmRealMeanQSize = _PxmTC4EthIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 3, 1, 12),
    _PxmTC4EthIntfPmRealMeanQSize_Type()
)
pxmTC4EthIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealMeanQSize.setStatus("current")
_PxmTC6EthIntfPmRealTable_Object = MibTable
pxmTC6EthIntfPmRealTable = _PxmTC6EthIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4)
)
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealTable.setStatus("current")
_PxmTC6EthIntfPmRealEntry_Object = MibTableRow
pxmTC6EthIntfPmRealEntry = _PxmTC6EthIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1)
)
pxmTC6EthIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealEntry.setStatus("current")
_PxmTC6EthIntfPmRealTCNum_Type = Integer32
_PxmTC6EthIntfPmRealTCNum_Object = MibTableColumn
pxmTC6EthIntfPmRealTCNum = _PxmTC6EthIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 1),
    _PxmTC6EthIntfPmRealTCNum_Type()
)
pxmTC6EthIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealTCNum.setStatus("current")
_PxmTC6EthIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC6EthIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC6EthIntfPmRealTDQueuingCurrentQDepth = _PxmTC6EthIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 2),
    _PxmTC6EthIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC6EthIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC6EthIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC6EthIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC6EthIntfPmRealQueueingDiscardOctets = _PxmTC6EthIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 3),
    _PxmTC6EthIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC6EthIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC6EthIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC6EthIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC6EthIntfPmRealQueueingDiscardPkts = _PxmTC6EthIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 4),
    _PxmTC6EthIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC6EthIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC6EthIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC6EthIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC6EthIntfPmRealRandomGreenDropPkts = _PxmTC6EthIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 5),
    _PxmTC6EthIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC6EthIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC6EthIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC6EthIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC6EthIntfPmRealRandomGreenDropOctets = _PxmTC6EthIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 6),
    _PxmTC6EthIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC6EthIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC6EthIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC6EthIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC6EthIntfPmRealRandomYellowDropPkts = _PxmTC6EthIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 7),
    _PxmTC6EthIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC6EthIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC6EthIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC6EthIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC6EthIntfPmRealRandomYellowDropOctets = _PxmTC6EthIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 8),
    _PxmTC6EthIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC6EthIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC6EthIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC6EthIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC6EthIntfPmRealQueueingTransmitPkts = _PxmTC6EthIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 9),
    _PxmTC6EthIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC6EthIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC6EthIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC6EthIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC6EthIntfPmRealQueueingTransmitOctets = _PxmTC6EthIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 10),
    _PxmTC6EthIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC6EthIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC6EthIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC6EthIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC6EthIntfPmRealQueueingMeanQSizeUnit = _PxmTC6EthIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 11),
    _PxmTC6EthIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC6EthIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC6EthIntfPmRealMeanQSize_Type = Integer32
_PxmTC6EthIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC6EthIntfPmRealMeanQSize = _PxmTC6EthIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 4, 1, 12),
    _PxmTC6EthIntfPmRealMeanQSize_Type()
)
pxmTC6EthIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealMeanQSize.setStatus("current")
_PxmTC7EthIntfPmRealTable_Object = MibTable
pxmTC7EthIntfPmRealTable = _PxmTC7EthIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5)
)
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealTable.setStatus("current")
_PxmTC7EthIntfPmRealEntry_Object = MibTableRow
pxmTC7EthIntfPmRealEntry = _PxmTC7EthIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1)
)
pxmTC7EthIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealEntry.setStatus("current")
_PxmTC7EthIntfPmRealTCNum_Type = Integer32
_PxmTC7EthIntfPmRealTCNum_Object = MibTableColumn
pxmTC7EthIntfPmRealTCNum = _PxmTC7EthIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 1),
    _PxmTC7EthIntfPmRealTCNum_Type()
)
pxmTC7EthIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealTCNum.setStatus("current")
_PxmTC7EthIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC7EthIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC7EthIntfPmRealTDQueuingCurrentQDepth = _PxmTC7EthIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 2),
    _PxmTC7EthIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC7EthIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC7EthIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC7EthIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC7EthIntfPmRealQueueingDiscardOctets = _PxmTC7EthIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 3),
    _PxmTC7EthIntfPmRealQueueingDiscardOctets_Type()
)
pxmTC7EthIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC7EthIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC7EthIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC7EthIntfPmRealQueueingDiscardPkts = _PxmTC7EthIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 4),
    _PxmTC7EthIntfPmRealQueueingDiscardPkts_Type()
)
pxmTC7EthIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC7EthIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC7EthIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC7EthIntfPmRealRandomGreenDropPkts = _PxmTC7EthIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 5),
    _PxmTC7EthIntfPmRealRandomGreenDropPkts_Type()
)
pxmTC7EthIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC7EthIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC7EthIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC7EthIntfPmRealRandomGreenDropOctets = _PxmTC7EthIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 6),
    _PxmTC7EthIntfPmRealRandomGreenDropOctets_Type()
)
pxmTC7EthIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC7EthIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC7EthIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC7EthIntfPmRealRandomYellowDropPkts = _PxmTC7EthIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 7),
    _PxmTC7EthIntfPmRealRandomYellowDropPkts_Type()
)
pxmTC7EthIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC7EthIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC7EthIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC7EthIntfPmRealRandomYellowDropOctets = _PxmTC7EthIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 8),
    _PxmTC7EthIntfPmRealRandomYellowDropOctets_Type()
)
pxmTC7EthIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC7EthIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC7EthIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC7EthIntfPmRealQueueingTransmitPkts = _PxmTC7EthIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 9),
    _PxmTC7EthIntfPmRealQueueingTransmitPkts_Type()
)
pxmTC7EthIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC7EthIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC7EthIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC7EthIntfPmRealQueueingTransmitOctets = _PxmTC7EthIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 10),
    _PxmTC7EthIntfPmRealQueueingTransmitOctets_Type()
)
pxmTC7EthIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC7EthIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC7EthIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC7EthIntfPmRealQueueingMeanQSizeUnit = _PxmTC7EthIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 11),
    _PxmTC7EthIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC7EthIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC7EthIntfPmRealMeanQSize_Type = Integer32
_PxmTC7EthIntfPmRealMeanQSize_Object = MibTableColumn
pxmTC7EthIntfPmRealMeanQSize = _PxmTC7EthIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 5, 1, 12),
    _PxmTC7EthIntfPmRealMeanQSize_Type()
)
pxmTC7EthIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealMeanQSize.setStatus("current")
_PxmTCANYEthIntfPmRealTable_Object = MibTable
pxmTCANYEthIntfPmRealTable = _PxmTCANYEthIntfPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6)
)
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealTable.setStatus("current")
_PxmTCANYEthIntfPmRealEntry_Object = MibTableRow
pxmTCANYEthIntfPmRealEntry = _PxmTCANYEthIntfPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1)
)
pxmTCANYEthIntfPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealEntry.setStatus("current")
_PxmTCANYEthIntfPmRealTCNum_Type = Integer32
_PxmTCANYEthIntfPmRealTCNum_Object = MibTableColumn
pxmTCANYEthIntfPmRealTCNum = _PxmTCANYEthIntfPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 1),
    _PxmTCANYEthIntfPmRealTCNum_Type()
)
pxmTCANYEthIntfPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealTCNum.setStatus("current")
_PxmTCANYEthIntfPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTCANYEthIntfPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTCANYEthIntfPmRealTDQueuingCurrentQDepth = _PxmTCANYEthIntfPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 2),
    _PxmTCANYEthIntfPmRealTDQueuingCurrentQDepth_Type()
)
pxmTCANYEthIntfPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTCANYEthIntfPmRealQueueingDiscardOctets_Type = Counter64
_PxmTCANYEthIntfPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTCANYEthIntfPmRealQueueingDiscardOctets = _PxmTCANYEthIntfPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 3),
    _PxmTCANYEthIntfPmRealQueueingDiscardOctets_Type()
)
pxmTCANYEthIntfPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealQueueingDiscardOctets.setStatus("current")
_PxmTCANYEthIntfPmRealQueueingDiscardPkts_Type = Integer32
_PxmTCANYEthIntfPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTCANYEthIntfPmRealQueueingDiscardPkts = _PxmTCANYEthIntfPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 4),
    _PxmTCANYEthIntfPmRealQueueingDiscardPkts_Type()
)
pxmTCANYEthIntfPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealQueueingDiscardPkts.setStatus("current")
_PxmTCANYEthIntfPmRealRandomGreenDropPkts_Type = Counter64
_PxmTCANYEthIntfPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTCANYEthIntfPmRealRandomGreenDropPkts = _PxmTCANYEthIntfPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 5),
    _PxmTCANYEthIntfPmRealRandomGreenDropPkts_Type()
)
pxmTCANYEthIntfPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealRandomGreenDropPkts.setStatus("current")
_PxmTCANYEthIntfPmRealRandomGreenDropOctets_Type = Counter64
_PxmTCANYEthIntfPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTCANYEthIntfPmRealRandomGreenDropOctets = _PxmTCANYEthIntfPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 6),
    _PxmTCANYEthIntfPmRealRandomGreenDropOctets_Type()
)
pxmTCANYEthIntfPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealRandomGreenDropOctets.setStatus("current")
_PxmTCANYEthIntfPmRealRandomYellowDropPkts_Type = Counter64
_PxmTCANYEthIntfPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTCANYEthIntfPmRealRandomYellowDropPkts = _PxmTCANYEthIntfPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 7),
    _PxmTCANYEthIntfPmRealRandomYellowDropPkts_Type()
)
pxmTCANYEthIntfPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealRandomYellowDropPkts.setStatus("current")
_PxmTCANYEthIntfPmRealRandomYellowDropOctets_Type = Counter64
_PxmTCANYEthIntfPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTCANYEthIntfPmRealRandomYellowDropOctets = _PxmTCANYEthIntfPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 8),
    _PxmTCANYEthIntfPmRealRandomYellowDropOctets_Type()
)
pxmTCANYEthIntfPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealRandomYellowDropOctets.setStatus("current")
_PxmTCANYEthIntfPmRealQueueingTransmitPkts_Type = Counter64
_PxmTCANYEthIntfPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTCANYEthIntfPmRealQueueingTransmitPkts = _PxmTCANYEthIntfPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 9),
    _PxmTCANYEthIntfPmRealQueueingTransmitPkts_Type()
)
pxmTCANYEthIntfPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealQueueingTransmitPkts.setStatus("current")
_PxmTCANYEthIntfPmRealQueueingTransmitOctets_Type = Counter64
_PxmTCANYEthIntfPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTCANYEthIntfPmRealQueueingTransmitOctets = _PxmTCANYEthIntfPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 10),
    _PxmTCANYEthIntfPmRealQueueingTransmitOctets_Type()
)
pxmTCANYEthIntfPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealQueueingTransmitOctets.setStatus("current")
_PxmTCANYEthIntfPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTCANYEthIntfPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTCANYEthIntfPmRealQueueingMeanQSizeUnit = _PxmTCANYEthIntfPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 11),
    _PxmTCANYEthIntfPmRealQueueingMeanQSizeUnit_Type()
)
pxmTCANYEthIntfPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTCANYEthIntfPmRealMeanQSize_Type = Integer32
_PxmTCANYEthIntfPmRealMeanQSize_Object = MibTableColumn
pxmTCANYEthIntfPmRealMeanQSize = _PxmTCANYEthIntfPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 1, 6, 1, 12),
    _PxmTCANYEthIntfPmRealMeanQSize_Type()
)
pxmTCANYEthIntfPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealMeanQSize.setStatus("current")
_PxmCmEthIntfPm_ObjectIdentity = ObjectIdentity
pxmCmEthIntfPm = _PxmCmEthIntfPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2)
)
_PxmTC0EthIntfPmTable_Object = MibTable
pxmTC0EthIntfPmTable = _PxmTC0EthIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmTable.setStatus("current")
_PxmTC0EthIntfPmEntry_Object = MibTableRow
pxmTC0EthIntfPmEntry = _PxmTC0EthIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1)
)
pxmTC0EthIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmEntry.setStatus("current")


class _PxmTC0EthIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC0EthIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC0EthIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC0EthIntfPmTimestamp_Object = MibTableColumn
pxmTC0EthIntfPmTimestamp = _PxmTC0EthIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 1),
    _PxmTC0EthIntfPmTimestamp_Type()
)
pxmTC0EthIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmTimestamp.setStatus("current")


class _PxmTC0EthIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC0EthIntfPmSampleDuration based on Integer32"""
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


_PxmTC0EthIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC0EthIntfPmSampleDuration_Object = MibTableColumn
pxmTC0EthIntfPmSampleDuration = _PxmTC0EthIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 2),
    _PxmTC0EthIntfPmSampleDuration_Type()
)
pxmTC0EthIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmSampleDuration.setStatus("current")
_PxmTC0EthIntfPmValidity_Type = TruthValue
_PxmTC0EthIntfPmValidity_Object = MibTableColumn
pxmTC0EthIntfPmValidity = _PxmTC0EthIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 3),
    _PxmTC0EthIntfPmValidity_Type()
)
pxmTC0EthIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmValidity.setStatus("current")
_PxmTC0EthIntfPmTCNum_Type = Integer32
_PxmTC0EthIntfPmTCNum_Object = MibTableColumn
pxmTC0EthIntfPmTCNum = _PxmTC0EthIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 4),
    _PxmTC0EthIntfPmTCNum_Type()
)
pxmTC0EthIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmTCNum.setStatus("current")
_PxmTC0EthIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC0EthIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC0EthIntfPmQueueingDiscardOctets = _PxmTC0EthIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 5),
    _PxmTC0EthIntfPmQueueingDiscardOctets_Type()
)
pxmTC0EthIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC0EthIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC0EthIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC0EthIntfPmQueueingDiscardPkts = _PxmTC0EthIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 6),
    _PxmTC0EthIntfPmQueueingDiscardPkts_Type()
)
pxmTC0EthIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC0EthIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC0EthIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC0EthIntfPmRandomGreenDropPkts = _PxmTC0EthIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 7),
    _PxmTC0EthIntfPmRandomGreenDropPkts_Type()
)
pxmTC0EthIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC0EthIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC0EthIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC0EthIntfPmRandomGreenDropOctets = _PxmTC0EthIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 8),
    _PxmTC0EthIntfPmRandomGreenDropOctets_Type()
)
pxmTC0EthIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC0EthIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC0EthIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC0EthIntfPmRandomYellowDropPkts = _PxmTC0EthIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 9),
    _PxmTC0EthIntfPmRandomYellowDropPkts_Type()
)
pxmTC0EthIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC0EthIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC0EthIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC0EthIntfPmRandomYellowDropOctets = _PxmTC0EthIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 10),
    _PxmTC0EthIntfPmRandomYellowDropOctets_Type()
)
pxmTC0EthIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC0EthIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC0EthIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC0EthIntfPmQueueingTransmitPkts = _PxmTC0EthIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 11),
    _PxmTC0EthIntfPmQueueingTransmitPkts_Type()
)
pxmTC0EthIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC0EthIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC0EthIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC0EthIntfPmQueueingTransmitOctets = _PxmTC0EthIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 1, 1, 12),
    _PxmTC0EthIntfPmQueueingTransmitOctets_Type()
)
pxmTC0EthIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTC2EthIntfPmTable_Object = MibTable
pxmTC2EthIntfPmTable = _PxmTC2EthIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2)
)
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmTable.setStatus("current")
_PxmTC2EthIntfPmEntry_Object = MibTableRow
pxmTC2EthIntfPmEntry = _PxmTC2EthIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1)
)
pxmTC2EthIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmEntry.setStatus("current")


class _PxmTC2EthIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC2EthIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC2EthIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC2EthIntfPmTimestamp_Object = MibTableColumn
pxmTC2EthIntfPmTimestamp = _PxmTC2EthIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 1),
    _PxmTC2EthIntfPmTimestamp_Type()
)
pxmTC2EthIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmTimestamp.setStatus("current")


class _PxmTC2EthIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC2EthIntfPmSampleDuration based on Integer32"""
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


_PxmTC2EthIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC2EthIntfPmSampleDuration_Object = MibTableColumn
pxmTC2EthIntfPmSampleDuration = _PxmTC2EthIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 2),
    _PxmTC2EthIntfPmSampleDuration_Type()
)
pxmTC2EthIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmSampleDuration.setStatus("current")
_PxmTC2EthIntfPmValidity_Type = TruthValue
_PxmTC2EthIntfPmValidity_Object = MibTableColumn
pxmTC2EthIntfPmValidity = _PxmTC2EthIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 3),
    _PxmTC2EthIntfPmValidity_Type()
)
pxmTC2EthIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmValidity.setStatus("current")
_PxmTC2EthIntfPmTCNum_Type = Integer32
_PxmTC2EthIntfPmTCNum_Object = MibTableColumn
pxmTC2EthIntfPmTCNum = _PxmTC2EthIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 4),
    _PxmTC2EthIntfPmTCNum_Type()
)
pxmTC2EthIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmTCNum.setStatus("current")
_PxmTC2EthIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC2EthIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC2EthIntfPmQueueingDiscardOctets = _PxmTC2EthIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 5),
    _PxmTC2EthIntfPmQueueingDiscardOctets_Type()
)
pxmTC2EthIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC2EthIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC2EthIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC2EthIntfPmQueueingDiscardPkts = _PxmTC2EthIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 6),
    _PxmTC2EthIntfPmQueueingDiscardPkts_Type()
)
pxmTC2EthIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC2EthIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC2EthIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC2EthIntfPmRandomGreenDropPkts = _PxmTC2EthIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 7),
    _PxmTC2EthIntfPmRandomGreenDropPkts_Type()
)
pxmTC2EthIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC2EthIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC2EthIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC2EthIntfPmRandomGreenDropOctets = _PxmTC2EthIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 8),
    _PxmTC2EthIntfPmRandomGreenDropOctets_Type()
)
pxmTC2EthIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC2EthIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC2EthIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC2EthIntfPmRandomYellowDropPkts = _PxmTC2EthIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 9),
    _PxmTC2EthIntfPmRandomYellowDropPkts_Type()
)
pxmTC2EthIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC2EthIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC2EthIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC2EthIntfPmRandomYellowDropOctets = _PxmTC2EthIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 10),
    _PxmTC2EthIntfPmRandomYellowDropOctets_Type()
)
pxmTC2EthIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC2EthIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC2EthIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC2EthIntfPmQueueingTransmitPkts = _PxmTC2EthIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 11),
    _PxmTC2EthIntfPmQueueingTransmitPkts_Type()
)
pxmTC2EthIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC2EthIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC2EthIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC2EthIntfPmQueueingTransmitOctets = _PxmTC2EthIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 2, 1, 12),
    _PxmTC2EthIntfPmQueueingTransmitOctets_Type()
)
pxmTC2EthIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTC4EthIntfPmTable_Object = MibTable
pxmTC4EthIntfPmTable = _PxmTC4EthIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3)
)
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmTable.setStatus("current")
_PxmTC4EthIntfPmEntry_Object = MibTableRow
pxmTC4EthIntfPmEntry = _PxmTC4EthIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1)
)
pxmTC4EthIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmEntry.setStatus("current")


class _PxmTC4EthIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC4EthIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC4EthIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC4EthIntfPmTimestamp_Object = MibTableColumn
pxmTC4EthIntfPmTimestamp = _PxmTC4EthIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 1),
    _PxmTC4EthIntfPmTimestamp_Type()
)
pxmTC4EthIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmTimestamp.setStatus("current")


class _PxmTC4EthIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC4EthIntfPmSampleDuration based on Integer32"""
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


_PxmTC4EthIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC4EthIntfPmSampleDuration_Object = MibTableColumn
pxmTC4EthIntfPmSampleDuration = _PxmTC4EthIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 2),
    _PxmTC4EthIntfPmSampleDuration_Type()
)
pxmTC4EthIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmSampleDuration.setStatus("current")
_PxmTC4EthIntfPmValidity_Type = TruthValue
_PxmTC4EthIntfPmValidity_Object = MibTableColumn
pxmTC4EthIntfPmValidity = _PxmTC4EthIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 3),
    _PxmTC4EthIntfPmValidity_Type()
)
pxmTC4EthIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmValidity.setStatus("current")
_PxmTC4EthIntfPmTCNum_Type = Integer32
_PxmTC4EthIntfPmTCNum_Object = MibTableColumn
pxmTC4EthIntfPmTCNum = _PxmTC4EthIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 4),
    _PxmTC4EthIntfPmTCNum_Type()
)
pxmTC4EthIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmTCNum.setStatus("current")
_PxmTC4EthIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC4EthIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC4EthIntfPmQueueingDiscardOctets = _PxmTC4EthIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 5),
    _PxmTC4EthIntfPmQueueingDiscardOctets_Type()
)
pxmTC4EthIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC4EthIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC4EthIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC4EthIntfPmQueueingDiscardPkts = _PxmTC4EthIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 6),
    _PxmTC4EthIntfPmQueueingDiscardPkts_Type()
)
pxmTC4EthIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC4EthIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC4EthIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC4EthIntfPmRandomGreenDropPkts = _PxmTC4EthIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 7),
    _PxmTC4EthIntfPmRandomGreenDropPkts_Type()
)
pxmTC4EthIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC4EthIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC4EthIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC4EthIntfPmRandomGreenDropOctets = _PxmTC4EthIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 8),
    _PxmTC4EthIntfPmRandomGreenDropOctets_Type()
)
pxmTC4EthIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC4EthIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC4EthIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC4EthIntfPmRandomYellowDropPkts = _PxmTC4EthIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 9),
    _PxmTC4EthIntfPmRandomYellowDropPkts_Type()
)
pxmTC4EthIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC4EthIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC4EthIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC4EthIntfPmRandomYellowDropOctets = _PxmTC4EthIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 10),
    _PxmTC4EthIntfPmRandomYellowDropOctets_Type()
)
pxmTC4EthIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC4EthIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC4EthIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC4EthIntfPmQueueingTransmitPkts = _PxmTC4EthIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 11),
    _PxmTC4EthIntfPmQueueingTransmitPkts_Type()
)
pxmTC4EthIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC4EthIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC4EthIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC4EthIntfPmQueueingTransmitOctets = _PxmTC4EthIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 3, 1, 12),
    _PxmTC4EthIntfPmQueueingTransmitOctets_Type()
)
pxmTC4EthIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTC6EthIntfPmTable_Object = MibTable
pxmTC6EthIntfPmTable = _PxmTC6EthIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4)
)
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmTable.setStatus("current")
_PxmTC6EthIntfPmEntry_Object = MibTableRow
pxmTC6EthIntfPmEntry = _PxmTC6EthIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1)
)
pxmTC6EthIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmEntry.setStatus("current")


class _PxmTC6EthIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC6EthIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC6EthIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC6EthIntfPmTimestamp_Object = MibTableColumn
pxmTC6EthIntfPmTimestamp = _PxmTC6EthIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 1),
    _PxmTC6EthIntfPmTimestamp_Type()
)
pxmTC6EthIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmTimestamp.setStatus("current")


class _PxmTC6EthIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC6EthIntfPmSampleDuration based on Integer32"""
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


_PxmTC6EthIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC6EthIntfPmSampleDuration_Object = MibTableColumn
pxmTC6EthIntfPmSampleDuration = _PxmTC6EthIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 2),
    _PxmTC6EthIntfPmSampleDuration_Type()
)
pxmTC6EthIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmSampleDuration.setStatus("current")
_PxmTC6EthIntfPmValidity_Type = TruthValue
_PxmTC6EthIntfPmValidity_Object = MibTableColumn
pxmTC6EthIntfPmValidity = _PxmTC6EthIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 3),
    _PxmTC6EthIntfPmValidity_Type()
)
pxmTC6EthIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmValidity.setStatus("current")
_PxmTC6EthIntfPmTCNum_Type = Integer32
_PxmTC6EthIntfPmTCNum_Object = MibTableColumn
pxmTC6EthIntfPmTCNum = _PxmTC6EthIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 4),
    _PxmTC6EthIntfPmTCNum_Type()
)
pxmTC6EthIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmTCNum.setStatus("current")
_PxmTC6EthIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC6EthIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC6EthIntfPmQueueingDiscardOctets = _PxmTC6EthIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 5),
    _PxmTC6EthIntfPmQueueingDiscardOctets_Type()
)
pxmTC6EthIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC6EthIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC6EthIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC6EthIntfPmQueueingDiscardPkts = _PxmTC6EthIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 6),
    _PxmTC6EthIntfPmQueueingDiscardPkts_Type()
)
pxmTC6EthIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC6EthIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC6EthIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC6EthIntfPmRandomGreenDropPkts = _PxmTC6EthIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 7),
    _PxmTC6EthIntfPmRandomGreenDropPkts_Type()
)
pxmTC6EthIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC6EthIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC6EthIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC6EthIntfPmRandomGreenDropOctets = _PxmTC6EthIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 8),
    _PxmTC6EthIntfPmRandomGreenDropOctets_Type()
)
pxmTC6EthIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC6EthIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC6EthIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC6EthIntfPmRandomYellowDropPkts = _PxmTC6EthIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 9),
    _PxmTC6EthIntfPmRandomYellowDropPkts_Type()
)
pxmTC6EthIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC6EthIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC6EthIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC6EthIntfPmRandomYellowDropOctets = _PxmTC6EthIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 10),
    _PxmTC6EthIntfPmRandomYellowDropOctets_Type()
)
pxmTC6EthIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC6EthIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC6EthIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC6EthIntfPmQueueingTransmitPkts = _PxmTC6EthIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 11),
    _PxmTC6EthIntfPmQueueingTransmitPkts_Type()
)
pxmTC6EthIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC6EthIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC6EthIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC6EthIntfPmQueueingTransmitOctets = _PxmTC6EthIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 4, 1, 12),
    _PxmTC6EthIntfPmQueueingTransmitOctets_Type()
)
pxmTC6EthIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTC7EthIntfPmTable_Object = MibTable
pxmTC7EthIntfPmTable = _PxmTC7EthIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5)
)
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmTable.setStatus("current")
_PxmTC7EthIntfPmEntry_Object = MibTableRow
pxmTC7EthIntfPmEntry = _PxmTC7EthIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1)
)
pxmTC7EthIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmEntry.setStatus("current")


class _PxmTC7EthIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTC7EthIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC7EthIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTC7EthIntfPmTimestamp_Object = MibTableColumn
pxmTC7EthIntfPmTimestamp = _PxmTC7EthIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 1),
    _PxmTC7EthIntfPmTimestamp_Type()
)
pxmTC7EthIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmTimestamp.setStatus("current")


class _PxmTC7EthIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTC7EthIntfPmSampleDuration based on Integer32"""
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


_PxmTC7EthIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC7EthIntfPmSampleDuration_Object = MibTableColumn
pxmTC7EthIntfPmSampleDuration = _PxmTC7EthIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 2),
    _PxmTC7EthIntfPmSampleDuration_Type()
)
pxmTC7EthIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmSampleDuration.setStatus("current")
_PxmTC7EthIntfPmValidity_Type = TruthValue
_PxmTC7EthIntfPmValidity_Object = MibTableColumn
pxmTC7EthIntfPmValidity = _PxmTC7EthIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 3),
    _PxmTC7EthIntfPmValidity_Type()
)
pxmTC7EthIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmValidity.setStatus("current")
_PxmTC7EthIntfPmTCNum_Type = Integer32
_PxmTC7EthIntfPmTCNum_Object = MibTableColumn
pxmTC7EthIntfPmTCNum = _PxmTC7EthIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 4),
    _PxmTC7EthIntfPmTCNum_Type()
)
pxmTC7EthIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmTCNum.setStatus("current")
_PxmTC7EthIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTC7EthIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC7EthIntfPmQueueingDiscardOctets = _PxmTC7EthIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 5),
    _PxmTC7EthIntfPmQueueingDiscardOctets_Type()
)
pxmTC7EthIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTC7EthIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTC7EthIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC7EthIntfPmQueueingDiscardPkts = _PxmTC7EthIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 6),
    _PxmTC7EthIntfPmQueueingDiscardPkts_Type()
)
pxmTC7EthIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTC7EthIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTC7EthIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC7EthIntfPmRandomGreenDropPkts = _PxmTC7EthIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 7),
    _PxmTC7EthIntfPmRandomGreenDropPkts_Type()
)
pxmTC7EthIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTC7EthIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTC7EthIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC7EthIntfPmRandomGreenDropOctets = _PxmTC7EthIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 8),
    _PxmTC7EthIntfPmRandomGreenDropOctets_Type()
)
pxmTC7EthIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTC7EthIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTC7EthIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC7EthIntfPmRandomYellowDropPkts = _PxmTC7EthIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 9),
    _PxmTC7EthIntfPmRandomYellowDropPkts_Type()
)
pxmTC7EthIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTC7EthIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTC7EthIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC7EthIntfPmRandomYellowDropOctets = _PxmTC7EthIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 10),
    _PxmTC7EthIntfPmRandomYellowDropOctets_Type()
)
pxmTC7EthIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTC7EthIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTC7EthIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC7EthIntfPmQueueingTransmitPkts = _PxmTC7EthIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 11),
    _PxmTC7EthIntfPmQueueingTransmitPkts_Type()
)
pxmTC7EthIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTC7EthIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTC7EthIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC7EthIntfPmQueueingTransmitOctets = _PxmTC7EthIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 5, 1, 12),
    _PxmTC7EthIntfPmQueueingTransmitOctets_Type()
)
pxmTC7EthIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmQueueingTransmitOctets.setStatus("current")
_PxmTCANYEthIntfPmTable_Object = MibTable
pxmTCANYEthIntfPmTable = _PxmTCANYEthIntfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6)
)
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmTable.setStatus("current")
_PxmTCANYEthIntfPmEntry_Object = MibTableRow
pxmTCANYEthIntfPmEntry = _PxmTCANYEthIntfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1)
)
pxmTCANYEthIntfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmSampleDuration"),
    (0, "INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmEntry.setStatus("current")


class _PxmTCANYEthIntfPmTimestamp_Type(Integer32):
    """Custom type pxmTCANYEthIntfPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTCANYEthIntfPmTimestamp_Type.__name__ = "Integer32"
_PxmTCANYEthIntfPmTimestamp_Object = MibTableColumn
pxmTCANYEthIntfPmTimestamp = _PxmTCANYEthIntfPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 1),
    _PxmTCANYEthIntfPmTimestamp_Type()
)
pxmTCANYEthIntfPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmTimestamp.setStatus("current")


class _PxmTCANYEthIntfPmSampleDuration_Type(Integer32):
    """Custom type pxmTCANYEthIntfPmSampleDuration based on Integer32"""
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


_PxmTCANYEthIntfPmSampleDuration_Type.__name__ = "Integer32"
_PxmTCANYEthIntfPmSampleDuration_Object = MibTableColumn
pxmTCANYEthIntfPmSampleDuration = _PxmTCANYEthIntfPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 2),
    _PxmTCANYEthIntfPmSampleDuration_Type()
)
pxmTCANYEthIntfPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmSampleDuration.setStatus("current")
_PxmTCANYEthIntfPmValidity_Type = TruthValue
_PxmTCANYEthIntfPmValidity_Object = MibTableColumn
pxmTCANYEthIntfPmValidity = _PxmTCANYEthIntfPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 3),
    _PxmTCANYEthIntfPmValidity_Type()
)
pxmTCANYEthIntfPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmValidity.setStatus("current")
_PxmTCANYEthIntfPmTCNum_Type = Integer32
_PxmTCANYEthIntfPmTCNum_Object = MibTableColumn
pxmTCANYEthIntfPmTCNum = _PxmTCANYEthIntfPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 4),
    _PxmTCANYEthIntfPmTCNum_Type()
)
pxmTCANYEthIntfPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmTCNum.setStatus("current")
_PxmTCANYEthIntfPmQueueingDiscardOctets_Type = Counter64
_PxmTCANYEthIntfPmQueueingDiscardOctets_Object = MibTableColumn
pxmTCANYEthIntfPmQueueingDiscardOctets = _PxmTCANYEthIntfPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 5),
    _PxmTCANYEthIntfPmQueueingDiscardOctets_Type()
)
pxmTCANYEthIntfPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmQueueingDiscardOctets.setStatus("current")
_PxmTCANYEthIntfPmQueueingDiscardPkts_Type = Integer32
_PxmTCANYEthIntfPmQueueingDiscardPkts_Object = MibTableColumn
pxmTCANYEthIntfPmQueueingDiscardPkts = _PxmTCANYEthIntfPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 6),
    _PxmTCANYEthIntfPmQueueingDiscardPkts_Type()
)
pxmTCANYEthIntfPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmQueueingDiscardPkts.setStatus("current")
_PxmTCANYEthIntfPmRandomGreenDropPkts_Type = Counter64
_PxmTCANYEthIntfPmRandomGreenDropPkts_Object = MibTableColumn
pxmTCANYEthIntfPmRandomGreenDropPkts = _PxmTCANYEthIntfPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 7),
    _PxmTCANYEthIntfPmRandomGreenDropPkts_Type()
)
pxmTCANYEthIntfPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRandomGreenDropPkts.setStatus("current")
_PxmTCANYEthIntfPmRandomGreenDropOctets_Type = Counter64
_PxmTCANYEthIntfPmRandomGreenDropOctets_Object = MibTableColumn
pxmTCANYEthIntfPmRandomGreenDropOctets = _PxmTCANYEthIntfPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 8),
    _PxmTCANYEthIntfPmRandomGreenDropOctets_Type()
)
pxmTCANYEthIntfPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRandomGreenDropOctets.setStatus("current")
_PxmTCANYEthIntfPmRandomYellowDropPkts_Type = Counter64
_PxmTCANYEthIntfPmRandomYellowDropPkts_Object = MibTableColumn
pxmTCANYEthIntfPmRandomYellowDropPkts = _PxmTCANYEthIntfPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 9),
    _PxmTCANYEthIntfPmRandomYellowDropPkts_Type()
)
pxmTCANYEthIntfPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRandomYellowDropPkts.setStatus("current")
_PxmTCANYEthIntfPmRandomYellowDropOctets_Type = Counter64
_PxmTCANYEthIntfPmRandomYellowDropOctets_Object = MibTableColumn
pxmTCANYEthIntfPmRandomYellowDropOctets = _PxmTCANYEthIntfPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 10),
    _PxmTCANYEthIntfPmRandomYellowDropOctets_Type()
)
pxmTCANYEthIntfPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRandomYellowDropOctets.setStatus("current")
_PxmTCANYEthIntfPmQueueingTransmitPkts_Type = Counter64
_PxmTCANYEthIntfPmQueueingTransmitPkts_Object = MibTableColumn
pxmTCANYEthIntfPmQueueingTransmitPkts = _PxmTCANYEthIntfPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 11),
    _PxmTCANYEthIntfPmQueueingTransmitPkts_Type()
)
pxmTCANYEthIntfPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmQueueingTransmitPkts.setStatus("current")
_PxmTCANYEthIntfPmQueueingTransmitOctets_Type = Counter64
_PxmTCANYEthIntfPmQueueingTransmitOctets_Object = MibTableColumn
pxmTCANYEthIntfPmQueueingTransmitOctets = _PxmTCANYEthIntfPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 3, 2, 6, 1, 12),
    _PxmTCANYEthIntfPmQueueingTransmitOctets_Type()
)
pxmTCANYEthIntfPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmQueueingTransmitOctets.setStatus("current")
_PxmEthIntfPmConformance_ObjectIdentity = ObjectIdentity
pxmEthIntfPmConformance = _PxmEthIntfPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4)
)
_PxmEthIntfPmCompliances_ObjectIdentity = ObjectIdentity
pxmEthIntfPmCompliances = _PxmEthIntfPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 1)
)
_PxmEthIntfPmGroups_ObjectIdentity = ObjectIdentity
pxmEthIntfPmGroups = _PxmEthIntfPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2)
)

# Managed Objects groups

pxmEthIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 1)
)
pxmEthIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmValidity"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxPackets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxCrcAlignedErr"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxUndersized"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxOversized"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxUnicastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxBroadcastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxMulticastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxPktErrors"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxSize64"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxSize65to127"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxSize128to255"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxSize256to511"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxSize512to1023"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRxSize1024to1518"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmTxPackets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmTxOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmTxUnicastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmTxBroadcastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmTxMulticastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmTxPktErrors"))
)
if mibBuilder.loadTexts:
    pxmEthIntfPmGroup.setStatus("current")

pxmEthIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 2)
)
pxmEthIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxPackets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxCrcAlignedErr"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxUndersized"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxOversized"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxUnicastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxBroadcastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxMulticastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxPktErrors"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxSize64"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxSize65to127"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxSize128to255"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxSize256to511"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxSize512to1023"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxSize1024to1518"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealRxLU"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealTxPackets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealTxOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealTxUnicastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealTxBroadcastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealTxMulticastPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealTxPktErrors"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealTxLU"))
)
if mibBuilder.loadTexts:
    pxmEthIntfPmRealGroup.setStatus("current")

pxmBwpEthIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 3)
)
pxmBwpEthIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmTimestamp"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmSampleDuration"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmValidity"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmPolicerConformedPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmPolicerConformedOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmPolicerExceededPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmPolicerExceededOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmPolicerViolatedPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmPolicerViolatedOctets"))
)
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmGroup.setStatus("current")

pxmBwpEthIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 4)
)
pxmBwpEthIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmRealPolicerConformedPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmRealPolicerConformedOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmRealPolicerExceededPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmRealPolicerExceededOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmRealPolicerViolatedPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmBwpEthIntfPmRealPolicerViolatedOctets"))
)
if mibBuilder.loadTexts:
    pxmBwpEthIntfPmRealGroup.setStatus("current")

pxmTC0EthIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 5)
)
pxmTC0EthIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmRealGroup.setStatus("current")

pxmTC0EthIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 6)
)
pxmTC0EthIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmValidity"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC0EthIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC0EthIntfPmGroup.setStatus("current")

pxmTC2EthIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 7)
)
pxmTC2EthIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmRealGroup.setStatus("current")

pxmTC2EthIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 8)
)
pxmTC2EthIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmValidity"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC2EthIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC2EthIntfPmGroup.setStatus("current")

pxmTC4EthIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 9)
)
pxmTC4EthIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmRealGroup.setStatus("current")

pxmTC4EthIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 10)
)
pxmTC4EthIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmValidity"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC4EthIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC4EthIntfPmGroup.setStatus("current")

pxmTC6EthIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 11)
)
pxmTC6EthIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmRealGroup.setStatus("current")

pxmTC6EthIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 12)
)
pxmTC6EthIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmValidity"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC6EthIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC6EthIntfPmGroup.setStatus("current")

pxmTC7EthIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 13)
)
pxmTC7EthIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmRealGroup.setStatus("current")

pxmTC7EthIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 14)
)
pxmTC7EthIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmValidity"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTC7EthIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC7EthIntfPmGroup.setStatus("current")

pxmTCANYEthIntfPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 15)
)
pxmTCANYEthIntfPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmRealGroup.setStatus("current")

pxmTCANYEthIntfPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 2, 16)
)
pxmTCANYEthIntfPmGroup.setObjects(
      *(("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmValidity"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmTCNum"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMETHINTF-MIB", "pxmTCANYEthIntfPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTCANYEthIntfPmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmEthIntfPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 1, 1)
)
pxmEthIntfPmCompliance.setObjects(
    ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmGroup")
)
if mibBuilder.loadTexts:
    pxmEthIntfPmCompliance.setStatus(
        "current"
    )

pxmEthIntfPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 97, 4, 1, 2)
)
pxmEthIntfPmRealCompliance.setObjects(
    ("INFINERA-PM-PXMETHINTF-MIB", "pxmEthIntfPmRealGroup")
)
if mibBuilder.loadTexts:
    pxmEthIntfPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-PXMETHINTF-MIB",
    **{"pxmEthIntfPmMIB": pxmEthIntfPmMIB,
       "pxmEthIntfRmonPm": pxmEthIntfRmonPm,
       "pxmEthIntfPmRealTable": pxmEthIntfPmRealTable,
       "pxmEthIntfPmRealEntry": pxmEthIntfPmRealEntry,
       "pxmEthIntfPmRealRxPackets": pxmEthIntfPmRealRxPackets,
       "pxmEthIntfPmRealRxOctets": pxmEthIntfPmRealRxOctets,
       "pxmEthIntfPmRealRxCrcAlignedErr": pxmEthIntfPmRealRxCrcAlignedErr,
       "pxmEthIntfPmRealRxUndersized": pxmEthIntfPmRealRxUndersized,
       "pxmEthIntfPmRealRxOversized": pxmEthIntfPmRealRxOversized,
       "pxmEthIntfPmRealRxUnicastPkts": pxmEthIntfPmRealRxUnicastPkts,
       "pxmEthIntfPmRealRxBroadcastPkts": pxmEthIntfPmRealRxBroadcastPkts,
       "pxmEthIntfPmRealRxMulticastPkts": pxmEthIntfPmRealRxMulticastPkts,
       "pxmEthIntfPmRealRxPktErrors": pxmEthIntfPmRealRxPktErrors,
       "pxmEthIntfPmRealRxSize64": pxmEthIntfPmRealRxSize64,
       "pxmEthIntfPmRealRxSize65to127": pxmEthIntfPmRealRxSize65to127,
       "pxmEthIntfPmRealRxSize128to255": pxmEthIntfPmRealRxSize128to255,
       "pxmEthIntfPmRealRxSize256to511": pxmEthIntfPmRealRxSize256to511,
       "pxmEthIntfPmRealRxSize512to1023": pxmEthIntfPmRealRxSize512to1023,
       "pxmEthIntfPmRealRxSize1024to1518": pxmEthIntfPmRealRxSize1024to1518,
       "pxmEthIntfPmRealRxLU": pxmEthIntfPmRealRxLU,
       "pxmEthIntfPmRealTxPackets": pxmEthIntfPmRealTxPackets,
       "pxmEthIntfPmRealTxOctets": pxmEthIntfPmRealTxOctets,
       "pxmEthIntfPmRealTxUnicastPkts": pxmEthIntfPmRealTxUnicastPkts,
       "pxmEthIntfPmRealTxBroadcastPkts": pxmEthIntfPmRealTxBroadcastPkts,
       "pxmEthIntfPmRealTxMulticastPkts": pxmEthIntfPmRealTxMulticastPkts,
       "pxmEthIntfPmRealTxPktErrors": pxmEthIntfPmRealTxPktErrors,
       "pxmEthIntfPmRealTxLU": pxmEthIntfPmRealTxLU,
       "pxmEthIntfPmTable": pxmEthIntfPmTable,
       "pxmEthIntfPmEntry": pxmEthIntfPmEntry,
       "pxmEthIntfPmTimestamp": pxmEthIntfPmTimestamp,
       "pxmEthIntfPmSampleDuration": pxmEthIntfPmSampleDuration,
       "pxmEthIntfPmValidity": pxmEthIntfPmValidity,
       "pxmEthIntfPmRxPackets": pxmEthIntfPmRxPackets,
       "pxmEthIntfPmRxOctets": pxmEthIntfPmRxOctets,
       "pxmEthIntfPmRxCrcAlignedErr": pxmEthIntfPmRxCrcAlignedErr,
       "pxmEthIntfPmRxUndersized": pxmEthIntfPmRxUndersized,
       "pxmEthIntfPmRxOversized": pxmEthIntfPmRxOversized,
       "pxmEthIntfPmRxUnicastPkts": pxmEthIntfPmRxUnicastPkts,
       "pxmEthIntfPmRxBroadcastPkts": pxmEthIntfPmRxBroadcastPkts,
       "pxmEthIntfPmRxMulticastPkts": pxmEthIntfPmRxMulticastPkts,
       "pxmEthIntfPmRxPktErrors": pxmEthIntfPmRxPktErrors,
       "pxmEthIntfPmRxSize64": pxmEthIntfPmRxSize64,
       "pxmEthIntfPmRxSize65to127": pxmEthIntfPmRxSize65to127,
       "pxmEthIntfPmRxSize128to255": pxmEthIntfPmRxSize128to255,
       "pxmEthIntfPmRxSize256to511": pxmEthIntfPmRxSize256to511,
       "pxmEthIntfPmRxSize512to1023": pxmEthIntfPmRxSize512to1023,
       "pxmEthIntfPmRxSize1024to1518": pxmEthIntfPmRxSize1024to1518,
       "pxmEthIntfPmTxPackets": pxmEthIntfPmTxPackets,
       "pxmEthIntfPmTxOctets": pxmEthIntfPmTxOctets,
       "pxmEthIntfPmTxUnicastPkts": pxmEthIntfPmTxUnicastPkts,
       "pxmEthIntfPmTxBroadcastPkts": pxmEthIntfPmTxBroadcastPkts,
       "pxmEthIntfPmTxMulticastPkts": pxmEthIntfPmTxMulticastPkts,
       "pxmEthIntfPmTxPktErrors": pxmEthIntfPmTxPktErrors,
       "pxmEthIntfBwpPm": pxmEthIntfBwpPm,
       "pxmBwpEthIntfPmRealTable": pxmBwpEthIntfPmRealTable,
       "pxmBwpEthIntfPmRealEntry": pxmBwpEthIntfPmRealEntry,
       "pxmBwpEthIntfPmRealPolicerConformedPkts": pxmBwpEthIntfPmRealPolicerConformedPkts,
       "pxmBwpEthIntfPmRealPolicerConformedOctets": pxmBwpEthIntfPmRealPolicerConformedOctets,
       "pxmBwpEthIntfPmRealPolicerExceededPkts": pxmBwpEthIntfPmRealPolicerExceededPkts,
       "pxmBwpEthIntfPmRealPolicerExceededOctets": pxmBwpEthIntfPmRealPolicerExceededOctets,
       "pxmBwpEthIntfPmRealPolicerViolatedPkts": pxmBwpEthIntfPmRealPolicerViolatedPkts,
       "pxmBwpEthIntfPmRealPolicerViolatedOctets": pxmBwpEthIntfPmRealPolicerViolatedOctets,
       "pxmBwpEthIntfPmTable": pxmBwpEthIntfPmTable,
       "pxmBwpEthIntfPmEntry": pxmBwpEthIntfPmEntry,
       "pxmBwpEthIntfPmTimestamp": pxmBwpEthIntfPmTimestamp,
       "pxmBwpEthIntfPmSampleDuration": pxmBwpEthIntfPmSampleDuration,
       "pxmBwpEthIntfPmValidity": pxmBwpEthIntfPmValidity,
       "pxmBwpEthIntfPmPolicerConformedPkts": pxmBwpEthIntfPmPolicerConformedPkts,
       "pxmBwpEthIntfPmPolicerConformedOctets": pxmBwpEthIntfPmPolicerConformedOctets,
       "pxmBwpEthIntfPmPolicerExceededPkts": pxmBwpEthIntfPmPolicerExceededPkts,
       "pxmBwpEthIntfPmPolicerExceededOctets": pxmBwpEthIntfPmPolicerExceededOctets,
       "pxmBwpEthIntfPmPolicerViolatedPkts": pxmBwpEthIntfPmPolicerViolatedPkts,
       "pxmBwpEthIntfPmPolicerViolatedOctets": pxmBwpEthIntfPmPolicerViolatedOctets,
       "pxmCmEthIntfPmObjects": pxmCmEthIntfPmObjects,
       "pxmCmEthIntfRealPm": pxmCmEthIntfRealPm,
       "pxmTC0EthIntfPmRealTable": pxmTC0EthIntfPmRealTable,
       "pxmTC0EthIntfPmRealEntry": pxmTC0EthIntfPmRealEntry,
       "pxmTC0EthIntfPmRealTCNum": pxmTC0EthIntfPmRealTCNum,
       "pxmTC0EthIntfPmRealTDQueuingCurrentQDepth": pxmTC0EthIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC0EthIntfPmRealQueueingDiscardOctets": pxmTC0EthIntfPmRealQueueingDiscardOctets,
       "pxmTC0EthIntfPmRealQueueingDiscardPkts": pxmTC0EthIntfPmRealQueueingDiscardPkts,
       "pxmTC0EthIntfPmRealRandomGreenDropPkts": pxmTC0EthIntfPmRealRandomGreenDropPkts,
       "pxmTC0EthIntfPmRealRandomGreenDropOctets": pxmTC0EthIntfPmRealRandomGreenDropOctets,
       "pxmTC0EthIntfPmRealRandomYellowDropPkts": pxmTC0EthIntfPmRealRandomYellowDropPkts,
       "pxmTC0EthIntfPmRealRandomYellowDropOctets": pxmTC0EthIntfPmRealRandomYellowDropOctets,
       "pxmTC0EthIntfPmRealQueueingTransmitPkts": pxmTC0EthIntfPmRealQueueingTransmitPkts,
       "pxmTC0EthIntfPmRealQueueingTransmitOctets": pxmTC0EthIntfPmRealQueueingTransmitOctets,
       "pxmTC0EthIntfPmRealQueueingMeanQSizeUnit": pxmTC0EthIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC0EthIntfPmRealMeanQSize": pxmTC0EthIntfPmRealMeanQSize,
       "pxmTC2EthIntfPmRealTable": pxmTC2EthIntfPmRealTable,
       "pxmTC2EthIntfPmRealEntry": pxmTC2EthIntfPmRealEntry,
       "pxmTC2EthIntfPmRealTCNum": pxmTC2EthIntfPmRealTCNum,
       "pxmTC2EthIntfPmRealTDQueuingCurrentQDepth": pxmTC2EthIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC2EthIntfPmRealQueueingDiscardOctets": pxmTC2EthIntfPmRealQueueingDiscardOctets,
       "pxmTC2EthIntfPmRealQueueingDiscardPkts": pxmTC2EthIntfPmRealQueueingDiscardPkts,
       "pxmTC2EthIntfPmRealRandomGreenDropPkts": pxmTC2EthIntfPmRealRandomGreenDropPkts,
       "pxmTC2EthIntfPmRealRandomGreenDropOctets": pxmTC2EthIntfPmRealRandomGreenDropOctets,
       "pxmTC2EthIntfPmRealRandomYellowDropPkts": pxmTC2EthIntfPmRealRandomYellowDropPkts,
       "pxmTC2EthIntfPmRealRandomYellowDropOctets": pxmTC2EthIntfPmRealRandomYellowDropOctets,
       "pxmTC2EthIntfPmRealQueueingTransmitPkts": pxmTC2EthIntfPmRealQueueingTransmitPkts,
       "pxmTC2EthIntfPmRealQueueingTransmitOctets": pxmTC2EthIntfPmRealQueueingTransmitOctets,
       "pxmTC2EthIntfPmRealQueueingMeanQSizeUnit": pxmTC2EthIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC2EthIntfPmRealMeanQSize": pxmTC2EthIntfPmRealMeanQSize,
       "pxmTC4EthIntfPmRealTable": pxmTC4EthIntfPmRealTable,
       "pxmTC4EthIntfPmRealEntry": pxmTC4EthIntfPmRealEntry,
       "pxmTC4EthIntfPmRealTCNum": pxmTC4EthIntfPmRealTCNum,
       "pxmTC4EthIntfPmRealTDQueuingCurrentQDepth": pxmTC4EthIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC4EthIntfPmRealQueueingDiscardOctets": pxmTC4EthIntfPmRealQueueingDiscardOctets,
       "pxmTC4EthIntfPmRealQueueingDiscardPkts": pxmTC4EthIntfPmRealQueueingDiscardPkts,
       "pxmTC4EthIntfPmRealRandomGreenDropPkts": pxmTC4EthIntfPmRealRandomGreenDropPkts,
       "pxmTC4EthIntfPmRealRandomGreenDropOctets": pxmTC4EthIntfPmRealRandomGreenDropOctets,
       "pxmTC4EthIntfPmRealRandomYellowDropPkts": pxmTC4EthIntfPmRealRandomYellowDropPkts,
       "pxmTC4EthIntfPmRealRandomYellowDropOctets": pxmTC4EthIntfPmRealRandomYellowDropOctets,
       "pxmTC4EthIntfPmRealQueueingTransmitPkts": pxmTC4EthIntfPmRealQueueingTransmitPkts,
       "pxmTC4EthIntfPmRealQueueingTransmitOctets": pxmTC4EthIntfPmRealQueueingTransmitOctets,
       "pxmTC4EthIntfPmRealQueueingMeanQSizeUnit": pxmTC4EthIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC4EthIntfPmRealMeanQSize": pxmTC4EthIntfPmRealMeanQSize,
       "pxmTC6EthIntfPmRealTable": pxmTC6EthIntfPmRealTable,
       "pxmTC6EthIntfPmRealEntry": pxmTC6EthIntfPmRealEntry,
       "pxmTC6EthIntfPmRealTCNum": pxmTC6EthIntfPmRealTCNum,
       "pxmTC6EthIntfPmRealTDQueuingCurrentQDepth": pxmTC6EthIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC6EthIntfPmRealQueueingDiscardOctets": pxmTC6EthIntfPmRealQueueingDiscardOctets,
       "pxmTC6EthIntfPmRealQueueingDiscardPkts": pxmTC6EthIntfPmRealQueueingDiscardPkts,
       "pxmTC6EthIntfPmRealRandomGreenDropPkts": pxmTC6EthIntfPmRealRandomGreenDropPkts,
       "pxmTC6EthIntfPmRealRandomGreenDropOctets": pxmTC6EthIntfPmRealRandomGreenDropOctets,
       "pxmTC6EthIntfPmRealRandomYellowDropPkts": pxmTC6EthIntfPmRealRandomYellowDropPkts,
       "pxmTC6EthIntfPmRealRandomYellowDropOctets": pxmTC6EthIntfPmRealRandomYellowDropOctets,
       "pxmTC6EthIntfPmRealQueueingTransmitPkts": pxmTC6EthIntfPmRealQueueingTransmitPkts,
       "pxmTC6EthIntfPmRealQueueingTransmitOctets": pxmTC6EthIntfPmRealQueueingTransmitOctets,
       "pxmTC6EthIntfPmRealQueueingMeanQSizeUnit": pxmTC6EthIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC6EthIntfPmRealMeanQSize": pxmTC6EthIntfPmRealMeanQSize,
       "pxmTC7EthIntfPmRealTable": pxmTC7EthIntfPmRealTable,
       "pxmTC7EthIntfPmRealEntry": pxmTC7EthIntfPmRealEntry,
       "pxmTC7EthIntfPmRealTCNum": pxmTC7EthIntfPmRealTCNum,
       "pxmTC7EthIntfPmRealTDQueuingCurrentQDepth": pxmTC7EthIntfPmRealTDQueuingCurrentQDepth,
       "pxmTC7EthIntfPmRealQueueingDiscardOctets": pxmTC7EthIntfPmRealQueueingDiscardOctets,
       "pxmTC7EthIntfPmRealQueueingDiscardPkts": pxmTC7EthIntfPmRealQueueingDiscardPkts,
       "pxmTC7EthIntfPmRealRandomGreenDropPkts": pxmTC7EthIntfPmRealRandomGreenDropPkts,
       "pxmTC7EthIntfPmRealRandomGreenDropOctets": pxmTC7EthIntfPmRealRandomGreenDropOctets,
       "pxmTC7EthIntfPmRealRandomYellowDropPkts": pxmTC7EthIntfPmRealRandomYellowDropPkts,
       "pxmTC7EthIntfPmRealRandomYellowDropOctets": pxmTC7EthIntfPmRealRandomYellowDropOctets,
       "pxmTC7EthIntfPmRealQueueingTransmitPkts": pxmTC7EthIntfPmRealQueueingTransmitPkts,
       "pxmTC7EthIntfPmRealQueueingTransmitOctets": pxmTC7EthIntfPmRealQueueingTransmitOctets,
       "pxmTC7EthIntfPmRealQueueingMeanQSizeUnit": pxmTC7EthIntfPmRealQueueingMeanQSizeUnit,
       "pxmTC7EthIntfPmRealMeanQSize": pxmTC7EthIntfPmRealMeanQSize,
       "pxmTCANYEthIntfPmRealTable": pxmTCANYEthIntfPmRealTable,
       "pxmTCANYEthIntfPmRealEntry": pxmTCANYEthIntfPmRealEntry,
       "pxmTCANYEthIntfPmRealTCNum": pxmTCANYEthIntfPmRealTCNum,
       "pxmTCANYEthIntfPmRealTDQueuingCurrentQDepth": pxmTCANYEthIntfPmRealTDQueuingCurrentQDepth,
       "pxmTCANYEthIntfPmRealQueueingDiscardOctets": pxmTCANYEthIntfPmRealQueueingDiscardOctets,
       "pxmTCANYEthIntfPmRealQueueingDiscardPkts": pxmTCANYEthIntfPmRealQueueingDiscardPkts,
       "pxmTCANYEthIntfPmRealRandomGreenDropPkts": pxmTCANYEthIntfPmRealRandomGreenDropPkts,
       "pxmTCANYEthIntfPmRealRandomGreenDropOctets": pxmTCANYEthIntfPmRealRandomGreenDropOctets,
       "pxmTCANYEthIntfPmRealRandomYellowDropPkts": pxmTCANYEthIntfPmRealRandomYellowDropPkts,
       "pxmTCANYEthIntfPmRealRandomYellowDropOctets": pxmTCANYEthIntfPmRealRandomYellowDropOctets,
       "pxmTCANYEthIntfPmRealQueueingTransmitPkts": pxmTCANYEthIntfPmRealQueueingTransmitPkts,
       "pxmTCANYEthIntfPmRealQueueingTransmitOctets": pxmTCANYEthIntfPmRealQueueingTransmitOctets,
       "pxmTCANYEthIntfPmRealQueueingMeanQSizeUnit": pxmTCANYEthIntfPmRealQueueingMeanQSizeUnit,
       "pxmTCANYEthIntfPmRealMeanQSize": pxmTCANYEthIntfPmRealMeanQSize,
       "pxmCmEthIntfPm": pxmCmEthIntfPm,
       "pxmTC0EthIntfPmTable": pxmTC0EthIntfPmTable,
       "pxmTC0EthIntfPmEntry": pxmTC0EthIntfPmEntry,
       "pxmTC0EthIntfPmTimestamp": pxmTC0EthIntfPmTimestamp,
       "pxmTC0EthIntfPmSampleDuration": pxmTC0EthIntfPmSampleDuration,
       "pxmTC0EthIntfPmValidity": pxmTC0EthIntfPmValidity,
       "pxmTC0EthIntfPmTCNum": pxmTC0EthIntfPmTCNum,
       "pxmTC0EthIntfPmQueueingDiscardOctets": pxmTC0EthIntfPmQueueingDiscardOctets,
       "pxmTC0EthIntfPmQueueingDiscardPkts": pxmTC0EthIntfPmQueueingDiscardPkts,
       "pxmTC0EthIntfPmRandomGreenDropPkts": pxmTC0EthIntfPmRandomGreenDropPkts,
       "pxmTC0EthIntfPmRandomGreenDropOctets": pxmTC0EthIntfPmRandomGreenDropOctets,
       "pxmTC0EthIntfPmRandomYellowDropPkts": pxmTC0EthIntfPmRandomYellowDropPkts,
       "pxmTC0EthIntfPmRandomYellowDropOctets": pxmTC0EthIntfPmRandomYellowDropOctets,
       "pxmTC0EthIntfPmQueueingTransmitPkts": pxmTC0EthIntfPmQueueingTransmitPkts,
       "pxmTC0EthIntfPmQueueingTransmitOctets": pxmTC0EthIntfPmQueueingTransmitOctets,
       "pxmTC2EthIntfPmTable": pxmTC2EthIntfPmTable,
       "pxmTC2EthIntfPmEntry": pxmTC2EthIntfPmEntry,
       "pxmTC2EthIntfPmTimestamp": pxmTC2EthIntfPmTimestamp,
       "pxmTC2EthIntfPmSampleDuration": pxmTC2EthIntfPmSampleDuration,
       "pxmTC2EthIntfPmValidity": pxmTC2EthIntfPmValidity,
       "pxmTC2EthIntfPmTCNum": pxmTC2EthIntfPmTCNum,
       "pxmTC2EthIntfPmQueueingDiscardOctets": pxmTC2EthIntfPmQueueingDiscardOctets,
       "pxmTC2EthIntfPmQueueingDiscardPkts": pxmTC2EthIntfPmQueueingDiscardPkts,
       "pxmTC2EthIntfPmRandomGreenDropPkts": pxmTC2EthIntfPmRandomGreenDropPkts,
       "pxmTC2EthIntfPmRandomGreenDropOctets": pxmTC2EthIntfPmRandomGreenDropOctets,
       "pxmTC2EthIntfPmRandomYellowDropPkts": pxmTC2EthIntfPmRandomYellowDropPkts,
       "pxmTC2EthIntfPmRandomYellowDropOctets": pxmTC2EthIntfPmRandomYellowDropOctets,
       "pxmTC2EthIntfPmQueueingTransmitPkts": pxmTC2EthIntfPmQueueingTransmitPkts,
       "pxmTC2EthIntfPmQueueingTransmitOctets": pxmTC2EthIntfPmQueueingTransmitOctets,
       "pxmTC4EthIntfPmTable": pxmTC4EthIntfPmTable,
       "pxmTC4EthIntfPmEntry": pxmTC4EthIntfPmEntry,
       "pxmTC4EthIntfPmTimestamp": pxmTC4EthIntfPmTimestamp,
       "pxmTC4EthIntfPmSampleDuration": pxmTC4EthIntfPmSampleDuration,
       "pxmTC4EthIntfPmValidity": pxmTC4EthIntfPmValidity,
       "pxmTC4EthIntfPmTCNum": pxmTC4EthIntfPmTCNum,
       "pxmTC4EthIntfPmQueueingDiscardOctets": pxmTC4EthIntfPmQueueingDiscardOctets,
       "pxmTC4EthIntfPmQueueingDiscardPkts": pxmTC4EthIntfPmQueueingDiscardPkts,
       "pxmTC4EthIntfPmRandomGreenDropPkts": pxmTC4EthIntfPmRandomGreenDropPkts,
       "pxmTC4EthIntfPmRandomGreenDropOctets": pxmTC4EthIntfPmRandomGreenDropOctets,
       "pxmTC4EthIntfPmRandomYellowDropPkts": pxmTC4EthIntfPmRandomYellowDropPkts,
       "pxmTC4EthIntfPmRandomYellowDropOctets": pxmTC4EthIntfPmRandomYellowDropOctets,
       "pxmTC4EthIntfPmQueueingTransmitPkts": pxmTC4EthIntfPmQueueingTransmitPkts,
       "pxmTC4EthIntfPmQueueingTransmitOctets": pxmTC4EthIntfPmQueueingTransmitOctets,
       "pxmTC6EthIntfPmTable": pxmTC6EthIntfPmTable,
       "pxmTC6EthIntfPmEntry": pxmTC6EthIntfPmEntry,
       "pxmTC6EthIntfPmTimestamp": pxmTC6EthIntfPmTimestamp,
       "pxmTC6EthIntfPmSampleDuration": pxmTC6EthIntfPmSampleDuration,
       "pxmTC6EthIntfPmValidity": pxmTC6EthIntfPmValidity,
       "pxmTC6EthIntfPmTCNum": pxmTC6EthIntfPmTCNum,
       "pxmTC6EthIntfPmQueueingDiscardOctets": pxmTC6EthIntfPmQueueingDiscardOctets,
       "pxmTC6EthIntfPmQueueingDiscardPkts": pxmTC6EthIntfPmQueueingDiscardPkts,
       "pxmTC6EthIntfPmRandomGreenDropPkts": pxmTC6EthIntfPmRandomGreenDropPkts,
       "pxmTC6EthIntfPmRandomGreenDropOctets": pxmTC6EthIntfPmRandomGreenDropOctets,
       "pxmTC6EthIntfPmRandomYellowDropPkts": pxmTC6EthIntfPmRandomYellowDropPkts,
       "pxmTC6EthIntfPmRandomYellowDropOctets": pxmTC6EthIntfPmRandomYellowDropOctets,
       "pxmTC6EthIntfPmQueueingTransmitPkts": pxmTC6EthIntfPmQueueingTransmitPkts,
       "pxmTC6EthIntfPmQueueingTransmitOctets": pxmTC6EthIntfPmQueueingTransmitOctets,
       "pxmTC7EthIntfPmTable": pxmTC7EthIntfPmTable,
       "pxmTC7EthIntfPmEntry": pxmTC7EthIntfPmEntry,
       "pxmTC7EthIntfPmTimestamp": pxmTC7EthIntfPmTimestamp,
       "pxmTC7EthIntfPmSampleDuration": pxmTC7EthIntfPmSampleDuration,
       "pxmTC7EthIntfPmValidity": pxmTC7EthIntfPmValidity,
       "pxmTC7EthIntfPmTCNum": pxmTC7EthIntfPmTCNum,
       "pxmTC7EthIntfPmQueueingDiscardOctets": pxmTC7EthIntfPmQueueingDiscardOctets,
       "pxmTC7EthIntfPmQueueingDiscardPkts": pxmTC7EthIntfPmQueueingDiscardPkts,
       "pxmTC7EthIntfPmRandomGreenDropPkts": pxmTC7EthIntfPmRandomGreenDropPkts,
       "pxmTC7EthIntfPmRandomGreenDropOctets": pxmTC7EthIntfPmRandomGreenDropOctets,
       "pxmTC7EthIntfPmRandomYellowDropPkts": pxmTC7EthIntfPmRandomYellowDropPkts,
       "pxmTC7EthIntfPmRandomYellowDropOctets": pxmTC7EthIntfPmRandomYellowDropOctets,
       "pxmTC7EthIntfPmQueueingTransmitPkts": pxmTC7EthIntfPmQueueingTransmitPkts,
       "pxmTC7EthIntfPmQueueingTransmitOctets": pxmTC7EthIntfPmQueueingTransmitOctets,
       "pxmTCANYEthIntfPmTable": pxmTCANYEthIntfPmTable,
       "pxmTCANYEthIntfPmEntry": pxmTCANYEthIntfPmEntry,
       "pxmTCANYEthIntfPmTimestamp": pxmTCANYEthIntfPmTimestamp,
       "pxmTCANYEthIntfPmSampleDuration": pxmTCANYEthIntfPmSampleDuration,
       "pxmTCANYEthIntfPmValidity": pxmTCANYEthIntfPmValidity,
       "pxmTCANYEthIntfPmTCNum": pxmTCANYEthIntfPmTCNum,
       "pxmTCANYEthIntfPmQueueingDiscardOctets": pxmTCANYEthIntfPmQueueingDiscardOctets,
       "pxmTCANYEthIntfPmQueueingDiscardPkts": pxmTCANYEthIntfPmQueueingDiscardPkts,
       "pxmTCANYEthIntfPmRandomGreenDropPkts": pxmTCANYEthIntfPmRandomGreenDropPkts,
       "pxmTCANYEthIntfPmRandomGreenDropOctets": pxmTCANYEthIntfPmRandomGreenDropOctets,
       "pxmTCANYEthIntfPmRandomYellowDropPkts": pxmTCANYEthIntfPmRandomYellowDropPkts,
       "pxmTCANYEthIntfPmRandomYellowDropOctets": pxmTCANYEthIntfPmRandomYellowDropOctets,
       "pxmTCANYEthIntfPmQueueingTransmitPkts": pxmTCANYEthIntfPmQueueingTransmitPkts,
       "pxmTCANYEthIntfPmQueueingTransmitOctets": pxmTCANYEthIntfPmQueueingTransmitOctets,
       "pxmEthIntfPmConformance": pxmEthIntfPmConformance,
       "pxmEthIntfPmCompliances": pxmEthIntfPmCompliances,
       "pxmEthIntfPmCompliance": pxmEthIntfPmCompliance,
       "pxmEthIntfPmRealCompliance": pxmEthIntfPmRealCompliance,
       "pxmEthIntfPmGroups": pxmEthIntfPmGroups,
       "pxmEthIntfPmGroup": pxmEthIntfPmGroup,
       "pxmEthIntfPmRealGroup": pxmEthIntfPmRealGroup,
       "pxmBwpEthIntfPmGroup": pxmBwpEthIntfPmGroup,
       "pxmBwpEthIntfPmRealGroup": pxmBwpEthIntfPmRealGroup,
       "pxmTC0EthIntfPmRealGroup": pxmTC0EthIntfPmRealGroup,
       "pxmTC0EthIntfPmGroup": pxmTC0EthIntfPmGroup,
       "pxmTC2EthIntfPmRealGroup": pxmTC2EthIntfPmRealGroup,
       "pxmTC2EthIntfPmGroup": pxmTC2EthIntfPmGroup,
       "pxmTC4EthIntfPmRealGroup": pxmTC4EthIntfPmRealGroup,
       "pxmTC4EthIntfPmGroup": pxmTC4EthIntfPmGroup,
       "pxmTC6EthIntfPmRealGroup": pxmTC6EthIntfPmRealGroup,
       "pxmTC6EthIntfPmGroup": pxmTC6EthIntfPmGroup,
       "pxmTC7EthIntfPmRealGroup": pxmTC7EthIntfPmRealGroup,
       "pxmTC7EthIntfPmGroup": pxmTC7EthIntfPmGroup,
       "pxmTCANYEthIntfPmRealGroup": pxmTCANYEthIntfPmRealGroup,
       "pxmTCANYEthIntfPmGroup": pxmTCANYEthIntfPmGroup}
)
