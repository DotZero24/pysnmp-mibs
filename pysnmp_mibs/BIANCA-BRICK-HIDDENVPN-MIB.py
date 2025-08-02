_G='flash'
_F='read-only'
_E='blink'
_D='on'
_C='off'
_B='mandatory'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Admin_ObjectIdentity=ObjectIdentity
admin=_Admin_ObjectIdentity((1,3,6,1,4,1,272,4,1))
_BiboAdmLed_ObjectIdentity=ObjectIdentity
biboAdmLed=_BiboAdmLed_ObjectIdentity((1,3,6,1,4,1,272,253))
class _BiboAdmLedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_G,4)))
_BiboAdmLedStatus_Type.__name__=_A
_BiboAdmLedStatus_Object=MibScalar
biboAdmLedStatus=_BiboAdmLedStatus_Object((1,3,6,1,4,1,272,253,1),_BiboAdmLedStatus_Type())
biboAdmLedStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:biboAdmLedStatus.setStatus(_B)
class _BiboAdmLedMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_G,4)))
_BiboAdmLedMgmt_Type.__name__=_A
_BiboAdmLedMgmt_Object=MibScalar
biboAdmLedMgmt=_BiboAdmLedMgmt_Object((1,3,6,1,4,1,272,253,2),_BiboAdmLedMgmt_Type())
biboAdmLedMgmt.setMaxAccess(_F)
if mibBuilder.loadTexts:biboAdmLedMgmt.setStatus(_B)
class _BiboAdmLedHA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_G,4)))
_BiboAdmLedHA_Type.__name__=_A
_BiboAdmLedHA_Object=MibScalar
biboAdmLedHA=_BiboAdmLedHA_Object((1,3,6,1,4,1,272,253,3),_BiboAdmLedHA_Type())
biboAdmLedHA.setMaxAccess(_F)
if mibBuilder.loadTexts:biboAdmLedHA.setStatus(_B)
class _BiboAdmLedInternet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_G,4)))
_BiboAdmLedInternet_Type.__name__=_A
_BiboAdmLedInternet_Object=MibScalar
biboAdmLedInternet=_BiboAdmLedInternet_Object((1,3,6,1,4,1,272,253,4),_BiboAdmLedInternet_Type())
biboAdmLedInternet.setMaxAccess(_F)
if mibBuilder.loadTexts:biboAdmLedInternet.setStatus(_B)
class _BiboAdmLedSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('linkact',4)))
_BiboAdmLedSwitch_Type.__name__=_A
_BiboAdmLedSwitch_Object=MibScalar
biboAdmLedSwitch=_BiboAdmLedSwitch_Object((1,3,6,1,4,1,272,253,5),_BiboAdmLedSwitch_Type())
biboAdmLedSwitch.setMaxAccess(_F)
if mibBuilder.loadTexts:biboAdmLedSwitch.setStatus(_B)
class _BiboAdmLedMeter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_BiboAdmLedMeter_Type.__name__=_A
_BiboAdmLedMeter_Object=MibScalar
biboAdmLedMeter=_BiboAdmLedMeter_Object((1,3,6,1,4,1,272,253,6),_BiboAdmLedMeter_Type())
biboAdmLedMeter.setMaxAccess('read-write')
if mibBuilder.loadTexts:biboAdmLedMeter.setStatus(_B)
mibBuilder.exportSymbols('BIANCA-BRICK-HIDDENVPN-MIB',**{'bintec':bintec,'bibo':bibo,'admin':admin,'biboAdmLed':biboAdmLed,'biboAdmLedStatus':biboAdmLedStatus,'biboAdmLedMgmt':biboAdmLedMgmt,'biboAdmLedHA':biboAdmLedHA,'biboAdmLedInternet':biboAdmLedInternet,'biboAdmLedSwitch':biboAdmLedSwitch,'biboAdmLedMeter':biboAdmLedMeter})