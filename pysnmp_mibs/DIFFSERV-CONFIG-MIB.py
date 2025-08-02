_O='diffServConfigMIBConfigGroup'
_N='diffServConfigStatus'
_M='diffServConfigStorage'
_L='diffServConfigStart'
_K='diffServConfigLastChange'
_J='diffServConfigOwner'
_I='diffServConfigDescr'
_H='diffServConfigId'
_G='StorageType'
_F='RowStatus'
_E='RowPointer'
_D='SnmpAdminString'
_C='read-create'
_B='DIFFSERV-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2','zeroDotZero')
DateAndTime,DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress',_E,_F,_G,'TextualConvention')
diffServConfigMib=ModuleIdentity((1,3,6,1,2,1,108))
if mibBuilder.loadTexts:diffServConfigMib.setRevisions(('2004-01-22 00:00',))
_DiffServConfigMIBObjects_ObjectIdentity=ObjectIdentity
diffServConfigMIBObjects=_DiffServConfigMIBObjects_ObjectIdentity((1,3,6,1,2,1,108,1))
_DiffServConfigTable_Object=MibTable
diffServConfigTable=_DiffServConfigTable_Object((1,3,6,1,2,1,108,1,2))
if mibBuilder.loadTexts:diffServConfigTable.setStatus(_A)
_DiffServConfigEntry_Object=MibTableRow
diffServConfigEntry=_DiffServConfigEntry_Object((1,3,6,1,2,1,108,1,2,1))
diffServConfigEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:diffServConfigEntry.setStatus(_A)
class _DiffServConfigId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,116))
_DiffServConfigId_Type.__name__=_D
_DiffServConfigId_Object=MibTableColumn
diffServConfigId=_DiffServConfigId_Object((1,3,6,1,2,1,108,1,2,1,1),_DiffServConfigId_Type())
diffServConfigId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:diffServConfigId.setStatus(_A)
_DiffServConfigDescr_Type=SnmpAdminString
_DiffServConfigDescr_Object=MibTableColumn
diffServConfigDescr=_DiffServConfigDescr_Object((1,3,6,1,2,1,108,1,2,1,2),_DiffServConfigDescr_Type())
diffServConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServConfigDescr.setStatus(_A)
_DiffServConfigOwner_Type=SnmpAdminString
_DiffServConfigOwner_Object=MibTableColumn
diffServConfigOwner=_DiffServConfigOwner_Object((1,3,6,1,2,1,108,1,2,1,3),_DiffServConfigOwner_Type())
diffServConfigOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServConfigOwner.setStatus(_A)
_DiffServConfigLastChange_Type=DateAndTime
_DiffServConfigLastChange_Object=MibTableColumn
diffServConfigLastChange=_DiffServConfigLastChange_Object((1,3,6,1,2,1,108,1,2,1,4),_DiffServConfigLastChange_Type())
diffServConfigLastChange.setMaxAccess('read-only')
if mibBuilder.loadTexts:diffServConfigLastChange.setStatus(_A)
class _DiffServConfigStart_Type(RowPointer):defaultValue=0,0
_DiffServConfigStart_Type.__name__=_E
_DiffServConfigStart_Object=MibTableColumn
diffServConfigStart=_DiffServConfigStart_Object((1,3,6,1,2,1,108,1,2,1,5),_DiffServConfigStart_Type())
diffServConfigStart.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServConfigStart.setStatus(_A)
class _DiffServConfigStorage_Type(StorageType):defaultValue=3
_DiffServConfigStorage_Type.__name__=_G
_DiffServConfigStorage_Object=MibTableColumn
diffServConfigStorage=_DiffServConfigStorage_Object((1,3,6,1,2,1,108,1,2,1,6),_DiffServConfigStorage_Type())
diffServConfigStorage.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServConfigStorage.setStatus(_A)
class _DiffServConfigStatus_Type(RowStatus):defaultValue=2
_DiffServConfigStatus_Type.__name__=_F
_DiffServConfigStatus_Object=MibTableColumn
diffServConfigStatus=_DiffServConfigStatus_Object((1,3,6,1,2,1,108,1,2,1,7),_DiffServConfigStatus_Type())
diffServConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServConfigStatus.setStatus(_A)
_DiffServConfigMIBConformance_ObjectIdentity=ObjectIdentity
diffServConfigMIBConformance=_DiffServConfigMIBConformance_ObjectIdentity((1,3,6,1,2,1,108,2))
_DiffServConfigMIBCompliances_ObjectIdentity=ObjectIdentity
diffServConfigMIBCompliances=_DiffServConfigMIBCompliances_ObjectIdentity((1,3,6,1,2,1,108,2,1))
_DiffServConfigMIBGroups_ObjectIdentity=ObjectIdentity
diffServConfigMIBGroups=_DiffServConfigMIBGroups_ObjectIdentity((1,3,6,1,2,1,108,2,2))
diffServConfigMIBConfigGroup=ObjectGroup((1,3,6,1,2,1,108,2,2,1))
diffServConfigMIBConfigGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:diffServConfigMIBConfigGroup.setStatus(_A)
diffServConfigMIBFullCompliance=ModuleCompliance((1,3,6,1,2,1,108,2,1,1))
diffServConfigMIBFullCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:diffServConfigMIBFullCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'diffServConfigMib':diffServConfigMib,'diffServConfigMIBObjects':diffServConfigMIBObjects,'diffServConfigTable':diffServConfigTable,'diffServConfigEntry':diffServConfigEntry,_H:diffServConfigId,_I:diffServConfigDescr,_J:diffServConfigOwner,_K:diffServConfigLastChange,_L:diffServConfigStart,_M:diffServConfigStorage,_N:diffServConfigStatus,'diffServConfigMIBConformance':diffServConfigMIBConformance,'diffServConfigMIBCompliances':diffServConfigMIBCompliances,'diffServConfigMIBFullCompliance':diffServConfigMIBFullCompliance,'diffServConfigMIBGroups':diffServConfigMIBGroups,_O:diffServConfigMIBConfigGroup})