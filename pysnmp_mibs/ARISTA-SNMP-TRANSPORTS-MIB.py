#
# PySNMP MIB module ARISTA-SNMP-TRANSPORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-SNMP-TRANSPORTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TAddress, DisplayString, TextualConvention, TDomain = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "DisplayString", "TextualConvention", "TDomain")
aristaSnmpTransportMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10))
aristaSnmpTransportMIB.setRevisions(('2014-08-15 00:00', '2012-01-09 13:00', '2012-01-05 18:30',))
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setOrganization('Arista Networks, Inc.')
class TransportAddressIPv4NS(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d:2d@*1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 255)

class TransportAddressIPv6NS(TextualConvention, OctetString):
    status = 'current'
    displayHint = '0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d@*1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(19, 255)

aristaUDPNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 1))
if mibBuilder.loadTexts: aristaUDPNSDomain.setStatus('current')
aristaTCPNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 2))
if mibBuilder.loadTexts: aristaTCPNSDomain.setStatus('current')
aristaUDPNS6Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 3))
if mibBuilder.loadTexts: aristaUDPNS6Domain.setStatus('current')
aristaTCPNS6Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 4))
if mibBuilder.loadTexts: aristaTCPNS6Domain.setStatus('current')
aristaAuthFailTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5))
aristaTransportConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6))
aristaAuthFailTrapTDomain = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 1), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaAuthFailTrapTDomain.setStatus('current')
aristaAuthFailTrapSrcTAddress = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaAuthFailTrapSrcTAddress.setStatus('current')
aristaAuthFailTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1))
aristaAuthFailCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2))
aristaAuthFailCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2, 1)).setObjects(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaAuthFailCompliance = aristaAuthFailCompliance.setStatus('current')
aristaAuthFailTrapObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1, 1)).setObjects(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapTDomain"), ("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapSrcTAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaAuthFailTrapObjectsGroup = aristaAuthFailTrapObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", aristaAuthFailCompliance=aristaAuthFailCompliance, TransportAddressIPv6NS=TransportAddressIPv6NS, aristaAuthFailTrapObjects=aristaAuthFailTrapObjects, aristaAuthFailCompliances=aristaAuthFailCompliances, aristaTCPNSDomain=aristaTCPNSDomain, aristaAuthFailTrapGroups=aristaAuthFailTrapGroups, aristaAuthFailTrapObjectsGroup=aristaAuthFailTrapObjectsGroup, aristaSnmpTransportMIB=aristaSnmpTransportMIB, TransportAddressIPv4NS=TransportAddressIPv4NS, aristaUDPNS6Domain=aristaUDPNS6Domain, aristaTCPNS6Domain=aristaTCPNS6Domain, aristaTransportConformance=aristaTransportConformance, aristaAuthFailTrapTDomain=aristaAuthFailTrapTDomain, aristaAuthFailTrapSrcTAddress=aristaAuthFailTrapSrcTAddress, PYSNMP_MODULE_ID=aristaSnmpTransportMIB, aristaUDPNSDomain=aristaUDPNSDomain)
