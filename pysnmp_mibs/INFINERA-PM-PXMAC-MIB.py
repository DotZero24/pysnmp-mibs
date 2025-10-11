# SNMP MIB module (INFINERA-PM-PXMAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-PXMAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:16 2025
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

pxmAcPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95)
)
if mibBuilder.loadTexts:
    pxmAcPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmAcRmonPm_ObjectIdentity = ObjectIdentity
pxmAcRmonPm = _PxmAcRmonPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1)
)
_PxmAcPmRealTable_Object = MibTable
pxmAcPmRealTable = _PxmAcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 1)
)
if mibBuilder.loadTexts:
    pxmAcPmRealTable.setStatus("current")
_PxmAcPmRealEntry_Object = MibTableRow
pxmAcPmRealEntry = _PxmAcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 1, 1)
)
pxmAcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmAcPmRealEntry.setStatus("current")
_PxmAcPmRealRxPackets_Type = Counter64
_PxmAcPmRealRxPackets_Object = MibTableColumn
pxmAcPmRealRxPackets = _PxmAcPmRealRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 1, 1, 1),
    _PxmAcPmRealRxPackets_Type()
)
pxmAcPmRealRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmRealRxPackets.setStatus("current")
_PxmAcPmRealRxOctets_Type = Counter64
_PxmAcPmRealRxOctets_Object = MibTableColumn
pxmAcPmRealRxOctets = _PxmAcPmRealRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 1, 1, 2),
    _PxmAcPmRealRxOctets_Type()
)
pxmAcPmRealRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmRealRxOctets.setStatus("current")
_PxmAcPmRealTxPackets_Type = Counter64
_PxmAcPmRealTxPackets_Object = MibTableColumn
pxmAcPmRealTxPackets = _PxmAcPmRealTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 1, 1, 3),
    _PxmAcPmRealTxPackets_Type()
)
pxmAcPmRealTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmRealTxPackets.setStatus("current")
_PxmAcPmRealTxOctets_Type = Counter64
_PxmAcPmRealTxOctets_Object = MibTableColumn
pxmAcPmRealTxOctets = _PxmAcPmRealTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 1, 1, 4),
    _PxmAcPmRealTxOctets_Type()
)
pxmAcPmRealTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmRealTxOctets.setStatus("current")
_PxmAcPmTable_Object = MibTable
pxmAcPmTable = _PxmAcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2)
)
if mibBuilder.loadTexts:
    pxmAcPmTable.setStatus("current")
_PxmAcPmEntry_Object = MibTableRow
pxmAcPmEntry = _PxmAcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2, 1)
)
pxmAcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmAcPmSampleDuration"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmAcPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmAcPmEntry.setStatus("current")


class _PxmAcPmTimestamp_Type(Integer32):
    """Custom type pxmAcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmAcPmTimestamp_Type.__name__ = "Integer32"
_PxmAcPmTimestamp_Object = MibTableColumn
pxmAcPmTimestamp = _PxmAcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2, 1, 1),
    _PxmAcPmTimestamp_Type()
)
pxmAcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmAcPmTimestamp.setStatus("current")


class _PxmAcPmSampleDuration_Type(Integer32):
    """Custom type pxmAcPmSampleDuration based on Integer32"""
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


_PxmAcPmSampleDuration_Type.__name__ = "Integer32"
_PxmAcPmSampleDuration_Object = MibTableColumn
pxmAcPmSampleDuration = _PxmAcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2, 1, 2),
    _PxmAcPmSampleDuration_Type()
)
pxmAcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmAcPmSampleDuration.setStatus("current")
_PxmAcPmValidity_Type = TruthValue
_PxmAcPmValidity_Object = MibTableColumn
pxmAcPmValidity = _PxmAcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2, 1, 3),
    _PxmAcPmValidity_Type()
)
pxmAcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmValidity.setStatus("current")
_PxmAcPmRxPackets_Type = HCPerfIntervalCount
_PxmAcPmRxPackets_Object = MibTableColumn
pxmAcPmRxPackets = _PxmAcPmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2, 1, 4),
    _PxmAcPmRxPackets_Type()
)
pxmAcPmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmRxPackets.setStatus("current")
_PxmAcPmRxOctets_Type = HCPerfIntervalCount
_PxmAcPmRxOctets_Object = MibTableColumn
pxmAcPmRxOctets = _PxmAcPmRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2, 1, 5),
    _PxmAcPmRxOctets_Type()
)
pxmAcPmRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmRxOctets.setStatus("current")
_PxmAcPmTxPackets_Type = HCPerfIntervalCount
_PxmAcPmTxPackets_Object = MibTableColumn
pxmAcPmTxPackets = _PxmAcPmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2, 1, 6),
    _PxmAcPmTxPackets_Type()
)
pxmAcPmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmTxPackets.setStatus("current")
_PxmAcPmTxOctets_Type = HCPerfIntervalCount
_PxmAcPmTxOctets_Object = MibTableColumn
pxmAcPmTxOctets = _PxmAcPmTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 1, 2, 1, 7),
    _PxmAcPmTxOctets_Type()
)
pxmAcPmTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAcPmTxOctets.setStatus("current")
_PxmAcBwpPm_ObjectIdentity = ObjectIdentity
pxmAcBwpPm = _PxmAcBwpPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2)
)
_PxmBwpAcPmRealTable_Object = MibTable
pxmBwpAcPmRealTable = _PxmBwpAcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 1)
)
if mibBuilder.loadTexts:
    pxmBwpAcPmRealTable.setStatus("current")
_PxmBwpAcPmRealEntry_Object = MibTableRow
pxmBwpAcPmRealEntry = _PxmBwpAcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 1, 1)
)
pxmBwpAcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmBwpAcPmRealEntry.setStatus("current")
_PxmBwpAcPmRealPolicerConformedPkts_Type = Counter64
_PxmBwpAcPmRealPolicerConformedPkts_Object = MibTableColumn
pxmBwpAcPmRealPolicerConformedPkts = _PxmBwpAcPmRealPolicerConformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 1, 1, 1),
    _PxmBwpAcPmRealPolicerConformedPkts_Type()
)
pxmBwpAcPmRealPolicerConformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmRealPolicerConformedPkts.setStatus("current")
_PxmBwpAcPmRealPolicerConformedOctets_Type = Counter64
_PxmBwpAcPmRealPolicerConformedOctets_Object = MibTableColumn
pxmBwpAcPmRealPolicerConformedOctets = _PxmBwpAcPmRealPolicerConformedOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 1, 1, 2),
    _PxmBwpAcPmRealPolicerConformedOctets_Type()
)
pxmBwpAcPmRealPolicerConformedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmRealPolicerConformedOctets.setStatus("current")
_PxmBwpAcPmRealPolicerExceededPkts_Type = Counter64
_PxmBwpAcPmRealPolicerExceededPkts_Object = MibTableColumn
pxmBwpAcPmRealPolicerExceededPkts = _PxmBwpAcPmRealPolicerExceededPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 1, 1, 3),
    _PxmBwpAcPmRealPolicerExceededPkts_Type()
)
pxmBwpAcPmRealPolicerExceededPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmRealPolicerExceededPkts.setStatus("current")
_PxmBwpAcPmRealPolicerExceededOctets_Type = Counter64
_PxmBwpAcPmRealPolicerExceededOctets_Object = MibTableColumn
pxmBwpAcPmRealPolicerExceededOctets = _PxmBwpAcPmRealPolicerExceededOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 1, 1, 4),
    _PxmBwpAcPmRealPolicerExceededOctets_Type()
)
pxmBwpAcPmRealPolicerExceededOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmRealPolicerExceededOctets.setStatus("current")
_PxmBwpAcPmRealPolicerViolatedPkts_Type = Counter64
_PxmBwpAcPmRealPolicerViolatedPkts_Object = MibTableColumn
pxmBwpAcPmRealPolicerViolatedPkts = _PxmBwpAcPmRealPolicerViolatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 1, 1, 5),
    _PxmBwpAcPmRealPolicerViolatedPkts_Type()
)
pxmBwpAcPmRealPolicerViolatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmRealPolicerViolatedPkts.setStatus("current")
_PxmBwpAcPmRealPolicerViolatedOctets_Type = Counter64
_PxmBwpAcPmRealPolicerViolatedOctets_Object = MibTableColumn
pxmBwpAcPmRealPolicerViolatedOctets = _PxmBwpAcPmRealPolicerViolatedOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 1, 1, 6),
    _PxmBwpAcPmRealPolicerViolatedOctets_Type()
)
pxmBwpAcPmRealPolicerViolatedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmRealPolicerViolatedOctets.setStatus("current")
_PxmBwpAcPmTable_Object = MibTable
pxmBwpAcPmTable = _PxmBwpAcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2)
)
if mibBuilder.loadTexts:
    pxmBwpAcPmTable.setStatus("current")
_PxmBwpAcPmEntry_Object = MibTableRow
pxmBwpAcPmEntry = _PxmBwpAcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1)
)
pxmBwpAcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmSampleDuration"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmBwpAcPmEntry.setStatus("current")


class _PxmBwpAcPmTimestamp_Type(Integer32):
    """Custom type pxmBwpAcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmBwpAcPmTimestamp_Type.__name__ = "Integer32"
_PxmBwpAcPmTimestamp_Object = MibTableColumn
pxmBwpAcPmTimestamp = _PxmBwpAcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 1),
    _PxmBwpAcPmTimestamp_Type()
)
pxmBwpAcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmBwpAcPmTimestamp.setStatus("current")


class _PxmBwpAcPmSampleDuration_Type(Integer32):
    """Custom type pxmBwpAcPmSampleDuration based on Integer32"""
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


