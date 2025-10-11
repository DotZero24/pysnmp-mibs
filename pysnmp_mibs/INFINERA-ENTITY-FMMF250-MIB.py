# SNMP MIB module (INFINERA-ENTITY-FMMF250-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FMMF250-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:52 2025
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

(FloatHundredths,
 InfnEnableDisable,
 InfnEqptType,
 InfnOAOperatingMode,
 InfnReporting) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnOAOperatingMode",
    "InfnReporting")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fmmf250MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fmmf250Table_Object = MibTable
fmmf250Table = _Fmmf250Table_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1)
)
if mibBuilder.loadTexts:
    fmmf250Table.setStatus("current")
_Fmmf250Entry_Object = MibTableRow
fmmf250Entry = _Fmmf250Entry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1)
)
fmmf250Entry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fmmf250Entry.setStatus("current")
_Fmmf250MoId_Type = DisplayString
_Fmmf250MoId_Object = MibTableColumn
fmmf250MoId = _Fmmf250MoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 1),
    _Fmmf250MoId_Type()
)
fmmf250MoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250MoId.setStatus("current")
_Fmmf250ProvEqptType_Type = InfnEqptType
_Fmmf250ProvEqptType_Object = MibTableColumn
fmmf250ProvEqptType = _Fmmf250ProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 2),
    _Fmmf250ProvEqptType_Type()
)
fmmf250ProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250ProvEqptType.setStatus("current")
_Fmmf250AutomaticTiltControl_Type = InfnReporting
_Fmmf250AutomaticTiltControl_Object = MibTableColumn
fmmf250AutomaticTiltControl = _Fmmf250AutomaticTiltControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 3),
    _Fmmf250AutomaticTiltControl_Type()
)
fmmf250AutomaticTiltControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250AutomaticTiltControl.setStatus("current")
_Fmmf250EdfaPowerOffset_Type = FloatHundredths
_Fmmf250EdfaPowerOffset_Object = MibTableColumn
fmmf250EdfaPowerOffset = _Fmmf250EdfaPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 4),
    _Fmmf250EdfaPowerOffset_Type()
)
fmmf250EdfaPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250EdfaPowerOffset.setStatus("current")
_Fmmf250DisableGainControlLoop_Type = TruthValue
_Fmmf250DisableGainControlLoop_Object = MibTableColumn
fmmf250DisableGainControlLoop = _Fmmf250DisableGainControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 5),
    _Fmmf250DisableGainControlLoop_Type()
)
fmmf250DisableGainControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250DisableGainControlLoop.setStatus("current")
_Fmmf250RxPowerOffset_Type = FloatHundredths
_Fmmf250RxPowerOffset_Object = MibTableColumn
fmmf250RxPowerOffset = _Fmmf250RxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 6),
    _Fmmf250RxPowerOffset_Type()
)
fmmf250RxPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250RxPowerOffset.setStatus("current")
_Fmmf250SpectrumTiltOffset_Type = FloatHundredths
_Fmmf250SpectrumTiltOffset_Object = MibTableColumn
fmmf250SpectrumTiltOffset = _Fmmf250SpectrumTiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 7),
    _Fmmf250SpectrumTiltOffset_Type()
)
fmmf250SpectrumTiltOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250SpectrumTiltOffset.setStatus("current")
_Fmmf250OperatingMode_Type = InfnOAOperatingMode
_Fmmf250OperatingMode_Object = MibTableColumn
fmmf250OperatingMode = _Fmmf250OperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 8),
    _Fmmf250OperatingMode_Type()
)
fmmf250OperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250OperatingMode.setStatus("current")
_Fmmf250ConfigurationOffset_Type = FloatHundredths
_Fmmf250ConfigurationOffset_Object = MibTableColumn
fmmf250ConfigurationOffset = _Fmmf250ConfigurationOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 1, 1, 9),
    _Fmmf250ConfigurationOffset_Type()
)
fmmf250ConfigurationOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmf250ConfigurationOffset.setStatus("current")
_Fmmf250Conffrmance_ObjectIdentity = ObjectIdentity
fmmf250Conffrmance = _Fmmf250Conffrmance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 3)
)
_Fmmf250Compliances_ObjectIdentity = ObjectIdentity
fmmf250Compliances = _Fmmf250Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 3, 1)
)
_Fmmf250Groups_ObjectIdentity = ObjectIdentity
fmmf250Groups = _Fmmf250Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 3, 2)
)

# Managed Objects groups

fmmf250Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 3, 2, 1)
)
fmmf250Group.setObjects(
      *(("INFINERA-ENTITY-FMMF250-MIB", "fmmf250MoId"),
        ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250ProvEqptType"),
        ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250AutomaticTiltControl"),
        ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250EdfaPowerOffset"),
        ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250DisableGainControlLoop"),
        ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250RxPowerOffset"),
        ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250SpectrumTiltOffset"),
        ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250OperatingMode"),
        ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250ConfigurationOffset"))
)
if mibBuilder.loadTexts:
    fmmf250Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmmf250Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 42, 3, 1, 1)
)
fmmf250Compliance.setObjects(
    ("INFINERA-ENTITY-FMMF250-MIB", "fmmf250Group")
)
if mibBuilder.loadTexts:
    fmmf250Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FMMF250-MIB",
    **{"fmmf250MIB": fmmf250MIB,
       "fmmf250Table": fmmf250Table,
       "fmmf250Entry": fmmf250Entry,
       "fmmf250MoId": fmmf250MoId,
       "fmmf250ProvEqptType": fmmf250ProvEqptType,
       "fmmf250AutomaticTiltControl": fmmf250AutomaticTiltControl,
       "fmmf250EdfaPowerOffset": fmmf250EdfaPowerOffset,
       "fmmf250DisableGainControlLoop": fmmf250DisableGainControlLoop,
       "fmmf250RxPowerOffset": fmmf250RxPowerOffset,
       "fmmf250SpectrumTiltOffset": fmmf250SpectrumTiltOffset,
       "fmmf250OperatingMode": fmmf250OperatingMode,
       "fmmf250ConfigurationOffset": fmmf250ConfigurationOffset,
       "fmmf250Conffrmance": fmmf250Conffrmance,
       "fmmf250Compliances": fmmf250Compliances,
       "fmmf250Compliance": fmmf250Compliance,
       "fmmf250Groups": fmmf250Groups,
       "fmmf250Group": fmmf250Group}
)
