#
# PySNMP MIB module INFINERA-ENTITY-SCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-SCM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "FloatTenths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-SCM-MIB", scmGroup=scmGroup, scmConformance=scmConformance, scmAssociatedDegree=scmAssociatedDegree, scmRowStatus=scmRowStatus, scmGroups=scmGroups, scmIdlerVoaAttenuation=scmIdlerVoaAttenuation, scmCompliance=scmCompliance, PYSNMP_MODULE_ID=scmMIB, scmTable=scmTable, scmProvEqptType=scmProvEqptType, scmMoId=scmMoId, scmProvisionedRemoteSCM=scmProvisionedRemoteSCM, scmCompliances=scmCompliances, scmMIB=scmMIB, scmEntry=scmEntry)
