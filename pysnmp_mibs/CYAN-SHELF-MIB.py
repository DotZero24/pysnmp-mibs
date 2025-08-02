_g='cyanShelfObjectGroup'
_f='cyanShelfType'
_e='cyanShelfSecServState'
_d='cyanShelfRelayRack'
_c='cyanShelfRackUnits'
_b='cyanShelfOwner'
_a='cyanShelfOssLabel'
_Z='cyanShelfOperStateQual'
_Y='cyanShelfOperState'
_X='cyanShelfOidClass'
_W='cyanShelfName'
_V='cyanShelfMfgSerialNumber'
_U='cyanShelfMfgRevision'
_T='cyanShelfMfgPartNumber'
_S='cyanShelfMfgModuleId'
_R='cyanShelfMfgEciCode'
_Q='cyanShelfMfgCleiCode'
_P='cyanShelfMacBlockSize'
_O='cyanShelfIdentifier'
_N='cyanShelfFanSpeed'
_M='cyanShelfFanFilterReplacingIntervalDays'
_L='cyanShelfDescription'
_K='cyanShelfDaysSinceLastReplacement'
_J='cyanShelfBay'
_I='cyanShelfBaseMacAddress'
_H='cyanShelfAutoprovisioningFlag'
_G='cyanShelfAssetTag'
_F='cyanShelfShelfId'
_E='Unsigned32'
_D='DisplayString'
_C='read-only'
_B='CYAN-SHELF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CyanTypeTc,cyanEntityModules=mibBuilder.importSymbols('CYAN-MIB','CyanTypeTc','cyanEntityModules')
CyanNoYesTc,CyanOpStateQualTc,CyanOpStateTc,CyanSecServiceStateTc=mibBuilder.importSymbols('CYAN-TC-MIB','CyanNoYesTc','CyanOpStateQualTc','CyanOpStateTc','CyanSecServiceStateTc')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
cyanShelfModule=ModuleIdentity((1,3,6,1,4,1,28533,5,30,20))
if mibBuilder.loadTexts:cyanShelfModule.setRevisions(('2014-12-07 05:45',))
_CyanShelfMibObjects_ObjectIdentity=ObjectIdentity
cyanShelfMibObjects=_CyanShelfMibObjects_ObjectIdentity((1,3,6,1,4,1,28533,5,30,20,1))
_CyanShelfTable_Object=MibTable
cyanShelfTable=_CyanShelfTable_Object((1,3,6,1,4,1,28533,5,30,20,1,1))
if mibBuilder.loadTexts:cyanShelfTable.setStatus(_A)
_CyanShelfEntry_Object=MibTableRow
cyanShelfEntry=_CyanShelfEntry_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1))
cyanShelfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cyanShelfEntry.setStatus(_A)
class _CyanShelfShelfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanShelfShelfId_Type.__name__=_E
_CyanShelfShelfId_Object=MibTableColumn
cyanShelfShelfId=_CyanShelfShelfId_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,1),_CyanShelfShelfId_Type())
cyanShelfShelfId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cyanShelfShelfId.setStatus(_A)
class _CyanShelfAssetTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,124))
_CyanShelfAssetTag_Type.__name__=_D
_CyanShelfAssetTag_Object=MibTableColumn
cyanShelfAssetTag=_CyanShelfAssetTag_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,2),_CyanShelfAssetTag_Type())
cyanShelfAssetTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfAssetTag.setStatus(_A)
_CyanShelfAutoprovisioningFlag_Type=CyanNoYesTc
_CyanShelfAutoprovisioningFlag_Object=MibTableColumn
cyanShelfAutoprovisioningFlag=_CyanShelfAutoprovisioningFlag_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,3),_CyanShelfAutoprovisioningFlag_Type())
cyanShelfAutoprovisioningFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfAutoprovisioningFlag.setStatus(_A)
_CyanShelfBaseMacAddress_Type=DisplayString
_CyanShelfBaseMacAddress_Object=MibTableColumn
cyanShelfBaseMacAddress=_CyanShelfBaseMacAddress_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,4),_CyanShelfBaseMacAddress_Type())
cyanShelfBaseMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfBaseMacAddress.setStatus(_A)
class _CyanShelfBay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CyanShelfBay_Type.__name__=_D
_CyanShelfBay_Object=MibTableColumn
cyanShelfBay=_CyanShelfBay_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,5),_CyanShelfBay_Type())
cyanShelfBay.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfBay.setStatus(_A)
_CyanShelfDaysSinceLastReplacement_Type=Unsigned32
_CyanShelfDaysSinceLastReplacement_Object=MibTableColumn
cyanShelfDaysSinceLastReplacement=_CyanShelfDaysSinceLastReplacement_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,6),_CyanShelfDaysSinceLastReplacement_Type())
cyanShelfDaysSinceLastReplacement.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfDaysSinceLastReplacement.setStatus(_A)
class _CyanShelfDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CyanShelfDescription_Type.__name__=_D
_CyanShelfDescription_Object=MibTableColumn
cyanShelfDescription=_CyanShelfDescription_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,7),_CyanShelfDescription_Type())
cyanShelfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfDescription.setStatus(_A)
_CyanShelfFanFilterReplacingIntervalDays_Type=Unsigned32
_CyanShelfFanFilterReplacingIntervalDays_Object=MibTableColumn
cyanShelfFanFilterReplacingIntervalDays=_CyanShelfFanFilterReplacingIntervalDays_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,8),_CyanShelfFanFilterReplacingIntervalDays_Type())
cyanShelfFanFilterReplacingIntervalDays.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfFanFilterReplacingIntervalDays.setStatus(_A)
_CyanShelfFanSpeed_Type=Integer32
_CyanShelfFanSpeed_Object=MibTableColumn
cyanShelfFanSpeed=_CyanShelfFanSpeed_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,9),_CyanShelfFanSpeed_Type())
cyanShelfFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfFanSpeed.setStatus(_A)
_CyanShelfIdentifier_Type=DisplayString
_CyanShelfIdentifier_Object=MibTableColumn
cyanShelfIdentifier=_CyanShelfIdentifier_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,10),_CyanShelfIdentifier_Type())
cyanShelfIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfIdentifier.setStatus(_A)
class _CyanShelfMacBlockSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanShelfMacBlockSize_Type.__name__=_E
_CyanShelfMacBlockSize_Object=MibTableColumn
cyanShelfMacBlockSize=_CyanShelfMacBlockSize_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,11),_CyanShelfMacBlockSize_Type())
cyanShelfMacBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfMacBlockSize.setStatus(_A)
class _CyanShelfMfgCleiCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CyanShelfMfgCleiCode_Type.__name__=_D
_CyanShelfMfgCleiCode_Object=MibTableColumn
cyanShelfMfgCleiCode=_CyanShelfMfgCleiCode_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,12),_CyanShelfMfgCleiCode_Type())
cyanShelfMfgCleiCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfMfgCleiCode.setStatus(_A)
class _CyanShelfMfgEciCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_CyanShelfMfgEciCode_Type.__name__=_D
_CyanShelfMfgEciCode_Object=MibTableColumn
cyanShelfMfgEciCode=_CyanShelfMfgEciCode_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,13),_CyanShelfMfgEciCode_Type())
cyanShelfMfgEciCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfMfgEciCode.setStatus(_A)
_CyanShelfMfgModuleId_Type=Unsigned32
_CyanShelfMfgModuleId_Object=MibTableColumn
cyanShelfMfgModuleId=_CyanShelfMfgModuleId_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,14),_CyanShelfMfgModuleId_Type())
cyanShelfMfgModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfMfgModuleId.setStatus(_A)
class _CyanShelfMfgPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CyanShelfMfgPartNumber_Type.__name__=_D
_CyanShelfMfgPartNumber_Object=MibTableColumn
cyanShelfMfgPartNumber=_CyanShelfMfgPartNumber_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,15),_CyanShelfMfgPartNumber_Type())
cyanShelfMfgPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfMfgPartNumber.setStatus(_A)
class _CyanShelfMfgRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CyanShelfMfgRevision_Type.__name__=_D
_CyanShelfMfgRevision_Object=MibTableColumn
cyanShelfMfgRevision=_CyanShelfMfgRevision_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,16),_CyanShelfMfgRevision_Type())
cyanShelfMfgRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfMfgRevision.setStatus(_A)
class _CyanShelfMfgSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CyanShelfMfgSerialNumber_Type.__name__=_D
_CyanShelfMfgSerialNumber_Object=MibTableColumn
cyanShelfMfgSerialNumber=_CyanShelfMfgSerialNumber_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,17),_CyanShelfMfgSerialNumber_Type())
cyanShelfMfgSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfMfgSerialNumber.setStatus(_A)
_CyanShelfName_Type=DisplayString
_CyanShelfName_Object=MibTableColumn
cyanShelfName=_CyanShelfName_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,18),_CyanShelfName_Type())
cyanShelfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfName.setStatus(_A)
_CyanShelfOidClass_Type=DisplayString
_CyanShelfOidClass_Object=MibTableColumn
cyanShelfOidClass=_CyanShelfOidClass_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,19),_CyanShelfOidClass_Type())
cyanShelfOidClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfOidClass.setStatus(_A)
_CyanShelfOperState_Type=CyanOpStateTc
_CyanShelfOperState_Object=MibTableColumn
cyanShelfOperState=_CyanShelfOperState_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,20),_CyanShelfOperState_Type())
cyanShelfOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfOperState.setStatus(_A)
_CyanShelfOperStateQual_Type=CyanOpStateQualTc
_CyanShelfOperStateQual_Object=MibTableColumn
cyanShelfOperStateQual=_CyanShelfOperStateQual_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,21),_CyanShelfOperStateQual_Type())
cyanShelfOperStateQual.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfOperStateQual.setStatus(_A)
class _CyanShelfOssLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CyanShelfOssLabel_Type.__name__=_D
_CyanShelfOssLabel_Object=MibTableColumn
cyanShelfOssLabel=_CyanShelfOssLabel_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,22),_CyanShelfOssLabel_Type())
cyanShelfOssLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfOssLabel.setStatus(_A)
class _CyanShelfOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CyanShelfOwner_Type.__name__=_D
_CyanShelfOwner_Object=MibTableColumn
cyanShelfOwner=_CyanShelfOwner_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,23),_CyanShelfOwner_Type())
cyanShelfOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfOwner.setStatus(_A)
class _CyanShelfRackUnits_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CyanShelfRackUnits_Type.__name__=_D
_CyanShelfRackUnits_Object=MibTableColumn
cyanShelfRackUnits=_CyanShelfRackUnits_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,24),_CyanShelfRackUnits_Type())
cyanShelfRackUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfRackUnits.setStatus(_A)
class _CyanShelfRelayRack_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CyanShelfRelayRack_Type.__name__=_D
_CyanShelfRelayRack_Object=MibTableColumn
cyanShelfRelayRack=_CyanShelfRelayRack_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,25),_CyanShelfRelayRack_Type())
cyanShelfRelayRack.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfRelayRack.setStatus(_A)
_CyanShelfSecServState_Type=CyanSecServiceStateTc
_CyanShelfSecServState_Object=MibTableColumn
cyanShelfSecServState=_CyanShelfSecServState_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,26),_CyanShelfSecServState_Type())
cyanShelfSecServState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfSecServState.setStatus(_A)
_CyanShelfType_Type=CyanTypeTc
_CyanShelfType_Object=MibTableColumn
cyanShelfType=_CyanShelfType_Object((1,3,6,1,4,1,28533,5,30,20,1,1,1,27),_CyanShelfType_Type())
cyanShelfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanShelfType.setStatus(_A)
cyanShelfObjectGroup=ObjectGroup((1,3,6,1,4,1,28533,5,30,20,20))
cyanShelfObjectGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:cyanShelfObjectGroup.setStatus(_A)
cyanShelfCompliance=ModuleCompliance((1,3,6,1,4,1,28533,5,30,20,30))
cyanShelfCompliance.setObjects((_B,_g))
if mibBuilder.loadTexts:cyanShelfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cyanShelfModule':cyanShelfModule,'cyanShelfMibObjects':cyanShelfMibObjects,'cyanShelfTable':cyanShelfTable,'cyanShelfEntry':cyanShelfEntry,_F:cyanShelfShelfId,_G:cyanShelfAssetTag,_H:cyanShelfAutoprovisioningFlag,_I:cyanShelfBaseMacAddress,_J:cyanShelfBay,_K:cyanShelfDaysSinceLastReplacement,_L:cyanShelfDescription,_M:cyanShelfFanFilterReplacingIntervalDays,_N:cyanShelfFanSpeed,_O:cyanShelfIdentifier,_P:cyanShelfMacBlockSize,_Q:cyanShelfMfgCleiCode,_R:cyanShelfMfgEciCode,_S:cyanShelfMfgModuleId,_T:cyanShelfMfgPartNumber,_U:cyanShelfMfgRevision,_V:cyanShelfMfgSerialNumber,_W:cyanShelfName,_X:cyanShelfOidClass,_Y:cyanShelfOperState,_Z:cyanShelfOperStateQual,_a:cyanShelfOssLabel,_b:cyanShelfOwner,_c:cyanShelfRackUnits,_d:cyanShelfRelayRack,_e:cyanShelfSecServState,_f:cyanShelfType,_g:cyanShelfObjectGroup,'cyanShelfCompliance':cyanShelfCompliance})