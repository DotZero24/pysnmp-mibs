_K='rlIscsiQosProfileIndex'
_J='rlIscsiQosFlowDestAddress'
_I='rlIscsiQosFlowDestAddressType'
_H='rlIscsiQosFlowType'
_G='rlIscsiQosFlowDestTcpPort'
_F='rlQosApps'
_E='not-accessible'
_D='CISCOSB-QOS-APPS-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rlQosApps,switch001=mibBuilder.importSymbols('CISCOSB-MIB',_F,'switch001')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlQosApps=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,232))
if mibBuilder.loadTexts:rlQosApps.setRevisions(('2016-06-02 00:00',))
_RlIscsiQos_ObjectIdentity=ObjectIdentity
rlIscsiQos=_RlIscsiQos_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,232,1))
_RlIscsiQosEnable_Type=TruthValue
_RlIscsiQosEnable_Object=MibScalar
rlIscsiQosEnable=_RlIscsiQosEnable_Object((1,3,6,1,4,1,9,6,1,101,232,1,1),_RlIscsiQosEnable_Type())
rlIscsiQosEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiQosEnable.setStatus(_A)
_RlIscsiQosFlowTable_Object=MibTable
rlIscsiQosFlowTable=_RlIscsiQosFlowTable_Object((1,3,6,1,4,1,9,6,1,101,232,1,2))
if mibBuilder.loadTexts:rlIscsiQosFlowTable.setStatus(_A)
_RlIscsiQosFlowEntry_Object=MibTableRow
rlIscsiQosFlowEntry=_RlIscsiQosFlowEntry_Object((1,3,6,1,4,1,9,6,1,101,232,1,2,1))
rlIscsiQosFlowEntry.setIndexNames((0,_D,_G),(0,_D,_H),(0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:rlIscsiQosFlowEntry.setStatus(_A)
class _RlIscsiQosFlowDestTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlIscsiQosFlowDestTcpPort_Type.__name__=_B
_RlIscsiQosFlowDestTcpPort_Object=MibTableColumn
rlIscsiQosFlowDestTcpPort=_RlIscsiQosFlowDestTcpPort_Object((1,3,6,1,4,1,9,6,1,101,232,1,2,1,1),_RlIscsiQosFlowDestTcpPort_Type())
rlIscsiQosFlowDestTcpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiQosFlowDestTcpPort.setStatus(_A)
class _RlIscsiQosFlowType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('both',3)))
_RlIscsiQosFlowType_Type.__name__=_B
_RlIscsiQosFlowType_Object=MibTableColumn
rlIscsiQosFlowType=_RlIscsiQosFlowType_Object((1,3,6,1,4,1,9,6,1,101,232,1,2,1,2),_RlIscsiQosFlowType_Type())
rlIscsiQosFlowType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiQosFlowType.setStatus(_A)
_RlIscsiQosFlowDestAddressType_Type=InetAddressType
_RlIscsiQosFlowDestAddressType_Object=MibTableColumn
rlIscsiQosFlowDestAddressType=_RlIscsiQosFlowDestAddressType_Object((1,3,6,1,4,1,9,6,1,101,232,1,2,1,3),_RlIscsiQosFlowDestAddressType_Type())
rlIscsiQosFlowDestAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiQosFlowDestAddressType.setStatus(_A)
_RlIscsiQosFlowDestAddress_Type=InetAddress
_RlIscsiQosFlowDestAddress_Object=MibTableColumn
rlIscsiQosFlowDestAddress=_RlIscsiQosFlowDestAddress_Object((1,3,6,1,4,1,9,6,1,101,232,1,2,1,4),_RlIscsiQosFlowDestAddress_Type())
rlIscsiQosFlowDestAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiQosFlowDestAddress.setStatus(_A)
_RlIscsiQosFlowStatus_Type=RowStatus
_RlIscsiQosFlowStatus_Object=MibTableColumn
rlIscsiQosFlowStatus=_RlIscsiQosFlowStatus_Object((1,3,6,1,4,1,9,6,1,101,232,1,2,1,5),_RlIscsiQosFlowStatus_Type())
rlIscsiQosFlowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiQosFlowStatus.setStatus(_A)
_RlIscsiQosProfileTable_Object=MibTable
rlIscsiQosProfileTable=_RlIscsiQosProfileTable_Object((1,3,6,1,4,1,9,6,1,101,232,1,3))
if mibBuilder.loadTexts:rlIscsiQosProfileTable.setStatus(_A)
_RlIscsiQosProfileEntry_Object=MibTableRow
rlIscsiQosProfileEntry=_RlIscsiQosProfileEntry_Object((1,3,6,1,4,1,9,6,1,101,232,1,3,1))
rlIscsiQosProfileEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:rlIscsiQosProfileEntry.setStatus(_A)
class _RlIscsiQosProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIscsiQosProfileIndex_Type.__name__=_B
_RlIscsiQosProfileIndex_Object=MibTableColumn
rlIscsiQosProfileIndex=_RlIscsiQosProfileIndex_Object((1,3,6,1,4,1,9,6,1,101,232,1,3,1,1),_RlIscsiQosProfileIndex_Type())
rlIscsiQosProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlIscsiQosProfileIndex.setStatus(_A)
class _RlIscsiQosProfileVpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlIscsiQosProfileVpt_Type.__name__=_B
_RlIscsiQosProfileVpt_Object=MibTableColumn
rlIscsiQosProfileVpt=_RlIscsiQosProfileVpt_Object((1,3,6,1,4,1,9,6,1,101,232,1,3,1,2),_RlIscsiQosProfileVpt_Type())
rlIscsiQosProfileVpt.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiQosProfileVpt.setStatus(_A)
class _RlIscsiQosProfileDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlIscsiQosProfileDscp_Type.__name__=_B
_RlIscsiQosProfileDscp_Object=MibTableColumn
rlIscsiQosProfileDscp=_RlIscsiQosProfileDscp_Object((1,3,6,1,4,1,9,6,1,101,232,1,3,1,3),_RlIscsiQosProfileDscp_Type())
rlIscsiQosProfileDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiQosProfileDscp.setStatus(_A)
class _RlIscsiQosProfileQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlIscsiQosProfileQueue_Type.__name__=_B
_RlIscsiQosProfileQueue_Object=MibTableColumn
rlIscsiQosProfileQueue=_RlIscsiQosProfileQueue_Object((1,3,6,1,4,1,9,6,1,101,232,1,3,1,4),_RlIscsiQosProfileQueue_Type())
rlIscsiQosProfileQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiQosProfileQueue.setStatus(_A)
_RlIscsiQosProfileStatus_Type=RowStatus
_RlIscsiQosProfileStatus_Object=MibTableColumn
rlIscsiQosProfileStatus=_RlIscsiQosProfileStatus_Object((1,3,6,1,4,1,9,6,1,101,232,1,3,1,5),_RlIscsiQosProfileStatus_Type())
rlIscsiQosProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIscsiQosProfileStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_F:rlQosApps,'rlIscsiQos':rlIscsiQos,'rlIscsiQosEnable':rlIscsiQosEnable,'rlIscsiQosFlowTable':rlIscsiQosFlowTable,'rlIscsiQosFlowEntry':rlIscsiQosFlowEntry,_G:rlIscsiQosFlowDestTcpPort,_H:rlIscsiQosFlowType,_I:rlIscsiQosFlowDestAddressType,_J:rlIscsiQosFlowDestAddress,'rlIscsiQosFlowStatus':rlIscsiQosFlowStatus,'rlIscsiQosProfileTable':rlIscsiQosProfileTable,'rlIscsiQosProfileEntry':rlIscsiQosProfileEntry,_K:rlIscsiQosProfileIndex,'rlIscsiQosProfileVpt':rlIscsiQosProfileVpt,'rlIscsiQosProfileDscp':rlIscsiQosProfileDscp,'rlIscsiQosProfileQueue':rlIscsiQosProfileQueue,'rlIscsiQosProfileStatus':rlIscsiQosProfileStatus})