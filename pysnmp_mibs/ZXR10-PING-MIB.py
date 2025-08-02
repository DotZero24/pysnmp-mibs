_O='zxr10PingCommResultRoundTripAvgTime'
_N='zxr10PingCommResultRoundTripMaxTime'
_M='zxr10PingCommResultRoundTripMinTime'
_L='zxr10PingCommResultRcvPkts'
_K='zxr10PingCommResultSentPkts'
_J='zxr10PingCommonSerial'
_I='TruthValue'
_H='zxr10PingCommResultSerial'
_G='none'
_F='DisplayString'
_E='ZXR10-PING-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,experimental,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','experimental','iso','mgmt')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
zxr10L2vpn,=mibBuilder.importSymbols('ZXR10-SMI','zxr10L2vpn')
class DisplayString(OctetString):0
_Zxr10PingMIB_ObjectIdentity=ObjectIdentity
zxr10PingMIB=_Zxr10PingMIB_ObjectIdentity((1,3,6,1,4,1,3902,3,104,2))
_Zxr10PingTable_Object=MibTable
zxr10PingTable=_Zxr10PingTable_Object((1,3,6,1,4,1,3902,3,104,2,1))
if mibBuilder.loadTexts:zxr10PingTable.setStatus(_A)
_Zxr10pingCommonEntry_Object=MibTableRow
zxr10pingCommonEntry=_Zxr10pingCommonEntry_Object((1,3,6,1,4,1,3902,3,104,2,1,1))
zxr10pingCommonEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:zxr10pingCommonEntry.setStatus(_A)
_Zxr10PingCommonSerial_Type=Integer32
_Zxr10PingCommonSerial_Object=MibTableColumn
zxr10PingCommonSerial=_Zxr10PingCommonSerial_Object((1,3,6,1,4,1,3902,3,104,2,1,1,1),_Zxr10PingCommonSerial_Type())
zxr10PingCommonSerial.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommonSerial.setStatus(_A)
class _Zxr10PingCommonPingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('common',0),('mng',1),('vrf',2)))
_Zxr10PingCommonPingType_Type.__name__=_C
_Zxr10PingCommonPingType_Object=MibTableColumn
zxr10PingCommonPingType=_Zxr10PingCommonPingType_Object((1,3,6,1,4,1,3902,3,104,2,1,1,2),_Zxr10PingCommonPingType_Type())
zxr10PingCommonPingType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonPingType.setStatus(_A)
_Zxr10PingCommonDestAddr_Type=IpAddress
_Zxr10PingCommonDestAddr_Object=MibTableColumn
zxr10PingCommonDestAddr=_Zxr10PingCommonDestAddr_Object((1,3,6,1,4,1,3902,3,104,2,1,1,3),_Zxr10PingCommonDestAddr_Type())
zxr10PingCommonDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonDestAddr.setStatus(_A)
class _Zxr10PingCommonVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Zxr10PingCommonVrfName_Type.__name__=_F
_Zxr10PingCommonVrfName_Object=MibTableColumn
zxr10PingCommonVrfName=_Zxr10PingCommonVrfName_Object((1,3,6,1,4,1,3902,3,104,2,1,1,4),_Zxr10PingCommonVrfName_Type())
zxr10PingCommonVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonVrfName.setStatus(_A)
class _Zxr10PingCommonIfOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('option',1)))
_Zxr10PingCommonIfOption_Type.__name__=_C
_Zxr10PingCommonIfOption_Object=MibTableColumn
zxr10PingCommonIfOption=_Zxr10PingCommonIfOption_Object((1,3,6,1,4,1,3902,3,104,2,1,1,5),_Zxr10PingCommonIfOption_Type())
zxr10PingCommonIfOption.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonIfOption.setStatus(_A)
_Zxr10PingCommonPacketCount_Type=Integer32
_Zxr10PingCommonPacketCount_Object=MibTableColumn
zxr10PingCommonPacketCount=_Zxr10PingCommonPacketCount_Object((1,3,6,1,4,1,3902,3,104,2,1,1,6),_Zxr10PingCommonPacketCount_Type())
zxr10PingCommonPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonPacketCount.setStatus(_A)
class _Zxr10PingCommonTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Zxr10PingCommonTimeOut_Type.__name__=_C
_Zxr10PingCommonTimeOut_Object=MibTableColumn
zxr10PingCommonTimeOut=_Zxr10PingCommonTimeOut_Object((1,3,6,1,4,1,3902,3,104,2,1,1,7),_Zxr10PingCommonTimeOut_Type())
zxr10PingCommonTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonTimeOut.setStatus(_A)
class _Zxr10PingCommonDataLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(36,8192))
_Zxr10PingCommonDataLen_Type.__name__=_C
_Zxr10PingCommonDataLen_Object=MibTableColumn
zxr10PingCommonDataLen=_Zxr10PingCommonDataLen_Object((1,3,6,1,4,1,3902,3,104,2,1,1,8),_Zxr10PingCommonDataLen_Type())
zxr10PingCommonDataLen.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonDataLen.setStatus(_A)
class _Zxr10PingCommonIfExtOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('extcom',1)))
_Zxr10PingCommonIfExtOption_Type.__name__=_C
_Zxr10PingCommonIfExtOption_Object=MibTableColumn
zxr10PingCommonIfExtOption=_Zxr10PingCommonIfExtOption_Object((1,3,6,1,4,1,3902,3,104,2,1,1,9),_Zxr10PingCommonIfExtOption_Type())
zxr10PingCommonIfExtOption.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonIfExtOption.setStatus(_A)
_Zxr10PingCommonExtSourceAddr_Type=IpAddress
_Zxr10PingCommonExtSourceAddr_Object=MibTableColumn
zxr10PingCommonExtSourceAddr=_Zxr10PingCommonExtSourceAddr_Object((1,3,6,1,4,1,3902,3,104,2,1,1,10),_Zxr10PingCommonExtSourceAddr_Type())
zxr10PingCommonExtSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtSourceAddr.setStatus(_A)
class _Zxr10PingCommonExtTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Zxr10PingCommonExtTos_Type.__name__=_C
_Zxr10PingCommonExtTos_Object=MibTableColumn
zxr10PingCommonExtTos=_Zxr10PingCommonExtTos_Object((1,3,6,1,4,1,3902,3,104,2,1,1,11),_Zxr10PingCommonExtTos_Type())
zxr10PingCommonExtTos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtTos.setStatus(_A)
class _Zxr10PingCommonExtTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Zxr10PingCommonExtTTL_Type.__name__=_C
_Zxr10PingCommonExtTTL_Object=MibTableColumn
zxr10PingCommonExtTTL=_Zxr10PingCommonExtTTL_Object((1,3,6,1,4,1,3902,3,104,2,1,1,12),_Zxr10PingCommonExtTTL_Type())
zxr10PingCommonExtTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtTTL.setStatus(_A)
class _Zxr10PingCommonExtFragement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Zxr10PingCommonExtFragement_Type.__name__=_C
_Zxr10PingCommonExtFragement_Object=MibTableColumn
zxr10PingCommonExtFragement=_Zxr10PingCommonExtFragement_Object((1,3,6,1,4,1,3902,3,104,2,1,1,13),_Zxr10PingCommonExtFragement_Type())
zxr10PingCommonExtFragement.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtFragement.setStatus(_A)
class _Zxr10PingCommonExtOpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),('loose',1),('record',2),('strict',3),('timestamp',4)))
_Zxr10PingCommonExtOpType_Type.__name__=_C
_Zxr10PingCommonExtOpType_Object=MibTableColumn
zxr10PingCommonExtOpType=_Zxr10PingCommonExtOpType_Object((1,3,6,1,4,1,3902,3,104,2,1,1,14),_Zxr10PingCommonExtOpType_Type())
zxr10PingCommonExtOpType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpType.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr1_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr1_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr1=_Zxr10PingCommonExtOpIpAddr1_Object((1,3,6,1,4,1,3902,3,104,2,1,1,15),_Zxr10PingCommonExtOpIpAddr1_Type())
zxr10PingCommonExtOpIpAddr1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr1.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr2_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr2_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr2=_Zxr10PingCommonExtOpIpAddr2_Object((1,3,6,1,4,1,3902,3,104,2,1,1,16),_Zxr10PingCommonExtOpIpAddr2_Type())
zxr10PingCommonExtOpIpAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr2.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr3_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr3_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr3=_Zxr10PingCommonExtOpIpAddr3_Object((1,3,6,1,4,1,3902,3,104,2,1,1,17),_Zxr10PingCommonExtOpIpAddr3_Type())
zxr10PingCommonExtOpIpAddr3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr3.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr4_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr4_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr4=_Zxr10PingCommonExtOpIpAddr4_Object((1,3,6,1,4,1,3902,3,104,2,1,1,18),_Zxr10PingCommonExtOpIpAddr4_Type())
zxr10PingCommonExtOpIpAddr4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr4.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr5_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr5_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr5=_Zxr10PingCommonExtOpIpAddr5_Object((1,3,6,1,4,1,3902,3,104,2,1,1,19),_Zxr10PingCommonExtOpIpAddr5_Type())
zxr10PingCommonExtOpIpAddr5.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr5.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr6_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr6_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr6=_Zxr10PingCommonExtOpIpAddr6_Object((1,3,6,1,4,1,3902,3,104,2,1,1,20),_Zxr10PingCommonExtOpIpAddr6_Type())
zxr10PingCommonExtOpIpAddr6.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr6.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr7_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr7_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr7=_Zxr10PingCommonExtOpIpAddr7_Object((1,3,6,1,4,1,3902,3,104,2,1,1,21),_Zxr10PingCommonExtOpIpAddr7_Type())
zxr10PingCommonExtOpIpAddr7.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr7.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr8_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr8_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr8=_Zxr10PingCommonExtOpIpAddr8_Object((1,3,6,1,4,1,3902,3,104,2,1,1,22),_Zxr10PingCommonExtOpIpAddr8_Type())
zxr10PingCommonExtOpIpAddr8.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr8.setStatus(_A)
_Zxr10PingCommonExtOpIpAddr9_Type=IpAddress
_Zxr10PingCommonExtOpIpAddr9_Object=MibTableColumn
zxr10PingCommonExtOpIpAddr9=_Zxr10PingCommonExtOpIpAddr9_Object((1,3,6,1,4,1,3902,3,104,2,1,1,23),_Zxr10PingCommonExtOpIpAddr9_Type())
zxr10PingCommonExtOpIpAddr9.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpIpAddr9.setStatus(_A)
class _Zxr10PingCommonExtOpRecordNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_Zxr10PingCommonExtOpRecordNum_Type.__name__=_C
_Zxr10PingCommonExtOpRecordNum_Object=MibTableColumn
zxr10PingCommonExtOpRecordNum=_Zxr10PingCommonExtOpRecordNum_Object((1,3,6,1,4,1,3902,3,104,2,1,1,24),_Zxr10PingCommonExtOpRecordNum_Type())
zxr10PingCommonExtOpRecordNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpRecordNum.setStatus(_A)
class _Zxr10PingCommonExtOpTimestampNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_Zxr10PingCommonExtOpTimestampNum_Type.__name__=_C
_Zxr10PingCommonExtOpTimestampNum_Object=MibTableColumn
zxr10PingCommonExtOpTimestampNum=_Zxr10PingCommonExtOpTimestampNum_Object((1,3,6,1,4,1,3902,3,104,2,1,1,25),_Zxr10PingCommonExtOpTimestampNum_Type())
zxr10PingCommonExtOpTimestampNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonExtOpTimestampNum.setStatus(_A)
class _Zxr10PingCommonRosStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-active',1),('start-ping',2),('ping-processing',3),('ping-completed',4)))
_Zxr10PingCommonRosStatus_Type.__name__=_C
_Zxr10PingCommonRosStatus_Object=MibTableColumn
zxr10PingCommonRosStatus=_Zxr10PingCommonRosStatus_Object((1,3,6,1,4,1,3902,3,104,2,1,1,26),_Zxr10PingCommonRosStatus_Type())
zxr10PingCommonRosStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonRosStatus.setStatus(_A)
_Zxr10PingCommonEntryOwner_Type=DisplayString
_Zxr10PingCommonEntryOwner_Object=MibTableColumn
zxr10PingCommonEntryOwner=_Zxr10PingCommonEntryOwner_Object((1,3,6,1,4,1,3902,3,104,2,1,1,27),_Zxr10PingCommonEntryOwner_Type())
zxr10PingCommonEntryOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonEntryOwner.setStatus(_A)
class _Zxr10PingCommonTrapOncompletion_Type(TruthValue):defaultValue=1
_Zxr10PingCommonTrapOncompletion_Type.__name__=_I
_Zxr10PingCommonTrapOncompletion_Object=MibTableColumn
zxr10PingCommonTrapOncompletion=_Zxr10PingCommonTrapOncompletion_Object((1,3,6,1,4,1,3902,3,104,2,1,1,28),_Zxr10PingCommonTrapOncompletion_Type())
zxr10PingCommonTrapOncompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingCommonTrapOncompletion.setStatus(_A)
_Zxr10PingResultTable_Object=MibTable
zxr10PingResultTable=_Zxr10PingResultTable_Object((1,3,6,1,4,1,3902,3,104,2,2))
if mibBuilder.loadTexts:zxr10PingResultTable.setStatus(_A)
_Zxr10pingResultEntry_Object=MibTableRow
zxr10pingResultEntry=_Zxr10pingResultEntry_Object((1,3,6,1,4,1,3902,3,104,2,2,1))
zxr10pingResultEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:zxr10pingResultEntry.setStatus(_A)
_Zxr10PingCommResultSerial_Type=Integer32
_Zxr10PingCommResultSerial_Object=MibTableColumn
zxr10PingCommResultSerial=_Zxr10PingCommResultSerial_Object((1,3,6,1,4,1,3902,3,104,2,2,1,1),_Zxr10PingCommResultSerial_Type())
zxr10PingCommResultSerial.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultSerial.setStatus(_A)
_Zxr10PingCommResultSentPkts_Type=Integer32
_Zxr10PingCommResultSentPkts_Object=MibTableColumn
zxr10PingCommResultSentPkts=_Zxr10PingCommResultSentPkts_Object((1,3,6,1,4,1,3902,3,104,2,2,1,2),_Zxr10PingCommResultSentPkts_Type())
zxr10PingCommResultSentPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultSentPkts.setStatus(_A)
_Zxr10PingCommResultRcvPkts_Type=Integer32
_Zxr10PingCommResultRcvPkts_Object=MibTableColumn
zxr10PingCommResultRcvPkts=_Zxr10PingCommResultRcvPkts_Object((1,3,6,1,4,1,3902,3,104,2,2,1,3),_Zxr10PingCommResultRcvPkts_Type())
zxr10PingCommResultRcvPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultRcvPkts.setStatus(_A)
_Zxr10PingCommResultRoundTripMinTime_Type=Integer32
_Zxr10PingCommResultRoundTripMinTime_Object=MibTableColumn
zxr10PingCommResultRoundTripMinTime=_Zxr10PingCommResultRoundTripMinTime_Object((1,3,6,1,4,1,3902,3,104,2,2,1,4),_Zxr10PingCommResultRoundTripMinTime_Type())
zxr10PingCommResultRoundTripMinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultRoundTripMinTime.setStatus(_A)
_Zxr10PingCommResultRoundTripMaxTime_Type=Integer32
_Zxr10PingCommResultRoundTripMaxTime_Object=MibTableColumn
zxr10PingCommResultRoundTripMaxTime=_Zxr10PingCommResultRoundTripMaxTime_Object((1,3,6,1,4,1,3902,3,104,2,2,1,5),_Zxr10PingCommResultRoundTripMaxTime_Type())
zxr10PingCommResultRoundTripMaxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultRoundTripMaxTime.setStatus(_A)
_Zxr10PingCommResultRoundTripAvgTime_Type=Integer32
_Zxr10PingCommResultRoundTripAvgTime_Object=MibTableColumn
zxr10PingCommResultRoundTripAvgTime=_Zxr10PingCommResultRoundTripAvgTime_Object((1,3,6,1,4,1,3902,3,104,2,2,1,6),_Zxr10PingCommResultRoundTripAvgTime_Type())
zxr10PingCommResultRoundTripAvgTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultRoundTripAvgTime.setStatus(_A)
_Zxr10PingCommExtResultTimeStampInfo_Type=DisplayString
_Zxr10PingCommExtResultTimeStampInfo_Object=MibTableColumn
zxr10PingCommExtResultTimeStampInfo=_Zxr10PingCommExtResultTimeStampInfo_Object((1,3,6,1,4,1,3902,3,104,2,2,1,7),_Zxr10PingCommExtResultTimeStampInfo_Type())
zxr10PingCommExtResultTimeStampInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommExtResultTimeStampInfo.setStatus(_A)
_Zxr10PingCommExtResultIpAddrInfo_Type=DisplayString
_Zxr10PingCommExtResultIpAddrInfo_Object=MibTableColumn
zxr10PingCommExtResultIpAddrInfo=_Zxr10PingCommExtResultIpAddrInfo_Object((1,3,6,1,4,1,3902,3,104,2,2,1,8),_Zxr10PingCommExtResultIpAddrInfo_Type())
zxr10PingCommExtResultIpAddrInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommExtResultIpAddrInfo.setStatus(_A)
_Zxr10PingCommResultEntryOwner_Type=DisplayString
_Zxr10PingCommResultEntryOwner_Object=MibTableColumn
zxr10PingCommResultEntryOwner=_Zxr10PingCommResultEntryOwner_Object((1,3,6,1,4,1,3902,3,104,2,2,1,9),_Zxr10PingCommResultEntryOwner_Type())
zxr10PingCommResultEntryOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultEntryOwner.setStatus(_A)
_Zxr10PingCommResultRoundWobbleMinTime_Type=Integer32
_Zxr10PingCommResultRoundWobbleMinTime_Object=MibTableColumn
zxr10PingCommResultRoundWobbleMinTime=_Zxr10PingCommResultRoundWobbleMinTime_Object((1,3,6,1,4,1,3902,3,104,2,2,1,10),_Zxr10PingCommResultRoundWobbleMinTime_Type())
zxr10PingCommResultRoundWobbleMinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultRoundWobbleMinTime.setStatus(_A)
_Zxr10PingCommResultRoundWobbleMaxTime_Type=Integer32
_Zxr10PingCommResultRoundWobbleMaxTime_Object=MibTableColumn
zxr10PingCommResultRoundWobbleMaxTime=_Zxr10PingCommResultRoundWobbleMaxTime_Object((1,3,6,1,4,1,3902,3,104,2,2,1,11),_Zxr10PingCommResultRoundWobbleMaxTime_Type())
zxr10PingCommResultRoundWobbleMaxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultRoundWobbleMaxTime.setStatus(_A)
_Zxr10PingCommResultRoundWobbleAvgTime_Type=Integer32
_Zxr10PingCommResultRoundWobbleAvgTime_Object=MibTableColumn
zxr10PingCommResultRoundWobbleAvgTime=_Zxr10PingCommResultRoundWobbleAvgTime_Object((1,3,6,1,4,1,3902,3,104,2,2,1,12),_Zxr10PingCommResultRoundWobbleAvgTime_Type())
zxr10PingCommResultRoundWobbleAvgTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxr10PingCommResultRoundWobbleAvgTime.setStatus(_A)
_PingNotifications_ObjectIdentity=ObjectIdentity
pingNotifications=_PingNotifications_ObjectIdentity((1,3,6,1,4,1,3902,3,104,2,3))
pingTrapResult=NotificationType((1,3,6,1,4,1,3902,3,104,2,3,1))
pingTrapResult.setObjects(*((_E,_H),(_E,_K),(_E,_L),(_E,_M),(_E,_N),(_E,_O)))
if mibBuilder.loadTexts:pingTrapResult.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_F:DisplayString,'zxr10PingMIB':zxr10PingMIB,'zxr10PingTable':zxr10PingTable,'zxr10pingCommonEntry':zxr10pingCommonEntry,_J:zxr10PingCommonSerial,'zxr10PingCommonPingType':zxr10PingCommonPingType,'zxr10PingCommonDestAddr':zxr10PingCommonDestAddr,'zxr10PingCommonVrfName':zxr10PingCommonVrfName,'zxr10PingCommonIfOption':zxr10PingCommonIfOption,'zxr10PingCommonPacketCount':zxr10PingCommonPacketCount,'zxr10PingCommonTimeOut':zxr10PingCommonTimeOut,'zxr10PingCommonDataLen':zxr10PingCommonDataLen,'zxr10PingCommonIfExtOption':zxr10PingCommonIfExtOption,'zxr10PingCommonExtSourceAddr':zxr10PingCommonExtSourceAddr,'zxr10PingCommonExtTos':zxr10PingCommonExtTos,'zxr10PingCommonExtTTL':zxr10PingCommonExtTTL,'zxr10PingCommonExtFragement':zxr10PingCommonExtFragement,'zxr10PingCommonExtOpType':zxr10PingCommonExtOpType,'zxr10PingCommonExtOpIpAddr1':zxr10PingCommonExtOpIpAddr1,'zxr10PingCommonExtOpIpAddr2':zxr10PingCommonExtOpIpAddr2,'zxr10PingCommonExtOpIpAddr3':zxr10PingCommonExtOpIpAddr3,'zxr10PingCommonExtOpIpAddr4':zxr10PingCommonExtOpIpAddr4,'zxr10PingCommonExtOpIpAddr5':zxr10PingCommonExtOpIpAddr5,'zxr10PingCommonExtOpIpAddr6':zxr10PingCommonExtOpIpAddr6,'zxr10PingCommonExtOpIpAddr7':zxr10PingCommonExtOpIpAddr7,'zxr10PingCommonExtOpIpAddr8':zxr10PingCommonExtOpIpAddr8,'zxr10PingCommonExtOpIpAddr9':zxr10PingCommonExtOpIpAddr9,'zxr10PingCommonExtOpRecordNum':zxr10PingCommonExtOpRecordNum,'zxr10PingCommonExtOpTimestampNum':zxr10PingCommonExtOpTimestampNum,'zxr10PingCommonRosStatus':zxr10PingCommonRosStatus,'zxr10PingCommonEntryOwner':zxr10PingCommonEntryOwner,'zxr10PingCommonTrapOncompletion':zxr10PingCommonTrapOncompletion,'zxr10PingResultTable':zxr10PingResultTable,'zxr10pingResultEntry':zxr10pingResultEntry,_H:zxr10PingCommResultSerial,_K:zxr10PingCommResultSentPkts,_L:zxr10PingCommResultRcvPkts,_M:zxr10PingCommResultRoundTripMinTime,_N:zxr10PingCommResultRoundTripMaxTime,_O:zxr10PingCommResultRoundTripAvgTime,'zxr10PingCommExtResultTimeStampInfo':zxr10PingCommExtResultTimeStampInfo,'zxr10PingCommExtResultIpAddrInfo':zxr10PingCommExtResultIpAddrInfo,'zxr10PingCommResultEntryOwner':zxr10PingCommResultEntryOwner,'zxr10PingCommResultRoundWobbleMinTime':zxr10PingCommResultRoundWobbleMinTime,'zxr10PingCommResultRoundWobbleMaxTime':zxr10PingCommResultRoundWobbleMaxTime,'zxr10PingCommResultRoundWobbleAvgTime':zxr10PingCommResultRoundWobbleAvgTime,'pingNotifications':pingNotifications,'pingTrapResult':pingTrapResult})