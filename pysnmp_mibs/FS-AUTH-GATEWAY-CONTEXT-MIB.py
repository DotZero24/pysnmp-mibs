#
# PySNMP MIB module FS-AUTH-GATEWAY-CONTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-AUTH-GATEWAY-CONTEXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-AUTH-GATEWAY-CONTEXT-MIB", authUserIpAddrVC=authUserIpAddrVC, fsWebAuthUserVCTable=fsWebAuthUserVCTable, fsWebAuthVCMIB=fsWebAuthVCMIB, authUserTimeLimitVC=authUserTimeLimitVC, fsWebAuthVCMIBGroup=fsWebAuthVCMIBGroup, fsWebAuthUserVCEntry=fsWebAuthUserVCEntry, fsWebAuthVCMIBConformance=fsWebAuthVCMIBConformance, fsWebAuthVCMIBCompliances=fsWebAuthVCMIBCompliances, fsWebAuthVCMIBObjects=fsWebAuthVCMIBObjects, authUserStatusVC=authUserStatusVC, authUserContextNameVC=authUserContextNameVC, authUserTimeUsedVC=authUserTimeUsedVC, fsWebAuthVCMIBCompliance=fsWebAuthVCMIBCompliance, fsWebAuthVCMIBGroups=fsWebAuthVCMIBGroups, PYSNMP_MODULE_ID=fsWebAuthVCMIB, authUserOnlineFlagVC=authUserOnlineFlagVC)
