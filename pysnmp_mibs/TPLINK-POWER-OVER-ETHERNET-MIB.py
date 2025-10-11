# SNMP MIB module (TPLINK-POWER-OVER-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-POWER-OVER-ETHERNET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:02 2025
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkPowerOverEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56)
)
if mibBuilder.loadTexts:
    tplinkPowerOverEthernetMIB.setRevisions(
        ("2013-07-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPoeMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPoeMIBObjects = _TplinkPoeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1)
)
_TpPoeConfig_ObjectIdentity = ObjectIdentity
tpPoeConfig = _TpPoeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1)
)
_TpPoeGlobal_ObjectIdentity = ObjectIdentity
tpPoeGlobal = _TpPoeGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 1)
)


class _TpSystemPowerLimit_Type(Integer32):
    """Custom type tpSystemPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200),
    )


_TpSystemPowerLimit_Type.__name__ = "Integer32"
_TpSystemPowerLimit_Object = MibScalar
tpSystemPowerLimit = _TpSystemPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 1, 1),
    _TpSystemPowerLimit_Type()
)
tpSystemPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSystemPowerLimit.setStatus("current")


class _TpPowerDisconnectMethod_Type(Integer32):
    """Custom type tpPowerDisconnectMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deny-lower-priority", 1)
    )


_TpPowerDisconnectMethod_Type.__name__ = "Integer32"
_TpPowerDisconnectMethod_Object = MibScalar
tpPowerDisconnectMethod = _TpPowerDisconnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 1, 2),
    _TpPowerDisconnectMethod_Type()
)
tpPowerDisconnectMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPowerDisconnectMethod.setStatus("current")


class _TpSystemPowerConsumption_Type(Integer32):
    """Custom type tpSystemPowerConsumption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200),
    )


_TpSystemPowerConsumption_Type.__name__ = "Integer32"
_TpSystemPowerConsumption_Object = MibScalar
tpSystemPowerConsumption = _TpSystemPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 1, 3),
    _TpSystemPowerConsumption_Type()
)
tpSystemPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSystemPowerConsumption.setStatus("current")


class _TpSystemPowerRemain_Type(Integer32):
    """Custom type tpSystemPowerRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200),
    )


_TpSystemPowerRemain_Type.__name__ = "Integer32"
_TpSystemPowerRemain_Object = MibScalar
tpSystemPowerRemain = _TpSystemPowerRemain_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 1, 4),
    _TpSystemPowerRemain_Type()
)
tpSystemPowerRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSystemPowerRemain.setStatus("current")
_TpPoePort_ObjectIdentity = ObjectIdentity
tpPoePort = _TpPoePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2)
)
_TpPoePortConfigTable_Object = MibTable
tpPoePortConfigTable = _TpPoePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpPoePortConfigTable.setStatus("current")
_TpPoePortConfigEntry_Object = MibTableRow
tpPoePortConfigEntry = _TpPoePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1)
)
tpPoePortConfigEntry.setIndexNames(
    (0, "TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoePortIndex"),
)
if mibBuilder.loadTexts:
    tpPoePortConfigEntry.setStatus("current")
_TpPoePortIndex_Type = Integer32
_TpPoePortIndex_Object = MibTableColumn
tpPoePortIndex = _TpPoePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 1),
    _TpPoePortIndex_Type()
)
tpPoePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPoePortIndex.setStatus("current")


class _TpPoePortStatus_Type(Integer32):
    """Custom type tpPoePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpPoePortStatus_Type.__name__ = "Integer32"
_TpPoePortStatus_Object = MibTableColumn
tpPoePortStatus = _TpPoePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 2),
    _TpPoePortStatus_Type()
)
tpPoePortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPoePortStatus.setStatus("current")


class _TpPoePriority_Type(Integer32):
    """Custom type tpPoePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("middle", 1),
          ("low", 2))
    )


_TpPoePriority_Type.__name__ = "Integer32"
_TpPoePriority_Object = MibTableColumn
tpPoePriority = _TpPoePriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 3),
    _TpPoePriority_Type()
)
tpPoePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPoePriority.setStatus("current")


class _TpPoePowerLimit_Type(Integer32):
    """Custom type tpPoePowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TpPoePowerLimit_Type.__name__ = "Integer32"
_TpPoePowerLimit_Object = MibTableColumn
tpPoePowerLimit = _TpPoePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 4),
    _TpPoePowerLimit_Type()
)
tpPoePowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPoePowerLimit.setStatus("current")


class _TpPoePortTimeRangeName_Type(OctetString):
    """Custom type tpPoePortTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpPoePortTimeRangeName_Type.__name__ = "OctetString"
_TpPoePortTimeRangeName_Object = MibTableColumn
tpPoePortTimeRangeName = _TpPoePortTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 5),
    _TpPoePortTimeRangeName_Type()
)
tpPoePortTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPoePortTimeRangeName.setStatus("current")


