#
# PySNMP MIB module DELL-NETWORKING-ISIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/DELL-NETWORKING-ISIS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
dellNetIsisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 18))
dellNetIsisMib.setRevisions(('2011-07-01 00:00',))
if mibBuilder.loadTexts: dellNetIsisMib.setLastUpdated('201107010000Z')
if mibBuilder.loadTexts: dellNetIsisMib.setOrganization('Dell Inc')
class DellNetIsisISLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("area", 1), ("domain", 2))

dellNetIsisNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 0))
dellNetIsisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1))
dellNetIsisConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2))
dellNetIsisSysOloadSetOverload = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIsisSysOloadSetOverload.setStatus('current')
dellNetIsisSysOloadSetOloadOnStartupUntil = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(600)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIsisSysOloadSetOloadOnStartupUntil.setStatus('current')
dellNetIsisSysOloadWaitForBgp = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(600)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIsisSysOloadWaitForBgp.setStatus('current')
dellNetIsisSysOloadV6SetOverload = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIsisSysOloadV6SetOverload.setStatus('current')
dellNetIsisSysOloadV6SetOloadOnStartupUntil = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(600)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIsisSysOloadV6SetOloadOnStartupUntil.setStatus('current')
dellNetIsisSysOloadV6WaitForBgp = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(600)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIsisSysOloadV6WaitForBgp.setStatus('current')
dellNetIsisSysLevelTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7), )
if mibBuilder.loadTexts: dellNetIsisSysLevelTable.setStatus('current')
dellNetIsisSysLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1), ).setIndexNames((0, "DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysLevelIndex"))
if mibBuilder.loadTexts: dellNetIsisSysLevelEntry.setStatus('current')
dellNetIsisSysLevelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 1), DellNetIsisISLevel())
if mibBuilder.loadTexts: dellNetIsisSysLevelIndex.setStatus('current')
dellNetIsisSysLevelOverloadState = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIsisSysLevelOverloadState.setStatus('current')
dellNetIsisSysLevelV6OverloadState = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIsisSysLevelV6OverloadState.setStatus('current')
dellNetIsisAdjChanges = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 18, 0, 1))
if mibBuilder.loadTexts: dellNetIsisAdjChanges.setStatus('current')
dellNetIsisGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1))
dellNetIsisCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 2))
dellNetIsisCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 2, 1)).setObjects(("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSystemGroup"), ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetIsisCompliance = dellNetIsisCompliance.setStatus('current')
dellNetIsisSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1, 1)).setObjects(("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadSetOverload"), ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadSetOloadOnStartupUntil"), ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadWaitForBgp"), ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadV6SetOverload"), ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadV6SetOloadOnStartupUntil"), ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysLevelOverloadState"), ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysLevelV6OverloadState"), ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadV6WaitForBgp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetIsisSystemGroup = dellNetIsisSystemGroup.setStatus('current')
dellNetIsisNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1, 2)).setObjects(("DELL-NETWORKING-ISIS-MIB", "dellNetIsisAdjChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetIsisNotificationGroup = dellNetIsisNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DELL-NETWORKING-ISIS-MIB", dellNetIsisObjects=dellNetIsisObjects, DellNetIsisISLevel=DellNetIsisISLevel, dellNetIsisSysLevelIndex=dellNetIsisSysLevelIndex, dellNetIsisSysOloadV6WaitForBgp=dellNetIsisSysOloadV6WaitForBgp, dellNetIsisSysLevelTable=dellNetIsisSysLevelTable, dellNetIsisAdjChanges=dellNetIsisAdjChanges, dellNetIsisSysLevelV6OverloadState=dellNetIsisSysLevelV6OverloadState, dellNetIsisSysOloadV6SetOloadOnStartupUntil=dellNetIsisSysOloadV6SetOloadOnStartupUntil, dellNetIsisGroups=dellNetIsisGroups, dellNetIsisConformance=dellNetIsisConformance, PYSNMP_MODULE_ID=dellNetIsisMib, dellNetIsisMib=dellNetIsisMib, dellNetIsisSysOloadSetOloadOnStartupUntil=dellNetIsisSysOloadSetOloadOnStartupUntil, dellNetIsisCompliances=dellNetIsisCompliances, dellNetIsisSysOloadSetOverload=dellNetIsisSysOloadSetOverload, dellNetIsisCompliance=dellNetIsisCompliance, dellNetIsisNotifications=dellNetIsisNotifications, dellNetIsisSysOloadV6SetOverload=dellNetIsisSysOloadV6SetOverload, dellNetIsisSysLevelEntry=dellNetIsisSysLevelEntry, dellNetIsisNotificationGroup=dellNetIsisNotificationGroup, dellNetIsisSysOloadWaitForBgp=dellNetIsisSysOloadWaitForBgp, dellNetIsisSysLevelOverloadState=dellNetIsisSysLevelOverloadState, dellNetIsisSystemGroup=dellNetIsisSystemGroup)
