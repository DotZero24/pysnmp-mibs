_K='portIndex'
_J='trapManagerIndex'
_I='NotificationType'
_H='ZYXEL-MES2110-MIB'
_G='enable'
_F='disable'
_E='read-only'
_D='Integer32'
_C='DisplayString'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
_Zyxel_ObjectIdentity=ObjectIdentity
zyxel=_Zyxel_ObjectIdentity((1,3,6,1,4,1,890))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,890,1))
_AccessSwitch_ObjectIdentity=ObjectIdentity
accessSwitch=_AccessSwitch_ObjectIdentity((1,3,6,1,4,1,890,1,5))
_EsSeries_ObjectIdentity=ObjectIdentity
esSeries=_EsSeries_ObjectIdentity((1,3,6,1,4,1,890,1,5,8))
_Mes2110_MIB_ObjectIdentity=ObjectIdentity
mes2110_MIB=_Mes2110_MIB_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,2110))
_Mes2110_SystemInfo_ObjectIdentity=ObjectIdentity
mes2110_SystemInfo=_Mes2110_SystemInfo_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,2110,1))
class _Mes2110_SystemContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Mes2110_SystemContact_Type.__name__=_C
_Mes2110_SystemContact_Object=MibScalar
mes2110_SystemContact=_Mes2110_SystemContact_Object((1,3,6,1,4,1,890,1,5,8,2110,1,1),_Mes2110_SystemContact_Type())
mes2110_SystemContact.setMaxAccess(_B)
if mibBuilder.loadTexts:mes2110_SystemContact.setStatus(_A)
class _Mes2110_SystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Mes2110_SystemName_Type.__name__=_C
_Mes2110_SystemName_Object=MibScalar
mes2110_SystemName=_Mes2110_SystemName_Object((1,3,6,1,4,1,890,1,5,8,2110,1,2),_Mes2110_SystemName_Type())
mes2110_SystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:mes2110_SystemName.setStatus(_A)
class _Mes2110_SystemLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Mes2110_SystemLocation_Type.__name__=_C
_Mes2110_SystemLocation_Object=MibScalar
mes2110_SystemLocation=_Mes2110_SystemLocation_Object((1,3,6,1,4,1,890,1,5,8,2110,1,3),_Mes2110_SystemLocation_Type())
mes2110_SystemLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:mes2110_SystemLocation.setStatus(_A)
_Mes2110_Mgt_ObjectIdentity=ObjectIdentity
mes2110_Mgt=_Mes2110_Mgt_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,2110,2))
class _Mes2110_MgtSnmpVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v1',1),('v2c',2)))
_Mes2110_MgtSnmpVer_Type.__name__=_D
_Mes2110_MgtSnmpVer_Object=MibScalar
mes2110_MgtSnmpVer=_Mes2110_MgtSnmpVer_Object((1,3,6,1,4,1,890,1,5,8,2110,2,1),_Mes2110_MgtSnmpVer_Type())
mes2110_MgtSnmpVer.setMaxAccess(_E)
if mibBuilder.loadTexts:mes2110_MgtSnmpVer.setStatus(_A)
class _Mes2110_MgtModPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Mes2110_MgtModPN_Type.__name__=_C
_Mes2110_MgtModPN_Object=MibScalar
mes2110_MgtModPN=_Mes2110_MgtModPN_Object((1,3,6,1,4,1,890,1,5,8,2110,2,2),_Mes2110_MgtModPN_Type())
mes2110_MgtModPN.setMaxAccess(_E)
if mibBuilder.loadTexts:mes2110_MgtModPN.setStatus(_A)
class _Mes2110_MgtModSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Mes2110_MgtModSN_Type.__name__=_C
_Mes2110_MgtModSN_Object=MibScalar
mes2110_MgtModSN=_Mes2110_MgtModSN_Object((1,3,6,1,4,1,890,1,5,8,2110,2,3),_Mes2110_MgtModSN_Type())
mes2110_MgtModSN.setMaxAccess(_E)
if mibBuilder.loadTexts:mes2110_MgtModSN.setStatus(_A)
class _Mes2110_MgtModManuDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Mes2110_MgtModManuDate_Type.__name__=_C
_Mes2110_MgtModManuDate_Object=MibScalar
mes2110_MgtModManuDate=_Mes2110_MgtModManuDate_Object((1,3,6,1,4,1,890,1,5,8,2110,2,4),_Mes2110_MgtModManuDate_Type())
mes2110_MgtModManuDate.setMaxAccess(_E)
if mibBuilder.loadTexts:mes2110_MgtModManuDate.setStatus(_A)
class _Mes2110_MgtModRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Mes2110_MgtModRev_Type.__name__=_C
_Mes2110_MgtModRev_Object=MibScalar
mes2110_MgtModRev=_Mes2110_MgtModRev_Object((1,3,6,1,4,1,890,1,5,8,2110,2,5),_Mes2110_MgtModRev_Type())
mes2110_MgtModRev.setMaxAccess(_E)
if mibBuilder.loadTexts:mes2110_MgtModRev.setStatus(_A)
class _Mes2110_MgtModDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_Mes2110_MgtModDesc_Type.__name__=_C
_Mes2110_MgtModDesc_Object=MibScalar
mes2110_MgtModDesc=_Mes2110_MgtModDesc_Object((1,3,6,1,4,1,890,1,5,8,2110,2,6),_Mes2110_MgtModDesc_Type())
mes2110_MgtModDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:mes2110_MgtModDesc.setStatus(_A)
class _CommunityStringRO_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CommunityStringRO_Type.__name__=_C
_CommunityStringRO_Object=MibScalar
communityStringRO=_CommunityStringRO_Object((1,3,6,1,4,1,890,1,5,8,2110,2,7),_CommunityStringRO_Type())
communityStringRO.setMaxAccess(_B)
if mibBuilder.loadTexts:communityStringRO.setStatus(_A)
class _CommunityStringRW_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CommunityStringRW_Type.__name__=_C
_CommunityStringRW_Object=MibScalar
communityStringRW=_CommunityStringRW_Object((1,3,6,1,4,1,890,1,5,8,2110,2,8),_CommunityStringRW_Type())
communityStringRW.setMaxAccess(_B)
if mibBuilder.loadTexts:communityStringRW.setStatus(_A)
_DefaultGateway_Type=IpAddress
_DefaultGateway_Object=MibScalar
defaultGateway=_DefaultGateway_Object((1,3,6,1,4,1,890,1,5,8,2110,2,9),_DefaultGateway_Type())
defaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultGateway.setStatus(_A)
_InterfaceIpAddress_Type=IpAddress
_InterfaceIpAddress_Object=MibScalar
interfaceIpAddress=_InterfaceIpAddress_Object((1,3,6,1,4,1,890,1,5,8,2110,2,10),_InterfaceIpAddress_Type())
interfaceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceIpAddress.setStatus(_A)
_InterfaceSubnetMask_Type=IpAddress
_InterfaceSubnetMask_Object=MibScalar
interfaceSubnetMask=_InterfaceSubnetMask_Object((1,3,6,1,4,1,890,1,5,8,2110,2,11),_InterfaceSubnetMask_Type())
interfaceSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceSubnetMask.setStatus(_A)
class _MgtStp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_MgtStp_Type.__name__=_D
_MgtStp_Object=MibScalar
mgtStp=_MgtStp_Object((1,3,6,1,4,1,890,1,5,8,2110,2,12),_MgtStp_Type())
mgtStp.setMaxAccess(_B)
if mibBuilder.loadTexts:mgtStp.setStatus(_A)
_TrapManagerTable_Object=MibTable
trapManagerTable=_TrapManagerTable_Object((1,3,6,1,4,1,890,1,5,8,2110,2,13))
if mibBuilder.loadTexts:trapManagerTable.setStatus(_A)
_TrapManagerTableEntry_Object=MibTableRow
trapManagerTableEntry=_TrapManagerTableEntry_Object((1,3,6,1,4,1,890,1,5,8,2110,2,13,1))
trapManagerTableEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:trapManagerTableEntry.setStatus(_A)
_TrapManagerIndex_Type=Integer32
_TrapManagerIndex_Object=MibTableColumn
trapManagerIndex=_TrapManagerIndex_Object((1,3,6,1,4,1,890,1,5,8,2110,2,13,1,1),_TrapManagerIndex_Type())
trapManagerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:trapManagerIndex.setStatus(_A)
_TrapManagerIpAddress_Type=IpAddress
_TrapManagerIpAddress_Object=MibTableColumn
trapManagerIpAddress=_TrapManagerIpAddress_Object((1,3,6,1,4,1,890,1,5,8,2110,2,13,1,2),_TrapManagerIpAddress_Type())
trapManagerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:trapManagerIpAddress.setStatus(_A)
class _TrapManagerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TrapManagerName_Type.__name__=_C
_TrapManagerName_Object=MibTableColumn
trapManagerName=_TrapManagerName_Object((1,3,6,1,4,1,890,1,5,8,2110,2,13,1,3),_TrapManagerName_Type())
trapManagerName.setMaxAccess(_B)
if mibBuilder.loadTexts:trapManagerName.setStatus(_A)
class _TrapManagerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_TrapManagerStatus_Type.__name__=_D
_TrapManagerStatus_Object=MibTableColumn
trapManagerStatus=_TrapManagerStatus_Object((1,3,6,1,4,1,890,1,5,8,2110,2,13,1,4),_TrapManagerStatus_Type())
trapManagerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:trapManagerStatus.setStatus(_A)
_Mes2110_Port_ObjectIdentity=ObjectIdentity
mes2110_Port=_Mes2110_Port_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,2110,3))
_Mes2110_PortTable_Object=MibTable
mes2110_PortTable=_Mes2110_PortTable_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1))
if mibBuilder.loadTexts:mes2110_PortTable.setStatus(_A)
_Mes2110_PortEntry_Object=MibTableRow
mes2110_PortEntry=_Mes2110_PortEntry_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1))
mes2110_PortEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:mes2110_PortEntry.setStatus(_A)
class _PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_PortIndex_Type.__name__=_D
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_PortName_Type.__name__=_C
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1,2),_PortName_Type())
portName.setMaxAccess(_B)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_F,1),(_G,4)))
_PortAdminStatus_Type.__name__=_D
_PortAdminStatus_Object=MibTableColumn
portAdminStatus=_PortAdminStatus_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1,3),_PortAdminStatus_Type())
portAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portAdminStatus.setStatus(_A)
class _PortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_PortLinkStatus_Type.__name__=_D
_PortLinkStatus_Object=MibTableColumn
portLinkStatus=_PortLinkStatus_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1,4),_PortLinkStatus_Type())
portLinkStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portLinkStatus.setStatus(_A)
class _PortSpeedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('speed-10M',1),('speed-100M',2),('speed-1000M',3)))
_PortSpeedMode_Type.__name__=_D
_PortSpeedMode_Object=MibTableColumn
portSpeedMode=_PortSpeedMode_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1,5),_PortSpeedMode_Type())
portSpeedMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portSpeedMode.setStatus(_A)
class _PortDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half',1),('full',2)))
_PortDuplexMode_Type.__name__=_D
_PortDuplexMode_Object=MibTableColumn
portDuplexMode=_PortDuplexMode_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1,6),_PortDuplexMode_Type())
portDuplexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portDuplexMode.setStatus(_A)
class _PortAuto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortAuto_Type.__name__=_D
_PortAuto_Object=MibTableColumn
portAuto=_PortAuto_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1,7),_PortAuto_Type())
portAuto.setMaxAccess(_B)
if mibBuilder.loadTexts:portAuto.setStatus(_A)
class _PortFfc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFfc_Type.__name__=_D
_PortFfc_Object=MibTableColumn
portFfc=_PortFfc_Object((1,3,6,1,4,1,890,1,5,8,2110,3,1,1,8),_PortFfc_Type())
portFfc.setMaxAccess(_B)
if mibBuilder.loadTexts:portFfc.setStatus(_A)
_Mes2110_Traps_ObjectIdentity=ObjectIdentity
mes2110_Traps=_Mes2110_Traps_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,2110,4))
almColdStart=NotificationType((1,3,6,1,4,1,890,1,5,8,2110,4,0,1))
if mibBuilder.loadTexts:almColdStart.setStatus('')
almWarmStart=NotificationType((1,3,6,1,4,1,890,1,5,8,2110,4,0,2))
if mibBuilder.loadTexts:almWarmStart.setStatus('')
almLinkUp=NotificationType((1,3,6,1,4,1,890,1,5,8,2110,4,0,3))
if mibBuilder.loadTexts:almLinkUp.setStatus('')
almLinkDown=NotificationType((1,3,6,1,4,1,890,1,5,8,2110,4,0,4))
if mibBuilder.loadTexts:almLinkDown.setStatus('')
almConfChange=NotificationType((1,3,6,1,4,1,890,1,5,8,2110,4,0,5))
if mibBuilder.loadTexts:almConfChange.setStatus('')
mibBuilder.exportSymbols(_H,**{'zyxel':zyxel,'products':products,'accessSwitch':accessSwitch,'esSeries':esSeries,'mes2110_MIB':mes2110_MIB,'mes2110_SystemInfo':mes2110_SystemInfo,'mes2110_SystemContact':mes2110_SystemContact,'mes2110_SystemName':mes2110_SystemName,'mes2110_SystemLocation':mes2110_SystemLocation,'mes2110_Mgt':mes2110_Mgt,'mes2110_MgtSnmpVer':mes2110_MgtSnmpVer,'mes2110_MgtModPN':mes2110_MgtModPN,'mes2110_MgtModSN':mes2110_MgtModSN,'mes2110_MgtModManuDate':mes2110_MgtModManuDate,'mes2110_MgtModRev':mes2110_MgtModRev,'mes2110_MgtModDesc':mes2110_MgtModDesc,'communityStringRO':communityStringRO,'communityStringRW':communityStringRW,'defaultGateway':defaultGateway,'interfaceIpAddress':interfaceIpAddress,'interfaceSubnetMask':interfaceSubnetMask,'mgtStp':mgtStp,'trapManagerTable':trapManagerTable,'trapManagerTableEntry':trapManagerTableEntry,_J:trapManagerIndex,'trapManagerIpAddress':trapManagerIpAddress,'trapManagerName':trapManagerName,'trapManagerStatus':trapManagerStatus,'mes2110_Port':mes2110_Port,'mes2110_PortTable':mes2110_PortTable,'mes2110_PortEntry':mes2110_PortEntry,_K:portIndex,'portName':portName,'portAdminStatus':portAdminStatus,'portLinkStatus':portLinkStatus,'portSpeedMode':portSpeedMode,'portDuplexMode':portDuplexMode,'portAuto':portAuto,'portFfc':portFfc,'mes2110_Traps':mes2110_Traps,'almColdStart':almColdStart,'almWarmStart':almWarmStart,'almLinkUp':almLinkUp,'almLinkDown':almLinkDown,'almConfChange':almConfChange})