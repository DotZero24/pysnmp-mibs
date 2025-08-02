_I='rbAteTestType'
_H='RB-ATE-MIB'
_G='startTest'
_F='DisplayString'
_E='read-only'
_D='none'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
rainbowAteMib=ModuleIdentity((1,3,6,1,4,1,12394,1,2,301))
if mibBuilder.loadTexts:rainbowAteMib.setRevisions(('2006-05-05 15:00',))
_Alvarion_ObjectIdentity=ObjectIdentity
alvarion=_Alvarion_ObjectIdentity((1,3,6,1,4,1,12394))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,12394,1))
_Rainbow_ObjectIdentity=ObjectIdentity
rainbow=_Rainbow_ObjectIdentity((1,3,6,1,4,1,12394,1,2))
_RbAteConfig_ObjectIdentity=ObjectIdentity
rbAteConfig=_RbAteConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,2,301,1))
class _RbAteStartTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('startFullTest',2),('startHostTest',3),('startC5Test',4)))
_RbAteStartTest_Type.__name__=_C
_RbAteStartTest_Object=MibScalar
rbAteStartTest=_RbAteStartTest_Object((1,3,6,1,4,1,12394,1,2,301,1,1),_RbAteStartTest_Type())
rbAteStartTest.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteStartTest.setStatus(_A)
class _RbAteExitTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('exitTest',2)))
_RbAteExitTest_Type.__name__=_C
_RbAteExitTest_Object=MibScalar
rbAteExitTest=_RbAteExitTest_Object((1,3,6,1,4,1,12394,1,2,301,1,2),_RbAteExitTest_Type())
rbAteExitTest.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteExitTest.setStatus(_A)
_RbAteTimeToRunC5Test_Type=Integer32
_RbAteTimeToRunC5Test_Object=MibScalar
rbAteTimeToRunC5Test=_RbAteTimeToRunC5Test_Object((1,3,6,1,4,1,12394,1,2,301,1,3),_RbAteTimeToRunC5Test_Type())
rbAteTimeToRunC5Test.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteTimeToRunC5Test.setStatus(_A)
class _RbAteTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readyForTest',1),('testInProgress',2)))
_RbAteTestStatus_Type.__name__=_C
_RbAteTestStatus_Object=MibScalar
rbAteTestStatus=_RbAteTestStatus_Object((1,3,6,1,4,1,12394,1,2,301,1,4),_RbAteTestStatus_Type())
rbAteTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteTestStatus.setStatus(_A)
class _RbAteState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inWorkingMode',1),('inAteTestMode',2)))
_RbAteState_Type.__name__=_C
_RbAteState_Object=MibScalar
rbAteState=_RbAteState_Object((1,3,6,1,4,1,12394,1,2,301,1,5),_RbAteState_Type())
rbAteState.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteState.setStatus(_A)
class _RbAteTimeOfLastC5Test_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RbAteTimeOfLastC5Test_Type.__name__=_F
_RbAteTimeOfLastC5Test_Object=MibScalar
rbAteTimeOfLastC5Test=_RbAteTimeOfLastC5Test_Object((1,3,6,1,4,1,12394,1,2,301,1,6),_RbAteTimeOfLastC5Test_Type())
rbAteTimeOfLastC5Test.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteTimeOfLastC5Test.setStatus(_A)
class _RbAteSnmpRelaySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('relayOn',1),('relayOff',2)))
_RbAteSnmpRelaySupport_Type.__name__=_C
_RbAteSnmpRelaySupport_Object=MibScalar
rbAteSnmpRelaySupport=_RbAteSnmpRelaySupport_Object((1,3,6,1,4,1,12394,1,2,301,1,7),_RbAteSnmpRelaySupport_Type())
rbAteSnmpRelaySupport.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteSnmpRelaySupport.setStatus(_A)
_RbAteClockConfig_ObjectIdentity=ObjectIdentity
rbAteClockConfig=_RbAteClockConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,2,301,2))
_RbAteDateDay_Type=Integer32
_RbAteDateDay_Object=MibScalar
rbAteDateDay=_RbAteDateDay_Object((1,3,6,1,4,1,12394,1,2,301,2,1),_RbAteDateDay_Type())
rbAteDateDay.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteDateDay.setStatus(_A)
class _RbAteDateDayOfWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('sunday',7)))
_RbAteDateDayOfWeek_Type.__name__=_C
_RbAteDateDayOfWeek_Object=MibScalar
rbAteDateDayOfWeek=_RbAteDateDayOfWeek_Object((1,3,6,1,4,1,12394,1,2,301,2,2),_RbAteDateDayOfWeek_Type())
rbAteDateDayOfWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteDateDayOfWeek.setStatus(_A)
_RbAteDateMonth_Type=Integer32
_RbAteDateMonth_Object=MibScalar
rbAteDateMonth=_RbAteDateMonth_Object((1,3,6,1,4,1,12394,1,2,301,2,3),_RbAteDateMonth_Type())
rbAteDateMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteDateMonth.setStatus(_A)
_RbAteDateYear_Type=Integer32
_RbAteDateYear_Object=MibScalar
rbAteDateYear=_RbAteDateYear_Object((1,3,6,1,4,1,12394,1,2,301,2,4),_RbAteDateYear_Type())
rbAteDateYear.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteDateYear.setStatus(_A)
_RbAteDateHour_Type=Integer32
_RbAteDateHour_Object=MibScalar
rbAteDateHour=_RbAteDateHour_Object((1,3,6,1,4,1,12394,1,2,301,2,5),_RbAteDateHour_Type())
rbAteDateHour.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteDateHour.setStatus(_A)
_RbAteDateMin_Type=Integer32
_RbAteDateMin_Object=MibScalar
rbAteDateMin=_RbAteDateMin_Object((1,3,6,1,4,1,12394,1,2,301,2,6),_RbAteDateMin_Type())
rbAteDateMin.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteDateMin.setStatus(_A)
_RbAteDateSec_Type=Integer32
_RbAteDateSec_Object=MibScalar
rbAteDateSec=_RbAteDateSec_Object((1,3,6,1,4,1,12394,1,2,301,2,7),_RbAteDateSec_Type())
rbAteDateSec.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteDateSec.setStatus(_A)
_RbAteTestResults_ObjectIdentity=ObjectIdentity
rbAteTestResults=_RbAteTestResults_ObjectIdentity((1,3,6,1,4,1,12394,1,2,301,3))
_RbAteTestResultsTable_Object=MibTable
rbAteTestResultsTable=_RbAteTestResultsTable_Object((1,3,6,1,4,1,12394,1,2,301,3,1))
if mibBuilder.loadTexts:rbAteTestResultsTable.setStatus(_A)
_RbAteTestResultsEntry_Object=MibTableRow
rbAteTestResultsEntry=_RbAteTestResultsEntry_Object((1,3,6,1,4,1,12394,1,2,301,3,1,1))
rbAteTestResultsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:rbAteTestResultsEntry.setStatus(_A)
class _RbAteTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('flashMemoryTest',1),('sdRAMMemoryTest',2),('watchDogTest',3),('diskOnChipMemoryTest',4),('tempSensorTest',5),('i2CBusIntTest',6),('rs232MonitorTest',7),('alarmsInOutTest',8),('acmInOutTest',9),('gpsTest',10),('bstSyncTest',11),('mhzAnd1pps',12),('bitDcpTest',13),('bitDcpPhyTest',14),('bitDcpTluHashTest',15),('bitExt1PPSTest',16),('gpsRS422Test',17)))
_RbAteTestType_Type.__name__=_C
_RbAteTestType_Object=MibTableColumn
rbAteTestType=_RbAteTestType_Object((1,3,6,1,4,1,12394,1,2,301,3,1,1,1),_RbAteTestType_Type())
rbAteTestType.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteTestType.setStatus(_A)
class _RbAteTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('success',0),('failed',1)))
_RbAteTestResult_Type.__name__=_C
_RbAteTestResult_Object=MibTableColumn
rbAteTestResult=_RbAteTestResult_Object((1,3,6,1,4,1,12394,1,2,301,3,1,1,2),_RbAteTestResult_Type())
rbAteTestResult.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteTestResult.setStatus(_A)
_RbAteTestResultVal_Type=Integer32
_RbAteTestResultVal_Object=MibTableColumn
rbAteTestResultVal=_RbAteTestResultVal_Object((1,3,6,1,4,1,12394,1,2,301,3,1,1,3),_RbAteTestResultVal_Type())
rbAteTestResultVal.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteTestResultVal.setStatus(_A)
class _RbAteTestResultDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RbAteTestResultDescription_Type.__name__=_F
_RbAteTestResultDescription_Object=MibTableColumn
rbAteTestResultDescription=_RbAteTestResultDescription_Object((1,3,6,1,4,1,12394,1,2,301,3,1,1,4),_RbAteTestResultDescription_Type())
rbAteTestResultDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:rbAteTestResultDescription.setStatus(_A)
_RbAteBurnFuncs_ObjectIdentity=ObjectIdentity
rbAteBurnFuncs=_RbAteBurnFuncs_ObjectIdentity((1,3,6,1,4,1,12394,1,2,301,4))
class _RbAteEnterSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RbAteEnterSerialNum_Type.__name__=_F
_RbAteEnterSerialNum_Object=MibScalar
rbAteEnterSerialNum=_RbAteEnterSerialNum_Object((1,3,6,1,4,1,12394,1,2,301,4,1),_RbAteEnterSerialNum_Type())
rbAteEnterSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteEnterSerialNum.setStatus(_A)
class _RbAteEnterMacAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_RbAteEnterMacAddress_Type.__name__=_F
_RbAteEnterMacAddress_Object=MibScalar
rbAteEnterMacAddress=_RbAteEnterMacAddress_Object((1,3,6,1,4,1,12394,1,2,301,4,2),_RbAteEnterMacAddress_Type())
rbAteEnterMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteEnterMacAddress.setStatus(_A)
_RbAteCleanUpParams_ObjectIdentity=ObjectIdentity
rbAteCleanUpParams=_RbAteCleanUpParams_ObjectIdentity((1,3,6,1,4,1,12394,1,2,301,5))
class _RbAteDeleteNpuShadowFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('delete',2)))
_RbAteDeleteNpuShadowFile_Type.__name__=_C
_RbAteDeleteNpuShadowFile_Object=MibScalar
rbAteDeleteNpuShadowFile=_RbAteDeleteNpuShadowFile_Object((1,3,6,1,4,1,12394,1,2,301,5,1),_RbAteDeleteNpuShadowFile_Type())
rbAteDeleteNpuShadowFile.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteDeleteNpuShadowFile.setStatus(_A)
class _RbAteSetServiceDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('setDefault',2)))
_RbAteSetServiceDefault_Type.__name__=_C
_RbAteSetServiceDefault_Object=MibScalar
rbAteSetServiceDefault=_RbAteSetServiceDefault_Object((1,3,6,1,4,1,12394,1,2,301,5,2),_RbAteSetServiceDefault_Type())
rbAteSetServiceDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteSetServiceDefault.setStatus(_A)
class _RbAtePowerOnCntReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('reset',2)))
_RbAtePowerOnCntReset_Type.__name__=_C
_RbAtePowerOnCntReset_Object=MibScalar
rbAtePowerOnCntReset=_RbAtePowerOnCntReset_Object((1,3,6,1,4,1,12394,1,2,301,5,3),_RbAtePowerOnCntReset_Type())
rbAtePowerOnCntReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAtePowerOnCntReset.setStatus(_A)
_RbAteManualTests_ObjectIdentity=ObjectIdentity
rbAteManualTests=_RbAteManualTests_ObjectIdentity((1,3,6,1,4,1,12394,1,2,301,6))
class _RbAteStartDcpTluHashTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_G,2)))
_RbAteStartDcpTluHashTest_Type.__name__=_C
_RbAteStartDcpTluHashTest_Object=MibScalar
rbAteStartDcpTluHashTest=_RbAteStartDcpTluHashTest_Object((1,3,6,1,4,1,12394,1,2,301,6,1),_RbAteStartDcpTluHashTest_Type())
rbAteStartDcpTluHashTest.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteStartDcpTluHashTest.setStatus(_A)
class _RbAteStartGpsExt1PPSTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_G,2)))
_RbAteStartGpsExt1PPSTest_Type.__name__=_C
_RbAteStartGpsExt1PPSTest_Object=MibScalar
rbAteStartGpsExt1PPSTest=_RbAteStartGpsExt1PPSTest_Object((1,3,6,1,4,1,12394,1,2,301,6,2),_RbAteStartGpsExt1PPSTest_Type())
rbAteStartGpsExt1PPSTest.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteStartGpsExt1PPSTest.setStatus(_A)
class _RbAteStartGpsRS422Test_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_G,2)))
_RbAteStartGpsRS422Test_Type.__name__=_C
_RbAteStartGpsRS422Test_Object=MibScalar
rbAteStartGpsRS422Test=_RbAteStartGpsRS422Test_Object((1,3,6,1,4,1,12394,1,2,301,6,3),_RbAteStartGpsRS422Test_Type())
rbAteStartGpsRS422Test.setMaxAccess(_B)
if mibBuilder.loadTexts:rbAteStartGpsRS422Test.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'alvarion':alvarion,'products':products,'rainbow':rainbow,'rainbowAteMib':rainbowAteMib,'rbAteConfig':rbAteConfig,'rbAteStartTest':rbAteStartTest,'rbAteExitTest':rbAteExitTest,'rbAteTimeToRunC5Test':rbAteTimeToRunC5Test,'rbAteTestStatus':rbAteTestStatus,'rbAteState':rbAteState,'rbAteTimeOfLastC5Test':rbAteTimeOfLastC5Test,'rbAteSnmpRelaySupport':rbAteSnmpRelaySupport,'rbAteClockConfig':rbAteClockConfig,'rbAteDateDay':rbAteDateDay,'rbAteDateDayOfWeek':rbAteDateDayOfWeek,'rbAteDateMonth':rbAteDateMonth,'rbAteDateYear':rbAteDateYear,'rbAteDateHour':rbAteDateHour,'rbAteDateMin':rbAteDateMin,'rbAteDateSec':rbAteDateSec,'rbAteTestResults':rbAteTestResults,'rbAteTestResultsTable':rbAteTestResultsTable,'rbAteTestResultsEntry':rbAteTestResultsEntry,_I:rbAteTestType,'rbAteTestResult':rbAteTestResult,'rbAteTestResultVal':rbAteTestResultVal,'rbAteTestResultDescription':rbAteTestResultDescription,'rbAteBurnFuncs':rbAteBurnFuncs,'rbAteEnterSerialNum':rbAteEnterSerialNum,'rbAteEnterMacAddress':rbAteEnterMacAddress,'rbAteCleanUpParams':rbAteCleanUpParams,'rbAteDeleteNpuShadowFile':rbAteDeleteNpuShadowFile,'rbAteSetServiceDefault':rbAteSetServiceDefault,'rbAtePowerOnCntReset':rbAtePowerOnCntReset,'rbAteManualTests':rbAteManualTests,'rbAteStartDcpTluHashTest':rbAteStartDcpTluHashTest,'rbAteStartGpsExt1PPSTest':rbAteStartGpsExt1PPSTest,'rbAteStartGpsRS422Test':rbAteStartGpsRS422Test})