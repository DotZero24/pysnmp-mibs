# SNMP MIB module (INFINERA-ENTITY-FMMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FMMC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:15 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatThousandths,
 InfnAlienTxEDFAGain,
 InfnCBandOlosSoakTime,
 InfnEqptType,
 InfnModelingMode,
 InfnOperatingMode,
 InfnWaveInterfaceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatThousandths",
    "InfnAlienTxEDFAGain",
    "InfnCBandOlosSoakTime",
    "InfnEqptType",
    "InfnModelingMode",
    "InfnOperatingMode",
    "InfnWaveInterfaceType")

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

fmmcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fmmc5Table_Object = MibTable
fmmc5Table = _Fmmc5Table_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 1)
)
if mibBuilder.loadTexts:
    fmmc5Table.setStatus("current")
_Fmmc5Entry_Object = MibTableRow
fmmc5Entry = _Fmmc5Entry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 1, 1)
)
fmmc5Entry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fmmc5Entry.setStatus("current")
_Fmmc5MoId_Type = DisplayString
_Fmmc5MoId_Object = MibTableColumn
fmmc5MoId = _Fmmc5MoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 1, 1, 1),
    _Fmmc5MoId_Type()
)
fmmc5MoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc5MoId.setStatus("current")
_Fmmc5ProvEqptType_Type = InfnEqptType
_Fmmc5ProvEqptType_Object = MibTableColumn
fmmc5ProvEqptType = _Fmmc5ProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 1, 1, 2),
    _Fmmc5ProvEqptType_Type()
)
fmmc5ProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc5ProvEqptType.setStatus("current")
_Fmmc5OperatingMode_Type = InfnOperatingMode
_Fmmc5OperatingMode_Object = MibTableColumn
fmmc5OperatingMode = _Fmmc5OperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 1, 1, 3),
    _Fmmc5OperatingMode_Type()
)
fmmc5OperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmc5OperatingMode.setStatus("current")
_Fmmc12Table_Object = MibTable
fmmc12Table = _Fmmc12Table_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2)
)
if mibBuilder.loadTexts:
    fmmc12Table.setStatus("current")
_Fmmc12Entry_Object = MibTableRow
fmmc12Entry = _Fmmc12Entry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2, 1)
)
fmmc12Entry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fmmc12Entry.setStatus("current")
_Fmmc12MoId_Type = DisplayString
_Fmmc12MoId_Object = MibTableColumn
fmmc12MoId = _Fmmc12MoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2, 1, 1),
    _Fmmc12MoId_Type()
)
fmmc12MoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc12MoId.setStatus("current")
_Fmmc12ProvEqptType_Type = InfnEqptType
_Fmmc12ProvEqptType_Object = MibTableColumn
fmmc12ProvEqptType = _Fmmc12ProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2, 1, 2),
    _Fmmc12ProvEqptType_Type()
)
fmmc12ProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc12ProvEqptType.setStatus("current")
_Fmmc12OperatingMode_Type = InfnOperatingMode
_Fmmc12OperatingMode_Object = MibTableColumn
fmmc12OperatingMode = _Fmmc12OperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2, 1, 3),
    _Fmmc12OperatingMode_Type()
)
fmmc12OperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc12OperatingMode.setStatus("current")
_Fmmc12InputSource_Type = InfnWaveInterfaceType
_Fmmc12InputSource_Object = MibTableColumn
fmmc12InputSource = _Fmmc12InputSource_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2, 1, 4),
    _Fmmc12InputSource_Type()
)
fmmc12InputSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc12InputSource.setStatus("current")
_Fmmc12AlienTxEDFAGain_Type = InfnAlienTxEDFAGain
_Fmmc12AlienTxEDFAGain_Object = MibTableColumn
fmmc12AlienTxEDFAGain = _Fmmc12AlienTxEDFAGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2, 1, 5),
    _Fmmc12AlienTxEDFAGain_Type()
)
fmmc12AlienTxEDFAGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc12AlienTxEDFAGain.setStatus("current")
_Fmmc12ModelingMode_Type = InfnModelingMode
_Fmmc12ModelingMode_Object = MibTableColumn
fmmc12ModelingMode = _Fmmc12ModelingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2, 1, 6),
    _Fmmc12ModelingMode_Type()
)
fmmc12ModelingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc12ModelingMode.setStatus("current")
_Fmmc12OlosSoakTime_Type = InfnCBandOlosSoakTime
_Fmmc12OlosSoakTime_Object = MibTableColumn
fmmc12OlosSoakTime = _Fmmc12OlosSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 2, 1, 7),
    _Fmmc12OlosSoakTime_Type()
)
fmmc12OlosSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmc12OlosSoakTime.setStatus("current")
_FmmcConformance_ObjectIdentity = ObjectIdentity
fmmcConformance = _FmmcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 3)
)
_FmmcCompliances_ObjectIdentity = ObjectIdentity
fmmcCompliances = _FmmcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 3, 1)
)
_FmmcGroups_ObjectIdentity = ObjectIdentity
fmmcGroups = _FmmcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 3, 2)
)

