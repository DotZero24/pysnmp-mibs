#
# PySNMP MIB module PACKETFRONT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/packetfront/PACKETFRONT-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pfModules, = mibBuilder.importSymbols("PACKETFRONT-SMI", "pfModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pfTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 5, 1))
pfTextualConventions.setRevisions(('2009-03-23 10:40', '2008-05-01 08:39', '2007-05-18 00:00',))
if mibBuilder.loadTexts: pfTextualConventions.setLastUpdated('200903231040Z')
if mibBuilder.loadTexts: pfTextualConventions.setOrganization('PacketFront Systems AB')
class PortList(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("PACKETFRONT-TC", PortList=PortList, pfTextualConventions=pfTextualConventions, PYSNMP_MODULE_ID=pfTextualConventions)
