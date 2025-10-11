# SNMP MIB module (INFINERA-PM-ODUI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-ODUI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:22 2025
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
 InfnServiceType,
 InfnValidityBitmap) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnSampleDuration",
    "InfnServiceType",
    "InfnValidityBitmap")

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

oduiPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29)
)
if mibBuilder.loadTexts:
    oduiPmMIB.setRevisions(
        ("2009-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OduiPmRealTable_Object = MibTable
oduiPmRealTable = _OduiPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 1)
)
if mibBuilder.loadTexts:
    oduiPmRealTable.setStatus("current")
_OduiPmRealEntry_Object = MibTableRow
oduiPmRealEntry = _OduiPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 1, 1)
)
oduiPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oduiPmRealEntry.setStatus("current")
_OduiPmRealRxDefectSeconds_Type = Integer32
_OduiPmRealRxDefectSeconds_Object = MibTableColumn
oduiPmRealRxDefectSeconds = _OduiPmRealRxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 1, 1, 1),
    _OduiPmRealRxDefectSeconds_Type()
)
oduiPmRealRxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmRealRxDefectSeconds.setStatus("current")
_OduiPmRealRxDefectSecondsFEND_Type = Integer32
_OduiPmRealRxDefectSecondsFEND_Object = MibTableColumn
oduiPmRealRxDefectSecondsFEND = _OduiPmRealRxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 1, 1, 2),
    _OduiPmRealRxDefectSecondsFEND_Type()
)
oduiPmRealRxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmRealRxDefectSecondsFEND.setStatus("current")
_OduiPmRealRxCVP_Type = HCPerfIntervalCount
_OduiPmRealRxCVP_Object = MibTableColumn
oduiPmRealRxCVP = _OduiPmRealRxCVP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 1, 1, 3),
    _OduiPmRealRxCVP_Type()
)
oduiPmRealRxCVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmRealRxCVP.setStatus("current")
_OduiPmRealRxBEICount_Type = HCPerfIntervalCount
_OduiPmRealRxBEICount_Object = MibTableColumn
oduiPmRealRxBEICount = _OduiPmRealRxBEICount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 1, 1, 4),
    _OduiPmRealRxBEICount_Type()
)
oduiPmRealRxBEICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmRealRxBEICount.setStatus("current")
_OduiPmTable_Object = MibTable
oduiPmTable = _OduiPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2)
)
if mibBuilder.loadTexts:
    oduiPmTable.setStatus("current")
_OduiPmEntry_Object = MibTableRow
oduiPmEntry = _OduiPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1)
)
oduiPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-ODUI-MIB", "oduiPmSampleDuration"),
    (0, "INFINERA-PM-ODUI-MIB", "oduiPmTimestamp"),
)
if mibBuilder.loadTexts:
    oduiPmEntry.setStatus("current")


