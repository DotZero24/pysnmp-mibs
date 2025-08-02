_F='dot1dBasePort'
_E='BRIDGE-MIB'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_E,_F)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelMacAuthentication=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,46))
_ZyxelMacAuthenticationSetup_ObjectIdentity=ObjectIdentity
zyxelMacAuthenticationSetup=_ZyxelMacAuthenticationSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,46,1))
_ZyMacAuthenticationState_Type=EnabledStatus
_ZyMacAuthenticationState_Object=MibScalar
zyMacAuthenticationState=_ZyMacAuthenticationState_Object((1,3,6,1,4,1,890,1,15,3,46,1,1),_ZyMacAuthenticationState_Type())
zyMacAuthenticationState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationState.setStatus(_A)
_ZyMacAuthenticationNamePrefix_Type=DisplayString
_ZyMacAuthenticationNamePrefix_Object=MibScalar
zyMacAuthenticationNamePrefix=_ZyMacAuthenticationNamePrefix_Object((1,3,6,1,4,1,890,1,15,3,46,1,2),_ZyMacAuthenticationNamePrefix_Type())
zyMacAuthenticationNamePrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationNamePrefix.setStatus(_A)
_ZyMacAuthenticationPassword_Type=DisplayString
_ZyMacAuthenticationPassword_Object=MibScalar
zyMacAuthenticationPassword=_ZyMacAuthenticationPassword_Object((1,3,6,1,4,1,890,1,15,3,46,1,3),_ZyMacAuthenticationPassword_Type())
zyMacAuthenticationPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationPassword.setStatus(_A)
_ZyMacAuthenticationTimeout_Type=Integer32
_ZyMacAuthenticationTimeout_Object=MibScalar
zyMacAuthenticationTimeout=_ZyMacAuthenticationTimeout_Object((1,3,6,1,4,1,890,1,15,3,46,1,4),_ZyMacAuthenticationTimeout_Type())
zyMacAuthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationTimeout.setStatus(_A)
_ZyxelMacAuthenticationPortTable_Object=MibTable
zyxelMacAuthenticationPortTable=_ZyxelMacAuthenticationPortTable_Object((1,3,6,1,4,1,890,1,15,3,46,1,5))
if mibBuilder.loadTexts:zyxelMacAuthenticationPortTable.setStatus(_A)
_ZyxelMacAuthenticationPortEntry_Object=MibTableRow
zyxelMacAuthenticationPortEntry=_ZyxelMacAuthenticationPortEntry_Object((1,3,6,1,4,1,890,1,15,3,46,1,5,1))
zyxelMacAuthenticationPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelMacAuthenticationPortEntry.setStatus(_A)
_ZyMacAuthenticationPortState_Type=EnabledStatus
_ZyMacAuthenticationPortState_Object=MibTableColumn
zyMacAuthenticationPortState=_ZyMacAuthenticationPortState_Object((1,3,6,1,4,1,890,1,15,3,46,1,5,1,1),_ZyMacAuthenticationPortState_Type())
zyMacAuthenticationPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationPortState.setStatus(_A)
class _ZyMacAuthenticationPortTrustedVlan1k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyMacAuthenticationPortTrustedVlan1k_Type.__name__=_C
_ZyMacAuthenticationPortTrustedVlan1k_Object=MibTableColumn
zyMacAuthenticationPortTrustedVlan1k=_ZyMacAuthenticationPortTrustedVlan1k_Object((1,3,6,1,4,1,890,1,15,3,46,1,5,1,2),_ZyMacAuthenticationPortTrustedVlan1k_Type())
zyMacAuthenticationPortTrustedVlan1k.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationPortTrustedVlan1k.setStatus(_A)
class _ZyMacAuthenticationPortTrustedVlan2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyMacAuthenticationPortTrustedVlan2k_Type.__name__=_C
_ZyMacAuthenticationPortTrustedVlan2k_Object=MibTableColumn
zyMacAuthenticationPortTrustedVlan2k=_ZyMacAuthenticationPortTrustedVlan2k_Object((1,3,6,1,4,1,890,1,15,3,46,1,5,1,3),_ZyMacAuthenticationPortTrustedVlan2k_Type())
zyMacAuthenticationPortTrustedVlan2k.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationPortTrustedVlan2k.setStatus(_A)
class _ZyMacAuthenticationPortTrustedVlan3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyMacAuthenticationPortTrustedVlan3k_Type.__name__=_C
_ZyMacAuthenticationPortTrustedVlan3k_Object=MibTableColumn
zyMacAuthenticationPortTrustedVlan3k=_ZyMacAuthenticationPortTrustedVlan3k_Object((1,3,6,1,4,1,890,1,15,3,46,1,5,1,4),_ZyMacAuthenticationPortTrustedVlan3k_Type())
zyMacAuthenticationPortTrustedVlan3k.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationPortTrustedVlan3k.setStatus(_A)
class _ZyMacAuthenticationPortTrustedVlan4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyMacAuthenticationPortTrustedVlan4k_Type.__name__=_C
_ZyMacAuthenticationPortTrustedVlan4k_Object=MibTableColumn
zyMacAuthenticationPortTrustedVlan4k=_ZyMacAuthenticationPortTrustedVlan4k_Object((1,3,6,1,4,1,890,1,15,3,46,1,5,1,5),_ZyMacAuthenticationPortTrustedVlan4k_Type())
zyMacAuthenticationPortTrustedVlan4k.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationPortTrustedVlan4k.setStatus(_A)
class _ZyMacAuthenticationDelimiter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dash',1),('colon',2),('none',3)))
_ZyMacAuthenticationDelimiter_Type.__name__=_D
_ZyMacAuthenticationDelimiter_Object=MibScalar
zyMacAuthenticationDelimiter=_ZyMacAuthenticationDelimiter_Object((1,3,6,1,4,1,890,1,15,3,46,1,6),_ZyMacAuthenticationDelimiter_Type())
zyMacAuthenticationDelimiter.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationDelimiter.setStatus(_A)
class _ZyMacAuthenticationCase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upper',1),('lower',2)))
_ZyMacAuthenticationCase_Type.__name__=_D
_ZyMacAuthenticationCase_Object=MibScalar
zyMacAuthenticationCase=_ZyMacAuthenticationCase_Object((1,3,6,1,4,1,890,1,15,3,46,1,7),_ZyMacAuthenticationCase_Type())
zyMacAuthenticationCase.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationCase.setStatus(_A)
class _ZyMacAuthenticationPasswordType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('mac-address',2)))
_ZyMacAuthenticationPasswordType_Type.__name__=_D
_ZyMacAuthenticationPasswordType_Object=MibScalar
zyMacAuthenticationPasswordType=_ZyMacAuthenticationPasswordType_Object((1,3,6,1,4,1,890,1,15,3,46,1,8),_ZyMacAuthenticationPasswordType_Type())
zyMacAuthenticationPasswordType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacAuthenticationPasswordType.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-MAC-AUTHENTICATION-MIB',**{'zyxelMacAuthentication':zyxelMacAuthentication,'zyxelMacAuthenticationSetup':zyxelMacAuthenticationSetup,'zyMacAuthenticationState':zyMacAuthenticationState,'zyMacAuthenticationNamePrefix':zyMacAuthenticationNamePrefix,'zyMacAuthenticationPassword':zyMacAuthenticationPassword,'zyMacAuthenticationTimeout':zyMacAuthenticationTimeout,'zyxelMacAuthenticationPortTable':zyxelMacAuthenticationPortTable,'zyxelMacAuthenticationPortEntry':zyxelMacAuthenticationPortEntry,'zyMacAuthenticationPortState':zyMacAuthenticationPortState,'zyMacAuthenticationPortTrustedVlan1k':zyMacAuthenticationPortTrustedVlan1k,'zyMacAuthenticationPortTrustedVlan2k':zyMacAuthenticationPortTrustedVlan2k,'zyMacAuthenticationPortTrustedVlan3k':zyMacAuthenticationPortTrustedVlan3k,'zyMacAuthenticationPortTrustedVlan4k':zyMacAuthenticationPortTrustedVlan4k,'zyMacAuthenticationDelimiter':zyMacAuthenticationDelimiter,'zyMacAuthenticationCase':zyMacAuthenticationCase,'zyMacAuthenticationPasswordType':zyMacAuthenticationPasswordType})