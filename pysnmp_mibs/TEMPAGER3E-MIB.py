_F='alarmmessage'
_E='TEMPAGER3E-MIB'
_D='NotificationType'
_C='mandatory'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Avtech_ObjectIdentity=ObjectIdentity
avtech=_Avtech_ObjectIdentity((1,3,6,1,4,1,20916))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,20916,1))
_TEMPAGER3E_ObjectIdentity=ObjectIdentity
TEMPAGER3E=_TEMPAGER3E_ObjectIdentity((1,3,6,1,4,1,20916,1,7))
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,20916,1,7,1))
_Internal_ObjectIdentity=ObjectIdentity
internal=_Internal_ObjectIdentity((1,3,6,1,4,1,20916,1,7,1,1))
_Temperature_ObjectIdentity=ObjectIdentity
temperature=_Temperature_ObjectIdentity((1,3,6,1,4,1,20916,1,7,1,1,1))
class _Internal_tempc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Internal_tempc_Type.__name__=_A
_Internal_tempc_Object=MibScalar
internal_tempc=_Internal_tempc_Object((1,3,6,1,4,1,20916,1,7,1,1,1,1),_Internal_tempc_Type())
internal_tempc.setMaxAccess(_B)
if mibBuilder.loadTexts:internal_tempc.setStatus(_C)
class _Internal_tempf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Internal_tempf_Type.__name__=_A
_Internal_tempf_Object=MibScalar
internal_tempf=_Internal_tempf_Object((1,3,6,1,4,1,20916,1,7,1,1,1,2),_Internal_tempf_Type())
internal_tempf.setMaxAccess(_B)
if mibBuilder.loadTexts:internal_tempf.setStatus(_C)
_Digital_ObjectIdentity=ObjectIdentity
digital=_Digital_ObjectIdentity((1,3,6,1,4,1,20916,1,7,1,2))
_Digital_sen1_ObjectIdentity=ObjectIdentity
digital_sen1=_Digital_sen1_ObjectIdentity((1,3,6,1,4,1,20916,1,7,1,2,1))
class _Digital_sen1_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_1_Type.__name__=_A
_Digital_sen1_1_Object=MibScalar
digital_sen1_1=_Digital_sen1_1_Object((1,3,6,1,4,1,20916,1,7,1,2,1,1),_Digital_sen1_1_Type())
digital_sen1_1.setMaxAccess(_B)
if mibBuilder.loadTexts:digital_sen1_1.setStatus(_C)
class _Digital_sen1_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_2_Type.__name__=_A
_Digital_sen1_2_Object=MibScalar
digital_sen1_2=_Digital_sen1_2_Object((1,3,6,1,4,1,20916,1,7,1,2,1,2),_Digital_sen1_2_Type())
digital_sen1_2.setMaxAccess(_B)
if mibBuilder.loadTexts:digital_sen1_2.setStatus(_C)
class _Digital_sen1_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_3_Type.__name__=_A
_Digital_sen1_3_Object=MibScalar
digital_sen1_3=_Digital_sen1_3_Object((1,3,6,1,4,1,20916,1,7,1,2,1,3),_Digital_sen1_3_Type())
digital_sen1_3.setMaxAccess(_B)
if mibBuilder.loadTexts:digital_sen1_3.setStatus(_C)
class _Digital_sen1_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_4_Type.__name__=_A
_Digital_sen1_4_Object=MibScalar
digital_sen1_4=_Digital_sen1_4_Object((1,3,6,1,4,1,20916,1,7,1,2,1,4),_Digital_sen1_4_Type())
digital_sen1_4.setMaxAccess(_B)
if mibBuilder.loadTexts:digital_sen1_4.setStatus(_C)
_Digital_sen2_ObjectIdentity=ObjectIdentity
digital_sen2=_Digital_sen2_ObjectIdentity((1,3,6,1,4,1,20916,1,7,1,2,2))
class _Digital_sen2_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_1_Type.__name__=_A
_Digital_sen2_1_Object=MibScalar
digital_sen2_1=_Digital_sen2_1_Object((1,3,6,1,4,1,20916,1,7,1,2,2,1),_Digital_sen2_1_Type())
digital_sen2_1.setMaxAccess(_B)
if mibBuilder.loadTexts:digital_sen2_1.setStatus(_C)
class _Digital_sen2_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_2_Type.__name__=_A
_Digital_sen2_2_Object=MibScalar
digital_sen2_2=_Digital_sen2_2_Object((1,3,6,1,4,1,20916,1,7,1,2,2,2),_Digital_sen2_2_Type())
digital_sen2_2.setMaxAccess(_B)
if mibBuilder.loadTexts:digital_sen2_2.setStatus(_C)
class _Digital_sen2_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_3_Type.__name__=_A
_Digital_sen2_3_Object=MibScalar
digital_sen2_3=_Digital_sen2_3_Object((1,3,6,1,4,1,20916,1,7,1,2,2,3),_Digital_sen2_3_Type())
digital_sen2_3.setMaxAccess(_B)
if mibBuilder.loadTexts:digital_sen2_3.setStatus(_C)
class _Digital_sen2_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_4_Type.__name__=_A
_Digital_sen2_4_Object=MibScalar
digital_sen2_4=_Digital_sen2_4_Object((1,3,6,1,4,1,20916,1,7,1,2,2,4),_Digital_sen2_4_Type())
digital_sen2_4.setMaxAccess(_B)
if mibBuilder.loadTexts:digital_sen2_4.setStatus(_C)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,20916,1,7,2))
_Alarmmessage_Type=OctetString
_Alarmmessage_Object=MibScalar
alarmmessage=_Alarmmessage_Object((1,3,6,1,4,1,20916,1,7,2,1),_Alarmmessage_Type())
alarmmessage.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmmessage.setStatus(_C)
tempager3e_snmp_trap=NotificationType((1,3,6,1,4,1,20916,1,7,0,2))
tempager3e_snmp_trap.setObjects((_E,_F))
if mibBuilder.loadTexts:tempager3e_snmp_trap.setStatus('')
mibBuilder.exportSymbols(_E,**{'avtech':avtech,'products':products,'TEMPAGER3E':TEMPAGER3E,'tempager3e-snmp-trap':tempager3e_snmp_trap,'sensors':sensors,'internal':internal,'temperature':temperature,'internal-tempc':internal_tempc,'internal-tempf':internal_tempf,'digital':digital,'digital-sen1':digital_sen1,'digital-sen1-1':digital_sen1_1,'digital-sen1-2':digital_sen1_2,'digital-sen1-3':digital_sen1_3,'digital-sen1-4':digital_sen1_4,'digital-sen2':digital_sen2,'digital-sen2-1':digital_sen2_1,'digital-sen2-2':digital_sen2_2,'digital-sen2-3':digital_sen2_3,'digital-sen2-4':digital_sen2_4,'traps':traps,_F:alarmmessage})