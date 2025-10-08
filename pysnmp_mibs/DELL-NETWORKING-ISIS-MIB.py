#
# PySNMP MIB module DELL-NETWORKING-ISIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DELL-NETWORKING-ISIS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("DELL-NETWORKING-ISIS-MIB", dellNetIsisSysOloadWaitForBgp=dellNetIsisSysOloadWaitForBgp, dellNetIsisObjects=dellNetIsisObjects, dellNetIsisSysOloadV6SetOloadOnStartupUntil=dellNetIsisSysOloadV6SetOloadOnStartupUntil, DellNetIsisISLevel=DellNetIsisISLevel, dellNetIsisGroups=dellNetIsisGroups, dellNetIsisSysOloadSetOloadOnStartupUntil=dellNetIsisSysOloadSetOloadOnStartupUntil, dellNetIsisSysLevelOverloadState=dellNetIsisSysLevelOverloadState, dellNetIsisCompliances=dellNetIsisCompliances, dellNetIsisNotificationGroup=dellNetIsisNotificationGroup, dellNetIsisMib=dellNetIsisMib, dellNetIsisSysLevelIndex=dellNetIsisSysLevelIndex, dellNetIsisSysLevelTable=dellNetIsisSysLevelTable, dellNetIsisSysLevelEntry=dellNetIsisSysLevelEntry, dellNetIsisSysOloadV6SetOverload=dellNetIsisSysOloadV6SetOverload, dellNetIsisConformance=dellNetIsisConformance, dellNetIsisSysOloadSetOverload=dellNetIsisSysOloadSetOverload, dellNetIsisCompliance=dellNetIsisCompliance, dellNetIsisSystemGroup=dellNetIsisSystemGroup, dellNetIsisAdjChanges=dellNetIsisAdjChanges, dellNetIsisNotifications=dellNetIsisNotifications, PYSNMP_MODULE_ID=dellNetIsisMib, dellNetIsisSysOloadV6WaitForBgp=dellNetIsisSysOloadV6WaitForBgp, dellNetIsisSysLevelV6OverloadState=dellNetIsisSysLevelV6OverloadState)
