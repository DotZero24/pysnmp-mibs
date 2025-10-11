# SNMP MIB module (INFINERA-PM-ODUKTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-ODUKTI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:59 2025
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

oduiKtPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31)
)
if mibBuilder.loadTexts:
    oduiKtPmMIB.setRevisions(
        ("2011-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OduiKtPmRealTable_Object = MibTable
oduiKtPmRealTable = _OduiKtPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 1)
)
if mibBuilder.loadTexts:
    oduiKtPmRealTable.setStatus("current")
_OduiKtPmRealEntry_Object = MibTableRow
oduiKtPmRealEntry = _OduiKtPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 1, 1)
)
oduiKtPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oduiKtPmRealEntry.setStatus("current")
_OduiKtPmRealCVT_Type = HCPerfIntervalCount
_OduiKtPmRealCVT_Object = MibTableColumn
oduiKtPmRealCVT = _OduiKtPmRealCVT_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 1, 1, 1),
    _OduiKtPmRealCVT_Type()
)
oduiKtPmRealCVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmRealCVT.setStatus("current")
_OduiKtPmRealErroredBlocks_Type = HCPerfIntervalCount
_OduiKtPmRealErroredBlocks_Object = MibTableColumn
oduiKtPmRealErroredBlocks = _OduiKtPmRealErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 1, 1, 2),
    _OduiKtPmRealErroredBlocks_Type()
)
oduiKtPmRealErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmRealErroredBlocks.setStatus("current")
_OduiKtPmRealBEICount_Type = HCPerfIntervalCount
_OduiKtPmRealBEICount_Object = MibTableColumn
oduiKtPmRealBEICount = _OduiKtPmRealBEICount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 1, 1, 3),
    _OduiKtPmRealBEICount_Type()
)
oduiKtPmRealBEICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmRealBEICount.setStatus("current")
_OduiKtPmRealDefectSeconds_Type = Integer32
_OduiKtPmRealDefectSeconds_Object = MibTableColumn
oduiKtPmRealDefectSeconds = _OduiKtPmRealDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 1, 1, 4),
    _OduiKtPmRealDefectSeconds_Type()
)
oduiKtPmRealDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmRealDefectSeconds.setStatus("current")
_OduiKtPmTable_Object = MibTable
oduiKtPmTable = _OduiKtPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2)
)
if mibBuilder.loadTexts:
    oduiKtPmTable.setStatus("current")
_OduiKtPmEntry_Object = MibTableRow
oduiKtPmEntry = _OduiKtPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1)
)
oduiKtPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-ODUKTI-MIB", "oduiKtPmSampleDuration"),
    (0, "INFINERA-PM-ODUKTI-MIB", "oduiKtPmTimestamp"),
)
if mibBuilder.loadTexts:
    oduiKtPmEntry.setStatus("current")


