_AM='currentNotificationGroup'
_AL='currentObjectGroup'
_AK='hwIsmAlarmReporting'
_AJ='hwIsmEventNotiAddition'
_AI='hwIsmEventNotiAlarmID'
_AH='hwIsmEventNotiSerialNo'
_AG='hwIsmEventNotiFaultTime'
_AF='hwIsmEventNotiFaultType'
_AE='hwIsmEventNotiFaultTitle'
_AD='hwIsmEventNotiLocationInfo'
_AC='hwIsmEventNotiNodeCode'
_AB='hwIsmNENodeClusterName'
_AA='hwIsmNENodeWorkingMode'
_A9='hwIsmNENodeRunningStatus'
_A8='hwIsmTrapTargetAddrUSMUserName'
_A7='hwIsmTrapTargetAddrTrapType'
_A6='hwIsmTrapTargetAddrIPAddrNew'
_A5='hwIsmTrapTargetAddrTrapVer'
_A4='hwIsmReportingAlarmProductSN'
_A3='hwIsmReportingAlarmProductModel'
_A2='hwIsmActiveAlarmInfoLocalAlarmID'
_A1='hwIsmTrapTargetAddrRowStatus'
_A0='hwIsmTrapTargetAddrPort'
_z='hwIsmTrapTargetAddrIPAddr'
_y='hwIsmActiveAlarmInfoAddtionInfo'
_x='hwIsmClearedAlarmConfirm'
_w='hwIsmNENodeContextEngineID'
_v='hwIsmNENodeContextName'
_u='hwIsmNENodeIPAddress'
_t='hwIsmNENodeType'
_s='hwIsmActiveAlarmInfoCategory'
_r='hwIsmActiveAlarmInfoOccurTime'
_q='hwIsmActiveAlarmInfoAlarmID'
_p='hwIsmActiveAlarmInfoLevel'
_o='hwIsmActiveAlarmInfoType'
_n='hwIsmActiveAlarmInfoTitle'
_m='hwIsmActiveAlarmInfoRestoreAdvice'
_l='hwIsmActiveAlarmInfoLocationInfo'
_k='eventAlarm'
_j='resumeAlarm'
_i='faultAlarm'
_h='warningAlarm'
_g='minorAlarm'
_f='majorAlarm'
_e='criticalAlarm'
_d='performanceLimit'
_c='environmentFault'
_b='serviceQuality'
_a='processError'
_Z='equipmentFault'
_Y='communicationQuality'
_X='hwIsmReportingAlarmLocationAlarmID'
_W='hwIsmReportingAlarmAdditionInfo'
_V='hwIsmReportingAlarmFaultCategory'
_U='hwIsmReportingAlarmSerialNo'
_T='hwIsmReportingAlarmFaultTime'
_S='hwIsmReportingAlarmAlarmID'
_R='hwIsmReportingAlarmFaultLevel'
_Q='hwIsmReportingAlarmFaultType'
_P='hwIsmReportingAlarmFaultTitle'
_O='hwIsmReportingAlarmRestoreAdvice'
_N='hwIsmReportingAlarmLocationInfo'
_M='hwIsmReportingAlarmNodeCode'
_L='hwIsmTrapTargetAddrIndex'
_K='hwIsmActiveAlarmInfoSerialNo'
_J='hwIsmActiveAlarmInfoNodeCode'
_I='hwIsmNENodeCode'
_H='OctetString'
_G='read-write'
_F='read-create'
_E='Integer32'
_D='read-only'
_C='accessible-for-notify'
_B='ISM-HUAWEI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
hwISMCommon=ModuleIdentity((1,3,6,1,4,1,2011,2,91))
if mibBuilder.loadTexts:hwISMCommon.setRevisions(('2008-09-17 16:29',))
class NodeCodeString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(15,17))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,2011,2))
_HwIsmTopo_ObjectIdentity=ObjectIdentity
hwIsmTopo=_HwIsmTopo_ObjectIdentity((1,3,6,1,4,1,2011,2,91,9))
_HwIsmAccessNodeInfo_ObjectIdentity=ObjectIdentity
hwIsmAccessNodeInfo=_HwIsmAccessNodeInfo_ObjectIdentity((1,3,6,1,4,1,2011,2,91,9,1))
_HwIsmAccessNodeTable_Object=MibTable
hwIsmAccessNodeTable=_HwIsmAccessNodeTable_Object((1,3,6,1,4,1,2011,2,91,9,1,1))
if mibBuilder.loadTexts:hwIsmAccessNodeTable.setStatus(_A)
_HwIsmAccessNodeEntry_Object=MibTableRow
hwIsmAccessNodeEntry=_HwIsmAccessNodeEntry_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1))
hwIsmAccessNodeEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwIsmAccessNodeEntry.setStatus(_A)
_HwIsmNENodeCode_Type=NodeCodeString
_HwIsmNENodeCode_Object=MibTableColumn
hwIsmNENodeCode=_HwIsmNENodeCode_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,1),_HwIsmNENodeCode_Type())
hwIsmNENodeCode.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmNENodeCode.setStatus(_A)
_HwIsmNENodeType_Type=Integer32
_HwIsmNENodeType_Object=MibTableColumn
hwIsmNENodeType=_HwIsmNENodeType_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,2),_HwIsmNENodeType_Type())
hwIsmNENodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmNENodeType.setStatus(_A)
class _HwIsmNENodeWorkingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mode1',1),('mode2',2),('mode3',3),('mode4',4)))
_HwIsmNENodeWorkingMode_Type.__name__=_E
_HwIsmNENodeWorkingMode_Object=MibTableColumn
hwIsmNENodeWorkingMode=_HwIsmNENodeWorkingMode_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,3),_HwIsmNENodeWorkingMode_Type())
hwIsmNENodeWorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmNENodeWorkingMode.setStatus(_A)
_HwIsmNENodeIPAddress_Type=IpAddress
_HwIsmNENodeIPAddress_Object=MibTableColumn
hwIsmNENodeIPAddress=_HwIsmNENodeIPAddress_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,4),_HwIsmNENodeIPAddress_Type())
hwIsmNENodeIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmNENodeIPAddress.setStatus(_A)
_HwIsmNENodeContextName_Type=DisplayString
_HwIsmNENodeContextName_Object=MibTableColumn
hwIsmNENodeContextName=_HwIsmNENodeContextName_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,5),_HwIsmNENodeContextName_Type())
hwIsmNENodeContextName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmNENodeContextName.setStatus(_A)
_HwIsmNENodeContextEngineID_Type=DisplayString
_HwIsmNENodeContextEngineID_Object=MibTableColumn
hwIsmNENodeContextEngineID=_HwIsmNENodeContextEngineID_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,6),_HwIsmNENodeContextEngineID_Type())
hwIsmNENodeContextEngineID.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmNENodeContextEngineID.setStatus(_A)
_HwIsmNENodeClusterName_Type=DisplayString
_HwIsmNENodeClusterName_Object=MibTableColumn
hwIsmNENodeClusterName=_HwIsmNENodeClusterName_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,7),_HwIsmNENodeClusterName_Type())
hwIsmNENodeClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmNENodeClusterName.setStatus(_A)
class _HwIsmNENodeRunningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('admin',1),('freedom',2)))
_HwIsmNENodeRunningStatus_Type.__name__=_E
_HwIsmNENodeRunningStatus_Object=MibTableColumn
hwIsmNENodeRunningStatus=_HwIsmNENodeRunningStatus_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,8),_HwIsmNENodeRunningStatus_Type())
hwIsmNENodeRunningStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmNENodeRunningStatus.setStatus(_A)
_HwIsmNENodeId_Type=OctetString
_HwIsmNENodeId_Object=MibTableColumn
hwIsmNENodeId=_HwIsmNENodeId_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,9),_HwIsmNENodeId_Type())
hwIsmNENodeId.setMaxAccess(_G)
if mibBuilder.loadTexts:hwIsmNENodeId.setStatus(_A)
_HwIsmNENodeName_Type=OctetString
_HwIsmNENodeName_Object=MibTableColumn
hwIsmNENodeName=_HwIsmNENodeName_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,10),_HwIsmNENodeName_Type())
hwIsmNENodeName.setMaxAccess(_G)
if mibBuilder.loadTexts:hwIsmNENodeName.setStatus(_A)
_HwIsmNENodeArrayStatus_Type=Integer32
_HwIsmNENodeArrayStatus_Object=MibTableColumn
hwIsmNENodeArrayStatus=_HwIsmNENodeArrayStatus_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,11),_HwIsmNENodeArrayStatus_Type())
hwIsmNENodeArrayStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hwIsmNENodeArrayStatus.setStatus(_A)
_HwIsmNENodeLocation_Type=OctetString
_HwIsmNENodeLocation_Object=MibTableColumn
hwIsmNENodeLocation=_HwIsmNENodeLocation_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,12),_HwIsmNENodeLocation_Type())
hwIsmNENodeLocation.setMaxAccess(_G)
if mibBuilder.loadTexts:hwIsmNENodeLocation.setStatus(_A)
_HwIsmNENodeControllerIpList_Type=OctetString
_HwIsmNENodeControllerIpList_Object=MibTableColumn
hwIsmNENodeControllerIpList=_HwIsmNENodeControllerIpList_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,13),_HwIsmNENodeControllerIpList_Type())
hwIsmNENodeControllerIpList.setMaxAccess(_G)
if mibBuilder.loadTexts:hwIsmNENodeControllerIpList.setStatus(_A)
_HwIsmNEType_Type=Integer32
_HwIsmNEType_Object=MibTableColumn
hwIsmNEType=_HwIsmNEType_Object((1,3,6,1,4,1,2011,2,91,9,1,1,1,14),_HwIsmNEType_Type())
hwIsmNEType.setMaxAccess(_G)
if mibBuilder.loadTexts:hwIsmNEType.setStatus(_A)
_HwIsmNotification_ObjectIdentity=ObjectIdentity
hwIsmNotification=_HwIsmNotification_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10))
_HwIsmActiveAlarmInfo_ObjectIdentity=ObjectIdentity
hwIsmActiveAlarmInfo=_HwIsmActiveAlarmInfo_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,1))
_HwIsmActiveAlarmInfoTable_Object=MibTable
hwIsmActiveAlarmInfoTable=_HwIsmActiveAlarmInfoTable_Object((1,3,6,1,4,1,2011,2,91,10,1,1))
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoTable.setStatus(_A)
_HwIsmActiveAlarmInfoEntry_Object=MibTableRow
hwIsmActiveAlarmInfoEntry=_HwIsmActiveAlarmInfoEntry_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1))
hwIsmActiveAlarmInfoEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoEntry.setStatus(_A)
_HwIsmActiveAlarmInfoNodeCode_Type=NodeCodeString
_HwIsmActiveAlarmInfoNodeCode_Object=MibTableColumn
hwIsmActiveAlarmInfoNodeCode=_HwIsmActiveAlarmInfoNodeCode_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,1),_HwIsmActiveAlarmInfoNodeCode_Type())
hwIsmActiveAlarmInfoNodeCode.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoNodeCode.setStatus(_A)
_HwIsmActiveAlarmInfoLocationInfo_Type=DisplayString
_HwIsmActiveAlarmInfoLocationInfo_Object=MibTableColumn
hwIsmActiveAlarmInfoLocationInfo=_HwIsmActiveAlarmInfoLocationInfo_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,2),_HwIsmActiveAlarmInfoLocationInfo_Type())
hwIsmActiveAlarmInfoLocationInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoLocationInfo.setStatus(_A)
_HwIsmActiveAlarmInfoRestoreAdvice_Type=DisplayString
_HwIsmActiveAlarmInfoRestoreAdvice_Object=MibTableColumn
hwIsmActiveAlarmInfoRestoreAdvice=_HwIsmActiveAlarmInfoRestoreAdvice_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,3),_HwIsmActiveAlarmInfoRestoreAdvice_Type())
hwIsmActiveAlarmInfoRestoreAdvice.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoRestoreAdvice.setStatus(_A)
_HwIsmActiveAlarmInfoTitle_Type=DisplayString
_HwIsmActiveAlarmInfoTitle_Object=MibTableColumn
hwIsmActiveAlarmInfoTitle=_HwIsmActiveAlarmInfoTitle_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,4),_HwIsmActiveAlarmInfoTitle_Type())
hwIsmActiveAlarmInfoTitle.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoTitle.setStatus(_A)
class _HwIsmActiveAlarmInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4),(_c,5),(_d,6)))
_HwIsmActiveAlarmInfoType_Type.__name__=_E
_HwIsmActiveAlarmInfoType_Object=MibTableColumn
hwIsmActiveAlarmInfoType=_HwIsmActiveAlarmInfoType_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,5),_HwIsmActiveAlarmInfoType_Type())
hwIsmActiveAlarmInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoType.setStatus(_A)
class _HwIsmActiveAlarmInfoLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4)))
_HwIsmActiveAlarmInfoLevel_Type.__name__=_E
_HwIsmActiveAlarmInfoLevel_Object=MibTableColumn
hwIsmActiveAlarmInfoLevel=_HwIsmActiveAlarmInfoLevel_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,6),_HwIsmActiveAlarmInfoLevel_Type())
hwIsmActiveAlarmInfoLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoLevel.setStatus(_A)
_HwIsmActiveAlarmInfoAlarmID_Type=Gauge32
_HwIsmActiveAlarmInfoAlarmID_Object=MibTableColumn
hwIsmActiveAlarmInfoAlarmID=_HwIsmActiveAlarmInfoAlarmID_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,7),_HwIsmActiveAlarmInfoAlarmID_Type())
hwIsmActiveAlarmInfoAlarmID.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoAlarmID.setStatus(_A)
_HwIsmActiveAlarmInfoOccurTime_Type=DateAndTime
_HwIsmActiveAlarmInfoOccurTime_Object=MibTableColumn
hwIsmActiveAlarmInfoOccurTime=_HwIsmActiveAlarmInfoOccurTime_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,8),_HwIsmActiveAlarmInfoOccurTime_Type())
hwIsmActiveAlarmInfoOccurTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoOccurTime.setStatus(_A)
_HwIsmActiveAlarmInfoSerialNo_Type=Gauge32
_HwIsmActiveAlarmInfoSerialNo_Object=MibTableColumn
hwIsmActiveAlarmInfoSerialNo=_HwIsmActiveAlarmInfoSerialNo_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,9),_HwIsmActiveAlarmInfoSerialNo_Type())
hwIsmActiveAlarmInfoSerialNo.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoSerialNo.setStatus(_A)
_HwIsmActiveAlarmInfoAddtionInfo_Type=OctetString
_HwIsmActiveAlarmInfoAddtionInfo_Object=MibTableColumn
hwIsmActiveAlarmInfoAddtionInfo=_HwIsmActiveAlarmInfoAddtionInfo_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,10),_HwIsmActiveAlarmInfoAddtionInfo_Type())
hwIsmActiveAlarmInfoAddtionInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoAddtionInfo.setStatus(_A)
class _HwIsmActiveAlarmInfoCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_HwIsmActiveAlarmInfoCategory_Type.__name__=_E
_HwIsmActiveAlarmInfoCategory_Object=MibTableColumn
hwIsmActiveAlarmInfoCategory=_HwIsmActiveAlarmInfoCategory_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,11),_HwIsmActiveAlarmInfoCategory_Type())
hwIsmActiveAlarmInfoCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoCategory.setStatus(_A)
_HwIsmActiveAlarmInfoLocalAlarmID_Type=Counter64
_HwIsmActiveAlarmInfoLocalAlarmID_Object=MibTableColumn
hwIsmActiveAlarmInfoLocalAlarmID=_HwIsmActiveAlarmInfoLocalAlarmID_Object((1,3,6,1,4,1,2011,2,91,10,1,1,1,12),_HwIsmActiveAlarmInfoLocalAlarmID_Type())
hwIsmActiveAlarmInfoLocalAlarmID.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmActiveAlarmInfoLocalAlarmID.setStatus(_A)
_HwIsmClearedAlarmConfirm_Type=Gauge32
_HwIsmClearedAlarmConfirm_Object=MibScalar
hwIsmClearedAlarmConfirm=_HwIsmClearedAlarmConfirm_Object((1,3,6,1,4,1,2011,2,91,10,1,2),_HwIsmClearedAlarmConfirm_Type())
hwIsmClearedAlarmConfirm.setMaxAccess(_G)
if mibBuilder.loadTexts:hwIsmClearedAlarmConfirm.setStatus(_A)
_HwIsmNotificationType_ObjectIdentity=ObjectIdentity
hwIsmNotificationType=_HwIsmNotificationType_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,2))
_HwinfoFaultNotificationType_ObjectIdentity=ObjectIdentity
hwinfoFaultNotificationType=_HwinfoFaultNotificationType_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,2,1))
_HwIsmFaultNotificationTypeV2_ObjectIdentity=ObjectIdentity
hwIsmFaultNotificationTypeV2=_HwIsmFaultNotificationTypeV2_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,2,1,0))
if mibBuilder.loadTexts:hwIsmFaultNotificationTypeV2.setStatus(_A)
_HwIsmEventNotificationType_ObjectIdentity=ObjectIdentity
hwIsmEventNotificationType=_HwIsmEventNotificationType_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,2,2))
_HwIsmEventNotificationTypeV2_ObjectIdentity=ObjectIdentity
hwIsmEventNotificationTypeV2=_HwIsmEventNotificationTypeV2_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,2,2,0))
if mibBuilder.loadTexts:hwIsmEventNotificationTypeV2.setStatus(_A)
_HwIsmTrapNotification_ObjectIdentity=ObjectIdentity
hwIsmTrapNotification=_HwIsmTrapNotification_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,3))
_HwIsmFaultNotification_ObjectIdentity=ObjectIdentity
hwIsmFaultNotification=_HwIsmFaultNotification_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,3,1))
_HwIsmReportingAlarm_ObjectIdentity=ObjectIdentity
hwIsmReportingAlarm=_HwIsmReportingAlarm_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,3,1,1))
_HwIsmReportingAlarmNodeCode_Type=NodeCodeString
_HwIsmReportingAlarmNodeCode_Object=MibScalar
hwIsmReportingAlarmNodeCode=_HwIsmReportingAlarmNodeCode_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,1),_HwIsmReportingAlarmNodeCode_Type())
hwIsmReportingAlarmNodeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmNodeCode.setStatus(_A)
_HwIsmReportingAlarmLocationInfo_Type=DisplayString
_HwIsmReportingAlarmLocationInfo_Object=MibScalar
hwIsmReportingAlarmLocationInfo=_HwIsmReportingAlarmLocationInfo_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,2),_HwIsmReportingAlarmLocationInfo_Type())
hwIsmReportingAlarmLocationInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmLocationInfo.setStatus(_A)
class _HwIsmReportingAlarmRestoreAdvice_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwIsmReportingAlarmRestoreAdvice_Type.__name__=_H
_HwIsmReportingAlarmRestoreAdvice_Object=MibScalar
hwIsmReportingAlarmRestoreAdvice=_HwIsmReportingAlarmRestoreAdvice_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,3),_HwIsmReportingAlarmRestoreAdvice_Type())
hwIsmReportingAlarmRestoreAdvice.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmRestoreAdvice.setStatus(_A)
class _HwIsmReportingAlarmFaultTitle_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwIsmReportingAlarmFaultTitle_Type.__name__=_H
_HwIsmReportingAlarmFaultTitle_Object=MibScalar
hwIsmReportingAlarmFaultTitle=_HwIsmReportingAlarmFaultTitle_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,4),_HwIsmReportingAlarmFaultTitle_Type())
hwIsmReportingAlarmFaultTitle.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmFaultTitle.setStatus(_A)
class _HwIsmReportingAlarmFaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4),(_c,5),(_d,6)))
_HwIsmReportingAlarmFaultType_Type.__name__=_E
_HwIsmReportingAlarmFaultType_Object=MibScalar
hwIsmReportingAlarmFaultType=_HwIsmReportingAlarmFaultType_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,5),_HwIsmReportingAlarmFaultType_Type())
hwIsmReportingAlarmFaultType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmFaultType.setStatus(_A)
class _HwIsmReportingAlarmFaultLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4)))
_HwIsmReportingAlarmFaultLevel_Type.__name__=_E
_HwIsmReportingAlarmFaultLevel_Object=MibScalar
hwIsmReportingAlarmFaultLevel=_HwIsmReportingAlarmFaultLevel_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,6),_HwIsmReportingAlarmFaultLevel_Type())
hwIsmReportingAlarmFaultLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmFaultLevel.setStatus(_A)
_HwIsmReportingAlarmAlarmID_Type=Gauge32
_HwIsmReportingAlarmAlarmID_Object=MibScalar
hwIsmReportingAlarmAlarmID=_HwIsmReportingAlarmAlarmID_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,7),_HwIsmReportingAlarmAlarmID_Type())
hwIsmReportingAlarmAlarmID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmAlarmID.setStatus(_A)
_HwIsmReportingAlarmFaultTime_Type=DateAndTime
_HwIsmReportingAlarmFaultTime_Object=MibScalar
hwIsmReportingAlarmFaultTime=_HwIsmReportingAlarmFaultTime_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,8),_HwIsmReportingAlarmFaultTime_Type())
hwIsmReportingAlarmFaultTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmFaultTime.setStatus(_A)
_HwIsmReportingAlarmSerialNo_Type=Gauge32
_HwIsmReportingAlarmSerialNo_Object=MibScalar
hwIsmReportingAlarmSerialNo=_HwIsmReportingAlarmSerialNo_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,9),_HwIsmReportingAlarmSerialNo_Type())
hwIsmReportingAlarmSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmSerialNo.setStatus(_A)
_HwIsmReportingAlarmAdditionInfo_Type=DisplayString
_HwIsmReportingAlarmAdditionInfo_Object=MibScalar
hwIsmReportingAlarmAdditionInfo=_HwIsmReportingAlarmAdditionInfo_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,10),_HwIsmReportingAlarmAdditionInfo_Type())
hwIsmReportingAlarmAdditionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmAdditionInfo.setStatus(_A)
class _HwIsmReportingAlarmFaultCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_HwIsmReportingAlarmFaultCategory_Type.__name__=_E
_HwIsmReportingAlarmFaultCategory_Object=MibScalar
hwIsmReportingAlarmFaultCategory=_HwIsmReportingAlarmFaultCategory_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,11),_HwIsmReportingAlarmFaultCategory_Type())
hwIsmReportingAlarmFaultCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmFaultCategory.setStatus(_A)
_HwIsmReportingAlarmLocationAlarmID_Type=Counter64
_HwIsmReportingAlarmLocationAlarmID_Object=MibScalar
hwIsmReportingAlarmLocationAlarmID=_HwIsmReportingAlarmLocationAlarmID_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,12),_HwIsmReportingAlarmLocationAlarmID_Type())
hwIsmReportingAlarmLocationAlarmID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmLocationAlarmID.setStatus(_A)
_HwIsmReportingAlarmProductModel_Type=Integer32
_HwIsmReportingAlarmProductModel_Object=MibScalar
hwIsmReportingAlarmProductModel=_HwIsmReportingAlarmProductModel_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,13),_HwIsmReportingAlarmProductModel_Type())
hwIsmReportingAlarmProductModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmProductModel.setStatus(_A)
_HwIsmReportingAlarmProductSN_Type=OctetString
_HwIsmReportingAlarmProductSN_Object=MibScalar
hwIsmReportingAlarmProductSN=_HwIsmReportingAlarmProductSN_Object((1,3,6,1,4,1,2011,2,91,10,3,1,1,14),_HwIsmReportingAlarmProductSN_Type())
hwIsmReportingAlarmProductSN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmReportingAlarmProductSN.setStatus(_A)
_HwIsmEventNotification_ObjectIdentity=ObjectIdentity
hwIsmEventNotification=_HwIsmEventNotification_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,3,2))
_HwIsmEventNotiNodeCode_Type=NodeCodeString
_HwIsmEventNotiNodeCode_Object=MibScalar
hwIsmEventNotiNodeCode=_HwIsmEventNotiNodeCode_Object((1,3,6,1,4,1,2011,2,91,10,3,2,1),_HwIsmEventNotiNodeCode_Type())
hwIsmEventNotiNodeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmEventNotiNodeCode.setStatus(_A)
_HwIsmEventNotiLocationInfo_Type=DisplayString
_HwIsmEventNotiLocationInfo_Object=MibScalar
hwIsmEventNotiLocationInfo=_HwIsmEventNotiLocationInfo_Object((1,3,6,1,4,1,2011,2,91,10,3,2,2),_HwIsmEventNotiLocationInfo_Type())
hwIsmEventNotiLocationInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmEventNotiLocationInfo.setStatus(_A)
class _HwIsmEventNotiFaultTitle_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwIsmEventNotiFaultTitle_Type.__name__=_H
_HwIsmEventNotiFaultTitle_Object=MibScalar
hwIsmEventNotiFaultTitle=_HwIsmEventNotiFaultTitle_Object((1,3,6,1,4,1,2011,2,91,10,3,2,3),_HwIsmEventNotiFaultTitle_Type())
hwIsmEventNotiFaultTitle.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmEventNotiFaultTitle.setStatus(_A)
class _HwIsmEventNotiFaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('objectcreation',1),('objectdeletion',2),('statechanged',3)))
_HwIsmEventNotiFaultType_Type.__name__=_E
_HwIsmEventNotiFaultType_Object=MibScalar
hwIsmEventNotiFaultType=_HwIsmEventNotiFaultType_Object((1,3,6,1,4,1,2011,2,91,10,3,2,4),_HwIsmEventNotiFaultType_Type())
hwIsmEventNotiFaultType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmEventNotiFaultType.setStatus(_A)
_HwIsmEventNotiAddition_Type=DisplayString
_HwIsmEventNotiAddition_Object=MibScalar
hwIsmEventNotiAddition=_HwIsmEventNotiAddition_Object((1,3,6,1,4,1,2011,2,91,10,3,2,5),_HwIsmEventNotiAddition_Type())
hwIsmEventNotiAddition.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmEventNotiAddition.setStatus(_A)
_HwIsmEventNotiAlarmID_Type=Gauge32
_HwIsmEventNotiAlarmID_Object=MibScalar
hwIsmEventNotiAlarmID=_HwIsmEventNotiAlarmID_Object((1,3,6,1,4,1,2011,2,91,10,3,2,6),_HwIsmEventNotiAlarmID_Type())
hwIsmEventNotiAlarmID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmEventNotiAlarmID.setStatus(_A)
_HwIsmEventNotiFaultTime_Type=DateAndTime
_HwIsmEventNotiFaultTime_Object=MibScalar
hwIsmEventNotiFaultTime=_HwIsmEventNotiFaultTime_Object((1,3,6,1,4,1,2011,2,91,10,3,2,7),_HwIsmEventNotiFaultTime_Type())
hwIsmEventNotiFaultTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmEventNotiFaultTime.setStatus(_A)
_HwIsmEventNotiSerialNo_Type=Gauge32
_HwIsmEventNotiSerialNo_Object=MibScalar
hwIsmEventNotiSerialNo=_HwIsmEventNotiSerialNo_Object((1,3,6,1,4,1,2011,2,91,10,3,2,8),_HwIsmEventNotiSerialNo_Type())
hwIsmEventNotiSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmEventNotiSerialNo.setStatus(_A)
_HwIsmTrapForwardControl_ObjectIdentity=ObjectIdentity
hwIsmTrapForwardControl=_HwIsmTrapForwardControl_ObjectIdentity((1,3,6,1,4,1,2011,2,91,10,4))
_HwIsmTrapTargetAddrTable_Object=MibTable
hwIsmTrapTargetAddrTable=_HwIsmTrapTargetAddrTable_Object((1,3,6,1,4,1,2011,2,91,10,4,1))
if mibBuilder.loadTexts:hwIsmTrapTargetAddrTable.setStatus(_A)
_HwIsmTrapTargetAddrEntry_Object=MibTableRow
hwIsmTrapTargetAddrEntry=_HwIsmTrapTargetAddrEntry_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1))
hwIsmTrapTargetAddrEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:hwIsmTrapTargetAddrEntry.setStatus(_A)
_HwIsmTrapTargetAddrIPAddr_Type=IpAddress
_HwIsmTrapTargetAddrIPAddr_Object=MibTableColumn
hwIsmTrapTargetAddrIPAddr=_HwIsmTrapTargetAddrIPAddr_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1,1),_HwIsmTrapTargetAddrIPAddr_Type())
hwIsmTrapTargetAddrIPAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIsmTrapTargetAddrIPAddr.setStatus(_A)
_HwIsmTrapTargetAddrPort_Type=Integer32
_HwIsmTrapTargetAddrPort_Object=MibTableColumn
hwIsmTrapTargetAddrPort=_HwIsmTrapTargetAddrPort_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1,2),_HwIsmTrapTargetAddrPort_Type())
hwIsmTrapTargetAddrPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIsmTrapTargetAddrPort.setStatus(_A)
_HwIsmTrapTargetAddrRowStatus_Type=RowStatus
_HwIsmTrapTargetAddrRowStatus_Object=MibTableColumn
hwIsmTrapTargetAddrRowStatus=_HwIsmTrapTargetAddrRowStatus_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1,3),_HwIsmTrapTargetAddrRowStatus_Type())
hwIsmTrapTargetAddrRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIsmTrapTargetAddrRowStatus.setStatus(_A)
_HwIsmTrapTargetAddrIndex_Type=OctetString
_HwIsmTrapTargetAddrIndex_Object=MibTableColumn
hwIsmTrapTargetAddrIndex=_HwIsmTrapTargetAddrIndex_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1,4),_HwIsmTrapTargetAddrIndex_Type())
hwIsmTrapTargetAddrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIsmTrapTargetAddrIndex.setStatus(_A)
_HwIsmTrapTargetAddrTrapVer_Type=Integer32
_HwIsmTrapTargetAddrTrapVer_Object=MibTableColumn
hwIsmTrapTargetAddrTrapVer=_HwIsmTrapTargetAddrTrapVer_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1,5),_HwIsmTrapTargetAddrTrapVer_Type())
hwIsmTrapTargetAddrTrapVer.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIsmTrapTargetAddrTrapVer.setStatus(_A)
_HwIsmTrapTargetAddrIPAddrNew_Type=OctetString
_HwIsmTrapTargetAddrIPAddrNew_Object=MibTableColumn
hwIsmTrapTargetAddrIPAddrNew=_HwIsmTrapTargetAddrIPAddrNew_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1,6),_HwIsmTrapTargetAddrIPAddrNew_Type())
hwIsmTrapTargetAddrIPAddrNew.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIsmTrapTargetAddrIPAddrNew.setStatus(_A)
_HwIsmTrapTargetAddrTrapType_Type=Integer32
_HwIsmTrapTargetAddrTrapType_Object=MibTableColumn
hwIsmTrapTargetAddrTrapType=_HwIsmTrapTargetAddrTrapType_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1,7),_HwIsmTrapTargetAddrTrapType_Type())
hwIsmTrapTargetAddrTrapType.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIsmTrapTargetAddrTrapType.setStatus(_A)
_HwIsmTrapTargetAddrUSMUserName_Type=OctetString
_HwIsmTrapTargetAddrUSMUserName_Object=MibTableColumn
hwIsmTrapTargetAddrUSMUserName=_HwIsmTrapTargetAddrUSMUserName_Object((1,3,6,1,4,1,2011,2,91,10,4,1,1,8),_HwIsmTrapTargetAddrUSMUserName_Type())
hwIsmTrapTargetAddrUSMUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:hwIsmTrapTargetAddrUSMUserName.setStatus(_A)
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_B,_J),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_K),(_B,_s),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_I),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_X),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_L),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_A)
hwIsmAlarmReporting=NotificationType((1,3,6,1,4,1,2011,2,91,10,2,1,0,1))
hwIsmAlarmReporting.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_X),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:hwIsmAlarmReporting.setStatus(_A)
hwIsmEvent=NotificationType((1,3,6,1,4,1,2011,2,91,10,2,2,0,1))
hwIsmEvent.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:hwIsmEvent.setStatus(_A)
currentNotificationGroup=NotificationGroup((1,6,1,2))
currentNotificationGroup.setObjects((_B,_AK))
if mibBuilder.loadTexts:currentNotificationGroup.setStatus(_A)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects(*((_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:basicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NodeCodeString':NodeCodeString,'huawei':huawei,'products':products,'hwISMCommon':hwISMCommon,'hwIsmTopo':hwIsmTopo,'hwIsmAccessNodeInfo':hwIsmAccessNodeInfo,'hwIsmAccessNodeTable':hwIsmAccessNodeTable,'hwIsmAccessNodeEntry':hwIsmAccessNodeEntry,_I:hwIsmNENodeCode,_t:hwIsmNENodeType,_AA:hwIsmNENodeWorkingMode,_u:hwIsmNENodeIPAddress,_v:hwIsmNENodeContextName,_w:hwIsmNENodeContextEngineID,_AB:hwIsmNENodeClusterName,_A9:hwIsmNENodeRunningStatus,'hwIsmNENodeId':hwIsmNENodeId,'hwIsmNENodeName':hwIsmNENodeName,'hwIsmNENodeArrayStatus':hwIsmNENodeArrayStatus,'hwIsmNENodeLocation':hwIsmNENodeLocation,'hwIsmNENodeControllerIpList':hwIsmNENodeControllerIpList,'hwIsmNEType':hwIsmNEType,'hwIsmNotification':hwIsmNotification,'hwIsmActiveAlarmInfo':hwIsmActiveAlarmInfo,'hwIsmActiveAlarmInfoTable':hwIsmActiveAlarmInfoTable,'hwIsmActiveAlarmInfoEntry':hwIsmActiveAlarmInfoEntry,_J:hwIsmActiveAlarmInfoNodeCode,_l:hwIsmActiveAlarmInfoLocationInfo,_m:hwIsmActiveAlarmInfoRestoreAdvice,_n:hwIsmActiveAlarmInfoTitle,_o:hwIsmActiveAlarmInfoType,_p:hwIsmActiveAlarmInfoLevel,_q:hwIsmActiveAlarmInfoAlarmID,_r:hwIsmActiveAlarmInfoOccurTime,_K:hwIsmActiveAlarmInfoSerialNo,_y:hwIsmActiveAlarmInfoAddtionInfo,_s:hwIsmActiveAlarmInfoCategory,_A2:hwIsmActiveAlarmInfoLocalAlarmID,_x:hwIsmClearedAlarmConfirm,'hwIsmNotificationType':hwIsmNotificationType,'hwinfoFaultNotificationType':hwinfoFaultNotificationType,'hwIsmFaultNotificationTypeV2':hwIsmFaultNotificationTypeV2,_AK:hwIsmAlarmReporting,'hwIsmEventNotificationType':hwIsmEventNotificationType,'hwIsmEventNotificationTypeV2':hwIsmEventNotificationTypeV2,'hwIsmEvent':hwIsmEvent,'hwIsmTrapNotification':hwIsmTrapNotification,'hwIsmFaultNotification':hwIsmFaultNotification,'hwIsmReportingAlarm':hwIsmReportingAlarm,_M:hwIsmReportingAlarmNodeCode,_N:hwIsmReportingAlarmLocationInfo,_O:hwIsmReportingAlarmRestoreAdvice,_P:hwIsmReportingAlarmFaultTitle,_Q:hwIsmReportingAlarmFaultType,_R:hwIsmReportingAlarmFaultLevel,_S:hwIsmReportingAlarmAlarmID,_T:hwIsmReportingAlarmFaultTime,_U:hwIsmReportingAlarmSerialNo,_W:hwIsmReportingAlarmAdditionInfo,_V:hwIsmReportingAlarmFaultCategory,_X:hwIsmReportingAlarmLocationAlarmID,_A3:hwIsmReportingAlarmProductModel,_A4:hwIsmReportingAlarmProductSN,'hwIsmEventNotification':hwIsmEventNotification,_AC:hwIsmEventNotiNodeCode,_AD:hwIsmEventNotiLocationInfo,_AE:hwIsmEventNotiFaultTitle,_AF:hwIsmEventNotiFaultType,_AJ:hwIsmEventNotiAddition,_AI:hwIsmEventNotiAlarmID,_AG:hwIsmEventNotiFaultTime,_AH:hwIsmEventNotiSerialNo,'hwIsmTrapForwardControl':hwIsmTrapForwardControl,'hwIsmTrapTargetAddrTable':hwIsmTrapTargetAddrTable,'hwIsmTrapTargetAddrEntry':hwIsmTrapTargetAddrEntry,_z:hwIsmTrapTargetAddrIPAddr,_A0:hwIsmTrapTargetAddrPort,_A1:hwIsmTrapTargetAddrRowStatus,_L:hwIsmTrapTargetAddrIndex,_A5:hwIsmTrapTargetAddrTrapVer,_A6:hwIsmTrapTargetAddrIPAddrNew,_A7:hwIsmTrapTargetAddrTrapType,_A8:hwIsmTrapTargetAddrUSMUserName,'isoConformance':isoConformance,'isoGroups':isoGroups,_AL:currentObjectGroup,_AM:currentNotificationGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})