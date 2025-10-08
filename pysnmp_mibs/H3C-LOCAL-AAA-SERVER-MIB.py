#
# PySNMP MIB module H3C-LOCAL-AAA-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("H3C-LOCAL-AAA-SERVER-MIB", h3cLocAAASvr=h3cLocAAASvr, h3cLocAAASvrTrapPrex=h3cLocAAASvrTrapPrex, h3cLocAAASvrControl=h3cLocAAASvrControl, h3cLocAAASvrTrap=h3cLocAAASvrTrap, PYSNMP_MODULE_ID=h3cLocAAASvr, h3cLocAAASvrTables=h3cLocAAASvrTables, h3cLocAAASvrBillExportFailed=h3cLocAAASvrBillExportFailed)
