#
# PySNMP MIB module DCP-LINKVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/smartoptics/DCP-LINKVIEW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dcpGeneric, = mibBuilder.importSymbols("DCP-MIB", "dcpGeneric")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
InterfaceStatus, OpticalPower1Decimal = mibBuilder.importSymbols("SO-TC-MIB", "InterfaceStatus", "OpticalPower1Decimal")
dcpLinkview = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3))
dcpLinkview.setRevisions(('2021-02-25 12:00', '2018-10-08 14:44',))
if mibBuilder.loadTexts: dcpLinkview.setLastUpdated('202102251200Z')
if mibBuilder.loadTexts: dcpLinkview.setOrganization('Smartoptics.')
class DcpFiberLoss(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class DcpFiberAttenuation(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 10)

class DcpFiberLength(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 500)

dcpLinkviewObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1))
dcpLinkviewTable = MibTable((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1), )
if mibBuilder.loadTexts: dcpLinkviewTable.setStatus('current')
dcpLinkviewEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1), ).setIndexNames((0, "DCP-LINKVIEW-MIB", "dcpLinkviewIndex"))
if mibBuilder.loadTexts: dcpLinkviewEntry.setStatus('current')
dcpLinkviewIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000)))
if mibBuilder.loadTexts: dcpLinkviewIndex.setStatus('current')
dcpLinkviewLocalHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewLocalHostname.setStatus('current')
dcpLinkviewLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewLocalName.setStatus('current')
dcpLinkviewLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 4), InterfaceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewLocalStatus.setStatus('current')
dcpLinkviewLocalPower = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 5), OpticalPower1Decimal()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewLocalPower.setStatus('current')
dcpLinkviewFiberLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 6), DcpFiberLoss()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewFiberLoss.setStatus('current')
dcpLinkviewFiberAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 7), DcpFiberAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewFiberAttenuation.setStatus('current')
dcpLinkviewFiberLength = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 8), DcpFiberLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewFiberLength.setStatus('current')
dcpLinkviewFiberDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewFiberDispersion.setStatus('current')
dcpLinkviewFiberType = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewFiberType.setStatus('current')
dcpLinkviewFiberDispComp = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-10000, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewFiberDispComp.setStatus('current')
dcpLinkviewFiberDispFinal = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-10000, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewFiberDispFinal.setStatus('current')
dcpLinkviewFiberUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewFiberUtilization.setStatus('current')
dcpLinkviewRemotePower = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 14), OpticalPower1Decimal()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewRemotePower.setStatus('current')
dcpLinkviewRemoteName = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewRemoteName.setStatus('current')
dcpLinkviewRemoteHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpLinkviewRemoteHostname.setStatus('current')
dcpLinkviewMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2))
dcpLinkviewMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2, 1))
dcpLinkviewTableGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2, 1, 1)).setObjects(("DCP-LINKVIEW-MIB", "dcpLinkviewLocalHostname"), ("DCP-LINKVIEW-MIB", "dcpLinkviewLocalName"), ("DCP-LINKVIEW-MIB", "dcpLinkviewLocalStatus"), ("DCP-LINKVIEW-MIB", "dcpLinkviewLocalPower"), ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberLoss"), ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberAttenuation"), ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberLength"), ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberDispersion"), ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberType"), ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberDispComp"), ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberDispFinal"), ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberUtilization"), ("DCP-LINKVIEW-MIB", "dcpLinkviewRemotePower"), ("DCP-LINKVIEW-MIB", "dcpLinkviewRemoteName"), ("DCP-LINKVIEW-MIB", "dcpLinkviewRemoteHostname"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcpLinkviewTableGroupV1 = dcpLinkviewTableGroupV1.setStatus('current')
dcpLinkviewMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2, 2))
dcpLinkviewBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2, 2, 1)).setObjects(("DCP-LINKVIEW-MIB", "dcpLinkviewTableGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcpLinkviewBasicComplV1 = dcpLinkviewBasicComplV1.setStatus('current')
mibBuilder.exportSymbols("DCP-LINKVIEW-MIB", dcpLinkviewMIBGroups=dcpLinkviewMIBGroups, DcpFiberLength=DcpFiberLength, dcpLinkviewFiberUtilization=dcpLinkviewFiberUtilization, PYSNMP_MODULE_ID=dcpLinkview, DcpFiberLoss=DcpFiberLoss, dcpLinkviewLocalPower=dcpLinkviewLocalPower, dcpLinkviewFiberLoss=dcpLinkviewFiberLoss, dcpLinkviewBasicComplV1=dcpLinkviewBasicComplV1, dcpLinkviewFiberType=dcpLinkviewFiberType, dcpLinkviewTableGroupV1=dcpLinkviewTableGroupV1, dcpLinkviewFiberAttenuation=dcpLinkviewFiberAttenuation, DcpFiberAttenuation=DcpFiberAttenuation, dcpLinkviewIndex=dcpLinkviewIndex, dcpLinkviewMIBCompliances=dcpLinkviewMIBCompliances, dcpLinkviewFiberLength=dcpLinkviewFiberLength, dcpLinkviewRemoteName=dcpLinkviewRemoteName, dcpLinkview=dcpLinkview, dcpLinkviewLocalHostname=dcpLinkviewLocalHostname, dcpLinkviewObjects=dcpLinkviewObjects, dcpLinkviewEntry=dcpLinkviewEntry, dcpLinkviewFiberDispComp=dcpLinkviewFiberDispComp, dcpLinkviewLocalName=dcpLinkviewLocalName, dcpLinkviewFiberDispersion=dcpLinkviewFiberDispersion, dcpLinkviewFiberDispFinal=dcpLinkviewFiberDispFinal, dcpLinkviewRemoteHostname=dcpLinkviewRemoteHostname, dcpLinkviewRemotePower=dcpLinkviewRemotePower, dcpLinkviewTable=dcpLinkviewTable, dcpLinkviewMIBCompliance=dcpLinkviewMIBCompliance, dcpLinkviewLocalStatus=dcpLinkviewLocalStatus)
