_z='ciscoExtScsiConfigGroup2'
_y='ciscoExtScsiConfigGroup1'
_x='ciscoExtScsiLunDiscDoneNotify'
_w='ciscoExtScsiDiscType'
_v='ciscoExtScsiIntrDiscLunPortId'
_u='ciscoExtScsiPartialLunRowStatus'
_t='ciscoExtScsiNotificationCntl'
_s='ciscoExtScsiIntrDiscLunsEntry'
_r='ciscoExtScsiIntrDiscTgtEntry'
_q='ciscoExtScsiGenInstanceEntry'
_p='LunDiscOS'
_o='ciscoExtScsiPartialLunDomId'
_n='TruthValue'
_m='Unsigned32'
_l='vsanIndex'
_k='CISCO-VSAN-MIB'
_j='VsanIndex'
_i='FcAddressId'
_h='ciscoExtScsiConfigGroup'
_g='ciscoExtScsiLunCacheTgtIndex'
_f='ciscoExtScsiLunCachePortIndex'
_e='ciscoExtScsiLunCacheDevIndex'
_d='ciscoExtScsiLunCacheScsiIndex'
_c='ciscoExtScsiLunDiscPortId'
_b='ciscoExtScsiLunDiscVsanId'
_a='ciscoExtScsiIntrDiscLunOs'
_Z='ciscoExtScsiLunDiscOs'
_Y='ciscoExtScsiPartialDiscGroup'
_X='ciscoExtScsiIntrDiscLunSerialNum'
_W='ciscoExtScsiIntrDiscLunNumber'
_V='ciscoExtScsiIntrDiscLunCapacity'
_U='ciscoExtScsiIntrDiscTgtOtherInfo'
_T='ciscoExtScsiIntrDiscTgtRevLevel'
_S='ciscoExtScsiIntrDiscTgtProductId'
_R='ciscoExtScsiIntrDiscTgtVendorId'
_Q='ciscoExtScsiIntrDiscTgtDevType'
_P='ciscoExtScsiIntrDiscTgtVsanId'
_O='ciscoExtScsiLunDiscCompleteTime'
_N='ciscoExtScsiStartLunDisc'
_M='ciscoExtScsiLunDiscSpinLock'
_L='ciscoExtScsiLineCardOrSup'
_K='ciscoExtScsiDiskGrpId'
_J='Integer32'
_I='ciscoExtScsiNotifyGroup'
_H='ciscoExtScsiNotifyControlGroup'
_G='deprecated'
_F='ciscoExtScsiLunDiscStatus'
_E='read-write'
_D='OctetString'
_C='read-only'
_B='current'
_A='CISCO-EXT-SCSI-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ScsiIndexValue,ciscoScsiDscLunEntry,ciscoScsiDscTgtEntry,ciscoScsiInstanceEntry=mibBuilder.importSymbols('CISCO-SCSI-MIB','ScsiIndexValue','ciscoScsiDscLunEntry','ciscoScsiDscTgtEntry','ciscoScsiInstanceEntry')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
DomainId,FcAddressId,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','DomainId',_i,_j)
vsanIndex,=mibBuilder.importSymbols(_k,_l)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_m,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp',_n)
ciscoExtScsiMIB=ModuleIdentity((1,3,6,1,4,1,9,9,299))
if mibBuilder.loadTexts:ciscoExtScsiMIB.setRevisions(('2004-03-14 00:00','2003-11-28 00:00','2003-01-28 00:00','2002-10-10 00:00','2002-10-05 00:00'))
class LunDiscOS(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('windows',1),('aix',2),('solaris',3),('linux',4),('hpux',5),('all',6)))
_CiscoExtScsiMIBObjects_ObjectIdentity=ObjectIdentity
ciscoExtScsiMIBObjects=_CiscoExtScsiMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,299,1))
_CiscoExtScsiConfiguration_ObjectIdentity=ObjectIdentity
ciscoExtScsiConfiguration=_CiscoExtScsiConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,299,1,1))
_CiscoExtScsiGenInstanceTable_Object=MibTable
ciscoExtScsiGenInstanceTable=_CiscoExtScsiGenInstanceTable_Object((1,3,6,1,4,1,9,9,299,1,1,1))
if mibBuilder.loadTexts:ciscoExtScsiGenInstanceTable.setStatus(_B)
_CiscoExtScsiGenInstanceEntry_Object=MibTableRow
ciscoExtScsiGenInstanceEntry=_CiscoExtScsiGenInstanceEntry_Object((1,3,6,1,4,1,9,9,299,1,1,1,1))
if mibBuilder.loadTexts:ciscoExtScsiGenInstanceEntry.setStatus(_B)
class _CiscoExtScsiDiskGrpId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(64,64))
_CiscoExtScsiDiskGrpId_Type.__name__=_D
_CiscoExtScsiDiskGrpId_Object=MibTableColumn
ciscoExtScsiDiskGrpId=_CiscoExtScsiDiskGrpId_Object((1,3,6,1,4,1,9,9,299,1,1,1,1,1),_CiscoExtScsiDiskGrpId_Type())
ciscoExtScsiDiskGrpId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiDiskGrpId.setStatus(_B)
class _CiscoExtScsiLineCardOrSup_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoExtScsiLineCardOrSup_Type.__name__=_m
_CiscoExtScsiLineCardOrSup_Object=MibTableColumn
ciscoExtScsiLineCardOrSup=_CiscoExtScsiLineCardOrSup_Object((1,3,6,1,4,1,9,9,299,1,1,1,1,2),_CiscoExtScsiLineCardOrSup_Type())
ciscoExtScsiLineCardOrSup.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiLineCardOrSup.setStatus(_B)
_CiscoExtScsiLunDiscSpinLock_Type=TestAndIncr
_CiscoExtScsiLunDiscSpinLock_Object=MibScalar
ciscoExtScsiLunDiscSpinLock=_CiscoExtScsiLunDiscSpinLock_Object((1,3,6,1,4,1,9,9,299,1,1,2),_CiscoExtScsiLunDiscSpinLock_Type())
ciscoExtScsiLunDiscSpinLock.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoExtScsiLunDiscSpinLock.setStatus(_B)
class _CiscoExtScsiStartLunDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('startDiscovery',1),('startLocalDiscovery',2),('startRemoteDiscovery',3),('noop',4),('startPartialDiscovery',5),('startPortBasedDiscovery',6)))
_CiscoExtScsiStartLunDisc_Type.__name__=_J
_CiscoExtScsiStartLunDisc_Object=MibScalar
ciscoExtScsiStartLunDisc=_CiscoExtScsiStartLunDisc_Object((1,3,6,1,4,1,9,9,299,1,1,3),_CiscoExtScsiStartLunDisc_Type())
ciscoExtScsiStartLunDisc.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoExtScsiStartLunDisc.setStatus(_B)
class _CiscoExtScsiLunDiscStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inProgress',1),('completed',2),('failure',3)))
_CiscoExtScsiLunDiscStatus_Type.__name__=_J
_CiscoExtScsiLunDiscStatus_Object=MibScalar
ciscoExtScsiLunDiscStatus=_CiscoExtScsiLunDiscStatus_Object((1,3,6,1,4,1,9,9,299,1,1,4),_CiscoExtScsiLunDiscStatus_Type())
ciscoExtScsiLunDiscStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiLunDiscStatus.setStatus(_B)
_CiscoExtScsiLunDiscCompleteTime_Type=TimeStamp
_CiscoExtScsiLunDiscCompleteTime_Object=MibScalar
ciscoExtScsiLunDiscCompleteTime=_CiscoExtScsiLunDiscCompleteTime_Object((1,3,6,1,4,1,9,9,299,1,1,5),_CiscoExtScsiLunDiscCompleteTime_Type())
ciscoExtScsiLunDiscCompleteTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiLunDiscCompleteTime.setStatus(_B)
_CiscoExtScsiIntrDiscTgtTable_Object=MibTable
ciscoExtScsiIntrDiscTgtTable=_CiscoExtScsiIntrDiscTgtTable_Object((1,3,6,1,4,1,9,9,299,1,1,6))
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscTgtTable.setStatus(_B)
_CiscoExtScsiIntrDiscTgtEntry_Object=MibTableRow
ciscoExtScsiIntrDiscTgtEntry=_CiscoExtScsiIntrDiscTgtEntry_Object((1,3,6,1,4,1,9,9,299,1,1,6,1))
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscTgtEntry.setStatus(_B)
_CiscoExtScsiIntrDiscTgtVsanId_Type=VsanIndex
_CiscoExtScsiIntrDiscTgtVsanId_Object=MibTableColumn
ciscoExtScsiIntrDiscTgtVsanId=_CiscoExtScsiIntrDiscTgtVsanId_Object((1,3,6,1,4,1,9,9,299,1,1,6,1,1),_CiscoExtScsiIntrDiscTgtVsanId_Type())
ciscoExtScsiIntrDiscTgtVsanId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscTgtVsanId.setStatus(_B)
_CiscoExtScsiIntrDiscTgtDevType_Type=Unsigned32
_CiscoExtScsiIntrDiscTgtDevType_Object=MibTableColumn
ciscoExtScsiIntrDiscTgtDevType=_CiscoExtScsiIntrDiscTgtDevType_Object((1,3,6,1,4,1,9,9,299,1,1,6,1,2),_CiscoExtScsiIntrDiscTgtDevType_Type())
ciscoExtScsiIntrDiscTgtDevType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscTgtDevType.setStatus(_B)
class _CiscoExtScsiIntrDiscTgtVendorId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CiscoExtScsiIntrDiscTgtVendorId_Type.__name__=_D
_CiscoExtScsiIntrDiscTgtVendorId_Object=MibTableColumn
ciscoExtScsiIntrDiscTgtVendorId=_CiscoExtScsiIntrDiscTgtVendorId_Object((1,3,6,1,4,1,9,9,299,1,1,6,1,3),_CiscoExtScsiIntrDiscTgtVendorId_Type())
ciscoExtScsiIntrDiscTgtVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscTgtVendorId.setStatus(_B)
class _CiscoExtScsiIntrDiscTgtProductId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CiscoExtScsiIntrDiscTgtProductId_Type.__name__=_D
_CiscoExtScsiIntrDiscTgtProductId_Object=MibTableColumn
ciscoExtScsiIntrDiscTgtProductId=_CiscoExtScsiIntrDiscTgtProductId_Object((1,3,6,1,4,1,9,9,299,1,1,6,1,4),_CiscoExtScsiIntrDiscTgtProductId_Type())
ciscoExtScsiIntrDiscTgtProductId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscTgtProductId.setStatus(_B)
class _CiscoExtScsiIntrDiscTgtRevLevel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CiscoExtScsiIntrDiscTgtRevLevel_Type.__name__=_D
_CiscoExtScsiIntrDiscTgtRevLevel_Object=MibTableColumn
ciscoExtScsiIntrDiscTgtRevLevel=_CiscoExtScsiIntrDiscTgtRevLevel_Object((1,3,6,1,4,1,9,9,299,1,1,6,1,5),_CiscoExtScsiIntrDiscTgtRevLevel_Type())
ciscoExtScsiIntrDiscTgtRevLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscTgtRevLevel.setStatus(_B)
class _CiscoExtScsiIntrDiscTgtOtherInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CiscoExtScsiIntrDiscTgtOtherInfo_Type.__name__=_D
_CiscoExtScsiIntrDiscTgtOtherInfo_Object=MibTableColumn
ciscoExtScsiIntrDiscTgtOtherInfo=_CiscoExtScsiIntrDiscTgtOtherInfo_Object((1,3,6,1,4,1,9,9,299,1,1,6,1,6),_CiscoExtScsiIntrDiscTgtOtherInfo_Type())
ciscoExtScsiIntrDiscTgtOtherInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscTgtOtherInfo.setStatus(_B)
_CiscoExtScsiIntrDiscLunsTable_Object=MibTable
ciscoExtScsiIntrDiscLunsTable=_CiscoExtScsiIntrDiscLunsTable_Object((1,3,6,1,4,1,9,9,299,1,1,7))
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscLunsTable.setStatus(_B)
_CiscoExtScsiIntrDiscLunsEntry_Object=MibTableRow
ciscoExtScsiIntrDiscLunsEntry=_CiscoExtScsiIntrDiscLunsEntry_Object((1,3,6,1,4,1,9,9,299,1,1,7,1))
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscLunsEntry.setStatus(_B)
_CiscoExtScsiIntrDiscLunCapacity_Type=Unsigned32
_CiscoExtScsiIntrDiscLunCapacity_Object=MibTableColumn
ciscoExtScsiIntrDiscLunCapacity=_CiscoExtScsiIntrDiscLunCapacity_Object((1,3,6,1,4,1,9,9,299,1,1,7,1,1),_CiscoExtScsiIntrDiscLunCapacity_Type())
ciscoExtScsiIntrDiscLunCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscLunCapacity.setStatus(_B)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscLunCapacity.setUnits('MBytes')
class _CiscoExtScsiIntrDiscLunNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CiscoExtScsiIntrDiscLunNumber_Type.__name__=_D
_CiscoExtScsiIntrDiscLunNumber_Object=MibTableColumn
ciscoExtScsiIntrDiscLunNumber=_CiscoExtScsiIntrDiscLunNumber_Object((1,3,6,1,4,1,9,9,299,1,1,7,1,2),_CiscoExtScsiIntrDiscLunNumber_Type())
ciscoExtScsiIntrDiscLunNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscLunNumber.setStatus(_B)
class _CiscoExtScsiIntrDiscLunSerialNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoExtScsiIntrDiscLunSerialNum_Type.__name__=_D
_CiscoExtScsiIntrDiscLunSerialNum_Object=MibTableColumn
ciscoExtScsiIntrDiscLunSerialNum=_CiscoExtScsiIntrDiscLunSerialNum_Object((1,3,6,1,4,1,9,9,299,1,1,7,1,3),_CiscoExtScsiIntrDiscLunSerialNum_Type())
ciscoExtScsiIntrDiscLunSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscLunSerialNum.setStatus(_B)
_CiscoExtScsiIntrDiscLunOs_Type=LunDiscOS
_CiscoExtScsiIntrDiscLunOs_Object=MibTableColumn
ciscoExtScsiIntrDiscLunOs=_CiscoExtScsiIntrDiscLunOs_Object((1,3,6,1,4,1,9,9,299,1,1,7,1,4),_CiscoExtScsiIntrDiscLunOs_Type())
ciscoExtScsiIntrDiscLunOs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscLunOs.setStatus(_B)
_CiscoExtScsiIntrDiscLunPortId_Type=FcAddressId
_CiscoExtScsiIntrDiscLunPortId_Object=MibTableColumn
ciscoExtScsiIntrDiscLunPortId=_CiscoExtScsiIntrDiscLunPortId_Object((1,3,6,1,4,1,9,9,299,1,1,7,1,5),_CiscoExtScsiIntrDiscLunPortId_Type())
ciscoExtScsiIntrDiscLunPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiIntrDiscLunPortId.setStatus(_B)
class _CiscoExtScsiNotificationCntl_Type(TruthValue):defaultValue=2
_CiscoExtScsiNotificationCntl_Type.__name__=_n
_CiscoExtScsiNotificationCntl_Object=MibScalar
ciscoExtScsiNotificationCntl=_CiscoExtScsiNotificationCntl_Object((1,3,6,1,4,1,9,9,299,1,1,8),_CiscoExtScsiNotificationCntl_Type())
ciscoExtScsiNotificationCntl.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoExtScsiNotificationCntl.setStatus(_B)
_CiscoExtScsiPartialLunDiscTable_Object=MibTable
ciscoExtScsiPartialLunDiscTable=_CiscoExtScsiPartialLunDiscTable_Object((1,3,6,1,4,1,9,9,299,1,1,9))
if mibBuilder.loadTexts:ciscoExtScsiPartialLunDiscTable.setStatus(_B)
_CiscoExtScsiPartialLunDiscEntry_Object=MibTableRow
ciscoExtScsiPartialLunDiscEntry=_CiscoExtScsiPartialLunDiscEntry_Object((1,3,6,1,4,1,9,9,299,1,1,9,1))
ciscoExtScsiPartialLunDiscEntry.setIndexNames((0,_k,_l),(0,_A,_o))
if mibBuilder.loadTexts:ciscoExtScsiPartialLunDiscEntry.setStatus(_B)
_CiscoExtScsiPartialLunDomId_Type=DomainId
_CiscoExtScsiPartialLunDomId_Object=MibTableColumn
ciscoExtScsiPartialLunDomId=_CiscoExtScsiPartialLunDomId_Object((1,3,6,1,4,1,9,9,299,1,1,9,1,1),_CiscoExtScsiPartialLunDomId_Type())
ciscoExtScsiPartialLunDomId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoExtScsiPartialLunDomId.setStatus(_B)
_CiscoExtScsiPartialLunRowStatus_Type=RowStatus
_CiscoExtScsiPartialLunRowStatus_Object=MibTableColumn
ciscoExtScsiPartialLunRowStatus=_CiscoExtScsiPartialLunRowStatus_Object((1,3,6,1,4,1,9,9,299,1,1,9,1,2),_CiscoExtScsiPartialLunRowStatus_Type())
ciscoExtScsiPartialLunRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:ciscoExtScsiPartialLunRowStatus.setStatus(_B)
class _CiscoExtScsiLunDiscOs_Type(LunDiscOS):defaultValue=1
_CiscoExtScsiLunDiscOs_Type.__name__=_p
_CiscoExtScsiLunDiscOs_Object=MibScalar
ciscoExtScsiLunDiscOs=_CiscoExtScsiLunDiscOs_Object((1,3,6,1,4,1,9,9,299,1,1,10),_CiscoExtScsiLunDiscOs_Type())
ciscoExtScsiLunDiscOs.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoExtScsiLunDiscOs.setStatus(_B)
class _CiscoExtScsiLunDiscVsanId_Type(VsanIndex):defaultValue=1
_CiscoExtScsiLunDiscVsanId_Type.__name__=_j
_CiscoExtScsiLunDiscVsanId_Object=MibScalar
ciscoExtScsiLunDiscVsanId=_CiscoExtScsiLunDiscVsanId_Object((1,3,6,1,4,1,9,9,299,1,1,11),_CiscoExtScsiLunDiscVsanId_Type())
ciscoExtScsiLunDiscVsanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoExtScsiLunDiscVsanId.setStatus(_B)
class _CiscoExtScsiLunDiscPortId_Type(FcAddressId):defaultHexValue='000000'
_CiscoExtScsiLunDiscPortId_Type.__name__=_i
_CiscoExtScsiLunDiscPortId_Object=MibScalar
ciscoExtScsiLunDiscPortId=_CiscoExtScsiLunDiscPortId_Object((1,3,6,1,4,1,9,9,299,1,1,12),_CiscoExtScsiLunDiscPortId_Type())
ciscoExtScsiLunDiscPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoExtScsiLunDiscPortId.setStatus(_B)
_CiscoExtScsiLunCacheScsiIndex_Type=ScsiIndexValue
_CiscoExtScsiLunCacheScsiIndex_Object=MibScalar
ciscoExtScsiLunCacheScsiIndex=_CiscoExtScsiLunCacheScsiIndex_Object((1,3,6,1,4,1,9,9,299,1,1,13),_CiscoExtScsiLunCacheScsiIndex_Type())
ciscoExtScsiLunCacheScsiIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiLunCacheScsiIndex.setStatus(_B)
_CiscoExtScsiLunCacheDevIndex_Type=ScsiIndexValue
_CiscoExtScsiLunCacheDevIndex_Object=MibScalar
ciscoExtScsiLunCacheDevIndex=_CiscoExtScsiLunCacheDevIndex_Object((1,3,6,1,4,1,9,9,299,1,1,14),_CiscoExtScsiLunCacheDevIndex_Type())
ciscoExtScsiLunCacheDevIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiLunCacheDevIndex.setStatus(_B)
_CiscoExtScsiLunCachePortIndex_Type=ScsiIndexValue
_CiscoExtScsiLunCachePortIndex_Object=MibScalar
ciscoExtScsiLunCachePortIndex=_CiscoExtScsiLunCachePortIndex_Object((1,3,6,1,4,1,9,9,299,1,1,15),_CiscoExtScsiLunCachePortIndex_Type())
ciscoExtScsiLunCachePortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiLunCachePortIndex.setStatus(_B)
_CiscoExtScsiLunCacheTgtIndex_Type=ScsiIndexValue
_CiscoExtScsiLunCacheTgtIndex_Object=MibScalar
ciscoExtScsiLunCacheTgtIndex=_CiscoExtScsiLunCacheTgtIndex_Object((1,3,6,1,4,1,9,9,299,1,1,16),_CiscoExtScsiLunCacheTgtIndex_Type())
ciscoExtScsiLunCacheTgtIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoExtScsiLunCacheTgtIndex.setStatus(_B)
class _CiscoExtScsiDiscType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('targets',1),('luns',2)))
_CiscoExtScsiDiscType_Type.__name__=_J
_CiscoExtScsiDiscType_Object=MibScalar
ciscoExtScsiDiscType=_CiscoExtScsiDiscType_Object((1,3,6,1,4,1,9,9,299,1,1,17),_CiscoExtScsiDiscType_Type())
ciscoExtScsiDiscType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoExtScsiDiscType.setStatus(_B)
_CiscoExtScsiNotification_ObjectIdentity=ObjectIdentity
ciscoExtScsiNotification=_CiscoExtScsiNotification_ObjectIdentity((1,3,6,1,4,1,9,9,299,1,2))
_CiscoExtScsiNotifications_ObjectIdentity=ObjectIdentity
ciscoExtScsiNotifications=_CiscoExtScsiNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,299,1,2,0))
_CiscoExtScsiStats_ObjectIdentity=ObjectIdentity
ciscoExtScsiStats=_CiscoExtScsiStats_ObjectIdentity((1,3,6,1,4,1,9,9,299,1,3))
_CiscoExtScsiMIBConformance_ObjectIdentity=ObjectIdentity
ciscoExtScsiMIBConformance=_CiscoExtScsiMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,299,2))
_CiscoExtScsiMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoExtScsiMIBCompliances=_CiscoExtScsiMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,299,2,1))
_CiscoExtScsiMIBGroups_ObjectIdentity=ObjectIdentity
ciscoExtScsiMIBGroups=_CiscoExtScsiMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,299,2,2))
ciscoScsiInstanceEntry.registerAugmentions((_A,_q))
ciscoExtScsiGenInstanceEntry.setIndexNames(*ciscoScsiInstanceEntry.getIndexNames())
ciscoScsiDscTgtEntry.registerAugmentions((_A,_r))
ciscoExtScsiIntrDiscTgtEntry.setIndexNames(*ciscoScsiDscTgtEntry.getIndexNames())
ciscoScsiDscLunEntry.registerAugmentions((_A,_s))
ciscoExtScsiIntrDiscLunsEntry.setIndexNames(*ciscoScsiDscLunEntry.getIndexNames())
ciscoExtScsiConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,299,2,2,1))
ciscoExtScsiConfigGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_F),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoExtScsiConfigGroup.setStatus(_G)
ciscoExtScsiNotifyControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,299,2,2,2))
ciscoExtScsiNotifyControlGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:ciscoExtScsiNotifyControlGroup.setStatus(_B)
ciscoExtScsiPartialDiscGroup=ObjectGroup((1,3,6,1,4,1,9,9,299,2,2,4))
ciscoExtScsiPartialDiscGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:ciscoExtScsiPartialDiscGroup.setStatus(_B)
ciscoExtScsiConfigGroup1=ObjectGroup((1,3,6,1,4,1,9,9,299,2,2,5))
ciscoExtScsiConfigGroup1.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_Z),(_A,_N),(_A,_F),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoExtScsiConfigGroup1.setStatus(_G)
ciscoExtScsiConfigGroup2=ObjectGroup((1,3,6,1,4,1,9,9,299,2,2,6))
ciscoExtScsiConfigGroup2.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_Z),(_A,_N),(_A,_F),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_a),(_A,_v),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_w)))
if mibBuilder.loadTexts:ciscoExtScsiConfigGroup2.setStatus(_B)
ciscoExtScsiLunDiscDoneNotify=NotificationType((1,3,6,1,4,1,9,9,299,1,2,0,1))
ciscoExtScsiLunDiscDoneNotify.setObjects((_A,_F))
if mibBuilder.loadTexts:ciscoExtScsiLunDiscDoneNotify.setStatus(_B)
ciscoExtScsiNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,299,2,2,3))
ciscoExtScsiNotifyGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:ciscoExtScsiNotifyGroup.setStatus(_B)
ciscoExtScsiMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,299,2,1,1))
ciscoExtScsiMIBCompliance.setObjects(*((_A,_h),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ciscoExtScsiMIBCompliance.setStatus(_G)
ciscoExtScsiMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,299,2,1,2))
ciscoExtScsiMIBCompliance2.setObjects(*((_A,_h),(_A,_Y),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ciscoExtScsiMIBCompliance2.setStatus(_G)
ciscoExtScsiMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,299,2,1,3))
ciscoExtScsiMIBComplianceRev3.setObjects(*((_A,_y),(_A,_Y),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ciscoExtScsiMIBComplianceRev3.setStatus(_G)
ciscoExtScsiMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,299,2,1,4))
ciscoExtScsiMIBComplianceRev4.setObjects(*((_A,_z),(_A,_Y),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ciscoExtScsiMIBComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_p:LunDiscOS,'ciscoExtScsiMIB':ciscoExtScsiMIB,'ciscoExtScsiMIBObjects':ciscoExtScsiMIBObjects,'ciscoExtScsiConfiguration':ciscoExtScsiConfiguration,'ciscoExtScsiGenInstanceTable':ciscoExtScsiGenInstanceTable,_q:ciscoExtScsiGenInstanceEntry,_K:ciscoExtScsiDiskGrpId,_L:ciscoExtScsiLineCardOrSup,_M:ciscoExtScsiLunDiscSpinLock,_N:ciscoExtScsiStartLunDisc,_F:ciscoExtScsiLunDiscStatus,_O:ciscoExtScsiLunDiscCompleteTime,'ciscoExtScsiIntrDiscTgtTable':ciscoExtScsiIntrDiscTgtTable,_r:ciscoExtScsiIntrDiscTgtEntry,_P:ciscoExtScsiIntrDiscTgtVsanId,_Q:ciscoExtScsiIntrDiscTgtDevType,_R:ciscoExtScsiIntrDiscTgtVendorId,_S:ciscoExtScsiIntrDiscTgtProductId,_T:ciscoExtScsiIntrDiscTgtRevLevel,_U:ciscoExtScsiIntrDiscTgtOtherInfo,'ciscoExtScsiIntrDiscLunsTable':ciscoExtScsiIntrDiscLunsTable,_s:ciscoExtScsiIntrDiscLunsEntry,_V:ciscoExtScsiIntrDiscLunCapacity,_W:ciscoExtScsiIntrDiscLunNumber,_X:ciscoExtScsiIntrDiscLunSerialNum,_a:ciscoExtScsiIntrDiscLunOs,_v:ciscoExtScsiIntrDiscLunPortId,_t:ciscoExtScsiNotificationCntl,'ciscoExtScsiPartialLunDiscTable':ciscoExtScsiPartialLunDiscTable,'ciscoExtScsiPartialLunDiscEntry':ciscoExtScsiPartialLunDiscEntry,_o:ciscoExtScsiPartialLunDomId,_u:ciscoExtScsiPartialLunRowStatus,_Z:ciscoExtScsiLunDiscOs,_b:ciscoExtScsiLunDiscVsanId,_c:ciscoExtScsiLunDiscPortId,_d:ciscoExtScsiLunCacheScsiIndex,_e:ciscoExtScsiLunCacheDevIndex,_f:ciscoExtScsiLunCachePortIndex,_g:ciscoExtScsiLunCacheTgtIndex,_w:ciscoExtScsiDiscType,'ciscoExtScsiNotification':ciscoExtScsiNotification,'ciscoExtScsiNotifications':ciscoExtScsiNotifications,_x:ciscoExtScsiLunDiscDoneNotify,'ciscoExtScsiStats':ciscoExtScsiStats,'ciscoExtScsiMIBConformance':ciscoExtScsiMIBConformance,'ciscoExtScsiMIBCompliances':ciscoExtScsiMIBCompliances,'ciscoExtScsiMIBCompliance':ciscoExtScsiMIBCompliance,'ciscoExtScsiMIBCompliance2':ciscoExtScsiMIBCompliance2,'ciscoExtScsiMIBComplianceRev3':ciscoExtScsiMIBComplianceRev3,'ciscoExtScsiMIBComplianceRev4':ciscoExtScsiMIBComplianceRev4,'ciscoExtScsiMIBGroups':ciscoExtScsiMIBGroups,_h:ciscoExtScsiConfigGroup,_H:ciscoExtScsiNotifyControlGroup,_I:ciscoExtScsiNotifyGroup,_Y:ciscoExtScsiPartialDiscGroup,_y:ciscoExtScsiConfigGroup1,_z:ciscoExtScsiConfigGroup2})