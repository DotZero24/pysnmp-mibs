_N='NotificationType'
_M='tempreading1f'
_L='tempreading1c'
_K='tempreading4f'
_J='tempreading4c'
_I='tempreading3f'
_H='tempreading3c'
_G='tempreading2f'
_F='tempreading2c'
_E='alarmmessage'
_D='read-only'
_C='mandatory'
_B='Integer32'
_A='TEMPAGER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Avtech_ObjectIdentity=ObjectIdentity
avtech=_Avtech_ObjectIdentity((1,3,6,1,4,1,20916))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,20916,1))
_Tempager_ObjectIdentity=ObjectIdentity
tempager=_Tempager_ObjectIdentity((1,3,6,1,4,1,20916,1,1))
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,20916,1,1,1))
_Temperature_ObjectIdentity=ObjectIdentity
temperature=_Temperature_ObjectIdentity((1,3,6,1,4,1,20916,1,1,1,1))
class _Tempreading1c_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tempreading1c_Type.__name__=_B
_Tempreading1c_Object=MibScalar
tempreading1c=_Tempreading1c_Object((1,3,6,1,4,1,20916,1,1,1,1,1),_Tempreading1c_Type())
tempreading1c.setMaxAccess(_D)
if mibBuilder.loadTexts:tempreading1c.setStatus(_C)
class _Tempreading2c_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tempreading2c_Type.__name__=_B
_Tempreading2c_Object=MibScalar
tempreading2c=_Tempreading2c_Object((1,3,6,1,4,1,20916,1,1,1,1,2),_Tempreading2c_Type())
tempreading2c.setMaxAccess(_D)
if mibBuilder.loadTexts:tempreading2c.setStatus(_C)
class _Tempreading3c_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tempreading3c_Type.__name__=_B
_Tempreading3c_Object=MibScalar
tempreading3c=_Tempreading3c_Object((1,3,6,1,4,1,20916,1,1,1,1,3),_Tempreading3c_Type())
tempreading3c.setMaxAccess(_D)
if mibBuilder.loadTexts:tempreading3c.setStatus(_C)
class _Tempreading4c_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tempreading4c_Type.__name__=_B
_Tempreading4c_Object=MibScalar
tempreading4c=_Tempreading4c_Object((1,3,6,1,4,1,20916,1,1,1,1,4),_Tempreading4c_Type())
tempreading4c.setMaxAccess(_D)
if mibBuilder.loadTexts:tempreading4c.setStatus(_C)
class _Tempreading1f_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tempreading1f_Type.__name__=_B
_Tempreading1f_Object=MibScalar
tempreading1f=_Tempreading1f_Object((1,3,6,1,4,1,20916,1,1,1,1,5),_Tempreading1f_Type())
tempreading1f.setMaxAccess(_D)
if mibBuilder.loadTexts:tempreading1f.setStatus(_C)
class _Tempreading2f_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tempreading2f_Type.__name__=_B
_Tempreading2f_Object=MibScalar
tempreading2f=_Tempreading2f_Object((1,3,6,1,4,1,20916,1,1,1,1,6),_Tempreading2f_Type())
tempreading2f.setMaxAccess(_D)
if mibBuilder.loadTexts:tempreading2f.setStatus(_C)
class _Tempreading3f_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tempreading3f_Type.__name__=_B
_Tempreading3f_Object=MibScalar
tempreading3f=_Tempreading3f_Object((1,3,6,1,4,1,20916,1,1,1,1,7),_Tempreading3f_Type())
tempreading3f.setMaxAccess(_D)
if mibBuilder.loadTexts:tempreading3f.setStatus(_C)
class _Tempreading4f_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tempreading4f_Type.__name__=_B
_Tempreading4f_Object=MibScalar
tempreading4f=_Tempreading4f_Object((1,3,6,1,4,1,20916,1,1,1,1,8),_Tempreading4f_Type())
tempreading4f.setMaxAccess(_D)
if mibBuilder.loadTexts:tempreading4f.setStatus(_C)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,20916,1,1,2))
class _Alarmtemp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Alarmtemp1_Type.__name__=_B
_Alarmtemp1_Object=MibScalar
alarmtemp1=_Alarmtemp1_Object((1,3,6,1,4,1,20916,1,1,2,1),_Alarmtemp1_Type())
alarmtemp1.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmtemp1.setStatus(_C)
class _Alarmtemp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Alarmtemp2_Type.__name__=_B
_Alarmtemp2_Object=MibScalar
alarmtemp2=_Alarmtemp2_Object((1,3,6,1,4,1,20916,1,1,2,2),_Alarmtemp2_Type())
alarmtemp2.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmtemp2.setStatus(_C)
class _Alarmtemp3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Alarmtemp3_Type.__name__=_B
_Alarmtemp3_Object=MibScalar
alarmtemp3=_Alarmtemp3_Object((1,3,6,1,4,1,20916,1,1,2,3),_Alarmtemp3_Type())
alarmtemp3.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmtemp3.setStatus(_C)
class _Alarmtemp4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Alarmtemp4_Type.__name__=_B
_Alarmtemp4_Object=MibScalar
alarmtemp4=_Alarmtemp4_Object((1,3,6,1,4,1,20916,1,1,2,4),_Alarmtemp4_Type())
alarmtemp4.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmtemp4.setStatus(_C)
_Alarmmessage_Type=OctetString
_Alarmmessage_Object=MibScalar
alarmmessage=_Alarmmessage_Object((1,3,6,1,4,1,20916,1,1,2,5),_Alarmmessage_Type())
alarmmessage.setMaxAccess('read-write')
if mibBuilder.loadTexts:alarmmessage.setStatus(_C)
_Thresholds_ObjectIdentity=ObjectIdentity
thresholds=_Thresholds_ObjectIdentity((1,3,6,1,4,1,20916,1,1,3))
class _Upperlimit1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_Upperlimit1_Type.__name__=_B
_Upperlimit1_Object=MibScalar
upperlimit1=_Upperlimit1_Object((1,3,6,1,4,1,20916,1,1,3,1),_Upperlimit1_Type())
upperlimit1.setMaxAccess(_D)
if mibBuilder.loadTexts:upperlimit1.setStatus(_C)
class _Lowerlimit1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_Lowerlimit1_Type.__name__=_B
_Lowerlimit1_Object=MibScalar
lowerlimit1=_Lowerlimit1_Object((1,3,6,1,4,1,20916,1,1,3,2),_Lowerlimit1_Type())
lowerlimit1.setMaxAccess(_D)
if mibBuilder.loadTexts:lowerlimit1.setStatus(_C)
class _Upperlimit2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_Upperlimit2_Type.__name__=_B
_Upperlimit2_Object=MibScalar
upperlimit2=_Upperlimit2_Object((1,3,6,1,4,1,20916,1,1,3,3),_Upperlimit2_Type())
upperlimit2.setMaxAccess(_D)
if mibBuilder.loadTexts:upperlimit2.setStatus(_C)
class _Lowerlimit2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_Lowerlimit2_Type.__name__=_B
_Lowerlimit2_Object=MibScalar
lowerlimit2=_Lowerlimit2_Object((1,3,6,1,4,1,20916,1,1,3,4),_Lowerlimit2_Type())
lowerlimit2.setMaxAccess(_D)
if mibBuilder.loadTexts:lowerlimit2.setStatus(_C)
class _Upperlimit3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_Upperlimit3_Type.__name__=_B
_Upperlimit3_Object=MibScalar
upperlimit3=_Upperlimit3_Object((1,3,6,1,4,1,20916,1,1,3,5),_Upperlimit3_Type())
upperlimit3.setMaxAccess(_D)
if mibBuilder.loadTexts:upperlimit3.setStatus(_C)
class _Lowerlimit3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_Lowerlimit3_Type.__name__=_B
_Lowerlimit3_Object=MibScalar
lowerlimit3=_Lowerlimit3_Object((1,3,6,1,4,1,20916,1,1,3,6),_Lowerlimit3_Type())
lowerlimit3.setMaxAccess(_D)
if mibBuilder.loadTexts:lowerlimit3.setStatus(_C)
class _Upperlimit4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_Upperlimit4_Type.__name__=_B
_Upperlimit4_Object=MibScalar
upperlimit4=_Upperlimit4_Object((1,3,6,1,4,1,20916,1,1,3,7),_Upperlimit4_Type())
upperlimit4.setMaxAccess(_D)
if mibBuilder.loadTexts:upperlimit4.setStatus(_C)
class _Lowerlimit4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_Lowerlimit4_Type.__name__=_B
_Lowerlimit4_Object=MibScalar
lowerlimit4=_Lowerlimit4_Object((1,3,6,1,4,1,20916,1,1,3,8),_Lowerlimit4_Type())
lowerlimit4.setMaxAccess(_D)
if mibBuilder.loadTexts:lowerlimit4.setStatus(_C)
alarmstart1_t4=NotificationType((1,3,6,1,4,1,20916,1,1,0,1))
alarmstart1_t4.setObjects(*((_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:alarmstart1_t4.setStatus('')
tempager_snmp_trap=NotificationType((1,3,6,1,4,1,20916,1,1,0,2))
tempager_snmp_trap.setObjects(*((_A,_E),(_A,_L),(_A,_M),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:tempager_snmp_trap.setStatus('')
alarmstart2_t4=NotificationType((1,3,6,1,4,1,20916,1,1,0,3))
alarmstart2_t4.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:alarmstart2_t4.setStatus('')
alarmclear2_t4=NotificationType((1,3,6,1,4,1,20916,1,1,0,4))
alarmclear2_t4.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:alarmclear2_t4.setStatus('')
alarmstart3_t4=NotificationType((1,3,6,1,4,1,20916,1,1,0,5))
alarmstart3_t4.setObjects(*((_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:alarmstart3_t4.setStatus('')
alarmclear3_t4=NotificationType((1,3,6,1,4,1,20916,1,1,0,6))
alarmclear3_t4.setObjects(*((_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:alarmclear3_t4.setStatus('')
alarmstart4_t4=NotificationType((1,3,6,1,4,1,20916,1,1,0,7))
alarmstart4_t4.setObjects(*((_A,_E),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:alarmstart4_t4.setStatus('')
alarmclear4_t4=NotificationType((1,3,6,1,4,1,20916,1,1,0,8))
alarmclear4_t4.setObjects(*((_A,_E),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:alarmclear4_t4.setStatus('')
mibBuilder.exportSymbols(_A,**{'avtech':avtech,'products':products,'tempager':tempager,'alarmstart1-t4':alarmstart1_t4,'tempager-snmp-trap':tempager_snmp_trap,'alarmstart2-t4':alarmstart2_t4,'alarmclear2-t4':alarmclear2_t4,'alarmstart3-t4':alarmstart3_t4,'alarmclear3-t4':alarmclear3_t4,'alarmstart4-t4':alarmstart4_t4,'alarmclear4-t4':alarmclear4_t4,'sensors':sensors,'temperature':temperature,_L:tempreading1c,_F:tempreading2c,_H:tempreading3c,_J:tempreading4c,_M:tempreading1f,_G:tempreading2f,_I:tempreading3f,_K:tempreading4f,'traps':traps,'alarmtemp1':alarmtemp1,'alarmtemp2':alarmtemp2,'alarmtemp3':alarmtemp3,'alarmtemp4':alarmtemp4,_E:alarmmessage,'thresholds':thresholds,'upperlimit1':upperlimit1,'lowerlimit1':lowerlimit1,'upperlimit2':upperlimit2,'lowerlimit2':lowerlimit2,'upperlimit3':upperlimit3,'lowerlimit3':lowerlimit3,'upperlimit4':upperlimit4,'lowerlimit4':lowerlimit4})