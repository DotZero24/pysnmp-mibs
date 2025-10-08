#
# PySNMP MIB module CISCO-VOICE-CARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-CARD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoiceCard = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 300576))
ciscoVoiceCard.setRevisions(('2002-02-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceCard.setLastUpdated('200202150000Z')
if mibBuilder.loadTexts: ciscoVoiceCard.setOrganization('Cisco Systems, Inc')
ciscoVoiceCardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 0))
ciscoVoiceCardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1))
cVoiceCardTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1), )
if mibBuilder.loadTexts: cVoiceCardTable.setStatus('current')
cVoiceCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CARD-MIB", "cVoiceCardIndex"))
if mibBuilder.loadTexts: cVoiceCardEntry.setStatus('current')
cVoiceCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: cVoiceCardIndex.setStatus('current')
cVoiceCardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVoiceCardSlotNumber.setStatus('current')
cVoiceCardCodecComplexity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4))).clone(namedValues=NamedValues(("hc", 2), ("mc", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoiceCardCodecComplexity.setStatus('current')
cVoiceCardAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoiceCardAdminStatus.setStatus('current')
ciscoVoiceCardConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2))
ciscoVoiceCardMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 1))
ciscoVoiceCardMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 2))
ciscoVoiceCardMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 1, 1)).setObjects(("CISCO-VOICE-CARD-MIB", "ciscoVoiceCardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCardMIBCompliance = ciscoVoiceCardMIBCompliance.setStatus('current')
ciscoVoiceCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 2, 1)).setObjects(("CISCO-VOICE-CARD-MIB", "cVoiceCardSlotNumber"), ("CISCO-VOICE-CARD-MIB", "cVoiceCardCodecComplexity"), ("CISCO-VOICE-CARD-MIB", "cVoiceCardAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCardGroup = ciscoVoiceCardGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-CARD-MIB", ciscoVoiceCardObjects=ciscoVoiceCardObjects, ciscoVoiceCardNotifications=ciscoVoiceCardNotifications, cVoiceCardSlotNumber=cVoiceCardSlotNumber, ciscoVoiceCardConformance=ciscoVoiceCardConformance, cVoiceCardIndex=cVoiceCardIndex, cVoiceCardCodecComplexity=cVoiceCardCodecComplexity, ciscoVoiceCardMIBGroups=ciscoVoiceCardMIBGroups, cVoiceCardTable=cVoiceCardTable, ciscoVoiceCardMIBCompliances=ciscoVoiceCardMIBCompliances, PYSNMP_MODULE_ID=ciscoVoiceCard, cVoiceCardAdminStatus=cVoiceCardAdminStatus, ciscoVoiceCard=ciscoVoiceCard, ciscoVoiceCardMIBCompliance=ciscoVoiceCardMIBCompliance, ciscoVoiceCardGroup=ciscoVoiceCardGroup, cVoiceCardEntry=cVoiceCardEntry)
