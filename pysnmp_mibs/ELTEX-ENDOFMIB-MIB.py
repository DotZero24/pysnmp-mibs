#
# PySNMP MIB module ELTEX-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-ENDOFMIB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
elt, = mibBuilder.importSymbols("ELTEX-MIB", "elt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1000))
eltEndOfMibGroup.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltEndOfMibGroup.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltEndOfMibGroup.setOrganization('Eltex Enterprise Co, Ltd.')
eltEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltEndOfMib.setStatus('current')
mibBuilder.exportSymbols("ELTEX-ENDOFMIB-MIB", PYSNMP_MODULE_ID=eltEndOfMibGroup, eltEndOfMibGroup=eltEndOfMibGroup, eltEndOfMib=eltEndOfMib)
