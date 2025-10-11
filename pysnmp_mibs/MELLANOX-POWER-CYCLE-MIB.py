# SNMP MIB module (MELLANOX-POWER-CYCLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mellanox/MELLANOX-POWER-CYCLE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:45 2025
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

(mellanoxPowerCycle,) = mibBuilder.importSymbols(
    "MELLANOX-SMI-MIB",
    "mellanoxPowerCycle")

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


# MODULE-IDENTITY

mellanoxPowerCycleMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 10, 1)
)
if mibBuilder.loadTexts:
    mellanoxPowerCycleMib.setRevisions(
        ("2018-06-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MellanoxPowerCycleMibObjects_ObjectIdentity = ObjectIdentity
mellanoxPowerCycleMibObjects = _MellanoxPowerCycleMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 10, 1, 1)
)
_MellanoxPowerCycleCmd_ObjectIdentity = ObjectIdentity
mellanoxPowerCycleCmd = _MellanoxPowerCycleCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 2)
)


class _MellanoxPowerCycleCmdExecute_Type(Integer32):
    """Custom type mellanoxPowerCycleCmdExecute based on Integer32"""
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
        *(("mellanoxPowerCycleCmdExecuteReload", 1),
          ("mellanoxPowerCycleCmdExecuteReloadDiscard", 2),
          ("mellanoxPowerCycleCmdExecuteReloadForce", 3),
          ("mellanoxPowerCycleCmdExecuteReloadSlave", 4))
    )


_MellanoxPowerCycleCmdExecute_Type.__name__ = "Integer32"
_MellanoxPowerCycleCmdExecute_Object = MibScalar
mellanoxPowerCycleCmdExecute = _MellanoxPowerCycleCmdExecute_Object(
    (1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 2, 1),
    _MellanoxPowerCycleCmdExecute_Type()
)
mellanoxPowerCycleCmdExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxPowerCycleCmdExecute.setStatus("current")
_MellanoxPowerCycleCmdStatus_Type = Integer32
_MellanoxPowerCycleCmdStatus_Object = MibScalar
mellanoxPowerCycleCmdStatus = _MellanoxPowerCycleCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 2, 2),
    _MellanoxPowerCycleCmdStatus_Type()
)
mellanoxPowerCycleCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxPowerCycleCmdStatus.setStatus("current")
_MellanoxPowerCycleCmdStatusString_Type = OctetString
_MellanoxPowerCycleCmdStatusString_Object = MibScalar
mellanoxPowerCycleCmdStatusString = _MellanoxPowerCycleCmdStatusString_Object(
    (1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 2, 3),
    _MellanoxPowerCycleCmdStatusString_Type()
)
mellanoxPowerCycleCmdStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxPowerCycleCmdStatusString.setStatus("current")
_MellanoxPowerCycleNotifications_ObjectIdentity = ObjectIdentity
mellanoxPowerCycleNotifications = _MellanoxPowerCycleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 3)
)

# Managed Objects groups


# Notification objects

mellanoxPowerCyclePlannedReload = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mellanoxPowerCyclePlannedReload.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-POWER-CYCLE-MIB",
    **{"mellanoxPowerCycleMib": mellanoxPowerCycleMib,
       "mellanoxPowerCycleMibObjects": mellanoxPowerCycleMibObjects,
       "mellanoxPowerCycleCmd": mellanoxPowerCycleCmd,
       "mellanoxPowerCycleCmdExecute": mellanoxPowerCycleCmdExecute,
       "mellanoxPowerCycleCmdStatus": mellanoxPowerCycleCmdStatus,
       "mellanoxPowerCycleCmdStatusString": mellanoxPowerCycleCmdStatusString,
       "mellanoxPowerCycleNotifications": mellanoxPowerCycleNotifications,
       "mellanoxPowerCyclePlannedReload": mellanoxPowerCyclePlannedReload}
)
