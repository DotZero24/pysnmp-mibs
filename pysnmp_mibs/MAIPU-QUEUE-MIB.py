_T='mpQATMstatQNumber'
_S='mpQFRstatQNumber'
_R='mpQIFstatQNumber'
_Q='cells'
_P='bytes'
_O='mpQATMCfgVCI'
_N='mpQATMCfgVPI'
_M='mpQFRCfgDLCI'
_L='weightedFair'
_K='custom'
_J='priority'
_I='fifo'
_H='Unsigned32'
_G='not-accessible'
_F='ifIndex'
_E='packets'
_D='Integer32'
_C='MAIPU-QUEUE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
maipuQueueMIB=ModuleIdentity((1,3,6,1,4,1,5651,6,2,3,3))
_Maipu_ObjectIdentity=ObjectIdentity
maipu=_Maipu_ObjectIdentity((1,3,6,1,4,1,5651))
_MpMgmt2_ObjectIdentity=ObjectIdentity
mpMgmt2=_MpMgmt2_ObjectIdentity((1,3,6,1,4,1,5651,6))
_MpRouterTech_ObjectIdentity=ObjectIdentity
mpRouterTech=_MpRouterTech_ObjectIdentity((1,3,6,1,4,1,5651,6,2))
_MpRtQoSv2_ObjectIdentity=ObjectIdentity
mpRtQoSv2=_MpRtQoSv2_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3))
_MaipuQueueObjects_ObjectIdentity=ObjectIdentity
maipuQueueObjects=_MaipuQueueObjects_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,3,1))
_MpQueueConfig_ObjectIdentity=ObjectIdentity
mpQueueConfig=_MpQueueConfig_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,3,1,1))
_MpQInterfaceCfgTable_Object=MibTable
mpQInterfaceCfgTable=_MpQInterfaceCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,1))
if mibBuilder.loadTexts:mpQInterfaceCfgTable.setStatus(_A)
_MpQInterfaceCfgEntry_Object=MibTableRow
mpQInterfaceCfgEntry=_MpQInterfaceCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,1,1))
mpQInterfaceCfgEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:mpQInterfaceCfgEntry.setStatus(_A)
class _MpQIFCfgQType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_MpQIFCfgQType_Type.__name__=_D
_MpQIFCfgQType_Object=MibTableColumn
mpQIFCfgQType=_MpQIFCfgQType_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,1,1,1),_MpQIFCfgQType_Type())
mpQIFCfgQType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQIFCfgQType.setStatus(_A)
_MpQIFCfgQueues_Type=Integer32
_MpQIFCfgQueues_Object=MibTableColumn
mpQIFCfgQueues=_MpQIFCfgQueues_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,1,1,2),_MpQIFCfgQueues_Type())
mpQIFCfgQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQIFCfgQueues.setStatus(_A)
_MpQFrameRelayVCCfgTable_Object=MibTable
mpQFrameRelayVCCfgTable=_MpQFrameRelayVCCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,2))
if mibBuilder.loadTexts:mpQFrameRelayVCCfgTable.setStatus(_A)
_MpQFrameRelayVCCfgEntry_Object=MibTableRow
mpQFrameRelayVCCfgEntry=_MpQFrameRelayVCCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,2,1))
mpQFrameRelayVCCfgEntry.setIndexNames((0,_C,_F),(0,_C,_M))
if mibBuilder.loadTexts:mpQFrameRelayVCCfgEntry.setStatus(_A)
class _MpQFRCfgDLCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1007))
_MpQFRCfgDLCI_Type.__name__=_H
_MpQFRCfgDLCI_Object=MibTableColumn
mpQFRCfgDLCI=_MpQFRCfgDLCI_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,2,1,1),_MpQFRCfgDLCI_Type())
mpQFRCfgDLCI.setMaxAccess(_G)
if mibBuilder.loadTexts:mpQFRCfgDLCI.setStatus(_A)
class _MpQFRCfgQType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_MpQFRCfgQType_Type.__name__=_D
_MpQFRCfgQType_Object=MibTableColumn
mpQFRCfgQType=_MpQFRCfgQType_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,2,1,2),_MpQFRCfgQType_Type())
mpQFRCfgQType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQFRCfgQType.setStatus(_A)
_MpQFRCfgQueues_Type=Integer32
_MpQFRCfgQueues_Object=MibTableColumn
mpQFRCfgQueues=_MpQFRCfgQueues_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,2,1,3),_MpQFRCfgQueues_Type())
mpQFRCfgQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQFRCfgQueues.setStatus(_A)
_MpQATMPVCCfgTable_Object=MibTable
mpQATMPVCCfgTable=_MpQATMPVCCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,3))
if mibBuilder.loadTexts:mpQATMPVCCfgTable.setStatus(_A)
_MpQATMPVCCfgEntry_Object=MibTableRow
mpQATMPVCCfgEntry=_MpQATMPVCCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,3,1))
mpQATMPVCCfgEntry.setIndexNames((0,_C,_F),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:mpQATMPVCCfgEntry.setStatus(_A)
class _MpQATMCfgVPI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpQATMCfgVPI_Type.__name__=_H
_MpQATMCfgVPI_Object=MibTableColumn
mpQATMCfgVPI=_MpQATMCfgVPI_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,3,1,1),_MpQATMCfgVPI_Type())
mpQATMCfgVPI.setMaxAccess(_G)
if mibBuilder.loadTexts:mpQATMCfgVPI.setStatus(_A)
class _MpQATMCfgVCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpQATMCfgVCI_Type.__name__=_H
_MpQATMCfgVCI_Object=MibTableColumn
mpQATMCfgVCI=_MpQATMCfgVCI_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,3,1,2),_MpQATMCfgVCI_Type())
mpQATMCfgVCI.setMaxAccess(_G)
if mibBuilder.loadTexts:mpQATMCfgVCI.setStatus(_A)
class _MpQATMCfgQType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_MpQATMCfgQType_Type.__name__=_D
_MpQATMCfgQType_Object=MibTableColumn
mpQATMCfgQType=_MpQATMCfgQType_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,3,1,3),_MpQATMCfgQType_Type())
mpQATMCfgQType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQATMCfgQType.setStatus(_A)
_MpQATMCfgQueues_Type=Integer32
_MpQATMCfgQueues_Object=MibTableColumn
mpQATMCfgQueues=_MpQATMCfgQueues_Object((1,3,6,1,4,1,5651,6,2,3,3,1,1,3,1,4),_MpQATMCfgQueues_Type())
mpQATMCfgQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQATMCfgQueues.setStatus(_A)
_MpQueueStats_ObjectIdentity=ObjectIdentity
mpQueueStats=_MpQueueStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,3,1,2))
_MpQInterfaceStatTable_Object=MibTable
mpQInterfaceStatTable=_MpQInterfaceStatTable_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,1))
if mibBuilder.loadTexts:mpQInterfaceStatTable.setStatus(_A)
_MpQInterfaceStatEntry_Object=MibTableRow
mpQInterfaceStatEntry=_MpQInterfaceStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,1,1))
mpQInterfaceStatEntry.setIndexNames((0,_C,_F),(0,_C,_R))
if mibBuilder.loadTexts:mpQInterfaceStatEntry.setStatus(_A)
class _MpQIFstatQNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MpQIFstatQNumber_Type.__name__=_D
_MpQIFstatQNumber_Object=MibTableColumn
mpQIFstatQNumber=_MpQIFstatQNumber_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,1,1,1),_MpQIFstatQNumber_Type())
mpQIFstatQNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:mpQIFstatQNumber.setStatus(_A)
class _MpQIFstatDepthUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_P,2),(_Q,3),('ms',4),('us',5)))
_MpQIFstatDepthUnit_Type.__name__=_D
_MpQIFstatDepthUnit_Object=MibTableColumn
mpQIFstatDepthUnit=_MpQIFstatDepthUnit_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,1,1,2),_MpQIFstatDepthUnit_Type())
mpQIFstatDepthUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQIFstatDepthUnit.setStatus(_A)
_MpQIFstatCurrentDepth_Type=Gauge32
_MpQIFstatCurrentDepth_Object=MibTableColumn
mpQIFstatCurrentDepth=_MpQIFstatCurrentDepth_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,1,1,3),_MpQIFstatCurrentDepth_Type())
mpQIFstatCurrentDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQIFstatCurrentDepth.setStatus(_A)
_MpQIFstatMaxDepth_Type=Integer32
_MpQIFstatMaxDepth_Object=MibTableColumn
mpQIFstatMaxDepth=_MpQIFstatMaxDepth_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,1,1,4),_MpQIFstatMaxDepth_Type())
mpQIFstatMaxDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQIFstatMaxDepth.setStatus(_A)
_MpQIFstatTransmitPkt64_Type=Counter64
_MpQIFstatTransmitPkt64_Object=MibTableColumn
mpQIFstatTransmitPkt64=_MpQIFstatTransmitPkt64_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,1,1,5),_MpQIFstatTransmitPkt64_Type())
mpQIFstatTransmitPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQIFstatTransmitPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpQIFstatTransmitPkt64.setUnits(_E)
_MpQIFstatDiscardPkt64_Type=Counter64
_MpQIFstatDiscardPkt64_Object=MibTableColumn
mpQIFstatDiscardPkt64=_MpQIFstatDiscardPkt64_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,1,1,6),_MpQIFstatDiscardPkt64_Type())
mpQIFstatDiscardPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQIFstatDiscardPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpQIFstatDiscardPkt64.setUnits(_E)
_MpQFrameRelayVCStatTable_Object=MibTable
mpQFrameRelayVCStatTable=_MpQFrameRelayVCStatTable_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,2))
if mibBuilder.loadTexts:mpQFrameRelayVCStatTable.setStatus(_A)
_MpQFrameRelayVCStatEntry_Object=MibTableRow
mpQFrameRelayVCStatEntry=_MpQFrameRelayVCStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,2,1))
mpQFrameRelayVCStatEntry.setIndexNames((0,_C,_F),(0,_C,_M),(0,_C,_S))
if mibBuilder.loadTexts:mpQFrameRelayVCStatEntry.setStatus(_A)
class _MpQFRstatQNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MpQFRstatQNumber_Type.__name__=_D
_MpQFRstatQNumber_Object=MibTableColumn
mpQFRstatQNumber=_MpQFRstatQNumber_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,2,1,1),_MpQFRstatQNumber_Type())
mpQFRstatQNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:mpQFRstatQNumber.setStatus(_A)
class _MpQFRstatDepthUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_P,2),(_Q,3),('ms',4),('us',5)))
_MpQFRstatDepthUnit_Type.__name__=_D
_MpQFRstatDepthUnit_Object=MibTableColumn
mpQFRstatDepthUnit=_MpQFRstatDepthUnit_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,2,1,2),_MpQFRstatDepthUnit_Type())
mpQFRstatDepthUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQFRstatDepthUnit.setStatus(_A)
_MpQFRstatCurrentDepth_Type=Gauge32
_MpQFRstatCurrentDepth_Object=MibTableColumn
mpQFRstatCurrentDepth=_MpQFRstatCurrentDepth_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,2,1,3),_MpQFRstatCurrentDepth_Type())
mpQFRstatCurrentDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQFRstatCurrentDepth.setStatus(_A)
_MpQFRstatMaxDepth_Type=Integer32
_MpQFRstatMaxDepth_Object=MibTableColumn
mpQFRstatMaxDepth=_MpQFRstatMaxDepth_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,2,1,4),_MpQFRstatMaxDepth_Type())
mpQFRstatMaxDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQFRstatMaxDepth.setStatus(_A)
_MpQFRstatTransmitPkt64_Type=Counter64
_MpQFRstatTransmitPkt64_Object=MibTableColumn
mpQFRstatTransmitPkt64=_MpQFRstatTransmitPkt64_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,2,1,5),_MpQFRstatTransmitPkt64_Type())
mpQFRstatTransmitPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQFRstatTransmitPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpQFRstatTransmitPkt64.setUnits(_E)
_MpQFRstatDiscardPkt64_Type=Counter64
_MpQFRstatDiscardPkt64_Object=MibTableColumn
mpQFRstatDiscardPkt64=_MpQFRstatDiscardPkt64_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,2,1,6),_MpQFRstatDiscardPkt64_Type())
mpQFRstatDiscardPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQFRstatDiscardPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpQFRstatDiscardPkt64.setUnits(_E)
_MpQATMPVCStatTable_Object=MibTable
mpQATMPVCStatTable=_MpQATMPVCStatTable_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,3))
if mibBuilder.loadTexts:mpQATMPVCStatTable.setStatus(_A)
_MpQATMPVCStatEntry_Object=MibTableRow
mpQATMPVCStatEntry=_MpQATMPVCStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,3,1))
mpQATMPVCStatEntry.setIndexNames((0,_C,_F),(0,_C,_N),(0,_C,_O),(0,_C,_T))
if mibBuilder.loadTexts:mpQATMPVCStatEntry.setStatus(_A)
class _MpQATMstatQNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MpQATMstatQNumber_Type.__name__=_D
_MpQATMstatQNumber_Object=MibTableColumn
mpQATMstatQNumber=_MpQATMstatQNumber_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,3,1,1),_MpQATMstatQNumber_Type())
mpQATMstatQNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:mpQATMstatQNumber.setStatus(_A)
class _MpQATMstatDepthUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_P,2),(_Q,3),('ms',4),('us',5)))
_MpQATMstatDepthUnit_Type.__name__=_D
_MpQATMstatDepthUnit_Object=MibTableColumn
mpQATMstatDepthUnit=_MpQATMstatDepthUnit_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,3,1,2),_MpQATMstatDepthUnit_Type())
mpQATMstatDepthUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQATMstatDepthUnit.setStatus(_A)
_MpQATMstatCurrentDepth_Type=Gauge32
_MpQATMstatCurrentDepth_Object=MibTableColumn
mpQATMstatCurrentDepth=_MpQATMstatCurrentDepth_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,3,1,3),_MpQATMstatCurrentDepth_Type())
mpQATMstatCurrentDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQATMstatCurrentDepth.setStatus(_A)
_MpQATMstatMaxDepth_Type=Integer32
_MpQATMstatMaxDepth_Object=MibTableColumn
mpQATMstatMaxDepth=_MpQATMstatMaxDepth_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,3,1,4),_MpQATMstatMaxDepth_Type())
mpQATMstatMaxDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQATMstatMaxDepth.setStatus(_A)
_MpQATMstatTransmitPkt64_Type=Counter64
_MpQATMstatTransmitPkt64_Object=MibTableColumn
mpQATMstatTransmitPkt64=_MpQATMstatTransmitPkt64_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,3,1,5),_MpQATMstatTransmitPkt64_Type())
mpQATMstatTransmitPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQATMstatTransmitPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpQATMstatTransmitPkt64.setUnits(_E)
_MpQATMstatDiscardPkt64_Type=Counter64
_MpQATMstatDiscardPkt64_Object=MibTableColumn
mpQATMstatDiscardPkt64=_MpQATMstatDiscardPkt64_Object((1,3,6,1,4,1,5651,6,2,3,3,1,2,3,1,6),_MpQATMstatDiscardPkt64_Type())
mpQATMstatDiscardPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpQATMstatDiscardPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpQATMstatDiscardPkt64.setUnits(_E)
mibBuilder.exportSymbols(_C,**{'maipu':maipu,'mpMgmt2':mpMgmt2,'mpRouterTech':mpRouterTech,'mpRtQoSv2':mpRtQoSv2,'maipuQueueMIB':maipuQueueMIB,'maipuQueueObjects':maipuQueueObjects,'mpQueueConfig':mpQueueConfig,'mpQInterfaceCfgTable':mpQInterfaceCfgTable,'mpQInterfaceCfgEntry':mpQInterfaceCfgEntry,'mpQIFCfgQType':mpQIFCfgQType,'mpQIFCfgQueues':mpQIFCfgQueues,'mpQFrameRelayVCCfgTable':mpQFrameRelayVCCfgTable,'mpQFrameRelayVCCfgEntry':mpQFrameRelayVCCfgEntry,_M:mpQFRCfgDLCI,'mpQFRCfgQType':mpQFRCfgQType,'mpQFRCfgQueues':mpQFRCfgQueues,'mpQATMPVCCfgTable':mpQATMPVCCfgTable,'mpQATMPVCCfgEntry':mpQATMPVCCfgEntry,_N:mpQATMCfgVPI,_O:mpQATMCfgVCI,'mpQATMCfgQType':mpQATMCfgQType,'mpQATMCfgQueues':mpQATMCfgQueues,'mpQueueStats':mpQueueStats,'mpQInterfaceStatTable':mpQInterfaceStatTable,'mpQInterfaceStatEntry':mpQInterfaceStatEntry,_R:mpQIFstatQNumber,'mpQIFstatDepthUnit':mpQIFstatDepthUnit,'mpQIFstatCurrentDepth':mpQIFstatCurrentDepth,'mpQIFstatMaxDepth':mpQIFstatMaxDepth,'mpQIFstatTransmitPkt64':mpQIFstatTransmitPkt64,'mpQIFstatDiscardPkt64':mpQIFstatDiscardPkt64,'mpQFrameRelayVCStatTable':mpQFrameRelayVCStatTable,'mpQFrameRelayVCStatEntry':mpQFrameRelayVCStatEntry,_S:mpQFRstatQNumber,'mpQFRstatDepthUnit':mpQFRstatDepthUnit,'mpQFRstatCurrentDepth':mpQFRstatCurrentDepth,'mpQFRstatMaxDepth':mpQFRstatMaxDepth,'mpQFRstatTransmitPkt64':mpQFRstatTransmitPkt64,'mpQFRstatDiscardPkt64':mpQFRstatDiscardPkt64,'mpQATMPVCStatTable':mpQATMPVCStatTable,'mpQATMPVCStatEntry':mpQATMPVCStatEntry,_T:mpQATMstatQNumber,'mpQATMstatDepthUnit':mpQATMstatDepthUnit,'mpQATMstatCurrentDepth':mpQATMstatCurrentDepth,'mpQATMstatMaxDepth':mpQATMstatMaxDepth,'mpQATMstatTransmitPkt64':mpQATMstatTransmitPkt64,'mpQATMstatDiscardPkt64':mpQATMstatDiscardPkt64})