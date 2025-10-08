#
# PySNMP MIB module HPN-ICF-LOCAL-AAA-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HPN-ICF-LOCAL-AAA-SERVER-MIB", hpnicfLocAAASvrTrapPrex=hpnicfLocAAASvrTrapPrex, hpnicfLocAAASvrTrap=hpnicfLocAAASvrTrap, hpnicfLocAAASvr=hpnicfLocAAASvr, hpnicfLocAAASvrControl=hpnicfLocAAASvrControl, hpnicfLocAAASvrTables=hpnicfLocAAASvrTables, hpnicfLocAAASvrBillExportFailed=hpnicfLocAAASvrBillExportFailed, PYSNMP_MODULE_ID=hpnicfLocAAASvr)
