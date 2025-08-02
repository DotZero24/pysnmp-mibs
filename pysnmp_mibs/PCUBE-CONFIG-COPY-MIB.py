_I='pcubeCopyGroup'
_H='pcubeCopyDestFileType'
_G='pcubeCopySourceFileType'
_F='pcubeCopyEntryRowStatus'
_E='pcubeCopyIndex'
_D='Integer32'
_C='read-write'
_B='PCUBE-CONFIG-COPY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pcubeMgmt,=mibBuilder.importSymbols('PCUBE-SMI','pcubeMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
pcubeConfigCopyMIB=ModuleIdentity((1,3,6,1,4,1,5655,3,1))
if mibBuilder.loadTexts:pcubeConfigCopyMIB.setRevisions(('2006-04-06 20:00','2002-01-14 20:00'))
class ConfigFileType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('startupConfig',1),('runningConfig',2)))
_PcubeConfigCopyMIBObjects_ObjectIdentity=ObjectIdentity
pcubeConfigCopyMIBObjects=_PcubeConfigCopyMIBObjects_ObjectIdentity((1,3,6,1,4,1,5655,3,1,1))
_PcubeCopy_ObjectIdentity=ObjectIdentity
pcubeCopy=_PcubeCopy_ObjectIdentity((1,3,6,1,4,1,5655,3,1,1,1))
_PcubeCopyTable_Object=MibTable
pcubeCopyTable=_PcubeCopyTable_Object((1,3,6,1,4,1,5655,3,1,1,1,1))
if mibBuilder.loadTexts:pcubeCopyTable.setStatus(_A)
_PcubeCopyEntry_Object=MibTableRow
pcubeCopyEntry=_PcubeCopyEntry_Object((1,3,6,1,4,1,5655,3,1,1,1,1,1))
pcubeCopyEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:pcubeCopyEntry.setStatus(_A)
class _PcubeCopyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PcubeCopyIndex_Type.__name__=_D
_PcubeCopyIndex_Object=MibTableColumn
pcubeCopyIndex=_PcubeCopyIndex_Object((1,3,6,1,4,1,5655,3,1,1,1,1,1,1),_PcubeCopyIndex_Type())
pcubeCopyIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pcubeCopyIndex.setStatus(_A)
_PcubeCopyEntryRowStatus_Type=RowStatus
_PcubeCopyEntryRowStatus_Object=MibTableColumn
pcubeCopyEntryRowStatus=_PcubeCopyEntryRowStatus_Object((1,3,6,1,4,1,5655,3,1,1,1,1,1,2),_PcubeCopyEntryRowStatus_Type())
pcubeCopyEntryRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pcubeCopyEntryRowStatus.setStatus(_A)
_PcubeCopySourceFileType_Type=ConfigFileType
_PcubeCopySourceFileType_Object=MibTableColumn
pcubeCopySourceFileType=_PcubeCopySourceFileType_Object((1,3,6,1,4,1,5655,3,1,1,1,1,1,3),_PcubeCopySourceFileType_Type())
pcubeCopySourceFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:pcubeCopySourceFileType.setStatus(_A)
_PcubeCopyDestFileType_Type=ConfigFileType
_PcubeCopyDestFileType_Object=MibTableColumn
pcubeCopyDestFileType=_PcubeCopyDestFileType_Object((1,3,6,1,4,1,5655,3,1,1,1,1,1,4),_PcubeCopyDestFileType_Type())
pcubeCopyDestFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:pcubeCopyDestFileType.setStatus(_A)
_PcubeConfigCopyMIBConformance_ObjectIdentity=ObjectIdentity
pcubeConfigCopyMIBConformance=_PcubeConfigCopyMIBConformance_ObjectIdentity((1,3,6,1,4,1,5655,3,1,2))
_PcubeConfigCopyMIBGroups_ObjectIdentity=ObjectIdentity
pcubeConfigCopyMIBGroups=_PcubeConfigCopyMIBGroups_ObjectIdentity((1,3,6,1,4,1,5655,3,1,2,1))
_PcubeConfigCopyMIBCompliances_ObjectIdentity=ObjectIdentity
pcubeConfigCopyMIBCompliances=_PcubeConfigCopyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5655,3,1,2,2))
pcubeCopyGroup=ObjectGroup((1,3,6,1,4,1,5655,3,1,2,1,1))
pcubeCopyGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:pcubeCopyGroup.setStatus(_A)
pcubeConfigCopyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,5655,3,1,2,2,1))
pcubeConfigCopyMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:pcubeConfigCopyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ConfigFileType':ConfigFileType,'pcubeConfigCopyMIB':pcubeConfigCopyMIB,'pcubeConfigCopyMIBObjects':pcubeConfigCopyMIBObjects,'pcubeCopy':pcubeCopy,'pcubeCopyTable':pcubeCopyTable,'pcubeCopyEntry':pcubeCopyEntry,_E:pcubeCopyIndex,_F:pcubeCopyEntryRowStatus,_G:pcubeCopySourceFileType,_H:pcubeCopyDestFileType,'pcubeConfigCopyMIBConformance':pcubeConfigCopyMIBConformance,'pcubeConfigCopyMIBGroups':pcubeConfigCopyMIBGroups,_I:pcubeCopyGroup,'pcubeConfigCopyMIBCompliances':pcubeConfigCopyMIBCompliances,'pcubeConfigCopyMIBCompliance':pcubeConfigCopyMIBCompliance})