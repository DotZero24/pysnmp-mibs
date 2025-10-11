# SNMP MIB module (HIRSCHMANN-WLAN-BATC2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HIRSCHMANN-WLAN-BATC2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:52:24 2025
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

(batC2,) = mibBuilder.importSymbols(
    "HIRSCHMANN-WLAN-LT-MIB",
    "batC2")

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
 Opaque,
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
    "Opaque",
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

batC2MIB = ModuleIdentity(
    (248, 32, 100, 1, 15, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Batc2Trap_ObjectIdentity = ObjectIdentity
batc2Trap = _Batc2Trap_ObjectIdentity(
    (248, 32, 100, 1, 15, 4)
)
_AlarmType_Type = DisplayString
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (248, 32, 100, 1, 15, 4, 2),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_AlarmValue_Type = DisplayString
_AlarmValue_Object = MibScalar
alarmValue = _AlarmValue_Object(
    (248, 32, 100, 1, 15, 4, 3),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmValue.setStatus("current")

# Managed Objects groups


# Notification objects

alarm = NotificationType(
    (248, 32, 100, 1, 15, 4, 1)
)
if mibBuilder.loadTexts:
    alarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-WLAN-BATC2-MIB",
    **{"batC2MIB": batC2MIB,
       "batc2Trap": batc2Trap,
       "alarm": alarm,
       "alarmType": alarmType,
       "alarmValue": alarmValue}
)
