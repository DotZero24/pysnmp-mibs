_J='hpnsaDIMMHPSlotIndex'
_I='hpnsaDIMMSlotIndex'
_H='hpnsaDIMMAgentIndex'
_G='OctetString'
_F='HPNSADIMM-MIB'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaDIMM_ObjectIdentity=ObjectIdentity
hpnsaDIMM=_HpnsaDIMM_ObjectIdentity((1,3,6,1,4,1,11,2,23,21))
_HpnsaDIMMMibRev_ObjectIdentity=ObjectIdentity
hpnsaDIMMMibRev=_HpnsaDIMMMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,21,1))
class _HpnsaDIMMMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaDIMMMibRevMajor_Type.__name__=_C
_HpnsaDIMMMibRevMajor_Object=MibScalar
hpnsaDIMMMibRevMajor=_HpnsaDIMMMibRevMajor_Object((1,3,6,1,4,1,11,2,23,21,1,1),_HpnsaDIMMMibRevMajor_Type())
hpnsaDIMMMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMMibRevMajor.setStatus(_A)
class _HpnsaDIMMMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaDIMMMibRevMinor_Type.__name__=_C
_HpnsaDIMMMibRevMinor_Object=MibScalar
hpnsaDIMMMibRevMinor=_HpnsaDIMMMibRevMinor_Object((1,3,6,1,4,1,11,2,23,21,1,2),_HpnsaDIMMMibRevMinor_Type())
hpnsaDIMMMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMMibRevMinor.setStatus(_A)
_HpnsaDIMMAgent_ObjectIdentity=ObjectIdentity
hpnsaDIMMAgent=_HpnsaDIMMAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,21,2))
_HpnsaDIMMAgentTable_Object=MibTable
hpnsaDIMMAgentTable=_HpnsaDIMMAgentTable_Object((1,3,6,1,4,1,11,2,23,21,2,1))
if mibBuilder.loadTexts:hpnsaDIMMAgentTable.setStatus(_A)
_HpnsaDIMMAgentEntry_Object=MibTableRow
hpnsaDIMMAgentEntry=_HpnsaDIMMAgentEntry_Object((1,3,6,1,4,1,11,2,23,21,2,1,1))
hpnsaDIMMAgentEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:hpnsaDIMMAgentEntry.setStatus(_A)
class _HpnsaDIMMAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaDIMMAgentIndex_Type.__name__=_C
_HpnsaDIMMAgentIndex_Object=MibTableColumn
hpnsaDIMMAgentIndex=_HpnsaDIMMAgentIndex_Object((1,3,6,1,4,1,11,2,23,21,2,1,1,1),_HpnsaDIMMAgentIndex_Type())
hpnsaDIMMAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMAgentIndex.setStatus(_A)
class _HpnsaDIMMAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaDIMMAgentName_Type.__name__=_D
_HpnsaDIMMAgentName_Object=MibTableColumn
hpnsaDIMMAgentName=_HpnsaDIMMAgentName_Object((1,3,6,1,4,1,11,2,23,21,2,1,1,2),_HpnsaDIMMAgentName_Type())
hpnsaDIMMAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMAgentName.setStatus(_A)
class _HpnsaDIMMAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnsaDIMMAgentVersion_Type.__name__=_D
_HpnsaDIMMAgentVersion_Object=MibTableColumn
hpnsaDIMMAgentVersion=_HpnsaDIMMAgentVersion_Object((1,3,6,1,4,1,11,2,23,21,2,1,1,3),_HpnsaDIMMAgentVersion_Type())
hpnsaDIMMAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMAgentVersion.setStatus(_A)
class _HpnsaDIMMAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_HpnsaDIMMAgentDate_Type.__name__=_G
_HpnsaDIMMAgentDate_Object=MibTableColumn
hpnsaDIMMAgentDate=_HpnsaDIMMAgentDate_Object((1,3,6,1,4,1,11,2,23,21,2,1,1,4),_HpnsaDIMMAgentDate_Type())
hpnsaDIMMAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMAgentDate.setStatus(_A)
_HpnsaDIMMInfo_ObjectIdentity=ObjectIdentity
hpnsaDIMMInfo=_HpnsaDIMMInfo_ObjectIdentity((1,3,6,1,4,1,11,2,23,21,3))
_HpnsaDIMMTable_Object=MibTable
hpnsaDIMMTable=_HpnsaDIMMTable_Object((1,3,6,1,4,1,11,2,23,21,3,1))
if mibBuilder.loadTexts:hpnsaDIMMTable.setStatus(_A)
_HpnsaDIMMEntry_Object=MibTableRow
hpnsaDIMMEntry=_HpnsaDIMMEntry_Object((1,3,6,1,4,1,11,2,23,21,3,1,1))
hpnsaDIMMEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:hpnsaDIMMEntry.setStatus(_A)
class _HpnsaDIMMSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaDIMMSlotIndex_Type.__name__=_C
_HpnsaDIMMSlotIndex_Object=MibTableColumn
hpnsaDIMMSlotIndex=_HpnsaDIMMSlotIndex_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,1),_HpnsaDIMMSlotIndex_Type())
hpnsaDIMMSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMSlotIndex.setStatus(_A)
_HpnsaDIMMSize_Type=Integer32
_HpnsaDIMMSize_Object=MibTableColumn
hpnsaDIMMSize=_HpnsaDIMMSize_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,2),_HpnsaDIMMSize_Type())
hpnsaDIMMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMSize.setStatus(_A)
class _HpnsaDIMMType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dimm-NONE',0),('dimm-Parity',1),('dimm-ECC',2)))
_HpnsaDIMMType_Type.__name__=_C
_HpnsaDIMMType_Object=MibTableColumn
hpnsaDIMMType=_HpnsaDIMMType_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,3),_HpnsaDIMMType_Type())
hpnsaDIMMType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMType.setStatus(_A)
_HpnsaDIMMSpeed_Type=Integer32
_HpnsaDIMMSpeed_Object=MibTableColumn
hpnsaDIMMSpeed=_HpnsaDIMMSpeed_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,4),_HpnsaDIMMSpeed_Type())
hpnsaDIMMSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMSpeed.setStatus(_A)
class _HpnsaDIMMManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaDIMMManufacturer_Type.__name__=_D
_HpnsaDIMMManufacturer_Object=MibTableColumn
hpnsaDIMMManufacturer=_HpnsaDIMMManufacturer_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,5),_HpnsaDIMMManufacturer_Type())
hpnsaDIMMManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMManufacturer.setStatus(_A)
class _HpnsaDIMMManufacturerPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaDIMMManufacturerPartNumber_Type.__name__=_D
_HpnsaDIMMManufacturerPartNumber_Object=MibTableColumn
hpnsaDIMMManufacturerPartNumber=_HpnsaDIMMManufacturerPartNumber_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,6),_HpnsaDIMMManufacturerPartNumber_Type())
hpnsaDIMMManufacturerPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMManufacturerPartNumber.setStatus(_A)
class _HpnsaDIMMManufactureDateCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HpnsaDIMMManufactureDateCode_Type.__name__=_G
_HpnsaDIMMManufactureDateCode_Object=MibScalar
hpnsaDIMMManufactureDateCode=_HpnsaDIMMManufactureDateCode_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,7),_HpnsaDIMMManufactureDateCode_Type())
hpnsaDIMMManufactureDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMManufactureDateCode.setStatus(_A)
class _HpnsaDIMMDramType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dimm-FastPageMode',1),('dimm-ExtendedDataOut',2),('dimm-PipelinedNibble',3),('dimm-Synchronous',4)))
_HpnsaDIMMDramType_Type.__name__=_C
_HpnsaDIMMDramType_Object=MibTableColumn
hpnsaDIMMDramType=_HpnsaDIMMDramType_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,8),_HpnsaDIMMDramType_Type())
hpnsaDIMMDramType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMDramType.setStatus(_A)
class _HpnsaDIMMSocketDesignation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaDIMMSocketDesignation_Type.__name__=_D
_HpnsaDIMMSocketDesignation_Object=MibTableColumn
hpnsaDIMMSocketDesignation=_HpnsaDIMMSocketDesignation_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,9),_HpnsaDIMMSocketDesignation_Type())
hpnsaDIMMSocketDesignation.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMSocketDesignation.setStatus(_A)
_HpnsaDIMMSoftwareStatus_Type=Integer32
_HpnsaDIMMSoftwareStatus_Object=MibTableColumn
hpnsaDIMMSoftwareStatus=_HpnsaDIMMSoftwareStatus_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,10),_HpnsaDIMMSoftwareStatus_Type())
hpnsaDIMMSoftwareStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnsaDIMMSoftwareStatus.setStatus(_A)
_HpnsaDIMMSingleBitEventCounter_Type=Integer32
_HpnsaDIMMSingleBitEventCounter_Object=MibTableColumn
hpnsaDIMMSingleBitEventCounter=_HpnsaDIMMSingleBitEventCounter_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,11),_HpnsaDIMMSingleBitEventCounter_Type())
hpnsaDIMMSingleBitEventCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnsaDIMMSingleBitEventCounter.setStatus(_A)
_HpnsaDIMMPredictiveEventCounter_Type=Integer32
_HpnsaDIMMPredictiveEventCounter_Object=MibTableColumn
hpnsaDIMMPredictiveEventCounter=_HpnsaDIMMPredictiveEventCounter_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,12),_HpnsaDIMMPredictiveEventCounter_Type())
hpnsaDIMMPredictiveEventCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnsaDIMMPredictiveEventCounter.setStatus(_A)
_HpnsaDIMMDoubleBitEventCounter_Type=Integer32
_HpnsaDIMMDoubleBitEventCounter_Object=MibTableColumn
hpnsaDIMMDoubleBitEventCounter=_HpnsaDIMMDoubleBitEventCounter_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,13),_HpnsaDIMMDoubleBitEventCounter_Type())
hpnsaDIMMDoubleBitEventCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnsaDIMMDoubleBitEventCounter.setStatus(_A)
_HpnsaDIMMMostSevereEventID_Type=Integer32
_HpnsaDIMMMostSevereEventID_Object=MibTableColumn
hpnsaDIMMMostSevereEventID=_HpnsaDIMMMostSevereEventID_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,14),_HpnsaDIMMMostSevereEventID_Type())
hpnsaDIMMMostSevereEventID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnsaDIMMMostSevereEventID.setStatus(_A)
_HpnsaDIMMHardwareStatus_Type=Integer32
_HpnsaDIMMHardwareStatus_Object=MibTableColumn
hpnsaDIMMHardwareStatus=_HpnsaDIMMHardwareStatus_Object((1,3,6,1,4,1,11,2,23,21,3,1,1,15),_HpnsaDIMMHardwareStatus_Type())
hpnsaDIMMHardwareStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnsaDIMMHardwareStatus.setStatus(_A)
_HpnsaDIMMHPLocalEntry_Object=MibTableRow
hpnsaDIMMHPLocalEntry=_HpnsaDIMMHPLocalEntry_Object((1,3,6,1,4,1,11,2,23,21,3,1,2))
hpnsaDIMMHPLocalEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:hpnsaDIMMHPLocalEntry.setStatus(_A)
class _HpnsaDIMMHPSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaDIMMHPSlotIndex_Type.__name__=_C
_HpnsaDIMMHPSlotIndex_Object=MibTableColumn
hpnsaDIMMHPSlotIndex=_HpnsaDIMMHPSlotIndex_Object((1,3,6,1,4,1,11,2,23,21,3,1,2,1),_HpnsaDIMMHPSlotIndex_Type())
hpnsaDIMMHPSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMHPSlotIndex.setStatus(_A)
class _HpnsaDIMMHPProductNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_HpnsaDIMMHPProductNumber_Type.__name__=_D
_HpnsaDIMMHPProductNumber_Object=MibTableColumn
hpnsaDIMMHPProductNumber=_HpnsaDIMMHPProductNumber_Object((1,3,6,1,4,1,11,2,23,21,3,1,2,2),_HpnsaDIMMHPProductNumber_Type())
hpnsaDIMMHPProductNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMHPProductNumber.setStatus(_A)
_HpnsaDIMMSerialNumber_Type=Integer32
_HpnsaDIMMSerialNumber_Object=MibScalar
hpnsaDIMMSerialNumber=_HpnsaDIMMSerialNumber_Object((1,3,6,1,4,1,11,2,23,21,3,1,2,3),_HpnsaDIMMSerialNumber_Type())
hpnsaDIMMSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaDIMMSerialNumber.setStatus(_A)
_HpnsaDIMMStatus_ObjectIdentity=ObjectIdentity
hpnsaDIMMStatus=_HpnsaDIMMStatus_ObjectIdentity((1,3,6,1,4,1,11,2,23,21,4))
_HpnsaDIMMOverallStatusSeverity_Type=Integer32
_HpnsaDIMMOverallStatusSeverity_Object=MibScalar
hpnsaDIMMOverallStatusSeverity=_HpnsaDIMMOverallStatusSeverity_Object((1,3,6,1,4,1,11,2,23,21,4,1),_HpnsaDIMMOverallStatusSeverity_Type())
hpnsaDIMMOverallStatusSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnsaDIMMOverallStatusSeverity.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaDIMM':hpnsaDIMM,'hpnsaDIMMMibRev':hpnsaDIMMMibRev,'hpnsaDIMMMibRevMajor':hpnsaDIMMMibRevMajor,'hpnsaDIMMMibRevMinor':hpnsaDIMMMibRevMinor,'hpnsaDIMMAgent':hpnsaDIMMAgent,'hpnsaDIMMAgentTable':hpnsaDIMMAgentTable,'hpnsaDIMMAgentEntry':hpnsaDIMMAgentEntry,_H:hpnsaDIMMAgentIndex,'hpnsaDIMMAgentName':hpnsaDIMMAgentName,'hpnsaDIMMAgentVersion':hpnsaDIMMAgentVersion,'hpnsaDIMMAgentDate':hpnsaDIMMAgentDate,'hpnsaDIMMInfo':hpnsaDIMMInfo,'hpnsaDIMMTable':hpnsaDIMMTable,'hpnsaDIMMEntry':hpnsaDIMMEntry,_I:hpnsaDIMMSlotIndex,'hpnsaDIMMSize':hpnsaDIMMSize,'hpnsaDIMMType':hpnsaDIMMType,'hpnsaDIMMSpeed':hpnsaDIMMSpeed,'hpnsaDIMMManufacturer':hpnsaDIMMManufacturer,'hpnsaDIMMManufacturerPartNumber':hpnsaDIMMManufacturerPartNumber,'hpnsaDIMMManufactureDateCode':hpnsaDIMMManufactureDateCode,'hpnsaDIMMDramType':hpnsaDIMMDramType,'hpnsaDIMMSocketDesignation':hpnsaDIMMSocketDesignation,'hpnsaDIMMSoftwareStatus':hpnsaDIMMSoftwareStatus,'hpnsaDIMMSingleBitEventCounter':hpnsaDIMMSingleBitEventCounter,'hpnsaDIMMPredictiveEventCounter':hpnsaDIMMPredictiveEventCounter,'hpnsaDIMMDoubleBitEventCounter':hpnsaDIMMDoubleBitEventCounter,'hpnsaDIMMMostSevereEventID':hpnsaDIMMMostSevereEventID,'hpnsaDIMMHardwareStatus':hpnsaDIMMHardwareStatus,'hpnsaDIMMHPLocalEntry':hpnsaDIMMHPLocalEntry,_J:hpnsaDIMMHPSlotIndex,'hpnsaDIMMHPProductNumber':hpnsaDIMMHPProductNumber,'hpnsaDIMMSerialNumber':hpnsaDIMMSerialNumber,'hpnsaDIMMStatus':hpnsaDIMMStatus,'hpnsaDIMMOverallStatusSeverity':hpnsaDIMMOverallStatusSeverity})