# SNMP MIB module (ELTEX-ERRDISABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-ERRDISABLE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:29 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

eltexErrdisableMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 53)
)
if mibBuilder.loadTexts:
    eltexErrdisableMIB.setRevisions(
        ("2023-03-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexErrdisableCauseType(TextualConvention, Integer32):
    status = "current"
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
        *(("storm-control", 1),
          ("loopback-detection", 2),
          ("udld", 3),
          ("port-security", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EltexErrdisableObjects_ObjectIdentity = ObjectIdentity
eltexErrdisableObjects = _EltexErrdisableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1)
)
_EltexErrdisableGlobals_ObjectIdentity = ObjectIdentity
eltexErrdisableGlobals = _EltexErrdisableGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 1)
)
_EltexErrdisableReactivateInterface_Type = InterfaceIndexOrZero
_EltexErrdisableReactivateInterface_Object = MibScalar
eltexErrdisableReactivateInterface = _EltexErrdisableReactivateInterface_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 1, 1),
    _EltexErrdisableReactivateInterface_Type()
)
eltexErrdisableReactivateInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErrdisableReactivateInterface.setStatus("current")


class _EltexErrdisableGlobalRecoveryInterval_Type(Integer32):
    """Custom type eltexErrdisableGlobalRecoveryInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_EltexErrdisableGlobalRecoveryInterval_Type.__name__ = "Integer32"
_EltexErrdisableGlobalRecoveryInterval_Object = MibScalar
eltexErrdisableGlobalRecoveryInterval = _EltexErrdisableGlobalRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 1, 2),
    _EltexErrdisableGlobalRecoveryInterval_Type()
)
eltexErrdisableGlobalRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErrdisableGlobalRecoveryInterval.setStatus("current")
if mibBuilder.loadTexts:
    eltexErrdisableGlobalRecoveryInterval.setUnits("seconds")
_EltexErrdisableConfigs_ObjectIdentity = ObjectIdentity
eltexErrdisableConfigs = _EltexErrdisableConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 2)
)
_EltexErrdisableConfigTable_Object = MibTable
eltexErrdisableConfigTable = _EltexErrdisableConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexErrdisableConfigTable.setStatus("current")
_EltexErrdisableConfigEntry_Object = MibTableRow
eltexErrdisableConfigEntry = _EltexErrdisableConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 2, 1, 1)
)
eltexErrdisableConfigEntry.setIndexNames(
    (0, "ELTEX-ERRDISABLE-MIB", "eltexErrdisableConfigCause"),
)
if mibBuilder.loadTexts:
    eltexErrdisableConfigEntry.setStatus("current")
_EltexErrdisableConfigCause_Type = EltexErrdisableCauseType
_EltexErrdisableConfigCause_Object = MibTableColumn
eltexErrdisableConfigCause = _EltexErrdisableConfigCause_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 2, 1, 1, 1),
    _EltexErrdisableConfigCause_Type()
)
eltexErrdisableConfigCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexErrdisableConfigCause.setStatus("current")
_EltexErrdisableConfigRecoveryEnable_Type = TruthValue
_EltexErrdisableConfigRecoveryEnable_Object = MibTableColumn
eltexErrdisableConfigRecoveryEnable = _EltexErrdisableConfigRecoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 2, 1, 1, 2),
    _EltexErrdisableConfigRecoveryEnable_Type()
)
eltexErrdisableConfigRecoveryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErrdisableConfigRecoveryEnable.setStatus("current")
_EltexErrdisableConfigTrapEnable_Type = TruthValue
_EltexErrdisableConfigTrapEnable_Object = MibTableColumn
eltexErrdisableConfigTrapEnable = _EltexErrdisableConfigTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 2, 1, 1, 3),
    _EltexErrdisableConfigTrapEnable_Type()
)
eltexErrdisableConfigTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErrdisableConfigTrapEnable.setStatus("current")
_EltexErrdisableStatistics_ObjectIdentity = ObjectIdentity
eltexErrdisableStatistics = _EltexErrdisableStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 3)
)
_EltexErrdisableIfStatusTable_Object = MibTable
eltexErrdisableIfStatusTable = _EltexErrdisableIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltexErrdisableIfStatusTable.setStatus("current")
_EltexErrdisableIfStatusEntry_Object = MibTableRow
eltexErrdisableIfStatusEntry = _EltexErrdisableIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 3, 1, 1)
)
eltexErrdisableIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltexErrdisableIfStatusEntry.setStatus("current")
_EltexErrdisableIfStatusCause_Type = EltexErrdisableCauseType
_EltexErrdisableIfStatusCause_Object = MibTableColumn
eltexErrdisableIfStatusCause = _EltexErrdisableIfStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 3, 1, 1, 1),
    _EltexErrdisableIfStatusCause_Type()
)
eltexErrdisableIfStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexErrdisableIfStatusCause.setStatus("current")
_EltexErrdisableIfStatusRecoveryEnable_Type = TruthValue
_EltexErrdisableIfStatusRecoveryEnable_Object = MibTableColumn
eltexErrdisableIfStatusRecoveryEnable = _EltexErrdisableIfStatusRecoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 53, 1, 3, 1, 1, 2),
    _EltexErrdisableIfStatusRecoveryEnable_Type()
)
eltexErrdisableIfStatusRecoveryEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexErrdisableIfStatusRecoveryEnable.setStatus("current")
_EltexErrdisableNotifications_ObjectIdentity = ObjectIdentity
eltexErrdisableNotifications = _EltexErrdisableNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 53, 2)
)
_EltexErrdisableNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltexErrdisableNotificationsPrefix = _EltexErrdisableNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 53, 2, 0)
)

# Managed Objects groups


# Notification objects

eltexErrdisableIfSuspendedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 53, 2, 0, 1)
)
eltexErrdisableIfSuspendedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ELTEX-ERRDISABLE-MIB", "eltexErrdisableIfStatusCause"))
)
if mibBuilder.loadTexts:
    eltexErrdisableIfSuspendedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-ERRDISABLE-MIB",
    **{"EltexErrdisableCauseType": EltexErrdisableCauseType,
       "eltexErrdisableMIB": eltexErrdisableMIB,
       "eltexErrdisableObjects": eltexErrdisableObjects,
       "eltexErrdisableGlobals": eltexErrdisableGlobals,
       "eltexErrdisableReactivateInterface": eltexErrdisableReactivateInterface,
       "eltexErrdisableGlobalRecoveryInterval": eltexErrdisableGlobalRecoveryInterval,
       "eltexErrdisableConfigs": eltexErrdisableConfigs,
       "eltexErrdisableConfigTable": eltexErrdisableConfigTable,
       "eltexErrdisableConfigEntry": eltexErrdisableConfigEntry,
       "eltexErrdisableConfigCause": eltexErrdisableConfigCause,
       "eltexErrdisableConfigRecoveryEnable": eltexErrdisableConfigRecoveryEnable,
       "eltexErrdisableConfigTrapEnable": eltexErrdisableConfigTrapEnable,
       "eltexErrdisableStatistics": eltexErrdisableStatistics,
       "eltexErrdisableIfStatusTable": eltexErrdisableIfStatusTable,
       "eltexErrdisableIfStatusEntry": eltexErrdisableIfStatusEntry,
       "eltexErrdisableIfStatusCause": eltexErrdisableIfStatusCause,
       "eltexErrdisableIfStatusRecoveryEnable": eltexErrdisableIfStatusRecoveryEnable,
       "eltexErrdisableNotifications": eltexErrdisableNotifications,
       "eltexErrdisableNotificationsPrefix": eltexErrdisableNotificationsPrefix,
       "eltexErrdisableIfSuspendedTrap": eltexErrdisableIfSuspendedTrap}
)
