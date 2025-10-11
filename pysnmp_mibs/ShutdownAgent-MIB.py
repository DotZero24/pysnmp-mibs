# SNMP MIB module (ShutdownAgent-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/delta/ShutdownAgent-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:56:41 2025
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

_Delta_ObjectIdentity = ObjectIdentity
delta = _Delta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2)
)
_Shutdownagent_ObjectIdentity = ObjectIdentity
shutdownagent = _Shutdownagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200)
)
_DagentMonitor_ObjectIdentity = ObjectIdentity
dagentMonitor = _DagentMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 1)
)


class _DagentOSVersion_Type(DisplayString):
    """Custom type dagentOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DagentOSVersion_Type.__name__ = "DisplayString"
_DagentOSVersion_Object = MibScalar
dagentOSVersion = _DagentOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 1, 1),
    _DagentOSVersion_Type()
)
dagentOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dagentOSVersion.setStatus("mandatory")


class _DagentSoftwareVersion_Type(DisplayString):
    """Custom type dagentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DagentSoftwareVersion_Type.__name__ = "DisplayString"
_DagentSoftwareVersion_Object = MibScalar
dagentSoftwareVersion = _DagentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 1, 2),
    _DagentSoftwareVersion_Type()
)
dagentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dagentSoftwareVersion.setStatus("mandatory")


class _DagentIsOSCountdown_Type(Integer32):
    """Custom type dagentIsOSCountdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_DagentIsOSCountdown_Type.__name__ = "Integer32"
_DagentIsOSCountdown_Object = MibScalar
dagentIsOSCountdown = _DagentIsOSCountdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 1, 3),
    _DagentIsOSCountdown_Type()
)
dagentIsOSCountdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dagentIsOSCountdown.setStatus("mandatory")
_DagentOSCountdown_Type = Integer32
_DagentOSCountdown_Object = MibScalar
dagentOSCountdown = _DagentOSCountdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 1, 4),
    _DagentOSCountdown_Type()
)
dagentOSCountdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dagentOSCountdown.setStatus("mandatory")
if mibBuilder.loadTexts:
    dagentOSCountdown.setUnits("second")


class _DagentShutdownReason_Type(Integer32):
    """Custom type dagentShutdownReason based on Integer32"""
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
        *(("none", 1),
          ("power_fail", 2),
          ("battery_low", 3),
          ("overload", 4),
          ("on_bypass", 5),
          ("smart_shutdown", 6))
    )


_DagentShutdownReason_Type.__name__ = "Integer32"
_DagentShutdownReason_Object = MibScalar
dagentShutdownReason = _DagentShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 1, 5),
    _DagentShutdownReason_Type()
)
dagentShutdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dagentShutdownReason.setStatus("mandatory")


class _DagentHostName_Type(DisplayString):
    """Custom type dagentHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DagentHostName_Type.__name__ = "DisplayString"
_DagentHostName_Object = MibScalar
dagentHostName = _DagentHostName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 1, 6),
    _DagentHostName_Type()
)
dagentHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dagentHostName.setStatus("mandatory")
_DagentConfigure_ObjectIdentity = ObjectIdentity
dagentConfigure = _DagentConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2)
)


class _DagentSetShutdownType_Type(Integer32):
    """Custom type dagentSetShutdownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("power_off", 2),
          ("hibernate", 3))
    )


_DagentSetShutdownType_Type.__name__ = "Integer32"
_DagentSetShutdownType_Object = MibScalar
dagentSetShutdownType = _DagentSetShutdownType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 1),
    _DagentSetShutdownType_Type()
)
dagentSetShutdownType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetShutdownType.setStatus("mandatory")


class _DagentSetEnablePowerFail_Type(Integer32):
    """Custom type dagentSetEnablePowerFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DagentSetEnablePowerFail_Type.__name__ = "Integer32"
_DagentSetEnablePowerFail_Object = MibScalar
dagentSetEnablePowerFail = _DagentSetEnablePowerFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 2),
    _DagentSetEnablePowerFail_Type()
)
dagentSetEnablePowerFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetEnablePowerFail.setStatus("mandatory")
_DagentSetOSDelayPowerFail_Type = Integer32
_DagentSetOSDelayPowerFail_Object = MibScalar
dagentSetOSDelayPowerFail = _DagentSetOSDelayPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 3),
    _DagentSetOSDelayPowerFail_Type()
)
dagentSetOSDelayPowerFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetOSDelayPowerFail.setStatus("mandatory")
if mibBuilder.loadTexts:
    dagentSetOSDelayPowerFail.setUnits("second")


class _DagentSetEnableBatteryLow_Type(Integer32):
    """Custom type dagentSetEnableBatteryLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DagentSetEnableBatteryLow_Type.__name__ = "Integer32"
_DagentSetEnableBatteryLow_Object = MibScalar
dagentSetEnableBatteryLow = _DagentSetEnableBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 4),
    _DagentSetEnableBatteryLow_Type()
)
dagentSetEnableBatteryLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetEnableBatteryLow.setStatus("mandatory")
_DagentSetOSDelayBatteryLow_Type = Integer32
_DagentSetOSDelayBatteryLow_Object = MibScalar
dagentSetOSDelayBatteryLow = _DagentSetOSDelayBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 5),
    _DagentSetOSDelayBatteryLow_Type()
)
dagentSetOSDelayBatteryLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetOSDelayBatteryLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    dagentSetOSDelayBatteryLow.setUnits("second")


class _DagentSetEnableOverload_Type(Integer32):
    """Custom type dagentSetEnableOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DagentSetEnableOverload_Type.__name__ = "Integer32"
