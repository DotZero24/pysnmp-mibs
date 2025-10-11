# SNMP MIB module (ELTEX-MES-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-POE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:18 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

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

eltMesPoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 16)
)
if mibBuilder.loadTexts:
    eltMesPoe.setRevisions(
        ("2019-04-02 00:00",
         "2017-11-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesPoeNotifications_ObjectIdentity = ObjectIdentity
eltMesPoeNotifications = _EltMesPoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 0)
)
_EltMesPoeObjects_ObjectIdentity = ObjectIdentity
eltMesPoeObjects = _EltMesPoeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 1)
)


class _EltPoeRestartAction_Type(Integer32):
    """Custom type eltPoeRestartAction based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
        ValueRangeConstraint(255, 255),
    )


_EltPoeRestartAction_Type.__name__ = "Integer32"
_EltPoeRestartAction_Object = MibScalar
eltPoeRestartAction = _EltPoeRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 1, 1),
    _EltPoeRestartAction_Type()
)
eltPoeRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPoeRestartAction.setStatus("current")


class _EltPoeDisabled_Type(TruthValue):
    """Custom type eltPoeDisabled based on TruthValue"""
    defaultValue = 1


_EltPoeDisabled_Type.__name__ = "TruthValue"
_EltPoeDisabled_Object = MibScalar
eltPoeDisabled = _EltPoeDisabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 1, 2),
    _EltPoeDisabled_Type()
)
eltPoeDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPoeDisabled.setStatus("current")


class _EltPoeAutoRestart_Type(TruthValue):
    """Custom type eltPoeAutoRestart based on TruthValue"""
    defaultValue = 1


_EltPoeAutoRestart_Type.__name__ = "TruthValue"
_EltPoeAutoRestart_Object = MibScalar
eltPoeAutoRestart = _EltPoeAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 1, 3),
    _EltPoeAutoRestart_Type()
)
eltPoeAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPoeAutoRestart.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-POE-MIB",
    **{"eltMesPoe": eltMesPoe,
       "eltMesPoeNotifications": eltMesPoeNotifications,
       "eltMesPoeObjects": eltMesPoeObjects,
       "eltPoeRestartAction": eltPoeRestartAction,
       "eltPoeDisabled": eltPoeDisabled,
       "eltPoeAutoRestart": eltPoeAutoRestart}
)
