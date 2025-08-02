_A1='currentNotificationGroup'
_A0='currentObjectGroup'
_z='hwStorageEventType'
_y='hwStorageAlarmReporting'
_x='hwStorageActiveAlarmInfoLocalAlarmID'
_w='hwStorageActiveAlarmInfoCategory'
_v='hwStorageActiveAlarmInfoAddtionInfo'
_u='hwStorageActiveAlarmInfoOccurTime'
_t='hwStorageActiveAlarmInfoAlarmID'
_s='hwStorageActiveAlarmInfoLevel'
_r='hwStorageActiveAlarmInfoType'
_q='hwStorageActiveAlarmInfoTitle'
_p='hwStorageActiveAlarmInfoRestoreAdvice'
_o='hwStorageActiveAlarmInfoLocationInfo'
_n='eventAlarm'
_m='resumeAlarm'
_l='faultAlarm'
_k='warningAlarm'
_j='minorAlarm'
_i='majorAlarm'
_h='criticalAlarm'
_g='equipmentFault'
_f='hwStorageTrapEventRecoveryTimeStr'
_e='hwStorageTrapEventTimeStr'
_d='hwStorageTrapEventID32Bit'
_c='hwStorageTrapEventParameter'
_b='hwStorageTrapEventRecoveryTime'
_a='hwStorageTrapEventTime'
_Z='hwStorageTrapEventSequence'
_Y='hwStorageTrapEventLevel'
_X='hwStorageTrapEventID'
_W='hwStorageTrapEventType'
_V='hwStorageReportingAlarmProductSN'
_U='hwStorageReportingAlarmProductModel'
_T='hwStorageReportingAlarmLocationAlarmID'
_S='hwStorageReportingAlarmFaultCategory'
_R='hwStorageReportingAlarmAdditionInfo'
_Q='hwStorageReportingAlarmSerialNo'
_P='hwStorageReportingAlarmFaultTime'
_O='hwStorageReportingAlarmAlarmID'
_N='hwStorageReportingAlarmFaultLevel'
_M='hwStorageReportingAlarmFaultType'
_L='hwStorageReportingAlarmFaultTitle'
_K='hwStorageReportingAlarmRestoreAdvice'
_J='hwStorageReportingAlarmLocationInfo'
_I='hwStorageReportingAlarmNodeCode'
_H='hwStorageActiveAlarmInfoSerialNo'
_G='hwStorageActiveAlarmInfoNodeCode'
_F='OctetString'
_E='Integer32'
_D='read-only'
_C='accessible-for-notify'
_B='current'
_A='HUAWEI-STORAGE-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
storage=ModuleIdentity((1,3,6,1,4,1,2011,2,251))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,2011,2))
_Alarm_ObjectIdentity=ObjectIdentity
alarm=_Alarm_ObjectIdentity((1,3,6,1,4,1,2011,2,251,20))
_HwStorageNotification_ObjectIdentity=ObjectIdentity
hwStorageNotification=_HwStorageNotification_ObjectIdentity((1,3,6,1,4,1,2011,2,251,20,1))
_HwStorageActiveAlarmInfo_ObjectIdentity=ObjectIdentity
hwStorageActiveAlarmInfo=_HwStorageActiveAlarmInfo_ObjectIdentity((1,3,6,1,4,1,2011,2,251,20,1,1))
_HwStorageActiveAlarmInfoTable_Object=MibTable
hwStorageActiveAlarmInfoTable=_HwStorageActiveAlarmInfoTable_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1))
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoTable.setStatus(_B)
_HwStorageActiveAlarmInfoEntry_Object=MibTableRow
hwStorageActiveAlarmInfoEntry=_HwStorageActiveAlarmInfoEntry_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1))
hwStorageActiveAlarmInfoEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoEntry.setStatus(_B)
_HwStorageActiveAlarmInfoNodeCode_Type=OctetString
_HwStorageActiveAlarmInfoNodeCode_Object=MibTableColumn
hwStorageActiveAlarmInfoNodeCode=_HwStorageActiveAlarmInfoNodeCode_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,1),_HwStorageActiveAlarmInfoNodeCode_Type())
hwStorageActiveAlarmInfoNodeCode.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoNodeCode.setStatus(_B)
_HwStorageActiveAlarmInfoLocationInfo_Type=DisplayString
_HwStorageActiveAlarmInfoLocationInfo_Object=MibTableColumn
hwStorageActiveAlarmInfoLocationInfo=_HwStorageActiveAlarmInfoLocationInfo_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,2),_HwStorageActiveAlarmInfoLocationInfo_Type())
hwStorageActiveAlarmInfoLocationInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoLocationInfo.setStatus(_B)
_HwStorageActiveAlarmInfoRestoreAdvice_Type=DisplayString
_HwStorageActiveAlarmInfoRestoreAdvice_Object=MibTableColumn
hwStorageActiveAlarmInfoRestoreAdvice=_HwStorageActiveAlarmInfoRestoreAdvice_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,3),_HwStorageActiveAlarmInfoRestoreAdvice_Type())
hwStorageActiveAlarmInfoRestoreAdvice.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoRestoreAdvice.setStatus(_B)
_HwStorageActiveAlarmInfoTitle_Type=DisplayString
_HwStorageActiveAlarmInfoTitle_Object=MibTableColumn
hwStorageActiveAlarmInfoTitle=_HwStorageActiveAlarmInfoTitle_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,4),_HwStorageActiveAlarmInfoTitle_Type())
hwStorageActiveAlarmInfoTitle.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoTitle.setStatus(_B)
class _HwStorageActiveAlarmInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_g,2))
_HwStorageActiveAlarmInfoType_Type.__name__=_E
_HwStorageActiveAlarmInfoType_Object=MibTableColumn
hwStorageActiveAlarmInfoType=_HwStorageActiveAlarmInfoType_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,5),_HwStorageActiveAlarmInfoType_Type())
hwStorageActiveAlarmInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoType.setStatus(_B)
class _HwStorageActiveAlarmInfoLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4)))
_HwStorageActiveAlarmInfoLevel_Type.__name__=_E
_HwStorageActiveAlarmInfoLevel_Object=MibTableColumn
hwStorageActiveAlarmInfoLevel=_HwStorageActiveAlarmInfoLevel_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,6),_HwStorageActiveAlarmInfoLevel_Type())
hwStorageActiveAlarmInfoLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoLevel.setStatus(_B)
_HwStorageActiveAlarmInfoAlarmID_Type=Gauge32
_HwStorageActiveAlarmInfoAlarmID_Object=MibTableColumn
hwStorageActiveAlarmInfoAlarmID=_HwStorageActiveAlarmInfoAlarmID_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,7),_HwStorageActiveAlarmInfoAlarmID_Type())
hwStorageActiveAlarmInfoAlarmID.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoAlarmID.setStatus(_B)
_HwStorageActiveAlarmInfoOccurTime_Type=OctetString
_HwStorageActiveAlarmInfoOccurTime_Object=MibTableColumn
hwStorageActiveAlarmInfoOccurTime=_HwStorageActiveAlarmInfoOccurTime_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,8),_HwStorageActiveAlarmInfoOccurTime_Type())
hwStorageActiveAlarmInfoOccurTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoOccurTime.setStatus(_B)
_HwStorageActiveAlarmInfoSerialNo_Type=Gauge32
_HwStorageActiveAlarmInfoSerialNo_Object=MibTableColumn
hwStorageActiveAlarmInfoSerialNo=_HwStorageActiveAlarmInfoSerialNo_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,9),_HwStorageActiveAlarmInfoSerialNo_Type())
hwStorageActiveAlarmInfoSerialNo.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoSerialNo.setStatus(_B)
_HwStorageActiveAlarmInfoAddtionInfo_Type=OctetString
_HwStorageActiveAlarmInfoAddtionInfo_Object=MibTableColumn
hwStorageActiveAlarmInfoAddtionInfo=_HwStorageActiveAlarmInfoAddtionInfo_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,10),_HwStorageActiveAlarmInfoAddtionInfo_Type())
hwStorageActiveAlarmInfoAddtionInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoAddtionInfo.setStatus(_B)
class _HwStorageActiveAlarmInfoCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_HwStorageActiveAlarmInfoCategory_Type.__name__=_E
_HwStorageActiveAlarmInfoCategory_Object=MibTableColumn
hwStorageActiveAlarmInfoCategory=_HwStorageActiveAlarmInfoCategory_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,11),_HwStorageActiveAlarmInfoCategory_Type())
hwStorageActiveAlarmInfoCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoCategory.setStatus(_B)
_HwStorageActiveAlarmInfoLocalAlarmID_Type=Counter64
_HwStorageActiveAlarmInfoLocalAlarmID_Object=MibTableColumn
hwStorageActiveAlarmInfoLocalAlarmID=_HwStorageActiveAlarmInfoLocalAlarmID_Object((1,3,6,1,4,1,2011,2,251,20,1,1,1,1,12),_HwStorageActiveAlarmInfoLocalAlarmID_Type())
hwStorageActiveAlarmInfoLocalAlarmID.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStorageActiveAlarmInfoLocalAlarmID.setStatus(_B)
_HwStorageNotificationType_ObjectIdentity=ObjectIdentity
hwStorageNotificationType=_HwStorageNotificationType_ObjectIdentity((1,3,6,1,4,1,2011,2,251,20,1,2))
_HwStorageReportingAlarm_ObjectIdentity=ObjectIdentity
hwStorageReportingAlarm=_HwStorageReportingAlarm_ObjectIdentity((1,3,6,1,4,1,2011,2,251,20,1,3))
_HwStorageReportingAlarmNodeCode_Type=OctetString
_HwStorageReportingAlarmNodeCode_Object=MibScalar
hwStorageReportingAlarmNodeCode=_HwStorageReportingAlarmNodeCode_Object((1,3,6,1,4,1,2011,2,251,20,1,3,1),_HwStorageReportingAlarmNodeCode_Type())
hwStorageReportingAlarmNodeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmNodeCode.setStatus(_B)
_HwStorageReportingAlarmLocationInfo_Type=DisplayString
_HwStorageReportingAlarmLocationInfo_Object=MibScalar
hwStorageReportingAlarmLocationInfo=_HwStorageReportingAlarmLocationInfo_Object((1,3,6,1,4,1,2011,2,251,20,1,3,2),_HwStorageReportingAlarmLocationInfo_Type())
hwStorageReportingAlarmLocationInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmLocationInfo.setStatus(_B)
class _HwStorageReportingAlarmRestoreAdvice_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwStorageReportingAlarmRestoreAdvice_Type.__name__=_F
_HwStorageReportingAlarmRestoreAdvice_Object=MibScalar
hwStorageReportingAlarmRestoreAdvice=_HwStorageReportingAlarmRestoreAdvice_Object((1,3,6,1,4,1,2011,2,251,20,1,3,3),_HwStorageReportingAlarmRestoreAdvice_Type())
hwStorageReportingAlarmRestoreAdvice.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmRestoreAdvice.setStatus(_B)
class _HwStorageReportingAlarmFaultTitle_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwStorageReportingAlarmFaultTitle_Type.__name__=_F
_HwStorageReportingAlarmFaultTitle_Object=MibScalar
hwStorageReportingAlarmFaultTitle=_HwStorageReportingAlarmFaultTitle_Object((1,3,6,1,4,1,2011,2,251,20,1,3,4),_HwStorageReportingAlarmFaultTitle_Type())
hwStorageReportingAlarmFaultTitle.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmFaultTitle.setStatus(_B)
class _HwStorageReportingAlarmFaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('communicationQuality',1),(_g,2),('processError',3),('serviceQuality',4),('environmentFault',5),('performanceLimit',6)))
_HwStorageReportingAlarmFaultType_Type.__name__=_E
_HwStorageReportingAlarmFaultType_Object=MibScalar
hwStorageReportingAlarmFaultType=_HwStorageReportingAlarmFaultType_Object((1,3,6,1,4,1,2011,2,251,20,1,3,5),_HwStorageReportingAlarmFaultType_Type())
hwStorageReportingAlarmFaultType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmFaultType.setStatus(_B)
class _HwStorageReportingAlarmFaultLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4)))
_HwStorageReportingAlarmFaultLevel_Type.__name__=_E
_HwStorageReportingAlarmFaultLevel_Object=MibScalar
hwStorageReportingAlarmFaultLevel=_HwStorageReportingAlarmFaultLevel_Object((1,3,6,1,4,1,2011,2,251,20,1,3,6),_HwStorageReportingAlarmFaultLevel_Type())
hwStorageReportingAlarmFaultLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmFaultLevel.setStatus(_B)
_HwStorageReportingAlarmAlarmID_Type=Gauge32
_HwStorageReportingAlarmAlarmID_Object=MibScalar
hwStorageReportingAlarmAlarmID=_HwStorageReportingAlarmAlarmID_Object((1,3,6,1,4,1,2011,2,251,20,1,3,7),_HwStorageReportingAlarmAlarmID_Type())
hwStorageReportingAlarmAlarmID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmAlarmID.setStatus(_B)
_HwStorageReportingAlarmFaultTime_Type=OctetString
_HwStorageReportingAlarmFaultTime_Object=MibScalar
hwStorageReportingAlarmFaultTime=_HwStorageReportingAlarmFaultTime_Object((1,3,6,1,4,1,2011,2,251,20,1,3,8),_HwStorageReportingAlarmFaultTime_Type())
hwStorageReportingAlarmFaultTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmFaultTime.setStatus(_B)
_HwStorageReportingAlarmSerialNo_Type=Gauge32
_HwStorageReportingAlarmSerialNo_Object=MibScalar
hwStorageReportingAlarmSerialNo=_HwStorageReportingAlarmSerialNo_Object((1,3,6,1,4,1,2011,2,251,20,1,3,9),_HwStorageReportingAlarmSerialNo_Type())
hwStorageReportingAlarmSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmSerialNo.setStatus(_B)
_HwStorageReportingAlarmAdditionInfo_Type=DisplayString
_HwStorageReportingAlarmAdditionInfo_Object=MibScalar
hwStorageReportingAlarmAdditionInfo=_HwStorageReportingAlarmAdditionInfo_Object((1,3,6,1,4,1,2011,2,251,20,1,3,10),_HwStorageReportingAlarmAdditionInfo_Type())
hwStorageReportingAlarmAdditionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmAdditionInfo.setStatus(_B)
class _HwStorageReportingAlarmFaultCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_HwStorageReportingAlarmFaultCategory_Type.__name__=_E
_HwStorageReportingAlarmFaultCategory_Object=MibScalar
hwStorageReportingAlarmFaultCategory=_HwStorageReportingAlarmFaultCategory_Object((1,3,6,1,4,1,2011,2,251,20,1,3,11),_HwStorageReportingAlarmFaultCategory_Type())
hwStorageReportingAlarmFaultCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmFaultCategory.setStatus(_B)
_HwStorageReportingAlarmLocationAlarmID_Type=Counter64
_HwStorageReportingAlarmLocationAlarmID_Object=MibScalar
hwStorageReportingAlarmLocationAlarmID=_HwStorageReportingAlarmLocationAlarmID_Object((1,3,6,1,4,1,2011,2,251,20,1,3,12),_HwStorageReportingAlarmLocationAlarmID_Type())
hwStorageReportingAlarmLocationAlarmID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmLocationAlarmID.setStatus(_B)
_HwStorageReportingAlarmProductModel_Type=Integer32
_HwStorageReportingAlarmProductModel_Object=MibScalar
hwStorageReportingAlarmProductModel=_HwStorageReportingAlarmProductModel_Object((1,3,6,1,4,1,2011,2,251,20,1,3,13),_HwStorageReportingAlarmProductModel_Type())
hwStorageReportingAlarmProductModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmProductModel.setStatus(_B)
_HwStorageReportingAlarmProductSN_Type=OctetString
_HwStorageReportingAlarmProductSN_Object=MibScalar
hwStorageReportingAlarmProductSN=_HwStorageReportingAlarmProductSN_Object((1,3,6,1,4,1,2011,2,251,20,1,3,14),_HwStorageReportingAlarmProductSN_Type())
hwStorageReportingAlarmProductSN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageReportingAlarmProductSN.setStatus(_B)
_HwStorageEvent_ObjectIdentity=ObjectIdentity
hwStorageEvent=_HwStorageEvent_ObjectIdentity((1,3,6,1,4,1,2011,2,251,20,2))
_NotificationType_ObjectIdentity=ObjectIdentity
notificationType=_NotificationType_ObjectIdentity((1,3,6,1,4,1,2011,2,251,20,2,1))
_TrapEvent_ObjectIdentity=ObjectIdentity
trapEvent=_TrapEvent_ObjectIdentity((1,3,6,1,4,1,2011,2,251,20,2,2))
_HwStorageTrapEventType_Type=Unsigned32
_HwStorageTrapEventType_Object=MibScalar
hwStorageTrapEventType=_HwStorageTrapEventType_Object((1,3,6,1,4,1,2011,2,251,20,2,2,1),_HwStorageTrapEventType_Type())
hwStorageTrapEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventType.setStatus(_B)
_HwStorageTrapEventID_Type=Counter64
_HwStorageTrapEventID_Object=MibScalar
hwStorageTrapEventID=_HwStorageTrapEventID_Object((1,3,6,1,4,1,2011,2,251,20,2,2,2),_HwStorageTrapEventID_Type())
hwStorageTrapEventID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventID.setStatus(_B)
_HwStorageTrapEventLevel_Type=Unsigned32
_HwStorageTrapEventLevel_Object=MibScalar
hwStorageTrapEventLevel=_HwStorageTrapEventLevel_Object((1,3,6,1,4,1,2011,2,251,20,2,2,3),_HwStorageTrapEventLevel_Type())
hwStorageTrapEventLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventLevel.setStatus(_B)
_HwStorageTrapEventSequence_Type=Unsigned32
_HwStorageTrapEventSequence_Object=MibScalar
hwStorageTrapEventSequence=_HwStorageTrapEventSequence_Object((1,3,6,1,4,1,2011,2,251,20,2,2,4),_HwStorageTrapEventSequence_Type())
hwStorageTrapEventSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventSequence.setStatus(_B)
_HwStorageTrapEventTime_Type=Unsigned32
_HwStorageTrapEventTime_Object=MibScalar
hwStorageTrapEventTime=_HwStorageTrapEventTime_Object((1,3,6,1,4,1,2011,2,251,20,2,2,5),_HwStorageTrapEventTime_Type())
hwStorageTrapEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventTime.setStatus(_B)
_HwStorageTrapEventRecoveryTime_Type=Unsigned32
_HwStorageTrapEventRecoveryTime_Object=MibScalar
hwStorageTrapEventRecoveryTime=_HwStorageTrapEventRecoveryTime_Object((1,3,6,1,4,1,2011,2,251,20,2,2,6),_HwStorageTrapEventRecoveryTime_Type())
hwStorageTrapEventRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventRecoveryTime.setStatus(_B)
_HwStorageTrapEventParameter_Type=OctetString
_HwStorageTrapEventParameter_Object=MibScalar
hwStorageTrapEventParameter=_HwStorageTrapEventParameter_Object((1,3,6,1,4,1,2011,2,251,20,2,2,7),_HwStorageTrapEventParameter_Type())
hwStorageTrapEventParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventParameter.setStatus(_B)
_HwStorageTrapEventID32Bit_Type=Unsigned32
_HwStorageTrapEventID32Bit_Object=MibScalar
hwStorageTrapEventID32Bit=_HwStorageTrapEventID32Bit_Object((1,3,6,1,4,1,2011,2,251,20,2,2,8),_HwStorageTrapEventID32Bit_Type())
hwStorageTrapEventID32Bit.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventID32Bit.setStatus(_B)
_HwStorageTrapEventTimeStr_Type=OctetString
_HwStorageTrapEventTimeStr_Object=MibScalar
hwStorageTrapEventTimeStr=_HwStorageTrapEventTimeStr_Object((1,3,6,1,4,1,2011,2,251,20,2,2,9),_HwStorageTrapEventTimeStr_Type())
hwStorageTrapEventTimeStr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventTimeStr.setStatus(_B)
_HwStorageTrapEventRecoveryTimeStr_Type=OctetString
_HwStorageTrapEventRecoveryTimeStr_Object=MibScalar
hwStorageTrapEventRecoveryTimeStr=_HwStorageTrapEventRecoveryTimeStr_Object((1,3,6,1,4,1,2011,2,251,20,2,2,10),_HwStorageTrapEventRecoveryTimeStr_Type())
hwStorageTrapEventRecoveryTimeStr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageTrapEventRecoveryTimeStr.setStatus(_B)
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_A,_G),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_H),(_A,_v),(_A,_w),(_A,_x),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_B)
hwStorageAlarmReporting=NotificationType((1,3,6,1,4,1,2011,2,251,20,1,2,1))
hwStorageAlarmReporting.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:hwStorageAlarmReporting.setStatus(_B)
hwStorageEventType=NotificationType((1,3,6,1,4,1,2011,2,251,20,2,1,1))
hwStorageEventType.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:hwStorageEventType.setStatus(_B)
currentNotificationGroup=NotificationGroup((1,6,1,2))
currentNotificationGroup.setObjects(*((_A,_y),(_A,_z)))
if mibBuilder.loadTexts:currentNotificationGroup.setStatus(_B)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects(*((_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:basicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'huawei':huawei,'products':products,'storage':storage,'alarm':alarm,'hwStorageNotification':hwStorageNotification,'hwStorageActiveAlarmInfo':hwStorageActiveAlarmInfo,'hwStorageActiveAlarmInfoTable':hwStorageActiveAlarmInfoTable,'hwStorageActiveAlarmInfoEntry':hwStorageActiveAlarmInfoEntry,_G:hwStorageActiveAlarmInfoNodeCode,_o:hwStorageActiveAlarmInfoLocationInfo,_p:hwStorageActiveAlarmInfoRestoreAdvice,_q:hwStorageActiveAlarmInfoTitle,_r:hwStorageActiveAlarmInfoType,_s:hwStorageActiveAlarmInfoLevel,_t:hwStorageActiveAlarmInfoAlarmID,_u:hwStorageActiveAlarmInfoOccurTime,_H:hwStorageActiveAlarmInfoSerialNo,_v:hwStorageActiveAlarmInfoAddtionInfo,_w:hwStorageActiveAlarmInfoCategory,_x:hwStorageActiveAlarmInfoLocalAlarmID,'hwStorageNotificationType':hwStorageNotificationType,_y:hwStorageAlarmReporting,'hwStorageReportingAlarm':hwStorageReportingAlarm,_I:hwStorageReportingAlarmNodeCode,_J:hwStorageReportingAlarmLocationInfo,_K:hwStorageReportingAlarmRestoreAdvice,_L:hwStorageReportingAlarmFaultTitle,_M:hwStorageReportingAlarmFaultType,_N:hwStorageReportingAlarmFaultLevel,_O:hwStorageReportingAlarmAlarmID,_P:hwStorageReportingAlarmFaultTime,_Q:hwStorageReportingAlarmSerialNo,_R:hwStorageReportingAlarmAdditionInfo,_S:hwStorageReportingAlarmFaultCategory,_T:hwStorageReportingAlarmLocationAlarmID,_U:hwStorageReportingAlarmProductModel,_V:hwStorageReportingAlarmProductSN,'hwStorageEvent':hwStorageEvent,'notificationType':notificationType,_z:hwStorageEventType,'trapEvent':trapEvent,_W:hwStorageTrapEventType,_X:hwStorageTrapEventID,_Y:hwStorageTrapEventLevel,_Z:hwStorageTrapEventSequence,_a:hwStorageTrapEventTime,_b:hwStorageTrapEventRecoveryTime,_c:hwStorageTrapEventParameter,_d:hwStorageTrapEventID32Bit,_e:hwStorageTrapEventTimeStr,_f:hwStorageTrapEventRecoveryTimeStr,'isoConformance':isoConformance,'isoGroups':isoGroups,_A0:currentObjectGroup,_A1:currentNotificationGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})