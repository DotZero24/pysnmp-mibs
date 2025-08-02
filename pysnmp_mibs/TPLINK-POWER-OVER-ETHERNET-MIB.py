_N='tpSystemPowerLimit'
_M='tpPoePortStatus'
_L='tpPoeProfileName'
_K='middle'
_J='enable'
_I='disable'
_H='read-create'
_G='OctetString'
_F='read-write'
_E='tpPoePortIndex'
_D='TPLINK-POWER-OVER-ETHERNET-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkPowerOverEthernetMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,56))
if mibBuilder.loadTexts:tplinkPowerOverEthernetMIB.setRevisions(('2013-07-03 00:00',))
_TplinkPoeMIBObjects_ObjectIdentity=ObjectIdentity
tplinkPoeMIBObjects=_TplinkPoeMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,56,1))
_TpPoeConfig_ObjectIdentity=ObjectIdentity
tpPoeConfig=_TpPoeConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,56,1,1))
_TpPoeGlobal_ObjectIdentity=ObjectIdentity
tpPoeGlobal=_TpPoeGlobal_ObjectIdentity((1,3,6,1,4,1,11863,6,56,1,1,1))
class _TpSystemPowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3200))
_TpSystemPowerLimit_Type.__name__=_B
_TpSystemPowerLimit_Object=MibScalar
tpSystemPowerLimit=_TpSystemPowerLimit_Object((1,3,6,1,4,1,11863,6,56,1,1,1,1),_TpSystemPowerLimit_Type())
tpSystemPowerLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:tpSystemPowerLimit.setStatus(_A)
class _TpPowerDisconnectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('deny-lower-priority',1))
_TpPowerDisconnectMethod_Type.__name__=_B
_TpPowerDisconnectMethod_Object=MibScalar
tpPowerDisconnectMethod=_TpPowerDisconnectMethod_Object((1,3,6,1,4,1,11863,6,56,1,1,1,2),_TpPowerDisconnectMethod_Type())
tpPowerDisconnectMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPowerDisconnectMethod.setStatus(_A)
class _TpSystemPowerConsumption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3200))
_TpSystemPowerConsumption_Type.__name__=_B
_TpSystemPowerConsumption_Object=MibScalar
tpSystemPowerConsumption=_TpSystemPowerConsumption_Object((1,3,6,1,4,1,11863,6,56,1,1,1,3),_TpSystemPowerConsumption_Type())
tpSystemPowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:tpSystemPowerConsumption.setStatus(_A)
class _TpSystemPowerRemain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3200))
_TpSystemPowerRemain_Type.__name__=_B
_TpSystemPowerRemain_Object=MibScalar
tpSystemPowerRemain=_TpSystemPowerRemain_Object((1,3,6,1,4,1,11863,6,56,1,1,1,4),_TpSystemPowerRemain_Type())
tpSystemPowerRemain.setMaxAccess(_C)
if mibBuilder.loadTexts:tpSystemPowerRemain.setStatus(_A)
_TpPoePort_ObjectIdentity=ObjectIdentity
tpPoePort=_TpPoePort_ObjectIdentity((1,3,6,1,4,1,11863,6,56,1,1,2))
_TpPoePortConfigTable_Object=MibTable
tpPoePortConfigTable=_TpPoePortConfigTable_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1))
if mibBuilder.loadTexts:tpPoePortConfigTable.setStatus(_A)
_TpPoePortConfigEntry_Object=MibTableRow
tpPoePortConfigEntry=_TpPoePortConfigEntry_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1))
tpPoePortConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tpPoePortConfigEntry.setStatus(_A)
_TpPoePortIndex_Type=Integer32
_TpPoePortIndex_Object=MibTableColumn
tpPoePortIndex=_TpPoePortIndex_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,1),_TpPoePortIndex_Type())
tpPoePortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPoePortIndex.setStatus(_A)
class _TpPoePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_TpPoePortStatus_Type.__name__=_B
_TpPoePortStatus_Object=MibTableColumn
tpPoePortStatus=_TpPoePortStatus_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,2),_TpPoePortStatus_Type())
tpPoePortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:tpPoePortStatus.setStatus(_A)
class _TpPoePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('high',0),(_K,1),('low',2)))
_TpPoePriority_Type.__name__=_B
_TpPoePriority_Object=MibTableColumn
tpPoePriority=_TpPoePriority_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,3),_TpPoePriority_Type())
tpPoePriority.setMaxAccess(_F)
if mibBuilder.loadTexts:tpPoePriority.setStatus(_A)
class _TpPoePowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_TpPoePowerLimit_Type.__name__=_B
_TpPoePowerLimit_Object=MibTableColumn
tpPoePowerLimit=_TpPoePowerLimit_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,4),_TpPoePowerLimit_Type())
tpPoePowerLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:tpPoePowerLimit.setStatus(_A)
class _TpPoePortTimeRangeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpPoePortTimeRangeName_Type.__name__=_G
_TpPoePortTimeRangeName_Object=MibTableColumn
tpPoePortTimeRangeName=_TpPoePortTimeRangeName_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,5),_TpPoePortTimeRangeName_Type())
tpPoePortTimeRangeName.setMaxAccess(_F)
if mibBuilder.loadTexts:tpPoePortTimeRangeName.setStatus(_A)
class _TpPoePortProfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpPoePortProfileName_Type.__name__=_G
_TpPoePortProfileName_Object=MibTableColumn
tpPoePortProfileName=_TpPoePortProfileName_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,6),_TpPoePortProfileName_Type())
tpPoePortProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:tpPoePortProfileName.setStatus(_A)
class _TpPoePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_TpPoePower_Type.__name__=_B
_TpPoePower_Object=MibTableColumn
tpPoePower=_TpPoePower_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,7),_TpPoePower_Type())
tpPoePower.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPoePower.setStatus(_A)
class _TpPoeCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_TpPoeCurrent_Type.__name__=_B
_TpPoeCurrent_Object=MibTableColumn
tpPoeCurrent=_TpPoeCurrent_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,8),_TpPoeCurrent_Type())
tpPoeCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPoeCurrent.setStatus(_A)
class _TpPoeVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_TpPoeVoltage_Type.__name__=_B
_TpPoeVoltage_Object=MibTableColumn
tpPoeVoltage=_TpPoeVoltage_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,9),_TpPoeVoltage_Type())
tpPoeVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPoeVoltage.setStatus(_A)
class _TpPoeClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,7)));namedValues=NamedValues(*(('class0',0),('class1',1),('class2',2),('class3',3),('class4',4),('class-not-defined',7)))
_TpPoeClass_Type.__name__=_B
_TpPoeClass_Object=MibTableColumn
tpPoeClass=_TpPoeClass_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,10),_TpPoeClass_Type())
tpPoeClass.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPoeClass.setStatus(_A)
class _TpPoePowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('off',0),('turning-on',1),('on',2),('overload',3),('short',4),('nonstandard-pd',5),('voltage-high',6),('voltage-low',7),('hardware-fault',8),('overtemperature',9)))
_TpPoePowerStatus_Type.__name__=_B
_TpPoePowerStatus_Object=MibTableColumn
tpPoePowerStatus=_TpPoePowerStatus_Object((1,3,6,1,4,1,11863,6,56,1,1,2,1,1,11),_TpPoePowerStatus_Type())
tpPoePowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPoePowerStatus.setStatus(_A)
_TpPoeProfile_ObjectIdentity=ObjectIdentity
tpPoeProfile=_TpPoeProfile_ObjectIdentity((1,3,6,1,4,1,11863,6,56,1,2))
_TpPoeProfileTable_Object=MibTable
tpPoeProfileTable=_TpPoeProfileTable_Object((1,3,6,1,4,1,11863,6,56,1,2,1))
if mibBuilder.loadTexts:tpPoeProfileTable.setStatus(_A)
_TpPoeProfileEntry_Object=MibTableRow
tpPoeProfileEntry=_TpPoeProfileEntry_Object((1,3,6,1,4,1,11863,6,56,1,2,1,1))
tpPoeProfileEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:tpPoeProfileEntry.setStatus(_A)
_TpPoeProfileIndex_Type=Integer32
_TpPoeProfileIndex_Object=MibTableColumn
tpPoeProfileIndex=_TpPoeProfileIndex_Object((1,3,6,1,4,1,11863,6,56,1,2,1,1,1),_TpPoeProfileIndex_Type())
tpPoeProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPoeProfileIndex.setStatus(_A)
class _TpPoeProfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpPoeProfileName_Type.__name__=_G
_TpPoeProfileName_Object=MibTableColumn
tpPoeProfileName=_TpPoeProfileName_Object((1,3,6,1,4,1,11863,6,56,1,2,1,1,2),_TpPoeProfileName_Type())
tpPoeProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPoeProfileName.setStatus(_A)
class _TpPoeProfilePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_TpPoeProfilePortStatus_Type.__name__=_B
_TpPoeProfilePortStatus_Object=MibTableColumn
tpPoeProfilePortStatus=_TpPoeProfilePortStatus_Object((1,3,6,1,4,1,11863,6,56,1,2,1,1,3),_TpPoeProfilePortStatus_Type())
tpPoeProfilePortStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:tpPoeProfilePortStatus.setStatus(_A)
class _TpPoeProfilePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('high',0),(_K,1),('low',2)))
_TpPoeProfilePriority_Type.__name__=_B
_TpPoeProfilePriority_Object=MibTableColumn
tpPoeProfilePriority=_TpPoeProfilePriority_Object((1,3,6,1,4,1,11863,6,56,1,2,1,1,4),_TpPoeProfilePriority_Type())
tpPoeProfilePriority.setMaxAccess(_H)
if mibBuilder.loadTexts:tpPoeProfilePriority.setStatus(_A)
class _TpPoeProfilePowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_TpPoeProfilePowerLimit_Type.__name__=_B
_TpPoeProfilePowerLimit_Object=MibTableColumn
tpPoeProfilePowerLimit=_TpPoeProfilePowerLimit_Object((1,3,6,1,4,1,11863,6,56,1,2,1,1,5),_TpPoeProfilePowerLimit_Type())
tpPoeProfilePowerLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:tpPoeProfilePowerLimit.setStatus(_A)
_TpPoeProfileStatus_Type=TPRowStatus
_TpPoeProfileStatus_Object=MibTableColumn
tpPoeProfileStatus=_TpPoeProfileStatus_Object((1,3,6,1,4,1,11863,6,56,1,2,1,1,6),_TpPoeProfileStatus_Type())
tpPoeProfileStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:tpPoeProfileStatus.setStatus(_A)
_TplinkPoeNotifications_ObjectIdentity=ObjectIdentity
tplinkPoeNotifications=_TplinkPoeNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,56,2))
tpPoePortPowerChange=NotificationType((1,3,6,1,4,1,11863,6,56,2,1))
tpPoePortPowerChange.setObjects(*((_D,_E),(_D,_M)))
if mibBuilder.loadTexts:tpPoePortPowerChange.setStatus(_A)
tpPoePortPowerOverLoading=NotificationType((1,3,6,1,4,1,11863,6,56,2,2))
tpPoePortPowerOverLoading.setObjects((_D,_E))
if mibBuilder.loadTexts:tpPoePortPowerOverLoading.setStatus(_A)
tpPoePortShortCircuit=NotificationType((1,3,6,1,4,1,11863,6,56,2,3))
tpPoePortShortCircuit.setObjects((_D,_E))
if mibBuilder.loadTexts:tpPoePortShortCircuit.setStatus(_A)
tpPoePortPowerOver30Watts=NotificationType((1,3,6,1,4,1,11863,6,56,2,4))
tpPoePortPowerOver30Watts.setObjects((_D,_E))
if mibBuilder.loadTexts:tpPoePortPowerOver30Watts.setStatus(_A)
tpPoePortPowerDeny=NotificationType((1,3,6,1,4,1,11863,6,56,2,5))
tpPoePortPowerDeny.setObjects((_D,_E))
if mibBuilder.loadTexts:tpPoePortPowerDeny.setStatus(_A)
tpPoeThermalShutdown=NotificationType((1,3,6,1,4,1,11863,6,56,2,6))
tpPoeThermalShutdown.setObjects((_D,_E))
if mibBuilder.loadTexts:tpPoeThermalShutdown.setStatus(_A)
tpPoeOverMaxPowerBudget=NotificationType((1,3,6,1,4,1,11863,6,56,2,7))
tpPoeOverMaxPowerBudget.setObjects((_D,_N))
if mibBuilder.loadTexts:tpPoeOverMaxPowerBudget.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'tplinkPowerOverEthernetMIB':tplinkPowerOverEthernetMIB,'tplinkPoeMIBObjects':tplinkPoeMIBObjects,'tpPoeConfig':tpPoeConfig,'tpPoeGlobal':tpPoeGlobal,_N:tpSystemPowerLimit,'tpPowerDisconnectMethod':tpPowerDisconnectMethod,'tpSystemPowerConsumption':tpSystemPowerConsumption,'tpSystemPowerRemain':tpSystemPowerRemain,'tpPoePort':tpPoePort,'tpPoePortConfigTable':tpPoePortConfigTable,'tpPoePortConfigEntry':tpPoePortConfigEntry,_E:tpPoePortIndex,_M:tpPoePortStatus,'tpPoePriority':tpPoePriority,'tpPoePowerLimit':tpPoePowerLimit,'tpPoePortTimeRangeName':tpPoePortTimeRangeName,'tpPoePortProfileName':tpPoePortProfileName,'tpPoePower':tpPoePower,'tpPoeCurrent':tpPoeCurrent,'tpPoeVoltage':tpPoeVoltage,'tpPoeClass':tpPoeClass,'tpPoePowerStatus':tpPoePowerStatus,'tpPoeProfile':tpPoeProfile,'tpPoeProfileTable':tpPoeProfileTable,'tpPoeProfileEntry':tpPoeProfileEntry,'tpPoeProfileIndex':tpPoeProfileIndex,_L:tpPoeProfileName,'tpPoeProfilePortStatus':tpPoeProfilePortStatus,'tpPoeProfilePriority':tpPoeProfilePriority,'tpPoeProfilePowerLimit':tpPoeProfilePowerLimit,'tpPoeProfileStatus':tpPoeProfileStatus,'tplinkPoeNotifications':tplinkPoeNotifications,'tpPoePortPowerChange':tpPoePortPowerChange,'tpPoePortPowerOverLoading':tpPoePortPowerOverLoading,'tpPoePortShortCircuit':tpPoePortShortCircuit,'tpPoePortPowerOver30Watts':tpPoePortPowerOver30Watts,'tpPoePortPowerDeny':tpPoePortPowerDeny,'tpPoeThermalShutdown':tpPoeThermalShutdown,'tpPoeOverMaxPowerBudget':tpPoeOverMaxPowerBudget})