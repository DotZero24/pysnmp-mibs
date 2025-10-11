# SNMP MIB module (RITTAL-RIZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rittal/RITTAL-RIZONE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:05:27 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rittal_ObjectIdentity = ObjectIdentity
rittal = _Rittal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606)
)
_RiZone_ObjectIdentity = ObjectIdentity
riZone = _RiZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6)
)
_RiZoneMibRev_ObjectIdentity = ObjectIdentity
riZoneMibRev = _RiZoneMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6, 1)
)
_RiZoneMibMajRev_Type = Integer32
_RiZoneMibMajRev_Object = MibScalar
riZoneMibMajRev = _RiZoneMibMajRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 1, 1),
    _RiZoneMibMajRev_Type()
)
riZoneMibMajRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneMibMajRev.setStatus("mandatory")
_RiZoneMibMinRev_Type = Integer32
_RiZoneMibMinRev_Object = MibScalar
riZoneMibMinRev = _RiZoneMibMinRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 1, 2),
    _RiZoneMibMinRev_Type()
)
riZoneMibMinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneMibMinRev.setStatus("mandatory")


class _RiZoneMibCondition_Type(Integer32):
    """Custom type riZoneMibCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4),
          ("configChanged", 5),
          ("timeout", 6))
    )


_RiZoneMibCondition_Type.__name__ = "Integer32"
_RiZoneMibCondition_Object = MibScalar
riZoneMibCondition = _RiZoneMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 1, 3),
    _RiZoneMibCondition_Type()
)
riZoneMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneMibCondition.setStatus("mandatory")
_RiZoneModules_ObjectIdentity = ObjectIdentity
riZoneModules = _RiZoneModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6, 2)
)


class _RiZoneCoreState_Type(Integer32):
    """Custom type riZoneCoreState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_RiZoneCoreState_Type.__name__ = "Integer32"
_RiZoneCoreState_Object = MibScalar
riZoneCoreState = _RiZoneCoreState_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 2, 1),
    _RiZoneCoreState_Type()
)
riZoneCoreState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneCoreState.setStatus("mandatory")


class _RiZoneCoreVersion_Type(DisplayString):
    """Custom type riZoneCoreVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RiZoneCoreVersion_Type.__name__ = "DisplayString"
_RiZoneCoreVersion_Object = MibScalar
riZoneCoreVersion = _RiZoneCoreVersion_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 2, 2),
    _RiZoneCoreVersion_Type()
)
riZoneCoreVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneCoreVersion.setStatus("mandatory")
_RiZoneProject_ObjectIdentity = ObjectIdentity
riZoneProject = _RiZoneProject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6, 3)
)


class _RiZoneProjectName_Type(DisplayString):
    """Custom type riZoneProjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RiZoneProjectName_Type.__name__ = "DisplayString"
_RiZoneProjectName_Object = MibScalar
riZoneProjectName = _RiZoneProjectName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 3, 1),
    _RiZoneProjectName_Type()
)
riZoneProjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneProjectName.setStatus("mandatory")


class _RiZoneProjectChangeTime_Type(DisplayString):
    """Custom type riZoneProjectChangeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_RiZoneProjectChangeTime_Type.__name__ = "DisplayString"
_RiZoneProjectChangeTime_Object = MibScalar
riZoneProjectChangeTime = _RiZoneProjectChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 3, 2),
    _RiZoneProjectChangeTime_Type()
)
riZoneProjectChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneProjectChangeTime.setStatus("mandatory")
_RiZoneStatus_ObjectIdentity = ObjectIdentity
riZoneStatus = _RiZoneStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4)
)
_RiZoneComponents_ObjectIdentity = ObjectIdentity
riZoneComponents = _RiZoneComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1)
)
_RiZoneNumberOfComponents_Type = Integer32
_RiZoneNumberOfComponents_Object = MibScalar
riZoneNumberOfComponents = _RiZoneNumberOfComponents_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 1),
    _RiZoneNumberOfComponents_Type()
)
riZoneNumberOfComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneNumberOfComponents.setStatus("mandatory")
_RiZoneComponentTable_Object = MibTable
riZoneComponentTable = _RiZoneComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    riZoneComponentTable.setStatus("mandatory")
_RiZoneComponentEntry_Object = MibTableRow
riZoneComponentEntry = _RiZoneComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1)
)
riZoneComponentEntry.setIndexNames(
    (0, "RITTAL-RIZONE-MIB", "componentIndex"),
)
if mibBuilder.loadTexts:
    riZoneComponentEntry.setStatus("mandatory")


class _ComponentIndex_Type(Integer32):
    """Custom type componentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ComponentIndex_Type.__name__ = "Integer32"
