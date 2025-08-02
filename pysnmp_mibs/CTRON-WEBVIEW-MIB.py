_E='disable'
_D='enable'
_C='Integer32'
_B='mandatory'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctApplication,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctApplication')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtWebView_ObjectIdentity=ObjectIdentity
ctWebView=_CtWebView_ObjectIdentity((1,3,6,1,4,1,52,4,1,4,4))
_CtEwvConfiguration_ObjectIdentity=ObjectIdentity
ctEwvConfiguration=_CtEwvConfiguration_ObjectIdentity((1,3,6,1,4,1,52,4,1,4,4,1))
_CtEwvDocSupport_ObjectIdentity=ObjectIdentity
ctEwvDocSupport=_CtEwvDocSupport_ObjectIdentity((1,3,6,1,4,1,52,4,1,4,4,1,1))
class _CtEwvDocSupportAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtEwvDocSupportAdmin_Type.__name__=_C
_CtEwvDocSupportAdmin_Object=MibScalar
ctEwvDocSupportAdmin=_CtEwvDocSupportAdmin_Object((1,3,6,1,4,1,52,4,1,4,4,1,1,1),_CtEwvDocSupportAdmin_Type())
ctEwvDocSupportAdmin.setMaxAccess(_A)
if mibBuilder.loadTexts:ctEwvDocSupportAdmin.setStatus(_B)
_CtEwvDocSupportLocation_Type=DisplayString
_CtEwvDocSupportLocation_Object=MibScalar
ctEwvDocSupportLocation=_CtEwvDocSupportLocation_Object((1,3,6,1,4,1,52,4,1,4,4,1,1,2),_CtEwvDocSupportLocation_Type())
ctEwvDocSupportLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:ctEwvDocSupportLocation.setStatus(_B)
class _CtEwvDocSupportAdminUID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtEwvDocSupportAdminUID_Type.__name__=_C
_CtEwvDocSupportAdminUID_Object=MibScalar
ctEwvDocSupportAdminUID=_CtEwvDocSupportAdminUID_Object((1,3,6,1,4,1,52,4,1,4,4,1,1,3),_CtEwvDocSupportAdminUID_Type())
ctEwvDocSupportAdminUID.setMaxAccess(_A)
if mibBuilder.loadTexts:ctEwvDocSupportAdminUID.setStatus(_B)
_CtEwvDocSupportUsername_Type=DisplayString
_CtEwvDocSupportUsername_Object=MibScalar
ctEwvDocSupportUsername=_CtEwvDocSupportUsername_Object((1,3,6,1,4,1,52,4,1,4,4,1,1,4),_CtEwvDocSupportUsername_Type())
ctEwvDocSupportUsername.setMaxAccess(_A)
if mibBuilder.loadTexts:ctEwvDocSupportUsername.setStatus(_B)
_CtEwvDocSupportPassword_Type=DisplayString
_CtEwvDocSupportPassword_Object=MibScalar
ctEwvDocSupportPassword=_CtEwvDocSupportPassword_Object((1,3,6,1,4,1,52,4,1,4,4,1,1,5),_CtEwvDocSupportPassword_Type())
ctEwvDocSupportPassword.setMaxAccess(_A)
if mibBuilder.loadTexts:ctEwvDocSupportPassword.setStatus(_B)
_CtEwvSystemParameters_ObjectIdentity=ObjectIdentity
ctEwvSystemParameters=_CtEwvSystemParameters_ObjectIdentity((1,3,6,1,4,1,52,4,1,4,4,1,2))
class _CtEwvAuthScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('basic',2),('digest',3)))
_CtEwvAuthScheme_Type.__name__=_C
_CtEwvAuthScheme_Object=MibScalar
ctEwvAuthScheme=_CtEwvAuthScheme_Object((1,3,6,1,4,1,52,4,1,4,4,1,2,1),_CtEwvAuthScheme_Type())
ctEwvAuthScheme.setMaxAccess(_A)
if mibBuilder.loadTexts:ctEwvAuthScheme.setStatus(_B)
_CtEwvAuthNonceValidCount_Type=Integer32
_CtEwvAuthNonceValidCount_Object=MibScalar
ctEwvAuthNonceValidCount=_CtEwvAuthNonceValidCount_Object((1,3,6,1,4,1,52,4,1,4,4,1,2,2),_CtEwvAuthNonceValidCount_Type())
ctEwvAuthNonceValidCount.setMaxAccess(_A)
if mibBuilder.loadTexts:ctEwvAuthNonceValidCount.setStatus(_B)
_CtEwvStatus_ObjectIdentity=ObjectIdentity
ctEwvStatus=_CtEwvStatus_ObjectIdentity((1,3,6,1,4,1,52,4,1,4,4,2))
mibBuilder.exportSymbols('CTRON-WEBVIEW-MIB',**{'ctWebView':ctWebView,'ctEwvConfiguration':ctEwvConfiguration,'ctEwvDocSupport':ctEwvDocSupport,'ctEwvDocSupportAdmin':ctEwvDocSupportAdmin,'ctEwvDocSupportLocation':ctEwvDocSupportLocation,'ctEwvDocSupportAdminUID':ctEwvDocSupportAdminUID,'ctEwvDocSupportUsername':ctEwvDocSupportUsername,'ctEwvDocSupportPassword':ctEwvDocSupportPassword,'ctEwvSystemParameters':ctEwvSystemParameters,'ctEwvAuthScheme':ctEwvAuthScheme,'ctEwvAuthNonceValidCount':ctEwvAuthNonceValidCount,'ctEwvStatus':ctEwvStatus})