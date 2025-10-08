#
# PySNMP MIB module QTECH-AUTH-GATEWAY-CONTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-AUTH-GATEWAY-CONTEXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
qtechWebAuthVCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67))
qtechWebAuthVCMIB.setRevisions(('2009-12-06 00:00',))
if mibBuilder.loadTexts: qtechWebAuthVCMIB.setLastUpdated('200912060000Z')
if mibBuilder.loadTexts: qtechWebAuthVCMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechWebAuthVCMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1))
qtechWebAuthUserVCTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1), )
if mibBuilder.loadTexts: qtechWebAuthUserVCTable.setStatus('current')
qtechWebAuthUserVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1), ).setIndexNames((0, "QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserContextNameVC"), (0, "QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserIpAddrVC"))
if mibBuilder.loadTexts: qtechWebAuthUserVCEntry.setStatus('current')
authUserContextNameVC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserContextNameVC.setStatus('current')
authUserIpAddrVC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserIpAddrVC.setStatus('current')
authUserOnlineFlagVC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserOnlineFlagVC.setStatus('current')
authUserTimeLimitVC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 4), Gauge32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: authUserTimeLimitVC.setStatus('current')
authUserTimeUsedVC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserTimeUsedVC.setStatus('current')
authUserStatusVC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: authUserStatusVC.setStatus('current')
qtechWebAuthVCMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3))
qtechWebAuthVCMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3, 1))
qtechWebAuthVCMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3, 2))
qtechWebAuthVCMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3, 1, 1)).setObjects(("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "qtechWebAuthVCMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechWebAuthVCMIBCompliance = qtechWebAuthVCMIBCompliance.setStatus('current')
qtechWebAuthVCMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3, 2, 1)).setObjects(("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserContextNameVC"), ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserIpAddrVC"), ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserOnlineFlagVC"), ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserTimeLimitVC"), ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserTimeUsedVC"), ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserStatusVC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechWebAuthVCMIBGroup = qtechWebAuthVCMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-AUTH-GATEWAY-CONTEXT-MIB", qtechWebAuthUserVCEntry=qtechWebAuthUserVCEntry, authUserTimeLimitVC=authUserTimeLimitVC, PYSNMP_MODULE_ID=qtechWebAuthVCMIB, authUserIpAddrVC=authUserIpAddrVC, qtechWebAuthVCMIBConformance=qtechWebAuthVCMIBConformance, qtechWebAuthVCMIBObjects=qtechWebAuthVCMIBObjects, qtechWebAuthVCMIBGroup=qtechWebAuthVCMIBGroup, authUserOnlineFlagVC=authUserOnlineFlagVC, authUserStatusVC=authUserStatusVC, qtechWebAuthVCMIB=qtechWebAuthVCMIB, qtechWebAuthVCMIBCompliance=qtechWebAuthVCMIBCompliance, qtechWebAuthUserVCTable=qtechWebAuthUserVCTable, qtechWebAuthVCMIBCompliances=qtechWebAuthVCMIBCompliances, authUserTimeUsedVC=authUserTimeUsedVC, qtechWebAuthVCMIBGroups=qtechWebAuthVCMIBGroups, authUserContextNameVC=authUserContextNameVC)
