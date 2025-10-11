# SNMP MIB module (INFINERA-PM-PXMMEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-PXMMEP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:30 2025
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

(FloatHundredths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths")

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

pxmMepPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94)
)
if mibBuilder.loadTexts:
    pxmMepPmMIB.setRevisions(
        ("2014-02-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmMepPmRealTable_Object = MibTable
pxmMepPmRealTable = _PxmMepPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1)
)
if mibBuilder.loadTexts:
    pxmMepPmRealTable.setStatus("current")
_PxmMepPmRealEntry_Object = MibTableRow
pxmMepPmRealEntry = _PxmMepPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1)
)
pxmMepPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmMepPmRealEntry.setStatus("current")
_PxmMepPmRealRxAISPackets_Type = Counter64
_PxmMepPmRealRxAISPackets_Object = MibTableColumn
pxmMepPmRealRxAISPackets = _PxmMepPmRealRxAISPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 1),
    _PxmMepPmRealRxAISPackets_Type()
)
pxmMepPmRealRxAISPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealRxAISPackets.setStatus("current")
_PxmMepPmRealTxAISPackets_Type = Counter64
_PxmMepPmRealTxAISPackets_Object = MibTableColumn
pxmMepPmRealTxAISPackets = _PxmMepPmRealTxAISPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 2),
    _PxmMepPmRealTxAISPackets_Type()
)
pxmMepPmRealTxAISPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealTxAISPackets.setStatus("current")
_PxmMepPmRealTxEthCSFPDUs_Type = Counter64
_PxmMepPmRealTxEthCSFPDUs_Object = MibTableColumn
pxmMepPmRealTxEthCSFPDUs = _PxmMepPmRealTxEthCSFPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 3),
    _PxmMepPmRealTxEthCSFPDUs_Type()
)
pxmMepPmRealTxEthCSFPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealTxEthCSFPDUs.setStatus("current")
_PxmMepPmRealRxEthCSFPDUs_Type = Counter64
_PxmMepPmRealRxEthCSFPDUs_Object = MibTableColumn
pxmMepPmRealRxEthCSFPDUs = _PxmMepPmRealRxEthCSFPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 4),
    _PxmMepPmRealRxEthCSFPDUs_Type()
)
pxmMepPmRealRxEthCSFPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealRxEthCSFPDUs.setStatus("current")
_PxmMepPmRealRxEthCSFLOSPDUs_Type = Counter64
_PxmMepPmRealRxEthCSFLOSPDUs_Object = MibTableColumn
pxmMepPmRealRxEthCSFLOSPDUs = _PxmMepPmRealRxEthCSFLOSPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 5),
    _PxmMepPmRealRxEthCSFLOSPDUs_Type()
)
pxmMepPmRealRxEthCSFLOSPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealRxEthCSFLOSPDUs.setStatus("current")
_PxmMepPmRealRxEthCSFRDIPDUs_Type = Counter64
_PxmMepPmRealRxEthCSFRDIPDUs_Object = MibTableColumn
pxmMepPmRealRxEthCSFRDIPDUs = _PxmMepPmRealRxEthCSFRDIPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 6),
    _PxmMepPmRealRxEthCSFRDIPDUs_Type()
)
pxmMepPmRealRxEthCSFRDIPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealRxEthCSFRDIPDUs.setStatus("current")
_PxmMepPmRealRxEthCSFFDIPDUs_Type = Counter64
_PxmMepPmRealRxEthCSFFDIPDUs_Object = MibTableColumn
pxmMepPmRealRxEthCSFFDIPDUs = _PxmMepPmRealRxEthCSFFDIPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 7),
    _PxmMepPmRealRxEthCSFFDIPDUs_Type()
)
pxmMepPmRealRxEthCSFFDIPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealRxEthCSFFDIPDUs.setStatus("current")
_PxmMepPmRealRxEthCSFCDCIPDUs_Type = Counter64
_PxmMepPmRealRxEthCSFCDCIPDUs_Object = MibTableColumn
pxmMepPmRealRxEthCSFCDCIPDUs = _PxmMepPmRealRxEthCSFCDCIPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 8),
    _PxmMepPmRealRxEthCSFCDCIPDUs_Type()
)
pxmMepPmRealRxEthCSFCDCIPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealRxEthCSFCDCIPDUs.setStatus("current")
_PxmMepPmRealRxEthCSFErrPDUs_Type = Counter64
_PxmMepPmRealRxEthCSFErrPDUs_Object = MibTableColumn
pxmMepPmRealRxEthCSFErrPDUs = _PxmMepPmRealRxEthCSFErrPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 1, 1, 9),
    _PxmMepPmRealRxEthCSFErrPDUs_Type()
)
pxmMepPmRealRxEthCSFErrPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRealRxEthCSFErrPDUs.setStatus("current")
_PxmMepPmTable_Object = MibTable
pxmMepPmTable = _PxmMepPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2)
)
if mibBuilder.loadTexts:
    pxmMepPmTable.setStatus("current")
