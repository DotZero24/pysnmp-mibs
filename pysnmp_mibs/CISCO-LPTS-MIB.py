#
# PySNMP MIB module CISCO-LPTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-LPTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("CISCO-LPTS-MIB", clGlobalFlowIndex=clGlobalFlowIndex, clGlobalCurrentRate=clGlobalCurrentRate, clLocalCurrentRate=clLocalCurrentRate, PYSNMP_MODULE_ID=ciscoLptsMIB, clLocalFlowEntry=clLocalFlowEntry, ciscoLptsMIBCompliance=ciscoLptsMIBCompliance, clLocalTosValue=clLocalTosValue, clGlobalType=clGlobalType, ciscoLptsMIBNotifs=ciscoLptsMIBNotifs, ciscoLptsMIBGroups=ciscoLptsMIBGroups, ciscoLptsMIBConform=ciscoLptsMIBConform, clGlobalFlowTable=clGlobalFlowTable, clLocalFlowGroup=clLocalFlowGroup, ciscoLptsMIB=ciscoLptsMIB, clLocalType=clLocalType, clLocalNodeID=clLocalNodeID, clLocalAccepted=clLocalAccepted, clLocalFlowTable=clLocalFlowTable, clGlobalFlowType=clGlobalFlowType, ciscoLptsMIBCompliances=ciscoLptsMIBCompliances, clGlobalFlowEntry=clGlobalFlowEntry, clGlobalFlowGroup=clGlobalFlowGroup, ciscoLptsMIBObjects=ciscoLptsMIBObjects, ClFlowType=ClFlowType, clLocalDropped=clLocalDropped)
