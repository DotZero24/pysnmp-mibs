#
# PySNMP MIB module ARISTA-SNMP-TRANSPORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/arista/ARISTA-SNMP-TRANSPORTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TDomain, TAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "TAddress", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", aristaTransportConformance=aristaTransportConformance, aristaTCPNSDomain=aristaTCPNSDomain, aristaAuthFailTrapObjects=aristaAuthFailTrapObjects, aristaAuthFailTrapTDomain=aristaAuthFailTrapTDomain, aristaAuthFailTrapSrcTAddress=aristaAuthFailTrapSrcTAddress, aristaSnmpTransportMIB=aristaSnmpTransportMIB, TransportAddressIPv4NS=TransportAddressIPv4NS, aristaAuthFailCompliances=aristaAuthFailCompliances, aristaAuthFailCompliance=aristaAuthFailCompliance, aristaTCPNS6Domain=aristaTCPNS6Domain, aristaAuthFailTrapGroups=aristaAuthFailTrapGroups, aristaAuthFailTrapObjectsGroup=aristaAuthFailTrapObjectsGroup, aristaUDPNS6Domain=aristaUDPNS6Domain, TransportAddressIPv6NS=TransportAddressIPv6NS, aristaUDPNSDomain=aristaUDPNSDomain, PYSNMP_MODULE_ID=aristaSnmpTransportMIB)
