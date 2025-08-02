_F='slFtTftpStatus'
_E='SL-FT-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ifAlias,ifIndex=mibBuilder.importSymbols('IF-MIB','ifAlias','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp','TruthValue')
slFt=ModuleIdentity((1,3,6,1,4,1,4515,1,3,30))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class SftpUserLogin(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
class SftpUserPassword(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_SlFtGen_ObjectIdentity=ObjectIdentity
slFtGen=_SlFtGen_ObjectIdentity((1,3,6,1,4,1,4515,1,3,30,1))
_SlFtSystems_ObjectIdentity=ObjectIdentity
slFtSystems=_SlFtSystems_ObjectIdentity((1,3,6,1,4,1,4515,1,3,30,1,1))
_SlFtSystemsEvents_ObjectIdentity=ObjectIdentity
slFtSystemsEvents=_SlFtSystemsEvents_ObjectIdentity((1,3,6,1,4,1,4515,1,3,30,1,1,0))
if mibBuilder.loadTexts:slFtSystemsEvents.setStatus(_A)
_SlFtAgnt_ObjectIdentity=ObjectIdentity
slFtAgnt=_SlFtAgnt_ObjectIdentity((1,3,6,1,4,1,4515,1,3,30,1,2))
_SlFtFileTransfer_ObjectIdentity=ObjectIdentity
slFtFileTransfer=_SlFtFileTransfer_ObjectIdentity((1,3,6,1,4,1,4515,1,3,30,1,2,12))
_SlFtFileServerIP_Type=IpAddress
_SlFtFileServerIP_Object=MibScalar
slFtFileServerIP=_SlFtFileServerIP_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,1),_SlFtFileServerIP_Type())
slFtFileServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtFileServerIP.setStatus(_A)
_SlFtFileName_Type=DisplayString
_SlFtFileName_Object=MibScalar
slFtFileName=_SlFtFileName_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,2),_SlFtFileName_Type())
slFtFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtFileName.setStatus(_A)
class _SlFtFileTransCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,38,255)));namedValues=NamedValues(*(('swDwnLoad',1),('configDwnLoad',2),('configUpLoad',3),('coProcDwnLoad',4),('stateUpLoad',5),('dwnLoadUserFile',6),('upLoadUserFile',7),('swDwnLoadAndReset',8),('swUpLoad',9),('swDwnLoad2BkupStorage',10),('bootDwnLoad',11),('bootUpLoad',12),('swUpLoadFromBkupStorage',13),('licenseDwnLoad',14),('configDwnLoadToDefaultFile',15),('osaUpLoad1',21),('osaUpLoad2',22),('osaUpLoad3',23),('osaUpLoad4',24),('osaUpLoad5',25),('osaUpLoad6',26),('osaUpLoad7',27),('osaUpLoad8',28),('otdrUpLoad1',31),('otdrUpLoad2',32),('otdrUpLoad3',33),('otdrUpLoad4',34),('otdrUpLoad5',35),('otdrUpLoad6',36),('otdrUpLoad7',37),('otdrUpLoad8',38),('noOp',255)))
_SlFtFileTransCmd_Type.__name__=_C
_SlFtFileTransCmd_Object=MibScalar
slFtFileTransCmd=_SlFtFileTransCmd_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,3),_SlFtFileTransCmd_Type())
slFtFileTransCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtFileTransCmd.setStatus(_A)
_SlFtTftpRetryTimeOut_Type=Integer32
_SlFtTftpRetryTimeOut_Object=MibScalar
slFtTftpRetryTimeOut=_SlFtTftpRetryTimeOut_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,4),_SlFtTftpRetryTimeOut_Type())
slFtTftpRetryTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtTftpRetryTimeOut.setStatus(_A)
_SlFtTftpTotalTimeOut_Type=Integer32
_SlFtTftpTotalTimeOut_Object=MibScalar
slFtTftpTotalTimeOut=_SlFtTftpTotalTimeOut_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,5),_SlFtTftpTotalTimeOut_Type())
slFtTftpTotalTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtTftpTotalTimeOut.setStatus(_A)
class _SlFtTftpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*(('noOp',2),('connecting',3),('transferringData',4),('endedTimeOut',5),('endedOk',6),('error',7)))
_SlFtTftpStatus_Type.__name__=_C
_SlFtTftpStatus_Object=MibScalar
slFtTftpStatus=_SlFtTftpStatus_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,6),_SlFtTftpStatus_Type())
slFtTftpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtTftpStatus.setStatus(_A)
class _SlFtTftpError_Type(OctetString):defaultHexValue='0000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SlFtTftpError_Type.__name__=_D
_SlFtTftpError_Object=MibScalar
slFtTftpError=_SlFtTftpError_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,7),_SlFtTftpError_Type())
slFtTftpError.setMaxAccess('read-only')
if mibBuilder.loadTexts:slFtTftpError.setStatus(_A)
class _SlFtFileTransferToSubSystems_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_SlFtFileTransferToSubSystems_Type.__name__=_D
_SlFtFileTransferToSubSystems_Object=MibScalar
slFtFileTransferToSubSystems=_SlFtFileTransferToSubSystems_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,8),_SlFtFileTransferToSubSystems_Type())
slFtFileTransferToSubSystems.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtFileTransferToSubSystems.setStatus(_A)
_SlFtFileNameWithinProduct_Type=DisplayString
_SlFtFileNameWithinProduct_Object=MibScalar
slFtFileNameWithinProduct=_SlFtFileNameWithinProduct_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,9),_SlFtFileNameWithinProduct_Type())
slFtFileNameWithinProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtFileNameWithinProduct.setStatus(_A)
_SlFtFileTransferServerPort_Type=Unsigned32
_SlFtFileTransferServerPort_Object=MibScalar
slFtFileTransferServerPort=_SlFtFileTransferServerPort_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,14),_SlFtFileTransferServerPort_Type())
slFtFileTransferServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtFileTransferServerPort.setStatus(_A)
class _SlFtFileTransferProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tftp',1),('sftp',2)))
_SlFtFileTransferProtocol_Type.__name__=_C
_SlFtFileTransferProtocol_Object=MibScalar
slFtFileTransferProtocol=_SlFtFileTransferProtocol_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,15),_SlFtFileTransferProtocol_Type())
slFtFileTransferProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtFileTransferProtocol.setStatus(_A)
_SlFtSftpUserLogin_Type=SftpUserLogin
_SlFtSftpUserLogin_Object=MibScalar
slFtSftpUserLogin=_SlFtSftpUserLogin_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,16),_SlFtSftpUserLogin_Type())
slFtSftpUserLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtSftpUserLogin.setStatus(_A)
_SlFtSftpPasswordLogin_Type=SftpUserPassword
_SlFtSftpPasswordLogin_Object=MibScalar
slFtSftpPasswordLogin=_SlFtSftpPasswordLogin_Object((1,3,6,1,4,1,4515,1,3,30,1,2,12,17),_SlFtSftpPasswordLogin_Type())
slFtSftpPasswordLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtSftpPasswordLogin.setStatus(_A)
class _SlFtSystemReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('off',2),('on',3),('resetConfig',4),('resetMapping',5),('resetStandby',6)))
_SlFtSystemReset_Type.__name__=_C
_SlFtSystemReset_Object=MibScalar
slFtSystemReset=_SlFtSystemReset_Object((1,3,6,1,4,1,4515,1,3,30,1,2,13),_SlFtSystemReset_Type())
slFtSystemReset.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtSystemReset.setStatus(_A)
class _SlFtAgnSwVersionSwapCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('off',2),('mainAndBackup',3)))
_SlFtAgnSwVersionSwapCmd_Type.__name__=_C
_SlFtAgnSwVersionSwapCmd_Object=MibScalar
slFtAgnSwVersionSwapCmd=_SlFtAgnSwVersionSwapCmd_Object((1,3,6,1,4,1,4515,1,3,30,1,2,51),_SlFtAgnSwVersionSwapCmd_Type())
slFtAgnSwVersionSwapCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:slFtAgnSwVersionSwapCmd.setStatus(_A)
slFtTftpStatusChangeTrap=NotificationType((1,3,6,1,4,1,4515,1,3,30,1,1,0,1))
slFtTftpStatusChangeTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:slFtTftpStatusChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'SftpUserLogin':SftpUserLogin,'SftpUserPassword':SftpUserPassword,'slFt':slFt,'slFtGen':slFtGen,'slFtSystems':slFtSystems,'slFtSystemsEvents':slFtSystemsEvents,'slFtTftpStatusChangeTrap':slFtTftpStatusChangeTrap,'slFtAgnt':slFtAgnt,'slFtFileTransfer':slFtFileTransfer,'slFtFileServerIP':slFtFileServerIP,'slFtFileName':slFtFileName,'slFtFileTransCmd':slFtFileTransCmd,'slFtTftpRetryTimeOut':slFtTftpRetryTimeOut,'slFtTftpTotalTimeOut':slFtTftpTotalTimeOut,_F:slFtTftpStatus,'slFtTftpError':slFtTftpError,'slFtFileTransferToSubSystems':slFtFileTransferToSubSystems,'slFtFileNameWithinProduct':slFtFileNameWithinProduct,'slFtFileTransferServerPort':slFtFileTransferServerPort,'slFtFileTransferProtocol':slFtFileTransferProtocol,'slFtSftpUserLogin':slFtSftpUserLogin,'slFtSftpPasswordLogin':slFtSftpPasswordLogin,'slFtSystemReset':slFtSystemReset,'slFtAgnSwVersionSwapCmd':slFtAgnSwVersionSwapCmd})