_F='netioOutputID'
_E='NETIO-PRODUCTS-NETIO-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
netioProducts=ModuleIdentity((1,3,6,1,4,1,47952))
if mibBuilder.loadTexts:netioProducts.setRevisions(('2017-03-27 00:00',))
_Netio4_ObjectIdentity=ObjectIdentity
netio4=_Netio4_ObjectIdentity((1,3,6,1,4,1,47952,1))
_NetioOutputTable_Object=MibTable
netioOutputTable=_NetioOutputTable_Object((1,3,6,1,4,1,47952,1,1))
if mibBuilder.loadTexts:netioOutputTable.setStatus(_A)
_NetioOutputEntry_Object=MibTableRow
netioOutputEntry=_NetioOutputEntry_Object((1,3,6,1,4,1,47952,1,1,1))
netioOutputEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:netioOutputEntry.setStatus(_A)
class _NetioOutputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NetioOutputID_Type.__name__=_C
_NetioOutputID_Object=MibTableColumn
netioOutputID=_NetioOutputID_Object((1,3,6,1,4,1,47952,1,1,1,1),_NetioOutputID_Type())
netioOutputID.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputID.setStatus(_A)
class _NetioOutputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NetioOutputName_Type.__name__=_D
_NetioOutputName_Object=MibTableColumn
netioOutputName=_NetioOutputName_Object((1,3,6,1,4,1,47952,1,1,1,2),_NetioOutputName_Type())
netioOutputName.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputName.setStatus(_A)
class _NetioOutputState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NetioOutputState_Type.__name__=_C
_NetioOutputState_Object=MibTableColumn
netioOutputState=_NetioOutputState_Object((1,3,6,1,4,1,47952,1,1,1,3),_NetioOutputState_Type())
netioOutputState.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputState.setStatus(_A)
class _NetioOutputStateString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NetioOutputStateString_Type.__name__=_D
_NetioOutputStateString_Object=MibTableColumn
netioOutputStateString=_NetioOutputStateString_Object((1,3,6,1,4,1,47952,1,1,1,4),_NetioOutputStateString_Type())
netioOutputStateString.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputStateString.setStatus(_A)
class _NetioOutputAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('off',0),('on',1),('reset',2),('shortOn',3),('switch',4),('idle',5)))
_NetioOutputAction_Type.__name__=_C
_NetioOutputAction_Object=MibTableColumn
netioOutputAction=_NetioOutputAction_Object((1,3,6,1,4,1,47952,1,1,1,5),_NetioOutputAction_Type())
netioOutputAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:netioOutputAction.setStatus(_A)
class _NetioOutputLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NetioOutputLoad_Type.__name__=_C
_NetioOutputLoad_Object=MibTableColumn
netioOutputLoad=_NetioOutputLoad_Object((1,3,6,1,4,1,47952,1,1,1,25),_NetioOutputLoad_Type())
netioOutputLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputLoad.setStatus(_A)
class _NetioOutputEnergy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0x7fffffffffffffff))
_NetioOutputEnergy_Type.__name__=_C
_NetioOutputEnergy_Object=MibTableColumn
netioOutputEnergy=_NetioOutputEnergy_Object((1,3,6,1,4,1,47952,1,1,1,26),_NetioOutputEnergy_Type())
netioOutputEnergy.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputEnergy.setStatus(_A)
_NetioOutputEnergyStart_Type=DateAndTime
_NetioOutputEnergyStart_Object=MibTableColumn
netioOutputEnergyStart=_NetioOutputEnergyStart_Object((1,3,6,1,4,1,47952,1,1,1,27),_NetioOutputEnergyStart_Type())
netioOutputEnergyStart.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputEnergyStart.setStatus(_A)
class _NetioOutputCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NetioOutputCurrent_Type.__name__=_C
_NetioOutputCurrent_Object=MibTableColumn
netioOutputCurrent=_NetioOutputCurrent_Object((1,3,6,1,4,1,47952,1,1,1,28),_NetioOutputCurrent_Type())
netioOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputCurrent.setStatus(_A)
class _NetioOutputPowerFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_NetioOutputPowerFactor_Type.__name__=_C
_NetioOutputPowerFactor_Object=MibTableColumn
netioOutputPowerFactor=_NetioOutputPowerFactor_Object((1,3,6,1,4,1,47952,1,1,1,29),_NetioOutputPowerFactor_Type())
netioOutputPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOutputPowerFactor.setStatus(_A)
_NetioGlobalMeasure_ObjectIdentity=ObjectIdentity
netioGlobalMeasure=_NetioGlobalMeasure_ObjectIdentity((1,3,6,1,4,1,47952,1,2))
class _NetioVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NetioVoltage_Type.__name__=_C
_NetioVoltage_Object=MibScalar
netioVoltage=_NetioVoltage_Object((1,3,6,1,4,1,47952,1,2,1),_NetioVoltage_Type())
netioVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:netioVoltage.setStatus(_A)
class _NetioFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NetioFrequency_Type.__name__=_C
_NetioFrequency_Object=MibScalar
netioFrequency=_NetioFrequency_Object((1,3,6,1,4,1,47952,1,2,2),_NetioFrequency_Type())
netioFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:netioFrequency.setStatus(_A)
class _NetioTotalCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NetioTotalCurrent_Type.__name__=_C
_NetioTotalCurrent_Object=MibScalar
netioTotalCurrent=_NetioTotalCurrent_Object((1,3,6,1,4,1,47952,1,2,3),_NetioTotalCurrent_Type())
netioTotalCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:netioTotalCurrent.setStatus(_A)
class _NetioOverallPowerFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_NetioOverallPowerFactor_Type.__name__=_C
_NetioOverallPowerFactor_Object=MibScalar
netioOverallPowerFactor=_NetioOverallPowerFactor_Object((1,3,6,1,4,1,47952,1,2,4),_NetioOverallPowerFactor_Type())
netioOverallPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:netioOverallPowerFactor.setStatus(_A)
class _NetioTotalLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NetioTotalLoad_Type.__name__=_C
_NetioTotalLoad_Object=MibScalar
netioTotalLoad=_NetioTotalLoad_Object((1,3,6,1,4,1,47952,1,2,5),_NetioTotalLoad_Type())
netioTotalLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:netioTotalLoad.setStatus(_A)
class _NetioTotalEnergy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NetioTotalEnergy_Type.__name__=_C
_NetioTotalEnergy_Object=MibScalar
netioTotalEnergy=_NetioTotalEnergy_Object((1,3,6,1,4,1,47952,1,2,6),_NetioTotalEnergy_Type())
netioTotalEnergy.setMaxAccess(_B)
if mibBuilder.loadTexts:netioTotalEnergy.setStatus(_A)
_NetioEnergyStart_Type=DateAndTime
_NetioEnergyStart_Object=MibScalar
netioEnergyStart=_NetioEnergyStart_Object((1,3,6,1,4,1,47952,1,2,7),_NetioEnergyStart_Type())
netioEnergyStart.setMaxAccess(_B)
if mibBuilder.loadTexts:netioEnergyStart.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netioProducts':netioProducts,'netio4':netio4,'netioOutputTable':netioOutputTable,'netioOutputEntry':netioOutputEntry,_F:netioOutputID,'netioOutputName':netioOutputName,'netioOutputState':netioOutputState,'netioOutputStateString':netioOutputStateString,'netioOutputAction':netioOutputAction,'netioOutputLoad':netioOutputLoad,'netioOutputEnergy':netioOutputEnergy,'netioOutputEnergyStart':netioOutputEnergyStart,'netioOutputCurrent':netioOutputCurrent,'netioOutputPowerFactor':netioOutputPowerFactor,'netioGlobalMeasure':netioGlobalMeasure,'netioVoltage':netioVoltage,'netioFrequency':netioFrequency,'netioTotalCurrent':netioTotalCurrent,'netioOverallPowerFactor':netioOverallPowerFactor,'netioTotalLoad':netioTotalLoad,'netioTotalEnergy':netioTotalEnergy,'netioEnergyStart':netioEnergyStart})