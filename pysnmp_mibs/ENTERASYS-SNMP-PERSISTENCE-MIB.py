_L='etsysSnmpPersistenceGroup'
_K='etsysSnmpPersistenceErrorTime'
_J='etsysSnmpPersistenceError'
_I='etsysSnmpPersistenceStatusTime'
_H='etsysSnmpPersistenceStatus'
_G='etsysSnmpPersistenceSave'
_F='etsysSnmpPersistenceMode'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ENTERASYS-SNMP-PERSISTENCE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
etsysSnmpPersistenceMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,24))
if mibBuilder.loadTexts:etsysSnmpPersistenceMIB.setRevisions(('2002-09-09 20:22',))
_EtsysSnmpPersistenceObjects_ObjectIdentity=ObjectIdentity
etsysSnmpPersistenceObjects=_EtsysSnmpPersistenceObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,24,1))
class _EtsysSnmpPersistenceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmpNormalSave',1),('pushButtonSave',2),('timeDelayedSave',3)))
_EtsysSnmpPersistenceMode_Type.__name__=_C
_EtsysSnmpPersistenceMode_Object=MibScalar
etsysSnmpPersistenceMode=_EtsysSnmpPersistenceMode_Object((1,3,6,1,4,1,5624,1,2,24,1,1),_EtsysSnmpPersistenceMode_Type())
etsysSnmpPersistenceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSnmpPersistenceMode.setStatus(_A)
class _EtsysSnmpPersistenceSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nop',1),('save',2)))
_EtsysSnmpPersistenceSave_Type.__name__=_C
_EtsysSnmpPersistenceSave_Object=MibScalar
etsysSnmpPersistenceSave=_EtsysSnmpPersistenceSave_Object((1,3,6,1,4,1,5624,1,2,24,1,2),_EtsysSnmpPersistenceSave_Type())
etsysSnmpPersistenceSave.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSnmpPersistenceSave.setStatus(_A)
class _EtsysSnmpPersistenceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('unsavedChanges',2),('savingChanges',3),('saveSucceeded',4),('saveFailed',5)))
_EtsysSnmpPersistenceStatus_Type.__name__=_C
_EtsysSnmpPersistenceStatus_Object=MibScalar
etsysSnmpPersistenceStatus=_EtsysSnmpPersistenceStatus_Object((1,3,6,1,4,1,5624,1,2,24,1,3),_EtsysSnmpPersistenceStatus_Type())
etsysSnmpPersistenceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSnmpPersistenceStatus.setStatus(_A)
_EtsysSnmpPersistenceStatusTime_Type=TimeTicks
_EtsysSnmpPersistenceStatusTime_Object=MibScalar
etsysSnmpPersistenceStatusTime=_EtsysSnmpPersistenceStatusTime_Object((1,3,6,1,4,1,5624,1,2,24,1,4),_EtsysSnmpPersistenceStatusTime_Type())
etsysSnmpPersistenceStatusTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSnmpPersistenceStatusTime.setStatus(_A)
_EtsysSnmpPersistenceError_Type=SnmpAdminString
_EtsysSnmpPersistenceError_Object=MibScalar
etsysSnmpPersistenceError=_EtsysSnmpPersistenceError_Object((1,3,6,1,4,1,5624,1,2,24,1,5),_EtsysSnmpPersistenceError_Type())
etsysSnmpPersistenceError.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSnmpPersistenceError.setStatus(_A)
_EtsysSnmpPersistenceErrorTime_Type=DateAndTime
_EtsysSnmpPersistenceErrorTime_Object=MibScalar
etsysSnmpPersistenceErrorTime=_EtsysSnmpPersistenceErrorTime_Object((1,3,6,1,4,1,5624,1,2,24,1,6),_EtsysSnmpPersistenceErrorTime_Type())
etsysSnmpPersistenceErrorTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSnmpPersistenceErrorTime.setStatus(_A)
_EtsysSnmpPersistenceConformance_ObjectIdentity=ObjectIdentity
etsysSnmpPersistenceConformance=_EtsysSnmpPersistenceConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,24,2))
_EtsysSnmpPersistenceGroups_ObjectIdentity=ObjectIdentity
etsysSnmpPersistenceGroups=_EtsysSnmpPersistenceGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,24,2,1))
_EtsysSnmpPersistenceCompliances_ObjectIdentity=ObjectIdentity
etsysSnmpPersistenceCompliances=_EtsysSnmpPersistenceCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,24,2,2))
etsysSnmpPersistenceGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,24,2,1,1))
etsysSnmpPersistenceGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:etsysSnmpPersistenceGroup.setStatus(_A)
etsysSnmpPersistenceCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,24,2,2,1))
etsysSnmpPersistenceCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:etsysSnmpPersistenceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysSnmpPersistenceMIB':etsysSnmpPersistenceMIB,'etsysSnmpPersistenceObjects':etsysSnmpPersistenceObjects,_F:etsysSnmpPersistenceMode,_G:etsysSnmpPersistenceSave,_H:etsysSnmpPersistenceStatus,_I:etsysSnmpPersistenceStatusTime,_J:etsysSnmpPersistenceError,_K:etsysSnmpPersistenceErrorTime,'etsysSnmpPersistenceConformance':etsysSnmpPersistenceConformance,'etsysSnmpPersistenceGroups':etsysSnmpPersistenceGroups,_L:etsysSnmpPersistenceGroup,'etsysSnmpPersistenceCompliances':etsysSnmpPersistenceCompliances,'etsysSnmpPersistenceCompliance':etsysSnmpPersistenceCompliance})