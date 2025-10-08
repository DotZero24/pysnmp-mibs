#
# PySNMP MIB module RBTWS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/RBTWS-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("RBTWS-ROOT-MIB", cabletron=cabletron, rbtwsTraps=rbtwsTraps, rbtwsProducts=rbtwsProducts, ctronTrapeze=ctronTrapeze, PYSNMP_MODULE_ID=rbtwsRootMib, rbtwsRegistration=rbtwsRegistration, rbtwsMibs=rbtwsMibs, rbtwsRootMib=rbtwsRootMib, mibs=mibs, rbtwsTemporary=rbtwsTemporary)
