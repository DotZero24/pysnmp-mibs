_O='ciscoWanCesRsrcPartGroup'
_N='cesmResPartCtrlrID'
_M='cesmResPartEgrPctBW'
_L='cesmResPartIngrPctBW'
_K='cesmResPartLcnHigh'
_J='cesmResPartLcnLow'
_I='cesmResPartNumOfLcnAvail'
_H='cesmResPartRowStatus'
_G='read-only'
_F='cesmResPartCtrlrNum'
_E='cesmResPartPortNum'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-CES-RSRC-PART-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cesmPort,=mibBuilder.importSymbols('CISCO-WAN-CES-PORT-MIB','cesmPort')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanCesRsrcPartMIB=ModuleIdentity((1,3,6,1,4,1,351,150,41))
if mibBuilder.loadTexts:ciscoWanCesRsrcPartMIB.setRevisions(('2002-09-03 00:00',))
_CesmPortCnfResPartGrp_ObjectIdentity=ObjectIdentity
cesmPortCnfResPartGrp=_CesmPortCnfResPartGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,3,1,2))
_CesmPortCnfResPartGrpTable_Object=MibTable
cesmPortCnfResPartGrpTable=_CesmPortCnfResPartGrpTable_Object((1,3,6,1,4,1,351,110,5,3,1,2,1))
if mibBuilder.loadTexts:cesmPortCnfResPartGrpTable.setStatus(_A)
_CesmPortCnfResPartGrpEntry_Object=MibTableRow
cesmPortCnfResPartGrpEntry=_CesmPortCnfResPartGrpEntry_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1))
cesmPortCnfResPartGrpEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:cesmPortCnfResPartGrpEntry.setStatus(_A)
class _CesmResPartPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CesmResPartPortNum_Type.__name__=_C
_CesmResPartPortNum_Object=MibTableColumn
cesmResPartPortNum=_CesmResPartPortNum_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,1),_CesmResPartPortNum_Type())
cesmResPartPortNum.setMaxAccess(_G)
if mibBuilder.loadTexts:cesmResPartPortNum.setStatus(_A)
class _CesmResPartCtrlrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('par',1),('pnni',2),('tag',3)))
_CesmResPartCtrlrNum_Type.__name__=_C
_CesmResPartCtrlrNum_Object=MibTableColumn
cesmResPartCtrlrNum=_CesmResPartCtrlrNum_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,2),_CesmResPartCtrlrNum_Type())
cesmResPartCtrlrNum.setMaxAccess(_G)
if mibBuilder.loadTexts:cesmResPartCtrlrNum.setStatus(_A)
class _CesmResPartRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_CesmResPartRowStatus_Type.__name__=_C
_CesmResPartRowStatus_Object=MibTableColumn
cesmResPartRowStatus=_CesmResPartRowStatus_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,3),_CesmResPartRowStatus_Type())
cesmResPartRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmResPartRowStatus.setStatus(_A)
class _CesmResPartNumOfLcnAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CesmResPartNumOfLcnAvail_Type.__name__=_C
_CesmResPartNumOfLcnAvail_Object=MibTableColumn
cesmResPartNumOfLcnAvail=_CesmResPartNumOfLcnAvail_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,4),_CesmResPartNumOfLcnAvail_Type())
cesmResPartNumOfLcnAvail.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmResPartNumOfLcnAvail.setStatus(_A)
class _CesmResPartLcnLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CesmResPartLcnLow_Type.__name__=_C
_CesmResPartLcnLow_Object=MibTableColumn
cesmResPartLcnLow=_CesmResPartLcnLow_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,5),_CesmResPartLcnLow_Type())
cesmResPartLcnLow.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmResPartLcnLow.setStatus(_A)
class _CesmResPartLcnHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CesmResPartLcnHigh_Type.__name__=_C
_CesmResPartLcnHigh_Object=MibTableColumn
cesmResPartLcnHigh=_CesmResPartLcnHigh_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,6),_CesmResPartLcnHigh_Type())
cesmResPartLcnHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmResPartLcnHigh.setStatus(_A)
class _CesmResPartIngrPctBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CesmResPartIngrPctBW_Type.__name__=_C
_CesmResPartIngrPctBW_Object=MibTableColumn
cesmResPartIngrPctBW=_CesmResPartIngrPctBW_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,7),_CesmResPartIngrPctBW_Type())
cesmResPartIngrPctBW.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmResPartIngrPctBW.setStatus(_A)
class _CesmResPartEgrPctBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CesmResPartEgrPctBW_Type.__name__=_C
_CesmResPartEgrPctBW_Object=MibTableColumn
cesmResPartEgrPctBW=_CesmResPartEgrPctBW_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,8),_CesmResPartEgrPctBW_Type())
cesmResPartEgrPctBW.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmResPartEgrPctBW.setStatus(_A)
class _CesmResPartCtrlrID_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CesmResPartCtrlrID_Type.__name__=_C
_CesmResPartCtrlrID_Object=MibTableColumn
cesmResPartCtrlrID=_CesmResPartCtrlrID_Object((1,3,6,1,4,1,351,110,5,3,1,2,1,1,9),_CesmResPartCtrlrID_Type())
cesmResPartCtrlrID.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmResPartCtrlrID.setStatus(_A)
_CwcRsrcPartMIBConformance_ObjectIdentity=ObjectIdentity
cwcRsrcPartMIBConformance=_CwcRsrcPartMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,41,2))
_CwcRsrcPartMIBCompliances_ObjectIdentity=ObjectIdentity
cwcRsrcPartMIBCompliances=_CwcRsrcPartMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,41,2,1))
_CwcRsrcPartMIBGroups_ObjectIdentity=ObjectIdentity
cwcRsrcPartMIBGroups=_CwcRsrcPartMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,41,2,2))
ciscoWanCesRsrcPartGroup=ObjectGroup((1,3,6,1,4,1,351,150,41,2,2,1))
ciscoWanCesRsrcPartGroup.setObjects(*((_B,_E),(_B,_F),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoWanCesRsrcPartGroup.setStatus(_A)
ciscoWanCesRsrcPartCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,41,2,1,1))
ciscoWanCesRsrcPartCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoWanCesRsrcPartCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cesmPortCnfResPartGrp':cesmPortCnfResPartGrp,'cesmPortCnfResPartGrpTable':cesmPortCnfResPartGrpTable,'cesmPortCnfResPartGrpEntry':cesmPortCnfResPartGrpEntry,_E:cesmResPartPortNum,_F:cesmResPartCtrlrNum,_H:cesmResPartRowStatus,_I:cesmResPartNumOfLcnAvail,_J:cesmResPartLcnLow,_K:cesmResPartLcnHigh,_L:cesmResPartIngrPctBW,_M:cesmResPartEgrPctBW,_N:cesmResPartCtrlrID,'ciscoWanCesRsrcPartMIB':ciscoWanCesRsrcPartMIB,'cwcRsrcPartMIBConformance':cwcRsrcPartMIBConformance,'cwcRsrcPartMIBCompliances':cwcRsrcPartMIBCompliances,'ciscoWanCesRsrcPartCompliance':ciscoWanCesRsrcPartCompliance,'cwcRsrcPartMIBGroups':cwcRsrcPartMIBGroups,_O:ciscoWanCesRsrcPartGroup})