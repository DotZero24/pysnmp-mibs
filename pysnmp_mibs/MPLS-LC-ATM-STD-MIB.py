#
# PySNMP MIB module MPLS-LC-ATM-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/MPLS-LC-ATM-STD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
AtmVpIdentifier, = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier")
mplsInterfaceIndex, = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInterfaceIndex")
MplsAtmVcIdentifier, mplsStdMIB = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsAtmVcIdentifier", "mplsStdMIB")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, StorageType, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "StorageType", "TruthValue", "DisplayString")
mplsLcAtmStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 9))
mplsLcAtmStdMIB.setRevisions(('2006-01-12 00:00',))
if mibBuilder.loadTexts: mplsLcAtmStdMIB.setLastUpdated('200601120000Z')
if mibBuilder.loadTexts: mplsLcAtmStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
mplsLcAtmStdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 0))
mplsLcAtmStdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 1))
mplsLcAtmStdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 2))
mplsLcAtmStdInterfaceConfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1), )
if mibBuilder.loadTexts: mplsLcAtmStdInterfaceConfTable.setStatus('current')
mplsLcAtmStdInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"))
if mibBuilder.loadTexts: mplsLcAtmStdInterfaceConfEntry.setStatus('current')
mplsLcAtmStdCtrlVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 1), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdCtrlVpi.setStatus('current')
mplsLcAtmStdCtrlVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 2), MplsAtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdCtrlVci.setStatus('current')
mplsLcAtmStdUnlabTrafVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 3), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdUnlabTrafVpi.setStatus('current')
mplsLcAtmStdUnlabTrafVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 4), MplsAtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdUnlabTrafVci.setStatus('current')
mplsLcAtmStdVcMerge = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdVcMerge.setStatus('current')
mplsLcAtmVcDirectlyConnected = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmVcDirectlyConnected.setStatus('current')
mplsLcAtmLcAtmVPI = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 7), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmLcAtmVPI.setStatus('current')
mplsLcAtmStdIfConfRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdIfConfRowStatus.setStatus('current')
mplsLcAtmStdIfConfStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdIfConfStorageType.setStatus('current')
mplsLcAtmStdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1))
mplsLcAtmStdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 2))
mplsLcAtmStdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1, 1)).setObjects(("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcAtmStdModuleFullCompliance = mplsLcAtmStdModuleFullCompliance.setStatus('current')
mplsLcAtmStdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1, 2)).setObjects(("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcAtmStdModuleReadOnlyCompliance = mplsLcAtmStdModuleReadOnlyCompliance.setStatus('current')
mplsLcAtmStdIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 2, 1)).setObjects(("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdCtrlVpi"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdCtrlVci"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdUnlabTrafVpi"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdUnlabTrafVci"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdVcMerge"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmVcDirectlyConnected"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmLcAtmVPI"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfConfRowStatus"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfConfStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcAtmStdIfGroup = mplsLcAtmStdIfGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LC-ATM-STD-MIB", mplsLcAtmStdCtrlVpi=mplsLcAtmStdCtrlVpi, mplsLcAtmStdModuleReadOnlyCompliance=mplsLcAtmStdModuleReadOnlyCompliance, mplsLcAtmLcAtmVPI=mplsLcAtmLcAtmVPI, mplsLcAtmStdObjects=mplsLcAtmStdObjects, mplsLcAtmStdInterfaceConfEntry=mplsLcAtmStdInterfaceConfEntry, mplsLcAtmStdNotifications=mplsLcAtmStdNotifications, mplsLcAtmStdVcMerge=mplsLcAtmStdVcMerge, mplsLcAtmStdInterfaceConfTable=mplsLcAtmStdInterfaceConfTable, mplsLcAtmStdIfConfStorageType=mplsLcAtmStdIfConfStorageType, mplsLcAtmStdIfGroup=mplsLcAtmStdIfGroup, mplsLcAtmStdModuleFullCompliance=mplsLcAtmStdModuleFullCompliance, mplsLcAtmStdConformance=mplsLcAtmStdConformance, mplsLcAtmStdUnlabTrafVci=mplsLcAtmStdUnlabTrafVci, PYSNMP_MODULE_ID=mplsLcAtmStdMIB, mplsLcAtmStdIfConfRowStatus=mplsLcAtmStdIfConfRowStatus, mplsLcAtmStdGroups=mplsLcAtmStdGroups, mplsLcAtmStdUnlabTrafVpi=mplsLcAtmStdUnlabTrafVpi, mplsLcAtmStdCompliances=mplsLcAtmStdCompliances, mplsLcAtmStdMIB=mplsLcAtmStdMIB, mplsLcAtmStdCtrlVci=mplsLcAtmStdCtrlVci, mplsLcAtmVcDirectlyConnected=mplsLcAtmVcDirectlyConnected)
