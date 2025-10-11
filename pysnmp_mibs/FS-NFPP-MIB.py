# SNMP MIB module (FS-NFPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-NFPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:35 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsNFPPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43)
)
if mibBuilder.loadTexts:
    fsNFPPMIB.setRevisions(
        ("2009-07-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsNFPPMIBObjects_ObjectIdentity = ObjectIdentity
fsNFPPMIBObjects = _FsNFPPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 1)
)


class _FsNFPPMessageContent_Type(OctetString):
    """Custom type fsNFPPMessageContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FsNFPPMessageContent_Type.__name__ = "OctetString"
_FsNFPPMessageContent_Object = MibScalar
fsNFPPMessageContent = _FsNFPPMessageContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 1, 0),
    _FsNFPPMessageContent_Type()
)
fsNFPPMessageContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsNFPPMessageContent.setStatus("current")
_FsNFPPMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
fsNFPPMIBNotificationPrefix = _FsNFPPMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 2)
)
_FsNFPPMIBNotifications_ObjectIdentity = ObjectIdentity
fsNFPPMIBNotifications = _FsNFPPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 2, 0)
)
_FsNFPPMIBConformance_ObjectIdentity = ObjectIdentity
fsNFPPMIBConformance = _FsNFPPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3)
)
_FsNFPPMIBCompliances_ObjectIdentity = ObjectIdentity
fsNFPPMIBCompliances = _FsNFPPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 1)
)
_FsNFPPMIBGroups_ObjectIdentity = ObjectIdentity
fsNFPPMIBGroups = _FsNFPPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 2)
)

# Managed Objects groups

fsNFPPNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 2, 1)
)
fsNFPPNotifObjectsGroup.setObjects(
    ("FS-NFPP-MIB", "fsNFPPMessageContent")
)
if mibBuilder.loadTexts:
    fsNFPPNotifObjectsGroup.setStatus("current")


# Notification objects

fsNFPPMessageGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 2, 0, 1)
)
fsNFPPMessageGenerated.setObjects(
    ("FS-NFPP-MIB", "fsNFPPMessageContent")
)
if mibBuilder.loadTexts:
    fsNFPPMessageGenerated.setStatus(
        "current"
    )


# Notifications groups

fsNFPPNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 2, 2)
)
fsNFPPNotificationsGroup.setObjects(
    ("FS-NFPP-MIB", "fsNFPPMessageGenerated")
)
if mibBuilder.loadTexts:
    fsNFPPNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsNFPPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 1, 1)
)
fsNFPPMIBCompliance.setObjects(
      *(("FS-NFPP-MIB", "fsNFPPNotifObjectsGroup"),
        ("FS-NFPP-MIB", "fsNFPPNotificationsGroup"))
)
if mibBuilder.loadTexts:
    fsNFPPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-NFPP-MIB",
    **{"fsNFPPMIB": fsNFPPMIB,
       "fsNFPPMIBObjects": fsNFPPMIBObjects,
       "fsNFPPMessageContent": fsNFPPMessageContent,
       "fsNFPPMIBNotificationPrefix": fsNFPPMIBNotificationPrefix,
       "fsNFPPMIBNotifications": fsNFPPMIBNotifications,
       "fsNFPPMessageGenerated": fsNFPPMessageGenerated,
       "fsNFPPMIBConformance": fsNFPPMIBConformance,
       "fsNFPPMIBCompliances": fsNFPPMIBCompliances,
       "fsNFPPMIBCompliance": fsNFPPMIBCompliance,
       "fsNFPPMIBGroups": fsNFPPMIBGroups,
       "fsNFPPNotifObjectsGroup": fsNFPPNotifObjectsGroup,
       "fsNFPPNotificationsGroup": fsNFPPNotificationsGroup}
)
