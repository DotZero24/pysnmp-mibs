#
# PySNMP MIB module MPLS-LC-FR-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/MPLS-LC-FR-STD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
DLCI, = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "DLCI")
mplsInterfaceIndex, = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInterfaceIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
mplsLcFrStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 10))
mplsLcFrStdMIB.setRevisions(('2006-01-12 00:00',))
if mibBuilder.loadTexts: mplsLcFrStdMIB.setLastUpdated('200601120000Z')
if mibBuilder.loadTexts: mplsLcFrStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
mplsLcFrStdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 0))
mplsLcFrStdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 1))
mplsLcFrStdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2))
mplsLcFrStdInterfaceConfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1), )
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfTable.setStatus('current')
mplsLcFrStdInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"))
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfEntry.setStatus('current')
mplsLcFrStdTrafficMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 1), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdTrafficMinDlci.setStatus('current')
mplsLcFrStdTrafficMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 2), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdTrafficMaxDlci.setStatus('current')
mplsLcFrStdCtrlMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 3), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdCtrlMinDlci.setStatus('current')
mplsLcFrStdCtrlMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 4), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdCtrlMaxDlci.setStatus('current')
mplsLcFrStdInterfaceConfRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfRowStatus.setStatus('current')
mplsLcFrStdInterfaceConfStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfStorageType.setStatus('current')
mplsLcFrStdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1))
mplsLcFrStdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2))
mplsLcFrStdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1, 1)).setObjects(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcFrStdModuleFullCompliance = mplsLcFrStdModuleFullCompliance.setStatus('current')
mplsLcFrStdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1, 2)).setObjects(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcFrStdModuleReadOnlyCompliance = mplsLcFrStdModuleReadOnlyCompliance.setStatus('current')
mplsLcFrStdIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2, 1)).setObjects(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdTrafficMinDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdTrafficMaxDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdCtrlMinDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdCtrlMaxDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdInterfaceConfRowStatus"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdInterfaceConfStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcFrStdIfGroup = mplsLcFrStdIfGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LC-FR-STD-MIB", PYSNMP_MODULE_ID=mplsLcFrStdMIB, mplsLcFrStdMIB=mplsLcFrStdMIB, mplsLcFrStdInterfaceConfRowStatus=mplsLcFrStdInterfaceConfRowStatus, mplsLcFrStdConformance=mplsLcFrStdConformance, mplsLcFrStdInterfaceConfTable=mplsLcFrStdInterfaceConfTable, mplsLcFrStdInterfaceConfStorageType=mplsLcFrStdInterfaceConfStorageType, mplsLcFrStdModuleReadOnlyCompliance=mplsLcFrStdModuleReadOnlyCompliance, mplsLcFrStdTrafficMaxDlci=mplsLcFrStdTrafficMaxDlci, mplsLcFrStdCtrlMinDlci=mplsLcFrStdCtrlMinDlci, mplsLcFrStdIfGroup=mplsLcFrStdIfGroup, mplsLcFrStdNotifications=mplsLcFrStdNotifications, mplsLcFrStdInterfaceConfEntry=mplsLcFrStdInterfaceConfEntry, mplsLcFrStdCompliances=mplsLcFrStdCompliances, mplsLcFrStdTrafficMinDlci=mplsLcFrStdTrafficMinDlci, mplsLcFrStdGroups=mplsLcFrStdGroups, mplsLcFrStdModuleFullCompliance=mplsLcFrStdModuleFullCompliance, mplsLcFrStdObjects=mplsLcFrStdObjects, mplsLcFrStdCtrlMaxDlci=mplsLcFrStdCtrlMaxDlci)
