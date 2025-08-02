_S='casnActiveGroupSup1'
_R='casnVaiIfIndex'
_Q='casnNasPort'
_P='casnDisconnectedSessions'
_O='casnTotalSessions'
_N='casnCallTrackerId'
_M='casnDisconnect'
_L='casnIdleTime'
_K='casnIpAddr'
_J='casnUserId'
_I='casnActiveTableHighWaterMark'
_H='casnActiveTableEntries'
_G='casnSessionId'
_F='DisplayString'
_E='casnGeneralGroup'
_D='casnActiveGroup'
_C='read-only'
_B='CISCO-AAA-SESSION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowPointer','TextualConvention','TruthValue')
ciscoAAASessionMIB=ModuleIdentity((1,3,6,1,4,1,9,9,150))
if mibBuilder.loadTexts:ciscoAAASessionMIB.setRevisions(('2006-03-21 00:00','2002-04-11 00:00','1999-11-16 00:00'))
class CctCallId(TextualConvention,Unsigned32):status=_A
class CasnSessionId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CasnMIBObjects_ObjectIdentity=ObjectIdentity
casnMIBObjects=_CasnMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,150,1))
_CasnActive_ObjectIdentity=ObjectIdentity
casnActive=_CasnActive_ObjectIdentity((1,3,6,1,4,1,9,9,150,1,1))
_CasnActiveTableEntries_Type=Gauge32
_CasnActiveTableEntries_Object=MibScalar
casnActiveTableEntries=_CasnActiveTableEntries_Object((1,3,6,1,4,1,9,9,150,1,1,1),_CasnActiveTableEntries_Type())
casnActiveTableEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:casnActiveTableEntries.setStatus(_A)
_CasnActiveTableHighWaterMark_Type=Gauge32
_CasnActiveTableHighWaterMark_Object=MibScalar
casnActiveTableHighWaterMark=_CasnActiveTableHighWaterMark_Object((1,3,6,1,4,1,9,9,150,1,1,2),_CasnActiveTableHighWaterMark_Type())
casnActiveTableHighWaterMark.setMaxAccess(_C)
if mibBuilder.loadTexts:casnActiveTableHighWaterMark.setStatus(_A)
_CasnActiveTable_Object=MibTable
casnActiveTable=_CasnActiveTable_Object((1,3,6,1,4,1,9,9,150,1,1,3))
if mibBuilder.loadTexts:casnActiveTable.setStatus(_A)
_CasnActiveEntry_Object=MibTableRow
casnActiveEntry=_CasnActiveEntry_Object((1,3,6,1,4,1,9,9,150,1,1,3,1))
casnActiveEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:casnActiveEntry.setStatus(_A)
_CasnSessionId_Type=CasnSessionId
_CasnSessionId_Object=MibTableColumn
casnSessionId=_CasnSessionId_Object((1,3,6,1,4,1,9,9,150,1,1,3,1,1),_CasnSessionId_Type())
casnSessionId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:casnSessionId.setStatus(_A)
class _CasnUserId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CasnUserId_Type.__name__=_F
_CasnUserId_Object=MibTableColumn
casnUserId=_CasnUserId_Object((1,3,6,1,4,1,9,9,150,1,1,3,1,2),_CasnUserId_Type())
casnUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:casnUserId.setStatus(_A)
_CasnIpAddr_Type=IpAddress
_CasnIpAddr_Object=MibTableColumn
casnIpAddr=_CasnIpAddr_Object((1,3,6,1,4,1,9,9,150,1,1,3,1,3),_CasnIpAddr_Type())
casnIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:casnIpAddr.setStatus(_A)
_CasnIdleTime_Type=Gauge32
_CasnIdleTime_Object=MibTableColumn
casnIdleTime=_CasnIdleTime_Object((1,3,6,1,4,1,9,9,150,1,1,3,1,4),_CasnIdleTime_Type())
casnIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:casnIdleTime.setStatus(_A)
if mibBuilder.loadTexts:casnIdleTime.setUnits('seconds')
_CasnDisconnect_Type=TruthValue
_CasnDisconnect_Object=MibTableColumn
casnDisconnect=_CasnDisconnect_Object((1,3,6,1,4,1,9,9,150,1,1,3,1,5),_CasnDisconnect_Type())
casnDisconnect.setMaxAccess('read-write')
if mibBuilder.loadTexts:casnDisconnect.setStatus(_A)
_CasnCallTrackerId_Type=CctCallId
_CasnCallTrackerId_Object=MibTableColumn
casnCallTrackerId=_CasnCallTrackerId_Object((1,3,6,1,4,1,9,9,150,1,1,3,1,6),_CasnCallTrackerId_Type())
casnCallTrackerId.setMaxAccess(_C)
if mibBuilder.loadTexts:casnCallTrackerId.setStatus(_A)
_CasnNasPort_Type=RowPointer
_CasnNasPort_Object=MibTableColumn
casnNasPort=_CasnNasPort_Object((1,3,6,1,4,1,9,9,150,1,1,3,1,7),_CasnNasPort_Type())
casnNasPort.setMaxAccess(_C)
if mibBuilder.loadTexts:casnNasPort.setStatus(_A)
_CasnVaiIfIndex_Type=InterfaceIndexOrZero
_CasnVaiIfIndex_Object=MibTableColumn
casnVaiIfIndex=_CasnVaiIfIndex_Object((1,3,6,1,4,1,9,9,150,1,1,3,1,8),_CasnVaiIfIndex_Type())
casnVaiIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:casnVaiIfIndex.setStatus(_A)
_CasnGeneral_ObjectIdentity=ObjectIdentity
casnGeneral=_CasnGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,150,1,2))
_CasnTotalSessions_Type=Counter32
_CasnTotalSessions_Object=MibScalar
casnTotalSessions=_CasnTotalSessions_Object((1,3,6,1,4,1,9,9,150,1,2,1),_CasnTotalSessions_Type())
casnTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:casnTotalSessions.setStatus(_A)
_CasnDisconnectedSessions_Type=Counter32
_CasnDisconnectedSessions_Object=MibScalar
casnDisconnectedSessions=_CasnDisconnectedSessions_Object((1,3,6,1,4,1,9,9,150,1,2,2),_CasnDisconnectedSessions_Type())
casnDisconnectedSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:casnDisconnectedSessions.setStatus(_A)
_CasnMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
casnMIBNotificationPrefix=_CasnMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,150,2))
_CasnMIBNotifications_ObjectIdentity=ObjectIdentity
casnMIBNotifications=_CasnMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,150,2,1))
_CasnMIBConformance_ObjectIdentity=ObjectIdentity
casnMIBConformance=_CasnMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,150,3))
_CasnMIBCompliances_ObjectIdentity=ObjectIdentity
casnMIBCompliances=_CasnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,150,3,1))
_CasnMIBGroups_ObjectIdentity=ObjectIdentity
casnMIBGroups=_CasnMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,150,3,2))
casnActiveGroup=ObjectGroup((1,3,6,1,4,1,9,9,150,3,2,1))
casnActiveGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:casnActiveGroup.setStatus(_A)
casnGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,150,3,2,2))
casnGeneralGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:casnGeneralGroup.setStatus(_A)
casnActiveGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,150,3,2,3))
casnActiveGroupSup1.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:casnActiveGroupSup1.setStatus(_A)
casnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,150,3,1,1))
casnMIBCompliance.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:casnMIBCompliance.setStatus('deprecated')
casnMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,150,3,1,2))
casnMIBComplianceRev1.setObjects(*((_B,_D),(_B,_E),(_B,_S)))
if mibBuilder.loadTexts:casnMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CctCallId':CctCallId,'CasnSessionId':CasnSessionId,'ciscoAAASessionMIB':ciscoAAASessionMIB,'casnMIBObjects':casnMIBObjects,'casnActive':casnActive,_H:casnActiveTableEntries,_I:casnActiveTableHighWaterMark,'casnActiveTable':casnActiveTable,'casnActiveEntry':casnActiveEntry,_G:casnSessionId,_J:casnUserId,_K:casnIpAddr,_L:casnIdleTime,_M:casnDisconnect,_N:casnCallTrackerId,_Q:casnNasPort,_R:casnVaiIfIndex,'casnGeneral':casnGeneral,_O:casnTotalSessions,_P:casnDisconnectedSessions,'casnMIBNotificationPrefix':casnMIBNotificationPrefix,'casnMIBNotifications':casnMIBNotifications,'casnMIBConformance':casnMIBConformance,'casnMIBCompliances':casnMIBCompliances,'casnMIBCompliance':casnMIBCompliance,'casnMIBComplianceRev1':casnMIBComplianceRev1,'casnMIBGroups':casnMIBGroups,_D:casnActiveGroup,_E:casnGeneralGroup,_S:casnActiveGroupSup1})