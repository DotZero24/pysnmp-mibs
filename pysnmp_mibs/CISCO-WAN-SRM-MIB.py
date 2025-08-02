_T='ciscoWanSrmeConfGroup'
_S='ciscoWanSrmConfGroup'
_R='srmeVtFramingType'
_Q='srmeTargetSlotLineNum'
_P='srmeTargetSlotNum'
_O='srmeRowStatus'
_N='srmTargetSlotLineNum'
_M='srmTargetSlotNum'
_L='srmT1RowStatus'
_K='modify'
_J='delete'
_I='srmeStartVtNum'
_H='srmeLineNum'
_G='srmStartT1LineNum'
_F='srmT3LineNum'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-SRM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardSpecific,=mibBuilder.importSymbols('BASIS-MIB','cardSpecific')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanSrmMIB=ModuleIdentity((1,3,6,1,4,1,351,150,30))
if mibBuilder.loadTexts:ciscoWanSrmMIB.setRevisions(('2002-08-26 00:00',))
_Srm3T3CnfGrp_ObjectIdentity=ObjectIdentity
srm3T3CnfGrp=_Srm3T3CnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,3,10))
_Srm3T3CnfGrpTable_Object=MibTable
srm3T3CnfGrpTable=_Srm3T3CnfGrpTable_Object((1,3,6,1,4,1,351,110,3,10,1))
if mibBuilder.loadTexts:srm3T3CnfGrpTable.setStatus(_A)
_Srm3T3CnfGrpEntry_Object=MibTableRow
srm3T3CnfGrpEntry=_Srm3T3CnfGrpEntry_Object((1,3,6,1,4,1,351,110,3,10,1,1))
srm3T3CnfGrpEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:srm3T3CnfGrpEntry.setStatus(_A)
class _SrmT3LineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SrmT3LineNum_Type.__name__=_C
_SrmT3LineNum_Object=MibTableColumn
srmT3LineNum=_SrmT3LineNum_Object((1,3,6,1,4,1,351,110,3,10,1,1,1),_SrmT3LineNum_Type())
srmT3LineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:srmT3LineNum.setStatus(_A)
class _SrmStartT1LineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_SrmStartT1LineNum_Type.__name__=_C
_SrmStartT1LineNum_Object=MibTableColumn
srmStartT1LineNum=_SrmStartT1LineNum_Object((1,3,6,1,4,1,351,110,3,10,1,1,2),_SrmStartT1LineNum_Type())
srmStartT1LineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:srmStartT1LineNum.setStatus(_A)
class _SrmT1RowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),(_J,2),(_K,3)))
_SrmT1RowStatus_Type.__name__=_C
_SrmT1RowStatus_Object=MibTableColumn
srmT1RowStatus=_SrmT1RowStatus_Object((1,3,6,1,4,1,351,110,3,10,1,1,3),_SrmT1RowStatus_Type())
srmT1RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:srmT1RowStatus.setStatus(_A)
class _SrmTargetSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SrmTargetSlotNum_Type.__name__=_C
_SrmTargetSlotNum_Object=MibTableColumn
srmTargetSlotNum=_SrmTargetSlotNum_Object((1,3,6,1,4,1,351,110,3,10,1,1,4),_SrmTargetSlotNum_Type())
srmTargetSlotNum.setMaxAccess(_D)
if mibBuilder.loadTexts:srmTargetSlotNum.setStatus(_A)
class _SrmTargetSlotLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SrmTargetSlotLineNum_Type.__name__=_C
_SrmTargetSlotLineNum_Object=MibTableColumn
srmTargetSlotLineNum=_SrmTargetSlotLineNum_Object((1,3,6,1,4,1,351,110,3,10,1,1,5),_SrmTargetSlotLineNum_Type())
srmTargetSlotLineNum.setMaxAccess(_D)
if mibBuilder.loadTexts:srmTargetSlotLineNum.setStatus(_A)
_SrmeCnfGrp_ObjectIdentity=ObjectIdentity
srmeCnfGrp=_SrmeCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,3,22))
_SrmeCnfGrpTable_Object=MibTable
srmeCnfGrpTable=_SrmeCnfGrpTable_Object((1,3,6,1,4,1,351,110,3,22,1))
if mibBuilder.loadTexts:srmeCnfGrpTable.setStatus(_A)
_SrmeCnfGrpEntry_Object=MibTableRow
srmeCnfGrpEntry=_SrmeCnfGrpEntry_Object((1,3,6,1,4,1,351,110,3,22,1,1))
srmeCnfGrpEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:srmeCnfGrpEntry.setStatus(_A)
class _SrmeLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SrmeLineNum_Type.__name__=_C
_SrmeLineNum_Object=MibTableColumn
srmeLineNum=_SrmeLineNum_Object((1,3,6,1,4,1,351,110,3,22,1,1,1),_SrmeLineNum_Type())
srmeLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:srmeLineNum.setStatus(_A)
class _SrmeStartVtNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,84))
_SrmeStartVtNum_Type.__name__=_C
_SrmeStartVtNum_Object=MibTableColumn
srmeStartVtNum=_SrmeStartVtNum_Object((1,3,6,1,4,1,351,110,3,22,1,1,2),_SrmeStartVtNum_Type())
srmeStartVtNum.setMaxAccess(_E)
if mibBuilder.loadTexts:srmeStartVtNum.setStatus(_A)
class _SrmeRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),(_J,2),(_K,3)))
_SrmeRowStatus_Type.__name__=_C
_SrmeRowStatus_Object=MibTableColumn
srmeRowStatus=_SrmeRowStatus_Object((1,3,6,1,4,1,351,110,3,22,1,1,3),_SrmeRowStatus_Type())
srmeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:srmeRowStatus.setStatus(_A)
class _SrmeTargetSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SrmeTargetSlotNum_Type.__name__=_C
_SrmeTargetSlotNum_Object=MibTableColumn
srmeTargetSlotNum=_SrmeTargetSlotNum_Object((1,3,6,1,4,1,351,110,3,22,1,1,4),_SrmeTargetSlotNum_Type())
srmeTargetSlotNum.setMaxAccess(_D)
if mibBuilder.loadTexts:srmeTargetSlotNum.setStatus(_A)
class _SrmeTargetSlotLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SrmeTargetSlotLineNum_Type.__name__=_C
_SrmeTargetSlotLineNum_Object=MibTableColumn
srmeTargetSlotLineNum=_SrmeTargetSlotLineNum_Object((1,3,6,1,4,1,351,110,3,22,1,1,5),_SrmeTargetSlotLineNum_Type())
srmeTargetSlotLineNum.setMaxAccess(_D)
if mibBuilder.loadTexts:srmeTargetSlotLineNum.setStatus(_A)
class _SrmeVtFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('sf',2),('esf',3)))
_SrmeVtFramingType_Type.__name__=_C
_SrmeVtFramingType_Object=MibTableColumn
srmeVtFramingType=_SrmeVtFramingType_Object((1,3,6,1,4,1,351,110,3,22,1,1,6),_SrmeVtFramingType_Type())
srmeVtFramingType.setMaxAccess(_D)
if mibBuilder.loadTexts:srmeVtFramingType.setStatus(_A)
_CiscoWanSrmMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanSrmMIBConformance=_CiscoWanSrmMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,30,2))
_CiscoWanSrmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanSrmMIBGroups=_CiscoWanSrmMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,30,2,1))
_CiscoWanSrmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanSrmMIBCompliances=_CiscoWanSrmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,30,2,2))
ciscoWanSrmConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,30,2,1,1))
ciscoWanSrmConfGroup.setObjects(*((_B,_F),(_B,_G),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoWanSrmConfGroup.setStatus(_A)
ciscoWanSrmeConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,30,2,1,2))
ciscoWanSrmeConfGroup.setObjects(*((_B,_H),(_B,_I),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoWanSrmeConfGroup.setStatus(_A)
ciscoWanSrmCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,30,2,2,1))
ciscoWanSrmCompliance.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoWanSrmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'srm3T3CnfGrp':srm3T3CnfGrp,'srm3T3CnfGrpTable':srm3T3CnfGrpTable,'srm3T3CnfGrpEntry':srm3T3CnfGrpEntry,_F:srmT3LineNum,_G:srmStartT1LineNum,_L:srmT1RowStatus,_M:srmTargetSlotNum,_N:srmTargetSlotLineNum,'srmeCnfGrp':srmeCnfGrp,'srmeCnfGrpTable':srmeCnfGrpTable,'srmeCnfGrpEntry':srmeCnfGrpEntry,_H:srmeLineNum,_I:srmeStartVtNum,_O:srmeRowStatus,_P:srmeTargetSlotNum,_Q:srmeTargetSlotLineNum,_R:srmeVtFramingType,'ciscoWanSrmMIB':ciscoWanSrmMIB,'ciscoWanSrmMIBConformance':ciscoWanSrmMIBConformance,'ciscoWanSrmMIBGroups':ciscoWanSrmMIBGroups,_S:ciscoWanSrmConfGroup,_T:ciscoWanSrmeConfGroup,'ciscoWanSrmMIBCompliances':ciscoWanSrmMIBCompliances,'ciscoWanSrmCompliance':ciscoWanSrmCompliance})