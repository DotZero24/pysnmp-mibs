_J='disabled'
_I='restart'
_H='edfaOperControlMode'
_G='edfaStatus'
_F='edfaIfIndex'
_E='SL-EDFA-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
slEdfa=ModuleIdentity((1,3,6,1,4,1,4515,1,9))
_EdfaConfig_ObjectIdentity=ObjectIdentity
edfaConfig=_EdfaConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,9,1))
_EdfaConfigTable_Object=MibTable
edfaConfigTable=_EdfaConfigTable_Object((1,3,6,1,4,1,4515,1,9,1,1))
if mibBuilder.loadTexts:edfaConfigTable.setStatus(_A)
_EdfaConfigEntry_Object=MibTableRow
edfaConfigEntry=_EdfaConfigEntry_Object((1,3,6,1,4,1,4515,1,9,1,1,1))
edfaConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:edfaConfigEntry.setStatus(_A)
_EdfaIfIndex_Type=InterfaceIndex
_EdfaIfIndex_Object=MibTableColumn
edfaIfIndex=_EdfaIfIndex_Object((1,3,6,1,4,1,4515,1,9,1,1,1,1),_EdfaIfIndex_Type())
edfaIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaIfIndex.setStatus(_A)
_EdfaPumpTemp_Type=Integer32
_EdfaPumpTemp_Object=MibTableColumn
edfaPumpTemp=_EdfaPumpTemp_Object((1,3,6,1,4,1,4515,1,9,1,1,1,2),_EdfaPumpTemp_Type())
edfaPumpTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaPumpTemp.setStatus(_A)
_EdfaRxPower_Type=Integer32
_EdfaRxPower_Object=MibTableColumn
edfaRxPower=_EdfaRxPower_Object((1,3,6,1,4,1,4515,1,9,1,1,1,3),_EdfaRxPower_Type())
edfaRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaRxPower.setStatus(_A)
class _EdfaPumpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3)))
_EdfaPumpAdminStatus_Type.__name__=_D
_EdfaPumpAdminStatus_Object=MibTableColumn
edfaPumpAdminStatus=_EdfaPumpAdminStatus_Object((1,3,6,1,4,1,4515,1,9,1,1,1,4),_EdfaPumpAdminStatus_Type())
edfaPumpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaPumpAdminStatus.setStatus(_A)
class _EdfaPumpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3),('unknown',4)))
_EdfaPumpOperStatus_Type.__name__=_D
_EdfaPumpOperStatus_Object=MibTableColumn
edfaPumpOperStatus=_EdfaPumpOperStatus_Object((1,3,6,1,4,1,4515,1,9,1,1,1,5),_EdfaPumpOperStatus_Type())
edfaPumpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaPumpOperStatus.setStatus(_A)
class _EdfaStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_EdfaStatus_Type.__name__=_D
_EdfaStatus_Object=MibTableColumn
edfaStatus=_EdfaStatus_Object((1,3,6,1,4,1,4515,1,9,1,1,1,6),_EdfaStatus_Type())
edfaStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaStatus.setStatus(_A)
_EdfaVoa_Type=Integer32
_EdfaVoa_Object=MibTableColumn
edfaVoa=_EdfaVoa_Object((1,3,6,1,4,1,4515,1,9,1,1,1,7),_EdfaVoa_Type())
edfaVoa.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaVoa.setStatus(_A)
_EdfaAutomaticMode_Type=TruthValue
_EdfaAutomaticMode_Object=MibTableColumn
edfaAutomaticMode=_EdfaAutomaticMode_Object((1,3,6,1,4,1,4515,1,9,1,1,1,8),_EdfaAutomaticMode_Type())
edfaAutomaticMode.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaAutomaticMode.setStatus(_A)
class _EdfaAdminControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('apc',1),('agc',2)))
_EdfaAdminControlMode_Type.__name__=_D
_EdfaAdminControlMode_Object=MibTableColumn
edfaAdminControlMode=_EdfaAdminControlMode_Object((1,3,6,1,4,1,4515,1,9,1,1,1,9),_EdfaAdminControlMode_Type())
edfaAdminControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaAdminControlMode.setStatus(_A)
class _EdfaOperControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('apc',1),('agc',2)))
_EdfaOperControlMode_Type.__name__=_D
_EdfaOperControlMode_Object=MibTableColumn
edfaOperControlMode=_EdfaOperControlMode_Object((1,3,6,1,4,1,4515,1,9,1,1,1,10),_EdfaOperControlMode_Type())
edfaOperControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaOperControlMode.setStatus(_A)
_EdfaAdminGain_Type=Integer32
_EdfaAdminGain_Object=MibTableColumn
edfaAdminGain=_EdfaAdminGain_Object((1,3,6,1,4,1,4515,1,9,1,1,1,11),_EdfaAdminGain_Type())
edfaAdminGain.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaAdminGain.setStatus(_A)
_EdfaOperGain_Type=Integer32
_EdfaOperGain_Object=MibTableColumn
edfaOperGain=_EdfaOperGain_Object((1,3,6,1,4,1,4515,1,9,1,1,1,12),_EdfaOperGain_Type())
edfaOperGain.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaOperGain.setStatus(_A)
_EdfaAdminOutputPower_Type=Integer32
_EdfaAdminOutputPower_Object=MibTableColumn
edfaAdminOutputPower=_EdfaAdminOutputPower_Object((1,3,6,1,4,1,4515,1,9,1,1,1,13),_EdfaAdminOutputPower_Type())
edfaAdminOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaAdminOutputPower.setStatus(_A)
_EdfaOperOutputPower_Type=Integer32
_EdfaOperOutputPower_Object=MibTableColumn
edfaOperOutputPower=_EdfaOperOutputPower_Object((1,3,6,1,4,1,4515,1,9,1,1,1,14),_EdfaOperOutputPower_Type())
edfaOperOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaOperOutputPower.setStatus(_A)
_EdfaChannelsNumber_Type=Integer32
_EdfaChannelsNumber_Object=MibTableColumn
edfaChannelsNumber=_EdfaChannelsNumber_Object((1,3,6,1,4,1,4515,1,9,1,1,1,15),_EdfaChannelsNumber_Type())
edfaChannelsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaChannelsNumber.setStatus(_A)
_EdfaTotalChannelsNumber_Type=Integer32
_EdfaTotalChannelsNumber_Object=MibTableColumn
edfaTotalChannelsNumber=_EdfaTotalChannelsNumber_Object((1,3,6,1,4,1,4515,1,9,1,1,1,16),_EdfaTotalChannelsNumber_Type())
edfaTotalChannelsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaTotalChannelsNumber.setStatus(_A)
_EdfaEyeSafetyMode_Type=TruthValue
_EdfaEyeSafetyMode_Object=MibTableColumn
edfaEyeSafetyMode=_EdfaEyeSafetyMode_Object((1,3,6,1,4,1,4515,1,9,1,1,1,17),_EdfaEyeSafetyMode_Type())
edfaEyeSafetyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaEyeSafetyMode.setStatus(_A)
_EdfaShutDownLipEnable_Type=TruthValue
_EdfaShutDownLipEnable_Object=MibTableColumn
edfaShutDownLipEnable=_EdfaShutDownLipEnable_Object((1,3,6,1,4,1,4515,1,9,1,1,1,18),_EdfaShutDownLipEnable_Type())
edfaShutDownLipEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaShutDownLipEnable.setStatus(_A)
_EdfaAutoPowerUpLipEnable_Type=TruthValue
_EdfaAutoPowerUpLipEnable_Object=MibTableColumn
edfaAutoPowerUpLipEnable=_EdfaAutoPowerUpLipEnable_Object((1,3,6,1,4,1,4515,1,9,1,1,1,19),_EdfaAutoPowerUpLipEnable_Type())
edfaAutoPowerUpLipEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaAutoPowerUpLipEnable.setStatus(_A)
_EdfaMaxGain_Type=Integer32
_EdfaMaxGain_Object=MibTableColumn
edfaMaxGain=_EdfaMaxGain_Object((1,3,6,1,4,1,4515,1,9,1,1,1,20),_EdfaMaxGain_Type())
edfaMaxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaMaxGain.setStatus(_A)
_EdfaGainInFrom_Type=Integer32
_EdfaGainInFrom_Object=MibTableColumn
edfaGainInFrom=_EdfaGainInFrom_Object((1,3,6,1,4,1,4515,1,9,1,1,1,21),_EdfaGainInFrom_Type())
edfaGainInFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaGainInFrom.setStatus(_A)
_EdfaGainInTo_Type=Integer32
_EdfaGainInTo_Object=MibTableColumn
edfaGainInTo=_EdfaGainInTo_Object((1,3,6,1,4,1,4515,1,9,1,1,1,22),_EdfaGainInTo_Type())
edfaGainInTo.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaGainInTo.setStatus(_A)
_EdfaGainOutFrom_Type=Integer32
_EdfaGainOutFrom_Object=MibTableColumn
edfaGainOutFrom=_EdfaGainOutFrom_Object((1,3,6,1,4,1,4515,1,9,1,1,1,23),_EdfaGainOutFrom_Type())
edfaGainOutFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaGainOutFrom.setStatus(_A)
_EdfaGainOutTo_Type=Integer32
_EdfaGainOutTo_Object=MibTableColumn
edfaGainOutTo=_EdfaGainOutTo_Object((1,3,6,1,4,1,4515,1,9,1,1,1,24),_EdfaGainOutTo_Type())
edfaGainOutTo.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaGainOutTo.setStatus(_A)
_EdfaPowerInFrom_Type=Integer32
_EdfaPowerInFrom_Object=MibTableColumn
edfaPowerInFrom=_EdfaPowerInFrom_Object((1,3,6,1,4,1,4515,1,9,1,1,1,25),_EdfaPowerInFrom_Type())
edfaPowerInFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaPowerInFrom.setStatus(_A)
_EdfaPowerInTo_Type=Integer32
_EdfaPowerInTo_Object=MibTableColumn
edfaPowerInTo=_EdfaPowerInTo_Object((1,3,6,1,4,1,4515,1,9,1,1,1,26),_EdfaPowerInTo_Type())
edfaPowerInTo.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaPowerInTo.setStatus(_A)
_EdfaPowerOutFrom_Type=Integer32
_EdfaPowerOutFrom_Object=MibTableColumn
edfaPowerOutFrom=_EdfaPowerOutFrom_Object((1,3,6,1,4,1,4515,1,9,1,1,1,27),_EdfaPowerOutFrom_Type())
edfaPowerOutFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaPowerOutFrom.setStatus(_A)
_EdfaPowerOutTo_Type=Integer32
_EdfaPowerOutTo_Object=MibTableColumn
edfaPowerOutTo=_EdfaPowerOutTo_Object((1,3,6,1,4,1,4515,1,9,1,1,1,28),_EdfaPowerOutTo_Type())
edfaPowerOutTo.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaPowerOutTo.setStatus(_A)
_EdfaFromChannel_Type=Integer32
_EdfaFromChannel_Object=MibTableColumn
edfaFromChannel=_EdfaFromChannel_Object((1,3,6,1,4,1,4515,1,9,1,1,1,29),_EdfaFromChannel_Type())
edfaFromChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaFromChannel.setStatus(_A)
_EdfaToChannel_Type=Integer32
_EdfaToChannel_Object=MibTableColumn
edfaToChannel=_EdfaToChannel_Object((1,3,6,1,4,1,4515,1,9,1,1,1,30),_EdfaToChannel_Type())
edfaToChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaToChannel.setStatus(_A)
_EdfaOscChannel_Type=Integer32
_EdfaOscChannel_Object=MibTableColumn
edfaOscChannel=_EdfaOscChannel_Object((1,3,6,1,4,1,4515,1,9,1,1,1,31),_EdfaOscChannel_Type())
edfaOscChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaOscChannel.setStatus(_A)
class _EdfaRedBlueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('red',1),('blue',2),('none',3)))
_EdfaRedBlueType_Type.__name__=_D
_EdfaRedBlueType_Object=MibTableColumn
edfaRedBlueType=_EdfaRedBlueType_Object((1,3,6,1,4,1,4515,1,9,1,1,1,32),_EdfaRedBlueType_Type())
edfaRedBlueType.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaRedBlueType.setStatus(_A)
class _EdfaRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('booster',1),('boosterInline',2),('preamp',3),('inline',4),('raman',5),('other',6)))
_EdfaRole_Type.__name__=_D
_EdfaRole_Object=MibTableColumn
edfaRole=_EdfaRole_Object((1,3,6,1,4,1,4515,1,9,1,1,1,33),_EdfaRole_Type())
edfaRole.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaRole.setStatus(_A)
_EdfaFreeDescription_Type=DisplayString
_EdfaFreeDescription_Object=MibTableColumn
edfaFreeDescription=_EdfaFreeDescription_Object((1,3,6,1,4,1,4515,1,9,1,1,1,34),_EdfaFreeDescription_Type())
edfaFreeDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaFreeDescription.setStatus(_A)
_EdfaConfigSafetyThreshold_Type=Integer32
_EdfaConfigSafetyThreshold_Object=MibTableColumn
edfaConfigSafetyThreshold=_EdfaConfigSafetyThreshold_Object((1,3,6,1,4,1,4515,1,9,1,1,1,35),_EdfaConfigSafetyThreshold_Type())
edfaConfigSafetyThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaConfigSafetyThreshold.setStatus(_A)
_EdfaSigOutputPower_Type=Integer32
_EdfaSigOutputPower_Object=MibTableColumn
edfaSigOutputPower=_EdfaSigOutputPower_Object((1,3,6,1,4,1,4515,1,9,1,1,1,36),_EdfaSigOutputPower_Type())
edfaSigOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:edfaSigOutputPower.setStatus(_A)
class _EdfaLossPropagation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('enabled',2)))
_EdfaLossPropagation_Type.__name__=_D
_EdfaLossPropagation_Object=MibTableColumn
edfaLossPropagation=_EdfaLossPropagation_Object((1,3,6,1,4,1,4515,1,9,1,1,1,37),_EdfaLossPropagation_Type())
edfaLossPropagation.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaLossPropagation.setStatus(_A)
class _EdfaConfigAmpMngPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('mng1',1),('mng2',2)))
_EdfaConfigAmpMngPort_Type.__name__=_D
_EdfaConfigAmpMngPort_Object=MibScalar
edfaConfigAmpMngPort=_EdfaConfigAmpMngPort_Object((1,3,6,1,4,1,4515,1,9,1,2),_EdfaConfigAmpMngPort_Type())
edfaConfigAmpMngPort.setMaxAccess(_C)
if mibBuilder.loadTexts:edfaConfigAmpMngPort.setStatus(_A)
_EdfaTraps_ObjectIdentity=ObjectIdentity
edfaTraps=_EdfaTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,9,2))
_EdfaTraps0_ObjectIdentity=ObjectIdentity
edfaTraps0=_EdfaTraps0_ObjectIdentity((1,3,6,1,4,1,4515,1,9,2,0))
edfaStatusChange0=NotificationType((1,3,6,1,4,1,4515,1,9,2,0,1))
edfaStatusChange0.setObjects(*((_E,_F),(_E,_G)))
if mibBuilder.loadTexts:edfaStatusChange0.setStatus(_A)
edfaControlModeChange0=NotificationType((1,3,6,1,4,1,4515,1,9,2,0,2))
edfaControlModeChange0.setObjects(*((_E,_F),(_E,_H)))
if mibBuilder.loadTexts:edfaControlModeChange0.setStatus(_A)
edfaStatusChange=NotificationType((1,3,6,1,4,1,4515,1,9,2,1))
edfaStatusChange.setObjects(*((_E,_F),(_E,_G)))
if mibBuilder.loadTexts:edfaStatusChange.setStatus(_A)
edfaControlModeChange=NotificationType((1,3,6,1,4,1,4515,1,9,2,2))
edfaControlModeChange.setObjects(*((_E,_F),(_E,_H)))
if mibBuilder.loadTexts:edfaControlModeChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'slEdfa':slEdfa,'edfaConfig':edfaConfig,'edfaConfigTable':edfaConfigTable,'edfaConfigEntry':edfaConfigEntry,_F:edfaIfIndex,'edfaPumpTemp':edfaPumpTemp,'edfaRxPower':edfaRxPower,'edfaPumpAdminStatus':edfaPumpAdminStatus,'edfaPumpOperStatus':edfaPumpOperStatus,_G:edfaStatus,'edfaVoa':edfaVoa,'edfaAutomaticMode':edfaAutomaticMode,'edfaAdminControlMode':edfaAdminControlMode,_H:edfaOperControlMode,'edfaAdminGain':edfaAdminGain,'edfaOperGain':edfaOperGain,'edfaAdminOutputPower':edfaAdminOutputPower,'edfaOperOutputPower':edfaOperOutputPower,'edfaChannelsNumber':edfaChannelsNumber,'edfaTotalChannelsNumber':edfaTotalChannelsNumber,'edfaEyeSafetyMode':edfaEyeSafetyMode,'edfaShutDownLipEnable':edfaShutDownLipEnable,'edfaAutoPowerUpLipEnable':edfaAutoPowerUpLipEnable,'edfaMaxGain':edfaMaxGain,'edfaGainInFrom':edfaGainInFrom,'edfaGainInTo':edfaGainInTo,'edfaGainOutFrom':edfaGainOutFrom,'edfaGainOutTo':edfaGainOutTo,'edfaPowerInFrom':edfaPowerInFrom,'edfaPowerInTo':edfaPowerInTo,'edfaPowerOutFrom':edfaPowerOutFrom,'edfaPowerOutTo':edfaPowerOutTo,'edfaFromChannel':edfaFromChannel,'edfaToChannel':edfaToChannel,'edfaOscChannel':edfaOscChannel,'edfaRedBlueType':edfaRedBlueType,'edfaRole':edfaRole,'edfaFreeDescription':edfaFreeDescription,'edfaConfigSafetyThreshold':edfaConfigSafetyThreshold,'edfaSigOutputPower':edfaSigOutputPower,'edfaLossPropagation':edfaLossPropagation,'edfaConfigAmpMngPort':edfaConfigAmpMngPort,'edfaTraps':edfaTraps,'edfaTraps0':edfaTraps0,'edfaStatusChange0':edfaStatusChange0,'edfaControlModeChange0':edfaControlModeChange0,'edfaStatusChange':edfaStatusChange,'edfaControlModeChange':edfaControlModeChange})