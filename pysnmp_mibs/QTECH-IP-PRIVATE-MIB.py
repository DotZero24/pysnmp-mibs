# SNMP MIB module (QTECH-IP-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-IP-PRIVATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:35 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechIPPrivateMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73)
)
if mibBuilder.loadTexts:
    qtechIPPrivateMgmt.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechIPPrivateAcNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
qtechIPPrivateAcNotificationsMIBObjects = _QtechIPPrivateAcNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1)
)
_QtechIPPrivateAcNtfObjects_ObjectIdentity = ObjectIdentity
qtechIPPrivateAcNtfObjects = _QtechIPPrivateAcNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 1)
)
_QtechIPPrivateAcNotifyIpv4AddressChangeType_Type = Integer32
_QtechIPPrivateAcNotifyIpv4AddressChangeType_Object = MibScalar
qtechIPPrivateAcNotifyIpv4AddressChangeType = _QtechIPPrivateAcNotifyIpv4AddressChangeType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 1, 1),
    _QtechIPPrivateAcNotifyIpv4AddressChangeType_Type()
)
qtechIPPrivateAcNotifyIpv4AddressChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPPrivateAcNotifyIpv4AddressChangeType.setStatus("current")
_QtechIPPrivateAcNotifyIpv4ChangeAddress_Type = IpAddress
_QtechIPPrivateAcNotifyIpv4ChangeAddress_Object = MibScalar
qtechIPPrivateAcNotifyIpv4ChangeAddress = _QtechIPPrivateAcNotifyIpv4ChangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 1, 2),
    _QtechIPPrivateAcNotifyIpv4ChangeAddress_Type()
)
qtechIPPrivateAcNotifyIpv4ChangeAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPPrivateAcNotifyIpv4ChangeAddress.setStatus("current")
_QtechIPPrivateAcNotifyIpv4ChangeAddressMask_Type = IpAddress
_QtechIPPrivateAcNotifyIpv4ChangeAddressMask_Object = MibScalar
qtechIPPrivateAcNotifyIpv4ChangeAddressMask = _QtechIPPrivateAcNotifyIpv4ChangeAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 1, 3),
    _QtechIPPrivateAcNotifyIpv4ChangeAddressMask_Type()
)
qtechIPPrivateAcNotifyIpv4ChangeAddressMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPPrivateAcNotifyIpv4ChangeAddressMask.setStatus("current")
_QtechIPPrivateAcNotifyIpv4ChangeIfIndex_Type = Integer32
_QtechIPPrivateAcNotifyIpv4ChangeIfIndex_Object = MibScalar
qtechIPPrivateAcNotifyIpv4ChangeIfIndex = _QtechIPPrivateAcNotifyIpv4ChangeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 1, 4),
    _QtechIPPrivateAcNotifyIpv4ChangeIfIndex_Type()
)
qtechIPPrivateAcNotifyIpv4ChangeIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPPrivateAcNotifyIpv4ChangeIfIndex.setStatus("current")
_QtechIPPrivateAcNotifications_ObjectIdentity = ObjectIdentity
qtechIPPrivateAcNotifications = _QtechIPPrivateAcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 2)
)
_QtechIPPrivateAcQueryApMIBObject_ObjectIdentity = ObjectIdentity
qtechIPPrivateAcQueryApMIBObject = _QtechIPPrivateAcQueryApMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 3)
)
_QtechIPPrivateAcQueryApInfo_ObjectIdentity = ObjectIdentity
qtechIPPrivateAcQueryApInfo = _QtechIPPrivateAcQueryApInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 3, 1)
)
_QtechIPPrivateAcQueryApMIBTable_Object = MibTable
qtechIPPrivateAcQueryApMIBTable = _QtechIPPrivateAcQueryApMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qtechIPPrivateAcQueryApMIBTable.setStatus("current")
_QtechIPPrivateApInfoEntry_Object = MibTableRow
qtechIPPrivateApInfoEntry = _QtechIPPrivateApInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1)
)
qtechIPPrivateApInfoEntry.setIndexNames(
    (0, "QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcApMacAddr"),
    (0, "QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcApIp"),
)
if mibBuilder.loadTexts:
    qtechIPPrivateApInfoEntry.setStatus("current")
_QtechIPPrivateAcApMacAddr_Type = MacAddress
_QtechIPPrivateAcApMacAddr_Object = MibTableColumn
qtechIPPrivateAcApMacAddr = _QtechIPPrivateAcApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 1),
    _QtechIPPrivateAcApMacAddr_Type()
)
qtechIPPrivateAcApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPPrivateAcApMacAddr.setStatus("current")
_QtechIPPrivateAcApIp_Type = IpAddress
_QtechIPPrivateAcApIp_Object = MibTableColumn
qtechIPPrivateAcApIp = _QtechIPPrivateAcApIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 2),
    _QtechIPPrivateAcApIp_Type()
)
qtechIPPrivateAcApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPPrivateAcApIp.setStatus("current")
_QtechIPPrivateAcApMask_Type = IpAddress
_QtechIPPrivateAcApMask_Object = MibTableColumn
qtechIPPrivateAcApMask = _QtechIPPrivateAcApMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 3),
    _QtechIPPrivateAcApMask_Type()
)
qtechIPPrivateAcApMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPPrivateAcApMask.setStatus("current")
_QtechIPPrivateAcApGateway_Type = IpAddress
_QtechIPPrivateAcApGateway_Object = MibTableColumn
qtechIPPrivateAcApGateway = _QtechIPPrivateAcApGateway_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 4),
    _QtechIPPrivateAcApGateway_Type()
)
qtechIPPrivateAcApGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPPrivateAcApGateway.setStatus("current")
_QtechIPPrivateMIBConformance_ObjectIdentity = ObjectIdentity
qtechIPPrivateMIBConformance = _QtechIPPrivateMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 2)
)
_QtechIPPrivateMIBCompliances_ObjectIdentity = ObjectIdentity
qtechIPPrivateMIBCompliances = _QtechIPPrivateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 2, 1)
)
_QtechIPPrivateMIBGroups_ObjectIdentity = ObjectIdentity
qtechIPPrivateMIBGroups = _QtechIPPrivateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 2, 2)
)

