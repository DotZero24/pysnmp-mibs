# SNMP MIB module (INFINERA-PM-ODUKT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-ODUKT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:37 2025
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

(InfnSampleDuration,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnSampleDuration",
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

oduKtPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21)
)
if mibBuilder.loadTexts:
    oduKtPmMIB.setRevisions(
        ("2009-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OduKtPmRealTable_Object = MibTable
oduKtPmRealTable = _OduKtPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 1)
)
if mibBuilder.loadTexts:
    oduKtPmRealTable.setStatus("current")
_OduKtPmRealEntry_Object = MibTableRow
oduKtPmRealEntry = _OduKtPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 1, 1)
)
oduKtPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oduKtPmRealEntry.setStatus("current")
_OduKtPmRealCVT_Type = HCPerfIntervalCount
_OduKtPmRealCVT_Object = MibTableColumn
oduKtPmRealCVT = _OduKtPmRealCVT_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 1, 1, 1),
    _OduKtPmRealCVT_Type()
)
oduKtPmRealCVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmRealCVT.setStatus("current")
_OduKtPmRealErroredBlocks_Type = HCPerfIntervalCount
_OduKtPmRealErroredBlocks_Object = MibTableColumn
oduKtPmRealErroredBlocks = _OduKtPmRealErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 1, 1, 2),
    _OduKtPmRealErroredBlocks_Type()
)
oduKtPmRealErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmRealErroredBlocks.setStatus("current")
_OduKtPmRealBEICount_Type = HCPerfIntervalCount
_OduKtPmRealBEICount_Object = MibTableColumn
oduKtPmRealBEICount = _OduKtPmRealBEICount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 1, 1, 3),
    _OduKtPmRealBEICount_Type()
)
oduKtPmRealBEICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmRealBEICount.setStatus("current")
_OduKtPmRealDefectSeconds_Type = Integer32
_OduKtPmRealDefectSeconds_Object = MibTableColumn
oduKtPmRealDefectSeconds = _OduKtPmRealDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 1, 1, 4),
    _OduKtPmRealDefectSeconds_Type()
)
oduKtPmRealDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmRealDefectSeconds.setStatus("current")
_OduKtPmRealDefectSecondsFEND_Type = Integer32
_OduKtPmRealDefectSecondsFEND_Object = MibTableColumn
oduKtPmRealDefectSecondsFEND = _OduKtPmRealDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 1, 1, 5),
    _OduKtPmRealDefectSecondsFEND_Type()
)
oduKtPmRealDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmRealDefectSecondsFEND.setStatus("current")
_OduKtPmTable_Object = MibTable
oduKtPmTable = _OduKtPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2)
)
if mibBuilder.loadTexts:
    oduKtPmTable.setStatus("current")
_OduKtPmEntry_Object = MibTableRow
oduKtPmEntry = _OduKtPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1)
)
oduKtPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-ODUKT-MIB", "oduKtPmSampleDuration"),
    (0, "INFINERA-PM-ODUKT-MIB", "oduKtPmTimestamp"),
)
if mibBuilder.loadTexts:
    oduKtPmEntry.setStatus("current")


