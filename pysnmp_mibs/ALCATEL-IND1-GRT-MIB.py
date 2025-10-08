#
# PySNMP MIB module ALCATEL-IND1-GRT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alcatel/ALCATEL-IND1-GRT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
routingIND1GlobalRouteTableMIB, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1GlobalRouteTableMIB")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alcatelIND1GRTMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1))
alcatelIND1GRTMIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1GRTMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1GRTMIB.setOrganization('Alcatel-Lucent')
alcatelIND1GRTMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2))
alaGrtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1))
class AlaGrtRouteDistinguisher(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

alaGrtRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1), )
if mibBuilder.loadTexts: alaGrtRouteTable.setStatus('current')
alaGrtRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-GRT-MIB", "alaGrtRouteDistinguisher"), (0, "ALCATEL-IND1-GRT-MIB", "alaGrtRouteDest"), (0, "ALCATEL-IND1-GRT-MIB", "alaGrtRouteMaskLen"), (0, "ALCATEL-IND1-GRT-MIB", "alaGrtRouteNextHop"))
if mibBuilder.loadTexts: alaGrtRouteEntry.setStatus('current')
alaGrtRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 1), AlaGrtRouteDistinguisher())
if mibBuilder.loadTexts: alaGrtRouteDistinguisher.setStatus('current')
alaGrtRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: alaGrtRouteDest.setStatus('current')
alaGrtRouteDestType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 3), InetAddressType())
if mibBuilder.loadTexts: alaGrtRouteDestType.setStatus('current')
alaGrtRouteMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)))
if mibBuilder.loadTexts: alaGrtRouteMaskLen.setStatus('current')
alaGrtRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 5), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: alaGrtRouteNextHop.setStatus('current')
alaGrtRouteNextHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 6), InetAddressType())
if mibBuilder.loadTexts: alaGrtRouteNextHopType.setStatus('current')
alaGrtRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteMetric.setStatus('current')
alaGrtRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteTag.setStatus('current')
alaGrtRouteVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 2, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteVrfName.setStatus('current')
alcatelIND1GRTMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1))
alcatelIND1GRTMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1, 1))
alcatelIND1GRTMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1, 2))
alaGlobalRouteTableCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1, 1, 1)).setObjects(("ALCATEL-IND1-GRT-MIB", "alaGlobalRouteTableMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaGlobalRouteTableCompliance = alaGlobalRouteTableCompliance.setStatus('current')
alaGlobalRouteTableMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 16, 1, 1, 2, 1)).setObjects(("ALCATEL-IND1-GRT-MIB", "alaGrtRouteVrfName"), ("ALCATEL-IND1-GRT-MIB", "alaGrtRouteMetric"), ("ALCATEL-IND1-GRT-MIB", "alaGrtRouteTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaGlobalRouteTableMIBGroup = alaGlobalRouteTableMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-GRT-MIB", alaGrtRouteNextHopType=alaGrtRouteNextHopType, alcatelIND1GRTMIBGroups=alcatelIND1GRTMIBGroups, alaGrtRouteDistinguisher=alaGrtRouteDistinguisher, alaGlobalRouteTableMIBGroup=alaGlobalRouteTableMIBGroup, alaGrtRouteNextHop=alaGrtRouteNextHop, PYSNMP_MODULE_ID=alcatelIND1GRTMIB, AlaGrtRouteDistinguisher=AlaGrtRouteDistinguisher, alaGrtRouteDestType=alaGrtRouteDestType, alaGrtConfig=alaGrtConfig, alaGrtRouteTable=alaGrtRouteTable, alaGrtRouteTag=alaGrtRouteTag, alcatelIND1GRTMIBConformance=alcatelIND1GRTMIBConformance, alcatelIND1GRTMIB=alcatelIND1GRTMIB, alaGrtRouteMaskLen=alaGrtRouteMaskLen, alaGrtRouteVrfName=alaGrtRouteVrfName, alaGlobalRouteTableCompliance=alaGlobalRouteTableCompliance, alcatelIND1GRTMIBObjects=alcatelIND1GRTMIBObjects, alaGrtRouteEntry=alaGrtRouteEntry, alaGrtRouteDest=alaGrtRouteDest, alaGrtRouteMetric=alaGrtRouteMetric, alcatelIND1GRTMIBCompliances=alcatelIND1GRTMIBCompliances)