_ComponentIndex_Object = MibTableColumn
componentIndex = _ComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 1),
    _ComponentIndex_Type()
)
componentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentIndex.setStatus("mandatory")
_ComponentId_Type = Integer32
_ComponentId_Object = MibTableColumn
componentId = _ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 2),
    _ComponentId_Type()
)
componentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentId.setStatus("mandatory")


class _ComponentName_Type(DisplayString):
    """Custom type componentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ComponentName_Type.__name__ = "DisplayString"
_ComponentName_Object = MibTableColumn
componentName = _ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 3),
    _ComponentName_Type()
)
componentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentName.setStatus("mandatory")


class _ComponentType_Type(Integer32):
    """Custom type componentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("removed", 1),
          ("domain", 2),
          ("location", 3),
          ("building", 4),
          ("room", 5),
          ("rackrow", 6),
          ("rack", 7),
          ("device", 8),
          ("rackitem", 9))
    )


_ComponentType_Type.__name__ = "Integer32"
_ComponentType_Object = MibTableColumn
componentType = _ComponentType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 4),
    _ComponentType_Type()
)
componentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentType.setStatus("mandatory")
_ComponentParent_Type = Integer32
_ComponentParent_Object = MibTableColumn
componentParent = _ComponentParent_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 5),
    _ComponentParent_Type()
)
componentParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentParent.setStatus("mandatory")


class _ComponentStatusTotal_Type(Integer32):
    """Custom type componentStatusTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4),
          ("timeout", 5))
    )


_ComponentStatusTotal_Type.__name__ = "Integer32"
_ComponentStatusTotal_Object = MibTableColumn
componentStatusTotal = _ComponentStatusTotal_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 6),
    _ComponentStatusTotal_Type()
)
componentStatusTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatusTotal.setStatus("mandatory")


class _ComponentStatusAvailability_Type(Integer32):
    """Custom type componentStatusAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4),
          ("timeout", 5))
    )


_ComponentStatusAvailability_Type.__name__ = "Integer32"
_ComponentStatusAvailability_Object = MibTableColumn
componentStatusAvailability = _ComponentStatusAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 7),
    _ComponentStatusAvailability_Type()
)
componentStatusAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatusAvailability.setStatus("mandatory")


class _ComponentStatusCooling_Type(Integer32):
    """Custom type componentStatusCooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_ComponentStatusCooling_Type.__name__ = "Integer32"
_ComponentStatusCooling_Object = MibTableColumn
componentStatusCooling = _ComponentStatusCooling_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 8),
    _ComponentStatusCooling_Type()
)
componentStatusCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatusCooling.setStatus("mandatory")


class _ComponentStatusPower_Type(Integer32):
    """Custom type componentStatusPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_ComponentStatusPower_Type.__name__ = "Integer32"
_ComponentStatusPower_Object = MibTableColumn
componentStatusPower = _ComponentStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 9),
    _ComponentStatusPower_Type()
)
componentStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatusPower.setStatus("mandatory")


class _ComponentStatusMonitoring_Type(Integer32):
    """Custom type componentStatusMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_ComponentStatusMonitoring_Type.__name__ = "Integer32"
_ComponentStatusMonitoring_Object = MibTableColumn
componentStatusMonitoring = _ComponentStatusMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 10),
    _ComponentStatusMonitoring_Type()
)
componentStatusMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatusMonitoring.setStatus("mandatory")


class _ComponentStatusSecurity_Type(Integer32):
    """Custom type componentStatusSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_ComponentStatusSecurity_Type.__name__ = "Integer32"
_ComponentStatusSecurity_Object = MibTableColumn
componentStatusSecurity = _ComponentStatusSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 11),
    _ComponentStatusSecurity_Type()
)
componentStatusSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatusSecurity.setStatus("mandatory")


