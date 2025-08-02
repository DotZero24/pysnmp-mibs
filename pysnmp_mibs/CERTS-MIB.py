_F='certIdx'
_E='CERTS-MIB'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
one4net,=mibBuilder.importSymbols('ONE4NET-MIB','one4net')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
certs=ModuleIdentity((1,3,6,1,4,1,12196,14))
if mibBuilder.loadTexts:certs.setRevisions(('2018-12-07 03:10',))
_CertsTable_Object=MibTable
certsTable=_CertsTable_Object((1,3,6,1,4,1,12196,14,1))
if mibBuilder.loadTexts:certsTable.setStatus(_A)
_CertEntry_Object=MibTableRow
certEntry=_CertEntry_Object((1,3,6,1,4,1,12196,14,1,1))
certEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:certEntry.setStatus(_A)
class _CertIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CertIdx_Type.__name__=_D
_CertIdx_Object=MibTableColumn
certIdx=_CertIdx_Object((1,3,6,1,4,1,12196,14,1,1,1),_CertIdx_Type())
certIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:certIdx.setStatus(_A)
class _CertFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CertFileName_Type.__name__=_C
_CertFileName_Object=MibTableColumn
certFileName=_CertFileName_Object((1,3,6,1,4,1,12196,14,1,1,2),_CertFileName_Type())
certFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:certFileName.setStatus(_A)
class _CertSubjectName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CertSubjectName_Type.__name__=_C
_CertSubjectName_Object=MibTableColumn
certSubjectName=_CertSubjectName_Object((1,3,6,1,4,1,12196,14,1,1,3),_CertSubjectName_Type())
certSubjectName.setMaxAccess(_B)
if mibBuilder.loadTexts:certSubjectName.setStatus(_A)
class _CertSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CertSerialNumber_Type.__name__=_C
_CertSerialNumber_Object=MibTableColumn
certSerialNumber=_CertSerialNumber_Object((1,3,6,1,4,1,12196,14,1,1,4),_CertSerialNumber_Type())
certSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:certSerialNumber.setStatus(_A)
_CertStartDate_Type=DateAndTime
_CertStartDate_Object=MibTableColumn
certStartDate=_CertStartDate_Object((1,3,6,1,4,1,12196,14,1,1,5),_CertStartDate_Type())
certStartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:certStartDate.setStatus(_A)
_CertEndDate_Type=DateAndTime
_CertEndDate_Object=MibTableColumn
certEndDate=_CertEndDate_Object((1,3,6,1,4,1,12196,14,1,1,6),_CertEndDate_Type())
certEndDate.setMaxAccess(_B)
if mibBuilder.loadTexts:certEndDate.setStatus(_A)
class _CertIssuer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CertIssuer_Type.__name__=_C
_CertIssuer_Object=MibTableColumn
certIssuer=_CertIssuer_Object((1,3,6,1,4,1,12196,14,1,1,7),_CertIssuer_Type())
certIssuer.setMaxAccess(_B)
if mibBuilder.loadTexts:certIssuer.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'certs':certs,'certsTable':certsTable,'certEntry':certEntry,_F:certIdx,'certFileName':certFileName,'certSubjectName':certSubjectName,'certSerialNumber':certSerialNumber,'certStartDate':certStartDate,'certEndDate':certEndDate,'certIssuer':certIssuer})