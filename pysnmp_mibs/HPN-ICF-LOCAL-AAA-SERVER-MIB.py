#
# PySNMP MIB module HPN-ICF-LOCAL-AAA-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfLocAAASvr = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141))
hpnicfLocAAASvr.setRevisions(('2013-07-06 09:45',))
if mibBuilder.loadTexts: hpnicfLocAAASvr.setLastUpdated('201307060945Z')
if mibBuilder.loadTexts: hpnicfLocAAASvr.setOrganization('')
hpnicfLocAAASvrControl = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 1))
hpnicfLocAAASvrTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 2))
hpnicfLocAAASvrTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 3))
hpnicfLocAAASvrTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 3, 0))
hpnicfLocAAASvrBillExportFailed = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141, 3, 0, 1))
if mibBuilder.loadTexts: hpnicfLocAAASvrBillExportFailed.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LOCAL-AAA-SERVER-MIB", hpnicfLocAAASvrTables=hpnicfLocAAASvrTables, hpnicfLocAAASvrBillExportFailed=hpnicfLocAAASvrBillExportFailed, hpnicfLocAAASvrControl=hpnicfLocAAASvrControl, hpnicfLocAAASvrTrap=hpnicfLocAAASvrTrap, hpnicfLocAAASvr=hpnicfLocAAASvr, PYSNMP_MODULE_ID=hpnicfLocAAASvr, hpnicfLocAAASvrTrapPrex=hpnicfLocAAASvrTrapPrex)
