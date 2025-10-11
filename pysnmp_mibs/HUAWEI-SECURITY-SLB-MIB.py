# SNMP MIB module (HUAWEI-SECURITY-SLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-SLB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:30:42 2025
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

hwSlb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67)
)
if mibBuilder.loadTexts:
    hwSlb.setRevisions(
        ("2014-01-07 16:09",)
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
_HwSlbNotification_ObjectIdentity = ObjectIdentity
hwSlbNotification = _HwSlbNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 1)
)
_HwSlbTrapObjects_ObjectIdentity = ObjectIdentity
hwSlbTrapObjects = _HwSlbTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 1, 1)
)
_HwSlbServerIndex_Type = Gauge32
_HwSlbServerIndex_Object = MibScalar
hwSlbServerIndex = _HwSlbServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 1, 1, 1),
    _HwSlbServerIndex_Type()
)
hwSlbServerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSlbServerIndex.setStatus("current")
_HwSlbServerIp_Type = IpAddress
_HwSlbServerIp_Object = MibScalar
hwSlbServerIp = _HwSlbServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 1, 1, 2),
    _HwSlbServerIp_Type()
)
hwSlbServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSlbServerIp.setStatus("current")
_HwSlbTraps_ObjectIdentity = ObjectIdentity
hwSlbTraps = _HwSlbTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 2)
)
_HwSlbConformance_ObjectIdentity = ObjectIdentity
hwSlbConformance = _HwSlbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3)
)
_HwSlbCompliances_ObjectIdentity = ObjectIdentity
hwSlbCompliances = _HwSlbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 1)
)
_HwSlbMibGroups_ObjectIdentity = ObjectIdentity
hwSlbMibGroups = _HwSlbMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 2)
)

# Managed Objects groups

hwSlbObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 2, 1)
)
hwSlbObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIndex"),
        ("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIp"))
)
if mibBuilder.loadTexts:
    hwSlbObjectGroup.setStatus("current")


# Notification objects

hwSlbRserverStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 2, 1)
)
hwSlbRserverStateUp.setObjects(
      *(("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIndex"),
        ("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIp"))
)
if mibBuilder.loadTexts:
    hwSlbRserverStateUp.setStatus(
        "current"
    )

hwSlbRserverStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 2, 2)
)
hwSlbRserverStateDown.setObjects(
      *(("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIndex"),
        ("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIp"))
)
if mibBuilder.loadTexts:
    hwSlbRserverStateDown.setStatus(
        "current"
    )


# Notifications groups

hwSlbTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 2, 2)
)
hwSlbTrapGroup.setObjects(
      *(("HUAWEI-SECURITY-SLB-MIB", "hwSlbRserverStateUp"),
        ("HUAWEI-SECURITY-SLB-MIB", "hwSlbRserverStateDown"))
)
if mibBuilder.loadTexts:
    hwSlbTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSlbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 1, 1)
)
hwSlbCompliance.setObjects(
      *(("HUAWEI-SECURITY-SLB-MIB", "hwSlbObjectGroup"),
        ("HUAWEI-SECURITY-SLB-MIB", "hwSlbTrapGroup"))
)
if mibBuilder.loadTexts:
    hwSlbCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-SLB-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwSlb": hwSlb,
       "hwSlbNotification": hwSlbNotification,
       "hwSlbTrapObjects": hwSlbTrapObjects,
       "hwSlbServerIndex": hwSlbServerIndex,
       "hwSlbServerIp": hwSlbServerIp,
       "hwSlbTraps": hwSlbTraps,
       "hwSlbRserverStateUp": hwSlbRserverStateUp,
       "hwSlbRserverStateDown": hwSlbRserverStateDown,
       "hwSlbConformance": hwSlbConformance,
       "hwSlbCompliances": hwSlbCompliances,
       "hwSlbCompliance": hwSlbCompliance,
       "hwSlbMibGroups": hwSlbMibGroups,
       "hwSlbObjectGroup": hwSlbObjectGroup,
       "hwSlbTrapGroup": hwSlbTrapGroup}
)
