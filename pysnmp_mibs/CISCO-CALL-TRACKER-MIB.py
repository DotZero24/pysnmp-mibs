_Ab='cctHistoryGroupRev1'
_Aa='cctActiveGroupRev1'
_AZ='cctHistoryGroup'
_AY='cctActiveGroup'
_AX='cctCallTerminateNotification'
_AW='cctCallSetupNotification'
_AV='cctHistoryCallSignalingType'
_AU='cctActiveCallSignalingType'
_AT='cctCallSetupTermNotifyEnable'
_AS='cctCallIdPrefix'
_AR='cctHistoryIndex'
_AQ='originate'
_AP='not-accessible'
_AO='cctActiveCallId'
_AN='cctNotificationGroup'
_AM='cctNotificationConfigGroup'
_AL='cctGeneralGroup'
_AK='cctHistoryDisconnectReasonText'
_AJ='cctHistoryDisconnectTime'
_AI='cctHistoryTransmitBytes'
_AH='cctHistoryReceiveBytes'
_AG='cctHistoryChargedUnits'
_AF='cctHistoryMpBundleId'
_AE='cctHistoryCallingPartyId'
_AD='cctHistoryCalledPartyId'
_AC='cctHistoryEntryChannel'
_AB='cctHistoryEntryDs1'
_AA='cctHistoryEntryPort'
_A9='cctHistoryEntrySlot'
_A8='cctHistoryResourcePort'
_A7='cctHistoryResourceSlot'
_A6='cctHistoryInitialTxRate'
_A5='cctHistoryInitialRxRate'
_A4='cctHistoryCallCategory'
_A3='cctHistoryAccountingSessionId'
_A2='cctHistoryUserSubnetMask'
_A1='cctHistoryUserIpAddr'
_A0='cctHistoryUserId'
_z='cctHistoryUserValidationTime'
_y='cctHistoryServiceType'
_x='cctHistoryServiceUpTime'
_w='cctHistoryPhysicalLayerReadyTime'
_v='cctHistoryConnectionTime'
_u='cctHistoryOrigin'
_t='cctHistorySetupTime'
_s='cctHistoryTableNewestIndex'
_r='cctHistoryTableHighWaterMark'
_q='cctHistoryTableNumberEntries'
_p='cctHistoryTableRetainTimer'
_o='cctHistoryTableMaxEntries'
_n='cctHistoryTableEntriesLimit'
_m='deprecated'
_l='cctActiveTransmitBytes'
_k='cctActiveReceiveBytes'
_j='cctActiveChargedUnits'
_i='cctActiveMpBundleId'
_h='cctActiveEntryChannel'
_g='cctActiveEntryDs1'
_f='cctActiveEntryPort'
_e='cctActiveEntrySlot'
_d='cctActiveResourcePort'
_c='cctActiveResourceSlot'
_b='cctActiveInitialTxRate'
_a='cctActiveInitialRxRate'
_Z='cctActiveAccountingSessionId'
_Y='cctActiveUserSubnetMask'
_X='cctActiveUserIpAddr'
_W='cctActiveUserId'
_V='cctActiveUserValidationTime'
_U='cctActiveServiceType'
_T='cctActiveServiceUpTime'
_S='cctActivePhysicalLayerReadyTime'
_R='cctActiveConnectionTime'
_Q='cctActiveOrigin'
_P='cctActiveTableHighWaterMark'
_O='cctActiveTableNumberEntries'
_N='read-write'
_M='cctHistoryCallId'
_L='cctActiveCallingPartyId'
_K='cctActiveCalledPartyId'
_J='cctActiveCallCategory'
_I='cctActiveSetupTime'
_H='bytes'
_G='bits per second'
_F='Unsigned32'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-CALL-TRACKER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
AbsoluteCounter32,=mibBuilder.importSymbols('DIAL-CONTROL-MIB','AbsoluteCounter32')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoCallTrackerMIB=ModuleIdentity((1,3,6,1,4,1,9,9,163))
if mibBuilder.loadTexts:ciscoCallTrackerMIB.setRevisions(('2005-04-12 00:00','2004-02-02 00:00','2000-02-10 00:00'))
class CctCallId(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CctServiceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',1),('other',2),('slip',3),('ppp',4),('mp',5),('tcpClear',6),('telnet',7),('exec',8),('l2f',9),('l2tp',10)))
class CctCallCategory(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',1),('other',2),('modem',3),('isdnSync',4),('v110',5),('v120',6),('casDigital',7),('mgcpData',8),('syncData',9),('lapb-ta',10)))
class CctCallSigType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('external',2),('q931',3),('autoDetect',4)))
_CctMIBObjects_ObjectIdentity=ObjectIdentity
cctMIBObjects=_CctMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,163,1))
_CctGeneral_ObjectIdentity=ObjectIdentity
cctGeneral=_CctGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,163,1,1))
_CctCallIdPrefix_Type=Unsigned32
_CctCallIdPrefix_Object=MibScalar
cctCallIdPrefix=_CctCallIdPrefix_Object((1,3,6,1,4,1,9,9,163,1,1,1),_CctCallIdPrefix_Type())
cctCallIdPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cctCallIdPrefix.setStatus(_B)
_CctActive_ObjectIdentity=ObjectIdentity
cctActive=_CctActive_ObjectIdentity((1,3,6,1,4,1,9,9,163,1,2))
_CctActiveTableNumberEntries_Type=Gauge32
_CctActiveTableNumberEntries_Object=MibScalar
cctActiveTableNumberEntries=_CctActiveTableNumberEntries_Object((1,3,6,1,4,1,9,9,163,1,2,1),_CctActiveTableNumberEntries_Type())
cctActiveTableNumberEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveTableNumberEntries.setStatus(_B)
_CctActiveTableHighWaterMark_Type=Gauge32
_CctActiveTableHighWaterMark_Object=MibScalar
cctActiveTableHighWaterMark=_CctActiveTableHighWaterMark_Object((1,3,6,1,4,1,9,9,163,1,2,2),_CctActiveTableHighWaterMark_Type())
cctActiveTableHighWaterMark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveTableHighWaterMark.setStatus(_B)
_CctActiveTable_Object=MibTable
cctActiveTable=_CctActiveTable_Object((1,3,6,1,4,1,9,9,163,1,2,3))
if mibBuilder.loadTexts:cctActiveTable.setStatus(_B)
_CctActiveEntry_Object=MibTableRow
cctActiveEntry=_CctActiveEntry_Object((1,3,6,1,4,1,9,9,163,1,2,3,1))
cctActiveEntry.setIndexNames((0,_A,_AO))
if mibBuilder.loadTexts:cctActiveEntry.setStatus(_B)
_CctActiveCallId_Type=CctCallId
_CctActiveCallId_Object=MibTableColumn
cctActiveCallId=_CctActiveCallId_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,1),_CctActiveCallId_Type())
cctActiveCallId.setMaxAccess(_AP)
if mibBuilder.loadTexts:cctActiveCallId.setStatus(_B)
_CctActiveSetupTime_Type=TimeStamp
_CctActiveSetupTime_Object=MibTableColumn
cctActiveSetupTime=_CctActiveSetupTime_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,2),_CctActiveSetupTime_Type())
cctActiveSetupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveSetupTime.setStatus(_B)
class _CctActiveOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AQ,1),('answer',2)))
_CctActiveOrigin_Type.__name__=_D
_CctActiveOrigin_Object=MibTableColumn
cctActiveOrigin=_CctActiveOrigin_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,3),_CctActiveOrigin_Type())
cctActiveOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveOrigin.setStatus(_B)
_CctActiveConnectionTime_Type=TimeStamp
_CctActiveConnectionTime_Object=MibTableColumn
cctActiveConnectionTime=_CctActiveConnectionTime_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,4),_CctActiveConnectionTime_Type())
cctActiveConnectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveConnectionTime.setStatus(_B)
_CctActivePhysicalLayerReadyTime_Type=TimeStamp
_CctActivePhysicalLayerReadyTime_Object=MibTableColumn
cctActivePhysicalLayerReadyTime=_CctActivePhysicalLayerReadyTime_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,5),_CctActivePhysicalLayerReadyTime_Type())
cctActivePhysicalLayerReadyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActivePhysicalLayerReadyTime.setStatus(_B)
_CctActiveServiceUpTime_Type=TimeStamp
_CctActiveServiceUpTime_Object=MibTableColumn
cctActiveServiceUpTime=_CctActiveServiceUpTime_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,6),_CctActiveServiceUpTime_Type())
cctActiveServiceUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveServiceUpTime.setStatus(_B)
_CctActiveServiceType_Type=CctServiceType
_CctActiveServiceType_Object=MibTableColumn
cctActiveServiceType=_CctActiveServiceType_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,7),_CctActiveServiceType_Type())
cctActiveServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveServiceType.setStatus(_B)
_CctActiveUserValidationTime_Type=TimeStamp
_CctActiveUserValidationTime_Object=MibTableColumn
cctActiveUserValidationTime=_CctActiveUserValidationTime_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,8),_CctActiveUserValidationTime_Type())
cctActiveUserValidationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveUserValidationTime.setStatus(_B)
class _CctActiveUserId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CctActiveUserId_Type.__name__=_E
_CctActiveUserId_Object=MibTableColumn
cctActiveUserId=_CctActiveUserId_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,9),_CctActiveUserId_Type())
cctActiveUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveUserId.setStatus(_B)
_CctActiveUserIpAddr_Type=IpAddress
_CctActiveUserIpAddr_Object=MibTableColumn
cctActiveUserIpAddr=_CctActiveUserIpAddr_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,10),_CctActiveUserIpAddr_Type())
cctActiveUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveUserIpAddr.setStatus(_B)
_CctActiveUserSubnetMask_Type=IpAddress
_CctActiveUserSubnetMask_Object=MibTableColumn
cctActiveUserSubnetMask=_CctActiveUserSubnetMask_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,11),_CctActiveUserSubnetMask_Type())
cctActiveUserSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveUserSubnetMask.setStatus(_B)
class _CctActiveAccountingSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CctActiveAccountingSessionId_Type.__name__=_E
_CctActiveAccountingSessionId_Object=MibTableColumn
cctActiveAccountingSessionId=_CctActiveAccountingSessionId_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,12),_CctActiveAccountingSessionId_Type())
cctActiveAccountingSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveAccountingSessionId.setStatus(_B)
_CctActiveCallCategory_Type=CctCallCategory
_CctActiveCallCategory_Object=MibTableColumn
cctActiveCallCategory=_CctActiveCallCategory_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,13),_CctActiveCallCategory_Type())
cctActiveCallCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveCallCategory.setStatus(_B)
_CctActiveInitialRxRate_Type=Unsigned32
_CctActiveInitialRxRate_Object=MibTableColumn
cctActiveInitialRxRate=_CctActiveInitialRxRate_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,14),_CctActiveInitialRxRate_Type())
cctActiveInitialRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveInitialRxRate.setStatus(_B)
if mibBuilder.loadTexts:cctActiveInitialRxRate.setUnits(_G)
_CctActiveInitialTxRate_Type=Unsigned32
_CctActiveInitialTxRate_Object=MibTableColumn
cctActiveInitialTxRate=_CctActiveInitialTxRate_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,15),_CctActiveInitialTxRate_Type())
cctActiveInitialTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveInitialTxRate.setStatus(_B)
if mibBuilder.loadTexts:cctActiveInitialTxRate.setUnits(_G)
class _CctActiveResourceSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,214783647))
_CctActiveResourceSlot_Type.__name__=_D
_CctActiveResourceSlot_Object=MibTableColumn
cctActiveResourceSlot=_CctActiveResourceSlot_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,16),_CctActiveResourceSlot_Type())
cctActiveResourceSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveResourceSlot.setStatus(_B)
class _CctActiveResourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,214783647))
_CctActiveResourcePort_Type.__name__=_D
_CctActiveResourcePort_Object=MibTableColumn
cctActiveResourcePort=_CctActiveResourcePort_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,17),_CctActiveResourcePort_Type())
cctActiveResourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveResourcePort.setStatus(_B)
class _CctActiveEntrySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_CctActiveEntrySlot_Type.__name__=_D
_CctActiveEntrySlot_Object=MibTableColumn
cctActiveEntrySlot=_CctActiveEntrySlot_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,18),_CctActiveEntrySlot_Type())
cctActiveEntrySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveEntrySlot.setStatus(_B)
class _CctActiveEntryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_CctActiveEntryPort_Type.__name__=_D
_CctActiveEntryPort_Object=MibTableColumn
cctActiveEntryPort=_CctActiveEntryPort_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,19),_CctActiveEntryPort_Type())
cctActiveEntryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveEntryPort.setStatus(_B)
class _CctActiveEntryDs1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_CctActiveEntryDs1_Type.__name__=_D
_CctActiveEntryDs1_Object=MibTableColumn
cctActiveEntryDs1=_CctActiveEntryDs1_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,20),_CctActiveEntryDs1_Type())
cctActiveEntryDs1.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveEntryDs1.setStatus(_B)
class _CctActiveEntryChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_CctActiveEntryChannel_Type.__name__=_D
_CctActiveEntryChannel_Object=MibTableColumn
cctActiveEntryChannel=_CctActiveEntryChannel_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,21),_CctActiveEntryChannel_Type())
cctActiveEntryChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveEntryChannel.setStatus(_B)
class _CctActiveCalledPartyId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CctActiveCalledPartyId_Type.__name__=_E
_CctActiveCalledPartyId_Object=MibTableColumn
cctActiveCalledPartyId=_CctActiveCalledPartyId_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,22),_CctActiveCalledPartyId_Type())
cctActiveCalledPartyId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveCalledPartyId.setStatus(_B)
class _CctActiveCallingPartyId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CctActiveCallingPartyId_Type.__name__=_E
_CctActiveCallingPartyId_Object=MibTableColumn
cctActiveCallingPartyId=_CctActiveCallingPartyId_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,23),_CctActiveCallingPartyId_Type())
cctActiveCallingPartyId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveCallingPartyId.setStatus(_B)
_CctActiveMpBundleId_Type=Unsigned32
_CctActiveMpBundleId_Object=MibTableColumn
cctActiveMpBundleId=_CctActiveMpBundleId_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,24),_CctActiveMpBundleId_Type())
cctActiveMpBundleId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveMpBundleId.setStatus(_B)
_CctActiveChargedUnits_Type=AbsoluteCounter32
_CctActiveChargedUnits_Object=MibTableColumn
cctActiveChargedUnits=_CctActiveChargedUnits_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,25),_CctActiveChargedUnits_Type())
cctActiveChargedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveChargedUnits.setStatus(_B)
_CctActiveReceiveBytes_Type=AbsoluteCounter32
_CctActiveReceiveBytes_Object=MibTableColumn
cctActiveReceiveBytes=_CctActiveReceiveBytes_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,26),_CctActiveReceiveBytes_Type())
cctActiveReceiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveReceiveBytes.setStatus(_B)
if mibBuilder.loadTexts:cctActiveReceiveBytes.setUnits(_H)
_CctActiveTransmitBytes_Type=AbsoluteCounter32
_CctActiveTransmitBytes_Object=MibTableColumn
cctActiveTransmitBytes=_CctActiveTransmitBytes_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,27),_CctActiveTransmitBytes_Type())
cctActiveTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveTransmitBytes.setStatus(_B)
if mibBuilder.loadTexts:cctActiveTransmitBytes.setUnits(_H)
_CctActiveCallSignalingType_Type=CctCallSigType
_CctActiveCallSignalingType_Object=MibTableColumn
cctActiveCallSignalingType=_CctActiveCallSignalingType_Object((1,3,6,1,4,1,9,9,163,1,2,3,1,28),_CctActiveCallSignalingType_Type())
cctActiveCallSignalingType.setMaxAccess(_C)
if mibBuilder.loadTexts:cctActiveCallSignalingType.setStatus(_B)
_CctHistory_ObjectIdentity=ObjectIdentity
cctHistory=_CctHistory_ObjectIdentity((1,3,6,1,4,1,9,9,163,1,3))
class _CctHistoryTableEntriesLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CctHistoryTableEntriesLimit_Type.__name__=_F
_CctHistoryTableEntriesLimit_Object=MibScalar
cctHistoryTableEntriesLimit=_CctHistoryTableEntriesLimit_Object((1,3,6,1,4,1,9,9,163,1,3,1),_CctHistoryTableEntriesLimit_Type())
cctHistoryTableEntriesLimit.setMaxAccess(_N)
if mibBuilder.loadTexts:cctHistoryTableEntriesLimit.setStatus(_B)
_CctHistoryTableMaxEntries_Type=Unsigned32
_CctHistoryTableMaxEntries_Object=MibScalar
cctHistoryTableMaxEntries=_CctHistoryTableMaxEntries_Object((1,3,6,1,4,1,9,9,163,1,3,2),_CctHistoryTableMaxEntries_Type())
cctHistoryTableMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryTableMaxEntries.setStatus(_B)
class _CctHistoryTableRetainTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CctHistoryTableRetainTimer_Type.__name__=_F
_CctHistoryTableRetainTimer_Object=MibScalar
cctHistoryTableRetainTimer=_CctHistoryTableRetainTimer_Object((1,3,6,1,4,1,9,9,163,1,3,3),_CctHistoryTableRetainTimer_Type())
cctHistoryTableRetainTimer.setMaxAccess(_N)
if mibBuilder.loadTexts:cctHistoryTableRetainTimer.setStatus(_B)
if mibBuilder.loadTexts:cctHistoryTableRetainTimer.setUnits('minutes')
_CctHistoryTableNumberEntries_Type=Gauge32
_CctHistoryTableNumberEntries_Object=MibScalar
cctHistoryTableNumberEntries=_CctHistoryTableNumberEntries_Object((1,3,6,1,4,1,9,9,163,1,3,4),_CctHistoryTableNumberEntries_Type())
cctHistoryTableNumberEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryTableNumberEntries.setStatus(_B)
_CctHistoryTableHighWaterMark_Type=Gauge32
_CctHistoryTableHighWaterMark_Object=MibScalar
cctHistoryTableHighWaterMark=_CctHistoryTableHighWaterMark_Object((1,3,6,1,4,1,9,9,163,1,3,5),_CctHistoryTableHighWaterMark_Type())
cctHistoryTableHighWaterMark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryTableHighWaterMark.setStatus(_B)
class _CctHistoryTableNewestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CctHistoryTableNewestIndex_Type.__name__=_F
_CctHistoryTableNewestIndex_Object=MibScalar
cctHistoryTableNewestIndex=_CctHistoryTableNewestIndex_Object((1,3,6,1,4,1,9,9,163,1,3,6),_CctHistoryTableNewestIndex_Type())
cctHistoryTableNewestIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryTableNewestIndex.setStatus(_B)
_CctHistoryTable_Object=MibTable
cctHistoryTable=_CctHistoryTable_Object((1,3,6,1,4,1,9,9,163,1,3,7))
if mibBuilder.loadTexts:cctHistoryTable.setStatus(_B)
_CctHistoryEntry_Object=MibTableRow
cctHistoryEntry=_CctHistoryEntry_Object((1,3,6,1,4,1,9,9,163,1,3,7,1))
cctHistoryEntry.setIndexNames((0,_A,_AR))
if mibBuilder.loadTexts:cctHistoryEntry.setStatus(_B)
class _CctHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CctHistoryIndex_Type.__name__=_F
_CctHistoryIndex_Object=MibTableColumn
cctHistoryIndex=_CctHistoryIndex_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,1),_CctHistoryIndex_Type())
cctHistoryIndex.setMaxAccess(_AP)
if mibBuilder.loadTexts:cctHistoryIndex.setStatus(_B)
_CctHistoryCallId_Type=CctCallId
_CctHistoryCallId_Object=MibTableColumn
cctHistoryCallId=_CctHistoryCallId_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,2),_CctHistoryCallId_Type())
cctHistoryCallId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryCallId.setStatus(_B)
_CctHistorySetupTime_Type=TimeStamp
_CctHistorySetupTime_Object=MibTableColumn
cctHistorySetupTime=_CctHistorySetupTime_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,3),_CctHistorySetupTime_Type())
cctHistorySetupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistorySetupTime.setStatus(_B)
class _CctHistoryOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AQ,1),('answer',2)))
_CctHistoryOrigin_Type.__name__=_D
_CctHistoryOrigin_Object=MibTableColumn
cctHistoryOrigin=_CctHistoryOrigin_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,4),_CctHistoryOrigin_Type())
cctHistoryOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryOrigin.setStatus(_B)
_CctHistoryConnectionTime_Type=TimeStamp
_CctHistoryConnectionTime_Object=MibTableColumn
cctHistoryConnectionTime=_CctHistoryConnectionTime_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,5),_CctHistoryConnectionTime_Type())
cctHistoryConnectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryConnectionTime.setStatus(_B)
_CctHistoryPhysicalLayerReadyTime_Type=TimeStamp
_CctHistoryPhysicalLayerReadyTime_Object=MibTableColumn
cctHistoryPhysicalLayerReadyTime=_CctHistoryPhysicalLayerReadyTime_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,6),_CctHistoryPhysicalLayerReadyTime_Type())
cctHistoryPhysicalLayerReadyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryPhysicalLayerReadyTime.setStatus(_B)
_CctHistoryServiceUpTime_Type=TimeStamp
_CctHistoryServiceUpTime_Object=MibTableColumn
cctHistoryServiceUpTime=_CctHistoryServiceUpTime_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,7),_CctHistoryServiceUpTime_Type())
cctHistoryServiceUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryServiceUpTime.setStatus(_B)
_CctHistoryServiceType_Type=CctServiceType
_CctHistoryServiceType_Object=MibTableColumn
cctHistoryServiceType=_CctHistoryServiceType_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,8),_CctHistoryServiceType_Type())
cctHistoryServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryServiceType.setStatus(_B)
_CctHistoryUserValidationTime_Type=TimeStamp
_CctHistoryUserValidationTime_Object=MibTableColumn
cctHistoryUserValidationTime=_CctHistoryUserValidationTime_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,9),_CctHistoryUserValidationTime_Type())
cctHistoryUserValidationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryUserValidationTime.setStatus(_B)
class _CctHistoryUserId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CctHistoryUserId_Type.__name__=_E
_CctHistoryUserId_Object=MibTableColumn
cctHistoryUserId=_CctHistoryUserId_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,10),_CctHistoryUserId_Type())
cctHistoryUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryUserId.setStatus(_B)
_CctHistoryUserIpAddr_Type=IpAddress
_CctHistoryUserIpAddr_Object=MibTableColumn
cctHistoryUserIpAddr=_CctHistoryUserIpAddr_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,11),_CctHistoryUserIpAddr_Type())
cctHistoryUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryUserIpAddr.setStatus(_B)
_CctHistoryUserSubnetMask_Type=IpAddress
_CctHistoryUserSubnetMask_Object=MibTableColumn
cctHistoryUserSubnetMask=_CctHistoryUserSubnetMask_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,12),_CctHistoryUserSubnetMask_Type())
cctHistoryUserSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryUserSubnetMask.setStatus(_B)
class _CctHistoryAccountingSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CctHistoryAccountingSessionId_Type.__name__=_E
_CctHistoryAccountingSessionId_Object=MibTableColumn
cctHistoryAccountingSessionId=_CctHistoryAccountingSessionId_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,13),_CctHistoryAccountingSessionId_Type())
cctHistoryAccountingSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryAccountingSessionId.setStatus(_B)
_CctHistoryCallCategory_Type=CctCallCategory
_CctHistoryCallCategory_Object=MibTableColumn
cctHistoryCallCategory=_CctHistoryCallCategory_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,14),_CctHistoryCallCategory_Type())
cctHistoryCallCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryCallCategory.setStatus(_B)
_CctHistoryInitialRxRate_Type=Unsigned32
_CctHistoryInitialRxRate_Object=MibTableColumn
cctHistoryInitialRxRate=_CctHistoryInitialRxRate_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,15),_CctHistoryInitialRxRate_Type())
cctHistoryInitialRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryInitialRxRate.setStatus(_B)
if mibBuilder.loadTexts:cctHistoryInitialRxRate.setUnits(_G)
_CctHistoryInitialTxRate_Type=Unsigned32
_CctHistoryInitialTxRate_Object=MibTableColumn
cctHistoryInitialTxRate=_CctHistoryInitialTxRate_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,16),_CctHistoryInitialTxRate_Type())
cctHistoryInitialTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryInitialTxRate.setStatus(_B)
if mibBuilder.loadTexts:cctHistoryInitialTxRate.setUnits(_G)
class _CctHistoryResourceSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,214783647))
_CctHistoryResourceSlot_Type.__name__=_D
_CctHistoryResourceSlot_Object=MibTableColumn
cctHistoryResourceSlot=_CctHistoryResourceSlot_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,17),_CctHistoryResourceSlot_Type())
cctHistoryResourceSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryResourceSlot.setStatus(_B)
class _CctHistoryResourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,214783647))
_CctHistoryResourcePort_Type.__name__=_D
_CctHistoryResourcePort_Object=MibTableColumn
cctHistoryResourcePort=_CctHistoryResourcePort_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,18),_CctHistoryResourcePort_Type())
cctHistoryResourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryResourcePort.setStatus(_B)
class _CctHistoryEntrySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_CctHistoryEntrySlot_Type.__name__=_D
_CctHistoryEntrySlot_Object=MibTableColumn
cctHistoryEntrySlot=_CctHistoryEntrySlot_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,19),_CctHistoryEntrySlot_Type())
cctHistoryEntrySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryEntrySlot.setStatus(_B)
class _CctHistoryEntryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_CctHistoryEntryPort_Type.__name__=_D
_CctHistoryEntryPort_Object=MibTableColumn
cctHistoryEntryPort=_CctHistoryEntryPort_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,20),_CctHistoryEntryPort_Type())
cctHistoryEntryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryEntryPort.setStatus(_B)
class _CctHistoryEntryDs1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_CctHistoryEntryDs1_Type.__name__=_D
_CctHistoryEntryDs1_Object=MibTableColumn
cctHistoryEntryDs1=_CctHistoryEntryDs1_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,22),_CctHistoryEntryDs1_Type())
cctHistoryEntryDs1.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryEntryDs1.setStatus(_B)
class _CctHistoryEntryChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_CctHistoryEntryChannel_Type.__name__=_D
_CctHistoryEntryChannel_Object=MibTableColumn
cctHistoryEntryChannel=_CctHistoryEntryChannel_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,23),_CctHistoryEntryChannel_Type())
cctHistoryEntryChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryEntryChannel.setStatus(_B)
class _CctHistoryCalledPartyId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CctHistoryCalledPartyId_Type.__name__=_E
_CctHistoryCalledPartyId_Object=MibTableColumn
cctHistoryCalledPartyId=_CctHistoryCalledPartyId_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,24),_CctHistoryCalledPartyId_Type())
cctHistoryCalledPartyId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryCalledPartyId.setStatus(_B)
class _CctHistoryCallingPartyId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CctHistoryCallingPartyId_Type.__name__=_E
_CctHistoryCallingPartyId_Object=MibTableColumn
cctHistoryCallingPartyId=_CctHistoryCallingPartyId_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,25),_CctHistoryCallingPartyId_Type())
cctHistoryCallingPartyId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryCallingPartyId.setStatus(_B)
_CctHistoryMpBundleId_Type=Unsigned32
_CctHistoryMpBundleId_Object=MibTableColumn
cctHistoryMpBundleId=_CctHistoryMpBundleId_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,26),_CctHistoryMpBundleId_Type())
cctHistoryMpBundleId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryMpBundleId.setStatus(_B)
_CctHistoryChargedUnits_Type=Gauge32
_CctHistoryChargedUnits_Object=MibTableColumn
cctHistoryChargedUnits=_CctHistoryChargedUnits_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,27),_CctHistoryChargedUnits_Type())
cctHistoryChargedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryChargedUnits.setStatus(_B)
_CctHistoryReceiveBytes_Type=Gauge32
_CctHistoryReceiveBytes_Object=MibTableColumn
cctHistoryReceiveBytes=_CctHistoryReceiveBytes_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,28),_CctHistoryReceiveBytes_Type())
cctHistoryReceiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryReceiveBytes.setStatus(_B)
if mibBuilder.loadTexts:cctHistoryReceiveBytes.setUnits(_H)
_CctHistoryTransmitBytes_Type=Gauge32
_CctHistoryTransmitBytes_Object=MibTableColumn
cctHistoryTransmitBytes=_CctHistoryTransmitBytes_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,29),_CctHistoryTransmitBytes_Type())
cctHistoryTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryTransmitBytes.setStatus(_B)
if mibBuilder.loadTexts:cctHistoryTransmitBytes.setUnits(_H)
_CctHistoryDisconnectTime_Type=TimeStamp
_CctHistoryDisconnectTime_Object=MibTableColumn
cctHistoryDisconnectTime=_CctHistoryDisconnectTime_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,30),_CctHistoryDisconnectTime_Type())
cctHistoryDisconnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryDisconnectTime.setStatus(_B)
class _CctHistoryDisconnectReasonText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CctHistoryDisconnectReasonText_Type.__name__=_E
_CctHistoryDisconnectReasonText_Object=MibTableColumn
cctHistoryDisconnectReasonText=_CctHistoryDisconnectReasonText_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,31),_CctHistoryDisconnectReasonText_Type())
cctHistoryDisconnectReasonText.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryDisconnectReasonText.setStatus(_B)
_CctHistoryCallSignalingType_Type=CctCallSigType
_CctHistoryCallSignalingType_Object=MibTableColumn
cctHistoryCallSignalingType=_CctHistoryCallSignalingType_Object((1,3,6,1,4,1,9,9,163,1,3,7,1,32),_CctHistoryCallSignalingType_Type())
cctHistoryCallSignalingType.setMaxAccess(_C)
if mibBuilder.loadTexts:cctHistoryCallSignalingType.setStatus(_B)
_CctNotificationConfig_ObjectIdentity=ObjectIdentity
cctNotificationConfig=_CctNotificationConfig_ObjectIdentity((1,3,6,1,4,1,9,9,163,1,4))
_CctCallSetupTermNotifyEnable_Type=TruthValue
_CctCallSetupTermNotifyEnable_Object=MibScalar
cctCallSetupTermNotifyEnable=_CctCallSetupTermNotifyEnable_Object((1,3,6,1,4,1,9,9,163,1,4,1),_CctCallSetupTermNotifyEnable_Type())
cctCallSetupTermNotifyEnable.setMaxAccess(_N)
if mibBuilder.loadTexts:cctCallSetupTermNotifyEnable.setStatus(_B)
_CctMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cctMIBNotificationPrefix=_CctMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,163,2))
_CctMIBNotifications_ObjectIdentity=ObjectIdentity
cctMIBNotifications=_CctMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,163,2,0))
_CctMIBConformance_ObjectIdentity=ObjectIdentity
cctMIBConformance=_CctMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,163,3))
_CctMIBCompliances_ObjectIdentity=ObjectIdentity
cctMIBCompliances=_CctMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,163,3,1))
_CctMIBGroups_ObjectIdentity=ObjectIdentity
cctMIBGroups=_CctMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,163,3,2))
cctGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,163,3,2,1))
cctGeneralGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:cctGeneralGroup.setStatus(_B)
cctActiveGroup=ObjectGroup((1,3,6,1,4,1,9,9,163,3,2,2))
cctActiveGroup.setObjects(*((_A,_O),(_A,_P),(_A,_I),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_J),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_K),(_A,_L),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:cctActiveGroup.setStatus(_m)
cctHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,163,3,2,3))
cctHistoryGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_M),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:cctHistoryGroup.setStatus(_m)
cctNotificationConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,163,3,2,4))
cctNotificationConfigGroup.setObjects((_A,_AT))
if mibBuilder.loadTexts:cctNotificationConfigGroup.setStatus(_B)
cctActiveGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,163,3,2,6))
cctActiveGroupRev1.setObjects(*((_A,_O),(_A,_P),(_A,_I),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_J),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_K),(_A,_L),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_AU)))
if mibBuilder.loadTexts:cctActiveGroupRev1.setStatus(_B)
cctHistoryGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,163,3,2,7))
cctHistoryGroupRev1.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_M),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AV)))
if mibBuilder.loadTexts:cctHistoryGroupRev1.setStatus(_B)
cctCallSetupNotification=NotificationType((1,3,6,1,4,1,9,9,163,2,0,1))
cctCallSetupNotification.setObjects(*((_A,_I),(_A,_K),(_A,_L),(_A,_J)))
if mibBuilder.loadTexts:cctCallSetupNotification.setStatus(_B)
cctCallTerminateNotification=NotificationType((1,3,6,1,4,1,9,9,163,2,0,2))
cctCallTerminateNotification.setObjects((_A,_M))
if mibBuilder.loadTexts:cctCallTerminateNotification.setStatus(_B)
cctNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,163,3,2,5))
cctNotificationGroup.setObjects(*((_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:cctNotificationGroup.setStatus(_B)
cctMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,163,3,1,1))
cctMIBCompliance.setObjects(*((_A,_AL),(_A,_AY),(_A,_AZ),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cctMIBCompliance.setStatus(_m)
cctMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,163,3,1,2))
cctMIBComplianceRev1.setObjects(*((_A,_AL),(_A,_Aa),(_A,_Ab),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cctMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CctCallId':CctCallId,'CctServiceType':CctServiceType,'CctCallCategory':CctCallCategory,'CctCallSigType':CctCallSigType,'ciscoCallTrackerMIB':ciscoCallTrackerMIB,'cctMIBObjects':cctMIBObjects,'cctGeneral':cctGeneral,_AS:cctCallIdPrefix,'cctActive':cctActive,_O:cctActiveTableNumberEntries,_P:cctActiveTableHighWaterMark,'cctActiveTable':cctActiveTable,'cctActiveEntry':cctActiveEntry,_AO:cctActiveCallId,_I:cctActiveSetupTime,_Q:cctActiveOrigin,_R:cctActiveConnectionTime,_S:cctActivePhysicalLayerReadyTime,_T:cctActiveServiceUpTime,_U:cctActiveServiceType,_V:cctActiveUserValidationTime,_W:cctActiveUserId,_X:cctActiveUserIpAddr,_Y:cctActiveUserSubnetMask,_Z:cctActiveAccountingSessionId,_J:cctActiveCallCategory,_a:cctActiveInitialRxRate,_b:cctActiveInitialTxRate,_c:cctActiveResourceSlot,_d:cctActiveResourcePort,_e:cctActiveEntrySlot,_f:cctActiveEntryPort,_g:cctActiveEntryDs1,_h:cctActiveEntryChannel,_K:cctActiveCalledPartyId,_L:cctActiveCallingPartyId,_i:cctActiveMpBundleId,_j:cctActiveChargedUnits,_k:cctActiveReceiveBytes,_l:cctActiveTransmitBytes,_AU:cctActiveCallSignalingType,'cctHistory':cctHistory,_n:cctHistoryTableEntriesLimit,_o:cctHistoryTableMaxEntries,_p:cctHistoryTableRetainTimer,_q:cctHistoryTableNumberEntries,_r:cctHistoryTableHighWaterMark,_s:cctHistoryTableNewestIndex,'cctHistoryTable':cctHistoryTable,'cctHistoryEntry':cctHistoryEntry,_AR:cctHistoryIndex,_M:cctHistoryCallId,_t:cctHistorySetupTime,_u:cctHistoryOrigin,_v:cctHistoryConnectionTime,_w:cctHistoryPhysicalLayerReadyTime,_x:cctHistoryServiceUpTime,_y:cctHistoryServiceType,_z:cctHistoryUserValidationTime,_A0:cctHistoryUserId,_A1:cctHistoryUserIpAddr,_A2:cctHistoryUserSubnetMask,_A3:cctHistoryAccountingSessionId,_A4:cctHistoryCallCategory,_A5:cctHistoryInitialRxRate,_A6:cctHistoryInitialTxRate,_A7:cctHistoryResourceSlot,_A8:cctHistoryResourcePort,_A9:cctHistoryEntrySlot,_AA:cctHistoryEntryPort,_AB:cctHistoryEntryDs1,_AC:cctHistoryEntryChannel,_AD:cctHistoryCalledPartyId,_AE:cctHistoryCallingPartyId,_AF:cctHistoryMpBundleId,_AG:cctHistoryChargedUnits,_AH:cctHistoryReceiveBytes,_AI:cctHistoryTransmitBytes,_AJ:cctHistoryDisconnectTime,_AK:cctHistoryDisconnectReasonText,_AV:cctHistoryCallSignalingType,'cctNotificationConfig':cctNotificationConfig,_AT:cctCallSetupTermNotifyEnable,'cctMIBNotificationPrefix':cctMIBNotificationPrefix,'cctMIBNotifications':cctMIBNotifications,_AW:cctCallSetupNotification,_AX:cctCallTerminateNotification,'cctMIBConformance':cctMIBConformance,'cctMIBCompliances':cctMIBCompliances,'cctMIBCompliance':cctMIBCompliance,'cctMIBComplianceRev1':cctMIBComplianceRev1,'cctMIBGroups':cctMIBGroups,_AL:cctGeneralGroup,_AY:cctActiveGroup,_AZ:cctHistoryGroup,_AM:cctNotificationConfigGroup,_AN:cctNotificationGroup,_Aa:cctActiveGroupRev1,_Ab:cctHistoryGroupRev1})