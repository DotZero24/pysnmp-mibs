#
# PySNMP MIB module ME1200-TT-LOOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ME1200-TT-LOOP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ME1200RowEditorState, ME1200DisplayString, ME1200InterfaceIndex = mibBuilder.importSymbols("ME1200-TC", "ME1200RowEditorState", "ME1200DisplayString", "ME1200InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention")
me1200TtLoopMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128))
me1200TtLoopMib.setRevisions(('2016-12-07 00:00', '2014-05-19 00:00',))
if mibBuilder.loadTexts: me1200TtLoopMib.setLastUpdated('201405190000Z')
if mibBuilder.loadTexts: me1200TtLoopMib.setOrganization('Cisco Systems, Inc')
class ME1200TtLoopInstanceAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("adminDisabled", 0), ("adminEnabled", 1))

class ME1200TtLoopInstanceDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("facility", 0), ("terminal", 1))

class ME1200TtLoopInstanceDomain(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("port", 0), ("evc", 1), ("vlan", 2))

class ME1200TtLoopInstanceOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("operDown", 0), ("operUp", 1), ("operInact", 2))

class ME1200TtLoopInstanceSubscriber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("all", 1), ("test", 2))

class ME1200TtLoopInstanceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("macLoop", 0), ("oamLoop", 1))

