_I='nbsMetaMibVariableID'
_H='nbsMetaMibVariableIfIndex'
_G='nbsMetaMibFeatureID'
_F='Integer32'
_E='not-accessible'
_D='NBS-META-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
nbsMetaMib=ModuleIdentity((1,3,6,1,4,1,629,205))
_NbsMetaMibGrp_ObjectIdentity=ObjectIdentity
nbsMetaMibGrp=_NbsMetaMibGrp_ObjectIdentity((1,3,6,1,4,1,629,205,1))
if mibBuilder.loadTexts:nbsMetaMibGrp.setStatus(_A)
_NbsMetaMibFeatureTableSize_Type=Integer32
_NbsMetaMibFeatureTableSize_Object=MibScalar
nbsMetaMibFeatureTableSize=_NbsMetaMibFeatureTableSize_Object((1,3,6,1,4,1,629,205,1,1),_NbsMetaMibFeatureTableSize_Type())
nbsMetaMibFeatureTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibFeatureTableSize.setStatus(_A)
_NbsMetaMibFeatureTable_Object=MibTable
nbsMetaMibFeatureTable=_NbsMetaMibFeatureTable_Object((1,3,6,1,4,1,629,205,1,2))
if mibBuilder.loadTexts:nbsMetaMibFeatureTable.setStatus(_A)
_NbsMetaMibFeatureEntry_Object=MibTableRow
nbsMetaMibFeatureEntry=_NbsMetaMibFeatureEntry_Object((1,3,6,1,4,1,629,205,1,2,1))
nbsMetaMibFeatureEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:nbsMetaMibFeatureEntry.setStatus(_A)
_NbsMetaMibFeatureID_Type=Integer32
_NbsMetaMibFeatureID_Object=MibTableColumn
nbsMetaMibFeatureID=_NbsMetaMibFeatureID_Object((1,3,6,1,4,1,629,205,1,2,1,1),_NbsMetaMibFeatureID_Type())
nbsMetaMibFeatureID.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsMetaMibFeatureID.setStatus(_A)
class _NbsMetaMibFeatureFamily_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbsMetaMibFeatureFamily_Type.__name__=_C
_NbsMetaMibFeatureFamily_Object=MibTableColumn
nbsMetaMibFeatureFamily=_NbsMetaMibFeatureFamily_Object((1,3,6,1,4,1,629,205,1,2,1,2),_NbsMetaMibFeatureFamily_Type())
nbsMetaMibFeatureFamily.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibFeatureFamily.setStatus(_A)
class _NbsMetaMibFeatureName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbsMetaMibFeatureName_Type.__name__=_C
_NbsMetaMibFeatureName_Object=MibTableColumn
nbsMetaMibFeatureName=_NbsMetaMibFeatureName_Object((1,3,6,1,4,1,629,205,1,2,1,3),_NbsMetaMibFeatureName_Type())
nbsMetaMibFeatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibFeatureName.setStatus(_A)
_NbsMetaMibFeatureDesc_Type=DisplayString
_NbsMetaMibFeatureDesc_Object=MibTableColumn
nbsMetaMibFeatureDesc=_NbsMetaMibFeatureDesc_Object((1,3,6,1,4,1,629,205,1,2,1,4),_NbsMetaMibFeatureDesc_Type())
nbsMetaMibFeatureDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibFeatureDesc.setStatus(_A)
class _NbsMetaMibFeatureUnits_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsMetaMibFeatureUnits_Type.__name__=_C
_NbsMetaMibFeatureUnits_Object=MibTableColumn
nbsMetaMibFeatureUnits=_NbsMetaMibFeatureUnits_Object((1,3,6,1,4,1,629,205,1,2,1,5),_NbsMetaMibFeatureUnits_Type())
nbsMetaMibFeatureUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibFeatureUnits.setStatus(_A)
class _NbsMetaMibFeatureType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enum',1),('string',2),('integer',3),('float',4)))
_NbsMetaMibFeatureType_Type.__name__=_F
_NbsMetaMibFeatureType_Object=MibTableColumn
nbsMetaMibFeatureType=_NbsMetaMibFeatureType_Object((1,3,6,1,4,1,629,205,1,2,1,6),_NbsMetaMibFeatureType_Type())
nbsMetaMibFeatureType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibFeatureType.setStatus(_A)
_NbsMetaMibVariableTableSize_Type=Integer32
_NbsMetaMibVariableTableSize_Object=MibScalar
nbsMetaMibVariableTableSize=_NbsMetaMibVariableTableSize_Object((1,3,6,1,4,1,629,205,1,3),_NbsMetaMibVariableTableSize_Type())
nbsMetaMibVariableTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibVariableTableSize.setStatus(_A)
_NbsMetaMibVariableTable_Object=MibTable
nbsMetaMibVariableTable=_NbsMetaMibVariableTable_Object((1,3,6,1,4,1,629,205,1,4))
if mibBuilder.loadTexts:nbsMetaMibVariableTable.setStatus(_A)
_NbsMetaMibVariableEntry_Object=MibTableRow
nbsMetaMibVariableEntry=_NbsMetaMibVariableEntry_Object((1,3,6,1,4,1,629,205,1,4,1))
nbsMetaMibVariableEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:nbsMetaMibVariableEntry.setStatus(_A)
_NbsMetaMibVariableIfIndex_Type=InterfaceIndex
_NbsMetaMibVariableIfIndex_Object=MibTableColumn
nbsMetaMibVariableIfIndex=_NbsMetaMibVariableIfIndex_Object((1,3,6,1,4,1,629,205,1,4,1,1),_NbsMetaMibVariableIfIndex_Type())
nbsMetaMibVariableIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsMetaMibVariableIfIndex.setStatus(_A)
_NbsMetaMibVariableID_Type=Integer32
_NbsMetaMibVariableID_Object=MibTableColumn
nbsMetaMibVariableID=_NbsMetaMibVariableID_Object((1,3,6,1,4,1,629,205,1,4,1,2),_NbsMetaMibVariableID_Type())
nbsMetaMibVariableID.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsMetaMibVariableID.setStatus(_A)
class _NbsMetaMibVariableCaps_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NbsMetaMibVariableCaps_Type.__name__=_C
_NbsMetaMibVariableCaps_Object=MibTableColumn
nbsMetaMibVariableCaps=_NbsMetaMibVariableCaps_Object((1,3,6,1,4,1,629,205,1,4,1,3),_NbsMetaMibVariableCaps_Type())
nbsMetaMibVariableCaps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibVariableCaps.setStatus(_A)
class _NbsMetaMibVariableDefault_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NbsMetaMibVariableDefault_Type.__name__=_C
_NbsMetaMibVariableDefault_Object=MibTableColumn
nbsMetaMibVariableDefault=_NbsMetaMibVariableDefault_Object((1,3,6,1,4,1,629,205,1,4,1,4),_NbsMetaMibVariableDefault_Type())
nbsMetaMibVariableDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibVariableDefault.setStatus(_A)
_NbsMetaMibVariableJumper_Type=DisplayString
_NbsMetaMibVariableJumper_Object=MibTableColumn
nbsMetaMibVariableJumper=_NbsMetaMibVariableJumper_Object((1,3,6,1,4,1,629,205,1,4,1,5),_NbsMetaMibVariableJumper_Type())
nbsMetaMibVariableJumper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibVariableJumper.setStatus(_A)
class _NbsMetaMibVariableOper_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NbsMetaMibVariableOper_Type.__name__=_C
_NbsMetaMibVariableOper_Object=MibTableColumn
nbsMetaMibVariableOper=_NbsMetaMibVariableOper_Object((1,3,6,1,4,1,629,205,1,4,1,6),_NbsMetaMibVariableOper_Type())
nbsMetaMibVariableOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibVariableOper.setStatus(_A)
class _NbsMetaMibVariableAdmin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NbsMetaMibVariableAdmin_Type.__name__=_C
_NbsMetaMibVariableAdmin_Object=MibTableColumn
nbsMetaMibVariableAdmin=_NbsMetaMibVariableAdmin_Object((1,3,6,1,4,1,629,205,1,4,1,7),_NbsMetaMibVariableAdmin_Type())
nbsMetaMibVariableAdmin.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbsMetaMibVariableAdmin.setStatus(_A)
class _NbsMetaMibVariableStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NbsMetaMibVariableStatus_Type.__name__=_C
_NbsMetaMibVariableStatus_Object=MibTableColumn
nbsMetaMibVariableStatus=_NbsMetaMibVariableStatus_Object((1,3,6,1,4,1,629,205,1,4,1,8),_NbsMetaMibVariableStatus_Type())
nbsMetaMibVariableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsMetaMibVariableStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsMetaMib':nbsMetaMib,'nbsMetaMibGrp':nbsMetaMibGrp,'nbsMetaMibFeatureTableSize':nbsMetaMibFeatureTableSize,'nbsMetaMibFeatureTable':nbsMetaMibFeatureTable,'nbsMetaMibFeatureEntry':nbsMetaMibFeatureEntry,_G:nbsMetaMibFeatureID,'nbsMetaMibFeatureFamily':nbsMetaMibFeatureFamily,'nbsMetaMibFeatureName':nbsMetaMibFeatureName,'nbsMetaMibFeatureDesc':nbsMetaMibFeatureDesc,'nbsMetaMibFeatureUnits':nbsMetaMibFeatureUnits,'nbsMetaMibFeatureType':nbsMetaMibFeatureType,'nbsMetaMibVariableTableSize':nbsMetaMibVariableTableSize,'nbsMetaMibVariableTable':nbsMetaMibVariableTable,'nbsMetaMibVariableEntry':nbsMetaMibVariableEntry,_H:nbsMetaMibVariableIfIndex,_I:nbsMetaMibVariableID,'nbsMetaMibVariableCaps':nbsMetaMibVariableCaps,'nbsMetaMibVariableDefault':nbsMetaMibVariableDefault,'nbsMetaMibVariableJumper':nbsMetaMibVariableJumper,'nbsMetaMibVariableOper':nbsMetaMibVariableOper,'nbsMetaMibVariableAdmin':nbsMetaMibVariableAdmin,'nbsMetaMibVariableStatus':nbsMetaMibVariableStatus})