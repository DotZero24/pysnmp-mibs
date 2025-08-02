_L='rlSnaClientAgentMibName'
_K='rlSnaClientAgentAgentAddress'
_J='rlSnaClientAgentAgentAddressType'
_I='rlSnaClientAgentClientSessionId'
_H='TruthValue'
_G='TimeInterval'
_F='OctetString'
_E='DisplayString'
_D='not-accessible'
_C='read-create'
_B='CISCOSB-SNA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TestAndIncr',_G,_H)
rlSna=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,229))
if mibBuilder.loadTexts:rlSna.setRevisions(('2015-05-12 00:00',))
_RlSnaNextFreeSessionId_Type=TestAndIncr
_RlSnaNextFreeSessionId_Object=MibScalar
rlSnaNextFreeSessionId=_RlSnaNextFreeSessionId_Object((1,3,6,1,4,1,9,6,1,101,229,1),_RlSnaNextFreeSessionId_Type())
rlSnaNextFreeSessionId.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlSnaNextFreeSessionId.setStatus(_A)
_RlSnaClientAgentPollingTable_Object=MibTable
rlSnaClientAgentPollingTable=_RlSnaClientAgentPollingTable_Object((1,3,6,1,4,1,9,6,1,101,229,2))
if mibBuilder.loadTexts:rlSnaClientAgentPollingTable.setStatus(_A)
_RlSnaClientAgentPollingEntry_Object=MibTableRow
rlSnaClientAgentPollingEntry=_RlSnaClientAgentPollingEntry_Object((1,3,6,1,4,1,9,6,1,101,229,2,1))
rlSnaClientAgentPollingEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(1,_B,_L))
if mibBuilder.loadTexts:rlSnaClientAgentPollingEntry.setStatus(_A)
_RlSnaClientAgentClientSessionId_Type=Integer32
_RlSnaClientAgentClientSessionId_Object=MibTableColumn
rlSnaClientAgentClientSessionId=_RlSnaClientAgentClientSessionId_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,1),_RlSnaClientAgentClientSessionId_Type())
rlSnaClientAgentClientSessionId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSnaClientAgentClientSessionId.setStatus(_A)
_RlSnaClientAgentAgentAddressType_Type=InetAddressType
_RlSnaClientAgentAgentAddressType_Object=MibTableColumn
rlSnaClientAgentAgentAddressType=_RlSnaClientAgentAgentAddressType_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,2),_RlSnaClientAgentAgentAddressType_Type())
rlSnaClientAgentAgentAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSnaClientAgentAgentAddressType.setStatus(_A)
_RlSnaClientAgentAgentAddress_Type=InetAddress
_RlSnaClientAgentAgentAddress_Object=MibTableColumn
rlSnaClientAgentAgentAddress=_RlSnaClientAgentAgentAddress_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,3),_RlSnaClientAgentAgentAddress_Type())
rlSnaClientAgentAgentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSnaClientAgentAgentAddress.setStatus(_A)
class _RlSnaClientAgentMibName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_RlSnaClientAgentMibName_Type.__name__=_E
_RlSnaClientAgentMibName_Object=MibTableColumn
rlSnaClientAgentMibName=_RlSnaClientAgentMibName_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,4),_RlSnaClientAgentMibName_Type())
rlSnaClientAgentMibName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSnaClientAgentMibName.setStatus(_A)
class _RlSnaClientAgentMibFieldsMask_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlSnaClientAgentMibFieldsMask_Type.__name__=_F
_RlSnaClientAgentMibFieldsMask_Object=MibTableColumn
rlSnaClientAgentMibFieldsMask=_RlSnaClientAgentMibFieldsMask_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,5),_RlSnaClientAgentMibFieldsMask_Type())
rlSnaClientAgentMibFieldsMask.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSnaClientAgentMibFieldsMask.setStatus(_A)
class _RlSnaClientAgentSecondaryMibName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RlSnaClientAgentSecondaryMibName_Type.__name__=_E
_RlSnaClientAgentSecondaryMibName_Object=MibTableColumn
rlSnaClientAgentSecondaryMibName=_RlSnaClientAgentSecondaryMibName_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,6),_RlSnaClientAgentSecondaryMibName_Type())
rlSnaClientAgentSecondaryMibName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSnaClientAgentSecondaryMibName.setStatus(_A)
class _RlSnaClientAgentPollingEnable_Type(TruthValue):defaultValue=2
_RlSnaClientAgentPollingEnable_Type.__name__=_H
_RlSnaClientAgentPollingEnable_Object=MibTableColumn
rlSnaClientAgentPollingEnable=_RlSnaClientAgentPollingEnable_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,7),_RlSnaClientAgentPollingEnable_Type())
rlSnaClientAgentPollingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSnaClientAgentPollingEnable.setStatus(_A)
class _RlSnaClientAgentPollingInterval_Type(TimeInterval):defaultValue=12000
_RlSnaClientAgentPollingInterval_Type.__name__=_G
_RlSnaClientAgentPollingInterval_Object=MibTableColumn
rlSnaClientAgentPollingInterval=_RlSnaClientAgentPollingInterval_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,8),_RlSnaClientAgentPollingInterval_Type())
rlSnaClientAgentPollingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSnaClientAgentPollingInterval.setStatus(_A)
_RlSnaClientAgentStatus_Type=RowStatus
_RlSnaClientAgentStatus_Object=MibTableColumn
rlSnaClientAgentStatus=_RlSnaClientAgentStatus_Object((1,3,6,1,4,1,9,6,1,101,229,2,1,9),_RlSnaClientAgentStatus_Type())
rlSnaClientAgentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSnaClientAgentStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rlSna':rlSna,'rlSnaNextFreeSessionId':rlSnaNextFreeSessionId,'rlSnaClientAgentPollingTable':rlSnaClientAgentPollingTable,'rlSnaClientAgentPollingEntry':rlSnaClientAgentPollingEntry,_I:rlSnaClientAgentClientSessionId,_J:rlSnaClientAgentAgentAddressType,_K:rlSnaClientAgentAgentAddress,_L:rlSnaClientAgentMibName,'rlSnaClientAgentMibFieldsMask':rlSnaClientAgentMibFieldsMask,'rlSnaClientAgentSecondaryMibName':rlSnaClientAgentSecondaryMibName,'rlSnaClientAgentPollingEnable':rlSnaClientAgentPollingEnable,'rlSnaClientAgentPollingInterval':rlSnaClientAgentPollingInterval,'rlSnaClientAgentStatus':rlSnaClientAgentStatus})