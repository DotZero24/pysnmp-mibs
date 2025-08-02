_P='zxr10PingMacResultRoundTripAvgTime'
_O='zxr10PingMacResultRoundTripMaxTime'
_N='zxr10PingMacResultRoundTripMinTime'
_M='zxr10PingMacResultRcvPkts'
_L='zxr10PingMacResultSentPkts'
_K='detail'
_J='summary'
_I='zxr10PingMacSerial'
_H='TruthValue'
_G='zxr10PingMacResultSerial'
_F='DisplayString'
_E='ZXR10-MACPING-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,experimental,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','experimental','iso','mgmt')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
zxr10L2vpn,=mibBuilder.importSymbols('ZXR10-SMI','zxr10L2vpn')
class DisplayString(OctetString):0
class OptionType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ce',0),('pe',1)))
_Zxr10MacPingMIB_ObjectIdentity=ObjectIdentity
zxr10MacPingMIB=_Zxr10MacPingMIB_ObjectIdentity((1,3,6,1,4,1,3902,3,104,4))
_Zxr10MacPingTable_Object=MibTable
zxr10MacPingTable=_Zxr10MacPingTable_Object((1,3,6,1,4,1,3902,3,104,4,1))
if mibBuilder.loadTexts:zxr10MacPingTable.setStatus(_A)
_Zxr10MacPingEntry_Object=MibTableRow
zxr10MacPingEntry=_Zxr10MacPingEntry_Object((1,3,6,1,4,1,3902,3,104,4,1,1))
zxr10MacPingEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:zxr10MacPingEntry.setStatus(_A)
_Zxr10PingMacSerial_Type=Integer32
_Zxr10PingMacSerial_Object=MibTableColumn
zxr10PingMacSerial=_Zxr10PingMacSerial_Object((1,3,6,1,4,1,3902,3,104,4,1,1,1),_Zxr10PingMacSerial_Type())
zxr10PingMacSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacSerial.setStatus(_A)
_Zxr10PingMacDestMac_Type=MacAddress
_Zxr10PingMacDestMac_Object=MibTableColumn
zxr10PingMacDestMac=_Zxr10PingMacDestMac_Object((1,3,6,1,4,1,3902,3,104,4,1,1,2),_Zxr10PingMacDestMac_Type())
zxr10PingMacDestMac.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacDestMac.setStatus(_A)
_Zxr10PingMacControlOutEtherIf_Type=Integer32
_Zxr10PingMacControlOutEtherIf_Object=MibTableColumn
zxr10PingMacControlOutEtherIf=_Zxr10PingMacControlOutEtherIf_Object((1,3,6,1,4,1,3902,3,104,4,1,1,3),_Zxr10PingMacControlOutEtherIf_Type())
zxr10PingMacControlOutEtherIf.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacControlOutEtherIf.setStatus(_A)
class _Zxr10PingMacIfOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('option',1)))
_Zxr10PingMacIfOption_Type.__name__=_D
_Zxr10PingMacIfOption_Object=MibTableColumn
zxr10PingMacIfOption=_Zxr10PingMacIfOption_Object((1,3,6,1,4,1,3902,3,104,4,1,1,4),_Zxr10PingMacIfOption_Type())
zxr10PingMacIfOption.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacIfOption.setStatus(_A)
_Zxr10PingMacPacketCount_Type=Integer32
_Zxr10PingMacPacketCount_Object=MibTableColumn
zxr10PingMacPacketCount=_Zxr10PingMacPacketCount_Object((1,3,6,1,4,1,3902,3,104,4,1,1,5),_Zxr10PingMacPacketCount_Type())
zxr10PingMacPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacPacketCount.setStatus(_A)
class _Zxr10PingMacTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Zxr10PingMacTimeOut_Type.__name__=_D
_Zxr10PingMacTimeOut_Object=MibTableColumn
zxr10PingMacTimeOut=_Zxr10PingMacTimeOut_Object((1,3,6,1,4,1,3902,3,104,4,1,1,6),_Zxr10PingMacTimeOut_Type())
zxr10PingMacTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacTimeOut.setStatus(_A)
class _Zxr10PingMacHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Zxr10PingMacHops_Type.__name__=_D
_Zxr10PingMacHops_Object=MibTableColumn
zxr10PingMacHops=_Zxr10PingMacHops_Object((1,3,6,1,4,1,3902,3,104,4,1,1,7),_Zxr10PingMacHops_Type())
zxr10PingMacHops.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacHops.setStatus(_A)
class _Zxr10PingMacControlResultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_Zxr10PingMacControlResultType_Type.__name__=_D
_Zxr10PingMacControlResultType_Object=MibTableColumn
zxr10PingMacControlResultType=_Zxr10PingMacControlResultType_Object((1,3,6,1,4,1,3902,3,104,4,1,1,8),_Zxr10PingMacControlResultType_Type())
zxr10PingMacControlResultType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacControlResultType.setStatus(_A)
class _Zxr10PingMacTrapOncompletion_Type(TruthValue):defaultValue=1
_Zxr10PingMacTrapOncompletion_Type.__name__=_H
_Zxr10PingMacTrapOncompletion_Object=MibTableColumn
zxr10PingMacTrapOncompletion=_Zxr10PingMacTrapOncompletion_Object((1,3,6,1,4,1,3902,3,104,4,1,1,9),_Zxr10PingMacTrapOncompletion_Type())
zxr10PingMacTrapOncompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacTrapOncompletion.setStatus(_A)
class _Zxr10PingMacRosStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-active',1),('start-ping',2),('ping-processing',3),('ping-completed',4)))
_Zxr10PingMacRosStatus_Type.__name__=_D
_Zxr10PingMacRosStatus_Object=MibTableColumn
zxr10PingMacRosStatus=_Zxr10PingMacRosStatus_Object((1,3,6,1,4,1,3902,3,104,4,1,1,10),_Zxr10PingMacRosStatus_Type())
zxr10PingMacRosStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacRosStatus.setStatus(_A)
_Zxr10PingMacEntryOwner_Type=DisplayString
_Zxr10PingMacEntryOwner_Object=MibTableColumn
zxr10PingMacEntryOwner=_Zxr10PingMacEntryOwner_Object((1,3,6,1,4,1,3902,3,104,4,1,1,11),_Zxr10PingMacEntryOwner_Type())
zxr10PingMacEntryOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacEntryOwner.setStatus(_A)
_Zxr10PingMacIfPeOption_Type=OptionType
_Zxr10PingMacIfPeOption_Object=MibTableColumn
zxr10PingMacIfPeOption=_Zxr10PingMacIfPeOption_Object((1,3,6,1,4,1,3902,3,104,4,1,1,12),_Zxr10PingMacIfPeOption_Type())
zxr10PingMacIfPeOption.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacIfPeOption.setStatus(_A)
_Zxr10PingMacVfiName_Type=DisplayString
_Zxr10PingMacVfiName_Object=MibTableColumn
zxr10PingMacVfiName=_Zxr10PingMacVfiName_Object((1,3,6,1,4,1,3902,3,104,4,1,1,13),_Zxr10PingMacVfiName_Type())
zxr10PingMacVfiName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacVfiName.setStatus(_A)
_Zxr10PingMacPeerAddress_Type=IpAddress
_Zxr10PingMacPeerAddress_Object=MibTableColumn
zxr10PingMacPeerAddress=_Zxr10PingMacPeerAddress_Object((1,3,6,1,4,1,3902,3,104,4,1,1,14),_Zxr10PingMacPeerAddress_Type())
zxr10PingMacPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10PingMacPeerAddress.setStatus(_A)
_Zxr10PingMacResultTable_Object=MibTable
zxr10PingMacResultTable=_Zxr10PingMacResultTable_Object((1,3,6,1,4,1,3902,3,104,4,2))
if mibBuilder.loadTexts:zxr10PingMacResultTable.setStatus(_A)
_Zxr10pingMacResultEntry_Object=MibTableRow
zxr10pingMacResultEntry=_Zxr10pingMacResultEntry_Object((1,3,6,1,4,1,3902,3,104,4,2,1))
zxr10pingMacResultEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:zxr10pingMacResultEntry.setStatus(_A)
_Zxr10PingMacResultSerial_Type=Integer32
_Zxr10PingMacResultSerial_Object=MibTableColumn
zxr10PingMacResultSerial=_Zxr10PingMacResultSerial_Object((1,3,6,1,4,1,3902,3,104,4,2,1,1),_Zxr10PingMacResultSerial_Type())
zxr10PingMacResultSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultSerial.setStatus(_A)
_Zxr10PingMacResultSentPkts_Type=Integer32
_Zxr10PingMacResultSentPkts_Object=MibTableColumn
zxr10PingMacResultSentPkts=_Zxr10PingMacResultSentPkts_Object((1,3,6,1,4,1,3902,3,104,4,2,1,2),_Zxr10PingMacResultSentPkts_Type())
zxr10PingMacResultSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultSentPkts.setStatus(_A)
_Zxr10PingMacResultRcvPkts_Type=Integer32
_Zxr10PingMacResultRcvPkts_Object=MibTableColumn
zxr10PingMacResultRcvPkts=_Zxr10PingMacResultRcvPkts_Object((1,3,6,1,4,1,3902,3,104,4,2,1,3),_Zxr10PingMacResultRcvPkts_Type())
zxr10PingMacResultRcvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultRcvPkts.setStatus(_A)
_Zxr10PingMacResultRoundTripMinTime_Type=Integer32
_Zxr10PingMacResultRoundTripMinTime_Object=MibTableColumn
zxr10PingMacResultRoundTripMinTime=_Zxr10PingMacResultRoundTripMinTime_Object((1,3,6,1,4,1,3902,3,104,4,2,1,4),_Zxr10PingMacResultRoundTripMinTime_Type())
zxr10PingMacResultRoundTripMinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultRoundTripMinTime.setStatus(_A)
_Zxr10PingMacResultRoundTripMaxTime_Type=Integer32
_Zxr10PingMacResultRoundTripMaxTime_Object=MibTableColumn
zxr10PingMacResultRoundTripMaxTime=_Zxr10PingMacResultRoundTripMaxTime_Object((1,3,6,1,4,1,3902,3,104,4,2,1,5),_Zxr10PingMacResultRoundTripMaxTime_Type())
zxr10PingMacResultRoundTripMaxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultRoundTripMaxTime.setStatus(_A)
_Zxr10PingMacResultRoundTripAvgTime_Type=Integer32
_Zxr10PingMacResultRoundTripAvgTime_Object=MibTableColumn
zxr10PingMacResultRoundTripAvgTime=_Zxr10PingMacResultRoundTripAvgTime_Object((1,3,6,1,4,1,3902,3,104,4,2,1,6),_Zxr10PingMacResultRoundTripAvgTime_Type())
zxr10PingMacResultRoundTripAvgTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultRoundTripAvgTime.setStatus(_A)
class _Zxr10PingMacResultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_Zxr10PingMacResultType_Type.__name__=_D
_Zxr10PingMacResultType_Object=MibTableColumn
zxr10PingMacResultType=_Zxr10PingMacResultType_Object((1,3,6,1,4,1,3902,3,104,4,2,1,7),_Zxr10PingMacResultType_Type())
zxr10PingMacResultType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultType.setStatus(_A)
class _Zxr10PingMacExtResultDestIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10PingMacExtResultDestIfName_Type.__name__=_F
_Zxr10PingMacExtResultDestIfName_Object=MibTableColumn
zxr10PingMacExtResultDestIfName=_Zxr10PingMacExtResultDestIfName_Object((1,3,6,1,4,1,3902,3,104,4,2,1,8),_Zxr10PingMacExtResultDestIfName_Type())
zxr10PingMacExtResultDestIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacExtResultDestIfName.setStatus(_A)
class _Zxr10PingMacExtResultDestHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_Zxr10PingMacExtResultDestHostName_Type.__name__=_F
_Zxr10PingMacExtResultDestHostName_Object=MibTableColumn
zxr10PingMacExtResultDestHostName=_Zxr10PingMacExtResultDestHostName_Object((1,3,6,1,4,1,3902,3,104,4,2,1,9),_Zxr10PingMacExtResultDestHostName_Type())
zxr10PingMacExtResultDestHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacExtResultDestHostName.setStatus(_A)
class _Zxr10PingMacExtResultSourceIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10PingMacExtResultSourceIfName_Type.__name__=_F
_Zxr10PingMacExtResultSourceIfName_Object=MibTableColumn
zxr10PingMacExtResultSourceIfName=_Zxr10PingMacExtResultSourceIfName_Object((1,3,6,1,4,1,3902,3,104,4,2,1,10),_Zxr10PingMacExtResultSourceIfName_Type())
zxr10PingMacExtResultSourceIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacExtResultSourceIfName.setStatus(_A)
class _Zxr10PingMacExtResultSourceHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_Zxr10PingMacExtResultSourceHostName_Type.__name__=_F
_Zxr10PingMacExtResultSourceHostName_Object=MibTableColumn
zxr10PingMacExtResultSourceHostName=_Zxr10PingMacExtResultSourceHostName_Object((1,3,6,1,4,1,3902,3,104,4,2,1,11),_Zxr10PingMacExtResultSourceHostName_Type())
zxr10PingMacExtResultSourceHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacExtResultSourceHostName.setStatus(_A)
class _Zxr10PingMacExtResultOutVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_Zxr10PingMacExtResultOutVlanId_Type.__name__=_D
_Zxr10PingMacExtResultOutVlanId_Object=MibTableColumn
zxr10PingMacExtResultOutVlanId=_Zxr10PingMacExtResultOutVlanId_Object((1,3,6,1,4,1,3902,3,104,4,2,1,12),_Zxr10PingMacExtResultOutVlanId_Type())
zxr10PingMacExtResultOutVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacExtResultOutVlanId.setStatus(_A)
class _Zxr10PingMacExtResultInVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_Zxr10PingMacExtResultInVlanId_Type.__name__=_D
_Zxr10PingMacExtResultInVlanId_Object=MibTableColumn
zxr10PingMacExtResultInVlanId=_Zxr10PingMacExtResultInVlanId_Object((1,3,6,1,4,1,3902,3,104,4,2,1,13),_Zxr10PingMacExtResultInVlanId_Type())
zxr10PingMacExtResultInVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacExtResultInVlanId.setStatus(_A)
_Zxr10PingMacResultEntryOwner_Type=DisplayString
_Zxr10PingMacResultEntryOwner_Object=MibTableColumn
zxr10PingMacResultEntryOwner=_Zxr10PingMacResultEntryOwner_Object((1,3,6,1,4,1,3902,3,104,4,2,1,14),_Zxr10PingMacResultEntryOwner_Type())
zxr10PingMacResultEntryOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultEntryOwner.setStatus(_A)
_Zxr10PingMacResultRoundWobbleMinTime_Type=Integer32
_Zxr10PingMacResultRoundWobbleMinTime_Object=MibTableColumn
zxr10PingMacResultRoundWobbleMinTime=_Zxr10PingMacResultRoundWobbleMinTime_Object((1,3,6,1,4,1,3902,3,104,4,2,1,15),_Zxr10PingMacResultRoundWobbleMinTime_Type())
zxr10PingMacResultRoundWobbleMinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultRoundWobbleMinTime.setStatus(_A)
_Zxr10PingMacResultRoundWobbleMaxTime_Type=Integer32
_Zxr10PingMacResultRoundWobbleMaxTime_Object=MibTableColumn
zxr10PingMacResultRoundWobbleMaxTime=_Zxr10PingMacResultRoundWobbleMaxTime_Object((1,3,6,1,4,1,3902,3,104,4,2,1,16),_Zxr10PingMacResultRoundWobbleMaxTime_Type())
zxr10PingMacResultRoundWobbleMaxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultRoundWobbleMaxTime.setStatus(_A)
_Zxr10PingMacResultRoundWobbleAvgTime_Type=Integer32
_Zxr10PingMacResultRoundWobbleAvgTime_Object=MibTableColumn
zxr10PingMacResultRoundWobbleAvgTime=_Zxr10PingMacResultRoundWobbleAvgTime_Object((1,3,6,1,4,1,3902,3,104,4,2,1,17),_Zxr10PingMacResultRoundWobbleAvgTime_Type())
zxr10PingMacResultRoundWobbleAvgTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PingMacResultRoundWobbleAvgTime.setStatus(_A)
_MacpingNotifications_ObjectIdentity=ObjectIdentity
macpingNotifications=_MacpingNotifications_ObjectIdentity((1,3,6,1,4,1,3902,3,104,4,3))
macpingTrapResult=NotificationType((1,3,6,1,4,1,3902,3,104,4,3,1))
macpingTrapResult.setObjects(*((_E,_G),(_E,_L),(_E,_M),(_E,_N),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:macpingTrapResult.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_F:DisplayString,'OptionType':OptionType,'zxr10MacPingMIB':zxr10MacPingMIB,'zxr10MacPingTable':zxr10MacPingTable,'zxr10MacPingEntry':zxr10MacPingEntry,_I:zxr10PingMacSerial,'zxr10PingMacDestMac':zxr10PingMacDestMac,'zxr10PingMacControlOutEtherIf':zxr10PingMacControlOutEtherIf,'zxr10PingMacIfOption':zxr10PingMacIfOption,'zxr10PingMacPacketCount':zxr10PingMacPacketCount,'zxr10PingMacTimeOut':zxr10PingMacTimeOut,'zxr10PingMacHops':zxr10PingMacHops,'zxr10PingMacControlResultType':zxr10PingMacControlResultType,'zxr10PingMacTrapOncompletion':zxr10PingMacTrapOncompletion,'zxr10PingMacRosStatus':zxr10PingMacRosStatus,'zxr10PingMacEntryOwner':zxr10PingMacEntryOwner,'zxr10PingMacIfPeOption':zxr10PingMacIfPeOption,'zxr10PingMacVfiName':zxr10PingMacVfiName,'zxr10PingMacPeerAddress':zxr10PingMacPeerAddress,'zxr10PingMacResultTable':zxr10PingMacResultTable,'zxr10pingMacResultEntry':zxr10pingMacResultEntry,_G:zxr10PingMacResultSerial,_L:zxr10PingMacResultSentPkts,_M:zxr10PingMacResultRcvPkts,_N:zxr10PingMacResultRoundTripMinTime,_O:zxr10PingMacResultRoundTripMaxTime,_P:zxr10PingMacResultRoundTripAvgTime,'zxr10PingMacResultType':zxr10PingMacResultType,'zxr10PingMacExtResultDestIfName':zxr10PingMacExtResultDestIfName,'zxr10PingMacExtResultDestHostName':zxr10PingMacExtResultDestHostName,'zxr10PingMacExtResultSourceIfName':zxr10PingMacExtResultSourceIfName,'zxr10PingMacExtResultSourceHostName':zxr10PingMacExtResultSourceHostName,'zxr10PingMacExtResultOutVlanId':zxr10PingMacExtResultOutVlanId,'zxr10PingMacExtResultInVlanId':zxr10PingMacExtResultInVlanId,'zxr10PingMacResultEntryOwner':zxr10PingMacResultEntryOwner,'zxr10PingMacResultRoundWobbleMinTime':zxr10PingMacResultRoundWobbleMinTime,'zxr10PingMacResultRoundWobbleMaxTime':zxr10PingMacResultRoundWobbleMaxTime,'zxr10PingMacResultRoundWobbleAvgTime':zxr10PingMacResultRoundWobbleAvgTime,'macpingNotifications':macpingNotifications,'macpingTrapResult':macpingTrapResult})