class _OduiKtPmTimestamp_Type(Integer32):
    """Custom type oduiKtPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OduiKtPmTimestamp_Type.__name__ = "Integer32"
_OduiKtPmTimestamp_Object = MibTableColumn
oduiKtPmTimestamp = _OduiKtPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 1),
    _OduiKtPmTimestamp_Type()
)
oduiKtPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oduiKtPmTimestamp.setStatus("current")
_OduiKtPmSampleDuration_Type = InfnSampleDuration
_OduiKtPmSampleDuration_Object = MibTableColumn
oduiKtPmSampleDuration = _OduiKtPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 2),
    _OduiKtPmSampleDuration_Type()
)
oduiKtPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oduiKtPmSampleDuration.setStatus("current")
_OduiKtPmValidity_Type = TruthValue
_OduiKtPmValidity_Object = MibTableColumn
oduiKtPmValidity = _OduiKtPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 3),
    _OduiKtPmValidity_Type()
)
oduiKtPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmValidity.setStatus("current")
_OduiKtPmCVT_Type = HCPerfIntervalCount
_OduiKtPmCVT_Object = MibTableColumn
oduiKtPmCVT = _OduiKtPmCVT_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 4),
    _OduiKtPmCVT_Type()
)
oduiKtPmCVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmCVT.setStatus("current")
_OduiKtPmErroredBlocks_Type = HCPerfIntervalCount
_OduiKtPmErroredBlocks_Object = MibTableColumn
oduiKtPmErroredBlocks = _OduiKtPmErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 5),
    _OduiKtPmErroredBlocks_Type()
)
oduiKtPmErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmErroredBlocks.setStatus("current")
_OduiKtPmBEICount_Type = HCPerfIntervalCount
_OduiKtPmBEICount_Object = MibTableColumn
oduiKtPmBEICount = _OduiKtPmBEICount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 6),
    _OduiKtPmBEICount_Type()
)
oduiKtPmBEICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmBEICount.setStatus("current")
_OduiKtPmDefectSeconds_Type = Integer32
_OduiKtPmDefectSeconds_Object = MibTableColumn
oduiKtPmDefectSeconds = _OduiKtPmDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 7),
    _OduiKtPmDefectSeconds_Type()
)
oduiKtPmDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmDefectSeconds.setStatus("current")
_OduiKtPmCircuitId_Type = DisplayString
_OduiKtPmCircuitId_Object = MibTableColumn
oduiKtPmCircuitId = _OduiKtPmCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 8),
    _OduiKtPmCircuitId_Type()
)
oduiKtPmCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmCircuitId.setStatus("current")
_OduiKtPmPayloadType_Type = InfnServiceType
_OduiKtPmPayloadType_Object = MibTableColumn
oduiKtPmPayloadType = _OduiKtPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 2, 1, 9),
    _OduiKtPmPayloadType_Type()
)
oduiKtPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiKtPmPayloadType.setStatus("current")
_OduiKtPmConformance_ObjectIdentity = ObjectIdentity
oduiKtPmConformance = _OduiKtPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 3)
)
_OduiKtPmCompliances_ObjectIdentity = ObjectIdentity
oduiKtPmCompliances = _OduiKtPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 3, 1)
)
_OduiKtPmGroups_ObjectIdentity = ObjectIdentity
oduiKtPmGroups = _OduiKtPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 3, 2)
)

# Managed Objects groups

oduiKtPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 3, 2, 1)
)
oduiKtPmGroup.setObjects(
      *(("INFINERA-PM-ODUKTI-MIB", "oduiKtPmTimestamp"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmSampleDuration"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmValidity"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmCVT"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmErroredBlocks"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmBEICount"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmDefectSeconds"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmCircuitId"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmPayloadType"))
)
if mibBuilder.loadTexts:
    oduiKtPmGroup.setStatus("current")

oduiKtPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 3, 2, 2)
)
oduiKtPmRealGroup.setObjects(
      *(("INFINERA-PM-ODUKTI-MIB", "oduiKtPmRealCVT"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmRealErroredBlocks"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmRealBEICount"),
        ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmRealDefectSeconds"))
)
if mibBuilder.loadTexts:
    oduiKtPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oduiKtPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 3, 1, 1)
)
oduiKtPmCompliance.setObjects(
    ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmGroup")
)
if mibBuilder.loadTexts:
    oduiKtPmCompliance.setStatus(
        "current"
    )

oduiKtPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 31, 3, 1, 2)
)
oduiKtPmRealCompliance.setObjects(
    ("INFINERA-PM-ODUKTI-MIB", "oduiKtPmRealGroup")
)
if mibBuilder.loadTexts:
    oduiKtPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-ODUKTI-MIB",
    **{"oduiKtPmMIB": oduiKtPmMIB,
       "oduiKtPmRealTable": oduiKtPmRealTable,
       "oduiKtPmRealEntry": oduiKtPmRealEntry,
       "oduiKtPmRealCVT": oduiKtPmRealCVT,
       "oduiKtPmRealErroredBlocks": oduiKtPmRealErroredBlocks,
       "oduiKtPmRealBEICount": oduiKtPmRealBEICount,
       "oduiKtPmRealDefectSeconds": oduiKtPmRealDefectSeconds,
       "oduiKtPmTable": oduiKtPmTable,
       "oduiKtPmEntry": oduiKtPmEntry,
       "oduiKtPmTimestamp": oduiKtPmTimestamp,
       "oduiKtPmSampleDuration": oduiKtPmSampleDuration,
       "oduiKtPmValidity": oduiKtPmValidity,
       "oduiKtPmCVT": oduiKtPmCVT,
       "oduiKtPmErroredBlocks": oduiKtPmErroredBlocks,
       "oduiKtPmBEICount": oduiKtPmBEICount,
       "oduiKtPmDefectSeconds": oduiKtPmDefectSeconds,
       "oduiKtPmCircuitId": oduiKtPmCircuitId,
       "oduiKtPmPayloadType": oduiKtPmPayloadType,
       "oduiKtPmConformance": oduiKtPmConformance,
       "oduiKtPmCompliances": oduiKtPmCompliances,
       "oduiKtPmCompliance": oduiKtPmCompliance,
       "oduiKtPmRealCompliance": oduiKtPmRealCompliance,
       "oduiKtPmGroups": oduiKtPmGroups,
       "oduiKtPmGroup": oduiKtPmGroup,
       "oduiKtPmRealGroup": oduiKtPmRealGroup}
)
