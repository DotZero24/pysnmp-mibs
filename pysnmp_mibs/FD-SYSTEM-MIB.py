_B1='systemUpgradeGroup'
_B0='userManageGroup'
_A_='onuAuthGroup'
_Az='cardModuleGroup'
_Ay='chassisInfoGroup'
_Ax='sysBaseManageGroup'
_Aw='ftpOperTarget'
_Av='upgradeOperation'
_Au='ftpProgress'
_At='upgradeStatus'
_As='operDeviceMap'
_Ar='dwLoadFileCrcValue'
_Aq='dwLoadFileCrcCheck'
_Ap='ftpOperFileName'
_Ao='ftpServerUserPasswd'
_An='ftpServerUserName'
_Am='ftpServerIp'
_Al='userEntryRowStatus'
_Ak='loginTimeout'
_Aj='userAccessDeviceMap'
_Ai='userPermission'
_Ah='userPassword'
_Ag='authMethodV2'
_Af='onuAuthBlacklistMacAddr'
_Ae='onuAuthBlacklistMacCfgRowStatus'
_Ad='onuAuthWhitelistMacAddr'
_Ac='onuAuthWhitelistMacCfgRowStatus'
_Ab='onuAuthLoidStrings'
_Aa='onuAuthPasswordStrings'
_AZ='onuAuthLoidCfgRowStatus'
_AY='nonAuthOnuTries'
_AX='nonAuthOnuMac'
_AW='onuAuthMacRowStatus'
_AV='endMacAddr'
_AU='beginMacAddr'
_AT='nonAuthOper'
_AS='authMethod'
_AR='ponCardUpgradeStat'
_AQ='ponCardOperate'
_AP='ponCardRuningTime'
_AO='ponCardRunningStatus'
_AN='ponCardFwVer'
_AM='ponCardHwRev'
_AL='ponCardFactorySerial'
_AK='ponCardType'
_AJ='mainCardOperate'
_AI='mainCardRunningTime'
_AH='mainCardRunningStatus'
_AG='mainCardSWVersion'
_AF='mainCardHWRevision'
_AE='mainCardFactorySerial'
_AD='mainCardType'
_AC='fanStatusBit'
_AB='powerStatusBit'
_AA='chassisTemperature'
_A9='chassisRevision'
_A8='chassisFactorySerial'
_A7='chassisType'
_A6='sysAutoBackupServer'
_A5='sysAutoBackupInterval'
_A4='sysAutoBackupType'
_A3='sysAutoBackupEnable'
_A2='sysCpuUtilization'
_A1='sysOperate'
_A0='outbandIpAddr'
_z='outbandNetMask'
_y='sysCfgRestoreFilename'
_x='sysCfgBackupType'
_w='sysCfgBackupServer'
_v='sysCfgRestoreType'
_u='sysCfgRestoreServer'
_t='sysLogLevel'
_s='sysLogEntryEnable'
_r='trapDstIpAddr4'
_q='trapDstIpAddr3'
_p='trapDstIpAddr2'
_o='trapDstIpAddr1'
_n='snmpRWCommunity'
_m='snmpReadCommunity'
_l='manageGateway'
_k='manageNetMask'
_j='manageIpAddr'
_i='consolePortSpd'
_h='sysAlarmDesc'
_g='sysCriAlarmLed'
_f='sysMajAlarmLed'
_e='sysContact'
_d='sysLocation'
_c='sysDesc'
_b='sysModel'
_a='upgrade'
_Z='userId'
_Y='authLoidEntryId'
_X='authWhitelistMacEntryId'
_W='authBlacklistMacEntryId'
_V='nonAuthOnuMacIndex'
_U='authMacEntryId'
_T='upgradeErr'
_S='upgradeOk'
_R='upgrading'
_Q='ponCardSlotId'
_P='sysLogEntryIndex'
_O='enable'
_N='onu'
_M='olt'
_L='disable'
_K='oltId'
_J='DisplayString'
_I='OctetString'
_H='Unsigned32'
_G='not-accessible'
_F='read-create'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='FD-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DeviceOperation,DeviceStatus,DeviceType,LedStatus,epon=mibBuilder.importSymbols('EPON-EOC-MIB','DeviceOperation','DeviceStatus','DeviceType','LedStatus','epon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention')
systemInfo=ModuleIdentity((1,3,6,1,4,1,34592,1,3,1))
_SysBaseInfo_ObjectIdentity=ObjectIdentity
sysBaseInfo=_SysBaseInfo_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,1))
_SysModel_Type=DeviceType
_SysModel_Object=MibScalar
sysModel=_SysModel_Object((1,3,6,1,4,1,34592,1,3,1,1,1),_SysModel_Type())
sysModel.setMaxAccess(_D)
if mibBuilder.loadTexts:sysModel.setStatus(_A)
_SysDesc_Type=DisplayString
_SysDesc_Object=MibScalar
sysDesc=_SysDesc_Object((1,3,6,1,4,1,34592,1,3,1,1,2),_SysDesc_Type())
sysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDesc.setStatus(_A)
_SysLocation_Type=DisplayString
_SysLocation_Object=MibScalar
sysLocation=_SysLocation_Object((1,3,6,1,4,1,34592,1,3,1,1,3),_SysLocation_Type())
sysLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLocation.setStatus(_A)
_SysContact_Type=DisplayString
_SysContact_Object=MibScalar
sysContact=_SysContact_Object((1,3,6,1,4,1,34592,1,3,1,1,4),_SysContact_Type())
sysContact.setMaxAccess(_C)
if mibBuilder.loadTexts:sysContact.setStatus(_A)
_SysMajAlarmLed_Type=LedStatus
_SysMajAlarmLed_Object=MibScalar
sysMajAlarmLed=_SysMajAlarmLed_Object((1,3,6,1,4,1,34592,1,3,1,1,5),_SysMajAlarmLed_Type())
sysMajAlarmLed.setMaxAccess(_D)
if mibBuilder.loadTexts:sysMajAlarmLed.setStatus(_A)
_SysCriAlarmLed_Type=LedStatus
_SysCriAlarmLed_Object=MibScalar
sysCriAlarmLed=_SysCriAlarmLed_Object((1,3,6,1,4,1,34592,1,3,1,1,6),_SysCriAlarmLed_Type())
sysCriAlarmLed.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCriAlarmLed.setStatus(_A)
_SysAlarmDesc_Type=DisplayString
_SysAlarmDesc_Object=MibScalar
sysAlarmDesc=_SysAlarmDesc_Object((1,3,6,1,4,1,34592,1,3,1,1,7),_SysAlarmDesc_Type())
sysAlarmDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmDesc.setStatus(_A)
class _SysCpuUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SysCpuUtilization_Type.__name__=_E
_SysCpuUtilization_Object=MibScalar
sysCpuUtilization=_SysCpuUtilization_Object((1,3,6,1,4,1,34592,1,3,1,1,8),_SysCpuUtilization_Type())
sysCpuUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCpuUtilization.setStatus(_A)
class _SysMTU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,2047))
_SysMTU_Type.__name__=_E
_SysMTU_Object=MibScalar
sysMTU=_SysMTU_Object((1,3,6,1,4,1,34592,1,3,1,1,9),_SysMTU_Type())
sysMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMTU.setStatus(_A)
_SysConfig_ObjectIdentity=ObjectIdentity
sysConfig=_SysConfig_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,2))
class _ConsolePortSpd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('bps2400',1),('bps4800',2),('bps9600',3),('bps19200',4),('bps38400',5),('bps57600',6),('bps115200',7)))
_ConsolePortSpd_Type.__name__=_E
_ConsolePortSpd_Object=MibScalar
consolePortSpd=_ConsolePortSpd_Object((1,3,6,1,4,1,34592,1,3,1,2,1),_ConsolePortSpd_Type())
consolePortSpd.setMaxAccess(_D)
if mibBuilder.loadTexts:consolePortSpd.setStatus(_A)
_ManageIpAddr_Type=IpAddress
_ManageIpAddr_Object=MibScalar
manageIpAddr=_ManageIpAddr_Object((1,3,6,1,4,1,34592,1,3,1,2,2),_ManageIpAddr_Type())
manageIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:manageIpAddr.setStatus(_A)
_ManageNetMask_Type=IpAddress
_ManageNetMask_Object=MibScalar
manageNetMask=_ManageNetMask_Object((1,3,6,1,4,1,34592,1,3,1,2,3),_ManageNetMask_Type())
manageNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:manageNetMask.setStatus(_A)
_ManageGateway_Type=IpAddress
_ManageGateway_Object=MibScalar
manageGateway=_ManageGateway_Object((1,3,6,1,4,1,34592,1,3,1,2,4),_ManageGateway_Type())
manageGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:manageGateway.setStatus(_A)
_SnmpReadCommunity_Type=DisplayString
_SnmpReadCommunity_Object=MibScalar
snmpReadCommunity=_SnmpReadCommunity_Object((1,3,6,1,4,1,34592,1,3,1,2,5),_SnmpReadCommunity_Type())
snmpReadCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpReadCommunity.setStatus(_A)
_SnmpRWCommunity_Type=DisplayString
_SnmpRWCommunity_Object=MibScalar
snmpRWCommunity=_SnmpRWCommunity_Object((1,3,6,1,4,1,34592,1,3,1,2,6),_SnmpRWCommunity_Type())
snmpRWCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpRWCommunity.setStatus(_A)
_TrapDstIpAddr1_Type=IpAddress
_TrapDstIpAddr1_Object=MibScalar
trapDstIpAddr1=_TrapDstIpAddr1_Object((1,3,6,1,4,1,34592,1,3,1,2,8),_TrapDstIpAddr1_Type())
trapDstIpAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDstIpAddr1.setStatus(_A)
_TrapDstIpAddr2_Type=IpAddress
_TrapDstIpAddr2_Object=MibScalar
trapDstIpAddr2=_TrapDstIpAddr2_Object((1,3,6,1,4,1,34592,1,3,1,2,9),_TrapDstIpAddr2_Type())
trapDstIpAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDstIpAddr2.setStatus(_A)
_TrapDstIpAddr3_Type=IpAddress
_TrapDstIpAddr3_Object=MibScalar
trapDstIpAddr3=_TrapDstIpAddr3_Object((1,3,6,1,4,1,34592,1,3,1,2,10),_TrapDstIpAddr3_Type())
trapDstIpAddr3.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDstIpAddr3.setStatus(_A)
_TrapDstIpAddr4_Type=IpAddress
_TrapDstIpAddr4_Object=MibScalar
trapDstIpAddr4=_TrapDstIpAddr4_Object((1,3,6,1,4,1,34592,1,3,1,2,11),_TrapDstIpAddr4_Type())
trapDstIpAddr4.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDstIpAddr4.setStatus(_A)
_SysOperate_Type=DeviceOperation
_SysOperate_Object=MibScalar
sysOperate=_SysOperate_Object((1,3,6,1,4,1,34592,1,3,1,2,12),_SysOperate_Type())
sysOperate.setMaxAccess(_C)
if mibBuilder.loadTexts:sysOperate.setStatus(_A)
_OutbandIpAddr_Type=IpAddress
_OutbandIpAddr_Object=MibScalar
outbandIpAddr=_OutbandIpAddr_Object((1,3,6,1,4,1,34592,1,3,1,2,13),_OutbandIpAddr_Type())
outbandIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:outbandIpAddr.setStatus(_A)
_OutbandNetMask_Type=IpAddress
_OutbandNetMask_Object=MibScalar
outbandNetMask=_OutbandNetMask_Object((1,3,6,1,4,1,34592,1,3,1,2,14),_OutbandNetMask_Type())
outbandNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:outbandNetMask.setStatus(_A)
_SysConfigurations_ObjectIdentity=ObjectIdentity
sysConfigurations=_SysConfigurations_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,2,15))
_CfgAutoBackup_ObjectIdentity=ObjectIdentity
cfgAutoBackup=_CfgAutoBackup_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,2,15,1))
class _SysAutoBackupEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_O,1)))
_SysAutoBackupEnable_Type.__name__=_E
_SysAutoBackupEnable_Object=MibScalar
sysAutoBackupEnable=_SysAutoBackupEnable_Object((1,3,6,1,4,1,34592,1,3,1,2,15,1,1),_SysAutoBackupEnable_Type())
sysAutoBackupEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAutoBackupEnable.setStatus(_A)
class _SysAutoBackupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),('all',3)))
_SysAutoBackupType_Type.__name__=_E
_SysAutoBackupType_Object=MibScalar
sysAutoBackupType=_SysAutoBackupType_Object((1,3,6,1,4,1,34592,1,3,1,2,15,1,2),_SysAutoBackupType_Type())
sysAutoBackupType.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAutoBackupType.setStatus(_A)
class _SysAutoBackupInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,365))
_SysAutoBackupInterval_Type.__name__=_E
_SysAutoBackupInterval_Object=MibScalar
sysAutoBackupInterval=_SysAutoBackupInterval_Object((1,3,6,1,4,1,34592,1,3,1,2,15,1,3),_SysAutoBackupInterval_Type())
sysAutoBackupInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAutoBackupInterval.setStatus(_A)
_SysAutoBackupServer_Type=IpAddress
_SysAutoBackupServer_Object=MibScalar
sysAutoBackupServer=_SysAutoBackupServer_Object((1,3,6,1,4,1,34592,1,3,1,2,15,1,4),_SysAutoBackupServer_Type())
sysAutoBackupServer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAutoBackupServer.setStatus(_A)
_CfgBackup_ObjectIdentity=ObjectIdentity
cfgBackup=_CfgBackup_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,2,15,2))
class _SysCfgBackupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SysCfgBackupType_Type.__name__=_E
_SysCfgBackupType_Object=MibScalar
sysCfgBackupType=_SysCfgBackupType_Object((1,3,6,1,4,1,34592,1,3,1,2,15,2,1),_SysCfgBackupType_Type())
sysCfgBackupType.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCfgBackupType.setStatus(_A)
_SysCfgBackupServer_Type=IpAddress
_SysCfgBackupServer_Object=MibScalar
sysCfgBackupServer=_SysCfgBackupServer_Object((1,3,6,1,4,1,34592,1,3,1,2,15,2,2),_SysCfgBackupServer_Type())
sysCfgBackupServer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCfgBackupServer.setStatus(_A)
_CfgRestore_ObjectIdentity=ObjectIdentity
cfgRestore=_CfgRestore_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,2,15,3))
class _SysCfgRestoreType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SysCfgRestoreType_Type.__name__=_E
_SysCfgRestoreType_Object=MibScalar
sysCfgRestoreType=_SysCfgRestoreType_Object((1,3,6,1,4,1,34592,1,3,1,2,15,3,1),_SysCfgRestoreType_Type())
sysCfgRestoreType.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCfgRestoreType.setStatus(_A)
_SysCfgRestoreServer_Type=IpAddress
_SysCfgRestoreServer_Object=MibScalar
sysCfgRestoreServer=_SysCfgRestoreServer_Object((1,3,6,1,4,1,34592,1,3,1,2,15,3,2),_SysCfgRestoreServer_Type())
sysCfgRestoreServer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCfgRestoreServer.setStatus(_A)
_SysCfgRestoreFilename_Type=DisplayString
_SysCfgRestoreFilename_Object=MibScalar
sysCfgRestoreFilename=_SysCfgRestoreFilename_Object((1,3,6,1,4,1,34592,1,3,1,2,15,3,3),_SysCfgRestoreFilename_Type())
sysCfgRestoreFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCfgRestoreFilename.setStatus(_A)
_SysLog_ObjectIdentity=ObjectIdentity
sysLog=_SysLog_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,2,16))
_SysLogLevel_Type=Integer32
_SysLogLevel_Object=MibScalar
sysLogLevel=_SysLogLevel_Object((1,3,6,1,4,1,34592,1,3,1,2,16,1),_SysLogLevel_Type())
sysLogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLogLevel.setStatus(_A)
_SysLogTable_Object=MibTable
sysLogTable=_SysLogTable_Object((1,3,6,1,4,1,34592,1,3,1,2,16,2))
if mibBuilder.loadTexts:sysLogTable.setStatus(_A)
_SysLogEntry_Object=MibTableRow
sysLogEntry=_SysLogEntry_Object((1,3,6,1,4,1,34592,1,3,1,2,16,2,1))
sysLogEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:sysLogEntry.setStatus(_A)
class _SysLogEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,127)));namedValues=NamedValues(*(('onuOnOffLine',1),('onuDyingGaspAlarm',2),('onuUniLoopBackAlarm',3),('all',127)))
_SysLogEntryIndex_Type.__name__=_E
_SysLogEntryIndex_Object=MibTableColumn
sysLogEntryIndex=_SysLogEntryIndex_Object((1,3,6,1,4,1,34592,1,3,1,2,16,2,1,1),_SysLogEntryIndex_Type())
sysLogEntryIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sysLogEntryIndex.setStatus(_A)
class _SysLogEntryEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_O,1)))
_SysLogEntryEnable_Type.__name__=_E
_SysLogEntryEnable_Object=MibTableColumn
sysLogEntryEnable=_SysLogEntryEnable_Object((1,3,6,1,4,1,34592,1,3,1,2,16,2,1,2),_SysLogEntryEnable_Type())
sysLogEntryEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLogEntryEnable.setStatus(_A)
_Date_ObjectIdentity=ObjectIdentity
date=_Date_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,2,17))
_ChassisInfo_ObjectIdentity=ObjectIdentity
chassisInfo=_ChassisInfo_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,3))
_ChassisType_Type=DeviceType
_ChassisType_Object=MibScalar
chassisType=_ChassisType_Object((1,3,6,1,4,1,34592,1,3,1,3,1),_ChassisType_Type())
chassisType.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisType.setStatus(_A)
class _ChassisFactorySerial_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_ChassisFactorySerial_Type.__name__=_I
_ChassisFactorySerial_Object=MibScalar
chassisFactorySerial=_ChassisFactorySerial_Object((1,3,6,1,4,1,34592,1,3,1,3,2),_ChassisFactorySerial_Type())
chassisFactorySerial.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisFactorySerial.setStatus(_A)
_ChassisRevision_Type=DisplayString
_ChassisRevision_Object=MibScalar
chassisRevision=_ChassisRevision_Object((1,3,6,1,4,1,34592,1,3,1,3,3),_ChassisRevision_Type())
chassisRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisRevision.setStatus(_A)
_ChassisTemperature_Type=Unsigned32
_ChassisTemperature_Object=MibScalar
chassisTemperature=_ChassisTemperature_Object((1,3,6,1,4,1,34592,1,3,1,3,4),_ChassisTemperature_Type())
chassisTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisTemperature.setStatus(_A)
_PowerStatusBit_Type=Unsigned32
_PowerStatusBit_Object=MibScalar
powerStatusBit=_PowerStatusBit_Object((1,3,6,1,4,1,34592,1,3,1,3,5),_PowerStatusBit_Type())
powerStatusBit.setMaxAccess(_D)
if mibBuilder.loadTexts:powerStatusBit.setStatus(_A)
_FanStatusBit_Type=Unsigned32
_FanStatusBit_Object=MibScalar
fanStatusBit=_FanStatusBit_Object((1,3,6,1,4,1,34592,1,3,1,3,6),_FanStatusBit_Type())
fanStatusBit.setMaxAccess(_D)
if mibBuilder.loadTexts:fanStatusBit.setStatus(_A)
_CardModule_ObjectIdentity=ObjectIdentity
cardModule=_CardModule_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,5))
_MainCard_ObjectIdentity=ObjectIdentity
mainCard=_MainCard_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,5,1))
_MainCardType_Type=DeviceType
_MainCardType_Object=MibScalar
mainCardType=_MainCardType_Object((1,3,6,1,4,1,34592,1,3,1,5,1,1),_MainCardType_Type())
mainCardType.setMaxAccess(_D)
if mibBuilder.loadTexts:mainCardType.setStatus(_A)
class _MainCardFactorySerial_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_MainCardFactorySerial_Type.__name__=_I
_MainCardFactorySerial_Object=MibScalar
mainCardFactorySerial=_MainCardFactorySerial_Object((1,3,6,1,4,1,34592,1,3,1,5,1,2),_MainCardFactorySerial_Type())
mainCardFactorySerial.setMaxAccess(_D)
if mibBuilder.loadTexts:mainCardFactorySerial.setStatus(_A)
_MainCardHWRevision_Type=DisplayString
_MainCardHWRevision_Object=MibScalar
mainCardHWRevision=_MainCardHWRevision_Object((1,3,6,1,4,1,34592,1,3,1,5,1,3),_MainCardHWRevision_Type())
mainCardHWRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:mainCardHWRevision.setStatus(_A)
_MainCardSWVersion_Type=DisplayString
_MainCardSWVersion_Object=MibScalar
mainCardSWVersion=_MainCardSWVersion_Object((1,3,6,1,4,1,34592,1,3,1,5,1,4),_MainCardSWVersion_Type())
mainCardSWVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:mainCardSWVersion.setStatus(_A)
_MainCardRunningStatus_Type=DeviceStatus
_MainCardRunningStatus_Object=MibScalar
mainCardRunningStatus=_MainCardRunningStatus_Object((1,3,6,1,4,1,34592,1,3,1,5,1,5),_MainCardRunningStatus_Type())
mainCardRunningStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mainCardRunningStatus.setStatus(_A)
_MainCardRunningTime_Type=TimeTicks
_MainCardRunningTime_Object=MibScalar
mainCardRunningTime=_MainCardRunningTime_Object((1,3,6,1,4,1,34592,1,3,1,5,1,6),_MainCardRunningTime_Type())
mainCardRunningTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mainCardRunningTime.setStatus(_A)
_MainCardOperate_Type=DeviceOperation
_MainCardOperate_Object=MibScalar
mainCardOperate=_MainCardOperate_Object((1,3,6,1,4,1,34592,1,3,1,5,1,7),_MainCardOperate_Type())
mainCardOperate.setMaxAccess(_C)
if mibBuilder.loadTexts:mainCardOperate.setStatus(_A)
_PonCard_ObjectIdentity=ObjectIdentity
ponCard=_PonCard_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,5,2))
_PonCardTable_Object=MibTable
ponCardTable=_PonCardTable_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1))
if mibBuilder.loadTexts:ponCardTable.setStatus(_A)
_PonCardEntry_Object=MibTableRow
ponCardEntry=_PonCardEntry_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1))
ponCardEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:ponCardEntry.setStatus(_A)
class _PonCardSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_PonCardSlotId_Type.__name__=_E
_PonCardSlotId_Object=MibTableColumn
ponCardSlotId=_PonCardSlotId_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,1),_PonCardSlotId_Type())
ponCardSlotId.setMaxAccess(_G)
if mibBuilder.loadTexts:ponCardSlotId.setStatus(_A)
_PonCardType_Type=DeviceType
_PonCardType_Object=MibTableColumn
ponCardType=_PonCardType_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,2),_PonCardType_Type())
ponCardType.setMaxAccess(_D)
if mibBuilder.loadTexts:ponCardType.setStatus(_A)
class _PonCardFactorySerial_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_PonCardFactorySerial_Type.__name__=_I
_PonCardFactorySerial_Object=MibTableColumn
ponCardFactorySerial=_PonCardFactorySerial_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,3),_PonCardFactorySerial_Type())
ponCardFactorySerial.setMaxAccess(_D)
if mibBuilder.loadTexts:ponCardFactorySerial.setStatus(_A)
_PonCardHwRev_Type=DisplayString
_PonCardHwRev_Object=MibTableColumn
ponCardHwRev=_PonCardHwRev_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,4),_PonCardHwRev_Type())
ponCardHwRev.setMaxAccess(_D)
if mibBuilder.loadTexts:ponCardHwRev.setStatus(_A)
_PonCardFwVer_Type=DisplayString
_PonCardFwVer_Object=MibTableColumn
ponCardFwVer=_PonCardFwVer_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,5),_PonCardFwVer_Type())
ponCardFwVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ponCardFwVer.setStatus(_A)
_PonCardRunningStatus_Type=DeviceStatus
_PonCardRunningStatus_Object=MibTableColumn
ponCardRunningStatus=_PonCardRunningStatus_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,7),_PonCardRunningStatus_Type())
ponCardRunningStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ponCardRunningStatus.setStatus(_A)
_PonCardRuningTime_Type=TimeTicks
_PonCardRuningTime_Object=MibTableColumn
ponCardRuningTime=_PonCardRuningTime_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,8),_PonCardRuningTime_Type())
ponCardRuningTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ponCardRuningTime.setStatus(_A)
_PonCardOperate_Type=DeviceOperation
_PonCardOperate_Object=MibTableColumn
ponCardOperate=_PonCardOperate_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,9),_PonCardOperate_Type())
ponCardOperate.setMaxAccess(_C)
if mibBuilder.loadTexts:ponCardOperate.setStatus(_A)
class _PonCardUpgradeStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('booting',1),('normalRun',2),('rcvFileIng',3),('rcvFileOk',4),('rcvFileErr',5),(_R,6),(_S,7),(_T,8),('upgradeOlt',9),('upgradeOnu',10)))
_PonCardUpgradeStat_Type.__name__=_E
_PonCardUpgradeStat_Object=MibTableColumn
ponCardUpgradeStat=_PonCardUpgradeStat_Object((1,3,6,1,4,1,34592,1,3,1,5,2,1,1,10),_PonCardUpgradeStat_Type())
ponCardUpgradeStat.setMaxAccess(_D)
if mibBuilder.loadTexts:ponCardUpgradeStat.setStatus(_A)
_OnuAuth_ObjectIdentity=ObjectIdentity
onuAuth=_OnuAuth_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,6))
class _AuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blackList',1),('whiteList',2),('none',3)))
_AuthMethod_Type.__name__=_E
_AuthMethod_Object=MibScalar
authMethod=_AuthMethod_Object((1,3,6,1,4,1,34592,1,3,1,6,1),_AuthMethod_Type())
authMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:authMethod.setStatus(_A)
class _NonAuthOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('clearNonAuthMacList',2))
_NonAuthOper_Type.__name__=_E
_NonAuthOper_Object=MibScalar
nonAuthOper=_NonAuthOper_Object((1,3,6,1,4,1,34592,1,3,1,6,2),_NonAuthOper_Type())
nonAuthOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nonAuthOper.setStatus(_A)
_OnuAuthMacCfgTable_Object=MibTable
onuAuthMacCfgTable=_OnuAuthMacCfgTable_Object((1,3,6,1,4,1,34592,1,3,1,6,3))
if mibBuilder.loadTexts:onuAuthMacCfgTable.setStatus(_A)
_OnuAuthMacCfgEntry_Object=MibTableRow
onuAuthMacCfgEntry=_OnuAuthMacCfgEntry_Object((1,3,6,1,4,1,34592,1,3,1,6,3,1))
onuAuthMacCfgEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:onuAuthMacCfgEntry.setStatus(_A)
class _AuthMacEntryId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_AuthMacEntryId_Type.__name__=_H
_AuthMacEntryId_Object=MibTableColumn
authMacEntryId=_AuthMacEntryId_Object((1,3,6,1,4,1,34592,1,3,1,6,3,1,1),_AuthMacEntryId_Type())
authMacEntryId.setMaxAccess(_G)
if mibBuilder.loadTexts:authMacEntryId.setStatus(_A)
_BeginMacAddr_Type=MacAddress
_BeginMacAddr_Object=MibTableColumn
beginMacAddr=_BeginMacAddr_Object((1,3,6,1,4,1,34592,1,3,1,6,3,1,2),_BeginMacAddr_Type())
beginMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:beginMacAddr.setStatus(_A)
_EndMacAddr_Type=MacAddress
_EndMacAddr_Object=MibTableColumn
endMacAddr=_EndMacAddr_Object((1,3,6,1,4,1,34592,1,3,1,6,3,1,3),_EndMacAddr_Type())
endMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:endMacAddr.setStatus(_A)
class _MacAttr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blackMac',1),('whiteMac',2),('obsolete',3)))
_MacAttr_Type.__name__=_E
_MacAttr_Object=MibTableColumn
macAttr=_MacAttr_Object((1,3,6,1,4,1,34592,1,3,1,6,3,1,4),_MacAttr_Type())
macAttr.setMaxAccess(_F)
if mibBuilder.loadTexts:macAttr.setStatus(_A)
_OnuAuthMacRowStatus_Type=RowStatus
_OnuAuthMacRowStatus_Object=MibTableColumn
onuAuthMacRowStatus=_OnuAuthMacRowStatus_Object((1,3,6,1,4,1,34592,1,3,1,6,3,1,5),_OnuAuthMacRowStatus_Type())
onuAuthMacRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:onuAuthMacRowStatus.setStatus(_A)
_NonAuthOnuListTable_Object=MibTable
nonAuthOnuListTable=_NonAuthOnuListTable_Object((1,3,6,1,4,1,34592,1,3,1,6,4))
if mibBuilder.loadTexts:nonAuthOnuListTable.setStatus(_A)
_NonAuthOnuListEntry_Object=MibTableRow
nonAuthOnuListEntry=_NonAuthOnuListEntry_Object((1,3,6,1,4,1,34592,1,3,1,6,4,1))
nonAuthOnuListEntry.setIndexNames((0,_B,_K),(0,_B,_V))
if mibBuilder.loadTexts:nonAuthOnuListEntry.setStatus(_A)
class _NonAuthOnuMacIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_NonAuthOnuMacIndex_Type.__name__=_H
_NonAuthOnuMacIndex_Object=MibTableColumn
nonAuthOnuMacIndex=_NonAuthOnuMacIndex_Object((1,3,6,1,4,1,34592,1,3,1,6,4,1,1),_NonAuthOnuMacIndex_Type())
nonAuthOnuMacIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nonAuthOnuMacIndex.setStatus(_A)
_NonAuthOnuMac_Type=MacAddress
_NonAuthOnuMac_Object=MibTableColumn
nonAuthOnuMac=_NonAuthOnuMac_Object((1,3,6,1,4,1,34592,1,3,1,6,4,1,2),_NonAuthOnuMac_Type())
nonAuthOnuMac.setMaxAccess(_D)
if mibBuilder.loadTexts:nonAuthOnuMac.setStatus(_A)
_NonAuthOnuTries_Type=Unsigned32
_NonAuthOnuTries_Object=MibTableColumn
nonAuthOnuTries=_NonAuthOnuTries_Object((1,3,6,1,4,1,34592,1,3,1,6,4,1,3),_NonAuthOnuTries_Type())
nonAuthOnuTries.setMaxAccess(_D)
if mibBuilder.loadTexts:nonAuthOnuTries.setStatus(_A)
class _OltId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_OltId_Type.__name__=_E
_OltId_Object=MibTableColumn
oltId=_OltId_Object((1,3,6,1,4,1,34592,1,3,1,6,4,1,4),_OltId_Type())
oltId.setMaxAccess(_D)
if mibBuilder.loadTexts:oltId.setStatus(_A)
class _AuthMethodV2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_L,0),('mac',1),('loid',2),('hybrid',3),('blacklist',4),('whitelist',5)))
_AuthMethodV2_Type.__name__=_E
_AuthMethodV2_Object=MibScalar
authMethodV2=_AuthMethodV2_Object((1,3,6,1,4,1,34592,1,3,1,6,5),_AuthMethodV2_Type())
authMethodV2.setMaxAccess(_C)
if mibBuilder.loadTexts:authMethodV2.setStatus(_A)
_OnuAuthBlacklistMacCfgTable_Object=MibTable
onuAuthBlacklistMacCfgTable=_OnuAuthBlacklistMacCfgTable_Object((1,3,6,1,4,1,34592,1,3,1,6,6))
if mibBuilder.loadTexts:onuAuthBlacklistMacCfgTable.setStatus(_A)
_OnuAuthBlacklistMacCfgEntry_Object=MibTableRow
onuAuthBlacklistMacCfgEntry=_OnuAuthBlacklistMacCfgEntry_Object((1,3,6,1,4,1,34592,1,3,1,6,6,1))
onuAuthBlacklistMacCfgEntry.setIndexNames((0,_B,_K),(0,_B,_W))
if mibBuilder.loadTexts:onuAuthBlacklistMacCfgEntry.setStatus(_A)
class _AuthBlacklistMacEntryId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_AuthBlacklistMacEntryId_Type.__name__=_H
_AuthBlacklistMacEntryId_Object=MibTableColumn
authBlacklistMacEntryId=_AuthBlacklistMacEntryId_Object((1,3,6,1,4,1,34592,1,3,1,6,6,1,1),_AuthBlacklistMacEntryId_Type())
authBlacklistMacEntryId.setMaxAccess(_G)
if mibBuilder.loadTexts:authBlacklistMacEntryId.setStatus(_A)
_OnuAuthBlacklistMacAddr_Type=MacAddress
_OnuAuthBlacklistMacAddr_Object=MibTableColumn
onuAuthBlacklistMacAddr=_OnuAuthBlacklistMacAddr_Object((1,3,6,1,4,1,34592,1,3,1,6,6,1,2),_OnuAuthBlacklistMacAddr_Type())
onuAuthBlacklistMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:onuAuthBlacklistMacAddr.setStatus(_A)
_OnuAuthBlacklistMacCfgRowStatus_Type=RowStatus
_OnuAuthBlacklistMacCfgRowStatus_Object=MibTableColumn
onuAuthBlacklistMacCfgRowStatus=_OnuAuthBlacklistMacCfgRowStatus_Object((1,3,6,1,4,1,34592,1,3,1,6,6,1,3),_OnuAuthBlacklistMacCfgRowStatus_Type())
onuAuthBlacklistMacCfgRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:onuAuthBlacklistMacCfgRowStatus.setStatus(_A)
_OnuAuthWhitelistMacCfgTable_Object=MibTable
onuAuthWhitelistMacCfgTable=_OnuAuthWhitelistMacCfgTable_Object((1,3,6,1,4,1,34592,1,3,1,6,7))
if mibBuilder.loadTexts:onuAuthWhitelistMacCfgTable.setStatus(_A)
_OnuAuthWhitelistMacCfgEntry_Object=MibTableRow
onuAuthWhitelistMacCfgEntry=_OnuAuthWhitelistMacCfgEntry_Object((1,3,6,1,4,1,34592,1,3,1,6,7,1))
onuAuthWhitelistMacCfgEntry.setIndexNames((0,_B,_K),(0,_B,_X))
if mibBuilder.loadTexts:onuAuthWhitelistMacCfgEntry.setStatus(_A)
class _AuthWhitelistMacEntryId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_AuthWhitelistMacEntryId_Type.__name__=_H
_AuthWhitelistMacEntryId_Object=MibTableColumn
authWhitelistMacEntryId=_AuthWhitelistMacEntryId_Object((1,3,6,1,4,1,34592,1,3,1,6,7,1,1),_AuthWhitelistMacEntryId_Type())
authWhitelistMacEntryId.setMaxAccess(_G)
if mibBuilder.loadTexts:authWhitelistMacEntryId.setStatus(_A)
_OnuAuthWhitelistMacAddr_Type=MacAddress
_OnuAuthWhitelistMacAddr_Object=MibTableColumn
onuAuthWhitelistMacAddr=_OnuAuthWhitelistMacAddr_Object((1,3,6,1,4,1,34592,1,3,1,6,7,1,2),_OnuAuthWhitelistMacAddr_Type())
onuAuthWhitelistMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:onuAuthWhitelistMacAddr.setStatus(_A)
_OnuAuthWhitelistMacCfgRowStatus_Type=RowStatus
_OnuAuthWhitelistMacCfgRowStatus_Object=MibTableColumn
onuAuthWhitelistMacCfgRowStatus=_OnuAuthWhitelistMacCfgRowStatus_Object((1,3,6,1,4,1,34592,1,3,1,6,7,1,3),_OnuAuthWhitelistMacCfgRowStatus_Type())
onuAuthWhitelistMacCfgRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:onuAuthWhitelistMacCfgRowStatus.setStatus(_A)
_OnuAuthLoidCfgTable_Object=MibTable
onuAuthLoidCfgTable=_OnuAuthLoidCfgTable_Object((1,3,6,1,4,1,34592,1,3,1,6,8))
if mibBuilder.loadTexts:onuAuthLoidCfgTable.setStatus(_A)
_OnuAuthLoidCfgEntry_Object=MibTableRow
onuAuthLoidCfgEntry=_OnuAuthLoidCfgEntry_Object((1,3,6,1,4,1,34592,1,3,1,6,8,1))
onuAuthLoidCfgEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:onuAuthLoidCfgEntry.setStatus(_A)
class _AuthLoidEntryId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_AuthLoidEntryId_Type.__name__=_H
_AuthLoidEntryId_Object=MibTableColumn
authLoidEntryId=_AuthLoidEntryId_Object((1,3,6,1,4,1,34592,1,3,1,6,8,1,1),_AuthLoidEntryId_Type())
authLoidEntryId.setMaxAccess(_G)
if mibBuilder.loadTexts:authLoidEntryId.setStatus(_A)
_OnuAuthLoidStrings_Type=DisplayString
_OnuAuthLoidStrings_Object=MibTableColumn
onuAuthLoidStrings=_OnuAuthLoidStrings_Object((1,3,6,1,4,1,34592,1,3,1,6,8,1,2),_OnuAuthLoidStrings_Type())
onuAuthLoidStrings.setMaxAccess(_F)
if mibBuilder.loadTexts:onuAuthLoidStrings.setStatus(_A)
_OnuAuthPasswordStrings_Type=DisplayString
_OnuAuthPasswordStrings_Object=MibTableColumn
onuAuthPasswordStrings=_OnuAuthPasswordStrings_Object((1,3,6,1,4,1,34592,1,3,1,6,8,1,3),_OnuAuthPasswordStrings_Type())
onuAuthPasswordStrings.setMaxAccess(_F)
if mibBuilder.loadTexts:onuAuthPasswordStrings.setStatus(_A)
_OnuAuthLoidCfgRowStatus_Type=RowStatus
_OnuAuthLoidCfgRowStatus_Object=MibTableColumn
onuAuthLoidCfgRowStatus=_OnuAuthLoidCfgRowStatus_Object((1,3,6,1,4,1,34592,1,3,1,6,8,1,4),_OnuAuthLoidCfgRowStatus_Type())
onuAuthLoidCfgRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:onuAuthLoidCfgRowStatus.setStatus(_A)
_UserManage_ObjectIdentity=ObjectIdentity
userManage=_UserManage_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,7))
_UserManageTable_Object=MibTable
userManageTable=_UserManageTable_Object((1,3,6,1,4,1,34592,1,3,1,7,1))
if mibBuilder.loadTexts:userManageTable.setStatus(_A)
_UserManageEntry_Object=MibTableRow
userManageEntry=_UserManageEntry_Object((1,3,6,1,4,1,34592,1,3,1,7,1,1))
userManageEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:userManageEntry.setStatus(_A)
class _UserId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_UserId_Type.__name__=_E
_UserId_Object=MibTableColumn
userId=_UserId_Object((1,3,6,1,4,1,34592,1,3,1,7,1,1,1),_UserId_Type())
userId.setMaxAccess(_G)
if mibBuilder.loadTexts:userId.setStatus(_A)
_UserName_Type=DisplayString
_UserName_Object=MibTableColumn
userName=_UserName_Object((1,3,6,1,4,1,34592,1,3,1,7,1,1,2),_UserName_Type())
userName.setMaxAccess(_F)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _UserPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserPassword_Type.__name__=_I
_UserPassword_Object=MibTableColumn
userPassword=_UserPassword_Object((1,3,6,1,4,1,34592,1,3,1,7,1,1,3),_UserPassword_Type())
userPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:userPassword.setStatus(_A)
_UserPermission_Type=Unsigned32
_UserPermission_Object=MibTableColumn
userPermission=_UserPermission_Object((1,3,6,1,4,1,34592,1,3,1,7,1,1,4),_UserPermission_Type())
userPermission.setMaxAccess(_D)
if mibBuilder.loadTexts:userPermission.setStatus(_A)
_UserAccessDeviceMap_Type=Unsigned32
_UserAccessDeviceMap_Object=MibTableColumn
userAccessDeviceMap=_UserAccessDeviceMap_Object((1,3,6,1,4,1,34592,1,3,1,7,1,1,5),_UserAccessDeviceMap_Type())
userAccessDeviceMap.setMaxAccess(_F)
if mibBuilder.loadTexts:userAccessDeviceMap.setStatus(_A)
class _LoginTimeout_Type(Unsigned32):defaultValue=300
_LoginTimeout_Type.__name__=_H
_LoginTimeout_Object=MibTableColumn
loginTimeout=_LoginTimeout_Object((1,3,6,1,4,1,34592,1,3,1,7,1,1,6),_LoginTimeout_Type())
loginTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:loginTimeout.setStatus(_A)
_UserEntryRowStatus_Type=RowStatus
_UserEntryRowStatus_Object=MibTableColumn
userEntryRowStatus=_UserEntryRowStatus_Object((1,3,6,1,4,1,34592,1,3,1,7,1,1,7),_UserEntryRowStatus_Type())
userEntryRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:userEntryRowStatus.setStatus(_A)
_Upgrade_ObjectIdentity=ObjectIdentity
upgrade=_Upgrade_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,8))
class _FtpServerIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FtpServerIp_Type.__name__=_J
_FtpServerIp_Object=MibScalar
ftpServerIp=_FtpServerIp_Object((1,3,6,1,4,1,34592,1,3,1,8,1),_FtpServerIp_Type())
ftpServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ftpServerIp.setStatus(_A)
class _FtpServerUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FtpServerUserName_Type.__name__=_J
_FtpServerUserName_Object=MibScalar
ftpServerUserName=_FtpServerUserName_Object((1,3,6,1,4,1,34592,1,3,1,8,2),_FtpServerUserName_Type())
ftpServerUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ftpServerUserName.setStatus(_A)
class _FtpServerUserPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FtpServerUserPasswd_Type.__name__=_J
_FtpServerUserPasswd_Object=MibScalar
ftpServerUserPasswd=_FtpServerUserPasswd_Object((1,3,6,1,4,1,34592,1,3,1,8,3),_FtpServerUserPasswd_Type())
ftpServerUserPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:ftpServerUserPasswd.setStatus(_A)
class _FtpOperFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FtpOperFileName_Type.__name__=_J
_FtpOperFileName_Object=MibScalar
ftpOperFileName=_FtpOperFileName_Object((1,3,6,1,4,1,34592,1,3,1,8,4),_FtpOperFileName_Type())
ftpOperFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:ftpOperFileName.setStatus(_A)
class _FtpOperTarget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('ctrlCardImage',1),('ponCardImage',2),('oltApp',3),('oltPers',4),('oltBoot',5),('onuApp',6),('onuPers',7),('onuBoot',8),('otherSpecifiedFile',9)))
_FtpOperTarget_Type.__name__=_E
_FtpOperTarget_Object=MibScalar
ftpOperTarget=_FtpOperTarget_Object((1,3,6,1,4,1,34592,1,3,1,8,6),_FtpOperTarget_Type())
ftpOperTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:ftpOperTarget.setStatus(_A)
class _DwLoadFileCrcCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('checkCrc',1),('dontCheckCrc',2)))
_DwLoadFileCrcCheck_Type.__name__=_E
_DwLoadFileCrcCheck_Object=MibScalar
dwLoadFileCrcCheck=_DwLoadFileCrcCheck_Object((1,3,6,1,4,1,34592,1,3,1,8,7),_DwLoadFileCrcCheck_Type())
dwLoadFileCrcCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:dwLoadFileCrcCheck.setStatus(_A)
_DwLoadFileCrcValue_Type=Unsigned32
_DwLoadFileCrcValue_Object=MibScalar
dwLoadFileCrcValue=_DwLoadFileCrcValue_Object((1,3,6,1,4,1,34592,1,3,1,8,8),_DwLoadFileCrcValue_Type())
dwLoadFileCrcValue.setMaxAccess(_C)
if mibBuilder.loadTexts:dwLoadFileCrcValue.setStatus(_A)
class _OperDeviceMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_OperDeviceMap_Type.__name__=_I
_OperDeviceMap_Object=MibScalar
operDeviceMap=_OperDeviceMap_Object((1,3,6,1,4,1,34592,1,3,1,8,9),_OperDeviceMap_Type())
operDeviceMap.setMaxAccess(_C)
if mibBuilder.loadTexts:operDeviceMap.setStatus(_A)
class _UpgradeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('paraErr',1),('initFtpErr',2),('transmitting',3),('transmitErr',4),('transmitOk',5),(_R,6),(_T,7),(_S,8),('uploading',9),('uploadErr',10),('uploadOk',11)))
_UpgradeStatus_Type.__name__=_E
_UpgradeStatus_Object=MibScalar
upgradeStatus=_UpgradeStatus_Object((1,3,6,1,4,1,34592,1,3,1,8,10),_UpgradeStatus_Type())
upgradeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upgradeStatus.setStatus(_A)
class _UpgradeOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('downloadFile',1),(_a,2),('reboot',3),('uploadFile',4)))
_UpgradeOperation_Type.__name__=_E
_UpgradeOperation_Object=MibScalar
upgradeOperation=_UpgradeOperation_Object((1,3,6,1,4,1,34592,1,3,1,8,11),_UpgradeOperation_Type())
upgradeOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:upgradeOperation.setStatus(_A)
_FtpProgress_Type=Integer32
_FtpProgress_Object=MibScalar
ftpProgress=_FtpProgress_Object((1,3,6,1,4,1,34592,1,3,1,8,12),_FtpProgress_Type())
ftpProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpProgress.setStatus(_A)
if mibBuilder.loadTexts:ftpProgress.setUnits('percent')
_FdSysConformance_ObjectIdentity=ObjectIdentity
fdSysConformance=_FdSysConformance_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,13))
_FdSystemGroups_ObjectIdentity=ObjectIdentity
fdSystemGroups=_FdSystemGroups_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,13,1))
_FdSystemCompliances_ObjectIdentity=ObjectIdentity
fdSystemCompliances=_FdSystemCompliances_ObjectIdentity((1,3,6,1,4,1,34592,1,3,1,13,2))
sysBaseManageGroup=ObjectGroup((1,3,6,1,4,1,34592,1,3,1,13,1,1))
sysBaseManageGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,'sysMTU'),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:sysBaseManageGroup.setStatus(_A)
chassisInfoGroup=ObjectGroup((1,3,6,1,4,1,34592,1,3,1,13,1,2))
chassisInfoGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:chassisInfoGroup.setStatus(_A)
cardModuleGroup=ObjectGroup((1,3,6,1,4,1,34592,1,3,1,13,1,3))
cardModuleGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:cardModuleGroup.setStatus(_A)
onuAuthGroup=ObjectGroup((1,3,6,1,4,1,34592,1,3,1,13,1,4))
onuAuthGroup.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,'macAttr'),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_K),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:onuAuthGroup.setStatus(_A)
userManageGroup=ObjectGroup((1,3,6,1,4,1,34592,1,3,1,13,1,5))
userManageGroup.setObjects(*((_B,'userName'),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:userManageGroup.setStatus(_A)
systemUpgradeGroup=ObjectGroup((1,3,6,1,4,1,34592,1,3,1,13,1,6))
systemUpgradeGroup.setObjects(*((_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:systemUpgradeGroup.setStatus(_A)
fdSystemCompliance=ModuleCompliance((1,3,6,1,4,1,34592,1,3,1,13,2,1))
fdSystemCompliance.setObjects(*((_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1)))
if mibBuilder.loadTexts:fdSystemCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'systemInfo':systemInfo,'sysBaseInfo':sysBaseInfo,_b:sysModel,_c:sysDesc,_d:sysLocation,_e:sysContact,_f:sysMajAlarmLed,_g:sysCriAlarmLed,_h:sysAlarmDesc,_A2:sysCpuUtilization,'sysMTU':sysMTU,'sysConfig':sysConfig,_i:consolePortSpd,_j:manageIpAddr,_k:manageNetMask,_l:manageGateway,_m:snmpReadCommunity,_n:snmpRWCommunity,_o:trapDstIpAddr1,_p:trapDstIpAddr2,_q:trapDstIpAddr3,_r:trapDstIpAddr4,_A1:sysOperate,_A0:outbandIpAddr,_z:outbandNetMask,'sysConfigurations':sysConfigurations,'cfgAutoBackup':cfgAutoBackup,_A3:sysAutoBackupEnable,_A4:sysAutoBackupType,_A5:sysAutoBackupInterval,_A6:sysAutoBackupServer,'cfgBackup':cfgBackup,_x:sysCfgBackupType,_w:sysCfgBackupServer,'cfgRestore':cfgRestore,_v:sysCfgRestoreType,_u:sysCfgRestoreServer,_y:sysCfgRestoreFilename,'sysLog':sysLog,_t:sysLogLevel,'sysLogTable':sysLogTable,'sysLogEntry':sysLogEntry,_P:sysLogEntryIndex,_s:sysLogEntryEnable,'date':date,'chassisInfo':chassisInfo,_A7:chassisType,_A8:chassisFactorySerial,_A9:chassisRevision,_AA:chassisTemperature,_AB:powerStatusBit,_AC:fanStatusBit,'cardModule':cardModule,'mainCard':mainCard,_AD:mainCardType,_AE:mainCardFactorySerial,_AF:mainCardHWRevision,_AG:mainCardSWVersion,_AH:mainCardRunningStatus,_AI:mainCardRunningTime,_AJ:mainCardOperate,'ponCard':ponCard,'ponCardTable':ponCardTable,'ponCardEntry':ponCardEntry,_Q:ponCardSlotId,_AK:ponCardType,_AL:ponCardFactorySerial,_AM:ponCardHwRev,_AN:ponCardFwVer,_AO:ponCardRunningStatus,_AP:ponCardRuningTime,_AQ:ponCardOperate,_AR:ponCardUpgradeStat,'onuAuth':onuAuth,_AS:authMethod,_AT:nonAuthOper,'onuAuthMacCfgTable':onuAuthMacCfgTable,'onuAuthMacCfgEntry':onuAuthMacCfgEntry,_U:authMacEntryId,_AU:beginMacAddr,_AV:endMacAddr,'macAttr':macAttr,_AW:onuAuthMacRowStatus,'nonAuthOnuListTable':nonAuthOnuListTable,'nonAuthOnuListEntry':nonAuthOnuListEntry,_V:nonAuthOnuMacIndex,_AX:nonAuthOnuMac,_AY:nonAuthOnuTries,_K:oltId,_Ag:authMethodV2,'onuAuthBlacklistMacCfgTable':onuAuthBlacklistMacCfgTable,'onuAuthBlacklistMacCfgEntry':onuAuthBlacklistMacCfgEntry,_W:authBlacklistMacEntryId,_Af:onuAuthBlacklistMacAddr,_Ae:onuAuthBlacklistMacCfgRowStatus,'onuAuthWhitelistMacCfgTable':onuAuthWhitelistMacCfgTable,'onuAuthWhitelistMacCfgEntry':onuAuthWhitelistMacCfgEntry,_X:authWhitelistMacEntryId,_Ad:onuAuthWhitelistMacAddr,_Ac:onuAuthWhitelistMacCfgRowStatus,'onuAuthLoidCfgTable':onuAuthLoidCfgTable,'onuAuthLoidCfgEntry':onuAuthLoidCfgEntry,_Y:authLoidEntryId,_Ab:onuAuthLoidStrings,_Aa:onuAuthPasswordStrings,_AZ:onuAuthLoidCfgRowStatus,'userManage':userManage,'userManageTable':userManageTable,'userManageEntry':userManageEntry,_Z:userId,'userName':userName,_Ah:userPassword,_Ai:userPermission,_Aj:userAccessDeviceMap,_Ak:loginTimeout,_Al:userEntryRowStatus,_a:upgrade,_Am:ftpServerIp,_An:ftpServerUserName,_Ao:ftpServerUserPasswd,_Ap:ftpOperFileName,_Aw:ftpOperTarget,_Aq:dwLoadFileCrcCheck,_Ar:dwLoadFileCrcValue,_As:operDeviceMap,_At:upgradeStatus,_Av:upgradeOperation,_Au:ftpProgress,'fdSysConformance':fdSysConformance,'fdSystemGroups':fdSystemGroups,_Ax:sysBaseManageGroup,_Ay:chassisInfoGroup,_Az:cardModuleGroup,_A_:onuAuthGroup,_B0:userManageGroup,_B1:systemUpgradeGroup,'fdSystemCompliances':fdSystemCompliances,'fdSystemCompliance':fdSystemCompliance})