_PxmBwpAcPmSampleDuration_Type.__name__ = "Integer32"
_PxmBwpAcPmSampleDuration_Object = MibTableColumn
pxmBwpAcPmSampleDuration = _PxmBwpAcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 2),
    _PxmBwpAcPmSampleDuration_Type()
)
pxmBwpAcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmBwpAcPmSampleDuration.setStatus("current")
_PxmBwpAcPmValidity_Type = TruthValue
_PxmBwpAcPmValidity_Object = MibTableColumn
pxmBwpAcPmValidity = _PxmBwpAcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 3),
    _PxmBwpAcPmValidity_Type()
)
pxmBwpAcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmValidity.setStatus("current")
_PxmBwpAcPmPolicerConformedPkts_Type = HCPerfIntervalCount
_PxmBwpAcPmPolicerConformedPkts_Object = MibTableColumn
pxmBwpAcPmPolicerConformedPkts = _PxmBwpAcPmPolicerConformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 4),
    _PxmBwpAcPmPolicerConformedPkts_Type()
)
pxmBwpAcPmPolicerConformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmPolicerConformedPkts.setStatus("current")
_PxmBwpAcPmPolicerConformedOctets_Type = HCPerfIntervalCount
_PxmBwpAcPmPolicerConformedOctets_Object = MibTableColumn
pxmBwpAcPmPolicerConformedOctets = _PxmBwpAcPmPolicerConformedOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 5),
    _PxmBwpAcPmPolicerConformedOctets_Type()
)
pxmBwpAcPmPolicerConformedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmPolicerConformedOctets.setStatus("current")
_PxmBwpAcPmPolicerExceededPkts_Type = HCPerfIntervalCount
_PxmBwpAcPmPolicerExceededPkts_Object = MibTableColumn
pxmBwpAcPmPolicerExceededPkts = _PxmBwpAcPmPolicerExceededPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 6),
    _PxmBwpAcPmPolicerExceededPkts_Type()
)
pxmBwpAcPmPolicerExceededPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmPolicerExceededPkts.setStatus("current")
_PxmBwpAcPmPolicerExceededOctets_Type = HCPerfIntervalCount
_PxmBwpAcPmPolicerExceededOctets_Object = MibTableColumn
pxmBwpAcPmPolicerExceededOctets = _PxmBwpAcPmPolicerExceededOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 7),
    _PxmBwpAcPmPolicerExceededOctets_Type()
)
pxmBwpAcPmPolicerExceededOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmPolicerExceededOctets.setStatus("current")
_PxmBwpAcPmPolicerViolatedPkts_Type = HCPerfIntervalCount
_PxmBwpAcPmPolicerViolatedPkts_Object = MibTableColumn
pxmBwpAcPmPolicerViolatedPkts = _PxmBwpAcPmPolicerViolatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 8),
    _PxmBwpAcPmPolicerViolatedPkts_Type()
)
pxmBwpAcPmPolicerViolatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmPolicerViolatedPkts.setStatus("current")
_PxmBwpAcPmPolicerViolatedOctets_Type = HCPerfIntervalCount
_PxmBwpAcPmPolicerViolatedOctets_Object = MibTableColumn
pxmBwpAcPmPolicerViolatedOctets = _PxmBwpAcPmPolicerViolatedOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 2, 2, 1, 9),
    _PxmBwpAcPmPolicerViolatedOctets_Type()
)
pxmBwpAcPmPolicerViolatedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmBwpAcPmPolicerViolatedOctets.setStatus("current")
_PxmCmAcPmObjects_ObjectIdentity = ObjectIdentity
pxmCmAcPmObjects = _PxmCmAcPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3)
)
_PxmCmAcRealPm_ObjectIdentity = ObjectIdentity
pxmCmAcRealPm = _PxmCmAcRealPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1)
)
_PxmTC0AcPmRealTable_Object = MibTable
pxmTC0AcPmRealTable = _PxmTC0AcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pxmTC0AcPmRealTable.setStatus("current")
_PxmTC0AcPmRealEntry_Object = MibTableRow
pxmTC0AcPmRealEntry = _PxmTC0AcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1)
)
pxmTC0AcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC0AcPmRealEntry.setStatus("current")
_PxmTC0AcPmRealTCNum_Type = Integer32
_PxmTC0AcPmRealTCNum_Object = MibTableColumn
pxmTC0AcPmRealTCNum = _PxmTC0AcPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 1),
    _PxmTC0AcPmRealTCNum_Type()
)
pxmTC0AcPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealTCNum.setStatus("current")
_PxmTC0AcPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC0AcPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC0AcPmRealTDQueuingCurrentQDepth = _PxmTC0AcPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 2),
    _PxmTC0AcPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC0AcPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC0AcPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC0AcPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC0AcPmRealQueueingDiscardOctets = _PxmTC0AcPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 3),
    _PxmTC0AcPmRealQueueingDiscardOctets_Type()
)
pxmTC0AcPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC0AcPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC0AcPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC0AcPmRealQueueingDiscardPkts = _PxmTC0AcPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 4),
    _PxmTC0AcPmRealQueueingDiscardPkts_Type()
)
pxmTC0AcPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC0AcPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC0AcPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC0AcPmRealRandomGreenDropPkts = _PxmTC0AcPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 5),
    _PxmTC0AcPmRealRandomGreenDropPkts_Type()
)
pxmTC0AcPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC0AcPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC0AcPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC0AcPmRealRandomGreenDropOctets = _PxmTC0AcPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 6),
    _PxmTC0AcPmRealRandomGreenDropOctets_Type()
)
pxmTC0AcPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC0AcPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC0AcPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC0AcPmRealRandomYellowDropPkts = _PxmTC0AcPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 7),
    _PxmTC0AcPmRealRandomYellowDropPkts_Type()
)
pxmTC0AcPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC0AcPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC0AcPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC0AcPmRealRandomYellowDropOctets = _PxmTC0AcPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 8),
    _PxmTC0AcPmRealRandomYellowDropOctets_Type()
)
pxmTC0AcPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC0AcPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC0AcPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC0AcPmRealQueueingTransmitPkts = _PxmTC0AcPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 9),
    _PxmTC0AcPmRealQueueingTransmitPkts_Type()
)
pxmTC0AcPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC0AcPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC0AcPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC0AcPmRealQueueingTransmitOctets = _PxmTC0AcPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 10),
    _PxmTC0AcPmRealQueueingTransmitOctets_Type()
)
pxmTC0AcPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC0AcPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC0AcPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC0AcPmRealQueueingMeanQSizeUnit = _PxmTC0AcPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 11),
    _PxmTC0AcPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC0AcPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC0AcPmRealMeanQSize_Type = Integer32
_PxmTC0AcPmRealMeanQSize_Object = MibTableColumn
pxmTC0AcPmRealMeanQSize = _PxmTC0AcPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 1, 1, 12),
    _PxmTC0AcPmRealMeanQSize_Type()
)
pxmTC0AcPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRealMeanQSize.setStatus("current")
_PxmTC2AcPmRealTable_Object = MibTable
pxmTC2AcPmRealTable = _PxmTC2AcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2)
)
if mibBuilder.loadTexts:
    pxmTC2AcPmRealTable.setStatus("current")
_PxmTC2AcPmRealEntry_Object = MibTableRow
pxmTC2AcPmRealEntry = _PxmTC2AcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1)
)
pxmTC2AcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC2AcPmRealEntry.setStatus("current")
_PxmTC2AcPmRealTCNum_Type = Integer32
_PxmTC2AcPmRealTCNum_Object = MibTableColumn
pxmTC2AcPmRealTCNum = _PxmTC2AcPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 1),
    _PxmTC2AcPmRealTCNum_Type()
)
pxmTC2AcPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealTCNum.setStatus("current")
_PxmTC2AcPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC2AcPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC2AcPmRealTDQueuingCurrentQDepth = _PxmTC2AcPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 2),
    _PxmTC2AcPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC2AcPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC2AcPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC2AcPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC2AcPmRealQueueingDiscardOctets = _PxmTC2AcPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 3),
    _PxmTC2AcPmRealQueueingDiscardOctets_Type()
)
pxmTC2AcPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC2AcPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC2AcPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC2AcPmRealQueueingDiscardPkts = _PxmTC2AcPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 4),
    _PxmTC2AcPmRealQueueingDiscardPkts_Type()
)
pxmTC2AcPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC2AcPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC2AcPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC2AcPmRealRandomGreenDropPkts = _PxmTC2AcPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 5),
    _PxmTC2AcPmRealRandomGreenDropPkts_Type()
)
pxmTC2AcPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC2AcPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC2AcPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC2AcPmRealRandomGreenDropOctets = _PxmTC2AcPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 6),
    _PxmTC2AcPmRealRandomGreenDropOctets_Type()
)
pxmTC2AcPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC2AcPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC2AcPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC2AcPmRealRandomYellowDropPkts = _PxmTC2AcPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 7),
    _PxmTC2AcPmRealRandomYellowDropPkts_Type()
)
pxmTC2AcPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC2AcPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC2AcPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC2AcPmRealRandomYellowDropOctets = _PxmTC2AcPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 8),
    _PxmTC2AcPmRealRandomYellowDropOctets_Type()
)
pxmTC2AcPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC2AcPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC2AcPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC2AcPmRealQueueingTransmitPkts = _PxmTC2AcPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 9),
    _PxmTC2AcPmRealQueueingTransmitPkts_Type()
)
pxmTC2AcPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC2AcPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC2AcPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC2AcPmRealQueueingTransmitOctets = _PxmTC2AcPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 10),
    _PxmTC2AcPmRealQueueingTransmitOctets_Type()
)
pxmTC2AcPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC2AcPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC2AcPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC2AcPmRealQueueingMeanQSizeUnit = _PxmTC2AcPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 11),
    _PxmTC2AcPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC2AcPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC2AcPmRealMeanQSize_Type = Integer32
_PxmTC2AcPmRealMeanQSize_Object = MibTableColumn
pxmTC2AcPmRealMeanQSize = _PxmTC2AcPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 2, 1, 12),
    _PxmTC2AcPmRealMeanQSize_Type()
)
pxmTC2AcPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRealMeanQSize.setStatus("current")
_PxmTC4AcPmRealTable_Object = MibTable
pxmTC4AcPmRealTable = _PxmTC4AcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3)
)
if mibBuilder.loadTexts:
    pxmTC4AcPmRealTable.setStatus("current")
_PxmTC4AcPmRealEntry_Object = MibTableRow
pxmTC4AcPmRealEntry = _PxmTC4AcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1)
)
pxmTC4AcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC4AcPmRealEntry.setStatus("current")
_PxmTC4AcPmRealTCNum_Type = Integer32
_PxmTC4AcPmRealTCNum_Object = MibTableColumn
pxmTC4AcPmRealTCNum = _PxmTC4AcPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 1),
    _PxmTC4AcPmRealTCNum_Type()
)
pxmTC4AcPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealTCNum.setStatus("current")
_PxmTC4AcPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC4AcPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC4AcPmRealTDQueuingCurrentQDepth = _PxmTC4AcPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 2),
    _PxmTC4AcPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC4AcPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC4AcPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC4AcPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC4AcPmRealQueueingDiscardOctets = _PxmTC4AcPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 3),
    _PxmTC4AcPmRealQueueingDiscardOctets_Type()
)
pxmTC4AcPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC4AcPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC4AcPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC4AcPmRealQueueingDiscardPkts = _PxmTC4AcPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 4),
    _PxmTC4AcPmRealQueueingDiscardPkts_Type()
)
pxmTC4AcPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC4AcPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC4AcPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC4AcPmRealRandomGreenDropPkts = _PxmTC4AcPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 5),
    _PxmTC4AcPmRealRandomGreenDropPkts_Type()
)
pxmTC4AcPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC4AcPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC4AcPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC4AcPmRealRandomGreenDropOctets = _PxmTC4AcPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 6),
    _PxmTC4AcPmRealRandomGreenDropOctets_Type()
)
pxmTC4AcPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC4AcPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC4AcPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC4AcPmRealRandomYellowDropPkts = _PxmTC4AcPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 7),
    _PxmTC4AcPmRealRandomYellowDropPkts_Type()
)
pxmTC4AcPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC4AcPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC4AcPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC4AcPmRealRandomYellowDropOctets = _PxmTC4AcPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 8),
    _PxmTC4AcPmRealRandomYellowDropOctets_Type()
)
pxmTC4AcPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC4AcPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC4AcPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC4AcPmRealQueueingTransmitPkts = _PxmTC4AcPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 9),
    _PxmTC4AcPmRealQueueingTransmitPkts_Type()
)
pxmTC4AcPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC4AcPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC4AcPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC4AcPmRealQueueingTransmitOctets = _PxmTC4AcPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 10),
    _PxmTC4AcPmRealQueueingTransmitOctets_Type()
)
pxmTC4AcPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC4AcPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC4AcPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC4AcPmRealQueueingMeanQSizeUnit = _PxmTC4AcPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 11),
    _PxmTC4AcPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC4AcPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC4AcPmRealMeanQSize_Type = Integer32
_PxmTC4AcPmRealMeanQSize_Object = MibTableColumn
pxmTC4AcPmRealMeanQSize = _PxmTC4AcPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 3, 1, 12),
    _PxmTC4AcPmRealMeanQSize_Type()
)
pxmTC4AcPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRealMeanQSize.setStatus("current")
_PxmTC6AcPmRealTable_Object = MibTable
pxmTC6AcPmRealTable = _PxmTC6AcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4)
)
if mibBuilder.loadTexts:
    pxmTC6AcPmRealTable.setStatus("current")
