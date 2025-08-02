_E='zxPwIndex'
_D='ZXPW-STD-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zxAnCesMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnCesMib')
zxPwIndex,=mibBuilder.importSymbols(_D,_E)
zxPwL2tpv3ExtMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,22))
_ZxPwL2tpv3ExtObjects_ObjectIdentity=ObjectIdentity
zxPwL2tpv3ExtObjects=_ZxPwL2tpv3ExtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,22,1))
_ZxPwL2tpv3ExtTable_Object=MibTable
zxPwL2tpv3ExtTable=_ZxPwL2tpv3ExtTable_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1))
if mibBuilder.loadTexts:zxPwL2tpv3ExtTable.setStatus(_A)
_ZxPwL2tpv3ExtEntry_Object=MibTableRow
zxPwL2tpv3ExtEntry=_ZxPwL2tpv3ExtEntry_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1,1))
zxPwL2tpv3ExtEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxPwL2tpv3ExtEntry.setStatus(_A)
_ZxPwL2tpv3ExtLocalCookie1_Type=Unsigned32
_ZxPwL2tpv3ExtLocalCookie1_Object=MibTableColumn
zxPwL2tpv3ExtLocalCookie1=_ZxPwL2tpv3ExtLocalCookie1_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1,1,1),_ZxPwL2tpv3ExtLocalCookie1_Type())
zxPwL2tpv3ExtLocalCookie1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwL2tpv3ExtLocalCookie1.setStatus(_A)
_ZxPwL2tpv3ExtLocalCookie2_Type=Unsigned32
_ZxPwL2tpv3ExtLocalCookie2_Object=MibTableColumn
zxPwL2tpv3ExtLocalCookie2=_ZxPwL2tpv3ExtLocalCookie2_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1,1,2),_ZxPwL2tpv3ExtLocalCookie2_Type())
zxPwL2tpv3ExtLocalCookie2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwL2tpv3ExtLocalCookie2.setStatus(_A)
_ZxPwL2tpv3ExtRemoteCookie1_Type=Unsigned32
_ZxPwL2tpv3ExtRemoteCookie1_Object=MibTableColumn
zxPwL2tpv3ExtRemoteCookie1=_ZxPwL2tpv3ExtRemoteCookie1_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1,1,3),_ZxPwL2tpv3ExtRemoteCookie1_Type())
zxPwL2tpv3ExtRemoteCookie1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwL2tpv3ExtRemoteCookie1.setStatus(_A)
_ZxPwL2tpv3ExtRemoteCookie2_Type=Unsigned32
_ZxPwL2tpv3ExtRemoteCookie2_Object=MibTableColumn
zxPwL2tpv3ExtRemoteCookie2=_ZxPwL2tpv3ExtRemoteCookie2_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1,1,4),_ZxPwL2tpv3ExtRemoteCookie2_Type())
zxPwL2tpv3ExtRemoteCookie2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwL2tpv3ExtRemoteCookie2.setStatus(_A)
class _ZxPwL2tpv3ExtServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tdm',1),('ethernet',2)))
_ZxPwL2tpv3ExtServiceType_Type.__name__=_C
_ZxPwL2tpv3ExtServiceType_Object=MibTableColumn
zxPwL2tpv3ExtServiceType=_ZxPwL2tpv3ExtServiceType_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1,1,5),_ZxPwL2tpv3ExtServiceType_Type())
zxPwL2tpv3ExtServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwL2tpv3ExtServiceType.setStatus(_A)
class _ZxPwL2tpv3ExtLocalCookieSize_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,8))
_ZxPwL2tpv3ExtLocalCookieSize_Type.__name__=_C
_ZxPwL2tpv3ExtLocalCookieSize_Object=MibTableColumn
zxPwL2tpv3ExtLocalCookieSize=_ZxPwL2tpv3ExtLocalCookieSize_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1,1,6),_ZxPwL2tpv3ExtLocalCookieSize_Type())
zxPwL2tpv3ExtLocalCookieSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwL2tpv3ExtLocalCookieSize.setStatus(_A)
class _ZxPwL2tpv3ExtRemoteCookieSize_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,8))
_ZxPwL2tpv3ExtRemoteCookieSize_Type.__name__=_C
_ZxPwL2tpv3ExtRemoteCookieSize_Object=MibTableColumn
zxPwL2tpv3ExtRemoteCookieSize=_ZxPwL2tpv3ExtRemoteCookieSize_Object((1,3,6,1,4,1,3902,1015,1013,22,1,1,1,7),_ZxPwL2tpv3ExtRemoteCookieSize_Type())
zxPwL2tpv3ExtRemoteCookieSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwL2tpv3ExtRemoteCookieSize.setStatus(_A)
mibBuilder.exportSymbols('ZXPW-L2TPV3-EXT-MIB',**{'zxPwL2tpv3ExtMIB':zxPwL2tpv3ExtMIB,'zxPwL2tpv3ExtObjects':zxPwL2tpv3ExtObjects,'zxPwL2tpv3ExtTable':zxPwL2tpv3ExtTable,'zxPwL2tpv3ExtEntry':zxPwL2tpv3ExtEntry,'zxPwL2tpv3ExtLocalCookie1':zxPwL2tpv3ExtLocalCookie1,'zxPwL2tpv3ExtLocalCookie2':zxPwL2tpv3ExtLocalCookie2,'zxPwL2tpv3ExtRemoteCookie1':zxPwL2tpv3ExtRemoteCookie1,'zxPwL2tpv3ExtRemoteCookie2':zxPwL2tpv3ExtRemoteCookie2,'zxPwL2tpv3ExtServiceType':zxPwL2tpv3ExtServiceType,'zxPwL2tpv3ExtLocalCookieSize':zxPwL2tpv3ExtLocalCookieSize,'zxPwL2tpv3ExtRemoteCookieSize':zxPwL2tpv3ExtRemoteCookieSize})