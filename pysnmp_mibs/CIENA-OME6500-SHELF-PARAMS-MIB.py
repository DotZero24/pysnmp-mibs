_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaOme6500,=mibBuilder.importSymbols('CIENA-OME6500-OPTICAL-MIB','cienaOme6500')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaOme6500ShelfParams=ModuleIdentity((1,3,6,1,4,1,1271,68,11,1))
if mibBuilder.loadTexts:cienaOme6500ShelfParams.setRevisions(('2015-06-30 00:00',))
class ErrorCodes(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65)));namedValues=NamedValues(*(('eNil',0),('eMSG-SENT',1),('ePRTL',2),('eCOMPLD',3),('eDENY',4),('eENEQ',5),('eENEX',6),('eENPS',7),('eIBEX',8),('eIBMS',9),('eICNV',10),('eIDNV',11),('eIDRG',12),('eIEAE',13),('eIENE',14),('eIIAC',15),('eIICT',16),('eIIPG',17),('eIITA',18),('eINUP',19),('eIPEX',20),('eIPMS',21),('eIPNV',22),('ePICC',23),('ePIUC',24),('ePIUI',25),('ePLNA',26),('eSAAL',27),('eSAAS',28),('eSABT',29),('eSAIN',30),('eSAIS',31),('eSAMS',32),('eSANP',33),('eSAOP',34),('eSAPR',35),('eSARB',36),('eSARL',37),('eSDNC',38),('eSDNR',39),('eSLEM',40),('eSNSR',41),('eSNVS',42),('eSPFA',43),('eSPLD',44),('eSPUA',45),('eSRCI',46),('eSROF',47),('eSSRD',48),('eSSRE',49),('eSSTP',50),('eSWFA',51),('eSWLD',52),('eSRPR',53),('eEQWT',54),('eICNS',55),('eODNV',56),('eIATA',57),('eICNI',58),('eTL1SNA',59),('eMERR',60),('eSFTPC-OK',61),('eSFTPC-ERR',62),('eLOST',63),('eCANC',64),('eMAX',65)))
_CienaOme6500ShelfParamsProv_ObjectIdentity=ObjectIdentity
cienaOme6500ShelfParamsProv=_CienaOme6500ShelfParamsProv_ObjectIdentity((1,3,6,1,4,1,1271,68,11,1,1))
class _Ome6500ShelfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Ome6500ShelfId_Type.__name__=_C
_Ome6500ShelfId_Object=MibScalar
ome6500ShelfId=_Ome6500ShelfId_Object((1,3,6,1,4,1,1271,68,11,1,1,1),_Ome6500ShelfId_Type())
ome6500ShelfId.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfId.setStatus(_B)
class _Ome6500ShelfSubId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_Ome6500ShelfSubId_Type.__name__=_C
_Ome6500ShelfSubId_Object=MibScalar
ome6500ShelfSubId=_Ome6500ShelfSubId_Object((1,3,6,1,4,1,1271,68,11,1,1,2),_Ome6500ShelfSubId_Type())
ome6500ShelfSubId.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfSubId.setStatus(_B)
_Ome6500ShelfTid_Type=DisplayString
_Ome6500ShelfTid_Object=MibScalar
ome6500ShelfTid=_Ome6500ShelfTid_Object((1,3,6,1,4,1,1271,68,11,1,1,3),_Ome6500ShelfTid_Type())
ome6500ShelfTid.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfTid.setStatus(_B)
_Ome6500ShelfIpAddress_Type=IpAddress
_Ome6500ShelfIpAddress_Object=MibScalar
ome6500ShelfIpAddress=_Ome6500ShelfIpAddress_Object((1,3,6,1,4,1,1271,68,11,1,1,4),_Ome6500ShelfIpAddress_Type())
ome6500ShelfIpAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfIpAddress.setStatus(_B)
_Ome6500ShelfSoftwareVersion_Type=DisplayString
_Ome6500ShelfSoftwareVersion_Object=MibScalar
ome6500ShelfSoftwareVersion=_Ome6500ShelfSoftwareVersion_Object((1,3,6,1,4,1,1271,68,11,1,1,5),_Ome6500ShelfSoftwareVersion_Type())
ome6500ShelfSoftwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfSoftwareVersion.setStatus(_B)
class _Ome6500ShelfSiteId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ome6500ShelfSiteId_Type.__name__=_C
_Ome6500ShelfSiteId_Object=MibScalar
ome6500ShelfSiteId=_Ome6500ShelfSiteId_Object((1,3,6,1,4,1,1271,68,11,1,1,6),_Ome6500ShelfSiteId_Type())
ome6500ShelfSiteId.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfSiteId.setStatus(_B)
_Ome6500ShelfSiteName_Type=DisplayString
_Ome6500ShelfSiteName_Object=MibScalar
ome6500ShelfSiteName=_Ome6500ShelfSiteName_Object((1,3,6,1,4,1,1271,68,11,1,1,7),_Ome6500ShelfSiteName_Type())
ome6500ShelfSiteName.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfSiteName.setStatus(_B)
class _Ome6500ShelfSnmpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1v2c',1),('v1v2cv3',2),('v3',3)))
_Ome6500ShelfSnmpVersion_Type.__name__=_C
_Ome6500ShelfSnmpVersion_Object=MibScalar
ome6500ShelfSnmpVersion=_Ome6500ShelfSnmpVersion_Object((1,3,6,1,4,1,1271,68,11,1,1,8),_Ome6500ShelfSnmpVersion_Type())
ome6500ShelfSnmpVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfSnmpVersion.setStatus(_B)
class _Ome6500shelfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sonet',1),('sdh',2),('jsdh',3)))
_Ome6500shelfMode_Type.__name__=_C
_Ome6500shelfMode_Object=MibScalar
ome6500shelfMode=_Ome6500shelfMode_Object((1,3,6,1,4,1,1271,68,11,1,1,9),_Ome6500shelfMode_Type())
ome6500shelfMode.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500shelfMode.setStatus(_B)
class _Ome6500ShelfIsGne_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_Ome6500ShelfIsGne_Type.__name__=_C
_Ome6500ShelfIsGne_Object=MibScalar
ome6500ShelfIsGne=_Ome6500ShelfIsGne_Object((1,3,6,1,4,1,1271,68,11,1,1,10),_Ome6500ShelfIsGne_Type())
ome6500ShelfIsGne.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfIsGne.setStatus(_B)
_Ome6500ShelfGneIpAddress_Type=IpAddress
_Ome6500ShelfGneIpAddress_Object=MibScalar
ome6500ShelfGneIpAddress=_Ome6500ShelfGneIpAddress_Object((1,3,6,1,4,1,1271,68,11,1,1,11),_Ome6500ShelfGneIpAddress_Type())
ome6500ShelfGneIpAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfGneIpAddress.setStatus(_B)
_Ome6500LastErrorRc_Type=ErrorCodes
_Ome6500LastErrorRc_Object=MibScalar
ome6500LastErrorRc=_Ome6500LastErrorRc_Object((1,3,6,1,4,1,1271,68,11,1,1,12),_Ome6500LastErrorRc_Type())
ome6500LastErrorRc.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500LastErrorRc.setStatus(_B)
_Ome6500LastErrorDescription_Type=DisplayString
_Ome6500LastErrorDescription_Object=MibScalar
ome6500LastErrorDescription=_Ome6500LastErrorDescription_Object((1,3,6,1,4,1,1271,68,11,1,1,13),_Ome6500LastErrorDescription_Type())
ome6500LastErrorDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500LastErrorDescription.setStatus(_B)
_Ome6500ShelfInetAddressType_Type=InetAddressType
_Ome6500ShelfInetAddressType_Object=MibScalar
ome6500ShelfInetAddressType=_Ome6500ShelfInetAddressType_Object((1,3,6,1,4,1,1271,68,11,1,1,14),_Ome6500ShelfInetAddressType_Type())
ome6500ShelfInetAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfInetAddressType.setStatus(_B)
_Ome6500ShelfInetAddress_Type=InetAddress
_Ome6500ShelfInetAddress_Object=MibScalar
ome6500ShelfInetAddress=_Ome6500ShelfInetAddress_Object((1,3,6,1,4,1,1271,68,11,1,1,15),_Ome6500ShelfInetAddress_Type())
ome6500ShelfInetAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfInetAddress.setStatus(_B)
_Ome6500ShelfGneInetAddressType_Type=InetAddressType
_Ome6500ShelfGneInetAddressType_Object=MibScalar
ome6500ShelfGneInetAddressType=_Ome6500ShelfGneInetAddressType_Object((1,3,6,1,4,1,1271,68,11,1,1,16),_Ome6500ShelfGneInetAddressType_Type())
ome6500ShelfGneInetAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfGneInetAddressType.setStatus(_B)
_Ome6500ShelfGneInetAddress_Type=InetAddress
_Ome6500ShelfGneInetAddress_Object=MibScalar
ome6500ShelfGneInetAddress=_Ome6500ShelfGneInetAddress_Object((1,3,6,1,4,1,1271,68,11,1,1,17),_Ome6500ShelfGneInetAddress_Type())
ome6500ShelfGneInetAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:ome6500ShelfGneInetAddress.setStatus(_B)
mibBuilder.exportSymbols('CIENA-OME6500-SHELF-PARAMS-MIB',**{'ErrorCodes':ErrorCodes,'cienaOme6500ShelfParams':cienaOme6500ShelfParams,'cienaOme6500ShelfParamsProv':cienaOme6500ShelfParamsProv,'ome6500ShelfId':ome6500ShelfId,'ome6500ShelfSubId':ome6500ShelfSubId,'ome6500ShelfTid':ome6500ShelfTid,'ome6500ShelfIpAddress':ome6500ShelfIpAddress,'ome6500ShelfSoftwareVersion':ome6500ShelfSoftwareVersion,'ome6500ShelfSiteId':ome6500ShelfSiteId,'ome6500ShelfSiteName':ome6500ShelfSiteName,'ome6500ShelfSnmpVersion':ome6500ShelfSnmpVersion,'ome6500shelfMode':ome6500shelfMode,'ome6500ShelfIsGne':ome6500ShelfIsGne,'ome6500ShelfGneIpAddress':ome6500ShelfGneIpAddress,'ome6500LastErrorRc':ome6500LastErrorRc,'ome6500LastErrorDescription':ome6500LastErrorDescription,'ome6500ShelfInetAddressType':ome6500ShelfInetAddressType,'ome6500ShelfInetAddress':ome6500ShelfInetAddress,'ome6500ShelfGneInetAddressType':ome6500ShelfGneInetAddressType,'ome6500ShelfGneInetAddress':ome6500ShelfGneInetAddress})