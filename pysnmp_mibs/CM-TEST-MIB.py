_M='bits per second'
_L='milliseconds'
_K='invalidLogin'
_J='serviceNotAvail'
_I='transferComplete'
_H='inProgress'
_G='cancel'
_F='InetPortNumber'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TimeInterval')
cmTestMib=ModuleIdentity((1,3,6,1,4,1,1166,1,19,61))
if mibBuilder.loadTexts:cmTestMib.setRevisions(('2011-05-20 10:00','2010-03-26 10:00','2009-12-16 10:00','2009-05-11 10:00'))
_Gi_ObjectIdentity=ObjectIdentity
gi=_Gi_ObjectIdentity((1,3,6,1,4,1,1166))
_Giproducts_ObjectIdentity=ObjectIdentity
giproducts=_Giproducts_ObjectIdentity((1,3,6,1,4,1,1166,1))
_Cm_ObjectIdentity=ObjectIdentity
cm=_Cm_ObjectIdentity((1,3,6,1,4,1,1166,1,19))
_CmTestFtpDownstreamSpeed_ObjectIdentity=ObjectIdentity
cmTestFtpDownstreamSpeed=_CmTestFtpDownstreamSpeed_ObjectIdentity((1,3,6,1,4,1,1166,1,19,61,1))
_CmTestFtpServerAddressType_Type=InetAddressType
_CmTestFtpServerAddressType_Object=MibScalar
cmTestFtpServerAddressType=_CmTestFtpServerAddressType_Object((1,3,6,1,4,1,1166,1,19,61,1,1),_CmTestFtpServerAddressType_Type())
cmTestFtpServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpServerAddressType.setStatus(_A)
class _CmTestFtpServerAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmTestFtpServerAddress_Type.__name__=_D
_CmTestFtpServerAddress_Object=MibScalar
cmTestFtpServerAddress=_CmTestFtpServerAddress_Object((1,3,6,1,4,1,1166,1,19,61,1,2),_CmTestFtpServerAddress_Type())
cmTestFtpServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpServerAddress.setStatus(_A)
class _CmTestFtpServerPort_Type(InetPortNumber):defaultValue=21
_CmTestFtpServerPort_Type.__name__=_F
_CmTestFtpServerPort_Object=MibScalar
cmTestFtpServerPort=_CmTestFtpServerPort_Object((1,3,6,1,4,1,1166,1,19,61,1,3),_CmTestFtpServerPort_Type())
cmTestFtpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpServerPort.setStatus(_A)
class _CmTestFtpUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmTestFtpUserName_Type.__name__=_D
_CmTestFtpUserName_Object=MibScalar
cmTestFtpUserName=_CmTestFtpUserName_Object((1,3,6,1,4,1,1166,1,19,61,1,4),_CmTestFtpUserName_Type())
cmTestFtpUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUserName.setStatus(_A)
class _CmTestFtpPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmTestFtpPassword_Type.__name__=_D
_CmTestFtpPassword_Object=MibScalar
cmTestFtpPassword=_CmTestFtpPassword_Object((1,3,6,1,4,1,1166,1,19,61,1,5),_CmTestFtpPassword_Type())
cmTestFtpPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpPassword.setStatus(_A)
class _CmTestFtpFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmTestFtpFilename_Type.__name__=_D
_CmTestFtpFilename_Object=MibScalar
cmTestFtpFilename=_CmTestFtpFilename_Object((1,3,6,1,4,1,1166,1,19,61,1,6),_CmTestFtpFilename_Type())
cmTestFtpFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpFilename.setStatus(_A)
class _CmTestFtpCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('get',1)))
_CmTestFtpCommand_Type.__name__=_E
_CmTestFtpCommand_Object=MibScalar
cmTestFtpCommand=_CmTestFtpCommand_Object((1,3,6,1,4,1,1166,1,19,61,1,7),_CmTestFtpCommand_Type())
cmTestFtpCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpCommand.setStatus(_A)
class _CmTestFtpTransferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,226,421,530,550)));namedValues=NamedValues(*(('idle',0),(_H,1),(_I,226),(_J,421),(_K,530),('fileNotFound',550)))
_CmTestFtpTransferStatus_Type.__name__=_E
_CmTestFtpTransferStatus_Object=MibScalar
cmTestFtpTransferStatus=_CmTestFtpTransferStatus_Object((1,3,6,1,4,1,1166,1,19,61,1,8),_CmTestFtpTransferStatus_Type())
cmTestFtpTransferStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpTransferStatus.setStatus(_A)
_CmTestFtpTransferPayloadBytes_Type=Counter32
_CmTestFtpTransferPayloadBytes_Object=MibScalar
cmTestFtpTransferPayloadBytes=_CmTestFtpTransferPayloadBytes_Object((1,3,6,1,4,1,1166,1,19,61,1,9),_CmTestFtpTransferPayloadBytes_Type())
cmTestFtpTransferPayloadBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpTransferPayloadBytes.setStatus(_A)
_CmTestFtpTransferTotalBytes_Type=Counter32
_CmTestFtpTransferTotalBytes_Object=MibScalar
cmTestFtpTransferTotalBytes=_CmTestFtpTransferTotalBytes_Object((1,3,6,1,4,1,1166,1,19,61,1,10),_CmTestFtpTransferTotalBytes_Type())
cmTestFtpTransferTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpTransferTotalBytes.setStatus(_A)
_CmTestFtpTransferElapsedTime_Type=TimeInterval
_CmTestFtpTransferElapsedTime_Object=MibScalar
cmTestFtpTransferElapsedTime=_CmTestFtpTransferElapsedTime_Object((1,3,6,1,4,1,1166,1,19,61,1,11),_CmTestFtpTransferElapsedTime_Type())
cmTestFtpTransferElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpTransferElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:cmTestFtpTransferElapsedTime.setUnits(_L)
_CmTestFtpTransferThroughput_Type=Unsigned32
_CmTestFtpTransferThroughput_Object=MibScalar
cmTestFtpTransferThroughput=_CmTestFtpTransferThroughput_Object((1,3,6,1,4,1,1166,1,19,61,1,12),_CmTestFtpTransferThroughput_Type())
cmTestFtpTransferThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpTransferThroughput.setStatus(_A)
if mibBuilder.loadTexts:cmTestFtpTransferThroughput.setUnits(_M)
_CmTestFtpUpstreamSpeed_ObjectIdentity=ObjectIdentity
cmTestFtpUpstreamSpeed=_CmTestFtpUpstreamSpeed_ObjectIdentity((1,3,6,1,4,1,1166,1,19,61,2))
_CmTestFtpUpstreamServerAddressType_Type=InetAddressType
_CmTestFtpUpstreamServerAddressType_Object=MibScalar
cmTestFtpUpstreamServerAddressType=_CmTestFtpUpstreamServerAddressType_Object((1,3,6,1,4,1,1166,1,19,61,2,1),_CmTestFtpUpstreamServerAddressType_Type())
cmTestFtpUpstreamServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUpstreamServerAddressType.setStatus(_A)
class _CmTestFtpUpstreamServerAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmTestFtpUpstreamServerAddress_Type.__name__=_D
_CmTestFtpUpstreamServerAddress_Object=MibScalar
cmTestFtpUpstreamServerAddress=_CmTestFtpUpstreamServerAddress_Object((1,3,6,1,4,1,1166,1,19,61,2,2),_CmTestFtpUpstreamServerAddress_Type())
cmTestFtpUpstreamServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUpstreamServerAddress.setStatus(_A)
class _CmTestFtpUpstreamServerPort_Type(InetPortNumber):defaultValue=21
_CmTestFtpUpstreamServerPort_Type.__name__=_F
_CmTestFtpUpstreamServerPort_Object=MibScalar
cmTestFtpUpstreamServerPort=_CmTestFtpUpstreamServerPort_Object((1,3,6,1,4,1,1166,1,19,61,2,3),_CmTestFtpUpstreamServerPort_Type())
cmTestFtpUpstreamServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUpstreamServerPort.setStatus(_A)
class _CmTestFtpUpstreamUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmTestFtpUpstreamUserName_Type.__name__=_D
_CmTestFtpUpstreamUserName_Object=MibScalar
cmTestFtpUpstreamUserName=_CmTestFtpUpstreamUserName_Object((1,3,6,1,4,1,1166,1,19,61,2,4),_CmTestFtpUpstreamUserName_Type())
cmTestFtpUpstreamUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUpstreamUserName.setStatus(_A)
class _CmTestFtpUpstreamPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmTestFtpUpstreamPassword_Type.__name__=_D
_CmTestFtpUpstreamPassword_Object=MibScalar
cmTestFtpUpstreamPassword=_CmTestFtpUpstreamPassword_Object((1,3,6,1,4,1,1166,1,19,61,2,5),_CmTestFtpUpstreamPassword_Type())
cmTestFtpUpstreamPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUpstreamPassword.setStatus(_A)
class _CmTestFtpUpstreamFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmTestFtpUpstreamFilename_Type.__name__=_D
_CmTestFtpUpstreamFilename_Object=MibScalar
cmTestFtpUpstreamFilename=_CmTestFtpUpstreamFilename_Object((1,3,6,1,4,1,1166,1,19,61,2,6),_CmTestFtpUpstreamFilename_Type())
cmTestFtpUpstreamFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUpstreamFilename.setStatus(_A)
_CmTestFtpUpstreamFileSize_Type=Counter32
_CmTestFtpUpstreamFileSize_Object=MibScalar
cmTestFtpUpstreamFileSize=_CmTestFtpUpstreamFileSize_Object((1,3,6,1,4,1,1166,1,19,61,2,7),_CmTestFtpUpstreamFileSize_Type())
cmTestFtpUpstreamFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUpstreamFileSize.setStatus(_A)
class _CmTestFtpUpstreamCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('put',1)))
_CmTestFtpUpstreamCommand_Type.__name__=_E
_CmTestFtpUpstreamCommand_Object=MibScalar
cmTestFtpUpstreamCommand=_CmTestFtpUpstreamCommand_Object((1,3,6,1,4,1,1166,1,19,61,2,8),_CmTestFtpUpstreamCommand_Type())
cmTestFtpUpstreamCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:cmTestFtpUpstreamCommand.setStatus(_A)
class _CmTestFtpUpstreamTransferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,226,421,530)));namedValues=NamedValues(*(('idle',0),(_H,1),(_I,226),(_J,421),(_K,530)))
_CmTestFtpUpstreamTransferStatus_Type.__name__=_E
_CmTestFtpUpstreamTransferStatus_Object=MibScalar
cmTestFtpUpstreamTransferStatus=_CmTestFtpUpstreamTransferStatus_Object((1,3,6,1,4,1,1166,1,19,61,2,9),_CmTestFtpUpstreamTransferStatus_Type())
cmTestFtpUpstreamTransferStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpUpstreamTransferStatus.setStatus(_A)
_CmTestFtpUpstreamTransferPayloadBytes_Type=Counter32
_CmTestFtpUpstreamTransferPayloadBytes_Object=MibScalar
cmTestFtpUpstreamTransferPayloadBytes=_CmTestFtpUpstreamTransferPayloadBytes_Object((1,3,6,1,4,1,1166,1,19,61,2,10),_CmTestFtpUpstreamTransferPayloadBytes_Type())
cmTestFtpUpstreamTransferPayloadBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpUpstreamTransferPayloadBytes.setStatus(_A)
_CmTestFtpUpstreamTransferTotalBytes_Type=Counter32
_CmTestFtpUpstreamTransferTotalBytes_Object=MibScalar
cmTestFtpUpstreamTransferTotalBytes=_CmTestFtpUpstreamTransferTotalBytes_Object((1,3,6,1,4,1,1166,1,19,61,2,11),_CmTestFtpUpstreamTransferTotalBytes_Type())
cmTestFtpUpstreamTransferTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpUpstreamTransferTotalBytes.setStatus(_A)
_CmTestFtpUpstreamTransferElapsedTime_Type=TimeInterval
_CmTestFtpUpstreamTransferElapsedTime_Object=MibScalar
cmTestFtpUpstreamTransferElapsedTime=_CmTestFtpUpstreamTransferElapsedTime_Object((1,3,6,1,4,1,1166,1,19,61,2,12),_CmTestFtpUpstreamTransferElapsedTime_Type())
cmTestFtpUpstreamTransferElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpUpstreamTransferElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:cmTestFtpUpstreamTransferElapsedTime.setUnits(_L)
_CmTestFtpUpstreamTransferThroughput_Type=Unsigned32
_CmTestFtpUpstreamTransferThroughput_Object=MibScalar
cmTestFtpUpstreamTransferThroughput=_CmTestFtpUpstreamTransferThroughput_Object((1,3,6,1,4,1,1166,1,19,61,2,13),_CmTestFtpUpstreamTransferThroughput_Type())
cmTestFtpUpstreamTransferThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTestFtpUpstreamTransferThroughput.setStatus(_A)
if mibBuilder.loadTexts:cmTestFtpUpstreamTransferThroughput.setUnits(_M)
mibBuilder.exportSymbols('CM-TEST-MIB',**{'gi':gi,'giproducts':giproducts,'cm':cm,'cmTestMib':cmTestMib,'cmTestFtpDownstreamSpeed':cmTestFtpDownstreamSpeed,'cmTestFtpServerAddressType':cmTestFtpServerAddressType,'cmTestFtpServerAddress':cmTestFtpServerAddress,'cmTestFtpServerPort':cmTestFtpServerPort,'cmTestFtpUserName':cmTestFtpUserName,'cmTestFtpPassword':cmTestFtpPassword,'cmTestFtpFilename':cmTestFtpFilename,'cmTestFtpCommand':cmTestFtpCommand,'cmTestFtpTransferStatus':cmTestFtpTransferStatus,'cmTestFtpTransferPayloadBytes':cmTestFtpTransferPayloadBytes,'cmTestFtpTransferTotalBytes':cmTestFtpTransferTotalBytes,'cmTestFtpTransferElapsedTime':cmTestFtpTransferElapsedTime,'cmTestFtpTransferThroughput':cmTestFtpTransferThroughput,'cmTestFtpUpstreamSpeed':cmTestFtpUpstreamSpeed,'cmTestFtpUpstreamServerAddressType':cmTestFtpUpstreamServerAddressType,'cmTestFtpUpstreamServerAddress':cmTestFtpUpstreamServerAddress,'cmTestFtpUpstreamServerPort':cmTestFtpUpstreamServerPort,'cmTestFtpUpstreamUserName':cmTestFtpUpstreamUserName,'cmTestFtpUpstreamPassword':cmTestFtpUpstreamPassword,'cmTestFtpUpstreamFilename':cmTestFtpUpstreamFilename,'cmTestFtpUpstreamFileSize':cmTestFtpUpstreamFileSize,'cmTestFtpUpstreamCommand':cmTestFtpUpstreamCommand,'cmTestFtpUpstreamTransferStatus':cmTestFtpUpstreamTransferStatus,'cmTestFtpUpstreamTransferPayloadBytes':cmTestFtpUpstreamTransferPayloadBytes,'cmTestFtpUpstreamTransferTotalBytes':cmTestFtpUpstreamTransferTotalBytes,'cmTestFtpUpstreamTransferElapsedTime':cmTestFtpUpstreamTransferElapsedTime,'cmTestFtpUpstreamTransferThroughput':cmTestFtpUpstreamTransferThroughput})