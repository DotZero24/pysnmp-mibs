_w='qtechCapwapAppMIBGroup'
_v='qtechNeedConfiguration'
_u='qtechAssignedIPAddress'
_t='qtechAppAdminTargetLevel'
_s='qtechAppAdminLoginFailReason'
_r='qtechAppAdminInfoConfigContext'
_q='qtechAppAdminInfoLoginType'
_p='qtechSyslogServerStatus'
_o='qtechSyslogServerVrfName'
_n='qtechSyslogServerAddr'
_m='qtechAppSyslogStatus'
_l='qtechAppSyslogVrfName'
_k='qtechAppSyslogSvrNetPort'
_j='qtechAppSyslogReportEventLevel'
_i='qtechAppSyslogSvcEnable'
_h='qtechAppRcvToDefConfig'
_g='qtechAppPollTimeOfLast'
_f='qtechAppAdminStatus'
_e='qtechAppAdminPriLevel'
_d='qtechAppAdminPwd'
_c='qtechAppHeartbeatPeriod'
_b='qtechAppHeartbeatOnOff'
_a='qtechAppTrapType'
_Z='qtechSyslogServerIndex'
_Y='sysObjectID'
_X='SNMPv2-MIB'
_W='qtechSystemSerialno'
_V='QTECH-SYSTEM-MIB'
_U='qtechDeviceMacAddress'
_T='QTECH-ENTITY-MIB'
_S='OctetString'
_R='qtechAppAdminTerminalInfo'
_Q='qtechAppConfigParseErrReason'
_P='qtechAppConfigFileName'
_O='qtechAppHeartbeatTimeStamp'
_N='qtechAppHeartbeatIpAddr'
_M='qtechAppSyslogSvrNetAddr'
_L='qtechAppSyslogSvrNetType'
_K='qtechAppAdminName'
_J='qtechAppAdminInfoIpAddr'
_I='qtechAppAdminInfoName'
_H='read-write'
_G='DisplayString'
_F='not-accessible'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='QTECH-CAPWAP-APP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
qtechDeviceMacAddress,=mibBuilder.importSymbols(_T,_U)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
qtechSystemSerialno,=mibBuilder.importSymbols(_V,_W)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysObjectID,=mibBuilder.importSymbols(_X,_Y)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TAddress','TextualConvention','TruthValue')
qtechCapwapAppMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,87))
if mibBuilder.loadTexts:qtechCapwapAppMIB.setRevisions(('2010-06-04 00:00',))
_QtechCapwapAppMIBObjects_ObjectIdentity=ObjectIdentity
qtechCapwapAppMIBObjects=_QtechCapwapAppMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1))
_QtechAppHeartbeatMIBObjects_ObjectIdentity=ObjectIdentity
qtechAppHeartbeatMIBObjects=_QtechAppHeartbeatMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,1))
_QtechAppHeartbeatMIBTraps_ObjectIdentity=ObjectIdentity
qtechAppHeartbeatMIBTraps=_QtechAppHeartbeatMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,1,0))
class _QtechAppHeartbeatOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_QtechAppHeartbeatOnOff_Type.__name__=_D
_QtechAppHeartbeatOnOff_Object=MibScalar
qtechAppHeartbeatOnOff=_QtechAppHeartbeatOnOff_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,1,1),_QtechAppHeartbeatOnOff_Type())
qtechAppHeartbeatOnOff.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechAppHeartbeatOnOff.setStatus(_A)
class _QtechAppHeartbeatPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_QtechAppHeartbeatPeriod_Type.__name__=_D
_QtechAppHeartbeatPeriod_Object=MibScalar
qtechAppHeartbeatPeriod=_QtechAppHeartbeatPeriod_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,1,2),_QtechAppHeartbeatPeriod_Type())
qtechAppHeartbeatPeriod.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechAppHeartbeatPeriod.setStatus(_A)
_QtechAppHeartbeatIpAddr_Type=IpAddress
_QtechAppHeartbeatIpAddr_Object=MibScalar
qtechAppHeartbeatIpAddr=_QtechAppHeartbeatIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,1,3),_QtechAppHeartbeatIpAddr_Type())
qtechAppHeartbeatIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppHeartbeatIpAddr.setStatus(_A)
_QtechAppHeartbeatTimeStamp_Type=TimeTicks
_QtechAppHeartbeatTimeStamp_Object=MibScalar
qtechAppHeartbeatTimeStamp=_QtechAppHeartbeatTimeStamp_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,1,4),_QtechAppHeartbeatTimeStamp_Type())
qtechAppHeartbeatTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppHeartbeatTimeStamp.setStatus(_A)
_QtechAppAdminInfoMIBObjects_ObjectIdentity=ObjectIdentity
qtechAppAdminInfoMIBObjects=_QtechAppAdminInfoMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,2))
_QtechAppAdminMIBTraps_ObjectIdentity=ObjectIdentity
qtechAppAdminMIBTraps=_QtechAppAdminMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,0))
_QtechAppAdminInfoTable_Object=MibTable
qtechAppAdminInfoTable=_QtechAppAdminInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,1))
if mibBuilder.loadTexts:qtechAppAdminInfoTable.setStatus(_A)
_QtechAppAdminInfoEntry_Object=MibTableRow
qtechAppAdminInfoEntry=_QtechAppAdminInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,1,1))
qtechAppAdminInfoEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechAppAdminInfoEntry.setStatus(_A)
class _QtechAppAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechAppAdminName_Type.__name__=_G
_QtechAppAdminName_Object=MibTableColumn
qtechAppAdminName=_QtechAppAdminName_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,1,1,1),_QtechAppAdminName_Type())
qtechAppAdminName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppAdminName.setStatus(_A)
class _QtechAppAdminPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_QtechAppAdminPwd_Type.__name__=_G
_QtechAppAdminPwd_Object=MibTableColumn
qtechAppAdminPwd=_QtechAppAdminPwd_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,1,1,2),_QtechAppAdminPwd_Type())
qtechAppAdminPwd.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAppAdminPwd.setStatus(_A)
_QtechAppAdminPriLevel_Type=Integer32
_QtechAppAdminPriLevel_Object=MibTableColumn
qtechAppAdminPriLevel=_QtechAppAdminPriLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,1,1,3),_QtechAppAdminPriLevel_Type())
qtechAppAdminPriLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAppAdminPriLevel.setStatus(_A)
_QtechAppAdminStatus_Type=RowStatus
_QtechAppAdminStatus_Object=MibTableColumn
qtechAppAdminStatus=_QtechAppAdminStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,1,1,4),_QtechAppAdminStatus_Type())
qtechAppAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAppAdminStatus.setStatus(_A)
class _QtechAppAdminInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechAppAdminInfoName_Type.__name__=_G
_QtechAppAdminInfoName_Object=MibScalar
qtechAppAdminInfoName=_QtechAppAdminInfoName_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,2),_QtechAppAdminInfoName_Type())
qtechAppAdminInfoName.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechAppAdminInfoName.setStatus(_A)
_QtechAppAdminInfoIpAddr_Type=IpAddress
_QtechAppAdminInfoIpAddr_Object=MibScalar
qtechAppAdminInfoIpAddr=_QtechAppAdminInfoIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,3),_QtechAppAdminInfoIpAddr_Type())
qtechAppAdminInfoIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechAppAdminInfoIpAddr.setStatus(_A)
class _QtechAppAdminInfoConfigContext_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,512))
_QtechAppAdminInfoConfigContext_Type.__name__=_S
_QtechAppAdminInfoConfigContext_Object=MibScalar
qtechAppAdminInfoConfigContext=_QtechAppAdminInfoConfigContext_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,4),_QtechAppAdminInfoConfigContext_Type())
qtechAppAdminInfoConfigContext.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechAppAdminInfoConfigContext.setStatus(_A)
class _QtechAppAdminInfoLoginType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechAppAdminInfoLoginType_Type.__name__=_G
_QtechAppAdminInfoLoginType_Object=MibScalar
qtechAppAdminInfoLoginType=_QtechAppAdminInfoLoginType_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,5),_QtechAppAdminInfoLoginType_Type())
qtechAppAdminInfoLoginType.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechAppAdminInfoLoginType.setStatus(_A)
class _QtechAppAdminTerminalInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechAppAdminTerminalInfo_Type.__name__=_G
_QtechAppAdminTerminalInfo_Object=MibScalar
qtechAppAdminTerminalInfo=_QtechAppAdminTerminalInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,6),_QtechAppAdminTerminalInfo_Type())
qtechAppAdminTerminalInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechAppAdminTerminalInfo.setStatus(_A)
_QtechAppAdminLoginFailReason_Type=Integer32
_QtechAppAdminLoginFailReason_Object=MibScalar
qtechAppAdminLoginFailReason=_QtechAppAdminLoginFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,7),_QtechAppAdminLoginFailReason_Type())
qtechAppAdminLoginFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechAppAdminLoginFailReason.setStatus(_A)
class _QtechAppAdminTargetLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QtechAppAdminTargetLevel_Type.__name__=_D
_QtechAppAdminTargetLevel_Object=MibScalar
qtechAppAdminTargetLevel=_QtechAppAdminTargetLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,8),_QtechAppAdminTargetLevel_Type())
qtechAppAdminTargetLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechAppAdminTargetLevel.setStatus(_A)
_QtechAppPollTimeMIBObjects_ObjectIdentity=ObjectIdentity
qtechAppPollTimeMIBObjects=_QtechAppPollTimeMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,3))
_QtechAppPollTimeOfLast_Type=TimeTicks
_QtechAppPollTimeOfLast_Object=MibScalar
qtechAppPollTimeOfLast=_QtechAppPollTimeOfLast_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,3,1),_QtechAppPollTimeOfLast_Type())
qtechAppPollTimeOfLast.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppPollTimeOfLast.setStatus(_A)
_QtechAppConfigMIBObjects_ObjectIdentity=ObjectIdentity
qtechAppConfigMIBObjects=_QtechAppConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,4))
_QtechAppConfigMIBTraps_ObjectIdentity=ObjectIdentity
qtechAppConfigMIBTraps=_QtechAppConfigMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,4,0))
class _QtechAppRcvToDefConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('reset',1)))
_QtechAppRcvToDefConfig_Type.__name__=_D
_QtechAppRcvToDefConfig_Object=MibScalar
qtechAppRcvToDefConfig=_QtechAppRcvToDefConfig_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,4,1),_QtechAppRcvToDefConfig_Type())
qtechAppRcvToDefConfig.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechAppRcvToDefConfig.setStatus(_A)
class _QtechAppConfigFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechAppConfigFileName_Type.__name__=_G
_QtechAppConfigFileName_Object=MibScalar
qtechAppConfigFileName=_QtechAppConfigFileName_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,4,2),_QtechAppConfigFileName_Type())
qtechAppConfigFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppConfigFileName.setStatus(_A)
class _QtechAppConfigParseErrReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_QtechAppConfigParseErrReason_Type.__name__=_G
_QtechAppConfigParseErrReason_Object=MibScalar
qtechAppConfigParseErrReason=_QtechAppConfigParseErrReason_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,4,3),_QtechAppConfigParseErrReason_Type())
qtechAppConfigParseErrReason.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppConfigParseErrReason.setStatus(_A)
_QtechAppSyslogMIBObjects_ObjectIdentity=ObjectIdentity
qtechAppSyslogMIBObjects=_QtechAppSyslogMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,5))
_QtechAppSyslogSvcEnable_Type=TruthValue
_QtechAppSyslogSvcEnable_Object=MibScalar
qtechAppSyslogSvcEnable=_QtechAppSyslogSvcEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,1),_QtechAppSyslogSvcEnable_Type())
qtechAppSyslogSvcEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechAppSyslogSvcEnable.setStatus(_A)
_QtechAppSyslogReportEventLevel_Type=Integer32
_QtechAppSyslogReportEventLevel_Object=MibScalar
qtechAppSyslogReportEventLevel=_QtechAppSyslogReportEventLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,2),_QtechAppSyslogReportEventLevel_Type())
qtechAppSyslogReportEventLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechAppSyslogReportEventLevel.setStatus(_A)
_QtechAppSyslogSvrCfgTable_Object=MibTable
qtechAppSyslogSvrCfgTable=_QtechAppSyslogSvrCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,3))
if mibBuilder.loadTexts:qtechAppSyslogSvrCfgTable.setStatus(_A)
_QtechAppSyslogSvrCfgEntry_Object=MibTableRow
qtechAppSyslogSvrCfgEntry=_QtechAppSyslogSvrCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,3,1))
qtechAppSyslogSvrCfgEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:qtechAppSyslogSvrCfgEntry.setStatus(_A)
_QtechAppSyslogSvrNetType_Type=InetAddressType
_QtechAppSyslogSvrNetType_Object=MibTableColumn
qtechAppSyslogSvrNetType=_QtechAppSyslogSvrNetType_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,3,1,1),_QtechAppSyslogSvrNetType_Type())
qtechAppSyslogSvrNetType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppSyslogSvrNetType.setStatus(_A)
_QtechAppSyslogSvrNetAddr_Type=InetAddress
_QtechAppSyslogSvrNetAddr_Object=MibTableColumn
qtechAppSyslogSvrNetAddr=_QtechAppSyslogSvrNetAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,3,1,2),_QtechAppSyslogSvrNetAddr_Type())
qtechAppSyslogSvrNetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppSyslogSvrNetAddr.setStatus(_A)
_QtechAppSyslogSvrNetPort_Type=Unsigned32
_QtechAppSyslogSvrNetPort_Object=MibTableColumn
qtechAppSyslogSvrNetPort=_QtechAppSyslogSvrNetPort_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,3,1,3),_QtechAppSyslogSvrNetPort_Type())
qtechAppSyslogSvrNetPort.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAppSyslogSvrNetPort.setStatus(_A)
_QtechAppSyslogVrfName_Type=DisplayString
_QtechAppSyslogVrfName_Object=MibTableColumn
qtechAppSyslogVrfName=_QtechAppSyslogVrfName_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,3,1,4),_QtechAppSyslogVrfName_Type())
qtechAppSyslogVrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAppSyslogVrfName.setStatus(_A)
_QtechAppSyslogStatus_Type=RowStatus
_QtechAppSyslogStatus_Object=MibTableColumn
qtechAppSyslogStatus=_QtechAppSyslogStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,3,1,5),_QtechAppSyslogStatus_Type())
qtechAppSyslogStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAppSyslogStatus.setStatus(_A)
_QtechSyslogServerAddrInfoTable_Object=MibTable
qtechSyslogServerAddrInfoTable=_QtechSyslogServerAddrInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,4))
if mibBuilder.loadTexts:qtechSyslogServerAddrInfoTable.setStatus(_A)
_QtechSyslogServerAddrInfoEntry_Object=MibTableRow
qtechSyslogServerAddrInfoEntry=_QtechSyslogServerAddrInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,4,1))
qtechSyslogServerAddrInfoEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:qtechSyslogServerAddrInfoEntry.setStatus(_A)
_QtechSyslogServerIndex_Type=Integer32
_QtechSyslogServerIndex_Object=MibTableColumn
qtechSyslogServerIndex=_QtechSyslogServerIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,4,1,1),_QtechSyslogServerIndex_Type())
qtechSyslogServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyslogServerIndex.setStatus(_A)
_QtechSyslogServerAddr_Type=TAddress
_QtechSyslogServerAddr_Object=MibTableColumn
qtechSyslogServerAddr=_QtechSyslogServerAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,4,1,2),_QtechSyslogServerAddr_Type())
qtechSyslogServerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSyslogServerAddr.setStatus(_A)
_QtechSyslogServerVrfName_Type=DisplayString
_QtechSyslogServerVrfName_Object=MibTableColumn
qtechSyslogServerVrfName=_QtechSyslogServerVrfName_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,4,1,3),_QtechSyslogServerVrfName_Type())
qtechSyslogServerVrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSyslogServerVrfName.setStatus(_A)
_QtechSyslogServerStatus_Type=RowStatus
_QtechSyslogServerStatus_Object=MibTableColumn
qtechSyslogServerStatus=_QtechSyslogServerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,5,4,1,4),_QtechSyslogServerStatus_Type())
qtechSyslogServerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSyslogServerStatus.setStatus(_A)
_QtechAppTrapActionMIBObjects_ObjectIdentity=ObjectIdentity
qtechAppTrapActionMIBObjects=_QtechAppTrapActionMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,6))
class _QtechAppTrapActionEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disableSendTrap',0),('enableSendTrap',1)))
_QtechAppTrapActionEnable_Type.__name__=_D
_QtechAppTrapActionEnable_Object=MibScalar
qtechAppTrapActionEnable=_QtechAppTrapActionEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,6,1),_QtechAppTrapActionEnable_Type())
qtechAppTrapActionEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechAppTrapActionEnable.setStatus(_A)
_QtechAppTrapActionTable_Object=MibTable
qtechAppTrapActionTable=_QtechAppTrapActionTable_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,6,2))
if mibBuilder.loadTexts:qtechAppTrapActionTable.setStatus(_A)
_QtechAppTrapActionEntry_Object=MibTableRow
qtechAppTrapActionEntry=_QtechAppTrapActionEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,6,2,1))
qtechAppTrapActionEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:qtechAppTrapActionEntry.setStatus(_A)
class _QtechAppTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202)));namedValues=NamedValues(*(('gencoldstart',1),('genwarmstart',2),('genlinkdown',3),('genlinkup',4),('genauthenfail',5),('genegpnbloss',6),('spenewroot',7),('spetopchange',8),('spehardchange',9),('speportsecuviolation',10),('spestormviolation',11),('spemacnotification',12),('spevrrpnewmaster',13),('spevrrpauthfailure',14),('spepowerstatetrans',15),('spefanstatetrans',16),('speospf',17),('speospfvifstatechange',18),('speospfnbrstatechange',19),('speospfvifnbrstatechange',20),('speospfifconfigerror',21),('speospfvifconfigerror',22),('speospfifauthfailure',23),('speospfvifauthfailure',24),('speospfifrxbadpacket',25),('speospfvifrxbadpacket',26),('speospftxretransmit',27),('speospfviftxretransmit',28),('speospforiginatelsa',29),('speospfmaxagelsa',30),('speospflsdboverflow',31),('speospflsdbapproachingoverflow',32),('speospfifstatechange',33),('spebgpestablished',34),('spebgpbackwardtransition',35),('speisisdatabaseoverload',36),('speisismanualaddressdrop',37),('speisiscorruptedlspdetected',38),('speisisattempttoexceedmaxseq',39),('speisisidlenmismatch',40),('speisismaxareaaddrmismatch',41),('speisisownlsppurge',42),('speisisseqnumberskip',43),('speisisauthtypefailure',44),('speisisauthfailure',45),('speisisversionskew',46),('speisisareamismatch',47),('speisisrejectedadj',48),('speisislsptoolargetopropagate',49),('speisisoriglspbufsizemismatch',50),('speisisprotocolsupportedmismatch',51),('speisisadjchange',52),('spepim',53),('speigmp',54),('spedvmrp',55),('speentitychange',56),('specluster',57),('spedetectipviolation',58),('spelinestate',59),('spesysguard',60),('spernfpmsgtrap',61),('sperrmclientsfailedtrap',62),('sperrmloadfailedtrap',63),('sperrmnoisefailedtrap',64),('sperrminterferencefailedtrap',65),('sperrmperformancefailedtrap',66),('sperrmclientspasstrap',67),('sperrmloadpasstrap',68),('sperrmnoisepasstrap',69),('sperrminterferencepasstrap',70),('sperrmperformancepasstrap',71),('sperrmchannelchangetrap',72),('sperrmtxpowerchangetrap',73),('sperrmleaderachangetrap',74),('sperrmleaderbchangetrap',75),('sperrmdfsfreecountatrap',76),('sperrmdfsfreecountbtrap',77),('sperrmneighborapintertrap',78),('sperrmstationintertrap',79),('sperrmotherdiveceintertrap',80),('rmonalarmfallingtrap',81),('rmonalarmrisingtrap',82),('smpframerelaytrap',83),('priventitytrans',84),('privtemperaturetrans',85),('speipv6ifstatechange',86),('psmachashconflicttrap',87),('privwebauthuserleave',88),('radiusauthserverdowntrap',89),('radiusacctserverdowntrap',90),('configurationerrortrap',91),('cpuusagetoohightrap',92),('cpuusagetoohighrecovtrap',93),('memusagetoohightrap',94),('memusagetoohighrecovtrap',95),('systmcoldstarttrap',96),('ipaddrchangetrap',97),('apmtworkmodechgtrap',98),('apswupdatefailtrap',99),('ssidkeyconflicttrap',100),('fatapheartbeattrap',101),('acconfigurationerrortrap',102),('accpuusagetoohightrap',103),('accpuusagetoohighrecovtrap',104),('acmemusagetoohightrap',105),('acmemusagetoohighrecovtrap',106),('acofflinetrap',107),('aconlinetrap',108),('acapmtworkmodechgtrap',109),('acapswupdatefailtrap',110),('acssidkeyconflicttrap',111),('acfatapheartbeattrap',112),('staauthfailtrap',113),('staassofailtrap',114),('acstaauthfailtrap',115),('acstaassofailtrap',116),('invalidcertinvadetrap',117),('repaccacktrap',118),('tamperattacktrap',119),('lowersafeattacktrap',120),('addrredirectiontrap',121),('acinvalidcertinvadetrap',122),('acrepaccacktrap',123),('actamperattacktrap',124),('aclowersafeattacktrap',125),('acaddrredirectiontrap',126),('widsieee80211connect',127),('widsieee80211disconnect',128),('widsieee80211reauthentication',129),('widsieee80211authenticationfailure',130),('widsieee80211connectfailure',131),('apcointerfdetectedtrap',132),('apcointerfcleartrap',133),('apnerborinterfdetectedtrap',134),('apneiborinterfcleartrap',135),('stainterfdetectedtrap',136),('stainterfcleartrap',137),('otherdeviceinterfdetectedtrap',138),('otherdevinterfcleartrap',139),('radiodowntrap',140),('radiodownrecovtrap',141),('apstafulltrap',142),('apstafullrecovertrap',143),('apmtrdochanlchgtrap',144),('acapcointerfdetectedtrap',145),('acapcointerfcleartrap',146),('acapnerborinterfdetectedtrap',147),('acapneiborinterfcleartrap',148),('acstainterfdetectedtrap',149),('acstainterfcleartrap',150),('acotherdeviceinterfdetectedtrap',151),('acotherdevinterfcleartrap',152),('acradiodowntrap',153),('acradiodownrecovtrap',154),('acapstafulltrap',155),('acapstafullrecovertrap',156),('acapmtrdochanlchgtrap',157),('acspeciousdevicedetecttrap',158),('acrxpackage',159),('accpuusage',160),('capwapbasechanup',161),('capwapbasechandown',162),('capwapbasedecrypterrorreport',163),('capwapbasejoinfail',164),('capwapbaseimageupgradefail',165),('capwapbaseconifgmsgerror',166),('capwapbaseradiooperstatu',167),('capwapbaseauthenfail',168),('apmgmtaptimestamp',169),('apmgmtstaoper',170),('apmgmtmbchange',171),('apmgmtapswupdtfail',172),('widswarninginfo',173),('privcmccportalunavailable',174),('privipaddrchange',175),('dhcppoolexhaust',176),('dhcppoolnoexhaust',177),('speheartbeatperiodtrap',178),('tftpupgradefailed',179),('syscpuhigh',180),('syscpuhighrecov',181),('systemperaturehigh',182),('systemperaturehighrecov',183),('sysmemoryhigh',184),('sysmemoryhighrecov',185),('speconfigmodifytrap',186),('speconfigparseerrtrap',187),('apmgmtstaactoverthrehold',188),('apmgmtstadisactoverthredhold',189),('apmgmtstaroamtotaloverthredhlod',190),('apmgmtstaroamoerminoverthredhold',191),('apmgmtapwritebuffero',192),('apmgmtacheartbeat',193),('apmgmtacpowerstatus',194),('radiusauthserverrecovertrap',195),('radiusacctserverrecovertrap',196),('privcmccportalavailable',197),('sysapcpuhigh',198),('sysapcpuhighrecov',199),('sysapmemoryhigh',200),('sysapmemoryhighrecov',201),('syssystemreset',202)))
_QtechAppTrapType_Type.__name__=_D
_QtechAppTrapType_Object=MibTableColumn
qtechAppTrapType=_QtechAppTrapType_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,6,2,1,1),_QtechAppTrapType_Type())
qtechAppTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAppTrapType.setStatus(_A)
class _QtechAppTrapAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_QtechAppTrapAction_Type.__name__=_D
_QtechAppTrapAction_Object=MibTableColumn
qtechAppTrapAction=_QtechAppTrapAction_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,6,2,1,2),_QtechAppTrapAction_Type())
qtechAppTrapAction.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechAppTrapAction.setStatus(_A)
_QtechAppTrapDescr_Type=DisplayString
_QtechAppTrapDescr_Object=MibTableColumn
qtechAppTrapDescr=_QtechAppTrapDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,6,2,1,3),_QtechAppTrapDescr_Type())
qtechAppTrapDescr.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechAppTrapDescr.setStatus(_A)
_QtechZCMMIBObjects_ObjectIdentity=ObjectIdentity
qtechZCMMIBObjects=_QtechZCMMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,7))
_QtechZCMMIBTraps_ObjectIdentity=ObjectIdentity
qtechZCMMIBTraps=_QtechZCMMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,1,7,0))
_QtechAssignedIPAddress_Type=IpAddress
_QtechAssignedIPAddress_Object=MibScalar
qtechAssignedIPAddress=_QtechAssignedIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,7,1),_QtechAssignedIPAddress_Type())
qtechAssignedIPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechAssignedIPAddress.setStatus(_A)
class _QtechNeedConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_QtechNeedConfiguration_Type.__name__=_D
_QtechNeedConfiguration_Object=MibScalar
qtechNeedConfiguration=_QtechNeedConfiguration_Object((1,3,6,1,4,1,27514,1,1,10,2,87,1,7,2),_QtechNeedConfiguration_Type())
qtechNeedConfiguration.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechNeedConfiguration.setStatus(_A)
_QtechCapwapAppMIBConformance_ObjectIdentity=ObjectIdentity
qtechCapwapAppMIBConformance=_QtechCapwapAppMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,2))
_QtechCapwapAppMIBCompliances_ObjectIdentity=ObjectIdentity
qtechCapwapAppMIBCompliances=_QtechCapwapAppMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,2,1))
_QtechCapwapAppMIBGroups_ObjectIdentity=ObjectIdentity
qtechCapwapAppMIBGroups=_QtechCapwapAppMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,87,2,2))
qtechCapwapAppMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,87,2,2,1))
qtechCapwapAppMIBGroup.setObjects(*((_B,_b),(_B,_c),(_B,_N),(_B,_O),(_B,_K),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_P),(_B,_Q),(_B,_i),(_B,_j),(_B,_L),(_B,_M),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:qtechCapwapAppMIBGroup.setStatus(_A)
qtechAppHeartbeatTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,87,1,1,0,1))
qtechAppHeartbeatTrap.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:qtechAppHeartbeatTrap.setStatus(_A)
qtechAppAdminLoginTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,0,1))
qtechAppAdminLoginTrap.setObjects(*((_B,_I),(_B,_J),(_B,_q)))
if mibBuilder.loadTexts:qtechAppAdminLoginTrap.setStatus(_A)
qtechAppAdminModifyConfigTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,0,2))
qtechAppAdminModifyConfigTrap.setObjects(*((_B,_I),(_B,_J),(_B,_r)))
if mibBuilder.loadTexts:qtechAppAdminModifyConfigTrap.setStatus(_A)
qtechAppAdminLoginFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,0,3))
qtechAppAdminLoginFailTrap.setObjects(*((_B,_I),(_B,_J),(_B,_R),(_B,_s)))
if mibBuilder.loadTexts:qtechAppAdminLoginFailTrap.setStatus(_A)
qtechAppAdminEnableFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,87,1,2,0,4))
qtechAppAdminEnableFailTrap.setObjects(*((_B,_I),(_B,_J),(_B,_R),(_B,_t)))
if mibBuilder.loadTexts:qtechAppAdminEnableFailTrap.setStatus(_A)
qtechAppConfigModifyFileTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,87,1,4,0,1))
if mibBuilder.loadTexts:qtechAppConfigModifyFileTrap.setStatus(_A)
qtechAppConfigParseErrTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,87,1,4,0,2))
qtechAppConfigParseErrTrap.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:qtechAppConfigParseErrTrap.setStatus(_A)
qtechZCMNotifyTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,87,1,7,0,1))
qtechZCMNotifyTrap.setObjects(*((_V,_W),(_T,_U),(_B,_u),(_B,_v),(_X,_Y)))
if mibBuilder.loadTexts:qtechZCMNotifyTrap.setStatus(_A)
qtechCapwapAppMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,87,2,1,1))
qtechCapwapAppMIBCompliance.setObjects((_B,_w))
if mibBuilder.loadTexts:qtechCapwapAppMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechCapwapAppMIB':qtechCapwapAppMIB,'qtechCapwapAppMIBObjects':qtechCapwapAppMIBObjects,'qtechAppHeartbeatMIBObjects':qtechAppHeartbeatMIBObjects,'qtechAppHeartbeatMIBTraps':qtechAppHeartbeatMIBTraps,'qtechAppHeartbeatTrap':qtechAppHeartbeatTrap,_b:qtechAppHeartbeatOnOff,_c:qtechAppHeartbeatPeriod,_N:qtechAppHeartbeatIpAddr,_O:qtechAppHeartbeatTimeStamp,'qtechAppAdminInfoMIBObjects':qtechAppAdminInfoMIBObjects,'qtechAppAdminMIBTraps':qtechAppAdminMIBTraps,'qtechAppAdminLoginTrap':qtechAppAdminLoginTrap,'qtechAppAdminModifyConfigTrap':qtechAppAdminModifyConfigTrap,'qtechAppAdminLoginFailTrap':qtechAppAdminLoginFailTrap,'qtechAppAdminEnableFailTrap':qtechAppAdminEnableFailTrap,'qtechAppAdminInfoTable':qtechAppAdminInfoTable,'qtechAppAdminInfoEntry':qtechAppAdminInfoEntry,_K:qtechAppAdminName,_d:qtechAppAdminPwd,_e:qtechAppAdminPriLevel,_f:qtechAppAdminStatus,_I:qtechAppAdminInfoName,_J:qtechAppAdminInfoIpAddr,_r:qtechAppAdminInfoConfigContext,_q:qtechAppAdminInfoLoginType,_R:qtechAppAdminTerminalInfo,_s:qtechAppAdminLoginFailReason,_t:qtechAppAdminTargetLevel,'qtechAppPollTimeMIBObjects':qtechAppPollTimeMIBObjects,_g:qtechAppPollTimeOfLast,'qtechAppConfigMIBObjects':qtechAppConfigMIBObjects,'qtechAppConfigMIBTraps':qtechAppConfigMIBTraps,'qtechAppConfigModifyFileTrap':qtechAppConfigModifyFileTrap,'qtechAppConfigParseErrTrap':qtechAppConfigParseErrTrap,_h:qtechAppRcvToDefConfig,_P:qtechAppConfigFileName,_Q:qtechAppConfigParseErrReason,'qtechAppSyslogMIBObjects':qtechAppSyslogMIBObjects,_i:qtechAppSyslogSvcEnable,_j:qtechAppSyslogReportEventLevel,'qtechAppSyslogSvrCfgTable':qtechAppSyslogSvrCfgTable,'qtechAppSyslogSvrCfgEntry':qtechAppSyslogSvrCfgEntry,_L:qtechAppSyslogSvrNetType,_M:qtechAppSyslogSvrNetAddr,_k:qtechAppSyslogSvrNetPort,_l:qtechAppSyslogVrfName,_m:qtechAppSyslogStatus,'qtechSyslogServerAddrInfoTable':qtechSyslogServerAddrInfoTable,'qtechSyslogServerAddrInfoEntry':qtechSyslogServerAddrInfoEntry,_Z:qtechSyslogServerIndex,_n:qtechSyslogServerAddr,_o:qtechSyslogServerVrfName,_p:qtechSyslogServerStatus,'qtechAppTrapActionMIBObjects':qtechAppTrapActionMIBObjects,'qtechAppTrapActionEnable':qtechAppTrapActionEnable,'qtechAppTrapActionTable':qtechAppTrapActionTable,'qtechAppTrapActionEntry':qtechAppTrapActionEntry,_a:qtechAppTrapType,'qtechAppTrapAction':qtechAppTrapAction,'qtechAppTrapDescr':qtechAppTrapDescr,'qtechZCMMIBObjects':qtechZCMMIBObjects,'qtechZCMMIBTraps':qtechZCMMIBTraps,'qtechZCMNotifyTrap':qtechZCMNotifyTrap,_u:qtechAssignedIPAddress,_v:qtechNeedConfiguration,'qtechCapwapAppMIBConformance':qtechCapwapAppMIBConformance,'qtechCapwapAppMIBCompliances':qtechCapwapAppMIBCompliances,'qtechCapwapAppMIBCompliance':qtechCapwapAppMIBCompliance,'qtechCapwapAppMIBGroups':qtechCapwapAppMIBGroups,_w:qtechCapwapAppMIBGroup})