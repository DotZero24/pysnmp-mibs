#
# PySNMP MIB module TN-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TN-LOG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:21:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
TNamedItem, = mibBuilder.importSymbols("TN-TC-MIB", "TNamedItem")
tnSRMIBModules, tnSRObjs = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSRMIBModules", "tnSRObjs")
tnSysSwitchId, = mibBuilder.importSymbols("TROPIC-SYSTEM-MIB", "tnSysSwitchId")
tnSRLogMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 12))
tnSRLogMIBModule.setRevisions(('2012-12-05 00:00', '2009-02-28 00:00', '2008-01-01 00:00', '2007-01-01 00:00', '2006-03-15 00:00', '2005-01-24 00:00', '2004-05-27 00:00', '2004-01-15 00:00', '2003-08-15 00:00', '2003-01-20 00:00', '2001-11-10 00:00',))
if mibBuilder.loadTexts: tnSRLogMIBModule.setLastUpdated('201212050000Z')
if mibBuilder.loadTexts: tnSRLogMIBModule.setOrganization('Nokia')
tnSRLogObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12))
tnEventAppTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9), )
if mibBuilder.loadTexts: tnEventAppTable.setStatus('current')
tnEventAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-LOG-MIB", "tnEventAppIndex"))
if mibBuilder.loadTexts: tnEventAppEntry.setStatus('current')
tnEventAppIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1, 1), Unsigned32())
if mibBuilder.loadTexts: tnEventAppIndex.setStatus('current')
tnEventAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1, 2), TNamedItem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnEventAppName.setStatus('current')
mibBuilder.exportSymbols("TN-LOG-MIB", tnEventAppTable=tnEventAppTable, tnEventAppIndex=tnEventAppIndex, tnSRLogObjs=tnSRLogObjs, tnSRLogMIBModule=tnSRLogMIBModule, tnEventAppName=tnEventAppName, tnEventAppEntry=tnEventAppEntry, PYSNMP_MODULE_ID=tnSRLogMIBModule)