class _OduiPmTimestamp_Type(Integer32):
    """Custom type oduiPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OduiPmTimestamp_Type.__name__ = "Integer32"
_OduiPmTimestamp_Object = MibTableColumn
oduiPmTimestamp = _OduiPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 1),
    _OduiPmTimestamp_Type()
)
oduiPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oduiPmTimestamp.setStatus("current")
_OduiPmSampleDuration_Type = InfnSampleDuration
_OduiPmSampleDuration_Object = MibTableColumn
oduiPmSampleDuration = _OduiPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 2),
    _OduiPmSampleDuration_Type()
)
oduiPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oduiPmSampleDuration.setStatus("current")
_OduiPmValidity_Type = InfnValidityBitmap
_OduiPmValidity_Object = MibTableColumn
oduiPmValidity = _OduiPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 3),
    _OduiPmValidity_Type()
)
oduiPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmValidity.setStatus("current")
_OduiPmRxDefectSeconds_Type = Integer32
_OduiPmRxDefectSeconds_Object = MibTableColumn
oduiPmRxDefectSeconds = _OduiPmRxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 4),
    _OduiPmRxDefectSeconds_Type()
)
oduiPmRxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmRxDefectSeconds.setStatus("current")
_OduiPmCircuitId_Type = DisplayString
_OduiPmCircuitId_Object = MibTableColumn
oduiPmCircuitId = _OduiPmCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 5),
    _OduiPmCircuitId_Type()
)
oduiPmCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmCircuitId.setStatus("current")
_OduiPmPayloadType_Type = InfnServiceType
_OduiPmPayloadType_Object = MibTableColumn
oduiPmPayloadType = _OduiPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 6),
    _OduiPmPayloadType_Type()
)
oduiPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmPayloadType.setStatus("current")
_OduiPmRxDefectSecondsFEND_Type = Integer32
_OduiPmRxDefectSecondsFEND_Object = MibTableColumn
oduiPmRxDefectSecondsFEND = _OduiPmRxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 7),
    _OduiPmRxDefectSecondsFEND_Type()
)
oduiPmRxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmRxDefectSecondsFEND.setStatus("current")
_OduiPmRxCVP_Type = HCPerfIntervalCount
_OduiPmRxCVP_Object = MibTableColumn
oduiPmRxCVP = _OduiPmRxCVP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 8),
    _OduiPmRxCVP_Type()
)
oduiPmRxCVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmRxCVP.setStatus("current")
_OduiPmRxBEICount_Type = HCPerfIntervalCount
_OduiPmRxBEICount_Object = MibTableColumn
oduiPmRxBEICount = _OduiPmRxBEICount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 2, 1, 9),
    _OduiPmRxBEICount_Type()
)
oduiPmRxBEICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduiPmRxBEICount.setStatus("current")
_OduiPmConformance_ObjectIdentity = ObjectIdentity
oduiPmConformance = _OduiPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 3)
)
_OduiPmCompliances_ObjectIdentity = ObjectIdentity
oduiPmCompliances = _OduiPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 3, 1)
)
_OduiPmGroups_ObjectIdentity = ObjectIdentity
oduiPmGroups = _OduiPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 3, 2)
)

# Managed Objects groups

oduiPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 3, 2, 1)
)
oduiPmGroup.setObjects(
      *(("INFINERA-PM-ODUI-MIB", "oduiPmTimestamp"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmSampleDuration"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmValidity"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmRxDefectSeconds"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmCircuitId"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmPayloadType"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmRxDefectSecondsFEND"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmRealRxCVP"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmRealRxBEICount"))
)
if mibBuilder.loadTexts:
    oduiPmGroup.setStatus("current")

oduiPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 3, 2, 2)
)
oduiPmRealGroup.setObjects(
      *(("INFINERA-PM-ODUI-MIB", "oduiPmRealRxDefectSeconds"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmRealRxDefectSecondsFEND"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmRealRxCVP"),
        ("INFINERA-PM-ODUI-MIB", "oduiPmRealRxBEICount"))
)
if mibBuilder.loadTexts:
    oduiPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oduiPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 3, 1, 1)
)
oduiPmCompliance.setObjects(
    ("INFINERA-PM-ODUI-MIB", "oduiPmGroup")
)
if mibBuilder.loadTexts:
    oduiPmCompliance.setStatus(
        "current"
    )

oduiPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 29, 3, 1, 2)
)
oduiPmRealCompliance.setObjects(
    ("INFINERA-PM-ODUI-MIB", "oduiPmRealGroup")
)
if mibBuilder.loadTexts:
    oduiPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-ODUI-MIB",
    **{"oduiPmMIB": oduiPmMIB,
       "oduiPmRealTable": oduiPmRealTable,
       "oduiPmRealEntry": oduiPmRealEntry,
       "oduiPmRealRxDefectSeconds": oduiPmRealRxDefectSeconds,
       "oduiPmRealRxDefectSecondsFEND": oduiPmRealRxDefectSecondsFEND,
       "oduiPmRealRxCVP": oduiPmRealRxCVP,
       "oduiPmRealRxBEICount": oduiPmRealRxBEICount,
       "oduiPmTable": oduiPmTable,
       "oduiPmEntry": oduiPmEntry,
       "oduiPmTimestamp": oduiPmTimestamp,
       "oduiPmSampleDuration": oduiPmSampleDuration,
       "oduiPmValidity": oduiPmValidity,
       "oduiPmRxDefectSeconds": oduiPmRxDefectSeconds,
       "oduiPmCircuitId": oduiPmCircuitId,
       "oduiPmPayloadType": oduiPmPayloadType,
       "oduiPmRxDefectSecondsFEND": oduiPmRxDefectSecondsFEND,
       "oduiPmRxCVP": oduiPmRxCVP,
       "oduiPmRxBEICount": oduiPmRxBEICount,
       "oduiPmConformance": oduiPmConformance,
       "oduiPmCompliances": oduiPmCompliances,
       "oduiPmCompliance": oduiPmCompliance,
       "oduiPmRealCompliance": oduiPmRealCompliance,
       "oduiPmGroups": oduiPmGroups,
       "oduiPmGroup": oduiPmGroup,
       "oduiPmRealGroup": oduiPmRealGroup}
)
