_I='cmmRsrcPartGroup'
_H='cardResPartNumOfLcnAvail'
_G='cardResPartRowStatus'
_F='cardLcnPartitionType'
_E='cardResPartCtrlrNum'
_D='read-write'
_C='Integer32'
_B='CISCO-MGX82XX-MODULE-RSRC-PART-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardGeneric,=mibBuilder.importSymbols('BASIS-MIB','cardGeneric')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxModuleRsrcPartMIB=ModuleIdentity((1,3,6,1,4,1,351,150,73))
if mibBuilder.loadTexts:ciscoMgx82xxModuleRsrcPartMIB.setRevisions(('2003-04-18 00:00',))
_CardResourcePartition_ObjectIdentity=ObjectIdentity
cardResourcePartition=_CardResourcePartition_ObjectIdentity((1,3,6,1,4,1,351,110,2,9))
class _CardLcnPartitionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noPartition',1),('controllerBased',2),('portControllerBased',3)))
_CardLcnPartitionType_Type.__name__=_C
_CardLcnPartitionType_Object=MibScalar
cardLcnPartitionType=_CardLcnPartitionType_Object((1,3,6,1,4,1,351,110,2,9,1),_CardLcnPartitionType_Type())
cardLcnPartitionType.setMaxAccess(_D)
if mibBuilder.loadTexts:cardLcnPartitionType.setStatus(_A)
_CardResPartGrpTable_Object=MibTable
cardResPartGrpTable=_CardResPartGrpTable_Object((1,3,6,1,4,1,351,110,2,9,2))
if mibBuilder.loadTexts:cardResPartGrpTable.setStatus(_A)
_CardResPartGrpEntry_Object=MibTableRow
cardResPartGrpEntry=_CardResPartGrpEntry_Object((1,3,6,1,4,1,351,110,2,9,2,1))
cardResPartGrpEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cardResPartGrpEntry.setStatus(_A)
class _CardResPartCtrlrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('par',1),('pnni',2),('tag',3)))
_CardResPartCtrlrNum_Type.__name__=_C
_CardResPartCtrlrNum_Object=MibTableColumn
cardResPartCtrlrNum=_CardResPartCtrlrNum_Object((1,3,6,1,4,1,351,110,2,9,2,1,1),_CardResPartCtrlrNum_Type())
cardResPartCtrlrNum.setMaxAccess('read-only')
if mibBuilder.loadTexts:cardResPartCtrlrNum.setStatus(_A)
class _CardResPartRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_CardResPartRowStatus_Type.__name__=_C
_CardResPartRowStatus_Object=MibTableColumn
cardResPartRowStatus=_CardResPartRowStatus_Object((1,3,6,1,4,1,351,110,2,9,2,1,2),_CardResPartRowStatus_Type())
cardResPartRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cardResPartRowStatus.setStatus(_A)
class _CardResPartNumOfLcnAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CardResPartNumOfLcnAvail_Type.__name__=_C
_CardResPartNumOfLcnAvail_Object=MibTableColumn
cardResPartNumOfLcnAvail=_CardResPartNumOfLcnAvail_Object((1,3,6,1,4,1,351,110,2,9,2,1,3),_CardResPartNumOfLcnAvail_Type())
cardResPartNumOfLcnAvail.setMaxAccess(_D)
if mibBuilder.loadTexts:cardResPartNumOfLcnAvail.setStatus(_A)
_CmmRsrcPartMIBConformance_ObjectIdentity=ObjectIdentity
cmmRsrcPartMIBConformance=_CmmRsrcPartMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,73,2))
_CmmRsrcPartMIBCompliances_ObjectIdentity=ObjectIdentity
cmmRsrcPartMIBCompliances=_CmmRsrcPartMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,73,2,1))
_CmmRsrcPartMIBGroups_ObjectIdentity=ObjectIdentity
cmmRsrcPartMIBGroups=_CmmRsrcPartMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,73,2,2))
cmmRsrcPartGroup=ObjectGroup((1,3,6,1,4,1,351,150,73,2,2,1))
cmmRsrcPartGroup.setObjects(*((_B,_F),(_B,_E),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cmmRsrcPartGroup.setStatus(_A)
cmmRsrcPartCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,73,2,1,1))
cmmRsrcPartCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:cmmRsrcPartCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cardResourcePartition':cardResourcePartition,_F:cardLcnPartitionType,'cardResPartGrpTable':cardResPartGrpTable,'cardResPartGrpEntry':cardResPartGrpEntry,_E:cardResPartCtrlrNum,_G:cardResPartRowStatus,_H:cardResPartNumOfLcnAvail,'ciscoMgx82xxModuleRsrcPartMIB':ciscoMgx82xxModuleRsrcPartMIB,'cmmRsrcPartMIBConformance':cmmRsrcPartMIBConformance,'cmmRsrcPartMIBCompliances':cmmRsrcPartMIBCompliances,'cmmRsrcPartCompliance':cmmRsrcPartCompliance,'cmmRsrcPartMIBGroups':cmmRsrcPartMIBGroups,_I:cmmRsrcPartGroup})