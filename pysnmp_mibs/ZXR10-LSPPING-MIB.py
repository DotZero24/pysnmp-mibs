_N='lspPingResultRoundTripAvgTime'
_M='lspPingResultRoundTripMaxTime'
_L='lspPingResultRoundTripMinTime'
_K='lspPingResultRcvPkts'
_J='lspPingResultSentPkts'
_I='lspPingSerial'
_H='TruthValue'
_G='DisplayString'
_F='lspPingResultSerial'
_E='Integer32'
_D='ZXR10-LSPPING-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,experimental,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','experimental','iso','mgmt')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
zxr10L2vpn,=mibBuilder.importSymbols('ZXR10-SMI','zxr10L2vpn')
class DisplayString(OctetString):0
_Zxr10LspPingMIB_ObjectIdentity=ObjectIdentity
zxr10LspPingMIB=_Zxr10LspPingMIB_ObjectIdentity((1,3,6,1,4,1,3902,3,104,5))
_LspPingTable_Object=MibTable
lspPingTable=_LspPingTable_Object((1,3,6,1,4,1,3902,3,104,5,1))
if mibBuilder.loadTexts:lspPingTable.setStatus(_A)
_LspPingEntry_Object=MibTableRow
lspPingEntry=_LspPingEntry_Object((1,3,6,1,4,1,3902,3,104,5,1,1))
lspPingEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:lspPingEntry.setStatus(_A)
_LspPingSerial_Type=Integer32
_LspPingSerial_Object=MibTableColumn
lspPingSerial=_LspPingSerial_Object((1,3,6,1,4,1,3902,3,104,5,1,1,1),_LspPingSerial_Type())
lspPingSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingSerial.setStatus(_A)
class _LspPingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ldp',0),('rsvp-te',1),('vccv',2)))
_LspPingType_Type.__name__=_E
_LspPingType_Object=MibTableColumn
lspPingType=_LspPingType_Object((1,3,6,1,4,1,3902,3,104,5,1,1,2),_LspPingType_Type())
lspPingType.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingType.setStatus(_A)
_LspPingLdpPrefix_Type=IpAddress
_LspPingLdpPrefix_Object=MibTableColumn
lspPingLdpPrefix=_LspPingLdpPrefix_Object((1,3,6,1,4,1,3902,3,104,5,1,1,3),_LspPingLdpPrefix_Type())
lspPingLdpPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingLdpPrefix.setStatus(_A)
_LspPingLdpPrefixlen_Type=Integer32
_LspPingLdpPrefixlen_Object=MibTableColumn
lspPingLdpPrefixlen=_LspPingLdpPrefixlen_Object((1,3,6,1,4,1,3902,3,104,5,1,1,4),_LspPingLdpPrefixlen_Type())
lspPingLdpPrefixlen.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingLdpPrefixlen.setStatus(_A)
_LspPingMplsTeTunnelIfName_Type=Integer32
_LspPingMplsTeTunnelIfName_Object=MibTableColumn
lspPingMplsTeTunnelIfName=_LspPingMplsTeTunnelIfName_Object((1,3,6,1,4,1,3902,3,104,5,1,1,5),_LspPingMplsTeTunnelIfName_Type())
lspPingMplsTeTunnelIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingMplsTeTunnelIfName.setStatus(_A)
_LspPingAtomDesAddr_Type=IpAddress
_LspPingAtomDesAddr_Object=MibTableColumn
lspPingAtomDesAddr=_LspPingAtomDesAddr_Object((1,3,6,1,4,1,3902,3,104,5,1,1,6),_LspPingAtomDesAddr_Type())
lspPingAtomDesAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingAtomDesAddr.setStatus(_A)
_LspPingAtomVcid_Type=Integer32
_LspPingAtomVcid_Object=MibTableColumn
lspPingAtomVcid=_LspPingAtomVcid_Object((1,3,6,1,4,1,3902,3,104,5,1,1,7),_LspPingAtomVcid_Type())
lspPingAtomVcid.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingAtomVcid.setStatus(_A)
class _LspPingIfOption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('option',1)))
_LspPingIfOption_Type.__name__=_E
_LspPingIfOption_Object=MibTableColumn
lspPingIfOption=_LspPingIfOption_Object((1,3,6,1,4,1,3902,3,104,5,1,1,8),_LspPingIfOption_Type())
lspPingIfOption.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingIfOption.setStatus(_A)
class _LspPingPacketCount_Type(Integer32):defaultValue=5
_LspPingPacketCount_Type.__name__=_E
_LspPingPacketCount_Object=MibTableColumn
lspPingPacketCount=_LspPingPacketCount_Object((1,3,6,1,4,1,3902,3,104,5,1,1,9),_LspPingPacketCount_Type())
lspPingPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingPacketCount.setStatus(_A)
class _LspPingTimeOut_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_LspPingTimeOut_Type.__name__=_E
_LspPingTimeOut_Object=MibTableColumn
lspPingTimeOut=_LspPingTimeOut_Object((1,3,6,1,4,1,3902,3,104,5,1,1,10),_LspPingTimeOut_Type())
lspPingTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingTimeOut.setStatus(_A)
class _LspPingDataLen_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,8192))
_LspPingDataLen_Type.__name__=_E
_LspPingDataLen_Object=MibTableColumn
lspPingDataLen=_LspPingDataLen_Object((1,3,6,1,4,1,3902,3,104,5,1,1,11),_LspPingDataLen_Type())
lspPingDataLen.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingDataLen.setStatus(_A)
class _LspPingTrapOncompletion_Type(TruthValue):defaultValue=1
_LspPingTrapOncompletion_Type.__name__=_H
_LspPingTrapOncompletion_Object=MibTableColumn
lspPingTrapOncompletion=_LspPingTrapOncompletion_Object((1,3,6,1,4,1,3902,3,104,5,1,1,12),_LspPingTrapOncompletion_Type())
lspPingTrapOncompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingTrapOncompletion.setStatus(_A)
class _LspPingRosStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-active',1),('start-ping',2),('ping-processing',3),('ping-completed',4)))
_LspPingRosStatus_Type.__name__=_E
_LspPingRosStatus_Object=MibTableColumn
lspPingRosStatus=_LspPingRosStatus_Object((1,3,6,1,4,1,3902,3,104,5,1,1,13),_LspPingRosStatus_Type())
lspPingRosStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingRosStatus.setStatus(_A)
_LspPingEntryOwner_Type=DisplayString
_LspPingEntryOwner_Object=MibTableColumn
lspPingEntryOwner=_LspPingEntryOwner_Object((1,3,6,1,4,1,3902,3,104,5,1,1,14),_LspPingEntryOwner_Type())
lspPingEntryOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:lspPingEntryOwner.setStatus(_A)
_LspPingResultTable_Object=MibTable
lspPingResultTable=_LspPingResultTable_Object((1,3,6,1,4,1,3902,3,104,5,2))
if mibBuilder.loadTexts:lspPingResultTable.setStatus(_A)
_LspPingResultEntry_Object=MibTableRow
lspPingResultEntry=_LspPingResultEntry_Object((1,3,6,1,4,1,3902,3,104,5,2,1))
lspPingResultEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lspPingResultEntry.setStatus(_A)
_LspPingResultSerial_Type=Integer32
_LspPingResultSerial_Object=MibTableColumn
lspPingResultSerial=_LspPingResultSerial_Object((1,3,6,1,4,1,3902,3,104,5,2,1,1),_LspPingResultSerial_Type())
lspPingResultSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultSerial.setStatus(_A)
_LspPingResultSentPkts_Type=Integer32
_LspPingResultSentPkts_Object=MibTableColumn
lspPingResultSentPkts=_LspPingResultSentPkts_Object((1,3,6,1,4,1,3902,3,104,5,2,1,2),_LspPingResultSentPkts_Type())
lspPingResultSentPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultSentPkts.setStatus(_A)
_LspPingResultRcvPkts_Type=Integer32
_LspPingResultRcvPkts_Object=MibTableColumn
lspPingResultRcvPkts=_LspPingResultRcvPkts_Object((1,3,6,1,4,1,3902,3,104,5,2,1,3),_LspPingResultRcvPkts_Type())
lspPingResultRcvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultRcvPkts.setStatus(_A)
_LspPingResultRoundTripMinTime_Type=Integer32
_LspPingResultRoundTripMinTime_Object=MibTableColumn
lspPingResultRoundTripMinTime=_LspPingResultRoundTripMinTime_Object((1,3,6,1,4,1,3902,3,104,5,2,1,4),_LspPingResultRoundTripMinTime_Type())
lspPingResultRoundTripMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultRoundTripMinTime.setStatus(_A)
_LspPingResultRoundTripMaxTime_Type=Integer32
_LspPingResultRoundTripMaxTime_Object=MibTableColumn
lspPingResultRoundTripMaxTime=_LspPingResultRoundTripMaxTime_Object((1,3,6,1,4,1,3902,3,104,5,2,1,5),_LspPingResultRoundTripMaxTime_Type())
lspPingResultRoundTripMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultRoundTripMaxTime.setStatus(_A)
_LspPingResultRoundTripAvgTime_Type=Integer32
_LspPingResultRoundTripAvgTime_Object=MibTableColumn
lspPingResultRoundTripAvgTime=_LspPingResultRoundTripAvgTime_Object((1,3,6,1,4,1,3902,3,104,5,2,1,6),_LspPingResultRoundTripAvgTime_Type())
lspPingResultRoundTripAvgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultRoundTripAvgTime.setStatus(_A)
_LspPingResultEntryOwner_Type=DisplayString
_LspPingResultEntryOwner_Object=MibTableColumn
lspPingResultEntryOwner=_LspPingResultEntryOwner_Object((1,3,6,1,4,1,3902,3,104,5,2,1,9),_LspPingResultEntryOwner_Type())
lspPingResultEntryOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultEntryOwner.setStatus(_A)
_LspPingResultRoundWobbleMinTime_Type=Integer32
_LspPingResultRoundWobbleMinTime_Object=MibTableColumn
lspPingResultRoundWobbleMinTime=_LspPingResultRoundWobbleMinTime_Object((1,3,6,1,4,1,3902,3,104,5,2,1,10),_LspPingResultRoundWobbleMinTime_Type())
lspPingResultRoundWobbleMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultRoundWobbleMinTime.setStatus(_A)
_LspPingResultRoundWobbleMaxTime_Type=Integer32
_LspPingResultRoundWobbleMaxTime_Object=MibTableColumn
lspPingResultRoundWobbleMaxTime=_LspPingResultRoundWobbleMaxTime_Object((1,3,6,1,4,1,3902,3,104,5,2,1,11),_LspPingResultRoundWobbleMaxTime_Type())
lspPingResultRoundWobbleMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultRoundWobbleMaxTime.setStatus(_A)
_LspPingResultRoundWobbleAvgTime_Type=Integer32
_LspPingResultRoundWobbleAvgTime_Object=MibTableColumn
lspPingResultRoundWobbleAvgTime=_LspPingResultRoundWobbleAvgTime_Object((1,3,6,1,4,1,3902,3,104,5,2,1,12),_LspPingResultRoundWobbleAvgTime_Type())
lspPingResultRoundWobbleAvgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lspPingResultRoundWobbleAvgTime.setStatus(_A)
_LsppingNotifications_ObjectIdentity=ObjectIdentity
lsppingNotifications=_LsppingNotifications_ObjectIdentity((1,3,6,1,4,1,3902,3,104,5,3))
lsppingTrapResult=NotificationType((1,3,6,1,4,1,3902,3,104,5,3,1))
lsppingTrapResult.setObjects(*((_D,_F),(_D,_J),(_D,_K),(_D,_L),(_D,_M),(_D,_N)))
if mibBuilder.loadTexts:lsppingTrapResult.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_G:DisplayString,'zxr10LspPingMIB':zxr10LspPingMIB,'lspPingTable':lspPingTable,'lspPingEntry':lspPingEntry,_I:lspPingSerial,'lspPingType':lspPingType,'lspPingLdpPrefix':lspPingLdpPrefix,'lspPingLdpPrefixlen':lspPingLdpPrefixlen,'lspPingMplsTeTunnelIfName':lspPingMplsTeTunnelIfName,'lspPingAtomDesAddr':lspPingAtomDesAddr,'lspPingAtomVcid':lspPingAtomVcid,'lspPingIfOption':lspPingIfOption,'lspPingPacketCount':lspPingPacketCount,'lspPingTimeOut':lspPingTimeOut,'lspPingDataLen':lspPingDataLen,'lspPingTrapOncompletion':lspPingTrapOncompletion,'lspPingRosStatus':lspPingRosStatus,'lspPingEntryOwner':lspPingEntryOwner,'lspPingResultTable':lspPingResultTable,'lspPingResultEntry':lspPingResultEntry,_F:lspPingResultSerial,_J:lspPingResultSentPkts,_K:lspPingResultRcvPkts,_L:lspPingResultRoundTripMinTime,_M:lspPingResultRoundTripMaxTime,_N:lspPingResultRoundTripAvgTime,'lspPingResultEntryOwner':lspPingResultEntryOwner,'lspPingResultRoundWobbleMinTime':lspPingResultRoundWobbleMinTime,'lspPingResultRoundWobbleMaxTime':lspPingResultRoundWobbleMaxTime,'lspPingResultRoundWobbleAvgTime':lspPingResultRoundWobbleAvgTime,'lsppingNotifications':lsppingNotifications,'lsppingTrapResult':lsppingTrapResult})