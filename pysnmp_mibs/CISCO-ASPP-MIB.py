_c='asppPortsAposGroup'
_b='asppPortsGenericGroup'
_a='asppPortDCDAlways'
_Z='asppPortDirect'
_Y='asppPortSendAck'
_X='asppPortDisableEnq'
_W='asppPortDelayEnq'
_V='asppPortRetryCount'
_U='asppPortConnectTimer'
_T='asppPortHostTimer'
_S='asppPortRxTimer'
_R='asppPortRspTimer'
_Q='asppPortIgnoreSequenceNumber'
_P='asppPortSOFCharacter'
_O='asppPortEOFCharacter'
_N='asppPortDeviceAddressOffset'
_M='asppPortReceiveInterFrameTimeout'
_L='asppPortRole'
_K='asppPortProtocol'
_J='milliseconds'
_I='ifIndex'
_H='IF-MIB'
_G='asppPortsGroup'
_F='seconds'
_E='TruthValue'
_D='Integer32'
_C='read-only'
_B='CISCO-ASPP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
ciscoAsppMIB=ModuleIdentity((1,3,6,1,4,1,9,9,55))
if mibBuilder.loadTexts:ciscoAsppMIB.setRevisions(('2003-02-10 00:00','1995-08-21 00:00'))
_AsppObjects_ObjectIdentity=ObjectIdentity
asppObjects=_AsppObjects_ObjectIdentity((1,3,6,1,4,1,9,9,55,1))
_AsppPorts_ObjectIdentity=ObjectIdentity
asppPorts=_AsppPorts_ObjectIdentity((1,3,6,1,4,1,9,9,55,1,1))
_AsppPortTable_Object=MibTable
asppPortTable=_AsppPortTable_Object((1,3,6,1,4,1,9,9,55,1,1,1))
if mibBuilder.loadTexts:asppPortTable.setStatus(_A)
_AsppPortEntry_Object=MibTableRow
asppPortEntry=_AsppPortEntry_Object((1,3,6,1,4,1,9,9,55,1,1,1,1))
asppPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:asppPortEntry.setStatus(_A)
class _AsppPortProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('adplex',1),('adtPollSelect',2),('adtVariPoll',3),('diebold',4),('asyncGeneric',5),('mdi',6),('mosec',7),('gddb',8),('apos',9)))
_AsppPortProtocol_Type.__name__=_D
_AsppPortProtocol_Object=MibTableColumn
asppPortProtocol=_AsppPortProtocol_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,1),_AsppPortProtocol_Type())
asppPortProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortProtocol.setStatus(_A)
class _AsppPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_AsppPortRole_Type.__name__=_D
_AsppPortRole_Object=MibTableColumn
asppPortRole=_AsppPortRole_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,2),_AsppPortRole_Type())
asppPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortRole.setStatus(_A)
class _AsppPortReceiveInterFrameTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AsppPortReceiveInterFrameTimeout_Type.__name__=_D
_AsppPortReceiveInterFrameTimeout_Object=MibTableColumn
asppPortReceiveInterFrameTimeout=_AsppPortReceiveInterFrameTimeout_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,3),_AsppPortReceiveInterFrameTimeout_Type())
asppPortReceiveInterFrameTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortReceiveInterFrameTimeout.setStatus(_A)
if mibBuilder.loadTexts:asppPortReceiveInterFrameTimeout.setUnits(_J)
class _AsppPortDeviceAddressOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AsppPortDeviceAddressOffset_Type.__name__=_D
_AsppPortDeviceAddressOffset_Object=MibTableColumn
asppPortDeviceAddressOffset=_AsppPortDeviceAddressOffset_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,4),_AsppPortDeviceAddressOffset_Type())
asppPortDeviceAddressOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortDeviceAddressOffset.setStatus(_A)
if mibBuilder.loadTexts:asppPortDeviceAddressOffset.setUnits('bytes')
class _AsppPortEOFCharacter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_AsppPortEOFCharacter_Type.__name__=_D
_AsppPortEOFCharacter_Object=MibTableColumn
asppPortEOFCharacter=_AsppPortEOFCharacter_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,5),_AsppPortEOFCharacter_Type())
asppPortEOFCharacter.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortEOFCharacter.setStatus(_A)
class _AsppPortSOFCharacter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_AsppPortSOFCharacter_Type.__name__=_D
_AsppPortSOFCharacter_Object=MibTableColumn
asppPortSOFCharacter=_AsppPortSOFCharacter_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,6),_AsppPortSOFCharacter_Type())
asppPortSOFCharacter.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortSOFCharacter.setStatus(_A)
class _AsppPortIgnoreSequenceNumber_Type(TruthValue):defaultValue=2
_AsppPortIgnoreSequenceNumber_Type.__name__=_E
_AsppPortIgnoreSequenceNumber_Object=MibTableColumn
asppPortIgnoreSequenceNumber=_AsppPortIgnoreSequenceNumber_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,7),_AsppPortIgnoreSequenceNumber_Type())
asppPortIgnoreSequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortIgnoreSequenceNumber.setStatus(_A)
class _AsppPortRspTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AsppPortRspTimer_Type.__name__=_D
_AsppPortRspTimer_Object=MibTableColumn
asppPortRspTimer=_AsppPortRspTimer_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,8),_AsppPortRspTimer_Type())
asppPortRspTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortRspTimer.setStatus(_A)
if mibBuilder.loadTexts:asppPortRspTimer.setUnits(_F)
class _AsppPortRxTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60))
_AsppPortRxTimer_Type.__name__=_D
_AsppPortRxTimer_Object=MibTableColumn
asppPortRxTimer=_AsppPortRxTimer_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,9),_AsppPortRxTimer_Type())
asppPortRxTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortRxTimer.setStatus(_A)
if mibBuilder.loadTexts:asppPortRxTimer.setUnits(_F)
class _AsppPortHostTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,120))
_AsppPortHostTimer_Type.__name__=_D
_AsppPortHostTimer_Object=MibTableColumn
asppPortHostTimer=_AsppPortHostTimer_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,10),_AsppPortHostTimer_Type())
asppPortHostTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortHostTimer.setStatus(_A)
if mibBuilder.loadTexts:asppPortHostTimer.setUnits(_F)
class _AsppPortConnectTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AsppPortConnectTimer_Type.__name__=_D
_AsppPortConnectTimer_Object=MibTableColumn
asppPortConnectTimer=_AsppPortConnectTimer_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,11),_AsppPortConnectTimer_Type())
asppPortConnectTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortConnectTimer.setStatus(_A)
if mibBuilder.loadTexts:asppPortConnectTimer.setUnits(_F)
class _AsppPortRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AsppPortRetryCount_Type.__name__=_D
_AsppPortRetryCount_Object=MibTableColumn
asppPortRetryCount=_AsppPortRetryCount_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,12),_AsppPortRetryCount_Type())
asppPortRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortRetryCount.setStatus(_A)
class _AsppPortDelayEnq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_AsppPortDelayEnq_Type.__name__=_D
_AsppPortDelayEnq_Object=MibTableColumn
asppPortDelayEnq=_AsppPortDelayEnq_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,13),_AsppPortDelayEnq_Type())
asppPortDelayEnq.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortDelayEnq.setStatus(_A)
if mibBuilder.loadTexts:asppPortDelayEnq.setUnits(_J)
class _AsppPortDisableEnq_Type(TruthValue):defaultValue=2
_AsppPortDisableEnq_Type.__name__=_E
_AsppPortDisableEnq_Object=MibTableColumn
asppPortDisableEnq=_AsppPortDisableEnq_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,14),_AsppPortDisableEnq_Type())
asppPortDisableEnq.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortDisableEnq.setStatus(_A)
class _AsppPortSendAck_Type(TruthValue):defaultValue=2
_AsppPortSendAck_Type.__name__=_E
_AsppPortSendAck_Object=MibTableColumn
asppPortSendAck=_AsppPortSendAck_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,15),_AsppPortSendAck_Type())
asppPortSendAck.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortSendAck.setStatus(_A)
class _AsppPortDirect_Type(TruthValue):defaultValue=2
_AsppPortDirect_Type.__name__=_E
_AsppPortDirect_Object=MibTableColumn
asppPortDirect=_AsppPortDirect_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,16),_AsppPortDirect_Type())
asppPortDirect.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortDirect.setStatus(_A)
class _AsppPortDCDAlways_Type(TruthValue):defaultValue=2
_AsppPortDCDAlways_Type.__name__=_E
_AsppPortDCDAlways_Object=MibTableColumn
asppPortDCDAlways=_AsppPortDCDAlways_Object((1,3,6,1,4,1,9,9,55,1,1,1,1,17),_AsppPortDCDAlways_Type())
asppPortDCDAlways.setMaxAccess(_C)
if mibBuilder.loadTexts:asppPortDCDAlways.setStatus(_A)
_AsppMibConformance_ObjectIdentity=ObjectIdentity
asppMibConformance=_AsppMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,55,3))
_AsppMibCompliances_ObjectIdentity=ObjectIdentity
asppMibCompliances=_AsppMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,55,3,1))
_AsppMibGroups_ObjectIdentity=ObjectIdentity
asppMibGroups=_AsppMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,55,3,2))
asppPortsGroup=ObjectGroup((1,3,6,1,4,1,9,9,55,3,2,1))
asppPortsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:asppPortsGroup.setStatus(_A)
asppPortsGenericGroup=ObjectGroup((1,3,6,1,4,1,9,9,55,3,2,2))
asppPortsGenericGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:asppPortsGenericGroup.setStatus(_A)
asppPortsAposGroup=ObjectGroup((1,3,6,1,4,1,9,9,55,3,2,3))
asppPortsAposGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:asppPortsAposGroup.setStatus(_A)
asppMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,55,3,1,1))
asppMibCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:asppMibCompliance.setStatus('deprecated')
asppMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,55,3,1,2))
asppMibComplianceRev1.setObjects(*((_B,_G),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:asppMibComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoAsppMIB':ciscoAsppMIB,'asppObjects':asppObjects,'asppPorts':asppPorts,'asppPortTable':asppPortTable,'asppPortEntry':asppPortEntry,_K:asppPortProtocol,_L:asppPortRole,_M:asppPortReceiveInterFrameTimeout,_N:asppPortDeviceAddressOffset,_O:asppPortEOFCharacter,_P:asppPortSOFCharacter,_Q:asppPortIgnoreSequenceNumber,_R:asppPortRspTimer,_S:asppPortRxTimer,_T:asppPortHostTimer,_U:asppPortConnectTimer,_V:asppPortRetryCount,_W:asppPortDelayEnq,_X:asppPortDisableEnq,_Y:asppPortSendAck,_Z:asppPortDirect,_a:asppPortDCDAlways,'asppMibConformance':asppMibConformance,'asppMibCompliances':asppMibCompliances,'asppMibCompliance':asppMibCompliance,'asppMibComplianceRev1':asppMibComplianceRev1,'asppMibGroups':asppMibGroups,_G:asppPortsGroup,_b:asppPortsGenericGroup,_c:asppPortsAposGroup})