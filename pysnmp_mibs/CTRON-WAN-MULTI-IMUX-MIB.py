_M='ctWanMMuxChannelId'
_L='ctWanMMuxChannelGroupId'
_K='ctWanMMuxChannelMMuxId'
_J='ctWanMMuxGroupId'
_I='ctWanMMuxGroupMMuxId'
_H='enabled'
_G='disabled'
_F='ctWanMMuxId'
_E='read-write'
_D='CTRON-WAN-MULTI-IMUX-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctWanServices,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctWanServices')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtWanMultiMux_ObjectIdentity=ObjectIdentity
ctWanMultiMux=_CtWanMultiMux_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,3,2))
_CtWANMMuxGeneralGroup_ObjectIdentity=ObjectIdentity
ctWANMMuxGeneralGroup=_CtWANMMuxGeneralGroup_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,3,2,1))
_CtWANMMuxMaxNum_Type=Integer32
_CtWANMMuxMaxNum_Object=MibScalar
ctWANMMuxMaxNum=_CtWANMMuxMaxNum_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,1,1),_CtWANMMuxMaxNum_Type())
ctWANMMuxMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWANMMuxMaxNum.setStatus(_A)
_CtWanMMuxTable_Object=MibTable
ctWanMMuxTable=_CtWanMMuxTable_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,2))
if mibBuilder.loadTexts:ctWanMMuxTable.setStatus(_A)
_CtWanMMuxEntry_Object=MibTableRow
ctWanMMuxEntry=_CtWanMMuxEntry_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,2,1))
ctWanMMuxEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:ctWanMMuxEntry.setStatus(_A)
class _CtWanMMuxId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMMuxId_Type.__name__=_C
_CtWanMMuxId_Object=MibTableColumn
ctWanMMuxId=_CtWanMMuxId_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,2,1,1),_CtWanMMuxId_Type())
ctWanMMuxId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxId.setStatus(_A)
class _CtWanMMuxIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMMuxIfIndex_Type.__name__=_C
_CtWanMMuxIfIndex_Object=MibTableColumn
ctWanMMuxIfIndex=_CtWanMMuxIfIndex_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,2,1,2),_CtWanMMuxIfIndex_Type())
ctWanMMuxIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxIfIndex.setStatus(_A)
_CtWanMMuxMaxNumGroups_Type=Integer32
_CtWanMMuxMaxNumGroups_Object=MibTableColumn
ctWanMMuxMaxNumGroups=_CtWanMMuxMaxNumGroups_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,2,1,3),_CtWanMMuxMaxNumGroups_Type())
ctWanMMuxMaxNumGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxMaxNumGroups.setStatus(_A)
class _CtWanMMuxAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtWanMMuxAdmin_Type.__name__=_C
_CtWanMMuxAdmin_Object=MibTableColumn
ctWanMMuxAdmin=_CtWanMMuxAdmin_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,2,1,4),_CtWanMMuxAdmin_Type())
ctWanMMuxAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:ctWanMMuxAdmin.setStatus(_A)
_CtWanMMuxGroupTable_Object=MibTable
ctWanMMuxGroupTable=_CtWanMMuxGroupTable_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,3))
if mibBuilder.loadTexts:ctWanMMuxGroupTable.setStatus(_A)
_CtWanMMuxGroupEntry_Object=MibTableRow
ctWanMMuxGroupEntry=_CtWanMMuxGroupEntry_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,3,1))
ctWanMMuxGroupEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:ctWanMMuxGroupEntry.setStatus(_A)
class _CtWanMMuxGroupMMuxId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMMuxGroupMMuxId_Type.__name__=_C
_CtWanMMuxGroupMMuxId_Object=MibTableColumn
ctWanMMuxGroupMMuxId=_CtWanMMuxGroupMMuxId_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,3,1,1),_CtWanMMuxGroupMMuxId_Type())
ctWanMMuxGroupMMuxId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxGroupMMuxId.setStatus(_A)
class _CtWanMMuxGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMMuxGroupId_Type.__name__=_C
_CtWanMMuxGroupId_Object=MibTableColumn
ctWanMMuxGroupId=_CtWanMMuxGroupId_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,3,1,2),_CtWanMMuxGroupId_Type())
ctWanMMuxGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxGroupId.setStatus(_A)
class _CtWanMMuxGroupAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtWanMMuxGroupAdmin_Type.__name__=_C
_CtWanMMuxGroupAdmin_Object=MibTableColumn
ctWanMMuxGroupAdmin=_CtWanMMuxGroupAdmin_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,3,1,3),_CtWanMMuxGroupAdmin_Type())
ctWanMMuxGroupAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:ctWanMMuxGroupAdmin.setStatus(_A)
_CtWanMMuxGroupNumChannels_Type=Integer32
_CtWanMMuxGroupNumChannels_Object=MibTableColumn
ctWanMMuxGroupNumChannels=_CtWanMMuxGroupNumChannels_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,3,1,4),_CtWanMMuxGroupNumChannels_Type())
ctWanMMuxGroupNumChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxGroupNumChannels.setStatus(_A)
_CtWanMMuxGroupAddChannel_Type=Integer32
_CtWanMMuxGroupAddChannel_Object=MibTableColumn
ctWanMMuxGroupAddChannel=_CtWanMMuxGroupAddChannel_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,3,1,5),_CtWanMMuxGroupAddChannel_Type())
ctWanMMuxGroupAddChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:ctWanMMuxGroupAddChannel.setStatus(_A)
_CtWanMMuxGroupDelChannel_Type=Integer32
_CtWanMMuxGroupDelChannel_Object=MibTableColumn
ctWanMMuxGroupDelChannel=_CtWanMMuxGroupDelChannel_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,3,1,6),_CtWanMMuxGroupDelChannel_Type())
ctWanMMuxGroupDelChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:ctWanMMuxGroupDelChannel.setStatus(_A)
_CtWanMMuxChannelTable_Object=MibTable
ctWanMMuxChannelTable=_CtWanMMuxChannelTable_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4))
if mibBuilder.loadTexts:ctWanMMuxChannelTable.setStatus(_A)
_CtWanMMuxChannelEntry_Object=MibTableRow
ctWanMMuxChannelEntry=_CtWanMMuxChannelEntry_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1))
ctWanMMuxChannelEntry.setIndexNames((0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:ctWanMMuxChannelEntry.setStatus(_A)
class _CtWanMMuxChannelMMuxId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMMuxChannelMMuxId_Type.__name__=_C
_CtWanMMuxChannelMMuxId_Object=MibTableColumn
ctWanMMuxChannelMMuxId=_CtWanMMuxChannelMMuxId_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1,1),_CtWanMMuxChannelMMuxId_Type())
ctWanMMuxChannelMMuxId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxChannelMMuxId.setStatus(_A)
class _CtWanMMuxChannelGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMMuxChannelGroupId_Type.__name__=_C
_CtWanMMuxChannelGroupId_Object=MibTableColumn
ctWanMMuxChannelGroupId=_CtWanMMuxChannelGroupId_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1,2),_CtWanMMuxChannelGroupId_Type())
ctWanMMuxChannelGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxChannelGroupId.setStatus(_A)
class _CtWanMMuxChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMMuxChannelId_Type.__name__=_C
_CtWanMMuxChannelId_Object=MibTableColumn
ctWanMMuxChannelId=_CtWanMMuxChannelId_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1,3),_CtWanMMuxChannelId_Type())
ctWanMMuxChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxChannelId.setStatus(_A)
_CtWanMMuxChannelIfIndex_Type=Integer32
_CtWanMMuxChannelIfIndex_Object=MibTableColumn
ctWanMMuxChannelIfIndex=_CtWanMMuxChannelIfIndex_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1,4),_CtWanMMuxChannelIfIndex_Type())
ctWanMMuxChannelIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxChannelIfIndex.setStatus(_A)
_CtWanMMuxChannelPhysNum_Type=Integer32
_CtWanMMuxChannelPhysNum_Object=MibTableColumn
ctWanMMuxChannelPhysNum=_CtWanMMuxChannelPhysNum_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1,5),_CtWanMMuxChannelPhysNum_Type())
ctWanMMuxChannelPhysNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxChannelPhysNum.setStatus(_A)
_CtWanMMuxChannelBwAvail_Type=Integer32
_CtWanMMuxChannelBwAvail_Object=MibTableColumn
ctWanMMuxChannelBwAvail=_CtWanMMuxChannelBwAvail_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1,6),_CtWanMMuxChannelBwAvail_Type())
ctWanMMuxChannelBwAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxChannelBwAvail.setStatus(_A)
_CtWanMMuxChannelByteCount_Type=Integer32
_CtWanMMuxChannelByteCount_Object=MibTableColumn
ctWanMMuxChannelByteCount=_CtWanMMuxChannelByteCount_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1,7),_CtWanMMuxChannelByteCount_Type())
ctWanMMuxChannelByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxChannelByteCount.setStatus(_A)
class _CtWanMMuxChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_CtWanMMuxChannelStatus_Type.__name__=_C
_CtWanMMuxChannelStatus_Object=MibTableColumn
ctWanMMuxChannelStatus=_CtWanMMuxChannelStatus_Object((1,3,6,1,4,1,52,4,1,2,7,3,2,4,1,8),_CtWanMMuxChannelStatus_Type())
ctWanMMuxChannelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMMuxChannelStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ctWanMultiMux':ctWanMultiMux,'ctWANMMuxGeneralGroup':ctWANMMuxGeneralGroup,'ctWANMMuxMaxNum':ctWANMMuxMaxNum,'ctWanMMuxTable':ctWanMMuxTable,'ctWanMMuxEntry':ctWanMMuxEntry,_F:ctWanMMuxId,'ctWanMMuxIfIndex':ctWanMMuxIfIndex,'ctWanMMuxMaxNumGroups':ctWanMMuxMaxNumGroups,'ctWanMMuxAdmin':ctWanMMuxAdmin,'ctWanMMuxGroupTable':ctWanMMuxGroupTable,'ctWanMMuxGroupEntry':ctWanMMuxGroupEntry,_I:ctWanMMuxGroupMMuxId,_J:ctWanMMuxGroupId,'ctWanMMuxGroupAdmin':ctWanMMuxGroupAdmin,'ctWanMMuxGroupNumChannels':ctWanMMuxGroupNumChannels,'ctWanMMuxGroupAddChannel':ctWanMMuxGroupAddChannel,'ctWanMMuxGroupDelChannel':ctWanMMuxGroupDelChannel,'ctWanMMuxChannelTable':ctWanMMuxChannelTable,'ctWanMMuxChannelEntry':ctWanMMuxChannelEntry,_K:ctWanMMuxChannelMMuxId,_L:ctWanMMuxChannelGroupId,_M:ctWanMMuxChannelId,'ctWanMMuxChannelIfIndex':ctWanMMuxChannelIfIndex,'ctWanMMuxChannelPhysNum':ctWanMMuxChannelPhysNum,'ctWanMMuxChannelBwAvail':ctWanMMuxChannelBwAvail,'ctWanMMuxChannelByteCount':ctWanMMuxChannelByteCount,'ctWanMMuxChannelStatus':ctWanMMuxChannelStatus})