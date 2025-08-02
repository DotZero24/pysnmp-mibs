_f='rlPethPerPseDeviceIndex'
_e='rlPethPerPseGroupIndex'
_d='rlPethUnitIndex'
_c='rlPethPdPortIndex'
_b='rlPethPowerPseGroupIndex'
_a='nextport'
_Z='lowestpriority'
_Y='maxlimit'
_X='classlimit'
_W='portlimit'
_V='rlPethMainPseGroupIndex'
_U='protocolOwnerLLDPExpired'
_T='protocolOwnerCDPExpired'
_S='protocolOwnerLLDP'
_R='protocolOwnerCDP'
_Q='protocolOwnerNone'
_P='rlPethPsePortIndex'
_O='rlPethPsePortGroupIndex'
_N='poe60w'
_M='TruthValue'
_L='PortList'
_K='none'
_J='not-relevant'
_I='DisplayString'
_H='disabled'
_G='enabled'
_F='not-accessible'
_E='CISCOSB-POE-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention',_M)
rlPoe=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,108))
if mibBuilder.loadTexts:rlPoe.setRevisions(('2010-06-02 00:00','2009-11-26 00:00'))
class RlPoeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('poe',2),('poeplus',3),(_N,4),('poeBTtype3',5),('poeBTtype4',6)))
_RlPethPsePortTable_Object=MibTable
rlPethPsePortTable=_RlPethPsePortTable_Object((1,3,6,1,4,1,9,6,1,101,108,1))
if mibBuilder.loadTexts:rlPethPsePortTable.setStatus(_A)
_RlPethPsePortEntry_Object=MibTableRow
rlPethPsePortEntry=_RlPethPsePortEntry_Object((1,3,6,1,4,1,9,6,1,101,108,1,1))
rlPethPsePortEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:rlPethPsePortEntry.setStatus(_A)
class _RlPethPsePortGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlPethPsePortGroupIndex_Type.__name__=_B
_RlPethPsePortGroupIndex_Object=MibTableColumn
rlPethPsePortGroupIndex=_RlPethPsePortGroupIndex_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,1),_RlPethPsePortGroupIndex_Type())
rlPethPsePortGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPethPsePortGroupIndex.setStatus(_A)
class _RlPethPsePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlPethPsePortIndex_Type.__name__=_B
_RlPethPsePortIndex_Object=MibTableColumn
rlPethPsePortIndex=_RlPethPsePortIndex_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,2),_RlPethPsePortIndex_Type())
rlPethPsePortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPethPsePortIndex.setStatus(_A)
class _RlPethPsePortOutputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortOutputVoltage_Type.__name__=_B
_RlPethPsePortOutputVoltage_Object=MibTableColumn
rlPethPsePortOutputVoltage=_RlPethPsePortOutputVoltage_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,3),_RlPethPsePortOutputVoltage_Type())
rlPethPsePortOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOutputVoltage.setStatus(_A)
class _RlPethPsePortOutputCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortOutputCurrent_Type.__name__=_B
_RlPethPsePortOutputCurrent_Object=MibTableColumn
rlPethPsePortOutputCurrent=_RlPethPsePortOutputCurrent_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,4),_RlPethPsePortOutputCurrent_Type())
rlPethPsePortOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOutputCurrent.setStatus(_A)
class _RlPethPsePortOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortOutputPower_Type.__name__=_B
_RlPethPsePortOutputPower_Object=MibTableColumn
rlPethPsePortOutputPower=_RlPethPsePortOutputPower_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,5),_RlPethPsePortOutputPower_Type())
rlPethPsePortOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOutputPower.setStatus(_A)
class _RlPethPsePortPowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortPowerLimit_Type.__name__=_B
_RlPethPsePortPowerLimit_Object=MibTableColumn
rlPethPsePortPowerLimit=_RlPethPsePortPowerLimit_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,6),_RlPethPsePortPowerLimit_Type())
rlPethPsePortPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortPowerLimit.setStatus(_A)
class _RlPethPsePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortStatus_Type.__name__=_B
_RlPethPsePortStatus_Object=MibTableColumn
rlPethPsePortStatus=_RlPethPsePortStatus_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,7),_RlPethPsePortStatus_Type())
rlPethPsePortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortStatus.setStatus(_A)
class _RlPethPsePortStatusDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_RlPethPsePortStatusDescription_Type.__name__=_I
_RlPethPsePortStatusDescription_Object=MibTableColumn
rlPethPsePortStatusDescription=_RlPethPsePortStatusDescription_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,8),_RlPethPsePortStatusDescription_Type())
rlPethPsePortStatusDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortStatusDescription.setStatus(_A)
class _RlPethPsePortOperPowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortOperPowerLimit_Type.__name__=_B
_RlPethPsePortOperPowerLimit_Object=MibTableColumn
rlPethPsePortOperPowerLimit=_RlPethPsePortOperPowerLimit_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,9),_RlPethPsePortOperPowerLimit_Type())
rlPethPsePortOperPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOperPowerLimit.setStatus(_A)
class _RlPethPsePortTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlPethPsePortTimeRangeName_Type.__name__=_I
_RlPethPsePortTimeRangeName_Object=MibTableColumn
rlPethPsePortTimeRangeName=_RlPethPsePortTimeRangeName_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,10),_RlPethPsePortTimeRangeName_Type())
rlPethPsePortTimeRangeName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortTimeRangeName.setStatus(_A)
_RlPethPsePortOperStatus_Type=TruthValue
_RlPethPsePortOperStatus_Object=MibTableColumn
rlPethPsePortOperStatus=_RlPethPsePortOperStatus_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,11),_RlPethPsePortOperStatus_Type())
rlPethPsePortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOperStatus.setStatus(_A)
class _RlPethPsePortMaxPowerAllocAllowed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortMaxPowerAllocAllowed_Type.__name__=_B
_RlPethPsePortMaxPowerAllocAllowed_Object=MibTableColumn
rlPethPsePortMaxPowerAllocAllowed=_RlPethPsePortMaxPowerAllocAllowed_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,12),_RlPethPsePortMaxPowerAllocAllowed_Type())
rlPethPsePortMaxPowerAllocAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortMaxPowerAllocAllowed.setStatus(_A)
_RlPethPsePortSupportPoeType_Type=RlPoeType
_RlPethPsePortSupportPoeType_Object=MibTableColumn
rlPethPsePortSupportPoeType=_RlPethPsePortSupportPoeType_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,13),_RlPethPsePortSupportPoeType_Type())
rlPethPsePortSupportPoeType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortSupportPoeType.setStatus(_A)
_RlPethPsePortLinkPartnerPoeType_Type=RlPoeType
_RlPethPsePortLinkPartnerPoeType_Object=MibTableColumn
rlPethPsePortLinkPartnerPoeType=_RlPethPsePortLinkPartnerPoeType_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,14),_RlPethPsePortLinkPartnerPoeType_Type())
rlPethPsePortLinkPartnerPoeType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortLinkPartnerPoeType.setStatus(_A)
class _RlPethPsePortFourPairForced_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('forcedEnable',0),('forcedDisable',1)))
_RlPethPsePortFourPairForced_Type.__name__=_B
_RlPethPsePortFourPairForced_Object=MibTableColumn
rlPethPsePortFourPairForced=_RlPethPsePortFourPairForced_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,15),_RlPethPsePortFourPairForced_Type())
rlPethPsePortFourPairForced.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortFourPairForced.setStatus(_A)
class _RlPethPsePortFourPairEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fourPairEnable',1),('fourPairDisable',2)))
_RlPethPsePortFourPairEnabled_Type.__name__=_B
_RlPethPsePortFourPairEnabled_Object=MibTableColumn
rlPethPsePortFourPairEnabled=_RlPethPsePortFourPairEnabled_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,16),_RlPethPsePortFourPairEnabled_Type())
rlPethPsePortFourPairEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortFourPairEnabled.setStatus(_A)
class _RlPethPsePortNegotiationAllocatedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortNegotiationAllocatedPower_Type.__name__=_B
_RlPethPsePortNegotiationAllocatedPower_Object=MibTableColumn
rlPethPsePortNegotiationAllocatedPower=_RlPethPsePortNegotiationAllocatedPower_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,17),_RlPethPsePortNegotiationAllocatedPower_Type())
rlPethPsePortNegotiationAllocatedPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortNegotiationAllocatedPower.setStatus(_A)
class _RlPethPsePortNegotiationProtocolOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2),(_T,3),(_U,4)))
_RlPethPsePortNegotiationProtocolOwner_Type.__name__=_B
_RlPethPsePortNegotiationProtocolOwner_Object=MibTableColumn
rlPethPsePortNegotiationProtocolOwner=_RlPethPsePortNegotiationProtocolOwner_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,18),_RlPethPsePortNegotiationProtocolOwner_Type())
rlPethPsePortNegotiationProtocolOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortNegotiationProtocolOwner.setStatus(_A)
class _RlPethPsePortLegacySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_G,1),(_H,2)))
_RlPethPsePortLegacySupport_Type.__name__=_B
_RlPethPsePortLegacySupport_Object=MibTableColumn
rlPethPsePortLegacySupport=_RlPethPsePortLegacySupport_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,19),_RlPethPsePortLegacySupport_Type())
rlPethPsePortLegacySupport.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortLegacySupport.setStatus(_A)
class _RlPethPsePortHighPowerModeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_G,1),(_H,2)))
_RlPethPsePortHighPowerModeEnable_Type.__name__=_B
_RlPethPsePortHighPowerModeEnable_Object=MibTableColumn
rlPethPsePortHighPowerModeEnable=_RlPethPsePortHighPowerModeEnable_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,20),_RlPethPsePortHighPowerModeEnable_Type())
rlPethPsePortHighPowerModeEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortHighPowerModeEnable.setStatus(_A)
class _RlPethPsePortMenagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('dynamic',1),('static',2)))
_RlPethPsePortMenagementMode_Type.__name__=_B
_RlPethPsePortMenagementMode_Object=MibTableColumn
rlPethPsePortMenagementMode=_RlPethPsePortMenagementMode_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,21),_RlPethPsePortMenagementMode_Type())
rlPethPsePortMenagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortMenagementMode.setStatus(_A)
class _RlPethPsePortStaticPowerAllocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortStaticPowerAllocation_Type.__name__=_B
_RlPethPsePortStaticPowerAllocation_Object=MibTableColumn
rlPethPsePortStaticPowerAllocation=_RlPethPsePortStaticPowerAllocation_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,22),_RlPethPsePortStaticPowerAllocation_Type())
rlPethPsePortStaticPowerAllocation.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortStaticPowerAllocation.setStatus(_A)
class _RlPethPsePortHighPowerOpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_G,1),(_H,2)))
_RlPethPsePortHighPowerOpStatus_Type.__name__=_B
_RlPethPsePortHighPowerOpStatus_Object=MibTableColumn
rlPethPsePortHighPowerOpStatus=_RlPethPsePortHighPowerOpStatus_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,23),_RlPethPsePortHighPowerOpStatus_Type())
rlPethPsePortHighPowerOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortHighPowerOpStatus.setStatus(_A)
class _RlPethPsePortClassLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,4,5,6,7)));namedValues=NamedValues(*(('unlimited',0),('class3',3),('class4',4),('class5',5),('class6',6),('class7',7)))
_RlPethPsePortClassLimit_Type.__name__=_B
_RlPethPsePortClassLimit_Object=MibTableColumn
rlPethPsePortClassLimit=_RlPethPsePortClassLimit_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,24),_RlPethPsePortClassLimit_Type())
rlPethPsePortClassLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortClassLimit.setStatus(_A)
_RlPethPsePortNegotiation_Type=TruthValue
_RlPethPsePortNegotiation_Object=MibTableColumn
rlPethPsePortNegotiation=_RlPethPsePortNegotiation_Object((1,3,6,1,4,1,9,6,1,101,108,1,1,25),_RlPethPsePortNegotiation_Type())
rlPethPsePortNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortNegotiation.setStatus(_A)
_RlPethMainPseTable_Object=MibTable
rlPethMainPseTable=_RlPethMainPseTable_Object((1,3,6,1,4,1,9,6,1,101,108,2))
if mibBuilder.loadTexts:rlPethMainPseTable.setStatus(_A)
_RlPethMainPseEntry_Object=MibTableRow
rlPethMainPseEntry=_RlPethMainPseEntry_Object((1,3,6,1,4,1,9,6,1,101,108,2,1))
rlPethMainPseEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:rlPethMainPseEntry.setStatus(_A)
class _RlPethMainPseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlPethMainPseGroupIndex_Type.__name__=_B
_RlPethMainPseGroupIndex_Object=MibTableColumn
rlPethMainPseGroupIndex=_RlPethMainPseGroupIndex_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,1),_RlPethMainPseGroupIndex_Type())
rlPethMainPseGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPethMainPseGroupIndex.setStatus(_A)
class _RlPethMainPseSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlPethMainPseSwVersion_Type.__name__=_I
_RlPethMainPseSwVersion_Object=MibTableColumn
rlPethMainPseSwVersion=_RlPethMainPseSwVersion_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,2),_RlPethMainPseSwVersion_Type())
rlPethMainPseSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainPseSwVersion.setStatus(_A)
class _RlPethMainPseHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlPethMainPseHwVersion_Type.__name__=_I
_RlPethMainPseHwVersion_Object=MibTableColumn
rlPethMainPseHwVersion=_RlPethMainPseHwVersion_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,3),_RlPethMainPseHwVersion_Type())
rlPethMainPseHwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainPseHwVersion.setStatus('obsolete')
class _RlPethMainPseHwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('enhanced',1),('plus',2),('auto',3),('nonPoe',4),('enhancedPlus',5),(_N,6),('poeBT',7)))
_RlPethMainPseHwType_Type.__name__=_B
_RlPethMainPseHwType_Object=MibTableColumn
rlPethMainPseHwType=_RlPethMainPseHwType_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,4),_RlPethMainPseHwType_Type())
rlPethMainPseHwType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainPseHwType.setStatus(_A)
class _RlPethMainPsePowerGuardBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_RlPethMainPsePowerGuardBand_Type.__name__=_B
_RlPethMainPsePowerGuardBand_Object=MibTableColumn
rlPethMainPsePowerGuardBand=_RlPethMainPsePowerGuardBand_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,5),_RlPethMainPsePowerGuardBand_Type())
rlPethMainPsePowerGuardBand.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethMainPsePowerGuardBand.setStatus(_A)
class _RlPethMainPsePowerManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,6)));namedValues=NamedValues(*((_W,0),(_X,5),(_Y,6)))
_RlPethMainPsePowerManagementMode_Type.__name__=_B
_RlPethMainPsePowerManagementMode_Object=MibTableColumn
rlPethMainPsePowerManagementMode=_RlPethMainPsePowerManagementMode_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,6),_RlPethMainPsePowerManagementMode_Type())
rlPethMainPsePowerManagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethMainPsePowerManagementMode.setStatus(_A)
class _RlPethMainPsedisconnectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_RlPethMainPsedisconnectMethod_Type.__name__=_B
_RlPethMainPsedisconnectMethod_Object=MibTableColumn
rlPethMainPsedisconnectMethod=_RlPethMainPsedisconnectMethod_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,7),_RlPethMainPsedisconnectMethod_Type())
rlPethMainPsedisconnectMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethMainPsedisconnectMethod.setStatus(_A)
class _RlPethMainPseTemperatureSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,200),ValueRangeConstraint(32767,32767))
_RlPethMainPseTemperatureSensor_Type.__name__=_B
_RlPethMainPseTemperatureSensor_Object=MibTableColumn
rlPethMainPseTemperatureSensor=_RlPethMainPseTemperatureSensor_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,8),_RlPethMainPseTemperatureSensor_Type())
rlPethMainPseTemperatureSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainPseTemperatureSensor.setStatus(_A)
class _RlPethMainPseInrushTestEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RlPethMainPseInrushTestEnabled_Type.__name__=_B
_RlPethMainPseInrushTestEnabled_Object=MibTableColumn
rlPethMainPseInrushTestEnabled=_RlPethMainPseInrushTestEnabled_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,9),_RlPethMainPseInrushTestEnabled_Type())
rlPethMainPseInrushTestEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethMainPseInrushTestEnabled.setStatus(_A)
class _RlPethMainPseLegacyDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RlPethMainPseLegacyDisabled_Type.__name__=_B
_RlPethMainPseLegacyDisabled_Object=MibTableColumn
rlPethMainPseLegacyDisabled=_RlPethMainPseLegacyDisabled_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,10),_RlPethMainPseLegacyDisabled_Type())
rlPethMainPseLegacyDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethMainPseLegacyDisabled.setStatus(_A)
_RlPethMainBanksValues_Type=OctetString
_RlPethMainBanksValues_Object=MibTableColumn
rlPethMainBanksValues=_RlPethMainBanksValues_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,11),_RlPethMainBanksValues_Type())
rlPethMainBanksValues.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainBanksValues.setStatus(_A)
_RlPethMainBanksActivePowerBank_Type=Integer32
_RlPethMainBanksActivePowerBank_Object=MibTableColumn
rlPethMainBanksActivePowerBank=_RlPethMainBanksActivePowerBank_Object((1,3,6,1,4,1,9,6,1,101,108,2,1,12),_RlPethMainBanksActivePowerBank_Type())
rlPethMainBanksActivePowerBank.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainBanksActivePowerBank.setStatus(_A)
_RlPethPowerPseTable_Object=MibTable
rlPethPowerPseTable=_RlPethPowerPseTable_Object((1,3,6,1,4,1,9,6,1,101,108,3))
if mibBuilder.loadTexts:rlPethPowerPseTable.setStatus(_A)
_RlPethPowerPseEntry_Object=MibTableRow
rlPethPowerPseEntry=_RlPethPowerPseEntry_Object((1,3,6,1,4,1,9,6,1,101,108,3,1))
rlPethPowerPseEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:rlPethPowerPseEntry.setStatus(_A)
class _RlPethPowerPseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlPethPowerPseGroupIndex_Type.__name__=_B
_RlPethPowerPseGroupIndex_Object=MibTableColumn
rlPethPowerPseGroupIndex=_RlPethPowerPseGroupIndex_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,1),_RlPethPowerPseGroupIndex_Type())
rlPethPowerPseGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPethPowerPseGroupIndex.setStatus(_A)
class _RlPethPowerPsePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('ps1',1),('ps2',2),('ps3',3)))
_RlPethPowerPsePower_Type.__name__=_B
_RlPethPowerPsePower_Object=MibTableColumn
rlPethPowerPsePower=_RlPethPowerPsePower_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,2),_RlPethPowerPsePower_Type())
rlPethPowerPsePower.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPsePower.setStatus(_A)
class _RlPethPowerPseRpsPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('rps1',1),('rps2',2),('rps3',3)))
_RlPethPowerPseRpsPower_Type.__name__=_B
_RlPethPowerPseRpsPower_Object=MibTableColumn
rlPethPowerPseRpsPower=_RlPethPowerPseRpsPower_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,3),_RlPethPowerPseRpsPower_Type())
rlPethPowerPseRpsPower.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPseRpsPower.setStatus(_A)
class _RlPethPowerPsePowerManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,6)));namedValues=NamedValues(*((_W,0),(_X,5),(_Y,6)))
_RlPethPowerPsePowerManagementMode_Type.__name__=_B
_RlPethPowerPsePowerManagementMode_Object=MibTableColumn
rlPethPowerPsePowerManagementMode=_RlPethPowerPsePowerManagementMode_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,4),_RlPethPowerPsePowerManagementMode_Type())
rlPethPowerPsePowerManagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPsePowerManagementMode.setStatus(_A)
class _RlPethPowerPsedisconnectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_RlPethPowerPsedisconnectMethod_Type.__name__=_B
_RlPethPowerPsedisconnectMethod_Object=MibTableColumn
rlPethPowerPsedisconnectMethod=_RlPethPowerPsedisconnectMethod_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,5),_RlPethPowerPsedisconnectMethod_Type())
rlPethPowerPsedisconnectMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPsedisconnectMethod.setStatus(_A)
class _RlPethPowerPseTemperatureSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,200))
_RlPethPowerPseTemperatureSensor_Type.__name__=_B
_RlPethPowerPseTemperatureSensor_Object=MibTableColumn
rlPethPowerPseTemperatureSensor=_RlPethPowerPseTemperatureSensor_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,6),_RlPethPowerPseTemperatureSensor_Type())
rlPethPowerPseTemperatureSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPowerPseTemperatureSensor.setStatus(_A)
class _RlPethPowerPseInrushTestEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RlPethPowerPseInrushTestEnabled_Type.__name__=_B
_RlPethPowerPseInrushTestEnabled_Object=MibTableColumn
rlPethPowerPseInrushTestEnabled=_RlPethPowerPseInrushTestEnabled_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,7),_RlPethPowerPseInrushTestEnabled_Type())
rlPethPowerPseInrushTestEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPseInrushTestEnabled.setStatus(_A)
class _RlPethPowerPseLegacyDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RlPethPowerPseLegacyDisabled_Type.__name__=_B
_RlPethPowerPseLegacyDisabled_Object=MibTableColumn
rlPethPowerPseLegacyDisabled=_RlPethPowerPseLegacyDisabled_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,8),_RlPethPowerPseLegacyDisabled_Type())
rlPethPowerPseLegacyDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPseLegacyDisabled.setStatus(_A)
_RlPethPowerBanksValues_Type=OctetString
_RlPethPowerBanksValues_Object=MibTableColumn
rlPethPowerBanksValues=_RlPethPowerBanksValues_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,9),_RlPethPowerBanksValues_Type())
rlPethPowerBanksValues.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPowerBanksValues.setStatus(_A)
_RlPethPowerBanksActivePowerBank_Type=Integer32
_RlPethPowerBanksActivePowerBank_Object=MibTableColumn
rlPethPowerBanksActivePowerBank=_RlPethPowerBanksActivePowerBank_Object((1,3,6,1,4,1,9,6,1,101,108,3,1,10),_RlPethPowerBanksActivePowerBank_Type())
rlPethPowerBanksActivePowerBank.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPowerBanksActivePowerBank.setStatus(_A)
_RlPethPdPortTable_Object=MibTable
rlPethPdPortTable=_RlPethPdPortTable_Object((1,3,6,1,4,1,9,6,1,101,108,4))
if mibBuilder.loadTexts:rlPethPdPortTable.setStatus(_A)
_RlPethPdPortEntry_Object=MibTableRow
rlPethPdPortEntry=_RlPethPdPortEntry_Object((1,3,6,1,4,1,9,6,1,101,108,4,1))
rlPethPdPortEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:rlPethPdPortEntry.setStatus(_A)
_RlPethPdPortIndex_Type=InterfaceIndex
_RlPethPdPortIndex_Object=MibTableColumn
rlPethPdPortIndex=_RlPethPdPortIndex_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,1),_RlPethPdPortIndex_Type())
rlPethPdPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPethPdPortIndex.setStatus(_A)
_RlPethPdPortSupportPoeType_Type=RlPoeType
_RlPethPdPortSupportPoeType_Object=MibTableColumn
rlPethPdPortSupportPoeType=_RlPethPdPortSupportPoeType_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,2),_RlPethPdPortSupportPoeType_Type())
rlPethPdPortSupportPoeType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPdPortSupportPoeType.setStatus(_A)
_RlPethPdPortOperPoeType_Type=RlPoeType
_RlPethPdPortOperPoeType_Object=MibTableColumn
rlPethPdPortOperPoeType=_RlPethPdPortOperPoeType_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,3),_RlPethPdPortOperPoeType_Type())
rlPethPdPortOperPoeType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPdPortOperPoeType.setStatus(_A)
_RlPethPdPortPowerRequest_Type=Unsigned32
_RlPethPdPortPowerRequest_Object=MibTableColumn
rlPethPdPortPowerRequest=_RlPethPdPortPowerRequest_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,4),_RlPethPdPortPowerRequest_Type())
rlPethPdPortPowerRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPdPortPowerRequest.setStatus(_A)
_RlPethPdPortPowerAvailable_Type=Unsigned32
_RlPethPdPortPowerAvailable_Object=MibTableColumn
rlPethPdPortPowerAvailable=_RlPethPdPortPowerAvailable_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,5),_RlPethPdPortPowerAvailable_Type())
rlPethPdPortPowerAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPdPortPowerAvailable.setStatus(_A)
_RlPethPdPortForcedMode_Type=RlPoeType
_RlPethPdPortForcedMode_Object=MibTableColumn
rlPethPdPortForcedMode=_RlPethPdPortForcedMode_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,6),_RlPethPdPortForcedMode_Type())
rlPethPdPortForcedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPdPortForcedMode.setStatus(_A)
class _RlPethPdPortNegotiationProtocolOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2),(_T,3),(_U,4)))
_RlPethPdPortNegotiationProtocolOwner_Type.__name__=_B
_RlPethPdPortNegotiationProtocolOwner_Object=MibTableColumn
rlPethPdPortNegotiationProtocolOwner=_RlPethPdPortNegotiationProtocolOwner_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,7),_RlPethPdPortNegotiationProtocolOwner_Type())
rlPethPdPortNegotiationProtocolOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPdPortNegotiationProtocolOwner.setStatus(_A)
_RlPethPdPortNegotiationEnable_Type=TruthValue
_RlPethPdPortNegotiationEnable_Object=MibTableColumn
rlPethPdPortNegotiationEnable=_RlPethPdPortNegotiationEnable_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,8),_RlPethPdPortNegotiationEnable_Type())
rlPethPdPortNegotiationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPdPortNegotiationEnable.setStatus(_A)
class _RlPethPdPortPoweredStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('poweredStatusNA',0),('poweredStatusPowered',1),('poweredStatusAbsent',2)))
_RlPethPdPortPoweredStatus_Type.__name__=_B
_RlPethPdPortPoweredStatus_Object=MibTableColumn
rlPethPdPortPoweredStatus=_RlPethPdPortPoweredStatus_Object((1,3,6,1,4,1,9,6,1,101,108,4,1,9),_RlPethPdPortPoweredStatus_Type())
rlPethPdPortPoweredStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPdPortPoweredStatus.setStatus(_A)
_RlPethPseUnitTable_Object=MibTable
rlPethPseUnitTable=_RlPethPseUnitTable_Object((1,3,6,1,4,1,9,6,1,101,108,5))
if mibBuilder.loadTexts:rlPethPseUnitTable.setStatus(_A)
_RlPethPseUnitEntry_Object=MibTableRow
rlPethPseUnitEntry=_RlPethPseUnitEntry_Object((1,3,6,1,4,1,9,6,1,101,108,5,1))
rlPethPseUnitEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:rlPethPseUnitEntry.setStatus(_A)
class _RlPethUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlPethUnitIndex_Type.__name__=_B
_RlPethUnitIndex_Object=MibTableColumn
rlPethUnitIndex=_RlPethUnitIndex_Object((1,3,6,1,4,1,9,6,1,101,108,5,1,1),_RlPethUnitIndex_Type())
rlPethUnitIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPethUnitIndex.setStatus(_A)
class _RlPethUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unitTypeNone',0),('unitTypePSE',1),('unitTypePD',2),('unitTypePSEPD',3)))
_RlPethUnitType_Type.__name__=_B
_RlPethUnitType_Object=MibTableColumn
rlPethUnitType=_RlPethUnitType_Object((1,3,6,1,4,1,9,6,1,101,108,5,1,2),_RlPethUnitType_Type())
rlPethUnitType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethUnitType.setStatus(_A)
class _RlPethUnitColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unitColorNone',0),('unitColorGreen',1),('unitColorYellow',2),('unitColorRed',3)))
_RlPethUnitColor_Type.__name__=_B
_RlPethUnitColor_Object=MibTableColumn
rlPethUnitColor=_RlPethUnitColor_Object((1,3,6,1,4,1,9,6,1,101,108,5,1,3),_RlPethUnitColor_Type())
rlPethUnitColor.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethUnitColor.setStatus(_A)
_RlPethPseCountersClear_Type=InterfaceIndexOrZero
_RlPethPseCountersClear_Object=MibScalar
rlPethPseCountersClear=_RlPethPseCountersClear_Object((1,3,6,1,4,1,9,6,1,101,108,6),_RlPethPseCountersClear_Type())
rlPethPseCountersClear.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPseCountersClear.setStatus(_A)
class _RlPoeClassErrorDetectionStatus_Type(TruthValue):defaultValue=1
_RlPoeClassErrorDetectionStatus_Type.__name__=_M
_RlPoeClassErrorDetectionStatus_Object=MibScalar
rlPoeClassErrorDetectionStatus=_RlPoeClassErrorDetectionStatus_Object((1,3,6,1,4,1,9,6,1,101,108,8),_RlPoeClassErrorDetectionStatus_Type())
rlPoeClassErrorDetectionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPoeClassErrorDetectionStatus.setStatus(_A)
_RlPethPerPseTable_Object=MibTable
rlPethPerPseTable=_RlPethPerPseTable_Object((1,3,6,1,4,1,9,6,1,101,108,9))
if mibBuilder.loadTexts:rlPethPerPseTable.setStatus(_A)
_RlPethPerPseEntry_Object=MibTableRow
rlPethPerPseEntry=_RlPethPerPseEntry_Object((1,3,6,1,4,1,9,6,1,101,108,9,1))
rlPethPerPseEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:rlPethPerPseEntry.setStatus(_A)
class _RlPethPerPseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlPethPerPseGroupIndex_Type.__name__=_B
_RlPethPerPseGroupIndex_Object=MibTableColumn
rlPethPerPseGroupIndex=_RlPethPerPseGroupIndex_Object((1,3,6,1,4,1,9,6,1,101,108,9,1,1),_RlPethPerPseGroupIndex_Type())
rlPethPerPseGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPethPerPseGroupIndex.setStatus(_A)
class _RlPethPerPseDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_RlPethPerPseDeviceIndex_Type.__name__=_B
_RlPethPerPseDeviceIndex_Object=MibTableColumn
rlPethPerPseDeviceIndex=_RlPethPerPseDeviceIndex_Object((1,3,6,1,4,1,9,6,1,101,108,9,1,2),_RlPethPerPseDeviceIndex_Type())
rlPethPerPseDeviceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPethPerPseDeviceIndex.setStatus(_A)
class _RlPethPerPseTemperatureValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,200),ValueRangeConstraint(32767,32767))
_RlPethPerPseTemperatureValue_Type.__name__=_B
_RlPethPerPseTemperatureValue_Object=MibTableColumn
rlPethPerPseTemperatureValue=_RlPethPerPseTemperatureValue_Object((1,3,6,1,4,1,9,6,1,101,108,9,1,3),_RlPethPerPseTemperatureValue_Type())
rlPethPerPseTemperatureValue.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPerPseTemperatureValue.setStatus(_A)
class _RlPethPerPseHwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlPethPerPseHwRevision_Type.__name__=_I
_RlPethPerPseHwRevision_Object=MibTableColumn
rlPethPerPseHwRevision=_RlPethPerPseHwRevision_Object((1,3,6,1,4,1,9,6,1,101,108,9,1,4),_RlPethPerPseHwRevision_Type())
rlPethPerPseHwRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPerPseHwRevision.setStatus(_A)
class _RlPethPerPseVopStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('deviceOk',0),('detectionError',1),('classificationError',2),('legacyError',3),('undefinedState',4)))
_RlPethPerPseVopStatus_Type.__name__=_B
_RlPethPerPseVopStatus_Object=MibTableColumn
rlPethPerPseVopStatus=_RlPethPerPseVopStatus_Object((1,3,6,1,4,1,9,6,1,101,108,9,1,5),_RlPethPerPseVopStatus_Type())
rlPethPerPseVopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPerPseVopStatus.setStatus(_A)
class _RlPethPsePortReactivate_Type(PortList):defaultHexValue=''
_RlPethPsePortReactivate_Type.__name__=_L
_RlPethPsePortReactivate_Object=MibScalar
rlPethPsePortReactivate=_RlPethPsePortReactivate_Object((1,3,6,1,4,1,9,6,1,101,108,10),_RlPethPsePortReactivate_Type())
rlPethPsePortReactivate.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortReactivate.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RlPoeType':RlPoeType,'rlPoe':rlPoe,'rlPethPsePortTable':rlPethPsePortTable,'rlPethPsePortEntry':rlPethPsePortEntry,_O:rlPethPsePortGroupIndex,_P:rlPethPsePortIndex,'rlPethPsePortOutputVoltage':rlPethPsePortOutputVoltage,'rlPethPsePortOutputCurrent':rlPethPsePortOutputCurrent,'rlPethPsePortOutputPower':rlPethPsePortOutputPower,'rlPethPsePortPowerLimit':rlPethPsePortPowerLimit,'rlPethPsePortStatus':rlPethPsePortStatus,'rlPethPsePortStatusDescription':rlPethPsePortStatusDescription,'rlPethPsePortOperPowerLimit':rlPethPsePortOperPowerLimit,'rlPethPsePortTimeRangeName':rlPethPsePortTimeRangeName,'rlPethPsePortOperStatus':rlPethPsePortOperStatus,'rlPethPsePortMaxPowerAllocAllowed':rlPethPsePortMaxPowerAllocAllowed,'rlPethPsePortSupportPoeType':rlPethPsePortSupportPoeType,'rlPethPsePortLinkPartnerPoeType':rlPethPsePortLinkPartnerPoeType,'rlPethPsePortFourPairForced':rlPethPsePortFourPairForced,'rlPethPsePortFourPairEnabled':rlPethPsePortFourPairEnabled,'rlPethPsePortNegotiationAllocatedPower':rlPethPsePortNegotiationAllocatedPower,'rlPethPsePortNegotiationProtocolOwner':rlPethPsePortNegotiationProtocolOwner,'rlPethPsePortLegacySupport':rlPethPsePortLegacySupport,'rlPethPsePortHighPowerModeEnable':rlPethPsePortHighPowerModeEnable,'rlPethPsePortMenagementMode':rlPethPsePortMenagementMode,'rlPethPsePortStaticPowerAllocation':rlPethPsePortStaticPowerAllocation,'rlPethPsePortHighPowerOpStatus':rlPethPsePortHighPowerOpStatus,'rlPethPsePortClassLimit':rlPethPsePortClassLimit,'rlPethPsePortNegotiation':rlPethPsePortNegotiation,'rlPethMainPseTable':rlPethMainPseTable,'rlPethMainPseEntry':rlPethMainPseEntry,_V:rlPethMainPseGroupIndex,'rlPethMainPseSwVersion':rlPethMainPseSwVersion,'rlPethMainPseHwVersion':rlPethMainPseHwVersion,'rlPethMainPseHwType':rlPethMainPseHwType,'rlPethMainPsePowerGuardBand':rlPethMainPsePowerGuardBand,'rlPethMainPsePowerManagementMode':rlPethMainPsePowerManagementMode,'rlPethMainPsedisconnectMethod':rlPethMainPsedisconnectMethod,'rlPethMainPseTemperatureSensor':rlPethMainPseTemperatureSensor,'rlPethMainPseInrushTestEnabled':rlPethMainPseInrushTestEnabled,'rlPethMainPseLegacyDisabled':rlPethMainPseLegacyDisabled,'rlPethMainBanksValues':rlPethMainBanksValues,'rlPethMainBanksActivePowerBank':rlPethMainBanksActivePowerBank,'rlPethPowerPseTable':rlPethPowerPseTable,'rlPethPowerPseEntry':rlPethPowerPseEntry,_b:rlPethPowerPseGroupIndex,'rlPethPowerPsePower':rlPethPowerPsePower,'rlPethPowerPseRpsPower':rlPethPowerPseRpsPower,'rlPethPowerPsePowerManagementMode':rlPethPowerPsePowerManagementMode,'rlPethPowerPsedisconnectMethod':rlPethPowerPsedisconnectMethod,'rlPethPowerPseTemperatureSensor':rlPethPowerPseTemperatureSensor,'rlPethPowerPseInrushTestEnabled':rlPethPowerPseInrushTestEnabled,'rlPethPowerPseLegacyDisabled':rlPethPowerPseLegacyDisabled,'rlPethPowerBanksValues':rlPethPowerBanksValues,'rlPethPowerBanksActivePowerBank':rlPethPowerBanksActivePowerBank,'rlPethPdPortTable':rlPethPdPortTable,'rlPethPdPortEntry':rlPethPdPortEntry,_c:rlPethPdPortIndex,'rlPethPdPortSupportPoeType':rlPethPdPortSupportPoeType,'rlPethPdPortOperPoeType':rlPethPdPortOperPoeType,'rlPethPdPortPowerRequest':rlPethPdPortPowerRequest,'rlPethPdPortPowerAvailable':rlPethPdPortPowerAvailable,'rlPethPdPortForcedMode':rlPethPdPortForcedMode,'rlPethPdPortNegotiationProtocolOwner':rlPethPdPortNegotiationProtocolOwner,'rlPethPdPortNegotiationEnable':rlPethPdPortNegotiationEnable,'rlPethPdPortPoweredStatus':rlPethPdPortPoweredStatus,'rlPethPseUnitTable':rlPethPseUnitTable,'rlPethPseUnitEntry':rlPethPseUnitEntry,_d:rlPethUnitIndex,'rlPethUnitType':rlPethUnitType,'rlPethUnitColor':rlPethUnitColor,'rlPethPseCountersClear':rlPethPseCountersClear,'rlPoeClassErrorDetectionStatus':rlPoeClassErrorDetectionStatus,'rlPethPerPseTable':rlPethPerPseTable,'rlPethPerPseEntry':rlPethPerPseEntry,_e:rlPethPerPseGroupIndex,_f:rlPethPerPseDeviceIndex,'rlPethPerPseTemperatureValue':rlPethPerPseTemperatureValue,'rlPethPerPseHwRevision':rlPethPerPseHwRevision,'rlPethPerPseVopStatus':rlPethPerPseVopStatus,'rlPethPsePortReactivate':rlPethPsePortReactivate})