_H='normalOperation'
_G='DisplayString'
_F='OctetString'
_E='Integer32'
_D='mandatory'
_C='read-write'
_B='read-only'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctDownLoad,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDownLoad')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_CtDL_ObjectIdentity=ObjectIdentity
ctDL=_CtDL_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,8,1))
_CtDLForceOnBoot_Type=Integer32
_CtDLForceOnBoot_Object=MibScalar
ctDLForceOnBoot=_CtDLForceOnBoot_Object((1,3,6,1,4,1,52,4,1,5,8,1,1),_CtDLForceOnBoot_Type())
ctDLForceOnBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLForceOnBoot.setStatus(_A)
_CtDLCommitRAMToFlash_Type=Integer32
_CtDLCommitRAMToFlash_Object=MibScalar
ctDLCommitRAMToFlash=_CtDLCommitRAMToFlash_Object((1,3,6,1,4,1,52,4,1,5,8,1,2),_CtDLCommitRAMToFlash_Type())
ctDLCommitRAMToFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLCommitRAMToFlash.setStatus(_A)
_CtDLInitiateColdBoot_Type=Integer32
_CtDLInitiateColdBoot_Object=MibScalar
ctDLInitiateColdBoot=_CtDLInitiateColdBoot_Object((1,3,6,1,4,1,52,4,1,5,8,1,3),_CtDLInitiateColdBoot_Type())
ctDLInitiateColdBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLInitiateColdBoot.setStatus(_D)
_CtDLTFTPRequestHost_Type=IpAddress
_CtDLTFTPRequestHost_Object=MibScalar
ctDLTFTPRequestHost=_CtDLTFTPRequestHost_Object((1,3,6,1,4,1,52,4,1,5,8,1,4),_CtDLTFTPRequestHost_Type())
ctDLTFTPRequestHost.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLTFTPRequestHost.setStatus(_A)
_CtDLTFTPRequest_Type=DisplayString
_CtDLTFTPRequest_Object=MibScalar
ctDLTFTPRequest=_CtDLTFTPRequest_Object((1,3,6,1,4,1,52,4,1,5,8,1,5),_CtDLTFTPRequest_Type())
ctDLTFTPRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLTFTPRequest.setStatus(_A)
_CtDLLastImageFilename_Type=DisplayString
_CtDLLastImageFilename_Object=MibScalar
ctDLLastImageFilename=_CtDLLastImageFilename_Object((1,3,6,1,4,1,52,4,1,5,8,1,6),_CtDLLastImageFilename_Type())
ctDLLastImageFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLLastImageFilename.setStatus(_D)
_CtDLLastServerIPAddress_Type=IpAddress
_CtDLLastServerIPAddress_Object=MibScalar
ctDLLastServerIPAddress=_CtDLLastServerIPAddress_Object((1,3,6,1,4,1,52,4,1,5,8,1,7),_CtDLLastServerIPAddress_Type())
ctDLLastServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLLastServerIPAddress.setStatus(_D)
_CtDLFlashSize_Type=Integer32
_CtDLFlashSize_Object=MibScalar
ctDLFlashSize=_CtDLFlashSize_Object((1,3,6,1,4,1,52,4,1,5,8,1,8),_CtDLFlashSize_Type())
ctDLFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLFlashSize.setStatus(_A)
_CtDLFlashCount_Type=Integer32
_CtDLFlashCount_Object=MibScalar
ctDLFlashCount=_CtDLFlashCount_Object((1,3,6,1,4,1,52,4,1,5,8,1,9),_CtDLFlashCount_Type())
ctDLFlashCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLFlashCount.setStatus(_A)
_CtDLFirmwareBase_Type=Integer32
_CtDLFirmwareBase_Object=MibScalar
ctDLFirmwareBase=_CtDLFirmwareBase_Object((1,3,6,1,4,1,52,4,1,5,8,1,10),_CtDLFirmwareBase_Type())
ctDLFirmwareBase.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLFirmwareBase.setStatus(_A)
_CtDLFirmwareTop_Type=Integer32
_CtDLFirmwareTop_Object=MibScalar
ctDLFirmwareTop=_CtDLFirmwareTop_Object((1,3,6,1,4,1,52,4,1,5,8,1,11),_CtDLFirmwareTop_Type())
ctDLFirmwareTop.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLFirmwareTop.setStatus(_A)
_CtDLFirmwareStart_Type=Integer32
_CtDLFirmwareStart_Object=MibScalar
ctDLFirmwareStart=_CtDLFirmwareStart_Object((1,3,6,1,4,1,52,4,1,5,8,1,12),_CtDLFirmwareStart_Type())
ctDLFirmwareStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLFirmwareStart.setStatus(_A)
class _CtDLBootRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,9));fixedLength=9
_CtDLBootRev_Type.__name__=_F
_CtDLBootRev_Object=MibScalar
ctDLBootRev=_CtDLBootRev_Object((1,3,6,1,4,1,52,4,1,5,8,1,13),_CtDLBootRev_Type())
ctDLBootRev.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLBootRev.setStatus(_A)
_CtDLForceBootp_Type=Integer32
_CtDLForceBootp_Object=MibScalar
ctDLForceBootp=_CtDLForceBootp_Object((1,3,6,1,4,1,52,4,1,5,8,1,14),_CtDLForceBootp_Type())
ctDLForceBootp.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLForceBootp.setStatus(_A)
_CtDLServerName_Type=OctetString
_CtDLServerName_Object=MibScalar
ctDLServerName=_CtDLServerName_Object((1,3,6,1,4,1,52,4,1,5,8,1,15),_CtDLServerName_Type())
ctDLServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLServerName.setStatus(_A)
class _CtDLOnLineDownLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('forceDownLoad',2),('forceDownLoadReset',3),('downLoadConfiguration',4),('upLoadConfiguration',5)))
_CtDLOnLineDownLoad_Type.__name__=_E
_CtDLOnLineDownLoad_Object=MibScalar
ctDLOnLineDownLoad=_CtDLOnLineDownLoad_Object((1,3,6,1,4,1,52,4,1,5,8,1,16),_CtDLOnLineDownLoad_Type())
ctDLOnLineDownLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLOnLineDownLoad.setStatus(_D)
class _CtDLOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('unknown',2),(_H,3),('downLoadActive',4),('downLoadCompleteError',5)))
_CtDLOperStatus_Type.__name__=_E
_CtDLOperStatus_Object=MibScalar
ctDLOperStatus=_CtDLOperStatus_Object((1,3,6,1,4,1,52,4,1,5,8,1,17),_CtDLOperStatus_Type())
ctDLOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLOperStatus.setStatus(_D)
_CtDLNetAddress_Type=IpAddress
_CtDLNetAddress_Object=MibScalar
ctDLNetAddress=_CtDLNetAddress_Object((1,3,6,1,4,1,52,4,1,5,8,1,18),_CtDLNetAddress_Type())
ctDLNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLNetAddress.setStatus(_D)
class _CtDLFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CtDLFileName_Type.__name__=_G
_CtDLFileName_Object=MibScalar
ctDLFileName=_CtDLFileName_Object((1,3,6,1,4,1,52,4,1,5,8,1,19),_CtDLFileName_Type())
ctDLFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLFileName.setStatus(_D)
_CtDLErrorString_Type=DisplayString
_CtDLErrorString_Object=MibScalar
ctDLErrorString=_CtDLErrorString_Object((1,3,6,1,4,1,52,4,1,5,8,1,20),_CtDLErrorString_Type())
ctDLErrorString.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLErrorString.setStatus(_D)
_CtDLTftpServerGatewayIPAddress_Type=IpAddress
_CtDLTftpServerGatewayIPAddress_Object=MibScalar
ctDLTftpServerGatewayIPAddress=_CtDLTftpServerGatewayIPAddress_Object((1,3,6,1,4,1,52,4,1,5,8,1,21),_CtDLTftpServerGatewayIPAddress_Type())
ctDLTftpServerGatewayIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDLTftpServerGatewayIPAddress.setStatus(_A)
_CtDLBlockCount_Type=Integer32
_CtDLBlockCount_Object=MibScalar
ctDLBlockCount=_CtDLBlockCount_Object((1,3,6,1,4,1,52,4,1,5,8,1,22),_CtDLBlockCount_Type())
ctDLBlockCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLBlockCount.setStatus(_D)
class _CtDLBootPartitionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('good',1),('bad',2),('inProgress',3)))
_CtDLBootPartitionStatus_Type.__name__=_E
_CtDLBootPartitionStatus_Object=MibScalar
ctDLBootPartitionStatus=_CtDLBootPartitionStatus_Object((1,3,6,1,4,1,52,4,1,5,8,1,23),_CtDLBootPartitionStatus_Type())
ctDLBootPartitionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDLBootPartitionStatus.setStatus(_A)
mibBuilder.exportSymbols('CTRON-DOWNLOAD-MIB',**{'ctDL':ctDL,'ctDLForceOnBoot':ctDLForceOnBoot,'ctDLCommitRAMToFlash':ctDLCommitRAMToFlash,'ctDLInitiateColdBoot':ctDLInitiateColdBoot,'ctDLTFTPRequestHost':ctDLTFTPRequestHost,'ctDLTFTPRequest':ctDLTFTPRequest,'ctDLLastImageFilename':ctDLLastImageFilename,'ctDLLastServerIPAddress':ctDLLastServerIPAddress,'ctDLFlashSize':ctDLFlashSize,'ctDLFlashCount':ctDLFlashCount,'ctDLFirmwareBase':ctDLFirmwareBase,'ctDLFirmwareTop':ctDLFirmwareTop,'ctDLFirmwareStart':ctDLFirmwareStart,'ctDLBootRev':ctDLBootRev,'ctDLForceBootp':ctDLForceBootp,'ctDLServerName':ctDLServerName,'ctDLOnLineDownLoad':ctDLOnLineDownLoad,'ctDLOperStatus':ctDLOperStatus,'ctDLNetAddress':ctDLNetAddress,'ctDLFileName':ctDLFileName,'ctDLErrorString':ctDLErrorString,'ctDLTftpServerGatewayIPAddress':ctDLTftpServerGatewayIPAddress,'ctDLBlockCount':ctDLBlockCount,'ctDLBootPartitionStatus':ctDLBootPartitionStatus})