_PxmTC6AcPmRealEntry_Object = MibTableRow
pxmTC6AcPmRealEntry = _PxmTC6AcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1)
)
pxmTC6AcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC6AcPmRealEntry.setStatus("current")
_PxmTC6AcPmRealTCNum_Type = Integer32
_PxmTC6AcPmRealTCNum_Object = MibTableColumn
pxmTC6AcPmRealTCNum = _PxmTC6AcPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 1),
    _PxmTC6AcPmRealTCNum_Type()
)
pxmTC6AcPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealTCNum.setStatus("current")
_PxmTC6AcPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC6AcPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC6AcPmRealTDQueuingCurrentQDepth = _PxmTC6AcPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 2),
    _PxmTC6AcPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC6AcPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC6AcPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC6AcPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC6AcPmRealQueueingDiscardOctets = _PxmTC6AcPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 3),
    _PxmTC6AcPmRealQueueingDiscardOctets_Type()
)
pxmTC6AcPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC6AcPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC6AcPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC6AcPmRealQueueingDiscardPkts = _PxmTC6AcPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 4),
    _PxmTC6AcPmRealQueueingDiscardPkts_Type()
)
pxmTC6AcPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC6AcPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC6AcPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC6AcPmRealRandomGreenDropPkts = _PxmTC6AcPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 5),
    _PxmTC6AcPmRealRandomGreenDropPkts_Type()
)
pxmTC6AcPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC6AcPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC6AcPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC6AcPmRealRandomGreenDropOctets = _PxmTC6AcPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 6),
    _PxmTC6AcPmRealRandomGreenDropOctets_Type()
)
pxmTC6AcPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC6AcPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC6AcPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC6AcPmRealRandomYellowDropPkts = _PxmTC6AcPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 7),
    _PxmTC6AcPmRealRandomYellowDropPkts_Type()
)
pxmTC6AcPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC6AcPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC6AcPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC6AcPmRealRandomYellowDropOctets = _PxmTC6AcPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 8),
    _PxmTC6AcPmRealRandomYellowDropOctets_Type()
)
pxmTC6AcPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC6AcPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC6AcPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC6AcPmRealQueueingTransmitPkts = _PxmTC6AcPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 9),
    _PxmTC6AcPmRealQueueingTransmitPkts_Type()
)
pxmTC6AcPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC6AcPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC6AcPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC6AcPmRealQueueingTransmitOctets = _PxmTC6AcPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 10),
    _PxmTC6AcPmRealQueueingTransmitOctets_Type()
)
pxmTC6AcPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC6AcPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC6AcPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC6AcPmRealQueueingMeanQSizeUnit = _PxmTC6AcPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 11),
    _PxmTC6AcPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC6AcPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC6AcPmRealMeanQSize_Type = Integer32
_PxmTC6AcPmRealMeanQSize_Object = MibTableColumn
pxmTC6AcPmRealMeanQSize = _PxmTC6AcPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 4, 1, 12),
    _PxmTC6AcPmRealMeanQSize_Type()
)
pxmTC6AcPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRealMeanQSize.setStatus("current")
_PxmTC7AcPmRealTable_Object = MibTable
pxmTC7AcPmRealTable = _PxmTC7AcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5)
)
if mibBuilder.loadTexts:
    pxmTC7AcPmRealTable.setStatus("current")
_PxmTC7AcPmRealEntry_Object = MibTableRow
pxmTC7AcPmRealEntry = _PxmTC7AcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1)
)
pxmTC7AcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTC7AcPmRealEntry.setStatus("current")
_PxmTC7AcPmRealTCNum_Type = Integer32
_PxmTC7AcPmRealTCNum_Object = MibTableColumn
pxmTC7AcPmRealTCNum = _PxmTC7AcPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 1),
    _PxmTC7AcPmRealTCNum_Type()
)
pxmTC7AcPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealTCNum.setStatus("current")
_PxmTC7AcPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTC7AcPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTC7AcPmRealTDQueuingCurrentQDepth = _PxmTC7AcPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 2),
    _PxmTC7AcPmRealTDQueuingCurrentQDepth_Type()
)
pxmTC7AcPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTC7AcPmRealQueueingDiscardOctets_Type = Counter64
_PxmTC7AcPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTC7AcPmRealQueueingDiscardOctets = _PxmTC7AcPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 3),
    _PxmTC7AcPmRealQueueingDiscardOctets_Type()
)
pxmTC7AcPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealQueueingDiscardOctets.setStatus("current")
_PxmTC7AcPmRealQueueingDiscardPkts_Type = Integer32
_PxmTC7AcPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTC7AcPmRealQueueingDiscardPkts = _PxmTC7AcPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 4),
    _PxmTC7AcPmRealQueueingDiscardPkts_Type()
)
pxmTC7AcPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealQueueingDiscardPkts.setStatus("current")
_PxmTC7AcPmRealRandomGreenDropPkts_Type = Counter64
_PxmTC7AcPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTC7AcPmRealRandomGreenDropPkts = _PxmTC7AcPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 5),
    _PxmTC7AcPmRealRandomGreenDropPkts_Type()
)
pxmTC7AcPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealRandomGreenDropPkts.setStatus("current")
_PxmTC7AcPmRealRandomGreenDropOctets_Type = Counter64
_PxmTC7AcPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTC7AcPmRealRandomGreenDropOctets = _PxmTC7AcPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 6),
    _PxmTC7AcPmRealRandomGreenDropOctets_Type()
)
pxmTC7AcPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealRandomGreenDropOctets.setStatus("current")
_PxmTC7AcPmRealRandomYellowDropPkts_Type = Counter64
_PxmTC7AcPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTC7AcPmRealRandomYellowDropPkts = _PxmTC7AcPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 7),
    _PxmTC7AcPmRealRandomYellowDropPkts_Type()
)
pxmTC7AcPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealRandomYellowDropPkts.setStatus("current")
_PxmTC7AcPmRealRandomYellowDropOctets_Type = Counter64
_PxmTC7AcPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTC7AcPmRealRandomYellowDropOctets = _PxmTC7AcPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 8),
    _PxmTC7AcPmRealRandomYellowDropOctets_Type()
)
pxmTC7AcPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealRandomYellowDropOctets.setStatus("current")
_PxmTC7AcPmRealQueueingTransmitPkts_Type = Counter64
_PxmTC7AcPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTC7AcPmRealQueueingTransmitPkts = _PxmTC7AcPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 9),
    _PxmTC7AcPmRealQueueingTransmitPkts_Type()
)
pxmTC7AcPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealQueueingTransmitPkts.setStatus("current")
_PxmTC7AcPmRealQueueingTransmitOctets_Type = Counter64
_PxmTC7AcPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTC7AcPmRealQueueingTransmitOctets = _PxmTC7AcPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 10),
    _PxmTC7AcPmRealQueueingTransmitOctets_Type()
)
pxmTC7AcPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealQueueingTransmitOctets.setStatus("current")
_PxmTC7AcPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTC7AcPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTC7AcPmRealQueueingMeanQSizeUnit = _PxmTC7AcPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 11),
    _PxmTC7AcPmRealQueueingMeanQSizeUnit_Type()
)
pxmTC7AcPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTC7AcPmRealMeanQSize_Type = Integer32
_PxmTC7AcPmRealMeanQSize_Object = MibTableColumn
pxmTC7AcPmRealMeanQSize = _PxmTC7AcPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 5, 1, 12),
    _PxmTC7AcPmRealMeanQSize_Type()
)
pxmTC7AcPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRealMeanQSize.setStatus("current")
_PxmTCANYAcPmRealTable_Object = MibTable
pxmTCANYAcPmRealTable = _PxmTCANYAcPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6)
)
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealTable.setStatus("current")
_PxmTCANYAcPmRealEntry_Object = MibTableRow
pxmTCANYAcPmRealEntry = _PxmTCANYAcPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1)
)
pxmTCANYAcPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealEntry.setStatus("current")
_PxmTCANYAcPmRealTCNum_Type = Integer32
_PxmTCANYAcPmRealTCNum_Object = MibTableColumn
pxmTCANYAcPmRealTCNum = _PxmTCANYAcPmRealTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 1),
    _PxmTCANYAcPmRealTCNum_Type()
)
pxmTCANYAcPmRealTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealTCNum.setStatus("current")
_PxmTCANYAcPmRealTDQueuingCurrentQDepth_Type = Integer32
_PxmTCANYAcPmRealTDQueuingCurrentQDepth_Object = MibTableColumn
pxmTCANYAcPmRealTDQueuingCurrentQDepth = _PxmTCANYAcPmRealTDQueuingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 2),
    _PxmTCANYAcPmRealTDQueuingCurrentQDepth_Type()
)
pxmTCANYAcPmRealTDQueuingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealTDQueuingCurrentQDepth.setStatus("current")
_PxmTCANYAcPmRealQueueingDiscardOctets_Type = Counter64
_PxmTCANYAcPmRealQueueingDiscardOctets_Object = MibTableColumn
pxmTCANYAcPmRealQueueingDiscardOctets = _PxmTCANYAcPmRealQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 3),
    _PxmTCANYAcPmRealQueueingDiscardOctets_Type()
)
pxmTCANYAcPmRealQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealQueueingDiscardOctets.setStatus("current")
_PxmTCANYAcPmRealQueueingDiscardPkts_Type = Integer32
_PxmTCANYAcPmRealQueueingDiscardPkts_Object = MibTableColumn
pxmTCANYAcPmRealQueueingDiscardPkts = _PxmTCANYAcPmRealQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 4),
    _PxmTCANYAcPmRealQueueingDiscardPkts_Type()
)
pxmTCANYAcPmRealQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealQueueingDiscardPkts.setStatus("current")
_PxmTCANYAcPmRealRandomGreenDropPkts_Type = Counter64
_PxmTCANYAcPmRealRandomGreenDropPkts_Object = MibTableColumn
pxmTCANYAcPmRealRandomGreenDropPkts = _PxmTCANYAcPmRealRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 5),
    _PxmTCANYAcPmRealRandomGreenDropPkts_Type()
)
pxmTCANYAcPmRealRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealRandomGreenDropPkts.setStatus("current")
_PxmTCANYAcPmRealRandomGreenDropOctets_Type = Counter64
_PxmTCANYAcPmRealRandomGreenDropOctets_Object = MibTableColumn
pxmTCANYAcPmRealRandomGreenDropOctets = _PxmTCANYAcPmRealRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 6),
    _PxmTCANYAcPmRealRandomGreenDropOctets_Type()
)
pxmTCANYAcPmRealRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealRandomGreenDropOctets.setStatus("current")
_PxmTCANYAcPmRealRandomYellowDropPkts_Type = Counter64
_PxmTCANYAcPmRealRandomYellowDropPkts_Object = MibTableColumn
pxmTCANYAcPmRealRandomYellowDropPkts = _PxmTCANYAcPmRealRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 7),
    _PxmTCANYAcPmRealRandomYellowDropPkts_Type()
)
pxmTCANYAcPmRealRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealRandomYellowDropPkts.setStatus("current")
_PxmTCANYAcPmRealRandomYellowDropOctets_Type = Counter64
_PxmTCANYAcPmRealRandomYellowDropOctets_Object = MibTableColumn
pxmTCANYAcPmRealRandomYellowDropOctets = _PxmTCANYAcPmRealRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 8),
    _PxmTCANYAcPmRealRandomYellowDropOctets_Type()
)
pxmTCANYAcPmRealRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealRandomYellowDropOctets.setStatus("current")
_PxmTCANYAcPmRealQueueingTransmitPkts_Type = Counter64
_PxmTCANYAcPmRealQueueingTransmitPkts_Object = MibTableColumn
pxmTCANYAcPmRealQueueingTransmitPkts = _PxmTCANYAcPmRealQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 9),
    _PxmTCANYAcPmRealQueueingTransmitPkts_Type()
)
pxmTCANYAcPmRealQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealQueueingTransmitPkts.setStatus("current")
_PxmTCANYAcPmRealQueueingTransmitOctets_Type = Counter64
_PxmTCANYAcPmRealQueueingTransmitOctets_Object = MibTableColumn
pxmTCANYAcPmRealQueueingTransmitOctets = _PxmTCANYAcPmRealQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 10),
    _PxmTCANYAcPmRealQueueingTransmitOctets_Type()
)
pxmTCANYAcPmRealQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealQueueingTransmitOctets.setStatus("current")
_PxmTCANYAcPmRealQueueingMeanQSizeUnit_Type = Integer32
_PxmTCANYAcPmRealQueueingMeanQSizeUnit_Object = MibTableColumn
pxmTCANYAcPmRealQueueingMeanQSizeUnit = _PxmTCANYAcPmRealQueueingMeanQSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 11),
    _PxmTCANYAcPmRealQueueingMeanQSizeUnit_Type()
)
pxmTCANYAcPmRealQueueingMeanQSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealQueueingMeanQSizeUnit.setStatus("current")
_PxmTCANYAcPmRealMeanQSize_Type = Integer32
_PxmTCANYAcPmRealMeanQSize_Object = MibTableColumn
pxmTCANYAcPmRealMeanQSize = _PxmTCANYAcPmRealMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 1, 6, 1, 12),
    _PxmTCANYAcPmRealMeanQSize_Type()
)
pxmTCANYAcPmRealMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealMeanQSize.setStatus("current")
_PxmCmAcPm_ObjectIdentity = ObjectIdentity
pxmCmAcPm = _PxmCmAcPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2)
)
_PxmTC0AcPmTable_Object = MibTable
pxmTC0AcPmTable = _PxmTC0AcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pxmTC0AcPmTable.setStatus("current")
_PxmTC0AcPmEntry_Object = MibTableRow
pxmTC0AcPmEntry = _PxmTC0AcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1)
)
pxmTC0AcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmSampleDuration"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC0AcPmEntry.setStatus("current")


