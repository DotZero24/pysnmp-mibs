_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtMIBObjects')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ftpMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,12))
if mibBuilder.loadTexts:ftpMgmt.setRevisions(('2009-08-12 00:00','2009-03-04 00:00'))
class _FtpIpStackInterface_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_FtpIpStackInterface_Type.__name__=_C
_FtpIpStackInterface_Object=MibScalar
ftpIpStackInterface=_FtpIpStackInterface_Object((1,3,6,1,4,1,4413,2,2,2,1,12,1),_FtpIpStackInterface_Type())
ftpIpStackInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpIpStackInterface.setStatus(_A)
_FtpServerAddressType_Type=InetAddressType
_FtpServerAddressType_Object=MibScalar
ftpServerAddressType=_FtpServerAddressType_Object((1,3,6,1,4,1,4413,2,2,2,1,12,2),_FtpServerAddressType_Type())
ftpServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpServerAddressType.setStatus(_A)
_FtpServerAddress_Type=InetAddress
_FtpServerAddress_Object=MibScalar
ftpServerAddress=_FtpServerAddress_Object((1,3,6,1,4,1,4413,2,2,2,1,12,3),_FtpServerAddress_Type())
ftpServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpServerAddress.setStatus(_A)
class _FtpServerPort_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FtpServerPort_Type.__name__=_C
_FtpServerPort_Object=MibScalar
ftpServerPort=_FtpServerPort_Object((1,3,6,1,4,1,4413,2,2,2,1,12,4),_FtpServerPort_Type())
ftpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpServerPort.setStatus(_A)
class _FtpUserName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FtpUserName_Type.__name__=_E
_FtpUserName_Object=MibScalar
ftpUserName=_FtpUserName_Object((1,3,6,1,4,1,4413,2,2,2,1,12,5),_FtpUserName_Type())
ftpUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpUserName.setStatus(_A)
class _FtpPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FtpPassword_Type.__name__=_E
_FtpPassword_Object=MibScalar
ftpPassword=_FtpPassword_Object((1,3,6,1,4,1,4413,2,2,2,1,12,6),_FtpPassword_Type())
ftpPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpPassword.setStatus(_A)
class _FtpFilename_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FtpFilename_Type.__name__=_E
_FtpFilename_Object=MibScalar
ftpFilename=_FtpFilename_Object((1,3,6,1,4,1,4413,2,2,2,1,12,7),_FtpFilename_Type())
ftpFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpFilename.setStatus(_A)
class _FtpCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cancel',0),('get',1)))
_FtpCommand_Type.__name__=_C
_FtpCommand_Object=MibScalar
ftpCommand=_FtpCommand_Object((1,3,6,1,4,1,4413,2,2,2,1,12,8),_FtpCommand_Type())
ftpCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpCommand.setStatus(_A)
class _FtpTransferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,150,200,221,226,230,331,421,530,550,600)));namedValues=NamedValues(*(('idle',0),('fileStatusOk',150),('serviceReady',200),('sessionReady',221),('transferComplete',226),('passwordOk',230),('userNameOk',331),('serviceNotAvail',421),('invalidLogin',530),('fileNotFound',550),('socketConnectFailure',600)))
_FtpTransferStatus_Type.__name__=_C
_FtpTransferStatus_Object=MibScalar
ftpTransferStatus=_FtpTransferStatus_Object((1,3,6,1,4,1,4413,2,2,2,1,12,9),_FtpTransferStatus_Type())
ftpTransferStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpTransferStatus.setStatus(_A)
_FtpTransferPayloadBytes_Type=Counter32
_FtpTransferPayloadBytes_Object=MibScalar
ftpTransferPayloadBytes=_FtpTransferPayloadBytes_Object((1,3,6,1,4,1,4413,2,2,2,1,12,10),_FtpTransferPayloadBytes_Type())
ftpTransferPayloadBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpTransferPayloadBytes.setStatus(_A)
_FtpTransferTotalBytes_Type=Counter32
_FtpTransferTotalBytes_Object=MibScalar
ftpTransferTotalBytes=_FtpTransferTotalBytes_Object((1,3,6,1,4,1,4413,2,2,2,1,12,11),_FtpTransferTotalBytes_Type())
ftpTransferTotalBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpTransferTotalBytes.setStatus(_A)
_FtpTransferElapsedTime_Type=Counter32
_FtpTransferElapsedTime_Object=MibScalar
ftpTransferElapsedTime=_FtpTransferElapsedTime_Object((1,3,6,1,4,1,4413,2,2,2,1,12,12),_FtpTransferElapsedTime_Type())
ftpTransferElapsedTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpTransferElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:ftpTransferElapsedTime.setUnits('milliseconds')
_FtpTransferThroughput_Type=Unsigned32
_FtpTransferThroughput_Object=MibScalar
ftpTransferThroughput=_FtpTransferThroughput_Object((1,3,6,1,4,1,4413,2,2,2,1,12,13),_FtpTransferThroughput_Type())
ftpTransferThroughput.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpTransferThroughput.setStatus(_A)
if mibBuilder.loadTexts:ftpTransferThroughput.setUnits('bits per second')
mibBuilder.exportSymbols('BRCM-FTP-MGMT-MIB',**{'ftpMgmt':ftpMgmt,'ftpIpStackInterface':ftpIpStackInterface,'ftpServerAddressType':ftpServerAddressType,'ftpServerAddress':ftpServerAddress,'ftpServerPort':ftpServerPort,'ftpUserName':ftpUserName,'ftpPassword':ftpPassword,'ftpFilename':ftpFilename,'ftpCommand':ftpCommand,'ftpTransferStatus':ftpTransferStatus,'ftpTransferPayloadBytes':ftpTransferPayloadBytes,'ftpTransferTotalBytes':ftpTransferTotalBytes,'ftpTransferElapsedTime':ftpTransferElapsedTime,'ftpTransferThroughput':ftpTransferThroughput})