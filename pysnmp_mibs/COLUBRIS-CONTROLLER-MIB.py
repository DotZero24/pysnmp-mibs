# SNMP MIB module (COLUBRIS-CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/colubris/COLUBRIS-CONTROLLER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:29 2025
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisNotificationEnable,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

colubrisControllerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisControllerMIBObjects_ObjectIdentity = ObjectIdentity
colubrisControllerMIBObjects = _ColubrisControllerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1)
)
_CoControllerConfigGroup_ObjectIdentity = ObjectIdentity
coControllerConfigGroup = _CoControllerConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 1)
)


class _CoControllerStateNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type coControllerStateNotificationEnabled based on ColubrisNotificationEnable"""
    defaultValue = 2


_CoControllerStateNotificationEnabled_Type.__name__ = "ColubrisNotificationEnable"
_CoControllerStateNotificationEnabled_Object = MibScalar
coControllerStateNotificationEnabled = _CoControllerStateNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 1, 1),
    _CoControllerStateNotificationEnabled_Type()
)
coControllerStateNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coControllerStateNotificationEnabled.setStatus("current")
_CoControllerTeamIpAddress_Type = IpAddress
_CoControllerTeamIpAddress_Object = MibScalar
coControllerTeamIpAddress = _CoControllerTeamIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 1, 2),
    _CoControllerTeamIpAddress_Type()
)
coControllerTeamIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coControllerTeamIpAddress.setStatus("current")
_CoControllerTeamName_Type = DisplayString
_CoControllerTeamName_Object = MibScalar
coControllerTeamName = _CoControllerTeamName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 1, 3),
    _CoControllerTeamName_Type()
)
coControllerTeamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coControllerTeamName.setStatus("current")
_CoControllerDiscoveryGroup_ObjectIdentity = ObjectIdentity
coControllerDiscoveryGroup = _CoControllerDiscoveryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2)
)
_CoControllerNbDisController_Type = Unsigned32
_CoControllerNbDisController_Object = MibScalar
coControllerNbDisController = _CoControllerNbDisController_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2, 1),
    _CoControllerNbDisController_Type()
)
coControllerNbDisController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coControllerNbDisController.setStatus("current")
_CoControllerDiscoveryTable_Object = MibTable
coControllerDiscoveryTable = _CoControllerDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2, 2)
)
if mibBuilder.loadTexts:
    coControllerDiscoveryTable.setStatus("current")
_CoControllerDiscoveryEntry_Object = MibTableRow
coControllerDiscoveryEntry = _CoControllerDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2, 2, 1)
)
coControllerDiscoveryEntry.setIndexNames(
    (0, "COLUBRIS-CONTROLLER-MIB", "coControllerDisIndex"),
)
if mibBuilder.loadTexts:
    coControllerDiscoveryEntry.setStatus("current")


class _CoControllerDisIndex_Type(Integer32):
    """Custom type coControllerDisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoControllerDisIndex_Type.__name__ = "Integer32"
_CoControllerDisIndex_Object = MibTableColumn
coControllerDisIndex = _CoControllerDisIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2, 2, 1, 1),
    _CoControllerDisIndex_Type()
)
coControllerDisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coControllerDisIndex.setStatus("current")
_CoControllerDisSerialNumber_Type = DisplayString
_CoControllerDisSerialNumber_Object = MibTableColumn
coControllerDisSerialNumber = _CoControllerDisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2, 2, 1, 2),
    _CoControllerDisSerialNumber_Type()
)
coControllerDisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coControllerDisSerialNumber.setStatus("current")
_CoControllerDisMacAddress_Type = MacAddress
_CoControllerDisMacAddress_Object = MibTableColumn
coControllerDisMacAddress = _CoControllerDisMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2, 2, 1, 3),
    _CoControllerDisMacAddress_Type()
)
coControllerDisMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coControllerDisMacAddress.setStatus("current")
_CoControllerDisIpAddress_Type = IpAddress
_CoControllerDisIpAddress_Object = MibTableColumn
coControllerDisIpAddress = _CoControllerDisIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2, 2, 1, 4),
    _CoControllerDisIpAddress_Type()
)
coControllerDisIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coControllerDisIpAddress.setStatus("current")


