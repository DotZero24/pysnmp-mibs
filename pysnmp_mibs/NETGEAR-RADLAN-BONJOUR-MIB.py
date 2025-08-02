_N='rlBonjourL2Ifindex'
_M='rlBonjourStateL2Interface'
_L='rlBonjourStateServiceName'
_K='rlBonjourStatusIPInterfaceAddr'
_J='rlBonjourStatusIPInterfaceType'
_I='rlBonjourStatusServiceName'
_H='exclude'
_G='include'
_F='read-write'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='NETGEAR-RADLAN-BONJOUR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rlBonjour=ModuleIdentity((1,3,6,1,4,1,4526,17,114))
if mibBuilder.loadTexts:rlBonjour.setRevisions(('2009-04-23 00:00','2015-05-12 00:00'))
class RlBonjourServiceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('rlBonjourNotPublished',0),('rlBonjourInactive',1),('rlBonjourRegistering',2),('rlBonjourRunning',3)))
class RlBonjourOperationState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
class RlBonjourOperationReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('notExclude',0),(_G,1),('notInclude',2),(_H,3),('bonjourDisabled',4),('serviceDisabled',5),('noIPaddress',6),('l2InterfaceDown',7),('notPresent',8),('unknown',9)))
class _RlBonjourPublish_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RlBonjourPublish_Type.__name__=_E
_RlBonjourPublish_Object=MibScalar
rlBonjourPublish=_RlBonjourPublish_Object((1,3,6,1,4,1,4526,17,114,1),_RlBonjourPublish_Type())
rlBonjourPublish.setMaxAccess(_F)
if mibBuilder.loadTexts:rlBonjourPublish.setStatus(_A)
_RlBonjourStatusTable_Object=MibTable
rlBonjourStatusTable=_RlBonjourStatusTable_Object((1,3,6,1,4,1,4526,17,114,2))
if mibBuilder.loadTexts:rlBonjourStatusTable.setStatus(_A)
_RlBonjourStatusEntry_Object=MibTableRow
rlBonjourStatusEntry=_RlBonjourStatusEntry_Object((1,3,6,1,4,1,4526,17,114,2,1))
rlBonjourStatusEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:rlBonjourStatusEntry.setStatus(_A)
_RlBonjourStatusServiceName_Type=DisplayString
_RlBonjourStatusServiceName_Object=MibTableColumn
rlBonjourStatusServiceName=_RlBonjourStatusServiceName_Object((1,3,6,1,4,1,4526,17,114,2,1,1),_RlBonjourStatusServiceName_Type())
rlBonjourStatusServiceName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBonjourStatusServiceName.setStatus(_A)
_RlBonjourStatusIPInterfaceType_Type=InetAddressType
_RlBonjourStatusIPInterfaceType_Object=MibTableColumn
rlBonjourStatusIPInterfaceType=_RlBonjourStatusIPInterfaceType_Object((1,3,6,1,4,1,4526,17,114,2,1,2),_RlBonjourStatusIPInterfaceType_Type())
rlBonjourStatusIPInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBonjourStatusIPInterfaceType.setStatus(_A)
_RlBonjourStatusIPInterfaceAddr_Type=InetAddress
_RlBonjourStatusIPInterfaceAddr_Object=MibTableColumn
rlBonjourStatusIPInterfaceAddr=_RlBonjourStatusIPInterfaceAddr_Object((1,3,6,1,4,1,4526,17,114,2,1,3),_RlBonjourStatusIPInterfaceAddr_Type())
rlBonjourStatusIPInterfaceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBonjourStatusIPInterfaceAddr.setStatus(_A)
_RlBonjourStatusState_Type=RlBonjourServiceState
_RlBonjourStatusState_Object=MibTableColumn
rlBonjourStatusState=_RlBonjourStatusState_Object((1,3,6,1,4,1,4526,17,114,2,1,4),_RlBonjourStatusState_Type())
rlBonjourStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBonjourStatusState.setStatus(_A)
_RlBonjourStateTable_Object=MibTable
rlBonjourStateTable=_RlBonjourStateTable_Object((1,3,6,1,4,1,4526,17,114,3))
if mibBuilder.loadTexts:rlBonjourStateTable.setStatus(_A)
_RlBonjourStateEntry_Object=MibTableRow
rlBonjourStateEntry=_RlBonjourStateEntry_Object((1,3,6,1,4,1,4526,17,114,3,1))
rlBonjourStateEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:rlBonjourStateEntry.setStatus(_A)
_RlBonjourStateServiceName_Type=DisplayString
_RlBonjourStateServiceName_Object=MibTableColumn
rlBonjourStateServiceName=_RlBonjourStateServiceName_Object((1,3,6,1,4,1,4526,17,114,3,1,1),_RlBonjourStateServiceName_Type())
rlBonjourStateServiceName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBonjourStateServiceName.setStatus(_A)
_RlBonjourStateL2Interface_Type=InterfaceIndex
_RlBonjourStateL2Interface_Object=MibTableColumn
rlBonjourStateL2Interface=_RlBonjourStateL2Interface_Object((1,3,6,1,4,1,4526,17,114,3,1,2),_RlBonjourStateL2Interface_Type())
rlBonjourStateL2Interface.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBonjourStateL2Interface.setStatus(_A)
_RlBonjourStateOperationMode_Type=RlBonjourOperationState
_RlBonjourStateOperationMode_Object=MibTableColumn
rlBonjourStateOperationMode=_RlBonjourStateOperationMode_Object((1,3,6,1,4,1,4526,17,114,3,1,3),_RlBonjourStateOperationMode_Type())
rlBonjourStateOperationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBonjourStateOperationMode.setStatus(_A)
_RlBonjourStateOperationReason_Type=RlBonjourOperationReason
_RlBonjourStateOperationReason_Object=MibTableColumn
rlBonjourStateOperationReason=_RlBonjourStateOperationReason_Object((1,3,6,1,4,1,4526,17,114,3,1,4),_RlBonjourStateOperationReason_Type())
rlBonjourStateOperationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBonjourStateOperationReason.setStatus(_A)
_RlBonjourStateIPv6OperationMode_Type=RlBonjourOperationState
_RlBonjourStateIPv6OperationMode_Object=MibTableColumn
rlBonjourStateIPv6OperationMode=_RlBonjourStateIPv6OperationMode_Object((1,3,6,1,4,1,4526,17,114,3,1,5),_RlBonjourStateIPv6OperationMode_Type())
rlBonjourStateIPv6OperationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBonjourStateIPv6OperationMode.setStatus(_A)
_RlBonjourStateIPv6OperationReason_Type=RlBonjourOperationReason
_RlBonjourStateIPv6OperationReason_Object=MibTableColumn
rlBonjourStateIPv6OperationReason=_RlBonjourStateIPv6OperationReason_Object((1,3,6,1,4,1,4526,17,114,3,1,6),_RlBonjourStateIPv6OperationReason_Type())
rlBonjourStateIPv6OperationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBonjourStateIPv6OperationReason.setStatus(_A)
_RlBonjourL2Table_Object=MibTable
rlBonjourL2Table=_RlBonjourL2Table_Object((1,3,6,1,4,1,4526,17,114,4))
if mibBuilder.loadTexts:rlBonjourL2Table.setStatus(_A)
_RlBonjourL2Entry_Object=MibTableRow
rlBonjourL2Entry=_RlBonjourL2Entry_Object((1,3,6,1,4,1,4526,17,114,4,1))
rlBonjourL2Entry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:rlBonjourL2Entry.setStatus(_A)
_RlBonjourL2Ifindex_Type=InterfaceIndex
_RlBonjourL2Ifindex_Object=MibTableColumn
rlBonjourL2Ifindex=_RlBonjourL2Ifindex_Object((1,3,6,1,4,1,4526,17,114,4,1,1),_RlBonjourL2Ifindex_Type())
rlBonjourL2Ifindex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBonjourL2Ifindex.setStatus(_A)
_RlBonjourL2RowStatus_Type=RowStatus
_RlBonjourL2RowStatus_Object=MibTableColumn
rlBonjourL2RowStatus=_RlBonjourL2RowStatus_Object((1,3,6,1,4,1,4526,17,114,4,1,2),_RlBonjourL2RowStatus_Type())
rlBonjourL2RowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rlBonjourL2RowStatus.setStatus(_A)
class _RlBonjourL2Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RlBonjourL2Mode_Type.__name__=_E
_RlBonjourL2Mode_Object=MibScalar
rlBonjourL2Mode=_RlBonjourL2Mode_Object((1,3,6,1,4,1,4526,17,114,5),_RlBonjourL2Mode_Type())
rlBonjourL2Mode.setMaxAccess(_F)
if mibBuilder.loadTexts:rlBonjourL2Mode.setStatus(_A)
_RlBonjourInstanceName_Type=Integer32
_RlBonjourInstanceName_Object=MibScalar
rlBonjourInstanceName=_RlBonjourInstanceName_Object((1,3,6,1,4,1,4526,17,114,6),_RlBonjourInstanceName_Type())
rlBonjourInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBonjourInstanceName.setStatus(_A)
_RlBonjourHostName_Type=Integer32
_RlBonjourHostName_Object=MibScalar
rlBonjourHostName=_RlBonjourHostName_Object((1,3,6,1,4,1,4526,17,114,7),_RlBonjourHostName_Type())
rlBonjourHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBonjourHostName.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RlBonjourServiceState':RlBonjourServiceState,'RlBonjourOperationState':RlBonjourOperationState,'RlBonjourOperationReason':RlBonjourOperationReason,'rlBonjour':rlBonjour,'rlBonjourPublish':rlBonjourPublish,'rlBonjourStatusTable':rlBonjourStatusTable,'rlBonjourStatusEntry':rlBonjourStatusEntry,_I:rlBonjourStatusServiceName,_J:rlBonjourStatusIPInterfaceType,_K:rlBonjourStatusIPInterfaceAddr,'rlBonjourStatusState':rlBonjourStatusState,'rlBonjourStateTable':rlBonjourStateTable,'rlBonjourStateEntry':rlBonjourStateEntry,_L:rlBonjourStateServiceName,_M:rlBonjourStateL2Interface,'rlBonjourStateOperationMode':rlBonjourStateOperationMode,'rlBonjourStateOperationReason':rlBonjourStateOperationReason,'rlBonjourStateIPv6OperationMode':rlBonjourStateIPv6OperationMode,'rlBonjourStateIPv6OperationReason':rlBonjourStateIPv6OperationReason,'rlBonjourL2Table':rlBonjourL2Table,'rlBonjourL2Entry':rlBonjourL2Entry,_N:rlBonjourL2Ifindex,'rlBonjourL2RowStatus':rlBonjourL2RowStatus,'rlBonjourL2Mode':rlBonjourL2Mode,'rlBonjourInstanceName':rlBonjourInstanceName,'rlBonjourHostName':rlBonjourHostName})