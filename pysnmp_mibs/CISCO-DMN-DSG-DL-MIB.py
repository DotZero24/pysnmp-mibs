_G='dlAboutAppIndex'
_F='CISCO-DMN-DSG-DL-MIB'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ciscoDSGDl=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,1))
if mibBuilder.loadTexts:ciscoDSGDl.setRevisions(('2010-10-13 08:00','2010-08-30 11:00','2010-05-25 08:00','2010-02-12 15:00','2009-12-20 15:00','2009-11-22 15:00'))
_DlAbout_ObjectIdentity=ObjectIdentity
dlAbout=_DlAbout_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,1,1))
class _DlAboutCurrentVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_DlAboutCurrentVer_Type.__name__=_E
_DlAboutCurrentVer_Object=MibScalar
dlAboutCurrentVer=_DlAboutCurrentVer_Object((1,3,6,1,4,1,1429,2,2,5,1,1,1),_DlAboutCurrentVer_Type())
dlAboutCurrentVer.setMaxAccess(_C)
if mibBuilder.loadTexts:dlAboutCurrentVer.setStatus(_A)
class _DlAboutSafeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_DlAboutSafeVer_Type.__name__=_E
_DlAboutSafeVer_Object=MibScalar
dlAboutSafeVer=_DlAboutSafeVer_Object((1,3,6,1,4,1,1429,2,2,5,1,1,2),_DlAboutSafeVer_Type())
dlAboutSafeVer.setMaxAccess(_C)
if mibBuilder.loadTexts:dlAboutSafeVer.setStatus(_A)
class _DlAboutBootVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_DlAboutBootVer_Type.__name__=_E
_DlAboutBootVer_Object=MibScalar
dlAboutBootVer=_DlAboutBootVer_Object((1,3,6,1,4,1,1429,2,2,5,1,1,3),_DlAboutBootVer_Type())
dlAboutBootVer.setMaxAccess(_C)
if mibBuilder.loadTexts:dlAboutBootVer.setStatus(_A)
class _DlAboutProductId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_DlAboutProductId_Type.__name__=_E
_DlAboutProductId_Object=MibScalar
dlAboutProductId=_DlAboutProductId_Object((1,3,6,1,4,1,1429,2,2,5,1,1,4),_DlAboutProductId_Type())
dlAboutProductId.setMaxAccess(_C)
if mibBuilder.loadTexts:dlAboutProductId.setStatus(_A)
class _DlAboutTrackingId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DlAboutTrackingId_Type.__name__=_E
_DlAboutTrackingId_Object=MibScalar
dlAboutTrackingId=_DlAboutTrackingId_Object((1,3,6,1,4,1,1429,2,2,5,1,1,5),_DlAboutTrackingId_Type())
dlAboutTrackingId.setMaxAccess(_C)
if mibBuilder.loadTexts:dlAboutTrackingId.setStatus(_A)
class _DlAboutChangeApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_DlAboutChangeApp_Type.__name__=_B
_DlAboutChangeApp_Object=MibScalar
dlAboutChangeApp=_DlAboutChangeApp_Object((1,3,6,1,4,1,1429,2,2,5,1,1,6),_DlAboutChangeApp_Type())
dlAboutChangeApp.setMaxAccess(_D)
if mibBuilder.loadTexts:dlAboutChangeApp.setStatus(_A)
class _DlAboutEraseApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_DlAboutEraseApp_Type.__name__=_B
_DlAboutEraseApp_Object=MibScalar
dlAboutEraseApp=_DlAboutEraseApp_Object((1,3,6,1,4,1,1429,2,2,5,1,1,7),_DlAboutEraseApp_Type())
dlAboutEraseApp.setMaxAccess(_D)
if mibBuilder.loadTexts:dlAboutEraseApp.setStatus(_A)
class _DlAboutReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_DlAboutReboot_Type.__name__=_B
_DlAboutReboot_Object=MibScalar
dlAboutReboot=_DlAboutReboot_Object((1,3,6,1,4,1,1429,2,2,5,1,1,8),_DlAboutReboot_Type())
dlAboutReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:dlAboutReboot.setStatus(_A)
_DlAboutAppTable_Object=MibTable
dlAboutAppTable=_DlAboutAppTable_Object((1,3,6,1,4,1,1429,2,2,5,1,1,9))
if mibBuilder.loadTexts:dlAboutAppTable.setStatus(_A)
_DlAboutAppEntry_Object=MibTableRow
dlAboutAppEntry=_DlAboutAppEntry_Object((1,3,6,1,4,1,1429,2,2,5,1,1,9,1))
dlAboutAppEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dlAboutAppEntry.setStatus(_A)
class _DlAboutAppIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_DlAboutAppIndex_Type.__name__=_B
_DlAboutAppIndex_Object=MibTableColumn
dlAboutAppIndex=_DlAboutAppIndex_Object((1,3,6,1,4,1,1429,2,2,5,1,1,9,1,1),_DlAboutAppIndex_Type())
dlAboutAppIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dlAboutAppIndex.setStatus(_A)
class _DlAboutAppString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_DlAboutAppString_Type.__name__=_E
_DlAboutAppString_Object=MibTableColumn
dlAboutAppString=_DlAboutAppString_Object((1,3,6,1,4,1,1429,2,2,5,1,1,9,1,2),_DlAboutAppString_Type())
dlAboutAppString.setMaxAccess(_C)
if mibBuilder.loadTexts:dlAboutAppString.setStatus(_A)
_DlDownload_ObjectIdentity=ObjectIdentity
dlDownload=_DlDownload_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,1,2))
_DlDownloadTftpServerIP_Type=IpAddress
_DlDownloadTftpServerIP_Object=MibScalar
dlDownloadTftpServerIP=_DlDownloadTftpServerIP_Object((1,3,6,1,4,1,1429,2,2,5,1,2,1),_DlDownloadTftpServerIP_Type())
dlDownloadTftpServerIP.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadTftpServerIP.setStatus(_A)
class _DlDownloadMicroCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DlDownloadMicroCode_Type.__name__=_B
_DlDownloadMicroCode_Object=MibScalar
dlDownloadMicroCode=_DlDownloadMicroCode_Object((1,3,6,1,4,1,1429,2,2,5,1,2,2),_DlDownloadMicroCode_Type())
dlDownloadMicroCode.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadMicroCode.setStatus(_A)
class _DlDownloadCodeVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlDownloadCodeVersion_Type.__name__=_B
_DlDownloadCodeVersion_Object=MibScalar
dlDownloadCodeVersion=_DlDownloadCodeVersion_Object((1,3,6,1,4,1,1429,2,2,5,1,2,3),_DlDownloadCodeVersion_Type())
dlDownloadCodeVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadCodeVersion.setStatus(_A)
class _DlDownloadNanoVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DlDownloadNanoVersion_Type.__name__=_B
_DlDownloadNanoVersion_Object=MibScalar
dlDownloadNanoVersion=_DlDownloadNanoVersion_Object((1,3,6,1,4,1,1429,2,2,5,1,2,4),_DlDownloadNanoVersion_Type())
dlDownloadNanoVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadNanoVersion.setStatus(_A)
class _DlDownloadBankSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DlDownloadBankSelect_Type.__name__=_B
_DlDownloadBankSelect_Object=MibScalar
dlDownloadBankSelect=_DlDownloadBankSelect_Object((1,3,6,1,4,1,1429,2,2,5,1,2,5),_DlDownloadBankSelect_Type())
dlDownloadBankSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadBankSelect.setStatus(_A)
class _DlDownloadForcedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_DlDownloadForcedFlag_Type.__name__=_B
_DlDownloadForcedFlag_Object=MibScalar
dlDownloadForcedFlag=_DlDownloadForcedFlag_Object((1,3,6,1,4,1,1429,2,2,5,1,2,6),_DlDownloadForcedFlag_Type())
dlDownloadForcedFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadForcedFlag.setStatus(_A)
class _DlDownloadTransitionBlocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DlDownloadTransitionBlocked_Type.__name__=_B
_DlDownloadTransitionBlocked_Object=MibScalar
dlDownloadTransitionBlocked=_DlDownloadTransitionBlocked_Object((1,3,6,1,4,1,1429,2,2,5,1,2,7),_DlDownloadTransitionBlocked_Type())
dlDownloadTransitionBlocked.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadTransitionBlocked.setStatus(_A)
class _DlDownloadTftpFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DlDownloadTftpFilename_Type.__name__=_E
_DlDownloadTftpFilename_Object=MibScalar
dlDownloadTftpFilename=_DlDownloadTftpFilename_Object((1,3,6,1,4,1,1429,2,2,5,1,2,8),_DlDownloadTftpFilename_Type())
dlDownloadTftpFilename.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadTftpFilename.setStatus(_A)
class _DlDownloadAbort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('abort',1)))
_DlDownloadAbort_Type.__name__=_B
_DlDownloadAbort_Object=MibScalar
dlDownloadAbort=_DlDownloadAbort_Object((1,3,6,1,4,1,1429,2,2,5,1,2,9),_DlDownloadAbort_Type())
dlDownloadAbort.setMaxAccess(_D)
if mibBuilder.loadTexts:dlDownloadAbort.setStatus(_A)
class _DlDownloadState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idle',0),('busy',1)))
_DlDownloadState_Type.__name__=_B
_DlDownloadState_Object=MibScalar
dlDownloadState=_DlDownloadState_Object((1,3,6,1,4,1,1429,2,2,5,1,2,10),_DlDownloadState_Type())
dlDownloadState.setMaxAccess(_C)
if mibBuilder.loadTexts:dlDownloadState.setStatus(_A)
class _DlDownloadErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ok',0),('reject',1),('fails',2)))
_DlDownloadErrorStatus_Type.__name__=_B
_DlDownloadErrorStatus_Object=MibScalar
dlDownloadErrorStatus=_DlDownloadErrorStatus_Object((1,3,6,1,4,1,1429,2,2,5,1,2,11),_DlDownloadErrorStatus_Type())
dlDownloadErrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlDownloadErrorStatus.setStatus(_A)
_DlCfg_ObjectIdentity=ObjectIdentity
dlCfg=_DlCfg_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,1,3))
class _DlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noTrigger',1),('download',2),('trigger',3)))
_DlStatus_Type.__name__=_B
_DlStatus_Object=MibScalar
dlStatus=_DlStatus_Object((1,3,6,1,4,1,1429,2,2,5,1,3,1),_DlStatus_Type())
dlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlStatus.setStatus(_A)
class _DlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('always',1),('once',2),('never',3)))
_DlMode_Type.__name__=_B
_DlMode_Object=MibScalar
dlMode=_DlMode_Object((1,3,6,1,4,1,1429,2,2,5,1,3,2),_DlMode_Type())
dlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dlMode.setStatus(_A)
class _DlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('rearPanel',2),('http',3),('overAir',4)))
_DlType_Type.__name__=_B
_DlType_Object=MibScalar
dlType=_DlType_Object((1,3,6,1,4,1,1429,2,2,5,1,3,3),_DlType_Type())
dlType.setMaxAccess(_C)
if mibBuilder.loadTexts:dlType.setStatus(_A)
class _DlBank_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('app5514',1),('app7109',2),('fpga7109',3),('sat7109',4),('screenLogo',5),('menuLogo',6),('ethLogo',7),('appPPC',8),('appVASA',9),('dbUpdate',10),('execBin',11)))
_DlBank_Type.__name__=_B
_DlBank_Object=MibScalar
dlBank=_DlBank_Object((1,3,6,1,4,1,1429,2,2,5,1,3,4),_DlBank_Type())
dlBank.setMaxAccess(_C)
if mibBuilder.loadTexts:dlBank.setStatus(_A)
class _DlTotalCdt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DlTotalCdt_Type.__name__=_E
_DlTotalCdt_Object=MibScalar
dlTotalCdt=_DlTotalCdt_Object((1,3,6,1,4,1,1429,2,2,5,1,3,5),_DlTotalCdt_Type())
dlTotalCdt.setMaxAccess(_C)
if mibBuilder.loadTexts:dlTotalCdt.setStatus(_A)
class _DlReceived_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DlReceived_Type.__name__=_E
_DlReceived_Object=MibScalar
dlReceived=_DlReceived_Object((1,3,6,1,4,1,1429,2,2,5,1,3,6),_DlReceived_Type())
dlReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:dlReceived.setStatus(_A)
class _DlRejected_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DlRejected_Type.__name__=_E
_DlRejected_Object=MibScalar
dlRejected=_DlRejected_Object((1,3,6,1,4,1,1429,2,2,5,1,3,7),_DlRejected_Type())
dlRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:dlRejected.setStatus(_A)
class _DlCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('restart',1),('abort',2),('writeOnly',3)))
_DlCommand_Type.__name__=_B
_DlCommand_Object=MibScalar
dlCommand=_DlCommand_Object((1,3,6,1,4,1,1429,2,2,5,1,3,8),_DlCommand_Type())
dlCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:dlCommand.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ciscoDSGDl':ciscoDSGDl,'dlAbout':dlAbout,'dlAboutCurrentVer':dlAboutCurrentVer,'dlAboutSafeVer':dlAboutSafeVer,'dlAboutBootVer':dlAboutBootVer,'dlAboutProductId':dlAboutProductId,'dlAboutTrackingId':dlAboutTrackingId,'dlAboutChangeApp':dlAboutChangeApp,'dlAboutEraseApp':dlAboutEraseApp,'dlAboutReboot':dlAboutReboot,'dlAboutAppTable':dlAboutAppTable,'dlAboutAppEntry':dlAboutAppEntry,_G:dlAboutAppIndex,'dlAboutAppString':dlAboutAppString,'dlDownload':dlDownload,'dlDownloadTftpServerIP':dlDownloadTftpServerIP,'dlDownloadMicroCode':dlDownloadMicroCode,'dlDownloadCodeVersion':dlDownloadCodeVersion,'dlDownloadNanoVersion':dlDownloadNanoVersion,'dlDownloadBankSelect':dlDownloadBankSelect,'dlDownloadForcedFlag':dlDownloadForcedFlag,'dlDownloadTransitionBlocked':dlDownloadTransitionBlocked,'dlDownloadTftpFilename':dlDownloadTftpFilename,'dlDownloadAbort':dlDownloadAbort,'dlDownloadState':dlDownloadState,'dlDownloadErrorStatus':dlDownloadErrorStatus,'dlCfg':dlCfg,'dlStatus':dlStatus,'dlMode':dlMode,'dlType':dlType,'dlBank':dlBank,'dlTotalCdt':dlTotalCdt,'dlReceived':dlReceived,'dlRejected':dlRejected,'dlCommand':dlCommand})