_DagentSetEnableOverload_Object = MibScalar
dagentSetEnableOverload = _DagentSetEnableOverload_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 6),
    _DagentSetEnableOverload_Type()
)
dagentSetEnableOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetEnableOverload.setStatus("mandatory")
_DagentSetOSDelayOverload_Type = Integer32
_DagentSetOSDelayOverload_Object = MibScalar
dagentSetOSDelayOverload = _DagentSetOSDelayOverload_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 7),
    _DagentSetOSDelayOverload_Type()
)
dagentSetOSDelayOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetOSDelayOverload.setStatus("mandatory")
if mibBuilder.loadTexts:
    dagentSetOSDelayOverload.setUnits("second")


class _DagentSetEnableBypass_Type(Integer32):
    """Custom type dagentSetEnableBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DagentSetEnableBypass_Type.__name__ = "Integer32"
_DagentSetEnableBypass_Object = MibScalar
dagentSetEnableBypass = _DagentSetEnableBypass_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 8),
    _DagentSetEnableBypass_Type()
)
dagentSetEnableBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetEnableBypass.setStatus("mandatory")
_DagentSetOSDelayBypass_Type = Integer32
_DagentSetOSDelayBypass_Object = MibScalar
dagentSetOSDelayBypass = _DagentSetOSDelayBypass_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 9),
    _DagentSetOSDelayBypass_Type()
)
dagentSetOSDelayBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetOSDelayBypass.setStatus("mandatory")
if mibBuilder.loadTexts:
    dagentSetOSDelayBypass.setUnits("second")


class _DagentSetEnableSmartShutdown_Type(Integer32):
    """Custom type dagentSetEnableSmartShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DagentSetEnableSmartShutdown_Type.__name__ = "Integer32"
_DagentSetEnableSmartShutdown_Object = MibScalar
dagentSetEnableSmartShutdown = _DagentSetEnableSmartShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 10),
    _DagentSetEnableSmartShutdown_Type()
)
dagentSetEnableSmartShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetEnableSmartShutdown.setStatus("mandatory")
_DagentSetOSDelaySmartShutdown_Type = Integer32
_DagentSetOSDelaySmartShutdown_Object = MibScalar
dagentSetOSDelaySmartShutdown = _DagentSetOSDelaySmartShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 2, 11),
    _DagentSetOSDelaySmartShutdown_Type()
)
dagentSetOSDelaySmartShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentSetOSDelaySmartShutdown.setStatus("mandatory")
if mibBuilder.loadTexts:
    dagentSetOSDelaySmartShutdown.setUnits("second")
_DagentControl_ObjectIdentity = ObjectIdentity
dagentControl = _DagentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 3)
)


class _DagentCancelShutdown_Type(Integer32):
    """Custom type dagentCancelShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 1),
          ("resume", 2))
    )


_DagentCancelShutdown_Type.__name__ = "Integer32"
_DagentCancelShutdown_Object = MibScalar
dagentCancelShutdown = _DagentCancelShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 200, 3, 1),
    _DagentCancelShutdown_Type()
)
dagentCancelShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dagentCancelShutdown.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ShutdownAgent-MIB",
    **{"delta": delta,
       "ups": ups,
       "shutdownagent": shutdownagent,
       "dagentMonitor": dagentMonitor,
       "dagentOSVersion": dagentOSVersion,
       "dagentSoftwareVersion": dagentSoftwareVersion,
       "dagentIsOSCountdown": dagentIsOSCountdown,
       "dagentOSCountdown": dagentOSCountdown,
       "dagentShutdownReason": dagentShutdownReason,
       "dagentHostName": dagentHostName,
       "dagentConfigure": dagentConfigure,
       "dagentSetShutdownType": dagentSetShutdownType,
       "dagentSetEnablePowerFail": dagentSetEnablePowerFail,
       "dagentSetOSDelayPowerFail": dagentSetOSDelayPowerFail,
       "dagentSetEnableBatteryLow": dagentSetEnableBatteryLow,
       "dagentSetOSDelayBatteryLow": dagentSetOSDelayBatteryLow,
       "dagentSetEnableOverload": dagentSetEnableOverload,
       "dagentSetOSDelayOverload": dagentSetOSDelayOverload,
       "dagentSetEnableBypass": dagentSetEnableBypass,
       "dagentSetOSDelayBypass": dagentSetOSDelayBypass,
       "dagentSetEnableSmartShutdown": dagentSetEnableSmartShutdown,
       "dagentSetOSDelaySmartShutdown": dagentSetOSDelaySmartShutdown,
       "dagentControl": dagentControl,
       "dagentCancelShutdown": dagentCancelShutdown}
)
