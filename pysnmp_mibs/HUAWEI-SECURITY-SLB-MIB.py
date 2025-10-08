#
# PySNMP MIB module HUAWEI-SECURITY-SLB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/huawei/HUAWEI-SECURITY-SLB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:01:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwSlb = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67))
hwSlb.setRevisions(('2014-01-07 16:09',))
if mibBuilder.loadTexts: hwSlb.setLastUpdated('201401071609Z')
if mibBuilder.loadTexts: hwSlb.setOrganization('Huawei Technologies Co.,Ltd.')
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
huaweiUtility = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6))
hwSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122))
hwSlbNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 1))
hwSlbTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 1, 1))
hwSlbServerIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 1, 1, 1), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSlbServerIndex.setStatus('current')
hwSlbServerIp = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 1, 1, 2), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSlbServerIp.setStatus('current')
hwSlbTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 2))
hwSlbRserverStateUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 2, 1)).setObjects(("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIndex"), ("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIp"))
if mibBuilder.loadTexts: hwSlbRserverStateUp.setStatus('current')
hwSlbRserverStateDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 2, 2)).setObjects(("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIndex"), ("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIp"))
if mibBuilder.loadTexts: hwSlbRserverStateDown.setStatus('current')
hwSlbConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3))
hwSlbCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 1))
hwSlbCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 1, 1)).setObjects(("HUAWEI-SECURITY-SLB-MIB", "hwSlbObjectGroup"), ("HUAWEI-SECURITY-SLB-MIB", "hwSlbTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSlbCompliance = hwSlbCompliance.setStatus('current')
hwSlbMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 2))
hwSlbObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 2, 1)).setObjects(("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIndex"), ("HUAWEI-SECURITY-SLB-MIB", "hwSlbServerIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSlbObjectGroup = hwSlbObjectGroup.setStatus('current')
hwSlbTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 6, 122, 67, 3, 2, 2)).setObjects(("HUAWEI-SECURITY-SLB-MIB", "hwSlbRserverStateUp"), ("HUAWEI-SECURITY-SLB-MIB", "hwSlbRserverStateDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSlbTrapGroup = hwSlbTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SECURITY-SLB-MIB", hwSlbObjectGroup=hwSlbObjectGroup, hwSlbServerIp=hwSlbServerIp, hwSlbTrapGroup=hwSlbTrapGroup, hwSlbServerIndex=hwSlbServerIndex, hwSlbRserverStateDown=hwSlbRserverStateDown, PYSNMP_MODULE_ID=hwSlb, hwSlbTraps=hwSlbTraps, hwSlbMibGroups=hwSlbMibGroups, hwSecurity=hwSecurity, hwSlbNotification=hwSlbNotification, hwSlbRserverStateUp=hwSlbRserverStateUp, hwSlbConformance=hwSlbConformance, hwSlbCompliances=hwSlbCompliances, huawei=huawei, huaweiUtility=huaweiUtility, hwSlb=hwSlb, hwSlbCompliance=hwSlbCompliance, hwSlbTrapObjects=hwSlbTrapObjects)
