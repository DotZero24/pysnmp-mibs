_R='clGlobalFlowGroup'
_Q='clLocalFlowGroup'
_P='clLocalTosValue'
_O='clLocalType'
_N='clLocalDropped'
_M='clLocalAccepted'
_L='clLocalCurrentRate'
_K='clGlobalType'
_J='clGlobalCurrentRate'
_I='clGlobalFlowType'
_H='clLocalNodeID'
_G='not-accessible'
_F='SnmpAdminString'
_E='clGlobalFlowIndex'
_D='Unsigned32'
_C='read-only'
_B='CISCO-LPTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoLptsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,812))
if mibBuilder.loadTexts:ciscoLptsMIB.setRevisions(('2013-09-03 00:00',))
class ClFlowType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('global',2),('local',3)))
_CiscoLptsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLptsMIBNotifs=_CiscoLptsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,812,0))
_CiscoLptsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLptsMIBObjects=_CiscoLptsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,812,1))
_ClGlobalFlowTable_Object=MibTable
clGlobalFlowTable=_ClGlobalFlowTable_Object((1,3,6,1,4,1,9,9,812,1,1))
if mibBuilder.loadTexts:clGlobalFlowTable.setStatus(_A)
_ClGlobalFlowEntry_Object=MibTableRow
clGlobalFlowEntry=_ClGlobalFlowEntry_Object((1,3,6,1,4,1,9,9,812,1,1,1))
clGlobalFlowEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:clGlobalFlowEntry.setStatus(_A)
class _ClGlobalFlowIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ClGlobalFlowIndex_Type.__name__=_D
_ClGlobalFlowIndex_Object=MibTableColumn
clGlobalFlowIndex=_ClGlobalFlowIndex_Object((1,3,6,1,4,1,9,9,812,1,1,1,1),_ClGlobalFlowIndex_Type())
clGlobalFlowIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:clGlobalFlowIndex.setStatus(_A)
class _ClGlobalFlowType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_ClGlobalFlowType_Type.__name__=_F
_ClGlobalFlowType_Object=MibTableColumn
clGlobalFlowType=_ClGlobalFlowType_Object((1,3,6,1,4,1,9,9,812,1,1,1,2),_ClGlobalFlowType_Type())
clGlobalFlowType.setMaxAccess(_C)
if mibBuilder.loadTexts:clGlobalFlowType.setStatus(_A)
_ClGlobalType_Type=ClFlowType
_ClGlobalType_Object=MibTableColumn
clGlobalType=_ClGlobalType_Object((1,3,6,1,4,1,9,9,812,1,1,1,3),_ClGlobalType_Type())
clGlobalType.setMaxAccess(_C)
if mibBuilder.loadTexts:clGlobalType.setStatus(_A)
_ClGlobalCurrentRate_Type=Unsigned32
_ClGlobalCurrentRate_Object=MibTableColumn
clGlobalCurrentRate=_ClGlobalCurrentRate_Object((1,3,6,1,4,1,9,9,812,1,1,1,4),_ClGlobalCurrentRate_Type())
clGlobalCurrentRate.setMaxAccess('read-write')
if mibBuilder.loadTexts:clGlobalCurrentRate.setStatus(_A)
if mibBuilder.loadTexts:clGlobalCurrentRate.setUnits('PPS')
_ClLocalFlowTable_Object=MibTable
clLocalFlowTable=_ClLocalFlowTable_Object((1,3,6,1,4,1,9,9,812,1,2))
if mibBuilder.loadTexts:clLocalFlowTable.setStatus(_A)
_ClLocalFlowEntry_Object=MibTableRow
clLocalFlowEntry=_ClLocalFlowEntry_Object((1,3,6,1,4,1,9,9,812,1,2,1))
clLocalFlowEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:clLocalFlowEntry.setStatus(_A)
class _ClLocalNodeID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ClLocalNodeID_Type.__name__=_D
_ClLocalNodeID_Object=MibTableColumn
clLocalNodeID=_ClLocalNodeID_Object((1,3,6,1,4,1,9,9,812,1,2,1,1),_ClLocalNodeID_Type())
clLocalNodeID.setMaxAccess(_G)
if mibBuilder.loadTexts:clLocalNodeID.setStatus(_A)
_ClLocalType_Type=ClFlowType
_ClLocalType_Object=MibTableColumn
clLocalType=_ClLocalType_Object((1,3,6,1,4,1,9,9,812,1,2,1,2),_ClLocalType_Type())
clLocalType.setMaxAccess(_C)
if mibBuilder.loadTexts:clLocalType.setStatus(_A)
_ClLocalCurrentRate_Type=Unsigned32
_ClLocalCurrentRate_Object=MibTableColumn
clLocalCurrentRate=_ClLocalCurrentRate_Object((1,3,6,1,4,1,9,9,812,1,2,1,3),_ClLocalCurrentRate_Type())
clLocalCurrentRate.setMaxAccess(_C)
if mibBuilder.loadTexts:clLocalCurrentRate.setStatus(_A)
if mibBuilder.loadTexts:clLocalCurrentRate.setUnits('PPS')
_ClLocalAccepted_Type=Counter64
_ClLocalAccepted_Object=MibTableColumn
clLocalAccepted=_ClLocalAccepted_Object((1,3,6,1,4,1,9,9,812,1,2,1,4),_ClLocalAccepted_Type())
clLocalAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:clLocalAccepted.setStatus(_A)
_ClLocalDropped_Type=Counter64
_ClLocalDropped_Object=MibTableColumn
clLocalDropped=_ClLocalDropped_Object((1,3,6,1,4,1,9,9,812,1,2,1,5),_ClLocalDropped_Type())
clLocalDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:clLocalDropped.setStatus(_A)
_ClLocalTosValue_Type=Unsigned32
_ClLocalTosValue_Object=MibTableColumn
clLocalTosValue=_ClLocalTosValue_Object((1,3,6,1,4,1,9,9,812,1,2,1,6),_ClLocalTosValue_Type())
clLocalTosValue.setMaxAccess(_C)
if mibBuilder.loadTexts:clLocalTosValue.setStatus(_A)
_CiscoLptsMIBConform_ObjectIdentity=ObjectIdentity
ciscoLptsMIBConform=_CiscoLptsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,812,2))
_CiscoLptsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLptsMIBCompliances=_CiscoLptsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,812,2,1))
_CiscoLptsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLptsMIBGroups=_CiscoLptsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,812,2,2))
clGlobalFlowGroup=ObjectGroup((1,3,6,1,4,1,9,9,812,2,2,1))
clGlobalFlowGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:clGlobalFlowGroup.setStatus(_A)
clLocalFlowGroup=ObjectGroup((1,3,6,1,4,1,9,9,812,2,2,2))
clLocalFlowGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:clLocalFlowGroup.setStatus(_A)
ciscoLptsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,812,2,1,1))
ciscoLptsMIBCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoLptsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ClFlowType':ClFlowType,'ciscoLptsMIB':ciscoLptsMIB,'ciscoLptsMIBNotifs':ciscoLptsMIBNotifs,'ciscoLptsMIBObjects':ciscoLptsMIBObjects,'clGlobalFlowTable':clGlobalFlowTable,'clGlobalFlowEntry':clGlobalFlowEntry,_E:clGlobalFlowIndex,_I:clGlobalFlowType,_K:clGlobalType,_J:clGlobalCurrentRate,'clLocalFlowTable':clLocalFlowTable,'clLocalFlowEntry':clLocalFlowEntry,_H:clLocalNodeID,_O:clLocalType,_L:clLocalCurrentRate,_M:clLocalAccepted,_N:clLocalDropped,_P:clLocalTosValue,'ciscoLptsMIBConform':ciscoLptsMIBConform,'ciscoLptsMIBCompliances':ciscoLptsMIBCompliances,'ciscoLptsMIBCompliance':ciscoLptsMIBCompliance,'ciscoLptsMIBGroups':ciscoLptsMIBGroups,_R:clGlobalFlowGroup,_Q:clLocalFlowGroup})