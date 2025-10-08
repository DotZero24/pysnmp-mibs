#
# PySNMP MIB module STONESOFT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/forcepoint/STONESOFT-SMI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stonesoftSmiMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 1369, 3, 2))
stonesoftSmiMibModule.setRevisions(('2004-06-16 00:00',))
if mibBuilder.loadTexts: stonesoftSmiMibModule.setLastUpdated('200406160000Z')
if mibBuilder.loadTexts: stonesoftSmiMibModule.setOrganization('Stonesoft Corp')
stonesoft = MibIdentifier((1, 3, 6, 1, 4, 1, 1369))
stonesoftModules = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 3))
stonesoftExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 4))
stonesoftProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5))
stonesoftGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 6))
stonesoftLoadBalancer = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 1))
stonesoftFirewall = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 2))
stonesoftVPN = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 3))
stonesoftIDS = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 4))
stonesoftIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 5, 5))
stonesoftNetworkNode = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 6, 1))
stonesoftCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 6, 2))
mibBuilder.exportSymbols("STONESOFT-SMI-MIB", PYSNMP_MODULE_ID=stonesoftSmiMibModule, stonesoftIDS=stonesoftIDS, stonesoftExperimental=stonesoftExperimental, stonesoftFirewall=stonesoftFirewall, stonesoftVPN=stonesoftVPN, stonesoftSmiMibModule=stonesoftSmiMibModule, stonesoftProducts=stonesoftProducts, stonesoft=stonesoft, stonesoftIPS=stonesoftIPS, stonesoftGeneric=stonesoftGeneric, stonesoftCluster=stonesoftCluster, stonesoftNetworkNode=stonesoftNetworkNode, stonesoftModules=stonesoftModules, stonesoftLoadBalancer=stonesoftLoadBalancer)
