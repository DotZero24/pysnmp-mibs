#
# PySNMP MIB module PANASAS-PANFS-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/panasas/PANASAS-PANFS-MIB-V1
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
panProducts, = mibBuilder.importSymbols("PANASAS-ROOT-MIB", "panProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panFs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159, 1, 3))
panFs.setRevisions(('2011-04-07 00:00',))
if mibBuilder.loadTexts: panFs.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panFs.setOrganization('Panasas, Inc')
panEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1))
panSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2))
panBSet = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 3))
panVol = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4))
panPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 5))
mibBuilder.exportSymbols("PANASAS-PANFS-MIB-V1", panSystem=panSystem, panVol=panVol, panBSet=panBSet, panFs=panFs, panPerf=panPerf, PYSNMP_MODULE_ID=panFs, panEvents=panEvents)
