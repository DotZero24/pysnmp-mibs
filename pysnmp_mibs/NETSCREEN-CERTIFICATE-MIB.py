_G='nsVpnCertCfgIndex'
_F='nsVpnCertDefIndex'
_E='NETSCREEN-CERTIFICATE-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVpn,netscreenVpnMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVpn','netscreenVpnMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
netscreenCertificateMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,7))
if mibBuilder.loadTexts:netscreenCertificateMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-12 00:00','2001-09-28 00:00','2001-05-15 00:00'))
_NsVpnCert_ObjectIdentity=ObjectIdentity
nsVpnCert=_NsVpnCert_ObjectIdentity((1,3,6,1,4,1,3224,4,7))
_NsVpnCertDefTable_Object=MibTable
nsVpnCertDefTable=_NsVpnCertDefTable_Object((1,3,6,1,4,1,3224,4,7,1))
if mibBuilder.loadTexts:nsVpnCertDefTable.setStatus(_A)
_NsVpnCertDefEntry_Object=MibTableRow
nsVpnCertDefEntry=_NsVpnCertDefEntry_Object((1,3,6,1,4,1,3224,4,7,1,1))
nsVpnCertDefEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsVpnCertDefEntry.setStatus(_A)
class _NsVpnCertDefIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnCertDefIndex_Type.__name__=_D
_NsVpnCertDefIndex_Object=MibTableColumn
nsVpnCertDefIndex=_NsVpnCertDefIndex_Object((1,3,6,1,4,1,3224,4,7,1,1,1),_NsVpnCertDefIndex_Type())
nsVpnCertDefIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertDefIndex.setStatus(_A)
class _NsVpnCertDefLdap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnCertDefLdap_Type.__name__=_C
_NsVpnCertDefLdap_Object=MibTableColumn
nsVpnCertDefLdap=_NsVpnCertDefLdap_Object((1,3,6,1,4,1,3224,4,7,1,1,2),_NsVpnCertDefLdap_Type())
nsVpnCertDefLdap.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertDefLdap.setStatus(_A)
class _NsVpnCertDefCrlUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnCertDefCrlUrl_Type.__name__=_C
_NsVpnCertDefCrlUrl_Object=MibTableColumn
nsVpnCertDefCrlUrl=_NsVpnCertDefCrlUrl_Object((1,3,6,1,4,1,3224,4,7,1,1,3),_NsVpnCertDefCrlUrl_Type())
nsVpnCertDefCrlUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertDefCrlUrl.setStatus(_A)
class _NsVpnCertDefRefresh_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnCertDefRefresh_Type.__name__=_C
_NsVpnCertDefRefresh_Object=MibTableColumn
nsVpnCertDefRefresh=_NsVpnCertDefRefresh_Object((1,3,6,1,4,1,3224,4,7,1,1,4),_NsVpnCertDefRefresh_Type())
nsVpnCertDefRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertDefRefresh.setStatus(_A)
class _NsVpnCertDefX509_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('partial',0),('full',1)))
_NsVpnCertDefX509_Type.__name__=_D
_NsVpnCertDefX509_Object=MibTableColumn
nsVpnCertDefX509=_NsVpnCertDefX509_Object((1,3,6,1,4,1,3224,4,7,1,1,5),_NsVpnCertDefX509_Type())
nsVpnCertDefX509.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertDefX509.setStatus(_A)
_NsVpnCertDefVsys_Type=Integer32
_NsVpnCertDefVsys_Object=MibTableColumn
nsVpnCertDefVsys=_NsVpnCertDefVsys_Object((1,3,6,1,4,1,3224,4,7,1,1,6),_NsVpnCertDefVsys_Type())
nsVpnCertDefVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertDefVsys.setStatus(_A)
_NsVpnCertCfgTable_Object=MibTable
nsVpnCertCfgTable=_NsVpnCertCfgTable_Object((1,3,6,1,4,1,3224,4,7,2))
if mibBuilder.loadTexts:nsVpnCertCfgTable.setStatus(_A)
_NsVpnCertCfgEntry_Object=MibTableRow
nsVpnCertCfgEntry=_NsVpnCertCfgEntry_Object((1,3,6,1,4,1,3224,4,7,2,1))
nsVpnCertCfgEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:nsVpnCertCfgEntry.setStatus(_A)
class _NsVpnCertCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnCertCfgIndex_Type.__name__=_D
_NsVpnCertCfgIndex_Object=MibTableColumn
nsVpnCertCfgIndex=_NsVpnCertCfgIndex_Object((1,3,6,1,4,1,3224,4,7,2,1,1),_NsVpnCertCfgIndex_Type())
nsVpnCertCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertCfgIndex.setStatus(_A)
class _NsVpnCertCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ca',0),('local',1)))
_NsVpnCertCfgType_Type.__name__=_D
_NsVpnCertCfgType_Object=MibTableColumn
nsVpnCertCfgType=_NsVpnCertCfgType_Object((1,3,6,1,4,1,3224,4,7,2,1,2),_NsVpnCertCfgType_Type())
nsVpnCertCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertCfgType.setStatus(_A)
class _NsVpnCertCfgSubject_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsVpnCertCfgSubject_Type.__name__=_C
_NsVpnCertCfgSubject_Object=MibTableColumn
nsVpnCertCfgSubject=_NsVpnCertCfgSubject_Object((1,3,6,1,4,1,3224,4,7,2,1,3),_NsVpnCertCfgSubject_Type())
nsVpnCertCfgSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertCfgSubject.setStatus(_A)
class _NsVpnCertCfgExpire_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnCertCfgExpire_Type.__name__=_C
_NsVpnCertCfgExpire_Object=MibTableColumn
nsVpnCertCfgExpire=_NsVpnCertCfgExpire_Object((1,3,6,1,4,1,3224,4,7,2,1,4),_NsVpnCertCfgExpire_Type())
nsVpnCertCfgExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertCfgExpire.setStatus(_A)
class _NsVpnCertCfgIssuer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NsVpnCertCfgIssuer_Type.__name__=_C
_NsVpnCertCfgIssuer_Object=MibTableColumn
nsVpnCertCfgIssuer=_NsVpnCertCfgIssuer_Object((1,3,6,1,4,1,3224,4,7,2,1,5),_NsVpnCertCfgIssuer_Type())
nsVpnCertCfgIssuer.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertCfgIssuer.setStatus(_A)
_NsVpnCertCfgVsys_Type=Integer32
_NsVpnCertCfgVsys_Object=MibTableColumn
nsVpnCertCfgVsys=_NsVpnCertCfgVsys_Object((1,3,6,1,4,1,3224,4,7,2,1,6),_NsVpnCertCfgVsys_Type())
nsVpnCertCfgVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnCertCfgVsys.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenCertificateMibModule':netscreenCertificateMibModule,'nsVpnCert':nsVpnCert,'nsVpnCertDefTable':nsVpnCertDefTable,'nsVpnCertDefEntry':nsVpnCertDefEntry,_F:nsVpnCertDefIndex,'nsVpnCertDefLdap':nsVpnCertDefLdap,'nsVpnCertDefCrlUrl':nsVpnCertDefCrlUrl,'nsVpnCertDefRefresh':nsVpnCertDefRefresh,'nsVpnCertDefX509':nsVpnCertDefX509,'nsVpnCertDefVsys':nsVpnCertDefVsys,'nsVpnCertCfgTable':nsVpnCertCfgTable,'nsVpnCertCfgEntry':nsVpnCertCfgEntry,_G:nsVpnCertCfgIndex,'nsVpnCertCfgType':nsVpnCertCfgType,'nsVpnCertCfgSubject':nsVpnCertCfgSubject,'nsVpnCertCfgExpire':nsVpnCertCfgExpire,'nsVpnCertCfgIssuer':nsVpnCertCfgIssuer,'nsVpnCertCfgVsys':nsVpnCertCfgVsys})