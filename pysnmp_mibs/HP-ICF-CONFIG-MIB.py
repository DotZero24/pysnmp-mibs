_P='hpicfConfigFilesGroup'
_O='hpicfConfigScalarsGroup'
_N='hpicfConfigTimestamp'
_M='hpicfConfigFileName'
_L='hpicfConfigRecoveryMode'
_K='hpicfConfigRestoreStatus'
_J='hpicfConfigStartupConfigSHA'
_I='hpicfConfigRunningConfigSHA'
_H='hpicfConfigRestoreFileName'
_G='hpicfConfigFilePos'
_F='read-write'
_E='Integer32'
_D='read-only'
_C='OctetString'
_B='HP-ICF-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
hpicfConfig=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136))
if mibBuilder.loadTexts:hpicfConfig.setRevisions(('2017-10-07 00:00','2017-04-19 00:00','2017-03-08 00:00'))
_HpicfConfigNotifications_ObjectIdentity=ObjectIdentity
hpicfConfigNotifications=_HpicfConfigNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,0))
_HpicfConfigScalar_ObjectIdentity=ObjectIdentity
hpicfConfigScalar=_HpicfConfigScalar_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,1))
_HpicfConfigGlobals_ObjectIdentity=ObjectIdentity
hpicfConfigGlobals=_HpicfConfigGlobals_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,2))
_HpicfConfigConformance_ObjectIdentity=ObjectIdentity
hpicfConfigConformance=_HpicfConfigConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,3))
_HpicfConfigGroups_ObjectIdentity=ObjectIdentity
hpicfConfigGroups=_HpicfConfigGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,3,1))
_HpicfConfigMIBCompliances_ObjectIdentity=ObjectIdentity
hpicfConfigMIBCompliances=_HpicfConfigMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,3,2))
_HpicfConfigConfig_ObjectIdentity=ObjectIdentity
hpicfConfigConfig=_HpicfConfigConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,4))
_HpicfConfigObjects_ObjectIdentity=ObjectIdentity
hpicfConfigObjects=_HpicfConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,4,1))
class _HpicfConfigRestoreFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfConfigRestoreFileName_Type.__name__=_C
_HpicfConfigRestoreFileName_Object=MibScalar
hpicfConfigRestoreFileName=_HpicfConfigRestoreFileName_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,1,1),_HpicfConfigRestoreFileName_Type())
hpicfConfigRestoreFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfConfigRestoreFileName.setStatus(_A)
class _HpicfConfigRunningConfigSHA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfConfigRunningConfigSHA_Type.__name__=_C
_HpicfConfigRunningConfigSHA_Object=MibScalar
hpicfConfigRunningConfigSHA=_HpicfConfigRunningConfigSHA_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,1,2),_HpicfConfigRunningConfigSHA_Type())
hpicfConfigRunningConfigSHA.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfConfigRunningConfigSHA.setStatus(_A)
class _HpicfConfigStartupConfigSHA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfConfigStartupConfigSHA_Type.__name__=_C
_HpicfConfigStartupConfigSHA_Object=MibScalar
hpicfConfigStartupConfigSHA=_HpicfConfigStartupConfigSHA_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,1,3),_HpicfConfigStartupConfigSHA_Type())
hpicfConfigStartupConfigSHA.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfConfigStartupConfigSHA.setStatus(_A)
class _HpicfConfigRestoreStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notYetRun',1),('inProgress',2),('success',3),('failed',4)))
_HpicfConfigRestoreStatus_Type.__name__=_E
_HpicfConfigRestoreStatus_Object=MibScalar
hpicfConfigRestoreStatus=_HpicfConfigRestoreStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,1,4),_HpicfConfigRestoreStatus_Type())
hpicfConfigRestoreStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfConfigRestoreStatus.setStatus(_A)
class _HpicfConfigRecoveryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpicfConfigRecoveryMode_Type.__name__=_E
_HpicfConfigRecoveryMode_Object=MibScalar
hpicfConfigRecoveryMode=_HpicfConfigRecoveryMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,1,5),_HpicfConfigRecoveryMode_Type())
hpicfConfigRecoveryMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfConfigRecoveryMode.setStatus(_A)
_HpicfConfigFilesObjects_ObjectIdentity=ObjectIdentity
hpicfConfigFilesObjects=_HpicfConfigFilesObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,136,4,2))
_HpicfConfigFilesTable_Object=MibTable
hpicfConfigFilesTable=_HpicfConfigFilesTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,2,1))
if mibBuilder.loadTexts:hpicfConfigFilesTable.setStatus(_A)
_HpicfConfigFilesEntry_Object=MibTableRow
hpicfConfigFilesEntry=_HpicfConfigFilesEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,2,1,1))
hpicfConfigFilesEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpicfConfigFilesEntry.setStatus(_A)
_HpicfConfigFilePos_Type=Unsigned32
_HpicfConfigFilePos_Object=MibTableColumn
hpicfConfigFilePos=_HpicfConfigFilePos_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,2,1,1,1),_HpicfConfigFilePos_Type())
hpicfConfigFilePos.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfConfigFilePos.setStatus(_A)
class _HpicfConfigFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfConfigFileName_Type.__name__=_C
_HpicfConfigFileName_Object=MibTableColumn
hpicfConfigFileName=_HpicfConfigFileName_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,2,1,1,2),_HpicfConfigFileName_Type())
hpicfConfigFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfConfigFileName.setStatus(_A)
_HpicfConfigTimestamp_Type=DateAndTime
_HpicfConfigTimestamp_Object=MibTableColumn
hpicfConfigTimestamp=_HpicfConfigTimestamp_Object((1,3,6,1,4,1,11,2,14,11,5,1,136,4,2,1,1,3),_HpicfConfigTimestamp_Type())
hpicfConfigTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfConfigTimestamp.setStatus(_A)
hpicfConfigScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,136,3,1,1))
hpicfConfigScalarsGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpicfConfigScalarsGroup.setStatus(_A)
hpicfConfigFilesGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,136,3,1,2))
hpicfConfigFilesGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpicfConfigFilesGroup.setStatus(_A)
hpicfConfigMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,136,3,2,1))
hpicfConfigMIBCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hpicfConfigMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfConfig':hpicfConfig,'hpicfConfigNotifications':hpicfConfigNotifications,'hpicfConfigScalar':hpicfConfigScalar,'hpicfConfigGlobals':hpicfConfigGlobals,'hpicfConfigConformance':hpicfConfigConformance,'hpicfConfigGroups':hpicfConfigGroups,_O:hpicfConfigScalarsGroup,_P:hpicfConfigFilesGroup,'hpicfConfigMIBCompliances':hpicfConfigMIBCompliances,'hpicfConfigMIBCompliance':hpicfConfigMIBCompliance,'hpicfConfigConfig':hpicfConfigConfig,'hpicfConfigObjects':hpicfConfigObjects,_H:hpicfConfigRestoreFileName,_I:hpicfConfigRunningConfigSHA,_J:hpicfConfigStartupConfigSHA,_K:hpicfConfigRestoreStatus,_L:hpicfConfigRecoveryMode,'hpicfConfigFilesObjects':hpicfConfigFilesObjects,'hpicfConfigFilesTable':hpicfConfigFilesTable,'hpicfConfigFilesEntry':hpicfConfigFilesEntry,_G:hpicfConfigFilePos,_M:hpicfConfigFileName,_N:hpicfConfigTimestamp})