_d='tnMcLagInfoLagEntry'
_c='tnMcDomainId'
_b='tnMcsClientApplication'
_a='tnMcPeerSyncPortEncapMax'
_Z='tnMcPeerSyncPortEncapMin'
_Y='tnMcPeerSyncPortEncapType'
_X='TmnxEnabledDisabled'
_W='InetAddressPrefixLength'
_V='tnMcLagConfigLagId'
_U='read-write'
_T='tnMcPeerSyncPortId'
_S='TItemDescription'
_R='Bits'
_Q='InetAddressType'
_P='OctetString'
_O='TmnxAdminState'
_N='TNamedItemOrEmpty'
_M='InetAddress'
_L='TruthValue'
_K='Integer32'
_J='Unsigned32'
_I='not-accessible'
_H='tnMcPeerIpAddr'
_G='tnMcPeerIpType'
_F='tnSysSwitchId'
_E='TROPIC-SYSTEM-MIB'
_D='read-create'
_C='TN-MC-REDUNDANCY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_M,_W,_Q)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_R,'Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_L)
LAGInterfaceNumber,=mibBuilder.importSymbols('TN-LAG-MIB','LAGInterfaceNumber')
tnSapEncapValue,tnSapPortId=mibBuilder.importSymbols('TN-SAP-MIB','tnSapEncapValue','tnSapPortId')
tnSvcId,=mibBuilder.importSymbols('TN-SERV-MIB','tnSvcId')
TItemDescription,TNamedItem,TNamedItemOrEmpty,TmnxAdminState,TmnxEnabledDisabled,TmnxEncapVal,TmnxOperState,TmnxPortID,TmnxVRtrID=mibBuilder.importSymbols('TN-TC-MIB',_S,'TNamedItem',_N,_O,_X,'TmnxEncapVal','TmnxOperState','TmnxPortID','TmnxVRtrID')
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_E,_F)
tnMcRedundancyMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,40))
if mibBuilder.loadTexts:tnMcRedundancyMIBModule.setRevisions(('2012-11-28 00:00',))
class TmnxMcsClientApp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('igmp',0),('igmpSnooping',1),('subMgmtIpoe',2),('srrp',3),('mcRing',4),('mldSnooping',5),('dhcpServer',6),('subHostTrk',7),('subMgmtPppoe',8)))
_TnMcRedundancy_ObjectIdentity=ObjectIdentity
tnMcRedundancy=_TnMcRedundancy_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,40))
_TnMcRedundancyObjs_ObjectIdentity=ObjectIdentity
tnMcRedundancyObjs=_TnMcRedundancyObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,40,1))
_TnMcPeerTable_Object=MibTable
tnMcPeerTable=_TnMcPeerTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1))
if mibBuilder.loadTexts:tnMcPeerTable.setStatus(_A)
_TnMcPeerEntry_Object=MibTableRow
tnMcPeerEntry=_TnMcPeerEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1))
tnMcPeerEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:tnMcPeerEntry.setStatus(_A)
_TnMcPeerIpType_Type=InetAddressType
_TnMcPeerIpType_Object=MibTableColumn
tnMcPeerIpType=_TnMcPeerIpType_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,1),_TnMcPeerIpType_Type())
tnMcPeerIpType.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcPeerIpType.setStatus(_A)
_TnMcPeerIpAddr_Type=InetAddress
_TnMcPeerIpAddr_Object=MibTableColumn
tnMcPeerIpAddr=_TnMcPeerIpAddr_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,2),_TnMcPeerIpAddr_Type())
tnMcPeerIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcPeerIpAddr.setStatus(_A)
_TnMcPeerRowStatus_Type=RowStatus
_TnMcPeerRowStatus_Object=MibTableColumn
tnMcPeerRowStatus=_TnMcPeerRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,3),_TnMcPeerRowStatus_Type())
tnMcPeerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerRowStatus.setStatus(_A)
class _TnMcPeerDescription_Type(TItemDescription):defaultValue=OctetString('')
_TnMcPeerDescription_Type.__name__=_S
_TnMcPeerDescription_Object=MibTableColumn
tnMcPeerDescription=_TnMcPeerDescription_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,4),_TnMcPeerDescription_Type())
tnMcPeerDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerDescription.setStatus(_A)
class _TnMcPeerAuthKey_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TnMcPeerAuthKey_Type.__name__=_P
_TnMcPeerAuthKey_Object=MibTableColumn
tnMcPeerAuthKey=_TnMcPeerAuthKey_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,5),_TnMcPeerAuthKey_Type())
tnMcPeerAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerAuthKey.setStatus(_A)
class _TnMcPeerSrcIpType_Type(InetAddressType):defaultValue=0
_TnMcPeerSrcIpType_Type.__name__=_Q
_TnMcPeerSrcIpType_Object=MibTableColumn
tnMcPeerSrcIpType=_TnMcPeerSrcIpType_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,6),_TnMcPeerSrcIpType_Type())
tnMcPeerSrcIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSrcIpType.setStatus(_A)
class _TnMcPeerSrcIpAddr_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_TnMcPeerSrcIpAddr_Type.__name__=_M
_TnMcPeerSrcIpAddr_Object=MibTableColumn
tnMcPeerSrcIpAddr=_TnMcPeerSrcIpAddr_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,7),_TnMcPeerSrcIpAddr_Type())
tnMcPeerSrcIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSrcIpAddr.setStatus(_A)
class _TnMcPeerAdminState_Type(TmnxAdminState):defaultValue=3
_TnMcPeerAdminState_Type.__name__=_O
_TnMcPeerAdminState_Object=MibTableColumn
tnMcPeerAdminState=_TnMcPeerAdminState_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,8),_TnMcPeerAdminState_Type())
tnMcPeerAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerAdminState.setStatus(_A)
_TnMcPeerSrcIpOperType_Type=InetAddressType
_TnMcPeerSrcIpOperType_Object=MibTableColumn
tnMcPeerSrcIpOperType=_TnMcPeerSrcIpOperType_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,9),_TnMcPeerSrcIpOperType_Type())
tnMcPeerSrcIpOperType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSrcIpOperType.setStatus(_A)
class _TnMcPeerSrcIpOperAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_TnMcPeerSrcIpOperAddr_Type.__name__=_M
_TnMcPeerSrcIpOperAddr_Object=MibTableColumn
tnMcPeerSrcIpOperAddr=_TnMcPeerSrcIpOperAddr_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,10),_TnMcPeerSrcIpOperAddr_Type())
tnMcPeerSrcIpOperAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSrcIpOperAddr.setStatus(_A)
_TnMcPeerRingsOperState_Type=TmnxOperState
_TnMcPeerRingsOperState_Object=MibTableColumn
tnMcPeerRingsOperState=_TnMcPeerRingsOperState_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,11),_TnMcPeerRingsOperState_Type())
tnMcPeerRingsOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerRingsOperState.setStatus(_A)
class _TnMcPeerName_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TnMcPeerName_Type.__name__=_N
_TnMcPeerName_Object=MibTableColumn
tnMcPeerName=_TnMcPeerName_Object((1,3,6,1,4,1,7483,6,1,2,40,1,1,1,12),_TnMcPeerName_Type())
tnMcPeerName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerName.setStatus(_A)
_TnMcPeerSyncTable_Object=MibTable
tnMcPeerSyncTable=_TnMcPeerSyncTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2))
if mibBuilder.loadTexts:tnMcPeerSyncTable.setStatus(_A)
_TnMcPeerSyncEntry_Object=MibTableRow
tnMcPeerSyncEntry=_TnMcPeerSyncEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1))
tnMcPeerSyncEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:tnMcPeerSyncEntry.setStatus(_A)
_TnMcPeerSyncRowStatus_Type=RowStatus
_TnMcPeerSyncRowStatus_Object=MibTableColumn
tnMcPeerSyncRowStatus=_TnMcPeerSyncRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,1),_TnMcPeerSyncRowStatus_Type())
tnMcPeerSyncRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncRowStatus.setStatus(_A)
class _TnMcPeerSyncIgmp_Type(TruthValue):defaultValue=2
_TnMcPeerSyncIgmp_Type.__name__=_L
_TnMcPeerSyncIgmp_Object=MibTableColumn
tnMcPeerSyncIgmp=_TnMcPeerSyncIgmp_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,2),_TnMcPeerSyncIgmp_Type())
tnMcPeerSyncIgmp.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncIgmp.setStatus(_A)
class _TnMcPeerSyncIgmpSnooping_Type(TruthValue):defaultValue=2
_TnMcPeerSyncIgmpSnooping_Type.__name__=_L
_TnMcPeerSyncIgmpSnooping_Object=MibTableColumn
tnMcPeerSyncIgmpSnooping=_TnMcPeerSyncIgmpSnooping_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,3),_TnMcPeerSyncIgmpSnooping_Type())
tnMcPeerSyncIgmpSnooping.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncIgmpSnooping.setStatus(_A)
class _TnMcPeerSyncSubMgmt_Type(TruthValue):defaultValue=2
_TnMcPeerSyncSubMgmt_Type.__name__=_L
_TnMcPeerSyncSubMgmt_Object=MibTableColumn
tnMcPeerSyncSubMgmt=_TnMcPeerSyncSubMgmt_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,4),_TnMcPeerSyncSubMgmt_Type())
tnMcPeerSyncSubMgmt.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncSubMgmt.setStatus(_A)
class _TnMcPeerSyncSrrp_Type(TruthValue):defaultValue=2
_TnMcPeerSyncSrrp_Type.__name__=_L
_TnMcPeerSyncSrrp_Object=MibTableColumn
tnMcPeerSyncSrrp=_TnMcPeerSyncSrrp_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,5),_TnMcPeerSyncSrrp_Type())
tnMcPeerSyncSrrp.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncSrrp.setStatus(_A)
class _TnMcPeerSyncAdminState_Type(TmnxAdminState):defaultValue=3
_TnMcPeerSyncAdminState_Type.__name__=_O
_TnMcPeerSyncAdminState_Object=MibTableColumn
tnMcPeerSyncAdminState=_TnMcPeerSyncAdminState_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,6),_TnMcPeerSyncAdminState_Type())
tnMcPeerSyncAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncAdminState.setStatus(_A)
_TnMcPeerSyncOperState_Type=TmnxOperState
_TnMcPeerSyncOperState_Object=MibTableColumn
tnMcPeerSyncOperState=_TnMcPeerSyncOperState_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,7),_TnMcPeerSyncOperState_Type())
tnMcPeerSyncOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncOperState.setStatus(_A)
class _TnMcPeerSyncOperFlags_Type(Bits):namedValues=NamedValues(*(('syncAdminDown',0),('peerAdminDown',1),('connectionDown',2),('internalError',3),('mcsVersionMismatch',4),('platformMismatch',5),('appVersionMismatch',6),('appSupportMismatch',7)))
_TnMcPeerSyncOperFlags_Type.__name__=_R
_TnMcPeerSyncOperFlags_Object=MibTableColumn
tnMcPeerSyncOperFlags=_TnMcPeerSyncOperFlags_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,8),_TnMcPeerSyncOperFlags_Type())
tnMcPeerSyncOperFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncOperFlags.setStatus(_A)
class _TnMcPeerSyncStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inSync',1),('syncInProgress',2),('outOfSync',3)))
_TnMcPeerSyncStatus_Type.__name__=_K
_TnMcPeerSyncStatus_Object=MibTableColumn
tnMcPeerSyncStatus=_TnMcPeerSyncStatus_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,9),_TnMcPeerSyncStatus_Type())
tnMcPeerSyncStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncStatus.setStatus(_A)
_TnMcPeerSyncLastSyncTime_Type=TimeStamp
_TnMcPeerSyncLastSyncTime_Object=MibTableColumn
tnMcPeerSyncLastSyncTime=_TnMcPeerSyncLastSyncTime_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,10),_TnMcPeerSyncLastSyncTime_Type())
tnMcPeerSyncLastSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncLastSyncTime.setStatus(_A)
_TnMcPeerSyncNumEntries_Type=Counter32
_TnMcPeerSyncNumEntries_Object=MibTableColumn
tnMcPeerSyncNumEntries=_TnMcPeerSyncNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,11),_TnMcPeerSyncNumEntries_Type())
tnMcPeerSyncNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncNumEntries.setStatus(_A)
_TnMcPeerSyncLclDeletedEntries_Type=Counter32
_TnMcPeerSyncLclDeletedEntries_Object=MibTableColumn
tnMcPeerSyncLclDeletedEntries=_TnMcPeerSyncLclDeletedEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,12),_TnMcPeerSyncLclDeletedEntries_Type())
tnMcPeerSyncLclDeletedEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncLclDeletedEntries.setStatus(_A)
_TnMcPeerSyncAlarmedEntries_Type=Counter32
_TnMcPeerSyncAlarmedEntries_Object=MibTableColumn
tnMcPeerSyncAlarmedEntries=_TnMcPeerSyncAlarmedEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,13),_TnMcPeerSyncAlarmedEntries_Type())
tnMcPeerSyncAlarmedEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncAlarmedEntries.setStatus(_A)
_TnMcPeerSyncRemNumEntries_Type=Counter32
_TnMcPeerSyncRemNumEntries_Object=MibTableColumn
tnMcPeerSyncRemNumEntries=_TnMcPeerSyncRemNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,14),_TnMcPeerSyncRemNumEntries_Type())
tnMcPeerSyncRemNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncRemNumEntries.setStatus(_A)
_TnMcPeerSyncRemLclDelEntries_Type=Counter32
_TnMcPeerSyncRemLclDelEntries_Object=MibTableColumn
tnMcPeerSyncRemLclDelEntries=_TnMcPeerSyncRemLclDelEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,15),_TnMcPeerSyncRemLclDelEntries_Type())
tnMcPeerSyncRemLclDelEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncRemLclDelEntries.setStatus(_A)
_TnMcPeerSyncRemAlarmedEntries_Type=Counter32
_TnMcPeerSyncRemAlarmedEntries_Object=MibTableColumn
tnMcPeerSyncRemAlarmedEntries=_TnMcPeerSyncRemAlarmedEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,2,1,16),_TnMcPeerSyncRemAlarmedEntries_Type())
tnMcPeerSyncRemAlarmedEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncRemAlarmedEntries.setStatus(_A)
_TnMcPeerSyncPortTable_Object=MibTable
tnMcPeerSyncPortTable=_TnMcPeerSyncPortTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,3))
if mibBuilder.loadTexts:tnMcPeerSyncPortTable.setStatus(_A)
_TnMcPeerSyncPortEntry_Object=MibTableRow
tnMcPeerSyncPortEntry=_TnMcPeerSyncPortEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,3,1))
tnMcPeerSyncPortEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H),(0,_C,_T))
if mibBuilder.loadTexts:tnMcPeerSyncPortEntry.setStatus(_A)
_TnMcPeerSyncPortId_Type=TmnxPortID
_TnMcPeerSyncPortId_Object=MibTableColumn
tnMcPeerSyncPortId=_TnMcPeerSyncPortId_Object((1,3,6,1,4,1,7483,6,1,2,40,1,3,1,1),_TnMcPeerSyncPortId_Type())
tnMcPeerSyncPortId.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcPeerSyncPortId.setStatus(_A)
_TnMcPeerSyncPortRowStatus_Type=RowStatus
_TnMcPeerSyncPortRowStatus_Object=MibTableColumn
tnMcPeerSyncPortRowStatus=_TnMcPeerSyncPortRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,40,1,3,1,2),_TnMcPeerSyncPortRowStatus_Type())
tnMcPeerSyncPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncPortRowStatus.setStatus(_A)
class _TnMcPeerSyncPortSyncTag_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnMcPeerSyncPortSyncTag_Type.__name__=_N
_TnMcPeerSyncPortSyncTag_Object=MibTableColumn
tnMcPeerSyncPortSyncTag=_TnMcPeerSyncPortSyncTag_Object((1,3,6,1,4,1,7483,6,1,2,40,1,3,1,3),_TnMcPeerSyncPortSyncTag_Type())
tnMcPeerSyncPortSyncTag.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncPortSyncTag.setStatus(_A)
_TnMcPeerSyncPortEncapRangeTable_Object=MibTable
tnMcPeerSyncPortEncapRangeTable=_TnMcPeerSyncPortEncapRangeTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,4))
if mibBuilder.loadTexts:tnMcPeerSyncPortEncapRangeTable.setStatus(_A)
_TnMcPeerSyncPortEncapRangeEntry_Object=MibTableRow
tnMcPeerSyncPortEncapRangeEntry=_TnMcPeerSyncPortEncapRangeEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,4,1))
tnMcPeerSyncPortEncapRangeEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H),(0,_C,_T),(0,_C,_Y),(0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:tnMcPeerSyncPortEncapRangeEntry.setStatus(_A)
class _TnMcPeerSyncPortEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1q',1),('qinq',2)))
_TnMcPeerSyncPortEncapType_Type.__name__=_K
_TnMcPeerSyncPortEncapType_Object=MibTableColumn
tnMcPeerSyncPortEncapType=_TnMcPeerSyncPortEncapType_Object((1,3,6,1,4,1,7483,6,1,2,40,1,4,1,1),_TnMcPeerSyncPortEncapType_Type())
tnMcPeerSyncPortEncapType.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcPeerSyncPortEncapType.setStatus(_A)
_TnMcPeerSyncPortEncapMin_Type=TmnxEncapVal
_TnMcPeerSyncPortEncapMin_Object=MibTableColumn
tnMcPeerSyncPortEncapMin=_TnMcPeerSyncPortEncapMin_Object((1,3,6,1,4,1,7483,6,1,2,40,1,4,1,2),_TnMcPeerSyncPortEncapMin_Type())
tnMcPeerSyncPortEncapMin.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcPeerSyncPortEncapMin.setStatus(_A)
_TnMcPeerSyncPortEncapMax_Type=TmnxEncapVal
_TnMcPeerSyncPortEncapMax_Object=MibTableColumn
tnMcPeerSyncPortEncapMax=_TnMcPeerSyncPortEncapMax_Object((1,3,6,1,4,1,7483,6,1,2,40,1,4,1,3),_TnMcPeerSyncPortEncapMax_Type())
tnMcPeerSyncPortEncapMax.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcPeerSyncPortEncapMax.setStatus(_A)
_TnMcPeerSyncPortEncapRowStatus_Type=RowStatus
_TnMcPeerSyncPortEncapRowStatus_Object=MibTableColumn
tnMcPeerSyncPortEncapRowStatus=_TnMcPeerSyncPortEncapRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,40,1,4,1,4),_TnMcPeerSyncPortEncapRowStatus_Type())
tnMcPeerSyncPortEncapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncPortEncapRowStatus.setStatus(_A)
_TnMcPeerSyncPortEncapSyncTag_Type=TNamedItem
_TnMcPeerSyncPortEncapSyncTag_Object=MibTableColumn
tnMcPeerSyncPortEncapSyncTag=_TnMcPeerSyncPortEncapSyncTag_Object((1,3,6,1,4,1,7483,6,1,2,40,1,4,1,5),_TnMcPeerSyncPortEncapSyncTag_Type())
tnMcPeerSyncPortEncapSyncTag.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcPeerSyncPortEncapSyncTag.setStatus(_A)
_TnMcLagConfigTableLastChanged_Type=TimeStamp
_TnMcLagConfigTableLastChanged_Object=MibScalar
tnMcLagConfigTableLastChanged=_TnMcLagConfigTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,40,1,5),_TnMcLagConfigTableLastChanged_Type())
tnMcLagConfigTableLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigTableLastChanged.setStatus(_A)
_TnMcLagConfigTable_Object=MibTable
tnMcLagConfigTable=_TnMcLagConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,6))
if mibBuilder.loadTexts:tnMcLagConfigTable.setStatus(_A)
_TnMcLagConfigEntry_Object=MibTableRow
tnMcLagConfigEntry=_TnMcLagConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,6,1))
tnMcLagConfigEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:tnMcLagConfigEntry.setStatus(_A)
_TnMcLagConfigPeerLastChanged_Type=TimeStamp
_TnMcLagConfigPeerLastChanged_Object=MibTableColumn
tnMcLagConfigPeerLastChanged=_TnMcLagConfigPeerLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,40,1,6,1,1),_TnMcLagConfigPeerLastChanged_Type())
tnMcLagConfigPeerLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigPeerLastChanged.setStatus(_A)
class _TnMcLagConfigPeerAdminstate_Type(TmnxAdminState):defaultValue=3
_TnMcLagConfigPeerAdminstate_Type.__name__=_O
_TnMcLagConfigPeerAdminstate_Object=MibTableColumn
tnMcLagConfigPeerAdminstate=_TnMcLagConfigPeerAdminstate_Object((1,3,6,1,4,1,7483,6,1,2,40,1,6,1,2),_TnMcLagConfigPeerAdminstate_Type())
tnMcLagConfigPeerAdminstate.setMaxAccess(_U)
if mibBuilder.loadTexts:tnMcLagConfigPeerAdminstate.setStatus(_A)
class _TnMcLagConfigKeepALiveIvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,500))
_TnMcLagConfigKeepALiveIvl_Type.__name__=_J
_TnMcLagConfigKeepALiveIvl_Object=MibTableColumn
tnMcLagConfigKeepALiveIvl=_TnMcLagConfigKeepALiveIvl_Object((1,3,6,1,4,1,7483,6,1,2,40,1,6,1,3),_TnMcLagConfigKeepALiveIvl_Type())
tnMcLagConfigKeepALiveIvl.setMaxAccess(_U)
if mibBuilder.loadTexts:tnMcLagConfigKeepALiveIvl.setStatus(_A)
if mibBuilder.loadTexts:tnMcLagConfigKeepALiveIvl.setUnits('deci-seconds')
class _TnMcLagConfigHoldOnNgbrFailure_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,25))
_TnMcLagConfigHoldOnNgbrFailure_Type.__name__=_J
_TnMcLagConfigHoldOnNgbrFailure_Object=MibTableColumn
tnMcLagConfigHoldOnNgbrFailure=_TnMcLagConfigHoldOnNgbrFailure_Object((1,3,6,1,4,1,7483,6,1,2,40,1,6,1,4),_TnMcLagConfigHoldOnNgbrFailure_Type())
tnMcLagConfigHoldOnNgbrFailure.setMaxAccess(_U)
if mibBuilder.loadTexts:tnMcLagConfigHoldOnNgbrFailure.setStatus(_A)
class _TnMcLagConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inService',0),('outOfService',1)))
_TnMcLagConfigOperState_Type.__name__=_K
_TnMcLagConfigOperState_Object=MibTableColumn
tnMcLagConfigOperState=_TnMcLagConfigOperState_Object((1,3,6,1,4,1,7483,6,1,2,40,1,6,1,5),_TnMcLagConfigOperState_Type())
tnMcLagConfigOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigOperState.setStatus(_A)
_TnMcLagConfigPeerLastStateChge_Type=TimeStamp
_TnMcLagConfigPeerLastStateChge_Object=MibTableColumn
tnMcLagConfigPeerLastStateChge=_TnMcLagConfigPeerLastStateChge_Object((1,3,6,1,4,1,7483,6,1,2,40,1,6,1,6),_TnMcLagConfigPeerLastStateChge_Type())
tnMcLagConfigPeerLastStateChge.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigPeerLastStateChge.setStatus(_A)
_TnMcLagConfigLagTableLastChanged_Type=TimeStamp
_TnMcLagConfigLagTableLastChanged_Object=MibScalar
tnMcLagConfigLagTableLastChanged=_TnMcLagConfigLagTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,40,1,7),_TnMcLagConfigLagTableLastChanged_Type())
tnMcLagConfigLagTableLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigLagTableLastChanged.setStatus(_A)
_TnMcLagConfigLagTable_Object=MibTable
tnMcLagConfigLagTable=_TnMcLagConfigLagTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8))
if mibBuilder.loadTexts:tnMcLagConfigLagTable.setStatus(_A)
_TnMcLagConfigLagEntry_Object=MibTableRow
tnMcLagConfigLagEntry=_TnMcLagConfigLagEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1))
tnMcLagConfigLagEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H),(0,_C,_V))
if mibBuilder.loadTexts:tnMcLagConfigLagEntry.setStatus(_A)
_TnMcLagConfigLagId_Type=LAGInterfaceNumber
_TnMcLagConfigLagId_Object=MibTableColumn
tnMcLagConfigLagId=_TnMcLagConfigLagId_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,1),_TnMcLagConfigLagId_Type())
tnMcLagConfigLagId.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcLagConfigLagId.setStatus(_A)
_TnMcLagConfigLagLastChanged_Type=TimeStamp
_TnMcLagConfigLagLastChanged_Object=MibTableColumn
tnMcLagConfigLagLastChanged=_TnMcLagConfigLagLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,2),_TnMcLagConfigLagLastChanged_Type())
tnMcLagConfigLagLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigLagLastChanged.setStatus(_A)
_TnMcLagConfigLagRowStatus_Type=RowStatus
_TnMcLagConfigLagRowStatus_Object=MibTableColumn
tnMcLagConfigLagRowStatus=_TnMcLagConfigLagRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,3),_TnMcLagConfigLagRowStatus_Type())
tnMcLagConfigLagRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcLagConfigLagRowStatus.setStatus(_A)
class _TnMcLagConfigLaglacpKey_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnMcLagConfigLaglacpKey_Type.__name__=_J
_TnMcLagConfigLaglacpKey_Object=MibTableColumn
tnMcLagConfigLaglacpKey=_TnMcLagConfigLaglacpKey_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,4),_TnMcLagConfigLaglacpKey_Type())
tnMcLagConfigLaglacpKey.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcLagConfigLaglacpKey.setStatus(_A)
class _TnMcLagConfigLagSystemId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TnMcLagConfigLagSystemId_Type.__name__=_P
_TnMcLagConfigLagSystemId_Object=MibTableColumn
tnMcLagConfigLagSystemId=_TnMcLagConfigLagSystemId_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,5),_TnMcLagConfigLagSystemId_Type())
tnMcLagConfigLagSystemId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcLagConfigLagSystemId.setStatus(_A)
class _TnMcLagConfigLagSystemPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnMcLagConfigLagSystemPriority_Type.__name__=_J
_TnMcLagConfigLagSystemPriority_Object=MibTableColumn
tnMcLagConfigLagSystemPriority=_TnMcLagConfigLagSystemPriority_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,6),_TnMcLagConfigLagSystemPriority_Type())
tnMcLagConfigLagSystemPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcLagConfigLagSystemPriority.setStatus(_A)
_TnMcLagConfigLagRemoteLagId_Type=LAGInterfaceNumber
_TnMcLagConfigLagRemoteLagId_Object=MibTableColumn
tnMcLagConfigLagRemoteLagId=_TnMcLagConfigLagRemoteLagId_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,7),_TnMcLagConfigLagRemoteLagId_Type())
tnMcLagConfigLagRemoteLagId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcLagConfigLagRemoteLagId.setStatus(_A)
class _TnMcLagConfigLagSrcBMacLSB_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535),ValueRangeConstraint(4294967295,4294967295))
_TnMcLagConfigLagSrcBMacLSB_Type.__name__=_J
_TnMcLagConfigLagSrcBMacLSB_Object=MibTableColumn
tnMcLagConfigLagSrcBMacLSB=_TnMcLagConfigLagSrcBMacLSB_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,8),_TnMcLagConfigLagSrcBMacLSB_Type())
tnMcLagConfigLagSrcBMacLSB.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcLagConfigLagSrcBMacLSB.setStatus(_A)
_TnMcLagConfigLagOperSrcBMacLSB_Type=Unsigned32
_TnMcLagConfigLagOperSrcBMacLSB_Object=MibTableColumn
tnMcLagConfigLagOperSrcBMacLSB=_TnMcLagConfigLagOperSrcBMacLSB_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,9),_TnMcLagConfigLagOperSrcBMacLSB_Type())
tnMcLagConfigLagOperSrcBMacLSB.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigLagOperSrcBMacLSB.setStatus(_A)
class _TnMcLagConfigLagFlushEthRingOnActive_Type(TmnxEnabledDisabled):defaultValue=2
_TnMcLagConfigLagFlushEthRingOnActive_Type.__name__=_X
_TnMcLagConfigLagFlushEthRingOnActive_Object=MibTableColumn
tnMcLagConfigLagFlushEthRingOnActive=_TnMcLagConfigLagFlushEthRingOnActive_Object((1,3,6,1,4,1,7483,6,1,2,40,1,8,1,10),_TnMcLagConfigLagFlushEthRingOnActive_Type())
tnMcLagConfigLagFlushEthRingOnActive.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcLagConfigLagFlushEthRingOnActive.setStatus(_A)
_TnMcLagInfoLagTable_Object=MibTable
tnMcLagInfoLagTable=_TnMcLagInfoLagTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,10))
if mibBuilder.loadTexts:tnMcLagInfoLagTable.setStatus(_A)
_TnMcLagInfoLagEntry_Object=MibTableRow
tnMcLagInfoLagEntry=_TnMcLagInfoLagEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,10,1))
if mibBuilder.loadTexts:tnMcLagInfoLagEntry.setStatus(_A)
_TnMcLagActiveStandby_Type=TruthValue
_TnMcLagActiveStandby_Object=MibTableColumn
tnMcLagActiveStandby=_TnMcLagActiveStandby_Object((1,3,6,1,4,1,7483,6,1,2,40,1,10,1,1),_TnMcLagActiveStandby_Type())
tnMcLagActiveStandby.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagActiveStandby.setStatus(_A)
_TnMcLagLacpIdInUse_Type=TruthValue
_TnMcLagLacpIdInUse_Object=MibTableColumn
tnMcLagLacpIdInUse=_TnMcLagLacpIdInUse_Object((1,3,6,1,4,1,7483,6,1,2,40,1,10,1,2),_TnMcLagLacpIdInUse_Type())
tnMcLagLacpIdInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagLacpIdInUse.setStatus(_A)
_TnMcLagExtendedTimeOut_Type=TruthValue
_TnMcLagExtendedTimeOut_Object=MibTableColumn
tnMcLagExtendedTimeOut=_TnMcLagExtendedTimeOut_Object((1,3,6,1,4,1,7483,6,1,2,40,1,10,1,3),_TnMcLagExtendedTimeOut_Type())
tnMcLagExtendedTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagExtendedTimeOut.setStatus(_A)
_TnMcLagSelectionLogic_Type=DisplayString
_TnMcLagSelectionLogic_Object=MibTableColumn
tnMcLagSelectionLogic=_TnMcLagSelectionLogic_Object((1,3,6,1,4,1,7483,6,1,2,40,1,10,1,4),_TnMcLagSelectionLogic_Type())
tnMcLagSelectionLogic.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagSelectionLogic.setStatus(_A)
_TnMcLagConfigMismatchString_Type=DisplayString
_TnMcLagConfigMismatchString_Object=MibTableColumn
tnMcLagConfigMismatchString=_TnMcLagConfigMismatchString_Object((1,3,6,1,4,1,7483,6,1,2,40,1,10,1,5),_TnMcLagConfigMismatchString_Type())
tnMcLagConfigMismatchString.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigMismatchString.setStatus(_A)
class _TnMcLagConfigMismatchFlags_Type(Bits):namedValues=NamedValues(*(('lagIsNotMultiChassis',0),('localRemoteLagIdMismatch',1),('lagSelectionCriteriaMismatch',2),('lagEncapsulationMismatch',3),('mcLacpkeyMismatch',4),('mcSystemPriorityMismatch',5),('mcSystemIdMismatch',6)))
_TnMcLagConfigMismatchFlags_Type.__name__=_R
_TnMcLagConfigMismatchFlags_Object=MibTableColumn
tnMcLagConfigMismatchFlags=_TnMcLagConfigMismatchFlags_Object((1,3,6,1,4,1,7483,6,1,2,40,1,10,1,6),_TnMcLagConfigMismatchFlags_Type())
tnMcLagConfigMismatchFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagConfigMismatchFlags.setStatus(_A)
_TnMcsClientAppTable_Object=MibTable
tnMcsClientAppTable=_TnMcsClientAppTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11))
if mibBuilder.loadTexts:tnMcsClientAppTable.setStatus(_A)
_TnMcsClientAppEntry_Object=MibTableRow
tnMcsClientAppEntry=_TnMcsClientAppEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11,1))
tnMcsClientAppEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H),(0,_C,_b))
if mibBuilder.loadTexts:tnMcsClientAppEntry.setStatus(_A)
_TnMcsClientApplication_Type=TmnxMcsClientApp
_TnMcsClientApplication_Object=MibTableColumn
tnMcsClientApplication=_TnMcsClientApplication_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11,1,1),_TnMcsClientApplication_Type())
tnMcsClientApplication.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcsClientApplication.setStatus(_A)
_TnMcsClientNumEntries_Type=Counter32
_TnMcsClientNumEntries_Object=MibTableColumn
tnMcsClientNumEntries=_TnMcsClientNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11,1,2),_TnMcsClientNumEntries_Type())
tnMcsClientNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcsClientNumEntries.setStatus(_A)
_TnMcsClientLclDeletedEntries_Type=Counter32
_TnMcsClientLclDeletedEntries_Object=MibTableColumn
tnMcsClientLclDeletedEntries=_TnMcsClientLclDeletedEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11,1,3),_TnMcsClientLclDeletedEntries_Type())
tnMcsClientLclDeletedEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcsClientLclDeletedEntries.setStatus(_A)
_TnMcsClientAlarmedEntries_Type=Counter32
_TnMcsClientAlarmedEntries_Object=MibTableColumn
tnMcsClientAlarmedEntries=_TnMcsClientAlarmedEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11,1,4),_TnMcsClientAlarmedEntries_Type())
tnMcsClientAlarmedEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcsClientAlarmedEntries.setStatus(_A)
_TnMcsClientRemNumEntries_Type=Counter32
_TnMcsClientRemNumEntries_Object=MibTableColumn
tnMcsClientRemNumEntries=_TnMcsClientRemNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11,1,5),_TnMcsClientRemNumEntries_Type())
tnMcsClientRemNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcsClientRemNumEntries.setStatus(_A)
_TnMcsClientRemLclDelEntries_Type=Counter32
_TnMcsClientRemLclDelEntries_Object=MibTableColumn
tnMcsClientRemLclDelEntries=_TnMcsClientRemLclDelEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11,1,6),_TnMcsClientRemLclDelEntries_Type())
tnMcsClientRemLclDelEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcsClientRemLclDelEntries.setStatus(_A)
_TnMcsClientRemAlarmedEntries_Type=Counter32
_TnMcsClientRemAlarmedEntries_Object=MibTableColumn
tnMcsClientRemAlarmedEntries=_TnMcsClientRemAlarmedEntries_Object((1,3,6,1,4,1,7483,6,1,2,40,1,11,1,7),_TnMcsClientRemAlarmedEntries_Type())
tnMcsClientRemAlarmedEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcsClientRemAlarmedEntries.setStatus(_A)
_TnMcDomainTable_Object=MibTable
tnMcDomainTable=_TnMcDomainTable_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91))
if mibBuilder.loadTexts:tnMcDomainTable.setStatus(_A)
_TnMcDomainEntry_Object=MibTableRow
tnMcDomainEntry=_TnMcDomainEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91,1))
tnMcDomainEntry.setIndexNames((0,_E,_F),(0,_C,_c))
if mibBuilder.loadTexts:tnMcDomainEntry.setStatus(_A)
class _TnMcDomainId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,250))
_TnMcDomainId_Type.__name__=_K
_TnMcDomainId_Object=MibTableColumn
tnMcDomainId=_TnMcDomainId_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91,1,1),_TnMcDomainId_Type())
tnMcDomainId.setMaxAccess(_I)
if mibBuilder.loadTexts:tnMcDomainId.setStatus(_A)
_TnMcDomainRowStatus_Type=RowStatus
_TnMcDomainRowStatus_Object=MibTableColumn
tnMcDomainRowStatus=_TnMcDomainRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91,1,2),_TnMcDomainRowStatus_Type())
tnMcDomainRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcDomainRowStatus.setStatus(_A)
class _TnMcDomainDescription_Type(TItemDescription):defaultHexValue=''
_TnMcDomainDescription_Type.__name__=_S
_TnMcDomainDescription_Object=MibTableColumn
tnMcDomainDescription=_TnMcDomainDescription_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91,1,3),_TnMcDomainDescription_Type())
tnMcDomainDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcDomainDescription.setStatus(_A)
class _TnMcDomainSrcIpType_Type(InetAddressType):defaultValue=0
_TnMcDomainSrcIpType_Type.__name__=_Q
_TnMcDomainSrcIpType_Object=MibTableColumn
tnMcDomainSrcIpType=_TnMcDomainSrcIpType_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91,1,4),_TnMcDomainSrcIpType_Type())
tnMcDomainSrcIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcDomainSrcIpType.setStatus(_A)
class _TnMcDomainSrcIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_TnMcDomainSrcIpAddr_Type.__name__=_M
_TnMcDomainSrcIpAddr_Object=MibTableColumn
tnMcDomainSrcIpAddr=_TnMcDomainSrcIpAddr_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91,1,5),_TnMcDomainSrcIpAddr_Type())
tnMcDomainSrcIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcDomainSrcIpAddr.setStatus(_A)
class _TnMcDomainSrcIpMask_Type(InetAddressPrefixLength):defaultValue=24
_TnMcDomainSrcIpMask_Type.__name__=_W
_TnMcDomainSrcIpMask_Object=MibTableColumn
tnMcDomainSrcIpMask=_TnMcDomainSrcIpMask_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91,1,6),_TnMcDomainSrcIpMask_Type())
tnMcDomainSrcIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcDomainSrcIpMask.setStatus(_A)
class _TnMcDomainSvcName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnMcDomainSvcName_Type.__name__=_N
_TnMcDomainSvcName_Object=MibTableColumn
tnMcDomainSvcName=_TnMcDomainSvcName_Object((1,3,6,1,4,1,7483,6,1,2,40,1,91,1,7),_TnMcDomainSvcName_Type())
tnMcDomainSvcName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMcDomainSvcName.setStatus(_A)
_TnMcRedundancyStatsObjs_ObjectIdentity=ObjectIdentity
tnMcRedundancyStatsObjs=_TnMcRedundancyStatsObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,40,2))
_TnMcLagGlobalStatsTable_Object=MibTable
tnMcLagGlobalStatsTable=_TnMcLagGlobalStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20))
if mibBuilder.loadTexts:tnMcLagGlobalStatsTable.setStatus(_A)
_TnMcLagGlobalStatsEntry_Object=MibTableRow
tnMcLagGlobalStatsEntry=_TnMcLagGlobalStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1))
tnMcLagGlobalStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tnMcLagGlobalStatsEntry.setStatus(_A)
_TnMcLagStatsPktsRx_Type=Counter32
_TnMcLagStatsPktsRx_Object=MibTableColumn
tnMcLagStatsPktsRx=_TnMcLagStatsPktsRx_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,1),_TnMcLagStatsPktsRx_Type())
tnMcLagStatsPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsRx.setStatus(_A)
_TnMcLagStatsPktsRxKeepalive_Type=Counter32
_TnMcLagStatsPktsRxKeepalive_Object=MibTableColumn
tnMcLagStatsPktsRxKeepalive=_TnMcLagStatsPktsRxKeepalive_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,2),_TnMcLagStatsPktsRxKeepalive_Type())
tnMcLagStatsPktsRxKeepalive.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsRxKeepalive.setStatus(_A)
_TnMcLagStatsPktsRxConfig_Type=Counter32
_TnMcLagStatsPktsRxConfig_Object=MibTableColumn
tnMcLagStatsPktsRxConfig=_TnMcLagStatsPktsRxConfig_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,3),_TnMcLagStatsPktsRxConfig_Type())
tnMcLagStatsPktsRxConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsRxConfig.setStatus(_A)
_TnMcLagStatsPktsRxPeerConfig_Type=Counter32
_TnMcLagStatsPktsRxPeerConfig_Object=MibTableColumn
tnMcLagStatsPktsRxPeerConfig=_TnMcLagStatsPktsRxPeerConfig_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,4),_TnMcLagStatsPktsRxPeerConfig_Type())
tnMcLagStatsPktsRxPeerConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsRxPeerConfig.setStatus(_A)
_TnMcLagStatsPktsRxState_Type=Counter32
_TnMcLagStatsPktsRxState_Object=MibTableColumn
tnMcLagStatsPktsRxState=_TnMcLagStatsPktsRxState_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,5),_TnMcLagStatsPktsRxState_Type())
tnMcLagStatsPktsRxState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsRxState.setStatus(_A)
_TnMcLagStatsDropPktKpaliveTask_Type=Counter32
_TnMcLagStatsDropPktKpaliveTask_Object=MibTableColumn
tnMcLagStatsDropPktKpaliveTask=_TnMcLagStatsDropPktKpaliveTask_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,6),_TnMcLagStatsDropPktKpaliveTask_Type())
tnMcLagStatsDropPktKpaliveTask.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropPktKpaliveTask.setStatus(_A)
_TnMcLagStatsDropPktTooShort_Type=Counter32
_TnMcLagStatsDropPktTooShort_Object=MibTableColumn
tnMcLagStatsDropPktTooShort=_TnMcLagStatsDropPktTooShort_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,7),_TnMcLagStatsDropPktTooShort_Type())
tnMcLagStatsDropPktTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropPktTooShort.setStatus(_A)
_TnMcLagStatsDropPktVerifyFaild_Type=Counter32
_TnMcLagStatsDropPktVerifyFaild_Object=MibTableColumn
tnMcLagStatsDropPktVerifyFaild=_TnMcLagStatsDropPktVerifyFaild_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,8),_TnMcLagStatsDropPktVerifyFaild_Type())
tnMcLagStatsDropPktVerifyFaild.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropPktVerifyFaild.setStatus(_A)
_TnMcLagStatsDropTlvInvalidSize_Type=Counter32
_TnMcLagStatsDropTlvInvalidSize_Object=MibTableColumn
tnMcLagStatsDropTlvInvalidSize=_TnMcLagStatsDropTlvInvalidSize_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,9),_TnMcLagStatsDropTlvInvalidSize_Type())
tnMcLagStatsDropTlvInvalidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropTlvInvalidSize.setStatus(_A)
_TnMcLagStatsDropOutOfSeq_Type=Counter32
_TnMcLagStatsDropOutOfSeq_Object=MibTableColumn
tnMcLagStatsDropOutOfSeq=_TnMcLagStatsDropOutOfSeq_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,10),_TnMcLagStatsDropOutOfSeq_Type())
tnMcLagStatsDropOutOfSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropOutOfSeq.setStatus(_A)
_TnMcLagStatsDropUnknownTlv_Type=Counter32
_TnMcLagStatsDropUnknownTlv_Object=MibTableColumn
tnMcLagStatsDropUnknownTlv=_TnMcLagStatsDropUnknownTlv_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,11),_TnMcLagStatsDropUnknownTlv_Type())
tnMcLagStatsDropUnknownTlv.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropUnknownTlv.setStatus(_A)
_TnMcLagStatsDropTlvInvldLagId_Type=Counter32
_TnMcLagStatsDropTlvInvldLagId_Object=MibTableColumn
tnMcLagStatsDropTlvInvldLagId=_TnMcLagStatsDropTlvInvldLagId_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,12),_TnMcLagStatsDropTlvInvldLagId_Type())
tnMcLagStatsDropTlvInvldLagId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropTlvInvldLagId.setStatus(_A)
_TnMcLagStatsDropMD5_Type=Counter32
_TnMcLagStatsDropMD5_Object=MibTableColumn
tnMcLagStatsDropMD5=_TnMcLagStatsDropMD5_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,13),_TnMcLagStatsDropMD5_Type())
tnMcLagStatsDropMD5.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropMD5.setStatus(_A)
_TnMcLagStatsDropUnknownPeer_Type=Counter32
_TnMcLagStatsDropUnknownPeer_Object=MibTableColumn
tnMcLagStatsDropUnknownPeer=_TnMcLagStatsDropUnknownPeer_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,14),_TnMcLagStatsDropUnknownPeer_Type())
tnMcLagStatsDropUnknownPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsDropUnknownPeer.setStatus(_A)
_TnMcLagStatsPktsTx_Type=Counter32
_TnMcLagStatsPktsTx_Object=MibTableColumn
tnMcLagStatsPktsTx=_TnMcLagStatsPktsTx_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,15),_TnMcLagStatsPktsTx_Type())
tnMcLagStatsPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsTx.setStatus(_A)
_TnMcLagStatsPktsTxKeepalive_Type=Counter32
_TnMcLagStatsPktsTxKeepalive_Object=MibTableColumn
tnMcLagStatsPktsTxKeepalive=_TnMcLagStatsPktsTxKeepalive_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,16),_TnMcLagStatsPktsTxKeepalive_Type())
tnMcLagStatsPktsTxKeepalive.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsTxKeepalive.setStatus(_A)
_TnMcLagStatsPktsTxConfig_Type=Counter32
_TnMcLagStatsPktsTxConfig_Object=MibTableColumn
tnMcLagStatsPktsTxConfig=_TnMcLagStatsPktsTxConfig_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,17),_TnMcLagStatsPktsTxConfig_Type())
tnMcLagStatsPktsTxConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsTxConfig.setStatus(_A)
_TnMcLagStatsPktsTxPeerConfig_Type=Counter32
_TnMcLagStatsPktsTxPeerConfig_Object=MibTableColumn
tnMcLagStatsPktsTxPeerConfig=_TnMcLagStatsPktsTxPeerConfig_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,18),_TnMcLagStatsPktsTxPeerConfig_Type())
tnMcLagStatsPktsTxPeerConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsTxPeerConfig.setStatus(_A)
_TnMcLagStatsPktsTxState_Type=Counter32
_TnMcLagStatsPktsTxState_Object=MibTableColumn
tnMcLagStatsPktsTxState=_TnMcLagStatsPktsTxState_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,19),_TnMcLagStatsPktsTxState_Type())
tnMcLagStatsPktsTxState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsTxState.setStatus(_A)
_TnMcLagStatsPktsTxFailed_Type=Counter32
_TnMcLagStatsPktsTxFailed_Object=MibTableColumn
tnMcLagStatsPktsTxFailed=_TnMcLagStatsPktsTxFailed_Object((1,3,6,1,4,1,7483,6,1,2,40,2,20,1,20),_TnMcLagStatsPktsTxFailed_Type())
tnMcLagStatsPktsTxFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagStatsPktsTxFailed.setStatus(_A)
_TnMcLagPeerStatsTable_Object=MibTable
tnMcLagPeerStatsTable=_TnMcLagPeerStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21))
if mibBuilder.loadTexts:tnMcLagPeerStatsTable.setStatus(_A)
_TnMcLagPeerStatsEntry_Object=MibTableRow
tnMcLagPeerStatsEntry=_TnMcLagPeerStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1))
tnMcLagPeerStatsEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:tnMcLagPeerStatsEntry.setStatus(_A)
_TnMcLagPeerStatsPktsRx_Type=Counter32
_TnMcLagPeerStatsPktsRx_Object=MibTableColumn
tnMcLagPeerStatsPktsRx=_TnMcLagPeerStatsPktsRx_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,1),_TnMcLagPeerStatsPktsRx_Type())
tnMcLagPeerStatsPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsRx.setStatus(_A)
_TnMcLagPeerStatsPktsRxKpalive_Type=Counter32
_TnMcLagPeerStatsPktsRxKpalive_Object=MibTableColumn
tnMcLagPeerStatsPktsRxKpalive=_TnMcLagPeerStatsPktsRxKpalive_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,2),_TnMcLagPeerStatsPktsRxKpalive_Type())
tnMcLagPeerStatsPktsRxKpalive.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsRxKpalive.setStatus(_A)
_TnMcLagPeerStatsPktsRxConfig_Type=Counter32
_TnMcLagPeerStatsPktsRxConfig_Object=MibTableColumn
tnMcLagPeerStatsPktsRxConfig=_TnMcLagPeerStatsPktsRxConfig_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,3),_TnMcLagPeerStatsPktsRxConfig_Type())
tnMcLagPeerStatsPktsRxConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsRxConfig.setStatus(_A)
_TnMcLagPeerStatsPktsRxPeerCfg_Type=Counter32
_TnMcLagPeerStatsPktsRxPeerCfg_Object=MibTableColumn
tnMcLagPeerStatsPktsRxPeerCfg=_TnMcLagPeerStatsPktsRxPeerCfg_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,4),_TnMcLagPeerStatsPktsRxPeerCfg_Type())
tnMcLagPeerStatsPktsRxPeerCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsRxPeerCfg.setStatus(_A)
_TnMcLagPeerStatsPktsRxState_Type=Counter32
_TnMcLagPeerStatsPktsRxState_Object=MibTableColumn
tnMcLagPeerStatsPktsRxState=_TnMcLagPeerStatsPktsRxState_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,5),_TnMcLagPeerStatsPktsRxState_Type())
tnMcLagPeerStatsPktsRxState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsRxState.setStatus(_A)
_TnMcLagPeerStatsDropStateDsbld_Type=Counter32
_TnMcLagPeerStatsDropStateDsbld_Object=MibTableColumn
tnMcLagPeerStatsDropStateDsbld=_TnMcLagPeerStatsDropStateDsbld_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,6),_TnMcLagPeerStatsDropStateDsbld_Type())
tnMcLagPeerStatsDropStateDsbld.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsDropStateDsbld.setStatus(_A)
_TnMcLagPeerStatsDropPktTooShrt_Type=Counter32
_TnMcLagPeerStatsDropPktTooShrt_Object=MibTableColumn
tnMcLagPeerStatsDropPktTooShrt=_TnMcLagPeerStatsDropPktTooShrt_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,7),_TnMcLagPeerStatsDropPktTooShrt_Type())
tnMcLagPeerStatsDropPktTooShrt.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsDropPktTooShrt.setStatus(_A)
_TnMcLagPeerStatsDropTlvInvldSz_Type=Counter32
_TnMcLagPeerStatsDropTlvInvldSz_Object=MibTableColumn
tnMcLagPeerStatsDropTlvInvldSz=_TnMcLagPeerStatsDropTlvInvldSz_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,8),_TnMcLagPeerStatsDropTlvInvldSz_Type())
tnMcLagPeerStatsDropTlvInvldSz.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsDropTlvInvldSz.setStatus(_A)
_TnMcLagPeerStatsDropTlvInvldId_Type=Counter32
_TnMcLagPeerStatsDropTlvInvldId_Object=MibTableColumn
tnMcLagPeerStatsDropTlvInvldId=_TnMcLagPeerStatsDropTlvInvldId_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,9),_TnMcLagPeerStatsDropTlvInvldId_Type())
tnMcLagPeerStatsDropTlvInvldId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsDropTlvInvldId.setStatus(_A)
_TnMcLagPeerStatsDropOutOfSeq_Type=Counter32
_TnMcLagPeerStatsDropOutOfSeq_Object=MibTableColumn
tnMcLagPeerStatsDropOutOfSeq=_TnMcLagPeerStatsDropOutOfSeq_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,10),_TnMcLagPeerStatsDropOutOfSeq_Type())
tnMcLagPeerStatsDropOutOfSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsDropOutOfSeq.setStatus(_A)
_TnMcLagPeerStatsDropUnknownTlv_Type=Counter32
_TnMcLagPeerStatsDropUnknownTlv_Object=MibTableColumn
tnMcLagPeerStatsDropUnknownTlv=_TnMcLagPeerStatsDropUnknownTlv_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,11),_TnMcLagPeerStatsDropUnknownTlv_Type())
tnMcLagPeerStatsDropUnknownTlv.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsDropUnknownTlv.setStatus(_A)
_TnMcLagPeerStatsDropMD5_Type=Counter32
_TnMcLagPeerStatsDropMD5_Object=MibTableColumn
tnMcLagPeerStatsDropMD5=_TnMcLagPeerStatsDropMD5_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,12),_TnMcLagPeerStatsDropMD5_Type())
tnMcLagPeerStatsDropMD5.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsDropMD5.setStatus(_A)
_TnMcLagPeerStatsPktsTx_Type=Counter32
_TnMcLagPeerStatsPktsTx_Object=MibTableColumn
tnMcLagPeerStatsPktsTx=_TnMcLagPeerStatsPktsTx_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,13),_TnMcLagPeerStatsPktsTx_Type())
tnMcLagPeerStatsPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsTx.setStatus(_A)
_TnMcLagPeerStatsPktsTxKpalive_Type=Counter32
_TnMcLagPeerStatsPktsTxKpalive_Object=MibTableColumn
tnMcLagPeerStatsPktsTxKpalive=_TnMcLagPeerStatsPktsTxKpalive_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,14),_TnMcLagPeerStatsPktsTxKpalive_Type())
tnMcLagPeerStatsPktsTxKpalive.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsTxKpalive.setStatus(_A)
_TnMcLagPeerStatsPktsTxPeerCfg_Type=Counter32
_TnMcLagPeerStatsPktsTxPeerCfg_Object=MibTableColumn
tnMcLagPeerStatsPktsTxPeerCfg=_TnMcLagPeerStatsPktsTxPeerCfg_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,15),_TnMcLagPeerStatsPktsTxPeerCfg_Type())
tnMcLagPeerStatsPktsTxPeerCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsTxPeerCfg.setStatus(_A)
_TnMcLagPeerStatsPktsTxFailed_Type=Counter32
_TnMcLagPeerStatsPktsTxFailed_Object=MibTableColumn
tnMcLagPeerStatsPktsTxFailed=_TnMcLagPeerStatsPktsTxFailed_Object((1,3,6,1,4,1,7483,6,1,2,40,2,21,1,16),_TnMcLagPeerStatsPktsTxFailed_Type())
tnMcLagPeerStatsPktsTxFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagPeerStatsPktsTxFailed.setStatus(_A)
_TnMcLagLagStatsTable_Object=MibTable
tnMcLagLagStatsTable=_TnMcLagLagStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,40,2,22))
if mibBuilder.loadTexts:tnMcLagLagStatsTable.setStatus(_A)
_TnMcLagLagStatsEntry_Object=MibTableRow
tnMcLagLagStatsEntry=_TnMcLagLagStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,2,22,1))
tnMcLagLagStatsEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H),(0,_C,_V))
if mibBuilder.loadTexts:tnMcLagLagStatsEntry.setStatus(_A)
_TnMcLagLagStatsPktsRxConfig_Type=Counter32
_TnMcLagLagStatsPktsRxConfig_Object=MibTableColumn
tnMcLagLagStatsPktsRxConfig=_TnMcLagLagStatsPktsRxConfig_Object((1,3,6,1,4,1,7483,6,1,2,40,2,22,1,1),_TnMcLagLagStatsPktsRxConfig_Type())
tnMcLagLagStatsPktsRxConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagLagStatsPktsRxConfig.setStatus(_A)
_TnMcLagLagStatsPktsRxState_Type=Counter32
_TnMcLagLagStatsPktsRxState_Object=MibTableColumn
tnMcLagLagStatsPktsRxState=_TnMcLagLagStatsPktsRxState_Object((1,3,6,1,4,1,7483,6,1,2,40,2,22,1,2),_TnMcLagLagStatsPktsRxState_Type())
tnMcLagLagStatsPktsRxState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagLagStatsPktsRxState.setStatus(_A)
_TnMcLagLagStatsPktsTxConfig_Type=Counter32
_TnMcLagLagStatsPktsTxConfig_Object=MibTableColumn
tnMcLagLagStatsPktsTxConfig=_TnMcLagLagStatsPktsTxConfig_Object((1,3,6,1,4,1,7483,6,1,2,40,2,22,1,3),_TnMcLagLagStatsPktsTxConfig_Type())
tnMcLagLagStatsPktsTxConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagLagStatsPktsTxConfig.setStatus(_A)
_TnMcLagLagStatsPktsTxState_Type=Counter32
_TnMcLagLagStatsPktsTxState_Object=MibTableColumn
tnMcLagLagStatsPktsTxState=_TnMcLagLagStatsPktsTxState_Object((1,3,6,1,4,1,7483,6,1,2,40,2,22,1,4),_TnMcLagLagStatsPktsTxState_Type())
tnMcLagLagStatsPktsTxState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagLagStatsPktsTxState.setStatus(_A)
_TnMcLagLagStatsPktsTxFailed_Type=Counter32
_TnMcLagLagStatsPktsTxFailed_Object=MibTableColumn
tnMcLagLagStatsPktsTxFailed=_TnMcLagLagStatsPktsTxFailed_Object((1,3,6,1,4,1,7483,6,1,2,40,2,22,1,5),_TnMcLagLagStatsPktsTxFailed_Type())
tnMcLagLagStatsPktsTxFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcLagLagStatsPktsTxFailed.setStatus(_A)
_TnMcPeerSyncStatsTable_Object=MibTable
tnMcPeerSyncStatsTable=_TnMcPeerSyncStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23))
if mibBuilder.loadTexts:tnMcPeerSyncStatsTable.setStatus(_A)
_TnMcPeerSyncStatsEntry_Object=MibTableRow
tnMcPeerSyncStatsEntry=_TnMcPeerSyncStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1))
tnMcPeerSyncStatsEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:tnMcPeerSyncStatsEntry.setStatus(_A)
_TnMcPeerSyncPktsTxAll_Type=Counter32
_TnMcPeerSyncPktsTxAll_Object=MibTableColumn
tnMcPeerSyncPktsTxAll=_TnMcPeerSyncPktsTxAll_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,1),_TnMcPeerSyncPktsTxAll_Type())
tnMcPeerSyncPktsTxAll.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsTxAll.setStatus(_A)
_TnMcPeerSyncPktsTxHello_Type=Counter32
_TnMcPeerSyncPktsTxHello_Object=MibTableColumn
tnMcPeerSyncPktsTxHello=_TnMcPeerSyncPktsTxHello_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,2),_TnMcPeerSyncPktsTxHello_Type())
tnMcPeerSyncPktsTxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsTxHello.setStatus(_A)
_TnMcPeerSyncPktsTxData_Type=Counter32
_TnMcPeerSyncPktsTxData_Object=MibTableColumn
tnMcPeerSyncPktsTxData=_TnMcPeerSyncPktsTxData_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,3),_TnMcPeerSyncPktsTxData_Type())
tnMcPeerSyncPktsTxData.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsTxData.setStatus(_A)
_TnMcPeerSyncPktsTxOther_Type=Counter32
_TnMcPeerSyncPktsTxOther_Object=MibTableColumn
tnMcPeerSyncPktsTxOther=_TnMcPeerSyncPktsTxOther_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,4),_TnMcPeerSyncPktsTxOther_Type())
tnMcPeerSyncPktsTxOther.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsTxOther.setStatus(_A)
_TnMcPeerSyncPktsTxErr_Type=Counter32
_TnMcPeerSyncPktsTxErr_Object=MibTableColumn
tnMcPeerSyncPktsTxErr=_TnMcPeerSyncPktsTxErr_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,5),_TnMcPeerSyncPktsTxErr_Type())
tnMcPeerSyncPktsTxErr.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsTxErr.setStatus(_A)
_TnMcPeerSyncPktsRxAll_Type=Counter32
_TnMcPeerSyncPktsRxAll_Object=MibTableColumn
tnMcPeerSyncPktsRxAll=_TnMcPeerSyncPktsRxAll_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,6),_TnMcPeerSyncPktsRxAll_Type())
tnMcPeerSyncPktsRxAll.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsRxAll.setStatus(_A)
_TnMcPeerSyncPktsRxHello_Type=Counter32
_TnMcPeerSyncPktsRxHello_Object=MibTableColumn
tnMcPeerSyncPktsRxHello=_TnMcPeerSyncPktsRxHello_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,7),_TnMcPeerSyncPktsRxHello_Type())
tnMcPeerSyncPktsRxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsRxHello.setStatus(_A)
_TnMcPeerSyncPktsRxData_Type=Counter32
_TnMcPeerSyncPktsRxData_Object=MibTableColumn
tnMcPeerSyncPktsRxData=_TnMcPeerSyncPktsRxData_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,8),_TnMcPeerSyncPktsRxData_Type())
tnMcPeerSyncPktsRxData.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsRxData.setStatus(_A)
_TnMcPeerSyncPktsRxOther_Type=Counter32
_TnMcPeerSyncPktsRxOther_Object=MibTableColumn
tnMcPeerSyncPktsRxOther=_TnMcPeerSyncPktsRxOther_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,9),_TnMcPeerSyncPktsRxOther_Type())
tnMcPeerSyncPktsRxOther.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsRxOther.setStatus(_A)
_TnMcPeerSyncPktsRxErr_Type=Counter32
_TnMcPeerSyncPktsRxErr_Object=MibTableColumn
tnMcPeerSyncPktsRxErr=_TnMcPeerSyncPktsRxErr_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,10),_TnMcPeerSyncPktsRxErr_Type())
tnMcPeerSyncPktsRxErr.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsRxErr.setStatus(_A)
_TnMcPeerSyncPktsRxErrHeader_Type=Counter32
_TnMcPeerSyncPktsRxErrHeader_Object=MibTableColumn
tnMcPeerSyncPktsRxErrHeader=_TnMcPeerSyncPktsRxErrHeader_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,11),_TnMcPeerSyncPktsRxErrHeader_Type())
tnMcPeerSyncPktsRxErrHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsRxErrHeader.setStatus(_A)
_TnMcPeerSyncPktsRxErrBody_Type=Counter32
_TnMcPeerSyncPktsRxErrBody_Object=MibTableColumn
tnMcPeerSyncPktsRxErrBody=_TnMcPeerSyncPktsRxErrBody_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,12),_TnMcPeerSyncPktsRxErrBody_Type())
tnMcPeerSyncPktsRxErrBody.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsRxErrBody.setStatus(_A)
_TnMcPeerSyncPktsRxErrSeqNum_Type=Counter32
_TnMcPeerSyncPktsRxErrSeqNum_Object=MibTableColumn
tnMcPeerSyncPktsRxErrSeqNum=_TnMcPeerSyncPktsRxErrSeqNum_Object((1,3,6,1,4,1,7483,6,1,2,40,2,23,1,13),_TnMcPeerSyncPktsRxErrSeqNum_Type())
tnMcPeerSyncPktsRxErrSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcPeerSyncPktsRxErrSeqNum.setStatus(_A)
_TnMcRedundancyStatsScalar1_Type=Unsigned32
_TnMcRedundancyStatsScalar1_Object=MibScalar
tnMcRedundancyStatsScalar1=_TnMcRedundancyStatsScalar1_Object((1,3,6,1,4,1,7483,6,1,2,40,2,101),_TnMcRedundancyStatsScalar1_Type())
tnMcRedundancyStatsScalar1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcRedundancyStatsScalar1.setStatus(_A)
_TnMcRedundancyStatsScalar2_Type=Unsigned32
_TnMcRedundancyStatsScalar2_Object=MibScalar
tnMcRedundancyStatsScalar2=_TnMcRedundancyStatsScalar2_Object((1,3,6,1,4,1,7483,6,1,2,40,2,102),_TnMcRedundancyStatsScalar2_Type())
tnMcRedundancyStatsScalar2.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMcRedundancyStatsScalar2.setStatus(_A)
tnMcLagConfigLagEntry.registerAugmentions((_C,_d))
tnMcLagInfoLagEntry.setIndexNames(*tnMcLagConfigLagEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'TmnxMcsClientApp':TmnxMcsClientApp,'tnMcRedundancyMIBModule':tnMcRedundancyMIBModule,'tnMcRedundancy':tnMcRedundancy,'tnMcRedundancyObjs':tnMcRedundancyObjs,'tnMcPeerTable':tnMcPeerTable,'tnMcPeerEntry':tnMcPeerEntry,_G:tnMcPeerIpType,_H:tnMcPeerIpAddr,'tnMcPeerRowStatus':tnMcPeerRowStatus,'tnMcPeerDescription':tnMcPeerDescription,'tnMcPeerAuthKey':tnMcPeerAuthKey,'tnMcPeerSrcIpType':tnMcPeerSrcIpType,'tnMcPeerSrcIpAddr':tnMcPeerSrcIpAddr,'tnMcPeerAdminState':tnMcPeerAdminState,'tnMcPeerSrcIpOperType':tnMcPeerSrcIpOperType,'tnMcPeerSrcIpOperAddr':tnMcPeerSrcIpOperAddr,'tnMcPeerRingsOperState':tnMcPeerRingsOperState,'tnMcPeerName':tnMcPeerName,'tnMcPeerSyncTable':tnMcPeerSyncTable,'tnMcPeerSyncEntry':tnMcPeerSyncEntry,'tnMcPeerSyncRowStatus':tnMcPeerSyncRowStatus,'tnMcPeerSyncIgmp':tnMcPeerSyncIgmp,'tnMcPeerSyncIgmpSnooping':tnMcPeerSyncIgmpSnooping,'tnMcPeerSyncSubMgmt':tnMcPeerSyncSubMgmt,'tnMcPeerSyncSrrp':tnMcPeerSyncSrrp,'tnMcPeerSyncAdminState':tnMcPeerSyncAdminState,'tnMcPeerSyncOperState':tnMcPeerSyncOperState,'tnMcPeerSyncOperFlags':tnMcPeerSyncOperFlags,'tnMcPeerSyncStatus':tnMcPeerSyncStatus,'tnMcPeerSyncLastSyncTime':tnMcPeerSyncLastSyncTime,'tnMcPeerSyncNumEntries':tnMcPeerSyncNumEntries,'tnMcPeerSyncLclDeletedEntries':tnMcPeerSyncLclDeletedEntries,'tnMcPeerSyncAlarmedEntries':tnMcPeerSyncAlarmedEntries,'tnMcPeerSyncRemNumEntries':tnMcPeerSyncRemNumEntries,'tnMcPeerSyncRemLclDelEntries':tnMcPeerSyncRemLclDelEntries,'tnMcPeerSyncRemAlarmedEntries':tnMcPeerSyncRemAlarmedEntries,'tnMcPeerSyncPortTable':tnMcPeerSyncPortTable,'tnMcPeerSyncPortEntry':tnMcPeerSyncPortEntry,_T:tnMcPeerSyncPortId,'tnMcPeerSyncPortRowStatus':tnMcPeerSyncPortRowStatus,'tnMcPeerSyncPortSyncTag':tnMcPeerSyncPortSyncTag,'tnMcPeerSyncPortEncapRangeTable':tnMcPeerSyncPortEncapRangeTable,'tnMcPeerSyncPortEncapRangeEntry':tnMcPeerSyncPortEncapRangeEntry,_Y:tnMcPeerSyncPortEncapType,_Z:tnMcPeerSyncPortEncapMin,_a:tnMcPeerSyncPortEncapMax,'tnMcPeerSyncPortEncapRowStatus':tnMcPeerSyncPortEncapRowStatus,'tnMcPeerSyncPortEncapSyncTag':tnMcPeerSyncPortEncapSyncTag,'tnMcLagConfigTableLastChanged':tnMcLagConfigTableLastChanged,'tnMcLagConfigTable':tnMcLagConfigTable,'tnMcLagConfigEntry':tnMcLagConfigEntry,'tnMcLagConfigPeerLastChanged':tnMcLagConfigPeerLastChanged,'tnMcLagConfigPeerAdminstate':tnMcLagConfigPeerAdminstate,'tnMcLagConfigKeepALiveIvl':tnMcLagConfigKeepALiveIvl,'tnMcLagConfigHoldOnNgbrFailure':tnMcLagConfigHoldOnNgbrFailure,'tnMcLagConfigOperState':tnMcLagConfigOperState,'tnMcLagConfigPeerLastStateChge':tnMcLagConfigPeerLastStateChge,'tnMcLagConfigLagTableLastChanged':tnMcLagConfigLagTableLastChanged,'tnMcLagConfigLagTable':tnMcLagConfigLagTable,'tnMcLagConfigLagEntry':tnMcLagConfigLagEntry,_V:tnMcLagConfigLagId,'tnMcLagConfigLagLastChanged':tnMcLagConfigLagLastChanged,'tnMcLagConfigLagRowStatus':tnMcLagConfigLagRowStatus,'tnMcLagConfigLaglacpKey':tnMcLagConfigLaglacpKey,'tnMcLagConfigLagSystemId':tnMcLagConfigLagSystemId,'tnMcLagConfigLagSystemPriority':tnMcLagConfigLagSystemPriority,'tnMcLagConfigLagRemoteLagId':tnMcLagConfigLagRemoteLagId,'tnMcLagConfigLagSrcBMacLSB':tnMcLagConfigLagSrcBMacLSB,'tnMcLagConfigLagOperSrcBMacLSB':tnMcLagConfigLagOperSrcBMacLSB,'tnMcLagConfigLagFlushEthRingOnActive':tnMcLagConfigLagFlushEthRingOnActive,'tnMcLagInfoLagTable':tnMcLagInfoLagTable,_d:tnMcLagInfoLagEntry,'tnMcLagActiveStandby':tnMcLagActiveStandby,'tnMcLagLacpIdInUse':tnMcLagLacpIdInUse,'tnMcLagExtendedTimeOut':tnMcLagExtendedTimeOut,'tnMcLagSelectionLogic':tnMcLagSelectionLogic,'tnMcLagConfigMismatchString':tnMcLagConfigMismatchString,'tnMcLagConfigMismatchFlags':tnMcLagConfigMismatchFlags,'tnMcsClientAppTable':tnMcsClientAppTable,'tnMcsClientAppEntry':tnMcsClientAppEntry,_b:tnMcsClientApplication,'tnMcsClientNumEntries':tnMcsClientNumEntries,'tnMcsClientLclDeletedEntries':tnMcsClientLclDeletedEntries,'tnMcsClientAlarmedEntries':tnMcsClientAlarmedEntries,'tnMcsClientRemNumEntries':tnMcsClientRemNumEntries,'tnMcsClientRemLclDelEntries':tnMcsClientRemLclDelEntries,'tnMcsClientRemAlarmedEntries':tnMcsClientRemAlarmedEntries,'tnMcDomainTable':tnMcDomainTable,'tnMcDomainEntry':tnMcDomainEntry,_c:tnMcDomainId,'tnMcDomainRowStatus':tnMcDomainRowStatus,'tnMcDomainDescription':tnMcDomainDescription,'tnMcDomainSrcIpType':tnMcDomainSrcIpType,'tnMcDomainSrcIpAddr':tnMcDomainSrcIpAddr,'tnMcDomainSrcIpMask':tnMcDomainSrcIpMask,'tnMcDomainSvcName':tnMcDomainSvcName,'tnMcRedundancyStatsObjs':tnMcRedundancyStatsObjs,'tnMcLagGlobalStatsTable':tnMcLagGlobalStatsTable,'tnMcLagGlobalStatsEntry':tnMcLagGlobalStatsEntry,'tnMcLagStatsPktsRx':tnMcLagStatsPktsRx,'tnMcLagStatsPktsRxKeepalive':tnMcLagStatsPktsRxKeepalive,'tnMcLagStatsPktsRxConfig':tnMcLagStatsPktsRxConfig,'tnMcLagStatsPktsRxPeerConfig':tnMcLagStatsPktsRxPeerConfig,'tnMcLagStatsPktsRxState':tnMcLagStatsPktsRxState,'tnMcLagStatsDropPktKpaliveTask':tnMcLagStatsDropPktKpaliveTask,'tnMcLagStatsDropPktTooShort':tnMcLagStatsDropPktTooShort,'tnMcLagStatsDropPktVerifyFaild':tnMcLagStatsDropPktVerifyFaild,'tnMcLagStatsDropTlvInvalidSize':tnMcLagStatsDropTlvInvalidSize,'tnMcLagStatsDropOutOfSeq':tnMcLagStatsDropOutOfSeq,'tnMcLagStatsDropUnknownTlv':tnMcLagStatsDropUnknownTlv,'tnMcLagStatsDropTlvInvldLagId':tnMcLagStatsDropTlvInvldLagId,'tnMcLagStatsDropMD5':tnMcLagStatsDropMD5,'tnMcLagStatsDropUnknownPeer':tnMcLagStatsDropUnknownPeer,'tnMcLagStatsPktsTx':tnMcLagStatsPktsTx,'tnMcLagStatsPktsTxKeepalive':tnMcLagStatsPktsTxKeepalive,'tnMcLagStatsPktsTxConfig':tnMcLagStatsPktsTxConfig,'tnMcLagStatsPktsTxPeerConfig':tnMcLagStatsPktsTxPeerConfig,'tnMcLagStatsPktsTxState':tnMcLagStatsPktsTxState,'tnMcLagStatsPktsTxFailed':tnMcLagStatsPktsTxFailed,'tnMcLagPeerStatsTable':tnMcLagPeerStatsTable,'tnMcLagPeerStatsEntry':tnMcLagPeerStatsEntry,'tnMcLagPeerStatsPktsRx':tnMcLagPeerStatsPktsRx,'tnMcLagPeerStatsPktsRxKpalive':tnMcLagPeerStatsPktsRxKpalive,'tnMcLagPeerStatsPktsRxConfig':tnMcLagPeerStatsPktsRxConfig,'tnMcLagPeerStatsPktsRxPeerCfg':tnMcLagPeerStatsPktsRxPeerCfg,'tnMcLagPeerStatsPktsRxState':tnMcLagPeerStatsPktsRxState,'tnMcLagPeerStatsDropStateDsbld':tnMcLagPeerStatsDropStateDsbld,'tnMcLagPeerStatsDropPktTooShrt':tnMcLagPeerStatsDropPktTooShrt,'tnMcLagPeerStatsDropTlvInvldSz':tnMcLagPeerStatsDropTlvInvldSz,'tnMcLagPeerStatsDropTlvInvldId':tnMcLagPeerStatsDropTlvInvldId,'tnMcLagPeerStatsDropOutOfSeq':tnMcLagPeerStatsDropOutOfSeq,'tnMcLagPeerStatsDropUnknownTlv':tnMcLagPeerStatsDropUnknownTlv,'tnMcLagPeerStatsDropMD5':tnMcLagPeerStatsDropMD5,'tnMcLagPeerStatsPktsTx':tnMcLagPeerStatsPktsTx,'tnMcLagPeerStatsPktsTxKpalive':tnMcLagPeerStatsPktsTxKpalive,'tnMcLagPeerStatsPktsTxPeerCfg':tnMcLagPeerStatsPktsTxPeerCfg,'tnMcLagPeerStatsPktsTxFailed':tnMcLagPeerStatsPktsTxFailed,'tnMcLagLagStatsTable':tnMcLagLagStatsTable,'tnMcLagLagStatsEntry':tnMcLagLagStatsEntry,'tnMcLagLagStatsPktsRxConfig':tnMcLagLagStatsPktsRxConfig,'tnMcLagLagStatsPktsRxState':tnMcLagLagStatsPktsRxState,'tnMcLagLagStatsPktsTxConfig':tnMcLagLagStatsPktsTxConfig,'tnMcLagLagStatsPktsTxState':tnMcLagLagStatsPktsTxState,'tnMcLagLagStatsPktsTxFailed':tnMcLagLagStatsPktsTxFailed,'tnMcPeerSyncStatsTable':tnMcPeerSyncStatsTable,'tnMcPeerSyncStatsEntry':tnMcPeerSyncStatsEntry,'tnMcPeerSyncPktsTxAll':tnMcPeerSyncPktsTxAll,'tnMcPeerSyncPktsTxHello':tnMcPeerSyncPktsTxHello,'tnMcPeerSyncPktsTxData':tnMcPeerSyncPktsTxData,'tnMcPeerSyncPktsTxOther':tnMcPeerSyncPktsTxOther,'tnMcPeerSyncPktsTxErr':tnMcPeerSyncPktsTxErr,'tnMcPeerSyncPktsRxAll':tnMcPeerSyncPktsRxAll,'tnMcPeerSyncPktsRxHello':tnMcPeerSyncPktsRxHello,'tnMcPeerSyncPktsRxData':tnMcPeerSyncPktsRxData,'tnMcPeerSyncPktsRxOther':tnMcPeerSyncPktsRxOther,'tnMcPeerSyncPktsRxErr':tnMcPeerSyncPktsRxErr,'tnMcPeerSyncPktsRxErrHeader':tnMcPeerSyncPktsRxErrHeader,'tnMcPeerSyncPktsRxErrBody':tnMcPeerSyncPktsRxErrBody,'tnMcPeerSyncPktsRxErrSeqNum':tnMcPeerSyncPktsRxErrSeqNum,'tnMcRedundancyStatsScalar1':tnMcRedundancyStatsScalar1,'tnMcRedundancyStatsScalar2':tnMcRedundancyStatsScalar2})