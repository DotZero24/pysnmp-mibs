_L='dvmFpgaIoTestResultIndex'
_K='unknown'
_J='dvmFpgaSoftwareTableIndex'
_I='ELECTROLINE-DVM-TEST-MIB'
_H='other'
_G='failure'
_F='inProgress'
_E='success'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dvmPrivate,=mibBuilder.importSymbols('ELECTROLINE-DVM-ROOT-MIB','dvmPrivate')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
class _DvmSwMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,30)));namedValues=NamedValues(*(('normal',0),('testOnly',1),('cmOnly',2),('ScanFeatureInDiagnosticMode',30)))
_DvmSwMode_Type.__name__=_C
_DvmSwMode_Object=MibScalar
dvmSwMode=_DvmSwMode_Object((1,3,6,1,4,1,5802,1,3,1,3,4,1),_DvmSwMode_Type())
dvmSwMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmSwMode.setStatus(_A)
_DvmTest_ObjectIdentity=ObjectIdentity
dvmTest=_DvmTest_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,4,2))
_DvmTestFpga_ObjectIdentity=ObjectIdentity
dvmTestFpga=_DvmTestFpga_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,4,2,1))
_DvmTestFpgaSoftwareControl_ObjectIdentity=ObjectIdentity
dvmTestFpgaSoftwareControl=_DvmTestFpgaSoftwareControl_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1))
_DvmTestFpgaSwImageNumber_Type=Integer32
_DvmTestFpgaSwImageNumber_Object=MibScalar
dvmTestFpgaSwImageNumber=_DvmTestFpgaSwImageNumber_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,1),_DvmTestFpgaSwImageNumber_Type())
dvmTestFpgaSwImageNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmTestFpgaSwImageNumber.setStatus(_A)
_DvmTestFpgaSwDloadTftpServer_Type=IpAddress
_DvmTestFpgaSwDloadTftpServer_Object=MibScalar
dvmTestFpgaSwDloadTftpServer=_DvmTestFpgaSwDloadTftpServer_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,2),_DvmTestFpgaSwDloadTftpServer_Type())
dvmTestFpgaSwDloadTftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmTestFpgaSwDloadTftpServer.setStatus(_A)
_DvmTestFpgaSwDloadTftpPath_Type=SnmpAdminString
_DvmTestFpgaSwDloadTftpPath_Object=MibScalar
dvmTestFpgaSwDloadTftpPath=_DvmTestFpgaSwDloadTftpPath_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,3),_DvmTestFpgaSwDloadTftpPath_Type())
dvmTestFpgaSwDloadTftpPath.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmTestFpgaSwDloadTftpPath.setStatus(_A)
_DvmTestFpgaSwDloadNow_Type=TruthValue
_DvmTestFpgaSwDloadNow_Object=MibScalar
dvmTestFpgaSwDloadNow=_DvmTestFpgaSwDloadNow_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,4),_DvmTestFpgaSwDloadNow_Type())
dvmTestFpgaSwDloadNow.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmTestFpgaSwDloadNow.setStatus(_A)
class _DvmTestFpgaSwDloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_E,1),(_F,2),(_H,3)))
_DvmTestFpgaSwDloadStatus_Type.__name__=_C
_DvmTestFpgaSwDloadStatus_Object=MibScalar
dvmTestFpgaSwDloadStatus=_DvmTestFpgaSwDloadStatus_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,5),_DvmTestFpgaSwDloadStatus_Type())
dvmTestFpgaSwDloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmTestFpgaSwDloadStatus.setStatus(_A)
_DvmTestFpgaSwCopyImageFrom_Type=Integer32
_DvmTestFpgaSwCopyImageFrom_Object=MibScalar
dvmTestFpgaSwCopyImageFrom=_DvmTestFpgaSwCopyImageFrom_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,6),_DvmTestFpgaSwCopyImageFrom_Type())
dvmTestFpgaSwCopyImageFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmTestFpgaSwCopyImageFrom.setStatus(_A)
class _DvmTestFpgaSwCopyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_E,1),(_F,2),(_H,3)))
_DvmTestFpgaSwCopyStatus_Type.__name__=_C
_DvmTestFpgaSwCopyStatus_Object=MibScalar
dvmTestFpgaSwCopyStatus=_DvmTestFpgaSwCopyStatus_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,7),_DvmTestFpgaSwCopyStatus_Type())
dvmTestFpgaSwCopyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmTestFpgaSwCopyStatus.setStatus(_A)
_DvmTestFpgaSwSendImageFrom_Type=Integer32
_DvmTestFpgaSwSendImageFrom_Object=MibScalar
dvmTestFpgaSwSendImageFrom=_DvmTestFpgaSwSendImageFrom_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,8),_DvmTestFpgaSwSendImageFrom_Type())
dvmTestFpgaSwSendImageFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmTestFpgaSwSendImageFrom.setStatus(_A)
class _DvmTestFpgaSwSendImageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_E,1),(_F,2),(_H,3)))
_DvmTestFpgaSwSendImageStatus_Type.__name__=_C
_DvmTestFpgaSwSendImageStatus_Object=MibScalar
dvmTestFpgaSwSendImageStatus=_DvmTestFpgaSwSendImageStatus_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,1,9),_DvmTestFpgaSwSendImageStatus_Type())
dvmTestFpgaSwSendImageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmTestFpgaSwSendImageStatus.setStatus(_A)
_DvmTestFpgaSotwareTable_Object=MibTable
dvmTestFpgaSotwareTable=_DvmTestFpgaSotwareTable_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2))
if mibBuilder.loadTexts:dvmTestFpgaSotwareTable.setStatus(_A)
_DvmTestFpgaSotwareEntry_Object=MibTableRow
dvmTestFpgaSotwareEntry=_DvmTestFpgaSotwareEntry_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1))
dvmTestFpgaSotwareEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:dvmTestFpgaSotwareEntry.setStatus(_A)
class _DvmFpgaSoftwareTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DvmFpgaSoftwareTableIndex_Type.__name__=_C
_DvmFpgaSoftwareTableIndex_Object=MibTableColumn
dvmFpgaSoftwareTableIndex=_DvmFpgaSoftwareTableIndex_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,1),_DvmFpgaSoftwareTableIndex_Type())
dvmFpgaSoftwareTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaSoftwareTableIndex.setStatus(_A)
_DvmFpgaProcessorId_Type=Unsigned32
_DvmFpgaProcessorId_Object=MibTableColumn
dvmFpgaProcessorId=_DvmFpgaProcessorId_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,2),_DvmFpgaProcessorId_Type())
dvmFpgaProcessorId.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaProcessorId.setStatus(_A)
_DvmFpgaSoftwareMajorRevision_Type=Unsigned32
_DvmFpgaSoftwareMajorRevision_Object=MibTableColumn
dvmFpgaSoftwareMajorRevision=_DvmFpgaSoftwareMajorRevision_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,3),_DvmFpgaSoftwareMajorRevision_Type())
dvmFpgaSoftwareMajorRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaSoftwareMajorRevision.setStatus(_A)
_DvmFpgaSoftwareMinorRevision_Type=Unsigned32
_DvmFpgaSoftwareMinorRevision_Object=MibTableColumn
dvmFpgaSoftwareMinorRevision=_DvmFpgaSoftwareMinorRevision_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,4),_DvmFpgaSoftwareMinorRevision_Type())
dvmFpgaSoftwareMinorRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaSoftwareMinorRevision.setStatus(_A)
_DvmFpgaBuildTime_Type=DateAndTime
_DvmFpgaBuildTime_Object=MibTableColumn
dvmFpgaBuildTime=_DvmFpgaBuildTime_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,5),_DvmFpgaBuildTime_Type())
dvmFpgaBuildTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaBuildTime.setStatus(_A)
_DvmFpgaFileLength_Type=Unsigned32
_DvmFpgaFileLength_Object=MibTableColumn
dvmFpgaFileLength=_DvmFpgaFileLength_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,6),_DvmFpgaFileLength_Type())
dvmFpgaFileLength.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaFileLength.setStatus(_A)
_DvmFpgaFileName_Type=DisplayString
_DvmFpgaFileName_Object=MibTableColumn
dvmFpgaFileName=_DvmFpgaFileName_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,7),_DvmFpgaFileName_Type())
dvmFpgaFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaFileName.setStatus(_A)
_DvmFpgaHeaderHCS_Type=Unsigned32
_DvmFpgaHeaderHCS_Object=MibTableColumn
dvmFpgaHeaderHCS=_DvmFpgaHeaderHCS_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,8),_DvmFpgaHeaderHCS_Type())
dvmFpgaHeaderHCS.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaHeaderHCS.setStatus(_A)
_DvmFpgaSoftwareCRC_Type=Unsigned32
_DvmFpgaSoftwareCRC_Object=MibTableColumn
dvmFpgaSoftwareCRC=_DvmFpgaSoftwareCRC_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,2,1,9),_DvmFpgaSoftwareCRC_Type())
dvmFpgaSoftwareCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaSoftwareCRC.setStatus(_A)
_DvmTestFpgaIOtest_ObjectIdentity=ObjectIdentity
dvmTestFpgaIOtest=_DvmTestFpgaIOtest_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,3))
_DvmTestFpgaIoTestRunNow_Type=TruthValue
_DvmTestFpgaIoTestRunNow_Object=MibScalar
dvmTestFpgaIoTestRunNow=_DvmTestFpgaIoTestRunNow_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,3,1),_DvmTestFpgaIoTestRunNow_Type())
dvmTestFpgaIoTestRunNow.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmTestFpgaIoTestRunNow.setStatus(_A)
class _DvmTestFpgaIoTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_F,1),(_E,2),('fail',3)))
_DvmTestFpgaIoTestStatus_Type.__name__=_C
_DvmTestFpgaIoTestStatus_Object=MibScalar
dvmTestFpgaIoTestStatus=_DvmTestFpgaIoTestStatus_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,3,2),_DvmTestFpgaIoTestStatus_Type())
dvmTestFpgaIoTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmTestFpgaIoTestStatus.setStatus(_A)
_DvmTestFpgaIoTestResultTable_Object=MibTable
dvmTestFpgaIoTestResultTable=_DvmTestFpgaIoTestResultTable_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,3,3))
if mibBuilder.loadTexts:dvmTestFpgaIoTestResultTable.setStatus(_A)
_DvmTestFpgaIoTestResultEntry_Object=MibTableRow
dvmTestFpgaIoTestResultEntry=_DvmTestFpgaIoTestResultEntry_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,3,3,1))
dvmTestFpgaIoTestResultEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:dvmTestFpgaIoTestResultEntry.setStatus(_A)
_DvmFpgaIoTestResultIndex_Type=Integer32
_DvmFpgaIoTestResultIndex_Object=MibTableColumn
dvmFpgaIoTestResultIndex=_DvmFpgaIoTestResultIndex_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,3,3,1,1),_DvmFpgaIoTestResultIndex_Type())
dvmFpgaIoTestResultIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaIoTestResultIndex.setStatus(_A)
_DvmFpgaIoTestResultInfo_Type=DisplayString
_DvmFpgaIoTestResultInfo_Object=MibTableColumn
dvmFpgaIoTestResultInfo=_DvmFpgaIoTestResultInfo_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,3,3,1,2),_DvmFpgaIoTestResultInfo_Type())
dvmFpgaIoTestResultInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaIoTestResultInfo.setStatus(_A)
class _DvmFpgaIoTestResultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_E,1),('fail',2)))
_DvmFpgaIoTestResultStatus_Type.__name__=_C
_DvmFpgaIoTestResultStatus_Object=MibTableColumn
dvmFpgaIoTestResultStatus=_DvmFpgaIoTestResultStatus_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,1,3,3,1,3),_DvmFpgaIoTestResultStatus_Type())
dvmFpgaIoTestResultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmFpgaIoTestResultStatus.setStatus(_A)
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,4,2,3))
class _FormatFlash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('format',1))
_FormatFlash_Type.__name__=_C
_FormatFlash_Object=MibScalar
formatFlash=_FormatFlash_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,3,1),_FormatFlash_Type())
formatFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:formatFlash.setStatus(_A)
_MicroControllers_ObjectIdentity=ObjectIdentity
microControllers=_MicroControllers_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,4,2,4))
_RenesassFirmwareVersion_Type=OctetString
_RenesassFirmwareVersion_Object=MibScalar
renesassFirmwareVersion=_RenesassFirmwareVersion_Object((1,3,6,1,4,1,5802,1,3,1,3,4,2,4,1),_RenesassFirmwareVersion_Type())
renesassFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:renesassFirmwareVersion.setStatus(_A)
_Leds_ObjectIdentity=ObjectIdentity
leds=_Leds_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,4,2,5))
mibBuilder.exportSymbols(_I,**{'dvmSwMode':dvmSwMode,'dvmTest':dvmTest,'dvmTestFpga':dvmTestFpga,'dvmTestFpgaSoftwareControl':dvmTestFpgaSoftwareControl,'dvmTestFpgaSwImageNumber':dvmTestFpgaSwImageNumber,'dvmTestFpgaSwDloadTftpServer':dvmTestFpgaSwDloadTftpServer,'dvmTestFpgaSwDloadTftpPath':dvmTestFpgaSwDloadTftpPath,'dvmTestFpgaSwDloadNow':dvmTestFpgaSwDloadNow,'dvmTestFpgaSwDloadStatus':dvmTestFpgaSwDloadStatus,'dvmTestFpgaSwCopyImageFrom':dvmTestFpgaSwCopyImageFrom,'dvmTestFpgaSwCopyStatus':dvmTestFpgaSwCopyStatus,'dvmTestFpgaSwSendImageFrom':dvmTestFpgaSwSendImageFrom,'dvmTestFpgaSwSendImageStatus':dvmTestFpgaSwSendImageStatus,'dvmTestFpgaSotwareTable':dvmTestFpgaSotwareTable,'dvmTestFpgaSotwareEntry':dvmTestFpgaSotwareEntry,_J:dvmFpgaSoftwareTableIndex,'dvmFpgaProcessorId':dvmFpgaProcessorId,'dvmFpgaSoftwareMajorRevision':dvmFpgaSoftwareMajorRevision,'dvmFpgaSoftwareMinorRevision':dvmFpgaSoftwareMinorRevision,'dvmFpgaBuildTime':dvmFpgaBuildTime,'dvmFpgaFileLength':dvmFpgaFileLength,'dvmFpgaFileName':dvmFpgaFileName,'dvmFpgaHeaderHCS':dvmFpgaHeaderHCS,'dvmFpgaSoftwareCRC':dvmFpgaSoftwareCRC,'dvmTestFpgaIOtest':dvmTestFpgaIOtest,'dvmTestFpgaIoTestRunNow':dvmTestFpgaIoTestRunNow,'dvmTestFpgaIoTestStatus':dvmTestFpgaIoTestStatus,'dvmTestFpgaIoTestResultTable':dvmTestFpgaIoTestResultTable,'dvmTestFpgaIoTestResultEntry':dvmTestFpgaIoTestResultEntry,_L:dvmFpgaIoTestResultIndex,'dvmFpgaIoTestResultInfo':dvmFpgaIoTestResultInfo,'dvmFpgaIoTestResultStatus':dvmFpgaIoTestResultStatus,'configuration':configuration,'formatFlash':formatFlash,'microControllers':microControllers,'renesassFirmwareVersion':renesassFirmwareVersion,'leds':leds})