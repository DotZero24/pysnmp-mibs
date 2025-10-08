#
# PySNMP MIB module CIENA-OME6500-SYNOPTICS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-OME6500-SYNOPTICS-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaOme6500, = mibBuilder.importSymbols("CIENA-OME6500-OPTICAL-MIB", "cienaOme6500")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaSynoptics = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 68, 11, 2))
cienaSynoptics.setRevisions(('2005-10-11 00:00',))
if mibBuilder.loadTexts: cienaSynoptics.setLastUpdated('200510110000Z')
if mibBuilder.loadTexts: cienaSynoptics.setOrganization('Ciena Corp.')
cienaSynopticProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 68, 11, 2, 1))
cienaSeries5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 68, 11, 2, 1, 6))
mibBuilder.exportSymbols("CIENA-OME6500-SYNOPTICS-ROOT-MIB", cienaSynoptics=cienaSynoptics, PYSNMP_MODULE_ID=cienaSynoptics, cienaSynopticProducts=cienaSynopticProducts, cienaSeries5000=cienaSeries5000)
