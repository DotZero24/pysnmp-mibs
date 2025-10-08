#
# PySNMP MIB module MPLS-LC-ATM-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/MPLS-LC-ATM-STD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
AtmVpIdentifier, = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier")
mplsInterfaceIndex, = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInterfaceIndex")
mplsStdMIB, MplsAtmVcIdentifier = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB", "MplsAtmVcIdentifier")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, StorageType, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("MPLS-LC-ATM-STD-MIB", mplsLcAtmStdUnlabTrafVpi=mplsLcAtmStdUnlabTrafVpi, mplsLcAtmStdUnlabTrafVci=mplsLcAtmStdUnlabTrafVci, mplsLcAtmStdCompliances=mplsLcAtmStdCompliances, mplsLcAtmStdCtrlVci=mplsLcAtmStdCtrlVci, mplsLcAtmLcAtmVPI=mplsLcAtmLcAtmVPI, mplsLcAtmStdIfConfStorageType=mplsLcAtmStdIfConfStorageType, mplsLcAtmStdIfGroup=mplsLcAtmStdIfGroup, mplsLcAtmStdMIB=mplsLcAtmStdMIB, mplsLcAtmStdInterfaceConfTable=mplsLcAtmStdInterfaceConfTable, mplsLcAtmStdIfConfRowStatus=mplsLcAtmStdIfConfRowStatus, mplsLcAtmStdNotifications=mplsLcAtmStdNotifications, mplsLcAtmStdVcMerge=mplsLcAtmStdVcMerge, mplsLcAtmStdInterfaceConfEntry=mplsLcAtmStdInterfaceConfEntry, mplsLcAtmStdObjects=mplsLcAtmStdObjects, mplsLcAtmStdModuleFullCompliance=mplsLcAtmStdModuleFullCompliance, mplsLcAtmStdCtrlVpi=mplsLcAtmStdCtrlVpi, PYSNMP_MODULE_ID=mplsLcAtmStdMIB, mplsLcAtmStdModuleReadOnlyCompliance=mplsLcAtmStdModuleReadOnlyCompliance, mplsLcAtmStdConformance=mplsLcAtmStdConformance, mplsLcAtmStdGroups=mplsLcAtmStdGroups, mplsLcAtmVcDirectlyConnected=mplsLcAtmVcDirectlyConnected)
