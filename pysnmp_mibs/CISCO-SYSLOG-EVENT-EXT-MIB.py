#
# PySNMP MIB module CISCO-SYSLOG-EVENT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SYSLOG-EVENT-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SyslogSeverity, = mibBuilder.importSymbols("CISCO-SYSLOG-MIB", "SyslogSeverity")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSyslogEventExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 270))
ciscoSyslogEventExtMIB.setRevisions(('2002-02-12 00:00',))
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setLastUpdated('200202120000Z')
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setOrganization('Cisco System Inc.')
ciscoSyslogEventExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 1))
cslogEventConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1))
class CslogEventDisposition(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("count", 1), ("display", 2), ("notify", 3))

cslogEventDetailDefault = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noDisplay", 1), ("sparseDetail", 2), ("normalDetail", 3), ("verboseDetail", 4), ("exhaustiveDetail", 5))).clone('normalDetail')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventDetailDefault.setStatus('current')
cslogEventSeverityDispConsole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 2), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispConsole.setStatus('current')
cslogEventSeverityDispHtmlGUI = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 3), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlGUI.setStatus('current')
cslogEventSeverityDispHtmlConsol = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 4), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlConsol.setStatus('current')
cslogEventDispositionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5), )
if mibBuilder.loadTexts: cslogEventDispositionTable.setStatus('current')
cslogEventDispositionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionSeverity"))
if mibBuilder.loadTexts: cslogEventDispositionEntry.setStatus('current')
cslogEventDispositionSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 1), SyslogSeverity())
if mibBuilder.loadTexts: cslogEventDispositionSeverity.setStatus('current')
cslogEventDisposition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 2), CslogEventDisposition().clone(namedValues=NamedValues(("none", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventDisposition.setStatus('current')
cslogEventDispositionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslogEventDispositionCount.setStatus('current')
ciscoSlogEventExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2))
ciscoSlogEventExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1))
ciscoSlogEventExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2))
ciscoSlogEventExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1, 1)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "ciscoSlogEventExtConfigGroup"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "ciscoSlogEventExtStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtCompliance = ciscoSlogEventExtCompliance.setStatus('current')
ciscoSlogEventExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 1)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDetailDefault"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispConsole"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlGUI"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlConsol"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDisposition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtConfigGroup = ciscoSlogEventExtConfigGroup.setStatus('current')
ciscoSlogEventExtStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 2)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtStatsGroup = ciscoSlogEventExtStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSLOG-EVENT-EXT-MIB", cslogEventDispositionSeverity=cslogEventDispositionSeverity, ciscoSlogEventExtConfigGroup=ciscoSlogEventExtConfigGroup, ciscoSlogEventExtMIBGroups=ciscoSlogEventExtMIBGroups, cslogEventSeverityDispConsole=cslogEventSeverityDispConsole, cslogEventDetailDefault=cslogEventDetailDefault, ciscoSyslogEventExtMIBObjects=ciscoSyslogEventExtMIBObjects, cslogEventDisposition=cslogEventDisposition, ciscoSlogEventExtMIBCompliances=ciscoSlogEventExtMIBCompliances, CslogEventDisposition=CslogEventDisposition, cslogEventDispositionEntry=cslogEventDispositionEntry, cslogEventSeverityDispHtmlGUI=cslogEventSeverityDispHtmlGUI, PYSNMP_MODULE_ID=ciscoSyslogEventExtMIB, cslogEventSeverityDispHtmlConsol=cslogEventSeverityDispHtmlConsol, ciscoSlogEventExtStatsGroup=ciscoSlogEventExtStatsGroup, cslogEventDispositionCount=cslogEventDispositionCount, ciscoSyslogEventExtMIB=ciscoSyslogEventExtMIB, ciscoSlogEventExtMIBConformance=ciscoSlogEventExtMIBConformance, cslogEventDispositionTable=cslogEventDispositionTable, cslogEventConfig=cslogEventConfig, ciscoSlogEventExtCompliance=ciscoSlogEventExtCompliance)
