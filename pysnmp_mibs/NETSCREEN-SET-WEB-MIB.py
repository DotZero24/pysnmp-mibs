_F='nsSetWebVsys'
_E='NETSCREEN-SET-WEB-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSetting,netscreenSettingMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSetting','netscreenSettingMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenSetWebMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,12))
if mibBuilder.loadTexts:netscreenSetWebMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-12 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetWebUI_ObjectIdentity=ObjectIdentity
nsSetWebUI=_NsSetWebUI_ObjectIdentity((1,3,6,1,4,1,3224,7,12))
_NsSetWebUICfgTable_Object=MibTable
nsSetWebUICfgTable=_NsSetWebUICfgTable_Object((1,3,6,1,4,1,3224,7,12,1))
if mibBuilder.loadTexts:nsSetWebUICfgTable.setStatus(_A)
_NsSetWebUICfgEntry_Object=MibTableRow
nsSetWebUICfgEntry=_NsSetWebUICfgEntry_Object((1,3,6,1,4,1,3224,7,12,1,1))
nsSetWebUICfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsSetWebUICfgEntry.setStatus(_A)
class _NsSetWebVsys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSetWebVsys_Type.__name__=_C
_NsSetWebVsys_Object=MibTableColumn
nsSetWebVsys=_NsSetWebVsys_Object((1,3,6,1,4,1,3224,7,12,1,1,1),_NsSetWebVsys_Type())
nsSetWebVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetWebVsys.setStatus(_A)
class _NsSetWebIdleTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enabled',1)))
_NsSetWebIdleTimeout_Type.__name__=_C
_NsSetWebIdleTimeout_Object=MibTableColumn
nsSetWebIdleTimeout=_NsSetWebIdleTimeout_Object((1,3,6,1,4,1,3224,7,12,1,1,2),_NsSetWebIdleTimeout_Type())
nsSetWebIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetWebIdleTimeout.setStatus(_A)
_NsSetWebTimeout_Type=Integer32
_NsSetWebTimeout_Object=MibTableColumn
nsSetWebTimeout=_NsSetWebTimeout_Object((1,3,6,1,4,1,3224,7,12,1,1,3),_NsSetWebTimeout_Type())
nsSetWebTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetWebTimeout.setStatus(_A)
_NsSetWebPort_Type=Integer32
_NsSetWebPort_Object=MibTableColumn
nsSetWebPort=_NsSetWebPort_Object((1,3,6,1,4,1,3224,7,12,1,1,4),_NsSetWebPort_Type())
nsSetWebPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetWebPort.setStatus(_A)
_NsSetWebSSLPort_Type=Integer32
_NsSetWebSSLPort_Object=MibTableColumn
nsSetWebSSLPort=_NsSetWebSSLPort_Object((1,3,6,1,4,1,3224,7,12,1,1,5),_NsSetWebSSLPort_Type())
nsSetWebSSLPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetWebSSLPort.setStatus(_A)
class _NsSetWebSSLCertificate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsSetWebSSLCertificate_Type.__name__=_D
_NsSetWebSSLCertificate_Object=MibTableColumn
nsSetWebSSLCertificate=_NsSetWebSSLCertificate_Object((1,3,6,1,4,1,3224,7,12,1,1,6),_NsSetWebSSLCertificate_Type())
nsSetWebSSLCertificate.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetWebSSLCertificate.setStatus(_A)
class _NsSetWebSSLCipher_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('rc4-md5',0),('rc4-40-md5',1),('des-sha',2),('triple-des-sha',3)))
_NsSetWebSSLCipher_Type.__name__=_C
_NsSetWebSSLCipher_Object=MibTableColumn
nsSetWebSSLCipher=_NsSetWebSSLCipher_Object((1,3,6,1,4,1,3224,7,12,1,1,7),_NsSetWebSSLCipher_Type())
nsSetWebSSLCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetWebSSLCipher.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenSetWebMibModule':netscreenSetWebMibModule,'nsSetWebUI':nsSetWebUI,'nsSetWebUICfgTable':nsSetWebUICfgTable,'nsSetWebUICfgEntry':nsSetWebUICfgEntry,_F:nsSetWebVsys,'nsSetWebIdleTimeout':nsSetWebIdleTimeout,'nsSetWebTimeout':nsSetWebTimeout,'nsSetWebPort':nsSetWebPort,'nsSetWebSSLPort':nsSetWebSSLPort,'nsSetWebSSLCertificate':nsSetWebSSLCertificate,'nsSetWebSSLCipher':nsSetWebSSLCipher})