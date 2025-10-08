#
# PySNMP MIB module STONESOFT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/forcepoint/STONESOFT-SMI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("STONESOFT-SMI-MIB", stonesoftIDS=stonesoftIDS, stonesoftCluster=stonesoftCluster, stonesoftLoadBalancer=stonesoftLoadBalancer, stonesoftExperimental=stonesoftExperimental, stonesoft=stonesoft, stonesoftNetworkNode=stonesoftNetworkNode, stonesoftGeneric=stonesoftGeneric, stonesoftModules=stonesoftModules, PYSNMP_MODULE_ID=stonesoftSmiMibModule, stonesoftSmiMibModule=stonesoftSmiMibModule, stonesoftVPN=stonesoftVPN, stonesoftProducts=stonesoftProducts, stonesoftFirewall=stonesoftFirewall, stonesoftIPS=stonesoftIPS)
