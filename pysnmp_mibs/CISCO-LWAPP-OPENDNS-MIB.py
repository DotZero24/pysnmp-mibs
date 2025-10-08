#
# PySNMP MIB module CISCO-LWAPP-OPENDNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-LWAPP-OPENDNS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-LWAPP-OPENDNS-MIB", claOpendnsProfileRowStatus=claOpendnsProfileRowStatus, claOpendnsWlanTable=claOpendnsWlanTable, claOpendnsWlanDhcpOpt6=claOpendnsWlanDhcpOpt6, ciscoLwappOpendnsMIBComplianceRev1=ciscoLwappOpendnsMIBComplianceRev1, ciscoLwappOpendnsMIBConform=ciscoLwappOpendnsMIBConform, ciscoLwappOpendnsMIBGroups=ciscoLwappOpendnsMIBGroups, ciscoLwappOpendnsTagGroupVer2=ciscoLwappOpendnsTagGroupVer2, ciscoLwappOpendnsConfig=ciscoLwappOpendnsConfig, ciscoLwappOpendnsMIBObjects=ciscoLwappOpendnsMIBObjects, claOpendnsWlanEntry=claOpendnsWlanEntry, claOpendnsWlanProfileStatus=claOpendnsWlanProfileStatus, ciscoLwappOpendnsConfigGroup=ciscoLwappOpendnsConfigGroup, claOpendnsApiToken=claOpendnsApiToken, ciscoLwappOpendnsMIBNotifs=ciscoLwappOpendnsMIBNotifs, claOpendnsProfileEntry=claOpendnsProfileEntry, claOpendnsProfileIdentity=claOpendnsProfileIdentity, ciscoLwappOpendnsTagGroup=ciscoLwappOpendnsTagGroup, claOpendnsWlanMode=claOpendnsWlanMode, claOpendnsWlanProfileName=claOpendnsWlanProfileName, PYSNMP_MODULE_ID=ciscoLwappOpendnsMIB, claOpendnsProfileStatus=claOpendnsProfileStatus, claOpendnsProfileTable=claOpendnsProfileTable, ciscoLwappOpendnsMIBCompliances=ciscoLwappOpendnsMIBCompliances, ciscoLwappOpendnsMIBCompliance=ciscoLwappOpendnsMIBCompliance, ciscoLwappOpendnsMIBComplianceRev2=ciscoLwappOpendnsMIBComplianceRev2, ciscoLwappOpendnsTag=ciscoLwappOpendnsTag, claOpendnsProfileName=claOpendnsProfileName, ciscoLwappOpendnsMIB=ciscoLwappOpendnsMIB, claOpendnsEnable=claOpendnsEnable, claOpendnsForceEnable=claOpendnsForceEnable)
