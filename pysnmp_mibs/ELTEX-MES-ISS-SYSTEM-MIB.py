#
# PySNMP MIB module ELTEX-MES-ISS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
mcTrapDescr, = mibBuilder.importSymbols("ELTEX-SMI", "mcTrapDescr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-MES-ISS-SYSTEM-MIB", eltMesIssSysBootVarImageStateAfterReboot=eltMesIssSysBootVarImageStateAfterReboot, eltMesIssSysObjects=eltMesIssSysObjects, eltMesIssSysBootVarMd5Digest=eltMesIssSysBootVarMd5Digest, eltMesIssSysClearDebugLogs=eltMesIssSysClearDebugLogs, eltMesIssSysBootVarImageType=eltMesIssSysBootVarImageType, eltMesIssSysReloadRequestTrap=eltMesIssSysReloadRequestTrap, eltMesIssSysBootVarCommit=eltMesIssSysBootVarCommit, eltMesIssSysReloadRequestLoggingEnable=eltMesIssSysReloadRequestLoggingEnable, EltMesIssSysDelayedReloadMode=EltMesIssSysDelayedReloadMode, eltMesIssSysStartupType=eltMesIssSysStartupType, eltMesIssDelayReloadTime=eltMesIssDelayReloadTime, eltMesIssSysBootVarValid=eltMesIssSysBootVarValid, eltMesIssSysBootVarImageState=eltMesIssSysBootVarImageState, eltMesIssSysNotificationsPrefix=eltMesIssSysNotificationsPrefix, eltMesIssSysLoggingParams=eltMesIssSysLoggingParams, eltMesIssSysBootVarTime=eltMesIssSysBootVarTime, PYSNMP_MODULE_ID=eltMesIssSystemMIB, eltMesIssSysGlobals=eltMesIssSysGlobals, eltMesIssSysDescr=eltMesIssSysDescr, eltMesIssSystemMIB=eltMesIssSystemMIB, EltMesIssSysImageType=EltMesIssSysImageType, eltMesIssSysNotifications=eltMesIssSysNotifications, eltMesIssSysReloadParams=eltMesIssSysReloadParams, eltMesIssDelayReloadAction=eltMesIssDelayReloadAction, eltMesIssSysBootVarTable=eltMesIssSysBootVarTable, eltMesIssSysBootVarBuild=eltMesIssSysBootVarBuild, eltMesIssSysBootVarVersion=eltMesIssSysBootVarVersion, EltMesIssSysImageState=EltMesIssSysImageState, eltMesIssSysBootVar=eltMesIssSysBootVar, eltMesIssSysBootVarEntry=eltMesIssSysBootVarEntry)
