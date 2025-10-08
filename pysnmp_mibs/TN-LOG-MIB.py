#
# PySNMP MIB module TN-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TN-LOG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:39:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
TNamedItem, = mibBuilder.importSymbols("TN-TC-MIB", "TNamedItem")
tnSRObjs, tnSRMIBModules = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSRObjs", "tnSRMIBModules")
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
mibBuilder.exportSymbols("TN-LOG-MIB", PYSNMP_MODULE_ID=tnSRLogMIBModule, tnSRLogObjs=tnSRLogObjs, tnSRLogMIBModule=tnSRLogMIBModule, tnEventAppEntry=tnEventAppEntry, tnEventAppName=tnEventAppName, tnEventAppTable=tnEventAppTable, tnEventAppIndex=tnEventAppIndex)
