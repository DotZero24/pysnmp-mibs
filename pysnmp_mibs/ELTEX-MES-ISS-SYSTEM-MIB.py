_N='not-accessible'
_M='eltMesIssSysBootVarImageState'
_L='eltMesIssSysBootVarImageType'
_K='EltMesIssSysDelayedReloadMode'
_J='TruthValue'
_I='DisplayString'
_H='Integer32'
_G='mcTrapDescr'
_F='ELTEX-SMI'
_E='OctetString'
_D='ELTEX-MES-ISS-SYSTEM-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
mcTrapDescr,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention',_J)
eltMesIssSystemMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,18))
if mibBuilder.loadTexts:eltMesIssSystemMIB.setRevisions(('2023-01-30 00:00','2022-06-09 00:00','2021-04-28 00:00','2021-02-05 00:00','2020-05-08 00:00','2019-10-15 00:00'))
class EltMesIssSysDelayedReloadMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reloadIn',1),('reloadAt',2),('noReload',3)))
class EltMesIssSysImageType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('image',1),('boot',2),('preloader',3)))
class EltMesIssSysImageState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_EltMesIssSysObjects_ObjectIdentity=ObjectIdentity
eltMesIssSysObjects=_EltMesIssSysObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,18,1))
_EltMesIssSysGlobals_ObjectIdentity=ObjectIdentity
eltMesIssSysGlobals=_EltMesIssSysGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,18,1,1))
_EltMesIssSysReloadParams_ObjectIdentity=ObjectIdentity
eltMesIssSysReloadParams=_EltMesIssSysReloadParams_ObjectIdentity((1,3,6,1,4,1,35265,1,139,18,1,1,1))
class _EltMesIssDelayReloadTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_EltMesIssDelayReloadTime_Type.__name__=_E
_EltMesIssDelayReloadTime_Object=MibScalar
eltMesIssDelayReloadTime=_EltMesIssDelayReloadTime_Object((1,3,6,1,4,1,35265,1,139,18,1,1,1,1),_EltMesIssDelayReloadTime_Type())
eltMesIssDelayReloadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssDelayReloadTime.setStatus(_A)
class _EltMesIssDelayReloadAction_Type(EltMesIssSysDelayedReloadMode):defaultValue=3
_EltMesIssDelayReloadAction_Type.__name__=_K
_EltMesIssDelayReloadAction_Object=MibScalar
eltMesIssDelayReloadAction=_EltMesIssDelayReloadAction_Object((1,3,6,1,4,1,35265,1,139,18,1,1,1,2),_EltMesIssDelayReloadAction_Type())
eltMesIssDelayReloadAction.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssDelayReloadAction.setStatus(_A)
_EltMesIssSysLoggingParams_ObjectIdentity=ObjectIdentity
eltMesIssSysLoggingParams=_EltMesIssSysLoggingParams_ObjectIdentity((1,3,6,1,4,1,35265,1,139,18,1,1,2))
_EltMesIssSysClearDebugLogs_Type=TruthValue
_EltMesIssSysClearDebugLogs_Object=MibScalar
eltMesIssSysClearDebugLogs=_EltMesIssSysClearDebugLogs_Object((1,3,6,1,4,1,35265,1,139,18,1,1,2,1),_EltMesIssSysClearDebugLogs_Type())
eltMesIssSysClearDebugLogs.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssSysClearDebugLogs.setStatus(_A)
class _EltMesIssSysReloadRequestLoggingEnable_Type(TruthValue):defaultValue=1
_EltMesIssSysReloadRequestLoggingEnable_Type.__name__=_J
_EltMesIssSysReloadRequestLoggingEnable_Object=MibScalar
eltMesIssSysReloadRequestLoggingEnable=_EltMesIssSysReloadRequestLoggingEnable_Object((1,3,6,1,4,1,35265,1,139,18,1,1,2,2),_EltMesIssSysReloadRequestLoggingEnable_Type())
eltMesIssSysReloadRequestLoggingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssSysReloadRequestLoggingEnable.setStatus(_A)
class _EltMesIssSysStartupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('coldstart',0),('warmstart',1),('undefined',2)))
_EltMesIssSysStartupType_Type.__name__=_H
_EltMesIssSysStartupType_Object=MibScalar
eltMesIssSysStartupType=_EltMesIssSysStartupType_Object((1,3,6,1,4,1,35265,1,139,18,1,1,2,3),_EltMesIssSysStartupType_Type())
eltMesIssSysStartupType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssSysStartupType.setStatus(_A)
_EltMesIssSysBootVar_ObjectIdentity=ObjectIdentity
eltMesIssSysBootVar=_EltMesIssSysBootVar_ObjectIdentity((1,3,6,1,4,1,35265,1,139,18,1,1,3))
_EltMesIssSysBootVarTable_Object=MibTable
eltMesIssSysBootVarTable=_EltMesIssSysBootVarTable_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1))
if mibBuilder.loadTexts:eltMesIssSysBootVarTable.setStatus(_A)
_EltMesIssSysBootVarEntry_Object=MibTableRow
eltMesIssSysBootVarEntry=_EltMesIssSysBootVarEntry_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1))
eltMesIssSysBootVarEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:eltMesIssSysBootVarEntry.setStatus(_A)
_EltMesIssSysBootVarImageType_Type=EltMesIssSysImageType
_EltMesIssSysBootVarImageType_Object=MibTableColumn
eltMesIssSysBootVarImageType=_EltMesIssSysBootVarImageType_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,1),_EltMesIssSysBootVarImageType_Type())
eltMesIssSysBootVarImageType.setMaxAccess(_N)
if mibBuilder.loadTexts:eltMesIssSysBootVarImageType.setStatus(_A)
_EltMesIssSysBootVarImageState_Type=EltMesIssSysImageState
_EltMesIssSysBootVarImageState_Object=MibTableColumn
eltMesIssSysBootVarImageState=_EltMesIssSysBootVarImageState_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,2),_EltMesIssSysBootVarImageState_Type())
eltMesIssSysBootVarImageState.setMaxAccess(_N)
if mibBuilder.loadTexts:eltMesIssSysBootVarImageState.setStatus(_A)
_EltMesIssSysBootVarValid_Type=TruthValue
_EltMesIssSysBootVarValid_Object=MibTableColumn
eltMesIssSysBootVarValid=_EltMesIssSysBootVarValid_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,3),_EltMesIssSysBootVarValid_Type())
eltMesIssSysBootVarValid.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssSysBootVarValid.setStatus(_A)
_EltMesIssSysBootVarVersion_Type=DisplayString
_EltMesIssSysBootVarVersion_Object=MibTableColumn
eltMesIssSysBootVarVersion=_EltMesIssSysBootVarVersion_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,4),_EltMesIssSysBootVarVersion_Type())
eltMesIssSysBootVarVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssSysBootVarVersion.setStatus(_A)
_EltMesIssSysBootVarCommit_Type=DisplayString
_EltMesIssSysBootVarCommit_Object=MibTableColumn
eltMesIssSysBootVarCommit=_EltMesIssSysBootVarCommit_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,5),_EltMesIssSysBootVarCommit_Type())
eltMesIssSysBootVarCommit.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssSysBootVarCommit.setStatus(_A)
_EltMesIssSysBootVarBuild_Type=DisplayString
_EltMesIssSysBootVarBuild_Object=MibTableColumn
eltMesIssSysBootVarBuild=_EltMesIssSysBootVarBuild_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,6),_EltMesIssSysBootVarBuild_Type())
eltMesIssSysBootVarBuild.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssSysBootVarBuild.setStatus(_A)
_EltMesIssSysBootVarMd5Digest_Type=DisplayString
_EltMesIssSysBootVarMd5Digest_Object=MibTableColumn
eltMesIssSysBootVarMd5Digest=_EltMesIssSysBootVarMd5Digest_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,7),_EltMesIssSysBootVarMd5Digest_Type())
eltMesIssSysBootVarMd5Digest.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssSysBootVarMd5Digest.setStatus(_A)
_EltMesIssSysBootVarTime_Type=DisplayString
_EltMesIssSysBootVarTime_Object=MibTableColumn
eltMesIssSysBootVarTime=_EltMesIssSysBootVarTime_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,8),_EltMesIssSysBootVarTime_Type())
eltMesIssSysBootVarTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssSysBootVarTime.setStatus(_A)
_EltMesIssSysBootVarImageStateAfterReboot_Type=EltMesIssSysImageState
_EltMesIssSysBootVarImageStateAfterReboot_Object=MibTableColumn
eltMesIssSysBootVarImageStateAfterReboot=_EltMesIssSysBootVarImageStateAfterReboot_Object((1,3,6,1,4,1,35265,1,139,18,1,1,3,1,1,9),_EltMesIssSysBootVarImageStateAfterReboot_Type())
eltMesIssSysBootVarImageStateAfterReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssSysBootVarImageStateAfterReboot.setStatus(_A)
class _EltMesIssSysDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EltMesIssSysDescr_Type.__name__=_I
_EltMesIssSysDescr_Object=MibScalar
eltMesIssSysDescr=_EltMesIssSysDescr_Object((1,3,6,1,4,1,35265,1,139,18,1,1,4),_EltMesIssSysDescr_Type())
eltMesIssSysDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssSysDescr.setStatus(_A)
_EltMesIssSysNotifications_ObjectIdentity=ObjectIdentity
eltMesIssSysNotifications=_EltMesIssSysNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,18,2))
_EltMesIssSysNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltMesIssSysNotificationsPrefix=_EltMesIssSysNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,139,18,2,0))
eltMesIssSysReloadRequestTrap=NotificationType((1,3,6,1,4,1,35265,1,139,18,2,0,1))
eltMesIssSysReloadRequestTrap.setObjects((_F,_G))
if mibBuilder.loadTexts:eltMesIssSysReloadRequestTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_K:EltMesIssSysDelayedReloadMode,'EltMesIssSysImageType':EltMesIssSysImageType,'EltMesIssSysImageState':EltMesIssSysImageState,'eltMesIssSystemMIB':eltMesIssSystemMIB,'eltMesIssSysObjects':eltMesIssSysObjects,'eltMesIssSysGlobals':eltMesIssSysGlobals,'eltMesIssSysReloadParams':eltMesIssSysReloadParams,'eltMesIssDelayReloadTime':eltMesIssDelayReloadTime,'eltMesIssDelayReloadAction':eltMesIssDelayReloadAction,'eltMesIssSysLoggingParams':eltMesIssSysLoggingParams,'eltMesIssSysClearDebugLogs':eltMesIssSysClearDebugLogs,'eltMesIssSysReloadRequestLoggingEnable':eltMesIssSysReloadRequestLoggingEnable,'eltMesIssSysStartupType':eltMesIssSysStartupType,'eltMesIssSysBootVar':eltMesIssSysBootVar,'eltMesIssSysBootVarTable':eltMesIssSysBootVarTable,'eltMesIssSysBootVarEntry':eltMesIssSysBootVarEntry,_L:eltMesIssSysBootVarImageType,_M:eltMesIssSysBootVarImageState,'eltMesIssSysBootVarValid':eltMesIssSysBootVarValid,'eltMesIssSysBootVarVersion':eltMesIssSysBootVarVersion,'eltMesIssSysBootVarCommit':eltMesIssSysBootVarCommit,'eltMesIssSysBootVarBuild':eltMesIssSysBootVarBuild,'eltMesIssSysBootVarMd5Digest':eltMesIssSysBootVarMd5Digest,'eltMesIssSysBootVarTime':eltMesIssSysBootVarTime,'eltMesIssSysBootVarImageStateAfterReboot':eltMesIssSysBootVarImageStateAfterReboot,'eltMesIssSysDescr':eltMesIssSysDescr,'eltMesIssSysNotifications':eltMesIssSysNotifications,'eltMesIssSysNotificationsPrefix':eltMesIssSysNotificationsPrefix,'eltMesIssSysReloadRequestTrap':eltMesIssSysReloadRequestTrap})