me1200TtLoopMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1))
me1200TtLoopCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 1))
me1200TtLoopCapabilitiesInstanceMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200TtLoopCapabilitiesInstanceMax.setStatus('current')
me1200TtLoopCapabilitiesNameMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200TtLoopCapabilitiesNameMax.setStatus('current')
me1200TtLoopConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2))
me1200TtLoopConfigInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1), )
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceTable.setStatus('current')
me1200TtLoopConfigInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1), ).setIndexNames((0, "ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceId"))
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceEntry.setStatus('current')
me1200TtLoopConfigInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceId.setStatus('current')
me1200TtLoopConfigInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 2), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceName.setStatus('current')
me1200TtLoopConfigInstanceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 3), ME1200TtLoopInstanceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceType.setStatus('current')
me1200TtLoopConfigInstanceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 4), ME1200TtLoopInstanceDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceDirection.setStatus('current')
me1200TtLoopConfigInstanceDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 5), ME1200TtLoopInstanceDomain()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceDomain.setStatus('current')
me1200TtLoopConfigInstanceFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceFlow.setStatus('current')
me1200TtLoopConfigInstancePort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 7), ME1200InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstancePort.setStatus('current')
me1200TtLoopConfigInstanceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceLevel.setStatus('current')
me1200TtLoopConfigInstanceSubscriber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 9), ME1200TtLoopInstanceSubscriber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceSubscriber.setStatus('current')
me1200TtLoopConfigInstanceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 10), ME1200TtLoopInstanceAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceAdminState.setStatus('current')
me1200TtLoopConfigInstanceAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 100), ME1200RowEditorState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceAction.setStatus('current')
me1200TtLoopConfigInstanceRowEditor = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2))
me1200TtLoopConfigInstanceRowEditorId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorId.setStatus('current')
me1200TtLoopConfigInstanceRowEditorName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 2), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorName.setStatus('current')
me1200TtLoopConfigInstanceRowEditorType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 3), ME1200TtLoopInstanceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorType.setStatus('current')
me1200TtLoopConfigInstanceRowEditorDirection = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 4), ME1200TtLoopInstanceDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorDirection.setStatus('current')
me1200TtLoopConfigInstanceRowEditorDomain = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 5), ME1200TtLoopInstanceDomain()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorDomain.setStatus('current')
me1200TtLoopConfigInstanceRowEditorFlow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorFlow.setStatus('current')
me1200TtLoopConfigInstanceRowEditorPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 7), ME1200InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorPort.setStatus('current')
me1200TtLoopConfigInstanceRowEditorLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorLevel.setStatus('current')
me1200TtLoopConfigInstanceRowEditorSubscriber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 9), ME1200TtLoopInstanceSubscriber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorSubscriber.setStatus('current')
me1200TtLoopConfigInstanceRowEditorAdminState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 10), ME1200TtLoopInstanceAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorAdminState.setStatus('current')
me1200TtLoopConfigInstanceRowEditorAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 100), ME1200RowEditorState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopConfigInstanceRowEditorAction.setStatus('current')
me1200TtLoopLlConfigInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 3), )
if mibBuilder.loadTexts: me1200TtLoopLlConfigInstanceTable.setStatus('current')
me1200TtLoopLlConfigInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 3, 1), ).setIndexNames((0, "ME1200-TT-LOOP-MIB", "me1200TtLoopLlConfigInstanceId"))
if mibBuilder.loadTexts: me1200TtLoopLlConfigInstanceEntry.setStatus('current')
me1200TtLoopLlConfigInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: me1200TtLoopLlConfigInstanceId.setStatus('current')
me1200TtLoopLlConfigInstanceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopLlConfigInstanceEnable.setStatus('current')
me1200TtLoopLlConfigInstanceMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopLlConfigInstanceMepId.setStatus('current')
me1200TtLoopLlConfigInstanceSourceMac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 3, 1, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200TtLoopLlConfigInstanceSourceMac.setStatus('current')
me1200TtLoopStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3))
me1200TtLoopStatusInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 1), )
if mibBuilder.loadTexts: me1200TtLoopStatusInstanceTable.setStatus('current')
me1200TtLoopStatusInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 1, 1), ).setIndexNames((0, "ME1200-TT-LOOP-MIB", "me1200TtLoopStatusInstanceId"))
if mibBuilder.loadTexts: me1200TtLoopStatusInstanceEntry.setStatus('current')
me1200TtLoopStatusInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: me1200TtLoopStatusInstanceId.setStatus('current')
me1200TtLoopStatusInstanceOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 1, 1, 2), ME1200TtLoopInstanceOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200TtLoopStatusInstanceOperState.setStatus('current')
me1200TtLoopLlStatusInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 2), )
if mibBuilder.loadTexts: me1200TtLoopLlStatusInstanceTable.setStatus('current')
me1200TtLoopLlStatusInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 2, 1), ).setIndexNames((0, "ME1200-TT-LOOP-MIB", "me1200TtLoopLlStatusInstanceId"))
if mibBuilder.loadTexts: me1200TtLoopLlStatusInstanceEntry.setStatus('current')
me1200TtLoopLlStatusInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: me1200TtLoopLlStatusInstanceId.setStatus('current')
me1200TtLoopLlStatusInstanceRemainExpTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200TtLoopLlStatusInstanceRemainExpTimer.setStatus('current')
me1200TtLoopMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3))
me1200TtLoopMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 1))
me1200TtLoopMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2))
me1200TtLoopCapabilitiesInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 1)).setObjects(("ME1200-TT-LOOP-MIB", "me1200TtLoopCapabilitiesInstanceMax"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopCapabilitiesNameMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200TtLoopCapabilitiesInfoGroup = me1200TtLoopCapabilitiesInfoGroup.setStatus('current')
me1200TtLoopConfigInstanceTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 2)).setObjects(("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceName"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceType"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceDirection"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceDomain"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceFlow"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstancePort"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceLevel"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceSubscriber"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceAdminState"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200TtLoopConfigInstanceTableInfoGroup = me1200TtLoopConfigInstanceTableInfoGroup.setStatus('current')
me1200TtLoopConfigInstanceRowEditorInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 3)).setObjects(("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorId"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorName"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorType"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorDirection"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorDomain"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorFlow"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorPort"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorLevel"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorSubscriber"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorAdminState"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200TtLoopConfigInstanceRowEditorInfoGroup = me1200TtLoopConfigInstanceRowEditorInfoGroup.setStatus('current')
me1200TtLoopLlConfigInstanceTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 4)).setObjects(("ME1200-TT-LOOP-MIB", "me1200TtLoopLlConfigInstanceEnable"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopLlConfigInstanceMepId"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopLlConfigInstanceSourceMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200TtLoopLlConfigInstanceTableInfoGroup = me1200TtLoopLlConfigInstanceTableInfoGroup.setStatus('current')
me1200TtLoopStatusInstanceTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 5)).setObjects(("ME1200-TT-LOOP-MIB", "me1200TtLoopStatusInstanceOperState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200TtLoopStatusInstanceTableInfoGroup = me1200TtLoopStatusInstanceTableInfoGroup.setStatus('current')
me1200TtLoopLlStatusInstanceTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 6)).setObjects(("ME1200-TT-LOOP-MIB", "me1200TtLoopLlStatusInstanceRemainExpTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200TtLoopLlStatusInstanceTableInfoGroup = me1200TtLoopLlStatusInstanceTableInfoGroup.setStatus('current')
me1200TtLoopMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 1, 1)).setObjects(("ME1200-TT-LOOP-MIB", "me1200TtLoopCapabilitiesInfoGroup"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceTableInfoGroup"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorInfoGroup"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopLlConfigInstanceTableInfoGroup"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopStatusInstanceTableInfoGroup"), ("ME1200-TT-LOOP-MIB", "me1200TtLoopLlStatusInstanceTableInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200TtLoopMibCompliance = me1200TtLoopMibCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-TT-LOOP-MIB", me1200TtLoopMib=me1200TtLoopMib, me1200TtLoopConfigInstancePort=me1200TtLoopConfigInstancePort, me1200TtLoopConfigInstanceRowEditor=me1200TtLoopConfigInstanceRowEditor, me1200TtLoopConfigInstanceRowEditorDirection=me1200TtLoopConfigInstanceRowEditorDirection, me1200TtLoopLlConfigInstanceEntry=me1200TtLoopLlConfigInstanceEntry, me1200TtLoopLlStatusInstanceTable=me1200TtLoopLlStatusInstanceTable, me1200TtLoopMibConformance=me1200TtLoopMibConformance, me1200TtLoopLlConfigInstanceId=me1200TtLoopLlConfigInstanceId, me1200TtLoopLlStatusInstanceTableInfoGroup=me1200TtLoopLlStatusInstanceTableInfoGroup, me1200TtLoopConfig=me1200TtLoopConfig, me1200TtLoopLlConfigInstanceTableInfoGroup=me1200TtLoopLlConfigInstanceTableInfoGroup, me1200TtLoopCapabilities=me1200TtLoopCapabilities, me1200TtLoopConfigInstanceAdminState=me1200TtLoopConfigInstanceAdminState, ME1200TtLoopInstanceType=ME1200TtLoopInstanceType, me1200TtLoopConfigInstanceTable=me1200TtLoopConfigInstanceTable, me1200TtLoopConfigInstanceFlow=me1200TtLoopConfigInstanceFlow, me1200TtLoopCapabilitiesInstanceMax=me1200TtLoopCapabilitiesInstanceMax, me1200TtLoopStatusInstanceTable=me1200TtLoopStatusInstanceTable, me1200TtLoopConfigInstanceRowEditorName=me1200TtLoopConfigInstanceRowEditorName, me1200TtLoopConfigInstanceRowEditorPort=me1200TtLoopConfigInstanceRowEditorPort, me1200TtLoopConfigInstanceLevel=me1200TtLoopConfigInstanceLevel, me1200TtLoopLlConfigInstanceMepId=me1200TtLoopLlConfigInstanceMepId, me1200TtLoopStatusInstanceId=me1200TtLoopStatusInstanceId, me1200TtLoopConfigInstanceId=me1200TtLoopConfigInstanceId, me1200TtLoopMibObjects=me1200TtLoopMibObjects, me1200TtLoopConfigInstanceRowEditorId=me1200TtLoopConfigInstanceRowEditorId, PYSNMP_MODULE_ID=me1200TtLoopMib, ME1200TtLoopInstanceDirection=ME1200TtLoopInstanceDirection, me1200TtLoopConfigInstanceAction=me1200TtLoopConfigInstanceAction, me1200TtLoopConfigInstanceEntry=me1200TtLoopConfigInstanceEntry, me1200TtLoopStatusInstanceEntry=me1200TtLoopStatusInstanceEntry, me1200TtLoopLlStatusInstanceRemainExpTimer=me1200TtLoopLlStatusInstanceRemainExpTimer, ME1200TtLoopInstanceSubscriber=ME1200TtLoopInstanceSubscriber, me1200TtLoopStatusInstanceOperState=me1200TtLoopStatusInstanceOperState, me1200TtLoopConfigInstanceRowEditorSubscriber=me1200TtLoopConfigInstanceRowEditorSubscriber, ME1200TtLoopInstanceAdminState=ME1200TtLoopInstanceAdminState, me1200TtLoopCapabilitiesNameMax=me1200TtLoopCapabilitiesNameMax, me1200TtLoopConfigInstanceName=me1200TtLoopConfigInstanceName, me1200TtLoopConfigInstanceSubscriber=me1200TtLoopConfigInstanceSubscriber, me1200TtLoopConfigInstanceRowEditorDomain=me1200TtLoopConfigInstanceRowEditorDomain, me1200TtLoopConfigInstanceRowEditorAdminState=me1200TtLoopConfigInstanceRowEditorAdminState, ME1200TtLoopInstanceDomain=ME1200TtLoopInstanceDomain, me1200TtLoopMibGroups=me1200TtLoopMibGroups, ME1200TtLoopInstanceOperState=ME1200TtLoopInstanceOperState, me1200TtLoopConfigInstanceDirection=me1200TtLoopConfigInstanceDirection, me1200TtLoopConfigInstanceRowEditorType=me1200TtLoopConfigInstanceRowEditorType, me1200TtLoopStatus=me1200TtLoopStatus, me1200TtLoopLlStatusInstanceId=me1200TtLoopLlStatusInstanceId, me1200TtLoopConfigInstanceRowEditorInfoGroup=me1200TtLoopConfigInstanceRowEditorInfoGroup, me1200TtLoopCapabilitiesInfoGroup=me1200TtLoopCapabilitiesInfoGroup, me1200TtLoopConfigInstanceTableInfoGroup=me1200TtLoopConfigInstanceTableInfoGroup, me1200TtLoopLlConfigInstanceSourceMac=me1200TtLoopLlConfigInstanceSourceMac, me1200TtLoopMibCompliances=me1200TtLoopMibCompliances, me1200TtLoopMibCompliance=me1200TtLoopMibCompliance, me1200TtLoopConfigInstanceType=me1200TtLoopConfigInstanceType, me1200TtLoopConfigInstanceRowEditorFlow=me1200TtLoopConfigInstanceRowEditorFlow, me1200TtLoopConfigInstanceRowEditorAction=me1200TtLoopConfigInstanceRowEditorAction, me1200TtLoopLlConfigInstanceTable=me1200TtLoopLlConfigInstanceTable, me1200TtLoopLlStatusInstanceEntry=me1200TtLoopLlStatusInstanceEntry, me1200TtLoopStatusInstanceTableInfoGroup=me1200TtLoopStatusInstanceTableInfoGroup, me1200TtLoopConfigInstanceRowEditorLevel=me1200TtLoopConfigInstanceRowEditorLevel, me1200TtLoopConfigInstanceDomain=me1200TtLoopConfigInstanceDomain, me1200TtLoopLlConfigInstanceEnable=me1200TtLoopLlConfigInstanceEnable)
