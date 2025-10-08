#
# PySNMP MIB module LEXMARK-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/lexmark/LEXMARK-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lexmarkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 4, 1))
lexmarkMIB.setRevisions(('2010-12-01 23:00', '2009-11-24 20:40',))
if mibBuilder.loadTexts: lexmarkMIB.setLastUpdated('201012012300Z')
if mibBuilder.loadTexts: lexmarkMIB.setOrganization('Lexmark International, Inc.')
lexmark = MibIdentifier((1, 3, 6, 1, 4, 1, 641))
lexmarkModules = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 4))
lexmarkMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 5))
mibBuilder.exportSymbols("LEXMARK-ROOT-MIB", lexmarkMibObjects=lexmarkMibObjects, lexmarkModules=lexmarkModules, lexmarkMIB=lexmarkMIB, lexmark=lexmark, PYSNMP_MODULE_ID=lexmarkMIB)
