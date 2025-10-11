# SNMP MIB module (OS-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:10 2025
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

(IANAtunnelType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAtunnelType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

osTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23)
)
if mibBuilder.loadTexts:
    osTunnelMIB.setRevisions(
        ("2020-04-06 00:00",
         "2017-02-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsTunnelNotifications_ObjectIdentity = ObjectIdentity
osTunnelNotifications = _OsTunnelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 0)
)
_OsTunnelMIBObjects_ObjectIdentity = ObjectIdentity
osTunnelMIBObjects = _OsTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1)
)
_OsTunnel_ObjectIdentity = ObjectIdentity
osTunnel = _OsTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1)
)
_OsTunnelTable_Object = MibTable
osTunnelTable = _OsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    osTunnelTable.setStatus("current")
_OsTunnelEntry_Object = MibTableRow
osTunnelEntry = _OsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1)
)
osTunnelEntry.setIndexNames(
    (0, "OS-TUNNEL-MIB", "osTunnelName"),
)
if mibBuilder.loadTexts:
    osTunnelEntry.setStatus("current")


class _OsTunnelName_Type(DisplayString):
    """Custom type osTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OsTunnelName_Type.__name__ = "DisplayString"
_OsTunnelName_Object = MibTableColumn
osTunnelName = _OsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 1),
    _OsTunnelName_Type()
)
osTunnelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osTunnelName.setStatus("current")
_OsTunnelAddressType_Type = InetAddressType
_OsTunnelAddressType_Object = MibTableColumn
osTunnelAddressType = _OsTunnelAddressType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 2),
    _OsTunnelAddressType_Type()
)
osTunnelAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osTunnelAddressType.setStatus("current")
_OsTunnelLocalAddress_Type = InetAddress
_OsTunnelLocalAddress_Object = MibTableColumn
osTunnelLocalAddress = _OsTunnelLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 3),
    _OsTunnelLocalAddress_Type()
)
osTunnelLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osTunnelLocalAddress.setStatus("current")
_OsTunnelRemoteAddress_Type = InetAddress
_OsTunnelRemoteAddress_Object = MibTableColumn
osTunnelRemoteAddress = _OsTunnelRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 4),
    _OsTunnelRemoteAddress_Type()
)
osTunnelRemoteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osTunnelRemoteAddress.setStatus("current")
_OsTunnelEncapsMethod_Type = IANAtunnelType
_OsTunnelEncapsMethod_Object = MibTableColumn
osTunnelEncapsMethod = _OsTunnelEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 5),
    _OsTunnelEncapsMethod_Type()
)
osTunnelEncapsMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osTunnelEncapsMethod.setStatus("current")


class _OsTunnelLocation_Type(DisplayString):
    """Custom type osTunnelLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OsTunnelLocation_Type.__name__ = "DisplayString"
_OsTunnelLocation_Object = MibTableColumn
osTunnelLocation = _OsTunnelLocation_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 6),
    _OsTunnelLocation_Type()
)
osTunnelLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osTunnelLocation.setStatus("current")


class _OsTunnelDescription_Type(DisplayString):
    """Custom type osTunnelDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OsTunnelDescription_Type.__name__ = "DisplayString"
_OsTunnelDescription_Object = MibTableColumn
osTunnelDescription = _OsTunnelDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 7),
    _OsTunnelDescription_Type()
)
osTunnelDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osTunnelDescription.setStatus("current")
_OsTunnelStatus_Type = RowStatus
_OsTunnelStatus_Object = MibTableColumn
osTunnelStatus = _OsTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 8),
    _OsTunnelStatus_Type()
)
osTunnelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osTunnelStatus.setStatus("current")


class _OsTunnelAdminStatus_Type(Integer32):
    """Custom type osTunnelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OsTunnelAdminStatus_Type.__name__ = "Integer32"
_OsTunnelAdminStatus_Object = MibTableColumn
osTunnelAdminStatus = _OsTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 9),
    _OsTunnelAdminStatus_Type()
)
osTunnelAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osTunnelAdminStatus.setStatus("current")


