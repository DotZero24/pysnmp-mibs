#
# PySNMP MIB module PDN-PPP-ML-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-PPP-ML-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
PdnPPPState, SwitchState = mibBuilder.importSymbols("PDN-TC", "PdnPPPState", "SwitchState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
pdnPppMlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30))
pdnPppMlMIB.setRevisions(('2004-09-14 00:00',))
if mibBuilder.loadTexts: pdnPppMlMIB.setLastUpdated('200409140000Z')
if mibBuilder.loadTexts: pdnPppMlMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnPppMlNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 0))
pdnPppMlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1))
pdnPppMlAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 2))
pdnPppMlConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3))
class MRRU(TextualConvention, Unsigned32):
    reference = "RFC 1990, Section 5.1.1, `Multilink MRRU LCP Option'."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class SSNHF(TextualConvention, Integer32):
    reference = "RFC 1990, Section 5.1.2, `Short Sequence Number Header Option'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ssnhfUnknown", 1), ("ssnhf12BitSeqNbrs", 2), ("ssnhf24BitSeqNbrs", 3))

class EDClass(TextualConvention, Integer32):
    reference = "RFC 1990, Section 5.1.3, `Endpoint Discriminator Option'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("nullClass", 0), ("locallyAssigned", 1), ("ipAddr", 2), ("ieee802", 3), ("pppMagicNbrBlk", 4), ("publicSwNetDirNbr", 5))

