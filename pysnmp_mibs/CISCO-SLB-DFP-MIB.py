#
# PySNMP MIB module CISCO-SLB-DFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SLB-DFP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSlbDfpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 689))
ciscoSlbDfpMIB.setRevisions(('2009-01-29 00:00',))
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setLastUpdated('200901290000Z')
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setOrganization('Cisco Systems, Inc.')
ciscoSlbDfpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 0))
ciscoSlbDfpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 1))
ciscoSlbDfpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2))
cslbcDfpCongestionThresholdType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reject", 1), ("abort", 2), ("redirect", 3), ("drop", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cslbcDfpCongestionThresholdType.setStatus('current')
cslbcProcessorDfpValTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4), )
if mibBuilder.loadTexts: cslbcProcessorDfpValTable.setStatus('current')
cslbcProcessorDfpValEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1), ).setIndexNames((0, "CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValPhysicalIndex"))
if mibBuilder.loadTexts: cslbcProcessorDfpValEntry.setStatus('current')
cslbcProcessorDfpValPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 1), EntPhysicalIndexOrZero())
if mibBuilder.loadTexts: cslbcProcessorDfpValPhysicalIndex.setStatus('current')
cslbcProcessorDfpValDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslbcProcessorDfpValDescription.setStatus('current')
class CslbcDfpValue(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

cslbcDfpCongestionOnsetThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 1), CslbcDfpValue()).setUnits('DFP weight').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslbcDfpCongestionOnsetThreshold.setStatus('current')
cslbcDfpCongestionAbateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 2), CslbcDfpValue()).setUnits('DFP weight').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslbcDfpCongestionAbateThreshold.setStatus('current')
cslbcProcessorDfpValDfpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 3), CslbcDfpValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslbcProcessorDfpValDfpValue.setStatus('current')
cslbcSlbDfpCongestionOnset = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 1)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"))
if mibBuilder.loadTexts: cslbcSlbDfpCongestionOnset.setStatus('current')
cslbcSlbDfpCongestionAbate = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 2)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
if mibBuilder.loadTexts: cslbcSlbDfpCongestionAbate.setStatus('current')
ciscoSlbDfpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1))
ciscoSlbDfpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2))
ciscoSlbDfpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1, 1)).setObjects(("CISCO-SLB-DFP-MIB", "ciscoSlbDfpInstanceGroup"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpScalarsGroup"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbDfpMIBCompliance = ciscoSlbDfpMIBCompliance.setStatus('current')
ciscoSlbDfpInstanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 1)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbDfpInstanceGroup = ciscoSlbDfpInstanceGroup.setStatus('current')
cslbcSlbDfpScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 2)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cslbcSlbDfpScalarsGroup = cslbcSlbDfpScalarsGroup.setStatus('current')
cslbcSlbDfpCongestionGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 3)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionOnset"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionAbate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cslbcSlbDfpCongestionGroup = cslbcSlbDfpCongestionGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SLB-DFP-MIB", cslbcSlbDfpCongestionAbate=cslbcSlbDfpCongestionAbate, ciscoSlbDfpMIBObjects=ciscoSlbDfpMIBObjects, cslbcDfpCongestionThresholdType=cslbcDfpCongestionThresholdType, cslbcProcessorDfpValEntry=cslbcProcessorDfpValEntry, ciscoSlbDfpMIBCompliance=ciscoSlbDfpMIBCompliance, ciscoSlbDfpMIBConform=ciscoSlbDfpMIBConform, CslbcDfpValue=CslbcDfpValue, cslbcProcessorDfpValDfpValue=cslbcProcessorDfpValDfpValue, ciscoSlbDfpMIBGroups=ciscoSlbDfpMIBGroups, cslbcDfpCongestionAbateThreshold=cslbcDfpCongestionAbateThreshold, cslbcProcessorDfpValPhysicalIndex=cslbcProcessorDfpValPhysicalIndex, ciscoSlbDfpMIB=ciscoSlbDfpMIB, ciscoSlbDfpInstanceGroup=ciscoSlbDfpInstanceGroup, cslbcSlbDfpScalarsGroup=cslbcSlbDfpScalarsGroup, PYSNMP_MODULE_ID=ciscoSlbDfpMIB, ciscoSlbDfpMIBCompliances=ciscoSlbDfpMIBCompliances, cslbcDfpCongestionOnsetThreshold=cslbcDfpCongestionOnsetThreshold, cslbcSlbDfpCongestionOnset=cslbcSlbDfpCongestionOnset, cslbcProcessorDfpValDescription=cslbcProcessorDfpValDescription, ciscoSlbDfpMIBNotifs=ciscoSlbDfpMIBNotifs, cslbcProcessorDfpValTable=cslbcProcessorDfpValTable, cslbcSlbDfpCongestionGroup=cslbcSlbDfpCongestionGroup)
