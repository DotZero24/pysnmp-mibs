_Q='docsBpi2Ext31CmGroup'
_P='docsBpi2Ext31CodeCoSignerCvcAccessStart'
_O='docsBpi2Ext31CodeCoSignerCodeAccessStart'
_N='docsBpi2Ext31CodeCoSignerOrgName'
_M='docsBpi2Ext31CodeMfgCvcAccessStart'
_L='docsBpi2Ext31CodeMfgCodeAccessStart'
_K='docsBpi2Ext31CodeMfgOrgName'
_J='docsBpi2Ext31CodeUpdateCvcChain'
_I='docsBpi2Ext31CmDeviceManufCert'
_H='docsBpi2Ext31CmDeviceCmCert'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='DateAndTime'
_C='read-only'
_B='DOCS-BPI2EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjDocsis,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjDocsis')
DocsX509ASN1DEREncodedCertificate,=mibBuilder.importSymbols('DOCS-IETF-BPI2-MIB','DocsX509ASN1DEREncodedCertificate')
ifIndex,=mibBuilder.importSymbols(_E,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'DisplayString','PhysAddress','TextualConvention')
docsBpi2Ext31Mib=ModuleIdentity((1,3,6,1,4,1,4491,2,1,29))
if mibBuilder.loadTexts:docsBpi2Ext31Mib.setRevisions(('2016-01-13 00:00',))
class DocsCvcCaCertificateChain(TextualConvention,OctetString):status=_A;displayHint='50x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8192))
_DocsBpi2Ext31Notifications_ObjectIdentity=ObjectIdentity
docsBpi2Ext31Notifications=_DocsBpi2Ext31Notifications_ObjectIdentity((1,3,6,1,4,1,4491,2,1,29,0))
_DocsBpi2Ext31MibObjects_ObjectIdentity=ObjectIdentity
docsBpi2Ext31MibObjects=_DocsBpi2Ext31MibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,29,1))
_DocsBpi2Ext31CmObjects_ObjectIdentity=ObjectIdentity
docsBpi2Ext31CmObjects=_DocsBpi2Ext31CmObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,29,1,1))
_DocsBpi2Ext31CmCertObjects_ObjectIdentity=ObjectIdentity
docsBpi2Ext31CmCertObjects=_DocsBpi2Ext31CmCertObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,29,1,1,1))
_DocsBpi2Ext31CmDeviceCertTable_Object=MibTable
docsBpi2Ext31CmDeviceCertTable=_DocsBpi2Ext31CmDeviceCertTable_Object((1,3,6,1,4,1,4491,2,1,29,1,1,1,1))
if mibBuilder.loadTexts:docsBpi2Ext31CmDeviceCertTable.setStatus(_A)
_DocsBpi2Ext31CmDeviceCertEntry_Object=MibTableRow
docsBpi2Ext31CmDeviceCertEntry=_DocsBpi2Ext31CmDeviceCertEntry_Object((1,3,6,1,4,1,4491,2,1,29,1,1,1,1,1))
docsBpi2Ext31CmDeviceCertEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:docsBpi2Ext31CmDeviceCertEntry.setStatus(_A)
_DocsBpi2Ext31CmDeviceCmCert_Type=DocsX509ASN1DEREncodedCertificate
_DocsBpi2Ext31CmDeviceCmCert_Object=MibTableColumn
docsBpi2Ext31CmDeviceCmCert=_DocsBpi2Ext31CmDeviceCmCert_Object((1,3,6,1,4,1,4491,2,1,29,1,1,1,1,1,1),_DocsBpi2Ext31CmDeviceCmCert_Type())
docsBpi2Ext31CmDeviceCmCert.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpi2Ext31CmDeviceCmCert.setStatus(_A)
_DocsBpi2Ext31CmDeviceManufCert_Type=DocsX509ASN1DEREncodedCertificate
_DocsBpi2Ext31CmDeviceManufCert_Object=MibTableColumn
docsBpi2Ext31CmDeviceManufCert=_DocsBpi2Ext31CmDeviceManufCert_Object((1,3,6,1,4,1,4491,2,1,29,1,1,1,1,1,2),_DocsBpi2Ext31CmDeviceManufCert_Type())
docsBpi2Ext31CmDeviceManufCert.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpi2Ext31CmDeviceManufCert.setStatus(_A)
_DocsBpi2Ext31CodeDownloadControl_ObjectIdentity=ObjectIdentity
docsBpi2Ext31CodeDownloadControl=_DocsBpi2Ext31CodeDownloadControl_ObjectIdentity((1,3,6,1,4,1,4491,2,1,29,1,2))
_DocsBpi2Ext31CodeUpdateCvcChain_Type=DocsCvcCaCertificateChain
_DocsBpi2Ext31CodeUpdateCvcChain_Object=MibScalar
docsBpi2Ext31CodeUpdateCvcChain=_DocsBpi2Ext31CodeUpdateCvcChain_Object((1,3,6,1,4,1,4491,2,1,29,1,2,1),_DocsBpi2Ext31CodeUpdateCvcChain_Type())
docsBpi2Ext31CodeUpdateCvcChain.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpi2Ext31CodeUpdateCvcChain.setStatus(_A)
_DocsBpi2Ext31CodeMfgOrgName_Type=SnmpAdminString
_DocsBpi2Ext31CodeMfgOrgName_Object=MibScalar
docsBpi2Ext31CodeMfgOrgName=_DocsBpi2Ext31CodeMfgOrgName_Object((1,3,6,1,4,1,4491,2,1,29,1,2,2),_DocsBpi2Ext31CodeMfgOrgName_Type())
docsBpi2Ext31CodeMfgOrgName.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpi2Ext31CodeMfgOrgName.setStatus(_A)
class _DocsBpi2Ext31CodeMfgCodeAccessStart_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_DocsBpi2Ext31CodeMfgCodeAccessStart_Type.__name__=_D
_DocsBpi2Ext31CodeMfgCodeAccessStart_Object=MibScalar
docsBpi2Ext31CodeMfgCodeAccessStart=_DocsBpi2Ext31CodeMfgCodeAccessStart_Object((1,3,6,1,4,1,4491,2,1,29,1,2,3),_DocsBpi2Ext31CodeMfgCodeAccessStart_Type())
docsBpi2Ext31CodeMfgCodeAccessStart.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpi2Ext31CodeMfgCodeAccessStart.setStatus(_A)
class _DocsBpi2Ext31CodeMfgCvcAccessStart_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_DocsBpi2Ext31CodeMfgCvcAccessStart_Type.__name__=_D
_DocsBpi2Ext31CodeMfgCvcAccessStart_Object=MibScalar
docsBpi2Ext31CodeMfgCvcAccessStart=_DocsBpi2Ext31CodeMfgCvcAccessStart_Object((1,3,6,1,4,1,4491,2,1,29,1,2,4),_DocsBpi2Ext31CodeMfgCvcAccessStart_Type())
docsBpi2Ext31CodeMfgCvcAccessStart.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpi2Ext31CodeMfgCvcAccessStart.setStatus(_A)
_DocsBpi2Ext31CodeCoSignerOrgName_Type=SnmpAdminString
_DocsBpi2Ext31CodeCoSignerOrgName_Object=MibScalar
docsBpi2Ext31CodeCoSignerOrgName=_DocsBpi2Ext31CodeCoSignerOrgName_Object((1,3,6,1,4,1,4491,2,1,29,1,2,5),_DocsBpi2Ext31CodeCoSignerOrgName_Type())
docsBpi2Ext31CodeCoSignerOrgName.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpi2Ext31CodeCoSignerOrgName.setStatus(_A)
class _DocsBpi2Ext31CodeCoSignerCodeAccessStart_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_DocsBpi2Ext31CodeCoSignerCodeAccessStart_Type.__name__=_D
_DocsBpi2Ext31CodeCoSignerCodeAccessStart_Object=MibScalar
docsBpi2Ext31CodeCoSignerCodeAccessStart=_DocsBpi2Ext31CodeCoSignerCodeAccessStart_Object((1,3,6,1,4,1,4491,2,1,29,1,2,6),_DocsBpi2Ext31CodeCoSignerCodeAccessStart_Type())
docsBpi2Ext31CodeCoSignerCodeAccessStart.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpi2Ext31CodeCoSignerCodeAccessStart.setStatus(_A)
class _DocsBpi2Ext31CodeCoSignerCvcAccessStart_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_DocsBpi2Ext31CodeCoSignerCvcAccessStart_Type.__name__=_D
_DocsBpi2Ext31CodeCoSignerCvcAccessStart_Object=MibScalar
docsBpi2Ext31CodeCoSignerCvcAccessStart=_DocsBpi2Ext31CodeCoSignerCvcAccessStart_Object((1,3,6,1,4,1,4491,2,1,29,1,2,7),_DocsBpi2Ext31CodeCoSignerCvcAccessStart_Type())
docsBpi2Ext31CodeCoSignerCvcAccessStart.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpi2Ext31CodeCoSignerCvcAccessStart.setStatus(_A)
_DocsBpi2Ext31Conformance_ObjectIdentity=ObjectIdentity
docsBpi2Ext31Conformance=_DocsBpi2Ext31Conformance_ObjectIdentity((1,3,6,1,4,1,4491,2,1,29,2))
_DocsBpi2Ext31Compliances_ObjectIdentity=ObjectIdentity
docsBpi2Ext31Compliances=_DocsBpi2Ext31Compliances_ObjectIdentity((1,3,6,1,4,1,4491,2,1,29,2,1))
_DocsBpi2Ext31Groups_ObjectIdentity=ObjectIdentity
docsBpi2Ext31Groups=_DocsBpi2Ext31Groups_ObjectIdentity((1,3,6,1,4,1,4491,2,1,29,2,2))
docsBpi2Ext31CmGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,29,2,2,1))
docsBpi2Ext31CmGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:docsBpi2Ext31CmGroup.setStatus(_A)
docsBpi2Ext31MIBCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,1,29,2,1,1))
docsBpi2Ext31MIBCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:docsBpi2Ext31MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DocsCvcCaCertificateChain':DocsCvcCaCertificateChain,'docsBpi2Ext31Mib':docsBpi2Ext31Mib,'docsBpi2Ext31Notifications':docsBpi2Ext31Notifications,'docsBpi2Ext31MibObjects':docsBpi2Ext31MibObjects,'docsBpi2Ext31CmObjects':docsBpi2Ext31CmObjects,'docsBpi2Ext31CmCertObjects':docsBpi2Ext31CmCertObjects,'docsBpi2Ext31CmDeviceCertTable':docsBpi2Ext31CmDeviceCertTable,'docsBpi2Ext31CmDeviceCertEntry':docsBpi2Ext31CmDeviceCertEntry,_H:docsBpi2Ext31CmDeviceCmCert,_I:docsBpi2Ext31CmDeviceManufCert,'docsBpi2Ext31CodeDownloadControl':docsBpi2Ext31CodeDownloadControl,_J:docsBpi2Ext31CodeUpdateCvcChain,_K:docsBpi2Ext31CodeMfgOrgName,_L:docsBpi2Ext31CodeMfgCodeAccessStart,_M:docsBpi2Ext31CodeMfgCvcAccessStart,_N:docsBpi2Ext31CodeCoSignerOrgName,_O:docsBpi2Ext31CodeCoSignerCodeAccessStart,_P:docsBpi2Ext31CodeCoSignerCvcAccessStart,'docsBpi2Ext31Conformance':docsBpi2Ext31Conformance,'docsBpi2Ext31Compliances':docsBpi2Ext31Compliances,'docsBpi2Ext31MIBCompliance':docsBpi2Ext31MIBCompliance,'docsBpi2Ext31Groups':docsBpi2Ext31Groups,_Q:docsBpi2Ext31CmGroup})