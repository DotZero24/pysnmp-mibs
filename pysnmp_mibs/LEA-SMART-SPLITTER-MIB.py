_F='relayIndex'
_E='LEA-SMART-SPLITTER-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
leaSplitters,=mibBuilder.importSymbols('LEA-MIB','leaSplitters')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
leaSmartSplitter=ModuleIdentity((1,3,6,1,4,1,14841,1,1))
if mibBuilder.loadTexts:leaSmartSplitter.setRevisions(('2002-09-26 00:00',))
_SplitterRelay_ObjectIdentity=ObjectIdentity
splitterRelay=_SplitterRelay_ObjectIdentity((1,3,6,1,4,1,14841,1,1,1))
class _RelayActiveDuration_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_RelayActiveDuration_Type.__name__=_B
_RelayActiveDuration_Object=MibScalar
relayActiveDuration=_RelayActiveDuration_Object((1,3,6,1,4,1,14841,1,1,1,1),_RelayActiveDuration_Type())
relayActiveDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:relayActiveDuration.setStatus(_A)
class _NumberOfActiveRelays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_NumberOfActiveRelays_Type.__name__=_B
_NumberOfActiveRelays_Object=MibScalar
numberOfActiveRelays=_NumberOfActiveRelays_Object((1,3,6,1,4,1,14841,1,1,1,2),_NumberOfActiveRelays_Type())
numberOfActiveRelays.setMaxAccess(_C)
if mibBuilder.loadTexts:numberOfActiveRelays.setStatus(_A)
class _HeartBeat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ack',1))
_HeartBeat_Type.__name__=_B
_HeartBeat_Object=MibScalar
heartBeat=_HeartBeat_Object((1,3,6,1,4,1,14841,1,1,1,3),_HeartBeat_Type())
heartBeat.setMaxAccess(_C)
if mibBuilder.loadTexts:heartBeat.setStatus(_A)
_RelayTable_Object=MibTable
relayTable=_RelayTable_Object((1,3,6,1,4,1,14841,1,1,1,4))
if mibBuilder.loadTexts:relayTable.setStatus(_A)
_RelayTableEntry_Object=MibTableRow
relayTableEntry=_RelayTableEntry_Object((1,3,6,1,4,1,14841,1,1,1,4,1))
relayTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:relayTableEntry.setStatus(_A)
_RelayIndex_Type=Integer32
_RelayIndex_Object=MibTableColumn
relayIndex=_RelayIndex_Object((1,3,6,1,4,1,14841,1,1,1,4,1,1),_RelayIndex_Type())
relayIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:relayIndex.setStatus(_A)
class _RelaySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('Slot-1',1),('Slot-2',2),('Slot-3',3),('Slot-4',4),('Slot-5',5),('Slot-6',6),('Slot-7',7),('Slot-8',8),('Slot-9',9),('Slot-10',10),('Slot-11',11),('Slot-12',12),('Slot-13',13),('Slot-14',14),('Slot-15',15)))
_RelaySlot_Type.__name__=_B
_RelaySlot_Object=MibTableColumn
relaySlot=_RelaySlot_Object((1,3,6,1,4,1,14841,1,1,1,4,1,2),_RelaySlot_Type())
relaySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:relaySlot.setStatus(_A)
class _RelayPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('Port-1',1),('Port-2',2),('Port-3',3),('Port-4',4),('Port-5',5),('Port-6',6),('Port-7',7),('Port-8',8),('Port-9',9),('Port-10',10),('Port-11',11),('Port-12',12),('Port-13',13),('Port-14',14),('Port-15',15),('Port-16',16),('Port-17',17),('Port-18',18),('Port-19',19),('Port-20',20),('Port-21',21),('Port-22',22),('Port-23',23),('Port-24',24)))
_RelayPort_Type.__name__=_B
_RelayPort_Object=MibTableColumn
relayPort=_RelayPort_Object((1,3,6,1,4,1,14841,1,1,1,4,1,3),_RelayPort_Type())
relayPort.setMaxAccess(_C)
if mibBuilder.loadTexts:relayPort.setStatus(_A)
class _RelayStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('closed',2)))
_RelayStatus_Type.__name__=_B
_RelayStatus_Object=MibTableColumn
relayStatus=_RelayStatus_Object((1,3,6,1,4,1,14841,1,1,1,4,1,4),_RelayStatus_Type())
relayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:relayStatus.setStatus(_A)
class _RelayResetAll_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unchanged',1),('reset',2)))
_RelayResetAll_Type.__name__=_B
_RelayResetAll_Object=MibScalar
relayResetAll=_RelayResetAll_Object((1,3,6,1,4,1,14841,1,1,1,5),_RelayResetAll_Type())
relayResetAll.setMaxAccess(_D)
if mibBuilder.loadTexts:relayResetAll.setStatus(_A)
_RelayChangeNotification_Type=SnmpAdminString
_RelayChangeNotification_Object=MibScalar
relayChangeNotification=_RelayChangeNotification_Object((1,3,6,1,4,1,14841,1,1,1,6),_RelayChangeNotification_Type())
relayChangeNotification.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:relayChangeNotification.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'leaSmartSplitter':leaSmartSplitter,'splitterRelay':splitterRelay,'relayActiveDuration':relayActiveDuration,'numberOfActiveRelays':numberOfActiveRelays,'heartBeat':heartBeat,'relayTable':relayTable,'relayTableEntry':relayTableEntry,_F:relayIndex,'relaySlot':relaySlot,'relayPort':relayPort,'relayStatus':relayStatus,'relayResetAll':relayResetAll,'relayChangeNotification':relayChangeNotification})