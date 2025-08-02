_h='cyanFanObjectGroup'
_g='cyanFanType'
_f='cyanFanSecServState'
_e='cyanFanPowerLed'
_d='cyanFanPartNumber'
_c='cyanFanOwner'
_b='cyanFanOssLabel'
_a='cyanFanOperStateQual'
_Z='cyanFanOperState'
_Y='cyanFanOidClass'
_X='cyanFanName'
_W='cyanFanMfgSerialNumber'
_V='cyanFanMfgRevision'
_U='cyanFanMfgPartNumber'
_T='cyanFanMfgModuleId'
_S='cyanFanMfgEciCode'
_R='cyanFanMfgCleiCode'
_Q='cyanFanMacBlockSize'
_P='cyanFanIdentifier'
_O='cyanFanHotSwapLed'
_N='cyanFanDescription'
_M='cyanFanBaseMacAddress'
_L='cyanFanAutoinserviceSoakTimeSec'
_K='cyanFanAssetTag'
_J='cyanFanAlarmLed'
_I='cyanFanAdminState'
_H='not-accessible'
_G='cyanFanFanId'
_F='cyanFanShelfId'
_E='Unsigned32'
_D='DisplayString'
_C='read-only'
_B='CYAN-FAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CyanTypeTc,cyanEntityModules=mibBuilder.importSymbols('CYAN-MIB','CyanTypeTc','cyanEntityModules')
CyanAdminStateTc,CyanLEDTc,CyanOpStateQualTc,CyanOpStateTc,CyanSecServiceStateTc=mibBuilder.importSymbols('CYAN-TC-MIB','CyanAdminStateTc','CyanLEDTc','CyanOpStateQualTc','CyanOpStateTc','CyanSecServiceStateTc')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
cyanFanModule=ModuleIdentity((1,3,6,1,4,1,28533,5,30,40))
if mibBuilder.loadTexts:cyanFanModule.setRevisions(('2014-12-07 05:45',))
_CyanFanMibObjects_ObjectIdentity=ObjectIdentity
cyanFanMibObjects=_CyanFanMibObjects_ObjectIdentity((1,3,6,1,4,1,28533,5,30,40,1))
_CyanFanTable_Object=MibTable
cyanFanTable=_CyanFanTable_Object((1,3,6,1,4,1,28533,5,30,40,1,1))
if mibBuilder.loadTexts:cyanFanTable.setStatus(_A)
_CyanFanEntry_Object=MibTableRow
cyanFanEntry=_CyanFanEntry_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1))
cyanFanEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cyanFanEntry.setStatus(_A)
class _CyanFanShelfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanFanShelfId_Type.__name__=_E
_CyanFanShelfId_Object=MibTableColumn
cyanFanShelfId=_CyanFanShelfId_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,1),_CyanFanShelfId_Type())
cyanFanShelfId.setMaxAccess(_H)
if mibBuilder.loadTexts:cyanFanShelfId.setStatus(_A)
_CyanFanFanId_Type=Unsigned32
_CyanFanFanId_Object=MibTableColumn
cyanFanFanId=_CyanFanFanId_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,2),_CyanFanFanId_Type())
cyanFanFanId.setMaxAccess(_H)
if mibBuilder.loadTexts:cyanFanFanId.setStatus(_A)
_CyanFanAdminState_Type=CyanAdminStateTc
_CyanFanAdminState_Object=MibTableColumn
cyanFanAdminState=_CyanFanAdminState_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,3),_CyanFanAdminState_Type())
cyanFanAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanAdminState.setStatus(_A)
_CyanFanAlarmLed_Type=CyanLEDTc
_CyanFanAlarmLed_Object=MibTableColumn
cyanFanAlarmLed=_CyanFanAlarmLed_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,4),_CyanFanAlarmLed_Type())
cyanFanAlarmLed.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanAlarmLed.setStatus(_A)
class _CyanFanAssetTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,124))
_CyanFanAssetTag_Type.__name__=_D
_CyanFanAssetTag_Object=MibTableColumn
cyanFanAssetTag=_CyanFanAssetTag_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,5),_CyanFanAssetTag_Type())
cyanFanAssetTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanAssetTag.setStatus(_A)
_CyanFanAutoinserviceSoakTimeSec_Type=Integer32
_CyanFanAutoinserviceSoakTimeSec_Object=MibTableColumn
cyanFanAutoinserviceSoakTimeSec=_CyanFanAutoinserviceSoakTimeSec_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,6),_CyanFanAutoinserviceSoakTimeSec_Type())
cyanFanAutoinserviceSoakTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanAutoinserviceSoakTimeSec.setStatus(_A)
_CyanFanBaseMacAddress_Type=DisplayString
_CyanFanBaseMacAddress_Object=MibTableColumn
cyanFanBaseMacAddress=_CyanFanBaseMacAddress_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,7),_CyanFanBaseMacAddress_Type())
cyanFanBaseMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanBaseMacAddress.setStatus(_A)
class _CyanFanDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CyanFanDescription_Type.__name__=_D
_CyanFanDescription_Object=MibTableColumn
cyanFanDescription=_CyanFanDescription_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,8),_CyanFanDescription_Type())
cyanFanDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanDescription.setStatus(_A)
_CyanFanHotSwapLed_Type=CyanLEDTc
_CyanFanHotSwapLed_Object=MibTableColumn
cyanFanHotSwapLed=_CyanFanHotSwapLed_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,9),_CyanFanHotSwapLed_Type())
cyanFanHotSwapLed.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanHotSwapLed.setStatus(_A)
_CyanFanIdentifier_Type=DisplayString
_CyanFanIdentifier_Object=MibTableColumn
cyanFanIdentifier=_CyanFanIdentifier_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,10),_CyanFanIdentifier_Type())
cyanFanIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanIdentifier.setStatus(_A)
class _CyanFanMacBlockSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanFanMacBlockSize_Type.__name__=_E
_CyanFanMacBlockSize_Object=MibTableColumn
cyanFanMacBlockSize=_CyanFanMacBlockSize_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,11),_CyanFanMacBlockSize_Type())
cyanFanMacBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanMacBlockSize.setStatus(_A)
class _CyanFanMfgCleiCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CyanFanMfgCleiCode_Type.__name__=_D
_CyanFanMfgCleiCode_Object=MibTableColumn
cyanFanMfgCleiCode=_CyanFanMfgCleiCode_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,12),_CyanFanMfgCleiCode_Type())
cyanFanMfgCleiCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanMfgCleiCode.setStatus(_A)
class _CyanFanMfgEciCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_CyanFanMfgEciCode_Type.__name__=_D
_CyanFanMfgEciCode_Object=MibTableColumn
cyanFanMfgEciCode=_CyanFanMfgEciCode_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,13),_CyanFanMfgEciCode_Type())
cyanFanMfgEciCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanMfgEciCode.setStatus(_A)
_CyanFanMfgModuleId_Type=Unsigned32
_CyanFanMfgModuleId_Object=MibTableColumn
cyanFanMfgModuleId=_CyanFanMfgModuleId_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,14),_CyanFanMfgModuleId_Type())
cyanFanMfgModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanMfgModuleId.setStatus(_A)
class _CyanFanMfgPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CyanFanMfgPartNumber_Type.__name__=_D
_CyanFanMfgPartNumber_Object=MibTableColumn
cyanFanMfgPartNumber=_CyanFanMfgPartNumber_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,15),_CyanFanMfgPartNumber_Type())
cyanFanMfgPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanMfgPartNumber.setStatus(_A)
class _CyanFanMfgRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CyanFanMfgRevision_Type.__name__=_D
_CyanFanMfgRevision_Object=MibTableColumn
cyanFanMfgRevision=_CyanFanMfgRevision_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,16),_CyanFanMfgRevision_Type())
cyanFanMfgRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanMfgRevision.setStatus(_A)
class _CyanFanMfgSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CyanFanMfgSerialNumber_Type.__name__=_D
_CyanFanMfgSerialNumber_Object=MibTableColumn
cyanFanMfgSerialNumber=_CyanFanMfgSerialNumber_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,17),_CyanFanMfgSerialNumber_Type())
cyanFanMfgSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanMfgSerialNumber.setStatus(_A)
_CyanFanName_Type=DisplayString
_CyanFanName_Object=MibTableColumn
cyanFanName=_CyanFanName_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,18),_CyanFanName_Type())
cyanFanName.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanName.setStatus(_A)
_CyanFanOidClass_Type=DisplayString
_CyanFanOidClass_Object=MibTableColumn
cyanFanOidClass=_CyanFanOidClass_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,19),_CyanFanOidClass_Type())
cyanFanOidClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanOidClass.setStatus(_A)
_CyanFanOperState_Type=CyanOpStateTc
_CyanFanOperState_Object=MibTableColumn
cyanFanOperState=_CyanFanOperState_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,20),_CyanFanOperState_Type())
cyanFanOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanOperState.setStatus(_A)
_CyanFanOperStateQual_Type=CyanOpStateQualTc
_CyanFanOperStateQual_Object=MibTableColumn
cyanFanOperStateQual=_CyanFanOperStateQual_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,21),_CyanFanOperStateQual_Type())
cyanFanOperStateQual.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanOperStateQual.setStatus(_A)
class _CyanFanOssLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CyanFanOssLabel_Type.__name__=_D
_CyanFanOssLabel_Object=MibTableColumn
cyanFanOssLabel=_CyanFanOssLabel_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,22),_CyanFanOssLabel_Type())
cyanFanOssLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanOssLabel.setStatus(_A)
class _CyanFanOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CyanFanOwner_Type.__name__=_D
_CyanFanOwner_Object=MibTableColumn
cyanFanOwner=_CyanFanOwner_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,23),_CyanFanOwner_Type())
cyanFanOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanOwner.setStatus(_A)
class _CyanFanPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_CyanFanPartNumber_Type.__name__=_D
_CyanFanPartNumber_Object=MibTableColumn
cyanFanPartNumber=_CyanFanPartNumber_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,24),_CyanFanPartNumber_Type())
cyanFanPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanPartNumber.setStatus(_A)
_CyanFanPowerLed_Type=CyanLEDTc
_CyanFanPowerLed_Object=MibTableColumn
cyanFanPowerLed=_CyanFanPowerLed_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,25),_CyanFanPowerLed_Type())
cyanFanPowerLed.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanPowerLed.setStatus(_A)
_CyanFanSecServState_Type=CyanSecServiceStateTc
_CyanFanSecServState_Object=MibTableColumn
cyanFanSecServState=_CyanFanSecServState_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,26),_CyanFanSecServState_Type())
cyanFanSecServState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanSecServState.setStatus(_A)
_CyanFanType_Type=CyanTypeTc
_CyanFanType_Object=MibTableColumn
cyanFanType=_CyanFanType_Object((1,3,6,1,4,1,28533,5,30,40,1,1,1,27),_CyanFanType_Type())
cyanFanType.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanFanType.setStatus(_A)
cyanFanObjectGroup=ObjectGroup((1,3,6,1,4,1,28533,5,30,40,20))
cyanFanObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cyanFanObjectGroup.setStatus(_A)
cyanFanCompliance=ModuleCompliance((1,3,6,1,4,1,28533,5,30,40,30))
cyanFanCompliance.setObjects((_B,_h))
if mibBuilder.loadTexts:cyanFanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cyanFanModule':cyanFanModule,'cyanFanMibObjects':cyanFanMibObjects,'cyanFanTable':cyanFanTable,'cyanFanEntry':cyanFanEntry,_F:cyanFanShelfId,_G:cyanFanFanId,_I:cyanFanAdminState,_J:cyanFanAlarmLed,_K:cyanFanAssetTag,_L:cyanFanAutoinserviceSoakTimeSec,_M:cyanFanBaseMacAddress,_N:cyanFanDescription,_O:cyanFanHotSwapLed,_P:cyanFanIdentifier,_Q:cyanFanMacBlockSize,_R:cyanFanMfgCleiCode,_S:cyanFanMfgEciCode,_T:cyanFanMfgModuleId,_U:cyanFanMfgPartNumber,_V:cyanFanMfgRevision,_W:cyanFanMfgSerialNumber,_X:cyanFanName,_Y:cyanFanOidClass,_Z:cyanFanOperState,_a:cyanFanOperStateQual,_b:cyanFanOssLabel,_c:cyanFanOwner,_d:cyanFanPartNumber,_e:cyanFanPowerLed,_f:cyanFanSecServState,_g:cyanFanType,_h:cyanFanObjectGroup,'cyanFanCompliance':cyanFanCompliance})