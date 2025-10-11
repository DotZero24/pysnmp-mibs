# SNMP MIB module (HUAWEI-SECURITY-IPLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-IPLINK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:29:09 2025
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

hwIplink = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45)
)
if mibBuilder.loadTexts:
    hwIplink.setRevisions(
        ("2012-03-19 19:33",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwSecurity_ObjectIdentity = ObjectIdentity
hwSecurity = _HwSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122)
)
_HwIpLinkNotification_ObjectIdentity = ObjectIdentity
hwIpLinkNotification = _HwIpLinkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 1)
)
_HwIpLinkTrapObjects_ObjectIdentity = ObjectIdentity
hwIpLinkTrapObjects = _HwIpLinkTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 1, 1)
)
_HwIpLinkName_Type = OctetString
_HwIpLinkName_Object = MibScalar
hwIpLinkName = _HwIpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 1, 1, 1),
    _HwIpLinkName_Type()
)
hwIpLinkName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpLinkName.setStatus("current")
_HwIpLinkStatus_Type = OctetString
_HwIpLinkStatus_Object = MibScalar
hwIpLinkStatus = _HwIpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 1, 1, 2),
    _HwIpLinkStatus_Type()
)
hwIpLinkStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpLinkStatus.setStatus("current")
_HwIpLinkTraps_ObjectIdentity = ObjectIdentity
hwIpLinkTraps = _HwIpLinkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 2)
)
_HwIpLinkConformance_ObjectIdentity = ObjectIdentity
hwIpLinkConformance = _HwIpLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3)
)
_HwIpLinkCompliances_ObjectIdentity = ObjectIdentity
hwIpLinkCompliances = _HwIpLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 1)
)
_HwIpLinkMibGroups_ObjectIdentity = ObjectIdentity
hwIpLinkMibGroups = _HwIpLinkMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 2)
)

# Managed Objects groups

hwIpLinkObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 2, 1)
)
hwIpLinkObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkName"),
        ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkStatus"))
)
if mibBuilder.loadTexts:
    hwIpLinkObjectGroup.setStatus("current")


# Notification objects

hwIpLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 2, 1)
)
hwIpLinkUp.setObjects(
      *(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkName"),
        ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkStatus"))
)
if mibBuilder.loadTexts:
    hwIpLinkUp.setStatus(
        "current"
    )

hwIpLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 2, 2)
)
hwIpLinkDown.setObjects(
      *(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkName"),
        ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkStatus"))
)
if mibBuilder.loadTexts:
    hwIpLinkDown.setStatus(
        "current"
    )


# Notifications groups

hwIpLinkTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 2, 2)
)
hwIpLinkTrapGroup.setObjects(
      *(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkUp"),
        ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkDown"))
)
if mibBuilder.loadTexts:
    hwIpLinkTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIpLinkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 1, 1)
)
hwIpLinkCompliance.setObjects(
      *(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkObjectGroup"),
        ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkTrapGroup"))
)
if mibBuilder.loadTexts:
    hwIpLinkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-IPLINK-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwIplink": hwIplink,
       "hwIpLinkNotification": hwIpLinkNotification,
       "hwIpLinkTrapObjects": hwIpLinkTrapObjects,
       "hwIpLinkName": hwIpLinkName,
       "hwIpLinkStatus": hwIpLinkStatus,
       "hwIpLinkTraps": hwIpLinkTraps,
       "hwIpLinkUp": hwIpLinkUp,
       "hwIpLinkDown": hwIpLinkDown,
       "hwIpLinkConformance": hwIpLinkConformance,
       "hwIpLinkCompliances": hwIpLinkCompliances,
       "hwIpLinkCompliance": hwIpLinkCompliance,
       "hwIpLinkMibGroups": hwIpLinkMibGroups,
       "hwIpLinkObjectGroup": hwIpLinkObjectGroup,
       "hwIpLinkTrapGroup": hwIpLinkTrapGroup}
)
