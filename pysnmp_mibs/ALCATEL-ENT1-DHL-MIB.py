_l='alaDHLNotificationGroup'
_k='alaDHLVlanMapGroup'
_j='alaDHLVpaGroup'
_i='alaDHLLinksGroup'
_h='alaDHLSessionGroup'
_g='alaDHLVlanMoveTrap'
_f='alaDHLVlanMapRowStatus'
_e='alaDHLVpaActiveLink'
_d='alaDHLVpaVlanType'
_c='alaDHLLinksRowStatus'
_b='alaDHLLinkslinkBOperStatus'
_a='alaDHLLinkslinkAOperStatus'
_Z='alaDHLSessionRowStatus'
_Y='alaDHLSessionActiveMacFlushing'
_X='alaDHLSessionAdminMacFlushing'
_W='alaDHLSessionPreemptionTime'
_V='alaDHLSessionOperStatus'
_U='alaDHLSessionAdminStatus'
_T='alaDHLSessionDescr'
_S='alaDHLVlanMapVlanEnd'
_R='alaDHLVlanMapVlanStart'
_Q='alaDHLVpaVlan'
_P='alaDHLVpalink'
_O='alaDHLLinkslinkB'
_N='alaDHLLinkslinkA'
_M='alaDHLVlanMoveReason'
_L='alaDHLPortTo'
_K='alaDHLPortFrom'
_J='alaDHLSessionID'
_I='down'
_H='accessible-for-notify'
_G='alaDHLSessionIndex'
_F='read-only'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='ALCATEL-ENT1-DHL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1DHL,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1DHL')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1DHLMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1))
_AlcatelIND1DHLMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1DHLMIBNotifications=_AlcatelIND1DHLMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,0))
if mibBuilder.loadTexts:alcatelIND1DHLMIBNotifications.setStatus(_A)
_AlcatelIND1DHLMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1DHLMIBObjects=_AlcatelIND1DHLMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,1))
if mibBuilder.loadTexts:alcatelIND1DHLMIBObjects.setStatus(_A)
_AlaDHLSessionConfig_ObjectIdentity=ObjectIdentity
alaDHLSessionConfig=_AlaDHLSessionConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1))
_AlaDHLSessionTable_Object=MibTable
alaDHLSessionTable=_AlaDHLSessionTable_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1))
if mibBuilder.loadTexts:alaDHLSessionTable.setStatus(_A)
_AlaDHLSessionEntry_Object=MibTableRow
alaDHLSessionEntry=_AlaDHLSessionEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1))
alaDHLSessionEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:alaDHLSessionEntry.setStatus(_A)
class _AlaDHLSessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_AlaDHLSessionIndex_Type.__name__=_C
_AlaDHLSessionIndex_Object=MibTableColumn
alaDHLSessionIndex=_AlaDHLSessionIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1,1),_AlaDHLSessionIndex_Type())
alaDHLSessionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHLSessionIndex.setStatus(_A)
_AlaDHLSessionDescr_Type=SnmpAdminString
_AlaDHLSessionDescr_Object=MibTableColumn
alaDHLSessionDescr=_AlaDHLSessionDescr_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1,2),_AlaDHLSessionDescr_Type())
alaDHLSessionDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHLSessionDescr.setStatus(_A)
class _AlaDHLSessionAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_AlaDHLSessionAdminStatus_Type.__name__=_C
_AlaDHLSessionAdminStatus_Object=MibTableColumn
alaDHLSessionAdminStatus=_AlaDHLSessionAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1,3),_AlaDHLSessionAdminStatus_Type())
alaDHLSessionAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHLSessionAdminStatus.setStatus(_A)
class _AlaDHLSessionOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_I,2)))
_AlaDHLSessionOperStatus_Type.__name__=_C
_AlaDHLSessionOperStatus_Object=MibTableColumn
alaDHLSessionOperStatus=_AlaDHLSessionOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1,4),_AlaDHLSessionOperStatus_Type())
alaDHLSessionOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaDHLSessionOperStatus.setStatus(_A)
class _AlaDHLSessionPreemptionTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_AlaDHLSessionPreemptionTime_Type.__name__=_C
_AlaDHLSessionPreemptionTime_Object=MibTableColumn
alaDHLSessionPreemptionTime=_AlaDHLSessionPreemptionTime_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1,5),_AlaDHLSessionPreemptionTime_Type())
alaDHLSessionPreemptionTime.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHLSessionPreemptionTime.setStatus(_A)
if mibBuilder.loadTexts:alaDHLSessionPreemptionTime.setUnits('seconds')
class _AlaDHLSessionAdminMacFlushing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('raw',2),('mvrp',3)))
_AlaDHLSessionAdminMacFlushing_Type.__name__=_C
_AlaDHLSessionAdminMacFlushing_Object=MibTableColumn
alaDHLSessionAdminMacFlushing=_AlaDHLSessionAdminMacFlushing_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1,6),_AlaDHLSessionAdminMacFlushing_Type())
alaDHLSessionAdminMacFlushing.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHLSessionAdminMacFlushing.setStatus(_A)
class _AlaDHLSessionActiveMacFlushing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('raw',2),('mvrp',3)))
_AlaDHLSessionActiveMacFlushing_Type.__name__=_C
_AlaDHLSessionActiveMacFlushing_Object=MibTableColumn
alaDHLSessionActiveMacFlushing=_AlaDHLSessionActiveMacFlushing_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1,7),_AlaDHLSessionActiveMacFlushing_Type())
alaDHLSessionActiveMacFlushing.setMaxAccess(_F)
if mibBuilder.loadTexts:alaDHLSessionActiveMacFlushing.setStatus(_A)
_AlaDHLSessionRowStatus_Type=RowStatus
_AlaDHLSessionRowStatus_Object=MibTableColumn
alaDHLSessionRowStatus=_AlaDHLSessionRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,1,1,1,8),_AlaDHLSessionRowStatus_Type())
alaDHLSessionRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHLSessionRowStatus.setStatus(_A)
_AlaDHLLinksConfig_ObjectIdentity=ObjectIdentity
alaDHLLinksConfig=_AlaDHLLinksConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,2))
_AlaDHLLinksTable_Object=MibTable
alaDHLLinksTable=_AlaDHLLinksTable_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,2,1))
if mibBuilder.loadTexts:alaDHLLinksTable.setStatus(_A)
_AlaDHLLinksEntry_Object=MibTableRow
alaDHLLinksEntry=_AlaDHLLinksEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,2,1,1))
alaDHLLinksEntry.setIndexNames((0,_B,_G),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:alaDHLLinksEntry.setStatus(_A)
_AlaDHLLinkslinkA_Type=InterfaceIndex
_AlaDHLLinkslinkA_Object=MibTableColumn
alaDHLLinkslinkA=_AlaDHLLinkslinkA_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,2,1,1,1),_AlaDHLLinkslinkA_Type())
alaDHLLinkslinkA.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHLLinkslinkA.setStatus(_A)
_AlaDHLLinkslinkB_Type=InterfaceIndex
_AlaDHLLinkslinkB_Object=MibTableColumn
alaDHLLinkslinkB=_AlaDHLLinkslinkB_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,2,1,1,2),_AlaDHLLinkslinkB_Type())
alaDHLLinkslinkB.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHLLinkslinkB.setStatus(_A)
class _AlaDHLLinkslinkAOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_I,2)))
_AlaDHLLinkslinkAOperStatus_Type.__name__=_C
_AlaDHLLinkslinkAOperStatus_Object=MibTableColumn
alaDHLLinkslinkAOperStatus=_AlaDHLLinkslinkAOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,2,1,1,3),_AlaDHLLinkslinkAOperStatus_Type())
alaDHLLinkslinkAOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaDHLLinkslinkAOperStatus.setStatus(_A)
class _AlaDHLLinkslinkBOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_I,2)))
_AlaDHLLinkslinkBOperStatus_Type.__name__=_C
_AlaDHLLinkslinkBOperStatus_Object=MibTableColumn
alaDHLLinkslinkBOperStatus=_AlaDHLLinkslinkBOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,2,1,1,4),_AlaDHLLinkslinkBOperStatus_Type())
alaDHLLinkslinkBOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaDHLLinkslinkBOperStatus.setStatus(_A)
_AlaDHLLinksRowStatus_Type=RowStatus
_AlaDHLLinksRowStatus_Object=MibTableColumn
alaDHLLinksRowStatus=_AlaDHLLinksRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,2,1,1,5),_AlaDHLLinksRowStatus_Type())
alaDHLLinksRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHLLinksRowStatus.setStatus(_A)
_AlaDHLVpa_ObjectIdentity=ObjectIdentity
alaDHLVpa=_AlaDHLVpa_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,3))
_AlaDHLVpaTable_Object=MibTable
alaDHLVpaTable=_AlaDHLVpaTable_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,3,1))
if mibBuilder.loadTexts:alaDHLVpaTable.setStatus(_A)
_AlaDHLVpaEntry_Object=MibTableRow
alaDHLVpaEntry=_AlaDHLVpaEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,3,1,1))
alaDHLVpaEntry.setIndexNames((0,_B,_G),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:alaDHLVpaEntry.setStatus(_A)
_AlaDHLVpalink_Type=InterfaceIndex
_AlaDHLVpalink_Object=MibTableColumn
alaDHLVpalink=_AlaDHLVpalink_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,3,1,1,1),_AlaDHLVpalink_Type())
alaDHLVpalink.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHLVpalink.setStatus(_A)
class _AlaDHLVpaVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaDHLVpaVlan_Type.__name__=_C
_AlaDHLVpaVlan_Object=MibTableColumn
alaDHLVpaVlan=_AlaDHLVpaVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,3,1,1,2),_AlaDHLVpaVlan_Type())
alaDHLVpaVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHLVpaVlan.setStatus(_A)
class _AlaDHLVpaVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('protectedVlan',1),('unprotectedVlan',2)))
_AlaDHLVpaVlanType_Type.__name__=_C
_AlaDHLVpaVlanType_Object=MibTableColumn
alaDHLVpaVlanType=_AlaDHLVpaVlanType_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,3,1,1,3),_AlaDHLVpaVlanType_Type())
alaDHLVpaVlanType.setMaxAccess(_F)
if mibBuilder.loadTexts:alaDHLVpaVlanType.setStatus(_A)
_AlaDHLVpaActiveLink_Type=InterfaceIndex
_AlaDHLVpaActiveLink_Object=MibTableColumn
alaDHLVpaActiveLink=_AlaDHLVpaActiveLink_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,3,1,1,4),_AlaDHLVpaActiveLink_Type())
alaDHLVpaActiveLink.setMaxAccess(_F)
if mibBuilder.loadTexts:alaDHLVpaActiveLink.setStatus(_A)
_AlaDHLVlanMap_ObjectIdentity=ObjectIdentity
alaDHLVlanMap=_AlaDHLVlanMap_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,4))
_AlaDHLVlanMapTable_Object=MibTable
alaDHLVlanMapTable=_AlaDHLVlanMapTable_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,4,1))
if mibBuilder.loadTexts:alaDHLVlanMapTable.setStatus(_A)
_AlaDHLVlanMapEntry_Object=MibTableRow
alaDHLVlanMapEntry=_AlaDHLVlanMapEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,4,1,1))
alaDHLVlanMapEntry.setIndexNames((0,_B,_G),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:alaDHLVlanMapEntry.setStatus(_A)
class _AlaDHLVlanMapVlanStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaDHLVlanMapVlanStart_Type.__name__=_C
_AlaDHLVlanMapVlanStart_Object=MibTableColumn
alaDHLVlanMapVlanStart=_AlaDHLVlanMapVlanStart_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,4,1,1,1),_AlaDHLVlanMapVlanStart_Type())
alaDHLVlanMapVlanStart.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHLVlanMapVlanStart.setStatus(_A)
class _AlaDHLVlanMapVlanEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaDHLVlanMapVlanEnd_Type.__name__=_C
_AlaDHLVlanMapVlanEnd_Object=MibTableColumn
alaDHLVlanMapVlanEnd=_AlaDHLVlanMapVlanEnd_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,4,1,1,2),_AlaDHLVlanMapVlanEnd_Type())
alaDHLVlanMapVlanEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHLVlanMapVlanEnd.setStatus(_A)
_AlaDHLVlanMapRowStatus_Type=RowStatus
_AlaDHLVlanMapRowStatus_Object=MibTableColumn
alaDHLVlanMapRowStatus=_AlaDHLVlanMapRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,4,1,1,3),_AlaDHLVlanMapRowStatus_Type())
alaDHLVlanMapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHLVlanMapRowStatus.setStatus(_A)
_AlaDHLTrapsObj_ObjectIdentity=ObjectIdentity
alaDHLTrapsObj=_AlaDHLTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,5))
_AlaDHLSessionID_Type=Integer32
_AlaDHLSessionID_Object=MibScalar
alaDHLSessionID=_AlaDHLSessionID_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,5,1),_AlaDHLSessionID_Type())
alaDHLSessionID.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDHLSessionID.setStatus(_A)
_AlaDHLPortFrom_Type=InterfaceIndex
_AlaDHLPortFrom_Object=MibScalar
alaDHLPortFrom=_AlaDHLPortFrom_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,5,2),_AlaDHLPortFrom_Type())
alaDHLPortFrom.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDHLPortFrom.setStatus(_A)
_AlaDHLPortTo_Type=InterfaceIndex
_AlaDHLPortTo_Object=MibScalar
alaDHLPortTo=_AlaDHLPortTo_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,5,3),_AlaDHLPortTo_Type())
alaDHLPortTo.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDHLPortTo.setStatus(_A)
class _AlaDHLVlanMoveReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linkUp',1),('linkDown',2)))
_AlaDHLVlanMoveReason_Type.__name__=_C
_AlaDHLVlanMoveReason_Object=MibScalar
alaDHLVlanMoveReason=_AlaDHLVlanMoveReason_Object((1,3,6,1,4,1,6486,801,1,2,1,65,1,1,5,4),_AlaDHLVlanMoveReason_Type())
alaDHLVlanMoveReason.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDHLVlanMoveReason.setStatus(_A)
_AlcatelIND1DHLMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1DHLMIBConformance=_AlcatelIND1DHLMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,2))
if mibBuilder.loadTexts:alcatelIND1DHLMIBConformance.setStatus(_A)
_AlcatelIND1DHLMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1DHLMIBGroups=_AlcatelIND1DHLMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,1))
if mibBuilder.loadTexts:alcatelIND1DHLMIBGroups.setStatus(_A)
_AlcatelIND1DHLMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1DHLMIBCompliances=_AlcatelIND1DHLMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,2))
if mibBuilder.loadTexts:alcatelIND1DHLMIBCompliances.setStatus(_A)
alaDHLSessionGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,1,1))
alaDHLSessionGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:alaDHLSessionGroup.setStatus(_A)
alaDHLLinksGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,1,2))
alaDHLLinksGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:alaDHLLinksGroup.setStatus(_A)
alaDHLVpaGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,1,3))
alaDHLVpaGroup.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:alaDHLVpaGroup.setStatus(_A)
alaDHLVlanMapGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,1,4))
alaDHLVlanMapGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:alaDHLVlanMapGroup.setStatus(_A)
alaDHLNotificationObjectGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,1,5))
alaDHLNotificationObjectGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:alaDHLNotificationObjectGroup.setStatus(_A)
alaDHLVlanMoveTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,65,1,0,1))
alaDHLVlanMoveTrap.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:alaDHLVlanMoveTrap.setStatus(_A)
alaDHLNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,1,6))
alaDHLNotificationGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:alaDHLNotificationGroup.setStatus(_A)
alcatelIND1DHLMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,65,1,2,2,1))
alcatelIND1DHLMIBCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alcatelIND1DHLMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1DHLMIB':alcatelIND1DHLMIB,'alcatelIND1DHLMIBNotifications':alcatelIND1DHLMIBNotifications,_g:alaDHLVlanMoveTrap,'alcatelIND1DHLMIBObjects':alcatelIND1DHLMIBObjects,'alaDHLSessionConfig':alaDHLSessionConfig,'alaDHLSessionTable':alaDHLSessionTable,'alaDHLSessionEntry':alaDHLSessionEntry,_G:alaDHLSessionIndex,_T:alaDHLSessionDescr,_U:alaDHLSessionAdminStatus,_V:alaDHLSessionOperStatus,_W:alaDHLSessionPreemptionTime,_X:alaDHLSessionAdminMacFlushing,_Y:alaDHLSessionActiveMacFlushing,_Z:alaDHLSessionRowStatus,'alaDHLLinksConfig':alaDHLLinksConfig,'alaDHLLinksTable':alaDHLLinksTable,'alaDHLLinksEntry':alaDHLLinksEntry,_N:alaDHLLinkslinkA,_O:alaDHLLinkslinkB,_a:alaDHLLinkslinkAOperStatus,_b:alaDHLLinkslinkBOperStatus,_c:alaDHLLinksRowStatus,'alaDHLVpa':alaDHLVpa,'alaDHLVpaTable':alaDHLVpaTable,'alaDHLVpaEntry':alaDHLVpaEntry,_P:alaDHLVpalink,_Q:alaDHLVpaVlan,_d:alaDHLVpaVlanType,_e:alaDHLVpaActiveLink,'alaDHLVlanMap':alaDHLVlanMap,'alaDHLVlanMapTable':alaDHLVlanMapTable,'alaDHLVlanMapEntry':alaDHLVlanMapEntry,_R:alaDHLVlanMapVlanStart,_S:alaDHLVlanMapVlanEnd,_f:alaDHLVlanMapRowStatus,'alaDHLTrapsObj':alaDHLTrapsObj,_J:alaDHLSessionID,_K:alaDHLPortFrom,_L:alaDHLPortTo,_M:alaDHLVlanMoveReason,'alcatelIND1DHLMIBConformance':alcatelIND1DHLMIBConformance,'alcatelIND1DHLMIBGroups':alcatelIND1DHLMIBGroups,_h:alaDHLSessionGroup,_i:alaDHLLinksGroup,_j:alaDHLVpaGroup,_k:alaDHLVlanMapGroup,'alaDHLNotificationObjectGroup':alaDHLNotificationObjectGroup,_l:alaDHLNotificationGroup,'alcatelIND1DHLMIBCompliances':alcatelIND1DHLMIBCompliances,'alcatelIND1DHLMIBCompliance':alcatelIND1DHLMIBCompliance})