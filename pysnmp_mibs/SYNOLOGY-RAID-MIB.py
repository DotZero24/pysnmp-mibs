_K='raidGroup'
_J='raidHotspareCnt'
_I='raidTotalSize'
_H='raidFreeSize'
_G='raidStatus'
_F='raidName'
_E='raidIndex'
_D='Integer32'
_C='read-only'
_B='SYNOLOGY-RAID-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synoRaid=ModuleIdentity((1,3,6,1,4,1,6574,3))
if mibBuilder.loadTexts:synoRaid.setRevisions(('2013-09-11 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_RaidTable_Object=MibTable
raidTable=_RaidTable_Object((1,3,6,1,4,1,6574,3,1))
if mibBuilder.loadTexts:raidTable.setStatus(_A)
_RaidEntry_Object=MibTableRow
raidEntry=_RaidEntry_Object((1,3,6,1,4,1,6574,3,1,1))
raidEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:raidEntry.setStatus(_A)
class _RaidIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaidIndex_Type.__name__=_D
_RaidIndex_Object=MibTableColumn
raidIndex=_RaidIndex_Object((1,3,6,1,4,1,6574,3,1,1,1),_RaidIndex_Type())
raidIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:raidIndex.setStatus(_A)
_RaidName_Type=OctetString
_RaidName_Object=MibTableColumn
raidName=_RaidName_Object((1,3,6,1,4,1,6574,3,1,1,2),_RaidName_Type())
raidName.setMaxAccess(_C)
if mibBuilder.loadTexts:raidName.setStatus(_A)
class _RaidStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_RaidStatus_Type.__name__=_D
_RaidStatus_Object=MibTableColumn
raidStatus=_RaidStatus_Object((1,3,6,1,4,1,6574,3,1,1,3),_RaidStatus_Type())
raidStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raidStatus.setStatus(_A)
_RaidFreeSize_Type=Counter64
_RaidFreeSize_Object=MibTableColumn
raidFreeSize=_RaidFreeSize_Object((1,3,6,1,4,1,6574,3,1,1,4),_RaidFreeSize_Type())
raidFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:raidFreeSize.setStatus(_A)
_RaidTotalSize_Type=Counter64
_RaidTotalSize_Object=MibTableColumn
raidTotalSize=_RaidTotalSize_Object((1,3,6,1,4,1,6574,3,1,1,5),_RaidTotalSize_Type())
raidTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:raidTotalSize.setStatus(_A)
_RaidHotspareCnt_Type=Integer32
_RaidHotspareCnt_Object=MibTableColumn
raidHotspareCnt=_RaidHotspareCnt_Object((1,3,6,1,4,1,6574,3,1,1,6),_RaidHotspareCnt_Type())
raidHotspareCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:raidHotspareCnt.setStatus(_A)
_RaidConformance_ObjectIdentity=ObjectIdentity
raidConformance=_RaidConformance_ObjectIdentity((1,3,6,1,4,1,6574,3,2))
_RaidCompliances_ObjectIdentity=ObjectIdentity
raidCompliances=_RaidCompliances_ObjectIdentity((1,3,6,1,4,1,6574,3,2,1))
_RaidGroups_ObjectIdentity=ObjectIdentity
raidGroups=_RaidGroups_ObjectIdentity((1,3,6,1,4,1,6574,3,2,2))
raidGroup=ObjectGroup((1,3,6,1,4,1,6574,3,2,2,1))
raidGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:raidGroup.setStatus(_A)
raidCompliance=ModuleCompliance((1,3,6,1,4,1,6574,3,2,1,1))
raidCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:raidCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synoRaid':synoRaid,'raidTable':raidTable,'raidEntry':raidEntry,_E:raidIndex,_F:raidName,_G:raidStatus,_H:raidFreeSize,_I:raidTotalSize,_J:raidHotspareCnt,'raidConformance':raidConformance,'raidCompliances':raidCompliances,'raidCompliance':raidCompliance,'raidGroups':raidGroups,_K:raidGroup})