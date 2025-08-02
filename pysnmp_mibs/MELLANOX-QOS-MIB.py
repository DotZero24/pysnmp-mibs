_L='mellanoxQoSPortIfIndex'
_K='mellanoxQoSTCIndex'
_J='mellanoxQoSTCIfIndex'
_I='mellanoxQoSPGIndex'
_H='mellanoxQoSPGIfIndex'
_G='mellanoxQoSPFCIndex'
_F='mellanoxQoSPFCIfIndex'
_E='mellanoxQoSPrioIndex'
_D='mellanoxQoSPrioIfIndex'
_C='MELLANOX-QOS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
mellanoxQoS,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxQoS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxQoSMib=ModuleIdentity((1,3,6,1,4,1,33049,15,1))
if mibBuilder.loadTexts:mellanoxQoSMib.setRevisions(('2017-07-26 00:00',))
_MellanoxQoSPrioTable_Object=MibTable
mellanoxQoSPrioTable=_MellanoxQoSPrioTable_Object((1,3,6,1,4,1,33049,15,1,1))
if mibBuilder.loadTexts:mellanoxQoSPrioTable.setStatus(_A)
_MellanoxQoSPrioEntry_Object=MibTableRow
mellanoxQoSPrioEntry=_MellanoxQoSPrioEntry_Object((1,3,6,1,4,1,33049,15,1,1,1))
mellanoxQoSPrioEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:mellanoxQoSPrioEntry.setStatus(_A)
_MellanoxQoSPrioIfIndex_Type=InterfaceIndex
_MellanoxQoSPrioIfIndex_Object=MibTableColumn
mellanoxQoSPrioIfIndex=_MellanoxQoSPrioIfIndex_Object((1,3,6,1,4,1,33049,15,1,1,1,1),_MellanoxQoSPrioIfIndex_Type())
mellanoxQoSPrioIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioIfIndex.setStatus(_A)
_MellanoxQoSPrioIndex_Type=Integer32
_MellanoxQoSPrioIndex_Object=MibTableColumn
mellanoxQoSPrioIndex=_MellanoxQoSPrioIndex_Object((1,3,6,1,4,1,33049,15,1,1,1,2),_MellanoxQoSPrioIndex_Type())
mellanoxQoSPrioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioIndex.setStatus(_A)
_MellanoxQoSPrioRxPkts_Type=Counter64
_MellanoxQoSPrioRxPkts_Object=MibTableColumn
mellanoxQoSPrioRxPkts=_MellanoxQoSPrioRxPkts_Object((1,3,6,1,4,1,33049,15,1,1,1,3),_MellanoxQoSPrioRxPkts_Type())
mellanoxQoSPrioRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioRxPkts.setStatus(_A)
_MellanoxQoSPrioRxUcastPkts_Type=Counter64
_MellanoxQoSPrioRxUcastPkts_Object=MibTableColumn
mellanoxQoSPrioRxUcastPkts=_MellanoxQoSPrioRxUcastPkts_Object((1,3,6,1,4,1,33049,15,1,1,1,4),_MellanoxQoSPrioRxUcastPkts_Type())
mellanoxQoSPrioRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioRxUcastPkts.setStatus(_A)
_MellanoxQoSPrioRxMcastPkts_Type=Counter64
_MellanoxQoSPrioRxMcastPkts_Object=MibTableColumn
mellanoxQoSPrioRxMcastPkts=_MellanoxQoSPrioRxMcastPkts_Object((1,3,6,1,4,1,33049,15,1,1,1,5),_MellanoxQoSPrioRxMcastPkts_Type())
mellanoxQoSPrioRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioRxMcastPkts.setStatus(_A)
_MellanoxQoSPrioRxBcastPkts_Type=Counter64
_MellanoxQoSPrioRxBcastPkts_Object=MibTableColumn
mellanoxQoSPrioRxBcastPkts=_MellanoxQoSPrioRxBcastPkts_Object((1,3,6,1,4,1,33049,15,1,1,1,6),_MellanoxQoSPrioRxBcastPkts_Type())
mellanoxQoSPrioRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioRxBcastPkts.setStatus(_A)
_MellanoxQoSPrioRxBytes_Type=Counter64
_MellanoxQoSPrioRxBytes_Object=MibTableColumn
mellanoxQoSPrioRxBytes=_MellanoxQoSPrioRxBytes_Object((1,3,6,1,4,1,33049,15,1,1,1,7),_MellanoxQoSPrioRxBytes_Type())
mellanoxQoSPrioRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioRxBytes.setStatus(_A)
_MellanoxQoSPrioRxPausePkts_Type=Counter64
_MellanoxQoSPrioRxPausePkts_Object=MibTableColumn
mellanoxQoSPrioRxPausePkts=_MellanoxQoSPrioRxPausePkts_Object((1,3,6,1,4,1,33049,15,1,1,1,8),_MellanoxQoSPrioRxPausePkts_Type())
mellanoxQoSPrioRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioRxPausePkts.setStatus(_A)
_MellanoxQoSPrioRxPauseDuration_Type=Counter64
_MellanoxQoSPrioRxPauseDuration_Object=MibTableColumn
mellanoxQoSPrioRxPauseDuration=_MellanoxQoSPrioRxPauseDuration_Object((1,3,6,1,4,1,33049,15,1,1,1,9),_MellanoxQoSPrioRxPauseDuration_Type())
mellanoxQoSPrioRxPauseDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioRxPauseDuration.setStatus(_A)
_MellanoxQoSPrioTxPkts_Type=Counter64
_MellanoxQoSPrioTxPkts_Object=MibTableColumn
mellanoxQoSPrioTxPkts=_MellanoxQoSPrioTxPkts_Object((1,3,6,1,4,1,33049,15,1,1,1,10),_MellanoxQoSPrioTxPkts_Type())
mellanoxQoSPrioTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioTxPkts.setStatus(_A)
_MellanoxQoSPrioTxUcastPkts_Type=Counter64
_MellanoxQoSPrioTxUcastPkts_Object=MibTableColumn
mellanoxQoSPrioTxUcastPkts=_MellanoxQoSPrioTxUcastPkts_Object((1,3,6,1,4,1,33049,15,1,1,1,11),_MellanoxQoSPrioTxUcastPkts_Type())
mellanoxQoSPrioTxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioTxUcastPkts.setStatus(_A)
_MellanoxQoSPrioTxMcastPkts_Type=Counter64
_MellanoxQoSPrioTxMcastPkts_Object=MibTableColumn
mellanoxQoSPrioTxMcastPkts=_MellanoxQoSPrioTxMcastPkts_Object((1,3,6,1,4,1,33049,15,1,1,1,12),_MellanoxQoSPrioTxMcastPkts_Type())
mellanoxQoSPrioTxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioTxMcastPkts.setStatus(_A)
_MellanoxQoSPrioTxBcastPkts_Type=Counter64
_MellanoxQoSPrioTxBcastPkts_Object=MibTableColumn
mellanoxQoSPrioTxBcastPkts=_MellanoxQoSPrioTxBcastPkts_Object((1,3,6,1,4,1,33049,15,1,1,1,13),_MellanoxQoSPrioTxBcastPkts_Type())
mellanoxQoSPrioTxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioTxBcastPkts.setStatus(_A)
_MellanoxQoSPrioTxBytes_Type=Counter64
_MellanoxQoSPrioTxBytes_Object=MibTableColumn
mellanoxQoSPrioTxBytes=_MellanoxQoSPrioTxBytes_Object((1,3,6,1,4,1,33049,15,1,1,1,14),_MellanoxQoSPrioTxBytes_Type())
mellanoxQoSPrioTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioTxBytes.setStatus(_A)
_MellanoxQoSPrioTxPausePkts_Type=Counter64
_MellanoxQoSPrioTxPausePkts_Object=MibTableColumn
mellanoxQoSPrioTxPausePkts=_MellanoxQoSPrioTxPausePkts_Object((1,3,6,1,4,1,33049,15,1,1,1,15),_MellanoxQoSPrioTxPausePkts_Type())
mellanoxQoSPrioTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPrioTxPausePkts.setStatus(_A)
_MellanoxQoSPFCTable_Object=MibTable
mellanoxQoSPFCTable=_MellanoxQoSPFCTable_Object((1,3,6,1,4,1,33049,15,1,2))
if mibBuilder.loadTexts:mellanoxQoSPFCTable.setStatus(_A)
_MellanoxQoSPFCEntry_Object=MibTableRow
mellanoxQoSPFCEntry=_MellanoxQoSPFCEntry_Object((1,3,6,1,4,1,33049,15,1,2,1))
mellanoxQoSPFCEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:mellanoxQoSPFCEntry.setStatus(_A)
_MellanoxQoSPFCIfIndex_Type=InterfaceIndex
_MellanoxQoSPFCIfIndex_Object=MibTableColumn
mellanoxQoSPFCIfIndex=_MellanoxQoSPFCIfIndex_Object((1,3,6,1,4,1,33049,15,1,2,1,1),_MellanoxQoSPFCIfIndex_Type())
mellanoxQoSPFCIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPFCIfIndex.setStatus(_A)
_MellanoxQoSPFCIndex_Type=Integer32
_MellanoxQoSPFCIndex_Object=MibTableColumn
mellanoxQoSPFCIndex=_MellanoxQoSPFCIndex_Object((1,3,6,1,4,1,33049,15,1,2,1,2),_MellanoxQoSPFCIndex_Type())
mellanoxQoSPFCIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPFCIndex.setStatus(_A)
_MellanoxQoSPFCRxPausePkts_Type=Counter64
_MellanoxQoSPFCRxPausePkts_Object=MibTableColumn
mellanoxQoSPFCRxPausePkts=_MellanoxQoSPFCRxPausePkts_Object((1,3,6,1,4,1,33049,15,1,2,1,3),_MellanoxQoSPFCRxPausePkts_Type())
mellanoxQoSPFCRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPFCRxPausePkts.setStatus(_A)
_MellanoxQoSPFCRxPauseDuration_Type=Counter64
_MellanoxQoSPFCRxPauseDuration_Object=MibTableColumn
mellanoxQoSPFCRxPauseDuration=_MellanoxQoSPFCRxPauseDuration_Object((1,3,6,1,4,1,33049,15,1,2,1,4),_MellanoxQoSPFCRxPauseDuration_Type())
mellanoxQoSPFCRxPauseDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPFCRxPauseDuration.setStatus(_A)
_MellanoxQoSPFCTxPausePkts_Type=Counter64
_MellanoxQoSPFCTxPausePkts_Object=MibTableColumn
mellanoxQoSPFCTxPausePkts=_MellanoxQoSPFCTxPausePkts_Object((1,3,6,1,4,1,33049,15,1,2,1,5),_MellanoxQoSPFCTxPausePkts_Type())
mellanoxQoSPFCTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPFCTxPausePkts.setStatus(_A)
_MellanoxQoSPFCTxPauseDuration_Type=Counter64
_MellanoxQoSPFCTxPauseDuration_Object=MibTableColumn
mellanoxQoSPFCTxPauseDuration=_MellanoxQoSPFCTxPauseDuration_Object((1,3,6,1,4,1,33049,15,1,2,1,6),_MellanoxQoSPFCTxPauseDuration_Type())
mellanoxQoSPFCTxPauseDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPFCTxPauseDuration.setStatus(_A)
_MellanoxQoSPGTable_Object=MibTable
mellanoxQoSPGTable=_MellanoxQoSPGTable_Object((1,3,6,1,4,1,33049,15,1,3))
if mibBuilder.loadTexts:mellanoxQoSPGTable.setStatus(_A)
_MellanoxQoSPGEntry_Object=MibTableRow
mellanoxQoSPGEntry=_MellanoxQoSPGEntry_Object((1,3,6,1,4,1,33049,15,1,3,1))
mellanoxQoSPGEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:mellanoxQoSPGEntry.setStatus(_A)
_MellanoxQoSPGIfIndex_Type=InterfaceIndex
_MellanoxQoSPGIfIndex_Object=MibTableColumn
mellanoxQoSPGIfIndex=_MellanoxQoSPGIfIndex_Object((1,3,6,1,4,1,33049,15,1,3,1,1),_MellanoxQoSPGIfIndex_Type())
mellanoxQoSPGIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPGIfIndex.setStatus(_A)
_MellanoxQoSPGIndex_Type=Integer32
_MellanoxQoSPGIndex_Object=MibTableColumn
mellanoxQoSPGIndex=_MellanoxQoSPGIndex_Object((1,3,6,1,4,1,33049,15,1,3,1,2),_MellanoxQoSPGIndex_Type())
mellanoxQoSPGIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPGIndex.setStatus(_A)
_MellanoxQoSPGPkts_Type=Counter64
_MellanoxQoSPGPkts_Object=MibTableColumn
mellanoxQoSPGPkts=_MellanoxQoSPGPkts_Object((1,3,6,1,4,1,33049,15,1,3,1,3),_MellanoxQoSPGPkts_Type())
mellanoxQoSPGPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPGPkts.setStatus(_A)
_MellanoxQoSPGBytes_Type=Counter64
_MellanoxQoSPGBytes_Object=MibTableColumn
mellanoxQoSPGBytes=_MellanoxQoSPGBytes_Object((1,3,6,1,4,1,33049,15,1,3,1,4),_MellanoxQoSPGBytes_Type())
mellanoxQoSPGBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPGBytes.setStatus(_A)
_MellanoxQoSPGQueueDepth_Type=Counter64
_MellanoxQoSPGQueueDepth_Object=MibTableColumn
mellanoxQoSPGQueueDepth=_MellanoxQoSPGQueueDepth_Object((1,3,6,1,4,1,33049,15,1,3,1,5),_MellanoxQoSPGQueueDepth_Type())
mellanoxQoSPGQueueDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPGQueueDepth.setStatus(_A)
_MellanoxQoSPGNoBufferDiscard_Type=Counter64
_MellanoxQoSPGNoBufferDiscard_Object=MibTableColumn
mellanoxQoSPGNoBufferDiscard=_MellanoxQoSPGNoBufferDiscard_Object((1,3,6,1,4,1,33049,15,1,3,1,6),_MellanoxQoSPGNoBufferDiscard_Type())
mellanoxQoSPGNoBufferDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPGNoBufferDiscard.setStatus(_A)
_MellanoxQoSPGSharedBufferDiscard_Type=Counter64
_MellanoxQoSPGSharedBufferDiscard_Object=MibTableColumn
mellanoxQoSPGSharedBufferDiscard=_MellanoxQoSPGSharedBufferDiscard_Object((1,3,6,1,4,1,33049,15,1,3,1,7),_MellanoxQoSPGSharedBufferDiscard_Type())
mellanoxQoSPGSharedBufferDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPGSharedBufferDiscard.setStatus(_A)
_MellanoxQoSTCTable_Object=MibTable
mellanoxQoSTCTable=_MellanoxQoSTCTable_Object((1,3,6,1,4,1,33049,15,1,4))
if mibBuilder.loadTexts:mellanoxQoSTCTable.setStatus(_A)
_MellanoxQoSTCEntry_Object=MibTableRow
mellanoxQoSTCEntry=_MellanoxQoSTCEntry_Object((1,3,6,1,4,1,33049,15,1,4,1))
mellanoxQoSTCEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:mellanoxQoSTCEntry.setStatus(_A)
_MellanoxQoSTCIfIndex_Type=InterfaceIndex
_MellanoxQoSTCIfIndex_Object=MibTableColumn
mellanoxQoSTCIfIndex=_MellanoxQoSTCIfIndex_Object((1,3,6,1,4,1,33049,15,1,4,1,1),_MellanoxQoSTCIfIndex_Type())
mellanoxQoSTCIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCIfIndex.setStatus(_A)
_MellanoxQoSTCIndex_Type=Integer32
_MellanoxQoSTCIndex_Object=MibTableColumn
mellanoxQoSTCIndex=_MellanoxQoSTCIndex_Object((1,3,6,1,4,1,33049,15,1,4,1,2),_MellanoxQoSTCIndex_Type())
mellanoxQoSTCIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCIndex.setStatus(_A)
_MellanoxQoSTCPkts_Type=Counter64
_MellanoxQoSTCPkts_Object=MibTableColumn
mellanoxQoSTCPkts=_MellanoxQoSTCPkts_Object((1,3,6,1,4,1,33049,15,1,4,1,3),_MellanoxQoSTCPkts_Type())
mellanoxQoSTCPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCPkts.setStatus(_A)
_MellanoxQoSTCBytes_Type=Counter64
_MellanoxQoSTCBytes_Object=MibTableColumn
mellanoxQoSTCBytes=_MellanoxQoSTCBytes_Object((1,3,6,1,4,1,33049,15,1,4,1,4),_MellanoxQoSTCBytes_Type())
mellanoxQoSTCBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCBytes.setStatus(_A)
_MellanoxQoSTCSXQueueDepth_Type=Counter64
_MellanoxQoSTCSXQueueDepth_Object=MibTableColumn
mellanoxQoSTCSXQueueDepth=_MellanoxQoSTCSXQueueDepth_Object((1,3,6,1,4,1,33049,15,1,4,1,5),_MellanoxQoSTCSXQueueDepth_Type())
mellanoxQoSTCSXQueueDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCSXQueueDepth.setStatus(_A)
_MellanoxQoSTCUnicastQueueDepth_Type=Counter64
_MellanoxQoSTCUnicastQueueDepth_Object=MibTableColumn
mellanoxQoSTCUnicastQueueDepth=_MellanoxQoSTCUnicastQueueDepth_Object((1,3,6,1,4,1,33049,15,1,4,1,6),_MellanoxQoSTCUnicastQueueDepth_Type())
mellanoxQoSTCUnicastQueueDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCUnicastQueueDepth.setStatus(_A)
_MellanoxQoSTCMulticastQueueDepth_Type=Counter64
_MellanoxQoSTCMulticastQueueDepth_Object=MibTableColumn
mellanoxQoSTCMulticastQueueDepth=_MellanoxQoSTCMulticastQueueDepth_Object((1,3,6,1,4,1,33049,15,1,4,1,7),_MellanoxQoSTCMulticastQueueDepth_Type())
mellanoxQoSTCMulticastQueueDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCMulticastQueueDepth.setStatus(_A)
_MellanoxQoSTCUnicastNoBufferDiscard_Type=Counter64
_MellanoxQoSTCUnicastNoBufferDiscard_Object=MibTableColumn
mellanoxQoSTCUnicastNoBufferDiscard=_MellanoxQoSTCUnicastNoBufferDiscard_Object((1,3,6,1,4,1,33049,15,1,4,1,8),_MellanoxQoSTCUnicastNoBufferDiscard_Type())
mellanoxQoSTCUnicastNoBufferDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCUnicastNoBufferDiscard.setStatus(_A)
_MellanoxQoSTCWREDDiscard_Type=Counter64
_MellanoxQoSTCWREDDiscard_Object=MibTableColumn
mellanoxQoSTCWREDDiscard=_MellanoxQoSTCWREDDiscard_Object((1,3,6,1,4,1,33049,15,1,4,1,9),_MellanoxQoSTCWREDDiscard_Type())
mellanoxQoSTCWREDDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSTCWREDDiscard.setStatus(_A)
_MellanoxQoSPortTable_Object=MibTable
mellanoxQoSPortTable=_MellanoxQoSPortTable_Object((1,3,6,1,4,1,33049,15,1,5))
if mibBuilder.loadTexts:mellanoxQoSPortTable.setStatus(_A)
_MellanoxQoSPortEntry_Object=MibTableRow
mellanoxQoSPortEntry=_MellanoxQoSPortEntry_Object((1,3,6,1,4,1,33049,15,1,5,1))
mellanoxQoSPortEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:mellanoxQoSPortEntry.setStatus(_A)
_MellanoxQoSPortIfIndex_Type=InterfaceIndex
_MellanoxQoSPortIfIndex_Object=MibTableColumn
mellanoxQoSPortIfIndex=_MellanoxQoSPortIfIndex_Object((1,3,6,1,4,1,33049,15,1,5,1,1),_MellanoxQoSPortIfIndex_Type())
mellanoxQoSPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPortIfIndex.setStatus(_A)
_MellanoxQoSPortRxPausePkts_Type=Counter64
_MellanoxQoSPortRxPausePkts_Object=MibTableColumn
mellanoxQoSPortRxPausePkts=_MellanoxQoSPortRxPausePkts_Object((1,3,6,1,4,1,33049,15,1,5,1,2),_MellanoxQoSPortRxPausePkts_Type())
mellanoxQoSPortRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPortRxPausePkts.setStatus(_A)
_MellanoxQoSPortTxPausePkts_Type=Counter64
_MellanoxQoSPortTxPausePkts_Object=MibTableColumn
mellanoxQoSPortTxPausePkts=_MellanoxQoSPortTxPausePkts_Object((1,3,6,1,4,1,33049,15,1,5,1,3),_MellanoxQoSPortTxPausePkts_Type())
mellanoxQoSPortTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPortTxPausePkts.setStatus(_A)
_MellanoxQoSPortTxPauseDuration_Type=Counter64
_MellanoxQoSPortTxPauseDuration_Object=MibTableColumn
mellanoxQoSPortTxPauseDuration=_MellanoxQoSPortTxPauseDuration_Object((1,3,6,1,4,1,33049,15,1,5,1,4),_MellanoxQoSPortTxPauseDuration_Type())
mellanoxQoSPortTxPauseDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPortTxPauseDuration.setStatus(_A)
_MellanoxQoSPortTxWaitMicroseconds_Type=Counter64
_MellanoxQoSPortTxWaitMicroseconds_Object=MibTableColumn
mellanoxQoSPortTxWaitMicroseconds=_MellanoxQoSPortTxWaitMicroseconds_Object((1,3,6,1,4,1,33049,15,1,5,1,5),_MellanoxQoSPortTxWaitMicroseconds_Type())
mellanoxQoSPortTxWaitMicroseconds.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxQoSPortTxWaitMicroseconds.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mellanoxQoSMib':mellanoxQoSMib,'mellanoxQoSPrioTable':mellanoxQoSPrioTable,'mellanoxQoSPrioEntry':mellanoxQoSPrioEntry,_D:mellanoxQoSPrioIfIndex,_E:mellanoxQoSPrioIndex,'mellanoxQoSPrioRxPkts':mellanoxQoSPrioRxPkts,'mellanoxQoSPrioRxUcastPkts':mellanoxQoSPrioRxUcastPkts,'mellanoxQoSPrioRxMcastPkts':mellanoxQoSPrioRxMcastPkts,'mellanoxQoSPrioRxBcastPkts':mellanoxQoSPrioRxBcastPkts,'mellanoxQoSPrioRxBytes':mellanoxQoSPrioRxBytes,'mellanoxQoSPrioRxPausePkts':mellanoxQoSPrioRxPausePkts,'mellanoxQoSPrioRxPauseDuration':mellanoxQoSPrioRxPauseDuration,'mellanoxQoSPrioTxPkts':mellanoxQoSPrioTxPkts,'mellanoxQoSPrioTxUcastPkts':mellanoxQoSPrioTxUcastPkts,'mellanoxQoSPrioTxMcastPkts':mellanoxQoSPrioTxMcastPkts,'mellanoxQoSPrioTxBcastPkts':mellanoxQoSPrioTxBcastPkts,'mellanoxQoSPrioTxBytes':mellanoxQoSPrioTxBytes,'mellanoxQoSPrioTxPausePkts':mellanoxQoSPrioTxPausePkts,'mellanoxQoSPFCTable':mellanoxQoSPFCTable,'mellanoxQoSPFCEntry':mellanoxQoSPFCEntry,_F:mellanoxQoSPFCIfIndex,_G:mellanoxQoSPFCIndex,'mellanoxQoSPFCRxPausePkts':mellanoxQoSPFCRxPausePkts,'mellanoxQoSPFCRxPauseDuration':mellanoxQoSPFCRxPauseDuration,'mellanoxQoSPFCTxPausePkts':mellanoxQoSPFCTxPausePkts,'mellanoxQoSPFCTxPauseDuration':mellanoxQoSPFCTxPauseDuration,'mellanoxQoSPGTable':mellanoxQoSPGTable,'mellanoxQoSPGEntry':mellanoxQoSPGEntry,_H:mellanoxQoSPGIfIndex,_I:mellanoxQoSPGIndex,'mellanoxQoSPGPkts':mellanoxQoSPGPkts,'mellanoxQoSPGBytes':mellanoxQoSPGBytes,'mellanoxQoSPGQueueDepth':mellanoxQoSPGQueueDepth,'mellanoxQoSPGNoBufferDiscard':mellanoxQoSPGNoBufferDiscard,'mellanoxQoSPGSharedBufferDiscard':mellanoxQoSPGSharedBufferDiscard,'mellanoxQoSTCTable':mellanoxQoSTCTable,'mellanoxQoSTCEntry':mellanoxQoSTCEntry,_J:mellanoxQoSTCIfIndex,_K:mellanoxQoSTCIndex,'mellanoxQoSTCPkts':mellanoxQoSTCPkts,'mellanoxQoSTCBytes':mellanoxQoSTCBytes,'mellanoxQoSTCSXQueueDepth':mellanoxQoSTCSXQueueDepth,'mellanoxQoSTCUnicastQueueDepth':mellanoxQoSTCUnicastQueueDepth,'mellanoxQoSTCMulticastQueueDepth':mellanoxQoSTCMulticastQueueDepth,'mellanoxQoSTCUnicastNoBufferDiscard':mellanoxQoSTCUnicastNoBufferDiscard,'mellanoxQoSTCWREDDiscard':mellanoxQoSTCWREDDiscard,'mellanoxQoSPortTable':mellanoxQoSPortTable,'mellanoxQoSPortEntry':mellanoxQoSPortEntry,_L:mellanoxQoSPortIfIndex,'mellanoxQoSPortRxPausePkts':mellanoxQoSPortRxPausePkts,'mellanoxQoSPortTxPausePkts':mellanoxQoSPortTxPausePkts,'mellanoxQoSPortTxPauseDuration':mellanoxQoSPortTxPauseDuration,'mellanoxQoSPortTxWaitMicroseconds':mellanoxQoSPortTxWaitMicroseconds})