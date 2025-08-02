_Z='hm2DlrNetworkStatus'
_Y='Hm2DlrGatewayStatusType'
_X='hm2DlrRingParticipantsIndex'
_W='Hm2DlrTimeInterval'
_V='Hm2DlrNetworkStatusType'
_U='Hm2DlrNetworkTopologyType'
_T='Hm2DlrRingDeviceStatusType'
_S='accessible-for-notify'
_R='supervisor'
_Q='unsupported'
_P='backup'
_O='Integer32'
_N='hm2DlrGatewayIndex'
_M='SnmpAdminString'
_L='000000000000'
_K='00000000'
_J='HmEnabledStatus'
_I='MacAddress'
_H='InetAddress'
_G='InetAddressType'
_F='hm2DlrRingIndex'
_E='HM2-L2REDUNDANCY-DLR-MIB'
_D='Unsigned32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2L2RedundancyMibObjects,=mibBuilder.importSymbols('HM2-L2REDUNDANCY-MIB','hm2L2RedundancyMibObjects')
HmEnabledStatus,=mibBuilder.importSymbols('HM2-TC-MIB',_J)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_G)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_O,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_I,'PhysAddress','RowStatus','TextualConvention')
hm2DlrMibGroup=ModuleIdentity((1,3,6,1,4,1,248,11,40,1,5))
if mibBuilder.loadTexts:hm2DlrMibGroup.setRevisions(('2014-11-07 00:00',))
class Hm2DlrNetworkTopologyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('linear',0),('ring',1)))
class Hm2DlrNetworkStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('normal',0),('ringFault',1),('loop',2),('partial',3),('rapidFault',4)))
class Hm2DlrGatewayStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('nonGateway',0),(_P,1),('active',2),('uplinkFault',3),(_Q,4),('networkFault',5)))
class Hm2DlrRingDeviceStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),(_R,1),('node',2),('nonDlr',3),(_Q,4)))
class Hm2DlrPortStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('blocked',2),('forwarding',3),('notConnected',4)))
class Hm2DlrTimeInterval(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DlrMibNotifications_ObjectIdentity=ObjectIdentity
hm2DlrMibNotifications=_Hm2DlrMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,5,0))
_Hm2DlrMibObjects_ObjectIdentity=ObjectIdentity
hm2DlrMibObjects=_Hm2DlrMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,5,1))
_Hm2DlrConfiguration_ObjectIdentity=ObjectIdentity
hm2DlrConfiguration=_Hm2DlrConfiguration_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,5,1,1))
class _Hm2DlrGlobalAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2DlrGlobalAdminState_Type.__name__=_J
_Hm2DlrGlobalAdminState_Object=MibScalar
hm2DlrGlobalAdminState=_Hm2DlrGlobalAdminState_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,1),_Hm2DlrGlobalAdminState_Type())
hm2DlrGlobalAdminState.setMaxAccess('read-write')
if mibBuilder.loadTexts:hm2DlrGlobalAdminState.setStatus(_A)
_Hm2DlrConfigTable_Object=MibTable
hm2DlrConfigTable=_Hm2DlrConfigTable_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10))
if mibBuilder.loadTexts:hm2DlrConfigTable.setStatus(_A)
_Hm2DlrConfigEntry_Object=MibTableRow
hm2DlrConfigEntry=_Hm2DlrConfigEntry_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1))
hm2DlrConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hm2DlrConfigEntry.setStatus(_A)
class _Hm2DlrRingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2DlrRingIndex_Type.__name__=_D
_Hm2DlrRingIndex_Object=MibTableColumn
hm2DlrRingIndex=_Hm2DlrRingIndex_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,1),_Hm2DlrRingIndex_Type())
hm2DlrRingIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:hm2DlrRingIndex.setStatus(_A)
class _Hm2DlrRingName_Type(SnmpAdminString):defaultValue=OctetString('')
_Hm2DlrRingName_Type.__name__=_M
_Hm2DlrRingName_Object=MibTableColumn
hm2DlrRingName=_Hm2DlrRingName_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,2),_Hm2DlrRingName_Type())
hm2DlrRingName.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrRingName.setStatus(_A)
_Hm2DlrRingport1IfIndex_Type=InterfaceIndexOrZero
_Hm2DlrRingport1IfIndex_Object=MibTableColumn
hm2DlrRingport1IfIndex=_Hm2DlrRingport1IfIndex_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,3),_Hm2DlrRingport1IfIndex_Type())
hm2DlrRingport1IfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrRingport1IfIndex.setStatus(_A)
_Hm2DlrRingport2IfIndex_Type=InterfaceIndexOrZero
_Hm2DlrRingport2IfIndex_Object=MibTableColumn
hm2DlrRingport2IfIndex=_Hm2DlrRingport2IfIndex_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,4),_Hm2DlrRingport2IfIndex_Type())
hm2DlrRingport2IfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrRingport2IfIndex.setStatus(_A)
_Hm2DlrRingport1OperStatus_Type=Hm2DlrPortStatusType
_Hm2DlrRingport1OperStatus_Object=MibTableColumn
hm2DlrRingport1OperStatus=_Hm2DlrRingport1OperStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,5),_Hm2DlrRingport1OperStatus_Type())
hm2DlrRingport1OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrRingport1OperStatus.setStatus(_A)
_Hm2DlrRingport2OperStatus_Type=Hm2DlrPortStatusType
_Hm2DlrRingport2OperStatus_Object=MibTableColumn
hm2DlrRingport2OperStatus=_Hm2DlrRingport2OperStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,6),_Hm2DlrRingport2OperStatus_Type())
hm2DlrRingport2OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrRingport2OperStatus.setStatus(_A)
class _Hm2DlrSupervisorAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2DlrSupervisorAdminState_Type.__name__=_J
_Hm2DlrSupervisorAdminState_Object=MibTableColumn
hm2DlrSupervisorAdminState=_Hm2DlrSupervisorAdminState_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,7),_Hm2DlrSupervisorAdminState_Type())
hm2DlrSupervisorAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrSupervisorAdminState.setStatus(_A)
class _Hm2DlrSupervisorPrecedence_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2DlrSupervisorPrecedence_Type.__name__=_D
_Hm2DlrSupervisorPrecedence_Object=MibTableColumn
hm2DlrSupervisorPrecedence=_Hm2DlrSupervisorPrecedence_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,8),_Hm2DlrSupervisorPrecedence_Type())
hm2DlrSupervisorPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrSupervisorPrecedence.setStatus(_A)
class _Hm2DlrBeaconInterval_Type(Unsigned32):defaultValue=400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,100000))
_Hm2DlrBeaconInterval_Type.__name__=_D
_Hm2DlrBeaconInterval_Object=MibTableColumn
hm2DlrBeaconInterval=_Hm2DlrBeaconInterval_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,9),_Hm2DlrBeaconInterval_Type())
hm2DlrBeaconInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrBeaconInterval.setStatus(_A)
class _Hm2DlrBeaconTimeout_Type(Unsigned32):defaultValue=1960;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(800,500000))
_Hm2DlrBeaconTimeout_Type.__name__=_D
_Hm2DlrBeaconTimeout_Object=MibTableColumn
hm2DlrBeaconTimeout=_Hm2DlrBeaconTimeout_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,10),_Hm2DlrBeaconTimeout_Type())
hm2DlrBeaconTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrBeaconTimeout.setStatus(_A)
class _Hm2DlrVLANID_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4042))
_Hm2DlrVLANID_Type.__name__=_D
_Hm2DlrVLANID_Object=MibTableColumn
hm2DlrVLANID=_Hm2DlrVLANID_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,11),_Hm2DlrVLANID_Type())
hm2DlrVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrVLANID.setStatus(_A)
class _Hm2DlrService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noService',0),('verifyFaultLocation',1),('clearRapidFaults',2),('restartSignOn',3),('clearGatewayPartialFault',4)))
_Hm2DlrService_Type.__name__=_O
_Hm2DlrService_Object=MibTableColumn
hm2DlrService=_Hm2DlrService_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,12),_Hm2DlrService_Type())
hm2DlrService.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrService.setStatus(_A)
_Hm2DlrConfigRowStatus_Type=RowStatus
_Hm2DlrConfigRowStatus_Object=MibTableColumn
hm2DlrConfigRowStatus=_Hm2DlrConfigRowStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,10,1,15),_Hm2DlrConfigRowStatus_Type())
hm2DlrConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrConfigRowStatus.setStatus(_A)
_Hm2DlrGatewayConfigTable_Object=MibTable
hm2DlrGatewayConfigTable=_Hm2DlrGatewayConfigTable_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11))
if mibBuilder.loadTexts:hm2DlrGatewayConfigTable.setStatus(_A)
_Hm2DlrGatewayConfigEntry_Object=MibTableRow
hm2DlrGatewayConfigEntry=_Hm2DlrGatewayConfigEntry_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1))
hm2DlrGatewayConfigEntry.setIndexNames((0,_E,_F),(0,_E,_N))
if mibBuilder.loadTexts:hm2DlrGatewayConfigEntry.setStatus(_A)
class _Hm2DlrGatewayIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2DlrGatewayIndex_Type.__name__=_D
_Hm2DlrGatewayIndex_Object=MibTableColumn
hm2DlrGatewayIndex=_Hm2DlrGatewayIndex_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,1),_Hm2DlrGatewayIndex_Type())
hm2DlrGatewayIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:hm2DlrGatewayIndex.setStatus(_A)
class _Hm2DlrGatewayName_Type(SnmpAdminString):defaultValue=OctetString('')
_Hm2DlrGatewayName_Type.__name__=_M
_Hm2DlrGatewayName_Object=MibTableColumn
hm2DlrGatewayName=_Hm2DlrGatewayName_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,2),_Hm2DlrGatewayName_Type())
hm2DlrGatewayName.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrGatewayName.setStatus(_A)
class _Hm2DlrGatewayConfigLearningUpdate_Type(HmEnabledStatus):defaultValue=1
_Hm2DlrGatewayConfigLearningUpdate_Type.__name__=_J
_Hm2DlrGatewayConfigLearningUpdate_Object=MibTableColumn
hm2DlrGatewayConfigLearningUpdate=_Hm2DlrGatewayConfigLearningUpdate_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,3),_Hm2DlrGatewayConfigLearningUpdate_Type())
hm2DlrGatewayConfigLearningUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrGatewayConfigLearningUpdate.setStatus(_A)
class _Hm2DlrGatewayConfigPrecedence_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2DlrGatewayConfigPrecedence_Type.__name__=_D
_Hm2DlrGatewayConfigPrecedence_Object=MibTableColumn
hm2DlrGatewayConfigPrecedence=_Hm2DlrGatewayConfigPrecedence_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,4),_Hm2DlrGatewayConfigPrecedence_Type())
hm2DlrGatewayConfigPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrGatewayConfigPrecedence.setStatus(_A)
class _Hm2DlrGatewayConfigAdvertiseInterval_Type(Unsigned32):defaultValue=2000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,100000))
_Hm2DlrGatewayConfigAdvertiseInterval_Type.__name__=_D
_Hm2DlrGatewayConfigAdvertiseInterval_Object=MibTableColumn
hm2DlrGatewayConfigAdvertiseInterval=_Hm2DlrGatewayConfigAdvertiseInterval_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,5),_Hm2DlrGatewayConfigAdvertiseInterval_Type())
hm2DlrGatewayConfigAdvertiseInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrGatewayConfigAdvertiseInterval.setStatus(_A)
class _Hm2DlrGatewayConfigAdvertiseTimeout_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2500,500000))
_Hm2DlrGatewayConfigAdvertiseTimeout_Type.__name__=_D
_Hm2DlrGatewayConfigAdvertiseTimeout_Object=MibTableColumn
hm2DlrGatewayConfigAdvertiseTimeout=_Hm2DlrGatewayConfigAdvertiseTimeout_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,6),_Hm2DlrGatewayConfigAdvertiseTimeout_Type())
hm2DlrGatewayConfigAdvertiseTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrGatewayConfigAdvertiseTimeout.setStatus(_A)
_Hm2DlrGatewayConfigUplinkPort1IfIndex_Type=InterfaceIndexOrZero
_Hm2DlrGatewayConfigUplinkPort1IfIndex_Object=MibTableColumn
hm2DlrGatewayConfigUplinkPort1IfIndex=_Hm2DlrGatewayConfigUplinkPort1IfIndex_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,7),_Hm2DlrGatewayConfigUplinkPort1IfIndex_Type())
hm2DlrGatewayConfigUplinkPort1IfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrGatewayConfigUplinkPort1IfIndex.setStatus(_A)
_Hm2DlrGatewayConfigUplinkPort2IfIndex_Type=InterfaceIndexOrZero
_Hm2DlrGatewayConfigUplinkPort2IfIndex_Object=MibTableColumn
hm2DlrGatewayConfigUplinkPort2IfIndex=_Hm2DlrGatewayConfigUplinkPort2IfIndex_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,8),_Hm2DlrGatewayConfigUplinkPort2IfIndex_Type())
hm2DlrGatewayConfigUplinkPort2IfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrGatewayConfigUplinkPort2IfIndex.setStatus(_A)
_Hm2DlrGatewayUplinkPort1OperStatus_Type=Hm2DlrPortStatusType
_Hm2DlrGatewayUplinkPort1OperStatus_Object=MibTableColumn
hm2DlrGatewayUplinkPort1OperStatus=_Hm2DlrGatewayUplinkPort1OperStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,9),_Hm2DlrGatewayUplinkPort1OperStatus_Type())
hm2DlrGatewayUplinkPort1OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrGatewayUplinkPort1OperStatus.setStatus(_A)
_Hm2DlrGatewayUplinkPort2OperStatus_Type=Hm2DlrPortStatusType
_Hm2DlrGatewayUplinkPort2OperStatus_Object=MibTableColumn
hm2DlrGatewayUplinkPort2OperStatus=_Hm2DlrGatewayUplinkPort2OperStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,10),_Hm2DlrGatewayUplinkPort2OperStatus_Type())
hm2DlrGatewayUplinkPort2OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrGatewayUplinkPort2OperStatus.setStatus(_A)
_Hm2DlrGatewayConfigRowStatus_Type=RowStatus
_Hm2DlrGatewayConfigRowStatus_Object=MibTableColumn
hm2DlrGatewayConfigRowStatus=_Hm2DlrGatewayConfigRowStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,1,11,1,15),_Hm2DlrGatewayConfigRowStatus_Type())
hm2DlrGatewayConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DlrGatewayConfigRowStatus.setStatus(_A)
_Hm2DlrStatus_ObjectIdentity=ObjectIdentity
hm2DlrStatus=_Hm2DlrStatus_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,5,1,2))
_Hm2DlrStatusTable_Object=MibTable
hm2DlrStatusTable=_Hm2DlrStatusTable_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1))
if mibBuilder.loadTexts:hm2DlrStatusTable.setStatus(_A)
_Hm2DlrStatusEntry_Object=MibTableRow
hm2DlrStatusEntry=_Hm2DlrStatusEntry_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1))
hm2DlrStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hm2DlrStatusEntry.setStatus(_A)
class _Hm2DlrCapabilityFlags_Type(Bits):defaultBinValue='01';namedValues=NamedValues(*(('announce',0),('beacon',1),(_R,5),('gateway',6),('flushTable',7)))
_Hm2DlrCapabilityFlags_Type.__name__='Bits'
_Hm2DlrCapabilityFlags_Object=MibTableColumn
hm2DlrCapabilityFlags=_Hm2DlrCapabilityFlags_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,1),_Hm2DlrCapabilityFlags_Type())
hm2DlrCapabilityFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrCapabilityFlags.setStatus(_A)
class _Hm2DlrDeviceOperStatus_Type(Hm2DlrRingDeviceStatusType):defaultValue=2
_Hm2DlrDeviceOperStatus_Type.__name__=_T
_Hm2DlrDeviceOperStatus_Object=MibTableColumn
hm2DlrDeviceOperStatus=_Hm2DlrDeviceOperStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,2),_Hm2DlrDeviceOperStatus_Type())
hm2DlrDeviceOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrDeviceOperStatus.setStatus(_A)
class _Hm2DlrNetworkTopology_Type(Hm2DlrNetworkTopologyType):defaultValue=1
_Hm2DlrNetworkTopology_Type.__name__=_U
_Hm2DlrNetworkTopology_Object=MibTableColumn
hm2DlrNetworkTopology=_Hm2DlrNetworkTopology_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,3),_Hm2DlrNetworkTopology_Type())
hm2DlrNetworkTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrNetworkTopology.setStatus(_A)
class _Hm2DlrNetworkStatus_Type(Hm2DlrNetworkStatusType):defaultValue=0
_Hm2DlrNetworkStatus_Type.__name__=_V
_Hm2DlrNetworkStatus_Object=MibTableColumn
hm2DlrNetworkStatus=_Hm2DlrNetworkStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,4),_Hm2DlrNetworkStatus_Type())
hm2DlrNetworkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrNetworkStatus.setStatus(_A)
class _Hm2DlrLastNetworkStatusChange_Type(Hm2DlrTimeInterval):defaultValue=0
_Hm2DlrLastNetworkStatusChange_Type.__name__=_W
_Hm2DlrLastNetworkStatusChange_Object=MibTableColumn
hm2DlrLastNetworkStatusChange=_Hm2DlrLastNetworkStatusChange_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,5),_Hm2DlrLastNetworkStatusChange_Type())
hm2DlrLastNetworkStatusChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrLastNetworkStatusChange.setStatus(_A)
if mibBuilder.loadTexts:hm2DlrLastNetworkStatusChange.setUnits('seconds')
class _Hm2DlrRingParticipantsCount_Type(Unsigned32):defaultValue=0
_Hm2DlrRingParticipantsCount_Type.__name__=_D
_Hm2DlrRingParticipantsCount_Object=MibTableColumn
hm2DlrRingParticipantsCount=_Hm2DlrRingParticipantsCount_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,6),_Hm2DlrRingParticipantsCount_Type())
hm2DlrRingParticipantsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrRingParticipantsCount.setStatus(_A)
class _Hm2DlrActiveSupervisorIpAddressType_Type(InetAddressType):defaultValue=1
_Hm2DlrActiveSupervisorIpAddressType_Type.__name__=_G
_Hm2DlrActiveSupervisorIpAddressType_Object=MibTableColumn
hm2DlrActiveSupervisorIpAddressType=_Hm2DlrActiveSupervisorIpAddressType_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,7),_Hm2DlrActiveSupervisorIpAddressType_Type())
hm2DlrActiveSupervisorIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrActiveSupervisorIpAddressType.setStatus(_A)
class _Hm2DlrActiveSupervisorIpAddress_Type(InetAddress):defaultHexValue=_K
_Hm2DlrActiveSupervisorIpAddress_Type.__name__=_H
_Hm2DlrActiveSupervisorIpAddress_Object=MibTableColumn
hm2DlrActiveSupervisorIpAddress=_Hm2DlrActiveSupervisorIpAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,8),_Hm2DlrActiveSupervisorIpAddress_Type())
hm2DlrActiveSupervisorIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrActiveSupervisorIpAddress.setStatus(_A)
class _Hm2DlrActiveSupervisorMacAddress_Type(MacAddress):defaultHexValue=_L
_Hm2DlrActiveSupervisorMacAddress_Type.__name__=_I
_Hm2DlrActiveSupervisorMacAddress_Object=MibTableColumn
hm2DlrActiveSupervisorMacAddress=_Hm2DlrActiveSupervisorMacAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,9),_Hm2DlrActiveSupervisorMacAddress_Type())
hm2DlrActiveSupervisorMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrActiveSupervisorMacAddress.setStatus(_A)
class _Hm2DlrActiveSupervisorPrecedence_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2DlrActiveSupervisorPrecedence_Type.__name__=_D
_Hm2DlrActiveSupervisorPrecedence_Object=MibTableColumn
hm2DlrActiveSupervisorPrecedence=_Hm2DlrActiveSupervisorPrecedence_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,10),_Hm2DlrActiveSupervisorPrecedence_Type())
hm2DlrActiveSupervisorPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrActiveSupervisorPrecedence.setStatus(_A)
class _Hm2DlrRingFaultsCount_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2DlrRingFaultsCount_Type.__name__=_D
_Hm2DlrRingFaultsCount_Object=MibTableColumn
hm2DlrRingFaultsCount=_Hm2DlrRingFaultsCount_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,11),_Hm2DlrRingFaultsCount_Type())
hm2DlrRingFaultsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrRingFaultsCount.setStatus(_A)
class _Hm2DlrLastActiveNodePort1IpAddressType_Type(InetAddressType):defaultValue=1
_Hm2DlrLastActiveNodePort1IpAddressType_Type.__name__=_G
_Hm2DlrLastActiveNodePort1IpAddressType_Object=MibTableColumn
hm2DlrLastActiveNodePort1IpAddressType=_Hm2DlrLastActiveNodePort1IpAddressType_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,12),_Hm2DlrLastActiveNodePort1IpAddressType_Type())
hm2DlrLastActiveNodePort1IpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrLastActiveNodePort1IpAddressType.setStatus(_A)
class _Hm2DlrLastActiveNodePort1IpAddress_Type(InetAddress):defaultHexValue=_K
_Hm2DlrLastActiveNodePort1IpAddress_Type.__name__=_H
_Hm2DlrLastActiveNodePort1IpAddress_Object=MibTableColumn
hm2DlrLastActiveNodePort1IpAddress=_Hm2DlrLastActiveNodePort1IpAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,13),_Hm2DlrLastActiveNodePort1IpAddress_Type())
hm2DlrLastActiveNodePort1IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrLastActiveNodePort1IpAddress.setStatus(_A)
class _Hm2DlrLastActiveNodePort1MacAddress_Type(MacAddress):defaultHexValue=_L
_Hm2DlrLastActiveNodePort1MacAddress_Type.__name__=_I
_Hm2DlrLastActiveNodePort1MacAddress_Object=MibTableColumn
hm2DlrLastActiveNodePort1MacAddress=_Hm2DlrLastActiveNodePort1MacAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,14),_Hm2DlrLastActiveNodePort1MacAddress_Type())
hm2DlrLastActiveNodePort1MacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrLastActiveNodePort1MacAddress.setStatus(_A)
class _Hm2DlrLastActiveNodePort2IpAddressType_Type(InetAddressType):defaultValue=1
_Hm2DlrLastActiveNodePort2IpAddressType_Type.__name__=_G
_Hm2DlrLastActiveNodePort2IpAddressType_Object=MibTableColumn
hm2DlrLastActiveNodePort2IpAddressType=_Hm2DlrLastActiveNodePort2IpAddressType_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,15),_Hm2DlrLastActiveNodePort2IpAddressType_Type())
hm2DlrLastActiveNodePort2IpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrLastActiveNodePort2IpAddressType.setStatus(_A)
class _Hm2DlrLastActiveNodePort2IpAddress_Type(InetAddress):defaultHexValue=_K
_Hm2DlrLastActiveNodePort2IpAddress_Type.__name__=_H
_Hm2DlrLastActiveNodePort2IpAddress_Object=MibTableColumn
hm2DlrLastActiveNodePort2IpAddress=_Hm2DlrLastActiveNodePort2IpAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,16),_Hm2DlrLastActiveNodePort2IpAddress_Type())
hm2DlrLastActiveNodePort2IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrLastActiveNodePort2IpAddress.setStatus(_A)
class _Hm2DlrLastActiveNodePort2MacAddress_Type(MacAddress):defaultHexValue=_L
_Hm2DlrLastActiveNodePort2MacAddress_Type.__name__=_I
_Hm2DlrLastActiveNodePort2MacAddress_Object=MibTableColumn
hm2DlrLastActiveNodePort2MacAddress=_Hm2DlrLastActiveNodePort2MacAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,1,1,17),_Hm2DlrLastActiveNodePort2MacAddress_Type())
hm2DlrLastActiveNodePort2MacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrLastActiveNodePort2MacAddress.setStatus(_A)
_Hm2DlrRingParticipantsTable_Object=MibTable
hm2DlrRingParticipantsTable=_Hm2DlrRingParticipantsTable_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,2))
if mibBuilder.loadTexts:hm2DlrRingParticipantsTable.setStatus(_A)
_Hm2DlrRingParticipantsEntry_Object=MibTableRow
hm2DlrRingParticipantsEntry=_Hm2DlrRingParticipantsEntry_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,2,1))
hm2DlrRingParticipantsEntry.setIndexNames((0,_E,_F),(0,_E,_X))
if mibBuilder.loadTexts:hm2DlrRingParticipantsEntry.setStatus(_A)
_Hm2DlrRingParticipantsIndex_Type=Unsigned32
_Hm2DlrRingParticipantsIndex_Object=MibTableColumn
hm2DlrRingParticipantsIndex=_Hm2DlrRingParticipantsIndex_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,2,1,1),_Hm2DlrRingParticipantsIndex_Type())
hm2DlrRingParticipantsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hm2DlrRingParticipantsIndex.setStatus(_A)
class _Hm2DlrRingParticipantsIpAddressType_Type(InetAddressType):defaultValue=1
_Hm2DlrRingParticipantsIpAddressType_Type.__name__=_G
_Hm2DlrRingParticipantsIpAddressType_Object=MibTableColumn
hm2DlrRingParticipantsIpAddressType=_Hm2DlrRingParticipantsIpAddressType_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,2,1,2),_Hm2DlrRingParticipantsIpAddressType_Type())
hm2DlrRingParticipantsIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrRingParticipantsIpAddressType.setStatus(_A)
_Hm2DlrRingParticipantsIpAddress_Type=InetAddress
_Hm2DlrRingParticipantsIpAddress_Object=MibTableColumn
hm2DlrRingParticipantsIpAddress=_Hm2DlrRingParticipantsIpAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,2,1,3),_Hm2DlrRingParticipantsIpAddress_Type())
hm2DlrRingParticipantsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrRingParticipantsIpAddress.setStatus(_A)
_Hm2DlrRingParticipantsMacAddress_Type=MacAddress
_Hm2DlrRingParticipantsMacAddress_Object=MibTableColumn
hm2DlrRingParticipantsMacAddress=_Hm2DlrRingParticipantsMacAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,2,1,4),_Hm2DlrRingParticipantsMacAddress_Type())
hm2DlrRingParticipantsMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrRingParticipantsMacAddress.setStatus(_A)
_Hm2DlrGatewayStatusTable_Object=MibTable
hm2DlrGatewayStatusTable=_Hm2DlrGatewayStatusTable_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,3))
if mibBuilder.loadTexts:hm2DlrGatewayStatusTable.setStatus(_A)
_Hm2DlrGatewayStatusEntry_Object=MibTableRow
hm2DlrGatewayStatusEntry=_Hm2DlrGatewayStatusEntry_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,3,1))
hm2DlrGatewayStatusEntry.setIndexNames((0,_E,_F),(0,_E,_N))
if mibBuilder.loadTexts:hm2DlrGatewayStatusEntry.setStatus(_A)
class _Hm2DlrGatewayStatus_Type(Hm2DlrGatewayStatusType):defaultValue=0
_Hm2DlrGatewayStatus_Type.__name__=_Y
_Hm2DlrGatewayStatus_Object=MibTableColumn
hm2DlrGatewayStatus=_Hm2DlrGatewayStatus_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,3,1,1),_Hm2DlrGatewayStatus_Type())
hm2DlrGatewayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrGatewayStatus.setStatus(_A)
class _Hm2DlrGatewayStatusPrecedence_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2DlrGatewayStatusPrecedence_Type.__name__=_D
_Hm2DlrGatewayStatusPrecedence_Object=MibTableColumn
hm2DlrGatewayStatusPrecedence=_Hm2DlrGatewayStatusPrecedence_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,3,1,2),_Hm2DlrGatewayStatusPrecedence_Type())
hm2DlrGatewayStatusPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrGatewayStatusPrecedence.setStatus(_A)
class _Hm2DlrGatewayStatusIpAddressType_Type(InetAddressType):defaultValue=1
_Hm2DlrGatewayStatusIpAddressType_Type.__name__=_G
_Hm2DlrGatewayStatusIpAddressType_Object=MibTableColumn
hm2DlrGatewayStatusIpAddressType=_Hm2DlrGatewayStatusIpAddressType_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,3,1,3),_Hm2DlrGatewayStatusIpAddressType_Type())
hm2DlrGatewayStatusIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrGatewayStatusIpAddressType.setStatus(_A)
class _Hm2DlrGatewayStatusIpAddress_Type(InetAddress):defaultHexValue=_K
_Hm2DlrGatewayStatusIpAddress_Type.__name__=_H
_Hm2DlrGatewayStatusIpAddress_Object=MibTableColumn
hm2DlrGatewayStatusIpAddress=_Hm2DlrGatewayStatusIpAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,3,1,4),_Hm2DlrGatewayStatusIpAddress_Type())
hm2DlrGatewayStatusIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrGatewayStatusIpAddress.setStatus(_A)
class _Hm2DlrGatewayStatusMacAddress_Type(MacAddress):defaultHexValue=_L
_Hm2DlrGatewayStatusMacAddress_Type.__name__=_I
_Hm2DlrGatewayStatusMacAddress_Object=MibTableColumn
hm2DlrGatewayStatusMacAddress=_Hm2DlrGatewayStatusMacAddress_Object((1,3,6,1,4,1,248,11,40,1,5,1,2,3,1,5),_Hm2DlrGatewayStatusMacAddress_Type())
hm2DlrGatewayStatusMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DlrGatewayStatusMacAddress.setStatus(_A)
hm2DlrRingStatusTrap=NotificationType((1,3,6,1,4,1,248,11,40,1,5,0,1))
hm2DlrRingStatusTrap.setObjects(*((_E,_F),(_E,_Z)))
if mibBuilder.loadTexts:hm2DlrRingStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_U:Hm2DlrNetworkTopologyType,_V:Hm2DlrNetworkStatusType,_Y:Hm2DlrGatewayStatusType,_T:Hm2DlrRingDeviceStatusType,'Hm2DlrPortStatusType':Hm2DlrPortStatusType,_W:Hm2DlrTimeInterval,'hm2DlrMibGroup':hm2DlrMibGroup,'hm2DlrMibNotifications':hm2DlrMibNotifications,'hm2DlrRingStatusTrap':hm2DlrRingStatusTrap,'hm2DlrMibObjects':hm2DlrMibObjects,'hm2DlrConfiguration':hm2DlrConfiguration,'hm2DlrGlobalAdminState':hm2DlrGlobalAdminState,'hm2DlrConfigTable':hm2DlrConfigTable,'hm2DlrConfigEntry':hm2DlrConfigEntry,_F:hm2DlrRingIndex,'hm2DlrRingName':hm2DlrRingName,'hm2DlrRingport1IfIndex':hm2DlrRingport1IfIndex,'hm2DlrRingport2IfIndex':hm2DlrRingport2IfIndex,'hm2DlrRingport1OperStatus':hm2DlrRingport1OperStatus,'hm2DlrRingport2OperStatus':hm2DlrRingport2OperStatus,'hm2DlrSupervisorAdminState':hm2DlrSupervisorAdminState,'hm2DlrSupervisorPrecedence':hm2DlrSupervisorPrecedence,'hm2DlrBeaconInterval':hm2DlrBeaconInterval,'hm2DlrBeaconTimeout':hm2DlrBeaconTimeout,'hm2DlrVLANID':hm2DlrVLANID,'hm2DlrService':hm2DlrService,'hm2DlrConfigRowStatus':hm2DlrConfigRowStatus,'hm2DlrGatewayConfigTable':hm2DlrGatewayConfigTable,'hm2DlrGatewayConfigEntry':hm2DlrGatewayConfigEntry,_N:hm2DlrGatewayIndex,'hm2DlrGatewayName':hm2DlrGatewayName,'hm2DlrGatewayConfigLearningUpdate':hm2DlrGatewayConfigLearningUpdate,'hm2DlrGatewayConfigPrecedence':hm2DlrGatewayConfigPrecedence,'hm2DlrGatewayConfigAdvertiseInterval':hm2DlrGatewayConfigAdvertiseInterval,'hm2DlrGatewayConfigAdvertiseTimeout':hm2DlrGatewayConfigAdvertiseTimeout,'hm2DlrGatewayConfigUplinkPort1IfIndex':hm2DlrGatewayConfigUplinkPort1IfIndex,'hm2DlrGatewayConfigUplinkPort2IfIndex':hm2DlrGatewayConfigUplinkPort2IfIndex,'hm2DlrGatewayUplinkPort1OperStatus':hm2DlrGatewayUplinkPort1OperStatus,'hm2DlrGatewayUplinkPort2OperStatus':hm2DlrGatewayUplinkPort2OperStatus,'hm2DlrGatewayConfigRowStatus':hm2DlrGatewayConfigRowStatus,'hm2DlrStatus':hm2DlrStatus,'hm2DlrStatusTable':hm2DlrStatusTable,'hm2DlrStatusEntry':hm2DlrStatusEntry,'hm2DlrCapabilityFlags':hm2DlrCapabilityFlags,'hm2DlrDeviceOperStatus':hm2DlrDeviceOperStatus,'hm2DlrNetworkTopology':hm2DlrNetworkTopology,_Z:hm2DlrNetworkStatus,'hm2DlrLastNetworkStatusChange':hm2DlrLastNetworkStatusChange,'hm2DlrRingParticipantsCount':hm2DlrRingParticipantsCount,'hm2DlrActiveSupervisorIpAddressType':hm2DlrActiveSupervisorIpAddressType,'hm2DlrActiveSupervisorIpAddress':hm2DlrActiveSupervisorIpAddress,'hm2DlrActiveSupervisorMacAddress':hm2DlrActiveSupervisorMacAddress,'hm2DlrActiveSupervisorPrecedence':hm2DlrActiveSupervisorPrecedence,'hm2DlrRingFaultsCount':hm2DlrRingFaultsCount,'hm2DlrLastActiveNodePort1IpAddressType':hm2DlrLastActiveNodePort1IpAddressType,'hm2DlrLastActiveNodePort1IpAddress':hm2DlrLastActiveNodePort1IpAddress,'hm2DlrLastActiveNodePort1MacAddress':hm2DlrLastActiveNodePort1MacAddress,'hm2DlrLastActiveNodePort2IpAddressType':hm2DlrLastActiveNodePort2IpAddressType,'hm2DlrLastActiveNodePort2IpAddress':hm2DlrLastActiveNodePort2IpAddress,'hm2DlrLastActiveNodePort2MacAddress':hm2DlrLastActiveNodePort2MacAddress,'hm2DlrRingParticipantsTable':hm2DlrRingParticipantsTable,'hm2DlrRingParticipantsEntry':hm2DlrRingParticipantsEntry,_X:hm2DlrRingParticipantsIndex,'hm2DlrRingParticipantsIpAddressType':hm2DlrRingParticipantsIpAddressType,'hm2DlrRingParticipantsIpAddress':hm2DlrRingParticipantsIpAddress,'hm2DlrRingParticipantsMacAddress':hm2DlrRingParticipantsMacAddress,'hm2DlrGatewayStatusTable':hm2DlrGatewayStatusTable,'hm2DlrGatewayStatusEntry':hm2DlrGatewayStatusEntry,'hm2DlrGatewayStatus':hm2DlrGatewayStatus,'hm2DlrGatewayStatusPrecedence':hm2DlrGatewayStatusPrecedence,'hm2DlrGatewayStatusIpAddressType':hm2DlrGatewayStatusIpAddressType,'hm2DlrGatewayStatusIpAddress':hm2DlrGatewayStatusIpAddress,'hm2DlrGatewayStatusMacAddress':hm2DlrGatewayStatusMacAddress})