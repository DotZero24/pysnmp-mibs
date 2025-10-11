# SNMP MIB module (RAISECOM-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-POE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:15 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(pethMainPseGroupIndex,
 pethPsePortGroupIndex,
 pethPsePortIndex) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseGroupIndex",
    "pethPsePortGroupIndex",
    "pethPsePortIndex")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcPoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51)
)
if mibBuilder.loadTexts:
    rcPoe.setRevisions(
        ("2007-11-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcPsePortTable_Object = MibTable
rcPsePortTable = _RcPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1)
)
if mibBuilder.loadTexts:
    rcPsePortTable.setStatus("current")
_RcPsePortEntry_Object = MibTableRow
rcPsePortEntry = _RcPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1)
)
rcPsePortEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    rcPsePortEntry.setStatus("current")
_RcPsePortPeakPower_Type = Unsigned32
_RcPsePortPeakPower_Object = MibTableColumn
rcPsePortPeakPower = _RcPsePortPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 1),
    _RcPsePortPeakPower_Type()
)
rcPsePortPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPsePortPeakPower.setStatus("current")
_RcPsePortAveragePower_Type = Unsigned32
_RcPsePortAveragePower_Object = MibTableColumn
rcPsePortAveragePower = _RcPsePortAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 2),
    _RcPsePortAveragePower_Type()
)
rcPsePortAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPsePortAveragePower.setStatus("current")
_RcPsePortCurrentPower_Type = Unsigned32
_RcPsePortCurrentPower_Object = MibTableColumn
rcPsePortCurrentPower = _RcPsePortCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 3),
    _RcPsePortCurrentPower_Type()
)
rcPsePortCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPsePortCurrentPower.setStatus("current")
_RcPsePortCurrentVoltage_Type = Unsigned32
_RcPsePortCurrentVoltage_Object = MibTableColumn
rcPsePortCurrentVoltage = _RcPsePortCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 4),
    _RcPsePortCurrentVoltage_Type()
)
rcPsePortCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPsePortCurrentVoltage.setStatus("current")
_RcPsePortCurrent_Type = Unsigned32
_RcPsePortCurrent_Object = MibTableColumn
rcPsePortCurrent = _RcPsePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 5),
    _RcPsePortCurrent_Type()
)
rcPsePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPsePortCurrent.setStatus("current")
_RcPsePortPowerLimit_Type = Unsigned32
_RcPsePortPowerLimit_Object = MibTableColumn
rcPsePortPowerLimit = _RcPsePortPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 6),
    _RcPsePortPowerLimit_Type()
)
rcPsePortPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPsePortPowerLimit.setStatus("current")


class _RcPsePortOperStatus_Type(Integer32):
    """Custom type rcPsePortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("force-power", 3))
    )


_RcPsePortOperStatus_Type.__name__ = "Integer32"
_RcPsePortOperStatus_Object = MibTableColumn
rcPsePortOperStatus = _RcPsePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 7),
    _RcPsePortOperStatus_Type()
)
rcPsePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPsePortOperStatus.setStatus("current")
_RcPsePortForcePower_Type = EnableVar
_RcPsePortForcePower_Object = MibTableColumn
rcPsePortForcePower = _RcPsePortForcePower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 8),
    _RcPsePortForcePower_Type()
)
rcPsePortForcePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPsePortForcePower.setStatus("current")


class _RcPsePortPoeProtectStatus_Type(OctetString):
    """Custom type rcPsePortPoeProtectStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_RcPsePortPoeProtectStatus_Type.__name__ = "OctetString"
_RcPsePortPoeProtectStatus_Object = MibTableColumn
rcPsePortPoeProtectStatus = _RcPsePortPoeProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 1, 1, 9),
    _RcPsePortPoeProtectStatus_Type()
)
rcPsePortPoeProtectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPsePortPoeProtectStatus.setStatus("current")
_RcMainPseTable_Object = MibTable
rcMainPseTable = _RcMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2)
)
if mibBuilder.loadTexts:
    rcMainPseTable.setStatus("current")
_RcMainPseEntry_Object = MibTableRow
rcMainPseEntry = _RcMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1)
)
rcMainPseEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    rcMainPseEntry.setStatus("current")
_RcMainPseAveragePower_Type = Unsigned32
_RcMainPseAveragePower_Object = MibTableColumn
rcMainPseAveragePower = _RcMainPseAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 1),
    _RcMainPseAveragePower_Type()
)
rcMainPseAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMainPseAveragePower.setStatus("current")
_RcMainPsePeakPower_Type = Unsigned32
_RcMainPsePeakPower_Object = MibTableColumn
rcMainPsePeakPower = _RcMainPsePeakPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 2),
    _RcMainPsePeakPower_Type()
)
rcMainPsePeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMainPsePeakPower.setStatus("current")
_RcMainPseLegacyDetectionEnable_Type = EnableVar
_RcMainPseLegacyDetectionEnable_Object = MibTableColumn
rcMainPseLegacyDetectionEnable = _RcMainPseLegacyDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 3),
    _RcMainPseLegacyDetectionEnable_Type()
)
rcMainPseLegacyDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMainPseLegacyDetectionEnable.setStatus("current")