class _ComponentStatusCapacity_Type(Integer32):
    """Custom type componentStatusCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_ComponentStatusCapacity_Type.__name__ = "Integer32"
_ComponentStatusCapacity_Object = MibTableColumn
componentStatusCapacity = _ComponentStatusCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 12),
    _ComponentStatusCapacity_Type()
)
componentStatusCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatusCapacity.setStatus("mandatory")


class _ComponentStatusRack_Type(Integer32):
    """Custom type componentStatusRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_ComponentStatusRack_Type.__name__ = "Integer32"
_ComponentStatusRack_Object = MibTableColumn
componentStatusRack = _ComponentStatusRack_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 1, 2, 1, 13),
    _ComponentStatusRack_Type()
)
componentStatusRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatusRack.setStatus("mandatory")
_RiZoneVariables_ObjectIdentity = ObjectIdentity
riZoneVariables = _RiZoneVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2)
)
_RiZoneNumberOfVariables_Type = Integer32
_RiZoneNumberOfVariables_Object = MibScalar
riZoneNumberOfVariables = _RiZoneNumberOfVariables_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 1),
    _RiZoneNumberOfVariables_Type()
)
riZoneNumberOfVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneNumberOfVariables.setStatus("mandatory")
_RiZoneVariableTable_Object = MibTable
riZoneVariableTable = _RiZoneVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    riZoneVariableTable.setStatus("mandatory")
_RiZoneVariableEntry_Object = MibTableRow
riZoneVariableEntry = _RiZoneVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1)
)
riZoneVariableEntry.setIndexNames(
    (0, "RITTAL-RIZONE-MIB", "variableIndex"),
)
if mibBuilder.loadTexts:
    riZoneVariableEntry.setStatus("mandatory")


class _VariableIndex_Type(Integer32):
    """Custom type variableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VariableIndex_Type.__name__ = "Integer32"
_VariableIndex_Object = MibTableColumn
variableIndex = _VariableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 1),
    _VariableIndex_Type()
)
variableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableIndex.setStatus("mandatory")
_VariableId_Type = Integer32
_VariableId_Object = MibTableColumn
variableId = _VariableId_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 2),
    _VariableId_Type()
)
variableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableId.setStatus("mandatory")


class _VariableName_Type(DisplayString):
    """Custom type variableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_VariableName_Type.__name__ = "DisplayString"
_VariableName_Object = MibTableColumn
variableName = _VariableName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 3),
    _VariableName_Type()
)
variableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableName.setStatus("mandatory")


class _VariableMaintenanceGroup_Type(Integer32):
    """Custom type variableMaintenanceGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("cooling", 2),
          ("power", 4),
          ("rack", 8),
          ("monitoring", 16),
          ("remoting", 32),
          ("availability", 64),
          ("security", 128),
          ("capacity", 256))
    )


_VariableMaintenanceGroup_Type.__name__ = "Integer32"
_VariableMaintenanceGroup_Object = MibTableColumn
variableMaintenanceGroup = _VariableMaintenanceGroup_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 4),
    _VariableMaintenanceGroup_Type()
)
variableMaintenanceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableMaintenanceGroup.setStatus("mandatory")


class _VariableMeasurand_Type(Integer32):
    """Custom type variableMeasurand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("temperature", 2),
          ("current", 3),
          ("power", 4),
          ("effectivePower", 5),
          ("humidity", 6),
          ("voltage", 7),
          ("energy", 8),
          ("frequency", 9),
          ("access", 10),
          ("leakage", 11),
          ("percent", 12),
          ("rpm", 13),
          ("co2", 14),
          ("pue", 15),
          ("flow", 16),
          ("time", 17),
          ("costs", 18),
          ("imp", 19),
          ("heatCapacity", 20),
          ("constant", 21),
          ("temperatureDiff", 22),
          ("timespan", 23),
          ("cycles", 24),
          ("pulseRate", 34),
          ("pressure", 35),
          ("acceleration", 36),
          ("timeSpanTicks", 37))
    )


