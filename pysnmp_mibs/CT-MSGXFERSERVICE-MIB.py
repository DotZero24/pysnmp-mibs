_E='mtsInstanceID'
_D='CT-MSGXFERSERVICE-MIB'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cabletron,=mibBuilder.importSymbols('CTRON-OIDS','cabletron')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtSSA_ObjectIdentity=ObjectIdentity
ctSSA=_CtSSA_ObjectIdentity((1,3,6,1,4,1,52,4497))
_CtMessageTransferService_ObjectIdentity=ObjectIdentity
ctMessageTransferService=_CtMessageTransferService_ObjectIdentity((1,3,6,1,4,1,52,4497,7))
_NumberOfMTSInstances_Type=Integer32
_NumberOfMTSInstances_Object=MibScalar
numberOfMTSInstances=_NumberOfMTSInstances_Object((1,3,6,1,4,1,52,4497,7,1),_NumberOfMTSInstances_Type())
numberOfMTSInstances.setMaxAccess(_C)
if mibBuilder.loadTexts:numberOfMTSInstances.setStatus(_A)
_MessageTransferServiceTable_Object=MibTable
messageTransferServiceTable=_MessageTransferServiceTable_Object((1,3,6,1,4,1,52,4497,7,2))
if mibBuilder.loadTexts:messageTransferServiceTable.setStatus(_A)
_MessageTransferServiceEntry_Object=MibTableRow
messageTransferServiceEntry=_MessageTransferServiceEntry_Object((1,3,6,1,4,1,52,4497,7,2,1))
messageTransferServiceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:messageTransferServiceEntry.setStatus(_A)
_MtsInstanceID_Type=Integer32
_MtsInstanceID_Object=MibTableColumn
mtsInstanceID=_MtsInstanceID_Object((1,3,6,1,4,1,52,4497,7,2,1,1),_MtsInstanceID_Type())
mtsInstanceID.setMaxAccess(_C)
if mibBuilder.loadTexts:mtsInstanceID.setStatus(_A)
_MtsMBusID_Type=Integer32
_MtsMBusID_Object=MibTableColumn
mtsMBusID=_MtsMBusID_Object((1,3,6,1,4,1,52,4497,7,2,1,2),_MtsMBusID_Type())
mtsMBusID.setMaxAccess(_C)
if mibBuilder.loadTexts:mtsMBusID.setStatus(_A)
_MtsNumberOfMTSUsers_Type=Integer32
_MtsNumberOfMTSUsers_Object=MibTableColumn
mtsNumberOfMTSUsers=_MtsNumberOfMTSUsers_Object((1,3,6,1,4,1,52,4497,7,2,1,3),_MtsNumberOfMTSUsers_Type())
mtsNumberOfMTSUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:mtsNumberOfMTSUsers.setStatus(_A)
_MtsNumberOfMTSBuffers_Type=Integer32
_MtsNumberOfMTSBuffers_Object=MibTableColumn
mtsNumberOfMTSBuffers=_MtsNumberOfMTSBuffers_Object((1,3,6,1,4,1,52,4497,7,2,1,4),_MtsNumberOfMTSBuffers_Type())
mtsNumberOfMTSBuffers.setMaxAccess(_C)
if mibBuilder.loadTexts:mtsNumberOfMTSBuffers.setStatus(_A)
_MtsSizeOfMTSBuffers_Type=Integer32
_MtsSizeOfMTSBuffers_Object=MibTableColumn
mtsSizeOfMTSBuffers=_MtsSizeOfMTSBuffers_Object((1,3,6,1,4,1,52,4497,7,2,1,5),_MtsSizeOfMTSBuffers_Type())
mtsSizeOfMTSBuffers.setMaxAccess(_C)
if mibBuilder.loadTexts:mtsSizeOfMTSBuffers.setStatus(_A)
_MtsNumberOfPostedMsgs_Type=Counter32
_MtsNumberOfPostedMsgs_Object=MibTableColumn
mtsNumberOfPostedMsgs=_MtsNumberOfPostedMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,6),_MtsNumberOfPostedMsgs_Type())
mtsNumberOfPostedMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfPostedMsgs.setStatus(_A)
_MtsNumberOfPostedBytes_Type=Counter32
_MtsNumberOfPostedBytes_Object=MibTableColumn
mtsNumberOfPostedBytes=_MtsNumberOfPostedBytes_Object((1,3,6,1,4,1,52,4497,7,2,1,7),_MtsNumberOfPostedBytes_Type())
mtsNumberOfPostedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfPostedBytes.setStatus(_A)
_MtsNumberOfPostedPriorityMsgs_Type=Counter32
_MtsNumberOfPostedPriorityMsgs_Object=MibTableColumn
mtsNumberOfPostedPriorityMsgs=_MtsNumberOfPostedPriorityMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,8),_MtsNumberOfPostedPriorityMsgs_Type())
mtsNumberOfPostedPriorityMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfPostedPriorityMsgs.setStatus(_A)
_MtsNumberOfPostedPriorityBytes_Type=Counter32
_MtsNumberOfPostedPriorityBytes_Object=MibTableColumn
mtsNumberOfPostedPriorityBytes=_MtsNumberOfPostedPriorityBytes_Object((1,3,6,1,4,1,52,4497,7,2,1,9),_MtsNumberOfPostedPriorityBytes_Type())
mtsNumberOfPostedPriorityBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfPostedPriorityBytes.setStatus(_A)
_MtsNumberOfSentMsgs_Type=Counter32
_MtsNumberOfSentMsgs_Object=MibTableColumn
mtsNumberOfSentMsgs=_MtsNumberOfSentMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,10),_MtsNumberOfSentMsgs_Type())
mtsNumberOfSentMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfSentMsgs.setStatus(_A)
_MtsNumberOfSentBytes_Type=Counter32
_MtsNumberOfSentBytes_Object=MibTableColumn
mtsNumberOfSentBytes=_MtsNumberOfSentBytes_Object((1,3,6,1,4,1,52,4497,7,2,1,11),_MtsNumberOfSentBytes_Type())
mtsNumberOfSentBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfSentBytes.setStatus(_A)
_MtsNumberOfPendingMsgs_Type=Gauge32
_MtsNumberOfPendingMsgs_Object=MibTableColumn
mtsNumberOfPendingMsgs=_MtsNumberOfPendingMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,12),_MtsNumberOfPendingMsgs_Type())
mtsNumberOfPendingMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:mtsNumberOfPendingMsgs.setStatus(_A)
_MtsNumberOfPendingBytes_Type=Gauge32
_MtsNumberOfPendingBytes_Object=MibTableColumn
mtsNumberOfPendingBytes=_MtsNumberOfPendingBytes_Object((1,3,6,1,4,1,52,4497,7,2,1,13),_MtsNumberOfPendingBytes_Type())
mtsNumberOfPendingBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mtsNumberOfPendingBytes.setStatus(_A)
_MtsHighWaterForPendingMsgs_Type=Integer32
_MtsHighWaterForPendingMsgs_Object=MibTableColumn
mtsHighWaterForPendingMsgs=_MtsHighWaterForPendingMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,14),_MtsHighWaterForPendingMsgs_Type())
mtsHighWaterForPendingMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsHighWaterForPendingMsgs.setStatus(_A)
_MtsHighWaterForPendingBytes_Type=Integer32
_MtsHighWaterForPendingBytes_Object=MibTableColumn
mtsHighWaterForPendingBytes=_MtsHighWaterForPendingBytes_Object((1,3,6,1,4,1,52,4497,7,2,1,15),_MtsHighWaterForPendingBytes_Type())
mtsHighWaterForPendingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsHighWaterForPendingBytes.setStatus(_A)
_MtsNumberOfTransmissions_Type=Counter32
_MtsNumberOfTransmissions_Object=MibTableColumn
mtsNumberOfTransmissions=_MtsNumberOfTransmissions_Object((1,3,6,1,4,1,52,4497,7,2,1,16),_MtsNumberOfTransmissions_Type())
mtsNumberOfTransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfTransmissions.setStatus(_A)
_MtsNumberOfReceptions_Type=Counter32
_MtsNumberOfReceptions_Object=MibTableColumn
mtsNumberOfReceptions=_MtsNumberOfReceptions_Object((1,3,6,1,4,1,52,4497,7,2,1,17),_MtsNumberOfReceptions_Type())
mtsNumberOfReceptions.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfReceptions.setStatus(_A)
_MtsNumberOfReceivedMsgs_Type=Counter32
_MtsNumberOfReceivedMsgs_Object=MibTableColumn
mtsNumberOfReceivedMsgs=_MtsNumberOfReceivedMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,18),_MtsNumberOfReceivedMsgs_Type())
mtsNumberOfReceivedMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfReceivedMsgs.setStatus(_A)
_MtsNumberOfRcvNoBufs_Type=Counter32
_MtsNumberOfRcvNoBufs_Object=MibTableColumn
mtsNumberOfRcvNoBufs=_MtsNumberOfRcvNoBufs_Object((1,3,6,1,4,1,52,4497,7,2,1,19),_MtsNumberOfRcvNoBufs_Type())
mtsNumberOfRcvNoBufs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfRcvNoBufs.setStatus(_A)
_MtsNumberOfRcvNoUsers_Type=Counter32
_MtsNumberOfRcvNoUsers_Object=MibTableColumn
mtsNumberOfRcvNoUsers=_MtsNumberOfRcvNoUsers_Object((1,3,6,1,4,1,52,4497,7,2,1,20),_MtsNumberOfRcvNoUsers_Type())
mtsNumberOfRcvNoUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfRcvNoUsers.setStatus(_A)
_MtsNumberOfSentPriorityMsgs_Type=Counter32
_MtsNumberOfSentPriorityMsgs_Object=MibTableColumn
mtsNumberOfSentPriorityMsgs=_MtsNumberOfSentPriorityMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,21),_MtsNumberOfSentPriorityMsgs_Type())
mtsNumberOfSentPriorityMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfSentPriorityMsgs.setStatus(_A)
_MtsNumberOfSentPriorityBytes_Type=Counter32
_MtsNumberOfSentPriorityBytes_Object=MibTableColumn
mtsNumberOfSentPriorityBytes=_MtsNumberOfSentPriorityBytes_Object((1,3,6,1,4,1,52,4497,7,2,1,22),_MtsNumberOfSentPriorityBytes_Type())
mtsNumberOfSentPriorityBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfSentPriorityBytes.setStatus(_A)
_MtsNumberOfReceivedBytes_Type=Counter32
_MtsNumberOfReceivedBytes_Object=MibTableColumn
mtsNumberOfReceivedBytes=_MtsNumberOfReceivedBytes_Object((1,3,6,1,4,1,52,4497,7,2,1,23),_MtsNumberOfReceivedBytes_Type())
mtsNumberOfReceivedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfReceivedBytes.setStatus(_A)
_MtsNumberOfReceivedPriorityMsgs_Type=Counter32
_MtsNumberOfReceivedPriorityMsgs_Object=MibTableColumn
mtsNumberOfReceivedPriorityMsgs=_MtsNumberOfReceivedPriorityMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,24),_MtsNumberOfReceivedPriorityMsgs_Type())
mtsNumberOfReceivedPriorityMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfReceivedPriorityMsgs.setStatus(_A)
_MtsNumberOfReceivedPriorityBytes_Type=Counter32
_MtsNumberOfReceivedPriorityBytes_Object=MibTableColumn
mtsNumberOfReceivedPriorityBytes=_MtsNumberOfReceivedPriorityBytes_Object((1,3,6,1,4,1,52,4497,7,2,1,25),_MtsNumberOfReceivedPriorityBytes_Type())
mtsNumberOfReceivedPriorityBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfReceivedPriorityBytes.setStatus(_A)
_MtsNumberOfAckdMsgs_Type=Counter32
_MtsNumberOfAckdMsgs_Object=MibTableColumn
mtsNumberOfAckdMsgs=_MtsNumberOfAckdMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,26),_MtsNumberOfAckdMsgs_Type())
mtsNumberOfAckdMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfAckdMsgs.setStatus(_A)
_MtsNumberOfAckdPriorityMsgs_Type=Counter32
_MtsNumberOfAckdPriorityMsgs_Object=MibTableColumn
mtsNumberOfAckdPriorityMsgs=_MtsNumberOfAckdPriorityMsgs_Object((1,3,6,1,4,1,52,4497,7,2,1,27),_MtsNumberOfAckdPriorityMsgs_Type())
mtsNumberOfAckdPriorityMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsNumberOfAckdPriorityMsgs.setStatus(_A)
_MtsHighWaterForMsgsPerTransmission_Type=Integer32
_MtsHighWaterForMsgsPerTransmission_Object=MibTableColumn
mtsHighWaterForMsgsPerTransmission=_MtsHighWaterForMsgsPerTransmission_Object((1,3,6,1,4,1,52,4497,7,2,1,28),_MtsHighWaterForMsgsPerTransmission_Type())
mtsHighWaterForMsgsPerTransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsHighWaterForMsgsPerTransmission.setStatus(_A)
_MtsHighWaterForMsgsPerReception_Type=Integer32
_MtsHighWaterForMsgsPerReception_Object=MibTableColumn
mtsHighWaterForMsgsPerReception=_MtsHighWaterForMsgsPerReception_Object((1,3,6,1,4,1,52,4497,7,2,1,29),_MtsHighWaterForMsgsPerReception_Type())
mtsHighWaterForMsgsPerReception.setMaxAccess(_B)
if mibBuilder.loadTexts:mtsHighWaterForMsgsPerReception.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ctSSA':ctSSA,'ctMessageTransferService':ctMessageTransferService,'numberOfMTSInstances':numberOfMTSInstances,'messageTransferServiceTable':messageTransferServiceTable,'messageTransferServiceEntry':messageTransferServiceEntry,_E:mtsInstanceID,'mtsMBusID':mtsMBusID,'mtsNumberOfMTSUsers':mtsNumberOfMTSUsers,'mtsNumberOfMTSBuffers':mtsNumberOfMTSBuffers,'mtsSizeOfMTSBuffers':mtsSizeOfMTSBuffers,'mtsNumberOfPostedMsgs':mtsNumberOfPostedMsgs,'mtsNumberOfPostedBytes':mtsNumberOfPostedBytes,'mtsNumberOfPostedPriorityMsgs':mtsNumberOfPostedPriorityMsgs,'mtsNumberOfPostedPriorityBytes':mtsNumberOfPostedPriorityBytes,'mtsNumberOfSentMsgs':mtsNumberOfSentMsgs,'mtsNumberOfSentBytes':mtsNumberOfSentBytes,'mtsNumberOfPendingMsgs':mtsNumberOfPendingMsgs,'mtsNumberOfPendingBytes':mtsNumberOfPendingBytes,'mtsHighWaterForPendingMsgs':mtsHighWaterForPendingMsgs,'mtsHighWaterForPendingBytes':mtsHighWaterForPendingBytes,'mtsNumberOfTransmissions':mtsNumberOfTransmissions,'mtsNumberOfReceptions':mtsNumberOfReceptions,'mtsNumberOfReceivedMsgs':mtsNumberOfReceivedMsgs,'mtsNumberOfRcvNoBufs':mtsNumberOfRcvNoBufs,'mtsNumberOfRcvNoUsers':mtsNumberOfRcvNoUsers,'mtsNumberOfSentPriorityMsgs':mtsNumberOfSentPriorityMsgs,'mtsNumberOfSentPriorityBytes':mtsNumberOfSentPriorityBytes,'mtsNumberOfReceivedBytes':mtsNumberOfReceivedBytes,'mtsNumberOfReceivedPriorityMsgs':mtsNumberOfReceivedPriorityMsgs,'mtsNumberOfReceivedPriorityBytes':mtsNumberOfReceivedPriorityBytes,'mtsNumberOfAckdMsgs':mtsNumberOfAckdMsgs,'mtsNumberOfAckdPriorityMsgs':mtsNumberOfAckdPriorityMsgs,'mtsHighWaterForMsgsPerTransmission':mtsHighWaterForMsgsPerTransmission,'mtsHighWaterForMsgsPerReception':mtsHighWaterForMsgsPerReception})