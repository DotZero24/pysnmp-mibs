_O='configurationChangeTrapsEnable'
_N='configChangeTransactionKey'
_M='configChangeNotificationFamilyOid'
_L='read-write'
_K='not-accessible'
_J='configurationChangeFamilyOid'
_I='sysName'
_H='SNMPv2-MIB'
_G='OctetString'
_F='configurationChangeId'
_E='read-only'
_D='accessible-for-notify'
_C='Integer32'
_B='RAD-ConfigChange-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
systemsEvents,=mibBuilder.importSymbols('RAD-GEN-MIB','systemsEvents')
agnt,=mibBuilder.importSymbols('RAD-SMI-MIB','agnt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_H,_I)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
agnConfigChange=ModuleIdentity((1,3,6,1,4,1,164,6,2,75))
_ConfigChange_ObjectIdentity=ObjectIdentity
configChange=_ConfigChange_ObjectIdentity((1,3,6,1,4,1,164,6,2,75,1))
_ConfigurationChangeTable_Object=MibTable
configurationChangeTable=_ConfigurationChangeTable_Object((1,3,6,1,4,1,164,6,2,75,1,1))
if mibBuilder.loadTexts:configurationChangeTable.setStatus(_A)
_ConfigurationChangeEntry_Object=MibTableRow
configurationChangeEntry=_ConfigurationChangeEntry_Object((1,3,6,1,4,1,164,6,2,75,1,1,1))
configurationChangeEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:configurationChangeEntry.setStatus(_A)
_ConfigurationChangeFamilyOid_Type=ObjectIdentifier
_ConfigurationChangeFamilyOid_Object=MibTableColumn
configurationChangeFamilyOid=_ConfigurationChangeFamilyOid_Object((1,3,6,1,4,1,164,6,2,75,1,1,1,1),_ConfigurationChangeFamilyOid_Type())
configurationChangeFamilyOid.setMaxAccess(_K)
if mibBuilder.loadTexts:configurationChangeFamilyOid.setStatus(_A)
_ConfigurationChangeLastChangeId_Type=Unsigned32
_ConfigurationChangeLastChangeId_Object=MibTableColumn
configurationChangeLastChangeId=_ConfigurationChangeLastChangeId_Object((1,3,6,1,4,1,164,6,2,75,1,1,1,2),_ConfigurationChangeLastChangeId_Type())
configurationChangeLastChangeId.setMaxAccess(_E)
if mibBuilder.loadTexts:configurationChangeLastChangeId.setStatus(_A)
class _ConfigurationChangeOIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('tableOID',2),('scalarOID',3)))
_ConfigurationChangeOIDType_Type.__name__=_C
_ConfigurationChangeOIDType_Object=MibTableColumn
configurationChangeOIDType=_ConfigurationChangeOIDType_Object((1,3,6,1,4,1,164,6,2,75,1,1,1,3),_ConfigurationChangeOIDType_Type())
configurationChangeOIDType.setMaxAccess(_E)
if mibBuilder.loadTexts:configurationChangeOIDType.setStatus(_A)
_ConfigurationChangeId_Type=Unsigned32
_ConfigurationChangeId_Object=MibScalar
configurationChangeId=_ConfigurationChangeId_Object((1,3,6,1,4,1,164,6,2,75,1,2),_ConfigurationChangeId_Type())
configurationChangeId.setMaxAccess(_E)
if mibBuilder.loadTexts:configurationChangeId.setStatus(_A)
class _ConfigurationChangeTrapsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('off',2),('on',3)))
_ConfigurationChangeTrapsEnable_Type.__name__=_C
_ConfigurationChangeTrapsEnable_Object=MibScalar
configurationChangeTrapsEnable=_ConfigurationChangeTrapsEnable_Object((1,3,6,1,4,1,164,6,2,75,1,4),_ConfigurationChangeTrapsEnable_Type())
configurationChangeTrapsEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:configurationChangeTrapsEnable.setStatus(_A)
class _ConfigurationChangeEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('start',1),('end',2),('startAndEnd',3),('continue',4)))
_ConfigurationChangeEnd_Type.__name__=_C
_ConfigurationChangeEnd_Object=MibScalar
configurationChangeEnd=_ConfigurationChangeEnd_Object((1,3,6,1,4,1,164,6,2,75,1,5),_ConfigurationChangeEnd_Type())
configurationChangeEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:configurationChangeEnd.setStatus(_A)
_ConfigChangeNotificationTable_Object=MibTable
configChangeNotificationTable=_ConfigChangeNotificationTable_Object((1,3,6,1,4,1,164,6,2,75,1,6))
if mibBuilder.loadTexts:configChangeNotificationTable.setStatus(_A)
_ConfigChangeNotificationEntry_Object=MibTableRow
configChangeNotificationEntry=_ConfigChangeNotificationEntry_Object((1,3,6,1,4,1,164,6,2,75,1,6,1))
configChangeNotificationEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:configChangeNotificationEntry.setStatus(_A)
_ConfigChangeNotificationFamilyOid_Type=ObjectIdentifier
_ConfigChangeNotificationFamilyOid_Object=MibTableColumn
configChangeNotificationFamilyOid=_ConfigChangeNotificationFamilyOid_Object((1,3,6,1,4,1,164,6,2,75,1,6,1,1),_ConfigChangeNotificationFamilyOid_Type())
configChangeNotificationFamilyOid.setMaxAccess(_K)
if mibBuilder.loadTexts:configChangeNotificationFamilyOid.setStatus(_A)
_ConfigChangeNotificationAdd_Type=ObjectIdentifier
_ConfigChangeNotificationAdd_Object=MibTableColumn
configChangeNotificationAdd=_ConfigChangeNotificationAdd_Object((1,3,6,1,4,1,164,6,2,75,1,6,1,2),_ConfigChangeNotificationAdd_Type())
configChangeNotificationAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:configChangeNotificationAdd.setStatus(_A)
_ConfigChangeNotificationChange_Type=ObjectIdentifier
_ConfigChangeNotificationChange_Object=MibTableColumn
configChangeNotificationChange=_ConfigChangeNotificationChange_Object((1,3,6,1,4,1,164,6,2,75,1,6,1,3),_ConfigChangeNotificationChange_Type())
configChangeNotificationChange.setMaxAccess(_D)
if mibBuilder.loadTexts:configChangeNotificationChange.setStatus(_A)
_ConfigChangeNotificationRemove_Type=ObjectIdentifier
_ConfigChangeNotificationRemove_Object=MibTableColumn
configChangeNotificationRemove=_ConfigChangeNotificationRemove_Object((1,3,6,1,4,1,164,6,2,75,1,6,1,4),_ConfigChangeNotificationRemove_Type())
configChangeNotificationRemove.setMaxAccess(_D)
if mibBuilder.loadTexts:configChangeNotificationRemove.setStatus(_A)
class _ConfigChangeTransactionKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ConfigChangeTransactionKey_Type.__name__=_G
_ConfigChangeTransactionKey_Object=MibScalar
configChangeTransactionKey=_ConfigChangeTransactionKey_Object((1,3,6,1,4,1,164,6,2,75,1,7),_ConfigChangeTransactionKey_Type())
configChangeTransactionKey.setMaxAccess(_L)
if mibBuilder.loadTexts:configChangeTransactionKey.setStatus(_A)
systemConfigurationChange=NotificationType((1,3,6,1,4,1,164,6,1,0,79))
systemConfigurationChange.setObjects(*((_B,_F),(_B,_N)))
if mibBuilder.loadTexts:systemConfigurationChange.setStatus(_A)
systemConfigChangeEnableTraps=NotificationType((1,3,6,1,4,1,164,6,1,0,80))
systemConfigChangeEnableTraps.setObjects(*((_H,_I),(_B,_F),(_B,_O)))
if mibBuilder.loadTexts:systemConfigChangeEnableTraps.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'systemConfigurationChange':systemConfigurationChange,'systemConfigChangeEnableTraps':systemConfigChangeEnableTraps,'agnConfigChange':agnConfigChange,'configChange':configChange,'configurationChangeTable':configurationChangeTable,'configurationChangeEntry':configurationChangeEntry,_J:configurationChangeFamilyOid,'configurationChangeLastChangeId':configurationChangeLastChangeId,'configurationChangeOIDType':configurationChangeOIDType,_F:configurationChangeId,_O:configurationChangeTrapsEnable,'configurationChangeEnd':configurationChangeEnd,'configChangeNotificationTable':configChangeNotificationTable,'configChangeNotificationEntry':configChangeNotificationEntry,_M:configChangeNotificationFamilyOid,'configChangeNotificationAdd':configChangeNotificationAdd,'configChangeNotificationChange':configChangeNotificationChange,'configChangeNotificationRemove':configChangeNotificationRemove,_N:configChangeTransactionKey})