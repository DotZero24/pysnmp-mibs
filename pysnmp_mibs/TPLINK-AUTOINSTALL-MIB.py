# SNMP MIB module (TPLINK-AUTOINSTALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-AUTOINSTALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:08 2025
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


# MODULE-IDENTITY

tplinkAutoInstallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97)
)
if mibBuilder.loadTexts:
    tplinkAutoInstallMIB.setRevisions(
        ("2012-12-17 10:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkAutoInstallMIBObjects_ObjectIdentity = ObjectIdentity
tplinkAutoInstallMIBObjects = _TplinkAutoInstallMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 1)
)
_AutoInstallConfig_ObjectIdentity = ObjectIdentity
autoInstallConfig = _AutoInstallConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1)
)


class _AutoInstallStartStop_Type(Integer32):
    """Custom type autoInstallStartStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stop", 0),
          ("start", 1))
    )


_AutoInstallStartStop_Type.__name__ = "Integer32"
_AutoInstallStartStop_Object = MibScalar
autoInstallStartStop = _AutoInstallStartStop_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 1),
    _AutoInstallStartStop_Type()
)
autoInstallStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoInstallStartStop.setStatus("current")


class _AutoInstallPersistentMode_Type(Integer32):
    """Custom type autoInstallPersistentMode based on Integer32"""
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


_AutoInstallPersistentMode_Type.__name__ = "Integer32"
_AutoInstallPersistentMode_Object = MibScalar
autoInstallPersistentMode = _AutoInstallPersistentMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 2),
    _AutoInstallPersistentMode_Type()
)
autoInstallPersistentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoInstallPersistentMode.setStatus("current")


class _AutoInstallAutoSave_Type(Integer32):
    """Custom type autoInstallAutoSave based on Integer32"""
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


_AutoInstallAutoSave_Type.__name__ = "Integer32"
_AutoInstallAutoSave_Object = MibScalar
autoInstallAutoSave = _AutoInstallAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 3),
    _AutoInstallAutoSave_Type()
)
autoInstallAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoInstallAutoSave.setStatus("current")


class _AutoInstallAutoReboot_Type(Integer32):
    """Custom type autoInstallAutoReboot based on Integer32"""
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


_AutoInstallAutoReboot_Type.__name__ = "Integer32"
_AutoInstallAutoReboot_Object = MibScalar
autoInstallAutoReboot = _AutoInstallAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 4),
    _AutoInstallAutoReboot_Type()
)
autoInstallAutoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoInstallAutoReboot.setStatus("current")


class _AutoInstallRetryCount_Type(Integer32):
    """Custom type autoInstallRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AutoInstallRetryCount_Type.__name__ = "Integer32"
_AutoInstallRetryCount_Object = MibScalar
autoInstallRetryCount = _AutoInstallRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 5),
    _AutoInstallRetryCount_Type()
)
autoInstallRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoInstallRetryCount.setStatus("current")


class _AutoInstallState_Type(OctetString):
    """Custom type autoInstallState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AutoInstallState_Type.__name__ = "OctetString"
_AutoInstallState_Object = MibScalar
autoInstallState = _AutoInstallState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 6),
    _AutoInstallState_Type()
)
autoInstallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoInstallState.setStatus("current")
_TplinkAutoInstallNotifications_ObjectIdentity = ObjectIdentity
tplinkAutoInstallNotifications = _TplinkAutoInstallNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 97, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-AUTOINSTALL-MIB",
    **{"tplinkAutoInstallMIB": tplinkAutoInstallMIB,
       "tplinkAutoInstallMIBObjects": tplinkAutoInstallMIBObjects,
       "autoInstallConfig": autoInstallConfig,
       "autoInstallStartStop": autoInstallStartStop,
       "autoInstallPersistentMode": autoInstallPersistentMode,
       "autoInstallAutoSave": autoInstallAutoSave,
       "autoInstallAutoReboot": autoInstallAutoReboot,
       "autoInstallRetryCount": autoInstallRetryCount,
       "autoInstallState": autoInstallState,
       "tplinkAutoInstallNotifications": tplinkAutoInstallNotifications}
)
