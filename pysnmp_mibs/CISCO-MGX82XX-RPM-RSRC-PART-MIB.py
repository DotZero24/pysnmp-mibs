_P='cmrRsrcPartMIBGroup'
_O='rpmIfRscPrtMaxChans'
_N='rpmIfRscPrtVciHigh'
_M='rpmIfRscPrtVciLow'
_L='rpmIfRscPrtVpiHigh'
_K='rpmIfRscPrtVpiLow'
_J='rpmIfRscPrtEgrPctBandwidth'
_I='rpmIfRscPrtIngrPctBandwidth'
_H='rpmIfRscPrtRowStatus'
_G='rpmIfRscPartCtrlrNum'
_F='rpmIfRscPartIfNum'
_E='rpmIfRscSlotNum'
_D='read-only'
_C='Integer32'
_B='current'
_A='CISCO-MGX82XX-RPM-RSRC-PART-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rpmInterface,=mibBuilder.importSymbols('BASIS-MIB','rpmInterface')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxRpmRsrcPartMIB=ModuleIdentity((1,3,6,1,4,1,351,150,61))
if mibBuilder.loadTexts:ciscoMgx82xxRpmRsrcPartMIB.setRevisions(('2002-09-17 00:00',))
_RpmIfCnfResPart_ObjectIdentity=ObjectIdentity
rpmIfCnfResPart=_RpmIfCnfResPart_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,9,2))
_RpmIfCnfRscPartTable_Object=MibTable
rpmIfCnfRscPartTable=_RpmIfCnfRscPartTable_Object((1,3,6,1,4,1,351,110,5,2,9,2,1))
if mibBuilder.loadTexts:rpmIfCnfRscPartTable.setStatus(_B)
_RpmIfCnfRscPartEntry_Object=MibTableRow
rpmIfCnfRscPartEntry=_RpmIfCnfRscPartEntry_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1))
rpmIfCnfRscPartEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G))
if mibBuilder.loadTexts:rpmIfCnfRscPartEntry.setStatus(_B)
class _RpmIfRscSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_RpmIfRscSlotNum_Type.__name__=_C
_RpmIfRscSlotNum_Object=MibTableColumn
rpmIfRscSlotNum=_RpmIfRscSlotNum_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,1),_RpmIfRscSlotNum_Type())
rpmIfRscSlotNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscSlotNum.setStatus(_B)
class _RpmIfRscPartIfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpmIfRscPartIfNum_Type.__name__=_C
_RpmIfRscPartIfNum_Object=MibTableColumn
rpmIfRscPartIfNum=_RpmIfRscPartIfNum_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,2),_RpmIfRscPartIfNum_Type())
rpmIfRscPartIfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPartIfNum.setStatus(_B)
class _RpmIfRscPartCtrlrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('par',1),('pnni',2),('tag',3)))
_RpmIfRscPartCtrlrNum_Type.__name__=_C
_RpmIfRscPartCtrlrNum_Object=MibTableColumn
rpmIfRscPartCtrlrNum=_RpmIfRscPartCtrlrNum_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,3),_RpmIfRscPartCtrlrNum_Type())
rpmIfRscPartCtrlrNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPartCtrlrNum.setStatus(_B)
class _RpmIfRscPrtRowStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_RpmIfRscPrtRowStatus_Type.__name__=_C
_RpmIfRscPrtRowStatus_Object=MibTableColumn
rpmIfRscPrtRowStatus=_RpmIfRscPrtRowStatus_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,4),_RpmIfRscPrtRowStatus_Type())
rpmIfRscPrtRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPrtRowStatus.setStatus(_B)
class _RpmIfRscPrtIngrPctBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RpmIfRscPrtIngrPctBandwidth_Type.__name__=_C
_RpmIfRscPrtIngrPctBandwidth_Object=MibTableColumn
rpmIfRscPrtIngrPctBandwidth=_RpmIfRscPrtIngrPctBandwidth_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,5),_RpmIfRscPrtIngrPctBandwidth_Type())
rpmIfRscPrtIngrPctBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPrtIngrPctBandwidth.setStatus(_B)
class _RpmIfRscPrtEgrPctBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RpmIfRscPrtEgrPctBandwidth_Type.__name__=_C
_RpmIfRscPrtEgrPctBandwidth_Object=MibTableColumn
rpmIfRscPrtEgrPctBandwidth=_RpmIfRscPrtEgrPctBandwidth_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,6),_RpmIfRscPrtEgrPctBandwidth_Type())
rpmIfRscPrtEgrPctBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPrtEgrPctBandwidth.setStatus(_B)
class _RpmIfRscPrtVpiLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RpmIfRscPrtVpiLow_Type.__name__=_C
_RpmIfRscPrtVpiLow_Object=MibTableColumn
rpmIfRscPrtVpiLow=_RpmIfRscPrtVpiLow_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,7),_RpmIfRscPrtVpiLow_Type())
rpmIfRscPrtVpiLow.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPrtVpiLow.setStatus(_B)
class _RpmIfRscPrtVpiHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RpmIfRscPrtVpiHigh_Type.__name__=_C
_RpmIfRscPrtVpiHigh_Object=MibTableColumn
rpmIfRscPrtVpiHigh=_RpmIfRscPrtVpiHigh_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,8),_RpmIfRscPrtVpiHigh_Type())
rpmIfRscPrtVpiHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPrtVpiHigh.setStatus(_B)
class _RpmIfRscPrtVciLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RpmIfRscPrtVciLow_Type.__name__=_C
_RpmIfRscPrtVciLow_Object=MibTableColumn
rpmIfRscPrtVciLow=_RpmIfRscPrtVciLow_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,9),_RpmIfRscPrtVciLow_Type())
rpmIfRscPrtVciLow.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPrtVciLow.setStatus(_B)
class _RpmIfRscPrtVciHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RpmIfRscPrtVciHigh_Type.__name__=_C
_RpmIfRscPrtVciHigh_Object=MibTableColumn
rpmIfRscPrtVciHigh=_RpmIfRscPrtVciHigh_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,10),_RpmIfRscPrtVciHigh_Type())
rpmIfRscPrtVciHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPrtVciHigh.setStatus(_B)
class _RpmIfRscPrtMaxChans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4047))
_RpmIfRscPrtMaxChans_Type.__name__=_C
_RpmIfRscPrtMaxChans_Object=MibTableColumn
rpmIfRscPrtMaxChans=_RpmIfRscPrtMaxChans_Object((1,3,6,1,4,1,351,110,5,2,9,2,1,1,11),_RpmIfRscPrtMaxChans_Type())
rpmIfRscPrtMaxChans.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmIfRscPrtMaxChans.setStatus(_B)
_CmrRsrcPartMIBConformance_ObjectIdentity=ObjectIdentity
cmrRsrcPartMIBConformance=_CmrRsrcPartMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,61,3))
_CmrRsrcPartMIBCompliances_ObjectIdentity=ObjectIdentity
cmrRsrcPartMIBCompliances=_CmrRsrcPartMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,61,3,1))
_CmrRsrcPartMIBGroups_ObjectIdentity=ObjectIdentity
cmrRsrcPartMIBGroups=_CmrRsrcPartMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,61,3,2))
cmrRsrcPartMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,61,3,2,1))
cmrRsrcPartMIBGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:cmrRsrcPartMIBGroup.setStatus(_B)
cmrRsrcPartMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,61,3,1,1))
cmrRsrcPartMIBCompliance.setObjects((_A,_P))
if mibBuilder.loadTexts:cmrRsrcPartMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rpmIfCnfResPart':rpmIfCnfResPart,'rpmIfCnfRscPartTable':rpmIfCnfRscPartTable,'rpmIfCnfRscPartEntry':rpmIfCnfRscPartEntry,_E:rpmIfRscSlotNum,_F:rpmIfRscPartIfNum,_G:rpmIfRscPartCtrlrNum,_H:rpmIfRscPrtRowStatus,_I:rpmIfRscPrtIngrPctBandwidth,_J:rpmIfRscPrtEgrPctBandwidth,_K:rpmIfRscPrtVpiLow,_L:rpmIfRscPrtVpiHigh,_M:rpmIfRscPrtVciLow,_N:rpmIfRscPrtVciHigh,_O:rpmIfRscPrtMaxChans,'ciscoMgx82xxRpmRsrcPartMIB':ciscoMgx82xxRpmRsrcPartMIB,'cmrRsrcPartMIBConformance':cmrRsrcPartMIBConformance,'cmrRsrcPartMIBCompliances':cmrRsrcPartMIBCompliances,'cmrRsrcPartMIBCompliance':cmrRsrcPartMIBCompliance,'cmrRsrcPartMIBGroups':cmrRsrcPartMIBGroups,_P:cmrRsrcPartMIBGroup})