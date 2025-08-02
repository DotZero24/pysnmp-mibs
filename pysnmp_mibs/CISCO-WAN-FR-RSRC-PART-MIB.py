_P='ciscoWanFrRsrcPartGroup'
_O='frResPartCtrlrID'
_N='frResPartEgrPctBW'
_M='frResPartIngrPctBW'
_L='frResPartDlciHigh'
_K='frResPartDlciLow'
_J='frResPartNumOfLcnAvail'
_I='frResPartRowStatus'
_H='percentage'
_G='read-only'
_F='frResPartCtrlrNum'
_E='frResPartPortNum'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-FR-RSRC-PART-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
frPortCnfResPartGrp,=mibBuilder.importSymbols('BASIS-MIB','frPortCnfResPartGrp')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanFrRsrcPartMIB=ModuleIdentity((1,3,6,1,4,1,351,150,45))
if mibBuilder.loadTexts:ciscoWanFrRsrcPartMIB.setRevisions(('2002-09-04 00:00',))
_FrPortCnfResPartGrpTable_Object=MibTable
frPortCnfResPartGrpTable=_FrPortCnfResPartGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1))
if mibBuilder.loadTexts:frPortCnfResPartGrpTable.setStatus(_A)
_FrPortCnfResPartGrpEntry_Object=MibTableRow
frPortCnfResPartGrpEntry=_FrPortCnfResPartGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1))
frPortCnfResPartGrpEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:frPortCnfResPartGrpEntry.setStatus(_A)
class _FrResPartPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrResPartPortNum_Type.__name__=_C
_FrResPartPortNum_Object=MibTableColumn
frResPartPortNum=_FrResPartPortNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,1),_FrResPartPortNum_Type())
frResPartPortNum.setMaxAccess(_G)
if mibBuilder.loadTexts:frResPartPortNum.setStatus(_A)
class _FrResPartCtrlrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('par',1),('pnni',2),('tag',3)))
_FrResPartCtrlrNum_Type.__name__=_C
_FrResPartCtrlrNum_Object=MibTableColumn
frResPartCtrlrNum=_FrResPartCtrlrNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,2),_FrResPartCtrlrNum_Type())
frResPartCtrlrNum.setMaxAccess(_G)
if mibBuilder.loadTexts:frResPartCtrlrNum.setStatus(_A)
class _FrResPartRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_FrResPartRowStatus_Type.__name__=_C
_FrResPartRowStatus_Object=MibTableColumn
frResPartRowStatus=_FrResPartRowStatus_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,3),_FrResPartRowStatus_Type())
frResPartRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:frResPartRowStatus.setStatus(_A)
class _FrResPartNumOfLcnAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000))
_FrResPartNumOfLcnAvail_Type.__name__=_C
_FrResPartNumOfLcnAvail_Object=MibTableColumn
frResPartNumOfLcnAvail=_FrResPartNumOfLcnAvail_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,4),_FrResPartNumOfLcnAvail_Type())
frResPartNumOfLcnAvail.setMaxAccess(_D)
if mibBuilder.loadTexts:frResPartNumOfLcnAvail.setStatus(_A)
class _FrResPartDlciLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388607))
_FrResPartDlciLow_Type.__name__=_C
_FrResPartDlciLow_Object=MibTableColumn
frResPartDlciLow=_FrResPartDlciLow_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,5),_FrResPartDlciLow_Type())
frResPartDlciLow.setMaxAccess(_D)
if mibBuilder.loadTexts:frResPartDlciLow.setStatus(_A)
class _FrResPartDlciHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388607))
_FrResPartDlciHigh_Type.__name__=_C
_FrResPartDlciHigh_Object=MibTableColumn
frResPartDlciHigh=_FrResPartDlciHigh_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,6),_FrResPartDlciHigh_Type())
frResPartDlciHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:frResPartDlciHigh.setStatus(_A)
class _FrResPartIngrPctBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FrResPartIngrPctBW_Type.__name__=_C
_FrResPartIngrPctBW_Object=MibTableColumn
frResPartIngrPctBW=_FrResPartIngrPctBW_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,7),_FrResPartIngrPctBW_Type())
frResPartIngrPctBW.setMaxAccess(_D)
if mibBuilder.loadTexts:frResPartIngrPctBW.setStatus(_A)
if mibBuilder.loadTexts:frResPartIngrPctBW.setUnits(_H)
class _FrResPartEgrPctBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FrResPartEgrPctBW_Type.__name__=_C
_FrResPartEgrPctBW_Object=MibTableColumn
frResPartEgrPctBW=_FrResPartEgrPctBW_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,8),_FrResPartEgrPctBW_Type())
frResPartEgrPctBW.setMaxAccess(_D)
if mibBuilder.loadTexts:frResPartEgrPctBW.setStatus(_A)
if mibBuilder.loadTexts:frResPartEgrPctBW.setUnits(_H)
class _FrResPartCtrlrID_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrResPartCtrlrID_Type.__name__=_C
_FrResPartCtrlrID_Object=MibTableColumn
frResPartCtrlrID=_FrResPartCtrlrID_Object((1,3,6,1,4,1,351,110,5,1,1,1,5,1,1,9),_FrResPartCtrlrID_Type())
frResPartCtrlrID.setMaxAccess(_D)
if mibBuilder.loadTexts:frResPartCtrlrID.setStatus(_A)
_CwfRsrcPartMIBConformance_ObjectIdentity=ObjectIdentity
cwfRsrcPartMIBConformance=_CwfRsrcPartMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,45,2))
_CwfRsrcPartMIBCompliances_ObjectIdentity=ObjectIdentity
cwfRsrcPartMIBCompliances=_CwfRsrcPartMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,45,2,1))
_CwfRsrcPartMIBGroups_ObjectIdentity=ObjectIdentity
cwfRsrcPartMIBGroups=_CwfRsrcPartMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,45,2,2))
ciscoWanFrRsrcPartGroup=ObjectGroup((1,3,6,1,4,1,351,150,45,2,2,1))
ciscoWanFrRsrcPartGroup.setObjects(*((_B,_E),(_B,_F),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoWanFrRsrcPartGroup.setStatus(_A)
ciscoWanFrRsrcPartCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,45,2,1,1))
ciscoWanFrRsrcPartCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:ciscoWanFrRsrcPartCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'frPortCnfResPartGrpTable':frPortCnfResPartGrpTable,'frPortCnfResPartGrpEntry':frPortCnfResPartGrpEntry,_E:frResPartPortNum,_F:frResPartCtrlrNum,_I:frResPartRowStatus,_J:frResPartNumOfLcnAvail,_K:frResPartDlciLow,_L:frResPartDlciHigh,_M:frResPartIngrPctBW,_N:frResPartEgrPctBW,_O:frResPartCtrlrID,'ciscoWanFrRsrcPartMIB':ciscoWanFrRsrcPartMIB,'cwfRsrcPartMIBConformance':cwfRsrcPartMIBConformance,'cwfRsrcPartMIBCompliances':cwfRsrcPartMIBCompliances,'ciscoWanFrRsrcPartCompliance':ciscoWanFrRsrcPartCompliance,'cwfRsrcPartMIBGroups':cwfRsrcPartMIBGroups,_P:ciscoWanFrRsrcPartGroup})