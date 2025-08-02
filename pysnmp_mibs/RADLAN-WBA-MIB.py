_N='rlWBAImageInfoNumber'
_M='rlWBADataIndex'
_L='rlWBADataNumber'
_K='rlWBAImageIndex'
_J='rlWBAImageNumber'
_I='RlWBARetryFlagOp'
_H='read-only'
_G='rlWBAIp'
_F='DisplayString'
_E='not-accessible'
_D='Integer32'
_C='RADLAN-WBA-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6','InetAddressType')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention')
rlWBA=ModuleIdentity((1,3,6,1,4,1,89,230))
if mibBuilder.loadTexts:rlWBA.setRevisions(('2010-07-05 00:00',))
class RlWBAStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',0),('inProcess',1),('failAuthen',2),('pending',3),('authenticating',4),('authenticated',5),('waitAck',6)))
class RlWBARetryFlagOp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_RlWBAAuxiliaryTable_Object=MibTable
rlWBAAuxiliaryTable=_RlWBAAuxiliaryTable_Object((1,3,6,1,4,1,89,230,1))
if mibBuilder.loadTexts:rlWBAAuxiliaryTable.setStatus(_A)
_RlWBAAuxiliaryEntry_Object=MibTableRow
rlWBAAuxiliaryEntry=_RlWBAAuxiliaryEntry_Object((1,3,6,1,4,1,89,230,1,1))
rlWBAAuxiliaryEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:rlWBAAuxiliaryEntry.setStatus(_A)
_RlWBAIp_Type=InetAddress
_RlWBAIp_Object=MibTableColumn
rlWBAIp=_RlWBAIp_Object((1,3,6,1,4,1,89,230,1,1,1),_RlWBAIp_Type())
rlWBAIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBAIp.setStatus(_A)
_RlWBAStatus_Type=RlWBAStatusType
_RlWBAStatus_Object=MibTableColumn
rlWBAStatus=_RlWBAStatus_Object((1,3,6,1,4,1,89,230,1,1,2),_RlWBAStatus_Type())
rlWBAStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:rlWBAStatus.setStatus(_A)
_RlAuxFailReason_Type=Integer32
_RlAuxFailReason_Object=MibTableColumn
rlAuxFailReason=_RlAuxFailReason_Object((1,3,6,1,4,1,89,230,1,1,3),_RlAuxFailReason_Type())
rlAuxFailReason.setMaxAccess(_H)
if mibBuilder.loadTexts:rlAuxFailReason.setStatus(_A)
class _RlIsRetryFlag_Type(RlWBARetryFlagOp):defaultValue=0
_RlIsRetryFlag_Type.__name__=_I
_RlIsRetryFlag_Object=MibTableColumn
rlIsRetryFlag=_RlIsRetryFlag_Object((1,3,6,1,4,1,89,230,1,1,4),_RlIsRetryFlag_Type())
rlIsRetryFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIsRetryFlag.setStatus(_A)
class _RlWBAUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlWBAUsername_Type.__name__=_F
_RlWBAUsername_Object=MibTableColumn
rlWBAUsername=_RlWBAUsername_Object((1,3,6,1,4,1,89,230,1,1,5),_RlWBAUsername_Type())
rlWBAUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBAUsername.setStatus(_A)
class _RlWBAPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlWBAPassword_Type.__name__=_F
_RlWBAPassword_Object=MibTableColumn
rlWBAPassword=_RlWBAPassword_Object((1,3,6,1,4,1,89,230,1,1,6),_RlWBAPassword_Type())
rlWBAPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBAPassword.setStatus(_A)
_RlWBAImageTable_Object=MibTable
rlWBAImageTable=_RlWBAImageTable_Object((1,3,6,1,4,1,89,230,2))
if mibBuilder.loadTexts:rlWBAImageTable.setStatus(_A)
_RlWBAImageEntry_Object=MibTableRow
rlWBAImageEntry=_RlWBAImageEntry_Object((1,3,6,1,4,1,89,230,2,1))
rlWBAImageEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:rlWBAImageEntry.setStatus(_A)
class _RlWBAImageNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RlWBAImageNumber_Type.__name__=_D
_RlWBAImageNumber_Object=MibTableColumn
rlWBAImageNumber=_RlWBAImageNumber_Object((1,3,6,1,4,1,89,230,2,1,1),_RlWBAImageNumber_Type())
rlWBAImageNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:rlWBAImageNumber.setStatus(_A)
class _RlWBAImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_RlWBAImageIndex_Type.__name__=_D
_RlWBAImageIndex_Object=MibTableColumn
rlWBAImageIndex=_RlWBAImageIndex_Object((1,3,6,1,4,1,89,230,2,1,2),_RlWBAImageIndex_Type())
rlWBAImageIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlWBAImageIndex.setStatus(_A)
_RlWBAImageText_Type=OctetString
_RlWBAImageText_Object=MibTableColumn
rlWBAImageText=_RlWBAImageText_Object((1,3,6,1,4,1,89,230,2,1,3),_RlWBAImageText_Type())
rlWBAImageText.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBAImageText.setStatus(_A)
_RlWBADataTable_Object=MibTable
rlWBADataTable=_RlWBADataTable_Object((1,3,6,1,4,1,89,230,3))
if mibBuilder.loadTexts:rlWBADataTable.setStatus(_A)
_RlWBADataEntry_Object=MibTableRow
rlWBADataEntry=_RlWBADataEntry_Object((1,3,6,1,4,1,89,230,3,1))
rlWBADataEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:rlWBADataEntry.setStatus(_A)
class _RlWBADataNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RlWBADataNumber_Type.__name__=_D
_RlWBADataNumber_Object=MibTableColumn
rlWBADataNumber=_RlWBADataNumber_Object((1,3,6,1,4,1,89,230,3,1,1),_RlWBADataNumber_Type())
rlWBADataNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:rlWBADataNumber.setStatus(_A)
class _RlWBADataIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_RlWBADataIndex_Type.__name__=_D
_RlWBADataIndex_Object=MibTableColumn
rlWBADataIndex=_RlWBADataIndex_Object((1,3,6,1,4,1,89,230,3,1,2),_RlWBADataIndex_Type())
rlWBADataIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlWBADataIndex.setStatus(_A)
_RlWBADataText_Type=SnmpAdminString
_RlWBADataText_Object=MibTableColumn
rlWBADataText=_RlWBADataText_Object((1,3,6,1,4,1,89,230,3,1,3),_RlWBADataText_Type())
rlWBADataText.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBADataText.setStatus(_A)
_RlWBAImageInfoTable_Object=MibTable
rlWBAImageInfoTable=_RlWBAImageInfoTable_Object((1,3,6,1,4,1,89,230,4))
if mibBuilder.loadTexts:rlWBAImageInfoTable.setStatus(_A)
_RlWBAImageInfoEntry_Object=MibTableRow
rlWBAImageInfoEntry=_RlWBAImageInfoEntry_Object((1,3,6,1,4,1,89,230,4,1))
rlWBAImageInfoEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:rlWBAImageInfoEntry.setStatus(_A)
class _RlWBAImageInfoNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RlWBAImageInfoNumber_Type.__name__=_D
_RlWBAImageInfoNumber_Object=MibTableColumn
rlWBAImageInfoNumber=_RlWBAImageInfoNumber_Object((1,3,6,1,4,1,89,230,4,1,1),_RlWBAImageInfoNumber_Type())
rlWBAImageInfoNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:rlWBAImageInfoNumber.setStatus(_A)
_RlWBAImageInfoName_Type=SnmpAdminString
_RlWBAImageInfoName_Object=MibTableColumn
rlWBAImageInfoName=_RlWBAImageInfoName_Object((1,3,6,1,4,1,89,230,4,1,2),_RlWBAImageInfoName_Type())
rlWBAImageInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBAImageInfoName.setStatus(_A)
_RlWBAImageInfoSize_Type=Integer32
_RlWBAImageInfoSize_Object=MibTableColumn
rlWBAImageInfoSize=_RlWBAImageInfoSize_Object((1,3,6,1,4,1,89,230,4,1,3),_RlWBAImageInfoSize_Type())
rlWBAImageInfoSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBAImageInfoSize.setStatus(_A)
_RlWBAImageClear_Type=Integer32
_RlWBAImageClear_Object=MibScalar
rlWBAImageClear=_RlWBAImageClear_Object((1,3,6,1,4,1,89,230,5),_RlWBAImageClear_Type())
rlWBAImageClear.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBAImageClear.setStatus(_A)
_RlWBADataClear_Type=Integer32
_RlWBADataClear_Object=MibScalar
rlWBADataClear=_RlWBADataClear_Object((1,3,6,1,4,1,89,230,6),_RlWBADataClear_Type())
rlWBADataClear.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBADataClear.setStatus(_A)
_RlWBAImageDownloadFinishStatus_Type=Integer32
_RlWBAImageDownloadFinishStatus_Object=MibScalar
rlWBAImageDownloadFinishStatus=_RlWBAImageDownloadFinishStatus_Object((1,3,6,1,4,1,89,230,7),_RlWBAImageDownloadFinishStatus_Type())
rlWBAImageDownloadFinishStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlWBAImageDownloadFinishStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RlWBAStatusType':RlWBAStatusType,_I:RlWBARetryFlagOp,'rlWBA':rlWBA,'rlWBAAuxiliaryTable':rlWBAAuxiliaryTable,'rlWBAAuxiliaryEntry':rlWBAAuxiliaryEntry,_G:rlWBAIp,'rlWBAStatus':rlWBAStatus,'rlAuxFailReason':rlAuxFailReason,'rlIsRetryFlag':rlIsRetryFlag,'rlWBAUsername':rlWBAUsername,'rlWBAPassword':rlWBAPassword,'rlWBAImageTable':rlWBAImageTable,'rlWBAImageEntry':rlWBAImageEntry,_J:rlWBAImageNumber,_K:rlWBAImageIndex,'rlWBAImageText':rlWBAImageText,'rlWBADataTable':rlWBADataTable,'rlWBADataEntry':rlWBADataEntry,_L:rlWBADataNumber,_M:rlWBADataIndex,'rlWBADataText':rlWBADataText,'rlWBAImageInfoTable':rlWBAImageInfoTable,'rlWBAImageInfoEntry':rlWBAImageInfoEntry,_N:rlWBAImageInfoNumber,'rlWBAImageInfoName':rlWBAImageInfoName,'rlWBAImageInfoSize':rlWBAImageInfoSize,'rlWBAImageClear':rlWBAImageClear,'rlWBADataClear':rlWBADataClear,'rlWBAImageDownloadFinishStatus':rlWBAImageDownloadFinishStatus})