class _PxmTC0AcPmTimestamp_Type(Integer32):
    """Custom type pxmTC0AcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC0AcPmTimestamp_Type.__name__ = "Integer32"
_PxmTC0AcPmTimestamp_Object = MibTableColumn
pxmTC0AcPmTimestamp = _PxmTC0AcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 1),
    _PxmTC0AcPmTimestamp_Type()
)
pxmTC0AcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC0AcPmTimestamp.setStatus("current")


class _PxmTC0AcPmSampleDuration_Type(Integer32):
    """Custom type pxmTC0AcPmSampleDuration based on Integer32"""
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


_PxmTC0AcPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC0AcPmSampleDuration_Object = MibTableColumn
pxmTC0AcPmSampleDuration = _PxmTC0AcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 2),
    _PxmTC0AcPmSampleDuration_Type()
)
pxmTC0AcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC0AcPmSampleDuration.setStatus("current")
_PxmTC0AcPmValidity_Type = TruthValue
_PxmTC0AcPmValidity_Object = MibTableColumn
pxmTC0AcPmValidity = _PxmTC0AcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 3),
    _PxmTC0AcPmValidity_Type()
)
pxmTC0AcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmValidity.setStatus("current")
_PxmTC0AcPmTCNum_Type = Integer32
_PxmTC0AcPmTCNum_Object = MibTableColumn
pxmTC0AcPmTCNum = _PxmTC0AcPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 4),
    _PxmTC0AcPmTCNum_Type()
)
pxmTC0AcPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmTCNum.setStatus("current")
_PxmTC0AcPmQueueingDiscardOctets_Type = Counter64
_PxmTC0AcPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC0AcPmQueueingDiscardOctets = _PxmTC0AcPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 5),
    _PxmTC0AcPmQueueingDiscardOctets_Type()
)
pxmTC0AcPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmQueueingDiscardOctets.setStatus("current")
_PxmTC0AcPmQueueingDiscardPkts_Type = Integer32
_PxmTC0AcPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC0AcPmQueueingDiscardPkts = _PxmTC0AcPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 6),
    _PxmTC0AcPmQueueingDiscardPkts_Type()
)
pxmTC0AcPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmQueueingDiscardPkts.setStatus("current")
_PxmTC0AcPmRandomGreenDropPkts_Type = Counter64
_PxmTC0AcPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC0AcPmRandomGreenDropPkts = _PxmTC0AcPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 7),
    _PxmTC0AcPmRandomGreenDropPkts_Type()
)
pxmTC0AcPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRandomGreenDropPkts.setStatus("current")
_PxmTC0AcPmRandomGreenDropOctets_Type = Counter64
_PxmTC0AcPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC0AcPmRandomGreenDropOctets = _PxmTC0AcPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 8),
    _PxmTC0AcPmRandomGreenDropOctets_Type()
)
pxmTC0AcPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRandomGreenDropOctets.setStatus("current")
_PxmTC0AcPmRandomYellowDropPkts_Type = Counter64
_PxmTC0AcPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC0AcPmRandomYellowDropPkts = _PxmTC0AcPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 9),
    _PxmTC0AcPmRandomYellowDropPkts_Type()
)
pxmTC0AcPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRandomYellowDropPkts.setStatus("current")
_PxmTC0AcPmRandomYellowDropOctets_Type = Counter64
_PxmTC0AcPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC0AcPmRandomYellowDropOctets = _PxmTC0AcPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 10),
    _PxmTC0AcPmRandomYellowDropOctets_Type()
)
pxmTC0AcPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmRandomYellowDropOctets.setStatus("current")
_PxmTC0AcPmQueueingTransmitPkts_Type = Counter64
_PxmTC0AcPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC0AcPmQueueingTransmitPkts = _PxmTC0AcPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 11),
    _PxmTC0AcPmQueueingTransmitPkts_Type()
)
pxmTC0AcPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmQueueingTransmitPkts.setStatus("current")
_PxmTC0AcPmQueueingTransmitOctets_Type = Counter64
_PxmTC0AcPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC0AcPmQueueingTransmitOctets = _PxmTC0AcPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 1, 1, 12),
    _PxmTC0AcPmQueueingTransmitOctets_Type()
)
pxmTC0AcPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC0AcPmQueueingTransmitOctets.setStatus("current")
_PxmTC2AcPmTable_Object = MibTable
pxmTC2AcPmTable = _PxmTC2AcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2)
)
if mibBuilder.loadTexts:
    pxmTC2AcPmTable.setStatus("current")
_PxmTC2AcPmEntry_Object = MibTableRow
pxmTC2AcPmEntry = _PxmTC2AcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1)
)
pxmTC2AcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmSampleDuration"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC2AcPmEntry.setStatus("current")


class _PxmTC2AcPmTimestamp_Type(Integer32):
    """Custom type pxmTC2AcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC2AcPmTimestamp_Type.__name__ = "Integer32"
_PxmTC2AcPmTimestamp_Object = MibTableColumn
pxmTC2AcPmTimestamp = _PxmTC2AcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 1),
    _PxmTC2AcPmTimestamp_Type()
)
pxmTC2AcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC2AcPmTimestamp.setStatus("current")


class _PxmTC2AcPmSampleDuration_Type(Integer32):
    """Custom type pxmTC2AcPmSampleDuration based on Integer32"""
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


_PxmTC2AcPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC2AcPmSampleDuration_Object = MibTableColumn
pxmTC2AcPmSampleDuration = _PxmTC2AcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 2),
    _PxmTC2AcPmSampleDuration_Type()
)
pxmTC2AcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC2AcPmSampleDuration.setStatus("current")
_PxmTC2AcPmValidity_Type = TruthValue
_PxmTC2AcPmValidity_Object = MibTableColumn
pxmTC2AcPmValidity = _PxmTC2AcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 3),
    _PxmTC2AcPmValidity_Type()
)
pxmTC2AcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmValidity.setStatus("current")
_PxmTC2AcPmTCNum_Type = Integer32
_PxmTC2AcPmTCNum_Object = MibTableColumn
pxmTC2AcPmTCNum = _PxmTC2AcPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 4),
    _PxmTC2AcPmTCNum_Type()
)
pxmTC2AcPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmTCNum.setStatus("current")
_PxmTC2AcPmQueueingDiscardOctets_Type = Counter64
_PxmTC2AcPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC2AcPmQueueingDiscardOctets = _PxmTC2AcPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 5),
    _PxmTC2AcPmQueueingDiscardOctets_Type()
)
pxmTC2AcPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmQueueingDiscardOctets.setStatus("current")
_PxmTC2AcPmQueueingDiscardPkts_Type = Integer32
_PxmTC2AcPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC2AcPmQueueingDiscardPkts = _PxmTC2AcPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 6),
    _PxmTC2AcPmQueueingDiscardPkts_Type()
)
pxmTC2AcPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmQueueingDiscardPkts.setStatus("current")
_PxmTC2AcPmRandomGreenDropPkts_Type = Counter64
_PxmTC2AcPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC2AcPmRandomGreenDropPkts = _PxmTC2AcPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 7),
    _PxmTC2AcPmRandomGreenDropPkts_Type()
)
pxmTC2AcPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRandomGreenDropPkts.setStatus("current")
_PxmTC2AcPmRandomGreenDropOctets_Type = Counter64
_PxmTC2AcPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC2AcPmRandomGreenDropOctets = _PxmTC2AcPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 8),
    _PxmTC2AcPmRandomGreenDropOctets_Type()
)
pxmTC2AcPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRandomGreenDropOctets.setStatus("current")
_PxmTC2AcPmRandomYellowDropPkts_Type = Counter64
_PxmTC2AcPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC2AcPmRandomYellowDropPkts = _PxmTC2AcPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 9),
    _PxmTC2AcPmRandomYellowDropPkts_Type()
)
pxmTC2AcPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRandomYellowDropPkts.setStatus("current")
_PxmTC2AcPmRandomYellowDropOctets_Type = Counter64
_PxmTC2AcPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC2AcPmRandomYellowDropOctets = _PxmTC2AcPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 10),
    _PxmTC2AcPmRandomYellowDropOctets_Type()
)
pxmTC2AcPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmRandomYellowDropOctets.setStatus("current")
_PxmTC2AcPmQueueingTransmitPkts_Type = Counter64
_PxmTC2AcPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC2AcPmQueueingTransmitPkts = _PxmTC2AcPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 11),
    _PxmTC2AcPmQueueingTransmitPkts_Type()
)
pxmTC2AcPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmQueueingTransmitPkts.setStatus("current")
_PxmTC2AcPmQueueingTransmitOctets_Type = Counter64
_PxmTC2AcPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC2AcPmQueueingTransmitOctets = _PxmTC2AcPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 2, 1, 12),
    _PxmTC2AcPmQueueingTransmitOctets_Type()
)
pxmTC2AcPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC2AcPmQueueingTransmitOctets.setStatus("current")
_PxmTC4AcPmTable_Object = MibTable
pxmTC4AcPmTable = _PxmTC4AcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3)
)
if mibBuilder.loadTexts:
    pxmTC4AcPmTable.setStatus("current")
_PxmTC4AcPmEntry_Object = MibTableRow
pxmTC4AcPmEntry = _PxmTC4AcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1)
)
pxmTC4AcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmSampleDuration"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC4AcPmEntry.setStatus("current")


