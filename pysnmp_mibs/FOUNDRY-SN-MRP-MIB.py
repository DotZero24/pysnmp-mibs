_Q='tunnel'
_P='regular'
_O='blocking'
_N='forwarding'
_M='preforwarding'
_L='enabled'
_K='not-accessible'
_J='snMetroRingId'
_I='snMetroRingVLanId'
_H='2017-08-07 00:00'
_G='FOUNDRY-SN-MRP-MIB'
_F='disabled'
_E='read-write'
_D='other'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snMetroRing=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,29))
if mibBuilder.loadTexts:snMetroRing.setRevisions((_H,_H))
_SnMetroRingGlobalObjects_ObjectIdentity=ObjectIdentity
snMetroRingGlobalObjects=_SnMetroRingGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,29,1))
_SnMetroRingTableObjects_ObjectIdentity=ObjectIdentity
snMetroRingTableObjects=_SnMetroRingTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,29,2))
_SnMetroRingTable_Object=MibTable
snMetroRingTable=_SnMetroRingTable_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1))
if mibBuilder.loadTexts:snMetroRingTable.setStatus(_A)
_SnMetroRingEntry_Object=MibTableRow
snMetroRingEntry=_SnMetroRingEntry_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1))
snMetroRingEntry.setIndexNames((0,_G,_I),(0,_G,_J))
if mibBuilder.loadTexts:snMetroRingEntry.setStatus(_A)
_SnMetroRingVLanId_Type=Integer32
_SnMetroRingVLanId_Object=MibTableColumn
snMetroRingVLanId=_SnMetroRingVLanId_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,1),_SnMetroRingVLanId_Type())
snMetroRingVLanId.setMaxAccess(_K)
if mibBuilder.loadTexts:snMetroRingVLanId.setStatus(_A)
_SnMetroRingId_Type=Integer32
_SnMetroRingId_Object=MibTableColumn
snMetroRingId=_SnMetroRingId_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,2),_SnMetroRingId_Type())
snMetroRingId.setMaxAccess(_K)
if mibBuilder.loadTexts:snMetroRingId.setStatus(_A)
class _SnMetroRingConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_L,2),(_F,3)))
_SnMetroRingConfigState_Type.__name__=_C
_SnMetroRingConfigState_Object=MibTableColumn
snMetroRingConfigState=_SnMetroRingConfigState_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,3),_SnMetroRingConfigState_Type())
snMetroRingConfigState.setMaxAccess(_E)
if mibBuilder.loadTexts:snMetroRingConfigState.setStatus(_A)
class _SnMetroRingRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('master',2),('member',3)))
_SnMetroRingRole_Type.__name__=_C
_SnMetroRingRole_Object=MibTableColumn
snMetroRingRole=_SnMetroRingRole_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,4),_SnMetroRingRole_Type())
snMetroRingRole.setMaxAccess(_E)
if mibBuilder.loadTexts:snMetroRingRole.setStatus(_A)
_SnMetroRingHelloTime_Type=Integer32
_SnMetroRingHelloTime_Object=MibTableColumn
snMetroRingHelloTime=_SnMetroRingHelloTime_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,5),_SnMetroRingHelloTime_Type())
snMetroRingHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:snMetroRingHelloTime.setStatus(_A)
_SnMetroRingPreforwardingTime_Type=Integer32
_SnMetroRingPreforwardingTime_Object=MibTableColumn
snMetroRingPreforwardingTime=_SnMetroRingPreforwardingTime_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,6),_SnMetroRingPreforwardingTime_Type())
snMetroRingPreforwardingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:snMetroRingPreforwardingTime.setStatus(_A)
_SnMetroRingPort1_Type=InterfaceIndex
_SnMetroRingPort1_Object=MibTableColumn
snMetroRingPort1=_SnMetroRingPort1_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,7),_SnMetroRingPort1_Type())
snMetroRingPort1.setMaxAccess(_E)
if mibBuilder.loadTexts:snMetroRingPort1.setStatus(_A)
_SnMetroRingPort2_Type=InterfaceIndex
_SnMetroRingPort2_Object=MibTableColumn
snMetroRingPort2=_SnMetroRingPort2_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,8),_SnMetroRingPort2_Type())
snMetroRingPort2.setMaxAccess(_E)
if mibBuilder.loadTexts:snMetroRingPort2.setStatus(_A)
_SnMetroRingName_Type=DisplayString
_SnMetroRingName_Object=MibTableColumn
snMetroRingName=_SnMetroRingName_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,9),_SnMetroRingName_Type())
snMetroRingName.setMaxAccess(_E)
if mibBuilder.loadTexts:snMetroRingName.setStatus(_A)
class _SnMetroRingRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('valid',2),('delete',3),('create',4)))
_SnMetroRingRowStatus_Type.__name__=_C
_SnMetroRingRowStatus_Object=MibTableColumn
snMetroRingRowStatus=_SnMetroRingRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,10),_SnMetroRingRowStatus_Type())
snMetroRingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snMetroRingRowStatus.setStatus(_A)
class _SnMetroRingOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_L,2),(_F,3)))
_SnMetroRingOperState_Type.__name__=_C
_SnMetroRingOperState_Object=MibTableColumn
snMetroRingOperState=_SnMetroRingOperState_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,11),_SnMetroRingOperState_Type())
snMetroRingOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingOperState.setStatus(_A)
_SnMetroRingTopoGroupId_Type=Integer32
_SnMetroRingTopoGroupId_Object=MibTableColumn
snMetroRingTopoGroupId=_SnMetroRingTopoGroupId_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,12),_SnMetroRingTopoGroupId_Type())
snMetroRingTopoGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingTopoGroupId.setStatus(_A)
_SnMetroRingRHPTransmitted_Type=Counter32
_SnMetroRingRHPTransmitted_Object=MibTableColumn
snMetroRingRHPTransmitted=_SnMetroRingRHPTransmitted_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,13),_SnMetroRingRHPTransmitted_Type())
snMetroRingRHPTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingRHPTransmitted.setStatus(_A)
_SnMetroRingRHPReceived_Type=Counter32
_SnMetroRingRHPReceived_Object=MibTableColumn
snMetroRingRHPReceived=_SnMetroRingRHPReceived_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,14),_SnMetroRingRHPReceived_Type())
snMetroRingRHPReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingRHPReceived.setStatus(_A)
_SnMetroRingStateChanged_Type=Counter32
_SnMetroRingStateChanged_Object=MibTableColumn
snMetroRingStateChanged=_SnMetroRingStateChanged_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,15),_SnMetroRingStateChanged_Type())
snMetroRingStateChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingStateChanged.setStatus(_A)
_SnMetroRingTCRBPDUReceived_Type=Counter32
_SnMetroRingTCRBPDUReceived_Object=MibTableColumn
snMetroRingTCRBPDUReceived=_SnMetroRingTCRBPDUReceived_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,16),_SnMetroRingTCRBPDUReceived_Type())
snMetroRingTCRBPDUReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingTCRBPDUReceived.setStatus(_A)
_SnMetroRingPriPort_Type=InterfaceIndex
_SnMetroRingPriPort_Object=MibTableColumn
snMetroRingPriPort=_SnMetroRingPriPort_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,17),_SnMetroRingPriPort_Type())
snMetroRingPriPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingPriPort.setStatus(_A)
_SnMetroRingSecPort_Type=InterfaceIndex
_SnMetroRingSecPort_Object=MibTableColumn
snMetroRingSecPort=_SnMetroRingSecPort_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,18),_SnMetroRingSecPort_Type())
snMetroRingSecPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingSecPort.setStatus(_A)
class _SnMetroRingPriPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_M,2),(_N,3),(_O,4),(_F,5)))
_SnMetroRingPriPortState_Type.__name__=_C
_SnMetroRingPriPortState_Object=MibTableColumn
snMetroRingPriPortState=_SnMetroRingPriPortState_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,19),_SnMetroRingPriPortState_Type())
snMetroRingPriPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingPriPortState.setStatus(_A)
class _SnMetroRingSecPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_M,2),(_N,3),(_O,4),(_F,5)))
_SnMetroRingSecPortState_Type.__name__=_C
_SnMetroRingSecPortState_Object=MibTableColumn
snMetroRingSecPortState=_SnMetroRingSecPortState_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,20),_SnMetroRingSecPortState_Type())
snMetroRingSecPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingSecPortState.setStatus(_A)
class _SnMetroRingPriPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_P,2),(_Q,3)))
_SnMetroRingPriPortType_Type.__name__=_C
_SnMetroRingPriPortType_Object=MibTableColumn
snMetroRingPriPortType=_SnMetroRingPriPortType_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,21),_SnMetroRingPriPortType_Type())
snMetroRingPriPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingPriPortType.setStatus(_A)
class _SnMetroRingSecPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_P,2),(_Q,3)))
_SnMetroRingSecPortType_Type.__name__=_C
_SnMetroRingSecPortType_Object=MibTableColumn
snMetroRingSecPortType=_SnMetroRingSecPortType_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,22),_SnMetroRingSecPortType_Type())
snMetroRingSecPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingSecPortType.setStatus(_A)
_SnMetroRingPriPortActivePort_Type=InterfaceIndex
_SnMetroRingPriPortActivePort_Object=MibTableColumn
snMetroRingPriPortActivePort=_SnMetroRingPriPortActivePort_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,23),_SnMetroRingPriPortActivePort_Type())
snMetroRingPriPortActivePort.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingPriPortActivePort.setStatus(_A)
_SnMetroRingSecPortActivePort_Type=InterfaceIndex
_SnMetroRingSecPortActivePort_Object=MibTableColumn
snMetroRingSecPortActivePort=_SnMetroRingSecPortActivePort_Object((1,3,6,1,4,1,1991,1,1,3,29,2,1,1,24),_SnMetroRingSecPortActivePort_Type())
snMetroRingSecPortActivePort.setMaxAccess(_B)
if mibBuilder.loadTexts:snMetroRingSecPortActivePort.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'snMetroRing':snMetroRing,'snMetroRingGlobalObjects':snMetroRingGlobalObjects,'snMetroRingTableObjects':snMetroRingTableObjects,'snMetroRingTable':snMetroRingTable,'snMetroRingEntry':snMetroRingEntry,_I:snMetroRingVLanId,_J:snMetroRingId,'snMetroRingConfigState':snMetroRingConfigState,'snMetroRingRole':snMetroRingRole,'snMetroRingHelloTime':snMetroRingHelloTime,'snMetroRingPreforwardingTime':snMetroRingPreforwardingTime,'snMetroRingPort1':snMetroRingPort1,'snMetroRingPort2':snMetroRingPort2,'snMetroRingName':snMetroRingName,'snMetroRingRowStatus':snMetroRingRowStatus,'snMetroRingOperState':snMetroRingOperState,'snMetroRingTopoGroupId':snMetroRingTopoGroupId,'snMetroRingRHPTransmitted':snMetroRingRHPTransmitted,'snMetroRingRHPReceived':snMetroRingRHPReceived,'snMetroRingStateChanged':snMetroRingStateChanged,'snMetroRingTCRBPDUReceived':snMetroRingTCRBPDUReceived,'snMetroRingPriPort':snMetroRingPriPort,'snMetroRingSecPort':snMetroRingSecPort,'snMetroRingPriPortState':snMetroRingPriPortState,'snMetroRingSecPortState':snMetroRingSecPortState,'snMetroRingPriPortType':snMetroRingPriPortType,'snMetroRingSecPortType':snMetroRingSecPortType,'snMetroRingPriPortActivePort':snMetroRingPriPortActivePort,'snMetroRingSecPortActivePort':snMetroRingSecPortActivePort})