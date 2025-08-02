_M='aristaNexthopGroupCounterGroup'
_L='aristaNexthopGroupGroup'
_K='aristaNexthopGroupCounterByteCount'
_J='aristaNexthopGroupCounterPacketCount'
_I='aristaNexthopGroupCounterIndex'
_H='aristaNexthopGroupType'
_G='aristaNexthopGroupName'
_F='aristaNexthopGroupEntryIndex'
_E='not-accessible'
_D='aristaNexthopGroupId'
_C='read-only'
_B='ARISTA-NEXTHOP-GROUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaNexthopGroupMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,21))
if mibBuilder.loadTexts:aristaNexthopGroupMIB.setRevisions(('2016-04-17 00:00',))
class NexthopGroupName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class NexthopGroupType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('invalid',0),('ipInIp',1),('gre',2),('mpls',3),('ip',4),('mplsOverGre',5)))
_AristaNexthopGroupMibObjects_ObjectIdentity=ObjectIdentity
aristaNexthopGroupMibObjects=_AristaNexthopGroupMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,21,1))
_AristaNexthopGroupTable_Object=MibTable
aristaNexthopGroupTable=_AristaNexthopGroupTable_Object((1,3,6,1,4,1,30065,3,21,1,1))
if mibBuilder.loadTexts:aristaNexthopGroupTable.setStatus(_A)
_AristaNexthopGroupEntry_Object=MibTableRow
aristaNexthopGroupEntry=_AristaNexthopGroupEntry_Object((1,3,6,1,4,1,30065,3,21,1,1,1))
aristaNexthopGroupEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:aristaNexthopGroupEntry.setStatus(_A)
_AristaNexthopGroupId_Type=Unsigned32
_AristaNexthopGroupId_Object=MibTableColumn
aristaNexthopGroupId=_AristaNexthopGroupId_Object((1,3,6,1,4,1,30065,3,21,1,1,1,1),_AristaNexthopGroupId_Type())
aristaNexthopGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaNexthopGroupId.setStatus(_A)
_AristaNexthopGroupName_Type=NexthopGroupName
_AristaNexthopGroupName_Object=MibTableColumn
aristaNexthopGroupName=_AristaNexthopGroupName_Object((1,3,6,1,4,1,30065,3,21,1,1,1,2),_AristaNexthopGroupName_Type())
aristaNexthopGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaNexthopGroupName.setStatus(_A)
_AristaNexthopGroupType_Type=NexthopGroupType
_AristaNexthopGroupType_Object=MibTableColumn
aristaNexthopGroupType=_AristaNexthopGroupType_Object((1,3,6,1,4,1,30065,3,21,1,1,1,3),_AristaNexthopGroupType_Type())
aristaNexthopGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaNexthopGroupType.setStatus(_A)
_AristaNexthopGroupCounterTable_Object=MibTable
aristaNexthopGroupCounterTable=_AristaNexthopGroupCounterTable_Object((1,3,6,1,4,1,30065,3,21,1,2))
if mibBuilder.loadTexts:aristaNexthopGroupCounterTable.setStatus(_A)
_AristaNexthopGroupCounterEntry_Object=MibTableRow
aristaNexthopGroupCounterEntry=_AristaNexthopGroupCounterEntry_Object((1,3,6,1,4,1,30065,3,21,1,2,1))
aristaNexthopGroupCounterEntry.setIndexNames((0,_B,_D),(0,_B,_F))
if mibBuilder.loadTexts:aristaNexthopGroupCounterEntry.setStatus(_A)
_AristaNexthopGroupEntryIndex_Type=Unsigned32
_AristaNexthopGroupEntryIndex_Object=MibTableColumn
aristaNexthopGroupEntryIndex=_AristaNexthopGroupEntryIndex_Object((1,3,6,1,4,1,30065,3,21,1,2,1,1),_AristaNexthopGroupEntryIndex_Type())
aristaNexthopGroupEntryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaNexthopGroupEntryIndex.setStatus(_A)
_AristaNexthopGroupCounterIndex_Type=Unsigned32
_AristaNexthopGroupCounterIndex_Object=MibTableColumn
aristaNexthopGroupCounterIndex=_AristaNexthopGroupCounterIndex_Object((1,3,6,1,4,1,30065,3,21,1,2,1,2),_AristaNexthopGroupCounterIndex_Type())
aristaNexthopGroupCounterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaNexthopGroupCounterIndex.setStatus(_A)
_AristaNexthopGroupCounterPacketCount_Type=Counter64
_AristaNexthopGroupCounterPacketCount_Object=MibTableColumn
aristaNexthopGroupCounterPacketCount=_AristaNexthopGroupCounterPacketCount_Object((1,3,6,1,4,1,30065,3,21,1,2,1,3),_AristaNexthopGroupCounterPacketCount_Type())
aristaNexthopGroupCounterPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaNexthopGroupCounterPacketCount.setStatus(_A)
_AristaNexthopGroupCounterByteCount_Type=Counter64
_AristaNexthopGroupCounterByteCount_Object=MibTableColumn
aristaNexthopGroupCounterByteCount=_AristaNexthopGroupCounterByteCount_Object((1,3,6,1,4,1,30065,3,21,1,2,1,4),_AristaNexthopGroupCounterByteCount_Type())
aristaNexthopGroupCounterByteCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaNexthopGroupCounterByteCount.setStatus(_A)
_AristaNexthopGroupMibConformance_ObjectIdentity=ObjectIdentity
aristaNexthopGroupMibConformance=_AristaNexthopGroupMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,21,2))
_AristaNexthopGroupMibCompliances_ObjectIdentity=ObjectIdentity
aristaNexthopGroupMibCompliances=_AristaNexthopGroupMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,21,2,1))
_AristaNexthopGroupMibGroups_ObjectIdentity=ObjectIdentity
aristaNexthopGroupMibGroups=_AristaNexthopGroupMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,21,2,2))
aristaNexthopGroupGroup=ObjectGroup((1,3,6,1,4,1,30065,3,21,2,2,1))
aristaNexthopGroupGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:aristaNexthopGroupGroup.setStatus(_A)
aristaNexthopGroupCounterGroup=ObjectGroup((1,3,6,1,4,1,30065,3,21,2,2,2))
aristaNexthopGroupCounterGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:aristaNexthopGroupCounterGroup.setStatus(_A)
aristaNexthopGroupMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,21,2,1,1))
aristaNexthopGroupMibCompliance.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:aristaNexthopGroupMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NexthopGroupName':NexthopGroupName,'NexthopGroupType':NexthopGroupType,'aristaNexthopGroupMIB':aristaNexthopGroupMIB,'aristaNexthopGroupMibObjects':aristaNexthopGroupMibObjects,'aristaNexthopGroupTable':aristaNexthopGroupTable,'aristaNexthopGroupEntry':aristaNexthopGroupEntry,_D:aristaNexthopGroupId,_G:aristaNexthopGroupName,_H:aristaNexthopGroupType,'aristaNexthopGroupCounterTable':aristaNexthopGroupCounterTable,'aristaNexthopGroupCounterEntry':aristaNexthopGroupCounterEntry,_F:aristaNexthopGroupEntryIndex,_I:aristaNexthopGroupCounterIndex,_J:aristaNexthopGroupCounterPacketCount,_K:aristaNexthopGroupCounterByteCount,'aristaNexthopGroupMibConformance':aristaNexthopGroupMibConformance,'aristaNexthopGroupMibCompliances':aristaNexthopGroupMibCompliances,'aristaNexthopGroupMibCompliance':aristaNexthopGroupMibCompliance,'aristaNexthopGroupMibGroups':aristaNexthopGroupMibGroups,_L:aristaNexthopGroupGroup,_M:aristaNexthopGroupCounterGroup})