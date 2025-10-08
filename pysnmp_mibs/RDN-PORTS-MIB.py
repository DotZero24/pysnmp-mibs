#
# PySNMP MIB module RDN-PORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/riverdelta/RDN-PORTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnPorts = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 5))
rdnPorts.setRevisions(('2008-08-08 00:00', '2005-10-20 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-05-08 00:00',))
if mibBuilder.loadTexts: rdnPorts.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnPorts.setOrganization('Motorola')
rdnPortsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 0))
rdnPortsGige = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 1))
rdnPortsEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 2))
rdnPortsCableMac = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 3))
rdnPortsCableUpstream = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 4))
rdnPortsCableDownstream = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 5))
rdnPortsCableSubIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 6))
rdnPortsLoopback = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 7))
rdnPortsT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 8))
rdnPortsNull = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 9))
rdnPortsTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 10))
rdnPortsPOS = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 11))
rdnPortsATM = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 12))
mibBuilder.exportSymbols("RDN-PORTS-MIB", rdnPortsGige=rdnPortsGige, rdnPortsCableDownstream=rdnPortsCableDownstream, rdnPortsTunnel=rdnPortsTunnel, rdnPortsCableSubIf=rdnPortsCableSubIf, rdnPortsATM=rdnPortsATM, rdnPortsCableMac=rdnPortsCableMac, rdnPortsNull=rdnPortsNull, rdnPortsT1=rdnPortsT1, PYSNMP_MODULE_ID=rdnPorts, rdnPortsUnknown=rdnPortsUnknown, rdnPortsLoopback=rdnPortsLoopback, rdnPortsEthernet=rdnPortsEthernet, rdnPortsPOS=rdnPortsPOS, rdnPorts=rdnPorts, rdnPortsCableUpstream=rdnPortsCableUpstream)