_VariableMeasurand_Type.__name__ = "Integer32"
_VariableMeasurand_Object = MibTableColumn
variableMeasurand = _VariableMeasurand_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 5),
    _VariableMeasurand_Type()
)
variableMeasurand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableMeasurand.setStatus("mandatory")
_VariableParentId_Type = Integer32
_VariableParentId_Object = MibTableColumn
variableParentId = _VariableParentId_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 6),
    _VariableParentId_Type()
)
variableParentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableParentId.setStatus("mandatory")


class _VariableType_Type(Integer32):
    """Custom type variableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("number", 1),
          ("string", 2),
          ("enum", 3))
    )


_VariableType_Type.__name__ = "Integer32"
_VariableType_Object = MibTableColumn
variableType = _VariableType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 7),
    _VariableType_Type()
)
variableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableType.setStatus("mandatory")


class _VariableQuality_Type(Integer32):
    """Custom type variableQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("good", 2),
          ("bad", 3))
    )


_VariableQuality_Type.__name__ = "Integer32"
_VariableQuality_Object = MibTableColumn
variableQuality = _VariableQuality_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 8),
    _VariableQuality_Type()
)
variableQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableQuality.setStatus("mandatory")
_VariableValueInt_Type = Integer32
_VariableValueInt_Object = MibTableColumn
variableValueInt = _VariableValueInt_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 9),
    _VariableValueInt_Type()
)
variableValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableValueInt.setStatus("mandatory")


class _VariableValueString_Type(DisplayString):
    """Custom type variableValueString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_VariableValueString_Type.__name__ = "DisplayString"
_VariableValueString_Object = MibTableColumn
variableValueString = _VariableValueString_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 10),
    _VariableValueString_Type()
)
variableValueString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    variableValueString.setStatus("mandatory")


class _VariableValueUnit_Type(DisplayString):
    """Custom type variableValueUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VariableValueUnit_Type.__name__ = "DisplayString"
_VariableValueUnit_Object = MibTableColumn
variableValueUnit = _VariableValueUnit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 11),
    _VariableValueUnit_Type()
)
variableValueUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableValueUnit.setStatus("mandatory")
_VariableDivisor_Type = Integer32
_VariableDivisor_Object = MibTableColumn
variableDivisor = _VariableDivisor_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 12),
    _VariableDivisor_Type()
)
variableDivisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableDivisor.setStatus("mandatory")
_VariableMultiplicator_Type = Integer32
_VariableMultiplicator_Object = MibTableColumn
variableMultiplicator = _VariableMultiplicator_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 2, 2, 1, 13),
    _VariableMultiplicator_Type()
)
variableMultiplicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableMultiplicator.setStatus("mandatory")


class _RiZoneStatusAvailability_Type(Integer32):
    """Custom type riZoneStatusAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4),
          ("timeout", 5))
    )


_RiZoneStatusAvailability_Type.__name__ = "Integer32"
_RiZoneStatusAvailability_Object = MibScalar
riZoneStatusAvailability = _RiZoneStatusAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 3),
    _RiZoneStatusAvailability_Type()
)
riZoneStatusAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneStatusAvailability.setStatus("mandatory")


class _RiZoneStatusCooling_Type(Integer32):
    """Custom type riZoneStatusCooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RiZoneStatusCooling_Type.__name__ = "Integer32"
_RiZoneStatusCooling_Object = MibScalar
riZoneStatusCooling = _RiZoneStatusCooling_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 4),
    _RiZoneStatusCooling_Type()
)
riZoneStatusCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneStatusCooling.setStatus("mandatory")


class _RiZoneStatusPower_Type(Integer32):
    """Custom type riZoneStatusPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RiZoneStatusPower_Type.__name__ = "Integer32"
_RiZoneStatusPower_Object = MibScalar
riZoneStatusPower = _RiZoneStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 5),
    _RiZoneStatusPower_Type()
)
riZoneStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneStatusPower.setStatus("mandatory")


class _RiZoneStatusMonitoring_Type(Integer32):
    """Custom type riZoneStatusMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RiZoneStatusMonitoring_Type.__name__ = "Integer32"
_RiZoneStatusMonitoring_Object = MibScalar
riZoneStatusMonitoring = _RiZoneStatusMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 6),
    _RiZoneStatusMonitoring_Type()
)
riZoneStatusMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneStatusMonitoring.setStatus("mandatory")


