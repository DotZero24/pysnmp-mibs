_W='ciscoItpSp2QosGroup'
_V='ciscoItpSp2EventsGroup'
_U='cisQosRowStatus'
_T='cisQosAclId'
_S='cisQosIpDscp'
_R='cisQosPrecedenceValue'
_Q='cisQosType'
_P='cisEventHistoryDescr'
_O='cisEventHistoryTableEntAllowed'
_N='cisEventHistoryMaxEntries'
_M='cisEventSummryDroppedEvents'
_L='cisEventSummryLoggedEvents'
_K='cisQosClass'
_J='not-accessible'
_I='cisEventHistoryIndex'
_H='SnmpAdminString'
_G='CItpTcAclId'
_F='read-only'
_E='Unsigned32'
_D='Integer32'
_C='read-create'
_B='CISCO-ITP-SP2-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CItpTcAclId,=mibBuilder.importSymbols('CISCO-ITP-TC-MIB',_G)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoItpSp2MIB=ModuleIdentity((1,3,6,1,4,1,9,9,248))
if mibBuilder.loadTexts:ciscoItpSp2MIB.setRevisions(('2002-09-16 00:00','2002-02-21 00:00'))
class CisTcQosClass(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CiscoItpSp2MIBNotifications_ObjectIdentity=ObjectIdentity
ciscoItpSp2MIBNotifications=_CiscoItpSp2MIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,248,0))
_CiscoItpSp2MIBObjects_ObjectIdentity=ObjectIdentity
ciscoItpSp2MIBObjects=_CiscoItpSp2MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,248,1))
_CisEvents_ObjectIdentity=ObjectIdentity
cisEvents=_CisEvents_ObjectIdentity((1,3,6,1,4,1,9,9,248,1,1))
_CisEventSummryLoggedEvents_Type=Counter32
_CisEventSummryLoggedEvents_Object=MibScalar
cisEventSummryLoggedEvents=_CisEventSummryLoggedEvents_Object((1,3,6,1,4,1,9,9,248,1,1,1),_CisEventSummryLoggedEvents_Type())
cisEventSummryLoggedEvents.setMaxAccess(_F)
if mibBuilder.loadTexts:cisEventSummryLoggedEvents.setStatus(_A)
_CisEventSummryDroppedEvents_Type=Counter32
_CisEventSummryDroppedEvents_Object=MibScalar
cisEventSummryDroppedEvents=_CisEventSummryDroppedEvents_Object((1,3,6,1,4,1,9,9,248,1,1,2),_CisEventSummryDroppedEvents_Type())
cisEventSummryDroppedEvents.setMaxAccess(_F)
if mibBuilder.loadTexts:cisEventSummryDroppedEvents.setStatus(_A)
class _CisEventHistoryMaxEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CisEventHistoryMaxEntries_Type.__name__=_E
_CisEventHistoryMaxEntries_Object=MibScalar
cisEventHistoryMaxEntries=_CisEventHistoryMaxEntries_Object((1,3,6,1,4,1,9,9,248,1,1,3),_CisEventHistoryMaxEntries_Type())
cisEventHistoryMaxEntries.setMaxAccess('read-write')
if mibBuilder.loadTexts:cisEventHistoryMaxEntries.setStatus(_A)
class _CisEventHistoryTableEntAllowed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CisEventHistoryTableEntAllowed_Type.__name__=_E
_CisEventHistoryTableEntAllowed_Object=MibScalar
cisEventHistoryTableEntAllowed=_CisEventHistoryTableEntAllowed_Object((1,3,6,1,4,1,9,9,248,1,1,4),_CisEventHistoryTableEntAllowed_Type())
cisEventHistoryTableEntAllowed.setMaxAccess(_F)
if mibBuilder.loadTexts:cisEventHistoryTableEntAllowed.setStatus(_A)
_CisEventHistoryTable_Object=MibTable
cisEventHistoryTable=_CisEventHistoryTable_Object((1,3,6,1,4,1,9,9,248,1,1,5))
if mibBuilder.loadTexts:cisEventHistoryTable.setStatus(_A)
_CisEventHistoryTableEntry_Object=MibTableRow
cisEventHistoryTableEntry=_CisEventHistoryTableEntry_Object((1,3,6,1,4,1,9,9,248,1,1,5,1))
cisEventHistoryTableEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cisEventHistoryTableEntry.setStatus(_A)
class _CisEventHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CisEventHistoryIndex_Type.__name__=_E
_CisEventHistoryIndex_Object=MibTableColumn
cisEventHistoryIndex=_CisEventHistoryIndex_Object((1,3,6,1,4,1,9,9,248,1,1,5,1,1),_CisEventHistoryIndex_Type())
cisEventHistoryIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cisEventHistoryIndex.setStatus(_A)
class _CisEventHistoryDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CisEventHistoryDescr_Type.__name__=_H
_CisEventHistoryDescr_Object=MibTableColumn
cisEventHistoryDescr=_CisEventHistoryDescr_Object((1,3,6,1,4,1,9,9,248,1,1,5,1,2),_CisEventHistoryDescr_Type())
cisEventHistoryDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:cisEventHistoryDescr.setStatus(_A)
_CisQos_ObjectIdentity=ObjectIdentity
cisQos=_CisQos_ObjectIdentity((1,3,6,1,4,1,9,9,248,1,2))
_CisQosTable_Object=MibTable
cisQosTable=_CisQosTable_Object((1,3,6,1,4,1,9,9,248,1,2,1))
if mibBuilder.loadTexts:cisQosTable.setStatus(_A)
_CisQosTableEntry_Object=MibTableRow
cisQosTableEntry=_CisQosTableEntry_Object((1,3,6,1,4,1,9,9,248,1,2,1,1))
cisQosTableEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cisQosTableEntry.setStatus(_A)
_CisQosClass_Type=CisTcQosClass
_CisQosClass_Object=MibTableColumn
cisQosClass=_CisQosClass_Object((1,3,6,1,4,1,9,9,248,1,2,1,1,1),_CisQosClass_Type())
cisQosClass.setMaxAccess(_J)
if mibBuilder.loadTexts:cisQosClass.setStatus(_A)
class _CisQosType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipPrecedence',1),('ipDscp',2)))
_CisQosType_Type.__name__=_D
_CisQosType_Object=MibTableColumn
cisQosType=_CisQosType_Object((1,3,6,1,4,1,9,9,248,1,2,1,1,2),_CisQosType_Type())
cisQosType.setMaxAccess(_C)
if mibBuilder.loadTexts:cisQosType.setStatus(_A)
class _CisQosPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_CisQosPrecedenceValue_Type.__name__=_D
_CisQosPrecedenceValue_Object=MibTableColumn
cisQosPrecedenceValue=_CisQosPrecedenceValue_Object((1,3,6,1,4,1,9,9,248,1,2,1,1,3),_CisQosPrecedenceValue_Type())
cisQosPrecedenceValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cisQosPrecedenceValue.setStatus(_A)
class _CisQosIpDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,63))
_CisQosIpDscp_Type.__name__=_D
_CisQosIpDscp_Object=MibTableColumn
cisQosIpDscp=_CisQosIpDscp_Object((1,3,6,1,4,1,9,9,248,1,2,1,1,4),_CisQosIpDscp_Type())
cisQosIpDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:cisQosIpDscp.setStatus(_A)
class _CisQosAclId_Type(CItpTcAclId):defaultValue=0
_CisQosAclId_Type.__name__=_G
_CisQosAclId_Object=MibTableColumn
cisQosAclId=_CisQosAclId_Object((1,3,6,1,4,1,9,9,248,1,2,1,1,5),_CisQosAclId_Type())
cisQosAclId.setMaxAccess(_C)
if mibBuilder.loadTexts:cisQosAclId.setStatus(_A)
_CisQosRowStatus_Type=RowStatus
_CisQosRowStatus_Object=MibTableColumn
cisQosRowStatus=_CisQosRowStatus_Object((1,3,6,1,4,1,9,9,248,1,2,1,1,6),_CisQosRowStatus_Type())
cisQosRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cisQosRowStatus.setStatus(_A)
_CiscoItpSp2MIBConformance_ObjectIdentity=ObjectIdentity
ciscoItpSp2MIBConformance=_CiscoItpSp2MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,248,2))
_CiscoItpSp2MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoItpSp2MIBCompliances=_CiscoItpSp2MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,248,2,1))
_CiscoItpSp2MIBGroups_ObjectIdentity=ObjectIdentity
ciscoItpSp2MIBGroups=_CiscoItpSp2MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,248,2,2))
ciscoItpSp2EventsGroup=ObjectGroup((1,3,6,1,4,1,9,9,248,2,2,1))
ciscoItpSp2EventsGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoItpSp2EventsGroup.setStatus(_A)
ciscoItpSp2QosGroup=ObjectGroup((1,3,6,1,4,1,9,9,248,2,2,2))
ciscoItpSp2QosGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoItpSp2QosGroup.setStatus(_A)
ciscoItpSp2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,248,2,1,1))
ciscoItpSp2MIBCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoItpSp2MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CisTcQosClass':CisTcQosClass,'ciscoItpSp2MIB':ciscoItpSp2MIB,'ciscoItpSp2MIBNotifications':ciscoItpSp2MIBNotifications,'ciscoItpSp2MIBObjects':ciscoItpSp2MIBObjects,'cisEvents':cisEvents,_L:cisEventSummryLoggedEvents,_M:cisEventSummryDroppedEvents,_N:cisEventHistoryMaxEntries,_O:cisEventHistoryTableEntAllowed,'cisEventHistoryTable':cisEventHistoryTable,'cisEventHistoryTableEntry':cisEventHistoryTableEntry,_I:cisEventHistoryIndex,_P:cisEventHistoryDescr,'cisQos':cisQos,'cisQosTable':cisQosTable,'cisQosTableEntry':cisQosTableEntry,_K:cisQosClass,_Q:cisQosType,_R:cisQosPrecedenceValue,_S:cisQosIpDscp,_T:cisQosAclId,_U:cisQosRowStatus,'ciscoItpSp2MIBConformance':ciscoItpSp2MIBConformance,'ciscoItpSp2MIBCompliances':ciscoItpSp2MIBCompliances,'ciscoItpSp2MIBCompliance':ciscoItpSp2MIBCompliance,'ciscoItpSp2MIBGroups':ciscoItpSp2MIBGroups,_V:ciscoItpSp2EventsGroup,_W:ciscoItpSp2QosGroup})