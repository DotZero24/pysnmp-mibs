_M='rcPacketAllStatisticsProtocolIndex'
_L='rcPacketVlanStatisticsProtocolIndex'
_K='rcPacketVlanStatisticsVlanIndex'
_J='rcPacketPortStatisticsProtocolIndex'
_I='rcPacketPortStatisticsPortIndex'
_H='rcCpuCachePacketUploadServerIndex'
_G='rcCpuCachePacketPortIndex'
_F='not-accessible'
_E='SWITCH-CCP-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
EnableVar,ObjName,PortList=mibBuilder.importSymbols('SWITCH-TC','EnableVar','ObjName','PortList')
rcCcp=ModuleIdentity((1,3,6,1,4,1,8886,6,1,55))
if mibBuilder.loadTexts:rcCcp.setRevisions(('2010-11-08 00:00',))
_RcCpuCachePacket_ObjectIdentity=ObjectIdentity
rcCpuCachePacket=_RcCpuCachePacket_ObjectIdentity((1,3,6,1,4,1,8886,6,1,55,1))
_RcCpuCachePacketEnable_Type=EnableVar
_RcCpuCachePacketEnable_Object=MibScalar
rcCpuCachePacketEnable=_RcCpuCachePacketEnable_Object((1,3,6,1,4,1,8886,6,1,55,1,1),_RcCpuCachePacketEnable_Type())
rcCpuCachePacketEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketEnable.setStatus(_A)
_RcCpuCachePacketPortList_Type=PortList
_RcCpuCachePacketPortList_Object=MibScalar
rcCpuCachePacketPortList=_RcCpuCachePacketPortList_Object((1,3,6,1,4,1,8886,6,1,55,1,2),_RcCpuCachePacketPortList_Type())
rcCpuCachePacketPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketPortList.setStatus(_A)
class _RcCpuCachePacketLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('header',1),('all',2)))
_RcCpuCachePacketLen_Type.__name__=_D
_RcCpuCachePacketLen_Object=MibScalar
rcCpuCachePacketLen=_RcCpuCachePacketLen_Object((1,3,6,1,4,1,8886,6,1,55,1,3),_RcCpuCachePacketLen_Type())
rcCpuCachePacketLen.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketLen.setStatus(_A)
_RcCpuCachePacketBufferSize_Type=Integer32
_RcCpuCachePacketBufferSize_Object=MibScalar
rcCpuCachePacketBufferSize=_RcCpuCachePacketBufferSize_Object((1,3,6,1,4,1,8886,6,1,55,1,4),_RcCpuCachePacketBufferSize_Type())
rcCpuCachePacketBufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketBufferSize.setStatus(_A)
_RcCpuCachePacketManualUpload_Type=EnableVar
_RcCpuCachePacketManualUpload_Object=MibScalar
rcCpuCachePacketManualUpload=_RcCpuCachePacketManualUpload_Object((1,3,6,1,4,1,8886,6,1,55,1,5),_RcCpuCachePacketManualUpload_Type())
rcCpuCachePacketManualUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketManualUpload.setStatus(_A)
_RcCpuCachePacketAutoUpload_Type=EnableVar
_RcCpuCachePacketAutoUpload_Object=MibScalar
rcCpuCachePacketAutoUpload=_RcCpuCachePacketAutoUpload_Object((1,3,6,1,4,1,8886,6,1,55,1,6),_RcCpuCachePacketAutoUpload_Type())
rcCpuCachePacketAutoUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketAutoUpload.setStatus(_A)
_RcCpuCachePacketOverride_Type=EnableVar
_RcCpuCachePacketOverride_Object=MibScalar
rcCpuCachePacketOverride=_RcCpuCachePacketOverride_Object((1,3,6,1,4,1,8886,6,1,55,1,7),_RcCpuCachePacketOverride_Type())
rcCpuCachePacketOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketOverride.setStatus(_A)
class _RcCpuCachePacketAutoUploadTimes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCpuCachePacketAutoUploadTimes_Type.__name__=_D
_RcCpuCachePacketAutoUploadTimes_Object=MibScalar
rcCpuCachePacketAutoUploadTimes=_RcCpuCachePacketAutoUploadTimes_Object((1,3,6,1,4,1,8886,6,1,55,1,8),_RcCpuCachePacketAutoUploadTimes_Type())
rcCpuCachePacketAutoUploadTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketAutoUploadTimes.setStatus(_A)
_RcCpuCachePacketClear_Type=EnableVar
_RcCpuCachePacketClear_Object=MibScalar
rcCpuCachePacketClear=_RcCpuCachePacketClear_Object((1,3,6,1,4,1,8886,6,1,55,1,9),_RcCpuCachePacketClear_Type())
rcCpuCachePacketClear.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketClear.setStatus(_A)
_RcCpuCachePacketsAutoUploadCounter_Type=Integer32
_RcCpuCachePacketsAutoUploadCounter_Object=MibScalar
rcCpuCachePacketsAutoUploadCounter=_RcCpuCachePacketsAutoUploadCounter_Object((1,3,6,1,4,1,8886,6,1,55,1,10),_RcCpuCachePacketsAutoUploadCounter_Type())
rcCpuCachePacketsAutoUploadCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCpuCachePacketsAutoUploadCounter.setStatus(_A)
_RcCpuCachePacketMirrorToCpuStatus_Type=EnableVar
_RcCpuCachePacketMirrorToCpuStatus_Object=MibScalar
rcCpuCachePacketMirrorToCpuStatus=_RcCpuCachePacketMirrorToCpuStatus_Object((1,3,6,1,4,1,8886,6,1,55,1,11),_RcCpuCachePacketMirrorToCpuStatus_Type())
rcCpuCachePacketMirrorToCpuStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCpuCachePacketMirrorToCpuStatus.setStatus(_A)
class _RcCpuCachePacketBufferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('not-malloc',1),('not-full',2),('full',3)))
_RcCpuCachePacketBufferStatus_Type.__name__=_D
_RcCpuCachePacketBufferStatus_Object=MibScalar
rcCpuCachePacketBufferStatus=_RcCpuCachePacketBufferStatus_Object((1,3,6,1,4,1,8886,6,1,55,1,12),_RcCpuCachePacketBufferStatus_Type())
rcCpuCachePacketBufferStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCpuCachePacketBufferStatus.setStatus(_A)
class _RcCpuCachePacketStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('uploading',2),('collecting',3)))
_RcCpuCachePacketStatus_Type.__name__=_D
_RcCpuCachePacketStatus_Object=MibScalar
rcCpuCachePacketStatus=_RcCpuCachePacketStatus_Object((1,3,6,1,4,1,8886,6,1,55,1,13),_RcCpuCachePacketStatus_Type())
rcCpuCachePacketStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCpuCachePacketStatus.setStatus(_A)
_RcCpuCachePacketCount_Type=Integer32
_RcCpuCachePacketCount_Object=MibScalar
rcCpuCachePacketCount=_RcCpuCachePacketCount_Object((1,3,6,1,4,1,8886,6,1,55,1,14),_RcCpuCachePacketCount_Type())
rcCpuCachePacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCpuCachePacketCount.setStatus(_A)
_RcCpuCachePacketUploadedNumber_Type=Integer32
_RcCpuCachePacketUploadedNumber_Object=MibScalar
rcCpuCachePacketUploadedNumber=_RcCpuCachePacketUploadedNumber_Object((1,3,6,1,4,1,8886,6,1,55,1,15),_RcCpuCachePacketUploadedNumber_Type())
rcCpuCachePacketUploadedNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCpuCachePacketUploadedNumber.setStatus(_A)
_RcCpuCachePacketAclTable_Object=MibTable
rcCpuCachePacketAclTable=_RcCpuCachePacketAclTable_Object((1,3,6,1,4,1,8886,6,1,55,1,16))
if mibBuilder.loadTexts:rcCpuCachePacketAclTable.setStatus(_A)
_RcCpuCachePacketAclEntry_Object=MibTableRow
rcCpuCachePacketAclEntry=_RcCpuCachePacketAclEntry_Object((1,3,6,1,4,1,8886,6,1,55,1,16,1))
rcCpuCachePacketAclEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:rcCpuCachePacketAclEntry.setStatus(_A)
_RcCpuCachePacketPortIndex_Type=Integer32
_RcCpuCachePacketPortIndex_Object=MibTableColumn
rcCpuCachePacketPortIndex=_RcCpuCachePacketPortIndex_Object((1,3,6,1,4,1,8886,6,1,55,1,16,1,1),_RcCpuCachePacketPortIndex_Type())
rcCpuCachePacketPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcCpuCachePacketPortIndex.setStatus(_A)
class _RcCpuCachePacketAclType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip-access-list',1),('mac-access-list',2),('access-list-map',3)))
_RcCpuCachePacketAclType_Type.__name__=_D
_RcCpuCachePacketAclType_Object=MibTableColumn
rcCpuCachePacketAclType=_RcCpuCachePacketAclType_Object((1,3,6,1,4,1,8886,6,1,55,1,16,1,2),_RcCpuCachePacketAclType_Type())
rcCpuCachePacketAclType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketAclType.setStatus(_A)
class _RcCpuCachePacketAclNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_RcCpuCachePacketAclNo_Type.__name__=_D
_RcCpuCachePacketAclNo_Object=MibTableColumn
rcCpuCachePacketAclNo=_RcCpuCachePacketAclNo_Object((1,3,6,1,4,1,8886,6,1,55,1,16,1,3),_RcCpuCachePacketAclNo_Type())
rcCpuCachePacketAclNo.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketAclNo.setStatus(_A)
_RcCpuCachePacketAclEnable_Type=EnableVar
_RcCpuCachePacketAclEnable_Object=MibTableColumn
rcCpuCachePacketAclEnable=_RcCpuCachePacketAclEnable_Object((1,3,6,1,4,1,8886,6,1,55,1,16,1,4),_RcCpuCachePacketAclEnable_Type())
rcCpuCachePacketAclEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketAclEnable.setStatus(_A)
_RcCpuCachePacketUploadServerTable_Object=MibTable
rcCpuCachePacketUploadServerTable=_RcCpuCachePacketUploadServerTable_Object((1,3,6,1,4,1,8886,6,1,55,1,17))
if mibBuilder.loadTexts:rcCpuCachePacketUploadServerTable.setStatus(_A)
_RcCpuCachePacketUploadServerEntry_Object=MibTableRow
rcCpuCachePacketUploadServerEntry=_RcCpuCachePacketUploadServerEntry_Object((1,3,6,1,4,1,8886,6,1,55,1,17,1))
rcCpuCachePacketUploadServerEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:rcCpuCachePacketUploadServerEntry.setStatus(_A)
_RcCpuCachePacketUploadServerIndex_Type=Integer32
_RcCpuCachePacketUploadServerIndex_Object=MibTableColumn
rcCpuCachePacketUploadServerIndex=_RcCpuCachePacketUploadServerIndex_Object((1,3,6,1,4,1,8886,6,1,55,1,17,1,1),_RcCpuCachePacketUploadServerIndex_Type())
rcCpuCachePacketUploadServerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcCpuCachePacketUploadServerIndex.setStatus(_A)
class _RcCpuCachePacketUploadServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tftp',1),('ftp',2)))
_RcCpuCachePacketUploadServerMode_Type.__name__=_D
_RcCpuCachePacketUploadServerMode_Object=MibTableColumn
rcCpuCachePacketUploadServerMode=_RcCpuCachePacketUploadServerMode_Object((1,3,6,1,4,1,8886,6,1,55,1,17,1,2),_RcCpuCachePacketUploadServerMode_Type())
rcCpuCachePacketUploadServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketUploadServerMode.setStatus(_A)
_RcCpuCachePacketUploadServerAddress_Type=IpAddress
_RcCpuCachePacketUploadServerAddress_Object=MibTableColumn
rcCpuCachePacketUploadServerAddress=_RcCpuCachePacketUploadServerAddress_Object((1,3,6,1,4,1,8886,6,1,55,1,17,1,3),_RcCpuCachePacketUploadServerAddress_Type())
rcCpuCachePacketUploadServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketUploadServerAddress.setStatus(_A)
_RcCpuCachePacketUploadServerUserName_Type=ObjName
_RcCpuCachePacketUploadServerUserName_Object=MibTableColumn
rcCpuCachePacketUploadServerUserName=_RcCpuCachePacketUploadServerUserName_Object((1,3,6,1,4,1,8886,6,1,55,1,17,1,4),_RcCpuCachePacketUploadServerUserName_Type())
rcCpuCachePacketUploadServerUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketUploadServerUserName.setStatus(_A)
_RcCpuCachePacketUploadServerPassword_Type=ObjName
_RcCpuCachePacketUploadServerPassword_Object=MibTableColumn
rcCpuCachePacketUploadServerPassword=_RcCpuCachePacketUploadServerPassword_Object((1,3,6,1,4,1,8886,6,1,55,1,17,1,5),_RcCpuCachePacketUploadServerPassword_Type())
rcCpuCachePacketUploadServerPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketUploadServerPassword.setStatus(_A)
_RcCpuCachePacketUploadServerEnable_Type=EnableVar
_RcCpuCachePacketUploadServerEnable_Object=MibTableColumn
rcCpuCachePacketUploadServerEnable=_RcCpuCachePacketUploadServerEnable_Object((1,3,6,1,4,1,8886,6,1,55,1,17,1,6),_RcCpuCachePacketUploadServerEnable_Type())
rcCpuCachePacketUploadServerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCpuCachePacketUploadServerEnable.setStatus(_A)
_RcCpuCachePacketPortStatisticsTable_Object=MibTable
rcCpuCachePacketPortStatisticsTable=_RcCpuCachePacketPortStatisticsTable_Object((1,3,6,1,4,1,8886,6,1,55,1,18))
if mibBuilder.loadTexts:rcCpuCachePacketPortStatisticsTable.setStatus(_A)
_RcCpuCachePacketPortStatisticsEntry_Object=MibTableRow
rcCpuCachePacketPortStatisticsEntry=_RcCpuCachePacketPortStatisticsEntry_Object((1,3,6,1,4,1,8886,6,1,55,1,18,1))
rcCpuCachePacketPortStatisticsEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:rcCpuCachePacketPortStatisticsEntry.setStatus(_A)
_RcPacketPortStatisticsPortIndex_Type=Integer32
_RcPacketPortStatisticsPortIndex_Object=MibTableColumn
rcPacketPortStatisticsPortIndex=_RcPacketPortStatisticsPortIndex_Object((1,3,6,1,4,1,8886,6,1,55,1,18,1,1),_RcPacketPortStatisticsPortIndex_Type())
rcPacketPortStatisticsPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPacketPortStatisticsPortIndex.setStatus(_A)
_RcPacketPortStatisticsProtocolIndex_Type=Integer32
_RcPacketPortStatisticsProtocolIndex_Object=MibTableColumn
rcPacketPortStatisticsProtocolIndex=_RcPacketPortStatisticsProtocolIndex_Object((1,3,6,1,4,1,8886,6,1,55,1,18,1,2),_RcPacketPortStatisticsProtocolIndex_Type())
rcPacketPortStatisticsProtocolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPacketPortStatisticsProtocolIndex.setStatus(_A)
_RcPacketPortStatisticsPktCount_Type=Integer32
_RcPacketPortStatisticsPktCount_Object=MibTableColumn
rcPacketPortStatisticsPktCount=_RcPacketPortStatisticsPktCount_Object((1,3,6,1,4,1,8886,6,1,55,1,18,1,3),_RcPacketPortStatisticsPktCount_Type())
rcPacketPortStatisticsPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPacketPortStatisticsPktCount.setStatus(_A)
_RcPacketPortStatisticsAllPktRatio_Type=Integer32
_RcPacketPortStatisticsAllPktRatio_Object=MibTableColumn
rcPacketPortStatisticsAllPktRatio=_RcPacketPortStatisticsAllPktRatio_Object((1,3,6,1,4,1,8886,6,1,55,1,18,1,4),_RcPacketPortStatisticsAllPktRatio_Type())
rcPacketPortStatisticsAllPktRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPacketPortStatisticsAllPktRatio.setStatus(_A)
_RcPacketPortStatisticsPortPktRatio_Type=Integer32
_RcPacketPortStatisticsPortPktRatio_Object=MibTableColumn
rcPacketPortStatisticsPortPktRatio=_RcPacketPortStatisticsPortPktRatio_Object((1,3,6,1,4,1,8886,6,1,55,1,18,1,5),_RcPacketPortStatisticsPortPktRatio_Type())
rcPacketPortStatisticsPortPktRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPacketPortStatisticsPortPktRatio.setStatus(_A)
_RcCpuCachePacketVlanStatisticsTable_Object=MibTable
rcCpuCachePacketVlanStatisticsTable=_RcCpuCachePacketVlanStatisticsTable_Object((1,3,6,1,4,1,8886,6,1,55,1,19))
if mibBuilder.loadTexts:rcCpuCachePacketVlanStatisticsTable.setStatus(_A)
_RcCpuCachePacketVlanStatisticsEntry_Object=MibTableRow
rcCpuCachePacketVlanStatisticsEntry=_RcCpuCachePacketVlanStatisticsEntry_Object((1,3,6,1,4,1,8886,6,1,55,1,19,1))
rcCpuCachePacketVlanStatisticsEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:rcCpuCachePacketVlanStatisticsEntry.setStatus(_A)
_RcPacketVlanStatisticsVlanIndex_Type=Integer32
_RcPacketVlanStatisticsVlanIndex_Object=MibTableColumn
rcPacketVlanStatisticsVlanIndex=_RcPacketVlanStatisticsVlanIndex_Object((1,3,6,1,4,1,8886,6,1,55,1,19,1,1),_RcPacketVlanStatisticsVlanIndex_Type())
rcPacketVlanStatisticsVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPacketVlanStatisticsVlanIndex.setStatus(_A)
_RcPacketVlanStatisticsProtocolIndex_Type=Integer32
_RcPacketVlanStatisticsProtocolIndex_Object=MibTableColumn
rcPacketVlanStatisticsProtocolIndex=_RcPacketVlanStatisticsProtocolIndex_Object((1,3,6,1,4,1,8886,6,1,55,1,19,1,2),_RcPacketVlanStatisticsProtocolIndex_Type())
rcPacketVlanStatisticsProtocolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPacketVlanStatisticsProtocolIndex.setStatus(_A)
_RcPacketVlanStatisticsPktCount_Type=Integer32
_RcPacketVlanStatisticsPktCount_Object=MibTableColumn
rcPacketVlanStatisticsPktCount=_RcPacketVlanStatisticsPktCount_Object((1,3,6,1,4,1,8886,6,1,55,1,19,1,3),_RcPacketVlanStatisticsPktCount_Type())
rcPacketVlanStatisticsPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPacketVlanStatisticsPktCount.setStatus(_A)
_RcPacketVlanStatisticsAllPktRatio_Type=Integer32
_RcPacketVlanStatisticsAllPktRatio_Object=MibTableColumn
rcPacketVlanStatisticsAllPktRatio=_RcPacketVlanStatisticsAllPktRatio_Object((1,3,6,1,4,1,8886,6,1,55,1,19,1,4),_RcPacketVlanStatisticsAllPktRatio_Type())
rcPacketVlanStatisticsAllPktRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPacketVlanStatisticsAllPktRatio.setStatus(_A)
_RcPacketVlanStatisticsVlanPktRatio_Type=Integer32
_RcPacketVlanStatisticsVlanPktRatio_Object=MibTableColumn
rcPacketVlanStatisticsVlanPktRatio=_RcPacketVlanStatisticsVlanPktRatio_Object((1,3,6,1,4,1,8886,6,1,55,1,19,1,5),_RcPacketVlanStatisticsVlanPktRatio_Type())
rcPacketVlanStatisticsVlanPktRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPacketVlanStatisticsVlanPktRatio.setStatus(_A)
_RcCpuCachePacketAllStatisticsTable_Object=MibTable
rcCpuCachePacketAllStatisticsTable=_RcCpuCachePacketAllStatisticsTable_Object((1,3,6,1,4,1,8886,6,1,55,1,20))
if mibBuilder.loadTexts:rcCpuCachePacketAllStatisticsTable.setStatus(_A)
_RcCpuCachePacketAllStatisticsEntry_Object=MibTableRow
rcCpuCachePacketAllStatisticsEntry=_RcCpuCachePacketAllStatisticsEntry_Object((1,3,6,1,4,1,8886,6,1,55,1,20,1))
rcCpuCachePacketAllStatisticsEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:rcCpuCachePacketAllStatisticsEntry.setStatus(_A)
_RcPacketAllStatisticsProtocolIndex_Type=Integer32
_RcPacketAllStatisticsProtocolIndex_Object=MibTableColumn
rcPacketAllStatisticsProtocolIndex=_RcPacketAllStatisticsProtocolIndex_Object((1,3,6,1,4,1,8886,6,1,55,1,20,1,1),_RcPacketAllStatisticsProtocolIndex_Type())
rcPacketAllStatisticsProtocolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPacketAllStatisticsProtocolIndex.setStatus(_A)
_RcPacketAllStatisticsPktCount_Type=Integer32
_RcPacketAllStatisticsPktCount_Object=MibTableColumn
rcPacketAllStatisticsPktCount=_RcPacketAllStatisticsPktCount_Object((1,3,6,1,4,1,8886,6,1,55,1,20,1,2),_RcPacketAllStatisticsPktCount_Type())
rcPacketAllStatisticsPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPacketAllStatisticsPktCount.setStatus(_A)
_RcPacketAllStatisticsAllPktRatio_Type=Integer32
_RcPacketAllStatisticsAllPktRatio_Object=MibTableColumn
rcPacketAllStatisticsAllPktRatio=_RcPacketAllStatisticsAllPktRatio_Object((1,3,6,1,4,1,8886,6,1,55,1,20,1,3),_RcPacketAllStatisticsAllPktRatio_Type())
rcPacketAllStatisticsAllPktRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPacketAllStatisticsAllPktRatio.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rcCcp':rcCcp,'rcCpuCachePacket':rcCpuCachePacket,'rcCpuCachePacketEnable':rcCpuCachePacketEnable,'rcCpuCachePacketPortList':rcCpuCachePacketPortList,'rcCpuCachePacketLen':rcCpuCachePacketLen,'rcCpuCachePacketBufferSize':rcCpuCachePacketBufferSize,'rcCpuCachePacketManualUpload':rcCpuCachePacketManualUpload,'rcCpuCachePacketAutoUpload':rcCpuCachePacketAutoUpload,'rcCpuCachePacketOverride':rcCpuCachePacketOverride,'rcCpuCachePacketAutoUploadTimes':rcCpuCachePacketAutoUploadTimes,'rcCpuCachePacketClear':rcCpuCachePacketClear,'rcCpuCachePacketsAutoUploadCounter':rcCpuCachePacketsAutoUploadCounter,'rcCpuCachePacketMirrorToCpuStatus':rcCpuCachePacketMirrorToCpuStatus,'rcCpuCachePacketBufferStatus':rcCpuCachePacketBufferStatus,'rcCpuCachePacketStatus':rcCpuCachePacketStatus,'rcCpuCachePacketCount':rcCpuCachePacketCount,'rcCpuCachePacketUploadedNumber':rcCpuCachePacketUploadedNumber,'rcCpuCachePacketAclTable':rcCpuCachePacketAclTable,'rcCpuCachePacketAclEntry':rcCpuCachePacketAclEntry,_G:rcCpuCachePacketPortIndex,'rcCpuCachePacketAclType':rcCpuCachePacketAclType,'rcCpuCachePacketAclNo':rcCpuCachePacketAclNo,'rcCpuCachePacketAclEnable':rcCpuCachePacketAclEnable,'rcCpuCachePacketUploadServerTable':rcCpuCachePacketUploadServerTable,'rcCpuCachePacketUploadServerEntry':rcCpuCachePacketUploadServerEntry,_H:rcCpuCachePacketUploadServerIndex,'rcCpuCachePacketUploadServerMode':rcCpuCachePacketUploadServerMode,'rcCpuCachePacketUploadServerAddress':rcCpuCachePacketUploadServerAddress,'rcCpuCachePacketUploadServerUserName':rcCpuCachePacketUploadServerUserName,'rcCpuCachePacketUploadServerPassword':rcCpuCachePacketUploadServerPassword,'rcCpuCachePacketUploadServerEnable':rcCpuCachePacketUploadServerEnable,'rcCpuCachePacketPortStatisticsTable':rcCpuCachePacketPortStatisticsTable,'rcCpuCachePacketPortStatisticsEntry':rcCpuCachePacketPortStatisticsEntry,_I:rcPacketPortStatisticsPortIndex,_J:rcPacketPortStatisticsProtocolIndex,'rcPacketPortStatisticsPktCount':rcPacketPortStatisticsPktCount,'rcPacketPortStatisticsAllPktRatio':rcPacketPortStatisticsAllPktRatio,'rcPacketPortStatisticsPortPktRatio':rcPacketPortStatisticsPortPktRatio,'rcCpuCachePacketVlanStatisticsTable':rcCpuCachePacketVlanStatisticsTable,'rcCpuCachePacketVlanStatisticsEntry':rcCpuCachePacketVlanStatisticsEntry,_K:rcPacketVlanStatisticsVlanIndex,_L:rcPacketVlanStatisticsProtocolIndex,'rcPacketVlanStatisticsPktCount':rcPacketVlanStatisticsPktCount,'rcPacketVlanStatisticsAllPktRatio':rcPacketVlanStatisticsAllPktRatio,'rcPacketVlanStatisticsVlanPktRatio':rcPacketVlanStatisticsVlanPktRatio,'rcCpuCachePacketAllStatisticsTable':rcCpuCachePacketAllStatisticsTable,'rcCpuCachePacketAllStatisticsEntry':rcCpuCachePacketAllStatisticsEntry,_M:rcPacketAllStatisticsProtocolIndex,'rcPacketAllStatisticsPktCount':rcPacketAllStatisticsPktCount,'rcPacketAllStatisticsAllPktRatio':rcPacketAllStatisticsAllPktRatio})