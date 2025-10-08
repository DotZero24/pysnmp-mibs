#
# PySNMP MIB module ARUBAWIRED-CIPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-CIPT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
MacAddress, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention")
arubaWiredCiptMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12))
arubaWiredCiptMIB.setRevisions(('2020-02-07 00:00',))
if mibBuilder.loadTexts: arubaWiredCiptMIB.setLastUpdated('202002070000Z')
if mibBuilder.loadTexts: arubaWiredCiptMIB.setOrganization('HPE/Aruba Networking Division')
class VidList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '512x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(512, 512)
    fixedLength = 512

arubaWiredCiptConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1))
arubaWiredCiptClients = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2))
arubaWiredCiptGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 1))
arubaWiredCiptEnable = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredCiptEnable.setStatus('current')
arubaWiredCiptProbeEnable = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredCiptProbeEnable.setStatus('current')
arubaWiredCiptVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 2))
arubaWiredCiptVidList = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 2, 1), VidList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredCiptVidList.setStatus('current')
arubaWiredCiptPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3))
arubaWiredCiptPortTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1), )
if mibBuilder.loadTexts: arubaWiredCiptPortTable.setStatus('current')
arubaWiredCiptPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1), ).setIndexNames((0, "ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortIfIndex"))
if mibBuilder.loadTexts: arubaWiredCiptPortEntry.setStatus('current')
arubaWiredCiptPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: arubaWiredCiptPortIfIndex.setStatus('current')
arubaWiredCiptPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1), ("auto", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredCiptPortEnable.setStatus('current')
arubaWiredCiptPortUpdateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 28800))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredCiptPortUpdateInterval.setStatus('current')
arubaWiredCiptPortClientLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredCiptPortClientLimit.setStatus('current')
arubaWiredCiptTrackedClients = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1))
arubaWiredCiptClientTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1), )
if mibBuilder.loadTexts: arubaWiredCiptClientTable.setStatus('current')
arubaWiredCiptClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1), ).setIndexNames((0, "ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientMacAddress"), (0, "ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientVlanId"), (0, "ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientIpIndex"))
if mibBuilder.loadTexts: arubaWiredCiptClientEntry.setStatus('current')
arubaWiredCiptClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: arubaWiredCiptClientMacAddress.setStatus('current')
arubaWiredCiptClientVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 2), VlanIndex())
if mibBuilder.loadTexts: arubaWiredCiptClientVlanId.setStatus('current')
arubaWiredCiptClientIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: arubaWiredCiptClientIpIndex.setStatus('current')
arubaWiredCiptClientIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredCiptClientIpAddrType.setStatus('current')
arubaWiredCiptClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredCiptClientIpAddress.setStatus('current')
arubaWiredCiptClientPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredCiptClientPortIfIndex.setStatus('current')
arubaWiredCiptConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3))
arubaWiredCiptGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1))
arubaWiredCiptCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 2))
arubaWiredCiptConfigGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1, 1)).setObjects(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptEnable"), ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptProbeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredCiptConfigGlobalGroup = arubaWiredCiptConfigGlobalGroup.setStatus('current')
arubaWiredCiptVlanConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1, 2)).setObjects(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptVidList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredCiptVlanConfigGroup = arubaWiredCiptVlanConfigGroup.setStatus('current')
arubaWiredCiptPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1, 3)).setObjects(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortEnable"), ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortUpdateInterval"), ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortClientLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredCiptPortConfigGroup = arubaWiredCiptPortConfigGroup.setStatus('current')
arubaWiredCiptTrackedClientsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1, 4)).setObjects(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientIpAddrType"), ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientIpAddress"), ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientPortIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredCiptTrackedClientsGroup = arubaWiredCiptTrackedClientsGroup.setStatus('current')
arubaWiredCiptCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 2, 1)).setObjects(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptConfigGlobalGroup"), ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptVlanConfigGroup"), ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortConfigGroup"), ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptTrackedClientsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredCiptCompliance = arubaWiredCiptCompliance.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-CIPT-MIB", arubaWiredCiptProbeEnable=arubaWiredCiptProbeEnable, arubaWiredCiptClientTable=arubaWiredCiptClientTable, arubaWiredCiptClientIpAddress=arubaWiredCiptClientIpAddress, arubaWiredCiptConfig=arubaWiredCiptConfig, arubaWiredCiptVidList=arubaWiredCiptVidList, arubaWiredCiptPortUpdateInterval=arubaWiredCiptPortUpdateInterval, arubaWiredCiptClientPortIfIndex=arubaWiredCiptClientPortIfIndex, arubaWiredCiptClientMacAddress=arubaWiredCiptClientMacAddress, arubaWiredCiptConfigGlobalGroup=arubaWiredCiptConfigGlobalGroup, arubaWiredCiptPortEntry=arubaWiredCiptPortEntry, arubaWiredCiptPortTable=arubaWiredCiptPortTable, arubaWiredCiptPortConfigGroup=arubaWiredCiptPortConfigGroup, arubaWiredCiptClients=arubaWiredCiptClients, arubaWiredCiptVlanConfigGroup=arubaWiredCiptVlanConfigGroup, arubaWiredCiptEnable=arubaWiredCiptEnable, arubaWiredCiptClientIpAddrType=arubaWiredCiptClientIpAddrType, arubaWiredCiptClientEntry=arubaWiredCiptClientEntry, arubaWiredCiptGlobalConfig=arubaWiredCiptGlobalConfig, arubaWiredCiptPortEnable=arubaWiredCiptPortEnable, arubaWiredCiptMIB=arubaWiredCiptMIB, arubaWiredCiptClientVlanId=arubaWiredCiptClientVlanId, arubaWiredCiptVlanConfig=arubaWiredCiptVlanConfig, arubaWiredCiptPortConfig=arubaWiredCiptPortConfig, PYSNMP_MODULE_ID=arubaWiredCiptMIB, arubaWiredCiptPortIfIndex=arubaWiredCiptPortIfIndex, arubaWiredCiptCompliance=arubaWiredCiptCompliance, arubaWiredCiptConformance=arubaWiredCiptConformance, VidList=VidList, arubaWiredCiptTrackedClients=arubaWiredCiptTrackedClients, arubaWiredCiptClientIpIndex=arubaWiredCiptClientIpIndex, arubaWiredCiptCompliances=arubaWiredCiptCompliances, arubaWiredCiptPortClientLimit=arubaWiredCiptPortClientLimit, arubaWiredCiptTrackedClientsGroup=arubaWiredCiptTrackedClientsGroup, arubaWiredCiptGroups=arubaWiredCiptGroups)
