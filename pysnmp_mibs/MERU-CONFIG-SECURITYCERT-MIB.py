_D='read-only'
_C='read-write'
_B='current'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_A,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigSecurityCert=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,10))
_MwSslCertInput_ObjectIdentity=ObjectIdentity
mwSslCertInput=_MwSslCertInput_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,10,2))
class _MwSslCertInputCertificateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MwSslCertInputCertificateName_Type.__name__=_A
_MwSslCertInputCertificateName_Object=MibScalar
mwSslCertInputCertificateName=_MwSslCertInputCertificateName_Object((1,3,6,1,4,1,15983,1,1,4,10,2,1),_MwSslCertInputCertificateName_Type())
mwSslCertInputCertificateName.setMaxAccess(_C)
if mibBuilder.loadTexts:mwSslCertInputCertificateName.setStatus(_B)
class _MwSslCertInputPfxPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwSslCertInputPfxPassword_Type.__name__=_A
_MwSslCertInputPfxPassword_Object=MibScalar
mwSslCertInputPfxPassword=_MwSslCertInputPfxPassword_Object((1,3,6,1,4,1,15983,1,1,4,10,2,2),_MwSslCertInputPfxPassword_Type())
mwSslCertInputPfxPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:mwSslCertInputPfxPassword.setStatus(_B)
_MwSslCert_ObjectIdentity=ObjectIdentity
mwSslCert=_MwSslCert_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,10,3))
class _MwSslCertCertificateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MwSslCertCertificateName_Type.__name__=_A
_MwSslCertCertificateName_Object=MibScalar
mwSslCertCertificateName=_MwSslCertCertificateName_Object((1,3,6,1,4,1,15983,1,1,4,10,3,1),_MwSslCertCertificateName_Type())
mwSslCertCertificateName.setMaxAccess(_D)
if mibBuilder.loadTexts:mwSslCertCertificateName.setStatus(_B)
_MwSslCertCertFormattedText_Type=DisplayString
_MwSslCertCertFormattedText_Object=MibScalar
mwSslCertCertFormattedText=_MwSslCertCertFormattedText_Object((1,3,6,1,4,1,15983,1,1,4,10,3,2),_MwSslCertCertFormattedText_Type())
mwSslCertCertFormattedText.setMaxAccess(_D)
if mibBuilder.loadTexts:mwSslCertCertFormattedText.setStatus(_B)
mibBuilder.exportSymbols('MERU-CONFIG-SECURITYCERT-MIB',**{'mwConfigSecurityCert':mwConfigSecurityCert,'mwSslCertInput':mwSslCertInput,'mwSslCertInputCertificateName':mwSslCertInputCertificateName,'mwSslCertInputPfxPassword':mwSslCertInputPfxPassword,'mwSslCert':mwSslCert,'mwSslCertCertificateName':mwSslCertCertificateName,'mwSslCertCertFormattedText':mwSslCertCertFormattedText})