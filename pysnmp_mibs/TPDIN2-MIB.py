_D='read-write'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
tpdin2=ModuleIdentity((1,3,6,1,4,1,45621,2))
class Tenths(TextualConvention,Integer32):status=_A;displayHint='d-1';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Tycon_ObjectIdentity=ObjectIdentity
tycon=_Tycon_ObjectIdentity((1,3,6,1,4,1,45621))
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,45621,2,1))
_Name_Type=DisplayString
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,45621,2,1,1),_Name_Type())
name.setMaxAccess(_B)
if mibBuilder.loadTexts:name.setStatus(_A)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,45621,2,1,2),_Version_Type())
version.setMaxAccess(_B)
if mibBuilder.loadTexts:version.setStatus(_A)
_Builddate_Type=DisplayString
_Builddate_Object=MibScalar
builddate=_Builddate_Object((1,3,6,1,4,1,45621,2,1,3),_Builddate_Type())
builddate.setMaxAccess(_B)
if mibBuilder.loadTexts:builddate.setStatus(_A)
_Monitor_ObjectIdentity=ObjectIdentity
monitor=_Monitor_ObjectIdentity((1,3,6,1,4,1,45621,2,2))
_Relay1_Type=Integer32
_Relay1_Object=MibScalar
relay1=_Relay1_Object((1,3,6,1,4,1,45621,2,2,1),_Relay1_Type())
relay1.setMaxAccess(_D)
if mibBuilder.loadTexts:relay1.setStatus(_A)
_Relay2_Type=Integer32
_Relay2_Object=MibScalar
relay2=_Relay2_Object((1,3,6,1,4,1,45621,2,2,2),_Relay2_Type())
relay2.setMaxAccess(_D)
if mibBuilder.loadTexts:relay2.setStatus(_A)
_Relay3_Type=Integer32
_Relay3_Object=MibScalar
relay3=_Relay3_Object((1,3,6,1,4,1,45621,2,2,3),_Relay3_Type())
relay3.setMaxAccess(_D)
if mibBuilder.loadTexts:relay3.setStatus(_A)
_Relay4_Type=Integer32
_Relay4_Object=MibScalar
relay4=_Relay4_Object((1,3,6,1,4,1,45621,2,2,4),_Relay4_Type())
relay4.setMaxAccess(_D)
if mibBuilder.loadTexts:relay4.setStatus(_A)
_Voltage1_Type=Tenths
_Voltage1_Object=MibScalar
voltage1=_Voltage1_Object((1,3,6,1,4,1,45621,2,2,5),_Voltage1_Type())
voltage1.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage1.setStatus(_A)
_Voltage2_Type=Tenths
_Voltage2_Object=MibScalar
voltage2=_Voltage2_Object((1,3,6,1,4,1,45621,2,2,6),_Voltage2_Type())
voltage2.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage2.setStatus(_A)
_Voltage3_Type=Tenths
_Voltage3_Object=MibScalar
voltage3=_Voltage3_Object((1,3,6,1,4,1,45621,2,2,7),_Voltage3_Type())
voltage3.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage3.setStatus(_A)
_Voltage4_Type=Tenths
_Voltage4_Object=MibScalar
voltage4=_Voltage4_Object((1,3,6,1,4,1,45621,2,2,8),_Voltage4_Type())
voltage4.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage4.setStatus(_A)
_Current1_Type=Tenths
_Current1_Object=MibScalar
current1=_Current1_Object((1,3,6,1,4,1,45621,2,2,9),_Current1_Type())
current1.setMaxAccess(_B)
if mibBuilder.loadTexts:current1.setStatus(_A)
_Current2_Type=Tenths
_Current2_Object=MibScalar
current2=_Current2_Object((1,3,6,1,4,1,45621,2,2,10),_Current2_Type())
current2.setMaxAccess(_B)
if mibBuilder.loadTexts:current2.setStatus(_A)
_Current3_Type=Tenths
_Current3_Object=MibScalar
current3=_Current3_Object((1,3,6,1,4,1,45621,2,2,11),_Current3_Type())
current3.setMaxAccess(_B)
if mibBuilder.loadTexts:current3.setStatus(_A)
_Current4_Type=Tenths
_Current4_Object=MibScalar
current4=_Current4_Object((1,3,6,1,4,1,45621,2,2,12),_Current4_Type())
current4.setMaxAccess(_B)
if mibBuilder.loadTexts:current4.setStatus(_A)
_Temperature1_Type=Tenths
_Temperature1_Object=MibScalar
temperature1=_Temperature1_Object((1,3,6,1,4,1,45621,2,2,13),_Temperature1_Type())
temperature1.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature1.setStatus(_A)
_Temperature2_Type=Tenths
_Temperature2_Object=MibScalar
temperature2=_Temperature2_Object((1,3,6,1,4,1,45621,2,2,14),_Temperature2_Type())
temperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature2.setStatus(_A)
class _Voltage1String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Voltage1String_Type.__name__=_C
_Voltage1String_Object=MibScalar
voltage1String=_Voltage1String_Object((1,3,6,1,4,1,45621,2,2,15),_Voltage1String_Type())
voltage1String.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage1String.setStatus(_A)
class _Voltage2String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Voltage2String_Type.__name__=_C
_Voltage2String_Object=MibScalar
voltage2String=_Voltage2String_Object((1,3,6,1,4,1,45621,2,2,16),_Voltage2String_Type())
voltage2String.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage2String.setStatus(_A)
class _Voltage3String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Voltage3String_Type.__name__=_C
_Voltage3String_Object=MibScalar
voltage3String=_Voltage3String_Object((1,3,6,1,4,1,45621,2,2,17),_Voltage3String_Type())
voltage3String.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage3String.setStatus(_A)
class _Voltage4String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Voltage4String_Type.__name__=_C
_Voltage4String_Object=MibScalar
voltage4String=_Voltage4String_Object((1,3,6,1,4,1,45621,2,2,18),_Voltage4String_Type())
voltage4String.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage4String.setStatus(_A)
class _Current1String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Current1String_Type.__name__=_C
_Current1String_Object=MibScalar
current1String=_Current1String_Object((1,3,6,1,4,1,45621,2,2,19),_Current1String_Type())
current1String.setMaxAccess(_B)
if mibBuilder.loadTexts:current1String.setStatus(_A)
class _Current2String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Current2String_Type.__name__=_C
_Current2String_Object=MibScalar
current2String=_Current2String_Object((1,3,6,1,4,1,45621,2,2,20),_Current2String_Type())
current2String.setMaxAccess(_B)
if mibBuilder.loadTexts:current2String.setStatus(_A)
class _Current3String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Current3String_Type.__name__=_C
_Current3String_Object=MibScalar
current3String=_Current3String_Object((1,3,6,1,4,1,45621,2,2,21),_Current3String_Type())
current3String.setMaxAccess(_B)
if mibBuilder.loadTexts:current3String.setStatus(_A)
class _Current4String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Current4String_Type.__name__=_C
_Current4String_Object=MibScalar
current4String=_Current4String_Object((1,3,6,1,4,1,45621,2,2,22),_Current4String_Type())
current4String.setMaxAccess(_B)
if mibBuilder.loadTexts:current4String.setStatus(_A)
class _Temp1String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Temp1String_Type.__name__=_C
_Temp1String_Object=MibScalar
temp1String=_Temp1String_Object((1,3,6,1,4,1,45621,2,2,23),_Temp1String_Type())
temp1String.setMaxAccess(_B)
if mibBuilder.loadTexts:temp1String.setStatus(_A)
class _Temp2String_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Temp2String_Type.__name__=_C
_Temp2String_Object=MibScalar
temp2String=_Temp2String_Object((1,3,6,1,4,1,45621,2,2,24),_Temp2String_Type())
temp2String.setMaxAccess(_B)
if mibBuilder.loadTexts:temp2String.setStatus(_A)
mibBuilder.exportSymbols('TPDIN2-MIB',**{'Tenths':Tenths,'tycon':tycon,'tpdin2':tpdin2,'product':product,'name':name,'version':version,'builddate':builddate,'monitor':monitor,'relay1':relay1,'relay2':relay2,'relay3':relay3,'relay4':relay4,'voltage1':voltage1,'voltage2':voltage2,'voltage3':voltage3,'voltage4':voltage4,'current1':current1,'current2':current2,'current3':current3,'current4':current4,'temperature1':temperature1,'temperature2':temperature2,'voltage1String':voltage1String,'voltage2String':voltage2String,'voltage3String':voltage3String,'voltage4String':voltage4String,'current1String':current1String,'current2String':current2String,'current3String':current3String,'current4String':current4String,'temp1String':temp1String,'temp2String':temp2String})