class _OsTunnelOperStatus_Type(Integer32):
    """Custom type osTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OsTunnelOperStatus_Type.__name__ = "Integer32"
_OsTunnelOperStatus_Object = MibTableColumn
osTunnelOperStatus = _OsTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 1, 1, 10),
    _OsTunnelOperStatus_Type()
)
osTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osTunnelOperStatus.setStatus("current")
_OsWanTable_Object = MibTable
osWanTable = _OsWanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    osWanTable.setStatus("current")
_OsWanEntry_Object = MibTableRow
osWanEntry = _OsWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2, 1)
)
osWanEntry.setIndexNames(
    (0, "OS-TUNNEL-MIB", "osWanModule"),
)
if mibBuilder.loadTexts:
    osWanEntry.setStatus("current")


class _OsWanModule_Type(DisplayString):
    """Custom type osWanModule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OsWanModule_Type.__name__ = "DisplayString"
_OsWanModule_Object = MibTableColumn
osWanModule = _OsWanModule_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2, 1, 1),
    _OsWanModule_Type()
)
osWanModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osWanModule.setStatus("current")
_OsWanLocalIpv4Address_Type = InetAddress
_OsWanLocalIpv4Address_Object = MibTableColumn
osWanLocalIpv4Address = _OsWanLocalIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2, 1, 2),
    _OsWanLocalIpv4Address_Type()
)
osWanLocalIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWanLocalIpv4Address.setStatus("current")
_OsWanRemoteIpv4Address_Type = InetAddress
_OsWanRemoteIpv4Address_Object = MibTableColumn
osWanRemoteIpv4Address = _OsWanRemoteIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2, 1, 3),
    _OsWanRemoteIpv4Address_Type()
)
osWanRemoteIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWanRemoteIpv4Address.setStatus("current")


class _OsWanIpv4Receive_Type(Integer32):
    """Custom type osWanIpv4Receive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreceive", 0),
          ("receive", 1))
    )


_OsWanIpv4Receive_Type.__name__ = "Integer32"
_OsWanIpv4Receive_Object = MibTableColumn
osWanIpv4Receive = _OsWanIpv4Receive_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2, 1, 4),
    _OsWanIpv4Receive_Type()
)
osWanIpv4Receive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWanIpv4Receive.setStatus("current")
_OsWanLocalIpv6Address_Type = InetAddress
_OsWanLocalIpv6Address_Object = MibTableColumn
osWanLocalIpv6Address = _OsWanLocalIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2, 1, 5),
    _OsWanLocalIpv6Address_Type()
)
osWanLocalIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWanLocalIpv6Address.setStatus("current")
_OsWanRemoteIpv6Address_Type = InetAddress
_OsWanRemoteIpv6Address_Object = MibTableColumn
osWanRemoteIpv6Address = _OsWanRemoteIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2, 1, 6),
    _OsWanRemoteIpv6Address_Type()
)
osWanRemoteIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWanRemoteIpv6Address.setStatus("current")


class _OsWanIpv6Receive_Type(Integer32):
    """Custom type osWanIpv6Receive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreceive", 0),
          ("receive", 1))
    )


_OsWanIpv6Receive_Type.__name__ = "Integer32"
_OsWanIpv6Receive_Object = MibTableColumn
osWanIpv6Receive = _OsWanIpv6Receive_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 1, 1, 2, 1, 7),
    _OsWanIpv6Receive_Type()
)
osWanIpv6Receive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWanIpv6Receive.setStatus("current")
_OsTunnelConformance_ObjectIdentity = ObjectIdentity
osTunnelConformance = _OsTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 10)
)
_OsTunnelMIBCompliances_ObjectIdentity = ObjectIdentity
osTunnelMIBCompliances = _OsTunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 10, 1)
)
_OsTunnelMIBGroups_ObjectIdentity = ObjectIdentity
osTunnelMIBGroups = _OsTunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 10, 2)
)

# Managed Objects groups

osTunnelMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 10, 2, 1)
)
osTunnelMandatoryGroup.setObjects(
      *(("OS-TUNNEL-MIB", "osTunnelAddressType"),
        ("OS-TUNNEL-MIB", "osTunnelLocalAddress"),
        ("OS-TUNNEL-MIB", "osTunnelRemoteAddress"),
        ("OS-TUNNEL-MIB", "osTunnelEncapsMethod"),
        ("OS-TUNNEL-MIB", "osTunnelLocation"),
        ("OS-TUNNEL-MIB", "osTunnelDescription"),
        ("OS-TUNNEL-MIB", "osTunnelStatus"),
        ("OS-TUNNEL-MIB", "osTunnelAdminStatus"),
        ("OS-TUNNEL-MIB", "osTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    osTunnelMandatoryGroup.setStatus("current")

osWanMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 10, 2, 2)
)
osWanMandatoryGroup.setObjects(
      *(("OS-TUNNEL-MIB", "osWanLocalIpv4Address"),
        ("OS-TUNNEL-MIB", "osWanRemoteIpv4Address"),
        ("OS-TUNNEL-MIB", "osWanIpv4Receive"),
        ("OS-TUNNEL-MIB", "osWanLocalIpv6Address"),
        ("OS-TUNNEL-MIB", "osWanRemoteIpv6Address"),
        ("OS-TUNNEL-MIB", "osWanIpv6Receive"))
)
if mibBuilder.loadTexts:
    osWanMandatoryGroup.setStatus("current")


# Notification objects

osTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 0, 1)
)
osTunnelUp.setObjects(
    ("OS-TUNNEL-MIB", "osTunnelDescription")
)
if mibBuilder.loadTexts:
    osTunnelUp.setStatus(
        "current"
    )

osTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 0, 2)
)
osTunnelDown.setObjects(
    ("OS-TUNNEL-MIB", "osTunnelDescription")
)
if mibBuilder.loadTexts:
    osTunnelDown.setStatus(
        "current"
    )


# Notifications groups

osTunnelNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 10, 2, 3)
)
osTunnelNotificationsGroup.setObjects(
      *(("OS-TUNNEL-MIB", "osTunnelUp"),
        ("OS-TUNNEL-MIB", "osTunnelDown"))
)
if mibBuilder.loadTexts:
    osTunnelNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

osTunnelMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 23, 10, 1, 1)
)
osTunnelMIBCompliance.setObjects(
      *(("OS-TUNNEL-MIB", "osTunnelMandatoryGroup"),
        ("OS-TUNNEL-MIB", "osWanMandatoryGroup"),
        ("OS-TUNNEL-MIB", "osTunnelNotificationsGroup"))
)
if mibBuilder.loadTexts:
    osTunnelMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-TUNNEL-MIB",
    **{"osTunnelMIB": osTunnelMIB,
       "osTunnelNotifications": osTunnelNotifications,
       "osTunnelUp": osTunnelUp,
       "osTunnelDown": osTunnelDown,
       "osTunnelMIBObjects": osTunnelMIBObjects,
       "osTunnel": osTunnel,
       "osTunnelTable": osTunnelTable,
       "osTunnelEntry": osTunnelEntry,
       "osTunnelName": osTunnelName,
       "osTunnelAddressType": osTunnelAddressType,
       "osTunnelLocalAddress": osTunnelLocalAddress,
       "osTunnelRemoteAddress": osTunnelRemoteAddress,
       "osTunnelEncapsMethod": osTunnelEncapsMethod,
       "osTunnelLocation": osTunnelLocation,
       "osTunnelDescription": osTunnelDescription,
       "osTunnelStatus": osTunnelStatus,
       "osTunnelAdminStatus": osTunnelAdminStatus,
       "osTunnelOperStatus": osTunnelOperStatus,
       "osWanTable": osWanTable,
       "osWanEntry": osWanEntry,
       "osWanModule": osWanModule,
       "osWanLocalIpv4Address": osWanLocalIpv4Address,
       "osWanRemoteIpv4Address": osWanRemoteIpv4Address,
       "osWanIpv4Receive": osWanIpv4Receive,
       "osWanLocalIpv6Address": osWanLocalIpv6Address,
       "osWanRemoteIpv6Address": osWanRemoteIpv6Address,
       "osWanIpv6Receive": osWanIpv6Receive,
       "osTunnelConformance": osTunnelConformance,
       "osTunnelMIBCompliances": osTunnelMIBCompliances,
       "osTunnelMIBCompliance": osTunnelMIBCompliance,
       "osTunnelMIBGroups": osTunnelMIBGroups,
       "osTunnelMandatoryGroup": osTunnelMandatoryGroup,
       "osWanMandatoryGroup": osWanMandatoryGroup,
       "osTunnelNotificationsGroup": osTunnelNotificationsGroup}
)