class _OduKtPmTimestamp_Type(Integer32):
    """Custom type oduKtPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OduKtPmTimestamp_Type.__name__ = "Integer32"
_OduKtPmTimestamp_Object = MibTableColumn
oduKtPmTimestamp = _OduKtPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 1),
    _OduKtPmTimestamp_Type()
)
oduKtPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oduKtPmTimestamp.setStatus("current")
_OduKtPmSampleDuration_Type = InfnSampleDuration
_OduKtPmSampleDuration_Object = MibTableColumn
oduKtPmSampleDuration = _OduKtPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 2),
    _OduKtPmSampleDuration_Type()
)
oduKtPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oduKtPmSampleDuration.setStatus("current")
_OduKtPmValidity_Type = TruthValue
_OduKtPmValidity_Object = MibTableColumn
oduKtPmValidity = _OduKtPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 3),
    _OduKtPmValidity_Type()
)
oduKtPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmValidity.setStatus("current")
_OduKtPmCVT_Type = HCPerfIntervalCount
_OduKtPmCVT_Object = MibTableColumn
oduKtPmCVT = _OduKtPmCVT_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 4),
    _OduKtPmCVT_Type()
)
oduKtPmCVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmCVT.setStatus("current")
_OduKtPmErroredBlocks_Type = HCPerfIntervalCount
_OduKtPmErroredBlocks_Object = MibTableColumn
oduKtPmErroredBlocks = _OduKtPmErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 5),
    _OduKtPmErroredBlocks_Type()
)
oduKtPmErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmErroredBlocks.setStatus("current")
_OduKtPmBEICount_Type = HCPerfIntervalCount
_OduKtPmBEICount_Object = MibTableColumn
oduKtPmBEICount = _OduKtPmBEICount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 6),
    _OduKtPmBEICount_Type()
)
oduKtPmBEICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmBEICount.setStatus("current")
_OduKtPmDefectSeconds_Type = Integer32
_OduKtPmDefectSeconds_Object = MibTableColumn
oduKtPmDefectSeconds = _OduKtPmDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 7),
    _OduKtPmDefectSeconds_Type()
)
oduKtPmDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmDefectSeconds.setStatus("current")
_OduKtPmCircuitId_Type = DisplayString
_OduKtPmCircuitId_Object = MibTableColumn
oduKtPmCircuitId = _OduKtPmCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 8),
    _OduKtPmCircuitId_Type()
)
oduKtPmCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmCircuitId.setStatus("current")
_OduKtPmPayloadType_Type = InfnServiceType
_OduKtPmPayloadType_Object = MibTableColumn
oduKtPmPayloadType = _OduKtPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 9),
    _OduKtPmPayloadType_Type()
)
oduKtPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmPayloadType.setStatus("current")
_OduKtPmDefectSecondsFEND_Type = Integer32
_OduKtPmDefectSecondsFEND_Object = MibTableColumn
oduKtPmDefectSecondsFEND = _OduKtPmDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 2, 1, 10),
    _OduKtPmDefectSecondsFEND_Type()
)
oduKtPmDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduKtPmDefectSecondsFEND.setStatus("current")
_OduKtPmConformance_ObjectIdentity = ObjectIdentity
oduKtPmConformance = _OduKtPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 3)
)
_OduKtPmCompliances_ObjectIdentity = ObjectIdentity
oduKtPmCompliances = _OduKtPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 3, 1)
)
_OduKtPmGroups_ObjectIdentity = ObjectIdentity
oduKtPmGroups = _OduKtPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 3, 2)
)

# Managed Objects groups

oduKtPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 3, 2, 1)
)
oduKtPmGroup.setObjects(
      *(("INFINERA-PM-ODUKT-MIB", "oduKtPmTimestamp"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmSampleDuration"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmValidity"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmCVT"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmErroredBlocks"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmBEICount"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmDefectSeconds"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmCircuitId"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmPayloadType"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmDefectSecondsFEND"))
)
if mibBuilder.loadTexts:
    oduKtPmGroup.setStatus("current")

oduKtPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 3, 2, 2)
)
oduKtPmRealGroup.setObjects(
      *(("INFINERA-PM-ODUKT-MIB", "oduKtPmRealCVT"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmRealErroredBlocks"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmRealBEICount"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmRealDefectSeconds"),
        ("INFINERA-PM-ODUKT-MIB", "oduKtPmRealDefectSecondsFEND"))
)
if mibBuilder.loadTexts:
    oduKtPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oduKtPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 3, 1, 1)
)
oduKtPmCompliance.setObjects(
    ("INFINERA-PM-ODUKT-MIB", "oduKtPmGroup")
)
if mibBuilder.loadTexts:
    oduKtPmCompliance.setStatus(
        "current"
    )

oduKtPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 21, 3, 1, 2)
)
oduKtPmRealCompliance.setObjects(
    ("INFINERA-PM-ODUKT-MIB", "oduKtPmRealGroup")
)
if mibBuilder.loadTexts:
    oduKtPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-ODUKT-MIB",
    **{"oduKtPmMIB": oduKtPmMIB,
       "oduKtPmRealTable": oduKtPmRealTable,
       "oduKtPmRealEntry": oduKtPmRealEntry,
       "oduKtPmRealCVT": oduKtPmRealCVT,
       "oduKtPmRealErroredBlocks": oduKtPmRealErroredBlocks,
       "oduKtPmRealBEICount": oduKtPmRealBEICount,
       "oduKtPmRealDefectSeconds": oduKtPmRealDefectSeconds,
       "oduKtPmRealDefectSecondsFEND": oduKtPmRealDefectSecondsFEND,
       "oduKtPmTable": oduKtPmTable,
       "oduKtPmEntry": oduKtPmEntry,
       "oduKtPmTimestamp": oduKtPmTimestamp,
       "oduKtPmSampleDuration": oduKtPmSampleDuration,
       "oduKtPmValidity": oduKtPmValidity,
       "oduKtPmCVT": oduKtPmCVT,
       "oduKtPmErroredBlocks": oduKtPmErroredBlocks,
       "oduKtPmBEICount": oduKtPmBEICount,
       "oduKtPmDefectSeconds": oduKtPmDefectSeconds,
       "oduKtPmCircuitId": oduKtPmCircuitId,
       "oduKtPmPayloadType": oduKtPmPayloadType,
       "oduKtPmDefectSecondsFEND": oduKtPmDefectSecondsFEND,
       "oduKtPmConformance": oduKtPmConformance,
       "oduKtPmCompliances": oduKtPmCompliances,
       "oduKtPmCompliance": oduKtPmCompliance,
       "oduKtPmRealCompliance": oduKtPmRealCompliance,
       "oduKtPmGroups": oduKtPmGroups,
       "oduKtPmGroup": oduKtPmGroup,
       "oduKtPmRealGroup": oduKtPmRealGroup}
)
