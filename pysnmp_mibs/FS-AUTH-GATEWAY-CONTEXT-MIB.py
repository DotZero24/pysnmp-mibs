#
# PySNMP MIB module FS-AUTH-GATEWAY-CONTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-AUTH-GATEWAY-CONTEXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fsWebAuthVCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67))
fsWebAuthVCMIB.setRevisions(('2009-12-06 00:00',))
if mibBuilder.loadTexts: fsWebAuthVCMIB.setLastUpdated('200912060000Z')
if mibBuilder.loadTexts: fsWebAuthVCMIB.setOrganization('FS.COM Inc..')
fsWebAuthVCMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1))
fsWebAuthUserVCTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1, 1), )
if mibBuilder.loadTexts: fsWebAuthUserVCTable.setStatus('current')
fsWebAuthUserVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1, 1, 1), ).setIndexNames((0, "FS-AUTH-GATEWAY-CONTEXT-MIB", "authUserContextNameVC"), (0, "FS-AUTH-GATEWAY-CONTEXT-MIB", "authUserIpAddrVC"))
if mibBuilder.loadTexts: fsWebAuthUserVCEntry.setStatus('current')
authUserContextNameVC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserContextNameVC.setStatus('current')
authUserIpAddrVC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserIpAddrVC.setStatus('current')
authUserOnlineFlagVC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserOnlineFlagVC.setStatus('current')
authUserTimeLimitVC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1, 1, 1, 4), Gauge32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: authUserTimeLimitVC.setStatus('current')
authUserTimeUsedVC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserTimeUsedVC.setStatus('current')
authUserStatusVC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: authUserStatusVC.setStatus('current')
fsWebAuthVCMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 3))
fsWebAuthVCMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 3, 1))
fsWebAuthVCMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 3, 2))
fsWebAuthVCMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 3, 1, 1)).setObjects(("FS-AUTH-GATEWAY-CONTEXT-MIB", "fsWebAuthVCMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsWebAuthVCMIBCompliance = fsWebAuthVCMIBCompliance.setStatus('current')
fsWebAuthVCMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 67, 3, 2, 1)).setObjects(("FS-AUTH-GATEWAY-CONTEXT-MIB", "authUserContextNameVC"), ("FS-AUTH-GATEWAY-CONTEXT-MIB", "authUserIpAddrVC"), ("FS-AUTH-GATEWAY-CONTEXT-MIB", "authUserOnlineFlagVC"), ("FS-AUTH-GATEWAY-CONTEXT-MIB", "authUserTimeLimitVC"), ("FS-AUTH-GATEWAY-CONTEXT-MIB", "authUserTimeUsedVC"), ("FS-AUTH-GATEWAY-CONTEXT-MIB", "authUserStatusVC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsWebAuthVCMIBGroup = fsWebAuthVCMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-AUTH-GATEWAY-CONTEXT-MIB", authUserTimeLimitVC=authUserTimeLimitVC, authUserIpAddrVC=authUserIpAddrVC, fsWebAuthVCMIBGroups=fsWebAuthVCMIBGroups, authUserOnlineFlagVC=authUserOnlineFlagVC, authUserStatusVC=authUserStatusVC, PYSNMP_MODULE_ID=fsWebAuthVCMIB, fsWebAuthVCMIB=fsWebAuthVCMIB, fsWebAuthVCMIBConformance=fsWebAuthVCMIBConformance, fsWebAuthVCMIBCompliance=fsWebAuthVCMIBCompliance, fsWebAuthVCMIBCompliances=fsWebAuthVCMIBCompliances, fsWebAuthVCMIBGroup=fsWebAuthVCMIBGroup, fsWebAuthUserVCTable=fsWebAuthUserVCTable, fsWebAuthUserVCEntry=fsWebAuthUserVCEntry, authUserTimeUsedVC=authUserTimeUsedVC, fsWebAuthVCMIBObjects=fsWebAuthVCMIBObjects, authUserContextNameVC=authUserContextNameVC)
