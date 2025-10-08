#
# PySNMP MIB module ELTEX-MES-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ENDOFMIB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltMesEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1000))
eltMesEndOfMibGroup.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltMesEndOfMibGroup.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltMesEndOfMibGroup.setOrganization('Eltex Enterprise Co, Ltd.')
eltEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltEndOfMib.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ENDOFMIB-MIB", PYSNMP_MODULE_ID=eltMesEndOfMibGroup, eltMesEndOfMibGroup=eltMesEndOfMibGroup, eltEndOfMib=eltEndOfMib)
