#
# PySNMP MIB module ONEACCESS-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-PING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pingCtlTestName, pingCtlOwnerIndex = mibBuilder.importSymbols("DISMAN-PING-MIB", "pingCtlTestName", "pingCtlOwnerIndex")
oneAccess, oacExpIMPing, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oneAccess", "oacExpIMPing", "oacMIBModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ONEACCESS-PING-MIB", oacPingJitterSamples=oacPingJitterSamples, oacPingConformance=oacPingConformance, oacPingNotifications=oacPingNotifications, oacPingResultsAverageJitter=oacPingResultsAverageJitter, oacPingGroups=oacPingGroups, oacPingGroup=oacPingGroup, oacPingResultsEntry=oacPingResultsEntry, oacPingResultsMinJitter=oacPingResultsMinJitter, oacPingResultsTable=oacPingResultsTable, oacPingCompliance=oacPingCompliance, PYSNMP_MODULE_ID=oacPingMIBModule, oacPingCompliances=oacPingCompliances, oacPingObjects=oacPingObjects, oacPingResultsMaxJitter=oacPingResultsMaxJitter, oacPingMIBModule=oacPingMIBModule)
