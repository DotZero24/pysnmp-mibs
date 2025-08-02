_O='synologyDiskSMARTGroup'
_N='diskSMARTAttrRaw64'
_M='diskSMARTAttrStatus'
_L='diskSMARTAttrRaw'
_K='diskSMARTAttrThreshold'
_J='diskSMARTAttrWorst'
_I='diskSMARTAttrCurrent'
_H='diskSMARTAttrId'
_G='diskSMARTAttrName'
_F='diskSMARTInfoDevName'
_E='diskSMARTInfoIndex'
_D='Integer32'
_C='read-only'
_B='SYNOLOGY-SMART-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synologyDiskSMART=ModuleIdentity((1,3,6,1,4,1,6574,5))
if mibBuilder.loadTexts:synologyDiskSMART.setRevisions(('2016-05-05 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_DiskSMARTTable_Object=MibTable
diskSMARTTable=_DiskSMARTTable_Object((1,3,6,1,4,1,6574,5,1))
if mibBuilder.loadTexts:diskSMARTTable.setStatus(_A)
_DiskSMARTEntry_Object=MibTableRow
diskSMARTEntry=_DiskSMARTEntry_Object((1,3,6,1,4,1,6574,5,1,1))
diskSMARTEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:diskSMARTEntry.setStatus(_A)
class _DiskSMARTInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DiskSMARTInfoIndex_Type.__name__=_D
_DiskSMARTInfoIndex_Object=MibTableColumn
diskSMARTInfoIndex=_DiskSMARTInfoIndex_Object((1,3,6,1,4,1,6574,5,1,1,1),_DiskSMARTInfoIndex_Type())
diskSMARTInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:diskSMARTInfoIndex.setStatus(_A)
_DiskSMARTInfoDevName_Type=OctetString
_DiskSMARTInfoDevName_Object=MibTableColumn
diskSMARTInfoDevName=_DiskSMARTInfoDevName_Object((1,3,6,1,4,1,6574,5,1,1,2),_DiskSMARTInfoDevName_Type())
diskSMARTInfoDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTInfoDevName.setStatus(_A)
_DiskSMARTAttrName_Type=OctetString
_DiskSMARTAttrName_Object=MibTableColumn
diskSMARTAttrName=_DiskSMARTAttrName_Object((1,3,6,1,4,1,6574,5,1,1,3),_DiskSMARTAttrName_Type())
diskSMARTAttrName.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTAttrName.setStatus(_A)
_DiskSMARTAttrId_Type=Integer32
_DiskSMARTAttrId_Object=MibTableColumn
diskSMARTAttrId=_DiskSMARTAttrId_Object((1,3,6,1,4,1,6574,5,1,1,4),_DiskSMARTAttrId_Type())
diskSMARTAttrId.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTAttrId.setStatus(_A)
_DiskSMARTAttrCurrent_Type=Integer32
_DiskSMARTAttrCurrent_Object=MibTableColumn
diskSMARTAttrCurrent=_DiskSMARTAttrCurrent_Object((1,3,6,1,4,1,6574,5,1,1,5),_DiskSMARTAttrCurrent_Type())
diskSMARTAttrCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTAttrCurrent.setStatus(_A)
_DiskSMARTAttrWorst_Type=Integer32
_DiskSMARTAttrWorst_Object=MibTableColumn
diskSMARTAttrWorst=_DiskSMARTAttrWorst_Object((1,3,6,1,4,1,6574,5,1,1,6),_DiskSMARTAttrWorst_Type())
diskSMARTAttrWorst.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTAttrWorst.setStatus(_A)
_DiskSMARTAttrThreshold_Type=Integer32
_DiskSMARTAttrThreshold_Object=MibTableColumn
diskSMARTAttrThreshold=_DiskSMARTAttrThreshold_Object((1,3,6,1,4,1,6574,5,1,1,7),_DiskSMARTAttrThreshold_Type())
diskSMARTAttrThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTAttrThreshold.setStatus(_A)
_DiskSMARTAttrRaw_Type=Integer32
_DiskSMARTAttrRaw_Object=MibTableColumn
diskSMARTAttrRaw=_DiskSMARTAttrRaw_Object((1,3,6,1,4,1,6574,5,1,1,8),_DiskSMARTAttrRaw_Type())
diskSMARTAttrRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTAttrRaw.setStatus(_A)
_DiskSMARTAttrStatus_Type=OctetString
_DiskSMARTAttrStatus_Object=MibTableColumn
diskSMARTAttrStatus=_DiskSMARTAttrStatus_Object((1,3,6,1,4,1,6574,5,1,1,9),_DiskSMARTAttrStatus_Type())
diskSMARTAttrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTAttrStatus.setStatus(_A)
_DiskSMARTAttrRaw64_Type=Counter64
_DiskSMARTAttrRaw64_Object=MibTableColumn
diskSMARTAttrRaw64=_DiskSMARTAttrRaw64_Object((1,3,6,1,4,1,6574,5,1,1,10),_DiskSMARTAttrRaw64_Type())
diskSMARTAttrRaw64.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSMARTAttrRaw64.setStatus(_A)
_SynologyDiskSMARTConformance_ObjectIdentity=ObjectIdentity
synologyDiskSMARTConformance=_SynologyDiskSMARTConformance_ObjectIdentity((1,3,6,1,4,1,6574,5,2))
_SynologyDiskSMARTCompliances_ObjectIdentity=ObjectIdentity
synologyDiskSMARTCompliances=_SynologyDiskSMARTCompliances_ObjectIdentity((1,3,6,1,4,1,6574,5,2,1))
_SynologyDiskSMARTGroups_ObjectIdentity=ObjectIdentity
synologyDiskSMARTGroups=_SynologyDiskSMARTGroups_ObjectIdentity((1,3,6,1,4,1,6574,5,2,2))
synologyDiskSMARTGroup=ObjectGroup((1,3,6,1,4,1,6574,5,2,2,1))
synologyDiskSMARTGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:synologyDiskSMARTGroup.setStatus(_A)
synologyDiskSMARTCompliance=ModuleCompliance((1,3,6,1,4,1,6574,5,2,1,1))
synologyDiskSMARTCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:synologyDiskSMARTCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synologyDiskSMART':synologyDiskSMART,'diskSMARTTable':diskSMARTTable,'diskSMARTEntry':diskSMARTEntry,_E:diskSMARTInfoIndex,_F:diskSMARTInfoDevName,_G:diskSMARTAttrName,_H:diskSMARTAttrId,_I:diskSMARTAttrCurrent,_J:diskSMARTAttrWorst,_K:diskSMARTAttrThreshold,_L:diskSMARTAttrRaw,_M:diskSMARTAttrStatus,_N:diskSMARTAttrRaw64,'synologyDiskSMARTConformance':synologyDiskSMARTConformance,'synologyDiskSMARTCompliances':synologyDiskSMARTCompliances,'synologyDiskSMARTCompliance':synologyDiskSMARTCompliance,'synologyDiskSMARTGroups':synologyDiskSMARTGroups,_O:synologyDiskSMARTGroup})