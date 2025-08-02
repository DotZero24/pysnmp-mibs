_I='locked'
_H='not-locked'
_G='operational'
_F='aniBsuWirelessPort'
_E='BSUWIRELESSIF-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bsu,=mibBuilder.importSymbols('ANIROOT-MIB','bsu')
aniBsuWirelessPort,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
aniBsuStatus=ModuleIdentity((1,3,6,1,4,1,4325,3,1))
class _AniBsuStatusBootState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('starting',1),('dhcpc-req-sent',2),('configf-req-sent',3),('wait-for-tod',4),('wait-for-wss',5),(_G,6),('standby',7)))
_AniBsuStatusBootState_Type.__name__=_C
_AniBsuStatusBootState_Object=MibScalar
aniBsuStatusBootState=_AniBsuStatusBootState_Object((1,3,6,1,4,1,4325,3,1,1),_AniBsuStatusBootState_Type())
aniBsuStatusBootState.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusBootState.setStatus(_A)
class _AniBsuStatusSysUpTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_AniBsuStatusSysUpTime_Type.__name__=_D
_AniBsuStatusSysUpTime_Object=MibScalar
aniBsuStatusSysUpTime=_AniBsuStatusSysUpTime_Object((1,3,6,1,4,1,4325,3,1,2),_AniBsuStatusSysUpTime_Type())
aniBsuStatusSysUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusSysUpTime.setStatus(_A)
_AniBsuStatusNumPortsConf_Type=Integer32
_AniBsuStatusNumPortsConf_Object=MibScalar
aniBsuStatusNumPortsConf=_AniBsuStatusNumPortsConf_Object((1,3,6,1,4,1,4325,3,1,3),_AniBsuStatusNumPortsConf_Type())
aniBsuStatusNumPortsConf.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusNumPortsConf.setStatus(_A)
_AniBsuStatusNumPortsPresent_Type=Integer32
_AniBsuStatusNumPortsPresent_Object=MibScalar
aniBsuStatusNumPortsPresent=_AniBsuStatusNumPortsPresent_Object((1,3,6,1,4,1,4325,3,1,4),_AniBsuStatusNumPortsPresent_Type())
aniBsuStatusNumPortsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusNumPortsPresent.setStatus(_A)
class _AniBsuStatusSuCounts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6144))
_AniBsuStatusSuCounts_Type.__name__=_C
_AniBsuStatusSuCounts_Object=MibScalar
aniBsuStatusSuCounts=_AniBsuStatusSuCounts_Object((1,3,6,1,4,1,4325,3,1,5),_AniBsuStatusSuCounts_Type())
aniBsuStatusSuCounts.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusSuCounts.setStatus(_A)
class _AniBsuStatusCellName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AniBsuStatusCellName_Type.__name__=_D
_AniBsuStatusCellName_Object=MibScalar
aniBsuStatusCellName=_AniBsuStatusCellName_Object((1,3,6,1,4,1,4325,3,1,6),_AniBsuStatusCellName_Type())
aniBsuStatusCellName.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusCellName.setStatus(_A)
class _AniBsuStatusCellRadius_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10000,20000,30000,40000,50000,60000,70000,80000,90000,100000)));namedValues=NamedValues(*(('radius10km',10000),('radius20km',20000),('radius30km',30000),('radius40km',40000),('radius50km',50000),('radius60km',60000),('radius70km',70000),('radius80km',80000),('radius90km',90000),('radius100km',100000)))
_AniBsuStatusCellRadius_Type.__name__=_C
_AniBsuStatusCellRadius_Object=MibScalar
aniBsuStatusCellRadius=_AniBsuStatusCellRadius_Object((1,3,6,1,4,1,4325,3,1,7),_AniBsuStatusCellRadius_Type())
aniBsuStatusCellRadius.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusCellRadius.setStatus(_A)
class _AniBsuStatusSyncTimingRef_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internal',1),('external',2),('not-applicable',3)))
_AniBsuStatusSyncTimingRef_Type.__name__=_C
_AniBsuStatusSyncTimingRef_Object=MibScalar
aniBsuStatusSyncTimingRef=_AniBsuStatusSyncTimingRef_Object((1,3,6,1,4,1,4325,3,1,8),_AniBsuStatusSyncTimingRef_Type())
aniBsuStatusSyncTimingRef.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusSyncTimingRef.setStatus(_A)
class _AniBsuStatusRipFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AniBsuStatusRipFlag_Type.__name__=_C
_AniBsuStatusRipFlag_Object=MibScalar
aniBsuStatusRipFlag=_AniBsuStatusRipFlag_Object((1,3,6,1,4,1,4325,3,1,9),_AniBsuStatusRipFlag_Type())
aniBsuStatusRipFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRipFlag.setStatus(_A)
class _AniBsuStatusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('router',1),('bridge',2),('vlan',3)))
_AniBsuStatusMode_Type.__name__=_C
_AniBsuStatusMode_Object=MibScalar
aniBsuStatusMode=_AniBsuStatusMode_Object((1,3,6,1,4,1,4325,3,1,10),_AniBsuStatusMode_Type())
aniBsuStatusMode.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusMode.setStatus(_A)
_AniBsuStatusRadioTable_Object=MibTable
aniBsuStatusRadioTable=_AniBsuStatusRadioTable_Object((1,3,6,1,4,1,4325,3,1,11))
if mibBuilder.loadTexts:aniBsuStatusRadioTable.setStatus(_A)
_AniBsuStatusRadioEntry_Object=MibTableRow
aniBsuStatusRadioEntry=_AniBsuStatusRadioEntry_Object((1,3,6,1,4,1,4325,3,1,11,1))
aniBsuStatusRadioEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuStatusRadioEntry.setStatus(_A)
class _AniBsuStatusRadioSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AniBsuStatusRadioSerialNum_Type.__name__=_D
_AniBsuStatusRadioSerialNum_Object=MibTableColumn
aniBsuStatusRadioSerialNum=_AniBsuStatusRadioSerialNum_Object((1,3,6,1,4,1,4325,3,1,11,1,1),_AniBsuStatusRadioSerialNum_Type())
aniBsuStatusRadioSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioSerialNum.setStatus(_A)
_AniBsuStatusRadioFrequency_Type=DisplayString
_AniBsuStatusRadioFrequency_Object=MibTableColumn
aniBsuStatusRadioFrequency=_AniBsuStatusRadioFrequency_Object((1,3,6,1,4,1,4325,3,1,11,1,2),_AniBsuStatusRadioFrequency_Type())
aniBsuStatusRadioFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioFrequency.setStatus(_A)
if mibBuilder.loadTexts:aniBsuStatusRadioFrequency.setUnits('MHz')
class _AniBsuStatusRadioBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10,11,12)));namedValues=NamedValues(*(('unii-5-3GHz',1),('unii-5-8GHz',2),('general-5-8GHz',3),('mmds-2-6GHz',4),('general-2-6GHz',5),('general-3-5GHz',6),('etsi-3-5GHz-50',7),('etsi-3-5GHz-100',8),('ism-5-8GHz',10),('fdd-3-5GHz',11),('general-5-3GHz',12)))
_AniBsuStatusRadioBand_Type.__name__=_C
_AniBsuStatusRadioBand_Object=MibTableColumn
aniBsuStatusRadioBand=_AniBsuStatusRadioBand_Object((1,3,6,1,4,1,4325,3,1,11,1,3),_AniBsuStatusRadioBand_Type())
aniBsuStatusRadioBand.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioBand.setStatus(_A)
_AniBsuStatusRadioEepromRev_Type=DisplayString
_AniBsuStatusRadioEepromRev_Object=MibTableColumn
aniBsuStatusRadioEepromRev=_AniBsuStatusRadioEepromRev_Object((1,3,6,1,4,1,4325,3,1,11,1,4),_AniBsuStatusRadioEepromRev_Type())
aniBsuStatusRadioEepromRev.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioEepromRev.setStatus(_A)
class _AniBsuStatusRadioVRFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('not-operational',2)))
_AniBsuStatusRadioVRFlag_Type.__name__=_C
_AniBsuStatusRadioVRFlag_Object=MibTableColumn
aniBsuStatusRadioVRFlag=_AniBsuStatusRadioVRFlag_Object((1,3,6,1,4,1,4325,3,1,11,1,5),_AniBsuStatusRadioVRFlag_Type())
aniBsuStatusRadioVRFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioVRFlag.setStatus(_A)
class _AniBsuStatusRadioSynth1Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AniBsuStatusRadioSynth1Lock_Type.__name__=_C
_AniBsuStatusRadioSynth1Lock_Object=MibTableColumn
aniBsuStatusRadioSynth1Lock=_AniBsuStatusRadioSynth1Lock_Object((1,3,6,1,4,1,4325,3,1,11,1,6),_AniBsuStatusRadioSynth1Lock_Type())
aniBsuStatusRadioSynth1Lock.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioSynth1Lock.setStatus(_A)
class _AniBsuStatusRadioSynth2Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AniBsuStatusRadioSynth2Lock_Type.__name__=_C
_AniBsuStatusRadioSynth2Lock_Object=MibTableColumn
aniBsuStatusRadioSynth2Lock=_AniBsuStatusRadioSynth2Lock_Object((1,3,6,1,4,1,4325,3,1,11,1,7),_AniBsuStatusRadioSynth2Lock_Type())
aniBsuStatusRadioSynth2Lock.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioSynth2Lock.setStatus(_A)
_AniBsuStatusRadioTxGain_Type=DisplayString
_AniBsuStatusRadioTxGain_Object=MibTableColumn
aniBsuStatusRadioTxGain=_AniBsuStatusRadioTxGain_Object((1,3,6,1,4,1,4325,3,1,11,1,8),_AniBsuStatusRadioTxGain_Type())
aniBsuStatusRadioTxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioTxGain.setStatus(_A)
if mibBuilder.loadTexts:aniBsuStatusRadioTxGain.setUnits('dB')
class _AniBsuStatusRadioRxGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,45))
_AniBsuStatusRadioRxGain_Type.__name__=_C
_AniBsuStatusRadioRxGain_Object=MibTableColumn
aniBsuStatusRadioRxGain=_AniBsuStatusRadioRxGain_Object((1,3,6,1,4,1,4325,3,1,11,1,9),_AniBsuStatusRadioRxGain_Type())
aniBsuStatusRadioRxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioRxGain.setStatus(_A)
if mibBuilder.loadTexts:aniBsuStatusRadioRxGain.setUnits('dB')
_AniBsuStatusRadioCurrentTxMaxPower_Type=DisplayString
_AniBsuStatusRadioCurrentTxMaxPower_Object=MibTableColumn
aniBsuStatusRadioCurrentTxMaxPower=_AniBsuStatusRadioCurrentTxMaxPower_Object((1,3,6,1,4,1,4325,3,1,11,1,10),_AniBsuStatusRadioCurrentTxMaxPower_Type())
aniBsuStatusRadioCurrentTxMaxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioCurrentTxMaxPower.setStatus(_A)
if mibBuilder.loadTexts:aniBsuStatusRadioCurrentTxMaxPower.setUnits('dBm')
_AniBsuStatusRadioIfCableLoss_Type=DisplayString
_AniBsuStatusRadioIfCableLoss_Object=MibTableColumn
aniBsuStatusRadioIfCableLoss=_AniBsuStatusRadioIfCableLoss_Object((1,3,6,1,4,1,4325,3,1,11,1,11),_AniBsuStatusRadioIfCableLoss_Type())
aniBsuStatusRadioIfCableLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuStatusRadioIfCableLoss.setStatus(_A)
if mibBuilder.loadTexts:aniBsuStatusRadioIfCableLoss.setUnits('dB')
mibBuilder.exportSymbols('BSUSTATUS-MIB',**{'aniBsuStatus':aniBsuStatus,'aniBsuStatusBootState':aniBsuStatusBootState,'aniBsuStatusSysUpTime':aniBsuStatusSysUpTime,'aniBsuStatusNumPortsConf':aniBsuStatusNumPortsConf,'aniBsuStatusNumPortsPresent':aniBsuStatusNumPortsPresent,'aniBsuStatusSuCounts':aniBsuStatusSuCounts,'aniBsuStatusCellName':aniBsuStatusCellName,'aniBsuStatusCellRadius':aniBsuStatusCellRadius,'aniBsuStatusSyncTimingRef':aniBsuStatusSyncTimingRef,'aniBsuStatusRipFlag':aniBsuStatusRipFlag,'aniBsuStatusMode':aniBsuStatusMode,'aniBsuStatusRadioTable':aniBsuStatusRadioTable,'aniBsuStatusRadioEntry':aniBsuStatusRadioEntry,'aniBsuStatusRadioSerialNum':aniBsuStatusRadioSerialNum,'aniBsuStatusRadioFrequency':aniBsuStatusRadioFrequency,'aniBsuStatusRadioBand':aniBsuStatusRadioBand,'aniBsuStatusRadioEepromRev':aniBsuStatusRadioEepromRev,'aniBsuStatusRadioVRFlag':aniBsuStatusRadioVRFlag,'aniBsuStatusRadioSynth1Lock':aniBsuStatusRadioSynth1Lock,'aniBsuStatusRadioSynth2Lock':aniBsuStatusRadioSynth2Lock,'aniBsuStatusRadioTxGain':aniBsuStatusRadioTxGain,'aniBsuStatusRadioRxGain':aniBsuStatusRadioRxGain,'aniBsuStatusRadioCurrentTxMaxPower':aniBsuStatusRadioCurrentTxMaxPower,'aniBsuStatusRadioIfCableLoss':aniBsuStatusRadioIfCableLoss})