#
# PySNMP MIB module CIENA-OME6500-S5-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-OME6500-S5-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaSeries5000, = mibBuilder.importSymbols("CIENA-OME6500-SYNOPTICS-ROOT-MIB", "cienaSeries5000")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cienaS5RootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 68, 11, 2, 1, 6, 0))
cienaS5RootMib.setRevisions(('2015-10-20 00:00',))
if mibBuilder.loadTexts: cienaS5RootMib.setLastUpdated('201510200000Z')
if mibBuilder.loadTexts: cienaS5RootMib.setOrganization('Ciena Corp')
cienaS5EnMsTop = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 68, 11, 2, 1, 6, 13))
mibBuilder.exportSymbols("CIENA-OME6500-S5-ROOT-MIB", cienaS5RootMib=cienaS5RootMib, PYSNMP_MODULE_ID=cienaS5RootMib, cienaS5EnMsTop=cienaS5EnMsTop)
