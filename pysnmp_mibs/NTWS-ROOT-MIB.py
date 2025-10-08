#
# PySNMP MIB module NTWS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:03:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntwsRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1))
ntwsRootMib.setRevisions(('2007-08-15 00:04', '2006-03-31 00:03', '2005-04-21 00:00',))
if mibBuilder.loadTexts: ntwsRootMib.setLastUpdated('200708150004Z')
if mibBuilder.loadTexts: ntwsRootMib.setOrganization('Nortel Networks')
ntwsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 1))
ntwsTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 2))
ntwsRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3))
ntwsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4))
ntwsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 5))
mibBuilder.exportSymbols("NTWS-ROOT-MIB", ntwsMibs=ntwsMibs, ntwsTemporary=ntwsTemporary, ntwsProducts=ntwsProducts, PYSNMP_MODULE_ID=ntwsRootMib, ntwsTraps=ntwsTraps, ntwsRootMib=ntwsRootMib, ntwsRegistration=ntwsRegistration)
