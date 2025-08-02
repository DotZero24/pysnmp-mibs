_g='zxAnRuSwUpdateStatusModifyTime'
_f='zxAnRuSwUpdateStatusLastVersion'
_e='zxAnRuSwUpdateStatusCurrVersion'
_d='zxAnRuSwUpdateStatusTaskName'
_c='zxAnRuSwUpdateStatusSource'
_b='zxAnRuSwUpdateStatusFailReason'
_a='zxAnRuSwUpdateStatusResult'
_Z='zxAnRuSwUpdateStatusFileName'
_Y='zxAnRuSwUpdateStatusEquipType'
_X='zxAnRuSwUpdateStatusServiceType'
_W='zxAnRuSwImageIndex'
_V='offline'
_U='remote'
_T='updateAndCommit'
_S='updateLinkup'
_R='updateAndReboot'
_Q='update'
_P='zxAnRuSwOnu'
_O='zxAnRuSwPort'
_N='zxAnRuSwSlot'
_M='zxAnRuSwShelf'
_L='zxAnRuSwRack'
_K='zxAnRuSwUpdatingTaskName'
_J='Bits'
_I='OctetString'
_H='read-write'
_G='not-accessible'
_F='read-create'
_E='Integer32'
_D='read-only'
_C='DisplayString'
_B='ZTE-AN-REMOTE-UNIT-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention','TruthValue')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnRemoteUnitMgmtMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,80))
_ZxAnRemoteUnitSoftware_ObjectIdentity=ObjectIdentity
zxAnRemoteUnitSoftware=_ZxAnRemoteUnitSoftware_ObjectIdentity((1,3,6,1,4,1,3902,1015,80,1))
_ZxAnRuSwGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnRuSwGlobalObjects=_ZxAnRuSwGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,80,1,1))
_ZxAnRuSwFtpServerObjects_ObjectIdentity=ObjectIdentity
zxAnRuSwFtpServerObjects=_ZxAnRuSwFtpServerObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,80,1,1,1))
class _ZxAnRuSwFtpServerProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ftp',1),('sftp',2)))
_ZxAnRuSwFtpServerProtocolType_Type.__name__=_E
_ZxAnRuSwFtpServerProtocolType_Object=MibScalar
zxAnRuSwFtpServerProtocolType=_ZxAnRuSwFtpServerProtocolType_Object((1,3,6,1,4,1,3902,1015,80,1,1,1,1),_ZxAnRuSwFtpServerProtocolType_Type())
zxAnRuSwFtpServerProtocolType.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwFtpServerProtocolType.setStatus(_A)
_ZxAnRuSwFtpServerIpAddrType_Type=InetAddressType
_ZxAnRuSwFtpServerIpAddrType_Object=MibScalar
zxAnRuSwFtpServerIpAddrType=_ZxAnRuSwFtpServerIpAddrType_Object((1,3,6,1,4,1,3902,1015,80,1,1,1,2),_ZxAnRuSwFtpServerIpAddrType_Type())
zxAnRuSwFtpServerIpAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwFtpServerIpAddrType.setStatus(_A)
_ZxAnRuSwFtpServerIpAddr_Type=InetAddress
_ZxAnRuSwFtpServerIpAddr_Object=MibScalar
zxAnRuSwFtpServerIpAddr=_ZxAnRuSwFtpServerIpAddr_Object((1,3,6,1,4,1,3902,1015,80,1,1,1,3),_ZxAnRuSwFtpServerIpAddr_Type())
zxAnRuSwFtpServerIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwFtpServerIpAddr.setStatus(_A)
class _ZxAnRuSwFtpServerUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnRuSwFtpServerUserName_Type.__name__=_C
_ZxAnRuSwFtpServerUserName_Object=MibScalar
zxAnRuSwFtpServerUserName=_ZxAnRuSwFtpServerUserName_Object((1,3,6,1,4,1,3902,1015,80,1,1,1,4),_ZxAnRuSwFtpServerUserName_Type())
zxAnRuSwFtpServerUserName.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwFtpServerUserName.setStatus(_A)
class _ZxAnRuSwFtpServerUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnRuSwFtpServerUserPassword_Type.__name__=_C
_ZxAnRuSwFtpServerUserPassword_Object=MibScalar
zxAnRuSwFtpServerUserPassword=_ZxAnRuSwFtpServerUserPassword_Object((1,3,6,1,4,1,3902,1015,80,1,1,1,5),_ZxAnRuSwFtpServerUserPassword_Type())
zxAnRuSwFtpServerUserPassword.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwFtpServerUserPassword.setStatus(_A)
class _ZxAnRuCapabilities_Type(Bits):namedValues=NamedValues(('parallelLmtEnable',0))
_ZxAnRuCapabilities_Type.__name__=_J
_ZxAnRuCapabilities_Object=MibScalar
zxAnRuCapabilities=_ZxAnRuCapabilities_Object((1,3,6,1,4,1,3902,1015,80,1,1,100),_ZxAnRuCapabilities_Type())
zxAnRuCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuCapabilities.setStatus(_A)
_ZxAnRuSwObjects_ObjectIdentity=ObjectIdentity
zxAnRuSwObjects=_ZxAnRuSwObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,80,1,2))
_ZxAnRuSwManualUpdateObjects_ObjectIdentity=ObjectIdentity
zxAnRuSwManualUpdateObjects=_ZxAnRuSwManualUpdateObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,80,1,2,1))
class _ZxAnRuSwManualUpdateList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_ZxAnRuSwManualUpdateList_Type.__name__=_I
_ZxAnRuSwManualUpdateList_Object=MibScalar
zxAnRuSwManualUpdateList=_ZxAnRuSwManualUpdateList_Object((1,3,6,1,4,1,3902,1015,80,1,2,1,1),_ZxAnRuSwManualUpdateList_Type())
zxAnRuSwManualUpdateList.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwManualUpdateList.setStatus(_A)
class _ZxAnRuSwManualUpdateAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Q,1),(_R,2),('activate',3),('commit',4),('abort',5),(_S,6),(_T,7)))
_ZxAnRuSwManualUpdateAction_Type.__name__=_E
_ZxAnRuSwManualUpdateAction_Object=MibScalar
zxAnRuSwManualUpdateAction=_ZxAnRuSwManualUpdateAction_Object((1,3,6,1,4,1,3902,1015,80,1,2,1,6),_ZxAnRuSwManualUpdateAction_Type())
zxAnRuSwManualUpdateAction.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwManualUpdateAction.setStatus(_A)
class _ZxAnRuSwManualUpdateFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnRuSwManualUpdateFileName_Type.__name__=_C
_ZxAnRuSwManualUpdateFileName_Object=MibScalar
zxAnRuSwManualUpdateFileName=_ZxAnRuSwManualUpdateFileName_Object((1,3,6,1,4,1,3902,1015,80,1,2,1,7),_ZxAnRuSwManualUpdateFileName_Type())
zxAnRuSwManualUpdateFileName.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwManualUpdateFileName.setStatus(_A)
class _ZxAnRuSwManualUpdateLocate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),(_U,2)))
_ZxAnRuSwManualUpdateLocate_Type.__name__=_E
_ZxAnRuSwManualUpdateLocate_Object=MibScalar
zxAnRuSwManualUpdateLocate=_ZxAnRuSwManualUpdateLocate_Object((1,3,6,1,4,1,3902,1015,80,1,2,1,8),_ZxAnRuSwManualUpdateLocate_Type())
zxAnRuSwManualUpdateLocate.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnRuSwManualUpdateLocate.setStatus(_A)
_ZxAnRuSwUpdatingTaskTable_Object=MibTable
zxAnRuSwUpdatingTaskTable=_ZxAnRuSwUpdatingTaskTable_Object((1,3,6,1,4,1,3902,1015,80,1,2,2))
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskTable.setStatus(_A)
_ZxAnRuSwUpdatingTaskEntry_Object=MibTableRow
zxAnRuSwUpdatingTaskEntry=_ZxAnRuSwUpdatingTaskEntry_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1))
zxAnRuSwUpdatingTaskEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskEntry.setStatus(_A)
class _ZxAnRuSwUpdatingTaskName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnRuSwUpdatingTaskName_Type.__name__=_C
_ZxAnRuSwUpdatingTaskName_Object=MibTableColumn
zxAnRuSwUpdatingTaskName=_ZxAnRuSwUpdatingTaskName_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,1),_ZxAnRuSwUpdatingTaskName_Type())
zxAnRuSwUpdatingTaskName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskName.setStatus(_A)
class _ZxAnRuSwUpdatingTaskDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZxAnRuSwUpdatingTaskDesc_Type.__name__=_C
_ZxAnRuSwUpdatingTaskDesc_Object=MibTableColumn
zxAnRuSwUpdatingTaskDesc=_ZxAnRuSwUpdatingTaskDesc_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,2),_ZxAnRuSwUpdatingTaskDesc_Type())
zxAnRuSwUpdatingTaskDesc.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskDesc.setStatus(_A)
class _ZxAnRuSwUpdatingTaskMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('online',1),(_V,2),('both',3)))
_ZxAnRuSwUpdatingTaskMode_Type.__name__=_E
_ZxAnRuSwUpdatingTaskMode_Object=MibTableColumn
zxAnRuSwUpdatingTaskMode=_ZxAnRuSwUpdatingTaskMode_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,3),_ZxAnRuSwUpdatingTaskMode_Type())
zxAnRuSwUpdatingTaskMode.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskMode.setStatus(_A)
class _ZxAnRuSwUpdatingTaskServiceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_ZxAnRuSwUpdatingTaskServiceType_Type.__name__=_C
_ZxAnRuSwUpdatingTaskServiceType_Object=MibTableColumn
zxAnRuSwUpdatingTaskServiceType=_ZxAnRuSwUpdatingTaskServiceType_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,4),_ZxAnRuSwUpdatingTaskServiceType_Type())
zxAnRuSwUpdatingTaskServiceType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskServiceType.setStatus(_A)
class _ZxAnRuSwUpdatingTaskVendor_Type(DisplayString):defaultValue=OctetString('zte');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnRuSwUpdatingTaskVendor_Type.__name__=_C
_ZxAnRuSwUpdatingTaskVendor_Object=MibTableColumn
zxAnRuSwUpdatingTaskVendor=_ZxAnRuSwUpdatingTaskVendor_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,5),_ZxAnRuSwUpdatingTaskVendor_Type())
zxAnRuSwUpdatingTaskVendor.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskVendor.setStatus(_A)
class _ZxAnRuSwUpdatingTaskEquipType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnRuSwUpdatingTaskEquipType_Type.__name__=_C
_ZxAnRuSwUpdatingTaskEquipType_Object=MibTableColumn
zxAnRuSwUpdatingTaskEquipType=_ZxAnRuSwUpdatingTaskEquipType_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,6),_ZxAnRuSwUpdatingTaskEquipType_Type())
zxAnRuSwUpdatingTaskEquipType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskEquipType.setStatus(_A)
class _ZxAnRuSwUpdatingTaskCrtrnType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ignore',1),('equal',2),('notEqual',3),('below',4),('upper',5)))
_ZxAnRuSwUpdatingTaskCrtrnType_Type.__name__=_E
_ZxAnRuSwUpdatingTaskCrtrnType_Object=MibTableColumn
zxAnRuSwUpdatingTaskCrtrnType=_ZxAnRuSwUpdatingTaskCrtrnType_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,7),_ZxAnRuSwUpdatingTaskCrtrnType_Type())
zxAnRuSwUpdatingTaskCrtrnType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskCrtrnType.setStatus(_A)
class _ZxAnRuSwUpdatingTaskCrtrnVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnRuSwUpdatingTaskCrtrnVer_Type.__name__=_C
_ZxAnRuSwUpdatingTaskCrtrnVer_Object=MibTableColumn
zxAnRuSwUpdatingTaskCrtrnVer=_ZxAnRuSwUpdatingTaskCrtrnVer_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,8),_ZxAnRuSwUpdatingTaskCrtrnVer_Type())
zxAnRuSwUpdatingTaskCrtrnVer.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskCrtrnVer.setStatus(_A)
class _ZxAnRuSwUpdatingTaskOperObjType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ne',1),('port',2)))
_ZxAnRuSwUpdatingTaskOperObjType_Type.__name__=_E
_ZxAnRuSwUpdatingTaskOperObjType_Object=MibTableColumn
zxAnRuSwUpdatingTaskOperObjType=_ZxAnRuSwUpdatingTaskOperObjType_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,9),_ZxAnRuSwUpdatingTaskOperObjType_Type())
zxAnRuSwUpdatingTaskOperObjType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskOperObjType.setStatus(_A)
class _ZxAnRuSwUpdatingTaskOperObjList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_ZxAnRuSwUpdatingTaskOperObjList_Type.__name__=_I
_ZxAnRuSwUpdatingTaskOperObjList_Object=MibTableColumn
zxAnRuSwUpdatingTaskOperObjList=_ZxAnRuSwUpdatingTaskOperObjList_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,10),_ZxAnRuSwUpdatingTaskOperObjList_Type())
zxAnRuSwUpdatingTaskOperObjList.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskOperObjList.setStatus(_A)
class _ZxAnRuSwUpdatingTaskAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('abort',1),('restart',2)))
_ZxAnRuSwUpdatingTaskAction_Type.__name__=_E
_ZxAnRuSwUpdatingTaskAction_Object=MibTableColumn
zxAnRuSwUpdatingTaskAction=_ZxAnRuSwUpdatingTaskAction_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,11),_ZxAnRuSwUpdatingTaskAction_Type())
zxAnRuSwUpdatingTaskAction.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskAction.setStatus(_A)
class _ZxAnRuSwUpdatingTaskFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnRuSwUpdatingTaskFileName_Type.__name__=_C
_ZxAnRuSwUpdatingTaskFileName_Object=MibTableColumn
zxAnRuSwUpdatingTaskFileName=_ZxAnRuSwUpdatingTaskFileName_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,12),_ZxAnRuSwUpdatingTaskFileName_Type())
zxAnRuSwUpdatingTaskFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskFileName.setStatus(_A)
class _ZxAnRuSwUpdatingTaskFileLocate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),(_U,2)))
_ZxAnRuSwUpdatingTaskFileLocate_Type.__name__=_E
_ZxAnRuSwUpdatingTaskFileLocate_Object=MibTableColumn
zxAnRuSwUpdatingTaskFileLocate=_ZxAnRuSwUpdatingTaskFileLocate_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,13),_ZxAnRuSwUpdatingTaskFileLocate_Type())
zxAnRuSwUpdatingTaskFileLocate.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskFileLocate.setStatus(_A)
class _ZxAnRuSwUpdatingTaskStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('processing',1),('aborted',2),('finished',3)))
_ZxAnRuSwUpdatingTaskStatus_Type.__name__=_E
_ZxAnRuSwUpdatingTaskStatus_Object=MibTableColumn
zxAnRuSwUpdatingTaskStatus=_ZxAnRuSwUpdatingTaskStatus_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,14),_ZxAnRuSwUpdatingTaskStatus_Type())
zxAnRuSwUpdatingTaskStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskStatus.setStatus(_A)
class _ZxAnRuSwUpdatingTaskRuAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_R,2),('reboot',3),(_S,4),(_T,5)))
_ZxAnRuSwUpdatingTaskRuAction_Type.__name__=_E
_ZxAnRuSwUpdatingTaskRuAction_Object=MibTableColumn
zxAnRuSwUpdatingTaskRuAction=_ZxAnRuSwUpdatingTaskRuAction_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,15),_ZxAnRuSwUpdatingTaskRuAction_Type())
zxAnRuSwUpdatingTaskRuAction.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskRuAction.setStatus(_A)
class _ZxAnRuSwUpdatingTaskParallelLmt_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_ZxAnRuSwUpdatingTaskParallelLmt_Type.__name__=_E
_ZxAnRuSwUpdatingTaskParallelLmt_Object=MibTableColumn
zxAnRuSwUpdatingTaskParallelLmt=_ZxAnRuSwUpdatingTaskParallelLmt_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,16),_ZxAnRuSwUpdatingTaskParallelLmt_Type())
zxAnRuSwUpdatingTaskParallelLmt.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskParallelLmt.setStatus(_A)
_ZxAnRuSwUpdatingTaskRowStatus_Type=RowStatus
_ZxAnRuSwUpdatingTaskRowStatus_Object=MibTableColumn
zxAnRuSwUpdatingTaskRowStatus=_ZxAnRuSwUpdatingTaskRowStatus_Object((1,3,6,1,4,1,3902,1015,80,1,2,2,1,30),_ZxAnRuSwUpdatingTaskRowStatus_Type())
zxAnRuSwUpdatingTaskRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnRuSwUpdatingTaskRowStatus.setStatus(_A)
_ZxAnRuSwTaskStatTable_Object=MibTable
zxAnRuSwTaskStatTable=_ZxAnRuSwTaskStatTable_Object((1,3,6,1,4,1,3902,1015,80,1,2,3))
if mibBuilder.loadTexts:zxAnRuSwTaskStatTable.setStatus(_A)
_ZxAnRuSwTaskStatEntry_Object=MibTableRow
zxAnRuSwTaskStatEntry=_ZxAnRuSwTaskStatEntry_Object((1,3,6,1,4,1,3902,1015,80,1,2,3,1))
zxAnRuSwTaskStatEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:zxAnRuSwTaskStatEntry.setStatus(_A)
_ZxAnRuSwTaskStatsSuccesses_Type=Integer32
_ZxAnRuSwTaskStatsSuccesses_Object=MibTableColumn
zxAnRuSwTaskStatsSuccesses=_ZxAnRuSwTaskStatsSuccesses_Object((1,3,6,1,4,1,3902,1015,80,1,2,3,1,1),_ZxAnRuSwTaskStatsSuccesses_Type())
zxAnRuSwTaskStatsSuccesses.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwTaskStatsSuccesses.setStatus(_A)
_ZxAnRuSwTaskStatsFailures_Type=Integer32
_ZxAnRuSwTaskStatsFailures_Object=MibTableColumn
zxAnRuSwTaskStatsFailures=_ZxAnRuSwTaskStatsFailures_Object((1,3,6,1,4,1,3902,1015,80,1,2,3,1,2),_ZxAnRuSwTaskStatsFailures_Type())
zxAnRuSwTaskStatsFailures.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwTaskStatsFailures.setStatus(_A)
_ZxAnRuSwTaskStatsUpdatings_Type=Integer32
_ZxAnRuSwTaskStatsUpdatings_Object=MibTableColumn
zxAnRuSwTaskStatsUpdatings=_ZxAnRuSwTaskStatsUpdatings_Object((1,3,6,1,4,1,3902,1015,80,1,2,3,1,3),_ZxAnRuSwTaskStatsUpdatings_Type())
zxAnRuSwTaskStatsUpdatings.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwTaskStatsUpdatings.setStatus(_A)
_ZxAnRuSwTaskStatsWaitings_Type=Integer32
_ZxAnRuSwTaskStatsWaitings_Object=MibTableColumn
zxAnRuSwTaskStatsWaitings=_ZxAnRuSwTaskStatsWaitings_Object((1,3,6,1,4,1,3902,1015,80,1,2,3,1,4),_ZxAnRuSwTaskStatsWaitings_Type())
zxAnRuSwTaskStatsWaitings.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwTaskStatsWaitings.setStatus(_A)
_ZxAnRuSwUpdateStatusTable_Object=MibTable
zxAnRuSwUpdateStatusTable=_ZxAnRuSwUpdateStatusTable_Object((1,3,6,1,4,1,3902,1015,80,1,2,4))
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusTable.setStatus(_A)
_ZxAnRuSwUpdateStatusEntry_Object=MibTableRow
zxAnRuSwUpdateStatusEntry=_ZxAnRuSwUpdateStatusEntry_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1))
zxAnRuSwUpdateStatusEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusEntry.setStatus(_A)
_ZxAnRuSwRack_Type=Integer32
_ZxAnRuSwRack_Object=MibTableColumn
zxAnRuSwRack=_ZxAnRuSwRack_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,1),_ZxAnRuSwRack_Type())
zxAnRuSwRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwRack.setStatus(_A)
_ZxAnRuSwShelf_Type=Integer32
_ZxAnRuSwShelf_Object=MibTableColumn
zxAnRuSwShelf=_ZxAnRuSwShelf_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,2),_ZxAnRuSwShelf_Type())
zxAnRuSwShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwShelf.setStatus(_A)
_ZxAnRuSwSlot_Type=Integer32
_ZxAnRuSwSlot_Object=MibTableColumn
zxAnRuSwSlot=_ZxAnRuSwSlot_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,3),_ZxAnRuSwSlot_Type())
zxAnRuSwSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwSlot.setStatus(_A)
_ZxAnRuSwPort_Type=Integer32
_ZxAnRuSwPort_Object=MibTableColumn
zxAnRuSwPort=_ZxAnRuSwPort_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,4),_ZxAnRuSwPort_Type())
zxAnRuSwPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwPort.setStatus(_A)
_ZxAnRuSwOnu_Type=Integer32
_ZxAnRuSwOnu_Object=MibTableColumn
zxAnRuSwOnu=_ZxAnRuSwOnu_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,5),_ZxAnRuSwOnu_Type())
zxAnRuSwOnu.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwOnu.setStatus(_A)
class _ZxAnRuSwUpdateStatusServiceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_ZxAnRuSwUpdateStatusServiceType_Type.__name__=_C
_ZxAnRuSwUpdateStatusServiceType_Object=MibTableColumn
zxAnRuSwUpdateStatusServiceType=_ZxAnRuSwUpdateStatusServiceType_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,6),_ZxAnRuSwUpdateStatusServiceType_Type())
zxAnRuSwUpdateStatusServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusServiceType.setStatus(_A)
class _ZxAnRuSwUpdateStatusEquipType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnRuSwUpdateStatusEquipType_Type.__name__=_C
_ZxAnRuSwUpdateStatusEquipType_Object=MibTableColumn
zxAnRuSwUpdateStatusEquipType=_ZxAnRuSwUpdateStatusEquipType_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,7),_ZxAnRuSwUpdateStatusEquipType_Type())
zxAnRuSwUpdateStatusEquipType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusEquipType.setStatus(_A)
class _ZxAnRuSwUpdateStatusFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
_ZxAnRuSwUpdateStatusFileName_Type.__name__=_C
_ZxAnRuSwUpdateStatusFileName_Object=MibTableColumn
zxAnRuSwUpdateStatusFileName=_ZxAnRuSwUpdateStatusFileName_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,8),_ZxAnRuSwUpdateStatusFileName_Type())
zxAnRuSwUpdateStatusFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusFileName.setStatus(_A)
class _ZxAnRuSwUpdateStatusResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('success',3),('failure',4),('waiting',5)))
_ZxAnRuSwUpdateStatusResult_Type.__name__=_E
_ZxAnRuSwUpdateStatusResult_Object=MibTableColumn
zxAnRuSwUpdateStatusResult=_ZxAnRuSwUpdateStatusResult_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,9),_ZxAnRuSwUpdateStatusResult_Type())
zxAnRuSwUpdateStatusResult.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusResult.setStatus(_A)
class _ZxAnRuSwUpdateStatusFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('none',1),('downloadErr',2),('commitErr',3),('activateErr',4),('crcErr',5),('validErr',6),('useAbort',7),(_V,8),('rebootErr',9),('ruDeleted',10),('timeout',11),('notSupport',12)))
_ZxAnRuSwUpdateStatusFailReason_Type.__name__=_E
_ZxAnRuSwUpdateStatusFailReason_Object=MibTableColumn
zxAnRuSwUpdateStatusFailReason=_ZxAnRuSwUpdateStatusFailReason_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,10),_ZxAnRuSwUpdateStatusFailReason_Type())
zxAnRuSwUpdateStatusFailReason.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusFailReason.setStatus(_A)
class _ZxAnRuSwUpdateStatusProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnRuSwUpdateStatusProgress_Type.__name__=_E
_ZxAnRuSwUpdateStatusProgress_Object=MibTableColumn
zxAnRuSwUpdateStatusProgress=_ZxAnRuSwUpdateStatusProgress_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,11),_ZxAnRuSwUpdateStatusProgress_Type())
zxAnRuSwUpdateStatusProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusProgress.setStatus(_A)
class _ZxAnRuSwUpdateStatusSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('task',1),('manual',2)))
_ZxAnRuSwUpdateStatusSource_Type.__name__=_E
_ZxAnRuSwUpdateStatusSource_Object=MibTableColumn
zxAnRuSwUpdateStatusSource=_ZxAnRuSwUpdateStatusSource_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,12),_ZxAnRuSwUpdateStatusSource_Type())
zxAnRuSwUpdateStatusSource.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusSource.setStatus(_A)
class _ZxAnRuSwUpdateStatusTaskName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnRuSwUpdateStatusTaskName_Type.__name__=_C
_ZxAnRuSwUpdateStatusTaskName_Object=MibTableColumn
zxAnRuSwUpdateStatusTaskName=_ZxAnRuSwUpdateStatusTaskName_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,13),_ZxAnRuSwUpdateStatusTaskName_Type())
zxAnRuSwUpdateStatusTaskName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusTaskName.setStatus(_A)
class _ZxAnRuSwUpdateStatusModifyTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_ZxAnRuSwUpdateStatusModifyTime_Type.__name__=_C
_ZxAnRuSwUpdateStatusModifyTime_Object=MibTableColumn
zxAnRuSwUpdateStatusModifyTime=_ZxAnRuSwUpdateStatusModifyTime_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,14),_ZxAnRuSwUpdateStatusModifyTime_Type())
zxAnRuSwUpdateStatusModifyTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusModifyTime.setStatus(_A)
class _ZxAnRuSwUpdateStatusCurrVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
_ZxAnRuSwUpdateStatusCurrVersion_Type.__name__=_C
_ZxAnRuSwUpdateStatusCurrVersion_Object=MibTableColumn
zxAnRuSwUpdateStatusCurrVersion=_ZxAnRuSwUpdateStatusCurrVersion_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,15),_ZxAnRuSwUpdateStatusCurrVersion_Type())
zxAnRuSwUpdateStatusCurrVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusCurrVersion.setStatus(_A)
class _ZxAnRuSwUpdateStatusLastVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
_ZxAnRuSwUpdateStatusLastVersion_Type.__name__=_C
_ZxAnRuSwUpdateStatusLastVersion_Object=MibTableColumn
zxAnRuSwUpdateStatusLastVersion=_ZxAnRuSwUpdateStatusLastVersion_Object((1,3,6,1,4,1,3902,1015,80,1,2,4,1,16),_ZxAnRuSwUpdateStatusLastVersion_Type())
zxAnRuSwUpdateStatusLastVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwUpdateStatusLastVersion.setStatus(_A)
_ZxAnRuSwImageTable_Object=MibTable
zxAnRuSwImageTable=_ZxAnRuSwImageTable_Object((1,3,6,1,4,1,3902,1015,80,1,2,5))
if mibBuilder.loadTexts:zxAnRuSwImageTable.setStatus(_A)
_ZxAnRuSwImageEntry_Object=MibTableRow
zxAnRuSwImageEntry=_ZxAnRuSwImageEntry_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1))
zxAnRuSwImageEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_W))
if mibBuilder.loadTexts:zxAnRuSwImageEntry.setStatus(_A)
_ZxAnRuSwImageRack_Type=Integer32
_ZxAnRuSwImageRack_Object=MibTableColumn
zxAnRuSwImageRack=_ZxAnRuSwImageRack_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1,1),_ZxAnRuSwImageRack_Type())
zxAnRuSwImageRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwImageRack.setStatus(_A)
_ZxAnRuSwImageShelf_Type=Integer32
_ZxAnRuSwImageShelf_Object=MibTableColumn
zxAnRuSwImageShelf=_ZxAnRuSwImageShelf_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1,2),_ZxAnRuSwImageShelf_Type())
zxAnRuSwImageShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwImageShelf.setStatus(_A)
_ZxAnRuSwImageSlot_Type=Integer32
_ZxAnRuSwImageSlot_Object=MibTableColumn
zxAnRuSwImageSlot=_ZxAnRuSwImageSlot_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1,3),_ZxAnRuSwImageSlot_Type())
zxAnRuSwImageSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwImageSlot.setStatus(_A)
_ZxAnRuSwImagePort_Type=Integer32
_ZxAnRuSwImagePort_Object=MibTableColumn
zxAnRuSwImagePort=_ZxAnRuSwImagePort_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1,4),_ZxAnRuSwImagePort_Type())
zxAnRuSwImagePort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwImagePort.setStatus(_A)
_ZxAnRuSwImageOnu_Type=Integer32
_ZxAnRuSwImageOnu_Object=MibTableColumn
zxAnRuSwImageOnu=_ZxAnRuSwImageOnu_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1,5),_ZxAnRuSwImageOnu_Type())
zxAnRuSwImageOnu.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwImageOnu.setStatus(_A)
class _ZxAnRuSwImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnRuSwImageIndex_Type.__name__=_E
_ZxAnRuSwImageIndex_Object=MibTableColumn
zxAnRuSwImageIndex=_ZxAnRuSwImageIndex_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1,6),_ZxAnRuSwImageIndex_Type())
zxAnRuSwImageIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnRuSwImageIndex.setStatus(_A)
class _ZxAnRuSwImageVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
_ZxAnRuSwImageVersion_Type.__name__=_C
_ZxAnRuSwImageVersion_Object=MibTableColumn
zxAnRuSwImageVersion=_ZxAnRuSwImageVersion_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1,7),_ZxAnRuSwImageVersion_Type())
zxAnRuSwImageVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwImageVersion.setStatus(_A)
class _ZxAnRuSwImageStatus_Type(Bits):namedValues=NamedValues(*(('isCommitted',0),('isActive',1),('isValid',2)))
_ZxAnRuSwImageStatus_Type.__name__=_J
_ZxAnRuSwImageStatus_Object=MibTableColumn
zxAnRuSwImageStatus=_ZxAnRuSwImageStatus_Object((1,3,6,1,4,1,3902,1015,80,1,2,5,1,8),_ZxAnRuSwImageStatus_Type())
zxAnRuSwImageStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnRuSwImageStatus.setStatus(_A)
_ZxAnRuSwNotifications_ObjectIdentity=ObjectIdentity
zxAnRuSwNotifications=_ZxAnRuSwNotifications_ObjectIdentity((1,3,6,1,4,1,3902,1015,80,1,20))
zxAnRuSwUpdatedTrap=NotificationType((1,3,6,1,4,1,3902,1015,80,1,20,1))
zxAnRuSwUpdatedTrap.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:zxAnRuSwUpdatedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnRemoteUnitMgmtMib':zxAnRemoteUnitMgmtMib,'zxAnRemoteUnitSoftware':zxAnRemoteUnitSoftware,'zxAnRuSwGlobalObjects':zxAnRuSwGlobalObjects,'zxAnRuSwFtpServerObjects':zxAnRuSwFtpServerObjects,'zxAnRuSwFtpServerProtocolType':zxAnRuSwFtpServerProtocolType,'zxAnRuSwFtpServerIpAddrType':zxAnRuSwFtpServerIpAddrType,'zxAnRuSwFtpServerIpAddr':zxAnRuSwFtpServerIpAddr,'zxAnRuSwFtpServerUserName':zxAnRuSwFtpServerUserName,'zxAnRuSwFtpServerUserPassword':zxAnRuSwFtpServerUserPassword,'zxAnRuCapabilities':zxAnRuCapabilities,'zxAnRuSwObjects':zxAnRuSwObjects,'zxAnRuSwManualUpdateObjects':zxAnRuSwManualUpdateObjects,'zxAnRuSwManualUpdateList':zxAnRuSwManualUpdateList,'zxAnRuSwManualUpdateAction':zxAnRuSwManualUpdateAction,'zxAnRuSwManualUpdateFileName':zxAnRuSwManualUpdateFileName,'zxAnRuSwManualUpdateLocate':zxAnRuSwManualUpdateLocate,'zxAnRuSwUpdatingTaskTable':zxAnRuSwUpdatingTaskTable,'zxAnRuSwUpdatingTaskEntry':zxAnRuSwUpdatingTaskEntry,_K:zxAnRuSwUpdatingTaskName,'zxAnRuSwUpdatingTaskDesc':zxAnRuSwUpdatingTaskDesc,'zxAnRuSwUpdatingTaskMode':zxAnRuSwUpdatingTaskMode,'zxAnRuSwUpdatingTaskServiceType':zxAnRuSwUpdatingTaskServiceType,'zxAnRuSwUpdatingTaskVendor':zxAnRuSwUpdatingTaskVendor,'zxAnRuSwUpdatingTaskEquipType':zxAnRuSwUpdatingTaskEquipType,'zxAnRuSwUpdatingTaskCrtrnType':zxAnRuSwUpdatingTaskCrtrnType,'zxAnRuSwUpdatingTaskCrtrnVer':zxAnRuSwUpdatingTaskCrtrnVer,'zxAnRuSwUpdatingTaskOperObjType':zxAnRuSwUpdatingTaskOperObjType,'zxAnRuSwUpdatingTaskOperObjList':zxAnRuSwUpdatingTaskOperObjList,'zxAnRuSwUpdatingTaskAction':zxAnRuSwUpdatingTaskAction,'zxAnRuSwUpdatingTaskFileName':zxAnRuSwUpdatingTaskFileName,'zxAnRuSwUpdatingTaskFileLocate':zxAnRuSwUpdatingTaskFileLocate,'zxAnRuSwUpdatingTaskStatus':zxAnRuSwUpdatingTaskStatus,'zxAnRuSwUpdatingTaskRuAction':zxAnRuSwUpdatingTaskRuAction,'zxAnRuSwUpdatingTaskParallelLmt':zxAnRuSwUpdatingTaskParallelLmt,'zxAnRuSwUpdatingTaskRowStatus':zxAnRuSwUpdatingTaskRowStatus,'zxAnRuSwTaskStatTable':zxAnRuSwTaskStatTable,'zxAnRuSwTaskStatEntry':zxAnRuSwTaskStatEntry,'zxAnRuSwTaskStatsSuccesses':zxAnRuSwTaskStatsSuccesses,'zxAnRuSwTaskStatsFailures':zxAnRuSwTaskStatsFailures,'zxAnRuSwTaskStatsUpdatings':zxAnRuSwTaskStatsUpdatings,'zxAnRuSwTaskStatsWaitings':zxAnRuSwTaskStatsWaitings,'zxAnRuSwUpdateStatusTable':zxAnRuSwUpdateStatusTable,'zxAnRuSwUpdateStatusEntry':zxAnRuSwUpdateStatusEntry,_L:zxAnRuSwRack,_M:zxAnRuSwShelf,_N:zxAnRuSwSlot,_O:zxAnRuSwPort,_P:zxAnRuSwOnu,_X:zxAnRuSwUpdateStatusServiceType,_Y:zxAnRuSwUpdateStatusEquipType,_Z:zxAnRuSwUpdateStatusFileName,_a:zxAnRuSwUpdateStatusResult,_b:zxAnRuSwUpdateStatusFailReason,'zxAnRuSwUpdateStatusProgress':zxAnRuSwUpdateStatusProgress,_c:zxAnRuSwUpdateStatusSource,_d:zxAnRuSwUpdateStatusTaskName,_g:zxAnRuSwUpdateStatusModifyTime,_e:zxAnRuSwUpdateStatusCurrVersion,_f:zxAnRuSwUpdateStatusLastVersion,'zxAnRuSwImageTable':zxAnRuSwImageTable,'zxAnRuSwImageEntry':zxAnRuSwImageEntry,'zxAnRuSwImageRack':zxAnRuSwImageRack,'zxAnRuSwImageShelf':zxAnRuSwImageShelf,'zxAnRuSwImageSlot':zxAnRuSwImageSlot,'zxAnRuSwImagePort':zxAnRuSwImagePort,'zxAnRuSwImageOnu':zxAnRuSwImageOnu,_W:zxAnRuSwImageIndex,'zxAnRuSwImageVersion':zxAnRuSwImageVersion,'zxAnRuSwImageStatus':zxAnRuSwImageStatus,'zxAnRuSwNotifications':zxAnRuSwNotifications,'zxAnRuSwUpdatedTrap':zxAnRuSwUpdatedTrap})