#
# PySNMP MIB module ELTEX-MES-ISS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
mcTrapDescr, = mibBuilder.importSymbols("ELTEX-SMI", "mcTrapDescr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltMesIssSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18))
eltMesIssSystemMIB.setRevisions(('2023-01-30 00:00', '2022-06-09 00:00', '2021-04-28 00:00', '2021-02-05 00:00', '2020-05-08 00:00', '2019-10-15 00:00',))
if mibBuilder.loadTexts: eltMesIssSystemMIB.setLastUpdated('202301300000Z')
if mibBuilder.loadTexts: eltMesIssSystemMIB.setOrganization('Eltex Enterprise, Ltd.')
class EltMesIssSysDelayedReloadMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("reloadIn", 1), ("reloadAt", 2), ("noReload", 3))

class EltMesIssSysImageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("image", 1), ("boot", 2), ("preloader", 3))

class EltMesIssSysImageState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

eltMesIssSysObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1))
eltMesIssSysNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 2))
eltMesIssSysGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1))
eltMesIssSysReloadParams = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 1))
eltMesIssSysLoggingParams = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 2))
eltMesIssSysBootVar = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3))
eltMesIssSysNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 2, 0))
eltMesIssDelayReloadTime = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssDelayReloadTime.setStatus('current')
eltMesIssDelayReloadAction = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 1, 2), EltMesIssSysDelayedReloadMode().clone('noReload')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssDelayReloadAction.setStatus('current')
eltMesIssSysClearDebugLogs = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSysClearDebugLogs.setStatus('current')
eltMesIssSysReloadRequestLoggingEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 2, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSysReloadRequestLoggingEnable.setStatus('current')
eltMesIssSysStartupType = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("coldstart", 0), ("warmstart", 1), ("undefined", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSysStartupType.setStatus('current')
eltMesIssSysBootVarTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1), )
if mibBuilder.loadTexts: eltMesIssSysBootVarTable.setStatus('current')
eltMesIssSysBootVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1), ).setIndexNames((0, "ELTEX-MES-ISS-SYSTEM-MIB", "eltMesIssSysBootVarImageType"), (0, "ELTEX-MES-ISS-SYSTEM-MIB", "eltMesIssSysBootVarImageState"))
if mibBuilder.loadTexts: eltMesIssSysBootVarEntry.setStatus('current')
eltMesIssSysBootVarImageType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 1), EltMesIssSysImageType())
if mibBuilder.loadTexts: eltMesIssSysBootVarImageType.setStatus('current')
eltMesIssSysBootVarImageState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 2), EltMesIssSysImageState())
if mibBuilder.loadTexts: eltMesIssSysBootVarImageState.setStatus('current')
eltMesIssSysBootVarValid = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSysBootVarValid.setStatus('current')
eltMesIssSysBootVarVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSysBootVarVersion.setStatus('current')
eltMesIssSysBootVarCommit = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSysBootVarCommit.setStatus('current')
eltMesIssSysBootVarBuild = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSysBootVarBuild.setStatus('current')
eltMesIssSysBootVarMd5Digest = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSysBootVarMd5Digest.setStatus('current')
eltMesIssSysBootVarTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSysBootVarTime.setStatus('current')
eltMesIssSysBootVarImageStateAfterReboot = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 9), EltMesIssSysImageState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSysBootVarImageStateAfterReboot.setStatus('current')
eltMesIssSysDescr = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSysDescr.setStatus('current')
eltMesIssSysReloadRequestTrap = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 2, 0, 1)).setObjects(("ELTEX-SMI", "mcTrapDescr"))
if mibBuilder.loadTexts: eltMesIssSysReloadRequestTrap.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-SYSTEM-MIB", eltMesIssSysBootVarCommit=eltMesIssSysBootVarCommit, eltMesIssSysBootVarImageStateAfterReboot=eltMesIssSysBootVarImageStateAfterReboot, eltMesIssSysBootVarTime=eltMesIssSysBootVarTime, eltMesIssSysBootVarImageType=eltMesIssSysBootVarImageType, eltMesIssDelayReloadAction=eltMesIssDelayReloadAction, eltMesIssSysBootVarImageState=eltMesIssSysBootVarImageState, eltMesIssDelayReloadTime=eltMesIssDelayReloadTime, eltMesIssSysDescr=eltMesIssSysDescr, EltMesIssSysImageType=EltMesIssSysImageType, eltMesIssSysBootVarValid=eltMesIssSysBootVarValid, eltMesIssSysBootVarEntry=eltMesIssSysBootVarEntry, eltMesIssSysBootVarTable=eltMesIssSysBootVarTable, EltMesIssSysImageState=EltMesIssSysImageState, eltMesIssSysReloadParams=eltMesIssSysReloadParams, eltMesIssSysBootVarVersion=eltMesIssSysBootVarVersion, eltMesIssSysNotificationsPrefix=eltMesIssSysNotificationsPrefix, eltMesIssSysLoggingParams=eltMesIssSysLoggingParams, eltMesIssSysReloadRequestTrap=eltMesIssSysReloadRequestTrap, eltMesIssSysReloadRequestLoggingEnable=eltMesIssSysReloadRequestLoggingEnable, eltMesIssSysStartupType=eltMesIssSysStartupType, eltMesIssSysNotifications=eltMesIssSysNotifications, eltMesIssSysBootVar=eltMesIssSysBootVar, eltMesIssSysClearDebugLogs=eltMesIssSysClearDebugLogs, eltMesIssSysObjects=eltMesIssSysObjects, EltMesIssSysDelayedReloadMode=EltMesIssSysDelayedReloadMode, eltMesIssSysBootVarMd5Digest=eltMesIssSysBootVarMd5Digest, eltMesIssSysGlobals=eltMesIssSysGlobals, eltMesIssSysBootVarBuild=eltMesIssSysBootVarBuild, PYSNMP_MODULE_ID=eltMesIssSystemMIB, eltMesIssSystemMIB=eltMesIssSystemMIB)
