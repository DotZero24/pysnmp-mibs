_L='protocolsProtocolFssLLDPEntry'
_K='read-create'
_J='lldp-instancePortIfIndex'
_I='UnsignedByte'
_H='UnsignedShort'
_G='disable'
_F='protocolsProtocolName'
_E='FUJITSU-PROTOCOLS-MIB'
_D='FUJITSU-LLDP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fssProtocols,=mibBuilder.importSymbols('FSS-COMMON-SMI','fssProtocols')
protocolsProtocolEntry,protocolsProtocolName=mibBuilder.importSymbols(_E,'protocolsProtocolEntry',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fssLLDP=ModuleIdentity((1,3,6,1,4,1,211,1,24,12,1100,1100))
if mibBuilder.loadTexts:fssLLDP.setRevisions(('2016-11-03 00:00',))
class UnsignedByte(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class UnsignedShort(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class InetAddressIP(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
class String(TextualConvention,OctetString):status=_A;displayHint='1t'
_ProtocolsProtocolFssLLDPTable_Object=MibTable
protocolsProtocolFssLLDPTable=_ProtocolsProtocolFssLLDPTable_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,1))
if mibBuilder.loadTexts:protocolsProtocolFssLLDPTable.setStatus(_A)
_ProtocolsProtocolFssLLDPEntry_Object=MibTableRow
protocolsProtocolFssLLDPEntry=_ProtocolsProtocolFssLLDPEntry_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,1,1))
if mibBuilder.loadTexts:protocolsProtocolFssLLDPEntry.setStatus(_A)
class _Lldp_instanceGlobal_configAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('enable',1)))
_Lldp_instanceGlobal_configAdminStatus_Type.__name__=_B
_Lldp_instanceGlobal_configAdminStatus_Object=MibTableColumn
lldp_instanceGlobal_configAdminStatus=_Lldp_instanceGlobal_configAdminStatus_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,1,1,1),_Lldp_instanceGlobal_configAdminStatus_Type())
lldp_instanceGlobal_configAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lldp_instanceGlobal_configAdminStatus.setStatus(_A)
class _Lldp_instanceGlobal_configMsgTxInterval_Type(UnsignedShort):defaultValue=30;subtypeSpec=UnsignedShort.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,32768))
_Lldp_instanceGlobal_configMsgTxInterval_Type.__name__=_H
_Lldp_instanceGlobal_configMsgTxInterval_Object=MibTableColumn
lldp_instanceGlobal_configMsgTxInterval=_Lldp_instanceGlobal_configMsgTxInterval_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,1,1,2),_Lldp_instanceGlobal_configMsgTxInterval_Type())
lldp_instanceGlobal_configMsgTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:lldp_instanceGlobal_configMsgTxInterval.setStatus(_A)
class _Lldp_instanceGlobal_configMsgTxHoldMultiplier_Type(UnsignedByte):defaultValue=4;subtypeSpec=UnsignedByte.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_Lldp_instanceGlobal_configMsgTxHoldMultiplier_Type.__name__=_I
_Lldp_instanceGlobal_configMsgTxHoldMultiplier_Object=MibTableColumn
lldp_instanceGlobal_configMsgTxHoldMultiplier=_Lldp_instanceGlobal_configMsgTxHoldMultiplier_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,1,1,3),_Lldp_instanceGlobal_configMsgTxHoldMultiplier_Type())
lldp_instanceGlobal_configMsgTxHoldMultiplier.setMaxAccess(_C)
if mibBuilder.loadTexts:lldp_instanceGlobal_configMsgTxHoldMultiplier.setStatus(_A)
_Lldp_instancePortTable_Object=MibTable
lldp_instancePortTable=_Lldp_instancePortTable_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,2))
if mibBuilder.loadTexts:lldp_instancePortTable.setStatus(_A)
_Lldp_instancePortEntry_Object=MibTableRow
lldp_instancePortEntry=_Lldp_instancePortEntry_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,2,1))
lldp_instancePortEntry.setIndexNames((0,_E,_F),(0,_D,_J))
if mibBuilder.loadTexts:lldp_instancePortEntry.setStatus(_A)
class _Lldp_instancePortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Lldp_instancePortIfIndex_Type.__name__=_B
_Lldp_instancePortIfIndex_Object=MibTableColumn
lldp_instancePortIfIndex=_Lldp_instancePortIfIndex_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,2,1,1),_Lldp_instancePortIfIndex_Type())
lldp_instancePortIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:lldp_instancePortIfIndex.setStatus(_A)
class _Lldp_instancePortAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('txandrx',1),('txonly',2),('rxonly',3)))
_Lldp_instancePortAdminStatus_Type.__name__=_B
_Lldp_instancePortAdminStatus_Object=MibTableColumn
lldp_instancePortAdminStatus=_Lldp_instancePortAdminStatus_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,2,1,2),_Lldp_instancePortAdminStatus_Type())
lldp_instancePortAdminStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:lldp_instancePortAdminStatus.setStatus(_A)
_Lldp_instancePortRowstatus_Type=RowStatus
_Lldp_instancePortRowstatus_Object=MibTableColumn
lldp_instancePortRowstatus=_Lldp_instancePortRowstatus_Object((1,3,6,1,4,1,211,1,24,12,1100,1100,2,1,3),_Lldp_instancePortRowstatus_Type())
lldp_instancePortRowstatus.setMaxAccess(_K)
if mibBuilder.loadTexts:lldp_instancePortRowstatus.setStatus(_A)
protocolsProtocolEntry.registerAugmentions((_D,_L))
protocolsProtocolFssLLDPEntry.setIndexNames(*protocolsProtocolEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{_I:UnsignedByte,_H:UnsignedShort,'InetAddressIP':InetAddressIP,'String':String,'fssLLDP':fssLLDP,'protocolsProtocolFssLLDPTable':protocolsProtocolFssLLDPTable,_L:protocolsProtocolFssLLDPEntry,'lldp-instanceGlobal-configAdminStatus':lldp_instanceGlobal_configAdminStatus,'lldp-instanceGlobal-configMsgTxInterval':lldp_instanceGlobal_configMsgTxInterval,'lldp-instanceGlobal-configMsgTxHoldMultiplier':lldp_instanceGlobal_configMsgTxHoldMultiplier,'lldp-instancePortTable':lldp_instancePortTable,'lldp-instancePortEntry':lldp_instancePortEntry,_J:lldp_instancePortIfIndex,'lldp-instancePortAdminStatus':lldp_instancePortAdminStatus,'lldp-instancePortRowstatus':lldp_instancePortRowstatus})