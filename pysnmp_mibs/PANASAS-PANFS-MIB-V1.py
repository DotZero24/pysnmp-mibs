#
# PySNMP MIB module PANASAS-PANFS-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/panasas/PANASAS-PANFS-MIB-V1
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
panProducts, = mibBuilder.importSymbols("PANASAS-ROOT-MIB", "panProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
panFs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159, 1, 3))
panFs.setRevisions(('2011-04-07 00:00',))
if mibBuilder.loadTexts: panFs.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panFs.setOrganization('Panasas, Inc')
panEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1))
panSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2))
panBSet = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 3))
panVol = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4))
panPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 5))
mibBuilder.exportSymbols("PANASAS-PANFS-MIB-V1", panEvents=panEvents, panBSet=panBSet, PYSNMP_MODULE_ID=panFs, panPerf=panPerf, panSystem=panSystem, panFs=panFs, panVol=panVol)
