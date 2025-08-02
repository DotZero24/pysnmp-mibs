_AW='h3cSystemBtmLoadGroup'
_AV='h3cSysCurGroup'
_AU='h3cSystemManNotificationGroup'
_AT='h3cSysCFGFileGroup'
_AS='h3cSysImageGroup'
_AR='h3cSysReloadGroup'
_AQ='h3cSysClockGroup'
_AP='h3cSysStartUpNotification'
_AO='h3cSysReloadNotification'
_AN='h3cSysClockChangedNotification'
_AM='h3cSysBtmLoadTime'
_AL='h3cSysBtmErrorStatus'
_AK='h3cSysBtmRowStatus'
_AJ='h3cSysBtmFileType'
_AI='h3cSysBtmFileName'
_AH='h3cSysBtmLoadMaxNumber'
_AG='h3cSysCurUpdateBtmFileName'
_AF='h3cSysCurBtmFileName'
_AE='h3cSysCurImageIndex'
_AD='h3cSysCurCFGFileIndex'
_AC='h3cSysCFGFileLocation'
_AB='h3cSysCFGFileSize'
_AA='h3cSysCFGFileName'
_A9='h3cSysCFGFileNum'
_A8='h3cSysImageLocation'
_A7='h3cSysImageSize'
_A6='h3cSysImageName'
_A5='h3cSysImageNum'
_A4='h3cSysReloadRowStatus'
_A3='h3cSysReloadEntity'
_A2='h3cSysReloadTag'
_A1='h3cSysReloadScheduleTagList'
_A0='h3cSysReloadSchedule'
_z='h3cSysSummerTimeOffset'
_y='h3cSysSummerTimeEnd'
_x='h3cSysSummerTimeStart'
_w='h3cSysSummerTimeMethod'
_v='h3cSysSummerTimeZone'
_u='h3cSysSummerTimeEnable'
_t='h3cSysSetBootImageResultIndex'
_s='h3cSysBootIpeIndex'
_r='h3cSysBootPackageIndex'
_q='h3cSysIpeFileOperateIndex'
_p='h3cSysIpePackageIndex'
_o='opInvalidFile'
_n='opUnknownFailure'
_m='opSuccess'
_l='opInProgress'
_k='h3cSysPackageOperateIndex'
_j='inactive'
_i='active'
_h='feature'
_g='system'
_f='h3cSysPackageIndex'
_e='h3cSysBtmLoadIndex'
_d='h3cSysCFGFileIndex'
_c='h3cSysImageIndex'
_b='h3cSysReloadScheduleIndex'
_a='h3cSysCurEntPhysicalIndex'
_Z='h3cSysImageType'
_Y='h3cSysReloadScheduleTime'
_X='h3cSysReloadReason'
_W='h3cSysReloadCfgFile'
_V='h3cSysReloadImage'
_U='h3cSysReloadAction'
_T='h3cSysLocalClock'
_S='h3cSysIpeFileIndex'
_R='primarySecondary'
_Q='secondary'
_P='primary'
_O='failed'
_N='success'
_M='TruthValue'
_L='DateAndTime'
_K='Unsigned32'
_J='OctetString'
_I='none'
_H='not-accessible'
_G='read-create'
_F='read-write'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='H3C-SYS-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
SnmpTagList,SnmpTagValue=mibBuilder.importSymbols('SNMP-TARGET-MIB','SnmpTagList','SnmpTagValue')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,_E,'PhysAddress','RowStatus','TextualConvention',_M)
h3cSystemMan=ModuleIdentity((1,3,6,1,4,1,2011,10,2,3))
if mibBuilder.loadTexts:h3cSystemMan.setRevisions(('2018-01-10 00:00','2017-06-12 00:00','2015-07-27 00:00','2004-04-08 13:45'))
_H3cSystemManMIBObjects_ObjectIdentity=ObjectIdentity
h3cSystemManMIBObjects=_H3cSystemManMIBObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1))
_H3cSysClock_ObjectIdentity=ObjectIdentity
h3cSysClock=_H3cSysClock_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,1))
_H3cSysLocalClock_Type=DateAndTime
_H3cSysLocalClock_Object=MibScalar
h3cSysLocalClock=_H3cSysLocalClock_Object((1,3,6,1,4,1,2011,10,2,3,1,1,1),_H3cSysLocalClock_Type())
h3cSysLocalClock.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysLocalClock.setStatus(_A)
_H3cSysSummerTime_ObjectIdentity=ObjectIdentity
h3cSysSummerTime=_H3cSysSummerTime_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,1,2))
class _H3cSysSummerTimeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_H3cSysSummerTimeEnable_Type.__name__=_C
_H3cSysSummerTimeEnable_Object=MibScalar
h3cSysSummerTimeEnable=_H3cSysSummerTimeEnable_Object((1,3,6,1,4,1,2011,10,2,3,1,1,2,1),_H3cSysSummerTimeEnable_Type())
h3cSysSummerTimeEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysSummerTimeEnable.setStatus(_A)
class _H3cSysSummerTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysSummerTimeZone_Type.__name__=_E
_H3cSysSummerTimeZone_Object=MibScalar
h3cSysSummerTimeZone=_H3cSysSummerTimeZone_Object((1,3,6,1,4,1,2011,10,2,3,1,1,2,2),_H3cSysSummerTimeZone_Type())
h3cSysSummerTimeZone.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysSummerTimeZone.setStatus(_A)
class _H3cSysSummerTimeMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneOff',1),('repeating',2)))
_H3cSysSummerTimeMethod_Type.__name__=_C
_H3cSysSummerTimeMethod_Object=MibScalar
h3cSysSummerTimeMethod=_H3cSysSummerTimeMethod_Object((1,3,6,1,4,1,2011,10,2,3,1,1,2,3),_H3cSysSummerTimeMethod_Type())
h3cSysSummerTimeMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysSummerTimeMethod.setStatus(_A)
class _H3cSysSummerTimeStart_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_H3cSysSummerTimeStart_Type.__name__=_L
_H3cSysSummerTimeStart_Object=MibScalar
h3cSysSummerTimeStart=_H3cSysSummerTimeStart_Object((1,3,6,1,4,1,2011,10,2,3,1,1,2,4),_H3cSysSummerTimeStart_Type())
h3cSysSummerTimeStart.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysSummerTimeStart.setStatus(_A)
class _H3cSysSummerTimeEnd_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_H3cSysSummerTimeEnd_Type.__name__=_L
_H3cSysSummerTimeEnd_Object=MibScalar
h3cSysSummerTimeEnd=_H3cSysSummerTimeEnd_Object((1,3,6,1,4,1,2011,10,2,3,1,1,2,5),_H3cSysSummerTimeEnd_Type())
h3cSysSummerTimeEnd.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysSummerTimeEnd.setStatus(_A)
class _H3cSysSummerTimeOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86399))
_H3cSysSummerTimeOffset_Type.__name__=_C
_H3cSysSummerTimeOffset_Object=MibScalar
h3cSysSummerTimeOffset=_H3cSysSummerTimeOffset_Object((1,3,6,1,4,1,2011,10,2,3,1,1,2,6),_H3cSysSummerTimeOffset_Type())
h3cSysSummerTimeOffset.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysSummerTimeOffset.setStatus(_A)
class _H3cSysLocalClockString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,24))
_H3cSysLocalClockString_Type.__name__=_J
_H3cSysLocalClockString_Object=MibScalar
h3cSysLocalClockString=_H3cSysLocalClockString_Object((1,3,6,1,4,1,2011,10,2,3,1,1,3),_H3cSysLocalClockString_Type())
h3cSysLocalClockString.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysLocalClockString.setStatus(_A)
_H3cSysClockProtocolGroup_ObjectIdentity=ObjectIdentity
h3cSysClockProtocolGroup=_H3cSysClockProtocolGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,1,4))
class _H3cSysClockProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('ntp',2),('ptp',3),('interface',4)))
_H3cSysClockProtocol_Type.__name__=_C
_H3cSysClockProtocol_Object=MibScalar
h3cSysClockProtocol=_H3cSysClockProtocol_Object((1,3,6,1,4,1,2011,10,2,3,1,1,4,1),_H3cSysClockProtocol_Type())
h3cSysClockProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysClockProtocol.setStatus(_A)
class _H3cSysClockProtocolSrcMdc_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysClockProtocolSrcMdc_Type.__name__=_C
_H3cSysClockProtocolSrcMdc_Object=MibScalar
h3cSysClockProtocolSrcMdc=_H3cSysClockProtocolSrcMdc_Object((1,3,6,1,4,1,2011,10,2,3,1,1,4,2),_H3cSysClockProtocolSrcMdc_Type())
h3cSysClockProtocolSrcMdc.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysClockProtocolSrcMdc.setStatus(_A)
class _H3cSysClockProtocolSrcContext_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysClockProtocolSrcContext_Type.__name__=_C
_H3cSysClockProtocolSrcContext_Object=MibScalar
h3cSysClockProtocolSrcContext=_H3cSysClockProtocolSrcContext_Object((1,3,6,1,4,1,2011,10,2,3,1,1,4,3),_H3cSysClockProtocolSrcContext_Type())
h3cSysClockProtocolSrcContext.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysClockProtocolSrcContext.setStatus(_A)
class _H3cSysLocalClockString2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,19))
_H3cSysLocalClockString2_Type.__name__=_J
_H3cSysLocalClockString2_Object=MibScalar
h3cSysLocalClockString2=_H3cSysLocalClockString2_Object((1,3,6,1,4,1,2011,10,2,3,1,1,5),_H3cSysLocalClockString2_Type())
h3cSysLocalClockString2.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysLocalClockString2.setStatus(_A)
_H3cSysCurrent_ObjectIdentity=ObjectIdentity
h3cSysCurrent=_H3cSysCurrent_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,2))
_H3cSysCurTable_Object=MibTable
h3cSysCurTable=_H3cSysCurTable_Object((1,3,6,1,4,1,2011,10,2,3,1,2,1))
if mibBuilder.loadTexts:h3cSysCurTable.setStatus(_A)
_H3cSysCurEntry_Object=MibTableRow
h3cSysCurEntry=_H3cSysCurEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,2,1,1))
h3cSysCurEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:h3cSysCurEntry.setStatus(_A)
class _H3cSysCurEntPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysCurEntPhysicalIndex_Type.__name__=_C
_H3cSysCurEntPhysicalIndex_Object=MibTableColumn
h3cSysCurEntPhysicalIndex=_H3cSysCurEntPhysicalIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,2,1,1,1),_H3cSysCurEntPhysicalIndex_Type())
h3cSysCurEntPhysicalIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysCurEntPhysicalIndex.setStatus(_A)
class _H3cSysCurCFGFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysCurCFGFileIndex_Type.__name__=_C
_H3cSysCurCFGFileIndex_Object=MibTableColumn
h3cSysCurCFGFileIndex=_H3cSysCurCFGFileIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,2,1,1,2),_H3cSysCurCFGFileIndex_Type())
h3cSysCurCFGFileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysCurCFGFileIndex.setStatus(_A)
class _H3cSysCurImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysCurImageIndex_Type.__name__=_C
_H3cSysCurImageIndex_Object=MibTableColumn
h3cSysCurImageIndex=_H3cSysCurImageIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,2,1,1,3),_H3cSysCurImageIndex_Type())
h3cSysCurImageIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysCurImageIndex.setStatus(_A)
class _H3cSysCurBtmFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cSysCurBtmFileName_Type.__name__=_J
_H3cSysCurBtmFileName_Object=MibTableColumn
h3cSysCurBtmFileName=_H3cSysCurBtmFileName_Object((1,3,6,1,4,1,2011,10,2,3,1,2,1,1,4),_H3cSysCurBtmFileName_Type())
h3cSysCurBtmFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysCurBtmFileName.setStatus(_A)
class _H3cSysCurUpdateBtmFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cSysCurUpdateBtmFileName_Type.__name__=_J
_H3cSysCurUpdateBtmFileName_Object=MibTableColumn
h3cSysCurUpdateBtmFileName=_H3cSysCurUpdateBtmFileName_Object((1,3,6,1,4,1,2011,10,2,3,1,2,1,1,5),_H3cSysCurUpdateBtmFileName_Type())
h3cSysCurUpdateBtmFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysCurUpdateBtmFileName.setStatus(_A)
_H3cSysReload_ObjectIdentity=ObjectIdentity
h3cSysReload=_H3cSysReload_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,3))
class _H3cSysReloadSchedule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysReloadSchedule_Type.__name__=_C
_H3cSysReloadSchedule_Object=MibScalar
h3cSysReloadSchedule=_H3cSysReloadSchedule_Object((1,3,6,1,4,1,2011,10,2,3,1,3,1),_H3cSysReloadSchedule_Type())
h3cSysReloadSchedule.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysReloadSchedule.setStatus(_A)
class _H3cSysReloadAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('reloadUnavailable',1),('reloadOnSchedule',2),('reloadAtOnce',3),('reloadCancel',4)))
_H3cSysReloadAction_Type.__name__=_C
_H3cSysReloadAction_Object=MibScalar
h3cSysReloadAction=_H3cSysReloadAction_Object((1,3,6,1,4,1,2011,10,2,3,1,3,2),_H3cSysReloadAction_Type())
h3cSysReloadAction.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysReloadAction.setStatus(_A)
_H3cSysReloadScheduleTable_Object=MibTable
h3cSysReloadScheduleTable=_H3cSysReloadScheduleTable_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3))
if mibBuilder.loadTexts:h3cSysReloadScheduleTable.setStatus(_A)
_H3cSysReloadScheduleEntry_Object=MibTableRow
h3cSysReloadScheduleEntry=_H3cSysReloadScheduleEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1))
h3cSysReloadScheduleEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:h3cSysReloadScheduleEntry.setStatus(_A)
class _H3cSysReloadScheduleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysReloadScheduleIndex_Type.__name__=_C
_H3cSysReloadScheduleIndex_Object=MibTableColumn
h3cSysReloadScheduleIndex=_H3cSysReloadScheduleIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1,1),_H3cSysReloadScheduleIndex_Type())
h3cSysReloadScheduleIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysReloadScheduleIndex.setStatus(_A)
class _H3cSysReloadEntity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysReloadEntity_Type.__name__=_C
_H3cSysReloadEntity_Object=MibTableColumn
h3cSysReloadEntity=_H3cSysReloadEntity_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1,2),_H3cSysReloadEntity_Type())
h3cSysReloadEntity.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysReloadEntity.setStatus(_A)
class _H3cSysReloadCfgFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysReloadCfgFile_Type.__name__=_C
_H3cSysReloadCfgFile_Object=MibTableColumn
h3cSysReloadCfgFile=_H3cSysReloadCfgFile_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1,3),_H3cSysReloadCfgFile_Type())
h3cSysReloadCfgFile.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysReloadCfgFile.setStatus(_A)
class _H3cSysReloadImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysReloadImage_Type.__name__=_C
_H3cSysReloadImage_Object=MibTableColumn
h3cSysReloadImage=_H3cSysReloadImage_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1,4),_H3cSysReloadImage_Type())
h3cSysReloadImage.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysReloadImage.setStatus(_A)
class _H3cSysReloadReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysReloadReason_Type.__name__=_E
_H3cSysReloadReason_Object=MibTableColumn
h3cSysReloadReason=_H3cSysReloadReason_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1,5),_H3cSysReloadReason_Type())
h3cSysReloadReason.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysReloadReason.setStatus(_A)
class _H3cSysReloadScheduleTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_H3cSysReloadScheduleTime_Type.__name__=_L
_H3cSysReloadScheduleTime_Object=MibTableColumn
h3cSysReloadScheduleTime=_H3cSysReloadScheduleTime_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1,6),_H3cSysReloadScheduleTime_Type())
h3cSysReloadScheduleTime.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysReloadScheduleTime.setStatus(_A)
_H3cSysReloadRowStatus_Type=RowStatus
_H3cSysReloadRowStatus_Object=MibTableColumn
h3cSysReloadRowStatus=_H3cSysReloadRowStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1,7),_H3cSysReloadRowStatus_Type())
h3cSysReloadRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysReloadRowStatus.setStatus(_A)
_H3cSysReloadScheduleTagList_Type=SnmpTagList
_H3cSysReloadScheduleTagList_Object=MibTableColumn
h3cSysReloadScheduleTagList=_H3cSysReloadScheduleTagList_Object((1,3,6,1,4,1,2011,10,2,3,1,3,3,1,8),_H3cSysReloadScheduleTagList_Type())
h3cSysReloadScheduleTagList.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysReloadScheduleTagList.setStatus(_A)
_H3cSysReloadTag_Type=SnmpTagValue
_H3cSysReloadTag_Object=MibScalar
h3cSysReloadTag=_H3cSysReloadTag_Object((1,3,6,1,4,1,2011,10,2,3,1,3,4),_H3cSysReloadTag_Type())
h3cSysReloadTag.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysReloadTag.setStatus(_A)
_H3cSysImage_ObjectIdentity=ObjectIdentity
h3cSysImage=_H3cSysImage_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,4))
class _H3cSysImageNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysImageNum_Type.__name__=_C
_H3cSysImageNum_Object=MibScalar
h3cSysImageNum=_H3cSysImageNum_Object((1,3,6,1,4,1,2011,10,2,3,1,4,1),_H3cSysImageNum_Type())
h3cSysImageNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysImageNum.setStatus(_A)
_H3cSysImageTable_Object=MibTable
h3cSysImageTable=_H3cSysImageTable_Object((1,3,6,1,4,1,2011,10,2,3,1,4,2))
if mibBuilder.loadTexts:h3cSysImageTable.setStatus(_A)
_H3cSysImageEntry_Object=MibTableRow
h3cSysImageEntry=_H3cSysImageEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,4,2,1))
h3cSysImageEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:h3cSysImageEntry.setStatus(_A)
class _H3cSysImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysImageIndex_Type.__name__=_C
_H3cSysImageIndex_Object=MibTableColumn
h3cSysImageIndex=_H3cSysImageIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,4,2,1,1),_H3cSysImageIndex_Type())
h3cSysImageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysImageIndex.setStatus(_A)
class _H3cSysImageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysImageName_Type.__name__=_E
_H3cSysImageName_Object=MibTableColumn
h3cSysImageName=_H3cSysImageName_Object((1,3,6,1,4,1,2011,10,2,3,1,4,2,1,2),_H3cSysImageName_Type())
h3cSysImageName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysImageName.setStatus(_A)
class _H3cSysImageSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysImageSize_Type.__name__=_C
_H3cSysImageSize_Object=MibTableColumn
h3cSysImageSize=_H3cSysImageSize_Object((1,3,6,1,4,1,2011,10,2,3,1,4,2,1,3),_H3cSysImageSize_Type())
h3cSysImageSize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysImageSize.setStatus(_A)
class _H3cSysImageLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysImageLocation_Type.__name__=_E
_H3cSysImageLocation_Object=MibTableColumn
h3cSysImageLocation=_H3cSysImageLocation_Object((1,3,6,1,4,1,2011,10,2,3,1,4,2,1,4),_H3cSysImageLocation_Type())
h3cSysImageLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysImageLocation.setStatus(_A)
class _H3cSysImageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('main',1),('backup',2),(_I,3),('secure',4),('main-backup',5),('main-secure',6),('backup-secure',7),('main-backup-secure',8)))
_H3cSysImageType_Type.__name__=_C
_H3cSysImageType_Object=MibTableColumn
h3cSysImageType=_H3cSysImageType_Object((1,3,6,1,4,1,2011,10,2,3,1,4,2,1,5),_H3cSysImageType_Type())
h3cSysImageType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysImageType.setStatus(_A)
_H3cSysCFGFile_ObjectIdentity=ObjectIdentity
h3cSysCFGFile=_H3cSysCFGFile_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,5))
class _H3cSysCFGFileNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysCFGFileNum_Type.__name__=_C
_H3cSysCFGFileNum_Object=MibScalar
h3cSysCFGFileNum=_H3cSysCFGFileNum_Object((1,3,6,1,4,1,2011,10,2,3,1,5,1),_H3cSysCFGFileNum_Type())
h3cSysCFGFileNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysCFGFileNum.setStatus(_A)
_H3cSysCFGFileTable_Object=MibTable
h3cSysCFGFileTable=_H3cSysCFGFileTable_Object((1,3,6,1,4,1,2011,10,2,3,1,5,2))
if mibBuilder.loadTexts:h3cSysCFGFileTable.setStatus(_A)
_H3cSysCFGFileEntry_Object=MibTableRow
h3cSysCFGFileEntry=_H3cSysCFGFileEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,5,2,1))
h3cSysCFGFileEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:h3cSysCFGFileEntry.setStatus(_A)
class _H3cSysCFGFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysCFGFileIndex_Type.__name__=_C
_H3cSysCFGFileIndex_Object=MibTableColumn
h3cSysCFGFileIndex=_H3cSysCFGFileIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,5,2,1,1),_H3cSysCFGFileIndex_Type())
h3cSysCFGFileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysCFGFileIndex.setStatus(_A)
class _H3cSysCFGFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysCFGFileName_Type.__name__=_E
_H3cSysCFGFileName_Object=MibTableColumn
h3cSysCFGFileName=_H3cSysCFGFileName_Object((1,3,6,1,4,1,2011,10,2,3,1,5,2,1,2),_H3cSysCFGFileName_Type())
h3cSysCFGFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysCFGFileName.setStatus(_A)
class _H3cSysCFGFileSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysCFGFileSize_Type.__name__=_C
_H3cSysCFGFileSize_Object=MibTableColumn
h3cSysCFGFileSize=_H3cSysCFGFileSize_Object((1,3,6,1,4,1,2011,10,2,3,1,5,2,1,3),_H3cSysCFGFileSize_Type())
h3cSysCFGFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysCFGFileSize.setStatus(_A)
class _H3cSysCFGFileLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysCFGFileLocation_Type.__name__=_E
_H3cSysCFGFileLocation_Object=MibTableColumn
h3cSysCFGFileLocation=_H3cSysCFGFileLocation_Object((1,3,6,1,4,1,2011,10,2,3,1,5,2,1,4),_H3cSysCFGFileLocation_Type())
h3cSysCFGFileLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysCFGFileLocation.setStatus(_A)
_H3cSysBtmFile_ObjectIdentity=ObjectIdentity
h3cSysBtmFile=_H3cSysBtmFile_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,6))
_H3cSysBtmFileLoad_ObjectIdentity=ObjectIdentity
h3cSysBtmFileLoad=_H3cSysBtmFileLoad_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,6,1))
_H3cSysBtmLoadMaxNumber_Type=Integer32
_H3cSysBtmLoadMaxNumber_Object=MibScalar
h3cSysBtmLoadMaxNumber=_H3cSysBtmLoadMaxNumber_Object((1,3,6,1,4,1,2011,10,2,3,1,6,1,1),_H3cSysBtmLoadMaxNumber_Type())
h3cSysBtmLoadMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysBtmLoadMaxNumber.setStatus(_A)
_H3cSysBtmLoadTable_Object=MibTable
h3cSysBtmLoadTable=_H3cSysBtmLoadTable_Object((1,3,6,1,4,1,2011,10,2,3,1,6,2))
if mibBuilder.loadTexts:h3cSysBtmLoadTable.setStatus(_A)
_H3cSysBtmLoadEntry_Object=MibTableRow
h3cSysBtmLoadEntry=_H3cSysBtmLoadEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,6,2,1))
h3cSysBtmLoadEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:h3cSysBtmLoadEntry.setStatus(_A)
class _H3cSysBtmLoadIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysBtmLoadIndex_Type.__name__=_C
_H3cSysBtmLoadIndex_Object=MibTableColumn
h3cSysBtmLoadIndex=_H3cSysBtmLoadIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,6,2,1,1),_H3cSysBtmLoadIndex_Type())
h3cSysBtmLoadIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysBtmLoadIndex.setStatus(_A)
class _H3cSysBtmFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cSysBtmFileName_Type.__name__=_J
_H3cSysBtmFileName_Object=MibTableColumn
h3cSysBtmFileName=_H3cSysBtmFileName_Object((1,3,6,1,4,1,2011,10,2,3,1,6,2,1,2),_H3cSysBtmFileName_Type())
h3cSysBtmFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysBtmFileName.setStatus(_A)
class _H3cSysBtmFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main',1),(_I,2)))
_H3cSysBtmFileType_Type.__name__=_C
_H3cSysBtmFileType_Object=MibTableColumn
h3cSysBtmFileType=_H3cSysBtmFileType_Object((1,3,6,1,4,1,2011,10,2,3,1,6,2,1,3),_H3cSysBtmFileType_Type())
h3cSysBtmFileType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysBtmFileType.setStatus(_A)
_H3cSysBtmRowStatus_Type=RowStatus
_H3cSysBtmRowStatus_Object=MibTableColumn
h3cSysBtmRowStatus=_H3cSysBtmRowStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,6,2,1,4),_H3cSysBtmRowStatus_Type())
h3cSysBtmRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysBtmRowStatus.setStatus(_A)
class _H3cSysBtmErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalidFile',1),('inProgress',2),(_N,3),(_O,4)))
_H3cSysBtmErrorStatus_Type.__name__=_C
_H3cSysBtmErrorStatus_Object=MibTableColumn
h3cSysBtmErrorStatus=_H3cSysBtmErrorStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,6,2,1,5),_H3cSysBtmErrorStatus_Type())
h3cSysBtmErrorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysBtmErrorStatus.setStatus(_A)
_H3cSysBtmLoadTime_Type=TimeTicks
_H3cSysBtmLoadTime_Object=MibTableColumn
h3cSysBtmLoadTime=_H3cSysBtmLoadTime_Object((1,3,6,1,4,1,2011,10,2,3,1,6,2,1,6),_H3cSysBtmLoadTime_Type())
h3cSysBtmLoadTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysBtmLoadTime.setStatus(_A)
_H3cSysPackage_ObjectIdentity=ObjectIdentity
h3cSysPackage=_H3cSysPackage_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,7))
class _H3cSysPackageNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysPackageNum_Type.__name__=_C
_H3cSysPackageNum_Object=MibScalar
h3cSysPackageNum=_H3cSysPackageNum_Object((1,3,6,1,4,1,2011,10,2,3,1,7,1),_H3cSysPackageNum_Type())
h3cSysPackageNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageNum.setStatus(_A)
_H3cSysPackageTable_Object=MibTable
h3cSysPackageTable=_H3cSysPackageTable_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2))
if mibBuilder.loadTexts:h3cSysPackageTable.setStatus(_A)
_H3cSysPackageEntry_Object=MibTableRow
h3cSysPackageEntry=_H3cSysPackageEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1))
h3cSysPackageEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:h3cSysPackageEntry.setStatus(_A)
class _H3cSysPackageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysPackageIndex_Type.__name__=_C
_H3cSysPackageIndex_Object=MibTableColumn
h3cSysPackageIndex=_H3cSysPackageIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,1),_H3cSysPackageIndex_Type())
h3cSysPackageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysPackageIndex.setStatus(_A)
class _H3cSysPackageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysPackageName_Type.__name__=_E
_H3cSysPackageName_Object=MibTableColumn
h3cSysPackageName=_H3cSysPackageName_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,2),_H3cSysPackageName_Type())
h3cSysPackageName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageName.setStatus(_A)
class _H3cSysPackageSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cSysPackageSize_Type.__name__=_K
_H3cSysPackageSize_Object=MibTableColumn
h3cSysPackageSize=_H3cSysPackageSize_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,3),_H3cSysPackageSize_Type())
h3cSysPackageSize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageSize.setStatus(_A)
class _H3cSysPackageLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysPackageLocation_Type.__name__=_E
_H3cSysPackageLocation_Object=MibTableColumn
h3cSysPackageLocation=_H3cSysPackageLocation_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,4),_H3cSysPackageLocation_Type())
h3cSysPackageLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageLocation.setStatus(_A)
class _H3cSysPackageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('boot',1),(_g,2),(_h,3),('patch',4)))
_H3cSysPackageType_Type.__name__=_C
_H3cSysPackageType_Object=MibTableColumn
h3cSysPackageType=_H3cSysPackageType_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,5),_H3cSysPackageType_Type())
h3cSysPackageType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageType.setStatus(_A)
class _H3cSysPackageAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_P,2),(_Q,3),(_R,4)))
_H3cSysPackageAttribute_Type.__name__=_C
_H3cSysPackageAttribute_Object=MibTableColumn
h3cSysPackageAttribute=_H3cSysPackageAttribute_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,6),_H3cSysPackageAttribute_Type())
h3cSysPackageAttribute.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysPackageAttribute.setStatus(_A)
class _H3cSysPackageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_H3cSysPackageStatus_Type.__name__=_C
_H3cSysPackageStatus_Object=MibTableColumn
h3cSysPackageStatus=_H3cSysPackageStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,7),_H3cSysPackageStatus_Type())
h3cSysPackageStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageStatus.setStatus(_A)
class _H3cSysPackageDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysPackageDescription_Type.__name__=_E
_H3cSysPackageDescription_Object=MibTableColumn
h3cSysPackageDescription=_H3cSysPackageDescription_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,8),_H3cSysPackageDescription_Type())
h3cSysPackageDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageDescription.setStatus(_A)
class _H3cSysPackageFeature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysPackageFeature_Type.__name__=_E
_H3cSysPackageFeature_Object=MibTableColumn
h3cSysPackageFeature=_H3cSysPackageFeature_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,9),_H3cSysPackageFeature_Type())
h3cSysPackageFeature.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageFeature.setStatus(_A)
class _H3cSysPackageVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysPackageVersion_Type.__name__=_E
_H3cSysPackageVersion_Object=MibTableColumn
h3cSysPackageVersion=_H3cSysPackageVersion_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,10),_H3cSysPackageVersion_Type())
h3cSysPackageVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageVersion.setStatus(_A)
class _H3cSysPackageLoadAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_P,2),(_Q,3),(_R,4)))
_H3cSysPackageLoadAttribute_Type.__name__=_C
_H3cSysPackageLoadAttribute_Object=MibTableColumn
h3cSysPackageLoadAttribute=_H3cSysPackageLoadAttribute_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,11),_H3cSysPackageLoadAttribute_Type())
h3cSysPackageLoadAttribute.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysPackageLoadAttribute.setStatus(_A)
class _H3cSysPackageModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cSysPackageModel_Type.__name__=_E
_H3cSysPackageModel_Object=MibTableColumn
h3cSysPackageModel=_H3cSysPackageModel_Object((1,3,6,1,4,1,2011,10,2,3,1,7,2,1,12),_H3cSysPackageModel_Type())
h3cSysPackageModel.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageModel.setStatus(_A)
class _H3cSysPackageOperateEntryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysPackageOperateEntryLimit_Type.__name__=_C
_H3cSysPackageOperateEntryLimit_Object=MibScalar
h3cSysPackageOperateEntryLimit=_H3cSysPackageOperateEntryLimit_Object((1,3,6,1,4,1,2011,10,2,3,1,7,3),_H3cSysPackageOperateEntryLimit_Type())
h3cSysPackageOperateEntryLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysPackageOperateEntryLimit.setStatus(_A)
_H3cSysPackageOperateTable_Object=MibTable
h3cSysPackageOperateTable=_H3cSysPackageOperateTable_Object((1,3,6,1,4,1,2011,10,2,3,1,7,4))
if mibBuilder.loadTexts:h3cSysPackageOperateTable.setStatus(_A)
_H3cSysPackageOperateEntry_Object=MibTableRow
h3cSysPackageOperateEntry=_H3cSysPackageOperateEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,7,4,1))
h3cSysPackageOperateEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:h3cSysPackageOperateEntry.setStatus(_A)
class _H3cSysPackageOperateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysPackageOperateIndex_Type.__name__=_C
_H3cSysPackageOperateIndex_Object=MibTableColumn
h3cSysPackageOperateIndex=_H3cSysPackageOperateIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,7,4,1,1),_H3cSysPackageOperateIndex_Type())
h3cSysPackageOperateIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysPackageOperateIndex.setStatus(_A)
class _H3cSysPackageOperatePackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysPackageOperatePackIndex_Type.__name__=_C
_H3cSysPackageOperatePackIndex_Object=MibTableColumn
h3cSysPackageOperatePackIndex=_H3cSysPackageOperatePackIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,7,4,1,2),_H3cSysPackageOperatePackIndex_Type())
h3cSysPackageOperatePackIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysPackageOperatePackIndex.setStatus(_A)
class _H3cSysPackageOperateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_H3cSysPackageOperateStatus_Type.__name__=_C
_H3cSysPackageOperateStatus_Object=MibTableColumn
h3cSysPackageOperateStatus=_H3cSysPackageOperateStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,7,4,1,3),_H3cSysPackageOperateStatus_Type())
h3cSysPackageOperateStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysPackageOperateStatus.setStatus(_A)
_H3cSysPackageOperateRowStatus_Type=RowStatus
_H3cSysPackageOperateRowStatus_Object=MibTableColumn
h3cSysPackageOperateRowStatus=_H3cSysPackageOperateRowStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,7,4,1,4),_H3cSysPackageOperateRowStatus_Type())
h3cSysPackageOperateRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysPackageOperateRowStatus.setStatus(_A)
class _H3cSysPackageOperateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),('opNotSupport',5)))
_H3cSysPackageOperateResult_Type.__name__=_C
_H3cSysPackageOperateResult_Object=MibTableColumn
h3cSysPackageOperateResult=_H3cSysPackageOperateResult_Object((1,3,6,1,4,1,2011,10,2,3,1,7,4,1,5),_H3cSysPackageOperateResult_Type())
h3cSysPackageOperateResult.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysPackageOperateResult.setStatus(_A)
_H3cSysIpeFile_ObjectIdentity=ObjectIdentity
h3cSysIpeFile=_H3cSysIpeFile_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,8))
class _H3cSysIpeFileNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cSysIpeFileNum_Type.__name__=_C
_H3cSysIpeFileNum_Object=MibScalar
h3cSysIpeFileNum=_H3cSysIpeFileNum_Object((1,3,6,1,4,1,2011,10,2,3,1,8,1),_H3cSysIpeFileNum_Type())
h3cSysIpeFileNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpeFileNum.setStatus(_A)
_H3cSysIpeFileTable_Object=MibTable
h3cSysIpeFileTable=_H3cSysIpeFileTable_Object((1,3,6,1,4,1,2011,10,2,3,1,8,2))
if mibBuilder.loadTexts:h3cSysIpeFileTable.setStatus(_A)
_H3cSysIpeFileEntry_Object=MibTableRow
h3cSysIpeFileEntry=_H3cSysIpeFileEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,8,2,1))
h3cSysIpeFileEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:h3cSysIpeFileEntry.setStatus(_A)
class _H3cSysIpeFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysIpeFileIndex_Type.__name__=_C
_H3cSysIpeFileIndex_Object=MibTableColumn
h3cSysIpeFileIndex=_H3cSysIpeFileIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,8,2,1,1),_H3cSysIpeFileIndex_Type())
h3cSysIpeFileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysIpeFileIndex.setStatus(_A)
class _H3cSysIpeFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysIpeFileName_Type.__name__=_E
_H3cSysIpeFileName_Object=MibTableColumn
h3cSysIpeFileName=_H3cSysIpeFileName_Object((1,3,6,1,4,1,2011,10,2,3,1,8,2,1,2),_H3cSysIpeFileName_Type())
h3cSysIpeFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpeFileName.setStatus(_A)
class _H3cSysIpeFileSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cSysIpeFileSize_Type.__name__=_K
_H3cSysIpeFileSize_Object=MibTableColumn
h3cSysIpeFileSize=_H3cSysIpeFileSize_Object((1,3,6,1,4,1,2011,10,2,3,1,8,2,1,3),_H3cSysIpeFileSize_Type())
h3cSysIpeFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpeFileSize.setStatus(_A)
class _H3cSysIpeFileLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysIpeFileLocation_Type.__name__=_E
_H3cSysIpeFileLocation_Object=MibTableColumn
h3cSysIpeFileLocation=_H3cSysIpeFileLocation_Object((1,3,6,1,4,1,2011,10,2,3,1,8,2,1,4),_H3cSysIpeFileLocation_Type())
h3cSysIpeFileLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpeFileLocation.setStatus(_A)
_H3cSysIpeFileModel_Type=SnmpTagList
_H3cSysIpeFileModel_Object=MibTableColumn
h3cSysIpeFileModel=_H3cSysIpeFileModel_Object((1,3,6,1,4,1,2011,10,2,3,1,8,2,1,5),_H3cSysIpeFileModel_Type())
h3cSysIpeFileModel.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpeFileModel.setStatus(_A)
_H3cSysIpePackageTable_Object=MibTable
h3cSysIpePackageTable=_H3cSysIpePackageTable_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3))
if mibBuilder.loadTexts:h3cSysIpePackageTable.setStatus(_A)
_H3cSysIpePackageEntry_Object=MibTableRow
h3cSysIpePackageEntry=_H3cSysIpePackageEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1))
h3cSysIpePackageEntry.setIndexNames((0,_B,_S),(0,_B,_p))
if mibBuilder.loadTexts:h3cSysIpePackageEntry.setStatus(_A)
class _H3cSysIpePackageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysIpePackageIndex_Type.__name__=_C
_H3cSysIpePackageIndex_Object=MibTableColumn
h3cSysIpePackageIndex=_H3cSysIpePackageIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1,1),_H3cSysIpePackageIndex_Type())
h3cSysIpePackageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysIpePackageIndex.setStatus(_A)
class _H3cSysIpePackageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysIpePackageName_Type.__name__=_E
_H3cSysIpePackageName_Object=MibTableColumn
h3cSysIpePackageName=_H3cSysIpePackageName_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1,2),_H3cSysIpePackageName_Type())
h3cSysIpePackageName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpePackageName.setStatus(_A)
class _H3cSysIpePackageSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cSysIpePackageSize_Type.__name__=_K
_H3cSysIpePackageSize_Object=MibTableColumn
h3cSysIpePackageSize=_H3cSysIpePackageSize_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1,3),_H3cSysIpePackageSize_Type())
h3cSysIpePackageSize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpePackageSize.setStatus(_A)
class _H3cSysIpePackageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('boot',1),(_g,2),(_h,3),('patch',4)))
_H3cSysIpePackageType_Type.__name__=_C
_H3cSysIpePackageType_Object=MibTableColumn
h3cSysIpePackageType=_H3cSysIpePackageType_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1,4),_H3cSysIpePackageType_Type())
h3cSysIpePackageType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpePackageType.setStatus(_A)
class _H3cSysIpePackageDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysIpePackageDescription_Type.__name__=_E
_H3cSysIpePackageDescription_Object=MibTableColumn
h3cSysIpePackageDescription=_H3cSysIpePackageDescription_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1,5),_H3cSysIpePackageDescription_Type())
h3cSysIpePackageDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpePackageDescription.setStatus(_A)
class _H3cSysIpePackageFeature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysIpePackageFeature_Type.__name__=_E
_H3cSysIpePackageFeature_Object=MibTableColumn
h3cSysIpePackageFeature=_H3cSysIpePackageFeature_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1,6),_H3cSysIpePackageFeature_Type())
h3cSysIpePackageFeature.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpePackageFeature.setStatus(_A)
class _H3cSysIpePackageVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysIpePackageVersion_Type.__name__=_E
_H3cSysIpePackageVersion_Object=MibTableColumn
h3cSysIpePackageVersion=_H3cSysIpePackageVersion_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1,7),_H3cSysIpePackageVersion_Type())
h3cSysIpePackageVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpePackageVersion.setStatus(_A)
class _H3cSysIpePackageModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cSysIpePackageModel_Type.__name__=_E
_H3cSysIpePackageModel_Object=MibTableColumn
h3cSysIpePackageModel=_H3cSysIpePackageModel_Object((1,3,6,1,4,1,2011,10,2,3,1,8,3,1,8),_H3cSysIpePackageModel_Type())
h3cSysIpePackageModel.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpePackageModel.setStatus(_A)
_H3cSysIpeFileOperateTable_Object=MibTable
h3cSysIpeFileOperateTable=_H3cSysIpeFileOperateTable_Object((1,3,6,1,4,1,2011,10,2,3,1,8,4))
if mibBuilder.loadTexts:h3cSysIpeFileOperateTable.setStatus(_A)
_H3cSysIpeFileOperateEntry_Object=MibTableRow
h3cSysIpeFileOperateEntry=_H3cSysIpeFileOperateEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,8,4,1))
h3cSysIpeFileOperateEntry.setIndexNames((0,_B,_q))
if mibBuilder.loadTexts:h3cSysIpeFileOperateEntry.setStatus(_A)
class _H3cSysIpeFileOperateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysIpeFileOperateIndex_Type.__name__=_C
_H3cSysIpeFileOperateIndex_Object=MibTableColumn
h3cSysIpeFileOperateIndex=_H3cSysIpeFileOperateIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,8,4,1,1),_H3cSysIpeFileOperateIndex_Type())
h3cSysIpeFileOperateIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysIpeFileOperateIndex.setStatus(_A)
class _H3cSysIpeFileOperateFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysIpeFileOperateFileIndex_Type.__name__=_C
_H3cSysIpeFileOperateFileIndex_Object=MibTableColumn
h3cSysIpeFileOperateFileIndex=_H3cSysIpeFileOperateFileIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,8,4,1,2),_H3cSysIpeFileOperateFileIndex_Type())
h3cSysIpeFileOperateFileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysIpeFileOperateFileIndex.setStatus(_A)
class _H3cSysIpeFileOperateAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_P,2),(_Q,3),(_R,4)))
_H3cSysIpeFileOperateAttribute_Type.__name__=_C
_H3cSysIpeFileOperateAttribute_Object=MibTableColumn
h3cSysIpeFileOperateAttribute=_H3cSysIpeFileOperateAttribute_Object((1,3,6,1,4,1,2011,10,2,3,1,8,4,1,3),_H3cSysIpeFileOperateAttribute_Type())
h3cSysIpeFileOperateAttribute.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysIpeFileOperateAttribute.setStatus(_A)
_H3cSysIpeFileOperateRowStatus_Type=RowStatus
_H3cSysIpeFileOperateRowStatus_Object=MibTableColumn
h3cSysIpeFileOperateRowStatus=_H3cSysIpeFileOperateRowStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,8,4,1,4),_H3cSysIpeFileOperateRowStatus_Type())
h3cSysIpeFileOperateRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysIpeFileOperateRowStatus.setStatus(_A)
class _H3cSysIpeFileOperateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),('opDeviceFull',5),('opFileOpenError',6)))
_H3cSysIpeFileOperateResult_Type.__name__=_C
_H3cSysIpeFileOperateResult_Object=MibTableColumn
h3cSysIpeFileOperateResult=_H3cSysIpeFileOperateResult_Object((1,3,6,1,4,1,2011,10,2,3,1,8,4,1,5),_H3cSysIpeFileOperateResult_Type())
h3cSysIpeFileOperateResult.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysIpeFileOperateResult.setStatus(_A)
_H3cSysSetBootImage_ObjectIdentity=ObjectIdentity
h3cSysSetBootImage=_H3cSysSetBootImage_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,9))
_H3cSysSetBootImageOp_ObjectIdentity=ObjectIdentity
h3cSysSetBootImageOp=_H3cSysSetBootImageOp_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,1,9,1))
class _H3cSysSetBootImageAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,1),('done',2),('bootLoadPrimary',3),('bootLoadSecondary',4),('bootLoadPrimarySecondary',5),('bootPrimary',6),('bootSecondary',7),('bootPrimarySecondary',8),('loadPrimary',9),('loadSecondary',10),('loadPrimarySecondary',11)))
_H3cSysSetBootImageAction_Type.__name__=_C
_H3cSysSetBootImageAction_Object=MibScalar
h3cSysSetBootImageAction=_H3cSysSetBootImageAction_Object((1,3,6,1,4,1,2011,10,2,3,1,9,1,1),_H3cSysSetBootImageAction_Type())
h3cSysSetBootImageAction.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysSetBootImageAction.setStatus(_A)
class _H3cSysSetBootImageFileOverWrite_Type(TruthValue):defaultValue=2
_H3cSysSetBootImageFileOverWrite_Type.__name__=_M
_H3cSysSetBootImageFileOverWrite_Object=MibScalar
h3cSysSetBootImageFileOverWrite=_H3cSysSetBootImageFileOverWrite_Object((1,3,6,1,4,1,2011,10,2,3,1,9,1,2),_H3cSysSetBootImageFileOverWrite_Type())
h3cSysSetBootImageFileOverWrite.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysSetBootImageFileOverWrite.setStatus(_A)
class _H3cSysSetBootImageRemoveIpeFile_Type(TruthValue):defaultValue=2
_H3cSysSetBootImageRemoveIpeFile_Type.__name__=_M
_H3cSysSetBootImageRemoveIpeFile_Object=MibScalar
h3cSysSetBootImageRemoveIpeFile=_H3cSysSetBootImageRemoveIpeFile_Object((1,3,6,1,4,1,2011,10,2,3,1,9,1,3),_H3cSysSetBootImageRemoveIpeFile_Type())
h3cSysSetBootImageRemoveIpeFile.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSysSetBootImageRemoveIpeFile.setStatus(_A)
class _H3cSysSetBootImageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('doing',2),(_N,3),(_O,4)))
_H3cSysSetBootImageStatus_Type.__name__=_C
_H3cSysSetBootImageStatus_Object=MibScalar
h3cSysSetBootImageStatus=_H3cSysSetBootImageStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,9,1,4),_H3cSysSetBootImageStatus_Type())
h3cSysSetBootImageStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysSetBootImageStatus.setStatus(_A)
class _H3cSysSetBootImageFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysSetBootImageFailedReason_Type.__name__=_E
_H3cSysSetBootImageFailedReason_Object=MibScalar
h3cSysSetBootImageFailedReason=_H3cSysSetBootImageFailedReason_Object((1,3,6,1,4,1,2011,10,2,3,1,9,1,5),_H3cSysSetBootImageFailedReason_Type())
h3cSysSetBootImageFailedReason.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysSetBootImageFailedReason.setStatus(_A)
_H3cSysBootPackageTable_Object=MibTable
h3cSysBootPackageTable=_H3cSysBootPackageTable_Object((1,3,6,1,4,1,2011,10,2,3,1,9,2))
if mibBuilder.loadTexts:h3cSysBootPackageTable.setStatus(_A)
_H3cSysBootPackageEntry_Object=MibTableRow
h3cSysBootPackageEntry=_H3cSysBootPackageEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,9,2,1))
h3cSysBootPackageEntry.setIndexNames((0,_B,_r))
if mibBuilder.loadTexts:h3cSysBootPackageEntry.setStatus(_A)
class _H3cSysBootPackageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysBootPackageIndex_Type.__name__=_C
_H3cSysBootPackageIndex_Object=MibTableColumn
h3cSysBootPackageIndex=_H3cSysBootPackageIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,9,2,1,1),_H3cSysBootPackageIndex_Type())
h3cSysBootPackageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysBootPackageIndex.setStatus(_A)
_H3cSysBootPackageRowStatus_Type=RowStatus
_H3cSysBootPackageRowStatus_Object=MibTableColumn
h3cSysBootPackageRowStatus=_H3cSysBootPackageRowStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,9,2,1,2),_H3cSysBootPackageRowStatus_Type())
h3cSysBootPackageRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysBootPackageRowStatus.setStatus(_A)
_H3cSysBootIpeTable_Object=MibTable
h3cSysBootIpeTable=_H3cSysBootIpeTable_Object((1,3,6,1,4,1,2011,10,2,3,1,9,3))
if mibBuilder.loadTexts:h3cSysBootIpeTable.setStatus(_A)
_H3cSysBootIpeEntry_Object=MibTableRow
h3cSysBootIpeEntry=_H3cSysBootIpeEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,9,3,1))
h3cSysBootIpeEntry.setIndexNames((0,_B,_s))
if mibBuilder.loadTexts:h3cSysBootIpeEntry.setStatus(_A)
class _H3cSysBootIpeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSysBootIpeIndex_Type.__name__=_C
_H3cSysBootIpeIndex_Object=MibTableColumn
h3cSysBootIpeIndex=_H3cSysBootIpeIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,9,3,1,1),_H3cSysBootIpeIndex_Type())
h3cSysBootIpeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysBootIpeIndex.setStatus(_A)
_H3cSysBootIpeRowStatus_Type=RowStatus
_H3cSysBootIpeRowStatus_Object=MibTableColumn
h3cSysBootIpeRowStatus=_H3cSysBootIpeRowStatus_Object((1,3,6,1,4,1,2011,10,2,3,1,9,3,1,2),_H3cSysBootIpeRowStatus_Type())
h3cSysBootIpeRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSysBootIpeRowStatus.setStatus(_A)
_H3cSysSetBootImageResultTable_Object=MibTable
h3cSysSetBootImageResultTable=_H3cSysSetBootImageResultTable_Object((1,3,6,1,4,1,2011,10,2,3,1,9,4))
if mibBuilder.loadTexts:h3cSysSetBootImageResultTable.setStatus(_A)
_H3cSysSetBootImageResultEntry_Object=MibTableRow
h3cSysSetBootImageResultEntry=_H3cSysSetBootImageResultEntry_Object((1,3,6,1,4,1,2011,10,2,3,1,9,4,1))
h3cSysSetBootImageResultEntry.setIndexNames((0,_B,_t))
if mibBuilder.loadTexts:h3cSysSetBootImageResultEntry.setStatus(_A)
class _H3cSysSetBootImageResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cSysSetBootImageResultIndex_Type.__name__=_C
_H3cSysSetBootImageResultIndex_Object=MibTableColumn
h3cSysSetBootImageResultIndex=_H3cSysSetBootImageResultIndex_Object((1,3,6,1,4,1,2011,10,2,3,1,9,4,1,1),_H3cSysSetBootImageResultIndex_Type())
h3cSysSetBootImageResultIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSysSetBootImageResultIndex.setStatus(_A)
class _H3cSysSetBootImageResultStatusOfEachCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('doing',2),(_N,3),(_O,4)))
_H3cSysSetBootImageResultStatusOfEachCard_Type.__name__=_C
_H3cSysSetBootImageResultStatusOfEachCard_Object=MibTableColumn
h3cSysSetBootImageResultStatusOfEachCard=_H3cSysSetBootImageResultStatusOfEachCard_Object((1,3,6,1,4,1,2011,10,2,3,1,9,4,1,2),_H3cSysSetBootImageResultStatusOfEachCard_Type())
h3cSysSetBootImageResultStatusOfEachCard.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysSetBootImageResultStatusOfEachCard.setStatus(_A)
class _H3cSysSetBootImageFailedReasonOfEachCard_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSysSetBootImageFailedReasonOfEachCard_Type.__name__=_E
_H3cSysSetBootImageFailedReasonOfEachCard_Object=MibTableColumn
h3cSysSetBootImageFailedReasonOfEachCard=_H3cSysSetBootImageFailedReasonOfEachCard_Object((1,3,6,1,4,1,2011,10,2,3,1,9,4,1,3),_H3cSysSetBootImageFailedReasonOfEachCard_Type())
h3cSysSetBootImageFailedReasonOfEachCard.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSysSetBootImageFailedReasonOfEachCard.setStatus(_A)
_H3cSystemManMIBNotifications_ObjectIdentity=ObjectIdentity
h3cSystemManMIBNotifications=_H3cSystemManMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,2))
_H3cSystemManMIBConformance_ObjectIdentity=ObjectIdentity
h3cSystemManMIBConformance=_H3cSystemManMIBConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,3))
_H3cSystemManMIBCompliances_ObjectIdentity=ObjectIdentity
h3cSystemManMIBCompliances=_H3cSystemManMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,3,1))
_H3cSystemManMIBGroups_ObjectIdentity=ObjectIdentity
h3cSystemManMIBGroups=_H3cSystemManMIBGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,3,3,2))
h3cSysClockGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,3,3,2,1))
h3cSysClockGroup.setObjects(*((_B,_T),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:h3cSysClockGroup.setStatus(_A)
h3cSysReloadGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,3,3,2,2))
h3cSysReloadGroup.setObjects(*((_B,_A0),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_A1),(_B,_A2),(_B,_Y),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:h3cSysReloadGroup.setStatus(_A)
h3cSysImageGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,3,3,2,3))
h3cSysImageGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_Z)))
if mibBuilder.loadTexts:h3cSysImageGroup.setStatus(_A)
h3cSysCFGFileGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,3,3,2,4))
h3cSysCFGFileGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:h3cSysCFGFileGroup.setStatus(_A)
h3cSysCurGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,3,3,2,5))
h3cSysCurGroup.setObjects(*((_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:h3cSysCurGroup.setStatus(_A)
h3cSystemBtmLoadGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,3,3,2,7))
h3cSystemBtmLoadGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:h3cSystemBtmLoadGroup.setStatus(_A)
h3cSysClockChangedNotification=NotificationType((1,3,6,1,4,1,2011,10,2,3,2,1))
h3cSysClockChangedNotification.setObjects((_B,_T))
if mibBuilder.loadTexts:h3cSysClockChangedNotification.setStatus(_A)
h3cSysReloadNotification=NotificationType((1,3,6,1,4,1,2011,10,2,3,2,2))
h3cSysReloadNotification.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_U)))
if mibBuilder.loadTexts:h3cSysReloadNotification.setStatus(_A)
h3cSysStartUpNotification=NotificationType((1,3,6,1,4,1,2011,10,2,3,2,3))
h3cSysStartUpNotification.setObjects((_B,_Z))
if mibBuilder.loadTexts:h3cSysStartUpNotification.setStatus(_A)
h3cSystemManNotificationGroup=NotificationGroup((1,3,6,1,4,1,2011,10,2,3,3,2,6))
h3cSystemManNotificationGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:h3cSystemManNotificationGroup.setStatus(_A)
h3cSystemManMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,3,3,1,1))
h3cSystemManMIBCompliance.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:h3cSystemManMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cSystemMan':h3cSystemMan,'h3cSystemManMIBObjects':h3cSystemManMIBObjects,'h3cSysClock':h3cSysClock,_T:h3cSysLocalClock,'h3cSysSummerTime':h3cSysSummerTime,_u:h3cSysSummerTimeEnable,_v:h3cSysSummerTimeZone,_w:h3cSysSummerTimeMethod,_x:h3cSysSummerTimeStart,_y:h3cSysSummerTimeEnd,_z:h3cSysSummerTimeOffset,'h3cSysLocalClockString':h3cSysLocalClockString,'h3cSysClockProtocolGroup':h3cSysClockProtocolGroup,'h3cSysClockProtocol':h3cSysClockProtocol,'h3cSysClockProtocolSrcMdc':h3cSysClockProtocolSrcMdc,'h3cSysClockProtocolSrcContext':h3cSysClockProtocolSrcContext,'h3cSysLocalClockString2':h3cSysLocalClockString2,'h3cSysCurrent':h3cSysCurrent,'h3cSysCurTable':h3cSysCurTable,'h3cSysCurEntry':h3cSysCurEntry,_a:h3cSysCurEntPhysicalIndex,_AD:h3cSysCurCFGFileIndex,_AE:h3cSysCurImageIndex,_AF:h3cSysCurBtmFileName,_AG:h3cSysCurUpdateBtmFileName,'h3cSysReload':h3cSysReload,_A0:h3cSysReloadSchedule,_U:h3cSysReloadAction,'h3cSysReloadScheduleTable':h3cSysReloadScheduleTable,'h3cSysReloadScheduleEntry':h3cSysReloadScheduleEntry,_b:h3cSysReloadScheduleIndex,_A3:h3cSysReloadEntity,_W:h3cSysReloadCfgFile,_V:h3cSysReloadImage,_X:h3cSysReloadReason,_Y:h3cSysReloadScheduleTime,_A4:h3cSysReloadRowStatus,_A1:h3cSysReloadScheduleTagList,_A2:h3cSysReloadTag,'h3cSysImage':h3cSysImage,_A5:h3cSysImageNum,'h3cSysImageTable':h3cSysImageTable,'h3cSysImageEntry':h3cSysImageEntry,_c:h3cSysImageIndex,_A6:h3cSysImageName,_A7:h3cSysImageSize,_A8:h3cSysImageLocation,_Z:h3cSysImageType,'h3cSysCFGFile':h3cSysCFGFile,_A9:h3cSysCFGFileNum,'h3cSysCFGFileTable':h3cSysCFGFileTable,'h3cSysCFGFileEntry':h3cSysCFGFileEntry,_d:h3cSysCFGFileIndex,_AA:h3cSysCFGFileName,_AB:h3cSysCFGFileSize,_AC:h3cSysCFGFileLocation,'h3cSysBtmFile':h3cSysBtmFile,'h3cSysBtmFileLoad':h3cSysBtmFileLoad,_AH:h3cSysBtmLoadMaxNumber,'h3cSysBtmLoadTable':h3cSysBtmLoadTable,'h3cSysBtmLoadEntry':h3cSysBtmLoadEntry,_e:h3cSysBtmLoadIndex,_AI:h3cSysBtmFileName,_AJ:h3cSysBtmFileType,_AK:h3cSysBtmRowStatus,_AL:h3cSysBtmErrorStatus,_AM:h3cSysBtmLoadTime,'h3cSysPackage':h3cSysPackage,'h3cSysPackageNum':h3cSysPackageNum,'h3cSysPackageTable':h3cSysPackageTable,'h3cSysPackageEntry':h3cSysPackageEntry,_f:h3cSysPackageIndex,'h3cSysPackageName':h3cSysPackageName,'h3cSysPackageSize':h3cSysPackageSize,'h3cSysPackageLocation':h3cSysPackageLocation,'h3cSysPackageType':h3cSysPackageType,'h3cSysPackageAttribute':h3cSysPackageAttribute,'h3cSysPackageStatus':h3cSysPackageStatus,'h3cSysPackageDescription':h3cSysPackageDescription,'h3cSysPackageFeature':h3cSysPackageFeature,'h3cSysPackageVersion':h3cSysPackageVersion,'h3cSysPackageLoadAttribute':h3cSysPackageLoadAttribute,'h3cSysPackageModel':h3cSysPackageModel,'h3cSysPackageOperateEntryLimit':h3cSysPackageOperateEntryLimit,'h3cSysPackageOperateTable':h3cSysPackageOperateTable,'h3cSysPackageOperateEntry':h3cSysPackageOperateEntry,_k:h3cSysPackageOperateIndex,'h3cSysPackageOperatePackIndex':h3cSysPackageOperatePackIndex,'h3cSysPackageOperateStatus':h3cSysPackageOperateStatus,'h3cSysPackageOperateRowStatus':h3cSysPackageOperateRowStatus,'h3cSysPackageOperateResult':h3cSysPackageOperateResult,'h3cSysIpeFile':h3cSysIpeFile,'h3cSysIpeFileNum':h3cSysIpeFileNum,'h3cSysIpeFileTable':h3cSysIpeFileTable,'h3cSysIpeFileEntry':h3cSysIpeFileEntry,_S:h3cSysIpeFileIndex,'h3cSysIpeFileName':h3cSysIpeFileName,'h3cSysIpeFileSize':h3cSysIpeFileSize,'h3cSysIpeFileLocation':h3cSysIpeFileLocation,'h3cSysIpeFileModel':h3cSysIpeFileModel,'h3cSysIpePackageTable':h3cSysIpePackageTable,'h3cSysIpePackageEntry':h3cSysIpePackageEntry,_p:h3cSysIpePackageIndex,'h3cSysIpePackageName':h3cSysIpePackageName,'h3cSysIpePackageSize':h3cSysIpePackageSize,'h3cSysIpePackageType':h3cSysIpePackageType,'h3cSysIpePackageDescription':h3cSysIpePackageDescription,'h3cSysIpePackageFeature':h3cSysIpePackageFeature,'h3cSysIpePackageVersion':h3cSysIpePackageVersion,'h3cSysIpePackageModel':h3cSysIpePackageModel,'h3cSysIpeFileOperateTable':h3cSysIpeFileOperateTable,'h3cSysIpeFileOperateEntry':h3cSysIpeFileOperateEntry,_q:h3cSysIpeFileOperateIndex,'h3cSysIpeFileOperateFileIndex':h3cSysIpeFileOperateFileIndex,'h3cSysIpeFileOperateAttribute':h3cSysIpeFileOperateAttribute,'h3cSysIpeFileOperateRowStatus':h3cSysIpeFileOperateRowStatus,'h3cSysIpeFileOperateResult':h3cSysIpeFileOperateResult,'h3cSysSetBootImage':h3cSysSetBootImage,'h3cSysSetBootImageOp':h3cSysSetBootImageOp,'h3cSysSetBootImageAction':h3cSysSetBootImageAction,'h3cSysSetBootImageFileOverWrite':h3cSysSetBootImageFileOverWrite,'h3cSysSetBootImageRemoveIpeFile':h3cSysSetBootImageRemoveIpeFile,'h3cSysSetBootImageStatus':h3cSysSetBootImageStatus,'h3cSysSetBootImageFailedReason':h3cSysSetBootImageFailedReason,'h3cSysBootPackageTable':h3cSysBootPackageTable,'h3cSysBootPackageEntry':h3cSysBootPackageEntry,_r:h3cSysBootPackageIndex,'h3cSysBootPackageRowStatus':h3cSysBootPackageRowStatus,'h3cSysBootIpeTable':h3cSysBootIpeTable,'h3cSysBootIpeEntry':h3cSysBootIpeEntry,_s:h3cSysBootIpeIndex,'h3cSysBootIpeRowStatus':h3cSysBootIpeRowStatus,'h3cSysSetBootImageResultTable':h3cSysSetBootImageResultTable,'h3cSysSetBootImageResultEntry':h3cSysSetBootImageResultEntry,_t:h3cSysSetBootImageResultIndex,'h3cSysSetBootImageResultStatusOfEachCard':h3cSysSetBootImageResultStatusOfEachCard,'h3cSysSetBootImageFailedReasonOfEachCard':h3cSysSetBootImageFailedReasonOfEachCard,'h3cSystemManMIBNotifications':h3cSystemManMIBNotifications,_AN:h3cSysClockChangedNotification,_AO:h3cSysReloadNotification,_AP:h3cSysStartUpNotification,'h3cSystemManMIBConformance':h3cSystemManMIBConformance,'h3cSystemManMIBCompliances':h3cSystemManMIBCompliances,'h3cSystemManMIBCompliance':h3cSystemManMIBCompliance,'h3cSystemManMIBGroups':h3cSystemManMIBGroups,_AQ:h3cSysClockGroup,_AR:h3cSysReloadGroup,_AS:h3cSysImageGroup,_AT:h3cSysCFGFileGroup,_AV:h3cSysCurGroup,_AU:h3cSystemManNotificationGroup,_AW:h3cSystemBtmLoadGroup})