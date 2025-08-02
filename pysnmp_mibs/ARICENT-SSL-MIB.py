_D='TruthValue'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
ssl=ModuleIdentity((1,3,6,1,4,1,2076,96))
if mibBuilder.loadTexts:ssl.setRevisions(('2012-09-05 00:00',))
_SslGeneralGroup_ObjectIdentity=ObjectIdentity
sslGeneralGroup=_SslGeneralGroup_ObjectIdentity((1,3,6,1,4,1,2076,96,1))
class _SslSecureHttpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SslSecureHttpStatus_Type.__name__=_C
_SslSecureHttpStatus_Object=MibScalar
sslSecureHttpStatus=_SslSecureHttpStatus_Object((1,3,6,1,4,1,2076,96,1,2),_SslSecureHttpStatus_Type())
sslSecureHttpStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:sslSecureHttpStatus.setStatus(_B)
class _SslPort_Type(Integer32):defaultValue=443;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SslPort_Type.__name__=_C
_SslPort_Object=MibScalar
sslPort=_SslPort_Object((1,3,6,1,4,1,2076,96,1,3),_SslPort_Type())
sslPort.setMaxAccess(_A)
if mibBuilder.loadTexts:sslPort.setStatus(_B)
_SslTrace_Type=Integer32
_SslTrace_Object=MibScalar
sslTrace=_SslTrace_Object((1,3,6,1,4,1,2076,96,1,4),_SslTrace_Type())
sslTrace.setMaxAccess(_A)
if mibBuilder.loadTexts:sslTrace.setStatus(_B)
class _SslVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('ssl3',2),('tls1',3)))
_SslVersion_Type.__name__=_C
_SslVersion_Object=MibScalar
sslVersion=_SslVersion_Object((1,3,6,1,4,1,2076,96,1,5),_SslVersion_Type())
sslVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:sslVersion.setStatus(_B)
_SslCiphers_ObjectIdentity=ObjectIdentity
sslCiphers=_SslCiphers_ObjectIdentity((1,3,6,1,4,1,2076,96,2))
class _SslCipherList_Type(Integer32):defaultValue=8
_SslCipherList_Type.__name__=_C
_SslCipherList_Object=MibScalar
sslCipherList=_SslCipherList_Object((1,3,6,1,4,1,2076,96,2,1),_SslCipherList_Type())
sslCipherList.setMaxAccess(_A)
if mibBuilder.loadTexts:sslCipherList.setStatus(_B)
class _SslDefaultCipherList_Type(TruthValue):defaultValue=2
_SslDefaultCipherList_Type.__name__=_D
_SslDefaultCipherList_Object=MibScalar
sslDefaultCipherList=_SslDefaultCipherList_Object((1,3,6,1,4,1,2076,96,2,2),_SslDefaultCipherList_Type())
sslDefaultCipherList.setMaxAccess(_A)
if mibBuilder.loadTexts:sslDefaultCipherList.setStatus(_B)
mibBuilder.exportSymbols('ARICENT-SSL-MIB',**{'ssl':ssl,'sslGeneralGroup':sslGeneralGroup,'sslSecureHttpStatus':sslSecureHttpStatus,'sslPort':sslPort,'sslTrace':sslTrace,'sslVersion':sslVersion,'sslCiphers':sslCiphers,'sslCipherList':sslCipherList,'sslDefaultCipherList':sslDefaultCipherList})