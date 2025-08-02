_U='cfmLrGroup'
_T='cfmPoolGroup'
_S='cfmGenInfoGroup'
_R='cfmLrHighWaterInuseFgids'
_Q='cfmLrInuseFgids'
_P='cfmPoolHighWaterInuseFgids'
_O='cfmPoolInuseFgids'
_N='cfmPoolTotalFgids'
_M='cfmPoolType'
_L='cfmPoolName'
_K='cfmGenInfoHighWaterInuseFgids'
_J='cfmGenInfoInuseFgids'
_I='cfmGenInfoTotalFgids'
_H='cfmPoolId'
_G='Integer32'
_F='entLogicalIndex'
_E='ENTITY-MIB'
_D='fgid'
_C='read-only'
_B='CISCO-FABRIC-MCAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entLogicalIndex,=mibBuilder.importSymbols(_E,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoFabricMcastMIB=ModuleIdentity((1,3,6,1,4,1,9,9,255))
if mibBuilder.loadTexts:ciscoFabricMcastMIB.setRevisions(('2002-08-20 00:00',))
class CfmPoolIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CiscoFabricMcastMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFabricMcastMIBNotifs=_CiscoFabricMcastMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,255,0))
_CiscoFabricMcastMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFabricMcastMIBObjects=_CiscoFabricMcastMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,255,1))
_CfmGeneral_ObjectIdentity=ObjectIdentity
cfmGeneral=_CfmGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,255,1,1))
_CfmGenInfoTotalFgids_Type=Gauge32
_CfmGenInfoTotalFgids_Object=MibScalar
cfmGenInfoTotalFgids=_CfmGenInfoTotalFgids_Object((1,3,6,1,4,1,9,9,255,1,1,1),_CfmGenInfoTotalFgids_Type())
cfmGenInfoTotalFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmGenInfoTotalFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmGenInfoTotalFgids.setUnits(_D)
_CfmGenInfoInuseFgids_Type=Gauge32
_CfmGenInfoInuseFgids_Object=MibScalar
cfmGenInfoInuseFgids=_CfmGenInfoInuseFgids_Object((1,3,6,1,4,1,9,9,255,1,1,2),_CfmGenInfoInuseFgids_Type())
cfmGenInfoInuseFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmGenInfoInuseFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmGenInfoInuseFgids.setUnits(_D)
_CfmGenInfoHighWaterInuseFgids_Type=Gauge32
_CfmGenInfoHighWaterInuseFgids_Object=MibScalar
cfmGenInfoHighWaterInuseFgids=_CfmGenInfoHighWaterInuseFgids_Object((1,3,6,1,4,1,9,9,255,1,1,3),_CfmGenInfoHighWaterInuseFgids_Type())
cfmGenInfoHighWaterInuseFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmGenInfoHighWaterInuseFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmGenInfoHighWaterInuseFgids.setUnits(_D)
_CfmPool_ObjectIdentity=ObjectIdentity
cfmPool=_CfmPool_ObjectIdentity((1,3,6,1,4,1,9,9,255,1,2))
_CfmPoolTable_Object=MibTable
cfmPoolTable=_CfmPoolTable_Object((1,3,6,1,4,1,9,9,255,1,2,1))
if mibBuilder.loadTexts:cfmPoolTable.setStatus(_A)
_CfmPoolEntry_Object=MibTableRow
cfmPoolEntry=_CfmPoolEntry_Object((1,3,6,1,4,1,9,9,255,1,2,1,1))
cfmPoolEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cfmPoolEntry.setStatus(_A)
_CfmPoolId_Type=CfmPoolIndex
_CfmPoolId_Object=MibTableColumn
cfmPoolId=_CfmPoolId_Object((1,3,6,1,4,1,9,9,255,1,2,1,1,1),_CfmPoolId_Type())
cfmPoolId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfmPoolId.setStatus(_A)
_CfmPoolName_Type=SnmpAdminString
_CfmPoolName_Object=MibTableColumn
cfmPoolName=_CfmPoolName_Object((1,3,6,1,4,1,9,9,255,1,2,1,1,2),_CfmPoolName_Type())
cfmPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmPoolName.setStatus(_A)
class _CfmPoolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shared',1),('dedicated',2)))
_CfmPoolType_Type.__name__=_G
_CfmPoolType_Object=MibTableColumn
cfmPoolType=_CfmPoolType_Object((1,3,6,1,4,1,9,9,255,1,2,1,1,3),_CfmPoolType_Type())
cfmPoolType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmPoolType.setStatus(_A)
_CfmPoolTotalFgids_Type=Gauge32
_CfmPoolTotalFgids_Object=MibTableColumn
cfmPoolTotalFgids=_CfmPoolTotalFgids_Object((1,3,6,1,4,1,9,9,255,1,2,1,1,4),_CfmPoolTotalFgids_Type())
cfmPoolTotalFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmPoolTotalFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmPoolTotalFgids.setUnits(_D)
_CfmPoolInuseFgids_Type=Gauge32
_CfmPoolInuseFgids_Object=MibTableColumn
cfmPoolInuseFgids=_CfmPoolInuseFgids_Object((1,3,6,1,4,1,9,9,255,1,2,1,1,5),_CfmPoolInuseFgids_Type())
cfmPoolInuseFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmPoolInuseFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmPoolInuseFgids.setUnits(_D)
_CfmPoolHighWaterInuseFgids_Type=Gauge32
_CfmPoolHighWaterInuseFgids_Object=MibTableColumn
cfmPoolHighWaterInuseFgids=_CfmPoolHighWaterInuseFgids_Object((1,3,6,1,4,1,9,9,255,1,2,1,1,6),_CfmPoolHighWaterInuseFgids_Type())
cfmPoolHighWaterInuseFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmPoolHighWaterInuseFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmPoolHighWaterInuseFgids.setUnits(_D)
_CfmLr_ObjectIdentity=ObjectIdentity
cfmLr=_CfmLr_ObjectIdentity((1,3,6,1,4,1,9,9,255,1,3))
_CfmLrTable_Object=MibTable
cfmLrTable=_CfmLrTable_Object((1,3,6,1,4,1,9,9,255,1,3,1))
if mibBuilder.loadTexts:cfmLrTable.setStatus(_A)
_CfmLrEntry_Object=MibTableRow
cfmLrEntry=_CfmLrEntry_Object((1,3,6,1,4,1,9,9,255,1,3,1,1))
cfmLrEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cfmLrEntry.setStatus(_A)
_CfmLrInuseFgids_Type=Gauge32
_CfmLrInuseFgids_Object=MibTableColumn
cfmLrInuseFgids=_CfmLrInuseFgids_Object((1,3,6,1,4,1,9,9,255,1,3,1,1,1),_CfmLrInuseFgids_Type())
cfmLrInuseFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmLrInuseFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmLrInuseFgids.setUnits(_D)
_CfmLrHighWaterInuseFgids_Type=Gauge32
_CfmLrHighWaterInuseFgids_Object=MibTableColumn
cfmLrHighWaterInuseFgids=_CfmLrHighWaterInuseFgids_Object((1,3,6,1,4,1,9,9,255,1,3,1,1,2),_CfmLrHighWaterInuseFgids_Type())
cfmLrHighWaterInuseFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmLrHighWaterInuseFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmLrHighWaterInuseFgids.setUnits(_D)
_CiscoFabricMcastMIBConform_ObjectIdentity=ObjectIdentity
ciscoFabricMcastMIBConform=_CiscoFabricMcastMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,255,2))
_CfmMIBCompliances_ObjectIdentity=ObjectIdentity
cfmMIBCompliances=_CfmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,255,2,1))
_CfmMIBGroups_ObjectIdentity=ObjectIdentity
cfmMIBGroups=_CfmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,255,2,2))
cfmGenInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,255,2,2,1))
cfmGenInfoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cfmGenInfoGroup.setStatus(_A)
cfmPoolGroup=ObjectGroup((1,3,6,1,4,1,9,9,255,2,2,2))
cfmPoolGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cfmPoolGroup.setStatus(_A)
cfmLrGroup=ObjectGroup((1,3,6,1,4,1,9,9,255,2,2,3))
cfmLrGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cfmLrGroup.setStatus(_A)
cfmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,255,2,1,1))
cfmMIBCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cfmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CfmPoolIndex':CfmPoolIndex,'ciscoFabricMcastMIB':ciscoFabricMcastMIB,'ciscoFabricMcastMIBNotifs':ciscoFabricMcastMIBNotifs,'ciscoFabricMcastMIBObjects':ciscoFabricMcastMIBObjects,'cfmGeneral':cfmGeneral,_I:cfmGenInfoTotalFgids,_J:cfmGenInfoInuseFgids,_K:cfmGenInfoHighWaterInuseFgids,'cfmPool':cfmPool,'cfmPoolTable':cfmPoolTable,'cfmPoolEntry':cfmPoolEntry,_H:cfmPoolId,_L:cfmPoolName,_M:cfmPoolType,_N:cfmPoolTotalFgids,_O:cfmPoolInuseFgids,_P:cfmPoolHighWaterInuseFgids,'cfmLr':cfmLr,'cfmLrTable':cfmLrTable,'cfmLrEntry':cfmLrEntry,_Q:cfmLrInuseFgids,_R:cfmLrHighWaterInuseFgids,'ciscoFabricMcastMIBConform':ciscoFabricMcastMIBConform,'cfmMIBCompliances':cfmMIBCompliances,'cfmMIBCompliance':cfmMIBCompliance,'cfmMIBGroups':cfmMIBGroups,_S:cfmGenInfoGroup,_T:cfmPoolGroup,_U:cfmLrGroup})