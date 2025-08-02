_AF='fmlObsoleteTrapsComplianceGroup'
_AE='fmlTrapsComplianceGroup'
_AD='fmlHAModeConformanceGroup'
_AC='fmlHwSensorsConformanceGroup'
_AB='fmlMailOptionsConformanceGroup'
_AA='fmlIpConformanceGroup'
_A9='fmlSysOptionsConformanceGroup'
_A8='fmlSystemConformanceGroup'
_A7='fmlTrapIpChange'
_A6='fmlTrapPSUFailureEvent'
_A5='fmlTrapLogDiskHighThreshold'
_A4='fmlTrapMemLowThreshold'
_A3='fmlTrapCpuHighThreshold'
_A2='fmlTrapHAEvent'
_A1='fmlTrapRAIDEvent'
_A0='fmlTrapSystemEvent'
_z='fmlTrapSpamThresholdEvent'
_y='fmlTrapAvThresholdEvent'
_x='fmlTrapMailDeferredQueueHighThreshold'
_w='fmlTrapMailDiskHighThreshold'
_v='fmlRemoteStorageStatus'
_u='fmlHAEffectiveMode'
_t='fmlHAMode'
_s='fmlHwSensorCount'
_r='fmlMailQueueMailSize'
_q='fmlMailQueueMailCount'
_p='fmlMailQueueName'
_o='fmlIpSessExp'
_n='fmlIpSessToPort'
_m='fmlIpSessToAddr'
_l='fmlIpSessFromPort'
_k='fmlIpSessFromAddr'
_j='fmlIpSessProto'
_i='fmlSysOptAuthTimeout'
_h='fmlSysOptIdleTimeout'
_g='fmlSysLoad'
_f='fmlSysSesCount'
_e='fmlSysMailDiskUsage'
_d='fmlSysLogDiskUsage'
_c='fmlSysMemUsage'
_b='fmlSysCpuUsage'
_a='fmlSysOpMode'
_Z='fmlSysVersionAv'
_Y='fmlSysVersion'
_X='fmlSysModel'
_W='fmlHwSensorEntIndex'
_V='fmlMailQueueIndex'
_U='not-accessible'
_T='fmlIpSessIndex'
_S='ifIndex'
_R='IF-MIB'
_Q='fmlHwSensorEntAlarmStatus'
_P='fmlHwSensorEntValue'
_O='fmlHwSensorEntName'
_N='fmlHAEventReason'
_M='fmlHAUnitIp'
_L='fmlHAEventId'
_K='fmlRAIDDevName'
_J='fmlRAIDCode'
_I='fmlSysEventCode'
_H='Integer32'
_G='accessible-for-notify'
_F='DisplayString'
_E='obsolete'
_D='fmlSysSerial'
_C='read-only'
_B='current'
_A='FORTINET-FORTIMAIL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FnBoolState,FnIndex,FnSessionProto,fortinet=mibBuilder.importSymbols('FORTINET-CORE-MIB','FnBoolState','FnIndex','FnSessionProto','fortinet')
ifIndex,=mibBuilder.importSymbols(_R,_S)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
fnFortiMailMib=ModuleIdentity((1,3,6,1,4,1,12356,105))
if mibBuilder.loadTexts:fnFortiMailMib.setRevisions(('2013-06-28 00:00','2010-03-23 00:00','2009-10-22 00:00'))
class FmlIpv6Address(TextualConvention,OctetString):status=_B;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
class FmlOpMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('gateway',1),('transparent',2),('server',3)))
class FmlSysEventCodeVal(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('systemHalt',1),('systemReboot',2),('systemReload',3),('systemUpgrade',4),('guiUpgrade',5),('logdiskFormat',6),('maildiskFormat',7),('avDBUpdateSuccess',8),('avDBUpdateNetworkError',9),('avDBUpdateFailure',10)))
class FmlRAIDCodeVal(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('degradedArray',1),('sparesMissing',2),('rebuildStarted',3),('rebuildFinished',4),('fail',5),('failSpare',6),('spareActive',7)))
class FmlHAEventIdVal(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('masterUnitSwitch',1),('slaveUnitSwitch',2),('unitShutdown',3)))
class FmlHAModeVal(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('off',0),('master',1),('slave',2),('configMaster',3),('configSlave',4)))
_FmlTraps_ObjectIdentity=ObjectIdentity
fmlTraps=_FmlTraps_ObjectIdentity((1,3,6,1,4,1,12356,105,0))
_FmlSystem_ObjectIdentity=ObjectIdentity
fmlSystem=_FmlSystem_ObjectIdentity((1,3,6,1,4,1,12356,105,1))
class _FmlSysModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FmlSysModel_Type.__name__=_F
_FmlSysModel_Object=MibScalar
fmlSysModel=_FmlSysModel_Object((1,3,6,1,4,1,12356,105,1,1),_FmlSysModel_Type())
fmlSysModel.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysModel.setStatus(_B)
class _FmlSysSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FmlSysSerial_Type.__name__=_F
_FmlSysSerial_Object=MibScalar
fmlSysSerial=_FmlSysSerial_Object((1,3,6,1,4,1,12356,105,1,2),_FmlSysSerial_Type())
fmlSysSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysSerial.setStatus(_B)
class _FmlSysVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FmlSysVersion_Type.__name__=_F
_FmlSysVersion_Object=MibScalar
fmlSysVersion=_FmlSysVersion_Object((1,3,6,1,4,1,12356,105,1,3),_FmlSysVersion_Type())
fmlSysVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysVersion.setStatus(_B)
class _FmlSysVersionAv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FmlSysVersionAv_Type.__name__=_F
_FmlSysVersionAv_Object=MibScalar
fmlSysVersionAv=_FmlSysVersionAv_Object((1,3,6,1,4,1,12356,105,1,4),_FmlSysVersionAv_Type())
fmlSysVersionAv.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysVersionAv.setStatus(_B)
_FmlSysOpMode_Type=FmlOpMode
_FmlSysOpMode_Object=MibScalar
fmlSysOpMode=_FmlSysOpMode_Object((1,3,6,1,4,1,12356,105,1,5),_FmlSysOpMode_Type())
fmlSysOpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysOpMode.setStatus(_B)
_FmlSysCpuUsage_Type=Gauge32
_FmlSysCpuUsage_Object=MibScalar
fmlSysCpuUsage=_FmlSysCpuUsage_Object((1,3,6,1,4,1,12356,105,1,6),_FmlSysCpuUsage_Type())
fmlSysCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysCpuUsage.setStatus(_B)
_FmlSysMemUsage_Type=Gauge32
_FmlSysMemUsage_Object=MibScalar
fmlSysMemUsage=_FmlSysMemUsage_Object((1,3,6,1,4,1,12356,105,1,7),_FmlSysMemUsage_Type())
fmlSysMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysMemUsage.setStatus(_B)
_FmlSysLogDiskUsage_Type=Gauge32
_FmlSysLogDiskUsage_Object=MibScalar
fmlSysLogDiskUsage=_FmlSysLogDiskUsage_Object((1,3,6,1,4,1,12356,105,1,8),_FmlSysLogDiskUsage_Type())
fmlSysLogDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysLogDiskUsage.setStatus(_B)
_FmlSysMailDiskUsage_Type=Gauge32
_FmlSysMailDiskUsage_Object=MibScalar
fmlSysMailDiskUsage=_FmlSysMailDiskUsage_Object((1,3,6,1,4,1,12356,105,1,9),_FmlSysMailDiskUsage_Type())
fmlSysMailDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysMailDiskUsage.setStatus(_B)
_FmlSysSesCount_Type=Gauge32
_FmlSysSesCount_Object=MibScalar
fmlSysSesCount=_FmlSysSesCount_Object((1,3,6,1,4,1,12356,105,1,10),_FmlSysSesCount_Type())
fmlSysSesCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysSesCount.setStatus(_B)
_FmlSysEventCode_Type=FmlSysEventCodeVal
_FmlSysEventCode_Object=MibScalar
fmlSysEventCode=_FmlSysEventCode_Object((1,3,6,1,4,1,12356,105,1,11),_FmlSysEventCode_Type())
fmlSysEventCode.setMaxAccess(_G)
if mibBuilder.loadTexts:fmlSysEventCode.setStatus(_B)
_FmlRAIDCode_Type=FmlRAIDCodeVal
_FmlRAIDCode_Object=MibScalar
fmlRAIDCode=_FmlRAIDCode_Object((1,3,6,1,4,1,12356,105,1,12),_FmlRAIDCode_Type())
fmlRAIDCode.setMaxAccess(_G)
if mibBuilder.loadTexts:fmlRAIDCode.setStatus(_B)
class _FmlRAIDDevName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FmlRAIDDevName_Type.__name__=_F
_FmlRAIDDevName_Object=MibScalar
fmlRAIDDevName=_FmlRAIDDevName_Object((1,3,6,1,4,1,12356,105,1,13),_FmlRAIDDevName_Type())
fmlRAIDDevName.setMaxAccess(_G)
if mibBuilder.loadTexts:fmlRAIDDevName.setStatus(_B)
_FmlHAEventId_Type=FmlHAEventIdVal
_FmlHAEventId_Object=MibScalar
fmlHAEventId=_FmlHAEventId_Object((1,3,6,1,4,1,12356,105,1,14),_FmlHAEventId_Type())
fmlHAEventId.setMaxAccess(_G)
if mibBuilder.loadTexts:fmlHAEventId.setStatus(_B)
_FmlHAUnitIp_Type=IpAddress
_FmlHAUnitIp_Object=MibScalar
fmlHAUnitIp=_FmlHAUnitIp_Object((1,3,6,1,4,1,12356,105,1,15),_FmlHAUnitIp_Type())
fmlHAUnitIp.setMaxAccess(_G)
if mibBuilder.loadTexts:fmlHAUnitIp.setStatus(_B)
class _FmlHAEventReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FmlHAEventReason_Type.__name__=_F
_FmlHAEventReason_Object=MibScalar
fmlHAEventReason=_FmlHAEventReason_Object((1,3,6,1,4,1,12356,105,1,16),_FmlHAEventReason_Type())
fmlHAEventReason.setMaxAccess(_G)
if mibBuilder.loadTexts:fmlHAEventReason.setStatus(_B)
_FmlSysLoad_Type=Gauge32
_FmlSysLoad_Object=MibScalar
fmlSysLoad=_FmlSysLoad_Object((1,3,6,1,4,1,12356,105,1,30),_FmlSysLoad_Type())
fmlSysLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysLoad.setStatus(_B)
class _FmlRemoteStorageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_FmlRemoteStorageStatus_Type.__name__=_H
_FmlRemoteStorageStatus_Object=MibScalar
fmlRemoteStorageStatus=_FmlRemoteStorageStatus_Object((1,3,6,1,4,1,12356,105,1,31),_FmlRemoteStorageStatus_Type())
fmlRemoteStorageStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fmlRemoteStorageStatus.setStatus(_E)
_FmlSysOptions_ObjectIdentity=ObjectIdentity
fmlSysOptions=_FmlSysOptions_ObjectIdentity((1,3,6,1,4,1,12356,105,1,101))
_FmlSysOptIdleTimeout_Type=Integer32
_FmlSysOptIdleTimeout_Object=MibScalar
fmlSysOptIdleTimeout=_FmlSysOptIdleTimeout_Object((1,3,6,1,4,1,12356,105,1,101,1),_FmlSysOptIdleTimeout_Type())
fmlSysOptIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysOptIdleTimeout.setStatus(_B)
_FmlSysOptAuthTimeout_Type=Integer32
_FmlSysOptAuthTimeout_Object=MibScalar
fmlSysOptAuthTimeout=_FmlSysOptAuthTimeout_Object((1,3,6,1,4,1,12356,105,1,101,2),_FmlSysOptAuthTimeout_Type())
fmlSysOptAuthTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlSysOptAuthTimeout.setStatus(_B)
_FmlIp_ObjectIdentity=ObjectIdentity
fmlIp=_FmlIp_ObjectIdentity((1,3,6,1,4,1,12356,105,1,102))
_FmlIpSessTable_Object=MibTable
fmlIpSessTable=_FmlIpSessTable_Object((1,3,6,1,4,1,12356,105,1,102,2))
if mibBuilder.loadTexts:fmlIpSessTable.setStatus(_B)
_FmlIpSessEntry_Object=MibTableRow
fmlIpSessEntry=_FmlIpSessEntry_Object((1,3,6,1,4,1,12356,105,1,102,2,1))
fmlIpSessEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:fmlIpSessEntry.setStatus(_B)
_FmlIpSessIndex_Type=FnIndex
_FmlIpSessIndex_Object=MibTableColumn
fmlIpSessIndex=_FmlIpSessIndex_Object((1,3,6,1,4,1,12356,105,1,102,2,1,1),_FmlIpSessIndex_Type())
fmlIpSessIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:fmlIpSessIndex.setStatus(_B)
_FmlIpSessProto_Type=FnSessionProto
_FmlIpSessProto_Object=MibTableColumn
fmlIpSessProto=_FmlIpSessProto_Object((1,3,6,1,4,1,12356,105,1,102,2,1,2),_FmlIpSessProto_Type())
fmlIpSessProto.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlIpSessProto.setStatus(_B)
_FmlIpSessFromAddr_Type=IpAddress
_FmlIpSessFromAddr_Object=MibTableColumn
fmlIpSessFromAddr=_FmlIpSessFromAddr_Object((1,3,6,1,4,1,12356,105,1,102,2,1,3),_FmlIpSessFromAddr_Type())
fmlIpSessFromAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlIpSessFromAddr.setStatus(_B)
_FmlIpv6SessFromAddr_Type=FmlIpv6Address
_FmlIpv6SessFromAddr_Object=MibTableColumn
fmlIpv6SessFromAddr=_FmlIpv6SessFromAddr_Object((1,3,6,1,4,1,12356,105,1,102,2,1,4),_FmlIpv6SessFromAddr_Type())
fmlIpv6SessFromAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlIpv6SessFromAddr.setStatus(_B)
class _FmlIpSessFromPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FmlIpSessFromPort_Type.__name__=_H
_FmlIpSessFromPort_Object=MibTableColumn
fmlIpSessFromPort=_FmlIpSessFromPort_Object((1,3,6,1,4,1,12356,105,1,102,2,1,5),_FmlIpSessFromPort_Type())
fmlIpSessFromPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlIpSessFromPort.setStatus(_B)
_FmlIpSessToAddr_Type=IpAddress
_FmlIpSessToAddr_Object=MibTableColumn
fmlIpSessToAddr=_FmlIpSessToAddr_Object((1,3,6,1,4,1,12356,105,1,102,2,1,6),_FmlIpSessToAddr_Type())
fmlIpSessToAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlIpSessToAddr.setStatus(_B)
_FmlIpv6SessToAddr_Type=FmlIpv6Address
_FmlIpv6SessToAddr_Object=MibTableColumn
fmlIpv6SessToAddr=_FmlIpv6SessToAddr_Object((1,3,6,1,4,1,12356,105,1,102,2,1,7),_FmlIpv6SessToAddr_Type())
fmlIpv6SessToAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlIpv6SessToAddr.setStatus(_B)
class _FmlIpSessToPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FmlIpSessToPort_Type.__name__=_H
_FmlIpSessToPort_Object=MibTableColumn
fmlIpSessToPort=_FmlIpSessToPort_Object((1,3,6,1,4,1,12356,105,1,102,2,1,8),_FmlIpSessToPort_Type())
fmlIpSessToPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlIpSessToPort.setStatus(_B)
_FmlIpSessExp_Type=Gauge32
_FmlIpSessExp_Object=MibTableColumn
fmlIpSessExp=_FmlIpSessExp_Object((1,3,6,1,4,1,12356,105,1,102,2,1,9),_FmlIpSessExp_Type())
fmlIpSessExp.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlIpSessExp.setStatus(_B)
_FmlMailOptions_ObjectIdentity=ObjectIdentity
fmlMailOptions=_FmlMailOptions_ObjectIdentity((1,3,6,1,4,1,12356,105,1,103))
_FmlMailOptionsDeferQueue_Type=Gauge32
_FmlMailOptionsDeferQueue_Object=MibScalar
fmlMailOptionsDeferQueue=_FmlMailOptionsDeferQueue_Object((1,3,6,1,4,1,12356,105,1,103,1),_FmlMailOptionsDeferQueue_Type())
fmlMailOptionsDeferQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlMailOptionsDeferQueue.setStatus(_E)
_FmlMailQueueStatistics_Object=MibTable
fmlMailQueueStatistics=_FmlMailQueueStatistics_Object((1,3,6,1,4,1,12356,105,1,103,2))
if mibBuilder.loadTexts:fmlMailQueueStatistics.setStatus(_B)
_FmlMailQueueEntry_Object=MibTableRow
fmlMailQueueEntry=_FmlMailQueueEntry_Object((1,3,6,1,4,1,12356,105,1,103,2,1))
fmlMailQueueEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:fmlMailQueueEntry.setStatus(_B)
_FmlMailQueueIndex_Type=FnIndex
_FmlMailQueueIndex_Object=MibTableColumn
fmlMailQueueIndex=_FmlMailQueueIndex_Object((1,3,6,1,4,1,12356,105,1,103,2,1,1),_FmlMailQueueIndex_Type())
fmlMailQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlMailQueueIndex.setStatus(_B)
_FmlMailQueueName_Type=DisplayString
_FmlMailQueueName_Object=MibTableColumn
fmlMailQueueName=_FmlMailQueueName_Object((1,3,6,1,4,1,12356,105,1,103,2,1,2),_FmlMailQueueName_Type())
fmlMailQueueName.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlMailQueueName.setStatus(_B)
_FmlMailQueueMailCount_Type=Gauge32
_FmlMailQueueMailCount_Object=MibTableColumn
fmlMailQueueMailCount=_FmlMailQueueMailCount_Object((1,3,6,1,4,1,12356,105,1,103,2,1,3),_FmlMailQueueMailCount_Type())
fmlMailQueueMailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlMailQueueMailCount.setStatus(_B)
_FmlMailQueueMailSize_Type=Gauge32
_FmlMailQueueMailSize_Object=MibTableColumn
fmlMailQueueMailSize=_FmlMailQueueMailSize_Object((1,3,6,1,4,1,12356,105,1,103,2,1,4),_FmlMailQueueMailSize_Type())
fmlMailQueueMailSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlMailQueueMailSize.setStatus(_B)
_FmlHwSensors_ObjectIdentity=ObjectIdentity
fmlHwSensors=_FmlHwSensors_ObjectIdentity((1,3,6,1,4,1,12356,105,1,110))
_FmlHwSensorCount_Type=Integer32
_FmlHwSensorCount_Object=MibScalar
fmlHwSensorCount=_FmlHwSensorCount_Object((1,3,6,1,4,1,12356,105,1,110,1),_FmlHwSensorCount_Type())
fmlHwSensorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlHwSensorCount.setStatus(_B)
_FmlHwSensorTable_Object=MibTable
fmlHwSensorTable=_FmlHwSensorTable_Object((1,3,6,1,4,1,12356,105,1,110,2))
if mibBuilder.loadTexts:fmlHwSensorTable.setStatus(_B)
_FmlHwSensorEntry_Object=MibTableRow
fmlHwSensorEntry=_FmlHwSensorEntry_Object((1,3,6,1,4,1,12356,105,1,110,2,1))
fmlHwSensorEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:fmlHwSensorEntry.setStatus(_B)
_FmlHwSensorEntIndex_Type=FnIndex
_FmlHwSensorEntIndex_Object=MibTableColumn
fmlHwSensorEntIndex=_FmlHwSensorEntIndex_Object((1,3,6,1,4,1,12356,105,1,110,2,1,1),_FmlHwSensorEntIndex_Type())
fmlHwSensorEntIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:fmlHwSensorEntIndex.setStatus(_B)
_FmlHwSensorEntName_Type=DisplayString
_FmlHwSensorEntName_Object=MibTableColumn
fmlHwSensorEntName=_FmlHwSensorEntName_Object((1,3,6,1,4,1,12356,105,1,110,2,1,2),_FmlHwSensorEntName_Type())
fmlHwSensorEntName.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlHwSensorEntName.setStatus(_B)
_FmlHwSensorEntValue_Type=DisplayString
_FmlHwSensorEntValue_Object=MibTableColumn
fmlHwSensorEntValue=_FmlHwSensorEntValue_Object((1,3,6,1,4,1,12356,105,1,110,2,1,3),_FmlHwSensorEntValue_Type())
fmlHwSensorEntValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlHwSensorEntValue.setStatus(_B)
class _FmlHwSensorEntAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_FmlHwSensorEntAlarmStatus_Type.__name__=_H
_FmlHwSensorEntAlarmStatus_Object=MibTableColumn
fmlHwSensorEntAlarmStatus=_FmlHwSensorEntAlarmStatus_Object((1,3,6,1,4,1,12356,105,1,110,2,1,4),_FmlHwSensorEntAlarmStatus_Type())
fmlHwSensorEntAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlHwSensorEntAlarmStatus.setStatus(_B)
_FmlSysHA_ObjectIdentity=ObjectIdentity
fmlSysHA=_FmlSysHA_ObjectIdentity((1,3,6,1,4,1,12356,105,1,200))
_FmlHAMode_Type=FmlHAModeVal
_FmlHAMode_Object=MibScalar
fmlHAMode=_FmlHAMode_Object((1,3,6,1,4,1,12356,105,1,200,1),_FmlHAMode_Type())
fmlHAMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlHAMode.setStatus(_B)
_FmlHAEffectiveMode_Type=FmlHAModeVal
_FmlHAEffectiveMode_Object=MibScalar
fmlHAEffectiveMode=_FmlHAEffectiveMode_Object((1,3,6,1,4,1,12356,105,1,200,2),_FmlHAEffectiveMode_Type())
fmlHAEffectiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fmlHAEffectiveMode.setStatus(_B)
_FmlMIBConformance_ObjectIdentity=ObjectIdentity
fmlMIBConformance=_FmlMIBConformance_ObjectIdentity((1,3,6,1,4,1,12356,105,600))
fmlSystemConformanceGroup=ObjectGroup((1,3,6,1,4,1,12356,105,600,1))
fmlSystemConformanceGroup.setObjects(*((_A,_X),(_A,_D),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_g)))
if mibBuilder.loadTexts:fmlSystemConformanceGroup.setStatus(_B)
fmlSysOptionsConformanceGroup=ObjectGroup((1,3,6,1,4,1,12356,105,600,2))
fmlSysOptionsConformanceGroup.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:fmlSysOptionsConformanceGroup.setStatus(_B)
fmlIpConformanceGroup=ObjectGroup((1,3,6,1,4,1,12356,105,600,3))
fmlIpConformanceGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:fmlIpConformanceGroup.setStatus(_B)
fmlMailOptionsConformanceGroup=ObjectGroup((1,3,6,1,4,1,12356,105,600,4))
fmlMailOptionsConformanceGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:fmlMailOptionsConformanceGroup.setStatus(_B)
fmlHwSensorsConformanceGroup=ObjectGroup((1,3,6,1,4,1,12356,105,600,5))
fmlHwSensorsConformanceGroup.setObjects(*((_A,_s),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:fmlHwSensorsConformanceGroup.setStatus(_B)
fmlHAModeConformanceGroup=ObjectGroup((1,3,6,1,4,1,12356,105,600,6))
fmlHAModeConformanceGroup.setObjects(*((_A,_t),(_A,_u)))
if mibBuilder.loadTexts:fmlHAModeConformanceGroup.setStatus(_B)
fmlTrapCpuHighThreshold=NotificationType((1,3,6,1,4,1,12356,105,0,101))
fmlTrapCpuHighThreshold.setObjects((_A,_D))
if mibBuilder.loadTexts:fmlTrapCpuHighThreshold.setStatus(_E)
fmlTrapMemLowThreshold=NotificationType((1,3,6,1,4,1,12356,105,0,102))
fmlTrapMemLowThreshold.setObjects((_A,_D))
if mibBuilder.loadTexts:fmlTrapMemLowThreshold.setStatus(_E)
fmlTrapLogDiskHighThreshold=NotificationType((1,3,6,1,4,1,12356,105,0,103))
fmlTrapLogDiskHighThreshold.setObjects((_A,_D))
if mibBuilder.loadTexts:fmlTrapLogDiskHighThreshold.setStatus(_E)
fmlTrapMailDiskHighThreshold=NotificationType((1,3,6,1,4,1,12356,105,0,104))
fmlTrapMailDiskHighThreshold.setObjects((_A,_D))
if mibBuilder.loadTexts:fmlTrapMailDiskHighThreshold.setStatus(_B)
fmlTrapMailDeferredQueueHighThreshold=NotificationType((1,3,6,1,4,1,12356,105,0,105))
fmlTrapMailDeferredQueueHighThreshold.setObjects((_A,_D))
if mibBuilder.loadTexts:fmlTrapMailDeferredQueueHighThreshold.setStatus(_B)
fmlTrapAvThresholdEvent=NotificationType((1,3,6,1,4,1,12356,105,0,106))
fmlTrapAvThresholdEvent.setObjects((_A,_D))
if mibBuilder.loadTexts:fmlTrapAvThresholdEvent.setStatus(_B)
fmlTrapSpamThresholdEvent=NotificationType((1,3,6,1,4,1,12356,105,0,107))
fmlTrapSpamThresholdEvent.setObjects((_A,_D))
if mibBuilder.loadTexts:fmlTrapSpamThresholdEvent.setStatus(_B)
fmlTrapPSUFailureEvent=NotificationType((1,3,6,1,4,1,12356,105,0,108))
fmlTrapPSUFailureEvent.setObjects(*((_A,_D),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:fmlTrapPSUFailureEvent.setStatus(_E)
fmlTrapSystemEvent=NotificationType((1,3,6,1,4,1,12356,105,0,201))
fmlTrapSystemEvent.setObjects(*((_A,_D),(_A,_I)))
if mibBuilder.loadTexts:fmlTrapSystemEvent.setStatus(_B)
fmlTrapRAIDEvent=NotificationType((1,3,6,1,4,1,12356,105,0,202))
fmlTrapRAIDEvent.setObjects(*((_A,_D),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:fmlTrapRAIDEvent.setStatus(_B)
fmlTrapHAEvent=NotificationType((1,3,6,1,4,1,12356,105,0,203))
fmlTrapHAEvent.setObjects(*((_A,_D),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:fmlTrapHAEvent.setStatus(_B)
fmlTrapRemoteStorage=NotificationType((1,3,6,1,4,1,12356,105,0,205))
fmlTrapRemoteStorage.setObjects(*((_A,_D),(_A,_v)))
if mibBuilder.loadTexts:fmlTrapRemoteStorage.setStatus(_E)
fmlTrapIpChange=NotificationType((1,3,6,1,4,1,12356,105,0,301))
fmlTrapIpChange.setObjects(*((_A,_D),(_R,_S)))
if mibBuilder.loadTexts:fmlTrapIpChange.setStatus(_E)
fmlTrapsComplianceGroup=NotificationGroup((1,3,6,1,4,1,12356,105,600,7))
fmlTrapsComplianceGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:fmlTrapsComplianceGroup.setStatus(_B)
fmlObsoleteTrapsComplianceGroup=NotificationGroup((1,3,6,1,4,1,12356,105,600,8))
fmlObsoleteTrapsComplianceGroup.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:fmlObsoleteTrapsComplianceGroup.setStatus(_E)
fmlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,105,600,100))
fmlMIBCompliance.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:fmlMIBCompliance.setStatus(_B)
fmlObsoleteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,105,600,101))
fmlObsoleteMIBCompliance.setObjects((_A,_AF))
if mibBuilder.loadTexts:fmlObsoleteMIBCompliance.setStatus(_E)
mibBuilder.exportSymbols(_A,**{'FmlIpv6Address':FmlIpv6Address,'FmlOpMode':FmlOpMode,'FmlSysEventCodeVal':FmlSysEventCodeVal,'FmlRAIDCodeVal':FmlRAIDCodeVal,'FmlHAEventIdVal':FmlHAEventIdVal,'FmlHAModeVal':FmlHAModeVal,'fnFortiMailMib':fnFortiMailMib,'fmlTraps':fmlTraps,_A3:fmlTrapCpuHighThreshold,_A4:fmlTrapMemLowThreshold,_A5:fmlTrapLogDiskHighThreshold,_w:fmlTrapMailDiskHighThreshold,_x:fmlTrapMailDeferredQueueHighThreshold,_y:fmlTrapAvThresholdEvent,_z:fmlTrapSpamThresholdEvent,_A6:fmlTrapPSUFailureEvent,_A0:fmlTrapSystemEvent,_A1:fmlTrapRAIDEvent,_A2:fmlTrapHAEvent,'fmlTrapRemoteStorage':fmlTrapRemoteStorage,_A7:fmlTrapIpChange,'fmlSystem':fmlSystem,_X:fmlSysModel,_D:fmlSysSerial,_Y:fmlSysVersion,_Z:fmlSysVersionAv,_a:fmlSysOpMode,_b:fmlSysCpuUsage,_c:fmlSysMemUsage,_d:fmlSysLogDiskUsage,_e:fmlSysMailDiskUsage,_f:fmlSysSesCount,_I:fmlSysEventCode,_J:fmlRAIDCode,_K:fmlRAIDDevName,_L:fmlHAEventId,_M:fmlHAUnitIp,_N:fmlHAEventReason,_g:fmlSysLoad,_v:fmlRemoteStorageStatus,'fmlSysOptions':fmlSysOptions,_h:fmlSysOptIdleTimeout,_i:fmlSysOptAuthTimeout,'fmlIp':fmlIp,'fmlIpSessTable':fmlIpSessTable,'fmlIpSessEntry':fmlIpSessEntry,_T:fmlIpSessIndex,_j:fmlIpSessProto,_k:fmlIpSessFromAddr,'fmlIpv6SessFromAddr':fmlIpv6SessFromAddr,_l:fmlIpSessFromPort,_m:fmlIpSessToAddr,'fmlIpv6SessToAddr':fmlIpv6SessToAddr,_n:fmlIpSessToPort,_o:fmlIpSessExp,'fmlMailOptions':fmlMailOptions,'fmlMailOptionsDeferQueue':fmlMailOptionsDeferQueue,'fmlMailQueueStatistics':fmlMailQueueStatistics,'fmlMailQueueEntry':fmlMailQueueEntry,_V:fmlMailQueueIndex,_p:fmlMailQueueName,_q:fmlMailQueueMailCount,_r:fmlMailQueueMailSize,'fmlHwSensors':fmlHwSensors,_s:fmlHwSensorCount,'fmlHwSensorTable':fmlHwSensorTable,'fmlHwSensorEntry':fmlHwSensorEntry,_W:fmlHwSensorEntIndex,_O:fmlHwSensorEntName,_P:fmlHwSensorEntValue,_Q:fmlHwSensorEntAlarmStatus,'fmlSysHA':fmlSysHA,_t:fmlHAMode,_u:fmlHAEffectiveMode,'fmlMIBConformance':fmlMIBConformance,_A8:fmlSystemConformanceGroup,_A9:fmlSysOptionsConformanceGroup,_AA:fmlIpConformanceGroup,_AB:fmlMailOptionsConformanceGroup,_AC:fmlHwSensorsConformanceGroup,_AD:fmlHAModeConformanceGroup,_AE:fmlTrapsComplianceGroup,_AF:fmlObsoleteTrapsComplianceGroup,'fmlMIBCompliance':fmlMIBCompliance,'fmlObsoleteMIBCompliance':fmlObsoleteMIBCompliance})