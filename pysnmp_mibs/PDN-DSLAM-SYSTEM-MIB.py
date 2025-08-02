_e='loginFailureCount'
_d='sysDevConfigUserAccountIndex'
_c='sysDevUserAccountUserId'
_b='entCommunityName'
_a='trapDestAndPort'
_Z='trapCommunityName'
_Y='operator'
_X='administrator'
_W='telnet'
_V='console'
_U='loginTime'
_T='loginUserId'
_S='read-write'
_R='enable'
_Q='disable'
_P='loginFailureAccessApp'
_O='sysObjectID'
_N='SNMPv2-MIB'
_M='SwitchState'
_L='IdslClockMode'
_K='not-accessible'
_J='ifIndex'
_I='IF-MIB'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='DisplayString'
_E='read-only'
_D='PDN-DSLAM-SYSTEM-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
ifIndex,=mibBuilder.importSymbols(_I,_J)
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
IdslClockMode,SwitchState=mibBuilder.importSymbols('PDN-TC',_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysObjectID,=mibBuilder.importSymbols(_N,_O)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TAddress','TextualConvention')
pdn_dslam=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,24))
if mibBuilder.loadTexts:pdn_dslam.setRevisions(('1902-06-20 00:00','1902-06-05 00:00','1902-02-22 00:00'))
_SysDevDslamMIBObjects_ObjectIdentity=ObjectIdentity
sysDevDslamMIBObjects=_SysDevDslamMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,24,1))
_SysDevStats_ObjectIdentity=ObjectIdentity
sysDevStats=_SysDevStats_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,24,1,1))
_LoginHistTable_Object=MibTable
loginHistTable=_LoginHistTable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,1))
if mibBuilder.loadTexts:loginHistTable.setStatus(_A)
_LoginHistTableEntry_Object=MibTableRow
loginHistTableEntry=_LoginHistTableEntry_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,1,1))
loginHistTableEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:loginHistTableEntry.setStatus(_A)
_LoginUserId_Type=DisplayString
_LoginUserId_Object=MibTableColumn
loginUserId=_LoginUserId_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,1,1,1),_LoginUserId_Type())
loginUserId.setMaxAccess(_E)
if mibBuilder.loadTexts:loginUserId.setStatus(_A)
_LoginTime_Type=TimeTicks
_LoginTime_Object=MibTableColumn
loginTime=_LoginTime_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,1,1,2),_LoginTime_Type())
loginTime.setMaxAccess(_E)
if mibBuilder.loadTexts:loginTime.setStatus(_A)
class _LoginAccessApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_V,1),(_W,2),('ftp',3),('web',4),('modem',5)))
_LoginAccessApp_Type.__name__=_C
_LoginAccessApp_Object=MibTableColumn
loginAccessApp=_LoginAccessApp_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,1,1,3),_LoginAccessApp_Type())
loginAccessApp.setMaxAccess(_E)
if mibBuilder.loadTexts:loginAccessApp.setStatus(_A)
_LoginAccessHost_Type=IpAddress
_LoginAccessHost_Object=MibTableColumn
loginAccessHost=_LoginAccessHost_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,1,1,4),_LoginAccessHost_Type())
loginAccessHost.setMaxAccess(_E)
if mibBuilder.loadTexts:loginAccessHost.setStatus(_A)
class _LoginUserPriv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_LoginUserPriv_Type.__name__=_C
_LoginUserPriv_Object=MibTableColumn
loginUserPriv=_LoginUserPriv_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,1,1,5),_LoginUserPriv_Type())
loginUserPriv.setMaxAccess(_E)
if mibBuilder.loadTexts:loginUserPriv.setStatus(_A)
class _LoginStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_LoginStatus_Type.__name__=_C
_LoginStatus_Object=MibTableColumn
loginStatus=_LoginStatus_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,1,1,6),_LoginStatus_Type())
loginStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:loginStatus.setStatus(_A)
_LoginFailureCountTable_Object=MibTable
loginFailureCountTable=_LoginFailureCountTable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,2))
if mibBuilder.loadTexts:loginFailureCountTable.setStatus(_A)
_LoginFailureCountTableEntry_Object=MibTableRow
loginFailureCountTableEntry=_LoginFailureCountTableEntry_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,2,1))
loginFailureCountTableEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:loginFailureCountTableEntry.setStatus(_A)
class _LoginFailureAccessApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),('ftp',3)))
_LoginFailureAccessApp_Type.__name__=_C
_LoginFailureAccessApp_Object=MibTableColumn
loginFailureAccessApp=_LoginFailureAccessApp_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,2,1,1),_LoginFailureAccessApp_Type())
loginFailureAccessApp.setMaxAccess(_E)
if mibBuilder.loadTexts:loginFailureAccessApp.setStatus(_A)
_LoginFailureCount_Type=Counter32
_LoginFailureCount_Object=MibTableColumn
loginFailureCount=_LoginFailureCount_Object((1,3,6,1,4,1,1795,2,24,2,24,1,1,2,1,2),_LoginFailureCount_Type())
loginFailureCount.setMaxAccess(_E)
if mibBuilder.loadTexts:loginFailureCount.setStatus(_A)
_SysDevConfig_ObjectIdentity=ObjectIdentity
sysDevConfig=_SysDevConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,24,1,2))
class _EnablePowerSourceFailureAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_EnablePowerSourceFailureAlarm_Type.__name__=_C
_EnablePowerSourceFailureAlarm_Object=MibScalar
enablePowerSourceFailureAlarm=_EnablePowerSourceFailureAlarm_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,1),_EnablePowerSourceFailureAlarm_Type())
enablePowerSourceFailureAlarm.setMaxAccess(_S)
if mibBuilder.loadTexts:enablePowerSourceFailureAlarm.setStatus(_A)
_DevIfTable_Object=MibTable
devIfTable=_DevIfTable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,2))
if mibBuilder.loadTexts:devIfTable.setStatus(_A)
_DevIfTableEntry_Object=MibTableRow
devIfTableEntry=_DevIfTableEntry_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,2,1))
devIfTableEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:devIfTableEntry.setStatus(_A)
class _DevPacketDiscardPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOp',1),('mrrp',2),('lrrp',3)))
_DevPacketDiscardPolicy_Type.__name__=_C
_DevPacketDiscardPolicy_Object=MibTableColumn
devPacketDiscardPolicy=_DevPacketDiscardPolicy_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,2,1,1),_DevPacketDiscardPolicy_Type())
devPacketDiscardPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:devPacketDiscardPolicy.setStatus(_A)
class _DevLinkIntegrity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_Q,2),('none',3)))
_DevLinkIntegrity_Type.__name__=_C
_DevLinkIntegrity_Object=MibTableColumn
devLinkIntegrity=_DevLinkIntegrity_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,2,1,2),_DevLinkIntegrity_Type())
devLinkIntegrity.setMaxAccess(_B)
if mibBuilder.loadTexts:devLinkIntegrity.setStatus(_A)
_CommunityTrapAddressInfoTable_Object=MibTable
communityTrapAddressInfoTable=_CommunityTrapAddressInfoTable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,3))
if mibBuilder.loadTexts:communityTrapAddressInfoTable.setStatus(_A)
_CommunityTrapAddressInfoTableEntry_Object=MibTableRow
communityTrapAddressInfoTableEntry=_CommunityTrapAddressInfoTableEntry_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,3,1))
communityTrapAddressInfoTableEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:communityTrapAddressInfoTableEntry.setStatus(_A)
class _TrapCommunityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TrapCommunityName_Type.__name__=_F
_TrapCommunityName_Object=MibTableColumn
trapCommunityName=_TrapCommunityName_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,3,1,1),_TrapCommunityName_Type())
trapCommunityName.setMaxAccess(_K)
if mibBuilder.loadTexts:trapCommunityName.setStatus(_A)
_TrapDestAndPort_Type=TAddress
_TrapDestAndPort_Object=MibTableColumn
trapDestAndPort=_TrapDestAndPort_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,3,1,2),_TrapDestAndPort_Type())
trapDestAndPort.setMaxAccess(_K)
if mibBuilder.loadTexts:trapDestAndPort.setStatus(_A)
class _TrapsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_Q,2)))
_TrapsEnable_Type.__name__=_C
_TrapsEnable_Object=MibTableColumn
trapsEnable=_TrapsEnable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,3,1,3),_TrapsEnable_Type())
trapsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:trapsEnable.setStatus(_A)
_TrapRowStatus_Type=RowStatus
_TrapRowStatus_Object=MibTableColumn
trapRowStatus=_TrapRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,3,1,4),_TrapRowStatus_Type())
trapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:trapRowStatus.setStatus(_A)
_EntCommunityTable_Object=MibTable
entCommunityTable=_EntCommunityTable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,4))
if mibBuilder.loadTexts:entCommunityTable.setStatus(_A)
_EntCommunityTableEntry_Object=MibTableRow
entCommunityTableEntry=_EntCommunityTableEntry_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,4,1))
entCommunityTableEntry.setIndexNames((1,_D,_b))
if mibBuilder.loadTexts:entCommunityTableEntry.setStatus(_A)
class _EntCommunityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EntCommunityName_Type.__name__=_F
_EntCommunityName_Object=MibTableColumn
entCommunityName=_EntCommunityName_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,4,1,1),_EntCommunityName_Type())
entCommunityName.setMaxAccess(_K)
if mibBuilder.loadTexts:entCommunityName.setStatus(_A)
class _EntCommunityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_EntCommunityType_Type.__name__=_C
_EntCommunityType_Object=MibTableColumn
entCommunityType=_EntCommunityType_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,4,1,2),_EntCommunityType_Type())
entCommunityType.setMaxAccess(_B)
if mibBuilder.loadTexts:entCommunityType.setStatus(_A)
_EntCommunityRowStatus_Type=RowStatus
_EntCommunityRowStatus_Object=MibTableColumn
entCommunityRowStatus=_EntCommunityRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,4,1,3),_EntCommunityRowStatus_Type())
entCommunityRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:entCommunityRowStatus.setStatus(_A)
_SysDevUserAccountTable_Object=MibTable
sysDevUserAccountTable=_SysDevUserAccountTable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,5))
if mibBuilder.loadTexts:sysDevUserAccountTable.setStatus(_A)
_SysDevUserAccountEntry_Object=MibTableRow
sysDevUserAccountEntry=_SysDevUserAccountEntry_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,5,1))
sysDevUserAccountEntry.setIndexNames((1,_D,_c))
if mibBuilder.loadTexts:sysDevUserAccountEntry.setStatus(_A)
class _SysDevUserAccountUserId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,15))
_SysDevUserAccountUserId_Type.__name__=_F
_SysDevUserAccountUserId_Object=MibTableColumn
sysDevUserAccountUserId=_SysDevUserAccountUserId_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,5,1,1),_SysDevUserAccountUserId_Type())
sysDevUserAccountUserId.setMaxAccess(_K)
if mibBuilder.loadTexts:sysDevUserAccountUserId.setStatus(_A)
class _SysDevUserAccountPrivilege_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Y,1),(_X,2),('maintenance',3),('provisioning',4),('manufacturing',5)))
_SysDevUserAccountPrivilege_Type.__name__=_C
_SysDevUserAccountPrivilege_Object=MibTableColumn
sysDevUserAccountPrivilege=_SysDevUserAccountPrivilege_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,5,1,2),_SysDevUserAccountPrivilege_Type())
sysDevUserAccountPrivilege.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevUserAccountPrivilege.setStatus(_A)
class _SysDevUserAccountUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,15))
_SysDevUserAccountUserPassword_Type.__name__=_F
_SysDevUserAccountUserPassword_Object=MibTableColumn
sysDevUserAccountUserPassword=_SysDevUserAccountUserPassword_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,5,1,3),_SysDevUserAccountUserPassword_Type())
sysDevUserAccountUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevUserAccountUserPassword.setStatus(_A)
class _SysDevUserAccountAccessPartition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SysDevUserAccountAccessPartition_Type.__name__=_F
_SysDevUserAccountAccessPartition_Object=MibTableColumn
sysDevUserAccountAccessPartition=_SysDevUserAccountAccessPartition_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,5,1,4),_SysDevUserAccountAccessPartition_Type())
sysDevUserAccountAccessPartition.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevUserAccountAccessPartition.setStatus(_A)
_SysDevUserAccountRowStatus_Type=RowStatus
_SysDevUserAccountRowStatus_Object=MibTableColumn
sysDevUserAccountRowStatus=_SysDevUserAccountRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,5,1,5),_SysDevUserAccountRowStatus_Type())
sysDevUserAccountRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevUserAccountRowStatus.setStatus(_A)
_SysDevIDSLConfigTable_Object=MibTable
sysDevIDSLConfigTable=_SysDevIDSLConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,6))
if mibBuilder.loadTexts:sysDevIDSLConfigTable.setStatus(_A)
_SysDevIDSLConfigEntry_Object=MibTableRow
sysDevIDSLConfigEntry=_SysDevIDSLConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,6,1))
sysDevIDSLConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:sysDevIDSLConfigEntry.setStatus(_A)
class _SysDevIDSLConfigPrimaryNetClockMode_Type(IdslClockMode):defaultValue=1
_SysDevIDSLConfigPrimaryNetClockMode_Type.__name__=_L
_SysDevIDSLConfigPrimaryNetClockMode_Object=MibTableColumn
sysDevIDSLConfigPrimaryNetClockMode=_SysDevIDSLConfigPrimaryNetClockMode_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,6,1,1),_SysDevIDSLConfigPrimaryNetClockMode_Type())
sysDevIDSLConfigPrimaryNetClockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevIDSLConfigPrimaryNetClockMode.setStatus(_A)
class _SysDevIDSLConfigSecondaryNetClockMode_Type(IdslClockMode):defaultValue=1
_SysDevIDSLConfigSecondaryNetClockMode_Type.__name__=_L
_SysDevIDSLConfigSecondaryNetClockMode_Object=MibTableColumn
sysDevIDSLConfigSecondaryNetClockMode=_SysDevIDSLConfigSecondaryNetClockMode_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,6,1,2),_SysDevIDSLConfigSecondaryNetClockMode_Type())
sysDevIDSLConfigSecondaryNetClockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevIDSLConfigSecondaryNetClockMode.setStatus(_A)
_SysDevDslamSyslog_ObjectIdentity=ObjectIdentity
sysDevDslamSyslog=_SysDevDslamSyslog_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,24,1,2,7))
class _SysDevSyslogFtpServerXferStatsEnable_Type(SwitchState):defaultValue=2
_SysDevSyslogFtpServerXferStatsEnable_Type.__name__=_M
_SysDevSyslogFtpServerXferStatsEnable_Object=MibScalar
sysDevSyslogFtpServerXferStatsEnable=_SysDevSyslogFtpServerXferStatsEnable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,7,1),_SysDevSyslogFtpServerXferStatsEnable_Type())
sysDevSyslogFtpServerXferStatsEnable.setMaxAccess(_S)
if mibBuilder.loadTexts:sysDevSyslogFtpServerXferStatsEnable.setStatus(_A)
class _SysDevSyslogTftpServerXferStatsEnable_Type(SwitchState):defaultValue=2
_SysDevSyslogTftpServerXferStatsEnable_Type.__name__=_M
_SysDevSyslogTftpServerXferStatsEnable_Object=MibScalar
sysDevSyslogTftpServerXferStatsEnable=_SysDevSyslogTftpServerXferStatsEnable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,7,2),_SysDevSyslogTftpServerXferStatsEnable_Type())
sysDevSyslogTftpServerXferStatsEnable.setMaxAccess(_S)
if mibBuilder.loadTexts:sysDevSyslogTftpServerXferStatsEnable.setStatus(_A)
_SysDevConfigUserAccountTable_Object=MibTable
sysDevConfigUserAccountTable=_SysDevConfigUserAccountTable_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,8))
if mibBuilder.loadTexts:sysDevConfigUserAccountTable.setStatus(_A)
_SysDevConfigUserAccountEntry_Object=MibTableRow
sysDevConfigUserAccountEntry=_SysDevConfigUserAccountEntry_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,8,1))
sysDevConfigUserAccountEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:sysDevConfigUserAccountEntry.setStatus(_A)
_SysDevConfigUserAccountIndex_Type=Integer32
_SysDevConfigUserAccountIndex_Object=MibTableColumn
sysDevConfigUserAccountIndex=_SysDevConfigUserAccountIndex_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,8,1,1),_SysDevConfigUserAccountIndex_Type())
sysDevConfigUserAccountIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:sysDevConfigUserAccountIndex.setStatus(_A)
class _SysDevConfigUserAccountUserId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SysDevConfigUserAccountUserId_Type.__name__=_F
_SysDevConfigUserAccountUserId_Object=MibTableColumn
sysDevConfigUserAccountUserId=_SysDevConfigUserAccountUserId_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,8,1,2),_SysDevConfigUserAccountUserId_Type())
sysDevConfigUserAccountUserId.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevConfigUserAccountUserId.setStatus(_A)
class _SysDevConfigUserAccountPrivilegedPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysDevConfigUserAccountPrivilegedPassword_Type.__name__=_F
_SysDevConfigUserAccountPrivilegedPassword_Object=MibTableColumn
sysDevConfigUserAccountPrivilegedPassword=_SysDevConfigUserAccountPrivilegedPassword_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,8,1,3),_SysDevConfigUserAccountPrivilegedPassword_Type())
sysDevConfigUserAccountPrivilegedPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevConfigUserAccountPrivilegedPassword.setStatus(_A)
class _SysDevConfigUserAccountUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysDevConfigUserAccountUserPassword_Type.__name__=_F
_SysDevConfigUserAccountUserPassword_Object=MibTableColumn
sysDevConfigUserAccountUserPassword=_SysDevConfigUserAccountUserPassword_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,8,1,4),_SysDevConfigUserAccountUserPassword_Type())
sysDevConfigUserAccountUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevConfigUserAccountUserPassword.setStatus(_A)
_SysDevConfigUserAccountRowStatus_Type=RowStatus
_SysDevConfigUserAccountRowStatus_Object=MibTableColumn
sysDevConfigUserAccountRowStatus=_SysDevConfigUserAccountRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,8,1,5),_SysDevConfigUserAccountRowStatus_Type())
sysDevConfigUserAccountRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevConfigUserAccountRowStatus.setStatus(_A)
_SysDevConfigUserAccountIndexNext_Type=Integer32
_SysDevConfigUserAccountIndexNext_Object=MibScalar
sysDevConfigUserAccountIndexNext=_SysDevConfigUserAccountIndexNext_Object((1,3,6,1,4,1,1795,2,24,2,24,1,2,9),_SysDevConfigUserAccountIndexNext_Type())
sysDevConfigUserAccountIndexNext.setMaxAccess(_E)
if mibBuilder.loadTexts:sysDevConfigUserAccountIndexNext.setStatus(_A)
_SysDevDslamMIBTraps_ObjectIdentity=ObjectIdentity
sysDevDslamMIBTraps=_SysDevDslamMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,24,2))
cCN=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,7))
cCN.setObjects((_I,_J))
if mibBuilder.loadTexts:cCN.setStatus(_A)
authenticationFailureTrap=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,8))
authenticationFailureTrap.setObjects(*((_D,_P),(_D,_e)))
if mibBuilder.loadTexts:authenticationFailureTrap.setStatus(_A)
fanModuleFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,9))
if mibBuilder.loadTexts:fanModuleFailure.setStatus(_A)
powerSourceAFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,10))
if mibBuilder.loadTexts:powerSourceAFailure.setStatus(_A)
slotPollFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,11))
slotPollFailure.setObjects((_G,_H))
if mibBuilder.loadTexts:slotPollFailure.setStatus(_A)
ethernetJabber=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,12))
ethernetJabber.setObjects((_I,_J))
if mibBuilder.loadTexts:ethernetJabber.setStatus(_A)
ethernetJumbos=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,13))
ethernetJumbos.setObjects((_I,_J))
if mibBuilder.loadTexts:ethernetJumbos.setStatus(_A)
ethernetRunts=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,14))
ethernetRunts.setObjects((_I,_J))
if mibBuilder.loadTexts:ethernetRunts.setStatus(_A)
powerSourceBFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,17))
if mibBuilder.loadTexts:powerSourceBFailure.setStatus(_A)
nonIpConservativeCardDetected=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,18))
nonIpConservativeCardDetected.setObjects((_G,_H))
if mibBuilder.loadTexts:nonIpConservativeCardDetected.setStatus(_A)
nonSupportedMCC=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,20))
nonSupportedMCC.setObjects((_N,_O))
if mibBuilder.loadTexts:nonSupportedMCC.setStatus(_A)
nonSupportedChassis=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,21))
nonSupportedChassis.setObjects((_N,_O))
if mibBuilder.loadTexts:nonSupportedChassis.setStatus(_A)
fanEntityModuleFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,22))
fanEntityModuleFailure.setObjects((_G,_H))
if mibBuilder.loadTexts:fanEntityModuleFailure.setStatus(_A)
fanModuleOperational=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,109))
if mibBuilder.loadTexts:fanModuleOperational.setStatus(_A)
powerSourceAOperational=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,110))
if mibBuilder.loadTexts:powerSourceAOperational.setStatus(_A)
newCardDetected=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,111))
newCardDetected.setObjects((_G,_H))
if mibBuilder.loadTexts:newCardDetected.setStatus(_A)
ethernetJabberClear=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,112))
ethernetJabberClear.setObjects((_I,_J))
if mibBuilder.loadTexts:ethernetJabberClear.setStatus(_A)
powerSourceBOperational=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,117))
if mibBuilder.loadTexts:powerSourceBOperational.setStatus(_A)
fanEntityModuleOperational=NotificationType((1,3,6,1,4,1,1795,2,24,2,24,2,122))
fanEntityModuleOperational.setObjects((_G,_H))
if mibBuilder.loadTexts:fanEntityModuleOperational.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'pdn-dslam':pdn_dslam,'sysDevDslamMIBObjects':sysDevDslamMIBObjects,'sysDevStats':sysDevStats,'loginHistTable':loginHistTable,'loginHistTableEntry':loginHistTableEntry,_T:loginUserId,_U:loginTime,'loginAccessApp':loginAccessApp,'loginAccessHost':loginAccessHost,'loginUserPriv':loginUserPriv,'loginStatus':loginStatus,'loginFailureCountTable':loginFailureCountTable,'loginFailureCountTableEntry':loginFailureCountTableEntry,_P:loginFailureAccessApp,_e:loginFailureCount,'sysDevConfig':sysDevConfig,'enablePowerSourceFailureAlarm':enablePowerSourceFailureAlarm,'devIfTable':devIfTable,'devIfTableEntry':devIfTableEntry,'devPacketDiscardPolicy':devPacketDiscardPolicy,'devLinkIntegrity':devLinkIntegrity,'communityTrapAddressInfoTable':communityTrapAddressInfoTable,'communityTrapAddressInfoTableEntry':communityTrapAddressInfoTableEntry,_Z:trapCommunityName,_a:trapDestAndPort,'trapsEnable':trapsEnable,'trapRowStatus':trapRowStatus,'entCommunityTable':entCommunityTable,'entCommunityTableEntry':entCommunityTableEntry,_b:entCommunityName,'entCommunityType':entCommunityType,'entCommunityRowStatus':entCommunityRowStatus,'sysDevUserAccountTable':sysDevUserAccountTable,'sysDevUserAccountEntry':sysDevUserAccountEntry,_c:sysDevUserAccountUserId,'sysDevUserAccountPrivilege':sysDevUserAccountPrivilege,'sysDevUserAccountUserPassword':sysDevUserAccountUserPassword,'sysDevUserAccountAccessPartition':sysDevUserAccountAccessPartition,'sysDevUserAccountRowStatus':sysDevUserAccountRowStatus,'sysDevIDSLConfigTable':sysDevIDSLConfigTable,'sysDevIDSLConfigEntry':sysDevIDSLConfigEntry,'sysDevIDSLConfigPrimaryNetClockMode':sysDevIDSLConfigPrimaryNetClockMode,'sysDevIDSLConfigSecondaryNetClockMode':sysDevIDSLConfigSecondaryNetClockMode,'sysDevDslamSyslog':sysDevDslamSyslog,'sysDevSyslogFtpServerXferStatsEnable':sysDevSyslogFtpServerXferStatsEnable,'sysDevSyslogTftpServerXferStatsEnable':sysDevSyslogTftpServerXferStatsEnable,'sysDevConfigUserAccountTable':sysDevConfigUserAccountTable,'sysDevConfigUserAccountEntry':sysDevConfigUserAccountEntry,_d:sysDevConfigUserAccountIndex,'sysDevConfigUserAccountUserId':sysDevConfigUserAccountUserId,'sysDevConfigUserAccountPrivilegedPassword':sysDevConfigUserAccountPrivilegedPassword,'sysDevConfigUserAccountUserPassword':sysDevConfigUserAccountUserPassword,'sysDevConfigUserAccountRowStatus':sysDevConfigUserAccountRowStatus,'sysDevConfigUserAccountIndexNext':sysDevConfigUserAccountIndexNext,'sysDevDslamMIBTraps':sysDevDslamMIBTraps,'cCN':cCN,'authenticationFailureTrap':authenticationFailureTrap,'fanModuleFailure':fanModuleFailure,'powerSourceAFailure':powerSourceAFailure,'slotPollFailure':slotPollFailure,'ethernetJabber':ethernetJabber,'ethernetJumbos':ethernetJumbos,'ethernetRunts':ethernetRunts,'powerSourceBFailure':powerSourceBFailure,'nonIpConservativeCardDetected':nonIpConservativeCardDetected,'nonSupportedMCC':nonSupportedMCC,'nonSupportedChassis':nonSupportedChassis,'fanEntityModuleFailure':fanEntityModuleFailure,'fanModuleOperational':fanModuleOperational,'powerSourceAOperational':powerSourceAOperational,'newCardDetected':newCardDetected,'ethernetJabberClear':ethernetJabberClear,'powerSourceBOperational':powerSourceBOperational,'fanEntityModuleOperational':fanEntityModuleOperational})