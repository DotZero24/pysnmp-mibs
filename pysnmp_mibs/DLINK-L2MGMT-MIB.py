_N='swIGMPGroupIpAddr'
_M='swIGMPVid'
_L='swIGMPInfoVid'
_K='seconds'
_J='swIGMPCtrlVid'
_I='swPortMirrorIndex'
_H='swPortTrunkIndex'
_G='DisplayString'
_F='other'
_E='DLINK-L2MGMT-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
swDlinkL2Mgmt=ModuleIdentity((1,3,6,1,4,1,171,12,2))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class PortList(TextualConvention,OctetString):status=_A
_SwPortTrunkPackage_ObjectIdentity=ObjectIdentity
swPortTrunkPackage=_SwPortTrunkPackage_ObjectIdentity((1,3,6,1,4,1,171,12,2,1))
_SwPortTrunkMaxEntries_Type=Integer32
_SwPortTrunkMaxEntries_Object=MibScalar
swPortTrunkMaxEntries=_SwPortTrunkMaxEntries_Object((1,3,6,1,4,1,171,12,2,1,1),_SwPortTrunkMaxEntries_Type())
swPortTrunkMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortTrunkMaxEntries.setStatus(_A)
_SwPortTrunkMaxPortMembers_Type=Integer32
_SwPortTrunkMaxPortMembers_Object=MibScalar
swPortTrunkMaxPortMembers=_SwPortTrunkMaxPortMembers_Object((1,3,6,1,4,1,171,12,2,1,2),_SwPortTrunkMaxPortMembers_Type())
swPortTrunkMaxPortMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortTrunkMaxPortMembers.setStatus(_A)
_SwPortTrunkTable_Object=MibTable
swPortTrunkTable=_SwPortTrunkTable_Object((1,3,6,1,4,1,171,12,2,1,3))
if mibBuilder.loadTexts:swPortTrunkTable.setStatus(_A)
_SwPortTrunkEntry_Object=MibTableRow
swPortTrunkEntry=_SwPortTrunkEntry_Object((1,3,6,1,4,1,171,12,2,1,3,1))
swPortTrunkEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:swPortTrunkEntry.setStatus(_A)
_SwPortTrunkIndex_Type=Integer32
_SwPortTrunkIndex_Object=MibTableColumn
swPortTrunkIndex=_SwPortTrunkIndex_Object((1,3,6,1,4,1,171,12,2,1,3,1,1),_SwPortTrunkIndex_Type())
swPortTrunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortTrunkIndex.setStatus(_A)
class _SwPortTrunkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwPortTrunkName_Type.__name__=_G
_SwPortTrunkName_Object=MibTableColumn
swPortTrunkName=_SwPortTrunkName_Object((1,3,6,1,4,1,171,12,2,1,3,1,2),_SwPortTrunkName_Type())
swPortTrunkName.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortTrunkName.setStatus(_A)
_SwPortTrunkMasterPort_Type=Integer32
_SwPortTrunkMasterPort_Object=MibTableColumn
swPortTrunkMasterPort=_SwPortTrunkMasterPort_Object((1,3,6,1,4,1,171,12,2,1,3,1,3),_SwPortTrunkMasterPort_Type())
swPortTrunkMasterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortTrunkMasterPort.setStatus(_A)
_SwPortTrunkPortList_Type=PortList
_SwPortTrunkPortList_Object=MibTableColumn
swPortTrunkPortList=_SwPortTrunkPortList_Object((1,3,6,1,4,1,171,12,2,1,3,1,4),_SwPortTrunkPortList_Type())
swPortTrunkPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortTrunkPortList.setStatus(_A)
_SwPortTrunkState_Type=RowStatus
_SwPortTrunkState_Object=MibTableColumn
swPortTrunkState=_SwPortTrunkState_Object((1,3,6,1,4,1,171,12,2,1,3,1,5),_SwPortTrunkState_Type())
swPortTrunkState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortTrunkState.setStatus(_A)
_SwPortMirrorPackage_ObjectIdentity=ObjectIdentity
swPortMirrorPackage=_SwPortMirrorPackage_ObjectIdentity((1,3,6,1,4,1,171,12,2,2))
_SwPortMirrorMaxEntries_Type=Integer32
_SwPortMirrorMaxEntries_Object=MibScalar
swPortMirrorMaxEntries=_SwPortMirrorMaxEntries_Object((1,3,6,1,4,1,171,12,2,2,1),_SwPortMirrorMaxEntries_Type())
swPortMirrorMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortMirrorMaxEntries.setStatus(_A)
_SwPortMirrorCtrlTable_Object=MibTable
swPortMirrorCtrlTable=_SwPortMirrorCtrlTable_Object((1,3,6,1,4,1,171,12,2,2,2))
if mibBuilder.loadTexts:swPortMirrorCtrlTable.setStatus(_A)
_SwPortMirrorCtrlEntry_Object=MibTableRow
swPortMirrorCtrlEntry=_SwPortMirrorCtrlEntry_Object((1,3,6,1,4,1,171,12,2,2,2,1))
swPortMirrorCtrlEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:swPortMirrorCtrlEntry.setStatus(_A)
_SwPortMirrorIndex_Type=Integer32
_SwPortMirrorIndex_Object=MibTableColumn
swPortMirrorIndex=_SwPortMirrorIndex_Object((1,3,6,1,4,1,171,12,2,2,2,1,1),_SwPortMirrorIndex_Type())
swPortMirrorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortMirrorIndex.setStatus(_A)
_SwPortMirrorSourcePort_Type=Integer32
_SwPortMirrorSourcePort_Object=MibTableColumn
swPortMirrorSourcePort=_SwPortMirrorSourcePort_Object((1,3,6,1,4,1,171,12,2,2,2,1,2),_SwPortMirrorSourcePort_Type())
swPortMirrorSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorSourcePort.setStatus(_A)
_SwPortMirrorTargetPort_Type=Integer32
_SwPortMirrorTargetPort_Object=MibTableColumn
swPortMirrorTargetPort=_SwPortMirrorTargetPort_Object((1,3,6,1,4,1,171,12,2,2,2,1,3),_SwPortMirrorTargetPort_Type())
swPortMirrorTargetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorTargetPort.setStatus(_A)
class _SwPortMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('ingress',2),('egress',3),('both',4)))
_SwPortMirrorDirection_Type.__name__=_D
_SwPortMirrorDirection_Object=MibTableColumn
swPortMirrorDirection=_SwPortMirrorDirection_Object((1,3,6,1,4,1,171,12,2,2,2,1,4),_SwPortMirrorDirection_Type())
swPortMirrorDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorDirection.setStatus(_A)
_SwPortMirrorState_Type=RowStatus
_SwPortMirrorState_Object=MibTableColumn
swPortMirrorState=_SwPortMirrorState_Object((1,3,6,1,4,1,171,12,2,2,2,1,5),_SwPortMirrorState_Type())
swPortMirrorState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorState.setStatus(_A)
_SwIGMPPackage_ObjectIdentity=ObjectIdentity
swIGMPPackage=_SwIGMPPackage_ObjectIdentity((1,3,6,1,4,1,171,12,2,3))
class _SwIGMPCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('disabled',2),('enabled',3)))
_SwIGMPCtrlStatus_Type.__name__=_D
_SwIGMPCtrlStatus_Object=MibScalar
swIGMPCtrlStatus=_SwIGMPCtrlStatus_Object((1,3,6,1,4,1,171,12,2,3,1),_SwIGMPCtrlStatus_Type())
swIGMPCtrlStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:swIGMPCtrlStatus.setStatus(_A)
_SwIGMPCtrlMaxEntries_Type=Integer32
_SwIGMPCtrlMaxEntries_Object=MibScalar
swIGMPCtrlMaxEntries=_SwIGMPCtrlMaxEntries_Object((1,3,6,1,4,1,171,12,2,3,2),_SwIGMPCtrlMaxEntries_Type())
swIGMPCtrlMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPCtrlMaxEntries.setStatus(_A)
_SwIGMPCtrlTable_Object=MibTable
swIGMPCtrlTable=_SwIGMPCtrlTable_Object((1,3,6,1,4,1,171,12,2,3,3))
if mibBuilder.loadTexts:swIGMPCtrlTable.setStatus(_A)
_SwIGMPCtrlEntry_Object=MibTableRow
swIGMPCtrlEntry=_SwIGMPCtrlEntry_Object((1,3,6,1,4,1,171,12,2,3,3,1))
swIGMPCtrlEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:swIGMPCtrlEntry.setStatus(_A)
_SwIGMPCtrlVid_Type=Integer32
_SwIGMPCtrlVid_Object=MibTableColumn
swIGMPCtrlVid=_SwIGMPCtrlVid_Object((1,3,6,1,4,1,171,12,2,3,3,1,1),_SwIGMPCtrlVid_Type())
swIGMPCtrlVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPCtrlVid.setStatus(_A)
class _SwIGMPQueryInterval_Type(Integer32):defaultValue=125
_SwIGMPQueryInterval_Type.__name__=_D
_SwIGMPQueryInterval_Object=MibTableColumn
swIGMPQueryInterval=_SwIGMPQueryInterval_Object((1,3,6,1,4,1,171,12,2,3,3,1,2),_SwIGMPQueryInterval_Type())
swIGMPQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:swIGMPQueryInterval.setUnits(_K)
class _SwIGMPQueryMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwIGMPQueryMaxResponseTime_Type.__name__=_D
_SwIGMPQueryMaxResponseTime_Object=MibTableColumn
swIGMPQueryMaxResponseTime=_SwIGMPQueryMaxResponseTime_Object((1,3,6,1,4,1,171,12,2,3,3,1,3),_SwIGMPQueryMaxResponseTime_Type())
swIGMPQueryMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:swIGMPQueryMaxResponseTime.setUnits(_K)
class _SwIGMPRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwIGMPRobustness_Type.__name__=_D
_SwIGMPRobustness_Object=MibTableColumn
swIGMPRobustness=_SwIGMPRobustness_Object((1,3,6,1,4,1,171,12,2,3,3,1,4),_SwIGMPRobustness_Type())
swIGMPRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPRobustness.setStatus(_A)
class _SwIGMPCtrlTimer_Type(Integer32):defaultValue=300
_SwIGMPCtrlTimer_Type.__name__=_D
_SwIGMPCtrlTimer_Object=MibTableColumn
swIGMPCtrlTimer=_SwIGMPCtrlTimer_Object((1,3,6,1,4,1,171,12,2,3,3,1,5),_SwIGMPCtrlTimer_Type())
swIGMPCtrlTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPCtrlTimer.setStatus(_A)
class _SwIGMPQuerierVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('v0Querier',2),('v1Querier',3),('v2Querier',4)))
_SwIGMPQuerierVersion_Type.__name__=_D
_SwIGMPQuerierVersion_Object=MibTableColumn
swIGMPQuerierVersion=_SwIGMPQuerierVersion_Object((1,3,6,1,4,1,171,12,2,3,3,1,6),_SwIGMPQuerierVersion_Type())
swIGMPQuerierVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPQuerierVersion.setStatus(_A)
_SwIGMPCtrlState_Type=RowStatus
_SwIGMPCtrlState_Object=MibTableColumn
swIGMPCtrlState=_SwIGMPCtrlState_Object((1,3,6,1,4,1,171,12,2,3,3,1,7),_SwIGMPCtrlState_Type())
swIGMPCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPCtrlState.setStatus(_A)
_SwIGMPIfnoMaxEntries_Type=Integer32
_SwIGMPIfnoMaxEntries_Object=MibScalar
swIGMPIfnoMaxEntries=_SwIGMPIfnoMaxEntries_Object((1,3,6,1,4,1,171,12,2,3,4),_SwIGMPIfnoMaxEntries_Type())
swIGMPIfnoMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPIfnoMaxEntries.setStatus(_A)
_SwIGMPInfoTable_Object=MibTable
swIGMPInfoTable=_SwIGMPInfoTable_Object((1,3,6,1,4,1,171,12,2,3,5))
if mibBuilder.loadTexts:swIGMPInfoTable.setStatus(_A)
_SwIGMPInfoEntry_Object=MibTableRow
swIGMPInfoEntry=_SwIGMPInfoEntry_Object((1,3,6,1,4,1,171,12,2,3,5,1))
swIGMPInfoEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:swIGMPInfoEntry.setStatus(_A)
_SwIGMPInfoVid_Type=Integer32
_SwIGMPInfoVid_Object=MibTableColumn
swIGMPInfoVid=_SwIGMPInfoVid_Object((1,3,6,1,4,1,171,12,2,3,5,1,1),_SwIGMPInfoVid_Type())
swIGMPInfoVid.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPInfoVid.setStatus(_A)
_SwIGMPInfoQueryCount_Type=Integer32
_SwIGMPInfoQueryCount_Object=MibTableColumn
swIGMPInfoQueryCount=_SwIGMPInfoQueryCount_Object((1,3,6,1,4,1,171,12,2,3,5,1,2),_SwIGMPInfoQueryCount_Type())
swIGMPInfoQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPInfoQueryCount.setStatus(_A)
_SwIGMPInfoTxQueryCount_Type=Integer32
_SwIGMPInfoTxQueryCount_Object=MibTableColumn
swIGMPInfoTxQueryCount=_SwIGMPInfoTxQueryCount_Object((1,3,6,1,4,1,171,12,2,3,5,1,3),_SwIGMPInfoTxQueryCount_Type())
swIGMPInfoTxQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPInfoTxQueryCount.setStatus(_A)
_SwIGMPTableMaxEntries_Type=Integer32
_SwIGMPTableMaxEntries_Object=MibScalar
swIGMPTableMaxEntries=_SwIGMPTableMaxEntries_Object((1,3,6,1,4,1,171,12,2,3,6),_SwIGMPTableMaxEntries_Type())
swIGMPTableMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPTableMaxEntries.setStatus(_A)
_SwIGMPTable_Object=MibTable
swIGMPTable=_SwIGMPTable_Object((1,3,6,1,4,1,171,12,2,3,7))
if mibBuilder.loadTexts:swIGMPTable.setStatus(_A)
_SwIGMPEntry_Object=MibTableRow
swIGMPEntry=_SwIGMPEntry_Object((1,3,6,1,4,1,171,12,2,3,7,1))
swIGMPEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:swIGMPEntry.setStatus(_A)
_SwIGMPVid_Type=Integer32
_SwIGMPVid_Object=MibTableColumn
swIGMPVid=_SwIGMPVid_Object((1,3,6,1,4,1,171,12,2,3,7,1,1),_SwIGMPVid_Type())
swIGMPVid.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPVid.setStatus(_A)
_SwIGMPGroupIpAddr_Type=IpAddress
_SwIGMPGroupIpAddr_Object=MibTableColumn
swIGMPGroupIpAddr=_SwIGMPGroupIpAddr_Object((1,3,6,1,4,1,171,12,2,3,7,1,2),_SwIGMPGroupIpAddr_Type())
swIGMPGroupIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPGroupIpAddr.setStatus(_A)
_SwIGMPMacAddr_Type=MacAddress
_SwIGMPMacAddr_Object=MibTableColumn
swIGMPMacAddr=_SwIGMPMacAddr_Object((1,3,6,1,4,1,171,12,2,3,7,1,3),_SwIGMPMacAddr_Type())
swIGMPMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPMacAddr.setStatus(_A)
_SwIGMPPortMap_Type=PortList
_SwIGMPPortMap_Object=MibTableColumn
swIGMPPortMap=_SwIGMPPortMap_Object((1,3,6,1,4,1,171,12,2,3,7,1,4),_SwIGMPPortMap_Type())
swIGMPPortMap.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPPortMap.setStatus(_A)
_SwIGMPIpGroupReportCount_Type=Integer32
_SwIGMPIpGroupReportCount_Object=MibTableColumn
swIGMPIpGroupReportCount=_SwIGMPIpGroupReportCount_Object((1,3,6,1,4,1,171,12,2,3,7,1,5),_SwIGMPIpGroupReportCount_Type())
swIGMPIpGroupReportCount.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPIpGroupReportCount.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'PortList':PortList,'swDlinkL2Mgmt':swDlinkL2Mgmt,'swPortTrunkPackage':swPortTrunkPackage,'swPortTrunkMaxEntries':swPortTrunkMaxEntries,'swPortTrunkMaxPortMembers':swPortTrunkMaxPortMembers,'swPortTrunkTable':swPortTrunkTable,'swPortTrunkEntry':swPortTrunkEntry,_H:swPortTrunkIndex,'swPortTrunkName':swPortTrunkName,'swPortTrunkMasterPort':swPortTrunkMasterPort,'swPortTrunkPortList':swPortTrunkPortList,'swPortTrunkState':swPortTrunkState,'swPortMirrorPackage':swPortMirrorPackage,'swPortMirrorMaxEntries':swPortMirrorMaxEntries,'swPortMirrorCtrlTable':swPortMirrorCtrlTable,'swPortMirrorCtrlEntry':swPortMirrorCtrlEntry,_I:swPortMirrorIndex,'swPortMirrorSourcePort':swPortMirrorSourcePort,'swPortMirrorTargetPort':swPortMirrorTargetPort,'swPortMirrorDirection':swPortMirrorDirection,'swPortMirrorState':swPortMirrorState,'swIGMPPackage':swIGMPPackage,'swIGMPCtrlStatus':swIGMPCtrlStatus,'swIGMPCtrlMaxEntries':swIGMPCtrlMaxEntries,'swIGMPCtrlTable':swIGMPCtrlTable,'swIGMPCtrlEntry':swIGMPCtrlEntry,_J:swIGMPCtrlVid,'swIGMPQueryInterval':swIGMPQueryInterval,'swIGMPQueryMaxResponseTime':swIGMPQueryMaxResponseTime,'swIGMPRobustness':swIGMPRobustness,'swIGMPCtrlTimer':swIGMPCtrlTimer,'swIGMPQuerierVersion':swIGMPQuerierVersion,'swIGMPCtrlState':swIGMPCtrlState,'swIGMPIfnoMaxEntries':swIGMPIfnoMaxEntries,'swIGMPInfoTable':swIGMPInfoTable,'swIGMPInfoEntry':swIGMPInfoEntry,_L:swIGMPInfoVid,'swIGMPInfoQueryCount':swIGMPInfoQueryCount,'swIGMPInfoTxQueryCount':swIGMPInfoTxQueryCount,'swIGMPTableMaxEntries':swIGMPTableMaxEntries,'swIGMPTable':swIGMPTable,'swIGMPEntry':swIGMPEntry,_M:swIGMPVid,_N:swIGMPGroupIpAddr,'swIGMPMacAddr':swIGMPMacAddr,'swIGMPPortMap':swIGMPPortMap,'swIGMPIpGroupReportCount':swIGMPIpGroupReportCount})