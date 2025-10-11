# SNMP MIB module (FS-IP-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IP-PRIVATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:17 2025
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

fsIPPrivateMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73)
)
if mibBuilder.loadTexts:
    fsIPPrivateMgmt.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIPPrivateAcNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
fsIPPrivateAcNotificationsMIBObjects = _FsIPPrivateAcNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1)
)
_FsIPPrivateAcNtfObjects_ObjectIdentity = ObjectIdentity
fsIPPrivateAcNtfObjects = _FsIPPrivateAcNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 1)
)
_FsIPPrivateAcNotifyIpv4AddressChangeType_Type = Integer32
_FsIPPrivateAcNotifyIpv4AddressChangeType_Object = MibScalar
fsIPPrivateAcNotifyIpv4AddressChangeType = _FsIPPrivateAcNotifyIpv4AddressChangeType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 1, 1),
    _FsIPPrivateAcNotifyIpv4AddressChangeType_Type()
)
fsIPPrivateAcNotifyIpv4AddressChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPPrivateAcNotifyIpv4AddressChangeType.setStatus("current")
_FsIPPrivateAcNotifyIpv4ChangeAddress_Type = IpAddress
_FsIPPrivateAcNotifyIpv4ChangeAddress_Object = MibScalar
fsIPPrivateAcNotifyIpv4ChangeAddress = _FsIPPrivateAcNotifyIpv4ChangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 1, 2),
    _FsIPPrivateAcNotifyIpv4ChangeAddress_Type()
)
fsIPPrivateAcNotifyIpv4ChangeAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPPrivateAcNotifyIpv4ChangeAddress.setStatus("current")
_FsIPPrivateAcNotifyIpv4ChangeAddressMask_Type = IpAddress
_FsIPPrivateAcNotifyIpv4ChangeAddressMask_Object = MibScalar
fsIPPrivateAcNotifyIpv4ChangeAddressMask = _FsIPPrivateAcNotifyIpv4ChangeAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 1, 3),
    _FsIPPrivateAcNotifyIpv4ChangeAddressMask_Type()
)
fsIPPrivateAcNotifyIpv4ChangeAddressMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPPrivateAcNotifyIpv4ChangeAddressMask.setStatus("current")
_FsIPPrivateAcNotifyIpv4ChangeIfIndex_Type = Integer32
_FsIPPrivateAcNotifyIpv4ChangeIfIndex_Object = MibScalar
fsIPPrivateAcNotifyIpv4ChangeIfIndex = _FsIPPrivateAcNotifyIpv4ChangeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 1, 4),
    _FsIPPrivateAcNotifyIpv4ChangeIfIndex_Type()
)
fsIPPrivateAcNotifyIpv4ChangeIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPPrivateAcNotifyIpv4ChangeIfIndex.setStatus("current")
_FsIPPrivateAcNotifications_ObjectIdentity = ObjectIdentity
fsIPPrivateAcNotifications = _FsIPPrivateAcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 2)
)
_FsIPPrivateAcQueryApMIBObject_ObjectIdentity = ObjectIdentity
fsIPPrivateAcQueryApMIBObject = _FsIPPrivateAcQueryApMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 3)
)
_FsIPPrivateAcQueryApInfo_ObjectIdentity = ObjectIdentity
fsIPPrivateAcQueryApInfo = _FsIPPrivateAcQueryApInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 3, 1)
)
_FsIPPrivateAcQueryApMIBTable_Object = MibTable
fsIPPrivateAcQueryApMIBTable = _FsIPPrivateAcQueryApMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fsIPPrivateAcQueryApMIBTable.setStatus("current")
_FsIPPrivateApInfoEntry_Object = MibTableRow
fsIPPrivateApInfoEntry = _FsIPPrivateApInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1)
)
fsIPPrivateApInfoEntry.setIndexNames(
    (0, "FS-IP-PRIVATE-MIB", "fsIPPrivateAcApMacAddr"),
    (0, "FS-IP-PRIVATE-MIB", "fsIPPrivateAcApIp"),
)
if mibBuilder.loadTexts:
    fsIPPrivateApInfoEntry.setStatus("current")
