_Q='configManagementFailure'
_P='configManagementState'
_O='configMakingCopy'
_N='configUsing'
_M='configUploading'
_L='configDownloading'
_K='configSaving'
_J='configVerifying'
_I='DisplayString'
_H='Unsigned32'
_G='equipIpSnmpAgentAddress'
_F='SIAE-EQUIP-MIB'
_E='SIAE-CFGM-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmTrap,=mibBuilder.importSymbols('SIAE-ALARM-MIB','alarmTrap')
equipIpSnmpAgentAddress,=mibBuilder.importSymbols(_F,_G)
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
configManagement=ModuleIdentity((1,3,6,1,4,1,3373,1103,30))
if mibBuilder.loadTexts:configManagement.setRevisions(('2014-07-25 00:00','2014-02-03 00:00','2013-04-16 00:00'))
class _ConfigManagementMibVersion_Type(Integer32):defaultValue=1
_ConfigManagementMibVersion_Type.__name__=_B
_ConfigManagementMibVersion_Object=MibScalar
configManagementMibVersion=_ConfigManagementMibVersion_Object((1,3,6,1,4,1,3373,1103,30,1),_ConfigManagementMibVersion_Type())
configManagementMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:configManagementMibVersion.setStatus(_A)
class _ConfigManagementFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ConfigManagementFileName_Type.__name__=_I
_ConfigManagementFileName_Object=MibScalar
configManagementFileName=_ConfigManagementFileName_Object((1,3,6,1,4,1,3373,1103,30,2),_ConfigManagementFileName_Type())
configManagementFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:configManagementFileName.setStatus(_A)
_ConfigManagementServerIpAddress_Type=IpAddress
_ConfigManagementServerIpAddress_Object=MibScalar
configManagementServerIpAddress=_ConfigManagementServerIpAddress_Object((1,3,6,1,4,1,3373,1103,30,3),_ConfigManagementServerIpAddress_Type())
configManagementServerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:configManagementServerIpAddress.setStatus(_A)
class _ConfigManagementAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('configNone',0),('configSave',1),('configUse',2),('configBack',3),('configAbort',4),('configUseAndSwitch',5)))
_ConfigManagementAction_Type.__name__=_B
_ConfigManagementAction_Object=MibScalar
configManagementAction=_ConfigManagementAction_Object((1,3,6,1,4,1,3373,1103,30,4),_ConfigManagementAction_Type())
configManagementAction.setMaxAccess(_D)
if mibBuilder.loadTexts:configManagementAction.setStatus(_A)
class _ConfigManagementState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('configCompleted',1),('configInterrupted',2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),('configAborting',9),('configRestarting',10),('configStarted',11)))
_ConfigManagementState_Type.__name__=_B
_ConfigManagementState_Object=MibScalar
configManagementState=_ConfigManagementState_Object((1,3,6,1,4,1,3373,1103,30,5),_ConfigManagementState_Type())
configManagementState.setMaxAccess(_C)
if mibBuilder.loadTexts:configManagementState.setStatus(_A)
class _ConfigManagementFailure_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('configNoFailure',0),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),('configAborted',9)))
_ConfigManagementFailure_Type.__name__=_B
_ConfigManagementFailure_Object=MibScalar
configManagementFailure=_ConfigManagementFailure_Object((1,3,6,1,4,1,3373,1103,30,6),_ConfigManagementFailure_Type())
configManagementFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:configManagementFailure.setStatus(_A)
class _ConfigManagementBackupFileDate_Type(Unsigned32):defaultValue=0
_ConfigManagementBackupFileDate_Type.__name__=_H
_ConfigManagementBackupFileDate_Object=MibScalar
configManagementBackupFileDate=_ConfigManagementBackupFileDate_Object((1,3,6,1,4,1,3373,1103,30,7),_ConfigManagementBackupFileDate_Type())
configManagementBackupFileDate.setMaxAccess(_C)
if mibBuilder.loadTexts:configManagementBackupFileDate.setStatus(_A)
class _ConfigManagementTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trapDisable',1),('trapEnable',2)))
_ConfigManagementTrapNotification_Type.__name__=_B
_ConfigManagementTrapNotification_Object=MibScalar
configManagementTrapNotification=_ConfigManagementTrapNotification_Object((1,3,6,1,4,1,3373,1103,30,8),_ConfigManagementTrapNotification_Type())
configManagementTrapNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:configManagementTrapNotification.setStatus(_A)
configManagementFtpStatusTrap=NotificationType((1,3,6,1,4,1,3373,1103,0,3001))
configManagementFtpStatusTrap.setObjects(*((_F,_G),(_E,_P),(_E,_Q)))
if mibBuilder.loadTexts:configManagementFtpStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'configManagementFtpStatusTrap':configManagementFtpStatusTrap,'configManagement':configManagement,'configManagementMibVersion':configManagementMibVersion,'configManagementFileName':configManagementFileName,'configManagementServerIpAddress':configManagementServerIpAddress,'configManagementAction':configManagementAction,_P:configManagementState,_Q:configManagementFailure,'configManagementBackupFileDate':configManagementBackupFileDate,'configManagementTrapNotification':configManagementTrapNotification})