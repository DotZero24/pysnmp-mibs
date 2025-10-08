#
# PySNMP MIB module Juniper-UNI-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-UNI-SONET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifAlias, InterfaceIndexOrZero, ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifAlias", "InterfaceIndexOrZero", "ifIndex", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniNextIfIndex, = mibBuilder.importSymbols("Juniper-TC", "JuniNextIfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
juniSonetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7))
juniSonetMIB.setRevisions(('2003-07-16 19:52', '2002-11-22 16:37', '2001-10-10 20:42', '2001-01-02 18:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: juniSonetMIB.setLastUpdated('200307161952Z')
if mibBuilder.loadTexts: juniSonetMIB.setOrganization('Juniper Networks, Inc.')
class JuniSonetLineSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("sonetUnknownSpeed", 0), ("sonetOc1Stm0", 1), ("sonetOc3Stm1", 2), ("sonetOc12Stm3", 3), ("sonetOc48Stm16", 4))

class JuniSonetLogicalPathChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JuniSonetPathHierarchy(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class JuniSonetPathC2ByteOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class JuniSonetVTType(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4, 5))
    namedValues = NamedValues(("tribVT15TU11", 0), ("tribVT20TU12", 1), ("tribVT3", 3), ("tribVT6", 4), ("tribVT6c", 5))

juniSonetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1))
juniSonetPathObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2))
juniSonetVTObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3))
juniSonetMediumTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1), )
if mibBuilder.loadTexts: juniSonetMediumTable.setStatus('current')
juniSonetMediumEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: juniSonetMediumEntry.setStatus('current')
juniSonetMediumType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSonetMediumType.setStatus('deprecated')
juniSonetMediumLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sonetNoLoop", 0), ("sonetFacilityLoop", 1), ("sonetTerminalLoop", 2), ("sonetOtherLoop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSonetMediumLoopbackConfig.setStatus('current')
juniSonetMediumTimingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("loop", 0), ("internalModule", 1), ("internalChassis", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSonetMediumTimingSource.setStatus('current')
juniSonetMediumCircuitIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSonetMediumCircuitIdentifier.setStatus('deprecated')
juniSonetMediumTriggerAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 5), Bits().clone(namedValues=NamedValues(("sectionLOS", 0), ("sectionLOF", 1), ("lineAIS", 2), ("lineRDI", 3))).clone(namedValues=NamedValues(("sectionLOS", 0), ("sectionLOS", 0), ("lineAIS", 2), ("lineRDI", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSonetMediumTriggerAlarms.setStatus('current')
juniSonetMediumTriggerDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2500)).clone(2500)).setUnits('ms').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSonetMediumTriggerDelay.setStatus('current')
juniSonetPathCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1), )
if mibBuilder.loadTexts: juniSonetPathCapabilityTable.setStatus('current')
juniSonetPathCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: juniSonetPathCapabilityEntry.setStatus('current')
juniSonetPathRemoveFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSonetPathRemoveFlag.setStatus('current')
juniSonetPathChannelized = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSonetPathChannelized.setStatus('current')
juniSonetPathMaximumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSonetPathMaximumChannels.setStatus('current')
juniSonetPathMinimumPathSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 4), JuniSonetLineSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSonetPathMinimumPathSpeed.setStatus('current')
juniSonetPathMaximumPathSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 5), JuniSonetLineSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSonetPathMaximumPathSpeed.setStatus('current')
juniSonetPathNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 2), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSonetPathNextIfIndex.setStatus('current')
juniSonetPathTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3), )
if mibBuilder.loadTexts: juniSonetPathTable.setStatus('current')
juniSonetPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1), ).setIndexNames((0, "Juniper-UNI-SONET-MIB", "juniSonetPathIfIndex"))
if mibBuilder.loadTexts: juniSonetPathEntry.setStatus('current')
juniSonetPathIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniSonetPathIfIndex.setStatus('current')
juniSonetPathLogicalChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 2), JuniSonetLogicalPathChannel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathLogicalChannel.setStatus('current')
juniSonetPathSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 3), JuniSonetLineSpeed()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathSpeed.setStatus('current')
juniSonetPathHierarchy = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 4), JuniSonetPathHierarchy()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathHierarchy.setStatus('current')
juniSonetPathLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathLowerIfIndex.setStatus('current')
juniSonetPathRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathRowStatus.setStatus('current')
juniSonetPathTriggerAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 7), Bits().clone(namedValues=NamedValues(("pathLOP", 0), ("pathAIS", 1), ("pathRDI", 2))).clone(namedValues=NamedValues(("pathLOP", 0), ("pathAIS", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathTriggerAlarms.setStatus('current')
juniSonetPathC2ByteOverrideFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathC2ByteOverrideFlag.setStatus('current')
juniSonetPathC2ByteOverride = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 9), JuniSonetPathC2ByteOverride()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathC2ByteOverride.setStatus('current')
juniSonetPathTriggerDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2500)).clone(2500)).setUnits('ms').setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetPathTriggerDelay.setStatus('current')
juniSonetPathEventStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniSonetPathEventStatus.setStatus('current')
juniSonetVTNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSonetVTNextIfIndex.setStatus('current')
juniSonetVTTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2), )
if mibBuilder.loadTexts: juniSonetVTTable.setStatus('current')
juniSonetVTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1), ).setIndexNames((0, "Juniper-UNI-SONET-MIB", "juniSonetVTIfIndex"))
if mibBuilder.loadTexts: juniSonetVTEntry.setStatus('current')
juniSonetVTIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniSonetVTIfIndex.setStatus('current')
juniSonetVTPathLogicalChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 2), JuniSonetLogicalPathChannel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetVTPathLogicalChannel.setStatus('current')
juniSonetVTType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 3), JuniSonetVTType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetVTType.setStatus('deprecated')
juniSonetVTPathPayload = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetVTPathPayload.setStatus('current')
juniSonetVTTributaryGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetVTTributaryGroup.setStatus('current')
juniSonetVTTributarySubChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetVTTributarySubChannel.setStatus('current')
juniSonetVTLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetVTLowerIfIndex.setStatus('current')
juniSonetVTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSonetVTRowStatus.setStatus('current')
juniSonetTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 5))
juniSonetPathEventIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 5, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniSonetPathEventIfIndex.setStatus('current')
juniSonetTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 6))
juniSonetTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 6, 0))
juniSonetPathEvents = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 6, 0, 1)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetPathEventIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetPathEventStatus"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: juniSonetPathEvents.setStatus('current')
juniSonetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4))
juniSonetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1))
juniSonetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2))
juniSonetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 1)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetCompliance = juniSonetCompliance.setStatus('obsolete')
juniSonetCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 2)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetGroup"), ("Juniper-UNI-SONET-MIB", "juniSonetPathGroup"), ("Juniper-UNI-SONET-MIB", "juniSonetVirtualTributaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetCompliance2 = juniSonetCompliance2.setStatus('obsolete')
juniSonetCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 3)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetGroup2"), ("Juniper-UNI-SONET-MIB", "juniSonetPathGroup"), ("Juniper-UNI-SONET-MIB", "juniSonetVirtualTributaryGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetCompliance3 = juniSonetCompliance3.setStatus('obsolete')
juniSonetCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 4)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetGroup3"), ("Juniper-UNI-SONET-MIB", "juniSonetPathGroup2"), ("Juniper-UNI-SONET-MIB", "juniSonetVirtualTributaryGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetCompliance4 = juniSonetCompliance4.setStatus('obsolete')
juniSonetCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 5)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetGroup3"), ("Juniper-UNI-SONET-MIB", "juniSonetPathGroup3"), ("Juniper-UNI-SONET-MIB", "juniSonetPathNotificationGroup"), ("Juniper-UNI-SONET-MIB", "juniSonetVirtualTributaryGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetCompliance5 = juniSonetCompliance5.setStatus('current')
juniSonetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 1)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetMediumType"), ("Juniper-UNI-SONET-MIB", "juniSonetMediumLoopbackConfig"), ("Juniper-UNI-SONET-MIB", "juniSonetMediumTimingSource"), ("Juniper-UNI-SONET-MIB", "juniSonetMediumCircuitIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetGroup = juniSonetGroup.setStatus('obsolete')
juniSonetPathGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 2)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetPathRemoveFlag"), ("Juniper-UNI-SONET-MIB", "juniSonetPathChannelized"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumChannels"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMinimumPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathNextIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetPathLogicalChannel"), ("Juniper-UNI-SONET-MIB", "juniSonetPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathHierarchy"), ("Juniper-UNI-SONET-MIB", "juniSonetPathLowerIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetPathRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetPathGroup = juniSonetPathGroup.setStatus('obsolete')
juniSonetVirtualTributaryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 3)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetVTNextIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetVTPathLogicalChannel"), ("Juniper-UNI-SONET-MIB", "juniSonetVTType"), ("Juniper-UNI-SONET-MIB", "juniSonetVTPathPayload"), ("Juniper-UNI-SONET-MIB", "juniSonetVTTributaryGroup"), ("Juniper-UNI-SONET-MIB", "juniSonetVTTributarySubChannel"), ("Juniper-UNI-SONET-MIB", "juniSonetVTLowerIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetVTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetVirtualTributaryGroup = juniSonetVirtualTributaryGroup.setStatus('obsolete')
juniSonetGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 4)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetMediumLoopbackConfig"), ("Juniper-UNI-SONET-MIB", "juniSonetMediumTimingSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetGroup2 = juniSonetGroup2.setStatus('obsolete')
juniSonetVirtualTributaryGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 5)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetVTNextIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetVTPathLogicalChannel"), ("Juniper-UNI-SONET-MIB", "juniSonetVTPathPayload"), ("Juniper-UNI-SONET-MIB", "juniSonetVTTributaryGroup"), ("Juniper-UNI-SONET-MIB", "juniSonetVTTributarySubChannel"), ("Juniper-UNI-SONET-MIB", "juniSonetVTLowerIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetVTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetVirtualTributaryGroup2 = juniSonetVirtualTributaryGroup2.setStatus('current')
juniSonetDeprecatedMediumGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 6)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetMediumType"), ("Juniper-UNI-SONET-MIB", "juniSonetMediumCircuitIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetDeprecatedMediumGroup = juniSonetDeprecatedMediumGroup.setStatus('deprecated')
juniSonetDeprecatedVTGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 7)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetVTType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetDeprecatedVTGroup = juniSonetDeprecatedVTGroup.setStatus('deprecated')
juniSonetGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 8)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetMediumLoopbackConfig"), ("Juniper-UNI-SONET-MIB", "juniSonetMediumTimingSource"), ("Juniper-UNI-SONET-MIB", "juniSonetMediumTriggerAlarms"), ("Juniper-UNI-SONET-MIB", "juniSonetMediumTriggerDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetGroup3 = juniSonetGroup3.setStatus('current')
juniSonetPathGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 9)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetPathRemoveFlag"), ("Juniper-UNI-SONET-MIB", "juniSonetPathChannelized"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumChannels"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMinimumPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathNextIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetPathLogicalChannel"), ("Juniper-UNI-SONET-MIB", "juniSonetPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathHierarchy"), ("Juniper-UNI-SONET-MIB", "juniSonetPathLowerIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetPathRowStatus"), ("Juniper-UNI-SONET-MIB", "juniSonetPathTriggerAlarms"), ("Juniper-UNI-SONET-MIB", "juniSonetPathC2ByteOverrideFlag"), ("Juniper-UNI-SONET-MIB", "juniSonetPathC2ByteOverride"), ("Juniper-UNI-SONET-MIB", "juniSonetPathTriggerDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetPathGroup2 = juniSonetPathGroup2.setStatus('obsolete')
juniSonetPathGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 10)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetPathRemoveFlag"), ("Juniper-UNI-SONET-MIB", "juniSonetPathChannelized"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumChannels"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMinimumPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathNextIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetPathLogicalChannel"), ("Juniper-UNI-SONET-MIB", "juniSonetPathSpeed"), ("Juniper-UNI-SONET-MIB", "juniSonetPathHierarchy"), ("Juniper-UNI-SONET-MIB", "juniSonetPathLowerIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetPathRowStatus"), ("Juniper-UNI-SONET-MIB", "juniSonetPathTriggerAlarms"), ("Juniper-UNI-SONET-MIB", "juniSonetPathC2ByteOverrideFlag"), ("Juniper-UNI-SONET-MIB", "juniSonetPathC2ByteOverride"), ("Juniper-UNI-SONET-MIB", "juniSonetPathTriggerDelay"), ("Juniper-UNI-SONET-MIB", "juniSonetPathEventIfIndex"), ("Juniper-UNI-SONET-MIB", "juniSonetPathEventStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetPathGroup3 = juniSonetPathGroup3.setStatus('current')
juniSonetPathNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 11)).setObjects(("Juniper-UNI-SONET-MIB", "juniSonetPathEvents"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetPathNotificationGroup = juniSonetPathNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-UNI-SONET-MIB", juniSonetTraps=juniSonetTraps, juniSonetPathGroup=juniSonetPathGroup, JuniSonetLogicalPathChannel=JuniSonetLogicalPathChannel, juniSonetMediumTable=juniSonetMediumTable, juniSonetMediumEntry=juniSonetMediumEntry, juniSonetPathEntry=juniSonetPathEntry, juniSonetVTNextIfIndex=juniSonetVTNextIfIndex, juniSonetCompliances=juniSonetCompliances, juniSonetGroup2=juniSonetGroup2, juniSonetMediumTriggerAlarms=juniSonetMediumTriggerAlarms, juniSonetVirtualTributaryGroup2=juniSonetVirtualTributaryGroup2, juniSonetTrapPrefix=juniSonetTrapPrefix, juniSonetPathGroup3=juniSonetPathGroup3, juniSonetVirtualTributaryGroup=juniSonetVirtualTributaryGroup, JuniSonetLineSpeed=JuniSonetLineSpeed, juniSonetPathTriggerAlarms=juniSonetPathTriggerAlarms, juniSonetVTTable=juniSonetVTTable, juniSonetGroup3=juniSonetGroup3, juniSonetPathIfIndex=juniSonetPathIfIndex, juniSonetVTPathLogicalChannel=juniSonetVTPathLogicalChannel, juniSonetPathC2ByteOverrideFlag=juniSonetPathC2ByteOverrideFlag, juniSonetPathEventStatus=juniSonetPathEventStatus, juniSonetPathMinimumPathSpeed=juniSonetPathMinimumPathSpeed, juniSonetObjects=juniSonetObjects, juniSonetPathObjects=juniSonetPathObjects, PYSNMP_MODULE_ID=juniSonetMIB, juniSonetGroups=juniSonetGroups, juniSonetPathC2ByteOverride=juniSonetPathC2ByteOverride, juniSonetVTEntry=juniSonetVTEntry, juniSonetMIB=juniSonetMIB, juniSonetVTIfIndex=juniSonetVTIfIndex, juniSonetPathChannelized=juniSonetPathChannelized, juniSonetPathNextIfIndex=juniSonetPathNextIfIndex, juniSonetVTTributarySubChannel=juniSonetVTTributarySubChannel, juniSonetVTRowStatus=juniSonetVTRowStatus, juniSonetPathTable=juniSonetPathTable, juniSonetPathMaximumChannels=juniSonetPathMaximumChannels, juniSonetPathEventIfIndex=juniSonetPathEventIfIndex, juniSonetDeprecatedMediumGroup=juniSonetDeprecatedMediumGroup, juniSonetPathCapabilityEntry=juniSonetPathCapabilityEntry, juniSonetVTType=juniSonetVTType, juniSonetPathHierarchy=juniSonetPathHierarchy, juniSonetPathLowerIfIndex=juniSonetPathLowerIfIndex, juniSonetPathNotificationGroup=juniSonetPathNotificationGroup, juniSonetGroup=juniSonetGroup, juniSonetCompliance=juniSonetCompliance, juniSonetPathGroup2=juniSonetPathGroup2, juniSonetMediumType=juniSonetMediumType, juniSonetPathMaximumPathSpeed=juniSonetPathMaximumPathSpeed, juniSonetMediumTimingSource=juniSonetMediumTimingSource, juniSonetPathEvents=juniSonetPathEvents, juniSonetPathRowStatus=juniSonetPathRowStatus, JuniSonetPathHierarchy=JuniSonetPathHierarchy, juniSonetDeprecatedVTGroup=juniSonetDeprecatedVTGroup, juniSonetConformance=juniSonetConformance, JuniSonetPathC2ByteOverride=JuniSonetPathC2ByteOverride, juniSonetPathCapabilityTable=juniSonetPathCapabilityTable, juniSonetPathSpeed=juniSonetPathSpeed, juniSonetPathLogicalChannel=juniSonetPathLogicalChannel, juniSonetTrapControl=juniSonetTrapControl, juniSonetVTObjects=juniSonetVTObjects, juniSonetMediumTriggerDelay=juniSonetMediumTriggerDelay, juniSonetPathTriggerDelay=juniSonetPathTriggerDelay, JuniSonetVTType=JuniSonetVTType, juniSonetPathRemoveFlag=juniSonetPathRemoveFlag, juniSonetVTTributaryGroup=juniSonetVTTributaryGroup, juniSonetCompliance2=juniSonetCompliance2, juniSonetVTLowerIfIndex=juniSonetVTLowerIfIndex, juniSonetCompliance3=juniSonetCompliance3, juniSonetMediumLoopbackConfig=juniSonetMediumLoopbackConfig, juniSonetVTPathPayload=juniSonetVTPathPayload, juniSonetMediumCircuitIdentifier=juniSonetMediumCircuitIdentifier, juniSonetCompliance4=juniSonetCompliance4, juniSonetCompliance5=juniSonetCompliance5)
