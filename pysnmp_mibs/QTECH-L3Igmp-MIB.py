_L='igmpSrcAddress'
_K='not-accessible'
_J='igmpVlanID'
_I='igmpGroupIP'
_H='igmpifIndex'
_G='PortList'
_F='igmpCacheIfIdxEx'
_E='igmpCacheAddressEx'
_D='read-only'
_C='QTECH-L3Igmp-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_G)
gbnL3,=mibBuilder.importSymbols('QTECH-MASTER-MIB','gbnL3')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnL3IgmpMib=ModuleIdentity((1,3,6,1,4,1,27514,1,2,5,7))
if mibBuilder.loadTexts:gbnL3IgmpMib.setRevisions(('1904-11-19 00:01',))
class FilterMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
class PortList(TextualConvention,OctetString):status=_A
_GbnL3IgmpProxyGroup_ObjectIdentity=ObjectIdentity
gbnL3IgmpProxyGroup=_GbnL3IgmpProxyGroup_ObjectIdentity((1,3,6,1,4,1,27514,1,2,5,7,1))
_IgmpProxyEnable_Type=TruthValue
_IgmpProxyEnable_Object=MibScalar
igmpProxyEnable=_IgmpProxyEnable_Object((1,3,6,1,4,1,27514,1,2,5,7,1,1),_IgmpProxyEnable_Type())
igmpProxyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpProxyEnable.setStatus(_A)
_IgmpProxyIfIndex_Type=Integer32
_IgmpProxyIfIndex_Object=MibScalar
igmpProxyIfIndex=_IgmpProxyIfIndex_Object((1,3,6,1,4,1,27514,1,2,5,7,1,2),_IgmpProxyIfIndex_Type())
igmpProxyIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpProxyIfIndex.setStatus(_A)
_IgmpGrpNum_Type=Integer32
_IgmpGrpNum_Object=MibScalar
igmpGrpNum=_IgmpGrpNum_Object((1,3,6,1,4,1,27514,1,2,5,7,1,3),_IgmpGrpNum_Type())
igmpGrpNum.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpGrpNum.setStatus(_A)
_IgmpGrpMembNum_Type=Integer32
_IgmpGrpMembNum_Object=MibScalar
igmpGrpMembNum=_IgmpGrpMembNum_Object((1,3,6,1,4,1,27514,1,2,5,7,1,4),_IgmpGrpMembNum_Type())
igmpGrpMembNum.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpGrpMembNum.setStatus(_A)
_IgmpIfExTable_Object=MibTable
igmpIfExTable=_IgmpIfExTable_Object((1,3,6,1,4,1,27514,1,2,5,7,2))
if mibBuilder.loadTexts:igmpIfExTable.setStatus(_A)
_IgmpIfExEntry_Object=MibTableRow
igmpIfExEntry=_IgmpIfExEntry_Object((1,3,6,1,4,1,27514,1,2,5,7,2,1))
igmpIfExEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:igmpIfExEntry.setStatus(_A)
_IgmpifIndex_Type=Integer32
_IgmpifIndex_Object=MibTableColumn
igmpifIndex=_IgmpifIndex_Object((1,3,6,1,4,1,27514,1,2,5,7,2,1,1),_IgmpifIndex_Type())
igmpifIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpifIndex.setStatus(_A)
_IgmpIfPortList_Type=PortList
_IgmpIfPortList_Object=MibTableColumn
igmpIfPortList=_IgmpIfPortList_Object((1,3,6,1,4,1,27514,1,2,5,7,2,1,2),_IgmpIfPortList_Type())
igmpIfPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpIfPortList.setStatus(_A)
_IgmpifAccessNum_Type=Integer32
_IgmpifAccessNum_Object=MibTableColumn
igmpifAccessNum=_IgmpifAccessNum_Object((1,3,6,1,4,1,27514,1,2,5,7,2,1,3),_IgmpifAccessNum_Type())
igmpifAccessNum.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpifAccessNum.setStatus(_A)
_IgmpifQuerierExpire_Type=Integer32
_IgmpifQuerierExpire_Object=MibTableColumn
igmpifQuerierExpire=_IgmpifQuerierExpire_Object((1,3,6,1,4,1,27514,1,2,5,7,2,1,4),_IgmpifQuerierExpire_Type())
igmpifQuerierExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpifQuerierExpire.setStatus(_A)
_IgmpifV2QuerierTimer_Type=TimeTicks
_IgmpifV2QuerierTimer_Object=MibTableColumn
igmpifV2QuerierTimer=_IgmpifV2QuerierTimer_Object((1,3,6,1,4,1,27514,1,2,5,7,2,1,5),_IgmpifV2QuerierTimer_Type())
igmpifV2QuerierTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpifV2QuerierTimer.setStatus(_A)
_IgmpifLimiGroupNum_Type=Integer32
_IgmpifLimiGroupNum_Object=MibTableColumn
igmpifLimiGroupNum=_IgmpifLimiGroupNum_Object((1,3,6,1,4,1,27514,1,2,5,7,2,1,6),_IgmpifLimiGroupNum_Type())
igmpifLimiGroupNum.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpifLimiGroupNum.setStatus(_A)
_IgmpGroupVlanTable_Object=MibTable
igmpGroupVlanTable=_IgmpGroupVlanTable_Object((1,3,6,1,4,1,27514,1,2,5,7,3))
if mibBuilder.loadTexts:igmpGroupVlanTable.setStatus(_A)
_IgmpGroupVlanEntry_Object=MibTableRow
igmpGroupVlanEntry=_IgmpGroupVlanEntry_Object((1,3,6,1,4,1,27514,1,2,5,7,3,1))
igmpGroupVlanEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:igmpGroupVlanEntry.setStatus(_A)
_IgmpGroupIP_Type=IpAddress
_IgmpGroupIP_Object=MibTableColumn
igmpGroupIP=_IgmpGroupIP_Object((1,3,6,1,4,1,27514,1,2,5,7,3,1,1),_IgmpGroupIP_Type())
igmpGroupIP.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpGroupIP.setStatus(_A)
_IgmpVlanID_Type=Integer32
_IgmpVlanID_Object=MibTableColumn
igmpVlanID=_IgmpVlanID_Object((1,3,6,1,4,1,27514,1,2,5,7,3,1,2),_IgmpVlanID_Type())
igmpVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpVlanID.setStatus(_A)
_IgmpGroupVlanStatus_Type=RowStatus
_IgmpGroupVlanStatus_Object=MibTableColumn
igmpGroupVlanStatus=_IgmpGroupVlanStatus_Object((1,3,6,1,4,1,27514,1,2,5,7,3,1,3),_IgmpGroupVlanStatus_Type())
igmpGroupVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpGroupVlanStatus.setStatus(_A)
_IgmpCacheTableEx_Object=MibTable
igmpCacheTableEx=_IgmpCacheTableEx_Object((1,3,6,1,4,1,27514,1,2,5,7,4))
if mibBuilder.loadTexts:igmpCacheTableEx.setStatus(_A)
_IgmpCacheExEntry_Object=MibTableRow
igmpCacheExEntry=_IgmpCacheExEntry_Object((1,3,6,1,4,1,27514,1,2,5,7,4,1))
igmpCacheExEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:igmpCacheExEntry.setStatus(_A)
_IgmpCacheAddressEx_Type=IpAddress
_IgmpCacheAddressEx_Object=MibTableColumn
igmpCacheAddressEx=_IgmpCacheAddressEx_Object((1,3,6,1,4,1,27514,1,2,5,7,4,1,1),_IgmpCacheAddressEx_Type())
igmpCacheAddressEx.setMaxAccess(_K)
if mibBuilder.loadTexts:igmpCacheAddressEx.setStatus(_A)
_IgmpCacheIfIdxEx_Type=Integer32
_IgmpCacheIfIdxEx_Object=MibTableColumn
igmpCacheIfIdxEx=_IgmpCacheIfIdxEx_Object((1,3,6,1,4,1,27514,1,2,5,7,4,1,2),_IgmpCacheIfIdxEx_Type())
igmpCacheIfIdxEx.setMaxAccess(_K)
if mibBuilder.loadTexts:igmpCacheIfIdxEx.setStatus(_A)
_IgmpCacheVersion2HostTimer_Type=TimeTicks
_IgmpCacheVersion2HostTimer_Object=MibTableColumn
igmpCacheVersion2HostTimer=_IgmpCacheVersion2HostTimer_Object((1,3,6,1,4,1,27514,1,2,5,7,4,1,3),_IgmpCacheVersion2HostTimer_Type())
igmpCacheVersion2HostTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpCacheVersion2HostTimer.setStatus(_A)
_IgmpCacheFilterMode_Type=FilterMode
_IgmpCacheFilterMode_Object=MibTableColumn
igmpCacheFilterMode=_IgmpCacheFilterMode_Object((1,3,6,1,4,1,27514,1,2,5,7,4,1,4),_IgmpCacheFilterMode_Type())
igmpCacheFilterMode.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpCacheFilterMode.setStatus(_A)
_IgmpSrcInfoTable_Object=MibTable
igmpSrcInfoTable=_IgmpSrcInfoTable_Object((1,3,6,1,4,1,27514,1,2,5,7,5))
if mibBuilder.loadTexts:igmpSrcInfoTable.setStatus(_A)
_IgmpSrcInfoEntry_Object=MibTableRow
igmpSrcInfoEntry=_IgmpSrcInfoEntry_Object((1,3,6,1,4,1,27514,1,2,5,7,5,1))
igmpSrcInfoEntry.setIndexNames((0,_C,_E),(0,_C,_F),(0,_C,_L))
if mibBuilder.loadTexts:igmpSrcInfoEntry.setStatus(_A)
_IgmpSrcAddress_Type=IpAddress
_IgmpSrcAddress_Object=MibTableColumn
igmpSrcAddress=_IgmpSrcAddress_Object((1,3,6,1,4,1,27514,1,2,5,7,5,1,1),_IgmpSrcAddress_Type())
igmpSrcAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSrcAddress.setStatus(_A)
_IgmpSrcTimer_Type=TimeTicks
_IgmpSrcTimer_Object=MibTableColumn
igmpSrcTimer=_IgmpSrcTimer_Object((1,3,6,1,4,1,27514,1,2,5,7,5,1,2),_IgmpSrcTimer_Type())
igmpSrcTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSrcTimer.setStatus(_A)
_IgmpSrcInfoStatus_Type=RowStatus
_IgmpSrcInfoStatus_Object=MibTableColumn
igmpSrcInfoStatus=_IgmpSrcInfoStatus_Object((1,3,6,1,4,1,27514,1,2,5,7,5,1,3),_IgmpSrcInfoStatus_Type())
igmpSrcInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSrcInfoStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_G:PortList,'FilterMode':FilterMode,'gbnL3IgmpMib':gbnL3IgmpMib,'gbnL3IgmpProxyGroup':gbnL3IgmpProxyGroup,'igmpProxyEnable':igmpProxyEnable,'igmpProxyIfIndex':igmpProxyIfIndex,'igmpGrpNum':igmpGrpNum,'igmpGrpMembNum':igmpGrpMembNum,'igmpIfExTable':igmpIfExTable,'igmpIfExEntry':igmpIfExEntry,_H:igmpifIndex,'igmpIfPortList':igmpIfPortList,'igmpifAccessNum':igmpifAccessNum,'igmpifQuerierExpire':igmpifQuerierExpire,'igmpifV2QuerierTimer':igmpifV2QuerierTimer,'igmpifLimiGroupNum':igmpifLimiGroupNum,'igmpGroupVlanTable':igmpGroupVlanTable,'igmpGroupVlanEntry':igmpGroupVlanEntry,_I:igmpGroupIP,_J:igmpVlanID,'igmpGroupVlanStatus':igmpGroupVlanStatus,'igmpCacheTableEx':igmpCacheTableEx,'igmpCacheExEntry':igmpCacheExEntry,_E:igmpCacheAddressEx,_F:igmpCacheIfIdxEx,'igmpCacheVersion2HostTimer':igmpCacheVersion2HostTimer,'igmpCacheFilterMode':igmpCacheFilterMode,'igmpSrcInfoTable':igmpSrcInfoTable,'igmpSrcInfoEntry':igmpSrcInfoEntry,_L:igmpSrcAddress,'igmpSrcTimer':igmpSrcTimer,'igmpSrcInfoStatus':igmpSrcInfoStatus})