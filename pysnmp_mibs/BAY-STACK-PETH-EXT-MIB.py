_O='bspeIpPhonePowerPriority'
_N='bspeIpPhonePowerLimit'
_M='bspePethPsePortExtCurrentStatus'
_L='bspePethMainPseExtGroupIndex'
_K='bspePethPsePortExtIndex'
_J='bspePethPsePortExtGroupIndex'
_I='not-accessible'
_H='ifIndex'
_G='IF-MIB'
_F='Gauge32'
_E='read-only'
_D='BAY-STACK-PETH-EXT-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_F,_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackPethExtMib=ModuleIdentity((1,3,6,1,4,1,45,5,8))
if mibBuilder.loadTexts:bayStackPethExtMib.setRevisions(('2020-03-17 00:00','2019-11-21 00:00','2016-03-03 00:00','2015-12-09 00:00','2015-11-17 00:00','2015-07-06 00:00','2012-01-25 00:00','2011-07-20 00:00','2011-01-10 00:00','2004-11-11 00:00','2004-10-18 00:00','2004-09-14 00:00'))
_BspeNotifications_ObjectIdentity=ObjectIdentity
bspeNotifications=_BspeNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,8,0))
_BspeObjects_ObjectIdentity=ObjectIdentity
bspeObjects=_BspeObjects_ObjectIdentity((1,3,6,1,4,1,45,5,8,1))
_BspePethPsePortExtTable_Object=MibTable
bspePethPsePortExtTable=_BspePethPsePortExtTable_Object((1,3,6,1,4,1,45,5,8,1,1))
if mibBuilder.loadTexts:bspePethPsePortExtTable.setStatus(_A)
_BspePethPsePortExtEntry_Object=MibTableRow
bspePethPsePortExtEntry=_BspePethPsePortExtEntry_Object((1,3,6,1,4,1,45,5,8,1,1,1))
bspePethPsePortExtEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:bspePethPsePortExtEntry.setStatus(_A)
class _BspePethPsePortExtGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BspePethPsePortExtGroupIndex_Type.__name__=_B
_BspePethPsePortExtGroupIndex_Object=MibTableColumn
bspePethPsePortExtGroupIndex=_BspePethPsePortExtGroupIndex_Object((1,3,6,1,4,1,45,5,8,1,1,1,1),_BspePethPsePortExtGroupIndex_Type())
bspePethPsePortExtGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:bspePethPsePortExtGroupIndex.setStatus(_A)
class _BspePethPsePortExtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BspePethPsePortExtIndex_Type.__name__=_B
_BspePethPsePortExtIndex_Object=MibTableColumn
bspePethPsePortExtIndex=_BspePethPsePortExtIndex_Object((1,3,6,1,4,1,45,5,8,1,1,1,2),_BspePethPsePortExtIndex_Type())
bspePethPsePortExtIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:bspePethPsePortExtIndex.setStatus(_A)
class _BspePethPsePortExtPowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,98))
_BspePethPsePortExtPowerLimit_Type.__name__=_B
_BspePethPsePortExtPowerLimit_Object=MibTableColumn
bspePethPsePortExtPowerLimit=_BspePethPsePortExtPowerLimit_Object((1,3,6,1,4,1,45,5,8,1,1,1,3),_BspePethPsePortExtPowerLimit_Type())
bspePethPsePortExtPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethPsePortExtPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:bspePethPsePortExtPowerLimit.setUnits('watts')
class _BspePethPsePortExtDetailedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('poweredResistiveDiscovery',1),('poweredCapacitiveDiscovery',2),('poweredCiscoLegacyDiscovery',3),('invalidPD',4),('overloadFault',5),('underloadFault',6),('uvovFault',7),('powerManaged',8),('limitOverloadFault',9),('discoveryDisabled',10),('unableToResetTps',11),('unableToInitializeTps',12),('uninitialized',13),('nonexistent',14),('otherFault',15),('detectionStatus',16)))
_BspePethPsePortExtDetailedStatus_Type.__name__=_B
_BspePethPsePortExtDetailedStatus_Object=MibTableColumn
bspePethPsePortExtDetailedStatus=_BspePethPsePortExtDetailedStatus_Object((1,3,6,1,4,1,45,5,8,1,1,1,4),_BspePethPsePortExtDetailedStatus_Type())
bspePethPsePortExtDetailedStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:bspePethPsePortExtDetailedStatus.setStatus(_A)
class _BspePethPsePortExtMeasuredVoltage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(400,580))
_BspePethPsePortExtMeasuredVoltage_Type.__name__=_F
_BspePethPsePortExtMeasuredVoltage_Object=MibTableColumn
bspePethPsePortExtMeasuredVoltage=_BspePethPsePortExtMeasuredVoltage_Object((1,3,6,1,4,1,45,5,8,1,1,1,5),_BspePethPsePortExtMeasuredVoltage_Type())
bspePethPsePortExtMeasuredVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:bspePethPsePortExtMeasuredVoltage.setStatus(_A)
if mibBuilder.loadTexts:bspePethPsePortExtMeasuredVoltage.setUnits('decivolts')
class _BspePethPsePortExtMeasuredCurrent_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1920))
_BspePethPsePortExtMeasuredCurrent_Type.__name__=_F
_BspePethPsePortExtMeasuredCurrent_Object=MibTableColumn
bspePethPsePortExtMeasuredCurrent=_BspePethPsePortExtMeasuredCurrent_Object((1,3,6,1,4,1,45,5,8,1,1,1,6),_BspePethPsePortExtMeasuredCurrent_Type())
bspePethPsePortExtMeasuredCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:bspePethPsePortExtMeasuredCurrent.setStatus(_A)
if mibBuilder.loadTexts:bspePethPsePortExtMeasuredCurrent.setUnits('milliamps')
class _BspePethPsePortExtMeasuredPower_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,98000))
_BspePethPsePortExtMeasuredPower_Type.__name__=_F
_BspePethPsePortExtMeasuredPower_Object=MibTableColumn
bspePethPsePortExtMeasuredPower=_BspePethPsePortExtMeasuredPower_Object((1,3,6,1,4,1,45,5,8,1,1,1,7),_BspePethPsePortExtMeasuredPower_Type())
bspePethPsePortExtMeasuredPower.setMaxAccess(_E)
if mibBuilder.loadTexts:bspePethPsePortExtMeasuredPower.setStatus(_A)
if mibBuilder.loadTexts:bspePethPsePortExtMeasuredPower.setUnits('milliwatts')
class _BspePethPsePortExtCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('underCurrent',2),('overCurrent',3),('both',4)))
_BspePethPsePortExtCurrentStatus_Type.__name__=_B
_BspePethPsePortExtCurrentStatus_Object=MibTableColumn
bspePethPsePortExtCurrentStatus=_BspePethPsePortExtCurrentStatus_Object((1,3,6,1,4,1,45,5,8,1,1,1,8),_BspePethPsePortExtCurrentStatus_Type())
bspePethPsePortExtCurrentStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:bspePethPsePortExtCurrentStatus.setStatus(_A)
class _BspePethPsePortExtCurrentStatusClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('off',2)))
_BspePethPsePortExtCurrentStatusClear_Type.__name__=_B
_BspePethPsePortExtCurrentStatusClear_Object=MibTableColumn
bspePethPsePortExtCurrentStatusClear=_BspePethPsePortExtCurrentStatusClear_Object((1,3,6,1,4,1,45,5,8,1,1,1,9),_BspePethPsePortExtCurrentStatusClear_Type())
bspePethPsePortExtCurrentStatusClear.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethPsePortExtCurrentStatusClear.setStatus(_A)
class _BspePethPsePortExtPowerUpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dot3af',1),('highInrush',2),('pre802dot3at',3),('dot3at',4)))
_BspePethPsePortExtPowerUpMode_Type.__name__=_B
_BspePethPsePortExtPowerUpMode_Object=MibTableColumn
bspePethPsePortExtPowerUpMode=_BspePethPsePortExtPowerUpMode_Object((1,3,6,1,4,1,45,5,8,1,1,1,10),_BspePethPsePortExtPowerUpMode_Type())
bspePethPsePortExtPowerUpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethPsePortExtPowerUpMode.setStatus(_A)
class _BspePethPsePortExtPowerPairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('signal',1),('spare',2),('both',3)))
_BspePethPsePortExtPowerPairs_Type.__name__=_B
_BspePethPsePortExtPowerPairs_Object=MibTableColumn
bspePethPsePortExtPowerPairs=_BspePethPsePortExtPowerPairs_Object((1,3,6,1,4,1,45,5,8,1,1,1,11),_BspePethPsePortExtPowerPairs_Type())
bspePethPsePortExtPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethPsePortExtPowerPairs.setStatus(_A)
class _BspePethPsePortExtLldp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_BspePethPsePortExtLldp_Type.__name__=_B
_BspePethPsePortExtLldp_Object=MibTableColumn
bspePethPsePortExtLldp=_BspePethPsePortExtLldp_Object((1,3,6,1,4,1,45,5,8,1,1,1,12),_BspePethPsePortExtLldp_Type())
bspePethPsePortExtLldp.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethPsePortExtLldp.setStatus(_A)
_BspePethPsePortFastPoeEnable_Type=TruthValue
_BspePethPsePortFastPoeEnable_Object=MibTableColumn
bspePethPsePortFastPoeEnable=_BspePethPsePortFastPoeEnable_Object((1,3,6,1,4,1,45,5,8,1,1,1,13),_BspePethPsePortFastPoeEnable_Type())
bspePethPsePortFastPoeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethPsePortFastPoeEnable.setStatus(_A)
_BspePethPsePortPerpetualPoeEnable_Type=TruthValue
_BspePethPsePortPerpetualPoeEnable_Object=MibTableColumn
bspePethPsePortPerpetualPoeEnable=_BspePethPsePortPerpetualPoeEnable_Object((1,3,6,1,4,1,45,5,8,1,1,1,14),_BspePethPsePortPerpetualPoeEnable_Type())
bspePethPsePortPerpetualPoeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethPsePortPerpetualPoeEnable.setStatus(_A)
class _BspePethPsePortPowerClassifications_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('class0',1),('class1',2),('class2',3),('class3',4),('class4',5),('class5',6),('class6',7),('class7',8),('class8',9)))
_BspePethPsePortPowerClassifications_Type.__name__=_B
_BspePethPsePortPowerClassifications_Object=MibTableColumn
bspePethPsePortPowerClassifications=_BspePethPsePortPowerClassifications_Object((1,3,6,1,4,1,45,5,8,1,1,1,15),_BspePethPsePortPowerClassifications_Type())
bspePethPsePortPowerClassifications.setMaxAccess(_E)
if mibBuilder.loadTexts:bspePethPsePortPowerClassifications.setStatus(_A)
_BspePethMainPseExtTable_Object=MibTable
bspePethMainPseExtTable=_BspePethMainPseExtTable_Object((1,3,6,1,4,1,45,5,8,1,2))
if mibBuilder.loadTexts:bspePethMainPseExtTable.setStatus(_A)
_BspePethMainPseExtEntry_Object=MibTableRow
bspePethMainPseExtEntry=_BspePethMainPseExtEntry_Object((1,3,6,1,4,1,45,5,8,1,2,1))
bspePethMainPseExtEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:bspePethMainPseExtEntry.setStatus(_A)
class _BspePethMainPseExtGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BspePethMainPseExtGroupIndex_Type.__name__=_B
_BspePethMainPseExtGroupIndex_Object=MibTableColumn
bspePethMainPseExtGroupIndex=_BspePethMainPseExtGroupIndex_Object((1,3,6,1,4,1,45,5,8,1,2,1,1),_BspePethMainPseExtGroupIndex_Type())
bspePethMainPseExtGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:bspePethMainPseExtGroupIndex.setStatus(_A)
class _BspePethMainPseExtPowerPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acOnly',1),('dcOnly',2),('acDc',3)))
_BspePethMainPseExtPowerPresent_Type.__name__=_B
_BspePethMainPseExtPowerPresent_Object=MibTableColumn
bspePethMainPseExtPowerPresent=_BspePethMainPseExtPowerPresent_Object((1,3,6,1,4,1,45,5,8,1,2,1,2),_BspePethMainPseExtPowerPresent_Type())
bspePethMainPseExtPowerPresent.setMaxAccess(_E)
if mibBuilder.loadTexts:bspePethMainPseExtPowerPresent.setStatus(_A)
class _BspePethMainPseExtDisconnectScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('acDisconnect',1),('dcDisconnect',2)))
_BspePethMainPseExtDisconnectScheme_Type.__name__=_B
_BspePethMainPseExtDisconnectScheme_Object=MibTableColumn
bspePethMainPseExtDisconnectScheme=_BspePethMainPseExtDisconnectScheme_Object((1,3,6,1,4,1,45,5,8,1,2,1,3),_BspePethMainPseExtDisconnectScheme_Type())
bspePethMainPseExtDisconnectScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethMainPseExtDisconnectScheme.setStatus(_A)
_BspePethMainPseFastPoeEnable_Type=TruthValue
_BspePethMainPseFastPoeEnable_Object=MibTableColumn
bspePethMainPseFastPoeEnable=_BspePethMainPseFastPoeEnable_Object((1,3,6,1,4,1,45,5,8,1,2,1,4),_BspePethMainPseFastPoeEnable_Type())
bspePethMainPseFastPoeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethMainPseFastPoeEnable.setStatus(_A)
_BspePethMainPsePerpetualPoeEnable_Type=TruthValue
_BspePethMainPsePerpetualPoeEnable_Object=MibTableColumn
bspePethMainPsePerpetualPoeEnable=_BspePethMainPsePerpetualPoeEnable_Object((1,3,6,1,4,1,45,5,8,1,2,1,5),_BspePethMainPsePerpetualPoeEnable_Type())
bspePethMainPsePerpetualPoeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePethMainPsePerpetualPoeEnable.setStatus(_A)
_BspeScalars_ObjectIdentity=ObjectIdentity
bspeScalars=_BspeScalars_ObjectIdentity((1,3,6,1,4,1,45,5,8,1,3))
class _BspeIpPhonePowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,32))
_BspeIpPhonePowerLimit_Type.__name__=_B
_BspeIpPhonePowerLimit_Object=MibScalar
bspeIpPhonePowerLimit=_BspeIpPhonePowerLimit_Object((1,3,6,1,4,1,45,5,8,1,3,1),_BspeIpPhonePowerLimit_Type())
bspeIpPhonePowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:bspeIpPhonePowerLimit.setStatus(_A)
if mibBuilder.loadTexts:bspeIpPhonePowerLimit.setUnits('watts')
class _BspeIpPhonePowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3),('notApplicable',4)))
_BspeIpPhonePowerPriority_Type.__name__=_B
_BspeIpPhonePowerPriority_Object=MibScalar
bspeIpPhonePowerPriority=_BspeIpPhonePowerPriority_Object((1,3,6,1,4,1,45,5,8,1,3,2),_BspeIpPhonePowerPriority_Type())
bspeIpPhonePowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:bspeIpPhonePowerPriority.setStatus(_A)
class _BspePoEPowerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lowPowerBudget',1),('highPowerBudget',2)))
_BspePoEPowerMode_Type.__name__=_B
_BspePoEPowerMode_Object=MibScalar
bspePoEPowerMode=_BspePoEPowerMode_Object((1,3,6,1,4,1,45,5,8,1,3,3),_BspePoEPowerMode_Type())
bspePoEPowerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bspePoEPowerMode.setStatus(_A)
bspePethPsePortCurrentStatusNotification=NotificationType((1,3,6,1,4,1,45,5,8,0,1))
bspePethPsePortCurrentStatusNotification.setObjects((_D,_M))
if mibBuilder.loadTexts:bspePethPsePortCurrentStatusNotification.setStatus(_A)
bspeIpPhonePowerLimitNotification=NotificationType((1,3,6,1,4,1,45,5,8,0,2))
bspeIpPhonePowerLimitNotification.setObjects(*((_G,_H),(_D,_N)))
if mibBuilder.loadTexts:bspeIpPhonePowerLimitNotification.setStatus(_A)
bspeIpPhonePowerPriorityNotification=NotificationType((1,3,6,1,4,1,45,5,8,0,3))
bspeIpPhonePowerPriorityNotification.setObjects(*((_G,_H),(_D,_O)))
if mibBuilder.loadTexts:bspeIpPhonePowerPriorityNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bayStackPethExtMib':bayStackPethExtMib,'bspeNotifications':bspeNotifications,'bspePethPsePortCurrentStatusNotification':bspePethPsePortCurrentStatusNotification,'bspeIpPhonePowerLimitNotification':bspeIpPhonePowerLimitNotification,'bspeIpPhonePowerPriorityNotification':bspeIpPhonePowerPriorityNotification,'bspeObjects':bspeObjects,'bspePethPsePortExtTable':bspePethPsePortExtTable,'bspePethPsePortExtEntry':bspePethPsePortExtEntry,_J:bspePethPsePortExtGroupIndex,_K:bspePethPsePortExtIndex,'bspePethPsePortExtPowerLimit':bspePethPsePortExtPowerLimit,'bspePethPsePortExtDetailedStatus':bspePethPsePortExtDetailedStatus,'bspePethPsePortExtMeasuredVoltage':bspePethPsePortExtMeasuredVoltage,'bspePethPsePortExtMeasuredCurrent':bspePethPsePortExtMeasuredCurrent,'bspePethPsePortExtMeasuredPower':bspePethPsePortExtMeasuredPower,_M:bspePethPsePortExtCurrentStatus,'bspePethPsePortExtCurrentStatusClear':bspePethPsePortExtCurrentStatusClear,'bspePethPsePortExtPowerUpMode':bspePethPsePortExtPowerUpMode,'bspePethPsePortExtPowerPairs':bspePethPsePortExtPowerPairs,'bspePethPsePortExtLldp':bspePethPsePortExtLldp,'bspePethPsePortFastPoeEnable':bspePethPsePortFastPoeEnable,'bspePethPsePortPerpetualPoeEnable':bspePethPsePortPerpetualPoeEnable,'bspePethPsePortPowerClassifications':bspePethPsePortPowerClassifications,'bspePethMainPseExtTable':bspePethMainPseExtTable,'bspePethMainPseExtEntry':bspePethMainPseExtEntry,_L:bspePethMainPseExtGroupIndex,'bspePethMainPseExtPowerPresent':bspePethMainPseExtPowerPresent,'bspePethMainPseExtDisconnectScheme':bspePethMainPseExtDisconnectScheme,'bspePethMainPseFastPoeEnable':bspePethMainPseFastPoeEnable,'bspePethMainPsePerpetualPoeEnable':bspePethMainPsePerpetualPoeEnable,'bspeScalars':bspeScalars,_N:bspeIpPhonePowerLimit,_O:bspeIpPhonePowerPriority,'bspePoEPowerMode':bspePoEPowerMode})