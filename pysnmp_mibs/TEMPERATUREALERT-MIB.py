# SNMP MIB module (TEMPERATUREALERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tempalert/TEMPERATUREALERT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:32:15 2025
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

taMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27297)
)
if mibBuilder.loadTexts:
    taMIB.setRevisions(
        ("1918-10-23 12:00",
         "1906-10-31 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TaTraps_ObjectIdentity = ObjectIdentity
taTraps = _TaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27297, 0)
)
_TaService_ObjectIdentity = ObjectIdentity
taService = _TaService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27297, 1)
)
_TaDeviceIndex_Type = DisplayString
_TaDeviceIndex_Object = MibScalar
taDeviceIndex = _TaDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27297, 1, 1),
    _TaDeviceIndex_Type()
)
taDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taDeviceIndex.setStatus("current")
_TaTemperature_Type = DisplayString
_TaTemperature_Object = MibScalar
taTemperature = _TaTemperature_Object(
    (1, 3, 6, 1, 4, 1, 27297, 1, 2),
    _TaTemperature_Type()
)
taTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taTemperature.setStatus("current")
_TaLastCheck_Type = DisplayString
_TaLastCheck_Object = MibScalar
taLastCheck = _TaLastCheck_Object(
    (1, 3, 6, 1, 4, 1, 27297, 1, 3),
    _TaLastCheck_Type()
)
taLastCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taLastCheck.setStatus("current")
_TaWifi_ObjectIdentity = ObjectIdentity
taWifi = _TaWifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27297, 2)
)
_TaTemperatureTable_ObjectIdentity = ObjectIdentity
taTemperatureTable = _TaTemperatureTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27297, 2, 7)
)
_TaTemperatureEntry_ObjectIdentity = ObjectIdentity
taTemperatureEntry = _TaTemperatureEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27297, 2, 7, 1)
)
_TaTemperaturePort_Type = DisplayString
_TaTemperaturePort_Object = MibScalar
taTemperaturePort = _TaTemperaturePort_Object(
    (1, 3, 6, 1, 4, 1, 27297, 2, 7, 1, 7),
    _TaTemperaturePort_Type()
)
taTemperaturePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taTemperaturePort.setStatus("current")

# Managed Objects groups


# Notification objects

taNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 27297, 0, 1)
)
taNormal.setObjects(
      *(("TEMPERATUREALERT-MIB", "taDeviceIndex"),
        ("TEMPERATUREALERT-MIB", "taTemperature"),
        ("TEMPERATUREALERT-MIB", "taLastCheck"))
)
if mibBuilder.loadTexts:
    taNormal.setStatus(
        "current"
    )

taHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 27297, 0, 2)
)
taHighAlarm.setObjects(
      *(("TEMPERATUREALERT-MIB", "taDeviceIndex"),
        ("TEMPERATUREALERT-MIB", "taTemperature"),
        ("TEMPERATUREALERT-MIB", "taLastCheck"))
)
if mibBuilder.loadTexts:
    taHighAlarm.setStatus(
        "current"
    )

taLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 27297, 0, 3)
)
taLowAlarm.setObjects(
      *(("TEMPERATUREALERT-MIB", "taDeviceIndex"),
        ("TEMPERATUREALERT-MIB", "taTemperature"),
        ("TEMPERATUREALERT-MIB", "taLastCheck"))
)
if mibBuilder.loadTexts:
    taLowAlarm.setStatus(
        "current"
    )

taShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 27297, 0, 4)
)
if mibBuilder.loadTexts:
    taShutdown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TEMPERATUREALERT-MIB",
    **{"taMIB": taMIB,
       "taTraps": taTraps,
       "taNormal": taNormal,
       "taHighAlarm": taHighAlarm,
       "taLowAlarm": taLowAlarm,
       "taShutdown": taShutdown,
       "taService": taService,
       "taDeviceIndex": taDeviceIndex,
       "taTemperature": taTemperature,
       "taLastCheck": taLastCheck,
       "taWifi": taWifi,
       "taTemperatureTable": taTemperatureTable,
       "taTemperatureEntry": taTemperatureEntry,
       "taTemperaturePort": taTemperaturePort}
)
