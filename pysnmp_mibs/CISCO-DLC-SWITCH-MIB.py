_A1='frasBanLlcGroup'
_A0='frasBanSdlcGroup'
_z='frasBnnLlcGroup'
_y='frasBnnSdlcGroup'
_x='banLlcConFrRemoteSap'
_w='banLlcConFrLocalSap'
_v='banLlcBniAddress'
_u='banLlcConFrInterface'
_t='banLlcConState'
_s='banLlcConDlci'
_r='banSdlcConFrRemoteSap'
_q='banSdlcConFrLocalSap'
_p='banSdlcConBniAddress'
_o='banSdlcConVmac'
_n='banSdlcConState'
_m='banSdlcConDlci'
_l='banSdlcConLocalInterface'
_k='bnnLlcConFrRemoteSap'
_j='bnnLlcConFrLocalSap'
_i='bnnLlcConLocalMacAddress'
_h='bnnLlcConState'
_g='bnnLlcConDlci'
_f='bnnLlcConLanInterface'
_e='bnnSdlcConRemoteSap'
_d='bnnSdlcConLocalSap'
_c='bnnSdlcConFRInterface'
_b='bnnSdlcConDlci'
_a='bnnSdlcConState'
_Z='bnnLlcConLanRemoteSap'
_Y='bnnLlcConLanLocalSap'
_X='bnnLlcConDeviceMacAddress'
_W='bnnSdlcConAddress'
_V='banLlcBanDlciMac'
_U='banLlcConRemoteSap'
_T='banLlcConLocalSap'
_S='banLlcEndstnLocalMac'
_R='banSdlcConBanDlciMac'
_Q='banSdlcConAddress'
_P='discwait'
_O='contacted'
_N='connrspsent'
_M='connrspwait'
_L='sigstnwait'
_K='connrqsent'
_J='xidexchg'
_I='testSent'
_H='reset'
_G='not-accessible'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='CISCO-DLC-SWITCH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndexOrZero',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ciscoDlcSwitchMIB=ModuleIdentity((1,3,6,1,4,1,9,9,76))
class SAP(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
class SdlcAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CiscoDlcSwitchMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDlcSwitchMIBObjects=_CiscoDlcSwitchMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,76,1))
_FrasBnnSdlc_ObjectIdentity=ObjectIdentity
frasBnnSdlc=_FrasBnnSdlc_ObjectIdentity((1,3,6,1,4,1,9,9,76,1,1))
_FrasBnnSdlcConTable_Object=MibTable
frasBnnSdlcConTable=_FrasBnnSdlcConTable_Object((1,3,6,1,4,1,9,9,76,1,1,1))
if mibBuilder.loadTexts:frasBnnSdlcConTable.setStatus(_A)
_FrasBnnSdlcConEntry_Object=MibTableRow
frasBnnSdlcConEntry=_FrasBnnSdlcConEntry_Object((1,3,6,1,4,1,9,9,76,1,1,1,1))
frasBnnSdlcConEntry.setIndexNames((0,_E,_F),(0,_B,_W))
if mibBuilder.loadTexts:frasBnnSdlcConEntry.setStatus(_A)
_BnnSdlcConAddress_Type=SdlcAddress
_BnnSdlcConAddress_Object=MibTableColumn
bnnSdlcConAddress=_BnnSdlcConAddress_Object((1,3,6,1,4,1,9,9,76,1,1,1,1,1),_BnnSdlcConAddress_Type())
bnnSdlcConAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:bnnSdlcConAddress.setStatus(_A)
class _BnnSdlcConState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9)))
_BnnSdlcConState_Type.__name__=_D
_BnnSdlcConState_Object=MibTableColumn
bnnSdlcConState=_BnnSdlcConState_Object((1,3,6,1,4,1,9,9,76,1,1,1,1,2),_BnnSdlcConState_Type())
bnnSdlcConState.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnSdlcConState.setStatus(_A)
class _BnnSdlcConDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1022))
_BnnSdlcConDlci_Type.__name__=_D
_BnnSdlcConDlci_Object=MibTableColumn
bnnSdlcConDlci=_BnnSdlcConDlci_Object((1,3,6,1,4,1,9,9,76,1,1,1,1,3),_BnnSdlcConDlci_Type())
bnnSdlcConDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnSdlcConDlci.setStatus(_A)
_BnnSdlcConFRInterface_Type=InterfaceIndexOrZero
_BnnSdlcConFRInterface_Object=MibTableColumn
bnnSdlcConFRInterface=_BnnSdlcConFRInterface_Object((1,3,6,1,4,1,9,9,76,1,1,1,1,4),_BnnSdlcConFRInterface_Type())
bnnSdlcConFRInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnSdlcConFRInterface.setStatus(_A)
_BnnSdlcConLocalSap_Type=SAP
_BnnSdlcConLocalSap_Object=MibTableColumn
bnnSdlcConLocalSap=_BnnSdlcConLocalSap_Object((1,3,6,1,4,1,9,9,76,1,1,1,1,5),_BnnSdlcConLocalSap_Type())
bnnSdlcConLocalSap.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnSdlcConLocalSap.setStatus(_A)
_BnnSdlcConRemoteSap_Type=SAP
_BnnSdlcConRemoteSap_Object=MibTableColumn
bnnSdlcConRemoteSap=_BnnSdlcConRemoteSap_Object((1,3,6,1,4,1,9,9,76,1,1,1,1,6),_BnnSdlcConRemoteSap_Type())
bnnSdlcConRemoteSap.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnSdlcConRemoteSap.setStatus(_A)
_FrasBnnLlc_ObjectIdentity=ObjectIdentity
frasBnnLlc=_FrasBnnLlc_ObjectIdentity((1,3,6,1,4,1,9,9,76,1,2))
_FrasBnnLlcConTable_Object=MibTable
frasBnnLlcConTable=_FrasBnnLlcConTable_Object((1,3,6,1,4,1,9,9,76,1,2,1))
if mibBuilder.loadTexts:frasBnnLlcConTable.setStatus(_A)
_FrasBnnLlcConEntry_Object=MibTableRow
frasBnnLlcConEntry=_FrasBnnLlcConEntry_Object((1,3,6,1,4,1,9,9,76,1,2,1,1))
frasBnnLlcConEntry.setIndexNames((0,_E,_F),(0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:frasBnnLlcConEntry.setStatus(_A)
_BnnLlcConDeviceMacAddress_Type=MacAddress
_BnnLlcConDeviceMacAddress_Object=MibTableColumn
bnnLlcConDeviceMacAddress=_BnnLlcConDeviceMacAddress_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,1),_BnnLlcConDeviceMacAddress_Type())
bnnLlcConDeviceMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:bnnLlcConDeviceMacAddress.setStatus(_A)
_BnnLlcConLanLocalSap_Type=SAP
_BnnLlcConLanLocalSap_Object=MibTableColumn
bnnLlcConLanLocalSap=_BnnLlcConLanLocalSap_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,2),_BnnLlcConLanLocalSap_Type())
bnnLlcConLanLocalSap.setMaxAccess(_G)
if mibBuilder.loadTexts:bnnLlcConLanLocalSap.setStatus(_A)
_BnnLlcConLanRemoteSap_Type=SAP
_BnnLlcConLanRemoteSap_Object=MibTableColumn
bnnLlcConLanRemoteSap=_BnnLlcConLanRemoteSap_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,3),_BnnLlcConLanRemoteSap_Type())
bnnLlcConLanRemoteSap.setMaxAccess(_G)
if mibBuilder.loadTexts:bnnLlcConLanRemoteSap.setStatus(_A)
_BnnLlcConLanInterface_Type=InterfaceIndexOrZero
_BnnLlcConLanInterface_Object=MibTableColumn
bnnLlcConLanInterface=_BnnLlcConLanInterface_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,4),_BnnLlcConLanInterface_Type())
bnnLlcConLanInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnLlcConLanInterface.setStatus(_A)
class _BnnLlcConDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1022))
_BnnLlcConDlci_Type.__name__=_D
_BnnLlcConDlci_Object=MibTableColumn
bnnLlcConDlci=_BnnLlcConDlci_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,5),_BnnLlcConDlci_Type())
bnnLlcConDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnLlcConDlci.setStatus(_A)
class _BnnLlcConState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9)))
_BnnLlcConState_Type.__name__=_D
_BnnLlcConState_Object=MibTableColumn
bnnLlcConState=_BnnLlcConState_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,6),_BnnLlcConState_Type())
bnnLlcConState.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnLlcConState.setStatus(_A)
_BnnLlcConLocalMacAddress_Type=MacAddress
_BnnLlcConLocalMacAddress_Object=MibTableColumn
bnnLlcConLocalMacAddress=_BnnLlcConLocalMacAddress_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,7),_BnnLlcConLocalMacAddress_Type())
bnnLlcConLocalMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnLlcConLocalMacAddress.setStatus(_A)
_BnnLlcConFrLocalSap_Type=SAP
_BnnLlcConFrLocalSap_Object=MibTableColumn
bnnLlcConFrLocalSap=_BnnLlcConFrLocalSap_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,8),_BnnLlcConFrLocalSap_Type())
bnnLlcConFrLocalSap.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnLlcConFrLocalSap.setStatus(_A)
_BnnLlcConFrRemoteSap_Type=SAP
_BnnLlcConFrRemoteSap_Object=MibTableColumn
bnnLlcConFrRemoteSap=_BnnLlcConFrRemoteSap_Object((1,3,6,1,4,1,9,9,76,1,2,1,1,9),_BnnLlcConFrRemoteSap_Type())
bnnLlcConFrRemoteSap.setMaxAccess(_C)
if mibBuilder.loadTexts:bnnLlcConFrRemoteSap.setStatus(_A)
_FrasBanSdlc_ObjectIdentity=ObjectIdentity
frasBanSdlc=_FrasBanSdlc_ObjectIdentity((1,3,6,1,4,1,9,9,76,1,3))
_FrasBanSdlcConTable_Object=MibTable
frasBanSdlcConTable=_FrasBanSdlcConTable_Object((1,3,6,1,4,1,9,9,76,1,3,1))
if mibBuilder.loadTexts:frasBanSdlcConTable.setStatus(_A)
_FrasBanSdlcConEntry_Object=MibTableRow
frasBanSdlcConEntry=_FrasBanSdlcConEntry_Object((1,3,6,1,4,1,9,9,76,1,3,1,1))
frasBanSdlcConEntry.setIndexNames((0,_E,_F),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:frasBanSdlcConEntry.setStatus(_A)
_BanSdlcConLocalInterface_Type=InterfaceIndexOrZero
_BanSdlcConLocalInterface_Object=MibTableColumn
banSdlcConLocalInterface=_BanSdlcConLocalInterface_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,1),_BanSdlcConLocalInterface_Type())
banSdlcConLocalInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConLocalInterface.setStatus(_A)
_BanSdlcConAddress_Type=SdlcAddress
_BanSdlcConAddress_Object=MibTableColumn
banSdlcConAddress=_BanSdlcConAddress_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,2),_BanSdlcConAddress_Type())
banSdlcConAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConAddress.setStatus(_A)
_BanSdlcConBanDlciMac_Type=MacAddress
_BanSdlcConBanDlciMac_Object=MibTableColumn
banSdlcConBanDlciMac=_BanSdlcConBanDlciMac_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,3),_BanSdlcConBanDlciMac_Type())
banSdlcConBanDlciMac.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConBanDlciMac.setStatus(_A)
class _BanSdlcConDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1022))
_BanSdlcConDlci_Type.__name__=_D
_BanSdlcConDlci_Object=MibTableColumn
banSdlcConDlci=_BanSdlcConDlci_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,4),_BanSdlcConDlci_Type())
banSdlcConDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConDlci.setStatus(_A)
class _BanSdlcConState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9)))
_BanSdlcConState_Type.__name__=_D
_BanSdlcConState_Object=MibTableColumn
banSdlcConState=_BanSdlcConState_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,5),_BanSdlcConState_Type())
banSdlcConState.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConState.setStatus(_A)
_BanSdlcConVmac_Type=MacAddress
_BanSdlcConVmac_Object=MibTableColumn
banSdlcConVmac=_BanSdlcConVmac_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,6),_BanSdlcConVmac_Type())
banSdlcConVmac.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConVmac.setStatus(_A)
_BanSdlcConBniAddress_Type=MacAddress
_BanSdlcConBniAddress_Object=MibTableColumn
banSdlcConBniAddress=_BanSdlcConBniAddress_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,7),_BanSdlcConBniAddress_Type())
banSdlcConBniAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConBniAddress.setStatus(_A)
_BanSdlcConFrLocalSap_Type=SAP
_BanSdlcConFrLocalSap_Object=MibTableColumn
banSdlcConFrLocalSap=_BanSdlcConFrLocalSap_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,8),_BanSdlcConFrLocalSap_Type())
banSdlcConFrLocalSap.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConFrLocalSap.setStatus(_A)
_BanSdlcConFrRemoteSap_Type=SAP
_BanSdlcConFrRemoteSap_Object=MibTableColumn
banSdlcConFrRemoteSap=_BanSdlcConFrRemoteSap_Object((1,3,6,1,4,1,9,9,76,1,3,1,1,9),_BanSdlcConFrRemoteSap_Type())
banSdlcConFrRemoteSap.setMaxAccess(_C)
if mibBuilder.loadTexts:banSdlcConFrRemoteSap.setStatus(_A)
_FrasBanLlc_ObjectIdentity=ObjectIdentity
frasBanLlc=_FrasBanLlc_ObjectIdentity((1,3,6,1,4,1,9,9,76,1,4))
_FrasBanLlcConTable_Object=MibTable
frasBanLlcConTable=_FrasBanLlcConTable_Object((1,3,6,1,4,1,9,9,76,1,4,1))
if mibBuilder.loadTexts:frasBanLlcConTable.setStatus(_A)
_FrasBanLlcConEntry_Object=MibTableRow
frasBanLlcConEntry=_FrasBanLlcConEntry_Object((1,3,6,1,4,1,9,9,76,1,4,1,1))
frasBanLlcConEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:frasBanLlcConEntry.setStatus(_A)
_BanLlcEndstnLocalMac_Type=MacAddress
_BanLlcEndstnLocalMac_Object=MibTableColumn
banLlcEndstnLocalMac=_BanLlcEndstnLocalMac_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,1),_BanLlcEndstnLocalMac_Type())
banLlcEndstnLocalMac.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcEndstnLocalMac.setStatus(_A)
_BanLlcBanDlciMac_Type=MacAddress
_BanLlcBanDlciMac_Object=MibTableColumn
banLlcBanDlciMac=_BanLlcBanDlciMac_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,2),_BanLlcBanDlciMac_Type())
banLlcBanDlciMac.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcBanDlciMac.setStatus(_A)
_BanLlcConLocalSap_Type=SAP
_BanLlcConLocalSap_Object=MibTableColumn
banLlcConLocalSap=_BanLlcConLocalSap_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,3),_BanLlcConLocalSap_Type())
banLlcConLocalSap.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcConLocalSap.setStatus(_A)
_BanLlcConRemoteSap_Type=SAP
_BanLlcConRemoteSap_Object=MibTableColumn
banLlcConRemoteSap=_BanLlcConRemoteSap_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,4),_BanLlcConRemoteSap_Type())
banLlcConRemoteSap.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcConRemoteSap.setStatus(_A)
class _BanLlcConDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1022))
_BanLlcConDlci_Type.__name__=_D
_BanLlcConDlci_Object=MibTableColumn
banLlcConDlci=_BanLlcConDlci_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,5),_BanLlcConDlci_Type())
banLlcConDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcConDlci.setStatus(_A)
class _BanLlcConState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9)))
_BanLlcConState_Type.__name__=_D
_BanLlcConState_Object=MibTableColumn
banLlcConState=_BanLlcConState_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,6),_BanLlcConState_Type())
banLlcConState.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcConState.setStatus(_A)
_BanLlcConFrInterface_Type=InterfaceIndexOrZero
_BanLlcConFrInterface_Object=MibTableColumn
banLlcConFrInterface=_BanLlcConFrInterface_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,7),_BanLlcConFrInterface_Type())
banLlcConFrInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcConFrInterface.setStatus(_A)
_BanLlcBniAddress_Type=MacAddress
_BanLlcBniAddress_Object=MibTableColumn
banLlcBniAddress=_BanLlcBniAddress_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,8),_BanLlcBniAddress_Type())
banLlcBniAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcBniAddress.setStatus(_A)
_BanLlcConFrLocalSap_Type=SAP
_BanLlcConFrLocalSap_Object=MibTableColumn
banLlcConFrLocalSap=_BanLlcConFrLocalSap_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,9),_BanLlcConFrLocalSap_Type())
banLlcConFrLocalSap.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcConFrLocalSap.setStatus(_A)
_BanLlcConFrRemoteSap_Type=SAP
_BanLlcConFrRemoteSap_Object=MibTableColumn
banLlcConFrRemoteSap=_BanLlcConFrRemoteSap_Object((1,3,6,1,4,1,9,9,76,1,4,1,1,10),_BanLlcConFrRemoteSap_Type())
banLlcConFrRemoteSap.setMaxAccess(_C)
if mibBuilder.loadTexts:banLlcConFrRemoteSap.setStatus(_A)
_CiscoDlcSwitchConformance_ObjectIdentity=ObjectIdentity
ciscoDlcSwitchConformance=_CiscoDlcSwitchConformance_ObjectIdentity((1,3,6,1,4,1,9,9,76,2))
_CiscoDlcSwitchCompliances_ObjectIdentity=ObjectIdentity
ciscoDlcSwitchCompliances=_CiscoDlcSwitchCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,76,2,1))
_CiscoDlcSwitchGroups_ObjectIdentity=ObjectIdentity
ciscoDlcSwitchGroups=_CiscoDlcSwitchGroups_ObjectIdentity((1,3,6,1,4,1,9,9,76,2,2))
frasBnnSdlcGroup=ObjectGroup((1,3,6,1,4,1,9,9,76,2,2,1))
frasBnnSdlcGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:frasBnnSdlcGroup.setStatus(_A)
frasBnnLlcGroup=ObjectGroup((1,3,6,1,4,1,9,9,76,2,2,2))
frasBnnLlcGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:frasBnnLlcGroup.setStatus(_A)
frasBanSdlcGroup=ObjectGroup((1,3,6,1,4,1,9,9,76,2,2,3))
frasBanSdlcGroup.setObjects(*((_B,_l),(_B,_Q),(_B,_R),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:frasBanSdlcGroup.setStatus(_A)
frasBanLlcGroup=ObjectGroup((1,3,6,1,4,1,9,9,76,2,2,4))
frasBanLlcGroup.setObjects(*((_B,_S),(_B,_V),(_B,_s),(_B,_T),(_B,_U),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:frasBanLlcGroup.setStatus(_A)
ciscoDlcSwitchCoreCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,76,2,1,1))
ciscoDlcSwitchCoreCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoDlcSwitchCoreCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SAP':SAP,'SdlcAddress':SdlcAddress,'ciscoDlcSwitchMIB':ciscoDlcSwitchMIB,'ciscoDlcSwitchMIBObjects':ciscoDlcSwitchMIBObjects,'frasBnnSdlc':frasBnnSdlc,'frasBnnSdlcConTable':frasBnnSdlcConTable,'frasBnnSdlcConEntry':frasBnnSdlcConEntry,_W:bnnSdlcConAddress,_a:bnnSdlcConState,_b:bnnSdlcConDlci,_c:bnnSdlcConFRInterface,_d:bnnSdlcConLocalSap,_e:bnnSdlcConRemoteSap,'frasBnnLlc':frasBnnLlc,'frasBnnLlcConTable':frasBnnLlcConTable,'frasBnnLlcConEntry':frasBnnLlcConEntry,_X:bnnLlcConDeviceMacAddress,_Y:bnnLlcConLanLocalSap,_Z:bnnLlcConLanRemoteSap,_f:bnnLlcConLanInterface,_g:bnnLlcConDlci,_h:bnnLlcConState,_i:bnnLlcConLocalMacAddress,_j:bnnLlcConFrLocalSap,_k:bnnLlcConFrRemoteSap,'frasBanSdlc':frasBanSdlc,'frasBanSdlcConTable':frasBanSdlcConTable,'frasBanSdlcConEntry':frasBanSdlcConEntry,_l:banSdlcConLocalInterface,_Q:banSdlcConAddress,_R:banSdlcConBanDlciMac,_m:banSdlcConDlci,_n:banSdlcConState,_o:banSdlcConVmac,_p:banSdlcConBniAddress,_q:banSdlcConFrLocalSap,_r:banSdlcConFrRemoteSap,'frasBanLlc':frasBanLlc,'frasBanLlcConTable':frasBanLlcConTable,'frasBanLlcConEntry':frasBanLlcConEntry,_S:banLlcEndstnLocalMac,_V:banLlcBanDlciMac,_T:banLlcConLocalSap,_U:banLlcConRemoteSap,_s:banLlcConDlci,_t:banLlcConState,_u:banLlcConFrInterface,_v:banLlcBniAddress,_w:banLlcConFrLocalSap,_x:banLlcConFrRemoteSap,'ciscoDlcSwitchConformance':ciscoDlcSwitchConformance,'ciscoDlcSwitchCompliances':ciscoDlcSwitchCompliances,'ciscoDlcSwitchCoreCompliance':ciscoDlcSwitchCoreCompliance,'ciscoDlcSwitchGroups':ciscoDlcSwitchGroups,_y:frasBnnSdlcGroup,_z:frasBnnLlcGroup,_A0:frasBanSdlcGroup,_A1:frasBanLlcGroup})