_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
tme,=mibBuilder.importSymbols('Papouch-SMI','tme')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Vars_ObjectIdentity=ObjectIdentity
vars=_Vars_ObjectIdentity((1,3,6,1,4,1,18248,1,1))
_Int_temperature_Type=Integer32
_Int_temperature_Object=MibScalar
int_temperature=_Int_temperature_Object((1,3,6,1,4,1,18248,1,1,1),_Int_temperature_Type())
int_temperature.setMaxAccess(_A)
if mibBuilder.loadTexts:int_temperature.setStatus(_B)
_String_temperature_Type=DisplayString
_String_temperature_Object=MibScalar
string_temperature=_String_temperature_Object((1,3,6,1,4,1,18248,1,1,2),_String_temperature_Type())
string_temperature.setMaxAccess(_A)
if mibBuilder.loadTexts:string_temperature.setStatus(_B)
_Device_name_Type=DisplayString
_Device_name_Object=MibScalar
device_name=_Device_name_Object((1,3,6,1,4,1,18248,1,1,3),_Device_name_Type())
device_name.setMaxAccess(_A)
if mibBuilder.loadTexts:device_name.setStatus(_B)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,18248,1,2))
_Int_temperature_t_Type=Integer32
_Int_temperature_t_Object=MibScalar
int_temperature_t=_Int_temperature_t_Object((1,3,6,1,4,1,18248,1,2,1),_Int_temperature_t_Type())
int_temperature_t.setMaxAccess(_A)
if mibBuilder.loadTexts:int_temperature_t.setStatus(_B)
_String_temperature_t_Type=DisplayString
_String_temperature_t_Object=MibScalar
string_temperature_t=_String_temperature_t_Object((1,3,6,1,4,1,18248,1,2,2),_String_temperature_t_Type())
string_temperature_t.setMaxAccess(_A)
if mibBuilder.loadTexts:string_temperature_t.setStatus(_B)
_Device_name_t_Type=DisplayString
_Device_name_t_Object=MibScalar
device_name_t=_Device_name_t_Object((1,3,6,1,4,1,18248,1,2,3),_Device_name_t_Type())
device_name_t.setMaxAccess(_A)
if mibBuilder.loadTexts:device_name_t.setStatus(_B)
_Warning_t_Type=DisplayString
_Warning_t_Object=MibScalar
warning_t=_Warning_t_Object((1,3,6,1,4,1,18248,1,2,4),_Warning_t_Type())
warning_t.setMaxAccess(_A)
if mibBuilder.loadTexts:warning_t.setStatus(_B)
mibBuilder.exportSymbols('TMESNMP2-MIB',**{'vars':vars,'int_temperature':int_temperature,'string_temperature':string_temperature,'device_name':device_name,'traps':traps,'int_temperature_t':int_temperature_t,'string_temperature_t':string_temperature_t,'device_name_t':device_name_t,'warning_t':warning_t})