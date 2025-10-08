#
# PySNMP MIB module CRESTRON-PROGRAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/crestron/CRESTRON-PROGRAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
crestronControl, = mibBuilder.importSymbols("CRESTRON-ROOT-MIB", "crestronControl")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
crestronProgram = ModuleIdentity((1, 3, 6, 1, 4, 1, 3212, 7, 2))
crestronProgram.setRevisions(('2003-08-18 12:19',))
if mibBuilder.loadTexts: crestronProgram.setLastUpdated('200308181217Z')
if mibBuilder.loadTexts: crestronProgram.setOrganization('Crestron Electronics, Inc.')
class ProgramState(TextualConvention, Integer32):
    reference = '0 : unknown 1 : deleted 2 : initialized 3 : running 4 : paused 5 : stopped 6 : failed'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 6)

crestronProgAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 7, 2, 1))
crestronProgNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 7, 2, 2))
crestronProgStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 3212, 7, 2, 2, 1)).setObjects(("CRESTRON-PROGRAM-MIB", "crestronProgLabel"), ("CRESTRON-PROGRAM-MIB", "crestronProgUptime"))
if mibBuilder.loadTexts: crestronProgStateChangeTrap.setStatus('current')
crestronProgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3))
crestronProgMIBVersion = MibScalar((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crestronProgMIBVersion.setStatus('current')
crestronProgInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2))
crestronProgUptime = MibScalar((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crestronProgUptime.setStatus('current')
crestronProgLabel = MibScalar((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crestronProgLabel.setStatus('current')
crestronProgSymbolCnt = MibScalar((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crestronProgSymbolCnt.setStatus('current')
crestronProgFilename = MibScalar((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crestronProgFilename.setStatus('current')
crestronProgCompiledOn = MibScalar((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crestronProgCompiledOn.setStatus('current')
crestronProgState = MibScalar((1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 6), ProgramState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crestronProgState.setStatus('current')
crestronProgConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 7, 2, 5))
crestronProgCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 7, 2, 5, 1))
crestronProgGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 7, 2, 5, 2))
crestronProgAllObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 3212, 7, 2, 5, 2, 1)).setObjects(("CRESTRON-PROGRAM-MIB", "crestronProgMIBVersion"), ("CRESTRON-PROGRAM-MIB", "crestronProgUptime"), ("CRESTRON-PROGRAM-MIB", "crestronProgLabel"), ("CRESTRON-PROGRAM-MIB", "crestronProgSymbolCnt"), ("CRESTRON-PROGRAM-MIB", "crestronProgFilename"), ("CRESTRON-PROGRAM-MIB", "crestronProgCompiledOn"), ("CRESTRON-PROGRAM-MIB", "crestronProgState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crestronProgAllObjects = crestronProgAllObjects.setStatus('current')
crestronProgAllTraps = NotificationGroup((1, 3, 6, 1, 4, 1, 3212, 7, 2, 5, 2, 2)).setObjects(("CRESTRON-PROGRAM-MIB", "crestronProgStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crestronProgAllTraps = crestronProgAllTraps.setStatus('current')
mibBuilder.exportSymbols("CRESTRON-PROGRAM-MIB", crestronProgCompiledOn=crestronProgCompiledOn, crestronProgram=crestronProgram, crestronProgStateChangeTrap=crestronProgStateChangeTrap, crestronProgMIBVersion=crestronProgMIBVersion, crestronProgFilename=crestronProgFilename, crestronProgNotifications=crestronProgNotifications, crestronProgInfo=crestronProgInfo, crestronProgState=crestronProgState, crestronProgUptime=crestronProgUptime, crestronProgLabel=crestronProgLabel, crestronProgCompliances=crestronProgCompliances, crestronProgGroups=crestronProgGroups, crestronProgObjects=crestronProgObjects, crestronProgSymbolCnt=crestronProgSymbolCnt, ProgramState=ProgramState, crestronProgConformance=crestronProgConformance, PYSNMP_MODULE_ID=crestronProgram, crestronProgAdmin=crestronProgAdmin, crestronProgAllObjects=crestronProgAllObjects, crestronProgAllTraps=crestronProgAllTraps)