class _RiZoneStatusSecurity_Type(Integer32):
    """Custom type riZoneStatusSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RiZoneStatusSecurity_Type.__name__ = "Integer32"
_RiZoneStatusSecurity_Object = MibScalar
riZoneStatusSecurity = _RiZoneStatusSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 7),
    _RiZoneStatusSecurity_Type()
)
riZoneStatusSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneStatusSecurity.setStatus("mandatory")


class _RiZoneStatusCapacity_Type(Integer32):
    """Custom type riZoneStatusCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RiZoneStatusCapacity_Type.__name__ = "Integer32"
_RiZoneStatusCapacity_Object = MibScalar
riZoneStatusCapacity = _RiZoneStatusCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 8),
    _RiZoneStatusCapacity_Type()
)
riZoneStatusCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneStatusCapacity.setStatus("mandatory")


class _RiZoneStatusRack_Type(Integer32):
    """Custom type riZoneStatusRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_RiZoneStatusRack_Type.__name__ = "Integer32"
_RiZoneStatusRack_Object = MibScalar
riZoneStatusRack = _RiZoneStatusRack_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 4, 9),
    _RiZoneStatusRack_Type()
)
riZoneStatusRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneStatusRack.setStatus("mandatory")
_RiZoneCustomDefines_ObjectIdentity = ObjectIdentity
riZoneCustomDefines = _RiZoneCustomDefines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5)
)
_RiZoneCustomDefinedTraps_ObjectIdentity = ObjectIdentity
riZoneCustomDefinedTraps = _RiZoneCustomDefinedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1)
)
_RiZoneNumberOfTraps_Type = Integer32
_RiZoneNumberOfTraps_Object = MibScalar
riZoneNumberOfTraps = _RiZoneNumberOfTraps_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 1),
    _RiZoneNumberOfTraps_Type()
)
riZoneNumberOfTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riZoneNumberOfTraps.setStatus("mandatory")
_RiZoneCustomDefinedTrapsTable_Object = MibTable
riZoneCustomDefinedTrapsTable = _RiZoneCustomDefinedTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    riZoneCustomDefinedTrapsTable.setStatus("mandatory")
_RiZoneCustomDefinedTrapsEntry_Object = MibTableRow
riZoneCustomDefinedTrapsEntry = _RiZoneCustomDefinedTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1)
)
riZoneCustomDefinedTrapsEntry.setIndexNames(
    (0, "RITTAL-RIZONE-MIB", "customDefinedTrapIndex"),
)
if mibBuilder.loadTexts:
    riZoneCustomDefinedTrapsEntry.setStatus("mandatory")


class _CustomDefinedTrapIndex_Type(Integer32):
    """Custom type customDefinedTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CustomDefinedTrapIndex_Type.__name__ = "Integer32"
_CustomDefinedTrapIndex_Object = MibTableColumn
customDefinedTrapIndex = _CustomDefinedTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 1),
    _CustomDefinedTrapIndex_Type()
)
customDefinedTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customDefinedTrapIndex.setStatus("mandatory")


class _CdtMessageCategory_Type(Integer32):
    """Custom type cdtMessageCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("info", 2),
          ("warning", 3),
          ("error", 4),
          ("ok", 5))
    )


_CdtMessageCategory_Type.__name__ = "Integer32"
_CdtMessageCategory_Object = MibTableColumn
cdtMessageCategory = _CdtMessageCategory_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 2),
    _CdtMessageCategory_Type()
)
cdtMessageCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtMessageCategory.setStatus("mandatory")


class _CdtWorkflowId_Type(Integer32):
    """Custom type cdtWorkflowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdtWorkflowId_Type.__name__ = "Integer32"
_CdtWorkflowId_Object = MibTableColumn
cdtWorkflowId = _CdtWorkflowId_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 3),
    _CdtWorkflowId_Type()
)
cdtWorkflowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtWorkflowId.setStatus("mandatory")


