#
# PySNMP MIB module CIENA-OME6500-SYNOPTICS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-OME6500-SYNOPTICS-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaOme6500, = mibBuilder.importSymbols("CIENA-OME6500-OPTICAL-MIB", "cienaOme6500")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaSynoptics = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 68, 11, 2))
cienaSynoptics.setRevisions(('2005-10-11 00:00',))
if mibBuilder.loadTexts: cienaSynoptics.setLastUpdated('200510110000Z')
if mibBuilder.loadTexts: cienaSynoptics.setOrganization('Ciena Corp.')
cienaSynopticProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 68, 11, 2, 1))
cienaSeries5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 68, 11, 2, 1, 6))
mibBuilder.exportSymbols("CIENA-OME6500-SYNOPTICS-ROOT-MIB", PYSNMP_MODULE_ID=cienaSynoptics, cienaSynoptics=cienaSynoptics, cienaSynopticProducts=cienaSynopticProducts, cienaSeries5000=cienaSeries5000)
