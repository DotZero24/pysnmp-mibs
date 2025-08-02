_p='sfpsOutPortStatsPort'
_o='sfpsInPortStatsPort'
_n='sfpsOutPortConfigPort'
_m='no-router'
_l='router-port'
_k='linkDown'
_j='linkUp'
_i='atm-forum-svc'
_h='atm-forum-pvc'
_g='atm-forum-lec'
_f='atm-pvc'
_e='token-ring'
_d='atm-lec'
_c='ethernet'
_b='unknown-ra-standby'
_a='downlinkFlood'
_Z='uplinkFlood'
_Y='raPrimary'
_X='accessOnly'
_W='network-only'
_V='stand-by'
_U='hybrid-port'
_T='going-to-access'
_S='host-ctl-port'
_R='host-mgmt-port'
_Q='network-port'
_P='access-port'
_O='testing'
_N='invalid-config'
_M='pending-enable'
_L='pending-disable'
_K='loopback'
_J='sfpsInPortConfigPort'
_I='unknown'
_H='CTRON-SFPS-PORT-MIB'
_G='enabled'
_F='disabled'
_E='read-write'
_D='other'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsPortAttributeAPI,sfpsPortAttributeTable,sfpsPortConfig,sfpsPortStats=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsPortAttributeAPI','sfpsPortAttributeTable','sfpsPortConfig','sfpsPortStats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsSwitchPort(Integer32):0
class HexInteger(Integer32):0
_SfpsInPortConfigTable_Object=MibTable
sfpsInPortConfigTable=_SfpsInPortConfigTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1))
if mibBuilder.loadTexts:sfpsInPortConfigTable.setStatus(_A)
_SfpsInPortConfigEntry_Object=MibTableRow
sfpsInPortConfigEntry=_SfpsInPortConfigEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1))
sfpsInPortConfigEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:sfpsInPortConfigEntry.setStatus(_A)
_SfpsInPortConfigPort_Type=SfpsSwitchPort
_SfpsInPortConfigPort_Object=MibTableColumn
sfpsInPortConfigPort=_SfpsInPortConfigPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,1),_SfpsInPortConfigPort_Type())
sfpsInPortConfigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigPort.setStatus(_A)
class _SfpsInPortConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_G,3),(_K,4)))
_SfpsInPortConfigAdminStatus_Type.__name__=_C
_SfpsInPortConfigAdminStatus_Object=MibTableColumn
sfpsInPortConfigAdminStatus=_SfpsInPortConfigAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,2),_SfpsInPortConfigAdminStatus_Type())
sfpsInPortConfigAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsInPortConfigAdminStatus.setStatus(_A)
class _SfpsInPortConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_F,2),(_G,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_SfpsInPortConfigOperStatus_Type.__name__=_C
_SfpsInPortConfigOperStatus_Object=MibTableColumn
sfpsInPortConfigOperStatus=_SfpsInPortConfigOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,3),_SfpsInPortConfigOperStatus_Type())
sfpsInPortConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigOperStatus.setStatus(_A)
_SfpsInPortConfigOperTime_Type=TimeTicks
_SfpsInPortConfigOperTime_Object=MibTableColumn
sfpsInPortConfigOperTime=_SfpsInPortConfigOperTime_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,4),_SfpsInPortConfigOperTime_Type())
sfpsInPortConfigOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigOperTime.setStatus(_A)
class _SfpsInPortConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_D,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_I,6),(_T,7),(_U,8),(_V,9),(_W,10),(_X,11),(_Y,12),('uplink',13),('fclStandby',14),('loopStandby',15),('raStandby',16),('flood',17),(_Z,18),(_a,19),(_b,20)))
_SfpsInPortConfigType_Type.__name__=_C
_SfpsInPortConfigType_Object=MibTableColumn
sfpsInPortConfigType=_SfpsInPortConfigType_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,5),_SfpsInPortConfigType_Type())
sfpsInPortConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsInPortConfigType.setStatus(_A)
_SfpsInPortConfigReservedBW_Type=Integer32
_SfpsInPortConfigReservedBW_Object=MibTableColumn
sfpsInPortConfigReservedBW=_SfpsInPortConfigReservedBW_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,6),_SfpsInPortConfigReservedBW_Type())
sfpsInPortConfigReservedBW.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsInPortConfigReservedBW.setStatus(_A)
_SfpsInPortConfigAllocBW_Type=Integer32
_SfpsInPortConfigAllocBW_Object=MibTableColumn
sfpsInPortConfigAllocBW=_SfpsInPortConfigAllocBW_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,7),_SfpsInPortConfigAllocBW_Type())
sfpsInPortConfigAllocBW.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigAllocBW.setStatus(_A)
_SfpsInPortConfigQoS_Type=Integer32
_SfpsInPortConfigQoS_Object=MibTableColumn
sfpsInPortConfigQoS=_SfpsInPortConfigQoS_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,8),_SfpsInPortConfigQoS_Type())
sfpsInPortConfigQoS.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsInPortConfigQoS.setStatus(_A)
_SfpsInPortConfigQSize_Type=Integer32
_SfpsInPortConfigQSize_Object=MibTableColumn
sfpsInPortConfigQSize=_SfpsInPortConfigQSize_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,9),_SfpsInPortConfigQSize_Type())
sfpsInPortConfigQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigQSize.setStatus(_A)
_SfpsInPortConfigQLen_Type=Gauge32
_SfpsInPortConfigQLen_Object=MibTableColumn
sfpsInPortConfigQLen=_SfpsInPortConfigQLen_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,10),_SfpsInPortConfigQLen_Type())
sfpsInPortConfigQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigQLen.setStatus(_A)
_SfpsInPortConfigSwitchId_Type=OctetString
_SfpsInPortConfigSwitchId_Object=MibTableColumn
sfpsInPortConfigSwitchId=_SfpsInPortConfigSwitchId_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,11),_SfpsInPortConfigSwitchId_Type())
sfpsInPortConfigSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigSwitchId.setStatus(_A)
class _SfpsInPortConfigMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_c,1),('fddi',2),(_d,3),(_e,4),('wan',5),('inb',6),('hcp',7),('hdp',8),('atm-svc',9),(_f,10),(_I,11),(_g,12),(_h,13),(_i,14)))
_SfpsInPortConfigMediaType_Type.__name__=_C
_SfpsInPortConfigMediaType_Object=MibTableColumn
sfpsInPortConfigMediaType=_SfpsInPortConfigMediaType_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,12),_SfpsInPortConfigMediaType_Type())
sfpsInPortConfigMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigMediaType.setStatus(_A)
_SfpsInPortConfigFrontPanelPort_Type=SfpsSwitchPort
_SfpsInPortConfigFrontPanelPort_Object=MibTableColumn
sfpsInPortConfigFrontPanelPort=_SfpsInPortConfigFrontPanelPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,13),_SfpsInPortConfigFrontPanelPort_Type())
sfpsInPortConfigFrontPanelPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigFrontPanelPort.setStatus(_A)
class _SfpsInPortConfigLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_j,2),(_k,3),('link-N-A',4)))
_SfpsInPortConfigLinkStatus_Type.__name__=_C
_SfpsInPortConfigLinkStatus_Object=MibTableColumn
sfpsInPortConfigLinkStatus=_SfpsInPortConfigLinkStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,14),_SfpsInPortConfigLinkStatus_Type())
sfpsInPortConfigLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigLinkStatus.setStatus(_A)
_SfpsInPortConfigLinkStateAge_Type=TimeTicks
_SfpsInPortConfigLinkStateAge_Object=MibTableColumn
sfpsInPortConfigLinkStateAge=_SfpsInPortConfigLinkStateAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,15),_SfpsInPortConfigLinkStateAge_Type())
sfpsInPortConfigLinkStateAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigLinkStateAge.setStatus(_A)
class _SfpsInPortConfigRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_l,2),(_m,3)))
_SfpsInPortConfigRouterPort_Type.__name__=_C
_SfpsInPortConfigRouterPort_Object=MibTableColumn
sfpsInPortConfigRouterPort=_SfpsInPortConfigRouterPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,16),_SfpsInPortConfigRouterPort_Type())
sfpsInPortConfigRouterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigRouterPort.setStatus(_A)
_SfpsInPortConfigSlotNumber_Type=Integer32
_SfpsInPortConfigSlotNumber_Object=MibTableColumn
sfpsInPortConfigSlotNumber=_SfpsInPortConfigSlotNumber_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,17),_SfpsInPortConfigSlotNumber_Type())
sfpsInPortConfigSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigSlotNumber.setStatus(_A)
_SfpsInPortConfigMib2PortId_Type=Integer32
_SfpsInPortConfigMib2PortId_Object=MibTableColumn
sfpsInPortConfigMib2PortId=_SfpsInPortConfigMib2PortId_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,18),_SfpsInPortConfigMib2PortId_Type())
sfpsInPortConfigMib2PortId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigMib2PortId.setStatus(_A)
_SfpsInPortConfigTopoAgent_Type=DisplayString
_SfpsInPortConfigTopoAgent_Object=MibTableColumn
sfpsInPortConfigTopoAgent=_SfpsInPortConfigTopoAgent_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,19),_SfpsInPortConfigTopoAgent_Type())
sfpsInPortConfigTopoAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigTopoAgent.setStatus(_A)
class _SfpsInPortConfigLayer3Learning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3)))
_SfpsInPortConfigLayer3Learning_Type.__name__=_C
_SfpsInPortConfigLayer3Learning_Object=MibTableColumn
sfpsInPortConfigLayer3Learning=_SfpsInPortConfigLayer3Learning_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,1,1,22),_SfpsInPortConfigLayer3Learning_Type())
sfpsInPortConfigLayer3Learning.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortConfigLayer3Learning.setStatus(_A)
_SfpsOutPortConfigTable_Object=MibTable
sfpsOutPortConfigTable=_SfpsOutPortConfigTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2))
if mibBuilder.loadTexts:sfpsOutPortConfigTable.setStatus(_A)
_SfpsOutPortConfigEntry_Object=MibTableRow
sfpsOutPortConfigEntry=_SfpsOutPortConfigEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1))
sfpsOutPortConfigEntry.setIndexNames((0,_H,_n))
if mibBuilder.loadTexts:sfpsOutPortConfigEntry.setStatus(_A)
_SfpsOutPortConfigPort_Type=SfpsSwitchPort
_SfpsOutPortConfigPort_Object=MibTableColumn
sfpsOutPortConfigPort=_SfpsOutPortConfigPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,1),_SfpsOutPortConfigPort_Type())
sfpsOutPortConfigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigPort.setStatus(_A)
class _SfpsOutPortConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_G,3),(_K,4)))
_SfpsOutPortConfigAdminStatus_Type.__name__=_C
_SfpsOutPortConfigAdminStatus_Object=MibTableColumn
sfpsOutPortConfigAdminStatus=_SfpsOutPortConfigAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,2),_SfpsOutPortConfigAdminStatus_Type())
sfpsOutPortConfigAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsOutPortConfigAdminStatus.setStatus(_A)
class _SfpsOutPortConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_F,2),(_G,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_SfpsOutPortConfigOperStatus_Type.__name__=_C
_SfpsOutPortConfigOperStatus_Object=MibTableColumn
sfpsOutPortConfigOperStatus=_SfpsOutPortConfigOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,3),_SfpsOutPortConfigOperStatus_Type())
sfpsOutPortConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigOperStatus.setStatus(_A)
_SfpsOutPortConfigOperTime_Type=TimeTicks
_SfpsOutPortConfigOperTime_Object=MibTableColumn
sfpsOutPortConfigOperTime=_SfpsOutPortConfigOperTime_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,4),_SfpsOutPortConfigOperTime_Type())
sfpsOutPortConfigOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigOperTime.setStatus(_A)
class _SfpsOutPortConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_D,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_I,6),(_T,7),(_U,8),(_V,9),(_W,10),(_X,11),(_Y,12),('standbyFCLConflict',13),('standbyLoopedPort',14),('standbyVersionConflict',15),('standbyRANonPrimary',16),('flood',17),(_Z,18),(_a,19),(_b,20)))
_SfpsOutPortConfigType_Type.__name__=_C
_SfpsOutPortConfigType_Object=MibTableColumn
sfpsOutPortConfigType=_SfpsOutPortConfigType_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,5),_SfpsOutPortConfigType_Type())
sfpsOutPortConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsOutPortConfigType.setStatus(_A)
_SfpsOutPortConfigReservedBW_Type=Integer32
_SfpsOutPortConfigReservedBW_Object=MibTableColumn
sfpsOutPortConfigReservedBW=_SfpsOutPortConfigReservedBW_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,6),_SfpsOutPortConfigReservedBW_Type())
sfpsOutPortConfigReservedBW.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsOutPortConfigReservedBW.setStatus(_A)
_SfpsOutPortConfigAllocBW_Type=Integer32
_SfpsOutPortConfigAllocBW_Object=MibTableColumn
sfpsOutPortConfigAllocBW=_SfpsOutPortConfigAllocBW_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,7),_SfpsOutPortConfigAllocBW_Type())
sfpsOutPortConfigAllocBW.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigAllocBW.setStatus(_A)
_SfpsOutPortConfigQoS_Type=Integer32
_SfpsOutPortConfigQoS_Object=MibTableColumn
sfpsOutPortConfigQoS=_SfpsOutPortConfigQoS_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,8),_SfpsOutPortConfigQoS_Type())
sfpsOutPortConfigQoS.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsOutPortConfigQoS.setStatus(_A)
_SfpsOutPortConfigQSize_Type=Integer32
_SfpsOutPortConfigQSize_Object=MibTableColumn
sfpsOutPortConfigQSize=_SfpsOutPortConfigQSize_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,9),_SfpsOutPortConfigQSize_Type())
sfpsOutPortConfigQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigQSize.setStatus(_A)
_SfpsOutPortConfigQLen_Type=Gauge32
_SfpsOutPortConfigQLen_Object=MibTableColumn
sfpsOutPortConfigQLen=_SfpsOutPortConfigQLen_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,10),_SfpsOutPortConfigQLen_Type())
sfpsOutPortConfigQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigQLen.setStatus(_A)
_SfpsOutPortConfigSwitchId_Type=OctetString
_SfpsOutPortConfigSwitchId_Object=MibTableColumn
sfpsOutPortConfigSwitchId=_SfpsOutPortConfigSwitchId_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,11),_SfpsOutPortConfigSwitchId_Type())
sfpsOutPortConfigSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigSwitchId.setStatus(_A)
class _SfpsOutPortConfigMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_c,1),('fddi',2),(_d,3),(_e,4),('wan',5),('inb',6),('hcp',7),('hdp',8),('atm-encap',9),(_f,10),(_I,11),(_g,12),(_h,13),(_i,14)))
_SfpsOutPortConfigMediaType_Type.__name__=_C
_SfpsOutPortConfigMediaType_Object=MibTableColumn
sfpsOutPortConfigMediaType=_SfpsOutPortConfigMediaType_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,12),_SfpsOutPortConfigMediaType_Type())
sfpsOutPortConfigMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigMediaType.setStatus(_A)
_SfpsOutPortConfigFrontPanelPort_Type=SfpsSwitchPort
_SfpsOutPortConfigFrontPanelPort_Object=MibTableColumn
sfpsOutPortConfigFrontPanelPort=_SfpsOutPortConfigFrontPanelPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,13),_SfpsOutPortConfigFrontPanelPort_Type())
sfpsOutPortConfigFrontPanelPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigFrontPanelPort.setStatus(_A)
class _SfpsOutPortConfigLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_j,2),(_k,3),('linkNA',4)))
_SfpsOutPortConfigLinkStatus_Type.__name__=_C
_SfpsOutPortConfigLinkStatus_Object=MibTableColumn
sfpsOutPortConfigLinkStatus=_SfpsOutPortConfigLinkStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,14),_SfpsOutPortConfigLinkStatus_Type())
sfpsOutPortConfigLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigLinkStatus.setStatus(_A)
_SfpsOutPortConfigLinkStateAge_Type=TimeTicks
_SfpsOutPortConfigLinkStateAge_Object=MibTableColumn
sfpsOutPortConfigLinkStateAge=_SfpsOutPortConfigLinkStateAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,15),_SfpsOutPortConfigLinkStateAge_Type())
sfpsOutPortConfigLinkStateAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigLinkStateAge.setStatus(_A)
class _SfpsOutPortConfigRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_l,2),(_m,3)))
_SfpsOutPortConfigRouterPort_Type.__name__=_C
_SfpsOutPortConfigRouterPort_Object=MibTableColumn
sfpsOutPortConfigRouterPort=_SfpsOutPortConfigRouterPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,16),_SfpsOutPortConfigRouterPort_Type())
sfpsOutPortConfigRouterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigRouterPort.setStatus(_A)
_SfpsOutPortConfigSlotNumber_Type=Integer32
_SfpsOutPortConfigSlotNumber_Object=MibTableColumn
sfpsOutPortConfigSlotNumber=_SfpsOutPortConfigSlotNumber_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,17),_SfpsOutPortConfigSlotNumber_Type())
sfpsOutPortConfigSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigSlotNumber.setStatus(_A)
_SfpsOutPortConfigMib2PortId_Type=Integer32
_SfpsOutPortConfigMib2PortId_Object=MibTableColumn
sfpsOutPortConfigMib2PortId=_SfpsOutPortConfigMib2PortId_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,2,1,18),_SfpsOutPortConfigMib2PortId_Type())
sfpsOutPortConfigMib2PortId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortConfigMib2PortId.setStatus(_A)
_SfpsPortAttributePort_Type=Integer32
_SfpsPortAttributePort_Object=MibScalar
sfpsPortAttributePort=_SfpsPortAttributePort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,9,1,1),_SfpsPortAttributePort_Type())
sfpsPortAttributePort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPortAttributePort.setStatus(_A)
_SfpsPortAttributeAttributes_Type=HexInteger
_SfpsPortAttributeAttributes_Object=MibScalar
sfpsPortAttributeAttributes=_SfpsPortAttributeAttributes_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,9,1,2),_SfpsPortAttributeAttributes_Type())
sfpsPortAttributeAttributes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPortAttributeAttributes.setStatus(_A)
class _SfpsPortAttributeLearnSelfArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_SfpsPortAttributeLearnSelfArp_Type.__name__=_C
_SfpsPortAttributeLearnSelfArp_Object=MibScalar
sfpsPortAttributeLearnSelfArp=_SfpsPortAttributeLearnSelfArp_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,9,1,3),_SfpsPortAttributeLearnSelfArp_Type())
sfpsPortAttributeLearnSelfArp.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPortAttributeLearnSelfArp.setStatus(_A)
class _SfpsPortAttributeAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('resetAll',2),('resetPort',3),('enablePortAttr',4),('disablePortAttr',5)))
_SfpsPortAttributeAPIVerb_Type.__name__=_C
_SfpsPortAttributeAPIVerb_Object=MibScalar
sfpsPortAttributeAPIVerb=_SfpsPortAttributeAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,9,2,1),_SfpsPortAttributeAPIVerb_Type())
sfpsPortAttributeAPIVerb.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsPortAttributeAPIVerb.setStatus(_A)
_SfpsPortAttributeAPIPort_Type=Integer32
_SfpsPortAttributeAPIPort_Object=MibScalar
sfpsPortAttributeAPIPort=_SfpsPortAttributeAPIPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,9,2,2),_SfpsPortAttributeAPIPort_Type())
sfpsPortAttributeAPIPort.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsPortAttributeAPIPort.setStatus(_A)
class _SfpsPortAttributeAPIAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('learnSelfArp',1),('none',2)))
_SfpsPortAttributeAPIAttribute_Type.__name__=_C
_SfpsPortAttributeAPIAttribute_Object=MibScalar
sfpsPortAttributeAPIAttribute=_SfpsPortAttributeAPIAttribute_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,1,9,2,3),_SfpsPortAttributeAPIAttribute_Type())
sfpsPortAttributeAPIAttribute.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsPortAttributeAPIAttribute.setStatus(_A)
_SfpsInPortStatsTable_Object=MibTable
sfpsInPortStatsTable=_SfpsInPortStatsTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1))
if mibBuilder.loadTexts:sfpsInPortStatsTable.setStatus(_A)
_SfpsInPortStatsEntry_Object=MibTableRow
sfpsInPortStatsEntry=_SfpsInPortStatsEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1))
sfpsInPortStatsEntry.setIndexNames((0,_H,_o))
if mibBuilder.loadTexts:sfpsInPortStatsEntry.setStatus(_A)
_SfpsInPortStatsPort_Type=SfpsSwitchPort
_SfpsInPortStatsPort_Object=MibTableColumn
sfpsInPortStatsPort=_SfpsInPortStatsPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,1),_SfpsInPortStatsPort_Type())
sfpsInPortStatsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsPort.setStatus(_A)
class _SfpsInPortStatsAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_F,2),(_G,3)))
_SfpsInPortStatsAdminStatus_Type.__name__=_C
_SfpsInPortStatsAdminStatus_Object=MibTableColumn
sfpsInPortStatsAdminStatus=_SfpsInPortStatsAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,2),_SfpsInPortStatsAdminStatus_Type())
sfpsInPortStatsAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsInPortStatsAdminStatus.setStatus(_A)
class _SfpsInPortStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('reset',2)))
_SfpsInPortStatsReset_Type.__name__=_C
_SfpsInPortStatsReset_Object=MibTableColumn
sfpsInPortStatsReset=_SfpsInPortStatsReset_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,3),_SfpsInPortStatsReset_Type())
sfpsInPortStatsReset.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsInPortStatsReset.setStatus(_A)
_SfpsInPortStatsOperTime_Type=TimeTicks
_SfpsInPortStatsOperTime_Object=MibTableColumn
sfpsInPortStatsOperTime=_SfpsInPortStatsOperTime_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,4),_SfpsInPortStatsOperTime_Type())
sfpsInPortStatsOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsOperTime.setStatus(_A)
_SfpsInPortStatsPkts_Type=Counter32
_SfpsInPortStatsPkts_Object=MibTableColumn
sfpsInPortStatsPkts=_SfpsInPortStatsPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,5),_SfpsInPortStatsPkts_Type())
sfpsInPortStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsPkts.setStatus(_A)
_SfpsInPortStatsDiscardPkts_Type=Counter32
_SfpsInPortStatsDiscardPkts_Object=MibTableColumn
sfpsInPortStatsDiscardPkts=_SfpsInPortStatsDiscardPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,6),_SfpsInPortStatsDiscardPkts_Type())
sfpsInPortStatsDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsDiscardPkts.setStatus(_A)
_SfpsInPortStatsBytes_Type=Counter32
_SfpsInPortStatsBytes_Object=MibTableColumn
sfpsInPortStatsBytes=_SfpsInPortStatsBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,7),_SfpsInPortStatsBytes_Type())
sfpsInPortStatsBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsBytes.setStatus(_A)
_SfpsInPortStatsDiscardBytes_Type=Counter32
_SfpsInPortStatsDiscardBytes_Object=MibTableColumn
sfpsInPortStatsDiscardBytes=_SfpsInPortStatsDiscardBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,8),_SfpsInPortStatsDiscardBytes_Type())
sfpsInPortStatsDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsDiscardBytes.setStatus(_A)
_SfpsInPortStatsQOverflows_Type=Counter32
_SfpsInPortStatsQOverflows_Object=MibTableColumn
sfpsInPortStatsQOverflows=_SfpsInPortStatsQOverflows_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,9),_SfpsInPortStatsQOverflows_Type())
sfpsInPortStatsQOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsQOverflows.setStatus(_A)
_SfpsInPortStatsLinkUps_Type=Counter32
_SfpsInPortStatsLinkUps_Object=MibTableColumn
sfpsInPortStatsLinkUps=_SfpsInPortStatsLinkUps_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,10),_SfpsInPortStatsLinkUps_Type())
sfpsInPortStatsLinkUps.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsLinkUps.setStatus(_A)
_SfpsInPortStatsLinkDowns_Type=Counter32
_SfpsInPortStatsLinkDowns_Object=MibTableColumn
sfpsInPortStatsLinkDowns=_SfpsInPortStatsLinkDowns_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,1,1,11),_SfpsInPortStatsLinkDowns_Type())
sfpsInPortStatsLinkDowns.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsInPortStatsLinkDowns.setStatus(_A)
_SfpsOutPortStatsTable_Object=MibTable
sfpsOutPortStatsTable=_SfpsOutPortStatsTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2))
if mibBuilder.loadTexts:sfpsOutPortStatsTable.setStatus(_A)
_SfpsOutPortStatsEntry_Object=MibTableRow
sfpsOutPortStatsEntry=_SfpsOutPortStatsEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1))
sfpsOutPortStatsEntry.setIndexNames((0,_H,_p))
if mibBuilder.loadTexts:sfpsOutPortStatsEntry.setStatus(_A)
_SfpsOutPortStatsPort_Type=SfpsSwitchPort
_SfpsOutPortStatsPort_Object=MibTableColumn
sfpsOutPortStatsPort=_SfpsOutPortStatsPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,1),_SfpsOutPortStatsPort_Type())
sfpsOutPortStatsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsPort.setStatus(_A)
class _SfpsOutPortStatsAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_F,2),(_G,3)))
_SfpsOutPortStatsAdminStatus_Type.__name__=_C
_SfpsOutPortStatsAdminStatus_Object=MibTableColumn
sfpsOutPortStatsAdminStatus=_SfpsOutPortStatsAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,2),_SfpsOutPortStatsAdminStatus_Type())
sfpsOutPortStatsAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsOutPortStatsAdminStatus.setStatus(_A)
class _SfpsOutPortStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('reset',2)))
_SfpsOutPortStatsReset_Type.__name__=_C
_SfpsOutPortStatsReset_Object=MibTableColumn
sfpsOutPortStatsReset=_SfpsOutPortStatsReset_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,3),_SfpsOutPortStatsReset_Type())
sfpsOutPortStatsReset.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsOutPortStatsReset.setStatus(_A)
_SfpsOutPortStatsOperTime_Type=TimeTicks
_SfpsOutPortStatsOperTime_Object=MibTableColumn
sfpsOutPortStatsOperTime=_SfpsOutPortStatsOperTime_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,4),_SfpsOutPortStatsOperTime_Type())
sfpsOutPortStatsOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsOperTime.setStatus(_A)
_SfpsOutPortStatsPkts_Type=Counter32
_SfpsOutPortStatsPkts_Object=MibTableColumn
sfpsOutPortStatsPkts=_SfpsOutPortStatsPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,5),_SfpsOutPortStatsPkts_Type())
sfpsOutPortStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsPkts.setStatus(_A)
_SfpsOutPortStatsDiscardPkts_Type=Counter32
_SfpsOutPortStatsDiscardPkts_Object=MibTableColumn
sfpsOutPortStatsDiscardPkts=_SfpsOutPortStatsDiscardPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,6),_SfpsOutPortStatsDiscardPkts_Type())
sfpsOutPortStatsDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsDiscardPkts.setStatus(_A)
_SfpsOutPortStatsBytes_Type=Counter32
_SfpsOutPortStatsBytes_Object=MibTableColumn
sfpsOutPortStatsBytes=_SfpsOutPortStatsBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,7),_SfpsOutPortStatsBytes_Type())
sfpsOutPortStatsBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsBytes.setStatus(_A)
_SfpsOutPortStatsDiscardBytes_Type=Counter32
_SfpsOutPortStatsDiscardBytes_Object=MibTableColumn
sfpsOutPortStatsDiscardBytes=_SfpsOutPortStatsDiscardBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,8),_SfpsOutPortStatsDiscardBytes_Type())
sfpsOutPortStatsDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsDiscardBytes.setStatus(_A)
_SfpsOutPortStatsQOverflows_Type=Counter32
_SfpsOutPortStatsQOverflows_Object=MibTableColumn
sfpsOutPortStatsQOverflows=_SfpsOutPortStatsQOverflows_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,9),_SfpsOutPortStatsQOverflows_Type())
sfpsOutPortStatsQOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsQOverflows.setStatus(_A)
_SfpsOutPortStatsLinkUps_Type=Counter32
_SfpsOutPortStatsLinkUps_Object=MibTableColumn
sfpsOutPortStatsLinkUps=_SfpsOutPortStatsLinkUps_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,10),_SfpsOutPortStatsLinkUps_Type())
sfpsOutPortStatsLinkUps.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsLinkUps.setStatus(_A)
_SfpsOutPortStatsLinkDowns_Type=Counter32
_SfpsOutPortStatsLinkDowns_Object=MibTableColumn
sfpsOutPortStatsLinkDowns=_SfpsOutPortStatsLinkDowns_Object((1,3,6,1,4,1,52,4,2,4,2,1,2,2,2,1,11),_SfpsOutPortStatsLinkDowns_Type())
sfpsOutPortStatsLinkDowns.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsOutPortStatsLinkDowns.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'SfpsSwitchPort':SfpsSwitchPort,'HexInteger':HexInteger,'sfpsInPortConfigTable':sfpsInPortConfigTable,'sfpsInPortConfigEntry':sfpsInPortConfigEntry,_J:sfpsInPortConfigPort,'sfpsInPortConfigAdminStatus':sfpsInPortConfigAdminStatus,'sfpsInPortConfigOperStatus':sfpsInPortConfigOperStatus,'sfpsInPortConfigOperTime':sfpsInPortConfigOperTime,'sfpsInPortConfigType':sfpsInPortConfigType,'sfpsInPortConfigReservedBW':sfpsInPortConfigReservedBW,'sfpsInPortConfigAllocBW':sfpsInPortConfigAllocBW,'sfpsInPortConfigQoS':sfpsInPortConfigQoS,'sfpsInPortConfigQSize':sfpsInPortConfigQSize,'sfpsInPortConfigQLen':sfpsInPortConfigQLen,'sfpsInPortConfigSwitchId':sfpsInPortConfigSwitchId,'sfpsInPortConfigMediaType':sfpsInPortConfigMediaType,'sfpsInPortConfigFrontPanelPort':sfpsInPortConfigFrontPanelPort,'sfpsInPortConfigLinkStatus':sfpsInPortConfigLinkStatus,'sfpsInPortConfigLinkStateAge':sfpsInPortConfigLinkStateAge,'sfpsInPortConfigRouterPort':sfpsInPortConfigRouterPort,'sfpsInPortConfigSlotNumber':sfpsInPortConfigSlotNumber,'sfpsInPortConfigMib2PortId':sfpsInPortConfigMib2PortId,'sfpsInPortConfigTopoAgent':sfpsInPortConfigTopoAgent,'sfpsInPortConfigLayer3Learning':sfpsInPortConfigLayer3Learning,'sfpsOutPortConfigTable':sfpsOutPortConfigTable,'sfpsOutPortConfigEntry':sfpsOutPortConfigEntry,_n:sfpsOutPortConfigPort,'sfpsOutPortConfigAdminStatus':sfpsOutPortConfigAdminStatus,'sfpsOutPortConfigOperStatus':sfpsOutPortConfigOperStatus,'sfpsOutPortConfigOperTime':sfpsOutPortConfigOperTime,'sfpsOutPortConfigType':sfpsOutPortConfigType,'sfpsOutPortConfigReservedBW':sfpsOutPortConfigReservedBW,'sfpsOutPortConfigAllocBW':sfpsOutPortConfigAllocBW,'sfpsOutPortConfigQoS':sfpsOutPortConfigQoS,'sfpsOutPortConfigQSize':sfpsOutPortConfigQSize,'sfpsOutPortConfigQLen':sfpsOutPortConfigQLen,'sfpsOutPortConfigSwitchId':sfpsOutPortConfigSwitchId,'sfpsOutPortConfigMediaType':sfpsOutPortConfigMediaType,'sfpsOutPortConfigFrontPanelPort':sfpsOutPortConfigFrontPanelPort,'sfpsOutPortConfigLinkStatus':sfpsOutPortConfigLinkStatus,'sfpsOutPortConfigLinkStateAge':sfpsOutPortConfigLinkStateAge,'sfpsOutPortConfigRouterPort':sfpsOutPortConfigRouterPort,'sfpsOutPortConfigSlotNumber':sfpsOutPortConfigSlotNumber,'sfpsOutPortConfigMib2PortId':sfpsOutPortConfigMib2PortId,'sfpsPortAttributePort':sfpsPortAttributePort,'sfpsPortAttributeAttributes':sfpsPortAttributeAttributes,'sfpsPortAttributeLearnSelfArp':sfpsPortAttributeLearnSelfArp,'sfpsPortAttributeAPIVerb':sfpsPortAttributeAPIVerb,'sfpsPortAttributeAPIPort':sfpsPortAttributeAPIPort,'sfpsPortAttributeAPIAttribute':sfpsPortAttributeAPIAttribute,'sfpsInPortStatsTable':sfpsInPortStatsTable,'sfpsInPortStatsEntry':sfpsInPortStatsEntry,_o:sfpsInPortStatsPort,'sfpsInPortStatsAdminStatus':sfpsInPortStatsAdminStatus,'sfpsInPortStatsReset':sfpsInPortStatsReset,'sfpsInPortStatsOperTime':sfpsInPortStatsOperTime,'sfpsInPortStatsPkts':sfpsInPortStatsPkts,'sfpsInPortStatsDiscardPkts':sfpsInPortStatsDiscardPkts,'sfpsInPortStatsBytes':sfpsInPortStatsBytes,'sfpsInPortStatsDiscardBytes':sfpsInPortStatsDiscardBytes,'sfpsInPortStatsQOverflows':sfpsInPortStatsQOverflows,'sfpsInPortStatsLinkUps':sfpsInPortStatsLinkUps,'sfpsInPortStatsLinkDowns':sfpsInPortStatsLinkDowns,'sfpsOutPortStatsTable':sfpsOutPortStatsTable,'sfpsOutPortStatsEntry':sfpsOutPortStatsEntry,_p:sfpsOutPortStatsPort,'sfpsOutPortStatsAdminStatus':sfpsOutPortStatsAdminStatus,'sfpsOutPortStatsReset':sfpsOutPortStatsReset,'sfpsOutPortStatsOperTime':sfpsOutPortStatsOperTime,'sfpsOutPortStatsPkts':sfpsOutPortStatsPkts,'sfpsOutPortStatsDiscardPkts':sfpsOutPortStatsDiscardPkts,'sfpsOutPortStatsBytes':sfpsOutPortStatsBytes,'sfpsOutPortStatsDiscardBytes':sfpsOutPortStatsDiscardBytes,'sfpsOutPortStatsQOverflows':sfpsOutPortStatsQOverflows,'sfpsOutPortStatsLinkUps':sfpsOutPortStatsLinkUps,'sfpsOutPortStatsLinkDowns':sfpsOutPortStatsLinkDowns})