class _CdtWorkflowName_Type(DisplayString):
    """Custom type cdtWorkflowName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtWorkflowName_Type.__name__ = "DisplayString"
_CdtWorkflowName_Object = MibTableColumn
cdtWorkflowName = _CdtWorkflowName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 4),
    _CdtWorkflowName_Type()
)
cdtWorkflowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtWorkflowName.setStatus("mandatory")


class _CdtFlowElementId_Type(DisplayString):
    """Custom type cdtFlowElementId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CdtFlowElementId_Type.__name__ = "DisplayString"
_CdtFlowElementId_Object = MibTableColumn
cdtFlowElementId = _CdtFlowElementId_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 5),
    _CdtFlowElementId_Type()
)
cdtFlowElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtFlowElementId.setStatus("mandatory")


class _CdtMessageText_Type(DisplayString):
    """Custom type cdtMessageText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtMessageText_Type.__name__ = "DisplayString"
_CdtMessageText_Object = MibTableColumn
cdtMessageText = _CdtMessageText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 6),
    _CdtMessageText_Type()
)
cdtMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtMessageText.setStatus("mandatory")


class _CdtVariableId_Type(Integer32):
    """Custom type cdtVariableId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdtVariableId_Type.__name__ = "Integer32"
_CdtVariableId_Object = MibTableColumn
cdtVariableId = _CdtVariableId_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 7),
    _CdtVariableId_Type()
)
cdtVariableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtVariableId.setStatus("mandatory")


class _CdtVariableName_Type(DisplayString):
    """Custom type cdtVariableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtVariableName_Type.__name__ = "DisplayString"
_CdtVariableName_Object = MibTableColumn
cdtVariableName = _CdtVariableName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 8),
    _CdtVariableName_Type()
)
cdtVariableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtVariableName.setStatus("mandatory")


class _CdtVariableValue_Type(Integer32):
    """Custom type cdtVariableValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdtVariableValue_Type.__name__ = "Integer32"
_CdtVariableValue_Object = MibTableColumn
cdtVariableValue = _CdtVariableValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 9),
    _CdtVariableValue_Type()
)
cdtVariableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtVariableValue.setStatus("mandatory")


class _CdtVariableTranslation_Type(DisplayString):
    """Custom type cdtVariableTranslation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtVariableTranslation_Type.__name__ = "DisplayString"
_CdtVariableTranslation_Object = MibTableColumn
cdtVariableTranslation = _CdtVariableTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 10),
    _CdtVariableTranslation_Type()
)
cdtVariableTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtVariableTranslation.setStatus("mandatory")


class _CdtVariableOwnerId_Type(Integer32):
    """Custom type cdtVariableOwnerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdtVariableOwnerId_Type.__name__ = "Integer32"
_CdtVariableOwnerId_Object = MibTableColumn
cdtVariableOwnerId = _CdtVariableOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 11),
    _CdtVariableOwnerId_Type()
)
cdtVariableOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtVariableOwnerId.setStatus("mandatory")


