#
# PySNMP MIB module RDN-PORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/riverdelta/RDN-PORTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RDN-PORTS-MIB", rdnPortsCableUpstream=rdnPortsCableUpstream, rdnPortsNull=rdnPortsNull, PYSNMP_MODULE_ID=rdnPorts, rdnPortsLoopback=rdnPortsLoopback, rdnPortsUnknown=rdnPortsUnknown, rdnPortsCableDownstream=rdnPortsCableDownstream, rdnPortsCableSubIf=rdnPortsCableSubIf, rdnPortsEthernet=rdnPortsEthernet, rdnPortsCableMac=rdnPortsCableMac, rdnPortsGige=rdnPortsGige, rdnPortsATM=rdnPortsATM, rdnPortsT1=rdnPortsT1, rdnPorts=rdnPorts, rdnPortsPOS=rdnPortsPOS, rdnPortsTunnel=rdnPortsTunnel)
