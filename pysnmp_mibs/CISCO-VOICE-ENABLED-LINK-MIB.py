#
# PySNMP MIB module CISCO-VOICE-ENABLED-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-ENABLED-LINK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
ciscoVoiceEnabledLinkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 53))
if mibBuilder.loadTexts: ciscoVoiceEnabledLinkMIB.setLastUpdated('9905070000Z')
if mibBuilder.loadTexts: ciscoVoiceEnabledLinkMIB.setOrganization('Cisco Systems, Inc.')
cvenabledlinkMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 1))
cvEnabledLink = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1))
cvEnabledDefaultMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledDefaultMacAddr.setStatus('current')
cvEnabledLinkTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2), )
if mibBuilder.loadTexts: cvEnabledLinkTable.setStatus('current')
cvEnabledLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkIndex"))
if mibBuilder.loadTexts: cvEnabledLinkEntry.setStatus('current')
cvEnabledLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483648))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkIndex.setStatus('current')
cvEnabledLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("atm", 1), ("framerelay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkType.setStatus('current')
cvEnabledLinkInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkInterfaceName.setStatus('current')
cvEnabledLinkVpiDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkVpiDlci.setStatus('current')
cvEnabledLinkVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkVci.setStatus('current')
cvEnabledLinkRemoteMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkRemoteMacAddr.setStatus('current')
ciscoVoiceEnabledLinkMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 2))
ciscoVoiceEnabledLinkMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 2, 0))
ciscoVoiceEnabledlinkMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 3))
ciscoVoiceEnabledlinkMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 1))
ciscoVoiceEnabledlinkMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2))
ciscoVoiceEnabledlinkMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 1, 1)).setObjects(("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledMacAddrGroup"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceEnabledlinkMIBCompliance = ciscoVoiceEnabledlinkMIBCompliance.setStatus('current')
cvEnabledMacAddrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2, 1)).setObjects(("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledDefaultMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvEnabledMacAddrGroup = cvEnabledMacAddrGroup.setStatus('current')
cvEnabledLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2, 2)).setObjects(("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkIndex"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkType"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkInterfaceName"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkVpiDlci"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkVci"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkRemoteMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvEnabledLinkGroup = cvEnabledLinkGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-ENABLED-LINK-MIB", cvEnabledLinkTable=cvEnabledLinkTable, cvEnabledLinkType=cvEnabledLinkType, ciscoVoiceEnabledlinkMIBCompliances=ciscoVoiceEnabledlinkMIBCompliances, ciscoVoiceEnabledLinkMIB=ciscoVoiceEnabledLinkMIB, cvEnabledLinkInterfaceName=cvEnabledLinkInterfaceName, ciscoVoiceEnabledlinkMIBGroups=ciscoVoiceEnabledlinkMIBGroups, cvEnabledLinkIndex=cvEnabledLinkIndex, ciscoVoiceEnabledlinkMIBCompliance=ciscoVoiceEnabledlinkMIBCompliance, cvEnabledLinkVpiDlci=cvEnabledLinkVpiDlci, ciscoVoiceEnabledLinkMIBNotificationPrefix=ciscoVoiceEnabledLinkMIBNotificationPrefix, cvEnabledLinkVci=cvEnabledLinkVci, cvEnabledLinkEntry=cvEnabledLinkEntry, cvEnabledLinkGroup=cvEnabledLinkGroup, cvenabledlinkMIBObjects=cvenabledlinkMIBObjects, PYSNMP_MODULE_ID=ciscoVoiceEnabledLinkMIB, cvEnabledDefaultMacAddr=cvEnabledDefaultMacAddr, cvEnabledLink=cvEnabledLink, ciscoVoiceEnabledlinkMIBConformance=ciscoVoiceEnabledlinkMIBConformance, cvEnabledMacAddrGroup=cvEnabledMacAddrGroup, ciscoVoiceEnabledLinkMIBNotifications=ciscoVoiceEnabledLinkMIBNotifications, cvEnabledLinkRemoteMacAddr=cvEnabledLinkRemoteMacAddr)
