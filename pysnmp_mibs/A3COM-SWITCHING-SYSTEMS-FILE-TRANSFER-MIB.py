_N='A3ComSysAddressType'
_M='A3ComSysResourceBitMask'
_L='A3ComSysResourceType'
_K='A3ComSysStorageType'
_J='a3ComSysFtIndex'
_I='A3COM-SWITCHING-SYSTEMS-FILE-TRANSFER-MIB'
_H='NotificationType'
_G='ObjectIdentifier'
_F='OctetString'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,_G)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
class A3ComSysStorageType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
class A3ComSysAddressType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
class A3ComSysResourceType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
class A3ComSysResourceBitMask(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsMib=_A3ComSwitchingSystemsMib_ObjectIdentity((1,3,6,1,4,1,43,29,4))
_A3ComSysFtGroup_ObjectIdentity=ObjectIdentity
a3ComSysFtGroup=_A3ComSysFtGroup_ObjectIdentity((1,3,6,1,4,1,43,29,4,14))
_A3ComSysFtTable_Object=MibTable
a3ComSysFtTable=_A3ComSysFtTable_Object((1,3,6,1,4,1,43,29,4,14,1))
if mibBuilder.loadTexts:a3ComSysFtTable.setStatus(_A)
_A3ComSysFtTableEntry_Object=MibTableRow
a3ComSysFtTableEntry=_A3ComSysFtTableEntry_Object((1,3,6,1,4,1,43,29,4,14,1,1))
a3ComSysFtTableEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:a3ComSysFtTableEntry.setStatus(_A)
class _A3ComSysFtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysFtIndex_Type.__name__=_C
_A3ComSysFtIndex_Object=MibTableColumn
a3ComSysFtIndex=_A3ComSysFtIndex_Object((1,3,6,1,4,1,43,29,4,14,1,1,1),_A3ComSysFtIndex_Type())
a3ComSysFtIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysFtIndex.setStatus(_A)
class _A3ComSysFtDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localToRemote',1),('remoteToLocal',2)))
_A3ComSysFtDirection_Type.__name__=_C
_A3ComSysFtDirection_Object=MibTableColumn
a3ComSysFtDirection=_A3ComSysFtDirection_Object((1,3,6,1,4,1,43,29,4,14,1,1,2),_A3ComSysFtDirection_Type())
a3ComSysFtDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtDirection.setStatus(_A)
class _A3ComSysFtLocalStorageType_Type(A3ComSysStorageType):defaultValue=3
_A3ComSysFtLocalStorageType_Type.__name__=_K
_A3ComSysFtLocalStorageType_Object=MibTableColumn
a3ComSysFtLocalStorageType=_A3ComSysFtLocalStorageType_Object((1,3,6,1,4,1,43,29,4,14,1,1,3),_A3ComSysFtLocalStorageType_Type())
a3ComSysFtLocalStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtLocalStorageType.setStatus(_A)
class _A3ComSysFtLocalResourceType_Type(A3ComSysResourceType):defaultValue=2
_A3ComSysFtLocalResourceType_Type.__name__=_L
_A3ComSysFtLocalResourceType_Object=MibTableColumn
a3ComSysFtLocalResourceType=_A3ComSysFtLocalResourceType_Object((1,3,6,1,4,1,43,29,4,14,1,1,4),_A3ComSysFtLocalResourceType_Type())
a3ComSysFtLocalResourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtLocalResourceType.setStatus(_A)
class _A3ComSysFtLocalResourceMask_Type(A3ComSysResourceBitMask):defaultHexValue='00000080'
_A3ComSysFtLocalResourceMask_Type.__name__=_M
_A3ComSysFtLocalResourceMask_Object=MibTableColumn
a3ComSysFtLocalResourceMask=_A3ComSysFtLocalResourceMask_Object((1,3,6,1,4,1,43,29,4,14,1,1,5),_A3ComSysFtLocalResourceMask_Type())
a3ComSysFtLocalResourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtLocalResourceMask.setStatus(_A)
class _A3ComSysFtLocalResourceAttribute_Type(ObjectIdentifier):defaultValue=1,3,6,1,4,1,43,29,4,14,2,1,1
_A3ComSysFtLocalResourceAttribute_Type.__name__=_G
_A3ComSysFtLocalResourceAttribute_Object=MibTableColumn
a3ComSysFtLocalResourceAttribute=_A3ComSysFtLocalResourceAttribute_Object((1,3,6,1,4,1,43,29,4,14,1,1,6),_A3ComSysFtLocalResourceAttribute_Type())
a3ComSysFtLocalResourceAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtLocalResourceAttribute.setStatus(_A)
class _A3ComSysFtRemoteAddressType_Type(A3ComSysAddressType):defaultValue=2
_A3ComSysFtRemoteAddressType_Type.__name__=_N
_A3ComSysFtRemoteAddressType_Object=MibTableColumn
a3ComSysFtRemoteAddressType=_A3ComSysFtRemoteAddressType_Object((1,3,6,1,4,1,43,29,4,14,1,1,7),_A3ComSysFtRemoteAddressType_Type())
a3ComSysFtRemoteAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtRemoteAddressType.setStatus(_A)
class _A3ComSysFtRemoteAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_A3ComSysFtRemoteAddress_Type.__name__=_F
_A3ComSysFtRemoteAddress_Object=MibTableColumn
a3ComSysFtRemoteAddress=_A3ComSysFtRemoteAddress_Object((1,3,6,1,4,1,43,29,4,14,1,1,8),_A3ComSysFtRemoteAddress_Type())
a3ComSysFtRemoteAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtRemoteAddress.setStatus(_A)
class _A3ComSysFtRemoteFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_A3ComSysFtRemoteFileName_Type.__name__=_E
_A3ComSysFtRemoteFileName_Object=MibTableColumn
a3ComSysFtRemoteFileName=_A3ComSysFtRemoteFileName_Object((1,3,6,1,4,1,43,29,4,14,1,1,9),_A3ComSysFtRemoteFileName_Type())
a3ComSysFtRemoteFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtRemoteFileName.setStatus(_A)
class _A3ComSysFtRemoteUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_A3ComSysFtRemoteUserName_Type.__name__=_E
_A3ComSysFtRemoteUserName_Object=MibTableColumn
a3ComSysFtRemoteUserName=_A3ComSysFtRemoteUserName_Object((1,3,6,1,4,1,43,29,4,14,1,1,10),_A3ComSysFtRemoteUserName_Type())
a3ComSysFtRemoteUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtRemoteUserName.setStatus(_A)
class _A3ComSysFtRemoteUserPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_A3ComSysFtRemoteUserPassword_Type.__name__=_F
_A3ComSysFtRemoteUserPassword_Object=MibTableColumn
a3ComSysFtRemoteUserPassword=_A3ComSysFtRemoteUserPassword_Object((1,3,6,1,4,1,43,29,4,14,1,1,11),_A3ComSysFtRemoteUserPassword_Type())
a3ComSysFtRemoteUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtRemoteUserPassword.setStatus(_A)
class _A3ComSysFtForceTransfer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_A3ComSysFtForceTransfer_Type.__name__=_C
_A3ComSysFtForceTransfer_Object=MibTableColumn
a3ComSysFtForceTransfer=_A3ComSysFtForceTransfer_Object((1,3,6,1,4,1,43,29,4,14,1,1,12),_A3ComSysFtForceTransfer_Type())
a3ComSysFtForceTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtForceTransfer.setStatus(_A)
_A3ComSysFtBytesTransferred_Type=Counter32
_A3ComSysFtBytesTransferred_Object=MibTableColumn
a3ComSysFtBytesTransferred=_A3ComSysFtBytesTransferred_Object((1,3,6,1,4,1,43,29,4,14,1,1,13),_A3ComSysFtBytesTransferred_Type())
a3ComSysFtBytesTransferred.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysFtBytesTransferred.setStatus(_A)
class _A3ComSysFtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('statusSuccessfulCompletion',1),('statusInProgress',2),('statusLocalInvalid',3),('statusRemoteInvalid',4),('statusRemoteUnreachable',5),('statusUserAuthFailed',6),('statusFileNotFound',7),('statusFileTooBig',8),('statusFileIncompatible',9),('statusError',10)))
_A3ComSysFtStatus_Type.__name__=_C
_A3ComSysFtStatus_Object=MibTableColumn
a3ComSysFtStatus=_A3ComSysFtStatus_Object((1,3,6,1,4,1,43,29,4,14,1,1,14),_A3ComSysFtStatus_Type())
a3ComSysFtStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysFtStatus.setStatus(_A)
_A3ComSysFtDetailedStatus_Type=ObjectIdentifier
_A3ComSysFtDetailedStatus_Object=MibTableColumn
a3ComSysFtDetailedStatus=_A3ComSysFtDetailedStatus_Object((1,3,6,1,4,1,43,29,4,14,1,1,15),_A3ComSysFtDetailedStatus_Type())
a3ComSysFtDetailedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysFtDetailedStatus.setStatus(_A)
_A3ComSysFtDetailedStatusString_Type=DisplayString
_A3ComSysFtDetailedStatusString_Object=MibTableColumn
a3ComSysFtDetailedStatusString=_A3ComSysFtDetailedStatusString_Object((1,3,6,1,4,1,43,29,4,14,1,1,16),_A3ComSysFtDetailedStatusString_Type())
a3ComSysFtDetailedStatusString.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysFtDetailedStatusString.setStatus(_A)
class _A3ComSysFtOwnerString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_A3ComSysFtOwnerString_Type.__name__=_E
_A3ComSysFtOwnerString_Object=MibTableColumn
a3ComSysFtOwnerString=_A3ComSysFtOwnerString_Object((1,3,6,1,4,1,43,29,4,14,1,1,17),_A3ComSysFtOwnerString_Type())
a3ComSysFtOwnerString.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtOwnerString.setStatus(_A)
_A3ComSysFtRowStatus_Type=RowStatus
_A3ComSysFtRowStatus_Object=MibTableColumn
a3ComSysFtRowStatus=_A3ComSysFtRowStatus_Object((1,3,6,1,4,1,43,29,4,14,1,1,18),_A3ComSysFtRowStatus_Type())
a3ComSysFtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtRowStatus.setStatus(_A)
class _A3ComSysFtProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ftProtocolTftp',1),('ftProtocolFtp',2)))
_A3ComSysFtProtocol_Type.__name__=_C
_A3ComSysFtProtocol_Object=MibTableColumn
a3ComSysFtProtocol=_A3ComSysFtProtocol_Object((1,3,6,1,4,1,43,29,4,14,1,1,19),_A3ComSysFtProtocol_Type())
a3ComSysFtProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysFtProtocol.setStatus(_A)
_A3ComSysFtResourceAttributes_ObjectIdentity=ObjectIdentity
a3ComSysFtResourceAttributes=_A3ComSysFtResourceAttributes_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,2))
_A3ComSysFtSystemAttributes_ObjectIdentity=ObjectIdentity
a3ComSysFtSystemAttributes=_A3ComSysFtSystemAttributes_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,2,1))
_A3ComSysFtSystemOperationalCode_ObjectIdentity=ObjectIdentity
a3ComSysFtSystemOperationalCode=_A3ComSysFtSystemOperationalCode_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,2,1,1))
_A3ComSysFtSystemConfiguration_ObjectIdentity=ObjectIdentity
a3ComSysFtSystemConfiguration=_A3ComSysFtSystemConfiguration_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,2,1,2))
_A3ComSysFtSystemBridgeFilterCode_ObjectIdentity=ObjectIdentity
a3ComSysFtSystemBridgeFilterCode=_A3ComSysFtSystemBridgeFilterCode_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,2,1,3))
_A3ComSysFtDetailedResourceStatus_ObjectIdentity=ObjectIdentity
a3ComSysFtDetailedResourceStatus=_A3ComSysFtDetailedResourceStatus_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3))
_A3ComSysFtSystemDetailedStatus_ObjectIdentity=ObjectIdentity
a3ComSysFtSystemDetailedStatus=_A3ComSysFtSystemDetailedStatus_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1))
_A3ComSysFtSysStatusNotApplicable_ObjectIdentity=ObjectIdentity
a3ComSysFtSysStatusNotApplicable=_A3ComSysFtSysStatusNotApplicable_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,1))
_A3ComSysFtSysStatusNoImageLabel_ObjectIdentity=ObjectIdentity
a3ComSysFtSysStatusNoImageLabel=_A3ComSysFtSysStatusNoImageLabel_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,2))
_A3ComSysFtSysStatusConfigIdMismatch_ObjectIdentity=ObjectIdentity
a3ComSysFtSysStatusConfigIdMismatch=_A3ComSysFtSysStatusConfigIdMismatch_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,3))
_A3ComSysFtSysStatusChecksumError_ObjectIdentity=ObjectIdentity
a3ComSysFtSysStatusChecksumError=_A3ComSysFtSysStatusChecksumError_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,4))
_A3ComSysFtSysStatusNvRamError_ObjectIdentity=ObjectIdentity
a3ComSysFtSysStatusNvRamError=_A3ComSysFtSysStatusNvRamError_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,5))
_A3ComSysFtSysStatusFlashError_ObjectIdentity=ObjectIdentity
a3ComSysFtSysStatusFlashError=_A3ComSysFtSysStatusFlashError_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,6))
_A3ComSysFtSysStatusNoRoom_ObjectIdentity=ObjectIdentity
a3ComSysFtSysStatusNoRoom=_A3ComSysFtSysStatusNoRoom_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,7))
_A3ComSysFtSysBridgeFilterNotApplicable_ObjectIdentity=ObjectIdentity
a3ComSysFtSysBridgeFilterNotApplicable=_A3ComSysFtSysBridgeFilterNotApplicable_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,8))
_A3ComSysFtSysBridgeFilterSyntaxError_ObjectIdentity=ObjectIdentity
a3ComSysFtSysBridgeFilterSyntaxError=_A3ComSysFtSysBridgeFilterSyntaxError_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,9))
_A3ComSysFtSysBridgeFilterdownloadError_ObjectIdentity=ObjectIdentity
a3ComSysFtSysBridgeFilterdownloadError=_A3ComSysFtSysBridgeFilterdownloadError_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,10))
_A3ComSysFtSysBridgeFilterNoRoom_ObjectIdentity=ObjectIdentity
a3ComSysFtSysBridgeFilterNoRoom=_A3ComSysFtSysBridgeFilterNoRoom_ObjectIdentity((1,3,6,1,4,1,43,29,4,14,3,1,11))
mibBuilder.exportSymbols(_I,**{'RowStatus':RowStatus,_K:A3ComSysStorageType,_N:A3ComSysAddressType,_L:A3ComSysResourceType,_M:A3ComSysResourceBitMask,'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsMib':a3ComSwitchingSystemsMib,'a3ComSysFtGroup':a3ComSysFtGroup,'a3ComSysFtTable':a3ComSysFtTable,'a3ComSysFtTableEntry':a3ComSysFtTableEntry,_J:a3ComSysFtIndex,'a3ComSysFtDirection':a3ComSysFtDirection,'a3ComSysFtLocalStorageType':a3ComSysFtLocalStorageType,'a3ComSysFtLocalResourceType':a3ComSysFtLocalResourceType,'a3ComSysFtLocalResourceMask':a3ComSysFtLocalResourceMask,'a3ComSysFtLocalResourceAttribute':a3ComSysFtLocalResourceAttribute,'a3ComSysFtRemoteAddressType':a3ComSysFtRemoteAddressType,'a3ComSysFtRemoteAddress':a3ComSysFtRemoteAddress,'a3ComSysFtRemoteFileName':a3ComSysFtRemoteFileName,'a3ComSysFtRemoteUserName':a3ComSysFtRemoteUserName,'a3ComSysFtRemoteUserPassword':a3ComSysFtRemoteUserPassword,'a3ComSysFtForceTransfer':a3ComSysFtForceTransfer,'a3ComSysFtBytesTransferred':a3ComSysFtBytesTransferred,'a3ComSysFtStatus':a3ComSysFtStatus,'a3ComSysFtDetailedStatus':a3ComSysFtDetailedStatus,'a3ComSysFtDetailedStatusString':a3ComSysFtDetailedStatusString,'a3ComSysFtOwnerString':a3ComSysFtOwnerString,'a3ComSysFtRowStatus':a3ComSysFtRowStatus,'a3ComSysFtProtocol':a3ComSysFtProtocol,'a3ComSysFtResourceAttributes':a3ComSysFtResourceAttributes,'a3ComSysFtSystemAttributes':a3ComSysFtSystemAttributes,'a3ComSysFtSystemOperationalCode':a3ComSysFtSystemOperationalCode,'a3ComSysFtSystemConfiguration':a3ComSysFtSystemConfiguration,'a3ComSysFtSystemBridgeFilterCode':a3ComSysFtSystemBridgeFilterCode,'a3ComSysFtDetailedResourceStatus':a3ComSysFtDetailedResourceStatus,'a3ComSysFtSystemDetailedStatus':a3ComSysFtSystemDetailedStatus,'a3ComSysFtSysStatusNotApplicable':a3ComSysFtSysStatusNotApplicable,'a3ComSysFtSysStatusNoImageLabel':a3ComSysFtSysStatusNoImageLabel,'a3ComSysFtSysStatusConfigIdMismatch':a3ComSysFtSysStatusConfigIdMismatch,'a3ComSysFtSysStatusChecksumError':a3ComSysFtSysStatusChecksumError,'a3ComSysFtSysStatusNvRamError':a3ComSysFtSysStatusNvRamError,'a3ComSysFtSysStatusFlashError':a3ComSysFtSysStatusFlashError,'a3ComSysFtSysStatusNoRoom':a3ComSysFtSysStatusNoRoom,'a3ComSysFtSysBridgeFilterNotApplicable':a3ComSysFtSysBridgeFilterNotApplicable,'a3ComSysFtSysBridgeFilterSyntaxError':a3ComSysFtSysBridgeFilterSyntaxError,'a3ComSysFtSysBridgeFilterdownloadError':a3ComSysFtSysBridgeFilterdownloadError,'a3ComSysFtSysBridgeFilterNoRoom':a3ComSysFtSysBridgeFilterNoRoom})