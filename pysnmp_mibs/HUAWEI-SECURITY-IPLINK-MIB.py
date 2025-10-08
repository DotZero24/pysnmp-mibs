#
# PySNMP MIB module HUAWEI-SECURITY-IPLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/huawei/HUAWEI-SECURITY-IPLINK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:06:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwIplink = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45))
hwIplink.setRevisions(('2012-03-19 19:33',))
if mibBuilder.loadTexts: hwIplink.setLastUpdated('201203191933Z')
if mibBuilder.loadTexts: hwIplink.setOrganization('Huawei Technologies Co.,Ltd.')
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
huaweiUtility = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6))
hwSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122))
hwIpLinkNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 1))
hwIpLinkTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 1, 1))
hwIpLinkName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 1, 1, 1), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwIpLinkName.setStatus('current')
hwIpLinkStatus = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 1, 1, 2), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwIpLinkStatus.setStatus('current')
hwIpLinkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 2))
hwIpLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 2, 1)).setObjects(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkName"), ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkStatus"))
if mibBuilder.loadTexts: hwIpLinkUp.setStatus('current')
hwIpLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 2, 2)).setObjects(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkName"), ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkStatus"))
if mibBuilder.loadTexts: hwIpLinkDown.setStatus('current')
hwIpLinkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3))
hwIpLinkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 1))
hwIpLinkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 1, 1)).setObjects(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkObjectGroup"), ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIpLinkCompliance = hwIpLinkCompliance.setStatus('current')
hwIpLinkMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 2))
hwIpLinkObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 2, 1)).setObjects(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkName"), ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIpLinkObjectGroup = hwIpLinkObjectGroup.setStatus('current')
hwIpLinkTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 6, 122, 45, 3, 2, 2)).setObjects(("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkUp"), ("HUAWEI-SECURITY-IPLINK-MIB", "hwIpLinkDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIpLinkTrapGroup = hwIpLinkTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SECURITY-IPLINK-MIB", hwSecurity=hwSecurity, hwIpLinkNotification=hwIpLinkNotification, hwIpLinkDown=hwIpLinkDown, hwIpLinkStatus=hwIpLinkStatus, hwIpLinkCompliances=hwIpLinkCompliances, hwIpLinkTrapObjects=hwIpLinkTrapObjects, hwIpLinkCompliance=hwIpLinkCompliance, huaweiUtility=huaweiUtility, hwIpLinkTraps=hwIpLinkTraps, hwIpLinkUp=hwIpLinkUp, PYSNMP_MODULE_ID=hwIplink, hwIpLinkConformance=hwIpLinkConformance, hwIpLinkMibGroups=hwIpLinkMibGroups, hwIpLinkObjectGroup=hwIpLinkObjectGroup, hwIpLinkName=hwIpLinkName, hwIpLinkTrapGroup=hwIpLinkTrapGroup, huawei=huawei, hwIplink=hwIplink)