# Managed Objects groups

qtechIPPrivateMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 2, 2, 1)
)
qtechIPPrivateMIBGroup.setObjects(
      *(("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyIpv4AddressChangeType"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyIpv4ChangeAddress"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyIpv4ChangeAddressMask"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyIpv4ChangeIfIndex"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcApMacAddr"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcApIp"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcApMask"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcApGateway"))
)
if mibBuilder.loadTexts:
    qtechIPPrivateMIBGroup.setStatus("current")


# Notification objects

qtechIPPrivateAcNotifyChangeIpv4AddressAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 1, 2, 1)
)
qtechIPPrivateAcNotifyChangeIpv4AddressAlarm.setObjects(
      *(("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyIpv4AddressChangeType"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyIpv4ChangeAddress"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyIpv4ChangeAddressMask"),
        ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyIpv4ChangeIfIndex"))
)
if mibBuilder.loadTexts:
    qtechIPPrivateAcNotifyChangeIpv4AddressAlarm.setStatus(
        "current"
    )


# Notifications groups

qtechIPPrivateTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 2, 2, 2)
)
qtechIPPrivateTrapGroup.setObjects(
    ("QTECH-IP-PRIVATE-MIB", "qtechIPPrivateAcNotifyChangeIpv4AddressAlarm")
)
if mibBuilder.loadTexts:
    qtechIPPrivateTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechIPPrivateMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 73, 2, 1, 1)
)
qtechIPPrivateMIBCompliance.setObjects(
      *(("QTECH-IP-PRIVATE-MIB", "qtechAcIPPrivateMIBGroup"),
        ("QTECH-IP-PRIVATE-MIB", "qtechAcIPPrivateTrapGroup"))
)
if mibBuilder.loadTexts:
    qtechIPPrivateMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-IP-PRIVATE-MIB",
    **{"qtechIPPrivateMgmt": qtechIPPrivateMgmt,
       "qtechIPPrivateAcNotificationsMIBObjects": qtechIPPrivateAcNotificationsMIBObjects,
       "qtechIPPrivateAcNtfObjects": qtechIPPrivateAcNtfObjects,
       "qtechIPPrivateAcNotifyIpv4AddressChangeType": qtechIPPrivateAcNotifyIpv4AddressChangeType,
       "qtechIPPrivateAcNotifyIpv4ChangeAddress": qtechIPPrivateAcNotifyIpv4ChangeAddress,
       "qtechIPPrivateAcNotifyIpv4ChangeAddressMask": qtechIPPrivateAcNotifyIpv4ChangeAddressMask,
       "qtechIPPrivateAcNotifyIpv4ChangeIfIndex": qtechIPPrivateAcNotifyIpv4ChangeIfIndex,
       "qtechIPPrivateAcNotifications": qtechIPPrivateAcNotifications,
       "qtechIPPrivateAcNotifyChangeIpv4AddressAlarm": qtechIPPrivateAcNotifyChangeIpv4AddressAlarm,
       "qtechIPPrivateAcQueryApMIBObject": qtechIPPrivateAcQueryApMIBObject,
       "qtechIPPrivateAcQueryApInfo": qtechIPPrivateAcQueryApInfo,
       "qtechIPPrivateAcQueryApMIBTable": qtechIPPrivateAcQueryApMIBTable,
       "qtechIPPrivateApInfoEntry": qtechIPPrivateApInfoEntry,
       "qtechIPPrivateAcApMacAddr": qtechIPPrivateAcApMacAddr,
       "qtechIPPrivateAcApIp": qtechIPPrivateAcApIp,
       "qtechIPPrivateAcApMask": qtechIPPrivateAcApMask,
       "qtechIPPrivateAcApGateway": qtechIPPrivateAcApGateway,
       "qtechIPPrivateMIBConformance": qtechIPPrivateMIBConformance,
       "qtechIPPrivateMIBCompliances": qtechIPPrivateMIBCompliances,
       "qtechIPPrivateMIBCompliance": qtechIPPrivateMIBCompliance,
       "qtechIPPrivateMIBGroups": qtechIPPrivateMIBGroups,
       "qtechIPPrivateMIBGroup": qtechIPPrivateMIBGroup,
       "qtechIPPrivateTrapGroup": qtechIPPrivateTrapGroup}
)
