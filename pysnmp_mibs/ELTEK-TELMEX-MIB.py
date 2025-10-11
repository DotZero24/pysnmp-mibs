# SNMP MIB module (ELTEK-TELMEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltek/ELTEK-TELMEX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:17:00 2025
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

(eltek,) = mibBuilder.importSymbols(
    "ELTEK-COMMON-MIB",
    "eltek")

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

_Telmex_ObjectIdentity = ObjectIdentity
telmex = _Telmex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 13)
)
_EltekTraps_ObjectIdentity = ObjectIdentity
eltekTraps = _EltekTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1)
)

# Managed Objects groups


# Notification objects

mainsFailAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 1)
)
if mibBuilder.loadTexts:
    mainsFailAlarmOn.setStatus(
        "current"
    )

mainsFailAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 2)
)
if mibBuilder.loadTexts:
    mainsFailAlarmOff.setStatus(
        "current"
    )

batteryVoltageLowAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 3)
)
if mibBuilder.loadTexts:
    batteryVoltageLowAlarmOn.setStatus(
        "current"
    )

batteryVoltageLowAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 4)
)
if mibBuilder.loadTexts:
    batteryVoltageLowAlarmOff.setStatus(
        "current"
    )

batteryVoltageHighAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 5)
)
if mibBuilder.loadTexts:
    batteryVoltageHighAlarmOn.setStatus(
        "current"
    )

batteryVoltageHighAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 6)
)
if mibBuilder.loadTexts:
    batteryVoltageHighAlarmOff.setStatus(
        "current"
    )

rectifierErrorAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 7)
)
if mibBuilder.loadTexts:
    rectifierErrorAlarmOn.setStatus(
        "current"
    )

rectifierErrorAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 8)
)
if mibBuilder.loadTexts:
    rectifierErrorAlarmOff.setStatus(
        "current"
    )

userAlarm1On = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 9)
)
if mibBuilder.loadTexts:
    userAlarm1On.setStatus(
        "current"
    )

userAlarm1Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 10)
)
if mibBuilder.loadTexts:
    userAlarm1Off.setStatus(
        "current"
    )

userAlarm2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 11)
)
if mibBuilder.loadTexts:
    userAlarm2On.setStatus(
        "current"
    )

userAlarm2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 12)
)
if mibBuilder.loadTexts:
    userAlarm2Off.setStatus(
        "current"
    )

userAlarm3On = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 13)
)
if mibBuilder.loadTexts:
    userAlarm3On.setStatus(
        "current"
    )

userAlarm3Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 14)
)
if mibBuilder.loadTexts:
    userAlarm3Off.setStatus(
        "current"
    )

userAlarm4On = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 15)
)
if mibBuilder.loadTexts:
    userAlarm4On.setStatus(
        "current"
    )

userAlarm4Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 16)
)
if mibBuilder.loadTexts:
    userAlarm4Off.setStatus(
        "current"
    )

userAlarm5On = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 17)
)
if mibBuilder.loadTexts:
    userAlarm5On.setStatus(
        "current"
    )

userAlarm5Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 18)
)
if mibBuilder.loadTexts:
    userAlarm5Off.setStatus(
        "current"
    )

userAlarm6On = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 19)
)
if mibBuilder.loadTexts:
    userAlarm6On.setStatus(
        "current"
    )

userAlarm6Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 20)
)
if mibBuilder.loadTexts:
    userAlarm6Off.setStatus(
        "current"
    )

loadFuseAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 21)
)
if mibBuilder.loadTexts:
    loadFuseAlarmOn.setStatus(
        "current"
    )

loadFuseAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 22)
)
if mibBuilder.loadTexts:
    loadFuseAlarmOff.setStatus(
        "current"
    )

batteryFuseAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 23)
)
if mibBuilder.loadTexts:
    batteryFuseAlarmOn.setStatus(
        "current"
    )

batteryFuseAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 13, 1, 24)
)
if mibBuilder.loadTexts:
    batteryFuseAlarmOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEK-TELMEX-MIB",
    **{"telmex": telmex,
       "eltekTraps": eltekTraps,
       "mainsFailAlarmOn": mainsFailAlarmOn,
       "mainsFailAlarmOff": mainsFailAlarmOff,
       "batteryVoltageLowAlarmOn": batteryVoltageLowAlarmOn,
       "batteryVoltageLowAlarmOff": batteryVoltageLowAlarmOff,
       "batteryVoltageHighAlarmOn": batteryVoltageHighAlarmOn,
       "batteryVoltageHighAlarmOff": batteryVoltageHighAlarmOff,
       "rectifierErrorAlarmOn": rectifierErrorAlarmOn,
       "rectifierErrorAlarmOff": rectifierErrorAlarmOff,
       "userAlarm1On": userAlarm1On,
       "userAlarm1Off": userAlarm1Off,
       "userAlarm2On": userAlarm2On,
       "userAlarm2Off": userAlarm2Off,
       "userAlarm3On": userAlarm3On,
       "userAlarm3Off": userAlarm3Off,
       "userAlarm4On": userAlarm4On,
       "userAlarm4Off": userAlarm4Off,
       "userAlarm5On": userAlarm5On,
       "userAlarm5Off": userAlarm5Off,
       "userAlarm6On": userAlarm6On,
       "userAlarm6Off": userAlarm6Off,
       "loadFuseAlarmOn": loadFuseAlarmOn,
       "loadFuseAlarmOff": loadFuseAlarmOff,
       "batteryFuseAlarmOn": batteryFuseAlarmOn,
       "batteryFuseAlarmOff": batteryFuseAlarmOff}
)
