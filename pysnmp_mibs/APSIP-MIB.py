# SNMP MIB module (APSIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/acme/APSIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:39 2025
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApHardwareModuleFamily,
 ApPhyPortType,
 ApPresence,
 ApRedundancyState,
 ApServerStatus) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApHardwareModuleFamily",
    "ApPhyPortType",
    "ApPresence",
    "ApRedundancyState",
    "ApServerStatus")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

apSipModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15)
)
if mibBuilder.loadTexts:
    apSipModule.setRevisions(
        ("2012-07-13 00:00",
         "2012-03-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSipMIBObjects_ObjectIdentity = ObjectIdentity
apSipMIBObjects = _ApSipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1)
)
_ApSipMIBGeneralObjects_ObjectIdentity = ObjectIdentity
apSipMIBGeneralObjects = _ApSipMIBGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1)
)
_ApSipSecInterfaceObjects_ObjectIdentity = ObjectIdentity
apSipSecInterfaceObjects = _ApSipSecInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1, 1)
)
_ApSipSecInterfaceTotalRegistrations_Type = Unsigned32
_ApSipSecInterfaceTotalRegistrations_Object = MibScalar
apSipSecInterfaceTotalRegistrations = _ApSipSecInterfaceTotalRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1, 1, 1),
    _ApSipSecInterfaceTotalRegistrations_Type()
)
apSipSecInterfaceTotalRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSecInterfaceTotalRegistrations.setStatus("current")
_ApSipSecInterfaceRegThreshold_Type = Unsigned32
_ApSipSecInterfaceRegThreshold_Object = MibScalar
apSipSecInterfaceRegThreshold = _ApSipSecInterfaceRegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1, 1, 2),
    _ApSipSecInterfaceRegThreshold_Type()
)
apSipSecInterfaceRegThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSecInterfaceRegThreshold.setStatus("current")
_ApSipSecInterfaceClearThreshold_Type = Unsigned32
_ApSipSecInterfaceClearThreshold_Object = MibScalar
apSipSecInterfaceClearThreshold = _ApSipSecInterfaceClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1, 1, 3),
    _ApSipSecInterfaceClearThreshold_Type()
)
apSipSecInterfaceClearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSecInterfaceClearThreshold.setStatus("current")
_ApSipMIBTabularObjects_ObjectIdentity = ObjectIdentity
apSipMIBTabularObjects = _ApSipMIBTabularObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2)
)
_ApSipNotificationObjects_ObjectIdentity = ObjectIdentity
apSipNotificationObjects = _ApSipNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2)
)
_ApSipSecInterfaceNotifications_ObjectIdentity = ObjectIdentity
apSipSecInterfaceNotifications = _ApSipSecInterfaceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1)
)
_ApSipSecIntfNotifObjects_ObjectIdentity = ObjectIdentity
apSipSecIntfNotifObjects = _ApSipSecIntfNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 1)
)
_ApSipSecIntfNotifPrefix_ObjectIdentity = ObjectIdentity
apSipSecIntfNotifPrefix = _ApSipSecIntfNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 2)
)
_ApSipSecIntfNotifications_ObjectIdentity = ObjectIdentity
apSipSecIntfNotifications = _ApSipSecIntfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 2, 0)
)
_ApSipConformance_ObjectIdentity = ObjectIdentity
apSipConformance = _ApSipConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3)
)
_ApSipObjectGroups_ObjectIdentity = ObjectIdentity
apSipObjectGroups = _ApSipObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 1)
)
_ApSipNotificationGroups_ObjectIdentity = ObjectIdentity
apSipNotificationGroups = _ApSipNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 2)
)

# Managed Objects groups

apSipSecInterfaceRegObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 1, 1)
)
apSipSecInterfaceRegObjectsGroup.setObjects(
      *(("APSIP-MIB", "apSipSecInterfaceTotalRegistrations"),
        ("APSIP-MIB", "apSipSecInterfaceRegThreshold"),
        ("APSIP-MIB", "apSipSecInterfaceClearThreshold"))
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegObjectsGroup.setStatus("current")


# Notification objects

apSipSecInterfaceRegThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 2, 0, 1)
)
apSipSecInterfaceRegThresholdExceededTrap.setObjects(
      *(("APSIP-MIB", "apSipSecInterfaceTotalRegistrations"),
        ("APSIP-MIB", "apSipSecInterfaceRegThreshold"))
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegThresholdExceededTrap.setStatus(
        "current"
    )

apSipSecInterfaceRegThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 2, 0, 2)
)
apSipSecInterfaceRegThresholdClearTrap.setObjects(
      *(("APSIP-MIB", "apSipSecInterfaceTotalRegistrations"),
        ("APSIP-MIB", "apSipSecInterfaceClearThreshold"))
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegThresholdClearTrap.setStatus(
        "current"
    )


# Notifications groups

apSipSecInterfaceRegNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 2, 1)
)
apSipSecInterfaceRegNotificationsGroup.setObjects(
      *(("APSIP-MIB", "apSipSecInterfaceRegThresholdExceededTrap"),
        ("APSIP-MIB", "apSipSecInterfaceRegThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APSIP-MIB",
    **{"apSipModule": apSipModule,
       "apSipMIBObjects": apSipMIBObjects,
       "apSipMIBGeneralObjects": apSipMIBGeneralObjects,
       "apSipSecInterfaceObjects": apSipSecInterfaceObjects,
       "apSipSecInterfaceTotalRegistrations": apSipSecInterfaceTotalRegistrations,
       "apSipSecInterfaceRegThreshold": apSipSecInterfaceRegThreshold,
       "apSipSecInterfaceClearThreshold": apSipSecInterfaceClearThreshold,
       "apSipMIBTabularObjects": apSipMIBTabularObjects,
       "apSipNotificationObjects": apSipNotificationObjects,
       "apSipSecInterfaceNotifications": apSipSecInterfaceNotifications,
       "apSipSecIntfNotifObjects": apSipSecIntfNotifObjects,
       "apSipSecIntfNotifPrefix": apSipSecIntfNotifPrefix,
       "apSipSecIntfNotifications": apSipSecIntfNotifications,
       "apSipSecInterfaceRegThresholdExceededTrap": apSipSecInterfaceRegThresholdExceededTrap,
       "apSipSecInterfaceRegThresholdClearTrap": apSipSecInterfaceRegThresholdClearTrap,
       "apSipConformance": apSipConformance,
       "apSipObjectGroups": apSipObjectGroups,
       "apSipSecInterfaceRegObjectsGroup": apSipSecInterfaceRegObjectsGroup,
       "apSipNotificationGroups": apSipNotificationGroups,
       "apSipSecInterfaceRegNotificationsGroup": apSipSecInterfaceRegNotificationsGroup}
)
