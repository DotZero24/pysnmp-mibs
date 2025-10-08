#
# PySNMP MIB module NTWS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NTWS-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1))
ntwsRootMib.setRevisions(('2007-08-15 00:04', '2006-03-31 00:03', '2005-04-21 00:00',))
if mibBuilder.loadTexts: ntwsRootMib.setLastUpdated('200708150004Z')
if mibBuilder.loadTexts: ntwsRootMib.setOrganization('Nortel Networks')
ntwsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 1))
ntwsTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 2))
ntwsRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3))
ntwsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4))
ntwsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 5))
mibBuilder.exportSymbols("NTWS-ROOT-MIB", PYSNMP_MODULE_ID=ntwsRootMib, ntwsProducts=ntwsProducts, ntwsTraps=ntwsTraps, ntwsMibs=ntwsMibs, ntwsRegistration=ntwsRegistration, ntwsRootMib=ntwsRootMib, ntwsTemporary=ntwsTemporary)