# Managed Objects groups

fmmc5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 3, 2, 1)
)
fmmc5Group.setObjects(
      *(("INFINERA-ENTITY-FMMC-MIB", "fmmc5MoId"),
        ("INFINERA-ENTITY-FMMC-MIB", "fmmc5ProvEqptType"),
        ("INFINERA-ENTITY-FMMC-MIB", "fmmc5OperatingMode"))
)
if mibBuilder.loadTexts:
    fmmc5Group.setStatus("current")

fmmc12Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 3, 2, 2)
)
fmmc12Group.setObjects(
      *(("INFINERA-ENTITY-FMMC-MIB", "fmmc12MoId"),
        ("INFINERA-ENTITY-FMMC-MIB", "fmmc12ProvEqptType"),
        ("INFINERA-ENTITY-FMMC-MIB", "fmmc12OperatingMode"),
        ("INFINERA-ENTITY-FMMC-MIB", "fmmc12InputSource"),
        ("INFINERA-ENTITY-FMMC-MIB", "fmmc12AlienTxEDFAGain"),
        ("INFINERA-ENTITY-FMMC-MIB", "fmmc12ModelingMode"),
        ("INFINERA-ENTITY-FMMC-MIB", "fmmc12OlosSoakTime"))
)
if mibBuilder.loadTexts:
    fmmc12Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmmcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 3, 1, 1)
)
fmmcCompliance.setObjects(
    ("INFINERA-ENTITY-FMMC-MIB", "fmmc5Group")
)
if mibBuilder.loadTexts:
    fmmcCompliance.setStatus(
        "current"
    )

fmmc12Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 47, 3, 1, 2)
)
fmmc12Compliance.setObjects(
    ("INFINERA-ENTITY-FMMC-MIB", "fmmc12Group")
)
if mibBuilder.loadTexts:
    fmmc12Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FMMC-MIB",
    **{"fmmcMIB": fmmcMIB,
       "fmmc5Table": fmmc5Table,
       "fmmc5Entry": fmmc5Entry,
       "fmmc5MoId": fmmc5MoId,
       "fmmc5ProvEqptType": fmmc5ProvEqptType,
       "fmmc5OperatingMode": fmmc5OperatingMode,
       "fmmc12Table": fmmc12Table,
       "fmmc12Entry": fmmc12Entry,
       "fmmc12MoId": fmmc12MoId,
       "fmmc12ProvEqptType": fmmc12ProvEqptType,
       "fmmc12OperatingMode": fmmc12OperatingMode,
       "fmmc12InputSource": fmmc12InputSource,
       "fmmc12AlienTxEDFAGain": fmmc12AlienTxEDFAGain,
       "fmmc12ModelingMode": fmmc12ModelingMode,
       "fmmc12OlosSoakTime": fmmc12OlosSoakTime,
       "fmmcConformance": fmmcConformance,
       "fmmcCompliances": fmmcCompliances,
       "fmmcCompliance": fmmcCompliance,
       "fmmc12Compliance": fmmc12Compliance,
       "fmmcGroups": fmmcGroups,
       "fmmc5Group": fmmc5Group,
       "fmmc12Group": fmmc12Group}
)
