_F='fruIndex'
_E='fruChassisIndex'
_D='DCS3FRU-MIB'
_C='DisplayString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
class DellObjectRange(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
class DellUnsigned8BitRange(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class DellUnsigned16BitRange(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class DellUnsigned32BitRange(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class DellDateName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(25,25));fixedLength=25
class DellStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('unknown',2),('ok',3),('nonCritical',4),('critical',5),('nonRecoverable',6)))
class DellFRUInformationState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ok',1),('notSupported',2),('notAvailable',3),('checksumInvalid',4),('corrupted',5)))
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,674))
_Server3_ObjectIdentity=ObjectIdentity
server3=_Server3_ObjectIdentity((1,3,6,1,4,1,674,10892))
_BaseboardGroup_ObjectIdentity=ObjectIdentity
baseboardGroup=_BaseboardGroup_ObjectIdentity((1,3,6,1,4,1,674,10892,1))
_FruGroup_ObjectIdentity=ObjectIdentity
fruGroup=_FruGroup_ObjectIdentity((1,3,6,1,4,1,674,10892,1,2000))
_FruTable_Object=MibTable
fruTable=_FruTable_Object((1,3,6,1,4,1,674,10892,1,2000,10))
if mibBuilder.loadTexts:fruTable.setStatus(_A)
_FruTableEntry_Object=MibTableRow
fruTableEntry=_FruTableEntry_Object((1,3,6,1,4,1,674,10892,1,2000,10,1))
fruTableEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:fruTableEntry.setStatus(_A)
_FruChassisIndex_Type=DellObjectRange
_FruChassisIndex_Object=MibTableColumn
fruChassisIndex=_FruChassisIndex_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,1),_FruChassisIndex_Type())
fruChassisIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fruChassisIndex.setStatus(_A)
_FruIndex_Type=DellObjectRange
_FruIndex_Object=MibTableColumn
fruIndex=_FruIndex_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,2),_FruIndex_Type())
fruIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fruIndex.setStatus(_A)
_FruInformationStatus_Type=DellStatus
_FruInformationStatus_Object=MibTableColumn
fruInformationStatus=_FruInformationStatus_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,3),_FruInformationStatus_Type())
fruInformationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fruInformationStatus.setStatus(_A)
_FruInformationState_Type=DellFRUInformationState
_FruInformationState_Object=MibTableColumn
fruInformationState=_FruInformationState_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,4),_FruInformationState_Type())
fruInformationState.setMaxAccess(_B)
if mibBuilder.loadTexts:fruInformationState.setStatus(_A)
class _FruDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FruDeviceName_Type.__name__=_C
_FruDeviceName_Object=MibTableColumn
fruDeviceName=_FruDeviceName_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,5),_FruDeviceName_Type())
fruDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:fruDeviceName.setStatus(_A)
class _FruManufacturerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FruManufacturerName_Type.__name__=_C
_FruManufacturerName_Object=MibTableColumn
fruManufacturerName=_FruManufacturerName_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,6),_FruManufacturerName_Type())
fruManufacturerName.setMaxAccess(_B)
if mibBuilder.loadTexts:fruManufacturerName.setStatus(_A)
class _FruSerialNumberName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FruSerialNumberName_Type.__name__=_C
_FruSerialNumberName_Object=MibTableColumn
fruSerialNumberName=_FruSerialNumberName_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,7),_FruSerialNumberName_Type())
fruSerialNumberName.setMaxAccess(_B)
if mibBuilder.loadTexts:fruSerialNumberName.setStatus(_A)
class _FruPartNumberName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FruPartNumberName_Type.__name__=_C
_FruPartNumberName_Object=MibTableColumn
fruPartNumberName=_FruPartNumberName_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,8),_FruPartNumberName_Type())
fruPartNumberName.setMaxAccess(_B)
if mibBuilder.loadTexts:fruPartNumberName.setStatus(_A)
class _FruRevisionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FruRevisionName_Type.__name__=_C
_FruRevisionName_Object=MibTableColumn
fruRevisionName=_FruRevisionName_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,9),_FruRevisionName_Type())
fruRevisionName.setMaxAccess(_B)
if mibBuilder.loadTexts:fruRevisionName.setStatus(_A)
_FruManufacturingDateName_Type=DellDateName
_FruManufacturingDateName_Object=MibTableColumn
fruManufacturingDateName=_FruManufacturingDateName_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,10),_FruManufacturingDateName_Type())
fruManufacturingDateName.setMaxAccess(_B)
if mibBuilder.loadTexts:fruManufacturingDateName.setStatus(_A)
class _FruAssetTagName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FruAssetTagName_Type.__name__=_C
_FruAssetTagName_Object=MibTableColumn
fruAssetTagName=_FruAssetTagName_Object((1,3,6,1,4,1,674,10892,1,2000,10,1,11),_FruAssetTagName_Type())
fruAssetTagName.setMaxAccess(_B)
if mibBuilder.loadTexts:fruAssetTagName.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'DellObjectRange':DellObjectRange,'DellUnsigned8BitRange':DellUnsigned8BitRange,'DellUnsigned16BitRange':DellUnsigned16BitRange,'DellUnsigned32BitRange':DellUnsigned32BitRange,'DellDateName':DellDateName,'DellStatus':DellStatus,'DellFRUInformationState':DellFRUInformationState,'dell':dell,'server3':server3,'baseboardGroup':baseboardGroup,'fruGroup':fruGroup,'fruTable':fruTable,'fruTableEntry':fruTableEntry,_E:fruChassisIndex,_F:fruIndex,'fruInformationStatus':fruInformationStatus,'fruInformationState':fruInformationState,'fruDeviceName':fruDeviceName,'fruManufacturerName':fruManufacturerName,'fruSerialNumberName':fruSerialNumberName,'fruPartNumberName':fruPartNumberName,'fruRevisionName':fruRevisionName,'fruManufacturingDateName':fruManufacturingDateName,'fruAssetTagName':fruAssetTagName})