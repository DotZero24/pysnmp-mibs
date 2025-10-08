#
# PySNMP MIB module ME1200-RMIRROR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ME1200-RMIRROR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:27:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ME1200Unsigned16, ME1200InterfaceIndex = mibBuilder.importSymbols("ME1200-TC", "ME1200Unsigned16", "ME1200InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
me1200RmirrorMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120))
me1200RmirrorMib.setRevisions(('2014-05-08 00:00', '2014-05-07 00:00',))
if mibBuilder.loadTexts: me1200RmirrorMib.setLastUpdated('201405080000Z')
if mibBuilder.loadTexts: me1200RmirrorMib.setOrganization('Cisco Systems, Inc')
class ME1200RmirrorMirrorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tx", 1), ("rx", 2), ("both", 3))

class ME1200RmirrorPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("intermediate", 1), ("destination", 2), ("reflector", 3))

class ME1200RmirrorSwitchType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("mirror", 0), ("source", 1), ("intermediate", 2), ("destination", 3))

me1200RmirrorMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1))
me1200RmirrorCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 1))
me1200RmirrorCapabilitiesReflectorPortSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200RmirrorCapabilitiesReflectorPortSupport.setStatus('current')
me1200RmirrorCapabilitiesCpuMirrorSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200RmirrorCapabilitiesCpuMirrorSupport.setStatus('current')
me1200RmirrorConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2))
me1200RmirrorConfigSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1), )
if mibBuilder.loadTexts: me1200RmirrorConfigSessionTable.setStatus('current')
me1200RmirrorConfigSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1), ).setIndexNames((0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSessionId"))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionEntry.setStatus('current')
me1200RmirrorConfigSessionSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSessionId.setStatus('current')
me1200RmirrorConfigSessionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200RmirrorConfigSessionMode.setStatus('current')
me1200RmirrorConfigSessionSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1, 3), ME1200RmirrorSwitchType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSwitchType.setStatus('current')
me1200RmirrorConfigSessionVid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1, 4), ME1200Unsigned16().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200RmirrorConfigSessionVid.setStatus('current')
me1200RmirrorConfigSessionSourceCpuTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2), )
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceCpuTable.setStatus('current')
me1200RmirrorConfigSessionSourceCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2, 1), ).setIndexNames((0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceCpuSessionId"), (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceCpuSwitchId"))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceCpuEntry.setStatus('current')
me1200RmirrorConfigSessionSourceCpuSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceCpuSessionId.setStatus('current')
me1200RmirrorConfigSessionSourceCpuSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceCpuSwitchId.setStatus('current')
me1200RmirrorConfigSessionSourceCpuMirrorType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2, 1, 3), ME1200RmirrorMirrorType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceCpuMirrorType.setStatus('current')
me1200RmirrorConfigSessionSourceVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3), )
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceVlanTable.setStatus('current')
me1200RmirrorConfigSessionSourceVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3, 1), ).setIndexNames((0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceVlanSessionId"), (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceVlanIfIndex"))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceVlanEntry.setStatus('current')
me1200RmirrorConfigSessionSourceVlanSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceVlanSessionId.setStatus('current')
me1200RmirrorConfigSessionSourceVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3, 1, 2), ME1200InterfaceIndex())
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceVlanIfIndex.setStatus('current')
me1200RmirrorConfigSessionSourceVlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourceVlanMode.setStatus('current')
me1200RmirrorConfigSessionSourcePortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4), )
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourcePortTable.setStatus('current')
me1200RmirrorConfigSessionSourcePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4, 1), ).setIndexNames((0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourcePortSessionId"), (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourcePortIfIndex"))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourcePortEntry.setStatus('current')
me1200RmirrorConfigSessionSourcePortSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourcePortSessionId.setStatus('current')
me1200RmirrorConfigSessionSourcePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4, 1, 2), ME1200InterfaceIndex())
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourcePortIfIndex.setStatus('current')
me1200RmirrorConfigSessionSourcePortMirrorType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4, 1, 3), ME1200RmirrorMirrorType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200RmirrorConfigSessionSourcePortMirrorType.setStatus('current')
me1200RmirrorConfigSessionPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5), )
if mibBuilder.loadTexts: me1200RmirrorConfigSessionPortTable.setStatus('current')
me1200RmirrorConfigSessionPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5, 1), ).setIndexNames((0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionPortSessionId"), (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionPortIfIndex"))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionPortEntry.setStatus('current')
me1200RmirrorConfigSessionPortSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: me1200RmirrorConfigSessionPortSessionId.setStatus('current')
me1200RmirrorConfigSessionPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5, 1, 2), ME1200InterfaceIndex())
if mibBuilder.loadTexts: me1200RmirrorConfigSessionPortIfIndex.setStatus('current')
me1200RmirrorConfigSessionPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5, 1, 3), ME1200RmirrorPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200RmirrorConfigSessionPortType.setStatus('current')
me1200RmirrorMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2))
me1200RmirrorMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 1))
me1200RmirrorMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2))
me1200RmirrorCapabilitiesInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 1)).setObjects(("ME1200-RMIRROR-MIB", "me1200RmirrorCapabilitiesReflectorPortSupport"), ("ME1200-RMIRROR-MIB", "me1200RmirrorCapabilitiesCpuMirrorSupport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200RmirrorCapabilitiesInfoGroup = me1200RmirrorCapabilitiesInfoGroup.setStatus('current')
me1200RmirrorConfigSessionTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 2)).setObjects(("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionMode"), ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSwitchType"), ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionVid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200RmirrorConfigSessionTableInfoGroup = me1200RmirrorConfigSessionTableInfoGroup.setStatus('current')
me1200RmirrorConfigSessionSourceCpuTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 3)).setObjects(("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceCpuMirrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200RmirrorConfigSessionSourceCpuTableInfoGroup = me1200RmirrorConfigSessionSourceCpuTableInfoGroup.setStatus('current')
me1200RmirrorConfigSessionSourceVlanTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 4)).setObjects(("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceVlanMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200RmirrorConfigSessionSourceVlanTableInfoGroup = me1200RmirrorConfigSessionSourceVlanTableInfoGroup.setStatus('current')
me1200RmirrorConfigSessionSourcePortTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 5)).setObjects(("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourcePortMirrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200RmirrorConfigSessionSourcePortTableInfoGroup = me1200RmirrorConfigSessionSourcePortTableInfoGroup.setStatus('current')
me1200RmirrorConfigSessionPortTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 6)).setObjects(("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionPortType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200RmirrorConfigSessionPortTableInfoGroup = me1200RmirrorConfigSessionPortTableInfoGroup.setStatus('current')
me1200RmirrorMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 1, 1)).setObjects(("ME1200-RMIRROR-MIB", "me1200RmirrorCapabilitiesInfoGroup"), ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionTableInfoGroup"), ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceCpuTableInfoGroup"), ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceVlanTableInfoGroup"), ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourcePortTableInfoGroup"), ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionPortTableInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200RmirrorMibCompliance = me1200RmirrorMibCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-RMIRROR-MIB", me1200RmirrorCapabilitiesCpuMirrorSupport=me1200RmirrorCapabilitiesCpuMirrorSupport, me1200RmirrorConfig=me1200RmirrorConfig, me1200RmirrorCapabilitiesReflectorPortSupport=me1200RmirrorCapabilitiesReflectorPortSupport, me1200RmirrorConfigSessionSourceCpuTable=me1200RmirrorConfigSessionSourceCpuTable, me1200RmirrorConfigSessionSourcePortSessionId=me1200RmirrorConfigSessionSourcePortSessionId, me1200RmirrorConfigSessionPortSessionId=me1200RmirrorConfigSessionPortSessionId, me1200RmirrorConfigSessionSourceCpuEntry=me1200RmirrorConfigSessionSourceCpuEntry, me1200RmirrorConfigSessionSourceVlanTableInfoGroup=me1200RmirrorConfigSessionSourceVlanTableInfoGroup, me1200RmirrorConfigSessionSourcePortTable=me1200RmirrorConfigSessionSourcePortTable, me1200RmirrorConfigSessionSourcePortEntry=me1200RmirrorConfigSessionSourcePortEntry, me1200RmirrorConfigSessionSourceVlanSessionId=me1200RmirrorConfigSessionSourceVlanSessionId, me1200RmirrorConfigSessionTable=me1200RmirrorConfigSessionTable, me1200RmirrorConfigSessionPortType=me1200RmirrorConfigSessionPortType, me1200RmirrorConfigSessionPortTable=me1200RmirrorConfigSessionPortTable, me1200RmirrorConfigSessionEntry=me1200RmirrorConfigSessionEntry, me1200RmirrorConfigSessionSourcePortIfIndex=me1200RmirrorConfigSessionSourcePortIfIndex, PYSNMP_MODULE_ID=me1200RmirrorMib, me1200RmirrorConfigSessionSourceCpuSwitchId=me1200RmirrorConfigSessionSourceCpuSwitchId, me1200RmirrorConfigSessionSwitchType=me1200RmirrorConfigSessionSwitchType, me1200RmirrorConfigSessionSessionId=me1200RmirrorConfigSessionSessionId, me1200RmirrorConfigSessionVid=me1200RmirrorConfigSessionVid, me1200RmirrorConfigSessionSourceCpuMirrorType=me1200RmirrorConfigSessionSourceCpuMirrorType, me1200RmirrorMibCompliance=me1200RmirrorMibCompliance, me1200RmirrorCapabilities=me1200RmirrorCapabilities, me1200RmirrorConfigSessionPortIfIndex=me1200RmirrorConfigSessionPortIfIndex, me1200RmirrorConfigSessionMode=me1200RmirrorConfigSessionMode, me1200RmirrorMibConformance=me1200RmirrorMibConformance, me1200RmirrorCapabilitiesInfoGroup=me1200RmirrorCapabilitiesInfoGroup, me1200RmirrorConfigSessionSourceVlanTable=me1200RmirrorConfigSessionSourceVlanTable, ME1200RmirrorMirrorType=ME1200RmirrorMirrorType, me1200RmirrorMibGroups=me1200RmirrorMibGroups, me1200RmirrorConfigSessionPortTableInfoGroup=me1200RmirrorConfigSessionPortTableInfoGroup, me1200RmirrorConfigSessionPortEntry=me1200RmirrorConfigSessionPortEntry, me1200RmirrorConfigSessionSourcePortTableInfoGroup=me1200RmirrorConfigSessionSourcePortTableInfoGroup, me1200RmirrorConfigSessionSourceVlanEntry=me1200RmirrorConfigSessionSourceVlanEntry, me1200RmirrorMib=me1200RmirrorMib, me1200RmirrorConfigSessionSourceCpuTableInfoGroup=me1200RmirrorConfigSessionSourceCpuTableInfoGroup, ME1200RmirrorSwitchType=ME1200RmirrorSwitchType, ME1200RmirrorPortType=ME1200RmirrorPortType, me1200RmirrorConfigSessionSourceVlanIfIndex=me1200RmirrorConfigSessionSourceVlanIfIndex, me1200RmirrorConfigSessionSourceVlanMode=me1200RmirrorConfigSessionSourceVlanMode, me1200RmirrorMibObjects=me1200RmirrorMibObjects, me1200RmirrorConfigSessionSourceCpuSessionId=me1200RmirrorConfigSessionSourceCpuSessionId, me1200RmirrorMibCompliances=me1200RmirrorMibCompliances, me1200RmirrorConfigSessionTableInfoGroup=me1200RmirrorConfigSessionTableInfoGroup, me1200RmirrorConfigSessionSourcePortMirrorType=me1200RmirrorConfigSessionSourcePortMirrorType)
