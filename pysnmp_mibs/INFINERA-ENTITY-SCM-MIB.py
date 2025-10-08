#
# PySNMP MIB module INFINERA-ENTITY-SCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-SCM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "FloatTenths")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
scmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18))
if mibBuilder.loadTexts: scmMIB.setLastUpdated('201005240000Z')
if mibBuilder.loadTexts: scmMIB.setOrganization('INFINERA')
scmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3))
scmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3, 1))
scmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3, 2))
scmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1), )
if mibBuilder.loadTexts: scmTable.setStatus('current')
scmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: scmEntry.setStatus('current')
scmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scmMoId.setStatus('current')
scmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scmProvEqptType.setStatus('current')
scmIdlerVoaAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 3), FloatTenths()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scmIdlerVoaAttenuation.setStatus('current')
scmProvisionedRemoteSCM = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scmProvisionedRemoteSCM.setStatus('current')
scmAssociatedDegree = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scmAssociatedDegree.setStatus('current')
scmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scmRowStatus.setStatus('current')
scmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3, 1, 1)).setObjects(("INFINERA-ENTITY-SCM-MIB", "scmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scmCompliance = scmCompliance.setStatus('current')
scmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3, 2, 1)).setObjects(("INFINERA-ENTITY-SCM-MIB", "scmMoId"), ("INFINERA-ENTITY-SCM-MIB", "scmProvEqptType"), ("INFINERA-ENTITY-SCM-MIB", "scmRowStatus"), ("INFINERA-ENTITY-SCM-MIB", "scmIdlerVoaAttenuation"), ("INFINERA-ENTITY-SCM-MIB", "scmProvisionedRemoteSCM"), ("INFINERA-ENTITY-SCM-MIB", "scmAssociatedDegree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scmGroup = scmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-SCM-MIB", scmAssociatedDegree=scmAssociatedDegree, PYSNMP_MODULE_ID=scmMIB, scmGroups=scmGroups, scmEntry=scmEntry, scmMoId=scmMoId, scmConformance=scmConformance, scmIdlerVoaAttenuation=scmIdlerVoaAttenuation, scmTable=scmTable, scmRowStatus=scmRowStatus, scmProvisionedRemoteSCM=scmProvisionedRemoteSCM, scmCompliances=scmCompliances, scmGroup=scmGroup, scmMIB=scmMIB, scmProvEqptType=scmProvEqptType, scmCompliance=scmCompliance)
