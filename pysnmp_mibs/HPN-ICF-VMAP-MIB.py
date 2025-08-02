_N='hpnicfVMAP2to2InnerVlan'
_M='hpnicfVMAP2to2OuterVlan'
_L='hpnicfVMAP1to2Vlan'
_K='hpnicfVMAP1to2StartVlan'
_J='hpnicfVMAPNto1Vlan'
_I='hpnicfVMAPNto1StartVlan'
_H='hpnicfVMAP1to1Vlan'
_G='not-accessible'
_F='HPN-ICF-VMAP-MIB'
_E='ifIndex'
_D='IF-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfVmap=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,138))
if mibBuilder.loadTexts:hpnicfVmap.setRevisions(('2013-03-08 00:00',))
_HpnicfVMAPNNITable_Object=MibTable
hpnicfVMAPNNITable=_HpnicfVMAPNNITable_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,1))
if mibBuilder.loadTexts:hpnicfVMAPNNITable.setStatus(_A)
_HpnicfVMAPNNIEntry_Object=MibTableRow
hpnicfVMAPNNIEntry=_HpnicfVMAPNNIEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,1,1))
hpnicfVMAPNNIEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfVMAPNNIEntry.setStatus(_A)
_HpnicfVMAPNNIState_Type=TruthValue
_HpnicfVMAPNNIState_Object=MibTableColumn
hpnicfVMAPNNIState=_HpnicfVMAPNNIState_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,1,1,1),_HpnicfVMAPNNIState_Type())
hpnicfVMAPNNIState.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfVMAPNNIState.setStatus(_A)
_HpnicfVMAP1to1Table_Object=MibTable
hpnicfVMAP1to1Table=_HpnicfVMAP1to1Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,2))
if mibBuilder.loadTexts:hpnicfVMAP1to1Table.setStatus(_A)
_HpnicfVMAP1to1Entry_Object=MibTableRow
hpnicfVMAP1to1Entry=_HpnicfVMAP1to1Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,2,1))
hpnicfVMAP1to1Entry.setIndexNames((0,_D,_E),(0,_F,_H))
if mibBuilder.loadTexts:hpnicfVMAP1to1Entry.setStatus(_A)
class _HpnicfVMAP1to1Vlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP1to1Vlan_Type.__name__=_B
_HpnicfVMAP1to1Vlan_Object=MibTableColumn
hpnicfVMAP1to1Vlan=_HpnicfVMAP1to1Vlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,2,1,1),_HpnicfVMAP1to1Vlan_Type())
hpnicfVMAP1to1Vlan.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVMAP1to1Vlan.setStatus(_A)
class _HpnicfVMAP1to1TranslatedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP1to1TranslatedVlan_Type.__name__=_B
_HpnicfVMAP1to1TranslatedVlan_Object=MibTableColumn
hpnicfVMAP1to1TranslatedVlan=_HpnicfVMAP1to1TranslatedVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,2,1,2),_HpnicfVMAP1to1TranslatedVlan_Type())
hpnicfVMAP1to1TranslatedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP1to1TranslatedVlan.setStatus(_A)
_HpnicfVMAP1to1RowStatus_Type=RowStatus
_HpnicfVMAP1to1RowStatus_Object=MibTableColumn
hpnicfVMAP1to1RowStatus=_HpnicfVMAP1to1RowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,2,1,3),_HpnicfVMAP1to1RowStatus_Type())
hpnicfVMAP1to1RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP1to1RowStatus.setStatus(_A)
_HpnicfVMAPNto1RangeTable_Object=MibTable
hpnicfVMAPNto1RangeTable=_HpnicfVMAPNto1RangeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,3))
if mibBuilder.loadTexts:hpnicfVMAPNto1RangeTable.setStatus(_A)
_HpnicfVMAPNto1RangeEntry_Object=MibTableRow
hpnicfVMAPNto1RangeEntry=_HpnicfVMAPNto1RangeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,3,1))
hpnicfVMAPNto1RangeEntry.setIndexNames((0,_D,_E),(0,_F,_I))
if mibBuilder.loadTexts:hpnicfVMAPNto1RangeEntry.setStatus(_A)
class _HpnicfVMAPNto1StartVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAPNto1StartVlan_Type.__name__=_B
_HpnicfVMAPNto1StartVlan_Object=MibTableColumn
hpnicfVMAPNto1StartVlan=_HpnicfVMAPNto1StartVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,3,1,1),_HpnicfVMAPNto1StartVlan_Type())
hpnicfVMAPNto1StartVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVMAPNto1StartVlan.setStatus(_A)
class _HpnicfVMAPNto1EndVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAPNto1EndVlan_Type.__name__=_B
_HpnicfVMAPNto1EndVlan_Object=MibTableColumn
hpnicfVMAPNto1EndVlan=_HpnicfVMAPNto1EndVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,3,1,2),_HpnicfVMAPNto1EndVlan_Type())
hpnicfVMAPNto1EndVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAPNto1EndVlan.setStatus(_A)
class _HpnicfVMAPNto1RangeTranslatedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAPNto1RangeTranslatedVlan_Type.__name__=_B
_HpnicfVMAPNto1RangeTranslatedVlan_Object=MibTableColumn
hpnicfVMAPNto1RangeTranslatedVlan=_HpnicfVMAPNto1RangeTranslatedVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,3,1,3),_HpnicfVMAPNto1RangeTranslatedVlan_Type())
hpnicfVMAPNto1RangeTranslatedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAPNto1RangeTranslatedVlan.setStatus(_A)
_HpnicfVMAPNto1RangeRowStatus_Type=RowStatus
_HpnicfVMAPNto1RangeRowStatus_Object=MibTableColumn
hpnicfVMAPNto1RangeRowStatus=_HpnicfVMAPNto1RangeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,3,1,4),_HpnicfVMAPNto1RangeRowStatus_Type())
hpnicfVMAPNto1RangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAPNto1RangeRowStatus.setStatus(_A)
_HpnicfVMAPNto1SingleTable_Object=MibTable
hpnicfVMAPNto1SingleTable=_HpnicfVMAPNto1SingleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,4))
if mibBuilder.loadTexts:hpnicfVMAPNto1SingleTable.setStatus(_A)
_HpnicfVMAPNto1SingleEntry_Object=MibTableRow
hpnicfVMAPNto1SingleEntry=_HpnicfVMAPNto1SingleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,4,1))
hpnicfVMAPNto1SingleEntry.setIndexNames((0,_D,_E),(0,_F,_J))
if mibBuilder.loadTexts:hpnicfVMAPNto1SingleEntry.setStatus(_A)
class _HpnicfVMAPNto1Vlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAPNto1Vlan_Type.__name__=_B
_HpnicfVMAPNto1Vlan_Object=MibTableColumn
hpnicfVMAPNto1Vlan=_HpnicfVMAPNto1Vlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,4,1,1),_HpnicfVMAPNto1Vlan_Type())
hpnicfVMAPNto1Vlan.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVMAPNto1Vlan.setStatus(_A)
class _HpnicfVMAPNto1SingleTranslatedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAPNto1SingleTranslatedVlan_Type.__name__=_B
_HpnicfVMAPNto1SingleTranslatedVlan_Object=MibTableColumn
hpnicfVMAPNto1SingleTranslatedVlan=_HpnicfVMAPNto1SingleTranslatedVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,4,1,2),_HpnicfVMAPNto1SingleTranslatedVlan_Type())
hpnicfVMAPNto1SingleTranslatedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAPNto1SingleTranslatedVlan.setStatus(_A)
_HpnicfVMAPNto1SingleRowStatus_Type=RowStatus
_HpnicfVMAPNto1SingleRowStatus_Object=MibTableColumn
hpnicfVMAPNto1SingleRowStatus=_HpnicfVMAPNto1SingleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,4,1,3),_HpnicfVMAPNto1SingleRowStatus_Type())
hpnicfVMAPNto1SingleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAPNto1SingleRowStatus.setStatus(_A)
_HpnicfVMAP1to2RangeTable_Object=MibTable
hpnicfVMAP1to2RangeTable=_HpnicfVMAP1to2RangeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,5))
if mibBuilder.loadTexts:hpnicfVMAP1to2RangeTable.setStatus(_A)
_HpnicfVMAP1to2RangeEntry_Object=MibTableRow
hpnicfVMAP1to2RangeEntry=_HpnicfVMAP1to2RangeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,5,1))
hpnicfVMAP1to2RangeEntry.setIndexNames((0,_D,_E),(0,_F,_K))
if mibBuilder.loadTexts:hpnicfVMAP1to2RangeEntry.setStatus(_A)
class _HpnicfVMAP1to2StartVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP1to2StartVlan_Type.__name__=_B
_HpnicfVMAP1to2StartVlan_Object=MibTableColumn
hpnicfVMAP1to2StartVlan=_HpnicfVMAP1to2StartVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,5,1,1),_HpnicfVMAP1to2StartVlan_Type())
hpnicfVMAP1to2StartVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVMAP1to2StartVlan.setStatus(_A)
class _HpnicfVMAP1to2EndVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP1to2EndVlan_Type.__name__=_B
_HpnicfVMAP1to2EndVlan_Object=MibTableColumn
hpnicfVMAP1to2EndVlan=_HpnicfVMAP1to2EndVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,5,1,2),_HpnicfVMAP1to2EndVlan_Type())
hpnicfVMAP1to2EndVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP1to2EndVlan.setStatus(_A)
class _HpnicfVMAP1to2RangeNestedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP1to2RangeNestedVlan_Type.__name__=_B
_HpnicfVMAP1to2RangeNestedVlan_Object=MibTableColumn
hpnicfVMAP1to2RangeNestedVlan=_HpnicfVMAP1to2RangeNestedVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,5,1,3),_HpnicfVMAP1to2RangeNestedVlan_Type())
hpnicfVMAP1to2RangeNestedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP1to2RangeNestedVlan.setStatus(_A)
_HpnicfVMAP1to2RangeRowStatus_Type=RowStatus
_HpnicfVMAP1to2RangeRowStatus_Object=MibTableColumn
hpnicfVMAP1to2RangeRowStatus=_HpnicfVMAP1to2RangeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,5,1,4),_HpnicfVMAP1to2RangeRowStatus_Type())
hpnicfVMAP1to2RangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP1to2RangeRowStatus.setStatus(_A)
_HpnicfVMAP1to2SingleTable_Object=MibTable
hpnicfVMAP1to2SingleTable=_HpnicfVMAP1to2SingleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,6))
if mibBuilder.loadTexts:hpnicfVMAP1to2SingleTable.setStatus(_A)
_HpnicfVMAP1to2SingleEntry_Object=MibTableRow
hpnicfVMAP1to2SingleEntry=_HpnicfVMAP1to2SingleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,6,1))
hpnicfVMAP1to2SingleEntry.setIndexNames((0,_D,_E),(0,_F,_L))
if mibBuilder.loadTexts:hpnicfVMAP1to2SingleEntry.setStatus(_A)
class _HpnicfVMAP1to2Vlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP1to2Vlan_Type.__name__=_B
_HpnicfVMAP1to2Vlan_Object=MibTableColumn
hpnicfVMAP1to2Vlan=_HpnicfVMAP1to2Vlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,6,1,1),_HpnicfVMAP1to2Vlan_Type())
hpnicfVMAP1to2Vlan.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVMAP1to2Vlan.setStatus(_A)
class _HpnicfVMAP1to2SingleNestedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP1to2SingleNestedVlan_Type.__name__=_B
_HpnicfVMAP1to2SingleNestedVlan_Object=MibTableColumn
hpnicfVMAP1to2SingleNestedVlan=_HpnicfVMAP1to2SingleNestedVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,6,1,2),_HpnicfVMAP1to2SingleNestedVlan_Type())
hpnicfVMAP1to2SingleNestedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP1to2SingleNestedVlan.setStatus(_A)
_HpnicfVMAP1to2SingleRowStatus_Type=RowStatus
_HpnicfVMAP1to2SingleRowStatus_Object=MibTableColumn
hpnicfVMAP1to2SingleRowStatus=_HpnicfVMAP1to2SingleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,6,1,3),_HpnicfVMAP1to2SingleRowStatus_Type())
hpnicfVMAP1to2SingleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP1to2SingleRowStatus.setStatus(_A)
_HpnicfVMAP2to2Table_Object=MibTable
hpnicfVMAP2to2Table=_HpnicfVMAP2to2Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,7))
if mibBuilder.loadTexts:hpnicfVMAP2to2Table.setStatus(_A)
_HpnicfVMAP2to2Entry_Object=MibTableRow
hpnicfVMAP2to2Entry=_HpnicfVMAP2to2Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,7,1))
hpnicfVMAP2to2Entry.setIndexNames((0,_D,_E),(0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:hpnicfVMAP2to2Entry.setStatus(_A)
class _HpnicfVMAP2to2OuterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP2to2OuterVlan_Type.__name__=_B
_HpnicfVMAP2to2OuterVlan_Object=MibTableColumn
hpnicfVMAP2to2OuterVlan=_HpnicfVMAP2to2OuterVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,7,1,1),_HpnicfVMAP2to2OuterVlan_Type())
hpnicfVMAP2to2OuterVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVMAP2to2OuterVlan.setStatus(_A)
class _HpnicfVMAP2to2InnerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP2to2InnerVlan_Type.__name__=_B
_HpnicfVMAP2to2InnerVlan_Object=MibTableColumn
hpnicfVMAP2to2InnerVlan=_HpnicfVMAP2to2InnerVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,7,1,2),_HpnicfVMAP2to2InnerVlan_Type())
hpnicfVMAP2to2InnerVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVMAP2to2InnerVlan.setStatus(_A)
class _HpnicfVMAP2to2TranslatedOuterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP2to2TranslatedOuterVlan_Type.__name__=_B
_HpnicfVMAP2to2TranslatedOuterVlan_Object=MibTableColumn
hpnicfVMAP2to2TranslatedOuterVlan=_HpnicfVMAP2to2TranslatedOuterVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,7,1,3),_HpnicfVMAP2to2TranslatedOuterVlan_Type())
hpnicfVMAP2to2TranslatedOuterVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP2to2TranslatedOuterVlan.setStatus(_A)
class _HpnicfVMAP2to2TranslatedInnerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVMAP2to2TranslatedInnerVlan_Type.__name__=_B
_HpnicfVMAP2to2TranslatedInnerVlan_Object=MibTableColumn
hpnicfVMAP2to2TranslatedInnerVlan=_HpnicfVMAP2to2TranslatedInnerVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,7,1,4),_HpnicfVMAP2to2TranslatedInnerVlan_Type())
hpnicfVMAP2to2TranslatedInnerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP2to2TranslatedInnerVlan.setStatus(_A)
_HpnicfVMAP2to2RowStatus_Type=RowStatus
_HpnicfVMAP2to2RowStatus_Object=MibTableColumn
hpnicfVMAP2to2RowStatus=_HpnicfVMAP2to2RowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,138,7,1,5),_HpnicfVMAP2to2RowStatus_Type())
hpnicfVMAP2to2RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVMAP2to2RowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hpnicfVmap':hpnicfVmap,'hpnicfVMAPNNITable':hpnicfVMAPNNITable,'hpnicfVMAPNNIEntry':hpnicfVMAPNNIEntry,'hpnicfVMAPNNIState':hpnicfVMAPNNIState,'hpnicfVMAP1to1Table':hpnicfVMAP1to1Table,'hpnicfVMAP1to1Entry':hpnicfVMAP1to1Entry,_H:hpnicfVMAP1to1Vlan,'hpnicfVMAP1to1TranslatedVlan':hpnicfVMAP1to1TranslatedVlan,'hpnicfVMAP1to1RowStatus':hpnicfVMAP1to1RowStatus,'hpnicfVMAPNto1RangeTable':hpnicfVMAPNto1RangeTable,'hpnicfVMAPNto1RangeEntry':hpnicfVMAPNto1RangeEntry,_I:hpnicfVMAPNto1StartVlan,'hpnicfVMAPNto1EndVlan':hpnicfVMAPNto1EndVlan,'hpnicfVMAPNto1RangeTranslatedVlan':hpnicfVMAPNto1RangeTranslatedVlan,'hpnicfVMAPNto1RangeRowStatus':hpnicfVMAPNto1RangeRowStatus,'hpnicfVMAPNto1SingleTable':hpnicfVMAPNto1SingleTable,'hpnicfVMAPNto1SingleEntry':hpnicfVMAPNto1SingleEntry,_J:hpnicfVMAPNto1Vlan,'hpnicfVMAPNto1SingleTranslatedVlan':hpnicfVMAPNto1SingleTranslatedVlan,'hpnicfVMAPNto1SingleRowStatus':hpnicfVMAPNto1SingleRowStatus,'hpnicfVMAP1to2RangeTable':hpnicfVMAP1to2RangeTable,'hpnicfVMAP1to2RangeEntry':hpnicfVMAP1to2RangeEntry,_K:hpnicfVMAP1to2StartVlan,'hpnicfVMAP1to2EndVlan':hpnicfVMAP1to2EndVlan,'hpnicfVMAP1to2RangeNestedVlan':hpnicfVMAP1to2RangeNestedVlan,'hpnicfVMAP1to2RangeRowStatus':hpnicfVMAP1to2RangeRowStatus,'hpnicfVMAP1to2SingleTable':hpnicfVMAP1to2SingleTable,'hpnicfVMAP1to2SingleEntry':hpnicfVMAP1to2SingleEntry,_L:hpnicfVMAP1to2Vlan,'hpnicfVMAP1to2SingleNestedVlan':hpnicfVMAP1to2SingleNestedVlan,'hpnicfVMAP1to2SingleRowStatus':hpnicfVMAP1to2SingleRowStatus,'hpnicfVMAP2to2Table':hpnicfVMAP2to2Table,'hpnicfVMAP2to2Entry':hpnicfVMAP2to2Entry,_M:hpnicfVMAP2to2OuterVlan,_N:hpnicfVMAP2to2InnerVlan,'hpnicfVMAP2to2TranslatedOuterVlan':hpnicfVMAP2to2TranslatedOuterVlan,'hpnicfVMAP2to2TranslatedInnerVlan':hpnicfVMAP2to2TranslatedInnerVlan,'hpnicfVMAP2to2RowStatus':hpnicfVMAP2to2RowStatus})