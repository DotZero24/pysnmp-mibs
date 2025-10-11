# SNMP MIB module (H3C-FC-NAME-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FC-NAME-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:19 2025
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

(H3cFcNameId,) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcNameId")

(h3cSan,
 h3cVsanIndex) = mibBuilder.importSymbols(
    "H3C-VSAN-MIB",
    "h3cSan",
    "h3cVsanIndex")

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

h3cFcNameServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10)
)
if mibBuilder.loadTexts:
    h3cFcNameServer.setRevisions(
        ("2014-03-03 10:18",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFcNameServerMibObjects_ObjectIdentity = ObjectIdentity
h3cFcNameServerMibObjects = _H3cFcNameServerMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1)
)
_H3cFcNsNotification_ObjectIdentity = ObjectIdentity
h3cFcNsNotification = _H3cFcNsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1)
)
_H3cFcNsNotificationPrefix_ObjectIdentity = ObjectIdentity
h3cFcNsNotificationPrefix = _H3cFcNsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 0)
)
_H3cFcNsNotificationSwitch_ObjectIdentity = ObjectIdentity
h3cFcNsNotificationSwitch = _H3cFcNsNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 1)
)
_H3cFcNsPortLoginNotifyEnable_Type = TruthValue
_H3cFcNsPortLoginNotifyEnable_Object = MibScalar
h3cFcNsPortLoginNotifyEnable = _H3cFcNsPortLoginNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 1, 1),
    _H3cFcNsPortLoginNotifyEnable_Type()
)
h3cFcNsPortLoginNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcNsPortLoginNotifyEnable.setStatus("current")
_H3cFcNsPortLogoutNotifyEnable_Type = TruthValue
_H3cFcNsPortLogoutNotifyEnable_Object = MibScalar
h3cFcNsPortLogoutNotifyEnable = _H3cFcNsPortLogoutNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 1, 2),
    _H3cFcNsPortLogoutNotifyEnable_Type()
)
h3cFcNsPortLogoutNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcNsPortLogoutNotifyEnable.setStatus("current")
_H3cFcNsObjsForNotification_ObjectIdentity = ObjectIdentity
h3cFcNsObjsForNotification = _H3cFcNsObjsForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 2)
)
_H3cFcNsLocalSwitchWWN_Type = H3cFcNameId
_H3cFcNsLocalSwitchWWN_Object = MibScalar
h3cFcNsLocalSwitchWWN = _H3cFcNsLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 2, 1),
    _H3cFcNsLocalSwitchWWN_Type()
)
h3cFcNsLocalSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFcNsLocalSwitchWWN.setStatus("current")
_H3cFcNsFloginPortWWN_Type = H3cFcNameId
_H3cFcNsFloginPortWWN_Object = MibScalar
h3cFcNsFloginPortWWN = _H3cFcNsFloginPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 2, 2),
    _H3cFcNsFloginPortWWN_Type()
)
h3cFcNsFloginPortWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFcNsFloginPortWWN.setStatus("current")

# Managed Objects groups


# Notification objects

h3cFcNsPortLoginNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 0, 1)
)
h3cFcNsPortLoginNotify.setObjects(
      *(("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-FC-NAME-SERVER-MIB", "h3cFcNsLocalSwitchWWN"),
        ("H3C-FC-NAME-SERVER-MIB", "h3cFcNsFloginPortWWN"))
)
if mibBuilder.loadTexts:
    h3cFcNsPortLoginNotify.setStatus(
        "current"
    )

h3cFcNsPortLogoutNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 10, 1, 1, 0, 2)
)
h3cFcNsPortLogoutNotify.setObjects(
      *(("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-FC-NAME-SERVER-MIB", "h3cFcNsLocalSwitchWWN"),
        ("H3C-FC-NAME-SERVER-MIB", "h3cFcNsFloginPortWWN"))
)
if mibBuilder.loadTexts:
    h3cFcNsPortLogoutNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FC-NAME-SERVER-MIB",
    **{"h3cFcNameServer": h3cFcNameServer,
       "h3cFcNameServerMibObjects": h3cFcNameServerMibObjects,
       "h3cFcNsNotification": h3cFcNsNotification,
       "h3cFcNsNotificationPrefix": h3cFcNsNotificationPrefix,
       "h3cFcNsPortLoginNotify": h3cFcNsPortLoginNotify,
       "h3cFcNsPortLogoutNotify": h3cFcNsPortLogoutNotify,
       "h3cFcNsNotificationSwitch": h3cFcNsNotificationSwitch,
       "h3cFcNsPortLoginNotifyEnable": h3cFcNsPortLoginNotifyEnable,
       "h3cFcNsPortLogoutNotifyEnable": h3cFcNsPortLogoutNotifyEnable,
       "h3cFcNsObjsForNotification": h3cFcNsObjsForNotification,
       "h3cFcNsLocalSwitchWWN": h3cFcNsLocalSwitchWWN,
       "h3cFcNsFloginPortWWN": h3cFcNsFloginPortWWN}
)