_PxmMepPmEntry_Object = MibTableRow
pxmMepPmEntry = _PxmMepPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1)
)
pxmMepPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PXMMEP-MIB", "pxmMepPmSampleDuration"),
    (0, "INFINERA-PM-PXMMEP-MIB", "pxmMepPmTimestamp"),
)
if mibBuilder.loadTexts:
    pxmMepPmEntry.setStatus("current")


class _PxmMepPmTimestamp_Type(Integer32):
    """Custom type pxmMepPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PxmMepPmTimestamp_Type.__name__ = "Integer32"
_PxmMepPmTimestamp_Object = MibTableColumn
pxmMepPmTimestamp = _PxmMepPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 1),
    _PxmMepPmTimestamp_Type()
)
pxmMepPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmMepPmTimestamp.setStatus("current")


class _PxmMepPmSampleDuration_Type(Integer32):
    """Custom type pxmMepPmSampleDuration based on Integer32"""
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


_PxmMepPmSampleDuration_Type.__name__ = "Integer32"
_PxmMepPmSampleDuration_Object = MibTableColumn
pxmMepPmSampleDuration = _PxmMepPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 2),
    _PxmMepPmSampleDuration_Type()
)
pxmMepPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pxmMepPmSampleDuration.setStatus("current")
_PxmMepPmValidity_Type = TruthValue
_PxmMepPmValidity_Object = MibTableColumn
pxmMepPmValidity = _PxmMepPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 3),
    _PxmMepPmValidity_Type()
)
pxmMepPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmValidity.setStatus("current")
_PxmMepPmRxAISPackets_Type = HCPerfIntervalCount
_PxmMepPmRxAISPackets_Object = MibTableColumn
pxmMepPmRxAISPackets = _PxmMepPmRxAISPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 4),
    _PxmMepPmRxAISPackets_Type()
)
pxmMepPmRxAISPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRxAISPackets.setStatus("current")
_PxmMepPmTxAISPackets_Type = HCPerfIntervalCount
_PxmMepPmTxAISPackets_Object = MibTableColumn
pxmMepPmTxAISPackets = _PxmMepPmTxAISPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 5),
    _PxmMepPmTxAISPackets_Type()
)
pxmMepPmTxAISPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmTxAISPackets.setStatus("current")
_PxmMepPmTxEthCSFPDUs_Type = HCPerfIntervalCount
_PxmMepPmTxEthCSFPDUs_Object = MibTableColumn
pxmMepPmTxEthCSFPDUs = _PxmMepPmTxEthCSFPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 6),
    _PxmMepPmTxEthCSFPDUs_Type()
)
pxmMepPmTxEthCSFPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmTxEthCSFPDUs.setStatus("current")
_PxmMepPmRxEthCSFPDUs_Type = HCPerfIntervalCount
_PxmMepPmRxEthCSFPDUs_Object = MibTableColumn
pxmMepPmRxEthCSFPDUs = _PxmMepPmRxEthCSFPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 7),
    _PxmMepPmRxEthCSFPDUs_Type()
)
pxmMepPmRxEthCSFPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRxEthCSFPDUs.setStatus("current")
_PxmMepPmRxEthCSFLOSPDUs_Type = HCPerfIntervalCount
_PxmMepPmRxEthCSFLOSPDUs_Object = MibTableColumn
pxmMepPmRxEthCSFLOSPDUs = _PxmMepPmRxEthCSFLOSPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 8),
    _PxmMepPmRxEthCSFLOSPDUs_Type()
)
pxmMepPmRxEthCSFLOSPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRxEthCSFLOSPDUs.setStatus("current")
_PxmMepPmRxEthCSFRDIPDUs_Type = HCPerfIntervalCount
_PxmMepPmRxEthCSFRDIPDUs_Object = MibTableColumn
pxmMepPmRxEthCSFRDIPDUs = _PxmMepPmRxEthCSFRDIPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 9),
    _PxmMepPmRxEthCSFRDIPDUs_Type()
)
pxmMepPmRxEthCSFRDIPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRxEthCSFRDIPDUs.setStatus("current")
_PxmMepPmRxEthCSFFDIPDUs_Type = HCPerfIntervalCount
_PxmMepPmRxEthCSFFDIPDUs_Object = MibTableColumn
pxmMepPmRxEthCSFFDIPDUs = _PxmMepPmRxEthCSFFDIPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 10),
    _PxmMepPmRxEthCSFFDIPDUs_Type()
)
pxmMepPmRxEthCSFFDIPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRxEthCSFFDIPDUs.setStatus("current")
_PxmMepPmRxEthCSFCDCIPDUs_Type = HCPerfIntervalCount
_PxmMepPmRxEthCSFCDCIPDUs_Object = MibTableColumn
pxmMepPmRxEthCSFCDCIPDUs = _PxmMepPmRxEthCSFCDCIPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 11),
    _PxmMepPmRxEthCSFCDCIPDUs_Type()
)
pxmMepPmRxEthCSFCDCIPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRxEthCSFCDCIPDUs.setStatus("current")
_PxmMepPmRxEthCSFErrPDUs_Type = HCPerfIntervalCount
_PxmMepPmRxEthCSFErrPDUs_Object = MibTableColumn
pxmMepPmRxEthCSFErrPDUs = _PxmMepPmRxEthCSFErrPDUs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 2, 1, 12),
    _PxmMepPmRxEthCSFErrPDUs_Type()
)
pxmMepPmRxEthCSFErrPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMepPmRxEthCSFErrPDUs.setStatus("current")
_PxmMepPmConformance_ObjectIdentity = ObjectIdentity
pxmMepPmConformance = _PxmMepPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 3)
)
_PxmMepPmCompliances_ObjectIdentity = ObjectIdentity
pxmMepPmCompliances = _PxmMepPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 3, 1)
)
_PxmMepPmGroups_ObjectIdentity = ObjectIdentity
pxmMepPmGroups = _PxmMepPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 3, 2)
)

# Managed Objects groups

pxmMepPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 3, 2, 1)
)
pxmMepPmGroup.setObjects(
      *(("INFINERA-PM-PXMMEP-MIB", "pxmMepPmValidity"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRxAISPackets"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmTxAISPackets"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmTxEthCSFPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRxEthCSFPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRxEthCSFLOSPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRxEthCSFRDIPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRxEthCSFFDIPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRxEthCSFCDCIPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRxEthCSFErrPDUs"))
)
if mibBuilder.loadTexts:
    pxmMepPmGroup.setStatus("current")

pxmMepPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 3, 2, 2)
)
pxmMepPmRealGroup.setObjects(
      *(("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealRxAISPackets"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealTxAISPackets"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealTxEthCSFPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealRxEthCSFPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealRxEthCSFLOSPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealRxEthCSFRDIPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealRxEthCSFFDIPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealRxEthCSFCDCIPDUs"),
        ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealRxEthCSFErrPDUs"))
)
if mibBuilder.loadTexts:
    pxmMepPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmMepPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 3, 1, 1)
)
pxmMepPmCompliance.setObjects(
    ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmGroup")
)
if mibBuilder.loadTexts:
    pxmMepPmCompliance.setStatus(
        "current"
    )

pxmMepPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 94, 3, 1, 2)
)
pxmMepPmRealCompliance.setObjects(
    ("INFINERA-PM-PXMMEP-MIB", "pxmMepPmRealGroup")
)
if mibBuilder.loadTexts:
    pxmMepPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-PXMMEP-MIB",
    **{"pxmMepPmMIB": pxmMepPmMIB,
       "pxmMepPmRealTable": pxmMepPmRealTable,
       "pxmMepPmRealEntry": pxmMepPmRealEntry,
       "pxmMepPmRealRxAISPackets": pxmMepPmRealRxAISPackets,
       "pxmMepPmRealTxAISPackets": pxmMepPmRealTxAISPackets,
       "pxmMepPmRealTxEthCSFPDUs": pxmMepPmRealTxEthCSFPDUs,
       "pxmMepPmRealRxEthCSFPDUs": pxmMepPmRealRxEthCSFPDUs,
       "pxmMepPmRealRxEthCSFLOSPDUs": pxmMepPmRealRxEthCSFLOSPDUs,
       "pxmMepPmRealRxEthCSFRDIPDUs": pxmMepPmRealRxEthCSFRDIPDUs,
       "pxmMepPmRealRxEthCSFFDIPDUs": pxmMepPmRealRxEthCSFFDIPDUs,
       "pxmMepPmRealRxEthCSFCDCIPDUs": pxmMepPmRealRxEthCSFCDCIPDUs,
       "pxmMepPmRealRxEthCSFErrPDUs": pxmMepPmRealRxEthCSFErrPDUs,
       "pxmMepPmTable": pxmMepPmTable,
       "pxmMepPmEntry": pxmMepPmEntry,
       "pxmMepPmTimestamp": pxmMepPmTimestamp,
       "pxmMepPmSampleDuration": pxmMepPmSampleDuration,
       "pxmMepPmValidity": pxmMepPmValidity,
       "pxmMepPmRxAISPackets": pxmMepPmRxAISPackets,
       "pxmMepPmTxAISPackets": pxmMepPmTxAISPackets,
       "pxmMepPmTxEthCSFPDUs": pxmMepPmTxEthCSFPDUs,
       "pxmMepPmRxEthCSFPDUs": pxmMepPmRxEthCSFPDUs,
       "pxmMepPmRxEthCSFLOSPDUs": pxmMepPmRxEthCSFLOSPDUs,
       "pxmMepPmRxEthCSFRDIPDUs": pxmMepPmRxEthCSFRDIPDUs,
       "pxmMepPmRxEthCSFFDIPDUs": pxmMepPmRxEthCSFFDIPDUs,
       "pxmMepPmRxEthCSFCDCIPDUs": pxmMepPmRxEthCSFCDCIPDUs,
       "pxmMepPmRxEthCSFErrPDUs": pxmMepPmRxEthCSFErrPDUs,
       "pxmMepPmConformance": pxmMepPmConformance,
       "pxmMepPmCompliances": pxmMepPmCompliances,
       "pxmMepPmCompliance": pxmMepPmCompliance,
       "pxmMepPmRealCompliance": pxmMepPmRealCompliance,
       "pxmMepPmGroups": pxmMepPmGroups,
       "pxmMepPmGroup": pxmMepPmGroup,
       "pxmMepPmRealGroup": pxmMepPmRealGroup}
)
