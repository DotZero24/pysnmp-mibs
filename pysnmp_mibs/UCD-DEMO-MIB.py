_E='read-only'
_D='read-write'
_C='Integer32'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ucdavis,=mibBuilder.importSymbols('UCD-SNMP-MIB','ucdavis')
ucdDemoMIB=ModuleIdentity((1,3,6,1,4,1,2021,14))
if mibBuilder.loadTexts:ucdDemoMIB.setRevisions(('1999-12-09 00:00',))
_UcdDemoMIBObjects_ObjectIdentity=ObjectIdentity
ucdDemoMIBObjects=_UcdDemoMIBObjects_ObjectIdentity((1,3,6,1,4,1,2021,14,1))
_UcdDemoPublic_ObjectIdentity=ObjectIdentity
ucdDemoPublic=_UcdDemoPublic_ObjectIdentity((1,3,6,1,4,1,2021,14,1,1))
class _UcdDemoResetKeys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_UcdDemoResetKeys_Type.__name__=_C
_UcdDemoResetKeys_Object=MibScalar
ucdDemoResetKeys=_UcdDemoResetKeys_Object((1,3,6,1,4,1,2021,14,1,1,1),_UcdDemoResetKeys_Type())
ucdDemoResetKeys.setMaxAccess(_D)
if mibBuilder.loadTexts:ucdDemoResetKeys.setStatus(_A)
class _UcdDemoPublicString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_UcdDemoPublicString_Type.__name__=_B
_UcdDemoPublicString_Object=MibScalar
ucdDemoPublicString=_UcdDemoPublicString_Object((1,3,6,1,4,1,2021,14,1,1,2),_UcdDemoPublicString_Type())
ucdDemoPublicString.setMaxAccess(_D)
if mibBuilder.loadTexts:ucdDemoPublicString.setStatus(_A)
_UcdDemoUserList_Type=OctetString
_UcdDemoUserList_Object=MibScalar
ucdDemoUserList=_UcdDemoUserList_Object((1,3,6,1,4,1,2021,14,1,1,3),_UcdDemoUserList_Type())
ucdDemoUserList.setMaxAccess(_E)
if mibBuilder.loadTexts:ucdDemoUserList.setStatus(_A)
_UcdDemoPassphrase_Type=OctetString
_UcdDemoPassphrase_Object=MibScalar
ucdDemoPassphrase=_UcdDemoPassphrase_Object((1,3,6,1,4,1,2021,14,1,1,4),_UcdDemoPassphrase_Type())
ucdDemoPassphrase.setMaxAccess(_E)
if mibBuilder.loadTexts:ucdDemoPassphrase.setStatus(_A)
mibBuilder.exportSymbols('UCD-DEMO-MIB',**{'ucdDemoMIB':ucdDemoMIB,'ucdDemoMIBObjects':ucdDemoMIBObjects,'ucdDemoPublic':ucdDemoPublic,'ucdDemoResetKeys':ucdDemoResetKeys,'ucdDemoPublicString':ucdDemoPublicString,'ucdDemoUserList':ucdDemoUserList,'ucdDemoPassphrase':ucdDemoPassphrase})