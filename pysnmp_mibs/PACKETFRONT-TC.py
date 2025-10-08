#
# PySNMP MIB module PACKETFRONT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/packetfront/PACKETFRONT-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pfModules, = mibBuilder.importSymbols("PACKETFRONT-SMI", "pfModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pfTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 5, 1))
pfTextualConventions.setRevisions(('2009-03-23 10:40', '2008-05-01 08:39', '2007-05-18 00:00',))
if mibBuilder.loadTexts: pfTextualConventions.setLastUpdated('200903231040Z')
if mibBuilder.loadTexts: pfTextualConventions.setOrganization('PacketFront Systems AB')
class PortList(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("PACKETFRONT-TC", PYSNMP_MODULE_ID=pfTextualConventions, PortList=PortList, pfTextualConventions=pfTextualConventions)
