_k='oacNatStatGeneralGroup'
_j='oacNatOMTimeout'
_i='oacNatOMSessions'
_h='oacNatOMLocalAddr'
_g='oacNatIMTimeout'
_f='oacNatIMSessions'
_e='oacNatIMGlobalAddr'
_d='oacNatSessionTimeout'
_c='oacNatSessionOutPkts'
_b='oacNatSessionInPkts'
_a='oacNatSessionOutsideGlobalAddr'
_Z='oacNatSessionInsideGlobalPort'
_Y='oacNatSessionInsideGlobalAddr'
_X='oacNatSessionOutsidePort'
_W='oacNatSessionOutsideLocalAddr'
_V='oacNatSessionInsideLocalPort'
_U='oacNatSessionInsideLocalAddr'
_T='oacNatSessionProtocol'
_S='oacNatDynamicAllocFailures'
_R='oacNatOutPktsDropped'
_Q='oacNatInPktsDropped'
_P='oacNatOutsideAddrMaps'
_O='oacNatInsideAddrMaps'
_N='oacNatOutTranslations'
_M='oacNatInTranslations'
_L='oacNatSessionsClosed'
_K='oacNatActiveSessions'
_J='oacNatOMGlobalAddr'
_I='oacNatIMLocalAddr'
_H='oacNatSessionID'
_G='not-accessible'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='ONEACCESS-NAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
oacExpIMIpNatNotifications,oacExpIMIpNatStatistics,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIpNatNotifications','oacExpIMIpNatStatistics','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval')
oacNatMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,668))
if mibBuilder.loadTexts:oacNatMIBModule.setRevisions(('2011-10-27 00:00','2010-07-08 10:00'))
_OacNatStatObjects_ObjectIdentity=ObjectIdentity
oacNatStatObjects=_OacNatStatObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,1,1,1))
_OacNatStatGlobal_ObjectIdentity=ObjectIdentity
oacNatStatGlobal=_OacNatStatGlobal_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,1,1,1,1))
_OacNatActiveSessions_Type=Counter32
_OacNatActiveSessions_Object=MibScalar
oacNatActiveSessions=_OacNatActiveSessions_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,1),_OacNatActiveSessions_Type())
oacNatActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatActiveSessions.setStatus(_A)
_OacNatSessionsClosed_Type=Counter32
_OacNatSessionsClosed_Object=MibScalar
oacNatSessionsClosed=_OacNatSessionsClosed_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,2),_OacNatSessionsClosed_Type())
oacNatSessionsClosed.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionsClosed.setStatus(_A)
_OacNatInTranslations_Type=Counter32
_OacNatInTranslations_Object=MibScalar
oacNatInTranslations=_OacNatInTranslations_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,3),_OacNatInTranslations_Type())
oacNatInTranslations.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatInTranslations.setStatus(_A)
_OacNatOutTranslations_Type=Counter32
_OacNatOutTranslations_Object=MibScalar
oacNatOutTranslations=_OacNatOutTranslations_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,4),_OacNatOutTranslations_Type())
oacNatOutTranslations.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatOutTranslations.setStatus(_A)
_OacNatInsideAddrMaps_Type=Counter32
_OacNatInsideAddrMaps_Object=MibScalar
oacNatInsideAddrMaps=_OacNatInsideAddrMaps_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,5),_OacNatInsideAddrMaps_Type())
oacNatInsideAddrMaps.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatInsideAddrMaps.setStatus(_A)
_OacNatOutsideAddrMaps_Type=Counter32
_OacNatOutsideAddrMaps_Object=MibScalar
oacNatOutsideAddrMaps=_OacNatOutsideAddrMaps_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,6),_OacNatOutsideAddrMaps_Type())
oacNatOutsideAddrMaps.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatOutsideAddrMaps.setStatus(_A)
_OacNatInPktsDropped_Type=Counter32
_OacNatInPktsDropped_Object=MibScalar
oacNatInPktsDropped=_OacNatInPktsDropped_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,7),_OacNatInPktsDropped_Type())
oacNatInPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatInPktsDropped.setStatus(_A)
_OacNatOutPktsDropped_Type=Counter32
_OacNatOutPktsDropped_Object=MibScalar
oacNatOutPktsDropped=_OacNatOutPktsDropped_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,8),_OacNatOutPktsDropped_Type())
oacNatOutPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatOutPktsDropped.setStatus(_A)
_OacNatDynamicAllocFailures_Type=Counter32
_OacNatDynamicAllocFailures_Object=MibScalar
oacNatDynamicAllocFailures=_OacNatDynamicAllocFailures_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,1,9),_OacNatDynamicAllocFailures_Type())
oacNatDynamicAllocFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatDynamicAllocFailures.setStatus(_A)
_OacNatSessionTable_Object=MibTable
oacNatSessionTable=_OacNatSessionTable_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2))
if mibBuilder.loadTexts:oacNatSessionTable.setStatus(_A)
_OacNatSessionEntry_Object=MibTableRow
oacNatSessionEntry=_OacNatSessionEntry_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1))
oacNatSessionEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:oacNatSessionEntry.setStatus(_A)
_OacNatSessionID_Type=Unsigned32
_OacNatSessionID_Object=MibTableColumn
oacNatSessionID=_OacNatSessionID_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,1),_OacNatSessionID_Type())
oacNatSessionID.setMaxAccess(_G)
if mibBuilder.loadTexts:oacNatSessionID.setStatus(_A)
class _OacNatSessionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OacNatSessionProtocol_Type.__name__=_D
_OacNatSessionProtocol_Object=MibTableColumn
oacNatSessionProtocol=_OacNatSessionProtocol_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,2),_OacNatSessionProtocol_Type())
oacNatSessionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionProtocol.setStatus(_A)
_OacNatSessionInsideLocalAddr_Type=IpAddress
_OacNatSessionInsideLocalAddr_Object=MibTableColumn
oacNatSessionInsideLocalAddr=_OacNatSessionInsideLocalAddr_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,3),_OacNatSessionInsideLocalAddr_Type())
oacNatSessionInsideLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionInsideLocalAddr.setStatus(_A)
class _OacNatSessionInsideLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OacNatSessionInsideLocalPort_Type.__name__=_D
_OacNatSessionInsideLocalPort_Object=MibTableColumn
oacNatSessionInsideLocalPort=_OacNatSessionInsideLocalPort_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,4),_OacNatSessionInsideLocalPort_Type())
oacNatSessionInsideLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionInsideLocalPort.setStatus(_A)
_OacNatSessionOutsideLocalAddr_Type=IpAddress
_OacNatSessionOutsideLocalAddr_Object=MibTableColumn
oacNatSessionOutsideLocalAddr=_OacNatSessionOutsideLocalAddr_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,5),_OacNatSessionOutsideLocalAddr_Type())
oacNatSessionOutsideLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionOutsideLocalAddr.setStatus(_A)
class _OacNatSessionOutsidePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OacNatSessionOutsidePort_Type.__name__=_D
_OacNatSessionOutsidePort_Object=MibTableColumn
oacNatSessionOutsidePort=_OacNatSessionOutsidePort_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,6),_OacNatSessionOutsidePort_Type())
oacNatSessionOutsidePort.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionOutsidePort.setStatus(_A)
_OacNatSessionInsideGlobalAddr_Type=IpAddress
_OacNatSessionInsideGlobalAddr_Object=MibTableColumn
oacNatSessionInsideGlobalAddr=_OacNatSessionInsideGlobalAddr_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,7),_OacNatSessionInsideGlobalAddr_Type())
oacNatSessionInsideGlobalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionInsideGlobalAddr.setStatus(_A)
class _OacNatSessionInsideGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OacNatSessionInsideGlobalPort_Type.__name__=_D
_OacNatSessionInsideGlobalPort_Object=MibTableColumn
oacNatSessionInsideGlobalPort=_OacNatSessionInsideGlobalPort_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,8),_OacNatSessionInsideGlobalPort_Type())
oacNatSessionInsideGlobalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionInsideGlobalPort.setStatus(_A)
_OacNatSessionOutsideGlobalAddr_Type=IpAddress
_OacNatSessionOutsideGlobalAddr_Object=MibTableColumn
oacNatSessionOutsideGlobalAddr=_OacNatSessionOutsideGlobalAddr_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,9),_OacNatSessionOutsideGlobalAddr_Type())
oacNatSessionOutsideGlobalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionOutsideGlobalAddr.setStatus(_A)
_OacNatSessionInPkts_Type=Counter32
_OacNatSessionInPkts_Object=MibTableColumn
oacNatSessionInPkts=_OacNatSessionInPkts_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,10),_OacNatSessionInPkts_Type())
oacNatSessionInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionInPkts.setStatus(_A)
_OacNatSessionOutPkts_Type=Counter32
_OacNatSessionOutPkts_Object=MibTableColumn
oacNatSessionOutPkts=_OacNatSessionOutPkts_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,11),_OacNatSessionOutPkts_Type())
oacNatSessionOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionOutPkts.setStatus(_A)
_OacNatSessionTimeout_Type=TimeInterval
_OacNatSessionTimeout_Object=MibTableColumn
oacNatSessionTimeout=_OacNatSessionTimeout_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,2,1,12),_OacNatSessionTimeout_Type())
oacNatSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatSessionTimeout.setStatus(_A)
_OacNatInsideMapTable_Object=MibTable
oacNatInsideMapTable=_OacNatInsideMapTable_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,3))
if mibBuilder.loadTexts:oacNatInsideMapTable.setStatus(_A)
_OacNatInsideMapEntry_Object=MibTableRow
oacNatInsideMapEntry=_OacNatInsideMapEntry_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,3,1))
oacNatInsideMapEntry.setIndexNames((0,_E,_F),(0,_B,_I))
if mibBuilder.loadTexts:oacNatInsideMapEntry.setStatus(_A)
_OacNatIMLocalAddr_Type=IpAddress
_OacNatIMLocalAddr_Object=MibTableColumn
oacNatIMLocalAddr=_OacNatIMLocalAddr_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,3,1,1),_OacNatIMLocalAddr_Type())
oacNatIMLocalAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:oacNatIMLocalAddr.setStatus(_A)
_OacNatIMGlobalAddr_Type=IpAddress
_OacNatIMGlobalAddr_Object=MibTableColumn
oacNatIMGlobalAddr=_OacNatIMGlobalAddr_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,3,1,2),_OacNatIMGlobalAddr_Type())
oacNatIMGlobalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatIMGlobalAddr.setStatus(_A)
_OacNatIMSessions_Type=Integer32
_OacNatIMSessions_Object=MibTableColumn
oacNatIMSessions=_OacNatIMSessions_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,3,1,3),_OacNatIMSessions_Type())
oacNatIMSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatIMSessions.setStatus(_A)
_OacNatIMTimeout_Type=TimeInterval
_OacNatIMTimeout_Object=MibTableColumn
oacNatIMTimeout=_OacNatIMTimeout_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,3,1,4),_OacNatIMTimeout_Type())
oacNatIMTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatIMTimeout.setStatus(_A)
_OacNatOutsideMapTable_Object=MibTable
oacNatOutsideMapTable=_OacNatOutsideMapTable_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,4))
if mibBuilder.loadTexts:oacNatOutsideMapTable.setStatus(_A)
_OacNatOutsideMapEntry_Object=MibTableRow
oacNatOutsideMapEntry=_OacNatOutsideMapEntry_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,4,1))
oacNatOutsideMapEntry.setIndexNames((0,_E,_F),(0,_B,_J))
if mibBuilder.loadTexts:oacNatOutsideMapEntry.setStatus(_A)
_OacNatOMGlobalAddr_Type=IpAddress
_OacNatOMGlobalAddr_Object=MibTableColumn
oacNatOMGlobalAddr=_OacNatOMGlobalAddr_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,4,1,1),_OacNatOMGlobalAddr_Type())
oacNatOMGlobalAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:oacNatOMGlobalAddr.setStatus(_A)
_OacNatOMLocalAddr_Type=IpAddress
_OacNatOMLocalAddr_Object=MibTableColumn
oacNatOMLocalAddr=_OacNatOMLocalAddr_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,4,1,2),_OacNatOMLocalAddr_Type())
oacNatOMLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatOMLocalAddr.setStatus(_A)
_OacNatOMSessions_Type=Integer32
_OacNatOMSessions_Object=MibTableColumn
oacNatOMSessions=_OacNatOMSessions_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,4,1,3),_OacNatOMSessions_Type())
oacNatOMSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatOMSessions.setStatus(_A)
_OacNatOMTimeout_Type=TimeInterval
_OacNatOMTimeout_Object=MibTableColumn
oacNatOMTimeout=_OacNatOMTimeout_Object((1,3,6,1,4,1,13191,10,3,1,1,1,1,4,1,4),_OacNatOMTimeout_Type())
oacNatOMTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:oacNatOMTimeout.setStatus(_A)
_OacNatStatNotifications_ObjectIdentity=ObjectIdentity
oacNatStatNotifications=_OacNatStatNotifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,1,1,2))
_OacNatStatConformance_ObjectIdentity=ObjectIdentity
oacNatStatConformance=_OacNatStatConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,1,1,3))
_OacNatStatGroups_ObjectIdentity=ObjectIdentity
oacNatStatGroups=_OacNatStatGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,1,1,3,1))
_OacNatStatCompliances_ObjectIdentity=ObjectIdentity
oacNatStatCompliances=_OacNatStatCompliances_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,1,1,3,2))
oacNatStatGeneralGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,1,1,1,3,1,1))
oacNatStatGeneralGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:oacNatStatGeneralGroup.setStatus(_A)
oacNatNotificationMaximumSessionReached=NotificationType((1,3,6,1,4,1,13191,10,3,1,1,2,1))
if mibBuilder.loadTexts:oacNatNotificationMaximumSessionReached.setStatus(_A)
oacNatNotificationWarningSessionReachingLimit=NotificationType((1,3,6,1,4,1,13191,10,3,1,1,2,2))
if mibBuilder.loadTexts:oacNatNotificationWarningSessionReachingLimit.setStatus(_A)
oacNatStatCompliance=ModuleCompliance((1,3,6,1,4,1,13191,10,3,1,1,1,3,2,1))
oacNatStatCompliance.setObjects((_B,_k))
if mibBuilder.loadTexts:oacNatStatCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oacNatMIBModule':oacNatMIBModule,'oacNatStatObjects':oacNatStatObjects,'oacNatStatGlobal':oacNatStatGlobal,_K:oacNatActiveSessions,_L:oacNatSessionsClosed,_M:oacNatInTranslations,_N:oacNatOutTranslations,_O:oacNatInsideAddrMaps,_P:oacNatOutsideAddrMaps,_Q:oacNatInPktsDropped,_R:oacNatOutPktsDropped,_S:oacNatDynamicAllocFailures,'oacNatSessionTable':oacNatSessionTable,'oacNatSessionEntry':oacNatSessionEntry,_H:oacNatSessionID,_T:oacNatSessionProtocol,_U:oacNatSessionInsideLocalAddr,_V:oacNatSessionInsideLocalPort,_W:oacNatSessionOutsideLocalAddr,_X:oacNatSessionOutsidePort,_Y:oacNatSessionInsideGlobalAddr,_Z:oacNatSessionInsideGlobalPort,_a:oacNatSessionOutsideGlobalAddr,_b:oacNatSessionInPkts,_c:oacNatSessionOutPkts,_d:oacNatSessionTimeout,'oacNatInsideMapTable':oacNatInsideMapTable,'oacNatInsideMapEntry':oacNatInsideMapEntry,_I:oacNatIMLocalAddr,_e:oacNatIMGlobalAddr,_f:oacNatIMSessions,_g:oacNatIMTimeout,'oacNatOutsideMapTable':oacNatOutsideMapTable,'oacNatOutsideMapEntry':oacNatOutsideMapEntry,_J:oacNatOMGlobalAddr,_h:oacNatOMLocalAddr,_i:oacNatOMSessions,_j:oacNatOMTimeout,'oacNatStatNotifications':oacNatStatNotifications,'oacNatStatConformance':oacNatStatConformance,'oacNatStatGroups':oacNatStatGroups,_k:oacNatStatGeneralGroup,'oacNatStatCompliances':oacNatStatCompliances,'oacNatStatCompliance':oacNatStatCompliance,'oacNatNotificationMaximumSessionReached':oacNatNotificationMaximumSessionReached,'oacNatNotificationWarningSessionReachingLimit':oacNatNotificationWarningSessionReachingLimit})