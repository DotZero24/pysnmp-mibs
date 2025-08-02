_y='ciscoWebExMeetingMIBNotifsGroup'
_x='ciscoWebExCommSystemResourceGroup'
_w='ciscoWebExCommInfoGroup'
_v='cwCommSystemResourceUsageMajorEvent'
_u='cwCommSystemResourceUsageMinorEvent'
_t='cwCommSystemResourceUsageNormalEvent'
_s='cwCommDiskMonitoringStatus'
_r='cwCommDiskTotal'
_q='cwCommDiskUsage'
_p='cwCommDiskPartitionName'
_o='cwCommDiskUsageCount'
_n='cwCommMEMTotal'
_m='cwCommMEMSwapMonitoringStatus'
_l='cwCommMEMSwapUsage'
_k='cwCommMEMMonitoringStatus'
_j='cwCommMEMUsage'
_i='cwCommCPUCapacityTotal'
_h='cwCommCPUUsageCapacitySubTotal'
_g='cwCommCPUUsageSteal'
_f='cwCommCPUUsageSoftIRQ'
_e='cwCommCPUUsageIRQ'
_d='cwCommCPUUsageIOWait'
_c='cwCommCPUUsageIdle'
_b='cwCommCPUUsageSystem'
_a='cwCommCPUUsageNice'
_Z='cwCommCPUUsageUser'
_Y='cwCommCPUMonitoringStatus'
_X='cwCommCPUUsage'
_W='cwCommCPUName'
_V='cwCommCPUTotalNumber'
_U='cwCommCPUUsageWindow'
_T='cwCommCPUTotalUsage'
_S='cwCommSystemObjectID'
_R='cwCommSystemVersion'
_Q='cwCommDiskUsageIndex'
_P='not-accessible'
_O='cwCommCPUIndex'
_N='Unsigned32'
_M='SnmpAdminString'
_L='cwCommNotificationSeqNum'
_K='cwCommNotificationResValue'
_J='cwCommNotificationResName'
_I='cwCommNotificationHostAddress'
_H='cwCommNotificationHostAddressType'
_G='accessible-for-notify'
_F='percent'
_E='KHz'
_D='Gauge32'
_C='read-only'
_B='current'
_A='CISCO-WBX-MEETING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_D,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention')
ciscoWebExMeetingMIB=ModuleIdentity((1,3,6,1,4,1,9,9,809))
if mibBuilder.loadTexts:ciscoWebExMeetingMIB.setRevisions(('2013-05-29 00:00',))
class CiscoWebExCommSysResource(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('cpu',0),('memory',1),('swap',2),('fileDescriptor',3),('disk',4)))
class CiscoWebExCommSysResMonitoringStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('closed',0),('open',1)))
_CiscoWebExMeetingMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWebExMeetingMIBNotifs=_CiscoWebExMeetingMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,809,0))
_CiscoWebExMeetingMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWebExMeetingMIBObjects=_CiscoWebExMeetingMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,809,1))
_CiscoWebExCommInfo_ObjectIdentity=ObjectIdentity
ciscoWebExCommInfo=_CiscoWebExCommInfo_ObjectIdentity((1,3,6,1,4,1,9,9,809,1,1))
class _CwCommSystemVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CwCommSystemVersion_Type.__name__=_M
_CwCommSystemVersion_Object=MibScalar
cwCommSystemVersion=_CwCommSystemVersion_Object((1,3,6,1,4,1,9,9,809,1,1,1),_CwCommSystemVersion_Type())
cwCommSystemVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommSystemVersion.setStatus(_B)
_CwCommSystemObjectID_Type=AutonomousType
_CwCommSystemObjectID_Object=MibScalar
cwCommSystemObjectID=_CwCommSystemObjectID_Object((1,3,6,1,4,1,9,9,809,1,1,2),_CwCommSystemObjectID_Type())
cwCommSystemObjectID.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommSystemObjectID.setStatus(_B)
_CiscoWebExCommSystemResource_ObjectIdentity=ObjectIdentity
ciscoWebExCommSystemResource=_CiscoWebExCommSystemResource_ObjectIdentity((1,3,6,1,4,1,9,9,809,1,2))
_CwCommCPUUsageObject_ObjectIdentity=ObjectIdentity
cwCommCPUUsageObject=_CwCommCPUUsageObject_ObjectIdentity((1,3,6,1,4,1,9,9,809,1,2,1))
if mibBuilder.loadTexts:cwCommCPUUsageObject.setStatus(_B)
class _CwCommCPUTotalUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CwCommCPUTotalUsage_Type.__name__=_D
_CwCommCPUTotalUsage_Object=MibScalar
cwCommCPUTotalUsage=_CwCommCPUTotalUsage_Object((1,3,6,1,4,1,9,9,809,1,2,1,1),_CwCommCPUTotalUsage_Type())
cwCommCPUTotalUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUTotalUsage.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUTotalUsage.setUnits(_F)
class _CwCommCPUUsageWindow_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CwCommCPUUsageWindow_Type.__name__=_D
_CwCommCPUUsageWindow_Object=MibScalar
cwCommCPUUsageWindow=_CwCommCPUUsageWindow_Object((1,3,6,1,4,1,9,9,809,1,2,1,2),_CwCommCPUUsageWindow_Type())
cwCommCPUUsageWindow.setMaxAccess('read-write')
if mibBuilder.loadTexts:cwCommCPUUsageWindow.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageWindow.setUnits('Minute')
class _CwCommCPUTotalNumber_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CwCommCPUTotalNumber_Type.__name__=_D
_CwCommCPUTotalNumber_Object=MibScalar
cwCommCPUTotalNumber=_CwCommCPUTotalNumber_Object((1,3,6,1,4,1,9,9,809,1,2,1,3),_CwCommCPUTotalNumber_Type())
cwCommCPUTotalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUTotalNumber.setStatus(_B)
_CwCommCPUUsageTable_Object=MibTable
cwCommCPUUsageTable=_CwCommCPUUsageTable_Object((1,3,6,1,4,1,9,9,809,1,2,1,4))
if mibBuilder.loadTexts:cwCommCPUUsageTable.setStatus(_B)
_CwCommCPUUsageEntry_Object=MibTableRow
cwCommCPUUsageEntry=_CwCommCPUUsageEntry_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1))
cwCommCPUUsageEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:cwCommCPUUsageEntry.setStatus(_B)
class _CwCommCPUIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CwCommCPUIndex_Type.__name__=_N
_CwCommCPUIndex_Object=MibTableColumn
cwCommCPUIndex=_CwCommCPUIndex_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,1),_CwCommCPUIndex_Type())
cwCommCPUIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:cwCommCPUIndex.setStatus(_B)
class _CwCommCPUName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CwCommCPUName_Type.__name__=_M
_CwCommCPUName_Object=MibTableColumn
cwCommCPUName=_CwCommCPUName_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,2),_CwCommCPUName_Type())
cwCommCPUName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUName.setStatus(_B)
class _CwCommCPUUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CwCommCPUUsage_Type.__name__=_D
_CwCommCPUUsage_Object=MibTableColumn
cwCommCPUUsage=_CwCommCPUUsage_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,3),_CwCommCPUUsage_Type())
cwCommCPUUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsage.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsage.setUnits(_F)
class _CwCommCPUUsageUser_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageUser_Type.__name__=_D
_CwCommCPUUsageUser_Object=MibTableColumn
cwCommCPUUsageUser=_CwCommCPUUsageUser_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,4),_CwCommCPUUsageUser_Type())
cwCommCPUUsageUser.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageUser.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageUser.setUnits(_E)
class _CwCommCPUUsageNice_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageNice_Type.__name__=_D
_CwCommCPUUsageNice_Object=MibTableColumn
cwCommCPUUsageNice=_CwCommCPUUsageNice_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,5),_CwCommCPUUsageNice_Type())
cwCommCPUUsageNice.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageNice.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageNice.setUnits(_E)
class _CwCommCPUUsageSystem_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageSystem_Type.__name__=_D
_CwCommCPUUsageSystem_Object=MibTableColumn
cwCommCPUUsageSystem=_CwCommCPUUsageSystem_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,6),_CwCommCPUUsageSystem_Type())
cwCommCPUUsageSystem.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageSystem.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageSystem.setUnits(_E)
class _CwCommCPUUsageIdle_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageIdle_Type.__name__=_D
_CwCommCPUUsageIdle_Object=MibTableColumn
cwCommCPUUsageIdle=_CwCommCPUUsageIdle_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,7),_CwCommCPUUsageIdle_Type())
cwCommCPUUsageIdle.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageIdle.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageIdle.setUnits(_E)
class _CwCommCPUUsageIOWait_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageIOWait_Type.__name__=_D
_CwCommCPUUsageIOWait_Object=MibTableColumn
cwCommCPUUsageIOWait=_CwCommCPUUsageIOWait_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,8),_CwCommCPUUsageIOWait_Type())
cwCommCPUUsageIOWait.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageIOWait.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageIOWait.setUnits(_E)
class _CwCommCPUUsageIRQ_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageIRQ_Type.__name__=_D
_CwCommCPUUsageIRQ_Object=MibTableColumn
cwCommCPUUsageIRQ=_CwCommCPUUsageIRQ_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,9),_CwCommCPUUsageIRQ_Type())
cwCommCPUUsageIRQ.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageIRQ.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageIRQ.setUnits(_E)
class _CwCommCPUUsageSoftIRQ_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageSoftIRQ_Type.__name__=_D
_CwCommCPUUsageSoftIRQ_Object=MibTableColumn
cwCommCPUUsageSoftIRQ=_CwCommCPUUsageSoftIRQ_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,10),_CwCommCPUUsageSoftIRQ_Type())
cwCommCPUUsageSoftIRQ.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageSoftIRQ.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageSoftIRQ.setUnits(_E)
class _CwCommCPUUsageSteal_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageSteal_Type.__name__=_D
_CwCommCPUUsageSteal_Object=MibTableColumn
cwCommCPUUsageSteal=_CwCommCPUUsageSteal_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,11),_CwCommCPUUsageSteal_Type())
cwCommCPUUsageSteal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageSteal.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageSteal.setUnits(_E)
class _CwCommCPUUsageCapacitySubTotal_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUUsageCapacitySubTotal_Type.__name__=_D
_CwCommCPUUsageCapacitySubTotal_Object=MibTableColumn
cwCommCPUUsageCapacitySubTotal=_CwCommCPUUsageCapacitySubTotal_Object((1,3,6,1,4,1,9,9,809,1,2,1,4,1,12),_CwCommCPUUsageCapacitySubTotal_Type())
cwCommCPUUsageCapacitySubTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUUsageCapacitySubTotal.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUUsageCapacitySubTotal.setUnits(_E)
_CwCommCPUMonitoringStatus_Type=CiscoWebExCommSysResMonitoringStatus
_CwCommCPUMonitoringStatus_Object=MibScalar
cwCommCPUMonitoringStatus=_CwCommCPUMonitoringStatus_Object((1,3,6,1,4,1,9,9,809,1,2,1,5),_CwCommCPUMonitoringStatus_Type())
cwCommCPUMonitoringStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUMonitoringStatus.setStatus(_B)
class _CwCommCPUCapacityTotal_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommCPUCapacityTotal_Type.__name__=_D
_CwCommCPUCapacityTotal_Object=MibScalar
cwCommCPUCapacityTotal=_CwCommCPUCapacityTotal_Object((1,3,6,1,4,1,9,9,809,1,2,1,6),_CwCommCPUCapacityTotal_Type())
cwCommCPUCapacityTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommCPUCapacityTotal.setStatus(_B)
if mibBuilder.loadTexts:cwCommCPUCapacityTotal.setUnits(_E)
_CwCommMEMUsageObject_ObjectIdentity=ObjectIdentity
cwCommMEMUsageObject=_CwCommMEMUsageObject_ObjectIdentity((1,3,6,1,4,1,9,9,809,1,2,2))
if mibBuilder.loadTexts:cwCommMEMUsageObject.setStatus(_B)
class _CwCommMEMUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CwCommMEMUsage_Type.__name__=_D
_CwCommMEMUsage_Object=MibScalar
cwCommMEMUsage=_CwCommMEMUsage_Object((1,3,6,1,4,1,9,9,809,1,2,2,1),_CwCommMEMUsage_Type())
cwCommMEMUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommMEMUsage.setStatus(_B)
if mibBuilder.loadTexts:cwCommMEMUsage.setUnits(_F)
_CwCommMEMMonitoringStatus_Type=CiscoWebExCommSysResMonitoringStatus
_CwCommMEMMonitoringStatus_Object=MibScalar
cwCommMEMMonitoringStatus=_CwCommMEMMonitoringStatus_Object((1,3,6,1,4,1,9,9,809,1,2,2,2),_CwCommMEMMonitoringStatus_Type())
cwCommMEMMonitoringStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommMEMMonitoringStatus.setStatus(_B)
_CwCommMEMTotal_Type=Gauge32
_CwCommMEMTotal_Object=MibScalar
cwCommMEMTotal=_CwCommMEMTotal_Object((1,3,6,1,4,1,9,9,809,1,2,2,3),_CwCommMEMTotal_Type())
cwCommMEMTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommMEMTotal.setStatus(_B)
if mibBuilder.loadTexts:cwCommMEMTotal.setUnits('MBytes')
_CwCommMEMSwapUsageObject_ObjectIdentity=ObjectIdentity
cwCommMEMSwapUsageObject=_CwCommMEMSwapUsageObject_ObjectIdentity((1,3,6,1,4,1,9,9,809,1,2,3))
if mibBuilder.loadTexts:cwCommMEMSwapUsageObject.setStatus(_B)
class _CwCommMEMSwapUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CwCommMEMSwapUsage_Type.__name__=_D
_CwCommMEMSwapUsage_Object=MibScalar
cwCommMEMSwapUsage=_CwCommMEMSwapUsage_Object((1,3,6,1,4,1,9,9,809,1,2,3,1),_CwCommMEMSwapUsage_Type())
cwCommMEMSwapUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommMEMSwapUsage.setStatus(_B)
if mibBuilder.loadTexts:cwCommMEMSwapUsage.setUnits(_F)
_CwCommMEMSwapMonitoringStatus_Type=CiscoWebExCommSysResMonitoringStatus
_CwCommMEMSwapMonitoringStatus_Object=MibScalar
cwCommMEMSwapMonitoringStatus=_CwCommMEMSwapMonitoringStatus_Object((1,3,6,1,4,1,9,9,809,1,2,3,2),_CwCommMEMSwapMonitoringStatus_Type())
cwCommMEMSwapMonitoringStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommMEMSwapMonitoringStatus.setStatus(_B)
_CwCommSysResourceNotificationObject_ObjectIdentity=ObjectIdentity
cwCommSysResourceNotificationObject=_CwCommSysResourceNotificationObject_ObjectIdentity((1,3,6,1,4,1,9,9,809,1,2,4))
if mibBuilder.loadTexts:cwCommSysResourceNotificationObject.setStatus(_B)
_CwCommNotificationHostAddressType_Type=InetAddressType
_CwCommNotificationHostAddressType_Object=MibScalar
cwCommNotificationHostAddressType=_CwCommNotificationHostAddressType_Object((1,3,6,1,4,1,9,9,809,1,2,4,1),_CwCommNotificationHostAddressType_Type())
cwCommNotificationHostAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:cwCommNotificationHostAddressType.setStatus(_B)
_CwCommNotificationHostAddress_Type=InetAddress
_CwCommNotificationHostAddress_Object=MibScalar
cwCommNotificationHostAddress=_CwCommNotificationHostAddress_Object((1,3,6,1,4,1,9,9,809,1,2,4,2),_CwCommNotificationHostAddress_Type())
cwCommNotificationHostAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:cwCommNotificationHostAddress.setStatus(_B)
_CwCommNotificationResName_Type=CiscoWebExCommSysResource
_CwCommNotificationResName_Object=MibScalar
cwCommNotificationResName=_CwCommNotificationResName_Object((1,3,6,1,4,1,9,9,809,1,2,4,3),_CwCommNotificationResName_Type())
cwCommNotificationResName.setMaxAccess(_G)
if mibBuilder.loadTexts:cwCommNotificationResName.setStatus(_B)
_CwCommNotificationResValue_Type=Unsigned32
_CwCommNotificationResValue_Object=MibScalar
cwCommNotificationResValue=_CwCommNotificationResValue_Object((1,3,6,1,4,1,9,9,809,1,2,4,4),_CwCommNotificationResValue_Type())
cwCommNotificationResValue.setMaxAccess(_G)
if mibBuilder.loadTexts:cwCommNotificationResValue.setStatus(_B)
_CwCommNotificationSeqNum_Type=Counter32
_CwCommNotificationSeqNum_Object=MibScalar
cwCommNotificationSeqNum=_CwCommNotificationSeqNum_Object((1,3,6,1,4,1,9,9,809,1,2,4,5),_CwCommNotificationSeqNum_Type())
cwCommNotificationSeqNum.setMaxAccess(_G)
if mibBuilder.loadTexts:cwCommNotificationSeqNum.setStatus(_B)
_CwCommDiskUsageObject_ObjectIdentity=ObjectIdentity
cwCommDiskUsageObject=_CwCommDiskUsageObject_ObjectIdentity((1,3,6,1,4,1,9,9,809,1,2,5))
if mibBuilder.loadTexts:cwCommDiskUsageObject.setStatus(_B)
class _CwCommDiskUsageCount_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwCommDiskUsageCount_Type.__name__=_D
_CwCommDiskUsageCount_Object=MibScalar
cwCommDiskUsageCount=_CwCommDiskUsageCount_Object((1,3,6,1,4,1,9,9,809,1,2,5,1),_CwCommDiskUsageCount_Type())
cwCommDiskUsageCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommDiskUsageCount.setStatus(_B)
_CwCommDiskUsageTable_Object=MibTable
cwCommDiskUsageTable=_CwCommDiskUsageTable_Object((1,3,6,1,4,1,9,9,809,1,2,5,2))
if mibBuilder.loadTexts:cwCommDiskUsageTable.setStatus(_B)
_CwCommDiskUsageEntry_Object=MibTableRow
cwCommDiskUsageEntry=_CwCommDiskUsageEntry_Object((1,3,6,1,4,1,9,9,809,1,2,5,2,1))
cwCommDiskUsageEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:cwCommDiskUsageEntry.setStatus(_B)
class _CwCommDiskUsageIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CwCommDiskUsageIndex_Type.__name__=_N
_CwCommDiskUsageIndex_Object=MibTableColumn
cwCommDiskUsageIndex=_CwCommDiskUsageIndex_Object((1,3,6,1,4,1,9,9,809,1,2,5,2,1,1),_CwCommDiskUsageIndex_Type())
cwCommDiskUsageIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:cwCommDiskUsageIndex.setStatus(_B)
class _CwCommDiskPartitionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CwCommDiskPartitionName_Type.__name__=_M
_CwCommDiskPartitionName_Object=MibTableColumn
cwCommDiskPartitionName=_CwCommDiskPartitionName_Object((1,3,6,1,4,1,9,9,809,1,2,5,2,1,2),_CwCommDiskPartitionName_Type())
cwCommDiskPartitionName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommDiskPartitionName.setStatus(_B)
class _CwCommDiskUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CwCommDiskUsage_Type.__name__=_D
_CwCommDiskUsage_Object=MibTableColumn
cwCommDiskUsage=_CwCommDiskUsage_Object((1,3,6,1,4,1,9,9,809,1,2,5,2,1,3),_CwCommDiskUsage_Type())
cwCommDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommDiskUsage.setStatus(_B)
if mibBuilder.loadTexts:cwCommDiskUsage.setUnits(_F)
class _CwCommDiskTotal_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwCommDiskTotal_Type.__name__=_D
_CwCommDiskTotal_Object=MibTableColumn
cwCommDiskTotal=_CwCommDiskTotal_Object((1,3,6,1,4,1,9,9,809,1,2,5,2,1,4),_CwCommDiskTotal_Type())
cwCommDiskTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommDiskTotal.setStatus(_B)
if mibBuilder.loadTexts:cwCommDiskTotal.setUnits('KB')
_CwCommDiskMonitoringStatus_Type=CiscoWebExCommSysResMonitoringStatus
_CwCommDiskMonitoringStatus_Object=MibScalar
cwCommDiskMonitoringStatus=_CwCommDiskMonitoringStatus_Object((1,3,6,1,4,1,9,9,809,1,2,5,3),_CwCommDiskMonitoringStatus_Type())
cwCommDiskMonitoringStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwCommDiskMonitoringStatus.setStatus(_B)
_CiscoWebExMeetingMIBConform_ObjectIdentity=ObjectIdentity
ciscoWebExMeetingMIBConform=_CiscoWebExMeetingMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,809,2))
_CwCommMIBCompliances_ObjectIdentity=ObjectIdentity
cwCommMIBCompliances=_CwCommMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,809,2,1))
_CwCommMIBGroups_ObjectIdentity=ObjectIdentity
cwCommMIBGroups=_CwCommMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,809,2,2))
ciscoWebExCommInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,809,2,2,1))
ciscoWebExCommInfoGroup.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoWebExCommInfoGroup.setStatus(_B)
ciscoWebExCommSystemResourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,809,2,2,2))
ciscoWebExCommSystemResourceGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ciscoWebExCommSystemResourceGroup.setStatus(_B)
cwCommSystemResourceUsageNormalEvent=NotificationType((1,3,6,1,4,1,9,9,809,0,1))
cwCommSystemResourceUsageNormalEvent.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cwCommSystemResourceUsageNormalEvent.setStatus(_B)
cwCommSystemResourceUsageMinorEvent=NotificationType((1,3,6,1,4,1,9,9,809,0,2))
cwCommSystemResourceUsageMinorEvent.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cwCommSystemResourceUsageMinorEvent.setStatus(_B)
cwCommSystemResourceUsageMajorEvent=NotificationType((1,3,6,1,4,1,9,9,809,0,3))
cwCommSystemResourceUsageMajorEvent.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cwCommSystemResourceUsageMajorEvent.setStatus(_B)
ciscoWebExMeetingMIBNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,809,2,2,3))
ciscoWebExMeetingMIBNotifsGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:ciscoWebExMeetingMIBNotifsGroup.setStatus(_B)
cwCommMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,809,2,1,1))
cwCommMIBCompliance.setObjects(*((_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:cwCommMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoWebExCommSysResource':CiscoWebExCommSysResource,'CiscoWebExCommSysResMonitoringStatus':CiscoWebExCommSysResMonitoringStatus,'ciscoWebExMeetingMIB':ciscoWebExMeetingMIB,'ciscoWebExMeetingMIBNotifs':ciscoWebExMeetingMIBNotifs,_t:cwCommSystemResourceUsageNormalEvent,_u:cwCommSystemResourceUsageMinorEvent,_v:cwCommSystemResourceUsageMajorEvent,'ciscoWebExMeetingMIBObjects':ciscoWebExMeetingMIBObjects,'ciscoWebExCommInfo':ciscoWebExCommInfo,_R:cwCommSystemVersion,_S:cwCommSystemObjectID,'ciscoWebExCommSystemResource':ciscoWebExCommSystemResource,'cwCommCPUUsageObject':cwCommCPUUsageObject,_T:cwCommCPUTotalUsage,_U:cwCommCPUUsageWindow,_V:cwCommCPUTotalNumber,'cwCommCPUUsageTable':cwCommCPUUsageTable,'cwCommCPUUsageEntry':cwCommCPUUsageEntry,_O:cwCommCPUIndex,_W:cwCommCPUName,_X:cwCommCPUUsage,_Z:cwCommCPUUsageUser,_a:cwCommCPUUsageNice,_b:cwCommCPUUsageSystem,_c:cwCommCPUUsageIdle,_d:cwCommCPUUsageIOWait,_e:cwCommCPUUsageIRQ,_f:cwCommCPUUsageSoftIRQ,_g:cwCommCPUUsageSteal,_h:cwCommCPUUsageCapacitySubTotal,_Y:cwCommCPUMonitoringStatus,_i:cwCommCPUCapacityTotal,'cwCommMEMUsageObject':cwCommMEMUsageObject,_j:cwCommMEMUsage,_k:cwCommMEMMonitoringStatus,_n:cwCommMEMTotal,'cwCommMEMSwapUsageObject':cwCommMEMSwapUsageObject,_l:cwCommMEMSwapUsage,_m:cwCommMEMSwapMonitoringStatus,'cwCommSysResourceNotificationObject':cwCommSysResourceNotificationObject,_H:cwCommNotificationHostAddressType,_I:cwCommNotificationHostAddress,_J:cwCommNotificationResName,_K:cwCommNotificationResValue,_L:cwCommNotificationSeqNum,'cwCommDiskUsageObject':cwCommDiskUsageObject,_o:cwCommDiskUsageCount,'cwCommDiskUsageTable':cwCommDiskUsageTable,'cwCommDiskUsageEntry':cwCommDiskUsageEntry,_Q:cwCommDiskUsageIndex,_p:cwCommDiskPartitionName,_q:cwCommDiskUsage,_r:cwCommDiskTotal,_s:cwCommDiskMonitoringStatus,'ciscoWebExMeetingMIBConform':ciscoWebExMeetingMIBConform,'cwCommMIBCompliances':cwCommMIBCompliances,'cwCommMIBCompliance':cwCommMIBCompliance,'cwCommMIBGroups':cwCommMIBGroups,_w:ciscoWebExCommInfoGroup,_x:ciscoWebExCommSystemResourceGroup,_y:ciscoWebExMeetingMIBNotifsGroup})