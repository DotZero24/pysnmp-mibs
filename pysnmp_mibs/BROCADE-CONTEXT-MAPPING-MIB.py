_J='brocadeContextMapConfigGroup'
_I='bcmContextMappingRowStatus'
_H='bcmContextMappingStorageType'
_G='bcmContextMappingVrfName'
_F='bcmContextMappingVacmContextName'
_E='StorageType'
_D='read-only'
_C='SnmpAdminString'
_B='BROCADE-CONTEXT-MAPPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_E,'TextualConvention')
brocadeContextMappingMIB=ModuleIdentity((1,3,6,1,4,1,1588,3,1,7))
if mibBuilder.loadTexts:brocadeContextMappingMIB.setRevisions(('2015-06-18 00:00',))
_BContextMapMIBNotifs_ObjectIdentity=ObjectIdentity
bContextMapMIBNotifs=_BContextMapMIBNotifs_ObjectIdentity((1,3,6,1,4,1,1588,3,1,7,0))
_BContextMapMIBObjects_ObjectIdentity=ObjectIdentity
bContextMapMIBObjects=_BContextMapMIBObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,7,1))
_BcmContexMapConfig_ObjectIdentity=ObjectIdentity
bcmContexMapConfig=_BcmContexMapConfig_ObjectIdentity((1,3,6,1,4,1,1588,3,1,7,1,1))
_BcmContextMappingTable_Object=MibTable
bcmContextMappingTable=_BcmContextMappingTable_Object((1,3,6,1,4,1,1588,3,1,7,1,1,1))
if mibBuilder.loadTexts:bcmContextMappingTable.setStatus(_A)
_BcmContextMappingEntry_Object=MibTableRow
bcmContextMappingEntry=_BcmContextMappingEntry_Object((1,3,6,1,4,1,1588,3,1,7,1,1,1,1))
bcmContextMappingEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:bcmContextMappingEntry.setStatus(_A)
class _BcmContextMappingVacmContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcmContextMappingVacmContextName_Type.__name__=_C
_BcmContextMappingVacmContextName_Object=MibTableColumn
bcmContextMappingVacmContextName=_BcmContextMappingVacmContextName_Object((1,3,6,1,4,1,1588,3,1,7,1,1,1,1,1),_BcmContextMappingVacmContextName_Type())
bcmContextMappingVacmContextName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bcmContextMappingVacmContextName.setStatus(_A)
class _BcmContextMappingVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcmContextMappingVrfName_Type.__name__=_C
_BcmContextMappingVrfName_Object=MibTableColumn
bcmContextMappingVrfName=_BcmContextMappingVrfName_Object((1,3,6,1,4,1,1588,3,1,7,1,1,1,1,2),_BcmContextMappingVrfName_Type())
bcmContextMappingVrfName.setMaxAccess(_D)
if mibBuilder.loadTexts:bcmContextMappingVrfName.setStatus(_A)
class _BcmContextMappingStorageType_Type(StorageType):defaultValue=3
_BcmContextMappingStorageType_Type.__name__=_E
_BcmContextMappingStorageType_Object=MibTableColumn
bcmContextMappingStorageType=_BcmContextMappingStorageType_Object((1,3,6,1,4,1,1588,3,1,7,1,1,1,1,3),_BcmContextMappingStorageType_Type())
bcmContextMappingStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:bcmContextMappingStorageType.setStatus(_A)
_BcmContextMappingRowStatus_Type=RowStatus
_BcmContextMappingRowStatus_Object=MibTableColumn
bcmContextMappingRowStatus=_BcmContextMappingRowStatus_Object((1,3,6,1,4,1,1588,3,1,7,1,1,1,1,4),_BcmContextMappingRowStatus_Type())
bcmContextMappingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bcmContextMappingRowStatus.setStatus(_A)
_BContextMapMIBConform_ObjectIdentity=ObjectIdentity
bContextMapMIBConform=_BContextMapMIBConform_ObjectIdentity((1,3,6,1,4,1,1588,3,1,7,2))
_BrocadeContextMapMIBCompliances_ObjectIdentity=ObjectIdentity
brocadeContextMapMIBCompliances=_BrocadeContextMapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1588,3,1,7,2,1))
_BrocadeContextMapMIBGroups_ObjectIdentity=ObjectIdentity
brocadeContextMapMIBGroups=_BrocadeContextMapMIBGroups_ObjectIdentity((1,3,6,1,4,1,1588,3,1,7,2,2))
brocadeContextMapConfigGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,7,2,2,1))
brocadeContextMapConfigGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:brocadeContextMapConfigGroup.setStatus(_A)
brocadeContextMapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1588,3,1,7,2,1,1))
brocadeContextMapMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:brocadeContextMapMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'brocadeContextMappingMIB':brocadeContextMappingMIB,'bContextMapMIBNotifs':bContextMapMIBNotifs,'bContextMapMIBObjects':bContextMapMIBObjects,'bcmContexMapConfig':bcmContexMapConfig,'bcmContextMappingTable':bcmContextMappingTable,'bcmContextMappingEntry':bcmContextMappingEntry,_F:bcmContextMappingVacmContextName,_G:bcmContextMappingVrfName,_H:bcmContextMappingStorageType,_I:bcmContextMappingRowStatus,'bContextMapMIBConform':bContextMapMIBConform,'brocadeContextMapMIBCompliances':brocadeContextMapMIBCompliances,'brocadeContextMapMIBCompliance':brocadeContextMapMIBCompliance,'brocadeContextMapMIBGroups':brocadeContextMapMIBGroups,_J:brocadeContextMapConfigGroup})