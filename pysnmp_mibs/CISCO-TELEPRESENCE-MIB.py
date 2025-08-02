_AZ='ciscoTpDPPeripheralStatusGroup'
_AY='ciscoTpPeripheralStatusGroupR01'
_AX='ctpPeriStatusChangeNotification'
_AW='ctpPeripheralErrorNotification'
_AV='ctpDPPeripheralPowerStatus'
_AU='ctpDPPeripheralCableStatus'
_AT='ctpDefaultGatewayAddrType'
_AS='ctpDefaultGateway'
_AR='ctpVlanId'
_AQ='ctp802dot11PeripheralLinkStatus'
_AP='ctp802dot11PeripheralLinkStrength'
_AO='ctp802dot11PeripheralAddr'
_AN='ctp802dot11PeripheralAddrType'
_AM='ctp802dot11PeripheralIfIndex'
_AL='ctpUSBPeripheralPortRate'
_AK='ctpUSBPeripheralPortType'
_AJ='ctpUSBPeripheralPowerStatus'
_AI='ctpUSBPeripheralCableStatus'
_AH='ctpPeriStatusChangeNotifyEnable'
_AG='ctpPeripheralAttributeValue'
_AF='ctpPeripheralAttributeDescr'
_AE='ctpRS232PeripheralConnStatus'
_AD='ctpRS232PortIndex'
_AC='ctpPeripheralErrorNotifyEnable'
_AB='ctpSysUserAuthFailHistoryIndex'
_AA='ctpPeripheralErrorHistoryIndex'
_A9='ctpDPPeripheralIndex'
_A8='ctp802dot11PeripheralIndex'
_A7='ctpUSBPeripheralIndex'
_A6='ctpPeripheralAttributeIndex'
_A5='ctpRS232PeripheralIndex'
_A4='ctpDVIPeripheralIndex'
_A3='ctpHDMIPeripheralIndex'
_A2='ctpEtherPeripheralIndex'
_A1='CtpSystemResetMode'
_A0='internalError'
_z='ciscoTpConfigurationGroupR02'
_y='ciscoTpNotificationGroup'
_x='ciscoTpEventHistoryGroup'
_w='ciscoTpPeripheralStatusGroup'
_v='ciscoTpConfigurationGroup'
_u='ctpSysUserAuthFailNotification'
_t='ctpPeripheralErrorDeviceNumber'
_s='ctpPeripheralErrorDeviceCategory'
_r='ctpPeripheralDeviceNumber'
_q='ctpPeripheralDeviceCategory'
_p='ctpSysUserAuthFailTimeStamp'
_o='ctpSysUserAuthFailHistLastIndex'
_n='ctpSysUserAuthFailHistTableSize'
_m='ctpPeripheralErrorTimeStamp'
_l='ctpPeripheralErrorHistLastIndex'
_k='ctpPeripheralErrorHistTableSize'
_j='ctpSystemReset'
_i='ctpSysUserAuthFailNotifyEnable'
_h='SnmpAdminString'
_g='ciscoTpPeripheralStatusGroupR02'
_f='ctpSysUserAuthFailAccessProtocol'
_e='ctpSysUserAuthFailUserName'
_d='ctpSysUserAuthFailSourcePort'
_c='ctpSysUserAuthFailSourceAddr'
_b='ctpSysUserAuthFailSourceAddrType'
_a='ctpDVIPeripheralCableStatus'
_Z='ctpHDMIPeripheralPowerStatus'
_Y='ctpHDMIPeripheralCableStatus'
_X='ctpEtherPeripheralStatus'
_W='ctpEtherPeripheralAddr'
_V='ctpEtherPeripheralAddrType'
_U='ctpEtherPeripheralIfIndex'
_T='ctpPeripheralStatus'
_S='ctpPeripheralDescription'
_R='TruthValue'
_Q='ciscoTpNotificationGroupR01'
_P='ciscoTpEventHistoryGroupR01'
_O='ciscoTpConfigurationGroupR01'
_N='ctpPeripheralErrorStatus'
_M='ctpPeripheralErrorIndex'
_L='unknown'
_K='ciscoTpPeripheralAttributeGroup'
_J='ciscoTpRS232PeripheralStatusGroup'
_I='Integer32'
_H='Unsigned32'
_G='read-write'
_F='ctpPeripheralIndex'
_E='not-accessible'
_D='deprecated'
_C='read-only'
_B='current'
_A='CISCO-TELEPRESENCE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_h)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_R)
ciscoTelepresenceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,643))
if mibBuilder.loadTexts:ciscoTelepresenceMIB.setRevisions(('2014-07-18 00:00','2012-07-17 00:00','2012-03-23 00:00','2011-08-23 00:00','2010-07-23 00:00','2010-07-13 00:00','2009-07-12 00:00','2008-02-13 00:00','2007-12-11 00:00'))
class CtpSystemResetMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noRestart',1),('restartPending',2),('resetPending',3),('forceReset',4)))
class CtpPeripheralCableCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('plugged',1),('loose',2),('unplugged',3),(_L,4),(_A0,5)))
class CtpPeripheralPowerCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('on',1),('standby',2),('off',3),(_L,4),(_A0,5)))
class CtpPeripheralStatusCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noError',0),('other',1),('cableError',2),('powerError',3),('mgmtSysConfigError',4),('systemError',5),('deviceError',6),('linkError',7),('commError',8),('detectionDisabled',9)))
class CtpSystemAccessProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('http',1),('snmp',2),('ssh',3)))
class CtpPeripheralDeviceCategoryCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_L,0),('other',1),('uplinkDevice',2),('ipPhone',3),('camera',4),('display',5),('secCodec',6),('docCamera',7),('projector',8),('dviDevice',9),('presentationCodec',10),('auxiliaryControlUnit',11),('audioExpansionUnit',12),('microphone',13),('headset',14),('positionMic',15),('digitialMediaSystem',16),('auxHDMIOutputDevice',17),('uiDevice',18),('auxHDMIInputDevice',19),('bringYourOwnDevice',20)))
_CiscoTelepresenceMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoTelepresenceMIBNotifs=_CiscoTelepresenceMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,643,0))
_CiscoTelepresenceMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTelepresenceMIBObjects=_CiscoTelepresenceMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,643,1))
_CtpObjects_ObjectIdentity=ObjectIdentity
ctpObjects=_CtpObjects_ObjectIdentity((1,3,6,1,4,1,9,9,643,1,1))
class _CtpPeripheralErrorNotifyEnable_Type(TruthValue):defaultValue=2
_CtpPeripheralErrorNotifyEnable_Type.__name__=_R
_CtpPeripheralErrorNotifyEnable_Object=MibScalar
ctpPeripheralErrorNotifyEnable=_CtpPeripheralErrorNotifyEnable_Object((1,3,6,1,4,1,9,9,643,1,1,1),_CtpPeripheralErrorNotifyEnable_Type())
ctpPeripheralErrorNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpPeripheralErrorNotifyEnable.setStatus(_D)
class _CtpSysUserAuthFailNotifyEnable_Type(TruthValue):defaultValue=2
_CtpSysUserAuthFailNotifyEnable_Type.__name__=_R
_CtpSysUserAuthFailNotifyEnable_Object=MibScalar
ctpSysUserAuthFailNotifyEnable=_CtpSysUserAuthFailNotifyEnable_Object((1,3,6,1,4,1,9,9,643,1,1,2),_CtpSysUserAuthFailNotifyEnable_Type())
ctpSysUserAuthFailNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpSysUserAuthFailNotifyEnable.setStatus(_B)
class _CtpSystemReset_Type(CtpSystemResetMode):defaultValue=1
_CtpSystemReset_Type.__name__=_A1
_CtpSystemReset_Object=MibScalar
ctpSystemReset=_CtpSystemReset_Object((1,3,6,1,4,1,9,9,643,1,1,3),_CtpSystemReset_Type())
ctpSystemReset.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpSystemReset.setStatus(_B)
class _CtpPeriStatusChangeNotifyEnable_Type(TruthValue):defaultValue=2
_CtpPeriStatusChangeNotifyEnable_Type.__name__=_R
_CtpPeriStatusChangeNotifyEnable_Object=MibScalar
ctpPeriStatusChangeNotifyEnable=_CtpPeriStatusChangeNotifyEnable_Object((1,3,6,1,4,1,9,9,643,1,1,4),_CtpPeriStatusChangeNotifyEnable_Type())
ctpPeriStatusChangeNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpPeriStatusChangeNotifyEnable.setStatus(_B)
_CtpVlanId_Type=Unsigned32
_CtpVlanId_Object=MibScalar
ctpVlanId=_CtpVlanId_Object((1,3,6,1,4,1,9,9,643,1,1,5),_CtpVlanId_Type())
ctpVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpVlanId.setStatus(_B)
_CtpDefaultGatewayAddrType_Type=InetAddressType
_CtpDefaultGatewayAddrType_Object=MibScalar
ctpDefaultGatewayAddrType=_CtpDefaultGatewayAddrType_Object((1,3,6,1,4,1,9,9,643,1,1,6),_CtpDefaultGatewayAddrType_Type())
ctpDefaultGatewayAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpDefaultGatewayAddrType.setStatus(_B)
_CtpDefaultGateway_Type=InetAddress
_CtpDefaultGateway_Object=MibScalar
ctpDefaultGateway=_CtpDefaultGateway_Object((1,3,6,1,4,1,9,9,643,1,1,7),_CtpDefaultGateway_Type())
ctpDefaultGateway.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpDefaultGateway.setStatus(_B)
_CtpPeripheralStatusObjects_ObjectIdentity=ObjectIdentity
ctpPeripheralStatusObjects=_CtpPeripheralStatusObjects_ObjectIdentity((1,3,6,1,4,1,9,9,643,1,2))
_CtpPeripheralStatusTable_Object=MibTable
ctpPeripheralStatusTable=_CtpPeripheralStatusTable_Object((1,3,6,1,4,1,9,9,643,1,2,1))
if mibBuilder.loadTexts:ctpPeripheralStatusTable.setStatus(_B)
_CtpPeripheralStatusEntry_Object=MibTableRow
ctpPeripheralStatusEntry=_CtpPeripheralStatusEntry_Object((1,3,6,1,4,1,9,9,643,1,2,1,1))
ctpPeripheralStatusEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:ctpPeripheralStatusEntry.setStatus(_B)
_CtpPeripheralIndex_Type=Unsigned32
_CtpPeripheralIndex_Object=MibTableColumn
ctpPeripheralIndex=_CtpPeripheralIndex_Object((1,3,6,1,4,1,9,9,643,1,2,1,1,1),_CtpPeripheralIndex_Type())
ctpPeripheralIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpPeripheralIndex.setStatus(_B)
class _CtpPeripheralDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtpPeripheralDescription_Type.__name__=_h
_CtpPeripheralDescription_Object=MibTableColumn
ctpPeripheralDescription=_CtpPeripheralDescription_Object((1,3,6,1,4,1,9,9,643,1,2,1,1,2),_CtpPeripheralDescription_Type())
ctpPeripheralDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralDescription.setStatus(_B)
_CtpPeripheralStatus_Type=CtpPeripheralStatusCode
_CtpPeripheralStatus_Object=MibTableColumn
ctpPeripheralStatus=_CtpPeripheralStatus_Object((1,3,6,1,4,1,9,9,643,1,2,1,1,3),_CtpPeripheralStatus_Type())
ctpPeripheralStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralStatus.setStatus(_B)
_CtpPeripheralDeviceCategory_Type=CtpPeripheralDeviceCategoryCode
_CtpPeripheralDeviceCategory_Object=MibTableColumn
ctpPeripheralDeviceCategory=_CtpPeripheralDeviceCategory_Object((1,3,6,1,4,1,9,9,643,1,2,1,1,4),_CtpPeripheralDeviceCategory_Type())
ctpPeripheralDeviceCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralDeviceCategory.setStatus(_B)
_CtpPeripheralDeviceNumber_Type=Unsigned32
_CtpPeripheralDeviceNumber_Object=MibTableColumn
ctpPeripheralDeviceNumber=_CtpPeripheralDeviceNumber_Object((1,3,6,1,4,1,9,9,643,1,2,1,1,5),_CtpPeripheralDeviceNumber_Type())
ctpPeripheralDeviceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralDeviceNumber.setStatus(_B)
_CtpEtherPeripheralStatusTable_Object=MibTable
ctpEtherPeripheralStatusTable=_CtpEtherPeripheralStatusTable_Object((1,3,6,1,4,1,9,9,643,1,2,2))
if mibBuilder.loadTexts:ctpEtherPeripheralStatusTable.setStatus(_B)
_CtpEtherPeripheralStatusEntry_Object=MibTableRow
ctpEtherPeripheralStatusEntry=_CtpEtherPeripheralStatusEntry_Object((1,3,6,1,4,1,9,9,643,1,2,2,1))
ctpEtherPeripheralStatusEntry.setIndexNames((0,_A,_F),(0,_A,_A2))
if mibBuilder.loadTexts:ctpEtherPeripheralStatusEntry.setStatus(_B)
_CtpEtherPeripheralIndex_Type=Unsigned32
_CtpEtherPeripheralIndex_Object=MibTableColumn
ctpEtherPeripheralIndex=_CtpEtherPeripheralIndex_Object((1,3,6,1,4,1,9,9,643,1,2,2,1,1),_CtpEtherPeripheralIndex_Type())
ctpEtherPeripheralIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpEtherPeripheralIndex.setStatus(_B)
_CtpEtherPeripheralIfIndex_Type=InterfaceIndexOrZero
_CtpEtherPeripheralIfIndex_Object=MibTableColumn
ctpEtherPeripheralIfIndex=_CtpEtherPeripheralIfIndex_Object((1,3,6,1,4,1,9,9,643,1,2,2,1,2),_CtpEtherPeripheralIfIndex_Type())
ctpEtherPeripheralIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpEtherPeripheralIfIndex.setStatus(_B)
_CtpEtherPeripheralAddrType_Type=InetAddressType
_CtpEtherPeripheralAddrType_Object=MibTableColumn
ctpEtherPeripheralAddrType=_CtpEtherPeripheralAddrType_Object((1,3,6,1,4,1,9,9,643,1,2,2,1,3),_CtpEtherPeripheralAddrType_Type())
ctpEtherPeripheralAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpEtherPeripheralAddrType.setStatus(_B)
_CtpEtherPeripheralAddr_Type=InetAddress
_CtpEtherPeripheralAddr_Object=MibTableColumn
ctpEtherPeripheralAddr=_CtpEtherPeripheralAddr_Object((1,3,6,1,4,1,9,9,643,1,2,2,1,4),_CtpEtherPeripheralAddr_Type())
ctpEtherPeripheralAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpEtherPeripheralAddr.setStatus(_B)
_CtpEtherPeripheralStatus_Type=CtpPeripheralStatusCode
_CtpEtherPeripheralStatus_Object=MibTableColumn
ctpEtherPeripheralStatus=_CtpEtherPeripheralStatus_Object((1,3,6,1,4,1,9,9,643,1,2,2,1,5),_CtpEtherPeripheralStatus_Type())
ctpEtherPeripheralStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpEtherPeripheralStatus.setStatus(_B)
_CtpHDMIPeripheralStatusTable_Object=MibTable
ctpHDMIPeripheralStatusTable=_CtpHDMIPeripheralStatusTable_Object((1,3,6,1,4,1,9,9,643,1,2,3))
if mibBuilder.loadTexts:ctpHDMIPeripheralStatusTable.setStatus(_B)
_CtpHDMIPeripheralStatusEntry_Object=MibTableRow
ctpHDMIPeripheralStatusEntry=_CtpHDMIPeripheralStatusEntry_Object((1,3,6,1,4,1,9,9,643,1,2,3,1))
ctpHDMIPeripheralStatusEntry.setIndexNames((0,_A,_F),(0,_A,_A3))
if mibBuilder.loadTexts:ctpHDMIPeripheralStatusEntry.setStatus(_B)
_CtpHDMIPeripheralIndex_Type=Unsigned32
_CtpHDMIPeripheralIndex_Object=MibTableColumn
ctpHDMIPeripheralIndex=_CtpHDMIPeripheralIndex_Object((1,3,6,1,4,1,9,9,643,1,2,3,1,1),_CtpHDMIPeripheralIndex_Type())
ctpHDMIPeripheralIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpHDMIPeripheralIndex.setStatus(_B)
_CtpHDMIPeripheralCableStatus_Type=CtpPeripheralCableCode
_CtpHDMIPeripheralCableStatus_Object=MibTableColumn
ctpHDMIPeripheralCableStatus=_CtpHDMIPeripheralCableStatus_Object((1,3,6,1,4,1,9,9,643,1,2,3,1,2),_CtpHDMIPeripheralCableStatus_Type())
ctpHDMIPeripheralCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpHDMIPeripheralCableStatus.setStatus(_B)
_CtpHDMIPeripheralPowerStatus_Type=CtpPeripheralPowerCode
_CtpHDMIPeripheralPowerStatus_Object=MibTableColumn
ctpHDMIPeripheralPowerStatus=_CtpHDMIPeripheralPowerStatus_Object((1,3,6,1,4,1,9,9,643,1,2,3,1,3),_CtpHDMIPeripheralPowerStatus_Type())
ctpHDMIPeripheralPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpHDMIPeripheralPowerStatus.setStatus(_B)
_CtpDVIPeripheralStatusTable_Object=MibTable
ctpDVIPeripheralStatusTable=_CtpDVIPeripheralStatusTable_Object((1,3,6,1,4,1,9,9,643,1,2,4))
if mibBuilder.loadTexts:ctpDVIPeripheralStatusTable.setStatus(_B)
_CtpDVIPeripheralStatusEntry_Object=MibTableRow
ctpDVIPeripheralStatusEntry=_CtpDVIPeripheralStatusEntry_Object((1,3,6,1,4,1,9,9,643,1,2,4,1))
ctpDVIPeripheralStatusEntry.setIndexNames((0,_A,_F),(0,_A,_A4))
if mibBuilder.loadTexts:ctpDVIPeripheralStatusEntry.setStatus(_B)
_CtpDVIPeripheralIndex_Type=Unsigned32
_CtpDVIPeripheralIndex_Object=MibTableColumn
ctpDVIPeripheralIndex=_CtpDVIPeripheralIndex_Object((1,3,6,1,4,1,9,9,643,1,2,4,1,1),_CtpDVIPeripheralIndex_Type())
ctpDVIPeripheralIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpDVIPeripheralIndex.setStatus(_B)
_CtpDVIPeripheralCableStatus_Type=CtpPeripheralCableCode
_CtpDVIPeripheralCableStatus_Object=MibTableColumn
ctpDVIPeripheralCableStatus=_CtpDVIPeripheralCableStatus_Object((1,3,6,1,4,1,9,9,643,1,2,4,1,2),_CtpDVIPeripheralCableStatus_Type())
ctpDVIPeripheralCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpDVIPeripheralCableStatus.setStatus(_B)
_CtpRS232PeripheralStatusTable_Object=MibTable
ctpRS232PeripheralStatusTable=_CtpRS232PeripheralStatusTable_Object((1,3,6,1,4,1,9,9,643,1,2,5))
if mibBuilder.loadTexts:ctpRS232PeripheralStatusTable.setStatus(_B)
_CtpRS232PeripheralStatusEntry_Object=MibTableRow
ctpRS232PeripheralStatusEntry=_CtpRS232PeripheralStatusEntry_Object((1,3,6,1,4,1,9,9,643,1,2,5,1))
ctpRS232PeripheralStatusEntry.setIndexNames((0,_A,_F),(0,_A,_A5))
if mibBuilder.loadTexts:ctpRS232PeripheralStatusEntry.setStatus(_B)
_CtpRS232PeripheralIndex_Type=Unsigned32
_CtpRS232PeripheralIndex_Object=MibTableColumn
ctpRS232PeripheralIndex=_CtpRS232PeripheralIndex_Object((1,3,6,1,4,1,9,9,643,1,2,5,1,1),_CtpRS232PeripheralIndex_Type())
ctpRS232PeripheralIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpRS232PeripheralIndex.setStatus(_B)
_CtpRS232PortIndex_Type=InterfaceIndexOrZero
_CtpRS232PortIndex_Object=MibTableColumn
ctpRS232PortIndex=_CtpRS232PortIndex_Object((1,3,6,1,4,1,9,9,643,1,2,5,1,2),_CtpRS232PortIndex_Type())
ctpRS232PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpRS232PortIndex.setStatus(_B)
class _CtpRS232PeripheralConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),(_L,2)))
_CtpRS232PeripheralConnStatus_Type.__name__=_I
_CtpRS232PeripheralConnStatus_Object=MibTableColumn
ctpRS232PeripheralConnStatus=_CtpRS232PeripheralConnStatus_Object((1,3,6,1,4,1,9,9,643,1,2,5,1,3),_CtpRS232PeripheralConnStatus_Type())
ctpRS232PeripheralConnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpRS232PeripheralConnStatus.setStatus(_B)
_CtpPeripheralAttributeTable_Object=MibTable
ctpPeripheralAttributeTable=_CtpPeripheralAttributeTable_Object((1,3,6,1,4,1,9,9,643,1,2,6))
if mibBuilder.loadTexts:ctpPeripheralAttributeTable.setStatus(_B)
_CtpPeripheralAttributeEntry_Object=MibTableRow
ctpPeripheralAttributeEntry=_CtpPeripheralAttributeEntry_Object((1,3,6,1,4,1,9,9,643,1,2,6,1))
ctpPeripheralAttributeEntry.setIndexNames((0,_A,_F),(0,_A,_A6))
if mibBuilder.loadTexts:ctpPeripheralAttributeEntry.setStatus(_B)
_CtpPeripheralAttributeIndex_Type=Unsigned32
_CtpPeripheralAttributeIndex_Object=MibTableColumn
ctpPeripheralAttributeIndex=_CtpPeripheralAttributeIndex_Object((1,3,6,1,4,1,9,9,643,1,2,6,1,1),_CtpPeripheralAttributeIndex_Type())
ctpPeripheralAttributeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpPeripheralAttributeIndex.setStatus(_B)
class _CtpPeripheralAttributeDescr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lampOperTime',1),('lampState',2),('powerSwitchState',3)))
_CtpPeripheralAttributeDescr_Type.__name__=_I
_CtpPeripheralAttributeDescr_Object=MibTableColumn
ctpPeripheralAttributeDescr=_CtpPeripheralAttributeDescr_Object((1,3,6,1,4,1,9,9,643,1,2,6,1,2),_CtpPeripheralAttributeDescr_Type())
ctpPeripheralAttributeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralAttributeDescr.setStatus(_B)
_CtpPeripheralAttributeValue_Type=Unsigned32
_CtpPeripheralAttributeValue_Object=MibTableColumn
ctpPeripheralAttributeValue=_CtpPeripheralAttributeValue_Object((1,3,6,1,4,1,9,9,643,1,2,6,1,3),_CtpPeripheralAttributeValue_Type())
ctpPeripheralAttributeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralAttributeValue.setStatus(_B)
_CtpUSBPeripheralStatusTable_Object=MibTable
ctpUSBPeripheralStatusTable=_CtpUSBPeripheralStatusTable_Object((1,3,6,1,4,1,9,9,643,1,2,7))
if mibBuilder.loadTexts:ctpUSBPeripheralStatusTable.setStatus(_B)
_CtpUSBPeripheralStatusEntry_Object=MibTableRow
ctpUSBPeripheralStatusEntry=_CtpUSBPeripheralStatusEntry_Object((1,3,6,1,4,1,9,9,643,1,2,7,1))
ctpUSBPeripheralStatusEntry.setIndexNames((0,_A,_F),(0,_A,_A7))
if mibBuilder.loadTexts:ctpUSBPeripheralStatusEntry.setStatus(_B)
_CtpUSBPeripheralIndex_Type=Unsigned32
_CtpUSBPeripheralIndex_Object=MibTableColumn
ctpUSBPeripheralIndex=_CtpUSBPeripheralIndex_Object((1,3,6,1,4,1,9,9,643,1,2,7,1,1),_CtpUSBPeripheralIndex_Type())
ctpUSBPeripheralIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpUSBPeripheralIndex.setStatus(_B)
_CtpUSBPeripheralCableStatus_Type=CtpPeripheralCableCode
_CtpUSBPeripheralCableStatus_Object=MibTableColumn
ctpUSBPeripheralCableStatus=_CtpUSBPeripheralCableStatus_Object((1,3,6,1,4,1,9,9,643,1,2,7,1,2),_CtpUSBPeripheralCableStatus_Type())
ctpUSBPeripheralCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpUSBPeripheralCableStatus.setStatus(_B)
class _CtpUSBPeripheralPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('self',2),('bus',3),('both',4)))
_CtpUSBPeripheralPowerStatus_Type.__name__=_I
_CtpUSBPeripheralPowerStatus_Object=MibTableColumn
ctpUSBPeripheralPowerStatus=_CtpUSBPeripheralPowerStatus_Object((1,3,6,1,4,1,9,9,643,1,2,7,1,3),_CtpUSBPeripheralPowerStatus_Type())
ctpUSBPeripheralPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpUSBPeripheralPowerStatus.setStatus(_B)
class _CtpUSBPeripheralPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('host',1),('device',2),('hub',3)))
_CtpUSBPeripheralPortType_Type.__name__=_I
_CtpUSBPeripheralPortType_Object=MibTableColumn
ctpUSBPeripheralPortType=_CtpUSBPeripheralPortType_Object((1,3,6,1,4,1,9,9,643,1,2,7,1,4),_CtpUSBPeripheralPortType_Type())
ctpUSBPeripheralPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpUSBPeripheralPortType.setStatus(_B)
class _CtpUSBPeripheralPortRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('full',2),('high',3)))
_CtpUSBPeripheralPortRate_Type.__name__=_I
_CtpUSBPeripheralPortRate_Object=MibTableColumn
ctpUSBPeripheralPortRate=_CtpUSBPeripheralPortRate_Object((1,3,6,1,4,1,9,9,643,1,2,7,1,5),_CtpUSBPeripheralPortRate_Type())
ctpUSBPeripheralPortRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpUSBPeripheralPortRate.setStatus(_B)
_Ctp802dot11PeripheralStatusTable_Object=MibTable
ctp802dot11PeripheralStatusTable=_Ctp802dot11PeripheralStatusTable_Object((1,3,6,1,4,1,9,9,643,1,2,8))
if mibBuilder.loadTexts:ctp802dot11PeripheralStatusTable.setStatus(_B)
_Ctp802dot11PeripheralStatusEntry_Object=MibTableRow
ctp802dot11PeripheralStatusEntry=_Ctp802dot11PeripheralStatusEntry_Object((1,3,6,1,4,1,9,9,643,1,2,8,1))
ctp802dot11PeripheralStatusEntry.setIndexNames((0,_A,_F),(0,_A,_A8))
if mibBuilder.loadTexts:ctp802dot11PeripheralStatusEntry.setStatus(_B)
_Ctp802dot11PeripheralIndex_Type=Unsigned32
_Ctp802dot11PeripheralIndex_Object=MibTableColumn
ctp802dot11PeripheralIndex=_Ctp802dot11PeripheralIndex_Object((1,3,6,1,4,1,9,9,643,1,2,8,1,1),_Ctp802dot11PeripheralIndex_Type())
ctp802dot11PeripheralIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctp802dot11PeripheralIndex.setStatus(_B)
_Ctp802dot11PeripheralIfIndex_Type=InterfaceIndexOrZero
_Ctp802dot11PeripheralIfIndex_Object=MibTableColumn
ctp802dot11PeripheralIfIndex=_Ctp802dot11PeripheralIfIndex_Object((1,3,6,1,4,1,9,9,643,1,2,8,1,2),_Ctp802dot11PeripheralIfIndex_Type())
ctp802dot11PeripheralIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctp802dot11PeripheralIfIndex.setStatus(_B)
_Ctp802dot11PeripheralAddrType_Type=InetAddressType
_Ctp802dot11PeripheralAddrType_Object=MibTableColumn
ctp802dot11PeripheralAddrType=_Ctp802dot11PeripheralAddrType_Object((1,3,6,1,4,1,9,9,643,1,2,8,1,3),_Ctp802dot11PeripheralAddrType_Type())
ctp802dot11PeripheralAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctp802dot11PeripheralAddrType.setStatus(_B)
_Ctp802dot11PeripheralAddr_Type=InetAddress
_Ctp802dot11PeripheralAddr_Object=MibTableColumn
ctp802dot11PeripheralAddr=_Ctp802dot11PeripheralAddr_Object((1,3,6,1,4,1,9,9,643,1,2,8,1,4),_Ctp802dot11PeripheralAddr_Type())
ctp802dot11PeripheralAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctp802dot11PeripheralAddr.setStatus(_B)
_Ctp802dot11PeripheralLinkStrength_Type=Unsigned32
_Ctp802dot11PeripheralLinkStrength_Object=MibTableColumn
ctp802dot11PeripheralLinkStrength=_Ctp802dot11PeripheralLinkStrength_Object((1,3,6,1,4,1,9,9,643,1,2,8,1,5),_Ctp802dot11PeripheralLinkStrength_Type())
ctp802dot11PeripheralLinkStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:ctp802dot11PeripheralLinkStrength.setStatus(_B)
_Ctp802dot11PeripheralLinkStatus_Type=CtpPeripheralCableCode
_Ctp802dot11PeripheralLinkStatus_Object=MibTableColumn
ctp802dot11PeripheralLinkStatus=_Ctp802dot11PeripheralLinkStatus_Object((1,3,6,1,4,1,9,9,643,1,2,8,1,6),_Ctp802dot11PeripheralLinkStatus_Type())
ctp802dot11PeripheralLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctp802dot11PeripheralLinkStatus.setStatus(_B)
_CtpDPPeripheralStatusTable_Object=MibTable
ctpDPPeripheralStatusTable=_CtpDPPeripheralStatusTable_Object((1,3,6,1,4,1,9,9,643,1,2,9))
if mibBuilder.loadTexts:ctpDPPeripheralStatusTable.setStatus(_B)
_CtpDPPeripheralStatusEntry_Object=MibTableRow
ctpDPPeripheralStatusEntry=_CtpDPPeripheralStatusEntry_Object((1,3,6,1,4,1,9,9,643,1,2,9,1))
ctpDPPeripheralStatusEntry.setIndexNames((0,_A,_F),(0,_A,_A9))
if mibBuilder.loadTexts:ctpDPPeripheralStatusEntry.setStatus(_B)
_CtpDPPeripheralIndex_Type=Unsigned32
_CtpDPPeripheralIndex_Object=MibTableColumn
ctpDPPeripheralIndex=_CtpDPPeripheralIndex_Object((1,3,6,1,4,1,9,9,643,1,2,9,1,1),_CtpDPPeripheralIndex_Type())
ctpDPPeripheralIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpDPPeripheralIndex.setStatus(_B)
_CtpDPPeripheralCableStatus_Type=CtpPeripheralCableCode
_CtpDPPeripheralCableStatus_Object=MibTableColumn
ctpDPPeripheralCableStatus=_CtpDPPeripheralCableStatus_Object((1,3,6,1,4,1,9,9,643,1,2,9,1,2),_CtpDPPeripheralCableStatus_Type())
ctpDPPeripheralCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpDPPeripheralCableStatus.setStatus(_B)
_CtpDPPeripheralPowerStatus_Type=CtpPeripheralPowerCode
_CtpDPPeripheralPowerStatus_Object=MibTableColumn
ctpDPPeripheralPowerStatus=_CtpDPPeripheralPowerStatus_Object((1,3,6,1,4,1,9,9,643,1,2,9,1,3),_CtpDPPeripheralPowerStatus_Type())
ctpDPPeripheralPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpDPPeripheralPowerStatus.setStatus(_B)
_CtpEventHistory_ObjectIdentity=ObjectIdentity
ctpEventHistory=_CtpEventHistory_ObjectIdentity((1,3,6,1,4,1,9,9,643,1,3))
class _CtpPeripheralErrorHistTableSize_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CtpPeripheralErrorHistTableSize_Type.__name__=_H
_CtpPeripheralErrorHistTableSize_Object=MibScalar
ctpPeripheralErrorHistTableSize=_CtpPeripheralErrorHistTableSize_Object((1,3,6,1,4,1,9,9,643,1,3,1),_CtpPeripheralErrorHistTableSize_Type())
ctpPeripheralErrorHistTableSize.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpPeripheralErrorHistTableSize.setStatus(_B)
class _CtpPeripheralErrorHistLastIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CtpPeripheralErrorHistLastIndex_Type.__name__=_H
_CtpPeripheralErrorHistLastIndex_Object=MibScalar
ctpPeripheralErrorHistLastIndex=_CtpPeripheralErrorHistLastIndex_Object((1,3,6,1,4,1,9,9,643,1,3,2),_CtpPeripheralErrorHistLastIndex_Type())
ctpPeripheralErrorHistLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralErrorHistLastIndex.setStatus(_B)
_CtpPeripheralErrorHistoryTable_Object=MibTable
ctpPeripheralErrorHistoryTable=_CtpPeripheralErrorHistoryTable_Object((1,3,6,1,4,1,9,9,643,1,3,3))
if mibBuilder.loadTexts:ctpPeripheralErrorHistoryTable.setStatus(_B)
_CtpPeripheralErrorHistoryEntry_Object=MibTableRow
ctpPeripheralErrorHistoryEntry=_CtpPeripheralErrorHistoryEntry_Object((1,3,6,1,4,1,9,9,643,1,3,3,1))
ctpPeripheralErrorHistoryEntry.setIndexNames((0,_A,_AA))
if mibBuilder.loadTexts:ctpPeripheralErrorHistoryEntry.setStatus(_B)
class _CtpPeripheralErrorHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CtpPeripheralErrorHistoryIndex_Type.__name__=_H
_CtpPeripheralErrorHistoryIndex_Object=MibTableColumn
ctpPeripheralErrorHistoryIndex=_CtpPeripheralErrorHistoryIndex_Object((1,3,6,1,4,1,9,9,643,1,3,3,1,1),_CtpPeripheralErrorHistoryIndex_Type())
ctpPeripheralErrorHistoryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpPeripheralErrorHistoryIndex.setStatus(_B)
_CtpPeripheralErrorIndex_Type=Unsigned32
_CtpPeripheralErrorIndex_Object=MibTableColumn
ctpPeripheralErrorIndex=_CtpPeripheralErrorIndex_Object((1,3,6,1,4,1,9,9,643,1,3,3,1,2),_CtpPeripheralErrorIndex_Type())
ctpPeripheralErrorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralErrorIndex.setStatus(_B)
_CtpPeripheralErrorStatus_Type=CtpPeripheralStatusCode
_CtpPeripheralErrorStatus_Object=MibTableColumn
ctpPeripheralErrorStatus=_CtpPeripheralErrorStatus_Object((1,3,6,1,4,1,9,9,643,1,3,3,1,3),_CtpPeripheralErrorStatus_Type())
ctpPeripheralErrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralErrorStatus.setStatus(_B)
_CtpPeripheralErrorTimeStamp_Type=TimeStamp
_CtpPeripheralErrorTimeStamp_Object=MibTableColumn
ctpPeripheralErrorTimeStamp=_CtpPeripheralErrorTimeStamp_Object((1,3,6,1,4,1,9,9,643,1,3,3,1,4),_CtpPeripheralErrorTimeStamp_Type())
ctpPeripheralErrorTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralErrorTimeStamp.setStatus(_B)
_CtpPeripheralErrorDeviceCategory_Type=CtpPeripheralDeviceCategoryCode
_CtpPeripheralErrorDeviceCategory_Object=MibTableColumn
ctpPeripheralErrorDeviceCategory=_CtpPeripheralErrorDeviceCategory_Object((1,3,6,1,4,1,9,9,643,1,3,3,1,5),_CtpPeripheralErrorDeviceCategory_Type())
ctpPeripheralErrorDeviceCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralErrorDeviceCategory.setStatus(_B)
_CtpPeripheralErrorDeviceNumber_Type=Unsigned32
_CtpPeripheralErrorDeviceNumber_Object=MibTableColumn
ctpPeripheralErrorDeviceNumber=_CtpPeripheralErrorDeviceNumber_Object((1,3,6,1,4,1,9,9,643,1,3,3,1,6),_CtpPeripheralErrorDeviceNumber_Type())
ctpPeripheralErrorDeviceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpPeripheralErrorDeviceNumber.setStatus(_B)
class _CtpSysUserAuthFailHistTableSize_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CtpSysUserAuthFailHistTableSize_Type.__name__=_H
_CtpSysUserAuthFailHistTableSize_Object=MibScalar
ctpSysUserAuthFailHistTableSize=_CtpSysUserAuthFailHistTableSize_Object((1,3,6,1,4,1,9,9,643,1,3,4),_CtpSysUserAuthFailHistTableSize_Type())
ctpSysUserAuthFailHistTableSize.setMaxAccess(_G)
if mibBuilder.loadTexts:ctpSysUserAuthFailHistTableSize.setStatus(_B)
class _CtpSysUserAuthFailHistLastIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CtpSysUserAuthFailHistLastIndex_Type.__name__=_H
_CtpSysUserAuthFailHistLastIndex_Object=MibScalar
ctpSysUserAuthFailHistLastIndex=_CtpSysUserAuthFailHistLastIndex_Object((1,3,6,1,4,1,9,9,643,1,3,5),_CtpSysUserAuthFailHistLastIndex_Type())
ctpSysUserAuthFailHistLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpSysUserAuthFailHistLastIndex.setStatus(_B)
_CtpSysUserAuthFailHistoryTable_Object=MibTable
ctpSysUserAuthFailHistoryTable=_CtpSysUserAuthFailHistoryTable_Object((1,3,6,1,4,1,9,9,643,1,3,6))
if mibBuilder.loadTexts:ctpSysUserAuthFailHistoryTable.setStatus(_B)
_CtpSysUserAuthFailHistoryEntry_Object=MibTableRow
ctpSysUserAuthFailHistoryEntry=_CtpSysUserAuthFailHistoryEntry_Object((1,3,6,1,4,1,9,9,643,1,3,6,1))
ctpSysUserAuthFailHistoryEntry.setIndexNames((0,_A,_AB))
if mibBuilder.loadTexts:ctpSysUserAuthFailHistoryEntry.setStatus(_B)
class _CtpSysUserAuthFailHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CtpSysUserAuthFailHistoryIndex_Type.__name__=_H
_CtpSysUserAuthFailHistoryIndex_Object=MibTableColumn
ctpSysUserAuthFailHistoryIndex=_CtpSysUserAuthFailHistoryIndex_Object((1,3,6,1,4,1,9,9,643,1,3,6,1,1),_CtpSysUserAuthFailHistoryIndex_Type())
ctpSysUserAuthFailHistoryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctpSysUserAuthFailHistoryIndex.setStatus(_B)
_CtpSysUserAuthFailSourceAddrType_Type=InetAddressType
_CtpSysUserAuthFailSourceAddrType_Object=MibTableColumn
ctpSysUserAuthFailSourceAddrType=_CtpSysUserAuthFailSourceAddrType_Object((1,3,6,1,4,1,9,9,643,1,3,6,1,2),_CtpSysUserAuthFailSourceAddrType_Type())
ctpSysUserAuthFailSourceAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpSysUserAuthFailSourceAddrType.setStatus(_B)
_CtpSysUserAuthFailSourceAddr_Type=InetAddress
_CtpSysUserAuthFailSourceAddr_Object=MibTableColumn
ctpSysUserAuthFailSourceAddr=_CtpSysUserAuthFailSourceAddr_Object((1,3,6,1,4,1,9,9,643,1,3,6,1,3),_CtpSysUserAuthFailSourceAddr_Type())
ctpSysUserAuthFailSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpSysUserAuthFailSourceAddr.setStatus(_B)
_CtpSysUserAuthFailSourcePort_Type=Unsigned32
_CtpSysUserAuthFailSourcePort_Object=MibTableColumn
ctpSysUserAuthFailSourcePort=_CtpSysUserAuthFailSourcePort_Object((1,3,6,1,4,1,9,9,643,1,3,6,1,4),_CtpSysUserAuthFailSourcePort_Type())
ctpSysUserAuthFailSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpSysUserAuthFailSourcePort.setStatus(_B)
class _CtpSysUserAuthFailUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CtpSysUserAuthFailUserName_Type.__name__=_h
_CtpSysUserAuthFailUserName_Object=MibTableColumn
ctpSysUserAuthFailUserName=_CtpSysUserAuthFailUserName_Object((1,3,6,1,4,1,9,9,643,1,3,6,1,5),_CtpSysUserAuthFailUserName_Type())
ctpSysUserAuthFailUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpSysUserAuthFailUserName.setStatus(_B)
_CtpSysUserAuthFailAccessProtocol_Type=CtpSystemAccessProtocol
_CtpSysUserAuthFailAccessProtocol_Object=MibTableColumn
ctpSysUserAuthFailAccessProtocol=_CtpSysUserAuthFailAccessProtocol_Object((1,3,6,1,4,1,9,9,643,1,3,6,1,6),_CtpSysUserAuthFailAccessProtocol_Type())
ctpSysUserAuthFailAccessProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpSysUserAuthFailAccessProtocol.setStatus(_B)
_CtpSysUserAuthFailTimeStamp_Type=TimeStamp
_CtpSysUserAuthFailTimeStamp_Object=MibTableColumn
ctpSysUserAuthFailTimeStamp=_CtpSysUserAuthFailTimeStamp_Object((1,3,6,1,4,1,9,9,643,1,3,6,1,7),_CtpSysUserAuthFailTimeStamp_Type())
ctpSysUserAuthFailTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpSysUserAuthFailTimeStamp.setStatus(_B)
_CiscoTelepresenceMIBConform_ObjectIdentity=ObjectIdentity
ciscoTelepresenceMIBConform=_CiscoTelepresenceMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,643,2))
_CiscoTelepresenceCompliances_ObjectIdentity=ObjectIdentity
ciscoTelepresenceCompliances=_CiscoTelepresenceCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,643,2,1))
_CiscoTelepresenceMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTelepresenceMIBGroups=_CiscoTelepresenceMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,643,2,2))
ciscoTpConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,1))
ciscoTpConfigurationGroup.setObjects(*((_A,_AC),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoTpConfigurationGroup.setStatus(_D)
ciscoTpPeripheralStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,2))
ciscoTpPeripheralStatusGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoTpPeripheralStatusGroup.setStatus(_D)
ciscoTpEventHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,3))
ciscoTpEventHistoryGroup.setObjects(*((_A,_k),(_A,_l),(_A,_M),(_A,_N),(_A,_m),(_A,_n),(_A,_o),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_p)))
if mibBuilder.loadTexts:ciscoTpEventHistoryGroup.setStatus(_D)
ciscoTpRS232PeripheralStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,5))
ciscoTpRS232PeripheralStatusGroup.setObjects(*((_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ciscoTpRS232PeripheralStatusGroup.setStatus(_B)
ciscoTpPeripheralAttributeGroup=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,6))
ciscoTpPeripheralAttributeGroup.setObjects(*((_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:ciscoTpPeripheralAttributeGroup.setStatus(_B)
ciscoTpPeripheralStatusGroupR01=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,7))
ciscoTpPeripheralStatusGroupR01.setObjects(*((_A,_S),(_A,_T),(_A,_q),(_A,_r),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoTpPeripheralStatusGroupR01.setStatus(_D)
ciscoTpEventHistoryGroupR01=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,8))
ciscoTpEventHistoryGroupR01.setObjects(*((_A,_k),(_A,_l),(_A,_M),(_A,_N),(_A,_m),(_A,_s),(_A,_t),(_A,_n),(_A,_o),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_p)))
if mibBuilder.loadTexts:ciscoTpEventHistoryGroupR01.setStatus(_B)
ciscoTpConfigurationGroupR01=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,10))
ciscoTpConfigurationGroupR01.setObjects(*((_A,_i),(_A,_j),(_A,_AH)))
if mibBuilder.loadTexts:ciscoTpConfigurationGroupR01.setStatus(_B)
ciscoTpPeripheralStatusGroupR02=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,11))
ciscoTpPeripheralStatusGroupR02.setObjects(*((_A,_S),(_A,_T),(_A,_q),(_A,_r),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:ciscoTpPeripheralStatusGroupR02.setStatus(_B)
ciscoTpConfigurationGroupR02=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,12))
ciscoTpConfigurationGroupR02.setObjects(*((_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:ciscoTpConfigurationGroupR02.setStatus(_B)
ciscoTpDPPeripheralStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,643,2,2,13))
ciscoTpDPPeripheralStatusGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:ciscoTpDPPeripheralStatusGroup.setStatus(_B)
ctpPeripheralErrorNotification=NotificationType((1,3,6,1,4,1,9,9,643,0,1))
ctpPeripheralErrorNotification.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ctpPeripheralErrorNotification.setStatus(_D)
ctpSysUserAuthFailNotification=NotificationType((1,3,6,1,4,1,9,9,643,0,2))
ctpSysUserAuthFailNotification.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ctpSysUserAuthFailNotification.setStatus(_B)
ctpPeriStatusChangeNotification=NotificationType((1,3,6,1,4,1,9,9,643,0,3))
ctpPeriStatusChangeNotification.setObjects(*((_A,_M),(_A,_s),(_A,_t),(_A,_N)))
if mibBuilder.loadTexts:ctpPeriStatusChangeNotification.setStatus(_B)
ciscoTpNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,643,2,2,4))
ciscoTpNotificationGroup.setObjects(*((_A,_AW),(_A,_u)))
if mibBuilder.loadTexts:ciscoTpNotificationGroup.setStatus(_D)
ciscoTpNotificationGroupR01=NotificationGroup((1,3,6,1,4,1,9,9,643,2,2,9))
ciscoTpNotificationGroupR01.setObjects(*((_A,_AX),(_A,_u)))
if mibBuilder.loadTexts:ciscoTpNotificationGroupR01.setStatus(_B)
ciscoTelepresenceCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,643,2,1,1))
ciscoTelepresenceCompliance.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ciscoTelepresenceCompliance.setStatus(_D)
ciscoTelepresenceComplianceR01=ModuleCompliance((1,3,6,1,4,1,9,9,643,2,1,2))
ciscoTelepresenceComplianceR01.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoTelepresenceComplianceR01.setStatus(_D)
ciscoTelepresenceComplianceR02=ModuleCompliance((1,3,6,1,4,1,9,9,643,2,1,3))
ciscoTelepresenceComplianceR02.setObjects(*((_A,_O),(_A,_AY),(_A,_P),(_A,_Q),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoTelepresenceComplianceR02.setStatus(_D)
ciscoTelepresenceComplianceR03=ModuleCompliance((1,3,6,1,4,1,9,9,643,2,1,4))
ciscoTelepresenceComplianceR03.setObjects(*((_A,_O),(_A,_g),(_A,_P),(_A,_Q),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoTelepresenceComplianceR03.setStatus(_D)
ciscoTelepresenceComplianceR04=ModuleCompliance((1,3,6,1,4,1,9,9,643,2,1,5))
ciscoTelepresenceComplianceR04.setObjects(*((_A,_O),(_A,_z),(_A,_g),(_A,_P),(_A,_Q),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoTelepresenceComplianceR04.setStatus(_D)
ciscoTelepresenceComplianceR05=ModuleCompliance((1,3,6,1,4,1,9,9,643,2,1,6))
ciscoTelepresenceComplianceR05.setObjects(*((_A,_O),(_A,_z),(_A,_g),(_A,_P),(_A,_Q),(_A,_AZ),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoTelepresenceComplianceR05.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_A1:CtpSystemResetMode,'CtpPeripheralCableCode':CtpPeripheralCableCode,'CtpPeripheralPowerCode':CtpPeripheralPowerCode,'CtpPeripheralStatusCode':CtpPeripheralStatusCode,'CtpSystemAccessProtocol':CtpSystemAccessProtocol,'CtpPeripheralDeviceCategoryCode':CtpPeripheralDeviceCategoryCode,'ciscoTelepresenceMIB':ciscoTelepresenceMIB,'ciscoTelepresenceMIBNotifs':ciscoTelepresenceMIBNotifs,_AW:ctpPeripheralErrorNotification,_u:ctpSysUserAuthFailNotification,_AX:ctpPeriStatusChangeNotification,'ciscoTelepresenceMIBObjects':ciscoTelepresenceMIBObjects,'ctpObjects':ctpObjects,_AC:ctpPeripheralErrorNotifyEnable,_i:ctpSysUserAuthFailNotifyEnable,_j:ctpSystemReset,_AH:ctpPeriStatusChangeNotifyEnable,_AR:ctpVlanId,_AT:ctpDefaultGatewayAddrType,_AS:ctpDefaultGateway,'ctpPeripheralStatusObjects':ctpPeripheralStatusObjects,'ctpPeripheralStatusTable':ctpPeripheralStatusTable,'ctpPeripheralStatusEntry':ctpPeripheralStatusEntry,_F:ctpPeripheralIndex,_S:ctpPeripheralDescription,_T:ctpPeripheralStatus,_q:ctpPeripheralDeviceCategory,_r:ctpPeripheralDeviceNumber,'ctpEtherPeripheralStatusTable':ctpEtherPeripheralStatusTable,'ctpEtherPeripheralStatusEntry':ctpEtherPeripheralStatusEntry,_A2:ctpEtherPeripheralIndex,_U:ctpEtherPeripheralIfIndex,_V:ctpEtherPeripheralAddrType,_W:ctpEtherPeripheralAddr,_X:ctpEtherPeripheralStatus,'ctpHDMIPeripheralStatusTable':ctpHDMIPeripheralStatusTable,'ctpHDMIPeripheralStatusEntry':ctpHDMIPeripheralStatusEntry,_A3:ctpHDMIPeripheralIndex,_Y:ctpHDMIPeripheralCableStatus,_Z:ctpHDMIPeripheralPowerStatus,'ctpDVIPeripheralStatusTable':ctpDVIPeripheralStatusTable,'ctpDVIPeripheralStatusEntry':ctpDVIPeripheralStatusEntry,_A4:ctpDVIPeripheralIndex,_a:ctpDVIPeripheralCableStatus,'ctpRS232PeripheralStatusTable':ctpRS232PeripheralStatusTable,'ctpRS232PeripheralStatusEntry':ctpRS232PeripheralStatusEntry,_A5:ctpRS232PeripheralIndex,_AD:ctpRS232PortIndex,_AE:ctpRS232PeripheralConnStatus,'ctpPeripheralAttributeTable':ctpPeripheralAttributeTable,'ctpPeripheralAttributeEntry':ctpPeripheralAttributeEntry,_A6:ctpPeripheralAttributeIndex,_AF:ctpPeripheralAttributeDescr,_AG:ctpPeripheralAttributeValue,'ctpUSBPeripheralStatusTable':ctpUSBPeripheralStatusTable,'ctpUSBPeripheralStatusEntry':ctpUSBPeripheralStatusEntry,_A7:ctpUSBPeripheralIndex,_AI:ctpUSBPeripheralCableStatus,_AJ:ctpUSBPeripheralPowerStatus,_AK:ctpUSBPeripheralPortType,_AL:ctpUSBPeripheralPortRate,'ctp802dot11PeripheralStatusTable':ctp802dot11PeripheralStatusTable,'ctp802dot11PeripheralStatusEntry':ctp802dot11PeripheralStatusEntry,_A8:ctp802dot11PeripheralIndex,_AM:ctp802dot11PeripheralIfIndex,_AN:ctp802dot11PeripheralAddrType,_AO:ctp802dot11PeripheralAddr,_AP:ctp802dot11PeripheralLinkStrength,_AQ:ctp802dot11PeripheralLinkStatus,'ctpDPPeripheralStatusTable':ctpDPPeripheralStatusTable,'ctpDPPeripheralStatusEntry':ctpDPPeripheralStatusEntry,_A9:ctpDPPeripheralIndex,_AU:ctpDPPeripheralCableStatus,_AV:ctpDPPeripheralPowerStatus,'ctpEventHistory':ctpEventHistory,_k:ctpPeripheralErrorHistTableSize,_l:ctpPeripheralErrorHistLastIndex,'ctpPeripheralErrorHistoryTable':ctpPeripheralErrorHistoryTable,'ctpPeripheralErrorHistoryEntry':ctpPeripheralErrorHistoryEntry,_AA:ctpPeripheralErrorHistoryIndex,_M:ctpPeripheralErrorIndex,_N:ctpPeripheralErrorStatus,_m:ctpPeripheralErrorTimeStamp,_s:ctpPeripheralErrorDeviceCategory,_t:ctpPeripheralErrorDeviceNumber,_n:ctpSysUserAuthFailHistTableSize,_o:ctpSysUserAuthFailHistLastIndex,'ctpSysUserAuthFailHistoryTable':ctpSysUserAuthFailHistoryTable,'ctpSysUserAuthFailHistoryEntry':ctpSysUserAuthFailHistoryEntry,_AB:ctpSysUserAuthFailHistoryIndex,_b:ctpSysUserAuthFailSourceAddrType,_c:ctpSysUserAuthFailSourceAddr,_d:ctpSysUserAuthFailSourcePort,_e:ctpSysUserAuthFailUserName,_f:ctpSysUserAuthFailAccessProtocol,_p:ctpSysUserAuthFailTimeStamp,'ciscoTelepresenceMIBConform':ciscoTelepresenceMIBConform,'ciscoTelepresenceCompliances':ciscoTelepresenceCompliances,'ciscoTelepresenceCompliance':ciscoTelepresenceCompliance,'ciscoTelepresenceComplianceR01':ciscoTelepresenceComplianceR01,'ciscoTelepresenceComplianceR02':ciscoTelepresenceComplianceR02,'ciscoTelepresenceComplianceR03':ciscoTelepresenceComplianceR03,'ciscoTelepresenceComplianceR04':ciscoTelepresenceComplianceR04,'ciscoTelepresenceComplianceR05':ciscoTelepresenceComplianceR05,'ciscoTelepresenceMIBGroups':ciscoTelepresenceMIBGroups,_v:ciscoTpConfigurationGroup,_w:ciscoTpPeripheralStatusGroup,_x:ciscoTpEventHistoryGroup,_y:ciscoTpNotificationGroup,_J:ciscoTpRS232PeripheralStatusGroup,_K:ciscoTpPeripheralAttributeGroup,_AY:ciscoTpPeripheralStatusGroupR01,_P:ciscoTpEventHistoryGroupR01,_Q:ciscoTpNotificationGroupR01,_O:ciscoTpConfigurationGroupR01,_g:ciscoTpPeripheralStatusGroupR02,_z:ciscoTpConfigurationGroupR02,_AZ:ciscoTpDPPeripheralStatusGroup})