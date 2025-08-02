_O='ciscoDiameterSGHostCfgGroup'
_N='cdsgServerStorageType'
_M='cdsgServerRowStatus'
_L='cdsgServerName'
_K='cdsgServerGroupStorageType'
_J='cdsgServerGroupRowStatus'
_I='cdsgServerGroupName'
_H='cdsgServerIndex'
_G='not-accessible'
_F='cdsgServerGroupIndex'
_E='StorageType'
_D='Unsigned32'
_C='read-create'
_B='CISCO-DIAMETER-SG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_E,'TextualConvention')
ciscoDiameterSGMIB=ModuleIdentity((1,3,6,1,4,1,9,10,132))
if mibBuilder.loadTexts:ciscoDiameterSGMIB.setRevisions(('2006-09-06 00:00',))
_CiscoDiameterSGMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDiameterSGMIBNotifs=_CiscoDiameterSGMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,132,0))
_CiscoDiameterSGMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDiameterSGMIBObjects=_CiscoDiameterSGMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,132,1))
_CdsgHostCfgs_ObjectIdentity=ObjectIdentity
cdsgHostCfgs=_CdsgHostCfgs_ObjectIdentity((1,3,6,1,4,1,9,10,132,1,1))
_CdsgServerGroupTable_Object=MibTable
cdsgServerGroupTable=_CdsgServerGroupTable_Object((1,3,6,1,4,1,9,10,132,1,1,1))
if mibBuilder.loadTexts:cdsgServerGroupTable.setStatus(_A)
_CdsgServerGroupEntry_Object=MibTableRow
cdsgServerGroupEntry=_CdsgServerGroupEntry_Object((1,3,6,1,4,1,9,10,132,1,1,1,1))
cdsgServerGroupEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cdsgServerGroupEntry.setStatus(_A)
class _CdsgServerGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdsgServerGroupIndex_Type.__name__=_D
_CdsgServerGroupIndex_Object=MibTableColumn
cdsgServerGroupIndex=_CdsgServerGroupIndex_Object((1,3,6,1,4,1,9,10,132,1,1,1,1,1),_CdsgServerGroupIndex_Type())
cdsgServerGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdsgServerGroupIndex.setStatus(_A)
_CdsgServerGroupName_Type=SnmpAdminString
_CdsgServerGroupName_Object=MibTableColumn
cdsgServerGroupName=_CdsgServerGroupName_Object((1,3,6,1,4,1,9,10,132,1,1,1,1,2),_CdsgServerGroupName_Type())
cdsgServerGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsgServerGroupName.setStatus(_A)
class _CdsgServerGroupStorageType_Type(StorageType):defaultValue=3
_CdsgServerGroupStorageType_Type.__name__=_E
_CdsgServerGroupStorageType_Object=MibTableColumn
cdsgServerGroupStorageType=_CdsgServerGroupStorageType_Object((1,3,6,1,4,1,9,10,132,1,1,1,1,3),_CdsgServerGroupStorageType_Type())
cdsgServerGroupStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsgServerGroupStorageType.setStatus(_A)
_CdsgServerGroupRowStatus_Type=RowStatus
_CdsgServerGroupRowStatus_Object=MibTableColumn
cdsgServerGroupRowStatus=_CdsgServerGroupRowStatus_Object((1,3,6,1,4,1,9,10,132,1,1,1,1,4),_CdsgServerGroupRowStatus_Type())
cdsgServerGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsgServerGroupRowStatus.setStatus(_A)
_CdsgServerTable_Object=MibTable
cdsgServerTable=_CdsgServerTable_Object((1,3,6,1,4,1,9,10,132,1,1,2))
if mibBuilder.loadTexts:cdsgServerTable.setStatus(_A)
_CdsgServerEntry_Object=MibTableRow
cdsgServerEntry=_CdsgServerEntry_Object((1,3,6,1,4,1,9,10,132,1,1,2,1))
cdsgServerEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:cdsgServerEntry.setStatus(_A)
class _CdsgServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdsgServerIndex_Type.__name__=_D
_CdsgServerIndex_Object=MibTableColumn
cdsgServerIndex=_CdsgServerIndex_Object((1,3,6,1,4,1,9,10,132,1,1,2,1,1),_CdsgServerIndex_Type())
cdsgServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdsgServerIndex.setStatus(_A)
_CdsgServerName_Type=SnmpAdminString
_CdsgServerName_Object=MibTableColumn
cdsgServerName=_CdsgServerName_Object((1,3,6,1,4,1,9,10,132,1,1,2,1,2),_CdsgServerName_Type())
cdsgServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsgServerName.setStatus(_A)
class _CdsgServerStorageType_Type(StorageType):defaultValue=3
_CdsgServerStorageType_Type.__name__=_E
_CdsgServerStorageType_Object=MibTableColumn
cdsgServerStorageType=_CdsgServerStorageType_Object((1,3,6,1,4,1,9,10,132,1,1,2,1,3),_CdsgServerStorageType_Type())
cdsgServerStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsgServerStorageType.setStatus(_A)
_CdsgServerRowStatus_Type=RowStatus
_CdsgServerRowStatus_Object=MibTableColumn
cdsgServerRowStatus=_CdsgServerRowStatus_Object((1,3,6,1,4,1,9,10,132,1,1,2,1,4),_CdsgServerRowStatus_Type())
cdsgServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsgServerRowStatus.setStatus(_A)
_CiscoDiameterSGMIBConform_ObjectIdentity=ObjectIdentity
ciscoDiameterSGMIBConform=_CiscoDiameterSGMIBConform_ObjectIdentity((1,3,6,1,4,1,9,10,132,2))
_CiscoDiameterSGMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDiameterSGMIBCompliances=_CiscoDiameterSGMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,132,2,1))
_CiscoDiameterSGMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDiameterSGMIBGroups=_CiscoDiameterSGMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,132,2,2))
ciscoDiameterSGHostCfgGroup=ObjectGroup((1,3,6,1,4,1,9,10,132,2,2,1))
ciscoDiameterSGHostCfgGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoDiameterSGHostCfgGroup.setStatus(_A)
ciscoDiameterSGMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,132,2,1,1))
ciscoDiameterSGMIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoDiameterSGMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDiameterSGMIB':ciscoDiameterSGMIB,'ciscoDiameterSGMIBNotifs':ciscoDiameterSGMIBNotifs,'ciscoDiameterSGMIBObjects':ciscoDiameterSGMIBObjects,'cdsgHostCfgs':cdsgHostCfgs,'cdsgServerGroupTable':cdsgServerGroupTable,'cdsgServerGroupEntry':cdsgServerGroupEntry,_F:cdsgServerGroupIndex,_I:cdsgServerGroupName,_K:cdsgServerGroupStorageType,_J:cdsgServerGroupRowStatus,'cdsgServerTable':cdsgServerTable,'cdsgServerEntry':cdsgServerEntry,_H:cdsgServerIndex,_L:cdsgServerName,_N:cdsgServerStorageType,_M:cdsgServerRowStatus,'ciscoDiameterSGMIBConform':ciscoDiameterSGMIBConform,'ciscoDiameterSGMIBCompliances':ciscoDiameterSGMIBCompliances,'ciscoDiameterSGMIBCompliance':ciscoDiameterSGMIBCompliance,'ciscoDiameterSGMIBGroups':ciscoDiameterSGMIBGroups,_O:ciscoDiameterSGHostCfgGroup})