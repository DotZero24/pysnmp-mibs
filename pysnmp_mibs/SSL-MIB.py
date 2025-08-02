_E='Unsigned32'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
swSSLMIB=ModuleIdentity((1,3,6,1,4,1,171,12,7))
_SwSSLMgmt_ObjectIdentity=ObjectIdentity
swSSLMgmt=_SwSSLMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,7,1))
class _SwSSLStatusAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('disabled',2),('enabled',3)))
_SwSSLStatusAdmin_Type.__name__=_C
_SwSSLStatusAdmin_Object=MibScalar
swSSLStatusAdmin=_SwSSLStatusAdmin_Object((1,3,6,1,4,1,171,12,7,1,1),_SwSSLStatusAdmin_Type())
swSSLStatusAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:swSSLStatusAdmin.setStatus(_A)
class _SwSSLCipherSuites_Type(Bits):namedValues=NamedValues(*(('rsa-with-rc4-128-MD5',0),('rsa-with-3des-ede-cbc-sha',1),('dhe-dss-with-3des-ede-cbc-sha',2),('rsa-export-with-rc4-40-md5',3)))
_SwSSLCipherSuites_Type.__name__='Bits'
_SwSSLCipherSuites_Object=MibScalar
swSSLCipherSuites=_SwSSLCipherSuites_Object((1,3,6,1,4,1,171,12,7,1,2),_SwSSLCipherSuites_Type())
swSSLCipherSuites.setMaxAccess(_B)
if mibBuilder.loadTexts:swSSLCipherSuites.setStatus(_A)
class _SwSSLCacheTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_SwSSLCacheTimeout_Type.__name__=_E
_SwSSLCacheTimeout_Object=MibScalar
swSSLCacheTimeout=_SwSSLCacheTimeout_Object((1,3,6,1,4,1,171,12,7,1,3),_SwSSLCacheTimeout_Type())
swSSLCacheTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:swSSLCacheTimeout.setStatus(_A)
_SwSSLCertificateFile_ObjectIdentity=ObjectIdentity
swSSLCertificateFile=_SwSSLCertificateFile_ObjectIdentity((1,3,6,1,4,1,171,12,7,2))
_SwSSLCertificateFileIPAddr_Type=IpAddress
_SwSSLCertificateFileIPAddr_Object=MibScalar
swSSLCertificateFileIPAddr=_SwSSLCertificateFileIPAddr_Object((1,3,6,1,4,1,171,12,7,2,1),_SwSSLCertificateFileIPAddr_Type())
swSSLCertificateFileIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swSSLCertificateFileIPAddr.setStatus(_A)
class _SwSSLCertificateFilePath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSSLCertificateFilePath_Type.__name__=_D
_SwSSLCertificateFilePath_Object=MibScalar
swSSLCertificateFilePath=_SwSSLCertificateFilePath_Object((1,3,6,1,4,1,171,12,7,2,2),_SwSSLCertificateFilePath_Type())
swSSLCertificateFilePath.setMaxAccess(_B)
if mibBuilder.loadTexts:swSSLCertificateFilePath.setStatus(_A)
class _SwSSLCertificateKeyFilePath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSSLCertificateKeyFilePath_Type.__name__=_D
_SwSSLCertificateKeyFilePath_Object=MibScalar
swSSLCertificateKeyFilePath=_SwSSLCertificateKeyFilePath_Object((1,3,6,1,4,1,171,12,7,2,3),_SwSSLCertificateKeyFilePath_Type())
swSSLCertificateKeyFilePath.setMaxAccess(_B)
if mibBuilder.loadTexts:swSSLCertificateKeyFilePath.setStatus(_A)
class _SwSSLCertificateFileCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('inactive',2),('start',3),('delete',4)))
_SwSSLCertificateFileCtrl_Type.__name__=_C
_SwSSLCertificateFileCtrl_Object=MibScalar
swSSLCertificateFileCtrl=_SwSSLCertificateFileCtrl_Object((1,3,6,1,4,1,171,12,7,2,4),_SwSSLCertificateFileCtrl_Type())
swSSLCertificateFileCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swSSLCertificateFileCtrl.setStatus(_A)
class _SwSSLCertificateFileShowSatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('rsa',2),('dsa',3)))
_SwSSLCertificateFileShowSatus_Type.__name__=_C
_SwSSLCertificateFileShowSatus_Object=MibScalar
swSSLCertificateFileShowSatus=_SwSSLCertificateFileShowSatus_Object((1,3,6,1,4,1,171,12,7,2,5),_SwSSLCertificateFileShowSatus_Type())
swSSLCertificateFileShowSatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:swSSLCertificateFileShowSatus.setStatus(_A)
mibBuilder.exportSymbols('SSL-MIB',**{'swSSLMIB':swSSLMIB,'swSSLMgmt':swSSLMgmt,'swSSLStatusAdmin':swSSLStatusAdmin,'swSSLCipherSuites':swSSLCipherSuites,'swSSLCacheTimeout':swSSLCacheTimeout,'swSSLCertificateFile':swSSLCertificateFile,'swSSLCertificateFileIPAddr':swSSLCertificateFileIPAddr,'swSSLCertificateFilePath':swSSLCertificateFilePath,'swSSLCertificateKeyFilePath':swSSLCertificateKeyFilePath,'swSSLCertificateFileCtrl':swSSLCertificateFileCtrl,'swSSLCertificateFileShowSatus':swSSLCertificateFileShowSatus})