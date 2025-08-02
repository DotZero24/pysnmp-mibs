_P='etsysConfigChangeFirmwareGroup'
_O='etsysConfigChangeVolatileGroup'
_N='etsysConfigChangeNonVolatileGroup'
_M='etsysConfigChangeFirmwareMethod'
_L='etsysConfigChangeFirmwareTime'
_K='etsysConfigChangeFirmwareCount'
_J='etsysConfigChangeVolatileMethod'
_I='etsysConfigChangeVolatileTime'
_H='etsysConfigChangeVolatileCount'
_G='etsysConfigChangeNonVolatileMethod'
_F='etsysConfigChangeNonVolatileTime'
_E='etsysConfigChangeNonVolatileCount'
_D='SnmpAdminString'
_C='read-only'
_B='ENTERASYS-CONFIGURATION-CHANGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
etsysConfigurationChangeMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,12))
if mibBuilder.loadTexts:etsysConfigurationChangeMIB.setRevisions(('2001-11-26 16:44','2001-08-08 00:00'))
_EtsysConfigChangeNonVolatile_ObjectIdentity=ObjectIdentity
etsysConfigChangeNonVolatile=_EtsysConfigChangeNonVolatile_ObjectIdentity((1,3,6,1,4,1,5624,1,2,12,1))
_EtsysConfigChangeNonVolatileCount_Type=Counter32
_EtsysConfigChangeNonVolatileCount_Object=MibScalar
etsysConfigChangeNonVolatileCount=_EtsysConfigChangeNonVolatileCount_Object((1,3,6,1,4,1,5624,1,2,12,1,1),_EtsysConfigChangeNonVolatileCount_Type())
etsysConfigChangeNonVolatileCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeNonVolatileCount.setStatus(_A)
_EtsysConfigChangeNonVolatileTime_Type=DateAndTime
_EtsysConfigChangeNonVolatileTime_Object=MibScalar
etsysConfigChangeNonVolatileTime=_EtsysConfigChangeNonVolatileTime_Object((1,3,6,1,4,1,5624,1,2,12,1,2),_EtsysConfigChangeNonVolatileTime_Type())
etsysConfigChangeNonVolatileTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeNonVolatileTime.setStatus(_A)
class _EtsysConfigChangeNonVolatileMethod_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysConfigChangeNonVolatileMethod_Type.__name__=_D
_EtsysConfigChangeNonVolatileMethod_Object=MibScalar
etsysConfigChangeNonVolatileMethod=_EtsysConfigChangeNonVolatileMethod_Object((1,3,6,1,4,1,5624,1,2,12,1,3),_EtsysConfigChangeNonVolatileMethod_Type())
etsysConfigChangeNonVolatileMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeNonVolatileMethod.setStatus(_A)
_EtsysConfigChangeVolatile_ObjectIdentity=ObjectIdentity
etsysConfigChangeVolatile=_EtsysConfigChangeVolatile_ObjectIdentity((1,3,6,1,4,1,5624,1,2,12,2))
_EtsysConfigChangeVolatileCount_Type=Counter32
_EtsysConfigChangeVolatileCount_Object=MibScalar
etsysConfigChangeVolatileCount=_EtsysConfigChangeVolatileCount_Object((1,3,6,1,4,1,5624,1,2,12,2,1),_EtsysConfigChangeVolatileCount_Type())
etsysConfigChangeVolatileCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeVolatileCount.setStatus(_A)
_EtsysConfigChangeVolatileTime_Type=DateAndTime
_EtsysConfigChangeVolatileTime_Object=MibScalar
etsysConfigChangeVolatileTime=_EtsysConfigChangeVolatileTime_Object((1,3,6,1,4,1,5624,1,2,12,2,2),_EtsysConfigChangeVolatileTime_Type())
etsysConfigChangeVolatileTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeVolatileTime.setStatus(_A)
class _EtsysConfigChangeVolatileMethod_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysConfigChangeVolatileMethod_Type.__name__=_D
_EtsysConfigChangeVolatileMethod_Object=MibScalar
etsysConfigChangeVolatileMethod=_EtsysConfigChangeVolatileMethod_Object((1,3,6,1,4,1,5624,1,2,12,2,3),_EtsysConfigChangeVolatileMethod_Type())
etsysConfigChangeVolatileMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeVolatileMethod.setStatus(_A)
_EtsysConfigChangeFirmware_ObjectIdentity=ObjectIdentity
etsysConfigChangeFirmware=_EtsysConfigChangeFirmware_ObjectIdentity((1,3,6,1,4,1,5624,1,2,12,3))
_EtsysConfigChangeFirmwareCount_Type=Counter32
_EtsysConfigChangeFirmwareCount_Object=MibScalar
etsysConfigChangeFirmwareCount=_EtsysConfigChangeFirmwareCount_Object((1,3,6,1,4,1,5624,1,2,12,3,1),_EtsysConfigChangeFirmwareCount_Type())
etsysConfigChangeFirmwareCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeFirmwareCount.setStatus(_A)
_EtsysConfigChangeFirmwareTime_Type=DateAndTime
_EtsysConfigChangeFirmwareTime_Object=MibScalar
etsysConfigChangeFirmwareTime=_EtsysConfigChangeFirmwareTime_Object((1,3,6,1,4,1,5624,1,2,12,3,2),_EtsysConfigChangeFirmwareTime_Type())
etsysConfigChangeFirmwareTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeFirmwareTime.setStatus(_A)
class _EtsysConfigChangeFirmwareMethod_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysConfigChangeFirmwareMethod_Type.__name__=_D
_EtsysConfigChangeFirmwareMethod_Object=MibScalar
etsysConfigChangeFirmwareMethod=_EtsysConfigChangeFirmwareMethod_Object((1,3,6,1,4,1,5624,1,2,12,3,3),_EtsysConfigChangeFirmwareMethod_Type())
etsysConfigChangeFirmwareMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigChangeFirmwareMethod.setStatus(_A)
_EtsysConfigChangeConformance_ObjectIdentity=ObjectIdentity
etsysConfigChangeConformance=_EtsysConfigChangeConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,12,4))
_EtsysConfigChangeGroups_ObjectIdentity=ObjectIdentity
etsysConfigChangeGroups=_EtsysConfigChangeGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,12,4,1))
_EtsysConfigChangeCompliances_ObjectIdentity=ObjectIdentity
etsysConfigChangeCompliances=_EtsysConfigChangeCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,12,4,2))
etsysConfigChangeNonVolatileGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,12,4,1,1))
etsysConfigChangeNonVolatileGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:etsysConfigChangeNonVolatileGroup.setStatus(_A)
etsysConfigChangeVolatileGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,12,4,1,2))
etsysConfigChangeVolatileGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:etsysConfigChangeVolatileGroup.setStatus(_A)
etsysConfigChangeFirmwareGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,12,4,1,3))
etsysConfigChangeFirmwareGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:etsysConfigChangeFirmwareGroup.setStatus(_A)
etsysConfigChangeCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,12,4,2,1))
etsysConfigChangeCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:etsysConfigChangeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysConfigurationChangeMIB':etsysConfigurationChangeMIB,'etsysConfigChangeNonVolatile':etsysConfigChangeNonVolatile,_E:etsysConfigChangeNonVolatileCount,_F:etsysConfigChangeNonVolatileTime,_G:etsysConfigChangeNonVolatileMethod,'etsysConfigChangeVolatile':etsysConfigChangeVolatile,_H:etsysConfigChangeVolatileCount,_I:etsysConfigChangeVolatileTime,_J:etsysConfigChangeVolatileMethod,'etsysConfigChangeFirmware':etsysConfigChangeFirmware,_K:etsysConfigChangeFirmwareCount,_L:etsysConfigChangeFirmwareTime,_M:etsysConfigChangeFirmwareMethod,'etsysConfigChangeConformance':etsysConfigChangeConformance,'etsysConfigChangeGroups':etsysConfigChangeGroups,_N:etsysConfigChangeNonVolatileGroup,_O:etsysConfigChangeVolatileGroup,_P:etsysConfigChangeFirmwareGroup,'etsysConfigChangeCompliances':etsysConfigChangeCompliances,'etsysConfigChangeCompliance':etsysConfigChangeCompliance})