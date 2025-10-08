#
# PySNMP MIB module HUAWEI-SECURITY-SLB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/huawei/HUAWEI-SECURITY-SLB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HUAWEI-SECURITY-SLB-MIB", hwSecurity=hwSecurity, hwSlb=hwSlb, hwSlbServerIp=hwSlbServerIp, hwSlbRserverStateDown=hwSlbRserverStateDown, PYSNMP_MODULE_ID=hwSlb, huaweiUtility=huaweiUtility, hwSlbTrapObjects=hwSlbTrapObjects, hwSlbRserverStateUp=hwSlbRserverStateUp, hwSlbMibGroups=hwSlbMibGroups, hwSlbCompliances=hwSlbCompliances, hwSlbNotification=hwSlbNotification, hwSlbCompliance=hwSlbCompliance, hwSlbObjectGroup=hwSlbObjectGroup, hwSlbConformance=hwSlbConformance, hwSlbServerIndex=hwSlbServerIndex, huawei=huawei, hwSlbTrapGroup=hwSlbTrapGroup, hwSlbTraps=hwSlbTraps)
