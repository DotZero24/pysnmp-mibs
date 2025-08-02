_N='hm2LinkBackupBackupInterfaceStatus'
_M='hm2LinkBackupPrimaryInterfaceStatus'
_L='read-only'
_K='accessible-for-notify'
_J='TruthValue'
_I='Integer32'
_H='SnmpAdminString'
_G='HmEnabledStatus'
_F='HmLinkBackupStatus'
_E='hm2LinkBackupBackupInterface'
_D='hm2LinkBackupPrimaryInterface'
_C='read-create'
_B='HM2-LINK-BACKUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2L2RedundancyMibObjects,=mibBuilder.importSymbols('HM2-L2REDUNDANCY-MIB','hm2L2RedundancyMibObjects')
HmEnabledStatus,=mibBuilder.importSymbols('HM2-TC-MIB',_G)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
hm2LinkBackupMibGroup=ModuleIdentity((1,3,6,1,4,1,248,11,40,1,3))
if mibBuilder.loadTexts:hm2LinkBackupMibGroup.setRevisions(('2013-05-14 00:00',))
class HmLinkBackupStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forwarding',1),('blocking',2),('down',3),('unknown',4)))
_Hm2LinkBackupNotifications_ObjectIdentity=ObjectIdentity
hm2LinkBackupNotifications=_Hm2LinkBackupNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,3,0))
_Hm2LinkBackupObjects_ObjectIdentity=ObjectIdentity
hm2LinkBackupObjects=_Hm2LinkBackupObjects_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,3,1))
_Hm2LinkBackupConfiguration_ObjectIdentity=ObjectIdentity
hm2LinkBackupConfiguration=_Hm2LinkBackupConfiguration_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,3,1,1))
_Hm2LinkBackupGeneralGroup_ObjectIdentity=ObjectIdentity
hm2LinkBackupGeneralGroup=_Hm2LinkBackupGeneralGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,3,1,1,1))
class _Hm2LinkBackupAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2LinkBackupAdminStatus_Type.__name__=_G
_Hm2LinkBackupAdminStatus_Object=MibScalar
hm2LinkBackupAdminStatus=_Hm2LinkBackupAdminStatus_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,1,1),_Hm2LinkBackupAdminStatus_Type())
hm2LinkBackupAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hm2LinkBackupAdminStatus.setStatus(_A)
_Hm2LinkBackupInterfaceGroup_ObjectIdentity=ObjectIdentity
hm2LinkBackupInterfaceGroup=_Hm2LinkBackupInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,3,1,1,2))
_Hm2LinkBackupInterfaceConfigTable_Object=MibTable
hm2LinkBackupInterfaceConfigTable=_Hm2LinkBackupInterfaceConfigTable_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1))
if mibBuilder.loadTexts:hm2LinkBackupInterfaceConfigTable.setStatus(_A)
_Hm2LinkBackupInterfaceConfigEntry_Object=MibTableRow
hm2LinkBackupInterfaceConfigEntry=_Hm2LinkBackupInterfaceConfigEntry_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1))
hm2LinkBackupInterfaceConfigEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:hm2LinkBackupInterfaceConfigEntry.setStatus(_A)
_Hm2LinkBackupPrimaryInterface_Type=InterfaceIndex
_Hm2LinkBackupPrimaryInterface_Object=MibTableColumn
hm2LinkBackupPrimaryInterface=_Hm2LinkBackupPrimaryInterface_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1,1),_Hm2LinkBackupPrimaryInterface_Type())
hm2LinkBackupPrimaryInterface.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2LinkBackupPrimaryInterface.setStatus(_A)
_Hm2LinkBackupBackupInterface_Type=InterfaceIndex
_Hm2LinkBackupBackupInterface_Object=MibTableColumn
hm2LinkBackupBackupInterface=_Hm2LinkBackupBackupInterface_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1,2),_Hm2LinkBackupBackupInterface_Type())
hm2LinkBackupBackupInterface.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2LinkBackupBackupInterface.setStatus(_A)
class _Hm2LinkBackupPrimaryInterfaceStatus_Type(HmLinkBackupStatus):defaultValue=4
_Hm2LinkBackupPrimaryInterfaceStatus_Type.__name__=_F
_Hm2LinkBackupPrimaryInterfaceStatus_Object=MibTableColumn
hm2LinkBackupPrimaryInterfaceStatus=_Hm2LinkBackupPrimaryInterfaceStatus_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1,3),_Hm2LinkBackupPrimaryInterfaceStatus_Type())
hm2LinkBackupPrimaryInterfaceStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:hm2LinkBackupPrimaryInterfaceStatus.setStatus(_A)
class _Hm2LinkBackupBackupInterfaceStatus_Type(HmLinkBackupStatus):defaultValue=4
_Hm2LinkBackupBackupInterfaceStatus_Type.__name__=_F
_Hm2LinkBackupBackupInterfaceStatus_Object=MibTableColumn
hm2LinkBackupBackupInterfaceStatus=_Hm2LinkBackupBackupInterfaceStatus_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1,4),_Hm2LinkBackupBackupInterfaceStatus_Type())
hm2LinkBackupBackupInterfaceStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:hm2LinkBackupBackupInterfaceStatus.setStatus(_A)
class _Hm2LinkBackupFailBackEnable_Type(TruthValue):defaultValue=1
_Hm2LinkBackupFailBackEnable_Type.__name__=_J
_Hm2LinkBackupFailBackEnable_Object=MibTableColumn
hm2LinkBackupFailBackEnable=_Hm2LinkBackupFailBackEnable_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1,5),_Hm2LinkBackupFailBackEnable_Type())
hm2LinkBackupFailBackEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LinkBackupFailBackEnable.setStatus(_A)
class _Hm2LinkBackupFailBackDelay_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,3600))
_Hm2LinkBackupFailBackDelay_Type.__name__=_I
_Hm2LinkBackupFailBackDelay_Object=MibTableColumn
hm2LinkBackupFailBackDelay=_Hm2LinkBackupFailBackDelay_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1,6),_Hm2LinkBackupFailBackDelay_Type())
hm2LinkBackupFailBackDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LinkBackupFailBackDelay.setStatus(_A)
if mibBuilder.loadTexts:hm2LinkBackupFailBackDelay.setUnits('seconds')
class _Hm2LinkBackupDescription_Type(SnmpAdminString):defaultValue=OctetString('')
_Hm2LinkBackupDescription_Type.__name__=_H
_Hm2LinkBackupDescription_Object=MibTableColumn
hm2LinkBackupDescription=_Hm2LinkBackupDescription_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1,7),_Hm2LinkBackupDescription_Type())
hm2LinkBackupDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LinkBackupDescription.setStatus(_A)
_Hm2LinkBackupRowStatus_Type=RowStatus
_Hm2LinkBackupRowStatus_Object=MibTableColumn
hm2LinkBackupRowStatus=_Hm2LinkBackupRowStatus_Object((1,3,6,1,4,1,248,11,40,1,3,1,1,2,1,1,10),_Hm2LinkBackupRowStatus_Type())
hm2LinkBackupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LinkBackupRowStatus.setStatus(_A)
hm2LinkBackupStatusTrap=NotificationType((1,3,6,1,4,1,248,11,40,1,3,0,1))
hm2LinkBackupStatusTrap.setObjects(*((_B,_D),(_B,_E),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hm2LinkBackupStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:HmLinkBackupStatus,'hm2LinkBackupMibGroup':hm2LinkBackupMibGroup,'hm2LinkBackupNotifications':hm2LinkBackupNotifications,'hm2LinkBackupStatusTrap':hm2LinkBackupStatusTrap,'hm2LinkBackupObjects':hm2LinkBackupObjects,'hm2LinkBackupConfiguration':hm2LinkBackupConfiguration,'hm2LinkBackupGeneralGroup':hm2LinkBackupGeneralGroup,'hm2LinkBackupAdminStatus':hm2LinkBackupAdminStatus,'hm2LinkBackupInterfaceGroup':hm2LinkBackupInterfaceGroup,'hm2LinkBackupInterfaceConfigTable':hm2LinkBackupInterfaceConfigTable,'hm2LinkBackupInterfaceConfigEntry':hm2LinkBackupInterfaceConfigEntry,_D:hm2LinkBackupPrimaryInterface,_E:hm2LinkBackupBackupInterface,_M:hm2LinkBackupPrimaryInterfaceStatus,_N:hm2LinkBackupBackupInterfaceStatus,'hm2LinkBackupFailBackEnable':hm2LinkBackupFailBackEnable,'hm2LinkBackupFailBackDelay':hm2LinkBackupFailBackDelay,'hm2LinkBackupDescription':hm2LinkBackupDescription,'hm2LinkBackupRowStatus':hm2LinkBackupRowStatus})