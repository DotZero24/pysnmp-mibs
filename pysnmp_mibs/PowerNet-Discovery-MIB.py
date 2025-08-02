_O='apcDiscoveryDeviceAlarmStateChangeCount'
_N='apcTrapRecvIndex'
_M='apcDiscoveryDeviceAlarmStateTableIndex'
_L='apcDiscoveryDeviceDefTableIndex'
_K='apcDiscoveryDeviceProtocolTableIndex'
_J='apcDiscoveryDeviceFirmwareTableIndex'
_I='unknown'
_H='apcDiscoveryInfoTableIndex'
_G='NotificationType'
_F='read-write'
_E='DisplayString'
_D='Integer32'
_C='PowerNet-Discovery-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Apc_ObjectIdentity=ObjectIdentity
apc=_Apc_ObjectIdentity((1,3,6,1,4,1,318))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,318,1))
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,318,1,1))
_Software_ObjectIdentity=ObjectIdentity
software=_Software_ObjectIdentity((1,3,6,1,4,1,318,1,2))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,318,1,3))
_Experimental_ObjectIdentity=ObjectIdentity
experimental=_Experimental_ObjectIdentity((1,3,6,1,4,1,318,1,4))
_ApcDiscovery_ObjectIdentity=ObjectIdentity
apcDiscovery=_ApcDiscovery_ObjectIdentity((1,3,6,1,4,1,318,1,4,2))
_ApcDiscoveryInfoTableSize_Type=Integer32
_ApcDiscoveryInfoTableSize_Object=MibScalar
apcDiscoveryInfoTableSize=_ApcDiscoveryInfoTableSize_Object((1,3,6,1,4,1,318,1,4,2,1),_ApcDiscoveryInfoTableSize_Type())
apcDiscoveryInfoTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryInfoTableSize.setStatus(_A)
_ApcDiscoveryInfoTable_Object=MibTable
apcDiscoveryInfoTable=_ApcDiscoveryInfoTable_Object((1,3,6,1,4,1,318,1,4,2,2))
if mibBuilder.loadTexts:apcDiscoveryInfoTable.setStatus(_A)
_ApcDiscoveryInfoEntry_Object=MibTableRow
apcDiscoveryInfoEntry=_ApcDiscoveryInfoEntry_Object((1,3,6,1,4,1,318,1,4,2,2,1))
apcDiscoveryInfoEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:apcDiscoveryInfoEntry.setStatus(_A)
_ApcDiscoveryInfoTableIndex_Type=Integer32
_ApcDiscoveryInfoTableIndex_Object=MibTableColumn
apcDiscoveryInfoTableIndex=_ApcDiscoveryInfoTableIndex_Object((1,3,6,1,4,1,318,1,4,2,2,1,1),_ApcDiscoveryInfoTableIndex_Type())
apcDiscoveryInfoTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryInfoTableIndex.setStatus(_A)
_ApcDiscoveryModel_Type=DisplayString
_ApcDiscoveryModel_Object=MibTableColumn
apcDiscoveryModel=_ApcDiscoveryModel_Object((1,3,6,1,4,1,318,1,4,2,2,1,2),_ApcDiscoveryModel_Type())
apcDiscoveryModel.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryModel.setStatus(_A)
_ApcDiscoverySerialNumber_Type=DisplayString
_ApcDiscoverySerialNumber_Object=MibTableColumn
apcDiscoverySerialNumber=_ApcDiscoverySerialNumber_Object((1,3,6,1,4,1,318,1,4,2,2,1,3),_ApcDiscoverySerialNumber_Type())
apcDiscoverySerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoverySerialNumber.setStatus(_A)
class _ApcDiscoveryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),('deviceNormal',2),('deviceWarning',3),('deviceSevere',4),('deviceLostCom',5)))
_ApcDiscoveryStatus_Type.__name__=_D
_ApcDiscoveryStatus_Object=MibTableColumn
apcDiscoveryStatus=_ApcDiscoveryStatus_Object((1,3,6,1,4,1,318,1,4,2,2,1,4),_ApcDiscoveryStatus_Type())
apcDiscoveryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryStatus.setStatus(_A)
_ApcDiscoveryLabelString_Type=DisplayString
_ApcDiscoveryLabelString_Object=MibTableColumn
apcDiscoveryLabelString=_ApcDiscoveryLabelString_Object((1,3,6,1,4,1,318,1,4,2,2,1,5),_ApcDiscoveryLabelString_Type())
apcDiscoveryLabelString.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryLabelString.setStatus(_A)
_ApcDiscoveryDeviceHierarchy_Type=DisplayString
_ApcDiscoveryDeviceHierarchy_Object=MibTableColumn
apcDiscoveryDeviceHierarchy=_ApcDiscoveryDeviceHierarchy_Object((1,3,6,1,4,1,318,1,4,2,2,1,6),_ApcDiscoveryDeviceHierarchy_Type())
apcDiscoveryDeviceHierarchy.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceHierarchy.setStatus(_A)
_ApcDiscoveryDeviceLocation_Type=DisplayString
_ApcDiscoveryDeviceLocation_Object=MibTableColumn
apcDiscoveryDeviceLocation=_ApcDiscoveryDeviceLocation_Object((1,3,6,1,4,1,318,1,4,2,2,1,7),_ApcDiscoveryDeviceLocation_Type())
apcDiscoveryDeviceLocation.setMaxAccess(_F)
if mibBuilder.loadTexts:apcDiscoveryDeviceLocation.setStatus(_A)
_ApcDiscoveryDeviceLocationMaxLength_Type=Integer32
_ApcDiscoveryDeviceLocationMaxLength_Object=MibTableColumn
apcDiscoveryDeviceLocationMaxLength=_ApcDiscoveryDeviceLocationMaxLength_Object((1,3,6,1,4,1,318,1,4,2,2,1,8),_ApcDiscoveryDeviceLocationMaxLength_Type())
apcDiscoveryDeviceLocationMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceLocationMaxLength.setStatus(_A)
_ApcDiscoveryDeviceName_Type=DisplayString
_ApcDiscoveryDeviceName_Object=MibTableColumn
apcDiscoveryDeviceName=_ApcDiscoveryDeviceName_Object((1,3,6,1,4,1,318,1,4,2,2,1,9),_ApcDiscoveryDeviceName_Type())
apcDiscoveryDeviceName.setMaxAccess(_F)
if mibBuilder.loadTexts:apcDiscoveryDeviceName.setStatus(_A)
_ApcDiscoveryDeviceNameMaxLength_Type=Integer32
_ApcDiscoveryDeviceNameMaxLength_Object=MibTableColumn
apcDiscoveryDeviceNameMaxLength=_ApcDiscoveryDeviceNameMaxLength_Object((1,3,6,1,4,1,318,1,4,2,2,1,10),_ApcDiscoveryDeviceNameMaxLength_Type())
apcDiscoveryDeviceNameMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceNameMaxLength.setStatus(_A)
_ApcDiscoveryDeviceInstance_Type=Integer32
_ApcDiscoveryDeviceInstance_Object=MibTableColumn
apcDiscoveryDeviceInstance=_ApcDiscoveryDeviceInstance_Object((1,3,6,1,4,1,318,1,4,2,2,1,11),_ApcDiscoveryDeviceInstance_Type())
apcDiscoveryDeviceInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceInstance.setStatus(_A)
_ApcDiscoveryDeviceParamsIndex_Type=DisplayString
_ApcDiscoveryDeviceParamsIndex_Object=MibTableColumn
apcDiscoveryDeviceParamsIndex=_ApcDiscoveryDeviceParamsIndex_Object((1,3,6,1,4,1,318,1,4,2,2,1,12),_ApcDiscoveryDeviceParamsIndex_Type())
apcDiscoveryDeviceParamsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceParamsIndex.setStatus(_A)
_ApcDiscoveryDdfXReference_Type=Integer32
_ApcDiscoveryDdfXReference_Object=MibTableColumn
apcDiscoveryDdfXReference=_ApcDiscoveryDdfXReference_Object((1,3,6,1,4,1,318,1,4,2,2,1,13),_ApcDiscoveryDdfXReference_Type())
apcDiscoveryDdfXReference.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDdfXReference.setStatus(_A)
_ApcDiscoveryDeviceStatusBlockId_Type=DisplayString
_ApcDiscoveryDeviceStatusBlockId_Object=MibTableColumn
apcDiscoveryDeviceStatusBlockId=_ApcDiscoveryDeviceStatusBlockId_Object((1,3,6,1,4,1,318,1,4,2,2,1,14),_ApcDiscoveryDeviceStatusBlockId_Type())
apcDiscoveryDeviceStatusBlockId.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceStatusBlockId.setStatus(_A)
_ApcDiscoveryDeviceFirmwareTableSize_Type=Integer32
_ApcDiscoveryDeviceFirmwareTableSize_Object=MibScalar
apcDiscoveryDeviceFirmwareTableSize=_ApcDiscoveryDeviceFirmwareTableSize_Object((1,3,6,1,4,1,318,1,4,2,3),_ApcDiscoveryDeviceFirmwareTableSize_Type())
apcDiscoveryDeviceFirmwareTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceFirmwareTableSize.setStatus(_A)
_ApcDiscoveryDeviceFirmwareTable_Object=MibTable
apcDiscoveryDeviceFirmwareTable=_ApcDiscoveryDeviceFirmwareTable_Object((1,3,6,1,4,1,318,1,4,2,4))
if mibBuilder.loadTexts:apcDiscoveryDeviceFirmwareTable.setStatus(_A)
_ApcDiscoveryDeviceFirmwareEntry_Object=MibTableRow
apcDiscoveryDeviceFirmwareEntry=_ApcDiscoveryDeviceFirmwareEntry_Object((1,3,6,1,4,1,318,1,4,2,4,1))
apcDiscoveryDeviceFirmwareEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:apcDiscoveryDeviceFirmwareEntry.setStatus(_A)
_ApcDiscoveryDeviceFirmwareTableIndex_Type=Integer32
_ApcDiscoveryDeviceFirmwareTableIndex_Object=MibTableColumn
apcDiscoveryDeviceFirmwareTableIndex=_ApcDiscoveryDeviceFirmwareTableIndex_Object((1,3,6,1,4,1,318,1,4,2,4,1,1),_ApcDiscoveryDeviceFirmwareTableIndex_Type())
apcDiscoveryDeviceFirmwareTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceFirmwareTableIndex.setStatus(_A)
_ApcDiscoveryDeviceSerialNumber_Type=DisplayString
_ApcDiscoveryDeviceSerialNumber_Object=MibTableColumn
apcDiscoveryDeviceSerialNumber=_ApcDiscoveryDeviceSerialNumber_Object((1,3,6,1,4,1,318,1,4,2,4,1,2),_ApcDiscoveryDeviceSerialNumber_Type())
apcDiscoveryDeviceSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceSerialNumber.setStatus(_A)
_ApcDiscoveryFirmwareName_Type=DisplayString
_ApcDiscoveryFirmwareName_Object=MibTableColumn
apcDiscoveryFirmwareName=_ApcDiscoveryFirmwareName_Object((1,3,6,1,4,1,318,1,4,2,4,1,3),_ApcDiscoveryFirmwareName_Type())
apcDiscoveryFirmwareName.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryFirmwareName.setStatus(_A)
_ApcDiscoveryFirmwareRevision_Type=DisplayString
_ApcDiscoveryFirmwareRevision_Object=MibTableColumn
apcDiscoveryFirmwareRevision=_ApcDiscoveryFirmwareRevision_Object((1,3,6,1,4,1,318,1,4,2,4,1,4),_ApcDiscoveryFirmwareRevision_Type())
apcDiscoveryFirmwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryFirmwareRevision.setStatus(_A)
_ApcDiscoveryDeviceProtocolTableSize_Type=Integer32
_ApcDiscoveryDeviceProtocolTableSize_Object=MibScalar
apcDiscoveryDeviceProtocolTableSize=_ApcDiscoveryDeviceProtocolTableSize_Object((1,3,6,1,4,1,318,1,4,2,5),_ApcDiscoveryDeviceProtocolTableSize_Type())
apcDiscoveryDeviceProtocolTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceProtocolTableSize.setStatus(_A)
_ApcDiscoveryDeviceProtocolTable_Object=MibTable
apcDiscoveryDeviceProtocolTable=_ApcDiscoveryDeviceProtocolTable_Object((1,3,6,1,4,1,318,1,4,2,6))
if mibBuilder.loadTexts:apcDiscoveryDeviceProtocolTable.setStatus(_A)
_ApcDiscoveryDeviceProtocolEntry_Object=MibTableRow
apcDiscoveryDeviceProtocolEntry=_ApcDiscoveryDeviceProtocolEntry_Object((1,3,6,1,4,1,318,1,4,2,6,1))
apcDiscoveryDeviceProtocolEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:apcDiscoveryDeviceProtocolEntry.setStatus(_A)
_ApcDiscoveryDeviceProtocolTableIndex_Type=Integer32
_ApcDiscoveryDeviceProtocolTableIndex_Object=MibTableColumn
apcDiscoveryDeviceProtocolTableIndex=_ApcDiscoveryDeviceProtocolTableIndex_Object((1,3,6,1,4,1,318,1,4,2,6,1,1),_ApcDiscoveryDeviceProtocolTableIndex_Type())
apcDiscoveryDeviceProtocolTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceProtocolTableIndex.setStatus(_A)
_ApcDiscoveryProtocolNumber_Type=Integer32
_ApcDiscoveryProtocolNumber_Object=MibTableColumn
apcDiscoveryProtocolNumber=_ApcDiscoveryProtocolNumber_Object((1,3,6,1,4,1,318,1,4,2,6,1,2),_ApcDiscoveryProtocolNumber_Type())
apcDiscoveryProtocolNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryProtocolNumber.setStatus(_A)
_ApcDiscoveryProtocolVersion_Type=DisplayString
_ApcDiscoveryProtocolVersion_Object=MibTableColumn
apcDiscoveryProtocolVersion=_ApcDiscoveryProtocolVersion_Object((1,3,6,1,4,1,318,1,4,2,6,1,3),_ApcDiscoveryProtocolVersion_Type())
apcDiscoveryProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryProtocolVersion.setStatus(_A)
_ApcDiscoveryProtocolPort_Type=DisplayString
_ApcDiscoveryProtocolPort_Object=MibTableColumn
apcDiscoveryProtocolPort=_ApcDiscoveryProtocolPort_Object((1,3,6,1,4,1,318,1,4,2,6,1,4),_ApcDiscoveryProtocolPort_Type())
apcDiscoveryProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryProtocolPort.setStatus(_A)
class _ApcDiscoveryProtocolEnabledDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_ApcDiscoveryProtocolEnabledDisabled_Type.__name__=_D
_ApcDiscoveryProtocolEnabledDisabled_Object=MibTableColumn
apcDiscoveryProtocolEnabledDisabled=_ApcDiscoveryProtocolEnabledDisabled_Object((1,3,6,1,4,1,318,1,4,2,6,1,5),_ApcDiscoveryProtocolEnabledDisabled_Type())
apcDiscoveryProtocolEnabledDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryProtocolEnabledDisabled.setStatus(_A)
_ApcDiscoveryDeviceDefTableSize_Type=Integer32
_ApcDiscoveryDeviceDefTableSize_Object=MibScalar
apcDiscoveryDeviceDefTableSize=_ApcDiscoveryDeviceDefTableSize_Object((1,3,6,1,4,1,318,1,4,2,7),_ApcDiscoveryDeviceDefTableSize_Type())
apcDiscoveryDeviceDefTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceDefTableSize.setStatus(_A)
_ApcDiscoveryDeviceDefTable_Object=MibTable
apcDiscoveryDeviceDefTable=_ApcDiscoveryDeviceDefTable_Object((1,3,6,1,4,1,318,1,4,2,8))
if mibBuilder.loadTexts:apcDiscoveryDeviceDefTable.setStatus(_A)
_ApcDiscoveryDeviceDefEntry_Object=MibTableRow
apcDiscoveryDeviceDefEntry=_ApcDiscoveryDeviceDefEntry_Object((1,3,6,1,4,1,318,1,4,2,8,1))
apcDiscoveryDeviceDefEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:apcDiscoveryDeviceDefEntry.setStatus(_A)
_ApcDiscoveryDeviceDefTableIndex_Type=Integer32
_ApcDiscoveryDeviceDefTableIndex_Object=MibTableColumn
apcDiscoveryDeviceDefTableIndex=_ApcDiscoveryDeviceDefTableIndex_Object((1,3,6,1,4,1,318,1,4,2,8,1,1),_ApcDiscoveryDeviceDefTableIndex_Type())
apcDiscoveryDeviceDefTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceDefTableIndex.setStatus(_A)
_ApcDiscoveryDeviceDefDeviceClass_Type=DisplayString
_ApcDiscoveryDeviceDefDeviceClass_Object=MibTableColumn
apcDiscoveryDeviceDefDeviceClass=_ApcDiscoveryDeviceDefDeviceClass_Object((1,3,6,1,4,1,318,1,4,2,8,1,2),_ApcDiscoveryDeviceDefDeviceClass_Type())
apcDiscoveryDeviceDefDeviceClass.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceDefDeviceClass.setStatus(_A)
_ApcDiscoveryDeviceDefDeviceType_Type=DisplayString
_ApcDiscoveryDeviceDefDeviceType_Object=MibTableColumn
apcDiscoveryDeviceDefDeviceType=_ApcDiscoveryDeviceDefDeviceType_Object((1,3,6,1,4,1,318,1,4,2,8,1,3),_ApcDiscoveryDeviceDefDeviceType_Type())
apcDiscoveryDeviceDefDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceDefDeviceType.setStatus(_A)
_ApcDiscoveryDeviceDefDeviceFamily_Type=DisplayString
_ApcDiscoveryDeviceDefDeviceFamily_Object=MibTableColumn
apcDiscoveryDeviceDefDeviceFamily=_ApcDiscoveryDeviceDefDeviceFamily_Object((1,3,6,1,4,1,318,1,4,2,8,1,4),_ApcDiscoveryDeviceDefDeviceFamily_Type())
apcDiscoveryDeviceDefDeviceFamily.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceDefDeviceFamily.setStatus(_A)
_ApcDiscoveryDeviceDefDeviceVersion_Type=DisplayString
_ApcDiscoveryDeviceDefDeviceVersion_Object=MibTableColumn
apcDiscoveryDeviceDefDeviceVersion=_ApcDiscoveryDeviceDefDeviceVersion_Object((1,3,6,1,4,1,318,1,4,2,8,1,5),_ApcDiscoveryDeviceDefDeviceVersion_Type())
apcDiscoveryDeviceDefDeviceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceDefDeviceVersion.setStatus(_A)
_ApcDiscoveryDeviceDefDdfXReference_Type=Integer32
_ApcDiscoveryDeviceDefDdfXReference_Object=MibTableColumn
apcDiscoveryDeviceDefDdfXReference=_ApcDiscoveryDeviceDefDdfXReference_Object((1,3,6,1,4,1,318,1,4,2,8,1,6),_ApcDiscoveryDeviceDefDdfXReference_Type())
apcDiscoveryDeviceDefDdfXReference.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceDefDdfXReference.setStatus(_A)
_ApcDiscoveryDeviceAlarmStateChangeCount_Type=Integer32
_ApcDiscoveryDeviceAlarmStateChangeCount_Object=MibScalar
apcDiscoveryDeviceAlarmStateChangeCount=_ApcDiscoveryDeviceAlarmStateChangeCount_Object((1,3,6,1,4,1,318,1,4,2,9),_ApcDiscoveryDeviceAlarmStateChangeCount_Type())
apcDiscoveryDeviceAlarmStateChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceAlarmStateChangeCount.setStatus(_A)
_ApcDiscoveryDeviceAlarmStateTableSize_Type=Integer32
_ApcDiscoveryDeviceAlarmStateTableSize_Object=MibScalar
apcDiscoveryDeviceAlarmStateTableSize=_ApcDiscoveryDeviceAlarmStateTableSize_Object((1,3,6,1,4,1,318,1,4,2,10),_ApcDiscoveryDeviceAlarmStateTableSize_Type())
apcDiscoveryDeviceAlarmStateTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceAlarmStateTableSize.setStatus(_A)
_ApcDiscoveryDeviceAlarmStateTable_Object=MibTable
apcDiscoveryDeviceAlarmStateTable=_ApcDiscoveryDeviceAlarmStateTable_Object((1,3,6,1,4,1,318,1,4,2,11))
if mibBuilder.loadTexts:apcDiscoveryDeviceAlarmStateTable.setStatus(_A)
_ApcDiscoveryDeviceAlarmStateEntry_Object=MibTableRow
apcDiscoveryDeviceAlarmStateEntry=_ApcDiscoveryDeviceAlarmStateEntry_Object((1,3,6,1,4,1,318,1,4,2,11,1))
apcDiscoveryDeviceAlarmStateEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:apcDiscoveryDeviceAlarmStateEntry.setStatus(_A)
_ApcDiscoveryDeviceAlarmStateTableIndex_Type=Integer32
_ApcDiscoveryDeviceAlarmStateTableIndex_Object=MibTableColumn
apcDiscoveryDeviceAlarmStateTableIndex=_ApcDiscoveryDeviceAlarmStateTableIndex_Object((1,3,6,1,4,1,318,1,4,2,11,1,1),_ApcDiscoveryDeviceAlarmStateTableIndex_Type())
apcDiscoveryDeviceAlarmStateTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceAlarmStateTableIndex.setStatus(_A)
_ApcDiscoveryDeviceAlarmStateSerialNumber_Type=DisplayString
_ApcDiscoveryDeviceAlarmStateSerialNumber_Object=MibTableColumn
apcDiscoveryDeviceAlarmStateSerialNumber=_ApcDiscoveryDeviceAlarmStateSerialNumber_Object((1,3,6,1,4,1,318,1,4,2,11,1,2),_ApcDiscoveryDeviceAlarmStateSerialNumber_Type())
apcDiscoveryDeviceAlarmStateSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceAlarmStateSerialNumber.setStatus(_A)
_ApcDiscoveryDeviceAlarmStateCode_Type=OctetString
_ApcDiscoveryDeviceAlarmStateCode_Object=MibTableColumn
apcDiscoveryDeviceAlarmStateCode=_ApcDiscoveryDeviceAlarmStateCode_Object((1,3,6,1,4,1,318,1,4,2,11,1,3),_ApcDiscoveryDeviceAlarmStateCode_Type())
apcDiscoveryDeviceAlarmStateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceAlarmStateCode.setStatus(_A)
_ApcDiscoveryDeviceAlarmStateParam_Type=OctetString
_ApcDiscoveryDeviceAlarmStateParam_Object=MibTableColumn
apcDiscoveryDeviceAlarmStateParam=_ApcDiscoveryDeviceAlarmStateParam_Object((1,3,6,1,4,1,318,1,4,2,11,1,4),_ApcDiscoveryDeviceAlarmStateParam_Type())
apcDiscoveryDeviceAlarmStateParam.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceAlarmStateParam.setStatus(_A)
_ApcDiscoveryDeviceInfoChangeCount_Type=Integer32
_ApcDiscoveryDeviceInfoChangeCount_Object=MibScalar
apcDiscoveryDeviceInfoChangeCount=_ApcDiscoveryDeviceInfoChangeCount_Object((1,3,6,1,4,1,318,1,4,2,12),_ApcDiscoveryDeviceInfoChangeCount_Type())
apcDiscoveryDeviceInfoChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:apcDiscoveryDeviceInfoChangeCount.setStatus(_A)
_ApcTrapReceiver_ObjectIdentity=ObjectIdentity
apcTrapReceiver=_ApcTrapReceiver_ObjectIdentity((1,3,6,1,4,1,318,1,4,4))
_ApcTrapRecvTableSize_Type=Integer32
_ApcTrapRecvTableSize_Object=MibScalar
apcTrapRecvTableSize=_ApcTrapRecvTableSize_Object((1,3,6,1,4,1,318,1,4,4,1),_ApcTrapRecvTableSize_Type())
apcTrapRecvTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apcTrapRecvTableSize.setStatus(_A)
_ApcTrapRecvTable_Object=MibTable
apcTrapRecvTable=_ApcTrapRecvTable_Object((1,3,6,1,4,1,318,1,4,4,2))
if mibBuilder.loadTexts:apcTrapRecvTable.setStatus(_A)
_ApcTrapRecvEntry_Object=MibTableRow
apcTrapRecvEntry=_ApcTrapRecvEntry_Object((1,3,6,1,4,1,318,1,4,4,2,1))
apcTrapRecvEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:apcTrapRecvEntry.setStatus(_A)
_ApcTrapRecvIndex_Type=Integer32
_ApcTrapRecvIndex_Object=MibTableColumn
apcTrapRecvIndex=_ApcTrapRecvIndex_Object((1,3,6,1,4,1,318,1,4,4,2,1,1),_ApcTrapRecvIndex_Type())
apcTrapRecvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apcTrapRecvIndex.setStatus(_A)
class _ApcTrapRecvHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ApcTrapRecvHost_Type.__name__=_E
_ApcTrapRecvHost_Object=MibTableColumn
apcTrapRecvHost=_ApcTrapRecvHost_Object((1,3,6,1,4,1,318,1,4,4,2,1,2),_ApcTrapRecvHost_Type())
apcTrapRecvHost.setMaxAccess(_B)
if mibBuilder.loadTexts:apcTrapRecvHost.setStatus(_A)
class _ApcTrapRecvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('remove',2),('pcs',3),('isxm',4)))
_ApcTrapRecvType_Type.__name__=_D
_ApcTrapRecvType_Object=MibTableColumn
apcTrapRecvType=_ApcTrapRecvType_Object((1,3,6,1,4,1,318,1,4,4,2,1,3),_ApcTrapRecvType_Type())
apcTrapRecvType.setMaxAccess(_B)
if mibBuilder.loadTexts:apcTrapRecvType.setStatus(_A)
_ApcTrapRecvUniqueId_Type=Integer32
_ApcTrapRecvUniqueId_Object=MibTableColumn
apcTrapRecvUniqueId=_ApcTrapRecvUniqueId_Object((1,3,6,1,4,1,318,1,4,4,2,1,4),_ApcTrapRecvUniqueId_Type())
apcTrapRecvUniqueId.setMaxAccess(_B)
if mibBuilder.loadTexts:apcTrapRecvUniqueId.setStatus(_A)
class _ApcTrapRecvTableModify_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ApcTrapRecvTableModify_Type.__name__=_E
_ApcTrapRecvTableModify_Object=MibScalar
apcTrapRecvTableModify=_ApcTrapRecvTableModify_Object((1,3,6,1,4,1,318,1,4,4,3),_ApcTrapRecvTableModify_Type())
apcTrapRecvTableModify.setMaxAccess(_F)
if mibBuilder.loadTexts:apcTrapRecvTableModify.setStatus(_A)
_ApcTrapReceiverUniqueID_Type=Integer32
_ApcTrapReceiverUniqueID_Object=MibScalar
apcTrapReceiverUniqueID=_ApcTrapReceiverUniqueID_Object((1,3,6,1,4,1,318,1,4,4,4),_ApcTrapReceiverUniqueID_Type())
apcTrapReceiverUniqueID.setMaxAccess(_B)
if mibBuilder.loadTexts:apcTrapReceiverUniqueID.setStatus(_A)
_Apcmgmt_ObjectIdentity=ObjectIdentity
apcmgmt=_Apcmgmt_ObjectIdentity((1,3,6,1,4,1,318,2))
apcDiscoveryAlarmStateTableUpdate=NotificationType((1,3,6,1,4,1,318,0,1000))
apcDiscoveryAlarmStateTableUpdate.setObjects((_C,_O))
if mibBuilder.loadTexts:apcDiscoveryAlarmStateTableUpdate.setStatus('')
mibBuilder.exportSymbols(_C,**{'apc':apc,'apcDiscoveryAlarmStateTableUpdate':apcDiscoveryAlarmStateTableUpdate,'products':products,'hardware':hardware,'software':software,'system':system,'experimental':experimental,'apcDiscovery':apcDiscovery,'apcDiscoveryInfoTableSize':apcDiscoveryInfoTableSize,'apcDiscoveryInfoTable':apcDiscoveryInfoTable,'apcDiscoveryInfoEntry':apcDiscoveryInfoEntry,_H:apcDiscoveryInfoTableIndex,'apcDiscoveryModel':apcDiscoveryModel,'apcDiscoverySerialNumber':apcDiscoverySerialNumber,'apcDiscoveryStatus':apcDiscoveryStatus,'apcDiscoveryLabelString':apcDiscoveryLabelString,'apcDiscoveryDeviceHierarchy':apcDiscoveryDeviceHierarchy,'apcDiscoveryDeviceLocation':apcDiscoveryDeviceLocation,'apcDiscoveryDeviceLocationMaxLength':apcDiscoveryDeviceLocationMaxLength,'apcDiscoveryDeviceName':apcDiscoveryDeviceName,'apcDiscoveryDeviceNameMaxLength':apcDiscoveryDeviceNameMaxLength,'apcDiscoveryDeviceInstance':apcDiscoveryDeviceInstance,'apcDiscoveryDeviceParamsIndex':apcDiscoveryDeviceParamsIndex,'apcDiscoveryDdfXReference':apcDiscoveryDdfXReference,'apcDiscoveryDeviceStatusBlockId':apcDiscoveryDeviceStatusBlockId,'apcDiscoveryDeviceFirmwareTableSize':apcDiscoveryDeviceFirmwareTableSize,'apcDiscoveryDeviceFirmwareTable':apcDiscoveryDeviceFirmwareTable,'apcDiscoveryDeviceFirmwareEntry':apcDiscoveryDeviceFirmwareEntry,_J:apcDiscoveryDeviceFirmwareTableIndex,'apcDiscoveryDeviceSerialNumber':apcDiscoveryDeviceSerialNumber,'apcDiscoveryFirmwareName':apcDiscoveryFirmwareName,'apcDiscoveryFirmwareRevision':apcDiscoveryFirmwareRevision,'apcDiscoveryDeviceProtocolTableSize':apcDiscoveryDeviceProtocolTableSize,'apcDiscoveryDeviceProtocolTable':apcDiscoveryDeviceProtocolTable,'apcDiscoveryDeviceProtocolEntry':apcDiscoveryDeviceProtocolEntry,_K:apcDiscoveryDeviceProtocolTableIndex,'apcDiscoveryProtocolNumber':apcDiscoveryProtocolNumber,'apcDiscoveryProtocolVersion':apcDiscoveryProtocolVersion,'apcDiscoveryProtocolPort':apcDiscoveryProtocolPort,'apcDiscoveryProtocolEnabledDisabled':apcDiscoveryProtocolEnabledDisabled,'apcDiscoveryDeviceDefTableSize':apcDiscoveryDeviceDefTableSize,'apcDiscoveryDeviceDefTable':apcDiscoveryDeviceDefTable,'apcDiscoveryDeviceDefEntry':apcDiscoveryDeviceDefEntry,_L:apcDiscoveryDeviceDefTableIndex,'apcDiscoveryDeviceDefDeviceClass':apcDiscoveryDeviceDefDeviceClass,'apcDiscoveryDeviceDefDeviceType':apcDiscoveryDeviceDefDeviceType,'apcDiscoveryDeviceDefDeviceFamily':apcDiscoveryDeviceDefDeviceFamily,'apcDiscoveryDeviceDefDeviceVersion':apcDiscoveryDeviceDefDeviceVersion,'apcDiscoveryDeviceDefDdfXReference':apcDiscoveryDeviceDefDdfXReference,_O:apcDiscoveryDeviceAlarmStateChangeCount,'apcDiscoveryDeviceAlarmStateTableSize':apcDiscoveryDeviceAlarmStateTableSize,'apcDiscoveryDeviceAlarmStateTable':apcDiscoveryDeviceAlarmStateTable,'apcDiscoveryDeviceAlarmStateEntry':apcDiscoveryDeviceAlarmStateEntry,_M:apcDiscoveryDeviceAlarmStateTableIndex,'apcDiscoveryDeviceAlarmStateSerialNumber':apcDiscoveryDeviceAlarmStateSerialNumber,'apcDiscoveryDeviceAlarmStateCode':apcDiscoveryDeviceAlarmStateCode,'apcDiscoveryDeviceAlarmStateParam':apcDiscoveryDeviceAlarmStateParam,'apcDiscoveryDeviceInfoChangeCount':apcDiscoveryDeviceInfoChangeCount,'apcTrapReceiver':apcTrapReceiver,'apcTrapRecvTableSize':apcTrapRecvTableSize,'apcTrapRecvTable':apcTrapRecvTable,'apcTrapRecvEntry':apcTrapRecvEntry,_N:apcTrapRecvIndex,'apcTrapRecvHost':apcTrapRecvHost,'apcTrapRecvType':apcTrapRecvType,'apcTrapRecvUniqueId':apcTrapRecvUniqueId,'apcTrapRecvTableModify':apcTrapRecvTableModify,'apcTrapReceiverUniqueID':apcTrapReceiverUniqueID,'apcmgmt':apcmgmt})