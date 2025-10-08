#
# PySNMP MIB module LEFTHAND-NETWORKS-NSM-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-NSM-NTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lhnNsm, lhnModules = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG-MIB", "lhnNsm", "lhnModules")
lhnNsmNTP, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NSM-MIB", "lhnNsmNTP")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
lhnNsmNTPModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 2, 1, 6))
lhnNsmNTPModule.setRevisions(('2013-11-19 00:00', '2013-06-25 00:00', '2012-09-04 00:00', '2011-06-21 00:00', '2010-09-07 00:00', '2010-07-19 00:00', '2009-11-20 00:00', '2009-03-10 00:00', '2008-01-24 00:00',))
if mibBuilder.loadTexts: lhnNsmNTPModule.setLastUpdated('201311190000Z')
if mibBuilder.loadTexts: lhnNsmNTPModule.setOrganization('Hewlett Packard Company, StorageWorks Division')
lhnNsmNTPModuleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1))
lhnNsmNTPModuleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 1))
lhnNsmNTPModuleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 2))
lefthandNetworksNsmNTPMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 1, 1)).setObjects(("LEFTHAND-NETWORKS-NSM-NTP-MIB", "lefthandNetworksNsmNtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lefthandNetworksNsmNTPMibCompliance = lefthandNetworksNsmNTPMibCompliance.setStatus('current')
lefthandNetworksNsmNtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 2, 1)).setObjects(("LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpCount"), ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "timeGMTTime"), ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "timeTimeZone"), ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpPreferred"), ("LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpServer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lefthandNetworksNsmNtpGroup = lefthandNetworksNsmNtpGroup.setStatus('current')
lefthandNetworksNsmNtpGroupObsolete = ObjectGroup((1, 3, 6, 1, 4, 1, 9804, 2, 1, 6, 1, 2, 2)).setObjects(("LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lefthandNetworksNsmNtpGroupObsolete = lefthandNetworksNsmNtpGroupObsolete.setStatus('obsolete')
ntpCount = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpCount.setStatus('current')
ntpTable = MibTable((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2), )
if mibBuilder.loadTexts: ntpTable.setStatus('current')
ntpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1), ).setIndexNames((0, "LEFTHAND-NETWORKS-NSM-NTP-MIB", "ntpIndex"))
if mibBuilder.loadTexts: ntpEntry.setStatus('current')
ntpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ntpIndex.setStatus('current')
ntpPreferred = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpPreferred.setStatus('current')
ntpServer = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpServer.setStatus('current')
ntpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 2, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpRowStatus.setStatus('obsolete')
timeGMTTime = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeGMTTime.setStatus('current')
timeTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeTimeZone.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NSM-NTP-MIB", timeTimeZone=timeTimeZone, ntpTable=ntpTable, ntpServer=ntpServer, timeGMTTime=timeGMTTime, lhnNsmNTPModuleConformance=lhnNsmNTPModuleConformance, ntpRowStatus=ntpRowStatus, lhnNsmNTPModuleGroups=lhnNsmNTPModuleGroups, lhnNsmNTPModuleCompliances=lhnNsmNTPModuleCompliances, lefthandNetworksNsmNTPMibCompliance=lefthandNetworksNsmNTPMibCompliance, PYSNMP_MODULE_ID=lhnNsmNTPModule, ntpCount=ntpCount, lhnNsmNTPModule=lhnNsmNTPModule, ntpEntry=ntpEntry, ntpIndex=ntpIndex, lefthandNetworksNsmNtpGroupObsolete=lefthandNetworksNsmNtpGroupObsolete, lefthandNetworksNsmNtpGroup=lefthandNetworksNsmNtpGroup, ntpPreferred=ntpPreferred)
