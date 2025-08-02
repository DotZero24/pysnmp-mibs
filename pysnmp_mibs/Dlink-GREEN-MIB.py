_J='rlGreenEthPortSavingTypeValue'
_I='Dlink-GREEN-MIB'
_H='TruthValue'
_G='Unsigned32'
_F='PortList'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
ifIndex,=mibBuilder.importSymbols(_D,_E)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
rlGreenEth=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,134))
if mibBuilder.loadTexts:rlGreenEth.setRevisions(('2008-08-15 00:00',))
class RlGreenSavingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('energyDetect',1),('shortReach',2)))
class NonOperReasonType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('np',1),('lt',2),('lu',3),('ls',4),('ll',5),('er',6),('ld',7),('unknown',8)))
_RlGreenEthEnergyDetectEnable_Type=TruthValue
_RlGreenEthEnergyDetectEnable_Object=MibScalar
rlGreenEthEnergyDetectEnable=_RlGreenEthEnergyDetectEnable_Object((1,3,6,1,4,1,171,10,94,89,89,134,1),_RlGreenEthEnergyDetectEnable_Type())
rlGreenEthEnergyDetectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGreenEthEnergyDetectEnable.setStatus(_A)
_RlGreenEthShortReachEnable_Type=TruthValue
_RlGreenEthShortReachEnable_Object=MibScalar
rlGreenEthShortReachEnable=_RlGreenEthShortReachEnable_Object((1,3,6,1,4,1,171,10,94,89,89,134,2),_RlGreenEthShortReachEnable_Type())
rlGreenEthShortReachEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGreenEthShortReachEnable.setStatus(_A)
_RlGreenEthCurrentEnergyConsumption_Type=Unsigned32
_RlGreenEthCurrentEnergyConsumption_Object=MibScalar
rlGreenEthCurrentEnergyConsumption=_RlGreenEthCurrentEnergyConsumption_Object((1,3,6,1,4,1,171,10,94,89,89,134,3),_RlGreenEthCurrentEnergyConsumption_Type())
rlGreenEthCurrentEnergyConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:rlGreenEthCurrentEnergyConsumption.setStatus(_A)
if mibBuilder.loadTexts:rlGreenEthCurrentEnergyConsumption.setUnits('mWatt')
_RlGreenEthCurrentMaxEnergyConsumption_Type=Unsigned32
_RlGreenEthCurrentMaxEnergyConsumption_Object=MibScalar
rlGreenEthCurrentMaxEnergyConsumption=_RlGreenEthCurrentMaxEnergyConsumption_Object((1,3,6,1,4,1,171,10,94,89,89,134,4),_RlGreenEthCurrentMaxEnergyConsumption_Type())
rlGreenEthCurrentMaxEnergyConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:rlGreenEthCurrentMaxEnergyConsumption.setStatus(_A)
if mibBuilder.loadTexts:rlGreenEthCurrentMaxEnergyConsumption.setUnits('mWatt')
_RlGreenEthCumulativePowerSaveMeter_Type=Unsigned32
_RlGreenEthCumulativePowerSaveMeter_Object=MibScalar
rlGreenEthCumulativePowerSaveMeter=_RlGreenEthCumulativePowerSaveMeter_Object((1,3,6,1,4,1,171,10,94,89,89,134,5),_RlGreenEthCumulativePowerSaveMeter_Type())
rlGreenEthCumulativePowerSaveMeter.setMaxAccess(_C)
if mibBuilder.loadTexts:rlGreenEthCumulativePowerSaveMeter.setStatus(_A)
if mibBuilder.loadTexts:rlGreenEthCumulativePowerSaveMeter.setUnits('Watt*Hour')
class _RlGreenEthShortReachThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,70))
_RlGreenEthShortReachThreshold_Type.__name__=_G
_RlGreenEthShortReachThreshold_Object=MibScalar
rlGreenEthShortReachThreshold=_RlGreenEthShortReachThreshold_Object((1,3,6,1,4,1,171,10,94,89,89,134,6),_RlGreenEthShortReachThreshold_Type())
rlGreenEthShortReachThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGreenEthShortReachThreshold.setStatus(_A)
if mibBuilder.loadTexts:rlGreenEthShortReachThreshold.setUnits('meter')
class _RlGreenEthCumulativePowerSaveMeterReset_Type(TruthValue):defaultValue=2
_RlGreenEthCumulativePowerSaveMeterReset_Type.__name__=_H
_RlGreenEthCumulativePowerSaveMeterReset_Object=MibScalar
rlGreenEthCumulativePowerSaveMeterReset=_RlGreenEthCumulativePowerSaveMeterReset_Object((1,3,6,1,4,1,171,10,94,89,89,134,7),_RlGreenEthCumulativePowerSaveMeterReset_Type())
rlGreenEthCumulativePowerSaveMeterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGreenEthCumulativePowerSaveMeterReset.setStatus(_A)
_RlGreenEthPortTable_Object=MibTable
rlGreenEthPortTable=_RlGreenEthPortTable_Object((1,3,6,1,4,1,171,10,94,89,89,134,8))
if mibBuilder.loadTexts:rlGreenEthPortTable.setStatus(_A)
_RlGreenEthPortEntry_Object=MibTableRow
rlGreenEthPortEntry=_RlGreenEthPortEntry_Object((1,3,6,1,4,1,171,10,94,89,89,134,8,1))
rlGreenEthPortEntry.setIndexNames((0,_D,_E),(0,_I,_J))
if mibBuilder.loadTexts:rlGreenEthPortEntry.setStatus(_A)
_RlGreenEthPortSavingTypeValue_Type=RlGreenSavingType
_RlGreenEthPortSavingTypeValue_Object=MibTableColumn
rlGreenEthPortSavingTypeValue=_RlGreenEthPortSavingTypeValue_Object((1,3,6,1,4,1,171,10,94,89,89,134,8,1,1),_RlGreenEthPortSavingTypeValue_Type())
rlGreenEthPortSavingTypeValue.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlGreenEthPortSavingTypeValue.setStatus(_A)
_RlGreenEthPortAdminState_Type=TruthValue
_RlGreenEthPortAdminState_Object=MibTableColumn
rlGreenEthPortAdminState=_RlGreenEthPortAdminState_Object((1,3,6,1,4,1,171,10,94,89,89,134,8,1,2),_RlGreenEthPortAdminState_Type())
rlGreenEthPortAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGreenEthPortAdminState.setStatus(_A)
_RlGreenEthPortOperState_Type=TruthValue
_RlGreenEthPortOperState_Object=MibTableColumn
rlGreenEthPortOperState=_RlGreenEthPortOperState_Object((1,3,6,1,4,1,171,10,94,89,89,134,8,1,3),_RlGreenEthPortOperState_Type())
rlGreenEthPortOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlGreenEthPortOperState.setStatus(_A)
_RlGreenEthPortNonOperReason_Type=NonOperReasonType
_RlGreenEthPortNonOperReason_Object=MibTableColumn
rlGreenEthPortNonOperReason=_RlGreenEthPortNonOperReason_Object((1,3,6,1,4,1,171,10,94,89,89,134,8,1,4),_RlGreenEthPortNonOperReason_Type())
rlGreenEthPortNonOperReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rlGreenEthPortNonOperReason.setStatus(_A)
class _RlGreenEthForceShortReachIfIndexList_Type(PortList):defaultHexValue=''
_RlGreenEthForceShortReachIfIndexList_Type.__name__=_F
_RlGreenEthForceShortReachIfIndexList_Object=MibScalar
rlGreenEthForceShortReachIfIndexList=_RlGreenEthForceShortReachIfIndexList_Object((1,3,6,1,4,1,171,10,94,89,89,134,9),_RlGreenEthForceShortReachIfIndexList_Type())
rlGreenEthForceShortReachIfIndexList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGreenEthForceShortReachIfIndexList.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'RlGreenSavingType':RlGreenSavingType,'NonOperReasonType':NonOperReasonType,'rlGreenEth':rlGreenEth,'rlGreenEthEnergyDetectEnable':rlGreenEthEnergyDetectEnable,'rlGreenEthShortReachEnable':rlGreenEthShortReachEnable,'rlGreenEthCurrentEnergyConsumption':rlGreenEthCurrentEnergyConsumption,'rlGreenEthCurrentMaxEnergyConsumption':rlGreenEthCurrentMaxEnergyConsumption,'rlGreenEthCumulativePowerSaveMeter':rlGreenEthCumulativePowerSaveMeter,'rlGreenEthShortReachThreshold':rlGreenEthShortReachThreshold,'rlGreenEthCumulativePowerSaveMeterReset':rlGreenEthCumulativePowerSaveMeterReset,'rlGreenEthPortTable':rlGreenEthPortTable,'rlGreenEthPortEntry':rlGreenEthPortEntry,_J:rlGreenEthPortSavingTypeValue,'rlGreenEthPortAdminState':rlGreenEthPortAdminState,'rlGreenEthPortOperState':rlGreenEthPortOperState,'rlGreenEthPortNonOperReason':rlGreenEthPortNonOperReason,'rlGreenEthForceShortReachIfIndexList':rlGreenEthForceShortReachIfIndexList})