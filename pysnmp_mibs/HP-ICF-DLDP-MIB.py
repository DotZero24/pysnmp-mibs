_k='hpicfDldpNotificationGroup'
_j='hpicfDldpStatsGroup'
_i='hpicfDldpNeighborGroup'
_h='hpicfDldpPortGroup'
_g='hpicfDldpScalarsGroup'
_f='hpicfDldpTrapBidLink'
_e='hpicfDldpTrapUniLink'
_d='hpicfDldpStatClear'
_c='hpicfDldpAuthFailedPackets'
_b='hpicfDldpRxInvalidPackets'
_a='hpicfDldpRxValidPackets'
_Z='hpicfDldpTxPackets'
_Y='hpicfDldpRxPackets'
_X='hpicfDldpNeighborAgingTime'
_W='hpicfDldpNeighborStatus'
_V='hpicfDldpNeighborPortIndex'
_U='hpicfDldpNeighborBridgeMac'
_T='hpicfDldpPortLinkStatus'
_S='hpicfDldpPortOperStatus'
_R='hpicfDldpPortEnable'
_Q='hpicfDldpDelayDownInterval'
_P='hpicfDldpUniShutdown'
_O='hpicfDldpAuthPasswordEncrypted'
_N='hpicfDldpAuthPassword'
_M='hpicfDldpAuthMode'
_L='hpicfDldpInterval'
_K='hpicfDldpGlobalEnable'
_J='hpicfDldpNeighborPortId'
_I='OctetString'
_H='unknown'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='HP-ICF-DLDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
hpicfDldpMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108))
if mibBuilder.loadTexts:hpicfDldpMIB.setRevisions(('2014-03-07 00:00',))
_HpicfDldpNotifications_ObjectIdentity=ObjectIdentity
hpicfDldpNotifications=_HpicfDldpNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108,0))
_HpicfDldpConfigurationObjects_ObjectIdentity=ObjectIdentity
hpicfDldpConfigurationObjects=_HpicfDldpConfigurationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108,1))
_HpicfDldpScalars_ObjectIdentity=ObjectIdentity
hpicfDldpScalars=_HpicfDldpScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108,1,1))
_HpicfDldpGlobalEnable_Type=TruthValue
_HpicfDldpGlobalEnable_Object=MibScalar
hpicfDldpGlobalEnable=_HpicfDldpGlobalEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,1,1),_HpicfDldpGlobalEnable_Type())
hpicfDldpGlobalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpGlobalEnable.setStatus(_A)
class _HpicfDldpInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpicfDldpInterval_Type.__name__=_D
_HpicfDldpInterval_Object=MibScalar
hpicfDldpInterval=_HpicfDldpInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,1,2),_HpicfDldpInterval_Type())
hpicfDldpInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpInterval.setStatus(_A)
class _HpicfDldpAuthMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('none',2),('simple',3),('md5',4)))
_HpicfDldpAuthMode_Type.__name__=_D
_HpicfDldpAuthMode_Object=MibScalar
hpicfDldpAuthMode=_HpicfDldpAuthMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,1,3),_HpicfDldpAuthMode_Type())
hpicfDldpAuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpAuthMode.setStatus(_A)
class _HpicfDldpAuthPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HpicfDldpAuthPassword_Type.__name__=_I
_HpicfDldpAuthPassword_Object=MibScalar
hpicfDldpAuthPassword=_HpicfDldpAuthPassword_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,1,4),_HpicfDldpAuthPassword_Type())
hpicfDldpAuthPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpAuthPassword.setStatus(_A)
class _HpicfDldpAuthPasswordEncrypted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfDldpAuthPasswordEncrypted_Type.__name__=_I
_HpicfDldpAuthPasswordEncrypted_Object=MibScalar
hpicfDldpAuthPasswordEncrypted=_HpicfDldpAuthPasswordEncrypted_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,1,5),_HpicfDldpAuthPasswordEncrypted_Type())
hpicfDldpAuthPasswordEncrypted.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpAuthPasswordEncrypted.setStatus(_A)
class _HpicfDldpUniShutdown_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('auto',2),('manual',3)))
_HpicfDldpUniShutdown_Type.__name__=_D
_HpicfDldpUniShutdown_Object=MibScalar
hpicfDldpUniShutdown=_HpicfDldpUniShutdown_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,1,6),_HpicfDldpUniShutdown_Type())
hpicfDldpUniShutdown.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpUniShutdown.setStatus(_A)
class _HpicfDldpDelayDownInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpicfDldpDelayDownInterval_Type.__name__=_D
_HpicfDldpDelayDownInterval_Object=MibScalar
hpicfDldpDelayDownInterval=_HpicfDldpDelayDownInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,1,7),_HpicfDldpDelayDownInterval_Type())
hpicfDldpDelayDownInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpDelayDownInterval.setStatus(_A)
_HpicfDldpPortConfigTable_Object=MibTable
hpicfDldpPortConfigTable=_HpicfDldpPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,2))
if mibBuilder.loadTexts:hpicfDldpPortConfigTable.setStatus(_A)
_HpicfDldpPortConfigEntry_Object=MibTableRow
hpicfDldpPortConfigEntry=_HpicfDldpPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,2,1))
hpicfDldpPortConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpicfDldpPortConfigEntry.setStatus(_A)
_HpicfDldpPortEnable_Type=TruthValue
_HpicfDldpPortEnable_Object=MibTableColumn
hpicfDldpPortEnable=_HpicfDldpPortEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,2,1,1),_HpicfDldpPortEnable_Type())
hpicfDldpPortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpPortEnable.setStatus(_A)
_HpicfDldpPortStatusTable_Object=MibTable
hpicfDldpPortStatusTable=_HpicfDldpPortStatusTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,3))
if mibBuilder.loadTexts:hpicfDldpPortStatusTable.setStatus(_A)
_HpicfDldpPortStatusEntry_Object=MibTableRow
hpicfDldpPortStatusEntry=_HpicfDldpPortStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,3,1))
hpicfDldpPortStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpicfDldpPortStatusEntry.setStatus(_A)
class _HpicfDldpPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('initial',2),('inactive',3),('unidirectional',4),('bidirectional',5)))
_HpicfDldpPortOperStatus_Type.__name__=_D
_HpicfDldpPortOperStatus_Object=MibTableColumn
hpicfDldpPortOperStatus=_HpicfDldpPortOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,3,1,1),_HpicfDldpPortOperStatus_Type())
hpicfDldpPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpPortOperStatus.setStatus(_A)
class _HpicfDldpPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('down',2),('up',3)))
_HpicfDldpPortLinkStatus_Type.__name__=_D
_HpicfDldpPortLinkStatus_Object=MibTableColumn
hpicfDldpPortLinkStatus=_HpicfDldpPortLinkStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,3,1,2),_HpicfDldpPortLinkStatus_Type())
hpicfDldpPortLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpPortLinkStatus.setStatus(_A)
_HpicfDldpPortStatTable_Object=MibTable
hpicfDldpPortStatTable=_HpicfDldpPortStatTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,4))
if mibBuilder.loadTexts:hpicfDldpPortStatTable.setStatus(_A)
_HpicfDldpPortStatEntry_Object=MibTableRow
hpicfDldpPortStatEntry=_HpicfDldpPortStatEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,4,1))
hpicfDldpPortStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpicfDldpPortStatEntry.setStatus(_A)
_HpicfDldpRxPackets_Type=Counter64
_HpicfDldpRxPackets_Object=MibTableColumn
hpicfDldpRxPackets=_HpicfDldpRxPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,4,1,1),_HpicfDldpRxPackets_Type())
hpicfDldpRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpRxPackets.setStatus(_A)
_HpicfDldpTxPackets_Type=Counter64
_HpicfDldpTxPackets_Object=MibTableColumn
hpicfDldpTxPackets=_HpicfDldpTxPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,4,1,2),_HpicfDldpTxPackets_Type())
hpicfDldpTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpTxPackets.setStatus(_A)
_HpicfDldpRxValidPackets_Type=Counter64
_HpicfDldpRxValidPackets_Object=MibTableColumn
hpicfDldpRxValidPackets=_HpicfDldpRxValidPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,4,1,3),_HpicfDldpRxValidPackets_Type())
hpicfDldpRxValidPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpRxValidPackets.setStatus(_A)
_HpicfDldpRxInvalidPackets_Type=Counter64
_HpicfDldpRxInvalidPackets_Object=MibTableColumn
hpicfDldpRxInvalidPackets=_HpicfDldpRxInvalidPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,4,1,4),_HpicfDldpRxInvalidPackets_Type())
hpicfDldpRxInvalidPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpRxInvalidPackets.setStatus(_A)
_HpicfDldpAuthFailedPackets_Type=Counter64
_HpicfDldpAuthFailedPackets_Object=MibTableColumn
hpicfDldpAuthFailedPackets=_HpicfDldpAuthFailedPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,4,1,5),_HpicfDldpAuthFailedPackets_Type())
hpicfDldpAuthFailedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpAuthFailedPackets.setStatus(_A)
_HpicfDldpStatClear_Type=TruthValue
_HpicfDldpStatClear_Object=MibTableColumn
hpicfDldpStatClear=_HpicfDldpStatClear_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,4,1,6),_HpicfDldpStatClear_Type())
hpicfDldpStatClear.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDldpStatClear.setStatus(_A)
_HpicfDldpNeighborTable_Object=MibTable
hpicfDldpNeighborTable=_HpicfDldpNeighborTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,5))
if mibBuilder.loadTexts:hpicfDldpNeighborTable.setStatus(_A)
_HpicfDldpNeighborEntry_Object=MibTableRow
hpicfDldpNeighborEntry=_HpicfDldpNeighborEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,5,1))
hpicfDldpNeighborEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:hpicfDldpNeighborEntry.setStatus(_A)
class _HpicfDldpNeighborPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpicfDldpNeighborPortId_Type.__name__=_D
_HpicfDldpNeighborPortId_Object=MibTableColumn
hpicfDldpNeighborPortId=_HpicfDldpNeighborPortId_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,5,1,1),_HpicfDldpNeighborPortId_Type())
hpicfDldpNeighborPortId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfDldpNeighborPortId.setStatus(_A)
_HpicfDldpNeighborBridgeMac_Type=MacAddress
_HpicfDldpNeighborBridgeMac_Object=MibTableColumn
hpicfDldpNeighborBridgeMac=_HpicfDldpNeighborBridgeMac_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,5,1,2),_HpicfDldpNeighborBridgeMac_Type())
hpicfDldpNeighborBridgeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpNeighborBridgeMac.setStatus(_A)
_HpicfDldpNeighborPortIndex_Type=Integer32
_HpicfDldpNeighborPortIndex_Object=MibTableColumn
hpicfDldpNeighborPortIndex=_HpicfDldpNeighborPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,5,1,3),_HpicfDldpNeighborPortIndex_Type())
hpicfDldpNeighborPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpNeighborPortIndex.setStatus(_A)
class _HpicfDldpNeighborStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('unconfirmed',2),('confirmed',3)))
_HpicfDldpNeighborStatus_Type.__name__=_D
_HpicfDldpNeighborStatus_Object=MibTableColumn
hpicfDldpNeighborStatus=_HpicfDldpNeighborStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,5,1,4),_HpicfDldpNeighborStatus_Type())
hpicfDldpNeighborStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpNeighborStatus.setStatus(_A)
_HpicfDldpNeighborAgingTime_Type=Integer32
_HpicfDldpNeighborAgingTime_Object=MibTableColumn
hpicfDldpNeighborAgingTime=_HpicfDldpNeighborAgingTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,108,1,5,1,5),_HpicfDldpNeighborAgingTime_Type())
hpicfDldpNeighborAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDldpNeighborAgingTime.setStatus(_A)
_HpicfDldpStatisticsObjects_ObjectIdentity=ObjectIdentity
hpicfDldpStatisticsObjects=_HpicfDldpStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108,2))
_HpicfDldpScalarStats_ObjectIdentity=ObjectIdentity
hpicfDldpScalarStats=_HpicfDldpScalarStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108,2,1))
_HpicfDldpConformance_ObjectIdentity=ObjectIdentity
hpicfDldpConformance=_HpicfDldpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108,3))
_HpicfDldpCompliances_ObjectIdentity=ObjectIdentity
hpicfDldpCompliances=_HpicfDldpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108,3,1))
_HpicfDldpGroups_ObjectIdentity=ObjectIdentity
hpicfDldpGroups=_HpicfDldpGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,108,3,2))
hpicfDldpScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,108,3,2,1))
hpicfDldpScalarsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpicfDldpScalarsGroup.setStatus(_A)
hpicfDldpPortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,108,3,2,2))
hpicfDldpPortGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:hpicfDldpPortGroup.setStatus(_A)
hpicfDldpNeighborGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,108,3,2,3))
hpicfDldpNeighborGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:hpicfDldpNeighborGroup.setStatus(_A)
hpicfDldpStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,108,3,2,4))
hpicfDldpStatsGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:hpicfDldpStatsGroup.setStatus(_A)
hpicfDldpTrapUniLink=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,108,0,1))
hpicfDldpTrapUniLink.setObjects((_F,_G))
if mibBuilder.loadTexts:hpicfDldpTrapUniLink.setStatus(_A)
hpicfDldpTrapBidLink=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,108,0,2))
hpicfDldpTrapBidLink.setObjects((_F,_G))
if mibBuilder.loadTexts:hpicfDldpTrapBidLink.setStatus(_A)
hpicfDldpNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,108,3,2,5))
hpicfDldpNotificationGroup.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:hpicfDldpNotificationGroup.setStatus(_A)
hpicfDldpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,108,3,1,1))
hpicfDldpCompliance.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:hpicfDldpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfDldpMIB':hpicfDldpMIB,'hpicfDldpNotifications':hpicfDldpNotifications,_e:hpicfDldpTrapUniLink,_f:hpicfDldpTrapBidLink,'hpicfDldpConfigurationObjects':hpicfDldpConfigurationObjects,'hpicfDldpScalars':hpicfDldpScalars,_K:hpicfDldpGlobalEnable,_L:hpicfDldpInterval,_M:hpicfDldpAuthMode,_N:hpicfDldpAuthPassword,_O:hpicfDldpAuthPasswordEncrypted,_P:hpicfDldpUniShutdown,_Q:hpicfDldpDelayDownInterval,'hpicfDldpPortConfigTable':hpicfDldpPortConfigTable,'hpicfDldpPortConfigEntry':hpicfDldpPortConfigEntry,_R:hpicfDldpPortEnable,'hpicfDldpPortStatusTable':hpicfDldpPortStatusTable,'hpicfDldpPortStatusEntry':hpicfDldpPortStatusEntry,_S:hpicfDldpPortOperStatus,_T:hpicfDldpPortLinkStatus,'hpicfDldpPortStatTable':hpicfDldpPortStatTable,'hpicfDldpPortStatEntry':hpicfDldpPortStatEntry,_Y:hpicfDldpRxPackets,_Z:hpicfDldpTxPackets,_a:hpicfDldpRxValidPackets,_b:hpicfDldpRxInvalidPackets,_c:hpicfDldpAuthFailedPackets,_d:hpicfDldpStatClear,'hpicfDldpNeighborTable':hpicfDldpNeighborTable,'hpicfDldpNeighborEntry':hpicfDldpNeighborEntry,_J:hpicfDldpNeighborPortId,_U:hpicfDldpNeighborBridgeMac,_V:hpicfDldpNeighborPortIndex,_W:hpicfDldpNeighborStatus,_X:hpicfDldpNeighborAgingTime,'hpicfDldpStatisticsObjects':hpicfDldpStatisticsObjects,'hpicfDldpScalarStats':hpicfDldpScalarStats,'hpicfDldpConformance':hpicfDldpConformance,'hpicfDldpCompliances':hpicfDldpCompliances,'hpicfDldpCompliance':hpicfDldpCompliance,'hpicfDldpGroups':hpicfDldpGroups,_g:hpicfDldpScalarsGroup,_h:hpicfDldpPortGroup,_i:hpicfDldpNeighborGroup,_j:hpicfDldpStatsGroup,_k:hpicfDldpNotificationGroup})