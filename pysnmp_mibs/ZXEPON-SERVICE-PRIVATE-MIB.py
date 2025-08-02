_f='zxEponQueueSlotNo'
_e='zxEponQueueShelfNo'
_d='zxEponQueueRackNo'
_c='profileIndex'
_b='zxEponRunIp'
_a='zxEponIpPoolName'
_Z='zxDbaPriority'
_Y='onuIndex'
_X='eponP2pGroupId'
_W='static'
_V='success'
_U='ZxAnIdList'
_T='TruthValue'
_S='OctetString'
_R='deny'
_Q='authenticating'
_P='disable'
_O='enable'
_N='read-create'
_M='disabled'
_L='enabled'
_K='not-accessible'
_J='ZXEPON-SERVICE-PRIVATE-MIB'
_I='false'
_H='true'
_G='DisplayString'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention',_T)
ZxAnIdList,=mibBuilder.importSymbols('ZTE-AN-TC-MIB',_U)
zxAnEponMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnEponMib')
_PrivateObjects_ObjectIdentity=ObjectIdentity
privateObjects=_PrivateObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,7))
_SysAttrObjectTable_Object=MibTable
sysAttrObjectTable=_SysAttrObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,1))
if mibBuilder.loadTexts:sysAttrObjectTable.setStatus(_A)
_SysAttrObjectEntry_Object=MibTableRow
sysAttrObjectEntry=_SysAttrObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,1,1))
sysAttrObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sysAttrObjectEntry.setStatus(_A)
class _SysOnuAdminAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('mac',1),('sn',2),('hybrid',3),('loid',4),('snPlusMac',5)))
_SysOnuAdminAuthMode_Type.__name__=_C
_SysOnuAdminAuthMode_Object=MibTableColumn
sysOnuAdminAuthMode=_SysOnuAdminAuthMode_Object((1,3,6,1,4,1,3902,1015,1010,1,7,1,1,1),_SysOnuAdminAuthMode_Type())
sysOnuAdminAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sysOnuAdminAuthMode.setStatus(_A)
class _SysAttrAutoAuthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SysAttrAutoAuthEnable_Type.__name__=_C
_SysAttrAutoAuthEnable_Object=MibTableColumn
sysAttrAutoAuthEnable=_SysAttrAutoAuthEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,1,1,2),_SysAttrAutoAuthEnable_Type())
sysAttrAutoAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sysAttrAutoAuthEnable.setStatus(_A)
class _MacHwAuthOnuState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_MacHwAuthOnuState_Type.__name__=_C
_MacHwAuthOnuState_Object=MibTableColumn
macHwAuthOnuState=_MacHwAuthOnuState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,1,1,3),_MacHwAuthOnuState_Type())
macHwAuthOnuState.setMaxAccess(_B)
if mibBuilder.loadTexts:macHwAuthOnuState.setStatus(_A)
class _ZxAnEponOnuSilenceEnable_Type(TruthValue):defaultValue=1
_ZxAnEponOnuSilenceEnable_Type.__name__=_T
_ZxAnEponOnuSilenceEnable_Object=MibTableColumn
zxAnEponOnuSilenceEnable=_ZxAnEponOnuSilenceEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,1,1,4),_ZxAnEponOnuSilenceEnable_Type())
zxAnEponOnuSilenceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuSilenceEnable.setStatus(_A)
_OltLinkAdminTestObjectTable_Object=MibTable
oltLinkAdminTestObjectTable=_OltLinkAdminTestObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,2))
if mibBuilder.loadTexts:oltLinkAdminTestObjectTable.setStatus(_A)
_OltLinkAdminTestObjectEntry_Object=MibTableRow
oltLinkAdminTestObjectEntry=_OltLinkAdminTestObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,2,1))
oltLinkAdminTestObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oltLinkAdminTestObjectEntry.setStatus(_A)
class _TestControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_TestControlMode_Type.__name__=_C
_TestControlMode_Object=MibTableColumn
testControlMode=_TestControlMode_Object((1,3,6,1,4,1,3902,1015,1010,1,7,2,1,1),_TestControlMode_Type())
testControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:testControlMode.setStatus(_A)
class _TestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),('fail',2)))
_TestResult_Type.__name__=_C
_TestResult_Object=MibTableColumn
testResult=_TestResult_Object((1,3,6,1,4,1,3902,1015,1010,1,7,2,1,2),_TestResult_Type())
testResult.setMaxAccess(_D)
if mibBuilder.loadTexts:testResult.setStatus(_A)
_OltLoopbackObjectTable_Object=MibTable
oltLoopbackObjectTable=_OltLoopbackObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,3))
if mibBuilder.loadTexts:oltLoopbackObjectTable.setStatus(_A)
_OltLoopbackObjectEntry_Object=MibTableRow
oltLoopbackObjectEntry=_OltLoopbackObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,3,1))
oltLoopbackObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oltLoopbackObjectEntry.setStatus(_A)
class _LoopbackStation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pon',1),('nni',2)))
_LoopbackStation_Type.__name__=_C
_LoopbackStation_Object=MibTableColumn
loopbackStation=_LoopbackStation_Object((1,3,6,1,4,1,3902,1015,1010,1,7,3,1,1),_LoopbackStation_Type())
loopbackStation.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackStation.setStatus(_A)
class _LoopbackDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('line',1),('system',2)))
_LoopbackDirection_Type.__name__=_C
_LoopbackDirection_Object=MibTableColumn
loopbackDirection=_LoopbackDirection_Object((1,3,6,1,4,1,3902,1015,1010,1,7,3,1,2),_LoopbackDirection_Type())
loopbackDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackDirection.setStatus(_A)
class _LoopbackAdministration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mac',1),('phy',2)))
_LoopbackAdministration_Type.__name__=_C
_LoopbackAdministration_Object=MibTableColumn
loopbackAdministration=_LoopbackAdministration_Object((1,3,6,1,4,1,3902,1015,1010,1,7,3,1,3),_LoopbackAdministration_Type())
loopbackAdministration.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackAdministration.setStatus(_A)
class _LoopbackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noloopback',1),('loopback',2)))
_LoopbackState_Type.__name__=_C
_LoopbackState_Object=MibTableColumn
loopbackState=_LoopbackState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,3,1,4),_LoopbackState_Type())
loopbackState.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackState.setStatus(_A)
_OnuAdminObjectTable_Object=MibTable
onuAdminObjectTable=_OnuAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4))
if mibBuilder.loadTexts:onuAdminObjectTable.setStatus(_A)
_OnuAdminObjectEntry_Object=MibTableRow
onuAdminObjectEntry=_OnuAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1))
onuAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:onuAdminObjectEntry.setStatus(_A)
_OnuDescript_Type=DisplayString
_OnuDescript_Object=MibTableColumn
onuDescript=_OnuDescript_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,1),_OnuDescript_Type())
onuDescript.setMaxAccess(_B)
if mibBuilder.loadTexts:onuDescript.setStatus(_A)
_OnuSplitterSn_Type=Integer32
_OnuSplitterSn_Object=MibTableColumn
onuSplitterSn=_OnuSplitterSn_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,2),_OnuSplitterSn_Type())
onuSplitterSn.setMaxAccess(_B)
if mibBuilder.loadTexts:onuSplitterSn.setStatus(_A)
_OnuOpticalLineSn_Type=Integer32
_OnuOpticalLineSn_Object=MibTableColumn
onuOpticalLineSn=_OnuOpticalLineSn_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,3),_OnuOpticalLineSn_Type())
onuOpticalLineSn.setMaxAccess(_B)
if mibBuilder.loadTexts:onuOpticalLineSn.setStatus(_A)
_OnuUserInfo_Type=DisplayString
_OnuUserInfo_Object=MibTableColumn
onuUserInfo=_OnuUserInfo_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,4),_OnuUserInfo_Type())
onuUserInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUserInfo.setStatus(_A)
_OnuType_Type=DisplayString
_OnuType_Object=MibTableColumn
onuType=_OnuType_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,5),_OnuType_Type())
onuType.setMaxAccess(_B)
if mibBuilder.loadTexts:onuType.setStatus(_A)
class _OnuAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_OnuAdminState_Type.__name__=_C
_OnuAdminState_Object=MibTableColumn
onuAdminState=_OnuAdminState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,6),_OnuAdminState_Type())
onuAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:onuAdminState.setStatus(_A)
_OnuAuthMACAddress_Type=MacAddress
_OnuAuthMACAddress_Object=MibTableColumn
onuAuthMACAddress=_OnuAuthMACAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,7),_OnuAuthMACAddress_Type())
onuAuthMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:onuAuthMACAddress.setStatus(_A)
_OnuRegisterMACAddress_Type=MacAddress
_OnuRegisterMACAddress_Object=MibTableColumn
onuRegisterMACAddress=_OnuRegisterMACAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,8),_OnuRegisterMACAddress_Type())
onuRegisterMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:onuRegisterMACAddress.setStatus(_A)
_OnuAuthMACSn_Type=OctetString
_OnuAuthMACSn_Object=MibTableColumn
onuAuthMACSn=_OnuAuthMACSn_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,9),_OnuAuthMACSn_Type())
onuAuthMACSn.setMaxAccess(_B)
if mibBuilder.loadTexts:onuAuthMACSn.setStatus(_A)
_OnuRegisterSn_Type=OctetString
_OnuRegisterSn_Object=MibTableColumn
onuRegisterSn=_OnuRegisterSn_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,10),_OnuRegisterSn_Type())
onuRegisterSn.setMaxAccess(_D)
if mibBuilder.loadTexts:onuRegisterSn.setStatus(_A)
class _OnuCurrentRegState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unregister',1),('registering',2),('registered',3)))
_OnuCurrentRegState_Type.__name__=_C
_OnuCurrentRegState_Object=MibTableColumn
onuCurrentRegState=_OnuCurrentRegState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,11),_OnuCurrentRegState_Type())
onuCurrentRegState.setMaxAccess(_D)
if mibBuilder.loadTexts:onuCurrentRegState.setStatus(_A)
_OnuRegisterTime_Type=DisplayString
_OnuRegisterTime_Object=MibTableColumn
onuRegisterTime=_OnuRegisterTime_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,12),_OnuRegisterTime_Type())
onuRegisterTime.setMaxAccess(_D)
if mibBuilder.loadTexts:onuRegisterTime.setStatus(_A)
class _OnuCurrAdminAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),(_Q,2),('pass',3),(_R,4)))
_OnuCurrAdminAuthState_Type.__name__=_C
_OnuCurrAdminAuthState_Object=MibTableColumn
onuCurrAdminAuthState=_OnuCurrAdminAuthState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,13),_OnuCurrAdminAuthState_Type())
onuCurrAdminAuthState.setMaxAccess(_D)
if mibBuilder.loadTexts:onuCurrAdminAuthState.setStatus(_A)
_OnuLatelyPassAdminAuthTime_Type=DisplayString
_OnuLatelyPassAdminAuthTime_Object=MibTableColumn
onuLatelyPassAdminAuthTime=_OnuLatelyPassAdminAuthTime_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,14),_OnuLatelyPassAdminAuthTime_Type())
onuLatelyPassAdminAuthTime.setMaxAccess(_D)
if mibBuilder.loadTexts:onuLatelyPassAdminAuthTime.setStatus(_A)
_OnuCurrDot1xAuthState_Type=Integer32
_OnuCurrDot1xAuthState_Object=MibTableColumn
onuCurrDot1xAuthState=_OnuCurrDot1xAuthState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,15),_OnuCurrDot1xAuthState_Type())
onuCurrDot1xAuthState.setMaxAccess(_D)
if mibBuilder.loadTexts:onuCurrDot1xAuthState.setStatus(_A)
_OnuLatelyPassDot1xAuthTime_Type=DisplayString
_OnuLatelyPassDot1xAuthTime_Object=MibTableColumn
onuLatelyPassDot1xAuthTime=_OnuLatelyPassDot1xAuthTime_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,16),_OnuLatelyPassDot1xAuthTime_Type())
onuLatelyPassDot1xAuthTime.setMaxAccess(_D)
if mibBuilder.loadTexts:onuLatelyPassDot1xAuthTime.setStatus(_A)
class _OnuMgmtOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('poweroff',1),('offline',2),('online',3)))
_OnuMgmtOnlineStatus_Type.__name__=_C
_OnuMgmtOnlineStatus_Object=MibTableColumn
onuMgmtOnlineStatus=_OnuMgmtOnlineStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,17),_OnuMgmtOnlineStatus_Type())
onuMgmtOnlineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:onuMgmtOnlineStatus.setStatus(_A)
class _OnuActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_OnuActiveStatus_Type.__name__=_C
_OnuActiveStatus_Object=MibTableColumn
onuActiveStatus=_OnuActiveStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,18),_OnuActiveStatus_Type())
onuActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:onuActiveStatus.setStatus(_A)
_OnuMgmtEntryStatus_Type=RowStatus
_OnuMgmtEntryStatus_Object=MibTableColumn
onuMgmtEntryStatus=_OnuMgmtEntryStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,19),_OnuMgmtEntryStatus_Type())
onuMgmtEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:onuMgmtEntryStatus.setStatus(_A)
class _OnuMgmtIpCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),('dynatmic',2)))
_OnuMgmtIpCfgMode_Type.__name__=_C
_OnuMgmtIpCfgMode_Object=MibTableColumn
onuMgmtIpCfgMode=_OnuMgmtIpCfgMode_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,20),_OnuMgmtIpCfgMode_Type())
onuMgmtIpCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:onuMgmtIpCfgMode.setStatus(_A)
class _OnuAuthLoid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_OnuAuthLoid_Type.__name__=_G
_OnuAuthLoid_Object=MibTableColumn
onuAuthLoid=_OnuAuthLoid_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,21),_OnuAuthLoid_Type())
onuAuthLoid.setMaxAccess(_B)
if mibBuilder.loadTexts:onuAuthLoid.setStatus(_A)
class _OnuAuthPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_OnuAuthPassword_Type.__name__=_G
_OnuAuthPassword_Object=MibTableColumn
onuAuthPassword=_OnuAuthPassword_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,22),_OnuAuthPassword_Type())
onuAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:onuAuthPassword.setStatus(_A)
class _OnuRegisterLoid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_OnuRegisterLoid_Type.__name__=_G
_OnuRegisterLoid_Object=MibTableColumn
onuRegisterLoid=_OnuRegisterLoid_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,23),_OnuRegisterLoid_Type())
onuRegisterLoid.setMaxAccess(_D)
if mibBuilder.loadTexts:onuRegisterLoid.setStatus(_A)
class _OnuRegisterPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_OnuRegisterPassword_Type.__name__=_G
_OnuRegisterPassword_Object=MibTableColumn
onuRegisterPassword=_OnuRegisterPassword_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,24),_OnuRegisterPassword_Type())
onuRegisterPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:onuRegisterPassword.setStatus(_A)
class _ZxAnEponOnuCreateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_ZxAnEponOnuCreateTime_Type.__name__=_G
_ZxAnEponOnuCreateTime_Object=MibTableColumn
zxAnEponOnuCreateTime=_ZxAnEponOnuCreateTime_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,25),_ZxAnEponOnuCreateTime_Type())
zxAnEponOnuCreateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuCreateTime.setStatus(_A)
class _ZxAnEponOnuLastOfflineTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_ZxAnEponOnuLastOfflineTime_Type.__name__=_G
_ZxAnEponOnuLastOfflineTime_Object=MibTableColumn
zxAnEponOnuLastOfflineTime=_ZxAnEponOnuLastOfflineTime_Object((1,3,6,1,4,1,3902,1015,1010,1,7,4,1,26),_ZxAnEponOnuLastOfflineTime_Type())
zxAnEponOnuLastOfflineTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuLastOfflineTime.setStatus(_A)
_OltEncryAdminObjectTable_Object=MibTable
oltEncryAdminObjectTable=_OltEncryAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,5))
if mibBuilder.loadTexts:oltEncryAdminObjectTable.setStatus(_A)
_OltEncryAdminObjectEntry_Object=MibTableRow
oltEncryAdminObjectEntry=_OltEncryAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,5,1))
oltEncryAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oltEncryAdminObjectEntry.setStatus(_A)
class _EncryptArithmetic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aes128',1),('triplechurning',2)))
_EncryptArithmetic_Type.__name__=_C
_EncryptArithmetic_Object=MibTableColumn
encryptArithmetic=_EncryptArithmetic_Object((1,3,6,1,4,1,3902,1015,1010,1,7,5,1,1),_EncryptArithmetic_Type())
encryptArithmetic.setMaxAccess(_B)
if mibBuilder.loadTexts:encryptArithmetic.setStatus(_A)
_KeyUpdateTime_Type=Integer32
_KeyUpdateTime_Object=MibTableColumn
keyUpdateTime=_KeyUpdateTime_Object((1,3,6,1,4,1,3902,1015,1010,1,7,5,1,2),_KeyUpdateTime_Type())
keyUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:keyUpdateTime.setStatus(_A)
_KeyUpdateTimeout_Type=Integer32
_KeyUpdateTimeout_Object=MibTableColumn
keyUpdateTimeout=_KeyUpdateTimeout_Object((1,3,6,1,4,1,3902,1015,1010,1,7,5,1,3),_KeyUpdateTimeout_Type())
keyUpdateTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:keyUpdateTimeout.setStatus(_A)
_StartEncryptThreshold_Type=Integer32
_StartEncryptThreshold_Object=MibTableColumn
startEncryptThreshold=_StartEncryptThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,7,5,1,4),_StartEncryptThreshold_Type())
startEncryptThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:startEncryptThreshold.setStatus(_A)
_LineEncryAdminObjectTable_Object=MibTable
lineEncryAdminObjectTable=_LineEncryAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,6))
if mibBuilder.loadTexts:lineEncryAdminObjectTable.setStatus(_A)
_LineEncryAdminObjectEntry_Object=MibTableRow
lineEncryAdminObjectEntry=_LineEncryAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,6,1))
lineEncryAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:lineEncryAdminObjectEntry.setStatus(_A)
class _EncryptMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('downlink',1),('both',2)))
_EncryptMode_Type.__name__=_C
_EncryptMode_Object=MibTableColumn
encryptMode=_EncryptMode_Object((1,3,6,1,4,1,3902,1015,1010,1,7,6,1,1),_EncryptMode_Type())
encryptMode.setMaxAccess(_B)
if mibBuilder.loadTexts:encryptMode.setStatus(_A)
_EncrypeState_Type=TruthValue
_EncrypeState_Object=MibTableColumn
encrypeState=_EncrypeState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,6,1,2),_EncrypeState_Type())
encrypeState.setMaxAccess(_B)
if mibBuilder.loadTexts:encrypeState.setStatus(_A)
_SlaUpAdminObjectTable_Object=MibTable
slaUpAdminObjectTable=_SlaUpAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7))
if mibBuilder.loadTexts:slaUpAdminObjectTable.setStatus(_A)
_SlaUpAdminObjectEntry_Object=MibTableRow
slaUpAdminObjectEntry=_SlaUpAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1))
slaUpAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:slaUpAdminObjectEntry.setStatus(_A)
_UpFixedBw_Type=Integer32
_UpFixedBw_Object=MibTableColumn
upFixedBw=_UpFixedBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1,1),_UpFixedBw_Type())
upFixedBw.setMaxAccess(_B)
if mibBuilder.loadTexts:upFixedBw.setStatus(_A)
_UpAssuredBw_Type=Integer32
_UpAssuredBw_Object=MibTableColumn
upAssuredBw=_UpAssuredBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1,2),_UpAssuredBw_Type())
upAssuredBw.setMaxAccess(_B)
if mibBuilder.loadTexts:upAssuredBw.setStatus(_A)
_UpMaximumBw_Type=Integer32
_UpMaximumBw_Object=MibTableColumn
upMaximumBw=_UpMaximumBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1,3),_UpMaximumBw_Type())
upMaximumBw.setMaxAccess(_B)
if mibBuilder.loadTexts:upMaximumBw.setStatus(_A)
_UpMaxBurstSize_Type=Integer32
_UpMaxBurstSize_Object=MibTableColumn
upMaxBurstSize=_UpMaxBurstSize_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1,4),_UpMaxBurstSize_Type())
upMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:upMaxBurstSize.setStatus(_A)
class _UpPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_UpPri_Type.__name__=_C
_UpPri_Object=MibTableColumn
upPri=_UpPri_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1,5),_UpPri_Type())
upPri.setMaxAccess(_B)
if mibBuilder.loadTexts:upPri.setStatus(_A)
_UpMaxTimeDelay_Type=Integer32
_UpMaxTimeDelay_Object=MibTableColumn
upMaxTimeDelay=_UpMaxTimeDelay_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1,6),_UpMaxTimeDelay_Type())
upMaxTimeDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:upMaxTimeDelay.setStatus(_A)
_UpMaxDrift_Type=Integer32
_UpMaxDrift_Object=MibTableColumn
upMaxDrift=_UpMaxDrift_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1,7),_UpMaxDrift_Type())
upMaxDrift.setMaxAccess(_B)
if mibBuilder.loadTexts:upMaxDrift.setStatus(_A)
_UpFixedPacketSize_Type=Integer32
_UpFixedPacketSize_Object=MibTableColumn
upFixedPacketSize=_UpFixedPacketSize_Object((1,3,6,1,4,1,3902,1015,1010,1,7,7,1,8),_UpFixedPacketSize_Type())
upFixedPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:upFixedPacketSize.setStatus(_A)
_SlaDownAdminObjectTable_Object=MibTable
slaDownAdminObjectTable=_SlaDownAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,8))
if mibBuilder.loadTexts:slaDownAdminObjectTable.setStatus(_A)
_SlaDownAdminObjectEntry_Object=MibTableRow
slaDownAdminObjectEntry=_SlaDownAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,8,1))
slaDownAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:slaDownAdminObjectEntry.setStatus(_A)
_DownAssuredBw_Type=Integer32
_DownAssuredBw_Object=MibTableColumn
downAssuredBw=_DownAssuredBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,8,1,1),_DownAssuredBw_Type())
downAssuredBw.setMaxAccess(_B)
if mibBuilder.loadTexts:downAssuredBw.setStatus(_A)
_DownMaximumBw_Type=Integer32
_DownMaximumBw_Object=MibTableColumn
downMaximumBw=_DownMaximumBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,8,1,2),_DownMaximumBw_Type())
downMaximumBw.setMaxAccess(_B)
if mibBuilder.loadTexts:downMaximumBw.setStatus(_A)
_DownMaxBurstSize_Type=Integer32
_DownMaxBurstSize_Object=MibTableColumn
downMaxBurstSize=_DownMaxBurstSize_Object((1,3,6,1,4,1,3902,1015,1010,1,7,8,1,3),_DownMaxBurstSize_Type())
downMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:downMaxBurstSize.setStatus(_A)
class _DownPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DownPri_Type.__name__=_C
_DownPri_Object=MibTableColumn
downPri=_DownPri_Object((1,3,6,1,4,1,3902,1015,1010,1,7,8,1,4),_DownPri_Type())
downPri.setMaxAccess(_B)
if mibBuilder.loadTexts:downPri.setStatus(_A)
_DownMaxTimeDelay_Type=Integer32
_DownMaxTimeDelay_Object=MibTableColumn
downMaxTimeDelay=_DownMaxTimeDelay_Object((1,3,6,1,4,1,3902,1015,1010,1,7,8,1,5),_DownMaxTimeDelay_Type())
downMaxTimeDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:downMaxTimeDelay.setStatus(_A)
_DownMaxDrift_Type=Integer32
_DownMaxDrift_Object=MibTableColumn
downMaxDrift=_DownMaxDrift_Object((1,3,6,1,4,1,3902,1015,1010,1,7,8,1,6),_DownMaxDrift_Type())
downMaxDrift.setMaxAccess(_B)
if mibBuilder.loadTexts:downMaxDrift.setStatus(_A)
_SlaP2pAdminObjectTable_Object=MibTable
slaP2pAdminObjectTable=_SlaP2pAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,9))
if mibBuilder.loadTexts:slaP2pAdminObjectTable.setStatus(_A)
_SlaP2pAdminObjectEntry_Object=MibTableRow
slaP2pAdminObjectEntry=_SlaP2pAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,9,1))
slaP2pAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:slaP2pAdminObjectEntry.setStatus(_A)
_P2pAssuredBw_Type=Integer32
_P2pAssuredBw_Object=MibTableColumn
p2pAssuredBw=_P2pAssuredBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,9,1,1),_P2pAssuredBw_Type())
p2pAssuredBw.setMaxAccess(_B)
if mibBuilder.loadTexts:p2pAssuredBw.setStatus(_A)
_P2pMaximumBw_Type=Integer32
_P2pMaximumBw_Object=MibTableColumn
p2pMaximumBw=_P2pMaximumBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,9,1,2),_P2pMaximumBw_Type())
p2pMaximumBw.setMaxAccess(_B)
if mibBuilder.loadTexts:p2pMaximumBw.setStatus(_A)
_P2pMaxBurstSize_Type=Integer32
_P2pMaxBurstSize_Object=MibTableColumn
p2pMaxBurstSize=_P2pMaxBurstSize_Object((1,3,6,1,4,1,3902,1015,1010,1,7,9,1,3),_P2pMaxBurstSize_Type())
p2pMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:p2pMaxBurstSize.setStatus(_A)
class _P2pPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_P2pPri_Type.__name__=_C
_P2pPri_Object=MibTableColumn
p2pPri=_P2pPri_Object((1,3,6,1,4,1,3902,1015,1010,1,7,9,1,4),_P2pPri_Type())
p2pPri.setMaxAccess(_B)
if mibBuilder.loadTexts:p2pPri.setStatus(_A)
_P2pMaxTimeDelay_Type=Integer32
_P2pMaxTimeDelay_Object=MibTableColumn
p2pMaxTimeDelay=_P2pMaxTimeDelay_Object((1,3,6,1,4,1,3902,1015,1010,1,7,9,1,5),_P2pMaxTimeDelay_Type())
p2pMaxTimeDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:p2pMaxTimeDelay.setStatus(_A)
_P2pMaxDrift_Type=Integer32
_P2pMaxDrift_Object=MibTableColumn
p2pMaxDrift=_P2pMaxDrift_Object((1,3,6,1,4,1,3902,1015,1010,1,7,9,1,6),_P2pMaxDrift_Type())
p2pMaxDrift.setMaxAccess(_B)
if mibBuilder.loadTexts:p2pMaxDrift.setStatus(_A)
_P2pModeAdminObjectTable_Object=MibTable
p2pModeAdminObjectTable=_P2pModeAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,10))
if mibBuilder.loadTexts:p2pModeAdminObjectTable.setStatus(_A)
_P2pModeAdminObjectEntry_Object=MibTableRow
p2pModeAdminObjectEntry=_P2pModeAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,10,1))
p2pModeAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:p2pModeAdminObjectEntry.setStatus(_A)
class _EponP2pMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('group',2)))
_EponP2pMode_Type.__name__=_C
_EponP2pMode_Object=MibTableColumn
eponP2pMode=_EponP2pMode_Object((1,3,6,1,4,1,3902,1015,1010,1,7,10,1,1),_EponP2pMode_Type())
eponP2pMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eponP2pMode.setStatus(_A)
_P2pGroupAdminObjectTable_Object=MibTable
p2pGroupAdminObjectTable=_P2pGroupAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,12))
if mibBuilder.loadTexts:p2pGroupAdminObjectTable.setStatus(_A)
_P2pGroupAdminObjectEntry_Object=MibTableRow
p2pGroupAdminObjectEntry=_P2pGroupAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,12,1))
p2pGroupAdminObjectEntry.setIndexNames((0,_E,_F),(0,_J,_X))
if mibBuilder.loadTexts:p2pGroupAdminObjectEntry.setStatus(_A)
class _EponP2pGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2016))
_EponP2pGroupId_Type.__name__=_C
_EponP2pGroupId_Object=MibTableColumn
eponP2pGroupId=_EponP2pGroupId_Object((1,3,6,1,4,1,3902,1015,1010,1,7,12,1,1),_EponP2pGroupId_Type())
eponP2pGroupId.setMaxAccess(_K)
if mibBuilder.loadTexts:eponP2pGroupId.setStatus(_A)
class _EponP2pGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_EponP2pGroupName_Type.__name__=_G
_EponP2pGroupName_Object=MibTableColumn
eponP2pGroupName=_EponP2pGroupName_Object((1,3,6,1,4,1,3902,1015,1010,1,7,12,1,2),_EponP2pGroupName_Type())
eponP2pGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:eponP2pGroupName.setStatus(_A)
class _EponP2pGroupOnus_Type(ZxAnIdList):subtypeSpec=ZxAnIdList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EponP2pGroupOnus_Type.__name__=_U
_EponP2pGroupOnus_Object=MibTableColumn
eponP2pGroupOnus=_EponP2pGroupOnus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,12,1,3),_EponP2pGroupOnus_Type())
eponP2pGroupOnus.setMaxAccess(_B)
if mibBuilder.loadTexts:eponP2pGroupOnus.setStatus(_A)
class _EponP2pGroupAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_EponP2pGroupAdminStatus_Type.__name__=_C
_EponP2pGroupAdminStatus_Object=MibTableColumn
eponP2pGroupAdminStatus=_EponP2pGroupAdminStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,12,1,4),_EponP2pGroupAdminStatus_Type())
eponP2pGroupAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eponP2pGroupAdminStatus.setStatus(_A)
class _EponP2pGroupOpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_EponP2pGroupOpStatus_Type.__name__=_C
_EponP2pGroupOpStatus_Object=MibTableColumn
eponP2pGroupOpStatus=_EponP2pGroupOpStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,12,1,5),_EponP2pGroupOpStatus_Type())
eponP2pGroupOpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eponP2pGroupOpStatus.setStatus(_A)
_EponP2pGroupRowStatus_Type=RowStatus
_EponP2pGroupRowStatus_Object=MibTableColumn
eponP2pGroupRowStatus=_EponP2pGroupRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,12,1,6),_EponP2pGroupRowStatus_Type())
eponP2pGroupRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:eponP2pGroupRowStatus.setStatus(_A)
_P2pTransmitAdminObjectTable_Object=MibTable
p2pTransmitAdminObjectTable=_P2pTransmitAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,13))
if mibBuilder.loadTexts:p2pTransmitAdminObjectTable.setStatus(_A)
_P2pTransmitAdminObjectEntry_Object=MibTableRow
p2pTransmitAdminObjectEntry=_P2pTransmitAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,13,1))
p2pTransmitAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:p2pTransmitAdminObjectEntry.setStatus(_A)
_EponP2pCfgAddressNotFoundEnableFlood_Type=TruthValue
_EponP2pCfgAddressNotFoundEnableFlood_Object=MibTableColumn
eponP2pCfgAddressNotFoundEnableFlood=_EponP2pCfgAddressNotFoundEnableFlood_Object((1,3,6,1,4,1,3902,1015,1010,1,7,13,1,1),_EponP2pCfgAddressNotFoundEnableFlood_Type())
eponP2pCfgAddressNotFoundEnableFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:eponP2pCfgAddressNotFoundEnableFlood.setStatus(_A)
_EponP2pCfgBroadcastEnableFlood_Type=TruthValue
_EponP2pCfgBroadcastEnableFlood_Object=MibTableColumn
eponP2pCfgBroadcastEnableFlood=_EponP2pCfgBroadcastEnableFlood_Object((1,3,6,1,4,1,3902,1015,1010,1,7,13,1,2),_EponP2pCfgBroadcastEnableFlood_Type())
eponP2pCfgBroadcastEnableFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:eponP2pCfgBroadcastEnableFlood.setStatus(_A)
_OnuUnPassedAdminAuthInfoTable_Object=MibTable
onuUnPassedAdminAuthInfoTable=_OnuUnPassedAdminAuthInfoTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14))
if mibBuilder.loadTexts:onuUnPassedAdminAuthInfoTable.setStatus(_A)
_OnuUnPassedAdminAuthInfoEntry_Object=MibTableRow
onuUnPassedAdminAuthInfoEntry=_OnuUnPassedAdminAuthInfoEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1))
onuUnPassedAdminAuthInfoEntry.setIndexNames((0,_E,_F),(0,_J,_Y))
if mibBuilder.loadTexts:onuUnPassedAdminAuthInfoEntry.setStatus(_A)
_OnuIndex_Type=Integer32
_OnuIndex_Object=MibTableColumn
onuIndex=_OnuIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,1),_OnuIndex_Type())
onuIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:onuIndex.setStatus(_A)
_OnuRegisterMacAddress_Type=MacAddress
_OnuRegisterMacAddress_Object=MibTableColumn
onuRegisterMacAddress=_OnuRegisterMacAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,2),_OnuRegisterMacAddress_Type())
onuRegisterMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:onuRegisterMacAddress.setStatus(_A)
_OnuReportSn_Type=OctetString
_OnuReportSn_Object=MibTableColumn
onuReportSn=_OnuReportSn_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,3),_OnuReportSn_Type())
onuReportSn.setMaxAccess(_D)
if mibBuilder.loadTexts:onuReportSn.setStatus(_A)
class _OnuAdminAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_OnuAdminAuthState_Type.__name__=_C
_OnuAdminAuthState_Object=MibTableColumn
onuAdminAuthState=_OnuAdminAuthState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,4),_OnuAdminAuthState_Type())
onuAdminAuthState.setMaxAccess(_D)
if mibBuilder.loadTexts:onuAdminAuthState.setStatus(_A)
class _OnuDot1xAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_OnuDot1xAuthState_Type.__name__=_C
_OnuDot1xAuthState_Object=MibTableColumn
onuDot1xAuthState=_OnuDot1xAuthState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,5),_OnuDot1xAuthState_Type())
onuDot1xAuthState.setMaxAccess(_D)
if mibBuilder.loadTexts:onuDot1xAuthState.setStatus(_A)
_OnuUplineTime_Type=OctetString
_OnuUplineTime_Object=MibTableColumn
onuUplineTime=_OnuUplineTime_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,6),_OnuUplineTime_Type())
onuUplineTime.setMaxAccess(_D)
if mibBuilder.loadTexts:onuUplineTime.setStatus(_A)
_OnuReportLoid_Type=DisplayString
_OnuReportLoid_Object=MibTableColumn
onuReportLoid=_OnuReportLoid_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,7),_OnuReportLoid_Type())
onuReportLoid.setMaxAccess(_D)
if mibBuilder.loadTexts:onuReportLoid.setStatus(_A)
_OnuReportPassword_Type=DisplayString
_OnuReportPassword_Object=MibTableColumn
onuReportPassword=_OnuReportPassword_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,8),_OnuReportPassword_Type())
onuReportPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:onuReportPassword.setStatus(_A)
_OnuReportType_Type=DisplayString
_OnuReportType_Object=MibTableColumn
onuReportType=_OnuReportType_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,9),_OnuReportType_Type())
onuReportType.setMaxAccess(_D)
if mibBuilder.loadTexts:onuReportType.setStatus(_A)
_ZxAnEponOnuSwVersion_Type=DisplayString
_ZxAnEponOnuSwVersion_Object=MibTableColumn
zxAnEponOnuSwVersion=_ZxAnEponOnuSwVersion_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,10),_ZxAnEponOnuSwVersion_Type())
zxAnEponOnuSwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuSwVersion.setStatus(_A)
_ZxAnEponOnuHwVersion_Type=DisplayString
_ZxAnEponOnuHwVersion_Object=MibTableColumn
zxAnEponOnuHwVersion=_ZxAnEponOnuHwVersion_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,11),_ZxAnEponOnuHwVersion_Type())
zxAnEponOnuHwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuHwVersion.setStatus(_A)
class _ZxAnEponOnuOamBuildStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('failed',1),('inProgress',2),('notSupport',3),(_V,4)))
_ZxAnEponOnuOamBuildStatus_Type.__name__=_C
_ZxAnEponOnuOamBuildStatus_Object=MibTableColumn
zxAnEponOnuOamBuildStatus=_ZxAnEponOnuOamBuildStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,14,1,12),_ZxAnEponOnuOamBuildStatus_Type())
zxAnEponOnuOamBuildStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuOamBuildStatus.setStatus(_A)
_OnuConfigAdminObjectTable_Object=MibTable
onuConfigAdminObjectTable=_OnuConfigAdminObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,15))
if mibBuilder.loadTexts:onuConfigAdminObjectTable.setStatus(_A)
_OnuConfigAdminObjectEntry_Object=MibTableRow
onuConfigAdminObjectEntry=_OnuConfigAdminObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,15,1))
onuConfigAdminObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:onuConfigAdminObjectEntry.setStatus(_A)
class _OnuConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notconfigure',1),('configuring',2),('configurationsucceeded',3),('configurationfailed',4)))
_OnuConfigState_Type.__name__=_C
_OnuConfigState_Object=MibTableColumn
onuConfigState=_OnuConfigState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,15,1,1),_OnuConfigState_Type())
onuConfigState.setMaxAccess(_D)
if mibBuilder.loadTexts:onuConfigState.setStatus(_A)
_OnuCfgErrObjTables_Type=Integer32
_OnuCfgErrObjTables_Object=MibTableColumn
onuCfgErrObjTables=_OnuCfgErrObjTables_Object((1,3,6,1,4,1,3902,1015,1010,1,7,15,1,2),_OnuCfgErrObjTables_Type())
onuCfgErrObjTables.setMaxAccess(_D)
if mibBuilder.loadTexts:onuCfgErrObjTables.setStatus(_A)
_OltPonAttrObjectTable_Object=MibTable
oltPonAttrObjectTable=_OltPonAttrObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16))
if mibBuilder.loadTexts:oltPonAttrObjectTable.setStatus(_A)
_OltPonAttrObjectEntry_Object=MibTableRow
oltPonAttrObjectEntry=_OltPonAttrObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1))
oltPonAttrObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oltPonAttrObjectEntry.setStatus(_A)
_OltPonAttrName_Type=DisplayString
_OltPonAttrName_Object=MibTableColumn
oltPonAttrName=_OltPonAttrName_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,1),_OltPonAttrName_Type())
oltPonAttrName.setMaxAccess(_B)
if mibBuilder.loadTexts:oltPonAttrName.setStatus(_A)
_OltPonPonAttrDesc_Type=DisplayString
_OltPonPonAttrDesc_Object=MibTableColumn
oltPonPonAttrDesc=_OltPonPonAttrDesc_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,2),_OltPonPonAttrDesc_Type())
oltPonPonAttrDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:oltPonPonAttrDesc.setStatus(_A)
class _OltPonAttrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('reset',2)))
_OltPonAttrReset_Type.__name__=_C
_OltPonAttrReset_Object=MibTableColumn
oltPonAttrReset=_OltPonAttrReset_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,3),_OltPonAttrReset_Type())
oltPonAttrReset.setMaxAccess(_B)
if mibBuilder.loadTexts:oltPonAttrReset.setStatus(_A)
class _OltPonAttrResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_OltPonAttrResetCounters_Type.__name__=_C
_OltPonAttrResetCounters_Object=MibTableColumn
oltPonAttrResetCounters=_OltPonAttrResetCounters_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,4),_OltPonAttrResetCounters_Type())
oltPonAttrResetCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:oltPonAttrResetCounters.setStatus(_A)
class _OltPonAttrMultiLlidState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_OltPonAttrMultiLlidState_Type.__name__=_C
_OltPonAttrMultiLlidState_Object=MibTableColumn
oltPonAttrMultiLlidState=_OltPonAttrMultiLlidState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,5),_OltPonAttrMultiLlidState_Type())
oltPonAttrMultiLlidState.setMaxAccess(_B)
if mibBuilder.loadTexts:oltPonAttrMultiLlidState.setStatus(_A)
class _ZxAnEponOnuMaxLlidNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnEponOnuMaxLlidNumber_Type.__name__=_C
_ZxAnEponOnuMaxLlidNumber_Object=MibTableColumn
zxAnEponOnuMaxLlidNumber=_ZxAnEponOnuMaxLlidNumber_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,6),_ZxAnEponOnuMaxLlidNumber_Type())
zxAnEponOnuMaxLlidNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuMaxLlidNumber.setStatus(_A)
_OltPonAuthenticatedOnuIdList_Type=DisplayString
_OltPonAuthenticatedOnuIdList_Object=MibTableColumn
oltPonAuthenticatedOnuIdList=_OltPonAuthenticatedOnuIdList_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,7),_OltPonAuthenticatedOnuIdList_Type())
oltPonAuthenticatedOnuIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:oltPonAuthenticatedOnuIdList.setStatus(_A)
class _OltPonDualRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oneG',1),('tenGSymmetric',2),('tenGAsymmetric',3)))
_OltPonDualRate_Type.__name__=_C
_OltPonDualRate_Object=MibTableColumn
oltPonDualRate=_OltPonDualRate_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,8),_OltPonDualRate_Type())
oltPonDualRate.setMaxAccess(_B)
if mibBuilder.loadTexts:oltPonDualRate.setStatus(_A)
class _ZxAnEponIsUseOamCtc2Dot1OrMore_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_ZxAnEponIsUseOamCtc2Dot1OrMore_Type.__name__=_C
_ZxAnEponIsUseOamCtc2Dot1OrMore_Object=MibTableColumn
zxAnEponIsUseOamCtc2Dot1OrMore=_ZxAnEponIsUseOamCtc2Dot1OrMore_Object((1,3,6,1,4,1,3902,1015,1010,1,7,16,1,9),_ZxAnEponIsUseOamCtc2Dot1OrMore_Type())
zxAnEponIsUseOamCtc2Dot1OrMore.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponIsUseOamCtc2Dot1OrMore.setStatus(_A)
_OnuUpStreamPriorityObjectTable_Object=MibTable
onuUpStreamPriorityObjectTable=_OnuUpStreamPriorityObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,17))
if mibBuilder.loadTexts:onuUpStreamPriorityObjectTable.setStatus(_A)
_OnuUpStreamPriorityObjectEntry_Object=MibTableRow
onuUpStreamPriorityObjectEntry=_OnuUpStreamPriorityObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,17,1))
onuUpStreamPriorityObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:onuUpStreamPriorityObjectEntry.setStatus(_A)
_ZxEponOnuUpstreamPriority_Type=Integer32
_ZxEponOnuUpstreamPriority_Object=MibTableColumn
zxEponOnuUpstreamPriority=_ZxEponOnuUpstreamPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,7,17,1,1),_ZxEponOnuUpstreamPriority_Type())
zxEponOnuUpstreamPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuUpstreamPriority.setStatus(_A)
_ZxEponOnuUpstreamDefaultVlan_Type=Integer32
_ZxEponOnuUpstreamDefaultVlan_Object=MibTableColumn
zxEponOnuUpstreamDefaultVlan=_ZxEponOnuUpstreamDefaultVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,7,17,1,2),_ZxEponOnuUpstreamDefaultVlan_Type())
zxEponOnuUpstreamDefaultVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuUpstreamDefaultVlan.setStatus(_A)
class _ZxEponOnuUpStreamPriorityRegenerate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxEponOnuUpStreamPriorityRegenerate_Type.__name__=_C
_ZxEponOnuUpStreamPriorityRegenerate_Object=MibTableColumn
zxEponOnuUpStreamPriorityRegenerate=_ZxEponOnuUpStreamPriorityRegenerate_Object((1,3,6,1,4,1,3902,1015,1010,1,7,17,1,3),_ZxEponOnuUpStreamPriorityRegenerate_Type())
zxEponOnuUpStreamPriorityRegenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuUpStreamPriorityRegenerate.setStatus(_A)
_OnuDownStreamPriorityObjectTable_Object=MibTable
onuDownStreamPriorityObjectTable=_OnuDownStreamPriorityObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,18))
if mibBuilder.loadTexts:onuDownStreamPriorityObjectTable.setStatus(_A)
_OnuDownStreamPriorityObjectEntry_Object=MibTableRow
onuDownStreamPriorityObjectEntry=_OnuDownStreamPriorityObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,18,1))
onuDownStreamPriorityObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:onuDownStreamPriorityObjectEntry.setStatus(_A)
_ZxEponOnuDownstreamPriority_Type=Integer32
_ZxEponOnuDownstreamPriority_Object=MibTableColumn
zxEponOnuDownstreamPriority=_ZxEponOnuDownstreamPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,7,18,1,1),_ZxEponOnuDownstreamPriority_Type())
zxEponOnuDownstreamPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuDownstreamPriority.setStatus(_A)
_ZxEponOnuDownstreamDefaultVlan_Type=Integer32
_ZxEponOnuDownstreamDefaultVlan_Object=MibTableColumn
zxEponOnuDownstreamDefaultVlan=_ZxEponOnuDownstreamDefaultVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,7,18,1,2),_ZxEponOnuDownstreamDefaultVlan_Type())
zxEponOnuDownstreamDefaultVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuDownstreamDefaultVlan.setStatus(_A)
class _ZxEponOnuDownStreamPriorityRegenerate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxEponOnuDownStreamPriorityRegenerate_Type.__name__=_C
_ZxEponOnuDownStreamPriorityRegenerate_Object=MibTableColumn
zxEponOnuDownStreamPriorityRegenerate=_ZxEponOnuDownStreamPriorityRegenerate_Object((1,3,6,1,4,1,3902,1015,1010,1,7,18,1,3),_ZxEponOnuDownStreamPriorityRegenerate_Type())
zxEponOnuDownStreamPriorityRegenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuDownStreamPriorityRegenerate.setStatus(_A)
_ZxEponOnuDbaPriorityObjectTable_Object=MibTable
zxEponOnuDbaPriorityObjectTable=_ZxEponOnuDbaPriorityObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,19))
if mibBuilder.loadTexts:zxEponOnuDbaPriorityObjectTable.setStatus(_A)
_ZxEponOnuDbaPriorityObjectEntry_Object=MibTableRow
zxEponOnuDbaPriorityObjectEntry=_ZxEponOnuDbaPriorityObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,19,1))
zxEponOnuDbaPriorityObjectEntry.setIndexNames((0,_E,_F),(0,_J,_Z))
if mibBuilder.loadTexts:zxEponOnuDbaPriorityObjectEntry.setStatus(_A)
_ZxDbaPriority_Type=Integer32
_ZxDbaPriority_Object=MibTableColumn
zxDbaPriority=_ZxDbaPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,7,19,1,1),_ZxDbaPriority_Type())
zxDbaPriority.setMaxAccess(_K)
if mibBuilder.loadTexts:zxDbaPriority.setStatus(_A)
_ZxCyccleTime_Type=Integer32
_ZxCyccleTime_Object=MibTableColumn
zxCyccleTime=_ZxCyccleTime_Object((1,3,6,1,4,1,3902,1015,1010,1,7,19,1,2),_ZxCyccleTime_Type())
zxCyccleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCyccleTime.setStatus(_A)
_ZxEponOnuOpticalPowerMeasureObjectTable_Object=MibTable
zxEponOnuOpticalPowerMeasureObjectTable=_ZxEponOnuOpticalPowerMeasureObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,20))
if mibBuilder.loadTexts:zxEponOnuOpticalPowerMeasureObjectTable.setStatus(_A)
_ZxEponOnuOpticalPowerMeasureObjectEntry_Object=MibTableRow
zxEponOnuOpticalPowerMeasureObjectEntry=_ZxEponOnuOpticalPowerMeasureObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,20,1))
zxEponOnuOpticalPowerMeasureObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponOnuOpticalPowerMeasureObjectEntry.setStatus(_A)
class _ZxEponOnuTxOpticalPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxEponOnuTxOpticalPower_Type.__name__=_G
_ZxEponOnuTxOpticalPower_Object=MibTableColumn
zxEponOnuTxOpticalPower=_ZxEponOnuTxOpticalPower_Object((1,3,6,1,4,1,3902,1015,1010,1,7,20,1,1),_ZxEponOnuTxOpticalPower_Type())
zxEponOnuTxOpticalPower.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponOnuTxOpticalPower.setStatus(_A)
class _ZxEponOnuRxOpticalPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxEponOnuRxOpticalPower_Type.__name__=_G
_ZxEponOnuRxOpticalPower_Object=MibTableColumn
zxEponOnuRxOpticalPower=_ZxEponOnuRxOpticalPower_Object((1,3,6,1,4,1,3902,1015,1010,1,7,20,1,2),_ZxEponOnuRxOpticalPower_Type())
zxEponOnuRxOpticalPower.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponOnuRxOpticalPower.setStatus(_A)
_ZxEponOltOpticalPowerMeasureObjectTable_Object=MibTable
zxEponOltOpticalPowerMeasureObjectTable=_ZxEponOltOpticalPowerMeasureObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,21))
if mibBuilder.loadTexts:zxEponOltOpticalPowerMeasureObjectTable.setStatus(_A)
_ZxEponOltOpticalPowerMeasureObjectEntry_Object=MibTableRow
zxEponOltOpticalPowerMeasureObjectEntry=_ZxEponOltOpticalPowerMeasureObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,21,1))
zxEponOltOpticalPowerMeasureObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponOltOpticalPowerMeasureObjectEntry.setStatus(_A)
class _ZxEponOltTxOpticalPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxEponOltTxOpticalPower_Type.__name__=_G
_ZxEponOltTxOpticalPower_Object=MibTableColumn
zxEponOltTxOpticalPower=_ZxEponOltTxOpticalPower_Object((1,3,6,1,4,1,3902,1015,1010,1,7,21,1,1),_ZxEponOltTxOpticalPower_Type())
zxEponOltTxOpticalPower.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponOltTxOpticalPower.setStatus(_A)
class _ZxEponOltRxOpticalPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxEponOltRxOpticalPower_Type.__name__=_G
_ZxEponOltRxOpticalPower_Object=MibTableColumn
zxEponOltRxOpticalPower=_ZxEponOltRxOpticalPower_Object((1,3,6,1,4,1,3902,1015,1010,1,7,21,1,2),_ZxEponOltRxOpticalPower_Type())
zxEponOltRxOpticalPower.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponOltRxOpticalPower.setStatus(_A)
_ZxEponHighPriorityFrameObjectTable_Object=MibTable
zxEponHighPriorityFrameObjectTable=_ZxEponHighPriorityFrameObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22))
if mibBuilder.loadTexts:zxEponHighPriorityFrameObjectTable.setStatus(_A)
_ZxEponHighPriorityFrameObjectEntry_Object=MibTableRow
zxEponHighPriorityFrameObjectEntry=_ZxEponHighPriorityFrameObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1))
zxEponHighPriorityFrameObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponHighPriorityFrameObjectEntry.setStatus(_A)
class _Priority0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Priority0_Type.__name__=_C
_Priority0_Object=MibTableColumn
priority0=_Priority0_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1,1),_Priority0_Type())
priority0.setMaxAccess(_B)
if mibBuilder.loadTexts:priority0.setStatus(_A)
class _Priority1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Priority1_Type.__name__=_C
_Priority1_Object=MibTableColumn
priority1=_Priority1_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1,2),_Priority1_Type())
priority1.setMaxAccess(_B)
if mibBuilder.loadTexts:priority1.setStatus(_A)
class _Priority2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Priority2_Type.__name__=_C
_Priority2_Object=MibTableColumn
priority2=_Priority2_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1,3),_Priority2_Type())
priority2.setMaxAccess(_B)
if mibBuilder.loadTexts:priority2.setStatus(_A)
class _Priority3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Priority3_Type.__name__=_C
_Priority3_Object=MibTableColumn
priority3=_Priority3_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1,4),_Priority3_Type())
priority3.setMaxAccess(_B)
if mibBuilder.loadTexts:priority3.setStatus(_A)
class _Priority4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Priority4_Type.__name__=_C
_Priority4_Object=MibTableColumn
priority4=_Priority4_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1,5),_Priority4_Type())
priority4.setMaxAccess(_B)
if mibBuilder.loadTexts:priority4.setStatus(_A)
class _Priority5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Priority5_Type.__name__=_C
_Priority5_Object=MibTableColumn
priority5=_Priority5_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1,6),_Priority5_Type())
priority5.setMaxAccess(_B)
if mibBuilder.loadTexts:priority5.setStatus(_A)
class _Priority6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Priority6_Type.__name__=_C
_Priority6_Object=MibTableColumn
priority6=_Priority6_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1,7),_Priority6_Type())
priority6.setMaxAccess(_B)
if mibBuilder.loadTexts:priority6.setStatus(_A)
class _Priority7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Priority7_Type.__name__=_C
_Priority7_Object=MibTableColumn
priority7=_Priority7_Object((1,3,6,1,4,1,3902,1015,1010,1,7,22,1,8),_Priority7_Type())
priority7.setMaxAccess(_B)
if mibBuilder.loadTexts:priority7.setStatus(_A)
_ZxEponMaxrttObjectTable_Object=MibTable
zxEponMaxrttObjectTable=_ZxEponMaxrttObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,23))
if mibBuilder.loadTexts:zxEponMaxrttObjectTable.setStatus(_A)
_ZxEponMaxrttObjectEntry_Object=MibTableRow
zxEponMaxrttObjectEntry=_ZxEponMaxrttObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,23,1))
zxEponMaxrttObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponMaxrttObjectEntry.setStatus(_A)
_Maxrtt_Type=Integer32
_Maxrtt_Object=MibTableColumn
maxrtt=_Maxrtt_Object((1,3,6,1,4,1,3902,1015,1010,1,7,23,1,1),_Maxrtt_Type())
maxrtt.setMaxAccess(_B)
if mibBuilder.loadTexts:maxrtt.setStatus(_A)
_ZxEponPriorityQueueMapObjectTable_Object=MibTable
zxEponPriorityQueueMapObjectTable=_ZxEponPriorityQueueMapObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24))
if mibBuilder.loadTexts:zxEponPriorityQueueMapObjectTable.setStatus(_A)
_ZxEponPriorityQueueMapObjectEntry_Object=MibTableRow
zxEponPriorityQueueMapObjectEntry=_ZxEponPriorityQueueMapObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1))
zxEponPriorityQueueMapObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponPriorityQueueMapObjectEntry.setStatus(_A)
_Downstreampri0Que_Type=Integer32
_Downstreampri0Que_Object=MibTableColumn
downstreampri0Que=_Downstreampri0Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,1),_Downstreampri0Que_Type())
downstreampri0Que.setMaxAccess(_B)
if mibBuilder.loadTexts:downstreampri0Que.setStatus(_A)
_Downstreampri1Que_Type=Integer32
_Downstreampri1Que_Object=MibTableColumn
downstreampri1Que=_Downstreampri1Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,2),_Downstreampri1Que_Type())
downstreampri1Que.setMaxAccess(_B)
if mibBuilder.loadTexts:downstreampri1Que.setStatus(_A)
_Downstreampri2Que_Type=Integer32
_Downstreampri2Que_Object=MibTableColumn
downstreampri2Que=_Downstreampri2Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,3),_Downstreampri2Que_Type())
downstreampri2Que.setMaxAccess(_B)
if mibBuilder.loadTexts:downstreampri2Que.setStatus(_A)
_Downstreampri3Que_Type=Integer32
_Downstreampri3Que_Object=MibTableColumn
downstreampri3Que=_Downstreampri3Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,4),_Downstreampri3Que_Type())
downstreampri3Que.setMaxAccess(_B)
if mibBuilder.loadTexts:downstreampri3Que.setStatus(_A)
_Downstreampri4Que_Type=Integer32
_Downstreampri4Que_Object=MibTableColumn
downstreampri4Que=_Downstreampri4Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,5),_Downstreampri4Que_Type())
downstreampri4Que.setMaxAccess(_B)
if mibBuilder.loadTexts:downstreampri4Que.setStatus(_A)
_Downstreampri5Que_Type=Integer32
_Downstreampri5Que_Object=MibTableColumn
downstreampri5Que=_Downstreampri5Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,6),_Downstreampri5Que_Type())
downstreampri5Que.setMaxAccess(_B)
if mibBuilder.loadTexts:downstreampri5Que.setStatus(_A)
_Downstreampri6Que_Type=Integer32
_Downstreampri6Que_Object=MibTableColumn
downstreampri6Que=_Downstreampri6Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,7),_Downstreampri6Que_Type())
downstreampri6Que.setMaxAccess(_B)
if mibBuilder.loadTexts:downstreampri6Que.setStatus(_A)
_Downstreampri7Que_Type=Integer32
_Downstreampri7Que_Object=MibTableColumn
downstreampri7Que=_Downstreampri7Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,8),_Downstreampri7Que_Type())
downstreampri7Que.setMaxAccess(_B)
if mibBuilder.loadTexts:downstreampri7Que.setStatus(_A)
_Upstreampri0Que_Type=Integer32
_Upstreampri0Que_Object=MibTableColumn
upstreampri0Que=_Upstreampri0Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,9),_Upstreampri0Que_Type())
upstreampri0Que.setMaxAccess(_B)
if mibBuilder.loadTexts:upstreampri0Que.setStatus(_A)
_Upstreampri1Que_Type=Integer32
_Upstreampri1Que_Object=MibTableColumn
upstreampri1Que=_Upstreampri1Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,10),_Upstreampri1Que_Type())
upstreampri1Que.setMaxAccess(_B)
if mibBuilder.loadTexts:upstreampri1Que.setStatus(_A)
_Upstreampri2Que_Type=Integer32
_Upstreampri2Que_Object=MibTableColumn
upstreampri2Que=_Upstreampri2Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,11),_Upstreampri2Que_Type())
upstreampri2Que.setMaxAccess(_B)
if mibBuilder.loadTexts:upstreampri2Que.setStatus(_A)
_Upstreampri3Que_Type=Integer32
_Upstreampri3Que_Object=MibTableColumn
upstreampri3Que=_Upstreampri3Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,12),_Upstreampri3Que_Type())
upstreampri3Que.setMaxAccess(_B)
if mibBuilder.loadTexts:upstreampri3Que.setStatus(_A)
_Upstreampri4Que_Type=Integer32
_Upstreampri4Que_Object=MibTableColumn
upstreampri4Que=_Upstreampri4Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,13),_Upstreampri4Que_Type())
upstreampri4Que.setMaxAccess(_B)
if mibBuilder.loadTexts:upstreampri4Que.setStatus(_A)
_Upstreampri5Que_Type=Integer32
_Upstreampri5Que_Object=MibTableColumn
upstreampri5Que=_Upstreampri5Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,14),_Upstreampri5Que_Type())
upstreampri5Que.setMaxAccess(_B)
if mibBuilder.loadTexts:upstreampri5Que.setStatus(_A)
_Upstreampri6Que_Type=Integer32
_Upstreampri6Que_Object=MibTableColumn
upstreampri6Que=_Upstreampri6Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,15),_Upstreampri6Que_Type())
upstreampri6Que.setMaxAccess(_B)
if mibBuilder.loadTexts:upstreampri6Que.setStatus(_A)
_Upstreampri7Que_Type=Integer32
_Upstreampri7Que_Object=MibTableColumn
upstreampri7Que=_Upstreampri7Que_Object((1,3,6,1,4,1,3902,1015,1010,1,7,24,1,16),_Upstreampri7Que_Type())
upstreampri7Que.setMaxAccess(_B)
if mibBuilder.loadTexts:upstreampri7Que.setStatus(_A)
_ZxEponRxHecObjectTable_Object=MibTable
zxEponRxHecObjectTable=_ZxEponRxHecObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,25))
if mibBuilder.loadTexts:zxEponRxHecObjectTable.setStatus(_A)
_ZxEponRxHecObjectEntry_Object=MibTableRow
zxEponRxHecObjectEntry=_ZxEponRxHecObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,25,1))
zxEponRxHecObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponRxHecObjectEntry.setStatus(_A)
class _Rxhec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ahDraft8023',1),('ahStandard8023',2),('both',3),('no',4)))
_Rxhec_Type.__name__=_C
_Rxhec_Object=MibTableColumn
rxhec=_Rxhec_Object((1,3,6,1,4,1,3902,1015,1010,1,7,25,1,1),_Rxhec_Type())
rxhec.setMaxAccess(_B)
if mibBuilder.loadTexts:rxhec.setStatus(_A)
_ZxEponOnuAutoCfgObjectTable_Object=MibTable
zxEponOnuAutoCfgObjectTable=_ZxEponOnuAutoCfgObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,26))
if mibBuilder.loadTexts:zxEponOnuAutoCfgObjectTable.setStatus(_A)
_ZxEponOnuAutoCfgObjectEntry_Object=MibTableRow
zxEponOnuAutoCfgObjectEntry=_ZxEponOnuAutoCfgObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,26,1))
zxEponOnuAutoCfgObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponOnuAutoCfgObjectEntry.setStatus(_A)
class _OnuBindStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_OnuBindStatus_Type.__name__=_C
_OnuBindStatus_Object=MibTableColumn
onuBindStatus=_OnuBindStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,26,1,1),_OnuBindStatus_Type())
onuBindStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:onuBindStatus.setStatus(_A)
class _OnuAutoCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_OnuAutoCfgStatus_Type.__name__=_C
_OnuAutoCfgStatus_Object=MibTableColumn
onuAutoCfgStatus=_OnuAutoCfgStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,26,1,2),_OnuAutoCfgStatus_Type())
onuAutoCfgStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:onuAutoCfgStatus.setStatus(_A)
_ZxEponIpPoolObjectTable_Object=MibTable
zxEponIpPoolObjectTable=_ZxEponIpPoolObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27))
if mibBuilder.loadTexts:zxEponIpPoolObjectTable.setStatus(_A)
_ZxEponIpPoolObjectEntry_Object=MibTableRow
zxEponIpPoolObjectEntry=_ZxEponIpPoolObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1))
zxEponIpPoolObjectEntry.setIndexNames((0,_J,_a))
if mibBuilder.loadTexts:zxEponIpPoolObjectEntry.setStatus(_A)
class _ZxEponIpPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_ZxEponIpPoolName_Type.__name__=_S
_ZxEponIpPoolName_Object=MibTableColumn
zxEponIpPoolName=_ZxEponIpPoolName_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,1),_ZxEponIpPoolName_Type())
zxEponIpPoolName.setMaxAccess(_K)
if mibBuilder.loadTexts:zxEponIpPoolName.setStatus(_A)
_ZxEponIpPoolIpBegin_Type=IpAddress
_ZxEponIpPoolIpBegin_Object=MibTableColumn
zxEponIpPoolIpBegin=_ZxEponIpPoolIpBegin_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,2),_ZxEponIpPoolIpBegin_Type())
zxEponIpPoolIpBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolIpBegin.setStatus(_A)
_ZxEponIpPoolIpEnd_Type=IpAddress
_ZxEponIpPoolIpEnd_Object=MibTableColumn
zxEponIpPoolIpEnd=_ZxEponIpPoolIpEnd_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,3),_ZxEponIpPoolIpEnd_Type())
zxEponIpPoolIpEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolIpEnd.setStatus(_A)
_ZxEponIpPoolMask_Type=IpAddress
_ZxEponIpPoolMask_Object=MibTableColumn
zxEponIpPoolMask=_ZxEponIpPoolMask_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,4),_ZxEponIpPoolMask_Type())
zxEponIpPoolMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolMask.setStatus(_A)
_ZxEponIpPoolpriority_Type=Integer32
_ZxEponIpPoolpriority_Object=MibTableColumn
zxEponIpPoolpriority=_ZxEponIpPoolpriority_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,5),_ZxEponIpPoolpriority_Type())
zxEponIpPoolpriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolpriority.setStatus(_A)
_ZxEponIpPoolVlan_Type=Integer32
_ZxEponIpPoolVlan_Object=MibTableColumn
zxEponIpPoolVlan=_ZxEponIpPoolVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,6),_ZxEponIpPoolVlan_Type())
zxEponIpPoolVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolVlan.setStatus(_A)
_ZxEponIpPoolNetIp_Type=IpAddress
_ZxEponIpPoolNetIp_Object=MibTableColumn
zxEponIpPoolNetIp=_ZxEponIpPoolNetIp_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,7),_ZxEponIpPoolNetIp_Type())
zxEponIpPoolNetIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolNetIp.setStatus(_A)
_ZxEponIpPoolNetMask_Type=IpAddress
_ZxEponIpPoolNetMask_Object=MibTableColumn
zxEponIpPoolNetMask=_ZxEponIpPoolNetMask_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,8),_ZxEponIpPoolNetMask_Type())
zxEponIpPoolNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolNetMask.setStatus(_A)
_ZxEponIpPoolGateway_Type=IpAddress
_ZxEponIpPoolGateway_Object=MibTableColumn
zxEponIpPoolGateway=_ZxEponIpPoolGateway_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,9),_ZxEponIpPoolGateway_Type())
zxEponIpPoolGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolGateway.setStatus(_A)
_ZxEponIpPoolRowStatus_Type=RowStatus
_ZxEponIpPoolRowStatus_Object=MibTableColumn
zxEponIpPoolRowStatus=_ZxEponIpPoolRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,27,1,10),_ZxEponIpPoolRowStatus_Type())
zxEponIpPoolRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxEponIpPoolRowStatus.setStatus(_A)
_ZxEponRunIpObjectTable_Object=MibTable
zxEponRunIpObjectTable=_ZxEponRunIpObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28))
if mibBuilder.loadTexts:zxEponRunIpObjectTable.setStatus(_A)
_ZxEponRunIpObjectEntry_Object=MibTableRow
zxEponRunIpObjectEntry=_ZxEponRunIpObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1))
zxEponRunIpObjectEntry.setIndexNames((0,_J,_b))
if mibBuilder.loadTexts:zxEponRunIpObjectEntry.setStatus(_A)
_ZxEponRunIp_Type=Integer32
_ZxEponRunIp_Object=MibTableColumn
zxEponRunIp=_ZxEponRunIp_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,1),_ZxEponRunIp_Type())
zxEponRunIp.setMaxAccess(_K)
if mibBuilder.loadTexts:zxEponRunIp.setStatus(_A)
_ZxEponRunMask_Type=IpAddress
_ZxEponRunMask_Object=MibTableColumn
zxEponRunMask=_ZxEponRunMask_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,2),_ZxEponRunMask_Type())
zxEponRunMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunMask.setStatus(_A)
_ZxEponRunOnuIfIndex_Type=Integer32
_ZxEponRunOnuIfIndex_Object=MibTableColumn
zxEponRunOnuIfIndex=_ZxEponRunOnuIfIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,3),_ZxEponRunOnuIfIndex_Type())
zxEponRunOnuIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunOnuIfIndex.setStatus(_A)
_ZxEponRunIpPriority_Type=Integer32
_ZxEponRunIpPriority_Object=MibTableColumn
zxEponRunIpPriority=_ZxEponRunIpPriority_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,4),_ZxEponRunIpPriority_Type())
zxEponRunIpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunIpPriority.setStatus(_A)
_ZxEponRunIpVlan_Type=Integer32
_ZxEponRunIpVlan_Object=MibTableColumn
zxEponRunIpVlan=_ZxEponRunIpVlan_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,5),_ZxEponRunIpVlan_Type())
zxEponRunIpVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunIpVlan.setStatus(_A)
_ZxEponRunIpNetIp_Type=IpAddress
_ZxEponRunIpNetIp_Object=MibTableColumn
zxEponRunIpNetIp=_ZxEponRunIpNetIp_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,6),_ZxEponRunIpNetIp_Type())
zxEponRunIpNetIp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunIpNetIp.setStatus(_A)
_ZxEponRunIpNetMask_Type=IpAddress
_ZxEponRunIpNetMask_Object=MibTableColumn
zxEponRunIpNetMask=_ZxEponRunIpNetMask_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,7),_ZxEponRunIpNetMask_Type())
zxEponRunIpNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunIpNetMask.setStatus(_A)
_ZxEponRunIpGateway_Type=IpAddress
_ZxEponRunIpGateway_Object=MibTableColumn
zxEponRunIpGateway=_ZxEponRunIpGateway_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,8),_ZxEponRunIpGateway_Type())
zxEponRunIpGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunIpGateway.setStatus(_A)
class _ZxEponRunIpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_ZxEponRunIpStatus_Type.__name__=_C
_ZxEponRunIpStatus_Object=MibTableColumn
zxEponRunIpStatus=_ZxEponRunIpStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,9),_ZxEponRunIpStatus_Type())
zxEponRunIpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunIpStatus.setStatus(_A)
class _ZxEponRunIpCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),('dynamic',2)))
_ZxEponRunIpCfgMode_Type.__name__=_C
_ZxEponRunIpCfgMode_Object=MibTableColumn
zxEponRunIpCfgMode=_ZxEponRunIpCfgMode_Object((1,3,6,1,4,1,3902,1015,1010,1,7,28,1,10),_ZxEponRunIpCfgMode_Type())
zxEponRunIpCfgMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRunIpCfgMode.setStatus(_A)
_ZxEponIpPoolConjPonObjectTable_Object=MibTable
zxEponIpPoolConjPonObjectTable=_ZxEponIpPoolConjPonObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,29))
if mibBuilder.loadTexts:zxEponIpPoolConjPonObjectTable.setStatus(_A)
_ZxEponIpPoolConjPonObjectEntry_Object=MibTableRow
zxEponIpPoolConjPonObjectEntry=_ZxEponIpPoolConjPonObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,29,1))
zxEponIpPoolConjPonObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponIpPoolConjPonObjectEntry.setStatus(_A)
class _ZxEponIpPoolConjPonName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_ZxEponIpPoolConjPonName_Type.__name__=_S
_ZxEponIpPoolConjPonName_Object=MibTableColumn
zxEponIpPoolConjPonName=_ZxEponIpPoolConjPonName_Object((1,3,6,1,4,1,3902,1015,1010,1,7,29,1,1),_ZxEponIpPoolConjPonName_Type())
zxEponIpPoolConjPonName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponIpPoolConjPonName.setStatus(_A)
_ZxEponIpPoolConjRowStatus_Type=RowStatus
_ZxEponIpPoolConjRowStatus_Object=MibTableColumn
zxEponIpPoolConjRowStatus=_ZxEponIpPoolConjRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,29,1,2),_ZxEponIpPoolConjRowStatus_Type())
zxEponIpPoolConjRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxEponIpPoolConjRowStatus.setStatus(_A)
_ZxEponBwProfileAdmin_ObjectIdentity=ObjectIdentity
zxEponBwProfileAdmin=_ZxEponBwProfileAdmin_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,7,30))
_ZxEponBwProfileTable_Object=MibTable
zxEponBwProfileTable=_ZxEponBwProfileTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1))
if mibBuilder.loadTexts:zxEponBwProfileTable.setStatus(_A)
_ZxEponBwProfileEntry_Object=MibTableRow
zxEponBwProfileEntry=_ZxEponBwProfileEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1))
zxEponBwProfileEntry.setIndexNames((0,_J,_c))
if mibBuilder.loadTexts:zxEponBwProfileEntry.setStatus(_A)
class _ProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ProfileIndex_Type.__name__=_C
_ProfileIndex_Object=MibTableColumn
profileIndex=_ProfileIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,1),_ProfileIndex_Type())
profileIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:profileIndex.setStatus(_A)
class _ProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ProfileName_Type.__name__=_G
_ProfileName_Object=MibTableColumn
profileName=_ProfileName_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,2),_ProfileName_Type())
profileName.setMaxAccess(_B)
if mibBuilder.loadTexts:profileName.setStatus(_A)
class _UpBwProfileFixedBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_UpBwProfileFixedBw_Type.__name__=_C
_UpBwProfileFixedBw_Object=MibTableColumn
upBwProfileFixedBw=_UpBwProfileFixedBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,3),_UpBwProfileFixedBw_Type())
upBwProfileFixedBw.setMaxAccess(_B)
if mibBuilder.loadTexts:upBwProfileFixedBw.setStatus(_A)
class _UpBwProfileAssuredBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,1000000))
_UpBwProfileAssuredBw_Type.__name__=_C
_UpBwProfileAssuredBw_Object=MibTableColumn
upBwProfileAssuredBw=_UpBwProfileAssuredBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,4),_UpBwProfileAssuredBw_Type())
upBwProfileAssuredBw.setMaxAccess(_B)
if mibBuilder.loadTexts:upBwProfileAssuredBw.setStatus(_A)
class _UpBwProfileMaximumBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,1000000))
_UpBwProfileMaximumBw_Type.__name__=_C
_UpBwProfileMaximumBw_Object=MibTableColumn
upBwProfileMaximumBw=_UpBwProfileMaximumBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,5),_UpBwProfileMaximumBw_Type())
upBwProfileMaximumBw.setMaxAccess(_B)
if mibBuilder.loadTexts:upBwProfileMaximumBw.setStatus(_A)
class _UpBwProfileMaxBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_UpBwProfileMaxBurstSize_Type.__name__=_C
_UpBwProfileMaxBurstSize_Object=MibTableColumn
upBwProfileMaxBurstSize=_UpBwProfileMaxBurstSize_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,6),_UpBwProfileMaxBurstSize_Type())
upBwProfileMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:upBwProfileMaxBurstSize.setStatus(_A)
class _UpBwProfilePri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_UpBwProfilePri_Type.__name__=_C
_UpBwProfilePri_Object=MibTableColumn
upBwProfilePri=_UpBwProfilePri_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,7),_UpBwProfilePri_Type())
upBwProfilePri.setMaxAccess(_B)
if mibBuilder.loadTexts:upBwProfilePri.setStatus(_A)
class _UpBwProfileFixedPacketSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1582))
_UpBwProfileFixedPacketSize_Type.__name__=_C
_UpBwProfileFixedPacketSize_Object=MibTableColumn
upBwProfileFixedPacketSize=_UpBwProfileFixedPacketSize_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,8),_UpBwProfileFixedPacketSize_Type())
upBwProfileFixedPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:upBwProfileFixedPacketSize.setStatus(_A)
class _DownBwProfileMaximumBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,999994))
_DownBwProfileMaximumBw_Type.__name__=_C
_DownBwProfileMaximumBw_Object=MibTableColumn
downBwProfileMaximumBw=_DownBwProfileMaximumBw_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,9),_DownBwProfileMaximumBw_Type())
downBwProfileMaximumBw.setMaxAccess(_B)
if mibBuilder.loadTexts:downBwProfileMaximumBw.setStatus(_A)
class _DownBwProfileMaxBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_DownBwProfileMaxBurstSize_Type.__name__=_C
_DownBwProfileMaxBurstSize_Object=MibTableColumn
downBwProfileMaxBurstSize=_DownBwProfileMaxBurstSize_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,10),_DownBwProfileMaxBurstSize_Type())
downBwProfileMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:downBwProfileMaxBurstSize.setStatus(_A)
_BwProfileRowStatus_Type=RowStatus
_BwProfileRowStatus_Object=MibTableColumn
bwProfileRowStatus=_BwProfileRowStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,1,1,11),_BwProfileRowStatus_Type())
bwProfileRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:bwProfileRowStatus.setStatus(_A)
_BwProfileNextIndex_Type=Integer32
_BwProfileNextIndex_Object=MibScalar
bwProfileNextIndex=_BwProfileNextIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,7,30,2),_BwProfileNextIndex_Type())
bwProfileNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bwProfileNextIndex.setStatus(_A)
_ZxEponOnuBwCfgTable_Object=MibTable
zxEponOnuBwCfgTable=_ZxEponOnuBwCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,32))
if mibBuilder.loadTexts:zxEponOnuBwCfgTable.setStatus(_A)
_ZxEponOnuBwCfgEntry_Object=MibTableRow
zxEponOnuBwCfgEntry=_ZxEponOnuBwCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,32,1))
zxEponOnuBwCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponOnuBwCfgEntry.setStatus(_A)
class _OnuCfgBwProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_OnuCfgBwProfileIndex_Type.__name__=_C
_OnuCfgBwProfileIndex_Object=MibTableColumn
onuCfgBwProfileIndex=_OnuCfgBwProfileIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,7,32,1,1),_OnuCfgBwProfileIndex_Type())
onuCfgBwProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuCfgBwProfileIndex.setStatus(_A)
_ZxEponOnuIpCfgTable_Object=MibTable
zxEponOnuIpCfgTable=_ZxEponOnuIpCfgTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,33))
if mibBuilder.loadTexts:zxEponOnuIpCfgTable.setStatus(_A)
_ZxEponOnuIpCfgEntry_Object=MibTableRow
zxEponOnuIpCfgEntry=_ZxEponOnuIpCfgEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,33,1))
zxEponOnuIpCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponOnuIpCfgEntry.setStatus(_A)
_ZxEponOnuIpCfgIpAddr_Type=IpAddress
_ZxEponOnuIpCfgIpAddr_Object=MibTableColumn
zxEponOnuIpCfgIpAddr=_ZxEponOnuIpCfgIpAddr_Object((1,3,6,1,4,1,3902,1015,1010,1,7,33,1,1),_ZxEponOnuIpCfgIpAddr_Type())
zxEponOnuIpCfgIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponOnuIpCfgIpAddr.setStatus(_A)
class _ZxEponOnuIpCfgOperator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('assign',1),('release',2)))
_ZxEponOnuIpCfgOperator_Type.__name__=_C
_ZxEponOnuIpCfgOperator_Object=MibTableColumn
zxEponOnuIpCfgOperator=_ZxEponOnuIpCfgOperator_Object((1,3,6,1,4,1,3902,1015,1010,1,7,33,1,2),_ZxEponOnuIpCfgOperator_Type())
zxEponOnuIpCfgOperator.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuIpCfgOperator.setStatus(_A)
_ZxEponOnuAutoConfigTable_Object=MibTable
zxEponOnuAutoConfigTable=_ZxEponOnuAutoConfigTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,34))
if mibBuilder.loadTexts:zxEponOnuAutoConfigTable.setStatus(_A)
_ZxEponOnuAutoConfigEntry_Object=MibTableRow
zxEponOnuAutoConfigEntry=_ZxEponOnuAutoConfigEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,34,1))
zxEponOnuAutoConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponOnuAutoConfigEntry.setStatus(_A)
class _ZxEponOnuAutoConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ZxEponOnuAutoConfigStatus_Type.__name__=_C
_ZxEponOnuAutoConfigStatus_Object=MibTableColumn
zxEponOnuAutoConfigStatus=_ZxEponOnuAutoConfigStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,34,1,1),_ZxEponOnuAutoConfigStatus_Type())
zxEponOnuAutoConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuAutoConfigStatus.setStatus(_A)
class _ZxEponOnuVoipAutoConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ZxEponOnuVoipAutoConfigStatus_Type.__name__=_C
_ZxEponOnuVoipAutoConfigStatus_Object=MibTableColumn
zxEponOnuVoipAutoConfigStatus=_ZxEponOnuVoipAutoConfigStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,7,34,1,2),_ZxEponOnuVoipAutoConfigStatus_Type())
zxEponOnuVoipAutoConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponOnuVoipAutoConfigStatus.setStatus(_A)
_ZxEponRunningCtrl_ObjectIdentity=ObjectIdentity
zxEponRunningCtrl=_ZxEponRunningCtrl_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,7,35))
class _ZxEponRevision_Type(Bits):namedValues=NamedValues(('ctc21',1))
_ZxEponRevision_Type.__name__='Bits'
_ZxEponRevision_Object=MibScalar
zxEponRevision=_ZxEponRevision_Object((1,3,6,1,4,1,3902,1015,1010,1,7,35,1),_ZxEponRevision_Type())
zxEponRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponRevision.setStatus(_A)
_OnuCustomObjectTable_Object=MibTable
onuCustomObjectTable=_OnuCustomObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,36))
if mibBuilder.loadTexts:onuCustomObjectTable.setStatus(_A)
_OnuCustomObjectEntry_Object=MibTableRow
onuCustomObjectEntry=_OnuCustomObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,36,1))
onuCustomObjectEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:onuCustomObjectEntry.setStatus(_A)
class _OnuOnlineForwardAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OnuOnlineForwardAction_Type.__name__=_C
_OnuOnlineForwardAction_Object=MibTableColumn
onuOnlineForwardAction=_OnuOnlineForwardAction_Object((1,3,6,1,4,1,3902,1015,1010,1,7,36,1,1),_OnuOnlineForwardAction_Type())
onuOnlineForwardAction.setMaxAccess(_B)
if mibBuilder.loadTexts:onuOnlineForwardAction.setStatus(_A)
_ZxAnEponOnuVportMgmtTable_Object=MibTable
zxAnEponOnuVportMgmtTable=_ZxAnEponOnuVportMgmtTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,37))
if mibBuilder.loadTexts:zxAnEponOnuVportMgmtTable.setStatus(_A)
_ZxAnEponOnuVportMgmtTableEntry_Object=MibTableRow
zxAnEponOnuVportMgmtTableEntry=_ZxAnEponOnuVportMgmtTableEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,37,1))
zxAnEponOnuVportMgmtTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnEponOnuVportMgmtTableEntry.setStatus(_A)
_ZxAnEponOnuVportMacAddress_Type=MacAddress
_ZxAnEponOnuVportMacAddress_Object=MibTableColumn
zxAnEponOnuVportMacAddress=_ZxAnEponOnuVportMacAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,7,37,1,1),_ZxAnEponOnuVportMacAddress_Type())
zxAnEponOnuVportMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEponOnuVportMacAddress.setStatus(_A)
class _ZxAnEponOnuVportCurrAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),(_Q,2),('pass',3),(_R,4)))
_ZxAnEponOnuVportCurrAuthState_Type.__name__=_C
_ZxAnEponOnuVportCurrAuthState_Object=MibTableColumn
zxAnEponOnuVportCurrAuthState=_ZxAnEponOnuVportCurrAuthState_Object((1,3,6,1,4,1,3902,1015,1010,1,7,37,1,2),_ZxAnEponOnuVportCurrAuthState_Type())
zxAnEponOnuVportCurrAuthState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEponOnuVportCurrAuthState.setStatus(_A)
_ZxEponQueueBufferObjectTable_Object=MibTable
zxEponQueueBufferObjectTable=_ZxEponQueueBufferObjectTable_Object((1,3,6,1,4,1,3902,1015,1010,1,7,38))
if mibBuilder.loadTexts:zxEponQueueBufferObjectTable.setStatus(_A)
_ZxEponQueueBufferObjectEntry_Object=MibTableRow
zxEponQueueBufferObjectEntry=_ZxEponQueueBufferObjectEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,7,38,1))
zxEponQueueBufferObjectEntry.setIndexNames((0,_J,_d),(0,_J,_e),(0,_J,_f))
if mibBuilder.loadTexts:zxEponQueueBufferObjectEntry.setStatus(_A)
_ZxEponQueueRackNo_Type=Integer32
_ZxEponQueueRackNo_Object=MibTableColumn
zxEponQueueRackNo=_ZxEponQueueRackNo_Object((1,3,6,1,4,1,3902,1015,1010,1,7,38,1,1),_ZxEponQueueRackNo_Type())
zxEponQueueRackNo.setMaxAccess(_K)
if mibBuilder.loadTexts:zxEponQueueRackNo.setStatus(_A)
_ZxEponQueueShelfNo_Type=Integer32
_ZxEponQueueShelfNo_Object=MibTableColumn
zxEponQueueShelfNo=_ZxEponQueueShelfNo_Object((1,3,6,1,4,1,3902,1015,1010,1,7,38,1,2),_ZxEponQueueShelfNo_Type())
zxEponQueueShelfNo.setMaxAccess(_K)
if mibBuilder.loadTexts:zxEponQueueShelfNo.setStatus(_A)
_ZxEponQueueSlotNo_Type=Integer32
_ZxEponQueueSlotNo_Object=MibTableColumn
zxEponQueueSlotNo=_ZxEponQueueSlotNo_Object((1,3,6,1,4,1,3902,1015,1010,1,7,38,1,3),_ZxEponQueueSlotNo_Type())
zxEponQueueSlotNo.setMaxAccess(_K)
if mibBuilder.loadTexts:zxEponQueueSlotNo.setStatus(_A)
class _ZxEponQueueBufferSize_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1020))
_ZxEponQueueBufferSize_Type.__name__=_C
_ZxEponQueueBufferSize_Object=MibTableColumn
zxEponQueueBufferSize=_ZxEponQueueBufferSize_Object((1,3,6,1,4,1,3902,1015,1010,1,7,38,1,4),_ZxEponQueueBufferSize_Type())
zxEponQueueBufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxEponQueueBufferSize.setStatus(_A)
if mibBuilder.loadTexts:zxEponQueueBufferSize.setUnits('kbytes')
_ZxEponMgmtIndex_ObjectIdentity=ObjectIdentity
zxEponMgmtIndex=_ZxEponMgmtIndex_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,8))
_ZxEponIfIndexTable_Object=MibTable
zxEponIfIndexTable=_ZxEponIfIndexTable_Object((1,3,6,1,4,1,3902,1015,1010,1,8,1))
if mibBuilder.loadTexts:zxEponIfIndexTable.setStatus(_A)
_ZxEponIfIndexEntry_Object=MibTableRow
zxEponIfIndexEntry=_ZxEponIfIndexEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,8,1,1))
zxEponIfIndexEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxEponIfIndexEntry.setStatus(_A)
_ZxEponifIndex_Type=Integer32
_ZxEponifIndex_Object=MibTableColumn
zxEponifIndex=_ZxEponifIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,8,1,1,1),_ZxEponifIndex_Type())
zxEponifIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zxEponifIndex.setStatus(_A)
_ZxEponEntryStatus_Type=RowStatus
_ZxEponEntryStatus_Object=MibTableColumn
zxEponEntryStatus=_ZxEponEntryStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,8,1,1,2),_ZxEponEntryStatus_Type())
zxEponEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxEponEntryStatus.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'privateObjects':privateObjects,'sysAttrObjectTable':sysAttrObjectTable,'sysAttrObjectEntry':sysAttrObjectEntry,'sysOnuAdminAuthMode':sysOnuAdminAuthMode,'sysAttrAutoAuthEnable':sysAttrAutoAuthEnable,'macHwAuthOnuState':macHwAuthOnuState,'zxAnEponOnuSilenceEnable':zxAnEponOnuSilenceEnable,'oltLinkAdminTestObjectTable':oltLinkAdminTestObjectTable,'oltLinkAdminTestObjectEntry':oltLinkAdminTestObjectEntry,'testControlMode':testControlMode,'testResult':testResult,'oltLoopbackObjectTable':oltLoopbackObjectTable,'oltLoopbackObjectEntry':oltLoopbackObjectEntry,'loopbackStation':loopbackStation,'loopbackDirection':loopbackDirection,'loopbackAdministration':loopbackAdministration,'loopbackState':loopbackState,'onuAdminObjectTable':onuAdminObjectTable,'onuAdminObjectEntry':onuAdminObjectEntry,'onuDescript':onuDescript,'onuSplitterSn':onuSplitterSn,'onuOpticalLineSn':onuOpticalLineSn,'onuUserInfo':onuUserInfo,'onuType':onuType,'onuAdminState':onuAdminState,'onuAuthMACAddress':onuAuthMACAddress,'onuRegisterMACAddress':onuRegisterMACAddress,'onuAuthMACSn':onuAuthMACSn,'onuRegisterSn':onuRegisterSn,'onuCurrentRegState':onuCurrentRegState,'onuRegisterTime':onuRegisterTime,'onuCurrAdminAuthState':onuCurrAdminAuthState,'onuLatelyPassAdminAuthTime':onuLatelyPassAdminAuthTime,'onuCurrDot1xAuthState':onuCurrDot1xAuthState,'onuLatelyPassDot1xAuthTime':onuLatelyPassDot1xAuthTime,'onuMgmtOnlineStatus':onuMgmtOnlineStatus,'onuActiveStatus':onuActiveStatus,'onuMgmtEntryStatus':onuMgmtEntryStatus,'onuMgmtIpCfgMode':onuMgmtIpCfgMode,'onuAuthLoid':onuAuthLoid,'onuAuthPassword':onuAuthPassword,'onuRegisterLoid':onuRegisterLoid,'onuRegisterPassword':onuRegisterPassword,'zxAnEponOnuCreateTime':zxAnEponOnuCreateTime,'zxAnEponOnuLastOfflineTime':zxAnEponOnuLastOfflineTime,'oltEncryAdminObjectTable':oltEncryAdminObjectTable,'oltEncryAdminObjectEntry':oltEncryAdminObjectEntry,'encryptArithmetic':encryptArithmetic,'keyUpdateTime':keyUpdateTime,'keyUpdateTimeout':keyUpdateTimeout,'startEncryptThreshold':startEncryptThreshold,'lineEncryAdminObjectTable':lineEncryAdminObjectTable,'lineEncryAdminObjectEntry':lineEncryAdminObjectEntry,'encryptMode':encryptMode,'encrypeState':encrypeState,'slaUpAdminObjectTable':slaUpAdminObjectTable,'slaUpAdminObjectEntry':slaUpAdminObjectEntry,'upFixedBw':upFixedBw,'upAssuredBw':upAssuredBw,'upMaximumBw':upMaximumBw,'upMaxBurstSize':upMaxBurstSize,'upPri':upPri,'upMaxTimeDelay':upMaxTimeDelay,'upMaxDrift':upMaxDrift,'upFixedPacketSize':upFixedPacketSize,'slaDownAdminObjectTable':slaDownAdminObjectTable,'slaDownAdminObjectEntry':slaDownAdminObjectEntry,'downAssuredBw':downAssuredBw,'downMaximumBw':downMaximumBw,'downMaxBurstSize':downMaxBurstSize,'downPri':downPri,'downMaxTimeDelay':downMaxTimeDelay,'downMaxDrift':downMaxDrift,'slaP2pAdminObjectTable':slaP2pAdminObjectTable,'slaP2pAdminObjectEntry':slaP2pAdminObjectEntry,'p2pAssuredBw':p2pAssuredBw,'p2pMaximumBw':p2pMaximumBw,'p2pMaxBurstSize':p2pMaxBurstSize,'p2pPri':p2pPri,'p2pMaxTimeDelay':p2pMaxTimeDelay,'p2pMaxDrift':p2pMaxDrift,'p2pModeAdminObjectTable':p2pModeAdminObjectTable,'p2pModeAdminObjectEntry':p2pModeAdminObjectEntry,'eponP2pMode':eponP2pMode,'p2pGroupAdminObjectTable':p2pGroupAdminObjectTable,'p2pGroupAdminObjectEntry':p2pGroupAdminObjectEntry,_X:eponP2pGroupId,'eponP2pGroupName':eponP2pGroupName,'eponP2pGroupOnus':eponP2pGroupOnus,'eponP2pGroupAdminStatus':eponP2pGroupAdminStatus,'eponP2pGroupOpStatus':eponP2pGroupOpStatus,'eponP2pGroupRowStatus':eponP2pGroupRowStatus,'p2pTransmitAdminObjectTable':p2pTransmitAdminObjectTable,'p2pTransmitAdminObjectEntry':p2pTransmitAdminObjectEntry,'eponP2pCfgAddressNotFoundEnableFlood':eponP2pCfgAddressNotFoundEnableFlood,'eponP2pCfgBroadcastEnableFlood':eponP2pCfgBroadcastEnableFlood,'onuUnPassedAdminAuthInfoTable':onuUnPassedAdminAuthInfoTable,'onuUnPassedAdminAuthInfoEntry':onuUnPassedAdminAuthInfoEntry,_Y:onuIndex,'onuRegisterMacAddress':onuRegisterMacAddress,'onuReportSn':onuReportSn,'onuAdminAuthState':onuAdminAuthState,'onuDot1xAuthState':onuDot1xAuthState,'onuUplineTime':onuUplineTime,'onuReportLoid':onuReportLoid,'onuReportPassword':onuReportPassword,'onuReportType':onuReportType,'zxAnEponOnuSwVersion':zxAnEponOnuSwVersion,'zxAnEponOnuHwVersion':zxAnEponOnuHwVersion,'zxAnEponOnuOamBuildStatus':zxAnEponOnuOamBuildStatus,'onuConfigAdminObjectTable':onuConfigAdminObjectTable,'onuConfigAdminObjectEntry':onuConfigAdminObjectEntry,'onuConfigState':onuConfigState,'onuCfgErrObjTables':onuCfgErrObjTables,'oltPonAttrObjectTable':oltPonAttrObjectTable,'oltPonAttrObjectEntry':oltPonAttrObjectEntry,'oltPonAttrName':oltPonAttrName,'oltPonPonAttrDesc':oltPonPonAttrDesc,'oltPonAttrReset':oltPonAttrReset,'oltPonAttrResetCounters':oltPonAttrResetCounters,'oltPonAttrMultiLlidState':oltPonAttrMultiLlidState,'zxAnEponOnuMaxLlidNumber':zxAnEponOnuMaxLlidNumber,'oltPonAuthenticatedOnuIdList':oltPonAuthenticatedOnuIdList,'oltPonDualRate':oltPonDualRate,'zxAnEponIsUseOamCtc2Dot1OrMore':zxAnEponIsUseOamCtc2Dot1OrMore,'onuUpStreamPriorityObjectTable':onuUpStreamPriorityObjectTable,'onuUpStreamPriorityObjectEntry':onuUpStreamPriorityObjectEntry,'zxEponOnuUpstreamPriority':zxEponOnuUpstreamPriority,'zxEponOnuUpstreamDefaultVlan':zxEponOnuUpstreamDefaultVlan,'zxEponOnuUpStreamPriorityRegenerate':zxEponOnuUpStreamPriorityRegenerate,'onuDownStreamPriorityObjectTable':onuDownStreamPriorityObjectTable,'onuDownStreamPriorityObjectEntry':onuDownStreamPriorityObjectEntry,'zxEponOnuDownstreamPriority':zxEponOnuDownstreamPriority,'zxEponOnuDownstreamDefaultVlan':zxEponOnuDownstreamDefaultVlan,'zxEponOnuDownStreamPriorityRegenerate':zxEponOnuDownStreamPriorityRegenerate,'zxEponOnuDbaPriorityObjectTable':zxEponOnuDbaPriorityObjectTable,'zxEponOnuDbaPriorityObjectEntry':zxEponOnuDbaPriorityObjectEntry,_Z:zxDbaPriority,'zxCyccleTime':zxCyccleTime,'zxEponOnuOpticalPowerMeasureObjectTable':zxEponOnuOpticalPowerMeasureObjectTable,'zxEponOnuOpticalPowerMeasureObjectEntry':zxEponOnuOpticalPowerMeasureObjectEntry,'zxEponOnuTxOpticalPower':zxEponOnuTxOpticalPower,'zxEponOnuRxOpticalPower':zxEponOnuRxOpticalPower,'zxEponOltOpticalPowerMeasureObjectTable':zxEponOltOpticalPowerMeasureObjectTable,'zxEponOltOpticalPowerMeasureObjectEntry':zxEponOltOpticalPowerMeasureObjectEntry,'zxEponOltTxOpticalPower':zxEponOltTxOpticalPower,'zxEponOltRxOpticalPower':zxEponOltRxOpticalPower,'zxEponHighPriorityFrameObjectTable':zxEponHighPriorityFrameObjectTable,'zxEponHighPriorityFrameObjectEntry':zxEponHighPriorityFrameObjectEntry,'priority0':priority0,'priority1':priority1,'priority2':priority2,'priority3':priority3,'priority4':priority4,'priority5':priority5,'priority6':priority6,'priority7':priority7,'zxEponMaxrttObjectTable':zxEponMaxrttObjectTable,'zxEponMaxrttObjectEntry':zxEponMaxrttObjectEntry,'maxrtt':maxrtt,'zxEponPriorityQueueMapObjectTable':zxEponPriorityQueueMapObjectTable,'zxEponPriorityQueueMapObjectEntry':zxEponPriorityQueueMapObjectEntry,'downstreampri0Que':downstreampri0Que,'downstreampri1Que':downstreampri1Que,'downstreampri2Que':downstreampri2Que,'downstreampri3Que':downstreampri3Que,'downstreampri4Que':downstreampri4Que,'downstreampri5Que':downstreampri5Que,'downstreampri6Que':downstreampri6Que,'downstreampri7Que':downstreampri7Que,'upstreampri0Que':upstreampri0Que,'upstreampri1Que':upstreampri1Que,'upstreampri2Que':upstreampri2Que,'upstreampri3Que':upstreampri3Que,'upstreampri4Que':upstreampri4Que,'upstreampri5Que':upstreampri5Que,'upstreampri6Que':upstreampri6Que,'upstreampri7Que':upstreampri7Que,'zxEponRxHecObjectTable':zxEponRxHecObjectTable,'zxEponRxHecObjectEntry':zxEponRxHecObjectEntry,'rxhec':rxhec,'zxEponOnuAutoCfgObjectTable':zxEponOnuAutoCfgObjectTable,'zxEponOnuAutoCfgObjectEntry':zxEponOnuAutoCfgObjectEntry,'onuBindStatus':onuBindStatus,'onuAutoCfgStatus':onuAutoCfgStatus,'zxEponIpPoolObjectTable':zxEponIpPoolObjectTable,'zxEponIpPoolObjectEntry':zxEponIpPoolObjectEntry,_a:zxEponIpPoolName,'zxEponIpPoolIpBegin':zxEponIpPoolIpBegin,'zxEponIpPoolIpEnd':zxEponIpPoolIpEnd,'zxEponIpPoolMask':zxEponIpPoolMask,'zxEponIpPoolpriority':zxEponIpPoolpriority,'zxEponIpPoolVlan':zxEponIpPoolVlan,'zxEponIpPoolNetIp':zxEponIpPoolNetIp,'zxEponIpPoolNetMask':zxEponIpPoolNetMask,'zxEponIpPoolGateway':zxEponIpPoolGateway,'zxEponIpPoolRowStatus':zxEponIpPoolRowStatus,'zxEponRunIpObjectTable':zxEponRunIpObjectTable,'zxEponRunIpObjectEntry':zxEponRunIpObjectEntry,_b:zxEponRunIp,'zxEponRunMask':zxEponRunMask,'zxEponRunOnuIfIndex':zxEponRunOnuIfIndex,'zxEponRunIpPriority':zxEponRunIpPriority,'zxEponRunIpVlan':zxEponRunIpVlan,'zxEponRunIpNetIp':zxEponRunIpNetIp,'zxEponRunIpNetMask':zxEponRunIpNetMask,'zxEponRunIpGateway':zxEponRunIpGateway,'zxEponRunIpStatus':zxEponRunIpStatus,'zxEponRunIpCfgMode':zxEponRunIpCfgMode,'zxEponIpPoolConjPonObjectTable':zxEponIpPoolConjPonObjectTable,'zxEponIpPoolConjPonObjectEntry':zxEponIpPoolConjPonObjectEntry,'zxEponIpPoolConjPonName':zxEponIpPoolConjPonName,'zxEponIpPoolConjRowStatus':zxEponIpPoolConjRowStatus,'zxEponBwProfileAdmin':zxEponBwProfileAdmin,'zxEponBwProfileTable':zxEponBwProfileTable,'zxEponBwProfileEntry':zxEponBwProfileEntry,_c:profileIndex,'profileName':profileName,'upBwProfileFixedBw':upBwProfileFixedBw,'upBwProfileAssuredBw':upBwProfileAssuredBw,'upBwProfileMaximumBw':upBwProfileMaximumBw,'upBwProfileMaxBurstSize':upBwProfileMaxBurstSize,'upBwProfilePri':upBwProfilePri,'upBwProfileFixedPacketSize':upBwProfileFixedPacketSize,'downBwProfileMaximumBw':downBwProfileMaximumBw,'downBwProfileMaxBurstSize':downBwProfileMaxBurstSize,'bwProfileRowStatus':bwProfileRowStatus,'bwProfileNextIndex':bwProfileNextIndex,'zxEponOnuBwCfgTable':zxEponOnuBwCfgTable,'zxEponOnuBwCfgEntry':zxEponOnuBwCfgEntry,'onuCfgBwProfileIndex':onuCfgBwProfileIndex,'zxEponOnuIpCfgTable':zxEponOnuIpCfgTable,'zxEponOnuIpCfgEntry':zxEponOnuIpCfgEntry,'zxEponOnuIpCfgIpAddr':zxEponOnuIpCfgIpAddr,'zxEponOnuIpCfgOperator':zxEponOnuIpCfgOperator,'zxEponOnuAutoConfigTable':zxEponOnuAutoConfigTable,'zxEponOnuAutoConfigEntry':zxEponOnuAutoConfigEntry,'zxEponOnuAutoConfigStatus':zxEponOnuAutoConfigStatus,'zxEponOnuVoipAutoConfigStatus':zxEponOnuVoipAutoConfigStatus,'zxEponRunningCtrl':zxEponRunningCtrl,'zxEponRevision':zxEponRevision,'onuCustomObjectTable':onuCustomObjectTable,'onuCustomObjectEntry':onuCustomObjectEntry,'onuOnlineForwardAction':onuOnlineForwardAction,'zxAnEponOnuVportMgmtTable':zxAnEponOnuVportMgmtTable,'zxAnEponOnuVportMgmtTableEntry':zxAnEponOnuVportMgmtTableEntry,'zxAnEponOnuVportMacAddress':zxAnEponOnuVportMacAddress,'zxAnEponOnuVportCurrAuthState':zxAnEponOnuVportCurrAuthState,'zxEponQueueBufferObjectTable':zxEponQueueBufferObjectTable,'zxEponQueueBufferObjectEntry':zxEponQueueBufferObjectEntry,_d:zxEponQueueRackNo,_e:zxEponQueueShelfNo,_f:zxEponQueueSlotNo,'zxEponQueueBufferSize':zxEponQueueBufferSize,'zxEponMgmtIndex':zxEponMgmtIndex,'zxEponIfIndexTable':zxEponIfIndexTable,'zxEponIfIndexEntry':zxEponIfIndexEntry,'zxEponifIndex':zxEponifIndex,'zxEponEntryStatus':zxEponEntryStatus})