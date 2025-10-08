#
# PySNMP MIB module ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
etsysRadiusDynAuthorServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80))
etsysRadiusDynAuthorServerMIB.setRevisions(('2016-05-18 14:06', '2011-12-19 13:24',))
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerMIB.setLastUpdated('201605181406Z')
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerMIB.setOrganization('Extreme Networks')
etsysRadiusDynAuthorServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1))
etsysRadiusDynAuthorServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerEnable.setStatus('current')
etsysRadiusDynAuthorServerClientTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2), )
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerClientTable.setStatus('current')
etsysRadiusDynAuthorServerClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1), ).setIndexNames((0, "ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientIndex"))
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerClientEntry.setStatus('current')
etsysRadiusDynAuthorServerClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerClientIndex.setStatus('current')
etsysRadiusDynAuthorServerClientAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerClientAddressType.setStatus('current')
etsysRadiusDynAuthorServerClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerClientAddress.setStatus('current')
etsysRadiusDynAuthorServerClientSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerClientSecret.setStatus('current')
etsysRadiusDynAuthorServerClientSecretEntered = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerClientSecretEntered.setStatus('current')
etsysRadiusDynAuthorServerClientStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusDynAuthorServerClientStatus.setStatus('current')
etsysRadiusDynAuthorClientServerClientAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 7), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusDynAuthorClientServerClientAddressType.setStatus('current')
etsysRadiusDynAuthorClientServerClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 8), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusDynAuthorClientServerClientAddress.setStatus('current')
etsysRadiusDynAuthorClientServerClientVirtualRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 1, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusDynAuthorClientServerClientVirtualRouterName.setStatus('current')
etsysRadiusDynAuthorServerMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2))
etsysRadiusDynAuthorServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 1))
etsysRadiusDynAuthorServerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 2))
etsysRadiusDynAuthorServerMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 2, 1)).setObjects(("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerEnable"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientAddressType"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientAddress"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientSecret"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientSecretEntered"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusDynAuthorServerMIBGroup = etsysRadiusDynAuthorServerMIBGroup.setStatus('deprecated')
etsysRadiusDynAuthorServerMIBGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 2, 2)).setObjects(("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerEnable"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientAddressType"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientAddress"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientSecret"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientSecretEntered"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerClientStatus"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorClientServerClientAddressType"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorClientServerClientAddress"), ("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorClientServerClientVirtualRouterName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusDynAuthorServerMIBGroup2 = etsysRadiusDynAuthorServerMIBGroup2.setStatus('current')
etsysRadiusDynAuthorServerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 1, 1)).setObjects(("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusDynAuthorServerMIBCompliance = etsysRadiusDynAuthorServerMIBCompliance.setStatus('deprecated')
etsysRadiusDynAuthorServerMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 80, 2, 1, 2)).setObjects(("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", "etsysRadiusDynAuthorServerMIBGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusDynAuthorServerMIBCompliance2 = etsysRadiusDynAuthorServerMIBCompliance2.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-RADIUS-DYNAMIC-AUTHOR-SERVER-EXT-MIB", etsysRadiusDynAuthorServerClientSecret=etsysRadiusDynAuthorServerClientSecret, etsysRadiusDynAuthorServerMIBObjects=etsysRadiusDynAuthorServerMIBObjects, etsysRadiusDynAuthorServerMIBGroup=etsysRadiusDynAuthorServerMIBGroup, etsysRadiusDynAuthorServerClientSecretEntered=etsysRadiusDynAuthorServerClientSecretEntered, etsysRadiusDynAuthorClientServerClientAddressType=etsysRadiusDynAuthorClientServerClientAddressType, etsysRadiusDynAuthorServerClientAddressType=etsysRadiusDynAuthorServerClientAddressType, etsysRadiusDynAuthorClientServerClientAddress=etsysRadiusDynAuthorClientServerClientAddress, etsysRadiusDynAuthorServerEnable=etsysRadiusDynAuthorServerEnable, etsysRadiusDynAuthorServerMIBCompliances=etsysRadiusDynAuthorServerMIBCompliances, etsysRadiusDynAuthorServerClientTable=etsysRadiusDynAuthorServerClientTable, etsysRadiusDynAuthorServerClientAddress=etsysRadiusDynAuthorServerClientAddress, etsysRadiusDynAuthorServerMIBGroup2=etsysRadiusDynAuthorServerMIBGroup2, etsysRadiusDynAuthorServerMIBGroups=etsysRadiusDynAuthorServerMIBGroups, etsysRadiusDynAuthorServerMIBConformance=etsysRadiusDynAuthorServerMIBConformance, etsysRadiusDynAuthorClientServerClientVirtualRouterName=etsysRadiusDynAuthorClientServerClientVirtualRouterName, PYSNMP_MODULE_ID=etsysRadiusDynAuthorServerMIB, etsysRadiusDynAuthorServerMIB=etsysRadiusDynAuthorServerMIB, etsysRadiusDynAuthorServerClientEntry=etsysRadiusDynAuthorServerClientEntry, etsysRadiusDynAuthorServerMIBCompliance2=etsysRadiusDynAuthorServerMIBCompliance2, etsysRadiusDynAuthorServerMIBCompliance=etsysRadiusDynAuthorServerMIBCompliance, etsysRadiusDynAuthorServerClientStatus=etsysRadiusDynAuthorServerClientStatus, etsysRadiusDynAuthorServerClientIndex=etsysRadiusDynAuthorServerClientIndex)
