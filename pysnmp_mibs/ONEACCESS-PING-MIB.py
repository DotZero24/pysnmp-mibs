#
# PySNMP MIB module ONEACCESS-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-PING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pingCtlTestName, pingCtlOwnerIndex = mibBuilder.importSymbols("DISMAN-PING-MIB", "pingCtlTestName", "pingCtlOwnerIndex")
oneAccess, oacMIBModules, oacExpIMPing = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oneAccess", "oacMIBModules", "oacExpIMPing")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacPingMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 6601))
oacPingMIBModule.setRevisions(('2011-06-15 00:00', '2010-07-08 00:01',))
if mibBuilder.loadTexts: oacPingMIBModule.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oacPingMIBModule.setOrganization(' OneAccess ')
oacPingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 0))
oacPingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1))
oacPingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2))
oacPingResultsTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3), )
if mibBuilder.loadTexts: oacPingResultsTable.setStatus('current')
oacPingResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1), ).setIndexNames((0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"), (0, "DISMAN-PING-MIB", "pingCtlTestName"))
if mibBuilder.loadTexts: oacPingResultsEntry.setStatus('current')
oacPingJitterSamples = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacPingJitterSamples.setStatus('current')
oacPingResultsMinJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 2), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacPingResultsMinJitter.setStatus('current')
oacPingResultsMaxJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 3), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacPingResultsMaxJitter.setStatus('current')
oacPingResultsAverageJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 4), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacPingResultsAverageJitter.setStatus('current')
oacPingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 1))
oacPingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 2))
oacPingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 1, 1)).setObjects(("ONEACCESS-PING-MIB", "oacPingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacPingCompliance = oacPingCompliance.setStatus('current')
oacPingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 2, 1)).setObjects(("ONEACCESS-PING-MIB", "oacPingJitterSamples"), ("ONEACCESS-PING-MIB", "oacPingResultsMinJitter"), ("ONEACCESS-PING-MIB", "oacPingResultsMaxJitter"), ("ONEACCESS-PING-MIB", "oacPingResultsAverageJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacPingGroup = oacPingGroup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-PING-MIB", oacPingGroups=oacPingGroups, oacPingResultsAverageJitter=oacPingResultsAverageJitter, oacPingResultsMaxJitter=oacPingResultsMaxJitter, oacPingGroup=oacPingGroup, oacPingCompliance=oacPingCompliance, oacPingObjects=oacPingObjects, oacPingMIBModule=oacPingMIBModule, PYSNMP_MODULE_ID=oacPingMIBModule, oacPingResultsTable=oacPingResultsTable, oacPingConformance=oacPingConformance, oacPingResultsMinJitter=oacPingResultsMinJitter, oacPingJitterSamples=oacPingJitterSamples, oacPingResultsEntry=oacPingResultsEntry, oacPingCompliances=oacPingCompliances, oacPingNotifications=oacPingNotifications)
