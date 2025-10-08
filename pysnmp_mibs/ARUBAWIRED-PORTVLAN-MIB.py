#
# PySNMP MIB module ARUBAWIRED-PORTVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-PORTVLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredPortVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18))
arubaWiredPortVlanMIB.setRevisions(('2021-10-14 00:00', '2020-11-20 00:00',))
if mibBuilder.loadTexts: arubaWiredPortVlanMIB.setLastUpdated('202110140000Z')
if mibBuilder.loadTexts: arubaWiredPortVlanMIB.setOrganization('HPE/Aruba Networking Division')
class VidList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(512, 512)
    fixedLength = 512

arubaWiredPortVlanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 0))
arubaWiredPortVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1))
arubaWiredPortVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 0))
arubaWiredPortVlanStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1))
arubaWiredPortVlanMemberTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1), )
if mibBuilder.loadTexts: arubaWiredPortVlanMemberTable.setStatus('current')
arubaWiredPortVlanMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1, 1), ).setIndexNames((0, "ARUBAWIRED-PORTVLAN-MIB", "arubaWiredPortVlanMemberIndex"))
if mibBuilder.loadTexts: arubaWiredPortVlanMemberEntry.setStatus('current')
arubaWiredPortVlanMemberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: arubaWiredPortVlanMemberIndex.setStatus('current')
arubaWiredPortVlanMemberMode = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trunk", 1), ("access", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredPortVlanMemberMode.setStatus('current')
arubaWiredPortVlanMemberVid = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1, 1, 3), VidList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredPortVlanMemberVid.setStatus('current')
arubaWiredPortVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2))
arubaWiredPortVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2, 1))
arubaWiredPortVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2, 2))
arubaWiredPortVlanMemberTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2, 2, 1)).setObjects(("ARUBAWIRED-PORTVLAN-MIB", "arubaWiredPortVlanMemberMode"), ("ARUBAWIRED-PORTVLAN-MIB", "arubaWiredPortVlanMemberVid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredPortVlanMemberTableGroup = arubaWiredPortVlanMemberTableGroup.setStatus('current')
arubaWiredPortVlanMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2, 1, 1)).setObjects(("ARUBAWIRED-PORTVLAN-MIB", "arubaWiredPortVlanMemberTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredPortVlanMibCompliance = arubaWiredPortVlanMibCompliance.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-PORTVLAN-MIB", arubaWiredPortVlanGroups=arubaWiredPortVlanGroups, PYSNMP_MODULE_ID=arubaWiredPortVlanMIB, arubaWiredPortVlanMemberIndex=arubaWiredPortVlanMemberIndex, arubaWiredPortVlanStatus=arubaWiredPortVlanStatus, arubaWiredPortVlanMemberTableGroup=arubaWiredPortVlanMemberTableGroup, VidList=VidList, arubaWiredPortVlanMemberTable=arubaWiredPortVlanMemberTable, arubaWiredPortVlanNotifications=arubaWiredPortVlanNotifications, arubaWiredPortVlanMemberMode=arubaWiredPortVlanMemberMode, arubaWiredPortVlanMibCompliance=arubaWiredPortVlanMibCompliance, arubaWiredPortVlanMIB=arubaWiredPortVlanMIB, arubaWiredPortVlanCompliances=arubaWiredPortVlanCompliances, arubaWiredPortVlanMemberEntry=arubaWiredPortVlanMemberEntry, arubaWiredPortVlanMemberVid=arubaWiredPortVlanMemberVid, arubaWiredPortVlanConfig=arubaWiredPortVlanConfig, arubaWiredPortVlanObjects=arubaWiredPortVlanObjects, arubaWiredPortVlanConformance=arubaWiredPortVlanConformance)
