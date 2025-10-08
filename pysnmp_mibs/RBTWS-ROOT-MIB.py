#
# PySNMP MIB module RBTWS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/RBTWS-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctronTrapeze = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15))
rbtwsRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1))
rbtwsRootMib.setRevisions(('2005-05-07 00:00',))
if mibBuilder.loadTexts: rbtwsRootMib.setLastUpdated('200505070000Z')
if mibBuilder.loadTexts: rbtwsRootMib.setOrganization('Enterasys Networks')
rbtwsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 1))
rbtwsTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2))
rbtwsRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3))
rbtwsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4))
rbtwsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5))
mibBuilder.exportSymbols("RBTWS-ROOT-MIB", rbtwsMibs=rbtwsMibs, cabletron=cabletron, rbtwsProducts=rbtwsProducts, rbtwsTemporary=rbtwsTemporary, PYSNMP_MODULE_ID=rbtwsRootMib, ctronTrapeze=ctronTrapeze, mibs=mibs, rbtwsRootMib=rbtwsRootMib, rbtwsRegistration=rbtwsRegistration, rbtwsTraps=rbtwsTraps)
