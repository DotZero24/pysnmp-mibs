#
# PySNMP MIB module ARUBAWIRED-LOOPPROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-LOOPPROTECT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "TextualConvention")
arubaWiredLoopProtectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1))
arubaWiredLoopProtectMIB.setRevisions(('2017-11-02 00:00',))
if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setLastUpdated('201711020000Z')
if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setOrganization('HPE/Aruba Networking Division')
class ConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3))

class VidList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

arubaWiredLoopProtectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1))
class LoopProtectReceiverAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disableTx", 1), ("noDisable", 2), ("disableTxRx", 3))

arubaWiredLoopProtect = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5))
arubaWiredLoopProtectNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0))
arubaWiredLoopProtectBase = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1))
arubaWiredLoopProtectPort = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2))
arubaWiredLoopProtectInterval = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectInterval.setStatus('current')
arubaWiredLoopProtectTrapLoopDetectEnable = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectTrapLoopDetectEnable.setStatus('current')
arubaWiredLoopProtectEnableTimer = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectEnableTimer.setStatus('current')
arubaWiredLoopProtectMode = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port", 1), ("vlan", 2))).clone('port')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectMode.setStatus('current')
arubaWiredLoopProtectVIDList = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 5), VidList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectVIDList.setStatus('current')
arubaWiredLoopProtectPortTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1), )
if mibBuilder.loadTexts: arubaWiredLoopProtectPortTable.setStatus('current')
arubaWiredLoopProtectPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1), ).setIndexNames((0, "ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortInterfaceIndex"))
if mibBuilder.loadTexts: arubaWiredLoopProtectPortEntry.setStatus('current')
arubaWiredLoopProtectPortInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: arubaWiredLoopProtectPortInterfaceIndex.setStatus('current')
arubaWiredLoopProtectPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortEnable.setStatus('current')
arubaWiredLoopProtectPortLoopDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLoopDetected.setStatus('current')
arubaWiredLoopProtectPortLastLoopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLastLoopTime.setStatus('current')
arubaWiredLoopProtectPortLoopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLoopCount.setStatus('current')
arubaWiredLoopProtectPortReceiverAction = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 6), LoopProtectReceiverAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortReceiverAction.setStatus('current')
arubaWiredLoopProtectLoopDetectedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectLoopDetectedVlan.setStatus('current')
arubaWiredLoopProtectPortVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 8), VidList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortVlanList.setStatus('current')
arubaWiredLoopProtectLoopDetectedNotification = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"))
if mibBuilder.loadTexts: arubaWiredLoopProtectLoopDetectedNotification.setStatus('current')
arubaWiredLoopProtectVlanLoopDetectedNotification = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedVlan"))
if mibBuilder.loadTexts: arubaWiredLoopProtectVlanLoopDetectedNotification.setStatus('current')
arubaWiredLoopProtectConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3))
arubaWiredLoopProtectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1))
arubaWiredLoopProtectCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 2))
arubaWiredLoopProtectBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 4)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectInterval"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectEnableTimer"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectTrapLoopDetectEnable"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortEnable"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopDetected"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLastLoopTime"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectBaseGroup = arubaWiredLoopProtectBaseGroup.setStatus('current')
arubaWiredLoopProtectVLANGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 10)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectMode"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectVIDList"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedVlan"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortVlanList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectVLANGroup = arubaWiredLoopProtectVLANGroup.setStatus('current')
arubaWiredLoopProtectNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 11)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedNotification"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectVlanLoopDetectedNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectNotificationsGroup = arubaWiredLoopProtectNotificationsGroup.setStatus('current')
arubaWiredLoopProtectCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 2, 5)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectBaseGroup"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectNotificationsGroup"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectVLANGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectCompliance = arubaWiredLoopProtectCompliance.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-LOOPPROTECT-MIB", arubaWiredLoopProtectGroups=arubaWiredLoopProtectGroups, arubaWiredLoopProtectNotifications=arubaWiredLoopProtectNotifications, VidList=VidList, arubaWiredLoopProtectCompliances=arubaWiredLoopProtectCompliances, arubaWiredLoopProtectPortLoopCount=arubaWiredLoopProtectPortLoopCount, LoopProtectReceiverAction=LoopProtectReceiverAction, arubaWiredLoopProtectBase=arubaWiredLoopProtectBase, arubaWiredLoopProtectNotificationsGroup=arubaWiredLoopProtectNotificationsGroup, arubaWiredLoopProtectMode=arubaWiredLoopProtectMode, arubaWiredLoopProtectLoopDetectedVlan=arubaWiredLoopProtectLoopDetectedVlan, arubaWiredLoopProtectMIB=arubaWiredLoopProtectMIB, arubaWiredLoopProtectPortInterfaceIndex=arubaWiredLoopProtectPortInterfaceIndex, arubaWiredLoopProtectCompliance=arubaWiredLoopProtectCompliance, arubaWiredLoopProtectPortVlanList=arubaWiredLoopProtectPortVlanList, ConfigStatus=ConfigStatus, arubaWiredLoopProtectPortReceiverAction=arubaWiredLoopProtectPortReceiverAction, arubaWiredLoopProtectPortEntry=arubaWiredLoopProtectPortEntry, PYSNMP_MODULE_ID=arubaWiredLoopProtectMIB, arubaWiredLoopProtectPortEnable=arubaWiredLoopProtectPortEnable, arubaWiredLoopProtect=arubaWiredLoopProtect, arubaWiredLoopProtectObjects=arubaWiredLoopProtectObjects, arubaWiredLoopProtectVIDList=arubaWiredLoopProtectVIDList, arubaWiredLoopProtectEnableTimer=arubaWiredLoopProtectEnableTimer, arubaWiredLoopProtectVlanLoopDetectedNotification=arubaWiredLoopProtectVlanLoopDetectedNotification, arubaWiredLoopProtectBaseGroup=arubaWiredLoopProtectBaseGroup, arubaWiredLoopProtectPortLastLoopTime=arubaWiredLoopProtectPortLastLoopTime, arubaWiredLoopProtectConformance=arubaWiredLoopProtectConformance, arubaWiredLoopProtectVLANGroup=arubaWiredLoopProtectVLANGroup, arubaWiredLoopProtectPortTable=arubaWiredLoopProtectPortTable, arubaWiredLoopProtectLoopDetectedNotification=arubaWiredLoopProtectLoopDetectedNotification, arubaWiredLoopProtectTrapLoopDetectEnable=arubaWiredLoopProtectTrapLoopDetectEnable, arubaWiredLoopProtectPort=arubaWiredLoopProtectPort, arubaWiredLoopProtectPortLoopDetected=arubaWiredLoopProtectPortLoopDetected, arubaWiredLoopProtectInterval=arubaWiredLoopProtectInterval)
