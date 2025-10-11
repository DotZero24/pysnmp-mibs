# SNMP MIB module (QTECH-NFPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-NFPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:21 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechNFPPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43)
)
if mibBuilder.loadTexts:
    qtechNFPPMIB.setRevisions(
        ("2009-07-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechNFPPMIBObjects_ObjectIdentity = ObjectIdentity
qtechNFPPMIBObjects = _QtechNFPPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 1)
)


class _QtechNFPPMessageContent_Type(OctetString):
    """Custom type qtechNFPPMessageContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_QtechNFPPMessageContent_Type.__name__ = "OctetString"
_QtechNFPPMessageContent_Object = MibScalar
qtechNFPPMessageContent = _QtechNFPPMessageContent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 1, 0),
    _QtechNFPPMessageContent_Type()
)
qtechNFPPMessageContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNFPPMessageContent.setStatus("current")
_QtechNFPPMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
qtechNFPPMIBNotificationPrefix = _QtechNFPPMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 2)
)
_QtechNFPPMIBNotifications_ObjectIdentity = ObjectIdentity
qtechNFPPMIBNotifications = _QtechNFPPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 2, 0)
)
_QtechNFPPMIBConformance_ObjectIdentity = ObjectIdentity
qtechNFPPMIBConformance = _QtechNFPPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3)
)
_QtechNFPPMIBCompliances_ObjectIdentity = ObjectIdentity
qtechNFPPMIBCompliances = _QtechNFPPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 1)
)
_QtechNFPPMIBGroups_ObjectIdentity = ObjectIdentity
qtechNFPPMIBGroups = _QtechNFPPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 2)
)

# Managed Objects groups

qtechNFPPNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 2, 1)
)
qtechNFPPNotifObjectsGroup.setObjects(
    ("QTECH-NFPP-MIB", "qtechNFPPMessageContent")
)
if mibBuilder.loadTexts:
    qtechNFPPNotifObjectsGroup.setStatus("current")


# Notification objects

qtechNFPPMessageGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 2, 0, 1)
)
qtechNFPPMessageGenerated.setObjects(
    ("QTECH-NFPP-MIB", "qtechNFPPMessageContent")
)
if mibBuilder.loadTexts:
    qtechNFPPMessageGenerated.setStatus(
        "current"
    )


# Notifications groups

qtechNFPPNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 2, 2)
)
qtechNFPPNotificationsGroup.setObjects(
    ("QTECH-NFPP-MIB", "qtechNFPPMessageGenerated")
)
if mibBuilder.loadTexts:
    qtechNFPPNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechNFPPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 1, 1)
)
qtechNFPPMIBCompliance.setObjects(
      *(("QTECH-NFPP-MIB", "qtechNFPPNotifObjectsGroup"),
        ("QTECH-NFPP-MIB", "qtechNFPPNotificationsGroup"))
)
if mibBuilder.loadTexts:
    qtechNFPPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-NFPP-MIB",
    **{"qtechNFPPMIB": qtechNFPPMIB,
       "qtechNFPPMIBObjects": qtechNFPPMIBObjects,
       "qtechNFPPMessageContent": qtechNFPPMessageContent,
       "qtechNFPPMIBNotificationPrefix": qtechNFPPMIBNotificationPrefix,
       "qtechNFPPMIBNotifications": qtechNFPPMIBNotifications,
       "qtechNFPPMessageGenerated": qtechNFPPMessageGenerated,
       "qtechNFPPMIBConformance": qtechNFPPMIBConformance,
       "qtechNFPPMIBCompliances": qtechNFPPMIBCompliances,
       "qtechNFPPMIBCompliance": qtechNFPPMIBCompliance,
       "qtechNFPPMIBGroups": qtechNFPPMIBGroups,
       "qtechNFPPNotifObjectsGroup": qtechNFPPNotifObjectsGroup,
       "qtechNFPPNotificationsGroup": qtechNFPPNotificationsGroup}
)