class _TpPoePortProfileName_Type(OctetString):
    """Custom type tpPoePortProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpPoePortProfileName_Type.__name__ = "OctetString"
_TpPoePortProfileName_Object = MibTableColumn
tpPoePortProfileName = _TpPoePortProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 6),
    _TpPoePortProfileName_Type()
)
tpPoePortProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPoePortProfileName.setStatus("current")


class _TpPoePower_Type(Integer32):
    """Custom type tpPoePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TpPoePower_Type.__name__ = "Integer32"
_TpPoePower_Object = MibTableColumn
tpPoePower = _TpPoePower_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 7),
    _TpPoePower_Type()
)
tpPoePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPoePower.setStatus("current")


class _TpPoeCurrent_Type(Integer32):
    """Custom type tpPoeCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TpPoeCurrent_Type.__name__ = "Integer32"
_TpPoeCurrent_Object = MibTableColumn
tpPoeCurrent = _TpPoeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 8),
    _TpPoeCurrent_Type()
)
tpPoeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPoeCurrent.setStatus("current")


class _TpPoeVoltage_Type(Integer32):
    """Custom type tpPoeVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TpPoeVoltage_Type.__name__ = "Integer32"
_TpPoeVoltage_Object = MibTableColumn
tpPoeVoltage = _TpPoeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 9),
    _TpPoeVoltage_Type()
)
tpPoeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPoeVoltage.setStatus("current")


class _TpPoeClass_Type(Integer32):
    """Custom type tpPoeClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class-not-defined", 7))
    )


_TpPoeClass_Type.__name__ = "Integer32"
_TpPoeClass_Object = MibTableColumn
tpPoeClass = _TpPoeClass_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 10),
    _TpPoeClass_Type()
)
tpPoeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPoeClass.setStatus("current")


class _TpPoePowerStatus_Type(Integer32):
    """Custom type tpPoePowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("off", 0),
          ("turning-on", 1),
          ("on", 2),
          ("overload", 3),
          ("short", 4),
          ("nonstandard-pd", 5),
          ("voltage-high", 6),
          ("voltage-low", 7),
          ("hardware-fault", 8),
          ("overtemperature", 9))
    )


_TpPoePowerStatus_Type.__name__ = "Integer32"
_TpPoePowerStatus_Object = MibTableColumn
tpPoePowerStatus = _TpPoePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 1, 2, 1, 1, 11),
    _TpPoePowerStatus_Type()
)
tpPoePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPoePowerStatus.setStatus("current")
_TpPoeProfile_ObjectIdentity = ObjectIdentity
tpPoeProfile = _TpPoeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2)
)
_TpPoeProfileTable_Object = MibTable
tpPoeProfileTable = _TpPoeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpPoeProfileTable.setStatus("current")
_TpPoeProfileEntry_Object = MibTableRow
tpPoeProfileEntry = _TpPoeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2, 1, 1)
)
tpPoeProfileEntry.setIndexNames(
    (0, "TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoeProfileName"),
)
if mibBuilder.loadTexts:
    tpPoeProfileEntry.setStatus("current")
_TpPoeProfileIndex_Type = Integer32
_TpPoeProfileIndex_Object = MibTableColumn
tpPoeProfileIndex = _TpPoeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2, 1, 1, 1),
    _TpPoeProfileIndex_Type()
)
tpPoeProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPoeProfileIndex.setStatus("current")


class _TpPoeProfileName_Type(OctetString):
    """Custom type tpPoeProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpPoeProfileName_Type.__name__ = "OctetString"
_TpPoeProfileName_Object = MibTableColumn
tpPoeProfileName = _TpPoeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2, 1, 1, 2),
    _TpPoeProfileName_Type()
)
tpPoeProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPoeProfileName.setStatus("current")


class _TpPoeProfilePortStatus_Type(Integer32):
    """Custom type tpPoeProfilePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpPoeProfilePortStatus_Type.__name__ = "Integer32"
_TpPoeProfilePortStatus_Object = MibTableColumn
tpPoeProfilePortStatus = _TpPoeProfilePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2, 1, 1, 3),
    _TpPoeProfilePortStatus_Type()
)
tpPoeProfilePortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPoeProfilePortStatus.setStatus("current")


class _TpPoeProfilePriority_Type(Integer32):
    """Custom type tpPoeProfilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("middle", 1),
          ("low", 2))
    )


_TpPoeProfilePriority_Type.__name__ = "Integer32"
_TpPoeProfilePriority_Object = MibTableColumn
tpPoeProfilePriority = _TpPoeProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2, 1, 1, 4),
    _TpPoeProfilePriority_Type()
)
tpPoeProfilePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPoeProfilePriority.setStatus("current")


class _TpPoeProfilePowerLimit_Type(Integer32):
    """Custom type tpPoeProfilePowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TpPoeProfilePowerLimit_Type.__name__ = "Integer32"
