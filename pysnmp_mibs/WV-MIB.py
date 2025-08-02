_G='read-write'
_F='ON'
_E='OFF'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
webvoltmeter=ModuleIdentity((1,3,6,1,4,1,3))
class ON_OFF(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Tycon_ObjectIdentity=ObjectIdentity
tycon=_Tycon_ObjectIdentity((1,3,6,1,4,1,17095))
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,17095,1))
_Name_Type=DisplayString
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,17095,1,1),_Name_Type())
name.setMaxAccess(_B)
if mibBuilder.loadTexts:name.setStatus(_A)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,17095,1,2),_Version_Type())
version.setMaxAccess(_B)
if mibBuilder.loadTexts:version.setStatus(_A)
_Builddate_Type=DisplayString
_Builddate_Object=MibScalar
builddate=_Builddate_Object((1,3,6,1,4,1,17095,1,3),_Builddate_Type())
builddate.setMaxAccess(_B)
if mibBuilder.loadTexts:builddate.setStatus(_A)
_Control_ObjectIdentity=ObjectIdentity
control=_Control_ObjectIdentity((1,3,6,1,4,1,17095,3))
class _Relay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay1_Type.__name__=_D
_Relay1_Object=MibScalar
relay1=_Relay1_Object((1,3,6,1,4,1,17095,3,1),_Relay1_Type())
relay1.setMaxAccess(_G)
if mibBuilder.loadTexts:relay1.setStatus(_A)
class _Relay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay2_Type.__name__=_D
_Relay2_Object=MibScalar
relay2=_Relay2_Object((1,3,6,1,4,1,17095,3,2),_Relay2_Type())
relay2.setMaxAccess(_G)
if mibBuilder.loadTexts:relay2.setStatus(_A)
class _Relay3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay3_Type.__name__=_D
_Relay3_Object=MibScalar
relay3=_Relay3_Object((1,3,6,1,4,1,17095,3,3),_Relay3_Type())
relay3.setMaxAccess(_G)
if mibBuilder.loadTexts:relay3.setStatus(_A)
class _Relay4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay4_Type.__name__=_D
_Relay4_Object=MibScalar
relay4=_Relay4_Object((1,3,6,1,4,1,17095,3,4),_Relay4_Type())
relay4.setMaxAccess(_G)
if mibBuilder.loadTexts:relay4.setStatus(_A)
class _Volt1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Volt1_Type.__name__=_C
_Volt1_Object=MibScalar
volt1=_Volt1_Object((1,3,6,1,4,1,17095,3,5),_Volt1_Type())
volt1.setMaxAccess(_B)
if mibBuilder.loadTexts:volt1.setStatus(_A)
class _Volt2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Volt2_Type.__name__=_C
_Volt2_Object=MibScalar
volt2=_Volt2_Object((1,3,6,1,4,1,17095,3,6),_Volt2_Type())
volt2.setMaxAccess(_B)
if mibBuilder.loadTexts:volt2.setStatus(_A)
class _Volt3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Volt3_Type.__name__=_C
_Volt3_Object=MibScalar
volt3=_Volt3_Object((1,3,6,1,4,1,17095,3,7),_Volt3_Type())
volt3.setMaxAccess(_B)
if mibBuilder.loadTexts:volt3.setStatus(_A)
class _Volt4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Volt4_Type.__name__=_C
_Volt4_Object=MibScalar
volt4=_Volt4_Object((1,3,6,1,4,1,17095,3,8),_Volt4_Type())
volt4.setMaxAccess(_B)
if mibBuilder.loadTexts:volt4.setStatus(_A)
class _Amp1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Amp1_Type.__name__=_C
_Amp1_Object=MibScalar
amp1=_Amp1_Object((1,3,6,1,4,1,17095,3,9),_Amp1_Type())
amp1.setMaxAccess(_B)
if mibBuilder.loadTexts:amp1.setStatus(_A)
class _Amp2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Amp2_Type.__name__=_C
_Amp2_Object=MibScalar
amp2=_Amp2_Object((1,3,6,1,4,1,17095,3,10),_Amp2_Type())
amp2.setMaxAccess(_B)
if mibBuilder.loadTexts:amp2.setStatus(_A)
class _Amp3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Amp3_Type.__name__=_C
_Amp3_Object=MibScalar
amp3=_Amp3_Object((1,3,6,1,4,1,17095,3,11),_Amp3_Type())
amp3.setMaxAccess(_B)
if mibBuilder.loadTexts:amp3.setStatus(_A)
class _Amp4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Amp4_Type.__name__=_C
_Amp4_Object=MibScalar
amp4=_Amp4_Object((1,3,6,1,4,1,17095,3,12),_Amp4_Type())
amp4.setMaxAccess(_B)
if mibBuilder.loadTexts:amp4.setStatus(_A)
class _Temp1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Temp1_Type.__name__=_C
_Temp1_Object=MibScalar
temp1=_Temp1_Object((1,3,6,1,4,1,17095,3,13),_Temp1_Type())
temp1.setMaxAccess(_B)
if mibBuilder.loadTexts:temp1.setStatus(_A)
class _Temp2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Temp2_Type.__name__=_C
_Temp2_Object=MibScalar
temp2=_Temp2_Object((1,3,6,1,4,1,17095,3,14),_Temp2_Type())
temp2.setMaxAccess(_B)
if mibBuilder.loadTexts:temp2.setStatus(_A)
mibBuilder.exportSymbols('WV-MIB',**{'ON-OFF':ON_OFF,'webvoltmeter':webvoltmeter,'tycon':tycon,'product':product,'name':name,'version':version,'builddate':builddate,'control':control,'relay1':relay1,'relay2':relay2,'relay3':relay3,'relay4':relay4,'volt1':volt1,'volt2':volt2,'volt3':volt3,'volt4':volt4,'amp1':amp1,'amp2':amp2,'amp3':amp3,'amp4':amp4,'temp1':temp1,'temp2':temp2})