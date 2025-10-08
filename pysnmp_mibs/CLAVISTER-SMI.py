#
# PySNMP MIB module CLAVISTER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/clavister/CLAVISTER-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 11:09:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CLAVISTER-SMI", clavisterMibObjectGroups=clavisterMibObjectGroups, clavisterSmiMibModule=clavisterSmiMibModule, clavisterMibConfs=clavisterMibConfs, clavisterSystemStats=clavisterSystemStats, PYSNMP_MODULE_ID=clavisterSmiMibModule, clavisterMibModules=clavisterMibModules, clavisterSystemTrapInfo=clavisterSystemTrapInfo, clavisterOSTrapInfo=clavisterOSTrapInfo, clavisterSystemTrap=clavisterSystemTrap, clavister=clavister, clavisterSystem=clavisterSystem, clavisterOSStats=clavisterOSStats, clavisterOSTrap=clavisterOSTrap, clavisterOS=clavisterOS, clavisterReg=clavisterReg)