class _RcMainPseManageMode_Type(Integer32):
    """Custom type rcMainPseManageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_RcMainPseManageMode_Type.__name__ = "Integer32"
_RcMainPseManageMode_Object = MibTableColumn
rcMainPseManageMode = _RcMainPseManageMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 4),
    _RcMainPseManageMode_Type()
)
rcMainPseManageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMainPseManageMode.setStatus("current")
_RcMainPseTemperatureProtect_Type = EnableVar
_RcMainPseTemperatureProtect_Object = MibTableColumn
rcMainPseTemperatureProtect = _RcMainPseTemperatureProtect_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 5),
    _RcMainPseTemperatureProtect_Type()
)
rcMainPseTemperatureProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMainPseTemperatureProtect.setStatus("current")


class _RcMainPseModuleOverTemp_Type(Integer32):
    """Custom type rcMainPseModuleOverTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcMainPseModuleOverTemp_Type.__name__ = "Integer32"
_RcMainPseModuleOverTemp_Object = MibTableColumn
rcMainPseModuleOverTemp = _RcMainPseModuleOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 6),
    _RcMainPseModuleOverTemp_Type()
)
rcMainPseModuleOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMainPseModuleOverTemp.setStatus("current")
_RcMainPseChipSupplyVoltage_Type = Unsigned32
_RcMainPseChipSupplyVoltage_Object = MibTableColumn
rcMainPseChipSupplyVoltage = _RcMainPseChipSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 7),
    _RcMainPseChipSupplyVoltage_Type()
)
rcMainPseChipSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMainPseChipSupplyVoltage.setStatus("current")


class _RcMainPseMode_Type(Integer32):
    """Custom type rcMainPseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("AF", 1),
          ("AT", 2))
    )


_RcMainPseMode_Type.__name__ = "Integer32"
_RcMainPseMode_Object = MibTableColumn
rcMainPseMode = _RcMainPseMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 8),
    _RcMainPseMode_Type()
)
rcMainPseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMainPseMode.setStatus("current")
_RcMainPseHighInrushEnable_Type = EnableVar
_RcMainPseHighInrushEnable_Object = MibTableColumn
rcMainPseHighInrushEnable = _RcMainPseHighInrushEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 9),
    _RcMainPseHighInrushEnable_Type()
)
rcMainPseHighInrushEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMainPseHighInrushEnable.setStatus("current")


class _RcMainPseCurrentProtectMode_Type(Integer32):
    """Custom type rcMainPseCurrentProtectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("class", 1),
          ("power", 2))
    )


_RcMainPseCurrentProtectMode_Type.__name__ = "Integer32"
_RcMainPseCurrentProtectMode_Object = MibTableColumn
rcMainPseCurrentProtectMode = _RcMainPseCurrentProtectMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 2, 1, 10),
    _RcMainPseCurrentProtectMode_Type()
)
rcMainPseCurrentProtectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMainPseCurrentProtectMode.setStatus("current")
_RcPoeNotifications_ObjectIdentity = ObjectIdentity
rcPoeNotifications = _RcPoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 3)
)

# Managed Objects groups


# Notification objects

rcMainPseOverTempreture = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 51, 3, 1)
)
rcMainPseOverTempreture.setObjects(
    ("RAISECOM-POE-MIB", "rcMainPseModuleOverTemp")
)
if mibBuilder.loadTexts:
    rcMainPseOverTempreture.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-POE-MIB",
    **{"rcPoe": rcPoe,
       "rcPsePortTable": rcPsePortTable,
       "rcPsePortEntry": rcPsePortEntry,
       "rcPsePortPeakPower": rcPsePortPeakPower,
       "rcPsePortAveragePower": rcPsePortAveragePower,
       "rcPsePortCurrentPower": rcPsePortCurrentPower,
       "rcPsePortCurrentVoltage": rcPsePortCurrentVoltage,
       "rcPsePortCurrent": rcPsePortCurrent,
       "rcPsePortPowerLimit": rcPsePortPowerLimit,
       "rcPsePortOperStatus": rcPsePortOperStatus,
       "rcPsePortForcePower": rcPsePortForcePower,
       "rcPsePortPoeProtectStatus": rcPsePortPoeProtectStatus,
       "rcMainPseTable": rcMainPseTable,
       "rcMainPseEntry": rcMainPseEntry,
       "rcMainPseAveragePower": rcMainPseAveragePower,
       "rcMainPsePeakPower": rcMainPsePeakPower,
       "rcMainPseLegacyDetectionEnable": rcMainPseLegacyDetectionEnable,
       "rcMainPseManageMode": rcMainPseManageMode,
       "rcMainPseTemperatureProtect": rcMainPseTemperatureProtect,
       "rcMainPseModuleOverTemp": rcMainPseModuleOverTemp,
       "rcMainPseChipSupplyVoltage": rcMainPseChipSupplyVoltage,
       "rcMainPseMode": rcMainPseMode,
       "rcMainPseHighInrushEnable": rcMainPseHighInrushEnable,
       "rcMainPseCurrentProtectMode": rcMainPseCurrentProtectMode,
       "rcPoeNotifications": rcPoeNotifications,
       "rcMainPseOverTempreture": rcMainPseOverTempreture}
)
