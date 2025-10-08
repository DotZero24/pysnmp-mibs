#
# PySNMP MIB module H3C-LOCAL-AAA-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cLocAAASvr = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 141))
h3cLocAAASvr.setRevisions(('2013-07-06 09:45',))
if mibBuilder.loadTexts: h3cLocAAASvr.setLastUpdated('201307060945Z')
if mibBuilder.loadTexts: h3cLocAAASvr.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cLocAAASvrControl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 141, 1))
h3cLocAAASvrTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 141, 2))
h3cLocAAASvrTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 141, 3))
h3cLocAAASvrTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 141, 3, 0))
h3cLocAAASvrBillExportFailed = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 141, 3, 0, 1))
if mibBuilder.loadTexts: h3cLocAAASvrBillExportFailed.setStatus('current')
mibBuilder.exportSymbols("H3C-LOCAL-AAA-SERVER-MIB", h3cLocAAASvrControl=h3cLocAAASvrControl, h3cLocAAASvrTables=h3cLocAAASvrTables, h3cLocAAASvrBillExportFailed=h3cLocAAASvrBillExportFailed, h3cLocAAASvrTrap=h3cLocAAASvrTrap, h3cLocAAASvr=h3cLocAAASvr, h3cLocAAASvrTrapPrex=h3cLocAAASvrTrapPrex, PYSNMP_MODULE_ID=h3cLocAAASvr)
