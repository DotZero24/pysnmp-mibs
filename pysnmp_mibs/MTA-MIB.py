_AE='mtaRFC1566AssocGroup'
_AD='mtaStatusCode'
_AC='not-accessible'
_AB='mtaRFC2789ErrorGroup'
_AA='mtaRFC2789AssocGroup'
_A9='mtaRFC2249ErrorGroup'
_A8='mtaRFC2249AssocGroup'
_A7='mtaRFC1566Group'
_A6='mtaGroupOutboundErrorCount'
_A5='mtaGroupInternalErrorCount'
_A4='mtaGroupInboundErrorCount'
_A3='mtaGroupLoopsDetected'
_A2='mtaGroupOldestMessageId'
_A1='mtaGroupHierarchy'
_A0='mtaGroupCreationTime'
_z='mtaGroupURL'
_y='mtaGroupDescription'
_x='mtaGroupFailedConvertedMessages'
_w='mtaGroupSuccessfulConvertedMessages'
_v='mtaGroupLastOutboundAssociationAttempt'
_u='mtaLoopsDetected'
_t='mtaFailedConvertedMessages'
_s='mtaSuccessfulConvertedMessages'
_r='mtaGroupName'
_q='mtaGroupMailProtocol'
_p='mtaGroupScheduledRetry'
_o='mtaGroupOutboundConnectFailureReason'
_n='mtaGroupInboundRejectionReason'
_m='mtaGroupFailedOutboundAssociations'
_l='mtaGroupRejectedInboundAssociations'
_k='mtaGroupLastOutboundActivity'
_j='mtaGroupLastInboundActivity'
_i='mtaGroupAccumulatedOutboundAssociations'
_h='mtaGroupAccumulatedInboundAssociations'
_g='mtaGroupOutboundAssociations'
_f='mtaGroupInboundAssociations'
_e='mtaGroupOldestMessageStored'
_d='mtaGroupTransmittedRecipients'
_c='mtaGroupStoredRecipients'
_b='mtaGroupReceivedRecipients'
_a='mtaGroupTransmittedVolume'
_Z='mtaGroupStoredVolume'
_Y='mtaGroupReceivedVolume'
_X='mtaGroupTransmittedMessages'
_W='mtaGroupStoredMessages'
_V='mtaGroupRejectedMessages'
_U='mtaGroupReceivedMessages'
_T='mtaTransmittedRecipients'
_S='mtaStoredRecipients'
_R='mtaReceivedRecipients'
_Q='mtaTransmittedVolume'
_P='mtaStoredVolume'
_O='mtaReceivedVolume'
_N='mtaTransmittedMessages'
_M='mtaStoredMessages'
_L='mtaReceivedMessages'
_K='mtaGroupIndex'
_J='mtaRFC2789Group'
_I='mtaRFC2249Group'
_H='mtaGroupAssociationIndex'
_G='Integer32'
_F='applIndex'
_E='NETWORK-SERVICES-MIB'
_D='K-octets'
_C='read-only'
_B='current'
_A='MTA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
URLString,applIndex=mibBuilder.importSymbols(_E,'URLString',_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval')
mta=ModuleIdentity((1,3,6,1,2,1,28))
if mibBuilder.loadTexts:mta.setRevisions(('2000-03-03 00:00','1999-05-12 00:00','1997-08-17 00:00','1993-11-28 00:00'))
_MtaTable_Object=MibTable
mtaTable=_MtaTable_Object((1,3,6,1,2,1,28,1))
if mibBuilder.loadTexts:mtaTable.setStatus(_B)
_MtaEntry_Object=MibTableRow
mtaEntry=_MtaEntry_Object((1,3,6,1,2,1,28,1,1))
mtaEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mtaEntry.setStatus(_B)
_MtaReceivedMessages_Type=Counter32
_MtaReceivedMessages_Object=MibTableColumn
mtaReceivedMessages=_MtaReceivedMessages_Object((1,3,6,1,2,1,28,1,1,1),_MtaReceivedMessages_Type())
mtaReceivedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaReceivedMessages.setStatus(_B)
_MtaStoredMessages_Type=Gauge32
_MtaStoredMessages_Object=MibTableColumn
mtaStoredMessages=_MtaStoredMessages_Object((1,3,6,1,2,1,28,1,1,2),_MtaStoredMessages_Type())
mtaStoredMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaStoredMessages.setStatus(_B)
_MtaTransmittedMessages_Type=Counter32
_MtaTransmittedMessages_Object=MibTableColumn
mtaTransmittedMessages=_MtaTransmittedMessages_Object((1,3,6,1,2,1,28,1,1,3),_MtaTransmittedMessages_Type())
mtaTransmittedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaTransmittedMessages.setStatus(_B)
_MtaReceivedVolume_Type=Counter32
_MtaReceivedVolume_Object=MibTableColumn
mtaReceivedVolume=_MtaReceivedVolume_Object((1,3,6,1,2,1,28,1,1,4),_MtaReceivedVolume_Type())
mtaReceivedVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaReceivedVolume.setStatus(_B)
if mibBuilder.loadTexts:mtaReceivedVolume.setUnits(_D)
_MtaStoredVolume_Type=Gauge32
_MtaStoredVolume_Object=MibTableColumn
mtaStoredVolume=_MtaStoredVolume_Object((1,3,6,1,2,1,28,1,1,5),_MtaStoredVolume_Type())
mtaStoredVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaStoredVolume.setStatus(_B)
if mibBuilder.loadTexts:mtaStoredVolume.setUnits(_D)
_MtaTransmittedVolume_Type=Counter32
_MtaTransmittedVolume_Object=MibTableColumn
mtaTransmittedVolume=_MtaTransmittedVolume_Object((1,3,6,1,2,1,28,1,1,6),_MtaTransmittedVolume_Type())
mtaTransmittedVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaTransmittedVolume.setStatus(_B)
if mibBuilder.loadTexts:mtaTransmittedVolume.setUnits(_D)
_MtaReceivedRecipients_Type=Counter32
_MtaReceivedRecipients_Object=MibTableColumn
mtaReceivedRecipients=_MtaReceivedRecipients_Object((1,3,6,1,2,1,28,1,1,7),_MtaReceivedRecipients_Type())
mtaReceivedRecipients.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaReceivedRecipients.setStatus(_B)
_MtaStoredRecipients_Type=Gauge32
_MtaStoredRecipients_Object=MibTableColumn
mtaStoredRecipients=_MtaStoredRecipients_Object((1,3,6,1,2,1,28,1,1,8),_MtaStoredRecipients_Type())
mtaStoredRecipients.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaStoredRecipients.setStatus(_B)
_MtaTransmittedRecipients_Type=Counter32
_MtaTransmittedRecipients_Object=MibTableColumn
mtaTransmittedRecipients=_MtaTransmittedRecipients_Object((1,3,6,1,2,1,28,1,1,9),_MtaTransmittedRecipients_Type())
mtaTransmittedRecipients.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaTransmittedRecipients.setStatus(_B)
_MtaSuccessfulConvertedMessages_Type=Counter32
_MtaSuccessfulConvertedMessages_Object=MibTableColumn
mtaSuccessfulConvertedMessages=_MtaSuccessfulConvertedMessages_Object((1,3,6,1,2,1,28,1,1,10),_MtaSuccessfulConvertedMessages_Type())
mtaSuccessfulConvertedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaSuccessfulConvertedMessages.setStatus(_B)
_MtaFailedConvertedMessages_Type=Counter32
_MtaFailedConvertedMessages_Object=MibTableColumn
mtaFailedConvertedMessages=_MtaFailedConvertedMessages_Object((1,3,6,1,2,1,28,1,1,11),_MtaFailedConvertedMessages_Type())
mtaFailedConvertedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaFailedConvertedMessages.setStatus(_B)
_MtaLoopsDetected_Type=Counter32
_MtaLoopsDetected_Object=MibTableColumn
mtaLoopsDetected=_MtaLoopsDetected_Object((1,3,6,1,2,1,28,1,1,12),_MtaLoopsDetected_Type())
mtaLoopsDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaLoopsDetected.setStatus(_B)
_MtaGroupTable_Object=MibTable
mtaGroupTable=_MtaGroupTable_Object((1,3,6,1,2,1,28,2))
if mibBuilder.loadTexts:mtaGroupTable.setStatus(_B)
_MtaGroupEntry_Object=MibTableRow
mtaGroupEntry=_MtaGroupEntry_Object((1,3,6,1,2,1,28,2,1))
mtaGroupEntry.setIndexNames((0,_E,_F),(0,_A,_K))
if mibBuilder.loadTexts:mtaGroupEntry.setStatus(_B)
class _MtaGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MtaGroupIndex_Type.__name__=_G
_MtaGroupIndex_Object=MibTableColumn
mtaGroupIndex=_MtaGroupIndex_Object((1,3,6,1,2,1,28,2,1,1),_MtaGroupIndex_Type())
mtaGroupIndex.setMaxAccess(_AC)
if mibBuilder.loadTexts:mtaGroupIndex.setStatus(_B)
_MtaGroupReceivedMessages_Type=Counter32
_MtaGroupReceivedMessages_Object=MibTableColumn
mtaGroupReceivedMessages=_MtaGroupReceivedMessages_Object((1,3,6,1,2,1,28,2,1,2),_MtaGroupReceivedMessages_Type())
mtaGroupReceivedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupReceivedMessages.setStatus(_B)
_MtaGroupRejectedMessages_Type=Counter32
_MtaGroupRejectedMessages_Object=MibTableColumn
mtaGroupRejectedMessages=_MtaGroupRejectedMessages_Object((1,3,6,1,2,1,28,2,1,3),_MtaGroupRejectedMessages_Type())
mtaGroupRejectedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupRejectedMessages.setStatus(_B)
_MtaGroupStoredMessages_Type=Gauge32
_MtaGroupStoredMessages_Object=MibTableColumn
mtaGroupStoredMessages=_MtaGroupStoredMessages_Object((1,3,6,1,2,1,28,2,1,4),_MtaGroupStoredMessages_Type())
mtaGroupStoredMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupStoredMessages.setStatus(_B)
_MtaGroupTransmittedMessages_Type=Counter32
_MtaGroupTransmittedMessages_Object=MibTableColumn
mtaGroupTransmittedMessages=_MtaGroupTransmittedMessages_Object((1,3,6,1,2,1,28,2,1,5),_MtaGroupTransmittedMessages_Type())
mtaGroupTransmittedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupTransmittedMessages.setStatus(_B)
_MtaGroupReceivedVolume_Type=Counter32
_MtaGroupReceivedVolume_Object=MibTableColumn
mtaGroupReceivedVolume=_MtaGroupReceivedVolume_Object((1,3,6,1,2,1,28,2,1,6),_MtaGroupReceivedVolume_Type())
mtaGroupReceivedVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupReceivedVolume.setStatus(_B)
if mibBuilder.loadTexts:mtaGroupReceivedVolume.setUnits(_D)
_MtaGroupStoredVolume_Type=Gauge32
_MtaGroupStoredVolume_Object=MibTableColumn
mtaGroupStoredVolume=_MtaGroupStoredVolume_Object((1,3,6,1,2,1,28,2,1,7),_MtaGroupStoredVolume_Type())
mtaGroupStoredVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupStoredVolume.setStatus(_B)
if mibBuilder.loadTexts:mtaGroupStoredVolume.setUnits(_D)
_MtaGroupTransmittedVolume_Type=Counter32
_MtaGroupTransmittedVolume_Object=MibTableColumn
mtaGroupTransmittedVolume=_MtaGroupTransmittedVolume_Object((1,3,6,1,2,1,28,2,1,8),_MtaGroupTransmittedVolume_Type())
mtaGroupTransmittedVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupTransmittedVolume.setStatus(_B)
if mibBuilder.loadTexts:mtaGroupTransmittedVolume.setUnits(_D)
_MtaGroupReceivedRecipients_Type=Counter32
_MtaGroupReceivedRecipients_Object=MibTableColumn
mtaGroupReceivedRecipients=_MtaGroupReceivedRecipients_Object((1,3,6,1,2,1,28,2,1,9),_MtaGroupReceivedRecipients_Type())
mtaGroupReceivedRecipients.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupReceivedRecipients.setStatus(_B)
_MtaGroupStoredRecipients_Type=Gauge32
_MtaGroupStoredRecipients_Object=MibTableColumn
mtaGroupStoredRecipients=_MtaGroupStoredRecipients_Object((1,3,6,1,2,1,28,2,1,10),_MtaGroupStoredRecipients_Type())
mtaGroupStoredRecipients.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupStoredRecipients.setStatus(_B)
_MtaGroupTransmittedRecipients_Type=Counter32
_MtaGroupTransmittedRecipients_Object=MibTableColumn
mtaGroupTransmittedRecipients=_MtaGroupTransmittedRecipients_Object((1,3,6,1,2,1,28,2,1,11),_MtaGroupTransmittedRecipients_Type())
mtaGroupTransmittedRecipients.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupTransmittedRecipients.setStatus(_B)
_MtaGroupOldestMessageStored_Type=TimeInterval
_MtaGroupOldestMessageStored_Object=MibTableColumn
mtaGroupOldestMessageStored=_MtaGroupOldestMessageStored_Object((1,3,6,1,2,1,28,2,1,12),_MtaGroupOldestMessageStored_Type())
mtaGroupOldestMessageStored.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupOldestMessageStored.setStatus(_B)
_MtaGroupInboundAssociations_Type=Gauge32
_MtaGroupInboundAssociations_Object=MibTableColumn
mtaGroupInboundAssociations=_MtaGroupInboundAssociations_Object((1,3,6,1,2,1,28,2,1,13),_MtaGroupInboundAssociations_Type())
mtaGroupInboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupInboundAssociations.setStatus(_B)
_MtaGroupOutboundAssociations_Type=Gauge32
_MtaGroupOutboundAssociations_Object=MibTableColumn
mtaGroupOutboundAssociations=_MtaGroupOutboundAssociations_Object((1,3,6,1,2,1,28,2,1,14),_MtaGroupOutboundAssociations_Type())
mtaGroupOutboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupOutboundAssociations.setStatus(_B)
_MtaGroupAccumulatedInboundAssociations_Type=Counter32
_MtaGroupAccumulatedInboundAssociations_Object=MibTableColumn
mtaGroupAccumulatedInboundAssociations=_MtaGroupAccumulatedInboundAssociations_Object((1,3,6,1,2,1,28,2,1,15),_MtaGroupAccumulatedInboundAssociations_Type())
mtaGroupAccumulatedInboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupAccumulatedInboundAssociations.setStatus(_B)
_MtaGroupAccumulatedOutboundAssociations_Type=Counter32
_MtaGroupAccumulatedOutboundAssociations_Object=MibTableColumn
mtaGroupAccumulatedOutboundAssociations=_MtaGroupAccumulatedOutboundAssociations_Object((1,3,6,1,2,1,28,2,1,16),_MtaGroupAccumulatedOutboundAssociations_Type())
mtaGroupAccumulatedOutboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupAccumulatedOutboundAssociations.setStatus(_B)
_MtaGroupLastInboundActivity_Type=TimeInterval
_MtaGroupLastInboundActivity_Object=MibTableColumn
mtaGroupLastInboundActivity=_MtaGroupLastInboundActivity_Object((1,3,6,1,2,1,28,2,1,17),_MtaGroupLastInboundActivity_Type())
mtaGroupLastInboundActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupLastInboundActivity.setStatus(_B)
_MtaGroupLastOutboundActivity_Type=TimeInterval
_MtaGroupLastOutboundActivity_Object=MibTableColumn
mtaGroupLastOutboundActivity=_MtaGroupLastOutboundActivity_Object((1,3,6,1,2,1,28,2,1,18),_MtaGroupLastOutboundActivity_Type())
mtaGroupLastOutboundActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupLastOutboundActivity.setStatus(_B)
_MtaGroupRejectedInboundAssociations_Type=Counter32
_MtaGroupRejectedInboundAssociations_Object=MibTableColumn
mtaGroupRejectedInboundAssociations=_MtaGroupRejectedInboundAssociations_Object((1,3,6,1,2,1,28,2,1,19),_MtaGroupRejectedInboundAssociations_Type())
mtaGroupRejectedInboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupRejectedInboundAssociations.setStatus(_B)
_MtaGroupFailedOutboundAssociations_Type=Counter32
_MtaGroupFailedOutboundAssociations_Object=MibTableColumn
mtaGroupFailedOutboundAssociations=_MtaGroupFailedOutboundAssociations_Object((1,3,6,1,2,1,28,2,1,20),_MtaGroupFailedOutboundAssociations_Type())
mtaGroupFailedOutboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupFailedOutboundAssociations.setStatus(_B)
_MtaGroupInboundRejectionReason_Type=SnmpAdminString
_MtaGroupInboundRejectionReason_Object=MibTableColumn
mtaGroupInboundRejectionReason=_MtaGroupInboundRejectionReason_Object((1,3,6,1,2,1,28,2,1,21),_MtaGroupInboundRejectionReason_Type())
mtaGroupInboundRejectionReason.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupInboundRejectionReason.setStatus(_B)
_MtaGroupOutboundConnectFailureReason_Type=SnmpAdminString
_MtaGroupOutboundConnectFailureReason_Object=MibTableColumn
mtaGroupOutboundConnectFailureReason=_MtaGroupOutboundConnectFailureReason_Object((1,3,6,1,2,1,28,2,1,22),_MtaGroupOutboundConnectFailureReason_Type())
mtaGroupOutboundConnectFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupOutboundConnectFailureReason.setStatus(_B)
_MtaGroupScheduledRetry_Type=TimeInterval
_MtaGroupScheduledRetry_Object=MibTableColumn
mtaGroupScheduledRetry=_MtaGroupScheduledRetry_Object((1,3,6,1,2,1,28,2,1,23),_MtaGroupScheduledRetry_Type())
mtaGroupScheduledRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupScheduledRetry.setStatus(_B)
_MtaGroupMailProtocol_Type=ObjectIdentifier
_MtaGroupMailProtocol_Object=MibTableColumn
mtaGroupMailProtocol=_MtaGroupMailProtocol_Object((1,3,6,1,2,1,28,2,1,24),_MtaGroupMailProtocol_Type())
mtaGroupMailProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupMailProtocol.setStatus(_B)
_MtaGroupName_Type=SnmpAdminString
_MtaGroupName_Object=MibTableColumn
mtaGroupName=_MtaGroupName_Object((1,3,6,1,2,1,28,2,1,25),_MtaGroupName_Type())
mtaGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupName.setStatus(_B)
_MtaGroupSuccessfulConvertedMessages_Type=Counter32
_MtaGroupSuccessfulConvertedMessages_Object=MibTableColumn
mtaGroupSuccessfulConvertedMessages=_MtaGroupSuccessfulConvertedMessages_Object((1,3,6,1,2,1,28,2,1,26),_MtaGroupSuccessfulConvertedMessages_Type())
mtaGroupSuccessfulConvertedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupSuccessfulConvertedMessages.setStatus(_B)
_MtaGroupFailedConvertedMessages_Type=Counter32
_MtaGroupFailedConvertedMessages_Object=MibTableColumn
mtaGroupFailedConvertedMessages=_MtaGroupFailedConvertedMessages_Object((1,3,6,1,2,1,28,2,1,27),_MtaGroupFailedConvertedMessages_Type())
mtaGroupFailedConvertedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupFailedConvertedMessages.setStatus(_B)
_MtaGroupDescription_Type=SnmpAdminString
_MtaGroupDescription_Object=MibTableColumn
mtaGroupDescription=_MtaGroupDescription_Object((1,3,6,1,2,1,28,2,1,28),_MtaGroupDescription_Type())
mtaGroupDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupDescription.setStatus(_B)
_MtaGroupURL_Type=URLString
_MtaGroupURL_Object=MibTableColumn
mtaGroupURL=_MtaGroupURL_Object((1,3,6,1,2,1,28,2,1,29),_MtaGroupURL_Type())
mtaGroupURL.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupURL.setStatus(_B)
_MtaGroupCreationTime_Type=TimeInterval
_MtaGroupCreationTime_Object=MibTableColumn
mtaGroupCreationTime=_MtaGroupCreationTime_Object((1,3,6,1,2,1,28,2,1,30),_MtaGroupCreationTime_Type())
mtaGroupCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupCreationTime.setStatus(_B)
class _MtaGroupHierarchy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_MtaGroupHierarchy_Type.__name__=_G
_MtaGroupHierarchy_Object=MibTableColumn
mtaGroupHierarchy=_MtaGroupHierarchy_Object((1,3,6,1,2,1,28,2,1,31),_MtaGroupHierarchy_Type())
mtaGroupHierarchy.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupHierarchy.setStatus(_B)
_MtaGroupOldestMessageId_Type=SnmpAdminString
_MtaGroupOldestMessageId_Object=MibTableColumn
mtaGroupOldestMessageId=_MtaGroupOldestMessageId_Object((1,3,6,1,2,1,28,2,1,32),_MtaGroupOldestMessageId_Type())
mtaGroupOldestMessageId.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupOldestMessageId.setStatus(_B)
_MtaGroupLoopsDetected_Type=Counter32
_MtaGroupLoopsDetected_Object=MibTableColumn
mtaGroupLoopsDetected=_MtaGroupLoopsDetected_Object((1,3,6,1,2,1,28,2,1,33),_MtaGroupLoopsDetected_Type())
mtaGroupLoopsDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupLoopsDetected.setStatus(_B)
_MtaGroupLastOutboundAssociationAttempt_Type=TimeInterval
_MtaGroupLastOutboundAssociationAttempt_Object=MibTableColumn
mtaGroupLastOutboundAssociationAttempt=_MtaGroupLastOutboundAssociationAttempt_Object((1,3,6,1,2,1,28,2,1,34),_MtaGroupLastOutboundAssociationAttempt_Type())
mtaGroupLastOutboundAssociationAttempt.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupLastOutboundAssociationAttempt.setStatus(_B)
_MtaGroupAssociationTable_Object=MibTable
mtaGroupAssociationTable=_MtaGroupAssociationTable_Object((1,3,6,1,2,1,28,3))
if mibBuilder.loadTexts:mtaGroupAssociationTable.setStatus(_B)
_MtaGroupAssociationEntry_Object=MibTableRow
mtaGroupAssociationEntry=_MtaGroupAssociationEntry_Object((1,3,6,1,2,1,28,3,1))
mtaGroupAssociationEntry.setIndexNames((0,_E,_F),(0,_A,_K),(0,_A,_H))
if mibBuilder.loadTexts:mtaGroupAssociationEntry.setStatus(_B)
class _MtaGroupAssociationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MtaGroupAssociationIndex_Type.__name__=_G
_MtaGroupAssociationIndex_Object=MibTableColumn
mtaGroupAssociationIndex=_MtaGroupAssociationIndex_Object((1,3,6,1,2,1,28,3,1,1),_MtaGroupAssociationIndex_Type())
mtaGroupAssociationIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupAssociationIndex.setStatus(_B)
_MtaConformance_ObjectIdentity=ObjectIdentity
mtaConformance=_MtaConformance_ObjectIdentity((1,3,6,1,2,1,28,4))
_MtaGroups_ObjectIdentity=ObjectIdentity
mtaGroups=_MtaGroups_ObjectIdentity((1,3,6,1,2,1,28,4,1))
_MtaCompliances_ObjectIdentity=ObjectIdentity
mtaCompliances=_MtaCompliances_ObjectIdentity((1,3,6,1,2,1,28,4,2))
_MtaGroupErrorTable_Object=MibTable
mtaGroupErrorTable=_MtaGroupErrorTable_Object((1,3,6,1,2,1,28,5))
if mibBuilder.loadTexts:mtaGroupErrorTable.setStatus(_B)
_MtaGroupErrorEntry_Object=MibTableRow
mtaGroupErrorEntry=_MtaGroupErrorEntry_Object((1,3,6,1,2,1,28,5,1))
mtaGroupErrorEntry.setIndexNames((0,_E,_F),(0,_A,_K),(0,_A,_AD))
if mibBuilder.loadTexts:mtaGroupErrorEntry.setStatus(_B)
_MtaGroupInboundErrorCount_Type=Counter32
_MtaGroupInboundErrorCount_Object=MibTableColumn
mtaGroupInboundErrorCount=_MtaGroupInboundErrorCount_Object((1,3,6,1,2,1,28,5,1,1),_MtaGroupInboundErrorCount_Type())
mtaGroupInboundErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupInboundErrorCount.setStatus(_B)
_MtaGroupInternalErrorCount_Type=Counter32
_MtaGroupInternalErrorCount_Object=MibTableColumn
mtaGroupInternalErrorCount=_MtaGroupInternalErrorCount_Object((1,3,6,1,2,1,28,5,1,2),_MtaGroupInternalErrorCount_Type())
mtaGroupInternalErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupInternalErrorCount.setStatus(_B)
_MtaGroupOutboundErrorCount_Type=Counter32
_MtaGroupOutboundErrorCount_Object=MibTableColumn
mtaGroupOutboundErrorCount=_MtaGroupOutboundErrorCount_Object((1,3,6,1,2,1,28,5,1,3),_MtaGroupOutboundErrorCount_Type())
mtaGroupOutboundErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaGroupOutboundErrorCount.setStatus(_B)
class _MtaStatusCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4000000,5999999))
_MtaStatusCode_Type.__name__=_G
_MtaStatusCode_Object=MibTableColumn
mtaStatusCode=_MtaStatusCode_Object((1,3,6,1,2,1,28,5,1,4),_MtaStatusCode_Type())
mtaStatusCode.setMaxAccess(_AC)
if mibBuilder.loadTexts:mtaStatusCode.setStatus(_B)
mtaRFC2249Group=ObjectGroup((1,3,6,1,2,1,28,4,1,4))
mtaRFC2249Group.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_s),(_A,_t),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_u),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_v),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:mtaRFC2249Group.setStatus(_B)
mtaRFC2249AssocGroup=ObjectGroup((1,3,6,1,2,1,28,4,1,5))
mtaRFC2249AssocGroup.setObjects((_A,_H))
if mibBuilder.loadTexts:mtaRFC2249AssocGroup.setStatus(_B)
mtaRFC2249ErrorGroup=ObjectGroup((1,3,6,1,2,1,28,4,1,6))
mtaRFC2249ErrorGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:mtaRFC2249ErrorGroup.setStatus(_B)
mtaRFC2789Group=ObjectGroup((1,3,6,1,2,1,28,4,1,7))
mtaRFC2789Group.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_s),(_A,_t),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_u),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_v),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:mtaRFC2789Group.setStatus(_B)
mtaRFC2789AssocGroup=ObjectGroup((1,3,6,1,2,1,28,4,1,8))
mtaRFC2789AssocGroup.setObjects((_A,_H))
if mibBuilder.loadTexts:mtaRFC2789AssocGroup.setStatus(_B)
mtaRFC2789ErrorGroup=ObjectGroup((1,3,6,1,2,1,28,4,1,9))
mtaRFC2789ErrorGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:mtaRFC2789ErrorGroup.setStatus(_B)
mtaRFC1566Group=ObjectGroup((1,3,6,1,2,1,28,4,1,10))
mtaRFC1566Group.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:mtaRFC1566Group.setStatus(_B)
mtaRFC1566AssocGroup=ObjectGroup((1,3,6,1,2,1,28,4,1,11))
mtaRFC1566AssocGroup.setObjects((_A,_H))
if mibBuilder.loadTexts:mtaRFC1566AssocGroup.setStatus(_B)
mtaCompliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,1))
mtaCompliance.setObjects((_A,_A7))
if mibBuilder.loadTexts:mtaCompliance.setStatus(_B)
mtaAssocCompliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,2))
mtaAssocCompliance.setObjects(*((_A,_A7),(_A,_AE)))
if mibBuilder.loadTexts:mtaAssocCompliance.setStatus(_B)
mtaRFC2249Compliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,5))
mtaRFC2249Compliance.setObjects((_A,_I))
if mibBuilder.loadTexts:mtaRFC2249Compliance.setStatus(_B)
mtaRFC2249AssocCompliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,6))
mtaRFC2249AssocCompliance.setObjects(*((_A,_I),(_A,_A8)))
if mibBuilder.loadTexts:mtaRFC2249AssocCompliance.setStatus(_B)
mtaRFC2249ErrorCompliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,7))
mtaRFC2249ErrorCompliance.setObjects(*((_A,_I),(_A,_A9)))
if mibBuilder.loadTexts:mtaRFC2249ErrorCompliance.setStatus(_B)
mtaRFC2249FullCompliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,8))
mtaRFC2249FullCompliance.setObjects(*((_A,_I),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:mtaRFC2249FullCompliance.setStatus(_B)
mtaRFC2789Compliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,9))
mtaRFC2789Compliance.setObjects((_A,_J))
if mibBuilder.loadTexts:mtaRFC2789Compliance.setStatus(_B)
mtaRFC2789AssocCompliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,10))
mtaRFC2789AssocCompliance.setObjects(*((_A,_J),(_A,_AA)))
if mibBuilder.loadTexts:mtaRFC2789AssocCompliance.setStatus(_B)
mtaRFC2789ErrorCompliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,11))
mtaRFC2789ErrorCompliance.setObjects(*((_A,_J),(_A,_AB)))
if mibBuilder.loadTexts:mtaRFC2789ErrorCompliance.setStatus(_B)
mtaRFC2789FullCompliance=ModuleCompliance((1,3,6,1,2,1,28,4,2,12))
mtaRFC2789FullCompliance.setObjects(*((_A,_J),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:mtaRFC2789FullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'mta':mta,'mtaTable':mtaTable,'mtaEntry':mtaEntry,_L:mtaReceivedMessages,_M:mtaStoredMessages,_N:mtaTransmittedMessages,_O:mtaReceivedVolume,_P:mtaStoredVolume,_Q:mtaTransmittedVolume,_R:mtaReceivedRecipients,_S:mtaStoredRecipients,_T:mtaTransmittedRecipients,_s:mtaSuccessfulConvertedMessages,_t:mtaFailedConvertedMessages,_u:mtaLoopsDetected,'mtaGroupTable':mtaGroupTable,'mtaGroupEntry':mtaGroupEntry,_K:mtaGroupIndex,_U:mtaGroupReceivedMessages,_V:mtaGroupRejectedMessages,_W:mtaGroupStoredMessages,_X:mtaGroupTransmittedMessages,_Y:mtaGroupReceivedVolume,_Z:mtaGroupStoredVolume,_a:mtaGroupTransmittedVolume,_b:mtaGroupReceivedRecipients,_c:mtaGroupStoredRecipients,_d:mtaGroupTransmittedRecipients,_e:mtaGroupOldestMessageStored,_f:mtaGroupInboundAssociations,_g:mtaGroupOutboundAssociations,_h:mtaGroupAccumulatedInboundAssociations,_i:mtaGroupAccumulatedOutboundAssociations,_j:mtaGroupLastInboundActivity,_k:mtaGroupLastOutboundActivity,_l:mtaGroupRejectedInboundAssociations,_m:mtaGroupFailedOutboundAssociations,_n:mtaGroupInboundRejectionReason,_o:mtaGroupOutboundConnectFailureReason,_p:mtaGroupScheduledRetry,_q:mtaGroupMailProtocol,_r:mtaGroupName,_w:mtaGroupSuccessfulConvertedMessages,_x:mtaGroupFailedConvertedMessages,_y:mtaGroupDescription,_z:mtaGroupURL,_A0:mtaGroupCreationTime,_A1:mtaGroupHierarchy,_A2:mtaGroupOldestMessageId,_A3:mtaGroupLoopsDetected,_v:mtaGroupLastOutboundAssociationAttempt,'mtaGroupAssociationTable':mtaGroupAssociationTable,'mtaGroupAssociationEntry':mtaGroupAssociationEntry,_H:mtaGroupAssociationIndex,'mtaConformance':mtaConformance,'mtaGroups':mtaGroups,_I:mtaRFC2249Group,_A8:mtaRFC2249AssocGroup,_A9:mtaRFC2249ErrorGroup,_J:mtaRFC2789Group,_AA:mtaRFC2789AssocGroup,_AB:mtaRFC2789ErrorGroup,_A7:mtaRFC1566Group,_AE:mtaRFC1566AssocGroup,'mtaCompliances':mtaCompliances,'mtaCompliance':mtaCompliance,'mtaAssocCompliance':mtaAssocCompliance,'mtaRFC2249Compliance':mtaRFC2249Compliance,'mtaRFC2249AssocCompliance':mtaRFC2249AssocCompliance,'mtaRFC2249ErrorCompliance':mtaRFC2249ErrorCompliance,'mtaRFC2249FullCompliance':mtaRFC2249FullCompliance,'mtaRFC2789Compliance':mtaRFC2789Compliance,'mtaRFC2789AssocCompliance':mtaRFC2789AssocCompliance,'mtaRFC2789ErrorCompliance':mtaRFC2789ErrorCompliance,'mtaRFC2789FullCompliance':mtaRFC2789FullCompliance,'mtaGroupErrorTable':mtaGroupErrorTable,'mtaGroupErrorEntry':mtaGroupErrorEntry,_A4:mtaGroupInboundErrorCount,_A5:mtaGroupInternalErrorCount,_A6:mtaGroupOutboundErrorCount,_AD:mtaStatusCode})