#
# PySNMP MIB module CISCO-LPTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-LPTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLptsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 812))
ciscoLptsMIB.setRevisions(('2013-09-03 00:00',))
if mibBuilder.loadTexts: ciscoLptsMIB.setLastUpdated('201309030000Z')
if mibBuilder.loadTexts: ciscoLptsMIB.setOrganization('Cisco Systems, Inc.')
class ClFlowType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("static", 1), ("global", 2), ("local", 3))

ciscoLptsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 0))
ciscoLptsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 1))
ciscoLptsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2))
clGlobalFlowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1), )
if mibBuilder.loadTexts: clGlobalFlowTable.setStatus('current')
clGlobalFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1), ).setIndexNames((0, "CISCO-LPTS-MIB", "clGlobalFlowIndex"))
if mibBuilder.loadTexts: clGlobalFlowEntry.setStatus('current')
clGlobalFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: clGlobalFlowIndex.setStatus('current')
clGlobalFlowType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clGlobalFlowType.setStatus('current')
clGlobalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 3), ClFlowType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clGlobalType.setStatus('current')
clGlobalCurrentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 4), Unsigned32()).setUnits('PPS').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clGlobalCurrentRate.setStatus('current')
clLocalFlowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2), )
if mibBuilder.loadTexts: clLocalFlowTable.setStatus('current')
clLocalFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1), ).setIndexNames((0, "CISCO-LPTS-MIB", "clGlobalFlowIndex"), (0, "CISCO-LPTS-MIB", "clLocalNodeID"))
if mibBuilder.loadTexts: clLocalFlowEntry.setStatus('current')
clLocalNodeID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: clLocalNodeID.setStatus('current')
clLocalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 2), ClFlowType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalType.setStatus('current')
clLocalCurrentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 3), Unsigned32()).setUnits('PPS').setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalCurrentRate.setStatus('current')
clLocalAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalAccepted.setStatus('current')
clLocalDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalDropped.setStatus('current')
clLocalTosValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalTosValue.setStatus('current')
ciscoLptsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 1))
ciscoLptsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2))
ciscoLptsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 1, 1)).setObjects(("CISCO-LPTS-MIB", "clLocalFlowGroup"), ("CISCO-LPTS-MIB", "clGlobalFlowGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLptsMIBCompliance = ciscoLptsMIBCompliance.setStatus('current')
clGlobalFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2, 1)).setObjects(("CISCO-LPTS-MIB", "clGlobalFlowType"), ("CISCO-LPTS-MIB", "clGlobalCurrentRate"), ("CISCO-LPTS-MIB", "clGlobalType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clGlobalFlowGroup = clGlobalFlowGroup.setStatus('current')
clLocalFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2, 2)).setObjects(("CISCO-LPTS-MIB", "clLocalCurrentRate"), ("CISCO-LPTS-MIB", "clLocalAccepted"), ("CISCO-LPTS-MIB", "clLocalDropped"), ("CISCO-LPTS-MIB", "clLocalType"), ("CISCO-LPTS-MIB", "clLocalTosValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clLocalFlowGroup = clLocalFlowGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LPTS-MIB", ciscoLptsMIB=ciscoLptsMIB, clLocalAccepted=clLocalAccepted, ciscoLptsMIBObjects=ciscoLptsMIBObjects, clGlobalFlowEntry=clGlobalFlowEntry, clLocalNodeID=clLocalNodeID, clGlobalType=clGlobalType, ciscoLptsMIBNotifs=ciscoLptsMIBNotifs, ClFlowType=ClFlowType, clGlobalFlowGroup=clGlobalFlowGroup, clGlobalFlowIndex=clGlobalFlowIndex, clLocalFlowTable=clLocalFlowTable, clLocalTosValue=clLocalTosValue, clLocalFlowGroup=clLocalFlowGroup, ciscoLptsMIBCompliances=ciscoLptsMIBCompliances, ciscoLptsMIBCompliance=ciscoLptsMIBCompliance, clLocalType=clLocalType, ciscoLptsMIBGroups=ciscoLptsMIBGroups, PYSNMP_MODULE_ID=ciscoLptsMIB, clGlobalFlowTable=clGlobalFlowTable, ciscoLptsMIBConform=ciscoLptsMIBConform, clGlobalCurrentRate=clGlobalCurrentRate, clLocalDropped=clLocalDropped, clLocalCurrentRate=clLocalCurrentRate, clGlobalFlowType=clGlobalFlowType, clLocalFlowEntry=clLocalFlowEntry)