class _PxmTC4AcPmTimestamp_Type(Integer32):
    """Custom type pxmTC4AcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC4AcPmTimestamp_Type.__name__ = "Integer32"
_PxmTC4AcPmTimestamp_Object = MibTableColumn
pxmTC4AcPmTimestamp = _PxmTC4AcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 1),
    _PxmTC4AcPmTimestamp_Type()
)
pxmTC4AcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC4AcPmTimestamp.setStatus("current")


class _PxmTC4AcPmSampleDuration_Type(Integer32):
    """Custom type pxmTC4AcPmSampleDuration based on Integer32"""
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


_PxmTC4AcPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC4AcPmSampleDuration_Object = MibTableColumn
pxmTC4AcPmSampleDuration = _PxmTC4AcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 2),
    _PxmTC4AcPmSampleDuration_Type()
)
pxmTC4AcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC4AcPmSampleDuration.setStatus("current")
_PxmTC4AcPmValidity_Type = TruthValue
_PxmTC4AcPmValidity_Object = MibTableColumn
pxmTC4AcPmValidity = _PxmTC4AcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 3),
    _PxmTC4AcPmValidity_Type()
)
pxmTC4AcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmValidity.setStatus("current")
_PxmTC4AcPmTCNum_Type = Integer32
_PxmTC4AcPmTCNum_Object = MibTableColumn
pxmTC4AcPmTCNum = _PxmTC4AcPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 4),
    _PxmTC4AcPmTCNum_Type()
)
pxmTC4AcPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmTCNum.setStatus("current")
_PxmTC4AcPmQueueingDiscardOctets_Type = Counter64
_PxmTC4AcPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC4AcPmQueueingDiscardOctets = _PxmTC4AcPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 5),
    _PxmTC4AcPmQueueingDiscardOctets_Type()
)
pxmTC4AcPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmQueueingDiscardOctets.setStatus("current")
_PxmTC4AcPmQueueingDiscardPkts_Type = Integer32
_PxmTC4AcPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC4AcPmQueueingDiscardPkts = _PxmTC4AcPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 6),
    _PxmTC4AcPmQueueingDiscardPkts_Type()
)
pxmTC4AcPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmQueueingDiscardPkts.setStatus("current")
_PxmTC4AcPmRandomGreenDropPkts_Type = Counter64
_PxmTC4AcPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC4AcPmRandomGreenDropPkts = _PxmTC4AcPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 7),
    _PxmTC4AcPmRandomGreenDropPkts_Type()
)
pxmTC4AcPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRandomGreenDropPkts.setStatus("current")
_PxmTC4AcPmRandomGreenDropOctets_Type = Counter64
_PxmTC4AcPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC4AcPmRandomGreenDropOctets = _PxmTC4AcPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 8),
    _PxmTC4AcPmRandomGreenDropOctets_Type()
)
pxmTC4AcPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRandomGreenDropOctets.setStatus("current")
_PxmTC4AcPmRandomYellowDropPkts_Type = Counter64
_PxmTC4AcPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC4AcPmRandomYellowDropPkts = _PxmTC4AcPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 9),
    _PxmTC4AcPmRandomYellowDropPkts_Type()
)
pxmTC4AcPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRandomYellowDropPkts.setStatus("current")
_PxmTC4AcPmRandomYellowDropOctets_Type = Counter64
_PxmTC4AcPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC4AcPmRandomYellowDropOctets = _PxmTC4AcPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 10),
    _PxmTC4AcPmRandomYellowDropOctets_Type()
)
pxmTC4AcPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmRandomYellowDropOctets.setStatus("current")
_PxmTC4AcPmQueueingTransmitPkts_Type = Counter64
_PxmTC4AcPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC4AcPmQueueingTransmitPkts = _PxmTC4AcPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 11),
    _PxmTC4AcPmQueueingTransmitPkts_Type()
)
pxmTC4AcPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmQueueingTransmitPkts.setStatus("current")
_PxmTC4AcPmQueueingTransmitOctets_Type = Counter64
_PxmTC4AcPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC4AcPmQueueingTransmitOctets = _PxmTC4AcPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 3, 1, 12),
    _PxmTC4AcPmQueueingTransmitOctets_Type()
)
pxmTC4AcPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC4AcPmQueueingTransmitOctets.setStatus("current")
_PxmTC6AcPmTable_Object = MibTable
pxmTC6AcPmTable = _PxmTC6AcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4)
)
if mibBuilder.loadTexts:
    pxmTC6AcPmTable.setStatus("current")
_PxmTC6AcPmEntry_Object = MibTableRow
pxmTC6AcPmEntry = _PxmTC6AcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1)
)
pxmTC6AcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmSampleDuration"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC6AcPmEntry.setStatus("current")


class _PxmTC6AcPmTimestamp_Type(Integer32):
    """Custom type pxmTC6AcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC6AcPmTimestamp_Type.__name__ = "Integer32"
_PxmTC6AcPmTimestamp_Object = MibTableColumn
pxmTC6AcPmTimestamp = _PxmTC6AcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 1),
    _PxmTC6AcPmTimestamp_Type()
)
pxmTC6AcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC6AcPmTimestamp.setStatus("current")


class _PxmTC6AcPmSampleDuration_Type(Integer32):
    """Custom type pxmTC6AcPmSampleDuration based on Integer32"""
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


_PxmTC6AcPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC6AcPmSampleDuration_Object = MibTableColumn
pxmTC6AcPmSampleDuration = _PxmTC6AcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 2),
    _PxmTC6AcPmSampleDuration_Type()
)
pxmTC6AcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC6AcPmSampleDuration.setStatus("current")
_PxmTC6AcPmValidity_Type = TruthValue
_PxmTC6AcPmValidity_Object = MibTableColumn
pxmTC6AcPmValidity = _PxmTC6AcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 3),
    _PxmTC6AcPmValidity_Type()
)
pxmTC6AcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmValidity.setStatus("current")
_PxmTC6AcPmTCNum_Type = Integer32
_PxmTC6AcPmTCNum_Object = MibTableColumn
pxmTC6AcPmTCNum = _PxmTC6AcPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 4),
    _PxmTC6AcPmTCNum_Type()
)
pxmTC6AcPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmTCNum.setStatus("current")
_PxmTC6AcPmQueueingDiscardOctets_Type = Counter64
_PxmTC6AcPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC6AcPmQueueingDiscardOctets = _PxmTC6AcPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 5),
    _PxmTC6AcPmQueueingDiscardOctets_Type()
)
pxmTC6AcPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmQueueingDiscardOctets.setStatus("current")
_PxmTC6AcPmQueueingDiscardPkts_Type = Integer32
_PxmTC6AcPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC6AcPmQueueingDiscardPkts = _PxmTC6AcPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 6),
    _PxmTC6AcPmQueueingDiscardPkts_Type()
)
pxmTC6AcPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmQueueingDiscardPkts.setStatus("current")
_PxmTC6AcPmRandomGreenDropPkts_Type = Counter64
_PxmTC6AcPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC6AcPmRandomGreenDropPkts = _PxmTC6AcPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 7),
    _PxmTC6AcPmRandomGreenDropPkts_Type()
)
pxmTC6AcPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRandomGreenDropPkts.setStatus("current")
_PxmTC6AcPmRandomGreenDropOctets_Type = Counter64
_PxmTC6AcPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC6AcPmRandomGreenDropOctets = _PxmTC6AcPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 8),
    _PxmTC6AcPmRandomGreenDropOctets_Type()
)
pxmTC6AcPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRandomGreenDropOctets.setStatus("current")
_PxmTC6AcPmRandomYellowDropPkts_Type = Counter64
_PxmTC6AcPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC6AcPmRandomYellowDropPkts = _PxmTC6AcPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 9),
    _PxmTC6AcPmRandomYellowDropPkts_Type()
)
pxmTC6AcPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRandomYellowDropPkts.setStatus("current")
_PxmTC6AcPmRandomYellowDropOctets_Type = Counter64
_PxmTC6AcPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC6AcPmRandomYellowDropOctets = _PxmTC6AcPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 10),
    _PxmTC6AcPmRandomYellowDropOctets_Type()
)
pxmTC6AcPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmRandomYellowDropOctets.setStatus("current")
_PxmTC6AcPmQueueingTransmitPkts_Type = Counter64
_PxmTC6AcPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC6AcPmQueueingTransmitPkts = _PxmTC6AcPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 11),
    _PxmTC6AcPmQueueingTransmitPkts_Type()
)
pxmTC6AcPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmQueueingTransmitPkts.setStatus("current")
_PxmTC6AcPmQueueingTransmitOctets_Type = Counter64
_PxmTC6AcPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC6AcPmQueueingTransmitOctets = _PxmTC6AcPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 4, 1, 12),
    _PxmTC6AcPmQueueingTransmitOctets_Type()
)
pxmTC6AcPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC6AcPmQueueingTransmitOctets.setStatus("current")
_PxmTC7AcPmTable_Object = MibTable
pxmTC7AcPmTable = _PxmTC7AcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5)
)
if mibBuilder.loadTexts:
    pxmTC7AcPmTable.setStatus("current")
_PxmTC7AcPmEntry_Object = MibTableRow
pxmTC7AcPmEntry = _PxmTC7AcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1)
)
pxmTC7AcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmSampleDuration"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTC7AcPmEntry.setStatus("current")


class _PxmTC7AcPmTimestamp_Type(Integer32):
    """Custom type pxmTC7AcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTC7AcPmTimestamp_Type.__name__ = "Integer32"
_PxmTC7AcPmTimestamp_Object = MibTableColumn
pxmTC7AcPmTimestamp = _PxmTC7AcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 1),
    _PxmTC7AcPmTimestamp_Type()
)
pxmTC7AcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC7AcPmTimestamp.setStatus("current")


class _PxmTC7AcPmSampleDuration_Type(Integer32):
    """Custom type pxmTC7AcPmSampleDuration based on Integer32"""
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


_PxmTC7AcPmSampleDuration_Type.__name__ = "Integer32"
_PxmTC7AcPmSampleDuration_Object = MibTableColumn
pxmTC7AcPmSampleDuration = _PxmTC7AcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 2),
    _PxmTC7AcPmSampleDuration_Type()
)
pxmTC7AcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTC7AcPmSampleDuration.setStatus("current")
_PxmTC7AcPmValidity_Type = TruthValue
_PxmTC7AcPmValidity_Object = MibTableColumn
pxmTC7AcPmValidity = _PxmTC7AcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 3),
    _PxmTC7AcPmValidity_Type()
)
pxmTC7AcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmValidity.setStatus("current")
_PxmTC7AcPmTCNum_Type = Integer32
_PxmTC7AcPmTCNum_Object = MibTableColumn
pxmTC7AcPmTCNum = _PxmTC7AcPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 4),
    _PxmTC7AcPmTCNum_Type()
)
pxmTC7AcPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmTCNum.setStatus("current")
_PxmTC7AcPmQueueingDiscardOctets_Type = Counter64
_PxmTC7AcPmQueueingDiscardOctets_Object = MibTableColumn
pxmTC7AcPmQueueingDiscardOctets = _PxmTC7AcPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 5),
    _PxmTC7AcPmQueueingDiscardOctets_Type()
)
pxmTC7AcPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmQueueingDiscardOctets.setStatus("current")
_PxmTC7AcPmQueueingDiscardPkts_Type = Integer32
_PxmTC7AcPmQueueingDiscardPkts_Object = MibTableColumn
pxmTC7AcPmQueueingDiscardPkts = _PxmTC7AcPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 6),
    _PxmTC7AcPmQueueingDiscardPkts_Type()
)
pxmTC7AcPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmQueueingDiscardPkts.setStatus("current")
_PxmTC7AcPmRandomGreenDropPkts_Type = Counter64
_PxmTC7AcPmRandomGreenDropPkts_Object = MibTableColumn
pxmTC7AcPmRandomGreenDropPkts = _PxmTC7AcPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 7),
    _PxmTC7AcPmRandomGreenDropPkts_Type()
)
pxmTC7AcPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRandomGreenDropPkts.setStatus("current")
_PxmTC7AcPmRandomGreenDropOctets_Type = Counter64
_PxmTC7AcPmRandomGreenDropOctets_Object = MibTableColumn
pxmTC7AcPmRandomGreenDropOctets = _PxmTC7AcPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 8),
    _PxmTC7AcPmRandomGreenDropOctets_Type()
)
pxmTC7AcPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRandomGreenDropOctets.setStatus("current")
_PxmTC7AcPmRandomYellowDropPkts_Type = Counter64
_PxmTC7AcPmRandomYellowDropPkts_Object = MibTableColumn
pxmTC7AcPmRandomYellowDropPkts = _PxmTC7AcPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 9),
    _PxmTC7AcPmRandomYellowDropPkts_Type()
)
pxmTC7AcPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRandomYellowDropPkts.setStatus("current")
_PxmTC7AcPmRandomYellowDropOctets_Type = Counter64
_PxmTC7AcPmRandomYellowDropOctets_Object = MibTableColumn
pxmTC7AcPmRandomYellowDropOctets = _PxmTC7AcPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 10),
    _PxmTC7AcPmRandomYellowDropOctets_Type()
)
pxmTC7AcPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmRandomYellowDropOctets.setStatus("current")
_PxmTC7AcPmQueueingTransmitPkts_Type = Counter64
_PxmTC7AcPmQueueingTransmitPkts_Object = MibTableColumn
pxmTC7AcPmQueueingTransmitPkts = _PxmTC7AcPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 11),
    _PxmTC7AcPmQueueingTransmitPkts_Type()
)
pxmTC7AcPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmQueueingTransmitPkts.setStatus("current")
_PxmTC7AcPmQueueingTransmitOctets_Type = Counter64
_PxmTC7AcPmQueueingTransmitOctets_Object = MibTableColumn
pxmTC7AcPmQueueingTransmitOctets = _PxmTC7AcPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 5, 1, 12),
    _PxmTC7AcPmQueueingTransmitOctets_Type()
)
pxmTC7AcPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTC7AcPmQueueingTransmitOctets.setStatus("current")
_PxmTCANYAcPmTable_Object = MibTable
pxmTCANYAcPmTable = _PxmTCANYAcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6)
)
if mibBuilder.loadTexts:
    pxmTCANYAcPmTable.setStatus("current")
_PxmTCANYAcPmEntry_Object = MibTableRow
pxmTCANYAcPmEntry = _PxmTCANYAcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1)
)
pxmTCANYAcPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmSampleDuration"),
    (0, "INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmTCANYAcPmEntry.setStatus("current")


class _PxmTCANYAcPmTimestamp_Type(Integer32):
    """Custom type pxmTCANYAcPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmTCANYAcPmTimestamp_Type.__name__ = "Integer32"
