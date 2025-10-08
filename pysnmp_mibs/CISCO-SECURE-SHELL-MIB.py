#
# PySNMP MIB module CISCO-SECURE-SHELL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-SECURE-SHELL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:27:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
ciscoSecureShellMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 339))
ciscoSecureShellMIB.setRevisions(('2005-06-01 00:00', '2004-04-05 00:00', '2003-09-18 00:00', '2002-10-05 00:00',))
if mibBuilder.loadTexts: ciscoSecureShellMIB.setLastUpdated('200506010000Z')
if mibBuilder.loadTexts: ciscoSecureShellMIB.setOrganization('Cisco Systems, Inc.')
ciscoSecureShellMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 1))
cssConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1))
cssSessionInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2))
class CssVersions(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("v1", 0), ("v2", 1))

cssServiceActivation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssServiceActivation.setStatus('current')
cssKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2), )
if mibBuilder.loadTexts: cssKeyTable.setStatus('current')
cssKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-SECURE-SHELL-MIB", "cssKeyIndex"))
if mibBuilder.loadTexts: cssKeyEntry.setStatus('current')
cssKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rsa", 1), ("rsa1", 2), ("dsa", 3))))
if mibBuilder.loadTexts: cssKeyIndex.setStatus('current')
cssKeyNBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 2048))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cssKeyNBits.setStatus('current')
cssKeyOverWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cssKeyOverWrite.setStatus('current')
cssKeyLastCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssKeyLastCreationTime.setStatus('current')
cssKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cssKeyRowStatus.setStatus('current')
cssKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssKeyString.setStatus('current')
cssServiceCapability = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 3), CssVersions()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssServiceCapability.setStatus('current')
cssServiceMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 4), CssVersions()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssServiceMode.setStatus('current')
cssKeyGenerationStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inProgress", 1), ("successful", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssKeyGenerationStatus.setStatus('current')
cssSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1), )
if mibBuilder.loadTexts: cssSessionTable.setStatus('current')
cssSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-SECURE-SHELL-MIB", "cssSessionID"))
if mibBuilder.loadTexts: cssSessionEntry.setStatus('current')
cssSessionID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cssSessionID.setStatus('current')
cssSessionVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("one", 1), ("two", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionVersion.setStatus('current')
cssSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("sshSessionVersionOk", 1), ("sshSessionKeysExchanged", 2), ("sshSessionAuthenticated", 3), ("sshSessionOpen", 4), ("sshSessionDisconnecting", 5), ("sshSessionDisconnected", 6), ("sshSessionClosed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionState.setStatus('current')
cssSessionPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionPID.setStatus('current')
cssSessionUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionUserID.setStatus('current')
cssSessionHostAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionHostAddrType.setStatus('current')
cssSessionHostAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionHostAddr.setStatus('current')
ciscoSecureShellMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 2))
ciscoSecureShellMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1))
ciscoSecureShellMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2))
ciscoSecureShellMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 1)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSecureShellMIBCompliance = ciscoSecureShellMIBCompliance.setStatus('deprecated')
ciscoSecureShellMIBComplianceRv1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 2)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSecureShellMIBComplianceRv1 = ciscoSecureShellMIBComplianceRv1.setStatus('deprecated')
ciscoSecureShellMIBComplianceRv2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 3)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSecureShellMIBComplianceRv2 = ciscoSecureShellMIBComplianceRv2.setStatus('deprecated')
ciscoSecureShellMIBComplianceRv3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 4)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroupRev1"), ("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroupSupp1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSecureShellMIBComplianceRv3 = ciscoSecureShellMIBComplianceRv3.setStatus('current')
cssConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 1)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssServiceActivation"), ("CISCO-SECURE-SHELL-MIB", "cssKeyNBits"), ("CISCO-SECURE-SHELL-MIB", "cssKeyOverWrite"), ("CISCO-SECURE-SHELL-MIB", "cssKeyLastCreationTime"), ("CISCO-SECURE-SHELL-MIB", "cssKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssConfigurationGroup = cssConfigurationGroup.setStatus('deprecated')
cssConfigurationGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 2)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssServiceActivation"), ("CISCO-SECURE-SHELL-MIB", "cssKeyNBits"), ("CISCO-SECURE-SHELL-MIB", "cssKeyOverWrite"), ("CISCO-SECURE-SHELL-MIB", "cssKeyLastCreationTime"), ("CISCO-SECURE-SHELL-MIB", "cssKeyString"), ("CISCO-SECURE-SHELL-MIB", "cssKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssConfigurationGroupRev1 = cssConfigurationGroupRev1.setStatus('current')
cssServiceModeCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 3)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssServiceCapability"), ("CISCO-SECURE-SHELL-MIB", "cssServiceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssServiceModeCfgGroup = cssServiceModeCfgGroup.setStatus('current')
cssSessionInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 4)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssSessionVersion"), ("CISCO-SECURE-SHELL-MIB", "cssSessionState"), ("CISCO-SECURE-SHELL-MIB", "cssSessionPID"), ("CISCO-SECURE-SHELL-MIB", "cssSessionUserID"), ("CISCO-SECURE-SHELL-MIB", "cssSessionHostAddrType"), ("CISCO-SECURE-SHELL-MIB", "cssSessionHostAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssSessionInfoGroup = cssSessionInfoGroup.setStatus('current')
cssConfigurationGroupSupp1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 5)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssKeyGenerationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssConfigurationGroupSupp1 = cssConfigurationGroupSupp1.setStatus('current')
mibBuilder.exportSymbols("CISCO-SECURE-SHELL-MIB", cssSessionVersion=cssSessionVersion, cssSessionTable=cssSessionTable, ciscoSecureShellMIBCompliances=ciscoSecureShellMIBCompliances, cssKeyGenerationStatus=cssKeyGenerationStatus, cssKeyTable=cssKeyTable, cssSessionHostAddrType=cssSessionHostAddrType, ciscoSecureShellMIBConformance=ciscoSecureShellMIBConformance, cssSessionPID=cssSessionPID, cssSessionID=cssSessionID, ciscoSecureShellMIBComplianceRv2=ciscoSecureShellMIBComplianceRv2, ciscoSecureShellMIBComplianceRv1=ciscoSecureShellMIBComplianceRv1, cssSessionEntry=cssSessionEntry, cssKeyEntry=cssKeyEntry, cssConfigurationGroupSupp1=cssConfigurationGroupSupp1, CssVersions=CssVersions, cssKeyNBits=cssKeyNBits, ciscoSecureShellMIBCompliance=ciscoSecureShellMIBCompliance, cssServiceCapability=cssServiceCapability, cssServiceActivation=cssServiceActivation, cssSessionState=cssSessionState, PYSNMP_MODULE_ID=ciscoSecureShellMIB, ciscoSecureShellMIBComplianceRv3=ciscoSecureShellMIBComplianceRv3, cssSessionHostAddr=cssSessionHostAddr, cssConfiguration=cssConfiguration, cssKeyIndex=cssKeyIndex, ciscoSecureShellMIBGroups=ciscoSecureShellMIBGroups, cssServiceMode=cssServiceMode, cssServiceModeCfgGroup=cssServiceModeCfgGroup, ciscoSecureShellMIBObjects=ciscoSecureShellMIBObjects, cssConfigurationGroupRev1=cssConfigurationGroupRev1, cssKeyOverWrite=cssKeyOverWrite, cssKeyLastCreationTime=cssKeyLastCreationTime, cssKeyRowStatus=cssKeyRowStatus, cssSessionUserID=cssSessionUserID, cssKeyString=cssKeyString, cssSessionInfoGroup=cssSessionInfoGroup, cssSessionInfo=cssSessionInfo, cssConfigurationGroup=cssConfigurationGroup, ciscoSecureShellMIB=ciscoSecureShellMIB)
