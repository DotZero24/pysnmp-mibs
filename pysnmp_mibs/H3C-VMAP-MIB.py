_N='h3cVMAP2to2InnerVlan'
_M='h3cVMAP2to2OuterVlan'
_L='h3cVMAP1to2Vlan'
_K='h3cVMAP1to2StartVlan'
_J='h3cVMAPNto1Vlan'
_I='h3cVMAPNto1StartVlan'
_H='h3cVMAP1to1Vlan'
_G='not-accessible'
_F='H3C-VMAP-MIB'
_E='ifIndex'
_D='IF-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cVmap=ModuleIdentity((1,3,6,1,4,1,2011,10,2,138))
if mibBuilder.loadTexts:h3cVmap.setRevisions(('2013-03-08 00:00',))
_H3cVMAPNNITable_Object=MibTable
h3cVMAPNNITable=_H3cVMAPNNITable_Object((1,3,6,1,4,1,2011,10,2,138,1))
if mibBuilder.loadTexts:h3cVMAPNNITable.setStatus(_A)
_H3cVMAPNNIEntry_Object=MibTableRow
h3cVMAPNNIEntry=_H3cVMAPNNIEntry_Object((1,3,6,1,4,1,2011,10,2,138,1,1))
h3cVMAPNNIEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cVMAPNNIEntry.setStatus(_A)
_H3cVMAPNNIState_Type=TruthValue
_H3cVMAPNNIState_Object=MibTableColumn
h3cVMAPNNIState=_H3cVMAPNNIState_Object((1,3,6,1,4,1,2011,10,2,138,1,1,1),_H3cVMAPNNIState_Type())
h3cVMAPNNIState.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cVMAPNNIState.setStatus(_A)
_H3cVMAP1to1Table_Object=MibTable
h3cVMAP1to1Table=_H3cVMAP1to1Table_Object((1,3,6,1,4,1,2011,10,2,138,2))
if mibBuilder.loadTexts:h3cVMAP1to1Table.setStatus(_A)
_H3cVMAP1to1Entry_Object=MibTableRow
h3cVMAP1to1Entry=_H3cVMAP1to1Entry_Object((1,3,6,1,4,1,2011,10,2,138,2,1))
h3cVMAP1to1Entry.setIndexNames((0,_D,_E),(0,_F,_H))
if mibBuilder.loadTexts:h3cVMAP1to1Entry.setStatus(_A)
class _H3cVMAP1to1Vlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP1to1Vlan_Type.__name__=_B
_H3cVMAP1to1Vlan_Object=MibTableColumn
h3cVMAP1to1Vlan=_H3cVMAP1to1Vlan_Object((1,3,6,1,4,1,2011,10,2,138,2,1,1),_H3cVMAP1to1Vlan_Type())
h3cVMAP1to1Vlan.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVMAP1to1Vlan.setStatus(_A)
class _H3cVMAP1to1TranslatedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP1to1TranslatedVlan_Type.__name__=_B
_H3cVMAP1to1TranslatedVlan_Object=MibTableColumn
h3cVMAP1to1TranslatedVlan=_H3cVMAP1to1TranslatedVlan_Object((1,3,6,1,4,1,2011,10,2,138,2,1,2),_H3cVMAP1to1TranslatedVlan_Type())
h3cVMAP1to1TranslatedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP1to1TranslatedVlan.setStatus(_A)
_H3cVMAP1to1RowStatus_Type=RowStatus
_H3cVMAP1to1RowStatus_Object=MibTableColumn
h3cVMAP1to1RowStatus=_H3cVMAP1to1RowStatus_Object((1,3,6,1,4,1,2011,10,2,138,2,1,3),_H3cVMAP1to1RowStatus_Type())
h3cVMAP1to1RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP1to1RowStatus.setStatus(_A)
_H3cVMAPNto1RangeTable_Object=MibTable
h3cVMAPNto1RangeTable=_H3cVMAPNto1RangeTable_Object((1,3,6,1,4,1,2011,10,2,138,3))
if mibBuilder.loadTexts:h3cVMAPNto1RangeTable.setStatus(_A)
_H3cVMAPNto1RangeEntry_Object=MibTableRow
h3cVMAPNto1RangeEntry=_H3cVMAPNto1RangeEntry_Object((1,3,6,1,4,1,2011,10,2,138,3,1))
h3cVMAPNto1RangeEntry.setIndexNames((0,_D,_E),(0,_F,_I))
if mibBuilder.loadTexts:h3cVMAPNto1RangeEntry.setStatus(_A)
class _H3cVMAPNto1StartVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAPNto1StartVlan_Type.__name__=_B
_H3cVMAPNto1StartVlan_Object=MibTableColumn
h3cVMAPNto1StartVlan=_H3cVMAPNto1StartVlan_Object((1,3,6,1,4,1,2011,10,2,138,3,1,1),_H3cVMAPNto1StartVlan_Type())
h3cVMAPNto1StartVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVMAPNto1StartVlan.setStatus(_A)
class _H3cVMAPNto1EndVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAPNto1EndVlan_Type.__name__=_B
_H3cVMAPNto1EndVlan_Object=MibTableColumn
h3cVMAPNto1EndVlan=_H3cVMAPNto1EndVlan_Object((1,3,6,1,4,1,2011,10,2,138,3,1,2),_H3cVMAPNto1EndVlan_Type())
h3cVMAPNto1EndVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAPNto1EndVlan.setStatus(_A)
class _H3cVMAPNto1RangeTranslatedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAPNto1RangeTranslatedVlan_Type.__name__=_B
_H3cVMAPNto1RangeTranslatedVlan_Object=MibTableColumn
h3cVMAPNto1RangeTranslatedVlan=_H3cVMAPNto1RangeTranslatedVlan_Object((1,3,6,1,4,1,2011,10,2,138,3,1,3),_H3cVMAPNto1RangeTranslatedVlan_Type())
h3cVMAPNto1RangeTranslatedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAPNto1RangeTranslatedVlan.setStatus(_A)
_H3cVMAPNto1RangeRowStatus_Type=RowStatus
_H3cVMAPNto1RangeRowStatus_Object=MibTableColumn
h3cVMAPNto1RangeRowStatus=_H3cVMAPNto1RangeRowStatus_Object((1,3,6,1,4,1,2011,10,2,138,3,1,4),_H3cVMAPNto1RangeRowStatus_Type())
h3cVMAPNto1RangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAPNto1RangeRowStatus.setStatus(_A)
_H3cVMAPNto1SingleTable_Object=MibTable
h3cVMAPNto1SingleTable=_H3cVMAPNto1SingleTable_Object((1,3,6,1,4,1,2011,10,2,138,4))
if mibBuilder.loadTexts:h3cVMAPNto1SingleTable.setStatus(_A)
_H3cVMAPNto1SingleEntry_Object=MibTableRow
h3cVMAPNto1SingleEntry=_H3cVMAPNto1SingleEntry_Object((1,3,6,1,4,1,2011,10,2,138,4,1))
h3cVMAPNto1SingleEntry.setIndexNames((0,_D,_E),(0,_F,_J))
if mibBuilder.loadTexts:h3cVMAPNto1SingleEntry.setStatus(_A)
class _H3cVMAPNto1Vlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAPNto1Vlan_Type.__name__=_B
_H3cVMAPNto1Vlan_Object=MibTableColumn
h3cVMAPNto1Vlan=_H3cVMAPNto1Vlan_Object((1,3,6,1,4,1,2011,10,2,138,4,1,1),_H3cVMAPNto1Vlan_Type())
h3cVMAPNto1Vlan.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVMAPNto1Vlan.setStatus(_A)
class _H3cVMAPNto1SingleTranslatedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAPNto1SingleTranslatedVlan_Type.__name__=_B
_H3cVMAPNto1SingleTranslatedVlan_Object=MibTableColumn
h3cVMAPNto1SingleTranslatedVlan=_H3cVMAPNto1SingleTranslatedVlan_Object((1,3,6,1,4,1,2011,10,2,138,4,1,2),_H3cVMAPNto1SingleTranslatedVlan_Type())
h3cVMAPNto1SingleTranslatedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAPNto1SingleTranslatedVlan.setStatus(_A)
_H3cVMAPNto1SingleRowStatus_Type=RowStatus
_H3cVMAPNto1SingleRowStatus_Object=MibTableColumn
h3cVMAPNto1SingleRowStatus=_H3cVMAPNto1SingleRowStatus_Object((1,3,6,1,4,1,2011,10,2,138,4,1,3),_H3cVMAPNto1SingleRowStatus_Type())
h3cVMAPNto1SingleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAPNto1SingleRowStatus.setStatus(_A)
_H3cVMAP1to2RangeTable_Object=MibTable
h3cVMAP1to2RangeTable=_H3cVMAP1to2RangeTable_Object((1,3,6,1,4,1,2011,10,2,138,5))
if mibBuilder.loadTexts:h3cVMAP1to2RangeTable.setStatus(_A)
_H3cVMAP1to2RangeEntry_Object=MibTableRow
h3cVMAP1to2RangeEntry=_H3cVMAP1to2RangeEntry_Object((1,3,6,1,4,1,2011,10,2,138,5,1))
h3cVMAP1to2RangeEntry.setIndexNames((0,_D,_E),(0,_F,_K))
if mibBuilder.loadTexts:h3cVMAP1to2RangeEntry.setStatus(_A)
class _H3cVMAP1to2StartVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP1to2StartVlan_Type.__name__=_B
_H3cVMAP1to2StartVlan_Object=MibTableColumn
h3cVMAP1to2StartVlan=_H3cVMAP1to2StartVlan_Object((1,3,6,1,4,1,2011,10,2,138,5,1,1),_H3cVMAP1to2StartVlan_Type())
h3cVMAP1to2StartVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVMAP1to2StartVlan.setStatus(_A)
class _H3cVMAP1to2EndVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP1to2EndVlan_Type.__name__=_B
_H3cVMAP1to2EndVlan_Object=MibTableColumn
h3cVMAP1to2EndVlan=_H3cVMAP1to2EndVlan_Object((1,3,6,1,4,1,2011,10,2,138,5,1,2),_H3cVMAP1to2EndVlan_Type())
h3cVMAP1to2EndVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP1to2EndVlan.setStatus(_A)
class _H3cVMAP1to2RangeNestedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP1to2RangeNestedVlan_Type.__name__=_B
_H3cVMAP1to2RangeNestedVlan_Object=MibTableColumn
h3cVMAP1to2RangeNestedVlan=_H3cVMAP1to2RangeNestedVlan_Object((1,3,6,1,4,1,2011,10,2,138,5,1,3),_H3cVMAP1to2RangeNestedVlan_Type())
h3cVMAP1to2RangeNestedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP1to2RangeNestedVlan.setStatus(_A)
_H3cVMAP1to2RangeRowStatus_Type=RowStatus
_H3cVMAP1to2RangeRowStatus_Object=MibTableColumn
h3cVMAP1to2RangeRowStatus=_H3cVMAP1to2RangeRowStatus_Object((1,3,6,1,4,1,2011,10,2,138,5,1,4),_H3cVMAP1to2RangeRowStatus_Type())
h3cVMAP1to2RangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP1to2RangeRowStatus.setStatus(_A)
_H3cVMAP1to2SingleTable_Object=MibTable
h3cVMAP1to2SingleTable=_H3cVMAP1to2SingleTable_Object((1,3,6,1,4,1,2011,10,2,138,6))
if mibBuilder.loadTexts:h3cVMAP1to2SingleTable.setStatus(_A)
_H3cVMAP1to2SingleEntry_Object=MibTableRow
h3cVMAP1to2SingleEntry=_H3cVMAP1to2SingleEntry_Object((1,3,6,1,4,1,2011,10,2,138,6,1))
h3cVMAP1to2SingleEntry.setIndexNames((0,_D,_E),(0,_F,_L))
if mibBuilder.loadTexts:h3cVMAP1to2SingleEntry.setStatus(_A)
class _H3cVMAP1to2Vlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP1to2Vlan_Type.__name__=_B
_H3cVMAP1to2Vlan_Object=MibTableColumn
h3cVMAP1to2Vlan=_H3cVMAP1to2Vlan_Object((1,3,6,1,4,1,2011,10,2,138,6,1,1),_H3cVMAP1to2Vlan_Type())
h3cVMAP1to2Vlan.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVMAP1to2Vlan.setStatus(_A)
class _H3cVMAP1to2SingleNestedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP1to2SingleNestedVlan_Type.__name__=_B
_H3cVMAP1to2SingleNestedVlan_Object=MibTableColumn
h3cVMAP1to2SingleNestedVlan=_H3cVMAP1to2SingleNestedVlan_Object((1,3,6,1,4,1,2011,10,2,138,6,1,2),_H3cVMAP1to2SingleNestedVlan_Type())
h3cVMAP1to2SingleNestedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP1to2SingleNestedVlan.setStatus(_A)
_H3cVMAP1to2SingleRowStatus_Type=RowStatus
_H3cVMAP1to2SingleRowStatus_Object=MibTableColumn
h3cVMAP1to2SingleRowStatus=_H3cVMAP1to2SingleRowStatus_Object((1,3,6,1,4,1,2011,10,2,138,6,1,3),_H3cVMAP1to2SingleRowStatus_Type())
h3cVMAP1to2SingleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP1to2SingleRowStatus.setStatus(_A)
_H3cVMAP2to2Table_Object=MibTable
h3cVMAP2to2Table=_H3cVMAP2to2Table_Object((1,3,6,1,4,1,2011,10,2,138,7))
if mibBuilder.loadTexts:h3cVMAP2to2Table.setStatus(_A)
_H3cVMAP2to2Entry_Object=MibTableRow
h3cVMAP2to2Entry=_H3cVMAP2to2Entry_Object((1,3,6,1,4,1,2011,10,2,138,7,1))
h3cVMAP2to2Entry.setIndexNames((0,_D,_E),(0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:h3cVMAP2to2Entry.setStatus(_A)
class _H3cVMAP2to2OuterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP2to2OuterVlan_Type.__name__=_B
_H3cVMAP2to2OuterVlan_Object=MibTableColumn
h3cVMAP2to2OuterVlan=_H3cVMAP2to2OuterVlan_Object((1,3,6,1,4,1,2011,10,2,138,7,1,1),_H3cVMAP2to2OuterVlan_Type())
h3cVMAP2to2OuterVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVMAP2to2OuterVlan.setStatus(_A)
class _H3cVMAP2to2InnerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP2to2InnerVlan_Type.__name__=_B
_H3cVMAP2to2InnerVlan_Object=MibTableColumn
h3cVMAP2to2InnerVlan=_H3cVMAP2to2InnerVlan_Object((1,3,6,1,4,1,2011,10,2,138,7,1,2),_H3cVMAP2to2InnerVlan_Type())
h3cVMAP2to2InnerVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVMAP2to2InnerVlan.setStatus(_A)
class _H3cVMAP2to2TranslatedOuterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP2to2TranslatedOuterVlan_Type.__name__=_B
_H3cVMAP2to2TranslatedOuterVlan_Object=MibTableColumn
h3cVMAP2to2TranslatedOuterVlan=_H3cVMAP2to2TranslatedOuterVlan_Object((1,3,6,1,4,1,2011,10,2,138,7,1,3),_H3cVMAP2to2TranslatedOuterVlan_Type())
h3cVMAP2to2TranslatedOuterVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP2to2TranslatedOuterVlan.setStatus(_A)
class _H3cVMAP2to2TranslatedInnerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVMAP2to2TranslatedInnerVlan_Type.__name__=_B
_H3cVMAP2to2TranslatedInnerVlan_Object=MibTableColumn
h3cVMAP2to2TranslatedInnerVlan=_H3cVMAP2to2TranslatedInnerVlan_Object((1,3,6,1,4,1,2011,10,2,138,7,1,4),_H3cVMAP2to2TranslatedInnerVlan_Type())
h3cVMAP2to2TranslatedInnerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP2to2TranslatedInnerVlan.setStatus(_A)
_H3cVMAP2to2RowStatus_Type=RowStatus
_H3cVMAP2to2RowStatus_Object=MibTableColumn
h3cVMAP2to2RowStatus=_H3cVMAP2to2RowStatus_Object((1,3,6,1,4,1,2011,10,2,138,7,1,5),_H3cVMAP2to2RowStatus_Type())
h3cVMAP2to2RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMAP2to2RowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'h3cVmap':h3cVmap,'h3cVMAPNNITable':h3cVMAPNNITable,'h3cVMAPNNIEntry':h3cVMAPNNIEntry,'h3cVMAPNNIState':h3cVMAPNNIState,'h3cVMAP1to1Table':h3cVMAP1to1Table,'h3cVMAP1to1Entry':h3cVMAP1to1Entry,_H:h3cVMAP1to1Vlan,'h3cVMAP1to1TranslatedVlan':h3cVMAP1to1TranslatedVlan,'h3cVMAP1to1RowStatus':h3cVMAP1to1RowStatus,'h3cVMAPNto1RangeTable':h3cVMAPNto1RangeTable,'h3cVMAPNto1RangeEntry':h3cVMAPNto1RangeEntry,_I:h3cVMAPNto1StartVlan,'h3cVMAPNto1EndVlan':h3cVMAPNto1EndVlan,'h3cVMAPNto1RangeTranslatedVlan':h3cVMAPNto1RangeTranslatedVlan,'h3cVMAPNto1RangeRowStatus':h3cVMAPNto1RangeRowStatus,'h3cVMAPNto1SingleTable':h3cVMAPNto1SingleTable,'h3cVMAPNto1SingleEntry':h3cVMAPNto1SingleEntry,_J:h3cVMAPNto1Vlan,'h3cVMAPNto1SingleTranslatedVlan':h3cVMAPNto1SingleTranslatedVlan,'h3cVMAPNto1SingleRowStatus':h3cVMAPNto1SingleRowStatus,'h3cVMAP1to2RangeTable':h3cVMAP1to2RangeTable,'h3cVMAP1to2RangeEntry':h3cVMAP1to2RangeEntry,_K:h3cVMAP1to2StartVlan,'h3cVMAP1to2EndVlan':h3cVMAP1to2EndVlan,'h3cVMAP1to2RangeNestedVlan':h3cVMAP1to2RangeNestedVlan,'h3cVMAP1to2RangeRowStatus':h3cVMAP1to2RangeRowStatus,'h3cVMAP1to2SingleTable':h3cVMAP1to2SingleTable,'h3cVMAP1to2SingleEntry':h3cVMAP1to2SingleEntry,_L:h3cVMAP1to2Vlan,'h3cVMAP1to2SingleNestedVlan':h3cVMAP1to2SingleNestedVlan,'h3cVMAP1to2SingleRowStatus':h3cVMAP1to2SingleRowStatus,'h3cVMAP2to2Table':h3cVMAP2to2Table,'h3cVMAP2to2Entry':h3cVMAP2to2Entry,_M:h3cVMAP2to2OuterVlan,_N:h3cVMAP2to2InnerVlan,'h3cVMAP2to2TranslatedOuterVlan':h3cVMAP2to2TranslatedOuterVlan,'h3cVMAP2to2TranslatedInnerVlan':h3cVMAP2to2TranslatedInnerVlan,'h3cVMAP2to2RowStatus':h3cVMAP2to2RowStatus})