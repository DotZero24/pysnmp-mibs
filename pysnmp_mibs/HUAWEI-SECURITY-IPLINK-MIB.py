#
# PySNMP MIB module HUAWEI-SECURITY-IPLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/huawei/HUAWEI-SECURITY-IPLINK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:01:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HUAWEI-SECURITY-IPLINK-MIB", hwIpLinkCompliance=hwIpLinkCompliance, hwIpLinkName=hwIpLinkName, hwIplink=hwIplink, hwIpLinkCompliances=hwIpLinkCompliances, hwIpLinkTrapObjects=hwIpLinkTrapObjects, hwIpLinkConformance=hwIpLinkConformance, hwIpLinkObjectGroup=hwIpLinkObjectGroup, PYSNMP_MODULE_ID=hwIplink, hwSecurity=hwSecurity, hwIpLinkStatus=hwIpLinkStatus, hwIpLinkMibGroups=hwIpLinkMibGroups, huawei=huawei, huaweiUtility=huaweiUtility, hwIpLinkDown=hwIpLinkDown, hwIpLinkNotification=hwIpLinkNotification, hwIpLinkTrapGroup=hwIpLinkTrapGroup, hwIpLinkTraps=hwIpLinkTraps, hwIpLinkUp=hwIpLinkUp)
