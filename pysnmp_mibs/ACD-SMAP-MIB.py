_l='acdSmapPortCoSMapGroup'
_k='acdSmapPortCoSEncodeDeiGroup'
_j='acdSmapRegSetCodePointGroup'
_i='acdSmapRegSetGroup'
_h='acdSmapCoSProfCodePointGroup'
_g='acdSmapCoSProfGroup'
_f='acdSmapPortCoSMapYellowOut'
_e='acdSmapPortCoSMapGreenOut'
_d='acdSmapPortCoSMapCosIn'
_c='acdSmapPortCoSEncodeDeiEnable'
_b='acdSmapRegSetCodePointRegulatorEnable'
_a='acdSmapRegSetCodePointRegulatorID'
_Z='acdSmapRegSetType'
_Y='acdSmapRegSetName'
_X='acdSmapRegSetRowStatus'
_W='acdSmapCoSProfCodePointYellowOut'
_V='acdSmapCoSProfCodePointGreenOut'
_U='acdSmapCoSProfCodePointPreMarkingColor'
_T='acdSmapCoSProfEncodeDropBit'
_S='acdSmapCoSProfDecodeDropBit'
_R='acdSmapCoSProfType'
_Q='acdSmapCoSProfName'
_P='acdSmapCoSProfRowStatus'
_O='acdSmapPortCoSMapID'
_N='acdSmapRegSetCodePointID'
_M='acdSmapCoSProfCodePointID'
_L='acdSmapPortCoSPortID'
_K='acdSmapRegSetID'
_J='acdSmapCoSProfID'
_I='DisplayString'
_H='TruthValue'
_G='Integer32'
_F='not-accessible'
_E='read-write'
_D='read-create'
_C='Unsigned32'
_B='ACD-SMAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acdMibs,=mibBuilder.importSymbols('ACCEDIAN-SMI','acdMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention',_H)
acdSmap=ModuleIdentity((1,3,6,1,4,1,22420,2,8))
if mibBuilder.loadTexts:acdSmap.setRevisions(('2013-05-11 01:00','2008-10-01 01:00','2008-06-15 01:00'))
_AcdSmapNotifications_ObjectIdentity=ObjectIdentity
acdSmapNotifications=_AcdSmapNotifications_ObjectIdentity((1,3,6,1,4,1,22420,2,8,0))
_AcdSmapMIBObjects_ObjectIdentity=ObjectIdentity
acdSmapMIBObjects=_AcdSmapMIBObjects_ObjectIdentity((1,3,6,1,4,1,22420,2,8,1))
_AcdSmapConfig_ObjectIdentity=ObjectIdentity
acdSmapConfig=_AcdSmapConfig_ObjectIdentity((1,3,6,1,4,1,22420,2,8,1,1))
_AcdSmapCoSProfTable_Object=MibTable
acdSmapCoSProfTable=_AcdSmapCoSProfTable_Object((1,3,6,1,4,1,22420,2,8,1,1,1))
if mibBuilder.loadTexts:acdSmapCoSProfTable.setStatus(_A)
_AcdSmapCoSProfEntry_Object=MibTableRow
acdSmapCoSProfEntry=_AcdSmapCoSProfEntry_Object((1,3,6,1,4,1,22420,2,8,1,1,1,1))
acdSmapCoSProfEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:acdSmapCoSProfEntry.setStatus(_A)
_AcdSmapCoSProfID_Type=Unsigned32
_AcdSmapCoSProfID_Object=MibTableColumn
acdSmapCoSProfID=_AcdSmapCoSProfID_Object((1,3,6,1,4,1,22420,2,8,1,1,1,1,1),_AcdSmapCoSProfID_Type())
acdSmapCoSProfID.setMaxAccess(_F)
if mibBuilder.loadTexts:acdSmapCoSProfID.setStatus(_A)
_AcdSmapCoSProfRowStatus_Type=RowStatus
_AcdSmapCoSProfRowStatus_Object=MibTableColumn
acdSmapCoSProfRowStatus=_AcdSmapCoSProfRowStatus_Object((1,3,6,1,4,1,22420,2,8,1,1,1,1,2),_AcdSmapCoSProfRowStatus_Type())
acdSmapCoSProfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:acdSmapCoSProfRowStatus.setStatus(_A)
class _AcdSmapCoSProfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AcdSmapCoSProfName_Type.__name__=_I
_AcdSmapCoSProfName_Object=MibTableColumn
acdSmapCoSProfName=_AcdSmapCoSProfName_Object((1,3,6,1,4,1,22420,2,8,1,1,1,1,3),_AcdSmapCoSProfName_Type())
acdSmapCoSProfName.setMaxAccess(_D)
if mibBuilder.loadTexts:acdSmapCoSProfName.setStatus(_A)
class _AcdSmapCoSProfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pcp',1),('dscp',2),('pre',3)))
_AcdSmapCoSProfType_Type.__name__=_G
_AcdSmapCoSProfType_Object=MibTableColumn
acdSmapCoSProfType=_AcdSmapCoSProfType_Object((1,3,6,1,4,1,22420,2,8,1,1,1,1,4),_AcdSmapCoSProfType_Type())
acdSmapCoSProfType.setMaxAccess(_D)
if mibBuilder.loadTexts:acdSmapCoSProfType.setStatus(_A)
class _AcdSmapCoSProfDecodeDropBit_Type(TruthValue):defaultValue=2
_AcdSmapCoSProfDecodeDropBit_Type.__name__=_H
_AcdSmapCoSProfDecodeDropBit_Object=MibTableColumn
acdSmapCoSProfDecodeDropBit=_AcdSmapCoSProfDecodeDropBit_Object((1,3,6,1,4,1,22420,2,8,1,1,1,1,5),_AcdSmapCoSProfDecodeDropBit_Type())
acdSmapCoSProfDecodeDropBit.setMaxAccess(_D)
if mibBuilder.loadTexts:acdSmapCoSProfDecodeDropBit.setStatus(_A)
class _AcdSmapCoSProfEncodeDropBit_Type(TruthValue):defaultValue=2
_AcdSmapCoSProfEncodeDropBit_Type.__name__=_H
_AcdSmapCoSProfEncodeDropBit_Object=MibTableColumn
acdSmapCoSProfEncodeDropBit=_AcdSmapCoSProfEncodeDropBit_Object((1,3,6,1,4,1,22420,2,8,1,1,1,1,6),_AcdSmapCoSProfEncodeDropBit_Type())
acdSmapCoSProfEncodeDropBit.setMaxAccess(_D)
if mibBuilder.loadTexts:acdSmapCoSProfEncodeDropBit.setStatus(_A)
_AcdSmapCoSProfCodePointTable_Object=MibTable
acdSmapCoSProfCodePointTable=_AcdSmapCoSProfCodePointTable_Object((1,3,6,1,4,1,22420,2,8,1,1,2))
if mibBuilder.loadTexts:acdSmapCoSProfCodePointTable.setStatus(_A)
_AcdSmapCoSProfCodePointEntry_Object=MibTableRow
acdSmapCoSProfCodePointEntry=_AcdSmapCoSProfCodePointEntry_Object((1,3,6,1,4,1,22420,2,8,1,1,2,1))
acdSmapCoSProfCodePointEntry.setIndexNames((0,_B,_J),(0,_B,_M))
if mibBuilder.loadTexts:acdSmapCoSProfCodePointEntry.setStatus(_A)
class _AcdSmapCoSProfCodePointID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AcdSmapCoSProfCodePointID_Type.__name__=_C
_AcdSmapCoSProfCodePointID_Object=MibTableColumn
acdSmapCoSProfCodePointID=_AcdSmapCoSProfCodePointID_Object((1,3,6,1,4,1,22420,2,8,1,1,2,1,1),_AcdSmapCoSProfCodePointID_Type())
acdSmapCoSProfCodePointID.setMaxAccess(_F)
if mibBuilder.loadTexts:acdSmapCoSProfCodePointID.setStatus(_A)
class _AcdSmapCoSProfCodePointPreMarkingColor_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('green',1),('yellow',2)))
_AcdSmapCoSProfCodePointPreMarkingColor_Type.__name__=_G
_AcdSmapCoSProfCodePointPreMarkingColor_Object=MibTableColumn
acdSmapCoSProfCodePointPreMarkingColor=_AcdSmapCoSProfCodePointPreMarkingColor_Object((1,3,6,1,4,1,22420,2,8,1,1,2,1,2),_AcdSmapCoSProfCodePointPreMarkingColor_Type())
acdSmapCoSProfCodePointPreMarkingColor.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSmapCoSProfCodePointPreMarkingColor.setStatus(_A)
class _AcdSmapCoSProfCodePointGreenOut_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcdSmapCoSProfCodePointGreenOut_Type.__name__=_C
_AcdSmapCoSProfCodePointGreenOut_Object=MibTableColumn
acdSmapCoSProfCodePointGreenOut=_AcdSmapCoSProfCodePointGreenOut_Object((1,3,6,1,4,1,22420,2,8,1,1,2,1,3),_AcdSmapCoSProfCodePointGreenOut_Type())
acdSmapCoSProfCodePointGreenOut.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSmapCoSProfCodePointGreenOut.setStatus(_A)
class _AcdSmapCoSProfCodePointYellowOut_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcdSmapCoSProfCodePointYellowOut_Type.__name__=_C
_AcdSmapCoSProfCodePointYellowOut_Object=MibTableColumn
acdSmapCoSProfCodePointYellowOut=_AcdSmapCoSProfCodePointYellowOut_Object((1,3,6,1,4,1,22420,2,8,1,1,2,1,4),_AcdSmapCoSProfCodePointYellowOut_Type())
acdSmapCoSProfCodePointYellowOut.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSmapCoSProfCodePointYellowOut.setStatus(_A)
_AcdSmapRegSetTable_Object=MibTable
acdSmapRegSetTable=_AcdSmapRegSetTable_Object((1,3,6,1,4,1,22420,2,8,1,1,3))
if mibBuilder.loadTexts:acdSmapRegSetTable.setStatus(_A)
_AcdSmapRegSetEntry_Object=MibTableRow
acdSmapRegSetEntry=_AcdSmapRegSetEntry_Object((1,3,6,1,4,1,22420,2,8,1,1,3,1))
acdSmapRegSetEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:acdSmapRegSetEntry.setStatus(_A)
_AcdSmapRegSetID_Type=Unsigned32
_AcdSmapRegSetID_Object=MibTableColumn
acdSmapRegSetID=_AcdSmapRegSetID_Object((1,3,6,1,4,1,22420,2,8,1,1,3,1,1),_AcdSmapRegSetID_Type())
acdSmapRegSetID.setMaxAccess(_F)
if mibBuilder.loadTexts:acdSmapRegSetID.setStatus(_A)
_AcdSmapRegSetRowStatus_Type=RowStatus
_AcdSmapRegSetRowStatus_Object=MibTableColumn
acdSmapRegSetRowStatus=_AcdSmapRegSetRowStatus_Object((1,3,6,1,4,1,22420,2,8,1,1,3,1,2),_AcdSmapRegSetRowStatus_Type())
acdSmapRegSetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:acdSmapRegSetRowStatus.setStatus(_A)
class _AcdSmapRegSetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AcdSmapRegSetName_Type.__name__=_I
_AcdSmapRegSetName_Object=MibTableColumn
acdSmapRegSetName=_AcdSmapRegSetName_Object((1,3,6,1,4,1,22420,2,8,1,1,3,1,3),_AcdSmapRegSetName_Type())
acdSmapRegSetName.setMaxAccess(_D)
if mibBuilder.loadTexts:acdSmapRegSetName.setStatus(_A)
class _AcdSmapRegSetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pcp',1),('dscp',2),('pre',3)))
_AcdSmapRegSetType_Type.__name__=_G
_AcdSmapRegSetType_Object=MibTableColumn
acdSmapRegSetType=_AcdSmapRegSetType_Object((1,3,6,1,4,1,22420,2,8,1,1,3,1,4),_AcdSmapRegSetType_Type())
acdSmapRegSetType.setMaxAccess(_D)
if mibBuilder.loadTexts:acdSmapRegSetType.setStatus(_A)
_AcdSmapRegSetCodePointTable_Object=MibTable
acdSmapRegSetCodePointTable=_AcdSmapRegSetCodePointTable_Object((1,3,6,1,4,1,22420,2,8,1,1,4))
if mibBuilder.loadTexts:acdSmapRegSetCodePointTable.setStatus(_A)
_AcdSmapRegSetCodePointEntry_Object=MibTableRow
acdSmapRegSetCodePointEntry=_AcdSmapRegSetCodePointEntry_Object((1,3,6,1,4,1,22420,2,8,1,1,4,1))
acdSmapRegSetCodePointEntry.setIndexNames((0,_B,_K),(0,_B,_N))
if mibBuilder.loadTexts:acdSmapRegSetCodePointEntry.setStatus(_A)
class _AcdSmapRegSetCodePointID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AcdSmapRegSetCodePointID_Type.__name__=_C
_AcdSmapRegSetCodePointID_Object=MibTableColumn
acdSmapRegSetCodePointID=_AcdSmapRegSetCodePointID_Object((1,3,6,1,4,1,22420,2,8,1,1,4,1,1),_AcdSmapRegSetCodePointID_Type())
acdSmapRegSetCodePointID.setMaxAccess(_F)
if mibBuilder.loadTexts:acdSmapRegSetCodePointID.setStatus(_A)
class _AcdSmapRegSetCodePointRegulatorID_Type(Unsigned32):defaultValue=0
_AcdSmapRegSetCodePointRegulatorID_Type.__name__=_C
_AcdSmapRegSetCodePointRegulatorID_Object=MibTableColumn
acdSmapRegSetCodePointRegulatorID=_AcdSmapRegSetCodePointRegulatorID_Object((1,3,6,1,4,1,22420,2,8,1,1,4,1,2),_AcdSmapRegSetCodePointRegulatorID_Type())
acdSmapRegSetCodePointRegulatorID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSmapRegSetCodePointRegulatorID.setStatus(_A)
class _AcdSmapRegSetCodePointRegulatorEnable_Type(TruthValue):defaultValue=2
_AcdSmapRegSetCodePointRegulatorEnable_Type.__name__=_H
_AcdSmapRegSetCodePointRegulatorEnable_Object=MibTableColumn
acdSmapRegSetCodePointRegulatorEnable=_AcdSmapRegSetCodePointRegulatorEnable_Object((1,3,6,1,4,1,22420,2,8,1,1,4,1,3),_AcdSmapRegSetCodePointRegulatorEnable_Type())
acdSmapRegSetCodePointRegulatorEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSmapRegSetCodePointRegulatorEnable.setStatus(_A)
_AcdSmapPortCoSEncodeDeiTable_Object=MibTable
acdSmapPortCoSEncodeDeiTable=_AcdSmapPortCoSEncodeDeiTable_Object((1,3,6,1,4,1,22420,2,8,1,1,5))
if mibBuilder.loadTexts:acdSmapPortCoSEncodeDeiTable.setStatus(_A)
_AcdSmapPortCoSEncodeDeiEntry_Object=MibTableRow
acdSmapPortCoSEncodeDeiEntry=_AcdSmapPortCoSEncodeDeiEntry_Object((1,3,6,1,4,1,22420,2,8,1,1,5,1))
acdSmapPortCoSEncodeDeiEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:acdSmapPortCoSEncodeDeiEntry.setStatus(_A)
_AcdSmapPortCoSPortID_Type=Unsigned32
_AcdSmapPortCoSPortID_Object=MibTableColumn
acdSmapPortCoSPortID=_AcdSmapPortCoSPortID_Object((1,3,6,1,4,1,22420,2,8,1,1,5,1,1),_AcdSmapPortCoSPortID_Type())
acdSmapPortCoSPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:acdSmapPortCoSPortID.setStatus(_A)
class _AcdSmapPortCoSEncodeDeiEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('enable',0),('disable',1)))
_AcdSmapPortCoSEncodeDeiEnable_Type.__name__=_G
_AcdSmapPortCoSEncodeDeiEnable_Object=MibTableColumn
acdSmapPortCoSEncodeDeiEnable=_AcdSmapPortCoSEncodeDeiEnable_Object((1,3,6,1,4,1,22420,2,8,1,1,5,1,2),_AcdSmapPortCoSEncodeDeiEnable_Type())
acdSmapPortCoSEncodeDeiEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSmapPortCoSEncodeDeiEnable.setStatus(_A)
_AcdSmapPortCoSMapTable_Object=MibTable
acdSmapPortCoSMapTable=_AcdSmapPortCoSMapTable_Object((1,3,6,1,4,1,22420,2,8,1,1,6))
if mibBuilder.loadTexts:acdSmapPortCoSMapTable.setStatus(_A)
_AcdSmapPortCoSMapEntry_Object=MibTableRow
acdSmapPortCoSMapEntry=_AcdSmapPortCoSMapEntry_Object((1,3,6,1,4,1,22420,2,8,1,1,6,1))
acdSmapPortCoSMapEntry.setIndexNames((0,_B,_L),(0,_B,_O))
if mibBuilder.loadTexts:acdSmapPortCoSMapEntry.setStatus(_A)
class _AcdSmapPortCoSMapID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AcdSmapPortCoSMapID_Type.__name__=_C
_AcdSmapPortCoSMapID_Object=MibTableColumn
acdSmapPortCoSMapID=_AcdSmapPortCoSMapID_Object((1,3,6,1,4,1,22420,2,8,1,1,6,1,1),_AcdSmapPortCoSMapID_Type())
acdSmapPortCoSMapID.setMaxAccess(_F)
if mibBuilder.loadTexts:acdSmapPortCoSMapID.setStatus(_A)
class _AcdSmapPortCoSMapCosIn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcdSmapPortCoSMapCosIn_Type.__name__=_C
_AcdSmapPortCoSMapCosIn_Object=MibTableColumn
acdSmapPortCoSMapCosIn=_AcdSmapPortCoSMapCosIn_Object((1,3,6,1,4,1,22420,2,8,1,1,6,1,2),_AcdSmapPortCoSMapCosIn_Type())
acdSmapPortCoSMapCosIn.setMaxAccess('read-only')
if mibBuilder.loadTexts:acdSmapPortCoSMapCosIn.setStatus(_A)
class _AcdSmapPortCoSMapGreenOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcdSmapPortCoSMapGreenOut_Type.__name__=_C
_AcdSmapPortCoSMapGreenOut_Object=MibTableColumn
acdSmapPortCoSMapGreenOut=_AcdSmapPortCoSMapGreenOut_Object((1,3,6,1,4,1,22420,2,8,1,1,6,1,3),_AcdSmapPortCoSMapGreenOut_Type())
acdSmapPortCoSMapGreenOut.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSmapPortCoSMapGreenOut.setStatus(_A)
class _AcdSmapPortCoSMapYellowOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcdSmapPortCoSMapYellowOut_Type.__name__=_C
_AcdSmapPortCoSMapYellowOut_Object=MibTableColumn
acdSmapPortCoSMapYellowOut=_AcdSmapPortCoSMapYellowOut_Object((1,3,6,1,4,1,22420,2,8,1,1,6,1,4),_AcdSmapPortCoSMapYellowOut_Type())
acdSmapPortCoSMapYellowOut.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSmapPortCoSMapYellowOut.setStatus(_A)
_AcdSmapConformance_ObjectIdentity=ObjectIdentity
acdSmapConformance=_AcdSmapConformance_ObjectIdentity((1,3,6,1,4,1,22420,2,8,2))
_AcdSmapCompliances_ObjectIdentity=ObjectIdentity
acdSmapCompliances=_AcdSmapCompliances_ObjectIdentity((1,3,6,1,4,1,22420,2,8,2,1))
_AcdSmapGroups_ObjectIdentity=ObjectIdentity
acdSmapGroups=_AcdSmapGroups_ObjectIdentity((1,3,6,1,4,1,22420,2,8,2,2))
acdSmapCoSProfGroup=ObjectGroup((1,3,6,1,4,1,22420,2,8,2,2,1))
acdSmapCoSProfGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:acdSmapCoSProfGroup.setStatus(_A)
acdSmapCoSProfCodePointGroup=ObjectGroup((1,3,6,1,4,1,22420,2,8,2,2,2))
acdSmapCoSProfCodePointGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:acdSmapCoSProfCodePointGroup.setStatus(_A)
acdSmapRegSetGroup=ObjectGroup((1,3,6,1,4,1,22420,2,8,2,2,3))
acdSmapRegSetGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:acdSmapRegSetGroup.setStatus(_A)
acdSmapRegSetCodePointGroup=ObjectGroup((1,3,6,1,4,1,22420,2,8,2,2,4))
acdSmapRegSetCodePointGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:acdSmapRegSetCodePointGroup.setStatus(_A)
acdSmapPortCoSEncodeDeiGroup=ObjectGroup((1,3,6,1,4,1,22420,2,8,2,2,5))
acdSmapPortCoSEncodeDeiGroup.setObjects((_B,_c))
if mibBuilder.loadTexts:acdSmapPortCoSEncodeDeiGroup.setStatus(_A)
acdSmapPortCoSMapGroup=ObjectGroup((1,3,6,1,4,1,22420,2,8,2,2,6))
acdSmapPortCoSMapGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:acdSmapPortCoSMapGroup.setStatus(_A)
acdSmapCompliance=ModuleCompliance((1,3,6,1,4,1,22420,2,8,2,1,1))
acdSmapCompliance.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:acdSmapCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'acdSmap':acdSmap,'acdSmapNotifications':acdSmapNotifications,'acdSmapMIBObjects':acdSmapMIBObjects,'acdSmapConfig':acdSmapConfig,'acdSmapCoSProfTable':acdSmapCoSProfTable,'acdSmapCoSProfEntry':acdSmapCoSProfEntry,_J:acdSmapCoSProfID,_P:acdSmapCoSProfRowStatus,_Q:acdSmapCoSProfName,_R:acdSmapCoSProfType,_S:acdSmapCoSProfDecodeDropBit,_T:acdSmapCoSProfEncodeDropBit,'acdSmapCoSProfCodePointTable':acdSmapCoSProfCodePointTable,'acdSmapCoSProfCodePointEntry':acdSmapCoSProfCodePointEntry,_M:acdSmapCoSProfCodePointID,_U:acdSmapCoSProfCodePointPreMarkingColor,_V:acdSmapCoSProfCodePointGreenOut,_W:acdSmapCoSProfCodePointYellowOut,'acdSmapRegSetTable':acdSmapRegSetTable,'acdSmapRegSetEntry':acdSmapRegSetEntry,_K:acdSmapRegSetID,_X:acdSmapRegSetRowStatus,_Y:acdSmapRegSetName,_Z:acdSmapRegSetType,'acdSmapRegSetCodePointTable':acdSmapRegSetCodePointTable,'acdSmapRegSetCodePointEntry':acdSmapRegSetCodePointEntry,_N:acdSmapRegSetCodePointID,_a:acdSmapRegSetCodePointRegulatorID,_b:acdSmapRegSetCodePointRegulatorEnable,'acdSmapPortCoSEncodeDeiTable':acdSmapPortCoSEncodeDeiTable,'acdSmapPortCoSEncodeDeiEntry':acdSmapPortCoSEncodeDeiEntry,_L:acdSmapPortCoSPortID,_c:acdSmapPortCoSEncodeDeiEnable,'acdSmapPortCoSMapTable':acdSmapPortCoSMapTable,'acdSmapPortCoSMapEntry':acdSmapPortCoSMapEntry,_O:acdSmapPortCoSMapID,_d:acdSmapPortCoSMapCosIn,_e:acdSmapPortCoSMapGreenOut,_f:acdSmapPortCoSMapYellowOut,'acdSmapConformance':acdSmapConformance,'acdSmapCompliances':acdSmapCompliances,'acdSmapCompliance':acdSmapCompliance,'acdSmapGroups':acdSmapGroups,_g:acdSmapCoSProfGroup,_h:acdSmapCoSProfCodePointGroup,_i:acdSmapRegSetGroup,_j:acdSmapRegSetCodePointGroup,_k:acdSmapPortCoSEncodeDeiGroup,_l:acdSmapPortCoSMapGroup})