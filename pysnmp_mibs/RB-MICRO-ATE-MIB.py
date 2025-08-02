_I='rbAteMicroTestType'
_H='RB-MICRO-ATE-MIB'
_G='doNothing'
_F='none'
_E='read-only'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
rainbowMicroBSTAteMib=ModuleIdentity((1,3,6,1,4,1,12394,1,2,302))
if mibBuilder.loadTexts:rainbowMicroBSTAteMib.setRevisions(('2006-03-03 15:00',))
_Alvarion_ObjectIdentity=ObjectIdentity
alvarion=_Alvarion_ObjectIdentity((1,3,6,1,4,1,12394))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,12394,1))
_Rainbow_ObjectIdentity=ObjectIdentity
rainbow=_Rainbow_ObjectIdentity((1,3,6,1,4,1,12394,1,2))
_RbAteMicroConfig_ObjectIdentity=ObjectIdentity
rbAteMicroConfig=_RbAteMicroConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,2,302,1))
class _RbAteMicroStartTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('startFullTest',2),('startHostTest',3),('startPhysicalTest',4),('startMonitorTest',5),('startWatchDogTest',6)))
_RbAteMicroStartTest_Type.__name__=_C
_RbAteMicroStartTest_Object=MibScalar
rbAteMicroStartTest=_RbAteMicroStartTest_Object((1,3,6,1,4,1,12394,1,2,302,1,1),_RbAteMicroStartTest_Type())
rbAteMicroStartTest.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroStartTest.setStatus(_A)
_RbAteMicroTimeToRunPhysicalTest_Type=Integer32
_RbAteMicroTimeToRunPhysicalTest_Object=MibScalar
rbAteMicroTimeToRunPhysicalTest=_RbAteMicroTimeToRunPhysicalTest_Object((1,3,6,1,4,1,12394,1,2,302,1,2),_RbAteMicroTimeToRunPhysicalTest_Type())
rbAteMicroTimeToRunPhysicalTest.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroTimeToRunPhysicalTest.setStatus(_A)
_RbAteMicroNumOfPacketsToRunPhysTest_Type=Integer32
_RbAteMicroNumOfPacketsToRunPhysTest_Object=MibScalar
rbAteMicroNumOfPacketsToRunPhysTest=_RbAteMicroNumOfPacketsToRunPhysTest_Object((1,3,6,1,4,1,12394,1,2,302,1,3),_RbAteMicroNumOfPacketsToRunPhysTest_Type())
rbAteMicroNumOfPacketsToRunPhysTest.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroNumOfPacketsToRunPhysTest.setStatus(_A)
class _RbAteMicroTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readyForTest',1),('testInProgress',2)))
_RbAteMicroTestStatus_Type.__name__=_C
_RbAteMicroTestStatus_Object=MibScalar
rbAteMicroTestStatus=_RbAteMicroTestStatus_Object((1,3,6,1,4,1,12394,1,2,302,1,4),_RbAteMicroTestStatus_Type())
rbAteMicroTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteMicroTestStatus.setStatus(_A)
class _RbAteSnmpRelaySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('relayOn',1),('relayOff',2)))
_RbAteSnmpRelaySupport_Type.__name__=_C
_RbAteSnmpRelaySupport_Object=MibScalar
rbAteSnmpRelaySupport=_RbAteSnmpRelaySupport_Object((1,3,6,1,4,1,12394,1,2,302,1,5),_RbAteSnmpRelaySupport_Type())
rbAteSnmpRelaySupport.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteSnmpRelaySupport.setStatus(_A)
_RbAteMicroClockConfig_ObjectIdentity=ObjectIdentity
rbAteMicroClockConfig=_RbAteMicroClockConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,2,302,2))
_RbAteMicroDateDay_Type=Integer32
_RbAteMicroDateDay_Object=MibScalar
rbAteMicroDateDay=_RbAteMicroDateDay_Object((1,3,6,1,4,1,12394,1,2,302,2,1),_RbAteMicroDateDay_Type())
rbAteMicroDateDay.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroDateDay.setStatus(_A)
class _RbAteMicroDateDayOfWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('sunday',7)))
_RbAteMicroDateDayOfWeek_Type.__name__=_C
_RbAteMicroDateDayOfWeek_Object=MibScalar
rbAteMicroDateDayOfWeek=_RbAteMicroDateDayOfWeek_Object((1,3,6,1,4,1,12394,1,2,302,2,2),_RbAteMicroDateDayOfWeek_Type())
rbAteMicroDateDayOfWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroDateDayOfWeek.setStatus(_A)
_RbAteMicroDateMonth_Type=Integer32
_RbAteMicroDateMonth_Object=MibScalar
rbAteMicroDateMonth=_RbAteMicroDateMonth_Object((1,3,6,1,4,1,12394,1,2,302,2,3),_RbAteMicroDateMonth_Type())
rbAteMicroDateMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroDateMonth.setStatus(_A)
_RbAteMicroDateYear_Type=Integer32
_RbAteMicroDateYear_Object=MibScalar
rbAteMicroDateYear=_RbAteMicroDateYear_Object((1,3,6,1,4,1,12394,1,2,302,2,4),_RbAteMicroDateYear_Type())
rbAteMicroDateYear.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroDateYear.setStatus(_A)
_RbAteMicroDateHour_Type=Integer32
_RbAteMicroDateHour_Object=MibScalar
rbAteMicroDateHour=_RbAteMicroDateHour_Object((1,3,6,1,4,1,12394,1,2,302,2,5),_RbAteMicroDateHour_Type())
rbAteMicroDateHour.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroDateHour.setStatus(_A)
_RbAteMicroDateMin_Type=Integer32
_RbAteMicroDateMin_Object=MibScalar
rbAteMicroDateMin=_RbAteMicroDateMin_Object((1,3,6,1,4,1,12394,1,2,302,2,6),_RbAteMicroDateMin_Type())
rbAteMicroDateMin.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroDateMin.setStatus(_A)
_RbAteMicroDateSec_Type=Integer32
_RbAteMicroDateSec_Object=MibScalar
rbAteMicroDateSec=_RbAteMicroDateSec_Object((1,3,6,1,4,1,12394,1,2,302,2,7),_RbAteMicroDateSec_Type())
rbAteMicroDateSec.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroDateSec.setStatus(_A)
_RbAteMicroTestResults_ObjectIdentity=ObjectIdentity
rbAteMicroTestResults=_RbAteMicroTestResults_ObjectIdentity((1,3,6,1,4,1,12394,1,2,302,3))
_RbAteMicroTestResultsConfig_ObjectIdentity=ObjectIdentity
rbAteMicroTestResultsConfig=_RbAteMicroTestResultsConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,2,302,3,1))
class _RbAteMicroSaveTestResultsToFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('saveResults',2)))
_RbAteMicroSaveTestResultsToFlash_Type.__name__=_C
_RbAteMicroSaveTestResultsToFlash_Object=MibScalar
rbAteMicroSaveTestResultsToFlash=_RbAteMicroSaveTestResultsToFlash_Object((1,3,6,1,4,1,12394,1,2,302,3,1,1),_RbAteMicroSaveTestResultsToFlash_Type())
rbAteMicroSaveTestResultsToFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroSaveTestResultsToFlash.setStatus(_A)
class _RbAteMicroRecallTestResultsFromFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('recallResults',2)))
_RbAteMicroRecallTestResultsFromFlash_Type.__name__=_C
_RbAteMicroRecallTestResultsFromFlash_Object=MibScalar
rbAteMicroRecallTestResultsFromFlash=_RbAteMicroRecallTestResultsFromFlash_Object((1,3,6,1,4,1,12394,1,2,302,3,1,2),_RbAteMicroRecallTestResultsFromFlash_Type())
rbAteMicroRecallTestResultsFromFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroRecallTestResultsFromFlash.setStatus(_A)
_RbAteMicroTestResultsTab_ObjectIdentity=ObjectIdentity
rbAteMicroTestResultsTab=_RbAteMicroTestResultsTab_ObjectIdentity((1,3,6,1,4,1,12394,1,2,302,3,2))
_RbAteMicroTestResultsTable_Object=MibTable
rbAteMicroTestResultsTable=_RbAteMicroTestResultsTable_Object((1,3,6,1,4,1,12394,1,2,302,3,2,1))
if mibBuilder.loadTexts:rbAteMicroTestResultsTable.setStatus(_A)
_RbAteMicroTestResultsEntry_Object=MibTableRow
rbAteMicroTestResultsEntry=_RbAteMicroTestResultsEntry_Object((1,3,6,1,4,1,12394,1,2,302,3,2,1,1))
rbAteMicroTestResultsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:rbAteMicroTestResultsEntry.setStatus(_A)
class _RbAteMicroTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('flashMemoryTest',1),('sdRAMMemoryTest',2),('watchDogTest',3),('diskOnChipMemoryTest',4),('tempSensorTest',5),('i2CBusIntTest',6),('rs232MonitorTest',7),('alarmsInOutTest',8),('acmInOutTest',9),('mngEthernetPortTest',10),('dataEthernetPortTest',11),('backPlaneEthernetPortTest',12),('gpsTest',13),('bstSyncTest',14),('test16mhzAnd1pps',15)))
_RbAteMicroTestType_Type.__name__=_C
_RbAteMicroTestType_Object=MibTableColumn
rbAteMicroTestType=_RbAteMicroTestType_Object((1,3,6,1,4,1,12394,1,2,302,3,2,1,1,1),_RbAteMicroTestType_Type())
rbAteMicroTestType.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteMicroTestType.setStatus(_A)
class _RbAteMicroTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('success',0),('failed',1),('inactive',2),('notChecked',3)))
_RbAteMicroTestResult_Type.__name__=_C
_RbAteMicroTestResult_Object=MibTableColumn
rbAteMicroTestResult=_RbAteMicroTestResult_Object((1,3,6,1,4,1,12394,1,2,302,3,2,1,1,2),_RbAteMicroTestResult_Type())
rbAteMicroTestResult.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteMicroTestResult.setStatus(_A)
_RbAteMicroTestResultVal_Type=Integer32
_RbAteMicroTestResultVal_Object=MibTableColumn
rbAteMicroTestResultVal=_RbAteMicroTestResultVal_Object((1,3,6,1,4,1,12394,1,2,302,3,2,1,1,3),_RbAteMicroTestResultVal_Type())
rbAteMicroTestResultVal.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteMicroTestResultVal.setStatus(_A)
class _RbAteMicroTestResultDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RbAteMicroTestResultDescription_Type.__name__=_D
_RbAteMicroTestResultDescription_Object=MibTableColumn
rbAteMicroTestResultDescription=_RbAteMicroTestResultDescription_Object((1,3,6,1,4,1,12394,1,2,302,3,2,1,1,4),_RbAteMicroTestResultDescription_Type())
rbAteMicroTestResultDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteMicroTestResultDescription.setStatus(_A)
_RbAteMicroBurnFuncs_ObjectIdentity=ObjectIdentity
rbAteMicroBurnFuncs=_RbAteMicroBurnFuncs_ObjectIdentity((1,3,6,1,4,1,12394,1,2,302,4))
class _RbAteMicroEnterSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RbAteMicroEnterSerialNum_Type.__name__=_D
_RbAteMicroEnterSerialNum_Object=MibScalar
rbAteMicroEnterSerialNum=_RbAteMicroEnterSerialNum_Object((1,3,6,1,4,1,12394,1,2,302,4,1),_RbAteMicroEnterSerialNum_Type())
rbAteMicroEnterSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroEnterSerialNum.setStatus(_A)
class _RbAteMicroEnterDataMacAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_RbAteMicroEnterDataMacAddr_Type.__name__=_D
_RbAteMicroEnterDataMacAddr_Object=MibScalar
rbAteMicroEnterDataMacAddr=_RbAteMicroEnterDataMacAddr_Object((1,3,6,1,4,1,12394,1,2,302,4,2),_RbAteMicroEnterDataMacAddr_Type())
rbAteMicroEnterDataMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroEnterDataMacAddr.setStatus(_A)
class _RbAteMicroEnterMngmntMacAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_RbAteMicroEnterMngmntMacAddr_Type.__name__=_D
_RbAteMicroEnterMngmntMacAddr_Object=MibScalar
rbAteMicroEnterMngmntMacAddr=_RbAteMicroEnterMngmntMacAddr_Object((1,3,6,1,4,1,12394,1,2,302,4,3),_RbAteMicroEnterMngmntMacAddr_Type())
rbAteMicroEnterMngmntMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroEnterMngmntMacAddr.setStatus(_A)
class _RbAteMicroGetIduHwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RbAteMicroGetIduHwRevision_Type.__name__=_D
_RbAteMicroGetIduHwRevision_Object=MibScalar
rbAteMicroGetIduHwRevision=_RbAteMicroGetIduHwRevision_Object((1,3,6,1,4,1,12394,1,2,302,4,4),_RbAteMicroGetIduHwRevision_Type())
rbAteMicroGetIduHwRevision.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteMicroGetIduHwRevision.setStatus(_A)
_RbAteMicroCleanUpParams_ObjectIdentity=ObjectIdentity
rbAteMicroCleanUpParams=_RbAteMicroCleanUpParams_ObjectIdentity((1,3,6,1,4,1,12394,1,2,302,5))
class _RbAteMicroDeleteNpuShadowFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('delete',2)))
_RbAteMicroDeleteNpuShadowFile_Type.__name__=_C
_RbAteMicroDeleteNpuShadowFile_Object=MibScalar
rbAteMicroDeleteNpuShadowFile=_RbAteMicroDeleteNpuShadowFile_Object((1,3,6,1,4,1,12394,1,2,302,5,1),_RbAteMicroDeleteNpuShadowFile_Type())
rbAteMicroDeleteNpuShadowFile.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroDeleteNpuShadowFile.setStatus(_A)
class _RbAteMicroSetServiceDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('setDefault',2)))
_RbAteMicroSetServiceDefault_Type.__name__=_C
_RbAteMicroSetServiceDefault_Object=MibScalar
rbAteMicroSetServiceDefault=_RbAteMicroSetServiceDefault_Object((1,3,6,1,4,1,12394,1,2,302,5,2),_RbAteMicroSetServiceDefault_Type())
rbAteMicroSetServiceDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroSetServiceDefault.setStatus(_A)
class _RbAteMicroPowerOnCntReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('reset',2)))
_RbAteMicroPowerOnCntReset_Type.__name__=_C
_RbAteMicroPowerOnCntReset_Object=MibScalar
rbAteMicroPowerOnCntReset=_RbAteMicroPowerOnCntReset_Object((1,3,6,1,4,1,12394,1,2,302,5,3),_RbAteMicroPowerOnCntReset_Type())
rbAteMicroPowerOnCntReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteMicroPowerOnCntReset.setStatus(_A)
_RbAteManualTests_ObjectIdentity=ObjectIdentity
rbAteManualTests=_RbAteManualTests_ObjectIdentity((1,3,6,1,4,1,12394,1,2,302,6))
class _RbAteLedTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('startTest',2),('stopTest',3)))
_RbAteLedTest_Type.__name__=_C
_RbAteLedTest_Object=MibScalar
rbAteLedTest=_RbAteLedTest_Object((1,3,6,1,4,1,12394,1,2,302,6,1),_RbAteLedTest_Type())
rbAteLedTest.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteLedTest.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'alvarion':alvarion,'products':products,'rainbow':rainbow,'rainbowMicroBSTAteMib':rainbowMicroBSTAteMib,'rbAteMicroConfig':rbAteMicroConfig,'rbAteMicroStartTest':rbAteMicroStartTest,'rbAteMicroTimeToRunPhysicalTest':rbAteMicroTimeToRunPhysicalTest,'rbAteMicroNumOfPacketsToRunPhysTest':rbAteMicroNumOfPacketsToRunPhysTest,'rbAteMicroTestStatus':rbAteMicroTestStatus,'rbAteSnmpRelaySupport':rbAteSnmpRelaySupport,'rbAteMicroClockConfig':rbAteMicroClockConfig,'rbAteMicroDateDay':rbAteMicroDateDay,'rbAteMicroDateDayOfWeek':rbAteMicroDateDayOfWeek,'rbAteMicroDateMonth':rbAteMicroDateMonth,'rbAteMicroDateYear':rbAteMicroDateYear,'rbAteMicroDateHour':rbAteMicroDateHour,'rbAteMicroDateMin':rbAteMicroDateMin,'rbAteMicroDateSec':rbAteMicroDateSec,'rbAteMicroTestResults':rbAteMicroTestResults,'rbAteMicroTestResultsConfig':rbAteMicroTestResultsConfig,'rbAteMicroSaveTestResultsToFlash':rbAteMicroSaveTestResultsToFlash,'rbAteMicroRecallTestResultsFromFlash':rbAteMicroRecallTestResultsFromFlash,'rbAteMicroTestResultsTab':rbAteMicroTestResultsTab,'rbAteMicroTestResultsTable':rbAteMicroTestResultsTable,'rbAteMicroTestResultsEntry':rbAteMicroTestResultsEntry,_I:rbAteMicroTestType,'rbAteMicroTestResult':rbAteMicroTestResult,'rbAteMicroTestResultVal':rbAteMicroTestResultVal,'rbAteMicroTestResultDescription':rbAteMicroTestResultDescription,'rbAteMicroBurnFuncs':rbAteMicroBurnFuncs,'rbAteMicroEnterSerialNum':rbAteMicroEnterSerialNum,'rbAteMicroEnterDataMacAddr':rbAteMicroEnterDataMacAddr,'rbAteMicroEnterMngmntMacAddr':rbAteMicroEnterMngmntMacAddr,'rbAteMicroGetIduHwRevision':rbAteMicroGetIduHwRevision,'rbAteMicroCleanUpParams':rbAteMicroCleanUpParams,'rbAteMicroDeleteNpuShadowFile':rbAteMicroDeleteNpuShadowFile,'rbAteMicroSetServiceDefault':rbAteMicroSetServiceDefault,'rbAteMicroPowerOnCntReset':rbAteMicroPowerOnCntReset,'rbAteManualTests':rbAteManualTests,'rbAteLedTest':rbAteLedTest})