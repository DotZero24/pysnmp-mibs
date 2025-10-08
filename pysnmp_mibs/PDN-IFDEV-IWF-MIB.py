#
# PySNMP MIB module PDN-IFDEV-IWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-IFDEV-IWF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnIfDevIwfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27))
pdnIfDevIwfMIB.setRevisions(('2004-09-10 00:00',))
if mibBuilder.loadTexts: pdnIfDevIwfMIB.setLastUpdated('200409100000Z')
if mibBuilder.loadTexts: pdnIfDevIwfMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnIfDevIwfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 0))
pdnIfDevIwfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1))
pdnIfDevIwfAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 2))
pdnIfDevIwfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3))
class TxRxUnit(TextualConvention, Integer32):
    reference = "RFC 1662, Section 1.2, `Terminology'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("bits", 2), ("octets", 3), ("frames", 4), ("packets", 5), ("datagrams", 6))

pdnIfDevIwfStatsTotalTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1), )
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalTable.setStatus('current')
pdnIfDevIwfStatsTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalEntry.setStatus('current')
pdnIfDevIwfStatsTotalBufferUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalBufferUnderruns.setStatus('current')
pdnIfDevIwfStatsTotalMRUErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalMRUErrors.setStatus('current')
pdnIfDevIwfStatsTotalRxUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 3), TxRxUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRxUnit.setStatus('current')
pdnIfDevIwfStatsTotalRx = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRx.setStatus('current')
pdnIfDevIwfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 1))
pdnIfDevIwfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2))
pdnIfDevIwfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 1, 1)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalBufferUnderrunsGroup"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalMRUErrorsGroup"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfCompliance = pdnIfDevIwfCompliance.setStatus('current')
pdnIfDevIwfObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1))
pdnIfDevIwfAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 2))
pdnIfDevIwfNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 3))
pdnIfDevIwfStatsTotalBufferUnderrunsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 1)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalBufferUnderruns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalBufferUnderrunsGroup = pdnIfDevIwfStatsTotalBufferUnderrunsGroup.setStatus('current')
pdnIfDevIwfStatsTotalMRUErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 2)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalMRUErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalMRUErrorsGroup = pdnIfDevIwfStatsTotalMRUErrorsGroup.setStatus('current')
pdnIfDevIwfStatsTotalRxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 3)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRxUnit"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalRxGroup = pdnIfDevIwfStatsTotalRxGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-IFDEV-IWF-MIB", pdnIfDevIwfGroups=pdnIfDevIwfGroups, pdnIfDevIwfStatsTotalRxGroup=pdnIfDevIwfStatsTotalRxGroup, pdnIfDevIwfStatsTotalEntry=pdnIfDevIwfStatsTotalEntry, pdnIfDevIwfCompliances=pdnIfDevIwfCompliances, PYSNMP_MODULE_ID=pdnIfDevIwfMIB, pdnIfDevIwfConformance=pdnIfDevIwfConformance, pdnIfDevIwfStatsTotalRx=pdnIfDevIwfStatsTotalRx, pdnIfDevIwfCompliance=pdnIfDevIwfCompliance, pdnIfDevIwfStatsTotalBufferUnderrunsGroup=pdnIfDevIwfStatsTotalBufferUnderrunsGroup, TxRxUnit=TxRxUnit, pdnIfDevIwfObjects=pdnIfDevIwfObjects, pdnIfDevIwfStatsTotalBufferUnderruns=pdnIfDevIwfStatsTotalBufferUnderruns, pdnIfDevIwfAfnGroups=pdnIfDevIwfAfnGroups, pdnIfDevIwfStatsTotalTable=pdnIfDevIwfStatsTotalTable, pdnIfDevIwfAFNs=pdnIfDevIwfAFNs, pdnIfDevIwfStatsTotalMRUErrorsGroup=pdnIfDevIwfStatsTotalMRUErrorsGroup, pdnIfDevIwfStatsTotalMRUErrors=pdnIfDevIwfStatsTotalMRUErrors, pdnIfDevIwfNtfyGroups=pdnIfDevIwfNtfyGroups, pdnIfDevIwfNotifications=pdnIfDevIwfNotifications, pdnIfDevIwfMIB=pdnIfDevIwfMIB, pdnIfDevIwfStatsTotalRxUnit=pdnIfDevIwfStatsTotalRxUnit, pdnIfDevIwfObjGroups=pdnIfDevIwfObjGroups)