class _CoControllerDisState_Type(Integer32):
    """Custom type coControllerDisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("authorized", 2),
          ("join", 3),
          ("firmware", 4),
          ("security", 5),
          ("configuration", 6),
          ("running", 7))
    )


_CoControllerDisState_Type.__name__ = "Integer32"
_CoControllerDisState_Object = MibTableColumn
coControllerDisState = _CoControllerDisState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 1, 2, 2, 1, 5),
    _CoControllerDisState_Type()
)
coControllerDisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coControllerDisState.setStatus("current")
_ColubrisControllerMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisControllerMIBNotificationPrefix = _ColubrisControllerMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 2)
)
_ColubrisControllerMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisControllerMIBNotifications = _ColubrisControllerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 2, 0)
)
_ColubrisControllerMIBConformance_ObjectIdentity = ObjectIdentity
colubrisControllerMIBConformance = _ColubrisControllerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 3)
)
_ColubrisControllerMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisControllerMIBCompliances = _ColubrisControllerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 3, 1)
)
_ColubrisControllerMIBGroups_ObjectIdentity = ObjectIdentity
colubrisControllerMIBGroups = _ColubrisControllerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 3, 2)
)

# Managed Objects groups

colubrisControllerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 3, 2, 1)
)
colubrisControllerMIBGroup.setObjects(
      *(("COLUBRIS-CONTROLLER-MIB", "coControllerStateNotificationEnabled"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerTeamIpAddress"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerTeamName"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerNbDisController"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerDisSerialNumber"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerDisMacAddress"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerDisIpAddress"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerDisState"))
)
if mibBuilder.loadTexts:
    colubrisControllerMIBGroup.setStatus("current")


# Notification objects

coControllerStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 2, 0, 1)
)
coControllerStateNotification.setObjects(
      *(("COLUBRIS-CONTROLLER-MIB", "coControllerDisSerialNumber"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerDisMacAddress"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerDisIpAddress"),
        ("COLUBRIS-CONTROLLER-MIB", "coControllerDisState"))
)
if mibBuilder.loadTexts:
    coControllerStateNotification.setStatus(
        "current"
    )


# Notifications groups

colubrisControllerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 3, 2, 2)
)
colubrisControllerNotificationGroup.setObjects(
    ("COLUBRIS-CONTROLLER-MIB", "coControllerStateNotification")
)
if mibBuilder.loadTexts:
    colubrisControllerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisControllerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 27, 3, 1, 1)
)
colubrisControllerMIBCompliance.setObjects(
      *(("COLUBRIS-CONTROLLER-MIB", "colubrisControllerMIBGroup"),
        ("COLUBRIS-CONTROLLER-MIB", "colubrisControllerNotificationGroup"))
)
if mibBuilder.loadTexts:
    colubrisControllerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-CONTROLLER-MIB",
    **{"colubrisControllerMIB": colubrisControllerMIB,
       "colubrisControllerMIBObjects": colubrisControllerMIBObjects,
       "coControllerConfigGroup": coControllerConfigGroup,
       "coControllerStateNotificationEnabled": coControllerStateNotificationEnabled,
       "coControllerTeamIpAddress": coControllerTeamIpAddress,
       "coControllerTeamName": coControllerTeamName,
       "coControllerDiscoveryGroup": coControllerDiscoveryGroup,
       "coControllerNbDisController": coControllerNbDisController,
       "coControllerDiscoveryTable": coControllerDiscoveryTable,
       "coControllerDiscoveryEntry": coControllerDiscoveryEntry,
       "coControllerDisIndex": coControllerDisIndex,
       "coControllerDisSerialNumber": coControllerDisSerialNumber,
       "coControllerDisMacAddress": coControllerDisMacAddress,
       "coControllerDisIpAddress": coControllerDisIpAddress,
       "coControllerDisState": coControllerDisState,
       "colubrisControllerMIBNotificationPrefix": colubrisControllerMIBNotificationPrefix,
       "colubrisControllerMIBNotifications": colubrisControllerMIBNotifications,
       "coControllerStateNotification": coControllerStateNotification,
       "colubrisControllerMIBConformance": colubrisControllerMIBConformance,
       "colubrisControllerMIBCompliances": colubrisControllerMIBCompliances,
       "colubrisControllerMIBCompliance": colubrisControllerMIBCompliance,
       "colubrisControllerMIBGroups": colubrisControllerMIBGroups,
       "colubrisControllerMIBGroup": colubrisControllerMIBGroup,
       "colubrisControllerNotificationGroup": colubrisControllerNotificationGroup}
)
