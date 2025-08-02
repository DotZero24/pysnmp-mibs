_L='clabTopoGroup'
_K='clabTopoChFnCfgRowStatus'
_J='clabTopoFiberNodeCfgRowStatus'
_I='clabTopoFiberNodeCfgNodeDescr'
_H='clabTopoChFnCfgChIfIndex'
_G='not-accessible'
_F='NodeName'
_E='SnmpAdminString'
_D='read-create'
_C='clabTopoFiberNodeCfgNodeName'
_B='CLAB-TOPO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabCommonMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabCommonMibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
clabTopoMib=ModuleIdentity((1,3,6,1,4,1,4491,4,2))
if mibBuilder.loadTexts:clabTopoMib.setRevisions(('2006-12-07 17:00',))
class NodeName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ClabTopoMibObjects_ObjectIdentity=ObjectIdentity
clabTopoMibObjects=_ClabTopoMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,2,1))
_ClabTopoFiberNodeCfgTable_Object=MibTable
clabTopoFiberNodeCfgTable=_ClabTopoFiberNodeCfgTable_Object((1,3,6,1,4,1,4491,4,2,1,1))
if mibBuilder.loadTexts:clabTopoFiberNodeCfgTable.setStatus(_A)
_ClabTopoFiberNodeCfgEntry_Object=MibTableRow
clabTopoFiberNodeCfgEntry=_ClabTopoFiberNodeCfgEntry_Object((1,3,6,1,4,1,4491,4,2,1,1,1))
clabTopoFiberNodeCfgEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:clabTopoFiberNodeCfgEntry.setStatus(_A)
class _ClabTopoFiberNodeCfgNodeName_Type(NodeName):subtypeSpec=NodeName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ClabTopoFiberNodeCfgNodeName_Type.__name__=_F
_ClabTopoFiberNodeCfgNodeName_Object=MibTableColumn
clabTopoFiberNodeCfgNodeName=_ClabTopoFiberNodeCfgNodeName_Object((1,3,6,1,4,1,4491,4,2,1,1,1,1),_ClabTopoFiberNodeCfgNodeName_Type())
clabTopoFiberNodeCfgNodeName.setMaxAccess(_G)
if mibBuilder.loadTexts:clabTopoFiberNodeCfgNodeName.setStatus(_A)
class _ClabTopoFiberNodeCfgNodeDescr_Type(SnmpAdminString):defaultHexValue=''
_ClabTopoFiberNodeCfgNodeDescr_Type.__name__=_E
_ClabTopoFiberNodeCfgNodeDescr_Object=MibTableColumn
clabTopoFiberNodeCfgNodeDescr=_ClabTopoFiberNodeCfgNodeDescr_Object((1,3,6,1,4,1,4491,4,2,1,1,1,2),_ClabTopoFiberNodeCfgNodeDescr_Type())
clabTopoFiberNodeCfgNodeDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:clabTopoFiberNodeCfgNodeDescr.setStatus(_A)
_ClabTopoFiberNodeCfgRowStatus_Type=RowStatus
_ClabTopoFiberNodeCfgRowStatus_Object=MibTableColumn
clabTopoFiberNodeCfgRowStatus=_ClabTopoFiberNodeCfgRowStatus_Object((1,3,6,1,4,1,4491,4,2,1,1,1,3),_ClabTopoFiberNodeCfgRowStatus_Type())
clabTopoFiberNodeCfgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clabTopoFiberNodeCfgRowStatus.setStatus(_A)
_ClabTopoChFnCfgTable_Object=MibTable
clabTopoChFnCfgTable=_ClabTopoChFnCfgTable_Object((1,3,6,1,4,1,4491,4,2,1,2))
if mibBuilder.loadTexts:clabTopoChFnCfgTable.setStatus(_A)
_ClabTopoChFnCfgEntry_Object=MibTableRow
clabTopoChFnCfgEntry=_ClabTopoChFnCfgEntry_Object((1,3,6,1,4,1,4491,4,2,1,2,1))
clabTopoChFnCfgEntry.setIndexNames((0,_B,_C),(0,_B,_H))
if mibBuilder.loadTexts:clabTopoChFnCfgEntry.setStatus(_A)
_ClabTopoChFnCfgChIfIndex_Type=InterfaceIndex
_ClabTopoChFnCfgChIfIndex_Object=MibTableColumn
clabTopoChFnCfgChIfIndex=_ClabTopoChFnCfgChIfIndex_Object((1,3,6,1,4,1,4491,4,2,1,2,1,1),_ClabTopoChFnCfgChIfIndex_Type())
clabTopoChFnCfgChIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:clabTopoChFnCfgChIfIndex.setStatus(_A)
_ClabTopoChFnCfgRowStatus_Type=RowStatus
_ClabTopoChFnCfgRowStatus_Object=MibTableColumn
clabTopoChFnCfgRowStatus=_ClabTopoChFnCfgRowStatus_Object((1,3,6,1,4,1,4491,4,2,1,2,1,2),_ClabTopoChFnCfgRowStatus_Type())
clabTopoChFnCfgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clabTopoChFnCfgRowStatus.setStatus(_A)
_ClabTopoMibConformance_ObjectIdentity=ObjectIdentity
clabTopoMibConformance=_ClabTopoMibConformance_ObjectIdentity((1,3,6,1,4,1,4491,4,2,2))
_ClabTopoMibCompliances_ObjectIdentity=ObjectIdentity
clabTopoMibCompliances=_ClabTopoMibCompliances_ObjectIdentity((1,3,6,1,4,1,4491,4,2,2,1))
_ClabTopoMibGroups_ObjectIdentity=ObjectIdentity
clabTopoMibGroups=_ClabTopoMibGroups_ObjectIdentity((1,3,6,1,4,1,4491,4,2,2,2))
clabTopoGroup=ObjectGroup((1,3,6,1,4,1,4491,4,2,2,2,1))
clabTopoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:clabTopoGroup.setStatus(_A)
clabTopoCompliance=ModuleCompliance((1,3,6,1,4,1,4491,4,2,2,1,1))
clabTopoCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:clabTopoCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:NodeName,'clabTopoMib':clabTopoMib,'clabTopoMibObjects':clabTopoMibObjects,'clabTopoFiberNodeCfgTable':clabTopoFiberNodeCfgTable,'clabTopoFiberNodeCfgEntry':clabTopoFiberNodeCfgEntry,_C:clabTopoFiberNodeCfgNodeName,_I:clabTopoFiberNodeCfgNodeDescr,_J:clabTopoFiberNodeCfgRowStatus,'clabTopoChFnCfgTable':clabTopoChFnCfgTable,'clabTopoChFnCfgEntry':clabTopoChFnCfgEntry,_H:clabTopoChFnCfgChIfIndex,_K:clabTopoChFnCfgRowStatus,'clabTopoMibConformance':clabTopoMibConformance,'clabTopoMibCompliances':clabTopoMibCompliances,'clabTopoCompliance':clabTopoCompliance,'clabTopoMibGroups':clabTopoMibGroups,_L:clabTopoGroup})