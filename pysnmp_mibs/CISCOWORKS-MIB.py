#
# PySNMP MIB module CISCOWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCOWORKS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoworks, = mibBuilder.importSymbols("CISCO-SMI", "ciscoworks")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 14, 1))
cwLogMIB.setRevisions(('2003-02-18 00:00', '1995-04-02 00:00',))
if mibBuilder.loadTexts: cwLogMIB.setLastUpdated('200302180000Z')
if mibBuilder.loadTexts: cwLogMIB.setOrganization('Cisco Systems, Inc.')
cwLog = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 1))
cwTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 2))
cwMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3))
cwLogDate = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(15, 15)).setFixedLength(15)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogDate.setStatus('current')
cwLogSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ciscoworks", 2), ("device", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogSource.setStatus('current')
cwLogApp = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogApp.setStatus('current')
cwLogMsg = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogMsg.setStatus('current')
cwTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0))
cwAppLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogApp"), ("CISCOWORKS-MIB", "cwLogMsg"))
if mibBuilder.loadTexts: cwAppLogTrap.setStatus('current')
cwDevLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogMsg"))
if mibBuilder.loadTexts: cwDevLogTrap.setStatus('current')
ciscoCwMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1))
ciscoCwMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2))
ciscoCwMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1, 1)).setObjects(("CISCOWORKS-MIB", "ciscoCwObjectsGroup"), ("CISCOWORKS-MIB", "ciscoCwNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwMIBCompliance = ciscoCwMIBCompliance.setStatus('current')
ciscoCwObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 7)).setObjects(("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogApp"), ("CISCOWORKS-MIB", "cwLogMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwObjectsGroup = ciscoCwObjectsGroup.setStatus('current')
ciscoCwNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 12)).setObjects(("CISCOWORKS-MIB", "cwAppLogTrap"), ("CISCOWORKS-MIB", "cwDevLogTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwNotificationsGroup = ciscoCwNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCOWORKS-MIB", cwMIBConform=cwMIBConform, cwDevLogTrap=cwDevLogTrap, ciscoCwNotificationsGroup=ciscoCwNotificationsGroup, cwLogMsg=cwLogMsg, ciscoCwMIBCompliance=ciscoCwMIBCompliance, cwTrapsPrefix=cwTrapsPrefix, ciscoCwMIBCompliances=ciscoCwMIBCompliances, cwLogSource=cwLogSource, cwLogApp=cwLogApp, ciscoCwObjectsGroup=ciscoCwObjectsGroup, cwLogDate=cwLogDate, cwLog=cwLog, cwTraps=cwTraps, ciscoCwMIBGroups=ciscoCwMIBGroups, PYSNMP_MODULE_ID=cwLogMIB, cwAppLogTrap=cwAppLogTrap, cwLogMIB=cwLogMIB)
