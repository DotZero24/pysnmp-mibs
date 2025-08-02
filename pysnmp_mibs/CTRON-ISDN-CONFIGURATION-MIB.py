_S='callHistoryIndex'
_R='disabled'
_Q='enabled'
_P='rmtProfileEntryIndex'
_O='dialCtlNbrCfgIndex'
_N='dialCtlNbrCfgId'
_M='pri5ESS'
_L='pri4ESS'
_K='brini1'
_J='bridms100'
_I='bri5ESS'
_H='isdnDchIndex'
_G='DisplayString'
_F='CTRON-ISDN-CONFIGURATION-MIB'
_E='OctetString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,52,4))
_Ctron_ObjectIdentity=ObjectIdentity
ctron=_Ctron_ObjectIdentity((1,3,6,1,4,1,52,4,1))
_CtDataLink_ObjectIdentity=ObjectIdentity
ctDataLink=_CtDataLink_ObjectIdentity((1,3,6,1,4,1,52,4,1,2))
_CtronWan_ObjectIdentity=ObjectIdentity
ctronWan=_CtronWan_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7))
_CtISDNconfigMib_ObjectIdentity=ObjectIdentity
ctISDNconfigMib=_CtISDNconfigMib_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,4))
_CtISDNcontrol_ObjectIdentity=ObjectIdentity
ctISDNcontrol=_CtISDNcontrol_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,4,1))
_IsdnDchTable_Object=MibTable
isdnDchTable=_IsdnDchTable_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1))
if mibBuilder.loadTexts:isdnDchTable.setStatus(_A)
_IsdnDchEntry_Object=MibTableRow
isdnDchEntry=_IsdnDchEntry_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1))
isdnDchEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:isdnDchEntry.setStatus(_A)
_IsdnDchIndex_Type=Integer32
_IsdnDchIndex_Object=MibTableColumn
isdnDchIndex=_IsdnDchIndex_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,1),_IsdnDchIndex_Type())
isdnDchIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnDchIndex.setStatus(_A)
class _IsdnDchRateAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('bri1',2),('pri1',3),('pri2',4)))
_IsdnDchRateAccess_Type.__name__=_B
_IsdnDchRateAccess_Object=MibTableColumn
isdnDchRateAccess=_IsdnDchRateAccess_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,2),_IsdnDchRateAccess_Type())
isdnDchRateAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnDchRateAccess.setStatus(_A)
_IsdnDchAllowedCh_Type=Integer32
_IsdnDchAllowedCh_Object=MibTableColumn
isdnDchAllowedCh=_IsdnDchAllowedCh_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,3),_IsdnDchAllowedCh_Type())
isdnDchAllowedCh.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnDchAllowedCh.setStatus(_A)
_IsdnDchChInUse_Type=Integer32
_IsdnDchChInUse_Object=MibTableColumn
isdnDchChInUse=_IsdnDchChInUse_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,4),_IsdnDchChInUse_Type())
isdnDchChInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnDchChInUse.setStatus(_A)
class _IsdnDchSupportedSwitches_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,5,10,16,17)));namedValues=NamedValues(*((_I,2),(_J,5),(_K,10),(_L,16),(_M,17)))
_IsdnDchSupportedSwitches_Type.__name__=_B
_IsdnDchSupportedSwitches_Object=MibTableColumn
isdnDchSupportedSwitches=_IsdnDchSupportedSwitches_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,5),_IsdnDchSupportedSwitches_Type())
isdnDchSupportedSwitches.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnDchSupportedSwitches.setStatus(_A)
class _IsdnDchSwitchType_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,5,10,16,17)));namedValues=NamedValues(*((_I,2),(_J,5),(_K,10),(_L,16),(_M,17)))
_IsdnDchSwitchType_Type.__name__=_B
_IsdnDchSwitchType_Object=MibTableColumn
isdnDchSwitchType=_IsdnDchSwitchType_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,6),_IsdnDchSwitchType_Type())
isdnDchSwitchType.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDchSwitchType.setStatus(_A)
class _IsdnDchSPID1_Type(OctetString):defaultValue=OctetString('')
_IsdnDchSPID1_Type.__name__=_E
_IsdnDchSPID1_Object=MibTableColumn
isdnDchSPID1=_IsdnDchSPID1_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,7),_IsdnDchSPID1_Type())
isdnDchSPID1.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDchSPID1.setStatus(_A)
class _IsdnDchSPID2_Type(OctetString):defaultValue=OctetString('')
_IsdnDchSPID2_Type.__name__=_E
_IsdnDchSPID2_Object=MibTableColumn
isdnDchSPID2=_IsdnDchSPID2_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,8),_IsdnDchSPID2_Type())
isdnDchSPID2.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDchSPID2.setStatus(_A)
class _IsdnDchDirNum1_Type(OctetString):defaultValue=OctetString('')
_IsdnDchDirNum1_Type.__name__=_E
_IsdnDchDirNum1_Object=MibTableColumn
isdnDchDirNum1=_IsdnDchDirNum1_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,9),_IsdnDchDirNum1_Type())
isdnDchDirNum1.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDchDirNum1.setStatus(_A)
class _IsdnDchDirNum2_Type(OctetString):defaultValue=OctetString('')
_IsdnDchDirNum2_Type.__name__=_E
_IsdnDchDirNum2_Object=MibTableColumn
isdnDchDirNum2=_IsdnDchDirNum2_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,10),_IsdnDchDirNum2_Type())
isdnDchDirNum2.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnDchDirNum2.setStatus(_A)
class _IsdnDchOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_IsdnDchOperStatus_Type.__name__=_B
_IsdnDchOperStatus_Object=MibTableColumn
isdnDchOperStatus=_IsdnDchOperStatus_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,1,1,11),_IsdnDchOperStatus_Type())
isdnDchOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnDchOperStatus.setStatus(_A)
_DialCtlNbrCfgTable_Object=MibTable
dialCtlNbrCfgTable=_DialCtlNbrCfgTable_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,2))
if mibBuilder.loadTexts:dialCtlNbrCfgTable.setStatus(_A)
_DialCtlNbrCfgEntry_Object=MibTableRow
dialCtlNbrCfgEntry=_DialCtlNbrCfgEntry_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,2,1))
dialCtlNbrCfgEntry.setIndexNames((0,_F,_N),(0,_F,_O))
if mibBuilder.loadTexts:dialCtlNbrCfgEntry.setStatus(_A)
class _DialCtlNbrCfgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_DialCtlNbrCfgId_Type.__name__=_B
_DialCtlNbrCfgId_Object=MibTableColumn
dialCtlNbrCfgId=_DialCtlNbrCfgId_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,2,1,1),_DialCtlNbrCfgId_Type())
dialCtlNbrCfgId.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlNbrCfgId.setStatus(_A)
class _DialCtlNbrCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_DialCtlNbrCfgIndex_Type.__name__=_B
_DialCtlNbrCfgIndex_Object=MibTableColumn
dialCtlNbrCfgIndex=_DialCtlNbrCfgIndex_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,2,1,2),_DialCtlNbrCfgIndex_Type())
dialCtlNbrCfgIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlNbrCfgIndex.setStatus(_A)
class _DialCtlNbrCfgIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DialCtlNbrCfgIfIndex_Type.__name__=_B
_DialCtlNbrCfgIfIndex_Object=MibTableColumn
dialCtlNbrCfgIfIndex=_DialCtlNbrCfgIfIndex_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,2,1,3),_DialCtlNbrCfgIfIndex_Type())
dialCtlNbrCfgIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlNbrCfgIfIndex.setStatus(_A)
class _DialCtlNbrCfgOriginateAddress_Type(DisplayString):defaultValue=OctetString('')
_DialCtlNbrCfgOriginateAddress_Type.__name__=_G
_DialCtlNbrCfgOriginateAddress_Object=MibTableColumn
dialCtlNbrCfgOriginateAddress=_DialCtlNbrCfgOriginateAddress_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,2,1,4),_DialCtlNbrCfgOriginateAddress_Type())
dialCtlNbrCfgOriginateAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dialCtlNbrCfgOriginateAddress.setStatus(_A)
class _DialCtlNbrCfgAnswerAddress_Type(DisplayString):defaultValue=OctetString('')
_DialCtlNbrCfgAnswerAddress_Type.__name__=_G
_DialCtlNbrCfgAnswerAddress_Object=MibTableColumn
dialCtlNbrCfgAnswerAddress=_DialCtlNbrCfgAnswerAddress_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,2,1,5),_DialCtlNbrCfgAnswerAddress_Type())
dialCtlNbrCfgAnswerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dialCtlNbrCfgAnswerAddress.setStatus(_A)
_RmtProfileTable_Object=MibTable
rmtProfileTable=_RmtProfileTable_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3))
if mibBuilder.loadTexts:rmtProfileTable.setStatus(_A)
_RmtProfileEntry_Object=MibTableRow
rmtProfileEntry=_RmtProfileEntry_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1))
rmtProfileEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:rmtProfileEntry.setStatus(_A)
class _RmtProfileEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_RmtProfileEntryIndex_Type.__name__=_B
_RmtProfileEntryIndex_Object=MibTableColumn
rmtProfileEntryIndex=_RmtProfileEntryIndex_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,1),_RmtProfileEntryIndex_Type())
rmtProfileEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmtProfileEntryIndex.setStatus(_A)
class _RmtProfileEntryName_Type(OctetString):defaultValue=OctetString('')
_RmtProfileEntryName_Type.__name__=_E
_RmtProfileEntryName_Object=MibTableColumn
rmtProfileEntryName=_RmtProfileEntryName_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,2),_RmtProfileEntryName_Type())
rmtProfileEntryName.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryName.setStatus(_A)
class _RmtProfileEntryMakerName_Type(OctetString):defaultValue=OctetString('')
_RmtProfileEntryMakerName_Type.__name__=_E
_RmtProfileEntryMakerName_Object=MibTableColumn
rmtProfileEntryMakerName=_RmtProfileEntryMakerName_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,3),_RmtProfileEntryMakerName_Type())
rmtProfileEntryMakerName.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMakerName.setStatus(_A)
class _RmtProfileEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('connect',2),('hangup',3)))
_RmtProfileEntryAction_Type.__name__=_B
_RmtProfileEntryAction_Object=MibTableColumn
rmtProfileEntryAction=_RmtProfileEntryAction_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,4),_RmtProfileEntryAction_Type())
rmtProfileEntryAction.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryAction.setStatus(_A)
class _RmtProfileEntryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('calling',2),('ringing',3),('connected',4),('answering',5),('answered',6)))
_RmtProfileEntryState_Type.__name__=_B
_RmtProfileEntryState_Object=MibTableColumn
rmtProfileEntryState=_RmtProfileEntryState_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,5),_RmtProfileEntryState_Type())
rmtProfileEntryState.setMaxAccess(_C)
if mibBuilder.loadTexts:rmtProfileEntryState.setStatus(_A)
class _RmtProfileEntryMaxNeighbor_Type(Integer32):defaultValue=1
_RmtProfileEntryMaxNeighbor_Type.__name__=_B
_RmtProfileEntryMaxNeighbor_Object=MibTableColumn
rmtProfileEntryMaxNeighbor=_RmtProfileEntryMaxNeighbor_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,6),_RmtProfileEntryMaxNeighbor_Type())
rmtProfileEntryMaxNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:rmtProfileEntryMaxNeighbor.setStatus(_A)
_RmtProfileEntryBchInUse_Type=Integer32
_RmtProfileEntryBchInUse_Object=MibTableColumn
rmtProfileEntryBchInUse=_RmtProfileEntryBchInUse_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,7),_RmtProfileEntryBchInUse_Type())
rmtProfileEntryBchInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rmtProfileEntryBchInUse.setStatus(_A)
class _RmtProfileEntryLinkHead_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_RmtProfileEntryLinkHead_Type.__name__=_B
_RmtProfileEntryLinkHead_Object=MibTableColumn
rmtProfileEntryLinkHead=_RmtProfileEntryLinkHead_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,8),_RmtProfileEntryLinkHead_Type())
rmtProfileEntryLinkHead.setMaxAccess(_C)
if mibBuilder.loadTexts:rmtProfileEntryLinkHead.setStatus(_A)
class _RmtProfileEntryNextLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_RmtProfileEntryNextLink_Type.__name__=_B
_RmtProfileEntryNextLink_Object=MibTableColumn
rmtProfileEntryNextLink=_RmtProfileEntryNextLink_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,9),_RmtProfileEntryNextLink_Type())
rmtProfileEntryNextLink.setMaxAccess(_C)
if mibBuilder.loadTexts:rmtProfileEntryNextLink.setStatus(_A)
class _RmtProfileEntryMpCapable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RmtProfileEntryMpCapable_Type.__name__=_B
_RmtProfileEntryMpCapable_Object=MibTableColumn
rmtProfileEntryMpCapable=_RmtProfileEntryMpCapable_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,10),_RmtProfileEntryMpCapable_Type())
rmtProfileEntryMpCapable.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpCapable.setStatus(_A)
class _RmtProfileEntryMpLineUtilization_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RmtProfileEntryMpLineUtilization_Type.__name__=_B
_RmtProfileEntryMpLineUtilization_Object=MibTableColumn
rmtProfileEntryMpLineUtilization=_RmtProfileEntryMpLineUtilization_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,11),_RmtProfileEntryMpLineUtilization_Type())
rmtProfileEntryMpLineUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpLineUtilization.setStatus(_A)
class _RmtProfileEntryMpHistoryTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RmtProfileEntryMpHistoryTime_Type.__name__=_B
_RmtProfileEntryMpHistoryTime_Object=MibTableColumn
rmtProfileEntryMpHistoryTime=_RmtProfileEntryMpHistoryTime_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,12),_RmtProfileEntryMpHistoryTime_Type())
rmtProfileEntryMpHistoryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpHistoryTime.setStatus(_A)
class _RmtProfileEntryMpMoreBWSamples_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RmtProfileEntryMpMoreBWSamples_Type.__name__=_B
_RmtProfileEntryMpMoreBWSamples_Object=MibTableColumn
rmtProfileEntryMpMoreBWSamples=_RmtProfileEntryMpMoreBWSamples_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,13),_RmtProfileEntryMpMoreBWSamples_Type())
rmtProfileEntryMpMoreBWSamples.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpMoreBWSamples.setStatus(_A)
class _RmtProfileEntryMpLessBWSamples_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RmtProfileEntryMpLessBWSamples_Type.__name__=_B
_RmtProfileEntryMpLessBWSamples_Object=MibTableColumn
rmtProfileEntryMpLessBWSamples=_RmtProfileEntryMpLessBWSamples_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,14),_RmtProfileEntryMpLessBWSamples_Type())
rmtProfileEntryMpLessBWSamples.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpLessBWSamples.setStatus(_A)
class _RmtProfileEntryMpMaxCallsAllowed_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RmtProfileEntryMpMaxCallsAllowed_Type.__name__=_B
_RmtProfileEntryMpMaxCallsAllowed_Object=MibTableColumn
rmtProfileEntryMpMaxCallsAllowed=_RmtProfileEntryMpMaxCallsAllowed_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,15),_RmtProfileEntryMpMaxCallsAllowed_Type())
rmtProfileEntryMpMaxCallsAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpMaxCallsAllowed.setStatus(_A)
class _RmtProfileEntryMpCallsToAdd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RmtProfileEntryMpCallsToAdd_Type.__name__=_B
_RmtProfileEntryMpCallsToAdd_Object=MibTableColumn
rmtProfileEntryMpCallsToAdd=_RmtProfileEntryMpCallsToAdd_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,16),_RmtProfileEntryMpCallsToAdd_Type())
rmtProfileEntryMpCallsToAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpCallsToAdd.setStatus(_A)
class _RmtProfileEntryMpCallsToRemove_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RmtProfileEntryMpCallsToRemove_Type.__name__=_B
_RmtProfileEntryMpCallsToRemove_Object=MibTableColumn
rmtProfileEntryMpCallsToRemove=_RmtProfileEntryMpCallsToRemove_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,17),_RmtProfileEntryMpCallsToRemove_Type())
rmtProfileEntryMpCallsToRemove.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpCallsToRemove.setStatus(_A)
class _RmtProfileEntryMpAvgPktSize_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1500))
_RmtProfileEntryMpAvgPktSize_Type.__name__=_B
_RmtProfileEntryMpAvgPktSize_Object=MibTableColumn
rmtProfileEntryMpAvgPktSize=_RmtProfileEntryMpAvgPktSize_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,18),_RmtProfileEntryMpAvgPktSize_Type())
rmtProfileEntryMpAvgPktSize.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpAvgPktSize.setStatus(_A)
class _RmtProfileEntryMpRmtBwCtrl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RmtProfileEntryMpRmtBwCtrl_Type.__name__=_B
_RmtProfileEntryMpRmtBwCtrl_Object=MibTableColumn
rmtProfileEntryMpRmtBwCtrl=_RmtProfileEntryMpRmtBwCtrl_Object((1,3,6,1,4,1,52,4,1,2,7,4,1,3,1,19),_RmtProfileEntryMpRmtBwCtrl_Type())
rmtProfileEntryMpRmtBwCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:rmtProfileEntryMpRmtBwCtrl.setStatus(_A)
_CallHistory_ObjectIdentity=ObjectIdentity
callHistory=_CallHistory_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,4,2))
class _CallHistoryTableMaxLength_Type(Integer32):defaultValue=50
_CallHistoryTableMaxLength_Type.__name__=_B
_CallHistoryTableMaxLength_Object=MibScalar
callHistoryTableMaxLength=_CallHistoryTableMaxLength_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,1),_CallHistoryTableMaxLength_Type())
callHistoryTableMaxLength.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryTableMaxLength.setStatus(_A)
_CallHistoryTable_Object=MibTable
callHistoryTable=_CallHistoryTable_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2))
if mibBuilder.loadTexts:callHistoryTable.setStatus(_A)
_CallHistoryEntry_Object=MibTableRow
callHistoryEntry=_CallHistoryEntry_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1))
callHistoryEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:callHistoryEntry.setStatus(_A)
_CallHistorySetupTime_Type=Integer32
_CallHistorySetupTime_Object=MibTableColumn
callHistorySetupTime=_CallHistorySetupTime_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,1),_CallHistorySetupTime_Type())
callHistorySetupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistorySetupTime.setStatus(_A)
class _CallHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_CallHistoryIndex_Type.__name__=_B
_CallHistoryIndex_Object=MibTableColumn
callHistoryIndex=_CallHistoryIndex_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,2),_CallHistoryIndex_Type())
callHistoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryIndex.setStatus(_A)
_CallHistoryPeerAddress_Type=DisplayString
_CallHistoryPeerAddress_Object=MibTableColumn
callHistoryPeerAddress=_CallHistoryPeerAddress_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,3),_CallHistoryPeerAddress_Type())
callHistoryPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryPeerAddress.setStatus(_A)
class _CallHistoryNeighborId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CallHistoryNeighborId_Type.__name__=_B
_CallHistoryNeighborId_Object=MibTableColumn
callHistoryNeighborId=_CallHistoryNeighborId_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,4),_CallHistoryNeighborId_Type())
callHistoryNeighborId.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryNeighborId.setStatus(_A)
class _CallHistoryLogicalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CallHistoryLogicalIfIndex_Type.__name__=_B
_CallHistoryLogicalIfIndex_Object=MibTableColumn
callHistoryLogicalIfIndex=_CallHistoryLogicalIfIndex_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,5),_CallHistoryLogicalIfIndex_Type())
callHistoryLogicalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryLogicalIfIndex.setStatus(_A)
class _CallHistoryDisconnectCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6,16,17,18,21,22,28,31,34,38,41,42,43,44,52,54,58,63,65,66,70,79,81,82,85,88,90,91,95,96,97,98,99,100,111,133,134,135,136,138)));namedValues=NamedValues(*(('unassignedNumber',1),('noRouteToDestination',2),('channelUnacceptable',6),('normalCallClearing',16),('userBusy',17),('noUserResponding',18),('callRejected',21),('numberChangedAddress',22),('invalidNumberFormat',28),('normalUnspecified',31),('noChannelAvailable',34),('networkOutOfOrder',38),('temporaryFailure',41),('switchingEquipmentCongestion',42),('userInfoDiscarded',43),('requestedChannelNotAvailable',44),('outgoingCallsBarred',52),('incomingCallsBarred',54),('bearerCapabilityNotPresentlyAvail',58),('serviceNotAvailable',63),('bearerServiceNotImplemented',65),('channelTypeNotImplemented',66),('onlyRestrictedChannelAvailable',70),('serviceOrOptionNotImplemeted',79),('invalidCallReferenceValue',81),('identifiedChannelDoesNotExist',82),('invalidDigitValueForAddress',85),('incompatibleDestination',88),('destinationAddressMissing',90),('transitNetworkDoesNotExist',91),('invalidMessageSpecified',95),('mandatoryIEmissing',96),('messageTypeNonexistentOrNotImplemented',97),('messageNotCompatibleWithCallState',98),('iEnotImplemented',99),('invalidIEcontents',100),('protocolError',111),('callAlreadyActive',133),('lineDisabled',134),('badParameter',135),('timeoutOccured',136),('noCallActive',138)))
_CallHistoryDisconnectCause_Type.__name__=_B
_CallHistoryDisconnectCause_Object=MibTableColumn
callHistoryDisconnectCause=_CallHistoryDisconnectCause_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,6),_CallHistoryDisconnectCause_Type())
callHistoryDisconnectCause.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryDisconnectCause.setStatus(_A)
_CallHistoryConnectTime_Type=Integer32
_CallHistoryConnectTime_Object=MibTableColumn
callHistoryConnectTime=_CallHistoryConnectTime_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,7),_CallHistoryConnectTime_Type())
callHistoryConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryConnectTime.setStatus(_A)
_CallHistoryDisconnectTime_Type=Integer32
_CallHistoryDisconnectTime_Object=MibTableColumn
callHistoryDisconnectTime=_CallHistoryDisconnectTime_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,8),_CallHistoryDisconnectTime_Type())
callHistoryDisconnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryDisconnectTime.setStatus(_A)
class _CallHistoryCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('originate',1),('answer',2),('callback',3)))
_CallHistoryCallOrigin_Type.__name__=_B
_CallHistoryCallOrigin_Object=MibTableColumn
callHistoryCallOrigin=_CallHistoryCallOrigin_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,9),_CallHistoryCallOrigin_Type())
callHistoryCallOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryCallOrigin.setStatus(_A)
class _CallHistoryInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('other',1),('speech',2),('unrestrictedDigital',3),('unrestrictedDigital56',4),('restrictedDigital',5),('audio31',6),('audio7',7),('video',8),('packetSwitched',9)))
_CallHistoryInfoType_Type.__name__=_B
_CallHistoryInfoType_Object=MibTableColumn
callHistoryInfoType=_CallHistoryInfoType_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,10),_CallHistoryInfoType_Type())
callHistoryInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryInfoType.setStatus(_A)
_CallHistoryTransmitPackets_Type=Counter32
_CallHistoryTransmitPackets_Object=MibTableColumn
callHistoryTransmitPackets=_CallHistoryTransmitPackets_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,11),_CallHistoryTransmitPackets_Type())
callHistoryTransmitPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryTransmitPackets.setStatus(_A)
_CallHistoryTransmitBytes_Type=Counter32
_CallHistoryTransmitBytes_Object=MibTableColumn
callHistoryTransmitBytes=_CallHistoryTransmitBytes_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,12),_CallHistoryTransmitBytes_Type())
callHistoryTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryTransmitBytes.setStatus(_A)
_CallHistoryReceivePackets_Type=Counter32
_CallHistoryReceivePackets_Object=MibTableColumn
callHistoryReceivePackets=_CallHistoryReceivePackets_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,13),_CallHistoryReceivePackets_Type())
callHistoryReceivePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryReceivePackets.setStatus(_A)
_CallHistoryReceiveBytes_Type=Counter32
_CallHistoryReceiveBytes_Object=MibTableColumn
callHistoryReceiveBytes=_CallHistoryReceiveBytes_Object((1,3,6,1,4,1,52,4,1,2,7,4,2,2,1,14),_CallHistoryReceiveBytes_Type())
callHistoryReceiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryReceiveBytes.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_G:DisplayString,'cabletron':cabletron,'mibs':mibs,'ctron':ctron,'ctDataLink':ctDataLink,'ctronWan':ctronWan,'ctISDNconfigMib':ctISDNconfigMib,'ctISDNcontrol':ctISDNcontrol,'isdnDchTable':isdnDchTable,'isdnDchEntry':isdnDchEntry,_H:isdnDchIndex,'isdnDchRateAccess':isdnDchRateAccess,'isdnDchAllowedCh':isdnDchAllowedCh,'isdnDchChInUse':isdnDchChInUse,'isdnDchSupportedSwitches':isdnDchSupportedSwitches,'isdnDchSwitchType':isdnDchSwitchType,'isdnDchSPID1':isdnDchSPID1,'isdnDchSPID2':isdnDchSPID2,'isdnDchDirNum1':isdnDchDirNum1,'isdnDchDirNum2':isdnDchDirNum2,'isdnDchOperStatus':isdnDchOperStatus,'dialCtlNbrCfgTable':dialCtlNbrCfgTable,'dialCtlNbrCfgEntry':dialCtlNbrCfgEntry,_N:dialCtlNbrCfgId,_O:dialCtlNbrCfgIndex,'dialCtlNbrCfgIfIndex':dialCtlNbrCfgIfIndex,'dialCtlNbrCfgOriginateAddress':dialCtlNbrCfgOriginateAddress,'dialCtlNbrCfgAnswerAddress':dialCtlNbrCfgAnswerAddress,'rmtProfileTable':rmtProfileTable,'rmtProfileEntry':rmtProfileEntry,_P:rmtProfileEntryIndex,'rmtProfileEntryName':rmtProfileEntryName,'rmtProfileEntryMakerName':rmtProfileEntryMakerName,'rmtProfileEntryAction':rmtProfileEntryAction,'rmtProfileEntryState':rmtProfileEntryState,'rmtProfileEntryMaxNeighbor':rmtProfileEntryMaxNeighbor,'rmtProfileEntryBchInUse':rmtProfileEntryBchInUse,'rmtProfileEntryLinkHead':rmtProfileEntryLinkHead,'rmtProfileEntryNextLink':rmtProfileEntryNextLink,'rmtProfileEntryMpCapable':rmtProfileEntryMpCapable,'rmtProfileEntryMpLineUtilization':rmtProfileEntryMpLineUtilization,'rmtProfileEntryMpHistoryTime':rmtProfileEntryMpHistoryTime,'rmtProfileEntryMpMoreBWSamples':rmtProfileEntryMpMoreBWSamples,'rmtProfileEntryMpLessBWSamples':rmtProfileEntryMpLessBWSamples,'rmtProfileEntryMpMaxCallsAllowed':rmtProfileEntryMpMaxCallsAllowed,'rmtProfileEntryMpCallsToAdd':rmtProfileEntryMpCallsToAdd,'rmtProfileEntryMpCallsToRemove':rmtProfileEntryMpCallsToRemove,'rmtProfileEntryMpAvgPktSize':rmtProfileEntryMpAvgPktSize,'rmtProfileEntryMpRmtBwCtrl':rmtProfileEntryMpRmtBwCtrl,'callHistory':callHistory,'callHistoryTableMaxLength':callHistoryTableMaxLength,'callHistoryTable':callHistoryTable,'callHistoryEntry':callHistoryEntry,'callHistorySetupTime':callHistorySetupTime,_S:callHistoryIndex,'callHistoryPeerAddress':callHistoryPeerAddress,'callHistoryNeighborId':callHistoryNeighborId,'callHistoryLogicalIfIndex':callHistoryLogicalIfIndex,'callHistoryDisconnectCause':callHistoryDisconnectCause,'callHistoryConnectTime':callHistoryConnectTime,'callHistoryDisconnectTime':callHistoryDisconnectTime,'callHistoryCallOrigin':callHistoryCallOrigin,'callHistoryInfoType':callHistoryInfoType,'callHistoryTransmitPackets':callHistoryTransmitPackets,'callHistoryTransmitBytes':callHistoryTransmitBytes,'callHistoryReceivePackets':callHistoryReceivePackets,'callHistoryReceiveBytes':callHistoryReceiveBytes})