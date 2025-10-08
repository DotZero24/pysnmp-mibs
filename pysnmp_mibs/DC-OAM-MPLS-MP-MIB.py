#
# PySNMP MIB module DC-OAM-MPLS-MP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/DC-OAM-MPLS-MP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
AdminStatus, NumericIndex, BaseOperStatus = mibBuilder.importSymbols("DC-MASTER-TC", "AdminStatus", "NumericIndex", "BaseOperStatus")
oammEntApplIndex, = mibBuilder.importSymbols("DC-OAMM-MIB", "oammEntApplIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DC-OAM-MPLS-MP-MIB", mplsMpModuleReadOnlyCompliance=mplsMpModuleReadOnlyCompliance, mplsMpTable=mplsMpTable, mplsMpCompliances=mplsMpCompliances, mplsMpGeneralGroup=mplsMpGeneralGroup, mplsMpConformance=mplsMpConformance, mplsMpProactiveBfdConnVerif=mplsMpProactiveBfdConnVerif, mplsMpObjects=mplsMpObjects, mplsMpMib=mplsMpMib, PYSNMP_MODULE_ID=mplsMpMib, mplsMpAdminStatus=mplsMpAdminStatus, mplsMpProactiveBfdContCheck=mplsMpProactiveBfdContCheck, mplsMpIndex=mplsMpIndex, mplsMpEntry=mplsMpEntry, mplsMpLoopback=mplsMpLoopback, nbase=nbase, mplsMpRowStatus=mplsMpRowStatus, mplsMpModuleFullCompliance=mplsMpModuleFullCompliance, mplsMpOperStatus=mplsMpOperStatus, opx=opx, mplsMpGroups=mplsMpGroups)
