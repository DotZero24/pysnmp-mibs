# SNMP MIB module (INFINERA-ENTITY-PEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-PEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:53 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatTenths,
 InfnEqptType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnEqptType")

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

pemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PemTable_Object = MibTable
pemTable = _PemTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    pemTable.setStatus("current")
_PemEntry_Object = MibTableRow
pemEntry = _PemEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1)
)
pemEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    pemEntry.setStatus("current")
_PemMoId_Type = DisplayString
_PemMoId_Object = MibTableColumn
pemMoId = _PemMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1, 1),
    _PemMoId_Type()
)
pemMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemMoId.setStatus("current")
_PemProvEqptType_Type = InfnEqptType
_PemProvEqptType_Object = MibTableColumn
pemProvEqptType = _PemProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1, 2),
    _PemProvEqptType_Type()
)
pemProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemProvEqptType.setStatus("current")
_ProvRatingAmps_Type = Unsigned32
_ProvRatingAmps_Object = MibTableColumn
provRatingAmps = _ProvRatingAmps_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1, 3),
    _ProvRatingAmps_Type()
)
provRatingAmps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provRatingAmps.setStatus("current")
_InstalledRatingAmps_Type = Unsigned32
_InstalledRatingAmps_Object = MibTableColumn
installedRatingAmps = _InstalledRatingAmps_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1, 4),
    _InstalledRatingAmps_Type()
)
installedRatingAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedRatingAmps.setStatus("current")
_UnderVoltageThreshold_Type = FloatTenths
_UnderVoltageThreshold_Object = MibTableColumn
underVoltageThreshold = _UnderVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1, 5),
    _UnderVoltageThreshold_Type()
)
underVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    underVoltageThreshold.setStatus("current")
_OverVoltageThreshold_Type = FloatTenths
_OverVoltageThreshold_Object = MibTableColumn
overVoltageThreshold = _OverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1, 6),
    _OverVoltageThreshold_Type()
)
overVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overVoltageThreshold.setStatus("current")
_TransientVoltageThreshold_Type = FloatTenths
_TransientVoltageThreshold_Object = MibTableColumn
transientVoltageThreshold = _TransientVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1, 7),
    _TransientVoltageThreshold_Type()
)
transientVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transientVoltageThreshold.setStatus("current")
_InputVoltage_Type = Integer32
_InputVoltage_Object = MibTableColumn
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 1, 1, 8),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("current")
_PemConformance_ObjectIdentity = ObjectIdentity
pemConformance = _PemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 3)
)
_PemCompliances_ObjectIdentity = ObjectIdentity
pemCompliances = _PemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 3, 1)
)
_PemGroups_ObjectIdentity = ObjectIdentity
pemGroups = _PemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 3, 2)
)

# Managed Objects groups

pemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 3, 2, 1)
)
pemGroup.setObjects(
      *(("INFINERA-ENTITY-PEM-MIB", "pemMoId"),
        ("INFINERA-ENTITY-PEM-MIB", "pemProvEqptType"),
        ("INFINERA-ENTITY-PEM-MIB", "provRatingAmps"),
        ("INFINERA-ENTITY-PEM-MIB", "installedRatingAmps"),
        ("INFINERA-ENTITY-PEM-MIB", "underVoltageThreshold"),
        ("INFINERA-ENTITY-PEM-MIB", "overVoltageThreshold"),
        ("INFINERA-ENTITY-PEM-MIB", "transientVoltageThreshold"),
        ("INFINERA-ENTITY-PEM-MIB", "inputVoltage"))
)
if mibBuilder.loadTexts:
    pemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 15, 3, 1, 1)
)
pemCompliance.setObjects(
    ("INFINERA-ENTITY-PEM-MIB", "pemGroup")
)
if mibBuilder.loadTexts:
    pemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-PEM-MIB",
    **{"pemMIB": pemMIB,
       "pemTable": pemTable,
       "pemEntry": pemEntry,
       "pemMoId": pemMoId,
       "pemProvEqptType": pemProvEqptType,
       "provRatingAmps": provRatingAmps,
       "installedRatingAmps": installedRatingAmps,
       "underVoltageThreshold": underVoltageThreshold,
       "overVoltageThreshold": overVoltageThreshold,
       "transientVoltageThreshold": transientVoltageThreshold,
       "inputVoltage": inputVoltage,
       "pemConformance": pemConformance,
       "pemCompliances": pemCompliances,
       "pemCompliance": pemCompliance,
       "pemGroups": pemGroups,
       "pemGroup": pemGroup}
)
