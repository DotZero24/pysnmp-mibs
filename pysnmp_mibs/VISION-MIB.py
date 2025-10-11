# SNMP MIB module (VISION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/VISION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:30 2025
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

(rndApplications,) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rndApplications")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

_Managment_ObjectIdentity = ObjectIdentity
managment = _Managment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 10)
)
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1)
)
_AlertId_Type = Integer32
_AlertId_Object = MibScalar
alertId = _AlertId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 1),
    _AlertId_Type()
)
alertId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertId.setStatus("current")
_AlertMessage_Type = DisplayString
_AlertMessage_Object = MibScalar
alertMessage = _AlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 2),
    _AlertMessage_Type()
)
alertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMessage.setStatus("current")


class _AlertUser_Type(DisplayString):
    """Custom type alertUser based on DisplayString"""
    defaultValue = OctetString("APSolute_Vision")


_AlertUser_Type.__name__ = "DisplayString"
_AlertUser_Object = MibScalar
alertUser = _AlertUser_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 3),
    _AlertUser_Type()
)
alertUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertUser.setStatus("current")
_AlertSeverity_Type = DisplayString
_AlertSeverity_Object = MibScalar
alertSeverity = _AlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 4),
    _AlertSeverity_Type()
)
alertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSeverity.setStatus("current")
_AlertModule_Type = DisplayString
_AlertModule_Object = MibScalar
alertModule = _AlertModule_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 5),
    _AlertModule_Type()
)
alertModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertModule.setStatus("current")
_AlertCategory_Type = DisplayString
_AlertCategory_Object = MibScalar
alertCategory = _AlertCategory_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 6),
    _AlertCategory_Type()
)
alertCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertCategory.setStatus("current")
_AlertTimeString_Type = DisplayString
_AlertTimeString_Object = MibScalar
alertTimeString = _AlertTimeString_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 7),
    _AlertTimeString_Type()
)
alertTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertTimeString.setStatus("current")
_AlertTimeMillis_Type = Counter64
_AlertTimeMillis_Object = MibScalar
alertTimeMillis = _AlertTimeMillis_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 8),
    _AlertTimeMillis_Type()
)
alertTimeMillis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertTimeMillis.setStatus("current")


class _AlertSourceDeviceName_Type(DisplayString):
    """Custom type alertSourceDeviceName based on DisplayString"""
    defaultValue = OctetString("")


_AlertSourceDeviceName_Type.__name__ = "DisplayString"
_AlertSourceDeviceName_Object = MibScalar
alertSourceDeviceName = _AlertSourceDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 9),
    _AlertSourceDeviceName_Type()
)
alertSourceDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSourceDeviceName.setStatus("current")


class _AlertSourceDeviceIp_Type(DisplayString):
    """Custom type alertSourceDeviceIp based on DisplayString"""
    defaultValue = OctetString("")


_AlertSourceDeviceIp_Type.__name__ = "DisplayString"
_AlertSourceDeviceIp_Object = MibScalar
alertSourceDeviceIp = _AlertSourceDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 10),
    _AlertSourceDeviceIp_Type()
)
alertSourceDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSourceDeviceIp.setStatus("current")

# Managed Objects groups


# Notification objects

alertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 10, 1, 0, 200)
)
alertTrap.setObjects(
      *(("VISION-MIB", "alertId"),
        ("VISION-MIB", "alertMessage"),
        ("VISION-MIB", "alertUser"),
        ("VISION-MIB", "alertSeverity"),
        ("VISION-MIB", "alertModule"),
        ("VISION-MIB", "alertCategory"),
        ("VISION-MIB", "alertTimeString"),
        ("VISION-MIB", "alertTimeMillis"),
        ("VISION-MIB", "alertSourceDeviceName"),
        ("VISION-MIB", "alertSourceDeviceIp"))
)
if mibBuilder.loadTexts:
    alertTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VISION-MIB",
    **{"managment": managment,
       "alerts": alerts,
       "alertTrap": alertTrap,
       "alertId": alertId,
       "alertMessage": alertMessage,
       "alertUser": alertUser,
       "alertSeverity": alertSeverity,
       "alertModule": alertModule,
       "alertCategory": alertCategory,
       "alertTimeString": alertTimeString,
       "alertTimeMillis": alertTimeMillis,
       "alertSourceDeviceName": alertSourceDeviceName,
       "alertSourceDeviceIp": alertSourceDeviceIp}
)
