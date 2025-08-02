_H='securityCertificatesVer1'
_G='certificateExpirationDate'
_F='certificateSubjectCommonName'
_E='certificateName'
_D='read-only'
_C='OctetString'
_B='MX-SECURITY-CERTIFICATES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixMgmt,=mibBuilder.importSymbols('MX-SMI','mediatrixMgmt')
MxEnableState,=mibBuilder.importSymbols('MX-TC','MxEnableState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
securityCertificatesMIB=ModuleIdentity((1,3,6,1,4,1,4935,10,200))
if mibBuilder.loadTexts:securityCertificatesMIB.setRevisions(('2005-04-21 00:00',))
_SecurityCertificatesMIBObjects_ObjectIdentity=ObjectIdentity
securityCertificatesMIBObjects=_SecurityCertificatesMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,10,200,1))
_CertificateTable_Object=MibTable
certificateTable=_CertificateTable_Object((1,3,6,1,4,1,4935,10,200,1,500))
if mibBuilder.loadTexts:certificateTable.setStatus(_A)
_CertificateEntry_Object=MibTableRow
certificateEntry=_CertificateEntry_Object((1,3,6,1,4,1,4935,10,200,1,500,50))
certificateEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:certificateEntry.setStatus(_A)
class _CertificateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_CertificateName_Type.__name__=_C
_CertificateName_Object=MibTableColumn
certificateName=_CertificateName_Object((1,3,6,1,4,1,4935,10,200,1,500,50,50),_CertificateName_Type())
certificateName.setMaxAccess(_D)
if mibBuilder.loadTexts:certificateName.setStatus(_A)
class _CertificateSubjectCommonName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CertificateSubjectCommonName_Type.__name__=_C
_CertificateSubjectCommonName_Object=MibTableColumn
certificateSubjectCommonName=_CertificateSubjectCommonName_Object((1,3,6,1,4,1,4935,10,200,1,500,50,100),_CertificateSubjectCommonName_Type())
certificateSubjectCommonName.setMaxAccess(_D)
if mibBuilder.loadTexts:certificateSubjectCommonName.setStatus(_A)
class _CertificateExpirationDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_CertificateExpirationDate_Type.__name__=_C
_CertificateExpirationDate_Object=MibTableColumn
certificateExpirationDate=_CertificateExpirationDate_Object((1,3,6,1,4,1,4935,10,200,1,500,50,150),_CertificateExpirationDate_Type())
certificateExpirationDate.setMaxAccess(_D)
if mibBuilder.loadTexts:certificateExpirationDate.setStatus(_A)
_SecurityCertificatesConformance_ObjectIdentity=ObjectIdentity
securityCertificatesConformance=_SecurityCertificatesConformance_ObjectIdentity((1,3,6,1,4,1,4935,10,200,5))
_SecurityCertificatesCompliances_ObjectIdentity=ObjectIdentity
securityCertificatesCompliances=_SecurityCertificatesCompliances_ObjectIdentity((1,3,6,1,4,1,4935,10,200,5,1))
_SecurityCertificatesGroups_ObjectIdentity=ObjectIdentity
securityCertificatesGroups=_SecurityCertificatesGroups_ObjectIdentity((1,3,6,1,4,1,4935,10,200,5,5))
securityCertificatesVer1=ObjectGroup((1,3,6,1,4,1,4935,10,200,5,5,10))
securityCertificatesVer1.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:securityCertificatesVer1.setStatus(_A)
securityCertificatesComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,10,200,5,1,1))
securityCertificatesComplVer1.setObjects((_B,_H))
if mibBuilder.loadTexts:securityCertificatesComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'securityCertificatesMIB':securityCertificatesMIB,'securityCertificatesMIBObjects':securityCertificatesMIBObjects,'certificateTable':certificateTable,'certificateEntry':certificateEntry,_E:certificateName,_F:certificateSubjectCommonName,_G:certificateExpirationDate,'securityCertificatesConformance':securityCertificatesConformance,'securityCertificatesCompliances':securityCertificatesCompliances,'securityCertificatesComplVer1':securityCertificatesComplVer1,'securityCertificatesGroups':securityCertificatesGroups,_H:securityCertificatesVer1})