#
# PySNMP MIB module DC-OAM-MPLS-MP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/DC-OAM-MPLS-MP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
AdminStatus, NumericIndex, BaseOperStatus = mibBuilder.importSymbols("DC-MASTER-TC", "AdminStatus", "NumericIndex", "BaseOperStatus")
oammEntApplIndex, = mibBuilder.importSymbols("DC-OAMM-MIB", "oammEntApplIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
mplsMpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 10, 16))
mplsMpMib.setRevisions(('2014-12-21 00:00',))
if mibBuilder.loadTexts: mplsMpMib.setLastUpdated('201412210000Z')
if mibBuilder.loadTexts: mplsMpMib.setOrganization('MRV Communications.')
nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
opx = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 10))
mplsMpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 10, 16, 1))
mplsMpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 10, 16, 2))
mplsMpTable = MibTable((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2), )
if mibBuilder.loadTexts: mplsMpTable.setStatus('current')
mplsMpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1), ).setIndexNames((0, "DC-OAMM-MIB", "oammEntApplIndex"), (0, "DC-OAM-MPLS-MP-MIB", "mplsMpIndex"))
if mibBuilder.loadTexts: mplsMpEntry.setStatus('current')
mplsMpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 1), NumericIndex())
if mibBuilder.loadTexts: mplsMpIndex.setStatus('current')
mplsMpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsMpRowStatus.setStatus('current')
mplsMpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 3), AdminStatus().clone('adminStatusUp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsMpAdminStatus.setStatus('current')
mplsMpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 4), BaseOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsMpOperStatus.setStatus('current')
mplsMpProactiveBfdContCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsMpProactiveBfdContCheck.setStatus('current')
mplsMpProactiveBfdConnVerif = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsMpProactiveBfdConnVerif.setStatus('current')
mplsMpLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 100), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsMpLoopback.setStatus('current')
mplsMpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 1))
mplsMpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 2))
mplsMpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 2, 1)).setObjects(("DC-OAM-MPLS-MP-MIB", "mplsMpGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsMpModuleFullCompliance = mplsMpModuleFullCompliance.setStatus('current')
mplsMpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 2, 2)).setObjects(("DC-OAM-MPLS-MP-MIB", "mplsMpGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsMpModuleReadOnlyCompliance = mplsMpModuleReadOnlyCompliance.setStatus('current')
mplsMpGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 1, 1)).setObjects(("DC-OAM-MPLS-MP-MIB", "mplsMpRowStatus"), ("DC-OAM-MPLS-MP-MIB", "mplsMpAdminStatus"), ("DC-OAM-MPLS-MP-MIB", "mplsMpOperStatus"), ("DC-OAM-MPLS-MP-MIB", "mplsMpProactiveBfdContCheck"), ("DC-OAM-MPLS-MP-MIB", "mplsMpProactiveBfdConnVerif"), ("DC-OAM-MPLS-MP-MIB", "mplsMpLoopback"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsMpGeneralGroup = mplsMpGeneralGroup.setStatus('current')
mibBuilder.exportSymbols("DC-OAM-MPLS-MP-MIB", nbase=nbase, mplsMpObjects=mplsMpObjects, mplsMpModuleFullCompliance=mplsMpModuleFullCompliance, mplsMpMib=mplsMpMib, mplsMpRowStatus=mplsMpRowStatus, mplsMpConformance=mplsMpConformance, mplsMpGroups=mplsMpGroups, mplsMpLoopback=mplsMpLoopback, mplsMpEntry=mplsMpEntry, mplsMpIndex=mplsMpIndex, mplsMpGeneralGroup=mplsMpGeneralGroup, mplsMpProactiveBfdConnVerif=mplsMpProactiveBfdConnVerif, PYSNMP_MODULE_ID=mplsMpMib, mplsMpOperStatus=mplsMpOperStatus, mplsMpModuleReadOnlyCompliance=mplsMpModuleReadOnlyCompliance, mplsMpAdminStatus=mplsMpAdminStatus, opx=opx, mplsMpTable=mplsMpTable, mplsMpProactiveBfdContCheck=mplsMpProactiveBfdContCheck, mplsMpCompliances=mplsMpCompliances)