_FsIPPrivateAcApMacAddr_Type = MacAddress
_FsIPPrivateAcApMacAddr_Object = MibTableColumn
fsIPPrivateAcApMacAddr = _FsIPPrivateAcApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 1),
    _FsIPPrivateAcApMacAddr_Type()
)
fsIPPrivateAcApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPPrivateAcApMacAddr.setStatus("current")
_FsIPPrivateAcApIp_Type = IpAddress
_FsIPPrivateAcApIp_Object = MibTableColumn
fsIPPrivateAcApIp = _FsIPPrivateAcApIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 2),
    _FsIPPrivateAcApIp_Type()
)
fsIPPrivateAcApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPPrivateAcApIp.setStatus("current")
_FsIPPrivateAcApMask_Type = IpAddress
_FsIPPrivateAcApMask_Object = MibTableColumn
fsIPPrivateAcApMask = _FsIPPrivateAcApMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 3),
    _FsIPPrivateAcApMask_Type()
)
fsIPPrivateAcApMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPPrivateAcApMask.setStatus("current")
_FsIPPrivateAcApGateway_Type = IpAddress
_FsIPPrivateAcApGateway_Object = MibTableColumn
fsIPPrivateAcApGateway = _FsIPPrivateAcApGateway_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 4),
    _FsIPPrivateAcApGateway_Type()
)
fsIPPrivateAcApGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPPrivateAcApGateway.setStatus("current")
_FsIPPrivateMIBConformance_ObjectIdentity = ObjectIdentity
fsIPPrivateMIBConformance = _FsIPPrivateMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 2)
)
_FsIPPrivateMIBCompliances_ObjectIdentity = ObjectIdentity
fsIPPrivateMIBCompliances = _FsIPPrivateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 2, 1)
)
_FsIPPrivateMIBGroups_ObjectIdentity = ObjectIdentity
fsIPPrivateMIBGroups = _FsIPPrivateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 2, 2)
)

# Managed Objects groups

fsIPPrivateMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 2, 2, 1)
)
fsIPPrivateMIBGroup.setObjects(
      *(("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyIpv4AddressChangeType"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyIpv4ChangeAddress"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyIpv4ChangeAddressMask"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyIpv4ChangeIfIndex"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcApMacAddr"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcApIp"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcApMask"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcApGateway"))
)
if mibBuilder.loadTexts:
    fsIPPrivateMIBGroup.setStatus("current")


# Notification objects

fsIPPrivateAcNotifyChangeIpv4AddressAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 1, 2, 1)
)
fsIPPrivateAcNotifyChangeIpv4AddressAlarm.setObjects(
      *(("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyIpv4AddressChangeType"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyIpv4ChangeAddress"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyIpv4ChangeAddressMask"),
        ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyIpv4ChangeIfIndex"))
)
if mibBuilder.loadTexts:
    fsIPPrivateAcNotifyChangeIpv4AddressAlarm.setStatus(
        "current"
    )


# Notifications groups

fsIPPrivateTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 73, 2, 2, 2)
)
fsIPPrivateTrapGroup.setObjects(
    ("FS-IP-PRIVATE-MIB", "fsIPPrivateAcNotifyChangeIpv4AddressAlarm")
)
if mibBuilder.loadTexts:
    fsIPPrivateTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IP-PRIVATE-MIB",
    **{"fsIPPrivateMgmt": fsIPPrivateMgmt,
       "fsIPPrivateAcNotificationsMIBObjects": fsIPPrivateAcNotificationsMIBObjects,
       "fsIPPrivateAcNtfObjects": fsIPPrivateAcNtfObjects,
       "fsIPPrivateAcNotifyIpv4AddressChangeType": fsIPPrivateAcNotifyIpv4AddressChangeType,
       "fsIPPrivateAcNotifyIpv4ChangeAddress": fsIPPrivateAcNotifyIpv4ChangeAddress,
       "fsIPPrivateAcNotifyIpv4ChangeAddressMask": fsIPPrivateAcNotifyIpv4ChangeAddressMask,
       "fsIPPrivateAcNotifyIpv4ChangeIfIndex": fsIPPrivateAcNotifyIpv4ChangeIfIndex,
       "fsIPPrivateAcNotifications": fsIPPrivateAcNotifications,
       "fsIPPrivateAcNotifyChangeIpv4AddressAlarm": fsIPPrivateAcNotifyChangeIpv4AddressAlarm,
       "fsIPPrivateAcQueryApMIBObject": fsIPPrivateAcQueryApMIBObject,
       "fsIPPrivateAcQueryApInfo": fsIPPrivateAcQueryApInfo,
       "fsIPPrivateAcQueryApMIBTable": fsIPPrivateAcQueryApMIBTable,
       "fsIPPrivateApInfoEntry": fsIPPrivateApInfoEntry,
       "fsIPPrivateAcApMacAddr": fsIPPrivateAcApMacAddr,
       "fsIPPrivateAcApIp": fsIPPrivateAcApIp,
       "fsIPPrivateAcApMask": fsIPPrivateAcApMask,
       "fsIPPrivateAcApGateway": fsIPPrivateAcApGateway,
       "fsIPPrivateMIBConformance": fsIPPrivateMIBConformance,
       "fsIPPrivateMIBCompliances": fsIPPrivateMIBCompliances,
       "fsIPPrivateMIBGroups": fsIPPrivateMIBGroups,
       "fsIPPrivateMIBGroup": fsIPPrivateMIBGroup,
       "fsIPPrivateTrapGroup": fsIPPrivateTrapGroup}
)
