#
# PySNMP MIB module CISCO-FC-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-FC-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
DomainIdOrZero, = mibBuilder.importSymbols("CISCO-ST-TC", "DomainIdOrZero")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoFcMulticastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 435))
ciscoFcMulticastMIB.setRevisions(('2004-10-07 00:00',))
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setLastUpdated('200410070000Z')
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setOrganization('Cisco Systems Inc. ')
ciscoFcMulticastNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 0))
ciscoFcMulticastMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 1))
ciscoFcMulticaseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2))
cfmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1))
class CfmMulticastRootMode(TextualConvention, Integer32):
    reference = 'Refer to FC-SW-2 REV 5.4 for information on principal switch and lowest domain id switch.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("principalSwitch", 1), ("lowestDomainSwitch", 2))

cfmMulticastRootTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1), )
if mibBuilder.loadTexts: cfmMulticastRootTable.setStatus('current')
cfmMulticastRootEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: cfmMulticastRootEntry.setStatus('current')
cfmMulticastRootConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 1), CfmMulticastRootMode().clone('principalSwitch')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMulticastRootConfigMode.setStatus('current')
cfmMulticastRootOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 2), CfmMulticastRootMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMulticastRootOperMode.setStatus('current')
cfmMulticastRootDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 3), DomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMulticastRootDomainId.setStatus('current')
cfmMulticastRootRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMulticastRootRowStatus.setStatus('current')
ciscoFcMulticastMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1))
ciscoFcMulticastMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2))
ciscoFcMulticastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1, 1)).setObjects(("CISCO-FC-MULTICAST-MIB", "cfmConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcMulticastMIBCompliance = ciscoFcMulticastMIBCompliance.setStatus('current')
cfmConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2, 1)).setObjects(("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootConfigMode"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootOperMode"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootDomainId"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmConfigurationGroup = cfmConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FC-MULTICAST-MIB", ciscoFcMulticastNotifications=ciscoFcMulticastNotifications, CfmMulticastRootMode=CfmMulticastRootMode, cfmMulticastRootConfigMode=cfmMulticastRootConfigMode, ciscoFcMulticastMIBGroups=ciscoFcMulticastMIBGroups, cfmConfigurationGroup=cfmConfigurationGroup, cfmMulticastRootEntry=cfmMulticastRootEntry, ciscoFcMulticaseConformance=ciscoFcMulticaseConformance, ciscoFcMulticastMIBCompliance=ciscoFcMulticastMIBCompliance, ciscoFcMulticastMIB=ciscoFcMulticastMIB, cfmConfiguration=cfmConfiguration, cfmMulticastRootTable=cfmMulticastRootTable, cfmMulticastRootOperMode=cfmMulticastRootOperMode, cfmMulticastRootDomainId=cfmMulticastRootDomainId, ciscoFcMulticastMIBCompliances=ciscoFcMulticastMIBCompliances, cfmMulticastRootRowStatus=cfmMulticastRootRowStatus, ciscoFcMulticastMIBObjects=ciscoFcMulticastMIBObjects, PYSNMP_MODULE_ID=ciscoFcMulticastMIB)