_TpPoeProfilePowerLimit_Object = MibTableColumn
tpPoeProfilePowerLimit = _TpPoeProfilePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2, 1, 1, 5),
    _TpPoeProfilePowerLimit_Type()
)
tpPoeProfilePowerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPoeProfilePowerLimit.setStatus("current")
_TpPoeProfileStatus_Type = TPRowStatus
_TpPoeProfileStatus_Object = MibTableColumn
tpPoeProfileStatus = _TpPoeProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 1, 2, 1, 1, 6),
    _TpPoeProfileStatus_Type()
)
tpPoeProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPoeProfileStatus.setStatus("current")
_TplinkPoeNotifications_ObjectIdentity = ObjectIdentity
tplinkPoeNotifications = _TplinkPoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 2)
)

# Managed Objects groups


# Notification objects

tpPoePortPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 2, 1)
)
tpPoePortPowerChange.setObjects(
      *(("TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoePortIndex"),
        ("TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoePortStatus"))
)
if mibBuilder.loadTexts:
    tpPoePortPowerChange.setStatus(
        "current"
    )

tpPoePortPowerOverLoading = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 2, 2)
)
tpPoePortPowerOverLoading.setObjects(
    ("TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoePortIndex")
)
if mibBuilder.loadTexts:
    tpPoePortPowerOverLoading.setStatus(
        "current"
    )

tpPoePortShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 2, 3)
)
tpPoePortShortCircuit.setObjects(
    ("TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoePortIndex")
)
if mibBuilder.loadTexts:
    tpPoePortShortCircuit.setStatus(
        "current"
    )

tpPoePortPowerOver30Watts = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 2, 4)
)
tpPoePortPowerOver30Watts.setObjects(
    ("TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoePortIndex")
)
if mibBuilder.loadTexts:
    tpPoePortPowerOver30Watts.setStatus(
        "current"
    )

tpPoePortPowerDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 2, 5)
)
tpPoePortPowerDeny.setObjects(
    ("TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoePortIndex")
)
if mibBuilder.loadTexts:
    tpPoePortPowerDeny.setStatus(
        "current"
    )

tpPoeThermalShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 2, 6)
)
tpPoeThermalShutdown.setObjects(
    ("TPLINK-POWER-OVER-ETHERNET-MIB", "tpPoePortIndex")
)
if mibBuilder.loadTexts:
    tpPoeThermalShutdown.setStatus(
        "current"
    )

tpPoeOverMaxPowerBudget = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 56, 2, 7)
)
tpPoeOverMaxPowerBudget.setObjects(
    ("TPLINK-POWER-OVER-ETHERNET-MIB", "tpSystemPowerLimit")
)
if mibBuilder.loadTexts:
    tpPoeOverMaxPowerBudget.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-POWER-OVER-ETHERNET-MIB",
    **{"tplinkPowerOverEthernetMIB": tplinkPowerOverEthernetMIB,
       "tplinkPoeMIBObjects": tplinkPoeMIBObjects,
       "tpPoeConfig": tpPoeConfig,
       "tpPoeGlobal": tpPoeGlobal,
       "tpSystemPowerLimit": tpSystemPowerLimit,
       "tpPowerDisconnectMethod": tpPowerDisconnectMethod,
       "tpSystemPowerConsumption": tpSystemPowerConsumption,
       "tpSystemPowerRemain": tpSystemPowerRemain,
       "tpPoePort": tpPoePort,
       "tpPoePortConfigTable": tpPoePortConfigTable,
       "tpPoePortConfigEntry": tpPoePortConfigEntry,
       "tpPoePortIndex": tpPoePortIndex,
       "tpPoePortStatus": tpPoePortStatus,
       "tpPoePriority": tpPoePriority,
       "tpPoePowerLimit": tpPoePowerLimit,
       "tpPoePortTimeRangeName": tpPoePortTimeRangeName,
       "tpPoePortProfileName": tpPoePortProfileName,
       "tpPoePower": tpPoePower,
       "tpPoeCurrent": tpPoeCurrent,
       "tpPoeVoltage": tpPoeVoltage,
       "tpPoeClass": tpPoeClass,
       "tpPoePowerStatus": tpPoePowerStatus,
       "tpPoeProfile": tpPoeProfile,
       "tpPoeProfileTable": tpPoeProfileTable,
       "tpPoeProfileEntry": tpPoeProfileEntry,
       "tpPoeProfileIndex": tpPoeProfileIndex,
       "tpPoeProfileName": tpPoeProfileName,
       "tpPoeProfilePortStatus": tpPoeProfilePortStatus,
       "tpPoeProfilePriority": tpPoeProfilePriority,
       "tpPoeProfilePowerLimit": tpPoeProfilePowerLimit,
       "tpPoeProfileStatus": tpPoeProfileStatus,
       "tplinkPoeNotifications": tplinkPoeNotifications,
       "tpPoePortPowerChange": tpPoePortPowerChange,
       "tpPoePortPowerOverLoading": tpPoePortPowerOverLoading,
       "tpPoePortShortCircuit": tpPoePortShortCircuit,
       "tpPoePortPowerOver30Watts": tpPoePortPowerOver30Watts,
       "tpPoePortPowerDeny": tpPoePortPowerDeny,
       "tpPoeThermalShutdown": tpPoeThermalShutdown,
       "tpPoeOverMaxPowerBudget": tpPoeOverMaxPowerBudget}
)
