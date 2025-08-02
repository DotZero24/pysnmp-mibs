_J='ctWanMuxChannelId'
_I='ctWanMuxChannelGroupId'
_H='ctWanMuxGroupId'
_G='enabled'
_F='disabled'
_E='CTRON-WAN-IMUX-MIB'
_D='read-write'
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
_CtWanMux_ObjectIdentity=ObjectIdentity
ctWanMux=_CtWanMux_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,3,1))
_CtWANMuxGeneralGroup_ObjectIdentity=ObjectIdentity
ctWANMuxGeneralGroup=_CtWANMuxGeneralGroup_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,3,1,1))
_CtWANMuxMaxNumGroups_Type=Integer32
_CtWANMuxMaxNumGroups_Object=MibScalar
ctWANMuxMaxNumGroups=_CtWANMuxMaxNumGroups_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,1,1),_CtWANMuxMaxNumGroups_Type())
ctWANMuxMaxNumGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWANMuxMaxNumGroups.setStatus(_A)
class _CtWanMuxAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtWanMuxAdmin_Type.__name__=_C
_CtWanMuxAdmin_Object=MibScalar
ctWanMuxAdmin=_CtWanMuxAdmin_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,1,2),_CtWanMuxAdmin_Type())
ctWanMuxAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:ctWanMuxAdmin.setStatus(_A)
_CtWanMuxGroupTable_Object=MibTable
ctWanMuxGroupTable=_CtWanMuxGroupTable_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,2))
if mibBuilder.loadTexts:ctWanMuxGroupTable.setStatus(_A)
_CtWanMuxGroupEntry_Object=MibTableRow
ctWanMuxGroupEntry=_CtWanMuxGroupEntry_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,2,1))
ctWanMuxGroupEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ctWanMuxGroupEntry.setStatus(_A)
class _CtWanMuxGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMuxGroupId_Type.__name__=_C
_CtWanMuxGroupId_Object=MibTableColumn
ctWanMuxGroupId=_CtWanMuxGroupId_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,2,1,1),_CtWanMuxGroupId_Type())
ctWanMuxGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxGroupId.setStatus(_A)
class _CtWanMuxGroupAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtWanMuxGroupAdmin_Type.__name__=_C
_CtWanMuxGroupAdmin_Object=MibTableColumn
ctWanMuxGroupAdmin=_CtWanMuxGroupAdmin_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,2,1,2),_CtWanMuxGroupAdmin_Type())
ctWanMuxGroupAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:ctWanMuxGroupAdmin.setStatus(_A)
_CtWanMuxGroupNumChannels_Type=Integer32
_CtWanMuxGroupNumChannels_Object=MibTableColumn
ctWanMuxGroupNumChannels=_CtWanMuxGroupNumChannels_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,2,1,3),_CtWanMuxGroupNumChannels_Type())
ctWanMuxGroupNumChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxGroupNumChannels.setStatus(_A)
_CtWanMuxGroupAddChannel_Type=Integer32
_CtWanMuxGroupAddChannel_Object=MibTableColumn
ctWanMuxGroupAddChannel=_CtWanMuxGroupAddChannel_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,2,1,4),_CtWanMuxGroupAddChannel_Type())
ctWanMuxGroupAddChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:ctWanMuxGroupAddChannel.setStatus(_A)
_CtWanMuxGroupDelChannel_Type=Integer32
_CtWanMuxGroupDelChannel_Object=MibTableColumn
ctWanMuxGroupDelChannel=_CtWanMuxGroupDelChannel_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,2,1,5),_CtWanMuxGroupDelChannel_Type())
ctWanMuxGroupDelChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:ctWanMuxGroupDelChannel.setStatus(_A)
_CtWanMuxChannelTable_Object=MibTable
ctWanMuxChannelTable=_CtWanMuxChannelTable_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3))
if mibBuilder.loadTexts:ctWanMuxChannelTable.setStatus(_A)
_CtWanMuxChannelEntry_Object=MibTableRow
ctWanMuxChannelEntry=_CtWanMuxChannelEntry_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3,1))
ctWanMuxChannelEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:ctWanMuxChannelEntry.setStatus(_A)
class _CtWanMuxChannelGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMuxChannelGroupId_Type.__name__=_C
_CtWanMuxChannelGroupId_Object=MibTableColumn
ctWanMuxChannelGroupId=_CtWanMuxChannelGroupId_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3,1,1),_CtWanMuxChannelGroupId_Type())
ctWanMuxChannelGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxChannelGroupId.setStatus(_A)
class _CtWanMuxChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtWanMuxChannelId_Type.__name__=_C
_CtWanMuxChannelId_Object=MibTableColumn
ctWanMuxChannelId=_CtWanMuxChannelId_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3,1,2),_CtWanMuxChannelId_Type())
ctWanMuxChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxChannelId.setStatus(_A)
_CtWanMuxChannelIfIndex_Type=Integer32
_CtWanMuxChannelIfIndex_Object=MibTableColumn
ctWanMuxChannelIfIndex=_CtWanMuxChannelIfIndex_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3,1,3),_CtWanMuxChannelIfIndex_Type())
ctWanMuxChannelIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxChannelIfIndex.setStatus(_A)
_CtWanMuxChannelPhysNum_Type=Integer32
_CtWanMuxChannelPhysNum_Object=MibTableColumn
ctWanMuxChannelPhysNum=_CtWanMuxChannelPhysNum_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3,1,4),_CtWanMuxChannelPhysNum_Type())
ctWanMuxChannelPhysNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxChannelPhysNum.setStatus(_A)
_CtWanMuxChannelBwAvail_Type=Integer32
_CtWanMuxChannelBwAvail_Object=MibTableColumn
ctWanMuxChannelBwAvail=_CtWanMuxChannelBwAvail_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3,1,5),_CtWanMuxChannelBwAvail_Type())
ctWanMuxChannelBwAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxChannelBwAvail.setStatus(_A)
_CtWanMuxChannelByteCount_Type=Integer32
_CtWanMuxChannelByteCount_Object=MibTableColumn
ctWanMuxChannelByteCount=_CtWanMuxChannelByteCount_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3,1,6),_CtWanMuxChannelByteCount_Type())
ctWanMuxChannelByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxChannelByteCount.setStatus(_A)
class _CtWanMuxChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_CtWanMuxChannelStatus_Type.__name__=_C
_CtWanMuxChannelStatus_Object=MibTableColumn
ctWanMuxChannelStatus=_CtWanMuxChannelStatus_Object((1,3,6,1,4,1,52,4,1,2,7,3,1,3,1,7),_CtWanMuxChannelStatus_Type())
ctWanMuxChannelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanMuxChannelStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ctWanMux':ctWanMux,'ctWANMuxGeneralGroup':ctWANMuxGeneralGroup,'ctWANMuxMaxNumGroups':ctWANMuxMaxNumGroups,'ctWanMuxAdmin':ctWanMuxAdmin,'ctWanMuxGroupTable':ctWanMuxGroupTable,'ctWanMuxGroupEntry':ctWanMuxGroupEntry,_H:ctWanMuxGroupId,'ctWanMuxGroupAdmin':ctWanMuxGroupAdmin,'ctWanMuxGroupNumChannels':ctWanMuxGroupNumChannels,'ctWanMuxGroupAddChannel':ctWanMuxGroupAddChannel,'ctWanMuxGroupDelChannel':ctWanMuxGroupDelChannel,'ctWanMuxChannelTable':ctWanMuxChannelTable,'ctWanMuxChannelEntry':ctWanMuxChannelEntry,_I:ctWanMuxChannelGroupId,_J:ctWanMuxChannelId,'ctWanMuxChannelIfIndex':ctWanMuxChannelIfIndex,'ctWanMuxChannelPhysNum':ctWanMuxChannelPhysNum,'ctWanMuxChannelBwAvail':ctWanMuxChannelBwAvail,'ctWanMuxChannelByteCount':ctWanMuxChannelByteCount,'ctWanMuxChannelStatus':ctWanMuxChannelStatus})