pdnPppMlBundleNumber = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleNumber.setStatus('current')
pdnPppMlBundleConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2), )
if mibBuilder.loadTexts: pdnPppMlBundleConfigTable.setStatus('current')
pdnPppMlBundleConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1), ).setIndexNames((0, "PDN-PPP-ML-MIB", "pdnPppMlBundleIfIndex"))
if mibBuilder.loadTexts: pdnPppMlBundleConfigEntry.setStatus('current')
pdnPppMlBundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pdnPppMlBundleIfIndex.setStatus('current')
pdnPppMlBundleConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnPppMlBundleConfigRowStatus.setStatus('current')
pdnPppMlBundleConfigMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 3), MRRU()).setUnits('Number of octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnPppMlBundleConfigMRRU.setStatus('current')
pdnPppMlBundleConfigSSNHF = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 4), SwitchState()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnPppMlBundleConfigSSNHF.setStatus('current')
pdnPppMlBundleConfigFragmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967296))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnPppMlBundleConfigFragmentSize.setStatus('current')
pdnPppMlBundleMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 3), )
if mibBuilder.loadTexts: pdnPppMlBundleMappingTable.setStatus('current')
pdnPppMlBundleMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnPppMlBundleMappingEntry.setStatus('current')
pdnPppMlBundleMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnPppMlBundleMappingRowStatus.setStatus('current')
pdnPppMlBundleMappingBundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnPppMlBundleMappingBundleIfIndex.setStatus('current')
pdnPppMlBundleStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4), )
if mibBuilder.loadTexts: pdnPppMlBundleStatusTable.setStatus('current')
pdnPppMlBundleStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1), ).setIndexNames((0, "PDN-PPP-ML-MIB", "pdnPppMlBundleIfIndex"))
if mibBuilder.loadTexts: pdnPppMlBundleStatusEntry.setStatus('current')
pdnPppMlBundleStatusCurrState = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 1), PdnPPPState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusCurrState.setStatus('current')
pdnPppMlBundleStatusLocalToRemoteMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 2), MRRU()).setUnits('Number of octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusLocalToRemoteMRRU.setStatus('current')
pdnPppMlBundleStatusRemoteToLocalMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 3), MRRU()).setUnits('Number of octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusRemoteToLocalMRRU.setStatus('current')
pdnPppMlBundleStatusLocalToRemoteSSNHF = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 4), SSNHF()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusLocalToRemoteSSNHF.setStatus('current')
pdnPppMlBundleStatusRemoteToLocalSSNHF = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 5), SSNHF()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusRemoteToLocalSSNHF.setStatus('current')
pdnPppMlBundleStatusLocalToRemoteEDClass = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 6), EDClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusLocalToRemoteEDClass.setStatus('current')
pdnPppMlBundleStatusLocalToRemoteEDAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusLocalToRemoteEDAddr.setStatus('current')
pdnPppMlBundleStatusRemoteToLocalEDClass = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 8), EDClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusRemoteToLocalEDClass.setStatus('current')
pdnPppMlBundleStatusRemoteToLocalEDAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPppMlBundleStatusRemoteToLocalEDAddr.setStatus('current')
pdnPppMlCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 1))
pdnPppMlGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2))
pdnPppMlCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 1, 1)).setObjects(("PDN-PPP-ML-MIB", "pdnPppMlBundleDefinitionGroup"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleStateMachineGroup"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleMRRUGroup"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleSSNHFGroup"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleEDGroup"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleFragmentSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnPppMlCompliance = pdnPppMlCompliance.setStatus('current')
pdnPppMlObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1))
pdnPppMlAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 2))
pdnPppmlNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 3))
pdnPppMlBundleDefinitionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 1)).setObjects(("PDN-PPP-ML-MIB", "pdnPppMlBundleNumber"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigRowStatus"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleMappingBundleIfIndex"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleMappingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnPppMlBundleDefinitionGroup = pdnPppMlBundleDefinitionGroup.setStatus('current')
pdnPppMlBundleStateMachineGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 2)).setObjects(("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusCurrState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnPppMlBundleStateMachineGroup = pdnPppMlBundleStateMachineGroup.setStatus('current')
pdnPppMlBundleMRRUGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 3)).setObjects(("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigRowStatus"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigMRRU"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusLocalToRemoteMRRU"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusRemoteToLocalMRRU"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnPppMlBundleMRRUGroup = pdnPppMlBundleMRRUGroup.setStatus('current')
pdnPppMlBundleSSNHFGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 4)).setObjects(("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigRowStatus"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigSSNHF"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusLocalToRemoteSSNHF"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusRemoteToLocalSSNHF"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnPppMlBundleSSNHFGroup = pdnPppMlBundleSSNHFGroup.setStatus('current')
pdnPppMlBundleEDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 5)).setObjects(("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusLocalToRemoteEDClass"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusLocalToRemoteEDAddr"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusRemoteToLocalEDClass"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusRemoteToLocalEDAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnPppMlBundleEDGroup = pdnPppMlBundleEDGroup.setStatus('current')
pdnPppMlBundleFragmentSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 6)).setObjects(("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigRowStatus"), ("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigFragmentSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnPppMlBundleFragmentSizeGroup = pdnPppMlBundleFragmentSizeGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-PPP-ML-MIB", pdnPppMlBundleConfigEntry=pdnPppMlBundleConfigEntry, pdnPppMlBundleStatusEntry=pdnPppMlBundleStatusEntry, pdnPppMlBundleStatusLocalToRemoteSSNHF=pdnPppMlBundleStatusLocalToRemoteSSNHF, SSNHF=SSNHF, pdnPppMlBundleStatusRemoteToLocalSSNHF=pdnPppMlBundleStatusRemoteToLocalSSNHF, pdnPppMlBundleMappingRowStatus=pdnPppMlBundleMappingRowStatus, pdnPppMlBundleNumber=pdnPppMlBundleNumber, pdnPppMlObjects=pdnPppMlObjects, pdnPppMlBundleConfigSSNHF=pdnPppMlBundleConfigSSNHF, pdnPppMlBundleEDGroup=pdnPppMlBundleEDGroup, pdnPppMlBundleStatusLocalToRemoteMRRU=pdnPppMlBundleStatusLocalToRemoteMRRU, pdnPppMlBundleFragmentSizeGroup=pdnPppMlBundleFragmentSizeGroup, pdnPppMlBundleSSNHFGroup=pdnPppMlBundleSSNHFGroup, pdnPppMlObjGroups=pdnPppMlObjGroups, pdnPppMlBundleMRRUGroup=pdnPppMlBundleMRRUGroup, pdnPppMlBundleConfigRowStatus=pdnPppMlBundleConfigRowStatus, pdnPppMlCompliance=pdnPppMlCompliance, pdnPppMlBundleStatusTable=pdnPppMlBundleStatusTable, pdnPppMlBundleMappingEntry=pdnPppMlBundleMappingEntry, pdnPppMlAfnGroups=pdnPppMlAfnGroups, pdnPppMlAFNs=pdnPppMlAFNs, pdnPppMlBundleDefinitionGroup=pdnPppMlBundleDefinitionGroup, pdnPppMlConformance=pdnPppMlConformance, pdnPppMlBundleStatusCurrState=pdnPppMlBundleStatusCurrState, pdnPppMlBundleStatusRemoteToLocalMRRU=pdnPppMlBundleStatusRemoteToLocalMRRU, pdnPppMlBundleIfIndex=pdnPppMlBundleIfIndex, pdnPppMlBundleConfigMRRU=pdnPppMlBundleConfigMRRU, pdnPppMlBundleStatusLocalToRemoteEDClass=pdnPppMlBundleStatusLocalToRemoteEDClass, pdnPppMlBundleStatusRemoteToLocalEDClass=pdnPppMlBundleStatusRemoteToLocalEDClass, MRRU=MRRU, pdnPppMlCompliances=pdnPppMlCompliances, EDClass=EDClass, pdnPppMlBundleMappingBundleIfIndex=pdnPppMlBundleMappingBundleIfIndex, pdnPppMlBundleStatusLocalToRemoteEDAddr=pdnPppMlBundleStatusLocalToRemoteEDAddr, PYSNMP_MODULE_ID=pdnPppMlMIB, pdnPppMlMIB=pdnPppMlMIB, pdnPppMlNotifications=pdnPppMlNotifications, pdnPppmlNtfyGroups=pdnPppmlNtfyGroups, pdnPppMlBundleStateMachineGroup=pdnPppMlBundleStateMachineGroup, pdnPppMlGroups=pdnPppMlGroups, pdnPppMlBundleConfigFragmentSize=pdnPppMlBundleConfigFragmentSize, pdnPppMlBundleMappingTable=pdnPppMlBundleMappingTable, pdnPppMlBundleConfigTable=pdnPppMlBundleConfigTable, pdnPppMlBundleStatusRemoteToLocalEDAddr=pdnPppMlBundleStatusRemoteToLocalEDAddr)
