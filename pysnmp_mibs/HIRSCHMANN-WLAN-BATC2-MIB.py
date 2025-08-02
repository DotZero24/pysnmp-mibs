_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
batC2,=mibBuilder.importSymbols('HIRSCHMANN-WLAN-LT-MIB','batC2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
batC2MIB=ModuleIdentity((248,32,100,1,15,0))
_Batc2Trap_ObjectIdentity=ObjectIdentity
batc2Trap=_Batc2Trap_ObjectIdentity((248,32,100,1,15,4))
_AlarmType_Type=DisplayString
_AlarmType_Object=MibScalar
alarmType=_AlarmType_Object((248,32,100,1,15,4,2),_AlarmType_Type())
alarmType.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmType.setStatus(_A)
_AlarmValue_Type=DisplayString
_AlarmValue_Object=MibScalar
alarmValue=_AlarmValue_Object((248,32,100,1,15,4,3),_AlarmValue_Type())
alarmValue.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmValue.setStatus(_A)
alarm=NotificationType((248,32,100,1,15,4,1))
if mibBuilder.loadTexts:alarm.setStatus(_A)
mibBuilder.exportSymbols('HIRSCHMANN-WLAN-BATC2-MIB',**{'batC2MIB':batC2MIB,'batc2Trap':batc2Trap,'alarm':alarm,'alarmType':alarmType,'alarmValue':alarmValue})