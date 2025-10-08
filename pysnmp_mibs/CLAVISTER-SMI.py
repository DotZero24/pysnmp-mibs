#
# PySNMP MIB module CLAVISTER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/clavister/CLAVISTER-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:42:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
clavisterSmiMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5089, 0))
clavisterSmiMibModule.setRevisions(('2012-06-27 09:00', '2006-05-19 09:00',))
if mibBuilder.loadTexts: clavisterSmiMibModule.setLastUpdated('201206270900Z')
if mibBuilder.loadTexts: clavisterSmiMibModule.setOrganization('Clavister AB')
clavister = MibIdentifier((1, 3, 6, 1, 4, 1, 5089))
clavisterOS = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1))
clavisterOSTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 0))
clavisterOSTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 1))
clavisterOSStats = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 1, 2))
clavisterReg = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2))
clavisterMibModules = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 1))
clavisterMibConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 2))
clavisterMibObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 2, 3))
clavisterSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 3))
clavisterSystemTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 3, 0))
clavisterSystemTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 3, 1))
clavisterSystemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 5089, 3, 2))
mibBuilder.exportSymbols("CLAVISTER-SMI", clavisterSmiMibModule=clavisterSmiMibModule, clavisterMibModules=clavisterMibModules, clavisterSystemStats=clavisterSystemStats, clavisterOS=clavisterOS, PYSNMP_MODULE_ID=clavisterSmiMibModule, clavisterOSTrap=clavisterOSTrap, clavisterMibObjectGroups=clavisterMibObjectGroups, clavisterSystem=clavisterSystem, clavisterReg=clavisterReg, clavisterOSStats=clavisterOSStats, clavisterSystemTrap=clavisterSystemTrap, clavisterSystemTrapInfo=clavisterSystemTrapInfo, clavisterOSTrapInfo=clavisterOSTrapInfo, clavisterMibConfs=clavisterMibConfs, clavister=clavister)
