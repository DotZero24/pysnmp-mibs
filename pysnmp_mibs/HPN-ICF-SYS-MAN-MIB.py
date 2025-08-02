_AW='hpnicfSystemBtmLoadGroup'
_AV='hpnicfSysCurGroup'
_AU='hpnicfSystemManNotificationGroup'
_AT='hpnicfSysCFGFileGroup'
_AS='hpnicfSysImageGroup'
_AR='hpnicfSysReloadGroup'
_AQ='hpnicfSysClockGroup'
_AP='hpnicfSysStartUpNotification'
_AO='hpnicfSysReloadNotification'
_AN='hpnicfSysClockChangedNotification'
_AM='hpnicfSysBtmLoadTime'
_AL='hpnicfSysBtmErrorStatus'
_AK='hpnicfSysBtmRowStatus'
_AJ='hpnicfSysBtmFileType'
_AI='hpnicfSysBtmFileName'
_AH='hpnicfSysBtmLoadMaxNumber'
_AG='hpnicfSysCurUpdateBtmFileName'
_AF='hpnicfSysCurBtmFileName'
_AE='hpnicfSysCurImageIndex'
_AD='hpnicfSysCurCFGFileIndex'
_AC='hpnicfSysCFGFileLocation'
_AB='hpnicfSysCFGFileSize'
_AA='hpnicfSysCFGFileName'
_A9='hpnicfSysCFGFileNum'
_A8='hpnicfSysImageLocation'
_A7='hpnicfSysImageSize'
_A6='hpnicfSysImageName'
_A5='hpnicfSysImageNum'
_A4='hpnicfSysReloadRowStatus'
_A3='hpnicfSysReloadEntity'
_A2='hpnicfSysReloadTag'
_A1='hpnicfSysReloadScheduleTagList'
_A0='hpnicfSysReloadSchedule'
_z='hpnicfSysSummerTimeOffset'
_y='hpnicfSysSummerTimeEnd'
_x='hpnicfSysSummerTimeStart'
_w='hpnicfSysSummerTimeMethod'
_v='hpnicfSysSummerTimeZone'
_u='hpnicfSysSummerTimeEnable'
_t='hpnicfSysSetBootImageResultIndex'
_s='hpnicfSysBootIpeIndex'
_r='hpnicfSysBootPackageIndex'
_q='hpnicfSysIpeFileOperateIndex'
_p='hpnicfSysIpePackageIndex'
_o='opInvalidFile'
_n='opUnknownFailure'
_m='opSuccess'
_l='opInProgress'
_k='hpnicfSysPackageOperateIndex'
_j='inactive'
_i='active'
_h='feature'
_g='system'
_f='hpnicfSysPackageIndex'
_e='hpnicfSysBtmLoadIndex'
_d='hpnicfSysCFGFileIndex'
_c='hpnicfSysImageIndex'
_b='hpnicfSysReloadScheduleIndex'
_a='hpnicfSysCurEntPhysicalIndex'
_Z='hpnicfSysImageType'
_Y='hpnicfSysReloadScheduleTime'
_X='hpnicfSysReloadReason'
_W='hpnicfSysReloadCfgFile'
_V='hpnicfSysReloadImage'
_U='hpnicfSysReloadAction'
_T='hpnicfSysLocalClock'
_S='hpnicfSysIpeFileIndex'
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
_G='read-write'
_F='read-create'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='HPN-ICF-SYS-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
SnmpTagList,SnmpTagValue=mibBuilder.importSymbols('SNMP-TARGET-MIB','SnmpTagList','SnmpTagValue')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,_E,'PhysAddress','RowStatus','TextualConvention',_M)
hpnicfSystemMan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3))
if mibBuilder.loadTexts:hpnicfSystemMan.setRevisions(('2004-04-08 13:45',))
_HpnicfSystemManMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfSystemManMIBObjects=_HpnicfSystemManMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1))
_HpnicfSysClock_ObjectIdentity=ObjectIdentity
hpnicfSysClock=_HpnicfSysClock_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1))
_HpnicfSysLocalClock_Type=DateAndTime
_HpnicfSysLocalClock_Object=MibScalar
hpnicfSysLocalClock=_HpnicfSysLocalClock_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,1),_HpnicfSysLocalClock_Type())
hpnicfSysLocalClock.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysLocalClock.setStatus(_A)
_HpnicfSysSummerTime_ObjectIdentity=ObjectIdentity
hpnicfSysSummerTime=_HpnicfSysSummerTime_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,2))
class _HpnicfSysSummerTimeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpnicfSysSummerTimeEnable_Type.__name__=_C
_HpnicfSysSummerTimeEnable_Object=MibScalar
hpnicfSysSummerTimeEnable=_HpnicfSysSummerTimeEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,2,1),_HpnicfSysSummerTimeEnable_Type())
hpnicfSysSummerTimeEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysSummerTimeEnable.setStatus(_A)
class _HpnicfSysSummerTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysSummerTimeZone_Type.__name__=_E
_HpnicfSysSummerTimeZone_Object=MibScalar
hpnicfSysSummerTimeZone=_HpnicfSysSummerTimeZone_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,2,2),_HpnicfSysSummerTimeZone_Type())
hpnicfSysSummerTimeZone.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysSummerTimeZone.setStatus(_A)
class _HpnicfSysSummerTimeMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneOff',1),('repeating',2)))
_HpnicfSysSummerTimeMethod_Type.__name__=_C
_HpnicfSysSummerTimeMethod_Object=MibScalar
hpnicfSysSummerTimeMethod=_HpnicfSysSummerTimeMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,2,3),_HpnicfSysSummerTimeMethod_Type())
hpnicfSysSummerTimeMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysSummerTimeMethod.setStatus(_A)
class _HpnicfSysSummerTimeStart_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpnicfSysSummerTimeStart_Type.__name__=_L
_HpnicfSysSummerTimeStart_Object=MibScalar
hpnicfSysSummerTimeStart=_HpnicfSysSummerTimeStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,2,4),_HpnicfSysSummerTimeStart_Type())
hpnicfSysSummerTimeStart.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysSummerTimeStart.setStatus(_A)
class _HpnicfSysSummerTimeEnd_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpnicfSysSummerTimeEnd_Type.__name__=_L
_HpnicfSysSummerTimeEnd_Object=MibScalar
hpnicfSysSummerTimeEnd=_HpnicfSysSummerTimeEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,2,5),_HpnicfSysSummerTimeEnd_Type())
hpnicfSysSummerTimeEnd.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysSummerTimeEnd.setStatus(_A)
class _HpnicfSysSummerTimeOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86399))
_HpnicfSysSummerTimeOffset_Type.__name__=_C
_HpnicfSysSummerTimeOffset_Object=MibScalar
hpnicfSysSummerTimeOffset=_HpnicfSysSummerTimeOffset_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,2,6),_HpnicfSysSummerTimeOffset_Type())
hpnicfSysSummerTimeOffset.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysSummerTimeOffset.setStatus(_A)
class _HpnicfSysLocalClockString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,24))
_HpnicfSysLocalClockString_Type.__name__=_J
_HpnicfSysLocalClockString_Object=MibScalar
hpnicfSysLocalClockString=_HpnicfSysLocalClockString_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,1,3),_HpnicfSysLocalClockString_Type())
hpnicfSysLocalClockString.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysLocalClockString.setStatus(_A)
_HpnicfSysCurrent_ObjectIdentity=ObjectIdentity
hpnicfSysCurrent=_HpnicfSysCurrent_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,2))
_HpnicfSysCurTable_Object=MibTable
hpnicfSysCurTable=_HpnicfSysCurTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,2,1))
if mibBuilder.loadTexts:hpnicfSysCurTable.setStatus(_A)
_HpnicfSysCurEntry_Object=MibTableRow
hpnicfSysCurEntry=_HpnicfSysCurEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,2,1,1))
hpnicfSysCurEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:hpnicfSysCurEntry.setStatus(_A)
class _HpnicfSysCurEntPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysCurEntPhysicalIndex_Type.__name__=_C
_HpnicfSysCurEntPhysicalIndex_Object=MibTableColumn
hpnicfSysCurEntPhysicalIndex=_HpnicfSysCurEntPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,2,1,1,1),_HpnicfSysCurEntPhysicalIndex_Type())
hpnicfSysCurEntPhysicalIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysCurEntPhysicalIndex.setStatus(_A)
class _HpnicfSysCurCFGFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysCurCFGFileIndex_Type.__name__=_C
_HpnicfSysCurCFGFileIndex_Object=MibTableColumn
hpnicfSysCurCFGFileIndex=_HpnicfSysCurCFGFileIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,2,1,1,2),_HpnicfSysCurCFGFileIndex_Type())
hpnicfSysCurCFGFileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysCurCFGFileIndex.setStatus(_A)
class _HpnicfSysCurImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysCurImageIndex_Type.__name__=_C
_HpnicfSysCurImageIndex_Object=MibTableColumn
hpnicfSysCurImageIndex=_HpnicfSysCurImageIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,2,1,1,3),_HpnicfSysCurImageIndex_Type())
hpnicfSysCurImageIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysCurImageIndex.setStatus(_A)
class _HpnicfSysCurBtmFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfSysCurBtmFileName_Type.__name__=_J
_HpnicfSysCurBtmFileName_Object=MibTableColumn
hpnicfSysCurBtmFileName=_HpnicfSysCurBtmFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,2,1,1,4),_HpnicfSysCurBtmFileName_Type())
hpnicfSysCurBtmFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysCurBtmFileName.setStatus(_A)
class _HpnicfSysCurUpdateBtmFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfSysCurUpdateBtmFileName_Type.__name__=_J
_HpnicfSysCurUpdateBtmFileName_Object=MibTableColumn
hpnicfSysCurUpdateBtmFileName=_HpnicfSysCurUpdateBtmFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,2,1,1,5),_HpnicfSysCurUpdateBtmFileName_Type())
hpnicfSysCurUpdateBtmFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysCurUpdateBtmFileName.setStatus(_A)
_HpnicfSysReload_ObjectIdentity=ObjectIdentity
hpnicfSysReload=_HpnicfSysReload_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3))
class _HpnicfSysReloadSchedule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysReloadSchedule_Type.__name__=_C
_HpnicfSysReloadSchedule_Object=MibScalar
hpnicfSysReloadSchedule=_HpnicfSysReloadSchedule_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,1),_HpnicfSysReloadSchedule_Type())
hpnicfSysReloadSchedule.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysReloadSchedule.setStatus(_A)
class _HpnicfSysReloadAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('reloadUnavailable',1),('reloadOnSchedule',2),('reloadAtOnce',3),('reloadCancel',4)))
_HpnicfSysReloadAction_Type.__name__=_C
_HpnicfSysReloadAction_Object=MibScalar
hpnicfSysReloadAction=_HpnicfSysReloadAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,2),_HpnicfSysReloadAction_Type())
hpnicfSysReloadAction.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysReloadAction.setStatus(_A)
_HpnicfSysReloadScheduleTable_Object=MibTable
hpnicfSysReloadScheduleTable=_HpnicfSysReloadScheduleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3))
if mibBuilder.loadTexts:hpnicfSysReloadScheduleTable.setStatus(_A)
_HpnicfSysReloadScheduleEntry_Object=MibTableRow
hpnicfSysReloadScheduleEntry=_HpnicfSysReloadScheduleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1))
hpnicfSysReloadScheduleEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:hpnicfSysReloadScheduleEntry.setStatus(_A)
class _HpnicfSysReloadScheduleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysReloadScheduleIndex_Type.__name__=_C
_HpnicfSysReloadScheduleIndex_Object=MibTableColumn
hpnicfSysReloadScheduleIndex=_HpnicfSysReloadScheduleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1,1),_HpnicfSysReloadScheduleIndex_Type())
hpnicfSysReloadScheduleIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysReloadScheduleIndex.setStatus(_A)
class _HpnicfSysReloadEntity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysReloadEntity_Type.__name__=_C
_HpnicfSysReloadEntity_Object=MibTableColumn
hpnicfSysReloadEntity=_HpnicfSysReloadEntity_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1,2),_HpnicfSysReloadEntity_Type())
hpnicfSysReloadEntity.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysReloadEntity.setStatus(_A)
class _HpnicfSysReloadCfgFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysReloadCfgFile_Type.__name__=_C
_HpnicfSysReloadCfgFile_Object=MibTableColumn
hpnicfSysReloadCfgFile=_HpnicfSysReloadCfgFile_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1,3),_HpnicfSysReloadCfgFile_Type())
hpnicfSysReloadCfgFile.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysReloadCfgFile.setStatus(_A)
class _HpnicfSysReloadImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysReloadImage_Type.__name__=_C
_HpnicfSysReloadImage_Object=MibTableColumn
hpnicfSysReloadImage=_HpnicfSysReloadImage_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1,4),_HpnicfSysReloadImage_Type())
hpnicfSysReloadImage.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysReloadImage.setStatus(_A)
class _HpnicfSysReloadReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysReloadReason_Type.__name__=_E
_HpnicfSysReloadReason_Object=MibTableColumn
hpnicfSysReloadReason=_HpnicfSysReloadReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1,5),_HpnicfSysReloadReason_Type())
hpnicfSysReloadReason.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysReloadReason.setStatus(_A)
class _HpnicfSysReloadScheduleTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpnicfSysReloadScheduleTime_Type.__name__=_L
_HpnicfSysReloadScheduleTime_Object=MibTableColumn
hpnicfSysReloadScheduleTime=_HpnicfSysReloadScheduleTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1,6),_HpnicfSysReloadScheduleTime_Type())
hpnicfSysReloadScheduleTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysReloadScheduleTime.setStatus(_A)
_HpnicfSysReloadRowStatus_Type=RowStatus
_HpnicfSysReloadRowStatus_Object=MibTableColumn
hpnicfSysReloadRowStatus=_HpnicfSysReloadRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1,7),_HpnicfSysReloadRowStatus_Type())
hpnicfSysReloadRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysReloadRowStatus.setStatus(_A)
_HpnicfSysReloadScheduleTagList_Type=SnmpTagList
_HpnicfSysReloadScheduleTagList_Object=MibTableColumn
hpnicfSysReloadScheduleTagList=_HpnicfSysReloadScheduleTagList_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,3,1,8),_HpnicfSysReloadScheduleTagList_Type())
hpnicfSysReloadScheduleTagList.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysReloadScheduleTagList.setStatus(_A)
_HpnicfSysReloadTag_Type=SnmpTagValue
_HpnicfSysReloadTag_Object=MibScalar
hpnicfSysReloadTag=_HpnicfSysReloadTag_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,3,4),_HpnicfSysReloadTag_Type())
hpnicfSysReloadTag.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysReloadTag.setStatus(_A)
_HpnicfSysImage_ObjectIdentity=ObjectIdentity
hpnicfSysImage=_HpnicfSysImage_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4))
class _HpnicfSysImageNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysImageNum_Type.__name__=_C
_HpnicfSysImageNum_Object=MibScalar
hpnicfSysImageNum=_HpnicfSysImageNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4,1),_HpnicfSysImageNum_Type())
hpnicfSysImageNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysImageNum.setStatus(_A)
_HpnicfSysImageTable_Object=MibTable
hpnicfSysImageTable=_HpnicfSysImageTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4,2))
if mibBuilder.loadTexts:hpnicfSysImageTable.setStatus(_A)
_HpnicfSysImageEntry_Object=MibTableRow
hpnicfSysImageEntry=_HpnicfSysImageEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4,2,1))
hpnicfSysImageEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:hpnicfSysImageEntry.setStatus(_A)
class _HpnicfSysImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysImageIndex_Type.__name__=_C
_HpnicfSysImageIndex_Object=MibTableColumn
hpnicfSysImageIndex=_HpnicfSysImageIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4,2,1,1),_HpnicfSysImageIndex_Type())
hpnicfSysImageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysImageIndex.setStatus(_A)
class _HpnicfSysImageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysImageName_Type.__name__=_E
_HpnicfSysImageName_Object=MibTableColumn
hpnicfSysImageName=_HpnicfSysImageName_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4,2,1,2),_HpnicfSysImageName_Type())
hpnicfSysImageName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysImageName.setStatus(_A)
class _HpnicfSysImageSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysImageSize_Type.__name__=_C
_HpnicfSysImageSize_Object=MibTableColumn
hpnicfSysImageSize=_HpnicfSysImageSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4,2,1,3),_HpnicfSysImageSize_Type())
hpnicfSysImageSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysImageSize.setStatus(_A)
class _HpnicfSysImageLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysImageLocation_Type.__name__=_E
_HpnicfSysImageLocation_Object=MibTableColumn
hpnicfSysImageLocation=_HpnicfSysImageLocation_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4,2,1,4),_HpnicfSysImageLocation_Type())
hpnicfSysImageLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysImageLocation.setStatus(_A)
class _HpnicfSysImageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('main',1),('backup',2),(_I,3),('secure',4),('main-backup',5),('main-secure',6),('backup-secure',7),('main-backup-secure',8)))
_HpnicfSysImageType_Type.__name__=_C
_HpnicfSysImageType_Object=MibTableColumn
hpnicfSysImageType=_HpnicfSysImageType_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,4,2,1,5),_HpnicfSysImageType_Type())
hpnicfSysImageType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysImageType.setStatus(_A)
_HpnicfSysCFGFile_ObjectIdentity=ObjectIdentity
hpnicfSysCFGFile=_HpnicfSysCFGFile_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,5))
class _HpnicfSysCFGFileNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysCFGFileNum_Type.__name__=_C
_HpnicfSysCFGFileNum_Object=MibScalar
hpnicfSysCFGFileNum=_HpnicfSysCFGFileNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,5,1),_HpnicfSysCFGFileNum_Type())
hpnicfSysCFGFileNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysCFGFileNum.setStatus(_A)
_HpnicfSysCFGFileTable_Object=MibTable
hpnicfSysCFGFileTable=_HpnicfSysCFGFileTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,5,2))
if mibBuilder.loadTexts:hpnicfSysCFGFileTable.setStatus(_A)
_HpnicfSysCFGFileEntry_Object=MibTableRow
hpnicfSysCFGFileEntry=_HpnicfSysCFGFileEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,5,2,1))
hpnicfSysCFGFileEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:hpnicfSysCFGFileEntry.setStatus(_A)
class _HpnicfSysCFGFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysCFGFileIndex_Type.__name__=_C
_HpnicfSysCFGFileIndex_Object=MibTableColumn
hpnicfSysCFGFileIndex=_HpnicfSysCFGFileIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,5,2,1,1),_HpnicfSysCFGFileIndex_Type())
hpnicfSysCFGFileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysCFGFileIndex.setStatus(_A)
class _HpnicfSysCFGFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysCFGFileName_Type.__name__=_E
_HpnicfSysCFGFileName_Object=MibTableColumn
hpnicfSysCFGFileName=_HpnicfSysCFGFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,5,2,1,2),_HpnicfSysCFGFileName_Type())
hpnicfSysCFGFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysCFGFileName.setStatus(_A)
class _HpnicfSysCFGFileSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysCFGFileSize_Type.__name__=_C
_HpnicfSysCFGFileSize_Object=MibTableColumn
hpnicfSysCFGFileSize=_HpnicfSysCFGFileSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,5,2,1,3),_HpnicfSysCFGFileSize_Type())
hpnicfSysCFGFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysCFGFileSize.setStatus(_A)
class _HpnicfSysCFGFileLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysCFGFileLocation_Type.__name__=_E
_HpnicfSysCFGFileLocation_Object=MibTableColumn
hpnicfSysCFGFileLocation=_HpnicfSysCFGFileLocation_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,5,2,1,4),_HpnicfSysCFGFileLocation_Type())
hpnicfSysCFGFileLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysCFGFileLocation.setStatus(_A)
_HpnicfSysBtmFile_ObjectIdentity=ObjectIdentity
hpnicfSysBtmFile=_HpnicfSysBtmFile_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6))
_HpnicfSysBtmFileLoad_ObjectIdentity=ObjectIdentity
hpnicfSysBtmFileLoad=_HpnicfSysBtmFileLoad_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,1))
_HpnicfSysBtmLoadMaxNumber_Type=Integer32
_HpnicfSysBtmLoadMaxNumber_Object=MibScalar
hpnicfSysBtmLoadMaxNumber=_HpnicfSysBtmLoadMaxNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,1,1),_HpnicfSysBtmLoadMaxNumber_Type())
hpnicfSysBtmLoadMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysBtmLoadMaxNumber.setStatus(_A)
_HpnicfSysBtmLoadTable_Object=MibTable
hpnicfSysBtmLoadTable=_HpnicfSysBtmLoadTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,2))
if mibBuilder.loadTexts:hpnicfSysBtmLoadTable.setStatus(_A)
_HpnicfSysBtmLoadEntry_Object=MibTableRow
hpnicfSysBtmLoadEntry=_HpnicfSysBtmLoadEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,2,1))
hpnicfSysBtmLoadEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:hpnicfSysBtmLoadEntry.setStatus(_A)
class _HpnicfSysBtmLoadIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysBtmLoadIndex_Type.__name__=_C
_HpnicfSysBtmLoadIndex_Object=MibTableColumn
hpnicfSysBtmLoadIndex=_HpnicfSysBtmLoadIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,2,1,1),_HpnicfSysBtmLoadIndex_Type())
hpnicfSysBtmLoadIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysBtmLoadIndex.setStatus(_A)
class _HpnicfSysBtmFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfSysBtmFileName_Type.__name__=_J
_HpnicfSysBtmFileName_Object=MibTableColumn
hpnicfSysBtmFileName=_HpnicfSysBtmFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,2,1,2),_HpnicfSysBtmFileName_Type())
hpnicfSysBtmFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysBtmFileName.setStatus(_A)
class _HpnicfSysBtmFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main',1),(_I,2)))
_HpnicfSysBtmFileType_Type.__name__=_C
_HpnicfSysBtmFileType_Object=MibTableColumn
hpnicfSysBtmFileType=_HpnicfSysBtmFileType_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,2,1,3),_HpnicfSysBtmFileType_Type())
hpnicfSysBtmFileType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysBtmFileType.setStatus(_A)
_HpnicfSysBtmRowStatus_Type=RowStatus
_HpnicfSysBtmRowStatus_Object=MibTableColumn
hpnicfSysBtmRowStatus=_HpnicfSysBtmRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,2,1,4),_HpnicfSysBtmRowStatus_Type())
hpnicfSysBtmRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysBtmRowStatus.setStatus(_A)
class _HpnicfSysBtmErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalidFile',1),('inProgress',2),(_N,3),(_O,4)))
_HpnicfSysBtmErrorStatus_Type.__name__=_C
_HpnicfSysBtmErrorStatus_Object=MibTableColumn
hpnicfSysBtmErrorStatus=_HpnicfSysBtmErrorStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,2,1,5),_HpnicfSysBtmErrorStatus_Type())
hpnicfSysBtmErrorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysBtmErrorStatus.setStatus(_A)
_HpnicfSysBtmLoadTime_Type=TimeTicks
_HpnicfSysBtmLoadTime_Object=MibTableColumn
hpnicfSysBtmLoadTime=_HpnicfSysBtmLoadTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,6,2,1,6),_HpnicfSysBtmLoadTime_Type())
hpnicfSysBtmLoadTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysBtmLoadTime.setStatus(_A)
_HpnicfSysPackage_ObjectIdentity=ObjectIdentity
hpnicfSysPackage=_HpnicfSysPackage_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7))
class _HpnicfSysPackageNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysPackageNum_Type.__name__=_C
_HpnicfSysPackageNum_Object=MibScalar
hpnicfSysPackageNum=_HpnicfSysPackageNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,1),_HpnicfSysPackageNum_Type())
hpnicfSysPackageNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageNum.setStatus(_A)
_HpnicfSysPackageTable_Object=MibTable
hpnicfSysPackageTable=_HpnicfSysPackageTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2))
if mibBuilder.loadTexts:hpnicfSysPackageTable.setStatus(_A)
_HpnicfSysPackageEntry_Object=MibTableRow
hpnicfSysPackageEntry=_HpnicfSysPackageEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1))
hpnicfSysPackageEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:hpnicfSysPackageEntry.setStatus(_A)
class _HpnicfSysPackageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysPackageIndex_Type.__name__=_C
_HpnicfSysPackageIndex_Object=MibTableColumn
hpnicfSysPackageIndex=_HpnicfSysPackageIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,1),_HpnicfSysPackageIndex_Type())
hpnicfSysPackageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysPackageIndex.setStatus(_A)
class _HpnicfSysPackageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysPackageName_Type.__name__=_E
_HpnicfSysPackageName_Object=MibTableColumn
hpnicfSysPackageName=_HpnicfSysPackageName_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,2),_HpnicfSysPackageName_Type())
hpnicfSysPackageName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageName.setStatus(_A)
class _HpnicfSysPackageSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfSysPackageSize_Type.__name__=_K
_HpnicfSysPackageSize_Object=MibTableColumn
hpnicfSysPackageSize=_HpnicfSysPackageSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,3),_HpnicfSysPackageSize_Type())
hpnicfSysPackageSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageSize.setStatus(_A)
class _HpnicfSysPackageLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysPackageLocation_Type.__name__=_E
_HpnicfSysPackageLocation_Object=MibTableColumn
hpnicfSysPackageLocation=_HpnicfSysPackageLocation_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,4),_HpnicfSysPackageLocation_Type())
hpnicfSysPackageLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageLocation.setStatus(_A)
class _HpnicfSysPackageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('boot',1),(_g,2),(_h,3),('patch',4)))
_HpnicfSysPackageType_Type.__name__=_C
_HpnicfSysPackageType_Object=MibTableColumn
hpnicfSysPackageType=_HpnicfSysPackageType_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,5),_HpnicfSysPackageType_Type())
hpnicfSysPackageType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageType.setStatus(_A)
class _HpnicfSysPackageAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_P,2),(_Q,3),(_R,4)))
_HpnicfSysPackageAttribute_Type.__name__=_C
_HpnicfSysPackageAttribute_Object=MibTableColumn
hpnicfSysPackageAttribute=_HpnicfSysPackageAttribute_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,6),_HpnicfSysPackageAttribute_Type())
hpnicfSysPackageAttribute.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysPackageAttribute.setStatus(_A)
class _HpnicfSysPackageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_HpnicfSysPackageStatus_Type.__name__=_C
_HpnicfSysPackageStatus_Object=MibTableColumn
hpnicfSysPackageStatus=_HpnicfSysPackageStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,7),_HpnicfSysPackageStatus_Type())
hpnicfSysPackageStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageStatus.setStatus(_A)
class _HpnicfSysPackageDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysPackageDescription_Type.__name__=_E
_HpnicfSysPackageDescription_Object=MibTableColumn
hpnicfSysPackageDescription=_HpnicfSysPackageDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,8),_HpnicfSysPackageDescription_Type())
hpnicfSysPackageDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageDescription.setStatus(_A)
class _HpnicfSysPackageFeature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysPackageFeature_Type.__name__=_E
_HpnicfSysPackageFeature_Object=MibTableColumn
hpnicfSysPackageFeature=_HpnicfSysPackageFeature_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,9),_HpnicfSysPackageFeature_Type())
hpnicfSysPackageFeature.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageFeature.setStatus(_A)
class _HpnicfSysPackageVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysPackageVersion_Type.__name__=_E
_HpnicfSysPackageVersion_Object=MibTableColumn
hpnicfSysPackageVersion=_HpnicfSysPackageVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,10),_HpnicfSysPackageVersion_Type())
hpnicfSysPackageVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageVersion.setStatus(_A)
class _HpnicfSysPackageLoadAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_P,2),(_Q,3),(_R,4)))
_HpnicfSysPackageLoadAttribute_Type.__name__=_C
_HpnicfSysPackageLoadAttribute_Object=MibTableColumn
hpnicfSysPackageLoadAttribute=_HpnicfSysPackageLoadAttribute_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,11),_HpnicfSysPackageLoadAttribute_Type())
hpnicfSysPackageLoadAttribute.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysPackageLoadAttribute.setStatus(_A)
class _HpnicfSysPackageModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfSysPackageModel_Type.__name__=_E
_HpnicfSysPackageModel_Object=MibTableColumn
hpnicfSysPackageModel=_HpnicfSysPackageModel_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,2,1,12),_HpnicfSysPackageModel_Type())
hpnicfSysPackageModel.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageModel.setStatus(_A)
class _HpnicfSysPackageOperateEntryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysPackageOperateEntryLimit_Type.__name__=_C
_HpnicfSysPackageOperateEntryLimit_Object=MibScalar
hpnicfSysPackageOperateEntryLimit=_HpnicfSysPackageOperateEntryLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,3),_HpnicfSysPackageOperateEntryLimit_Type())
hpnicfSysPackageOperateEntryLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysPackageOperateEntryLimit.setStatus(_A)
_HpnicfSysPackageOperateTable_Object=MibTable
hpnicfSysPackageOperateTable=_HpnicfSysPackageOperateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,4))
if mibBuilder.loadTexts:hpnicfSysPackageOperateTable.setStatus(_A)
_HpnicfSysPackageOperateEntry_Object=MibTableRow
hpnicfSysPackageOperateEntry=_HpnicfSysPackageOperateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,4,1))
hpnicfSysPackageOperateEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:hpnicfSysPackageOperateEntry.setStatus(_A)
class _HpnicfSysPackageOperateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysPackageOperateIndex_Type.__name__=_C
_HpnicfSysPackageOperateIndex_Object=MibTableColumn
hpnicfSysPackageOperateIndex=_HpnicfSysPackageOperateIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,4,1,1),_HpnicfSysPackageOperateIndex_Type())
hpnicfSysPackageOperateIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysPackageOperateIndex.setStatus(_A)
class _HpnicfSysPackageOperatePackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysPackageOperatePackIndex_Type.__name__=_C
_HpnicfSysPackageOperatePackIndex_Object=MibTableColumn
hpnicfSysPackageOperatePackIndex=_HpnicfSysPackageOperatePackIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,4,1,2),_HpnicfSysPackageOperatePackIndex_Type())
hpnicfSysPackageOperatePackIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysPackageOperatePackIndex.setStatus(_A)
class _HpnicfSysPackageOperateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_HpnicfSysPackageOperateStatus_Type.__name__=_C
_HpnicfSysPackageOperateStatus_Object=MibTableColumn
hpnicfSysPackageOperateStatus=_HpnicfSysPackageOperateStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,4,1,3),_HpnicfSysPackageOperateStatus_Type())
hpnicfSysPackageOperateStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysPackageOperateStatus.setStatus(_A)
_HpnicfSysPackageOperateRowStatus_Type=RowStatus
_HpnicfSysPackageOperateRowStatus_Object=MibTableColumn
hpnicfSysPackageOperateRowStatus=_HpnicfSysPackageOperateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,4,1,4),_HpnicfSysPackageOperateRowStatus_Type())
hpnicfSysPackageOperateRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysPackageOperateRowStatus.setStatus(_A)
class _HpnicfSysPackageOperateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),('opNotSupport',5)))
_HpnicfSysPackageOperateResult_Type.__name__=_C
_HpnicfSysPackageOperateResult_Object=MibTableColumn
hpnicfSysPackageOperateResult=_HpnicfSysPackageOperateResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,7,4,1,5),_HpnicfSysPackageOperateResult_Type())
hpnicfSysPackageOperateResult.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysPackageOperateResult.setStatus(_A)
_HpnicfSysIpeFile_ObjectIdentity=ObjectIdentity
hpnicfSysIpeFile=_HpnicfSysIpeFile_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8))
class _HpnicfSysIpeFileNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfSysIpeFileNum_Type.__name__=_C
_HpnicfSysIpeFileNum_Object=MibScalar
hpnicfSysIpeFileNum=_HpnicfSysIpeFileNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,1),_HpnicfSysIpeFileNum_Type())
hpnicfSysIpeFileNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpeFileNum.setStatus(_A)
_HpnicfSysIpeFileTable_Object=MibTable
hpnicfSysIpeFileTable=_HpnicfSysIpeFileTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,2))
if mibBuilder.loadTexts:hpnicfSysIpeFileTable.setStatus(_A)
_HpnicfSysIpeFileEntry_Object=MibTableRow
hpnicfSysIpeFileEntry=_HpnicfSysIpeFileEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,2,1))
hpnicfSysIpeFileEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:hpnicfSysIpeFileEntry.setStatus(_A)
class _HpnicfSysIpeFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysIpeFileIndex_Type.__name__=_C
_HpnicfSysIpeFileIndex_Object=MibTableColumn
hpnicfSysIpeFileIndex=_HpnicfSysIpeFileIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,2,1,1),_HpnicfSysIpeFileIndex_Type())
hpnicfSysIpeFileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysIpeFileIndex.setStatus(_A)
class _HpnicfSysIpeFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysIpeFileName_Type.__name__=_E
_HpnicfSysIpeFileName_Object=MibTableColumn
hpnicfSysIpeFileName=_HpnicfSysIpeFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,2,1,2),_HpnicfSysIpeFileName_Type())
hpnicfSysIpeFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpeFileName.setStatus(_A)
class _HpnicfSysIpeFileSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfSysIpeFileSize_Type.__name__=_K
_HpnicfSysIpeFileSize_Object=MibTableColumn
hpnicfSysIpeFileSize=_HpnicfSysIpeFileSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,2,1,3),_HpnicfSysIpeFileSize_Type())
hpnicfSysIpeFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpeFileSize.setStatus(_A)
class _HpnicfSysIpeFileLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysIpeFileLocation_Type.__name__=_E
_HpnicfSysIpeFileLocation_Object=MibTableColumn
hpnicfSysIpeFileLocation=_HpnicfSysIpeFileLocation_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,2,1,4),_HpnicfSysIpeFileLocation_Type())
hpnicfSysIpeFileLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpeFileLocation.setStatus(_A)
_HpnicfSysIpeFileModel_Type=SnmpTagList
_HpnicfSysIpeFileModel_Object=MibTableColumn
hpnicfSysIpeFileModel=_HpnicfSysIpeFileModel_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,2,1,5),_HpnicfSysIpeFileModel_Type())
hpnicfSysIpeFileModel.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpeFileModel.setStatus(_A)
_HpnicfSysIpePackageTable_Object=MibTable
hpnicfSysIpePackageTable=_HpnicfSysIpePackageTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3))
if mibBuilder.loadTexts:hpnicfSysIpePackageTable.setStatus(_A)
_HpnicfSysIpePackageEntry_Object=MibTableRow
hpnicfSysIpePackageEntry=_HpnicfSysIpePackageEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1))
hpnicfSysIpePackageEntry.setIndexNames((0,_B,_S),(0,_B,_p))
if mibBuilder.loadTexts:hpnicfSysIpePackageEntry.setStatus(_A)
class _HpnicfSysIpePackageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysIpePackageIndex_Type.__name__=_C
_HpnicfSysIpePackageIndex_Object=MibTableColumn
hpnicfSysIpePackageIndex=_HpnicfSysIpePackageIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1,1),_HpnicfSysIpePackageIndex_Type())
hpnicfSysIpePackageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysIpePackageIndex.setStatus(_A)
class _HpnicfSysIpePackageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysIpePackageName_Type.__name__=_E
_HpnicfSysIpePackageName_Object=MibTableColumn
hpnicfSysIpePackageName=_HpnicfSysIpePackageName_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1,2),_HpnicfSysIpePackageName_Type())
hpnicfSysIpePackageName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpePackageName.setStatus(_A)
class _HpnicfSysIpePackageSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfSysIpePackageSize_Type.__name__=_K
_HpnicfSysIpePackageSize_Object=MibTableColumn
hpnicfSysIpePackageSize=_HpnicfSysIpePackageSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1,3),_HpnicfSysIpePackageSize_Type())
hpnicfSysIpePackageSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpePackageSize.setStatus(_A)
class _HpnicfSysIpePackageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('boot',1),(_g,2),(_h,3),('patch',4)))
_HpnicfSysIpePackageType_Type.__name__=_C
_HpnicfSysIpePackageType_Object=MibTableColumn
hpnicfSysIpePackageType=_HpnicfSysIpePackageType_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1,4),_HpnicfSysIpePackageType_Type())
hpnicfSysIpePackageType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpePackageType.setStatus(_A)
class _HpnicfSysIpePackageDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysIpePackageDescription_Type.__name__=_E
_HpnicfSysIpePackageDescription_Object=MibTableColumn
hpnicfSysIpePackageDescription=_HpnicfSysIpePackageDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1,5),_HpnicfSysIpePackageDescription_Type())
hpnicfSysIpePackageDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpePackageDescription.setStatus(_A)
class _HpnicfSysIpePackageFeature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysIpePackageFeature_Type.__name__=_E
_HpnicfSysIpePackageFeature_Object=MibTableColumn
hpnicfSysIpePackageFeature=_HpnicfSysIpePackageFeature_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1,6),_HpnicfSysIpePackageFeature_Type())
hpnicfSysIpePackageFeature.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpePackageFeature.setStatus(_A)
class _HpnicfSysIpePackageVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysIpePackageVersion_Type.__name__=_E
_HpnicfSysIpePackageVersion_Object=MibTableColumn
hpnicfSysIpePackageVersion=_HpnicfSysIpePackageVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1,7),_HpnicfSysIpePackageVersion_Type())
hpnicfSysIpePackageVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpePackageVersion.setStatus(_A)
class _HpnicfSysIpePackageModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfSysIpePackageModel_Type.__name__=_E
_HpnicfSysIpePackageModel_Object=MibTableColumn
hpnicfSysIpePackageModel=_HpnicfSysIpePackageModel_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,3,1,8),_HpnicfSysIpePackageModel_Type())
hpnicfSysIpePackageModel.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpePackageModel.setStatus(_A)
_HpnicfSysIpeFileOperateTable_Object=MibTable
hpnicfSysIpeFileOperateTable=_HpnicfSysIpeFileOperateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,4))
if mibBuilder.loadTexts:hpnicfSysIpeFileOperateTable.setStatus(_A)
_HpnicfSysIpeFileOperateEntry_Object=MibTableRow
hpnicfSysIpeFileOperateEntry=_HpnicfSysIpeFileOperateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,4,1))
hpnicfSysIpeFileOperateEntry.setIndexNames((0,_B,_q))
if mibBuilder.loadTexts:hpnicfSysIpeFileOperateEntry.setStatus(_A)
class _HpnicfSysIpeFileOperateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysIpeFileOperateIndex_Type.__name__=_C
_HpnicfSysIpeFileOperateIndex_Object=MibTableColumn
hpnicfSysIpeFileOperateIndex=_HpnicfSysIpeFileOperateIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,4,1,1),_HpnicfSysIpeFileOperateIndex_Type())
hpnicfSysIpeFileOperateIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysIpeFileOperateIndex.setStatus(_A)
class _HpnicfSysIpeFileOperateFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysIpeFileOperateFileIndex_Type.__name__=_C
_HpnicfSysIpeFileOperateFileIndex_Object=MibTableColumn
hpnicfSysIpeFileOperateFileIndex=_HpnicfSysIpeFileOperateFileIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,4,1,2),_HpnicfSysIpeFileOperateFileIndex_Type())
hpnicfSysIpeFileOperateFileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysIpeFileOperateFileIndex.setStatus(_A)
class _HpnicfSysIpeFileOperateAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_P,2),(_Q,3),(_R,4)))
_HpnicfSysIpeFileOperateAttribute_Type.__name__=_C
_HpnicfSysIpeFileOperateAttribute_Object=MibTableColumn
hpnicfSysIpeFileOperateAttribute=_HpnicfSysIpeFileOperateAttribute_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,4,1,3),_HpnicfSysIpeFileOperateAttribute_Type())
hpnicfSysIpeFileOperateAttribute.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysIpeFileOperateAttribute.setStatus(_A)
_HpnicfSysIpeFileOperateRowStatus_Type=RowStatus
_HpnicfSysIpeFileOperateRowStatus_Object=MibTableColumn
hpnicfSysIpeFileOperateRowStatus=_HpnicfSysIpeFileOperateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,4,1,4),_HpnicfSysIpeFileOperateRowStatus_Type())
hpnicfSysIpeFileOperateRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysIpeFileOperateRowStatus.setStatus(_A)
class _HpnicfSysIpeFileOperateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),('opDeviceFull',5),('opFileOpenError',6)))
_HpnicfSysIpeFileOperateResult_Type.__name__=_C
_HpnicfSysIpeFileOperateResult_Object=MibTableColumn
hpnicfSysIpeFileOperateResult=_HpnicfSysIpeFileOperateResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,8,4,1,5),_HpnicfSysIpeFileOperateResult_Type())
hpnicfSysIpeFileOperateResult.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysIpeFileOperateResult.setStatus(_A)
_HpnicfSysSetBootImage_ObjectIdentity=ObjectIdentity
hpnicfSysSetBootImage=_HpnicfSysSetBootImage_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9))
_HpnicfSysSetBootImageOp_ObjectIdentity=ObjectIdentity
hpnicfSysSetBootImageOp=_HpnicfSysSetBootImageOp_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,1))
class _HpnicfSysSetBootImageAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,1),('done',2),('bootLoadPrimary',3),('bootLoadSecondary',4),('bootLoadPrimarySecondary',5),('bootPrimary',6),('bootSecondary',7),('bootPrimarySecondary',8),('loadPrimary',9),('loadSecondary',10),('loadPrimarySecondary',11)))
_HpnicfSysSetBootImageAction_Type.__name__=_C
_HpnicfSysSetBootImageAction_Object=MibScalar
hpnicfSysSetBootImageAction=_HpnicfSysSetBootImageAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,1,1),_HpnicfSysSetBootImageAction_Type())
hpnicfSysSetBootImageAction.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysSetBootImageAction.setStatus(_A)
class _HpnicfSysSetBootImageFileOverWrite_Type(TruthValue):defaultValue=2
_HpnicfSysSetBootImageFileOverWrite_Type.__name__=_M
_HpnicfSysSetBootImageFileOverWrite_Object=MibScalar
hpnicfSysSetBootImageFileOverWrite=_HpnicfSysSetBootImageFileOverWrite_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,1,2),_HpnicfSysSetBootImageFileOverWrite_Type())
hpnicfSysSetBootImageFileOverWrite.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysSetBootImageFileOverWrite.setStatus(_A)
class _HpnicfSysSetBootImageRemoveIpeFile_Type(TruthValue):defaultValue=2
_HpnicfSysSetBootImageRemoveIpeFile_Type.__name__=_M
_HpnicfSysSetBootImageRemoveIpeFile_Object=MibScalar
hpnicfSysSetBootImageRemoveIpeFile=_HpnicfSysSetBootImageRemoveIpeFile_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,1,3),_HpnicfSysSetBootImageRemoveIpeFile_Type())
hpnicfSysSetBootImageRemoveIpeFile.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSysSetBootImageRemoveIpeFile.setStatus(_A)
class _HpnicfSysSetBootImageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('doing',2),(_N,3),(_O,4)))
_HpnicfSysSetBootImageStatus_Type.__name__=_C
_HpnicfSysSetBootImageStatus_Object=MibScalar
hpnicfSysSetBootImageStatus=_HpnicfSysSetBootImageStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,1,4),_HpnicfSysSetBootImageStatus_Type())
hpnicfSysSetBootImageStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysSetBootImageStatus.setStatus(_A)
class _HpnicfSysSetBootImageFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysSetBootImageFailedReason_Type.__name__=_E
_HpnicfSysSetBootImageFailedReason_Object=MibScalar
hpnicfSysSetBootImageFailedReason=_HpnicfSysSetBootImageFailedReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,1,5),_HpnicfSysSetBootImageFailedReason_Type())
hpnicfSysSetBootImageFailedReason.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysSetBootImageFailedReason.setStatus(_A)
_HpnicfSysBootPackageTable_Object=MibTable
hpnicfSysBootPackageTable=_HpnicfSysBootPackageTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,2))
if mibBuilder.loadTexts:hpnicfSysBootPackageTable.setStatus(_A)
_HpnicfSysBootPackageEntry_Object=MibTableRow
hpnicfSysBootPackageEntry=_HpnicfSysBootPackageEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,2,1))
hpnicfSysBootPackageEntry.setIndexNames((0,_B,_r))
if mibBuilder.loadTexts:hpnicfSysBootPackageEntry.setStatus(_A)
class _HpnicfSysBootPackageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysBootPackageIndex_Type.__name__=_C
_HpnicfSysBootPackageIndex_Object=MibTableColumn
hpnicfSysBootPackageIndex=_HpnicfSysBootPackageIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,2,1,1),_HpnicfSysBootPackageIndex_Type())
hpnicfSysBootPackageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysBootPackageIndex.setStatus(_A)
_HpnicfSysBootPackageRowStatus_Type=RowStatus
_HpnicfSysBootPackageRowStatus_Object=MibTableColumn
hpnicfSysBootPackageRowStatus=_HpnicfSysBootPackageRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,2,1,2),_HpnicfSysBootPackageRowStatus_Type())
hpnicfSysBootPackageRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysBootPackageRowStatus.setStatus(_A)
_HpnicfSysBootIpeTable_Object=MibTable
hpnicfSysBootIpeTable=_HpnicfSysBootIpeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,3))
if mibBuilder.loadTexts:hpnicfSysBootIpeTable.setStatus(_A)
_HpnicfSysBootIpeEntry_Object=MibTableRow
hpnicfSysBootIpeEntry=_HpnicfSysBootIpeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,3,1))
hpnicfSysBootIpeEntry.setIndexNames((0,_B,_s))
if mibBuilder.loadTexts:hpnicfSysBootIpeEntry.setStatus(_A)
class _HpnicfSysBootIpeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfSysBootIpeIndex_Type.__name__=_C
_HpnicfSysBootIpeIndex_Object=MibTableColumn
hpnicfSysBootIpeIndex=_HpnicfSysBootIpeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,3,1,1),_HpnicfSysBootIpeIndex_Type())
hpnicfSysBootIpeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysBootIpeIndex.setStatus(_A)
_HpnicfSysBootIpeRowStatus_Type=RowStatus
_HpnicfSysBootIpeRowStatus_Object=MibTableColumn
hpnicfSysBootIpeRowStatus=_HpnicfSysBootIpeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,3,1,2),_HpnicfSysBootIpeRowStatus_Type())
hpnicfSysBootIpeRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysBootIpeRowStatus.setStatus(_A)
_HpnicfSysSetBootImageResultTable_Object=MibTable
hpnicfSysSetBootImageResultTable=_HpnicfSysSetBootImageResultTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,4))
if mibBuilder.loadTexts:hpnicfSysSetBootImageResultTable.setStatus(_A)
_HpnicfSysSetBootImageResultEntry_Object=MibTableRow
hpnicfSysSetBootImageResultEntry=_HpnicfSysSetBootImageResultEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,4,1))
hpnicfSysSetBootImageResultEntry.setIndexNames((0,_B,_t))
if mibBuilder.loadTexts:hpnicfSysSetBootImageResultEntry.setStatus(_A)
class _HpnicfSysSetBootImageResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfSysSetBootImageResultIndex_Type.__name__=_C
_HpnicfSysSetBootImageResultIndex_Object=MibTableColumn
hpnicfSysSetBootImageResultIndex=_HpnicfSysSetBootImageResultIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,4,1,1),_HpnicfSysSetBootImageResultIndex_Type())
hpnicfSysSetBootImageResultIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSysSetBootImageResultIndex.setStatus(_A)
class _HpnicfSysSetBootImageResultStatusOfEachCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('doing',2),(_N,3),(_O,4)))
_HpnicfSysSetBootImageResultStatusOfEachCard_Type.__name__=_C
_HpnicfSysSetBootImageResultStatusOfEachCard_Object=MibTableColumn
hpnicfSysSetBootImageResultStatusOfEachCard=_HpnicfSysSetBootImageResultStatusOfEachCard_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,4,1,2),_HpnicfSysSetBootImageResultStatusOfEachCard_Type())
hpnicfSysSetBootImageResultStatusOfEachCard.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysSetBootImageResultStatusOfEachCard.setStatus(_A)
class _HpnicfSysSetBootImageFailedReasonOfEachCard_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSysSetBootImageFailedReasonOfEachCard_Type.__name__=_E
_HpnicfSysSetBootImageFailedReasonOfEachCard_Object=MibTableColumn
hpnicfSysSetBootImageFailedReasonOfEachCard=_HpnicfSysSetBootImageFailedReasonOfEachCard_Object((1,3,6,1,4,1,11,2,14,11,15,2,3,1,9,4,1,3),_HpnicfSysSetBootImageFailedReasonOfEachCard_Type())
hpnicfSysSetBootImageFailedReasonOfEachCard.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSysSetBootImageFailedReasonOfEachCard.setStatus(_A)
_HpnicfSystemManMIBNotifications_ObjectIdentity=ObjectIdentity
hpnicfSystemManMIBNotifications=_HpnicfSystemManMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,2))
_HpnicfSystemManMIBConformance_ObjectIdentity=ObjectIdentity
hpnicfSystemManMIBConformance=_HpnicfSystemManMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,3))
_HpnicfSystemManMIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfSystemManMIBCompliances=_HpnicfSystemManMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,3,1))
_HpnicfSystemManMIBGroups_ObjectIdentity=ObjectIdentity
hpnicfSystemManMIBGroups=_HpnicfSystemManMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,3,3,2))
hpnicfSysClockGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,3,3,2,1))
hpnicfSysClockGroup.setObjects(*((_B,_T),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:hpnicfSysClockGroup.setStatus(_A)
hpnicfSysReloadGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,3,3,2,2))
hpnicfSysReloadGroup.setObjects(*((_B,_A0),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_A1),(_B,_A2),(_B,_Y),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:hpnicfSysReloadGroup.setStatus(_A)
hpnicfSysImageGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,3,3,2,3))
hpnicfSysImageGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_Z)))
if mibBuilder.loadTexts:hpnicfSysImageGroup.setStatus(_A)
hpnicfSysCFGFileGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,3,3,2,4))
hpnicfSysCFGFileGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:hpnicfSysCFGFileGroup.setStatus(_A)
hpnicfSysCurGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,3,3,2,5))
hpnicfSysCurGroup.setObjects(*((_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:hpnicfSysCurGroup.setStatus(_A)
hpnicfSystemBtmLoadGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,3,3,2,7))
hpnicfSystemBtmLoadGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:hpnicfSystemBtmLoadGroup.setStatus(_A)
hpnicfSysClockChangedNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,3,2,1))
hpnicfSysClockChangedNotification.setObjects((_B,_T))
if mibBuilder.loadTexts:hpnicfSysClockChangedNotification.setStatus(_A)
hpnicfSysReloadNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,3,2,2))
hpnicfSysReloadNotification.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_U)))
if mibBuilder.loadTexts:hpnicfSysReloadNotification.setStatus(_A)
hpnicfSysStartUpNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,3,2,3))
hpnicfSysStartUpNotification.setObjects((_B,_Z))
if mibBuilder.loadTexts:hpnicfSysStartUpNotification.setStatus(_A)
hpnicfSystemManNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,3,3,2,6))
hpnicfSystemManNotificationGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:hpnicfSystemManNotificationGroup.setStatus(_A)
hpnicfSystemManMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,3,3,1,1))
hpnicfSystemManMIBCompliance.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:hpnicfSystemManMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfSystemMan':hpnicfSystemMan,'hpnicfSystemManMIBObjects':hpnicfSystemManMIBObjects,'hpnicfSysClock':hpnicfSysClock,_T:hpnicfSysLocalClock,'hpnicfSysSummerTime':hpnicfSysSummerTime,_u:hpnicfSysSummerTimeEnable,_v:hpnicfSysSummerTimeZone,_w:hpnicfSysSummerTimeMethod,_x:hpnicfSysSummerTimeStart,_y:hpnicfSysSummerTimeEnd,_z:hpnicfSysSummerTimeOffset,'hpnicfSysLocalClockString':hpnicfSysLocalClockString,'hpnicfSysCurrent':hpnicfSysCurrent,'hpnicfSysCurTable':hpnicfSysCurTable,'hpnicfSysCurEntry':hpnicfSysCurEntry,_a:hpnicfSysCurEntPhysicalIndex,_AD:hpnicfSysCurCFGFileIndex,_AE:hpnicfSysCurImageIndex,_AF:hpnicfSysCurBtmFileName,_AG:hpnicfSysCurUpdateBtmFileName,'hpnicfSysReload':hpnicfSysReload,_A0:hpnicfSysReloadSchedule,_U:hpnicfSysReloadAction,'hpnicfSysReloadScheduleTable':hpnicfSysReloadScheduleTable,'hpnicfSysReloadScheduleEntry':hpnicfSysReloadScheduleEntry,_b:hpnicfSysReloadScheduleIndex,_A3:hpnicfSysReloadEntity,_W:hpnicfSysReloadCfgFile,_V:hpnicfSysReloadImage,_X:hpnicfSysReloadReason,_Y:hpnicfSysReloadScheduleTime,_A4:hpnicfSysReloadRowStatus,_A1:hpnicfSysReloadScheduleTagList,_A2:hpnicfSysReloadTag,'hpnicfSysImage':hpnicfSysImage,_A5:hpnicfSysImageNum,'hpnicfSysImageTable':hpnicfSysImageTable,'hpnicfSysImageEntry':hpnicfSysImageEntry,_c:hpnicfSysImageIndex,_A6:hpnicfSysImageName,_A7:hpnicfSysImageSize,_A8:hpnicfSysImageLocation,_Z:hpnicfSysImageType,'hpnicfSysCFGFile':hpnicfSysCFGFile,_A9:hpnicfSysCFGFileNum,'hpnicfSysCFGFileTable':hpnicfSysCFGFileTable,'hpnicfSysCFGFileEntry':hpnicfSysCFGFileEntry,_d:hpnicfSysCFGFileIndex,_AA:hpnicfSysCFGFileName,_AB:hpnicfSysCFGFileSize,_AC:hpnicfSysCFGFileLocation,'hpnicfSysBtmFile':hpnicfSysBtmFile,'hpnicfSysBtmFileLoad':hpnicfSysBtmFileLoad,_AH:hpnicfSysBtmLoadMaxNumber,'hpnicfSysBtmLoadTable':hpnicfSysBtmLoadTable,'hpnicfSysBtmLoadEntry':hpnicfSysBtmLoadEntry,_e:hpnicfSysBtmLoadIndex,_AI:hpnicfSysBtmFileName,_AJ:hpnicfSysBtmFileType,_AK:hpnicfSysBtmRowStatus,_AL:hpnicfSysBtmErrorStatus,_AM:hpnicfSysBtmLoadTime,'hpnicfSysPackage':hpnicfSysPackage,'hpnicfSysPackageNum':hpnicfSysPackageNum,'hpnicfSysPackageTable':hpnicfSysPackageTable,'hpnicfSysPackageEntry':hpnicfSysPackageEntry,_f:hpnicfSysPackageIndex,'hpnicfSysPackageName':hpnicfSysPackageName,'hpnicfSysPackageSize':hpnicfSysPackageSize,'hpnicfSysPackageLocation':hpnicfSysPackageLocation,'hpnicfSysPackageType':hpnicfSysPackageType,'hpnicfSysPackageAttribute':hpnicfSysPackageAttribute,'hpnicfSysPackageStatus':hpnicfSysPackageStatus,'hpnicfSysPackageDescription':hpnicfSysPackageDescription,'hpnicfSysPackageFeature':hpnicfSysPackageFeature,'hpnicfSysPackageVersion':hpnicfSysPackageVersion,'hpnicfSysPackageLoadAttribute':hpnicfSysPackageLoadAttribute,'hpnicfSysPackageModel':hpnicfSysPackageModel,'hpnicfSysPackageOperateEntryLimit':hpnicfSysPackageOperateEntryLimit,'hpnicfSysPackageOperateTable':hpnicfSysPackageOperateTable,'hpnicfSysPackageOperateEntry':hpnicfSysPackageOperateEntry,_k:hpnicfSysPackageOperateIndex,'hpnicfSysPackageOperatePackIndex':hpnicfSysPackageOperatePackIndex,'hpnicfSysPackageOperateStatus':hpnicfSysPackageOperateStatus,'hpnicfSysPackageOperateRowStatus':hpnicfSysPackageOperateRowStatus,'hpnicfSysPackageOperateResult':hpnicfSysPackageOperateResult,'hpnicfSysIpeFile':hpnicfSysIpeFile,'hpnicfSysIpeFileNum':hpnicfSysIpeFileNum,'hpnicfSysIpeFileTable':hpnicfSysIpeFileTable,'hpnicfSysIpeFileEntry':hpnicfSysIpeFileEntry,_S:hpnicfSysIpeFileIndex,'hpnicfSysIpeFileName':hpnicfSysIpeFileName,'hpnicfSysIpeFileSize':hpnicfSysIpeFileSize,'hpnicfSysIpeFileLocation':hpnicfSysIpeFileLocation,'hpnicfSysIpeFileModel':hpnicfSysIpeFileModel,'hpnicfSysIpePackageTable':hpnicfSysIpePackageTable,'hpnicfSysIpePackageEntry':hpnicfSysIpePackageEntry,_p:hpnicfSysIpePackageIndex,'hpnicfSysIpePackageName':hpnicfSysIpePackageName,'hpnicfSysIpePackageSize':hpnicfSysIpePackageSize,'hpnicfSysIpePackageType':hpnicfSysIpePackageType,'hpnicfSysIpePackageDescription':hpnicfSysIpePackageDescription,'hpnicfSysIpePackageFeature':hpnicfSysIpePackageFeature,'hpnicfSysIpePackageVersion':hpnicfSysIpePackageVersion,'hpnicfSysIpePackageModel':hpnicfSysIpePackageModel,'hpnicfSysIpeFileOperateTable':hpnicfSysIpeFileOperateTable,'hpnicfSysIpeFileOperateEntry':hpnicfSysIpeFileOperateEntry,_q:hpnicfSysIpeFileOperateIndex,'hpnicfSysIpeFileOperateFileIndex':hpnicfSysIpeFileOperateFileIndex,'hpnicfSysIpeFileOperateAttribute':hpnicfSysIpeFileOperateAttribute,'hpnicfSysIpeFileOperateRowStatus':hpnicfSysIpeFileOperateRowStatus,'hpnicfSysIpeFileOperateResult':hpnicfSysIpeFileOperateResult,'hpnicfSysSetBootImage':hpnicfSysSetBootImage,'hpnicfSysSetBootImageOp':hpnicfSysSetBootImageOp,'hpnicfSysSetBootImageAction':hpnicfSysSetBootImageAction,'hpnicfSysSetBootImageFileOverWrite':hpnicfSysSetBootImageFileOverWrite,'hpnicfSysSetBootImageRemoveIpeFile':hpnicfSysSetBootImageRemoveIpeFile,'hpnicfSysSetBootImageStatus':hpnicfSysSetBootImageStatus,'hpnicfSysSetBootImageFailedReason':hpnicfSysSetBootImageFailedReason,'hpnicfSysBootPackageTable':hpnicfSysBootPackageTable,'hpnicfSysBootPackageEntry':hpnicfSysBootPackageEntry,_r:hpnicfSysBootPackageIndex,'hpnicfSysBootPackageRowStatus':hpnicfSysBootPackageRowStatus,'hpnicfSysBootIpeTable':hpnicfSysBootIpeTable,'hpnicfSysBootIpeEntry':hpnicfSysBootIpeEntry,_s:hpnicfSysBootIpeIndex,'hpnicfSysBootIpeRowStatus':hpnicfSysBootIpeRowStatus,'hpnicfSysSetBootImageResultTable':hpnicfSysSetBootImageResultTable,'hpnicfSysSetBootImageResultEntry':hpnicfSysSetBootImageResultEntry,_t:hpnicfSysSetBootImageResultIndex,'hpnicfSysSetBootImageResultStatusOfEachCard':hpnicfSysSetBootImageResultStatusOfEachCard,'hpnicfSysSetBootImageFailedReasonOfEachCard':hpnicfSysSetBootImageFailedReasonOfEachCard,'hpnicfSystemManMIBNotifications':hpnicfSystemManMIBNotifications,_AN:hpnicfSysClockChangedNotification,_AO:hpnicfSysReloadNotification,_AP:hpnicfSysStartUpNotification,'hpnicfSystemManMIBConformance':hpnicfSystemManMIBConformance,'hpnicfSystemManMIBCompliances':hpnicfSystemManMIBCompliances,'hpnicfSystemManMIBCompliance':hpnicfSystemManMIBCompliance,'hpnicfSystemManMIBGroups':hpnicfSystemManMIBGroups,_AQ:hpnicfSysClockGroup,_AR:hpnicfSysReloadGroup,_AS:hpnicfSysImageGroup,_AT:hpnicfSysCFGFileGroup,_AV:hpnicfSysCurGroup,_AU:hpnicfSystemManNotificationGroup,_AW:hpnicfSystemBtmLoadGroup})