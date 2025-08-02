_P='rlFipActiveFcoeTunnelSid'
_O='rlFipActiveFcoeTunnelDstMac'
_N='rlFipActiveFcoeTunnelSrcMac'
_M='rlFipActiveFcoeTunnelPort'
_L='rlFipStaticFcoeTunnelDstMac'
_K='rlFipStaticFcoeTunnelSrcMac'
_J='rlFipStaticFcoeTunnelPort'
_I='rlFipGlobalFcfListMac'
_H='RlFipIfType'
_G='rlFipIfIndex'
_F='OctetString'
_E='read-create'
_D='read-write'
_C='not-accessible'
_B='MARVELL-FIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlFip=ModuleIdentity((1,3,6,1,4,1,89,205))
if mibBuilder.loadTexts:rlFip.setRevisions(('2007-11-07 00:00',))
class RlFipIfType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('non-snooping',1),('non-fcoe',2),('fcoe',3),('enode',4)))
_RlFipIfTable_Object=MibTable
rlFipIfTable=_RlFipIfTable_Object((1,3,6,1,4,1,89,205,1))
if mibBuilder.loadTexts:rlFipIfTable.setStatus(_A)
_RlFipIfEntry_Object=MibTableRow
rlFipIfEntry=_RlFipIfEntry_Object((1,3,6,1,4,1,89,205,1,1))
rlFipIfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:rlFipIfEntry.setStatus(_A)
_RlFipIfIndex_Type=Integer32
_RlFipIfIndex_Object=MibTableColumn
rlFipIfIndex=_RlFipIfIndex_Object((1,3,6,1,4,1,89,205,1,1,1),_RlFipIfIndex_Type())
rlFipIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipIfIndex.setStatus(_A)
class _RlFipIfType_Type(RlFipIfType):defaultValue=4
_RlFipIfType_Type.__name__=_H
_RlFipIfType_Object=MibTableColumn
rlFipIfType=_RlFipIfType_Object((1,3,6,1,4,1,89,205,1,1,2),_RlFipIfType_Type())
rlFipIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlFipIfType.setStatus(_A)
_RlFipIfRowStatus_Type=RowStatus
_RlFipIfRowStatus_Object=MibTableColumn
rlFipIfRowStatus=_RlFipIfRowStatus_Object((1,3,6,1,4,1,89,205,1,1,3),_RlFipIfRowStatus_Type())
rlFipIfRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rlFipIfRowStatus.setStatus(_A)
_RlFipGlobalFcfListTable_Object=MibTable
rlFipGlobalFcfListTable=_RlFipGlobalFcfListTable_Object((1,3,6,1,4,1,89,205,2))
if mibBuilder.loadTexts:rlFipGlobalFcfListTable.setStatus(_A)
_RlFipGlobalFcfListEntry_Object=MibTableRow
rlFipGlobalFcfListEntry=_RlFipGlobalFcfListEntry_Object((1,3,6,1,4,1,89,205,2,1))
rlFipGlobalFcfListEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:rlFipGlobalFcfListEntry.setStatus(_A)
_RlFipGlobalFcfListMac_Type=MacAddress
_RlFipGlobalFcfListMac_Object=MibTableColumn
rlFipGlobalFcfListMac=_RlFipGlobalFcfListMac_Object((1,3,6,1,4,1,89,205,2,1,1),_RlFipGlobalFcfListMac_Type())
rlFipGlobalFcfListMac.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipGlobalFcfListMac.setStatus(_A)
_RlFipGlobalFcfListStatus_Type=RowStatus
_RlFipGlobalFcfListStatus_Object=MibTableColumn
rlFipGlobalFcfListStatus=_RlFipGlobalFcfListStatus_Object((1,3,6,1,4,1,89,205,2,1,2),_RlFipGlobalFcfListStatus_Type())
rlFipGlobalFcfListStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rlFipGlobalFcfListStatus.setStatus(_A)
_RlFipStaticFcoeTunnelTable_Object=MibTable
rlFipStaticFcoeTunnelTable=_RlFipStaticFcoeTunnelTable_Object((1,3,6,1,4,1,89,205,3))
if mibBuilder.loadTexts:rlFipStaticFcoeTunnelTable.setStatus(_A)
_RlFipStaticFcoeTunnelEntry_Object=MibTableRow
rlFipStaticFcoeTunnelEntry=_RlFipStaticFcoeTunnelEntry_Object((1,3,6,1,4,1,89,205,3,1))
rlFipStaticFcoeTunnelEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:rlFipStaticFcoeTunnelEntry.setStatus(_A)
_RlFipStaticFcoeTunnelPort_Type=Integer32
_RlFipStaticFcoeTunnelPort_Object=MibTableColumn
rlFipStaticFcoeTunnelPort=_RlFipStaticFcoeTunnelPort_Object((1,3,6,1,4,1,89,205,3,1,1),_RlFipStaticFcoeTunnelPort_Type())
rlFipStaticFcoeTunnelPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipStaticFcoeTunnelPort.setStatus(_A)
_RlFipStaticFcoeTunnelSrcMac_Type=MacAddress
_RlFipStaticFcoeTunnelSrcMac_Object=MibTableColumn
rlFipStaticFcoeTunnelSrcMac=_RlFipStaticFcoeTunnelSrcMac_Object((1,3,6,1,4,1,89,205,3,1,2),_RlFipStaticFcoeTunnelSrcMac_Type())
rlFipStaticFcoeTunnelSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipStaticFcoeTunnelSrcMac.setStatus(_A)
_RlFipStaticFcoeTunnelDstMac_Type=MacAddress
_RlFipStaticFcoeTunnelDstMac_Object=MibTableColumn
rlFipStaticFcoeTunnelDstMac=_RlFipStaticFcoeTunnelDstMac_Object((1,3,6,1,4,1,89,205,3,1,3),_RlFipStaticFcoeTunnelDstMac_Type())
rlFipStaticFcoeTunnelDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipStaticFcoeTunnelDstMac.setStatus(_A)
_RlFipStaticFcoeTunnelStatus_Type=RowStatus
_RlFipStaticFcoeTunnelStatus_Object=MibTableColumn
rlFipStaticFcoeTunnelStatus=_RlFipStaticFcoeTunnelStatus_Object((1,3,6,1,4,1,89,205,3,1,4),_RlFipStaticFcoeTunnelStatus_Type())
rlFipStaticFcoeTunnelStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rlFipStaticFcoeTunnelStatus.setStatus(_A)
_RlFipActiveFcoeTunnelTable_Object=MibTable
rlFipActiveFcoeTunnelTable=_RlFipActiveFcoeTunnelTable_Object((1,3,6,1,4,1,89,205,4))
if mibBuilder.loadTexts:rlFipActiveFcoeTunnelTable.setStatus(_A)
_RlFipActiveFcoeTunnelEntry_Object=MibTableRow
rlFipActiveFcoeTunnelEntry=_RlFipActiveFcoeTunnelEntry_Object((1,3,6,1,4,1,89,205,4,1))
rlFipActiveFcoeTunnelEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:rlFipActiveFcoeTunnelEntry.setStatus(_A)
_RlFipActiveFcoeTunnelPort_Type=Integer32
_RlFipActiveFcoeTunnelPort_Object=MibTableColumn
rlFipActiveFcoeTunnelPort=_RlFipActiveFcoeTunnelPort_Object((1,3,6,1,4,1,89,205,4,1,1),_RlFipActiveFcoeTunnelPort_Type())
rlFipActiveFcoeTunnelPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipActiveFcoeTunnelPort.setStatus(_A)
_RlFipActiveFcoeTunnelSrcMac_Type=MacAddress
_RlFipActiveFcoeTunnelSrcMac_Object=MibTableColumn
rlFipActiveFcoeTunnelSrcMac=_RlFipActiveFcoeTunnelSrcMac_Object((1,3,6,1,4,1,89,205,4,1,2),_RlFipActiveFcoeTunnelSrcMac_Type())
rlFipActiveFcoeTunnelSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipActiveFcoeTunnelSrcMac.setStatus(_A)
_RlFipActiveFcoeTunnelDstMac_Type=MacAddress
_RlFipActiveFcoeTunnelDstMac_Object=MibTableColumn
rlFipActiveFcoeTunnelDstMac=_RlFipActiveFcoeTunnelDstMac_Object((1,3,6,1,4,1,89,205,4,1,3),_RlFipActiveFcoeTunnelDstMac_Type())
rlFipActiveFcoeTunnelDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipActiveFcoeTunnelDstMac.setStatus(_A)
class _RlFipActiveFcoeTunnelSid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_RlFipActiveFcoeTunnelSid_Type.__name__=_F
_RlFipActiveFcoeTunnelSid_Object=MibTableColumn
rlFipActiveFcoeTunnelSid=_RlFipActiveFcoeTunnelSid_Object((1,3,6,1,4,1,89,205,4,1,4),_RlFipActiveFcoeTunnelSid_Type())
rlFipActiveFcoeTunnelSid.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFipActiveFcoeTunnelSid.setStatus(_A)
_RlFipActiveFcoeTunnelStatus_Type=RowStatus
_RlFipActiveFcoeTunnelStatus_Object=MibTableColumn
rlFipActiveFcoeTunnelStatus=_RlFipActiveFcoeTunnelStatus_Object((1,3,6,1,4,1,89,205,4,1,5),_RlFipActiveFcoeTunnelStatus_Type())
rlFipActiveFcoeTunnelStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rlFipActiveFcoeTunnelStatus.setStatus(_A)
_RlFipEnableScalar_Type=TruthValue
_RlFipEnableScalar_Object=MibScalar
rlFipEnableScalar=_RlFipEnableScalar_Object((1,3,6,1,4,1,89,205,5),_RlFipEnableScalar_Type())
rlFipEnableScalar.setMaxAccess(_D)
if mibBuilder.loadTexts:rlFipEnableScalar.setStatus(_A)
_RlFipClearDynamicEntiesScalar_Type=Integer32
_RlFipClearDynamicEntiesScalar_Object=MibScalar
rlFipClearDynamicEntiesScalar=_RlFipClearDynamicEntiesScalar_Object((1,3,6,1,4,1,89,205,6),_RlFipClearDynamicEntiesScalar_Type())
rlFipClearDynamicEntiesScalar.setMaxAccess(_D)
if mibBuilder.loadTexts:rlFipClearDynamicEntiesScalar.setStatus(_A)
_RlFipGlobalFcfFilteringEnableScalar_Type=TruthValue
_RlFipGlobalFcfFilteringEnableScalar_Object=MibScalar
rlFipGlobalFcfFilteringEnableScalar=_RlFipGlobalFcfFilteringEnableScalar_Object((1,3,6,1,4,1,89,205,7),_RlFipGlobalFcfFilteringEnableScalar_Type())
rlFipGlobalFcfFilteringEnableScalar.setMaxAccess(_D)
if mibBuilder.loadTexts:rlFipGlobalFcfFilteringEnableScalar.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:RlFipIfType,'rlFip':rlFip,'rlFipIfTable':rlFipIfTable,'rlFipIfEntry':rlFipIfEntry,_G:rlFipIfIndex,'rlFipIfType':rlFipIfType,'rlFipIfRowStatus':rlFipIfRowStatus,'rlFipGlobalFcfListTable':rlFipGlobalFcfListTable,'rlFipGlobalFcfListEntry':rlFipGlobalFcfListEntry,_I:rlFipGlobalFcfListMac,'rlFipGlobalFcfListStatus':rlFipGlobalFcfListStatus,'rlFipStaticFcoeTunnelTable':rlFipStaticFcoeTunnelTable,'rlFipStaticFcoeTunnelEntry':rlFipStaticFcoeTunnelEntry,_J:rlFipStaticFcoeTunnelPort,_K:rlFipStaticFcoeTunnelSrcMac,_L:rlFipStaticFcoeTunnelDstMac,'rlFipStaticFcoeTunnelStatus':rlFipStaticFcoeTunnelStatus,'rlFipActiveFcoeTunnelTable':rlFipActiveFcoeTunnelTable,'rlFipActiveFcoeTunnelEntry':rlFipActiveFcoeTunnelEntry,_M:rlFipActiveFcoeTunnelPort,_N:rlFipActiveFcoeTunnelSrcMac,_O:rlFipActiveFcoeTunnelDstMac,_P:rlFipActiveFcoeTunnelSid,'rlFipActiveFcoeTunnelStatus':rlFipActiveFcoeTunnelStatus,'rlFipEnableScalar':rlFipEnableScalar,'rlFipClearDynamicEntiesScalar':rlFipClearDynamicEntiesScalar,'rlFipGlobalFcfFilteringEnableScalar':rlFipGlobalFcfFilteringEnableScalar})