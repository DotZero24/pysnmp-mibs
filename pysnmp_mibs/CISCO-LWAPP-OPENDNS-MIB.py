#
# PySNMP MIB module CISCO-LWAPP-OPENDNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-LWAPP-OPENDNS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
ciscoLwappOpendnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 837))
ciscoLwappOpendnsMIB.setRevisions(('2018-07-03 00:00', '2017-02-10 00:00',))
if mibBuilder.loadTexts: ciscoLwappOpendnsMIB.setLastUpdated('201807030000Z')
if mibBuilder.loadTexts: ciscoLwappOpendnsMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappOpendnsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 0))
ciscoLwappOpendnsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 1))
ciscoLwappOpendnsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 2))
ciscoLwappOpendnsTag = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1))
ciscoLwappOpendnsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2))
claOpendnsEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsEnable.setStatus('current')
claOpendnsForceEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsForceEnable.setStatus('current')
claOpendnsApiToken = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsApiToken.setStatus('current')
claOpendnsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1), )
if mibBuilder.loadTexts: claOpendnsProfileTable.setStatus('current')
claOpendnsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileName"))
if mibBuilder.loadTexts: claOpendnsProfileEntry.setStatus('current')
claOpendnsProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: claOpendnsProfileName.setStatus('current')
claOpendnsProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claOpendnsProfileRowStatus.setStatus('current')
claOpendnsProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notInuse", 1), ("inProgress", 2), ("success", 3), ("failed", 4), ("inuse", 5))).clone('notInuse')).setMaxAccess("readonly")
if mibBuilder.loadTexts: claOpendnsProfileStatus.setStatus('current')
claOpendnsProfileIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: claOpendnsProfileIdentity.setStatus('current')
claOpendnsWlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2), )
if mibBuilder.loadTexts: claOpendnsWlanTable.setStatus('current')
claOpendnsWlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: claOpendnsWlanEntry.setStatus('current')
claOpendnsWlanProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsWlanProfileName.setStatus('current')
claOpendnsWlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("force", 2), ("copy", 3))).clone('force')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsWlanMode.setStatus('current')
claOpendnsWlanProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsWlanProfileStatus.setStatus('current')
claOpendnsWlanDhcpOpt6 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsWlanDhcpOpt6.setStatus('current')
ciscoLwappOpendnsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1))
ciscoLwappOpendnsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2))
ciscoLwappOpendnsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 1)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsMIBCompliance = ciscoLwappOpendnsMIBCompliance.setStatus('deprecated')
ciscoLwappOpendnsMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 2)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup"), ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsMIBComplianceRev1 = ciscoLwappOpendnsMIBComplianceRev1.setStatus('deprecated')
ciscoLwappOpendnsMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 3)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup"), ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsConfigGroup"), ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroupVer2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsMIBComplianceRev2 = ciscoLwappOpendnsMIBComplianceRev2.setStatus('current')
ciscoLwappOpendnsTagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 1)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileRowStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileName"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanMode"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileIdentity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsTagGroup = ciscoLwappOpendnsTagGroup.setStatus('deprecated')
ciscoLwappOpendnsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 2)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsEnable"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsForceEnable"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsApiToken"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsConfigGroup = ciscoLwappOpendnsConfigGroup.setStatus('current')
ciscoLwappOpendnsTagGroupVer2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 3)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileRowStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileName"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanMode"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileIdentity"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanDhcpOpt6"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsTagGroupVer2 = ciscoLwappOpendnsTagGroupVer2.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-OPENDNS-MIB", claOpendnsForceEnable=claOpendnsForceEnable, claOpendnsEnable=claOpendnsEnable, ciscoLwappOpendnsTagGroup=ciscoLwappOpendnsTagGroup, claOpendnsWlanTable=claOpendnsWlanTable, claOpendnsProfileStatus=claOpendnsProfileStatus, claOpendnsProfileIdentity=claOpendnsProfileIdentity, claOpendnsProfileEntry=claOpendnsProfileEntry, claOpendnsApiToken=claOpendnsApiToken, ciscoLwappOpendnsMIBNotifs=ciscoLwappOpendnsMIBNotifs, ciscoLwappOpendnsTag=ciscoLwappOpendnsTag, ciscoLwappOpendnsMIBCompliance=ciscoLwappOpendnsMIBCompliance, ciscoLwappOpendnsMIBComplianceRev1=ciscoLwappOpendnsMIBComplianceRev1, claOpendnsProfileName=claOpendnsProfileName, ciscoLwappOpendnsMIBCompliances=ciscoLwappOpendnsMIBCompliances, ciscoLwappOpendnsMIBComplianceRev2=ciscoLwappOpendnsMIBComplianceRev2, PYSNMP_MODULE_ID=ciscoLwappOpendnsMIB, claOpendnsWlanProfileName=claOpendnsWlanProfileName, ciscoLwappOpendnsMIBObjects=ciscoLwappOpendnsMIBObjects, claOpendnsWlanMode=claOpendnsWlanMode, ciscoLwappOpendnsMIBGroups=ciscoLwappOpendnsMIBGroups, ciscoLwappOpendnsConfig=ciscoLwappOpendnsConfig, ciscoLwappOpendnsMIBConform=ciscoLwappOpendnsMIBConform, claOpendnsWlanEntry=claOpendnsWlanEntry, claOpendnsProfileTable=claOpendnsProfileTable, ciscoLwappOpendnsConfigGroup=ciscoLwappOpendnsConfigGroup, claOpendnsWlanProfileStatus=claOpendnsWlanProfileStatus, claOpendnsWlanDhcpOpt6=claOpendnsWlanDhcpOpt6, ciscoLwappOpendnsTagGroupVer2=ciscoLwappOpendnsTagGroupVer2, ciscoLwappOpendnsMIB=ciscoLwappOpendnsMIB, claOpendnsProfileRowStatus=claOpendnsProfileRowStatus)
