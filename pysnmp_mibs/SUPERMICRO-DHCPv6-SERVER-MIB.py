_W='fsDhcp6SrvIfHmacFailCount'
_V='fsDhcp6SrvIfInvalidPktIn'
_U='fsDhcp6SrvIfUnknownTlvType'
_T='fsDhcp6SrvKeyIdentifier'
_S='fsDhcp6SrvClientIndex'
_R='fsDhcp6SrvIfIndex'
_Q='fsDhcp6SrvSubOptionType'
_P='fsDhcp6SrvIncludePrefixIndex'
_O='fsDhcp6SrvIncludePrefixContextId'
_N='Unsigned32'
_M='fsDhcp6SrvRealmIndex'
_L='fsDhcp6SrvOptionIndex'
_K='FsDhcp6SrvDuidType'
_J='DisplayString'
_I='fsDhcp6SrvPoolIndex'
_H='OctetString'
_G='read-write'
_F='not-accessible'
_E='Integer32'
_D='read-only'
_C='SUPERMICRO-DHCPv6-SERVER-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention','TruthValue')
fsdhcpv6srv=ModuleIdentity((1,3,6,1,4,1,10876,101,2,42))
if mibBuilder.loadTexts:fsdhcpv6srv.setRevisions(('2012-09-05 00:00',))
class FsDhcp6SrvDuidValue(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
class FsDhcp6SrvDuidType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dtLlt',1),('dtEn',2),('dtLl',3)))
_FsDhcp6SrvNotify_ObjectIdentity=ObjectIdentity
fsDhcp6SrvNotify=_FsDhcp6SrvNotify_ObjectIdentity((1,3,6,1,4,1,10876,101,2,42,0))
_FsDhcp6SrvSystem_ObjectIdentity=ObjectIdentity
fsDhcp6SrvSystem=_FsDhcp6SrvSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,2,42,1))
class _FsDhcp6SrvDebugTrace_Type(DisplayString):defaultValue=OctetString('critical');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsDhcp6SrvDebugTrace_Type.__name__=_J
_FsDhcp6SrvDebugTrace_Object=MibScalar
fsDhcp6SrvDebugTrace=_FsDhcp6SrvDebugTrace_Object((1,3,6,1,4,1,10876,101,2,42,1,1),_FsDhcp6SrvDebugTrace_Type())
fsDhcp6SrvDebugTrace.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6SrvDebugTrace.setStatus(_A)
_FsDhcp6SrvRealmTableNextIndex_Type=Unsigned32
_FsDhcp6SrvRealmTableNextIndex_Object=MibScalar
fsDhcp6SrvRealmTableNextIndex=_FsDhcp6SrvRealmTableNextIndex_Object((1,3,6,1,4,1,10876,101,2,42,1,2),_FsDhcp6SrvRealmTableNextIndex_Type())
fsDhcp6SrvRealmTableNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvRealmTableNextIndex.setStatus(_A)
_FsDhcp6SrvClientTableNextIndex_Type=Unsigned32
_FsDhcp6SrvClientTableNextIndex_Object=MibScalar
fsDhcp6SrvClientTableNextIndex=_FsDhcp6SrvClientTableNextIndex_Object((1,3,6,1,4,1,10876,101,2,42,1,3),_FsDhcp6SrvClientTableNextIndex_Type())
fsDhcp6SrvClientTableNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvClientTableNextIndex.setStatus(_A)
_FsDhcp6SrvPoolTableNextIndex_Type=Unsigned32
_FsDhcp6SrvPoolTableNextIndex_Object=MibScalar
fsDhcp6SrvPoolTableNextIndex=_FsDhcp6SrvPoolTableNextIndex_Object((1,3,6,1,4,1,10876,101,2,42,1,4),_FsDhcp6SrvPoolTableNextIndex_Type())
fsDhcp6SrvPoolTableNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvPoolTableNextIndex.setStatus(_A)
_FsDhcp6SrvIncludePrefixTableNextIndex_Type=Unsigned32
_FsDhcp6SrvIncludePrefixTableNextIndex_Object=MibScalar
fsDhcp6SrvIncludePrefixTableNextIndex=_FsDhcp6SrvIncludePrefixTableNextIndex_Object((1,3,6,1,4,1,10876,101,2,42,1,5),_FsDhcp6SrvIncludePrefixTableNextIndex_Type())
fsDhcp6SrvIncludePrefixTableNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvIncludePrefixTableNextIndex.setStatus(_A)
class _FsDhcp6SrvTrapAdminControl_Type(Bits):namedValues=NamedValues(*(('none',0),('trapUnknownTlv',1),('trapInvalidPacketIn',2),('trapHmacAuthFail',3)))
_FsDhcp6SrvTrapAdminControl_Type.__name__='Bits'
_FsDhcp6SrvTrapAdminControl_Object=MibScalar
fsDhcp6SrvTrapAdminControl=_FsDhcp6SrvTrapAdminControl_Object((1,3,6,1,4,1,10876,101,2,42,1,6),_FsDhcp6SrvTrapAdminControl_Type())
fsDhcp6SrvTrapAdminControl.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6SrvTrapAdminControl.setStatus(_A)
class _FsDhcp6SrvSysLogAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsDhcp6SrvSysLogAdminStatus_Type.__name__=_E
_FsDhcp6SrvSysLogAdminStatus_Object=MibScalar
fsDhcp6SrvSysLogAdminStatus=_FsDhcp6SrvSysLogAdminStatus_Object((1,3,6,1,4,1,10876,101,2,42,1,7),_FsDhcp6SrvSysLogAdminStatus_Type())
fsDhcp6SrvSysLogAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6SrvSysLogAdminStatus.setStatus(_A)
class _FsDhcp6SrvListenPort_Type(Integer32):defaultValue=547;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDhcp6SrvListenPort_Type.__name__=_E
_FsDhcp6SrvListenPort_Object=MibScalar
fsDhcp6SrvListenPort=_FsDhcp6SrvListenPort_Object((1,3,6,1,4,1,10876,101,2,42,1,8),_FsDhcp6SrvListenPort_Type())
fsDhcp6SrvListenPort.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6SrvListenPort.setStatus(_A)
class _FsDhcp6SrvClientTransmitPort_Type(Integer32):defaultValue=546;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDhcp6SrvClientTransmitPort_Type.__name__=_E
_FsDhcp6SrvClientTransmitPort_Object=MibScalar
fsDhcp6SrvClientTransmitPort=_FsDhcp6SrvClientTransmitPort_Object((1,3,6,1,4,1,10876,101,2,42,1,9),_FsDhcp6SrvClientTransmitPort_Type())
fsDhcp6SrvClientTransmitPort.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6SrvClientTransmitPort.setStatus(_A)
class _FsDhcp6SrvRelayTransmitPort_Type(Integer32):defaultValue=547;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDhcp6SrvRelayTransmitPort_Type.__name__=_E
_FsDhcp6SrvRelayTransmitPort_Object=MibScalar
fsDhcp6SrvRelayTransmitPort=_FsDhcp6SrvRelayTransmitPort_Object((1,3,6,1,4,1,10876,101,2,42,1,10),_FsDhcp6SrvRelayTransmitPort_Type())
fsDhcp6SrvRelayTransmitPort.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6SrvRelayTransmitPort.setStatus(_A)
_FsDhcp6SrvConfig_ObjectIdentity=ObjectIdentity
fsDhcp6SrvConfig=_FsDhcp6SrvConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,2,42,2))
_FsDhcp6SrvPoolTable_Object=MibTable
fsDhcp6SrvPoolTable=_FsDhcp6SrvPoolTable_Object((1,3,6,1,4,1,10876,101,2,42,2,1))
if mibBuilder.loadTexts:fsDhcp6SrvPoolTable.setStatus(_A)
_FsDhcp6SrvPoolEntry_Object=MibTableRow
fsDhcp6SrvPoolEntry=_FsDhcp6SrvPoolEntry_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1))
fsDhcp6SrvPoolEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:fsDhcp6SrvPoolEntry.setStatus(_A)
_FsDhcp6SrvPoolIndex_Type=Unsigned32
_FsDhcp6SrvPoolIndex_Object=MibTableColumn
fsDhcp6SrvPoolIndex=_FsDhcp6SrvPoolIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1,1),_FsDhcp6SrvPoolIndex_Type())
fsDhcp6SrvPoolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvPoolIndex.setStatus(_A)
class _FsDhcp6SrvPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsDhcp6SrvPoolName_Type.__name__=_J
_FsDhcp6SrvPoolName_Object=MibTableColumn
fsDhcp6SrvPoolName=_FsDhcp6SrvPoolName_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1,2),_FsDhcp6SrvPoolName_Type())
fsDhcp6SrvPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvPoolName.setStatus(_A)
class _FsDhcp6SrvPoolPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsDhcp6SrvPoolPreference_Type.__name__=_E
_FsDhcp6SrvPoolPreference_Object=MibTableColumn
fsDhcp6SrvPoolPreference=_FsDhcp6SrvPoolPreference_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1,3),_FsDhcp6SrvPoolPreference_Type())
fsDhcp6SrvPoolPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvPoolPreference.setStatus(_A)
class _FsDhcp6SrvPoolDuidType_Type(FsDhcp6SrvDuidType):defaultValue=1
_FsDhcp6SrvPoolDuidType_Type.__name__=_K
_FsDhcp6SrvPoolDuidType_Object=MibTableColumn
fsDhcp6SrvPoolDuidType=_FsDhcp6SrvPoolDuidType_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1,4),_FsDhcp6SrvPoolDuidType_Type())
fsDhcp6SrvPoolDuidType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6SrvPoolDuidType.setStatus(_A)
_FsDhcp6SrvPoolDuid_Type=FsDhcp6SrvDuidValue
_FsDhcp6SrvPoolDuid_Object=MibTableColumn
fsDhcp6SrvPoolDuid=_FsDhcp6SrvPoolDuid_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1,5),_FsDhcp6SrvPoolDuid_Type())
fsDhcp6SrvPoolDuid.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvPoolDuid.setStatus(_A)
class _FsDhcp6SrvPoolDuidIfIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDhcp6SrvPoolDuidIfIndex_Type.__name__=_E
_FsDhcp6SrvPoolDuidIfIndex_Object=MibTableColumn
fsDhcp6SrvPoolDuidIfIndex=_FsDhcp6SrvPoolDuidIfIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1,6),_FsDhcp6SrvPoolDuidIfIndex_Type())
fsDhcp6SrvPoolDuidIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6SrvPoolDuidIfIndex.setStatus(_A)
_FsDhcp6SrvPoolOptionTableNextIndex_Type=Unsigned32
_FsDhcp6SrvPoolOptionTableNextIndex_Object=MibTableColumn
fsDhcp6SrvPoolOptionTableNextIndex=_FsDhcp6SrvPoolOptionTableNextIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1,7),_FsDhcp6SrvPoolOptionTableNextIndex_Type())
fsDhcp6SrvPoolOptionTableNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvPoolOptionTableNextIndex.setStatus(_A)
_FsDhcp6SrvPoolRowStatus_Type=RowStatus
_FsDhcp6SrvPoolRowStatus_Object=MibTableColumn
fsDhcp6SrvPoolRowStatus=_FsDhcp6SrvPoolRowStatus_Object((1,3,6,1,4,1,10876,101,2,42,2,1,1,8),_FsDhcp6SrvPoolRowStatus_Type())
fsDhcp6SrvPoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvPoolRowStatus.setStatus(_A)
_FsDhcp6SrvIncludePrefixTable_Object=MibTable
fsDhcp6SrvIncludePrefixTable=_FsDhcp6SrvIncludePrefixTable_Object((1,3,6,1,4,1,10876,101,2,42,2,2))
if mibBuilder.loadTexts:fsDhcp6SrvIncludePrefixTable.setStatus(_A)
_FsDhcp6SrvIncludePrefixEntry_Object=MibTableRow
fsDhcp6SrvIncludePrefixEntry=_FsDhcp6SrvIncludePrefixEntry_Object((1,3,6,1,4,1,10876,101,2,42,2,2,1))
fsDhcp6SrvIncludePrefixEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:fsDhcp6SrvIncludePrefixEntry.setStatus(_A)
class _FsDhcp6SrvIncludePrefixContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsDhcp6SrvIncludePrefixContextId_Type.__name__=_E
_FsDhcp6SrvIncludePrefixContextId_Object=MibTableColumn
fsDhcp6SrvIncludePrefixContextId=_FsDhcp6SrvIncludePrefixContextId_Object((1,3,6,1,4,1,10876,101,2,42,2,2,1,1),_FsDhcp6SrvIncludePrefixContextId_Type())
fsDhcp6SrvIncludePrefixContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvIncludePrefixContextId.setStatus(_A)
class _FsDhcp6SrvIncludePrefixIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDhcp6SrvIncludePrefixIndex_Type.__name__=_E
_FsDhcp6SrvIncludePrefixIndex_Object=MibTableColumn
fsDhcp6SrvIncludePrefixIndex=_FsDhcp6SrvIncludePrefixIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,2,1,2),_FsDhcp6SrvIncludePrefixIndex_Type())
fsDhcp6SrvIncludePrefixIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvIncludePrefixIndex.setStatus(_A)
class _FsDhcp6SrvIncludePrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsDhcp6SrvIncludePrefix_Type.__name__=_H
_FsDhcp6SrvIncludePrefix_Object=MibTableColumn
fsDhcp6SrvIncludePrefix=_FsDhcp6SrvIncludePrefix_Object((1,3,6,1,4,1,10876,101,2,42,2,2,1,3),_FsDhcp6SrvIncludePrefix_Type())
fsDhcp6SrvIncludePrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvIncludePrefix.setStatus(_A)
_FsDhcp6SrvIncludePrefixPool_Type=Integer32
_FsDhcp6SrvIncludePrefixPool_Object=MibTableColumn
fsDhcp6SrvIncludePrefixPool=_FsDhcp6SrvIncludePrefixPool_Object((1,3,6,1,4,1,10876,101,2,42,2,2,1,4),_FsDhcp6SrvIncludePrefixPool_Type())
fsDhcp6SrvIncludePrefixPool.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvIncludePrefixPool.setStatus(_A)
_FsDhcp6SrvIncludePrefixRowStatus_Type=RowStatus
_FsDhcp6SrvIncludePrefixRowStatus_Object=MibTableColumn
fsDhcp6SrvIncludePrefixRowStatus=_FsDhcp6SrvIncludePrefixRowStatus_Object((1,3,6,1,4,1,10876,101,2,42,2,2,1,5),_FsDhcp6SrvIncludePrefixRowStatus_Type())
fsDhcp6SrvIncludePrefixRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvIncludePrefixRowStatus.setStatus(_A)
_FsDhcp6SrvOptionTable_Object=MibTable
fsDhcp6SrvOptionTable=_FsDhcp6SrvOptionTable_Object((1,3,6,1,4,1,10876,101,2,42,2,3))
if mibBuilder.loadTexts:fsDhcp6SrvOptionTable.setStatus(_A)
_FsDhcp6SrvOptionEntry_Object=MibTableRow
fsDhcp6SrvOptionEntry=_FsDhcp6SrvOptionEntry_Object((1,3,6,1,4,1,10876,101,2,42,2,3,1))
fsDhcp6SrvOptionEntry.setIndexNames((0,_C,_I),(0,_C,_L))
if mibBuilder.loadTexts:fsDhcp6SrvOptionEntry.setStatus(_A)
_FsDhcp6SrvOptionIndex_Type=Unsigned32
_FsDhcp6SrvOptionIndex_Object=MibTableColumn
fsDhcp6SrvOptionIndex=_FsDhcp6SrvOptionIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,3,1,1),_FsDhcp6SrvOptionIndex_Type())
fsDhcp6SrvOptionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvOptionIndex.setStatus(_A)
class _FsDhcp6SrvOptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDhcp6SrvOptionType_Type.__name__=_E
_FsDhcp6SrvOptionType_Object=MibTableColumn
fsDhcp6SrvOptionType=_FsDhcp6SrvOptionType_Object((1,3,6,1,4,1,10876,101,2,42,2,3,1,2),_FsDhcp6SrvOptionType_Type())
fsDhcp6SrvOptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvOptionType.setStatus(_A)
_FsDhcp6SrvOptionLength_Type=Integer32
_FsDhcp6SrvOptionLength_Object=MibTableColumn
fsDhcp6SrvOptionLength=_FsDhcp6SrvOptionLength_Object((1,3,6,1,4,1,10876,101,2,42,2,3,1,3),_FsDhcp6SrvOptionLength_Type())
fsDhcp6SrvOptionLength.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvOptionLength.setStatus(_A)
class _FsDhcp6SrvOptionValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsDhcp6SrvOptionValue_Type.__name__=_H
_FsDhcp6SrvOptionValue_Object=MibTableColumn
fsDhcp6SrvOptionValue=_FsDhcp6SrvOptionValue_Object((1,3,6,1,4,1,10876,101,2,42,2,3,1,4),_FsDhcp6SrvOptionValue_Type())
fsDhcp6SrvOptionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvOptionValue.setStatus(_A)
class _FsDhcp6SrvOptionPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsDhcp6SrvOptionPreference_Type.__name__=_E
_FsDhcp6SrvOptionPreference_Object=MibTableColumn
fsDhcp6SrvOptionPreference=_FsDhcp6SrvOptionPreference_Object((1,3,6,1,4,1,10876,101,2,42,2,3,1,5),_FsDhcp6SrvOptionPreference_Type())
fsDhcp6SrvOptionPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvOptionPreference.setStatus(_A)
_FsDhcp6SrvOptionRowStatus_Type=RowStatus
_FsDhcp6SrvOptionRowStatus_Object=MibTableColumn
fsDhcp6SrvOptionRowStatus=_FsDhcp6SrvOptionRowStatus_Object((1,3,6,1,4,1,10876,101,2,42,2,3,1,6),_FsDhcp6SrvOptionRowStatus_Type())
fsDhcp6SrvOptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvOptionRowStatus.setStatus(_A)
_FsDhcp6SrvSubOptionTable_Object=MibTable
fsDhcp6SrvSubOptionTable=_FsDhcp6SrvSubOptionTable_Object((1,3,6,1,4,1,10876,101,2,42,2,4))
if mibBuilder.loadTexts:fsDhcp6SrvSubOptionTable.setStatus(_A)
_FsDhcp6SrvSubOptionEntry_Object=MibTableRow
fsDhcp6SrvSubOptionEntry=_FsDhcp6SrvSubOptionEntry_Object((1,3,6,1,4,1,10876,101,2,42,2,4,1))
fsDhcp6SrvSubOptionEntry.setIndexNames((0,_C,_I),(0,_C,_L),(0,_C,_Q))
if mibBuilder.loadTexts:fsDhcp6SrvSubOptionEntry.setStatus(_A)
class _FsDhcp6SrvSubOptionType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsDhcp6SrvSubOptionType_Type.__name__=_N
_FsDhcp6SrvSubOptionType_Object=MibTableColumn
fsDhcp6SrvSubOptionType=_FsDhcp6SrvSubOptionType_Object((1,3,6,1,4,1,10876,101,2,42,2,4,1,1),_FsDhcp6SrvSubOptionType_Type())
fsDhcp6SrvSubOptionType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvSubOptionType.setStatus(_A)
_FsDhcp6SrvSubOptionLength_Type=Integer32
_FsDhcp6SrvSubOptionLength_Object=MibTableColumn
fsDhcp6SrvSubOptionLength=_FsDhcp6SrvSubOptionLength_Object((1,3,6,1,4,1,10876,101,2,42,2,4,1,2),_FsDhcp6SrvSubOptionLength_Type())
fsDhcp6SrvSubOptionLength.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvSubOptionLength.setStatus(_A)
class _FsDhcp6SrvSubOptionValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsDhcp6SrvSubOptionValue_Type.__name__=_H
_FsDhcp6SrvSubOptionValue_Object=MibTableColumn
fsDhcp6SrvSubOptionValue=_FsDhcp6SrvSubOptionValue_Object((1,3,6,1,4,1,10876,101,2,42,2,4,1,3),_FsDhcp6SrvSubOptionValue_Type())
fsDhcp6SrvSubOptionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvSubOptionValue.setStatus(_A)
_FsDhcp6SrvSubOptionRowStatus_Type=RowStatus
_FsDhcp6SrvSubOptionRowStatus_Object=MibTableColumn
fsDhcp6SrvSubOptionRowStatus=_FsDhcp6SrvSubOptionRowStatus_Object((1,3,6,1,4,1,10876,101,2,42,2,4,1,4),_FsDhcp6SrvSubOptionRowStatus_Type())
fsDhcp6SrvSubOptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvSubOptionRowStatus.setStatus(_A)
_FsDhcp6SrvIfTable_Object=MibTable
fsDhcp6SrvIfTable=_FsDhcp6SrvIfTable_Object((1,3,6,1,4,1,10876,101,2,42,2,5))
if mibBuilder.loadTexts:fsDhcp6SrvIfTable.setStatus(_A)
_FsDhcp6SrvIfEntry_Object=MibTableRow
fsDhcp6SrvIfEntry=_FsDhcp6SrvIfEntry_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1))
fsDhcp6SrvIfEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:fsDhcp6SrvIfEntry.setStatus(_A)
class _FsDhcp6SrvIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDhcp6SrvIfIndex_Type.__name__=_E
_FsDhcp6SrvIfIndex_Object=MibTableColumn
fsDhcp6SrvIfIndex=_FsDhcp6SrvIfIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,1),_FsDhcp6SrvIfIndex_Type())
fsDhcp6SrvIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvIfIndex.setStatus(_A)
_FsDhcp6SrvIfPool_Type=Integer32
_FsDhcp6SrvIfPool_Object=MibTableColumn
fsDhcp6SrvIfPool=_FsDhcp6SrvIfPool_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,2),_FsDhcp6SrvIfPool_Type())
fsDhcp6SrvIfPool.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvIfPool.setStatus(_A)
_FsDhcp6SrvIfInformIn_Type=Counter32
_FsDhcp6SrvIfInformIn_Object=MibTableColumn
fsDhcp6SrvIfInformIn=_FsDhcp6SrvIfInformIn_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,3),_FsDhcp6SrvIfInformIn_Type())
fsDhcp6SrvIfInformIn.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvIfInformIn.setStatus(_A)
_FsDhcp6SrvIfRelayForwIn_Type=Counter32
_FsDhcp6SrvIfRelayForwIn_Object=MibTableColumn
fsDhcp6SrvIfRelayForwIn=_FsDhcp6SrvIfRelayForwIn_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,4),_FsDhcp6SrvIfRelayForwIn_Type())
fsDhcp6SrvIfRelayForwIn.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvIfRelayForwIn.setStatus(_A)
_FsDhcp6SrvIfReplyOut_Type=Counter32
_FsDhcp6SrvIfReplyOut_Object=MibTableColumn
fsDhcp6SrvIfReplyOut=_FsDhcp6SrvIfReplyOut_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,5),_FsDhcp6SrvIfReplyOut_Type())
fsDhcp6SrvIfReplyOut.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvIfReplyOut.setStatus(_A)
_FsDhcp6SrvIfRelayReplyOut_Type=Counter32
_FsDhcp6SrvIfRelayReplyOut_Object=MibTableColumn
fsDhcp6SrvIfRelayReplyOut=_FsDhcp6SrvIfRelayReplyOut_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,6),_FsDhcp6SrvIfRelayReplyOut_Type())
fsDhcp6SrvIfRelayReplyOut.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvIfRelayReplyOut.setStatus(_A)
_FsDhcp6SrvIfInvalidPktIn_Type=Counter32
_FsDhcp6SrvIfInvalidPktIn_Object=MibTableColumn
fsDhcp6SrvIfInvalidPktIn=_FsDhcp6SrvIfInvalidPktIn_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,7),_FsDhcp6SrvIfInvalidPktIn_Type())
fsDhcp6SrvIfInvalidPktIn.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvIfInvalidPktIn.setStatus(_A)
_FsDhcp6SrvIfUnknownTlvType_Type=Integer32
_FsDhcp6SrvIfUnknownTlvType_Object=MibTableColumn
fsDhcp6SrvIfUnknownTlvType=_FsDhcp6SrvIfUnknownTlvType_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,8),_FsDhcp6SrvIfUnknownTlvType_Type())
fsDhcp6SrvIfUnknownTlvType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvIfUnknownTlvType.setStatus(_A)
_FsDhcp6SrvIfHmacFailCount_Type=Counter32
_FsDhcp6SrvIfHmacFailCount_Object=MibTableColumn
fsDhcp6SrvIfHmacFailCount=_FsDhcp6SrvIfHmacFailCount_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,9),_FsDhcp6SrvIfHmacFailCount_Type())
fsDhcp6SrvIfHmacFailCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvIfHmacFailCount.setStatus(_A)
_FsDhcp6SrvIfCounterReset_Type=TruthValue
_FsDhcp6SrvIfCounterReset_Object=MibTableColumn
fsDhcp6SrvIfCounterReset=_FsDhcp6SrvIfCounterReset_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,10),_FsDhcp6SrvIfCounterReset_Type())
fsDhcp6SrvIfCounterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvIfCounterReset.setStatus(_A)
_FsDhcp6SrvIfRowStatus_Type=RowStatus
_FsDhcp6SrvIfRowStatus_Object=MibTableColumn
fsDhcp6SrvIfRowStatus=_FsDhcp6SrvIfRowStatus_Object((1,3,6,1,4,1,10876,101,2,42,2,5,1,11),_FsDhcp6SrvIfRowStatus_Type())
fsDhcp6SrvIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvIfRowStatus.setStatus(_A)
_FsDhcp6SrvRealmTable_Object=MibTable
fsDhcp6SrvRealmTable=_FsDhcp6SrvRealmTable_Object((1,3,6,1,4,1,10876,101,2,42,2,6))
if mibBuilder.loadTexts:fsDhcp6SrvRealmTable.setStatus(_A)
_FsDhcp6SrvRealmEntry_Object=MibTableRow
fsDhcp6SrvRealmEntry=_FsDhcp6SrvRealmEntry_Object((1,3,6,1,4,1,10876,101,2,42,2,6,1))
fsDhcp6SrvRealmEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:fsDhcp6SrvRealmEntry.setStatus(_A)
_FsDhcp6SrvRealmIndex_Type=Unsigned32
_FsDhcp6SrvRealmIndex_Object=MibTableColumn
fsDhcp6SrvRealmIndex=_FsDhcp6SrvRealmIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,6,1,1),_FsDhcp6SrvRealmIndex_Type())
fsDhcp6SrvRealmIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvRealmIndex.setStatus(_A)
class _FsDhcp6SrvRealmName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsDhcp6SrvRealmName_Type.__name__=_H
_FsDhcp6SrvRealmName_Object=MibTableColumn
fsDhcp6SrvRealmName=_FsDhcp6SrvRealmName_Object((1,3,6,1,4,1,10876,101,2,42,2,6,1,2),_FsDhcp6SrvRealmName_Type())
fsDhcp6SrvRealmName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvRealmName.setStatus(_A)
_FsDhcp6SrvRealmKeyTableNextIndex_Type=Unsigned32
_FsDhcp6SrvRealmKeyTableNextIndex_Object=MibTableColumn
fsDhcp6SrvRealmKeyTableNextIndex=_FsDhcp6SrvRealmKeyTableNextIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,6,1,3),_FsDhcp6SrvRealmKeyTableNextIndex_Type())
fsDhcp6SrvRealmKeyTableNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcp6SrvRealmKeyTableNextIndex.setStatus(_A)
_FsDhcp6SrvRealmRowStatus_Type=RowStatus
_FsDhcp6SrvRealmRowStatus_Object=MibTableColumn
fsDhcp6SrvRealmRowStatus=_FsDhcp6SrvRealmRowStatus_Object((1,3,6,1,4,1,10876,101,2,42,2,6,1,4),_FsDhcp6SrvRealmRowStatus_Type())
fsDhcp6SrvRealmRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvRealmRowStatus.setStatus(_A)
_FsDhcp6SrvClientTable_Object=MibTable
fsDhcp6SrvClientTable=_FsDhcp6SrvClientTable_Object((1,3,6,1,4,1,10876,101,2,42,2,7))
if mibBuilder.loadTexts:fsDhcp6SrvClientTable.setStatus(_A)
_FsDhcp6SrvClientEntry_Object=MibTableRow
fsDhcp6SrvClientEntry=_FsDhcp6SrvClientEntry_Object((1,3,6,1,4,1,10876,101,2,42,2,7,1))
fsDhcp6SrvClientEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:fsDhcp6SrvClientEntry.setStatus(_A)
_FsDhcp6SrvClientIndex_Type=Unsigned32
_FsDhcp6SrvClientIndex_Object=MibTableColumn
fsDhcp6SrvClientIndex=_FsDhcp6SrvClientIndex_Object((1,3,6,1,4,1,10876,101,2,42,2,7,1,1),_FsDhcp6SrvClientIndex_Type())
fsDhcp6SrvClientIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvClientIndex.setStatus(_A)
_FsDhcp6SrvClientId_Type=FsDhcp6SrvDuidValue
_FsDhcp6SrvClientId_Object=MibTableColumn
fsDhcp6SrvClientId=_FsDhcp6SrvClientId_Object((1,3,6,1,4,1,10876,101,2,42,2,7,1,2),_FsDhcp6SrvClientId_Type())
fsDhcp6SrvClientId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvClientId.setStatus(_A)
class _FsDhcp6SrvClientIdType_Type(FsDhcp6SrvDuidType):defaultValue=1
_FsDhcp6SrvClientIdType_Type.__name__=_K
_FsDhcp6SrvClientIdType_Object=MibTableColumn
fsDhcp6SrvClientIdType=_FsDhcp6SrvClientIdType_Object((1,3,6,1,4,1,10876,101,2,42,2,7,1,3),_FsDhcp6SrvClientIdType_Type())
fsDhcp6SrvClientIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvClientIdType.setStatus(_A)
_FsDhcp6SrvClientRealm_Type=Unsigned32
_FsDhcp6SrvClientRealm_Object=MibTableColumn
fsDhcp6SrvClientRealm=_FsDhcp6SrvClientRealm_Object((1,3,6,1,4,1,10876,101,2,42,2,7,1,4),_FsDhcp6SrvClientRealm_Type())
fsDhcp6SrvClientRealm.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvClientRealm.setStatus(_A)
_FsDhcp6SrvClientRowStatus_Type=RowStatus
_FsDhcp6SrvClientRowStatus_Object=MibTableColumn
fsDhcp6SrvClientRowStatus=_FsDhcp6SrvClientRowStatus_Object((1,3,6,1,4,1,10876,101,2,42,2,7,1,5),_FsDhcp6SrvClientRowStatus_Type())
fsDhcp6SrvClientRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvClientRowStatus.setStatus(_A)
_FsDhcp6SrvKeyTable_Object=MibTable
fsDhcp6SrvKeyTable=_FsDhcp6SrvKeyTable_Object((1,3,6,1,4,1,10876,101,2,42,2,8))
if mibBuilder.loadTexts:fsDhcp6SrvKeyTable.setStatus(_A)
_FsDhcp6SrvKeyEntry_Object=MibTableRow
fsDhcp6SrvKeyEntry=_FsDhcp6SrvKeyEntry_Object((1,3,6,1,4,1,10876,101,2,42,2,8,1))
fsDhcp6SrvKeyEntry.setIndexNames((0,_C,_M),(0,_C,_T))
if mibBuilder.loadTexts:fsDhcp6SrvKeyEntry.setStatus(_A)
_FsDhcp6SrvKeyIdentifier_Type=Unsigned32
_FsDhcp6SrvKeyIdentifier_Object=MibTableColumn
fsDhcp6SrvKeyIdentifier=_FsDhcp6SrvKeyIdentifier_Object((1,3,6,1,4,1,10876,101,2,42,2,8,1,1),_FsDhcp6SrvKeyIdentifier_Type())
fsDhcp6SrvKeyIdentifier.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDhcp6SrvKeyIdentifier.setStatus(_A)
class _FsDhcp6SrvKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsDhcp6SrvKey_Type.__name__=_H
_FsDhcp6SrvKey_Object=MibTableColumn
fsDhcp6SrvKey=_FsDhcp6SrvKey_Object((1,3,6,1,4,1,10876,101,2,42,2,8,1,2),_FsDhcp6SrvKey_Type())
fsDhcp6SrvKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvKey.setStatus(_A)
_FsDhcp6SrvKeyRowStatus_Type=RowStatus
_FsDhcp6SrvKeyRowStatus_Object=MibTableColumn
fsDhcp6SrvKeyRowStatus=_FsDhcp6SrvKeyRowStatus_Object((1,3,6,1,4,1,10876,101,2,42,2,8,1,3),_FsDhcp6SrvKeyRowStatus_Type())
fsDhcp6SrvKeyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6SrvKeyRowStatus.setStatus(_A)
fsDhcp6SrvUnknownTlvTrap=NotificationType((1,3,6,1,4,1,10876,101,2,42,0,1))
fsDhcp6SrvUnknownTlvTrap.setObjects((_C,_U))
if mibBuilder.loadTexts:fsDhcp6SrvUnknownTlvTrap.setStatus(_A)
fsDhcp6SrvInvalidPacketTrap=NotificationType((1,3,6,1,4,1,10876,101,2,42,0,2))
fsDhcp6SrvInvalidPacketTrap.setObjects((_C,_V))
if mibBuilder.loadTexts:fsDhcp6SrvInvalidPacketTrap.setStatus(_A)
fsDhcp6SrvHmacAuthenticationFailTrap=NotificationType((1,3,6,1,4,1,10876,101,2,42,0,3))
fsDhcp6SrvHmacAuthenticationFailTrap.setObjects((_C,_W))
if mibBuilder.loadTexts:fsDhcp6SrvHmacAuthenticationFailTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FsDhcp6SrvDuidValue':FsDhcp6SrvDuidValue,_K:FsDhcp6SrvDuidType,'fsdhcpv6srv':fsdhcpv6srv,'fsDhcp6SrvNotify':fsDhcp6SrvNotify,'fsDhcp6SrvUnknownTlvTrap':fsDhcp6SrvUnknownTlvTrap,'fsDhcp6SrvInvalidPacketTrap':fsDhcp6SrvInvalidPacketTrap,'fsDhcp6SrvHmacAuthenticationFailTrap':fsDhcp6SrvHmacAuthenticationFailTrap,'fsDhcp6SrvSystem':fsDhcp6SrvSystem,'fsDhcp6SrvDebugTrace':fsDhcp6SrvDebugTrace,'fsDhcp6SrvRealmTableNextIndex':fsDhcp6SrvRealmTableNextIndex,'fsDhcp6SrvClientTableNextIndex':fsDhcp6SrvClientTableNextIndex,'fsDhcp6SrvPoolTableNextIndex':fsDhcp6SrvPoolTableNextIndex,'fsDhcp6SrvIncludePrefixTableNextIndex':fsDhcp6SrvIncludePrefixTableNextIndex,'fsDhcp6SrvTrapAdminControl':fsDhcp6SrvTrapAdminControl,'fsDhcp6SrvSysLogAdminStatus':fsDhcp6SrvSysLogAdminStatus,'fsDhcp6SrvListenPort':fsDhcp6SrvListenPort,'fsDhcp6SrvClientTransmitPort':fsDhcp6SrvClientTransmitPort,'fsDhcp6SrvRelayTransmitPort':fsDhcp6SrvRelayTransmitPort,'fsDhcp6SrvConfig':fsDhcp6SrvConfig,'fsDhcp6SrvPoolTable':fsDhcp6SrvPoolTable,'fsDhcp6SrvPoolEntry':fsDhcp6SrvPoolEntry,_I:fsDhcp6SrvPoolIndex,'fsDhcp6SrvPoolName':fsDhcp6SrvPoolName,'fsDhcp6SrvPoolPreference':fsDhcp6SrvPoolPreference,'fsDhcp6SrvPoolDuidType':fsDhcp6SrvPoolDuidType,'fsDhcp6SrvPoolDuid':fsDhcp6SrvPoolDuid,'fsDhcp6SrvPoolDuidIfIndex':fsDhcp6SrvPoolDuidIfIndex,'fsDhcp6SrvPoolOptionTableNextIndex':fsDhcp6SrvPoolOptionTableNextIndex,'fsDhcp6SrvPoolRowStatus':fsDhcp6SrvPoolRowStatus,'fsDhcp6SrvIncludePrefixTable':fsDhcp6SrvIncludePrefixTable,'fsDhcp6SrvIncludePrefixEntry':fsDhcp6SrvIncludePrefixEntry,_O:fsDhcp6SrvIncludePrefixContextId,_P:fsDhcp6SrvIncludePrefixIndex,'fsDhcp6SrvIncludePrefix':fsDhcp6SrvIncludePrefix,'fsDhcp6SrvIncludePrefixPool':fsDhcp6SrvIncludePrefixPool,'fsDhcp6SrvIncludePrefixRowStatus':fsDhcp6SrvIncludePrefixRowStatus,'fsDhcp6SrvOptionTable':fsDhcp6SrvOptionTable,'fsDhcp6SrvOptionEntry':fsDhcp6SrvOptionEntry,_L:fsDhcp6SrvOptionIndex,'fsDhcp6SrvOptionType':fsDhcp6SrvOptionType,'fsDhcp6SrvOptionLength':fsDhcp6SrvOptionLength,'fsDhcp6SrvOptionValue':fsDhcp6SrvOptionValue,'fsDhcp6SrvOptionPreference':fsDhcp6SrvOptionPreference,'fsDhcp6SrvOptionRowStatus':fsDhcp6SrvOptionRowStatus,'fsDhcp6SrvSubOptionTable':fsDhcp6SrvSubOptionTable,'fsDhcp6SrvSubOptionEntry':fsDhcp6SrvSubOptionEntry,_Q:fsDhcp6SrvSubOptionType,'fsDhcp6SrvSubOptionLength':fsDhcp6SrvSubOptionLength,'fsDhcp6SrvSubOptionValue':fsDhcp6SrvSubOptionValue,'fsDhcp6SrvSubOptionRowStatus':fsDhcp6SrvSubOptionRowStatus,'fsDhcp6SrvIfTable':fsDhcp6SrvIfTable,'fsDhcp6SrvIfEntry':fsDhcp6SrvIfEntry,_R:fsDhcp6SrvIfIndex,'fsDhcp6SrvIfPool':fsDhcp6SrvIfPool,'fsDhcp6SrvIfInformIn':fsDhcp6SrvIfInformIn,'fsDhcp6SrvIfRelayForwIn':fsDhcp6SrvIfRelayForwIn,'fsDhcp6SrvIfReplyOut':fsDhcp6SrvIfReplyOut,'fsDhcp6SrvIfRelayReplyOut':fsDhcp6SrvIfRelayReplyOut,_V:fsDhcp6SrvIfInvalidPktIn,_U:fsDhcp6SrvIfUnknownTlvType,_W:fsDhcp6SrvIfHmacFailCount,'fsDhcp6SrvIfCounterReset':fsDhcp6SrvIfCounterReset,'fsDhcp6SrvIfRowStatus':fsDhcp6SrvIfRowStatus,'fsDhcp6SrvRealmTable':fsDhcp6SrvRealmTable,'fsDhcp6SrvRealmEntry':fsDhcp6SrvRealmEntry,_M:fsDhcp6SrvRealmIndex,'fsDhcp6SrvRealmName':fsDhcp6SrvRealmName,'fsDhcp6SrvRealmKeyTableNextIndex':fsDhcp6SrvRealmKeyTableNextIndex,'fsDhcp6SrvRealmRowStatus':fsDhcp6SrvRealmRowStatus,'fsDhcp6SrvClientTable':fsDhcp6SrvClientTable,'fsDhcp6SrvClientEntry':fsDhcp6SrvClientEntry,_S:fsDhcp6SrvClientIndex,'fsDhcp6SrvClientId':fsDhcp6SrvClientId,'fsDhcp6SrvClientIdType':fsDhcp6SrvClientIdType,'fsDhcp6SrvClientRealm':fsDhcp6SrvClientRealm,'fsDhcp6SrvClientRowStatus':fsDhcp6SrvClientRowStatus,'fsDhcp6SrvKeyTable':fsDhcp6SrvKeyTable,'fsDhcp6SrvKeyEntry':fsDhcp6SrvKeyEntry,_T:fsDhcp6SrvKeyIdentifier,'fsDhcp6SrvKey':fsDhcp6SrvKey,'fsDhcp6SrvKeyRowStatus':fsDhcp6SrvKeyRowStatus})