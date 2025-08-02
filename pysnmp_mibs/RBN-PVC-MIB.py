_AK='rbnDot1qPvcOnFrGroup'
_AJ='rbnDot1qPvcOnAtmGroup'
_AI='rbnDot1qPvcOnEthGroup'
_AH='rbnFrameRelayPvcGroup'
_AG='rbnAtmPvcGroup'
_AF='rbnDot1qPvcOnFrClearCircuit'
_AE='rbnDot1qPvcOnFrCircuitHandle'
_AD='rbnDot1qPvcOnFrCircuitType'
_AC='rbnDot1qPvcOnFrEncapsulation'
_AB='rbnDot1qPvcOnFrProfileName'
_AA='rbnDot1qPvcOnFrRowStatus'
_A9='rbnDot1qPvcOnAtmClearCircuit'
_A8='rbnDot1qPvcOnAtmCircuitHandle'
_A7='rbnDot1qPvcOnAtmCircuitType'
_A6='rbnDot1qPvcOnAtmEncapsulation'
_A5='rbnDot1qPvcOnAtmProfileName'
_A4='rbnDot1qPvcOnAtmRowStatus'
_A3='rbnDot1qPvcOnEthClearCircuit'
_A2='rbnDot1qPvcOnEthCircuitHandle'
_A1='rbnDot1qPvcOnEthCircuitType'
_A0='rbnDot1qPvcOnEthEncapsulation'
_z='rbnDot1qPvcOnEthProfileName'
_y='rbnDot1qPvcOnEthRowStatus'
_x='rbnFrameRelayPvcClearCircuit'
_w='rbnFrameRelayPvcCircuitHandle'
_v='rbnFrameRelayPvcCircuitType'
_u='rbnAtmPvcClearCircuit'
_t='rbnAtmPvcCircuitHandle'
_s='rbnAtmPvcCircuitType'
_r='rbnDot1qPvcOnFrVlanId'
_q='rbnDot1qPvcOnFrDLCI'
_p='rbnDot1qPvcOnFrChannel'
_o='rbnDot1qPvcOnFrPort'
_n='rbnDot1qPvcOnFrSlot'
_m='rbnDot1qPvcOnAtmVlanId'
_l='rbnDot1qPvcOnAtmVci'
_k='rbnDot1qPvcOnAtmVpi'
_j='rbnDot1qPvcOnAtmPort'
_i='rbnDot1qPvcOnAtmSlot'
_h='rbnDot1qPvcOnEthVlanId'
_g='rbnDot1qPvcOnEthPort'
_f='rbnDot1qPvcOnEthSlot'
_e='rbnFrameRelayPvcDLCI'
_d='rbnFrameRelayPvcChannel'
_c='rbnFrameRelayPvcPort'
_b='rbnFrameRelayPvcSlot'
_a='rbnAtmPvcVci'
_Z='rbnAtmPvcVpi'
_Y='rbnAtmPvcPort'
_X='rbnAtmPvcSlot'
_W='unknown'
_V='pppAutoNopoe'
_U='pppAuto'
_T='l2tpVcMuxed'
_S='rbnFrameRelayPvcGroup2'
_R='rbnAtmPvcGroup2'
_Q='rbnFrameRelayPvcRowStatus'
_P='rbnFrameRelayPvcEncapsulation'
_O='rbnFrameRelayPvcProfileName'
_N='rbnAtmPvcRowStatus'
_M='rbnAtmPvcEncapsulation'
_L='rbnAtmPvcProfileName'
_K='pppOverEthernet'
_J='deprecated'
_I='read-only'
_H='TruthValue'
_G='RbnPvcCircuitType'
_F='SnmpAdminString'
_E='Unsigned32'
_D='not-accessible'
_C='read-create'
_B='RBN-PVC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnCircuitHandle,RbnPort,RbnSlot,RbnVidOrUntagged=mibBuilder.importSymbols('RBN-TC','RbnCircuitHandle','RbnPort','RbnSlot','RbnVidOrUntagged')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
rbnPvcMib=ModuleIdentity((1,3,6,1,4,1,2352,2,7))
if mibBuilder.loadTexts:rbnPvcMib.setRevisions(('2007-10-29 17:00','2004-05-21 17:00','2003-03-17 17:00','2002-12-20 17:00','2002-11-13 00:00','2002-05-23 17:00','2001-05-09 17:00','2001-02-10 17:00','2000-08-30 12:00'))
class RbnFrameRelayEncapsulation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('auto1490',1),('bridge1490',2),('multi1490',3),('route1490',4),('l2tp',5),(_T,6),('ppp',7),(_U,8),(_K,9),('dot1q1490',10),('clips1490',11),(_V,12)))
class RbnAtmEncapsulation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_W,0),('auto1483',1),('bridge1483',2),('multi1483',3),('route1483',4),('l2tp',5),(_T,6),('ppp',7),(_U,8),(_K,9),('pppSerial',10),('pppNlpid',11),('pppLlc',12),('pppVcMuxed',13),('raw',14),('dot1q1483',15),('clips1483',16),(_V,17),('cell',18)))
class RbnDot1qEncapsulation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_W,0),('ipOverEthernet',1),('dot1qMulti',2),(_K,3),('dot1qRaw',4),('dot1qClips',5),('dot1qTunnelMulti',6),('dot1qTunnelPppOverEthernet',7),('dot1qTunnelRaw',8),('dot1qTunnelClips',9)))
class RbnPvcCircuitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('explicit',1),('explicitRange',2),('onDemandRange',3),('protection',4)))
_RbnPvcMIBObjects_ObjectIdentity=ObjectIdentity
rbnPvcMIBObjects=_RbnPvcMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,7,1))
_RbnAtmPvcConfigTable_Object=MibTable
rbnAtmPvcConfigTable=_RbnAtmPvcConfigTable_Object((1,3,6,1,4,1,2352,2,7,1,1))
if mibBuilder.loadTexts:rbnAtmPvcConfigTable.setStatus(_A)
_RbnAtmPvcConfigEntry_Object=MibTableRow
rbnAtmPvcConfigEntry=_RbnAtmPvcConfigEntry_Object((1,3,6,1,4,1,2352,2,7,1,1,1))
rbnAtmPvcConfigEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:rbnAtmPvcConfigEntry.setStatus(_A)
_RbnAtmPvcSlot_Type=RbnSlot
_RbnAtmPvcSlot_Object=MibTableColumn
rbnAtmPvcSlot=_RbnAtmPvcSlot_Object((1,3,6,1,4,1,2352,2,7,1,1,1,1),_RbnAtmPvcSlot_Type())
rbnAtmPvcSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmPvcSlot.setStatus(_A)
_RbnAtmPvcPort_Type=RbnPort
_RbnAtmPvcPort_Object=MibTableColumn
rbnAtmPvcPort=_RbnAtmPvcPort_Object((1,3,6,1,4,1,2352,2,7,1,1,1,2),_RbnAtmPvcPort_Type())
rbnAtmPvcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmPvcPort.setStatus(_A)
class _RbnAtmPvcVpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RbnAtmPvcVpi_Type.__name__=_E
_RbnAtmPvcVpi_Object=MibTableColumn
rbnAtmPvcVpi=_RbnAtmPvcVpi_Object((1,3,6,1,4,1,2352,2,7,1,1,1,3),_RbnAtmPvcVpi_Type())
rbnAtmPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmPvcVpi.setStatus(_A)
class _RbnAtmPvcVci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RbnAtmPvcVci_Type.__name__=_E
_RbnAtmPvcVci_Object=MibTableColumn
rbnAtmPvcVci=_RbnAtmPvcVci_Object((1,3,6,1,4,1,2352,2,7,1,1,1,4),_RbnAtmPvcVci_Type())
rbnAtmPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmPvcVci.setStatus(_A)
class _RbnAtmPvcProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RbnAtmPvcProfileName_Type.__name__=_F
_RbnAtmPvcProfileName_Object=MibTableColumn
rbnAtmPvcProfileName=_RbnAtmPvcProfileName_Object((1,3,6,1,4,1,2352,2,7,1,1,1,5),_RbnAtmPvcProfileName_Type())
rbnAtmPvcProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmPvcProfileName.setStatus(_A)
_RbnAtmPvcEncapsulation_Type=RbnAtmEncapsulation
_RbnAtmPvcEncapsulation_Object=MibTableColumn
rbnAtmPvcEncapsulation=_RbnAtmPvcEncapsulation_Object((1,3,6,1,4,1,2352,2,7,1,1,1,6),_RbnAtmPvcEncapsulation_Type())
rbnAtmPvcEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmPvcEncapsulation.setStatus(_A)
_RbnAtmPvcRowStatus_Type=RowStatus
_RbnAtmPvcRowStatus_Object=MibTableColumn
rbnAtmPvcRowStatus=_RbnAtmPvcRowStatus_Object((1,3,6,1,4,1,2352,2,7,1,1,1,8),_RbnAtmPvcRowStatus_Type())
rbnAtmPvcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmPvcRowStatus.setStatus(_A)
class _RbnAtmPvcCircuitType_Type(RbnPvcCircuitType):defaultValue=1
_RbnAtmPvcCircuitType_Type.__name__=_G
_RbnAtmPvcCircuitType_Object=MibTableColumn
rbnAtmPvcCircuitType=_RbnAtmPvcCircuitType_Object((1,3,6,1,4,1,2352,2,7,1,1,1,9),_RbnAtmPvcCircuitType_Type())
rbnAtmPvcCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmPvcCircuitType.setStatus(_A)
_RbnAtmPvcCircuitHandle_Type=RbnCircuitHandle
_RbnAtmPvcCircuitHandle_Object=MibTableColumn
rbnAtmPvcCircuitHandle=_RbnAtmPvcCircuitHandle_Object((1,3,6,1,4,1,2352,2,7,1,1,1,10),_RbnAtmPvcCircuitHandle_Type())
rbnAtmPvcCircuitHandle.setMaxAccess(_I)
if mibBuilder.loadTexts:rbnAtmPvcCircuitHandle.setStatus(_A)
class _RbnAtmPvcClearCircuit_Type(TruthValue):defaultValue=2
_RbnAtmPvcClearCircuit_Type.__name__=_H
_RbnAtmPvcClearCircuit_Object=MibTableColumn
rbnAtmPvcClearCircuit=_RbnAtmPvcClearCircuit_Object((1,3,6,1,4,1,2352,2,7,1,1,1,11),_RbnAtmPvcClearCircuit_Type())
rbnAtmPvcClearCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmPvcClearCircuit.setStatus(_A)
_RbnFrameRelayPvcConfigTable_Object=MibTable
rbnFrameRelayPvcConfigTable=_RbnFrameRelayPvcConfigTable_Object((1,3,6,1,4,1,2352,2,7,1,2))
if mibBuilder.loadTexts:rbnFrameRelayPvcConfigTable.setStatus(_A)
_RbnFrameRelayPvcConfigEntry_Object=MibTableRow
rbnFrameRelayPvcConfigEntry=_RbnFrameRelayPvcConfigEntry_Object((1,3,6,1,4,1,2352,2,7,1,2,1))
rbnFrameRelayPvcConfigEntry.setIndexNames((0,_B,_b),(0,_B,_c),(0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:rbnFrameRelayPvcConfigEntry.setStatus(_A)
_RbnFrameRelayPvcSlot_Type=RbnSlot
_RbnFrameRelayPvcSlot_Object=MibTableColumn
rbnFrameRelayPvcSlot=_RbnFrameRelayPvcSlot_Object((1,3,6,1,4,1,2352,2,7,1,2,1,1),_RbnFrameRelayPvcSlot_Type())
rbnFrameRelayPvcSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnFrameRelayPvcSlot.setStatus(_A)
_RbnFrameRelayPvcPort_Type=RbnPort
_RbnFrameRelayPvcPort_Object=MibTableColumn
rbnFrameRelayPvcPort=_RbnFrameRelayPvcPort_Object((1,3,6,1,4,1,2352,2,7,1,2,1,2),_RbnFrameRelayPvcPort_Type())
rbnFrameRelayPvcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnFrameRelayPvcPort.setStatus(_A)
class _RbnFrameRelayPvcChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RbnFrameRelayPvcChannel_Type.__name__=_E
_RbnFrameRelayPvcChannel_Object=MibTableColumn
rbnFrameRelayPvcChannel=_RbnFrameRelayPvcChannel_Object((1,3,6,1,4,1,2352,2,7,1,2,1,3),_RbnFrameRelayPvcChannel_Type())
rbnFrameRelayPvcChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnFrameRelayPvcChannel.setStatus(_A)
class _RbnFrameRelayPvcDLCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RbnFrameRelayPvcDLCI_Type.__name__=_E
_RbnFrameRelayPvcDLCI_Object=MibTableColumn
rbnFrameRelayPvcDLCI=_RbnFrameRelayPvcDLCI_Object((1,3,6,1,4,1,2352,2,7,1,2,1,4),_RbnFrameRelayPvcDLCI_Type())
rbnFrameRelayPvcDLCI.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnFrameRelayPvcDLCI.setStatus(_A)
class _RbnFrameRelayPvcProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RbnFrameRelayPvcProfileName_Type.__name__=_F
_RbnFrameRelayPvcProfileName_Object=MibTableColumn
rbnFrameRelayPvcProfileName=_RbnFrameRelayPvcProfileName_Object((1,3,6,1,4,1,2352,2,7,1,2,1,5),_RbnFrameRelayPvcProfileName_Type())
rbnFrameRelayPvcProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFrameRelayPvcProfileName.setStatus(_A)
_RbnFrameRelayPvcEncapsulation_Type=RbnFrameRelayEncapsulation
_RbnFrameRelayPvcEncapsulation_Object=MibTableColumn
rbnFrameRelayPvcEncapsulation=_RbnFrameRelayPvcEncapsulation_Object((1,3,6,1,4,1,2352,2,7,1,2,1,6),_RbnFrameRelayPvcEncapsulation_Type())
rbnFrameRelayPvcEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFrameRelayPvcEncapsulation.setStatus(_A)
_RbnFrameRelayPvcRowStatus_Type=RowStatus
_RbnFrameRelayPvcRowStatus_Object=MibTableColumn
rbnFrameRelayPvcRowStatus=_RbnFrameRelayPvcRowStatus_Object((1,3,6,1,4,1,2352,2,7,1,2,1,8),_RbnFrameRelayPvcRowStatus_Type())
rbnFrameRelayPvcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFrameRelayPvcRowStatus.setStatus(_A)
class _RbnFrameRelayPvcCircuitType_Type(RbnPvcCircuitType):defaultValue=1
_RbnFrameRelayPvcCircuitType_Type.__name__=_G
_RbnFrameRelayPvcCircuitType_Object=MibTableColumn
rbnFrameRelayPvcCircuitType=_RbnFrameRelayPvcCircuitType_Object((1,3,6,1,4,1,2352,2,7,1,2,1,9),_RbnFrameRelayPvcCircuitType_Type())
rbnFrameRelayPvcCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFrameRelayPvcCircuitType.setStatus(_A)
_RbnFrameRelayPvcCircuitHandle_Type=RbnCircuitHandle
_RbnFrameRelayPvcCircuitHandle_Object=MibTableColumn
rbnFrameRelayPvcCircuitHandle=_RbnFrameRelayPvcCircuitHandle_Object((1,3,6,1,4,1,2352,2,7,1,2,1,10),_RbnFrameRelayPvcCircuitHandle_Type())
rbnFrameRelayPvcCircuitHandle.setMaxAccess(_I)
if mibBuilder.loadTexts:rbnFrameRelayPvcCircuitHandle.setStatus(_A)
_RbnFrameRelayPvcClearCircuit_Type=TruthValue
_RbnFrameRelayPvcClearCircuit_Object=MibTableColumn
rbnFrameRelayPvcClearCircuit=_RbnFrameRelayPvcClearCircuit_Object((1,3,6,1,4,1,2352,2,7,1,2,1,11),_RbnFrameRelayPvcClearCircuit_Type())
rbnFrameRelayPvcClearCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFrameRelayPvcClearCircuit.setStatus(_A)
_RbnDot1qPvcOnEthConfigTable_Object=MibTable
rbnDot1qPvcOnEthConfigTable=_RbnDot1qPvcOnEthConfigTable_Object((1,3,6,1,4,1,2352,2,7,1,3))
if mibBuilder.loadTexts:rbnDot1qPvcOnEthConfigTable.setStatus(_A)
_RbnDot1qPvcOnEthConfigEntry_Object=MibTableRow
rbnDot1qPvcOnEthConfigEntry=_RbnDot1qPvcOnEthConfigEntry_Object((1,3,6,1,4,1,2352,2,7,1,3,1))
rbnDot1qPvcOnEthConfigEntry.setIndexNames((0,_B,_f),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:rbnDot1qPvcOnEthConfigEntry.setStatus(_A)
_RbnDot1qPvcOnEthSlot_Type=RbnSlot
_RbnDot1qPvcOnEthSlot_Object=MibTableColumn
rbnDot1qPvcOnEthSlot=_RbnDot1qPvcOnEthSlot_Object((1,3,6,1,4,1,2352,2,7,1,3,1,1),_RbnDot1qPvcOnEthSlot_Type())
rbnDot1qPvcOnEthSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthSlot.setStatus(_A)
_RbnDot1qPvcOnEthPort_Type=RbnPort
_RbnDot1qPvcOnEthPort_Object=MibTableColumn
rbnDot1qPvcOnEthPort=_RbnDot1qPvcOnEthPort_Object((1,3,6,1,4,1,2352,2,7,1,3,1,2),_RbnDot1qPvcOnEthPort_Type())
rbnDot1qPvcOnEthPort.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthPort.setStatus(_A)
_RbnDot1qPvcOnEthVlanId_Type=RbnVidOrUntagged
_RbnDot1qPvcOnEthVlanId_Object=MibTableColumn
rbnDot1qPvcOnEthVlanId=_RbnDot1qPvcOnEthVlanId_Object((1,3,6,1,4,1,2352,2,7,1,3,1,3),_RbnDot1qPvcOnEthVlanId_Type())
rbnDot1qPvcOnEthVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthVlanId.setStatus(_A)
_RbnDot1qPvcOnEthRowStatus_Type=RowStatus
_RbnDot1qPvcOnEthRowStatus_Object=MibTableColumn
rbnDot1qPvcOnEthRowStatus=_RbnDot1qPvcOnEthRowStatus_Object((1,3,6,1,4,1,2352,2,7,1,3,1,4),_RbnDot1qPvcOnEthRowStatus_Type())
rbnDot1qPvcOnEthRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthRowStatus.setStatus(_A)
class _RbnDot1qPvcOnEthProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RbnDot1qPvcOnEthProfileName_Type.__name__=_F
_RbnDot1qPvcOnEthProfileName_Object=MibTableColumn
rbnDot1qPvcOnEthProfileName=_RbnDot1qPvcOnEthProfileName_Object((1,3,6,1,4,1,2352,2,7,1,3,1,5),_RbnDot1qPvcOnEthProfileName_Type())
rbnDot1qPvcOnEthProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthProfileName.setStatus(_A)
_RbnDot1qPvcOnEthEncapsulation_Type=RbnDot1qEncapsulation
_RbnDot1qPvcOnEthEncapsulation_Object=MibTableColumn
rbnDot1qPvcOnEthEncapsulation=_RbnDot1qPvcOnEthEncapsulation_Object((1,3,6,1,4,1,2352,2,7,1,3,1,6),_RbnDot1qPvcOnEthEncapsulation_Type())
rbnDot1qPvcOnEthEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthEncapsulation.setStatus(_A)
class _RbnDot1qPvcOnEthCircuitType_Type(RbnPvcCircuitType):defaultValue=1
_RbnDot1qPvcOnEthCircuitType_Type.__name__=_G
_RbnDot1qPvcOnEthCircuitType_Object=MibTableColumn
rbnDot1qPvcOnEthCircuitType=_RbnDot1qPvcOnEthCircuitType_Object((1,3,6,1,4,1,2352,2,7,1,3,1,7),_RbnDot1qPvcOnEthCircuitType_Type())
rbnDot1qPvcOnEthCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthCircuitType.setStatus(_A)
_RbnDot1qPvcOnEthCircuitHandle_Type=RbnCircuitHandle
_RbnDot1qPvcOnEthCircuitHandle_Object=MibTableColumn
rbnDot1qPvcOnEthCircuitHandle=_RbnDot1qPvcOnEthCircuitHandle_Object((1,3,6,1,4,1,2352,2,7,1,3,1,8),_RbnDot1qPvcOnEthCircuitHandle_Type())
rbnDot1qPvcOnEthCircuitHandle.setMaxAccess(_I)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthCircuitHandle.setStatus(_A)
class _RbnDot1qPvcOnEthClearCircuit_Type(TruthValue):defaultValue=2
_RbnDot1qPvcOnEthClearCircuit_Type.__name__=_H
_RbnDot1qPvcOnEthClearCircuit_Object=MibTableColumn
rbnDot1qPvcOnEthClearCircuit=_RbnDot1qPvcOnEthClearCircuit_Object((1,3,6,1,4,1,2352,2,7,1,3,1,9),_RbnDot1qPvcOnEthClearCircuit_Type())
rbnDot1qPvcOnEthClearCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnEthClearCircuit.setStatus(_A)
_RbnDot1qPvcOnAtmConfigTable_Object=MibTable
rbnDot1qPvcOnAtmConfigTable=_RbnDot1qPvcOnAtmConfigTable_Object((1,3,6,1,4,1,2352,2,7,1,4))
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmConfigTable.setStatus(_A)
_RbnDot1qPvcOnAtmConfigEntry_Object=MibTableRow
rbnDot1qPvcOnAtmConfigEntry=_RbnDot1qPvcOnAtmConfigEntry_Object((1,3,6,1,4,1,2352,2,7,1,4,1))
rbnDot1qPvcOnAtmConfigEntry.setIndexNames((0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmConfigEntry.setStatus(_A)
_RbnDot1qPvcOnAtmSlot_Type=RbnSlot
_RbnDot1qPvcOnAtmSlot_Object=MibTableColumn
rbnDot1qPvcOnAtmSlot=_RbnDot1qPvcOnAtmSlot_Object((1,3,6,1,4,1,2352,2,7,1,4,1,1),_RbnDot1qPvcOnAtmSlot_Type())
rbnDot1qPvcOnAtmSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmSlot.setStatus(_A)
_RbnDot1qPvcOnAtmPort_Type=RbnPort
_RbnDot1qPvcOnAtmPort_Object=MibTableColumn
rbnDot1qPvcOnAtmPort=_RbnDot1qPvcOnAtmPort_Object((1,3,6,1,4,1,2352,2,7,1,4,1,2),_RbnDot1qPvcOnAtmPort_Type())
rbnDot1qPvcOnAtmPort.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmPort.setStatus(_A)
class _RbnDot1qPvcOnAtmVpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RbnDot1qPvcOnAtmVpi_Type.__name__=_E
_RbnDot1qPvcOnAtmVpi_Object=MibTableColumn
rbnDot1qPvcOnAtmVpi=_RbnDot1qPvcOnAtmVpi_Object((1,3,6,1,4,1,2352,2,7,1,4,1,3),_RbnDot1qPvcOnAtmVpi_Type())
rbnDot1qPvcOnAtmVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmVpi.setStatus(_A)
class _RbnDot1qPvcOnAtmVci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RbnDot1qPvcOnAtmVci_Type.__name__=_E
_RbnDot1qPvcOnAtmVci_Object=MibTableColumn
rbnDot1qPvcOnAtmVci=_RbnDot1qPvcOnAtmVci_Object((1,3,6,1,4,1,2352,2,7,1,4,1,4),_RbnDot1qPvcOnAtmVci_Type())
rbnDot1qPvcOnAtmVci.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmVci.setStatus(_A)
_RbnDot1qPvcOnAtmVlanId_Type=RbnVidOrUntagged
_RbnDot1qPvcOnAtmVlanId_Object=MibTableColumn
rbnDot1qPvcOnAtmVlanId=_RbnDot1qPvcOnAtmVlanId_Object((1,3,6,1,4,1,2352,2,7,1,4,1,5),_RbnDot1qPvcOnAtmVlanId_Type())
rbnDot1qPvcOnAtmVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmVlanId.setStatus(_A)
_RbnDot1qPvcOnAtmRowStatus_Type=RowStatus
_RbnDot1qPvcOnAtmRowStatus_Object=MibTableColumn
rbnDot1qPvcOnAtmRowStatus=_RbnDot1qPvcOnAtmRowStatus_Object((1,3,6,1,4,1,2352,2,7,1,4,1,6),_RbnDot1qPvcOnAtmRowStatus_Type())
rbnDot1qPvcOnAtmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmRowStatus.setStatus(_A)
class _RbnDot1qPvcOnAtmProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RbnDot1qPvcOnAtmProfileName_Type.__name__=_F
_RbnDot1qPvcOnAtmProfileName_Object=MibTableColumn
rbnDot1qPvcOnAtmProfileName=_RbnDot1qPvcOnAtmProfileName_Object((1,3,6,1,4,1,2352,2,7,1,4,1,7),_RbnDot1qPvcOnAtmProfileName_Type())
rbnDot1qPvcOnAtmProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmProfileName.setStatus(_A)
_RbnDot1qPvcOnAtmEncapsulation_Type=RbnDot1qEncapsulation
_RbnDot1qPvcOnAtmEncapsulation_Object=MibTableColumn
rbnDot1qPvcOnAtmEncapsulation=_RbnDot1qPvcOnAtmEncapsulation_Object((1,3,6,1,4,1,2352,2,7,1,4,1,8),_RbnDot1qPvcOnAtmEncapsulation_Type())
rbnDot1qPvcOnAtmEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmEncapsulation.setStatus(_A)
class _RbnDot1qPvcOnAtmCircuitType_Type(RbnPvcCircuitType):defaultValue=1
_RbnDot1qPvcOnAtmCircuitType_Type.__name__=_G
_RbnDot1qPvcOnAtmCircuitType_Object=MibTableColumn
rbnDot1qPvcOnAtmCircuitType=_RbnDot1qPvcOnAtmCircuitType_Object((1,3,6,1,4,1,2352,2,7,1,4,1,9),_RbnDot1qPvcOnAtmCircuitType_Type())
rbnDot1qPvcOnAtmCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmCircuitType.setStatus(_A)
_RbnDot1qPvcOnAtmCircuitHandle_Type=RbnCircuitHandle
_RbnDot1qPvcOnAtmCircuitHandle_Object=MibTableColumn
rbnDot1qPvcOnAtmCircuitHandle=_RbnDot1qPvcOnAtmCircuitHandle_Object((1,3,6,1,4,1,2352,2,7,1,4,1,10),_RbnDot1qPvcOnAtmCircuitHandle_Type())
rbnDot1qPvcOnAtmCircuitHandle.setMaxAccess(_I)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmCircuitHandle.setStatus(_A)
class _RbnDot1qPvcOnAtmClearCircuit_Type(TruthValue):defaultValue=2
_RbnDot1qPvcOnAtmClearCircuit_Type.__name__=_H
_RbnDot1qPvcOnAtmClearCircuit_Object=MibTableColumn
rbnDot1qPvcOnAtmClearCircuit=_RbnDot1qPvcOnAtmClearCircuit_Object((1,3,6,1,4,1,2352,2,7,1,4,1,11),_RbnDot1qPvcOnAtmClearCircuit_Type())
rbnDot1qPvcOnAtmClearCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmClearCircuit.setStatus(_A)
_RbnDot1qPvcOnFrConfigTable_Object=MibTable
rbnDot1qPvcOnFrConfigTable=_RbnDot1qPvcOnFrConfigTable_Object((1,3,6,1,4,1,2352,2,7,1,5))
if mibBuilder.loadTexts:rbnDot1qPvcOnFrConfigTable.setStatus(_A)
_RbnDot1qPvcOnFrConfigEntry_Object=MibTableRow
rbnDot1qPvcOnFrConfigEntry=_RbnDot1qPvcOnFrConfigEntry_Object((1,3,6,1,4,1,2352,2,7,1,5,1))
rbnDot1qPvcOnFrConfigEntry.setIndexNames((0,_B,_n),(0,_B,_o),(0,_B,_p),(0,_B,_q),(0,_B,_r))
if mibBuilder.loadTexts:rbnDot1qPvcOnFrConfigEntry.setStatus(_A)
_RbnDot1qPvcOnFrSlot_Type=RbnSlot
_RbnDot1qPvcOnFrSlot_Object=MibTableColumn
rbnDot1qPvcOnFrSlot=_RbnDot1qPvcOnFrSlot_Object((1,3,6,1,4,1,2352,2,7,1,5,1,1),_RbnDot1qPvcOnFrSlot_Type())
rbnDot1qPvcOnFrSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrSlot.setStatus(_A)
_RbnDot1qPvcOnFrPort_Type=RbnPort
_RbnDot1qPvcOnFrPort_Object=MibTableColumn
rbnDot1qPvcOnFrPort=_RbnDot1qPvcOnFrPort_Object((1,3,6,1,4,1,2352,2,7,1,5,1,2),_RbnDot1qPvcOnFrPort_Type())
rbnDot1qPvcOnFrPort.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrPort.setStatus(_A)
class _RbnDot1qPvcOnFrChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RbnDot1qPvcOnFrChannel_Type.__name__=_E
_RbnDot1qPvcOnFrChannel_Object=MibTableColumn
rbnDot1qPvcOnFrChannel=_RbnDot1qPvcOnFrChannel_Object((1,3,6,1,4,1,2352,2,7,1,5,1,3),_RbnDot1qPvcOnFrChannel_Type())
rbnDot1qPvcOnFrChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrChannel.setStatus(_A)
class _RbnDot1qPvcOnFrDLCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RbnDot1qPvcOnFrDLCI_Type.__name__=_E
_RbnDot1qPvcOnFrDLCI_Object=MibTableColumn
rbnDot1qPvcOnFrDLCI=_RbnDot1qPvcOnFrDLCI_Object((1,3,6,1,4,1,2352,2,7,1,5,1,4),_RbnDot1qPvcOnFrDLCI_Type())
rbnDot1qPvcOnFrDLCI.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrDLCI.setStatus(_A)
_RbnDot1qPvcOnFrVlanId_Type=RbnVidOrUntagged
_RbnDot1qPvcOnFrVlanId_Object=MibTableColumn
rbnDot1qPvcOnFrVlanId=_RbnDot1qPvcOnFrVlanId_Object((1,3,6,1,4,1,2352,2,7,1,5,1,5),_RbnDot1qPvcOnFrVlanId_Type())
rbnDot1qPvcOnFrVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrVlanId.setStatus(_A)
_RbnDot1qPvcOnFrRowStatus_Type=RowStatus
_RbnDot1qPvcOnFrRowStatus_Object=MibTableColumn
rbnDot1qPvcOnFrRowStatus=_RbnDot1qPvcOnFrRowStatus_Object((1,3,6,1,4,1,2352,2,7,1,5,1,6),_RbnDot1qPvcOnFrRowStatus_Type())
rbnDot1qPvcOnFrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrRowStatus.setStatus(_A)
class _RbnDot1qPvcOnFrProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RbnDot1qPvcOnFrProfileName_Type.__name__=_F
_RbnDot1qPvcOnFrProfileName_Object=MibTableColumn
rbnDot1qPvcOnFrProfileName=_RbnDot1qPvcOnFrProfileName_Object((1,3,6,1,4,1,2352,2,7,1,5,1,7),_RbnDot1qPvcOnFrProfileName_Type())
rbnDot1qPvcOnFrProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrProfileName.setStatus(_A)
_RbnDot1qPvcOnFrEncapsulation_Type=RbnDot1qEncapsulation
_RbnDot1qPvcOnFrEncapsulation_Object=MibTableColumn
rbnDot1qPvcOnFrEncapsulation=_RbnDot1qPvcOnFrEncapsulation_Object((1,3,6,1,4,1,2352,2,7,1,5,1,8),_RbnDot1qPvcOnFrEncapsulation_Type())
rbnDot1qPvcOnFrEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrEncapsulation.setStatus(_A)
class _RbnDot1qPvcOnFrCircuitType_Type(RbnPvcCircuitType):defaultValue=1
_RbnDot1qPvcOnFrCircuitType_Type.__name__=_G
_RbnDot1qPvcOnFrCircuitType_Object=MibTableColumn
rbnDot1qPvcOnFrCircuitType=_RbnDot1qPvcOnFrCircuitType_Object((1,3,6,1,4,1,2352,2,7,1,5,1,9),_RbnDot1qPvcOnFrCircuitType_Type())
rbnDot1qPvcOnFrCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrCircuitType.setStatus(_A)
_RbnDot1qPvcOnFrCircuitHandle_Type=RbnCircuitHandle
_RbnDot1qPvcOnFrCircuitHandle_Object=MibTableColumn
rbnDot1qPvcOnFrCircuitHandle=_RbnDot1qPvcOnFrCircuitHandle_Object((1,3,6,1,4,1,2352,2,7,1,5,1,10),_RbnDot1qPvcOnFrCircuitHandle_Type())
rbnDot1qPvcOnFrCircuitHandle.setMaxAccess(_I)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrCircuitHandle.setStatus(_A)
class _RbnDot1qPvcOnFrClearCircuit_Type(TruthValue):defaultValue=2
_RbnDot1qPvcOnFrClearCircuit_Type.__name__=_H
_RbnDot1qPvcOnFrClearCircuit_Object=MibTableColumn
rbnDot1qPvcOnFrClearCircuit=_RbnDot1qPvcOnFrClearCircuit_Object((1,3,6,1,4,1,2352,2,7,1,5,1,11),_RbnDot1qPvcOnFrClearCircuit_Type())
rbnDot1qPvcOnFrClearCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDot1qPvcOnFrClearCircuit.setStatus(_A)
_RbnPvcMIBConformance_ObjectIdentity=ObjectIdentity
rbnPvcMIBConformance=_RbnPvcMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,7,2))
_RbnPvcCompliances_ObjectIdentity=ObjectIdentity
rbnPvcCompliances=_RbnPvcCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,7,2,1))
_RbnPvcGroups_ObjectIdentity=ObjectIdentity
rbnPvcGroups=_RbnPvcGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,7,2,2))
_RbnPvcMIBNotifications_ObjectIdentity=ObjectIdentity
rbnPvcMIBNotifications=_RbnPvcMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,7,3))
rbnAtmPvcGroup=ObjectGroup((1,3,6,1,4,1,2352,2,7,2,2,1))
rbnAtmPvcGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:rbnAtmPvcGroup.setStatus(_J)
rbnFrameRelayPvcGroup=ObjectGroup((1,3,6,1,4,1,2352,2,7,2,2,2))
rbnFrameRelayPvcGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:rbnFrameRelayPvcGroup.setStatus(_J)
rbnAtmPvcGroup2=ObjectGroup((1,3,6,1,4,1,2352,2,7,2,2,3))
rbnAtmPvcGroup2.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:rbnAtmPvcGroup2.setStatus(_A)
rbnFrameRelayPvcGroup2=ObjectGroup((1,3,6,1,4,1,2352,2,7,2,2,4))
rbnFrameRelayPvcGroup2.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:rbnFrameRelayPvcGroup2.setStatus(_A)
rbnDot1qPvcOnEthGroup=ObjectGroup((1,3,6,1,4,1,2352,2,7,2,2,5))
rbnDot1qPvcOnEthGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:rbnDot1qPvcOnEthGroup.setStatus(_A)
rbnDot1qPvcOnAtmGroup=ObjectGroup((1,3,6,1,4,1,2352,2,7,2,2,6))
rbnDot1qPvcOnAtmGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:rbnDot1qPvcOnAtmGroup.setStatus(_A)
rbnDot1qPvcOnFrGroup=ObjectGroup((1,3,6,1,4,1,2352,2,7,2,2,7))
rbnDot1qPvcOnFrGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:rbnDot1qPvcOnFrGroup.setStatus(_A)
rbnPvcCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,7,2,1,1))
rbnPvcCompliance.setObjects(*((_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:rbnPvcCompliance.setStatus(_J)
rbnPvcCompliance2=ModuleCompliance((1,3,6,1,4,1,2352,2,7,2,1,2))
rbnPvcCompliance2.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:rbnPvcCompliance2.setStatus(_J)
rbnPvcCompliance3=ModuleCompliance((1,3,6,1,4,1,2352,2,7,2,1,3))
rbnPvcCompliance3.setObjects(*((_B,_R),(_B,_S),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:rbnPvcCompliance3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RbnFrameRelayEncapsulation':RbnFrameRelayEncapsulation,'RbnAtmEncapsulation':RbnAtmEncapsulation,'RbnDot1qEncapsulation':RbnDot1qEncapsulation,_G:RbnPvcCircuitType,'rbnPvcMib':rbnPvcMib,'rbnPvcMIBObjects':rbnPvcMIBObjects,'rbnAtmPvcConfigTable':rbnAtmPvcConfigTable,'rbnAtmPvcConfigEntry':rbnAtmPvcConfigEntry,_X:rbnAtmPvcSlot,_Y:rbnAtmPvcPort,_Z:rbnAtmPvcVpi,_a:rbnAtmPvcVci,_L:rbnAtmPvcProfileName,_M:rbnAtmPvcEncapsulation,_N:rbnAtmPvcRowStatus,_s:rbnAtmPvcCircuitType,_t:rbnAtmPvcCircuitHandle,_u:rbnAtmPvcClearCircuit,'rbnFrameRelayPvcConfigTable':rbnFrameRelayPvcConfigTable,'rbnFrameRelayPvcConfigEntry':rbnFrameRelayPvcConfigEntry,_b:rbnFrameRelayPvcSlot,_c:rbnFrameRelayPvcPort,_d:rbnFrameRelayPvcChannel,_e:rbnFrameRelayPvcDLCI,_O:rbnFrameRelayPvcProfileName,_P:rbnFrameRelayPvcEncapsulation,_Q:rbnFrameRelayPvcRowStatus,_v:rbnFrameRelayPvcCircuitType,_w:rbnFrameRelayPvcCircuitHandle,_x:rbnFrameRelayPvcClearCircuit,'rbnDot1qPvcOnEthConfigTable':rbnDot1qPvcOnEthConfigTable,'rbnDot1qPvcOnEthConfigEntry':rbnDot1qPvcOnEthConfigEntry,_f:rbnDot1qPvcOnEthSlot,_g:rbnDot1qPvcOnEthPort,_h:rbnDot1qPvcOnEthVlanId,_y:rbnDot1qPvcOnEthRowStatus,_z:rbnDot1qPvcOnEthProfileName,_A0:rbnDot1qPvcOnEthEncapsulation,_A1:rbnDot1qPvcOnEthCircuitType,_A2:rbnDot1qPvcOnEthCircuitHandle,_A3:rbnDot1qPvcOnEthClearCircuit,'rbnDot1qPvcOnAtmConfigTable':rbnDot1qPvcOnAtmConfigTable,'rbnDot1qPvcOnAtmConfigEntry':rbnDot1qPvcOnAtmConfigEntry,_i:rbnDot1qPvcOnAtmSlot,_j:rbnDot1qPvcOnAtmPort,_k:rbnDot1qPvcOnAtmVpi,_l:rbnDot1qPvcOnAtmVci,_m:rbnDot1qPvcOnAtmVlanId,_A4:rbnDot1qPvcOnAtmRowStatus,_A5:rbnDot1qPvcOnAtmProfileName,_A6:rbnDot1qPvcOnAtmEncapsulation,_A7:rbnDot1qPvcOnAtmCircuitType,_A8:rbnDot1qPvcOnAtmCircuitHandle,_A9:rbnDot1qPvcOnAtmClearCircuit,'rbnDot1qPvcOnFrConfigTable':rbnDot1qPvcOnFrConfigTable,'rbnDot1qPvcOnFrConfigEntry':rbnDot1qPvcOnFrConfigEntry,_n:rbnDot1qPvcOnFrSlot,_o:rbnDot1qPvcOnFrPort,_p:rbnDot1qPvcOnFrChannel,_q:rbnDot1qPvcOnFrDLCI,_r:rbnDot1qPvcOnFrVlanId,_AA:rbnDot1qPvcOnFrRowStatus,_AB:rbnDot1qPvcOnFrProfileName,_AC:rbnDot1qPvcOnFrEncapsulation,_AD:rbnDot1qPvcOnFrCircuitType,_AE:rbnDot1qPvcOnFrCircuitHandle,_AF:rbnDot1qPvcOnFrClearCircuit,'rbnPvcMIBConformance':rbnPvcMIBConformance,'rbnPvcCompliances':rbnPvcCompliances,'rbnPvcCompliance':rbnPvcCompliance,'rbnPvcCompliance2':rbnPvcCompliance2,'rbnPvcCompliance3':rbnPvcCompliance3,'rbnPvcGroups':rbnPvcGroups,_AG:rbnAtmPvcGroup,_AH:rbnFrameRelayPvcGroup,_R:rbnAtmPvcGroup2,_S:rbnFrameRelayPvcGroup2,_AI:rbnDot1qPvcOnEthGroup,_AJ:rbnDot1qPvcOnAtmGroup,_AK:rbnDot1qPvcOnFrGroup,'rbnPvcMIBNotifications':rbnPvcMIBNotifications})