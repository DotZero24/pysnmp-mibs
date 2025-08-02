_O='ciscoVismRsrcPartGroup'
_N='vismResPartCtrlrID'
_M='vismResPartEgrPctBW'
_L='vismResPartIngrPctBW'
_K='vismResPartLcnHigh'
_J='vismResPartLcnLow'
_I='vismResPartNumOfLcnAvail'
_H='vismResPartRowStatus'
_G='read-only'
_F='vismResPartCtrlrNum'
_E='vismResPartPortNum'
_D='read-write'
_C='Integer32'
_B='CISCO-VISM-RSRC-PART-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
vismPort,=mibBuilder.importSymbols('BASIS-MIB','vismPort')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVismRsrcPartMIB=ModuleIdentity((1,3,6,1,4,1,351,150,93))
if mibBuilder.loadTexts:ciscoVismRsrcPartMIB.setRevisions(('2003-12-09 00:00',))
_VismPortResPartCnfGrp_ObjectIdentity=ObjectIdentity
vismPortResPartCnfGrp=_VismPortResPartCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,2,2))
_VismPortResPartCnfGrpTable_Object=MibTable
vismPortResPartCnfGrpTable=_VismPortResPartCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,5,2,2,1))
if mibBuilder.loadTexts:vismPortResPartCnfGrpTable.setStatus(_A)
_VismPortResPartCnfGrpEntry_Object=MibTableRow
vismPortResPartCnfGrpEntry=_VismPortResPartCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1))
vismPortResPartCnfGrpEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:vismPortResPartCnfGrpEntry.setStatus(_A)
class _VismResPartPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VismResPartPortNum_Type.__name__=_C
_VismResPartPortNum_Object=MibTableColumn
vismResPartPortNum=_VismResPartPortNum_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,1),_VismResPartPortNum_Type())
vismResPartPortNum.setMaxAccess(_G)
if mibBuilder.loadTexts:vismResPartPortNum.setStatus(_A)
class _VismResPartCtrlrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('par',1),('pnni',2),('tag',3)))
_VismResPartCtrlrNum_Type.__name__=_C
_VismResPartCtrlrNum_Object=MibTableColumn
vismResPartCtrlrNum=_VismResPartCtrlrNum_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,2),_VismResPartCtrlrNum_Type())
vismResPartCtrlrNum.setMaxAccess(_G)
if mibBuilder.loadTexts:vismResPartCtrlrNum.setStatus(_A)
class _VismResPartRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_VismResPartRowStatus_Type.__name__=_C
_VismResPartRowStatus_Object=MibTableColumn
vismResPartRowStatus=_VismResPartRowStatus_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,3),_VismResPartRowStatus_Type())
vismResPartRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vismResPartRowStatus.setStatus(_A)
class _VismResPartNumOfLcnAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,380))
_VismResPartNumOfLcnAvail_Type.__name__=_C
_VismResPartNumOfLcnAvail_Object=MibTableColumn
vismResPartNumOfLcnAvail=_VismResPartNumOfLcnAvail_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,4),_VismResPartNumOfLcnAvail_Type())
vismResPartNumOfLcnAvail.setMaxAccess(_D)
if mibBuilder.loadTexts:vismResPartNumOfLcnAvail.setStatus(_A)
class _VismResPartLcnLow_Type(Integer32):defaultValue=131;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismResPartLcnLow_Type.__name__=_C
_VismResPartLcnLow_Object=MibTableColumn
vismResPartLcnLow=_VismResPartLcnLow_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,5),_VismResPartLcnLow_Type())
vismResPartLcnLow.setMaxAccess(_D)
if mibBuilder.loadTexts:vismResPartLcnLow.setStatus(_A)
class _VismResPartLcnHigh_Type(Integer32):defaultValue=510;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismResPartLcnHigh_Type.__name__=_C
_VismResPartLcnHigh_Object=MibTableColumn
vismResPartLcnHigh=_VismResPartLcnHigh_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,6),_VismResPartLcnHigh_Type())
vismResPartLcnHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:vismResPartLcnHigh.setStatus(_A)
class _VismResPartIngrPctBW_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VismResPartIngrPctBW_Type.__name__=_C
_VismResPartIngrPctBW_Object=MibTableColumn
vismResPartIngrPctBW=_VismResPartIngrPctBW_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,7),_VismResPartIngrPctBW_Type())
vismResPartIngrPctBW.setMaxAccess(_D)
if mibBuilder.loadTexts:vismResPartIngrPctBW.setStatus(_A)
class _VismResPartEgrPctBW_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VismResPartEgrPctBW_Type.__name__=_C
_VismResPartEgrPctBW_Object=MibTableColumn
vismResPartEgrPctBW=_VismResPartEgrPctBW_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,8),_VismResPartEgrPctBW_Type())
vismResPartEgrPctBW.setMaxAccess(_D)
if mibBuilder.loadTexts:vismResPartEgrPctBW.setStatus(_A)
class _VismResPartCtrlrID_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VismResPartCtrlrID_Type.__name__=_C
_VismResPartCtrlrID_Object=MibTableColumn
vismResPartCtrlrID=_VismResPartCtrlrID_Object((1,3,6,1,4,1,351,110,5,5,2,2,1,1,9),_VismResPartCtrlrID_Type())
vismResPartCtrlrID.setMaxAccess(_D)
if mibBuilder.loadTexts:vismResPartCtrlrID.setStatus(_A)
_CiscoVismRsrcPartMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismRsrcPartMIBConformance=_CiscoVismRsrcPartMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,93,2))
_CiscoVismRsrcPartMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismRsrcPartMIBGroups=_CiscoVismRsrcPartMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,93,2,1))
_CiscoVismRsrcPartMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismRsrcPartMIBCompliances=_CiscoVismRsrcPartMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,93,2,2))
ciscoVismRsrcPartGroup=ObjectGroup((1,3,6,1,4,1,351,150,93,2,1,1))
ciscoVismRsrcPartGroup.setObjects(*((_B,_E),(_B,_F),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoVismRsrcPartGroup.setStatus(_A)
ciscoVismRsrcPartCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,93,2,2,1))
ciscoVismRsrcPartCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoVismRsrcPartCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismPortResPartCnfGrp':vismPortResPartCnfGrp,'vismPortResPartCnfGrpTable':vismPortResPartCnfGrpTable,'vismPortResPartCnfGrpEntry':vismPortResPartCnfGrpEntry,_E:vismResPartPortNum,_F:vismResPartCtrlrNum,_H:vismResPartRowStatus,_I:vismResPartNumOfLcnAvail,_J:vismResPartLcnLow,_K:vismResPartLcnHigh,_L:vismResPartIngrPctBW,_M:vismResPartEgrPctBW,_N:vismResPartCtrlrID,'ciscoVismRsrcPartMIB':ciscoVismRsrcPartMIB,'ciscoVismRsrcPartMIBConformance':ciscoVismRsrcPartMIBConformance,'ciscoVismRsrcPartMIBGroups':ciscoVismRsrcPartMIBGroups,_O:ciscoVismRsrcPartGroup,'ciscoVismRsrcPartMIBCompliances':ciscoVismRsrcPartMIBCompliances,'ciscoVismRsrcPartCompliance':ciscoVismRsrcPartCompliance})