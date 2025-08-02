_M='disabled'
_L='enabled'
_K='rlPethPowerPseGroupIndex'
_J='rlPethMainPseGroupIndex'
_I='rlPethPsePortIndex'
_H='rlPethPsePortGroupIndex'
_G='not-accessible'
_F='Dell-POE-MIB'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('Dell-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TruthValue')
rlPoe=ModuleIdentity((1,3,6,1,4,1,89,108))
if mibBuilder.loadTexts:rlPoe.setRevisions(('2010-06-02 00:00','2009-11-26 00:00'))
_RlPethPsePortTable_Object=MibTable
rlPethPsePortTable=_RlPethPsePortTable_Object((1,3,6,1,4,1,89,108,1))
if mibBuilder.loadTexts:rlPethPsePortTable.setStatus(_A)
_RlPethPsePortEntry_Object=MibTableRow
rlPethPsePortEntry=_RlPethPsePortEntry_Object((1,3,6,1,4,1,89,108,1,1))
rlPethPsePortEntry.setIndexNames((0,_F,_H),(0,_F,_I))
if mibBuilder.loadTexts:rlPethPsePortEntry.setStatus(_A)
class _RlPethPsePortGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlPethPsePortGroupIndex_Type.__name__=_B
_RlPethPsePortGroupIndex_Object=MibTableColumn
rlPethPsePortGroupIndex=_RlPethPsePortGroupIndex_Object((1,3,6,1,4,1,89,108,1,1,1),_RlPethPsePortGroupIndex_Type())
rlPethPsePortGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPethPsePortGroupIndex.setStatus(_A)
class _RlPethPsePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlPethPsePortIndex_Type.__name__=_B
_RlPethPsePortIndex_Object=MibTableColumn
rlPethPsePortIndex=_RlPethPsePortIndex_Object((1,3,6,1,4,1,89,108,1,1,2),_RlPethPsePortIndex_Type())
rlPethPsePortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPethPsePortIndex.setStatus(_A)
class _RlPethPsePortOutputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortOutputVoltage_Type.__name__=_B
_RlPethPsePortOutputVoltage_Object=MibTableColumn
rlPethPsePortOutputVoltage=_RlPethPsePortOutputVoltage_Object((1,3,6,1,4,1,89,108,1,1,3),_RlPethPsePortOutputVoltage_Type())
rlPethPsePortOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOutputVoltage.setStatus(_A)
class _RlPethPsePortOutputCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortOutputCurrent_Type.__name__=_B
_RlPethPsePortOutputCurrent_Object=MibTableColumn
rlPethPsePortOutputCurrent=_RlPethPsePortOutputCurrent_Object((1,3,6,1,4,1,89,108,1,1,4),_RlPethPsePortOutputCurrent_Type())
rlPethPsePortOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOutputCurrent.setStatus(_A)
class _RlPethPsePortOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortOutputPower_Type.__name__=_B
_RlPethPsePortOutputPower_Object=MibTableColumn
rlPethPsePortOutputPower=_RlPethPsePortOutputPower_Object((1,3,6,1,4,1,89,108,1,1,5),_RlPethPsePortOutputPower_Type())
rlPethPsePortOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOutputPower.setStatus(_A)
class _RlPethPsePortPowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortPowerLimit_Type.__name__=_B
_RlPethPsePortPowerLimit_Object=MibTableColumn
rlPethPsePortPowerLimit=_RlPethPsePortPowerLimit_Object((1,3,6,1,4,1,89,108,1,1,6),_RlPethPsePortPowerLimit_Type())
rlPethPsePortPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortPowerLimit.setStatus(_A)
class _RlPethPsePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortStatus_Type.__name__=_B
_RlPethPsePortStatus_Object=MibTableColumn
rlPethPsePortStatus=_RlPethPsePortStatus_Object((1,3,6,1,4,1,89,108,1,1,7),_RlPethPsePortStatus_Type())
rlPethPsePortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortStatus.setStatus(_A)
class _RlPethPsePortStatusDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RlPethPsePortStatusDescription_Type.__name__=_E
_RlPethPsePortStatusDescription_Object=MibTableColumn
rlPethPsePortStatusDescription=_RlPethPsePortStatusDescription_Object((1,3,6,1,4,1,89,108,1,1,8),_RlPethPsePortStatusDescription_Type())
rlPethPsePortStatusDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortStatusDescription.setStatus(_A)
class _RlPethPsePortOperPowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortOperPowerLimit_Type.__name__=_B
_RlPethPsePortOperPowerLimit_Object=MibTableColumn
rlPethPsePortOperPowerLimit=_RlPethPsePortOperPowerLimit_Object((1,3,6,1,4,1,89,108,1,1,9),_RlPethPsePortOperPowerLimit_Type())
rlPethPsePortOperPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOperPowerLimit.setStatus(_A)
_RlPethPsePortSupportPoePlus_Type=TruthValue
_RlPethPsePortSupportPoePlus_Object=MibTableColumn
rlPethPsePortSupportPoePlus=_RlPethPsePortSupportPoePlus_Object((1,3,6,1,4,1,89,108,1,1,10),_RlPethPsePortSupportPoePlus_Type())
rlPethPsePortSupportPoePlus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortSupportPoePlus.setStatus(_A)
class _RlPethPsePortTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlPethPsePortTimeRangeName_Type.__name__=_E
_RlPethPsePortTimeRangeName_Object=MibTableColumn
rlPethPsePortTimeRangeName=_RlPethPsePortTimeRangeName_Object((1,3,6,1,4,1,89,108,1,1,11),_RlPethPsePortTimeRangeName_Type())
rlPethPsePortTimeRangeName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPsePortTimeRangeName.setStatus(_A)
_RlPethPsePortOperStatus_Type=TruthValue
_RlPethPsePortOperStatus_Object=MibTableColumn
rlPethPsePortOperStatus=_RlPethPsePortOperStatus_Object((1,3,6,1,4,1,89,108,1,1,12),_RlPethPsePortOperStatus_Type())
rlPethPsePortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortOperStatus.setStatus(_A)
class _RlPethPsePortMaxPowerAllocAllowed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPsePortMaxPowerAllocAllowed_Type.__name__=_B
_RlPethPsePortMaxPowerAllocAllowed_Object=MibTableColumn
rlPethPsePortMaxPowerAllocAllowed=_RlPethPsePortMaxPowerAllocAllowed_Object((1,3,6,1,4,1,89,108,1,1,13),_RlPethPsePortMaxPowerAllocAllowed_Type())
rlPethPsePortMaxPowerAllocAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortMaxPowerAllocAllowed.setStatus(_A)
_RlPethPsePortSupportPoe_Type=TruthValue
_RlPethPsePortSupportPoe_Object=MibTableColumn
rlPethPsePortSupportPoe=_RlPethPsePortSupportPoe_Object((1,3,6,1,4,1,89,108,1,1,14),_RlPethPsePortSupportPoe_Type())
rlPethPsePortSupportPoe.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPsePortSupportPoe.setStatus(_A)
_RlPethMainPseTable_Object=MibTable
rlPethMainPseTable=_RlPethMainPseTable_Object((1,3,6,1,4,1,89,108,2))
if mibBuilder.loadTexts:rlPethMainPseTable.setStatus(_A)
_RlPethMainPseEntry_Object=MibTableRow
rlPethMainPseEntry=_RlPethMainPseEntry_Object((1,3,6,1,4,1,89,108,2,1))
rlPethMainPseEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:rlPethMainPseEntry.setStatus(_A)
class _RlPethMainPseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlPethMainPseGroupIndex_Type.__name__=_B
_RlPethMainPseGroupIndex_Object=MibTableColumn
rlPethMainPseGroupIndex=_RlPethMainPseGroupIndex_Object((1,3,6,1,4,1,89,108,2,1,1),_RlPethMainPseGroupIndex_Type())
rlPethMainPseGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPethMainPseGroupIndex.setStatus(_A)
class _RlPethMainPseSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlPethMainPseSwVersion_Type.__name__=_E
_RlPethMainPseSwVersion_Object=MibTableColumn
rlPethMainPseSwVersion=_RlPethMainPseSwVersion_Object((1,3,6,1,4,1,89,108,2,1,2),_RlPethMainPseSwVersion_Type())
rlPethMainPseSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainPseSwVersion.setStatus(_A)
class _RlPethMainPseHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlPethMainPseHwVersion_Type.__name__=_E
_RlPethMainPseHwVersion_Object=MibTableColumn
rlPethMainPseHwVersion=_RlPethMainPseHwVersion_Object((1,3,6,1,4,1,89,108,2,1,3),_RlPethMainPseHwVersion_Type())
rlPethMainPseHwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainPseHwVersion.setStatus(_A)
class _RlPethMainPseHwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('enhanced',1),('plus',2),('auto',3),('nonPoe',4),('enhancedPlus',5)))
_RlPethMainPseHwType_Type.__name__=_B
_RlPethMainPseHwType_Object=MibTableColumn
rlPethMainPseHwType=_RlPethMainPseHwType_Object((1,3,6,1,4,1,89,108,2,1,4),_RlPethMainPseHwType_Type())
rlPethMainPseHwType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainPseHwType.setStatus(_A)
class _RlPethMainPsePowerGuardBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethMainPsePowerGuardBand_Type.__name__=_B
_RlPethMainPsePowerGuardBand_Object=MibTableColumn
rlPethMainPsePowerGuardBand=_RlPethMainPsePowerGuardBand_Object((1,3,6,1,4,1,89,108,2,1,5),_RlPethMainPsePowerGuardBand_Type())
rlPethMainPsePowerGuardBand.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethMainPsePowerGuardBand.setStatus(_A)
_RlPethPowerPseTable_Object=MibTable
rlPethPowerPseTable=_RlPethPowerPseTable_Object((1,3,6,1,4,1,89,108,3))
if mibBuilder.loadTexts:rlPethPowerPseTable.setStatus(_A)
_RlPethPowerPseEntry_Object=MibTableRow
rlPethPowerPseEntry=_RlPethPowerPseEntry_Object((1,3,6,1,4,1,89,108,3,1))
rlPethPowerPseEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:rlPethPowerPseEntry.setStatus(_A)
class _RlPethPowerPseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlPethPowerPseGroupIndex_Type.__name__=_B
_RlPethPowerPseGroupIndex_Object=MibTableColumn
rlPethPowerPseGroupIndex=_RlPethPowerPseGroupIndex_Object((1,3,6,1,4,1,89,108,3,1,1),_RlPethPowerPseGroupIndex_Type())
rlPethPowerPseGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPethPowerPseGroupIndex.setStatus(_A)
class _RlPethPowerPsePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('ps1',1),('ps2',2),('ps3',3)))
_RlPethPowerPsePower_Type.__name__=_B
_RlPethPowerPsePower_Object=MibTableColumn
rlPethPowerPsePower=_RlPethPowerPsePower_Object((1,3,6,1,4,1,89,108,3,1,2),_RlPethPowerPsePower_Type())
rlPethPowerPsePower.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPsePower.setStatus(_A)
class _RlPethPowerPseRpsPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('rps1',1),('rps2',2),('rps3',3)))
_RlPethPowerPseRpsPower_Type.__name__=_B
_RlPethPowerPseRpsPower_Object=MibTableColumn
rlPethPowerPseRpsPower=_RlPethPowerPseRpsPower_Object((1,3,6,1,4,1,89,108,3,1,3),_RlPethPowerPseRpsPower_Type())
rlPethPowerPseRpsPower.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPseRpsPower.setStatus(_A)
class _RlPethPowerPsePowerManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,6)));namedValues=NamedValues(*(('portlimit',0),('classlimit',5),('maxlimit',6)))
_RlPethPowerPsePowerManagementMode_Type.__name__=_B
_RlPethPowerPsePowerManagementMode_Object=MibTableColumn
rlPethPowerPsePowerManagementMode=_RlPethPowerPsePowerManagementMode_Object((1,3,6,1,4,1,89,108,3,1,4),_RlPethPowerPsePowerManagementMode_Type())
rlPethPowerPsePowerManagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPsePowerManagementMode.setStatus(_A)
class _RlPethPowerPsedisconnectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('lowestpriority',0),('nextport',1)))
_RlPethPowerPsedisconnectMethod_Type.__name__=_B
_RlPethPowerPsedisconnectMethod_Object=MibTableColumn
rlPethPowerPsedisconnectMethod=_RlPethPowerPsedisconnectMethod_Object((1,3,6,1,4,1,89,108,3,1,5),_RlPethPowerPsedisconnectMethod_Type())
rlPethPowerPsedisconnectMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPsedisconnectMethod.setStatus(_A)
class _RlPethPowerPseTemperatureSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,200))
_RlPethPowerPseTemperatureSensor_Type.__name__=_B
_RlPethPowerPseTemperatureSensor_Object=MibTableColumn
rlPethPowerPseTemperatureSensor=_RlPethPowerPseTemperatureSensor_Object((1,3,6,1,4,1,89,108,3,1,6),_RlPethPowerPseTemperatureSensor_Type())
rlPethPowerPseTemperatureSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPethPowerPseTemperatureSensor.setStatus(_A)
class _RlPethPowerPseInrushTestEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_RlPethPowerPseInrushTestEnabled_Type.__name__=_B
_RlPethPowerPseInrushTestEnabled_Object=MibTableColumn
rlPethPowerPseInrushTestEnabled=_RlPethPowerPseInrushTestEnabled_Object((1,3,6,1,4,1,89,108,3,1,7),_RlPethPowerPseInrushTestEnabled_Type())
rlPethPowerPseInrushTestEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPseInrushTestEnabled.setStatus(_A)
class _RlPethPowerPseLegacyDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_RlPethPowerPseLegacyDisabled_Type.__name__=_B
_RlPethPowerPseLegacyDisabled_Object=MibTableColumn
rlPethPowerPseLegacyDisabled=_RlPethPowerPseLegacyDisabled_Object((1,3,6,1,4,1,89,108,3,1,8),_RlPethPowerPseLegacyDisabled_Type())
rlPethPowerPseLegacyDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPethPowerPseLegacyDisabled.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rlPoe':rlPoe,'rlPethPsePortTable':rlPethPsePortTable,'rlPethPsePortEntry':rlPethPsePortEntry,_H:rlPethPsePortGroupIndex,_I:rlPethPsePortIndex,'rlPethPsePortOutputVoltage':rlPethPsePortOutputVoltage,'rlPethPsePortOutputCurrent':rlPethPsePortOutputCurrent,'rlPethPsePortOutputPower':rlPethPsePortOutputPower,'rlPethPsePortPowerLimit':rlPethPsePortPowerLimit,'rlPethPsePortStatus':rlPethPsePortStatus,'rlPethPsePortStatusDescription':rlPethPsePortStatusDescription,'rlPethPsePortOperPowerLimit':rlPethPsePortOperPowerLimit,'rlPethPsePortSupportPoePlus':rlPethPsePortSupportPoePlus,'rlPethPsePortTimeRangeName':rlPethPsePortTimeRangeName,'rlPethPsePortOperStatus':rlPethPsePortOperStatus,'rlPethPsePortMaxPowerAllocAllowed':rlPethPsePortMaxPowerAllocAllowed,'rlPethPsePortSupportPoe':rlPethPsePortSupportPoe,'rlPethMainPseTable':rlPethMainPseTable,'rlPethMainPseEntry':rlPethMainPseEntry,_J:rlPethMainPseGroupIndex,'rlPethMainPseSwVersion':rlPethMainPseSwVersion,'rlPethMainPseHwVersion':rlPethMainPseHwVersion,'rlPethMainPseHwType':rlPethMainPseHwType,'rlPethMainPsePowerGuardBand':rlPethMainPsePowerGuardBand,'rlPethPowerPseTable':rlPethPowerPseTable,'rlPethPowerPseEntry':rlPethPowerPseEntry,_K:rlPethPowerPseGroupIndex,'rlPethPowerPsePower':rlPethPowerPsePower,'rlPethPowerPseRpsPower':rlPethPowerPseRpsPower,'rlPethPowerPsePowerManagementMode':rlPethPowerPsePowerManagementMode,'rlPethPowerPsedisconnectMethod':rlPethPowerPsedisconnectMethod,'rlPethPowerPseTemperatureSensor':rlPethPowerPseTemperatureSensor,'rlPethPowerPseInrushTestEnabled':rlPethPowerPseInrushTestEnabled,'rlPethPowerPseLegacyDisabled':rlPethPowerPseLegacyDisabled})