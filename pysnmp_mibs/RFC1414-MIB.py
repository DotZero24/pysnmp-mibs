_I='tcpConnRemPort'
_H='tcpConnRemAddress'
_G='tcpConnLocalPort'
_F='tcpConnLocalAddress'
_E='Integer32'
_D='read-only'
_C='TCP-MIB'
_B='OctetString'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tcpConnLocalAddress,tcpConnLocalPort,tcpConnRemAddress,tcpConnRemPort=mibBuilder.importSymbols(_C,_F,_G,_H,_I)
_Ident_ObjectIdentity=ObjectIdentity
ident=_Ident_ObjectIdentity((1,3,6,1,2,1,24))
_IdentInfo_ObjectIdentity=ObjectIdentity
identInfo=_IdentInfo_ObjectIdentity((1,3,6,1,2,1,24,1))
_IdentTable_Object=MibTable
identTable=_IdentTable_Object((1,3,6,1,2,1,24,1,1))
if mibBuilder.loadTexts:identTable.setStatus(_A)
_IdentEntry_Object=MibTableRow
identEntry=_IdentEntry_Object((1,3,6,1,2,1,24,1,1,1))
identEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:identEntry.setStatus(_A)
class _IdentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noError',1),('unknownError',2)))
_IdentStatus_Type.__name__=_E
_IdentStatus_Object=MibTableColumn
identStatus=_IdentStatus_Object((1,3,6,1,2,1,24,1,1,1,1),_IdentStatus_Type())
identStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:identStatus.setStatus(_A)
class _IdentOpSys_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_IdentOpSys_Type.__name__=_B
_IdentOpSys_Object=MibTableColumn
identOpSys=_IdentOpSys_Object((1,3,6,1,2,1,24,1,1,1,2),_IdentOpSys_Type())
identOpSys.setMaxAccess(_D)
if mibBuilder.loadTexts:identOpSys.setStatus(_A)
class _IdentCharset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_IdentCharset_Type.__name__=_B
_IdentCharset_Object=MibTableColumn
identCharset=_IdentCharset_Object((1,3,6,1,2,1,24,1,1,1,3),_IdentCharset_Type())
identCharset.setMaxAccess(_D)
if mibBuilder.loadTexts:identCharset.setStatus(_A)
class _IdentUserid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IdentUserid_Type.__name__=_B
_IdentUserid_Object=MibTableColumn
identUserid=_IdentUserid_Object((1,3,6,1,2,1,24,1,1,1,4),_IdentUserid_Type())
identUserid.setMaxAccess(_D)
if mibBuilder.loadTexts:identUserid.setStatus(_A)
class _IdentMisc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IdentMisc_Type.__name__=_B
_IdentMisc_Object=MibTableColumn
identMisc=_IdentMisc_Object((1,3,6,1,2,1,24,1,1,1,5),_IdentMisc_Type())
identMisc.setMaxAccess(_D)
if mibBuilder.loadTexts:identMisc.setStatus(_A)
mibBuilder.exportSymbols('RFC1414-MIB',**{'ident':ident,'identInfo':identInfo,'identTable':identTable,'identEntry':identEntry,'identStatus':identStatus,'identOpSys':identOpSys,'identCharset':identCharset,'identUserid':identUserid,'identMisc':identMisc})