class _CdtVariableOwnerName_Type(DisplayString):
    """Custom type cdtVariableOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtVariableOwnerName_Type.__name__ = "DisplayString"
_CdtVariableOwnerName_Object = MibTableColumn
cdtVariableOwnerName = _CdtVariableOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 6, 5, 1, 2, 1, 12),
    _CdtVariableOwnerName_Type()
)
cdtVariableOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtVariableOwnerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

projectUpload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 6, 0, 1)
)
projectUpload.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("RITTAL-RIZONE-MIB", "riZoneProjectName"),
        ("RITTAL-RIZONE-MIB", "riZoneProjectChangeTime"))
)
if mibBuilder.loadTexts:
    projectUpload.setStatus(
        ""
    )

customDefinedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 6, 0, 2)
)
customDefinedTrap.setObjects(
      *(("RITTAL-RIZONE-MIB", "cdtMessageCategory"),
        ("RITTAL-RIZONE-MIB", "cdtWorkflowId"),
        ("RITTAL-RIZONE-MIB", "cdtWorkflowName"),
        ("RITTAL-RIZONE-MIB", "cdtMessageText"),
        ("RITTAL-RIZONE-MIB", "cdtVariableId"),
        ("RITTAL-RIZONE-MIB", "cdtVariableName"),
        ("RITTAL-RIZONE-MIB", "cdtVariableValue"),
        ("RITTAL-RIZONE-MIB", "cdtVariableTranslation"),
        ("RITTAL-RIZONE-MIB", "cdtVariableOwnerId"),
        ("RITTAL-RIZONE-MIB", "cdtVariableOwnerName"))
)
if mibBuilder.loadTexts:
    customDefinedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RITTAL-RIZONE-MIB",
    **{"rittal": rittal,
       "riZone": riZone,
       "projectUpload": projectUpload,
       "customDefinedTrap": customDefinedTrap,
       "riZoneMibRev": riZoneMibRev,
       "riZoneMibMajRev": riZoneMibMajRev,
       "riZoneMibMinRev": riZoneMibMinRev,
       "riZoneMibCondition": riZoneMibCondition,
       "riZoneModules": riZoneModules,
       "riZoneCoreState": riZoneCoreState,
       "riZoneCoreVersion": riZoneCoreVersion,
       "riZoneProject": riZoneProject,
       "riZoneProjectName": riZoneProjectName,
       "riZoneProjectChangeTime": riZoneProjectChangeTime,
       "riZoneStatus": riZoneStatus,
       "riZoneComponents": riZoneComponents,
       "riZoneNumberOfComponents": riZoneNumberOfComponents,
       "riZoneComponentTable": riZoneComponentTable,
       "riZoneComponentEntry": riZoneComponentEntry,
       "componentIndex": componentIndex,
       "componentId": componentId,
       "componentName": componentName,
       "componentType": componentType,
       "componentParent": componentParent,
       "componentStatusTotal": componentStatusTotal,
       "componentStatusAvailability": componentStatusAvailability,
       "componentStatusCooling": componentStatusCooling,
       "componentStatusPower": componentStatusPower,
       "componentStatusMonitoring": componentStatusMonitoring,
       "componentStatusSecurity": componentStatusSecurity,
       "componentStatusCapacity": componentStatusCapacity,
       "componentStatusRack": componentStatusRack,
       "riZoneVariables": riZoneVariables,
       "riZoneNumberOfVariables": riZoneNumberOfVariables,
       "riZoneVariableTable": riZoneVariableTable,
       "riZoneVariableEntry": riZoneVariableEntry,
       "variableIndex": variableIndex,
       "variableId": variableId,
       "variableName": variableName,
       "variableMaintenanceGroup": variableMaintenanceGroup,
       "variableMeasurand": variableMeasurand,
       "variableParentId": variableParentId,
       "variableType": variableType,
       "variableQuality": variableQuality,
       "variableValueInt": variableValueInt,
       "variableValueString": variableValueString,
       "variableValueUnit": variableValueUnit,
       "variableDivisor": variableDivisor,
       "variableMultiplicator": variableMultiplicator,
       "riZoneStatusAvailability": riZoneStatusAvailability,
       "riZoneStatusCooling": riZoneStatusCooling,
       "riZoneStatusPower": riZoneStatusPower,
       "riZoneStatusMonitoring": riZoneStatusMonitoring,
       "riZoneStatusSecurity": riZoneStatusSecurity,
       "riZoneStatusCapacity": riZoneStatusCapacity,
       "riZoneStatusRack": riZoneStatusRack,
       "riZoneCustomDefines": riZoneCustomDefines,
       "riZoneCustomDefinedTraps": riZoneCustomDefinedTraps,
       "riZoneNumberOfTraps": riZoneNumberOfTraps,
       "riZoneCustomDefinedTrapsTable": riZoneCustomDefinedTrapsTable,
       "riZoneCustomDefinedTrapsEntry": riZoneCustomDefinedTrapsEntry,
       "customDefinedTrapIndex": customDefinedTrapIndex,
       "cdtMessageCategory": cdtMessageCategory,
       "cdtWorkflowId": cdtWorkflowId,
       "cdtWorkflowName": cdtWorkflowName,
       "cdtFlowElementId": cdtFlowElementId,
       "cdtMessageText": cdtMessageText,
       "cdtVariableId": cdtVariableId,
       "cdtVariableName": cdtVariableName,
       "cdtVariableValue": cdtVariableValue,
       "cdtVariableTranslation": cdtVariableTranslation,
       "cdtVariableOwnerId": cdtVariableOwnerId,
       "cdtVariableOwnerName": cdtVariableOwnerName}
)