_PxmTCANYAcPmTimestamp_Object = MibTableColumn
pxmTCANYAcPmTimestamp = _PxmTCANYAcPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 1),
    _PxmTCANYAcPmTimestamp_Type()
)
pxmTCANYAcPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTCANYAcPmTimestamp.setStatus("current")


class _PxmTCANYAcPmSampleDuration_Type(Integer32):
    """Custom type pxmTCANYAcPmSampleDuration based on Integer32"""
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


_PxmTCANYAcPmSampleDuration_Type.__name__ = "Integer32"
_PxmTCANYAcPmSampleDuration_Object = MibTableColumn
pxmTCANYAcPmSampleDuration = _PxmTCANYAcPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 2),
    _PxmTCANYAcPmSampleDuration_Type()
)
pxmTCANYAcPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmTCANYAcPmSampleDuration.setStatus("current")
_PxmTCANYAcPmValidity_Type = TruthValue
_PxmTCANYAcPmValidity_Object = MibTableColumn
pxmTCANYAcPmValidity = _PxmTCANYAcPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 3),
    _PxmTCANYAcPmValidity_Type()
)
pxmTCANYAcPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmValidity.setStatus("current")
_PxmTCANYAcPmTCNum_Type = Integer32
_PxmTCANYAcPmTCNum_Object = MibTableColumn
pxmTCANYAcPmTCNum = _PxmTCANYAcPmTCNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 4),
    _PxmTCANYAcPmTCNum_Type()
)
pxmTCANYAcPmTCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmTCNum.setStatus("current")
_PxmTCANYAcPmQueueingDiscardOctets_Type = Counter64
_PxmTCANYAcPmQueueingDiscardOctets_Object = MibTableColumn
pxmTCANYAcPmQueueingDiscardOctets = _PxmTCANYAcPmQueueingDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 5),
    _PxmTCANYAcPmQueueingDiscardOctets_Type()
)
pxmTCANYAcPmQueueingDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmQueueingDiscardOctets.setStatus("current")
_PxmTCANYAcPmQueueingDiscardPkts_Type = Integer32
_PxmTCANYAcPmQueueingDiscardPkts_Object = MibTableColumn
pxmTCANYAcPmQueueingDiscardPkts = _PxmTCANYAcPmQueueingDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 6),
    _PxmTCANYAcPmQueueingDiscardPkts_Type()
)
pxmTCANYAcPmQueueingDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmQueueingDiscardPkts.setStatus("current")
_PxmTCANYAcPmRandomGreenDropPkts_Type = Counter64
_PxmTCANYAcPmRandomGreenDropPkts_Object = MibTableColumn
pxmTCANYAcPmRandomGreenDropPkts = _PxmTCANYAcPmRandomGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 7),
    _PxmTCANYAcPmRandomGreenDropPkts_Type()
)
pxmTCANYAcPmRandomGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRandomGreenDropPkts.setStatus("current")
_PxmTCANYAcPmRandomGreenDropOctets_Type = Counter64
_PxmTCANYAcPmRandomGreenDropOctets_Object = MibTableColumn
pxmTCANYAcPmRandomGreenDropOctets = _PxmTCANYAcPmRandomGreenDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 8),
    _PxmTCANYAcPmRandomGreenDropOctets_Type()
)
pxmTCANYAcPmRandomGreenDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRandomGreenDropOctets.setStatus("current")
_PxmTCANYAcPmRandomYellowDropPkts_Type = Counter64
_PxmTCANYAcPmRandomYellowDropPkts_Object = MibTableColumn
pxmTCANYAcPmRandomYellowDropPkts = _PxmTCANYAcPmRandomYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 9),
    _PxmTCANYAcPmRandomYellowDropPkts_Type()
)
pxmTCANYAcPmRandomYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRandomYellowDropPkts.setStatus("current")
_PxmTCANYAcPmRandomYellowDropOctets_Type = Counter64
_PxmTCANYAcPmRandomYellowDropOctets_Object = MibTableColumn
pxmTCANYAcPmRandomYellowDropOctets = _PxmTCANYAcPmRandomYellowDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 10),
    _PxmTCANYAcPmRandomYellowDropOctets_Type()
)
pxmTCANYAcPmRandomYellowDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmRandomYellowDropOctets.setStatus("current")
_PxmTCANYAcPmQueueingTransmitPkts_Type = Counter64
_PxmTCANYAcPmQueueingTransmitPkts_Object = MibTableColumn
pxmTCANYAcPmQueueingTransmitPkts = _PxmTCANYAcPmQueueingTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 11),
    _PxmTCANYAcPmQueueingTransmitPkts_Type()
)
pxmTCANYAcPmQueueingTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmQueueingTransmitPkts.setStatus("current")
_PxmTCANYAcPmQueueingTransmitOctets_Type = Counter64
_PxmTCANYAcPmQueueingTransmitOctets_Object = MibTableColumn
pxmTCANYAcPmQueueingTransmitOctets = _PxmTCANYAcPmQueueingTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 3, 2, 6, 1, 12),
    _PxmTCANYAcPmQueueingTransmitOctets_Type()
)
pxmTCANYAcPmQueueingTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTCANYAcPmQueueingTransmitOctets.setStatus("current")
_PxmAcPmConformance_ObjectIdentity = ObjectIdentity
pxmAcPmConformance = _PxmAcPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4)
)
_PxmAcPmCompliances_ObjectIdentity = ObjectIdentity
pxmAcPmCompliances = _PxmAcPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 1)
)
_PxmAcPmGroups_ObjectIdentity = ObjectIdentity
pxmAcPmGroups = _PxmAcPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2)
)

# Managed Objects groups

pxmAcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 1)
)
pxmAcPmGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmAcPmValidity"),
        ("INFINERA-PM-PXMAC-MIB", "pxmAcPmRxPackets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmAcPmRxOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmAcPmTxPackets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmAcPmTxOctets"))
)
if mibBuilder.loadTexts:
    pxmAcPmGroup.setStatus("current")

pxmAcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 2)
)
pxmAcPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmAcPmRealRxPackets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmAcPmRealRxOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmAcPmRealTxPackets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmAcPmRealTxOctets"))
)
if mibBuilder.loadTexts:
    pxmAcPmRealGroup.setStatus("current")

pxmBwpAcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 3)
)
pxmBwpAcPmGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmValidity"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmPolicerConformedPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmPolicerConformedOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmPolicerExceededPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmPolicerExceededOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmPolicerViolatedPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmPolicerViolatedOctets"))
)
if mibBuilder.loadTexts:
    pxmBwpAcPmGroup.setStatus("current")

pxmBwpAcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 4)
)
pxmBwpAcPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmRealPolicerConformedPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmRealPolicerConformedOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmRealPolicerExceededPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmRealPolicerExceededOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmRealPolicerViolatedPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmBwpAcPmRealPolicerViolatedOctets"))
)
if mibBuilder.loadTexts:
    pxmBwpAcPmRealGroup.setStatus("current")

pxmTC0AcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 5)
)
pxmTC0AcPmGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmValidity"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC0AcPmGroup.setStatus("current")

pxmTC0AcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 6)
)
pxmTC0AcPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC0AcPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC0AcPmRealGroup.setStatus("current")

pxmTC2AcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 7)
)
pxmTC2AcPmGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmValidity"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC2AcPmGroup.setStatus("current")

pxmTC2AcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 8)
)
pxmTC2AcPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC2AcPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC2AcPmRealGroup.setStatus("current")

pxmTC4AcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 9)
)
pxmTC4AcPmGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmValidity"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC4AcPmGroup.setStatus("current")

pxmTC4AcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 10)
)
pxmTC4AcPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC4AcPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC4AcPmRealGroup.setStatus("current")

pxmTC6AcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 11)
)
pxmTC6AcPmGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmValidity"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC6AcPmGroup.setStatus("current")

pxmTC6AcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 12)
)
pxmTC6AcPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC6AcPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC6AcPmRealGroup.setStatus("current")

pxmTC7AcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 13)
)
pxmTC7AcPmGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmValidity"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTC7AcPmGroup.setStatus("current")

pxmTC7AcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 14)
)
pxmTC7AcPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTC7AcPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTC7AcPmRealGroup.setStatus("current")

pxmTCANYAcPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 15)
)
pxmTCANYAcPmGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmValidity"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmQueueingTransmitOctets"))
)
if mibBuilder.loadTexts:
    pxmTCANYAcPmGroup.setStatus("current")

pxmTCANYAcPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 2, 16)
)
pxmTCANYAcPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealTCNum"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealTDQueuingCurrentQDepth"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealQueueingDiscardOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealQueueingDiscardPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealRandomGreenDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealRandomGreenDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealRandomYellowDropPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealRandomYellowDropOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealQueueingTransmitPkts"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealQueueingTransmitOctets"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealQueueingMeanQSizeUnit"),
        ("INFINERA-PM-PXMAC-MIB", "pxmTCANYAcPmRealMeanQSize"))
)
if mibBuilder.loadTexts:
    pxmTCANYAcPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmAcPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 1, 1)
)
pxmAcPmCompliance.setObjects(
    ("INFINERA-PM-PXMAC-MIB", "pxmAcPmGroup")
)
if mibBuilder.loadTexts:
    pxmAcPmCompliance.setStatus(
        "current"
    )

pxmAcPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 95, 4, 1, 2)
)
pxmAcPmRealCompliance.setObjects(
    ("INFINERA-PM-PXMAC-MIB", "pxmAcPmRealGroup")
)
if mibBuilder.loadTexts:
    pxmAcPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-PXMAC-MIB",
    **{"pxmAcPmMIB": pxmAcPmMIB,
       "pxmAcRmonPm": pxmAcRmonPm,
       "pxmAcPmRealTable": pxmAcPmRealTable,
       "pxmAcPmRealEntry": pxmAcPmRealEntry,
       "pxmAcPmRealRxPackets": pxmAcPmRealRxPackets,
       "pxmAcPmRealRxOctets": pxmAcPmRealRxOctets,
       "pxmAcPmRealTxPackets": pxmAcPmRealTxPackets,
       "pxmAcPmRealTxOctets": pxmAcPmRealTxOctets,
       "pxmAcPmTable": pxmAcPmTable,
       "pxmAcPmEntry": pxmAcPmEntry,
       "pxmAcPmTimestamp": pxmAcPmTimestamp,
       "pxmAcPmSampleDuration": pxmAcPmSampleDuration,
       "pxmAcPmValidity": pxmAcPmValidity,
       "pxmAcPmRxPackets": pxmAcPmRxPackets,
       "pxmAcPmRxOctets": pxmAcPmRxOctets,
       "pxmAcPmTxPackets": pxmAcPmTxPackets,
       "pxmAcPmTxOctets": pxmAcPmTxOctets,
       "pxmAcBwpPm": pxmAcBwpPm,
       "pxmBwpAcPmRealTable": pxmBwpAcPmRealTable,
       "pxmBwpAcPmRealEntry": pxmBwpAcPmRealEntry,
       "pxmBwpAcPmRealPolicerConformedPkts": pxmBwpAcPmRealPolicerConformedPkts,
       "pxmBwpAcPmRealPolicerConformedOctets": pxmBwpAcPmRealPolicerConformedOctets,
       "pxmBwpAcPmRealPolicerExceededPkts": pxmBwpAcPmRealPolicerExceededPkts,
       "pxmBwpAcPmRealPolicerExceededOctets": pxmBwpAcPmRealPolicerExceededOctets,
       "pxmBwpAcPmRealPolicerViolatedPkts": pxmBwpAcPmRealPolicerViolatedPkts,
       "pxmBwpAcPmRealPolicerViolatedOctets": pxmBwpAcPmRealPolicerViolatedOctets,
       "pxmBwpAcPmTable": pxmBwpAcPmTable,
       "pxmBwpAcPmEntry": pxmBwpAcPmEntry,
       "pxmBwpAcPmTimestamp": pxmBwpAcPmTimestamp,
       "pxmBwpAcPmSampleDuration": pxmBwpAcPmSampleDuration,
       "pxmBwpAcPmValidity": pxmBwpAcPmValidity,
       "pxmBwpAcPmPolicerConformedPkts": pxmBwpAcPmPolicerConformedPkts,
       "pxmBwpAcPmPolicerConformedOctets": pxmBwpAcPmPolicerConformedOctets,
       "pxmBwpAcPmPolicerExceededPkts": pxmBwpAcPmPolicerExceededPkts,
       "pxmBwpAcPmPolicerExceededOctets": pxmBwpAcPmPolicerExceededOctets,
       "pxmBwpAcPmPolicerViolatedPkts": pxmBwpAcPmPolicerViolatedPkts,
       "pxmBwpAcPmPolicerViolatedOctets": pxmBwpAcPmPolicerViolatedOctets,
       "pxmCmAcPmObjects": pxmCmAcPmObjects,
       "pxmCmAcRealPm": pxmCmAcRealPm,
       "pxmTC0AcPmRealTable": pxmTC0AcPmRealTable,
       "pxmTC0AcPmRealEntry": pxmTC0AcPmRealEntry,
       "pxmTC0AcPmRealTCNum": pxmTC0AcPmRealTCNum,
       "pxmTC0AcPmRealTDQueuingCurrentQDepth": pxmTC0AcPmRealTDQueuingCurrentQDepth,
       "pxmTC0AcPmRealQueueingDiscardOctets": pxmTC0AcPmRealQueueingDiscardOctets,
       "pxmTC0AcPmRealQueueingDiscardPkts": pxmTC0AcPmRealQueueingDiscardPkts,
       "pxmTC0AcPmRealRandomGreenDropPkts": pxmTC0AcPmRealRandomGreenDropPkts,
       "pxmTC0AcPmRealRandomGreenDropOctets": pxmTC0AcPmRealRandomGreenDropOctets,
       "pxmTC0AcPmRealRandomYellowDropPkts": pxmTC0AcPmRealRandomYellowDropPkts,
       "pxmTC0AcPmRealRandomYellowDropOctets": pxmTC0AcPmRealRandomYellowDropOctets,
       "pxmTC0AcPmRealQueueingTransmitPkts": pxmTC0AcPmRealQueueingTransmitPkts,
       "pxmTC0AcPmRealQueueingTransmitOctets": pxmTC0AcPmRealQueueingTransmitOctets,
       "pxmTC0AcPmRealQueueingMeanQSizeUnit": pxmTC0AcPmRealQueueingMeanQSizeUnit,
       "pxmTC0AcPmRealMeanQSize": pxmTC0AcPmRealMeanQSize,
       "pxmTC2AcPmRealTable": pxmTC2AcPmRealTable,
       "pxmTC2AcPmRealEntry": pxmTC2AcPmRealEntry,
       "pxmTC2AcPmRealTCNum": pxmTC2AcPmRealTCNum,
       "pxmTC2AcPmRealTDQueuingCurrentQDepth": pxmTC2AcPmRealTDQueuingCurrentQDepth,
       "pxmTC2AcPmRealQueueingDiscardOctets": pxmTC2AcPmRealQueueingDiscardOctets,
       "pxmTC2AcPmRealQueueingDiscardPkts": pxmTC2AcPmRealQueueingDiscardPkts,
       "pxmTC2AcPmRealRandomGreenDropPkts": pxmTC2AcPmRealRandomGreenDropPkts,
       "pxmTC2AcPmRealRandomGreenDropOctets": pxmTC2AcPmRealRandomGreenDropOctets,
       "pxmTC2AcPmRealRandomYellowDropPkts": pxmTC2AcPmRealRandomYellowDropPkts,
       "pxmTC2AcPmRealRandomYellowDropOctets": pxmTC2AcPmRealRandomYellowDropOctets,
       "pxmTC2AcPmRealQueueingTransmitPkts": pxmTC2AcPmRealQueueingTransmitPkts,
       "pxmTC2AcPmRealQueueingTransmitOctets": pxmTC2AcPmRealQueueingTransmitOctets,
       "pxmTC2AcPmRealQueueingMeanQSizeUnit": pxmTC2AcPmRealQueueingMeanQSizeUnit,
       "pxmTC2AcPmRealMeanQSize": pxmTC2AcPmRealMeanQSize,
       "pxmTC4AcPmRealTable": pxmTC4AcPmRealTable,
       "pxmTC4AcPmRealEntry": pxmTC4AcPmRealEntry,
       "pxmTC4AcPmRealTCNum": pxmTC4AcPmRealTCNum,
       "pxmTC4AcPmRealTDQueuingCurrentQDepth": pxmTC4AcPmRealTDQueuingCurrentQDepth,
       "pxmTC4AcPmRealQueueingDiscardOctets": pxmTC4AcPmRealQueueingDiscardOctets,
       "pxmTC4AcPmRealQueueingDiscardPkts": pxmTC4AcPmRealQueueingDiscardPkts,
       "pxmTC4AcPmRealRandomGreenDropPkts": pxmTC4AcPmRealRandomGreenDropPkts,
       "pxmTC4AcPmRealRandomGreenDropOctets": pxmTC4AcPmRealRandomGreenDropOctets,
       "pxmTC4AcPmRealRandomYellowDropPkts": pxmTC4AcPmRealRandomYellowDropPkts,
       "pxmTC4AcPmRealRandomYellowDropOctets": pxmTC4AcPmRealRandomYellowDropOctets,
       "pxmTC4AcPmRealQueueingTransmitPkts": pxmTC4AcPmRealQueueingTransmitPkts,
       "pxmTC4AcPmRealQueueingTransmitOctets": pxmTC4AcPmRealQueueingTransmitOctets,
       "pxmTC4AcPmRealQueueingMeanQSizeUnit": pxmTC4AcPmRealQueueingMeanQSizeUnit,
       "pxmTC4AcPmRealMeanQSize": pxmTC4AcPmRealMeanQSize,
       "pxmTC6AcPmRealTable": pxmTC6AcPmRealTable,
       "pxmTC6AcPmRealEntry": pxmTC6AcPmRealEntry,
       "pxmTC6AcPmRealTCNum": pxmTC6AcPmRealTCNum,
       "pxmTC6AcPmRealTDQueuingCurrentQDepth": pxmTC6AcPmRealTDQueuingCurrentQDepth,
       "pxmTC6AcPmRealQueueingDiscardOctets": pxmTC6AcPmRealQueueingDiscardOctets,
       "pxmTC6AcPmRealQueueingDiscardPkts": pxmTC6AcPmRealQueueingDiscardPkts,
       "pxmTC6AcPmRealRandomGreenDropPkts": pxmTC6AcPmRealRandomGreenDropPkts,
       "pxmTC6AcPmRealRandomGreenDropOctets": pxmTC6AcPmRealRandomGreenDropOctets,
       "pxmTC6AcPmRealRandomYellowDropPkts": pxmTC6AcPmRealRandomYellowDropPkts,
       "pxmTC6AcPmRealRandomYellowDropOctets": pxmTC6AcPmRealRandomYellowDropOctets,
       "pxmTC6AcPmRealQueueingTransmitPkts": pxmTC6AcPmRealQueueingTransmitPkts,
       "pxmTC6AcPmRealQueueingTransmitOctets": pxmTC6AcPmRealQueueingTransmitOctets,
       "pxmTC6AcPmRealQueueingMeanQSizeUnit": pxmTC6AcPmRealQueueingMeanQSizeUnit,
       "pxmTC6AcPmRealMeanQSize": pxmTC6AcPmRealMeanQSize,
       "pxmTC7AcPmRealTable": pxmTC7AcPmRealTable,
       "pxmTC7AcPmRealEntry": pxmTC7AcPmRealEntry,
       "pxmTC7AcPmRealTCNum": pxmTC7AcPmRealTCNum,
       "pxmTC7AcPmRealTDQueuingCurrentQDepth": pxmTC7AcPmRealTDQueuingCurrentQDepth,
       "pxmTC7AcPmRealQueueingDiscardOctets": pxmTC7AcPmRealQueueingDiscardOctets,
       "pxmTC7AcPmRealQueueingDiscardPkts": pxmTC7AcPmRealQueueingDiscardPkts,
       "pxmTC7AcPmRealRandomGreenDropPkts": pxmTC7AcPmRealRandomGreenDropPkts,
       "pxmTC7AcPmRealRandomGreenDropOctets": pxmTC7AcPmRealRandomGreenDropOctets,
       "pxmTC7AcPmRealRandomYellowDropPkts": pxmTC7AcPmRealRandomYellowDropPkts,
       "pxmTC7AcPmRealRandomYellowDropOctets": pxmTC7AcPmRealRandomYellowDropOctets,
       "pxmTC7AcPmRealQueueingTransmitPkts": pxmTC7AcPmRealQueueingTransmitPkts,
       "pxmTC7AcPmRealQueueingTransmitOctets": pxmTC7AcPmRealQueueingTransmitOctets,
       "pxmTC7AcPmRealQueueingMeanQSizeUnit": pxmTC7AcPmRealQueueingMeanQSizeUnit,
       "pxmTC7AcPmRealMeanQSize": pxmTC7AcPmRealMeanQSize,
       "pxmTCANYAcPmRealTable": pxmTCANYAcPmRealTable,
       "pxmTCANYAcPmRealEntry": pxmTCANYAcPmRealEntry,
       "pxmTCANYAcPmRealTCNum": pxmTCANYAcPmRealTCNum,
       "pxmTCANYAcPmRealTDQueuingCurrentQDepth": pxmTCANYAcPmRealTDQueuingCurrentQDepth,
       "pxmTCANYAcPmRealQueueingDiscardOctets": pxmTCANYAcPmRealQueueingDiscardOctets,
       "pxmTCANYAcPmRealQueueingDiscardPkts": pxmTCANYAcPmRealQueueingDiscardPkts,
       "pxmTCANYAcPmRealRandomGreenDropPkts": pxmTCANYAcPmRealRandomGreenDropPkts,
       "pxmTCANYAcPmRealRandomGreenDropOctets": pxmTCANYAcPmRealRandomGreenDropOctets,
       "pxmTCANYAcPmRealRandomYellowDropPkts": pxmTCANYAcPmRealRandomYellowDropPkts,
       "pxmTCANYAcPmRealRandomYellowDropOctets": pxmTCANYAcPmRealRandomYellowDropOctets,
       "pxmTCANYAcPmRealQueueingTransmitPkts": pxmTCANYAcPmRealQueueingTransmitPkts,
       "pxmTCANYAcPmRealQueueingTransmitOctets": pxmTCANYAcPmRealQueueingTransmitOctets,
       "pxmTCANYAcPmRealQueueingMeanQSizeUnit": pxmTCANYAcPmRealQueueingMeanQSizeUnit,
       "pxmTCANYAcPmRealMeanQSize": pxmTCANYAcPmRealMeanQSize,
       "pxmCmAcPm": pxmCmAcPm,
       "pxmTC0AcPmTable": pxmTC0AcPmTable,
       "pxmTC0AcPmEntry": pxmTC0AcPmEntry,
       "pxmTC0AcPmTimestamp": pxmTC0AcPmTimestamp,
       "pxmTC0AcPmSampleDuration": pxmTC0AcPmSampleDuration,
       "pxmTC0AcPmValidity": pxmTC0AcPmValidity,
       "pxmTC0AcPmTCNum": pxmTC0AcPmTCNum,
       "pxmTC0AcPmQueueingDiscardOctets": pxmTC0AcPmQueueingDiscardOctets,
       "pxmTC0AcPmQueueingDiscardPkts": pxmTC0AcPmQueueingDiscardPkts,
       "pxmTC0AcPmRandomGreenDropPkts": pxmTC0AcPmRandomGreenDropPkts,
       "pxmTC0AcPmRandomGreenDropOctets": pxmTC0AcPmRandomGreenDropOctets,
       "pxmTC0AcPmRandomYellowDropPkts": pxmTC0AcPmRandomYellowDropPkts,
       "pxmTC0AcPmRandomYellowDropOctets": pxmTC0AcPmRandomYellowDropOctets,
       "pxmTC0AcPmQueueingTransmitPkts": pxmTC0AcPmQueueingTransmitPkts,
       "pxmTC0AcPmQueueingTransmitOctets": pxmTC0AcPmQueueingTransmitOctets,
       "pxmTC2AcPmTable": pxmTC2AcPmTable,
       "pxmTC2AcPmEntry": pxmTC2AcPmEntry,
       "pxmTC2AcPmTimestamp": pxmTC2AcPmTimestamp,
       "pxmTC2AcPmSampleDuration": pxmTC2AcPmSampleDuration,
       "pxmTC2AcPmValidity": pxmTC2AcPmValidity,
       "pxmTC2AcPmTCNum": pxmTC2AcPmTCNum,
       "pxmTC2AcPmQueueingDiscardOctets": pxmTC2AcPmQueueingDiscardOctets,
       "pxmTC2AcPmQueueingDiscardPkts": pxmTC2AcPmQueueingDiscardPkts,
       "pxmTC2AcPmRandomGreenDropPkts": pxmTC2AcPmRandomGreenDropPkts,
       "pxmTC2AcPmRandomGreenDropOctets": pxmTC2AcPmRandomGreenDropOctets,
       "pxmTC2AcPmRandomYellowDropPkts": pxmTC2AcPmRandomYellowDropPkts,
       "pxmTC2AcPmRandomYellowDropOctets": pxmTC2AcPmRandomYellowDropOctets,
       "pxmTC2AcPmQueueingTransmitPkts": pxmTC2AcPmQueueingTransmitPkts,
       "pxmTC2AcPmQueueingTransmitOctets": pxmTC2AcPmQueueingTransmitOctets,
       "pxmTC4AcPmTable": pxmTC4AcPmTable,
       "pxmTC4AcPmEntry": pxmTC4AcPmEntry,
       "pxmTC4AcPmTimestamp": pxmTC4AcPmTimestamp,
       "pxmTC4AcPmSampleDuration": pxmTC4AcPmSampleDuration,
       "pxmTC4AcPmValidity": pxmTC4AcPmValidity,
       "pxmTC4AcPmTCNum": pxmTC4AcPmTCNum,
       "pxmTC4AcPmQueueingDiscardOctets": pxmTC4AcPmQueueingDiscardOctets,
       "pxmTC4AcPmQueueingDiscardPkts": pxmTC4AcPmQueueingDiscardPkts,
       "pxmTC4AcPmRandomGreenDropPkts": pxmTC4AcPmRandomGreenDropPkts,
       "pxmTC4AcPmRandomGreenDropOctets": pxmTC4AcPmRandomGreenDropOctets,
       "pxmTC4AcPmRandomYellowDropPkts": pxmTC4AcPmRandomYellowDropPkts,
       "pxmTC4AcPmRandomYellowDropOctets": pxmTC4AcPmRandomYellowDropOctets,
       "pxmTC4AcPmQueueingTransmitPkts": pxmTC4AcPmQueueingTransmitPkts,
       "pxmTC4AcPmQueueingTransmitOctets": pxmTC4AcPmQueueingTransmitOctets,
       "pxmTC6AcPmTable": pxmTC6AcPmTable,
       "pxmTC6AcPmEntry": pxmTC6AcPmEntry,
       "pxmTC6AcPmTimestamp": pxmTC6AcPmTimestamp,
       "pxmTC6AcPmSampleDuration": pxmTC6AcPmSampleDuration,
       "pxmTC6AcPmValidity": pxmTC6AcPmValidity,
       "pxmTC6AcPmTCNum": pxmTC6AcPmTCNum,
       "pxmTC6AcPmQueueingDiscardOctets": pxmTC6AcPmQueueingDiscardOctets,
       "pxmTC6AcPmQueueingDiscardPkts": pxmTC6AcPmQueueingDiscardPkts,
       "pxmTC6AcPmRandomGreenDropPkts": pxmTC6AcPmRandomGreenDropPkts,
       "pxmTC6AcPmRandomGreenDropOctets": pxmTC6AcPmRandomGreenDropOctets,
       "pxmTC6AcPmRandomYellowDropPkts": pxmTC6AcPmRandomYellowDropPkts,
       "pxmTC6AcPmRandomYellowDropOctets": pxmTC6AcPmRandomYellowDropOctets,
       "pxmTC6AcPmQueueingTransmitPkts": pxmTC6AcPmQueueingTransmitPkts,
       "pxmTC6AcPmQueueingTransmitOctets": pxmTC6AcPmQueueingTransmitOctets,
       "pxmTC7AcPmTable": pxmTC7AcPmTable,
       "pxmTC7AcPmEntry": pxmTC7AcPmEntry,
       "pxmTC7AcPmTimestamp": pxmTC7AcPmTimestamp,
       "pxmTC7AcPmSampleDuration": pxmTC7AcPmSampleDuration,
       "pxmTC7AcPmValidity": pxmTC7AcPmValidity,
       "pxmTC7AcPmTCNum": pxmTC7AcPmTCNum,
       "pxmTC7AcPmQueueingDiscardOctets": pxmTC7AcPmQueueingDiscardOctets,
       "pxmTC7AcPmQueueingDiscardPkts": pxmTC7AcPmQueueingDiscardPkts,
       "pxmTC7AcPmRandomGreenDropPkts": pxmTC7AcPmRandomGreenDropPkts,
       "pxmTC7AcPmRandomGreenDropOctets": pxmTC7AcPmRandomGreenDropOctets,
       "pxmTC7AcPmRandomYellowDropPkts": pxmTC7AcPmRandomYellowDropPkts,
       "pxmTC7AcPmRandomYellowDropOctets": pxmTC7AcPmRandomYellowDropOctets,
       "pxmTC7AcPmQueueingTransmitPkts": pxmTC7AcPmQueueingTransmitPkts,
       "pxmTC7AcPmQueueingTransmitOctets": pxmTC7AcPmQueueingTransmitOctets,
       "pxmTCANYAcPmTable": pxmTCANYAcPmTable,
       "pxmTCANYAcPmEntry": pxmTCANYAcPmEntry,
       "pxmTCANYAcPmTimestamp": pxmTCANYAcPmTimestamp,
       "pxmTCANYAcPmSampleDuration": pxmTCANYAcPmSampleDuration,
       "pxmTCANYAcPmValidity": pxmTCANYAcPmValidity,
       "pxmTCANYAcPmTCNum": pxmTCANYAcPmTCNum,
       "pxmTCANYAcPmQueueingDiscardOctets": pxmTCANYAcPmQueueingDiscardOctets,
       "pxmTCANYAcPmQueueingDiscardPkts": pxmTCANYAcPmQueueingDiscardPkts,
       "pxmTCANYAcPmRandomGreenDropPkts": pxmTCANYAcPmRandomGreenDropPkts,
       "pxmTCANYAcPmRandomGreenDropOctets": pxmTCANYAcPmRandomGreenDropOctets,
       "pxmTCANYAcPmRandomYellowDropPkts": pxmTCANYAcPmRandomYellowDropPkts,
       "pxmTCANYAcPmRandomYellowDropOctets": pxmTCANYAcPmRandomYellowDropOctets,
       "pxmTCANYAcPmQueueingTransmitPkts": pxmTCANYAcPmQueueingTransmitPkts,
       "pxmTCANYAcPmQueueingTransmitOctets": pxmTCANYAcPmQueueingTransmitOctets,
       "pxmAcPmConformance": pxmAcPmConformance,
       "pxmAcPmCompliances": pxmAcPmCompliances,
       "pxmAcPmCompliance": pxmAcPmCompliance,
       "pxmAcPmRealCompliance": pxmAcPmRealCompliance,
       "pxmAcPmGroups": pxmAcPmGroups,
       "pxmAcPmGroup": pxmAcPmGroup,
       "pxmAcPmRealGroup": pxmAcPmRealGroup,
       "pxmBwpAcPmGroup": pxmBwpAcPmGroup,
       "pxmBwpAcPmRealGroup": pxmBwpAcPmRealGroup,
       "pxmTC0AcPmGroup": pxmTC0AcPmGroup,
       "pxmTC0AcPmRealGroup": pxmTC0AcPmRealGroup,
       "pxmTC2AcPmGroup": pxmTC2AcPmGroup,
       "pxmTC2AcPmRealGroup": pxmTC2AcPmRealGroup,
       "pxmTC4AcPmGroup": pxmTC4AcPmGroup,
       "pxmTC4AcPmRealGroup": pxmTC4AcPmRealGroup,
       "pxmTC6AcPmGroup": pxmTC6AcPmGroup,
       "pxmTC6AcPmRealGroup": pxmTC6AcPmRealGroup,
       "pxmTC7AcPmGroup": pxmTC7AcPmGroup,
       "pxmTC7AcPmRealGroup": pxmTC7AcPmRealGroup,
       "pxmTCANYAcPmGroup": pxmTCANYAcPmGroup,
       "pxmTCANYAcPmRealGroup": pxmTCANYAcPmRealGroup}
)
