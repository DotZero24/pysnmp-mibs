_S='fsIssuProcedureStatus'
_R='fsIssuCommandStatus'
_Q='fsIssuCommand'
_P='fsIssuMaintenanceOperStatus'
_O='fsIssuMaintenanceMode'
_N='successful'
_M='inprogress'
_L='incompatible'
_K='basecompatible'
_J='fullcompatible'
_I='notinitiated'
_H='TruthValue'
_G='failed'
_F='ARICENT-ISSU-MIB'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TimeStamp',_H)
fsIssu=ModuleIdentity((1,3,6,1,4,1,29601,2,103))
if mibBuilder.loadTexts:fsIssu.setRevisions(('2015-07-01 00:00',))
_FsIssuSystem_ObjectIdentity=ObjectIdentity
fsIssuSystem=_FsIssuSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,103,1))
_FsIssuMaintenanceMode_Type=TruthValue
_FsIssuMaintenanceMode_Object=MibScalar
fsIssuMaintenanceMode=_FsIssuMaintenanceMode_Object((1,3,6,1,4,1,29601,2,103,1,1),_FsIssuMaintenanceMode_Type())
fsIssuMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuMaintenanceMode.setStatus(_A)
_FsIssuMaintenanceOperStatus_Type=TruthValue
_FsIssuMaintenanceOperStatus_Object=MibScalar
fsIssuMaintenanceOperStatus=_FsIssuMaintenanceOperStatus_Object((1,3,6,1,4,1,29601,2,103,1,2),_FsIssuMaintenanceOperStatus_Type())
fsIssuMaintenanceOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIssuMaintenanceOperStatus.setStatus(_A)
class _FsIssuLoadSWPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsIssuLoadSWPath_Type.__name__=_E
_FsIssuLoadSWPath_Object=MibScalar
fsIssuLoadSWPath=_FsIssuLoadSWPath_Object((1,3,6,1,4,1,29601,2,103,1,3),_FsIssuLoadSWPath_Type())
fsIssuLoadSWPath.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuLoadSWPath.setStatus(_A)
class _FsIssuRollbackSWPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsIssuRollbackSWPath_Type.__name__=_E
_FsIssuRollbackSWPath_Object=MibScalar
fsIssuRollbackSWPath=_FsIssuRollbackSWPath_Object((1,3,6,1,4,1,29601,2,103,1,4),_FsIssuRollbackSWPath_Type())
fsIssuRollbackSWPath.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIssuRollbackSWPath.setStatus(_A)
class _FsIssuCurrentSWPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsIssuCurrentSWPath_Type.__name__=_E
_FsIssuCurrentSWPath_Object=MibScalar
fsIssuCurrentSWPath=_FsIssuCurrentSWPath_Object((1,3,6,1,4,1,29601,2,103,1,5),_FsIssuCurrentSWPath_Type())
fsIssuCurrentSWPath.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIssuCurrentSWPath.setStatus(_A)
class _FsIssuSoftwareCompatFilePath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsIssuSoftwareCompatFilePath_Type.__name__=_E
_FsIssuSoftwareCompatFilePath_Object=MibScalar
fsIssuSoftwareCompatFilePath=_FsIssuSoftwareCompatFilePath_Object((1,3,6,1,4,1,29601,2,103,1,6),_FsIssuSoftwareCompatFilePath_Type())
fsIssuSoftwareCompatFilePath.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuSoftwareCompatFilePath.setStatus(_A)
class _FsIssuSoftwareCompatCheckInit_Type(TruthValue):defaultValue=2
_FsIssuSoftwareCompatCheckInit_Type.__name__=_H
_FsIssuSoftwareCompatCheckInit_Object=MibScalar
fsIssuSoftwareCompatCheckInit=_FsIssuSoftwareCompatCheckInit_Object((1,3,6,1,4,1,29601,2,103,1,7),_FsIssuSoftwareCompatCheckInit_Type())
fsIssuSoftwareCompatCheckInit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuSoftwareCompatCheckInit.setStatus(_A)
class _FsIssuSoftwareCompatCheckStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),('checkinprogress',4),(_G,5)))
_FsIssuSoftwareCompatCheckStatus_Type.__name__=_C
_FsIssuSoftwareCompatCheckStatus_Object=MibScalar
fsIssuSoftwareCompatCheckStatus=_FsIssuSoftwareCompatCheckStatus_Object((1,3,6,1,4,1,29601,2,103,1,8),_FsIssuSoftwareCompatCheckStatus_Type())
fsIssuSoftwareCompatCheckStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIssuSoftwareCompatCheckStatus.setStatus(_A)
class _FsIssuMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_FsIssuMode_Type.__name__=_C
_FsIssuMode_Object=MibScalar
fsIssuMode=_FsIssuMode_Object((1,3,6,1,4,1,29601,2,103,1,9),_FsIssuMode_Type())
fsIssuMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuMode.setStatus(_A)
class _FsIssuCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loadversion',1),('forcestandby',2)))
_FsIssuCommand_Type.__name__=_C
_FsIssuCommand_Object=MibScalar
fsIssuCommand=_FsIssuCommand_Object((1,3,6,1,4,1,29601,2,103,1,10),_FsIssuCommand_Type())
fsIssuCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuCommand.setStatus(_A)
class _FsIssuCommandStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notstarted',0),(_M,1),(_N,2),(_G,3)))
_FsIssuCommandStatus_Type.__name__=_C
_FsIssuCommandStatus_Object=MibScalar
fsIssuCommandStatus=_FsIssuCommandStatus_Object((1,3,6,1,4,1,29601,2,103,1,11),_FsIssuCommandStatus_Type())
fsIssuCommandStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIssuCommandStatus.setStatus(_A)
class _FsIssuProcedureStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_M,1),(_N,2),(_G,3)))
_FsIssuProcedureStatus_Type.__name__=_C
_FsIssuProcedureStatus_Object=MibScalar
fsIssuProcedureStatus=_FsIssuProcedureStatus_Object((1,3,6,1,4,1,29601,2,103,1,12),_FsIssuProcedureStatus_Type())
fsIssuProcedureStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIssuProcedureStatus.setStatus(_A)
class _FsIssuRollbackSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsIssuRollbackSoftwareVersion_Type.__name__=_E
_FsIssuRollbackSoftwareVersion_Object=MibScalar
fsIssuRollbackSoftwareVersion=_FsIssuRollbackSoftwareVersion_Object((1,3,6,1,4,1,29601,2,103,1,13),_FsIssuRollbackSoftwareVersion_Type())
fsIssuRollbackSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIssuRollbackSoftwareVersion.setStatus(_A)
class _FsIssuTraceOption_Type(Integer32):defaultValue=0
_FsIssuTraceOption_Type.__name__=_C
_FsIssuTraceOption_Object=MibScalar
fsIssuTraceOption=_FsIssuTraceOption_Object((1,3,6,1,4,1,29601,2,103,1,14),_FsIssuTraceOption_Type())
fsIssuTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuTraceOption.setStatus(_A)
class _FsIssuTrapStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsIssuTrapStatus_Type.__name__=_C
_FsIssuTrapStatus_Object=MibScalar
fsIssuTrapStatus=_FsIssuTrapStatus_Object((1,3,6,1,4,1,29601,2,103,1,15),_FsIssuTrapStatus_Type())
fsIssuTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuTrapStatus.setStatus(_A)
_FsIssuLastUpgradeTime_Type=TimeStamp
_FsIssuLastUpgradeTime_Object=MibScalar
fsIssuLastUpgradeTime=_FsIssuLastUpgradeTime_Object((1,3,6,1,4,1,29601,2,103,1,16),_FsIssuLastUpgradeTime_Type())
fsIssuLastUpgradeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIssuLastUpgradeTime.setStatus(_A)
class _FsIssuSoftwareCompatForVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsIssuSoftwareCompatForVersion_Type.__name__=_E
_FsIssuSoftwareCompatForVersion_Object=MibScalar
fsIssuSoftwareCompatForVersion=_FsIssuSoftwareCompatForVersion_Object((1,3,6,1,4,1,29601,2,103,1,17),_FsIssuSoftwareCompatForVersion_Type())
fsIssuSoftwareCompatForVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIssuSoftwareCompatForVersion.setStatus(_A)
_FsIssuNotifications_ObjectIdentity=ObjectIdentity
fsIssuNotifications=_FsIssuNotifications_ObjectIdentity((1,3,6,1,4,1,29601,2,103,2))
_FsIssuTraps_ObjectIdentity=ObjectIdentity
fsIssuTraps=_FsIssuTraps_ObjectIdentity((1,3,6,1,4,1,29601,2,103,2,0))
fsIssuMaintenanceStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,103,2,0,1))
fsIssuMaintenanceStatusTrap.setObjects(*((_F,_O),(_F,_P)))
if mibBuilder.loadTexts:fsIssuMaintenanceStatusTrap.setStatus(_A)
fsIssuCommandStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,103,2,0,2))
fsIssuCommandStatusTrap.setObjects(*((_F,_Q),(_F,_R)))
if mibBuilder.loadTexts:fsIssuCommandStatusTrap.setStatus(_A)
fsIssuProcedureStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,103,2,0,3))
fsIssuProcedureStatusTrap.setObjects((_F,_S))
if mibBuilder.loadTexts:fsIssuProcedureStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'fsIssu':fsIssu,'fsIssuSystem':fsIssuSystem,_O:fsIssuMaintenanceMode,_P:fsIssuMaintenanceOperStatus,'fsIssuLoadSWPath':fsIssuLoadSWPath,'fsIssuRollbackSWPath':fsIssuRollbackSWPath,'fsIssuCurrentSWPath':fsIssuCurrentSWPath,'fsIssuSoftwareCompatFilePath':fsIssuSoftwareCompatFilePath,'fsIssuSoftwareCompatCheckInit':fsIssuSoftwareCompatCheckInit,'fsIssuSoftwareCompatCheckStatus':fsIssuSoftwareCompatCheckStatus,'fsIssuMode':fsIssuMode,_Q:fsIssuCommand,_R:fsIssuCommandStatus,_S:fsIssuProcedureStatus,'fsIssuRollbackSoftwareVersion':fsIssuRollbackSoftwareVersion,'fsIssuTraceOption':fsIssuTraceOption,'fsIssuTrapStatus':fsIssuTrapStatus,'fsIssuLastUpgradeTime':fsIssuLastUpgradeTime,'fsIssuSoftwareCompatForVersion':fsIssuSoftwareCompatForVersion,'fsIssuNotifications':fsIssuNotifications,'fsIssuTraps':fsIssuTraps,'fsIssuMaintenanceStatusTrap':fsIssuMaintenanceStatusTrap,'fsIssuCommandStatusTrap':fsIssuCommandStatusTrap,'fsIssuProcedureStatusTrap':fsIssuProcedureStatusTrap})