# SNMP MIB module (INFINERA-TP-OLDPSCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OLDPSCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:47 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnMonitoringMode,
 InfnTimReptMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnMonitoringMode",
    "InfnTimReptMode")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

oldpSchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58)
)
if mibBuilder.loadTexts:
    oldpSchMIB.setRevisions(
        ("2016-08-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OldpSchTable_Object = MibTable
oldpSchTable = _OldpSchTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1)
)
if mibBuilder.loadTexts:
    oldpSchTable.setStatus("current")
_OldpSchEntry_Object = MibTableRow
oldpSchEntry = _OldpSchEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1)
)
oldpSchEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oldpSchEntry.setStatus("current")
_TransmitTTI_Type = DisplayString
_TransmitTTI_Object = MibTableColumn
transmitTTI = _TransmitTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 1),
    _TransmitTTI_Type()
)
transmitTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitTTI.setStatus("current")
_RecievedTTI_Type = DisplayString
_RecievedTTI_Object = MibTableColumn
recievedTTI = _RecievedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 2),
    _RecievedTTI_Type()
)
recievedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recievedTTI.setStatus("current")
_ExpectedSAPI_Type = DisplayString
_ExpectedSAPI_Object = MibTableColumn
expectedSAPI = _ExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 3),
    _ExpectedSAPI_Type()
)
expectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expectedSAPI.setStatus("current")
_ExpectedDAPI_Type = DisplayString
_ExpectedDAPI_Object = MibTableColumn
expectedDAPI = _ExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 4),
    _ExpectedDAPI_Type()
)
expectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expectedDAPI.setStatus("current")
_TimDetMode_Type = InfnTimReptMode
_TimDetMode_Object = MibTableColumn
timDetMode = _TimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 5),
    _TimDetMode_Type()
)
timDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timDetMode.setStatus("current")
_MonitoringMode_Type = InfnMonitoringMode
_MonitoringMode_Object = MibTableColumn
monitoringMode = _MonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 6),
    _MonitoringMode_Type()
)
monitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitoringMode.setStatus("current")
_OldpSchConformance_ObjectIdentity = ObjectIdentity
oldpSchConformance = _OldpSchConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3)
)
_OldpSchCompliances_ObjectIdentity = ObjectIdentity
oldpSchCompliances = _OldpSchCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3, 1)
)
_OldpSchGroups_ObjectIdentity = ObjectIdentity
oldpSchGroups = _OldpSchGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3, 2)
)

# Managed Objects groups

oldpSchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3, 2, 1)
)
oldpSchGroup.setObjects(
      *(("INFINERA-TP-OLDPSCH-MIB", "transmitTTI"),
        ("INFINERA-TP-OLDPSCH-MIB", "recievedTTI"),
        ("INFINERA-TP-OLDPSCH-MIB", "expectedSAPI"),
        ("INFINERA-TP-OLDPSCH-MIB", "expectedDAPI"),
        ("INFINERA-TP-OLDPSCH-MIB", "timDetMode"),
        ("INFINERA-TP-OLDPSCH-MIB", "monitoringMode"))
)
if mibBuilder.loadTexts:
    oldpSchGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oldpSchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3, 1, 1)
)
oldpSchCompliance.setObjects(
    ("INFINERA-TP-OLDPSCH-MIB", "oldpSchGroup")
)
if mibBuilder.loadTexts:
    oldpSchCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OLDPSCH-MIB",
    **{"oldpSchMIB": oldpSchMIB,
       "oldpSchTable": oldpSchTable,
       "oldpSchEntry": oldpSchEntry,
       "transmitTTI": transmitTTI,
       "recievedTTI": recievedTTI,
       "expectedSAPI": expectedSAPI,
       "expectedDAPI": expectedDAPI,
       "timDetMode": timDetMode,
       "monitoringMode": monitoringMode,
       "oldpSchConformance": oldpSchConformance,
       "oldpSchCompliances": oldpSchCompliances,
       "oldpSchCompliance": oldpSchCompliance,
       "oldpSchGroups": oldpSchGroups,
       "oldpSchGroup": oldpSchGroup}
)
