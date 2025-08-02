_R='diskGroup'
_Q='diskHealthStatus'
_P='diskName'
_O='diskRemainLife'
_N='diskIdentifyFail'
_M='diskBadSector'
_L='diskRetry'
_K='diskRole'
_J='diskTemperature'
_I='diskStatus'
_H='diskType'
_G='diskModel'
_F='diskID'
_E='diskIndex'
_D='Integer32'
_C='read-only'
_B='SYNOLOGY-DISK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synoDisk=ModuleIdentity((1,3,6,1,4,1,6574,2))
if mibBuilder.loadTexts:synoDisk.setRevisions(('2013-09-11 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_DiskTable_Object=MibTable
diskTable=_DiskTable_Object((1,3,6,1,4,1,6574,2,1))
if mibBuilder.loadTexts:diskTable.setStatus(_A)
_DiskEntry_Object=MibTableRow
diskEntry=_DiskEntry_Object((1,3,6,1,4,1,6574,2,1,1))
diskEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:diskEntry.setStatus(_A)
class _DiskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DiskIndex_Type.__name__=_D
_DiskIndex_Object=MibTableColumn
diskIndex=_DiskIndex_Object((1,3,6,1,4,1,6574,2,1,1,1),_DiskIndex_Type())
diskIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:diskIndex.setStatus(_A)
_DiskID_Type=OctetString
_DiskID_Object=MibTableColumn
diskID=_DiskID_Object((1,3,6,1,4,1,6574,2,1,1,2),_DiskID_Type())
diskID.setMaxAccess(_C)
if mibBuilder.loadTexts:diskID.setStatus(_A)
_DiskModel_Type=OctetString
_DiskModel_Object=MibTableColumn
diskModel=_DiskModel_Object((1,3,6,1,4,1,6574,2,1,1,3),_DiskModel_Type())
diskModel.setMaxAccess(_C)
if mibBuilder.loadTexts:diskModel.setStatus(_A)
_DiskType_Type=OctetString
_DiskType_Object=MibTableColumn
diskType=_DiskType_Object((1,3,6,1,4,1,6574,2,1,1,4),_DiskType_Type())
diskType.setMaxAccess(_C)
if mibBuilder.loadTexts:diskType.setStatus(_A)
class _DiskStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_DiskStatus_Type.__name__=_D
_DiskStatus_Object=MibTableColumn
diskStatus=_DiskStatus_Object((1,3,6,1,4,1,6574,2,1,1,5),_DiskStatus_Type())
diskStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:diskStatus.setStatus(_A)
_DiskTemperature_Type=Integer32
_DiskTemperature_Object=MibTableColumn
diskTemperature=_DiskTemperature_Object((1,3,6,1,4,1,6574,2,1,1,6),_DiskTemperature_Type())
diskTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:diskTemperature.setStatus(_A)
_DiskRole_Type=OctetString
_DiskRole_Object=MibTableColumn
diskRole=_DiskRole_Object((1,3,6,1,4,1,6574,2,1,1,7),_DiskRole_Type())
diskRole.setMaxAccess(_C)
if mibBuilder.loadTexts:diskRole.setStatus(_A)
_DiskRetry_Type=Integer32
_DiskRetry_Object=MibTableColumn
diskRetry=_DiskRetry_Object((1,3,6,1,4,1,6574,2,1,1,8),_DiskRetry_Type())
diskRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:diskRetry.setStatus(_A)
_DiskBadSector_Type=Integer32
_DiskBadSector_Object=MibTableColumn
diskBadSector=_DiskBadSector_Object((1,3,6,1,4,1,6574,2,1,1,9),_DiskBadSector_Type())
diskBadSector.setMaxAccess(_C)
if mibBuilder.loadTexts:diskBadSector.setStatus(_A)
_DiskIdentifyFail_Type=Integer32
_DiskIdentifyFail_Object=MibTableColumn
diskIdentifyFail=_DiskIdentifyFail_Object((1,3,6,1,4,1,6574,2,1,1,10),_DiskIdentifyFail_Type())
diskIdentifyFail.setMaxAccess(_C)
if mibBuilder.loadTexts:diskIdentifyFail.setStatus(_A)
_DiskRemainLife_Type=Integer32
_DiskRemainLife_Object=MibTableColumn
diskRemainLife=_DiskRemainLife_Object((1,3,6,1,4,1,6574,2,1,1,11),_DiskRemainLife_Type())
diskRemainLife.setMaxAccess(_C)
if mibBuilder.loadTexts:diskRemainLife.setStatus(_A)
_DiskName_Type=OctetString
_DiskName_Object=MibTableColumn
diskName=_DiskName_Object((1,3,6,1,4,1,6574,2,1,1,12),_DiskName_Type())
diskName.setMaxAccess(_C)
if mibBuilder.loadTexts:diskName.setStatus(_A)
class _DiskHealthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_DiskHealthStatus_Type.__name__=_D
_DiskHealthStatus_Object=MibTableColumn
diskHealthStatus=_DiskHealthStatus_Object((1,3,6,1,4,1,6574,2,1,1,13),_DiskHealthStatus_Type())
diskHealthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:diskHealthStatus.setStatus(_A)
_DiskConformance_ObjectIdentity=ObjectIdentity
diskConformance=_DiskConformance_ObjectIdentity((1,3,6,1,4,1,6574,2,2))
_DiskCompliances_ObjectIdentity=ObjectIdentity
diskCompliances=_DiskCompliances_ObjectIdentity((1,3,6,1,4,1,6574,2,2,1))
_DiskGroups_ObjectIdentity=ObjectIdentity
diskGroups=_DiskGroups_ObjectIdentity((1,3,6,1,4,1,6574,2,2,2))
diskGroup=ObjectGroup((1,3,6,1,4,1,6574,2,2,2,1))
diskGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:diskGroup.setStatus(_A)
diskCompliance=ModuleCompliance((1,3,6,1,4,1,6574,2,2,1,1))
diskCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:diskCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synoDisk':synoDisk,'diskTable':diskTable,'diskEntry':diskEntry,_E:diskIndex,_F:diskID,_G:diskModel,_H:diskType,_I:diskStatus,_J:diskTemperature,_K:diskRole,_L:diskRetry,_M:diskBadSector,_N:diskIdentifyFail,_O:diskRemainLife,_P:diskName,_Q:diskHealthStatus,'diskConformance':diskConformance,'diskCompliances':diskCompliances,'diskCompliance':diskCompliance,'diskGroups':diskGroups,_R:diskGroup})