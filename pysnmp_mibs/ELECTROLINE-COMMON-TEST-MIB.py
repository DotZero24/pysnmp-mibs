_F='ELECTROLINE-COMMON-TEST-MIB'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonPrivate,=mibBuilder.importSymbols('ELECTROLINE-COMMON-ROOT-MIB','commonPrivate')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
class TenthCelsius(TextualConvention,Integer32):status=_A;displayHint='d-1'
class _SwMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,30)));namedValues=NamedValues(*(('normal',0),('testOnly',1),('cmOnly',2),('scanFeatureInDiagnosticMode',30)))
_SwMode_Type.__name__=_D
_SwMode_Object=MibScalar
swMode=_SwMode_Object((1,3,6,1,4,1,5802,1,3,1,4,4,1),_SwMode_Type())
swMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swMode.setStatus(_A)
_ProdTest_ObjectIdentity=ObjectIdentity
prodTest=_ProdTest_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4,2))
if mibBuilder.loadTexts:prodTest.setStatus(_A)
_ProdInventory_ObjectIdentity=ObjectIdentity
prodInventory=_ProdInventory_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4,2,1))
if mibBuilder.loadTexts:prodInventory.setStatus(_A)
_ProdInvHwType_Type=Integer32
_ProdInvHwType_Object=MibScalar
prodInvHwType=_ProdInvHwType_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,1,1),_ProdInvHwType_Type())
prodInvHwType.setMaxAccess(_B)
if mibBuilder.loadTexts:prodInvHwType.setStatus(_A)
_ProdInvHwMinorRev_Type=Integer32
_ProdInvHwMinorRev_Object=MibScalar
prodInvHwMinorRev=_ProdInvHwMinorRev_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,1,2),_ProdInvHwMinorRev_Type())
prodInvHwMinorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:prodInvHwMinorRev.setStatus(_A)
_ProdInvHwMajorRev_Type=Integer32
_ProdInvHwMajorRev_Object=MibScalar
prodInvHwMajorRev=_ProdInvHwMajorRev_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,1,3),_ProdInvHwMajorRev_Type())
prodInvHwMajorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:prodInvHwMajorRev.setStatus(_A)
_ProdInvHwDrvRev_Type=Integer32
_ProdInvHwDrvRev_Object=MibScalar
prodInvHwDrvRev=_ProdInvHwDrvRev_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,1,4),_ProdInvHwDrvRev_Type())
prodInvHwDrvRev.setMaxAccess(_B)
if mibBuilder.loadTexts:prodInvHwDrvRev.setStatus(_A)
class _ProdModelNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProdModelNumber_Type.__name__=_E
_ProdModelNumber_Object=MibScalar
prodModelNumber=_ProdModelNumber_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,1,5),_ProdModelNumber_Type())
prodModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prodModelNumber.setStatus(_A)
_ProdManufacturingInfo_ObjectIdentity=ObjectIdentity
prodManufacturingInfo=_ProdManufacturingInfo_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4,2,1,10))
if mibBuilder.loadTexts:prodManufacturingInfo.setStatus(_A)
_ProdMfcDateTime_Type=DateAndTime
_ProdMfcDateTime_Object=MibScalar
prodMfcDateTime=_ProdMfcDateTime_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,1,10,1),_ProdMfcDateTime_Type())
prodMfcDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:prodMfcDateTime.setStatus(_A)
_ProdMfcTestSwVersion_Type=OctetString
_ProdMfcTestSwVersion_Object=MibScalar
prodMfcTestSwVersion=_ProdMfcTestSwVersion_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,1,10,2),_ProdMfcTestSwVersion_Type())
prodMfcTestSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:prodMfcTestSwVersion.setStatus(_A)
_ProdConfiguration_ObjectIdentity=ObjectIdentity
prodConfiguration=_ProdConfiguration_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4,2,2))
if mibBuilder.loadTexts:prodConfiguration.setStatus(_A)
class _ProdFormatFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('format',1))
_ProdFormatFlash_Type.__name__=_D
_ProdFormatFlash_Object=MibScalar
prodFormatFlash=_ProdFormatFlash_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,2,1),_ProdFormatFlash_Type())
prodFormatFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:prodFormatFlash.setStatus(_A)
class _ProdDocsisMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('docsis',1),('euroDocsis',2)))
_ProdDocsisMode_Type.__name__=_D
_ProdDocsisMode_Object=MibScalar
prodDocsisMode=_ProdDocsisMode_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,2,2),_ProdDocsisMode_Type())
prodDocsisMode.setMaxAccess(_B)
if mibBuilder.loadTexts:prodDocsisMode.setStatus(_A)
_LedsControl_ObjectIdentity=ObjectIdentity
ledsControl=_LedsControl_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4,2,3))
if mibBuilder.loadTexts:ledsControl.setStatus(_A)
_LedsControlTable_Object=MibTable
ledsControlTable=_LedsControlTable_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,3,1))
if mibBuilder.loadTexts:ledsControlTable.setStatus(_A)
_LedsControlEntry_Object=MibTableRow
ledsControlEntry=_LedsControlEntry_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,3,1,1))
ledsControlEntry.setIndexNames((0,_F,'ledId'))
if mibBuilder.loadTexts:ledsControlEntry.setStatus(_A)
_LedId_Type=Integer32
_LedId_Object=MibTableColumn
ledId=_LedId_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,3,1,1,1),_LedId_Type())
ledId.setMaxAccess(_C)
if mibBuilder.loadTexts:ledId.setStatus(_A)
class _LedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_LedState_Type.__name__=_D
_LedState_Object=MibTableColumn
ledState=_LedState_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,3,1,1,2),_LedState_Type())
ledState.setMaxAccess(_B)
if mibBuilder.loadTexts:ledState.setStatus(_A)
_LedDesc_Type=OctetString
_LedDesc_Object=MibTableColumn
ledDesc=_LedDesc_Object((1,3,6,1,4,1,5802,1,3,1,4,4,2,3,1,1,3),_LedDesc_Type())
ledDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:ledDesc.setStatus(_A)
_ElineSpectrumAnalyzer_ObjectIdentity=ObjectIdentity
elineSpectrumAnalyzer=_ElineSpectrumAnalyzer_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4,3))
if mibBuilder.loadTexts:elineSpectrumAnalyzer.setStatus(_A)
_PlantPower_ObjectIdentity=ObjectIdentity
plantPower=_PlantPower_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4,3,1))
if mibBuilder.loadTexts:plantPower.setStatus(_A)
_PlantPowerStartFrequency_Type=Integer32
_PlantPowerStartFrequency_Object=MibScalar
plantPowerStartFrequency=_PlantPowerStartFrequency_Object((1,3,6,1,4,1,5802,1,3,1,4,4,3,1,1),_PlantPowerStartFrequency_Type())
plantPowerStartFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:plantPowerStartFrequency.setStatus(_A)
_PlantPowerStopFrequency_Type=Integer32
_PlantPowerStopFrequency_Object=MibScalar
plantPowerStopFrequency=_PlantPowerStopFrequency_Object((1,3,6,1,4,1,5802,1,3,1,4,4,3,1,2),_PlantPowerStopFrequency_Type())
plantPowerStopFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:plantPowerStopFrequency.setStatus(_A)
_PlantPowerNbAverage_Type=Integer32
_PlantPowerNbAverage_Object=MibScalar
plantPowerNbAverage=_PlantPowerNbAverage_Object((1,3,6,1,4,1,5802,1,3,1,4,4,3,1,3),_PlantPowerNbAverage_Type())
plantPowerNbAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:plantPowerNbAverage.setStatus(_A)
_PlantPowerPower_Type=Integer32
_PlantPowerPower_Object=MibScalar
plantPowerPower=_PlantPowerPower_Object((1,3,6,1,4,1,5802,1,3,1,4,4,3,1,4),_PlantPowerPower_Type())
plantPowerPower.setMaxAccess(_C)
if mibBuilder.loadTexts:plantPowerPower.setStatus(_A)
_PlanPowerRBW_Type=Integer32
_PlanPowerRBW_Object=MibScalar
planPowerRBW=_PlanPowerRBW_Object((1,3,6,1,4,1,5802,1,3,1,4,4,3,1,5),_PlanPowerRBW_Type())
planPowerRBW.setMaxAccess(_C)
if mibBuilder.loadTexts:planPowerRBW.setStatus(_A)
_PlantPowerNbBins_Type=Integer32
_PlantPowerNbBins_Object=MibScalar
plantPowerNbBins=_PlantPowerNbBins_Object((1,3,6,1,4,1,5802,1,3,1,4,4,3,1,6),_PlantPowerNbBins_Type())
plantPowerNbBins.setMaxAccess(_C)
if mibBuilder.loadTexts:plantPowerNbBins.setStatus(_A)
_PrivateStatus_ObjectIdentity=ObjectIdentity
privateStatus=_PrivateStatus_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,4,4))
if mibBuilder.loadTexts:privateStatus.setStatus(_A)
_DieTemperature_Type=TenthCelsius
_DieTemperature_Object=MibScalar
dieTemperature=_DieTemperature_Object((1,3,6,1,4,1,5802,1,3,1,4,4,4,1),_DieTemperature_Type())
dieTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dieTemperature.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'TenthCelsius':TenthCelsius,'swMode':swMode,'prodTest':prodTest,'prodInventory':prodInventory,'prodInvHwType':prodInvHwType,'prodInvHwMinorRev':prodInvHwMinorRev,'prodInvHwMajorRev':prodInvHwMajorRev,'prodInvHwDrvRev':prodInvHwDrvRev,'prodModelNumber':prodModelNumber,'prodManufacturingInfo':prodManufacturingInfo,'prodMfcDateTime':prodMfcDateTime,'prodMfcTestSwVersion':prodMfcTestSwVersion,'prodConfiguration':prodConfiguration,'prodFormatFlash':prodFormatFlash,'prodDocsisMode':prodDocsisMode,'ledsControl':ledsControl,'ledsControlTable':ledsControlTable,'ledsControlEntry':ledsControlEntry,'ledId':ledId,'ledState':ledState,'ledDesc':ledDesc,'elineSpectrumAnalyzer':elineSpectrumAnalyzer,'plantPower':plantPower,'plantPowerStartFrequency':plantPowerStartFrequency,'plantPowerStopFrequency':plantPowerStopFrequency,'plantPowerNbAverage':plantPowerNbAverage,'plantPowerPower':plantPowerPower,'planPowerRBW':planPowerRBW,'plantPowerNbBins':plantPowerNbBins,'privateStatus':privateStatus,'dieTemperature':dieTemperature})